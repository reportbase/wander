// POL run 11 (plans/pol-plan.md): a world of any size held as balls in a window round the reader and as totals in dyadic
// cells beyond, against a referee that computes every ball. Usage: node plans/pol/pol11.mjs
// Run 11's window: balls enter at the edge (mode 'edge'), cells read their flow as is, the plan's diffusion (I.DIFF).
// Since run 12 the engine's fold bug is fixed, so the pans' books (P28) now balance; everything else is run 11's.
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage(); p.setDefaultTimeout(0);
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool-infinite.html'));
await p.evaluate(() => {
  const I = window.__infinite; I.pause(true);
  const SECONDS = 60, EVERY = 12, TICKS = Math.round(SECONDS / I.TICK), V0 = 7.5, V1 = 37.5, W = 45;
  // the referee: every ball of a world 240 a side, wrapped; measured in the 64 views of 30 × 30 that tile it
  window.refRun = seed => {
    const gas = I.makeGas(240, seed); for (let k = 0; k < 720; k++) I.refereeStep(gas, I.TICK);
    const warm = I.cloneGas(gas), L = 240, B = gas.B, N = B.n, nv = 8;
    let E = 0; for (let i = 0; i < N; i++) E += 0.5 * (B.vx[i] ** 2 + B.vy[i] ** 2);
    const s = { c: 0, c2: 0, n: 0, ke: 0, contacts: 0, speeds: [], sigma: Math.sqrt(E / N), N };
    const counts = new Float64Array(nv * nv);
    for (let k = 1; k <= TICKS; k++) {
      I.refereeStep(gas, I.TICK, () => { s.contacts++; });
      if (k % EVERY) continue;
      counts.fill(0);
      for (let i = 0; i < N; i++) { counts[Math.min(nv - 1, Math.floor(B.y[i] / 30)) * nv + Math.min(nv - 1, Math.floor(B.x[i] / 30))]++; s.ke += 0.5 * (B.vx[i] ** 2 + B.vy[i] ** 2); }
      for (const c of counts) { s.c += c; s.c2 += c * c; s.n++; }
      if (k % (EVERY * 20) === 0) for (let i = 0; i < N; i++) s.speeds.push(Math.hypot(B.vx[i], B.vy[i]));
    }
    window['warm' + seed] = warm; return s;
  };
  // the multiscale world, open (or closed, the control), from a warmed referee state, the window at (oi, oj)
  const RUN11 = { mode: 'edge', quiet: false, D: I.DIFF };
  window.multiRun = (seed, oi, oj, closed) => {
    const M = I.multiFromGas(I.cloneGas(window['warm' + seed]), oi, oj, 6, 100 * seed + oi + 7 * oj, RUN11); M.closed = closed;
    const T0 = I.totals(M), B = M.B, s = { c: 0, c2: 0, n: 0, ke: 0, contacts: 0, wc: 0, wc2: 0, prof: new Float64Array(23), nb: { sum: 0, n: 0, lo: Infinity, hi: -Infinity }, T0, start: M.B.n };
    const onC = (i, j) => { const x = (B.x[i] + B.x[j]) / 2, y = (B.y[i] + B.y[j]) / 2; if (x >= V0 && x < V1 && y >= V0 && y < V1) s.contacts++; };
    for (let k = 1; k <= TICKS; k++) {
      I.multiStep(M, I.TICK, onC);
      if (k % EVERY) continue;
      let c = 0;
      for (let q = 0; q < B.n; q++) {
        const x = B.x[q], y = B.y[q];
        if (x >= V0 && x < V1 && y >= V0 && y < V1) { c++; s.ke += 0.5 * (B.vx[q] ** 2 + B.vy[q] ** 2); }
        s.prof[Math.min(22, Math.floor(Math.min(x, W - x, y, W - y)))]++;
      }
      s.c += c; s.c2 += c * c; s.n++; s.wc += B.n; s.wc2 += B.n * B.n;
      if (!closed) for (const g of M.segs) if (g.leaf.k === 0) { const r = g.leaf.N / g.leaf.A / I.N_DENS; s.nb.sum += r; s.nb.n++; s.nb.lo = Math.min(s.nb.lo, r); s.nb.hi = Math.max(s.nb.hi, r); }
    }
    s.T1 = I.totals(M); s.final = B.n; s.entered = M.entered; s.left = M.left; s.prof = [...s.prof]; return s;
  };
  // a pan of ten window widths and back; the view measured for 2 s at the far place, just after its balls were unfolded
  window.panRun = seed => {
    const M = I.multiFromGas(I.cloneGas(window['warm' + seed]), 13, 13, 6, 900 + seed, RUN11), T0 = I.totals(M), B = M.B;
    for (let k = 0; k < 480; k++) I.multiStep(M, I.TICK);
    for (let st = 0; st < 60; st++) { I.setWindow(M, M.oi + 1, M.oj, 6); for (let k = 0; k < 4; k++) I.multiStep(M, I.TICK); }
    let c = 0, ke = 0, n = 0;
    for (let k = 1; k <= 480; k++) { I.multiStep(M, I.TICK); if (k % EVERY) continue; n++;
      for (let q = 0; q < B.n; q++) { const x = B.x[q], y = B.y[q]; if (x >= V0 && x < V1 && y >= V0 && y < V1) { c++; ke += 0.5 * (B.vx[q] ** 2 + B.vy[q] ** 2); } } }
    for (let st = 0; st < 60; st++) { I.setWindow(M, M.oi - 1, M.oj, 6); for (let k = 0; k < 4; k++) I.multiStep(M, I.TICK); }
    return { T0, T1: I.totals(M), density: c / n / 900, kePer: ke / c };
  };
  // the work per simulated second
  window.workRun = () => {
    const ops = o => o.moves + o.pairs + (o.tries || 0) + (o.cells || 0), out = {};
    for (const K of [5, 9]) { const M = I.multiUniform(K, 6, 2 ** (K - 1) - 3, 2 ** (K - 1) - 3, 5, RUN11); for (let k = 0; k < 2400; k++) I.multiStep(M, I.TICK); out['multi' + K] = { perSecond: ops(M.ops) / 10, cells: M.leaves.size, balls: I.totals(M).N }; }
    for (const L of [240, 480]) { const g = I.makeGas(L, 9); for (let k = 0; k < 240; k++) I.refereeStep(g, I.TICK); out['ref' + L] = { perSecond: ops(g.ops), balls: g.B.n }; }
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
const consts = await p.evaluate(() => ({ N_DENS: __infinite.N_DENS, NU: __infinite.NU, NU_ENSKOG: __infinite.NU_ENSKOG }));
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }

const f3 = x => x.toFixed(3), f4 = x => x.toFixed(4), pc = x => (100 * x).toFixed(1) + '%';
const sum = (L, k) => L.reduce((z, o) => z + o[k], 0);
// the referee
const rN = ref[0].N, rT = 60, rNu = sum(ref, 'contacts') * 2 / (rN * rT * ref.length);
const rMean = sum(ref, 'c') / sum(ref, 'n'), rVar = sum(ref, 'c2') / sum(ref, 'n') - rMean ** 2, rDens = rMean / 900, rKE = sum(ref, 'ke') / sum(ref, 'c');
const sig = Math.sqrt(ref.reduce((z, o) => z + o.sigma ** 2, 0) / ref.length), sp = ref.flatMap(o => o.speeds).sort((a, b) => a - b);
let ks = 0; sp.forEach((v, i) => { const F = 1 - Math.exp(-v * v / (2 * sig * sig)); ks = Math.max(ks, Math.abs(F - i / sp.length), Math.abs(F - (i + 1) / sp.length)); });
console.log(`the referee: 4 states of ${rN} balls, 240 a side, wrapped; 60 s each, the 64 views of 30 × 30 sampled every 0.05 s`);
console.log(`  contacts per ball per second ${f3(rNu)} (the plan's 2.432; Enskog with the 2D cross-section, two diameters, ${f3(consts.NU_ENSKOG)})`);
console.log(`  speeds against Rayleigh (σ = ${f3(sig)} from the energy): largest gap ${f4(ks)} over ${sp.length} speeds`);
console.log(`  view: density ${f4(rDens)} (n = ${f4(consts.N_DENS)}), energy per ball ${f3(rKE)} (σ² = ${f3(sig * sig)}), count var/mean ${f3(rVar / rMean)}`);
const p29 = Math.abs(rNu / 2.432 - 1) <= 0.05 && ks < 0.01 && rVar / rMean >= 0.49 && rVar / rMean <= 0.61;
console.log(`P29: ${p29 ? 'not killed' : 'KILLED'}. contacts ${f3(rNu)} against 2.432 (within 5%: ${Math.abs(rNu / 2.432 - 1) <= 0.05}); Rayleigh gap ${f4(ks)} (< 0.01: ${ks < 0.01}); var/mean ${f3(rVar / rMean)} (in [0.49, 0.61]: ${rVar / rMean >= 0.49 && rVar / rMean <= 0.61})\n`);
// the multiscale world
const stat = L => { const m = sum(L, 'c') / sum(L, 'n'); return { dens: m / 900, ke: sum(L, 'ke') / sum(L, 'c'), vm: (sum(L, 'c2') / sum(L, 'n') - m * m) / m, nu: sum(L, 'contacts') * 2 / (m * 60 * L.length),
  wdens: sum(L, 'wc') / sum(L, 'n') / 2025, wvm: (sum(L, 'wc2') / sum(L, 'n') - (sum(L, 'wc') / sum(L, 'n')) ** 2) / (sum(L, 'wc') / sum(L, 'n')) }; };
const so = stat(open), sc = stat(closed);
console.log(`the multiscale world: the window 45 × 45 (6 × 6 level-0 cells) and its middle 30 × 30 the view; 4 states × 10 places, 60 s each`);
for (const [name, s] of [['open', so], ['closed (control)', sc]])
  console.log(`  ${name.padEnd(17)} view: density ${f4(s.dens)} (${pc(s.dens / rDens - 1)}), energy per ball ${f3(s.ke)} (${pc(s.ke / rKE - 1)}), contacts per ball ${f3(s.nu)} (${pc(s.nu / rNu - 1)}), count var/mean ${f3(s.vm)} (${pc(s.vm / (rVar / rMean) - 1)})`);
console.log(`  open, the whole window as the view (no margin): density ${f4(so.wdens)} (${pc(so.wdens / rDens - 1)}), count var/mean ${f3(so.wvm)}`);
const ent = sum(open, 'entered'), lef = sum(open, 'left');
console.log(`  open: balls entered ${ent}, left ${lef} over ${open.length} runs; the window held ${(sum(open, 'start') / open.length).toFixed(0)} balls at the start and ${(sum(open, 'final') / open.length).toFixed(0)} at the end, on average`);
const prof = Array.from({ length: 23 }, (_, d) => sum(open.map(o => ({ v: o.prof[d] })), 'v') / sum(open, 'n') / ((45 - 2 * d) ** 2 - Math.max(0, 45 - 2 * (d + 1)) ** 2) / rDens);
console.log(`  open, density against the referee's by distance from the window's edge (1-unit bands, edge first):\n    ${prof.map(x => x.toFixed(2)).join(' ')}`);
const nbS = open.reduce((z, o) => z + o.nb.sum, 0), nbN = open.reduce((z, o) => z + o.nb.n, 0);
console.log(`  level-0 cells beside the window, density over the world's: mean ${f3(nbS / nbN)}, lowest ${f3(Math.min(...open.map(o => o.nb.lo)))}, highest ${f3(Math.max(...open.map(o => o.nb.hi)))}`);
const p30 = [so.dens / rDens, so.ke / rKE, so.nu / rNu].every(r => Math.abs(r - 1) <= 0.03);
console.log(`P30: ${p30 ? 'not killed' : 'KILLED'}. the open view's density, energy per ball and contacts per ball within 3% of the referee's: ${pc(so.dens / rDens - 1)}, ${pc(so.ke / rKE - 1)}, ${pc(so.nu / rNu - 1)}`);
const r31o = so.vm / (rVar / rMean), r31c = sc.vm / (rVar / rMean), p31 = Math.abs(r31o - 1) <= 0.15 && r31c <= 0.75;
console.log(`P31: ${p31 ? 'not killed' : 'KILLED'}. var/mean open ${f3(so.vm)} (${pc(r31o - 1)} of the referee's; within 15%), closed ${f3(sc.vm)} (${pc(r31c - 1)}; at least 25% lower)\n`);
// the books
const off = (a, z) => ({ N: Math.abs(a.N - z.N), P: Math.hypot(a.Px - z.Px, a.Py - z.Py), E: Math.abs(a.E - z.E) / a.E });
const worst = L => L.reduce((w, o) => { const d = off(o.T0, o.T1); return { N: Math.max(w.N, d.N), P: Math.max(w.P, d.P), E: Math.max(w.E, d.E) }; }, { N: 0, P: 0, E: 0 });
const wr = worst(open), wp = worst(pans), p28 = [wr, wp].every(w => w.N <= 1e-6 && w.P <= 1e-6 && w.E <= 1e-9);
console.log(`the books: over the 40 open runs, count off by at most ${wr.N.toExponential(1)}, momentum ${wr.P.toExponential(1)}, energy ${wr.E.toExponential(1)} of itself`);
console.log(`           over the pans of ten window widths and back: ${wp.N.toExponential(1)}, ${wp.P.toExponential(1)}, ${wp.E.toExponential(1)}`);
console.log(`  just after a pan, the view's density ${f4(pans.reduce((z, o) => z + o.density, 0) / pans.length)} (${pc(pans.reduce((z, o) => z + o.density, 0) / pans.length / rDens - 1)}), energy per ball ${f3(pans.reduce((z, o) => z + o.kePer, 0) / pans.length)}`);
console.log(`P28: ${p28 ? 'not killed' : 'KILLED'}. count within 1e-6, momentum within 1e-6, energy within 1e-9 of itself\n`);
// the work
const g = work.multi9.perSecond / work.multi5.perSecond - 1;
console.log(`the work per simulated second (balls moved, pairs looked at, balls entering tried, cells updated):`);
console.log(`  multiscale, a world 240 a side (${work.multi5.balls.toExponential(3)} balls, ${work.multi5.cells} cells): ${work.multi5.perSecond.toExponential(3)}`);
console.log(`  multiscale, 3,840 a side (${work.multi9.balls.toExponential(3)} balls, ${work.multi9.cells} cells): ${work.multi9.perSecond.toExponential(3)} (${pc(g)})`);
console.log(`  the referee, 240 a side (${work.ref240.balls} balls): ${work.ref240.perSecond.toExponential(3)}; 480 a side (${work.ref480.balls} balls): ${work.ref480.perSecond.toExponential(3)} (×${(work.ref480.perSecond / work.ref240.perSecond).toFixed(2)})`);
console.log(`P32: ${Math.abs(g) < 0.05 ? 'not killed' : 'KILLED'}. the multiscale work changes by ${pc(g)} for 256 times the balls (less than 5%)`);
