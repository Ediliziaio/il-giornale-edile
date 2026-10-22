import { cpSync, existsSync, mkdirSync, readdirSync, rmSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const out = join(root, 'dist');
const directories = new Set(['guide-pratiche', 'speciali-aziende', 'editorial-assets', 'articoli', 'autore', 'categoria', 'comparatore', 'css', 'js', 'assets', 'fonts']);
const publicFile = /\.(html|xml|txt|ico|png|webmanifest)$/i;

// Every article is already HTML. Vite's single-entry build only emitted the
// home page; copy the complete public site, excluding source and configuration.
rmSync(out, { recursive: true, force: true });
mkdirSync(out);
for (const entry of readdirSync(root, { withFileTypes: true })) {
  const include = entry.isDirectory()
    ? directories.has(entry.name)
    : publicFile.test(entry.name) || entry.name === 'eic-lead.js';
  if (include) cpSync(join(root, entry.name), join(out, entry.name), { recursive: true });
}
for (const required of ['index.html', '404.html', 'robots.txt', 'sitemap.xml', 'feed.xml']) {
  if (!existsSync(join(out, required))) throw new Error(`Missing public output: ${required}`);
}
const pages = readdirSync(out, { recursive: true }).filter(file => file.endsWith('.html'));
console.log(`Static build: ${pages.length} complete HTML pages in dist/`);

// Search uses the same published native article files, never development drafts.
const search = readdirSync(join(out, 'articoli')).filter(f => f.endsWith('.html')).map(file => {
  const html = readFileSync(join(out, 'articoli', file), 'utf8');
  const text = value => value.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
  return { url: '/articoli/' + file, title: text(html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || ''), description: text(html.match(/<meta[^>]*name="description"[^>]*content="([^"]*)"/i)?.[1] || '') };
});
writeFileSync(join(out, 'assets', 'search-index.json'), JSON.stringify(search));
