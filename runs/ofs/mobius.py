"""mobius.py: is the Cauchy family closed under every real Möbius map of the signed reading? (OFS §11.2's table; SPN R418.)

ChatGPT, via Tom, 21 Oct 2026: "is the claimed Cauchy invariance valid under every transformation in that stated class
... General real Möbius transformations include maps with poles". McCullagh 1996's theorem: X ~ C(z) gives
(aX + b)/(cX + d) ~ C(g(z)) for every real map with ad − bc ≠ 0 (the conjugate for ad − bc < 0). A check of a classical
result, not a test of ours, so no prediction was written: 200 random maps of both signs, poles included, the law of g(X)
from X's distribution function on the two sides of the pole against C(g(z)), at four points each; and one case by sampling.
"""
import mpmath as mp
mp.mp.dps=30
# X ~ C(z), g(x)=(ax+b)/(cx+d). Claim: g(X) ~ C(g(z)) if det>0, C(conj g(z)) if det<0. Check the CDF exactly at points.
def F(z,x): m,g=z.real,z.imag; return mp.mpf(1)/2+mp.atan((x-m)/g)/mp.pi
def P_gX_le(z,a,b,c,d,y):
    # g(X)<=y : solve on the projective line; integrate the density over the preimage set numerically
    pole=-d/c
    # exact: preimage of (-inf,y] is an interval of the projective line with ends pole and g^{-1}(y)
    xi=(d*y-b)/(a-c*y)
    det=a*d-b*c
    A=F(z,xi); Pp=F(z,pole)
    # g is monotone (increasing if det>0) on each side of the pole
    if det>0:
        return (A-Pp) if xi>pole else (A+1-Pp)
    else:
        return (Pp-A) if xi<pole else (Pp+1-A)
worst=0
import random; R=random.Random(3)
for _ in range(200):
    z=mp.mpc(R.uniform(-3,3),R.uniform(0.1,3)); a,b,c,d=[mp.mpf(R.uniform(-2,2)) for _ in range(4)]
    w=(a*z+b)/(c*z+d); w=w if w.imag>0 else mp.conj(w)
    for y in (-5,-0.3,0.7,4):
        worst=max(worst,abs(P_gX_le(z,a,b,c,d,mp.mpf(y))-F(w,mp.mpf(y))))
print('worst', mp.nstr(worst,3))
# brute check one case by quadrature of the indicator
z=mp.mpc(0.4,0.8);a,b,c,d=1,2,1.5,-1  # det<0, pole at 2/3
y=mp.mpf('0.7'); w=mp.conj((a*z+b)/(c*z+d))
import numpy as np
xs=np.random.default_rng(1).standard_cauchy(2_000_000)*0.8+0.4
print('MC', np.mean((xs+2)/(1.5*xs-1)<=0.7), 'law', float(F(w,y)))
