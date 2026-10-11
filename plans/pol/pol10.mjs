// POL run 10 (plans/pol-plan.md): level of detail by time to contact. A larger ball ignores a smaller one by the kick it
// would bring, read from v, h and two looks (Lee's τ = v/v̇), against ignoring by size (run 6) and by τ alone, with the work
// saved matched. Usage: node plans/pol/pol10.mjs
import { chromium } from 'playwright';
import { fileURLToPath } from 'url';
import path from 'path';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(String(e)));
await p.goto('file://' + path.join(root, 'pool.html'));
const res = await p.evaluate(() => {
  const P = window.__pool, e = 0.96, TICK = 1 / 240, SEEDS = [1, 2, 3, 4, 5];
  // each ball's last two looks at each other ball: its reading v now and a tick ago
  function looker() {
    const M = new Map();
    const log = (A, B, d, hit, va, vb) => { if (hit) return; let m = M.get(A); if (!m) M.set(A, m = new Map()); let s = m.get(B); if (!s) m.set(B, s = [NaN, NaN, NaN, NaN]);
      s[0] = s[1]; s[1] = va; s[2] = s[3]; s[3] = vb; };
    const looks = (a, b) => { let s = M.get(a); s = s && s.get(b); if (s) return [s[0], s[1]]; s = M.get(b); s = s && s.get(a); return s ? [s[2], s[3]] : [NaN, NaN]; };
    return { log, looks };
  }
  // the kick a reads from its own readings: (1 + e)·ρ³/(1 + ρ³)/(h·τ), ρ = v/h, τ = v/v̇ from two looks; in a's radii per second
  function read(L, a, b, ia, ib) {
    const [v0, v1] = L.looks(a, b), v = ia.v, h = ib.v, rho = v / h;
    if (!isFinite(v0)) return { kick: Infinity, tau: 0 };                 // one look only: cannot read a rate, so attend
    const rate = (v1 - v0) / TICK / v1;                                  // v̇/v
    if (!(rate > 0)) return { kick: 0, tau: Infinity };                  // not growing in view
    const tau = 1 / rate; return { kick: (1 + e) * rho ** 3 / (1 + rho ** 3) / (h * tau), tau };
  }
  const smaller = (ia, ib) => ia.v < 0.75 * ib.v;                       // read as smaller (sizes are halvings): never an equal or larger ball
  // play the five fields under a rule; the rule is each ball's own, applied at each of its contact responses
  function play(make) {
    const out = SEEDS.map(sd => {
      const L = looker(), st = { kick0: 0, byJ: [0, 0, 0, 0] };
      const rule = make(L, st);
      const r = P.runField(sd, { K: rule, log: L.log });
      return { E: r.E, skipped: r.skipped, hits: r.hits, kick0: st.kick0, byJ: st.byJ };
    });
    return { E0: med(out.map(o => o.E[0])), E: [0, 1, 2, 3].map(k => med(out.map(o => o.E[k]))), skipped: out.reduce((z, o) => z + o.skipped, 0),
      hits: out.reduce((z, o) => z + o.hits, 0), kick0: med(out.map(o => o.kick0)), byJ: [0, 1, 2, 3].map(j => out.reduce((z, o) => z + o.byJ[j], 0)), perField: out.map(o => o.E[0]) };
  }
  function med(L) { const s = [...L].sort((x, y) => x - y); return s[2]; }
  // a skip, tallied: the level-0 reader's skipped change of speed (an amount: own units times its radius), and how many levels smaller
  const note = (st, a, b, ra) => { if (a.lv === 0) st.kick0 += Math.hypot(...ra.du) * a.r; st.byJ[b.lv - a.lv]++; };
  const S = K => (L, st) => (a, b, ia, ib, ra) => { const k = (b.lv - a.lv) >= K; if (k) note(st, a, b, ra); return k; };   // the reading v/h ≤ 2^(−K)
  const Mr = eps => (L, st) => (a, b, ia, ib, ra) => { const k = smaller(ia, ib) && read(L, a, b, ia, ib).kick < eps; if (k) note(st, a, b, ra); return k; };
  const Tr = ts => (L, st) => (a, b, ia, ib, ra) => { const k = smaller(ia, ib) && read(L, a, b, ia, ib).tau > ts; if (k) note(st, a, b, ra); return k; };
  // the value of ε or τ* whose total skips over the five fields come nearest the target (bisection in logs, one value for all fields)
  function match(mk, target, lo, hi, rising) {
    let best = null;
    for (let it = 0; it < 28; it++) {
      const x = Math.sqrt(lo * hi), r = play(mk(x));
      if (!best || Math.abs(r.skipped - target) < Math.abs(best.r.skipped - target)) best = { x, r };
      if (r.skipped === target) break;
      if ((r.skipped < target) === rising) lo = x; else hi = x;
    }
    return best;
  }
  // P25: in the true game, every response of a ball to a smaller one: the kick read from two looks against the response
  const L0 = looker(), cmp = [];
  P.runField(1, { K: Infinity, log: L0.log, each: (a, b, ra) => { const ia = P.image(a, b), ib = P.image(b, a); if (!smaller(ia, ib)) return;
    const k = read(L0, a, b, ia, ib).kick, du = Math.hypot(...ra.du); cmp.push(k / du); } });
  for (const sd of [2, 3, 4, 5]) { const L = looker(); P.runField(sd, { K: Infinity, log: L.log, each: (a, b, ra) => { const ia = P.image(a, b), ib = P.image(b, a); if (!smaller(ia, ib)) return;
    const k = read(L, a, b, ia, ib).kick, du = Math.hypot(...ra.du); cmp.push(k / du); } }); }
  const out = { cmp, rules: {} };
  for (const K of [1, 2, 3]) {
    const s = play(S(K)), m = K === 1 ? null : match(Mr, s.skipped, 1e-4, 1e4, true), t = K === 1 ? null : match(Tr, s.skipped, 1e-5, 1e5, false);
    out.rules[K] = { S: s, M: m && { eps: m.x, ...m.r }, T: t && { tau: t.x, ...t.r } };
  }
  return out;
});
await b.close();
if (errs.length) { console.log('page errors', errs); process.exit(1); }
const f = x => isFinite(x) ? x.toExponential(2) : 'sunk differs';
const within = (n, target) => Math.abs(n - target) <= Math.max(2, 0.02 * target);
const c = res.cmp, ok = c.filter(x => Math.abs(x - 1) <= 0.1).length, srt = [...c].sort((x, y) => x - y), q = k => srt[Math.floor(k * (srt.length - 1))];
console.log(`P25: the kick read from v, h and two looks over the response it would skip, ${c.length} responses to smaller balls, five fields, 1 s, nothing ignored`);
console.log(`  ratio: median ${q(0.5).toFixed(4)}, 5% ${q(0.05).toFixed(4)}, 95% ${q(0.95).toFixed(4)}; within 10%: ${ok} of ${c.length} (${(100 * ok / c.length).toFixed(1)}%)`);
console.log(`P25: ${ok >= 0.9 * c.length ? 'not killed' : 'KILLED'}. within 10% at ${(100 * ok / c.length).toFixed(1)}% of responses (90% needed)\n`);
console.log('fields of 116 balls, white struck at 14; level-0 error against the referee at 1 s (median of five); skips are contact responses, total over the five fields');
const line = (name, r, x) => `  ${name.padEnd(22)} skipped ${String(r.skipped).padStart(4)} of ${String(r.hits).padStart(4)}   E level 0 ${f(r.E0)}  (all levels ${r.E.map(f).join(', ')})   level-0 skipped kick ${f(r.kick0)}   skips by levels smaller 1/2/3: ${r.byJ.slice(1).join('/')}${x || ''}`;
for (const K of [1, 2, 3]) {
  const R = res.rules[K];
  console.log(`K = ${K}`); console.log(line(`S(${K}), size`, R.S));
  if (R.M) console.log(line(`M(ε = ${R.M.eps.toPrecision(3)}), kick`, R.M, within(R.M.skipped, R.S.skipped) ? '' : '   (work not matched)'));
  if (R.T) console.log(line(`T(τ* = ${R.T.tau.toPrecision(3)} s), τ`, R.T, within(R.T.skipped, R.S.skipped) ? '' : '   (work not matched)'));
  console.log(`    per field, level 0: S ${R.S.perField.map(f).join(', ')}${R.M ? `\n                        M ${R.M.perField.map(f).join(', ')}\n                        T ${R.T.perField.map(f).join(', ')}` : ''}`);
}
for (const K of [2, 3]) {
  const R = res.rules[K], mOK = within(R.M.skipped, R.S.skipped), tOK = within(R.T.skipped, R.S.skipped), fac = R.S.E0 / R.M.E0;
  console.log(`P26 at K = ${K}: ${!mOK ? 'UNDECIDED (work not matched)' : fac >= 1.5 ? 'not killed' : 'KILLED'}. S/M level-0 error ${fac.toFixed(2)} (at least 1.5)`);
  console.log(`P27 at K = ${K}: ${!(mOK && tOK) ? 'UNDECIDED (work not matched)' : R.T.E0 > R.M.E0 ? 'not killed' : 'KILLED'}. T ${f(R.T.E0)} against M ${f(R.M.E0)} (T higher)`);
}
