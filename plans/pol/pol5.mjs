// POL run 5 (plans/pol-plan.md): level of detail as size; the cost of ignoring smaller balls. Usage: node plans/pol/pol5.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const SEEDS = [1, 2, 3, 4, 5], KS = [null, 1, 2, 3];
const res = await p.evaluate(({ SEEDS, KS }) => { const P = window.__pool, out = {};
  for (const K of KS) out[K == null ? 'inf' : K] = SEEDS.map(sd => P.runField(sd, { K }));
  return out; }, { SEEDS, KS });
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const med = L => { const s = [...L].sort((x, y) => x - y); return s[2]; }, f = x => isFinite(x) ? x.toExponential(2) : 'sunk differs';
console.log(`fields of ${res.inf[0].n} balls (levels 0-3: 4, 12, 36, 64), white struck at 14; errors against the referee at 1 s`);
for (const K of ['inf', 1, 2, 3]) {
  const L = res[K], E = [0, 1, 2, 3].map(k => med(L.map(r => r.E[k]))), sk = L.reduce((z, r) => z + r.skipped, 0), hi = L.reduce((z, r) => z + r.hits, 0);
  console.log(`  K = ${String(K).padEnd(3)}  E by level (median of 5): ${E.map(f).join(', ')}   contact responses skipped ${sk} of ${hi} (${(100 * sk / Math.max(1, hi)).toFixed(1)}%)`);
  console.log(`         per field, level 0: ${L.map(r => f(r.E[0])).join(', ')}`);
}
const p13 = res.inf.every(r => r.E.every(e => e < 1e-9));
console.log(`P13: ${p13 ? 'not killed' : 'KILLED'}. K = inf against the referee: all levels within 1e-9 in all five fields`);
const E0 = K => med(res[K].map(r => r.E[0])), f12 = E0(1) / E0(2), f23 = E0(2) / E0(3);
console.log(`P14: ${f12 >= 4 && f12 <= 16 && f23 >= 4 && f23 <= 16 ? 'not killed' : 'KILLED'}. level-0 error falls by ${f12.toFixed(2)} (K 1 to 2) and ${f23.toFixed(2)} (K 2 to 3); band [4, 16]`);
