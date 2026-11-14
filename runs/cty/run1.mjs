// CTY run 1: the predictions C1-C8 of plans/cty-plan.md, through sky-city.html's hook in headless Chromium.
// Run from the repository's root: node runs/cty/run1.mjs
import { createRequire } from 'module'; import http from 'http'; import fs from 'fs'; import path from 'path';
const require = createRequire(import.meta.url);
let pw; try { pw = require('playwright'); } catch { pw = require('/opt/node-tools/node_modules/playwright'); }
const root = process.cwd();
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0]));
    fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html' : 'text/plain' }); r.end(d); }); }).listen(8961);
const b = await pw.chromium.launch(); const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto('http://localhost:8961/sky-city.html?time=0'); await p.waitForTimeout(1500);
const out = await p.evaluate(async () => {
    const C = window.__skyCity, R = {};
    // poses of a seeded flight: street level, mid-height, above the roofs, looking up, looking down
    let sd = 7 >>> 0; const rnd = () => ((sd = (Math.imul(sd, 1103515245) + 12345) >>> 0) / 4294967296);
    const poses = [];
    for (let k = 0; k < 40; k++) { const kind = k % 5, y = [6, 70, 260, 8, 300][kind], kp = [0, 10, -20, 80, -80][kind];
        poses.push({ eye: [Math.round((rnd() - 0.5) * 4000), y, Math.round((rnd() - 0.5) * 4000)], q: 2 * Math.floor(rnd() * 2), ky: Math.floor(rnd() * 256) - 128, kp, kind }); }
    R.C1 = []; R.C6 = { level: [], up: [], down: [], mid: [], roof: [] };
    for (const ps of poses) { C.set({ eye: ps.eye, q: ps.q, ky: ps.ky, kp: ps.kp, H: null }); C.frame(); C.frame();
        const m = C.againstMade(2), cu = C.cull(); R.C1.push({ kind: ps.kind, missing: m.missing, extra: m.extra, read: m.read, R: m.R });
        R.C6[['level', 'mid', 'roof', 'up', 'down'][ps.kind]].push(cu.held); }
    // C2: cars and elevators against stepped, still, flying, and from T = 10^30
    const at = (eye, tick) => C.set({ eye, q: 0, ky: 0, kp: 0, tick, H: 60 });
    at([0, 70, -60], 0); R.C2still = C.againstStepped({ ticks: 200, every: 10 });
    at([0, 70, -60], 0); R.C2fly = C.againstStepped({ ticks: 200, every: 10, fly: 0.5 });
    at([500, 80, 500], '1000000000000000000000000000000'); R.C2big = C.againstStepped({ ticks: 200, every: 10 });
    // C3
    at([0, 30, -60], 0); R.C3 = C.trigFree(300);
    // C4: aim at something first
    at([0, 30, -60], 0); C.frame(); C.frame(); R.C4 = C.scaleCheck(); R.C4target = C.state().target;
    // C5: cells scanned at one look, the thumb held, at 0, 10^6, 10^100 out
    const big = '1' + '0'.repeat(100); R.C5 = [];
    for (const x of ['0', '1000000', big]) { C.set({ eye: [C.Fr.make(BigInt(x)), C.Fr.make(30), C.Fr.make(-60)], q: 0, ky: 0, kp: 0, H: 60 }); const cu = C.cull(); R.C5.push({ x: x.length, scanned: cu.scanned, R: cu.R, held: cu.held }); }
    // C7, C8
    R.C7 = C.traffic.pieces(600, 10); R.C8 = C.traffic.check(6000);
    return R;
});
const sum = a => ({ n: a.length, min: Math.min(...a), max: Math.max(...a), mean: Math.round(a.reduce((x, y) => x + y, 0) / a.length) });
const res = {
    C1: { poses: out.C1.length, missing: out.C1.reduce((a, r) => a + r.missing, 0), extra: out.C1.reduce((a, r) => a + r.extra, 0), worst: out.C1.filter(r => r.missing || r.extra) },
    C2: ['C2still', 'C2fly', 'C2big'].map(k => ({ k, rows: out[k].length, bad: out[k].filter(r => r.missing || r.extra || !r.same).length, compared: out[k].reduce((a, r) => a + r.compared, 0), stored: out[k].at(-1).stored, adds: out[k].at(-1).adds })),
    C3: out.C3, C4: out.C4, C4target: out.C4target, C5: out.C5,
    C6: Object.fromEntries(Object.entries(out.C6).map(([k, v]) => [k, sum(v)])), C7: out.C7, C8: out.C8, errors: errs };
console.log(JSON.stringify(res, null, 1));
fs.writeFileSync('runs/cty/run1-out.json', JSON.stringify({ res, raw: out }, null, 1));
await p.goto('http://localhost:8961/sky-city.html?time=0&x=0&y=40&z=-60'); await p.waitForTimeout(1200);
await p.screenshot({ path: 'runs/cty/run1-street.png' });
await p.goto('http://localhost:8961/sky-city.html?time=0&x=-200&y=150&z=-300&kp=-15'); await p.waitForTimeout(1200);
await p.screenshot({ path: 'runs/cty/run1-above.png' });
await b.close(); srv.close();
