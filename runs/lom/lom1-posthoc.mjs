// Post hoc for LOM run 1: the same repeats (same seed), with 1/median(r̂), the share of r̂ exactly 0, and the rate the
// five-tick slope gives for a straight approach (the t³ term). Made from lom.mjs. Run: node runs/lom/lom1-posthoc.mjs
// LOM (plans/lom-plan.md): looming read as a ratio. A smooth sphere (radius ½) approaching home, seen on the inscribed
// sweep's Lambert grid of the whole wedge (2048 × 2048); its share's rate r̂ (half the five-tick slope of ln s) and
// τ̂ = 1/r̂ over many independent repeats; the only noise the cells'. Run: node runs/lom/lom.mjs
const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]], mul = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
const dot = (a, b) => a[0] * b[0] + a[1] * b[1] + a[2] * b[2], len = a => Math.hypot(a[0], a[1], a[2]), nrm = a => mul(a, 1 / len(a));
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
let seed = 11; const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const NG = 2048, N = NG * NG, CELL = Math.PI / 2 / NG, R = 0.5, D0 = 32, AX = nrm([1, 1, 1]);
const cellDir = (i, j) => { const ps = (i + 0.5) * CELL, y = (j + 0.5) / NG, q = Math.sqrt(1 - y * y); return [q * Math.cos(ps), y, q * Math.sin(ps)]; };
// the share of the sweep a sphere of radius R at distance d in direction u takes (cells whose middle lies in its cap)
function share(u, d){ const al = Math.asin(R / d), cs = Math.cos(al), ac = Math.asin(u[1]), ps = Math.atan2(u[2], u[0]), amax = ac + al;
    const j0 = Math.max(0, Math.floor(Math.sin(ac - al) * NG) - 1), j1 = Math.min(NG - 1, Math.ceil(Math.sin(amax) * NG) + 1);
    const dps = al / Math.cos(amax) + CELL, i0 = Math.max(0, Math.floor((ps - dps) / CELL) - 1), i1 = Math.min(NG - 1, Math.ceil((ps + dps) / CELL) + 1);
    let n = 0; for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++) if (dot(cellDir(i, j), u) > cs) n++; return n / N * Math.PI / 2; }
function repeat(tau){
    // a start within 5° of (1, 1, 1), moving 5 cells a tick across the line of sight in a random direction
    const z = 1 - (1 - Math.cos(5 * Math.PI / 180)) * rnd(), a = 2 * Math.PI * rnd(), e1 = nrm(cross(AX, [0, 1, 0])), e2 = cross(AX, e1), q = Math.sqrt(1 - z * z);
    const u0 = nrm(add(mul(AX, z), add(mul(e1, q * Math.cos(a)), mul(e2, q * Math.sin(a))))), b = 2 * Math.PI * rnd();
    const w = nrm(cross(u0, add(mul(e1, Math.cos(b)), mul(e2, Math.sin(b))))), om = 5 * CELL;
    let sl = 0; for (let t = -2; t <= 2; t++){ const u = nrm(add(mul(u0, Math.cos(om * t)), mul(w, Math.sin(om * t)))), d = D0 - (D0 / tau) * t; sl += t * Math.log(share(u, d)); }
    return sl / 10 / 2; }   // r̂: half the slope of ln s (s ∝ d⁻², so the slope is 2/τ)
const median = x => { const s = [...x].sort((a, b) => a - b); return s[(s.length - 1) >> 1]; };   // odd counts used
const mean = x => x.reduce((a, b) => a + b, 0) / x.length, sd = x => { const m = mean(x); return Math.sqrt(x.reduce((a, b) => a + (b - m) ** 2, 0) / (x.length - 1)); };
const ok = { L1: true, L2: true, L3: true, L4: true }; const rows = []; const sds = [];
let reachedL3 = false, testedL2 = false;
for (const tau of [10, 30, 100, 300, 1000, 3000, 10000]){
    const n = tau === 1000 || tau === 3000 ? 40001 : 4001, r = [];
    for (let k = 0; k < n; k++) r.push(repeat(tau));
    { const zero = r.filter(x => x === 0).length / n, expect = (1 / tau) * (1 + (34 / 10) / (3 * tau * tau)), flipMed = 1 / median(r);
      console.log(`   τ ${String(tau).padStart(5)}: r̂ = 0 exactly in ${(100 * zero).toFixed(2)}%; 1/median(r̂) ${flipMed.toFixed(2)} (${(100 * (flipMed / tau - 1)).toFixed(2)}%); r̂ mean against the slope's own expectation (1/τ)(1 + 34/(30τ²)): ${((mean(r) - expect) / (sd(r) / Math.sqrt(n))).toFixed(2)} se`); continue; }
    const T = r.map(x => 1 / x), cv = sd(r) * tau; sds.push(sd(r));
    const medId = Math.abs(median(T) * median(r) - 1), meanGap = Math.abs(mean(T) * mean(r) - 1);
    if (medId > 1e-12) ok.L1 = false; if (cv >= 0.05 && !(meanGap > 1e-4)) ok.L1 = false;
    const mBias = mean(T) / tau - 1, mdBias = median(T) / tau - 1, wrong = T.filter(x => x < 0).length / n;
    if (cv <= 0.3){ testedL2 = true; const want = cv * cv;
        if (want < 0.01 ? Math.abs(mBias - want) > 0.01 : !(mBias >= want / 1.5 && mBias <= want * 1.5)) ok.L2 = false; if (!(Math.abs(mdBias) < Math.abs(mBias))) ok.L2 = false; }
    let settle = '';
    if (cv >= 1){ reachedL3 = true; if (wrong < 0.15 || Math.abs(mdBias) > 0.25) ok.L3 = false;
        if (n > 4001){ const m1 = mean(T.slice(0, 4001)), m2 = mean(T), se = sd(T) / Math.sqrt(n); const unsettled = Math.abs(m1 - m2) > 3 * se || m1 < 0 || m2 < 0; if (!unsettled) ok.L3 = false;
            settle = `, mean over 4,001 ${m1.toFixed(0)} and over ${n} ${m2.toFixed(0)} (se ${se.toFixed(0)})`; } }
    const rBias = (mean(r) - 1 / tau) / (sd(r) / Math.sqrt(n)); if (Math.abs(rBias) > 3) ok.L4 = false;
    rows.push(`   τ ${String(tau).padStart(5)}: CV ${cv.toFixed(3)}, r̂ mean off ${rBias.toFixed(2)} se, sd ${sd(r).toExponential(3)}; τ̂ mean ${mean(T).toFixed(2)} (${(100 * mBias).toFixed(2)}%; CV² ${(100 * cv * cv).toFixed(2)}%), median ${median(T).toFixed(2)} (${(100 * mdBias).toFixed(2)}%), wrong sign ${(100 * wrong).toFixed(1)}%${settle}; median·median ${medId.toExponential(1)}, mean·mean − 1 ${meanGap.toExponential(2)}`);
    console.log(rows.at(-1));
}
