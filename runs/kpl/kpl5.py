# KPL run 5: S2's places and radial velocities fitted together (Gillessen et al. 2017, VizieR J/ApJ/837/30 table5).
# The places are looks (mas against the observer's years); the velocities are amounts (km/s), which bring in the distance
# R0 and with it the size in au and the mass. Newtonian, the focus fixed at zero (run 4b), no Roemer delay, no redshift.
# Usage: python3 -I runs/kpl/kpl5.py <table5.tsv>                 the data
#        python3 -I runs/kpl/kpl5.py <table5.tsv> --check <n>     the paper's orbit at the same dates, n draws (seed 1217)
#        python3 -I runs/kpl/kpl5.py <table5.tsv> --scale <k>     the data with every place times k (an identity check)
#        python3 -I runs/kpl/kpl5.py <table5.tsv> --places        the places alone (run 4b's frame-at-zero fit, as a check)
import sys, numpy as np
from scipy.optimize import least_squares

AUYR = 4.740470463533348          # km/s in one au a year
def read(fn):
    rows = [l.rstrip('\n').split('\t') for l in open(fn) if l.strip() and not l.startswith('#')]
    head = rows[0]; body = [r for r in rows[3:] if len(r) == len(head)]
    ix = {h.strip(): k for k, h in enumerate(head)}
    P, V = [], []
    for r in body:
        g = lambda c: r[ix[c]].strip()
        if g('Flag') == 'a' and '' not in (g('oRA-S2'), g('oDE-S2')):
            P.append((float(g('Date')), float(g('oDE-S2')), float(g('oRA-S2')), float(g('e_oDE-S2')), float(g('e_oRA-S2'))))
        if g('RV-S2') != '':
            V.append((float(g('Date')), float(g('RV-S2')), float(g('e_RV-S2'))))
    return np.array(sorted(P)), np.array(sorted(V))

def anomaly(e, P, Tp, tt):
    M = 2*np.pi*(tt - Tp)/P; E = M.copy()
    for _ in range(60): E = E - (E - e*np.sin(E) - M)/(1 - e*np.cos(E))
    return E
def model(q, tp, tv):
    a, i, W, w, e, P, Tp, R0, V0 = q          # a mas, angles rad, P yr, R0 pc, V0 km/s
    cw, sw, cW, sW, ci, si = np.cos(w), np.sin(w), np.cos(W), np.sin(W), np.cos(i), np.sin(i)
    A, B = a*(cw*cW - sw*sW*ci), a*(cw*sW + sw*cW*ci)
    F, G = a*(-sw*cW - cw*sW*ci), a*(-sw*sW + cw*cW*ci)
    C, H = a*sw*si, a*cw*si                   # z = C X + H Y, z away from the observer
    E = anomaly(e, P, Tp, tp); X, Y = np.cos(E) - e, np.sqrt(1 - e*e)*np.sin(E)
    xn, ye = A*X + F*Y, B*X + G*Y             # north, east
    E = anomaly(e, P, Tp, tv); Ed = (2*np.pi/P)/(1 - e*np.cos(E))
    zd = C*(-np.sin(E)*Ed) + H*(np.sqrt(1 - e*e)*np.cos(E)*Ed)      # mas a year
    return xn, ye, zd*R0*1e-3*AUYR + V0

def fit(Pd, Vd, use_v=True):
    tp, xn, ye, sxn, sye = Pd.T; tv, vr, sv = Vd.T
    def res(q):
        mx, my, mv = model(q, tp, tv)
        r = np.r_[(xn - mx)/sxn, (ye - my)/sye]
        return np.r_[r, (vr - mv)/sv] if use_v else r
    best = None
    for W0 in (np.radians(45.0), np.radians(225.0)):           # run 4b's pair of nodes, each with its omega
        w0 = W0 - np.radians(161.4)
        for P0 in (15.8, 16.1, 16.4):
            for Tp0 in (2002.2, 2002.4):
                q0 = [123.0, np.radians(135.0), W0, w0, 0.88, P0, Tp0, 8300.0, 0.0]
                lo = [50, 0, -10, -10, 0.0, 5, 1990, 1000, -500]; hi = [300, np.pi, 20, 20, 0.999, 40, 2020, 30000, 500]
                if not use_v: lo[7], hi[7], lo[8], hi[8] = 8299.0, 8301.0, -1, 1
                r = least_squares(res, q0, bounds=(lo, hi), x_scale='jac', max_nfev=5000)
                r.W0 = W0
                if best is None or r.cost < best.cost: best = r
    return best

