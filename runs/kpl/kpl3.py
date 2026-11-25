# KPL run 3: the untimed shape by the distance of each look from the projected orbit itself. Unknowns: the Thiele-Innes
# constants A, B, F, G, the eccentricity e, and one eccentric anomaly per look (a free number: no date enters). Residuals
# each look's offset from its point on the projected orbit over the stated errors. Started from run 2's conic.
# Then run 2's steps 2-4 unchanged on the fitted orbit.
# Usage: python3 -I runs/kpl/kpl3.py <table5.tsv> [table3.tsv]            the data
#        python3 -I runs/kpl/kpl3.py <table5.tsv> --check <n>               the paper's orbit at the same dates, n draws
import sys, os, io, contextlib, numpy as np
from scipy.optimize import least_squares
src = open(os.path.join(os.path.dirname(__file__), 'kpl2.py')).read()
pre, rest = src.split("# ---- step 1", 1)
step1, rest2 = rest.split("def ti(el):", 1)
exec(pre)     # reads the looks: t, x, y, sx, sy
T0 = (t.copy(), x.copy(), y.copy(), sx.copy(), sy.copy())

def proj(q, E):
    A, B, F, G, e = q[:5]; X = np.cos(E) - e; Y = np.sqrt(1 - e*e)*np.sin(E)
    return A*X + F*Y, B*X + G*Y

def geometric(x, y, sx, sy):
    global AB, FG, e, ctr
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec("# ---- step 1" + step1, globals())   # run 2's conic: AB, FG, e
    q0 = np.r_[AB, FG, e]
    T = np.array([[q0[0], q0[2]], [q0[1], q0[3]]]); XY = np.linalg.solve(T, np.vstack([x, y]))
    E0 = np.arctan2(XY[1]/np.sqrt(1 - q0[4]**2), XY[0] + q0[4])
    def res(p):
        px, py = proj(p[:5], p[5:]); return np.r_[(x - px)/sx, (y - py)/sy]
    lo = np.r_[[-np.inf]*4, 0.0, [-np.inf]*len(x)]; hi = np.r_[[np.inf]*4, 0.999999, [np.inf]*len(x)]
    r = least_squares(res, np.r_[q0, E0], bounds=(lo, hi), x_scale='jac', max_nfev=20000)
    AB, FG, e = r.x[0:2], r.x[2:4], r.x[4]
    ctr = -e*AB
    return r

def run(x_, y_, sx_, sy_, quiet=False):
    global x, y, sx, sy
    x, y, sx, sy = x_, y_, sx_, sy_
    r = geometric(x, y, sx, sy)
    chi2 = 2*r.cost/(2*len(x) - 5 - len(x))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print('STEP 1 (untimed, distance to the projected orbit): e = %.4f, chi2/dof %.2f' % (e, chi2))
        exec("def ti(el):" + rest2.split("print('\\nPREDICTIONS')")[0], globals())
    out = buf.getvalue()
    if not quiet: print(out, end='')
    return out

if '--check' in sys.argv:
    n = int(sys.argv[sys.argv.index('--check') + 1])
    a, e0, i, W, w, Tp, P = 125.5, 0.8839, np.radians(134.18), np.radians(226.94), np.radians(65.51), 2002.33, 16.00
    cw, sw, cW, sW, ci = np.cos(w), np.sin(w), np.cos(W), np.sin(W), np.cos(i)
    Ab, Bb, Fb, Gb = a*np.array([cw*cW - sw*sW*ci, cw*sW + sw*cW*ci, -sw*cW - cw*sW*ci, -sw*sW + cw*cW*ci])
    tt, _, _, sxx, syy = T0
    M = 2*np.pi*(tt - Tp)/P; E = M.copy()
    for _ in range(60): E = E - (E - e0*np.sin(E) - M)/(1 - e0*np.cos(E))
    X, Y = np.cos(E) - e0, np.sqrt(1 - e0*e0)*np.sin(E)
    xt, yt = Ab*X + Fb*Y, Bb*X + Gb*Y
    rng = np.random.default_rng(1214); rows = []
    for kd in range(n):
        o = run(xt + rng.normal(0, 1, len(tt))*sxx, yt + rng.normal(0, 1, len(tt))*syy, sxx, syy, quiet=True)
        g = lambda pat: float(o.split(pat)[1].split()[0].rstrip(','))
        rows.append((g('e = '), g('period '), g('a = ')))
        print('draw %d: e %.4f  P %.3f yr  a %.2f mas' % (kd, *rows[-1]), flush=True)
    rows = np.array(rows)
    print('over %d draws: e %.4f +- %.4f, P %.3f +- %.3f yr, a %.2f +- %.2f mas (truth 0.8839, 16.000, 125.50)' %
          (n, rows[:, 0].mean(), rows[:, 0].std(), rows[:, 1].mean(), rows[:, 1].std(), rows[:, 2].mean(), rows[:, 2].std()))
else:
    run(x, y, sx, sy)
    if len(sys.argv) > 2:
        exec("print('\\nPREDICTIONS')" + rest2.split("print('\\nPREDICTIONS')")[1].replace('V1', 'W1').replace('V2', 'W2')
             .replace('V3', 'W3').replace('V4', 'W4').replace('V5', 'W5'))
