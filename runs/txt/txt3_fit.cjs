// TXT run 3, step 1: every figure in every format at τ = 5 (plans/txt-plan.md, run 3).
//   node runs/txt/txt3_fit.cjs <draw dir> <forms.json from run 2> <forms3-k.json> k/n
'use strict';
const fs = require('fs');
const L = require('./txt_lib.cjs');
const F = require('./txt3_formats.cjs');
const [drawDir, formsIn, out, shard] = process.argv.slice(2);
const [sk, sn] = (shard || '1/1').split('/').map(Number);
const { tvf } = L.loadDraw(drawDir);
const TAU = 5, DPS = [0, 1];
const pass = (P, form, text) => { const R = F.read(form, text, tvf); return R ? L.hausdorff(P, R) <= TAU : false; };

// the fewest count in [lo0, hi0] (step 'step') that passes, by doubling then bisection
function fewest(lo0, hi0, step, ok) {
    let lo = lo0 - step, hi = lo0;
    while (hi <= hi0 && !ok(hi)) { lo = hi; hi = Math.max(hi * 2, hi + step); }
    if (hi > hi0) { if (ok(hi0)) hi = hi0; else return null; }
    while (hi - lo > step) {
        const mid = lo + step * Math.floor((hi - lo) / (2 * step));
        if (mid <= lo || mid >= hi) break;
        if (ok(mid)) hi = mid; else lo = mid;
    }
    return hi;
}

function fitFD(P) {
    const KMAX = 512, all = F.fdCoeffs(P, KMAX);
    for (const dpl of DPS) {
        const text = K => F.fdText(all.re.slice(KMAX - K, KMAX + K + 1), all.im.slice(KMAX - K, KMAX + K + 1), dpl);
        const K = fewest(1, KMAX, 1, K => pass(P, 'fd', text(K)));
        if (K) return { text: text(K), count: 2 * K + 1, dp: dpl };
    }
    return null;
}
function fitRAD(P) {
    const c = F.centroid(P), r = F.radialOf(P, c);
    if (!r) return { applies: false };
    for (const dpl of DPS) {
        const text = N => F.radText(c, Array.from({ length: N }, (_, k) => r((k + 0.5) * 2 * Math.PI / N)), dpl);
        const N = fewest(4, 1024, 2, N => pass(P, 'rad', text(N)));
        if (N) return { text: text(N), count: N, dp: dpl };
    }
    return { applies: true, failed: true };
}
function fitPolys(P, cs) {
    const start = cs.length ? cs[0] : 0, res = {};
    for (let tol = TAU * 0.8, k = 0; k < 16 && !(res.poly && res.turtle); k++, tol *= 0.8) {
        const V = F.dp(P, tol, start);
        for (const dpl of DPS) if (!res.poly && pass(P, 'poly', F.polyText(V, dpl))) {
            res.poly = { text: F.polyText(V, dpl), count: V.length, dp: dpl };
            res.step = { text: F.stepText(V, dpl), count: V.length, dp: dpl };
        }
        for (const [pd, pa] of [[0, 1], [1, 2]]) if (!res.turtle && pass(P, 'turtle', F.turtleText(V, pd, pa)))
            res.turtle = { text: F.turtleText(V, pd, pa), count: V.length, dp: pd };
    }
    return res;
}
function fitHYB(P, cs, tvfText) {
    if (!cs.length) return { text: tvfText, smooth: true };
    const n = P.length, idx = cs.slice().sort((a, b) => a - b);
    for (const dpl of DPS) for (let rt = TAU * 0.8, t = 0; t < 8; t++, rt *= 0.75) {
        const runs = [];
        for (let j = 0; j < idx.length; j++) {
            const a = idx[j], b = j + 1 < idx.length ? idx[j + 1] : idx[0] + n;
            const pts = []; for (let i = a; i <= b; i++) pts.push(P[i % n]);
            const A = P[a], B = P[b % n], m = pts.length - 1;
            const devAt = nn => Array.from({ length: nn }, (_, k) => {
                const s = (k + 0.5) / nn, f = s * m, i = Math.min(m - 1, Math.floor(f)), u = f - i;
                const x = pts[i][0] + u * (pts[i + 1][0] - pts[i][0]), y = pts[i][1] + u * (pts[i + 1][1] - pts[i][1]);
                return [L.rnd(x - (A[0] + s * (B[0] - A[0])), dpl), L.rnd(y - (A[1] + s * (B[1] - A[1])), dpl)];
            });
            const Ar = [L.rnd(A[0], dpl), L.rnd(A[1], dpl)], Br = [L.rnd(B[0], dpl), L.rnd(B[1], dpl)];
            const ok = nn => {
                const R = F.hybRun(Ar, Br, devAt(nn));
                R.push(Br);
                return Math.max(L.directed(pts, R, false), L.directed(R, pts, false)) <= rt;
            };
            const nn = ok(0) ? 0 : fewest(1, 256, 1, ok);
            if (nn === null) return null;
            runs.push({ A: Ar, dev: devAt(nn) });
        }
        const text = F.hybText(runs, dpl);
        if (pass(P, 'hyb', text)) return { text, count: runs.length + runs.reduce((s, r) => s + r.dev.length, 0), dp: dpl };
    }
    return null;
}

const forms = JSON.parse(fs.readFileSync(formsIn, 'utf8')).filter((_, i) => i % sn === sk - 1);
const res = [];
for (const f of forms) {
    const P = f.P, cs = F.corners(P), f5 = f.forms['5'];
    const t0 = Date.now();
    const texts = { tvf: f5.tvf, svgabs: f5.abs, svgrel: f5.rel };
    const fd = fitFD(P); if (fd) texts.fd = fd.text;
    const rad = fitRAD(P); if (rad && rad.text) texts.rad = rad.text;
    const pl = fitPolys(P, cs); for (const k of ['poly', 'step', 'turtle']) if (pl[k]) texts[k] = pl[k].text;
    const hy = fitHYB(P, cs, f5.tvf); if (hy) texts.hyb = hy.text;
    // check every text once more, as read back
    const check = {};
    for (const [k, t] of Object.entries(texts)) { const R = F.read(k, t, tvf); check[k] = R ? +L.hausdorff(P, R).toFixed(2) : null; }
    res.push({ key: f.key, corners: cs.length, radApplies: rad.applies !== false, P, texts, check });
    process.stderr.write(`${f.key}: corners ${cs.length} ${Object.keys(texts).join(',')} ${((Date.now() - t0) / 1000).toFixed(1)} s\n`);
}
fs.writeFileSync(out, JSON.stringify(res));
