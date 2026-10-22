// POR run 1, P1–P3 (plans/por-plan.md), on POL's own engine (pool.html's script, read only, via loadpool.mjs).
// Usage: node runs/por/por1.mjs   (from the repository root)
import { loadPool } from './loadpool.mjs';
const out = []; const say = s => { out.push(s); console.log(s); };
const f = x => x.toExponential(3);

// ── P1: scale the world by k (lengths and speeds), clock fixed ──
function rackRun(P, i) {   // run 1's break i, heavy ball, 8 s: every reading pair (v, h) of the inside table, contacts, referee's end
  const R = P.rack(true), S = P.rack(true); P.strike(R, i); P.strike(S, i);
  const rd = []; let hits = 0;
  const log = (A, B, d, hit, va, vb) => { if (hit) hits++; else rd.push(va, vb); };
  for (let fr = 0; fr < 480; fr++) { P.stepRef(R); P.stepSit(S, log, true, null, Infinity, null); }
  return { rd: Float64Array.from(rd), hits, ref: R.map(b => [b.x, b.z, !!b.sunk]), sit: S.map(b => [b.x, b.z, !!b.sunk]) };
}
function fieldRun(P, seed) {
  const rd = []; let hits = 0;
  P.runField(seed, { seconds: 1, log: (A, B, d, hit, va, vb) => { if (hit) hits++; else rd.push(va, vb); } });
  return { rd: Float64Array.from(rd), hits };
}
const P1 = loadPool(1);
const base = { rack: [], field: [] };
for (let i = 0; i < 10; i++) base.rack.push(rackRun(P1, i));
for (let s = 1; s <= 5; s++) base.field.push(fieldRun(P1, s));
let p1ok = true;
for (const k of [2, 7, 1e-3]) {
  const P = loadPool(k); let rdMax = 0, lenBad = 0, hitBad = 0, refMax = 0, sunkBad = 0, bitwise = true;
  for (let i = 0; i < 10; i++) {
    const a = base.rack[i], b = rackRun(P, i);
    if (a.rd.length !== b.rd.length) lenBad++; if (a.hits !== b.hits) hitBad++;
    for (let q = 0; q < Math.min(a.rd.length, b.rd.length); q++) { const dd = Math.abs(a.rd[q] - b.rd[q]); if (dd) bitwise = false; rdMax = Math.max(rdMax, dd); }
    a.ref.forEach((r, j) => { const s = b.ref[j]; if (r[2] !== s[2]) sunkBad++; else if (!r[2]) { const dd = Math.hypot(s[0] / k - r[0], s[1] / k - r[1]); if (dd) bitwise = false; refMax = Math.max(refMax, dd); } });
  }
  let frMax = 0, flenBad = 0, fhitBad = 0;
  for (let s = 0; s < 5; s++) {
    const a = base.field[s], b = fieldRun(P, s + 1);
    if (a.rd.length !== b.rd.length) flenBad++; if (a.hits !== b.hits) fhitBad++;
    for (let q = 0; q < Math.min(a.rd.length, b.rd.length); q++) { const dd = Math.abs(a.rd[q] - b.rd[q]); if (dd) bitwise = false; frMax = Math.max(frMax, dd); }
  }
  const ok = k === 2 ? (bitwise && !lenBad && !hitBad && !flenBad && !fhitBad && !sunkBad)
    : (rdMax < 1e-9 && frMax < 1e-9 && refMax < 1e-9 * 20 && !lenBad && !hitBad && !flenBad && !fhitBad && !sunkBad);
  if (!ok) p1ok = false;
  say(`  k = ${k}: rack readings max |Δ| ${f(rdMax)}, field readings ${f(frMax)}, referee positions/k vs k = 1 ${f(refMax)}; ` +
      `count mismatches (rack readings, rack contacts, field readings, field contacts, sunk) ${lenBad}, ${hitBad}, ${flenBad}, ${fhitBad}, ${sunkBad}; bitwise ${bitwise}`);
}
const nR = base.rack.reduce((z, r) => z + r.rd.length / 2, 0), nF = base.field.reduce((z, r) => z + r.rd.length / 2, 0);
say(`P1: ${p1ok ? 'not killed' : 'KILLED'}. ${nR} rack and ${nF} field reading pairs compared at each k; contacts ${base.rack.reduce((z, r) => z + r.hits, 0)} and ${base.field.reduce((z, r) => z + r.hits, 0)}`);

