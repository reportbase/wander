// Post hoc for RSH run 3 (P7′(d)): each body alone seen from O, with its relief and with it taken off (node rsh/rsh3-p7d.mjs [flat]).
// Made from rsh2.mjs above its census.
// RSH run 2 (plans/rsh-plan.md, "Run 2: many bodies at once"): a field of 40 Levels bodies around three readers.
// One standpoint's census painted by the first body each direction meets (P7, P8); three readers, directions only,
// on a flat screen of pixels ε wide, placing every seen point by its rays (P9), and with ε = 0 exactly (P10).
// Run 3 (the code fixed, P7′–P10′): the moved body, the visibility, the least squares and P10's index; see the plan.
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


const O=[0,0,0], ord=[...dist.keys()].sort((a,b)=>dist[a]-dist[b]);
const flat = process.argv[2] === 'flat';
for (const b of ord){ let F=F1[b]; if (flat){ const B=bodyOf(b); F={...F}; const s=F.s, c=F.c; F.R=u=>0.5; F.surf=u=>[c[0]+s[0]*0.5*u[0],c[1]+s[1]*0.5*u[1],c[2]+s[2]*0.5*u[2]]; F.hit=d=>F.surf(nrm([d[0]/s[0],d[1]/s[1],d[2]/s[2]])); F.inside=q=>{const w=sub(q,c),l=len(w); return l<len(sub(F.hit(w),c))*(1-1e-12);}; F.rb=0.5*Math.max(...s);}
  let n=0; for (const u of PTS) if (clear([F], O, F.surf(u))) n++; const mr = meanR[b];
  console.log(b, dist[b].toFixed(1), (n/1024).toFixed(3), ((1-mr/dist[b])/2).toFixed(3)); }
