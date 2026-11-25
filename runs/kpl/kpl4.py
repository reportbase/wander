# KPL run 4: run 3's untimed fit with the frame freed. mode 'offset': the focus at (x0, y0), a constant, still untimed.
# mode 'drift': the focus at (x0 + vx (t - 2009), y0 + vy (t - 2009)); the drift alone uses the dates.
# Then the clock, period and size as before, from places taken relative to the fitted focus.
# Usage: python3 -I runs/kpl/kpl4.py <table5.tsv> <offset|drift>                  the data
#        python3 -I runs/kpl/kpl4.py <table5.tsv> <offset|drift> --check <n>      the paper's orbit, n draws
import sys, os, io, contextlib, numpy as np
from scipy.optimize import least_squares
src = open(os.path.join(os.path.dirname(__file__), 'kpl2.py')).read()
pre, rest = src.split("# ---- step 1", 1)
step1, rest2 = rest.split("def ti(el):", 1)
mode = sys.argv[2]
exec(pre)
exec("def ti(el):" + rest2.split("untimed = []")[0], globals())
T0 = (t.copy(), x.copy(), y.copy(), sx.copy(), sy.copy())
nf = 2 if mode == 'offset' else (0 if mode == 'timed0' else 4)

def proj(q, E):
    A, B, F, G, e = q[:5]; X = np.cos(E) - e; Y = np.sqrt(1 - e*e)*np.sin(E)
    return A*X + F*Y, B*X + G*Y
def frame(f, tt):
    if len(f) == 0: return 0*tt, 0*tt
    if len(f) == 2: return f[0] + 0*tt, f[1] + 0*tt
    return f[0] + f[2]*(tt - 2009), f[1] + f[3]*(tt - 2009)

def fit(x, y, sx, sy):
    global AB, FG, e, ctr
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec("# ---- step 1" + step1, globals())   # run 2's conic as the start
    q0 = np.r_[AB, FG, e]
    T = np.array([[q0[0], q0[2]], [q0[1], q0[3]]]); XY = np.linalg.solve(T, np.vstack([x, y]))
    E0 = np.arctan2(XY[1]/np.sqrt(1 - q0[4]**2), XY[0] + q0[4])
    n = len(x)
    def res(p):
        px, py = proj(p[:5], p[5 + nf:]); fx, fy = frame(p[5:5 + nf], t)
        return np.r_[(x - fx - px)/sx, (y - fy - py)/sy]
    lo = np.r_[[-np.inf]*4, 0.0, [-np.inf]*(nf + n)]; hi = np.r_[[np.inf]*4, 0.999999, [np.inf]*(nf + n)]
    r = least_squares(res, np.r_[q0, np.zeros(nf), E0], bounds=(lo, hi), x_scale='jac', max_nfev=20000)
    AB, FG, e = r.x[0:2], r.x[2:4], r.x[4]; ctr = -e*AB
    return r

def kepler_xy(q, tt):
    A, B, F, G, e, P, Tp = q
    M = 2*np.pi*(tt - Tp)/P; E = M.copy()
    for _ in range(50): E = E - (E - e*np.sin(E) - M)/(1 - e*np.cos(E))
    return proj((A, B, F, G, e), E)
def fit_timed(x, y, sx, sy):
    global AB, FG, e, ctr, Pt, Tpt
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec("# ---- step 1" + step1, globals())
    best = None
    for P0 in (14.0, 16.0, 18.0):
        for Tp0 in (2001.5, 2002.3, 2003.0):
            for sg in (1, -1):
                q0 = np.r_[AB[0], AB[1], sg*FG[0], sg*FG[1], min(e, 0.95), P0, Tp0, np.zeros(nf)]
                def res(p):
                    px, py = kepler_xy(p[:7], t); fx, fy = frame(p[7:], t)
                    return np.r_[(x - fx - px)/sx, (y - fy - py)/sy]
                lo = np.r_[[-np.inf]*4, 0.0, 5.0, 1990.0, [-np.inf]*nf]; hi = np.r_[[np.inf]*4, 0.999, 40.0, 2020.0, [np.inf]*nf]
                r = least_squares(res, q0, bounds=(lo, hi), x_scale='jac', max_nfev=5000)
                if best is None or r.cost < best.cost: best = r
    q = best.x; AB, FG, e = q[0:2], q[2:4], q[4]; ctr = -e*AB; Pt, Tpt = q[5], q[6]
    best.fr = q[7:]
    return best

