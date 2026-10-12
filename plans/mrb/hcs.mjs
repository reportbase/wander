// MRB part 1: five hundred smooth inelastic marbles in a periodic cube, no gravity, event-driven. Each pair's next
// contact is the moment its readings reach h + v = 1 (each marble reads the other as v = r_b/d and is told h = r_a/d;
// equal marbles, so the corner h = v = ½), solved exactly as in POL run 9; the queue's clock is the one unsituated thing.
// node plans/mrb/hcs.mjs  → plans/mrb/mrb-run1.txt (and the same on stdout)
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

// ── a seeded generator (mulberry32) and Gaussians ──
function rng(seed) {
  let a = seed >>> 0;
  return () => { a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
}
const gauss = r => { let u; do u = r(); while (u === 0); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * r()); };

// ── the queue: a binary min-heap on time, struct of arrays; stale events (a marble that has since moved on) are
//    skipped when popped and dropped whenever the heap is compacted ──
class Queue {
  constructor(cap) { this.n = 0; this.alloc(cap); }
  alloc(cap) {
    const o = this; o.cap = cap;
    const T = new Float64Array(cap), I = new Int32Array(cap), J = new Int32Array(cap), CI = new Int32Array(cap), CJ = new Int32Array(cap);
    if (o.T) { T.set(o.T.subarray(0, o.n)); I.set(o.I.subarray(0, o.n)); J.set(o.J.subarray(0, o.n)); CI.set(o.CI.subarray(0, o.n)); CJ.set(o.CJ.subarray(0, o.n)); }
    Object.assign(o, { T, I, J, CI, CJ });
  }
  swap(a, b) { for (const A of [this.T, this.I, this.J, this.CI, this.CJ]) { const x = A[a]; A[a] = A[b]; A[b] = x; } }
  up(k) { const T = this.T; while (k > 0) { const p = (k - 1) >> 1; if (T[p] <= T[k]) break; this.swap(p, k); k = p; } }
  down(k) { const T = this.T, n = this.n; for (;;) { let m = k; const l = 2 * k + 1, r = l + 1; if (l < n && T[l] < T[m]) m = l; if (r < n && T[r] < T[m]) m = r; if (m === k) break; this.swap(m, k); k = m; } }
  push(t, i, j, ci, cj) {
    if (this.n === this.cap) this.alloc(this.cap * 2);
    const k = this.n++; this.T[k] = t; this.I[k] = i; this.J[k] = j; this.CI[k] = ci; this.CJ[k] = cj; this.up(k);
  }
  pop(out) {
    out.t = this.T[0]; out.i = this.I[0]; out.j = this.J[0]; out.ci = this.CI[0]; out.cj = this.CJ[0];
    this.n--; if (this.n > 0) { for (const A of [this.T, this.I, this.J, this.CI, this.CJ]) A[0] = A[this.n]; this.down(0); }
  }
  compact(valid) {   // keep the events still valid, then heapify
    let m = 0; for (let k = 0; k < this.n; k++) if (valid(this.I[k], this.J[k], this.CI[k], this.CJ[k])) {
      this.T[m] = this.T[k]; this.I[m] = this.I[k]; this.J[m] = this.J[k]; this.CI[m] = this.CI[k]; this.CJ[m] = this.CJ[k]; m++; }
    this.n = m; for (let k = (m >> 1) - 1; k >= 0; k--) this.down(k);
  }
}

