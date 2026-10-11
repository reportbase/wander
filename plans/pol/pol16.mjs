// POL run 16 (plans/pol-plan.md): a pressure pulse from 60 units away (a hot disc, warmth doubled), carried to the window by
// the referee (every ball), by run 15's far field (diffusion) and by a fluid far field (Euler with the hard-disc pressure,
// Rusanov's flux). Usage: node plans/pol/pol16.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage(); p.setDefaultTimeout(0);
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool-infinite.html'));
await p.evaluate(() => {
  const I = window.__infinite; I.pause(true);
  const TICKS = 2880, EVERY = 12, L = 240, SRC = [180, 120], RS = 10, V0 = 105, V1 = 135;
  window.stateOf16 = seed => {   // a warmed referee state with the pulse: the balls within 10 of the source twice as warm
    const gas = I.makeGas(L, seed); for (let k = 0; k < 720; k++) I.refereeStep(gas, I.TICK);
    const B = gas.B; let added = 0;
    for (let i = 0; i < B.n; i++) {
      let dx = B.x[i] - SRC[0], dy = B.y[i] - SRC[1]; dx -= L * Math.round(dx / L); dy -= L * Math.round(dy / L);
      if (dx * dx + dy * dy < RS * RS) { const e0 = 0.5 * (B.vx[i] ** 2 + B.vy[i] ** 2); B.vx[i] *= Math.SQRT2; B.vy[i] *= Math.SQRT2; added += e0; }
    }
    window['s16_' + seed] = gas; return added;
  };
  window.refRun16 = seed => {
    const gas = I.cloneGas(window['s16_' + seed]), B = gas.B, ke = [], cnt = [];
    for (let k = 1; k <= TICKS; k++) { I.refereeStep(gas, I.TICK); if (k % EVERY) continue;
      let c = 0, e = 0; for (let i = 0; i < B.n; i++) { const x = B.x[i], y = B.y[i]; if (x >= V0 && x < V1 && y >= V0 && y < V1) { c++; e += 0.5 * (B.vx[i] ** 2 + B.vy[i] ** 2); } }
      ke.push(e / c); cnt.push(c); }
    return { ke, cnt };
  };
  window.multiRun16 = (seed, far) => {
    const M = I.multiFromGas(I.cloneGas(window['s16_' + seed]), 13, 13, 6, 500 + seed, { mode: 'ring', quiet: true, D: I.DIFF_ENSKOG, gamma: 1, far });
    const T0 = I.totals(M), B = M.B, ke = [], cnt = [];
    for (let k = 1; k <= TICKS; k++) { I.multiStep(M, I.TICK); if (k % EVERY) continue;
      let c = 0, e = 0; for (let q = 0; q < B.n; q++) { const x = B.x[q], y = B.y[q]; if (x >= 7.5 && x < 37.5 && y >= 7.5 && y < 37.5) { c++; e += 0.5 * (B.vx[q] ** 2 + B.vy[q] ** 2); } }
      ke.push(e / c); cnt.push(c); }
    const pulseCell = I.leafAt(M, Math.floor(SRC[0] / 7.5), Math.floor(SRC[1] / 7.5));
    return { ke, cnt, T0, T1: I.totals(M), pulseLevel: pulseCell ? pulseCell.k : -1 };
  };
});
const SEEDS = Array.from({ length: 20 }, (_, i) => i + 1), ref = [], dif = [], flu = []; let added = 0, level = null;
for (const sd of SEEDS) {
  added += await p.evaluate(sd => window.stateOf16(sd), sd);
  ref.push(await p.evaluate(sd => window.refRun16(sd), sd));
  dif.push(await p.evaluate(sd => window.multiRun16(sd, 'diffusion'), sd));
  const fr = await p.evaluate(sd => window.multiRun16(sd, 'fluid'), sd); flu.push(fr); level = fr.pulseLevel;
  process.stderr.write(`state ${sd} done\n`);
}
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }

