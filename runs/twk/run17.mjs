// TWK run 17: things that interact. N balls on a ring, elastic collisions worked exactly event by event (the stepped
// truth), set beside the read: places from T alone by the free law, nothing kept. Run from the repository's root:
// node runs/twk/run17.mjs
const g = (a, b) => { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) [a, b] = [b, a % b]; return a; };
const F = (n, d = 1n) => { n = BigInt(n); d = BigInt(d); if (d < 0n) { n = -n; d = -d; } const k = g(n, d) || 1n; return { n: n / k, d: d / k }; };
const add = (a, b) => F(a.n * b.d + b.n * a.d, a.d * b.d), sub = (a, b) => F(a.n * b.d - b.n * a.d, a.d * b.d);
const mul = (a, b) => F(a.n * b.n, a.d * b.d), div = (a, b) => F(a.n * b.d, a.d * b.n);
const cmp = (a, b) => { const x = a.n * b.d - b.n * a.d; return x < 0n ? -1 : x > 0n ? 1 : 0; };
const eq = (a, b) => a.n === b.n && a.d === b.d;
const floorF = a => { const q = a.n / a.d; return (a.n % a.d !== 0n && a.n < 0n) ? q - 1n : q; };
const N = 16, Lint = 1000, L = F(Lint), TEND = 400, NCMP = 40;
function world(seed, unequal) {
  let s = seed >>> 0; const rnd = () => ((s = (Math.imul(s, 1103515245) + 12345) >>> 0) / 4294967296);
  const xs = new Set(); while (xs.size < N) xs.add(Math.floor(rnd() * Lint * 1000));
  const x = [...xs].sort((a, b) => a - b).map(v => F(v, 1000));
  const vs = new Set(); while (vs.size < N) vs.add(Math.floor(rnd() * 10001) - 5000);
  const v = [...vs].map(u => F(u, 1000));
  let m = Array(N).fill(1); if (unequal) { const idx = [...Array(N).keys()]; for (let i = N - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } idx.slice(0, N / 2).forEach(i => m[i] = 2); }
  return { x0: x.slice(), v0: v.slice(), y: x.slice(), v: v.slice(), m: m.map(k => F(k)) };
}
function run(w) {
  const { x0, v0, m } = w; let { y, v } = w; let t = F(0); const P0 = v.reduce((a, vi, i) => add(a, mul(m[i], vi)), F(0)), E0 = v.reduce((a, vi, i) => add(a, mul(m[i], mul(vi, vi))), F(0));
  let consOK = true, orderOK = true, triple = false, events = 0, firstUnequal = null, keptAtFirst = null; const rows = [];
  const freeAt = T => x0.map((xk, k) => add(xk, mul(v0[k], T)));
  const modL = a => sub(a, mul(L, F(floorF(div(a, L)))));
  const keptCount = T => { const fr = freeAt(T).map((f, k) => [modL(f), v0[k]]);
    return y.reduce((c, yk, k) => c + (fr.some(([p, u]) => eq(p, modL(yk)) && eq(u, v[k])) ? 0 : 1), 0); };
  for (let j = 1; j <= NCMP; j++) {
    const Tc = F(TEND * j / NCMP);
    for (;;) {
      let best = null, who = [];
      for (let i = 0; i < N; i++) { const k = (i + 1) % N, gap = k ? sub(y[k], y[i]) : sub(add(y[0], L), y[i]), dv = sub(v[i], v[k]);
        if (cmp(dv, F(0)) <= 0) continue; const dt = div(gap, dv); const c = best ? cmp(dt, best) : -1;
        if (c < 0) { best = dt; who = [i]; } else if (c === 0) who.push(i); }
      if (!best || cmp(add(t, best), Tc) > 0) { const dt = sub(Tc, t); y = y.map((yk, k) => add(yk, mul(v[k], dt))); t = Tc; break; }
      y = y.map((yk, k) => add(yk, mul(v[k], best))); t = add(t, best);
      for (let a = 0; a < who.length; a++) for (let b = a + 1; b < who.length; b++) { const d = Math.abs(who[a] - who[b]); if (d === 1 || d === N - 1) triple = true; }
      for (const i of who) { const k = (i + 1) % N, m1 = m[i], m2 = m[k], s = add(m1, m2);
        const v1 = div(add(mul(sub(m1, m2), v[i]), mul(F(2), mul(m2, v[k]))), s), v2 = div(add(mul(sub(m2, m1), v[k]), mul(F(2), mul(m1, v[i]))), s);
        v[i] = v1; v[k] = v2; events++;
        if (!eq(m1, m2) && !firstUnequal) { firstUnequal = t; keptAtFirst = keptCount(t); } }
      const P = v.reduce((a, vi, i) => add(a, mul(m[i], vi)), F(0)), E = v.reduce((a, vi, i) => add(a, mul(m[i], mul(vi, vi))), F(0));
      if (!eq(P, P0) || !eq(E, E0)) consOK = false;
      for (let i = 0; i + 1 < N; i++) if (cmp(y[i], y[i + 1]) > 0) orderOK = false; if (cmp(y[N - 1], add(y[0], L)) > 0) orderOK = false;
    }
    // the read: free places from T alone
    const fr = freeAt(Tc), fm = fr.map(modL), sorted = fm.slice().sort(cmp), tm = y.map(modL), tsorted = tm.slice().sort(cmp);
    const setEq = sorted.every((f, i) => eq(f, tsorted[i]));
    const W = fr.reduce((a, f) => a + floorF(div(f, L)), 0n), Wm = Number(((W % BigInt(N)) + BigInt(N)) % BigInt(N));
    const rankOK = tm.every((p, k) => eq(p, sorted[(Wm + k) % N]));
    rows.push({ T: Number(Tc.n / Tc.d), setEq, rankOK, kept: keptCount(Tc), events, digits: Math.max(...y.map(a => a.d.toString().length)) });
  }
  return { rows, consOK, orderOK, triple, events, firstUnequal: firstUnequal && Number(firstUnequal.n) / Number(firstUnequal.d), keptAtFirst };
}
const out = {};
for (const seed of [1, 2, 3]) {
  const b = run(world(seed, false)), c = run(world(seed, true));
  const after = c.rows.filter(r => c.firstUnequal !== null && r.T > c.firstUnequal);
  out['seed' + seed] = {
    equal: { R1: b.rows.every(r => r.setEq), R1b: b.rows.every(r => r.rankOK), R1c: b.orderOK, R4: b.consOK, triple: b.triple, events: b.events, maxKept: Math.max(...b.rows.map(r => r.kept)) },
    unequal: { R2: after.every(r => !r.setEq), R2rows: after.length, firstUnequal: c.firstUnequal, keptAtFirst: c.keptAtFirst, R3keptEnd: c.rows.at(-1).kept,
      keptPath: c.rows.filter((r, i) => i % 4 === 3).map(r => r.kept), R1c: c.orderOK, R4: c.consOK, triple: c.triple, events: c.events, digits: c.rows.at(-1).digits }
  };
}
console.log(JSON.stringify(out, null, 1));
