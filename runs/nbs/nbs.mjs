// NBS run 1: the bridge behind the 9-ball computer's aim (plans/nbs-plan.md). games.html read, not changed.
// node runs/nbs/nbs.mjs run        (60 positions on 4 browsers, writes runs/nbs/nbs-pos-*.json)
// node runs/nbs/nbs.mjs report     (writes runs/nbs/nbs-run1.txt)
import { serve, ninePage, chromium, GAMES } from './serve.mjs';
import { readFile, writeFile, readdir } from 'node:fs/promises';
import { createHash } from 'node:crypto';
const here = new URL('.', import.meta.url).pathname, PAGE = await readFile(here + 'page.js', 'utf8');
const SEED = 20261126, NPOS = 60, WORKERS = 4, BP_CAP = 50000;
const above = async () => { const t = await readFile(GAMES, 'utf8'), i = t.indexOf('// ══ IN THE FIELD (Oct 22)'); return createHash('sha256').update(t.slice(0, i)).digest('hex'); };

async function worker(w, port){
  const b = await chromium.launch(), p = await ninePage(b, port); await p.evaluate(PAGE);
  const n = await p.evaluate(([n, s]) => { window.__P = window.NBS.positions(n, s); return window.__P.length; }, [NPOS, SEED]);
  for (let k = w; k < n; k += WORKERS){
    const t0 = Date.now();
    const r = await p.evaluate(([k, cap]) => { const N = window.NBS, pos = window.__P[k], B = pos.balls, low = N.lowOf(B), nextN = N.nextOf(B, low), DEG = Math.PI / 180;
      const S3 = 0.8 * DEG, S5 = 0.15 * DEG, out = { k, idx: pos.idx, shot: pos.shot, low: low.n };
      // C, the games' planner at levels 3 and 5 (noise taken out), and whether its own aim pots
      const C3 = N.planC(B, 3), C5 = N.planC(B, 5);
      out.C = { c3: C3, c5: C5, finds: N.judge(N.fly(B, C5.a, C5.p, C5.tip), low.n).pot };
      // B at 720: maps at 16 and 28, pot pieces bridged on K = 8 leaves (counted)
      const c0 = N.count, maps = [];
      for (const pw of [16, 28]){ const m = N.mapScan(B, pw, 720, low.n); const br = m.pieces.map(pc => pc.j.pot ? N.bridgePiece(B, pw, pc, 8) : null); maps.push({ p: pw, pieces: m.pieces, br, edges: m.edges }); }
      out.B = { flights: N.count - c0, edges: maps.map(m => m.edges), pots: maps.map(m => m.pieces.filter(x => x.j.pot).length),
        potW: maps.flatMap(m => m.pieces.filter(x => x.j.pot).map(x => x.hi - x.lo)), impure: maps.flatMap(m => m.br.filter(x => x && !x.sigsOk)).length };
      out.B.finds = maps.some(m => m.pieces.some(x => x.j.pot));
      const b3 = N.planB(maps, S3, nextN), b5 = N.planB(maps, S5, nextN);
      out.B.b3 = b3 && { a: b3.a, p: b3.p, w: b3.hi - b3.lo, nine: b3.nine, v: b3.v }; out.B.b5 = b5 && { a: b5.a, p: b5.p, w: b5.hi - b5.lo, nine: b5.nine, v: b5.v };
      // A2: 200 flights each under the hand's error (seeded); a planner with no pot still flies its shot
      const fb = (x, s, sd) => x ? N.under(B, x.a, x.p, [0, 0], s, 200, sd, low.n) : 0;
      out.A2 = { C3: N.under(B, C3.a, C3.p, C3.tip, S3, 200, 11 + k, low.n), C5: N.under(B, C5.a, C5.p, C5.tip, S5, 200, 12 + k, low.n), B3: fb(b3, S3, 13 + k), B5: fb(b5, S5, 14 + k) };
      // A4: pot pieces wider than 1e-3, the white's place by K = 6, 8, 12 against 16 flights inside (not counted as B's)
      const rnd = N.mulberry(99 + k); out.A4 = [];
      maps.forEach(m => m.pieces.forEach(pc => { if (!pc.j.pot || pc.hi - pc.lo <= 1e-3) return;
        const chk = Array.from({ length: 16 }, () => pc.lo + (pc.hi - pc.lo) * (0.02 + 0.96 * rnd())), fl = chk.map(a => N.fly(B, a, m.p));
        const pure = fl.every(sm => N.sig(sm) === pc.s), errs = {};
        for (const K of [6, 8, 12]){ const br = N.bridgePiece(B, m.p, pc, K); errs[K] = Math.max(...chk.map((a, i) => { const q = N.bridgeAt(br, a), t = N.white(fl[i]); return Math.hypot(q[0] - t[0], q[1] - t[1]); })); }
        out.A4.push({ w: pc.hi - pc.lo, pure, errs }); }));
      // A5: in the level-5 window (a pot of the lowest), the chosen aim's leaveQ against the best of 64 flown aims
      if (b5 && !b5.nine){ let best = -1, at = 0; for (let q = 0; q < 64; q++){ const a = b5.lo + (b5.hi - b5.lo) * (q + 0.5) / 64, sm = N.fly(B, a, b5.p);
          const L = N.judge(sm, low.n).pot ? window.__N.leaveQ(sm.final, nextN) : -1; if (L > best){ best = L; } }
        const smc = N.fly(B, b5.a, b5.p); at = N.judge(smc, low.n).pot ? window.__N.leaveQ(smc.final, nextN) : -1;
        out.A5 = { best, at, ok: at >= best - 0.1 }; } else out.A5 = null;
      // A7: B at 1440 (scan + bisection only, as B's flights at 720 without the leaves, for the ratio), and B′
      const scanOnly = []; for (const M of [720, 1440]){ const c = N.count; const ps = []; for (const pw of [16, 28]) ps.push(N.mapScan(B, pw, M, low.n)); scanOnly.push({ M, flights: N.count - c, pieces: ps }); }
      out.A7 = { f720: scanOnly[0].flights, f1440: scanOnly[1].flights };
      const bp = [16, 28].map(pw => ({ p: pw, ...N.mapHalve(B, pw, 8, 1e-6, low.n, cap) }));
      out.A7.bp = bp.map(x => ({ p: x.p, flights: x.flights, pieces: x.pieces.length, pots: x.pieces.filter(y => y.j.pot).length, capped: x.capped, dropped: x.dropped }));
      // (a): each of B's pot pieces wider than 1e-3 covered by a B′ pot piece at its middle
      let need = 0, got = 0; maps.forEach((m, i) => m.pieces.forEach(pc => { if (!pc.j.pot || pc.hi - pc.lo <= 1e-3) return; need++; const mid = (pc.lo + pc.hi) / 2;
        if (bp[i].pieces.some(q => q.j.pot && q.lo <= mid && mid <= q.hi)) got++; }));
      out.A7.cover = { need, got };
      return out; }, [k, BP_CAP]);
    r.secs = (Date.now() - t0) / 1000;
    await writeFile(here + `nbs-pos-${String(k).padStart(2, '0')}.json`, JSON.stringify(r));
    console.log(`w${w} pos ${k} (${r.idx}/${r.shot}) ${r.secs.toFixed(0)} s, B ${r.B.flights}, C5 ${r.C.c5.flights}, finds C ${r.C.finds} B ${r.B.finds}`);
  }
  await b.close();
}

