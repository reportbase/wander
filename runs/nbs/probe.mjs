import { serve, ninePage, chromium } from './serve.mjs';
const s = await serve(), b = await chromium.launch(), p = await ninePage(b, s.address().port);
console.log(await p.evaluate(() => { const D = window.__N, B = D.rack9(3); const t0 = performance.now(); let n = 0;
  for (let k = 0; k < 40; k++){ const st = D.simulate ? null : null; } 
  const keys = Object.keys(D).concat(Object.keys(Object.getPrototypeOf(D))); 
  const st = D.strikeOf(0.3, 0, 0, 16, undefined, 0); for (let k = 0; k < 40; k++){ D.simulate(B, st.dir + k * 1e-3, st.speed, st.w, st.vy); n++; }
  return { ms: (performance.now() - t0) / n, hasSim: !!D.simulate, hasRack: !!D.rack9, keys: keys.filter(k => /nine|rack|low|leave|NINE|MATCH|sim|strike/.test(k)) }; }));
await b.close(); s.close();
