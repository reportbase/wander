// MRB run 1, post hoc (after P2 was killed at e = 0.7; not a prediction): 16 seeds at φ = 0.1, e = 0.7 and 0.9.
// Separates the seeds' noise from a systematic deficit, and reads where it comes from: the contacts per marble per unit
// time over Enskog's at the current T, and the box-scale flow R, through the fit's range.
// node plans/mrb/posthoc1.mjs → plans/mrb/mrb-run1-posthoc.txt
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { oneRun } from './hcs.mjs';
const out = [], say = s => { out.push(s); console.log(s); };
const chi = p => (1 - p / 2) / (1 - p) ** 3, a2 = e => 16 * (1 - e) * (1 - 2 * e * e) / (81 - 17 * e + 30 * (1 - e) * e * e);
const perContact = e => (1 - e * e) / 3 * (1 + 3 * a2(e) / 16) / (1 - a2(e) / 16);
const clock = (p, e) => 2 / 3 * Math.sqrt(Math.PI) * (6 * p / Math.PI) * chi(p) * (1 - e * e) * (1 + 3 * a2(e) / 16);
const omega = (p, e) => 4 * Math.sqrt(Math.PI) * (6 * p / Math.PI) * chi(p) * (1 - a2(e) / 16);
const fit = (X, Y) => { const n = X.length, mx = X.reduce((a, b) => a + b) / n, my = Y.reduce((a, b) => a + b) / n; let sxy = 0, sxx = 0;
  for (let k = 0; k < n; k++) { sxy += (X[k] - mx) * (Y[k] - my); sxx += (X[k] - mx) ** 2; } return sxy / sxx; };
const mean = a => a.reduce((x, y) => x + y) / a.length, sem = a => { const m = mean(a); return Math.sqrt(a.reduce((s, x) => s + (x - m) ** 2, 0) / (a.length - 1) / a.length); };
const phi = 0.1;
for (const e of [0.9, 0.7]) {
  const C1 = 5 + 3 * Math.log(100) / (1 - e * e), sC = [], st = [], rate = { a: [], b: [], c: [] }, R = { a: [], b: [], c: [] };
  for (let seed = 1; seed <= 16; seed++) {
    const r = oneRun({ phi, e, seed, Cmax: Math.ceil(C1) + 1 }), w = r.samples.filter(s => s.C >= 5 && s.C <= C1 + 1e-9);
    sC.push(fit(w.map(s => s.C), w.map(s => -Math.log(s.T)))); st.push(fit(w.map(s => s.t), w.map(s => s.T ** -0.5)));
    // contact rate over Enskog at the current T, in thirds of the range: ΔC / Σ ω_E √T Δt
    const third = (C1 - 5) / 3;
    for (const [k, lo] of [['a', 5], ['b', 5 + third], ['c', 5 + 2 * third]]) {
      const ww = w.filter(s => s.C >= lo - 1e-9 && s.C <= lo + third + 1e-9); let num = 0, den = 0;
      for (let m = 1; m < ww.length; m++) { num += ww[m].C - ww[m - 1].C; den += omega(phi, e) * Math.sqrt((ww[m].T + ww[m - 1].T) / 2) * (ww[m].t - ww[m - 1].t); }
      rate[k].push(num / den); R[k].push(mean(ww.map(s => s.R)));
    }
  }
  say(`φ ${phi} e ${e}, 16 seeds, C 5 to ${C1.toFixed(1)}:`);
  say(`  per contact ${mean(sC).toFixed(5)} ± ${sem(sC).toFixed(5)} (predicted ${perContact(e).toFixed(5)}, ${((mean(sC) / perContact(e) - 1) * 100).toFixed(2)}%)`);
  say(`  clock ${mean(st).toFixed(5)} ± ${sem(st).toFixed(5)} (predicted ${clock(phi, e).toFixed(5)}, ${((mean(st) / clock(phi, e) - 1) * 100).toFixed(2)}%)`);
  say(`  contact rate over Enskog's at the current T (with a₂), by thirds: ${['a', 'b', 'c'].map(k => `${mean(rate[k]).toFixed(4)} ± ${sem(rate[k]).toFixed(4)}`).join(', ')}`);
  say(`  box-scale flow R, mean by thirds: ${['a', 'b', 'c'].map(k => mean(R[k]).toFixed(2)).join(', ')}`);
}
writeFileSync(fileURLToPath(new URL('mrb-run1-posthoc.txt', import.meta.url)), out.join('\n') + '\n');
