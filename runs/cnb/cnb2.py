# CNB run 2: C7' by the root of the range's central difference
import sys; sys.path.insert(0, 'runs/cnb')
import numpy as np
from scipy.optimize import brentq
import importlib.util
spec = importlib.util.spec_from_file_location('c', 'runs/cnb/cnb.py')
src = open('runs/cnb/cnb.py').read().split('out = []')[0]; ns = {}; exec(src, ns); fly = ns['fly']
out = []
for b in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2):
    L = 1/b; h = 1e-4
    d = lambda s: fly(s+h, L=L)['R'] - fly(s-h, L=L)['R']
    s = brentq(d, 0.9, 1.0, xtol=1e-14)
    line = f'C7prime beta {b:g}: s* = {s:.10f}, (1 - s*)/beta = {(1-s)/b:.6f}'; print(line); out.append(line)
open('runs/cnb/cnb-run2.txt', 'w').write('\n'.join(out)+'\n')
