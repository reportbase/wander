"""REF run 2: real relief by octave. See plans/ref-plan.md, run 2 (predictions written before the data was downloaded).

Seven published spherical-harmonic models of rocky bodies' physical surfaces, 4pi-normalized, in metres. For each, the
degree power S_l = sum_m (C_lm^2 + S_lm^2), the RMS relief of each octave [2^k, 2^(k+1)), and the least-squares line of
log2 RMS against k over k = 3..9 (Venus 3..8). Numpy only.
Run: python3 -I plans/ref/ref2.py <data dir>   (the files named in the plan, as downloaded; under a minute)
"""
import sys, os, gzip, struct
import numpy as np

D = sys.argv[1]

def opener(path):
    return gzip.open(path, 'rb') if path.endswith('.gz') else open(path, 'rb')

def degree_power_bshc(path, lmax):
    """Curtin's bshc: doubles n_min, n_max, then every C(l, m) by degree, then every S(l, m)."""
    with opener(path) as f:
        n0, n1 = (int(v) for v in struct.unpack('<2d', f.read(16)))
        assert n0 == 0 and n1 >= lmax, (path, n0, n1)
        count = (n1 + 1) * (n1 + 2) // 2
        C = np.frombuffer(f.read(8 * count), '<f8')
        S = np.frombuffer(f.read(8 * count), '<f8')
        assert C.size == count and S.size == count, path
    ls = np.repeat(np.arange(n1 + 1), np.arange(1, n1 + 2))      # the degree of each entry, (l, m) with m = 0..l
    P = np.bincount(ls, weights=C * C + S * S, minlength=n1 + 1)
    return P[:lmax + 1], C[0], n1

def degree_power_text(path, lmax):
    """SHTOOLS text: lines 'l m C S'."""
    P = np.zeros(lmax + 1); c00 = None; top = 0
    with gzip.open(path, 'rt') if path.endswith('.gz') else open(path) as f:
        for line in f:
            p = line.replace(',', ' ').split()
            if len(p) < 4: continue
            try: l, m, c, s = int(p[0]), int(p[1]), float(p[2]), float(p[3])
            except ValueError: continue
            top = max(top, l)
            if l == 0 and m == 0: c00 = c
            if l <= lmax: P[l] += c * c + s * s
    return P, c00, top

BODIES = [   # name, file, reader, octave top k, mean radius (None: the file's C00)
    ('Mercury', 'Mercury_shape_1439.sh.gz', degree_power_bshc, 9, None),
    ('Venus', 'VenusTopo719.shape.gz', degree_power_text, 8, None),
    ('Earth', 'Earth2014.SUR2014.degree2160.bshc', degree_power_bshc, 9, 6371000.0),
    ('Moon', 'Moon_LOLA_shape_1439.bshc.gz', degree_power_bshc, 9, None),
    ('Mars', 'Mars_MOLA_shape_1439.bshc.gz', degree_power_bshc, 9, None),
    ('Vesta', 'Vesta_DLR_SPG_shape_1439.bshc.gz', degree_power_bshc, 9, None),
    ('Ceres', 'Ceres_DLR_SPG_shape_1439.bshc.gz', degree_power_bshc, 9, None),
]
INFO = [('Earth bedrock', 'Earth2014.BED2014.degree2160.bshc', degree_power_bshc, 9, 6371000.0)]
K0 = 3

def octaves(P, k1):
    return np.array([np.sqrt(P[2 ** k: 2 ** (k + 1)].sum()) for k in range(K0, k1 + 1)])

def study(name, fn, reader, k1, R):
    P, c00, top = reader(os.path.join(D, fn), 2 ** (k1 + 1) - 1)
    R = R if R is not None else c00
    rms = octaves(P, k1)
    ks = np.arange(K0, k1 + 1)
    y = np.log2(rms)
    slope, icpt = np.polyfit(ks, y, 1)
    res = y - (slope * ks + icpt)
    rho = rms * 2.0 ** (ks + 1) / (np.pi * R)
    total = np.sqrt(P[1:].sum())
    return dict(name=name, R=R, top=top, rms=rms, ks=ks, slope=slope, res=res, rho=rho, total=total, P=P)

out = [study(*b) for b in BODIES]
info = [study(*b) for b in INFO]

print("octaves k: degrees [2^k, 2^(k+1)); RMS relief in metres; log2 residual from the body's line; rho = RMS in the "
      "reader's addresses at the level where the octave is the finest held")
for r in out + info:
    print(f"\n{r['name']}: R {r['R'] / 1000:.1f} km (model to degree {r['top']}), relief RMS over degrees 1-{len(r['P']) - 1} "
          f"{r['total']:.0f} m; slope {r['slope']:+.3f} levels of relief per octave (degree power ~ l^{2 * r['slope'] - 1:+.2f})")
    for k, a, e, q in zip(r['ks'], r['rms'], r['res'], r['rho']):
        print(f"  k {k} [{2 ** k:4d}, {2 ** (k + 1):4d}): RMS {a:9.1f} m   residual {e:+.3f}   rho {q:.4f}")

worst = max(((abs(e), r['name'], k) for r in out for k, e in zip(r['ks'], r['res'])))
p6 = worst[0] <= 0.25
print(f"\nP6: {'not killed' if p6 else 'KILLED'}. largest departure from a body's line {worst[0]:.3f} levels "
      f"({worst[1]}, k = {worst[2]}); threshold 0.25. Over 0.25: " +
      (", ".join(f"{r['name']} k={k} ({e:+.3f})" for r in out for k, e in zip(r['ks'], r['res']) if abs(e) > 0.25) or "none"))
sl = {r['name']: r['slope'] for r in out}
out7 = [n for n, s in sl.items() if not (-1.15 <= s <= -0.85)]
print(f"P7: {'not killed' if not out7 else 'KILLED'}. slopes " + ", ".join(f"{n} {s:+.3f}" for n, s in sl.items()) +
      f"; outside [-1.15, -0.85]: {', '.join(out7) or 'none'}")
m = np.mean(list(sl.values())); spread = max(abs(s - m) for s in sl.values())
print(f"P8: {'not killed' if spread <= 0.1 else 'KILLED'}. mean slope {m:+.3f}, largest departure {spread:.3f} (threshold 0.1)")
