// PEB run 3 (plans/peb-plan.md): run 2, and the cloth from the moment of contact. node runs/peb/peb3.mjs
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const root = path.resolve('.');

// the slope copy, made from play-trick.html with the original untouched
let src = fs.readFileSync('play-trick.html', 'utf8');
const rep = (a, b) => { if (!src.includes(a)) throw new Error('patch point missing: ' + a.slice(0, 60)); src = src.replace(a, b); };
rep('cue.vx = power * Math.cos(ang); cue.vz = power * Math.sin(ang);',
    'if (Array.isArray(ang)) { cue.vx = power * ang[0]; cue.vz = power * ang[1]; } else { cue.vx = power * Math.cos(ang); cue.vz = power * Math.sin(ang); }');
rep('cut: Math.asin(sinPhi) / D,', 'cut: window.__slopeMode ? sinPhi : Math.asin(sinPhi) / D,');
rep('    const shotNow = () =>', `    // the strike in slopes: the aim and the elevation as half-slopes t = tan(a/2), te = tan(el/2); the struck direction a pair
    function strikeSlope(t, fx, fy, pw, mu, te) {
        const f2 = fx * fx + fy * fy; if (f2 > 0.9) { const k = Math.sqrt(0.9 / f2); fx *= k; fy *= k; }
        const ca_ = (1 - t * t) / (1 + t * t), sa_ = 2 * t / (1 + t * t), ce = (1 - te * te) / (1 + te * te), se = 2 * te / (1 + te * te);
        const ca = Math.sqrt(1 - fx * fx - fy * fy);
        const c = [ce * ca_, -se, ce * sa_], sv = [-sa_, 0, ca_];
        const up = [sv[1] * c[2] - sv[2] * c[1], sv[2] * c[0] - sv[0] * c[2], sv[0] * c[1] - sv[1] * c[0]];
        const n = [0, 1, 2].map(k => ca * c[k] - fx * sv[k] - fy * up[k]);
        const grip = Math.hypot(fx, fy) <= mu * ca + 1e-12;
        let J;
        if (grip) J = c.map(x => pw * x);
        else { const cn = c[0] * n[0] + c[1] * n[1] + c[2] * n[2], tt = [0, 1, 2].map(k => c[k] - cn * n[k]), tl = Math.hypot(...tt) || 1;
               J = [0, 1, 2].map(k => pw * ca * (n[k] + mu * tt[k] / tl)); }
        const r = [0, 1, 2].map(k => R * (-ca * c[k] + fx * sv[k] + fy * up[k]));
        const w = [r[1] * J[2] - r[2] * J[1], r[2] * J[0] - r[0] * J[2], r[0] * J[1] - r[1] * J[0]].map(x => 2.5 * x / (R * R));
        const vx = J[0], vz = J[2], sp = Math.hypot(vx, vz), vy0 = J[1] < 0 ? -J[1] * E_TABLE : J[1], vy = vy0 > 1.5 ? vy0 : 0;
        return { dir: [vx / sp, vz / sp], speed: sp, w, vy, grip };
    }
    const shotNow = () =>`);
rep('    window.__trick = {', '    window.__trick = { strikeRaw: strikeOf, strikeSlope, ballsNow: () => balls, ballOf, MU_TIP_: MU_TIP, D_: D,');
rep(`            if (us <= 3.5 * MU_S * h) {   // the slip is gone within this tick: the impulse −(2/7)·u, exactly
                b.vx -= 2 / 7 * ux; b.vz -= 2 / 7 * uz; b.wx += 5 / 7 * uz / b.r; b.wz -= 5 / 7 * ux / b.r;
            } else {`, `            if (us <= 3.5 * MU_S * h) {   // PEB run 2: it slides for the time tau the slip needs, then rolls for the rest of the tick
                const tau = us / (3.5 * MU_S);
                b.vx -= 2 / 7 * ux; b.vz -= 2 / 7 * uz; b.wx += 5 / 7 * uz / b.r; b.wz -= 5 / 7 * ux / b.r;
                let dx = b.vx * tau, dz = b.vz * tau;
                const sp = Math.hypot(b.vx, b.vz), rest = h - tau;
                if (sp > 0) { const ns = Math.max(0, sp - MU * rest); b.vx *= ns / sp; b.vz *= ns / sp; }
                b.wx = b.vz / b.r; b.wz = -b.vx / b.r;
                dx += b.vx * rest; dz += b.vz * rest;
                if (b.wy) { const d = MU_SP * h / b.r; b.wy = Math.abs(b.wy) <= d ? 0 : b.wy - Math.sign(b.wy) * d; }
                return [dx, dz];
            } else {`);