const mean = (runs, key) => runs[0][key].map((_, k) => runs.reduce((z, r) => z + r[key][k], 0) / runs.length);
const curve = runs => { const m = mean(runs, 'ke'), base = m.slice(0, 10).reduce((z, x) => z + x, 0) / 10, bins = [];
  for (let k = 0; k + 5 <= m.length; k += 5) bins.push({ t: (k + 2.5) * 0.05, rise: m.slice(k, k + 5).reduce((z, x) => z + x, 0) / 5 - base });
  const max = Math.max(...bins.map(x => x.rise)), half = bins.find(x => x.rise >= 0.5 * max);
  return { base, bins, max, tHalf: half ? half.t : NaN, tMax: bins.find(x => x.rise === max).t }; };
const cr = curve(ref), cd = curve(dif), cf = curve(flu);
console.log(`a pulse: the balls within 10 of a point 60 from the window's middle twice as warm (on average ${(added / SEEDS.length).toFixed(0)} units of energy added, against the world's ~339,000); 20 warmed states, 12 s`);
console.log(`the multiscale world holds the pulse's place in a level-${level} cell (${7.5 * 2 ** level} units wide)`);
console.log(`the view's mean kinetic energy per ball, less its first 0.5 s (baseline: referee ${cr.base.toFixed(3)}, diffusion ${cd.base.toFixed(3)}, fluid ${cf.base.toFixed(3)}):`);
console.log('    t (s)   referee   diffusion   fluid');
for (let i = 1; i < cr.bins.length; i += 2) console.log(`  ${cr.bins[i].t.toFixed(2).padStart(6)}  ${cr.bins[i].rise.toFixed(3).padStart(8)}  ${cd.bins[i].rise.toFixed(3).padStart(9)}  ${cf.bins[i].rise.toFixed(3).padStart(7)}`);
console.log(`largest rise: referee ${cr.max.toFixed(3)} at ${cr.tMax.toFixed(2)} s, diffusion ${cd.max.toFixed(3)} at ${cd.tMax.toFixed(2)} s, fluid ${cf.max.toFixed(3)} at ${cf.tMax.toFixed(2)} s`);
console.log(`half-maximum arrival: referee ${cr.tHalf.toFixed(2)} s, diffusion ${cd.tHalf.toFixed(2)} s, fluid ${cf.tHalf.toFixed(2)} s`);
const cnt = runs => { const m = mean(runs, 'cnt'); return [0, 60, 120, 180, 239].map(k => m[k].toFixed(1)).join(', '); };
console.log(`the view's count at 0, 3, 6, 9, 12 s: referee ${cnt(ref)}; diffusion ${cnt(dif)}; fluid ${cnt(flu)}`);
const off = r => ({ N: Math.abs(r.T1.N - r.T0.N), P: Math.hypot(r.T1.Px - r.T0.Px, r.T1.Py - r.T0.Py), E: Math.abs(r.T1.E / r.T0.E - 1) });
const wf = flu.reduce((w, r) => { const d = off(r); return { N: Math.max(w.N, d.N), P: Math.max(w.P, d.P), E: Math.max(w.E, d.E) }; }, { N: 0, P: 0, E: 0 });
console.log(`the fluid's books over the 20 runs: count off by at most ${wf.N.toExponential(1)}, momentum ${wf.P.toExponential(1)}, energy ${wf.E.toExponential(1)} of itself\n`);
console.log(`P34: ${cr.tHalf >= 3.6 && cr.tHalf <= 6.1 ? 'not killed' : 'KILLED'}. the referee's half-maximum arrival ${cr.tHalf.toFixed(2)} s (in [3.6, 6.1])`);
console.log(`P35: ${Math.abs(cf.tHalf / cr.tHalf - 1) <= 0.25 ? 'not killed' : 'KILLED'}. the fluid's arrival ${cf.tHalf.toFixed(2)} s against the referee's ${cr.tHalf.toFixed(2)} s (${(100 * (cf.tHalf / cr.tHalf - 1)).toFixed(1)}%; within 25%)`);
console.log(`P36: ${cd.max < 0.25 * cr.max ? 'not killed' : 'KILLED'}. diffusion's largest rise ${cd.max.toFixed(3)} against the referee's ${cr.max.toFixed(3)} (${(100 * cd.max / cr.max).toFixed(0)}%; under 25%)`);
console.log(`P37: ${wf.N <= 1e-6 && wf.P <= 1e-6 && wf.E <= 1e-9 ? 'not killed' : 'KILLED'}. the fluid keeps the books (1e-6, 1e-6, 1e-9)`);
