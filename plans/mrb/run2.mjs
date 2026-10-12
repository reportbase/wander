// MRB run 2: e = 0.7 at φ = 0.05, 0.1, 0.15 (L/L_c ≈ 0.50, 0.79, 1.00 by the plan's estimate), 16 seeds each.
// node plans/mrb/run2.mjs → plans/mrb/mrb-run2.txt
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { oneRun } from './hcs.mjs';
const out = [], say = s => { out.push(s); console.log(s); };
const chi = p => (1 - p / 2) / (1 - p) ** 3, a2 = e => 16 * (1 - e) * (1 - 2 * e * e) / (81 - 17 * e + 30 * (1 - e) * e * e);
const perContact = e => (1 - e * e) / 3 * (1 + 3 * a2(e) / 16) / (1 - a2(e) / 16);
const clock = (p, e) => 2 / 3 * Math.sqrt(Math.PI) * (6 * p / Math.PI) * chi(p) * (1 - e * e) * (1 + 3 * a2(e) / 16);
const fit = (X, Y) => { const n = X.length, mx = X.reduce((a, b) => a + b) / n, my = Y.reduce((a, b) => a + b) / n; let sxy = 0, sxx = 0;
  for (let k = 0; k < n; k++) { sxy += (X[k] - mx) * (Y[k] - my); sxx += (X[k] - mx) ** 2; } return sxy / sxx; };
const mean = a => a.reduce((x, y) => x + y) / a.length, sem = a => { const m = mean(a); return Math.sqrt(a.reduce((s, x) => s + (x - m) ** 2, 0) / (a.length - 1) / a.length); };
const e = 0.7, C1 = 5 + 3 * Math.log(100) / (1 - e * e), third = (C1 - 5) / 3, res = {};
for (const phi of [0.05, 0.1, 0.15]) {
  const sC = [], st = [], R = [], col = [];
  for (let seed = 1; seed <= 16; seed++) {
    const r = oneRun({ phi, e, seed, Cmax: Math.ceil(C1) + 1 }), w = r.samples.filter(s => s.C >= 5 && s.C <= C1 + 1e-9);
    if (r.collapse) col.push(seed);
    sC.push(fit(w.map(s => s.C), w.map(s => -Math.log(s.T)))); st.push(fit(w.map(s => s.t), w.map(s => s.T ** -0.5)));
    R.push(mean(w.filter(s => s.C >= C1 - third).map(s => s.R)));
  }
  const dC = mean(sC) / perContact(e) - 1, dt = mean(st) / clock(phi, e) - 1;
  res[phi] = { dC, dt, R: mean(R) };
  say(`φ ${phi} e ${e}, 16 seeds: per contact ${mean(sC).toFixed(5)} ± ${sem(sC).toFixed(5)} (pred. ${perContact(e).toFixed(5)}, ${(dC * 100).toFixed(2)}%); clock ${mean(st).toFixed(5)} ± ${sem(st).toFixed(5)} (pred. ${clock(phi, e).toFixed(5)}, ${(dt * 100).toFixed(2)}%); R last third ${mean(R).toFixed(2)}; collapses ${col.length}`);
}
const V = [], verdict = (id, killed, text) => V.push(`${id}: ${killed ? 'KILLED' : 'not killed'}. ${text}`);
{ const q = res[0.05]; verdict('P6', Math.abs(q.dC) >= 0.01 || Math.abs(q.dt) >= 0.015 || q.R >= 1.5, `φ 0.05: per contact ${(q.dC * 100).toFixed(2)}% (within 1%), clock ${(q.dt * 100).toFixed(2)}% (within 1.5%), R ${q.R.toFixed(2)} (below 1.5)`); }
{ const q = res[0.15]; verdict('P7', !(-q.dC > 0.025) || !(-q.dt > 0.052) || !(q.R > 2.3), `φ 0.15: per-contact deficit ${(-q.dC * 100).toFixed(2)}% (more than 2.5%), clock deficit ${(-q.dt * 100).toFixed(2)}% (more than 5.2%), R ${q.R.toFixed(2)} (above 2.3)`); }
{ const r = [0.1, 0.15].map(p => [p, res[p].dt / res[p].dC]); verdict('P8', r.some(([, x]) => !(x >= 1.5)), 'clock deficit over per-contact deficit: ' + r.map(([p, x]) => `φ ${p} ${x.toFixed(2)}`).join(', ') + ' (each at least 1.5)'); }
say(''); V.forEach(v => say(v));
writeFileSync(fileURLToPath(new URL('mrb-run2.txt', import.meta.url)), out.join('\n') + '\n');
