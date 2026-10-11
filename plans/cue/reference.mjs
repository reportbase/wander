// CUE run 1, the reference's side, and the verdicts. The published laws as pooltool 0.6.0 states them (PyPI sdist,
// sha256 1915bfabd429603da12de0d3d55a15bc4147859b4585376dd12f7239c631e3b0, Apache-2.0), re-implemented here from its
// source text; the downloaded code is not run. node plans/cue/reference.mjs (reads plans/cue/cue-engine.txt)
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const D = Math.PI / 180, UNIT = 0.028575 / 0.45;            // one engine unit in metres (the ball's radius is 0.45)
const speeds = { slow: 7, medium: 21, fast: 49 };            // engine units a second
const ms = v => v * UNIT;

// ── the reference's constants (pooltool/objects/ball/params.py, "taken from or based off of" Alciatore's
//    physical-properties page) and its ball–ball friction (physics/resolve/ball_ball/friction.py: "Friction fit curve
//    u_b = a + b e^(-c v_rel) used in David Alciatore's TP A-14", the default resolver's choice) ──
const REF = { u_s: 0.2, u_r: 0.01, e_b: 0.95, e_c: 0.85, f_c: 0.2, R: 0.028575, cushionH: 0.64 * 2 * 0.028575 };
const muAlciatore = vrel => 9.951e-3 + 0.108 * Math.exp(-1.088 * vrel);   // vrel: the balls' relative surface speed, m/s

// throw from a cut, the frictional inelastic model (ball_ball/frictional_inelastic), in closed form for a white with no
// side spin meeting a still ball of the same mass: normal impulse (1 + e)/2·v·cos φ; the friction impulse along the
// contact points' relative sliding, capped at what stops it (each ball's contact point moves 7/2 per unit impulse, so
// 7 for the pair); the struck ball's direction is turned by the friction impulse's part along the table, over the normal.
//   stun: relative sliding v·sin φ, across the line of centres
//   rolling: the white's topspin adds v·cos φ downward at the contact point, so the sliding is v (|v_t| = v), and only its
//            share sin φ lies along the table
function throwDeg(phiDeg, v, rolling, mu, e) {
  const phi = phiDeg * D, Jn = (1 + e) / 2 * v * Math.cos(phi);
  const vrel = rolling ? v : v * Math.sin(phi), Jf = Math.min(mu(vrel) * Jn, vrel / 7);
  const along = rolling ? Math.sin(phi) : 1;
  return Math.atan(Jf * along / Jn) / D;
}

// the cushion: Han (2005), "Dynamics in carom and three cushion billiards", as ball_cushion/han_2005/model.py states it
// (eqs 14–23), with its e and mu from properties.py (both the constants e_c, f_c there)
function han2005(psiDeg, v, e = REF.e_c, mu = REF.f_c, R = REF.R, h = REF.cushionH) {
  const m = 1, psi = psiDeg * D, th = Math.asin(h / R - 1);
  // cushion frame: x into the cushion, y along it, z up; a ball rolling on the cloth (spin (−vy/R, vx/R, 0))
  let [vx, vy, vz] = [v * Math.cos(psi), v * Math.sin(psi), 0], [wx, wy, wz] = [-vy / R, vx / R, 0];
  const sx = vx * Math.sin(th) - vz * Math.cos(th) + R * wy;
  const sy = -vy - R * wz * Math.cos(th) + R * wx * Math.sin(th);
  const c = -vx * Math.cos(th), II = 2 / 5 * m * R * R, A = 7 / 2 / m, B = 1 / m;
  const PzE = -(1 + e) * c / B, s0 = Math.hypot(sx, sy), PzS = s0 / A;
  let PxE, PyE;
  if (PzS <= mu * PzE) { PxE = sx / A; PyE = sy / A; } else { PxE = mu * PzE * sx / s0; PyE = mu * PzE * sy / s0; }
  const PX = -PxE * Math.sin(th) - PzE * Math.cos(th), PY = PyE;
  vx += PX / m; vy += PY / m;
  return { out: Math.atan2(Math.abs(vy), Math.abs(vx)) / D, eN: Math.abs(vx) / (v * Math.cos(psi)) };
}
// the speed-dependent restitution written in properties.py after its return (so never used there):
const eHanFit = vn => Math.max(0.40, 0.50 + 0.257 * vn - 0.044 * vn * vn);

// ── the engine's side, as committed with the plan ──
const here = fileURLToPath(new URL('.', import.meta.url)), lines = readFileSync(here + 'cue-engine.txt', 'utf8').split('\n');
const eng = {}; for (const l of lines) { let m;
  if ((m = l.match(/^throw (stun|rolling) v(\d+)\s+(.*)$/))) eng[`${m[1]} ${m[2]}`] = m[3].trim().split(/\s+/).map(Number);
  else if ((m = l.match(/^cushion v(\d+) (.*)$/))) eng[`cushion ${m[1]}`] = JSON.parse(m[2]); }

