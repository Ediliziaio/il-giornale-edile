#!/usr/bin/env python3
"""Genera pagine categoria, guide.html, sitemap.xml, robots.txt, feed.xml
leggendo i metadati dei 30 articoli in articoli/."""
import re, html, os
from datetime import date as _date
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://www.ilgiornaleedile.it"
ART = ROOT / "articoli"

CATS = {
    "Bonus & Fisco": ("bonus-fiscali", "t-bonus", "Bonus fiscali, detrazioni e agevolazioni per la casa: guide aggiornate su ristrutturazione, Ecobonus, Superbonus e Conto Termico."),
    "Energia & Rinnovabili": ("energia-rinnovabili", "t-energia", "Fotovoltaico, pompe di calore, comunità energetiche ed efficienza: le guide per tagliare le bollette e riqualificare gli edifici."),
    "Normative & Cantieri": ("normative-cantieri", "t-normative", "Norme tecniche, codice degli appalti, sicurezza e pratiche edilizie: tutto quello che serve sapere per lavorare in regola."),
    "Materiali & Tecnologie": ("materiali-tecnologie", "t-materiali", "Materiali innovativi, BIM, serramenti e tecnologie di cantiere: le soluzioni che stanno cambiando il modo di costruire."),
    "Mercato & Immobiliare": ("mercato-immobiliare", "t-mercato", "Prezzi, trend e investimenti: l'analisi del mercato immobiliare italiano e dei costi di costruzione e ristrutturazione."),
    "Serramenti & Infissi": ("serramenti-infissi", "t-materiali", "Infissi e serramenti: guide e confronti su PVC, alluminio e legno, migliori produttori, trasmittanza, prezzi e detrazioni fiscali."),
}

def unesc(s):
    return html.unescape(s).strip()

def parse_article(path):
    t = path.read_text(encoding="utf-8")
    def m(rx, default=""):
        r = re.search(rx, t, re.S)
        return unesc(r.group(1)) if r else default
    title_h1 = m(r'<h1 itemprop="headline">(.*?)</h1>')
    title_tag = m(r'<title>(.*?)</title>').replace(" | Il Giornale Edile", "")
    desc = m(r'<meta name="description" content="(.*?)"')
    section = unesc(re.search(r'article:section" content="(.*?)"', t).group(1))
    date = re.search(r'article:published_time" content="(\d{4}-\d{2}-\d{2})', t).group(1)
    mod = re.search(r'article:modified_time" content="(\d{4}-\d{2}-\d{2})', t)
    modified = mod.group(1) if mod else date
    thumb = re.search(r'<figure class="thumb (t-\w+)', t)
    thumb = thumb.group(1) if thumb else CATS[section][1]
    body = re.search(r'itemprop="articleBody"(.*?)</div>\s*<!-- Sidebar', t, re.S)
    txt = re.sub(r"<[^>]+>", " ", body.group(1) if body else "")
    chars = len(re.sub(r"\s+", " ", txt))
    return {"slug": path.stem, "title": title_h1 or title_tag, "desc": desc,
            "section": section, "date": date, "modified": modified, "thumb": thumb, "chars": chars}

arts = sorted((parse_article(p) for p in ART.glob("*.html")), key=lambda a: a["date"], reverse=True)

print(f"{'ARTICOLO':52} {'CHARS':>6}")
for a in arts:
    flag = "OK " if a["chars"] >= 4000 else "!! "
    print(f"{flag}{a['slug']:50} {a['chars']:>6}")

# ---------- blocchi comuni ----------
def head(title, desc, canonical, extra_ld=""):
    return f"""<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Il Giornale Edile">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://www.ilgiornaleedile.it/assets/cover-home.webp">
  <meta property="og:locale" content="it_IT">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  {extra_ld}
</head>"""

