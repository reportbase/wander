// TXT run 3 (plans/txt-plan.md): the readers' and writers' formats, each written and read back (leniently).
'use strict';
const L = require('./txt_lib.cjs');
const NUM = /^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/;
const lettered = ln => /[A-Za-z]/.test(ln);
// the numeric lines of a text, header lines (any letter) left out
const numRows = text => text.split('\n').filter(ln => !lettered(ln))
    .map(ln => ln.trim().split(/\s+/).filter(w => NUM.test(w)).map(Number)).filter(r => r.length);

// a corner: the outline turns by more than 30° within 1% of its length (±10 samples), local maxima 20 apart (run 2's rule)
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

// ── FD: Fourier descriptors c₋K … c_K of the outline walked by arc length ──
function fdCoeffs(P, K) {
    const n = P.length, re = [], im = [];
    for (let k = -K; k <= K; k++) {
        let a = 0, b = 0;
        for (let j = 0; j < n; j++) {
            const t = -2 * Math.PI * k * j / n, c = Math.cos(t), s = Math.sin(t);
            a += P[j][0] * c - P[j][1] * s; b += P[j][0] * s + P[j][1] * c;
        }
        re.push(a / n); im.push(b / n);
    }
    return { re, im };
}
const fdText = (re, im, dp) => 'FD ' + (re.length - 1) / 2 + '\n' + re.map(v => L.fmt(v, dp)).join(' ') + '\n' + im.map(v => L.fmt(v, dp)).join(' ');
function fdRead(text, M = 1024) {
    const rows = numRows(text).filter(r => r.length >= 3);
    if (rows.length < 2) return null;
    const [re, im] = rows, Kr = (re.length - 1) >> 1, Ki = (im.length - 1) >> 1, K = Math.max(Kr, Ki);
    const at = (row, Kx, k) => { const i = k + Kx; return i >= 0 && i < row.length ? row[i] : 0; };
    const out = [];
    for (let j = 0; j < M; j++) {
        let x = 0, y = 0;
        for (let k = -K; k <= K; k++) {
            const a = at(re, Kr, k), b = at(im, Ki, k), t = 2 * Math.PI * k * j / M, c = Math.cos(t), s = Math.sin(t);
            x += a * c - b * s; y += a * s + b * c;
        }
        out.push([x, y]);
    }
    return out;
}

// ── RAD: the radius from the area centroid at N even angles, rebuilt by draw's kernel ──
function centroid(P) {
    let A = 0, cx = 0, cy = 0;
    for (let i = 0; i < P.length; i++) {
        const p = P[i], q = P[(i + 1) % P.length], c = p[0] * q[1] - q[0] * p[1];
        A += c; cx += (p[0] + q[0]) * c; cy += (p[1] + q[1]) * c;
    }
    return [cx / (3 * A), cy / (3 * A)];
}
// the radius at angle θ if every ray meets the outline once (the angle about c turns monotonically), else null
function radialOf(P, c) {
    const n = P.length, th = P.map(p => Math.atan2(p[1] - c[1], p[0] - c[0]));
    let un = [th[0]], sgn = 0;
    for (let i = 1; i <= n; i++) {
        let d = th[i % n] - th[i - 1];
        while (d > Math.PI) d -= 2 * Math.PI;
        while (d < -Math.PI) d += 2 * Math.PI;
        if (d !== 0) { const s = Math.sign(d); if (sgn && s !== sgn) return null; sgn = s; }
        un.push(un[i - 1] + d);
    }
    if (Math.abs(Math.abs(un[n] - un[0]) - 2 * Math.PI) > 1e-6) return null;
    return theta => {           // walk the loop in the direction of increasing angle
        let t = ((theta - un[0]) * sgn) % (2 * Math.PI); if (t < 0) t += 2 * Math.PI;
        let lo = 0, hi = n;
        while (hi - lo > 1) { const m = (lo + hi) >> 1; if ((un[m] - un[0]) * sgn <= t) lo = m; else hi = m; }
        const a = (un[lo] - un[0]) * sgn, b = (un[lo + 1] - un[0]) * sgn, f = b > a ? (t - a) / (b - a) : 0;
        const p = P[lo % n], q = P[(lo + 1) % n];
        return Math.hypot(p[0] + f * (q[0] - p[0]) - c[0], p[1] + f * (q[1] - p[1]) - c[1]);
    };
}
const radText = (c, r, dp) => 'RAD ' + r.length + '\n' + L.fmt(c[0], dp) + ' ' + L.fmt(c[1], dp) + '\n' + r.map(v => L.fmt(v, dp)).join(' ');
function radRead(text, tvf, M = 1024) {
    const rows = numRows(text);
    const c = rows.find(r => r.length === 2), r = rows.find(r => r.length >= 3);
    if (!c || !r) return null;
    const R = tvf.reconstruct(r, M), out = [];
    for (let i = 0; i < M; i++) { const t = 2 * Math.PI * i / M; out.push([c[0] + R[i] * Math.cos(t), c[1] + R[i] * Math.sin(t)]); }
    return out;
}

