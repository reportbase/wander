// SKY (plans/sky-plan.md): a sky of 40 moving Levels bodies, tracked by the inscribed sweep's detections alone. The
// vector helpers, bodyOf, placed and enter are run 3's (rsh/rsh2.mjs), copied unchanged. Run: node sky/sky.mjs
const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]], add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
const mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k], dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2];
const len = a => Math.hypot(a[0], a[1], a[2]), nrm = a => mul(a, 1 / len(a));
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];

function bodyOf(idx){
    let s = (Math.imul(idx + 1, 2654435761) ^ 0x9e3779b9) >>> 0;
    const rnd = () => (s = (Math.imul(s, 1664525) + 1013904223) >>> 0) / 4294967296, waves = [];
    for (let b = 0; b < 4; b++){ const m = 0.3 + 1.4 * rnd();
        for (let j = 0; j < 5; j++){ const z = rnd() * 2 - 1, a = rnd() * 2 * Math.PI, q = Math.sqrt(1 - z * z);
            waves.push({ b, f: 3 * 2 ** b, A: 0.07 / 2 ** b * m, d: [q * Math.cos(a), z, q * Math.sin(a)], ph: rnd() * 2 * Math.PI }); } }
    const st = [0.85 + 0.3 * rnd(), 0.8 + 0.5 * rnd(), 0.85 + 0.3 * rnd()];
    return { waves, s: st };
}
// a body placed with its centre at C, the world scaled by k (centre and stretch alike)
function placed(idx, C, k = 1){
    const B = bodyOf(idx), s = B.s.map(x => x * k), c = mul(C, k);
    const R = u => { let r = 0; for (const w of B.waves) r += w.A * Math.cos(w.f * dot(u, w.d) + w.ph); return 0.5 * (1 + r); };
    const surf = u => { const r = R(u); return [c[0] + s[0] * r * u[0], c[1] + s[1] * r * u[1], c[2] + s[2] * r * u[2]]; };
    const hit = d => surf(nrm([d[0] / s[0], d[1] / s[1], d[2] / s[2]]));
    const inside = q => { const w = sub(q, c), l = len(w); if (l < 1e-300) return true; return l < len(sub(hit(w), c)) * (1 - 1e-12); };
    let sa = 0; for (const w of B.waves) sa += w.A;
    const rb = 0.5 * Math.max(...s) * (1 + sa);       // a bounding ball: R(u) ≤ ½(1 + Σ|A|)
    return { idx, c, s, R, surf, hit, inside, rb };
}
// first t ≥ 0 at which the ray o + t·d enters body F (d a unit vector), or null; marched then bisected
function enter(F, o, d, steps = 256){
    const w = sub(F.c, o), tc = dot(w, d), q2 = dot(w, w) - tc * tc;
    if (q2 >= F.rb * F.rb) return null;
    const hw = Math.sqrt(F.rb * F.rb - q2); let t0 = Math.max(0, tc - hw); const t1 = tc + hw;
    const at = t => F.inside([o[0] + t * d[0], o[1] + t * d[1], o[2] + t * d[2]]);
    let prev = t0;
    for (let i = 1; i <= steps; i++){ const t = t0 + (t1 - t0) * i / steps;
        if (at(t)){ let a = prev, b = t; for (let j = 0; j < 60; j++){ const m = 0.5 * (a + b); if (at(m)) b = m; else a = m; } return b; }
        prev = t; }
    return null;
}
const O = [0, 0, 0], AX = nrm([1, 1, 1]), E1 = nrm(cross(AX, [0, 1, 0])), E2 = cross(AX, E1);
let seed = 3; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const NG = 2048, N = NG * NG, CELL = Math.PI / 2 / NG, T = 25, MID = 12, M = 40, PAIRS = 4;
const COS30 = Math.cos(Math.PI / 6);
const coneDir = () => { const z = COS30 + (1 - COS30) * rnd(), a = 2 * Math.PI * rnd(), q = Math.sqrt(1 - z * z);
    return add(mul(AX, z), add(mul(E1, q * Math.cos(a)), mul(E2, q * Math.sin(a)))); };
