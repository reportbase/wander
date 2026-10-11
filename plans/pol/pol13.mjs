// POL run 13 (plans/pol-plan.md): run 12 with the band closed at its outer edge (a mirror), each part of it reading the three
// cells beside it; balls in and out only by the band's keeping, charged to the cells. Otherwise run 12 (its measures and
// predictions renamed). Usage: node plans/pol/pol13.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage(); p.setDefaultTimeout(0);
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool-infinite.html'));
await p.evaluate(() => {
  const I = window.__infinite; I.pause(true);
  const SECONDS = 60, EVERY = 12, TICKS = Math.round(SECONDS / I.TICK), V0 = 7.5, V1 = 37.5, W = 45, BAND = I.BAND;
  const RUN13 = { mode: "mirror", quiet: true, D: I.DIFF_ENSKOG };
  // the referee, as run 11, with each view's own count series kept for the within-view variance
  window.refRun = seed => {
    const gas = I.makeGas(240, seed); for (let k = 0; k < 720; k++) I.refereeStep(gas, I.TICK);
    const warm = I.cloneGas(gas), B = gas.B, N = B.n, nv = 8;
    const s = { c: 0, n: 0, ke: 0, contacts: 0, N, vc: new Float64Array(64), vc2: new Float64Array(64), vn: 0 };
    const counts = new Float64Array(nv * nv);
    for (let k = 1; k <= TICKS; k++) {
      I.refereeStep(gas, I.TICK, () => { s.contacts++; });
      if (k % EVERY) continue;
      counts.fill(0);
      for (let i = 0; i < N; i++) { counts[Math.min(nv - 1, Math.floor(B.y[i] / 30)) * nv + Math.min(nv - 1, Math.floor(B.x[i] / 30))]++; s.ke += 0.5 * (B.vx[i] ** 2 + B.vy[i] ** 2); }
      counts.forEach((c, v) => { s.c += c; s.n++; s.vc[v] += c; s.vc2[v] += c * c; }); s.vn++;
    }
    s.within = [...s.vc].map((m, v) => { const mean = m / s.vn; return (s.vc2[v] / s.vn - mean * mean) / mean; });
    delete s.vc; delete s.vc2; window['warm' + seed] = warm; return s;
  };
  window.multiRun = (seed, oi, oj, closed) => {
    const M = I.multiFromGas(I.cloneGas(window['warm' + seed]), oi, oj, 6, 100 * seed + oi + 7 * oj, RUN13); M.closed = closed;
    const T0 = I.totals(M), B = M.B, s = { c: 0, c2: 0, n: 0, ke: 0, contacts: 0, prof: new Float64Array(23), bandN: 0, bandKE: 0, nb: { sum: 0, n: 0, lo: Infinity, hi: -Infinity }, T0, start: M.B.n };
    const onC = (i, j) => { const x = (B.x[i] + B.x[j]) / 2, y = (B.y[i] + B.y[j]) / 2; if (x >= V0 && x < V1 && y >= V0 && y < V1) s.contacts++; };
    for (let k = 1; k <= TICKS; k++) {
      I.multiStep(M, I.TICK, onC);
      if (k % EVERY) continue;
      let c = 0;
      for (let q = 0; q < B.n; q++) {
        const x = B.x[q], y = B.y[q], d = Math.min(x, W - x, y, W - y), e = 0.5 * (B.vx[q] ** 2 + B.vy[q] ** 2);
        if (x >= V0 && x < V1 && y >= V0 && y < V1) { c++; s.ke += e; }
        if (d >= 0) s.prof[Math.min(22, Math.floor(d))]++;
        if (d >= 0 && d < BAND) { s.bandN++; s.bandKE += e; }
      }
      s.c += c; s.c2 += c * c; s.n++;
      if (!closed) for (const g of M.segs) if (g.leaf.k === 0) { const r = g.leaf.N / g.leaf.A / I.N_DENS; s.nb.sum += r; s.nb.n++; s.nb.lo = Math.min(s.nb.lo, r); s.nb.hi = Math.max(s.nb.hi, r); }
    }
    const mean = s.c / s.n; s.within = (s.c2 / s.n - mean * mean) / mean;
    s.T1 = I.totals(M); s.final = B.n; s.entered = M.entered; s.left = M.left; s.prof = [...s.prof]; return s;
  };
  window.panRun = seed => {
    const M = I.multiFromGas(I.cloneGas(window['warm' + seed]), 13, 13, 6, 900 + seed, RUN13), T0 = I.totals(M), B = M.B;
    for (let k = 0; k < 480; k++) I.multiStep(M, I.TICK);
    for (let st = 0; st < 60; st++) { I.setWindow(M, M.oi + 1, M.oj, 6); for (let k = 0; k < 4; k++) I.multiStep(M, I.TICK); }
    let c = 0, ke = 0, n = 0;
    for (let k = 1; k <= 480; k++) { I.multiStep(M, I.TICK); if (k % EVERY) continue; n++;
      for (let q = 0; q < B.n; q++) { const x = B.x[q], y = B.y[q]; if (x >= V0 && x < V1 && y >= V0 && y < V1) { c++; ke += 0.5 * (B.vx[q] ** 2 + B.vy[q] ** 2); } } }
    for (let st = 0; st < 60; st++) { I.setWindow(M, M.oi - 1, M.oj, 6); for (let k = 0; k < 4; k++) I.multiStep(M, I.TICK); }
    return { T0, T1: I.totals(M), density: c / n / 900, kePer: ke / c };
  };
  window.workRun = () => {
    const ops = o => o.moves + o.pairs + (o.tries || 0) + (o.cells || 0), out = {};
    for (const K of [5, 9]) { const M = I.multiUniform(K, 6, 2 ** (K - 1) - 3, 2 ** (K - 1) - 3, 5, RUN13); for (let k = 0; k < 2400; k++) I.multiStep(M, I.TICK); out['multi' + K] = { perSecond: ops(M.ops) / 10, cells: M.leaves.size, balls: I.totals(M).N }; }
    { const M = I.multiUniform(5, 6, 13, 13, 5, { mode: 'edge', quiet: false, D: I.DIFF }); for (let k = 0; k < 2400; k++) I.multiStep(M, I.TICK); out.edge5 = { perSecond: ops(M.ops) / 10 }; }
    return out;
  };
});
const SEEDS = [1, 2, 3, 4], PLACES = [[0, 0], [13, 13], [26, 5], [5, 20], [19, 27], [9, 3], [22, 16], [2, 12], [15, 24], [28, 28]];
const ref = [], open = [], closed = [], pans = [];
for (const sd of SEEDS) {
  ref.push(await p.evaluate(sd => window.refRun(sd), sd));
  for (const [oi, oj] of PLACES) { open.push(await p.evaluate(a => window.multiRun(...a), [sd, oi, oj, false])); closed.push(await p.evaluate(a => window.multiRun(...a), [sd, oi, oj, true])); }
  pans.push(await p.evaluate(sd => window.panRun(sd), sd));
  process.stderr.write(`state ${sd} done\n`);
}
const work = await p.evaluate(() => window.workRun());
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }

