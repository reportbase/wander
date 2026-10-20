// Post hoc for MON run 2 (plans/mon-plan.md): the same pass with the moon's relief taken off (R = ½ everywhere), M2 and M4
// only, to see whether the relief is what moved τ and the distance. Made from mon.mjs. Run: node runs/mon/mon2-smooth.mjs
// MON (plans/mon-plan.md): one moon moving across the sky. The inscribed sweep covers the whole wedge every tick and
// detects which addresses the moon meets (ratios); the central sweep paints its face, the radius arriving along fixed
// directions from its centre (amounts). bodyOf is games.html's, as recover.html copies it. Run: node runs/mon/mon.mjs
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
const W3 = [];   // post hoc: no relief
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

// ── the inscribed sweep: 4096 × 4096 addresses even in azimuth and height; only cells in the moon's bounding cone tested ──
const NG = 4096, N = NG * NG;
const cell = (i, j) => { const ps = (i + 0.5) / NG * Math.PI / 2, y = (j + 0.5) / NG, q = Math.sqrt(1 - y * y); return [q * Math.cos(ps), y, q * Math.sin(ps)]; };
function sweep(F){
    const dc = len(F.c), u = mul(F.c, 1 / dc), al = Math.asin(F.rb / dc), cs = Math.cos(al);
    const ac = Math.asin(u[1]), ps = Math.atan2(u[2], u[0]), amax = Math.min(Math.PI / 2, ac + al) , dps = al / Math.cos(amax) + 2 * Math.PI / 2 / NG;
    const j0 = Math.max(0, Math.floor(Math.sin(Math.max(0, ac - al)) * NG) - 1), j1 = Math.min(NG - 1, Math.ceil(Math.sin(amax) * NG) + 1);
    const i0 = Math.max(0, Math.floor((ps - dps) / (Math.PI / 2) * NG) - 1), i1 = Math.min(NG - 1, Math.ceil((ps + dps) / (Math.PI / 2) * NG) + 1);
    const det = []; let tested = 0, sum = [0, 0, 0];
    for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++){ const d = cell(i, j); if (dot(d, u) <= cs) continue; tested++;
        if (enter(F, O, d) !== null){ det.push(j * NG + i); sum = add(sum, d); } }
    return { det, tested, share: det.length / N * Math.PI / 2, c: nrm(sum) };
}
const ok = {};
const S1 = TICKS.map(t => sweep(moon(centre(t))));
console.log(`moon: body 3, stretch 1, mean radius ${RBAR.toFixed(4)}; ${TICKS.length} ticks, d ${len(centre(0)).toFixed(1)} → ${len(centre(TICKS.at(-1))).toFixed(1)}; ` +
    `${S1[0].det.length} → ${S1.at(-1).det.length} addresses met`);
// M2
let wt = 0, ww = 0, wb = 0; const rows = [];
for (let n = 1; n < TICKS.length - 1; n++){ const t = TICKS[n], C = centre(t), d = len(C);
    const tauT = d / -(dot(C, VEL) / d), omT = len(cross(C, VEL)) / (d * d), betaT = Math.acos(dot(VEL, mul(C, -1 / d)));
    const tau = 2 * S1[n].share / ((S1[n + 1].share - S1[n - 1].share) / 2);
    const om = Math.acos(Math.min(1, dot(S1[n - 1].c, S1[n + 1].c))) / 2, beta = Math.atan(om * tau);
    wt = Math.max(wt, Math.abs(tau / tauT - 1)); ww = Math.max(ww, Math.abs(om / omT - 1)); wb = Math.max(wb, Math.abs(beta - betaT) / RAD);
    if (n % 4 === 1 || n === TICKS.length - 2) rows.push(`   t=${t}: d ${d.toFixed(2)}, τ ${tau.toFixed(3)} (true ${tauT.toFixed(3)}), ω ${om.toExponential(4)} (${omT.toExponential(4)}), β ${(beta / RAD).toFixed(2)}° (${(betaT / RAD).toFixed(2)}°)`); }
rows.forEach(r => console.log(r));
ok.M2 = wt <= 0.03 && ww <= 0.01 && wb <= 2;
console.log(`M2 from the detections alone: τ worst ${(100 * wt).toFixed(2)}%, ω worst ${(100 * ww).toFixed(3)}%, β worst ${wb.toFixed(3)}°`);
// M4: one amount carried in
let wd = 0, wv = 0;
TICKS.forEach((t, n) => { const d = len(centre(t)), dE = RBAR * Math.sqrt(Math.PI / S1[n].share); wd = Math.max(wd, Math.abs(dE / d - 1));
    if (n > 0 && n < TICKS.length - 1){ const tau = 2 * S1[n].share / ((S1[n + 1].share - S1[n - 1].share) / 2), om = Math.acos(Math.min(1, dot(S1[n - 1].c, S1[n + 1].c))) / 2;
        wv = Math.max(wv, Math.abs(dE * Math.sqrt(om * om + 1 / (tau * tau)) - 1)); } });
ok.M4 = wd <= 0.02 && wv <= 0.03;
console.log(`M4 with R̄ carried in: distance worst ${(100 * wd).toFixed(2)}%, speed worst ${(100 * wv).toFixed(2)}%`);
for (const k of ['M2', 'M4']) console.log(k, ok[k] ? 'not killed' : 'KILLED');
