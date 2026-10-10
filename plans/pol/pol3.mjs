// POL run 3 (plans/pol-plan.md): each ball reads the others late. Usage: node plans/pol/pol3.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const CS = [25, 50, 100, 200, 400, 1e9];
const res = await p.evaluate(CS => { const P = window.__pool, out = {};
  for (const mode of ['naive', 'carry']) { out[mode] = {}; for (const c of CS) { out[mode][c] = []; for (let i = 0; i < 10; i++) out[mode][c].push(P.runLate(i, { c, mode })); } }
  return out; }, CS);
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const med = L => { const s = [...L].sort((x, y) => x - y); return (s[4] + s[5]) / 2; };
const E = {}, share = {};
for (const m of ['naive', 'carry']) { E[m] = {}; share[m] = {}; for (const c of CS) {
  E[m][c] = med(res[m][c].map(r => r.E)); const one = res[m][c].reduce((z, r) => z + r.oneSided, 0), both = res[m][c].reduce((z, r) => z + r.both, 0);
  share[m][c] = one / Math.max(1, one + both); } }
const slope = m => { const xs = CS.slice(0, 5).map(Math.log2), ys = CS.slice(0, 5).map(c => Math.log2(E[m][c])), mx = xs.reduce((a, b) => a + b) / 5, my = ys.reduce((a, b) => a + b) / 5;
  return xs.reduce((z, x, k) => z + (x - mx) * (ys[k] - my), 0) / xs.reduce((z, x) => z + (x - mx) ** 2, 0); };
const sn = slope('naive'), sc = slope('carry');
console.log('median over the ten heavy-ball breaks of E(c): the largest distance between the tables 0.05 s after the first contact');
for (const c of CS) console.log(`  c = ${String(c).padEnd(5)} naive ${E.naive[c].toExponential(3)}   carrying ${E.carry[c].toExponential(3)}   one-sided contact judgements: naive ${(100 * share.naive[c]).toFixed(1)}%, carrying ${(100 * share.carry[c]).toFixed(1)}%`);
console.log(`P9: ${sn >= -1.3 && sn <= -0.7 ? 'not killed' : 'KILLED'}. naive slope of log2 E against log2 c: ${sn.toFixed(3)}`);
const p10 = [50, 100, 200, 400].every(c => E.carry[c] <= E.naive[c] / 4);
console.log(`P10: ${p10 ? 'not killed' : 'KILLED'}. carrying at most a quarter of naive at c >= 50: ${[50, 100, 200, 400].map(c => (E.naive[c] / E.carry[c]).toFixed(1) + 'x').join(', ')}; carrying slope (measured) ${sc.toFixed(3)}`);
console.log(`P11: ${E.naive[1e9] < 1e-9 && E.carry[1e9] < 1e-9 ? 'not killed' : 'KILLED'}. at c = 1e9: naive ${E.naive[1e9].toExponential(2)}, carrying ${E.carry[1e9].toExponential(2)}`);
