"""ALG run 2 (plans/alg-plan.md): C3', CORDIC rotation mode steered by the slope left kept as a pair."""
import random
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 60
rng = random.Random(99)
table = [mp.atan(mp.mpf(2) ** (-i)) for i in range(32)]
same = 0
for _ in range(1000):
    th = mp.mpf(rng.uniform(-1.74, 1.74))
    z = th; sa = []
    for i in range(32):
        g = 1 if z >= 0 else -1; sa.append(g); z -= g * table[i]
    a, b = Fr(mp.nstr(mp.cos(th), 50)), Fr(mp.nstr(mp.sin(th), 50))
    x, y = Fr(1), Fr(0); sp_ = []
    for i in range(32):
        g = 1 if x * b - y * a >= 0 else -1; sp_.append(g)
        t = Fr(g, 2 ** i); x, y = x - y * t, y + x * t
    same += (sp_ == sa)
print(f"C3' sequences equal in {same} of 1000:", "not killed" if same == 1000 else "KILLED")
