"""SEP run 3: ethanol's 1H multiplets as overlapping Cauchys (SPN R1274; plans/sep-plan.md, run 3).
Data: BMRB bmse000297 set01 1H (fid, acqus), not committed; sha256 in the plan. Run from the root:
  python3 -I runs/sep/sep3.py <dir holding fid and acqus>"""
import sys, numpy as np, nmrglue as ng
from scipy.optimize import least_squares
d = sys.argv[1]
dic, data = ng.bruker.read(d)
data = ng.bruker.remove_digital_filter(dic, data)
a = dic['acqus']; SW = a['SW_h']; BF = a['BF1']; O1 = a['O1']; N = data.size
dt = 1 / SW; t = np.arange(N) * dt
out = []
def say(s): print(s, flush=True); out.append(s)
# frequency axis (Hz offset from the carrier) for the DFT, sign fixed by where the multiplets land
spec = np.fft.fftshift(np.fft.fft(data)) * dt
f = np.fft.fftshift(np.fft.fftfreq(N, dt))
for sign in (1, -1):
    ppm = (O1 + sign * f) / BF
    m3 = np.abs(spec[(ppm > 1.0) & (ppm < 1.35)]).max(); mb = np.median(np.abs(spec))
    if m3 > 50 * mb: break
say(f"400 MHz class: BF1 {BF} MHz, SW {SW:.1f} Hz, {N} complex points, frequency sign {sign}")
data = data if sign == 1 else np.conj(data)
spec = np.fft.fftshift(np.fft.fft(data)) * dt
ppm = (O1 + f) / BF
def peaks(lo, hi, n):
    sel = np.where((ppm > lo) & (ppm < hi))[0]; mag = np.abs(spec[sel])
    idx = [sel[i] for i in range(1, len(sel) - 1) if mag[i] > mag[i - 1] and mag[i] >= mag[i + 1]]
    idx = sorted(idx, key=lambda i: -np.abs(spec[i]))[:n]
    return sorted(f[i] for i in idx)
groups = {'CH3': (0.95, 1.20, 3, [1, 2, 1]), 'CH2': (3.40, 3.70, 4, [1, 3, 3, 1])}
# spinning sidebands: the water line's partners give the spin rate
iw = np.argmax(np.abs(spec) * ((ppm > 4.5) & (ppm < 4.9))); fw = f[iw]
sbw = [f[i] for i in range(iw - 80, iw + 81) if abs(abs(f[i] - fw) - 15) < 3 and np.abs(spec[i]) >= np.abs(spec[i - 1]) and np.abs(spec[i]) >= np.abs(spec[i + 1])]
OM = np.mean([abs(x - fw) for x in sbw]) if sbw else 15.0
say(f"spinning sidebands at +/- {OM:.3f} Hz (from the water line)")
res = {}
for name, (lo, hi, n, pat) in groups.items():
    f0 = np.array(peaks(lo, hi, n)); fc = f0.mean(); half = (f0[-1] - f0[0]) / 2 + 8
    w = np.abs(f - fc) < half; F = f[w]; S = spec[w]; om = 2 * np.pi * F
    def model(p):
        y = np.zeros_like(S)
        for k in range(n):
            ok, lg, cr, ci = p[4 * k:4 * k + 4]; g = np.exp(np.clip(lg, -5, 8)); c = cr + 1j * ci
            y = y + c / (g + 1j * (om - 2 * np.pi * ok))
        b = p[4 * n:]; return y + (b[0] + 1j * b[1]) + (b[2] + 1j * b[3]) * (F - fc)
    p0 = []
    for fk in f0:
        i = np.argmin(abs(F - fk)); g0 = 2 * np.pi * 0.5
        p0 += [fk, np.log(g0), (S[i] * g0).real, (S[i] * g0).imag]
    p0 = np.array(p0 + [0, 0, 0, 0])
    big = 50 * np.abs(S).max()
    lo_b, hi_b = [], []
    for fk in f0: lo_b += [fk - 3, np.log(0.5), -big, -big]; hi_b += [fk + 3, np.log(100), big, big]
    lo_b += [-big] * 4; hi_b += [big] * 4
    r = least_squares(lambda p: np.concatenate([(model(p) - S).real, (model(p) - S).imag]), p0, bounds=(lo_b, hi_b),
                      x_scale='jac', xtol=1e-14, ftol=1e-14, max_nfev=20000)
    p = r.x
    m1 = [(p[4 * k], np.exp(p[4 * k + 1]), abs(p[4 * k + 2] + 1j * p[4 * k + 3])) for k in range(n)]
    resid = np.sqrt(np.mean(np.abs(model(p) - S) ** 2)) / np.abs(S).max()
    # M2: matrix pencil on the decay shifted to the window, band-limited by a flat-topped window
    win = np.clip((half + 4 - np.abs(f - fc)) / 4, 0, 1)
    sub = np.fft.ifft(np.fft.ifftshift(spec * win)) / dt
    dec = max(1, int(SW / (4 * (half + 4)))); y = (sub * np.exp(-2j * np.pi * fc * t))[::dec]; y = y[:min(len(y), 1200)]
    L, M = len(y) // 3, 30
    Y = np.array([y[i:i + L + 1] for i in range(len(y) - L)])
    U, s_, Vh = np.linalg.svd(Y, full_matrices=False); V = Vh[:M].T
    z = np.linalg.eigvals(np.linalg.pinv(V[:-1]) @ V[1:])
    z = z[np.abs(z) < 1]
    A = np.power.outer(z, np.arange(len(y))).T; amp = np.linalg.lstsq(A, y, rcond=None)[0]
    fr = np.angle(z) / (2 * np.pi * dec * dt) + fc; gam = -np.log(np.abs(z)) / (dec * dt)
    m2 = []
    for fk in [x[0] for x in m1]:
        near = (np.abs(fr - fk) < 2.5) & (gam < 30)
        tot = amp[near].sum(); wa = np.abs(amp[near])
        pos = np.sum(fr[near] * wa) / wa.sum(); gm = np.sum(gam[near] * wa) / wa.sum()
        m2.append((pos, gm, abs(tot)))
    say(f"{name}: M2 poles assigned to lines: " + ", ".join(str(int(((np.abs(fr - x[0]) < 2.5) & (gam < 30)).sum())) for x in m1))
    res[name] = (m1, m2, pat, resid)
    say(f"{name}: M1 residual {resid:.2e} of the peak; lines (Hz, gamma 1/s, amount): " +
        "; ".join(f"{a:.3f} {b:.3f} {c:.4g}" for a, b, c in m1))
    say(f"{name}: M2 lines: " + "; ".join(f"{a:.3f} {b:.3f} {c:.4g}" for a, b, c in m2))
