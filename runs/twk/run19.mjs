// TWK run 19: things that touch, in two dimensions. 16 hard squares (side 8, not turning) on a torus 100 on a side,
// smooth elastic contact (the component normal to the touching faces exchanged as in one dimension, the other kept),
// worked event by event in exact fractions, against the free law (each square's start plus its velocity times T).
// Squares, not discs: a disc's contact time needs a square root, a square's is rational. Run from the repository's root:
// node runs/twk/run19.mjs
const g = (a, b) => { a = a < 0n ? -a : a; b = b < 0n ? -b : b; while (b) [a, b] = [b, a % b]; return a; };
const F = (n, d = 1n) => { n = BigInt(n); d = BigInt(d); if (d < 0n) { n = -n; d = -d; } const k = g(n, d) || 1n; return { n: n / k, d: d / k }; };
const add = (a, b) => F(a.n * b.d + b.n * a.d, a.d * b.d), sub = (a, b) => F(a.n * b.d - b.n * a.d, a.d * b.d);
const mul = (a, b) => F(a.n * b.n, a.d * b.d), div = (a, b) => F(a.n * b.d, a.d * b.n);
const cmp = (a, b) => { const x = a.n * b.d - b.n * a.d; return x < 0n ? -1 : x > 0n ? 1 : 0; };
const eq = (a, b) => a.n === b.n && a.d === b.d, neg = a => ({ n: -a.n, d: a.d }), abs = a => a.n < 0n ? neg(a) : a;
const floorF = a => { const q = a.n / a.d; return (a.n % a.d !== 0n && a.n < 0n) ? q - 1n : q; };
const N = 16, L = F(100), SIDE = F(8), HALF = F(50), TEND = 400, NCMP = 40, ZERO = F(0);
const modL = a => sub(a, mul(L, F(floorF(div(a, L)))));
const minImg = a => { let r = modL(a); if (cmp(r, HALF) > 0) r = sub(r, L); return r; };
function world(seed, unequal) {
  let s = seed >>> 0; const rnd = () => ((s = (Math.imul(s, 1103515245) + 12345) >>> 0) / 4294967296);
  const x = [], y = [], vx = [], vy = [];
  for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) {
    x.push(F(25000 * i + 12500 + Math.floor(rnd() * 8001) - 4000, 1000)); y.push(F(25000 * j + 12500 + Math.floor(rnd() * 8001) - 4000, 1000));
    vx.push(F(Math.floor(rnd() * 10001) - 5000, 1000)); vy.push(F(Math.floor(rnd() * 10001) - 5000, 1000)); }
  const m = Array(N).fill(1); if (unequal) { const idx = [...Array(N).keys()]; for (let i = N - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [idx[i], idx[j]] = [idx[j], idx[i]]; } idx.slice(0, N / 2).forEach(i => m[i] = 2); }
  return { x0: x.slice(), y0: y.slice(), vx0: vx.slice(), vy0: vy.slice(), x, y, vx, vy, m: m.map(k => F(k)) };
}
function axisWindow(d0, u) {   // the times (a, b) when |d0 + u·t| < SIDE, or null; Infinity as null ends
  if (u.n === 0n) return cmp(abs(d0), SIDE) < 0 ? [null, null] : undefined;
  let a = div(sub(neg(SIDE), d0), u), b = div(sub(SIDE, d0), u); if (cmp(a, b) > 0) [a, b] = [b, a]; return [a, b];
}
function firstContact(w, i, j, horizon) {   // earliest entry time in [0, horizon] for the pair, with its axis
  const px = minImg(sub(w.x[j], w.x[i])), py = minImg(sub(w.y[j], w.y[i])), ux = sub(w.vx[j], w.vx[i]), uy = sub(w.vy[j], w.vy[i]);
  let best = null;
  for (let kx = -1; kx <= 1; kx++) for (let ky = -1; ky <= 1; ky++) {
    const X = axisWindow(add(px, mul(F(kx), L)), ux), Y = axisWindow(add(py, mul(F(ky), L)), uy); if (!X || !Y) continue;
    const lo = X[0] === null ? Y[0] : Y[0] === null ? X[0] : (cmp(X[0], Y[0]) >= 0 ? X[0] : Y[0]);
    const hi = X[1] === null ? Y[1] : Y[1] === null ? X[1] : (cmp(X[1], Y[1]) <= 0 ? X[1] : Y[1]);
    if (lo === null || hi === null || cmp(lo, hi) >= 0 || cmp(hi, ZERO) <= 0) continue;
    if (cmp(lo, ZERO) < 0) return { overlap: true };
    if (cmp(lo, horizon) > 0) continue;
    const axis = X[0] === null ? 'y' : Y[0] === null ? 'x' : (cmp(X[0], Y[0]) > 0 ? 'x' : cmp(Y[0], X[0]) > 0 ? 'y' : 'xy');
    if (!best || cmp(lo, best.t) < 0) best = { t: lo, axis };
  }
  return best;
}
function run(w) {
  let t = F(0); const sumP = k => w.vx.reduce((a, v, i) => add(a, mul(w.m[i], k ? w.vy[i] : v)), F(0));
  const energy = () => w.vx.reduce((a, v, i) => add(a, mul(w.m[i], add(mul(v, v), mul(w.vy[i], w.vy[i])))), F(0));
  const P0x = sumP(0), P0y = sumP(1), E0 = energy(), sx0 = w.vx0.slice().sort(cmp), sy0 = w.vy0.slice().sort(cmp);
  let consOK = true, overlap = false, corners = 0, multi = 0, events = 0, firstMix = null, offAtFirst = null, firstUnequal = null; const rows = [];
  const offCount = () => { const fr = w.x0.map((x, k) => [modL(add(x, mul(w.vx0[k], t))), modL(add(w.y0[k], mul(w.vy0[k], t))), w.vx0[k], w.vy0[k]]);
    return w.x.reduce((c, _, i) => c + (fr.some(([a, b, u, v]) => eq(a, modL(w.x[i])) && eq(b, modL(w.y[i])) && eq(u, w.vx[i]) && eq(v, w.vy[i])) ? 0 : 1), 0); };
  const setsKept = () => w.vx.slice().sort(cmp).every((v, i) => eq(v, sx0[i])) && w.vy.slice().sort(cmp).every((v, i) => eq(v, sy0[i]));
  for (let j = 1; j <= NCMP; j++) {
    const Tc = F(TEND * j / NCMP);
    while (cmp(t, Tc) < 0) {
      const W = cmp(add(t, F(1)), Tc) < 0 ? add(t, F(1)) : Tc, horizon = sub(W, t);
      let best = null, list = [];
      for (let a = 0; a < N; a++) for (let b = a + 1; b < N; b++) { const c = firstContact(w, a, b, horizon); if (!c) continue;
        if (c.overlap) { overlap = true; continue; } const o = best ? cmp(c.t, best) : -1;
        if (o < 0) { best = c.t; list = [[a, b, c.axis]]; } else if (o === 0) list.push([a, b, c.axis]); }
      const dt = best || horizon;
      for (let i = 0; i < N; i++) { w.x[i] = modL(add(w.x[i], mul(w.vx[i], dt))); w.y[i] = modL(add(w.y[i], mul(w.vy[i], dt))); }
      t = add(t, dt); if (!best) continue;
      const seen = new Set(); for (const [a, b] of list) { if (seen.has(a) || seen.has(b)) multi++; seen.add(a); seen.add(b); }
      for (const [a, b, axis] of list) {
        if (axis === 'xy') corners++;
        const m1 = w.m[a], m2 = w.m[b], s = add(m1, m2);
        for (const ax of axis === 'xy' ? ['x', 'y'] : [axis]) { const V = ax === 'x' ? w.vx : w.vy;
          const v1 = div(add(mul(sub(m1, m2), V[a]), mul(F(2), mul(m2, V[b]))), s), v2 = div(add(mul(sub(m2, m1), V[b]), mul(F(2), mul(m1, V[a]))), s);
          V[a] = v1; V[b] = v2; }
        events++;
        const other = axis === 'x' ? w.vy : w.vx;
        if (!firstMix && eq(m1, m2) && axis !== 'xy' && !eq(other[a], other[b])) { firstMix = Number(t.n) / Number(t.d); offAtFirst = offCount(); }
        if (!firstUnequal && !eq(m1, m2)) firstUnequal = { t: Number(t.n) / Number(t.d), setsKeptAfter: null };
      }
      if (!eq(sumP(0), P0x) || !eq(sumP(1), P0y) || !eq(energy(), E0)) consOK = false;
    }
    const fr = w.x0.map((x, k) => [modL(add(x, mul(w.vx0[k], t))), modL(add(w.y0[k], mul(w.vy0[k], t)))].map(String).join()).sort();
    const tr = w.x.map((x, i) => [modL(x), modL(w.y[i])].map(String).join()).sort();
    rows.push({ T: TEND * j / NCMP, setEq: fr.every((f, i) => f === tr[i]), off: offCount(), setsKept: setsKept(), events,
      digits: Math.max(...w.x.map(a => a.d.toString().length), ...w.y.map(a => a.d.toString().length)) });
  }
  return { rows, consOK, overlap, corners, multi, events, firstMix, offAtFirst, firstUnequal };
}
const out = {};
for (const seed of [1, 2, 3]) {
  const e = run(world(seed, false)), u = run(world(seed, true));
  out['seed' + seed] = {
    equal: { firstMix: e.firstMix, offAtFirst: e.offAtFirst, D1: e.rows.filter(r => r.T > (e.firstMix ?? 1e9)).every(r => !r.setEq), D2offEnd: e.rows.at(-1).off,
      offPath: e.rows.filter((r, i) => i % 4 === 3).map(r => r.off), D3: e.rows.every(r => r.setsKept), D4: e.consOK && !e.overlap, corners: e.corners, multi: e.multi, events: e.events, digits: e.rows.at(-1).digits },
    unequal: { firstUnequal: u.firstUnequal && u.firstUnequal.t, D3setsLost: u.rows.filter(r => r.T > (u.firstUnequal ? u.firstUnequal.t : 1e9)).map(r => !r.setsKept),
      offEnd: u.rows.at(-1).off, offPath: u.rows.filter((r, i) => i % 4 === 3).map(r => r.off), D4: u.consOK && !u.overlap, corners: u.corners, multi: u.multi, events: u.events, digits: u.rows.at(-1).digits }
  };
  console.error('seed', seed, 'done');
}
console.log(JSON.stringify(out, null, 1));
