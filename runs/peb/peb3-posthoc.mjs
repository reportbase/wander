// PEB run 3, post hoc (plans/peb-plan.md): the largest remaining jump traced frame by frame. node runs/peb/peb3-posthoc.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-slope3.html`); await p.waitForFunction(() => window.__trick);
const r = await p.evaluate(() => {
  const T = window.__trick; const B = [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)];
  const sim = a => T.simulate(B, [Math.cos(a), Math.sin(a)], 14, null, 0);
  const fc = s => { const c = s.final.find(x=>x.cue); return [c.x, c.z]; };
  const lo = 0.2260359421921734, hi = 0.2783714456225511, N = 20000, h = (hi-lo)/N;
  let prev = fc(sim(lo)), best = null;
  for (let j = 1; j <= N; j++) { const a = lo + h*j, c = fc(sim(a)); const d = Math.hypot(c[0]-prev[0], c[1]-prev[1]); if (!best || d > best.d) best = { d, a }; prev = c; }
  // bisect the jump
  let a0 = best.a - h, a1 = best.a; const F = a => fc(sim(a));
  const f0 = F(a0);
  for (let it = 0; it < 50; it++) { const m = (a0+a1)/2; const fm = F(m); if (Math.hypot(fm[0]-f0[0], fm[1]-f0[1]) < best.d/2) a0 = m; else a1 = m; }
  const S0 = sim(a0), S1 = sim(a1);
  const diffs = []; const n = Math.min(S0.frames.length, S1.frames.length);
  for (let f = 0; f < n; f++) { let d = 0; for (let k = 0; k < S0.frames[f].length; k++) d = Math.max(d, Math.abs(S0.frames[f][k]-S1.frames[f][k])); diffs.push(d); }
  let firstBig = diffs.findIndex(d => d > 1e-4);
  return { jump: best.d, a0, a1, gap: a1-a0, firstBig, around: diffs.slice(Math.max(0,firstBig-3), firstBig+4), cush0: S0.cushions.map(c=>[c.n,c.t]), cush1: S1.cushions.map(c=>[c.n,c.t]), cont0: S0.contacts.map(c=>c.t), cont1: S1.contacts.map(c=>c.t), frames: [S0.frames.length, S1.frames.length], f0: S0.frames[firstBig-1] && [...S0.frames[firstBig-1]], f1: S1.frames[firstBig-1] && [...S1.frames[firstBig-1]] };
});
console.log(JSON.stringify(r, null, 1)); await b.close(); srv.close();
