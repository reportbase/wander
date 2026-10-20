// RSH run (plans/rsh-plan.md): drives games.html's Levels app (reportbase/games) through its hook LEVELS_APP._debug.recover.
// Run from the games checkout: node /home/user/wander/runs/rsh/rsh-run.mjs [games dir]
import { chromium } from '/home/user/games/node_modules/playwright/index.mjs';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join, normalize, extname } from 'node:path';
const ROOT = process.argv[2] || '/home/user/games';
const server = createServer(async (req, res) => { const p = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^\/+/, '');
  try { const b = await readFile(join(ROOT, p || 'index.html')); res.writeHead(200, { 'Content-Type': extname(p) === '.html' ? 'text/html' : extname(p) === '.js' ? 'text/javascript' : 'application/octet-stream' }); res.end(b); } catch { res.writeHead(404); res.end(); } });
await new Promise(ok => server.listen(0, '127.0.0.1', ok));
const browser = await chromium.launch({ args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
page.on('pageerror', e => console.log('pageerror', e.message));
await page.goto(`http://127.0.0.1:${server.address().port}/games.html?app=levels`);
await page.waitForFunction(() => window.FIELD_APPS && window.FIELD_APPS.find(a => a.name === 'levels'), null, { timeout: 60000 });
const out = await page.evaluate(() => {
  const D = window.FIELD_APPS.find(a => a.name === 'levels')._debug, R = [];
  const lat = D.recover(0).reads;                  // body 0's readings (the lattice's own, if P1 holds)
  let rd = 0, cross = 0, vh = [1, 0], both = [1, 0], rec = 0, fewest = 3, extR = 0, cen = 0, k4 = 0, k4w = 0;
  const recs = [];
  for (let idx = 0; idx < 200; idx++){
    const r = D.recover(idx);
    rd = Math.max(rd, r.rdErr);
    for (let i = 0; i < r.N; i++) for (let j = 0; j < 3; j++) cross = Math.max(cross, Math.abs(r.reads[i][j] - lat[i][j]));
    vh = [Math.min(vh[0], r.vh), Math.max(vh[1], r.vh)]; both = [Math.min(both[0], r.both), Math.max(both[1], r.both)];
    rec = Math.max(rec, r.recErr); fewest = Math.min(fewest, r.fewest);
    // P3: extents in the true ratios; the census 1:1:1
    const t = r.ext.truth, q = r.ext.rec, c = r.ext.census;
    for (const [i, j] of [[0, 1], [1, 2], [0, 2]]){ extR = Math.max(extR, Math.abs(q[i] / q[j] - t[i] / t[j]) / (t[i] / t[j])); cen = Math.max(cen, Math.abs(c[i] / c[j] - 1)); }
    if (idx < 20) recs.push(r.rec);
    // P4: scale the world
    if (idx < 20) for (const k of [1e-3, 7, 1e3]){ const s = D.recover(idx, k);
      for (let i = 0; i < s.N; i++){ for (let j = 0; j < 3; j++) k4 = Math.max(k4, Math.abs(s.reads[i][j] - r.reads[i][j]));
        if (s.rec[i] && r.rec[i]){ for (let j = 0; j < 3; j++) k4 = Math.max(k4, Math.abs(s.rec[i][j] - r.rec[i][j]) / (r.meanR / r.AB));
          for (let j = 0; j < 3; j++) k4w = Math.max(k4w, Math.abs(s.rec[i][j] * s.AB - s.P[i][j]) / s.meanR); } } }
  }
  // P6: bodies told apart by the three readers (in |AB|); from the one reader identical (cross above)
  let leastPair = Infinity;
  for (let a = 0; a < 20; a++) for (let b = a + 1; b < 20; b++){ let m = 0; const A = recs[a], B = recs[b];
    for (let i = 0; i < A.length; i++) if (A[i] && B[i]) for (let j = 0; j < 3; j++) m = Math.max(m, Math.abs(A[i][j] - B[i][j]));
    const r0 = D.recover(a); leastPair = Math.min(leastPair, m / (r0.meanR / r0.AB)); }
  return { rd, cross, vh, both, rec, fewest, extR, cen, k4, k4w, leastPair };
});
const f = x => x.toExponential(2), P = [];
console.log(`P1 readings against the lattice: worst ${f(out.rd)}; between bodies: worst ${f(out.cross)}; P(v ≤ h) ${out.vh.map(x => x.toFixed(4)).join('–')}, P(v ≤ h, v₂ ≤ h) ${out.both.map(x => x.toFixed(4)).join('–')}`);
P.push(['P1', out.rd <= 1e-12 && out.cross <= 1e-12 && Math.abs(out.vh[0] - 0.5) <= 0.01 && Math.abs(out.vh[1] - 0.5) <= 0.01 && Math.abs(out.both[0] - 1 / 3) <= 0.01 && Math.abs(out.both[1] - 1 / 3) <= 0.01]);
console.log(`P2 three readers, every point in |AB|: worst ${f(out.rec)} of the mean radius`); P.push(['P2', out.rec <= 1e-9]);
console.log(`P3 extents' ratios: worst ${f(out.extR)}; the census's from 1:1:1: worst ${f(out.cen)}`); P.push(['P3', out.extR <= 1e-9 && out.cen <= 0.01]);
console.log(`P4 k = 1e-3, 7, 1e3: readings and |AB| points worst ${f(out.k4)}; with |AB| carried in, off the truth ${f(out.k4w)}`); P.push(['P4', out.k4 <= 1e-9 && out.k4w <= 1e-9]);
console.log(`P5 fewest readers seeing a point, over 200 bodies: ${out.fewest}`); P.push(['P5', out.fewest >= 2]);
console.log(`P6 least pair difference among the first 20 bodies (three readers, in |AB|): ${out.leastPair.toFixed(4)} of the mean radius`); P.push(['P6', out.leastPair > 0.01]);
for (const [k, ok] of P) console.log(k, ok ? 'not killed' : 'KILLED');
await browser.close(); server.close();
