#!/usr/bin/env python3
"""Verifica finale: link/ancore, XML, conteggi, nav uniforme, copertura articoli."""
import re, glob, os, sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path('/Users/agenteai/Documents/kimi/workspace/giornale-edile')
os.chdir(ROOT)
errors = []

html_files = sorted(glob.glob('*.html') + glob.glob('categoria/*.html') + glob.glob('articoli/*.html'))

# ---------- (a) link + anchor check ----------
for f in html_files:
    t = open(f, encoding='utf-8').read()
    base = os.path.dirname(f)
    ids = set(re.findall(r'id="([^"]+)"', t))
    for attr in ('href', 'src'):
        for m in re.finditer(attr + r'="([^"]+)"', t):
            u = m.group(1)
            if u.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:')) or u == '#':
                continue
            path, _, frag = u.partition('#')
            if path:
                target = os.path.normpath(os.path.join(base, path))
                if not os.path.exists(target):
                    errors.append(f'[link] {f}: {attr}="{u}" -> file mancante')
                    continue
                if frag and target.endswith('.html'):
                    tt = open(target, encoding='utf-8').read()
                    if f'id="{frag}"' not in tt:
                        errors.append(f'[anchor-x] {f}: {u} -> ancora assente in {target}')
            elif frag:
                if frag not in ids:
                    errors.append(f'[anchor] {f}: #{frag} non risolve nella stessa pagina')

# ---------- (b) XML well-formed ----------
for x in ('sitemap.xml', 'sitemap-news.xml', 'feed.xml'):
    try:
        ET.parse(x)
    except Exception as e:
        errors.append(f'[xml] {x}: {e}')

# ---------- (c) conteggi ----------
n_html = len(html_files)
n_sitemap = open('sitemap.xml', encoding='utf-8').read().count('<url>')
n_feed = open('feed.xml', encoding='utf-8').read().count('<item>')
n_news = open('sitemap-news.xml', encoding='utf-8').read().count('<url>')

# ---------- (d) nav identica ----------
sigs = {}
for f in html_files:
    t = open(f, encoding='utf-8').read()
    m = re.search(r'<nav class="mainnav".*?</nav>', t, re.S)
    if not m:
        errors.append(f'[nav] {f}: mainnav assente'); continue
    items = tuple(re.findall(r'<li><a href="[^"]*?([^/"]+\.html)"[^>]*>([^<]+)</a></li>', m.group(0)))
    sigs.setdefault(items, []).append(f)
if len(sigs) != 1:
    errors.append(f'[nav] {len(sigs)} varianti di nav trovate')
nav_n = len(next(iter(sigs))) if sigs else 0

# ---------- (e) copertura articoli: categoria, sitemap.html, sitemap.xml ----------
SEC2CAT = {
    'Bonus & Fisco': 'bonus-fiscali', 'Energia & Rinnovabili': 'energia-rinnovabili',
    'Normative & Cantieri': 'normative-cantieri', 'Materiali & Tecnologie': 'materiali-tecnologie',
    'Mercato & Immobiliare': 'mercato-immobiliare', 'Serramenti & Infissi': 'serramenti-infissi',
}
sitemap_html = open('sitemap.html', encoding='utf-8').read()
sitemap_xml = open('sitemap.xml', encoding='utf-8').read()
cat_cache = {}
for f in sorted(glob.glob('articoli/*.html')):
    slug = Path(f).stem
    t = open(f, encoding='utf-8').read()
    sec = re.search(r'article:section" content="([^"]+)"', t).group(1).replace('&amp;', '&')
    cat = SEC2CAT[sec]
    if cat not in cat_cache:
        cat_cache[cat] = open(f'categoria/{cat}.html', encoding='utf-8').read()
    if f'articoli/{slug}.html' not in cat_cache[cat]:
        errors.append(f'[cover] {slug} assente da categoria/{cat}.html')
    if f'articoli/{slug}.html' not in sitemap_html:
        errors.append(f'[cover] {slug} assente da sitemap.html')
    if f'articoli/{slug}.html' not in sitemap_xml:
        errors.append(f'[cover] {slug} assente da sitemap.xml')

# ---------- report ----------
print('=== VERIFICA FINALE ===')
print(f'pagine HTML:        {n_html}')
print(f'URL sitemap.xml:    {n_sitemap}')
print(f'item feed.xml:      {n_feed}')
print(f'item sitemap-news:  {n_news}')
print(f'nav: {len(sigs)} variante(i), {nav_n} voci')
if errors:
    print(f'\nERRORI ({len(errors)}):')
    for e in errors[:50]:
        print(' ', e)
    sys.exit(1)
print('\n0 errori: tutti i controlli superati ✅')
