"""GMF run 1 (plans/gmf-plan.md): find the z in the geomagnetic field. Usage: python3 -I runs/gmf/gmf.py <datadir>"""
import sys, numpy as np
from scipy import signal, stats
dd = sys.argv[1]
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

def load(st):
    X, Y = [], []
    for line in open(f"{dd}/{st}.txt"):
        if not line[:4].isdigit(): continue
        p = line.split()
        x, y = float(p[3]), float(p[4])
        X.append(np.nan if x > 88880 else x); Y.append(np.nan if y > 88880 else y)
    return np.array(X), np.array(Y)

def segments(X, Y):
    """gaps over 5 min split; shorter gaps filled linearly; segments under 6 h dropped"""
    bad = np.isnan(X) | np.isnan(Y)
    segs, i, n = [], 0, len(X)
    while i < n:
        if bad[i]: i += 1; continue
        j = i; run_bad = 0; last_good = i
        while j < n:
            if bad[j]:
                run_bad += 1
                if run_bad > 5: break
            else:
                run_bad = 0; last_good = j
            j += 1
        segs.append((i, last_good + 1)); i = j
    return [(a, b) for a, b in segs if b - a >= 360]

def fill(v):
    v = v.copy(); idx = np.arange(len(v)); m = np.isnan(v)
    if m.any(): v[m] = np.interp(idx[m], idx[~m], v[~m])
    return v

BANDS = {"B1 (2.5-10 min; plan 2-10, Nyquist)": (1/600, 1/150), "B2 (10-60 min)": (1/3600, 1/600)}
fs = 1/60
def kd(a, b):  # KS distance between two samples
    return stats.ks_2samp(a, b).statistic

res = []
for st in ("BOU", "FRD", "CMO"):
    X, Y = load(st)
    miss = np.mean(np.isnan(X) | np.isnan(Y))
    say(f"{st}: {len(X)} minutes, missing {100*miss:.2f}%")
    if miss > 0.10:
        say(f"  dropped (more than 10% missing)"); continue
    segs = segments(X, Y)
    for bname, (lo, hi) in BANDS.items():
        sos = signal.butter(4, [lo, hi], btype='band', fs=fs, output='sos')
        fx, fy, ti = [], [], []
        for a, b in segs:
            x = signal.detrend(fill(X[a:b])); y = signal.detrend(fill(Y[a:b]))
            fx.append(signal.sosfiltfilt(sos, x)); fy.append(signal.sosfiltfilt(sos, y)); ti.append(np.arange(a, b))
        fx = np.concatenate(fx)[::2]; fy = np.concatenate(fy)[::2]; ti = np.concatenate(ti)[::2]
        half = len(X) // 2
        A = ti < half; B = ~A
        C = np.cov(fx[A], fy[A]); sx, sy = np.sqrt(C[0, 0]), np.sqrt(C[1, 1]); rho = C[0, 1] / (sx * sy)
        m = rho * sy / sx; g = (sy / sx) * np.sqrt(1 - rho**2)
        r = fy[B] / fx[B]
        D = stats.kstest(r, stats.cauchy(loc=m, scale=g).cdf).statistic
        q1, med, q3 = np.percentile(r, [25, 50, 75])
        # undone angle: whiten with half A's shape
        L = np.linalg.cholesky(C); W = np.linalg.solve(L, np.vstack([fx[B], fy[B]]))
        ang = np.mod(np.arctan2(W[1], W[0]), np.pi) / np.pi
        Dang = stats.kstest(ang, 'uniform').statistic
        # loudness by hour on half B
        hours = ti[B] // 60; uh = np.unique(hours)
        loud = np.array([np.sqrt(np.mean(fx[B][hours == h]**2 + fy[B][hours == h]**2)) for h in uh])
        qlo, qhi = np.percentile(loud, [25, 75])
        quiet = np.isin(hours, uh[loud <= qlo]); noisy = np.isin(hours, uh[loud >= qhi])
        Dr_loud = kd(r[quiet], r[noisy]); Dx_loud = kd(np.abs(fx[B][quiet]) / sx, np.abs(fx[B][noisy]) / sx)
        # amounts
        kx = stats.kurtosis(fx); ky = stats.kurtosis(fy)
        z = (fx - np.median(fx)); iqr = np.subtract(*np.percentile(fx, [75, 25]))
        Dcx = stats.kstest(z / (iqr / 2), 'cauchy').statistic
        Dgx = stats.kstest(fx / np.std(fx), 'norm').statistic
        say(f"  {bname}: m={m:.4f} g={g:.4f} rho={rho:.3f} sy/sx={sy/sx:.3f}; half B: D(r,Cauchy)={D:.4f} "
            f"median {med:.4f} quartiles {q1:.4f},{q3:.4f} (m-g {m-g:.4f}, m+g {m+g:.4f}); D(angle,uniform)={Dang:.4f}")
        say(f"     loud vs quiet: D(r)={Dr_loud:.4f}, D(|X|)={Dx_loud:.4f}; kurtosis X {kx:.1f} Y {ky:.1f}; "
            f"D(X, Cauchy)={Dcx:.3f}, D(X, Gauss)={Dgx:.3f}; n_B={B.sum()}")
        res.append(dict(st=st, band=bname, D=D, Dang=Dang, Dr=Dr_loud, Dx=Dx_loud, kx=kx, ky=ky, Dcx=Dcx))

n = len(res)
g1 = sum(1 for e in res if e['kx'] > 3 and e['ky'] > 3 and e['Dcx'] >= 0.05)
g2_fail = [e for e in res if e['D'] >= 0.03]
g3_fail = sum(1 for e in res if e['Dr'] >= 0.03)
g3_pass = sum(1 for e in res if e['Dr'] < 0.03 and e['Dx'] > 0.3)
g4_bad = [e for e in g2_fail if e['Dang'] < 0.03]
say(f"G1: {g1} of {n} meet it ->", "not killed" if g1 >= 4 else "KILLED")
say(f"G2: D >= 0.03 in {len(g2_fail)} of {n} ->", "KILLED" if len(g2_fail) >= 3 else "not killed")
say(f"G3: ratio D >= 0.03 in {g3_fail}; both parts met in {g3_pass} ->", "KILLED" if g3_fail >= 3 else ("not killed" if g3_pass >= 4 else "not killed in its kill clause, its pass clause short"))
say(f"G4: failures of G2 with the angle within 0.03 of uniform: {len(g4_bad)} ->", "KILLED" if g4_bad else "not killed")
say("G5: G2 failures at", [(e['st'], e['band']) for e in g2_fail])
open('runs/gmf/gmf-run1.txt', 'w').write("\n".join(out) + "\n")
