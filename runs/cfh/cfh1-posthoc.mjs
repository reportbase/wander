// CFH run 1 post hoc (plans/cfh-plan.md): which held directions had no ranged point within 2° (C1), and how the hull's
// tightness on the rim follows the cell's size at the nearest tick that rim was on (C4). The set-up is runs/cfh/cfh.mjs's, copied.
// Run: node runs/cfh/cfh1-posthoc.mjs
const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]], add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
const mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k], dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const len = a => Math.hypot(a[0], a[1], a[2]), nrm = a => mul(a, 1 / len(a));
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const RAD = Math.PI / 180, O = [0, 0, 0];
function bodyOf(idx){
    let s = (Math.imul(idx + 1, 2654435761) ^ 0x9e3779b9) >>> 0;
    const rnd = () => (s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296, waves = [];
    for (let b = 0; b < 4; b++){ const m = 0.3 + 1.4 * rnd();
        for (let j = 0; j < 5; j++){ const z = rnd() * 2 - 1, a = rnd() * 2 * Math.PI, q = Math.sqrt(1 - z * z);
            waves.push({ b, f: 3 * 2 ** b, A: 0.07 / 2 ** b * m, d: [q * Math.cos(a), z, q * Math.sin(a)], ph: rnd() * 2 * Math.PI }); } }
    return { waves };
}
// the moon: body 3's waves, stretch 1, its centre at C, the world scaled by k
const W3 = bodyOf(3).waves;
const R = u => { let r = 0; for (const w of W3) r += w.A * Math.cos(w.f * dot(u, w.d) + w.ph); return 0.5 * (1 + r); };
let SA = 0; for (const w of W3) SA += w.A;
function moon(C, k = 1){
    const c = mul(C, k);
    const surf = u => add(c, mul(u, k * R(u)));
    const inside = q => { const w = sub(q, c), l = len(w); if (l < 1e-300) return true; return l < k * R(mul(w, 1 / l)) * (1 - 1e-12); };
    return { c, surf, inside, rb: 0.5 * k * (1 + SA) };
}
function enter(F, o, d, steps = 256){
    const w = sub(F.c, o), tc = dot(w, d), q2 = dot(w, w) - tc * tc; if (q2 >= F.rb * F.rb) return null;
    const hw = Math.sqrt(F.rb * F.rb - q2), t0 = Math.max(0, tc - hw), t1 = tc + hw, at = t => F.inside(add(o, mul(d, t)));
    let prev = t0;
    for (let i = 1; i <= steps; i++){ const t = t0 + (t1 - t0) * i / steps;
        if (at(t)){ let a = prev, b = t; for (let j = 0; j < 60; j++){ const m = 0.5 * (a + b); if (at(m)) b = m; else a = m; } return b; } prev = t; }
    return null;
}
const fib = n => { const L = [], ga = Math.PI * (3 - Math.sqrt(5)); for (let i = 0; i < n; i++){ const y = 1 - 2 * (i + 0.5) / n, q = Math.sqrt(1 - y * y), a = ga * i; L.push([q * Math.cos(a), y, q * Math.sin(a)]); } return L; };
const LAT = fib(4096);
let RBAR = 0; for (const u of LAT) RBAR += R(u); RBAR /= LAT.length;

// the path: from 40 out at ψ = 30°, a = 25°, speed 1 a tick, 20° off straight toward O, in the plane of that direction and v
const dirOf = (ps, a) => [Math.cos(a) * Math.cos(ps), Math.sin(a), Math.cos(a) * Math.sin(ps)];
const U0 = dirOf(30 * RAD, 25 * RAD), EP = nrm(sub([0, 1, 0], mul(U0, U0[1])));
const VEL = add(mul(U0, -Math.cos(20 * RAD)), mul(EP, Math.sin(20 * RAD)));
const centre = t => add(mul(U0, 40), mul(VEL, t));
const TICKS = []; for (let t = 0; len(centre(t)) > 15; t++)   // run 2: d > 15 (run 1 asked d > 12, never reached)
{ const c = centre(t); if (c.some(x => x <= 0)) throw new Error('left the wedge'); TICKS.push(t); }


// ── the inscribed sweep, each detection carrying its range ρ (the distance along its ray to the first surface point) ──
const NG = 4096, N = NG * NG;
const cell = (i, j) => { const ps = (i + 0.5) / NG * Math.PI / 2, y = (j + 0.5) / NG, q = Math.sqrt(1 - y * y); return [q * Math.cos(ps), y, q * Math.sin(ps)]; };
const cellOf = x => { const l = len(x), y = x[1] / l, ps = Math.atan2(x[2], x[0]);
    if (y < 0 || y >= 1 || ps < 0 || ps >= Math.PI / 2) return -1;
    return Math.floor(y * NG) * NG + Math.floor(ps / (Math.PI / 2) * NG); };
function sweep(F){
    const dc = len(F.c), u = mul(F.c, 1 / dc), al = Math.asin(F.rb / dc), cs = Math.cos(al);
    const ac = Math.asin(u[1]), ps = Math.atan2(u[2], u[0]), amax = Math.min(Math.PI / 2, ac + al), dps = al / Math.cos(amax) + 2 * Math.PI / 2 / NG;
    const j0 = Math.max(0, Math.floor(Math.sin(Math.max(0, ac - al)) * NG) - 1), j1 = Math.min(NG - 1, Math.ceil(Math.sin(amax) * NG) + 1);
    const i0 = Math.max(0, Math.floor((ps - dps) / (Math.PI / 2) * NG) - 1), i1 = Math.min(NG - 1, Math.ceil((ps + dps) / (Math.PI / 2) * NG) + 1);
    const det = [], rho = [], dirs = []; let sum = [0, 0, 0];
    for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++){ const d = cell(i, j); if (dot(d, u) <= cs) continue;
        const e = enter(F, O, d); if (e !== null){ det.push(j * NG + i); rho.push(e); dirs.push(d); sum = add(sum, d); } }
    const bits = new Uint32Array(N / 32); for (const x of det) bits[x >>> 5] |= 1 << (x & 31);
    return { det, rho, dirs, bits, share: det.length / N * Math.PI / 2, c: nrm(sum) };
}
const has = (S, x) => { const c = cellOf(x); return c >= 0 && (S.bits[c >>> 5] >>> (c & 31) & 1) === 1; };
const ok = {}, T0 = Date.now(), el = () => `${((Date.now() - T0) / 1000).toFixed(0)} s`;
const S1 = TICKS.map(t => sweep(moon(centre(t))));
console.log(`moon: body 3, mean radius ${RBAR.toFixed(4)}; ${TICKS.length} ticks, d ${len(centre(0)).toFixed(2)} → ${len(centre(TICKS.at(-1))).toFixed(2)}; ` +
    `${S1[0].det.length} → ${S1.at(-1).det.length} addresses met (${el()})`);

