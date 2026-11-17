// ENG run 1: trig and root calls during the trick-shot engine's shots, attributed by the call stack (plans/eng-plan.md)
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': f.endsWith('.html') ? 'text/html' : 'application/octet-stream' }); r.end(d); } }); }).listen(0);
const port = srv.address().port;
const b = await chromium.launch(); const p = await b.newPage();
await p.addInitScript(() => {
  const TRIG = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2'], ROOT = ['sqrt', 'hypot'];
  window.__eng = { on: false, trig: {}, root: {}, stacks: false };
  const who = () => { const s = new Error().stack.split('\n')[3] || ''; const m = s.match(/at (?:Object\.)?([\w$.<>]+) \(/); return m ? m[1] : (s.includes('play-trick') ? '(anon)' : '(other)'); };
  for (const k of [...TRIG, ...ROOT]) { const f = Math[k], bag = TRIG.includes(k) ? 'trig' : 'root';
    Math[k] = function (...a) { const E = window.__eng; if (E.on) { const w = who() + ':' + k; E[bag][w] = (E[bag][w] || 0) + 1; } return f.apply(Math, a); }; }
});
await p.goto(`http://localhost:${port}/play-trick.html`); await p.waitForFunction(() => window.__trick);
const out = await p.evaluate(() => {
  const T = window.__trick, E = window.__eng, res = [];
  let seed = 12345; const rnd = () => { seed = (seed * 1103515245 + 12345) >>> 0; return seed / 2 ** 32; };
  const run = (label) => { E.trig = {}; E.root = {}; E.on = true; const s = T.preview(); E.on = false;
    const steps = (s.frames.length - 1) * 4; res.push({ label, steps, contacts: s.contacts.length, trig: E.trig, root: E.root }); };
  for (const L of ['rack', 'scatter', 'line', 'jump', 'masse']) for (let i = 0; i < 9; i++) {
    T.setLayout(L); T.aim(-30 + 60 * rnd()); T.power(6 + 30 * rnd()); T.tip(0.5 * (rnd() - 0.5), 0.5 * (rnd() - 0.5)); T.elev(L === 'jump' || L === 'masse' ? 20 + 40 * rnd() : 0);
    run(L + i); }
  T.elev(0);
  for (const c of T.challenges) { T.setChallenge(c.id); T.solve(); run('ch:' + c.id); }
  return res;
});
await b.close(); srv.close();
const physics = ['image', 'respond', 'pairs', 'inAir', 'imageInCushion', 'cloth', 'own', 'firstStop', 'gripOf'];
let physTrig = 0, maxTrig = 0, trigBy = {}, rootBy = {}, steps = 0, contacts = 0;
for (const r of out) { let t = 0; for (const [k, n] of Object.entries(r.trig)) { t += n; trigBy[k] = (trigBy[k] || 0) + n; if (physics.includes(k.split(':')[0])) physTrig += n; }
  maxTrig = Math.max(maxTrig, t); for (const [k, n] of Object.entries(r.root)) rootBy[k] = (rootBy[k] || 0) + n; steps += r.steps; contacts += r.contacts; }
const lines = [];
lines.push(`shots ${out.length}, substeps ${steps}, contacts ${contacts}`);
lines.push(`trig calls by function:call  ${JSON.stringify(trigBy)}`);
lines.push(`trig calls attributed to the physics functions: ${physTrig}`);
lines.push(`most trig calls in one shot: ${maxTrig}; per shot: ${out.map(r => Object.values(r.trig).reduce((a, b) => a + b, 0)).join(' ')}`);
const corr = (() => { const xs = out.map(r => r.steps), ys = out.map(r => Object.values(r.trig).reduce((a, b) => a + b, 0)); const mx = xs.reduce((a, b) => a + b) / xs.length, my = ys.reduce((a, b) => a + b) / ys.length; let sxy = 0, sxx = 0, syy = 0; xs.forEach((x, i) => { sxy += (x - mx) * (ys[i] - my); sxx += (x - mx) ** 2; syy += (ys[i] - my) ** 2; }); return sxy / Math.sqrt(sxx * syy || 1); })();
lines.push(`correlation of a shot's trig calls with its substeps: ${corr.toFixed(3)}`);
lines.push(`roots by function:call (all shots)  ${JSON.stringify(rootBy)}`);
lines.push(`roots per substep: ${(Object.values(rootBy).reduce((a, b) => a + b, 0) / steps).toFixed(3)}; per contact: ${(Object.values(rootBy).reduce((a, b) => a + b, 0) / Math.max(1, contacts)).toFixed(2)}`);
lines.push(`E2: ${physTrig === 0 && maxTrig <= 8 ? 'not killed' : 'KILLED'} (physics trig ${physTrig}, most in a shot ${maxTrig})`);
console.log(lines.join('\n'));
