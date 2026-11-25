# PHR run 2: data set 2, one notch resonator (plans/phr-plan.md). The same preprocessing and measures as phr.py.
# Usage: python3 runs/phr/phr2.py <path to online_data/Fig1c/resonance_curve.dat>
import sys, numpy as np
from scipy.optimize import curve_fit
def lor(f, a, f0, hw): return a/((f-f0)**2 + hw**2)
d = np.loadtxt(sys.argv[1], delimiter=',', comments='#')
f = d[:, 0]*1e9; z = d[:, 2] + 1j*d[:, 3]; o = np.argsort(f); f, z = f[o], z[o]
n = len(f); k = max(3, int(0.2*n)); idx = np.r_[0:k, n-k:n]
cr = np.polyfit(f[idx], z.real[idx], 1); ci = np.polyfit(f[idx], z.imag[idx], 1)
zc = z - (np.polyval(cr, f) + 1j*np.polyval(ci, f))
p = np.abs(zc)**2; noise = np.sqrt(np.mean(p[idx]**2))
print('points', n, 'peak/noise', p.max()/noise)
i0 = p.argmax(); above = np.where(p >= p[i0]/2)[0]; fw = f[above.max()] - f[above.min()]
popt, _ = curve_fit(lor, f, p, p0=[p[i0]*(fw/2)**2, f[i0], fw/2], maxfev=20000)
a, f0, hw = popt; hw = abs(hw); G = 2*hw; step = np.median(np.diff(f))
print(f'f0 {f0/1e9:.6f} GHz  Gamma {G/1e6:.4f} MHz  points per Gamma {G/step:.1f}  covers +-2G: {f[0] < f0-2*G and f[-1] > f0+2*G}')
win = (f > f0-2*G) & (f < f0+2*G)
resid = np.sqrt(np.mean((p[win]-lor(f[win], *popt))**2))/lor(f0, *popt)
ph = np.unwrap(np.angle(zc)); dph = np.gradient(ph, f)
m = int(max(1, (G/10)//step))
if m > 1: dph = np.convolve(dph, np.ones(m)/m, mode='same')
sgn = np.sign(np.sum(dph[win])); dph = sgn*dph
diff = np.sqrt(np.mean((dph[win]/dph[win].max() - p[win]/p[win].max())**2))
Gpk = 2/dph[win].max()
phs = sgn*ph; tot = phs[-k:].mean() - phs[:k].mean(); rel = (phs - phs[:k].mean())/tot
fa = np.interp(0.25, rel[win], f[win]); fb = np.interp(0.75, rel[win], f[win])
half = np.interp(f0+G/2, f, phs) - np.interp(f0-G/2, f, phs)
print(f'Lorentzian rms residual {resid:.4f} (Q2 needs < 0.02 to apply)')
print(f'Q2 scaled rms difference {diff:.4f} (killed if > 0.05)')
print(f'Q3 Gamma from phase peak / amplitude - 1 = {Gpk/G-1:+.4f}; from phase span = {(fb-fa)/G-1:+.4f} (killed if |.| > 0.05)')
print(f'Q4 total turn {np.degrees(tot):.1f} deg (killed if off 180 by > 10); within +-G/2 {np.degrees(half):.1f} deg (killed if off 90 by > 5)')
# post hoc, not judged: the same with dphi/df smoothed over 3 points
dph3 = np.convolve(sgn*np.gradient(ph, f), np.ones(3)/3, mode='same')
print(f'post hoc: 3-point smoothing, scaled rms difference {np.sqrt(np.mean((dph3[win]/dph3[win].max() - p[win]/p[win].max())**2)):.4f}')