// the sets compared: held (seen from home at some tick) and rim (within 3° of square to the line to home at some tick)
const heldAt = t => { const F = moon(centre(t)), H = new Set();
    LAT.forEach((u, i) => { const p = F.surf(u), L = len(p), e = enter(F, O, mul(p, 1 / L)); if (e !== null && e >= L * (1 - 1e-9)) H.add(i); }); return H; };
const HELD = new Set(); TICKS.forEach(t => heldAt(t).forEach(i => HELD.add(i)));
const RIM = new Set(), S3 = Math.sin(3 * RAD);
LAT.forEach((u, i) => { if (TICKS.some(t => Math.abs(dot(u, nrm(mul(centre(t), -1)))) < S3)) RIM.add(i); });
const HELD_NR = [...HELD].filter(i => !RIM.has(i));
console.log(`held ${HELD.size} of ${LAT.length} lattice directions (${(HELD.size / LAT.length).toFixed(4)}), rim ${RIM.size}, held and never on the rim ${HELD_NR.length}`);
const TRUE = LAT.map(R);
// a painting on a set: radius over its geometric mean there; compared with the true painting on the same directions
function compare(rad, set){ const ids = set.filter(i => rad[i] > 0 && isFinite(rad[i]));
    const g = a => Math.exp(ids.reduce((s, i) => s + Math.log(a[i]), 0) / ids.length), ga = g(rad), gt = g(TRUE);
    const p = ids.map(i => rad[i] / ga), q = ids.map(i => TRUE[i] / gt), e = p.map((x, n) => x - q[n]);
    const mp = p.reduce((a, b) => a + b, 0) / p.length, mq = q.reduce((a, b) => a + b, 0) / q.length;
    let sxy = 0, sxx = 0, syy = 0; p.forEach((x, n) => { sxy += (x - mp) * (q[n] - mq); sxx += (x - mp) ** 2; syy += (q[n] - mq) ** 2; });
    const ae = e.map(Math.abs).sort((a, b) => a - b);
    return { n: ids.length, of: set.length, rms: Math.sqrt(e.reduce((a, x) => a + x * x, 0) / e.length), worst: ae.at(-1), median: ae[ae.length >> 1], corr: sxy / Math.sqrt(sxx * syy) }; }
