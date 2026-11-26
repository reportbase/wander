// NBS's page side: defines window.NBS on the 9-ball page (games.html's own hooks, nothing changed there).
// Every flight is the games' `simulate` at the games' `strikeOf` with no tip and no rise (planner B) or the planner's own
// tip (planner C), counted in NBS.count.
(() => {
  const D = window.__N, PI = Math.PI, DEG = PI / 180;
  const mulberry = s => () => { s = (s + 0x6D2B79F5) >>> 0; let t = s; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const N = window.NBS = { count: 0 };
  const lowOf = B => B.filter(b => !b.cue && !b.sunk).sort((a, b) => a.n - b.n)[0] || null;
  const nextOf = (B, low) => (B.filter(b => !b.cue && !b.sunk && b !== low).sort((a, b) => a.n - b.n)[0] || {}).n;
  const copy = B => B.map(b => ({ ...b, vx: 0, vz: 0 }));
  N.fly = (B, a, p, tip = [0, 0]) => { N.count++; const st = D.strikeOf(a, tip[0], tip[1], p, undefined, 0); return D.simulate(B, st.dir, st.speed, st.w, st.vy); };
  // the shot's events in time order: contacts, cushions, pockets (the fixed-tick engine records no grips' choices or phase ends)
  N.sig = sm => { if (!sm) return 'none'; const ev = [];
    sm.contacts.forEach(c => ev.push([c.t, 'c' + Math.min(c.a, c.b) + '-' + Math.max(c.a, c.b)]));
    sm.cushions.forEach(c => ev.push([c.t, 'r' + c.n])); sm.sunk.forEach(s => ev.push([s.t, 'p' + s.n + ':' + s.pocket]));
    ev.sort((x, y) => x[0] - y[0]); return ev.map(e => e[1]).join(' '); };
  N.judge = (sm, lowN) => { if (!sm) return { legal: false, pot: false, nine: false };
    const legal = !!sm.first && sm.first.n === lowN && !sm.sunk.some(s => s.n === 0), pots = sm.sunk.filter(s => s.n !== 0 && s.pocket >= 0).map(s => s.n);
    return { legal, pot: legal && (pots.includes(lowN) || pots.includes(9)), nine: legal && pots.includes(9) }; };
  N.white = sm => { const w = sm && sm.final.find(b => b.cue); return w && !w.sunk ? [w.x, w.z] : [0, 0]; };

  // ── positions from seeded self-play, both sides ninePlan at level 3
  N.positions = (want, seed) => { const rnd = mulberry(seed), keep = [], save = Math.random; Math.random = rnd;
    try {
      for (let idx = 0; keep.length < want && idx < 400; idx++){
        const g = { idx, lv: 3, auto: true, balls: D.rack9(idx), potted: 0, shots: 0, ang: 0, power: 40, nine: Object.assign(D.MATCH.nine.fresh(), { kind: 'nine' }) };
        let plan = { a: 0.6 * DEG, p: 52, tip: [0, 0] }, brk = true;
        while (!g.nine.over && g.shots < 120 && keep.length < want){
          const hand = g.nine.hand;
          if (!brk && !hand) keep.push({ idx, shot: g.shots, balls: copy(g.balls) });
          const st = D.strikeOf(plan.a, plan.tip[0], plan.tip[1], plan.p, undefined, 0), sm = D.simulate(g.balls, st.dir, st.speed, st.w, st.vy); if (!sm) break;
          g.nine.hand = false; g.shots++; D.nineFinish(g, sm); brk = false;
          if (!g.nine.over) plan = D.ninePlan(g, 3);
        }
      }
    } finally { Math.random = save; }
    return keep; };
  // ninePlan puts the white in hand before it plans; ours never are (left out), so g.nine.hand is false
  const gOf = (balls, lv) => ({ idx: 0, lv, balls: copy(balls), ang: 0, nine: { hand: false } });

  // ── planner C: the games' own ninePlanGen, its hand's noise taken out (Math.random 0.25 puts its Gaussian at cos(π/2) = 0)
  N.planC = (balls, lv) => { const save = Math.random; Math.random = () => 0.25; let n = 0, r;
    try { const it = D.ninePlanGen(gOf(balls, lv), lv); do { r = it.next(); n++; } while (!r.done); } finally { Math.random = save; }
    return { a: r.value.a, p: r.value.p, tip: r.value.tip, score: r.value.score, flights: n - 1 }; };

  // ── Chebyshev leaves (first kind) on [lo, hi], barycentric interpolation, coefficients
  const cheb = K => Array.from({ length: K }, (_, j) => Math.cos(PI * (2 * j + 1) / (2 * K)));
  const leavesOn = (lo, hi, K) => cheb(K).map(x => (lo + hi) / 2 + (hi - lo) / 2 * x);
  const bary = (xs, ys, x) => { const K = xs.length; let num = 0, den = 0;
    for (let j = 0; j < K; j++){ const d = x - xs[j]; if (d === 0) return ys[j]; const wj = (j % 2 ? -1 : 1) * Math.sin(PI * (2 * j + 1) / (2 * K)) / d; num += wj * ys[j]; den += wj; }
    return num / den; };
  const coeffs = ys => { const K = ys.length, c = [];
    for (let k = 0; k < K; k++){ let s = 0; for (let j = 0; j < K; j++) s += ys[j] * Math.cos(PI * k * (2 * j + 1) / (2 * K)); c.push(s * (k ? 2 : 1) / K); } return c; };

  // ── the circle mapped at one power, scan of M aims, every change of events bisected to 1e-10 rad
  N.mapScan = (B, p, M, lowN) => {
    const c0 = N.count, A = i => 2 * PI * i / M, S = [];
    for (let i = 0; i < M; i++){ const sm = N.fly(B, A(i), p); S.push({ a: A(i), s: N.sig(sm), sm }); }
    const edges = [];
    const bisect = (L, sL, R, sR, depth) => {   // one change found, then the rest of the interval if its far side differs
      let l = L, r = R, sr = sR, smr = null;
      while (r - l > 1e-10){ const m = (l + r) / 2, sm = N.fly(B, m, p), s = N.sig(sm); if (s === sL) l = m; else { r = m; sr = s; smr = sm; } }
      edges.push({ e: (l + r) / 2, left: sL, right: sr });
      if (sr !== sR && depth < 12) bisect(r, sr, R, sR, depth + 1);
    };
    for (let i = 0; i < M; i++){ const a = S[i], b = S[(i + 1) % M], R = i + 1 < M ? b.a : 2 * PI; if (a.s !== b.s) bisect(a.a, a.s, R, b.s, 0); }
    // pieces between edges (with no edge at all, one piece the whole circle)
    edges.sort((x, y) => x.e - y.e);
    const pieces = [];
    if (!edges.length) pieces.push({ lo: 0, hi: 2 * PI, s: S[0].s, sm: S[0].sm });
    for (let k = 0; k < edges.length; k++){ const lo = edges[k].e, hi = k + 1 < edges.length ? edges[k + 1].e : edges[0].e + 2 * PI;
      const s = edges[k].right; const smp = S.find(x => x.s === s && x.a > lo && x.a < hi) || S.find(x => x.s === s && x.a + 2 * PI > lo && x.a + 2 * PI < hi);
      pieces.push({ lo, hi, s, sm: smp ? smp.sm : null }); }
    for (const pc of pieces){ if (!pc.sm){ pc.sm = N.fly(B, (pc.lo + pc.hi) / 2, p); } pc.j = N.judge(pc.sm, lowN); }
    return { pieces, flights: N.count - c0, edges: edges.length };
  };

  // ── the leave held on K leaves in a pot piece: white's place bridged, the layout of its nearest leaf
  N.bridgePiece = (B, p, pc, K) => { const xs = leavesOn(pc.lo, pc.hi, K), fl = xs.map(a => N.fly(B, a, p));
    return { xs, fl, sigsOk: fl.every(sm => N.sig(sm) === pc.s), wx: fl.map(sm => N.white(sm)[0]), wz: fl.map(sm => N.white(sm)[1]) }; };
  N.bridgeAt = (br, a) => [bary(br.xs, br.wx, a), bary(br.xs, br.wz, a)];
  const Phi = x => 0.5 * (1 + erf(x / Math.SQRT2));
  function erf(x){ const s = Math.sign(x); x = Math.abs(x); const t = 1 / (1 + 0.3275911 * x);
    return s * (1 - (((((1.061405429 * t - 1.453152027) * t) + 1.421413741) * t - 0.284496736) * t + 0.254829592) * t * Math.exp(-x * x)); }
  N.share = (lo, hi, t, sig) => Phi((hi - t) / sig) - Phi((lo - t) / sig);
  // the leave score at a with the white at its bridged place, the other balls as at the nearest leaf
  N.leaveAt = (br, a, nextN) => { let k = 0, d = 1e9; br.xs.forEach((x, j) => { if (Math.abs(x - a) < d){ d = Math.abs(x - a); k = j; } });
    const L = br.fl[k].final.map(b => ({ ...b })), w = L.find(b => b.cue), [x, z] = N.bridgeAt(br, a); if (w){ w.x = x; w.z = z; } return nextN == null ? 0 : D.leaveQ(L, nextN); };

  // ── planner B at one hand's error: the mapped pieces at powers 16 and 28, the best share × bridged score
  N.planB = (maps, sigma, nextN, K) => { let best = null;
    for (const { p, pieces, br } of maps) pieces.forEach((pc, i) => { if (!pc.j.pot) return; const b = br[i];
      for (let q = 0; q < 64; q++){ const t = pc.lo + (pc.hi - pc.lo) * (q + 0.5) / 64;
        const sc = pc.j.nine ? 10 : 2 + 3 * N.leaveAt(b, t, nextN), v = N.share(pc.lo, pc.hi, t, sigma) * sc;
        if (!best || v > best.v) best = { v, a: t, p, piece: i, lo: pc.lo, hi: pc.hi, nine: pc.j.nine, b }; } });
    return best; };

  // ── shots flown under the hand's error: the share of legal pots
  N.under = (B, a, p, tip, sigma, n, seed, lowN) => { const rnd = mulberry(seed); let k = 0;
    for (let i = 0; i < n; i++){ const u1 = rnd() || 1e-12, u2 = rnd(), g = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * PI * u2);
      if (N.judge(N.fly(B, a + g * sigma, p, tip), lowN).pot) k++; } return k / n; };

  // ── planner B′: no scan; spans halved until K leaves agree in events and the leave's last two coefficients are under tol
  N.mapHalve = (B, p, K, tol, lowN, budget) => { const c0 = N.count, pieces = [], stack = [];
    for (let i = 0; i < 16; i++) stack.push([2 * PI * i / 16, 2 * PI * (i + 1) / 16]);
    let capped = false, dropped = 0;
    while (stack.length){ const [lo, hi] = stack.pop();
      if (N.count - c0 > budget){ capped = true; break; }
      const xs = leavesOn(lo, hi, K), fl = xs.map(a => N.fly(B, a, p)), sg = fl.map(N.sig), same = sg.every(s => s === sg[0]);
      let ok = same; if (ok){ const cx = coeffs(fl.map(sm => N.white(sm)[0])), cz = coeffs(fl.map(sm => N.white(sm)[1]));
        ok = Math.max(Math.abs(cx[K - 1]), Math.abs(cx[K - 2]), Math.abs(cz[K - 1]), Math.abs(cz[K - 2])) < tol; }
      if (ok){ pieces.push({ lo, hi, s: sg[0], j: N.judge(fl[0], lowN) }); continue; }
      if (hi - lo < 1e-10){ dropped++; continue; }
      const m = (lo + hi) / 2; stack.push([m, hi]); stack.push([lo, m]);
    }
    return { pieces, flights: N.count - c0, capped, dropped };
  };
  N.lowOf = lowOf; N.nextOf = nextOf; N.leavesOn = leavesOn; N.bary = bary; N.mulberry = mulberry;
})();
