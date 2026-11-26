// PEB run 4, post hoc 2 (plans/peb-plan.md): do the contacts' stick/slip choices (Math.min in the ball and rail grips)
// change inside the pieces with no change of phase order? node runs/peb/peb4-posthoc2.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs';
let html = fs.readFileSync('runs/peb/play-trick-event.html', 'utf8');
const sub = (a, b) => { if (html.split(a).length !== 2) throw new Error('anchor: ' + a.slice(0, 60)); html = html.replace(a, b); };
sub('J = Math.min((muB ?? gripOf(ss)) * Jn, ss / (k * im)),', 'J = (window.__br.push((muB ?? gripOf(ss)) * Jn < ss / (k * im) ? "b" : "B"), Math.min((muB ?? gripOf(ss)) * Jn, ss / (k * im))),');
sub('if (ss > 1e-12) { const Jt = Math.min(MU_C * Jn, 2 / 7 * ss),', 'if (ss > 1e-12) { window.__br.push(MU_C * Jn < 2 / 7 * ss ? "r" : "R"); const Jt = Math.min(MU_C * Jn, 2 / 7 * ss),');
const srv = http.createServer((q, r) => { r.writeHead(200, { 'content-type': 'text/html' }); r.end(html); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage(); p.on('pageerror', e => console.log('page error', e.message));
await p.goto(`http://localhost:${srv.address().port}/`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
const cases = [['cut', 0.411481, 0.686901], ['cut', 5.596285, 5.934599], ['cut', 5.997167, 6.083866], ['tworail', 0.210803, 0.233102], ['tworail', 0.714453, 0.996790], ['tworail', 2.242385, 2.770406], ['tworail', 2.841709, 2.949500], ['tworail', 3.577584, 4.121342]];
const r = await p.evaluate((cases) => {
  const T = window.__trick, out = [];
  for (const [name, a0, a1] of cases) {
    const B = name === 'cut' ? [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)] : (T.setChallenge('tworail'), T.ballsNow().map(b => ({ ...b })));
    const obj = B.find(b => !b.cue).n;
    const run = a => { window.__br = []; const s = T.simulateEvent(B, [Math.cos(a), Math.sin(a)], 14, null, 0); s.br = window.__br.join(''); return s; };
    const outc = s => { const c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj); return [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z]; };
    const errs = (lo, hi) => { const mid = (lo + hi) / 2, half = (hi - lo) / 2, test = [];
      for (let q = 0; q < 200; q++) { const a = lo + (hi - lo) * (q + 0.5) / 200; test.push([(a - mid) / half, outc(run(a))]); }
      for (const K of [6, 8, 12, 16, 24, 32, 48, 64, 96, 128]) { const z = [], w = [], f = [];
        for (let k = 0; k < K; k++) { const th = (k + 0.5) * Math.PI / K; z.push(Math.cos(th)); w.push((k % 2 ? -1 : 1) * Math.sin(th)); f.push(outc(run(mid + half * Math.cos(th)))); }
        let err = 0; for (const [y, tr] of test) { let den = 0; const num = [0, 0, 0, 0]; for (let k = 0; k < K; k++) { const q = w[k] / (y - z[k]); den += q; for (let c = 0; c < 4; c++) num[c] += q * f[k][c]; } for (let c = 0; c < 4; c++) err = Math.max(err, Math.abs(num[c] / den - tr[c])); }
        if (err <= 1e-6) return K; }
      return null; };
    const lo0 = a0 + 1e-10, hi0 = a1 - 1e-10, N = 2001, A = [], F = [];
    for (let q = 0; q < N; q++) { const a = lo0 + (hi0 - lo0) * q / (N - 1); A.push(a); F.push(run(a).br); }
    const edges = [lo0];
    for (let q = 0; q < N - 1; q++) if (F[q] !== F[q + 1]) { let lo = A[q], hi = A[q + 1]; const f0 = F[q]; for (let it = 0; it < 60 && hi - lo > 1e-12; it++) { const m = (lo + hi) / 2; if (run(m).br === f0) lo = m; else hi = m; } edges.push(lo, hi); }
    edges.push(hi0);
    const subs = []; for (let k = 0; k < edges.length; k += 2) { const lo = edges[k], hi = edges[k + 1]; subs.push(hi - lo < 1e-6 ? 'narrow' : (errs(lo + 1e-12, hi - 1e-12) ?? 'not held')); }
    out.push({ name, a0, a1, patterns: [...new Set(F)], changes: (edges.length - 2) / 2, subs });
  }
  return out;
}, cases);
const L = r.map(x => `${x.name} ${x.a0}..${x.a1}: stick/slip patterns ${x.patterns.join(' | ')}; changes ${x.changes}; sub-pieces ${x.subs.join(', ')}`);
console.log(L.join('\n')); fs.writeFileSync('runs/peb/peb4-posthoc2.txt', L.join('\n') + '\n');
await b.close(); srv.close();
