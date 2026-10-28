// What "computers can't hold infinity" means operationally (essay 12 §9, OFS Appendix B, SPN R576).
// Run from the repo root: node runs/arr/infinity.mjs
// A uniform turn over the quarter turn, read in two charts: the angle θ (bounded) and v/h = tan θ (the half-Cauchy).
let s = 0x9e3779b97f4a7c15n;
const rnd = () => { s ^= s << 13n; s &= (1n << 64n) - 1n; s ^= s >> 7n; s ^= s << 17n; s &= (1n << 64n) - 1n;
  return Number(s >> 11n) / 2 ** 53; };                     // a uniform double in [0, 1), 53 bits
const median = a => { const b = Float64Array.from(a).sort(); const n = b.length;
  return n % 2 ? b[(n - 1) / 2] : (b[n / 2 - 1] + b[n / 2]) / 2; };
const mean = a => a.reduce((p, q) => p + q, 0) / a.length;
console.log('n'.padStart(9), 'mean θ', 'median θ', '(π/4 =', (Math.PI / 4).toFixed(6) + ')', 'median v/h', 'mean v/h');
for (const n of [11, 1001, 100001, 10000001]) {
  const th = new Float64Array(n), x = new Float64Array(n);
  for (let i = 0; i < n; i++) { th[i] = (Math.PI / 2) * rnd(); x[i] = Math.tan(th[i]); }
  console.log(String(n).padStart(9), mean(th).toFixed(6), median(th).toFixed(6), '          ',
    median(x).toFixed(6), mean(x).toFixed(3));
}
// Rounding and overflow are monotone: the median commutes with them, the mean does not.
const n = 100001, x = new Float64Array(n);
for (let i = 0; i < n; i++) x[i] = Math.tan((Math.PI / 2) * rnd());
const f32 = Float32Array.from(x);                                   // round to float32
console.log('float32: median of rounded = rounded median?', median(f32) === Math.fround(median(x)));
for (const cap of [10, 1000, 65504]) {                              // a smaller machine: values past the cap saturate
  const c = x.map(v => Math.min(v, cap));
  console.log('cap', cap.toExponential(2), ': median', median(c) === Math.min(median(x), cap) ? 'unchanged' : 'CHANGED',
    '; mean', mean(c).toFixed(3), 'against', mean(x).toFixed(3));
}
const M = Math.tan((Math.PI / 2) * (1 - 2 ** -53));
console.log('largest draw possible', M.toExponential(3), '; the truncated half-Cauchy mean (1/π)ln(1+M²) =',
  (Math.log1p(M * M) / Math.PI).toFixed(2), '; the true one does not exist');
