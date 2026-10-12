// MRB run 4: run 3's protocol repaired (the floor's push averaged over a time unit; rattlers only the marbles touching no
// other marble). Periodic sides, μ 0 and 0.5, seeds 5–8. node plans/mrb/run4.mjs → plans/mrb/mrb-run4.txt
import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile, writeFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';
const ROOT = fileURLToPath(new URL('../..', import.meta.url));
const server = createServer(async (req, res) => { const p = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
  try { const b = await readFile(join(ROOT, p)); res.writeHead(200, { 'Content-Type': extname(p) === '.html' ? 'text/html' : 'text/javascript' }); res.end(b); } catch { res.writeHead(404); res.end(); } });
await new Promise(ok => server.listen(0, '127.0.0.1', ok));
const browser = await chromium.launch(), page = await browser.newPage();
await page.goto(`http://127.0.0.1:${server.address().port}/play-marbles.html?n=20`, { waitUntil: 'load' });
const out = [], say = s => { out.push(s); console.log(s); };
const res = { 0: [], 0.5: [] }, t00 = Date.now();
for (const mu of [0, 0.5]) for (const seed of [5, 6, 7, 8]) {
  const r = await page.evaluate(o => {
    const w = __marbles.MARBLES.pour(o), rest = w.settle(1e-4, 300), wt = w.weight();
    const n = Math.round(1 / w.dt); let f = 0; for (let k = 0; k < n; k++) { w.step(); f += w.load.floor; }
    const top = w.top(), za = 2, zb = top - 2, c = w.coordination(za, zb, 1), cores = {};
    for (const k of [2, 3, 4, 5]) cores[k] = w.coordination(za, zb, k).n;
    return { rest, t: w.t, floor: f / n / wt, Z: c.Z, n: c.n, ratt: c.rattlers, of: c.of, cores };
  }, { N: 500, kn: 1e5, e: 0.5, mu, muW: mu, box: { kind: 'periodic', W: 7 }, seed });
  res[mu].push(r);
  say(`periodic W 7, μ ${mu}, seed ${seed}: ${r.rest ? 'at rest' : 'not at rest'} by t ${r.t.toFixed(1)}; floor's mean push / weight ${r.floor.toFixed(6)}; Z ${r.Z.toFixed(3)} over ${r.n} (rattlers ${r.ratt} of ${r.of}); k-cores in the bulk: ${Object.entries(r.cores).map(([k, n]) => `${k}: ${n}`).join(', ')}`);
}
const mean = a => a.reduce((x, y) => x + y) / a.length, Z0 = mean(res[0].map(r => r.Z)), Z5 = mean(res[0.5].map(r => r.Z));
const all = [...res[0], ...res[0.5]], worst = Math.max(...all.map(r => Math.abs(r.floor - 1)));
const V = [], verdict = (id, killed, text) => V.push(`${id}: ${killed ? 'KILLED' : 'not killed'}. ${text}`);
verdict('P14', worst >= 5e-4, `the floor's mean push against the weight, worst ${(worst * 100).toFixed(4)}% of 8 (within 0.05%)`);
verdict('P15', Math.abs(Z0 - 6) >= 0.25, `frictionless Z ${Z0.toFixed(3)} (${res[0].map(r => r.Z.toFixed(3)).join(', ')}), within 0.25 of 6`);
verdict('P16', !(Z5 >= 3.5 && Z5 <= 5) || !(Z5 <= Z0 - 1), `μ 0.5 Z ${Z5.toFixed(3)} (${res[0.5].map(r => r.Z.toFixed(3)).join(', ')}), between 3.5 and 5.0 and at least 1 below ${Z0.toFixed(3)}`);
say(''); V.forEach(v => say(v)); say(`(${((Date.now() - t00) / 60000).toFixed(1)} min)`);
await writeFile(fileURLToPath(new URL('mrb-run4.txt', import.meta.url)), out.join('\n') + '\n');
await browser.close(); server.close();
