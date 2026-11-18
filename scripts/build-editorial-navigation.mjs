import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const tools = dirname(fileURLToPath(import.meta.url));
const root = dirname(tools);
const config = JSON.parse(readFileSync(join(tools, 'editorial-navigation.json'), 'utf8'));
const origin = config.origin;
const excluded = new Set(['dist', 'node_modules', '.git', 'tools', 'scripts', 'build', 'editorial', 'assets', 'editorial-assets', 'css', 'js', 'fonts']);
const decode = s => s.replace(/&(?:amp|lt|gt|quot|apos|nbsp|#39|#x27);/gi, m => ({'&amp;':'&','&lt;':'<','&gt;':'>','&quot;':'"','&apos;':"'",'&nbsp;':' ','&#39;':"'",'&#x27;':"'"}[m.toLowerCase()] || m)).replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n))).replace(/&#x([\da-f]+);/gi, (_, n) => String.fromCodePoint(parseInt(n, 16)));
const text = s => decode(s.replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const attrs = s => Object.fromEntries([...s.matchAll(/([\w:-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g)].map(m => [m[1].toLowerCase(), decode(m[2] ?? m[3])]));
const norm = value => {
  const url = new URL(value, origin);
  if (url.origin !== origin) throw new Error(`Off-site editorial target: ${value}`);
  return url.pathname.replace(/\/index\.html$/, '/') || '/';
};
const key = s => s.toLowerCase().replace(/&|\be\b/g, ' ').replace(/[^\p{L}\p{N}]+/gu, ' ').trim();
const pages = [];
function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.') || excluded.has(entry.name)) continue;
    const file = join(dir, entry.name);
    if (entry.isDirectory()) { walk(file); continue; }
    if (!entry.name.endsWith('.html')) continue;
    const html = readFileSync(file, 'utf8');
    const links = [...html.matchAll(/<link\b[^>]*>/gi)].map(m => attrs(m[0]));
    const canonical = links.find(a => a.rel === 'canonical')?.href;
    if (!canonical || new URL(canonical).origin !== origin) continue;
    const path = norm(canonical);
    const noindex = [...html.matchAll(/<meta\b[^>]*>/gi)].map(m => attrs(m[0])).some(a => a.name === 'robots' && /noindex/i.test(a.content || ''));
    pages.push({ file, rel: relative(root, file).replaceAll('\\', '/'), html, canonical, path, noindex, title: text(html.match(/<h1\b[^>]*>([\s\S]*?)<\/h1>/i)?.[1] || '') });
  }
}
walk(root);
const byPath = new Map(pages.map(p => [p.path, p]));
const articles = pages.filter(p => !p.noindex && (config.kind === 'cardine' ? /^\/[^/]+\/[^/]+\/$/.test(p.path) : p.path.startsWith('/articoli/')));
for (const page of articles) {
  const section = page.html.match(/"articleSection"\s*:\s*"([^"]+)"/)?.[1] || '';
  page.hub = config.kind === 'cardine'
    ? config.hubs.find(h => page.path.startsWith(h.path))
    : config.hubs.find(h => (h.aliases || []).map(key).includes(key(decode(section))));
  if (!page.hub && config.articleHubs?.[page.path]) page.hub = config.hubs.find(h => h.path === config.articleHubs[page.path]);
  if (!page.hub) throw new Error(`Missing editorial category: ${page.path} (${section})`);
}
const ordered = list => [...list].sort((a, b) => a.title.localeCompare(b.title, 'it'));
const anchor = (path, label) => {
  if (label !== undefined && typeof label !== 'string') throw new TypeError(`Invalid editorial label for ${path}`);
  const page = byPath.get(norm(path));
  if (!page || page.noindex) throw new Error(`Missing/index-excluded reading target: ${path}`);
  return `<a href="${esc(page.path)}">${esc(label || page.title)}</a>`;
};
function linkedPaths(html, base) {
  html = html.match(/<main\b[^>]*>([\s\S]*?)<\/main>/i)?.[1] || html;
  const result = new Set();
  for (const m of html.matchAll(/<a\b[^>]*href\s*=\s*(?:"([^"]*)"|'([^']*)')/gi)) {
    try { result.add(norm(new URL(decode(m[1] ?? m[2]), base).href)); } catch { /* External and non-HTTP links are outside the editorial index. */ }
  }
  return result;
}
function itemList(page, members) {
  return { '@context': 'https://schema.org', '@type': 'ItemList', '@id': page.canonical + '#articoli', name: `Articoli — ${page.title}`, itemListOrder: 'https://schema.org/ItemListUnordered', numberOfItems: members.length, itemListElement: ordered(members).map((a, i) => ({ '@type': 'ListItem', position: i + 1, url: a.canonical, name: a.title })) };
}
function syncSchema(html, page, members) {
  const list = itemList(page, members);
  let foundList = false;
  html = html.replace(/(<script\b[^>]*type=["']application\/ld\+json["'][^>]*>)([\s\S]*?)(<\/script>)/gi, (whole, open, body, close) => {
    let value;
    try { value = JSON.parse(body); } catch { throw new Error(`Invalid JSON-LD in ${page.rel}`); }
    if (value['@type'] === 'ItemList') {
      if (foundList) throw new Error(`Multiple article ItemLists in ${page.rel}`);
      foundList = true;
      return `${open}\n${JSON.stringify(list, null, 2)}\n${close}`;
    }
    let changed = false;
    const visit = node => {
      if (!node || typeof node !== 'object') return;
      if (Array.isArray(node)) { node.forEach(visit); return; }
      if (node['@type'] === 'CollectionPage') {
        node.mainEntity = { '@id': list['@id'] };
        changed = true;
      }
      if (node['@graph']) visit(node['@graph']);
    };
    visit(value);
    return changed ? `${open}\n${JSON.stringify(value, null, 2)}\n${close}` : whole;
  });
  if (!foundList) html = html.replace(/<\/head>/i, `<script type="application/ld+json" data-editorial-index>\n${JSON.stringify(list, null, 2)}\n</script>\n</head>`);
  return html;
}
function managed(html, name, content, insert) {
  const start = `<!-- editorial-${name}:start -->`;
  const end = `<!-- editorial-${name}:end -->`;
  const block = `${start}\n${content}\n${end}`;
  const from = html.indexOf(start);
  if (from >= 0) {
    const to = html.indexOf(end, from);
    if (to < 0) throw new Error(`Unclosed editorial marker: ${name}`);
    return html.slice(0, from) + block + html.slice(to + end.length);
  }
  return insert(html, block);
}
function elementRange(html, openPattern) {
  const match = openPattern.exec(html);
  if (!match) throw new Error(`Missing managed element: ${openPattern}`);
  const tag = match[0].match(/^<([\w-]+)/)[1];
  const tokens = new RegExp(`<\\/?${tag}\\b[^>]*>`, 'gi');
  tokens.lastIndex = match.index + match[0].length;
  let depth = 1, token;
  while ((token = tokens.exec(html))) {
    depth += token[0].startsWith('</') ? -1 : 1;
    if (!depth) return { from: match.index, start: match.index + match[0].length, end: token.index, to: tokens.lastIndex };
  }
  throw new Error(`Unclosed managed element: ${openPattern}`);
}
const changed = [];
function save(page, html) {
  if (html !== page.html) { writeFileSync(page.file, html); page.html = html; changed.push(page.rel); }
}
for (const hub of config.hubs) {
  const page = byPath.get(hub.path);
  if (!page) throw new Error(`Missing category: ${hub.path}`);
  const members = articles.filter(a => a.hub.path === hub.path);
  let content = `<section class="${config.kind === 'cardine' ? 'widget' : 'cat-guide article-body'}" aria-labelledby="percorso-lettura">\n<h2${config.kind === 'cardine' ? ' class="w-title"' : ''} id="percorso-lettura">Da dove iniziare</h2>\n<p>${esc(hub.intro)}</p>\n`;
  for (const route of hub.routes) content += `<h3>${esc(route.title)}</h3>\n<p>${esc(route.description)} ${route.links.map(path => anchor(path)).join(' · ')}.</p>\n`;
  const outsideManaged = page.html.replace(/<!-- editorial-reading-paths:start -->[\s\S]*?<!-- editorial-reading-paths:end -->/g, '');
  const visible = linkedPaths(outsideManaged, page.canonical);
  hub.routes.flatMap(r => r.links).forEach(p => visible.add(norm(p)));
  const missing = ordered(members.filter(a => !visible.has(a.path)));
  if (missing.length) content += `<h3>Altre guide della sezione</h3>\n<ul>\n${missing.map(a => `<li>${anchor(a.path)}</li>`).join('\n')}\n</ul>\n`;
  content += '</section>';
  let html = managed(page.html, 'reading-paths', content, (source, block) => {
    const main = source.indexOf('<main');
    const pos = source.indexOf('<div class="card-grid">', main);
    if (pos < 0) throw new Error(`Missing category card grid: ${page.rel}`);
    return source.slice(0, pos) + block + '\n' + source.slice(pos);
  });
  // Every structured list entry has a visible ordinary link in the category.
  const afterLinks = linkedPaths(html, page.canonical);
  if (members.some(a => !afterLinks.has(a.path))) throw new Error(`Incomplete category index: ${page.rel}`);
  html = syncSchema(html, page, members);
  save(page, html);
}
const archive = byPath.get(config.archive);
if (!archive) throw new Error('Missing HTML editorial archive');
const archiveContent = config.hubs.map(h => {
  const members = ordered(articles.filter(a => a.hub.path === h.path));
  return `<section aria-labelledby="indice-${esc(h.path.replace(/[^a-z0-9]+/g, '-'))}">\n<h2 id="indice-${esc(h.path.replace(/[^a-z0-9]+/g, '-'))}">${anchor(h.path)}</h2>\n<p>${esc(h.archiveDescription)}</p>\n<ul>\n${members.map(a => `<li>${anchor(a.path)}</li>`).join('\n')}\n</ul>\n</section>`;
}).join('\n');
let archiveHTML = archive.html;
if (config.kind === 'cardine') {
  const range = elementRange(archiveHTML, /<div\b[^>]*class="sitemap-cols"[^>]*>/i);
  archiveHTML = archiveHTML.slice(0, range.start) + '\n' + archiveContent + '\n' + archiveHTML.slice(range.end);
} else {
  const range = elementRange(archiveHTML, /<article\b[^>]*class="article-body"[^>]*>/i);
  const header = archiveHTML.slice(range.start, range.end).match(/<h1\b[^>]*>[\s\S]*?<\/h1>/i)?.[0];
  if (!header) throw new Error('Archive heading missing');
  const inner = archiveHTML.slice(range.start, range.end);
  const servicesAt = inner.indexOf('<h2>Guide e strumenti</h2>');
  if (servicesAt < 0) throw new Error('Archive service links missing');
  const services = inner.slice(servicesAt).trimEnd();
  archiveHTML = archiveHTML.slice(0, range.start) + '\n' + header + `\n<p class="standfirst">L’indice degli ${articles.length} articoli pubblicati, divisi per argomento. Scegli una sezione per trovare le guide, i confronti e le presentazioni aziendali già disponibili.</p>\n` + archiveContent + '\n' + services + '\n' + archiveHTML.slice(range.end);
}
archiveHTML = syncSchema(archiveHTML, archive, articles);
save(archive, archiveHTML);
// A small number of deliberate paragraph links, rather than a shared keyword block.
for (const context of config.contexts) {
  const page = byPath.get(context.path);
  if (!page) throw new Error(`Missing contextual source: ${context.path}`);
  const content = '<p>' + context.parts.map(p => typeof p === 'string' ? esc(p) : anchor(p.path, p.label)).join('') + '</p>';
  let html = managed(page.html, 'context', content, (source, block) => {
    const faq = /<h2\b[^>]*>\s*(?:Domande frequenti|FAQ)\b[^<]*<\/h2>/i.exec(source);
    if (!faq) throw new Error(`Context FAQ insertion point missing: ${page.rel}`);
    return source.slice(0, faq.index) + block + '\n' + source.slice(faq.index);
  });
  if (context.breadcrumb) {
    const hub = byPath.get(context.breadcrumb);
    html = html.replace(/<nav aria-label="Percorso"><a href="\/">[^<]*<\/a> \/ Guida pratica<\/nav>/, `<nav aria-label="Percorso"><a href="/">${esc(config.name)}</a> / ${anchor(hub.path)} / ${esc(page.title)}</nav>`);
  }
  save(page, html);
}
console.log(`Editorial navigation: ${articles.length} canonical articles, ${config.hubs.length} categories, complete archive; ${changed.length} source files updated.`);