const fmt = c => `${c.n}/${c.of} directions: rms ${c.rms.toFixed(4)}, median ${c.median.toFixed(4)}, worst ${c.worst.toFixed(4)}, correlation ${c.corr.toFixed(4)}`;

// a bucket grid on the sphere, to find the ranged point nearest each lattice direction (within 2°)
const COS2 = Math.cos(2 * RAD), BK = 30, key = (a, b, c) => `${a},${b},${c}`;
function nearestRadii(points){   // points: [{u, r}] → per lattice direction the radius of the nearest within 2°, else 0
    const G = new Map(); for (const p of points){ const k = key(...p.u.map(x => Math.floor(x * BK))); if (!G.has(k)) G.set(k, []); G.get(k).push(p); }
    return LAT.map(u => { const b = u.map(x => Math.floor(x * BK)); let best = COS2, r = 0;
        for (let a = -1; a <= 1; a++) for (let c = -1; c <= 1; c++) for (let e = -1; e <= 1; e++){ const L = G.get(key(b[0] + a, b[1] + c, b[2] + e)); if (!L) continue;
            for (const p of L){ const cc = dot(p.u, u); if (cc > best){ best = cc; r = p.r; } } }
        return r; }); }

// ── C1: ranging, centre given ──
let c1 = 0; const P1 = [];
TICKS.forEach((t, n) => { const c = centre(t), S = S1[n]; S.dirs.forEach((d, m) => { const w = sub(mul(d, S.rho[m]), c), r = len(w), u = mul(w, 1 / r);
    c1 = Math.max(c1, Math.abs(r - R(u)) / RBAR); P1.push({ u, r }); }); });
const A1 = nearestRadii(P1), uncovered = [...HELD].filter(i => !(A1[i] > 0)).length;
ok.C1 = c1 <= 1e-9 && uncovered === 0;
console.log(`C1 ranging, centre given: |ρd − c| against R(u) worst ${c1.toExponential(2)} of R̄ over ${P1.length} ranged points; held directions with no ranged point within 2°: ${uncovered}`);
console.log(`   its painting on the held set: ${fmt(compare(A1, [...HELD]))}`);

// ── A2: the centre from the ranges, a sphere fitted each tick, then a straight line at constant speed ──
function solve(A, b){ const n = b.length, M = A.map((r, i) => [...r, b[i]]);
    for (let c = 0; c < n; c++){ let p = c; for (let r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r; [M[c], M[p]] = [M[p], M[c]];
        for (let r = 0; r < n; r++) if (r !== c){ const f = M[r][c] / M[c][c]; for (let k = c; k <= n; k++) M[r][k] -= f * M[c][k]; } }
    return M.map((r, i) => r[n] / r[i]); }
function sphereFit(pts){ const m = mul(pts.reduce((a, p) => add(a, p), [0, 0, 0]), 1 / pts.length), A = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], b = [0, 0, 0, 0];
    for (const p of pts){ const q = sub(p, m), row = [2 * q[0], 2 * q[1], 2 * q[2], 1], y = dot(q, q);
        for (let i = 0; i < 4; i++){ b[i] += row[i] * y; for (let j = 0; j < 4; j++) A[i][j] += row[i] * row[j]; } }
    const x = solve(A, b); return add(m, [x[0], x[1], x[2]]); }
function lineFit(cs){ const n = cs.length, tm = TICKS.reduce((a, t) => a + t, 0) / n, cm = mul(cs.reduce((a, c) => add(a, c), [0, 0, 0]), 1 / n);
    let stt = 0, b = [0, 0, 0]; TICKS.forEach((t, i) => { stt += (t - tm) ** 2; b = add(b, mul(sub(cs[i], cm), t - tm)); });
    const v = mul(b, 1 / stt); return { at: t => add(cm, mul(v, t - tm)), v }; }
function rangedFit(S, k = 1){
    const fits = S.map(s => sphereFit(s.dirs.map((d, m) => mul(d, s.rho[m])))), L = lineFit(fits);
    return { fits, L }; }
