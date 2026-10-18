// RSH run 2 (plans/rsh-plan.md, "Run 2: many bodies at once"): a field of 40 Levels bodies around three readers.
// One standpoint's census painted by the first body each direction meets (P7, P8); three readers, directions only,
// on a flat screen of pixels ε wide, placing every seen point by its rays (P9), and with ε = 0 exactly (P10).
// bodyOf is games.html's (as recover.html copies it). Run: node rsh/rsh2.mjs
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
const fib = n => { const L = [], ga = Math.PI * (3 - Math.sqrt(5));
    for (let i = 0; i < n; i++){ const y = 1 - 2 * (i + 0.5) / n, q = Math.sqrt(1 - y * y), a = ga * i; L.push([q * Math.cos(a), y, q * Math.sin(a)]); } return L; };
const PTS = fib(1024);
const AX = nrm([1, 1, 1]), E1 = nrm(cross(AX, [0, 1, 0])), E2 = cross(AX, E1);

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
// is the segment from a to the point p (on body own) clear of every body's inside? 64 steps, p's end excluded
function clear(field, a, p){
    const seg = sub(p, a), L = len(seg), d = mul(seg, 1 / L);
    for (const F of field){
        const w = sub(F.c, a), tc = Math.min(Math.max(dot(w, d), 0), L), cl = add(a, mul(d, tc));
        if (len(sub(F.c, cl)) >= F.rb) continue;
        for (let t = 1; t < 64; t++) if (F.inside([a[0] + seg[0] * t / 64, a[1] + seg[1] * t / 64, a[2] + seg[2] * t / 64])) return false;
    }
    return true;
}

// ── the field ─────────────────────────────────────────────────────────────────────────────────────────────
let seed = 2; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const M = 40, PLANT = 12, COS30 = Math.cos(Math.PI / 6);
function coneDir(){ const z = COS30 + (1 - COS30) * rnd(), a = 2 * Math.PI * rnd(), q = Math.sqrt(1 - z * z);
    return add(mul(AX, z), add(mul(E1, q * Math.cos(a)), mul(E2, q * Math.sin(a)))); }
const CEN = [], behind = [];
function freeOf(C, idx){ const F = placed(idx, C); if (len(C) < F.rb + 1) return false;
    for (let j = 0; j < CEN.length; j++){ const G = placed(j, CEN[j]); if (len(sub(C, CEN[j])) <= F.rb + G.rb) return false; } return true; }
for (let i = 0; i < M; i++){
    for (let tries = 0; ; tries++){
        if (tries > 5000) throw new Error('could not place body ' + i);
        let C;
        if (i < M - PLANT){ C = mul(coneDir(), 4 * 2 ** (12 * rnd())); }
        else { const h = Math.floor(rnd() * (M - PLANT)), dh = len(CEN[h]), Fh = placed(h, CEN[h]), Fi = placed(i, [0, 0, 0]);
            const d = Math.max((1.3 + 0.7 * rnd()) * dh, dh + Fh.rb + Fi.rb + 0.1); C = mul(nrm(CEN[h]), d); if (freeOf(C, i)) behind.push([h, i]); else continue; }
        if (freeOf(C, i)){ CEN.push(C); break; }
    }
}
const field = (k = 1, cen = CEN) => cen.map((C, i) => placed(i, C, k));
const F1 = field(1);
const dist = F1.map(F => len(F.c));
const meanR = F1.map(F => { let m = 0; for (const u of PTS) m += len(sub(F.surf(u), F.c)); return m / PTS.length; });
console.log(`field: ${M} bodies, d ${dist.reduce((a, b) => Math.min(a, b)).toFixed(2)} … ${dist.reduce((a, b) => Math.max(a, b)).toFixed(0)}, ` +
    `${behind.length} planted behind, mean radius ${(meanR.reduce((a, b) => a + b) / M).toFixed(3)}`);

