# FRD run 1: rotation measure from the polarization angle alone against the full Q, U response (plans/frd-plan.md).
# Usage: python3 runs/frd/frd.py <table6.tsv from VizieR J/ApJ/825/59>
import sys, numpy as np
from scipy.optimize import least_squares
C = 299792458.0

rows = [l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]
rows = [r for r in rows[3:] if len(r) >= 8]   # past the header, units and dashes lines
data = {}
for r in rows:
    try: v = [float(x) for x in r[1:8]]
    except ValueError: continue
    data.setdefault(r[0].strip(), []).append(v)

def angle_fit(l2, Q, U, sP, P):
    chi = 0.5*np.arctan2(U, Q)
    o = np.argsort(l2); l2, chi, s = l2[o], chi[o], (sP/(2*P))[o]
    ch = np.unwrap(2*chi)/2   # period pi
    W = 1/s**2; A = np.vstack([np.ones_like(l2), l2]).T
    cov = np.linalg.inv(A.T @ (A*W[:, None])); p = cov @ (A.T @ (W*ch))
    res = (ch - A @ p)/s
    return p[1], np.sqrt(cov[1, 1]), np.sum(res**2)/(len(l2) - 2)

def full_fit(l2, Q, U, eQ, eU, rm_starts):
    def model(q):
        c0, c1, c2, x0, rm = q
        p = c0 + c1*l2 + c2*l2**2
        return p*np.exp(2j*(x0 + rm*l2))
    def r(q):
        m = model(q); return np.r_[(m.real - Q)/eQ, (m.imag - U)/eU]
    best = None
    P0 = np.median(np.hypot(Q, U))
    for rm0 in rm_starts:
        for x0 in np.linspace(0, np.pi, 4, endpoint=False):
            f = least_squares(r, [P0, 0, 0, x0, rm0], x_scale='jac', max_nfev=5000)
            if best is None or f.cost < best.cost: best = f
    J = best.jac; dof = 2*len(l2) - 5
    cov = np.linalg.pinv(J.T @ J)
    return best.x[4], np.sqrt(cov[4, 4]), 2*best.cost/dof

def rmsynth_peak(l2, Q, U, w):
    grid = np.arange(-2000, 2000.5, 0.5)
    F = np.abs(np.exp(-2j*np.outer(grid, l2 - np.average(l2, weights=w))) @ (w*(Q + 1j*U)))
    return grid[np.argmax(F)]

out = []
for sid, v in sorted(data.items()):
    v = np.array(v); nu = v[:, 0]*1e9; I, eI, Q, eQ, U, eU = v[:, 1:].T
    eQ = np.where(eQ > 0, eQ, np.median(eQ[eQ > 0])); eU = np.where(eU > 0, eU, np.median(eU[eU > 0]))
    P = np.hypot(Q, U); sP = 0.5*(eQ + eU); keep = P >= 3*sP
    if keep.sum() < 20:
        out.append((sid, 'few', keep.sum())); continue
    l2 = (C/nu[keep])**2; q, u, eq, eu, p, sp = Q[keep], U[keep], eQ[keep], eU[keep], P[keep], sP[keep]
    ra, sa, xa = angle_fit(l2, q, u, sp, p)
    pk = rmsynth_peak(l2, q, u, 1/sp**2)
    rc, sc, xc = full_fit(l2, q, u, eq, eu, [ra, pk])
    # F5: fractional Q/I, U/I with the angle weights held fixed
    Ik = I[keep]
    ra5, _, _ = angle_fit(l2, q/Ik, u/Ik, sp, p)   # same sigma_chi: weights from the original sP/P
    rc5, _, _ = full_fit(l2, q/Ik, u/Ik, eq/Ik, eu/Ik, [rc])
    out.append((sid, 'ok', dict(n=int(keep.sum()), ra=ra, sa=sa, xa=xa, rc=rc, sc=sc, xc=xc, pk=pk,
                                d5a=abs(ra5 - ra), d5c=abs(rc5 - rc))))
    o = out[-1][2]
    print('%-10s n %3d  RM_angle %9.2f +- %6.2f (chi2 %6.2f)  RM_full %9.2f +- %6.2f (chi2 %6.2f)  synth %8.1f  |d|/s %6.2f' % (
        sid, o['n'], ra, sa, xa, rc, sc, xc, pk, abs(ra - rc)/np.hypot(sa, sc)), flush=True)

ok = [o[2] for o in out if o[1] == 'ok']
print('\nsources %d, analysed %d, too few channels %d' % (len(out), len(ok), sum(1 for o in out if o[1] == 'few')))
ad = [o for o in ok if o['xc'] < 2]
z = lambda o: abs(o['ra'] - o['rc'])/np.hypot(o['sa'], o['sc'])
print('adequate (full fit chi2/dof < 2): %d' % len(ad))
if ad:
    f1 = sum(z(o) <= 3 for o in ad)
    print('F1: within 3 sigma %d of %d (%.0f%%) ->' % (f1, len(ad), 100*f1/len(ad)), 'not killed' if f1 >= 0.9*len(ad) else 'KILLED')
    m = np.median([z(o) for o in ad])
    print('F2: median |d|/sigma %.2f ->' % m, 'not killed' if m < 1 else 'KILLED')
    f4 = sum(o['xa'] < 2 for o in ad)
    print('F4: angle line chi2/dof < 2 on %d of %d ->' % (f4, len(ad)), 'not killed' if f4 >= 0.8*len(ad) else 'KILLED')
    f5a = max(o['d5a'] for o in ad); f5c = sum(o['d5c'] > 1e-6 for o in ad)
    print('F5: RM_angle change under Q/I, U/I max %.2e; RM_full moved on %d of %d ->' % (f5a, f5c, len(ad)),
          'not killed' if f5a < 1e-9 and f5c >= 0.5*len(ad) else 'KILLED')
part = [o for o in ok if z(o) > 3]
if part:
    f3 = sum(o['xc'] >= 2 for o in part)
    print('F3: of %d parting beyond 3 sigma, %d inadequate ->' % (len(part), f3), 'not killed' if f3 >= 0.8*len(part) else 'KILLED')
else:
    print('F3: no source parts beyond 3 sigma (untested)')
