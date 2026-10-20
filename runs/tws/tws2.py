"""TWS run 2, T3′ (plans/tws-plan.md): the inward and outward rates from a pivot inside, each with an angle whose cut
lies away from the direction where it is differentiated.
Run: python3 runs/tws/tws2.py
"""
from mpmath import mp, mpf, sqrt, cos, sin, atan2, pi, diff, fabs
mp.dps = 40
TOL = mpf(10)**-30

def hit_xy(p, psi):
    c, s = cos(psi), sin(psi)
    lam = -p * c + sqrt(1 - p * p * s * s)
    return p + lam * c, lam * s

def angle_cut_at_pi(p, psi):          # cut at ±π: safe near ψ = 0, where the hit is near angle 0
    x, y = hit_xy(p, psi); return atan2(y, x)

def angle_cut_at_0(p, psi):           # cut at 0: safe near ψ = π, where the hit is near angle π
    x, y = hit_xy(p, psi); return atan2(-y, -x) + pi

ok = True
for p in (mpf('0.1'), mpf('0.5'), mpf('0.9')):
    inward = diff(lambda t: angle_cut_at_0(p, t), pi)
    outward = diff(lambda t: angle_cut_at_pi(p, t), mpf(0))
    good = fabs(inward - (1 + p)) <= TOL and fabs(outward - (1 - p)) <= TOL
    ok &= good
    print(f"p={p}: inward {mp.nstr(inward, 25)} (1 + p), outward {mp.nstr(outward, 25)} (1 − p) {'ok' if good else 'OFF'}")
print("T3′", 'not killed' if ok else 'KILLED')
