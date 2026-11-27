// NBS run 2 (plans/nbs-plan.md): B′, no scan, on PEB's event engine with its full signature (runs/peb/play-trick-event5.html).
// node runs/nbs/nbs2.mjs map cut 16 | map tworail 64 | ... ; node runs/nbs/nbs2.mjs report
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const part = process.argv[2], which = process.argv[3], S = +(process.argv[4] || 16);
const out = (w, s) => `runs/nbs/nbs2-${w}-${s}.json`;
const FLAG = { cut: [0.124, 0.145, 2.387, 3.958], tworail: [0.389] };   // PEB run 5's post hoc, the pieces with a hidden jump

if (part === 'report') {
  const L = []; const say = s => { console.log(s); L.push(s); };
  const med = a => { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : null; };
  const v = {};
  for (const w of ['cut', 'tworail']) {
    const A = JSON.parse(fs.readFileSync(out(w, 16), 'utf8')), B = JSON.parse(fs.readFileSync(out(w, 64), 'utf8'));
    const scan = 1024 + A.pebSteps, ctr = j => (j.lo + j.hi) / 2, nr = (a, b) => { const d = Math.abs(a - b) % (2 * Math.PI); return Math.min(d, 2 * Math.PI - d) < 1e-9; };
    A.cross = { aInB: A.jumps.filter(j => B.jumps.some(k => nr(ctr(j), ctr(k)))).length, bInA: B.jumps.filter(j => A.jumps.some(k => nr(ctr(j), ctr(k)))).length };
    say(`${w}: S=16 flights ${A.flights} (bisection steps ${A.steps}, leaf flights ${A.leafFlights}), ${A.jumps.length} jumps, ${A.pieces.length} pieces, dropped ${A.dropped} (widest ${A.dropWide.toExponential(1)}), capped ${A.capped}`);
    say(`   S=64 flights ${B.flights}, ${B.jumps.length} jumps, ${B.pieces.length} pieces, dropped ${B.dropped}, capped ${B.capped}`);
    say(`   the scan's flights 1,024 + ${A.pebSteps} = ${scan}`);
    say(`   PEB jumps found: ${A.pebFound}/${A.pebJumps} (S=64 ${B.pebFound}/${B.pebJumps}); missed at ${A.pebMissed.map(x => x.toFixed(6)).join(' ') || '-'}`);
    say(`   flagged pieces with a jump inside: ${A.flagged.filter(f => f.inside.length).length}/${A.flagged.length}: ${A.flagged.map(f => f.at + (f.inside.length ? ' [' + f.inside.map(x => x.toFixed(6)).join(' ') + ']' : ' none')).join('; ')}`);
    say(`   pieces wider than 1e-4: ${A.held.n}, held to 1e-6 by their K=8 bridge ${A.held.ok}; worst ${A.held.worst.toExponential(2)}`);
    say(`   S=16 against S=64: jumps of 16 found in 64 ${A.cross.aInB}/${A.jumps.length}, of 64 in 16 ${A.cross.bInA}/${B.jumps.length}; flights ratio ${(B.flights / A.flights).toFixed(3)}`);
    const P = A.pieces.length, J = A.jumps.length;
    say(`   cost bound 12K·P + 45·J = ${12 * 8 * P + 45 * J}; flights per piece ${(A.flights / P).toFixed(1)}; median halvings-depth width of pieces ${med(A.pieces.map(p => p.hi - p.lo)).toExponential(2)}`);
    v[w] = { A, B, scan, P, J };
  }
  const all = f => ['cut', 'tworail'].every(w => f(v[w]));
  say('C1 ' + (all(x => !x.A.capped && !x.B.capped && x.A.dropWide <= 1e-9 && x.B.dropWide <= 1e-9) ? 'not killed' : 'KILLED'));
  say('C2 ' + (all(x => x.A.pebFound === x.A.pebJumps) ? 'not killed' : 'KILLED'));
  const fl = ['cut', 'tworail'].reduce((s, w) => s + v[w].A.flagged.filter(f => f.inside.length).length, 0);
  say('C3 ' + (fl >= 4 ? 'not killed' : 'KILLED') + ` (${fl}/5)`);
  const hn = ['cut', 'tworail'].reduce((s, w) => s + v[w].A.held.n, 0), ho = ['cut', 'tworail'].reduce((s, w) => s + v[w].A.held.ok, 0);
  say('C4 ' + (ho / hn >= 0.95 ? 'not killed' : 'KILLED') + ` (${ho}/${hn})`);
  say('C5 ' + (all(x => x.A.cross.aInB === x.A.jumps.length && x.A.cross.bInA === x.B.jumps.length && Math.abs(x.B.flights / x.A.flights - 1) < 0.2) ? 'not killed' : 'KILLED'));
  say('C6 ' + (all(x => x.A.flights <= 2 * x.scan && x.A.flights <= 12 * 8 * x.P + 45 * x.J) ? 'not killed' : 'KILLED'));
  fs.writeFileSync('runs/nbs/nbs-run2.txt', L.join('\n') + '\n');
  process.exit(0);
}

