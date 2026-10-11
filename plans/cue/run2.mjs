// CUE run 2's verdicts: the engine with the fitted grip (cue-engine-run2.txt) against the reference's closed form
// (run 1's, reference.mjs), and the checks before and after (cue-checks-before.txt, cue-checks-after.txt).
// node plans/cue/run2.mjs
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
const here = fileURLToPath(new URL('.', import.meta.url)), D = Math.PI / 180, UNIT = 0.028575 / 0.45;
const mu = v => 9.951e-3 + 0.108 * Math.exp(-1.088 * v);
function throwDeg(phiDeg, v, rolling, e = 0.95) {   // as reference.mjs
  const phi = phiDeg * D, Jn = (1 + e) / 2 * v * Math.cos(phi), vrel = rolling ? v : v * Math.sin(phi), Jf = Math.min(mu(vrel) * Jn, vrel / 7);
  return Math.atan(Jf * (rolling ? Math.sin(phi) : 1) / Jn) / D; }
const eng = {}; for (const l of readFileSync(here + 'cue-engine-run2.txt', 'utf8').split('\n')) { const m = l.match(/^throw (stun|rolling) v(\d+)\s+(.*)$/); if (m) eng[`${m[1]} ${m[2]}`] = m[3].trim().split(/\s+/).map(Number); }
let worst = { d: 0 }; const cuts = [10, 20, 30, 45, 60];
for (const kind of ['stun', 'rolling']) for (const v of [7, 21, 49]) cuts.forEach((p, i) => { const r = throwDeg(p, v * UNIT, kind === 'rolling'), e = eng[`${kind} ${v}`][i], d = Math.abs(e - r);
  if (d > worst.d) worst = { d, at: `${kind} v${v} cut ${p}°: engine ${e}, reference ${r.toFixed(2)}` }; });
const read = f => Object.fromEntries(readFileSync(here + f, 'utf8').split('\n').filter(l => /^[a-zA-Z]+ -?[\d.]/.test(l)).map(l => l.split(' ')).map(([k, v]) => [k, +v]));
const ch = f => readFileSync(here + f, 'utf8').split('\n').filter(l => l.includes(': as set up'));
const b = read('cue-checks-before.txt'), a = read('cue-checks-after.txt'), chA = ch('cue-checks-after.txt');
const v = [];
v.push(`P9: ${worst.d >= 0.15 ? 'KILLED' : 'not killed'}. the engine's 30 throws against the reference's closed form: largest gap ${worst.d.toFixed(3)}° (${worst.at}) (under 0.15°)`);
v.push(`P10: ${Math.abs(a.cutThrow - 4.8) > 0.2 || Math.abs(a.sideThrow + 4.5) > 0.2 ? 'KILLED' : 'not killed'}. the smoke test's cut throw ${a.cutThrow.toFixed(2)}° (predicted 4.8 ± 0.2; before the change ${b.cutThrow.toFixed(2)}), side-spin throw ${a.sideThrow.toFixed(2)}° (predicted −4.5 ± 0.2; before ${b.sideThrow.toFixed(2)})`);
v.push(`P11: ${['follow', 'stun', 'draw'].some(k => a[k] !== b[k]) ? 'KILLED' : 'not killed'}. textbook results with the grip off: follow ${a.follow} (before ${b.follow}), stun ${a.stun} (${b.stun}), draw ${a.draw} (${b.draw})`);
v.push(`P12: ${chA.some(l => !/missed, reference shot solves it$/.test(l)) ? 'KILLED' : 'not killed'}. ${chA.filter(l => /missed, reference shot solves it$/.test(l)).length} of ${chA.length} challenges missed as set up and solved by their reference shot`);
console.log(`also: spin passed on ${b.passed.toFixed(2)} -> ${a.passed.toFixed(2)}, backspin passed ${b.backspinPassed.toFixed(2)} -> ${a.backspinPassed.toFixed(2)}, follow with the grip ${b.followGrip.toFixed(4)} -> ${a.followGrip.toFixed(4)}\n`);
console.log(v.join('\n'));
