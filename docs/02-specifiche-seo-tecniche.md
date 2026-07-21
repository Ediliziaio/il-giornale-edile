# Specifiche Tecniche SEO / GEO / AEO — Il Giornale Edile

**Documento:** 02 · Specifiche implementate sul template in produzione
**Verificato al:** 21 luglio 2026 · Tutti gli esempi sono tratti dal codice reale

---

## 1. Convenzioni title e meta description

**Title** — pattern `<Keyword primaria>: <specificatore> | Il Giornale Edile`, target ≤ 60 caratteri.

| Pagina | Title reale | Lungh. |
|---|---|---|
| Pillar | `Pannelli Solari: Guida Completa 2026 \| Il Giornale Edile` | 47 |
| Articolo | `Ecobonus 2026: guida completa \| Il Giornale Edile` | 42 |
| Top 5 | `Pompe di Calore: le 5 Migliori del 2026 \| Il Giornale Edile` | 48 |
| Categoria | `Serramenti & Infissi — News e Guide \| Il Giornale Edile` | 52 |
| Home | `Il Giornale Edile — News, Bonus e Guide per l'Edilizia Italiana` | 58 |

**Meta description** — target ≤ 155 caratteri, verbo + promessa informativa + anno:

> `Pannelli solari e fotovoltaico: la guida completa 2026. Come funzionano, tipi, costi, detrazioni, permessi, dimensionamento, batterie, manutenzione e CER.` (148 char)

**Robots meta**: `index, follow, max-image-preview:large` su tutte le pagine indicizzabili
(home aggiunge `max-snippet:-1`). **Canonical** assoluto su ogni pagina, autoreferenziale.

## 2. Gerarchia dei titoli

- **Un solo H1 per pagina**, coincidente con `itemprop="headline"` (verificato: 49/49).
- Home: H1 assente di proposito — il brand è nel logo `img` con alt descrittivo; le sezioni usano H2.
  (Nota: valutare in futuro un H1 nascosto visivamente per la home.)
- Articoli: H1 → H2 di sezione con `id` per le ancore TOC → H3 interni. Sidebar e widget
  usano H3 (`w-title`), mai H2, per non inquinare l'outline del contenuto.
- Le H2 degli articoli sono **formulate come domande reali degli utenti**
  (es. `<h2 id="quanto-costano">Quanto costano i pannelli solari nel 2026?</h2>`).

## 3. Stack JSON-LD per tipo di pagina

### Home — `Organization` + `WebSite` + `SearchAction`

```json
{ "@type": "Organization", "@id": "https://www.ilgiornaleedile.it/#org",
  "name": "Il Giornale Edile",
  "logo": { "@type": "ImageObject", "url": ".../assets/logo.png" } },
{ "@type": "WebSite", "url": "https://www.ilgiornaleedile.it/",
  "potentialAction": { "@type": "SearchAction",
    "target": ".../cerca.html?q={search_term_string}" } }
```

### Articoli — `NewsArticle` + `BreadcrumbList` + `FAQPage`

```json
{ "@type": "NewsArticle",
  "headline": "Pannelli solari e fotovoltaico: la guida completa 2026",
  "inLanguage": "it-IT",
  "datePublished": "2026-07-20T09:00:00+02:00",
  "author": { "@type": "Person", "name": "Luca Brambilla",
              "jobTitle": "Giornalista edile" },
  "publisher": { "@type": "Organization", "name": "Il Giornale Edile", "logo": ... },
  "articleSection": "Energia & Rinnovabili",
  "keywords": "pannelli solari, fotovoltaico, incentivi fotovoltaico, ..." }
```

Più, nel body, microdata `itemscope itemtype="https://schema.org/NewsArticle"` con
`itemprop="headline"`, `itemprop="author"`, `itemprop="datePublished"`, `itemprop="articleBody"`.
Il `BreadcrumbList` replica il breadcrumb visibile; il `FAQPage` replica 1:1 le FAQ
renderizzate in `<details>/<summary>` (coerenza contenuto ↔ markup, niente FAQ nascoste).

### Categorie — `CollectionPage` + `BreadcrumbList`

Con `name`, `description`, `isPartOf: WebSite`. Pagine servizio: nessun JSON-LD superfluo.

