// Comparatore — Il Giornale Edile
// Progressive enhancement: la tabella e' completa e indicizzabile anche senza JS.
(function () {
  "use strict";
  var table = document.querySelector("table.cmp");
  if (!table) return;

  var tbody   = table.tBodies[0];
  var rows    = Array.prototype.slice.call(tbody.rows);
  var search  = document.querySelector("[data-cmp-search]");
  var sortSel = document.querySelector("[data-cmp-sort]");
  var count   = document.querySelector("[data-cmp-count]");
  var reset   = document.querySelector("[data-cmp-reset]");
  var total   = rows.length;

  // Estrae il primo numero utile da una cella (gestisce "9.000-11.000 €", "0,35 €/Wp")
  function num(txt) {
    var m = txt.replace(/\./g, "").replace(/,/g, ".").match(/-?\d+(\.\d+)?/);
    return m ? parseFloat(m[0]) : null;
  }

  function render() {
    var q = (search && search.value || "").trim().toLowerCase();
    var visible = 0;
    rows.forEach(function (tr) {
      var hit = !q || tr.textContent.toLowerCase().indexOf(q) !== -1;
      tr.hidden = !hit;
      if (hit) visible++;
    });
    if (count) {
      count.textContent = visible === total
        ? total + " a confronto"
        : visible + " di " + total;
    }
    var empty = document.querySelector("[data-cmp-empty]");
    if (empty) empty.hidden = visible !== 0;
  }

  function sortBy(idx, dir) {
    var sorted = rows.slice().sort(function (a, b) {
      var ta = a.cells[idx] ? a.cells[idx].textContent.trim() : "";
      var tb = b.cells[idx] ? b.cells[idx].textContent.trim() : "";
      var na = num(ta), nb = num(tb);
      var r;
      if (na !== null && nb !== null) r = na - nb;
      else r = ta.localeCompare(tb, "it", { sensitivity: "base" });
      return dir === "desc" ? -r : r;
    });
    sorted.forEach(function (tr) { tbody.appendChild(tr); });

    Array.prototype.forEach.call(table.tHead.rows[0].cells, function (th, i) {
      if (i === idx) th.setAttribute("aria-sort", dir === "desc" ? "descending" : "ascending");
      else th.removeAttribute("aria-sort");
    });
  }

  // Ordinamento cliccando l'intestazione
  Array.prototype.forEach.call(table.tHead.rows[0].cells, function (th, i) {
    th.classList.add("sortable");
    th.tabIndex = 0;
    th.setAttribute("role", "button");
    var toggle = function () {
      var dir = th.getAttribute("aria-sort") === "ascending" ? "desc" : "asc";
      sortBy(i, dir);
      if (sortSel) sortSel.value = i + ":" + dir;
    };
    th.addEventListener("click", toggle);
    th.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); toggle(); }
    });
  });

  if (search)  search.addEventListener("input", render);
  if (sortSel) sortSel.addEventListener("change", function () {
    var p = sortSel.value.split(":");
    if (p.length === 2) sortBy(parseInt(p[0], 10), p[1]);
  });
  if (reset) reset.addEventListener("click", function () {
    if (search) search.value = "";
    render();
    if (search) search.focus();
  });

  render();
})();
