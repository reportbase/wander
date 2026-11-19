# NFS run 1: where the near-field sphere goes. Exact (mpmath 30 digits).
from mpmath import mp, mpf, sqrt, atan, asin, cos, sin, tan, pi, quad, acos, log, sech
mp.dps = 30
r3 = sqrt(3)
# N1
a0 = asin(1/r3); r0 = tan(a0)
print("N1 rim r0", r0, " 1/sqrt2", 1/sqrt(2), " share", 1 - cos(a0), " 1-sqrt(2/3)", 1 - sqrt(mpf(2)/3))
# N2
print("N2 heat at rim cos^3", cos(a0)**3, " half-heat r", sqrt(2**(mpf(2)/3) - 1), " share", 1 - 2**(-mpf(1)/3))
# N3
import itertools
look = [1/r3]*3
for h in [(0,1,1),(1,0,1),(1,1,0)]:
    n = sqrt(sum(x*x for x in h)); ca = sum(a*b for a,b in zip(h,look))/n
    print("N3 home", h, " r", tan(acos(ca)), " dist", n)
for t in [(1,0,0),(0,1,0),(0,0,1)]:
    ca = sum(a*b for a,b in zip(t,look)); print("N3 thumb tip", t, " r", tan(acos(ca)))
print("N3 tangent length", sqrt(3 - 1))
# N4: intersection of |p|=1 and |p-c|=1, c at distance sqrt3
x = r3/2; rad = sqrt(1 - x*x); print("N4 plane", x, " radius", rad, " alpha deg", atan(rad/x)*180/pi)
# heat mass: direction uniform on hemisphere (density sin a da/(1) over a in [0,pi/2], azimuth trivial), distance CDF (2/pi)atan d
def F(d): return 2/pi*atan(d)
# N5: S1 holds F(1)=1/2 on every direction
print("N5 S1 share", F(1))
# N6: S2 along direction a: d = sqrt3 cos a -+ sqrt(3cos^2 a - 2)
def m(a):
    c2 = 3*cos(a)**2 - 2
    if c2 <= 0: return mpf(0)
    d1 = r3*cos(a) - sqrt(c2); d2 = r3*cos(a) + sqrt(c2)
    return (F(d2) - F(d1))*sin(a)
S2 = quad(m, [0, a0])
print("N6 S2 share of combined heat", S2)
# N7
print("N7 hot point dist from c", r3 - 1)
# N8: heat cos^3(a) * sech(ln d) on S2, sampled over the sphere
import random
random.seed(1)
vals = []
for _ in range(4000):
    while True:
        v = [random.gauss(0,1) for _ in range(3)]
        n = sqrt(sum(x*x for x in v))
        p = [1 + x/n for x in v]
        d = sqrt(sum(x*x for x in p))
        ca = sum(a*b for a,b in zip(p,look))/d
        break
    vals.append(ca**3 * sech(log(d)))
mean = sum(vals)/len(vals); spread = max(vals) - min(vals)
print("N8 heat on S2 mean", mean, " min", min(vals), " max", max(vals), " spread/mean", spread/mean)
