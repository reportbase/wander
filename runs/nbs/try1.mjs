import { serve, ninePage, chromium } from './serve.mjs';
import { readFile } from 'node:fs/promises';
const s = await serve(), b = await chromium.launch(), p = await ninePage(b, s.address().port);
await p.evaluate(await readFile(new URL('./page.js', import.meta.url), 'utf8'));
const t0 = Date.now();
const r = await p.evaluate(() => { const N = window.NBS, P = N.positions(3, 20261126);
  const out = [];
  for (const pos of P){ const low = N.lowOf(pos.balls), c0 = N.count; const C = N.planC(pos.balls, 5);
    const t1 = performance.now(); const m = N.mapScan(pos.balls, 16, 720, low.n); const dt = performance.now() - t1;
    const t2 = performance.now(); const h = N.mapHalve(pos.balls, 16, 8, 1e-6, low.n, 200000); const dt2 = performance.now() - t2;
    out.push({ idx: pos.idx, shot: pos.shot, low: low.n, C: { score: C.score, flights: C.flights }, B: { flights: m.flights, edges: m.edges, pieces: m.pieces.length, pots: m.pieces.filter(x => x.j.pot).length, ms: dt | 0 },
      Bp: { flights: h.flights, pieces: h.pieces.length, pots: h.pieces.filter(x => x.j.pot).length, capped: h.capped, dropped: h.dropped, ms: dt2 | 0 } }); }
  return out; });
console.log(JSON.stringify(r, null, 1), (Date.now() - t0) / 1000);
await b.close(); s.close();
