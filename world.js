// world.js: Wander's world, shared by the flying page (index.html) and the lab (labs.html).
//
// Moved out of index.html on 6 October 2026, line for line, when the labs moved to labs.html (Tom's choice: one shared
// script, so that the labs keep running on exactly Wander's own machinery). It holds what both pages use and nothing
// that draws or reads the page: the constants, the solids, the systems and their ticks (tickSystem), the signals'
// speed and the arrival rule's pieces, the readout's distance step (farnessAt), and the reading functions the live
// readout took from the labs (plxTwoPart, plxTwoPartLT, twoAt, twoMisfit, planeMisfit, reachInPlane).
//
// A classic script, not a module: its top-level names are shared with the pages' own scripts, which is what lets both
// pages assign starsNow (the stars tickSystem pulls toward) and read the rest. Load it before either page's script.
// Edit the world here; a change here changes the labs' world too, so run every lab after it (THE LAB GUIDE, labs.html).

const $ = id => document.getElementById(id);

const TAU = Math.PI * 2,
    N = 240,
    GRAIN = 0.004,
    SCAN = 30,
    STRIP = 104,
    D1 = 3.5;

// ── solids, from the rung editor (3d.html): each is a radius r(θ, h) about its own axis, θ a full turn and h from
//    base to top on [0, 1]. The object carries its own addresses; a reader's address meets it where it first falls
//    inside r. Sampled once to a grid and read back by interpolation. ──
const PI = Math.PI,
    wrapA = a => Math.atan2(Math.sin(a), Math.cos(a));
