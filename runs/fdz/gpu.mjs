// FDZ Part B runner: node runs/fdz/gpu.mjs  (headless Chromium, the pre-installed Playwright)
import { createRequire } from 'module'; const require = createRequire(import.meta.url); const { chromium } = require('/opt/node22/lib/node_modules/playwright');
import path from 'path';
const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const pg = await b.newPage();
await pg.goto('file://' + path.resolve('runs/fdz/gpu.html'));
const info = await pg.evaluate(() => window.__fdz && { ok: __fdz.ok, formats: __fdz.formats, renderer: __fdz.renderer });
console.log(JSON.stringify(info));
if (info && info.ok) {
  const ds = Array.from({ length: 8 }, (_, i) => Math.pow(10, -2 + 4 * i / 7));
  const res = await pg.evaluate((ds) => {
    const out = {};
    for (const s of __fdz.S) out[s] = ds.map(d => __fdz.deltaStar(s, d));
    return out;
  }, ds);
  console.log(JSON.stringify({ ds, res }));
}
await b.close();