// a velocity: turning 3–10 cells a tick across the line of sight, radial speed d/τ₀ with τ₀ in ±[30, 300]
function velocity(C){ const d = len(C), u = mul(C, 1 / d), w = nrm(cross(u, [rnd() - 0.5, rnd() - 0.5, rnd() - 0.5]));
    const om = (3 + 7 * rnd()) * CELL, tau0 = (30 + 270 * rnd()) * (rnd() < 0.5 ? 1 : -1);
    return add(mul(w, om * d), mul(u, -d / tau0)); }
const rbOf = idx => placed(idx, [0, 0, 0]).rb;
const inOct = c => c[0] > 0 && c[1] > 0 && c[2] > 0;
// the least distance between two linearly moving centres over the run
function closest(A, VA, B, VB){ const D0 = sub(A, B), DV = sub(VA, VB), vv = dot(DV, DV); let t = vv > 0 ? -dot(D0, DV) / vv : 0; t = Math.max(0, Math.min(T - 1, t)); return len(add(D0, mul(DV, t))); }
const C0 = [], V = [];
function fits(c0, v, idx){ for (let t = 0; t < T; t++) if (!inOct(add(c0, mul(v, t))) || len(add(c0, mul(v, t))) < rbOf(idx) + 2) return false;
    return C0.every((c, j) => closest(c0, v, c, V[j]) > rbOf(idx) + rbOf(j)); }
for (let i = 0; i < M - 2 * PAIRS; i++) for (let tries = 0; ; tries++){ if (tries > 20000) throw new Error('place ' + i);
    const Cm = mul(coneDir(), 16 * 2 ** (10 * rnd())), v = velocity(Cm), c0 = sub(Cm, mul(v, MID)); if (fits(c0, v, i)){ C0.push(c0); V.push(v); break; } }
for (let p = 0; p < PAIRS; p++){ const a = M - 2 * PAIRS + 2 * p, b = a + 1;
    for (let tries = 0; ; tries++){ if (tries > 20000) throw new Error('pair ' + p);
        const u = coneDir(), dn = 16 * 2 ** (7 * rnd()), df = dn * (1.5 + 1.5 * rnd()), Ca = mul(u, dn), Cb = mul(u, df), va = velocity(Ca), vb = velocity(Cb);
        const ca = sub(Ca, mul(va, MID)), cb = sub(Cb, mul(vb, MID));
        if (!fits(ca, va, a)) continue; C0.push(ca); V.push(va); if (fits(cb, vb, b)){ C0.push(cb); V.push(vb); break; } C0.pop(); V.pop(); } }
