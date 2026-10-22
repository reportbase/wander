// Smoke test for Wander, in two parts, run in headless Chromium:
//
//   1. Fly: open the page, press Fly, look around with the mouse and fly with the
//      wheel and keys for a few seconds.
//   2. The labs: open labs.html?lab=all, which runs every lab in turn (THE LAB
//      GUIDE in labs.html asks for exactly this after every change), and wait
//      for the summary table. The labs run on world.js, which the flying page
//      loads too.
//
// Fails on any uncaught error, and on any lab whose latest run comes back
// "error" or with no verdict. A lab that comes back "killed" is a recorded
// open question rather than a fault (the page says so itself), so it is listed
// but does not fail the run.
//
//   npm test                       serves the repo itself on a free port
//   BASE_URL=http://host/ npm test test an already-running server instead

import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('..', import.meta.url));
const LAB_TIMEOUT_MS = Number(process.env.LAB_TIMEOUT_MS || 10 * 60 * 1000);
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json' };

function serve(){
  const server = createServer(async (req, res) => {
    const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
    try {
      const body = await readFile(join(ROOT, path || 'index.html'));
      res.writeHead(200, { 'Content-Type': TYPES[extname(path)] || 'application/octet-stream' });
      res.end(body);
    } catch {
      res.writeHead(404); res.end('not found');
    }
  });
  return new Promise(ok => server.listen(0, '127.0.0.1', () => ok(server)));
}

const server = process.env.BASE_URL ? null : await serve();
const base = process.env.BASE_URL || `http://127.0.0.1:${server.address().port}/`;

const launch = { args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] };
if (process.env.CHROMIUM_PATH) launch.executablePath = process.env.CHROMIUM_PATH;
const browser = await chromium.launch(launch);
const page = await browser.newPage({ viewport: { width: 1280, height: 800 } });

let current = 'page load';
const failures = [];
page.on('pageerror', e => failures.push(`[${current}] ${e.message}`));
page.on('console', m => { if (m.type() === 'error') console.log(`  console (${current}): ${m.text().slice(0, 200)}`); });