const f3 = x => x.toFixed(3), f4 = x => x.toFixed(4), pc = x => (x >= 0 ? '+' : '') + (100 * x).toFixed(1) + '%';
const sum = (L, k) => L.reduce((z, o) => z + o[k], 0), avg = L => L.reduce((z, x) => z + x, 0) / L.length;
const rN = ref[0].N, rNu = sum(ref, 'contacts') * 2 / (rN * 60 * ref.length), rDens = sum(ref, 'c') / sum(ref, 'n') / 900, rKE = sum(ref, 'ke') / sum(ref, 'c');
const rWithin = avg(ref.flatMap(o => o.within));
console.log(`the referee (as run 11): 4 states of ${rN} balls, 240 a side, wrapped; 60 s each, 64 views of 30 × 30 sampled every 0.05 s`);
console.log(`  view: density ${f4(rDens)}, energy per ball ${f3(rKE)}, contacts per ball per second ${f3(rNu)}; count var/mean within each view ${f3(rWithin)}\n`);
const stat = L => { const m = sum(L, 'c') / sum(L, 'n'); return { dens: m / 900, ke: sum(L, 'ke') / sum(L, 'c'), nu: sum(L, 'contacts') * 2 / (m * 60 * L.length), within: avg(L.map(o => o.within)),
  band: sum(L, 'bandN') / sum(L, 'n') / (45 * 45 - 41 * 41), bandKE: sum(L, 'bandKE') / Math.max(1, sum(L, 'bandN')) }; };
const so = stat(open), sc = stat(closed);
console.log(`the multiscale world, the band closed by a mirror: the window 45 × 45, its middle 30 × 30 the view; 4 states × 10 places, 60 s each`);
for (const [name, s] of [['open', so], ['closed (control)', sc]])
  console.log(`  ${name.padEnd(17)} view: density ${f4(s.dens)} (${pc(s.dens / rDens - 1)}), energy per ball ${f3(s.ke)} (${pc(s.ke / rKE - 1)}), contacts per ball ${f3(s.nu)} (${pc(s.nu / rNu - 1)}), count var/mean within the run ${f3(s.within)} (${pc(s.within / rWithin - 1)})`);