rep(`            } else cloth(b, h);
            b.x += b.vx * h; b.z += b.vz * h;`, `            } else { const d = cloth(b, h); if (d) { b.x += d[0] - b.vx * h; b.z += d[1] - b.vz * h; } }
            b.x += b.vx * h; b.z += b.vz * h;`);
const clothSince = `    // PEB run 3: the cloth from the moment of contact, for the time tau since it within this tick
    function clothSince(b, tau) {
        if (!(tau > 0) || b.sunk || b.y > 0 || b.vy > 0) return;
        const vx = b.vx, vz = b.vz, d = cloth(b, tau);
        if (d) { b.x += d[0] - vx * tau; b.z += d[1] - vz * tau; } else { b.x += (b.vx - vx) * tau; b.z += (b.vz - vz) * tau; }
    }
`;
rep('    function own(B, h, onSink, onRail) {', clothSince + '    function own(B, h, onSink, onRail) {');
rep(`                A.x += ft.ax * ra.tau; A.z += ft.az * ra.tau; Bb.x += ft.bx * rb.tau; Bb.z += ft.bz * rb.tau;   // moved with it since contact
            }`, `                A.x += ft.ax * ra.tau; A.z += ft.az * ra.tau; Bb.x += ft.bx * rb.tau; Bb.z += ft.bz * rb.tau;   // moved with it since contact
            }
            if (ra.hit) clothSince(A, ra.tau); if (rb.hit) clothSince(Bb, rb.tau);`);
rep(`                        b.vx -= Jt * ex; b.vz -= Jt * ez; b.wy -= 2.5 * Jt * (n[1] * ex - n[0] * ez) / b.r;
                    }
                }`, `                        b.vx -= Jt * ex; b.vz -= Jt * ez; b.wy -= 2.5 * Jt * (n[1] * ex - n[0] * ez) / b.r;
                    }
                    if (tau >= 0 && tau <= h) clothSince(b, tau);
                }`);
fs.writeFileSync('runs/peb/play-trick-slope3.html', src);

const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const port = srv.address().port;
const b = await chromium.launch(); const p = await b.newPage();
await p.addInitScript(() => {
  const TRIG = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2'];
  window.__cnt = { on: false, n: 0 };
  for (const k of TRIG) { const f = Math[k]; Math[k] = function (...a) { if (window.__cnt.on) window.__cnt.n++; return f.apply(Math, a); }; }
});
await p.goto(`http://localhost:${port}/runs/peb/play-trick-slope3.html`); await p.waitForFunction(() => window.__trick && window.__trick.strikeSlope);
const lines = [];
const say = s => { console.log(s); lines.push(s); };

