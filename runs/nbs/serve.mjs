// A tiny static server for the games clone, and a page on 9-ball with its debug hooks ready.
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join, extname } from 'node:path';
import { createRequire } from 'node:module';
const require = createRequire('/opt/node22/lib/node_modules/');
export const { chromium } = require('playwright');
export const GAMES = process.env.GAMES_HTML || '/home/user/games/games.html';
const ROOT = GAMES.replace(/\/[^/]*$/, ''), LIBS = process.env.LIBS_DIR || join(ROOT, 'node_modules');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.wasm': 'application/wasm', '.json': 'application/json' };
export function serve(){
  const s = createServer(async (q, r) => { try { const p = decodeURIComponent(new URL(q.url, 'http://x').pathname); const b = await readFile(join(ROOT, p));
    r.writeHead(200, { 'content-type': TYPES[extname(p)] || 'application/octet-stream' }); r.end(b); } catch { r.writeHead(404); r.end(); } });
  return new Promise(ok => s.listen(0, '127.0.0.1', () => ok(s)));
}
export async function ninePage(browser, port){
  const page = await browser.newPage({ viewport: { width: 640, height: 400 } });
  await page.route(u => !/^https?:\/\/127\.0\.0\.1[:/]/.test(u.href) && !/^(data|blob):/.test(u.href), async r => {
    const u = r.request().url(), lib = f => readFile(join(LIBS, f));
    if (/three\.module\.min\.js/.test(u)) return r.fulfill({ contentType: 'text/javascript', body: await lib('three/build/three.module.js') });
    if (/chess\.js@1\.4\.0/.test(u)) return r.fulfill({ contentType: 'text/javascript', body: await lib('chess.js/dist/esm/chess.js') });
    if (/unzipit/.test(u)) return r.fulfill({ contentType: 'text/javascript', body: await lib('unzipit/dist/unzipit.min.js') });
    return r.abort(); });
  page.on('pageerror', e => console.error('pageerror', e.message.slice(0, 200)));
  await page.goto(`http://127.0.0.1:${port}/games.html?app=nineball`, { waitUntil: 'domcontentloaded', timeout: 180000 });
  await page.waitForFunction(() => Array.isArray(window.FIELD_APPS) && window.FIELD_APPS.some(a => a.id === 'nineball') && typeof window.setFieldApp === 'function', null, { timeout: 180000 });
  await page.evaluate(() => { const A = window.FIELD_APPS.find(a => a.id === 'nineball'); window.setFieldApp(A); window.__N = A._debug; });
  return page;
}
