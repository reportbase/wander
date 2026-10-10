// POL run 1 (plans/pol-plan.md): the ten breaks, both tables in lockstep, through pool.html's hook.
// Usage: node plans/pol/pol.mjs   (from the repository root)
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const res = await p.evaluate(() => {
  const P = window.__pool, heavy = [], equal = [];
  for (let i = 0; i < 10; i++) { heavy.push(P.run(i)); equal.push(P.run(i, { heavy: false })); }
  return { heavy, equal };
});
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const H = res.heavy, E = res.equal, all = [...H, ...E], f = x => x == null ? 'never' : x.toExponential(2);
const p1bad = all.reduce((z, r) => z + r.p1bad, 0), p1near = all.reduce((z, r) => z + r.p1near, 0), pairs = all.reduce((z, r) => z + r.pairs, 0);
const p2bad = all.reduce((z, r) => z + r.p2bad, 0), contacts = all.reduce((z, r) => z + r.contacts, 0);
const p3eq = E.reduce((z, r) => z + r.p3wrong, 0), p3hv = H.map(r => r.p3wrong);
const p4first = H.every(r => r.diffAtFirst != null && r.diffAtFirst < 1e-9), p4half = H.every(r => r.diffHalf < 1e-6);
const maxL = Math.max(...all.map(r => r.maxLevelEq)), medOk = H.every(r => r.rackMedian >= 1 && r.rackMedian <= 3);
console.log(`${pairs} pair-substeps over 20 breaks (10 with the heavy ball, 10 all equal); ${contacts} contacts`);
console.log(`P1: ${p1bad === 0 ? 'not killed' : 'KILLED'}. d < r_a + r_b against h + v > 1: ${p1bad} disagreements past 1e-12 (${p1near} within 1e-12 of the line)`);
console.log(`P2: ${p2bad === 0 ? 'not killed' : 'KILLED'}. contacts off the corner (equal) or off the ray 4/3 (heavy): ${p2bad}`);
console.log(`P3: ${p3eq === 0 && p3hv.every(x => x > 0) ? 'not killed' : 'KILLED'}. one reading alone (v >= 1/2) against touching: all equal ${p3eq} wrong; with the heavy ball, per break ${p3hv.join(', ')}`);
console.log(`P4: ${p4first && p4half ? 'not killed' : 'KILLED'}. inside against the referee:`);
for (const r of H) console.log(`  break ${r.i}: first contact at ${r.firstContact?.toFixed(3)} s, differ ${f(r.diffAtFirst)} then; most in the first 0.5 s ${f(r.diffHalf)}; past 1e-3 at ${r.diverge == null ? 'never (8 s)' : r.diverge.toFixed(2) + ' s'}`);
for (const r of E) console.log(`  all equal, break ${r.i}: differ ${f(r.diffAtFirst)} at first contact; first 0.5 s ${f(r.diffHalf)}; past 1e-3 at ${r.diverge == null ? 'never (8 s)' : r.diverge.toFixed(2) + ' s'}`);
console.log(`P5: ${maxL < 4.63 && medOk ? 'not killed' : 'KILLED'}. most levels from touching (equal balls) ${maxL.toFixed(3)} (bound 4.63); rack medians ${H.map(r => r.rackMedian.toFixed(2)).join(', ')}`);
