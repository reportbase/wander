// PEB run 5 (plans/peb-plan.md): the full signature (grips' choices, phase ends, side spin's end) on run 4's event engine.
// node runs/peb/peb5-build.mjs; node runs/peb/peb5.mjs s1 | map cut | map tworail; node runs/peb/peb5.mjs report
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import http from 'http'; import fs from 'fs'; import path from 'path';
const part = process.argv[2], which = process.argv[3];
if (part === 'report') {
  const L = []; const say = s => { console.log(s); L.push(s); };
  const s1 = JSON.parse(fs.readFileSync('runs/peb/peb5-s1.json', 'utf8'));
  say(`S1: final state equal to run 4's engine bitwise on ${s1.same}/${s1.shots} shots; most trig calls ${s1.trigMax}`);
  say('S1 ' + (s1.same === s1.shots && s1.trigMax === 0 ? 'not killed' : 'KILLED'));
  let tot = 0, held = 0, rj = 0, rjHalf = 0, ne = 0, neOne = 0; const Ks = [];
  for (const name of ['cut', 'tworail']) {
    const m = JSON.parse(fs.readFileSync(`runs/peb/peb5-map-${name}.json`, 'utf8'));
    const hk = x => x.gl || x.gr ? x.Kb : x.K;
    const h = m.pieces.filter(x => hk(x) !== null); tot += m.pieces.length; held += h.length; h.forEach(x => Ks.push(hk(x)));
    const plain = m.ends.filter(e => !e.graze && e.slope !== null); ne += plain.length; neOne += plain.filter(e => Math.abs(e.slope - 1) <= 0.1).length;
    const rootJ = m.J.filter(j => j.graze); rj += rootJ.length;
    for (const j of rootJ) { const es = m.ends.filter(e => e.graze && e.slope !== null && (Math.abs(e.at - j.lo) < 1e-9 || Math.abs(e.at - j.hi) < 1e-9 || Math.abs(e.at - j.lo - 2 * Math.PI) < 1e-9 || Math.abs(e.at - j.hi - 2 * Math.PI) < 1e-9)); if (es.some(e => Math.abs(e.slope - 0.5) <= 0.1)) rjHalf++; }
    const kinds = {}; m.J.forEach(j => { const k = j.keys.map(x => x[0]).sort().join(''); kinds[k] = (kinds[k] || 0) + 1; });
    say(`${name}: ${m.jumps} jumps (${m.grazeJumps} a root's); ${m.pieces.length} pieces wider than 1e-4, held ${h.length}; first differing events by kind ${JSON.stringify(kinds)}`);
    say(`   not held: ${m.pieces.filter(x => hk(x) === null).map(x => x.e0.toFixed(6) + '..' + x.e1.toFixed(6) + (x.gl || x.gr ? ' (root chart)' : '')).join(', ') || 'none'}`);
    say(`   plain ends' slopes: ${plain.map(e => e.slope.toFixed(2)).join(' ')}`);
    say(`   root ends' slopes: ${m.ends.filter(e => e.graze && e.slope !== null).map(e => e.slope.toFixed(2)).join(' ') || '-'}`);
    if (name === 'tworail') {
      const w = m.J.filter(j => Math.abs(j.lo - 0.950) < 1e-3 && j.keys.some(k => k[0] === 'W'));
      const near = m.J.filter(j => j.lo > 0.714 && j.hi < 0.997);
      say(`S5: jumps inside 0.714..0.997: ${near.map(j => j.lo.toFixed(6) + ' ' + j.keys.join('/')).join('; ')}`);
      const ok = w.length > 0 && w.every(j => m.pieces.filter(x => Math.abs(x.e1 - j.lo) < 1e-9 || Math.abs(x.e0 - j.hi) < 1e-9).every(x => hk(x) !== null));
      say('S5 ' + (ok ? 'not killed' : 'KILLED'));
    }
  }
  say('S2 ' + (held / tot >= 0.9 ? 'not killed' : 'KILLED') + ` (${held}/${tot})`);
  say('S3 ' + (ne && neOne / ne >= 0.9 && (!rj || rjHalf / rj >= 0.8) ? 'not killed' : 'KILLED') + ` (plain ends at 1: ${neOne}/${ne}; root jumps with a side at 1/2: ${rjHalf}/${rj})`);
  const med = a => { const s = [...a].sort((x, y) => x - y); return s[Math.floor(s.length / 2)]; };
  say('S4 ' + (med(Ks) <= 12 ? 'not killed' : 'KILLED') + ` (median K* ${med(Ks)} over ${Ks.length})`);
  fs.writeFileSync('runs/peb/peb-run5.txt', L.join('\n') + '\n');
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
await p.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event5.html`); await p.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
if (part === 's1') {
  const p4 = await b.newPage(); p4.on('pageerror', e => console.log('page error', e.message));
  await p4.goto(`http://localhost:${srv.address().port}/runs/peb/play-trick-event.html`); await p4.waitForFunction(() => window.__trick && window.__trick.simulateEvent);
  const shots = pg => pg.evaluate(() => {
    const T = window.__trick, C = window.__cnt || { n: 0 };
    const halve = t => t / (1 + Math.sqrt(1 + t * t)), add = (a, b) => (a + b) / (1 - a * b);
    const lattice = N => { let b = 1, ang = 4; while (ang < 2 * N) { b = halve(b); ang *= 2; } const step = 2 * b / (1 - b * b), out = []; let cur = b;
      for (let k = 0; k < N / 4; k++) { out.push(cur); cur = add(cur, step); } for (let k = N / 4; k < N / 2; k++) out.push(1 / out[N / 2 - 1 - k]); return out; };
    const L = lattice(1 << 12); let seed = 4242; const rnd = () => { seed = (seed * 1103515245 + 12345) >>> 0; return seed / 2 ** 32; };
    const out = []; let trigMax = 0;
    for (const Lay of ['rack', 'scatter', 'line']) for (let i = 0; i < 12; i++) {
      T.setLayout(Lay); const B = T.ballsNow().map(b => ({ ...b }));
      const k = Math.floor(rnd() * L.length), side = rnd() < 0.5 ? 1 : -1, t = side * L[k];
      const fx = 0.5 * (rnd() - 0.5), fy = 0.5 * (rnd() - 0.5), pw = 6 + 30 * rnd();
      C.n = 0; C.on = true; const ss = T.strikeSlope(t, fx, fy, pw, T.MU_TIP_, 0); const E = T.simulateEvent(B, ss.dir, ss.speed, ss.w, ss.vy); C.on = false;
      trigMax = Math.max(trigMax, C.n); out.push(E.final.map(b => [b.n, b.sunk, b.x, b.z, b.vx, b.vz, b.wx, b.wy, b.wz]));
    }
    return { out, trigMax };
  });
  const A = await shots(p), B4 = await shots(p4);
  const same = A.out.filter((f, i) => JSON.stringify(f) === JSON.stringify(B4.out[i])).length;
  fs.writeFileSync('runs/peb/peb5-s1.json', JSON.stringify({ shots: A.out.length, same, trigMax: A.trigMax }));
  console.log('s1', same, '/', A.out.length, 'trig', A.trigMax);
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
      jumps.push({ lo, hi, graze: gs.length > 0 && Math.min(...gs) < 1e-3, keys: [A.ev[k], Bv.ev[k]].map(e => e ? e.key : '-') });
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
      pieces.push({ e0, e1, w: e1 - e0, contacts: nb, K, Kb, gl: J0.graze, gr: J1.graze });
      for (const [edge, dirn, gz] of [[e0, 1, J0.graze], [e1, -1, J1.graze]]) {
        const ref = outc(run(edge)), xs = [], ys = [];
        for (const d of [1e-9, 1e-8, 1e-7, 1e-6, 1e-5]) { const o = outc(run(edge + dirn * d)); const dv = Math.max(...o.map((v, q) => Math.abs(v - ref[q]))); if (dv > 0) { xs.push(Math.log(d)); ys.push(Math.log(dv)); } }
        let slope = null;
        if (xs.length >= 4) { const mx = xs.reduce((a, b) => a + b) / xs.length, my = ys.reduce((a, b) => a + b) / ys.length; let sxy = 0, sxx = 0; xs.forEach((x, q) => { sxy += (x - mx) * (ys[q] - my); sxx += (x - mx) ** 2; }); slope = sxy / sxx; }
        ends.push({ graze: gz, slope, at: edge, side: dirn });
      }
    }
    return { jumps: jumps.length, grazeJumps: jumps.filter(j => j.graze).length, J: jumps.map(j => ({ lo: j.lo, hi: j.hi, graze: j.graze, keys: j.keys })), pieces, ends };
  }, which);
  fs.writeFileSync(`runs/peb/peb5-map-${which}.json`, JSON.stringify(r));
  console.log('map', which, 'done');
}
await b.close(); srv.close();