def header(current=""):
    def navlink(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    return f"""<body>
  <a class="skip-link" href="#contenuto">Salta al contenuto</a>
  <div class="topbar"><div class="container">
    <span class="tb-date" data-tb-date>Martedì 21 luglio 2026</span>
    <nav class="tb-links" aria-label="Link utili">
      <a href="../chi-siamo.html">Chi siamo</a><a href="../contatti.html">Contatti</a>
      <a href="../pubblicita.html">Pubblicità</a><a href="../feed.xml">RSS</a>
    </nav>
  </div></div>
  <header class="masthead"><div class="container">
    <a class="logo" href="../index.html" aria-label="Il Giornale Edile - Home">
      <img src="../assets/logo.png" alt="Il Giornale Edile" width="460" height="44"></a>
    <div class="mh-right">
      <p class="mh-tagline">La testata di riferimento per imprese, professionisti e committenti dell'edilizia italiana.</p>
      <a class="btn" href="../index.html#newsletter">Iscriviti gratis</a>
    </div>
  </div></header>
  <nav class="mainnav" aria-label="Navigazione principale"><div class="container"><ul>
    {navlink("../index.html","Home","home")}
    {navlink("../categoria/bonus-fiscali.html","Bonus &amp; Fisco","bonus-fiscali")}
    {navlink("../categoria/energia-rinnovabili.html","Energia","energia-rinnovabili")}
    {navlink("../categoria/normative-cantieri.html","Normative","normative-cantieri")}
    {navlink("../categoria/materiali-tecnologie.html","Materiali &amp; Tech","materiali-tecnologie")}
    {navlink("../categoria/serramenti-infissi.html","Infissi","serramenti-infissi")}
    {navlink("../categoria/mercato-immobiliare.html","Mercato","mercato-immobiliare")}
    {navlink("../guide.html","Guide &amp; Top 5","guide")}
  </ul></div></nav>"""

FOOTER = """  <footer class="site-footer"><div class="container">
    <div class="footer-grid">
      <div>
        <a class="f-logo" href="../index.html"><img src="../assets/logo.png" alt="Il Giornale Edile" width="240" height="23" loading="lazy"></a>
        <p class="f-desc">Il Giornale Edile è la testata online dedicata al mondo delle costruzioni: bonus fiscali, norme tecniche, materiali, tecnologie di cantiere e mercato immobiliare.</p>
      </div>
      <nav aria-label="Sezioni del sito"><h4>Sezioni</h4><ul>
        <li><a href="../categoria/bonus-fiscali.html">Bonus &amp; Fisco</a></li>
        <li><a href="../categoria/energia-rinnovabili.html">Energia &amp; Rinnovabili</a></li>
        <li><a href="../categoria/normative-cantieri.html">Normative &amp; Cantieri</a></li>
        <li><a href="../categoria/materiali-tecnologie.html">Materiali &amp; Tecnologie</a></li>
        <li><a href="../categoria/mercato-immobiliare.html">Mercato &amp; Immobiliare</a></li>
        <li><a href="../categoria/serramenti-infissi.html">Serramenti &amp; Infissi</a></li>
      </ul></nav>
      <nav aria-label="Testata"><h4>Testata</h4><ul>
        <li><a href="../chi-siamo.html">Chi siamo</a></li>
        <li><a href="../contatti.html">Contatti</a></li>
        <li><a href="../pubblicita.html">Pubblicità</a></li>
        <li><a href="../feed.xml">Feed RSS</a></li>
        <li><a href="../sitemap.html">Mappa del sito</a></li>
      </ul></nav>
      <div><h4>Resta aggiornato</h4>
        <p class="f-desc">Bonus, scadenze e norme spiegate in 5 minuti, ogni settimana.</p>
        <a class="btn" href="../index.html#newsletter">Iscriviti gratis</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Il Giornale Edile — Tutti i diritti riservati</span>
      <span><a href="../privacy.html">Privacy</a> · <a href="../cookie-policy.html">Cookie</a> · <a href="../note-legali.html">Note legali</a></span>
    </div>
  </div></footer>
  <script src="../js/main.js" defer></script>
</body>
</html>"""

def card(a, subdir=""):
    excerpt = a["desc"][:110].rsplit(" ", 1)[0] + "…"
    d = a["date"][8:] + "/" + a["date"][5:7] + "/" + a["date"][:4]
    return f"""          <article class="card">
            <a href="{subdir}articoli/{a['slug']}.html"><div class="thumb {a['thumb']} ar-3-2"><span class="thumb-label">{html.escape(a['section'])}</span></div></a>
            <div class="card-body">
              <span class="cat-mini">{html.escape(a['section'])}</span>
              <h3><a href="{subdir}articoli/{a['slug']}.html">{html.escape(a['title'])}</a></h3>
              <p class="card-excerpt">{html.escape(excerpt)}</p>
              <div class="card-meta"><span>{d}</span></div>
            </div>
          </article>"""

AD_LEADER = """    <div class="ad-slot ad-leaderboard" data-ad-slot="leaderboard-top" role="complementary" aria-label="Spazio pubblicitario">
      <span class="ad-tag">Pubblicità</span><span class="ad-size">Leaderboard 970×250 / 728×90</span>
    </div>"""

# ---------- pagine categoria ----------
os.makedirs(ROOT / "categoria", exist_ok=True)
for name, (slug, tclass, catdesc) in CATS.items():
    items = [a for a in arts if a["section"] == name]
    ld = f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"CollectionPage",
   "name":"{name} — Il Giornale Edile","url":"{BASE}/categoria/{slug}.html",
   "description":"{catdesc}","inLanguage":"it-IT",
   "isPartOf":{{"@type":"WebSite","name":"Il Giornale Edile","url":"{BASE}/"}}}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
   {{"@type":"ListItem","position":1,"name":"Home","item":"{BASE}/"}},
   {{"@type":"ListItem","position":2,"name":"{name}"}}]}}
  </script>"""
    cards = "\n".join(card(a, "../") for a in items)
    page = f"""{head(f"{name} — News e Guide | Il Giornale Edile", catdesc, f"{BASE}/categoria/{slug}.html", ld)}
{header(slug)}
  <div class="container">{AD_LEADER}</div>
  <main id="contenuto" class="container">
    <nav class="breadcrumbs" aria-label="Percorso di navigazione" style="margin-top:18px">
      <a href="../index.html">Home</a><span class="sep">›</span><span>{html.escape(name)}</span>
    </nav>
    <header class="article-head" style="max-width:none;margin-top:6px">
      <h1>{html.escape(name)}</h1>
      <p class="standfirst">{catdesc}</p>
    </header>
    <section class="section" aria-label="Articoli della categoria">
      <div class="card-grid">
{cards}
      </div>
    </section>
  </main>
  <div class="ad-slot ad-footer" data-ad-slot="footer-leaderboard" role="complementary" aria-label="Spazio pubblicitario">
    <span class="ad-tag">Pubblicità</span><span class="ad-size">Leaderboard 728×90</span>
  </div>
{FOOTER}"""
    (ROOT / "categoria" / f"{slug}.html").write_text(page, encoding="utf-8")
    print(f"categoria/{slug}.html -> {len(items)} articoli")

# ---------- guide.html ----------
top5 = [a for a in arts if a["slug"].startswith("top-5-")]
guides = [a for a in arts if not a["slug"].startswith("top-5-") and a["slug"] in {
    "bonus-ristrutturazione-2026-guida-completa","ecobonus-65-guida","conto-termico-3-guida",
    "fotovoltaico-costi-permessi-2026","cappotto-termico-materiali-confronto",
    "mutui-green-casa-efficiente","costo-ristrutturazione-al-mq-2026","comunita-energetiche-cer-guida",
    "costruire-casa-prefabbricata-costi","superbonus-2026-cosa-resta",
    "accumulo-fotovoltaico-batterie-guida","posa-in-opera-infissi-guida","bonus-mobili-2026-guida",
    "vetri-basso-emissivi-selettivi-guida","isolamento-interno-pareti-guida",
    "prezzario-regionale-lavori-edili-guida","caldaia-condensazione-o-pompa-di-calore",
    "sostituzione-infissi-condominio-iter","normativa-antincendio-edilizia-2026",
    "pannelli-fotovoltaici-tecnologie-topcon-hjt","edilizia-scolastica-pnrr-cantieri",
    "cer-condominio-caso-studio","ristrutturazione-chiavi-in-mano","detrazioni-ristrutturazione-50-36"}]
ld_guide = f"""<script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"CollectionPage",
   "name":"Guide e Top 5 — Il Giornale Edile","url":"{BASE}/guide.html","inLanguage":"it-IT"}}
  </script>"""
page = f"""{head("Guide e Top 5 per l'Edilizia | Il Giornale Edile", "Le guide pratiche e le classifiche Top 5 del Giornale Edile: fornitori, materiali, software, bonus e costi spiegati in modo semplice.", f"{BASE}/guide.html", ld_guide)}
{header("guide")}
  <div class="container">{AD_LEADER}</div>
  <main id="contenuto" class="container">
    <nav class="breadcrumbs" aria-label="Percorso di navigazione" style="margin-top:18px">
      <a href="index.html">Home</a><span class="sep">›</span><span>Guide &amp; Top 5</span>
    </nav>
    <header class="article-head" style="max-width:none;margin-top:6px">
      <h1>Guide &amp; Top 5</h1>
      <p class="standfirst">Le guide pratiche e le classifiche redazionali per scegliere fornitori, materiali, software e bonus: confronti, prezzi e consigli operativi.</p>
    </header>
    <section class="section" aria-labelledby="top5">
      <div class="section-head"><h2 id="top5">Le <span>Top 5</span></h2></div>
      <div class="card-grid">
{chr(10).join(card(a) for a in top5)}
      </div>
    </section>
    <section class="section" aria-labelledby="guidepr">
      <div class="section-head"><h2 id="guidepr">Le <span>guide</span></h2></div>
      <div class="card-grid">
{chr(10).join(card(a) for a in guides)}
      </div>
    </section>
  </main>
  <div class="ad-slot ad-footer" data-ad-slot="footer-leaderboard" role="complementary" aria-label="Spazio pubblicitario">
    <span class="ad-tag">Pubblicità</span><span class="ad-size">Leaderboard 728×90</span>
  </div>
{FOOTER.replace("../", "")}"""
# fix root-level paths for guide.html (it lives in root, not in a subdir)
page = page.replace('href="../assets/', 'href="assets/').replace('src="../assets/', 'src="assets/')
page = page.replace('href="../css/', 'href="css/').replace('src="../js/', 'src="js/')
page = page.replace('href="../index.html', 'href="index.html').replace('href="../categoria/', 'href="categoria/')
page = page.replace('href="../chi-siamo.html', 'href="chi-siamo.html').replace('href="../contatti.html', 'href="contatti.html')
page = page.replace('href="../pubblicita.html', 'href="pubblicita.html').replace('href="../feed.xml', 'href="feed.xml')
page = page.replace('href="../privacy.html', 'href="privacy.html').replace('href="../cookie-policy.html', 'href="cookie-policy.html')
page = page.replace('href="../note-legali.html', 'href="note-legali.html').replace('href="../guide.html', 'href="guide.html')
(ROOT / "guide.html").write_text(page, encoding="utf-8")
print(f"guide.html -> {len(top5)} top5 + {len(guides)} guide")

# ---------- sitemap.xml ----------
STATIC_DATE = "2026-07-21"   # pagine istituzionali invariate
INDEX_DATE = "2026-07-31"    # home, categorie, guide, mappa: aggiornate con il ciclo 2
urls = [f"  <url><loc>{BASE}/</loc><lastmod>{INDEX_DATE}</lastmod><changefreq>daily</changefreq><priority>1.0</priority></url>",
        f"  <url><loc>{BASE}/guide.html</loc><lastmod>{INDEX_DATE}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>",
        f"  <url><loc>{BASE}/cerca.html</loc><lastmod>{STATIC_DATE}</lastmod><changefreq>monthly</changefreq><priority>0.3</priority></url>"]
for name, (slug, _, _) in CATS.items():
    urls.append(f"  <url><loc>{BASE}/categoria/{slug}.html</loc><lastmod>{INDEX_DATE}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>")
for a in arts:
    urls.append(f"  <url><loc>{BASE}/articoli/{a['slug']}.html</loc><lastmod>{a['modified']}</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
urls.append(f"  <url><loc>{BASE}/sitemap.html</loc><lastmod>{INDEX_DATE}</lastmod><changefreq>monthly</changefreq><priority>0.3</priority></url>")
for p in ["chi-siamo", "pubblicita", "contatti", "privacy", "cookie-policy", "note-legali"]:
    urls.append(f"  <url><loc>{BASE}/{p}.html</loc><lastmod>{STATIC_DATE}</lastmod><changefreq>yearly</changefreq><priority>0.3</priority></url>")
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
print(f"sitemap.xml -> {len(urls)} URL")

# ---------- sitemap-news.xml (Google News: articoli pubblicati dal 2026-07-19) ----------
news_items = []
for a in arts:
    if a['date'] >= "2026-07-19":
        news_items.append(f"""  <url>
    <loc>{BASE}/articoli/{a['slug']}.html</loc>
    <news:news>
      <news:publication>
        <news:name>Il Giornale Edile</news:name>
        <news:language>it</news:language>
      </news:publication>
      <news:publication_date>{a['date']}T08:00:00+02:00</news:publication_date>
      <news:title>{html.escape(a['title'])}</news:title>
    </news:news>
  </url>""")
newsmap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">\n'
           + "\n".join(news_items) + "\n</urlset>\n")
(ROOT / "sitemap-news.xml").write_text(newsmap, encoding="utf-8")
print(f"sitemap-news.xml -> {len(news_items)} news")

# ---------- robots.txt ----------
(ROOT / "robots.txt").write_text(f"""# Il Giornale Edile — robots.txt
# Politica AI-friendly: questa testata giornalistica online accoglie esplicitamente
# i crawler dei motori di ricerca e dei sistemi di intelligenza artificiale,
# perché i nostri contenuti possano essere indicizzati e citati correttamente.

