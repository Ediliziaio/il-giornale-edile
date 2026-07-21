# -*- coding: utf-8 -*-
"""Genera i 10 articoli de Il Giornale Edile replicando il template di riferimento."""
import json, os, re

BASE = "/Users/agenteai/Documents/kimi/workspace/giornale-edile/articoli"

AD_INART = '''<div class="ad-slot ad-rect ad-inarticle" data-ad-slot="inarticle-1" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>'''


def ld(obj):
    return ('<script type="application/ld+json">\n  '
            + json.dumps(obj, ensure_ascii=False, indent=2).replace("\n", "\n  ")
            + '\n  </script>')


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


NAV_CATS = [
    ("../index.html", "Home", None),
    ("../categoria/bonus-fiscali.html", "Bonus &amp; Fisco", "bonus-fiscali"),
    ("../categoria/energia-rinnovabili.html", "Energia", None),
    ("../categoria/normative-cantieri.html", "Normative", "normative-cantieri"),
    ("../categoria/materiali-tecnologie.html", "Materiali &amp; Tech", None),
    ("../categoria/mercato-immobiliare.html", "Mercato", None),
    ("../guide.html", "Guide &amp; Top 5", None),
]


def nav_html(active):
    items = []
    for href, label, key in NAV_CATS:
        cur = ' aria-current="page"' if key == active else ""
        items.append(f'        <li><a href="{href}"{cur}>{label}</a></li>')
    return "\n".join(items)


SIDEBAR = '''<aside class="sidebar">
          <div class="ad-slot ad-halfpage" data-ad-slot="sidebar-halfpage" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Half page 300×600</span>
          </div>

          <section class="widget" aria-labelledby="piu-letti">
            <h3 class="w-title" id="piu-letti">I più letti</h3>
            <ol class="rank-list">
              <li><div><a href="superbonus-2026-cosa-resta.html">Superbonus 2026: cosa resta e come accedere alle detrazioni residue</a><span class="rl-cat">Bonus &amp; Fisco</span></div></li>
              <li><div><a href="costo-ristrutturazione-al-mq-2026.html">Quanto costa ristrutturare casa nel 2026: prezzi al mq voce per voce</a><span class="rl-cat">Mercato</span></div></li>
              <li><div><a href="top-5-fornitori-pannelli-solari.html">I 5 migliori fornitori di pannelli solari in Italia</a><span class="rl-cat">Energia</span></div></li>
              <li><div><a href="direttiva-case-green-cosa-cambia.html">Direttiva Case Green: cosa cambia dal 2026</a><span class="rl-cat">Normative</span></div></li>
              <li><div><a href="cappotto-termico-materiali-confronto.html">Cappotto termico: EPS, lana di roccia o sughero?</a><span class="rl-cat">Materiali</span></div></li>
            </ol>
          </section>

          <section class="widget newsletter" aria-labelledby="nl-art">
            <h3 class="w-title" id="nl-art">Newsletter del cantiere</h3>
            <p>Bonus, norme e mercato dell'edilizia: ogni settimana nella tua email.</p>
            <form action="#" method="post">
              <label class="sr-only" for="nl-email-art">Email</label>
              <input type="email" id="nl-email-art" name="email" placeholder="La tua email" required>
              <button class="btn" type="submit">Iscriviti</button>
            </form>
            <small>Iscrivendoti accetti la nostra informativa privacy. Nessuno spam, solo edilizia.</small>
          </section>

          <div class="ad-slot ad-rect" data-ad-slot="sidebar-rect" role="complementary" aria-label="Spazio pubblicitario">
            <span class="ad-tag">Pubblicità</span>
            <span class="ad-size">Rectangle 300×250</span>
          </div>
        </aside>'''


FOOTER = '''<div class="ad-slot ad-footer" data-ad-slot="footer-leaderboard" role="complementary" aria-label="Spazio pubblicitario">
    <span class="ad-tag">Pubblicità</span>
    <span class="ad-size">Leaderboard 728×90</span>
  </div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="f-logo" href="../index.html"><img src="../assets/logo.png" alt="Il Giornale Edile" width="240" height="23"></a>
          <p class="f-desc">Il Giornale Edile è la testata online dedicata al mondo delle costruzioni: bonus fiscali, norme tecniche, materiali, tecnologie di cantiere e mercato immobiliare, con guide pratiche e analisi per professionisti e committenti.</p>
        </div>
        <nav aria-label="Sezioni del sito">
          <h4>Sezioni</h4>
          <ul>
            <li><a href="../categoria/bonus-fiscali.html">Bonus &amp; Fisco</a></li>
            <li><a href="../categoria/energia-rinnovabili.html">Energia &amp; Rinnovabili</a></li>
            <li><a href="../categoria/normative-cantieri.html">Normative &amp; Cantieri</a></li>
            <li><a href="../categoria/materiali-tecnologie.html">Materiali &amp; Tecnologie</a></li>
            <li><a href="../categoria/mercato-immobiliare.html">Mercato &amp; Immobiliare</a></li>
          </ul>
        </nav>
        <nav aria-label="Testata">
          <h4>Testata</h4>
          <ul>
            <li><a href="../chi-siamo.html">Chi siamo</a></li>
            <li><a href="../contatti.html">Contatti</a></li>
            <li><a href="../pubblicita.html">Pubblicità</a></li>
            <li><a href="../feed.xml">Feed RSS</a></li>
          </ul>
        </nav>
        <div>
          <h4>Resta aggiornato</h4>
          <p class="f-desc">Iscriviti alla newsletter: bonus, scadenze e norme spiegate in 5 minuti, ogni settimana.</p>
          <a class="btn" href="../index.html#newsletter">Iscriviti gratis</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span data-year>2026</span> Il Giornale Edile — Tutti i diritti riservati</span>
        <span><a href="../privacy.html">Privacy</a> · <a href="../cookie-policy.html">Cookie</a> · <a href="../note-legali.html">Note legali</a></span>
      </div>
    </div>
  </footer>
  <script src="../js/main.js" defer></script>'''


def faq_visible(a):
    parts = []
    for q, ans in a["faq"]:
        parts.append(f'''            <details>
              <summary>{q}</summary>
              <div class="faq-a"><p>{ans}</p></div>
            </details>''')
    return "\n".join(parts)


def related_html(a):
    cards = []
    for slug, thumb, catmini, title, excerpt, date, mins in a["rel"]:
        cards.append(f'''          <article class="card">
            <div class="thumb {thumb} ar-3-2"><span class="thumb-label">{catmini}</span></div>
            <div class="card-body">
              <span class="cat-mini">{catmini}</span>
              <h3><a href="{slug}.html">{title}</a></h3>
              <p class="card-excerpt">{excerpt}</p>
              <div class="card-meta"><span>{date}</span><span>{mins} min</span></div>
            </div>
          </article>''')
    return "\n".join(cards)


def tags_html(a):
    return "\n".join(f'            <a href="{href}">{label}</a>' for href, label in a["tags"])


def render(a):
    page_url = f"https://www.ilgiornaleedile.it/articoli/{a['slug']}.html"
    cat_url = f"https://www.ilgiornaleedile.it/categoria/{a['cat_slug']}.html"

    news_ld = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": a["h1"],
        "description": a["ld_desc"],
        "inLanguage": "it-IT",
        "datePublished": a["date_iso"],
        "dateModified": a["date_iso"],
        "author": {"@type": "Person", "name": a["author"], "jobTitle": "Giornalista edile"},
        "publisher": {
            "@type": "Organization",
            "name": "Il Giornale Edile",
            "url": "https://www.ilgiornaleedile.it/",
            "logo": {"@type": "ImageObject", "url": "https://www.ilgiornaleedile.it/assets/logo.png"},
        },
        "mainEntityOfPage": page_url,
        "articleSection": a["cat"].replace("&amp;", "&"),
        "keywords": a["kw"],
    }
    bread_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.ilgiornaleedile.it/"},
            {"@type": "ListItem", "position": 2, "name": a["cat"].replace("&amp;", "&"), "item": cat_url},
            {"@type": "ListItem", "position": 3, "name": a["bc_short"]},
        ],
    }
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": strip_tags(ans)}}
            for q, ans in a["faq"]
        ],
    }

    body = (a["body"]
            .replace("{AD}", AD_INART)
            .replace("{FAQ}", faq_visible(a))
            .replace("{TAGS}", tags_html(a)))

    return f'''<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a["title"]}</title>
  <meta name="description" content="{a["desc"]}">
  <link rel="canonical" href="{page_url}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="keywords" content="{a["kw"]}">
  <meta name="author" content="{a["author"]}">
  <meta name="geo.region" content="IT">
  <meta name="geo.placename" content="Italia">
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Il Giornale Edile">
  <meta property="og:title" content="{a["og_title"]}">
  <meta property="og:description" content="{a["og_desc"]}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:locale" content="it_IT">
  <meta property="article:published_time" content="{a["date_iso"]}">
  <meta property="article:modified_time" content="{a["date_iso"]}">
  <meta property="article:section" content="{a["cat"]}">
  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{a["tw_title"]}">
  <meta name="twitter:description" content="{a["tw_desc"]}">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Source+Sans+3:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <!-- Structured data: NewsArticle -->
  {ld(news_ld)}
  <!-- Structured data: Breadcrumbs -->
  {ld(bread_ld)}
  <!-- Structured data: FAQ (AEO) -->
  {ld(faq_ld)}
</head>
<body>
  <a class="skip-link" href="#contenuto">Salta al contenuto</a>
  <div class="reading-progress" aria-hidden="true"></div>

  <!-- Topbar -->
  <div class="topbar">
    <div class="container">
      <span class="tb-date" data-tb-date>{a["tb_date"]}</span>
      <nav class="tb-links" aria-label="Link utili">
        <a href="../chi-siamo.html">Chi siamo</a>
        <a href="../contatti.html">Contatti</a>
        <a href="../pubblicita.html">Pubblicità</a>
        <a href="../feed.xml">RSS</a>
      </nav>
    </div>
  </div>

  <!-- Testata -->
  <header class="masthead">
    <div class="container">
      <a class="logo" href="../index.html" aria-label="Il Giornale Edile - Home">
        <img src="../assets/logo.png" alt="Il Giornale Edile - Notizie di edilizia, bonus e costruzioni" width="460" height="44">
      </a>
      <div class="mh-right">
        <p class="mh-tagline">La testata di riferimento per imprese, professionisti e committenti dell'edilizia italiana.</p>
        <a class="btn" href="../index.html#newsletter">Iscriviti gratis</a>
      </div>
    </div>
  </header>

  <!-- Navigazione principale -->
  <nav class="mainnav" aria-label="Navigazione principale">
    <div class="container">
      <ul>
{nav_html(a["cat_slug"])}
      </ul>
    </div>
  </nav>

  <!-- Slot pubblicitario: leaderboard -->
  <div class="container">
    <div class="ad-slot ad-leaderboard" data-ad-slot="leaderboard-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <span class="ad-size">Leaderboard 970×250 / 728×90</span>
    </div>
    <div class="ad-slot ad-mobile mobile-only" data-ad-slot="mobile-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span>
      <span class="ad-size">Mobile banner 320×100</span>
    </div>
  </div>

  <main id="contenuto">
    <!-- Intestazione articolo -->
    <article itemscope itemtype="https://schema.org/NewsArticle">
      <header class="article-head container">
        <nav class="breadcrumbs" aria-label="Percorso di navigazione">
          <a href="../index.html">Home</a><span class="sep">›</span>
          <a href="../categoria/{a["cat_slug"]}.html">{a["cat"]}</a><span class="sep">›</span>
          <span>{a["bc_short"]}</span>
        </nav>
        <span class="kicker">{a["kicker"]}</span>
        <h1 itemprop="headline">{a["h1"]}</h1>
        <p class="standfirst" itemprop="description">{a["stand"]}</p>
        <div class="article-meta-bar">
          <span class="b-author" itemprop="author">di {a["author"]}</span>
          <span>Pubblicato il <time datetime="{a["date_iso"]}" itemprop="datePublished">{a["date_it"]}</time></span>
          <span>Tempo di lettura: {a["mins"]} min</span>
          <div class="share" aria-label="Condividi l'articolo">
            <a href="https://www.facebook.com/sharer/sharer.php?u={page_url}" rel="noopener" target="_blank" aria-label="Condividi su Facebook">f</a>
            <a href="https://www.linkedin.com/sharing/share-offsite/?url={page_url}" rel="noopener" target="_blank" aria-label="Condividi su LinkedIn">in</a>
            <a href="https://wa.me/?text={page_url}" rel="noopener" target="_blank" aria-label="Condividi su WhatsApp">wa</a>
          </div>
        </div>
      </header>

      <div class="article-layout">
        <div class="article-body" itemprop="articleBody">

          {body}

        </div>

        <!-- Sidebar articolo -->
        {SIDEBAR}
      </div>

      <!-- Articoli correlati -->
      <section class="related container" aria-labelledby="correlati">
        <h2 id="correlati">Leggi anche</h2>
        <div class="card-grid cg-4">
{related_html(a)}
        </div>
      </section>
    </article>
  </main>

  <!-- Slot pubblicitario: footer -->
  {FOOTER}
</body>
</html>
'''


ARTICLES = []

