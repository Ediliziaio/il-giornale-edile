# Checklist di pubblicazione — Il Giornale Edile

Documento operativo per la messa online della testata. Stato al 21 luglio 2026.

---

## 1. Hosting e dominio
- [ ] Registrare/puntare il dominio `ilgiornaleedile.it` (DNS A/CNAME verso l'hosting).
- [ ] Deploy della cartella del sito così com'è: è un sito statico, funziona ovunque (Netlify, Vercel, Cloudflare Pages, Aruba, SiteGround, qualsiasi hosting con HTTPS).
- [ ] Attivare HTTPS (certificato automatico incluso in tutte le piattaforme sopra).
- [ ] Attivare cache/CDN (Cloudflare gratuito): cache HTML breve (5-10 min), cache lunga per `assets/`, `css/`, `js/` e `*.webp`.
- [ ] Verificare compressione brotli/gzip lato server.

## 2. Indicizzazione (SEO)
- [ ] **Google Search Console**: aggiungi la proprietà dominio, verifica via DNS (o file HTML), invia `https://www.ilgiornaleedile.it/sitemap.xml`.
- [ ] **Bing Webmaster Tools**: importa direttamente da Search Console (import automatico) — Bing alimenta anche Copilot/AI answers (importante per AEO).
- [ ] Controllare dopo 48-72h: copertura indice, eventuali errori di scansione, rapporto Core Web Vitals.
- [ ] `robots.txt` e `sitemap.xml` sono già pronti nella root.

## 3. Contenuti e keyword map (anti-cannibalizzazione)
Ogni keyword ha UNA pagina pilastro; gli articoli affini linkano al pilastro con anchor descrittiva.

| Cluster | Pilastro | Articoli satellite |
|---|---|---|
| Fotovoltaico | `pannelli-solari-fotovoltaico-guida` | `fotovoltaico-costi-permessi-2026`, `top-5-fornitori-pannelli-solari`, `comunita-energetiche-cer-guida` |
| Bonus ristrutturazione | `bonus-ristrutturazione-2026-guida-completa` | `detrazioni-ristrutturazione-50-36`, `superbonus-2026-cosa-resta` |
| Efficienza energetica | `ecobonus-65-guida` | `conto-termico-3-guida`, `cappotto-termico-materiali-confronto`, `certificazione-ape-regole-2026` |
| Pompe di calore | `top-5-pompe-di-calore` | `riscaldamento-a-pavimento-pro-contro` |
| Serramenti | `infissi-pvc-alluminio-legno-confronto` | `top-5-produttori-serramenti` |
| BIM | `bim-obbligatorio-scadenze` | `top-5-software-bim` |
| Ristrutturare casa | `costo-ristrutturazione-al-mq-2026` | `ristrutturazione-chiavi-in-mano`, `costruire-casa-prefabbricata-costi` |

Regole redazionali:
- Non pubblicare due articoli sulla stessa identica query: aggiornare il pilastro esistente.
- Ogni nuovo articolo deve linkare il suo pilastro entro il primo terzo del testo.
- Aggiornare `dateModified` (visibile e JSON-LD) solo a seguito di modifiche sostanziali, mai automaticamente.

## 4. Monetizzazione (slot pubblicitari)
- Gli slot sono già predisposti con attributo `data-ad-slot`: `leaderboard-top`, `mobile-top`, `sidebar-halfpage`, `sidebar-rect`, `inarticle-1`, `infeed`, `footer-leaderboard`.
- **Caricare gli script dell'ad server (AdSense/Ad Manager) SOLO dopo consenso marketing**: agganciarsi all'evento `ge:consent` (vedi `js/cookie-consent.js`) e iniettare gli script quando `detail.marketing === true`, oltre che al caricamento se il consenso esiste già.
- Registrare il sito in Google AdSense/Ad Manager e aggiornare la Cookie Policy con l'elenco fornitori (IAB TCF se richiesto dal network).

## 5. Analytics
- Installare lo strumento di analisi (GA4, Plausible o Matomo) **solo dopo consenso "Analisi"**, stesso meccanismo dell'evento `ge:consent`.
- Obiettivi consigliati: lettura completa articolo (scroll 75%), click sui link uscita "Top 5", iscrizione newsletter.

## 6. Newsletter
- I form attualmente hanno `action="#"`: collegare un backend reale (Brevo — piano gratuito fino a 300 email/giorno — Mailchimp o MailerLite).
- Sostituire `action="#"` con l'endpoint del provider e aggiungere il double opt-in (obbligatorio per GDPR).

## 7. Conformità legale (obbligatoria per una testata)
- [ ] **Registrazione della testata** presso il Tribunale competente (art. 5 L. 47/1948) con nomina del direttore responsabile — attualmente il sito indica "da definirsi" nelle Note legali.
- [ ] Iscrizione al ROC (Registro Operatori di Comunicazione) AGCOM.
- [ ] Completare `note-legali.html` con i dati effettivi (editore, direttore, numero di registrazione).
- [ ] Verifica finale redazionale di tutti i contenuti prima del lancio (fact-check normativo già eseguito il 21/07/2026 su 12 articoli sensibili).

## 8. ⚠️ Processo esterno di scrittura file
Durante lo sviluppo sono stati rilevati file creati/modificati nella cartella del sito da un processo esterno a questa sessione (nuovi articoli, pagine categoria, riscritture). Non risulta alcuna automazione pianificata in Kimi Work. **Prima del lancio: identificare e fermare il processo** (altra sessione/agente aperta sulla stessa cartella), altrimenti i contenuti potranno essere sovrascritti senza controllo.

## 9. Post-lancio (prime 4 settimane)
- [ ] Monitorare query e CTR in Search Console; riscrivere title/description delle pagine con CTR < 2%.
- [ ] Pubblicare 2-3 articoli/settimana sui cluster esistenti (freschezza = ranking su query bonus/normative).
- [ ] Aggiornare le "Top 5" con prezzi reali raccolti dai listini/fornitori.
- [ ] Valutare immagini fotografiche reali al posto delle copertine grafiche generate (le copertine attuali sono valide per og:image e Discover, ma foto reali aumentano il CTR).