// ── the gas ──
export function makeGas({ N = 500, phi = 0.1, seed = 1 }) {
  const L = Math.cbrt(N * Math.PI / (6 * phi)), M = Math.floor(L), w = L / M;   // cells at least one diameter wide
  if (M < 3) throw new Error('box too small for the cells');
  const r = rng(seed);
  const g = {
    N, L, M, w, phi, e: 1, t: 0, ncoll: 0, collapse: null,
    x: new Float64Array(N), y: new Float64Array(N), z: new Float64Array(N),
    vx: new Float64Array(N), vy: new Float64Array(N), vz: new Float64Array(N), tp: new Float64Array(N),
    cx: new Int32Array(N), cy: new Int32Array(N), cz: new Int32Array(N), cnt: new Int32Array(N),
    head: new Int32Array(M * M * M).fill(-1), nxt: new Int32Array(N).fill(-1), prv: new Int32Array(N).fill(-1),
    last: new Int32Array(N).fill(-1), streak: new Int32Array(N), q: new Queue(1 << 16),
  };
  // 500 of the 512 sites of a simple cubic lattice, at random
  const S = Math.ceil(Math.cbrt(N)), a = L / S, sites = [];
  for (let i = 0; i < S; i++) for (let j = 0; j < S; j++) for (let k = 0; k < S; k++) sites.push([(i + 0.5) * a, (j + 0.5) * a, (k + 0.5) * a]);
  for (let k = sites.length - 1; k > 0; k--) { const m = Math.floor(r() * (k + 1)); [sites[k], sites[m]] = [sites[m], sites[k]]; }
  if (a < 1) throw new Error('lattice too tight');
  let px = 0, py = 0, pz = 0;
  for (let i = 0; i < N; i++) {
    [g.x[i], g.y[i], g.z[i]] = sites[i];
    g.vx[i] = gauss(r); g.vy[i] = gauss(r); g.vz[i] = gauss(r); px += g.vx[i]; py += g.vy[i]; pz += g.vz[i];
  }
  let s2 = 0; for (let i = 0; i < N; i++) { g.vx[i] -= px / N; g.vy[i] -= py / N; g.vz[i] -= pz / N; s2 += g.vx[i] ** 2 + g.vy[i] ** 2 + g.vz[i] ** 2; }
  const f = Math.sqrt(3 * N / s2); for (let i = 0; i < N; i++) { g.vx[i] *= f; g.vy[i] *= f; g.vz[i] *= f; }   // T = 1
  for (let i = 0; i < N; i++) {
    g.cx[i] = Math.min(M - 1, Math.floor(g.x[i] / w)); g.cy[i] = Math.min(M - 1, Math.floor(g.y[i] / w)); g.cz[i] = Math.min(M - 1, Math.floor(g.z[i] / w));
    link(g, i);
  }
  for (let i = 0; i < N; i++) predict(g, i);
  return g;
}

const cellOf = (g, i) => (g.cx[i] * g.M + g.cy[i]) * g.M + g.cz[i];
function link(g, i) { const c = cellOf(g, i), h = g.head[c]; g.nxt[i] = h; g.prv[i] = -1; if (h >= 0) g.prv[h] = i; g.head[c] = i; }
function unlink(g, i) { const c = cellOf(g, i); if (g.prv[i] >= 0) g.nxt[g.prv[i]] = g.nxt[i]; else g.head[c] = g.nxt[i]; if (g.nxt[i] >= 0) g.prv[g.nxt[i]] = g.prv[i]; }
function advance(g, i) { const d = g.t - g.tp[i]; g.x[i] += g.vx[i] * d; g.y[i] += g.vy[i] * d; g.z[i] += g.vz[i] * d; g.tp[i] = g.t; }

// The next moment two marbles' readings reach h + v = 1. Marble a, in its own units (its radius 1), reads b at
// v = 1/d_a and is told h = 1/d_a, so h + v = 1 when d_a = 2, one diameter: |r + u·s| = 1 in the gas's units.
function pairTime(g, i, j) {
  const t = g.t, L = g.L;
  let dx = (g.x[i] + g.vx[i] * (t - g.tp[i])) - (g.x[j] + g.vx[j] * (t - g.tp[j]));
  let dy = (g.y[i] + g.vy[i] * (t - g.tp[i])) - (g.y[j] + g.vy[j] * (t - g.tp[j]));
  let dz = (g.z[i] + g.vz[i] * (t - g.tp[i])) - (g.z[j] + g.vz[j] * (t - g.tp[j]));
  dx -= L * Math.round(dx / L); dy -= L * Math.round(dy / L); dz -= L * Math.round(dz / L);
  const ux = g.vx[i] - g.vx[j], uy = g.vy[i] - g.vy[j], uz = g.vz[i] - g.vz[j];
  const b = dx * ux + dy * uy + dz * uz; if (b >= 0) return Infinity;           // not closing
  const rr = dx * dx + dy * dy + dz * dz, uu = ux * ux + uy * uy + uz * uz;
  if (rr <= 1) return 0;                                                          // h + v ≥ 1 already (rounding): now
  const disc = b * b - uu * (rr - 1); if (disc < 0) return Infinity;              // they pass
  return (rr - 1) / (-b + Math.sqrt(disc));
}
function crossTime(g, i) {
  let best = Infinity, axis = -1;
  const P = [g.x[i], g.y[i], g.z[i]], V = [g.vx[i], g.vy[i], g.vz[i]], C = [g.cx[i], g.cy[i], g.cz[i]];
  for (let k = 0; k < 3; k++) {
    const v = V[k]; if (v === 0) continue;
    const s = v > 0 ? ((C[k] + 1) * g.w - P[k]) / v : (C[k] * g.w - P[k]) / v;
    if (s < best) { best = s; axis = k; }
  }
  return [Math.max(0, best), axis];
}
function predict(g, i) {
  const M = g.M, ci = g.cnt[i];
  advance(g, i);
  for (let a = -1; a <= 1; a++) for (let b = -1; b <= 1; b++) for (let c = -1; c <= 1; c++) {
    const X = (g.cx[i] + a + M) % M, Y = (g.cy[i] + b + M) % M, Z = (g.cz[i] + c + M) % M;
    for (let j = g.head[(X * M + Y) * M + Z]; j >= 0; j = g.nxt[j]) {
      if (j === i) continue;
      const s = pairTime(g, i, j); if (s < Infinity) g.q.push(g.t + s, i, j, ci, g.cnt[j]);
    }
  }
  const [s, axis] = crossTime(g, i); g.q.push(g.t + s, i, -1 - axis, ci, 0);
}