const SOLID_FN = {
    cylinder: (th, h) => 0.22,
    pawn: (th, h) => Math.max(0.05, 0.10 + 0.14 * Math.exp(-((h - 0.12) ** 2) / 0.02) + 0.09 * Math.exp(-((h - 0.55) ** 2) / 0.03) + 0.12 * Math.exp(-((h - 0.85) ** 2) / 0.012)),
    rook: (th, h) => {
        let r = 0.13;
        if (h < 0.18)
            r = 0.20 - 0.3 * h;
        if (h > 0.8)
            r = 0.19;
        return Math.max(0.08, Math.min(0.22, r));
    },
    knight: (th, h) => {
        let r = 0.16 - 0.05 * h;
        const dM = wrapA(th - 0);
        r += 0.13 * Math.exp(-(dM * dM) / (2 * 0.45 * 0.45)) * Math.exp(-((h - 0.72) ** 2) / (2 * 0.10 * 0.10));
        r += 0.05 * Math.exp(-(dM * dM) / (2 * 0.5 * 0.5)) * Math.exp(-((h - 0.88) ** 2) / (2 * 0.06 * 0.06));
        const dMane = wrapA(th - PI);
        r += 0.09 * Math.exp(-(dMane * dMane) / (2 * 0.55 * 0.55)) * Math.exp(-((h - 0.6) ** 2) / (2 * 0.22 * 0.22));
        for (const ea of [2.4, 3.9]) {
            const d = wrapA(th - ea);
            r += 0.04 * Math.exp(-(d * d) / (2 * 0.2 * 0.2)) * Math.exp(-((h - 0.95) ** 2) / (2 * 0.04 * 0.04));
        }
        return Math.max(0.04, r);
    },
    sphere: (th, h) => Math.max(0.04, 0.26 * Math.sin(PI * h)),
    egg: (th, h) => Math.max(0.04, 0.26 * Math.pow(Math.sin(PI * h * 0.92 + 0.08), 1.4)),
    cone: (th, h) => Math.max(0.04, 0.26 * (1 - h) + 0.04),
    diamond: (th, h) => Math.max(0.04, 0.30 * (1 - Math.abs(2 * h - 1)) + 0.03),
    vase: (th, h) => Math.max(0.05, 0.10 + 0.13 * Math.exp(-((h - 0.08) ** 2) / 0.01) + 0.16 * Math.pow(Math.sin(PI * Math.min(1, h * 1.05)), 1.6) - 0.06 * Math.exp(-((h - 0.45) ** 2) / 0.02)),
    cube: (th, h) => {
        const A = 0.28; // TRUE cube — sharp vertical edges (max in θ) + steep flat top/bottom
        const cs = A / Math.max(Math.abs(Math.cos(th)), Math.abs(Math.sin(th)));
        const u = 2 * Math.abs(h - 0.5) / 0.56,
            env = 1 - Math.pow(Math.max(0, Math.min(1, u)), 12);
        return Math.max(0.004, cs * env);
    },
    rounded_cube: (th, h) => {
        const A = 0.30,
            N = 4; // cube with rounded edges (w:d:h ≈ 1:1:1, verified)
        const cs = 1 / Math.pow(Math.pow(Math.abs(Math.cos(th)) / A, N) + Math.pow(Math.abs(Math.sin(th)) / A, N), 1 / N);
        const u = 2 * Math.abs(h - 0.5) / 0.55,
            env = 1 - Math.pow(Math.max(0, Math.min(1, u)), 6);
        return Math.max(0.004, cs * env);
    },
    gem: (th, h) => Math.max(0.04, (0.24 * Math.sin(PI * h) + 0.03) * (1 + 0.18 * Math.cos(6 * th))),
    fluted: (th, h) => Math.max(0.05, 0.20 * (1 + 0.12 * Math.cos(10 * th))),
    brilliant: (th, h) => {
        const env = h <= 0.55 ? 0.32 * (h / 0.55) : 0.32 - (h - 0.55) / 0.45 * 0.13;
        return Math.max(0.04, env * (1 + 0.15 * Math.cos(8 * th)));
    },
    // round brilliant: 8-fold, pointed culet, wide girdle, tabular crown
    emerald: (th, h) => {
        const env = 0.22 * Math.pow(Math.sin(PI * (h * 0.8 + 0.1)), 0.6);
        return Math.max(0.04, env * (1 + 0.20 * Math.cos(4 * th)));
    },
    // emerald cut: 4-fold rectangular, tapered ends
    quartz: (th, h) => {
        const env = h < 0.7 ? 0.22 : 0.22 * (1 - (h - 0.7) / 0.30);
        return Math.max(0.04, env * (1 + 0.10 * Math.cos(6 * th)));
    },
    // quartz crystal: 6-fold hex prism + pyramidal point on top
    twisted: (th, h) => Math.max(0.04, 0.20 * (1 + 0.18 * Math.cos(6 * th + TAU * h))),
    // helical 6-fold: facets rotate one full turn up the height
    star: (th, h) => {
        const peak = Math.pow((1 + Math.cos(5 * th)) / 2, 3);
        const env = 0.28 * (1 - h * 0.85);
        return Math.max(0.04, env * (0.55 + 0.45 * peak));
    },
    // 5-pointed star tapered to spire
    spiked: (th, h) => {
        const env = 0.20 * Math.sin(PI * h);
        const sp = Math.pow(Math.max(0, Math.cos(6 * th)), 2);
        return Math.max(0.04, env * (1 + 0.40 * sp));
    },
    // sphere with 6 sharp narrow spikes
    bishop: (th, h) => {
        let r = 0.09 + 0.13 * Math.exp(-((h - 0.1) ** 2) / 0.012) + 0.10 * Math.pow(Math.sin(PI * Math.min(1, h)), 1.3);
        const slit = wrapA(th - 0);
        r -= 0.05 * Math.exp(-(slit * slit) / (2 * 0.12 * 0.12)) * Math.exp(-((h - 0.82) ** 2) / (2 * 0.06 * 0.06));
        return Math.max(0.05, r);
    },
    queen: (th, h) => {
        let r = 0.10 + 0.13 * Math.exp(-((h - 0.1) ** 2) / 0.012) + 0.09 * Math.pow(Math.sin(PI * Math.min(1, h * 0.95)), 1.2);
        if (h > 0.82)
            r += 0.05 * Math.max(0, Math.cos(8 * th)) * ((h - 0.82) / 0.18);
        return Math.max(0.05, r);
    },

};
const GT = 192,
    GH = 128,
    HS = 1.1,
    SOLIDS = {};
