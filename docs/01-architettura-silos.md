# Architettura a Silos — Il Giornale Edile

**Documento:** 01 · Mappa del sito e architettura informativa
**Dominio canonico:** `https://www.ilgiornaleedile.it`
**Stato:** produzione, verificato al 21 luglio 2026
**Inventario:** 49 pagine HTML (1 home, 6 categorie, 33 articoli, 8 pagine servizio + sitemap utente), 2 sitemap XML, feed RSS, robots.txt, llms.txt

---

## 1. Albero completo del sito

```
https://www.ilgiornaleedile.it/
├── index.html ............................ Home (hub di distribuzione verso i silos)
├── guide.html ............................ Hub "Guide & Top 5" (indice trasversale)
├── cerca.html ............................ Ricerca interna (target della SearchAction)
├── sitemap.html .......................... Mappa del sito utente (HTML)
│
├── categoria/bonus-fiscali.html .......... SILO 1 — Bonus & Fisco (5 articoli)
├── categoria/energia-rinnovabili.html .... SILO 2 — Energia & Rinnovabili (6 articoli)
├── categoria/normative-cantieri.html ..... SILO 3 — Normative & Cantieri (6 articoli)
├── categoria/materiali-tecnologie.html ... SILO 4 — Materiali & Tecnologie (7 articoli)
├── categoria/mercato-immobiliare.html .... SILO 5 — Mercato & Immobiliare (7 articoli)
├── categoria/serramenti-infissi.html ..... SILO 6 — Serramenti & Infissi (2 articoli)
│
├── articoli/*.html ....................... 33 articoli (foglie dei silos)
│
├── chi-siamo.html ........................ Testata + redazione (E-E-A-T)
├── contatti.html ......................... Contatti redazione
├── pubblicita.html ....................... Offerta commerciale
├── privacy.html / cookie-policy.html / note-legali.html
├── feed.xml .............................. RSS 2.0 (20 item)
├── sitemap.xml / sitemap-news.xml ........ Sitemap crawler + Google News
├── robots.txt / llms.txt ................. Policy crawler e indice per LLM
└── assets/ css/ js/ ...................... Statici (logo, favicon, style.css, main.js)
```

La categoria di appartenenza di ogni articolo è dichiarata nel meta `article:section`
ed è la **fonte unica di verità** usata dal build per generare pagine categoria,
breadcrumb e sitemap utente.

---

## 2. I sei silos e il loro contenuto

### SILO 1 — Bonus & Fisco (`/categoria/bonus-fiscali.html`)

| Articolo | URL |
|---|---|
| Bonus Ristrutturazione 2026: guida completa **(pillar fiscale)** | `/articoli/bonus-ristrutturazione-2026-guida-completa.html` |
| Ecobonus 2026: guida completa | `/articoli/ecobonus-65-guida.html` |
| Superbonus 2026: cosa resta | `/articoli/superbonus-2026-cosa-resta.html` |
| Detrazione 50% prima casa e 36% seconda casa | `/articoli/detrazioni-ristrutturazione-50-36.html` |
| Conto Termico 3.0: incentivi GSE | `/articoli/conto-termico-3-guida.html` |

### SILO 2 — Energia & Rinnovabili (`/categoria/energia-rinnovabili.html`)

| Articolo | URL |
|---|---|
| Pannelli solari e fotovoltaico: la guida completa 2026 **(pillar del sito)** | `/articoli/pannelli-solari-fotovoltaico-guida.html` |
| I 5 migliori fornitori di pannelli solari in Italia | `/articoli/top-5-fornitori-pannelli-solari.html` |
| Le 5 migliori pompe di calore del 2026 | `/articoli/top-5-pompe-di-calore.html` |
| Fotovoltaico sul tetto: costi, permessi e iter 2026 | `/articoli/fotovoltaico-costi-permessi-2026.html` |
| Comunità energetiche (CER): guida | `/articoli/comunita-energetiche-cer-guida.html` |
| Riscaldamento a pavimento: pro, contro e costi | `/articoli/riscaldamento-a-pavimento-pro-contro.html` |

### SILO 3 — Normative & Cantieri (`/categoria/normative-cantieri.html`)