# Crawler generici: accesso completo
User-agent: *
Allow: /

# OpenAI (ChatGPT / GPTBot)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# Anthropic (Claude)
User-agent: ClaudeBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: anthropic-ai
Allow: /

# Perplexity
User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

# Google (training AI / Gemini)
User-agent: Google-Extended
Allow: /

# Common Crawl
User-agent: CCBot
Allow: /

# ByteDance
User-agent: Bytespider
Allow: /

# Meta AI
User-agent: meta-externalagent
Allow: /

# Apple (Apple Intelligence)
User-agent: Applebot-Extended
Allow: /

Sitemap: {BASE}/sitemap.xml
Sitemap: {BASE}/sitemap-news.xml
""", encoding="utf-8")
print("robots.txt -> OK")

# ---------- feed.xml (RSS 2.0) ----------
_WD = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
_MO = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
def rfc822(d):
    y, m, dd = int(d[:4]), int(d[5:7]), int(d[8:10])
    wd = _WD[_date(y, m, dd).weekday()]
    return f"{wd}, {dd:02d} {_MO[m-1]} {y} 08:00:00 +0200"
items = []
for a in arts[:20]:
    items.append(f"""  <item>
    <title>{html.escape(a['title'])}</title>
    <link>{BASE}/articoli/{a['slug']}.html</link>
    <guid isPermaLink="true">{BASE}/articoli/{a['slug']}.html</guid>
    <description>{html.escape(a['desc'])}</description>
    <category>{html.escape(a['section'])}</category>
    <pubDate>{rfc822(a['date'])}</pubDate>
  </item>""")
feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Il Giornale Edile</title>
  <link>{BASE}/</link>
  <description>News, bonus e guide per l'edilizia italiana</description>
  <language>it-IT</language>
{chr(10).join(items)}
</channel>
</rss>
"""
(ROOT / "feed.xml").write_text(feed, encoding="utf-8")
print(f"feed.xml -> {len(items)} item")
