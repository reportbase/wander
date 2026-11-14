// TWK run 20c: R3 measured on what is drawn (things in front whose centre lands on the screen), from a fresh start, and
// R4 at five poses. From the repository's root: node runs/twk/run20c.mjs
import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)('/opt/node22/lib/node_modules/playwright');
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd(), port = 8163;
const srv = http.createServer((q, r) => { fs.readFile(path.join(root, decodeURIComponent(q.url.split('?')[0])), (e, d) => { r.writeHead(e ? 404 : 200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(port);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } }); const errs = []; pg.on('pageerror', e => errs.push(String(e)));
await pg.goto(`http://localhost:${port}/thumbs-walk.html?time=0&movers=0&rings=0`); await pg.waitForFunction(() => window.__thumbsWalk);
const out = await pg.evaluate(async () => {
  const T = window.__thumbsWalk, sl = ms => new Promise(r => setTimeout(r, ms)), res = {};
  const snap = () => new Map(T.groundNear().filter(t => T.onScreen(t)).map(t => [t.key, T.fadeOf(t)]));
  let prev = snap(), worst = 0, worstFrac = 0, steps = [];
  for (let k = 0; k < 120; k++) { T.turnBy(1); await sl(16); T.frame(); const now = snap(); let w = 0, ch = 0;
    for (const [key, a] of now) { const d = Math.abs(a - (prev.get(key) ?? 0)); w = Math.max(w, d); if (!prev.has(key)) ch++; }
    for (const [key, a] of prev) if (!now.has(key)) { w = Math.max(w, a); ch++; }
    const f = ch / Math.max(1, prev.size); worst = Math.max(worst, w); worstFrac = Math.max(worstFrac, f); steps.push([k, +w.toFixed(3), +f.toFixed(3), now.size]); prev = now; }
  res.R3c = { worstFade: worst, worstFrac, onScreen: [Math.min(...steps.map(s => s[3])), Math.max(...steps.map(s => s[3]))], over: steps.filter(s => s[1] >= 0.35 || s[2] > 0.06) };
  const settle = async () => { for (let i = 0; i < 80; i++) { await sl(16); T.frame(); } };
  const poses = [{}, { q: 1, ky: 30 }, { kp: 50 }, { walk: 1 }, { H: 3 }]; res.R4c = [];
  T.set({ q: 0, ky: 0, kp: 0, H: null }); await settle();
  for (const p of poses) { if (p.walk) T.set({ eye: [5, 2, 40] }); else T.set(p); await settle(); const m = T.againstMadeNow(1); res.R4c.push({ missing: m.missing, extra: m.extra, held: m.read }); }
  return res; });
out.errors = errs; console.log(JSON.stringify(out, null, 1));
fs.writeFileSync(path.join(root, 'runs/twk/run20c-out.json'), JSON.stringify(out, null, 1));
await b.close(); srv.close();
