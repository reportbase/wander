// PEB run 4, post hoc (plans/peb-plan.md): why a third of the pieces are not held. node runs/peb/peb4-posthoc.mjs cut|tworail
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const which = process.argv[2], root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage(); p.on('pageerror', e => console.log('page error', e.message));
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event.html`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
const r = await p.evaluate((name) => {
  const T = window.__trick;
  const B = name === 'cut' ? [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)] : (T.setChallenge('tworail'), T.ballsNow().map(b => ({ ...b })));
  const pw = 14, obj = B.find(b => !b.cue).n;
  const run = a => T.simulateEvent(B, [Math.cos(a), Math.sin(a)], pw, null, 0);
  const sig = s => s.ev.map(e => e.key).join(' ');
  const full = s => [...s.contacts.map(c => [c.t, 'B' + c.a + '-' + c.b]), ...s.cushions.map(c => [c.t, 'C' + c.n]), ...s.sunk.map(c => [c.t, 'P' + c.n]), ...s.phases.map(c => [c.t, (c.ph === 'slide' ? 'S' : 'R') + c.n])].sort((x, y) => x[0] - y[0]).map(x => x[1]).join(' ');
  const outc = s => { const c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj); return [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z]; };
  const M = 1024, aims = [], sg = [];
  for (let j = 0; j < M; j++) { const a = (j + 0.5) * 2 * Math.PI / M; aims.push(a); sg.push(sig(run(a))); }
  const jumps = [];
  for (let j = 0; j < M; j++) {
    const j2 = (j + 1) % M; if (sg[j] === sg[j2]) continue;
    let lo = aims[j], hi = aims[j2] + (j2 === 0 ? 2 * Math.PI : 0); const s0 = sg[j];
    for (let it = 0; it < 60 && hi - lo > 1e-12; it++) { const m = (lo + hi) / 2; if (sig(run(m)) === s0) lo = m; else hi = m; }
    jumps.push({ lo, hi });
  }
  jumps.sort((x, y) => x.lo - y.lo);
  const KS = [6, 8, 12, 16, 24, 32, 48, 64, 96, 128];
  const errs = (lo, hi) => {
    const mid = (lo + hi) / 2, half = (hi - lo) / 2, test = [];
    for (let q = 0; q < 200; q++) { const a = lo + (hi - lo) * (q + 0.5) / 200; test.push([(a - mid) / half, outc(run(a))]); }
    const out = [];
    for (const K of KS) {
      const z = [], w = [], f = [];
      for (let k = 0; k < K; k++) { const th = (k + 0.5) * Math.PI / K; z.push(Math.cos(th)); w.push((k % 2 ? -1 : 1) * Math.sin(th)); f.push(outc(run(mid + half * Math.cos(th)))); }
      let err = 0, at = 0;
      for (const [y, tr] of test) { let den = 0; const num = [0, 0, 0, 0]; for (let k = 0; k < K; k++) { const q = w[k] / (y - z[k]); den += q; for (let c = 0; c < 4; c++) num[c] += q * f[k][c]; } for (let c = 0; c < 4; c++) { const e = Math.abs(num[c] / den - tr[c]); if (e > err) { err = e; at = y; } } }
      out.push([K, err, at]);
    }
    return out;
  };
  const res = [];
  for (let i = 0; i < jumps.length; i++) {
    const J0 = jumps[i], J1 = i + 1 < jumps.length ? jumps[i + 1] : { lo: jumps[0].lo + 2 * Math.PI, hi: jumps[0].hi + 2 * Math.PI };
    const e0 = J0.hi, e1 = J1.lo; if (e1 - e0 < 1e-4) continue;
    const E = errs(e0 + 1e-10, e1 - 1e-10); if (E[E.length - 1][1] <= 1e-6 || E.some(x => x[1] <= 1e-6)) continue;   // held: skip
    // full-order changes inside the piece
    const N = 2001, A = [], F = [];
    for (let q = 0; q < N; q++) { const a = e0 + 1e-10 + (e1 - e0 - 2e-10) * q / (N - 1); A.push(a); F.push(full(run(a))); }
    const sub = [];
    for (let q = 0; q < N - 1; q++) if (F[q] !== F[q + 1]) {
      let lo = A[q], hi = A[q + 1]; const f0 = F[q];
      for (let it = 0; it < 60 && hi - lo > 1e-12; it++) { const m = (lo + hi) / 2; if (full(run(m)) === f0) lo = m; else hi = m; }
      const fa = F[q].split(' '), fb = F[q + 1].split(' '); let k = 0; while (k < fa.length && fa[k] === fb[k]) k++;
      sub.push({ lo, hi, what: (fa[k] || '-') + ' / ' + (fb[k] || '-') });
    }
    // sub-pieces held?
    const cuts = [e0, ...sub.map(s => s.hi), e1].map((x, k, arr) => x);
    const edges = [e0, ...sub.flatMap(s => [s.lo, s.hi]), e1], subs = [];
    for (let k = 0; k < edges.length; k += 2) { const lo = edges[k], hi = edges[k + 1]; if (hi - lo < 1e-6) { subs.push({ w: hi - lo, K: 'narrow' }); continue; } const S = errs(lo + 1e-12, hi - 1e-12); const h = S.find(x => x[1] <= 1e-6); subs.push({ w: hi - lo, K: h ? h[0] : null, last: S[S.length - 1][1] }); }
    res.push({ a0: e0, a1: e1, w: e1 - e0, errs: E.map(x => [x[0], +x[1].toExponential(2), +x[2].toFixed(3)]), sub: sub.map(s => s.what), subs });
  }
  return res;
}, which);
fs.writeFileSync(`runs/peb/peb4-posthoc-${which}.json`, JSON.stringify(r, null, 1));
for (const x of r) {
  console.log(`piece ${x.a0.toFixed(6)}..${x.a1.toFixed(6)} (w ${x.w.toExponential(2)}): err at K=6..128 ${x.errs.map(e => e[1]).join(' ')}; worst at y ${x.errs[x.errs.length - 1][2]}`);
  console.log(`   phase-order changes inside: ${x.sub.length} ${x.sub.slice(0, 6).join('; ')}`);
  console.log(`   sub-pieces: ${x.subs.map(s => s.K === 'narrow' ? 'narrow' : (s.K ?? 'not held ' + s.last.toExponential(1))).join(', ')}`);
}
await b.close(); srv.close();