for (const [nm, f] of Object.entries(SOLID_FN)) {
    const g = new Float32Array(GT * GH);
    let mx = 0;
    for (let i = 0; i < GH; i++)
        for (let j = 0; j < GT; j++) {
            const v = f(TAU * j / GT, (i + 0.5) / GH);
            g[i * GT + j] = v;
            if (v > mx)
                mx = v;
        }
    SOLIDS[nm] = {
        g,
        mx
    };
}
// a true ball, for stars: radius half the height at the middle, closing to a point at each end
{
    const g = new Float32Array(GT * GH);
    for (let i = 0; i < GH; i++) {
        const h = (i + 0.5) / GH,
            r = (HS / 2) * Math.sqrt(Math.max(0, 1 - (2 * h - 1) ** 2));
        for (let j = 0; j < GT; j++)
            g[i * GT + j] = r;
    }
    SOLIDS.ball = {
        g,
        mx: HS / 2
    };
}

// ── how each object carries on. Every one has its own way; none of them knows anything but where it is and,
//    for a few, where you are. ──
const unit = v => {
    const l = Math.hypot(v[0], v[1], v[2]) || 1;
    return [v[0] / l, v[1] / l, v[2] / l];
};

const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const perp = u => unit(cross(u, Math.abs(u[1]) < 0.9 ? [0, 1, 0] : [1, 0, 0]));
const setAxis = (o, u) => {
    const e1 = perp(u);
    o.ax = [e1, u, cross(e1, u)];
};
const setSize = (o, S) => {
    o.S = S;
    o.sz = S;
    o.Rb = S * Math.hypot(o.mx, HS / 2) * 1.03;
};

// what an object does with itself. Where it goes is gravity's (below); these are its own ways of carrying on.
const BEHAVE = {
    still: () => {},
    spin: () => {},
    // a quick spin about its own axis; every object keeps its spin
    // its axis sweeps round, so it tumbles end over end
    tumble: o => {
        const a = o.w * o.t + o.ph,
            c = Math.cos(a),
            sn = Math.sin(a);
        setAxis(o, [o.u0[0] * c + o.w0[0] * sn, o.u0[1] * c + o.w0[1] * sn, o.u0[2] * c + o.w0[2] * sn]);
    },
    // grows and shrinks (its mass stays what it is)
    breathe: o => setSize(o, o.S0 * (1 + 0.3 * Math.sin(o.w * o.t + o.ph))),
    // turns from one shape into another and back
    morph: o => {
        o.mix = 0.5 - 0.5 * Math.cos(o.w * o.t + o.ph);
    },
    // pushes itself toward you and holds off a little way; gravity still has it
    curious: o => {
        const Y = seenReader(o),
            dx = Y[0] - o.x,
            dy = Y[1] - o.yo,
            dz = Y[2] - o.z,
            d = Math.hypot(dx, dy, dz) || 1,
            f = d < 40 && d > 6 + o.Rb ? 2.5 / d : 0;
        o.thr = [dx * f, dy * f, dz * f];
        o.drag = 0.6;
        const u = o.ax[1],
            k2 = 0.05;
        setAxis(o, unit([u[0] + (dx / d - u[0]) * k2, u[1] + (dy / d - u[1]) * k2, u[2] + (dz / d - u[2]) * k2]));
    },
    // pushes itself away from you when you come near
    shy: o => {
        const Y = seenReader(o),
            dx = o.x - Y[0],
            dy = o.yo - Y[1],
            dz = o.z - Y[2],
            d = Math.hypot(dx, dy, dz) || 1,
            f = d < 14 ? 7 / d : 0;
        o.thr = [dx * f, dy * f, dz * f];
        o.drag = 0.5;
    },
};
const behave = (o, dt) => (BEHAVE[o.beh] || BEHAVE.still)(o, dt);
// ── no shared now. Each system keeps its own time and steps at its own rate; at each of its steps it sends a
//    signal: where each of its bodies is, how it is turned, its size and shape, and whether it is still there, tagged
//    with the system's own time. Signals travel at C_SIG. The reader holds nothing of the world but what has
//    reached it: for each body, the latest signal to have arrived where the reader is now. Every system is a
//    distinct signal, so every system is a distinct serial read. ──
const G = 0.18,
    SOFT2 = 1.0,
    SYS = new Map(),
    C_SIG = 20,
    WARM = 4.6,
    HCAP = 200,
    HK = 16;