// ── the census from O ─────────────────────────────────────────────────────────────────────────────────────
const NC = 1 << 20, O = [0, 0, 0];
const CL = fib(NC);
function census(fl){
    const paint = new Int16Array(NC).fill(-1), hides = new Set();
    const cones = fl.map(F => { const l = len(F.c); return { u: mul(F.c, 1 / l), cs: Math.sqrt(Math.max(0, 1 - (F.rb / l) ** 2)) }; });
    for (let i = 0; i < NC; i++){ const d = CL[i]; if (dot(d, AX) < 0.7) continue;
        const hits = [];
        for (let b = 0; b < fl.length; b++){ if (dot(d, cones[b].u) <= cones[b].cs) continue; const t = enter(fl[b], O, d); if (t !== null) hits.push([t, b]); }
        if (!hits.length) continue;
        hits.sort((x, y) => x[0] - y[0]); paint[i] = hits[0][1];
        for (let x = 0; x < hits.length; x++) for (let y = x + 1; y < hits.length; y++) hides.add(hits[x][1] * 1000 + hits[y][1]);
    }
    return { paint, hides };
}
const C1 = census(F1);
const ok = {};
// P7(a)
let p7a = 0; const hidesK = {};
for (const k of [1e-3, 7, 1e3]){ const Ck = census(field(k)); hidesK[k] = Ck.hides; let diff = 0; for (let i = 0; i < NC; i++) if (Ck.paint[i] !== C1.paint[i]) diff++;
    p7a = Math.max(p7a, diff / NC); console.log(`   k=${k}: ${diff} of ${NC} directions painted otherwise`); }
// P7(b): the nearest body that hides and is hidden by none, whose doubled ball meets no other
const inPair = new Set(); for (const h of C1.hides){ inPair.add(Math.floor(h / 1000)); inPair.add(h % 1000); }
const order = [...dist.keys()].sort((a, b) => dist[a] - dist[b]);
let mv = -1;
for (const b of order){ if (inPair.has(b)) continue; const G = placed(b, mul(CEN[b], 2), 2);
    if (F1.every((F, j) => j === b || len(sub(F.c, G.c)) > F.rb + G.rb)) { mv = b; break; } }
const F2 = F1.slice(); F2[mv] = placed(mv, mul(CEN[mv], 2), 2);
const C2 = census(F2); let d7b = 0; for (let i = 0; i < NC; i++) if (C2.paint[i] !== C1.paint[i]) d7b++;
let share = 0; for (let i = 0; i < NC; i++) if (C1.paint[i] === mv) share++;
console.log(`   body ${mv} (d ${dist[mv].toFixed(1)}, ${share} directions) at 2d and twice the size: ${d7b} directions painted otherwise`);
// P7(c): body 0 alone on the ray (1,1,1)
function solidAngle(F, n = 20000){
    const l = len(F.c), u = mul(F.c, 1 / l), a = Math.asin(Math.min(1, F.rb / l)), one = 2 * Math.sin(a / 2) ** 2;  // 1 − cos α
    const e1 = nrm(cross(u, [0.3, 1, 0.2])), e2 = cross(u, e1), ga = Math.PI * (3 - Math.sqrt(5)); let hit = 0;
    for (let i = 0; i < n; i++){ const w = one * (i + 0.5) / n, z = 1 - w, q = Math.sqrt(w * (2 - w)), ph = ga * i;
        const d = add(mul(u, z), add(mul(e1, q * Math.cos(ph)), mul(e2, q * Math.sin(ph)))); if (enter(F, O, nrm(d)) !== null) hit++; }
    return 2 * Math.PI * one * hit / n;
}
const om = []; for (let j = 0; j <= 11; j++){ const d = 4 * 2 ** j; om.push([d, solidAngle(placed(0, mul(AX, d)))]); }
let p7c = true;
for (let j = 0; j < 11; j++){ const [d, w] = om[j], r = w / om[j + 1][1];
    if (d >= 64 && Math.abs(r / 4 - 1) > 0.02) p7c = false; if (d >= 512 && Math.abs(r / 4 - 1) > 0.005) p7c = false;
    console.log(`   d=${d}: Ω·d² ${(w * d * d).toFixed(5)}, Ω(d)/Ω(2d) ${r.toFixed(5)}`); }
