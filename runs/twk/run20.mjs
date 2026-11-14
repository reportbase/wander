// TWK run 20: the read's heat decides what is held (plans/twk-plan.md). Headless Chromium through the page's hook.
// From the repository's root: node runs/twk/run20.mjs
import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)('/opt/node22/lib/node_modules/playwright');
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd(), port = 8160;
const srv = http.createServer((q, r) => { fs.readFile(path.join(root, decodeURIComponent(q.url.split('?')[0])), (e, d) => { r.writeHead(e ? 404 : 200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(port);
const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1280, height: 720 } }); const errs = []; pg.on('pageerror', e => errs.push(String(e)));
await pg.goto(`http://localhost:${port}/thumbs-walk.html?time=0&movers=0&rings=0`); await pg.waitForFunction(() => window.__thumbsWalk);
const out = await pg.evaluate(async () => {
  const T = window.__thumbsWalk, sl = ms => new Promise(r => setTimeout(r, ms)), settle = async (n = 40) => { for (let i = 0; i < n; i++) { await sl(16); T.frame(); } };
  const behind = () => { const P = T.pose ? T.pose() : null; return T.groundNear().filter(t => { const F = window.__twF || null; return false; }).length; };
  await settle(); const res = {};
  const H0 = T.state().H; res.H0 = H0;
  // R2: H from 2^-6 to 2^6 times its start value, the look fixed
  res.R2 = []; for (let k = -6; k <= 6; k++) { T.set({ H: H0 * 2 ** k }); await settle(30); res.R2.push([k, T.groundNear().length]); }
  T.set({ H: H0 }); await settle(30);
  // R1: 16 looks, H held at its start value so only the look moves
  res.R1 = []; for (const kp of [0, 40]) for (let i = 0; i < 8; i++) { T.set({ q: i, ky: 0, kp }); await settle(30); res.R1.push(T.groundNear().length); }
  T.set({ q: 0, ky: 0, kp: 0, H: null }); await settle();
  // R3: 120 one-step pans, H free (following the crosshair), a frame of 16 ms each
  let prev = new Map(T.groundNear().map(t => [t.key, T.fadeOf(t)])), worst = 0, worstFrac = 0;
  for (let k = 0; k < 120; k++) { T.turnBy(1); await sl(16); T.frame(); const now = new Map(T.groundNear().map(t => [t.key, T.fadeOf(t)]));
    let ch = 0; for (const [key, a] of now) { const d = Math.abs(a - (prev.get(key) ?? 0)); worst = Math.max(worst, d); if (!prev.has(key)) ch++; }
    for (const [key, a] of prev) if (!now.has(key)) { worst = Math.max(worst, a); ch++; }
    worstFrac = Math.max(worstFrac, ch / Math.max(1, prev.size)); prev = now; }
  res.R3 = { worstFade: worst, worstFrac };
  // R4: five poses against a blueprint made about the eye by the same rule
  const poses = [{}, { q: 1, ky: 30 }, { kp: 50 }, { walk: 1 }, { H: 3 }]; res.R4 = [];
  T.set({ q: 0, ky: 0, kp: 0, H: null }); await settle();
  for (const p of poses) { if (p.walk) { T.set({ eye: [5, 2, 40] }); } else T.set(p); await settle(); const m = T.againstMadeNow(1); res.R4.push({ missing: m.missing, extra: m.extra, held: m.read }); }
  // R5: nothing behind the look
  res.R5 = T.behindHeld();
  return res; });
out.errors = errs; console.log(JSON.stringify(out, null, 1));
fs.writeFileSync(path.join(root, 'runs/twk/run20-out.json'), JSON.stringify(out, null, 1));
await b.close(); srv.close();
