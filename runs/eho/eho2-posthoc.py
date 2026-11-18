# EHO part 2, post hoc (not a prediction): the same m-ring fit with the blur w held fixed at 10 uas for every day,
# to see whether the 2017-2018 diameter difference is the fit trading diameter against width (emission into d).
# Run as: E=<dir holding 2019-D01-01 and 2024-D01-01> python3 runs/eho/eho2-posthoc.py
import os, glob, numpy as np
src = open("runs/eho/eho2.py").read().split("files = sorted")[0]
ns = {}; exec(src, ns)
from scipy.optimize import least_squares
def fitw(f, W):
    amp, cps = ns['prep'](ns['load'](f))
    best = None
    for d0 in (35, 40, 45, 50):
        for psi0 in np.deg2rad([0, 90, 180, 270]):
            r = least_squares(lambda q: ns['resid']([q[0], q[1], W, q[2], q[3]], amp, cps), [0.6, d0, 0.3, psi0],
                              bounds=([0.1, 20, 0, -10], [2, 70, 0.5, 10]))
            if best is None or r.cost < best.cost: best = r
    return best.x[1], 2*best.cost/len(best.fun)
base = os.environ['E']
for W in (5, 10, 15):
    out = {}
    for f in sorted(glob.glob(base+'/2019-D01-01/csv/SR1_M87_2017_*_StokesI.csv') + glob.glob(base+'/2024-D01-01/csv/L2V1_M87_2018_11[15]_b[34]_hops_netcal_10s_StokesI.csv')):
        p = f.split('/')[-1].split('_'); out[p[2]+'-'+p[3]+' '+p[4]] = fitw(f, W)
    d17 = np.mean([v[0] for k,v in out.items() if k.startswith('2017')]); d18 = np.mean([v[0] for k,v in out.items() if k.startswith('2018')])
    print(f"w fixed {W:2d} uas: 2017 mean d {d17:.2f}, 2018 (111, 115; b3, b4) mean d {d18:.2f}, ratio {d18/d17:.3f};",
          " ".join(f"{k}:{v[0]:.1f}/{v[1]:.1f}" for k,v in out.items() if k.startswith('2018')))
