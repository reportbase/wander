"""AFM run 1: the address-first mapper against bundle adjustment, structure only (plans/afm-plan.md).
Run from the repository's root: python3 runs/afm/afm.py"""
import time
import numpy as np
from scipy.optimize import least_squares

THINGS = [((1.0, 2.0, 0.0), (1.2, 0.8, 0.75)), ((3.4, 0.9, 0.0), (0.5, 0.5, 0.5)), ((1.4, 2.2, 0.75), (0.24, 0.24, 0.24)),
          ((4.2, 3.0, 0.0), (0.6, 0.5, 1.8))]
GAMMA = 1e-3
SEEDS = [11, 12, 13, 14, 15]


def features(rng):
    pts = []
    for _ in range(50):
        face = rng.integers(6); p = rng.uniform([0, 0, 0], [5, 4, 2.5]); p[face // 2] = [0, 5, 0, 4, 0, 2.5][face]
        pts.append(p)
    for i in range(30):
        c, s = THINGS[i % 4]; p = np.array(c) + rng.uniform(0, 1, 3) * s
        f = rng.integers(3); p[f] = c[f] + s[f] * rng.integers(2); pts.append(p)
    return np.array(pts)


def scene(seed, K):
    rng = np.random.default_rng(seed)
    P = features(rng)
    X = rng.uniform([1.5, 1, 1], [3.5, 3, 2], size=(16, 3))[:K]        # the first K of one seeded set of 16
    s = np.linalg.norm(X[1] - X[0])
    return (P - X[0]) / s, (X - X[0]) / s                               # in |AB|, standpoint 1 at the origin


def perp(u, rng):
    a = rng.normal(size=3); a -= u * (a @ u); return a / np.linalg.norm(a)


def read(P, X, law, f, rng):
    """R[k, i]: standpoint k's unit direction to feature i, turned off by the law's angle; a share f replaced."""
    R = np.empty((len(X), len(P), 3))
    for k, x in enumerate(X):
        for i, p in enumerate(P):
            u = (p - x) / np.linalg.norm(p - x)
            if law == 'cauchy': d = np.arctan(abs(GAMMA * np.tan(np.pi * (rng.random() - 0.5))))
            else: d = abs(rng.normal(0, GAMMA / 0.6745))
            n = perp(u, rng); v = u * np.cos(d) + n * np.sin(d)
            if rng.random() < f: v = rng.normal(size=3); v /= np.linalg.norm(v)
            R[k, i] = v
    return R


def linear(X, U):
    A = np.zeros((3, 3)); b = np.zeros(3)
    for x, u in zip(X, U):
        M = np.eye(3) - np.outer(u, u); A += M; b += M @ x
    return np.linalg.lstsq(A, b, rcond=None)[0]


def resid(p, X, U):
    out = []
    for x, u in zip(X, U):
        w = p - x; r = np.linalg.norm(w); out.extend((w - u * (w @ u)) / r)
    return np.array(out)


def ls(X, U):
    return least_squares(resid, linear(X, U), args=(X, U), method='lm').x


def cb(X, U, start):
    return least_squares(resid, start, args=(X, U), loss='cauchy', f_scale=GAMMA).x


def af(X, U):
    mids = []
    for a in range(len(X)):
        for b in range(a + 1, len(X)):
            o1, u1, o2, u2 = X[a], U[a], X[b], U[b]
            w = o1 - o2; bb = u1 @ u2; d, e = u1 @ w, u2 @ w; den = 1 - bb * bb
            if den <= 1e-15: continue
            t = (bb * e - d) / den; s = (e - bb * d) / den
            if t > 0 and s > 0: mids.append(((o1 + u1 * t) + (o2 + u2 * s)) / 2)
    return np.median(np.array(mids), axis=0) if mids else None


def run(K, law, f, timing=False):
    errs = {'LS': [], 'CB': [], 'AF': []}; tm = {'LS': 0.0, 'CB': 0.0, 'AF': 0.0}; rays = 0
    for seed in SEEDS:
        P, X = scene(seed, K)
        R = read(P, X, law, f, np.random.default_rng(seed * 7919 + K * 31 + int(f * 1000) + (law == 'normal') * 17))
        for i, p in enumerate(P):
            U = R[:, i, :]; d = np.linalg.norm(p)
            t0 = time.perf_counter(); q = ls(X, U); t1 = time.perf_counter()
            r = cb(X, U, q); t2 = time.perf_counter(); a = af(X, U); t3 = time.perf_counter()
            tm['LS'] += t1 - t0; tm['CB'] += t2 - t1; tm['AF'] += t3 - t2
            errs['LS'].append(np.linalg.norm(q - p) / d); errs['CB'].append(np.linalg.norm(r - p) / d)
            if a is None: rays += 1; errs['AF'].append(np.inf)
            else: errs['AF'].append(np.linalg.norm(a - p) / d)
    med = {k: float(np.median(v)) for k, v in errs.items()}
    n = len(SEEDS) * 80
    return med, {k: v / n for k, v in tm.items()}, rays


print("F1: Cauchy bearings, no outliers, median relative error")
c = {}
for K in (4, 8, 16):
    c[K], t, rays = run(K, 'cauchy', 0.0)
    print(f"  K = {K:2d}: LS {c[K]['LS']:.3e}  CB {c[K]['CB']:.3e}  AF {c[K]['AF']:.3e}  (rays only {rays})")
g = {k: c[4][k] / c[16][k] for k in c[4]}
f1 = g['LS'] < 1.5 and g['CB'] > 1.5 and g['AF'] > 1.5
print(f"  K 4 -> 16 improves LS by {g['LS']:.2f}, CB by {g['CB']:.2f}, AF by {g['AF']:.2f}")
print("F1", "not killed" if f1 else "KILLED")

print("\nF2: normal bearings (same median), K = 8")
nrm, _, _ = run(8, 'normal', 0.0)
f2 = nrm['LS'] <= 1.1 * nrm['CB'] and nrm['AF'] > 1.1 * nrm['LS']
print(f"  LS {nrm['LS']:.3e}  CB {nrm['CB']:.3e}  AF {nrm['AF']:.3e};  LS/CB {nrm['LS']/nrm['CB']:.3f}, AF/LS {nrm['AF']/nrm['LS']:.3f}")
print("F2", "not killed" if f2 else "KILLED")

print("\nF3, F4: outliers, Cauchy bearings, K = 8")
base = c[8]; rows = {}
fstar = None
for f in [round(0.05 * j, 2) for j in range(0, 15)]:
    m, _, rays = (base, None, 0) if f == 0 else run(8, 'cauchy', f)
    rows[f] = m
    print(f"  f = {f:.2f}: LS {m['LS']/base['LS']:9.2f}x  CB {m['CB']/base['CB']:9.2f}x  AF {m['AF']/base['AF']:9.2f}x  (rays only {rays})")
    if fstar is None and m['AF'] > 10 * base['AF']: fstar = f
f3 = rows[0.1]['LS'] > 10 * base['LS'] and rows[0.2]['CB'] <= 3 * base['CB'] and rows[0.2]['AF'] <= 3 * base['AF']
print("F3", "not killed" if f3 else "KILLED")
f4 = fstar is not None and 0.29 <= fstar <= 0.60
print(f"  AF's breakdown f* = {fstar}")
print("F4", "not killed" if f4 else "KILLED")

print("\nF5: time per feature at K = 16")
_, t16, _ = run(16, 'cauchy', 0.0)
print(f"  LS {t16['LS']*1e3:.2f} ms  CB {t16['CB']*1e3:.2f} ms  AF {t16['AF']*1e3:.2f} ms;  AF/LS {t16['AF']/t16['LS']:.2f}")
print("F5", "not killed" if t16['AF'] > 3 * t16['LS'] else "KILLED")
print("\nF6", "not killed" if (f1 and f2 and f3) else "KILLED")
