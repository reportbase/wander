"""SMN run 1: "find the z" on ambient seismic noise. See plans/smn-plan.md (method and predictions fixed there first).

Two horizontal channels (BH1 = x, BH2 = y) at IU.ANMO, IU.KONO, IU.HRV, 2026-09-01 to 09-08, bands 0.1-0.3 Hz and 1-4 Hz.
z = m + i*gamma from half A's covariance; the ratio y/x on half B against Cauchy(m, gamma); the loudest quarter of hours
against the quietest; the amounts' kurtosis and their distance from a Cauchy.
Run: python3 -I runs/smn/smn.py <dir with IU.<STA>.00.BH1.mseed and .BH2.mseed>
"""
import sys, os
import numpy as np
from obspy import read, UTCDateTime
from scipy import stats

D = sys.argv[1]
T0, T1 = UTCDateTime("2026-09-01T00:00:00"), UTCDateTime("2026-09-08T00:00:00")
THALF = T0 + 3.5 * 86400
BANDS = {"B1 0.1-0.3 Hz": (0.1, 0.3), "B2 1-4 Hz": (1.0, 4.0)}
STATIONS = ["ANMO", "KONO", "HRV"]


def segments(sta):
    a = read(os.path.join(D, f"IU.{sta}.00.BH1.mseed")); b = read(os.path.join(D, f"IU.{sta}.00.BH2.mseed"))
    for s in (a, b):
        s.merge(method=1)
    a = a.split(); b = b.split()
    out = []
    for ta in a:
        for tb in b:
            s0 = max(ta.stats.starttime, tb.stats.starttime, T0); s1 = min(ta.stats.endtime, tb.stats.endtime, T1)
            if s1 - s0 >= 3600:
                x = ta.copy().trim(s0, s1); y = tb.copy().trim(s0, s1)
                n = min(x.stats.npts, y.stats.npts)
                x.data = x.data[:n].astype(float); y.data = y.data[:n].astype(float)
                out.append((x, y))
    return out


def prepared(segs, band):
    xs, ys, ts = [], [], []
    for x0, y0 in segs:
        x, y = x0.copy(), y0.copy()
        for tr in (x, y):
            tr.detrend("demean"); tr.detrend("linear")
            tr.filter("bandpass", freqmin=band[0], freqmax=band[1], corners=4, zerophase=True)
        t = x.stats.starttime.timestamp + np.arange(x.stats.npts) / x.stats.sampling_rate
        xs.append(x.data[::10]); ys.append(y.data[::10]); ts.append(t[::10])
    return np.concatenate(xs), np.concatenate(ys), np.concatenate(ts)


def ks_cauchy(r, m, g):
    r = np.sort(r); n = r.size
    F = 0.5 + np.arctan((r - m) / g) / np.pi
    return max(np.max(np.arange(1, n + 1) / n - F), np.max(F - np.arange(n) / n))


def ks_uniform(a):  # a in [0, pi)
    a = np.sort(a) / np.pi; n = a.size
    return max(np.max(np.arange(1, n + 1) / n - a), np.max(a - np.arange(n) / n))