let starsNow = [];
// ── brightness (9 Oct 2026; Tom: "yes, do all of them", after SPN's "the same signal, a smaller share"). A body sending
//    light L spreads it over the sphere about it; a reader at d holding an aperture A (its own unit) receives L·A/(4π·d²)
//    of it, whether the body covers many of the reader's addresses or under one: the inverse square, with nothing in
//    between. The law has no corner of its own; the reader's grain puts one in. Read only by LAD's third run so far:
//    no other lab, and nothing the flying page draws, uses it. ──
const lightAt = (L, d, A = 1) => L * A / (4 * PI * d * d);
// the reader's own path, so that the bodies that heed it (curious, shy) also get only what has reached them
const RH = {
    t: new Float64Array(400),
    p: new Float32Array(1200),
    head: -1,
    n: 0
};

const seenReader = o => {
    for (let q = 0; q < RH.n; q++) {
        const i = (RH.head - q + 400) % 400,
            x = RH.p[i * 3],
            y = RH.p[i * 3 + 1],
            z = RH.p[i * 3 + 2];
        if (C_SIG * (o.t - RH.t[i]) >= Math.hypot(x - o.x, y - o.yo, z - o.z))
            return [x, y, z];
    }
    return RH.n ? [RH.p[((RH.head - RH.n + 1 + 400) % 400) * 3], RH.p[((RH.head - RH.n + 1 + 400) % 400) * 3 + 1], RH.p[((RH.head - RH.n + 1 + 400) % 400) * 3 + 2]] : [1e9, 1e9, 1e9];
};
function tickSystem(sy) {
    const h = sy.h,
        n = 2,
        hh = h / n;
    sy.t += h;
    const bodies = sy.bodies.filter(o => o.deadAt == null || o.deadAt > sy.t);
    for (const o of bodies) {
        o.t = sy.t;
        o.spin = o.y0 + o.yw * sy.t;
        behave(o);
    }
    const src = sy.free ? starsNow : bodies;
    for (let it = 0; it < n; it++) {
        for (const o of bodies) {
            let ax = 0,
                ay = 0,
                az = 0;
            if (o.thr) {
                ax = o.thr[0];
                ay = o.thr[1];
                az = o.thr[2];
            }
            for (const b of src) {
                if (b === o || (b.deadAt != null && b.deadAt <= sy.t))
                    continue;
                const dx = b.x - o.x,
                    dy = b.yo - o.yo,
                    dz = b.z - o.z,
                    r2 = dx * dx + dy * dy + dz * dz + (sy.soft2 != null ? sy.soft2 : SOFT2),
                    f = G * b.m / (r2 * Math.sqrt(r2));
                ax += dx * f;
                ay += dy * f;
                az += dz * f;
            }
            if (sy.hub) {
                const dx = sy.hub.x - o.x,
                    dy = sy.hub.y - o.yo,
                    dz = sy.hub.z - o.z,
                    r2 = dx * dx + dy * dy + dz * dz + SOFT2,
                    f = G * sy.hub.m / (r2 * Math.sqrt(r2));
                ax += dx * f;
                ay += dy * f;
                az += dz * f;
            }
            o.acc = [ax, ay, az];
        }
        for (const o of bodies) {
            const v = o.v,
                a = o.acc,
                dr = o.drag ? Math.max(0, 1 - o.drag * hh) : 1;
            v[0] = (v[0] + a[0] * hh) * dr;
            v[1] = (v[1] + a[1] * hh) * dr;
            v[2] = (v[2] + a[2] * hh) * dr;
            o.x += v[0] * hh;
            o.yo += v[1] * hh;
            o.z += v[2] * hh;
        }
        // the world's side: bodies of a cluster that touch bounce off each other, momentum kept (each taken as a ball of
        // its own size); every touch is written down, only to score the reader by
        if (sy.hub)
            for (const o of bodies) {
                const dx = o.x - sy.hub.x,
                    dy = o.yo - sy.hub.y,
                    dz = o.z - sy.hub.z,
                    dd = Math.hypot(dx, dy, dz),
                    lim = sy.hub.R - o.S * 0.8;
                if (dd > lim) {
                    const n = [dx / dd, dy / dd, dz / dd],
                        vn = o.v[0] * n[0] + o.v[1] * n[1] + o.v[2] * n[2];
                    if (vn > 0)
                        for (let q = 0; q < 3; q++)
                            o.v[q] -= 2 * vn * n[q];
                }
            }
        if (sy.hub)
            for (let i = 0; i < bodies.length; i++)
                for (let j = i + 1; j < bodies.length; j++) {
                    const A = bodies[i],
                        B = bodies[j],
                        rA = A.S * Math.max(A.mx, HS / 2) * 0.8,
                        rB = B.S * Math.max(B.mx, HS / 2) * 0.8;
                    const dx = B.x - A.x,
                        dy = B.yo - A.yo,
                        dz = B.z - A.z,
                        dd = Math.hypot(dx, dy, dz);
                    if (dd >= rA + rB || dd === 0)
                        continue;
                    const n = [dx / dd, dy / dd, dz / dd];
                    const vr = (B.v[0] - A.v[0]) * n[0] + (B.v[1] - A.v[1]) * n[1] + (B.v[2] - A.v[2]) * n[2],
                        push = (rA + rB - dd) / 2;
                    A.x -= n[0] * push;
                    A.yo -= n[1] * push;
                    A.z -= n[2] * push;
                    B.x += n[0] * push;
                    B.yo += n[1] * push;
                    B.z += n[2] * push;
                    if (vr < 0) {
                        const jj = 2 * vr / (1 / A.m + 1 / B.m);
                        for (let q = 0; q < 3; q++) {
                            A.v[q] += jj / A.m * n[q];
                            B.v[q] -= jj / B.m * n[q];
                        }
                        (sy.events || (sy.events = [])).push({
                            t: sy.t,
                            a: A,
                            b: B,
                            p: [A.x + n[0] * rA, A.yo + n[1] * rA, A.z + n[2] * rA]
                        });
                        if (sy.events.length > 60)
                            sy.events.shift();
                    }
                }
    }
    // the signal
    sy.head = (sy.head + 1) % HCAP;
    sy.times[sy.head] = sy.t;
    sy.count = Math.min(HCAP, sy.count + 1);
    for (const o of sy.bodies) {
        const b = o.hist,
            k = sy.head * HK,
            A = o.ax;
        b[k] = o.x;
        b[k + 1] = o.yo;
        b[k + 2] = o.z;
        b[k + 3] = o.spin;
        b[k + 4] = o.S;
        b[k + 5] = o.mix;
        b[k + 6] = A[0][0];
        b[k + 7] = A[0][1];
        b[k + 8] = A[0][2];
        b[k + 9] = A[1][0];
        b[k + 10] = A[1][1];
        b[k + 11] = A[1][2];
        b[k + 12] = A[2][0];
        b[k + 13] = A[2][1];
        b[k + 14] = A[2][2];
        b[k + 15] = o.deadAt != null && o.deadAt <= sy.t ? 1 : 0;
    }
}
// the readout's distance step, kept here so the PLX lab runs the same code the readout does
const worldDirW = (v, hd, pt) => {
    const c = Math.cos(pt),
        sn = Math.sin(pt),
        y = v[1] * c + v[2] * sn,
        z = -v[1] * sn + v[2] * c;
    return [v[0] * Math.cos(hd) + z * Math.sin(hd), y, -v[0] * Math.sin(hd) + z * Math.cos(hd)];
};
// how far, in units of the reader's own travel: over the last moments, the turn of its direction (the reader's own
// turning taken out) against the reader's own travel across that direction. d ∝ sin θ / ω; the speed cancels in a ratio.
const farnessAt = (H, clock) => {
    const w = H.filter(r => clock - r.t < 0.6);
    if (w.length < 3)
        return null;
    const r0 = w[0],
        r1 = w[w.length - 1],
        dt = r1.t - r0.t;
    if (dt <= 0)
        return null;
    const u0 = worldDirW(r0.dm, r0.hd, r0.pt),
        u1 = worldDirW(r1.dm, r1.hd, r1.pt),
        D = [r1.me[0] - r0.me[0], r1.me[1] - r0.me[1], r1.me[2] - r0.me[2]],
        dl = Math.hypot(D[0], D[1], D[2]);
    if (dl < 0.05)
        return null;
    const t = D.map(x => x / dl),
        um = unit([u0[0] + u1[0], u0[1] + u1[1], u0[2] + u1[2]]),
        cr = cross(t, um),
        sn = Math.hypot(cr[0], cr[1], cr[2]);
    const om = Math.acos(Math.max(-1, Math.min(1, u0[0] * u1[0] + u0[1] * u1[1] + u0[2] * u1[2]))) / dt;
    if (sn < 0.15 || om < 1e-4)
        return null;
    return sn / om;
};

