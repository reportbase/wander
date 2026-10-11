// POL run 10, after the run (post hoc, not a test): P25's two-look kick against the response, with the rate read as a
// difference of logs, ln(v_now/v_then)/tick, instead of run 10's (v_now − v_then)/(tick·v_now). Usage: node plans/pol/pol10-posthoc.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
await p.goto('file://' + path.join(root, 'pool.html'));
const res = await p.evaluate(() => {
  const P = window.__pool, e = 0.96, TICK = 1 / 240, out = { lin: [], log: [], head: [], obl: [] };
  for (const sd of [1, 2, 3, 4, 5]) {
    const M = new Map();
    const log = (A, B, d, hit, va, vb) => { if (hit) return; let m = M.get(A); if (!m) M.set(A, m = new Map()); let s = m.get(B); if (!s) m.set(B, s = [NaN, NaN, NaN, NaN]); s[0] = s[1]; s[1] = va; s[2] = s[3]; s[3] = vb; };
    const looks = (a, b) => { let s = M.get(a); s = s && s.get(b); if (s) return [s[0], s[1]]; s = M.get(b); s = s && s.get(a); return [s[2], s[3]]; };
    P.runField(sd, { K: Infinity, log, each: (a, b, ra) => { const ia = P.image(a, b), ib = P.image(b, a); if (!(ia.v < 0.75 * ib.v)) return;
      const [v0, v1] = looks(a, b), rho = ia.v / ib.v, sh = (1 + e) * rho ** 3 / (1 + rho ** 3) / ib.v, du = Math.hypot(...ra.du);
      const lin = sh * (v1 - v0) / TICK / v1, lg = sh * Math.log(v1 / v0) / TICK;
      // how oblique: the relative motion's angle to the line of centres (from the told motion; a measure, not the reader's)
      const w = [b.vx - a.vx, b.vz - a.vz], wl = Math.hypot(...w), cos = wl ? -(w[0] * ia.n[0] + w[1] * ia.n[1]) / wl : 1;
      out.lin.push(lin / du); out.log.push(lg / du); (cos > 0.9 ? out.head : out.obl).push(lg / du); } });
  }
  return out;
});
await b.close();
const q = (L, k) => { const s = [...L].sort((x, y) => x - y); return s[Math.floor(k * (s.length - 1))]; };
const row = (name, L) => console.log(`  ${name.padEnd(34)} n ${String(L.length).padStart(3)}  median ${q(L, 0.5).toFixed(4)}  5% ${q(L, 0.05).toFixed(4)}  95% ${q(L, 0.95).toFixed(4)}  within 10% ${(100 * L.filter(x => Math.abs(x - 1) <= 0.1).length / L.length).toFixed(1)}%`);
console.log('the kick read from two looks over the response, five fields, 1 s, nothing ignored (post hoc)');
row('run 10 rate, (v1 − v0)/(tick·v1)', res.lin); row('log rate, ln(v1/v0)/tick', res.log);
row('  log rate, near head-on (cos > 0.9)', res.head); row('  log rate, oblique (cos ≤ 0.9)', res.obl);
