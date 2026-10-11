// CUE run 2: the engine's textbook results (spinChecks) and every challenge (missed as set up, solved by its reference
// shot), read through play-trick.html's hooks. node plans/cue/checks.mjs > file
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { extname, join, normalize } from 'node:path';
const ROOT = fileURLToPath(new URL('../..', import.meta.url));
const server = createServer(async (req, res) => { const p = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '');
  try { const b = await readFile(join(ROOT, p)); res.writeHead(200, { 'Content-Type': extname(p) === '.html' ? 'text/html' : 'text/javascript' }); res.end(b); } catch { res.writeHead(404); res.end(); } });
await new Promise(ok => server.listen(0, '127.0.0.1', ok));
const browser = await chromium.launch(), page = await browser.newPage({ viewport: { width: 1280, height: 800 } });
await page.goto(`http://127.0.0.1:${server.address().port}/play-trick.html`, { waitUntil: 'load' });
const out = await page.evaluate(() => { const T = __trick, sc = T.spinChecks();
  const ch = T.challenges.map(c => { T.setChallenge(c.id); const start = T.check(); T.solve(); const sol = T.check(); return `${c.id}: as set up ${start === null ? 'solved' : 'missed'}, reference shot ${sol === null ? 'solves it' : 'misses (' + sol + ')'}`; });
  return { follow: sc.follow, followPred: sc.followPred, stun: sc.stun, draw: sc.draw, cutThrow: sc.cutThrow, sideThrow: sc.sideThrow, passed: sc.passed, backspinPassed: sc.backspinPassed, followGrip: sc.followGrip, ch }; });
for (const k of ['follow', 'followPred', 'stun', 'draw', 'cutThrow', 'sideThrow', 'passed', 'backspinPassed', 'followGrip']) console.log(`${k} ${out[k]}`);
for (const l of out.ch) console.log(l);
await browser.close(); server.close();