const FA = rangedFit(S1);
let wc = 0, wdist = 0; TICKS.forEach((t, n) => { const c = centre(t), e = FA.L.at(t); wc = Math.max(wc, len(sub(e, c)) / RBAR); wdist = Math.max(wdist, Math.abs(len(e) / len(c) - 1)); });
const wspeed = Math.abs(len(FA.L.v) - 1);
const P2 = []; TICKS.forEach((t, n) => { const c = FA.L.at(t), S = S1[n]; S.dirs.forEach((d, m) => { const w = sub(mul(d, S.rho[m]), c), r = len(w); P2.push({ u: mul(w, 1 / r), r }); }); });
const A2 = nearestRadii(P2), C3c = compare(A2, [...HELD]);
console.log(`A2 the centre from the ranges: worst ${wc.toFixed(4)} R̄ from the true centre; per-tick sphere fits off ${Math.max(...TICKS.map((t, n) => len(sub(FA.fits[n], centre(t))) / RBAR)).toFixed(4)} R̄ at worst`);
console.log(`   distance worst ${(100 * wdist).toFixed(3)}%, speed ${len(FA.L.v).toFixed(5)} a tick (${(100 * wspeed).toFixed(3)}% off 1)`);
console.log(`C3 its painting on the held set: ${fmt(C3c)}`);
ok.C3 = wc <= 0.1 && C3c.rms <= 0.05 && C3c.worst <= 0.12 && C3c.corr >= 0.8;

// ── B: the visual hull in the moon's frame, along each lattice direction from the centre, given a track ──
function hull(S, track, scale){   // scale: a length unit for the march (R̄ in world units, or the same in the track's unit)
    const step = 0.001 * scale / RBAR, rmax = 3 * scale;   // the plan's steps of 0.001 world units, in the track's unit
    const cs = TICKS.map(t => track(t));
    return LAT.map(u => { let r = 0;
        for (; r <= rmax; r += step){ const x = mul(u, r); let kept = true;
            for (let n = 0; n < cs.length; n++) if (!has(S[n], add(cs[n], x))){ kept = false; break; }
            if (!kept) break; }
        return r; }); }
const B1 = hull(S1, centre, RBAR);

// C1: the uncovered held directions, how far their nearest ranged point is, and how near the limb they are held
const miss = [...HELD].filter(i => !(A1[i] > 0));
for (const i of miss){ const u = LAT[i]; let best = -1; for (const p of P1) best = Math.max(best, dot(p.u, u));
    let graze = 0; TICKS.forEach(t => { const F = moon(centre(t)), p = F.surf(u), L = len(p), e = enter(F, O, mul(p, 1 / L));
        if (e !== null && e >= L * (1 - 1e-9)) graze = Math.max(graze, Math.abs(dot(u, nrm(mul(centre(t), -1))))); });
    console.log(`C1 uncovered lattice direction ${i}: nearest ranged point ${(Math.acos(Math.min(1, best)) / RAD).toFixed(2)}°, ` +
        `its largest cosine to home while held ${graze.toFixed(4)} (0 is the limb)`); }
// C4: each rim direction's error against one cell's breadth at the nearest tick it was on the rim, in R̄
const CELL = Math.PI / 2 / NG;
const rows = [...RIM].map(i => { const u = LAT[i]; let dmin = Infinity;
    TICKS.forEach(t => { if (Math.abs(dot(u, nrm(mul(centre(t), -1)))) < S3) dmin = Math.min(dmin, len(centre(t))); });
    return { e: B1[i] / TRUE[i] - 1, cellRel: CELL * dmin / TRUE[i], dmin }; });
for (const [lo, hi] of [[15, 20], [20, 25], [25, 30], [30, 35], [35, 41]]){ const g = rows.filter(r => r.dmin >= lo && r.dmin < hi); if (!g.length) continue;
    const es = g.map(r => r.e).sort((a, b) => a - b), cs = g.map(r => r.cellRel).sort((a, b) => a - b);
    console.log(`C4 rim directions last on the rim at d ${lo}–${hi}: ${g.length}, error median ${es[es.length >> 1].toFixed(4)}, within 3% ${(100 * es.filter(x => Math.abs(x) <= 0.03).length / es.length).toFixed(1)}%, ` +
        `one cell there ${cs[cs.length >> 1].toFixed(4)} of R`); }
const within = (m) => rows.filter(r => Math.abs(r.e) <= m * r.cellRel).length / rows.length;
console.log(`C4 rim directions within 1, 2, 3 cells' breadth at their nearest rim tick: ${[1, 2, 3].map(m => (100 * within(m)).toFixed(1) + '%').join(', ')}`);
