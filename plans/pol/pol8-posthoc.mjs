// POL run 8, after the run (post hoc, not a prediction): does the fixed-tick contact explain P19 and P20? Usage: node plans/pol/pol8-posthoc.mjs
import { chromium } from 'playwright';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://' + new URL('../../play-trick.html', import.meta.url).pathname);
const out = await p.evaluate(() => {
  const T = window.__trick, R = 0.45, D = Math.PI / 180, LX = 20, LZ = 10;
  let a = 8 >>> 0; const rnd = () => { a = (a + 0x6D2B79F5) >>> 0; let t = a; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const ball = (n, x, z) => ({ n, x, z, vx: 0, vz: 0, r: R, m: 1, col: '#fff', stripe: false, cue: n === 0, sunk: false });
  const wrap = x => Math.atan2(Math.sin(x), Math.cos(x)), dirOf = v => Math.atan2(v[1], v[0]);
  const struck = (sim, n) => sim.contacts.find(c => c.a === n || c.b === n);
  const rows = [];
  let made = 0;
  for (let tries = 0; tries < 20000 && made < 60; tries++) {   // the same chains, in the same order, as pol8.mjs
    const S0 = [-8 + rnd() * 4, -3 + rnd() * 6], psi = (rnd() * 2 - 1) * 0.5;
    const B = [ball(0, ...S0)], plan = []; let S = S0, dir = psi, ok = true;
    for (let k = 1; k <= 3; k++) {
      const s = 1.2 + rnd() * 3.8, phi = (rnd() * 90 - 45) * D;
      const G = [S[0] + s * Math.cos(dir), S[1] + s * Math.sin(dir)], nA = dir + phi, O = [G[0] + 2 * R * Math.cos(nA), G[1] + 2 * R * Math.sin(nA)];
      if (Math.abs(O[0]) > LX / 2 - 1 || Math.abs(O[1]) > LZ / 2 - 1) { ok = false; break; }
      B.push(ball(k, ...O)); plan.push({ s, phi }); S = O; dir = nA;
    }
    if (!ok) continue;
    if (B.some((x, i) => B.some((y, j) => j > i && Math.hypot(x.x - y.x, x.z - y.z) < 2 * R + 0.05))) continue;
    const base = T.simulate(B, psi, 20), pairs = base.contacts.map(c => [c.a, c.b].sort().join('-'));
    const firsts = []; for (const q of pairs) if (firsts[firsts.length - 1] !== q) firsts.push(q);
    if (firsts.slice(0, 3).join() !== '0-1,1-2,2-3') continue;
    if (base.sunk.some(x => x.t < base.contacts.find(c => [c.a, c.b].sort().join('-') === '2-3').t)) continue;
    made++;
    const pert = T.simulate(B, psi + 1e-7, 20);
    let ePrev = 1e-7, uPrev = psi;
    for (let k = 1; k <= 3; k++) {
      const c = struck(base, k), O = [B[k].x, B[k].z], Sx = [B[k - 1].x, B[k - 1].z];
      const cx = [c.x - O[0], c.z - O[1]], lc = Math.hypot(...cx), rho = lc + R, P = [O[0] + cx[0] * rho / lc, O[1] + cx[1] * rho / lc];
      const Dd = Math.hypot(P[0] - Sx[0], P[1] - Sx[1]), n = dirOf([O[0] - P[0], O[1] - P[1]]), phiE = wrap(n - uPrev);
      const e = Math.abs(wrap(dirOf(struck(pert, k).vb) - dirOf(c.vb))), meas = e / ePrev;
      rows.push({ meas, exact: plan[k - 1].s / (2 * R * Math.cos(plan[k - 1].phi)), engine: Dd * Math.cos(phiE) / rho, phi: plan[k - 1].phi / D, pen: 2 * R - rho });
      ePrev = e; uPrev = dirOf(c.vb);
    }
  }
  return rows;
});
await b.close();
const med = a => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
const r1 = out.map(r => r.meas / r.exact), r2 = out.map(r => r.meas / r.engine);
console.log(`${out.length} contacts. measured/exact: median ${med(r1).toFixed(4)}, within 15% ${r1.filter(x => Math.abs(x - 1) <= 0.15).length}`);
console.log(`measured/engine (D cos φ'/ρ, the contact as detected): median ${med(r2).toFixed(6)}, within 1% ${r2.filter(x => Math.abs(x - 1) <= 0.01).length}, within 15% ${r2.filter(x => Math.abs(x - 1) <= 0.15).length}`);
console.log(`overlap at detection: median ${med(out.map(r => r.pen)).toFixed(3)}, largest ${Math.max(...out.map(r => r.pen)).toFixed(3)} (2r = 0.9)`);
const big = out.filter(r => Math.abs(r.phi) > 30), small = out.filter(r => Math.abs(r.phi) < 15);
console.log(`measured/exact at |φ| < 15°: median ${med(small.map(r => r.meas / r.exact)).toFixed(3)} (${small.length}); at |φ| > 30°: ${med(big.map(r => r.meas / r.exact)).toFixed(3)} (${big.length}), cos² 30°–45° = 0.75–0.5`);
