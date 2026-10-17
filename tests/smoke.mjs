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
    const one = R.set({ lk: 0, count: false, walk: [R.PATH[0]] }); out.one = `${one.placed.length} ${one.rows.every(x => x.dir != null && x.central === 1)}`;
    const rr = R.set({ walk: [[0.6, 0.6], ...R.roundPoints('table')] }); out.round = rr.rows.find(x => x.name === 'table').central;
    R.set({ walk: R.PATH });
    return out;
  });
  const rwOk = rw.placed === 5 && rw.near.regime === 'both sweeps' && rw.near.central >= 2 && rw.mid.regime === 'parallax only' &&
    rw.mid.central === 1 && rw.mid.err < 1e-9 && rw.far.regime === 'a ray' && rw.far.err === null && !rw.far.resolved && rw.exact < 1e-9 && rw.scaleH < 1e-9 && rw.scaleShape < 1e-12 && rw.radiiK < 1e-12 && rw.metresK < 1e-9 &&
    rw.one === '0 true' && rw.round >= 8;
  if (!rwOk) failures.push(`[room-walk.html] ${JSON.stringify(rw)}`);
  console.log(`${failures.length === before32 ? 'ok  ' : 'FAIL'} room-walk.html (one standpoint: directions and one radius a thing, nothing placed; the path places all five from directions alone, in the first leg, exactly (${rw.exact.toExponential(0)}); scaling the world by 10⁻², 7, 10² moves no direction, place, breadth in H or shape, the radii and the metres by k; walking round the table gives ${rw.round} of its 16 directions; the tree at 2.5 m by both sweeps, at 30 m by parallax only (${rw.mid.err.toExponential(0)}), at 8 km a ray, unresolved)`);

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
