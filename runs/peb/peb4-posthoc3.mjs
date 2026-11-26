// PEB run 4, post hoc 3 (plans/peb-plan.md): side spin worn to zero at the second cushion, two rails 0.714..0.997. node runs/peb/peb4-posthoc3.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs';
let html = fs.readFileSync('runs/peb/play-trick-event.html', 'utf8');
html = html.replace('function cushionOne(b, c, onRail) {', 'function cushionOne(b, c, onRail) { (window.__wy = window.__wy || []).push(b.wy);');
const srv = http.createServer((q, r) => { r.writeHead(200, { 'content-type': 'text/html' }); r.end(html); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(`http://localhost:${srv.address().port}/`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
const r = await p.evaluate(() => {
  const T = window.__trick; T.setChallenge('tworail'); const B = T.ballsNow().map(b => ({ ...b }));
  const lo = 0.714453 + 1e-9, hi = 0.996790 - 1e-9, out = [];
  for (const f of [0.80, 0.82, 0.83, 0.835, 0.836, 0.837, 0.84, 0.85, 0.87]) { window.__wy = []; T.simulateEvent(B, [Math.cos(lo + (hi - lo) * f), Math.sin(lo + (hi - lo) * f)], 14, null, 0); out.push(f + ': wy at the cushions ' + window.__wy.map(x => x.toExponential(3)).join(', ')); }
  return out;
});
console.log(r.join('\n')); await b.close(); srv.close();
