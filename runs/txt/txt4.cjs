// TXT run 4 (plans/txt-plan.md): four polygons with every corner rounded to radius r, in every format at τ = 5,
// and each library figure's tightest radius of curvature (for U5).
//   DRAW_DIR=<draw dir> node runs/txt/txt4.cjs <forms3.json> <out.json>
'use strict';
const fs = require('fs');
const L = require('./txt_lib.cjs');
const A = require('./txt_fit.cjs');
const B = require('./txt3_fit.cjs');
const [forms3In, out] = process.argv.slice(2);

const POLYS = {
    square: [[0, 0], [1, 0], [1, 1], [0, 1]],
    triangle: [[0, 0], [1, 0], [0.5, Math.sqrt(3) / 2]],
    star5: Array.from({ length: 10 }, (_, k) => {
        const a = (90 + 36 * k) * Math.PI / 180, R = k % 2 ? 0.4 : 1;
        return [R * Math.cos(a), R * Math.sin(a)];
    }),
    arrow: [[0, 0.35], [0.6, 0.35], [0.6, 0.1], [1, 0.5], [0.6, 0.9], [0.6, 0.65], [0, 0.65]]
};
const FRACS = [0.003, 0.01, 0.03, 0.1, 0.3];

function toBox(V) {
    const xs = V.map(v => v[0]), ys = V.map(v => v[1]);
    const x0 = Math.min(...xs), y0 = Math.min(...ys), s = 1000 / Math.max(Math.max(...xs) - x0, Math.max(...ys) - y0);
    return V.map(v => [(v[0] - x0) * s, (v[1] - y0) * s]);
}
function turns(V) {
    const n = V.length;
    return V.map((v, i) => {
        const p = V[(i - 1 + n) % n], q = V[(i + 1) % n];
        const u = [v[0] - p[0], v[1] - p[1]], w = [q[0] - v[0], q[1] - v[1]];
        return Math.atan2(u[0] * w[1] - u[1] * w[0], u[0] * w[0] + u[1] * w[1]);
    });
}
function rMax(V) {
    const n = V.length, d = turns(V);
    let m = Infinity;
    for (let i = 0; i < n; i++) {
        const j = (i + 1) % n, e = Math.hypot(V[j][0] - V[i][0], V[j][1] - V[i][1]);
        m = Math.min(m, e / (Math.tan(Math.abs(d[i]) / 2) + Math.tan(Math.abs(d[j]) / 2)));
    }
    return m;
}
function rounded(V, r) {
    const n = V.length, d = turns(V), pts = [];
    for (let i = 0; i < n; i++) {
        const p = V[(i - 1 + n) % n], v = V[i], q = V[(i + 1) % n];
        const lu = Math.hypot(v[0] - p[0], v[1] - p[1]), lw = Math.hypot(q[0] - v[0], q[1] - v[1]);
        const u = [(v[0] - p[0]) / lu, (v[1] - p[1]) / lu], w = [(q[0] - v[0]) / lw, (q[1] - v[1]) / lw];
        const t = r * Math.tan(Math.abs(d[i]) / 2), sg = Math.sign(d[i]);
        const a = [v[0] - t * u[0], v[1] - t * u[1]];
        const nrm = [-u[1] * sg, u[0] * sg], c = [a[0] + r * nrm[0], a[1] + r * nrm[1]];
        const a0 = Math.atan2(a[1] - c[1], a[0] - c[0]);
        for (let k = 0; k <= 128; k++) {
            const th = a0 + sg * d[i] * sg * k / 128;
            pts.push([c[0] + r * Math.cos(th), c[1] + r * Math.sin(th)]);
        }
        // the straight edge to the next arc is the chord from this arc's end to its start (walk() runs it)
    }
    return pts;
}
const lengthOf = P => P.reduce((s, p, i) => s + Math.hypot(P[(i + 1) % P.length][0] - p[0], P[(i + 1) % P.length][1] - p[1]), 0);

const res = { polys: [], library: [] };
for (const [name, V0] of Object.entries(POLYS)) {
    const V = toBox(V0), rm = rMax(V);
    const used = [];
    for (const f of FRACS) {
        const r = Math.min(f * 1000, rm * 0.999);
        if (used.some(u => Math.abs(u - r) < 1e-9)) continue;
        used.push(r);
        const raw = rounded(V, r);
        const xs = raw.map(p => p[0]), ys = raw.map(p => p[1]);
        const s = 1000 / Math.max(Math.max(...xs) - Math.min(...xs), Math.max(...ys) - Math.min(...ys));
        const P = A.prep(raw), cs = A.corners(P), Lp = lengthOf(P), rAct = r * s;
        const t0 = Date.now();
        const tv = A.fitTvf(P, 5, 0), sv = A.fitSvg(P, cs, 5, 0);
        const fd = B.fitFD(P), rad = B.fitRAD(P), pl = B.fitPolys(P, cs);
        const texts = { tvf: tv.N ? L.tvfText(tv.lx, tv.ly, 0) : null, svgabs: sv.abs || null, svgrel: sv.rel || null,
            fd: fd ? fd.text : null, rad: rad && rad.text ? rad.text : null,
            poly: pl.poly ? pl.poly.text : null, step: pl.step ? pl.step.text : null, turtle: pl.turtle ? pl.turtle.text : null };
        const counts = { tvf: tv.N, svg: sv.segs, fd: fd ? fd.count : null, rad: rad && rad.count ? rad.count : null,
            poly: pl.poly ? pl.poly.count : null, turtle: pl.turtle ? pl.turtle.count : null };
        res.polys.push({ name, frac: f, capped: f * 1000 > rm * 0.999, r: rAct, L: Lp, corners: cs.length,
            radApplies: !(rad && rad.applies === false), counts, texts });
        process.stderr.write(`${name} r ${rAct.toFixed(1)} corners ${cs.length} ${JSON.stringify(counts)} ${((Date.now() - t0) / 1000).toFixed(1)} s\n`);
    }
}
// U5: each library figure's tightest radius of curvature, circles through points 5 apart of its 2,048
for (const f of JSON.parse(fs.readFileSync(forms3In, 'utf8'))) {
    const P = f.P, n = P.length;
    let rmin = Infinity;
    for (let i = 0; i < n; i++) {
        const a = P[(i - 5 + n) % n], b = P[i], c = P[(i + 5) % n];
        const ab = Math.hypot(b[0] - a[0], b[1] - a[1]), bc = Math.hypot(c[0] - b[0], c[1] - b[1]), ca = Math.hypot(a[0] - c[0], a[1] - c[1]);
        const cr = Math.abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]));
        const R = cr > 1e-12 ? ab * bc * ca / (2 * cr) : Infinity;
        if (R < rmin) rmin = R;
    }
    res.library.push({ key: f.key, corners: f.corners, L: lengthOf(P), rmin, texts: { tvf: f.texts.tvf, svgabs: f.texts.svgabs, svgrel: f.texts.svgrel } });
}
fs.writeFileSync(out, JSON.stringify(res));
