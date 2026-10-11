// POL run 9 (plans/pol-plan.md): run 8 again with the game's contact exact. Usage: node plans/pol/pol9.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'play-trick.html'));
const res = await p.evaluate(() => {
  const T = window.__trick, R = 0.45, D = Math.PI / 180, LX = 20, LZ = 10;
  let a = 8 >>> 0; const rnd = () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const ball = (n, x, z) => ({ n, x, z, vx: 0, vz: 0, r: R, m: 1, col: '#fff', stripe: false, cue: n === 0, sunk: false });
  const wrap = x => Math.atan2(Math.sin(x), Math.cos(x)), dirOf = v => Math.atan2(v[1], v[0]);
  // a ball's motion just after its first contact as the struck one (b), or as the striker for the white
  const struckDir = (sim, n) => { const c = sim.contacts.find(c => c.a === n || c.b === n); if (!c) return null; return dirOf(c.a === n ? c.va : c.vb); };
  function makeChain() {
    for (let tries = 0; tries < 1000; tries++) {
      const S0 = [-8 + rnd() * 4, -3 + rnd() * 6], psi = (rnd() * 2 - 1) * 0.5;
      const B = [ball(0, ...S0)], plan = []; let S = S0, dir = psi, ok = true;
      for (let k = 1; k <= 3; k++) {
        const s = 1.2 + rnd() * 3.8, phi = (rnd() * 90 - 45) * D;
        const G = [S[0] + s * Math.cos(dir), S[1] + s * Math.sin(dir)], nA = dir + phi, O = [G[0] + 2 * R * Math.cos(nA), G[1] + 2 * R * Math.sin(nA)];
        if (Math.abs(O[0]) > LX / 2 - 1 || Math.abs(O[1]) > LZ / 2 - 1) { ok = false; break; }
        B.push(ball(k, ...O)); plan.push({ s, phi, A: s / (2 * R * Math.cos(phi)) }); S = O; dir = nA;
      }
      if (!ok) continue;
      if (B.some((x, i) => B.some((y, j) => j > i && Math.hypot(x.x - y.x, x.z - y.z) < 2 * R + 0.05))) continue;
      const sim = T.simulate(B, psi, 20), pairs = sim.contacts.map(c => [c.a, c.b].sort().join('-'));
      const firsts = []; for (const q of pairs) if (firsts[firsts.length - 1] !== q) firsts.push(q);
      if (firsts.slice(0, 3).join() !== '0-1,1-2,2-3') continue;
      if (sim.sunk.some(x => x.t < sim.contacts.find(c => [c.a, c.b].sort().join('-') === '2-3').t)) continue;
      return { B, psi, plan };
    }
    return null;
  }
  const chains = [];
  for (let i = 0; i < 60; i++) {
    const ch = makeChain(); if (!ch) break;
    const base = T.simulate(ch.B, ch.psi, 20), out = { plan: ch.plan, e: {}, lin: [] };
    for (const del of [1e-7, 1e-8]) {
      const pert = T.simulate(ch.B, ch.psi + del, 20), e = [del];
      for (let k = 1; k <= 3; k++) { const d0 = struckDir(base, k), d1 = struckDir(pert, k); e.push(d0 == null || d1 == null ? NaN : Math.abs(wrap(d1 - d0))); }
      out.e[del] = e;
    }
    chains.push(out);
  }
  // measured: the game's own layouts, random aims; each ball's direction error at its first contact, by its depth in contacts
  const depthRows = [];
  for (const [name, seeds] of [['scatter', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], ['rack', [1, 2, 3, 4, 5, 6]]]) for (const sd of seeds) {
    const L = name === 'rack' ? T.layouts.rack() : T.layouts.scatter(sd), ang = name === 'rack' ? (sd - 3.5) * 0.4 * D : sd * 0.53, del = 1e-9;
    const base = T.simulate(L.B, ang, 14), pert = T.simulate(L.B, ang + del, 14), depth = { 0: 0 };
    for (const c of base.contacts) {   // a ball's depth: one more than the ball that first struck it
      const [x, y] = [c.a, c.b]; if (depth[x] != null && depth[y] == null) depth[y] = depth[x] + 1; else if (depth[y] != null && depth[x] == null) depth[x] = depth[y] + 1;
    }
    for (const n of Object.keys(depth).map(Number)) {
      if (n === 0) continue; const d0 = struckDir(base, n), d1 = struckDir(pert, n);
      if (d0 == null || d1 == null) continue; const e = Math.abs(wrap(d1 - d0)); if (e > 1e-2) continue;   // past linear: left out
      depthRows.push({ name, depth: depth[n], lv: Math.log2(e / del) });
    }
  }
  // P24: every corrected contact on h + v = 1, over the chains and the layouts
  let worst = 0, n24 = 0, fall = 0;
  const all = [...chains.map((_, i) => null)];
  for (const [name, seeds] of [['scatter', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]], ['rack', [1, 2, 3, 4, 5, 6]]]) for (const sd of seeds) {
    const L = name === 'rack' ? T.layouts.rack() : T.layouts.scatter(sd), ang = name === 'rack' ? (sd - 3.5) * 0.4 * D : sd * 0.53;
    for (const c of T.simulate(L.B, ang, 14).contacts) { n24++; if (c.hvC === c.hv) fall++; else worst = Math.max(worst, Math.abs(c.hvC - 1)); }
  }
  T.setLayout('line'); const combo = T.preview().sunk.map(q => q.n).join(); T.setLayout('rack'); T.aim(0); const f = T.preview().first;
  return { chains, depthRows, p24: { worst, n: n24, fall }, combo, full: f && f.n === 1 && f.overlap > 0.999 };
});
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const L2 = Math.log2, med = a => { const s = [...a].sort((x, y) => x - y), n = s.length; return n ? (n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2) : NaN; };
const C = res.chains;
console.log(`${C.length} chains (white and three, each struck from rest by the one before), power 20, aim turned by 1e-7 and 1e-8`);
let within = 0, total = 0, linOK = 0, linTot = 0; const ratios = [];
for (const ch of C) for (let k = 1; k <= 3; k++) {
  const e7 = ch.e['1e-7'], e8 = ch.e['1e-8'], meas = e7[k] / e7[k - 1], pred = ch.plan[k - 1].A; if (!isFinite(meas)) continue;
  total++; ratios.push(meas / pred); if (Math.abs(meas / pred - 1) <= 0.02) within++;
  const m8 = e8[k] / e8[k - 1]; linTot++; if (Math.abs(m8 / meas - 1) <= 0.01) linOK++;
}
const rs = [...ratios].sort((x, y) => x - y);
console.log(`  one contact: measured/predicted factor, median ${med(ratios).toFixed(4)}, 5%–95% ${rs[Math.floor(0.05 * rs.length)].toFixed(3)}–${rs[Math.floor(0.95 * rs.length)].toFixed(3)}; within 2%: ${within} of ${total}`);
let chOK = 0, chTot = 0; const dl = [];
for (const ch of C) { const e = ch.e['1e-7']; if (!isFinite(e[3])) continue; chTot++; const meas = L2(e[3] / e[0]), pred = ch.plan.reduce((z, q) => z + L2(q.A), 0); dl.push(meas - pred); if (Math.abs(meas - pred) <= 0.05) chOK++; }
console.log(`  the chain: levels lost minus predicted, median ${med(dl).toFixed(3)}, largest ${Math.max(...dl.map(Math.abs)).toFixed(3)}; within 0.05 levels: ${chOK} of ${chTot}`);
console.log(`P22: ${within >= 0.95 * total ? 'not killed' : 'KILLED'}. ${within} of ${total} contacts within 2% of s/(2r cos φ) (95% needed)`);
console.log(`P23: ${chOK >= 0.95 * chTot ? 'not killed' : 'KILLED'}. ${chOK} of ${chTot} chains within 0.05 levels of the sum (95% needed)`);
console.log(`P24: ${res.p24.worst < 1e-9 ? 'not killed' : 'KILLED'}. ${res.p24.n} contacts in the layouts, ${res.p24.fall} set down overlapping (the old push); the rest on h + v = 1 to ${res.p24.worst.toExponential(1)}`);
console.log(`  (linear, as run 8's P21: ${linOK} of ${linTot} factors the same at 1e-8 within 1%; the row of four pots ${res.combo}; the rack's first contact full-ball: ${res.full})`);
console.log(`\nmeasured, the game's layouts (scattered ×12, rack ×6, random aims, power 14): levels of aim error at each ball's first contact, by depth`);
const thr = L2((3.6 * Math.PI / 180) / (0.1 * Math.PI / 180));
for (const name of ['scatter', 'rack']) {
  const byD = {}; for (const r of res.depthRows.filter(r => r.name === name)) (byD[r.depth] = byD[r.depth] || []).push(r.lv);
  let horizon = null; console.log(`  ${name}:`);
  for (const d of Object.keys(byD).map(Number).sort((x, y) => x - y)) { const m = med(byD[d]); console.log(`    depth ${d}: ${String(byD[d].length).padStart(3)} balls, median ${m.toFixed(2)} levels`); if (horizon == null && m > thr) horizon = d; }
  console.log(`    a 0.1° aim error passes 3.6° (${thr.toFixed(2)} levels) at depth ${horizon ?? '> the deepest measured'}`);
}
