    // ══ PEB run 4: an event-driven integrator (plans/peb-plan.md, run 4). On the cloth each ball's motion between events is
    //    a closed form in t (sliding: the slip shrinks at 3.5·MU_S along a fixed direction; rolling: the speed falls at MU);
    //    every event (a slip ends, a ball stops, two balls touch, a cushion, a pocket) is found as the least root ahead and
    //    the engine's own response applied at that instant. No trigonometric call. ══
    const pev = (c, x) => { let s = 0; for (let i = c.length - 1; i >= 0; i--) s = s * x + c[i]; return s; };
    const pder = c => c.slice(1).map((v, i) => v * (i + 1));
    function rootsIn(c, a, b) {
        c = c.slice(); while (c.length > 1 && c[c.length - 1] === 0) c.pop();
        if (c.length <= 1) return [];
        if (c.length === 2) { const r = -c[0] / c[1]; return r >= a && r <= b ? [r] : []; }
        const pts = [a, ...rootsIn(pder(c), a, b), b], out = [];
        for (let i = 0; i < pts.length - 1; i++) {
            let lo = pts[i], hi = pts[i + 1], flo = pev(c, lo); const fhi = pev(c, hi);
            if (flo === 0) { out.push(lo); continue; }
            if (flo * fhi > 0) continue;
            for (let k = 0; k < 200 && hi - lo > 1e-17 * Math.max(1, Math.abs(hi)); k++) { const m = (lo + hi) / 2, fm = pev(c, m); if ((fm < 0) === (flo < 0)) { lo = m; flo = fm; } else hi = m; }
            out.push(hi);
        }
        return out;
    }
    function motionOf(b) {   // { ax, az, T, ph }: x(t) = x + vx t + ½ ax t², valid for t ≤ T
        if (b.sunk) return { ph: 'none', ax: 0, az: 0, T: Infinity };
        const u = slipOf(b), us = Math.hypot(u[0], u[1]);
        if (us > 1e-12) return { ph: 'slide', ax: -MU_S * u[0] / us, az: -MU_S * u[1] / us, T: us / (3.5 * MU_S) };
        const s = Math.hypot(b.vx, b.vz);
        if (s > 0) return { ph: 'roll', ax: -MU * b.vx / s, az: -MU * b.vz / s, T: s / MU };
        return { ph: 'still', ax: 0, az: 0, T: Infinity };
    }
    function advance(b, m, dt, endPhase) {
        if (m.ph === 'none' || m.ph === 'still' || dt === 0) { if (m.ph === 'still' && b.wy && dt > 0) { const d = MU_SP * dt / b.r; b.wy = Math.abs(b.wy) <= d ? 0 : b.wy - Math.sign(b.wy) * d; } return; }
        b.x += b.vx * dt + 0.5 * m.ax * dt * dt; b.z += b.vz * dt + 0.5 * m.az * dt * dt;
        b.vx += m.ax * dt; b.vz += m.az * dt;
        if (m.ph === 'slide') { b.wx -= 2.5 * m.az * dt / b.r; b.wz += 2.5 * m.ax * dt / b.r; }
        if (endPhase && m.ph === 'roll') { b.vx = 0; b.vz = 0; }
        if (m.ph === 'roll' || endPhase) { b.wx = b.vz / b.r; b.wz = -b.vx / b.r; }
        if (b.wy) { const d = MU_SP * dt / b.r; b.wy = Math.abs(b.wy) <= d ? 0 : b.wy - Math.sign(b.wy) * d; }
    }
    function cushionOne(b, c, onRail) {   // the engine's cushion response, at the moment the gap is r
        const im = { n: [c[0], c[1]], v: 0.5 };
        const u = [b.vx / b.r, b.vz / b.r], un = u[0] * im.n[0] + u[1] * im.n[1];
        if (!(un > 0)) return false;
        const r = respond(b, im, im, [u[0] - 2 * un * im.n[0], u[1] - 2 * un * im.n[1]], E_RAIL);
        if (!r.hit) return false;
        if (onRail) onRail(b);
        b.vx += r.du[0] * b.r; b.vz += r.du[1] * b.r;
        const n = im.n, Jn = (1 + E_RAIL) * un * b.r, vn = b.vx * n[0] + b.vz * n[1];
        const sx = b.vx - vn * n[0] + b.r * b.wy * n[1], sz = b.vz - vn * n[1] - b.r * b.wy * n[0], ss = Math.hypot(sx, sz);
        if (ss > 1e-12) { const Jt = Math.min(MU_C * Jn, 2 / 7 * ss), ex = sx / ss, ez = sz / ss; b.vx -= Jt * ex; b.vz -= Jt * ez; b.wy -= 2.5 * Jt * (n[1] * ex - n[0] * ez) / b.r; }
        return true;
    }
    const CLIM = [b => -LX / 2 + b.r, b => LX / 2 - b.r, b => -LZ / 2 + b.r, b => LZ / 2 - b.r];   // the centre's limit for each cushion
    function simulateEvent(B0, dir, power, w, vy) {
        const B = B0.map(b => ({ y: 0, vy: 0, wx: 0, wy: 0, wz: 0, ...b })), cue = B.find(b => b.cue && !b.sunk);
        cue.vx = power * dir[0]; cue.vz = power * dir[1]; [cue.wx, cue.wy, cue.wz] = w || [0, 0, 0]; cue.vy = vy || 0;
        const ev = [], contacts = [], cushions = [], sunk = []; let t = 0, offCloth = cue.vy > 0, events = 0;
        while (!offCloth && events < 200000) {
            const M = B.map(motionOf);
            let Tm = Infinity; for (const m of M) Tm = Math.min(Tm, m.T);
            if (!isFinite(Tm) && B.every((b, i) => M[i].ph === 'none' || M[i].ph === 'still')) break;
            let tBest = Tm, found = [];
            const consider = (tt, e) => { if (tt < tBest - 1e-12) { tBest = tt; found = [e]; } else if (tt <= tBest + 1e-12) found.push(e); };
            for (let i = 0; i < B.length; i++) {
                const b = B[i], m = M[i]; if (b.sunk) continue;
                const moving = m.ph === 'slide' || m.ph === 'roll';
                for (let j = i + 1; j < B.length; j++) {
                    const c = B[j], mc = M[j]; if (c.sunk) continue;
                    if (!moving && !(mc.ph === 'slide' || mc.ph === 'roll')) continue;
                    const P = [c.x - b.x, c.z - b.z], Q = [c.vx - b.vx, c.vz - b.vz], R2 = [(mc.ax - m.ax) / 2, (mc.az - m.az) / 2], rr = b.r + c.r;
                    const dot = (u, v) => u[0] * v[0] + u[1] * v[1];
                    const tmax = Math.min(tBest + 1e-12, Tm);
                    if (Math.hypot(P[0], P[1]) - rr > Math.hypot(Q[0], Q[1]) * tmax + Math.hypot(R2[0], R2[1]) * tmax * tmax + 1e-9) continue;   // cannot meet in the window
                    const poly = [dot(P, P) - rr * rr, 2 * dot(P, Q), dot(Q, Q) + 2 * dot(P, R2), 2 * dot(Q, R2), dot(R2, R2)];
                    if (poly[0] <= 1e-12 * rr * rr) { if (poly[1] < 0) consider(0, { k: 'ball', i, j }); continue; }
                    const rs = rootsIn(poly, 0, tmax);
                    for (const r of rs) { if (pev(pder(poly), r) < 0) { consider(r, { k: 'ball', i, j }); break; } }
                }
                if (!moving) continue;
                for (let k = 0; k < 4; k++) {   // left, right, near, far: centre x or z reaching its limit
                    const ax = k < 2 ? 'x' : 'z', lim = CLIM[k](b), p0 = b[ax], v0 = ax === 'x' ? b.vx : b.vz, a0 = ax === 'x' ? m.ax : m.az, sgn = k % 2 ? 1 : -1;
                    const poly = [sgn * (p0 - lim), sgn * v0, sgn * a0 / 2];   // ≥ 0 means past the limit
                    if (poly[0] >= -1e-12) { if (poly[1] > 0) consider(0, { k: 'cush', i, c: k }); continue; }
                    const rs = rootsIn(poly, 0, Math.min(tBest + 1e-12, Tm));
                    for (const r of rs) { if (pev(pder(poly), r) > 0) { consider(r, { k: 'cush', i, c: k }); break; } }
                }
                for (let k = 0; k < POCKETS.length; k++) {
                    const pk = POCKETS[k], P = [b.x - pk[0], b.z - pk[1]], Q = [b.vx, b.vz], R2 = [m.ax / 2, m.az / 2];
                    const dot = (u, v) => u[0] * v[0] + u[1] * v[1];
                    const tp = Math.min(tBest + 1e-12, Tm);
                    if (Math.hypot(P[0], P[1]) - POCK > Math.hypot(Q[0], Q[1]) * tp + Math.hypot(R2[0], R2[1]) * tp * tp + 1e-9) continue;
                    const poly = [dot(P, P) - POCK * POCK, 2 * dot(P, Q), dot(Q, Q) + 2 * dot(P, R2), 2 * dot(Q, R2), dot(R2, R2)];
                    if (poly[0] < 0) { consider(0, { k: 'pock', i, p: k }); continue; }
                    const rs = rootsIn(poly, 0, Math.min(tBest + 1e-12, Tm));
                    for (const r of rs) { if (pev(pder(poly), r) < 0) { consider(r, { k: 'pock', i, p: k }); break; } }
                }
            }
            const dt = tBest;
            const phaseEnd = found.length === 0;
            B.forEach((b, i) => advance(b, M[i], dt, phaseEnd && Math.abs(M[i].T - dt) <= 1e-15 * Math.max(1, dt)));
            t += dt; events++;
            if (phaseEnd) continue;
            // pockets first, then ball contacts together, then cushions
            for (const e of found.filter(e => e.k === 'pock')) { const b = B[e.i]; if (b.sunk) continue; b.sunk = true; b.vx = b.vz = b.wx = b.wy = b.wz = 0; sunk.push({ n: b.n, pocket: e.p, t }); ev.push({ key: 'P' + b.n + '@' + e.p, g: 1 }); }
            const balls = found.filter(e => e.k === 'ball' && !B[e.i].sunk && !B[e.j].sunk);
            if (balls.length) {
                const F = ['x', 'z', 'vx', 'vz', 'wx', 'wy', 'wz'], S = B.map(b => ({ ...b })), dl = B.map(() => F.map(() => 0));
                for (const e of balls) {
                    const a = { ...S[e.i] }, c = { ...S[e.j] };
                    const wv = [a.vx - c.vx, a.vz - c.vz], dx = [c.x - a.x, c.z - a.z], dd = Math.hypot(...dx), wn = Math.abs((wv[0] * dx[0] + wv[1] * dx[1]) / dd), ws = Math.hypot(...wv) || 1;
                    pairs([a, c], null, true);
                    F.forEach((f, k) => { dl[e.i][k] += a[f] - S[e.i][f]; dl[e.j][k] += c[f] - S[e.j][f]; });
                    contacts.push({ t, a: B[e.i].n, b: B[e.j].n }); ev.push({ key: 'B' + B[e.i].n + '-' + B[e.j].n, g: wn / ws });
                }
                B.forEach((b, i) => F.forEach((f, k) => { b[f] += dl[i][k]; }));
            }
            for (const e of found.filter(e => e.k === 'cush')) {
                const b = B[e.i]; if (b.sunk) continue; const c = CUSHIONS[e.c];
                const sp = Math.hypot(b.vx, b.vz) || 1, un = (b.vx * c[0] + b.vz * c[1]) / sp;
                if (cushionOne(b, c, bb => cushions.push({ n: bb.n, t }))) ev.push({ key: 'C' + b.n + ':' + e.c, g: Math.abs(un) });
            }
            if (B.some(b => !b.sunk && (b.y > 0 || b.vy > 0))) offCloth = true;
        }
        return { contacts, cushions, sunk, ev, final: B, offCloth, events, t };
    }
