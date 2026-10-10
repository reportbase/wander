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
  // the tap lands 10 px beside the target: pick one with no other drawn body near that point, so the tap is its alone
  const tgt = await page.evaluate(() => { const all = __wanderLab.drawn();
    return all.filter(o => !o.star && o.r > 2 && o.r < 10 && o.y > 80 && o.y < 650 && o.x > 100 && o.x < 1180)
      .sort((a, b) => b.r - a.r)
      .find(o => all.every(b => b === o || Math.hypot(b.x - (o.x + o.r + 10), b.y - o.y) > b.r + 25)); });
  if (!tgt) failures.push('[moving] no small body in view to tap');
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
      for (let i = 0; i < 10; i++){ await page.mouse.wheel(0, -200); await page.waitForTimeout(60); }
      const z0 = (await page.evaluate(() => __wanderLab.where())).t;
      await page.waitForFunction(t => __wanderLab.where().t > t + 3, z0, { timeout: 180000, polling: 200 });
      const s2 = (await page.evaluate(() => __wanderLab.where())).span;
      // zoom comes in at a capped rate, so 3 s of it adds about a fixed amount, not a fixed factor: a later start (a slower
      // runner, s1 already 0.73) leaves less room under the closest approach; ask for a clear gain and a span past 0.9
      if (!(s2 > s1 + 0.15 && s2 > 0.9)) failures.push(`[moving] zooming in took ${tgt.name} only from ${s1.toFixed(2)} to ${s2.toFixed(2)} across`);
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
  console.log(`${failures.length === before11 ? 'ok  ' : 'FAIL'} gameplay sketches (far lights, resolving, the navigator's ladder, the sky fills)`);

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
  await page.goto(new URL('levels.html', base).href, { waitUntil: 'load' });
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
  console.log(`${failures.length === before13 ? 'ok  ' : 'FAIL'} levels.html (each level half the last; ${lv.v1} seen at a one-pixel grain, one fewer at two; the shape crosses ${lv.cross} ring edges, its broad form ${lv.broad}; size divided out, the depth averages 0 on the corner)`);
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