// P7(d): each body alone, the share of its points seen from O
let p7d = 0;
const seenAlone = F1.map((F, b) => { let n = 0; for (const u of PTS) if (clear([F], O, F.surf(u))) n++; const sh = n / PTS.length, want = (1 - meanR[b] / dist[b]) / 2;
    p7d = Math.max(p7d, Math.abs(sh - want)); return [sh, want]; });
console.log(`   seen alone from O against (1 − R̄/d)/2: worst ${p7d.toFixed(4)} (nearest body ${seenAlone[order[0]][0].toFixed(3)} against ${seenAlone[order[0]][1].toFixed(3)})`);
ok.P7 = p7a <= 1e-4 && d7b / NC <= 1e-4 && p7c && p7d <= 0.08;
console.log(`P7 the census: scaled ${p7a.toExponential(2)}, moved and doubled ${(d7b / NC).toExponential(2)}, inverse square ${p7c}, seen share ${p7d.toFixed(4)}`);

// ── P8(a, b): occlusion ───────────────────────────────────────────────────────────────────────────────────
const pairs = [...C1.hides].map(h => [Math.floor(h / 1000), h % 1000]);
let cyc = false; { const adj = Array.from({ length: M }, () => []); for (const [a, b] of pairs) adj[a].push(b);
    const st = new Int8Array(M); const dfs = v => { st[v] = 1; for (const w of adj[v]){ if (st[w] === 1) cyc = true; else if (!st[w]) dfs(w); } st[v] = 2; };
    for (let v = 0; v < M; v++) if (!st[v]) dfs(v); }
let sepBad = 0, sepN = 0, close = 0;
for (const [a, b] of pairs){ if (Math.abs(dist[b] - dist[a]) > F1[a].rb + F1[b].rb){ sepN++; if (dist[a] > dist[b]) sepBad++; } else close++; }
let p8b = true; for (const k of [1e-3, 7, 1e3]){ const s = [...hidesK[k]];
    if (s.length !== C1.hides.size || s.some(h => !C1.hides.has(h))) p8b = false; }
console.log(`   ${pairs.length} hiding pairs: ${sepN} separated (${sepBad} against their centres), ${close} close; a cycle: ${cyc}; the same under k: ${p8b}`);

// ── three readers ─────────────────────────────────────────────────────────────────────────────────────────
const RD = [90, 210, 330].map(a => add(mul(E1, Math.cos(a * Math.PI / 180) / Math.sqrt(3)), mul(E2, Math.sin(a * Math.PI / 180) / Math.sqrt(3))));
const ABlen = len(sub(RD[1], RD[0]));
function readScreen(dir, eps){ const z = dot(dir, AX); let x = dot(dir, E1) / z, y = dot(dir, E2) / z;
    if (eps > 0){ x = (Math.floor(x / eps) + 0.5) * eps; y = (Math.floor(y / eps) + 0.5) * eps; }
    return { x, y, u: eps > 0 ? nrm(add(AX, add(mul(E1, x), mul(E2, y)))) : dir }; }