ok = {}
J = {}
for meth in (0, 1):
    for name in res:
        pos = np.array([x[0] for x in res[name][meth]]); J[(meth, name)] = np.diff(pos)
for meth, mname in ((0, 'M1'), (1, 'M2')):
    j3, j2 = J[(meth, 'CH3')], J[(meth, 'CH2')]
    say(f"N1 {mname}: spacings CH3 {np.round(j3, 3)}, CH2 {np.round(j2, 3)} Hz")
    allj = np.concatenate([j3, j2])
    ok[('N1', meth)] = (6.9 <= allj.min() and allj.max() <= 7.3 and abs(j3.mean() - j2.mean()) < 0.05)
    tot = {n: sum(x[2] for x in res[n][meth]) for n in res}
    ratio = tot['CH2'] / tot['CH3']; ok[('N2', meth)] = abs(ratio / (2 / 3) - 1) < 0.05
    say(f"N2 {mname}: CH2/CH3 = {ratio:.4f} (2/3 = 0.6667, off {100 * (ratio / (2 / 3) - 1):+.2f}%)")
    good = True
    for n in res:
        sh = np.array([x[2] for x in res[n][meth]]) / tot[n]; pat = np.array(res[n][2]) / sum(res[n][2])
        dev = sh / pat - 1; good &= np.all(np.abs(dev) < 0.10)
        say(f"N3 {mname} {n}: shares {np.round(sh, 4)} against {np.round(pat, 4)}, off {np.round(100 * dev, 2)}%")
        g = np.array([x[1] for x in res[n][meth]]); say(f"N5 {mname} {n}: widths gamma {np.round(g, 3)} /s, max/min {g.max() / g.min():.3f}")
        ok[('N5', meth, n)] = g.max() / g.min() <= 1.10
        hd = [np.arccosh(1 + (2 * np.pi * (res[n][meth][k + 1][0] - res[n][meth][k][0])) ** 2 / (2 * g[k] * g[k + 1]))
              for k in range(len(g) - 1)]
        say(f"   {n}: adjacent hyperbolic distances {np.round(hd, 2)}")
    ok[('N3', meth)] = good
line_dis, tot_dis = 0, 0
for n in res:
    a1 = np.array([x[2] for x in res[n][0]]); a2 = np.array([x[2] for x in res[n][1]])
    line_dis = max(line_dis, np.max(np.abs(a1 - a2) / a1)); tot_dis = max(tot_dis, abs(a1.sum() - a2.sum()) / a1.sum())
say(f"N4: methods disagree on single lines by up to {100 * line_dis:.3f}%, on totals by up to {100 * tot_dis:.3f}%")
v = {'N1': ok[('N1', 0)] and ok[('N1', 1)], 'N2': ok[('N2', 0)] and ok[('N2', 1)], 'N3': ok[('N3', 0)] and ok[('N3', 1)],
     'N4': line_dis > tot_dis, 'N5': all(val for k, val in ok.items() if k[0] == 'N5')}
for k, val in v.items(): say(f"{k}: {'not killed' if val else 'KILLED'}")
open('runs/sep/sep3-out.txt', 'w').write('\n'.join(out) + '\n')
