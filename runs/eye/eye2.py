# EYE run 2: E2's gap clause with the receptor index's wrap handled (run 1 wrapped angles below 0 to 2*pi). python3 runs/eye/eye2.py
import random
from mpmath import mp, mpf, pi, atan2, cos, sin, floor
mp.dps = 50
rnd = random.Random(1119)
T = []
for _ in range(400):
    d = mpf(10) ** mpf(rnd.uniform(-1.3, 4)); a = mpf(rnd.uniform(0.05, 1.5)); T.append((d*cos(a), d*sin(a)))
def rec(theta, K): return int(floor(K * theta / (pi/2)))   # no wrap: the index is the turn counted from the receptor's zero
for K in (64, 1024):
    base = [rec(atan2(y, x), K) for x, y in T]
    for al in (mpf('0.3'), mpf('-0.7'), mpf('1.1')):
        tu = [rec(atan2(y, x) - al, K) for x, y in T]
        gaps = max(abs((tu[i]-tu[j]) - (base[i]-base[j])) for i in range(400) for j in range(i+1, 400))
        print(f"K={K:5d}  turned {mp.nstr(al,2):>4}: largest change in any pair's receptor gap {gaps}")
