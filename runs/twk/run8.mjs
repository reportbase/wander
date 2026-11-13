import { createRequire } from 'module'; const { chromium } = createRequire(import.meta.url)('playwright'); import http from 'http'; import fs from 'fs'; import path from 'path';
const root = process.cwd();   // run from the repository's root
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(8137);
const b = await chromium.launch(); const pg = await b.newPage(); const errs = []; pg.on('pageerror', e => errs.push(String(e)));
await pg.goto('http://localhost:8137/thumbs-walk.html'); await pg.waitForFunction(() => window.__thumbsWalk);
const g1 = await pg.evaluate(() => { const T = window.__thumbsWalk; let s = 12345; const rnd = () => (s = (s * 1103515245 + 12345) % 2147483648) / 2147483648; const out = [];
  for (let k = 0; k < 20; k++) { const x = Math.round((rnd() * 2 - 1) * 2500), z = Math.round((rnd() * 2 - 1) * 2500);
    T.set({ q: Math.floor(rnd() * 4), ky: Math.round((rnd() * 2 - 1) * 50), kp: Math.round((rnd() * 2 - 1) * 40), eye: [x, 2, z] });
    out.push({ x, z, ...T.againstStored() }); } return out; });
console.log('G1/G2'); for (const r of g1) console.log(JSON.stringify(r));
for (const X of ['0', '100000', '1' + '0'.repeat(15), '1' + '0'.repeat(30), '1' + '0'.repeat(100)]) {
  const r = await pg.evaluate(X => { const T = window.__thumbsWalk; const x = BigInt(X); T.set({ q: 1, ky: 18, kp: 0, eye: [T.Fr.make(x), T.Fr.make(2), T.Fr.make(x - 30n)] });
    const a = T.againstMade(1), c = T.againstMade(2); return { a, c, focus: T.digits().focus }; }, X);
  console.log('G3 X=1e' + (X.length - 1), JSON.stringify(r));
}
console.log('errors', errs); await b.close(); srv.close();
