// HZN P5: draw's gallery/levels.html LEVELS module, run in Node on a 512-leaf circle read from a place on its outline.
// The page's tvf.js bundle and LEVELS module are lifted out of the page file as they are (path given as argv[2]).
import fs from 'fs'; import vm from 'vm';
const src = fs.readFileSync(process.argv[2], 'utf8');
const a = src.indexOf('const TVF = (function'), b = src.indexOf('// ── the shapes');
const ctx = { Math, Float64Array, Infinity, NaN, isFinite, console, globalThis: {} };
vm.createContext(ctx); vm.runInContext(src.slice(a, b) + '\nthis.LEVELS = LEVELS; this.TVF = TVF;', ctx);
const { LEVELS: LV, TVF } = ctx, N = 512, L = TVF.leafPositions(N);
const c = { x: Float64Array.from(L, p => Math.cos(p)), y: Float64Array.from(L, p => Math.sin(p)) };
const { X, Y } = LV.present(c, 1024), ti = 256, O = { x: X[ti], y: Y[ti] }, J = 4096;
const { r } = LV.read(X, Y, O, J, ti);
// direction th from the standpoint; the tangent at O is perpendicular to O; phi measured from the tangent, inward
const th0 = Math.atan2(O.y, O.x) + Math.PI / 2;            // the tangent direction (counter-clockwise)
let worst = 0, met = 0;
for (let j = 0; j < J; j++) { if (!(r[j] > 0)) continue; met++;
  const th = 2 * Math.PI * j / J; let phi = ((th - th0) % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);   // 0..2π, inward is 0..π
  const want = 2 * Math.sin(phi); worst = Math.max(worst, Math.abs(r[j] - want)); }
const gm = LV.geoMean(r);
const ok = worst < 1e-3 && Math.abs(met / J - 0.5) < 0.01 && Math.abs(gm - 1) < 1e-3;
console.log(`P5: ${ok ? 'not killed' : 'KILLED'}. draw's LEVELS on a 512-leaf circle from its outline: readings within ${worst.toExponential(2)} of 2 sin(phi); walls met in ${(100 * met / J).toFixed(2)}% of directions; geometric mean ${gm.toFixed(6)} of the radius`);