// ── P2: the time corner moves under k ──
const med = a => { const s = [...a].sort((x, y) => x - y); return s[s.length >> 1]; };
const late = (P, c) => [0, 4, 9].map(i => P.runLate(i, { c, mode: 'carry', sub: 4, stopAtE: true }).E);
const Ek = { 1: P1 };
let p2ok = true; const E1 = {};
for (const c of [50, 100, 200, 400, 800]) E1[c] = late(P1, c);
for (const k of [2, 0.5]) {
  const P = loadPool(k);
  for (const c of [100, 200, 400]) {
    const e = late(P, c), ref = E1[c / k], rel = Math.max(...e.map((x, j) => Math.abs(x / k - ref[j]) / ref[j]));
    if (!(rel <= 1e-12)) p2ok = false;
    say(`  k = ${k}, c = ${c}: E/k ${e.map(x => f(x / k)).join(', ')} | k = 1, c = ${c / k}: ${ref.map(f).join(', ')} | largest relative difference ${f(rel)}; lateness ${(0.9 * k * 240 / c).toFixed(2)} ticks; median E/k ${f(med(e) / k)}`);
  }
}
const m1 = med(E1[200]), P2k = loadPool(2), m2 = med(late(P2k, 200)) / 2;
if (!(m1 < 1e-3 && m2 > 1e-2)) p2ok = false;
say(`P2: ${p2ok ? 'not killed' : 'KILLED'}. at c = 200: median E/k ${f(m1)} at k = 1 (1.08 ticks), ${f(m2)} at k = 2 (2.16 ticks)`);

// ── P3: ignoring by size against ignoring by one reading (addresses spent) ──
const vc = rho => rho / (1 + rho), vStar = K => Math.sqrt(vc(2 ** -K) * vc(2 ** -(K - 1)));
let p3ok = true, excess = 0;
for (const K of [1, 2, 3]) {
  const vs = vStar(K); let dis = 0, n = 0;
  const sizeRule = (A, B, ia, ib) => { const s = (B.lv || 0) - (A.lv || 0) >= K, a = ia.v <= vs; n++; if (s !== a) dis++;
    excess = Math.max(excess, Math.log2(ia.v + ib.v)); return s; };
  const addrRule = (A, B, ia) => ia.v <= vs;
  const ES = [], EA = [], SK = [], SA = [];
  for (let s = 1; s <= 5; s++) { const a = P1.runField(s, { K: sizeRule, seconds: 1 }), b = P1.runField(s, { K: addrRule, seconds: 1 });
    ES.push(a.E[0]); EA.push(b.E[0]); SK.push(a.skipped); SA.push(b.skipped); }
  const same = ES.every((x, j) => Object.is(x, EA[j])) && SK.every((x, j) => x === SA[j]);
  if (dis || !same) p3ok = false;
  say(`  K = ${K}: v* = ${vs.toFixed(5)}; decisions compared ${n}, differing ${dis}; skipped (size) ${SK.join(',')} (address) ${SA.join(',')}; level-0 E size ${ES.map(f).join(', ')}; address ${EA.map(f).join(', ')}; identical ${same}`);
}
say(`P3: ${p3ok ? 'not killed' : 'KILLED'}. measured: the largest reading at a pushing response over its contact value, log2(h + v), ${excess.toFixed(4)} levels`);
// addresses spent at contact, per level smaller (a full turn of K_addr addresses), against the share skipped
for (const j of [1, 2, 3]) { const v = vc(2 ** -j); say(`  j = ${j}: v at contact ${v.toFixed(5)}, half-span ${(Math.asin(v) * 180 / Math.PI).toFixed(3)}°, share of a full turn ${(Math.asin(v) / Math.PI).toFixed(5)}, momentum share skipped (1+e)/(1+8^j) ${(1.96 / (1 + 8 ** j)).toFixed(5)}`); }
import fs from 'fs'; fs.writeFileSync('runs/por/por-run1-engine.txt', out.join('\n') + '\n');