results = []
for sta in STATIONS:
    segs = segments(sta)
    print(f"== {sta}: {len(segs)} common segments, {sum(s[0].stats.npts for s in segs) / 40 / 86400:.2f} days")
    for bname, band in BANDS.items():
        x, y, t = prepared(segs, band)
        A = t < THALF.timestamp; B = ~A
        C = np.cov(x[A], y[A]); sx, sy = np.sqrt(C[0, 0]), np.sqrt(C[1, 1]); rho = C[0, 1] / (sx * sy)
        m = rho * sy / sx; g = (sy / sx) * np.sqrt(1 - rho ** 2)
        xb, yb, tb = x[B], y[B], t[B]
        ok = xb != 0
        r = yb[ok] / xb[ok]
        Dr = ks_cauchy(r, m, g)
        med = np.median(r); q1, q3 = np.percentile(r, [25, 75])
        # the undone angle: half A's shape removed
        L = np.linalg.cholesky(C); Li = np.linalg.inv(L)
        u = Li @ np.vstack([xb, yb]); ang = np.mod(np.arctan2(u[1], u[0]), np.pi)
        Da = ks_uniform(ang)
        # loud and quiet hours of half B
        hr = np.floor((tb - T0.timestamp) / 3600).astype(int)
        hours = np.unique(hr)
        loud = np.array([np.sqrt(np.mean(xb[hr == h] ** 2 + yb[hr == h] ** 2)) for h in hours])
        qlo, qhi = np.percentile(loud, [25, 75])
        quiet_h = set(hours[loud <= qlo]); loud_h = set(hours[loud >= qhi])
        mq = np.isin(hr, list(quiet_h)) & ok; ml = np.isin(hr, list(loud_h)) & ok
        Dmix_r = stats.ks_2samp(yb[mq] / xb[mq], yb[ml] / xb[ml]).statistic
        Dmix_x = stats.ks_2samp(np.abs(xb[mq]) / sx, np.abs(xb[ml]) / sx).statistic
        # the amounts
        kx, ky = stats.kurtosis(x), stats.kurtosis(y)
        xs = np.sort(x); n = xs.size
        mc = np.median(x); gc = (np.percentile(x, 75) - np.percentile(x, 25)) / 2
        Fc = 0.5 + np.arctan((xs - mc) / gc) / np.pi
        Dxc = max(np.max(np.arange(1, n + 1) / n - Fc), np.max(Fc - np.arange(n) / n))
        Fg = stats.norm.cdf(xs, np.mean(x), np.std(x))
        Dxg = max(np.max(np.arange(1, n + 1) / n - Fg), np.max(Fg - np.arange(n) / n))
        print(f"  {bname}: rho {rho:+.3f}, sy/sx {sy/sx:.3f}, z = {m:+.3f} + {g:.3f}i; half B n {r.size}: "
              f"D(r, Cauchy z) {Dr:.4f}, median {med:+.3f} (m {m:+.3f}), quartiles {q1:+.3f} {q3:+.3f} "
              f"(m-g {m-g:+.3f}, m+g {m+g:+.3f}); angle D from uniform {Da:.4f}; quiet/loud hours ({len(quiet_h)} each): "
              f"D ratio {Dmix_r:.4f}, D |x| {Dmix_x:.4f}; kurtosis x {kx:.2f} y {ky:.2f}; x from Cauchy {Dxc:.4f}, from Gauss {Dxg:.4f}")
        results.append(dict(sta=sta, band=bname, Dr=Dr, Da=Da, Dmr=Dmix_r, Dmx=Dmix_x, kx=kx, ky=ky, Dxc=Dxc))

n1 = sum(1 for q in results if q["kx"] > 3 and q["ky"] > 3 and q["Dxc"] >= 0.05)
print(f"N1: {'not killed' if n1 >= 4 else 'KILLED'}. amounts heavy-tailed and not Cauchy in {n1} of {len(results)} (needs 4)")
bad2 = [q for q in results if q["Dr"] >= 0.03]
print(f"N2: {'KILLED' if len(bad2) >= 3 else 'not killed'}. D(r, Cauchy) >= 0.03 in {len(bad2)} of {len(results)}: "
      + ", ".join(f"{q['sta']} {q['band'][:2]} {q['Dr']:.3f}" for q in bad2))
bad3 = [q for q in results if q["Dmr"] >= 0.03]
both3 = sum(1 for q in results if q["Dmr"] < 0.03 and q["Dmx"] > 0.3)
print(f"N3: {'KILLED' if len(bad3) >= 3 else 'not killed'}. ratio loud vs quiet D >= 0.03 in {len(bad3)}; "
      f"ratio < 0.03 with |x| > 0.3 in {both3} of {len(results)}")
k4 = [q for q in bad2 if q["Da"] < 0.03]
b1 = sum(1 for q in bad2 if q["band"].startswith("B1")); b2 = len(bad2) - b1
print(f"N4: {'KILLED' if k4 else 'not killed'}. N2 failures with the angle within 0.03 of uniform: {len(k4)}; "
      f"failures in B1 {b1}, in B2 {b2}")