console.log(`  open: the band's density ${f4(so.band)} (${pc(so.band / rDens - 1)}), energy per ball ${f3(so.bandKE)} (${pc(so.bandKE / rKE - 1)}); balls put in ${sum(open, 'entered')}, taken out or left ${sum(open, 'left')}; the window held ${(sum(open, 'start') / open.length).toFixed(0)} at the start, ${(sum(open, 'final') / open.length).toFixed(0)} at the end, on average`);
const prof = Array.from({ length: 23 }, (_, d) => sum(open.map(o => ({ v: o.prof[d] })), 'v') / sum(open, 'n') / ((45 - 2 * d) ** 2 - Math.max(0, 45 - 2 * (d + 1)) ** 2) / rDens);
console.log(`  open, density against the referee's by distance from the window's edge (1-unit bands, edge first; the band is the first two):\n    ${prof.map(x => x.toFixed(3)).join(' ')}`);
const nbS = open.reduce((z, o) => z + o.nb.sum, 0), nbN = open.reduce((z, o) => z + o.nb.n, 0);
console.log(`  level-0 cells beside the window, density over the world's: mean ${f3(nbS / nbN)}, lowest ${f3(Math.min(...open.map(o => o.nb.lo)))}, highest ${f3(Math.max(...open.map(o => o.nb.hi)))}`);
console.log(`  just after a pan, the view's density ${f4(avg(pans.map(o => o.density)))} (${pc(avg(pans.map(o => o.density)) / rDens - 1)}), energy per ball ${f3(avg(pans.map(o => o.kePer)))} (${pc(avg(pans.map(o => o.kePer)) / rKE - 1)})`);
const off = (a, z) => ({ N: Math.abs(a.N - z.N), P: Math.hypot(a.Px - z.Px, a.Py - z.Py), E: Math.abs(a.E - z.E) / a.E });
const worst = L => L.reduce((w, o) => { const d = off(o.T0, o.T1); return { N: Math.max(w.N, d.N), P: Math.max(w.P, d.P), E: Math.max(w.E, d.E) }; }, { N: 0, P: 0, E: 0 });
const wr = worst(open), wp = worst(pans), p28 = [wr, wp].every(w => w.N <= 1e-6 && w.P <= 1e-6 && w.E <= 1e-9);
console.log(`  the books: over the 40 open runs, count off by at most ${wr.N.toExponential(1)}, momentum ${wr.P.toExponential(1)}, energy ${wr.E.toExponential(1)} of itself; over the pans ${wp.N.toExponential(1)}, ${wp.P.toExponential(1)}, ${wp.E.toExponential(1)}`);
const g = work.multi9.perSecond / work.multi5.perSecond - 1;
console.log(`  work per simulated second: 240 a side ${work.multi5.perSecond.toExponential(3)} (${work.multi5.cells} cells), 3,840 a side ${work.multi9.perSecond.toExponential(3)} (${work.multi9.cells} cells), ${pc(g)}; run 11's window (no band) ${work.edge5.perSecond.toExponential(3)}\n`);
console.log(`P28″: ${p28 ? 'not killed' : 'KILLED'}. count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself, over every run and pan`);
const p30 = [so.dens / rDens, so.ke / rKE, so.nu / rNu].every(r => Math.abs(r - 1) <= 0.03);
console.log(`P30″: ${p30 ? 'not killed' : 'KILLED'}. the open view's density ${pc(so.dens / rDens - 1)}, energy per ball ${pc(so.ke / rKE - 1)}, contacts per ball ${pc(so.nu / rNu - 1)} (each within 3%)`);
const r31o = so.within / rWithin, r31c = sc.within / rWithin, p31 = Math.abs(r31o - 1) <= 0.15 && r31c <= 0.75;
console.log(`P31″: ${p31 ? 'not killed' : 'KILLED'}. within-run var/mean: open ${f3(so.within)} (${pc(r31o - 1)}; within 15%), closed ${f3(sc.within)} (${pc(r31c - 1)}; at least 25% lower)`);
console.log(`P32″: ${Math.abs(g) < 0.05 ? 'not killed' : 'KILLED'}. the multiscale work changes by ${pc(g)} for 256 times the balls (less than 5%)`);
const worstBand = Math.max(...prof.slice(2).map(x => Math.abs(x - 1)));
console.log(`P33′: ${worstBand <= 0.05 ? 'not killed' : 'KILLED'}. from 2 units inward, the density is at most ${pc(worstBand)} from the referee's (within 5%)`);
