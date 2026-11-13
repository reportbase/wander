// TWK runs 13 and 14 (plans/twk-plan.md): the world made denser, and one walk drawn two ways
import { createRequire } from 'module'; const require = createRequire(import.meta.url);
const { chromium } = require((process.env.PW || 'playwright'));
const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 800 } });
const errs = []; p.on('pageerror', e => errs.push(e.message));
const url = 'file://' + process.cwd() + '/thumbs-walk.html';
const out = { run13: [], run14: null };
for (const mode of ['fixed', 'kheld']) for (const D of [1, 2, 4, 8, 16]) {
  await p.goto(url); await p.waitForTimeout(500);
  const r = await p.evaluate(({ D, mode }) => { const T = __thumbsWalk;
    T.set({ dens: D, kfix: mode === 'kheld' ? 2100 : 0 });
    for (let i = 0; i < 12; i++) T.frame();   // let K held settle
    const d = T.density(), m = T.againstMade(1.5), bp = T.blueprint();
    return { ...d, missing: m.missing, extra: m.extra, made: m.blueprint, storedN: bp.N }; }, { D, mode });
  out.run13.push({ mode, D, ...r }); console.log(mode, D, JSON.stringify(r));
}
await p.goto(url); await p.waitForTimeout(500);
out.run14 = await p.evaluate(() => __thumbsWalk.twoWays(1, 300));
console.log(JSON.stringify(out.run14));
out.errors = errs; console.log('errors', errs);
(await import('fs')).writeFileSync('runs/twk/run13-out.json', JSON.stringify(out, null, 1));
await b.close();
