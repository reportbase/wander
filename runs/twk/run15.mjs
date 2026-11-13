// TWK run 15: things that move. The read's movers against every mover stored and stepped one tick at a time.
// Run from the repository's root: PW=/opt/node22/lib/node_modules/playwright node runs/twk/run15.mjs
import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)(process.env.PW || 'playwright');
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd();
const srv = http.createServer((q, r) => { fs.readFile(path.join(root, decodeURIComponent(q.url.split('?')[0])), (e, d) => { r.writeHead(e ? 404 : 200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(8151);
const b = await chromium.launch(); const errs = [];
async function open(q) { const pg = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 }); pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto('http://localhost:8151/thumbs-walk.html?time=0' + q); await pg.waitForFunction(() => window.__thumbsWalk); return pg; }
const sum = rows => { const h = rows.map(r => r.read); return { compared: rows.length, missing: rows.reduce((a, r) => a + r.missing, 0), extra: rows.reduce((a, r) => a + r.extra, 0),
  exact: rows.every(r => r.exact), heldMin: Math.min(...h), heldMax: Math.max(...h), heldMean: h.reduce((a, x) => a + x, 0) / h.length,
  scanned: [...new Set(rows.map(r => r.scanned))], stored: rows.at(-1).stored, adds: rows.at(-1).adds }; };
const pg = await open('');
const out = {};
out.V4 = await pg.evaluate(() => { const T = window.__thumbsWalk; T.frame(); const all = T.cull(); const g = T.groundNear().length;
  return { groundHeld: g, keptWithMovers: all.kept }; });
out.V1still = sum(await pg.evaluate(() => window.__thumbsWalk.moversAgainstStepped({ T0: 0, ticks: 200, every: 10 })));
out.V1walk = sum(await pg.evaluate(() => window.__thumbsWalk.moversAgainstStepped({ T0: 0, ticks: 200, every: 10, walk: 0.5, seed: 7 })));
out.V1far = sum(await pg.evaluate(() => window.__thumbsWalk.moversAgainstStepped({ T0: '1' + '0'.repeat(30), ticks: 60, every: 10 })));
out.V3 = await pg.evaluate(() => window.__thumbsWalk.moverSteps());
out.V3far = await pg.evaluate(() => { const T = window.__thumbsWalk; const r = [];
  for (const t of ['0', '1000', '1' + '0'.repeat(30)]) { T.set({ tick: t }); const m = T.moversNear(); r.push({ tick: t.length > 6 ? '1e' + (t.length - 1) : t, held: m.length }); } T.set({ tick: 0 }); return r; });
out.V5 = await pg.evaluate(() => { const T = window.__thumbsWalk; const res = [];
  for (const t of ['0', '100', '10000', '1' + '0'.repeat(30)]) { T.set({ tick: t }); const m = T.moversNear(); if (!m.length) { res.push({ t, none: true }); continue; }
    let ok = 0, n = 0; for (const x of m.slice(0, 20)) { const X = T.exactOfThing ? T.exactOfThing(x) : null; if (!X) continue; n++; if (X.closureOK && X.pairs.every(p => p.eulerOK && p.modOK)) ok++; }
    res.push({ t: t.length > 6 ? '1e30' : t, checked: n, ok }); } T.set({ tick: 0 }); return res; });
await pg.close();
const p0 = await open('&movers=0');
out.V4off = await p0.evaluate(() => { const T = window.__thumbsWalk; T.frame(); return { held: T.cull().kept }; });
await p0.close();
const p1 = await open('');
out.V4made = await p1.evaluate(() => { const T = window.__thumbsWalk; T.frame(); return T.againstMadeNow(1); });
await p1.close();
console.log(JSON.stringify(out, null, 1)); console.log('errors', errs); await b.close(); srv.close();
