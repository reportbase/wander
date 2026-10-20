"""BER run 1: are real bearing errors heavy-tailed? (plans/ber-plan.md). Run from the repository's root:
python3 runs/ber/ber.py <directory holding the eight extracted sequences>"""
import sys, os
import numpy as np
import cv2
from scipy.optimize import minimize
from scipy.stats import norm

ROOT = sys.argv[1]
SEQS = ['graf', 'wall', 'boat', 'bark', 'bikes', 'trees', 'leuven', 'ubc']
PAIRS, W = (2, 3, 4), 8.0


def img(s, k):
    for ext in ('ppm', 'pgm'):
        p = os.path.join(ROOT, s, f'img{k}.{ext}')
        if os.path.exists(p): return cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    raise FileNotFoundError(s, k)


def errors(s, k, sift):
    a, b = img(s, 1), img(s, k)
    ka, da = sift.detectAndCompute(a, None); kb, db = sift.detectAndCompute(b, None)
    m = cv2.BFMatcher(cv2.NORM_L2).knnMatch(da, db, k=2)
    keep = [p[0] for p in m if len(p) == 2 and p[0].distance < 0.8 * p[1].distance]
    H = np.loadtxt(os.path.join(ROOT, s, f'H1to{k}p'))
    x1 = np.array([ka[q.queryIdx].pt for q in keep]); x2 = np.array([kb[q.trainIdx].pt for q in keep])
    y = (H @ np.column_stack([x1, np.ones(len(x1))]).T).T; y = y[:, :2] / y[:, 2:]
    return x2 - y


def fit(c, kind):
    """Maximum likelihood on [-W, W], truncated: location and log scale."""
    def nll(p):
        m, s = p[0], np.exp(p[1])
        if kind == 'cauchy':
            lp = -np.log(np.pi * s * (1 + ((c - m) / s) ** 2))
            mass = (np.arctan((W - m) / s) - np.arctan((-W - m) / s)) / np.pi
        else:
            lp = norm.logpdf(c, m, s); mass = norm.cdf(W, m, s) - norm.cdf(-W, m, s)
        return -(lp.sum() - len(c) * np.log(mass))
    r = minimize(nll, [np.median(c), np.log(max(np.median(np.abs(c - np.median(c))), 1e-3))], method='Nelder-Mead',
                 options={'xatol': 1e-8, 'fatol': 1e-8, 'maxiter': 4000})
    return -r.fun, np.exp(r.x[1])


def comps(E):
    E = E[(np.abs(E[:, 0]) <= W) & (np.abs(E[:, 1]) <= W)]
    return E.ravel()


sift = cv2.SIFT_create()
allE, b2, b3 = [], 0, 0
for s in SEQS:
    Es = {k: errors(s, k, sift) for k in PAIRS}
    pooled = np.vstack(list(Es.values())); allE.append(pooled)
    c = comps(pooled); lc, gc = fit(c, 'cauchy'); ln, sn = fit(c, 'normal')
    g = {k: fit(comps(Es[k]), 'cauchy')[1] for k in PAIRS}
    b2 += lc > ln; b3 += g[4] > g[2]
    n = {k: len(Es[k]) for k in PAIRS}
    print(f"{s:7s} matches {n[2]:5d} {n[3]:5d} {n[4]:5d}; in window {len(c)//2:5d}; logL Cauchy {lc:10.1f} normal {ln:10.1f} "
          f"(Cauchy {'higher' if lc > ln else 'lower'}); gamma {gc:.3f} px, sigma {sn:.3f} px; "
          f"gamma by pair {g[2]:.3f} {g[3]:.3f} {g[4]:.3f}", flush=True)
r = np.linalg.norm(np.vstack(allE), axis=1)
xs = np.logspace(np.log10(2), np.log10(32), 13)
S = np.array([(r > x).mean() for x in xs])
slope = np.polyfit(np.log(xs), np.log(S), 1)[0]
print(f"\npooled matches {len(r)}; P(|e| > x): " + "  ".join(f"{x:.1f}:{v:.4f}" for x, v in zip(xs, S)))
for lo, hi in ((0.5, 2), (2, 8), (8, 32), (32, 256)):
    xx = np.logspace(np.log10(lo), np.log10(hi), 9); SS = np.array([(r > x).mean() for x in xx])
    print(f"  slope over {lo}-{hi} px: {np.polyfit(np.log(xx), np.log(SS), 1)[0]:.3f}")
print(f"  share past 32 px {np.mean(r > 32):.4f}, past 256 px {np.mean(r > 256):.4f}, median {np.median(r):.3f} px")
b1 = -2 <= slope <= -0.5
print(f"\nB1 slope over 2-32 px {slope:.3f}:", "not killed" if b1 else "KILLED")
print(f"B2 Cauchy higher in {b2} of 8:", "not killed" if b2 >= 6 else "KILLED")
print(f"B3 gamma grows (1,2) to (1,4) in {b3} of 8:", "not killed" if b3 >= 6 else "KILLED")
print("B4", "not killed" if (b1 and b2 >= 6) else "KILLED")
