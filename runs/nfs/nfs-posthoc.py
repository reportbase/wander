# NFS post hoc: the heat's minimum on S2. On S2, d^2 = 2*sqrt3*d*cos(a) - 2.
from mpmath import mp, mpf, sqrt, cos, acos, asin, findroot, diff, pi
mp.dps = 30
r3 = sqrt(3)
def heat(a, far):
    c = cos(a); disc = max(3*c*c - 2, mpf(0))
    d = r3*c + (1 if far else -1)*sqrt(disc)
    return c**3 * 2*d/(1 + d*d), d
a0 = asin(1/r3)
best = None
for i in range(1, 20001):
    a = a0*i/20000
    for far in (True, False):
        h, d = heat(a, far)
        if best is None or h < best[0]: best = (h, a, d, far)
print("min heat on S2", best[0], " at alpha deg", best[1]*180/pi, " d", best[2], " far side", best[3])
print("heat at far point on the look (a=0, d=sqrt3+1)", heat(mpf(0), True)[0])
print("heat at the rim (d=sqrt2)", heat(a0, True)[0])
# refine the minimum to 30 digits
from mpmath import findroot
g = lambda a: heat(a, True)[0]
am = findroot(lambda a: diff(g, a), best[1])
print("refined: alpha deg", am*180/pi, " heat", g(am), " heat - 1/2", g(am) - mpf(1)/2, " d", heat(am, True)[1])
