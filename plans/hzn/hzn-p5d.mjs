// HZN run 3 (P5d, P5e): directions J = P: the same page code at presentations P = 1024 … 8192; the excess of the geometric mean over the
// radius, and the worst miss against 2 sin(phi) more than four segments from the tangent.
import fs from 'fs'; import vm from 'vm';
const src = fs.readFileSync(process.argv[2], 'utf8');
const a = src.indexOf('const TVF = (function'), b = src.indexOf('// ── the shapes');
const ctx = { Math, Float64Array, Infinity, NaN, isFinite, console, globalThis: {} };
vm.createContext(ctx); vm.runInContext(src.slice(a, b) + '\nthis.LEVELS = LEVELS; this.TVF = TVF;', ctx);
const { LEVELS: LV, TVF } = ctx, N = 512, L = TVF.leafPositions(N);
const c = { x: Float64Array.from(L, p => Math.cos(p)), y: Float64Array.from(L, p => Math.sin(p)) };
const rows = [];
for (const P of [1024, 2048, 4096, 8192]) { const J = P;
  const { X, Y } = LV.present(c, P), ti = P / 4, O = { x: X[ti], y: Y[ti] };
  const { r } = LV.read(X, Y, O, J, ti), th0 = Math.atan2(O.y, O.x) + Math.PI / 2, seg = 2 * Math.PI / P;
  let worst = 0;
  for (let j = 0; j < J; j++) { if (!(r[j] > 0)) continue;
    const phi = (((2 * Math.PI * j / J - th0) % (2 * Math.PI)) + 2 * Math.PI) % (2 * Math.PI);
    if (Math.min(phi, Math.PI - phi) <= 4 * seg) continue;
    worst = Math.max(worst, Math.abs(r[j] - 2 * Math.sin(phi))); }
  rows.push({ P, excess: LV.geoMean(r) - 1, worst });
}
const factors = rows.slice(1).map((r, i) => rows[i].excess / r.excess);
const okB = factors.every(f => f >= 1.5 && f <= 2.5), okC = rows.every(r => r.worst < 1e-4);
for (const r of rows) console.log(`P = ${r.P}: geometric mean excess ${r.excess.toExponential(3)}, worst miss past four segments ${r.worst.toExponential(2)}`);
console.log(`P5d: ${okB ? 'not killed' : 'KILLED'}. excess falls by ${factors.map(f => f.toFixed(2)).join(', ')} per doubling`);
console.log(`P5e: ${okC ? 'not killed' : 'KILLED'}. worst miss past four segments under 1e-4 at every P: ${okC}`);
