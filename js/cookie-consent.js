// Cookie consent GDPR — Il Giornale Edile
// Zero dipendenze, <6KB, caricato con defer: nessun impatto sulla resa mobile.
(function () {
  "use strict";

  var KEY = "ge_consent_v1";

  function getConsent() {
    try {
      var raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) { return null; }
  }

  function setConsent(consent) {
    consent.necessary = true;
    consent.ts = new Date().toISOString();
    try { localStorage.setItem(KEY, JSON.stringify(consent)); } catch (e) {}
    // Evento pubblico: qui si agganciano analytics e ad server quando il consenso c'è
    window.dispatchEvent(new CustomEvent("ge:consent", { detail: consent }));
  }

  function el(tag, cls, html) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (html != null) n.innerHTML = html;
    return n;
  }

  var banner = null;
  var reopenBtn = null;

  function hideBanner() {
    if (banner) {
      banner.classList.remove("ge-cb-visible");
      window.setTimeout(function () { banner.remove(); banner = null; }, 320);
    }
  }

  function showReopen() {
    if (reopenBtn) return;
    reopenBtn = el("button", "ge-cb-reopen", "Cookie");
    reopenBtn.type = "button";
    reopenBtn.setAttribute("aria-label", "Gestisci preferenze cookie");
    reopenBtn.addEventListener("click", function () { openBanner(); });
    document.body.appendChild(reopenBtn);
  }

  function buildBanner() {
    var c = getConsent() || { analytics: false, marketing: false };
    banner = el("div", "ge-cb");
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Informativa breve sui cookie");
    banner.setAttribute("aria-live", "polite");

    var inner = el("div", "ge-cb-inner");
    inner.appendChild(el("p", null,
      "<strong>Questo sito usa i cookie.</strong> Utilizziamo cookie tecnici necessari al funzionamento e, previo consenso, cookie di analisi e di marketing (anche per gli spazi pubblicitari). " +
      'Leggi la <a href="' + policyUrl() + '">Cookie Policy</a>.'
    ));

    // Pannello preferenze
    var prefs = el("div", "ge-cb-prefs");
    prefs.appendChild(prefRow("nec", "Necessari", "Sempre attivi: servono al funzionamento tecnico del sito.", true, true));
    prefs.appendChild(prefRow("ana", "Analisi", "Statistiche anonime di lettura per migliorare i contenuti.", c.analytics, false));
    prefs.appendChild(prefRow("mkt", "Marketing", "Misurazione e erogazione degli annunci pubblicitari.", c.marketing, false));
    inner.appendChild(prefs);

    // Azioni
    var actions = el("div", "ge-cb-actions");
    var accept = el("button", "ge-cb-accept", "Accetta tutti");
    accept.type = "button";
    accept.addEventListener("click", function () {
      setConsent({ analytics: true, marketing: true }); hideBanner(); showReopen();
    });
    var reject = el("button", "ge-cb-reject", "Rifiuta");
    reject.type = "button";
    reject.addEventListener("click", function () {
      setConsent({ analytics: false, marketing: false }); hideBanner(); showReopen();
    });
    var custom = el("button", "ge-cb-custom", "Personalizza");
    custom.type = "button";
    var save = el("button", "ge-cb-save", "Salva preferenze");
    save.type = "button";
    save.style.display = "none";
    custom.addEventListener("click", function () {
      banner.classList.add("ge-cb-show-prefs");
      custom.style.display = "none";
      save.style.display = "";
      reject.focus();
    });
    save.addEventListener("click", function () {
      setConsent({
        analytics: prefs.querySelector("#ge-cb-ana").checked,
        marketing: prefs.querySelector("#ge-cb-mkt").checked
      });
      hideBanner(); showReopen();
    });
    actions.appendChild(accept);
    actions.appendChild(reject);
    actions.appendChild(custom);
    actions.appendChild(save);
    inner.appendChild(actions);

    banner.appendChild(inner);
    document.body.appendChild(banner);
    // attiva la transizione dopo il primo paint
    window.requestAnimationFrame(function () {
      window.requestAnimationFrame(function () { banner.classList.add("ge-cb-visible"); });
    });
  }

  function prefRow(id, label, hint, checked, disabled) {
    var row = el("div", "ge-cb-pref");
    var input = document.createElement("input");
    input.type = "checkbox";
    input.id = "ge-cb-" + id;
    input.checked = checked;
    if (disabled) input.disabled = true;
    var lab = document.createElement("label");
    lab.setAttribute("for", "ge-cb-" + id);
    lab.innerHTML = label + "<small>" + hint + "</small>";
    row.appendChild(input);
    row.appendChild(lab);
    return row;
  }

  function policyUrl() {
    // funziona sia dalla root che da /articoli/ e /categoria/
    return location.pathname.indexOf("/articoli/") !== -1 || location.pathname.indexOf("/categoria/") !== -1
      ? "../cookie-policy.html" : "cookie-policy.html";
  }

  function openBanner() {
    if (banner) return;
    buildBanner();
  }

  // API pubblica minima
  window.geConsent = {
    get: getConsent,
    open: openBanner,
    has: function (what) {
      var c = getConsent();
      return !!(c && c[what]);
    }
  };

  // Link "Gestisci cookie" nel footer / nella policy
  document.addEventListener("click", function (ev) {
    var t = ev.target.closest("[data-ge-consent-open]");
    if (t) { ev.preventDefault(); openBanner(); }
  });

  // Avvio: mostra il banner solo se manca il consenso
  if (!getConsent()) {
    buildBanner();
  } else {
    showReopen();
  }
})();
