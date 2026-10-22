(() => {
  const form = document.querySelector('form[role="search"]');
  const input = document.getElementById('q');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-count');
  if (!form || !input || !results || !status) return;
  const normalize = s => s.toLocaleLowerCase('it').normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  let articles = [];
  function render() {
    results.replaceChildren();
    const words = normalize(input.value.trim()).split(/\s+/).filter(Boolean);
    const matches = words.length ? articles.filter(a => words.every(w => normalize(a.title + ' ' + a.description).includes(w))) : [];
    status.textContent = words.length ? matches.length + ' articoli trovati' : 'Inserisci una parola chiave per cercare negli articoli.';
    for (const a of matches) {
      const article = document.createElement('article');
      const h = document.createElement('h2');
      const link = document.createElement('a'); link.href = a.url; link.textContent = a.title; h.append(link);
      const p = document.createElement('p'); p.textContent = a.description;
      article.append(h, p); results.append(article);
    }
  }
  form.addEventListener('submit', e => { e.preventDefault(); const u = new URL(location.href); u.searchParams.set('q', input.value); history.replaceState(null, '', u); render(); });
  input.addEventListener('input', render);
  input.value = new URLSearchParams(location.search).get('q') || '';
  fetch('/assets/search-index.json').then(r => { if (!r.ok) throw new Error(); return r.json(); }).then(data => { articles = data; render(); }).catch(() => { status.textContent = 'Ricerca non disponibile. Riprova tra poco.'; });
})();
