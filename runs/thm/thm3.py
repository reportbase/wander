# THM run 3: U1' and U5' (plans/thm-plan.md). 50-digit mpmath.
import mpmath as mp
mp.mp.dps = 50
ok = lambda c: 'not killed' if c else 'KILLED'
s3 = mp.sqrt(3); half = mp.asin(1/s3)
look = [1/s3]*3
def ang(v):
    n = mp.sqrt(sum(x*x for x in v)); return mp.acos(sum(v[i]*look[i] for i in range(3))/n)
feet = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
devs = [abs(ang([mp.mpf(x) for x in f]) - half) for f in feet]
dist = [mp.sqrt(sum((1 - f[i])**2 for i in range(3))) for f in feet]
print("U1' touch points off the look minus the half-angle:", [mp.nstr(d, 3) for d in devs], '; their distance from C:', [mp.nstr(d, 5) for d in dist])
U1 = max(devs) < mp.mpf(10)**-40 and all(abs(d - 1) < mp.mpf(10)**-40 for d in dist)
print("U1'", ok(U1))

B = [1/mp.sqrt(6), 1/mp.sqrt(6), -2/mp.sqrt(6)]   # toward (1,1,0) from the look
def at(t):
    d = [mp.cos(t)*look[i] + mp.sin(t)*B[i] for i in range(3)]
    ls = [mp.log(d[i]/d[j]) for i, j in ((0, 1), (1, 2), (2, 0))]
    return mp.cosh(max(abs(x) for x in ls)), min(d)/max(d)
cross = None
for tdeg in (0, 5, 15, 25, 30, 33, 34, 35, 35.2, 35.26, 35.264):
    g, r = at(mp.mpf(tdeg)*mp.pi/180)
    print("U5' toward the touch point %7.3f°: worst grain ×%s, least reading %s, grain × reading %s" % (tdeg, mp.nstr(g, 8), mp.nstr(r, 8), mp.nstr(g*r, 10)))
for k in range(1, 3600):
    t = half*k/3600
    if cross is None and at(t)[0] > mp.mpf('2.1183179'): cross = t*180/mp.pi
g, r = at(half*(1 - mp.mpf(10)**-15))
print("U5' at 10⁻¹⁵ short of the outline: grain × reading", mp.nstr(g*r, 15), "; the grain passes ×2.118 at", mp.nstr(cross, 8), '°')
U5 = abs(g*r - mp.mpf(1)/2) < 1e-6 and cross < 35
print("U5'", ok(U5))