## 4. Policy canonical e date

- Canonical autoreferenziale assoluto su tutte le 49 pagine; niente parametri, niente paginazioni.
- Date esposte tre volte in modo coerente: meta `article:published_time` / `article:modified_time`,
  `<time datetime itemprop="datePublished">` visibile, `datePublished/dateModified` in JSON-LD.
  Lo stesso valore alimenta `lastmod` di sitemap.xml al build.

## 5. Policy immagini

- Le immagini di contenuto sono **thumb CSS** (`figure.thumb`, `role="img"` + `aria-label`
  descrittivo, es. "Impianto di pannelli solari fotovoltaici sul tetto di una villetta
  italiana"): zero richieste immagine pesanti, LCP dominato dal testo hero.
- Le thumb hanno `aspect-ratio` dichiarato (`ar-16-9`, `ar-3-2`, `ar-1-1`): nessun reflow.
- Il logo è l'unica `<img>` critica: `width/height` attributi sempre presenti;
  in home `fetchpriority="high"` perché candidato LCP:
  `<img src="assets/logo.png" alt="Il Giornale Edile - Notizie di edilizia..." width="460" height="44" fetchpriority="high">`
- Se in futuro si aggiungono foto reali: `loading="lazy"` obbligatorio sotto la piega,
  `width/height` sempre, WebP/AVIF, alt descrittivo con contesto edilizio.

## 6. Ad slot e riserva di spazio (CLS)

Ogni slot pubblicitario ha **dimensioni minime riservate nel CSS** prima del caricamento
dell'ad network — il layout non si sposta quando il creativo arriva:

```css
.ad-leaderboard { width: min(970px,100%); min-height: 110px; }
.ad-rect        { width: 300px; min-height: 250px; }
.ad-halfpage    { width: 300px; min-height: 600px; }
.ad-mobile      { width: 320px; min-height: 100px; }
.ad-footer      { width: min(728px,100%); min-height: 90px; }
```

Su mobile l'half-page si riduce (`min-height: 250px`) via media query. Gli slot sono
marcati `role="complementary" aria-label="Spazio pubblicitario"` e mai iniettati nel body dell'articolo.

## 7. Core Web Vitals: target e come li raggiungiamo

| Metrica | Target | Meccanismi del template |
|---|---|---|
| LCP | < 2,5 s | HTML statico (nessun framework JS), CSS singolo, hero testuale, logo con `fetchpriority="high"`, font con `preconnect` + `display=swap` |
| INP | < 200 ms | Un solo script (`main.js`, `defer`), niente librerie di terze parti nel rendering path |
| CLS | < 0,1 | `aspect-ratio` sulle thumb, `min-height` sugli ad slot, dimensioni fisse su logo/immagini, font fallback metricamente vicini |

**Mobile-first**: viewport standard, layout a griglie fluide (`card-grid`, `cg-4`),
classe `mobile-only` per il banner 320×100, nav orizzontale a scroll naturale,
tap target testuali. Le pagine sono HTML statico: TTFB dipende solo dall'hosting.

## 8. robots.txt — policy AI crawler

`Allow: /` per `User-agent: *` più **gruppi Allow dedicati a 13 bot AI**:
GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, anthropic-ai,
PerplexityBot, Perplexity-User, Google-Extended, CCBot, Bytespider,
meta-externalagent, Applebot-Extended. Commento in testa che dichiara la policy
("testata che vuole essere citata dai motori AI") e due righe `Sitemap:`
(sitemap.xml + sitemap-news.xml).

## 9. Sitemap XML e News

- `sitemap.xml`: 49 URL, `lastmod` reale per gli articoli (da `article:modified_time`),
  priorità/changefreq graduate (home 1.0/daily → servizio 0.3/yearly).
- `sitemap-news.xml`: solo articoli delle ultime 48-72 h (attualmente 9 item, 19-21/07/2026),
  namespace `http://www.google.com/schemas/sitemap-news/0.9`, `news:name` "Il Giornale Edile",
  `news:language` "it", `news:publication_date` con timezone.
- `feed.xml` RSS 2.0 per lettori e aggregatori (20 item).

## 10. llms.txt

Indice markdown curato per i retrieval dei LLM: H1 con nome testata, blockquote di
posizionamento, sezioni "Guide pilastro" (pillar fotovoltaico primo), "Categorie",
"Ultimi articoli", "Informazioni editoriali" — 35 URL con descrizione one-line.
Scopo: massimizzare la probabilità che un agente AI trovi subito i contenuti canonicali.

## 11. Misure GEO (Generative Engine Optimization)

1. **Frasi fattuali citabili**: dati numerici completi di contesto nella stessa frase —
   es. "un impianto domestico da 6 kWp costa 7.500-11.000 euro chiavi in mano, si ripaga
   in 5-8 anni e produce per 30-40 anni".
2. **Answer box "In breve"** in apertura di ogni articolo (3-5 bullet autoconsistenti):
   blocco pronto per la citazione diretta.
3. **Structured data completo** (NewsArticle con autore Person + jobTitle, FAQPage).
4. **E-E-A-T**: firma d'autore su ogni articolo, pagina "Chi siamo" con la redazione e i
   ruoli (Marco Ferreri — bonus e fiscalità; Giulia Santi — normativa; Luca Brambilla —
   materiali; Sara Colombo — mercato; Giulia Marchetti — ristrutturazioni; Paolo Riva —
   cantieri), paragrafo "Fonti" a fine articolo con riferimenti ufficiali (Agenzia delle
   Entrate, ENEA, UNI, GSE).
5. **Disclaimer di indipendenza** nelle Top 5 ("selezione redazionale e indipendente:
   nessun produttore ha contribuito economicamente").
6. **llms.txt + robots AI-friendly**: la testata dichiara esplicitamente di voler essere citata.

## 12. Misure AEO (Answer Engine Optimization)

1. **Box risposta rapida** subito dopo la hero (`aside.key-takeaways`, commento nel codice:
   "ottimizzato per featured snippet e risposte AI").
2. **H2 a forma di domanda** con risposta nel primo paragrafo della sezione.
3. **FAQPage** con 4-6 domande in `<details>/<summary>`, markup JSON-LD allineato.
4. **Tabelle comparative** (`Tabella comparativa e costi reali al mq`) e **liste**:
   formati che i motori di risposta estraggono più facilmente.
5. **TOC con ancore** per deep-linking alle singole risposte.

## 13. Anatomia del template articolo (sezione per sezione)

```
breadcrumb (nav.breadcrumbs + JSON-LD BreadcrumbList)
kicker (span.kicker: "Energia & Rinnovabili · La guida completa")
H1 (itemprop="headline")
standfirst (itemprop="description" — sottotitolo 30-45 parole)
meta bar: autore (b-author) · data (time/itemprop) · tempo lettura · share (fb/linkedin/wa)
hero thumb (figure.thumb ar-16-9, role="img" aria-label)
ASIDE "IN BREVE" (key-takeaways — answer box AEO)
TOC (nav.toc — ol di ancore #id verso le H2)
CORPO: H2 con id (domande) → paragrafi, H3, tabelle, liste; link contestuali ai cluster
FAQ (h2#faq + details/summary + JSON-LD FAQPage)
FONTI (p.sources — riferimenti ufficiali + disclaimer prezzi)
TAG (div.tags — link alle categorie, mai a pagine tag)
CORRELATI (section.related "Leggi anche" — 4 card intra-silo/pillar)
SIDEBAR: ad half-page · widget "I più letti" · newsletter · ad rect
AD SLOT: leaderboard top, in-feed, footer (min-height riservata)
FOOTER: Sezioni (6 categorie) · Testata (Chi siamo/Contatti/Pubblicità/RSS/Mappa del sito) · legal
```

Snippet reali rappresentativi:

```html
<!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
<aside class="key-takeaways"><h2>In breve</h2><ul>…</ul></aside>

<nav class="toc" aria-label="Indice dell'articolo">
  <h2>Indice dei contenuti</h2>
  <ol><li><a href="#quanto-costano">Quanto costano i pannelli solari nel 2026?</a></li>…</ol>
</nav>

<div class="article-meta-bar">
  <span class="b-author" itemprop="author">di Luca Brambilla</span>
  <span>Pubblicato il <time datetime="2026-07-20T09:00:00+02:00"
        itemprop="datePublished">20 luglio 2026</time></span>
</div>
```
