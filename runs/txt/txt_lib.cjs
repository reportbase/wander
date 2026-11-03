// TXT (plans/txt-plan.md): shared pieces. draw's tvf-core.js and its _fitCubics are loaded from a draw checkout,
// unchanged; the readers, writers and the distance are this test's own.
'use strict';
const fs = require('fs'), vm = require('vm'), path = require('path');

function loadDraw(dir) {
    const m = { exports: {} };
    vm.runInNewContext(fs.readFileSync(path.join(dir, 'tvf-core.js'), 'utf8'), { module: m, Float64Array, Math, console });
    const html = fs.readFileSync(path.join(dir, 'draw.html'), 'utf8');
    const a = html.indexOf('        function _fitCubics(pts, tol) {');
    const b = html.indexOf('\n        }\n', a) + 10;
    if (a < 0 || b < a) throw new Error('_fitCubics not found');
    const fitCubics = new Function(html.slice(a, b) + '\nreturn _fitCubics;')();
    return { tvf: m.exports.tvf, fitCubics };
}

// A closed polyline [[x, y]…] walked by arc length at the given fractions of its length.
function walk(P, fr) {
    const n = P.length, cum = [0];
    for (let i = 0; i < n; i++) {
        const p = P[i], q = P[(i + 1) % n];
        cum.push(cum[i] + Math.hypot(q[0] - p[0], q[1] - p[1]));
    }
    const L = cum[n];
    let i = 0;
    return fr.map(f => {
        const d = (((f % 1) + 1) % 1) * L;
        while (i < n - 1 && cum[i + 1] < d) i++;
        while (i > 0 && cum[i] > d) i--;
        const p = P[i], q = P[(i + 1) % n], g = cum[i + 1] - cum[i], t = g > 0 ? (d - cum[i]) / g : 0;
        return [p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])];
    });
}

// Distance from each point of A to the closed polyline B (segments), through a grid of buckets. Returns the max.
function nearestAll(A, B, closedB = true) {
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const p of B) { x0 = Math.min(x0, p[0]); y0 = Math.min(y0, p[1]); x1 = Math.max(x1, p[0]); y1 = Math.max(y1, p[1]); }
    const span = Math.max(x1 - x0, y1 - y0, 1e-9), G = 64, cs = span / G * (1 + 1e-9) + 1e-12;
    const nseg = closedB ? B.length : B.length - 1;
    const cells = new Map();
    const key = (i, j) => i * 100003 + j;
    for (let s = 0; s < nseg; s++) {
        const p = B[s], q = B[(s + 1) % B.length];
        const i0 = Math.floor((Math.min(p[0], q[0]) - x0) / cs), i1 = Math.floor((Math.max(p[0], q[0]) - x0) / cs);
        const j0 = Math.floor((Math.min(p[1], q[1]) - y0) / cs), j1 = Math.floor((Math.max(p[1], q[1]) - y0) / cs);
        for (let i = i0; i <= i1; i++) for (let j = j0; j <= j1; j++) {
            const k = key(i, j);
            (cells.get(k) || cells.set(k, []).get(k)).push(s);
        }
    }
    const segd = (a, s) => {
        const p = B[s], q = B[(s + 1) % B.length], dx = q[0] - p[0], dy = q[1] - p[1], l = dx * dx + dy * dy;
        let t = l > 0 ? ((a[0] - p[0]) * dx + (a[1] - p[1]) * dy) / l : 0;
        t = Math.max(0, Math.min(1, t));
        return Math.hypot(a[0] - p[0] - t * dx, a[1] - p[1] - t * dy);
    };
    const out = new Float64Array(A.length);
    let ai = 0;
    for (const a of A) {
        const ci = Math.floor((a[0] - x0) / cs), cj = Math.floor((a[1] - y0) / cs);
        let best = Infinity;
        // start at the ring that first reaches the grid; visit only cells inside it
        const r0 = Math.max(0, -ci, ci - (G - 1), -cj, cj - (G - 1));
        for (let r = r0; r < r0 + 2 * G + 2; r++) {
            const ia = Math.max(ci - r, 0), ib = Math.min(ci + r, G - 1);
            for (let i = ia; i <= ib; i++) {
                const edge = Math.abs(i - ci) === r;
                const ja = Math.max(cj - r, 0), jb = Math.min(cj + r, G - 1);
                for (let j = ja; j <= jb; j++) {
                    if (!edge && Math.abs(j - cj) !== r) { j = Math.max(j, cj + r - 1); continue; }
                    const c = cells.get(key(i, j));
                    if (c) for (const s of c) { const d = segd(a, s); if (d < best) best = d; }
                }
            }
            // every segment not yet seen lies at least (r) cells away from the point's cell
            if (best <= r * cs) break;
        }
        out[ai++] = best;
    }
    return out;
}
function directed(A, B, closedB = true) {
    let w = 0;
    for (const d of nearestAll(A, B, closedB)) if (d > w) w = d;
    return w;
}
const hausdorff = (A, B, closedB = true) => Math.max(directed(A, B, closedB), directed(B, A, true));