function collide(g, i, j) {
  advance(g, i); advance(g, j);
  const L = g.L;
  let dx = g.x[i] - g.x[j], dy = g.y[i] - g.y[j], dz = g.z[i] - g.z[j];
  dx -= L * Math.round(dx / L); dy -= L * Math.round(dy / L); dz -= L * Math.round(dz / L);
  const d = Math.hypot(dx, dy, dz), nx = dx / d, ny = dy / d, nz = dz / d;
  const b = (g.vx[i] - g.vx[j]) * nx + (g.vy[i] - g.vy[j]) * ny + (g.vz[i] - g.vz[j]) * nz;
  if (b >= 0) return false;
  const k = (1 + g.e) / 2 * b;
  g.vx[i] -= k * nx; g.vy[i] -= k * ny; g.vz[i] -= k * nz; g.vx[j] += k * nx; g.vy[j] += k * ny; g.vz[j] += k * nz;
  for (const [p, o] of [[i, j], [j, i]]) { if (g.last[p] === o) g.streak[p]++; else { g.last[p] = o; g.streak[p] = 1; } }
  if (g.streak[i] >= 100 || g.streak[j] >= 100) g.collapse = { t: g.t, i, j, ncoll: g.ncoll };
  return true;
}
function cross(g, i, axis) {
  advance(g, i); unlink(g, i);
  const M = g.M, w = g.w, P = axis === 0 ? 'x' : axis === 1 ? 'y' : 'z', C = 'c' + P, v = g['v' + P][i];
  if (v > 0) { g[C][i]++; g[P][i] = g[C][i] * w; if (g[C][i] === M) { g[C][i] = 0; g[P][i] = 0; } }
  else { g[P][i] = g[C][i] * w; g[C][i]--; if (g[C][i] < 0) { g[C][i] = M - 1; g[P][i] = g.L; } }
  link(g, i);
}

// run until the contacts reach `ncollTo`, or the collapse guard trips; call `each` between events (cheap check inside)
const ev = { t: 0, i: 0, j: 0, ci: 0, cj: 0 };
export function runTo(g, ncollTo, onColl) {
  const valid = (i, j, ci, cj) => ci === g.cnt[i] && (j < 0 || cj === g.cnt[j]);
  while (g.ncoll < ncollTo && !g.collapse) {
    if (g.q.n > 64 * g.N * 30) g.q.compact(valid);
    g.q.pop(ev);
    const { i, j } = ev;
    if (ev.ci !== g.cnt[i] || (j >= 0 && ev.cj !== g.cnt[j])) continue;
    g.t = ev.t;
    if (j < 0) { cross(g, i, -1 - j); g.cnt[i]++; predict(g, i); continue; }
    if (collide(g, i, j)) { g.ncoll++; if (onColl) onColl(g); }
    g.cnt[i]++; g.cnt[j]++; predict(g, i); predict(g, j);
  }
}

