"""LGO run 2 (plans/lgo-plan.md): the band, the drawing measured, V = H drawn by order, and the transient as payload.

Run from the repository's root:  python3 runs/lgo/lgo2.py   (needs run 1's cache, LGO_CACHE)
"""
import os
import numpy as np
from scipy.stats import kstest
from gwpy.timeseries import TimeSeries

GPS, DUR = 1257000000, 512
CACHE = os.environ.get("LGO_CACHE", "/tmp/lgo-cache")
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def white(det):
    ts = TimeSeries.read(os.path.join(CACHE, f"{det}-{GPS}-{DUR}.hdf5"))
    w = ts.whiten(fftlength=4, overlap=2).value; sr = int(ts.sample_rate.value)
    return np.asarray(w[sr * 2: -sr * 2], dtype=np.float64)

def bm(x, n):
    m = (len(x) // n) * n; return x[:m].reshape(-1, n).mean(axis=1)
def iqr(x):
    a, b = np.percentile(x, [25, 75]); return b - a
def slope(ns, ys):
    return np.polyfit(np.log(ns), np.log(ys), 1)[0]
def kurt(x):
    z = (x - x.mean()) / x.std(); return np.mean(z ** 4) - 3

H = white("H1"); L = white("L1"); n = min(len(H), len(L)); H, L = H[:n], L[:n]
v = {}

ns64 = [2 ** k for k in range(7)]
sH = slope(ns64, [iqr(bm(H, N)) for N in ns64]); sL = slope(ns64, [iqr(bm(L, N)) for N in ns64])
v["G1'"] = abs(sH + 0.5) <= 0.05 and abs(sL + 0.5) <= 0.05
say(f"G1': slope of block-mean IQR over N = 1..64, H1 {sH:.4f}, L1 {sL:.4f} -> {'not killed' if v[chr(71)+'1'+chr(39)] else 'KILLED'}")

ok = H != 0; r = L[ok] / H[ok]
c = iqr(L) / iqr(H)
med = np.median(np.abs(r)); q1, q3 = np.percentile(r, [25, 75])
v["G3'"] = all(abs(x / c - 1) <= 0.01 for x in (med, -q1, q3))
say(f"G3': c = IQR(L1)/IQR(H1) = {c:.4f}; median |r| {med:.4f}, quartiles {q1:.4f}, {q3:.4f} -> {'not killed' if v[chr(71)+'3'+chr(39)] else 'KILLED'}")

Hn, Ln = H / iqr(H), L / iqr(L); ok = Hn != 0; rn = Ln[ok] / Hn[ok]
m8 = np.median(np.abs(rn)); a8, b8 = np.percentile(rn, [25, 75])
ns = [2 ** k for k in range(11)]
s8 = slope(ns, [iqr(bm(rn, N)) for N in ns])
v["G8"] = abs(m8 - 1) <= 0.01 and abs(a8 + 1) <= 0.01 and abs(b8 - 1) <= 0.01 and abs(s8) <= 0.1
say(f"G8: drawn by order, median |r| {m8:.4f}, quartiles {a8:.4f}, {b8:.4f}, block-mean IQR slope {s8:.4f} -> {'not killed' if v['G8'] else 'KILLED'}")

phi = np.arctan2(L, H); D0 = kstest(phi, "uniform", args=(-np.pi, 2 * np.pi)).statistic
keep = np.abs(H) < np.quantile(np.abs(H), 0.999)
D1 = kstest(np.arctan2(L[keep], H[keep]), "uniform", args=(-np.pi, 2 * np.pi)).statistic
k0, k1 = kurt(H), kurt(H[keep])
v["G9"] = abs(D1 - D0) < 0.005 and k0 / k1 > 100
say(f"G9: angle's distance {D0:.5f} -> {D1:.5f} with the loudest 0.1% removed; H1 excess kurtosis {k0:.1f} -> {k1:.3f} -> {'not killed' if v['G9'] else 'KILLED'}")

say("summary: " + ", ".join(f"{k} {'ok' if x else 'killed'}" for k, x in v.items()))
with open(os.path.join(os.path.dirname(__file__), "lgo-run2.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
