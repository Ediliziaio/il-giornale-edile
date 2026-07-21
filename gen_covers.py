#!/usr/bin/env python3
"""Genera le immagini di copertina 1200x630 WebP per tutti gli articoli + default home."""
import re, html, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
ART = ROOT / "articoli"
OUT = ROOT / "assets" / "covers"
OUT.mkdir(parents=True, exist_ok=True)

FONT_DIR = Path("/Users/agenteai/Library/Application Support/kimi-desktop/daimon-share/daimon/runtime/python/.venv/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf")
F_BOLD = str(FONT_DIR / "DejaVuSans-Bold.ttf")
F_REG = str(FONT_DIR / "DejaVuSans.ttf")

# palette coerente con le thumb CSS del sito
GRADS = {
    "t-bonus":     ((18, 53, 36), (31, 111, 67), (212, 160, 23)),
    "t-energia":   ((14, 58, 74), (17, 138, 178), (255, 209, 102)),
    "t-normative": ((26, 35, 64), (47, 74, 138), (138, 167, 224)),
    "t-materiali": ((58, 35, 24), (138, 90, 47), (216, 176, 138)),
    "t-mercato":   ((36, 26, 48), (92, 58, 138), (201, 167, 224)),
    "t-sicurezza": ((64, 33, 15), (193, 68, 14), (255, 183, 3)),
    "default":     ((32, 35, 42), (58, 63, 75), (200, 16, 46)),
}
BRAND = (200, 16, 46)

def vgrad(size, c1, c2, c3):
    """Gradiente diagonale a 3 colori."""
    w, h = size
    base = Image.new("RGB", size)
    px = base.load()
    for y in range(h):
        for x in range(0, w, 4):  # passo 4px per velocità
            t = (x / w + y / h) / 2
            if t < 0.55:
                k = t / 0.55
                c = tuple(int(c1[i] + (c2[i] - c1[i]) * k) for i in range(3))
            else:
                k = (t - 0.55) / 0.45
                c = tuple(int(c2[i] + (c3[i] - c2[i]) * k) for i in range(3))
            for dx in range(4):
                if x + dx < w: px[x + dx, y] = c
    return base

def grid_overlay(img):
    d = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    for x in range(0, w, 46):
        d.line([(x, 0), (x, h)], fill=(255, 255, 255, 10), width=2)
    for y in range(0, h, 46):
        d.line([(0, y), (w, y)], fill=(255, 255, 255, 10), width=2)

def make_cover(title, cat_label, tclass, out_path):
    W, H = 1200, 630
    c1, c2, c3 = GRADS.get(tclass, GRADS["default"])
    img = vgrad((W, H), c1, c2, c3)
    grid_overlay(img)
    d = ImageDraw.Draw(img)

    f_cat = ImageFont.truetype(F_BOLD, 30)
    f_title = ImageFont.truetype(F_BOLD, 58)
    f_site = ImageFont.truetype(F_BOLD, 26)

    # barra brand + etichetta categoria
    d.rectangle([70, 78, 130, 86], fill=BRAND)
    d.text((148, 66), cat_label.upper(), font=f_cat, fill=(255, 255, 255))

    # titolo su max 4 righe
    lines = textwrap.wrap(title, width=34)
    if len(lines) > 4:
        lines = lines[:4]
        lines[-1] = lines[-1].rstrip(".,:;") + "…"
    # riduci font se troppe righe
    ft = f_title
    if len(lines) >= 4:
        ft = ImageFont.truetype(F_BOLD, 48)
    y = 150
    for ln in lines:
        d.text((70, y), ln, font=ft, fill=(255, 255, 255))
        y += ft.size + 18

    # firma testata in basso
    d.rectangle([70, H - 96, 82, H - 36], fill=BRAND)
    d.text((100, H - 82), "IL GIORNALE EDILE", font=f_site, fill=(255, 255, 255))
    d.text((100, H - 50), "ilgiornaleedile.it", font=ImageFont.truetype(F_REG, 22), fill=(230, 230, 230))

    img.save(out_path, "WEBP", quality=82, method=6)
    return out_path

def parse(path):
    t = path.read_text(encoding="utf-8")
    h1 = re.search(r"<h1 itemprop=\"headline\">(.*?)</h1>", t, re.S)
    sec = re.search(r'article:section" content="(.*?)"', t)
    th = re.search(r'<figure class="thumb (t-\w+)', t)
    return (html.unescape(h1.group(1)).strip() if h1 else path.stem,
            html.unescape(sec.group(1)) if sec else "Il Giornale Edile",
            th.group(1) if th else "default")

count = 0
for p in sorted(ART.glob("*.html")):
    title, cat, tclass = parse(p)
    make_cover(title, cat, tclass, OUT / f"{p.stem}.webp")
    count += 1

# cover default per home/pagine
make_cover("News, bonus e guide per l'edilizia italiana", "Il Giornale Edile", "default", ROOT / "assets" / "cover-home.webp")
print(f"Copertine generate: {count} articoli + home")