export const temperature = g => { let s = 0; for (let i = 0; i < g.N; i++) s += g.vx[i] ** 2 + g.vy[i] ** 2 + g.vz[i] ** 2; return s / (3 * g.N); };
// R: the six smallest wavevectors' share of the velocity field over an even share (1 with no flow)
export function flowR(g) {
  const k = 2 * Math.PI / g.L; let sum = 0, s2 = 0;
  for (let i = 0; i < g.N; i++) s2 += g.vx[i] ** 2 + g.vy[i] ** 2 + g.vz[i] ** 2;
  for (const ax of ['x', 'y', 'z']) {
    let re = [0, 0, 0], im = [0, 0, 0];
    for (let i = 0; i < g.N; i++) {
      const p = g[ax][i] + g['v' + ax][i] * (g.t - g.tp[i]), c = Math.cos(k * p), s = Math.sin(k * p), v = [g.vx[i], g.vy[i], g.vz[i]];
      for (let m = 0; m < 3; m++) { re[m] += v[m] * c; im[m] -= v[m] * s; }
    }
    sum += 2 * (re[0] ** 2 + re[1] ** 2 + re[2] ** 2 + im[0] ** 2 + im[1] ** 2 + im[2] ** 2);   // +k and −k alike
  }
  return sum / 6 / s2;
}

// ── theory ──
const chiCS = p => (1 - p / 2) / (1 - p) ** 3;
const a2 = e => 16 * (1 - e) * (1 - 2 * e * e) / (81 - 17 * e + 30 * (1 - e) * e * e);
const perContact = e => (1 - e * e) / 3 * (1 + 3 * a2(e) / 16) / (1 - a2(e) / 16);
const clockSlope = (phi, e) => 2 / 3 * Math.sqrt(Math.PI) * (6 * phi / Math.PI) * chiCS(phi) * (1 - e * e) * (1 + 3 * a2(e) / 16);
const enskog = phi => 4 * Math.sqrt(Math.PI) * (6 * phi / Math.PI) * chiCS(phi);
const fit = (X, Y) => { const n = X.length, mx = X.reduce((a, b) => a + b) / n, my = Y.reduce((a, b) => a + b) / n;
  let sxy = 0, sxx = 0; for (let k = 0; k < n; k++) { sxy += (X[k] - mx) * (Y[k] - my); sxx += (X[k] - mx) ** 2; } return sxy / sxx; };

// one run: melt at e = 1 to 20 contacts per marble, then e, read every 0.25 contacts per marble to Cmax
export function oneRun({ phi, e, seed, Cmax }) {
  const g = makeGas({ phi, seed }), N = g.N;
  let t5 = null, c5 = null;
  runTo(g, Math.round(5 * N / 2)); t5 = g.t; c5 = g.ncoll;
  runTo(g, Math.round(20 * N / 2));
  const melt = { rate: 2 * (g.ncoll - c5) / N / (g.t - t5) / Math.sqrt(temperature(g)), T: temperature(g) };
  g.e = e; const t0 = g.t, n0 = g.ncoll, T0 = temperature(g), samples = [];
  const read = () => samples.push({ C: 2 * (g.ncoll - n0) / N, t: g.t - t0, T: temperature(g) / T0, R: flowR(g) });
  read();
  for (let s = 1; s <= Cmax * 4 && !g.collapse; s++) { runTo(g, n0 + Math.round(s * N / 8)); read(); }
  return { melt, samples, collapse: g.collapse && { C: 2 * (g.collapse.ncoll - n0) / N, t: g.collapse.t - t0, i: g.collapse.i, j: g.collapse.j } };
}

function haffFits(samples, e) {
  const C0 = 5, C1 = 5 + 3 * Math.log(100) / (1 - e * e), win = samples.filter(s => s.C >= C0 && s.C <= C1 + 1e-9);
  const third = (C1 - C0) / 3, first = win.filter(s => s.C <= C0 + third), last = win.filter(s => s.C >= C1 - third);
  const sC = fit(win.map(s => s.C), win.map(s => -Math.log(s.T)));
  const st = fit(win.map(s => s.t), win.map(s => s.T ** -0.5)), stA = fit(first.map(s => s.t), first.map(s => s.T ** -0.5)), stB = fit(last.map(s => s.t), last.map(s => s.T ** -0.5));
  return { sC, st, form: stB / stA, reached: win.length ? win[win.length - 1].C : 0, C1 };
}

