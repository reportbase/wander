"""FDZ Part B scoring: F6 as written (δ* within a factor 2 of Part A's r(d)), then, post hoc, a CPU replay of the same
scan (uniforms rounded to float32, the scheme in float64, stored as 16-bit unorm or binary32)."""
import json, sys, math, numpy as np
sys.path.insert(0, 'runs/fdz')
from mpmath import mpf
import importlib.util
spec = importlib.util.spec_from_file_location('fdz', 'runs/fdz/fdz.py')
src = open('runs/fdz/fdz.py').read().split('U = [')[0]          # the scheme functions only
ns = {}; exec(src, ns)
J = json.load(open('runs/fdz/gpu-run1.json')); ds = J['ds']; R = J['res']
N, FAR, N32 = 1e-3, 1e3, 1e-6
def r_of(s, d):
    return float(ns['r16'](s, mpf(d))) if s.endswith('16') else float(ns['r32'](s, mpf(d)))
def stored(s, d):
    d = float(np.float32(d))
    if s == 'Z16': A = (FAR + N) / (FAR - N); B = 2 * FAR * N / (FAR - N); w = ((A - B / d) + 1) / 2; return round(w * 65535)
    if s == 'L16': return round(math.log(d / N) / math.log(FAR / N) * 65535)
    if s == 'T16': return round(2 / math.pi * math.atan(d) * 65535)
    if s == 'RZ32': return -float(np.float32(N32 / d))
    if s == 'T32': return float(np.float32(2 / math.pi * math.atan(d)))
def cpu_star(s, d):
    best = None
    for k in range(161):
        dl = 2 ** (-k / 4)
        if stored(s, d * (1 + dl)) > stored(s, d): best = dl
        else: break
    return best
out = []; tot = bad = agree = 0
for s in R:
    row = []
    for d, g in zip(ds, R[s]):
        r = r_of(s, d); c = cpu_star(s, d); tot += 1
        ratio = g / r if g else float('nan')
        if not (0.5 <= ratio <= 2): bad += 1
        if c == g: agree += 1
        row.append(f"d {d:.3g}: δ* {g:.2e}  r {r:.2e}  δ*/r {ratio:.2f}  cpu {c:.2e}")
    out.append(s + '\n    ' + '\n    '.join(row))
out.append(f"F6: δ* outside [r/2, 2r] at {bad} of {tot} points (killed if more than {tot//4}) -> {'KILLED' if bad > tot // 4 else 'not killed'}")
out.append(f"post hoc: GPU δ* equal to the CPU replay of the same scan at {agree} of {tot} points")
print('\n'.join(out)); open('runs/fdz/gpu-run1.txt', 'w').write(J and ('\n'.join(out) + '\n'))
