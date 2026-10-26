"""WHT: whitening is drawing V = H (plans/wht-plan.md, predictions W0–W3).

Run from the repository's root: python3 runs/wht/wht.py <dir holding wine.data and wdbc.data>
"""
import math
import sys
import time

import mpmath as mp
import numpy as np

T0 = time.time()
verdict = {}
DATA = sys.argv[1]


def say(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- W0: the theory, exact
mp.mp.dps = 40
worst = mp.mpf(0)
for r in ("-0.9", "-0.5", "0", "0.3", "0.9"):
    for c in ("1e-3", "0.1", "1", "7", "1e3"):
        r_, c_ = mp.mpf(r), mp.mpf(c)
        # X_j/X_i for a normal pair is Cauchy(location r·c, scale c·√(1 − r²)); P(|R| ≤ q) by its distribution function
        m, s = r_ * c_, c_ * mp.sqrt(1 - r_ ** 2)
        F = lambda q: (mp.atan((q - m) / s) + mp.atan((q + m) / s)) / mp.pi
        q_raw = mp.findroot(lambda q: F(q) - mp.mpf(1) / 2, (c_ / 100, c_ * 100), solver="illinois")
        ms, ss = r_, mp.sqrt(1 - r_ ** 2)
        Fs = lambda q: (mp.atan((q - ms) / ss) + mp.atan((q + ms) / ss)) / mp.pi
        q_std = mp.findroot(lambda q: Fs(q) - mp.mpf(1) / 2, (mp.mpf("0.01"), mp.mpf(100)), solver="illinois")
        worst = max(worst, abs(q_raw / c_ - 1), abs(q_std - 1))
        # and the law itself, by quadrature of the bivariate normal's ratio density (Hinkley 1969 with zero means)
        dens = lambda t: s / (mp.pi * ((t - m) ** 2 + s ** 2))
        p_quad = mp.quad(dens, [-c_, 0, c_])
        worst = max(worst, abs(p_quad - mp.mpf(1) / 2))
verdict["W0"] = worst < mp.mpf(10) ** -25
say(f"W0  normal pairs, 25 (r, c): median |X_j/X_i| / c − 1, median |Z_j/Z_i| − 1, P(|X_j/X_i| ≤ c) − ½: largest "
    f"{mp.nstr(worst, 3)}")


# ---------------------------------------------------------------- the data
def load(name):
    rows = [l.strip().split(",") for l in open(f"{DATA}/{name}") if l.strip()]
    if name == "wine.data":
        y = np.array([int(r[0]) for r in rows])
        X = np.array([[float(v) for v in r[1:]] for r in rows])
    else:
        y = np.array([1 if r[1] == "M" else 0 for r in rows])
        X = np.array([[float(v) for v in r[2:]] for r in rows])
    return X, y


def loo_1nn(X, y):
    D = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
    np.fill_diagonal(D, np.inf)
    return float(np.mean(y[np.argmin(D, axis=1)] == y))


w1 = w2 = w3 = True
for name in ("wine.data", "wdbc.data"):
    X, y = load(name)
    n, d = X.shape
    Xc = X - X.mean(axis=0)
    sd = Xc.std(axis=0)
    Z = Xc / sd
    say(f"\n{name}: {n} × {d}; σ from {sd.min():.3g} to {sd.max():.3g} (ratio {sd.max() / sd.min():.3g})")

    # W1
    ident, logs_raw, logs_c, near = 0.0, [], [], 0
    pairs = [(i, j) for i in range(d) for j in range(i + 1, d)]
    for i, j in pairs:
        ok = (Xc[:, i] != 0)
        mr = np.median(np.abs(Xc[ok, j] / Xc[ok, i]))
        ms = np.median(np.abs(Z[ok, j] / Z[ok, i]))
        c = sd[j] / sd[i]
        ident = max(ident, abs(mr / (c * ms) - 1))
        logs_raw.append(math.log(mr))
        logs_c.append(math.log(c))
        near += abs(math.log2(ms)) <= 0.5
    corr = float(np.corrcoef(logs_raw, logs_c)[0, 1])
    frac = near / len(pairs)
    ok1 = ident < 1e-12 and frac >= 0.90 and corr >= 0.99
    w1 &= ok1
    stdmed = [math.exp(a - b) for a, b in zip(logs_raw, logs_c)]
    say(f"W1  {len(pairs)} pairs: identity off by {ident:.1e}; standardized medians within a factor √2 of 1 in "
        f"{frac:.3f} (from {min(stdmed):.3f} to {max(stdmed):.3f}); raw medians span "
        f"{math.exp(min(logs_raw)):.3g} … {math.exp(max(logs_raw)):.3g}; corr(log raw median, log c) {corr:.5f}")

    # W2
    big = sd >= sd.max() / 10
    ev, evec = np.linalg.eigh(np.cov(Xc.T))
    pc1 = evec[:, -1]
    share_big = float(np.sum(pc1[big] ** 2))
    evs, evecs = np.linalg.eigh(np.corrcoef(Xc.T))
    pc1s = evecs[:, -1]
    maxload = float(np.max(np.abs(pc1s)))
    ok2 = share_big >= 0.99 and maxload <= 0.5
    w2 &= ok2
    say(f"W2  features with σ ≥ σ_max/10: {int(big.sum())} of {d}; raw PC1's squared loading on them {share_big:.5f} "
        f"(explained variance {ev[-1] / ev.sum():.4f}); standardized PC1's largest |loading| {maxload:.3f} "
        f"(explained {evs[-1] / evs.sum():.4f})")

    # W3
    a_raw, a_big, a_std = loo_1nn(X, y), loo_1nn(X[:, big], y), loo_1nn(Z, y)
    ok3 = abs(a_raw - a_big) <= 0.05 and a_std >= a_raw + 0.10
    w3 &= ok3
    say(f"W3  leave-one-out 1-NN: raw {a_raw:.4f}, long axes only {a_big:.4f}, standardized {a_std:.4f}")

verdict["W1"], verdict["W2"], verdict["W3"] = w1, w2, w3
say("")
for kk in ["W0", "W1", "W2", "W3"]:
    say(f"{kk}: {'not killed' if verdict[kk] else 'KILLED'}")
say(f"({time.time() - T0:.0f} s)")
