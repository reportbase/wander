// MRB run 3: the heap at rest, on play-marbles.html's engine, driven through its hook (as CUE drove play-trick.html's).
// node plans/mrb/run3.mjs → plans/mrb/mrb-run3.txt
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
await page.goto(`http://127.0.0.1:${server.address().port}/play-marbles.html`, { waitUntil: 'load' });
const out = [], say = s => { out.push(s); console.log(s); };
const KN = 1e5, E = 0.5;
// one pour, settled, read
const pourRead = opts => page.evaluate(o => {
  const w = __marbles.MARBLES.pour(o), t0 = performance.now(), rest = w.settle(1e-4, 600), wt = w.weight(), L = w.load, top = w.top();
  const r = { rest, t: w.t, secs: (performance.now() - t0) / 1000, floor: L.floor / wt, walls: L.walls / wt, top, vmax: w.maxSpeed(true) };
  if (o.box.kind === 'periodic') { const za = 2, zb = top - 2; r.coord = w.coordination(za, zb); r.phi = w.volumeIn(za, zb) / (o.box.W * o.box.W * (zb - za)); r.slab = [za, zb]; }
  if (o.box.kind === 'silo') { // the column's bulk density: marbles with centres below top − 1, over that column's volume
    let n = 0; for (let i = 0; i < w.N; i++) if (w.z[i] < top - 1) n++; r.rhoB = n / (o.box.W * o.box.W * (top - 1)); r.phiSlab = top > 5 ? w.volumeIn(1, top - 1) / (o.box.W * o.box.W * (top - 2)) : null; }
  return r;
}, { kn: KN, e: E, ...opts });
const t00 = Date.now(), res = { per: {}, silo: [], silo0: null };
for (const mu of [0, 0.5]) {
  res.per[mu] = [];
  for (const seed of [1, 2, 3, 4]) {
    const r = await pourRead({ N: 500, mu, muW: mu, box: { kind: 'periodic', W: 7 }, seed });
    res.per[mu].push(r);
    say(`periodic W 7, μ ${mu}, seed ${seed}: ${r.rest ? 'at rest' : 'NOT AT REST'} at t ${r.t.toFixed(1)} (${r.secs.toFixed(0)} s); floor/weight ${r.floor.toFixed(6)}; top ${r.top.toFixed(2)}; bulk z ${r.slab.map(v => v.toFixed(2)).join('–')}: Z ${r.coord.Z.toFixed(3)} over ${r.coord.n} (rattlers ${r.coord.rattlers} of ${r.coord.of}), φ ${r.phi.toFixed(4)}`);
  }
}
for (const N of [100, 200, 300, 400, 500]) for (const seed of [1, 2]) {
  const r = await pourRead({ N, mu: 0.5, muW: 0.5, box: { kind: 'silo', W: 6 }, seed });
  res.silo.push({ N, seed, ...r });
  say(`silo W 6, μ 0.5, μw 0.5, N ${N}, seed ${seed}: ${r.rest ? 'at rest' : 'NOT AT REST'} at t ${r.t.toFixed(1)} (${r.secs.toFixed(0)} s); floor ${r.floor.toFixed(4)} walls ${r.walls.toFixed(4)} of the weight (sum ${(r.floor + r.walls).toFixed(6)}); top ${r.top.toFixed(2)}; ρ_b ${r.rhoB.toFixed(4)}${r.phiSlab ? `, φ ${r.phiSlab.toFixed(4)}` : ''}`);
}
{ const r = await pourRead({ N: 500, mu: 0.5, muW: 0, box: { kind: 'silo', W: 6 }, seed: 1 }); res.silo0 = r;
  say(`silo W 6, μ 0.5, μw 0, N 500, seed 1: ${r.rest ? 'at rest' : 'NOT AT REST'} at t ${r.t.toFixed(1)} (${r.secs.toFixed(0)} s); floor ${r.floor.toFixed(6)} walls ${r.walls.toFixed(6)}`); }