// ── run 1 ──
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const out = [], say = s => { out.push(s); console.log(s); };
  const seeds = [1, 2, 3, 4], mean = a => a.reduce((x, y) => x + y) / a.length, spread = a => `${Math.min(...a).toFixed(5)}–${Math.max(...a).toFixed(5)}`;
  const conds = [[0.05, 0.9], [0.1, 0.95], [0.1, 0.9], [0.1, 0.8], [0.1, 0.7], [0.15, 0.9]];
  const res = {}, melts = {}, collapses = [], t00 = Date.now();
  say('MRB run 1: 500 smooth inelastic marbles, periodic cube, no gravity; 4 seeds a condition');
  say('per contact: −d ln T/dC over C from 5 to 5 + 3 ln(100)/(1 − e²); clock: d(T^−½)/dt over the same range; form: clock slope last third / first third');
  for (const [phi, e] of conds) {
    const C1 = 5 + 3 * Math.log(100) / (1 - e * e), rs = seeds.map(seed => oneRun({ phi, e, seed, Cmax: Math.ceil(C1) + 1 }));
    const fs = rs.map(r => haffFits(r.samples, e));
    rs.forEach(r => { (melts[phi] = melts[phi] || []).push(r.melt.rate); if (r.collapse) collapses.push({ phi, e, ...r.collapse }); });
    res[`${phi} ${e}`] = { phi, e, sC: mean(fs.map(f => f.sC)), st: mean(fs.map(f => f.st)), form: fs.map(f => f.form), reached: Math.min(...fs.map(f => f.reached)), C1,
      Rmax: Math.max(...rs.flatMap(r => r.samples.filter(s => s.C <= C1).map(s => s.R))) };
    const q = res[`${phi} ${e}`];
    say(`φ ${phi} e ${e}: per contact ${q.sC.toFixed(5)} (${spread(fs.map(f => f.sC))}) predicted ${perContact(e).toFixed(5)}, ${((q.sC / perContact(e) - 1) * 100).toFixed(2)}%;` +
      ` clock ${q.st.toFixed(5)} (${spread(fs.map(f => f.st))}) predicted ${clockSlope(phi, e).toFixed(5)}, ${((q.st / clockSlope(phi, e) - 1) * 100).toFixed(2)}%;` +
      ` form ${q.form.map(x => x.toFixed(3)).join(' ')}; C reached ${q.reached.toFixed(2)} of ${C1.toFixed(2)}; R at most ${q.Rmax.toFixed(2)}`);
  }
  // P4: φ = 0.3, e = 0.95 and 0.5, to C = 60
  const p4 = {};
  for (const e of [0.95, 0.5]) {
    const rs = seeds.map(seed => oneRun({ phi: 0.3, e, seed, Cmax: 60 }));
    rs.forEach(r => { (melts[0.3] = melts[0.3] || []).push(r.melt.rate); if (r.collapse) collapses.push({ phi: 0.3, e, ...r.collapse }); });
    p4[e] = rs.map(r => { const w = r.samples.filter(s => s.C <= 60), Rmax = Math.max(...w.map(s => s.R)), at20 = w.find(s => s.R > 20);
      return { Rmax, C20: at20 ? at20.C : null, reached: w[w.length - 1].C, collapse: r.collapse, Tend: w[w.length - 1].T,
        haff: Math.exp(-perContact(e) * w[w.length - 1].C), traj: w.filter((s, k) => k % 20 === 0).map(s => `${s.C.toFixed(0)}:${s.R.toFixed(1)}`).join(' ') }; });
    for (const [k, r] of p4[e].entries()) say(`φ 0.3 e ${e} seed ${seeds[k]}: R at most ${r.Rmax.toFixed(2)}${r.C20 != null ? `, past 20 at C ${r.C20.toFixed(2)}` : ''}; C reached ${r.reached.toFixed(2)}${r.collapse ? ` (collapse at C ${r.collapse.C.toFixed(2)}, t ${r.collapse.t.toFixed(4)}, marbles ${r.collapse.i} and ${r.collapse.j})` : ''}; T/T0 at the end ${r.Tend.toExponential(3)}, Haff per contact ${r.haff.toExponential(3)}`);
    for (const [k, r] of p4[e].entries()) say(`   R along C (seed ${seeds[k]}): ${r.traj}`);
  }
  say('melt (e = 1, C 5 to 20): contacts per marble per unit time over √T, against Enskog with Carnahan–Starling');
  for (const [phi, a] of Object.entries(melts)) say(`  φ ${phi}: ${mean(a).toFixed(4)} (${spread(a)}) Enskog ${enskog(+phi).toFixed(4)}, ${((mean(a) / enskog(+phi) - 1) * 100).toFixed(2)}%`);

  // verdicts, as the plan wrote them
  const V = [], verdict = (id, killed, text) => V.push(`${id}: ${killed ? 'KILLED' : 'not killed'}. ${text}`);
  { const offs = Object.entries(melts).map(([phi, a]) => [phi, mean(a) / enskog(+phi) - 1]);
    verdict('P0', offs.some(([, d]) => Math.abs(d) >= 0.02), 'melt contact rate against Enskog: ' + offs.map(([p, d]) => `φ ${p} ${(d * 100).toFixed(2)}%`).join(', ') + ' (each within 2%)'); }
  { const offs = Object.values(res).map(q => [q, q.sC / perContact(q.e) - 1]);
    verdict('P1', offs.some(([, d]) => Math.abs(d) >= 0.03), 'per-contact slope: ' + offs.map(([q, d]) => `φ ${q.phi} e ${q.e} ${(d * 100).toFixed(2)}%`).join(', ') + ' (each within 3%)'); }
  { const offs = Object.values(res).map(q => [q, q.st / clockSlope(q.phi, q.e) - 1, Math.max(...q.form.map(f => Math.abs(f - 1)))]);
    verdict('P2', offs.some(([, d, f]) => Math.abs(d) >= 0.03 || f >= 0.05), 'clock slope and form: ' + offs.map(([q, d, f]) => `φ ${q.phi} e ${q.e} ${(d * 100).toFixed(2)}%, form off ≤ ${(f * 100).toFixed(1)}%`).join('; ') + ' (slope within 3%, form within 5%)'); }
  { const s = [0.05, 0.1, 0.15].map(p => res[`${p} 0.9`]), spreadC = Math.max(...s.map(q => q.sC)) / Math.min(...s.map(q => q.sC)) - 1;
    const ratio = s[2].st / s[0].st, want = (0.28648 * 1.50621) / (0.09549 * 1.13719), want2 = clockSlope(0.15, 0.9) / clockSlope(0.05, 0.9);
    verdict('P3', spreadC >= 0.03 || Math.abs(ratio / want2 - 1) >= 0.05, `per-contact slopes at φ 0.05, 0.1, 0.15 spread ${(spreadC * 100).toFixed(2)}% (within 3%); clock ratio 0.15/0.05 ${ratio.toFixed(3)} against n·χ's ${want2.toFixed(3)} (${(want).toFixed(3)} by the rounded table), ${((ratio / want2 - 1) * 100).toFixed(2)}% (within 5%)`); }
  { const hi = p4[0.95], lo = p4[0.5], hiMax = Math.max(...hi.map(r => r.Rmax));
    const loPass = lo.filter(r => r.Rmax > 20), loUntested = lo.filter(r => r.Rmax <= 20 && r.collapse && r.reached < 60), loFail = lo.filter(r => r.Rmax <= 20 && !(r.collapse && r.reached < 60));
    verdict('P4', hiMax >= 4 || loFail.length > 0, `φ 0.3: e 0.95 R at most ${hiMax.toFixed(2)} (below 4); e 0.5 R past 20 before C 60 in ${loPass.length} of 4 seeds, collapsed first in ${loUntested.length} (not tested), short of 20 uncollapsed in ${loFail.length}`); }
  { const bad = collapses.filter(c => !(c.phi === 0.3 && c.e === 0.5));
    verdict('P5', bad.length > 0, `collapse guard tripped in ${bad.length} of the 28 predicted runs` + (collapses.length - bad.length ? `; the e 0.5 runs (not predicted): ${collapses.length - bad.length} of 4 collapsed` : '; the e 0.5 runs (not predicted): none collapsed')); }
  say(''); V.forEach(v => say(v));
  say(`(${((Date.now() - t00) / 1000).toFixed(0)} s)`);
  writeFileSync(fileURLToPath(new URL('mrb-run1.txt', import.meta.url)), out.join('\n') + '\n');
}