def run(x_, y_, sx_, sy_, quiet=False):
    if mode.startswith('timed'):
        r = fit_timed(x_, y_, sx_, sy_); f = r.fr
        a = np.hypot(*AB)   # a placeholder; the semi-major axis from the elements below
        chi2 = 2*r.cost/(2*len(x_) - 7 - nf)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            el = elements(AB[0], AB[1], FG[0], FG[1])
            print('TIMED (%s): e = %.4f, period %.3f yr, a = %.2f mas, chi2/dof %.2f, frame %s' % (mode, e, Pt, el[0][0] if el else np.nan, chi2, np.array2string(f, precision=3)))
            print('   elements (a, i, Omega, omega):', el)
        out = buf.getvalue()
        if not quiet: print(out, end='')
        return out, f
    return run_untimed(x_, y_, sx_, sy_, quiet)

def run_untimed(x_, y_, sx_, sy_, quiet=False):
    global x, y, sx, sy
    r = fit(x_, y_, sx_, sy_)
    f = r.x[5:5 + nf]; fx, fy = frame(f, t)
    x, y, sx, sy = x_ - fx, y_ - fy, sx_, sy_            # places relative to the fitted focus
    chi2 = 2*r.cost/(len(x) - 5 - nf)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        print('STEP 1 (%s): e = %.4f, chi2/dof %.2f, frame %s' % (mode, e, chi2, np.array2string(f, precision=3)))
        exec("def ti(el):" + rest2.split("print('\\nPREDICTIONS')")[0], globals())
    out = buf.getvalue()
    if not quiet: print(out, end='')
    return out, f

a_, e_, i_, W_, w_, Tp_, P_ = 125.5, 0.8839, np.radians(134.18), np.radians(226.94), np.radians(65.51), 2002.33, 16.00
if '--check' in sys.argv:
    nd = int(sys.argv[sys.argv.index('--check') + 1])
    cw, sw, cW, sW, ci = np.cos(w_), np.sin(w_), np.cos(W_), np.sin(W_), np.cos(i_)
    Ab, Bb, Fb, Gb = a_*np.array([cw*cW - sw*sW*ci, cw*sW + sw*cW*ci, -sw*cW - cw*sW*ci, -sw*sW + cw*cW*ci])
    tt, _, _, sxx, syy = T0
    M = 2*np.pi*(tt - Tp_)/P_; E = M.copy()
    for _ in range(60): E = E - (E - e_*np.sin(E) - M)/(1 - e_*np.cos(E))
    X, Y = np.cos(E) - e_, np.sqrt(1 - e_*e_)*np.sin(E)
    xt, yt = Ab*X + Fb*Y, Bb*X + Gb*Y
    rng = np.random.default_rng(1216); rows = []
    for kd in range(nd):
        t = tt
        o, f = run(xt + rng.normal(0, 1, len(tt))*sxx, yt + rng.normal(0, 1, len(tt))*syy, sxx, syy, quiet=True)
        g = lambda pat: float(o.split(pat)[1].split()[0].rstrip(','))
        rows.append((g('e = '), g('period '), g('a = ')) + tuple(f))
        print('draw %d: e %.4f  P %.3f yr  a %.2f mas  frame %s' % (kd, *rows[-1][:3], np.array2string(f, precision=3)), flush=True)
    rows = np.array(rows)
    print('over %d draws (%s): e %.4f +- %.4f, P %.3f +- %.3f yr, a %.2f +- %.2f mas; frame sd %s' % (nd, mode,
          rows[:, 0].mean(), rows[:, 0].std(), rows[:, 1].mean(), rows[:, 1].std(), rows[:, 2].mean(), rows[:, 2].std(),
          np.array2string(rows[:, 3:].std(0), precision=3)))
else:
    run(x, y, sx, sy)
