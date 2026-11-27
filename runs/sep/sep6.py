"""SEP run 6: a counted Cu Ka doublet across a powder pattern (SPN R1280; plans/sep-plan.md).
Run from the root: python3 -I runs/sep/sep5.py <path to PBSO4.XRA>"""
import sys, numpy as np
from scipy.optimize import minimize
out = []
def say(s): print(s, flush=True); out.append(s)
raw = open(sys.argv[1]).read().splitlines()
hdr = raw[1].split(); n = int(hdr[2]); start, step = float(hdr[5]) / 100, float(hdr[6]) / 100
vals = []
for line in raw[2:]:
    for k in range(0, len(line), 8):
        f = line[k:k + 8].strip()
        if f: vals.append(float(f))
y = np.array(vals[:n]); x = start + step * np.arange(n)
say(f"{n} points, {x[0]:.3f} to {x[-1]:.3f} deg, step {step}; counts {y.min():.0f} to {y.max():.0f}")
L1, L2 = 1.540598, 1.544426; a, b, c = 8.480, 5.398, 6.958
def allowed(h, k, l):
    if h == 0 and (k + l) % 2: return False
    if l == 0 and h % 2: return False
    if k == 0 and l == 0 and h % 2: return False
    if h == 0 and l == 0 and k % 2: return False
    if h == 0 and k == 0 and l % 2: return False
    return True
pos = []
for h in range(0, 15):
    for k in range(0, 10):
        for l in range(0, 13):
            if h == k == l == 0 or not allowed(h, k, l): continue
            d = 1 / np.sqrt(h * h / a ** 2 + k * k / b ** 2 + l * l / c ** 2)
            s = L1 / (2 * d)
            if s < 1:
                tt = 2 * np.degrees(np.arcsin(s))
                if x[0] + 1 < tt < x[-1] - 1: pos.append((tt, (h, k, l)))
pos.sort(); P = np.array([p[0] for p in pos])
def spacing(tt): th = np.radians(tt / 2); return np.degrees(2 * np.tan(th) * (L2 - L1) / L1)
def lor(xx, m, g): return g / (np.pi * ((xx - m) ** 2 + g * g))
def model5(q, xx, x0, D):
    b0, b1, m1, g, A1, A2 = q
    return b0 + b1 * (xx - x0) + A1 * lor(xx, m1, g) + A2 * lor(xx, m1 + D, g)
rows = []
for tt, hkl in pos:
    D = spacing(tt); iso = max(0.5, 3 * D)
    if np.any((np.abs(P - tt) < iso) & (np.abs(P - tt) > 1e-6)): continue
    half = 0.4 + 2 * D; w = (x > tt - half) & (x < tt + half + D)
    xx, yy = x[w], y[w]
    if len(xx) < 20: continue
    edge = np.r_[yy[:5], yy[-5:]]; bg = np.median(edge)
    near = np.abs(xx - tt) < 0.15
    if not near.any() or yy[near].max() - bg < 20 * np.sqrt(max(bg, 1)): continue
    m1 = xx[near][np.argmax(yy[near])]; hgt = yy[near].max() - bg; g0 = 0.04
    p0 = [bg, 0, m1, g0, hgt * np.pi * g0 / 1.5, hgt * np.pi * g0 / 3]
    x0 = m1
    def nll(q):
        mu = model5(q, xx, x0, D)
        if np.any(mu <= 0): return 1e30
        return np.sum(mu - yy * np.log(mu))
    bnds = [(0, None), (None, None), (m1 - 0.1, m1 + 0.1), (0.003, 0.5), (0, None), (0, None)]
    r = minimize(nll, p0, method='L-BFGS-B', bounds=bnds, options={'maxiter': 20000, 'maxfun': 200000})
    r = minimize(nll, r.x, method='Nelder-Mead', options={'maxiter': 40000, 'xatol': 1e-9, 'fatol': 1e-9})
    q = r.x; mu = model5(q, xx, x0, D); h = 1e-6
    J = np.stack([(model5(q + h * e, xx, x0, D) - model5(q - h * e, xx, x0, D)) / (2 * h) for e in np.eye(6)], 1)
    try: C = np.linalg.inv(J.T @ (J / mu[:, None]))
    except np.linalg.LinAlgError: continue
    A1, A2 = q[4], q[5]; R = A2 / A1
    gR = np.zeros(6); gR[4] = -A2 / A1 ** 2; gR[5] = 1 / A1
    seR = np.sqrt(max(gR @ C @ gR, 0))
    dh = np.arccosh(1 + D ** 2 / (2 * q[3] ** 2))
    tot = (A1 + A2) / step; cnt = np.sum(yy - (q[0] + q[1] * (xx - x0)))
    dev = 2 * np.sum(np.where(yy > 0, yy * np.log(yy / mu), 0) - (yy - mu)); dof = len(xx) - 6
    p = [0, 0, q[2], q[3], A1, q[2] + D, q[3], A2]
    rows.append(dict(tt=tt, hkl=hkl, D=D, sp=p[5] - p[2], R=R, seR=seR, d=dh, g1=p[3], g2=p[6],
                     tot=tot, cnt=cnt, chi=dev / dof, counts=A1 / step))
say(f"{len(pos)} allowed reflections, {len(rows)} kept and fitted")
say(" 2theta   hkl        spacing(pred)  ratio   se     d      g1     g2   tot/cnt  dev/dof")
for q in rows:
    say(f"{q['tt']:7.3f} {str(q['hkl']):11s} {q['sp']:.4f}({q['D']:.4f}) {q['R']:.3f} {q['seR']:.3f} {q['d']:6.2f} "
        f"{q['g1']:.4f} {q['g2']:.4f} {q['tot'] / q['cnt']:.3f} {q['chi']:.2f}")
from scipy.stats import spearmanr
R = np.array([q['R'] for q in rows]); dd = np.array([q['d'] for q in rows]); se = np.array([q['seR'] for q in rows])
U1 = abs(np.median(R) - 0.5) < 0.05
rho = spearmanr(dd, np.abs(R - 0.5)).correlation; U3 = rho < -0.3
far = dd >= 2
rms = np.sqrt(np.mean((R[far] - 0.5) ** 2)) if far.sum() else np.nan
U4 = far.sum() > 0 and rms <= 2 * np.median(se[far])
say(f"median ratio {np.median(R):.4f}; Spearman(d, |ratio - 0.5|) {rho:.3f}")
say(f"d >= 2: {far.sum()} reflections, rms(ratio - 0.5) {rms:.4f} against 2 x median se {2 * np.median(se[far]) if far.sum() else float('nan'):.4f}")
for nme, v in [("V1", U1), ("V3", U3), ("V4", U4)]: say(f"{nme}: {'not killed' if v else 'KILLED'}")
open('runs/sep/sep6-out.txt', 'w').write('\n'.join(out) + '\n')