const centre = (b, t, k = 1) => mul(add(C0[b], mul(V[b], t)), k);
const bodyAt = (b, t, k = 1) => placed(b, centre(b, t, 1), k);
const cellOf = d => { const ps = Math.atan2(d[2], d[0]), i = Math.min(NG - 1, Math.max(0, Math.floor(ps / (Math.PI / 2) * NG))), j = Math.min(NG - 1, Math.max(0, Math.floor(d[1] * NG))); return j * NG + i; };
const cellDir = id => { const i = id % NG, j = (id - i) / NG, ps = (i + 0.5) * CELL, y = (j + 0.5) / NG, q = Math.sqrt(1 - y * y); return [q * Math.cos(ps), y, q * Math.sin(ps)]; };
// ── one tick's sweep: the detections, and the referee's label for each ──
function sweep(t, k = 1){
    const F = Array.from({ length: M }, (_, b) => bodyAt(b, t, k)), lab = new Map();
    const cones = F.map(f => { const dc = len(f.c); return { u: mul(f.c, 1 / dc), al: Math.asin(Math.min(1, f.rb / dc)) }; });
    F.forEach((f, b) => { const { u, al } = cones[b], cs = Math.cos(al), ac = Math.asin(u[1]), ps = Math.atan2(u[2], u[0]), amax = Math.min(Math.PI / 2, ac + al), dps = al / Math.cos(amax) + CELL;
        const j0 = Math.max(0, Math.floor(Math.sin(Math.max(0, ac - al)) * NG) - 1), j1 = Math.min(NG - 1, Math.ceil(Math.sin(amax) * NG) + 1);
        const i0 = Math.max(0, Math.floor((ps - dps) / CELL) - 1), i1 = Math.min(NG - 1, Math.ceil((ps + dps) / CELL) + 1);
        for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++){ const id = j * NG + i, d = cellDir(id); if (dot(d, u) <= cs) continue;
            const e = enter(f, O, d); if (e === null) continue; const cur = lab.get(id); if (!cur || e < cur[0]) lab.set(id, [e, b]); } });
    // a body under a cell lights the cell holding its centre direction, unless a nearer body is met first along that ray
    const lit = [];
    F.forEach((f, b) => { const dc = len(f.c), u = mul(f.c, 1 / dc), id = cellOf(u), cur = lab.get(id);
        let hid = false; F.forEach((g, a) => { if (a === b || hid) return; if (dot(u, cones[a].u) <= Math.cos(cones[a].al)) return; const e = enter(g, O, u); if (e !== null && e < dc) hid = true; });
        if (!hid && !cur){ lab.set(id, [dc, b]); lit.push(b); } });
    return { lab, F };
}
// patches: 8-connected groups of detected cells
function patches(lab){ const seen = new Set(), out = [];
    for (const id of lab.keys()){ if (seen.has(id)) continue; const comp = [], st = [id]; seen.add(id);
        while (st.length){ const c = st.pop(); comp.push(c); const i = c % NG, j = (c - i) / NG;
            for (let dj = -1; dj <= 1; dj++) for (let di = -1; di <= 1; di++){ if (!di && !dj) continue; const ii = i + di, jj = j + dj; if (ii < 0 || jj < 0 || ii >= NG || jj >= NG) continue;
                const n = jj * NG + ii; if (lab.has(n) && !seen.has(n)){ seen.add(n); st.push(n); } } }
        let s = [0, 0, 0]; for (const c of comp) s = add(s, cellDir(c)); out.push({ cells: comp, dir: nrm(s), share: comp.length / N * Math.PI / 2 }); }
    return out; }
const ang = (a, b) => Math.acos(Math.max(-1, Math.min(1, dot(a, b))));
const ok = {};
// ── run the sky ──
const TICK = [];
for (let t = 0; t < T; t++){ const { lab, F } = sweep(t), P = patches(lab), count = new Map();
    for (const [, [, b]] of lab) count.set(b, (count.get(b) || 0) + 1);
    P.forEach(p => { const bs = new Set(p.cells.map(c => lab.get(c)[1])); p.bodies = [...bs]; p.clean = bs.size === 1 && count.get(p.bodies[0]) === p.cells.length; });
    const of = new Map(); P.forEach((p, n) => { if (p.clean) of.set(p.bodies[0], n); });
    const touch = new Set(); for (let b = 0; b < M; b++) if (!of.has(b)) touch.add(b);
    TICK.push({ lab, P, of, touch, F }); }
const rad = Array.from({ length: M }, (_, b) => Math.max(...Array.from({ length: T }, (_, t) => rbOf(b) / len(centre(b, t)))));
console.log(`sky: ${M} bodies (${2 * PAIRS} in ${PAIRS} crossing pairs), d ${Math.min(...C0.map((c, b) => len(centre(b, MID)))).toFixed(1)} … ${Math.max(...C0.map((c, b) => len(centre(b, MID)))).toFixed(0)}; ` +
    `${T} ticks; patches per tick ${Math.min(...TICK.map(x => x.P.length))}–${Math.max(...TICK.map(x => x.P.length))}; under one cell all run: ${rad.filter(r => r < CELL / 2).length}`);
