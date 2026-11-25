# PHR run 1: is a resonance's line the rate its phase turns? (plans/phr-plan.md)
# Usage: python3 runs/phr/phr.py <path to VWireStudyData/RawScans/Wire>
import sys, glob, os, numpy as np, sympy as sp
from scipy.optimize import curve_fit

# Q1, exact
w, w0, G = sp.symbols('omega omega0 Gamma', positive=True)
A = sp.symbols('A', positive=True)
chi = A/(w0 - w - sp.I*G/2)
phi = sp.atan((G/2)/(w0 - w))
q1 = sp.simplify(sp.diff(phi, w) - (G/2)*sp.Abs(chi)**2/A**2)
print('Q1 one pole: dphi/dw - (G/2)|chi|^2/|A|^2 =', sp.simplify(q1.rewrite(sp.re)))
g = sp.symbols('gamma', positive=True)
# driven oscillator chi = 1/(w0^2 - w^2 - i g w): its phase arg(chi) has
D = (w0**2 - w**2)**2 + (g*w)**2
dphi2 = g*(w0**2 + w**2)/D          # d arg(chi)/dw, checked against the arctan form below
chk = sp.simplify(sp.diff(sp.atan(g*w/(w0**2 - w**2)), w) - dphi2)
print('Q1 oscillator: d/dw atan(gw/(w0^2-w^2)) - g(w0^2+w^2)/D =', chk)
# so (dphi/dw)/|chi|^2 = g(w0^2 + w^2), varying over w0 +- g by
for Q in (10, 100, 1000):
    gg = 1.0/Q
    v = ((1+(1+gg)**2)/(1+(1-gg)**2)) - 1
    print(f'Q1 oscillator Q={Q}: (dphi/dw)/|chi|^2 varies by {v:.4e} over w0 +- gamma; 2 gamma/w0 = {2*gg:.4e}')

def lor(f, a, f0, hw): return a/((f-f0)**2 + hw**2)

root = sys.argv[1]
files = sorted(glob.glob(os.path.join(root, '02_Precision', '*.txt')) + glob.glob(os.path.join(root, '03_FieldReconstr', '*.txt')))
rows = []
for fn in files:
    try:
        d = np.genfromtxt(fn, delimiter=',', names=True)
    except Exception as e:
        continue
    if d.size < 20 or 'Frequency' not in d.dtype.names: continue
    f = d['Frequency']; o = np.argsort(f); f = f[o]
    for ch in (1, 2):
        z = (d[f'MeanX{ch}'] + 1j*d[f'MeanY{ch}'])[o]
        n = len(f); k = max(3, int(0.2*n))
        idx = np.r_[0:k, n-k:n]
        cr = np.polyfit(f[idx], z.real[idx], 1); ci = np.polyfit(f[idx], z.imag[idx], 1)
        zc = z - (np.polyval(cr, f) + 1j*np.polyval(ci, f))
        p = np.abs(zc)**2
        noise = np.sqrt(np.mean(p[idx]**2))
        if p.max() < 20*noise: rows.append((fn, ch, 'noise')); continue
        i0 = p.argmax(); half = p[i0]/2
        above = np.where(p >= half)[0]
        fw = f[above.max()] - f[above.min()]
        if fw <= 0: fw = np.median(np.diff(f))
        try:
            popt, _ = curve_fit(lor, f, p, p0=[p[i0]*(fw/2)**2, f[i0], fw/2], maxfev=20000)
        except Exception:
            rows.append((fn, ch, 'nofit')); continue
        a, f0, hw = popt; hw = abs(hw); Gam = 2*hw
        if f[0] > f0 - 2*Gam or f[-1] < f0 + 2*Gam: rows.append((fn, ch, 'narrow')); continue
        win = (f > f0-2*Gam) & (f < f0+2*Gam)
        resid = np.sqrt(np.mean((p[win]-lor(f[win], *popt))**2))/lor(f0, *popt)
        ph = np.unwrap(np.angle(zc))
        dph = np.gradient(ph, f)
        step = np.median(np.diff(f)); m = int(max(1, (Gam/10)//step))
        if m > 1: dph = np.convolve(dph, np.ones(m)/m, mode='same')
        sgn = np.sign(np.sum(dph[win])); dph = sgn*dph
        diff = np.sqrt(np.mean((dph[win]/dph[win].max() - p[win]/p[win].max())**2))
        G_phase_peak = 2/dph[win].max()/(2*np.pi) * (2*np.pi)  # dphi/df peak = 2/Gamma_f
        # span from pi/4 to 3pi/4 of the total turn
        phs = sgn*ph; tot = phs[-k:].mean() - phs[:k].mean()
        rel = (phs - phs[:k].mean())/tot
        try:
            fa = np.interp(0.25, rel[win], f[win]); fb = np.interp(0.75, rel[win], f[win])
            G_span = fb - fa
        except Exception: G_span = np.nan
        t_half = np.interp(f0+Gam/2, f, phs) - np.interp(f0-Gam/2, f, phs)
        rows.append((fn, ch, 'ok', f0, Gam, resid, diff, G_phase_peak/Gam-1, G_span/Gam-1, np.degrees(tot), np.degrees(t_half), Gam/step))

ok = [r for r in rows if r[2]=='ok']
from collections import Counter
print('channels:', len(rows), Counter(r[2] for r in rows))
lorz = [r for r in ok if r[5] < 0.02]
print('analysed', len(ok), '; Lorentzian (resid<2%)', len(lorz))
def frac(lst, pred): return sum(1 for r in lst if pred(r)), len(lst)
print('Q2 diff>5% among Lorentzian:', frac(lorz, lambda r: r[6] > 0.05))
print('Q3 phase-peak Gamma off >5%:', frac(lorz, lambda r: abs(r[7]) > 0.05))
print('Q3 phase-span Gamma off >5%:', frac(lorz, lambda r: not abs(r[8]) <= 0.05))
print('Q4 total turn off pi by >10 deg:', frac(lorz, lambda r: abs(abs(r[9])-180) > 10))
print('Q4 half-width turn off 90 by >5 deg:', frac(lorz, lambda r: abs(r[10]-90) > 5))
if ok:
    a = np.array([r[3:] for r in ok], float)
    print('medians over analysed: f0 %.1f Gamma %.3f resid %.4f diff %.4f Gpk %.3f Gspan %.3f turn %.1f half %.1f pts/Gamma %.1f' % tuple(np.median(a, axis=0)))
    for name, col in (('resid',2),('diff',3),('Gpk',4),('Gspan',5),('turn',6),('half',7),('ptsPerGamma',8)):
        print(f'  {name}: quartiles', np.round(np.percentile(a[:, col], [25, 50, 75]), 4))
