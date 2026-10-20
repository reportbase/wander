"""SPN R404: the lens of boost-sky.html breaks the Cauchy's middle and keeps its tails.

The lens theta' = theta + (lam/2) sin 2theta is not a Moebius map, but near both poles it is one: on the level
t = ln tan(theta/2) it slides the far tails by exactly +ln(1 + lam) (theta -> 0) and -ln(1 + lam) (theta -> pi).
Run from the repository root: python3 runs/ims/tails.py
"""
from mpmath import mp, mpf, tan, atan, log, sin, exp

mp.dps = 40

def shift(t, lam):
    th = 2 * atan(exp(mpf(t)))
    thp = th + lam / 2 * sin(2 * th)
    return log(tan(thp / 2)) - t

worst = mpf(0)
for lam in [mpf('-0.8'), mpf('-0.5'), mpf('0.5'), mpf('0.8')]:
    print(f"lam = {mp.nstr(lam, 3)}   ln(1 + lam) = {mp.nstr(log(1 + lam), 15)}")
    for t in [-30, -12, -8, -4, 0, 4, 8, 12, 30]:
        s = shift(t, lam)
        print(f"  t = {t:4d}   t' - t = {mp.nstr(s, 15)}")
    for t in [-30, 30]:
        target = log(1 + lam) if t < 0 else -log(1 + lam)
        worst = max(worst, abs(shift(t, lam) - target))
print(f"worst miss at |t| = 30 from +-ln(1 + lam): {mp.nstr(worst, 3)}")
