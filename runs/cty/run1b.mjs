// CTY run 1b: C4 at poses with something under the crosshair (run 1's pose had nothing there), and frame times.
import { createRequire } from 'module'; import http from 'http'; import fs from 'fs'; import path from 'path';
const require = createRequire(import.meta.url);
let pw; try { pw = require('playwright'); } catch { pw = require('/opt/node-tools/node_modules/playwright'); }
const root = process.cwd();
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
    fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); }); }).listen(8962);
const b = await pw.chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('http://localhost:8962/sky-city.html?time=0'); await p.waitForTimeout(1200);
const out = await p.evaluate(() => {
    const C = window.__skyCity, c4 = [], times = {};
    for (const [eye, kp] of [[[0, 30, -60], 0], [[100, 20, 300], 5], [[-500, 150, 40], -20], [[2000, 60, 2000], 10], [[0, 30, -60], 60]]) {
        for (let ky = -120; ky < 128; ky += 8) { C.set({ eye, q: 0, ky, kp, H: null }); C.frame(); C.frame();
            const s = C.state(); if (!s.target) continue; const r = C.scaleCheck(); c4.push({ eye, ky, kind: s.target.kind, same: r.same, closure: r.closure }); break; } }
    for (const [name, eye, kp] of [['street', [0, 30, -60], 0], ['mid', [-500, 150, 40], -20], ['above', [-200, 300, -300], -40], ['up', [0, 8, -60], 80]]) {
        C.set({ eye, q: 0, ky: 0, kp, H: null }); C.frame(); const t0 = performance.now(); for (let k = 0; k < 20; k++) C.frame(); times[name] = +((performance.now() - t0) / 20).toFixed(1); }
    return { c4, times };
});
console.log(JSON.stringify({ ...out, errors: errs }, null, 1));
fs.writeFileSync('runs/cty/run1b-out.json', JSON.stringify({ ...out, errors: errs }, null, 1));
await b.close(); srv.close();