// ── POLY, STEP, TURTLE: the outline's vertices (Douglas–Peucker), written three ways ──
function dp(P, tol, start) {
    const n = P.length, Q = P.slice(start).concat(P.slice(0, start)); Q.push(Q[0]);
    const keep = new Uint8Array(Q.length); keep[0] = keep[Q.length - 1] = 1;
    const st = [[0, Q.length - 1]];
    while (st.length) {
        const [a, b] = st.pop();
        let w = -1, at = -1;
        const ax = Q[a][0], ay = Q[a][1], dx = Q[b][0] - ax, dy = Q[b][1] - ay, l = Math.hypot(dx, dy);
        for (let i = a + 1; i < b; i++) {
            const d = l > 0 ? Math.abs((Q[i][0] - ax) * dy - (Q[i][1] - ay) * dx) / l : Math.hypot(Q[i][0] - ax, Q[i][1] - ay);
            if (d > w) { w = d; at = i; }
        }
        if (w > tol) { keep[at] = 1; st.push([a, at], [at, b]); }
    }
    const V = [];
    for (let i = 0; i < Q.length - 1; i++) if (keep[i]) V.push(Q[i]);
    return V;
}
const polyText = (V, dpl) => 'POLY ' + V.length + '\n' + V.map(v => L.fmt(v[0], dpl) + ' ' + L.fmt(v[1], dpl)).join(' ');
function stepText(V, dpl) {
    const R = V.map(v => [L.rnd(v[0], dpl), L.rnd(v[1], dpl)]);
    const s = [L.fmt(R[0][0], dpl) + ' ' + L.fmt(R[0][1], dpl)];
    for (let i = 1; i < R.length; i++) s.push(L.fmt(L.rnd(R[i][0] - R[i - 1][0], dpl), dpl) + ' ' + L.fmt(L.rnd(R[i][1] - R[i - 1][1], dpl), dpl));
    return 'STEP ' + R.length + '\n' + s.join(' ');
}
function turtleText(V, pd, pa) {
    // start, heading (degrees); then forward d, turn a, for each edge (the last edge closes the loop)
    const R = V.map(v => [L.rnd(v[0], pd), L.rnd(v[1], pd)]), n = R.length;
    const head = i => Math.atan2(R[(i + 1) % n][1] - R[i][1], R[(i + 1) % n][0] - R[i][0]) * 180 / Math.PI;
    let h = L.rnd(head(0), pa), x = R[0][0], y = R[0][1];
    const out = [];
    for (let i = 0; i < n; i++) {
        // write what lands nearest the true next vertex from where the turtle actually is (its own drift kept small)
        const tx = R[(i + 1) % n][0], ty = R[(i + 1) % n][1];
        const d = L.rnd(Math.hypot(tx - x, ty - y), pd);
        const want = Math.atan2(ty - y, tx - x) * 180 / Math.PI;
        let turn = want - h; while (turn > 180) turn -= 360; while (turn < -180) turn += 360;
        turn = L.rnd(turn, pa);
        h += turn;
        out.push(L.fmt(turn, pa) + ' ' + L.fmt(d, pd));
        x += d * Math.cos(h * Math.PI / 180); y += d * Math.sin(h * Math.PI / 180);
    }
    return 'TURTLE ' + n + '\n' + L.fmt(R[0][0], pd) + ' ' + L.fmt(R[0][1], pd) + ' ' + L.fmt(L.rnd(head(0), pa), pa) + '\n' + out.join(' ');
}
function pairsOf(nums) { const o = []; for (let i = 0; i + 1 < nums.length; i += 2) o.push([nums[i], nums[i + 1]]); return o; }
function polyRead(text) { const v = pairsOf(numRows(text).flat()); return v.length >= 2 ? v : null; }
function stepRead(text) {
    const v = pairsOf(numRows(text).flat());
    if (v.length < 2) return null;
    const o = [v[0]];
    for (let i = 1; i < v.length; i++) o.push([o[i - 1][0] + v[i][0], o[i - 1][1] + v[i][1]]);
    return o;
}
function turtleRead(text) {
    const nums = numRows(text).flat();
    if (nums.length < 5) return null;
    let x = nums[0], y = nums[1], h = nums[2];
    const o = [[x, y]];
    for (const [a, d] of pairsOf(nums.slice(3))) {
        h += a; x += d * Math.cos(h * Math.PI / 180); y += d * Math.sin(h * Math.PI / 180); o.push([x, y]);
    }
    return o;
}