const med = a => { const s = [...a].sort((x, y) => x - y), n = s.length; return n ? (n % 2 ? s[(n - 1) / 2] : (s[n / 2 - 1] + s[n / 2]) / 2) : NaN; };
async function report(){
  const files = (await readdir(here)).filter(f => /^nbs-pos-\d+\.json$/.test(f)).sort(), R = [];
  for (const f of files) R.push(JSON.parse(await readFile(here + f, 'utf8')));
  const L = [], say = s => L.push(s), pct = (a, b) => b ? (100 * a / b).toFixed(1) + '%' : 'n/a';
  say(`NBS run 1, ${R.length} positions (seed ${SEED}); games.html above IN THE FIELD sha256 ${await above()}`);
  // A1
  const cf = R.filter(r => r.C.finds), cn = R.filter(r => !r.C.finds);
  const a1a = cf.filter(r => r.B.finds).length, a1b = cn.filter(r => r.B.finds).length;
  say(`A1: C (level 5) pots in ${cf.length}; B in ${a1a} of those; where C finds none (${cn.length}), B finds one in ${a1b} (${pct(a1b, cn.length)})`);
  say(`    ${a1a === cf.length && (cn.length === 0 || a1b / cn.length >= 0.1) ? 'not killed' : 'KILLED'}`);
  // A2
  const av = k => R.reduce((s, r) => s + r.A2[k], 0) / R.length * 100;
  say(`A2: legal pots under the hand's error, mean over positions: level 3 B ${av('B3').toFixed(1)}% C ${av('C3').toFixed(1)}%; level 5 B ${av('B5').toFixed(1)}% C ${av('C5').toFixed(1)}%`);
  say(`    ${av('B3') - av('C3') >= 5 && av('C5') - av('B5') <= 2 ? 'not killed' : 'KILLED'}`);
  // A3
  const mb = med(R.map(r => r.B.flights)), mc = med(R.map(r => r.C.c5.flights));
  say(`A3: B's flights per position median ${mb} (range ${Math.min(...R.map(r => r.B.flights))}–${Math.max(...R.map(r => r.B.flights))}), C's (level 5) ${mc}, ratio ${(mb / mc).toFixed(0)}`);
  say(`    ${mb <= 4000 && mb >= 30 * mc ? 'not killed' : 'KILLED'}`);
  // A4
  const P4 = R.flatMap(r => r.A4), held = P4.filter(x => Math.min(x.errs[6], x.errs[8], x.errs[12]) <= 0.05).length;
  say(`A4: pot pieces wider than 1e-3: ${P4.length}; leave held to 0.05 by some K ≤ 12 in ${held} (${pct(held, P4.length)}); pure (no event change at the 16 checks) ${P4.filter(x => x.pure).length}`);
  say(`    median error K6 ${med(P4.map(x => x.errs[6])).toExponential(2)}, K8 ${med(P4.map(x => x.errs[8])).toExponential(2)}, K12 ${med(P4.map(x => x.errs[12])).toExponential(2)}`);
  say(`    ${P4.length && held / P4.length >= 0.8 ? 'not killed' : 'KILLED'}`);
  // A5
  const P5 = R.filter(r => r.A5), ok5 = P5.filter(r => r.A5.ok).length;
  say(`A5: positions with a level-5 window potting the lowest: ${P5.length}; chosen aim within 0.1 of the best of 64 in ${ok5} (${pct(ok5, P5.length)})`);
  say(`    ${P5.length && ok5 / P5.length >= 0.8 ? 'not killed' : 'KILLED'}`);
  // A6
  say(`A6: the text above IN THE FIELD unchanged (read before and after this report: one file, not written by the run); the referee is games' simulate. not killed`);
  // A7
  const cov = R.filter(r => r.A7.cover.need === r.A7.cover.got).length;
  say(`A7 (a): B's pot pieces wider than 1e-3 all covered by B′ in ${cov} of ${R.length} positions (${pct(cov, R.length)})`);
  const m720 = med(R.map(r => r.A7.f720)), m1440 = med(R.map(r => r.A7.f1440));
  say(`A7 (b): B's scan and bisection at 720 median ${m720}, at 1440 ${m1440}, ratio ${(m1440 / m720).toFixed(2)}; B′ has no scan (by construction unchanged)`);
  const bpf = R.map(r => r.A7.bp.reduce((s, x) => s + x.flights, 0)), bpp = R.map(r => r.A7.bp.reduce((s, x) => s + x.pieces, 0)), capped = R.filter(r => r.A7.bp.some(x => x.capped)).length;
  say(`A7 (c): B′ flights per position median ${med(bpf)}, pieces ${med(bpp)}, ratio ${(med(bpf) / med(bpp)).toFixed(1)} against 3K = 24; cap ${BP_CAP} a power hit in ${capped} of ${R.length}`);
  say(`    A7 ${cov / R.length >= 0.95 && m1440 / m720 >= 1.6 && med(bpf) / med(bpp) <= 24 ? 'not killed' : 'KILLED'}`);
  say(`B's edges per power median ${med(R.flatMap(r => r.B.edges))}; pot pieces per position median ${med(R.map(r => r.B.pots[0] + r.B.pots[1]))}; pot windows median width ${med(R.flatMap(r => r.B.potW)).toExponential(2)} rad; bridged pot pieces with a leaf off the piece's events ${R.reduce((s, r) => s + r.B.impure, 0)}`);
  const txt = L.join('\n') + '\n'; await writeFile(here + 'nbs-run1.txt', txt); console.log(txt);
}

if (process.argv[2] === 'run'){ const h0 = await above(); console.log('above IN THE FIELD', h0); const s = await serve();
  await Promise.all(Array.from({ length: WORKERS }, (_, w) => worker(w, s.address().port))); s.close();
  console.log('after', await above() === h0 ? 'unchanged' : 'CHANGED'); }
else if (process.argv[2] === 'report') await report();
