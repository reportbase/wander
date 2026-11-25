# KPL run 6: run 5's joint fit (places and radial velocities) with the Roemer delay: each look's date is the light's
# arrival, emitted earlier by z/c, z the star's distance behind the focus along the line of sight (z = C X + H Y in mas,
# times R0 into au). Solved by fixed-point iteration t_emit = t_obs - z(t_emit)/c.
# Usage: python3 -I runs/kpl/kpl6.py <table5.tsv>                     the data, with the delay
#        python3 -I runs/kpl/kpl6.py <table5.tsv> --check <n> <gen> <fit>   paper's orbit, delay in generation/fit 0|1 (seed 1218)
import sys, os, numpy as np
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kpl5.py')).read()
exec(src.split("Pd, Vd = read(sys.argv[1])")[0])
LTY = 499.004783836 / (365.25 * 86400)          # years of light travel per au
model5 = model
ROMER = [True]
def model(q, tp, tv):
    if not ROMER[0]: return model5(q, tp, tv)
    a, i, W, w, e, P, Tp, R0, V0 = q
    C, H = a*np.sin(w)*np.sin(i), a*np.cos(w)*np.sin(i)
    def emit(t):
        te = t.copy()
        for _ in range(4):
            E = anomaly(e, P, Tp, te)
            z = C*(np.cos(E) - e) + H*np.sqrt(1 - e*e)*np.sin(E)
            te = t - z*R0*1e-3*LTY
        return te
    return model5(q, emit(tp), emit(tv))
Pd, Vd = read(sys.argv[1])
paper = [125.5, np.radians(134.18), np.radians(226.94), np.radians(65.51), 0.8839, 16.00, 2002.33, 8320.0, 0.0]
if '--check' in sys.argv:
    k = sys.argv.index('--check'); nd, gen, fitr = int(sys.argv[k+1]), sys.argv[k+2] == '1', sys.argv[k+3] == '1'
    rng = np.random.default_rng(1218); ROMER[0] = gen
    mx, my, mv = model(paper, Pd[:, 0], Vd[:, 0]); rows = []
    for kd in range(nd):
        P2, V2 = Pd.copy(), Vd.copy()
        P2[:, 1] = mx + rng.normal(0, 1, len(mx))*Pd[:, 3]; P2[:, 2] = my + rng.normal(0, 1, len(my))*Pd[:, 4]
        V2[:, 1] = mv + rng.normal(0, 1, len(mv))*Vd[:, 2]
        ROMER[0] = fitr; d = report(fit(P2, V2), P2, V2, quiet=True); ROMER[0] = gen
        rows.append([d[c] for c in ('e', 'P', 'a', 'R0', 'M')])
        print('draw %d: e %.4f  P %.3f  a %.2f  R0 %.0f  M %.3e' % (kd, *rows[-1]), flush=True)
    rows = np.array(rows)
    print('generated with delay %d, fitted with delay %d, over %d draws:' % (gen, fitr, nd))
    for c, m, s in zip(('e', 'P', 'a', 'R0', 'M'), rows.mean(0), rows.std(0)): print('  %s %.5g +- %.3g' % (c, m, s))
else:
    report(fit(Pd, Vd), Pd, Vd)
