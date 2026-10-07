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
  const tgt = await page.evaluate(() => __wanderLab.drawn().filter(o => !o.star && o.r > 2 && o.r < 10 && o.y > 80 && o.y < 650 && o.x > 100 && o.x < 1180).sort((a, b) => b.r - a.r)[0]);
  if (!tgt) failures.push('[moving] no small body in view to tap');
  else {
    await page.mouse.click(tgt.x + tgt.r + 10, tgt.y);   // beside it, not on it
    await page.waitForTimeout(300);
    const o = await page.evaluate(() => __wanderLab.where());
    if (!o.orbit || o.name !== tgt.name) failures.push(`[moving] a tap beside ${tgt.name} took ${o.orbit ? o.name : 'nothing'}`);
    else {
      await page.waitForFunction(t => __wanderLab.where().t > t + 5, o.t, { timeout: 180000, polling: 200 });
      const s1 = (await page.evaluate(() => __wanderLab.where())).span;
      if (!(s1 > 0.5)) failures.push(`[moving] five seconds after tapping, ${tgt.name} spans only ${s1.toFixed(2)} (it should come in to about 0.7)`);
      for (let i = 0; i < 10; i++){ await page.mouse.wheel(0, -200); await page.waitForTimeout(60); }
      const z0 = (await page.evaluate(() => __wanderLab.where())).t;
      await page.waitForFunction(t => __wanderLab.where().t > t + 3, z0, { timeout: 180000, polling: 200 });
      const s2 = (await page.evaluate(() => __wanderLab.where())).span;
      if (!(s2 > s1 * 1.3 && s2 > 0.9)) failures.push(`[moving] zooming in took ${tgt.name} only from ${s1.toFixed(2)} to ${s2.toFixed(2)} across`);
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
