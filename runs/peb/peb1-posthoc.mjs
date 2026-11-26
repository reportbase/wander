// PEB run 1, post hoc (plans/peb-plan.md): the hidden jumps inside one piece of the cut's shot map. node runs/peb/peb1-posthoc.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-slope.html`); await p.waitForFunction(() => window.__trick);
const r = await p.evaluate(() => {
  const T = window.__trick; const B = [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)];
  const sim = a => { const s = T.simulate(B, [Math.cos(a), Math.sin(a)], 14, null, 0); const c = s.final.find(x=>x.cue), o = s.final.find(x=>!x.cue); return [c.x, c.z, o.x, o.z]; };
  const lo = 0.2260359421921734, hi = 0.2783714456225511; const N = 100000, h = (hi-lo)/N;
  let prev = sim(lo + h/2), d1p = null, big = 0, kinks = 0; const sizes = [];
  for (let j = 1; j < N; j++) { const cur = sim(lo + h*(j+0.5)); const d = Math.max(...cur.map((v,k)=>Math.abs(v-prev[k])));
    sizes.push(d); prev = cur; }
  const sorted = [...sizes].sort((a,b)=>a-b), med = sorted[sorted.length>>1];
  const jumps = sizes.filter(d => d > 20*med);
  return { width: hi-lo, step: h, median: med, jumps: jumps.length, largest: sorted[sorted.length-1], over1e4: sizes.filter(d=>d>1e-4).length, over1e6: sizes.filter(d=>d>1e-6 && d > 20*med).length };
});
console.log(JSON.stringify(r, null, 1)); await b.close(); srv.close();
