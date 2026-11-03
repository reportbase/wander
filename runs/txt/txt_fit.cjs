// TXT step 1: each library figure as TVF text and SVG path data at τ = 5 and τ = 1 (plans/txt-plan.md).
//   node runs/txt/txt_fit.cjs <draw dir> <figs-raw.json> <forms.json>
'use strict';
const fs = require('fs');
const L = require('./txt_lib.cjs');
const [drawDir, figsIn, out, shard] = process.argv.slice(2);
const [sk, sn] = (shard || '1/1').split('/').map(Number);
const { tvf, fitCubics } = L.loadDraw(drawDir);
const figs = JSON.parse(fs.readFileSync(figsIn, 'utf8')).filter((_, i) => i % sn === sk - 1);
const NP = 2048, TAUS = [[5, 0], [1, 1]];

function prep(raw) {
    let P = L.walk(raw, Array.from({ length: NP }, (_, i) => i / NP));
    const xs = P.map(p => p[0]), ys = P.map(p => p[1]);
    const x0 = Math.min(...xs), y0 = Math.min(...ys), s = 1000 / Math.max(Math.max(...xs) - x0, Math.max(...ys) - y0);
    return P.map(p => [(p[0] - x0) * s, (p[1] - y0) * s]);
}
// a corner: the outline turns by more than 30° within 1% of its length (±10 samples), local maxima 20 apart.
function corners(P) {
    const n = P.length, w = 10, ang = new Float64Array(n);
    for (let i = 0; i < n; i++) {
        const a = P[(i - w + n) % n], b = P[i], c = P[(i + w) % n];
        const u = [b[0] - a[0], b[1] - a[1]], v = [c[0] - b[0], c[1] - b[1]];
        ang[i] = Math.abs(Math.atan2(u[0] * v[1] - u[1] * v[0], u[0] * v[0] + u[1] * v[1]));
    }
    const out = [];
    for (let i = 0; i < n; i++) {
        if (ang[i] <= Math.PI / 6) continue;
        let peak = true;
        for (let d = -20; d <= 20 && peak; d++) if (d && (ang[(i + d + n) % n] > ang[i] || (ang[(i + d + n) % n] === ang[i] && d < 0))) peak = false;
        if (peak) out.push(i);
    }
    return out;
}
function tvfAt(P, N, dp) {
    const pts = L.walk(P, Array.from({ length: N }, (_, k) => (k + 0.5) / N));
    const lx = pts.map(p => L.rnd(p[0], dp)), ly = pts.map(p => L.rnd(p[1], dp));
    const rx = tvf.reconstruct(lx, 4096), ry = tvf.reconstruct(ly, 4096);
    const R = Array.from(rx, (v, i) => [v, ry[i]]);
    return { lx, ly, err: L.hausdorff(P, R) };
}
function fitTvf(P, tau, dp) {
    let lo = 2, hi = 4, r = null;
    while (hi <= 1024 && (r = tvfAt(P, hi, dp)).err > tau) { lo = hi; hi *= 2; }
    if (hi > 1024) return { N: null };
    let best = { N: hi, ...r };
    while (hi - lo > 2) {                  // bisection over even N, assuming the error falls with N
        const mid = 2 * Math.round((lo + hi) / 4);
        if (mid <= lo || mid >= hi) break;
        const m = tvfAt(P, mid, dp);
        if (m.err <= tau) { hi = mid; best = { N: mid, ...m }; } else lo = mid;
    }
    return best;
}
function fitSvg(P, cs, tau, dp) {
    // runs between corners (rotated so the first corner is at 0), each fitted by draw's _fitCubics
    const n = P.length, o = cs.length ? cs[0] : 0;
    const Q = P.slice(o).concat(P.slice(0, o)).map(p => ({ x: p[0], y: p[1] }));
    const cut = cs.length ? cs.map(c => (c - o + n) % n).sort((a, b) => a - b) : [0];
    for (let tol = tau * 0.7, k = 0; k < 14; k++, tol *= 0.7) {
        let segs = [];
        for (let j = 0; j < cut.length; j++) {
            const a = cut[j], b = j + 1 < cut.length ? cut[j + 1] : n;
            const run = Q.slice(a, b + 1 > n ? n : b + 1);
            if (b === n) run.push(Q[0]);
            segs = segs.concat(fitCubics(run, tol));
        }
        const R = segs.map(c => c.map(p => ({ x: L.rnd(p.x, dp), y: L.rnd(p.y, dp) })));
        for (let j = 1; j < R.length; j++) R[j][0] = R[j - 1][3];   // joined exactly as written
        const abs = L.svgAbs(R, dp), rel = L.svgRel(R, dp);
        const ea = L.hausdorff(P, L.readSvg(abs)), er = L.hausdorff(P, L.readSvg(rel));
        if (ea <= tau && er <= tau) return { segs: R.length, abs, rel, errAbs: ea, errRel: er, tol };
    }
    return { segs: null };
}

const res = [];
for (const f of figs) {
    const P = prep(f.pts), cs = corners(P);
    const row = { key: f.key, corners: cs.length, P: P.map(p => [L.rnd(p[0], 2), L.rnd(p[1], 2)]), forms: {} };
    for (const [tau, dp] of TAUS) {
        const t = fitTvf(P, tau, dp), s = fitSvg(P, cs, tau, dp);
        row.forms[tau] = {
            N: t.N, tvf: t.N ? L.tvfText(t.lx, t.ly, dp) : null, errTvf: t.err,
            segs: s.segs, abs: s.abs || null, rel: s.rel || null, errAbs: s.errAbs, errRel: s.errRel
        };
    }
    res.push(row);
    process.stderr.write(`${f.key}: corners ${cs.length}; τ5 N ${row.forms[5].N} segs ${row.forms[5].segs}; τ1 N ${row.forms[1].N} segs ${row.forms[1].segs}\n`);
}
fs.writeFileSync(out, JSON.stringify(res));
