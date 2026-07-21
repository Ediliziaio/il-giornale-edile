// Il Giornale Edile — JS minimo (progressive enhancement, nessuna dipendenza)
(function () {
  "use strict";

  // Data corrente nella topbar (formato italiano)
  var dateEl = document.querySelector("[data-tb-date]");
  if (dateEl) {
    var fmt = new Intl.DateTimeFormat("it-IT", {
      weekday: "long", day: "numeric", month: "long", year: "numeric"
    });
    dateEl.textContent = fmt.format(new Date());
  }

  // Barra di avanzamento lettura nelle pagine articolo
  var progress = document.querySelector(".reading-progress");
  if (progress) {
    var onScroll = function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
      progress.style.width = Math.min(100, pct) + "%";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  // Anno corrente nel footer
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) { yearEl.textContent = new Date().getFullYear(); }
})();