// the two-part reading: least squares in X0, V (6 numbers) over the window; also how well the window decides them
function plxTwoPart(fr) {
    const tm = (fr[0].t + fr[fr.length - 1].t) / 2,
        A = Array.from({
            length: 6
        }, () => new Float64Array(6)),
        b = new Float64Array(6);
    for (const q of fr) {
        const [ux, uy, uz] = q.u,
            Ux = [[0, -uz, uy], [uz, 0, -ux], [-uy, ux, 0]],
            tau = q.t - tm,
            rhs = Ux.map(row => row[0] * q.R[0] + row[1] * q.R[1] + row[2] * q.R[2]);
        for (let r = 0; r < 3; r++) {
            const row = [Ux[r][0], Ux[r][1], Ux[r][2], tau * Ux[r][0], tau * Ux[r][1], tau * Ux[r][2]];
            for (let a = 0; a < 6; a++) {
                b[a] += row[a] * rhs[r];
                for (let c = 0; c < 6; c++)
                    A[a][c] += row[a] * row[c];
            }
        }
    }
    // how well decided: the smallest over the largest of the normal matrix's eigenvalues (Jacobi), square-rooted
    const E = A.map(r => Array.from(r));
    for (let sweep = 0; sweep < 60; sweep++) {
        let off = 0;
        for (let p = 0; p < 6; p++)
            for (let q = p + 1; q < 6; q++)
                off += E[p][q] * E[p][q];
        if (off < 1e-30)
            break;
        for (let p = 0; p < 6; p++)
            for (let q = p + 1; q < 6; q++) {
                if (Math.abs(E[p][q]) < 1e-300)
                    continue;
                const th = (E[q][q] - E[p][p]) / (2 * E[p][q]),
                    t = Math.sign(th || 1) / (Math.abs(th) + Math.sqrt(th * th + 1)),
                    c = 1 / Math.sqrt(t * t + 1),
                    sn = t * c;
                for (let k = 0; k < 6; k++) {
                    const ep = E[k][p],
                        eq = E[k][q];
                    E[k][p] = c * ep - sn * eq;
                    E[k][q] = sn * ep + c * eq;
                }
                for (let k = 0; k < 6; k++) {
                    const ep = E[p][k],
                        eq = E[q][k];
                    E[p][k] = c * ep - sn * eq;
                    E[q][k] = sn * ep + c * eq;
                }
            }
    }
    const ev = E.map((r, k) => Math.abs(r[k])),
        decided = Math.sqrt(Math.min(...ev) / Math.max(...ev));
    const M = A.map((r, k) => [...r, b[k]]);
    for (let c = 0; c < 6; c++) {
        let pv = c;
        for (let r = c + 1; r < 6; r++)
            if (Math.abs(M[r][c]) > Math.abs(M[pv][c]))
                pv = r;
        [M[c], M[pv]] = [M[pv], M[c]];
        for (let r = 0; r < 6; r++)
            if (r !== c) {
                const k = M[r][c] / M[c][c];
                for (let q = c; q < 7; q++)
                    M[r][q] -= k * M[c][q];
            }
    }
    const x = M.map((r, k) => r[6] / r[k]),
        q = fr.reduce((p, z) => Math.abs(z.t - tm) < Math.abs(p.t - tm) ? z : p);
    return {
        d: Math.hypot(x[0] - q.R[0], x[1] - q.R[1], x[2] - q.R[2]),
        dTrue: q.d,
        V: [x[3], x[4], x[5]],
        X0: [x[0], x[1], x[2]],
        tm,
        decided
    };
}
// the two-part reading with the delay taken out: each arrival's moment moved back to when its signal left, by its
//    distance over the signals' speed C (the reader's own, from RMR); place, motion and moments settled together by
//    repeating the fit until they agree
function plxTwoPartLT(fr, C) {
    let r = plxTwoPart(fr);
    const tq = (fr[0].t + fr[fr.length - 1].t) / 2,
        q = fr.reduce((p, z) => Math.abs(z.t - tq) < Math.abs(p.t - tq) ? z : p);
    const at = (r, te) => [r.X0[0] + r.V[0] * (te - r.tm), r.X0[1] + r.V[1] * (te - r.tm), r.X0[2] + r.V[2] * (te - r.tm)];
    const left = (r, z) => {
        let te = z.t;
        for (let i = 0; i < 6; i++) {
            const X = at(r, te);
            te = z.t - Math.hypot(X[0] - z.R[0], X[1] - z.R[1], X[2] - z.R[2]) / C;
        }
        return te;
    };
    for (let it = 0; it < 10; it++)
        r = plxTwoPart(fr.map(z => ({
            t: left(r, z),
            R: z.R,
            u: z.u,
            d: z.d
        })));
    const X = at(r, left(r, q));
    return {
        d: Math.hypot(X[0] - q.R[0], X[1] - q.R[1], X[2] - q.R[2]),
        dTrue: q.d,
        V: r.V,
        X0: r.X0,
        tm: r.tm,
        decided: r.decided
    };
}
// the readout's use of the two-part reading: where the fitted body is, as it arrives at your clock t from where you are
function twoAt(T, t, R) {
    let te = t;
    if (T.C)
        for (let i = 0; i < 6; i++) {
            const X = [0, 1, 2].map(c => T.X0[c] + T.V[c] * (te - T.tm));
            te = t - Math.hypot(X[0] - R[0], X[1] - R[1], X[2] - R[2]) / T.C;
        }
    return [0, 1, 2].map(c => T.X0[c] + T.V[c] * (te - T.tm));
}
// how far the arrivals sit from the fitted track: the rms angle between each arrival and the fitted place for it
function twoMisfit(fr, r, C) {
    let s = 0;
    for (const z of fr) {
        const X = twoAt({
                X0: r.X0,
                V: r.V,
                tm: r.tm,
                C
            }, z.t, z.R),
            D = [X[0] - z.R[0], X[1] - z.R[1], X[2] - z.R[2]],
            d = Math.hypot(...D) || 1;
        const a = Math.acos(Math.max(-1, Math.min(1, (D[0] * z.u[0] + D[1] * z.u[1] + D[2] * z.u[2]) / d)));
        s += a * a;
    }
    return Math.sqrt(s / fr.length);
}