// ---------------------------------------------------------------- P1 and P2
const r12 = await p.evaluate(() => {
  const T = window.__trick, C = window.__cnt, D = T.D_;
  const halve = t => t / (1 + Math.sqrt(1 + t * t)), add = (a, b) => (a + b) / (1 - a * b);
  // the lattice of half-slopes tan((k + 1/2) pi / N), k < N/2, by halving from the corner and tangent addition
  const lattice = N => { let b = 1, ang = 4; while (ang < 2 * N) { b = halve(b); ang *= 2; } const step = 2 * b / (1 - b * b), out = []; let cur = b;
    for (let k = 0; k < N / 4; k++) { out.push(cur); cur = add(cur, step); } for (let k = N / 4; k < N / 2; k++) out.push(1 / out[N / 2 - 1 - k]); return out; };
  const L = lattice(1 << 12);            // half-slopes of aims in (0, pi): a = 2 (k + 1/2) pi / 4096
  const sign = s => s.contacts.map(c => c.a + '-' + c.b).join(',') + '|' + s.cushions.map(c => c.n).join(',') + '|' + s.sunk.map(c => c.n + '@' + c.pocket).join(',');
  const fin = s => s.final.map(b => [b.sunk ? 0 : b.x, b.sunk ? 0 : b.z]).flat();
  let seed = 4242; const rnd = () => { seed = (seed * 1103515245 + 12345) >>> 0; return seed / 2 ** 32; };
  const out = { shots: 0, worst: 0, sameSeq: 0, trigMax: 0, list: [] };
  const one = (label, B) => {
    const k = Math.floor(rnd() * L.length), side = rnd() < 0.5 ? 1 : -1;
    const t = side * L[k], a = 2 * Math.atan(t);                         // the same aim, as a slope and as an angle
    const fx = 0.5 * (rnd() - 0.5), fy = 0.5 * (rnd() - 0.5), pw = 6 + 30 * rnd();
    const el = (label === 'jump' || label === 'masse') ? 20 + 40 * rnd() : 0, te = Math.tan(el * D / 2), elA = 2 * Math.atan(te);
    const sa = T.strikeRaw(a, fx, fy, pw, T.MU_TIP_, elA), A = T.simulate(B, sa.dir, sa.speed, sa.w, sa.vy);
    window.__slopeMode = true; C.n = 0; C.on = true;
    const ss = T.strikeSlope(t, fx, fy, pw, T.MU_TIP_, te), S = T.simulate(B, ss.dir, ss.speed, ss.w, ss.vy);
    C.on = false; window.__slopeMode = false;
    const fa = fin(A), fs = fin(S); let d = 0; for (let i = 0; i < fa.length; i++) d = Math.max(d, Math.abs(fa[i] - fs[i]));
    out.shots++; out.worst = Math.max(out.worst, d); if (sign(A) === sign(S)) out.sameSeq++; out.trigMax = Math.max(out.trigMax, C.n);
    out.list.push([label, d, sign(A) === sign(S), C.n, A.contacts.length]);
  };
  for (const Lay of ['rack', 'scatter', 'line', 'jump', 'masse']) for (let i = 0; i < 12; i++) { T.setLayout(Lay); one(Lay, T.ballsNow()); }
  for (const c of T.challenges) { T.setChallenge(c.id); one('ch:' + c.id, T.ballsNow()); }
  // P2: the degree round trip against lattice aims
  T.setLayout('rack'); const B = T.ballsNow(); let moved = 0, worstRT = 0, latticeDiff = 0;
  for (let i = 0; i < 60; i++) {
    const a = (rnd() * 2 - 1) * Math.PI, A = T.simulate(B, a, 20, null, 0), R2 = T.simulate(B, (a / D) * D, 20, null, 0);
    const fa = fin(A), fr = fin(R2); let d = 0; for (let j = 0; j < fa.length; j++) d = Math.max(d, Math.abs(fa[j] - fr[j]));
    worstRT = Math.max(worstRT, d); if (d > 1e-9) moved++;
    const k = Math.floor(rnd() * L.length), t1 = L[k], t2 = lattice(1 << 12)[k];      // recorded as (12, k), made again
    const u = t => [(1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)];
    const S1 = T.simulate(B, u(t1), 20, null, 0), S2 = T.simulate(B, u(t2), 20, null, 0);
    const f1 = fin(S1), f2 = fin(S2); for (let j = 0; j < f1.length; j++) if (f1[j] !== f2[j]) { latticeDiff++; break; }
  }
  out.p2 = { moved, worstRT, latticeDiff };
  return out;
});
say(`P1: ${r12.shots} shots; largest final-position difference slope vs angle ${r12.worst.toExponential(2)}; same contact sequence ${r12.sameSeq}/${r12.shots}; most trig calls in a slope shot ${r12.trigMax}`);
const bad = r12.list.filter(x => x[1] > 1e-9 || !x[2]); say(`   shots past 1e-9 or with another sequence: ${bad.length}` + (bad.length ? ' ' + JSON.stringify(bad.slice(0, 8)) : ''));
say('P1″ ' + (r12.worst <= 1e-9 && r12.sameSeq === r12.shots && r12.trigMax === 0 ? 'not killed' : 'KILLED'));
// say(`P2: degree round trip moved ${r12.p2.moved}/60 shots past 1e-9 (largest ${r12.p2.worstRT.toExponential(2)}); lattice aims made again differing: ${r12.p2.latticeDiff}/60`);