const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const br = await chromium.launch(); const pg = await br.newPage(); pg.on('pageerror', e => console.log('page error', e.message)); pg.on('console', m => console.log(m.text()));
await pg.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event5.html`); await pg.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
const peb = JSON.parse(fs.readFileSync(`runs/peb/peb5-map-${which}.json`, 'utf8'));
const t0 = Date.now();
const r = await pg.evaluate(({ name, S, pebJ, pebP, flag }) => {
  const T = window.__trick, PI = Math.PI;
  const B = name === 'cut' ? [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)] : (T.setChallenge('tworail'), T.ballsNow().map(b => ({ ...b })));
  const pw = 14, obj = B.find(b => !b.cue).n;
  let flights = 0, steps = 0, leafFlights = 0, longest = 0, chatter = 0; const cache = new Map();
  const fly = a => { let v = cache.get(a); if (v) return v; flights++; if (DBG && flights > 8600) console.log('fly', flights, a);
    const s = T.simulateEvent(B, [Math.cos(a), Math.sin(a)], pw, null, 0), c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj);
    v = { s: hash(s.ev), n: s.ev.length, o: [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z] }; if (v.n > longest) longest = v.n; if (v.n > 10000) chatter++; cache.set(a, v); return v; };
  const K = 8, CAP = 200000, TOL = 1e-7, DBG = false;
  // the full signature kept as a 52-bit FNV-1a hash of its keys (a chattering shot has 600,000 events; the strings filled memory)
  const hash = ev => { let h1 = 0x811c9dc5, h2 = 0x01000193; for (const e of ev) { const k = e.key; for (let i = 0; i < k.length; i++) { const c = k.charCodeAt(i); h1 = Math.imul(h1 ^ c, 16777619) >>> 0; h2 = Math.imul(h2 ^ c, 2246822519) >>> 0; } h1 = Math.imul(h1 ^ 32, 16777619) >>> 0; } return h1 * 1048576 + (h2 & 0xfffff); };
    // Chebyshev–Lobatto leaves on [lo, hi] (the ends included, so every aim lies between two neighbouring leaves of some span)
  const nodes = (lo, hi) => Array.from({ length: K }, (_, j) => (lo + hi) / 2 - (hi - lo) / 2 * Math.cos(PI * j / (K - 1)));
  const lastCoeffs = ys => { const n = K - 1, c = [];   // DCT-I: Chebyshev coefficients from Lobatto values (in increasing x)
    for (const k of [n - 1, n]) { let s = 0; for (let j = 0; j <= n; j++) { const w = (j === 0 || j === n) ? 0.5 : 1; s += w * ys[n - j] * Math.cos(PI * k * j / n); } c.push(Math.abs(s * 2 / n * (k === n ? 0.5 : 1))); }
    return Math.max(...c); };
  const jumps = [], pieces = []; let dropped = 0, dropWide = 0, capped = false, iter = 0;
  const stack = []; for (let i = S - 1; i >= 0; i--) stack.push([2 * PI * i / S, 2 * PI * (i + 1) / S]);
  while (stack.length) {
    if (flights > CAP) { capped = true; break; }
    if (++iter % 20000 === 0) console.log('it', iter, 'flights', flights, 'stack', stack.length, 'jumps', jumps.length, 'pieces', pieces.length, 'cache', cache.size, 'span', stack.length ? (stack[stack.length-1][1]-stack[stack.length-1][0]).toExponential(2) + ' at ' + stack[stack.length-1][0].toFixed(6) : '');
    const [lo, hi] = stack.pop(), xs = nodes(lo, hi), before = flights, F = xs.map(fly); leafFlights += flights - before;
    let k = 0; while (k < K - 1 && F[k].s === F[k + 1].s) k++;
    if (k < K - 1 && hi - lo <= 1e-12) { jumps.push({ lo, hi, sL: F[0].s, sR: F[K - 1].s }); continue; }   // already a bracket: a jump, not cut again
    if (k < K - 1) {   // a change between leaves k and k+1: bisected, the span cut there
      let l = xs[k], h = xs[k + 1]; const sL = F[k].s;
      while (h - l > 1e-12) { const m = (l + h) / 2; if (m <= l || m >= h) break; steps++; if (fly(m).s === sL) l = m; else h = m; }
      jumps.push({ lo: l, hi: h, sL, sR: fly(h).s });
      stack.push([h, hi]); stack.push([lo, l]); continue;
    }
    let ok = true; for (let c = 0; c < 4 && ok; c++) ok = lastCoeffs(F.map(f => f.o[c])) < TOL;
    if (ok) { pieces.push({ lo, hi, s: F[0].s, xs, ys: F.map(f => f.o) }); continue; }
    if (hi - lo < 1e-12) { dropped++; dropWide = Math.max(dropWide, hi - lo); continue; }
    const m = (lo + hi) / 2; stack.push([m, hi]); stack.push([lo, m]);
  }
  const flightsMap = flights; console.log('mapped', flights, 'jumps', jumps.length, 'pieces', pieces.length, 'at', Date.now());
  // C2: every jump of PEB run 5 found within 1e-9, same signatures either side
  const near = (a, b) => { const d = Math.abs(a - b) % (2 * PI); return Math.min(d, 2 * PI - d); };
  let pebFound = 0; const pebMissed = [];
  for (const j of pebJ) { const c = (j.lo + j.hi) / 2, sL = fly(j.lo).s, sR = fly(j.hi).s;
    if (jumps.some(b => near((b.lo + b.hi) / 2, c) < 1e-9 && b.sL === sL && b.sR === sR)) pebFound++; else pebMissed.push(c); }
  // C3: inside each flagged piece of PEB run 5, a B′ jump
  const flagged = flag.map(at => { const pc = pebP.find(p => Math.abs(p.e0 - at) < 6e-4) || { e0: at, e1: at };
    return { at, e0: pc.e0, e1: pc.e1, inside: jumps.map(b => (b.lo + b.hi) / 2).filter(c => c > pc.e0 + 1e-9 && c < pc.e1 - 1e-9) }; });
  // C4: pieces wider than 1e-4, their own K=8 bridge (Lobatto barycentric) on 200 aims through the piece
  let hn = 0, hok = 0, worst = 0;
  for (const p of pieces) { if (p.hi - p.lo <= 1e-4) continue; hn++; if (hn % 20 === 0) console.log('held check', hn, 'flights', flights, Date.now());
    const w = p.xs.map((_, j) => (j % 2 ? -1 : 1) * ((j === 0 || j === K - 1) ? 0.5 : 1)); let err = 0;
    for (let q = 0; q < 200; q++) { const a = p.lo + (p.hi - p.lo) * (q + 0.5) / 200, tr = fly(a).o; let den = 0; const num = [0, 0, 0, 0];
      for (let j = 0; j < K; j++) { const t = w[j] / (a - p.xs[j]); den += t; for (let c = 0; c < 4; c++) num[c] += t * p.ys[j][c]; }
      for (let c = 0; c < 4; c++) err = Math.max(err, Math.abs(num[c] / den - tr[c])); }
    worst = Math.max(worst, err); if (err <= 1e-6) hok++; }
  // the scan's bisection steps, as PEB run 5's loop takes them (from 2π/1024 to 1e-12, at most 60)
  let pebSteps = 0; for (const j of pebJ) { let w = 2 * PI / 1024, n = 0; while (n < 60 && w > 1e-12) { w /= 2; n++; } pebSteps += n; }
  return { flights: flightsMap, steps, leafFlights, dropped, dropWide, capped, jumps: jumps.map(j => ({ lo: j.lo, hi: j.hi })),
    pieces: pieces.map(p => ({ lo: p.lo, hi: p.hi })), pebJumps: pebJ.length, longest, chatter, pebFound, pebMissed, flagged, held: { n: hn, ok: hok, worst }, pebSteps };
}, { name: which, S, pebJ: peb.J, pebP: peb.pieces, flag: FLAG[which] });
r.seconds = (Date.now() - t0) / 1000;
fs.writeFileSync(out(which, S), JSON.stringify(r));
console.log(which, S, 'longest', r.longest, 'chatter', r.chatter, 'flights', r.flights, 'jumps', r.jumps.length, 'pieces', r.pieces.length, 'capped', r.capped, 's', r.seconds);
await br.close(); srv.close();
