// PEB run 4 (plans/peb-plan.md): the event-driven copy against the tick, and its shot maps.
// node runs/peb/peb4-build.mjs; then node runs/peb/peb4.mjs q125 | map cut | map tworail | map rack; then node runs/peb/peb4.mjs report
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const part = process.argv[2], which = process.argv[3];
if (part === 'report') {
  const L = []; const say = s => { console.log(s); L.push(s); };
  const q = JSON.parse(fs.readFileSync('runs/peb/peb4-q125.json', 'utf8'));
  say(`Q1: ${q.shots} shots, ${q.off} left the cloth (excluded), ${q.used} compared`);
  say(`   median final-position difference event vs tick: SUB 4 ${q.med[0].toExponential(2)}, SUB 16 ${q.med[1].toExponential(2)}, SUB 64 ${q.med[2].toExponential(2)}; ratios ${(q.med[0] / q.med[1]).toFixed(2)}, ${(q.med[1] / q.med[2]).toFixed(2)}`);
  say(`   same signature at SUB 64: ${q.same64}/${q.used}; same contact pairs ignoring repeats: ${q.sameDedup64}/${q.used}`);
  say(`   by layout, median at SUB 4/16/64: ${Object.entries(q.byLay).map(([k, v]) => k + ' ' + v.map(x => x.toExponential(1)).join('/')).join('; ')}`);
  const q1 = q.med[0] / q.med[1] >= 3 && q.med[1] / q.med[2] >= 3 && q.same64 >= 30;
  say('Q1 ' + (q1 ? 'not killed' : 'KILLED'));
  say(`Q2: median step ${q.q2.med.toExponential(2)}, largest ${q.q2.largest.toExponential(2)}, steps past 20 x median ${q.q2.over}`);
  say('Q2 ' + (q.q2.over === 0 && q.q2.largest < 1e-4 ? 'not killed' : 'KILLED'));
  say(`Q5: most trig calls on the event path ${q.trigMax} over ${q.used} shots`);
  say('Q5 ' + (q.trigMax === 0 ? 'not killed' : 'KILLED'));
  let tot = 0, held = 0, gEnds = 0, gHalf = 0, nEnds = 0, nOne = 0, gp = 0, gpHeld = 0; const byC = {};
  for (const name of ['cut', 'tworail', 'rack']) {
    const m = JSON.parse(fs.readFileSync(`runs/peb/peb4-map-${name}.json`, 'utf8'));
    const h = m.pieces.filter(x => x.K !== null).length; tot += m.pieces.length; held += h;
    const ge = m.ends.filter(e => e.graze && e.slope !== null), ne = m.ends.filter(e => !e.graze && e.slope !== null);
    gEnds += ge.length; gHalf += ge.filter(e => Math.abs(e.slope - 0.5) <= 0.1).length; nEnds += ne.length; nOne += ne.filter(e => Math.abs(e.slope - 1) <= 0.1).length;
    const gpcs = m.pieces.filter(x => x.gl || x.gr); gp += gpcs.length; gpHeld += gpcs.filter(x => x.Kb !== null).length;
    say(`${name}: ${m.jumps} jumps (${m.grazeJumps} at a graze); ${m.pieces.length} pieces wider than 1e-4 rad, held ${h}; graze-ended pieces ${gpcs.length}, held in the root's chart ${gpcs.filter(x => x.Kb !== null).length}`);
    say(`   end slopes, graze: ${ge.map(e => e.slope.toFixed(2)).join(' ') || '-'}`);
    say(`   end slopes, not graze: ${ne.map(e => e.slope.toFixed(2)).join(' ') || '-'}`);
    for (const x of m.pieces) { const k = x.K !== null ? x.K : x.Kb; if (k !== null && k !== undefined) (byC[x.contacts] = byC[x.contacts] || []).push(k); }
  }
  say('Q3 ' + (tot && held / tot >= 0.9 ? 'not killed' : 'KILLED') + ` (${held}/${tot})`);
  say('Q3a ' + (gEnds && gHalf / gEnds >= 0.8 && (!nEnds || nOne / nEnds >= 0.8) ? 'not killed' : 'KILLED') + ` (graze ends at ½: ${gHalf}/${gEnds}; other ends at 1: ${nOne}/${nEnds})`);
  say('Q3b ' + (gp && gpHeld / gp >= 0.9 ? 'not killed' : 'KILLED') + ` (${gpHeld}/${gp})`);
  const med = a => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
  for (const c of Object.keys(byC).sort((a, b) => a - b)) say(`   ${c} ball contacts: ${byC[c].length} held pieces, median K* ${med(byC[c])}`);
  const m1 = byC[1] && med(byC[1]), m2 = byC[2] && med(byC[2]), m3 = byC[3] && med(byC[3]);
  say('Q4 ' + (m1 && m2 && m3 && m2 >= 1.5 * m1 && m3 >= 1.5 * m2 ? 'not killed' : 'KILLED') + ` (medians ${m1}, ${m2}, ${m3})`);
  fs.writeFileSync('runs/peb/peb-run4.txt', L.join('\n') + '\n');
  process.exit(0);
}
const root = path.resolve('.');
const srv = http.createServer((q, r) => { const f = path.join(root, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': 'text/html' }); r.end(d); } }); }).listen(0);
const b = await chromium.launch(); const p = await b.newPage(); p.on('pageerror', e => console.log('page error', e.message));
await p.addInitScript(() => {
  const TRIG = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'atan2'];
  window.__cnt = { on: false, n: 0 };
  for (const k of TRIG) { const f = Math[k]; Math[k] = function (...a) { if (window.__cnt.on) window.__cnt.n++; return f.apply(Math, a); }; }
});
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event.html`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
if (part === 'q125') {
  const r = await p.evaluate(() => {
    const T = window.__trick, C = window.__cnt;
    const halve = t => t / (1 + Math.sqrt(1 + t * t)), add = (a, b) => (a + b) / (1 - a * b);
    const lattice = N => { let b = 1, ang = 4; while (ang < 2 * N) { b = halve(b); ang *= 2; } const step = 2 * b / (1 - b * b), out = []; let cur = b;
      for (let k = 0; k < N / 4; k++) { out.push(cur); cur = add(cur, step); } for (let k = N / 4; k < N / 2; k++) out.push(1 / out[N / 2 - 1 - k]); return out; };
    const L = lattice(1 << 12);
    const sign = s => s.contacts.map(c => c.a + '-' + c.b).join(',') + '|' + s.cushions.map(c => c.n).join(',') + '|' + s.sunk.map(c => c.n + '@' + c.pocket).join(',');
    const pairsOnly = s => { const out = []; for (const c of s.contacts) { const k = Math.min(c.a, c.b) + '-' + Math.max(c.a, c.b); if (out[out.length - 1] !== k) out.push(k); } return out.join(','); };
    const diff = (E, S) => { let d = 0; E.final.forEach((b, i) => { const c = S.final[i]; if (b.sunk !== c.sunk) d = Infinity; else if (!b.sunk) d = Math.max(d, Math.hypot(b.x - c.x, b.z - c.z)); }); return d; };
    let seed = 4242; const rnd = () => { seed = (seed * 1103515245 + 12345) >>> 0; return seed / 2 ** 32; };
    const rows = []; let off = 0, trigMax = 0;
    for (const Lay of ['rack', 'scatter', 'line']) for (let i = 0; i < 12; i++) {
      T.setLayout(Lay); const B = T.ballsNow().map(b => ({ ...b }));
      const k = Math.floor(rnd() * L.length), side = rnd() < 0.5 ? 1 : -1, t = side * L[k];
      const fx = 0.5 * (rnd() - 0.5), fy = 0.5 * (rnd() - 0.5), pw = 6 + 30 * rnd();
      C.n = 0; C.on = true; const ss = T.strikeSlope(t, fx, fy, pw, T.MU_TIP_, 0); const E = T.simulateEvent(B, ss.dir, ss.speed, ss.w, ss.vy); C.on = false;
      if (E.offCloth) { off++; continue; }
      trigMax = Math.max(trigMax, C.n);
      const row = { Lay, d: [] };
      for (const s of [4, 16, 64]) { T.setSub(s); const S = T.simulate(B, ss.dir, ss.speed, ss.w, ss.vy); row.d.push(diff(E, S)); if (s === 64) { row.same = sign(E) === sign(S); row.sameD = pairsOnly(E) === pairsOnly(S) && sign(E).split('|').slice(1).join('|') === sign(S).split('|').slice(1).join('|'); } }
      T.setSub(4); rows.push(row);
    }
    const med = a => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
    const byLay = {}; for (const Lay of ['rack', 'scatter', 'line']) { const rs = rows.filter(r => r.Lay === Lay); byLay[Lay] = [0, 1, 2].map(i => med(rs.map(r => r.d[i]))); }
    // Q2
    const Bc = [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)];
    const sim = a => { const s = T.simulateEvent(Bc, [Math.cos(a), Math.sin(a)], 14, null, 0); const c = s.final.find(x => x.cue), o = s.final.find(x => !x.cue); return [c.x, c.z, o.x, o.z]; };
    const lo = 0.2260359421921734, hi = 0.2783714456225511, N = 100000, h = (hi - lo) / N;
    let prev = sim(lo + h / 2); const sizes = [];
    for (let j = 1; j < N; j++) { const cur = sim(lo + h * (j + 0.5)); sizes.push(Math.max(...cur.map((v, q) => Math.abs(v - prev[q])))); prev = cur; }
    const sorted = [...sizes].sort((a, b) => a - b), m2 = sorted[sorted.length >> 1];
    return { shots: 36, off, used: rows.length, med: [0, 1, 2].map(i => med(rows.map(r => r.d[i]))), same64: rows.filter(r => r.same).length, sameDedup64: rows.filter(r => r.sameD).length, byLay, trigMax,
      q2: { med: m2, largest: sorted[sorted.length - 1], over: sizes.filter(d => d > 20 * m2).length } };
  });
  fs.writeFileSync('runs/peb/peb4-q125.json', JSON.stringify(r));
  console.log('q125 done');
}
if (part === 'map') {
  const r = await p.evaluate((name) => {
    const T = window.__trick;
    const layouts = {
      cut: () => [T.ballOf(0, -5, 0), T.ballOf(1, 0, 1.2)],
      tworail: () => { T.setChallenge('tworail'); return T.ballsNow().map(b => ({ ...b })); },
      rack: () => { T.setLayout('rack'); return T.ballsNow().map(b => ({ ...b })); },
    };
    const B = layouts[name](), pw = 14, obj = B.find(b => !b.cue).n;
    const run = a => T.simulateEvent(B, [Math.cos(a), Math.sin(a)], pw, null, 0);
    const sig = s => s.ev.map(e => e.key).join(' ');
    const outc = s => { const c = s.final.find(b => b.cue), o = s.final.find(b => b.n === obj); return [c.sunk ? 0 : c.x, c.sunk ? 0 : c.z, o.sunk ? 0 : o.x, o.sunk ? 0 : o.z]; };
    const M = 1024, aims = [], sg = [];
    for (let j = 0; j < M; j++) { const a = (j + 0.5) * 2 * Math.PI / M; aims.push(a); sg.push(sig(run(a))); }
    const jumps = [];
    for (let j = 0; j < M; j++) {
      const j2 = (j + 1) % M; if (sg[j] === sg[j2]) continue;
      let lo = aims[j], hi = aims[j2] + (j2 === 0 ? 2 * Math.PI : 0); const s0 = sg[j];
      for (let it = 0; it < 60 && hi - lo > 1e-12; it++) { const m = (lo + hi) / 2; if (sig(run(m)) === s0) lo = m; else hi = m; }
      const A = run(lo), Bv = run(hi); let k = 0; while (k < A.ev.length && k < Bv.ev.length && A.ev[k].key === Bv.ev[k].key) k++;
      const gs = [A.ev[k], Bv.ev[k]].filter(Boolean).map(e => e.g);
      jumps.push({ lo, hi, graze: gs.length > 0 && Math.min(...gs) < 1e-3 });
    }
    jumps.sort((x, y) => x.lo - y.lo);
    const KS = [6, 8, 12, 16, 24, 32, 48, 64, 96, 128];
    // a bridge on the piece in a chart a = A(y), y in [-1, 1]; test points uniform in a
    const bridge = (A, Ainv, a0, a1) => {
      const test = []; for (let q = 0; q < 200; q++) { const a = a0 + (a1 - a0) * (q + 0.5) / 200; test.push([Ainv(a), outc(run(a))]); }
      for (const K of KS) {
        const z = [], w = [], f = [];
        for (let k = 0; k < K; k++) { const th = (k + 0.5) * Math.PI / K, y = Math.cos(th); z.push(y); w.push((k % 2 ? -1 : 1) * Math.sin(th)); f.push(outc(run(A(y)))); }
        let err = 0;
        for (const [y, tr] of test) { let den = 0; const num = [0, 0, 0, 0]; for (let k = 0; k < K; k++) { const q = w[k] / (y - z[k]); den += q; for (let c = 0; c < 4; c++) num[c] += q * f[k][c]; } for (let c = 0; c < 4; c++) err = Math.max(err, Math.abs(num[c] / den - tr[c])); }
        if (err <= 1e-6) return K;
      }
      return null;
    };
    const pieces = [], ends = [];
    for (let i = 0; i < jumps.length; i++) {
      const J0 = jumps[i], J1 = i + 1 < jumps.length ? jumps[i + 1] : { ...jumps[0], lo: jumps[0].lo + 2 * Math.PI, hi: jumps[0].hi + 2 * Math.PI };
      const e0 = J0.hi, e1 = J1.lo;   // the piece's own side of each bracket
      if (e1 - e0 < 1e-4) continue;
      const mid = (e0 + e1) / 2, half = (e1 - e0) / 2, nb = run(mid).contacts.length;
      const lo = e0 + 1e-10, hi = e1 - 1e-10, m0 = (lo + hi) / 2, h0 = (hi - lo) / 2;
      const K = bridge(y => m0 + h0 * y, a => (a - m0) / h0, lo, hi);
      let Kb = null;
      if (J0.graze || J1.graze) {
        const W = e1 - e0;
        if (J0.graze && J1.graze) {
          const A = y => mid + half * (3 * y - y * y * y) / 2;
          const Ainv = a => { let l = -1, h = 1; for (let k = 0; k < 80; k++) { const m = (l + h) / 2; if (A(m) < a) l = m; else h = m; } return (l + h) / 2; };
          Kb = bridge(A, Ainv, e0, e1);
        } else if (J0.graze) Kb = bridge(y => e0 + W * ((y + 1) / 2) ** 2, a => 2 * Math.sqrt(Math.max(0, (a - e0) / W)) - 1, e0, e1);
        else Kb = bridge(y => e1 - W * ((1 - y) / 2) ** 2, a => 1 - 2 * Math.sqrt(Math.max(0, (e1 - a) / W)), e0, e1);
      }
      pieces.push({ w: e1 - e0, contacts: nb, K, Kb, gl: J0.graze, gr: J1.graze });
      for (const [edge, dirn, gz] of [[e0, 1, J0.graze], [e1, -1, J1.graze]]) {
        const ref = outc(run(edge)), xs = [], ys = [];
        for (const d of [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]) { const o = outc(run(edge + dirn * d)); const dv = Math.max(...o.map((v, q) => Math.abs(v - ref[q]))); if (dv > 0) { xs.push(Math.log(d)); ys.push(Math.log(dv)); } }
        let slope = null;
        if (xs.length >= 4) { const mx = xs.reduce((a, b) => a + b) / xs.length, my = ys.reduce((a, b) => a + b) / ys.length; let sxy = 0, sxx = 0; xs.forEach((x, q) => { sxy += (x - mx) * (ys[q] - my); sxx += (x - mx) ** 2; }); slope = sxy / sxx; }
        ends.push({ graze: gz, slope });
      }
    }
    return { jumps: jumps.length, grazeJumps: jumps.filter(j => j.graze).length, pieces, ends };
  }, which);
  fs.writeFileSync(`runs/peb/peb4-map-${which}.json`, JSON.stringify(r));
  console.log('map', which, 'done');
}
await b.close(); srv.close();
