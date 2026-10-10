// POL run 7 (plans/pol-plan.md): the cost of ignoring smaller balls, per contact. Usage: node plans/pol/pol7.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const SEEDS = [1, 2, 3, 4, 5];
const res = await p.evaluate(({ SEEDS }) => { const P = window.__pool, e = 0.96;
  // P15: one contact through respond, head-on, closing speed 1 (an amount), the larger ball at rest
  const one = [1, 2, 3].map(j => { const ra = P.R0, rb = P.R0 / 2 ** j, d = ra + rb;
    const r = P.respond({ vx: 0, vz: 0, r: ra }, { n: [1, 0], v: rb / d }, { n: [-1, 0], v: ra / d }, [-1 / rb, 0]);
    return { j, du: Math.hypot(...r.du) * ra, exact: (1 + e) / (1 + 8 ** j) }; });
  const field = SEEDS.map(sd => P.runField(sd, { seconds: 3, contacts: true }));
  return { one, field: field.map(r => ({ seed: r.seed, contacts: r.contacts })) }; }, { SEEDS });
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const f = x => x.toExponential(3), med = L => { const s = [...L].sort((x, y) => x - y), n = s.length; return n ? (n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2) : NaN; };
const band = (x, lo, hi) => x >= lo && x <= hi;

console.log('P15, one contact, closing speed 1, the larger ball at rest:');
for (const o of res.one) console.log(`  j = ${o.j}: |du| = ${f(o.du)}  (1+e)/(1+8^j) = ${f(o.exact)}`);
const r12 = res.one[0].du / res.one[1].du, r23 = res.one[1].du / res.one[2].du;
const p15 = Math.abs(r12 - 65 / 9) < 1e-9 && Math.abs(r23 - 513 / 65) < 1e-9;
console.log(`P15: ${p15 ? 'not killed' : 'KILLED'}. ratios ${r12.toFixed(12)} (65/9 = ${(65 / 9).toFixed(12)}), ${r23.toFixed(12)} (513/65 = ${(513 / 65).toFixed(12)})`);

const all = res.field.flatMap(r => r.contacts.map(c => ({ ...c, seed: r.seed })));
console.log('\nlevel-0 contacts with smaller balls, true game (nothing ignored), five fields, 3 s:');
const W = {}, U = {};
for (const j of [1, 2, 3]) { const L = all.filter(c => c.j === j); W[j] = med(L.map(c => c.w)); U[j] = med(L.map(c => Math.hypot(...c.du)));
  const n1 = L.filter(c => c.t <= 1).length;
  console.log(`  j = ${j}: ${String(L.length).padStart(4)} contacts (${n1} before 1 s); median closing speed ${W[j].toFixed(3)}, median |du| ${f(U[j])}, du/w ${f(U[j] / W[j])}`); }
const few = [1, 2, 3].some(j => all.filter(c => c.j === j).length < 10);
const w12 = W[2] / W[1], w23 = W[3] / W[2], u12 = U[1] / U[2], u23 = U[2] / U[3];
console.log(`P16: ${few ? 'UNDECIDED (fewer than 10 contacts)' : band(w12, 1.4, 2.5) && band(w23, 1.4, 2.5) ? 'not killed' : 'KILLED'}. closing speed rises by ${w12.toFixed(2)} (j 1 to 2) and ${w23.toFixed(2)} (j 2 to 3); band [1.4, 2.5]`);
console.log(`P17: ${few ? 'UNDECIDED (fewer than 10 contacts)' : band(u12, 3.2, 5.7) && band(u23, 3.2, 5.7) ? 'not killed' : 'KILLED'}. per-contact |du| falls by ${u12.toFixed(2)} (j 1 to 2) and ${u23.toFixed(2)} (j 2 to 3); band [3.2, 5.7]`);

// P18: first-order drift by 1 s from the contacts a level-0 ball would skip at K, as run 6's E_K (largest over level-0 balls, median over fields)
const D = K => med(res.field.map(r => { const by = {};
  for (const c of r.contacts) if (c.t <= 1 && c.j >= K) { const s = by[c.i] || (by[c.i] = [0, 0]); s[0] += c.du[0] * (1 - c.t); s[1] += c.du[1] * (1 - c.t); }
  return Math.max(0, ...Object.values(by).map(s => Math.hypot(...s))); }));
const D1 = D(1), D2 = D(2), D3 = D(3), E6 = { 1: 2.32, 2: 0.609, 3: 0.144 };
console.log(`\nfirst-order drift by 1 s (median of the five fields' largest): D1 ${f(D1)}, D2 ${f(D2)}, D3 ${f(D3)}`);
console.log(`  run 6's E at 1 s: ${E6[1]}, ${E6[2]}, ${E6[3]}; the chaos's gain E/D: ${(E6[1] / D1).toFixed(2)}, ${(E6[2] / D2).toFixed(2)}, ${(E6[3] / D3).toFixed(2)}`);
const d12 = D1 / D2, d23 = D2 / D3;
console.log(`P18: ${band(d12, 2.54, 5.72) && band(d23, 2.82, 6.35) ? 'not killed' : 'KILLED'}. D falls by ${d12.toFixed(2)} (K 1 to 2; band [2.54, 5.72]) and ${d23.toFixed(2)} (K 2 to 3; band [2.82, 6.35])`);