# ============================ ARTICOLO 1: SUPERBONUS ============================
ARTICLES.append({
 "slug": "superbonus-2026-cosa-resta",
 "cat": "Bonus &amp; Fisco", "cat_slug": "bonus-fiscali", "thumb": "t-bonus",
 "title": "Superbonus 2026: cosa resta | Il Giornale Edile",
 "desc": "Superbonus 2026: cosa resta dell'agevolazione, aliquote residue, scadenze per i cantieri avviati e recupero delle detrazioni senza cessione.",
 "kw": "superbonus 2026, superbonus cosa resta, detrazioni residue, superbonus condomini, bonus edilizia 2026",
 "author": "Giulia Santi",
 "date_iso": "2026-07-20T08:00:00+02:00", "date_it": "20 luglio 2026", "tb_date": "Lunedì 20 luglio 2026", "mins": 9,
 "og_title": "Superbonus 2026: cosa resta e come accedere alle detrazioni residue",
 "og_desc": "Il Superbonus è archiviato per i nuovi cantieri, ma restano detrazioni residue, scadenze e adempimenti: la mappa completa per non perdere nulla.",
 "tw_title": "Superbonus 2026: cosa resta", "tw_desc": "Aliquote residue, scadenze e alternative: la guida aggiornata.",
 "ld_desc": "Superbonus 2026: niente nuovi cantieri, restano le detrazioni residue per i lavori avviati nei termini. Scadenze, adempimenti e alternative.",
 "bc_short": "Superbonus 2026",
 "kicker": "Bonus &amp; Fisco · Analisi",
 "h1": "Superbonus 2026: cosa resta, cosa è cambiato e come accedere alle detrazioni residue",
 "stand": "Archiviata l'era del 110%, il 2026 è l'anno della coda lunga del Superbonus: cantieri da completare, detrazioni da recuperare in dieci anni e un mercato che torna alle agevolazioni ordinarie. Ecco la mappa completa.",
 "faq": [
  ("Il Superbonus esiste ancora nel 2026?",
   "No: dal 2026 non è più possibile avviare nuovi cantieri con l'aliquota maggiorata. Restano valide solo le <strong>detrazioni residue</strong> per gli interventi avviati entro i termini previsti dalle proroghe, recuperabili in dichiarazione dei redditi in 10 rate annuali."),
  ("Posso ancora cedere il credito Superbonus o chiedere lo sconto in fattura?",
   "No. La cessione del credito e lo sconto in fattura sono stati aboliti per la generalità dei casi dal decreto 11/2023, salvo eccezioni residuali molto limitate. Il recupero avviene oggi quasi esclusivamente come <strong>detrazione IRPEF diretta</strong>."),
  ("Cosa succede se i lavori non sono finiti?",
   "Le spese sostenute nei periodi in cui l'agevolazione era attiva restano detraibili secondo l'aliquota propria di ciascun anno, a condizione che siano stati rispettati titoli edilizi, asseverazioni e comunicazioni ENEA. Per i casi dubbi è indispensabile una verifica con un professionista fiscale."),
  ("Quali bonus posso usare oggi al posto del Superbonus?",
   "Le alternative principali sono il <strong>bonus ristrutturazione</strong> (50% prima casa, 36% altre unità), l'<strong>Ecobonus</strong> per l'efficienza energetica e il <strong>Conto Termico 3.0</strong>, incentivo diretto del GSE per pompe di calore, solare termico e isolamento."),
 ],
 "tags": [("../categoria/bonus-fiscali.html","Superbonus"),("../categoria/bonus-fiscali.html","Detrazioni fiscali"),("../categoria/bonus-fiscali.html","Bonus casa 2026"),("../categoria/energia-rinnovabili.html","Riqualificazione energetica")],
 "rel": [
  ("bonus-ristrutturazione-2026-guida-completa","t-bonus","Bonus &amp; Fisco","Bonus Ristrutturazione 2026: la guida completa","Aliquote 50% e 36%, massimale 96.000 euro, interventi ammessi e adempimenti.","21 lug 2026",9),
  ("ecobonus-65-guida","t-bonus","Bonus &amp; Fisco","Ecobonus: come funziona e interventi ammessi","Efficienza energetica e detrazioni: caldaie, infissi, cappotto e schermature solari.","15 lug 2026",8),
  ("conto-termico-3-guida","t-bonus","Bonus &amp; Fisco","Conto Termico 3.0: incentivi GSE e procedura","Contributo a fondo perduto per pompe di calore e solare termico: importi e tempi.","4 lug 2026",7),
  ("detrazioni-ristrutturazione-50-36","t-bonus","Bonus &amp; Fisco","Detrazione 50% e 36%: regole e differenze 2026","Prima casa e seconda casa a confronto: requisiti, massimali ed esempi di calcolo.","2 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-bonus ar-16-9" role="img" aria-label="Condominio con ponteggio durante lavori di efficientamento energetico">
            <span class="thumb-label">Bonus &amp; Fisco</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Dal 2026 il Superbonus <strong>non è più attivo per i nuovi cantieri</strong>: restano solo le detrazioni residue per i lavori avviati nei termini di legge.</li>
              <li>Nel 2025 l'aliquota residua era del <strong>65% per i condomini</strong> con CILAS presentata entro il 15 ottobre 2024.</li>
              <li>Cessione del credito e sconto in fattura sono <strong>aboliti</strong> per la generalità dei casi: il recupero avviene in dichiarazione in 10 rate annuali.</li>
              <li>Le alternative operative oggi sono <strong>bonus ristrutturazione, Ecobonus e Conto Termico 3.0</strong>.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cosa-resta">Cosa resta del Superbonus nel 2026</a></li>
              <li><a href="#cronologia">La cronologia delle aliquote</a></li>
              <li><a href="#chi-puo">Chi può ancora accedere alle detrazioni residue</a></li>
              <li><a href="#come-recuperare">Come si recupera la detrazione</a></li>
              <li><a href="#alternative">Le alternative al Superbonus nel 2026</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cosa-resta">Cosa resta del Superbonus nel 2026</h2>
          <p>Il <strong>Superbonus</strong>, l'agevolazione introdotta dal decreto Rilancio del 2020 con l'aliquota al 110%, ha chiuso definitivamente la propria parabola. Dopo le riduzioni progressive — 90% nel 2023, 70% nel 2024 e 65% nel 2025 limitatamente ai casi residui — dal 2026 non è più possibile avviare nuovi cantieri con l'aliquota maggiorata. La misura, che secondo i monitoraggi ENEA ha attivato investimenti per oltre 120 miliardi di euro e interessato centinaia di migliaia di edifici, lascia però un'eredità lunga: detrazioni residue da gestire, lavori da completare nei termini e un decennio di rate da portare in dichiarazione.</p>
          <p>Per imprese edili, tecnici e amministratori di condominio il 2026 è quindi l'anno della <strong>gestione della coda</strong>: chiudere correttamente le pratiche aperte, verificare asseverazioni e comunicazioni, pianificare il recupero fiscale. Per chi invece progetta oggi una riqualificazione, il punto di riferimento torna a essere il sistema ordinario degli incentivi, dal bonus ristrutturazione all'Ecobonus fino al Conto Termico.</p>

          <h2 id="cronologia">La cronologia delle aliquote: dal 110% alle detrazioni residue</h2>
          <p>La parabola del Superbonus si può riassumere in una tabella che racconta cinque anni di politica fiscale per la casa. A ogni step di riduzione sono seguite proroghe mirate e una stretta sulle opzioni di monetizzazione del credito, con l'obiettivo dichiarato di contenere l'impatto sulla finanza pubblica.</p>
          <table>
            <thead>
              <tr><th>Periodo</th><th>Aliquota</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td>2020-2022</td><td>110%</td><td>Decreto Rilancio, massima espansione della misura</td></tr>
              <tr><td>2023</td><td>90%</td><td>Prima riduzione, stretta su cessione e sconto</td></tr>
              <tr><td>2024</td><td>70%</td><td>Riduzione prevista dalla norma originaria</td></tr>
              <tr><td>2025</td><td>65%</td><td>Solo casi residui, ad esempio condomini con CILAS entro il 15/10/2024</td></tr>
              <tr><td>2026</td><td>—</td><td>Nessun nuovo cantiere: gestione delle detrazioni residue</td></tr>
            </tbody>
          </table>
          <p>Anche per i casi residui restano fermi i requisiti originari: presenza di almeno un <strong>intervento trainante</strong> (isolamento termico delle superfici opache, sostituzione degli impianti di climatizzazione invernale, interventi antisismici), conseguimento del <strong>doppio salto di classe energetica</strong> (o raggiungimento della classe più alta possibile) e rispetto della congruità dei prezzi rispetto ai massimali ENEA.</p>

          <h2 id="chi-puo">Chi può ancora accedere alle detrazioni residue</h2>
          <p>La platea dei beneficiari residuali è circoscritta ma numericamente ancora rilevante. In sintesi:</p>
          <ul>
            <li><strong>Condomini</strong> con CILAS (CILA asseverata Superbonus) trasmessa entro il 15 ottobre 2024 e delibera assembleare valida: le spese 2025 hanno fruito dell'aliquota del 65%, recuperabile in 10 rate; nel 2026 si gestiscono saldi, collaudi e adempimenti finali.</li>
            <li><strong>Edifici unifamiliari e villette</strong> che avevano completato almeno il 30% dei lavori entro il 30 settembre 2022: proroga ormai esaurita, restano le detrazioni maturate.</li>
            <li><strong>Istituti di edilizia residenziale pubblica, cooperative e Onlus</strong>, per i quali le norme originarie prevedevano termini più ampi per la conclusione degli interventi.</li>
            <li>Edifici ricadenti in specifici contesti (zone colpite da eventi sismici, casi previsti da proroghe puntuali), sempre nel rispetto dei requisiti di ciascun regime.</li>
          </ul>
          <p>Fuori da questi perimetri non esistono scorciatoie: chi avvia oggi un cantiere di riqualificazione deve ragionare sulle aliquote ordinarie, come spiegato nella <a href="bonus-ristrutturazione-2026-guida-completa.html">guida al bonus ristrutturazione 2026</a>.</p>

          {AD}

          <h2 id="come-recuperare">Come si recupera la detrazione: addio cessione, si torna alla dichiarazione</h2>
          <p>Con l'abolizione generalizzata di cessione del credito e sconto in fattura, il canale di recupero è tornato a essere la <strong>detrazione IRPEF diretta in 10 quote annuali</strong> di pari importo. Per mettere in sicurezza il beneficio servono, in ordine logico: titolo edilizio coerente con l'intervento, asseverazione del salto di classe energetica firmata da un tecnico abilitato, attestazione di congruità dei prezzi, doppia certificazione APE (ante e post intervento), comunicazione ENEA entro 90 giorni dalla fine dei lavori e pagamenti tracciati con bonifico dedicato.</p>
          <p>La parte documentale è decisiva: molte delle decadenze rilevate nei controlli dell'Agenzia delle Entrate derivano da incongruenze tra CILAS, asseverazioni e fatture, oppure da mancati invii telematici nei termini. Chi ha beneficiato della cessione negli anni scorsi deve inoltre conservare la documentazione del visto di conformità e della polizza assicurativa del professionista.</p>
          <blockquote>«Il Superbonus non finisce con l'ultima rata in fattura: finisce dieci anni dopo, con l'ultima rata in dichiarazione. La gestione documentale è oggi la parte più delicata della pratica.»</blockquote>

          <h2 id="alternative">Le alternative al Superbonus nel 2026</h2>
          <p>Il mercato della riqualificazione non si ferma, cambia scala. Le tre agevolazioni di riferimento per il 2026 sono:</p>
          <ul>
            <li><strong>Bonus ristrutturazione</strong>: 50% per l'abitazione principale e 36% per le altre unità, massimale 96.000 euro, recupero in 10 anni. È il contenitore principale per la manutenzione straordinaria.</li>
            <li><strong>Ecobonus</strong>: dedicato agli interventi di efficienza energetica, con aliquote riallineate e massimali per tipologia di intervento. La <a href="ecobonus-65-guida.html">guida completa all'Ecobonus</a> illustra requisiti e adempimenti ENEA.</li>
            <li><strong>Conto Termico 3.0</strong>: incentivo diretto del GSE, non una detrazione, con contributi fino al 65% della spesa per pompe di calore, solare termico e isolamento. Ne parliamo nella <a href="conto-termico-3-guida.html">guida al Conto Termico 3.0</a>.</li>
          </ul>
          <p>La strategia più efficace nel 2026 è la <strong>combinazione ragionata</strong>: Ecobonus o Conto Termico per l'involucro e gli impianti, bonus ristrutturazione per le opere edili non energetiche, nel rispetto del principio di non doppia agevolazione della stessa spesa. Per cantieri complessi resta consigliabile un progetto unico con computo separato per linea di incentivo.</p>

          <h2 id="faq">Domande frequenti sul Superbonus 2026</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> Agenzia delle Entrate — guide e provvedimenti sulle agevolazioni edilizie; ENEA — monitoraggio Superbonus e portale dedicato; decreto Rilancio (DL 34/2020) e decreti attuativi successivi. Contenuto a scopo informativo: per i casi specifici consultare un professionista fiscale o il sito istituzionale.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 2: ECOBONUS ============================
ARTICLES.append({
 "slug": "ecobonus-65-guida",
 "cat": "Bonus &amp; Fisco", "cat_slug": "bonus-fiscali", "thumb": "t-bonus",
 "title": "Ecobonus 2026: guida completa | Il Giornale Edile",
 "desc": "Ecobonus: guida completa ad aliquote, interventi ammessi, massimali, requisiti e adempimenti ENEA per detrarre i lavori di efficienza energetica.",
 "kw": "ecobonus, ecobonus 2026, detrazione efficienza energetica, ecobonus interventi ammessi, ecobonus enea",
 "author": "Marco Ferreri",
 "date_iso": "2026-07-15T08:00:00+02:00", "date_it": "15 luglio 2026", "tb_date": "Mercoledì 15 luglio 2026", "mins": 9,
 "og_title": "Ecobonus: come funziona, interventi ammessi e requisiti aggiornati",
 "og_desc": "Aliquote, massimali per intervento, requisiti tecnici e adempimenti ENEA: tutto quello che serve per usare l'Ecobonus senza errori.",
 "tw_title": "Ecobonus: la guida completa", "tw_desc": "Interventi ammessi, aliquote e adempimenti ENEA aggiornati.",
 "ld_desc": "Ecobonus: aliquote 2026, interventi ammessi, massimali di detrazione, requisiti tecnici e adempimenti ENEA entro 90 giorni dalla fine lavori.",
 "bc_short": "Ecobonus: guida completa",
 "kicker": "Bonus &amp; Fisco · Guida aggiornata",
 "h1": "Ecobonus: come funziona, interventi ammessi e requisiti aggiornati",
 "stand": "È l'agevolazione di riferimento per l'efficienza energetica degli edifici: caldaie, pompe di calore, infissi, cappotto e schermature. Regole, massimali e adempimenti per portare a casa la detrazione senza sorprese.",
 "faq": [
  ("Qual è l'aliquota dell'Ecobonus nel 2026?",
   "Per le persone fisiche l'aliquota è del <strong>50% per l'abitazione principale</strong> e del <strong>36% per le altre unità immobiliari</strong>, con massimali di detrazione che variano per tipologia di intervento (60.000 euro per involucro e infissi, 30.000 per i generatori di calore)."),
  ("Quali interventi rientrano nell'Ecobonus?",
   "Riqualificazione energetica globale, isolamento dell'involucro, sostituzione di finestre e schermature solari, installazione di caldaie a condensazione, pompe di calore e sistemi ibridi, collettori solari termici e building automation."),
  ("È obbligatoria la comunicazione ENEA?",
   "Sì: per quasi tutti gli interventi Ecobonus la <strong>comunicazione telematica a ENEA entro 90 giorni dalla fine dei lavori</strong> è obbligatoria. La mancata trasmissione comporta la perdita della detrazione."),
  ("Ecobonus e Conto Termico si possono cumulare?",
   "No, non sulla stessa spesa: il principio di non doppia agevolazione vieta di detrarre con l'Ecobonus un costo già incentivato con il <strong>Conto Termico</strong>. È possibile invece usare le due misure su interventi distinti dello stesso cantiere."),
 ],
 "tags": [("../categoria/bonus-fiscali.html","Ecobonus"),("../categoria/bonus-fiscali.html","Detrazioni fiscali"),("../categoria/energia-rinnovabili.html","Efficienza energetica"),("../categoria/bonus-fiscali.html","Bonus casa 2026")],
 "rel": [
  ("superbonus-2026-cosa-resta","t-bonus","Bonus &amp; Fisco","Superbonus 2026: cosa resta e cosa è cambiato","Lo stato dell'arte dell'agevolazione simbolo: residui, scadenze e alternative.","20 lug 2026",9),
  ("conto-termico-3-guida","t-bonus","Bonus &amp; Fisco","Conto Termico 3.0: incentivi GSE e procedura","Contributo diretto per pompe di calore e solare termico: importi e tempi di erogazione.","4 lug 2026",7),
  ("bonus-ristrutturazione-2026-guida-completa","t-bonus","Bonus &amp; Fisco","Bonus Ristrutturazione 2026: la guida completa","Aliquote 50% e 36%, massimale 96.000 euro e adempimenti per non perdere il bonus.","21 lug 2026",9),
  ("top-5-pompe-di-calore","t-energia","Energia &amp; Rinnovabili","Le 5 migliori pompe di calore per la casa","Confronto tra i principali marchi: efficienza, rumorosità e prezzi reali.","10 lug 2026",6),
 ],
 "body": '''<figure class="thumb t-bonus ar-16-9" role="img" aria-label="Tecnico installa una pompa di calore in un edificio residenziale">
            <span class="thumb-label">Bonus &amp; Fisco</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>L'Ecobonus detrae gli interventi di <strong>efficienza energetica</strong>: nel 2026 vale il <strong>50% per l'abitazione principale</strong> e il <strong>36% per le altre unità</strong> per le persone fisiche.</li>
              <li>Massimali per intervento: <strong>60.000 euro</strong> per involucro e infissi, <strong>30.000 euro</strong> per i generatori di calore.</li>
              <li>Recupero in <strong>10 rate annuali</strong>, bonifico parlante obbligatorio e <strong>comunicazione ENEA entro 90 giorni</strong> dalla fine lavori.</li>
              <li>Non cumulabile con il Conto Termico sulla stessa spesa; combinabile con il bonus ristrutturazione su spese distinte.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cos-e">Cos'è l'Ecobonus e come funziona</a></li>
              <li><a href="#aliquote">Aliquote e massimali 2026</a></li>
              <li><a href="#interventi">Interventi ammessi</a></li>
              <li><a href="#requisiti">Requisiti tecnici e adempimenti ENEA</a></li>
              <li><a href="#errori">Errori da evitare e cumulabilità</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cos-e">Cos'è l'Ecobonus e come funziona</h2>
          <p>L'<strong>Ecobonus</strong> è la detrazione fiscale dedicata agli interventi di riqualificazione energetica degli edifici esistenti, disciplinata dall'articolo 14 del decreto legge 63/2013 e dalle norme di bilancio che ne hanno aggiornato aliquote e platee. A differenza del bonus ristrutturazione, che premia l'intervento edilizio in sé, l'Ecobonus premia il <strong>risultato energetico</strong>: ogni tipologia di lavoro deve rispettare requisiti tecnici minimi (trasmittanze, rendimenti, classi di efficienza) fissati dai decreti requisiti minimi.</p>
          <p>Con la fine del Superbonus, l'Ecobonus è tornato al centro dei cantieri di riqualificazione: secondo i report ENEA, gli interventi agevolati con il canale ordinario sono tornati a crescere in modo significativo, trainati dalla sostituzione dei generatori di calore e dagli infissi. Per imprese e committenti conoscere bene la misura è oggi essenziale: l'errore tecnico o documentale costa l'intera detrazione.</p>

          <h2 id="aliquote">Aliquote e massimali 2026: quanto si detrae</h2>
          <p>Per le spese sostenute dalle persone fisiche nel 2026, l'aliquota è del <strong>50% per l'abitazione principale</strong> e del <strong>36% per le altre unità immobiliari</strong>, in linea con il riordino generale delle agevolazioni casa. Ogni intervento ha però un proprio <strong>massimale di detrazione</strong>, non di spesa: la distinzione è fondamentale per calcolare il beneficio reale.</p>
          <table>
            <thead>
              <tr><th>Intervento</th><th>Aliquota</th><th>Massimale detrazione</th></tr>
            </thead>
            <tbody>
              <tr><td>Riqualificazione energetica globale</td><td>50% / 36%</td><td>153.000 €</td></tr>
              <tr><td>Isolamento involucro (&gt;25% superficie disperdente)</td><td>50% / 36%</td><td>60.000 €</td></tr>
              <tr><td>Infissi e schermature solari</td><td>50% / 36%</td><td>60.000 €</td></tr>
              <tr><td>Caldaie a condensazione, pompe di calore, sistemi ibridi</td><td>50% / 36%</td><td>30.000 €</td></tr>
              <tr><td>Collettori solari termici</td><td>50% / 36%</td><td>60.000 €</td></tr>
              <tr><td>Building automation</td><td>50% / 36%</td><td>15.000 €</td></tr>
            </tbody>
          </table>
          <p>La detrazione si ripartisce in <strong>10 quote annuali</strong> di pari importo. Per gli interventi sulle parti comuni condominiali e per particolari categorie di edifici possono applicarsi regimi specifici: la verifica puntuale sul sito dell'Agenzia delle Entrate è sempre consigliabile prima dell'apertura del cantiere.</p>

          <h2 id="interventi">Interventi ammessi: cosa si può detrarre</h2>
          <p>Il perimetro dell'Ecobonus copre i principali lavori di un cantiere di efficientamento:</p>
          <ul>
            <li><strong>Riqualificazione energetica globale</strong>: interventi che riducono il fabbisogno annuo di energia primaria sotto le soglie limite, con detrazione fino a 153.000 euro.</li>
            <li><strong>Involucro edilizio</strong>: cappotto termico, isolamento di coperture e pavimenti su oltre il 25% della superficie disperdente lorda.</li>
            <li><strong>Finestre e schermature</strong>: sostituzione di serramenti e infissi nel rispetto dei limiti di trasmittanza per zona climatica, chiusure oscuranti e tende.</li>
            <li><strong>Impianti termici</strong>: caldaie a condensazione, pompe di calore, sistemi ibridi, generatori a biomassa, scaldacqua a pompa di calore e microcogeneratori.</li>
            <li><strong>Solare termico e building automation</strong>: collettori per acqua calda sanitaria e sistemi di controllo da remoto degli impianti.</li>
          </ul>
          <p>Per valutare la macchina termica più adatta al proprio edificio è utile il confronto tra i principali produttori nella nostra <a href="top-5-pompe-di-calore.html">selezione delle migliori pompe di calore</a>; per il contributo a fondo perduto alternativo alla detrazione, il riferimento è la <a href="conto-termico-3-guida.html">guida al Conto Termico 3.0</a>.</p>

          {AD}

          <h2 id="requisiti">Requisiti tecnici e adempimenti ENEA</h2>
          <p>Ogni intervento deve rispettare i <strong>requisiti minimi</strong> dei decreti attuativi: valori di trasmittanza termica per superfici e serramenti (differenziati per zona climatica), rendimenti minimi per i generatori, classificazione per le pompe di calore. L'installazione deve essere eseguita da personale qualificato e, per gli impianti termici, nel rispetto della norma F-Gas quando si usano refrigeranti.</p>
          <p>Sul fronte documentale la checklist comprende:</p>
          <ol>
            <li><strong>Scheda descrittiva dell'intervento</strong> e documentazione tecnica (schede di prodotto, certificazioni, prove di trasmittanza).</li>
            <li><strong>Bonifico parlante</strong> con causale agevolazioni fiscali, codice fiscale del beneficiario e partita IVA del fornitore.</li>
            <li><strong>Comunicazione ENEA</strong> telematica entro 90 giorni dalla fine dei lavori, con i dati dell'immobile, dell'intervento e del tecnico.</li>
            <li><strong>APE</strong>, obbligatoria in specifici casi (riqualificazione globale, involucro esteso, sostituzione generatore con variazione di classe).</li>
            <li>Conservazione di fatture, ricevute e asseverazioni per l'intero periodo di detrazione.</li>
          </ol>

          <h2 id="errori">Errori da evitare e regole di cumulo</h2>
          <p>Gli errori più costosi riguardano la <strong>trasmittanza non conforme</strong> alla zona climatica, la mancata comunicazione ENEA nei 90 giorni, il bonifico con causale errata e la doppia agevolazione della stessa spesa. Attenzione anche alla data di fine lavori, che fa da spartiacque per aliquote e adempimenti: per gli interventi semplici coincide con il collaudo o con la data della fattura a saldo.</p>
          <p>Sul cumulo la regola è chiara: mai due incentivi sullo stesso euro speso. È invece legittimo — e spesso conveniente — usare l'Ecobonus per gli infissi e il <a href="bonus-ristrutturazione-2026-guida-completa.html">bonus ristrutturazione</a> per le opere edili connesse, oppure il Conto Termico per la pompa di calore e l'Ecobonus per l'involucro, con computi e fatturazione separati.</p>
          <blockquote>«L'Ecobonus si vince sul tavolo del progettista, non in cantiere: requisiti tecnici e massimali vanno verificati prima dell'ordine dei materiali, non dopo.»</blockquote>

          <h2 id="faq">Domande frequenti sull'Ecobonus</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> Agenzia delle Entrate — guida "Le agevolazioni fiscali per il risparmio energetico"; ENEA — portale dedicato e schede informative; decreto legge 63/2013 e decreti requisiti minimi. Contenuto a scopo informativo: per i casi specifici consultare un professionista fiscale o il sito istituzionale.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 3: CONTO TERMICO 3.0 ============================
ARTICLES.append({
 "slug": "conto-termico-3-guida",
 "cat": "Bonus &amp; Fisco", "cat_slug": "bonus-fiscali", "thumb": "t-bonus",
 "title": "Conto Termico 3.0: incentivi GSE | Il Giornale Edile",
 "desc": "Conto Termico 3.0: incentivi diretti GSE per pompe di calore, solare termico e isolamento. Importi, requisiti, tempi e procedura per la richiesta.",
 "kw": "conto termico 3.0, incentivi gse, conto termico 2026, pompe di calore incentivi, conto termico requisiti",
 "author": "Sara Colombo",
 "date_iso": "2026-07-04T08:00:00+02:00", "date_it": "4 luglio 2026", "tb_date": "Sabato 4 luglio 2026", "mins": 8,
 "og_title": "Conto Termico 3.0: incentivi GSE, importi e procedura per richiederlo",
 "og_desc": "Contributo diretto fino al 65% della spesa per pompe di calore, solare termico e isolamento: come funziona il nuovo meccanismo e chi può accedervi.",
 "tw_title": "Conto Termico 3.0: la guida", "tw_desc": "Incentivi diretti GSE: importi, requisiti e procedura.",
 "ld_desc": "Conto Termico 3.0: incentivo diretto GSE fino al 65% della spesa per efficienza energetica e rinnovabili termiche. Requisiti, importi e procedura.",
 "bc_short": "Conto Termico 3.0",
 "kicker": "Bonus &amp; Fisco · Guida",
 "h1": "Conto Termico 3.0: incentivi GSE, importi e procedura per richiederlo",
 "stand": "Non è una detrazione ma un contributo diretto, con tempi di erogazione più rapidi della fiscalità: il Conto Termico 3.0 è la nuova edizione dell'incentivo GSE per la riqualificazione energetica. Come funziona e per chi conviene.",
 "faq": [
  ("Cos'è il Conto Termico 3.0?",
   "È il meccanismo di incentivazione gestito dal GSE per interventi di <strong>efficienza energetica e produzione di energia termica da fonti rinnovabili</strong> su edifici esistenti. A differenza delle detrazioni, eroga un contributo diretto in denaro, in un'unica rata o in rate annuali."),
  ("Quanto si può ottenere con il Conto Termico 3.0?",
   "L'incentivo copre in genere <strong>fino al 65% della spesa ammissibile</strong>, con aliquote e massimali differenziati per tipologia di intervento e di beneficiario. Gli incentivi di importo contenuto possono essere erogati in un'unica soluzione."),
  ("Chi può richiedere il Conto Termico?",
   "Persone fisiche, condomini, imprese, titolari di reddito agrario ed enti pubblici, su immobili esistenti di qualsiasi categoria catastale. La domanda si presenta sul portale telematico <strong>Portaltermico</strong> del GSE."),
  ("Si può cumulare con l'Ecobonus?",
   "No, non sulla stessa spesa. È possibile utilizzare Conto Termico ed <strong>Ecobonus</strong> su interventi distinti dello stesso edificio, con contabilizzazioni e fatturazioni separate."),
 ],
 "tags": [("../categoria/bonus-fiscali.html","Conto Termico"),("../categoria/energia-rinnovabili.html","Pompe di calore"),("../categoria/bonus-fiscali.html","Incentivi GSE"),("../categoria/energia-rinnovabili.html","Efficienza energetica")],
 "rel": [
  ("ecobonus-65-guida","t-bonus","Bonus &amp; Fisco","Ecobonus: come funziona e interventi ammessi","Aliquote, massimali e adempimenti ENEA per la detrazione degli interventi energetici.","15 lug 2026",9),
  ("superbonus-2026-cosa-resta","t-bonus","Bonus &amp; Fisco","Superbonus 2026: cosa resta e cosa è cambiato","Detrazioni residue, scadenze e alternative per i cantieri di riqualificazione.","20 lug 2026",9),
  ("top-5-pompe-di-calore","t-energia","Energia &amp; Rinnovabili","Le 5 migliori pompe di calore per la casa","Confronto tra i marchi principali: efficienza stagionale, rumorosità e prezzi.","10 lug 2026",6),
  ("comunita-energetiche-cer-guida","t-energia","Energia &amp; Rinnovabili","Comunità energetiche: la guida per iniziare","Cosa sono le CER, come si costituiscono e quali incentivi le premiano.","8 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-bonus ar-16-9" role="img" aria-label="Unità esterna di pompa di calore installata su un balcone condominiale">
            <span class="thumb-label">Bonus &amp; Fisco</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Il Conto Termico 3.0 è un <strong>contributo diretto del GSE</strong>, non una detrazione: l'erogazione è più rapida della fiscalità ordinaria.</li>
              <li>Copre in genere <strong>fino al 65% della spesa</strong> per pompe di calore, solare termico, caldaie a biomassa e isolamento dell'involucro.</li>
              <li>La domanda si presenta sul portale <strong>Portaltermico</strong>, con prenotazione dell'incentivo o accesso diretto a lavori conclusi.</li>
              <li>Non cumulabile con Ecobonus e detrazioni sulla stessa spesa, ma <strong>combinabile su interventi distinti</strong> dello stesso edificio.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cos-e">Cos'è il Conto Termico 3.0</a></li>
              <li><a href="#novita">Le novità della terza edizione</a></li>
              <li><a href="#interventi">Interventi incentivabili e importi</a></li>
              <li><a href="#procedura">Procedura e tempi di erogazione</a></li>
              <li><a href="#confronto">Conto Termico o Ecobonus: come scegliere</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cos-e">Cos'è il Conto Termico 3.0</h2>
          <p>Il <strong>Conto Termico</strong> è il meccanismo di incentivazione gestito dal Gestore dei Servizi Energetici (GSE) che premia gli interventi di efficienza energetica e di produzione di calore da fonti rinnovabili sugli edifici esistenti. La differenza sostanziale rispetto alle detrazioni fiscali è nella forma: niente recupero in dieci anni nella dichiarazione dei redditi, ma un <strong>contributo in denaro accreditato sul conto corrente</strong>, in un'unica rata per gli importi più contenuti o in rate annuali per quelli più consistenti. La terza edizione del meccanismo, entrata in vigore nel 2025, ne ha rinnovato regole, platee e procedure.</p>
          <p>Per i committenti il vantaggio è doppio: tempi di rientro più rapidi e possibilità di accesso anche per soggetti con capienza fiscale limitata, come pensionati con redditi bassi o nuclei che non raggiungerebbero mai la piena detrazione IRPEF. Per le imprese installatrici, il Conto Termico è diventato uno strumento commerciale centrale nella vendita di pompe di calore e impianti ibridi.</p>

          <h2 id="novita">Le novità della terza edizione</h2>
          <p>Il Conto Termico 3.0 ha introdotto diversi cambiamenti rispetto alla versione precedente: l'adozione dei <strong>Criteri Ambientali Minimi (CAM)</strong> come requisito di accesso per le principali tipologie di intervento, l'ampliamento della soglia per l'erogazione in un'unica rata, la semplificazione delle procedure sul portale <strong>Portaltermico</strong> e l'estensione delle tipologie di beneficiari e di tecnologie ammissibili. Il meccanismo continua a essere alimentato da un budget annuale dedicato, suddiviso tra amministrazioni pubbliche e soggetti privati.</p>
          <p>Tra le novità operative più rilevanti per i privati figurano la <strong>prenotazione dell'incentivo</strong>, che consente di bloccare il contributo prima dell'avvio dei lavori riducendo il rischio di esaurimento dei fondi, e corsie semplificate per gli interventi standardizzati come la sostituzione del generatore di calore.</p>

          <h2 id="interventi">Interventi incentivabili e importi</h2>
          <p>Il perimetro del Conto Termico 3.0 copre le principali tecnologie per la climatizzazione efficiente e la produzione di acqua calda:</p>
          <table>
            <thead>
              <tr><th>Intervento</th><th>Beneficiari</th><th>Copertura indicativa</th></tr>
            </thead>
            <tbody>
              <tr><td>Pompe di calore elettriche e a gas</td><td>Privati, condomini, PA</td><td>Fino al 65% della spesa ammissibile</td></tr>
              <tr><td>Sistemi ibridi (caldaia + pompa di calore)</td><td>Privati, condomini</td><td>Fino al 65% della spesa ammissibile</td></tr>
              <tr><td>Collettori solari termici</td><td>Tutti i beneficiari</td><td>Fino al 65% della spesa ammissibile</td></tr>
              <tr><td>Caldaie e stufe a biomassa</td><td>Privati, PA, imprese agricole</td><td>Quote differenziate per zona</td></tr>
              <tr><td>Isolamento di pareti e coperture</td><td>Privati, condomini, PA</td><td>Fino al 65% in presenza di requisiti CAM</td></tr>
              <tr><td>Scaldacqua a pompa di calore</td><td>Privati, condomini</td><td>Contributo forfettario per taglia</td></tr>
            </tbody>
          </table>
          <p>Gli importi effettivi dipendono da taglia dell'impianto, zona climatica e prestazioni della macchina: per le pompe di calore, ad esempio, il contributo cresce al crescere dell'efficienza stagionale e della quota di fabbisogno coperta. Le schede tecniche GSE, aggiornate con la terza edizione, contengono le formule di calcolo per ciascuna fattispecie.</p>

          {AD}

          <h2 id="procedura">Procedura e tempi di erogazione</h2>
          <p>La domanda si presenta esclusivamente per via telematica sul portale <strong>Portaltermico</strong> del GSE, accedendo con SPID, CIE o CNS. Il percorso standard prevede:</p>
          <ol>
            <li><strong>Registrazione del soggetto richiedente</strong> e dell'edificio, con dati catastali e destinazione d'uso.</li>
            <li><strong>Scelta della modalità</strong>: accesso diretto (domanda entro 60 giorni dalla fine lavori) oppure prenotazione dell'incentivo prima dell'avvio del cantiere.</li>
            <li><strong>Caricamento della documentazione</strong>: fatture, ricevute di pagamento tracciato, schede tecniche, certificazioni CAM, relazione del tecnico quando richiesta.</li>
            <li><strong>Istruttoria GSE</strong>, con eventuali richieste di integrazione.</li>
            <li><strong>Erogazione</strong>: in un'unica rata per gli incentivi sotto la soglia prevista, altrimenti in rate annuali fino a un massimo di cinque.</li>
          </ol>
          <p>I tempi medi di istruttoria comunicati dal GSE si attestano su alcuni mesi, sensibilmente più rapidi dei dieci anni della detrazione ordinaria. La conservazione della documentazione resta obbligatoria per l'intera durata del rapporto incentivante.</p>

          <h2 id="confronto">Conto Termico o Ecobonus: come scegliere</h2>
          <p>La scelta tra le due misure dipende da tre variabili: <strong>capienza fiscale</strong>, tempi di rientro attesi e taglio del progetto. Chi ha reddito e IRPEF sufficienti può trovare più conveniente la detrazione del 50% sull'abitazione principale; chi ha bassa capienza fiscale, o vuole liquidità in tempi brevi, tende a preferire il contributo diretto. La regola d'oro resta la <strong>non cumulabilità sulla stessa spesa</strong>: è invece possibile destinare il Conto Termico alla pompa di calore e l'<a href="ecobonus-65-guida.html">Ecobonus</a> agli infissi dello stesso edificio, con fatture separate.</p>
          <p>Per i condomini il Conto Termico si combina efficacemente con gli interventi sulle parti comuni, mentre per le seconde case e gli immobili a reddito va valutata la convenienza rispetto all'aliquota ridotta del 36%. Chi sta pianificando un progetto più ampio trova il quadro completo delle opzioni nella nostra analisi su <a href="superbonus-2026-cosa-resta.html">cosa resta del Superbonus e sulle alternative 2026</a>.</p>
          <blockquote>«Il Conto Termico è l'incentivo giusto quando il problema non è quanto detrarre, ma quanto incassare e quando: per molte famiglie il contributo diretto vale più di una detrazione decennale.»</blockquote>

          <h2 id="faq">Domande frequenti sul Conto Termico 3.0</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> GSE — portale Portaltermico e regole applicative del Conto Termico; decreto interministeriale di aggiornamento del meccanismo; Criteri Ambientali Minimi per l'edilizia. Contenuto a scopo informativo: per i casi specifici consultare le regole applicative GSE o un professionista.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 4: DETRAZIONI 50/36 ============================
ARTICLES.append({
 "slug": "detrazioni-ristrutturazione-50-36",
 "cat": "Bonus &amp; Fisco", "cat_slug": "bonus-fiscali", "thumb": "t-bonus",
 "title": "Detrazioni 50% e 36%: regole 2026 | Il Giornale Edile",
 "desc": "Detrazione ristrutturazione 2026: aliquota 50% prima casa e 36% seconda casa. Regole, massimali, requisiti ed esempi di calcolo per non sbagliare.",
 "kw": "detrazione 50 prima casa, detrazione 36 seconda casa, bonus ristrutturazione aliquote, detrazioni casa 2026",
 "author": "Luca Brambilla",
 "date_iso": "2026-07-02T08:00:00+02:00", "date_it": "2 luglio 2026", "tb_date": "Giovedì 2 luglio 2026", "mins": 8,
 "og_title": "Detrazione 50% prima casa e 36% seconda casa: regole e differenze 2026",
 "og_desc": "Due aliquote, un solo massimale: come funziona la distinzione tra abitazione principale e altre unità, con esempi di calcolo e casi particolari.",
 "tw_title": "Detrazioni 50% e 36%: le regole", "tw_desc": "Prima casa e seconda casa a confronto: regole ed esempi.",
 "ld_desc": "Detrazione ristrutturazione 2026: aliquota 50% per l'abitazione principale e 36% per le altre unità, massimale 96.000 euro, requisiti ed esempi.",
 "bc_short": "Detrazioni 50% e 36%",
 "kicker": "Bonus &amp; Fisco · Approfondimento",
 "h1": "Detrazione 50% prima casa e 36% seconda casa: regole e differenze 2026",
 "stand": "Il riordino delle agevolazioni casa ha fissato due binari: aliquota piena per chi ristruttura l'abitazione principale, aliquota ridotta per tutto il resto. Requisiti, calcoli ed errori da evitare nella scelta del regime corretto.",
 "faq": [
  ("Qual è la differenza tra detrazione 50% e 36%?",
   "L'aliquota del <strong>50% si applica solo all'abitazione principale</strong>, cioè l'immobile in cui il contribuente o un familiare convivente dimora abitualmente. Per seconde case, immobili locati e altre unità residenziali l'aliquota è del 36%, sempre con massimale di 96.000 euro."),
  ("Cosa si intende per abitazione principale ai fini del bonus?",
   "L'immobile in cui il contribuente (o il coniuge, o un familiare convivente) <strong>dimora abitualmente</strong>. Non basta la residenza anagrafica formale se la dimora effettiva è altrove: in caso di controllo conta la sostanza."),
  ("Il massimale di 96.000 euro si rinnova ogni anno?",
   "Il massimale si riferisce a ciascun anno d'imposta considerato, ma concorre con le detrazioni già fruite per interventi sulla stessa unità immobiliare secondo le regole di prassi. In ogni caso il limite opera <strong>per unità immobiliare</strong>, non per contribuente."),
  ("Posso detrarre al 50% i lavori fatti prima di trasferirmi?",
   "Sì, a condizione che la dimora abituale sia instaurata entro tempi coerenti con la natura dei lavori. Se il trasferimento non avviene, l'Agenzia delle Entrate può <strong>ricalcolare la detrazione al 36%</strong> e recuperare la differenza."),
 ],
 "tags": [("../categoria/bonus-fiscali.html","Detrazioni fiscali"),("../categoria/bonus-fiscali.html","Bonus ristrutturazione"),("../categoria/bonus-fiscali.html","Prima casa"),("../categoria/mercato-immobiliare.html","Mercato immobiliare")],
 "rel": [
  ("bonus-ristrutturazione-2026-guida-completa","t-bonus","Bonus &amp; Fisco","Bonus Ristrutturazione 2026: la guida completa","Aliquote, massimali, interventi ammessi e adempimenti: il quadro completo.","21 lug 2026",9),
  ("superbonus-2026-cosa-resta","t-bonus","Bonus &amp; Fisco","Superbonus 2026: cosa resta e cosa è cambiato","Detrazioni residue e alternative per la riqualificazione energetica.","20 lug 2026",9),
  ("ecobonus-65-guida","t-bonus","Bonus &amp; Fisco","Ecobonus: come funziona e interventi ammessi","Efficienza energetica e detrazioni: requisiti tecnici e adempimenti ENEA.","15 lug 2026",9),
  ("costo-ristrutturazione-al-mq-2026","t-mercato","Mercato &amp; Immobiliare","Quanto costa ristrutturare casa nel 2026","Prezzi al mq voce per voce: impianti, bagni, pavimenti e imprevisti.","12 lug 2026",9),
 ],
 "body": '''<figure class="thumb t-bonus ar-16-9" role="img" aria-label="Interno di appartamento in ristrutturazione con operai al lavoro">
            <span class="thumb-label">Bonus &amp; Fisco</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Nel 2026 la detrazione ristrutturazione vale il <strong>50% per l'abitazione principale</strong> e il <strong>36% per le altre unità immobiliari</strong>.</li>
              <li>Il massimale di spesa resta di <strong>96.000 euro per unità immobiliare</strong>, con recupero in 10 rate annuali.</li>
              <li>Il requisito chiave è la <strong>dimora abituale</strong>: senza di essa, l'aliquota scende dal 50% al 36%.</li>
              <li>La stessa spesa non può essere agevolata due volte: attenzione ai confini con <strong>Ecobonus e Conto Termico</strong>.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#quadro">Il quadro: perché due aliquote</a></li>
              <li><a href="#differenze">50% e 36%: le differenze in sintesi</a></li>
              <li><a href="#abitazione-principale">Il requisito dell'abitazione principale</a></li>
              <li><a href="#calcoli">Esempi di calcolo</a></li>
              <li><a href="#casi-particolari">Casi particolari e cumulabilità</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="quadro">Il quadro: perché due aliquote</h2>
          <p>Il riordino delle agevolazioni per la casa ha introdotto una distinzione destinata a durare: l'aliquota maggiorata del <strong>50% è riservata all'abitazione principale</strong>, mentre tutte le altre unità immobiliari residenziali — seconde case, immobili locati, case dei familiari non conviventi — accedono all'aliquota ordinaria del <strong>36%</strong>. La logica dichiarata del legislatore è concentrare le risorse sulla casa di abitazione e ridurre il costo complessivo delle detrazioni per lo Stato, dopo gli anni record del Superbonus.</p>
          <p>Per famiglie, proprietari e investitori il cambio di passo è significativo: ristrutturare l'immobile in cui si vive conviene molto più che ristrutturare quello da mettere a reddito. Il che influenza le scelte di mercato, dalla tempistica dei lavori alla decisione stessa di vendere o riqualificare, come confermano le tendenze su <a href="costo-ristrutturazione-al-mq-2026.html">costi e domanda di ristrutturazioni nel 2026</a>.</p>

          <h2 id="differenze">50% e 36%: le differenze in sintesi</h2>
          <p>Le due aliquote condividono la stessa architettura — massimale di spesa, recupero decennale, adempimenti — ma producono benefici molto diversi. Il confronto diretto aiuta a capire la posta in gioco.</p>
          <table>
            <thead>
              <tr><th>Voce</th><th>Abitazione principale</th><th>Altre unità immobiliari</th></tr>
            </thead>
            <tbody>
              <tr><td>Aliquota 2026</td><td>50%</td><td>36%</td></tr>
              <tr><td>Massimale di spesa</td><td>96.000 €</td><td>96.000 €</td></tr>
              <tr><td>Detrazione massima</td><td>48.000 €</td><td>34.560 €</td></tr>
              <tr><td>Recupero</td><td>10 rate annuali</td><td>10 rate annuali</td></tr>
              <tr><td>Requisito chiave</td><td>Dimora abituale</td><td>Nessun requisito di dimora</td></tr>
            </tbody>
          </table>
          <p>Su un cantiere da 60.000 euro, la differenza tra le due aliquote vale <strong>8.400 euro</strong> di detrazione: cifra che giustifica da sola la massima attenzione nella qualificazione dell'immobile prima dell'inizio dei lavori.</p>

          <h2 id="abitazione-principale">Il requisito dell'abitazione principale: la vera partita</h2>
          <p>L'aliquota del 50% spetta solo se l'immobile è <strong>abitazione principale</strong>, ovvero quella in cui il contribuente — o il coniuge, o un familiare convivente entro il terzo grado — dimora abitualmente. Tre precisazioni operative:</p>
          <ul>
            <li><strong>Dimora abituale, non solo residenza</strong>: la residenza anagrafica aiuta ma non basta; in caso di controllo conta dove si vive di fatto.</li>
            <li><strong>Lavori prima del trasferimento</strong>: è ammesso ristrutturare prima di traslocare, purché la dimora sia instaurata entro tempi coerenti con l'intervento. In caso contrario, ricalcolo al 36%.</li>
            <li><strong>Un solo immobile</strong>: l'agevolazione maggiorata può riguardare una sola abitazione principale per nucleo; le altre unità seguono l'aliquota ordinaria.</li>
          </ul>
          <p>Attenzione ai casi borderline: casa in comproprietà tra fratelli non conviventi, immobile ceduto in comodato, unità acquistata e affittata in attesa del trasferimento. In tutti questi scenari la documentazione preventiva — e il parere di un fiscalista — fanno la differenza tra una detrazione piena e un contenzioso.</p>

          {AD}

          <h2 id="calcoli">Esempi di calcolo: quanto si recupera davvero</h2>
          <p>Tre scenari tipici mostrano l'impatto delle due aliquote su cantieri di dimensioni diverse. Gli importi sono lordi e non tengono conto di eventuali franchigie o limiti individuali di capienza IRPEF.</p>
          <table>
            <thead>
              <tr><th>Scenario</th><th>Spesa</th><th>Aliquota</th><th>Detrazione totale</th><th>Rata annua</th></tr>
            </thead>
            <tbody>
              <tr><td>Rifacimento bagno e impianti, prima casa</td><td>40.000 €</td><td>50%</td><td>20.000 €</td><td>2.000 €</td></tr>
              <tr><td>Ristrutturazione completa, seconda casa</td><td>80.000 €</td><td>36%</td><td>28.800 €</td><td>2.880 €</td></tr>
              <tr><td>Intervento al massimale, abitazione principale</td><td>96.000 €</td><td>50%</td><td>48.000 €</td><td>4.800 €</td></tr>
            </tbody>
          </table>
          <p>Il vincolo spesso sottovalutato è la <strong>capienza fiscale</strong>: la detrazione si perde nella parte che eccede l'IRPEF dovuta. Conviene quindi simulare la rata annua sul proprio reddito prima di dimensionare il cantiere, soprattutto per pensionati e lavoratori con redditi medio-bassi, per i quali il contributo diretto del <a href="conto-termico-3-guida.html">Conto Termico 3.0</a> può risultare più efficace.</p>

          <h2 id="casi-particolari">Casi particolari e regole di cumulo</h2>
          <p>Sul fronte del cumulo vale il principio generale: <strong>mai due agevolazioni sulla stessa spesa</strong>. È lecito invece sommare bonus diversi su voci distinte dello stesso cantiere — ad esempio Ecobonus per gli infissi e detrazione ristrutturazione per le opere murarie — con computo e fatturazione separati. Per i lavori di efficientamento il riferimento resta la <a href="ecobonus-65-guida.html">guida all'Ecobonus</a>, con i suoi massimali per intervento.</p>
          <p>Altri casi frequenti: gli <strong>interventi sulle parti comuni condominiali</strong> seguono regole proprie con ripartizione millesimale; gli immobili in <strong>patrimonio separato</strong> o in regime di comunione richiedono attenzione alla titolarità delle fatture; per i <strong>familiari conviventi</strong> che sostengono le spese serve la documentazione del vincolo. In tutti i casi, bonifico parlante e titolo edilizio restano i presidi irrinunciabili.</p>
          <blockquote>«Il 50% non è un diritto, è una qualifica: si guadagna con la dimora abituale e si difende con la documentazione. Chi pianifica prima, detrae dopo.»</blockquote>

          <h2 id="faq">Domande frequenti sulle detrazioni 50% e 36%</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> Agenzia delle Entrate — guida "Ristrutturazioni edilizie: le agevolazioni fiscali" e circolari di prassi; articolo 16-bis TUIR; Legge di Bilancio vigente. Contenuto a scopo informativo: per i casi specifici consultare un professionista fiscale o il sito istituzionale.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 5: DIRETTIVA CASE GREEN ============================
ARTICLES.append({
 "slug": "direttiva-case-green-cosa-cambia",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "Direttiva Case Green: cosa cambia | Il Giornale Edile",
 "desc": "Direttiva Case Green UE: obiettivi, scadenze e cosa cambia davvero per gli edifici italiani dal 2026. Obblighi, solare e riqualificazioni energetiche.",
 "kw": "direttiva case green, direttiva ue edifici, case green 2026, prestazione energetica edifici, direttiva epbd",
 "author": "Paolo Riva",
 "date_iso": "2026-07-20T08:00:00+02:00", "date_it": "20 luglio 2026", "tb_date": "Lunedì 20 luglio 2026", "mins": 10,
 "og_title": "Direttiva Case Green UE: cosa cambia per gli edifici italiani dal 2026",
 "og_desc": "Edifici a emissioni zero, obbligo solare e traiettorie nazionali di riqualificazione: la guida per capire cosa è obbligo e cosa no.",
 "tw_title": "Direttiva Case Green: cosa cambia", "tw_desc": "Obiettivi UE e impatti reali sul patrimonio edilizio italiano.",
 "ld_desc": "Direttiva Case Green (UE 2024/1275): obiettivi di decarbonizzazione degli edifici, scadenze 2026-2030, obbligo solare e impatti per l'Italia.",
 "bc_short": "Direttiva Case Green",
 "kicker": "Normative &amp; Cantieri · Europa",
 "h1": "Direttiva Case Green UE: cosa cambia per gli edifici italiani dal 2026",
 "stand": "La direttiva sulla prestazione energetica degli edifici riscrive la rotta del patrimonio immobiliare europeo: nuovi edifici a emissioni zero, pannelli solari progressivamente obbligatori e piani nazionali di riqualificazione. Cosa è vero obbligo e cosa no.",
 "faq": [
  ("Cos'è la Direttiva Case Green?",
   "È la direttiva UE 2024/1275 sulla <strong>prestazione energetica degli edifici</strong> (EPBD), che fissa obiettivi di decarbonizzazione del parco immobiliare europeo: nuovi edifici a emissioni zero dal 2030 e traiettorie nazionali di riduzione dei consumi degli edifici esistenti."),
  ("La direttiva obbliga a ristrutturare casa propria?",
   "No. La direttiva <strong>non impone obblighi diretti ai singoli proprietari</strong>: vincola gli Stati membri a definire piani nazionali di riqualificazione. Eventuali requisiti per gli edifici esistenti dipenderanno da come l'Italia attuerà la direttiva."),
  ("Quando sarà recepita in Italia?",
   "Gli Stati membri hanno tempo fino a <strong>maggio 2026</strong> per il recepimento. In Italia l'attuazione passa da decreti attuativi che aggiorneranno requisiti minimi, certificazione energetica e regole per gli edifici di nuova costruzione."),
  ("Cosa prevede per i pannelli solari?",
   "La direttiva introduce un <strong>obbligo progressivo di installazione solare</strong>: prima sugli edifici pubblici e su quelli nuovi o sottoposti a ristrutturazione rilevante, con scadenze scaglionate fino al 2030, compatibilmente con idoneità tecnica ed economica."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Direttiva Case Green"),("../categoria/normative-cantieri.html","Normativa UE"),("../categoria/energia-rinnovabili.html","Efficienza energetica"),("../categoria/normative-cantieri.html","Riqualificazione edifici")],
 "rel": [
  ("certificazione-ape-regole-2026","t-normative","Normative &amp; Cantieri","Certificazione APE: regole, costi e obblighi","Quando serve l'attestato di prestazione energetica, chi lo redige e quanto costa.","28 giu 2026",7),
  ("ntc-aggiornamenti-sismici","t-normative","Normative &amp; Cantieri","NTC: aggiornamenti e classificazione sismica","Norme Tecniche per le Costruzioni: verifiche, categorie d'uso e zone sismiche.","7 lug 2026",8),
  ("mutui-green-casa-efficiente","t-mercato","Mercato &amp; Immobiliare","Mutui green: finanziare la casa efficiente","Tassi agevolati per immobili in classe energetica alta: come funzionano.","6 lug 2026",6),
  ("fotovoltaico-costi-permessi-2026","t-energia","Energia &amp; Rinnovabili","Fotovoltaico 2026: costi e permessi","Prezzi al kWp, iter autorizzativi e convenienza dell'autoconsumo.","11 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Edificio residenziale moderno con pannelli solari in copertura">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>La Direttiva Case Green (UE 2024/1275) impone <strong>nuovi edifici a emissioni zero dal 2030</strong> (dal 2028 per gli edifici pubblici).</li>
              <li>Gli Stati membri devono ridurre i consumi del patrimonio residenziale esistente secondo <strong>traiettorie nazionali</strong>: obiettivi indicativi di -16% al 2030 e -20/22% al 2035.</li>
              <li><strong>Nessun obbligo diretto di ristrutturazione</strong> per i singoli proprietari: i vincoli nasceranno dai decreti nazionali di attuazione.</li>
              <li>Obbligo progressivo di <strong>installazione solare</strong> su edifici pubblici, nuovi edifici e ristrutturazioni rilevanti, con scadenze scaglionate.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cos-e">Cos'è la Direttiva Case Green</a></li>
              <li><a href="#obiettivi">Gli obiettivi e la tabella di marcia</a></li>
              <li><a href="#solare">L'obbligo progressivo dei pannelli solari</a></li>
              <li><a href="#cosa-non-cambia">Cosa non cambia: le bufale da smontare</a></li>
              <li><a href="#impatto">L'impatto su mercato e professionisti</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cos-e">Cos'è la Direttiva Case Green</h2>
          <p>Con l'espressione <strong>Direttiva Case Green</strong> si indica comunemente la direttiva (UE) 2024/1275 sulla prestazione energetica nell'edilizia, nota come EPBD recast. È il pilastro edilizio del Green Deal europeo: gli edifici rappresentano circa il 40% dei consumi energetici dell'Unione e oltre un terzo delle emissioni, e la maggior parte del patrimonio esistente è stato costruito prima di qualsiasi norma energetica. La direttiva fissa il quadro entro cui gli Stati membri devono decarbonizzare case, uffici e scuole entro il 2050.</p>
          <p>Il meccanismo è quello tipico delle direttive: Bruxelles fissa <strong>obiettivi e principi vincolanti</strong>, mentre gli strumenti concreti — requisiti minimi, incentivi, divieti — vengono definiti a livello nazionale. Per l'Italia, con un parco edilizio tra i più vecchi d'Europa (oltre la metà degli edifici precede il 1976), la partita dell'attuazione è particolarmente delicata e si intreccia con il sistema dei bonus fiscali.</p>

          <h2 id="obiettivi">Gli obiettivi e la tabella di marcia</h2>
          <p>La direttiva articola gli obiettivi su più binari temporali. La tabella riassume le scadenze principali rilevanti per imprese, progettisti e proprietari.</p>
          <table>
            <thead>
              <tr><th>Scadenza</th><th>Obiettivo</th><th>Ambito</th></tr>
            </thead>
            <tbody>
              <tr><td>Maggio 2026</td><td>Recepimento della direttiva</td><td>Stati membri</td></tr>
              <tr><td>2028</td><td>Edifici nuovi a emissioni zero (ZEB)</td><td>Edifici pubblici nuovi</td></tr>
              <tr><td>2030</td><td>Edifici nuovi a emissioni zero</td><td>Tutti i nuovi edifici</td></tr>
              <tr><td>2030</td><td>Riduzione indicativa dei consumi residenziali (-16%)</td><td>Patrimonio esistente</td></tr>
              <tr><td>2035</td><td>Riduzione indicativa (-20/22%)</td><td>Patrimonio esistente</td></tr>
              <tr><td>2040</td><td>Uscita graduale dalle caldaie a combustibile fossile</td><td>Traiettoria UE</td></tr>
            </tbody>
          </table>
          <p>Per gli edifici esistenti la direttiva introduce lo strumento delle <strong>traiettorie nazionali di riqualificazione</strong>: ogni Paese deve presentare un piano che riduca progressivamente la prestazione energetica media del patrimonio, concentrando gli sforzi sugli edifici con le prestazioni peggiori. I dettagli — soglie, scadenze, incentivi — saranno definiti dai decreti attuativi italiani.</p>

          <h2 id="solare">L'obbligo progressivo dei pannelli solari</h2>
          <p>Uno degli elementi più concreti della direttiva è l'introduzione di un <strong>obbligo scaglionato di installazione di impianti solari</strong> (fotovoltaici o termici), dove tecnicamente idoneo ed economicamente fattibile. La sequenza prevista parte dagli edifici pubblici esistenti e dai nuovi edifici pubblici, per estendersi ai nuovi edifici non residenziali, alle ristrutturazioni rilevanti e infine, entro il 2030, ai nuovi edifici residenziali.</p>
          <p>Per le imprese installatrici e i progettisti questo si traduce in una domanda strutturale di integrazione solare in copertura, già visibile nella crescita del settore descritta nel nostro approfondimento su <a href="fotovoltaico-costi-permessi-2026.html">costi e permessi del fotovoltaico nel 2026</a>. Le deroghe riguarderanno edifici vincolati, coperture con ombreggiamenti critici e casi di dimostrata sproporzione economica.</p>

          {AD}

          <h2 id="cosa-non-cambia">Cosa non cambia: le bufale da smontare</h2>
          <p>Attorno alla direttiva circolano letture errate che vale la pena correggere con chiarezza:</p>
          <ul>
            <li><strong>Nessun divieto di vendita o affitto</strong> per le case energivore imposto direttamente da Bruxelles: la direttiva non contiene obblighi per i singoli cittadini.</li>
            <li><strong>Nessuna scadenza 2030 per ristrutturare casa propria</strong>: il 2030 riguarda i nuovi edifici e gli obiettivi aggregati nazionali, non il singolo immobile.</li>
            <li><strong>Le classi energetiche non diventano automaticamente titoli di esclusione</strong>: eventuali meccanismi nazionali saranno discussi in sede di recepimento, con ampi margini di gradualità.</li>
          </ul>
          <p>Questo non significa che il mercato resti fermo: il valore degli immobili efficienti cresce, i finanziamenti verdi si diffondono — ne parliamo nell'articolo sui <a href="mutui-green-casa-efficiente.html">mutui green per la casa efficiente</a> — e la certificazione energetica diventa sempre più centrale nelle transazioni, come dettagliato nella guida alla <a href="certificazione-ape-regole-2026.html">certificazione APE</a>.</p>

          <h2 id="impatto">L'impatto su mercato, imprese e professionisti</h2>
          <p>Per la filiera delle costruzioni la direttiva disegna un quadro di domanda di lungo periodo: riqualificazioni dell'involucro, sostituzione dei generatori a fossile, integrazione solare e gestione intelligente degli impianti. I decreti attuativi italiani aggiorneranno i <strong>requisiti minimi di prestazione energetica</strong> per nuove costruzioni e ristrutturazioni, la normativa sulla certificazione APE e le regole per gli edifici a emissioni zero, ridefinendo di fatto lo standard di progetto.</p>
          <p>Le incognite riguardano le risorse: il raggiungimento delle traiettorie richiede un flusso stabile di incentivi, dopo che la stagione del Superbonus ha mostrato sia la potenza sia i rischi fiscali delle agevolazioni massicce. La sfida del legislatore nazionale sarà trovare un equilibrio tra ambizione europea e sostenibilità dei conti, possibilmente con strumenti strutturali come crediti d'imposta mirati, deduzioni e finanza verde.</p>
          <blockquote>«La direttiva non entra in casa di nessuno con la forza, ma cambia il valore di tutte le case: nei prossimi dieci anni l'efficienza energetica sarà una variabile di prezzo, non solo di bolletta.»</blockquote>

          <h2 id="faq">Domande frequenti sulla Direttiva Case Green</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> Direttiva (UE) 2024/1275 del Parlamento europeo e del Consiglio; Commissione europea — schede sul pacchetto "Pronti per il 55%"; Ministero dell'Ambiente e della Sicurezza Energetica — lavori di recepimento. Contenuto a scopo informativo: fare riferimento ai testi ufficiali e ai decreti attuativi nazionali.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 6: CERTIFICAZIONE APE ============================
ARTICLES.append({
 "slug": "certificazione-ape-regole-2026",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "Certificazione APE: regole e costi 2026 | Il Giornale Edile",
 "desc": "Certificazione energetica APE: cos'è, quando è obbligatoria, quanto costa e quanto dura. Classi, sanzioni e regole aggiornate per vendita e affitto.",
 "kw": "certificazione energetica ape, ape obbligatoria, costo ape, attestato prestazione energetica, classi energetiche edifici",
 "author": "Giulia Santi",
 "date_iso": "2026-06-28T08:00:00+02:00", "date_it": "28 giugno 2026", "tb_date": "Domenica 28 giugno 2026", "mins": 8,
 "og_title": "Certificazione energetica APE: regole, costi e quando è obbligatoria",
 "og_desc": "Dalle classi A4 a G alle sanzioni per chi non la consegna: la guida completa all'attestato di prestazione energetica tra vendite, affitti e bonus.",
 "tw_title": "APE: regole, costi e obblighi", "tw_desc": "Quando serve, chi la redige, quanto dura: la guida completa.",
 "ld_desc": "Certificazione energetica APE: obblighi per vendita e locazione, classi da A4 a G, costi indicativi, validità 10 anni e sanzioni.",
 "bc_short": "Certificazione APE",
 "kicker": "Normative &amp; Cantieri · Guida pratica",
 "h1": "Certificazione energetica APE: regole, costi e quando è obbligatoria",
 "stand": "È la carta d'identità energetica dell'edificio: senza APE non si vende, non si affitta e non si accede a gran parte dei bonus. Regole aggiornate, costi reali, sanzioni e trucchi per leggerla bene prima di comprare casa.",
 "faq": [
  ("Quando è obbligatoria la certificazione APE?",
   "L'APE è obbligatoria per <strong>vendita, nuovo contratto di locazione, nuova costruzione, ristrutturazione rilevante</strong> e per accedere alla maggior parte delle agevolazioni fiscali sull'efficienza energetica. Deve essere allegata all'atto notarile."),
  ("Quanto costa un attestato di prestazione energetica?",
   "Per un appartamento standard il costo di mercato è indicativamente tra <strong>100 e 300 euro</strong>, comprensivi di sopralluogo, calcolo e registrazione al catasto energetico regionale. Edifici complessi o grandi superfici costano di più."),
  ("Quanto dura la validità dell'APE?",
   "L'attestato ha validità di <strong>10 anni</strong> dalla data di rilascio, a condizione che non siano eseguiti interventi che modifichino la prestazione energetica dell'edificio: in tal caso va aggiornato."),
  ("Cosa succede se si vende casa senza APE?",
   "La mancata consegna dell'attestato in caso di vendita comporta una <strong>sanzione amministrativa pecuniaria</strong> (indicativamente da 3.000 a 18.000 euro, salvo aggiornamenti regionali) a carico del venditore, oltre a possibili contestazioni sull'atto."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Certificazione APE"),("../categoria/energia-rinnovabili.html","Efficienza energetica"),("../categoria/mercato-immobiliare.html","Compravendita"),("../categoria/normative-cantieri.html","Normativa edilizia")],
 "rel": [
  ("direttiva-case-green-cosa-cambia","t-normative","Normative &amp; Cantieri","Direttiva Case Green: cosa cambia dal 2026","Obiettivi UE, obbligo solare e impatti reali sul patrimonio edilizio italiano.","20 lug 2026",10),
  ("ecobonus-65-guida","t-bonus","Bonus &amp; Fisco","Ecobonus: come funziona e interventi ammessi","Aliquote, requisiti tecnici e adempimenti per la detrazione energetica.","15 lug 2026",9),
  ("mercato-immobiliare-2026-prezzi","t-mercato","Mercato &amp; Immobiliare","Mercato immobiliare 2026: prezzi e tendenze","Compravendite, quotazioni e il peso crescente della classe energetica.","14 lug 2026",8),
  ("mutui-green-casa-efficiente","t-mercato","Mercato &amp; Immobiliare","Mutui green: finanziare la casa efficiente","Condizioni agevolate per gli immobili in classe A e B: come accedervi.","6 lug 2026",6),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Tecnico certificatore rilieva i dati energetici di un appartamento">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>L'APE è obbligatoria per <strong>vendita, affitto, nuova costruzione e accesso ai bonus</strong> energetici.</li>
              <li>Classifica l'edificio dalla <strong>classe A4 (la migliore) alla G</strong>, con l'indice di prestazione energetica IPE.</li>
              <li>Costo indicativo di mercato: <strong>100-300 euro</strong> per un appartamento; validità <strong>10 anni</strong>.</li>
              <li>Vendere senza APE espone a <strong>sanzioni pecuniarie</strong> e contestazioni: deve essere consegnata all'acquirente e allegata all'atto.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cos-e">Cos'è l'APE e come si legge</a></li>
              <li><a href="#quando">Quando è obbligatoria</a></li>
              <li><a href="#chi-costi">Chi la redige e quanto costa</a></li>
              <li><a href="#validita">Validità, aggiornamento e sanzioni</a></li>
              <li><a href="#strategie">Come migliorare la classe prima di vendere</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cos-e">Cos'è l'APE e come si legge</h2>
          <p>L'<strong>Attestato di Prestazione Energetica</strong> (APE) è il documento che fotografa l'efficienza energetica di un edificio o di una singola unità immobiliare. Introdotto in attuazione delle direttive europee e disciplinato in Italia dal decreto legislativo 192/2005 e dal decreto requisiti minimi del 2015, assegna all'immobile una <strong>classe energetica dalla A4 — la più performante — alla G</strong>, sulla base di indici calcolati con metodologia standardizzata.</p>
          <p>Gli indicatori chiave da leggere per primi sono l'<strong>IPE globale</strong> (kWh/mq anno di energia primaria non rinnovabile), che determina la classe, e la distinzione tra consumi per riscaldamento, raffrescamento e acqua calda sanitaria. L'attestato riporta inoltre le <strong>raccomandazioni del certificatore</strong>: gli interventi con il miglior rapporto costo-beneficio per salire di classe, informazione preziosa sia per chi compra sia per chi pianifica una ristrutturazione.</p>

          <h2 id="quando">Quando è obbligatoria la certificazione APE</h2>
          <p>L'obbligo copre gran parte del ciclo di vita dell'immobile. La tabella sintetizza le fattispecie principali e le conseguenze della violazione.</p>
          <table>
            <thead>
              <tr><th>Caso</th><th>Obbligo</th><th>Rischio in caso di mancanza</th></tr>
            </thead>
            <tbody>
              <tr><td>Vendita di immobile</td><td>APE allegata all'atto e consegnata all'acquirente</td><td>Sanzione pecuniaria per il venditore</td></tr>
              <tr><td>Nuovo contratto di locazione</td><td>APE consegnata al conduttore</td><td>Sanzione pecuniaria per il locatore</td></tr>
              <tr><td>Nuova costruzione</td><td>APE obbligatoria per l'agibilità</td><td>Mancato rilascio del titolo</td></tr>
              <tr><td>Ristrutturazione rilevante</td><td>APE post-intervento</td><td>Inadempimento verso il Comune</td></tr>
              <tr><td>Annunci immobiliari</td><td>Indicazione di classe e IPE</td><td>Sanzione per intermediari e proprietari</td></tr>
              <tr><td>Accesso ai bonus energetici</td><td>APE ante e/o post intervento</td><td>Perdita dell'agevolazione</td></tr>
            </tbody>
          </table>
          <p>Per gli annunci di vendita e affitto la norma impone di esporre classe energetica e indice IPE già nella pubblicità: un dettaglio che ha progressivamente educato il mercato, rendendo la classe un <strong>parametro di confronto</strong> tra annunci, insieme a prezzo e metratura.</p>

          <h2 id="chi-costi">Chi la redige e quanto costa</h2>
          <p>L'APE può essere redatta solo da un <strong>certificatore energetico accreditato</strong>: architetti, ingegneri, geometri, periti e altri tecnici abilitati che abbiano seguito il corso riconosciuto dalla regione (80 ore per chi non è progettista) e siano iscritti al relativo elenco. Il certificatore è terzo rispetto alla proprietà e risponde civilmente e penalmente delle attestazioni.</p>
          <p>Il procedimento standard prevede il <strong>sopralluogo obbligatorio</strong>, la raccolta dei dati su involucro e impianti, il calcolo con software certificato CTU e la registrazione telematica al catasto energetico regionale, con tassa di registrazione variabile tra le regioni. I prezzi di mercato per un appartamento di medie dimensioni si attestano indicativamente tra <strong>100 e 300 euro</strong>, salvo complessità: attenzione alle offerte anomale a poche decine di euro, spesso sintomo di pratiche senza sopralluogo, irregolari e rischiose.</p>

          {AD}

          <h2 id="validita">Validità, aggiornamento e sanzioni</h2>
          <p>L'attestato dura <strong>10 anni</strong> dalla data di rilascio, ma decade prima se vengono eseguiti lavori che modificano la prestazione energetica: sostituzione della caldaia, nuovi infissi, coibentazioni. In questi casi l'APE va aggiornata — adempimento che per alcuni bonus, come l'<a href="ecobonus-65-guida.html">Ecobonus</a>, è parte integrante degli obblighi documentali.</p>
          <p>Sul fronte sanzionatorio, la vendita senza consegna dell'attestato espone a una <strong>multa amministrativa indicativamente tra 3.000 e 18.000 euro</strong>, con aggiornamenti demandati alle regioni; la locazione senza APE prevede sanzioni proporzionate. Oltre alla multa, la mancanza può generare contestazioni contrattuali: l'acquirente può rivalersi se la classe dichiarata non corrisponde al vero.</p>

          <h2 id="strategie">Come migliorare la classe prima di vendere</h2>
          <p>Con il mercato che premia le classi alte — le analisi sul <a href="mercato-immobiliare-2026-prezzi.html">mercato immobiliare 2026</a> registrano differenziali di prezzo significativi tra classi A-B e F-G nelle grandi città — migliorare l'APE prima della vendita può essere un investimento redditizio. Gli interventi con il miglior rapporto costo-risultato sono in genere:</p>
          <ul>
            <li><strong>Sostituzione del generatore di calore</strong> con caldaia a condensazione o pompa di calore;</li>
            <li><strong>Valvole termostatiche e contabilizzazione</strong>, dove mancanti;</li>
            <li><strong>Sostituzione degli infissi</strong> nelle unità più datate;</li>
            <li><strong>Insufflaggio delle intercapedini</strong>, intervento rapido e poco invasivo;</li>
            <li><strong>Pompa di calore per l'acqua calda sanitaria</strong> e luci a LED nelle parti comuni.</li>
          </ul>
          <p>Molti di questi lavori godono delle agevolazioni fiscali vigenti, dal bonus ristrutturazione al Conto Termico, riducendo l'esborso effettivo. Il contesto di lungo periodo è tracciato dalla <a href="direttiva-case-green-cosa-cambia.html">Direttiva Case Green</a>, che renderà la prestazione energetica ancora più centrale nel valore degli immobili.</p>
          <blockquote>«L'APE non è una tassa sulla burocrazia: è il prezzo della trasparenza. Chi vende una casa in classe A vende un prodotto diverso da chi vende la stessa casa in classe G.»</blockquote>

          <h2 id="faq">Domande frequenti sulla certificazione APE</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> Decreto legislativo 192/2005 e s.m.i.; decreto requisiti minimi 26 giugno 2015; linee guida nazionali per la certificazione energetica; portali dei catasti energetici regionali. Contenuto a scopo informativo: per i casi specifici consultare un certificatore accreditato o la normativa regionale.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 7: CODICE APPALTI ============================
ARTICLES.append({
 "slug": "codice-appalti-dlgs-36-2023",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "Codice Appalti D.Lgs 36/2023: le novità | Il Giornale Edile",
 "desc": "Nuovo Codice degli Appalti D.Lgs 36/2023: digitalizzazione, soglie, qualificazione e subappalto. Le novità per imprese edili e professionisti.",
 "kw": "codice appalti 2023, d.lgs 36/2023, nuovo codice appalti, appalti pubblici edilizia, digitalizzazione appalti",
 "author": "Paolo Riva",
 "date_iso": "2026-07-09T08:00:00+02:00", "date_it": "9 luglio 2026", "tb_date": "Giovedì 9 luglio 2026", "mins": 9,
 "og_title": "Nuovo Codice degli Appalti (D.Lgs 36/2023): le novità per imprese e professionisti",
 "og_desc": "Ciclo di vita digitale, affidamenti sotto soglia, qualificazione SOA e nuove regole sul subappalto: la mappa operativa del Codice a regime.",
 "tw_title": "Codice Appalti: le novità chiave", "tw_desc": "Digitalizzazione, soglie e subappalto nel D.Lgs 36/2023.",
 "ld_desc": "Codice degli Appalti D.Lgs 36/2023: digitalizzazione del ciclo di vita, soglie di affidamento, qualificazione delle imprese e regole sul subappalto.",
 "bc_short": "Codice Appalti D.Lgs 36/2023",
 "kicker": "Normative &amp; Cantieri · Appalti pubblici",
 "h1": "Nuovo Codice degli Appalti (D.Lgs 36/2023): le novità per imprese e professionisti",
 "stand": "A regime da oltre tre anni, il Codice ha cambiato il modo di progettare, gareggiare ed eseguire i lavori pubblici: digitalizzazione obbligatoria, nuove soglie, qualificazione ripensata. Il punto operativo per chi lavora con la PA.",
 "faq": [
  ("Quali sono i principi fondamentali del D.Lgs 36/2023?",
   "Il Codice si fonda sui principi di <strong>risultato, fiducia e accesso al mercato</strong>: le stazioni appaltanti sono incentivate a valutare l'esito dell'intervento, la discrezionalità amministrativa è rafforzata e la partecipazione delle piccole imprese è favorita."),
  ("Qual è la soglia per l'affidamento diretto dei lavori?",
   "Per i lavori, l'affidamento diretto è ammesso per importi <strong>inferiori a 150.000 euro</strong>. Oltre questa soglia e fino alla soglia comunitaria si ricorre a procedure negoziate con un numero crescente di operatori invitati."),
  ("Cosa cambia per il subappalto?",
   "Il Codice ha mantenuto il <strong>divieto di subappalto oltre certi limiti</strong> per i contratti sopra soglia comunitaria, con regole rafforzate su tracciabilità, autorizzazione preventiva e responsabilità solidale, salvo aggiornamenti dei decreti correttivi."),
  ("Cos'è il fascicolo virtuale dell'operatore economico?",
   "È il contenitore digitale, istituito presso l'ANAC, che raccoglie i <strong>dati e i documenti dell'impresa</strong> (certificazioni, qualificazioni SOA, casellario) per semplificare la partecipazione alle gare attraverso piattaforme certificate."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Codice Appalti"),("../categoria/normative-cantieri.html","Lavori pubblici"),("../categoria/materiali-tecnologie.html","Digitalizzazione"),("../categoria/normative-cantieri.html","Normativa edilizia")],
 "rel": [
  ("sicurezza-cantiere-dlgs-81-novita","t-normative","Normative &amp; Cantieri","Sicurezza in cantiere: le novità del D.Lgs 81/08","Patentino a crediti, coordinamento e sanzioni: cosa cambia per le imprese.","16 lug 2026",8),
  ("ntc-aggiornamenti-sismici","t-normative","Normative &amp; Cantieri","NTC: aggiornamenti e classificazione sismica","Norme Tecniche per le Costruzioni: verifiche e categorie d'uso aggiornate.","7 lug 2026",8),
  ("bim-obbligatorio-scadenze","t-materiali","Materiali &amp; Tecnologie","BIM obbligatorio: le scadenze per i lavori pubblici","Calendario dell'obbligo BIM per soglia di importo e strumenti per adeguarsi.","3 lug 2026",7),
  ("top-5-imprese-costruzione-italia","t-mercato","Mercato &amp; Immobiliare","Le 5 maggiori imprese di costruzione italiane","Fatturati, commesse e strategie dei principali general contractor nazionali.","17 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Cantiere di un'opera pubblica con gru e impalcature">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Il D.Lgs 36/2023 è il <strong>Codice dei contratti pubblici</strong> in vigore dal 1° aprile 2023, fondato su risultato, fiducia e accesso al mercato.</li>
              <li><strong>Affidamento diretto sotto i 150.000 euro</strong> per i lavori; procedure negoziate fino alla soglia comunitaria.</li>
              <li><strong>Digitalizzazione obbligatoria</strong> del ciclo di vita dei contratti: piattaforme certificate, fascicolo virtuale dell'operatore economico.</li>
              <li>Regole rafforzate su <strong>subappalto, qualificazione SOA</strong> e progettazione, con il BIM progressivamente obbligatorio nei lavori pubblici.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#quadro">Il quadro: principi e architettura del Codice</a></li>
              <li><a href="#soglie">Soglie e procedure di affidamento</a></li>
              <li><a href="#digitalizzazione">La digitalizzazione del ciclo di vita</a></li>
              <li><a href="#qualificazione">Qualificazione SOA e subappalto</a></li>
              <li><a href="#professionisti">Cosa cambia per progettisti e professionisti</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="quadro">Il quadro: principi e architettura del Codice</h2>
          <p>Il <strong>decreto legislativo 36/2023</strong>, entrato in vigore il 1° aprile 2023, ha sostituito il precedente Codice dei contratti pubblici (D.Lgs 50/2016) con un'impostazione nuova: pochi principi generali nel testo principale, regole operative demandate ad allegati e linee guida ANAC. Tre i cardini dichiarati: il <strong>principio del risultato</strong>, che orienta ogni scelta della stazione appaltante al miglior esito possibile dell'intervento; il <strong>principio della fiducia</strong>, che riduce i formalismi e rafforza la discrezionalità motivata dei funzionari; il <strong>principio dell'accesso al mercato</strong>, pensato per allargare la platea delle imprese partecipanti.</p>
          <p>A oltre tre anni dall'entrata in vigore, e dopo i decreti correttivi che ne hanno ritoccato diversi passaggi, il Codice è ormai il riferimento quotidiano di chi progetta, gareggia ed esegue lavori pubblici. Conoscerne la logica è condizione per non restare fuori dalle gare.</p>

          <h2 id="soglie">Soglie e procedure di affidamento</h2>
          <p>Il sistema delle soglie definisce quale procedura usare in base all'importo stimato del contratto. La tabella riassume lo schema per i lavori, sempre salvo aggiornamenti delle soglie comunitarie e dei decreti attuativi.</p>
          <table>
            <thead>
              <tr><th>Importo lavori</th><th>Procedura</th><th>Note operative</th></tr>
            </thead>
            <tbody>
              <tr><td>Fino a 150.000 €</td><td>Affidamento diretto</td><td>Anche senza consultazione di più preventivi</td></tr>
              <tr><td>150.000 € - 1 milione €</td><td>Procedura negoziata</td><td>Consultazione di almeno 5 operatori, se esistenti</td></tr>
              <tr><td>1 milione € - soglia comunitaria</td><td>Procedura negoziata</td><td>Consultazione di almeno 10 operatori</td></tr>
              <tr><td>Oltre soglia comunitaria</td><td>Procedure ordinarie (aperta, ristretta, competitiva)</td><td>Bando pubblicato anche in Gazzetta UE</td></tr>
            </tbody>
          </table>
          <p>L'ampliamento dell'affidamento diretto ha velocizzato i piccoli interventi di manutenzione, ma richiede alle stazioni appaltanti rotazioni genuine e motivazioni puntuali: l'ANAC vigila sulle pratiche di frazionamento artificioso, che restano vietate.</p>

          <h2 id="digitalizzazione">La digitalizzazione del ciclo di vita</h2>
          <p>La riforma ha introdotto l'obbligo di <strong>digitalizzazione integrale del ciclo di vita dei contratti</strong>: dalla programmazione all'esecuzione, ogni passaggio transita su piattaforme di approvvigionamento digitale certificate. Le tessere del mosaico comprendono:</p>
          <ul>
            <li>la <strong>Banca dati nazionale dei contratti pubblici</strong> (BDNCP) dell'ANAC, verso cui convergono tutti i dati delle procedure;</li>
            <li>il <strong>Fascicolo virtuale dell'operatore economico</strong> (FVOE), che centralizza documenti e certificazioni dell'impresa riducendo gli oneri ripetitivi in gara;</li>
            <li>l'<strong>e-procurement</strong> obbligatorio per gare, comunicazioni e pagamenti;</li>
            <li>l'integrazione progressiva con gli strumenti <strong>BIM</strong> per la progettazione e la gestione dell'opera, secondo il calendario dell'obbligo descritto nel nostro articolo sul <a href="bim-obbligatorio-scadenze.html">BIM obbligatorio e le sue scadenze</a>.</li>
          </ul>
          <p>Per le imprese la digitalizzazione non è più un'opzione: serve una dotazione informatica minima, firme digitali e procedure interne ordinate, pena l'esclusione dalle procedure più strutturate.</p>

          {AD}

          <h2 id="qualificazione">Qualificazione SOA e subappalto: le regole da conoscere</h2>
          <p>La <strong>qualificazione SOA</strong> resta il passaporto per i lavori pubblici sopra la soglia di 150.000 euro: l'attestazione certifica la capacità tecnico-economica dell'impresa nelle categorie generali (OG) e specializzate (OS). Il Codice ha confermato il sistema introducendo correttivi su verifiche, schede di qualificazione e gestione dei raggruppamenti.</p>
          <p>Sul <strong>subappalto</strong>, la disciplina mantiene un impianto restrittivo per i contratti sopra soglia comunitaria, con autorizzazione preventiva della stazione appaltante, divieto di cessione totale, tracciabilità dei pagamenti e responsabilità solidale dell'appaltatore per retribuzioni e versamenti. Le modifiche introdotte dai decreti correttivi e dalla legislazione collegata al PNRR hanno ritoccato più volte i confini: la verifica del testo vigente prima di ogni contratto è prassi indispensabile, così come l'attenzione agli adempimenti di sicurezza trattati nell'articolo sulle <a href="sicurezza-cantiere-dlgs-81-novita.html">novità del D.Lgs 81/08 in cantiere</a>.</p>

          <h2 id="professionisti">Cosa cambia per progettisti e professionisti</h2>
          <p>Per ingegneri, architetti e geometri il Codice ha ridisegnato il rapporto con la commessa pubblica. I punti essenziali:</p>
          <ul>
            <li><strong>Livelli di progettazione</strong>: il sistema resta articolato su quadro esigenziale, documento di fattibilità, progetto tecnico ed esecutivo, con l'appalto integrato ammesso in casi più ampi rispetto al passato ma sempre condizionato alla completezza della progettazione preliminare.</li>
            <li><strong>Metodi digitali</strong>: la progettazione BIM è richiesta per fasce crescenti di lavori pubblici; le stazioni appaltanti devono dotarsi di piani di gestione informativa.</li>
            <li><strong>Direzione lavori e collaudi</strong>: responsabilità e procedure aggiornate, con verifiche in corso d'opera semplificate sotto soglia.</li>
            <li><strong>Verifica della progettazione</strong>: resta obbligatoria per i lavori oltre i limiti fissati, svolta da soggetti qualificati.</li>
          </ul>
          <p>Il quadro tecnico di riferimento resta quello delle Norme Tecniche per le Costruzioni, di cui parliamo nell'approfondimento sugli <a href="ntc-aggiornamenti-sismici.html">aggiornamenti NTC e la classificazione sismica</a>: progetto di gara e progetto esecutivo devono dialogare con entrambi i sistemi normativi.</p>
          <blockquote>«Il nuovo Codice premia chi arriva preparato: documenti digitali in ordine, qualificazione aggiornata e capacità di leggere il principio del risultato prima ancora del disciplinare di gara.»</blockquote>

          <h2 id="faq">Domande frequenti sul Codice degli Appalti</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> D.Lgs 31 marzo 2023, n. 36 e decreti correttivi; ANAC — linee guida e atti di indirizzo; Banca dati nazionale dei contratti pubblici. Contenuto a scopo informativo: per le singole procedure fare riferimento ai testi ufficiali vigenti e ai pareri dell'ANAC.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 8: NTC ============================
ARTICLES.append({
 "slug": "ntc-aggiornamenti-sismici",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "NTC: aggiornamenti e classi sismiche | Il Giornale Edile",
 "desc": "Norme Tecniche per le Costruzioni: classificazione sismica, categorie d'uso, verifiche e aggiornamenti. Cosa devono sapere imprese e progettisti.",
 "kw": "norme tecniche costruzioni, ntc 2018, classificazione sismica italia, verifiche sismiche, categorie d'uso strutture",
 "author": "Luca Brambilla",
 "date_iso": "2026-07-07T08:00:00+02:00", "date_it": "7 luglio 2026", "tb_date": "Martedì 7 luglio 2026", "mins": 9,
 "og_title": "Norme Tecniche per le Costruzioni: aggiornamenti e classificazione sismica",
 "og_desc": "Zone sismiche, stati limite, categorie d'uso e vita nominale: la bussola per orientarsi nel sistema normativo delle costruzioni.",
 "tw_title": "NTC e classificazione sismica", "tw_desc": "Zone, verifiche e categorie d'uso: la guida operativa.",
 "ld_desc": "Norme Tecniche per le Costruzioni (DM 17/1/2018): classificazione sismica del territorio, stati limite, categorie d'uso e aggiornamenti normativi.",
 "bc_short": "NTC e classificazione sismica",
 "kicker": "Normative &amp; Cantieri · Strutture",
 "h1": "Norme Tecniche per le Costruzioni: aggiornamenti e classificazione sismica",
 "stand": "Sono la grammatica del costruire in Italia: le NTC definiscono come si progetta in sicurezza, dalle zone sismiche alle verifiche agli stati limite. La guida per orientarsi tra aggiornamenti, circolari e obblighi per imprese e progettisti.",
 "faq": [
  ("Cosa sono le Norme Tecniche per le Costruzioni?",
   "Le NTC, approvate con <strong>DM 17 gennaio 2018</strong>, sono il riferimento tecnico obbligatorio per la progettazione, esecuzione e collaudo delle costruzioni in Italia: definiscono azioni, materiali, verifiche di sicurezza e criteri antisismici."),
  ("Com'è classificato sismicamente il territorio italiano?",
   "L'Italia è suddivisa in <strong>4 zone sismiche</strong>, dalla zona 1 (più pericolosa) alla zona 4 (a pericolosità minore). La classificazione è comunale e incide su verifiche obbligatorie e opere in edilizia libera."),
  ("Cosa sono gli stati limite nelle verifiche strutturali?",
   "Sono le condizioni oltre le quali la struttura non soddisfa più le prestazioni richieste. Le NTC distinguono <strong>stati limite ultimi</strong> (sicurezza, inclusi SLV e SLC per il sisma) e <strong>stati limite di esercizio</strong> (funzionalità, SLD e SLO)."),
  ("Chi può firmare un progetto strutturale?",
   "Il progetto delle strutture deve essere redatto da un <strong>professionista abilitato iscritto all'ordine</strong> (ingegnere o architetto, secondo le competenze), depositato al Genio Civile quando richiesto, con relazione di calcolo e verifiche agli stati limite."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Norme Tecniche Costruzioni"),("../categoria/normative-cantieri.html","Rischio sismico"),("../categoria/normative-cantieri.html","Progettazione strutturale"),("../categoria/bonus-fiscali.html","Sismabonus")],
 "rel": [
  ("codice-appalti-dlgs-36-2023","t-normative","Normative &amp; Cantieri","Codice Appalti D.Lgs 36/2023: le novità","Soglie, digitalizzazione e subappalto: la mappa per i lavori pubblici.","9 lug 2026",9),
  ("sicurezza-cantiere-dlgs-81-novita","t-normative","Normative &amp; Cantieri","Sicurezza in cantiere: le novità del D.Lgs 81/08","Patentino a crediti, figure della sicurezza e sanzioni aggiornate.","16 lug 2026",8),
  ("bonus-ristrutturazione-2026-guida-completa","t-bonus","Bonus &amp; Fisco","Bonus Ristrutturazione 2026: la guida completa","Aliquote, massimali e adempimenti anche per le opere antisismiche.","21 lug 2026",9),
  ("edilizia-legno-xlam","t-materiali","Materiali &amp; Tecnologie","Edilizia in legno XLAM: vantaggi e limiti","Strutture leggere e performanti in zona sismica: costi e applicazioni.","1 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Struttura in cemento armato in costruzione con armature a vista">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Le NTC (DM 17/1/2018) sono il <strong>riferimento obbligatorio</strong> per progettazione, esecuzione e collaudo delle costruzioni in Italia.</li>
              <li>Il territorio è diviso in <strong>4 zone sismiche</strong>: la zona 1 è la più pericolosa, la 4 la meno esposta.</li>
              <li>Le verifiche si basano sugli <strong>stati limite</strong>: ultimi (SLV, SLC) per la sicurezza, di esercizio (SLD, SLO) per la funzionalità.</li>
              <li><strong>Categorie d'uso e vita nominale</strong> determinano il livello di prestazione richiesto a ciascuna opera.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#cosa-sono">Cosa sono le NTC e come sono organizzate</a></li>
              <li><a href="#classificazione">La classificazione sismica del territorio</a></li>
              <li><a href="#verifiche">Stati limite e verifiche di sicurezza</a></li>
              <li><a href="#categorie">Categorie d'uso e vita nominale</a></li>
              <li><a href="#esistente">Il patrimonio esistente: miglioramento e adeguamento</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="cosa-sono">Cosa sono le NTC e come sono organizzate</h2>
          <p>Le <strong>Norme Tecniche per le Costruzioni</strong>, approvate con decreto ministeriale il 17 gennaio 2018, sono il testo che regola il costruire in Italia: dalle fondazioni alle coperture, dal cemento armato al legno, dall'acciaio alla muratura. Il decreto definisce le <strong>azioni sulle strutture</strong> (peso proprio, neve, vento, sisma), i criteri di modellazione, i materiali ammessi e i metodi di verifica. A completamento opera la <strong>Circolare applicativa</strong>, che illustra l'interpretazione delle norme capitolo per capitolo.</p>
          <p>Le NTC hanno natura di <strong>norma cogente</strong>: non sono un'indicazione volontaria ma il riferimento contro cui si misura la legittimità di un progetto depositato al Genio Civile e la responsabilità di chi progetta, dirige e collauda. Per questo ogni aggiornamento — dal testo unico delle circolari ai decreti che modificano singoli capitoli — ha ricadute immediate sul lavoro quotidiano di studi e cantieri.</p>

          <h2 id="classificazione">La classificazione sismica del territorio italiano</h2>
          <p>L'Italia è interamente classificata dal punto di vista sismico: ogni comune ricade in una delle <strong>4 zone</strong> definite dall'ordinanza PCM 3274/2003 e dagli aggiornamenti successivi, in coerenza con la mappa di pericolosità sismica nazionale. La zona determina l'accelerazione di riferimento del terreno e, di conseguenza, lo spettro di progetto da utilizzare nelle verifiche.</p>
          <table>
            <thead>
              <tr><th>Zona</th><th>Pericolosità</th><th>Implicazioni principali</th></tr>
            </thead>
            <tbody>
              <tr><td>Zona 1</td><td>Alta</td><td>Verifiche sismiche complete, deposito strutture obbligatorio, massima severità di progetto</td></tr>
              <tr><td>Zona 2</td><td>Medio-alta</td><td>Verifiche sismiche obbligatorie, criteri costruttivi antisismici</td></tr>
              <tr><td>Zona 3</td><td>Medio-bassa</td><td>Verifiche sismiche con parametri ridotti</td></tr>
              <tr><td>Zona 4</td><td>Bassa</td><td>Verifiche semplificate; restano i requisiti minimi di sicurezza</td></tr>
            </tbody>
          </table>
          <p>La classificazione incide anche sul fronte amministrativo: in zone 1, 2 e 3 il progetto delle strutture va depositato agli uffici tecnici competenti (ex Genio Civile), mentre alcune opere minori in zona 4 possono ricadere in regimi semplificati. Gli strumenti di <strong>microzonazione sismica</strong>, dove disponibili, affinano il quadro a scala locale e possono modificare i parametri di progetto in modo significativo.</p>

          <h2 id="verifiche">Stati limite e verifiche di sicurezza: la logica delle NTC</h2>
          <p>Il cuore metodologico delle NTC è la verifica agli <strong>stati limite</strong>: la struttura deve garantire prestazioni crescenti al crescere della severità dell'evento. Per l'azione sismica la gerarchia comprende:</p>
          <ul>
            <li><strong>SLO</strong> (stato limite di operatività): dopo il sisma l'opera resta pienamente funzionante;</li>
            <li><strong>SLD</strong> (stato limite di danno): danni limitati e riparabili, funzionalità rapidamente ripristinabile;</li>
            <li><strong>SLV</strong> (stato limite di salvaguardia della vita): la struttura può danneggiarsi ma deve proteggere le persone;</li>
            <li><strong>SLC</strong> (stato limite di prevenzione del collasso): nessun collasso anche sotto eventi eccezionali.</li>
          </ul>
          <p>A ciascuno stato limite corrisponde una probabilità di superamento nel periodo di riferimento, funzione della <strong>vita nominale</strong> dell'opera e della sua categoria d'uso. Le verifiche riguardano resistenza, duttilità, gerarchia delle resistenze e dettagli costruttivi: l'area in cui la qualità esecutiva in cantiere fa la differenza più marcata tra progetto e opera reale.</p>

          {AD}

          <h2 id="categorie">Categorie d'uso e vita nominale: quanto deve durare una struttura</h2>
          <p>Le NTC assegnano a ogni opera una <strong>vita nominale</strong> e una <strong>categoria d'uso</strong>, che insieme calibrano il livello di prestazione richiesto. Lo schema semplificato:</p>
          <table>
            <thead>
              <tr><th>Categoria d'uso</th><th>Tipologia</th><th>Coefficiente d'uso</th></tr>
            </thead>
            <tbody>
              <tr><td>CU I</td><td>Opere provvisorie e strutture temporanee</td><td>1,0</td></tr>
              <tr><td>CU II</td><td>Opere ordinarie (abitazioni, uffici)</td><td>1,0</td></tr>
              <tr><td>CU III</td><td>Opere con affollamento significativo (scuole, stadi)</td><td>1,5</td></tr>
              <tr><td>CU IV</td><td>Opere strategiche (ospedali, caserme, ponti principali)</td><td>2,0</td></tr>
            </tbody>
          </table>
          <p>La vita nominale varia da 10 anni per le opere provvisorie a 50 per quelle ordinarie fino a 100 o più per grandi opere e infrastrutture: maggiore è la combinazione di vita e categoria, più severi sono gli spettri di progetto e le verifiche. È il meccanismo con cui la norma chiede di più a un ospedale rispetto a un capannone.</p>

          <h2 id="esistente">Il patrimonio esistente: miglioramento e adeguamento sismico</h2>
          <p>Gran parte del lavoro strutturale in Italia riguarda l'esistente: oltre la metà degli edifici è anteriore alle prime norme antisismiche moderne. Le NTC distinguono tra <strong>adeguamento</strong> (portare la struttura al livello richiesto per l'opera nuova) e <strong>miglioramento</strong> (incrementare la sicurezza senza raggiungere necessariamente quel livello), con obblighi diversi a seconda dell'entità dell'intervento e della destinazione d'uso.</p>
          <p>Sul piano fiscale, gli interventi di riduzione del rischio sismico interagiscono con le agevolazioni edilizie: il quadro aggiornato delle detrazioni disponibili, incluse le opere di messa in sicurezza, è nella <a href="bonus-ristrutturazione-2026-guida-completa.html">guida al bonus ristrutturazione 2026</a>. Per le strutture più recenti, materiali come il legno lamellare e l'XLAM offrono risposte efficaci in zona sismica grazie al rapporto tra resistenza e peso, come raccontiamo nell'approfondimento sull'<a href="edilizia-legno-xlam.html">edilizia in legno XLAM</a>.</p>
          <blockquote>«La norma sismica non chiede edifici indistruttibili: chiede edifici che proteggano la vita. La differenza tra le due cose è il cuore della cultura strutturale italiana.»</blockquote>

          <h2 id="faq">Domande frequenti sulle NTC e la classificazione sismica</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> DM 17 gennaio 2018 — Norme Tecniche per le Costruzioni; Circolare applicativa NTC; Ordinanza PCM 3274/2003 e aggiornamenti; Consiglio Superiore dei Lavori Pubblici. Contenuto a scopo informativo: per la progettazione fare riferimento ai testi ufficiali vigenti e a un professionista abilitato.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 9: SICUREZZA D.LGS 81/08 ============================
ARTICLES.append({
 "slug": "sicurezza-cantiere-dlgs-81-novita",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "Sicurezza in cantiere: novità D.Lgs 81 | Il Giornale Edile",
 "desc": "Sicurezza in cantiere: le novità del D.Lgs 81/08, dal patentino a crediti alle regole su ponteggi e coordinamento. Obblighi e sanzioni aggiornati.",
 "kw": "sicurezza cantiere, d.lgs 81/08, testo unico sicurezza, patentino crediti sicurezza, sicurezza lavori edili",
 "author": "Sara Colombo",
 "date_iso": "2026-07-16T08:00:00+02:00", "date_it": "16 luglio 2026", "tb_date": "Giovedì 16 luglio 2026", "mins": 8,
 "og_title": "Sicurezza in cantiere: le novità del Testo Unico D.Lgs 81/08",
 "og_desc": "Patentino a crediti per le imprese, coordinamento rafforzato e sanzioni più severe: cosa è cambiato davvero nella sicurezza dei cantieri.",
 "tw_title": "Sicurezza cantiere: le novità", "tw_desc": "Patentino a crediti, figure e sanzioni nel Testo Unico.",
 "ld_desc": "Sicurezza nei cantieri edili: novità del D.Lgs 81/08, patentino a crediti per imprese e lavoratori, figure CSP/CSE, PiMUS e sanzioni.",
 "bc_short": "Sicurezza in cantiere",
 "kicker": "Normative &amp; Cantieri · Sicurezza",
 "h1": "Sicurezza in cantiere: le novità del Testo Unico D.Lgs 81/08",
 "stand": "Dal patentino a crediti per imprese e lavoratori alle nuove regole su coordinamento e sospensione dei lavori: il cantiere edile italiano cambia pelle sulla sicurezza. La guida agli adempimenti che contano davvero.",
 "faq": [
  ("Cos'è il patentino a crediti per la sicurezza in cantiere?",
   "È un meccanismo introdotto nel 2024: imprese e lavoratori autonomi che operano nei cantieri temporanei o mobili devono possedere un <strong>punteggio minimo di crediti</strong>, ottenuti con formazione, esperienza e dotazioni di sicurezza. Senza i crediti non si può operare in cantiere."),
  ("Quali figure della sicurezza servono in un cantiere edile?",
   "Nei cantieri con più imprese esecutrici il committente nomina il <strong>coordinatore per la progettazione (CSP)</strong> e il <strong>coordinatore per l'esecuzione (CSE)</strong>; ogni impresa ha il proprio datore di lavoro, il RSPP e i preposti. Obbligatori POS, PSC e, dove previsto, DUVRI."),
  ("Chi deve redigere il PiMUS?",
   "Il <strong>PiMUS</strong> (Piano di Montaggio, Uso e Smontaggio dei ponteggi) è redatto dal datore di lavoro dell'impresa che monta il ponteggio, anche avvalendosi di un tecnico. Deve essere presente in cantiere insieme al libretto di autorizzazione ministeriale del ponteggio."),
  ("Quali sanzioni rischia un'impresa senza crediti di sicurezza?",
   "Operare in cantiere senza il punteggio minimo di crediti comporta <strong>sanzioni pecuniarie e l'impossibilità di lavorare nel cantiere</strong>; le violazioni gravi sulla sicurezza possono inoltre portare alla sospensione dell'attività e, nei casi più seri, a responsabilità penali."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Sicurezza cantiere"),("../categoria/normative-cantieri.html","D.Lgs 81/08"),("../categoria/normative-cantieri.html","Ponteggi"),("../categoria/normative-cantieri.html","Normativa lavoro")],
 "rel": [
  ("ponteggi-norme-sicurezza","t-normative","Normative &amp; Cantieri","Ponteggi: norme, autorizzazioni e sicurezza","PiMUS, ancoraggi e verifiche: le regole per montare e usare i ponteggi.","5 lug 2026",8),
  ("codice-appalti-dlgs-36-2023","t-normative","Normative &amp; Cantieri","Codice Appalti D.Lgs 36/2023: le novità","Subappalto, tracciabilità e responsabilità solidale nei lavori pubblici.","9 lug 2026",9),
  ("ntc-aggiornamenti-sismici","t-normative","Normative &amp; Cantieri","NTC: aggiornamenti e classificazione sismica","Verifiche strutturali e sicurezza dell'opera: la bussola delle NTC.","7 lug 2026",9),
  ("top-5-imprese-costruzione-italia","t-mercato","Mercato &amp; Immobiliare","Le 5 maggiori imprese di costruzione italiane","Fatturati e strategie dei general contractor, tra sicurezza e digitalizzazione.","17 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Operaio con dispositivi di protezione individuale in un cantiere edile">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Il <strong>patentino a crediti</strong> è operativo: imprese e lavoratori autonomi devono avere almeno 30 crediti per entrare in cantiere.</li>
              <li>Le figure cardine restano <strong>CSP e CSE</strong>, con POS, PSC e documentazione di cantiere sempre obbligatori nei cantieri con più imprese.</li>
              <li>Rafforzati <strong>controlli e sospensioni</strong> per violazioni gravi: il cantiere può essere fermato in giornata.</li>
              <li><strong>PiMUS e formazione specifica</strong> restano il cuore della prevenzione per ponteggi e lavori in quota.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#quadro">Il quadro: il Testo Unico e i cantieri edili</a></li>
              <li><a href="#patentino">Il patentino a crediti: come funziona</a></li>
              <li><a href="#figure">Le figure della sicurezza in cantiere</a></li>
              <li><a href="#controlli">Controlli, sospensioni e sanzioni</a></li>
              <li><a href="#quota">Lavori in quota e ponteggi</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="quadro">Il quadro: il Testo Unico e i cantieri edili</h2>
          <p>Il <strong>decreto legislativo 81/2008</strong>, il Testo Unico sulla salute e sicurezza sul lavoro, dedica il Titolo IV ai cantieri temporanei o mobili: il perimetro entro cui opera quasi tutta l'edilizia italiana. La filosofia è quella della valutazione dei rischi e della prevenzione organizzata: ogni cantiere deve avere un piano, delle figure responsabili e una catena di controlli che coinvolge committente, coordinatori e imprese. Negli ultimi anni il legislatore è intervenuto più volte per rafforzare il sistema, in risposta a una statistica infortunistica che nel settore delle costruzioni resta tra le più critiche d'Europa.</p>
          <p>Per le imprese la partita si gioca su tre tavoli: <strong>documentazione</strong> (POS, PSC, DUVRI, piani specifici), <strong>persone</strong> (formazione, addestramento, preposti) e <strong>mezzi</strong> (attrezzature conformi, DPI, ponteggi a regola d'arte). Su ciascuno sono arrivate novità rilevanti.</p>

          <h2 id="patentino">Il patentino a crediti: come funziona</h2>
          <p>La novità più incisiva è il sistema di <strong>abilitazione a crediti</strong>, operativo dall'ottobre 2024: imprese e lavoratori autonomi che intendono operare in un cantiere temporaneo o mobile devono disporre di un punteggio minimo di <strong>30 crediti</strong>, attestato dalla piattaforma nazionale. I crediti si ottengono attraverso una combinazione di elementi:</p>
          <table>
            <thead>
              <tr><th>Voce</th><th>Crediti indicativi</th><th>Note</th></tr>
            </thead>
            <tbody>
              <tr><td>Iscrizione CCIAA e regolarità contributiva</td><td>Fino a 10</td><td>Requisiti di base dell'impresa</td></tr>
              <tr><td>Formazione generale e specifica dei lavoratori</td><td>Fino a 15</td><td>Compresi corsi ponteggi e lavori in quota</td></tr>
              <tr><td>Esperienza pregressa nei cantieri</td><td>Fino a 10</td><td>Durata e continuità dell'attività</td></tr>
              <tr><td>Attrezzature e certificazioni di sicurezza</td><td>Variabile</td><td>Adozione di sistemi di gestione e dotazioni</td></tr>
            </tbody>
          </table>
          <p>I crediti vengono <strong>sottratti in caso di violazioni</strong> accertate: scendere sotto la soglia minima significa non poter operare fino al ripristino. Il meccanismo premia le imprese strutturate e rende tracciabile la storia di sicurezza di ciascun operatore, con effetti diretti anche sulla selezione nei subappalti.</p>

          <h2 id="figure">Le figure della sicurezza: chi fa cosa in cantiere</h2>
          <p>Nei cantieri in cui opera più di un'impresa, anche non contemporaneamente, il committente (o il responsabile dei lavori) deve nominare:</p>
          <ul>
            <li>il <strong>Coordinatore per la progettazione (CSP)</strong>, che redige il Piano di Sicurezza e Coordinamento (PSC) e il fascicolo dell'opera;</li>
            <li>il <strong>Coordinatore per l'esecuzione (CSE)</strong>, che verifica l'applicazione del PSC e l'aggiorna, con poteri di sospensione dei lavori in caso di pericolo grave e imminente.</li>
          </ul>
          <p>Ogni impresa esecutrice presenta il proprio <strong>POS</strong> (Piano Operativo di Sicurezza), coerente con il PSC, e organizza la propria catena prevenzionale: datore di lavoro, RSPP, medico competente quando dovuto, preposti e lavoratori formati. Il <strong>preposto</strong>, figura rafforzata dalle riforme recenti, ha obblighi specifici di vigilanza e intervento e una formazione dedicata obbligatoria.</p>

          {AD}

          <h2 id="controlli">Controlli, sospensioni e sanzioni: la stretta operativa</h2>
          <p>Il sistema sanzionatorio è stato progressivamente inasprito: per le violazioni più gravi — lavoratori non formati, assenza di protezioni contro le cadute, ponteggi non conformi — gli organi di vigilanza possono disporre la <strong>sospensione immediata dell'attività</strong>, con riammissione solo dopo la regolarizzazione e il pagamento della somma accessoria. Le sanzioni pecuniarie per il datore di lavoro sono state aggiornate al rialzo e nei casi di infortunio grave resta ferma la responsabilità penale.</p>
          <p>La tendenza dei controlli è verso la verifica documentale integrata: piattaforme nazionali incrociate, durc, iscrizioni e crediti del patentino. L'impresa che arriva in cantiere con la documentazione digitale in ordine riduce drasticamente il rischio di fermi e contestazioni.</p>

          <h2 id="quota">Lavori in quota e ponteggi: il fronte più critico</h2>
          <p>Le cadute dall'alto restano la prima causa di infortunio grave in edilizia. La norma impone protezioni collettive prioritarie — parapetti, reti, ponteggi conformi — e ricorre ai DPI anticaduta solo quando le prime non siano attuabili. Per i ponteggi valgono gli obblighi specifici del Titolo IV: <strong>PiMUS</strong>, libretto di autorizzazione ministeriale, montaggio da parte di personale formato secondo i contenuti dell'accordo Stato-Regioni e verifiche dopo eventi atmosferici eccezionali. L'approfondimento completo è nella guida su <a href="ponteggi-norme-sicurezza.html">ponteggi, norme e sicurezza nel montaggio</a>.</p>
          <p>Anche il committente privato ha responsabilità: la scelta dell'impresa non è neutra, e verificare crediti, POS e assicurazioni prima di affidare i lavori è oggi un dovere giuridico oltre che una cautela, specie nei cantieri condominiali dove la committenza è un soggetto non professionale. Sul fronte degli appalti pubblici, le regole di tracciabilità e responsabilità solidale si intrecciano con il <a href="codice-appalti-dlgs-36-2023.html">nuovo Codice degli Appalti</a>.</p>
          <blockquote>«La sicurezza in cantiere non si improvvisa il giorno dell'apertura: si costruisce con formazione, documenti e dotazioni, ed è diventata un requisito di accesso al mercato, non solo un obbligo di legge.»</blockquote>

          <h2 id="faq">Domande frequenti sulla sicurezza in cantiere</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> D.Lgs 81/2008 e s.m.i., Titolo IV; INL — circolari e indirizzi sul sistema a crediti; INAIL — statistiche infortunistiche e guide tecniche; accordi Stato-Regioni sulla formazione. Contenuto a scopo informativo: per gli adempimenti specifici consultare un professionista della sicurezza.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ ARTICOLO 10: PONTEGGI ============================
ARTICLES.append({
 "slug": "ponteggi-norme-sicurezza",
 "cat": "Normative &amp; Cantieri", "cat_slug": "normative-cantieri", "thumb": "t-normative",
 "title": "Ponteggi: norme e sicurezza | Il Giornale Edile",
 "desc": "Ponteggi: norme UNI, PiMUS, autorizzazioni e regole di sicurezza per montaggio e smontaggio. Guida completa per imprese, committenti e coordinatori.",
 "kw": "ponteggi norme, sicurezza ponteggi, pimus, montaggio ponteggi, ponteggio autorizzazione ministeriale",
 "author": "Marco Ferreri",
 "date_iso": "2026-07-05T08:00:00+02:00", "date_it": "5 luglio 2026", "tb_date": "Domenica 5 luglio 2026", "mins": 8,
 "og_title": "Ponteggi: norme, autorizzazioni e sicurezza nel montaggio",
 "og_desc": "Dal PiMUS al libretto ministeriale, dagli ancoraggi alle verifiche periodiche: le regole per un ponteggio a norma, senza improvvisazione.",
 "tw_title": "Ponteggi: norme e sicurezza", "tw_desc": "PiMUS, autorizzazioni e verifiche: la guida operativa.",
 "ld_desc": "Ponteggi: normativa D.Lgs 81/08 Titolo IV, PiMUS, libretto di autorizzazione ministeriale, ancoraggi, verifiche e sicurezza di montaggio e smontaggio.",
 "bc_short": "Ponteggi: norme e sicurezza",
 "kicker": "Normative &amp; Cantieri · Attrezzature",
 "h1": "Ponteggi: norme, autorizzazioni e sicurezza nel montaggio",
 "stand": "Sono l'attrezzatura più diffusa nei cantieri italiani e tra le prime cause di infortunio grave quando sono improvvisati: norme UNI, PiMUS, autorizzazioni e controlli per montare, usare e smontare i ponteggi a regola d'arte.",
 "faq": [
  ("Che cos'è il PiMUS e chi lo redige?",
   "Il PiMUS è il <strong>Piano di Montaggio, Uso e Smontaggio</strong> del ponteggio, obbligatorio per legge. Lo redige il datore di lavoro dell'impresa che monta il ponteggio, anche avvalendosi di un tecnico, e deve essere disponibile in cantiere."),
  ("Cos'è il libretto di autorizzazione ministeriale?",
   "È il documento che attesta l'<strong>autorizzazione del Ministero del Lavoro</strong> alla costruzione e all'impiego di un sistema di ponteggio (a telai prefabbricati o a tubi e giunti conformi). Senza libretto, il ponteggio non può essere usato."),
  ("Ogni quanto va verificato un ponteggio?",
   "Il ponteggio va verificato <strong>alla consegna dopo il montaggio, periodicamente durante l'uso e sempre dopo eventi eccezionali</strong> come forte vento, urti o modifiche strutturali. Le verifiche vanno registrate nei documenti di cantiere."),
  ("Serve un'autorizzazione per montare un ponteggio su suolo pubblico?",
   "Sì: l'occupazione di suolo pubblico richiede l'<strong>autorizzazione comunale</strong> (con pagamento del canone, quando dovuto) e la segnalazione con idonea cartellonistica; per ponteggi su strade trafficate servono anche piano della segnaletica e pareri specifici."),
 ],
 "tags": [("../categoria/normative-cantieri.html","Ponteggi"),("../categoria/normative-cantieri.html","Sicurezza cantiere"),("../categoria/normative-cantieri.html","Lavori in quota"),("../categoria/normative-cantieri.html","Normativa edilizia")],
 "rel": [
  ("sicurezza-cantiere-dlgs-81-novita","t-normative","Normative &amp; Cantieri","Sicurezza in cantiere: le novità del D.Lgs 81/08","Patentino a crediti, figure della sicurezza e sanzioni aggiornate.","16 lug 2026",8),
  ("ntc-aggiornamenti-sismici","t-normative","Normative &amp; Cantieri","NTC: aggiornamenti e classificazione sismica","Azioni sulle strutture e verifiche: i riferimenti tecnici delle NTC.","7 lug 2026",9),
  ("codice-appalti-dlgs-36-2023","t-normative","Normative &amp; Cantieri","Codice Appalti D.Lgs 36/2023: le novità","Qualificazione, subappalto e responsabilità nei lavori pubblici.","9 lug 2026",9),
  ("cappotto-termico-materiali-confronto","t-materiali","Materiali &amp; Tecnologie","Cappotto termico: EPS, lana di roccia o sughero?","Materiali a confronto per l'isolamento a cappotto eseguito da ponteggio.","13 lug 2026",7),
 ],
 "body": '''<figure class="thumb t-normative ar-16-9" role="img" aria-label="Ponteggio metallico a telai prefabbricati su facciata in ristrutturazione">
            <span class="thumb-label">Normative &amp; Cantieri</span>
          </figure>

          <!-- Box risposta rapida: ottimizzato per featured snippet e risposte AI (AEO) -->
          <aside class="key-takeaways">
            <h2>In breve</h2>
            <ul>
              <li>Il ponteggio può essere usato solo se dotato di <strong>libretto di autorizzazione ministeriale</strong> e montato secondo lo schema tipo o un progetto dedicato.</li>
              <li>Il <strong>PiMUS</strong> è obbligatorio: lo redige il datore di lavoro dell'impresa montatrice e deve essere in cantiere.</li>
              <li>Montaggio e smontaggio solo da <strong>personale formato</strong> secondo l'accordo Stato-Regioni, con protezioni anticaduta.</li>
              <li>Verifiche obbligatorie <strong>alla consegna, periodicamente e dopo eventi eccezionali</strong>; autorizzazione comunale per l'occupazione di suolo pubblico.</li>
            </ul>
          </aside>

          <nav class="toc" aria-label="Indice dell'articolo">
            <h2>Indice dei contenuti</h2>
            <ol>
              <li><a href="#quadro">Il quadro normativo: Titolo IV e norme UNI</a></li>
              <li><a href="#pimus">Il PiMUS: contenuto e responsabilità</a></li>
              <li><a href="#autorizzazioni">Libretto ministeriale e autorizzazioni</a></li>
              <li><a href="#montaggio">Le regole del montaggio sicuro</a></li>
              <li><a href="#verifiche">Verifiche, manutenzione e smontaggio</a></li>
              <li><a href="#faq">Domande frequenti</a></li>
            </ol>
          </nav>

          <h2 id="quadro">Il quadro normativo: Titolo IV e norme UNI</h2>
          <p>I ponteggi rientrano nelle attrezzature di lavoro disciplinate dal <strong>Titolo IV del D.Lgs 81/08</strong> e dal Titolo III per gli aspetti di conformità: il riferimento tecnico sono le norme <strong>UNI EN 12810 e UNI EN 12811</strong> per i sistemi di facciata, insieme alle disposizioni specifiche su ancoraggi, piattaforme e accessi. Il principio di fondo è che il ponteggio è un'opera provvisionale vera e propria: ha un progetto (o uno schema tipo), un responsabile, dei carichi ammissibili e una vita che va gestita dal montaggio allo smontaggio.</p>
          <p>Le statistiche INAIL confermano la criticità: i ponteggi sono costantemente tra le attrezzature associate al maggior numero di infortuni gravi, quasi sempre per errori di montaggio, ancoraggi mancanti o uso improprio delle piattaforme. La norma risponde con un sistema di obblighi documentali e formativi che non ammette improvvisazione.</p>

          <h2 id="pimus">Il PiMUS: contenuto e responsabilità</h2>
          <p>Il <strong>PiMUS — Piano di Montaggio, Uso e Smontaggio</strong> — è il documento cardine: obbligatorio per qualsiasi ponteggio di altezza superiore ai 2 metri, deve essere redatto dal datore di lavoro dell'impresa che esegue il montaggio, anche avvalendosi di un tecnico abilitato. Il piano contiene, come minimo:</p>
          <ul>
            <li>la descrizione del sistema impiegato e del <strong>libretto di autorizzazione ministeriale</strong> di riferimento;</li>
            <li>lo <strong>schema di montaggio</strong> con misure, altezze, sbalzi e ancoraggi;</li>
            <li>le <strong>modalità operative</strong> per montaggio, uso e smontaggio, incluse le protezioni anticaduta;</li>
            <li>le <strong>verifiche</strong> previste e i criteri di gestione delle modifiche;</li>
            <li>l'individuazione dei soggetti incaricati e delle loro competenze.</li>
          </ul>
          <p>Il PiMUS deve essere conservato in cantiere ed esibito agli organi di vigilanza: la sua assenza o la difformità del ponteggio reale dal piano sono tra le irregolarità più contestate e possono portare alla sospensione dei lavori, nel quadro sanzionatorio descritto nell'articolo sulle <a href="sicurezza-cantiere-dlgs-81-novita.html">novità del D.Lgs 81/08 in cantiere</a>.</p>

          <h2 id="autorizzazioni">Libretto ministeriale e autorizzazioni: la parte amministrativa</h2>
          <p>Ogni sistema di ponteggio — telai prefabbricati, tubi e giunti, montanti e traversi prefabbricati — deve essere coperto da <strong>autorizzazione ministeriale</strong>, attestata dal libretto che riporta schemi tipo, carichi ammissibili e istruzioni del costruttore. Gli elementi metallici devono essere conformi e riconducibili al sistema autorizzato: mescolare componenti di sistemi diversi è vietato.</p>
          <p>Sul fronte amministrativo, quando il ponteggio occupa suolo pubblico — marciapiedi, strade, piazze — serve l'<strong>autorizzazione comunale all'occupazione</strong>, con canone dove previsto, cartellonistica di cantiere e, nei casi di interferenza con la viabilità, piano della segnaletica approvato. Nei centri storici o su edifici vincolati possono aggiungersi prescrizioni della soprintendenza su fissaggi e impatto visivo.</p>

          {AD}

          <h2 id="montaggio">Le regole del montaggio sicuro</h2>
          <p>Il montaggio è la fase a più alto rischio: i ponteggiatori devono essere <strong>formati e addestrati</strong> secondo i contenuti dell'accordo Stato-Regioni, con verifica di idoneità alla mansione. Le regole operative essenziali:</p>
          <ol>
            <li><strong>Fondazioni</strong>: basi di appoggio idonee al terreno, con tavole di ripartizione e verifica dei carichi; mai appoggi diretti su terreno cedevole.</li>
            <li><strong>Ancoraggi</strong>: secondo schema tipo o progetto, in genere con maglia regolare (indicativamente ogni due impalcati in altezza e con interasse definito in orizzontale), mai rimossi per comodità di lavoro.</li>
            <li><strong>Piattaforme</strong>: impalcati completi, senza vuoti eccessivi, con tavole fermate contro il sollevamento.</li>
            <li><strong>Protezioni di bordo</strong>: parapetto con corrente superiore, intermedio e fermapiede su ogni fronte esposto.</li>
            <li><strong>Accessi</strong>: scale interne o torri di accesso dedicate; vietato l'accesso rampicante sui telai.</li>
            <li><strong>Anticaduta durante il montaggio</strong>: sistemi di ancoraggio progressivo o linee vita temporanee, perché il parapetto esiste solo a lavoro finito.</li>
          </ol>
          <p>Anche le interferenze contano: linee elettriche aeree, viabilità, altre imprese in quota. Il coordinatore per l'esecuzione verifica la coerenza del PiMUS con il PSC di cantiere.</p>

          <h2 id="verifiche">Verifiche, manutenzione e smontaggio</h2>
          <p>Il ponteggio va controllato lungo tutta la sua vita in cantiere. Lo schema delle verifiche obbligatorie:</p>
          <table>
            <thead>
              <tr><th>Momento</th><th>Verifica</th><th>Responsabile</th></tr>
            </thead>
            <tbody>
              <tr><td>Fine montaggio</td><td>Verifica di conformità allo schema e consegna</td><td>Impresa montatrice / datore di lavoro</td></tr>
              <tr><td>Uso ordinario</td><td>Controlli periodici su ancoraggi, impalcati, parapetti</td><td>Datore di lavoro / preposto</td></tr>
              <tr><td>Eventi eccezionali</td><td>Verifica straordinaria dopo vento forte, urti, modifiche</td><td>Datore di lavoro, anche con tecnico</td></tr>
              <tr><td>Smontaggio</td><td>Sequenza inversa al montaggio, aree interdette al pubblico</td><td>Impresa montatrice</td></tr>
            </tbody>
          </table>
          <p>La manutenzione riguarda anche il deposito: elementi corrosi, deformati o saldati abusivamente vanno scartati. In fase di smontaggio, il rischio maggiore è la precipitazione di materiali: le zone sottostanti vanno interdette e segnalate, con regia chiara delle fasi di calata. Per i lavori di facciata eseguiti da ponteggio — ad esempio il cappotto termico, con i materiali confrontati nel nostro <a href="cappotto-termico-materiali-confronto.html">articolo sui sistemi a cappotto</a> — la scelta tra ponteggio tradizionale, piattaforme o funi incide su costi, tempi e permessi e va valutata in fase di progetto.</p>
          <blockquote>«Un ponteggio non è mai "solo un ponteggio": è una struttura provvisionale che porta persone e carichi. Chi lo tratta da accessorio, prima o poi lo racconta in un verbale di infortunio.»</blockquote>

          <h2 id="faq">Domande frequenti su ponteggi e sicurezza</h2>
          <div class="faq">
          {FAQ}
          </div>

          <p class="sources"><strong>Fonti:</strong> D.Lgs 81/2008, Titoli III e IV; norme UNI EN 12810 e UNI EN 12811; Ministero del Lavoro — autorizzazioni sistemi di ponteggio; INAIL — guide tecniche e banche dati infortuni; accordi Stato-Regioni sulla formazione. Contenuto a scopo informativo: per la progettazione e il montaggio rivolgersi a tecnici e imprese qualificati.</p>

          <div class="tags" aria-label="Argomenti dell'articolo">
          {TAGS}
          </div>'''
})

# ============================ GENERAZIONE E VERIFICA ============================
def verify(path, a):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    # testo articleBody senza box pubblicitari e senza tag
    m = re.search(r'itemprop="articleBody">(.*?)<!-- Sidebar articolo -->', html, re.S)
    body = m.group(1) if m else html
    body = re.sub(r'<div class="ad-slot ad-rect ad-inarticle".*?</div>', "", body, flags=re.S)
    text = strip_tags(body)
    text = re.sub(r"\s+", " ", text).strip()
    n_chars = len(text)
    n_ld = html.count('application/ld+json')
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', html).group(1)
    return n_chars, n_ld, title, desc


if __name__ == "__main__":
    print(f"{'FILE':42} {'CHARS':>6} {'LD':>3}  TITLE (len) / DESC (len)")
    ok = True
    for a in ARTICLES:
        path = os.path.join(BASE, a["slug"] + ".html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(a))
        n_chars, n_ld, title, desc = verify(path, a)
        flag = "OK " if n_chars >= 4000 else "SHORT"
        if n_chars < 4000 or n_ld != 3:
            ok = False
        print(f"{a['slug']+'.html':42} {n_chars:>6} {n_ld:>3}  [{len(title)}c] {title[:55]}  [{len(desc)}c] desc  {flag}")
    print("\nTUTTI OK" if ok else "\nALCUNI FILE NON CONFORMI")
