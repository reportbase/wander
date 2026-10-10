// REF (plans/ref-plan.md): the corner as the reference sphere, on wander's bodies (res/*.tvf3d) and on published radii.
import fs from 'fs'; import path from 'path';
const dir = process.argv[2] || 'res', GH = 128, GT = 256;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.tvf3d')).sort();
const parse = t => { const L = t.split('\n'), R = {}; for (const l of L.slice(1)) { const w = l.trim().split(/\s+/); if (w[0] === 'Aa' || w[0] === 'Ab') (R[w[0]] = R[w[0]] || []).push(w.slice(1).map(Number)); } return R; };
const ball = h => { const y = 2 * h - 1; return 0.5 * Math.sqrt(Math.max(0, 1 - y * y)); };
const band = (n, m) => { const f = Math.max(n, m); return f < 10 ? 0 : f < 24 ? 1 : 2; };
const rows = [];
for (const f of files) {
  const { Aa, Ab } = parse(fs.readFileSync(path.join(dir, f), 'utf8')), NH = Aa.length, M = Aa[0].length;
  const hs = Array.from({ length: GH }, (_, i) => (i + 0.5) / GH);
  const E = Array.from({ length: NH }, (_, n) => hs.reduce((s, h, i) => s + ball(h) * Math.cos(n * Math.PI * h), 0) * (n ? 2 : 1) / GH);
  const cs = [], sn = []; for (let m = 0; m < M; m++) { cs.push([]); sn.push([]); for (let j = 0; j < GT; j++) { cs[m].push(Math.cos(m * 2 * Math.PI * j / GT)); sn[m].push(Math.sin(m * 2 * Math.PI * j / GT)); } }
  let logSum = 0; const D = [], bandVar = [0, 0, 0], bandMean = [0, 0, 0], cnt = GH * GT, bandVals = [[], [], []];
  for (let i = 0; i < GH; i++) {
    const h = hs[i], z = h - 0.5;
    const A = new Float64Array(M), B = new Float64Array(M), Ab3 = [0, 1, 2].map(() => [new Float64Array(M), new Float64Array(M)]);
    for (let n = 0; n < NH; n++) { const k = Math.cos(n * Math.PI * h);
      for (let m = 0; m < M; m++) { A[m] += k * Aa[n][m]; B[m] += k * Ab[n][m]; const b = band(n, m); Ab3[b][0][m] += k * (Aa[n][m] - (m ? 0 : E[n])); Ab3[b][1][m] += k * Ab[n][m]; } }
    for (let j = 0; j < GT; j++) {
      let rho = 0; for (let m = 0; m < M; m++) rho += A[m] * cs[m][j] + B[m] * sn[m][j];
      const R = Math.sqrt(Math.max(1e-9, rho) ** 2 + z * z); D.push(R); logSum += Math.log(R);
      for (let b = 0; b < 3; b++) { let s = 0; for (let m = 0; m < M; m++) s += Ab3[b][0][m] * cs[m][j] + Ab3[b][1][m] * sn[m][j]; bandVals[b].push(s * ball(h) / 0.5); }
    }
  }
  const Rbar = Math.exp(logSum / cnt), dl = D.map(R => Math.log2(R / Rbar));
  const v = bandVals.map(a => { const mu = a.reduce((x, y) => x + y, 0) / a.length; return a.reduce((x, y) => x + (y - mu) ** 2, 0) / a.length; });
  rows.push({ f: f.replace('.tvf3d', ''), Rbar, range: Math.max(...dl) - Math.min(...dl), v });
}
let ok1 = true, ok2 = true, ok3 = true;
for (const r of rows) {
  const p1 = Math.abs(r.Rbar / 0.5 - 1) <= 0.01, rock = r.f.startsWith('asteroid'), p2 = rock ? r.range > 0.3 : r.range < 0.1, p3 = r.v[0] > r.v[1] && r.v[1] > r.v[2];
  ok1 &&= p1; ok2 &&= p2; ok3 &&= p3;
  const tv = r.v[0] + r.v[1] + r.v[2];
  console.log(`${r.f.padEnd(15)} R̄ ${r.Rbar.toFixed(5)} (${((r.Rbar / 0.5 - 1) * 100).toFixed(2)}%)${p1 ? '' : ' ✗'}  range ${r.range.toFixed(4)} levels${p2 ? '' : ' ✗'}  bands ${r.v.map(x => (100 * x / tv).toFixed(1) + '%').join(' / ')}${p3 ? '' : ' ✗'}`);
}
console.log(`P1: ${ok1 ? 'not killed' : 'KILLED'}. every corner sphere within 1% of the ball, 1/2`);
console.log(`P2: ${ok2 ? 'not killed' : 'KILLED'}. suns, planets, moons under 0.1 levels; asteroids over 0.3`);
console.log(`P3: ${ok3 ? 'not killed' : 'KILLED'}. broad > middle > fine in every body`);
// P4, P5: published radii (km), through their ratios only
const L2 = x => Math.log2(x), W = { Earth: [6378.1, 6356.8, 0.0048], Mars: [3396.2, 3376.2, 0.0085], Moon: [1738.1, 1736.0, 0.0017], Jupiter: [71492, 66854, 0.097], Saturn: [60268, 54364, 0.149] };
let ok4 = true; const p4 = [];
for (const [k, [a, c, want]] of Object.entries(W)) { const got = L2(a / c); p4.push(`${k} ${got.toFixed(5)}`); if (Math.abs(got - want) > 0.0005) ok4 = false; if (['Earth', 'Mars', 'Moon'].includes(k) && got >= 0.01) ok4 = false; }
console.log(`P4: ${ok4 ? 'not killed' : 'KILLED'}. flattening in levels, log2(a/c): ${p4.join(', ')}`);
const relief = L2((6371 + 8.8) / (6371 - 10.9)), both = relief + L2(6378.1 / 6356.8);
console.log(`P5: ${relief <= 0.006 && both < 0.01 ? 'not killed' : 'KILLED'}. Earth's relief ${relief.toFixed(5)} levels; with its flattening ${both.toFixed(5)}`);