function lsq(As, us){                // the point nearest every ray A + t·u in least squares
    const M3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], r = [0, 0, 0];
    As.forEach((A, n) => { const u = us[n]; for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++){ const P = (i === j ? 1 : 0) - u[i] * u[j]; M3[i][j] += P; r[i] += P * A[j]; } });
    const det = m => m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
    const D = det(M3); return [0, 1, 2].map(c => det(M3.map((row, i) => row.map((v, j) => j === c ? r[i] : v))) / D);
}
// who sees each point (ε does not enter)
const truePts = F1.map(F => PTS.map(u => F.surf(u)));
const seers = truePts.map(P => P.map(p => [0, 1, 2].filter(i => clear(F1, RD[i], p))));
function readField(eps, k = 1){
    const fl = k === 1 ? F1 : field(k), rd = RD.map(a => mul(a, k)), AB = ABlen * k;
    return fl.map((F, b) => {
        const out = { placed: [], truth: [], rays: 0, two: 0 };
        PTS.forEach((u, n) => { const who = seers[b][n]; if (who.length < 2) return; out.two++;
            const p = F.surf(u), rs = who.map(i => readScreen(nrm(sub(p, rd[i])), eps));
            if (eps > 0 && rs.every(r => r.x === rs[0].x && r.y === rs[0].y)){ out.rays++; return; }
            const q = lsq(who.map(i => mul(rd[i], 1 / AB)), rs.map(r => r.u));
            out.placed.push(q); out.truth.push(mul(p, 1 / AB)); });
        return out; });
}
const cent = P => { const c = [0, 0, 0]; for (const p of P){ c[0] += p[0]; c[1] += p[1]; c[2] += p[2]; } return mul(c, 1 / P.length); };
function errs(R, b){ if (!R.placed.length) return null;
    const cp = cent(R.placed), ct = cent(R.truth), dAB = dist[b] / ABlen, rAB = meanR[b] / ABlen;
    let s2 = 0; R.placed.forEach((q, n) => { const e = sub(sub(q, cp), sub(R.truth[n], ct)); s2 += dot(e, e); });
    return { ep: len(sub(cp, ct)) / dAB, es: Math.sqrt(s2 / R.placed.length) / rAB, cdist: len(cp) * ABlen }; }

// P10: ε = 0
let p10 = 0, p10k = 0, p10w = 0;
const R0 = readField(0);
R0.forEach((R, b) => R.placed.forEach((q, n) => { p10 = Math.max(p10, len(sub(q, R.truth[n])) / len(R.truth[n])); }));
for (const k of [1e-3, 7, 1e3]){ const Rk = readField(0, k);
    Rk.forEach((R, b) => R.placed.forEach((q, n) => { p10k = Math.max(p10k, len(sub(q, R0[b].placed[n])) / len(R0[b].placed[n]));
        const w = mul(q, ABlen * k), tw = mul(truePts[b][n], k); p10w = Math.max(p10w, len(sub(w, tw)) / len(tw)); })); }
let fewest = Infinity; R0.forEach((R, b) => { fewest = Math.min(fewest, R.two); });
ok.P10 = p10 <= 1e-9 && p10k <= 1e-9 && p10w <= 1e-9;
console.log(`P10 ε = 0: every point in |AB| to ${p10.toExponential(2)} of its distance; k moves ${p10k.toExponential(2)}; ` +
    `with |AB| carried in ${p10w.toExponential(2)} (fewest points seen by two on a body: ${fewest})`);

// P9 and P8(c): ε = 10⁻³ and 10⁻⁴
const E = {};
for (const eps of [1e-3, 1e-4]){ const R = readField(eps); E[eps] = R.map((r, b) => ({ ...errs(r, b), rays: r.rays, two: r.two, raySh: r.two ? r.rays / r.two : 0, none: !r.placed.length })); }
const e3 = E[1e-3];
console.log('   body      d     R̄   seen2  rays(1e-3)  e_p(1e-3)  e_s(1e-3)   e_p(1e-4)  e_s(1e-4)');
for (const b of order) console.log(`   ${String(b).padStart(3)} ${dist[b].toFixed(1).padStart(9)} ${meanR[b].toFixed(3)} ${String(e3[b].two).padStart(6)} ` +
    `${e3[b].raySh.toFixed(3).padStart(10)} ${(e3[b].none ? '—' : e3[b].ep.toExponential(2)).padStart(10)} ${(e3[b].none ? '—' : e3[b].es.toExponential(2)).padStart(10)} ` +
    `${(E[1e-4][b].none ? '—' : E[1e-4][b].ep.toExponential(2)).padStart(11)} ${(E[1e-4][b].none ? '—' : E[1e-4][b].es.toExponential(2)).padStart(10)}`);