// half the longest chord through B, for points about B (B at the origin) on a loop in a plane: the plane from the
// loop's own turning, each point's angle in it, the far side found by halving the angle (as KEP does)
// how far points about B (B at the origin) are from lying in one plane through B: the smallest share of their spread
// across any plane through the origin (the least root of Σ r rᵀ, by its characteristic cubic)
function planeMisfit(rel) {
    let a = 0,
        b = 0,
        c = 0,
        d = 0,
        e = 0,
        f = 0;
    for (const r of rel) {
        a += r[0] * r[0];
        b += r[1] * r[1];
        c += r[2] * r[2];
        d += r[0] * r[1];
        e += r[1] * r[2];
        f += r[0] * r[2];
    }
    const tr = a + b + c,
        q = tr / 3,
        p1 = d * d + e * e + f * f,
        p2 = (a - q) ** 2 + (b - q) ** 2 + (c - q) ** 2 + 2 * p1,
        p = Math.sqrt(p2 / 6) || 1e-30;
    const B = [[(a - q) / p, d / p, f / p], [d / p, (b - q) / p, e / p], [f / p, e / p, (c - q) / p]],
        detB = B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0]) + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]);
    const phi = Math.acos(Math.max(-1, Math.min(1, detB / 2))) / 3;
    return (q + 2 * p * Math.cos(phi + 2 * PI / 3)) / (tr || 1);
}
function reachInPlane(rel) {
    const n = rel.length,
        k = Math.max(1, Math.floor(n / 4));
    let N = [0, 0, 0];
    for (let i = 0; i < n; i++) {
        const c = cross(rel[i], rel[(i + k) % n]);
        N = [N[0] + c[0], N[1] + c[1], N[2] + c[2]];
    }
    if (Math.hypot(...N) < 1e-9)
        return null;
    N = unit(N);
    const r0 = rel[0],
        dn = r0[0] * N[0] + r0[1] * N[1] + r0[2] * N[2],
        p1 = unit([r0[0] - dn * N[0], r0[1] - dn * N[1], r0[2] - dn * N[2]]),
        p2 = cross(N, p1);
    const srt = rel.map(r => ({
        phi: Math.atan2(r[0] * p2[0] + r[1] * p2[1] + r[2] * p2[2], r[0] * p1[0] + r[1] * p1[1] + r[2] * p1[2]),
        rho: Math.hypot(r[0], r[1], r[2])
    })).sort((a, b) => a.phi - b.phi); /* atan2 only as an index */
    const rhoAt = ph => {
        ph = ((ph + PI) % TAU + TAU) % TAU - PI;
        let lo = 0,
            hi = srt.length - 1;
        if (ph <= srt[0].phi || ph >= srt[hi].phi)
            return (srt[0].rho + srt[hi].rho) / 2;
        while (hi - lo > 1) {
            const m = (lo + hi) >> 1;
            if (srt[m].phi <= ph)
                lo = m;
            else
                hi = m;
        }
        const f = (ph - srt[lo].phi) / (srt[hi].phi - srt[lo].phi);
        return srt[lo].rho + f * (srt[hi].rho - srt[lo].rho);
    };
    let ch = 0;
    for (const p of srt)
        ch = Math.max(ch, p.rho + rhoAt(p.phi + PI));
    return ch / 2;
}
