"""LGO run 3 (plans/lgo-plan.md): three new segments, predictions L1–L5 fixed and committed before the data.

Run from the repository's root:  python3 runs/lgo/lgo3.py
Needs gwpy (GWOSC open data). Strain is cached outside the repo (LGO_CACHE). If the proxy's CA bundle does not cover
gwosc.org, point REQUESTS_CA_BUNDLE / SSL_CERT_FILE at it joined with certifi's (as in run 1); verification stays on.
"""
import os, hashlib
import numpy as np
from scipy.stats import kstest, ks_2samp
from gwpy.timeseries import TimeSeries

DUR = 512
STARTS = [1240000000, 1250000000, 1262000000]
CACHE = os.environ.get("LGO_CACHE", "/tmp/lgo-cache"); os.makedirs(CACHE, exist_ok=True)
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); out.append(s)

def fetch(det, gps):
    path = os.path.join(CACHE, f"{det}-{gps}-{DUR}.hdf5")
    if os.path.exists(path):
        return TimeSeries.read(path)
    ts = TimeSeries.fetch_open_data(det, gps, gps + DUR, verbose=False)
    ts.write(path, overwrite=True)
    return ts

def white(ts):
    w = ts.whiten(fftlength=4, overlap=2).value; sr = int(ts.sample_rate.value)
    return np.asarray(w[sr * 2: -sr * 2], dtype=np.float64)

def bm(x, n):
    m = (len(x) // n) * n; return x[:m].reshape(-1, n).mean(axis=1)
def iqr(x):
    a, b = np.percentile(x, [25, 75]); return b - a
def slope(ns, ys):
    return np.polyfit(np.log(ns), np.log(ys), 1)[0]

allv = {}
for S in STARTS:
    gps = None
    for k in range(40):
        g = S + 512 * k
        try:
            h, l = fetch("H1", g), fetch("L1", g)
        except Exception as e:
            say(f"  {g}: not available ({type(e).__name__})"); continue
        if np.isnan(h.value).any() or np.isnan(l.value).any() or len(h) != len(l):
            say(f"  {g}: gap or NaN"); continue
        gps = g; break
    if gps is None:
        say(f"segment from {S}: none found in 40 tries"); allv[S] = None; continue
    say(f"segment {gps}: H1 sha256 {hashlib.sha256(h.value.tobytes()).hexdigest()}")
    say(f"segment {gps}: L1 sha256 {hashlib.sha256(l.value.tobytes()).hexdigest()}")
    H, L = white(h), white(l); n = min(len(H), len(L)); H, L = H[:n], L[:n]
    sr = int(h.sample_rate.value)
    v = {}
    ns64 = [2 ** k for k in range(7)]
    sH = slope(ns64, [iqr(bm(H, N)) for N in ns64]); sL = slope(ns64, [iqr(bm(L, N)) for N in ns64])
    v["L1"] = abs(sH + 0.5) <= 0.07 and abs(sL + 0.5) <= 0.07
    say(f"  L1: block-mean IQR slope N=1..64, H1 {sH:.4f}, L1 {sL:.4f}")
    Hn, Ln = H / iqr(H), L / iqr(L); ok = Hn != 0; rn = Ln[ok] / Hn[ok]
    ns = [2 ** k for k in range(11)]
    s2 = slope(ns, [iqr(bm(rn, N)) for N in ns])
    v["L2"] = abs(s2) <= 0.1
    say(f"  L2: block-mean IQR slope of r, N=1..1024, {s2:.4f}")
    m3 = np.median(np.abs(rn)); a3, b3 = np.percentile(rn, [25, 75])
    v["L3"] = abs(m3 - 1) <= 0.01 and abs(a3 + 1) <= 0.01 and abs(b3 - 1) <= 0.01
    say(f"  L3: drawn, median |r| {m3:.4f}, quartiles {a3:.4f}, {b3:.4f}")
    ok = H != 0; r = L[ok] / H[ok]; c = iqr(L) / iqr(H)
    m4 = np.median(np.abs(r)); a4, b4 = np.percentile(r, [25, 75])
    v["L4"] = all(abs(x / c - 1) <= 0.01 for x in (m4, -a4, b4))
    say(f"  L4: c {c:.4f}; undrawn median |r| {m4:.4f}, quartiles {a4:.4f}, {b4:.4f}")
    phi = np.arctan2(Ln, Hn); phis = np.arctan2(np.roll(Ln, 8 * sr), Hn)
    Ds = kstest(phi, "uniform", args=(-np.pi, 2 * np.pi)).statistic
    Dh = kstest(phis, "uniform", args=(-np.pi, 2 * np.pi)).statistic
    D2 = ks_2samp(phi, phis).statistic
    v["L5"] = abs(Ds - Dh) <= 0.001 and D2 <= 0.003
    say(f"  L5: D_sim {Ds:.5f}, D_shift {Dh:.5f}, |diff| {abs(Ds-Dh):.5f}, two-sample {D2:.5f}; 1.36/sqrt(N) = {1.36/np.sqrt(len(phi)):.5f}")
    say(f"  segment {gps}: " + ", ".join(f"{k} {'not killed' if x else 'KILLED'}" for k, x in v.items()))
    allv[gps] = v

say("summary: " + "; ".join(f"{g}: " + (", ".join(f"{k} {'ok' if x else 'killed'}" for k, x in v.items()) if v else "no data") for g, v in allv.items()))
with open(os.path.join(os.path.dirname(__file__), "lgo-run3.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