const all = [...dist.keys()];
const p9a = all.every(b => !(dist[b] < 10) || (!e3[b].none && e3[b].es < 0.1)) && all.every(b => !(dist[b] > 100) || e3[b].none || e3[b].es > 0.1);
const p9b = all.every(b => !(dist[b] < 100) || (!e3[b].none && e3[b].ep < 0.1)) && all.every(b => !(dist[b] > 4000) || e3[b].none || e3[b].ep > 0.1);
const far = all.filter(b => dist[b] > 4000), meanRay = far.reduce((a, b) => a + e3[b].raySh, 0) / far.length;
const p9c = all.every(b => !(dist[b] < 250) || e3[b].rays === 0) && meanRay >= 0.3;
function fit(key, eps){ const xs = [], ys = []; for (const b of all){ const e = E[eps][b]; if (dist[b] < 8 || e.none || !(e[key] < 1) || e[key] <= 0) continue; xs.push(Math.log(dist[b])); ys.push(Math.log(e[key])); }
    const mx = xs.reduce((a, b) => a + b) / xs.length, my = ys.reduce((a, b) => a + b) / ys.length; let sxy = 0, sxx = 0;
    xs.forEach((x, i) => { sxy += (x - mx) * (ys[i] - my); sxx += (x - mx) ** 2; }); return { slope: sxy / sxx, n: xs.length }; }
const fs = fit('es', 1e-3), fp = fit('ep', 1e-3);
const p9d = Math.abs(fs.slope - 2) <= 0.25 && Math.abs(fp.slope - 1) <= 0.25;
function ratio(key){ let s = 0, n = 0; for (const b of all){ const a = E[1e-3][b], c = E[1e-4][b]; if (dist[b] < 8 || a.none || c.none || !(a[key] < 1) || a.rays || c.rays || a[key] <= 0 || c[key] <= 0) continue; s += Math.log(a[key] / c[key]); n++; } return { r: Math.exp(s / n), n }; }
const rs = ratio('es'), rp = ratio('ep');
const p9e = [rs.r, rp.r].every(r => r >= 10 / 1.5 && r <= 15);
ok.P9 = p9a && p9b && p9c && p9d && p9e;
console.log(`P9 (a) shape bands ${p9a}; (b) place bands ${p9b}; (c) no ray nearer than 250 and the mean ray share past 4,000 ${meanRay.toFixed(3)} ` +
    `(${far.length} bodies): ${p9c}; (d) e_s ∝ d^${fs.slope.toFixed(3)} (${fs.n} bodies), e_p ∝ d^${fp.slope.toFixed(3)} (${fp.n}): ${p9d}; ` +
    `(e) ε 10⁻³ over 10⁻⁴: e_s ×${rs.r.toFixed(2)} (${rs.n}), e_p ×${rp.r.toFixed(2)} (${rp.n}): ${p9e}`);
// P8(c)
let nearBad = 0, nearN = 0, farN = 0, farLost = 0; const farRows = [];
for (const [a, b] of pairs){
    if (dist[a] < 100 && dist[b] < 100){ nearN++; if (e3[a].none || e3[b].none || !(e3[a].cdist < e3[b].cdist)) nearBad++; }
    if (dist[a] > 4000){ farN++; const lost = e3[a].none || e3[b].none || !(e3[a].cdist < e3[b].cdist); if (lost) farLost++;
        farRows.push(`${a}→${b} (${dist[a].toFixed(0)}, ${dist[b].toFixed(0)}): placed at ${e3[a].none ? 'rays' : e3[a].cdist.toFixed(0)}, ${e3[b].none ? 'rays' : e3[b].cdist.toFixed(0)}`); }
}
farRows.forEach(r => console.log('   ' + r));
const p8c = nearBad === 0 && farN > 0 && farLost >= 1;
ok.P8 = !cyc && sepBad === 0 && p8b && p8c;
console.log(`P8 (a) no cycle, separated pairs as their centres: ${!cyc && sepBad === 0}; (b) ${p8b}; (c) near pairs ordered by the placed centroids ` +
    `${nearN - nearBad} of ${nearN}, far pairs lost by them ${farLost} of ${farN}: ${p8c}`);
for (const k of ['P7', 'P8', 'P9', 'P10']) console.log(k, ok[k] ? 'not killed' : 'KILLED');