`direttiva-case-green-cosa-cambia` · `codice-appalti-dlgs-36-2023` · `sicurezza-cantiere-dlgs-81-novita` ·
`ponteggi-norme-sicurezza` · `ntc-aggiornamenti-sismici` · `certificazione-ape-regole-2026`
(tutti in `/articoli/<slug>.html`)

### SILO 4 — Materiali & Tecnologie (`/categoria/materiali-tecnologie.html`)

`cappotto-termico-materiali-confronto` · `edilizia-legno-xlam` · `cemento-sostenibile-materiali` ·
`stampa-3d-edilizia` · `domotica-smart-home-ristrutturazione` · `bim-obbligatorio-scadenze` ·
`top-5-software-bim`

### SILO 5 — Mercato & Immobiliare (`/categoria/mercato-immobiliare.html`)

`mercato-immobiliare-2026-prezzi` · `costo-ristrutturazione-al-mq-2026` · `ristrutturazione-chiavi-in-mano` ·
`costruire-casa-prefabbricata-costi` · `mutui-green-casa-efficiente` · `rigenerazione-urbana-progetti-2026` ·
`top-5-imprese-costruzione-italia`

### SILO 6 — Serramenti & Infissi (`/categoria/serramenti-infissi.html`)

`infissi-pvc-alluminio-legno-confronto` · `top-5-produttori-serramenti`
(silo giovane, creato il 21/07/2026: priorità di espansione editoriale)

---

## 3. Struttura pillar → cluster

Il sito usa il modello **pillar page + cluster**: una guida madre esaustiva (4.000+ parole,
TOC a domande) copre il tema intero e rimanda agli articoli satellite che approfondiscono
una singola sotto-domanda.

### 3.1 Pillar principale: fotovoltaico

**Pillar:** `/articoli/pannelli-solari-fotovoltaico-guida.html`
(15.782 caratteri di corpo, 11 sezioni H2 a forma di domanda + FAQ)

| Sezione H2 del pillar (ancora TOC) | Articolo cluster che la approfondisce |
|---|---|
| `#quanto-costano` / `#permessi-iter` | `fotovoltaico-costi-permessi-2026.html` |
| `#incentivi-detrazioni` | `ecobonus-65-guida.html`, `detrazioni-ristrutturazione-50-36.html`, `conto-termico-3-guida.html` |
| `#migliori-marche` | `top-5-fornitori-pannelli-solari.html` |
| `#comunita-energetiche` | `comunita-energetiche-cer-guida.html` |
| `#case-green` | `direttiva-case-green-cosa-cambia.html` |
| `#accumulo-batterie` | **gap** — nessun articolo dedicato (in piano editoriale) |
| `#tipi-di-pannelli` | coperto nel pillar; espandibile con scheda tecnologie TOPCon/HJT |

