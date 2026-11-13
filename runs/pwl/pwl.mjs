// PWL: where pipelines hit walls. Run from the repository's root: node runs/pwl/pwl.mjs
// Plan and predictions: plans/pwl-plan.md (committed before this script).
const f32 = Math.fround, FOC = 1000, OUT = {};
// ---------- A. distance from the origin ----------
const FRAC = process.env.FRAC === '1';   // run 2: offsets not whole, so rounding begins at once
const corners = []; for (const x of FRAC ? [1.3, 3.7] : [1, 3]) for (const y of [0, 1]) for (const z of FRAC ? [8.1, 10.3] : [8, 10]) corners.push([x, y, z]);
const exactScr = o => [FOC * o[0] / o[2], FOC * o[1] / o[2]];
function bigOf(k) {   // X = 10^k, k in quarter steps, as an exact BigInt (rounded to an integer)
  const n = Math.floor(k), fr = k - n; const m = BigInt(Math.round(10 ** fr * 1e6));
  return n >= 6 ? m * 10n ** BigInt(n - 6) : m / 10n ** BigInt(6 - n) || 1n;
}
function errPlain(X, f) {   // world coordinates stored in the format about a fixed origin
  let worst = 0;
  for (const o of corners) {
    const E = [f(Number(X)), f(2), f(Number(X))];
    const P = FRAC ? [f(Number(X) + o[0]), f(2 + o[1]), f(Number(X) + o[2])] : [f(Number(X + BigInt(o[0]))), f(2 + o[1]), f(Number(X + BigInt(o[2])))];
    const v = [f(P[0] - E[0]), f(P[1] - E[1]), f(P[2] - E[2])];
    const s = [f(f(FOC * v[0]) / v[2]), f(f(FOC * v[1]) / v[2])], t = exactScr(o);
    const e = Math.max(Math.abs(s[0] - t[0]), Math.abs(s[1] - t[1])); worst = Number.isFinite(e) ? Math.max(worst, e) : Infinity;
  }
  return worst;
}
const SEC = 1024n, I64 = x => BigInt.asIntN(64, x);
function errFixed(X) {   // a floating origin over a sector grid: int64 sector index and a float64 offset
  let worst = 0; const sE = I64(X / SEC), lE = Number(X % SEC);
  for (const o of corners) {
    // the thing placed in the eye's sector by its offset (a local position under 1,024 + 11, exact in float64)
    const sPx = sE, lPx = lE + o[0], sPz = sE, lPz = lE + o[2];
    const v = [Number(I64(sPx - sE)) * 1024 + (lPx - lE), o[1], Number(I64(sPz - sE)) * 1024 + (lPz - lE)];
    const s = [FOC * v[0] / v[2], FOC * v[1] / v[2]], t = exactScr(o);
    worst = Math.max(worst, Math.abs(s[0] - t[0]), Math.abs(s[1] - t[1]));
  }
  // aliasing: does the stored place tell X from X + 2^64 sectors?
  const alias = I64(X / SEC) === I64((X + (1n << 64n) * SEC) / SEC);
  return { worst, alias };
}
function errOurs(X) {   // exact: the corner less the eye in fractions (in tenths), then the screen
  let worst = 0; for (const o of corners) { const t10 = x => BigInt(Math.round(x * 10)), X10 = X * 10n;
    const v = [(X10 + t10(o[0])) - X10, t10(o[1]), (X10 + t10(o[2])) - X10];
    const s = [FOC * Number(v[0]) / Number(v[2]), FOC * Number(v[1]) / Number(v[2])], t = exactScr(o);
    worst = Math.max(worst, Math.abs(s[0] - t[0]), Math.abs(s[1] - t[1])); }
  return { worst, digits: X.toString().length };
}
{ const rows = [], firstBreak = { plain32: null, plain64: null, fixed: null, ours: null }; let firstAlias = null;
  for (let q = 0; q <= 400; q++) { const k = q / 4, X = bigOf(k);
    const a = errPlain(X, f32), b = errPlain(X, x => x), c = errFixed(X), d = errOurs(X);
    rows.push({ k, plain32: a, plain64: b, fixed: c.worst, alias: c.alias, ours: d.worst, digits: d.digits });
    if (firstBreak.plain32 === null && !(a <= 0.5)) firstBreak.plain32 = k;
    if (firstBreak.plain64 === null && !(b <= 0.5)) firstBreak.plain64 = k;
    if (firstBreak.fixed === null && !(c.worst <= 0.5)) firstBreak.fixed = k;
    if (firstBreak.ours === null && !(d.worst <= 0.5)) firstBreak.ours = k;
    if (firstAlias === null && c.alias) firstAlias = k; }
  OUT.A = { firstBreak, firstAlias, sample: rows.filter(r => r.k % 5 === 0 || [4, 4.5, 5, 5.5, 13, 13.5, 14, 21, 21.75, 22].includes(r.k)) };
}
// ---------- B. turns composed ----------
let seed = 12345; const rnd = () => ((seed = (Math.imul(seed, 1103515245) + 12345) >>> 0) / 4294967296);
const Q = 128;
function cs(p) { const den = Q * Q + p * p; return [(Q * Q - p * p) / den, 2 * p * Q / den]; }
function mul(A, B, f) { const C = new Array(9); for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) {
  let acc = 0; for (let k = 0; k < 3; k++) acc = f(acc + f(A[3 * i + k] * B[3 * k + j])); C[3 * i + j] = acc; } return C; }
