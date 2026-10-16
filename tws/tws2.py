"""TWS run 2, T3′ (plans/tws-plan.md): the inward and outward rates from a pivot inside, with a branch-safe angle.
Run: python3 tws/tws2.py
"""
from mpmath import mp, mpf, sqrt, cos, sin, atan2, pi, diff, fabs
mp.dps = 40
TOL = mpf(10)**-30
def hit_safe(p, psi):
    c, s = cos(psi), sin(psi)
    lam = -p * c + sqrt(1 - p * p * s * s)
    x, y = p + lam * c, lam * s
    return atan2(-y, -x) + pi            # Q's angle about O, measured so that the cut sits at angle 0, away from ψ = π
ok = True
for p in (mpf('0.1'), mpf('0.5'), mpf('0.9')):
    inward = diff(lambda t: hit_safe(p, t), pi)
    outward = diff(lambda t: hit_safe(p, t) if True else 0, mpf(0)) if False else None
    from mpmath import atan2 as at
    out = diff(lambda t: at(sin(t) * (-p * cos(t) + sqrt(1 - p * p * sin(t)**2)), p + cos(t) * (-p * cos(t) + sqrt(1 - p * p * sin(t)**2))), mpf(0))
    good = fabs(inward - (1 + p)) <= TOL and fabs(out - (1 - p)) <= TOL
    ok &= good
    print(f"p={p}: inward {mp.nstr(inward, 25)} (1 + p), outward {mp.nstr(out, 25)} (1 − p) {'ok' if good else 'OFF'}")
print("T3′", 'not killed' if ok else 'KILLED')
