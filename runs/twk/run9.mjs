// TWK runs 9 and 10: three seeded walks, a blueprint made about the eye after every action, what each holds and draws.
// Run from the repository's root: node runs/twk/run9.mjs
import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)(process.env.PW || 'playwright');
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd();
const srv = http.createServer((q, r) => { fs.readFile(path.join(root, decodeURIComponent(q.url.split('?')[0])), (e, d) => { r.writeHead(e ? 404 : 200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(8139);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
const errs = []; pg.on('pageerror', e => errs.push(String(e)));
await pg.goto('http://localhost:8139/thumbs-walk.html'); await pg.waitForFunction(() => window.__thumbsWalk);
const N = +(process.env.N || 100), out = {};
for (const [name, X, seed, deep] of [['start', '0', 11, false], ['1e100', '1' + '0'.repeat(100), 22, false], ['1e30 deep', '1' + '0'.repeat(30), 33, true]]) {
  const t0 = Date.now();
  const r = await pg.evaluate(({ X, seed, deep, N }) => { const T = window.__thumbsWalk, F = T.Fr, x = BigInt(X);
    T.set({ q: 1, ky: 18, kp: 0, eye: [F.make(x), F.make(2), F.make(x - 30n)], focus: null });
    if (deep) { for (let i = 0; i < 40 && T.digits().focus >= 0; i++) { if (!T.approach(1)) { T.turnBy(3); } T.frame(); T.frame(); } }
    const startFocus = T.digits().focus;
    return { startFocus, ...T.walkTest(seed, N, 1.5, true) }; }, { X, seed, deep, N });
  const rows = r.rows, foci = [...new Set(rows.map(q => q.focus))].sort((a, c) => a - c);
  out[name] = { startFocus: r.startFocus, poses: rows.length, missing: rows.reduce((a, q) => a + q.missing, 0), extra: rows.reduce((a, q) => a + q.extra, 0),
    segMismatch: rows.reduce((a, q) => a + q.segMismatch, 0), maxPx: Math.max(...rows.map(q => q.maxPx)), segs: rows.reduce((a, q) => a + q.segs, 0),
    held: [Math.min(...rows.map(q => q.read)), Math.max(...rows.map(q => q.read))], foci, anchors: r.anchors, gActs: r.gActs, bActs: r.bActs,
    digits: [Math.min(...rows.map(q => q.digits)), Math.max(...rows.map(q => q.digits))], cellsOverScan: Math.min(...rows.map(q => q.cells / q.scanned)), W: r.W, H: r.H, s: (Date.now() - t0) / 1000 };
  console.log(name, JSON.stringify(out[name])); fs.writeFileSync('runs/twk/run9-' + name.replace(/ /g, '-') + '.json', JSON.stringify(rows));
}
console.log('errors', errs); await b.close(); srv.close();
