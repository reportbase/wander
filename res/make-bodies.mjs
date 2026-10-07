// The suns, planets and moons in this folder, written as .tvf3d fields (Oct 7: "make 3d objects of moons, suns,
// planets, create a variety of them, make them look great. use them in the wander program.").
//
//   node res/make-bodies.mjs          writes every body into res/
//
// A .tvf3d is one surface about an axis: its radius r(θ, h) and its colour, each a series
//   f(θ, h) = Σn cos(nπh) Σm (a[n][m] cos mθ + b[n][m] sin mθ),
// θ a full turn about the axis and h from the bottom (0) to the top (1), the radius in units of the height. It is the
// format the games page reads for chess pieces and the 3d studio writes. A body here is a ball of radius ½ (one unit
// tall) with relief on it, and its colour painted from where each point lies on the sphere, so nothing has a seam.
//
// Every body is generated from a seed, so running this again writes the same files. To make a new one, add it to
// BODIES and run it; index.html lists the files it loads (BODY_FILES).
//
// Two things keep the series honest. The ball itself is transformed on its own and kept to all 128 terms in h (its
// radius rises steeply at the poles, which a short cosine series only approaches; cut at 48 it rippled in bands and
// left a hole at each pole). 128 is the fine grid's own count, so read back at the grid's heights, as wander reads
// it, the ball is exact. Everything laid on it (relief and colour) is generated finely and cut to fewer terms with
// Lanczos σ factors, so a sharp coast or a crater rim does not ring; its rows past those terms are zero.
import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const OUT = fileURLToPath(new URL('.', import.meta.url));
const PI = Math.PI, TAU = 2 * PI;
const GH = 128, GT = 192;                         // the fine grid every body is painted on before the transform
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const sstep = (a, b, x) => { const t = clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
const mixc = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
const rgb = hex => [parseInt(hex.slice(1, 3), 16) / 255, parseInt(hex.slice(3, 5), 16) / 255, parseInt(hex.slice(5, 7), 16) / 255];

// ── noise on the sphere: gradient noise in three dimensions, read at the point itself, so it wraps without a seam ──
function noiseOf(seed){
  let s = seed >>> 0;
  const rnd = () => { s = (s + 0x6D2B79F5) >>> 0; let t = s; t = Math.imul(t ^ t >>> 15, 1 | t); t ^= t + Math.imul(t ^ t >>> 7, 61 | t); return ((t ^ t >>> 14) >>> 0) / 4294967296; };
  const P = new Uint8Array(512), G = [];
  const perm = [...Array(256).keys()];
  for (let i = 255; i > 0; i--){ const j = Math.floor(rnd() * (i + 1)); [perm[i], perm[j]] = [perm[j], perm[i]]; }
  for (let i = 0; i < 512; i++) P[i] = perm[i & 255];
  for (let i = 0; i < 256; i++){ const z = rnd() * 2 - 1, a = rnd() * TAU, r = Math.sqrt(1 - z * z); G.push([r * Math.cos(a), r * Math.sin(a), z]); }
  const fade = t => t * t * t * (t * (t * 6 - 15) + 10);
  const n3 = (x, y, z) => {
    const X = Math.floor(x), Y = Math.floor(y), Z = Math.floor(z), fx = x - X, fy = y - Y, fz = z - Z;
    const u = fade(fx), v = fade(fy), w = fade(fz);
    const g = (i, j, k) => { const q = G[P[P[P[(X + i) & 255] + ((Y + j) & 255)] + ((Z + k) & 255)]]; return q[0] * (fx - i) + q[1] * (fy - j) + q[2] * (fz - k); };
    const l = (a, b, t) => a + (b - a) * t;
    return l(l(l(g(0, 0, 0), g(1, 0, 0), u), l(g(0, 1, 0), g(1, 1, 0), u), v), l(l(g(0, 0, 1), g(1, 0, 1), u), l(g(0, 1, 1), g(1, 1, 1), u), v), w);
  };
  const fbm = (p, f, oct = 5, gain = 0.5) => { let a = 1, s = 0, n = 0; for (let o = 0; o < oct; o++){ s += a * n3(p[0] * f + o * 17.1, p[1] * f + o * 3.7, p[2] * f + o * 9.3); n += a; a *= gain; f *= 2; } return s / n; };
  const ridged = (p, f, oct = 5) => { let a = 1, s = 0, n = 0; for (let o = 0; o < oct; o++){ s += a * (1 - Math.abs(n3(p[0] * f + o * 7.7, p[1] * f + o * 1.3, p[2] * f + o * 5.1)) * 1.6); n += a; a *= 0.5; f *= 2; } return s / n; };
  return { rnd, n3, fbm, ridged };
}
// a point on the sphere from latitude and longitude, and back
const sph = (lat, lon) => [Math.cos(lat) * Math.cos(lon), Math.sin(lat), Math.cos(lat) * Math.sin(lon)];
const angle = (a, b) => Math.acos(clamp(a[0] * b[0] + a[1] * b[1] + a[2] * b[2], -1, 1));
// craters: a bowl with a raised rim, and its fresh ejecta bright; returns [relief, brightness change]
function craters(N, count, rmin, rmax, depth){
  const list = [];
  for (let i = 0; i < count; i++){ const z = N.rnd() * 2 - 1, a = N.rnd() * TAU, r = Math.sqrt(1 - z * z);
    const rc = rmin * Math.pow(rmax / rmin, Math.pow(N.rnd(), 2.2));   // many small, few large
    list.push({ c: [r * Math.cos(a), z, r * Math.sin(a)], rc, fresh: N.rnd() }); }
  return p => { let rel = 0, br = 0;
    for (const k of list){ const d = angle(p, k.c) / k.rc; if (d > 2.6) continue;
      if (d < 1) rel += depth * k.rc * (d * d - 1) * 0.9;                       // the bowl
      else rel += depth * k.rc * 0.35 * Math.exp(-((d - 1) ** 2) / 0.06);       // the rim
      br += (d < 1 ? -0.05 : 0) + k.fresh * 0.18 * Math.exp(-((d - 1.1) ** 2) / 0.5) * (d > 0.8 ? 1 : 0.3); }
    return [rel, br]; };
}

// ── the bodies. Each returns, for a point p on the unit sphere, its relief (a fraction of the radius) and its colour ──
const BODIES = {
  // suns: their own light; granulation, spots and the darker, redder limb are the renderer's
  'sun-yellow': seed => { const N = noiseOf(seed); const spots = Array.from({ length: 7 }, () => sph((N.rnd() * 2 - 1) * 0.5, N.rnd() * TAU));
    return p => { const g = N.fbm(p, 18, 3), f = N.fbm(p, 5, 4); let c = mixc(rgb('#ffcf5a'), rgb('#fff4c8'), sstep(-0.25, 0.35, g + 0.4 * f));
      let rel = 0.006 * g;
      for (const s of spots){ const d = angle(p, s); c = mixc(c, rgb('#7a3a10'), sstep(0.09, 0.03, d)); c = mixc(c, rgb('#c8701c'), sstep(0.14, 0.09, d) * 0.6); rel -= 0.012 * sstep(0.1, 0.03, d); }
      return [rel, c]; }; },
  'sun-orange': seed => { const N = noiseOf(seed); const spots = Array.from({ length: 10 }, () => sph((N.rnd() * 2 - 1) * 0.6, N.rnd() * TAU));
    return p => { const g = N.fbm(p, 14, 3), f = N.fbm(p, 4, 4); let c = mixc(rgb('#ff8a1e'), rgb('#ffd27a'), sstep(-0.3, 0.4, g + 0.5 * f));
      let rel = 0.006 * g;
      for (const s of spots){ const d = angle(p, s); c = mixc(c, rgb('#5a1c08'), sstep(0.07, 0.02, d)); c = mixc(c, rgb('#b04a10'), sstep(0.12, 0.07, d) * 0.6); rel -= 0.012 * sstep(0.08, 0.02, d); }
      return [rel, c]; }; },
  'sun-red': seed => { const N = noiseOf(seed);
    return p => { const g = N.fbm(p, 6, 4), f = N.fbm(p, 2.5, 3); return [0.01 * g, mixc(rgb('#b8240c'), rgb('#ff7a30'), sstep(-0.35, 0.45, g + 0.6 * f))]; }; },
  'sun-blue': seed => { const N = noiseOf(seed);
    return p => { const g = N.fbm(p, 20, 3), lat = Math.asin(p[1]); let c = mixc(rgb('#8fb4ff'), rgb('#eaf2ff'), sstep(-0.3, 0.35, g + 0.25 * Math.cos(6 * lat)));
      return [0.005 * g, c]; }; },
  'sun-white': seed => { const N = noiseOf(seed);
    return p => [0, mixc(rgb('#bccdf6'), rgb('#f2f6ff'), sstep(-0.35, 0.35, N.fbm(p, 10, 3) + 0.3 * N.fbm(p, 3, 3)))]; },

  // planets
  'planet-terra': seed => { const N = noiseOf(seed);
    return p => { const lat = Math.asin(p[1]), w = [p[0] + 0.4 * N.fbm(p, 2, 3), p[1] + 0.4 * N.fbm(p, 2.3, 3), p[2] + 0.4 * N.fbm(p, 2.6, 3)];
      const e = N.fbm(w, 1.4, 6) + 0.05;                                         // elevation: below 0 the sea
      const land = sstep(0.0, 0.025, e), mtn = sstep(0.12, 0.3, e), ice = sstep(0.78, 0.86, Math.abs(p[1]) + 0.06 * N.fbm(p, 6, 3));
      const dry = sstep(0.15, 0.55, 1 - Math.abs(Math.abs(lat) - 0.38) * 3.5 + 0.8 * N.fbm(p, 3, 4));
      let c = mixc(rgb('#0b2a5e'), rgb('#1f6aa0'), sstep(-0.25, 0, e));             // deep to shallow sea
      const ground = mixc(mixc(rgb('#3f7a32'), rgb('#b59a5a'), dry), mixc(rgb('#7a6650'), rgb('#f2f2f2'), sstep(0.32, 0.42, e)), mtn);
      c = mixc(c, ground, land); c = mixc(c, rgb('#f4f8fb'), ice);
      const cl = sstep(0.08, 0.38, N.fbm([w[0] * 1.3, w[1] * 2.2, w[2] * 1.3], 2.5, 5)); c = mixc(c, rgb('#ffffff'), cl * 0.85);
      return [land * (0.07 * Math.max(0, e) + 0.006 * N.ridged(p, 9, 4)), c]; }; },
  'planet-ocean': seed => { const N = noiseOf(seed);
    return p => { const e = N.fbm(p, 3, 6) - 0.28, land = sstep(0, 0.02, e);
      let c = mixc(rgb('#06244a'), rgb('#1a7fa8'), sstep(-0.35, 0, e)); c = mixc(c, mixc(rgb('#d9c48a'), rgb('#3f8a3c'), sstep(0.02, 0.06, e)), land);
      const w = [p[0] + 0.5 * N.fbm(p, 1.5, 3), p[1] * 2.5, p[2] + 0.5 * N.fbm(p, 1.7, 3)], cl = sstep(0.1, 0.4, N.fbm(w, 2, 5));
      c = mixc(c, rgb('#ffffff'), cl * 0.9); c = mixc(c, rgb('#eef6fb'), sstep(0.85, 0.92, Math.abs(p[1])));
      return [land * 0.05 * Math.max(0, e), c]; }; },
  'planet-mars': seed => { const N = noiseOf(seed), cr = craters(N, 60, 0.02, 0.16, 0.6);
    return p => { const [rel, br] = cr(p), dark = sstep(0.0, 0.25, N.fbm(p, 2, 5)), lat = Math.asin(p[1]);
      let c = mixc(rgb('#c1653a'), rgb('#6e3a26'), dark * 0.8); c = mixc(c, rgb('#e0a070'), sstep(0.1, 0.4, N.fbm(p, 6, 4)) * 0.4);
      const canyon = sstep(0.06, 0.0, Math.abs(lat - 0.1 * N.fbm(p, 3, 3) + 0.05)) * sstep(0.2, 0.6, Math.cos(Math.atan2(p[2], p[0]) - 1));
      c = mixc(c, rgb('#4a2418'), canyon * 0.8); c = c.map(v => clamp(v * (1 + br)));
      c = mixc(c, rgb('#f6f2ee'), sstep(0.88, 0.94, Math.abs(p[1]) + 0.05 * N.fbm(p, 8, 3)));
      return [rel - canyon * 0.04 + 0.012 * N.fbm(p, 5, 5), c]; }; },
  'planet-jupiter': seed => { const N = noiseOf(seed), spot = sph(-0.38, 1.2);
    const BANDS = ['#e9dcc2', '#c99b6a', '#f2e8d4', '#a8714a', '#e6cfa8', '#8e5b3a', '#f0e2c6', '#b98256', '#e9dcc2'].map(rgb);
    return p => { let lat = Math.asin(p[1]); const lon = Math.atan2(p[2], p[0]);
      const ds = angle(p, spot), sw = Math.exp(-((ds / 0.22) ** 2));
      lat += 0.05 * N.fbm([p[0] * 3, p[1] * 0.6, p[2] * 3], 4, 5) + sw * 0.15 * Math.sin(3 * (lon - 1.2) + ds * 9);
      const t = (Math.sin(lat * 7.5 + 0.4) * 0.5 + 0.5) * (BANDS.length - 1), i = Math.floor(t);
      let c = mixc(BANDS[i], BANDS[Math.min(BANDS.length - 1, i + 1)], t - i);
      c = mixc(c, rgb('#fff6e6'), sstep(0.25, 0.5, N.fbm([p[0] * 4, p[1], p[2] * 4], 6, 4)) * 0.25);
      const oval = Math.hypot((lon - 1.2) / 0.28, (Math.asin(p[1]) + 0.38) / 0.13);
      c = mixc(c, rgb('#c2563a'), sstep(1.0, 0.55, oval)); c = mixc(c, rgb('#e8a080'), sstep(0.5, 0.0, oval) * 0.4);
      return [0.003 * N.fbm(p, 7, 3), c]; }; },
  'planet-saturn': seed => { const N = noiseOf(seed);
    const BANDS = ['#f3e2b8', '#dcc08a', '#f6ead0', '#cfae78', '#efdcb0', '#e2c792'].map(rgb);
    return p => { const lat = Math.asin(p[1]) + 0.025 * N.fbm([p[0] * 3, p[1] * 0.5, p[2] * 3], 3, 4);
      const t = (Math.sin(lat * 9) * 0.5 + 0.5) * (BANDS.length - 1), i = Math.floor(t);
      let c = mixc(BANDS[i], BANDS[Math.min(BANDS.length - 1, i + 1)], t - i);
      c = mixc(c, rgb('#9fb4c8'), sstep(0.75, 0.95, p[1]) * 0.6);                 // a blue-grey northern cap
      return [0.003 * N.fbm(p, 7, 3), c]; }; },
  'planet-neptune': seed => { const N = noiseOf(seed), spot = sph(-0.35, 2.4);
    return p => { const lat = Math.asin(p[1]) + 0.04 * N.fbm(p, 3, 4);
      let c = mixc(rgb('#2a4fd0'), rgb('#3f74e8'), Math.sin(lat * 6) * 0.5 + 0.5);
      c = mixc(c, rgb('#1a2c8a'), sstep(0.2, 0.08, angle(p, spot)));
      const streak = sstep(0.55, 0.8, N.fbm([p[0] * 5, p[1] * 0.5, p[2] * 5], 3, 4)) * sstep(0.35, 0.15, Math.abs(Math.asin(p[1]) + 0.25));
      c = mixc(c, rgb('#f0f6ff'), streak * 0.9);
      return [0.003 * N.fbm(p, 7, 3), c]; }; },
  'planet-uranus': seed => { const N = noiseOf(seed);
    return p => { const lat = Math.asin(p[1]); let c = mixc(rgb('#9fd7df'), rgb('#c4eef0'), sstep(0.4, 1.2, lat) + 0.08 * Math.sin(lat * 10));
      c = mixc(c, rgb('#b7e5ea'), sstep(-0.1, 0.3, N.fbm([p[0] * 2, p[1] * 0.3, p[2] * 2], 3, 3)) * 0.3);
      return [0.003 * N.fbm(p, 7, 3), c]; }; },
  'planet-venus': seed => { const N = noiseOf(seed);
    return p => { const lon = Math.atan2(p[2], p[0]), lat = Math.asin(p[1]);
      const v = N.fbm([Math.cos(lon + 1.6 * Math.abs(lat)), p[1] * 3, Math.sin(lon + 1.6 * Math.abs(lat))], 2.5, 5);   // swept into a V by the winds
      return [0.004 * N.fbm(p, 6, 3), mixc(rgb('#c9a35a'), rgb('#f6e7b8'), sstep(-0.3, 0.35, v))]; }; },
  'planet-lava': seed => { const N = noiseOf(seed);
    return p => { const r = N.ridged(p, 2.2, 5), crack = sstep(0.78, 0.92, r);
      let c = mixc(rgb('#1c1414'), rgb('#3a2a24'), sstep(-0.3, 0.4, N.fbm(p, 4, 4)));
      c = mixc(c, rgb('#ff7a1a'), crack); c = mixc(c, rgb('#ffd060'), sstep(0.9, 0.97, r));
      return [-crack * 0.025 + 0.02 * N.fbm(p, 4, 5), c]; }; },
  'planet-alien': seed => { const N = noiseOf(seed);
    return p => { const e = N.fbm(p, 1.8, 6), land = sstep(0.0, 0.03, e);
      let c = mixc(rgb('#0e5a5a'), rgb('#20a0a0'), sstep(-0.3, 0, e));
      c = mixc(c, mixc(rgb('#6a2a8a'), rgb('#d07ad0'), sstep(0.05, 0.3, N.fbm(p, 5, 4) + e)), land);
      c = mixc(c, rgb('#ffe6ff'), sstep(0.12, 0.42, N.fbm([p[0], p[1] * 3, p[2]], 2.5, 5)) * 0.6);
      return [land * (0.06 * Math.max(0, e) + 0.005 * N.ridged(p, 8, 4)), c]; }; },

  // moons and smaller bodies
  'moon-luna': seed => { const N = noiseOf(seed), cr = craters(N, 140, 0.015, 0.2, 0.7);
    return p => { const [rel, br] = cr(p), maria = sstep(0.05, 0.2, N.fbm(p, 1.6, 5));
      let c = mixc(rgb('#b4b2ac'), rgb('#55565c'), maria * 0.85); c = mixc(c, rgb('#d8d6d0'), sstep(0.2, 0.5, N.fbm(p, 7, 4)) * 0.25);
      return [rel - maria * 0.006, c.map(v => clamp(v * (1 + br)))]; }; },
  'moon-ice': seed => { const N = noiseOf(seed);
    return p => { const l1 = sstep(0.9, 0.97, N.ridged(p, 2.5, 4)), l2 = sstep(0.92, 0.98, N.ridged(p, 5, 3));
      let c = mixc(rgb('#efe6d6'), rgb('#d9c8b0'), sstep(-0.2, 0.4, N.fbm(p, 3, 4)));
      c = mixc(c, rgb('#9a5a3a'), Math.max(l1, l2 * 0.7)); return [l1 * 0.012 + l2 * 0.006 + 0.004 * N.fbm(p, 10, 3), c]; }; },
  'moon-io': seed => { const N = noiseOf(seed); const vents = Array.from({ length: 22 }, () => [sph(Math.asin(N.rnd() * 2 - 1), N.rnd() * TAU), 0.03 + N.rnd() * 0.07]);
    return p => { let c = mixc(rgb('#e8d25a'), rgb('#f2e9a8'), sstep(-0.2, 0.4, N.fbm(p, 4, 4)));
      c = mixc(c, rgb('#c88a3a'), sstep(0.1, 0.35, N.fbm(p, 2.5, 4)) * 0.6);
      let rel = 0.006 * N.fbm(p, 6, 4);
      for (const [v, r] of vents){ const d = angle(p, v) / r; c = mixc(c, rgb('#d8642a'), sstep(2.6, 1.4, d) * 0.7); c = mixc(c, rgb('#20160e'), sstep(1, 0.5, d)); rel += r * 0.5 * Math.exp(-d * d / 3) - r * 0.4 * Math.exp(-d * d / 0.3); }
      c = mixc(c, rgb('#a8784a'), sstep(0.8, 0.95, Math.abs(p[1])) * 0.6); return [rel, c]; }; },
  'moon-callisto': seed => { const N = noiseOf(seed), cr = craters(N, 180, 0.012, 0.12, 0.6);
    return p => { const [rel, br] = cr(p); const c = mixc(rgb('#4c4038'), rgb('#7a6a5a'), sstep(-0.3, 0.4, N.fbm(p, 3, 4)));
      return [rel, c.map(v => clamp(v * (1 + 2.2 * br)))]; }; },
  'moon-rust': seed => { const N = noiseOf(seed), cr = craters(N, 70, 0.02, 0.18, 0.7);
    return p => { const [rel, br] = cr(p); const c = mixc(rgb('#7a4a36'), rgb('#b07a5a'), sstep(-0.3, 0.4, N.fbm(p, 2.5, 5)));
      return [rel + 0.01 * N.fbm(p, 3, 4), c.map(v => clamp(v * (1 + br)))]; }; },
  // asteroids: not round, so they read as rocks, not little moons
  'asteroid-grey': seed => { const N = noiseOf(seed), cr = craters(N, 40, 0.04, 0.3, 0.8);
    return p => { const [rel, br] = cr(p); const c = mixc(rgb('#6a6660'), rgb('#9a958c'), sstep(-0.3, 0.4, N.fbm(p, 4, 4)));
      return [0.28 * N.fbm(p, 1.1, 3) + 0.08 * N.fbm(p, 3, 3) + rel, c.map(v => clamp(v * (1 + br)))]; }; },
  'asteroid-dark': seed => { const N = noiseOf(seed), cr = craters(N, 30, 0.05, 0.35, 0.8);
    return p => { const [rel, br] = cr(p); const c = mixc(rgb('#3a3430'), rgb('#5e544a'), sstep(-0.3, 0.4, N.fbm(p, 5, 4)));
      return [0.32 * N.fbm(p, 0.9, 3) + 0.06 * N.fbm(p, 4, 3) + rel, c.map(v => clamp(v * (1 + br)))]; }; },
};
// how many terms each keeps: a smooth body needs few, a cratered or continental one more (and a bigger file)
const DETAIL = { 'sun-white': [24, 24], 'planet-uranus': [24, 16], 'sun-red': [32, 40], 'sun-blue': [40, 48], 'planet-saturn': [48, 24], 'planet-venus': [40, 48] };
const DEFAULT_DETAIL = [48, 64];

// ── the transform: sample on the fine grid, then the series, cut to NH × MT ──
function series(F, NH, MT, sigma){                 // F[i][j] at h_i = (i + ½)/GH, θ_j = 2πj/GT
  const A = Array.from({ length: NH }, () => new Float64Array(MT)), B = Array.from({ length: NH }, () => new Float64Array(MT));
  const Ch = Array.from({ length: NH }, (_, n) => Float64Array.from({ length: GH }, (_, i) => Math.cos(n * PI * (i + 0.5) / GH) * (n ? 2 : 1) / GH));
  const row = new Float64Array(GT);
  for (let n = 0; n < NH; n++){
    row.fill(0); for (let i = 0; i < GH; i++){ const w = Ch[n][i]; if (w) for (let j = 0; j < GT; j++) row[j] += w * F[i][j]; }
    for (let m = 0; m < MT; m++){ let a = 0, b = 0; for (let j = 0; j < GT; j++){ const t = TAU * j / GT; a += row[j] * Math.cos(m * t); b += row[j] * Math.sin(m * t); }
      const k = (m ? 2 : 1) / GT, s = sigma ? (n ? Math.sin(PI * n / NH) / (PI * n / NH) : 1) * (m ? Math.sin(PI * m / MT) / (PI * m / MT) : 1) : 1;
      A[n][m] = a * k * s; B[n][m] = m ? b * k * s : 0; } }
  return { A, B };
}
const fmt = v => { if (Math.abs(v) < 5e-6) return '0'; const s = v.toPrecision(4); return String(+s); };
function build(name){
  const make = BODIES[name](name.split('').reduce((h, c) => Math.imul(h ^ c.charCodeAt(0), 16777619) >>> 0, 2166136261));
  const [NH, MT] = DETAIL[name] || DEFAULT_DETAIL;
  const env = [], rel = [], ch = [[], [], []];
  for (let i = 0; i < GH; i++){
    const h = (i + 0.5) / GH, y = 2 * h - 1, lat = Math.asin(y), e = 0.5 * Math.sqrt(1 - y * y);
    env.push(new Float64Array(GT).fill(e)); const R = new Float64Array(GT), C = [new Float64Array(GT), new Float64Array(GT), new Float64Array(GT)];
    for (let j = 0; j < GT; j++){ const [dr, c] = make(sph(lat, TAU * j / GT)); R[j] = e * dr; for (let k = 0; k < 3; k++) C[k][j] = clamp(c[k]); }
    rel.push(R); ch.forEach((a, k) => a.push(C[k]));
  }
  const E = series(env, GH, 1, false), Rl = series(rel, NH, MT, true), Cs = ch.map(c => series(c, NH, MT, true));
  const full = M => Array.from({ length: GH }, (_, n) => n < M.length ? M[n] : new Float64Array(MT));   // zero rows past the cut
  const rows = (tag, M) => full(M).map(r => tag + ' ' + Array.from(r, fmt).join(' ')).join('\n') + '\n';
  const Aa = full(Rl.A).map((r, n) => r.map((v, m) => v + (m ? 0 : E.A[n][0]))), Ab = full(Rl.B);
  let txt = 'TVF3D ' + GH + ' ' + MT + ' color\n' + rows('Aa', Aa) + rows('Ab', Ab);
  ['r', 'g', 'b'].forEach((k, i) => { txt += rows('C' + k + 'a', Cs[i].A) + rows('C' + k + 'b', Cs[i].B); });
  writeFileSync(OUT + name + '.tvf3d', txt);
  return txt.length;
}
const only = process.argv.slice(2);
for (const name of Object.keys(BODIES)) if (!only.length || only.includes(name)){ const n = build(name); console.log(name.padEnd(16), (n / 1024).toFixed(0) + ' KB'); }
