"""LGO run 1: LIGO noise read through the address and the payload (plans/lgo-plan.md).

Run from the repository's root:  python3 runs/lgo/lgo.py
Needs gwpy (GWOSC open data). The fetched strain is cached outside the repo (LGO_CACHE, default /tmp/lgo-cache).
"""
import hashlib, os, sys
import numpy as np
from scipy.stats import cauchy, norm, t as student, kstest

GPS, DUR = 1257000000, 512
CACHE = os.environ.get("LGO_CACHE", "/tmp/lgo-cache")
os.makedirs(CACHE, exist_ok=True)
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def strain(det):
    from gwpy.timeseries import TimeSeries
    path = os.path.join(CACHE, f"{det}-{GPS}-{DUR}.hdf5")
    if os.path.exists(path):
        ts = TimeSeries.read(path)
    else:
        ts = TimeSeries.fetch_open_data(det, GPS, GPS + DUR, verbose=False)
        ts.write(path)
    raw = np.asarray(ts.value, dtype=np.float64)
    say(f"{det}: {len(raw)} samples at {ts.sample_rate}, sha256 of float64 strain {hashlib.sha256(raw.tobytes()).hexdigest()}")
    w = ts.whiten(fftlength=4, overlap=2).value
    sr = int(ts.sample_rate.value)
    return np.asarray(w[sr * 2: -sr * 2], dtype=np.float64)

def block_means(x, n):
    m = (len(x) // n) * n
    return x[:m].reshape(-1, n).mean(axis=1)

def iqr(x):
    q1, q3 = np.percentile(x, [25, 75]); return q3 - q1

def slope(ns, ys):
    return np.polyfit(np.log(ns), np.log(ys), 1)[0]

H = strain("H1"); L = strain("L1")
n = min(len(H), len(L)); H, L = H[:n], L[:n]
say(f"whitened and trimmed: {n} samples each; H1 sd {H.std():.4f}, L1 sd {L.std():.4f}")
verdict = {}

# G0: the old script's comparison, on H1 (its accumulated_residuals and fit_and_compare)
say("\nG0, the old comparison (H1): N, ΔLL Cauchy − Gaussian")
levels = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
dll = []
for N in levels:
    a = block_means(H, N); r = (a - a.mean()) / a.std()
    cl, cs = cauchy.fit(r); gl, gs = norm.fit(r)
    d = np.sum(cauchy.logpdf(r, cl, cs)) - np.sum(norm.logpdf(r, gl, gs)); dll.append(d)
    say(f"  {N:5d}  {len(r):8d}  {d:+.1f}")
verdict["G0"] = dll[0] > 0
say(f"G0 {'not killed' if verdict['G0'] else 'KILLED'}: ΔLL at N = 1 is {dll[0]:+.1f}")

# G1: the amounts' block means shrink
ns = [2 ** k for k in range(11)]
iq = [iqr(block_means(H, N)) for N in ns]
s1 = slope(ns, iq)
say("\nG1, IQR of H1 block means: " + ", ".join(f"{N}:{v:.4g}" for N, v in zip(ns, iq)))
verdict["G1"] = s1 <= -0.4 and abs(s1 + 0.5) <= 0.05
say(f"G1 {'not killed' if verdict['G1'] else 'KILLED'}: slope {s1:.4f} (predicted −0.5 ± 0.05; killed above −0.4)")

# G2: a Student-t at N = 1, against the Cauchy
r1 = (H - H.mean()) / H.std()
df, tl, ts_ = student.fit(r1)
ll_t = np.sum(student.logpdf(r1, df, tl, ts_))
cl, cs = cauchy.fit(r1); ll_c = np.sum(cauchy.logpdf(r1, cl, cs))
gl, gs = norm.fit(r1); ll_g = np.sum(norm.logpdf(r1, gl, gs))
k4 = np.mean(r1 ** 4) - 3
say(f"\nG2, H1 at N = 1: t ν = {df:.3f}, scale {ts_:.4f}; LL t − Cauchy {ll_t - ll_c:+.1f}, t − Gaussian {ll_t - ll_g:+.1f}; excess kurtosis {k4:.3f}")
verdict["G2"] = df > 2 and (ll_t - ll_c) > 100
say(f"G2 {'not killed' if verdict['G2'] else 'KILLED'}")

# G3: the direction's reading r = L1/H1
ok = H != 0
r = L[ok] / H[ok]
med = np.median(np.abs(r)); q1, q3 = np.percentile(r, [25, 75])
say(f"\nG3, r = L1/H1: median |r| {med:.4f}, quartiles {q1:.4f}, {q3:.4f}")
verdict["G3"] = abs(med - 1) <= 0.05 and abs(q1 + 1) <= 0.05 and abs(q3 - 1) <= 0.05
say(f"G3 {'not killed' if verdict['G3'] else 'KILLED'}")

# G4: the angle uniform
phi = np.arctan2(L, H)
D = kstest(phi, "uniform", args=(-np.pi, 2 * np.pi)).statistic
say(f"\nG4, φ = atan2(L1, H1): Kolmogorov distance from uniform {D:.5f}")
verdict["G4"] = D < 0.02
say(f"G4 {'not killed' if verdict['G4'] else 'KILLED'}")

# G5: averaging the direction gains nothing
iqr_r = [iqr(block_means(r, N)) for N in ns]
s5 = slope(ns, iqr_r)
say("\nG5, IQR of r block means: " + ", ".join(f"{N}:{v:.4g}" for N, v in zip(ns, iqr_r)))
verdict["G5"] = abs(s5) <= 0.1
say(f"G5 {'not killed' if verdict['G5'] else 'KILLED'}: slope {s5:.4f} (predicted 0 ± 0.1)")

# G6: the drawing sets the corner
g6 = []
for c in (0.5, 2.0):
    m = np.median(np.abs(c * r)); g6.append(abs(m - c) <= 0.05 * c)
    say(f"G6, c = {c}: median |c·r| {m:.4f}")
verdict["G6"] = all(g6)
say(f"G6 {'not killed' if verdict['G6'] else 'KILLED'}")

verdict["G7"] = verdict["G1"] and verdict["G2"] and verdict["G5"]
say(f"\nG7 (the verdict) {'not killed' if verdict['G7'] else 'KILLED'}")
say("summary: " + ", ".join(f"{k} {'ok' if v else 'killed'}" for k, v in verdict.items()))

with open(os.path.join(os.path.dirname(__file__), "lgo-run1.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