// ---------------------------------------------------------------- P3 and P4: the shot map
const maps = await p.evaluate(() => {
  const T = window.__trick;
  const sign = s => s.contacts.map(c => c.a + '-' + c.b).join(',') + '|' + s.cushions.map(c => c.n).join(',') + '|' + s.sunk.map(c => c.n + '@' + c.pocket).join(',');
  const ballContacts = s => s.contacts.length;
  const res = {};
  const layouts = {
    cut: () => [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)],
    tworail: () => { T.setChallenge('tworail'); return T.ballsNow().map(b => ({ ...b })); },
    rack: () => { T.setLayout('rack'); return T.ballsNow().map(b => ({ ...b })); },
  };
  for (const [name, mk] of Object.entries(layouts)) {
    const B = mk(), pw = 14, obj = B.find(b => !b.cue).n;
    const run = a => T.simulate(B, [Math.cos(a), Math.sin(a)], pw, null, 0);
    const outc = s => { const c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj); return [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z]; };
    const M = 1024, aims = [], sg = [];
    for (let j = 0; j < M; j++) { const a = (j + 0.5) * 2 * Math.PI / M; aims.push(a); sg.push(sign(run(a))); }
    const jumps = [];
    for (let j = 0; j < M; j++) {
      const j2 = (j + 1) % M; if (sg[j] === sg[j2]) continue;
      let lo = aims[j], hi = aims[j2] + (j2 === 0 ? 2 * Math.PI : 0), s0 = sg[j];
      for (let it = 0; it < 60 && hi - lo > 1e-12; it++) { const m = (lo + hi) / 2; if (sign(run(m)) === s0) lo = m; else hi = m; }
      jumps.push((lo + hi) / 2);
    }
    jumps.sort((x, y) => x - y);
    const pieces = [];
    const KS = [6, 8, 12, 16, 24, 32, 48, 64, 96, 128];
    for (let i = 0; i < jumps.length; i++) {
      const a0 = jumps[i], a1 = i + 1 < jumps.length ? jumps[i + 1] : jumps[0] + 2 * Math.PI;
      if (a1 - a0 < 1e-4) continue;
      const lo = a0 + 1e-10, hi = a1 - 1e-10, mid = (lo + hi) / 2, half = (hi - lo) / 2;
      const midS = run(mid), nb = ballContacts(midS);
      const test = []; for (let q = 0; q < 200; q++) { const a = lo + (hi - lo) * (q + 0.5) / 200; test.push([a, outc(run(a))]); }
      let kst = null;
      for (const K of KS) {
        const z = [], w = [], f = [];
        for (let k = 0; k < K; k++) { const th = (k + 0.5) * Math.PI / K; z.push(Math.cos(th)); w.push((k % 2 ? -1 : 1) * Math.sin(th)); f.push(outc(run(mid + half * Math.cos(th)))); }
        let err = 0;
        for (const [a, tr] of test) {
          const y = (a - mid) / half; let den = 0; const num = [0, 0, 0, 0];
          for (let k = 0; k < K; k++) { const q = w[k] / (y - z[k]); den += q; for (let c = 0; c < 4; c++) num[c] += q * f[k][c]; }
          for (let c = 0; c < 4; c++) err = Math.max(err, Math.abs(num[c] / den - tr[c]));
        }
        if (err <= 1e-6) { kst = K; break; }
      }
      pieces.push({ w: a1 - a0, contacts: nb, K: kst });
    }
    res[name] = { jumps: jumps.length, pieces };
  }
  return res;
});
let held = 0, tot = 0; const byC = {};
for (const [name, m] of Object.entries(maps)) {
  const ok = m.pieces.filter(x => x.K !== null).length; held += ok; tot += m.pieces.length;
  say(`P3 ${name}: ${m.jumps} jumps; ${m.pieces.length} pieces wider than 1e-4 rad; held to 1e-6 with K <= 128: ${ok}`);
  for (const x of m.pieces) (byC[x.contacts] = byC[x.contacts] || []).push(x.K === null ? 999 : x.K);
}
say('P3″ ' + (tot && held / tot >= 0.9 ? 'not killed' : 'KILLED') + ` (${held}/${tot})`);
const med = a => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
for (const c of Object.keys(byC).sort((a, b) => a - b)) say(`   ${c} ball contacts: ${byC[c].length} pieces, median K* ${med(byC[c])} (999 = more than 128)`);
const m1 = byC[1] && med(byC[1]), m2 = byC[2] && med(byC[2]), m3 = byC[3] && med(byC[3]);
say('P4″ ' + (m1 && m2 && m3 && m2 >= 1.5 * m1 && m3 >= 1.5 * m2 ? 'not killed' : 'KILLED') + ` (medians ${m1}, ${m2}, ${m3})`);

// P5: run 1's post hoc piece, the same 100,000 aims
const p5 = await p.evaluate(() => {
  const T = window.__trick; const B = [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)];
  const sim = a => { const s = T.simulate(B, [Math.cos(a), Math.sin(a)], 14, null, 0); const c = s.final.find(x => x.cue), o = s.final.find(x => !x.cue); return [c.x, c.z, o.x, o.z]; };
  const lo = 0.2260359421921734, hi = 0.2783714456225511, N = 100000, h = (hi - lo) / N;
  let prev = sim(lo + h / 2); const sizes = [];
  for (let j = 1; j < N; j++) { const cur = sim(lo + h * (j + 0.5)); sizes.push(Math.max(...cur.map((v, k) => Math.abs(v - prev[k])))); prev = cur; }
  const sorted = [...sizes].sort((a, b) => a - b), med = sorted[sorted.length >> 1];
  return { med, largest: sorted[sorted.length - 1], over: sizes.filter(d => d > 20 * med).length };
});
say(`P5: median step ${p5.med.toExponential(2)}, largest ${p5.largest.toExponential(2)}, steps past 20 x median ${p5.over}`);
say('P5″ ' + (p5.over === 0 ? 'not killed' : 'KILLED'));
fs.writeFileSync('runs/peb/peb-run3.txt', lines.join('\n') + '\n');
await b.close(); srv.close();
