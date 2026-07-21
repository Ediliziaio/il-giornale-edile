#!/usr/bin/env python3
"""Genera le pagine istituzionali: chi-siamo, contatti, pubblicita, privacy, cookie-policy, note-legali, cerca."""
import html
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://www.ilgiornaleedile.it"

PAGES = {
    "chi-siamo": ("Chi siamo", "La redazione del Giornale Edile: chi siamo, cosa facciamo e perché parliamo di costruzioni.", [
        ("La testata", "Il Giornale Edile è una testata giornalistica online interamente dedicata al mondo delle costruzioni e dell'edilizia italiana. Nasce con un obiettivo preciso: rendere accessibili a imprese, professionisti tecnici, artigiani e committenti privati le informazioni che contano davvero — bonus fiscali, norme tecniche, materiali, tecnologie di cantiere e dinamiche di mercato — con un linguaggio chiaro e un rigore da redazione specializzata."),
        ("Cosa facciamo", "Ogni settimana pubblichiamo guide pratiche, analisi di mercato, aggiornamenti normativi e confronti tra prodotti e fornitori. I nostri articoli superano i 4.000 caratteri perché crediamo nella profondità: ogni guida include tabelle comparative, risposte rapide alle domande più frequenti e riferimenti alle fonti ufficiali, dall'Agenzia delle Entrate alle norme UNI."),
        ("La redazione", "La redazione è composta da giornalisti e tecnici con esperienza pluriennale nel settore delle costruzioni: Marco Ferreri (bonus e fiscalità), Giulia Santi (normativa e certificazioni), Luca Brambilla (materiali e tecnologie), Sara Colombo (mercato immobiliare) e Paolo Riva (cantieri e sicurezza)."),
        ("Le nostre scelte editoriali", "Le classifiche e le selezioni di prodotti pubblicate nelle nostre guide 'Top 5' sono frutto di valutazione redazionale indipendente. Eventuali contenuti sponsorizzati sono sempre contrassegnati in modo trasparente."),
    ]),
    "contatti": ("Contatti", "Come contattare la redazione del Giornale Edile: segnalazioni, comunicati e richieste commerciali.", [
        ("Redazione", "Per segnalazioni, correzioni e comunicati stampa del settore edile scrivi a redazione@ilgiornaleedile.it. Leggiamo tutto: i comunicati rilevanti per i nostri lettori vengono valutati per la pubblicazione."),
        ("Ufficio commerciale", "Per informazioni su spazi pubblicitari, contenuti sponsorizzati e partnership scrivi a pubblicita@ilgiornaleedile.it o consulta la pagina Pubblicità."),
        ("Dove siamo", "Il Giornale Edile — Redazione online, Italia. Testata registrata presso il Tribunale competente (dati di registrazione disponibili nelle Note legali)."),
    ]),
    "pubblicita": ("Pubblicità", "Spazi pubblicitari sul Giornale Edile: formati IAB, posizioni e contatti per le campagne.", [
        ("Perché fare pubblicità qui", "Il Giornale Edile raggiunge un pubblico verticalissimo: imprese di costruzione, progettisti, geometri, architetti, installatori e privati che stanno ristrutturando. Un contesto editoriale premium in cui il tuo messaggio arriva a chi decide gli acquisti del cantiere."),
        ("Formati disponibili", "Leaderboard 970×250 e 728×90 (testata e piede di ogni pagina), Half Page 300×600 (sidebar), Medium Rectangle 300×250 (sidebar e in-article), Mobile Banner 320×100. Tutti gli spazi sono già predisposti nelle pagine del sito e contrassegnati come 'Pubblicità' nel rispetto della trasparenza verso i lettori."),
        ("Native e branded content", "Offriamo anche formati di contenuto sponsorizzato redazionale, sempre etichettati come tali, e la presenza nelle nostre guide comparative dove pertinente."),
        ("Contatti commerciali", "Per il media kit aggiornato e un preventivo scrivi a pubblicita@ilgiornaleedile.it."),
    ]),
    "privacy": ("Privacy Policy", "Informativa sulla privacy del Giornale Edile ai sensi del GDPR (Reg. UE 2016/679).", [
        ("Titolare del trattamento", "Il titolare del trattamento dei dati è Il Giornale Edile (di seguito 'il Titolare'), contattabile all'indirizzo privacy@ilgiornaleedile.it. La presente informativa è resa ai sensi dell'art. 13 del Regolamento UE 2016/679 (GDPR)."),
        ("Dati raccolti", "Raccogliamo: dati di navigazione anonimi e aggregati a fini statistici; l'indirizzo email fornito volontariamente per l'iscrizione alla newsletter; i dati inviati volontariamente tramite email o moduli di contatto."),
        ("Finalità e base giuridica", "L'invio della newsletter avviene sulla base del consenso dell'interessato, revocabile in qualsiasi momento tramite il link di disiscrizione presente in ogni email. I dati di contatto sono trattati per rispondere alle richieste ricevute."),
        ("Diritti dell'interessato", "In qualsiasi momento puoi esercitare i diritti di accesso, rettifica, cancellazione, limitazione e opposizione scrivendo a privacy@ilgiornaleedile.it, e proporre reclamo al Garante per la protezione dei dati personali."),
    ]),
    "cookie-policy": ("Cookie Policy", "Informativa sui cookie utilizzati dal Giornale Edile.", [
        ("Cosa sono i cookie", "I cookie sono piccoli file di testo che i siti visitati inviano al dispositivo dell'utente, dove vengono memorizzati per essere ritrasmessi agli stessi siti alla visita successiva."),
        ("Cookie utilizzati da questo sito", "Il Giornale Edile nella sua configurazione base utilizza esclusivamente cookie tecnici, necessari al funzionamento delle pagine, che non richiedono consenso. Con l'attivazione degli spazi pubblicitari potranno essere installati cookie di terze parti (es. ad server): in tal caso verrà mostrato un banner di consenso conforme alle linee guida del Garante."),
        ("Come gestire i cookie", "Puoi gestire o eliminare i cookie dalle impostazioni del tuo browser. La disattivazione dei cookie tecnici può compromettere alcune funzionalità del sito."),
    ]),
    "note-legali": ("Note legali", "Note legali, direttore responsabile e informazioni sulla testata Il Giornale Edile.", [
        ("Testata", "Il Giornale Edile — testata giornalistica online di informazione sul settore delle costruzioni. Direttore responsabile: da definirsi in fase di registrazione presso il Tribunale competente."),
        ("Proprietà intellettuale", "Tutti i contenuti pubblicati (testi, grafiche, marchi) sono di proprietà della testata o dei rispettivi titolari e sono protetti dalla normativa sul diritto d'autore. È consentita la citazione di brevi estratti con link alla fonte; ogni altro uso richiede autorizzazione scritta."),
        ("Esclusione di responsabilità", "I contenuti hanno scopo informativo e non costituiscono consulenza fiscale, legale o tecnica. Per l'applicazione ai casi concreti è sempre necessario rivolgersi a un professionista abilitato e verificare i testi ufficiali delle norme citate."),
    ]),
    "cerca": ("Cerca nel sito", "Cerca tra gli articoli del Giornale Edile.", [
        ("Come cercare", "Usa il campo di ricerca qui sotto per trovare articoli, guide e approfondimenti. La ricerca viene eseguita su titoli e contenuti degli articoli pubblicati."),
        ("Suggerimento", "Per risultati migliori usa parole chiave specifiche del settore: 'bonus ristrutturazione', 'cappotto termico', 'BIM', 'APE', 'Conto Termico'."),
    ]),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Il Giornale Edile</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{base}/{slug}.html">
  <meta name="robots" content="index, follow">
  <link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Source+Sans+3:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <a class="skip-link" href="#contenuto">Salta al contenuto</a>
  <div class="topbar"><div class="container">
    <span class="tb-date" data-tb-date>Martedì 21 luglio 2026</span>
    <nav class="tb-links" aria-label="Link utili">
      <a href="chi-siamo.html">Chi siamo</a><a href="contatti.html">Contatti</a>
      <a href="pubblicita.html">Pubblicità</a><a href="feed.xml">RSS</a>
    </nav>
  </div></div>
  <header class="masthead"><div class="container">
    <a class="logo" href="index.html" aria-label="Il Giornale Edile - Home">
      <img src="assets/logo.png" alt="Il Giornale Edile" width="460" height="44"></a>
    <div class="mh-right">
      <p class="mh-tagline">La testata di riferimento per imprese, professionisti e committenti dell'edilizia italiana.</p>
      <a class="btn" href="index.html#newsletter">Iscriviti gratis</a>
    </div>
  </div></header>
  <nav class="mainnav" aria-label="Navigazione principale"><div class="container"><ul>
    <li><a href="index.html">Home</a></li>
    <li><a href="categoria/bonus-fiscali.html">Bonus &amp; Fisco</a></li>
    <li><a href="categoria/energia-rinnovabili.html">Energia</a></li>
    <li><a href="categoria/normative-cantieri.html">Normative</a></li>
    <li><a href="categoria/materiali-tecnologie.html">Materiali &amp; Tech</a></li>
    <li><a href="categoria/mercato-immobiliare.html">Mercato</a></li>
    <li><a href="guide.html">Guide &amp; Top 5</a></li>
  </ul></div></nav>
  <main id="contenuto" class="container">
    <nav class="breadcrumbs" aria-label="Percorso di navigazione" style="margin-top:18px">
      <a href="index.html">Home</a><span class="sep">›</span><span>{title}</span>
    </nav>
    <article class="article-body" style="max-width:820px;padding-bottom:40px">
      <h1 style="font-size:clamp(30px,4vw,42px)">{title}</h1>
{body}
    </article>
  </main>
  <footer class="site-footer"><div class="container">
    <div class="footer-bottom" style="border-top:0">
      <span>© <span data-year>2026</span> Il Giornale Edile — Tutti i diritti riservati</span>
      <span><a href="privacy.html">Privacy</a> · <a href="cookie-policy.html">Cookie</a> · <a href="note-legali.html">Note legali</a></span>
    </div>
  </div></footer>
  <script src="js/main.js" defer></script>
</body>
</html>"""

SEARCH_EXTRA = """      <form action="cerca.html" method="get" role="search" style="margin:18px 0 26px;display:flex;gap:10px;max-width:520px">
        <label class="sr-only" for="q">Cerca</label>
        <input type="search" id="q" name="q" placeholder="Cerca articoli…" style="flex:1;padding:10px 12px;border:1px solid var(--line);border-radius:4px;font-size:15px">
        <button class="btn" type="submit">Cerca</button>
      </form>
"""

for slug, (title, desc, sections) in PAGES.items():
    body = f'      <p class="standfirst" style="font-size:19px;color:var(--ink-soft)">{html.escape(desc)}</p>\n'
    if slug == "cerca":
        body += SEARCH_EXTRA
    for h2, p in sections:
        body += f"      <h2>{html.escape(h2)}</h2>\n      <p>{html.escape(p)}</p>\n"
    page = TEMPLATE.format(title=html.escape(title), desc=html.escape(desc), base=BASE, slug=slug, body=body)
    (ROOT / f"{slug}.html").write_text(page, encoding="utf-8")
    print(f"{slug}.html -> OK")