// ── the reference's numbers at the plan's points ──
const cuts = [10, 20, 30, 45, 60];
console.log('throw (degrees) at cuts 10 20 30 45 60, the reference beside the engine');
for (const kind of ['stun', 'rolling']) for (const [name, v] of Object.entries(speeds)) {
  const ref = cuts.map(p => throwDeg(p, ms(v), kind === 'rolling', muAlciatore, REF.e_b));
  console.log(`  ${kind.padEnd(7)} ${name.padEnd(6)} (${ms(v).toFixed(2)} m/s)  ref ${ref.map(x => x.toFixed(2)).join('  ')}   engine ${eng[`${kind} ${v}`].join('  ')}`);
}
console.log('  (the reference\'s friction at half-ball, stun: ' + Object.entries(speeds).map(([n, v]) => `${n} ${muAlciatore(ms(v) * 0.5).toFixed(4)}`).join(', ') + '; rolling: ' + Object.entries(speeds).map(([n, v]) => `${n} ${muAlciatore(ms(v)).toFixed(4)}`).join(', ') + ')');
console.log('cushion, a rolling ball, Han 2005 (e 0.85, mu 0.2): out angle and eN, the reference beside the engine');
for (const [name, v] of Object.entries(speeds)) {
  const row = [15, 30, 45, 60].map((p, i) => { const r = han2005(p, ms(v)), en = eng[`cushion ${v}`][i];
    return `${p}°: ref ${r.out.toFixed(1)}° ${r.eN.toFixed(3)}  engine ${en ? en.out.toFixed(1) + '° ' + en.eN.toFixed(3) : '(not read)'}`; });
  console.log(`  ${name.padEnd(6)} ${row.join(' | ')}`);
}
console.log('  (with the speed-dependent restitution left unused in properties.py, at 15°: ' + Object.entries(speeds).map(([n, v]) => { const vn = ms(v) * Math.cos(15 * D); return `${n} e ${eHanFit(vn).toFixed(3)} eN ${han2005(15, ms(v), eHanFit(vn)).eN.toFixed(3)}`; }).join(', ') + ')');

// ── the verdicts, as the plan wrote them ──
const ref = (k, v, p) => throwDeg(p, ms(v), k === 'rolling', muAlciatore, REF.e_b);
const verdicts = [];
const say = (id, killed, text) => verdicts.push(`${id}: ${killed ? 'KILLED' : 'not killed'}. ${text}`);
{ const r = ref('stun', 7, 30), e = 3.43; say('P1', Math.abs(r - e) >= 1, `stun half-ball slow: reference ${r.toFixed(2)}° against the engine's ${e}° (within 1°)`); }
{ const r = ref('stun', 49, 30), e = 3.43; say('P2', Math.abs(r - e) >= 1, `stun half-ball fast: reference ${r.toFixed(2)}° against ${e}° (within 1°)`); }
{ const a = ref('stun', 7, 30), b = ref('stun', 49, 30); say('P3', Math.abs(a - b) >= 1, `the reference's stun half-ball throw changes ${(a - b).toFixed(2)}° from slow to fast (less than 1°)`); }
{ const r = ref('rolling', 21, 30), e = 1.73; say('P4', Math.abs(r - e) >= 1, `rolling half-ball medium: reference ${r.toFixed(2)}° against ${e}° (within 1°)`); }
{ const r = han2005(30, ms(21)); say('P5', Math.abs(r.out - 29.7) >= 5 || Math.abs(r.eN - 0.733) >= 0.1, `cushion, medium, 30° in: reference out ${r.out.toFixed(1)}° (engine 29.7°, within 5°), eN ${r.eN.toFixed(3)} (engine 0.733, within 0.1)`); }
{ const e15 = { 7: 0.618, 21: 0.74, 49: 0.774 }, rs = Object.values(speeds).map(v => [v, han2005(15, ms(v)).eN]);
  say('P6', rs.some(([v, r]) => Math.abs(r - e15[v]) >= 0.1), `cushion eN at 15°: ` + rs.map(([v, r]) => `v${v} reference ${r.toFixed(3)} engine ${e15[v]}`).join(', ') + ' (each within 0.1)'); }
{ const us = 30 / 154, ur = 1.2 / 154; say('P7', Math.abs(REF.u_s - us) >= 0.05 || ur / REF.u_r > 2 || REF.u_r / ur > 2, `cloth: sliding ${REF.u_s} against ${us.toFixed(3)} (within 0.05), rolling ${REF.u_r} against ${ur.toFixed(4)} (within a factor of 2)`); }
{ say('P8', Math.abs(REF.e_b - 0.96) >= 0.03, `ball–ball restitution ${REF.e_b} against 0.96 (within 0.03)`); }
console.log('\n' + verdicts.join('\n'));