let code = 0;
try {
  // ── 1. Fly ──
  current = 'fly';
  await page.goto(new URL('index.html', base).href, { waitUntil: 'load' });
  await page.click('#watch');
  await page.waitForTimeout(1000);
  await page.mouse.move(640, 400);
  await page.mouse.down();
  for (let i = 0; i <= 20; i++) await page.mouse.move(640 + i * 12, 400 + Math.round(Math.sin(i / 4) * 60), { steps: 2 });
  await page.mouse.up();
  for (let i = 0; i < 10; i++){ await page.mouse.wheel(0, -120); await page.waitForTimeout(100); }
  for (const k of ['ArrowUp', 'ArrowLeft', 'ArrowDown', 'ArrowRight']){
    await page.keyboard.down(k); await page.waitForTimeout(300); await page.keyboard.up(k);
  }
  await page.mouse.click(640, 400);              // a tap: goes round a body if one is under it
  await page.waitForTimeout(2000);
  console.log(`${failures.length ? 'FAIL' : 'ok  '} fly`);

  // ── 1b. the suns, planets and moons from res/*.tvf3d: they load, every system's star wears a sun and its planets
  //       planets lit by that star, and their shapes and colours reach the card ──
  current = 'bodies';
  const beforeB = failures.length;
  await page.waitForFunction(() => window.__bodies && (window.__bodies.BODIES.ready || window.__bodies.BODIES.failed), null, { timeout: 60000 });
  const bd = await page.evaluate(() => { const B = window.__bodies, L = B.bodies();
    return { failed: B.BODIES.failed, files: B.BODY_NAMES.length, loaded: B.BODIES.g.filter(Boolean).length,
             mx: Math.max(...B.BODIES.mx), coloured: B.BODIES.col.every(c => c.some((v, i) => i % 4 < 3 && v > 0)),
             n: L.length, worn: L.filter(o => o.si >= B.NSOLID).length,
             suns: L.filter(o => o.star && /^sun-/.test(o.name)).length, starsPlain: L.filter(o => o.star && !/^sun-/.test(o.name)).length,
             lit: L.filter(o => o.look === 'planet' && o.suns > 0).length, planets: L.filter(o => o.look === 'planet').length,
             // near and far: the ball plus its three relief bands give the whole radius back, the ball is round, and the
             // cratered moon has fine relief to show up close
             split: (() => { let worst = 0, round = 0; B.BODIES.bands.forEach((q, b) => { const g = B.BODIES.g[b];
                 for (let i = 0; i < g.length; i++){ const r = Math.max(0.004, q[4 * i] + q[4 * i + 1] + q[4 * i + 2] + q[4 * i + 3]); worst = Math.max(worst, Math.abs(r - g[i])); }
                 for (let i = 0; i < g.length; i += 192) round = Math.max(round, Math.abs(q[4 * i] - q[4 * (i + 96)])); });
               const luna = B.BODIES.bands[B.BODY_NAMES.indexOf('moon-luna')]; let fine = 0; for (let i = 3; i < luna.length; i += 4) fine = Math.max(fine, Math.abs(luna[i]));
               return { worst, round, fine }; })() }; });
  if (bd.failed) failures.push(`[bodies] did not load: ${bd.failed}`);
  if (bd.loaded !== bd.files) failures.push(`[bodies] ${bd.loaded} of ${bd.files} files read`);
  if (!bd.coloured) failures.push('[bodies] a body came out with no colour');
  if (!(bd.mx > 0.4 && bd.mx < 1)) failures.push(`[bodies] radius ${bd.mx}: not a body about half its height across`);
  if (!bd.n || bd.worn !== bd.n) failures.push(`[bodies] ${bd.worn} of ${bd.n} bodies wear their file`);
  if (!bd.suns || bd.starsPlain) failures.push(`[bodies] ${bd.suns} stars wear a sun, ${bd.starsPlain} do not`);
  if (!bd.planets || bd.lit !== bd.planets) failures.push(`[bodies] ${bd.lit} of ${bd.planets} planets know their star`);
  if (bd.split.worst > 1e-5) failures.push(`[bodies] the ball and its bands miss the radius by ${bd.split.worst}`);
  if (bd.split.round > 1e-6) failures.push(`[bodies] the ball under the relief is not round (${bd.split.round})`);
  if (!(bd.split.fine > 0.003)) failures.push(`[bodies] the moon has no fine relief to show up close (${bd.split.fine})`);
  await page.waitForTimeout(500);
  console.log(`${failures.length === beforeB ? 'ok  ' : 'FAIL'} bodies (${bd.files} files; ${bd.n} bodies held, ${bd.suns} suns, ${bd.planets} planets)`);

  // ── 1c. moving about (Oct 7: "i can't move to planets"): holding W gathers speed, letting go glides; a tap beside a small
  //       planet takes it; going round it brings it in to about 40° across, and zooming in brings it nearer still ──
  current = 'moving';
  const beforeM = failures.length;
  await page.keyboard.press('Escape');
  const w0 = await page.evaluate(() => __wanderLab.where());
  await page.keyboard.down('w');
  await page.waitForFunction(t0 => __wanderLab.where().t > t0 + 2.6, w0.t, { timeout: 120000, polling: 100 });
  const w1 = await page.evaluate(() => __wanderLab.where());
  await page.waitForFunction(t1 => __wanderLab.where().t > t1 + 0.4, w1.t, { timeout: 60000, polling: 100 });
  const w2 = await page.evaluate(() => __wanderLab.where());
  await page.keyboard.up('w');
  const fast = Math.hypot(w2.x - w1.x, w2.y - w1.y, w2.z - w1.z) / (w2.t - w1.t);
  if (!(fast > 20)) failures.push(`[moving] after 2.6 s held, flying at ${fast.toFixed(1)} a second (it starts at 5 and should reach 30)`);
  await page.waitForFunction(t2 => __wanderLab.where().t > t2 + 0.3, w2.t, { timeout: 60000, polling: 100 });
  const w3 = await page.evaluate(() => __wanderLab.where()), glide = Math.hypot(w3.x - w2.x, w3.y - w2.y, w3.z - w2.z);
  if (!(glide > 0.5)) failures.push(`[moving] letting go stopped dead (moved ${glide.toFixed(2)} after)`);
  await page.waitForTimeout(800);
  // the tap lands 10 px beside the target: pick one with no other drawn body near that point, so the tap is its alone.
  // A planet, as the step says, not any small body: a solid's closest approach is read from its span, so a tall one (the
  // knight) is already held there once its approach settles, and zooming has no room left to bring it in (measured:
  // 1.94 settled, nearest 2.07 after zooming). Five to seven planets were in reach in every run measured.
  const tgt = await page.evaluate(() => { const all = __wanderLab.drawn();
    return all.filter(o => !o.star && /^planet-/.test(o.name) && o.r > 2 && o.r < 10 && o.y > 80 && o.y < 650 && o.x > 100 && o.x < 1180)
      .sort((a, b) => b.r - a.r)
      .find(o => all.every(b => b === o || Math.hypot(b.x - (o.x + o.r + 10), b.y - o.y) > b.r + 25)); });
  if (!tgt) failures.push('[moving] no small planet in view to tap');
  else {
    await page.mouse.click(tgt.x + tgt.r + 10, tgt.y);   // beside it, not on it
    await page.waitForTimeout(300);
    const o = await page.evaluate(() => __wanderLab.where());
    if (!o.orbit || o.name !== tgt.name) failures.push(`[moving] a tap beside ${tgt.name} took ${o.orbit ? o.name : 'nothing'}`);
    else {
      // it comes in at a capped rate, read from arrivals that lag: allow up to 15 s of the world's clock, not a fixed 5
      await page.waitForFunction(t => { const w = __wanderLab.where(); return w.span > 0.6 || w.t > t + 15; }, o.t, { timeout: 300000, polling: 200 });
      const w5 = await page.evaluate(() => __wanderLab.where()), s1 = w5.span;
      if (!(s1 > 0.5)) failures.push(`[moving] ${(w5.t - o.t).toFixed(1)} s after tapping, ${tgt.name} spans only ${s1.toFixed(2)} (it should come in to about 0.7)`);
      // zooming in brings it nearer. Read by its distance, not its span: a solid's span swings as it turns (the knight's
      // read 1.48 and 1.92 once its approach had settled, then about 1.05 after zooming), and very near the span is not a
      // steady reading at all (it spiked to 77).
      // Let the approach settle first. It overshoots, passing the distance it holds (2.1 against 3.5, measured) and then
      // backing out (it steers on arrivals, which lag), so a reading taken on the way in is no baseline (Oct 11: 0.85 to
      // 0.94 across on CI, with the zoom working). The zoom overshoots in the same way, so take the nearest it comes in
      // 3 s, not where it is at the end: measured on planets, 0.23 to 0.50 of the settled distance, at full speed and with
      // the CPU 4 and 8 times slower.
      await page.waitForFunction(t => __wanderLab.where().t > t + 4, w5.t, { timeout: 180000, polling: 200 });
      const d0 = (await page.evaluate(() => __wanderLab.where())).dist;
      for (let i = 0; i < 10; i++){ await page.mouse.wheel(0, -200); await page.waitForTimeout(60); }
      const z0 = (await page.evaluate(() => __wanderLab.where())).t;
      await page.evaluate(() => { window.__nearest = Infinity; });
      await page.waitForFunction(t => { const w = __wanderLab.where(); if (w.dist != null) window.__nearest = Math.min(window.__nearest, w.dist); return w.t > t + 3; }, z0, { timeout: 180000, polling: 100 });
      const dMin = await page.evaluate(() => window.__nearest);
      if (!(d0 > 0 && dMin < 0.75 * d0)) failures.push(`[moving] zooming in took ${tgt.name} only from ${d0 == null ? '?' : d0.toFixed(2)} to ${dMin.toFixed(2)} away (settled, then nearest in 3 s)`);
    }
  }
  await page.keyboard.press('Escape');
  console.log(`${failures.length === beforeM ? 'ok  ' : 'FAIL'} moving (${fast.toFixed(0)} a second held${tgt ? ', a tap beside ' + tgt.name : ''})`);

  // ── 2. Every lab ──
  current = 'labs';
  const before = failures.length;
  await page.goto(new URL('labs.html?lab=all', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => /labs not killed/.test(document.getElementById('labStatus').textContent),
                             null, { timeout: LAB_TIMEOUT_MS, polling: 500 });
  const rows = await page.evaluate(() => [...document.querySelectorAll('#labBody table tr')].slice(1)
    .map(tr => [...tr.children].map(td => td.textContent.trim()))
    .map(c => ({ lab: c[0], verdict: c[4], secs: c[5] })));
  for (const r of rows){
    const bad = !/^(not killed|killed)$/i.test(r.verdict);
    if (bad) failures.push(`[lab ${r.lab}] latest run: ${r.verdict}`);
    console.log(`${bad ? 'FAIL' : 'ok  '} lab ${r.lab.padEnd(4)} ${r.verdict} (${r.secs}s)`);
  }
  if (!rows.length) failures.push('[labs] the summary table had no rows');
  console.log((await page.textContent('#labStatus')).split('.')[0] + '.');
  if (failures.length !== before) console.log('FAIL labs');

  // ── 3. labs.html: every lab has a card, one runs from its button, and index.html?lab= forwards here ──
  current = 'labs.html';
  const before3 = failures.length;
  await page.goto(new URL('labs.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => !document.getElementById('runAll').disabled, null, { timeout: 30000 });
  const cards = await page.$$eval('article.lab', a => a.map(x => x.id));
  if (cards.length !== rows.length) failures.push(`[labs.html] ${cards.length} cards, but ?lab=all ran ${rows.length} labs`);
  await page.click('#bal button');
  await page.waitForFunction(() => !/^(not run|running…)$/.test(document.querySelector('#bal .verdict').textContent),
                             null, { timeout: 120000, polling: 250 });
  const v = await page.textContent('#bal .verdict');
  if (!/^(not killed|killed)$/.test(v)) failures.push(`[labs.html] BAL came back: ${v}`);
  await page.goto(new URL('index.html?lab=bal', base).href, { waitUntil: 'load' });
  await page.waitForURL(/labs\.html\?lab=bal/, { timeout: 15000 });
  await page.waitForFunction(() => /(KILLED|[Nn]ot killed)/.test(document.getElementById('labStatus').textContent), null, { timeout: 120000 });
  console.log(`${failures.length === before3 ? 'ok  ' : 'FAIL'} labs.html (${cards.length} cards; BAL ${v}; index.html?lab= forwards)`);

  // ── 4. sweep.html: the sweep device loads, lays every example, and sweeps ──
  current = 'sweep.html';
  const before4 = failures.length;
  const laid = [];
  for (const ex of ['planets', 'shape', 'spread', 'line']){
    await page.goto(new URL('sweep.html?ex=' + ex, base).href, { waitUntil: 'load' });
    const n = await page.evaluate(() => window.sweepItems().filter(i => i.g >= 0 && i.g <= 1).length);
    if (!n) failures.push(`[sweep.html] ${ex}: nothing laid on the sweep`);
    laid.push(`${ex} ${n}`);
  }
  await page.click('#play'); await page.waitForTimeout(1500);
  console.log(`${failures.length === before4 ? 'ok  ' : 'FAIL'} sweep.html (${laid.join(', ')})`);

  // ── 5. dial.html: the h dial; a sure "two" costs (1 + s)·max(1, 1/s), least at the corner ──
  current = 'dial.html';
  const before5 = failures.length;
  await page.goto(new URL('dial.html?s=0.5', base).href, { waitUntil: 'load' });
  const dc = await page.evaluate(() => [0.5, 1, 2].map(x => __dial.meanCost(x, 4000)));
  if (!(Math.abs(dc[1] - 2) < 1e-9 && Math.abs(dc[0] - 3) < 0.3 && Math.abs(dc[2] - 3) < 1e-9 && dc[1] < dc[0]))
    failures.push(`[dial.html] costs at s = 0.5, 1, 2: ${dc.map(c => c.toFixed(2)).join(', ')} (want about 3, 2, 3)`);
  await page.click('#look'); await page.click('#measure');
  console.log(`${failures.length === before5 ? 'ok  ' : 'FAIL'} dial.html (cost ${dc.map(c => c.toFixed(2)).join(' / ')} at s = 0.5 / 1 / 2)`);

  // ── 6. sphere.html: the address loses the scale; the octant's area is π/2; far off the body is a plain ball ──
  current = 'sphere.html';
  const before6 = failures.length;
  await page.goto(new URL('sphere.html?map=reader', base).href, { waitUntil: 'load' });
  const sp = await page.evaluate(() => { const s = __sphere, a = s.address(0.2, 0.4, 0.6), b = s.address(0.02, 0.04, 0.06);
    return { same: a.every((x, i) => Math.abs(x - b[i]) < 1e-12), area: s.octantArea(), ch: s.chamber([0.2, 0.4, 0.6]),
      face: s.face([0.9, 0.2, 0.3]), rd: s.reader([0.9, 0.3, 0.7]), far: s.bandW(2), near: s.bandW(600) }; });
  if (!sp.same) failures.push('[sphere.html] the address changes with the scale');
  if (Math.abs(sp.area - Math.PI / 2) > 1e-3) failures.push(`[sphere.html] octant area ${sp.area} (want π/2)`);
  if (sp.ch !== 'v < h < f' || sp.face !== 'v' || sp.rd !== 'far in both') failures.push(`[sphere.html] ${sp.ch} / ${sp.face} / ${sp.rd}`);
  if (sp.far.some(w => w > 0) || sp.near.some(w => w < 1)) failures.push(`[sphere.html] bands far ${sp.far}, near ${sp.near}`);
  await page.click('[data-m="chambers"]'); await page.click('[data-p="1,1,1"]'); await page.waitForTimeout(300);
  console.log(`${failures.length === before6 ? 'ok  ' : 'FAIL'} sphere.html (octant area ${sp.area.toFixed(4)}, scale lost, bands off far and on near)`);

  // ── 8. thin.html: grains lit × brightest grain = light caught, 1/v² everywhere; the switch at one grain across ──
  current = 'thin.html';
  const before8 = failures.length;
  await page.goto(new URL('thin.html?v=400', base).href, { waitUntil: 'load' });
  const th = await page.evaluate(() => { const t = __thin, n = t.at(10), f = t.at(1000), f2 = t.at(2000), c = t.at(t.dstar * 1.0001);
    return { nPeak: n.peak, nLit: n.lit, fLit: f.lit, ratio: f2.total / f.total, fall: f.peak / f2.peak, prod: f.lit * f.peak / f.total, c: c.A, sum: t.sphereSum(123) }; });
  if (th.nPeak !== 1 || th.nLit <= 1) failures.push(`[thin.html] near: peak ${th.nPeak}, lit ${th.nLit}`);
  if (th.fLit !== 1 || Math.abs(th.fall - 4) > 0.01) failures.push(`[thin.html] far: lit ${th.fLit}, dims by ${th.fall} per doubling`);
  if (Math.abs(th.ratio - 0.25) > 0.001 || Math.abs(th.prod - 1) > 1e-9 || Math.abs(th.c - 1) > 0.01 || th.sum !== 1) failures.push(`[thin.html] ${JSON.stringify(th)}`);
  console.log(`${failures.length === before8 ? 'ok  ' : 'FAIL'} thin.html (near ${th.nLit.toFixed(1)} grains at full brightness; far one grain, dimming 4× per doubling)`);

  // ── 9. ladder.html: parallax gives out first, then width; light reads past both ──
  current = 'ladder.html';
  const before9 = failures.length;
  await page.goto(new URL('ladder.html?D=30000', base).href, { waitUntil: 'load' });
  const ld = await page.evaluate(() => { const L = __ladder, a = L.at(2000, false), b = L.at(30000, false), c = L.at(400000, false), d = L.at(1e7, true);
    return { a: [a.plx.read !== null, a.wid.read !== null], b: [b.plx.read === null, b.wid.read !== null], c: [c.wid.read === null, c.lit.off === 0], d: d.lit.read === null }; });
  if (!ld.a.every(Boolean) || !ld.b.every(Boolean) || !ld.c.every(Boolean) || !ld.d) failures.push(`[ladder.html] ${JSON.stringify(ld)}`);
  await page.click('#photons'); await page.waitForTimeout(100);
  console.log(`${failures.length === before9 ? 'ok  ' : 'FAIL'} ladder.html (parallax out by 30,000, width by 400,000, light past both)`);

  // ── 10. sky.html: the lit share follows 1 − e^(−L/λ); always been, the whole sky ──
  current = 'sky.html';
  const before10 = failures.length;
  await page.goto(new URL('sky.html?L=1', base).href, { waitUntil: 'load' });
  const sk = await page.evaluate(() => { const s = __sky; return { r: [0.25, 0.5, 1, 2].map(L => s.share(L) - s.pred(L)), all: s.share(Infinity) }; });
  if (sk.r.some(d => Math.abs(d) > 0.01) || sk.all !== 1) failures.push(`[sky.html] ${JSON.stringify(sk)}`);
  await page.click('#always'); await page.waitForTimeout(100);
  console.log(`${failures.length === before10 ? 'ok  ' : 'FAIL'} sky.html (share within ${Math.max(...sk.r.map(Math.abs)).toFixed(4)} of 1 − e^(−L/λ); always been, all lit)`);

  // ── 11. gameplay sketches: each page's one mechanic, through its hook ──
  current = 'play-*.html';
  const before11 = failures.length;
  await page.goto(new URL('play-points.html', base).href, { waitUntil: 'load' });
  const pp = await page.evaluate(() => ({ dim: __points.shade(0.25, 'dim').alpha, van: __points.shade(0.25, 'vanish').kind, pix: __points.shade(0.25, 'pixel').alpha, disc: __points.shade(2, 'dim').kind }));
  if (Math.abs(pp.dim - 0.25) > 1e-9 || pp.van !== 'none' || pp.pix !== 1 || pp.disc !== 'disc') failures.push(`[play-points.html] ${JSON.stringify(pp)}`);
  await page.goto(new URL('play-resolve.html', base).href, { waitUntil: 'load' });
  const pr = await page.evaluate(() => [0.2, 0.6, 7, 30, 100].map(p => __resolve.stageOf(p)));
  if (pr.join() !== '0,1,2,3,4') failures.push(`[play-resolve.html] stages ${pr}`);
  await page.goto(new URL('play-ladder.html', base).href, { waitUntil: 'load' });
  const pl = await page.evaluate(() => { const g = __navigator, a = g.measure(0, 'parallax'), far = g.measure(8, 'parallax'), lockd = g.measure(8, 'light');
    g.use(0, 'parallax'); g.log(0); const lit = g.measure(8, 'light'), wid = g.measure(8, 'width');
    return { a: a.D, far: far.D, lockd: lockd.D, lit: lit.D, wid: wid.D, learned: !!g.learned().A }; });
  if (!(pl.a > 0) || pl.far !== null || pl.lockd !== null || !pl.learned || !(Math.abs(pl.lit / 800000 - 1) < 0.25) || pl.wid !== null) failures.push(`[play-ladder.html] ${JSON.stringify(pl)}`);
  await page.goto(new URL('play-sky.html', base).href, { waitUntil: 'load' });
  const ps = await page.evaluate(() => { const s = __skyfill, k = s.arrived(10); return { k, exp: s.expected(10), back: s.timeFromCount(k), none: s.arrived(0.1), all: s.arrived(1000) }; });
  if (Math.abs(ps.k - ps.exp) > 3 * Math.sqrt(ps.exp) || Math.abs(ps.back / 10 - 1) > 0.1 || ps.none !== 0 || ps.all !== 1500) failures.push(`[play-sky.html] ${JSON.stringify(ps)}`);
  await page.goto(new URL('play-corner.html', base).href, { waitUntil: 'load' });
  const pc = await page.evaluate(() => { const c = __corner, cut = (f, d) => Math.abs(c.cutOf(f, d));
    const L = c.current(); c.aim(c.fFor(L.phi));
    return { near: cut(1, 3), far: cut(1, 30), full: cut(0, 7), graze: cut(2 - 1e-9, 5), miss: c.cutOf(2.1, 5), res: c.shoot() }; });
  if (Math.abs(pc.near - 30) > 1e-9 || Math.abs(pc.far - 30) > 1e-9 || pc.full !== 0 || Math.abs(pc.graze - 90) > 0.01 || pc.miss !== null || pc.res !== 'potted') failures.push(`[play-corner.html] ${JSON.stringify(pc)}`);
  await page.goto(new URL('play-trick.html', base).href, { waitUntil: 'load' });
  const pt = await page.evaluate(() => { const T = __trick, o = {};
    T.setLayout('rack'); T.aim(0); const s1 = T.preview(), s2 = T.preview();
    o.same = s1.frames.length === s2.frames.length && s1.frames.every((f, k) => f.every((x, i) => Object.is(x, s2.frames[k][i])));
    o.full = s1.first && s1.first.n === 1 && s1.first.overlap > 0.999;
    o.hv = s1.contacts.length > 0 && s1.contacts.every(c => c.hv >= 1 && c.hv < 1.05);
    const fin = s1.final, after = T.shootNow();
    o.plays = after.every((b, i) => b.n === 0 ? true : b.sunk === fin[i].sunk && (b.sunk || (b.x === fin[i].x && b.z === fin[i].z)));
    // contact found exactly on h + v = 1 (POL run 9), except where a cluster's pushes within one tick left a pair already
    // overlapping (the old push): a few, and those within 1%
    const off = s1.contacts.filter(c => Math.abs(c.hvC - 1) >= 1e-9);
    o.exact = off.length <= 0.05 * s1.contacts.length && off.every(c => Math.abs(c.hvC - 1) < 0.01);
    T.setLayout('line'); o.combo = T.preview().sunk.map(p => p.n).join(); o.sight = T.seen(3).join() + '/' + T.seen(4).join();
    const rt = T.roundTrip(3, -2); o.rt = Math.hypot(rt[0] - 3, rt[1] + 2) < 1e-9;
    // the strike: the tip meets the white on h + v = 1 where chosen on its face; bare, it turns the white sin φ = fx (30° at ½);
    // chalked, inside the grip, the white stays on the cue's line and takes spin; the textbook results of spin on this engine
    const b30 = T.strikeOf(0, 0.5, 0, 14, 0), bl = T.strikeOf(0, -0.5, 0, 14, 0), g = T.strikeOf(0, 0.3, 0.2, 14, T.MU_TIP), sc = T.spinChecks();
    o.strike = T.strikeOf(0, 0, 0).dir === 0 && Math.abs(b30.turn + 30) < 1e-9 && Math.abs(bl.turn - 30) < 1e-9 && b30.w.every(x => Math.abs(x) < 1e-9) && g.grip && g.turn === 0 && g.w[1] > 0;
    o.spin = { roll: sc.rollSlip < 1e-9, follow: Math.abs(sc.follow - sc.followPred) < 0.005, stun: Math.abs(sc.stun) < 0.05, draw: sc.draw < 0.5, english: sc.englishVx * sc.rightX > 0.3, miscue: !sc.miscue.grip && sc.miscue.turn < 0 && sc.miscue.turn > -44.5,
      cutThrow: sc.cutThrow > 0.5 && sc.cutThrow < 4.5, sideThrow: sc.sideThrow < -0.3 && sc.sideThrow > -4.5, passed: sc.passed < 0, masse: Math.abs(sc.masseBend) > 10, jump: sc.jumpCleared && sc.jumpPeak > 2 * 0.45,
      followGrip: sc.followGrip < sc.followPred - 0.01 && sc.followGrip > 0.15, backspinPassed: sc.backspinPassed > 0, offTable: sc.offTable };
    o.spinOK = Object.values(o.spin).every(Boolean);
    // challenges: each missed as set up and solved by its reference shot (a layout or engine change can break one);
    // a missed try puts the balls back and says why, a solved one is counted
    o.chFail = T.challenges.map(c => { T.setChallenge(c.id); const start = T.check(); T.solve(); const sol = T.check();
      return start !== null && sol === null ? null : `${c.id}: as set up ${start}, reference ${sol}`; }).filter(Boolean);
    T.setChallenge('combo'); const b0 = JSON.stringify(T.challenge().balls); T.shootNow(); const miss = T.challenge();
    T.solve(); T.shootNow(); const hit = T.challenge();
    o.chTries = miss.tries === 1 && !!miss.lastWhy && JSON.stringify(miss.balls) === b0 && hit.tries === 2 && hit.solvedIn === 2 && hit.lastWhy === null && JSON.stringify(hit.balls) === b0;
    // the throw challenge is the grip's (CUE run 2): with the balls' grip off, its reference shot misses
    T.setChallenge('throw'); T.solve(); T.grip(0); o.throwNeedsGrip = T.check() !== null; T.grip(null); o.throwSolves = T.check() === null;
    T.setLayout('rack'); o.chOff = T.challenge() === null; return o; });
  if (!pt.same || !pt.full || !pt.hv || !pt.exact || !pt.plays || pt.combo !== '4' || pt.sight !== '/4' || !pt.rt || !pt.strike || !pt.spinOK || pt.chFail.length || !pt.chTries || !pt.chOff || !pt.throwNeedsGrip || !pt.throwSolves) failures.push(`[play-trick.html] ${JSON.stringify(pt)}`);
  // play and feel: a shot played through (not jumped to its end) sounds the cue's tap, each ball on ball and each pocket;
  // and pulling the strip down and letting go shoots
  {
    await page.evaluate(() => { const T = __trick; T.sound(true); T.setChallenge('half'); T.solve(); });
    await page.click('#shoot');
    await page.waitForFunction(() => !__trick.playing(), null, { timeout: 60000, polling: 100 });
    const snd = await page.evaluate(() => __trick.heard());
    if (!(snd.cue === 1 && snd.ball >= 1 && snd.pocket >= 1)) failures.push(`[play-trick.html] a shot played through was not heard: ${JSON.stringify(snd)}`);
    await page.evaluate(() => { __trick.setLayout('rack'); });
    const box = await page.locator('#pull').boundingBox(), s0 = await page.evaluate(() => __trick.state().shots);
    await page.mouse.move(box.x + box.width / 2, box.y + 10); await page.mouse.down();
    await page.mouse.move(box.x + box.width / 2, box.y + box.height * 0.5, { steps: 6 });
    const pw = await page.evaluate(() => __trick.state().power); await page.mouse.up();
    const s1 = await page.evaluate(() => __trick.state().shots);
    if (!(s1 === s0 + 1 && pw > 20 && pw < 40)) failures.push(`[play-trick.html] pulling the strip half way did not shoot at middling power (shots ${s0} to ${s1}, power ${pw})`);
    await page.waitForFunction(() => !__trick.playing(), null, { timeout: 60000, polling: 100 });
  }
  console.log(`${failures.length === before11 ? 'ok  ' : 'FAIL'} gameplay sketches (far lights, resolving, the navigator's ladder, the sky fills, aiming from the cue ball, trick shots)`);

  // ── 12. facing.html: the facing is 2θ, square to the line at the corner, the arc off the line most there ──
  current = 'facing.html';
  const before12 = failures.length;
  await page.goto(new URL('facing.html?t=45', base).href, { waitUntil: 'load' });
  const fc = await page.evaluate(() => { const f = __facing; return { c: f.at(45), a: f.at(0), b: f.at(90), q: f.at(30) }; });
  if (Math.abs(fc.c.facing - 90) > 1e-9 || Math.abs(fc.c.ratio - 1) > 1e-9 || Math.abs(fc.c.share - 0.5) > 1e-9 ||
      Math.abs(fc.c.offLine - (1 - Math.SQRT1_2)) > 1e-9 || fc.a.facing !== 0 || fc.b.facing !== 180 || !(fc.q.offLine < fc.c.offLine))
    failures.push(`[facing.html] ${JSON.stringify(fc)}`);
  console.log(`${failures.length === before12 ? 'ok  ' : 'FAIL'} facing.html (facing 90° at the corner, 0° at A, 180° at B; off the line ${fc.c.offLine.toFixed(3)} there)`);

  // ── 13. levels.html: the near field in proportion, each doubling past the corner in half the room, rings seen to one grain ──
  current = 'levels.html';
  const before13 = failures.length;
  // the reader's lay (default since 11 Oct, SPN Prop 1.2 (g)): every doubling past the corner ln 2 wide, no edge
  await page.goto(new URL('levels.html', base).href, { waitUntil: 'load' });
  const lg = await page.evaluate(() => { const L = __levels; return { lay: L.lay, c: L.radius(1), w: [0, 1, 2, 3].map(k => L.level(k).width),
    r8: L.radius(8), back: L.reading(L.radius(8)), n: L.visible(L.R(), 1) }; });
  if (lg.lay !== 'log' || lg.c !== 1 || lg.w.some(w => Math.abs(w - Math.LN2) > 1e-12) || Math.abs(lg.r8 - (1 + Math.log(8))) > 1e-12 ||
      Math.abs(lg.back - 8) > 1e-9 || lg.n !== 6) failures.push(`[levels.html, the reader's lay] ${JSON.stringify(lg)}`);
  console.log(`${failures.length === before13 ? 'ok  ' : 'FAIL'} levels.html, the reader's lay (every doubling ${lg.w[0].toFixed(4)} wide; s = 8 at ${lg.r8.toFixed(4)}; ${lg.n} levels drawn)`);
  // the in-place lay, kept at ?lay=inplace: each doubling half the last, the horizon at 2
  await page.goto(new URL('levels.html?lay=inplace', base).href, { waitUntil: 'load' });
  const lv = await page.evaluate(() => { const L = __levels, R = L.R();
    return { R, half: L.radius(0.5), c: L.radius(1), w: [0, 1, 2, 3].map(k => L.level(k).width), r8: L.radius(8), back: L.reading(L.radius(8)),
      v1: L.visible(R, 1), v2: L.visible(R, 2), v1k: L.visible(1024, 1),
    lod3: L.lodRadius(3), cross: L.crossings(4), broad: L.crossings(4, L.BROAD),
    meanDepth: [...Array(1000)].reduce((z, _, i) => z + L.depth(2 * Math.PI * i / 1000), 0) / 1000,
    depthAt: L.depth(1) - Math.log2(L.shape(1, 4) / 4) }; });
  if (lv.half !== 0.5 || lv.c !== 1 || lv.w.some((w, k) => Math.abs(w - 2 ** (-k - 1)) > 1e-12) || Math.abs(lv.r8 - 1.875) > 1e-12 ||
      Math.abs(lv.back - 8) > 1e-9 || lv.v1 - lv.v2 !== 1 || lv.v1k !== 10 || Math.abs(lv.v1 - Math.log2(lv.R)) > 1 ||
      lv.lod3 !== 1.875 || !(lv.cross >= 6) || !(lv.broad < lv.cross) || Math.abs(lv.meanDepth) > 1e-9 || Math.abs(lv.depthAt) > 1e-12)
    failures.push(`[levels.html] ${JSON.stringify(lv)}`);
  console.log(`${failures.length === before13 ? 'ok  ' : 'FAIL'} levels.html?lay=inplace (each level half the last; ${lv.v1} seen at a one-pixel grain, one fewer at two; the shape crosses ${lv.cross} ring edges, its broad form ${lv.broad}; size divided out, the depth averages 0 on the corner)`);
  // a body from res/ chosen in the combo box, and a file that is not a .tvf refused
  const lb = await page.evaluate(async () => { const L = __levels; await L.choose('res:asteroid-grey');
    let refused = false; try { L.parseTVF('hello'); } catch (e) { refused = true; }
    let z = 0; for (let i = 0; i < 1000; i++) z += L.depth(2 * Math.PI * i / 1000);
    const N = 64, X = [], Y = []; for (let k = 0; k < N; k++) { const p = (k + 0.5) * 2 * Math.PI / N, r = 100 * (1 + 0.45 * Math.cos(5 * p)); X.push(300 + r * Math.cos(p)); Y.push(300 - r * Math.sin(p)); }
    const C = L.parseTVF(['TVF 64 1 2', '#meta name:star', '-1 ' + X.join(' '), '-1 ' + Y.join(' ')].join('\n'));
    const at = th => C.Aa[0].reduce((z, a, m) => z + a * Math.cos(m * th) + C.Ab[0][m] * Math.sin(m * th), 0);
    let oneCh = false; try { L.parseTVF('TVF 16 1 1\n-1 ' + Array(16).fill(0.5).join(' ')); } catch (e) { oneCh = true; }
    return { name: L.shapeName(), cross: L.crossings(4), meanDepth: z / 1000, refused, curve: C.curve, tip: at(0), dip: at(Math.PI / 5), oneCh }; });
  if (lb.name !== 'asteroid grey' || !(lb.cross > 0) || Math.abs(lb.meanDepth) > 1e-3 || !lb.refused || !lb.curve || Math.abs(lb.tip / lb.dip - 145 / 55) > 0.05 || !lb.oneCh) failures.push(`[levels.html, a body] ${JSON.stringify(lb)}`);
  console.log(`${failures.length === before13 ? 'ok  ' : 'FAIL'} levels.html, a body from res/ (${lb.name}: crosses ${lb.cross} ring edges at s₀ = 4; a non-.tvf file refused; a draw .tvf curve read from its centroid, tip/dip ${(lb.tip / lb.dip).toFixed(3)} of 2.636)`);

  // ── 14. walk.html: the sweep as my walk to you: 45° at d = V, levels doubling in steps, the near side in proportion ──
  current = 'walk.html';
  const before14 = failures.length;
  await page.goto(new URL('walk.html?d=40', base).href, { waitUntil: 'load' });
  const wk = await page.evaluate(() => { const w = __walk, V = w.V;
    return { V, c: w.at(V), far: w.at(4 * V), near: w.at(V / 4), costs: [0, 1, 2, 3].map(w.levelCost),
      cot: [10, 30, 45, 60, 80].map(t => w.stepsLeftAt(t) - V / Math.tan(t * Math.PI / 180)), lt: w.levelTheta(1) }; });
  if (Math.abs(wk.c.theta - 45) > 1e-9 || wk.c.h !== 1 || wk.c.v !== 1 || wk.far.h !== 1 || Math.abs(wk.far.v - 0.25) > 1e-12 ||
      wk.near.v !== 1 || Math.abs(wk.near.h - 0.25) > 1e-12 || Math.abs(wk.far.stepsLeft - 4 * wk.V) > 1e-9 ||
      wk.costs.some((c, k) => c !== wk.V * 2 ** k) || wk.cot.some(x => Math.abs(x) > 1e-9) || Math.abs(wk.lt - Math.atan(0.5) * 180 / Math.PI) > 1e-9)
    failures.push(`[walk.html] ${JSON.stringify(wk)}`);
  console.log(`${failures.length === before14 ? 'ok  ' : 'FAIL'} walk.html (45° at d = V; far, v fills against a full h; near, h empties; steps per level ${wk.costs.join(', ')}; steps left V·cot θ)`);

  // ── 15. pool.html: contact read from inside is h + v = 1, and the game from inside is the referee's ──
  current = 'pool.html';
  const before15 = failures.length;
  await page.goto(new URL('pool.html', base).href, { waitUntil: 'load' });
  const pq = await page.evaluate(() => { const r = __pool.run(4, { seconds: 3 }), e = __pool.run(4, { seconds: 3, heavy: false }), w = __pool.run(2, { seconds: 3, walls: 'inside' }),
    ln = __pool.runLate(4, { c: 50, mode: 'naive', seconds: 1 }), lc = __pool.runLate(4, { c: 50, mode: 'carry', seconds: 1 }),
    fd = __pool.runField(1, { seconds: 1 }); return { r, e, w, ln, lc, fd }; });
  if (pq.r.p1bad || pq.r.p2bad || pq.e.p3wrong || !(pq.r.p3wrong > 0) || !(pq.r.contacts > 5) || !(pq.r.diffAtFirst < 1e-9) || pq.r.diverge != null ||
      pq.w.p6bad || pq.w.p7bad || !(pq.w.p6checks > 0) || pq.w.firstRail == null || !(pq.w.diffAtRail < 1e-9) || pq.w.diverge != null ||
      !(pq.lc.E < pq.ln.E / 4) || !pq.fd.E.every(x => x < 1e-6))
    failures.push(`[pool.html] ${JSON.stringify(pq)}`);
  console.log(`${failures.length === before15 ? 'ok  ' : 'FAIL'} pool.html (${pq.r.contacts} contacts, every one on h + v = 1; cushions read as the ball's own mirror image; from inside and from nowhere the same game)`);

  // ── 16. flight.html: the corner keeps its row at any height; by v/h the levels keep theirs and hold equal counts ──
  current = 'flight.html';
  const before16 = failures.length;
  await page.goto(new URL('flight.html?still=1', base).href, { waitUntil: 'load' });
  const fl = await page.evaluate(() => { const f = __flight, out = {};
    f.set(50, 'vh'); out.c1 = f.cornerRow(); out.e1 = f.edgeRows(); out.n = f.linesPerLevel();
    f.set(1600, 'vh'); out.c2 = f.cornerRow(); out.e2 = f.edgeRows().slice(0, out.e1.length - 1);
    f.set(50, 'metres'); out.m1 = f.edgeRows()[0]; f.set(1600, 'metres'); out.m2 = f.edgeRows()[0];
    const F = f.focal(), rec = (h) => f.recoverAt(h, 0.3 * h, 0.8, F);
    out.exact = f.recoverAt(5, 1.2, 0.7, 0); out.near = rec(2); out.mid = rec(8); out.far = rec(400);
    out.lay = [0.5, 1, 2, 4, 8].map(x => f.layR(x));
    const at = (m) => [0.1, 0.5, 1, 2, 100].map(x => f.stripAt(x, m)); out.sf = at('folded'); out.sh = at('h/v'); out.sv = at('v/h'); return out; });
  if (Math.abs(fl.c1 - fl.c2) > 1e-9 || fl.e2.some((y, i) => Math.abs(y - fl.e1[i]) > 1e-9) ||
      fl.n.some(n => Math.abs(n - 8) > 1e-9) || Math.abs(fl.e1[0] - fl.c1) > 1e-9 ||
      !(Math.abs(fl.m1 - fl.m2) > 0.01) ||
      Math.abs(fl.exact.h - 5) > 1e-9 || Math.abs(fl.exact.x - 1.2) > 1e-9 || Math.abs(fl.exact.y - 0.7) > 1e-9 ||
      !(Math.abs(fl.near.h - 2) < 0.2) || !(Math.abs(fl.mid.h - 8) > Math.abs(fl.near.h - 2)) || fl.far.bearing === undefined ||
      Math.abs(fl.lay[0] - 0.5) > 1e-12 || fl.lay[1] !== 1 || Math.abs((fl.lay[3] - fl.lay[2]) - (fl.lay[4] - fl.lay[3])) > 1e-12 ||
      fl.sf.some(y => y < 0 || y > 1) || Math.abs(fl.sf[2] - 0.5) > 1e-9 || !(fl.sh[4] > 1) || !(fl.sh[0] >= 0) || !(fl.sv[0] < 0) || !(fl.sv[4] <= 1))
    failures.push(`[flight.html] ${JSON.stringify(fl)}`);
  console.log(`${failures.length === before16 ? 'ok  ' : 'FAIL'} flight.html (corner row ${fl.c1.toFixed(3)} at 50 m and 1.6 km; by v/h ${fl.n[1]} lines a level, the first edge the corner, edges fixed; by metres they slide; a post recovered exactly with no step, ${fl.near.h.toFixed(3)} for 2v and ${fl.mid.h === undefined ? 'a bearing' : fl.mid.h.toFixed(2)} for 8v at a pixel step, a bearing only at 400v; the lay true to the corner, each doubling past it ${(fl.lay[3] - fl.lay[2]).toFixed(3)} wide; strip folded holds 0.1v–100v, h/v runs off the top, v/h off the bottom)`);

  // ── 17. pool-infinite.html: a window of balls in a world of totals (POL runs 11–15): the books balance through steps and a
  //    pan, the window holds the world's density, the work does not grow with the world, and zooming out stops the window ──
  current = 'pool-infinite.html';
  const before17 = failures.length;
  await page.goto(new URL('pool-infinite.html', base).href, { waitUntil: 'load' });
  const pi = await page.evaluate(() => { const I = __infinite, o = {}; I.pause(true);
    const M = I.multiUniform(5, 6, 13, 13, 1), T0 = I.totals(M), ops = m => m.ops.moves + m.ops.pairs + m.ops.tries + m.ops.cells;
    for (let k = 0; k < 480; k++) I.multiStep(M, I.TICK);
    for (let st = 0; st < 16; st++) { I.setWindow(M, M.oi + (st < 8 ? 1 : -1), M.oj, 6); for (let k = 0; k < 4; k++) I.multiStep(M, I.TICK); }
    const T1 = I.totals(M); o.books = Math.abs(T1.N - T0.N) < 1e-6 && Math.hypot(T1.Px - T0.Px, T1.Py - T0.Py) < 1e-6 && Math.abs(T1.E / T0.E - 1) < 1e-9;
    o.density = M.B.n / (45 * 45) / I.N_DENS;
    const work = K => { const m = I.multiUniform(K, 6, 2 ** (K - 1) - 3, 2 ** (K - 1) - 3, 2); for (let k = 0; k < 240; k++) I.multiStep(m, I.TICK); return ops(m); };
    o.work = work(9) / work(5);
    I.setZoom(24); const wNear = I.page().M.w; I.setZoom(0.2); const P = I.page(); o.wFar = P.M.w; o.wNear = wNear; o.capped = P.M.w === P.windowFor && P.M.w < 48;
    return o; });
  if (!pi.books || !(Math.abs(pi.density - 1) < 0.2) || !(Math.abs(pi.work - 1) < 0.1) || !pi.capped || !(pi.wFar > pi.wNear)) failures.push(`[pool-infinite.html] ${JSON.stringify(pi)}`);
  console.log(`${failures.length === before17 ? 'ok  ' : 'FAIL'} pool-infinite.html (books balance through 2 s and a pan; the window at ${pi.density.toFixed(2)} of the world's density; work ×${pi.work.toFixed(3)} for a world 16 times wider; zoomed out the window stops at ${pi.wFar} cells)`);

  // ── 18. mountain.html: the worked example (OFS §10): the ends at the corner, the reader's view unchanged by scale,
  //    mountain equals thumb off by V/H, the walk of one thumb recovering the true distance and width ──
  current = 'mountain.html';
  const before18 = failures.length;
  await page.goto(new URL('mountain.html', base).href, { waitUntil: 'load' });
  const mt = await page.evaluate(() => { const m = __mountain, r = m.reading(20, 10), big = m.reading(20000, 10000), e = m.equalsThumb(20, 10), w = m.walk(20, 10);
    const vt = m.vantages(20, 10), vtBig = m.vantages(20000, 10000);
    m.set({ V: 20, d: 10, k: 1000, walk: true });
    return { r, big, e, w, vt, vtBig, hud: document.getElementById('hud').textContent.length > 0, lay: [m.lay(0.5), m.lay(10)] }; });
  if (Math.abs(mt.r.alpha - 45) > 1e-9 || mt.r.fingersOn !== 18 || Math.abs(mt.r.share - 0.5) > 1e-12 || !mt.r.atCorner ||
      Math.abs(mt.big.alpha - mt.r.alpha) > 1e-9 || mt.big.fingersOn !== mt.r.fingersOn ||
      mt.e.Vread !== 1 || Math.abs(mt.e.dRead - 0.5) > 1e-12 || mt.e.factor !== 20 || Math.abs(mt.e.doublings - Math.log2(20)) > 1e-12 ||
      Math.abs(mt.w.d - 10) > 1e-9 || Math.abs(mt.w.V - 20) > 1e-9 || Math.abs(mt.lay[1] - (1 + Math.log(10))) > 1e-12 || mt.lay[0] !== 0.5 || !mt.hud ||
      Math.abs(mt.vt.limb.product - 1) > 1e-15 || Math.abs(mt.vt.limb.innerFingers - 2 / Math.PI) > 1e-3 ||
      Math.abs(mt.vt.ends.outer - 1.1107207345) > 1e-9 || Math.abs(mt.vt.ends.product - 1) > 1e-15 || Math.abs(mt.vtBig.ends.outer - mt.vt.ends.outer) > 1e-12)
    failures.push(`[mountain.html] ${JSON.stringify(mt)}`);
  console.log(`${failures.length === before18 ? 'ok  ' : 'FAIL'} mountain.html (ends at ${mt.r.alpha.toFixed(1)}°, ${mt.r.fingersOn} of 36 fingers on the range, the same at ×1000; mountain = thumb reads 1 mi at ${mt.e.dRead} mi, off by ${mt.e.factor}, ${mt.e.doublings.toFixed(2)} doublings; one thumb walked recovers d = ${mt.w.d.toFixed(3)}, V = ${mt.w.V.toFixed(3)}; the two vantages on the thumb π/2 × ${mt.vt.limb.innerFingers.toFixed(4)} (2/π for every direction) = 1, to the ends ${mt.vt.ends.outer.toFixed(4)} × ${mt.vt.ends.inner.toFixed(4)} = 1, the same at ×1000)`);

  // ── 19. play-marbles.html: a bowl of 500 (MRB part 2's engine): the pour comes to rest in the bowl with the bowl and the
  //    table carrying the weight; the arc seen ahead ends at its first contact; a throw near the rim knocks marbles out and
  //    is heard; pulling the strip half way throws ──
  current = 'play-marbles.html';
  const before19 = failures.length;
  await page.goto(new URL('play-marbles.html', base).href, { waitUntil: 'load' });
  const mb = await page.evaluate(() => { const M = __marbles, g = M.game, w = M.world, o = {};
    o.pour = M.settleNow(300); let n = 0; for (let i = 0; i < M.NM; i++) if (w.on[i] && !g.out[i]) n++; o.inBowl = n;
    w.step(); o.held = (w.load.bowl + w.load.table) / w.weight();
    // the throw: at the heap's top 6 diameters from the middle, toward the eye, as hard as it goes
    const az = -Math.PI / 2, px = 6 * Math.cos(az), py = 6 * Math.sin(az); let zt = 0;
    for (let i = 0; i < w.N; i++) if (w.on[i] && Math.hypot(w.x[i] - px, w.y[i] - py) < 0.6) zt = Math.max(zt, w.z[i] + 0.5);
    const arc = M.arcOf([px, py, zt], 1), end = arc.pts[arc.pts.length - 1];
    let dmin = Infinity; for (let i = 0; i < M.NM; i++) if (w.on[i]) dmin = Math.min(dmin, Math.hypot(end[0] - w.x[i], end[1] - w.y[i], end[2] - w.z[i]));
    o.arcEnds = dmin < 1.05; o.reach = arc.reach;
    g.target = [px, py, zt]; const h0 = { ...M.heard }; M.throwAt(g.target, 1); o.after = M.settleNow(300); o.out = g.outs; o.throws = g.throws;
    o.heard = { glass: M.heard.glass - h0.glass, bowl: M.heard.bowl - h0.bowl, felt: M.heard.felt - h0.felt };
    return o; });
  if (mb.pour !== 'aim' || !(mb.inBowl >= 450) || !(Math.abs(mb.held - 1) < 0.01) || !mb.arcEnds || !mb.reach || mb.after !== 'aim' || !(mb.out >= 1) || mb.throws !== 1 || !(mb.heard.glass >= 1 && mb.heard.bowl >= 1 && mb.heard.felt >= 1))
    failures.push(`[play-marbles.html] ${JSON.stringify(mb)}`);
  { // the pull strip: half way down and let go throws the next one
    const box = await page.locator('#pull').boundingBox();
    await page.mouse.move(box.x + box.width / 2, box.y + 4); await page.mouse.down();
    await page.mouse.move(box.x + box.width / 2, box.y + box.height * 0.5, { steps: 6 }); await page.mouse.up();
    const t2 = await page.evaluate(() => ({ throws: __marbles.game.throws, state: __marbles.game.state }));
    if (t2.throws !== 2) failures.push(`[play-marbles.html] pulling the strip half way did not throw (${JSON.stringify(t2)})`);
  }
  console.log(`${failures.length === before19 ? 'ok  ' : 'FAIL'} play-marbles.html (${mb.inBowl} marbles poured and at rest, the bowl and table carrying ${(mb.held * 100).toFixed(2)}% of the weight; the arc seen ahead ends at its first contact; a throw near the rim knocked out ${mb.out}, heard ${mb.heard.glass} glass, ${mb.heard.bowl} bowl, ${mb.heard.felt} felt; the strip throws)`);

  // ── 20. zoom.html: what setting H does (OFS §8, "H is a zoom, not an escape"): the held window the same width in levels
  //    at every H, a doubling of H one level's shift, addresses per level halving inward and flat (the reader's lay) or
  //    mirrored (the in-place lay) outward, a cluster told apart at the corner and lost into home under a large H, detail
  //    absolute inside the corner and relative past it ──
  current = 'zoom.html';
  const before20 = failures.length;
  await page.goto(new URL('zoom.html', base).href, { waitUntil: 'load' });
  const zm = await page.evaluate(() => { const z = __zoom, n = 32, o = {};
    o.widths = [1 / 64, 1, 1024].map(H => [z.held(H, n, 'reader', 12).levels, z.held(H, n, 'inplace', 12).levels]);
    o.shift = Math.max(...[-8, -3, -1, 0, 1, 3, 8].map(k => Math.abs(z.perLevel(k, 1, n, 'reader', 12) - z.perLevel(k + 1, 2, n, 'reader', 12))));
    o.reader = [-3, -2, -1, 0, 1, 5].map(k => z.perLevel(k, 1, n, 'reader', 12));
    o.inplace = [-3, -2, -1, 0, 1, 2].map(k => z.perLevel(k, 1, n, 'inplace', 12));
    const w = z.makeWorld('nested'), atC = z.read(w, 100, n, 'reader', 12), big = z.read(w, 1e4, n, 'reader', 12);
    o.atCorner = atC.resolved.includes(2); o.lostSmall = !big.resolved.includes(2) && big.home >= 35;
    o.near = [z.detail(0.25, 1, n, 'reader'), z.detail(0.5, 1, n, 'reader')];
    o.far = [z.detail(4, 1, n, 'reader') / 4, z.detail(64, 1, n, 'reader') / 64, z.detail(64, 1, n, 'inplace') / 64];
    z.set({ H: 8, n: 64, world: 'even' }); o.hud = document.getElementById('hud').textContent.length > 0;
    return o; });
  const nl2 = 32 * Math.LN2;
  if (!zm.widths.every(([r, i]) => r === 17 && i === 10) || !(zm.shift < 1e-12) ||
      zm.reader.slice(0, 3).join() !== '4,8,16' || !zm.reader.slice(3).every(a => Math.abs(a - nl2) < 1e-9) ||
      zm.inplace.join() !== '4,8,16,16,8,4' || !zm.atCorner || !zm.lostSmall ||
      zm.near[0] !== zm.near[1] || Math.abs(zm.far[0] - 1 / 32) > 1e-15 || Math.abs(zm.far[1] - 1 / 32) > 1e-15 || zm.far[2] !== 2 || !zm.hud)
    failures.push(`[zoom.html] ${JSON.stringify(zm)}`);
  console.log(`${failures.length === before20 ? 'ok  ' : 'FAIL'} zoom.html (held ${zm.widths[0][0]} levels on the reader's lay and ${zm.widths[0][1]} on the in-place lay at every H; doubling H shifts the levels exactly; addresses per level ${zm.reader.slice(0, 3).join(', ')} inward, ${zm.reader[3].toFixed(1)} a level past the corner, the in-place lay ${zm.inplace.join(', ')}; a cluster told apart at the corner and lost into home under H 100 times larger)`);

  // ── 21. parallax.html: parallax from the corner (PXC): the error per step least and round at the corner, the same at k
  //    and 1/k, the band acosh(1/ε)/ln 2 levels each side, the error stretched by d/(B/2) along the line of sight, one
  //    reader alone holding only rays ──
  current = 'parallax.html';
  const before21 = failures.length;
  await page.goto(new URL('parallax.html', base).href, { waitUntil: 'load' });
  const px = await page.evaluate(() => { const p = __parallax, o = {};
    o.r1 = p.relErr(1, 1e-3); o.r4 = [p.relErr(4, 1e-3), p.relErr(0.25, 1e-3)]; o.band = p.band(1e-3);
    const c = p.triangulate(0, 1, 1e-6, 4000, 7), f = p.triangulate(0, 8, 1e-6, 4000, 8), nr = p.triangulate(0, 0.125, 1e-6, 4000, 9);
    o.aspect = [c.sAlong / c.sAcross, f.sAlong / f.sAcross, nr.sAlong / nr.sAcross];
    o.both = p.counts(); p.set({ mode: 'A' }); o.alone = p.counts(); p.set({ mode: 'both', preset: 'eyes' });
    o.hud = document.getElementById('hud').textContent.length > 0; return o; });
  if (Math.abs(px.r1 - 1e-3) > 1e-15 || Math.abs(px.r4[0] - 2.125e-3) > 1e-15 || px.r4[0] !== px.r4[1] ||
      Math.abs(px.band - 10.965783924) > 1e-8 || Math.abs(px.aspect[0] - 1) > 0.1 || Math.abs(px.aspect[1] / 8 - 1) > 0.1 ||
      Math.abs(px.aspect[2] / 0.125 - 1) > 0.1 || !(px.both.crisp > 0 && px.both.lost > 0) || px.alone.ray !== px.both.crisp + px.both.stretched + px.both.lost || !px.hud)
    failures.push(`[parallax.html] ${JSON.stringify(px)}`);
  console.log(`${failures.length === before21 ? 'ok  ' : 'FAIL'} parallax.html (error per step 1 at the corner, ×2.125 two levels either side; band ${px.band.toFixed(3)} levels each side at ε = 1e-3; the error round at the corner (${px.aspect[0].toFixed(2)}), stretched ${px.aspect[1].toFixed(1)} at 8 half-baselines and ${px.aspect[2].toFixed(3)} at an eighth; ${px.both.crisp} held, ${px.both.stretched} stretched, ${px.both.lost} lost to a ray; one reader alone, ${px.alone.ray} rays)`);

  // ── 22. sphere-cube.html: the sphere in the cube (WDG; SPN R221): every point of a turning sphere lands on one point of a
  //    cube at any extent, its address (u, t) the same at every extent and the face its largest component's; the even
  //    sphere gives each face a sixth, a face's middle quarter 38%, the wedge's three faces a third each; with the extent
  //    unknown the reader draws the cube at H, its amounts off by e/H ──
  current = 'sphere-cube.html';
  const before22 = failures.length;
  // The page loads three.js from jsDelivr. Serve the same pinned version from node_modules (a devDependency) so the test
  // does not depend on the CDN; fall through to the network if it is not installed.
  await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/three@0\.160\.0\//, async route => {
    const rel = new URL(route.request().url()).pathname.replace('/npm/three@0.160.0/', '');
    try { await route.fulfill({ status: 200, contentType: 'text/javascript', body: await readFile(join(ROOT, 'node_modules/three', rel)) }); }
    catch { await route.continue(); }
  });
  await page.goto(new URL('sphere-cube.html?step=6&turn=0', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__sphereCube && __sphereCube.frames > 2, null, { timeout: 30000 });
  const sq = await page.evaluate(() => { const c = __sphereCube, o = { rt: 0, ad: 0, faceOk: true };
    const pts = [];
    for (let i = 0; i < 9; i++) for (let j = 0; j < 9; j++) for (let k = 0; k < 9; k++) {
      const x = [(i - 4) / 4.1, (j - 4.2) / 4.3, (k - 3.9) / 3.9]; if (Math.hypot(...x) > 1e-9) pts.push(x); }
    for (const [axis, ang] of [[[1, 0, 0], 0], [[0.3, 0.8, 0.1], 1.1], [[-0.5, 0.2, 0.9], 2.3]]) {
      c.turnBy(axis, ang);
      for (const x of pts) {
        for (const e of [1e-3, 0.5, 1]) { const X = x.map(v => v * e), a = c.address(X, e), back = c.point(a.u, a.t, e);
          o.rt = Math.max(o.rt, Math.hypot(back[0] - X[0], back[1] - X[1], back[2] - X[2]) / Math.hypot(...X)); }
        const a1 = c.address(x, 1), a2 = c.address(x.map(v => v * 1e-3), 1e-3);
        o.ad = Math.max(o.ad, Math.abs(a1.t - a2.t), ...a1.u.map((v, k) => Math.abs(v - a2.u[k])));
        const m = Math.max(...x.map(Math.abs)), lg = x.findIndex(v => Math.abs(v) === m);
        if (c.faceOf(x).slice(1) !== ['h', 'v', 'v₂'][lg]) o.faceOk = false;
      }
    }
    const st = c.stats(6000); o.faces = st.faceShares; o.mid = st.middleShare; o.pred = c.predictedMiddle; o.wedge = st.wedge.shares;
    c.set({ step: 5, e: 0.25, known: false }); o.hud = c.hud(); o.frames = c.frames; o.webgl = c.webgl;
    // step 7, the two sweeps (AZM; SPN R237): altitude and azimuth each read their own pair, the corners at 45°; swept
    // evenly in both angles v ≤ h for 0.3426 and h largest 0.2326; swept evenly over the wedge (height even) ½ and ⅓
    c.set({ step: 7, alt: 30, az: 60, even: 'angles' }); const S = c.sweeps, r = S.readings(30, 60);
    o.sw = { az: r.az, alt: r.alt, exA: S.exact('angles'), exB: S.exact('area'), ctA: S.counted('angles'), ctB: S.counted('area'),
      top: [S.topShare('angles'), S.topShare('area')], lam: S.lambert(10, 50, 0.2, 0.7), hud: c.hud(),
      truth: S.truth(3, 0.5), centre: S.centre };
    return o; });
  const sw = sq.sw, close = (x, y, t) => Math.abs(x - y) <= t;
  const swOk = close(sw.az, Math.sqrt(3), 1e-12) && close(sw.alt, 1 / Math.sqrt(3), 1e-12) &&
    close(sw.exA.vh, 0.3425834779, 1e-8) && close(sw.exA.near, 0.2326315334, 1e-8) && close(sw.exA.v2h, 0.5, 1e-12) &&
    ['vh', 'v2h', 'v2v'].every(k => close(sw.exB[k], 0.5, 1e-12)) && close(sw.exB.near, 1 / 3, 1e-12) &&
    ['vh', 'v2h', 'v2v', 'near'].every(k => close(sw.ctA[k], sw.exA[k], 0.02) && close(sw.ctB[k], sw.exB[k], 0.02)) &&
    sw.top[0] > 0.4 && close(sw.top[1], 0.25, 0.01) && close(sw.lam.area, sw.lam.product, 1e-9) &&
    /azimuth reads v₂\/h = tan z = 1\.732/.test(sw.hud) && /v ≤ h 34\.3%/.test(sw.hud) &&
    // R238: the truth a point of h + v + v₂ = 1, the reader's drawing V = V₂ = H its centre
    [2 / 9, 2 / 3, 1 / 9].every((x, k) => close(sw.truth[k], x, 1e-15)) && sw.centre.every(x => close(x, 1 / 3, 1e-15)) &&
    /its centre \(⅓, ⅓, ⅓\)/.test(sw.hud);
  if (!(sq.rt < 1e-12) || !(sq.ad < 1e-12) || !sq.faceOk || sq.faces.some(f => Math.abs(f - 1 / 6) > 0.01) ||
      Math.abs(sq.mid - sq.pred) > 0.01 || sq.wedge.some(f => Math.abs(f - 1 / 3) > 0.02) ||
      !/off by e\/H = 0\.250, 2\.00 levels/.test(sq.hud) || !(sq.frames > 0) || !sq.webgl || !swOk)
    failures.push(`[sphere-cube.html] ${JSON.stringify({ ...sq, hud: sq.hud.slice(0, 200), sw: { ...sw, hud: sw.hud.slice(0, 300) } })}`);
  console.log(`${failures.length === before22 ? 'ok  ' : 'FAIL'} sphere-cube.html (round trip ${sq.rt.toExponential(1)}, the address the same at every extent to ${sq.ad.toExponential(1)}, the face the largest component's; faces ${sq.faces.map(f => f.toFixed(3)).join(' ')}; a face's middle quarter ${(100 * sq.mid).toFixed(1)}% (exactly ${(100 * sq.pred).toFixed(1)}%); the wedge's faces ${sq.wedge.map(f => (100 * f).toFixed(1) + '%').join(', ')}; extent unknown, off by e/H; two sweeps: v₂/h = tan z, v/reach = tan a, even in both angles v ≤ h ${sw.exA.vh.toFixed(4)} and h largest ${sw.exA.near.toFixed(4)} (drawn ${sw.ctA.vh.toFixed(3)}, ${sw.ctA.near.toFixed(3)}), even over the wedge ½ and ⅓ (drawn ${sw.ctB.vh.toFixed(3)}, ${sw.ctB.near.toFixed(3)}), Lambert's map equal-area; the drawing V = V₂ = H the triangle's centre, a true point off it)`);

  // ── 23. paths.html: one sweep, three paths (plans/ofs-review-6.md; OFS §11.2, question 2): the share of the sweep
  //    measured along each path matches its closed form; all three fair and ½ at the corner, parting between; the mean
  //    climbs ρ(0)·ln 10 a tenfold on each; sin² 2θ keeps the median at the corner and has the mean 4/π; on the circle
  //    outer × inner = 1, π/2 and 2/π at the horizon ──
  current = 'paths.html';
  const before23 = failures.length;
  await page.goto(new URL('paths.html?path=line&t=22.5', base).href, { waitUntil: 'load' });
  const pa = await page.evaluate(() => { const P = __paths, o = {};
    o.meas = Math.max(...P.paths.flatMap(p => [5, 22.5, 45, 67.5, 85].map(t => Math.abs(P.measure(p, t) - P.b(p, t)))));
    o.fair = Math.max(...P.paths.flatMap(p => Array.from({ length: 89 }, (_, i) => Math.abs(P.b(p, i + 1) + P.b(p, 89 - i) - 1))));
    o.corner = P.paths.map(p => P.b(p, 45)); o.at = P.paths.map(p => P.b(p, 22.5));
    o.dec = P.paths.map(p => P.perDecade(p, 1e8) / (P.rho0[p] * Math.LN10));
    o.w = [P.bWeighted(45), P.tmeanWeighted(1e8) / (4 / Math.PI)];
    const v = P.vantages(90); o.v = [v.outer, v.inner, v.product];
    o.hud = P.hud(); P.set({ path: 'square', t: 90 }); o.hud90 = P.hud(); o.vant = P.vant(); return o; });
  const pathsWant = [0.25, 1 - Math.SQRT1_2, (Math.SQRT2 - 1) / 2];
  if (!(pa.meas < 1e-9) || !(pa.fair < 1e-12) || pa.corner.some(c => Math.abs(c - 0.5) > 1e-12) ||
      pa.at.some((a, i) => Math.abs(a - pathsWant[i]) > 1e-12) || pa.dec.some(d => Math.abs(d - 1) > 1e-6) ||
      Math.abs(pa.w[0] - 0.5) > 1e-12 || Math.abs(pa.w[1] - 1) > 1e-12 ||
      Math.abs(pa.v[0] - Math.PI / 2) > 1e-12 || Math.abs(pa.v[1] - 2 / Math.PI) > 1e-12 || Math.abs(pa.v[2] - 1) > 1e-12 ||
      !/line 0\.293/.test(pa.hud) || !/v\/h = ∞/.test(pa.hud90) || !/2\/π = 0\.6366/.test(pa.vant))
    failures.push(`[paths.html] ${JSON.stringify({ ...pa, hud: pa.hud.slice(0, 160), hud90: pa.hud90.slice(0, 80) })}`);
  console.log(`${failures.length === before23 ? 'ok  ' : 'FAIL'} paths.html (the share measured along each path its closed form to ${pa.meas.toExponential(1)}; fair, ½ at the corner on all three; at 22.5° ${pa.at.map(a => a.toFixed(3)).join(', ')}; the mean climbing ρ(0)·ln 10 a tenfold; sin² 2θ median at the corner, mean 4/π; π/2 and 2/π at the horizon)`);

  // ── 24. h-limits.html: what is H? (HKO; SPN R228): past the world's ends the lays are the corner-free rulers (the
  //    number line at H of ∞, the logarithm or the reciprocal at H of 0), a corner only with H among the amounts; the
  //    world lost whole three ways at the thresholds; held 24 and 17 addresses at H = 1; the best H for a pair their
  //    geometric mean, the widest angle arcsin((r − 1)/(r + 1)) ──
  current = 'h-limits.html';
  const before24 = failures.length;
  await page.goto(new URL('h-limits.html', base).href, { waitUntil: 'load' });
  const hl = await page.evaluate(() => { const L = __hlimits, th = L.thresholds(32), o = {};
    o.dev = [L.deviation(1e3, 'reader').line, L.deviation(1e-3, 'reader').log, L.deviation(1e-3, 'inplace').recip, L.deviation(1e3, 'inplace').line];
    o.mid = [L.deviation(1, 'reader'), L.deviation(1, 'inplace')].map(d => Math.min(...Object.values(d)));
    o.home = L.held(th.home * 1.001, 'reader', 32); o.homeIn = L.held(th.home * 1.001, 'inplace', 32);
    o.edge = L.held(th.edge / 1.001, 'reader', 32); o.hor = L.held(th.horizon / 1.001, 'inplace', 32);
    o.short = [L.held(th.home / 1.001, 'reader', 32).addresses, L.held(th.edge * 1.001, 'reader', 32).addresses, L.held(th.horizon * 1.001, 'inplace', 32).addresses];
    o.at1 = [L.held(1, 'reader', 32).addresses, L.held(1, 'inplace', 32).addresses];
    const b = L.bestPair(1, 2); o.best = [b.H, b.angle, L.pairAngle(1, 2, b.H), L.pairAngle(1, 2, b.H * 1.01), L.pairAngle(1, 2, 1e-8), L.pairAngle(1, 2, 1e8)];
    const x = L.WORLD[20], D = x / 10, pk = L.objectPeak(x, D, 32);
    o.obj = [L.objectSpan('reader', x, D, x / 100, 32), L.objectSpan('reader', x, D, x / 3, 32), 32 * Math.log(1.1), L.objectSpan('reader', x, D, 10 * x, 32), L.objectSpan('inplace', x, D, 10 * x, 32),
      pk.H, Math.sqrt(x * (x + D)), L.objectSpan('inplace', x, D, pk.H, 32), pk.span, L.objectSpan('inplace', x, D, pk.H * 0.99, 32), L.objectSpan('inplace', x, D, pk.H * 1.01, 32)];
    o.unl = [L.held(1e-20, 'reader', Infinity).addresses, L.held(1e20, 'reader', Infinity).addresses, L.held(1e-20, 'inplace', Infinity).addresses, L.held(1e20, 'inplace', Infinity).addresses];
    L.set({ n: Infinity }); o.hudUnl = L.hud(); L.set({ n: 32 });
    L.set({ lg: 30, lay: 'reader' }); o.hudInf = L.hud(); L.set({ lg: -30, lay: 'inplace' }); o.hudZero = L.hud(); L.set({ lg: 0, lay: 'reader' }); return o; });
  if (hl.dev.some(d => d > 1e-12) || hl.mid.some(d => !(d > 1e-3)) || !hl.home.home || !hl.homeIn.home || hl.edge.addresses !== 0 || hl.edge.past !== 31 ||
      !hl.hor.horizon || hl.short.some(c => c < 1) || hl.short[0] === 1 || hl.short[2] === 1 || hl.at1[0] !== 24 || hl.at1[1] !== 17 ||
      Math.abs(hl.best[0] - Math.SQRT2) > 1e-12 || Math.abs(hl.best[1] - Math.asin(1 / 3)) > 1e-12 || Math.abs(hl.best[2] - hl.best[1]) > 1e-12 ||
      !(hl.best[3] < hl.best[2]) || hl.best[4] > 1e-6 || hl.best[5] > 1e-6 ||
      Math.abs(hl.obj[0] - hl.obj[2]) > 1e-12 || Math.abs(hl.obj[1] - hl.obj[2]) > 1e-12 || Math.abs(hl.obj[3] - 0.32) > 1e-12 || Math.abs(hl.obj[4] - 0.32) > 1e-12 ||
      Math.abs(hl.obj[5] - hl.obj[6]) > 1e-12 || Math.abs(hl.obj[7] - hl.obj[8]) > 1e-12 || !(hl.obj[9] < hl.obj[7] && hl.obj[10] < hl.obj[7]) ||
      hl.unl.some(c => c !== 31) || !/no longer matters/.test(hl.hudUnl) ||
      !/number line/.test(hl.hudInf) || !/home's first address/.test(hl.hudInf) || !/reciprocal/.test(hl.hudZero) || !/horizon's last address/.test(hl.hudZero))
    failures.push(`[h-limits.html] ${JSON.stringify({ ...hl, hudInf: hl.hudInf.slice(0, 120), hudZero: hl.hudZero.slice(0, 120) })}`);
  console.log(`${failures.length === before24 ? 'ok  ' : 'FAIL'} h-limits.html (past the world's ends the number line, the logarithm and the reciprocal exactly, a corner only with H inside; lost whole into home, past the edge, into the horizon at the thresholds; ${hl.at1[0]} and ${hl.at1[1]} addresses at H = 1; a pair best told apart at √(x₁x₂), ${(hl.best[1] * 180 / Math.PI).toFixed(2)}° for r = 2; one object's detail flat past the corner on the reader's lay, nΔ/H inside, most on the in-place lay at √(x(x + Δ)); with unlimited addresses all 31 held apart at every H)`);

  // ── 25. h-chain.html: the chain from H (HKO; SPN R228; draw's rcc and udv): one reader's even sweep gives back the
  //    unit circle for every figure at every size; two standpoints 2H apart hold every point at the best H and none at
  //    H = 10⁻³ or 10³; H of 0 or one standpoint leaves only rays; the best H the geometric middle of the figure's
  //    distances; the count of V's sets the facings and the near field; physics relabels and nothing moves ──
  current = 'h-chain.html';
  const before25 = failures.length;
  await page.goto(new URL('h-chain.html?step=5', base).href, { waitUntil: 'load' });
  const hc = await page.evaluate(() => { const C = __hchain, o = {};
    o.fe = Math.max(...['circle', 'egg', 'star', 'astroid'].flatMap(f => [1, 1000].map(s => C.fisheye(f, s).worst)));
    const b = C.bestH('star'); o.best = [b.H, Math.sqrt(b.near * b.far)];
    const at = H => C.triangulate({ H, sp: 2, eps: 0.5, fig: 'star', degenerate: null });
    o.held = [at(1e-3).held, at(b.H).held, at(1e3).held]; o.three = C.triangulate({ H: b.H, sp: 3, eps: 0.5, fig: 'star', degenerate: null }).held;
    o.zero = C.triangulate({ degenerate: 'zero' }).lost; o.one = C.triangulate({ sp: 1, degenerate: null }).lost;
    C.set({ step: 2, n: 5 }); o.hud2 = C.hud();
    C.set({ step: 6, unit: 'mi', lg: 1 }); o.hud6 = C.hud(); const after = C.triangulate({ H: 10, sp: 2, eps: 0.5, fig: 'star', degenerate: null });
    C.set({ unit: '' }); const before = C.triangulate({ H: 10, sp: 2, eps: 0.5, fig: 'star', degenerate: null });
    o.moved = Math.max(...after.res.map((r, i) => r.Q && before.res[i].Q ? Math.hypot(r.Q[0] - before.res[i].Q[0], r.Q[1] - before.res[i].Q[1]) : 0));
    return o; });
  if (!(hc.fe < 1e-12) || Math.abs(hc.best[0] - hc.best[1]) > 1e-12 || hc.held[1] !== 72 || hc.held[0] !== 0 || hc.held[2] !== 0 || hc.three !== 72 ||
      hc.zero !== 72 || hc.one !== 72 || !/1\/6/.test(hc.hud2) || !/miles/.test(hc.hud6) || hc.moved !== 0)
    failures.push(`[h-chain.html] ${JSON.stringify(hc)}`);
  console.log(`${failures.length === before25 ? 'ok  ' : 'FAIL'} h-chain.html (one reader's sweep gives back the unit circle for every figure to ${hc.fe.toExponential(1)}; two standpoints 2H apart hold ${hc.held[1]} of 72 at the best H = ${hc.best[0].toFixed(3)}, ${hc.held[0]} at 10⁻³ and ${hc.held[2]} at 10³; H of 0 or one standpoint, only rays; five parties, the near field 1/6; physics relabels, nothing moves)`);

  // ── 26. wedge.html: the wedge (SPN R240; WDG, AZM, SIT): from home the three parties at the corners of an equilateral
  //    triangle and every direction at its shares, the pairs' corners its medians; on Lambert's map the six chambers a
  //    sixth each, the corner v = h halving it, the three corners meeting at z = 45°, v = 1/√3; H moves every thing
  //    along its own ray, never across it; every situation reaches every direction in one scan, holding the whole wedge,
  //    a fan, a row or a cell at once; the drawing at the centre, at the truth with both breadths known ──
  current = 'wedge.html';
  const before26 = failures.length;
  await page.goto(new URL('wedge.html?step=4', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__wedge && __wedge.frames > 2, null, { timeout: 30000 });
  const wg = await page.evaluate(() => { const W = __wedge, o = {};
    const A = W.homeProject([1, 0, 0]), B = W.homeProject([0, 1, 0]), C = W.homeProject([0, 0, 1]), dist = (p, q) => Math.hypot(p[0] - q[0], p[1] - q[1]);
    o.sides = [dist(A, B), dist(B, C), dist(C, A)]; o.centre = W.homeProject([1, 1, 1]);
    o.sh = 0; o.med = 0;
    for (let i = 0; i < 400; i++) { const d = W.fromLambert((i * 37.1) % 90, (i * 0.6180339887) % 1), b = W.homeShares(d.map(c => c * (0.2 + (i % 7)))), s = W.shares(d);
      o.sh = Math.max(o.sh, ...b.map((x, k) => Math.abs(x - s[k]))); }
    for (const t of [0.05, 0.2, 0.4, 0.49]) { const b = W.homeShares([t, t, 1 - 2 * t]); o.med = Math.max(o.med, Math.abs(b[0] - b[1])); }
    o.ch = Object.values(W.chamberShares(240)); o.half = W.cornerHalf; o.triple = [W.cornerVH(45), W.cornerVV2(45)];
    const P = [0.01, 1, 1000].map(H => W.placeAt(H)); o.dir = 0; o.moved = 0;
    P[0].forEach((p, i) => { for (const Q of [P[1], P[2]]) { const q = Q[i];
      if (p.r > 0 && q.r > 0) o.dir = Math.max(o.dir, ...p.p.map((c, k) => Math.abs(c / p.r - q.p[k] / q.r)));
      if (Math.abs(p.r - q.r) > 1e-9) o.moved++; } });
    o.lay = [W.lay(1, 'reader'), W.lay(8, 'reader'), W.lay(8, 'inplace')];
    o.counts = [0.01, 1, 1000].map(H => W.counts(H));
    o.cov = [['once', 'once'], ['once', 'serial'], ['serial', 'once'], ['serial', 'serial']].map(([a, b]) => ({ ...W.coverage(a, b), name: W.situationName(a, b) }));
    o.draw = [W.drawingOf('once', 'serial', 3, 0.5), W.drawingOf('known', 'known', 3, 0.5), W.drawingOf('known', 'serial', 3, 0.5)];
    o.hud = W.hud();
    W.set({ step: 6, view: 'home' }); o.home = W.state(); o.hudHome = W.hud(); o.frames = W.frames; o.webgl = W.webgl;
    // step 7, position then sweep (SPN R242): one rotation places the wedge, the hand sweeps in its own frame
    const PS = W.position, p7 = {}; let sd = 11;
    const rn = () => { sd = (sd + 0x6D2B79F5) >>> 0; let t = sd; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };   // mulberry32
    const gs = () => Math.sqrt(-2 * Math.log(1 - rn())) * Math.cos(2 * Math.PI * rn());
    const rdir = () => { const v = [gs(), gs(), gs()], n = Math.hypot(...v); return v.map(x => x / n); };
    W.set({ step: 7, view: 'outside', pos: { lon: 150, lat: -25, roll: 40 } });
    p7.rt = 0; for (const [lo, la, ro] of [[150, -25, 40], [-60, 70, -120], [10, -5, 170], [45, 35.26, 0]]) { const b = PS.of(PS.quat(lo, la, ro));
      p7.rt = Math.max(p7.rt, Math.abs(((b.lon - lo + 540) % 360) - 180), Math.abs(b.lat - la), Math.abs(((b.roll - ro + 540) % 360) - 180)); }
    W.set({ alt: 33, az: 61 }); const tip = PS.handTip(), wd = PS.world(33, 61); p7.tip = Math.max(...tip.map((x, k) => Math.abs(x - wd[k]))); p7.hud = W.hud();
    p7.first = PS.of(PS.quat(45, Math.asin(1 / Math.sqrt(3)) * 180 / Math.PI, 0)); p7.idq = PS.quat(45, Math.asin(1 / Math.sqrt(3)) * 180 / Math.PI, 0);
    const oct = [0, 1, 2, 3, 4, 5, 6, 7].map(k => PS.octant(k)); p7.tile = 0;
    for (let i = 0; i < 3000; i++) { const d = rdir(); if (oct.filter(q => PS.inWedge(q, d)).length !== 1) p7.tile++; }
    const turns = PS.octahedral(), per = new Array(8).fill(0); for (const q of turns) per[PS.imageOctant(q)]++; p7.turns = [turns.length, per];
    const qr = PS.random(); let ins = 0; for (let i = 0; i < 40000; i++) if (PS.inWedge(qr, rdir())) ins++; p7.eighth = ins / 40000;
    W.set({ view: 'home' }); const pts = [[1, 0.2, 0.1], [0.3, 1, 0.5], [0.2, 0.4, 1], [1, 1, 1], [0.7, 0.1, 0.9]];
    W.set({ pos: { lon: 150, lat: -25, roll: 40 } }); const na = PS.homeNdc(pts); W.set({ pos: { octant: 5 } }); const nb = PS.homeNdc(pts);
    p7.home = Math.max(...na.map((p, i) => Math.max(Math.abs(p[0] - nb[i][0]), Math.abs(p[1] - nb[i][1])))); p7.hudHome = W.hud();
    o.p7 = p7;
    return o; });
  const wclose = (x, y, t) => Math.abs(x - y) <= t;
  const wOk = wg.sides.every(s => wclose(s, wg.sides[0], 1e-12)) && wg.centre.every(c => wclose(c, 0, 1e-12)) && wg.sh < 1e-12 && wg.med < 1e-12 &&
    wg.ch.length === 6 && wg.ch.every(c => wclose(c, 1 / 6, 0.002)) && wclose(wg.half, 0.5, 1e-9) && wg.triple.every(y => wclose(y, 1 / Math.sqrt(3), 1e-15)) &&
    wg.dir < 1e-12 && wg.moved > 100 && wclose(wg.lay[0], 1, 0) && wclose(wg.lay[1], 1 + Math.log(8), 1e-15) && wclose(wg.lay[2], 1.875, 1e-15) &&
    wg.counts.every(c => c.home + c.near + c.far + c.past === 280) && wg.counts[2].home > wg.counts[1].home && wg.counts[0].past > wg.counts[1].past &&
    wg.cov.every(c => c.share === 1) && wg.cov.map(c => c.held).join() === [1, 1 / 24, 1 / 24, 1 / 576].join() &&
    /camera's frame/.test(wg.cov[0].name) && /slit panoramic/.test(wg.cov[1].name) && /line camera/.test(wg.cov[2].name) && /single-pixel/.test(wg.cov[3].name) &&
    wg.draw[0].every(x => wclose(x, 1 / 3, 1e-15)) && [2 / 9, 2 / 3, 1 / 9].every((x, k) => wclose(wg.draw[1][k], x, 1e-15)) &&
    [0.2, 0.6, 0.2].every((x, k) => wclose(wg.draw[2][k], x, 1e-15)) &&
    /seen from home at its shares/.test(wg.hud) && /merged into home/.test(wg.hud) && /slit panoramic/.test(wg.hudHome) &&
    wg.home.view === 'home' && wg.frames > 0 && wg.webgl &&
    wg.p7.rt < 1e-9 && wg.p7.tip < 1e-6 && wg.p7.idq.slice(0, 3).every(x => Math.abs(x) < 1e-12) && wg.p7.tile === 0 &&
    wg.p7.turns[0] === 24 && wg.p7.turns[1].every(c => c === 3) && Math.abs(wg.p7.eighth - 0.125) < 0.01 && wg.p7.home < 1e-9 &&
    /turned 40\.0° about it/.test(wg.p7.hud) && /from home the wedge looks the same at every position/.test(wg.p7.hudHome);
  if (!wOk) failures.push(`[wedge.html] ${JSON.stringify({ ...wg, hud: wg.hud.slice(0, 200), hudHome: wg.hudHome.slice(0, 200) })}`);
  console.log(`${failures.length === before26 ? 'ok  ' : 'FAIL'} wedge.html (from home the parties at an equilateral triangle's corners, every direction at its shares to ${wg.sh.toExponential(1)}, the pairs' corners its medians; Lambert's map: six chambers ${wg.ch.map(c => c.toFixed(3)).join(' ')}, v = h halving it, the corners meeting at v = 1/√3; H moves things along their rays, never across (to ${wg.dir.toExponential(1)}); at H = 0.01, 1, 1000 merged into home ${wg.counts.map(c => c.home).join(', ')}, past the edge ${wg.counts.map(c => c.past).join(', ')}; every situation reaches every direction, holding 1, 1/24, 1/24, 1/576 at once; the drawing at the centre, at the truth with both known; step 7: one rotation places it (round trip ${wg.p7.rt.toExponential(1)}), the hand on the sphere R·d to ${wg.p7.tip.toExponential(1)}, the eight octants tile the sphere, the octahedron's 24 turns each octant 3 times, an eighth wherever put (${wg.p7.eighth.toFixed(4)}), from home the same at every position to ${wg.p7.home.toExponential(1)})`);

  // ── 27. wedge-browse.html: browsing the wedge (SPN R241; the calendar project's navigation dial): 2^53 − 1 items made
  //    from their addresses, every cell's halves adding to it exactly; the drawn cells and items adding to all of them in
  //    every state; at w = 1 and the drawing at 0 the view is the wedge itself; the gold, a rate, moves the blue by 0.4 a
  //    second at tan 1, and letting go re-centres the drawing on what the blue reached; the radius keeps the blue's place;
  //    an item found by its index sits at the triple corner with its total at the corner; from home nothing moves with H ──
  current = 'wedge-browse.html';
  const before27 = failures.length;
  await page.goto(new URL('wedge-browse.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__browse && __browse.frames > 2, null, { timeout: 30000 });
  const br = await page.evaluate(() => { const B = __browse, o = { split: true, totals: [] };
    let seed = 7; const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
    for (let k = 0; k < 200; k++) { let n = { ...B.ROOT };
      while (n.d < B.D_MAX) { const c = B.children(n);
        if (c[0].count + c[1].count !== n.count || c[0].start !== n.start || c[1].start !== n.start + c[0].count || c[0].count < 0 || c[1].count < 0) o.split = false;
        n = rnd() < 0.5 || c[1].count === 0 ? (c[0].count ? c[0] : c[1]) : c[1]; } }
    o.totals.push(B.drawn.total);
    o.wedge = 0; B.set({ mu1: 0, mu2: 0, lw: 0 });
    for (let k = 0; k < 300; k++) { const l1 = 60 * rnd() - 30, l2 = 60 * rnd() - 30, a = B.dispShares(l1, l2), b = B.trueShares(l1, l2); o.wedge = Math.max(o.wedge, ...a.map((x, i) => Math.abs(x - b[i]))); }
    o.totals.push(B.drawn.total);
    B.set({ lw: 2 }); const h = B.hold(1, 0, 1.0); o.zeta = Math.hypot(...h.zeta); const blue = h.blue; const r = B.release(); o.recentre = B.dispShares(...blue).map(x => Math.abs(x - 1 / 3)); o.mu = [r.mu1 - blue[0], r.mu2 - blue[1]];
    o.totals.push(B.drawn.total);
    B.placeBlue(r.mu1 + 1.5, r.mu2 - 0.7); const k0 = B.view().blue; B.set({ lw: 3 }); const k1 = B.view(); o.keep = Math.hypot(k1.blue[0] - k0[0], k1.blue[1] - k0[1]); o.keptMu = k1.mu1 === r.mu1 && k1.mu2 === r.mu2;
    B.set({ lw: -20 }); const k2 = B.view(); o.moved = Math.hypot(k2.mu1 - k0[0], k2.mu2 - k0[1]);
    o.items = [0, 1, 12345, 2 ** 52, 7e15, B.N - 1].map(i => { const it = B.itemAt(i), bx = B.boxOf(it.leaf), c = B.cellAt(it.l1, it.l2, B.D_MAX);
      return { ok: it.index === i && it.l1 >= bx[0] && it.l1 < bx[1] && it.l2 >= bx[2] && it.l2 < bx[3] && c.i1 === it.leaf.i1 && c.i2 === it.leaf.i2 && c.start === it.leaf.start } ; }).every(x => x.ok);
    const g = B.goTo(4503599627370495), v = B.view(); o.goto = { centre: B.dispShares(g.l1, g.l2).map(x => Math.abs(x - 1 / 3)), corner: Math.abs(2 ** (g.ell - v.lH) - 1), under: B.under(g.l1, g.l2) };
    o.totals.push(B.drawn.total); o.hud = B.hud();
    const s0 = B.screen(); B.set({ lH: v.lH + 7 }); const s1 = B.screen(); o.still = s0.length === s1.length && s0.every((p, i) => p[0] === s1[i][0] && p[1] === s1[i][1]);
    const t0 = performance.now(); B.set({ mu1: 0, mu2: 0, lw: 2, lH: 0 }); o.ms = performance.now() - t0; o.totals.push(B.drawn.total); o.frames = B.frames;
    return o; });
  const brOk = br.split && br.totals.every(t => t === 9007199254740991) && br.wedge < 1e-15 && Math.abs(br.zeta - 0.4) < 1e-9 &&
    br.recentre.every(x => x < 1e-12) && br.mu.every(x => x === 0) && br.keep < 1e-9 && br.keptMu && br.moved < 1e-9 && br.items &&
    br.goto.centre.every(x => x < 1e-9) && br.goto.corner < 1e-12 && br.goto.under && br.goto.under.kind === 'item' && br.goto.under.index === 4503599627370495 &&
    /adding to 9,007,199,254,740,991 of 9,007,199,254,740,991, exactly/.test(br.hud) && /read: item 4,503,599,627,370,495/.test(br.hud) && br.still && br.frames > 0;
  if (!brOk) failures.push(`[wedge-browse.html] ${JSON.stringify({ ...br, hud: br.hud.slice(0, 300) })}`);
  console.log(`${failures.length === before27 ? 'ok  ' : 'FAIL'} wedge-browse.html (2^53 − 1 items, every halving adding exactly; the drawn cells and items adding to all of them in ${br.totals.length} states; at w = 1 the wedge itself to ${br.wedge.toExponential(1)}; the gold at tan 1 for a second moves the blue ${br.zeta.toFixed(3)}, letting go re-centres on it; the radius keeps the blue's place, or moves the window to it; item 4,503,599,627,370,495 found by index at the triple corner, its total at the corner; from home nothing moves with H; a rebuild ${br.ms.toFixed(0)} ms)`);

  // ── 28. two-readers.html: the inscribed reader's directions and the central reader's shape do not move when the world
  //    is scaled (a₀); the central amounts move together by e^Δa₀; the writer writes only with all three, at the true
  //    size; a uniform sweep's inscribed median settles at the corner, its mean climbs, the central mean settles ──
  current = 'two-readers.html';
  const before28 = failures.length;
  await page.goto(new URL('two-readers.html', base).href, { waitUntil: 'load' });
  const tr = await page.evaluate(() => {
    const T = __twoReaders, out = { insc: 0, shape: 0, factor: 0, writer: [], size: 0 };
    for (const shape of ['circle', 'egg', 'star', 'lumpy']) for (const rho of [0, 0.5, 1]) {
      const p0 = T.params({ shape, rho, a0: 0 }), i0 = T.inscribed(p0), c0 = T.central(p0);
      for (const a0 of [-2, 0.7, 2]) {
        const p = T.params({ shape, rho, a0 }), i = T.inscribed(p), c = T.central(p);
        i.forEach((r, k) => { out.insc = Math.max(out.insc, Math.abs(r.alpha - i0[k].alpha)); });
        c.shape.forEach((s, k) => { out.shape = Math.max(out.shape, Math.abs(s - c0.shape[k])); });
        c.raw.forEach((r, k) => { out.factor = Math.max(out.factor, Math.abs(r / c0.raw[k] / Math.exp(a0) - 1)); });
        const w = T.writer(p, { addresses: true, amounts: true, unit: true });
        w.radii.forEach((r, k) => { out.size = Math.max(out.size, Math.abs(r / T.radius(p, c.dirs[k]) - 1)); });
      }
    }
    const circ = T.inscribed(T.params({ shape: 'circle', rho: 0 }));
    out.halfAngle = Math.max(...circ.map((r, k) => Math.abs(r.alpha - Math.PI * (k + 1) / 24 / 2)));
    const p = T.params({});
    for (const m of [0, 1, 2, 3, 4, 5, 6, 7]) out.writer.push(T.writer(p, { addresses: !!(m & 1), amounts: !!(m & 2), unit: !!(m & 4) }).ok);
    const st = T.stats(p, 20000, 7), early = st.find(s => s.n === 100), last = st[st.length - 1];
    out.median = last.median; out.meanEarly = early.meanI; out.meanLast = last.meanI; out.cmean = last.meanC; out.cexact = T.exactCentralMean(p);
    return out;
  });
  const trOk = tr.insc < 1e-12 && tr.shape < 1e-12 && tr.factor < 1e-12 && tr.size < 1e-12 && tr.halfAngle < 1e-12 &&
    tr.writer.every((ok, m) => ok === (m === 7)) && Math.abs(tr.median - 1) < 0.05 && tr.meanLast > tr.meanEarly + 1 &&
    Math.abs(tr.cmean - tr.cexact) < 0.01;
  if (!trOk) failures.push(`[two-readers.html] ${JSON.stringify(tr)}`);
  console.log(`${failures.length === before28 ? 'ok  ' : 'FAIL'} two-readers.html (scaling the world moves no direction from home (${tr.insc.toExponential(0)}) and not the central shape (${tr.shape.toExponential(0)}), its amounts all by e^Δa₀; on the circle the ray at half the central angle; the writer only with the addresses, the amounts and the unit, at the true size; a uniform sweep: the inscribed median ${tr.median.toFixed(3)}, its mean ${tr.meanEarly.toFixed(2)} → ${tr.meanLast.toFixed(2)}, the central mean ${tr.cmean.toFixed(4)} against ${tr.cexact.toFixed(4)})`);

  // ── 29. pinhole.html: the reading [h : v] is unchanged when the world is scaled; an infinite breadth is the horizon
  //    (0, 1), off the flat screen; the ruler reader's amounts move with the scale and only their quotient does not ──
  current = 'pinhole.html';
  const before29 = failures.length;
  await page.goto(new URL('pinhole.html?V=inf', base).href, { waitUntil: 'load' });
  const ph = await page.evaluate(() => {
    const P = __pinhole, out = { scale: 0, quot: 0, amounts: true };
    for (const [V, d] of [[3.2, 10], [0.01, 400], [700, 2]]) {
      const r0 = P.reading(V, d), u0 = P.ruler(V, d);
      for (const k of [1e-3, 7, 1e6]) {
        const r = P.reading(k * V, k * d), u = P.ruler(k * V, k * d);
        out.scale = Math.max(out.scale, Math.abs(r.h - r0.h), Math.abs(r.v - r0.v), Math.abs(r.theta - r0.theta));
        out.quot = Math.max(out.quot, Math.abs(u.q / u0.q - 1));
        if (Math.abs(u.a / u0.a / k - 1) > 1e-12 || Math.abs(u.b / u0.b / k - 1) > 1e-12) out.amounts = false;
      }
    }
    const inf = P.reading(Infinity, 10), st = P.state(), c = P.reading(5, 5);
    const sk = P.sky(40000, 11), skyErr = Math.max(...[0.5, 1, 2].map(q => Math.abs(sk.share(q) - sk.exact(q))));
    const cosErr = Math.max(...[[0, 0], [1, 0], [0.3, 2.2], [5, 7]].map(([a, b]) => Math.abs(sk.density(a, b) - sk.cos3(a, b))));
    return { ...out, inf, page: st.reading, corner: c, image: P.reading(3, 4).image, skyErr, cosErr, exact1: sk.exact(1) };
  });
  const phOk = ph.scale < 1e-12 && ph.quot < 1e-12 && ph.amounts && ph.inf.h === 0 && ph.inf.v === 1 && ph.inf.theta === 90 &&
    ph.inf.image === Infinity && ph.page.v === 1 && Math.abs(ph.corner.theta - 45) < 1e-12 && Math.abs(ph.corner.turn - 0.5) < 1e-12 &&
    Math.abs(ph.image - 0.75) < 1e-15 && ph.skyErr < 0.01 && ph.cosErr < 1e-15 && Math.abs(ph.exact1 - (1 - Math.SQRT1_2)) < 1e-15;
  if (!phOk) failures.push(`[pinhole.html] ${JSON.stringify(ph)}`);
  console.log(`${failures.length === before29 ? 'ok  ' : 'FAIL'} pinhole.html (the reading unchanged when the world is scaled by 10⁻³, 7, 10⁶ (${ph.scale.toExponential(0)}); an infinite breadth the horizon [0 : 1], off the flat screen; equal breadth and distance at 45°, half the turn; the ruler reader's amounts move by k, only their quotient does not; a uniform sky on the flat screen the Cauchy wedge, within q of the axis to ${ph.skyErr.toFixed(4)} of 1 − 1/√(1 + q²), its density (2/π)·cos³α)`);

  // ── 30. write.html: the nullities of RWT, 4, 1, 0, 0, 1, 0, 1, 0; every breadth written in A's own H from one known
  //    move, the same from a second; B's in its own H off by H_B/H_A, agreeing after one number; metres after one notch ──
  current = 'write.html';
  const before30 = failures.length;
  await page.goto(new URL('write.html', base).href, { waitUntil: 'load' });
  const wr = await page.evaluate(() => {
    const W = __write, out = { nul: [], eA: 0, eA2: 0, eB: 0, eBA: 0, eM: 0, free0: true, free6: true };
    for (const seed of [13, 5, 99]) {
      W.set({ seed, step: 0 }); const s = W.state(); out.nul.push(s.nullities.join(','));
      if (s.written.some(r => r.A !== undefined)) out.free0 = false;
      W.set({ step: 2 }); for (const r of W.state().written) out.eA = Math.max(out.eA, Math.abs(r.A / r.truth.inHA - 1));
      W.set({ step: 3 }); for (const r of W.state().written) out.eA2 = Math.max(out.eA2, Math.abs(r.A / r.truth.inHA - 1));
      W.set({ step: 4 }); const s4 = W.state(); for (const r of s4.written) out.eB = Math.max(out.eB, Math.abs(r.A / r.B / (s4.HB / s4.HA) - 1));
      W.set({ step: 5 }); for (const r of W.state().written) out.eBA = Math.max(out.eBA, Math.abs(r.BinA / r.A - 1));
      W.set({ step: 6 }); if (W.state().written.some(r => r.m !== undefined)) out.free6 = false;
      W.set({ step: 7 }); for (const r of W.state().written) out.eM = Math.max(out.eM, Math.abs(r.m / r.truth.m - 1));
    }
    W.set({ seed: 13, step: 0 });
    return out;
  });
  const wrOk = wr.nul.every(n => n === '4,1,0,0,1,0,1,0') && wr.free0 && wr.free6 && Math.max(wr.eA, wr.eA2, wr.eB, wr.eBA, wr.eM) < 1e-9;
  if (!wrOk) failures.push(`[write.html] ${JSON.stringify(wr)}`);
  console.log(`${failures.length === before30 ? 'ok  ' : 'FAIL'} write.html (still free at each step ${wr.nul[0]}, in three scenes; one known move writes every breadth in A's own H (${wr.eA.toExponential(0)}), a second the same; B's off by H_B/H_A until one number is sent; metres after one notch (${wr.eM.toExponential(0)}))`);

  // ── 31. room.html: scaling the world moves no address, shape or room-unit size; moving a thing changes its address and
  //    not its shape, reshaping its shape and not its address; one known step writes the room and the things' places ──
  current = 'room.html';
  const before31 = failures.length;
  await page.goto(new URL('room.html', base).href, { waitUntil: 'load' });
  const rm = await page.evaluate(() => {
    const R = __room, out = { scale: 0, size: 0, writeRoom: 0, places: 0, order: true, moveAddr: false, moveShape: 0,
      reshapeShape: false, reshapeAddr: 0, hit: '', place: 0 };
    const rel = (a, b) => Math.abs(a / b - 1);
    const snap = () => R.NAMES.map(n => ({ a: R.address(n), s: R.shape(n), z: R.sizeInRoom(n) }));
    R.set({ lk: 0 }); const s0 = snap();
    for (const lk of [-2, Math.log10(7), 2]) {
      R.set({ lk }); const s1 = snap();
      s0.forEach((x, i) => { out.scale = Math.max(out.scale, rel(s1[i].a.v2h, x.a.v2h), rel(s1[i].a.valt, x.a.valt), rel(s1[i].z, x.z),
        ...x.s.map((v, j) => v > 0 ? rel(s1[i].s[j], v) : 0)); });
      const w = R.writeRoom(1), k = Math.pow(10, lk);
      out.writeRoom = Math.max(out.writeRoom, rel(w.W, 5 * k), rel(w.D, 4 * k));
      for (const n of R.NAMES) { const c = R.thingAt(n).c; out.places = Math.max(out.places, rel(w.places[n].x, c[0]), rel(w.places[n].z, c[2])); }
    }
    R.set({ lk: 0 });
    for (const n of R.NAMES) for (const d of [1, 10, 1000]) out.size = Math.max(out.size, rel(R.sizeInRoom(n, d), R.sizeInRoom(n)));
    const ord = R.sweepOrder(); for (let i = 1; i < ord.length; i++) if (ord[i].g < ord[i - 1].g) out.order = false;
    const a0 = R.address('chair'), sh0 = R.shape('chair'); R.move('chair', [0.5, 0, -0.4]);
    const a1 = R.address('chair'), sh1 = R.shape('chair');
    out.moveAddr = Math.abs(a1.v2h - a0.v2h) > 1e-3; out.moveShape = Math.max(...sh0.map((v, j) => Math.abs(sh1[j] - v)));
    const b0 = R.address('table'), t0 = R.shape('table'); R.reshape('table');
    const b1 = R.address('table'), t1 = R.shape('table');
    out.reshapeShape = t1.some((v, j) => Math.abs(v - t0[j]) > 1e-3); out.reshapeAddr = Math.abs(b1.v2h - b0.v2h);
    const ta = R.address('ball'); R.set({ step: 2, alt: ta.alt * 180 / Math.PI, az: ta.az * 180 / Math.PI });
    out.hit = (R.hit(R.handDir()) || {}).name || 'none';
    R.set({ step: 6, stepTaken: true }); R.placeFromWall('chair', 1);
    const c = R.thingAt('chair'); out.place = Math.abs((c.c[2] + c.half[2]) - (R.room().D - 1));
    return out;
  });
  const rmOk = rm.scale < 1e-12 && rm.size < 1e-12 && rm.writeRoom < 1e-9 && rm.places < 1e-9 && rm.order && rm.moveAddr &&
    rm.moveShape < 1e-12 && rm.reshapeShape && rm.reshapeAddr < 1e-12 && rm.hit === 'ball' && rm.place < 1e-9;
  if (!rmOk) failures.push(`[room.html] ${JSON.stringify(rm)}`);
  console.log(`${failures.length === before31 ? 'ok  ' : 'FAIL'} room.html (scaling the world by 10⁻², 7, 10² moves no address, shape or room-unit size (${rm.scale.toExponential(0)}); a thing's size in room units the same at every distance; moving the chair changes its address and not its shape, reshaping the table its shape and not its address; the hand pointed at the ball meets it; one known step writes the room and every place (${rm.writeRoom.toExponential(0)}); the chair put 1 m from the wall)`);

  // ── 32. room-walk.html: walking the path places every thing from directions alone, in H (the first leg), exactly; the
  //    central sweep's shape and every place and breadth in H unmoved by scaling the world, the radii and metres moved by k;
  //    walking round a thing fills its central sweep; counting one leg writes the metres ──
  current = 'room-walk.html';
  const before32 = failures.length;
  await page.goto(new URL('room-walk.html?walk=path', base).href, { waitUntil: 'load' });
  const rw = await page.evaluate(() => {
    const R = __roomWalk, out = { near: null, mid: null, far: null, placed: 0, exact: 0, scaleH: 0, scaleShape: 0, radiiK: 0, metresK: 0, one: '', round: 0 };
    const rel = (a, b) => Math.abs(a / b - 1);
    let r0 = R.set({ lk: 0, count: false, walk: R.PATH });
    out.placed = r0.placed.length;
    const L1 = r0.trueLegs[0];
    for (const x of r0.rows) out.exact = Math.max(out.exact, Math.abs(x.placeH[0] * L1 - x.truth.place[0]), Math.abs(x.placeH[1] * L1 - x.truth.place[1]),
      Math.abs(x.across * L1 - x.truth.across));
    const m0 = R.set({ count: true });
    for (const lk of [-2, Math.log10(7), 2]) {
      const k = Math.pow(10, lk), r1 = R.set({ lk, count: false });
      r1.rows.forEach((x, i) => { const y = r0.rows[i];
        out.scaleH = Math.max(out.scaleH, Math.abs(x.placeH[0] - y.placeH[0]), Math.abs(x.placeH[1] - y.placeH[1]), rel(x.across, y.across), Math.abs(x.dir - y.dir));
        x.shape.forEach((v, j) => { out.scaleShape = Math.max(out.scaleShape, rel(v, y.shape[j])); out.radiiK = Math.max(out.radiiK, rel(x.radii[j], k * y.radii[j])); }); });
      const m1 = R.set({ count: true });
      m1.rows.forEach((x, i) => { out.metresK = Math.max(out.metresK, rel(x.acrossM, k * m0.rows[i].acrossM)); });
    }
    // the tree through the window: near, both sweeps; farther, parallax only (placed exactly); far, a ray
    for (const [lf, key] of [[0.4, 'near'], [Math.log10(30), 'mid'], [Math.log10(8000), 'far']]) {
      const r = R.set({ lk: 0, count: false, lfar: lf, walk: R.PATH }), t = r.rows.find(x => x.name === 'tree'), L = r.trueLegs[0];
      out[key] = { regime: t.regime, central: t.central, resolved: t.resolved,
        err: t.placeH ? Math.hypot(t.placeH[0] * L - t.truth.place[0], t.placeH[1] * L - t.truth.place[1]) / Math.hypot(...t.truth.place) : null };
    }
    R.set({ lfar: Math.log10(30) });
    // no fixed frame: whatever way the reader first faces, its map is the room's turned by that facing, exactly
    out.faces = 0;
    for (const f of [0, 2, -2.5]) { const r = R.set({ face0: f, walk: R.PATH }), L = r.trueLegs[0];
      for (const x of r.rows) if (x.placeH) out.faces = Math.max(out.faces, Math.abs(x.placeH[0] * L - x.truth.place[0]), Math.abs(x.placeH[1] * L - x.truth.place[1])); }
    R.set({ face0: 0.4 });
    const one = R.set({ lk: 0, count: false, walk: [R.PATH[0]] }); out.one = `${one.placed.length} ${one.rows.every(x => x.dir != null && x.central === 1)}`;
    const rr = R.set({ walk: [[0.6, 0.6], ...R.roundPoints('table')] }); out.round = rr.rows.find(x => x.name === 'table').central;
    R.set({ walk: R.PATH });
    return out;
  });
  const rwOk = rw.placed === 5 && rw.near.regime === 'both sweeps' && rw.near.central >= 2 && rw.mid.regime === 'parallax only' &&
    rw.mid.central === 1 && rw.mid.err < 1e-9 && rw.far.regime === 'a ray' && rw.far.err === null && !rw.far.resolved && rw.exact < 1e-9 && rw.scaleH < 1e-9 && rw.scaleShape < 1e-12 && rw.radiiK < 1e-12 && rw.metresK < 1e-9 &&
    rw.one === '0 true' && rw.round >= 8 && rw.faces < 1e-9;
  if (!rwOk) failures.push(`[room-walk.html] ${JSON.stringify(rw)}`);
  console.log(`${failures.length === before32 ? 'ok  ' : 'FAIL'} room-walk.html (one standpoint: directions and one radius a thing, nothing placed; the path places all five from directions alone, in the first leg, exactly (${rw.exact.toExponential(0)}); scaling the world by 10⁻², 7, 10² moves no direction, place, breadth in H or shape, the radii and the metres by k; walking round the table gives ${rw.round} of its 16 directions; the tree at 2.5 m by both sweeps, at 30 m by parallax only (${rw.mid.err.toExponential(0)}), at 8 km a ray, unresolved; no fixed frame: faced three ways at first, the map the room's turned, exactly (${rw.faces.toExponential(0)}))`);

  // ── 33. one-read.html: one turn meets one point, the address (A's ray at θ) and the payload (the radius at 2θ) at it
  //    only with V = H; arc over chord and chord over arc, product 1, π/2 and 2/π at the end of the turn ──
  current = 'one-read.html';
  const before33 = failures.length;
  await page.goto(new URL('one-read.html', base).href, { waitUntil: 'load' });
  const orr = await page.evaluate(() => {
    const O = __oneRead; let gap1 = 0, gap2 = 1, gapHalf = 1, prod = 0;
    for (let t = 0.5; t < 90; t += 0.5) { gap1 = Math.max(gap1, O.gap(t, 1)); gap2 = Math.min(gap2, O.gap(t, 2)); gapHalf = Math.min(gapHalf, O.gap(t, 0.5));
      prod = Math.max(prod, Math.abs(O.read(t).product - 1)); }
    const e = O.read(90), c = O.read(45), r = O.set({ t: 30, c: 1 });
    return { gap1, gap2, gapHalf, prod, pay: Math.abs(e.payload - Math.PI / 2), addr: Math.abs(e.address - 2 / Math.PI), ratio: c.ratio, g: c.g,
      foot: Math.abs(r.foot - 0.75), height: Math.abs(r.height - Math.sqrt(3) / 4) };
  });
  const orOk = orr.gap1 < 1e-12 && orr.gap2 > 1e-4 && orr.gapHalf > 1e-4 && orr.prod < 1e-12 && orr.pay < 1e-12 && orr.addr < 1e-12 &&
    Math.abs(orr.ratio - 1) < 1e-12 && Math.abs(orr.g - 0.5) < 1e-12 && orr.foot < 1e-12 && orr.height < 1e-12;
  if (!orOk) failures.push(`[one-read.html] ${JSON.stringify(orr)}`);
  console.log(`${failures.length === before33 ? 'ok  ' : 'FAIL'} one-read.html (at V = H the ray at θ and the radius at 2θ meet at one point at every θ (${orr.gap1.toExponential(0)}), at V = 2H and V = H/2 they part; arc over chord times chord over arc 1 throughout, π/2 and 2/π at the end of the turn; at 45° v/h = 1 and g = ½; at 30° foot ¾, height √3/4)`);

  // ── 34. sweep-zero.html: counted by its own turn the readings are the Cauchy, median 1; a clock alike on both sides
  //    keeps the median, a lopsided one moves it, a flat screen puts it at half the frame; the legs compose by tangent
  //    addition and once round to no turn; a turn carries the Cauchy onto itself ──
  current = 'sweep-zero.html';
  const before34 = failures.length;
  await page.goto(new URL('sweep-zero.html', base).href, { waitUntil: 'load' });
  const sz = await page.evaluate(() => {
    const S = __sweepZero, m = {}; for (const k of ['turn', 'even', 'lopsided', 'screen', 'payload']) m[k] = S.median(k);
    const half = S.tally('turn', 45), full = S.tally('turn', 90), round = S.compose([50, 80, 70, 85, 75]), two = S.compose([30, 40]);
    let gEq = 0; for (let t = 0; t <= 90; t += 7.5) { const y = S.tally('turn', t); gEq = Math.max(gEq, Math.abs(y.share - y.g)); }
    S.set({ t: 35, legs: [] }); S.stop(); const st = S.state();
    return { m, halfN: half.n, fullMed: full.median, gEq, closed: round.closed, roundH: round.h, two: Math.abs(two.reading - Math.tan(70 * Math.PI / 180)),
      fixed: Math.max(S.fixed(37), S.fixed(90), S.fixed(-120)), afterStop: st };
  });
  const szOk = Math.abs(sz.m.turn - 1) < 1e-12 && Math.abs(sz.m.even - 1) < 1e-6 && sz.m.lopsided > 1.3 && Math.abs(sz.m.screen - 2) < 1e-12 &&
    Math.abs(sz.m.payload - 1) > 0.05 && sz.halfN === 101 && Math.abs(sz.fullMed - 1) < 1e-12 && sz.gEq < 1e-12 && sz.closed && Math.abs(sz.roundH - 1) < 1e-12 &&
    sz.two < 1e-12 && sz.fixed < 1e-3 && sz.afterStop.t === 0 && sz.afterStop.legs.length === 1 && sz.afterStop.legs[0] === 35;
  if (!szOk) failures.push(`[sweep-zero.html] ${JSON.stringify(sz)}`);
  console.log(`${failures.length === before34 ? 'ok  ' : 'FAIL'} sweep-zero.html (counted by its own turn the share counted is the share turned and the median 1, half the counts by the corner; a clock alike on both sides keeps 1, a lopsided one moves it to ${sz.m.lopsided.toFixed(2)}, a flat screen to 2, half its edge; a stop is a new zero; 30° then 40° compose to tan 70°, once round to no turn; a turn carries the Cauchy onto itself (${sz.fixed.toExponential(0)}))`);

  // ── 35. writer-readers.html: one standpoint reads directions and no size; a second, one step H away, sizes the box in H;
  //    the step counted writes metres; the writer walks it; scaling the world moves only the metres ──
  current = 'writer-readers.html';
  const before35 = failures.length;
  await page.goto(new URL('writer-readers.html', base).href, { waitUntil: 'load' });
  const wrd = await page.evaluate(() => {
    const W = __writerReaders, T = W.truth(1), r1 = W.rung1(1), r2 = W.rung2(1), r3 = W.rung3(1), wr = W.writer(1), out = { scale: 0, metres: 0, ghosts: 0 };
    for (const k of [0.01, 7, 100]) {
      const a = W.rung1(k), b = W.rung2(k);
      out.scale = Math.max(out.scale, Math.abs(a.left.v - r1.left.v), Math.abs(a.right.h - r1.right.h), Math.abs(b.VH - r2.VH), Math.abs(b.dH - r2.dH));
      out.metres = Math.max(out.metres, Math.abs(W.rung3(k).Vm / (k * r3.Vm) - 1), Math.abs(W.writer(k).Vm / (k * wr.Vm) - 1));
    }
    // every ghost reads its edges along the same two directions from A
    for (const g of W.ghosts(1)) { const a = Math.atan2(g.d, g.x0), b = Math.atan2(g.d, g.x0 + g.V);
      out.ghosts = Math.max(out.ghosts, Math.abs(a - Math.atan2(r1.left.v, r1.left.h)), Math.abs(b - Math.atan2(r1.right.v, r1.right.h))); }
    // the writer's ruler, the number line: every stride the same length; a reader's lay: strides shorter past its corner
    const R = W.rulers(1), xs = R.ticks.map(R.writer), ys = R.ticks.map(R.reader), dw = xs.slice(1).map((x, i) => x - xs[i]), dr = ys.slice(1).map((y, i) => y - ys[i]);
    out.lineSpread = Math.max(...dw) - Math.min(...dw); out.layShrinks = dr[dr.length - 1] < 0.5 * dr[0];
    return Object.assign(out, { size1: r1.size, product: r1.product, VH: r2.VH, trueVH: T.V / T.step, Vm: r3.Vm, trueV: T.V, wV: wr.Vm, wD: wr.Dm, depthH: r2.depthH });
  });
  const wdrOk = wrd.size1 === null && wrd.lineSpread < 1e-12 && wrd.layShrinks && Math.abs(wrd.product - 1) < 1e-15 && Math.abs(wrd.VH - wrd.trueVH) < 1e-9 && Math.abs(wrd.Vm - wrd.trueV) < 1e-9 &&
    Math.abs(wrd.wV - 3) < 1e-9 && Math.abs(wrd.wD - 1) < 1e-9 && wrd.depthH === null && wrd.scale < 1e-9 && wrd.metres < 1e-9 && wrd.ghosts < 1e-12;
  if (!wdrOk) failures.push(`[writer-readers.html] ${JSON.stringify(wrd)}`);
  console.log(`${failures.length === before35 ? 'ok  ' : 'FAIL'} writer-readers.html (one standpoint: the frame, product 1, no size, every box along the same rays alike; two standpoints a step apart: V*/H = ${wrd.VH.toFixed(4)}, its depth unread; the step counted: ${wrd.Vm.toFixed(4)} m; the writer walks 3 m by 1 m; scaling the world by 10⁻², 7, 10² moves no reading and nothing in H, the metres by k; on the writer's number line every stride alike, on a reader's lay shorter past the corner)`);

  // ── 36. theorem6.html: (a) scaling, reshaping, reshuffling or thinning what arrives moves no address; (b) the median
  //    commutes with an increasing f, (c) the mean only with an affine one; (d) median 1, quartiles √2 ∓ 1, the mean
  //    climbing (2/π)·ln 10 a decade; (e) the line and the square's edges at the corner too, a lopsided weight off it ──
  current = 'theorem6.html';
  const before36 = failures.length;
  await page.goto(new URL('theorem6.html', base).href, { waitUntil: 'load' });
  const t6 = await page.evaluate(() => {
    const T = __theorem6, out = { moved: 0, med: 0, kept: {} };
    for (const op of ['none', 'scale', 'reshape', 'shuffle', 'thin']) { const s = T.set({ op, n: 25 }); out.moved = Math.max(out.moved, s.moved);
      out.med = Math.max(out.med, Math.abs(s.medianAfter - 1)); out.kept[op] = s.kept; }
    T.set({ op: 'none' });
    const X = T.readingsWith('none'), L = T.payload(), c = {};
    for (const f of ['affine', 'cube', 'sqrt', 'exp']) { const a = T.commute(X, f), b = T.commute(L, f);
      c[f] = { med: Math.max(Math.abs(a.medianFX - a.fMedianX), Math.abs(b.medianFX - b.fMedianX)), mean: Math.min(Math.abs(a.meanFX - a.fMeanX), Math.abs(b.meanFX - b.fMeanX)),
        jensen: f === 'cube' || f === 'exp' ? a.meanFX >= a.fMeanX && b.meanFX >= b.fMeanX : true }; }
    const q = T.quartiles('circle'), m4 = T.meanAt('circle', 10001), m5 = T.meanAt('circle', 100001);
    const meds = ['circle', 'line', 'square', 'lopsided'].map(p => T.medianAt(p, 100001));
    const climb = ['line', 'square'].map(p => T.meanAt(p, 100001) - T.meanAt(p, 10001));
    return Object.assign(out, { c, q, decade: m5 - m4, meds, climb });
  });
  const t6Ok = t6.moved < 1e-14 && t6.med < 1e-12 && t6.kept.thin === 13 && t6.kept.scale === 25 &&
    Object.values(t6.c).every(x => x.med < 1e-9 && x.jensen) && t6.c.affine.mean < 1e-9 && ['cube', 'sqrt', 'exp'].every(f => t6.c[f].mean > 1e-3) &&
    Math.abs(t6.q[0] - (Math.SQRT2 - 1)) < 1e-4 && Math.abs(t6.q[1] - (Math.SQRT2 + 1)) < 1e-3 && Math.abs(t6.decade - 2 / Math.PI * Math.LN10) < 1e-3 &&
    t6.meds.slice(0, 3).every(m => Math.abs(m - 1) < 1e-12) && t6.meds[3] > 1.2 && t6.climb.every(x => x > 1);
  if (!t6Ok) failures.push(`[theorem6.html] ${JSON.stringify(t6)}`);
  console.log(`${failures.length === before36 ? 'ok  ' : 'FAIL'} theorem6.html ((a) scaling, reshaping, reshuffling or thinning what arrives moves no address (${t6.moved.toExponential(0)}), the median at the corner; (b) the median commutes with x³, √x, eˣ and 2x + 1; (c) the mean only with 2x + 1, Jensen's way for the convex; (d) quartiles √2 ∓ 1, the mean climbing ${t6.decade.toFixed(4)} a decade; (e) the line and the square's edges with the median at 1 and no mean, a lopsided weight at ${t6.meds[3].toFixed(3)})`);

  // ── 37. head-turn.html: a pure turn (r = 0) places nothing and moves no shift; the head (r = 0.1 m, a quarter turn)
  //    places every post within the reach r·sin Δ/ε exactly; the eye alone reaches a few metres; fixating, the shift
  //    changes sign at the fixated distance ──
  current = 'head-turn.html';
  const before37 = failures.length;
  await page.goto(new URL('head-turn.html', base).href, { waitUntil: 'load' });
  const ht = await page.evaluate(() => {
    const H = __headTurn, out = {};
    const z = H.set({ r: 0, t: 90, eps: 'mrad' }); out.zeroPlaced = z.posts.filter(p => p.placed).length;
    out.zeroShift = Math.max(...[0.5, 1, 5, 100].map(d => Math.abs(H.shift(d, 2, 0, Math.PI / 3))));
    const a = H.set({ r: 0.1, t: 90, eps: 'mrad' }); out.reach = a.reach;
    out.headOk = a.posts.every(p => p.placed === (p.d < a.reach * 0.9)); out.headErr = Math.max(...a.posts.filter(p => p.placed).map(p => p.err));
    const b = H.set({ r: 0.1, t: 30 }), c = H.set({ r: 0.1, t: 150 }); out.r30 = b.reach; out.r150 = c.reach;
    const e = H.set({ r: 0.0076, t: 10, eps: 'arcmin' }); out.eyeReach = e.reach;
    out.flip = [0.5, 1.9, 2, 2.1, 50].map(d => H.shift(d, 2, 0.1, Math.PI / 6));
    H.set({ r: 0.1, t: 90, eps: 'mrad' });
    return out;
  });
  const htOk = ht.zeroPlaced === 0 && ht.zeroShift < 1e-12 && Math.abs(ht.reach - 100) < 1e-9 && ht.headOk && ht.headErr < 1e-9 &&
    Math.abs(ht.r30 - ht.r150) < 1e-9 && Math.abs(ht.r30 - 50) < 1e-9 && ht.eyeReach > 1 && ht.eyeReach < 10 &&
    ht.flip[0] > 0 && ht.flip[1] > 0 && Math.abs(ht.flip[2]) < 1e-12 && ht.flip[3] < 0 && ht.flip[4] < 0;
  if (!htOk) failures.push(`[head-turn.html] ${JSON.stringify(ht)}`);
  console.log(`${failures.length === before37 ? 'ok  ' : 'FAIL'} head-turn.html (a pure turn places nothing and shifts nothing; the head, 10 cm off its axis turned a quarter turn, reaches ${ht.reach.toFixed(0)} m at 1 mrad and places every post inside it exactly (${ht.headErr.toExponential(0)}); 30° and 150° reach alike, 50 m; the eye alone ${ht.eyeReach.toFixed(2)} m at 1 arcmin; fixating 2 m, nearer posts shift one way and farther the other)`);

  // ── 38. recover.html: recovering a body (RSH; SPN R348, R349): one reader at a Levels body's centre reads the sweep's own
  //    directions, the same for every body, the census a unit sphere; the wedge on the sphere holds an eighth of them, v ≤ h for
  //    half and the near field in both for a third, at any position; three readers, directions only, place every point in
  //    |AB| to rounding, and scaling the world moves nothing ──
  current = 'recover.html';
  const before38 = failures.length;
  await page.goto(new URL('recover.html?step=5', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__recover && __recover.frames > 2, null, { timeout: 30000 });
  const rv = await page.evaluate(() => { const X = __recover, a = X.recover(0), b = X.recover(7), k = X.recover(7, 1e3), o = {};
    o.rd = Math.max(a.rdErr, b.rdErr); o.cross = 0; o.kk = 0;
    for (let i = 0; i < a.reads.length; i++) for (let j = 0; j < 3; j++) { o.cross = Math.max(o.cross, Math.abs(a.reads[i][j] - b.reads[i][j]));
      if (k.rec[i] && b.rec[i]) o.kk = Math.max(o.kk, Math.abs(k.rec[i][j] - b.rec[i][j])); }
    o.rec = Math.max(a.recErr, b.recErr); o.fewest = Math.min(a.fewest, b.fewest);
    o.w = [[45, 35.26, 0], [120, -20, 30], [-60, 70, 100]].map(([lon, lat, roll]) => { const W = X.sharesOf(X.wedgeReadings(X.wedgeQuat(lon, lat, roll))); return [W.n / a.reads.length, W.vh, W.both]; });
    o.frames = X.frames; o.webgl = X.webgl; o.hud = X.hud();
    return o; });
  if (rv.rd > 1e-12 || rv.cross > 1e-12 || rv.rec > 1e-9 || rv.fewest < 2 || rv.kk > 1e-9 || !rv.webgl || rv.frames < 3
      || rv.w.some(([n, vh, both]) => Math.abs(n - 0.125) > 0.01 || Math.abs(vh - 0.5) > 0.02 || Math.abs(both - 1 / 3) > 0.02) || !/the body itself/.test(rv.hud))
    failures.push(`[${current}] ${JSON.stringify(rv)}`);
  console.log(`${failures.length === before38 ? 'ok  ' : 'FAIL'} ${current} (readings the sweep's own to ${rv.rd.toExponential(0)}, the same for two bodies; the wedge ${rv.w.map(w => w[0].toFixed(3)).join(', ')} of the sphere; points in |AB| to ${rv.rec.toExponential(0)}; ×10³ moves ${rv.kk.toExponential(0)})`);
  // step 6, many bodies (RSH runs 2–3): the census painted by body is the same with the world scaled; three readers at
  // ε = 0 place every seen point in |AB| to rounding at every distance, ×10³ moving none; at ε = 10⁻³ the nearest bodies
  // keep their shape, some far ones are a direction only, some are hidden, and the bands go out with a finer ε
  const before38b = failures.length;
  await page.goto(new URL('recover.html?step=6', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__recover && __recover.frames > 2, null, { timeout: 60000 });
  const many6 = await page.evaluate(() => { const X = __recover, W = X.many(), o = {};
    const near = W.dist.map((d, b) => [d, b]).sort((x, y) => x[0] - y[0]);
    const R0 = X.manyRead(0), R0k = X.manyRead(0, 1e3), R3 = X.manyRead(1e-3), R4 = X.manyRead(1e-4);
    o.e0 = Math.max(...R0.map(r => r.err0)); o.kk = 0;
    R0.forEach((r, b) => r.placed.forEach((q, n) => { const p = R0k[b].placed[n]; o.kk = Math.max(o.kk, Math.hypot(q[0] - p[0], q[1] - p[1], q[2] - p[2]) / Math.hypot(...q)); }));
    const bands = R => { const c = { shape: 0, place: 0, direction: 0, hidden: 0 }; R.forEach(r => c[r.band]++); return c; };
    o.b3 = bands(R3); o.b4 = bands(R4); o.b0 = bands(R0);
    o.nearShape = near.filter(([d, b]) => d < 8 && R3[b].band !== 'hidden').every(([d, b]) => R3[b].band === 'shape');
    o.farDir = near.filter(([d, b]) => d > 8000 && R3[b].band !== 'hidden').every(([d, b]) => R3[b].band === 'direction');
    // the census with the world scaled by 10³: the same body in every direction (a sample, the same marching)
    let diff = 0; const Fk = W.CEN.map((C, i) => X.placedBody(i, C, 1e3));
    for (let i = 0; i < W.dirs.length; i += 7){ const d = W.dirs[i]; let best = -1, bt = Infinity;
      Fk.forEach((f, b) => { const t = X.enterBody(f, [0, 0, 0], d); if (t !== null && t < bt){ bt = t; best = b; } }); if (best !== W.paint[i]) diff++; }
    o.paintDiff = diff; o.painted = [...W.paint].filter(b => b >= 0).length; o.hides = W.hides.size;
    o.frames = X.frames; o.hud = X.hud();
    return o; });
  if (many6.e0 > 1e-9 || many6.kk > 1e-9 || many6.paintDiff > 0 || many6.painted < 100 || !many6.nearShape || !many6.farDir || many6.b3.direction < 1 || many6.b3.hidden < 1
      || many6.b0.direction > 0 || many6.b4.shape + many6.b4.place < many6.b3.shape + many6.b3.place || many6.b4.shape < many6.b3.shape || !/no bands/.test(many6.hud))
    failures.push(`[${current} step 6] ${JSON.stringify(many6)}`);
  console.log(`${failures.length === before38b ? 'ok  ' : 'FAIL'} ${current} step 6 (many bodies: ${many6.painted} directions painted, the same at ×10³; at ε = 0 every point to ${many6.e0.toExponential(0)}; at ε = 10⁻³ shape ${many6.b3.shape}, place ${many6.b3.place}, direction ${many6.b3.direction}, hidden ${many6.b3.hidden}; at 10⁻⁴ shape ${many6.b4.shape}, place ${many6.b4.place})`);
  // step 7, the inscribed reader (RSH run 4): the whole wedge swept evenly, 256 × 256 addresses: whatever the bodies, v ≤ h
  // for half and the near field in both a third; the mirrored field's painted addresses at the corner; the painting the
  // same with the world scaled; the equal-angle readers exact at ε = 0 and banded at ε = 10⁻³
  const before38c = failures.length;
  await page.goto(new URL('recover.html?step=7&mirror=1', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__recover && __recover.frames > 2, null, { timeout: 60000 });
  const ins = await page.evaluate(() => { const X = __recover, o = {};
    const Wf = X.many('field'), Wm = X.many('mirror'), Mf = X.mapPaint(Wf), Mm = X.mapPaint(Wm), Mk = X.mapPaint(Wm, 1e3);
    o.all = [Mf.all.vh, Mf.all.both, Mm.all.vh, Mm.all.both]; o.mirror = Mm.painted.vh; o.field = Mf.painted.vh; o.metM = Mm.painted.n;
    o.dk = 0; for (let i = 0; i < Mm.paint.length; i++) if (Mk.paint[i] !== Mm.paint[i]) o.dk++;
    o.e0 = Math.max(...X.manyRead(0, 1, 'field', 'angle').map(r => r.err0));
    const R3 = X.manyRead(1e-3, 1, 'field', 'angle'), c = { shape: 0, place: 0, direction: 0, hidden: 0 }; R3.forEach(r => c[r.band]++); o.b3 = c;
    o.hud = X.hud(); o.frames = X.frames; return o; });
  if (ins.all.some((x, i) => Math.abs(x - (i % 2 ? 1 / 3 : 0.5)) > 0.003) || Math.abs(ins.mirror - 0.5) > 0.02 || ins.metM < 500 || ins.dk > 0
      || ins.e0 > 1e-9 || ins.b3.shape < 1 || ins.b3.direction < 1 || !/whatever the bodies/.test(ins.hud))
    failures.push(`[${current} step 7] ${JSON.stringify(ins)}`);
  console.log(`${failures.length === before38c ? 'ok  ' : 'FAIL'} ${current} step 7 (the inscribed reader: all addresses v ≤ h ${ins.all[0].toFixed(3)}, near field ${ins.all[1].toFixed(3)} with any bodies; the mirrored field's ${ins.metM} met at ${ins.mirror.toFixed(3)}, the field's at ${ins.field.toFixed(3)}; ×10³ moves none; equal-angle pixels: shape ${ins.b3.shape}, place ${ins.b3.place}, direction ${ins.b3.direction})`);

  // ── 39. moon.html: one moon (MON; SPN R352): the inscribed sweep's detections unmoved by scaling the world, its turn read
  //    from them to 1%, the smooth moon's time to contact and (with its radius carried in) its distance; the central sweep's
  //    painting R/GM the body's own, the same under k while its radii move by k, more of the face painted over the pass ──
  current = 'moon.html';
  const before39 = failures.length;
  await page.goto(new URL('moon.html?t=16&known=1', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__moon, null, { timeout: 60000 });
  const mo = await page.evaluate(() => { const M = __moon, o = { dk: 0, om: 0, tauS: 0, dS: 0 };
    for (const t of [3, 16, 28]) for (const k of [1e-3, 1e3]){ const a = new Set(M.detect(t, 1).det), b = M.detect(t, k).det; o.dk += Math.abs(a.size - b.length) + b.filter(x => !a.has(x)).length; }
    for (let t = 2; t < M.T - 2; t += 3){ const a = M.readout(t, false), b = M.readout(t, true);
      o.om = Math.max(o.om, Math.abs(a.om / a.truth.om - 1)); o.tauS = Math.max(o.tauS, Math.abs(b.tau / b.truth.tau - 1)); o.dS = Math.max(o.dS, Math.abs(b.dE / b.truth.d - 1)); }
    const P = M.paint(10), Q = M.paint(10, 7); o.pk = 0; o.rk = 0;
    if (P.held.length !== Q.held.length) o.pk = 1; else P.painting.forEach((x, n) => { o.pk = Math.max(o.pk, Math.abs(x - Q.painting[n])); o.rk = Math.max(o.rk, Math.abs(Q.radii[n] / P.radii[n] / 7 - 1)); });
    const ever = new Set(); for (let t = 0; t < M.T; t += 3) M.paint(t).held.forEach(i => ever.add(i)); o.ever = ever.size; o.once = P.held.length;
    o.hud = M.hud(); return o; });
  if (mo.dk > 0 || mo.om > 0.01 || mo.tauS > 0.08 || mo.dS > 0.02 || mo.pk > 1e-12 || mo.rk > 1e-12 || !(mo.ever > mo.once * 1.1) || !/radius known/.test(mo.hud))
    failures.push(`[${current}] ${JSON.stringify(mo)}`);
  console.log(`${failures.length === before39 ? 'ok  ' : 'FAIL'} ${current} (detections unmoved by ×10⁻³ and ×10³; ω to ${(100 * mo.om).toFixed(2)}%; the smooth moon's τ to ${(100 * mo.tauS).toFixed(1)}% and, its radius known, distance to ${(100 * mo.dS).toFixed(2)}%; the painting the same under k, radii ×k; ${mo.once} held at once, ${mo.ever} over the pass)`);

  // ── 40. from-home.html: the central sweep earned from home (CFH; SPN R355), on a slice through the moon: ranged points on
  //    the outline, the face from them exactly with the centre given; the hull containing the moon, tight where an edge grazed
  //    it and loose elsewhere; nothing in the detections or the hull moved by scaling the world, the ranges by k; with the
  //    centre fitted from the ranges, distance and speed written to 1% ──
  current = 'from-home.html';
  const before40 = failures.length;
  await page.goto(new URL('from-home.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__fromHome && window.__fromHome.last, null, { timeout: 60000 });
  const fh = await page.evaluate(() => { const F = __fromHome, R = F.last, o = {};
    o.on = R.onOutline; o.rc = R.cR.corr; o.ht = R.cHt.rms; o.hf = R.cHf.rms;
    o.inside = Math.min(...R.H.map((h, i) => (h - R.truth[i]) / 0.5));
    const A = F.ticks(31, 1, false), B = F.ticks(31, 1e3, false); o.dk = 0; o.rk = 0;
    A.forEach((a, i) => { const b = B[i]; if (a.lo !== b.lo || a.hi !== b.hi || a.hits.length !== b.hits.length) o.dk++; else a.hits.forEach((h, n) => { o.rk = Math.max(o.rk, Math.abs(b.hits[n].rho / (1e3 * h.rho) - 1)); }); });
    const c = (D, k) => { const s = F.silTrack(D); return F.hullOf(D, s.L.at, s.size); }, h1 = c(A), h2 = c(B); o.hk = Math.max(...h1.map((x, i) => Math.abs(x - h2[i])));
    F.set({ fit: true }); const Q = F.last, e = Q.rT.at(31), d = Math.hypot(...F.centre(31)); o.dist = Math.abs(Math.hypot(...e) / d - 1); o.speed = Math.abs(Math.hypot(...Q.rT.v) - 1);
    o.hud = F.hud(); return o; });
  if (fh.on > 1e-9 || fh.rc < 0.999 || fh.inside < -0.03 || !(fh.hf > 5 * fh.ht) || fh.dk > 0 || fh.rk > 1e-12 || fh.hk > 1e-12 || fh.dist > 0.01 || fh.speed > 0.01 || !/no metres/.test(fh.hud))
    failures.push(`[${current}] ${JSON.stringify(fh)}`);
  console.log(`${failures.length === before40 ? 'ok  ' : 'FAIL'} ${current} (ranged points on the outline to ${fh.on.toExponential(1)}, the face at correlation ${fh.rc.toFixed(4)}; the hull contains the moon (${fh.inside.toFixed(4)}), rms ${fh.ht.toFixed(3)} where grazed, ${fh.hf.toFixed(3)} elsewhere; ×10³ moves no detection or hull, the ranges ×k; fitted, distance ${(100 * fh.dist).toFixed(2)}%, speed ${(100 * fh.speed).toFixed(2)}%)`);

  // ── 41. depth.html: what the floor throws away (DYH; SPN R374): the cells as points of the half-plane, half of the Cauchy
  //    in its own cell, every tile of area 1, parent to child arcosh 3/2 and siblings arcosh 3 at every level; neighbours
  //    across the middle 2j apart by the tree, one step with sideways neighbours; the kept cells adding to the whole; the
  //    floor's fade and the Cauchy's never closer than 0.22 ──
  current = 'depth.html';
  const before41 = failures.length;
  await page.goto(new URL('depth.html?L=6', base).href, { waitUntil: 'load' });
  const dp = await page.evaluate(() => { const D = __depth, o = {};
    o.share = Math.max(...[[0, 0], [5, 7], [20, 12345], [40, 2 ** 39]].map(([j, k]) => Math.abs(D.share(j, k) - 0.5)));
    o.area = Math.max(...[0, 3, 20, 40].map(j => Math.abs(D.area(j) - 1)));
    o.pc = Math.max(...[1, 6, 30].map(j => Math.abs(D.dist(D.cell(j, 1), D.cell(j - 1, 0)) - Math.acosh(1.5))));
    o.sib = Math.max(...[1, 6, 30].map(j => Math.abs(D.dist(D.cell(j, 0), D.cell(j, 1)) - Math.acosh(3))));
    o.tree = D.tree(511, 512); o.graph = D.graph(511, 512, 10); o.mid = Math.abs(D.dist(D.cell(10, 511), D.cell(10, 512)) - Math.acosh(3));
    o.digits = D.digits(0.8125, 4); o.drawn = Math.max(...[0, 4, 11].map(L => Math.abs(D.drawn(L) - 1)));
    o.best = D.bestGamma(); const s = D.set({ x: 0.8125, L: 4 }); o.k = s.k; o.sh = s.share;
    o.rhHalf = D.RH(0.0587335); o.rhOwn = D.RH(0.5); o.rg = D.RG(0.327648); o.hl = [D.halfLevel('step'), D.halfLevel('smooth')];
    o.th = ['cauchy', 'gauss', 'sech', 'laplace'].map(k => D.thresh(k, 1)); o.th10 = [D.thresh('cauchy', 10), D.thresh('gauss', 10)];
    o.win = D.windowOf(0.25, true); o.lap = D.maxima('laplace', 0.05, 1).length; return o; });
  if (dp.share > 1e-12 || dp.area > 1e-12 || dp.pc > 1e-9 || dp.sib > 1e-9 || dp.tree !== 20 || dp.graph !== 1 || dp.mid > 1e-9 || dp.digits !== '1101' ||
    dp.drawn > 1e-12 || Math.abs(dp.best.diff - 0.2227) > 1e-3 || dp.k !== 13 || Math.abs(dp.sh - 0.5) > 1e-12 ||
    Math.abs(dp.rhHalf - 0.5) > 1e-5 || Math.abs(dp.rhOwn - 0.026855) > 1e-5 || Math.abs(dp.rg - 0.5) > 1e-4 ||
    Math.abs(dp.hl[0] + 3.0897) > 1e-3 || Math.abs(dp.hl[1] + 2.6098) > 1e-3 || Math.abs(dp.th[0] - 2 / Math.sqrt(3)) > 1e-4 ||
    Math.abs(dp.th[1] - 2) > 1e-4 || Math.abs(dp.th[2] - 2 * Math.atanh(1 / Math.sqrt(3))) > 1e-4 || dp.th[3] !== 0 ||
    Math.abs(dp.th10[0] - 3.4062) > 1e-3 || Math.abs(dp.th10[1] - 3.3540) > 1e-3 || Math.abs(dp.win - 0.369518) > 1e-5 || dp.lap !== 2)
    failures.push(`[${current}] ${JSON.stringify(dp)}`);
  console.log(`${failures.length === before41 ? 'ok  ' : 'FAIL'} ${current} (the Cauchy from a cell's point puts half in the cell, every tile's area 1, parent to child arcosh 3/2 and siblings arcosh 3 at every level; across the middle of level 10 the tree takes 20 steps, the tiling 1; 0.8125 is 0.1101, cell 13 of 16; the kept cells add to the whole; the fades never closer than ${dp.best.diff.toFixed(4)}; a step half kept ${(-dp.hl[0]).toFixed(2)} levels coarser than the reader's own cell, a smooth bump ${(-dp.hl[1]).toFixed(2)}; two equal sources part at Cauchy 2/√3, Gaussian 2, sech² 2·artanh(1/√3), a cusp at once, a tenfold fainter one later (Cauchy ${dp.th10[0].toFixed(3)}, Gaussian ${dp.th10[1].toFixed(3)}); the closed window at γ = ¼ ${dp.win.toFixed(5)})`);

  // ── 42. room-ratios.html: the room in ratios (SPN R386): the two inscribed sweeps' addresses unchanged by scaling the
  //    world or by a thing's ghost at ½ and 2 about the eye; a corner 45° across reads 1; one step's two rays cross at every
  //    corner, in steps, exactly; the map in steps unchanged by k; one counted stride writes metres; ratios between things ──
  current = 'room-ratios.html';
  const before42 = failures.length;
  await page.goto(new URL('room-ratios.html', base).href, { waitUntil: 'load' });
  const rr = await page.evaluate(() => { const R = __roomRatios, o = {};
    const addrs = () => R.NAMES.flatMap(n => R.corners(n).map(p => R.address(p, R.eyeA())));
    R.set({ k: 0 }); const a0 = addrs(), m0 = R.mapAll();
    o.k = 0; o.mk = 0; o.metres = 0;
    for (const lk of [-1, Math.log10(7), 1]) { R.set({ k: lk }); const a = addrs(), m = R.mapAll();
      o.k = Math.max(o.k, ...a.map((x, i) => Math.max(Math.abs(x.lr - a0[i].lr), Math.abs(x.ud - a0[i].ud))));
      for (const n of R.NAMES) { m[n].points.forEach((p, i) => p.forEach((x, j) => { o.mk = Math.max(o.mk, Math.abs(x - m0[n].points[i][j])); }));
        const t = R.truthIn(n, 1), c = m[n].centre.map(x => x * R.stepLen()); o.metres = Math.max(o.metres, ...t.map((x, j) => Math.abs(x - c[j]) / R.kOf())); } }
    R.set({ k: 0 }); const E = R.eyeA();
    o.ghost = Math.max(...R.NAMES.flatMap(n => R.corners(n).flatMap(p => [0.5, 2].map(f => { const q = E.map((e, i) => e + f * (p[i] - e));
      const x = R.address(q, E), y = R.address(p, E); return Math.max(Math.abs(x.lr - y.lr), Math.abs(x.ud - y.ud)); }))));
    const c45 = R.address([E[0] + 1, E[1] + 1, E[2] + Math.SQRT2], E); o.c45 = [c45.lr, c45.ud];
    o.steps = 0; o.gap = 0; const unit = Math.hypot(...R.eyeB().map((b, i) => b - E[i]));
    for (const n of R.NAMES) { const m = R.mapThing(n); o.gap = Math.max(o.gap, m.gap);
      R.corners(n).forEach((p, i) => p.forEach((x, j) => { o.steps = Math.max(o.steps, Math.abs(m.points[i][j] - (x - E[j]) / unit)); })); }
    const m = R.mapAll(), tc = n => Math.hypot(...R.truthIn(n, 1));
    o.ratio = Math.abs(R.ratios()[0][1] - tc('cabinet') / tc('ball'));
    o.ball = Math.abs(m.ball.size.across * unit - 0.3);
    R.set({ step: 1 }); o.s1 = document.getElementById('tab').textContent.includes('unread') && /nothing here says how far/.test(R.state().note);
    R.set({ step: 3 }); o.s3 = /metres/.test(R.state().say); return o; });
  if (rr.k > 1e-12 || rr.mk > 1e-9 || rr.metres > 1e-9 || rr.ghost > 1e-12 || Math.abs(rr.c45[0] - 1) > 1e-12 || Math.abs(rr.c45[1] - 1) > 1e-12 ||
    rr.steps > 1e-9 || rr.gap > 1e-9 || rr.ratio > 1e-9 || rr.ball > 1e-9 || !rr.s1 || !rr.s3)
    failures.push(`[${current}] ${JSON.stringify(rr)}`);
  console.log(`${failures.length === before42 ? 'ok  ' : 'FAIL'} ${current} (scaling the world by 10⁻¹, 7, 10 moves no address (${rr.k.toExponential(1)}) and no place in steps (${rr.mk.toExponential(1)}); a ghost at ½ and 2 about the eye the same addresses; 45° across and up reads 1 and 1; one step's rays cross at every corner, in steps, to ${rr.steps.toExponential(1)}; the counted stride writes metres to ${rr.metres.toExponential(1)}; the cabinet's distance over the ball's the referee's; from one place, distance unread)`);

  // ── 43. boost-sky.html: sampling a boosted sky (SPN R402, IMS run 1): the address part of the view change cancels from
  //    the Cauchy and from the payload tabled once; the table rebuilt per view falls behind at η = 4; the boost a pure slide ──
  current = 'boost-sky.html';
  const before43 = failures.length;
  await page.goto(new URL('boost-sky.html?eta=4', base).href, { waitUntil: 'load' });
  const bs = await page.evaluate(() => { const B = __boostSky, o = { zero: 0, cSpread: 0, mSpread: 0 }, cs = [], ms = [];
    for (const e of [0.5, 2, 4]) { const u = B.variance(e, 2, 'uniform'); o.zero = Math.max(o.zero, Math.abs(u.C), Math.abs(u.M));
      const v = B.variance(e, 2, 'sun'); cs.push(v.C); ms.push(v.M); o.beam = (o.beam ?? true) && B.variance(e, 4, 'sun').M < B.variance(e, 4, 'sun').C; }
    o.c = cs; o.m = ms; o.cSpread = Math.max(...cs) - Math.min(...cs); o.mSpread = Math.max(...ms) - Math.min(...ms);
    const t4 = B.variance(4, 2, 'sun'); o.t4 = t4.T; o.c4 = t4.C;
    o.slide = 0; for (const kind of ['cauchy', 'mixed']) for (const p of B.samples(kind, 4, 2, 'sun', 500)) o.slide = Math.max(o.slide, Math.abs(p.rest[0] - 4 - p.seen[0]));
    const c = B.samples('cauchy', 3, 2, 'uniform', 2000); o.meanRest = c.reduce((a, p) => a + p.restC, 0) / c.length;
    const l0 = B.lensStats(2, 0, 2, 'sun'), l5 = B.lensStats(2, 0.5, 2, 'uniform'); o.lens0 = Math.max(l0.residual, Math.abs(l0.bias));
    o.lensRes = l5.residual; o.lensBias = l5.bias;
    o.refit0 = B.lensRefitV(2, 0, 2, 'uniform', 1).V; o.refitW1 = B.lensRefitV(2, -0.5, 2, 'uniform', 1).V; o.refitW3 = B.lensRefitV(2, -0.5, 2, 'uniform', 3).V;
    o.ringN = 0; for (let i = 0; i < 20000; i++) { const th = Math.PI * (i + 0.5) / 20000; o.ringN += B.ringP(Math.cos(th), Math.sin(th), 0.8, 1) * 2 * Math.PI * Math.sin(th) * Math.PI / 20000; }
    o.onS = B.lensRefitV(0.5, 0.5, 2, 'uniform', 3).V; o.ringS = B.lensRingV(0.5, 0.5, 2, 'uniform', 3).V;
    B.set({ eta: 4, k: 2, sky: 'sun', show: 'table' }); o.tab = document.getElementById('tab').textContent; return o; });
  if (bs.zero > 1e-9 || bs.cSpread > 1e-6 || Math.abs(bs.c[0] - 124.75) > 0.01 || bs.mSpread > 1e-9 || Math.abs(bs.m[0] - 0.0684) > 0.001 ||
    !(bs.t4 > 10 * bs.c4) || !bs.beam || bs.slide > 1e-9 || Math.abs(bs.meanRest) > 0.05 || !bs.tab.includes('4,098') ||
    bs.lens0 > 1e-9 || !(bs.lensRes > 0.1) || !(Math.abs(bs.lensBias) > 0.05) ||
    !(Math.abs(bs.refit0) < 1e-3) || !(bs.refitW3 < 0.5 * bs.refitW1) ||
    Math.abs(bs.ringN - 1) > 1e-6 || !(Math.abs(bs.ringS) < 0.1 * bs.onS))
    failures.push(`[${current}] ${JSON.stringify(bs)}`);
  console.log(`${failures.length === before43 ? 'ok  ' : 'FAIL'} ${current} (a uniform sky's V 0 for the Cauchy and the payload tabled once at every η (${bs.zero.toExponential(1)}); with a sun the Cauchy's V ${bs.c[0].toFixed(2)} and the mixed sampler's ${bs.m[0].toFixed(4)} the same at η 0.5, 2, 4; the table rebuilt per view ${Math.round(bs.t4)} at η = 4; with beaming the mixed below the Cauchy; the boost a slide of η to ${bs.slide.toExponential(1)}; no lens a spherical Cauchy to ${bs.lens0.toExponential(1)}, a lens of 0.5 off by ${(100 * bs.lensRes).toFixed(0)}% and the one-z shortcut biased ${(100 * bs.lensBias).toFixed(0)}%; refit, unbiased, V ${bs.refit0.toExponential(1)} with no lens, ${bs.refitW1.toFixed(4)} and ${bs.refitW3.toFixed(4)} for one and three z's at λ = −0.5; a squeezing lens at η = 0.5 V ${bs.onS.toFixed(3)} on the axis, ${bs.ringS.toFixed(4)} with three rings off it)`);

  // ── 44. payload-free.html: the payload doesn't matter (SPN R405): every world, at every size or of unknown size, gives
  //    back the turn's own readings, median at the corner; the paint differs; the equal-metres reader moves with the size ──
  current = 'payload-free.html';
  const before44 = failures.length;
  await page.goto(new URL('payload-free.html?world=stars&s=unknown', base).href, { waitUntil: 'load' });
  const pf = await page.evaluate(() => { const P = __payloadFree, o = { worst: 0, med: 0, split: true, paints: new Set(), cases: 0 };
    for (const n of [15, 63, 255]) { const turn = P.fan(n).map(Math.tan);
      for (const [w] of P.WORLDS) for (const s of [0, 3, 6, 12, 15]) { const v = P.readings(w, s, n).map(r => r.v_h); o.cases++;
        v.forEach((x, k) => { o.worst = Math.max(o.worst, Math.abs(x - turn[k]) / turn[k]); });
        o.med = Math.max(o.med, Math.abs(P.median(v) - 1));
        if (v.filter(x => x < 1 - 1e-12).length !== (n - 1) / 2 || v.filter(x => x > 1 + 1e-12).length !== (n - 1) / 2) o.split = false;
        if (n === 15 && s === 0) o.paints.add(P.readings(w, s, n).map(r => r.col).join()); } }
    o.paints = o.paints.size; const a = P.metresFan(1e3, 15), b = P.metresFan(1e6, 15);
    o.metresMove = Math.abs(a[0] - b[0]); o.metresNone = P.metresFan(null, 15) === null && P.metresFan(Infinity, 15) === null;
    o.page = P.state().last;
    P.set({ sweep: 0.5 }); o.half = P.state().last; P.set({ sweep: 0 }); o.none = P.state().last; P.set({ sweep: 1 }); return o; });
  // the sweep: half way, half the addresses passed and only their payloads seen; at zero nothing arrived; the readings unmoved
  if (pf.half.shown !== 32 || !(pf.half.seen > 0 && pf.half.seen <= 32) || pf.none.shown !== 0 || pf.none.seen !== 0 || pf.half.worst > 1e-14) failures.push(`[${current}] sweep ${JSON.stringify([pf.half, pf.none])}`);
  if (pf.worst > 1e-14 || pf.med > 1e-12 || !pf.split || pf.paints < 7 || !(pf.metresMove > 1e-3) || !pf.metresNone ||
    pf.page.worst > 1e-14 || pf.page.metres !== null || pf.page.met !== 63)
    failures.push(`[${current}] ${JSON.stringify(pf)}`);
  console.log(`${failures.length === before44 ? 'ok  ' : 'FAIL'} ${current} (${pf.cases} worlds, sizes and fans give back the turn's own readings to ${pf.worst.toExponential(1)}, the median at the corner, half either side; ${pf.paints} different paints; the equal-metres reader moves with the size and has nothing to space against when it is unknown)`);

  // ── 45. payload-free-3d.html: the same in three dimensions: every world at every size or of unknown size gives back the
  //    sweep's own [h : v : v₂], so every count is the grid's (a half each side of every corner, the near field a third);
  //    the paint differs; the equal-metres screen needs the size; WebGL drew frames (three.js served as for check 22) ──
  current = 'payload-free-3d.html';
  const before45 = failures.length;
  await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/three@0\.160\.0\//, async route => {
    const rel = new URL(route.request().url()).pathname.replace('/npm/three@0.160.0/', '');
    try { await route.fulfill({ status: 200, contentType: 'text/javascript', body: await readFile(join(ROOT, 'node_modules/three', rel)) }); }
    catch { await route.continue(); }
  });
  await page.goto(new URL('payload-free-3d.html?world=room', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__payloadFree3d && __payloadFree3d.frames > 2, null, { timeout: 30000 }).catch(() => {});
  const p3 = await page.evaluate(() => { const P = __payloadFree3d, o = { worst: 0, cases: 0, counts: {}, paints: new Set() };
    for (const n of [16, 32]) { const G = P.grid(n), seen = new Set();
      for (const [w] of P.WORLDS) for (const s of [0, 6, 12, 15]) { const R = P.readings(w, s, n); o.cases++;
        R.forEach((r, k) => { const d = G[k].d; o.worst = Math.max(o.worst, Math.abs(r.vh - d[1] / d[0]) / (d[1] / d[0]), Math.abs(r.v2h - d[2] / d[0]) / (d[2] / d[0])); });
        seen.add(JSON.stringify(P.counts(R))); if (n === 16 && s === 0) o.paints.add(R.map(r => r.col ? r.col.join() : '-').join('|')); }
      o.counts[n] = [...seen].map(x => JSON.parse(x)); }
    o.paints = o.paints.size; const a = P.metresScreen(10, 16), b = P.metresScreen(1e4, 16);
    o.metresMove = Math.abs(a[5][1] - b[5][1]) > 1; o.metresNone = P.metresScreen(null, 16) === null;
    o.frames = P.frames; o.webgl = P.webgl; o.page = P.state().last;
    P.set({ sweep: 0.25 }); o.quarter = P.state().last; P.set({ sweep: 1 }); return o; });
  // the sweep: a quarter of the way, the first eight rows passed, every one meeting a wall of the room, the rest not yet seen
  if (p3.quarter.shown !== 256 || p3.quarter.seen !== 256 || p3.quarter.worst > 1e-14) failures.push(`[${current}] sweep ${JSON.stringify(p3.quarter)}`);
  const c32 = p3.counts[32];
  if (p3.worst > 1e-14 || p3.counts[16].length !== 1 || c32.length !== 1 || c32[0].v2LeH !== 0.5 || Math.abs(c32[0].vLeH - 0.5) > 0.01 ||
    Math.abs(c32[0].v2LeV - 0.5) > 0.01 || Math.abs(c32[0].near - 1 / 3) > 0.01 || p3.paints < 7 || !p3.metresMove || !p3.metresNone ||
    !p3.webgl || !(p3.frames > 2) || p3.page.met !== p3.page.N)
    failures.push(`[${current}] ${JSON.stringify(p3)}`);
  console.log(`${failures.length === before45 ? 'ok  ' : 'FAIL'} ${current} (${p3.cases} worlds, sizes and grids give back the sweep's own [h : v : v₂] to ${p3.worst.toExponential(1)}; one set of counts per grid, v ≤ h ${c32[0].vLeH}, v₂ ≤ h ${c32[0].v2LeH}, v₂ ≤ v ${c32[0].v2LeV}, the near field ${c32[0].near.toFixed(4)} at 32 × 32; ${p3.paints} paints; the equal-metres screen moves with the size and has none when it is unknown; WebGL drew ${p3.frames} frames)`);

  // ── 46. star-field.html: N is invisible to the reader (SPN R405, R406): every star back from its index; the reader's view
  //    (its share at each address) at N and 2N the same, ever closer as N grows, half past the corner; the writer's count
  //    doubles; the star pointed at is the star there; a star found by its index ──
  current = 'star-field.html';
  const before46 = failures.length;
  await page.goto(new URL('star-field.html?N=24', base).href, { waitUntil: 'load' });
  const sf = await page.evaluate(() => { const F = __starField, o = { bad: 0 };
    for (const j of [0, 1, 2, 5, 10, 20, 30, 40]) for (let k = 0; k < 12; k++) { const A = F.na(j), B = F.nr(j), ia = Math.floor((k * 0.618 % 1) * A), ir = Math.floor((k * 0.414 % 1) * B);
      const s = F.star(j, ia, ir), s2 = F.fromIndex(F.indexOf(s)); if (!s2 || s2.j !== j || s2.ia !== ia || s2.ir !== ir) o.bad++;
      if (!(s.r > (j ? 2 ** (j - 1) : 0) && s.r <= 2 ** j)) o.bad++; }
    o.diff = [20, 30, 40].map(m => { const a = F.readerView(2n ** BigInt(m), 512), b = F.readerView(2n ** BigInt(m + 1), 512);
      return [Math.max(...a.share.map((x, k) => Math.abs(x - b.share[k]))), a.near, b.near, a.total, Number(F.worldOf(2n ** BigInt(m)).N)]; });
    const inf = F.readerView(Infinity, 512); o.inf = [inf.near, inf.maxDev];
    o.Ns = [F.worldOf(2n ** 24n).N.toString(), F.worldOf(2n ** 25n).N.toString()];
    F.set({ m: 6 }); const s = F.star(2, 3, 1), [sx, sy] = F.toScr(s.R * Math.cos(s.th), s.R * Math.sin(s.th)), h = F.starNear(sx, sy);
    o.hover = !!h && F.indexOf(h) === F.indexOf(s); F.set({ m: 24 });
    F.set({ k: 0 }); const a0 = JSON.stringify(F.state().last.a0), st = F.star(12, 1000, 900), R0 = F.lay(st.r); o.near0 = F.state().last.near;
    F.set({ k: 6 }); o.Hsame = JSON.stringify(F.state().last.a0) === a0; o.slid = R0 - F.lay(st.r); o.near6 = F.state().last.near; F.set({ k: 0 });
    o.dist = [-4, 0, 12].map(k => { const H = 2 ** k, d = F.distanceAddresses(512, H); return [d.filter(x => x <= H * (1 + 1e-12)).length, d[0] / H]; });
    { const st = F.fromIndex(123456); F.set({ k: 0 }); const c0 = F.gridCell(st); F.set({ k: 6 }); const c6 = F.gridCell(st); F.set({ k: 0 });
      let mir = 0;
      const pos = k => { const b = Math.tan(k / 512 * Math.PI / 2); return b <= 1 ? b : 2 - 1 / b; }; for (let k = 1; k < 512; k++) mir = Math.max(mir, Math.abs(pos(512 - k) - (2 - pos(k))));
      o.grid = [c0.i === c6.i, c0.j !== c6.j, mir < 1e-12, F.inPlace(1) === 1, Math.abs(F.inPlace(4) - 1.75) < 1e-15]; }
    const g = F.goTo('123456789012'); o.goto = g && F.indexOf(g); o.info = document.getElementById('info').textContent; return o; });
  const [d20, d30, d40] = sf.diff;
  if (sf.bad || !(d20[0] < 0.02 && d30[0] < 1e-4 && d40[0] < 1e-7 && d30[0] < d20[0] && d40[0] < d30[0]) || sf.diff.some(d => d[1] !== 0.5 || d[2] !== 0.5 || d[3] !== d[4]) ||
    sf.inf[0] !== 0.5 || !(sf.inf[1] < 1e-9) || !(BigInt(sf.Ns[1]) >= 2n * BigInt(sf.Ns[0]) - 2n * 3n * 2n ** 11n) || !sf.hover || !sf.Hsame || sf.grid.some(x => !x) || !(Math.abs(sf.slid - 6 * Math.LN2) < 1e-9) || sf.near0 !== '4' || sf.near6 !== '16384' ||
    sf.dist.some(([c, w]) => c !== 256 || Math.abs(w - Math.tan(Math.PI / 1024)) > 1e-12) || sf.goto !== '123456789012' || !sf.info.includes('123,456,789,012'))
    failures.push(`[${current}] ${JSON.stringify(sf)}`);
  console.log(`${failures.length === before46 ? 'ok  ' : 'FAIL'} ${current} (every star back from its index at levels 0–40; the reader's view at N and 2N apart by at most ${sf.diff.map(d => d[0].toExponential(1)).join(', ')} at N = 2^20, 2^30, 2^40, half past the corner at every N and at ∞; the writer counts ${sf.Ns.join(' then ')}; the star pointed at is the star there; H from 1 to 64 u leaves the reader's view as it was and slides a star 6 ln 2, 4 then 16,384 stars inside it; 256 of 512 distance addresses inside H at H = 2^−4, 1, 2^12; in the K × K a star's direction address unmoved by H, its distance address moved, the far rings the near reflected about H; star #123,456,789,012 found)`);

  // ── 47. star-field-3d.html: the same in 3D, with H (SPN R405, R406): every star back from its index; the reader's view at
  //    N and 2N the same, ever closer as N grows, every pair at its corner and the near field a third; H moves nothing in
  //    the reader's view and slides each star along its own ray; the stars inside the corner counted; WebGL drew frames ──
  current = 'star-field-3d.html';
  const before47 = failures.length;
  await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/three@0\.160\.0\//, async route => {
    const rel = new URL(route.request().url()).pathname.replace('/npm/three@0.160.0/', '');
    try { await route.fulfill({ status: 200, contentType: 'text/javascript', body: await readFile(join(ROOT, 'node_modules/three', rel)) }); }
    catch { await route.continue(); }
  });
  await page.goto(new URL('star-field-3d.html?N=24', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__starField3d && __starField3d.frames > 2, null, { timeout: 30000 }).catch(() => {});
  const s3 = await page.evaluate(() => { const F = __starField3d, o = { bad: 0 };
    for (const j of [0, 1, 3, 8, 15, 20, 30]) for (let k = 0; k < 8; k++) { const ip = Math.floor((k * 0.618 % 1) * F.nPsi(j)), iy = Math.floor((k * 0.414 % 1) * F.nY(j)), ir = Math.floor((k * 0.732 % 1) * F.nR(j));
      const s = F.star(j, ip, iy, ir), s2 = F.fromIndex(F.indexOf(s)); if (!s2 || s2.j !== j || s2.ip !== ip || s2.iy !== iy || s2.ir !== ir) o.bad++;
      if (!(s.r > (j ? 2 ** (j - 1) : 0) && s.r <= 2 ** j)) o.bad++; }
    o.diff = [18, 30, 40].map(m => { const a = F.readerView(2n ** BigInt(m), 32), b = F.readerView(2n ** BigInt(m + 1), 32);
      return [Math.max(...a.share.map((x, k) => Math.abs(x - b.share[k]))), a.vh, a.v2h, a.v2v, a.near]; });
    F.set({ k: 0 }); const a0 = JSON.stringify(F.state().last.a); F.set({ k: 6 }); o.Hsame = JSON.stringify(F.state().last.a) === a0; o.near6 = F.state().last.near; F.set({ k: 0 });
    o.near0 = F.state().last.near;
    o.dist = [-4, 0, 12].map(k => { const H = 2 ** k, d = F.distanceAddresses(32, H); return [d.filter(x => x <= H * (1 + 1e-12)).length, d[0] / H]; });
    const st = F.star(12, 1000, 700, 900), p1 = F.placeOf(st, 1), p2 = F.placeOf(st, 64), n1 = Math.hypot(...p1), n2 = Math.hypot(...p2);
    o.sameRay = Math.max(...p1.map((x, i) => Math.abs(x / n1 - p2[i] / n2))); o.slid = n1 - n2;
    const g = F.goTo('98765432101234'); o.goto = g && F.indexOf(g); o.info = document.getElementById('info').textContent;
    o.webgl = F.webgl; o.frames = F.frames; o.drawn = F.drawn; return o; });
  const [e18, e30, e40] = s3.diff;
  if (s3.bad || !(e18[0] < 0.1 && e30[0] < 1e-4 && e40[0] < 1e-7) || s3.diff.slice(1).some(d => Math.abs(d[1] - 0.5) > 1e-6 || Math.abs(d[2] - 0.5) > 1e-6 || Math.abs(d[3] - 0.5) > 1e-6 || Math.abs(d[4] - 1 / 3) > 0.01) ||
    s3.dist.some(([c, w]) => c !== 16 || Math.abs(w - Math.tan(Math.PI / 64)) > 1e-12) ||
    !s3.Hsame || s3.near0 !== '8' || s3.near6 !== '2097152' || s3.sameRay > 1e-12 || !(Math.abs(s3.slid - 6 * Math.LN2) < 1e-9) ||
    s3.goto !== '98765432101234' || !s3.info.includes('98,765,432,101,234') || !s3.webgl || !(s3.frames > 2) || !(s3.drawn > 0))
    failures.push(`[${current}] ${JSON.stringify(s3)}`);
  console.log(`${failures.length === before47 ? 'ok  ' : 'FAIL'} ${current} (every star back from its index at levels 0–30; the reader's view at N and 2N apart by at most ${s3.diff.map(d => d[0].toExponential(1)).join(', ')} at N = 2^18, 2^30, 2^40, every pair at its corner and the near field ${e30[4].toFixed(3)}; H from 1 to 64 u leaves the reader's view as it was and slides a star 6 ln 2 along its own ray; 8 and 2,097,152 stars inside the corner; 16 of 32 distance addresses inside H at H = 2^−4, 1, 2^12, the first ${s3.dist[0][1].toFixed(4)} H wide at each; star #98,765,432,101,234 found; WebGL drew ${s3.frames} frames)`);

  // ── 48. star-dial.html: the dial on an infinite star field (21 Oct; Tom: "combine the dial with the wedge to browse an infinite
  //    starfield. we also need a way to set H."): every star back from its index at levels 0–30, level j holding 8^(j+1);
  //    every cell's four quarters adding to it exactly at three H; the drawn totals and stars adding to the held exactly in
  //    every state; the gold at tan 1 for a second moves the hand 0.4 and letting go re-centres on it; doubling H holds eight
  //    times the stars; a star found by its index at the triple corner, under the hand, and the same pixel at another H ──
  current = 'star-dial.html';
  const before48 = failures.length;
  await page.goto(new URL('star-dial.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__starDial && __starDial.frames > 2, null, { timeout: 30000 });
  const sd = await page.evaluate(() => { const S = __starDial, o = { bad: 0 };
    for (const j of [0, 1, 2, 5, 10, 15, 20, 25, 30]) for (let q = 0; q < 6; q++) { const N = 2 ** S.Dof(j), i = Math.floor((q * 0.618 % 1) * N), k = Math.floor((q * 0.414 % 1) * N), t = q % S.Mof(j);
      const s = S.star(j, i, k, t), s2 = S.fromIndex(S.indexOf(s)); if (!s2 || s2.j !== j || s2.i !== i || s2.k !== k || s2.t !== t) o.bad++; if (!(s.r > (j ? 2 ** (j - 1) : 0) && s.r <= 2 ** j)) o.bad++; }
    o.levels = [0, 1, 7, 20].every(j => BigInt(S.countBelow(j + 1)) - BigInt(S.countBelow(j)) === 8n ** BigInt(j + 1) && 4 ** S.Dof(j) * S.Mof(j) === 8 ** (j + 1));
    o.split = true; let seed = 7; const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
    for (const k of [-4, 0, 12]) for (let r = 0; r < 12; r++) { let n = S.ROOT; for (let d = 0; d < 44; d++) { const kids = S.kidsOf(n), sum = kids.reduce((a, c) => a + BigInt(S.count(c, k)), 0n);
      if (sum !== BigInt(S.count(n, k))) o.split = false; n = kids[Math.floor(rnd() * 4)]; } }
    o.root = [-4, 0, 4, 5, 12, 24].every(k => S.count(S.ROOT, k) === S.heldTotal(k));
    o.totals = []; const st = () => { const d = S.drawn; o.totals.push(d.total === d.held && BigInt(d.total) > 0n); };
    S.set({ mu1: 0, mu2: 0, lw: 1, lH: 0 }); st();
    const h = S.hold(1, 0, 1.0); o.zeta = Math.hypot(...h.zeta); const blue = h.blue, r = S.release();
    o.recentre = Math.max(...S.dispShares(...blue).map(x => Math.abs(x - 1 / 3))); o.mu = Math.max(Math.abs(r.mu1 - blue[0]), Math.abs(r.mu2 - blue[1])); st();
    S.set({ lw: -8 }); st(); S.set({ lH: 9 }); st();
    o.ratio = Number(BigInt(S.heldTotal(13))) / Number(BigInt(S.heldTotal(12)));
    const g = S.goTo('123456789012345'); o.goto = { centre: Math.max(...S.dispOfDir(g.dir).map(x => Math.abs(x - 1 / 3))), under: S.under(...S.lambdaOfDir(g.dir)), lH: S.view().lH }; st();
    const at = () => S.screen().find(x => x[0] === '123456789012345'); const p0 = at(); S.set({ lH: 13 }); const p1 = at(); st();
    o.still = !!(p0 && p1 && p0[1] === p1[1] && p0[2] === p1[2]); S.set({ lH: 14 });
    o.hud = S.hud(); o.frames = S.frames; return o; });
  if (sd.bad || !sd.levels || !sd.split || !sd.root || !sd.totals.every(Boolean) || Math.abs(sd.zeta - 0.4) > 1e-9 || sd.recentre > 1e-12 || sd.mu !== 0 ||
    Math.abs(sd.ratio - 8) > 0.01 || sd.goto.centre > 1e-6 || !sd.goto.under || sd.goto.under.index !== '123456789012345' || sd.goto.lH !== 14 || !sd.still ||
    !/adding to 10,540,996,612,321,181,696, exactly/.test(sd.hud) || !/read: star #123,456,789,012,345/.test(sd.hud) || !(sd.frames > 0))
    failures.push(`[${current}] ${JSON.stringify({ ...sd, hud: sd.hud.slice(0, 400) })}`);
  console.log(`${failures.length === before48 ? 'ok  ' : 'FAIL'} ${current} (every star back from its index at levels 0–30, level j holding 8^(j+1); every cell's quarters adding to it exactly at H = 2^−4, 1, 2^12; the drawn totals and stars adding to the held exactly in ${sd.totals.length} states; the gold at tan 1 for a second moves the hand ${sd.zeta.toFixed(3)}, letting go re-centres on it; doubling H holds ${sd.ratio.toFixed(3)} times the stars; star #123,456,789,012,345 at the triple corner (${sd.goto.centre.toExponential(0)}) and under the hand, the same pixel at H = 2^14 and 2^13)`);

  // ── 49. blueprint.html: one property, three vantages (22 Oct; Tom: "show the three observer vies, as a writer, a payload
  //    reader and the address reader"): scaling the world by 1/100, 7 and 100 moves the writer's lengths by k, the payload
  //    reader's ranges by k and its shape not at all, and no address; from every home half the turn lies either side of
  //    v = h; a ray from the living room's middle meets the kitchen wall 6 m east; every ray meets something ──
  current = 'blueprint.html';
  const before49 = failures.length;
  await page.goto(new URL('blueprint.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__blueprint, null, { timeout: 30000 });
  const bp = await page.evaluate(() => { const B = __blueprint, o = {}, ks = [0.01, 1, 7, 100];
    const pays = ks.map(k => B.payload(k, [12, 12]));
    o.shape = Math.max(...pays.map(p => Math.max(...p.rays.map((r, i) => Math.abs(r.shape - pays[1].rays[i].shape) / pays[1].rays[i].shape))));
    o.radii = Math.max(...pays.map((p, j) => Math.max(...p.rays.map((r, i) => Math.abs(r.r / ks[j] - pays[1].rays[i].r) / pays[1].rays[i].r))));
    o.addr = Object.keys(B.HOMES).every(h => { const a = ks.map(k => JSON.stringify(B.addresses(k, h).map(x => [x.what, x.ratio]))); return a.every(x => x === a[1]); });
    o.half = Object.keys(B.HOMES).map(h => B.addresses(1, h).filter(x => x.ratio < 1).length);
    o.writer = ks.map(k => B.writer(k).lot[0] / k);
    o.east = B.cast(B.world(1), 12, 12, 1, 0);
    o.open = pays.every(p => p.rays.every(r => isFinite(r.r) && r.what)) && Object.keys(B.HOMES).every(h => B.addresses(1, h).every(x => x.what));
    o.met = new Set(B.addresses(1, 'lot').map(x => x.what)).size;
    o.write = Object.keys(B.HOMES).map(h => { const w = ks.map(k => B.writeFrom(k, h));
      return { n: w[1].points.length, err: Math.max(...w.map(x => x.maxErr)), steps: Math.max(0, ...w.map(x => Math.max(0, ...x.points.map((p, i) => Math.hypot(p.steps[0] - w[1].points[i].steps[0], p.steps[1] - w[1].points[i].steps[1]))))),
        same: w.every(x => x.points.length === w[1].points.length) }; });
    return o; });
  if (!(bp.shape < 1e-12) || !(bp.radii < 1e-12) || !bp.addr || bp.half.some(n => n !== 128) || bp.writer.some(x => Math.abs(x - 48) > 1e-9) ||
    Math.abs(bp.east.d - 6) > 1e-12 || bp.east.what !== 'inner' || !bp.open || bp.met < 4 ||
    bp.write.some(w => w.n < 4 || !(w.err < 1e-9) || !(w.steps < 1e-9) || !w.same))
    failures.push(`[${current}] ${JSON.stringify(bp)}`);
  console.log(`${failures.length === before49 ? 'ok  ' : 'FAIL'} ${current} (the world scaled by 1/100, 7 and 100: the writer's lot 48 m × k, the payload reader's ranges by k (${bp.radii.toExponential(0)}) and its shape unmoved (${bp.shape.toExponential(0)}), no address moved; 128 of 256 addresses below v = h from every home; the kitchen wall 6 m east of the living room's middle; ${bp.met} things met from the lot's corner; one counted stride writes ${bp.write.map(w => w.n).join(', ')} corners from the four homes in metres to ${Math.max(...bp.write.map(w => w.err)).toExponential(0)}, their places in strides unmoved by k)`);

  // ── 50. blueprint-3d.html: the same in 3D (SPN R425): the payload reader's shell unmoved by k and its ranges by k; every
  //    address the same at every k, and the grid's counts (v ≤ h, v₂ ≤ h, v₂ ≤ v a half, the near field a third) from every
  //    home; one counted stride writing each room, in strides unmoved by k; WebGL drew frames ──
  current = 'blueprint-3d.html';
  const before50 = failures.length;
  await page.route(/^https:\/\/cdn\.jsdelivr\.net\/npm\/three@0\.160\.0\//, async route => {
    const rel = new URL(route.request().url()).pathname.replace('/npm/three@0.160.0/', '');
    try { await route.fulfill({ status: 200, contentType: 'text/javascript', body: await readFile(join(ROOT, 'node_modules/three', rel)) }); }
    catch { await route.continue(); }
  });
  await page.goto(new URL('blueprint-3d.html?write=1', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__blueprint3d && __blueprint3d.frames > 2, null, { timeout: 30000 }).catch(() => {});
  const b3 = await page.evaluate(() => { const B = __blueprint3d, o = {}, ks = [0.01, 1, 7, 100];
    const pays = ks.map(k => B.payload(k, B.SPOTS.living[1]));
    o.shape = Math.max(...pays.map(p => Math.max(0, ...p.rays.map((r, i) => isFinite(r.r) ? Math.abs(r.shape - pays[1].rays[i].shape) / pays[1].rays[i].shape : 0))));
    o.radii = Math.max(...pays.map((p, j) => Math.max(0, ...p.rays.map((r, i) => isFinite(r.r) ? Math.abs(r.r / ks[j] - pays[1].rays[i].r) / pays[1].rays[i].r : 0))));
    o.homes = Object.keys(B.HOMES).map(h => { const a = [1, 100, 0.01].map(k => B.addresses(k, h)), c = B.counts(a[0]);
      return { h, same: a.every(x => x.every((y, i) => y.what === a[0][i].what)), vh: c.vh, v2h: c.v2h, v2v: c.v2v, near: c.near, met: Object.keys(c.met).length }; });
    o.write = ['living', 'kitchen', 'garage'].map(h => { const w = ks.map(k => B.writeFrom(k, h));
      return { h, n: w[1].points.length, room: w[1].written.map(x => +x.toFixed(4)), err: Math.max(...w.map(x => x.maxErr)),
        steps: Math.max(0, ...w.map(x => Math.max(0, ...x.points.map((p, i) => Math.hypot(...p.steps.map((z, j) => z - w[1].points[i].steps[j])))))) }; });
    o.ws = ks.map(k => B.writerBox(k).hi.map(x => x / k));
    o.hz = 0;                                                // every point of every wedge's horizon on a face of the writer's box
    for (const h of Object.keys(B.HOMES)) for (const k of ks) { const W = B.wedgeHorizon(h, k), bx = B.writerBox(k);
      for (const p of W.edges.map(e => e.p).concat(W.arcs.flat())) { let m = Infinity;
        for (let i = 0; i < 3; i++) m = Math.min(m, Math.abs(p[i] - bx.lo[i]), Math.abs(p[i] - bx.hi[i])); o.hz = Math.max(o.hz, m / k); } }
    o.frames = B.frames; o.webgl = B.webgl; return o; });
  const rooms3 = { living: [12, 2.7, 8], kitchen: [12, 2.7, 6], garage: [7, 2.7, 7] };
  if (!(b3.shape < 1e-12) || !(b3.radii < 1e-12) || b3.homes.some(c => !c.same || Math.abs(c.vh - 0.5) > 0.01 || c.v2h !== 0.5 || Math.abs(c.v2v - 0.5) > 0.01 || Math.abs(c.near - 1 / 3) > 0.01 || c.met < 3) ||
    b3.write.some(w => w.n < 6 || !(w.err < 1e-9) || !(w.steps < 1e-9) || w.room.some((x, i) => Math.abs(x - rooms3[w.h][i]) > 1e-4)) || b3.ws.some(r => Math.abs(r[0] - 48) > 1e-9 || Math.abs(r[1] - 32) > 1e-9 || Math.abs(r[2] - 5.26) > 1e-9) || !(b3.hz < 1e-9) || !(b3.frames > 0) || !b3.webgl)
    failures.push(`[${current}] ${JSON.stringify(b3)}`);
  console.log(`${failures.length === before50 ? 'ok  ' : 'FAIL'} ${current} (the world scaled by 1/100, 7 and 100: the payload reader's 2,048 ranges by k (${b3.radii.toExponential(0)}), its shell unmoved (${b3.shape.toExponential(0)}); every address the same at every k from five homes, v ≤ h ${b3.homes[0].vh.toFixed(3)}, v₂ ≤ h ½, v₂ ≤ v ${b3.homes[0].v2v.toFixed(3)}, the near field ${b3.homes[0].near.toFixed(4)}; one counted stride writes ${b3.write.map(w => `the ${w.h} ${w.room[0]} × ${w.room[2]} × ${w.room[1]} m (${w.n} corners)`).join(', ')}, to ${Math.max(...b3.write.map(w => w.err)).toExponential(0)}, in strides unmoved by k; the writer's box 48 × 32 × 5.26 m × k, every wedge reaching its faces; WebGL drew ${b3.frames} frames)`);

  // ── 51. ground.html: one's own height as the base (Sedgwick's horizon ratio; SPN R433, R434): on level ground every thing's
  //    (tan E + tan F)/tan F is its V*/H and 1/tan F its d/H, exactly; the twin (one eye height) at the corner; scaling the world
  //    moves no reading, the metres by k; crouching moves the readings, not the metres; a tilted plane or a lifted foot misreads ──
  current = 'ground.html';
  const before51 = failures.length;
  await page.goto(new URL('ground.html', base).href, { waitUntil: 'load' });
  const gr = await page.evaluate(() => { const G = __ground, o = {}, ks = [0.01, 1, 7, 100];
    const tabs = ks.map(k => G.set({ k, H: 1.6, known: true, tilt: false, lift: false }));
    o.move = Math.max(...tabs.map(t => Math.max(...t.map((x, i) => Math.abs(x.ratio - tabs[1][i].ratio) + Math.abs(x.dist - tabs[1][i].dist)))));
    o.exact = Math.max(...tabs[1].map(x => x.err + x.distErr));
    const tw = tabs[1].find(x => x.name === 'a twin'); o.twin = [tw.ratio, tw.E];
    o.metres = Math.max(...tabs.map((t, j) => Math.max(...t.map((x, i) => Math.abs(x.written / (ks[j] * G.OBJECTS[i].V) - 1)))));
    const low = G.set({ k: 1, H: 0.8 }); o.crouchTwin = low.find(x => x.name === 'a twin').ratio;
    o.crouchMetres = Math.max(...low.map((x, i) => Math.abs(x.written - G.OBJECTS[i].V)));
    o.tiltErr = Math.max(...G.set({ H: 1.6, tilt: true }).map(x => x.err));
    const li = G.set({ tilt: false, lift: true }); o.liftErr = li.find(x => x.name === 'ball').err; o.liftOthers = Math.max(...li.filter(x => x.name !== 'ball').map(x => x.err));
    G.set({ lift: false, known: false }); return o; });
  if (!(gr.move < 1e-12) || !(gr.exact < 1e-12) || Math.abs(gr.twin[0] - 1) > 1e-12 || Math.abs(gr.twin[1]) > 1e-12 || !(gr.metres < 1e-12) ||
    Math.abs(gr.crouchTwin - 2) > 1e-12 || !(gr.crouchMetres < 1e-12) || !(gr.tiltErr > 0.1) || !(gr.liftErr > 0.5) || !(gr.liftOthers < 1e-12))
    failures.push(`[${current}] ${JSON.stringify(gr)}`);
  console.log(`${failures.length === before51 ? 'ok  ' : 'FAIL'} ${current} (level ground: every thing's (tan E + tan F)/tan F its V*/H and 1/tan F its d/H to ${gr.exact.toExponential(0)}; one eye height tall at the corner, its top on the horizon; the world scaled by 1/100, 7 and 100 moves no reading (${gr.move.toExponential(0)}), the metres by k; crouched to half height the twin reads 2 and the metres stay; a plane tilted ½° misreads by up to ${(100 * gr.tiltErr).toFixed(0)}%, the ball thrown up by ${(100 * gr.liftErr).toFixed(0)}%)`);

  // ── 52. writer-box.html: the writer's box and a reader's wedge inside it (SPN R445, R446): moving, turning, resizing and
  //    scaling the world change where the addresses land, never the addresses; every landing on a face of the box; the
  //    landings move by k exactly; at 32 × 32 every pair at its corner and the near field a third; a real drag of the
  //    gold ball moves the wedge; WebGL drew frames ──
  current = 'writer-box.html';
  const before52 = failures.length;
  await page.goto(new URL('writer-box.html', base).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__writerBox && __writerBox.ready && __writerBox.frames > 2, null, { timeout: 30000 }).catch(() => {});
  const wbx = await page.evaluate(() => { const W = __writerBox, o = { same: 0, face: 0, moved: 0 };
    const b0 = W.readAt({ n: 32 }), cases = [{ P: [4, 2, 3] }, { R: W.rotOf(-120, -20, 77) }, { R: W.octantRot([-1, 1, -1]) }, { k: 1e-3 }, { k: 1e3 }, { E: [3, 20, 5], P: [0.5, -7, 1] }];
    for (const c of cases) { const r = W.readAt({ n: 32, ...c }), k = c.k ?? 1, E = (c.E || W.state().E).map(x => x * k);
      for (const [i, a] of r.list.entries()) { const z = b0.list[i]; o.same = Math.max(o.same, Math.abs(a.h - z.h) + Math.abs(a.v - z.v) + Math.abs(a.v2 - z.v2));
        let m = Infinity; for (let q = 0; q < 3; q++) m = Math.min(m, Math.abs(Math.abs(a.p[q]) - E[q] / 2)); o.face = Math.max(o.face, m / k);
        if (!c.k) o.moved = Math.max(o.moved, Math.hypot(...a.p.map((x, q) => x - z.p[q]))); } }
    const k7 = W.readAt({ n: 16, k: 7 }), k1 = W.readAt({ n: 16, k: 1 }); o.kScale = Math.max(...k7.list.map((a, i) => Math.max(...a.p.map((x, q) => Math.abs(x - 7 * k1.list[i].p[q])))));
    o.c = b0.counts;
    // the three vantages (R447): the payload reader's shell unmoved by k, its mean by k; each view its camera
    const s1 = W.shellAt({ k: 1 }), s3 = W.shellAt({ k: 1e3 }); o.shell = Math.max(...s1.rel.map((x, i) => Math.abs(x - s3.rel[i]))); o.gm = s3.gm / s1.gm;
    o.cams = ['address', 'payload', 'writer'].map(v => { W.set({ view: v }); const c = W.camera(); return [v, c.kind, c.kind === 'perspective' && v === 'address' ? Math.hypot(...c.at.map((x, i) => x - W.state().P[i])) : null]; });
    o.p0 = W.state().P; o.ap = W.apexScreen(); o.frames = W.frames; o.webgl = W.webgl; return o; });
  await page.mouse.move(wbx.ap[0], wbx.ap[1]); await page.mouse.down(); await page.mouse.move(wbx.ap[0] + 50, wbx.ap[1] - 30, { steps: 5 }); await page.mouse.up();
  wbx.dragged = await page.evaluate(p0 => Math.hypot(...__writerBox.state().P.map((x, i) => x - p0[i])), wbx.p0);
  if (!(wbx.same === 0) || !(wbx.face < 1e-12) || !(wbx.moved > 1) || !(wbx.kScale < 1e-9) || wbx.c.vh !== 0.5 || wbx.c.v2h !== 0.5 || wbx.c.v2v !== 0.5 ||
    Math.abs(wbx.c.near - 1 / 3) > 0.01 || !(wbx.dragged > 0.3) || !(wbx.frames > 0) || !wbx.webgl ||
    !(wbx.shell < 1e-9) || Math.abs(wbx.gm / 1e3 - 1) > 1e-9 || wbx.cams[0][1] !== 'perspective' || !(wbx.cams[0][2] < 1e-9) || wbx.cams[2][1] !== 'orthographic')
    failures.push(`[${current}] ${JSON.stringify(wbx)}`);
  console.log(`${failures.length === before52 ? 'ok  ' : 'FAIL'} ${current} (moved, turned, resized and the world scaled by 10⁻³ and 10³: the 1,024 addresses unchanged, every landing on a face of the box (${wbx.face.toExponential(0)}), the landings moved by up to ${wbx.moved.toFixed(1)} and by k exactly; v ≤ h, v₂ ≤ h, v₂ ≤ v ½, the near field ${wbx.c.near.toFixed(4)}; a real drag moved the wedge ${wbx.dragged.toFixed(2)}; the three vantages: the writer's parallel rays, the address reader's camera at its standpoint, the payload reader's shell unmoved by k (${wbx.shell.toExponential(0)}) and its mean by k; WebGL drew frames)`);

  // ── 7. demos.html: every page it links to is there ──
  current = 'demos.html';
  const before7 = failures.length;
  await page.goto(new URL('demos.html', base).href, { waitUntil: 'load' });
  const links = await page.evaluate(() => [...document.querySelectorAll('main a')].map(a => a.href).filter(h => h.startsWith(location.origin)));
  const pages = [...new Set(links.map(h => new URL(h).pathname))];
  for (const pth of pages) {
    const r = await page.request.get(new URL(pth, base).href);
    if (!r.ok()) failures.push(`[demos.html] ${pth} answers ${r.status()}`);
  }
  if (pages.length < 14) failures.push(`[demos.html] links to only ${pages.length} pages`);
  await page.goto(new URL('index.html', base).href, { waitUntil: 'load' });
  await Promise.all([page.waitForURL(/demos\.html/, { timeout: 15000 }), page.click('#demosOpen')]);
  console.log(`${failures.length === before7 ? 'ok  ' : 'FAIL'} demos.html (${pages.length} pages, ${links.length} links)`);
} catch (e){
  failures.push(`[${current}] ${e.message.split('\n')[0]}`);
}

if (failures.length){
  console.error(`\n${failures.length} failure(s):\n` + failures.map(f => '  ' + f).join('\n'));
  code = 1;
} else {
  console.log('\nno uncaught errors, every lab returned a verdict');
}
await browser.close();
server?.close();
process.exit(code);
