// TWK run 11: a blueprint's cells and things against the square it covers, and the read's cells at each square's middle.
// Run from the repository's root: node runs/twk/run11.mjs
import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)(process.env.PW || 'playwright');
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd();
const srv = http.createServer((q, r) => { fs.readFile(path.join(root, decodeURIComponent(q.url.split('?')[0])), (e, d) => { r.writeHead(e ? 404 : 200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(8141);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
const errs = []; pg.on('pageerror', e => errs.push(String(e)));
await pg.goto('http://localhost:8141/thumbs-walk.html'); await pg.waitForFunction(() => window.__thumbsWalk);
const r = await pg.evaluate(() => { const T = window.__thumbsWalk, F = T.Fr, out = { builds: [], reads: [] };
  for (const R0 of [750, 1500, 3000, 6000]) out.builds.push({ ...T.buildCount(R0), formula: T.cellFormula(R0) });
  out.below = { formula: T.cellFormula(3000, -8, 8), formula0: T.cellFormula(3000, 0, 8) };
  for (const X of ['0', '0', '0', '0', '1' + '0'.repeat(100)]) { const x = BigInt(X);
    T.set({ q: 1, ky: 18, kp: 0, eye: [F.make(x), F.make(2), F.make(x)], focus: 0 }); const c = T.cull(); out.reads.push({ X: X.length, scanned: c.scanned, kept: c.kept }); }
  return out; });
console.log(JSON.stringify(r, null, 1)); console.log('errors', errs); await b.close(); srv.close();
