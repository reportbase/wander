# KPL run 2, post hoc code check: the paper's S2 orbit (table3) made into places at run 2's dates, noise-free and with
# the stated errors, run through kpl2.py's steps. Usage: python3 -I runs/kpl/kpl2-check.py <table5.tsv>
import sys, os, numpy as np, io, contextlib
src = open(os.path.join(os.path.dirname(__file__), 'kpl2.py')).read()
pre, steps = src.split("# ---- step 1", 1)
exec(pre)   # reads table5: t, x, y, sx, sy
a, e0, i, W, w, Tp, P = 125.5, 0.8839, np.radians(134.18), np.radians(226.94), np.radians(65.51), 2002.33, 16.00
cw, sw, cW, sW, ci = np.cos(w), np.sin(w), np.cos(W), np.sin(W), np.cos(i)
A, B, F, G = a*np.array([cw*cW - sw*sW*ci, cw*sW + sw*cW*ci, -sw*cW - cw*sW*ci, -sw*sW + cw*cW*ci])
def places(tt):
    M = 2*np.pi*(tt - Tp)/P; E = M.copy()
    for _ in range(60): E = E - (E - e0*np.sin(E) - M)/(1 - e0*np.cos(E))
    X, Y = np.cos(E) - e0, np.sqrt(1 - e0*e0)*np.sin(E)
    return A*X + F*Y, B*X + G*Y
xt, yt = places(t); rng = np.random.default_rng(1210)
for label, nx, ny in (('noise-free', 0, 0), ('with the stated errors', sx, sy)):
    x = xt + rng.normal(0, 1, len(t))*nx; y = yt + rng.normal(0, 1, len(t))*ny
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec("# ---- step 1" + steps)
    lines = [l for l in buf.getvalue().splitlines() if l.startswith(('STEP 1 (', '    (', 'STEP 2-3', '          period', 'STEP 4', 'V1', 'V4', 'V5'))]
    print(label); [print('   ', l) for l in lines]