// ── HYB: corners as places, each run's departure from its chord at n even places (sine interpolation) ──
function sineEval(d, s) {            // samples d_k at s_k = (k + ½)/n; the band-limited odd extension at s
    const n = d.length;
    if (!n) return 0;
    let v = 0;
    for (let m = 1; m <= n; m++) {
        let b = 0;
        for (let k = 0; k < n; k++) b += d[k] * Math.sin(m * Math.PI * (k + 0.5) / n);
        b *= 2 / n; if (m === n) b /= 2;
        v += b * Math.sin(m * Math.PI * s);
    }
    return v;
}
function hybRun(A, B, dev, S = 64) {
    const n = dev.length, out = [];
    const S2 = Math.max(S, 8 * n);
    // precompute the sine coefficients once
    const bx = [], by = [];
    for (let m = 1; m <= n; m++) {
        let a = 0, c = 0;
        for (let k = 0; k < n; k++) { const w = Math.sin(m * Math.PI * (k + 0.5) / n); a += dev[k][0] * w; c += dev[k][1] * w; }
        a *= 2 / n; c *= 2 / n; if (m === n) { a /= 2; c /= 2; }
        bx.push(a); by.push(c);
    }
    for (let i = 0; i < S2; i++) {
        const s = i / S2;
        let dx = 0, dy = 0;
        for (let m = 1; m <= n; m++) { const w = Math.sin(m * Math.PI * s); dx += bx[m - 1] * w; dy += by[m - 1] * w; }
        out.push([A[0] + s * (B[0] - A[0]) + dx, A[1] + s * (B[1] - A[1]) + dy]);
    }
    return out;
}
function hybText(runs, dpl) {
    return 'HYB ' + runs.length + '\n' + runs.map(r => [r.A[0], r.A[1]].concat(r.dev.flat()).map(v => L.fmt(v, dpl)).join(' ')).join('\n');
}
function hybRead(text, tvf) {
    if (/^\s*TVF/.test(text)) return L.readTvf(text, false, tvf, 1024);
    const rows = numRows(text).filter(r => r.length >= 2);
    if (!rows.length) return null;
    const runs = rows.map(r => ({ A: [r[0], r[1]], dev: pairsOf(r.slice(2)) }));
    const out = [];
    for (let j = 0; j < runs.length; j++) out.push(...hybRun(runs[j].A, runs[(j + 1) % runs.length].A, runs[j].dev));
    return out.length >= 2 ? out : null;
}

function read(form, text, tvf) {
    switch (form) {
        case 'tvf': return L.readTvf(text, false, tvf, 1024);
        case 'svgabs': case 'svgrel': return L.readSvg(text);
        case 'fd': return fdRead(text);
        case 'rad': return radRead(text, tvf);
        case 'poly': return polyRead(text);
        case 'step': return stepRead(text);
        case 'turtle': return turtleRead(text);
        case 'hyb': return hybRead(text, tvf);
    }
    throw new Error(form);
}

module.exports = { corners, fdCoeffs, fdText, centroid, radialOf, radText, dp, polyText, stepText, turtleText, hybRun, hybText, read, sineEval };
