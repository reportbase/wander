// POL run 4 (plans/pol-plan.md): the corner of lateness and tick. Usage: node plans/pol/pol4.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const CS = [50, 100, 200, 400], SUBS = [1, 2, 4, 8, 16], BR = [0, 4, 9];
const res = await p.evaluate(({ CS, SUBS, BR }) => { const P = window.__pool, out = [];
  for (const c of CS) for (const sub of SUBS) { const E = BR.map(i => P.runLate(i, { c, sub, mode: 'carry', stopAtE: true }).E).sort((x, y) => x - y); out.push({ c, sub, E: E[1], all: E }); }
  // the check: run 3's cell (c = 100, SUB = 4) again
  out.check = P.runLate(4, { c: 100, mode: 'carry' }).E; return { out, check: out.check }; }, { CS, SUBS, BR });
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
let bad = 0;
console.log('carrying reader, E = largest distance between the tables 0.05 s after the first contact, median of breaks 0, 4, 9');
console.log('L = lateness at contact in ticks = 0.9·60·SUB/c; predicted: E < 1e-3 when L < 1.5, E > 1e-2 when L > 3');
for (const r of res.out) {
  const L = 0.9 * 60 * r.sub / r.c, band = L < 1.5 ? 'small' : L > 3 ? 'large' : '-';
  const ok = band === 'small' ? r.E < 1e-3 : band === 'large' ? r.E > 1e-2 : true; if (!ok) bad++;
  console.log(`  c ${String(r.c).padStart(3)}  SUB ${String(r.sub).padStart(2)}  L ${L.toFixed(2).padStart(6)}  E ${r.E.toExponential(2)}  (${r.all.map(x => x.toExponential(1)).join(', ')})  ${band}${ok ? '' : '  ✗'}`);
}
console.log(`check, run 3's cell c = 100, SUB = 4, break 4: E ${res.check.toExponential(3)}`);
console.log(`P12: ${bad === 0 ? 'not killed' : 'KILLED'} (${bad} cells outside their band)`);
