"""MSR run 2: the tide as a cubic spline of its hourly samples. python3 -I runs/msr/msr2.py <data folder>"""
import sys, csv, math
import numpy as np
from scipy.interpolate import CubicSpline
DATA = sys.argv[1]
src = open('runs/msr/msr.py').read().split("say('data:', DATA)")[0]
g = {'sys': sys}; sys.argv = ['x', DATA]; exec(src, g)
h = []
with open(f'{DATA}/tide2025.csv') as fh:
    rd = csv.reader(fh); next(rd)
    for row in rd: h.append(float(row[1]))
h = np.array(h); t = np.arange(len(h), dtype=float)
cs = CubicSpline(t, h)
f = lambda x: cs(x)
out = []
tc = [24, 96, 384, 1536, 6144]
kt = [g['kstar'](f, c / 4, 4 * c, 0.02, 'ratio') if 4 * c <= t[-1] else 'outside the record' for c in tc]
kr = [g['kstar'](f, c - 48, c + 48, 0.02, 'records') for c in tc]
out.append(f'T1\': K* in the ratio window, c = 24, 96, 384, 1536, 6144 h: {kt}')
ok1 = kt[0] is not None and (kt[1] is None or kt[1] / kt[0] >= 2.5) and kt[2] is None
out.append("T1' " + ('not killed' if ok1 else 'KILLED'))
out.append(f'T2\': K* in the records window (half-width 48 h): {kr}')
ok2 = all(k is not None for k in kr) and max(kr) / min(kr) <= 2
out.append("T2' " + ('not killed' if ok2 else 'KILLED'))
print('\n'.join(out)); open('runs/msr/msr-run2.txt', 'w').write('\n'.join(out) + '\n')
