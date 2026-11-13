"""WND run 1: "find the z" in the wind. See plans/wnd-plan.md (method and predictions fixed there first).
Run: python3 -I runs/wnd/wnd.py <dir with STA.csv from IEM's ASOS one-minute archive>
"""
import sys, os, csv
import numpy as np
from scipy import stats

D = sys.argv[1]
STATIONS = ["DSM", "OKC", "DEN", "MSP", "BOS", "SFO"]
rng = np.random.default_rng(929)


def ks_cauchy(r, m, g):
    r = np.sort(r); n = r.size
    F = 0.5 + np.arctan((r - m) / g) / np.pi
    return max(np.max(np.arange(1, n + 1) / n - F), np.max(F - np.arange(n) / n))


def load(sta):
    day, hour, s, d = [], [], [], []
    with open(os.path.join(D, f"{sta}.csv")) as f:
        for row in csv.DictReader(f):
            try:
                dd = float(row["drct"]); ss = float(row["sknt"])
            except (ValueError, KeyError):
                continue
            if ss <= 0:
                continue
            t = row["valid(UTC)"]
            if not t.startswith("2026-10-"):
                continue
            day.append(int(t[8:10])); hour.append(int(t[11:13])); s.append(ss); d.append(dd)
    day, hour, s, d = map(np.array, (day, hour, s, d))
    s = s + rng.uniform(-0.5, 0.5, s.size); d = d + rng.uniform(-0.5, 0.5, d.size)
    s = np.clip(s, 1e-9, None)
    u = -s * np.sin(np.radians(d)); v = -s * np.cos(np.radians(d))
    return day, hour, u, v


results = []
for sta in STATIONS:
    day, hour, u, v = load(sta)
    key = day * 24 + hour
    xs, ys, hk, hd = [], [], [], []
    kept = 0
    for k in np.unique(key):
        sel = key == k
        if sel.sum() < 50:
            continue
        ub, vb = u[sel].mean(), v[sel].mean()
        sp = np.hypot(ub, vb)
        if sp < 5:
            continue
        kept += 1
        e = np.array([ub, vb]) / sp; c = np.array([-e[1], e[0]])
        du, dv = u[sel] - ub, v[sel] - vb
        xs.append(du * e[0] + dv * e[1]); ys.append(du * c[0] + dv * c[1])
        hk.append(np.full(sel.sum(), k)); hd.append(np.full(sel.sum(), day[sel][0]))
    x, y, hk, hd = map(np.concatenate, (xs, ys, hk, hd))
    A = hd <= 15; B = ~A
    C = np.cov(x[A], y[A]); sx, sy = np.sqrt(C[0, 0]), np.sqrt(C[1, 1]); rho = C[0, 1] / (sx * sy)
    m = rho * sy / sx; g = (sy / sx) * np.sqrt(1 - rho ** 2)
    xb, yb, kb = x[B], y[B], hk[B]
    ok = xb != 0
    r = yb[ok] / xb[ok]
    Dr = ks_cauchy(r, m, g)
    hours = np.unique(kb)
    loud = np.array([np.sqrt(np.mean(xb[kb == h] ** 2 + yb[kb == h] ** 2)) for h in hours])
    qlo, qhi = np.percentile(loud, [25, 75])
    mq = np.isin(kb, hours[loud <= qlo]) & ok; ml = np.isin(kb, hours[loud >= qhi]) & ok
    Dmr = stats.ks_2samp(yb[mq] / xb[mq], yb[ml] / xb[ml]).statistic
    Dmx = stats.ks_2samp(np.abs(xb[mq]) / sx, np.abs(xb[ml]) / sx).statistic
    kx, ky = stats.kurtosis(x), stats.kurtosis(y)
    xs_ = np.sort(x); n = xs_.size
    mc = np.median(x); gc = (np.percentile(x, 75) - np.percentile(x, 25)) / 2
    Fc = 0.5 + np.arctan((xs_ - mc) / gc) / np.pi
    Dxc = max(np.max(np.arange(1, n + 1) / n - Fc), np.max(Fc - np.arange(n) / n))
    print(f"== {sta}: {kept} hours kept, {x.size} minutes (half B {r.size}); rho {rho:+.3f}, sy/sx {sy/sx:.3f}, "
          f"z = {m:+.3f} + {g:.3f}i; D(r, Cauchy z) {Dr:.4f}, median r {np.median(r):+.3f}; "
          f"quiet/loud ({len(hours[loud <= qlo])} hours each): D ratio {Dmr:.4f}, D |x| {Dmx:.4f}; "
          f"kurtosis x {kx:.2f} y {ky:.2f}; x from Cauchy {Dxc:.4f}")
    results.append(dict(sta=sta, Dr=Dr, Dmr=Dmr, Dmx=Dmx, kx=kx, ky=ky, Dxc=Dxc))

w1 = sum(1 for q in results if q["kx"] > 3 and q["ky"] > 3 and q["Dxc"] >= 0.05)
print(f"W1: {'not killed' if w1 >= 4 else 'KILLED'}. heavy-tailed, not Cauchy at {w1} of 6 (needs 4)")
b2 = [q for q in results if q["Dr"] >= 0.03]
print(f"W2: {'KILLED' if len(b2) >= 3 else 'not killed'}. D >= 0.03 at {len(b2)}: " + ", ".join(f"{q['sta']} {q['Dr']:.3f}" for q in b2))
b3 = [q for q in results if q["Dmr"] >= 0.03]
both = sum(1 for q in results if q["Dmr"] < 0.03 and q["Dmx"] >= 5 * q["Dmr"])
print(f"W3: {'KILLED' if len(b3) >= 3 else 'not killed'}. ratio loud vs quiet >= 0.03 at {len(b3)}: "
      + ", ".join(f"{q['sta']} {q['Dmr']:.3f}" for q in b3) + f"; both parts met at {both} of 6")