// Numbers as written: integers at τ = 5, one decimal at τ = 1.
const fmt = (v, dp) => {
    let s = v.toFixed(dp);
    if (dp > 0) s = s.replace(/\.?0+$/, '');
    if (s === '-0') s = '0';
    return s;
};
const rnd = (v, dp) => Number(v.toFixed(dp));

function tvfText(lx, ly, dp) {
    return 'TVF ' + lx.length + ' 1 2\n' + lx.map(v => fmt(v, dp)).join(' ') + '\n' + ly.map(v => fmt(v, dp)).join(' ');
}
// segs: [[P0, P1, P2, P3]…] of {x, y}, already rounded.
function svgAbs(segs, dp) {
    const f = v => fmt(v, dp);
    let s = 'M' + f(segs[0][0].x) + ' ' + f(segs[0][0].y) + ' C';
    for (const c of segs) s += ' ' + [c[1], c[2], c[3]].map(p => f(p.x) + ' ' + f(p.y)).join(' ');
    return s + ' Z';
}
function svgRel(segs, dp) {
    const f = v => fmt(rnd(v, dp), dp);
    let px = segs[0][0].x, py = segs[0][0].y;
    let s = 'm' + f(px) + ' ' + f(py) + ' c';
    for (const c of segs) {
        s += ' ' + [c[1], c[2], c[3]].map(p => f(p.x - px) + ' ' + f(p.y - py)).join(' ');
        px = c[3].x; py = c[3].y;
    }
    return s + ' z';
}

// ── readers ──
const NUM = /^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/;
// TVF read leniently: rows are lines with no letters and at least 3 numbers; the first two are x and y.
function readTvf(text, strict, tvf, M = 1024) {
    const lines = text.split('\n');
    const rows = [];
    let headN = null, headOk = false;
    for (const ln of lines) {
        const t = ln.trim().split(/\s+/).filter(Boolean);
        if (/[A-Za-z]/.test(ln)) {
            const m = ln.trim().match(/^TVF (\d+) 1 2$/);
            if (m && !headOk) { headOk = true; headN = +m[1]; }
            continue;
        }
        const nums = t.filter(w => NUM.test(w)).map(Number);
        if (strict && nums.length !== t.length) return null;
        if (nums.length >= 3) rows.push(nums);
    }
    if (rows.length < 2) return null;
    const [x, y] = rows;
    if (strict && (!headOk || rows.length !== 2 || x.length !== headN || y.length !== headN)) return null;
    const rx = tvf.reconstruct(x, M), ry = tvf.reconstruct(y, M);
    const out = [];
    for (let i = 0; i < M; i++) out.push([rx[i], ry[i]]);
    return out;
}

// SVG path data by the spec's error rule: drawn up to the first error. M/m, C/c, L/l, Z/z; a closed outline.
function readSvg(text, K = 24) {
    const tok = text.match(/[A-Za-z]|[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?|\S/g) || [];
    const pts = [];
    let i = 0, cx = 0, cy = 0, sx = 0, sy = 0, cmd = null, started = false;
    const isNum = t => NUM.test(t);
    const take = n => {
        const a = [];
        for (let k = 0; k < n; k++) { if (i < tok.length && isNum(tok[i])) a.push(+tok[i++]); else return null; }
        return a;
    };
    outer: while (i < tok.length) {
        const t = tok[i];
        const letter = /[A-Za-z]/.test(t);
        if (letter) { cmd = t; i++; }
        else if (!isNum(t) || !cmd) break;
        const c = cmd;
        if (!started && c !== 'M' && c !== 'm') break;
        const rel = c === c.toLowerCase();
        const C = c.toUpperCase();
        if (C === 'Z') { if (!letter) break; cx = sx; cy = sy; continue; }
        const n = { M: 2, L: 2, C: 6 }[C];
        if (!n) break;
        let first = true;
        do {
            const a = take(n);
            if (!a) break outer;
            const ox = rel ? cx : 0, oy = rel ? cy : 0;
            if (C === 'M' && first) {
                cx = a[0] + ox; cy = a[1] + oy; sx = cx; sy = cy; started = true; pts.push([cx, cy]);
                cmd = rel ? 'l' : 'L';
            } else if (C === 'C') {
                const P = [[cx, cy], [a[0] + ox, a[1] + oy], [a[2] + ox, a[3] + oy], [a[4] + ox, a[5] + oy]];
                for (let k = 1; k <= K; k++) {
                    const u = k / K, v = 1 - u;
                    pts.push([0, 1].map(d => v * v * v * P[0][d] + 3 * u * v * v * P[1][d] + 3 * u * u * v * P[2][d] + u * u * u * P[3][d]));
                }
                cx = P[3][0]; cy = P[3][1];
            } else {
                cx = a[0] + ox; cy = a[1] + oy; pts.push([cx, cy]);
            }
            first = false;
        } while (i < tok.length && isNum(tok[i]));
    }
    return pts.length >= 2 ? pts : null;
}

module.exports = { nearestAll, loadDraw, walk, hausdorff, directed, fmt, rnd, tvfText, svgAbs, svgRel, readTvf, readSvg };