// Janssen's fit: M_app = M∞(1 − e^(−M/M∞)), one parameter, least squares over the ten pours (golden-section on M∞)
const pts = res.silo.map(s => [s.N, s.floor * s.N]);
const sse = Minf => pts.reduce((a, [M, A]) => a + (A - Minf * (1 - Math.exp(-M / Minf))) ** 2, 0);
let lo = 10, hi = 1e6; for (let k = 0; k < 200; k++) { const a = lo + (hi - lo) * 0.382, b = lo + (hi - lo) * 0.618; if (sse(a) < sse(b)) hi = b; else lo = a; }
const Minf = (lo + hi) / 2, rhoB = res.silo.filter(s => s.N === 500).reduce((a, s) => a + s.rhoB, 0) / 2, lam = Minf / (rhoB * 36), K = 6 / (4 * 0.5 * lam);
say(`Janssen fit: M∞ ${Minf.toFixed(1)} marbles; ρ_b ${rhoB.toFixed(4)} per σ³ (the 500 fills); λ ${lam.toFixed(2)}σ; K = W/(4 μ_w λ) ${K.toFixed(3)}`);
const offs = pts.map(([M, A]) => [M, A / (Minf * (1 - Math.exp(-M / Minf))) - 1]);
say('  each fill against the fit: ' + offs.map(([M, d], k) => `N ${M} s${res.silo[k].seed} ${(d * 100).toFixed(2)}%`).join(', '));

// verdicts, as the plan wrote them
const V = [], verdict = (id, killed, text) => V.push(`${id}: ${killed ? 'KILLED' : 'not killed'}. ${text}`);
const all = [...res.per[0], ...res.per[0.5], ...res.silo];
{ const worst = Math.max(...all.map(r => Math.abs(r.floor + r.walls - 1))), f0 = Math.abs(res.silo0.floor - 1);
  verdict('P9', worst >= 1e-3 || f0 >= 5e-3, `floor and walls against the weight, worst ${(worst * 100).toFixed(4)}% of 18 pours (within 0.1%); μ_w 0, floor alone ${(res.silo0.floor * 100).toFixed(4)}% (within 0.5%)`); }
const mean = a => a.reduce((x, y) => x + y) / a.length;
const Z0 = mean(res.per[0].map(r => r.coord.Z)), Z5 = mean(res.per[0.5].map(r => r.coord.Z)), p0 = mean(res.per[0].map(r => r.phi)), p5 = mean(res.per[0.5].map(r => r.phi));
verdict('P10', Math.abs(Z0 - 6) >= 0.25, `frictionless Z ${Z0.toFixed(3)} (seeds ${res.per[0].map(r => r.coord.Z.toFixed(3)).join(', ')}), within 0.25 of 6`);
verdict('P11', !(Z5 >= 4 && Z5 <= 5.5) || !(Z5 <= Z0 - 0.5), `μ 0.5 Z ${Z5.toFixed(3)} (seeds ${res.per[0.5].map(r => r.coord.Z.toFixed(3)).join(', ')}), between 4 and 5.5 and at least 0.5 below ${Z0.toFixed(3)}`);
verdict('P12', Math.abs(p0 - 0.637) > 0.015 || Math.abs(p5 - 0.60) > 0.02, `bulk φ frictionless ${p0.toFixed(4)} (0.637 ± 0.015), μ 0.5 ${p5.toFixed(4)} (0.60 ± 0.02)`);
verdict('P13', offs.some(([, d]) => Math.abs(d) >= 0.03) || !(K >= 0.3 && K <= 1.0), `every fill within 3% of the fit: worst ${(Math.max(...offs.map(([, d]) => Math.abs(d))) * 100).toFixed(2)}%; K ${K.toFixed(3)} (between 0.3 and 1.0)`);
const notRest = all.concat([res.silo0]).filter(r => !r.rest).length;
say(''); V.forEach(v => say(v)); say(`pours not at rest by t 600: ${notRest} of 19`); say(`(${((Date.now() - t00) / 60000).toFixed(1)} min)`);
await writeFile(fileURLToPath(new URL('mrb-run3.txt', import.meta.url)), out.join('\n') + '\n');
await browser.close(); server.close();
