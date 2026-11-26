// PEB run 5, post hoc (plans/peb-plan.md): for each piece not held, the bridge's error against K and where the second
// differences of the rest positions stand highest (a kink not recorded, or a smooth piece needing more leaves).
// node runs/peb/peb5-posthoc.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event5.html`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
const cases = [];
for (const name of ['cut', 'tworail']) { const m = JSON.parse(fs.readFileSync(`runs/peb/peb5-map-${name}.json`, 'utf8')); for (const x of m.pieces) if ((x.gl || x.gr ? x.Kb : x.K) === null) cases.push([name, x.e0, x.e1, !!(x.gl || x.gr)]); }
const r = await p.evaluate((cases) => {
  const T = window.__trick, out = [];
  for (const [name, a0, a1, rc] of cases) {
    const B = name === 'cut' ? [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)] : (T.setChallenge('tworail'), T.ballsNow().map(b => ({ ...b })));
    const obj = B.find(b => !b.cue).n;
    const run = a => T.simulateEvent(B, [Math.cos(a), Math.sin(a)], 14, null, 0);
    const outc = s => { const c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj); return [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z]; };
    const lo = a0 + 1e-10, hi = a1 - 1e-10, mid = (lo + hi) / 2, half = (hi - lo) / 2, test = [];
    for (let q = 0; q < 200; q++) { const a = lo + (hi - lo) * (q + 0.5) / 200; test.push([(a - mid) / half, outc(run(a))]); }
    const errs = [];
    for (const K of [6, 12, 24, 48, 96, 128, 256]) { const z = [], w = [], f = [];
      for (let k = 0; k < K; k++) { const th = (k + 0.5) * Math.PI / K; z.push(Math.cos(th)); w.push((k % 2 ? -1 : 1) * Math.sin(th)); f.push(outc(run(mid + half * Math.cos(th)))); }
      let err = 0; for (const [y, tr] of test) { let den = 0; const num = [0, 0, 0, 0]; for (let k = 0; k < K; k++) { const q = w[k] / (y - z[k]); den += q; for (let c = 0; c < 4; c++) num[c] += q * f[k][c]; } for (let c = 0; c < 4; c++) err = Math.max(err, Math.abs(num[c] / den - tr[c])); }
      errs.push(err); }
    const N = 4001, F = []; for (let q = 0; q < N; q++) F.push(outc(run(lo + (hi - lo) * q / (N - 1))));
    const d2 = []; for (let q = 1; q < N - 1; q++) d2.push(Math.max(...F[q].map((v, c) => Math.abs(F[q + 1][c] - 2 * v + F[q - 1][c]))));
    const s = [...d2].sort((x, y) => x - y), med = s[s.length >> 1]; let qm = 0; d2.forEach((v, q) => { if (v > d2[qm]) qm = q; });
    const at = lo + (hi - lo) * (qm + 1) / (N - 1), A = run(at - (hi - lo) / N), Bv = run(at + (hi - lo) / N);
    out.push({ name, a0, a1, rc, errs, spike: d2[qm] / (med || 1e-300), at: (qm + 1) / (N - 1), keysL: A.ev.map(e => e.key).join(' '), keysR: Bv.ev.map(e => e.key).join(' ') });
  }
  return out;
}, cases);
const L = r.map(x => `${x.name} ${x.a0.toFixed(6)}..${x.a1.toFixed(6)}${x.rc ? ' (root chart)' : ''}: err at K 6,12,24,48,96,128,256 ${x.errs.map(e => e.toExponential(1)).join(' ')}; second differences' peak ${x.spike.toExponential(1)} x median at ${x.at.toFixed(4)} of the piece`);
console.log(L.join('\n')); fs.writeFileSync('runs/peb/peb5-posthoc.txt', L.join('\n') + '\n');
await b.close(); srv.close();
