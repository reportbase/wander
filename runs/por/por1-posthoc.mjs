// POR run 1, after the run (post hoc, not a test): where P3's decisions differ, and how far the field's readings part at k = 7.
import { loadPool } from './loadpool.mjs'; import fs from 'fs';
const out = []; const say = s => { out.push(s); console.log(s); };
const P = loadPool(1), vc = r => r / (1 + r), vStar = K => Math.sqrt(vc(2 ** -K) * vc(2 ** -(K - 1)));
for (const K of [1, 2]) {
  const vs = vStar(K), dif = [], all = [];
  const rule = (A, B, ia, ib) => { const s = (B.lv || 0) - (A.lv || 0) >= K, a = ia.v <= vs, L = Math.log2(ia.v + ib.v);
    all.push(L); if (s !== a) dif.push({ L, s, a, la: A.lv || 0, lb: B.lv || 0, rho: ia.v / ib.v }); return s; };
  for (let s = 1; s <= 5; s++) P.runField(s, { K: rule, seconds: 1 });
  const q = (a, p) => { const b = [...a].sort((x, y) => x - y); return b[Math.floor(p * (b.length - 1))]; };
  say(`K = ${K}: ${dif.length} differing of ${all.length}; log2(h + v) at all pushing responses: median ${q(all, .5).toFixed(4)}, 90% ${q(all, .9).toFixed(4)}, max ${q(all, 1).toFixed(4)}`);
  const L = dif.map(d => d.L); if (L.length) say(`  at the differing ones: min ${q(L, 0).toFixed(4)}, median ${q(L, .5).toFixed(4)}; size said skip / address said keep ${dif.filter(d => d.s && !d.a).length}, the other way ${dif.filter(d => !d.s && d.a).length}; levels (reader, other) ${[...new Set(dif.map(d => d.la + '>' + d.lb))].join(' ')}`);
}
// the field's readings at k = 7 against k = 1, by time
const base = [], P7 = loadPool(7), sev = [];
for (const [PP, arr] of [[P, base], [P7, sev]]) { let t = 0; PP.runField(1, { seconds: 1, log: (A, B, d, hit, va, vb) => { if (!hit) arr.push(va); } }); }
const n = base.length, step = Math.floor(n / 8); let line = 'field seed 1, k = 7 against k = 1, largest |Δv| by eighths of the second:';
for (let e = 0; e < 8; e++) { let m = 0; for (let q = e * step; q < (e + 1) * step; q++) m = Math.max(m, Math.abs(base[q] - sev[q])); line += ' ' + m.toExponential(1); }
say(line);
fs.writeFileSync('runs/por/por-run1-posthoc.txt', out.join('\n') + '\n');
