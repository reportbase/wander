// RSH run 4 (plans/rsh-plan.md, "Run 4: the inscribed reader among many bodies"). One reader at home sweeps the whole
// wedge uniformly (a grid even in azimuth and height: equal shares of the sweep), each address painted by the first body
// it meets; three readers with equal-angle pixels (altitude and azimuth each rounded to ε). The field, its helpers and the
// readers' code are run 3's (runs/rsh/rsh2.mjs), copied unchanged; what is new is below "the inscribed sweep".
// Run: node runs/rsh/rsh4.mjs
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
// is p (a point of some body's surface) seen from a? Seen when no body's inside is met along the ray before it: the ray
// marched through each bounding ball it crosses and bisected (enter). Run 2 stepped 64 times along the whole segment,
// which steps clean over a body far off.
function clear(field, a, p){
    const seg = sub(p, a), L = len(seg), d = mul(seg, 1 / L);
    for (const F of field){ const t = enter(F, a, d); if (t !== null && t < L - 1e-9 * (L + F.rb)) return false; }
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

function solidAngle(F, n = 20000){
    const l = len(F.c), u = mul(F.c, 1 / l), a = Math.asin(Math.min(1, F.rb / l)), one = 2 * Math.sin(a / 2) ** 2;  // 1 − cos α
    const e1 = nrm(cross(u, [0.3, 1, 0.2])), e2 = cross(u, e1), ga = Math.PI * (3 - Math.sqrt(5)); let hit = 0;
    for (let i = 0; i < n; i++){ const w = one * (i + 0.5) / n, z = 1 - w, q = Math.sqrt(w * (2 - w)), ph = ga * i;
        const d = add(mul(u, z), add(mul(e1, q * Math.cos(ph)), mul(e2, q * Math.sin(ph)))); if (enter(F, O, nrm(d)) !== null) hit++; }
    return 2 * Math.PI * one * hit / n;
}
// ── three readers ─────────────────────────────────────────────────────────────────────────────────────────
const RD = [90, 210, 330].map(a => add(mul(E1, Math.cos(a * Math.PI / 180) / Math.sqrt(3)), mul(E2, Math.sin(a * Math.PI / 180) / Math.sqrt(3))));
const ABlen = len(sub(RD[1], RD[0]));
function readScreen(dir, eps){ const z = dot(dir, AX); let x = dot(dir, E1) / z, y = dot(dir, E2) / z;
    if (eps > 0){ x = (Math.floor(x / eps) + 0.5) * eps; y = (Math.floor(y / eps) + 0.5) * eps; }
    return { x, y, u: eps > 0 ? nrm(add(AX, add(mul(E1, x), mul(E2, y)))) : dir }; }
function lsq(As, us){                // the point nearest every ray A + t·u in least squares, in the frame of the rays' mean
    // direction m: each u = (c, p, q) there, and 1 − c² = p² + q² taken from p and q, so the small eigenvalue along m
    // (about γ², the rays nearly parallel far off) is not lost to rounding, as it was on the normal equations in run 2
    const m = nrm(us.reduce((x, u) => add(x, u), [0, 0, 0])), f = nrm(cross(m, Math.abs(m[0]) < 0.9 ? [1, 0, 0] : [0, 1, 0])), g = cross(m, f);
    const o = mul(As.reduce((x, A) => add(x, A), [0, 0, 0]), 1 / As.length);
    const M3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], r = [0, 0, 0];
    As.forEach((A0, n) => { const u = us[n], pq = [dot(u, f), dot(u, g)], c = dot(u, m), U = [c, pq[0], pq[1]];
        const w = sub(A0, o), A = [dot(w, m), dot(w, f), dot(w, g)];
        const P = [[pq[0] ** 2 + pq[1] ** 2, -c * U[1], -c * U[2]], [-c * U[1], 1 - U[1] ** 2, -U[1] * U[2]], [-c * U[2], -U[1] * U[2], 1 - U[2] ** 2]];
        for (let i = 0; i < 3; i++) for (let j = 0; j < 3; j++){ M3[i][j] += P[i][j]; r[i] += P[i][j] * A[j]; } });
    const det = q => q[0][0] * (q[1][1] * q[2][2] - q[1][2] * q[2][1]) - q[0][1] * (q[1][0] * q[2][2] - q[1][2] * q[2][0]) + q[0][2] * (q[1][0] * q[2][1] - q[1][1] * q[2][0]);
    const D = det(M3), x = [0, 1, 2].map(cc => det(M3.map((row, i) => row.map((v, j) => j === cc ? r[i] : v))) / D);
    return add(o, add(mul(m, x[0]), add(mul(f, x[1]), mul(g, x[2]))));
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

// ── the inscribed sweep: 2¹¹ × 2¹¹ addresses, even in azimuth ψ (v₂/h = tan ψ) and in height (h → x, v → y, v₂ → z) ──
const NG = 2048, NA = NG * NG, O = [0, 0, 0];
const addr = i => { const a = i % NG, b = (i - a) / NG, ps = (a + 0.5) / NG * Math.PI / 2, y = (b + 0.5) / NG, q = Math.sqrt(1 - y * y);
    return [q * Math.cos(ps), y, q * Math.sin(ps)]; };
function sweep(fl){
    const paint = new Int16Array(NA).fill(-1), hidden = new Set();
    const cones = fl.map(F => { const l = len(F.c); return { u: mul(F.c, 1 / l), cs: Math.sqrt(Math.max(0, 1 - (F.rb / l) ** 2)) }; });
    for (let i = 0; i < NA; i++){ const d = addr(i), hits = [];
        for (let b = 0; b < fl.length; b++){ if (dot(d, cones[b].u) <= cones[b].cs) continue; const t = enter(fl[b], O, d); if (t !== null) hits.push([t, b]); }
        if (!hits.length) continue;
        hits.sort((x, y) => x[0] - y[0]); paint[i] = hits[0][1]; for (let x = 1; x < hits.length; x++) hidden.add(hits[x][1]); }
    return { paint, hidden };
}
function shares(paint, pick = () => true){ let n = 0, vh = 0, both = 0;
    for (let i = 0; i < NA; i++){ if (!pick(paint[i])) continue; const [h, v, v2] = addr(i); n++; if (v <= h){ vh++; if (v2 <= h) both++; } }
    return { n, vh: vh / n, both: both / n }; }
const ok = {};
const S1 = sweep(F1);
// P11: a body's share is its solid angle
const cnt = new Array(M).fill(0); let sky = 0; for (let i = 0; i < NA; i++){ if (S1.paint[i] < 0) sky++; else cnt[S1.paint[i]]++; }
let p11 = true, worst = 0; const rows = [];
for (let b = 0; b < M; b++){ if (cnt[b] < 200 || S1.hidden.has(b)) continue;
    const om = solidAngle(F1[b]), sh = cnt[b] / NA * Math.PI / 2, r = sh / om - 1; worst = Math.max(worst, Math.abs(r)); if (Math.abs(r) > 0.02) p11 = false;
    rows.push(`   body ${b} (d ${dist[b].toFixed(1)}): ${cnt[b]} addresses, share·π/2 ${sh.toExponential(4)} against Ω ${om.toExponential(4)} (${(100 * r).toFixed(2)}%)`); }
rows.forEach(r => console.log(r));
const addsUp = cnt.reduce((a, b) => a + b, 0) + sky === NA;
let p11k = 0; for (const k of [1e-3, 7, 1e3]){ const Sk = sweep(field(k)); let d = 0; for (let i = 0; i < NA; i++) if (Sk.paint[i] !== S1.paint[i]) d++; p11k = Math.max(p11k, d / NA);
    console.log(`   k=${k}: ${d} of ${NA} addresses painted otherwise`); }
ok.P11 = p11 && addsUp && rows.length > 0 && p11k <= 1e-4;
console.log(`P11 ${rows.length} unhidden bodies with 200 addresses or more, share·π/2 against solid angle worst ${(100 * worst).toFixed(2)}%; shares and sky add to N: ${addsUp}; k: ${p11k.toExponential(2)}`);

// the mirrored field: 20 bodies in the half of the cone where v < h, each with its mirror across v = h (x ↔ y)
const sw = p => [p[1], p[0], p[2]];
const mirror = F => ({ idx: F.idx, c: sw(F.c), rb: F.rb, inside: q => F.inside(sw(q)) });
const MF = [];
{ let sd = 5; const r2 = () => { sd |= 0; sd = sd + 0x6D2B79F5 | 0; let t = Math.imul(sd ^ sd >>> 15, 1 | sd); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  for (let i = 0; i < 20; i++) for (let tries = 0; ; tries++){ if (tries > 5000) throw new Error('mirror field ' + i);
    const z = COS30 + (1 - COS30) * r2(), a = 2 * Math.PI * r2(), q = Math.sqrt(1 - z * z);
    let u = add(mul(AX, z), add(mul(E1, q * Math.cos(a)), mul(E2, q * Math.sin(a)))); if (u[1] > u[0]) u = sw(u);
    const F = placed(i, mul(u, 4 * 2 ** (12 * r2()))), G = mirror(F);
    if (len(F.c) < F.rb + 1 || len(sub(F.c, G.c)) <= 2 * F.rb) continue;
    if (MF.every(H => len(sub(H.c, F.c)) > H.rb + F.rb && len(sub(H.c, G.c)) > H.rb + G.rb)){ MF.push(F, G); break; } } }
const SM = sweep(MF);
// P12: the addresses are the sweep's, whatever the bodies
const all = shares(S1.paint), allM = shares(SM.paint), empty = shares(new Int16Array(NA).fill(-1));
const paintedM = shares(SM.paint, b => b >= 0), painted1 = shares(S1.paint, b => b >= 0);
const near = s => Math.abs(s.vh - 0.5) <= 0.002 && Math.abs(s.both - 1 / 3) <= 0.002;
ok.P12 = near(all) && near(allM) && near(empty) && Math.abs(paintedM.vh - 0.5) <= 0.01;
console.log(`P12 all addresses: empty ${empty.vh.toFixed(5)}/${empty.both.toFixed(5)}, field ${all.vh.toFixed(5)}/${all.both.toFixed(5)}, mirrored ${allM.vh.toFixed(5)}/${allM.both.toFixed(5)} ` +
    `(½ and ⅓); painted by the mirrored field ${paintedM.n} addresses, v ≤ h ${paintedM.vh.toFixed(4)}; painted by run 3's field ${painted1.n}, v ≤ h ${painted1.vh.toFixed(4)} (reported)`);

// ── equal-angle pixels: altitude a and azimuth ψ each rounded to ε ──
function readAngle(dir, eps){ let ps = Math.atan2(dir[2], dir[0]), a = Math.atan2(dir[1], Math.hypot(dir[0], dir[2]));
    if (eps > 0){ ps = (Math.floor(ps / eps) + 0.5) * eps; a = (Math.floor(a / eps) + 0.5) * eps; }
    return { x: ps, y: a, u: eps > 0 ? [Math.cos(a) * Math.cos(ps), Math.sin(a), Math.cos(a) * Math.sin(ps)] : dir }; }
function readWith(read, eps, k = 1){
    const fl = k === 1 ? F1 : field(k), rd = RD.map(a => mul(a, k)), AB = ABlen * k;
    return fl.map((F, b) => { const out = { placed: [], truth: [], rays: 0, two: 0, cells: [] };
        PTS.forEach((u, n) => { const who = seers[b][n]; if (who.length < 2) return; out.two++;
            const p = F.surf(u), rs = who.map(i => read(nrm(sub(p, rd[i])), eps)); out.cells.push(rs.map(r => r.x + ',' + r.y).join(';'));
            if (eps > 0 && rs.every(r => r.x === rs[0].x && r.y === rs[0].y)){ out.rays++; return; }
            out.placed.push(lsq(who.map(i => mul(rd[i], 1 / AB)), rs.map(r => r.u))); out.truth.push(mul(p, 1 / AB)); });
        return out; });
}
const Ebands = R => R.map((r, b) => ({ ...errs(r, b), rays: r.rays, two: r.two, raySh: r.two ? r.rays / r.two : 0, none: !r.placed.length }));
const EA = {}, EF = {};
for (const eps of [1e-3, 1e-4]){ EA[eps] = Ebands(readWith(readAngle, eps)); EF[eps] = Ebands(readWith(readScreen, eps)); }
const ids = [...dist.keys()], order = ids.slice().sort((a, b) => dist[a] - dist[b]);
const e3 = EA[1e-3], vis = ids.filter(b => e3[b].two >= 100);
const a9 = vis.every(b => !(dist[b] < 10) || (!e3[b].none && e3[b].es < 0.1)) && vis.every(b => !(dist[b] > 100) || e3[b].none || e3[b].es > 0.1);
const b9 = vis.every(b => !(dist[b] < 100) || (!e3[b].none && e3[b].ep < 0.1)) && vis.every(b => !(dist[b] > 4000) || e3[b].none || e3[b].ep > 0.1);
const far = vis.filter(b => dist[b] > 4000), meanRay = far.reduce((a, b) => a + e3[b].raySh, 0) / far.length;
const c9 = vis.every(b => !(dist[b] < 250) || e3[b].rays === 0) && meanRay >= 0.3;
const ratios = [];
for (const eps of [1e-3, 1e-4]) for (const b of vis){ const A = EA[eps][b], F = EF[eps][b]; if (A.none || F.none || !(A.es < 1) || !(F.es < 1) || !(A.es > 0) || !(F.es > 0)) continue; ratios.push(A.es / F.es); }
const gm = Math.exp(ratios.reduce((a, r) => a + Math.log(r), 0) / ratios.length);
ok.P13 = a9 && b9 && c9 && ratios.every(r => r >= 0.4 && r <= 2.5) && gm >= 0.7 && gm <= 1.4;
console.log('   body      d   seen2   rays(ang)  e_s ang/flat 1e-3        e_p ang/flat 1e-3');
for (const b of order){ const A = e3[b], F = EF[1e-3][b], f = x => x === undefined || x === null ? '—' : x.toExponential(2);
    console.log(`   ${String(b).padStart(3)} ${dist[b].toFixed(1).padStart(8)} ${String(A.two).padStart(6)} ${A.raySh.toFixed(3).padStart(10)}  ${f(A.es).padStart(9)} ${f(F.es).padStart(9)}   ${f(A.ep).padStart(9)} ${f(F.ep).padStart(9)}`); }
console.log(`P13 equal-angle pixels: (a) ${a9}, (b) ${b9}, (c) ${c9} (mean ray share past 4,000 ${meanRay.toFixed(3)}, ${far.length} bodies); ` +
    `e_s angle/flat over ${ratios.length}: ${Math.min(...ratios).toFixed(3)} … ${Math.max(...ratios).toFixed(3)}, geometric mean ${gm.toFixed(3)}`);
// P14: no size in an address
const R1 = readWith(readAngle, 1e-3); let changed = 0, total = 0;
for (const k of [1e-3, 7, 1e3]){ const Rk = readWith(readAngle, 1e-3, k); Rk.forEach((r, b) => r.cells.forEach((c, n) => { total++; if (c !== R1[b].cells[n]) changed++; })); }
const R0 = readWith(readAngle, 0); let e0 = 0; R0.forEach(r => r.placed.forEach((q, n) => { e0 = Math.max(e0, len(sub(q, r.truth[n])) / len(r.truth[n])); }));
ok.P14 = changed / total <= 1e-4 && e0 <= 1e-9;
console.log(`P14 rounded readings changed by k: ${changed} of ${total}; at ε = 0 every seen point in |AB| to ${e0.toExponential(2)}`);
for (const k of ['P11', 'P12', 'P13', 'P14']) console.log(k, ok[k] ? 'not killed' : 'KILLED');
