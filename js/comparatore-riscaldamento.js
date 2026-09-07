/* Il Giornale Edile — comparatore costi riscaldamento: caldaia, ibrido, pompa di calore.
   Costi di esercizio, installazione e manutenzione dalle rilevazioni pubblicate in
   "Caldaia a condensazione o pompa di calore: il confronto onesto del 2026".
   Valori indicativi per una casa tipo: non sostituiscono un progetto termotecnico. */
(function () {
  'use strict';
  // esercizio annuo (€) per scenario di isolamento
  var ESERCIZIO = {
    isolata: { label: 'Ben isolata (mandata 40 °C)', caldaia: 1000, pdc: 675,  pdcfv: 450 },
    media:   { label: 'Isolamento medio (50 °C)',    caldaia: 1100, pdc: 850,  pdcfv: 650 },
    scarsa:  { label: 'Poco isolata (65 °C)',        caldaia: 1300, pdc: 1300, pdcfv: 1100 }
  };
  var INSTALL = { caldaia: [1800, 3200], ibrido: [6000, 10000], pdc: [7000, 13000] };
  var MANUT   = { caldaia: 115, ibrido: 140, pdc: 115 };

  function el(id) { return document.getElementById(id); }
  function eur(n) { return Math.round(n).toLocaleString('it-IT', { useGrouping: true }) + ' €'; }
  function med(a) { return (a[0] + a[1]) / 2; }

  function calcola() {
    var iso = el('cmp-isolamento').value;
    var fv  = el('cmp-fv').checked;
    var out = el('cmp-out');
    var s = ESERCIZIO[iso];
    if (!s) { out.innerHTML = ''; return; }

    var eCaldaia = s.caldaia + MANUT.caldaia;
    var ePdc     = (fv ? s.pdcfv : s.pdc) + MANUT.pdc;
    var eIbrido  = ((s.caldaia + (fv ? s.pdcfv : s.pdc)) / 2) + MANUT.ibrido;

    var extraPdc = med(INSTALL.pdc) - med(INSTALL.caldaia);
    var risparmio = eCaldaia - ePdc;
    var rientro = risparmio > 0 ? extraPdc / risparmio : null;

    var righe = [
      ['Caldaia a condensazione', med(INSTALL.caldaia), eCaldaia, 'No', 'Limitati'],
      ['Sistema ibrido',          med(INSTALL.ibrido),  eIbrido,  'Parziale', 'Buoni'],
      ['Pompa di calore' + (fv ? ' + fotovoltaico' : ''), med(INSTALL.pdc), ePdc, 'Sì', 'Massimi']
    ];
    var minSpesa = Math.min.apply(null, righe.map(function (r) { return r[2]; }));

    var html = '<table class="cmp-table"><caption>' + s.label + (fv ? ' · con fotovoltaico' : '') + '</caption>' +
      '<thead><tr><th>Soluzione</th><th>Installazione</th><th>Spesa annua</th><th>Raffresca</th><th>Incentivi</th></tr></thead><tbody>';
    righe.forEach(function (r) {
      var best = r[2] === minSpesa ? ' class="cmp-best"' : '';
      html += '<tr' + best + '><th scope="row">' + r[0] + '</th><td>' + eur(r[1]) + '</td><td><strong>' +
              eur(r[2]) + '/anno</strong></td><td>' + r[3] + '</td><td>' + r[4] + '</td></tr>';
    });
    html += '</tbody></table>';

    if (rientro !== null && rientro > 0) {
      html += '<p class="cmp-note">Passare dalla caldaia alla pompa di calore costa circa <strong>' + eur(extraPdc) +
        '</strong> in più all’installazione e fa risparmiare <strong>' + eur(risparmio) +
        '</strong> l’anno: il maggior costo rientra in circa <strong>' + rientro.toFixed(1).replace('.', ',') +
        ' anni</strong>, senza contare gli incentivi che accorciano il conto.</p>';
    } else {
      html += '<p class="cmp-note">Su un edificio poco isolato la pompa di calore <strong>non conviene</strong>: ' +
        'lavorando a 65 °C il COP crolla e la spesa annua eguaglia o supera quella della caldaia. ' +
        'Prima conviene intervenire sull’involucro, oppure valutare il sistema ibrido.</p>';
    }
    html += '<p class="cmp-note">La manutenzione annua è già inclusa nella spesa. Gli incentivi non sono conteggiati: ' +
      'variano per intervento e reddito, e vanno verificati caso per caso.</p>';
    out.innerHTML = html;
  }

  function init() {
    var i = el('cmp-isolamento'), f = el('cmp-fv');
    if (!i) return;
    i.addEventListener('change', calcola);
    if (f) f.addEventListener('change', calcola);
    calcola();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