def report(r, Pd, Vd, use_v=True, quiet=False):
    a, i, W, w, e, P, Tp, R0, V0 = r.x
    n = 2*len(Pd) + (len(Vd) if use_v else 0); k = 9 if use_v else 7
    aau = a*R0*1e-3; Msun = aau**3/P**2
    W, w = np.degrees(W) % 360, np.degrees(w) % 360
    out = ('a %.2f mas, e %.4f, i %.2f deg, Omega %.2f deg, omega %.2f deg, P %.3f yr, Tp %.3f'
           % (a, e, np.degrees(i), W, w, P, Tp))
    if use_v: out += ', R0 %.0f pc, V0 %.1f km/s, a %.1f au, M %.3e suns' % (R0, V0, aau, Msun)
    out += ', chi2/dof %.2f' % (2*r.cost/(n - k))
    if not quiet: print(out, flush=True)
    return dict(a=a, e=e, i=np.degrees(i), W=W, w=w, P=P, Tp=Tp, R0=R0, V0=V0, M=Msun, chi2=2*r.cost)

Pd, Vd = read(sys.argv[1])
print('S2: %d places %.3f to %.3f, %d radial velocities %.3f to %.3f' % (len(Pd), Pd[0, 0], Pd[-1, 0], len(Vd), Vd[0, 0], Vd[-1, 0]))
paper = [125.5, np.radians(134.18), np.radians(226.94), np.radians(65.51), 0.8839, 16.00, 2002.33, 8320.0, 0.0]

if '--check' in sys.argv:
    nd = int(sys.argv[sys.argv.index('--check') + 1]); rng = np.random.default_rng(1217)
    mx, my, mv = model(paper, Pd[:, 0], Vd[:, 0]); rows = []
    for kd in range(nd):
        P2 = Pd.copy(); V2 = Vd.copy()
        P2[:, 1] = mx + rng.normal(0, 1, len(mx))*Pd[:, 3]; P2[:, 2] = my + rng.normal(0, 1, len(my))*Pd[:, 4]
        V2[:, 1] = mv + rng.normal(0, 1, len(mv))*Vd[:, 2]
        d = report(fit(P2, V2), P2, V2, quiet=True); rows.append([d[c] for c in ('e', 'P', 'a', 'R0', 'M', 'W', 'w')])
        print('draw %d: e %.4f  P %.3f  a %.2f  R0 %.0f  M %.3e  Omega %.2f  omega %.2f' % (kd, *rows[-1]), flush=True)
    rows = np.array(rows)
    for c, m, s in zip(('e', 'P', 'a', 'R0', 'M', 'Omega', 'omega'), rows.mean(0), rows.std(0)):
        print('over %d draws: %s %.5g +- %.3g' % (nd, c, m, s))
elif '--scale' in sys.argv:
    kf = float(sys.argv[sys.argv.index('--scale') + 1]); P2 = Pd.copy(); P2[:, 1:] *= kf
    report(fit(Pd, Vd), Pd, Vd); report(fit(P2, Vd), P2, Vd)
elif '--places' in sys.argv:
    report(fit(Pd, Vd, use_v=False), Pd, Vd, use_v=False)
else:
    r = fit(Pd, Vd); report(r, Pd, Vd)
    # the other node of the pair, held: how much worse the velocities make it
    W, w = r.x[2] + np.pi, r.x[3] + np.pi
    tp, xn, ye, sxn, sye = Pd.T; tv, vr, sv = Vd.T
    def res(q):
        mx, my, mv = model(np.r_[q[:2], W, w, q[2:]], tp, tv)
        return np.r_[(xn - mx)/sxn, (ye - my)/sye, (vr - mv)/sv]
    q0 = np.r_[r.x[:2], r.x[4:]]
    lo = [50, 0, 0.0, 5, 1990, 1000, -500]; hi = [300, np.pi, 0.999, 40, 2020, 30000, 500]
    r2 = least_squares(res, q0, bounds=(lo, hi), x_scale='jac', max_nfev=5000)
    print('the other node held (Omega %.2f, omega %.2f): chi2 %.1f against %.1f' % (np.degrees(W) % 360, np.degrees(w) % 360, 2*r2.cost, 2*r.cost))
    mx, my, mv = model(r.x, tp, tv)
    print('velocity residuals over errors: rms %.2f, worst %.2f at %.3f' % (np.sqrt(np.mean(((vr - mv)/sv)**2)),
          np.max(np.abs((vr - mv)/sv)), tv[np.argmax(np.abs((vr - mv)/sv))]))
