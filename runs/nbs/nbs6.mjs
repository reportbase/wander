// NBS run 6 (plans/nbs-plan.md): jumps counted about a place (the 65 nearest the new one), not over a span. From nbs5.mjs.
// NBS run 5 (plans/nbs-plan.md): run 4's busy rule, only the smallest busy span given up. From nbs4.mjs.
// NBS run 4 (plans/nbs-plan.md): run 2's B′ with the busy rule (a span with more than 64 jumps and no piece wider than its
// K-th part is unmapped). From nbs3.mjs, run 3's width floor removed;
// NBS run 2 (plans/nbs-plan.md): B′, no scan, on PEB's event engine with its full signature (runs/peb/play-trick-event5.html).
// node runs/nbs/nbs2.mjs map cut 16 | map tworail 64 | ... ; node runs/nbs/nbs2.mjs report
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const part = process.argv[2], which = process.argv[3], S = +(process.argv[4] || 16);
const out = (w, s) => `runs/nbs/nbs6-${w}-${s}.json`;
const FLAG = { cut: [0.124, 0.145, 2.387, 3.958], tworail: [0.389] };   // PEB run 5's post hoc, the pieces with a hidden jump

if (part === 'report') {
  const L = []; const say = t => { console.log(t); L.push(t); };
  const ctr = j => (j.lo + j.hi) / 2, dist = (a, b) => { const d = Math.abs(a - b) % (2 * Math.PI); return Math.min(d, 2 * Math.PI - d); };
  const inWin = (x, W) => W.some(([a, b]) => x >= a - 1e-9 && x <= b + 1e-9);
  const meas = W => W.reduce((t, w) => t + w[1] - w[0], 0);
  const R = {};
  for (const w of ['cut', 'tworail']) for (const S of [16, 64]) R[w + S] = JSON.parse(fs.readFileSync(out(w, S), 'utf8'));
  const r2 = JSON.parse(fs.readFileSync('runs/nbs/nbs2-cut-16.json', 'utf8'));
  for (const k of Object.keys(R)) { const x = R[k]; say(`${k}: flights ${x.flights}, capped ${x.capped}, ${x.jumps.length} jumps, ${x.pieces.length} pieces, unmapped ${x.unmapped.length} windows, ${meas(x.unmapped).toExponential(3)} rad: ${x.unmapped.slice(0, 8).map(w => w[0].toFixed(7) + '..' + w[1].toFixed(7)).join(' ')}${x.unmapped.length > 8 ? ' …' : ''}; longest shot ${x.longest} events, chatter flights ${x.chatter}`); }
  const e1 = Object.values(R).every(x => !x.capped);
  const T = R.tworail16, mT = meas(T.unmapped), inW = T.unmapped.reduce((t, [a, b]) => t + Math.max(0, Math.min(b, 0.5356) - Math.max(a, 0.5352)), 0);
  const e2 = mT < 1e-3 && (mT === 0 || inW / mT >= 0.9);
  const peb = JSON.parse(fs.readFileSync('runs/peb/peb5-map-tworail.json', 'utf8')).J;
  const outside = peb.filter(j => !inWin(ctr(j), T.unmapped)), found = outside.filter(j => T.jumps.some(b => dist(ctr(b), ctr(j)) < 1e-9));
  const missed = outside.filter(j => !found.includes(j)).map(ctr);
  const e3 = found.length === outside.length;
  const C = R.cut16, e4 = C.jumps.length === 137 && meas(C.unmapped) === 0 && Math.abs(C.flights / r2.flights - 1) <= 0.05;
  const e5 = T.held.n ? T.held.ok / T.held.n >= 0.95 : false;
  const T6 = R.tworail64, j16 = T.jumps.filter(j => !inWin(ctr(j), T.unmapped) && !inWin(ctr(j), T6.unmapped)), j64 = T6.jumps.filter(j => !inWin(ctr(j), T.unmapped) && !inWin(ctr(j), T6.unmapped));
  const a16 = j16.filter(j => j64.some(k => dist(ctr(j), ctr(k)) < 1e-9)).length, a64 = j64.filter(j => j16.some(k => dist(ctr(j), ctr(k)) < 1e-9)).length;
  const e6 = a16 === j16.length && a64 === j64.length && Math.abs(T6.flights / T.flights - 1) < 0.2;
  const e7 = T.flights <= 4 * 4621;
  say(`G1 ${e1 ? 'not killed' : 'KILLED'}`);
  say(`G2 ${e2 ? 'not killed' : 'KILLED'} (two rails unmapped ${mT.toExponential(3)} rad, ${mT ? (100 * inW / mT).toFixed(1) : '-'}% inside 0.5352–0.5356)`);
  say(`G3 ${e3 ? 'not killed' : 'KILLED'} (PEB jumps outside unmapped ${outside.length}, found ${found.length}; missed at ${missed.map(x => x.toFixed(6)).join(' ') || '-'})`);
  say(`G4 ${e4 ? 'not killed' : 'KILLED'} (cut ${C.jumps.length} jumps, unmapped ${meas(C.unmapped).toExponential(2)}, flights ${C.flights} against ${r2.flights})`);
  say(`G5 ${e5 ? 'not killed' : 'KILLED'} (${T.held.ok}/${T.held.n}, worst ${T.held.worst.toExponential(2)}; cut ${C.held.ok}/${C.held.n})`);
  say(`G6 ${e6 ? 'not killed' : 'KILLED'} (outside both windows: 16 in 64 ${a16}/${j16.length}, 64 in 16 ${a64}/${j64.length}; flights ${(T6.flights / T.flights).toFixed(3)})`);
  say(`G7 ${e7 ? 'not killed' : 'KILLED'} (two rails ${T.flights} against 4 × 4,621 = 18,484)`);
  fs.writeFileSync('runs/nbs/nbs-run6.txt', L.join('\n') + '\n');
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
  const jumps = [], pieces = []; let dropped = 0, dropWide = 0, capped = false, iter = 0; const J = 64, unmapped = [];
  // every jump found kept in order of its aim; every piece found kept with its ends
  const at = [], pcs = [], win0 = [];
  const ins = x => { let a = 0, b = at.length; while (a < b) { const m = (a + b) >> 1; if (at[m] < x) a = m + 1; else b = m; } at.splice(a, 0, x); return a; };
  // a new jump at x in a span of width w: the J + 1 found nearest it, their window I; given up if narrower than w/K
  // and no piece overlapping I is wider than |I|/K
  const onJump = (x, w) => { const p = ins(x); if (at.length < J + 1) return; let l = p, r = p;
    while (r - l < J) { if (l === 0) r++; else if (r === at.length - 1) l--; else if (x - at[l - 1] <= at[r + 1] - x) l--; else r++; }
    const a = at[l], b = at[r]; if (b - a >= w / K) return;
    for (const [u, v] of pcs) if (u < b && v > a && v - u > (b - a) / K) return;
    win0.push([a, b]); unmapped.push([a, b]); };
  const stack = []; for (let i = S - 1; i >= 0; i--) stack.push([2 * PI * i / S, 2 * PI * (i + 1) / S]);
  while (stack.length) {
    if (flights > CAP) { capped = true; break; }
    if (++iter % 20000 === 0) console.log('it', iter, 'flights', flights, 'stack', stack.length, 'jumps', jumps.length, 'pieces', pieces.length, 'cache', cache.size, 'span', stack.length ? (stack[stack.length-1][1]-stack[stack.length-1][0]).toExponential(2) + ' at ' + stack[stack.length-1][0].toFixed(6) : '');
    const [lo, hi] = stack.pop();
    const cutBy = win0.find(([a, b]) => a < hi && b > lo);   // a span over a given-up window: only its parts outside it
    if (cutBy) { if (cutBy[1] < hi) stack.push([cutBy[1], hi]); if (lo < cutBy[0]) stack.push([lo, cutBy[0]]); continue; } const xs = nodes(lo, hi), before = flights, F = xs.map(fly); leafFlights += flights - before;
    let k = 0; while (k < K - 1 && F[k].s === F[k + 1].s) k++;
    if (k < K - 1 && hi - lo <= 1e-12) { jumps.push({ lo, hi, sL: F[0].s, sR: F[K - 1].s }); onJump((lo + hi) / 2, hi - lo); continue; }   // already a bracket: a jump, not cut again
    if (k < K - 1) {   // a change between leaves k and k+1: bisected, the span cut there
      let l = xs[k], h = xs[k + 1]; const sL = F[k].s;
      while (h - l > 1e-12) { const m = (l + h) / 2; if (m <= l || m >= h) break; steps++; if (fly(m).s === sL) l = m; else h = m; }
      jumps.push({ lo: l, hi: h, sL, sR: fly(h).s }); onJump((l + h) / 2, hi - lo);
      stack.push([h, hi]); stack.push([lo, l]); continue;
    }
    let ok = true; for (let c = 0; c < 4 && ok; c++) ok = lastCoeffs(F.map(f => f.o[c])) < TOL;
    if (ok) { pieces.push({ lo, hi, s: F[0].s, xs, ys: F.map(f => f.o) }); pcs.push([lo, hi]); continue; }
    if (hi - lo < 1e-12) { dropped++; dropWide = Math.max(dropWide, hi - lo); continue; }
    const m = (lo + hi) / 2; stack.push([m, hi]); stack.push([lo, m]);
  }
  unmapped.sort((a, b) => a[0] - b[0]); const win = [];
  for (const [a, b] of unmapped) { const w = win[win.length - 1]; if (w && a - w[1] < 1e-9) w[1] = Math.max(w[1], b); else win.push([a, b]); }
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
  return { unmapped: win, flights: flightsMap, steps, leafFlights, dropped, dropWide, capped, jumps: jumps.map(j => ({ lo: j.lo, hi: j.hi })),
    pieces: pieces.map(p => ({ lo: p.lo, hi: p.hi })), pebJumps: pebJ.length, longest, chatter, pebFound, pebMissed, flagged, held: { n: hn, ok: hok, worst }, pebSteps };
}, { name: which, S, pebJ: peb.J, pebP: peb.pieces, flag: FLAG[which] });
r.seconds = (Date.now() - t0) / 1000;
fs.writeFileSync(out(which, S), JSON.stringify(r));
console.log(which, S, 'unmapped windows', r.unmapped.length, 'measure', r.unmapped.reduce((t, w) => t + w[1] - w[0], 0), 'longest', r.longest, 'chatter', r.chatter, 'flights', r.flights, 'jumps', r.jumps.length, 'pieces', r.pieces.length, 'capped', r.capped, 's', r.seconds);
await br.close(); srv.close();
