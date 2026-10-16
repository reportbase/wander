"""TWS, after R289: at every address s = v/h = tan θ, the inscribed sweep's address density (the even turn on (0, π/2)
laid on the line) equals (2/π) times the foot h² = cos²θ of the point that address points to on the chord. A density
integrates to the Cauchy's arctangent, the foot needs no integrating; they agree in shape only. Exact, mpmath.
Run: python3 tws/density.py
"""
from mpmath import mp, mpf, atan, cos, pi, quad, diff, fabs
mp.dps = 40
worst = mpf(0)
for k in range(1, 60):
    s = mpf(k) / 7
    th = atan(s)
    density = diff(lambda x: (2 / pi) * atan(x), s)          # d/ds of the share of the even turn below s
    foot = cos(th)**2                                         # the foot of P = (h², hv) on the chord AB = [0, 1]
    worst = max(worst, fabs(density - (2 / pi) * foot))
print(f"density − (2/π)·foot, worst over 59 addresses: {mp.nstr(worst, 3)}")
s = mpf(1)
print(f"at the corner: density {mp.nstr(diff(lambda x: (2 / pi) * atan(x), s), 15)}, foot {mp.nstr(cos(atan(s))**2, 15)}, "
      f"share of addresses up to the corner {mp.nstr((2 / pi) * atan(s), 15)}")
