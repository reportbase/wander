// Smoke test for Wander, in two parts, run in headless Chromium:
//
//   1. Fly: open the page, press Fly, look around with the mouse and fly with the
//      wheel and keys for a few seconds.
//   2. The labs: open ?lab=all, which runs every lab in turn (THE LAB GUIDE in
//      index.html asks for exactly this after every change), and wait for the
//      summary table.
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

  // ── 2. Every lab ──
  current = 'labs';
  const before = failures.length;
  await page.goto(new URL('index.html?lab=all', base).href, { waitUntil: 'load' });
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

  // ── 3. labs.html: every lab has a card, and one runs through the hidden frame ──
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
  console.log(`${failures.length === before3 ? 'ok  ' : 'FAIL'} labs.html (${cards.length} cards; BAL ${v})`);
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
