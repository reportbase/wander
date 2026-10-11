// CUE run 1, the engine's side: what the trick-shot engine predicts, through its own simulate hook (play-trick.html),
// computed and committed before any reference value was opened. node plans/cue/engine.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
const ROOT = fileURLToPath(new URL('../..', import.meta.url));   // the repo
const server = createServer(async (req, res) => { const p = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
  try { const b = await readFile(join(ROOT, p)); res.writeHead(200, { 'Content-Type': extname(p) === '.html' ? 'text/html' : 'text/javascript' }); res.end(b); } catch { res.writeHead(404); res.end(); } });
await new Promise(ok => server.listen(0, '127.0.0.1', ok));
const browser = await chromium.launch(), page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
await page.goto(`http://127.0.0.1:${server.address().port}/play-trick.html`, { waitUntil: 'load' });
const out = await page.evaluate(() => {
  const T = __trick, R = 0.45, D = Math.PI / 180;
  const ball = (n, x, z, cue = false) => ({ n, x, z, vx: 0, vz: 0, r: R, m: 1, cue, sunk: false, col: '#fff', stripe: false });
  // the struck ball's direction in the first frames after it starts to move
  const leave = (sim, k) => { const F = sim.frames; let i0 = -1;
    for (let i = 1; i < F.length; i++) if (F[i][2 * k] !== F[0][2 * k] || F[i][2 * k + 1] !== F[0][2 * k + 1]) { i0 = i; break; }
    if (i0 < 0 || i0 + 3 >= F.length) return null;
    return Math.atan2(F[i0 + 3][2 * k + 1] - F[i0][2 * k + 1], F[i0 + 3][2 * k] - F[i0][2 * k]); };
  // A. cut throw: the white along +x at speed v, the struck ball offset so the cut is phi; throw = phi − its direction
  const throwAt = (phiDeg, v, roll) => { const phi = phiDeg * D, gap = 0.02, W = ball(0, 0, 0, true), O = ball(1, gap + 2 * R * Math.cos(phi), 2 * R * Math.sin(phi));   // a stun stays a stun
    const sim = T.simulate([W, O], 0, v, roll ? [0, 0, -v / R] : [0, 0, 0], 0); const a = leave(sim, 1); return a == null ? null : phiDeg - a / D; };
  const A = {};
  for (const roll of [false, true]) for (const v of [7, 21, 49]) A[`${roll ? 'rolling' : 'stun'} v${v}`] = [10, 20, 30, 45, 60].map(p => +(throwAt(p, v, roll) ?? NaN).toFixed(2));
  // C. cushion: a rolling ball at speed v into the long cushion (z = 5, the centre stops at 4.55) at angle psi from the
  // normal, started 0.6 short of it; its velocity in the frames just before and just after the bounce
  const cush = (psiDeg, v) => { const psi = psiDeg * D, ang = Math.PI / 2 - psi, z0 = 4.55 - Math.max(0.6, v * 0.1) * Math.cos(psi), B = ball(0, -3, z0, true);
    const sim = T.simulate([B], ang, v, [v / R * Math.sin(ang), 0, -v / R * Math.cos(ang)], 0), F = sim.frames;
    let iHit = -1; for (let i = 1; i < F.length; i++) if (F[i][1] < F[i - 1][1] - 1e-9) { iHit = i; break; }
    if (iHit < 3 || iHit + 3 >= F.length) return null;
    const vin = [(F[iHit - 2][0] - F[iHit - 3][0]) * 60, (F[iHit - 2][1] - F[iHit - 3][1]) * 60], vout = [(F[iHit + 2][0] - F[iHit + 1][0]) * 60, (F[iHit + 2][1] - F[iHit + 1][1]) * 60];
    return { in: +(Math.atan2(Math.abs(vin[0]), Math.abs(vin[1])) / D).toFixed(1), out: +(Math.atan2(Math.abs(vout[0]), Math.abs(vout[1])) / D).toFixed(1),
      eN: +(Math.abs(vout[1]) / Math.abs(vin[1])).toFixed(3), speed: +(Math.hypot(...vout) / Math.hypot(...vin)).toFixed(3) }; };
  const C = {}; for (const v of [7, 21, 49]) C[`v${v}`] = [15, 30, 45, 60].map(p => cush(p, v));
  return { A, C };
});
for (const [k, v] of Object.entries(out.A)) console.log('throw', k.padEnd(12), v.join('  '));
for (const [k, v] of Object.entries(out.C)) console.log('cushion', k, JSON.stringify(v));
await browser.close(); server.close();