// S1
let s1 = 0, s1n = 0; for (const k of [1e-3, 7, 1e3]) for (let t = 0; t < T; t++){ const L = sweep(t, k).lab, A = TICK[t].lab; s1n += A.size; for (const id of A.keys()) if (!L.has(id)) s1++; for (const id of L.keys()) if (!A.has(id)) s1++; }
ok.S1 = s1 / s1n <= 1e-4;
console.log(`S1 the world scaled by 10⁻³, 7, 10³: ${s1} detections differ of ${s1n}`);
// S2
const trueOm = (b, t) => { const C = centre(b, t); return len(cross(C, V[b])) / dot(C, C); };
let s2n = 0, s2w = 0; const sub1 = [];
for (let b = 0; b < M; b++) for (let t = 1; t < T - 1; t++){ const a = TICK[t - 1].of.get(b), c = TICK[t].of.get(b), e = TICK[t + 1].of.get(b);
    if (a === undefined || c === undefined || e === undefined || TICK[t].P[c].cells.length < 50) continue;
    const om = ang(TICK[t - 1].P[a].dir, TICK[t + 1].P[e].dir) / 2; s2n++; s2w = Math.max(s2w, Math.abs(om / trueOm(b, t) - 1)); }
let s2c = 0, s2cn = 0;
for (let b = 0; b < M; b++){ if (!(rad[b] < CELL / 2)) continue; const a = TICK[0].of.get(b), e = TICK[T - 1].of.get(b); if (a === undefined || e === undefined) continue;
    const est = ang(TICK[0].P[a].dir, TICK[T - 1].P[e].dir), tru = ang(nrm(centre(b, 0)), nrm(centre(b, T - 1))); s2cn++; s2c = Math.max(s2c, Math.abs(est - tru) / CELL); }
ok.S2 = s2n > 0 && s2w <= 0.01 && s2c <= 2;
console.log(`S2 ω from clean patches of 50 cells or more: ${s2n} readings, worst ${(100 * s2w).toFixed(3)}%; bodies under one cell: ${s2cn}, whole-run turn worst ${s2c.toFixed(3)} cells`);
// S3
let s3n = 0, s3w = 0; const s3b = new Set();
for (let b = 0; b < M; b++) for (let t = 2; t < T - 2; t++){ const ids = [-2, -1, 0, 1, 2].map(j => TICK[t + j].of.get(b)); if (ids.some(x => x === undefined)) continue;
    const sh = ids.map((x, j) => TICK[t + j - 2].P[x]); if (sh.some(p => p.cells.length < 2000)) continue;
    let sl = 0; sh.forEach((p, j) => { sl += (j - 2) * Math.log(p.share); }); sl /= 10;
    const C = centre(b, t), d = len(C), tauT = d / -(dot(C, V[b]) / d), tau = 2 / sl; s3n++; s3b.add(b); s3w = Math.max(s3w, Math.abs(tau / tauT - 1)); }