Il pillar linka i cluster **sia nel corpo** (link contestuali, es. "rimandiamo alla guida
dedicata al fotovoltaico sul tetto: costi, permessi e iter 2026") **sia nella sezione
"Leggi anche"** (4 card finali).

### 3.2 Pillar secondario: bonus ristrutturazione

`/articoli/bonus-ristrutturazione-2026-guida-completa.html` → cluster:
`detrazioni-ristrutturazione-50-36.html`, `ecobonus-65-guida.html`,
`superbonus-2026-cosa-resta.html`, `conto-termico-3-guida.html`,
`costo-ristrutturazione-al-mq-2026.html`.

### 3.3 Stato attuale dei backlink cluster → pillar

Verifica sul grafo di link estratto dai 33 articoli: il pillar riceve link dalla home
(hero-side, sezione Energia, "I più letti") e dalle pagine categoria/guide, ma **nessun
articolo cluster linka attualmente il pillar con anchor descrittiva**. Regola da applicare
ai prossimi aggiornamenti: ogni cluster del silo fotovoltaico deve includere nel primo
terzo del corpo un link contestuale al pillar (es. "come spiegato nella nostra guida
completa ai pannelli solari").

---

## 4. Regole di naming delle URL

1. **Parlanti**: lo slug descrive il contenuto (`infissi-pvc-alluminio-legno-confronto.html`).
2. **Brevi**: max ~5 parole significative; stop-word ridotte al minimo.
3. **Gerarchiche a 2 livelli**: `/categoria/<silo>.html` → `/articoli/<slug>.html`.
   Niente date né ID nelle URL: gli slug restano evergreen e il `lastmod` vive in sitemap.
4. **Minuscolo, trattini, niente accenti/caratteri speciali** (`dlgs-36-2023`, `xlam`).
5. **Una keyword primaria per URL**, allineata a title e H1 ma non necessariamente identica.
6. Prefissi riconoscibili per formato: `top-5-*` per le classifiche, `*-guida*` per i pillar.

## 5. Policy dei breadcrumb

- Visibili in testa a ogni articolo e pagina categoria: `Home › <Silo> › <Titolo breve>`.
- Replicati in JSON-LD `BreadcrumbList` con URL assolute.
- Il livello intermedio punta **sempre** alla pagina categoria del silo: è il meccanismo
  che consolida l'architettura agli occhi del crawler.
- Anche i tag finali dell'articolo puntano alle categorie (mai a pagine tag inesistenti).

## 6. Regole di internal linking

| Pattern | Regola | Stato |
|---|---|---|
| Pillar → cluster | Link contestuali nel corpo + sezione "Leggi anche" | ✅ attivo |
| Cluster → pillar | 1 link nel primo terzo del corpo con anchor descrittiva | ⚠️ da rinforzare (vedi §3.3) |
| Cluster ↔ cluster stesso silo | Sezione "Leggi anche": 4 card pertinenti al silo | ✅ attivo (7-10 link interni/articolo) |
| Home → silos | Sezioni dedicate per categoria + hero + ticker | ✅ attivo (6 sezioni) |
| Footer → silos | Colonna "Sezioni" con le 6 categorie su tutte le 49 pagine | ✅ attivo |
| Sidebar "I più letti" | 5 link editoriali su home e articoli | ✅ attivo |
| Nav principale | 7 voci: Home + 5 categorie + Guide | ✅ attivo |
| Mappa del sito | Link "Mappa del sito" nel footer di tutte le pagine | ✅ attivo |

Vincolo anti-orphan: ogni articolo è raggiungibile da almeno 3 percorsi
(categoria, correlati di altri articoli, sitemap.html/feed.xml).

## 7. Strategia sitelink

I sitelink (di Google e delle risposte AI) si guadagnano con struttura, non con markup dedicato:

1. **TOC con ancore**: ogni articolo apre con `nav.toc` → 5-12 ancore `#id` verso H2.
   Google può mostrare i link alle sezioni direttamente in SERP (sitelink di pagina).
2. **H2 distintivi a forma di domanda** (es. `#quanto-costano` → "Quanto costano i pannelli
   solari nel 2026?"): ogni ancora è una query reale, massimizzando la probabilità di
   sitelink e di citazione AI.
3. **Articoli figli per le sezioni più ricercate**: le query ad alto volume non restano
   solo ancore ma diventano URL dedicate (§3.1), candidandosi a sitelink di dominio.
4. **SearchAction** in home (JSON-LD `WebSite.potentialAction` → `/cerca.html?q=...`)
   per il sitelinks search box.
5. Navigazione principale stabile e testuale (niente menu JS-only): le 7 voci sono i
   candidati naturali ai sitelink di dominio.

## 8. Setup sitemap / robots / llms.txt

| File | Contenuto |
|---|---|
| `sitemap.xml` | 49 URL: home (1.0/daily), guide (0.8/weekly), 6 categorie (0.8/daily), 33 articoli (0.7/weekly con `lastmod` da `article:modified_time`), sitemap.html + 6 pagine servizio (0.3/yearly) |
| `sitemap-news.xml` | 9 articoli pubblicati 19-21/07/2026, namespace Google News, publication "Il Giornale Edile", language `it` |
| `robots.txt` | `Allow: /` per tutti + 13 gruppi espliciti per crawler AI (vedi doc 02) + 2 righe `Sitemap:` |
| `llms.txt` | Indice markdown per LLM: pillar, categorie, ultimi articoli, info editoriali (35 URL) |
| `feed.xml` | RSS 2.0, 20 item più recenti, categorie incluse |

Tutti i file XML sono rigenerati da `build_pages.py`, che resta la fonte unica per
categorie, sitemap, robots e feed: ogni nuovo articolo entra automaticamente in tutti
gli indici al build successivo.