function Ry(p, f) { const [c, s] = cs(p).map(f); return [c, 0, s, 0, 1, 0, -s, 0, c]; }
function offSquare(R) { let m = 0; for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++) { let d = 0;
  for (let k = 0; k < 3; k++) d += R[3 * k + i] * R[3 * k + j]; m = Math.max(m, Math.abs(d - (i === j ? 1 : 0))); } return m; }
const offI = R => Math.max(...R.map((x, i) => Math.abs(x - ([0, 4, 8].includes(i) ? 1 : 0))));
function gram(R, f) {   // re-square the columns
  const col = j => [R[j], R[3 + j], R[6 + j]], dot = (a, b) => f(f(f(a[0] * b[0]) + f(a[1] * b[1])) + f(a[2] * b[2]));
  const nrm = a => { const n = f(Math.sqrt(dot(a, a))); return a.map(x => f(x / n)); };
  const a = nrm(col(0)), b0 = col(1), d1 = dot(a, b0), b = nrm(b0.map((x, i) => f(x - f(d1 * a[i]))));
  const c = [f(f(a[1] * b[2]) - f(a[2] * b[1])), f(f(a[2] * b[0]) - f(a[0] * b[2])), f(f(a[0] * b[1]) - f(a[1] * b[0]))];
  return [a[0], b[0], c[0], a[1], b[1], c[1], a[2], b[2], c[2]];
}
{ const N = 1e6, steps = []; for (let i = 0; i < N; i++) steps.push((rnd() < 0.5 ? -1 : 1) * (1 + Math.floor(rnd() * 12)));
  const res = {};
  for (const [name, f, sq] of [['plain32', f32, false], ['plain64', x => x, false], ['fixed32 re-squared', f32, true], ['fixed64 re-squared', x => x, true]]) {
    let R = [1, 0, 0, 0, 1, 0, 0, 0, 1];
    for (const p of steps) { R = mul(R, Ry(p, f), f); if (sq) R = gram(R, f); }
    const out = offSquare(R);
    for (let i = N - 1; i >= 0; i--) { R = mul(R, Ry(-steps[i], f), f); if (sq) R = gram(R, f); }
    res[name] = { offSquareOut: out, offStartBack: offI(R) };
  }
  // the integer heading (binary angle units, 2^32 a turn)
  const U = 2 ** 32, bam = p => Math.round(U * Math.atan2(2 * p * Q, Q * Q - p * p) / (2 * Math.PI));
  let h = 0; for (const p of steps) h = (h + bam(p)) % U; for (let i = N - 1; i >= 0; i--) h = (h + U + bam(-steps[i])) % U;
  res['fixed integer heading'] = { backExact: h === 0 };
  OUT.B = res;
}
// ours: the page's turnBy (q quarter turns, ky/128, the eighth-turn crossing by tangent subtraction rounded)
function walkOurs(steps) { let q = 0, ky = 0, cross = 0; const KMAX = 53;
  const turn = dk => { ky += dk; while (ky > KMAX) { q++; cross++; ky = Math.round(Q * (ky - Q) / (ky + Q)); }
    while (ky < -KMAX) { q--; cross++; ky = Math.round(Q * (ky + Q) / (Q - ky)); } };
  for (const s of steps) turn(s); for (let i = steps.length - 1; i >= 0; i--) turn(-steps[i]);
  return { back: q === 0 && ky === 0, cross, q, ky }; }
{ let crossWalks = 0, crossBack = 0, plainWalks = 0, plainBack = 0;
  for (let w = 0; w < 100; w++) { const st = []; for (let i = 0; i < 1e4; i++) st.push((rnd() < 0.5 ? -1 : 1) * (1 + Math.floor(rnd() * 12)));
    const r = walkOurs(st); if (r.cross) { crossWalks++; if (r.back) crossBack++; } else { plainWalks++; if (r.back) plainBack++; } }
  let small = 0, smallBack = 0; for (let w = 0; w < 100; w++) { const st = []; for (let i = 0; i < 20; i++) st.push((rnd() < 0.5 ? -1 : 1) * (1 + Math.floor(rnd() * 2)));
    const r = walkOurs(st); if (!r.cross) { small++; if (r.back) smallBack++; } }
  OUT.B.ours = { crossWalks, crossBack, plainWalks, plainBack, noCrossWalks: small, noCrossBack: smallBack };
}
// run 3 (R944): the page's turning since TWK run 12, the heading one whole number N of half-slope steps
function walkOurs2(steps) { let q = 0, ky = 0, cross = 0;
  const turn = dk => { const N = 128 * q + ky + dk, m = Math.floor((N + 128) / 256); if (2 * m !== q) cross++; q = 2 * m; ky = N - 256 * m; };
  for (const s of steps) turn(s); for (let i = steps.length - 1; i >= 0; i--) turn(-steps[i]);
  return { back: q === 0 && ky === 0, cross }; }
{ let crossWalks = 0, crossBack = 0, plainWalks = 0, plainBack = 0;
  for (let w = 0; w < 100; w++) { const st = []; for (let i = 0; i < 1e4; i++) st.push((rnd() < 0.5 ? -1 : 1) * (1 + Math.floor(rnd() * 12)));
    const r = walkOurs2(st); if (r.cross) { crossWalks++; if (r.back) crossBack++; } else { plainWalks++; if (r.back) plainBack++; } }
  OUT.B.ours2 = { crossWalks, crossBack, plainWalks, plainBack };
}
// ---------- C. depth told apart ----------
const NEAR = 0.1, FAR = 1e10, B24 = 2 ** 24 - 1;
const formats = {
  'standard 24-bit': d => Math.round((FAR / (FAR - NEAR)) * (1 - NEAR / d) * B24),
  'log depth 24-bit': d => Math.round(Math.log(d / NEAR) / Math.log(FAR / NEAR) * B24),
  'reversed-Z float32': d => -f32(NEAR / d),   // larger d stores smaller n/d; negate so order is increasing
};
{ const res = {};
  for (const [name, z] of Object.entries(formats)) { res[name] = [];
    for (let j = 0; j <= 9; j++) { const d = 10 ** j; let finest = null;
      for (let m = 0; m <= 64; m++) { const r = 10 ** (-m / 4); if (z(d * (1 + r)) > z(d)) finest = -m / 4; else break; }
      res[name].push({ d: j, log10r: finest }); } }
  let lastStd = null; for (let q = 0; q <= 40; q++) { const d = 10 ** (q / 4); if (formats['standard 24-bit'](d * 1.01) > formats['standard 24-bit'](d)) lastStd = q / 4; }
  res.std1pctLastLog10d = lastStd;
  res.ours = 'exact comparison of fractions: every r > 0 ordered at every d';
  OUT.C = res;
}
console.log(JSON.stringify(OUT, null, 1));