ok.S3 = s3n > 0 && s3w <= 0.03;
console.log(`S3 τ over five ticks for clean patches of 2,000 cells or more: ${s3n} readings on ${s3b.size} bodies, worst ${(100 * s3w).toFixed(2)}%`);
// S4: the tracker, from the detections alone
// (the plan leaves a one-point track's "last step" open: taken, before running, as the largest step a body is given, 10 cells)
const tracks = [], links = [];
for (let t = 0; t < T; t++){ const P = TICK[t].P, cand = [];
    tracks.forEach((tr, n) => { if (tr.dead) return; const k = tr.pts.length, last = tr.pts[k - 1], gap = t - last.t;
        let pred = last.dir, step = 10 * CELL;
        if (k >= 2){ const prev = tr.pts[k - 2], v = mul(sub(last.dir, prev.dir), 1 / (last.t - prev.t)); pred = nrm(add(last.dir, mul(v, gap))); step = ang(last.dir, prev.dir) / (last.t - prev.t); }
        const gate = 3 * CELL + 2 * step * gap;
        P.forEach((p, m) => { const dd = ang(pred, p.dir); if (dd <= gate) cand.push([dd, n, m]); }); });
    cand.sort((a, b) => a[0] - b[0]); const usedT = new Set(), usedP = new Set();
    for (const [, n, m] of cand){ if (usedT.has(n) || usedP.has(m)) continue; usedT.add(n); usedP.add(m); const tr = tracks[n], last = tr.pts.at(-1);
        links.push({ from: [last.t, last.m], to: [t, m], tr: n }); tr.pts.push({ t, m, dir: P[m].dir }); tr.coast = 0; }
    tracks.forEach((tr, n) => { if (!tr.dead && !usedT.has(n) && tr.pts.at(-1).t < t){ tr.coast = (tr.coast || 0) + 1; if (tr.coast > 2) tr.dead = true; } });
    P.forEach((p, m) => { if (!usedP.has(m)) tracks.push({ pts: [{ t, m, dir: p.dir }], coast: 0 }); }); }
let wrong = 0, missing = 0, atTouch = 0, cleanPairs = 0;
const linkFrom = new Map(); links.forEach(L => linkFrom.set(L.from.join(':'), L));
for (let t = 1; t < T; t++){ const A = TICK[t - 1], B = TICK[t], touching = A.touch.size + B.touch.size > 0;
    for (let b = 0; b < M; b++){ const a = A.of.get(b), c = B.of.get(b); if (a === undefined || c === undefined) continue; cleanPairs++;
        const L = linkFrom.get((t - 1) + ':' + a); if (!L || L.to[0] !== t){ missing++; continue; } const q = B.P[L.to[1]]; if (!(q.clean && q.bodies[0] === b)) wrong++; }
    // links touching an unclean patch at either end: wrong or missing ones there
    for (const L of links){ if (L.to[0] !== t || L.from[0] !== t - 1) continue; const p = A.P[L.from[1]], q = B.P[L.to[1]];
        if (!(p.clean && q.clean) && !(p.bodies.length === 1 && q.bodies.length === 1 && p.bodies[0] === q.bodies[0])) atTouch++; } }
ok.S4 = wrong === 0 && missing === 0;
console.log(`S4 tracker: ${tracks.length} tracks, ${links.length} links; clean–clean pairs ${cleanPairs}: ${wrong} wrong, ${missing} missing; links at touches that join different bodies or a body to another's patch: ${atTouch}` +
    (atTouch ? '' : ' (the last clause untested)'));
// S5: the far ones as single cells
let s5 = 0, s5n = 0, s5t = 0;
for (let b = 0; b < M; b++){ if (!(rad[b] < CELL / 2)) continue; s5n++; let ticks = 0;
    for (let t = 0; t < T; t++){ const n = TICK[t].of.get(b); if (n === undefined){ continue; } ticks++;
        const p = TICK[t].P[n]; if (p.cells.length !== 1 || p.cells[0] !== cellOf(nrm(centre(b, t)))) s5++; }
    if (ticks === T){ const tr = tracks.filter(tr => tr.pts.some(q => TICK[q.t].P[q.m].clean && TICK[q.t].P[q.m].bodies[0] === b)); if (tr.length !== 1 || tr[0].pts.filter(q => TICK[q.t].P[q.m].bodies.includes(b)).length !== T) s5t++; } }
ok.S5 = s5 === 0 && s5t === 0 && s5n > 0;
console.log(`S5 ${s5n} bodies under one cell: ${s5} ticks not one cell at the centre direction; ${s5t} not one track over all ${T} ticks`);
console.log('   touches by tick: ' + TICK.map(x => x.touch.size).join(' '));
for (const k of ['S1', 'S2', 'S3', 'S4', 'S5']) console.log(k, ok[k] ? 'not killed' : 'KILLED');
