// POL run 2 (plans/pol-plan.md): cushions and pockets read from inside too. Usage: node plans/pol/pol2.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const res = await p.evaluate(() => { const P = window.__pool, L = [];
  for (const heavy of [true, false]) for (let i = 0; i < 10; i++) L.push(P.run(i, { heavy, walls: 'inside' })); return L; });
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const sum = k => res.reduce((z, r) => z + r[k], 0), f = x => x == null ? 'none' : x.toExponential(2);
console.log(`20 breaks, cushions and pockets read from inside: ${sum('p6checks')} cushion readings, ${sum('p7checks')} pocket readings`);
console.log(`P6: ${sum('p6bad') === 0 ? 'not killed' : 'KILLED'}. cushion: centre within r of the line against the image's h + v > 1 (h = v): ${sum('p6bad')} disagreements`);
console.log(`P7: ${sum('p7bad') === 0 ? 'not killed' : 'KILLED'}. pocket: d < POCK against v > 1: ${sum('p7bad')} disagreements`);
const ok8 = res.every(r => r.firstRail == null || (r.diffAtRail != null && r.diffAtRail < 1e-9));
console.log(`P8: ${ok8 ? 'not killed' : 'KILLED'}. the whole game from inside against the referee:`);
for (const r of res) console.log(`  ${r.heavy ? 'heavy' : 'equal'} break ${r.i}: first cushion at ${r.firstRail == null ? 'none' : r.firstRail.toFixed(3) + ' s'}, differ ${f(r.diffAtRail)} then; past 1e-3 at ${r.diverge == null ? 'never (8 s)' : r.diverge.toFixed(2) + ' s'}; sunk ${r.sunkRef} / ${r.sunkSit}`);
console.log(`  diverged past 1e-3: ${res.filter(r => r.diverge != null).length} of 20`);
