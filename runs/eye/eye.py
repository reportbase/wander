# EYE: give the bar eyes (plans/eye-plan.md). Run from the repository root: python3 runs/eye/eye.py
import random
from mpmath import mp, mpf, pi, tan, atan2, cos, sin, sqrt, floor, diff, findroot, log
mp.dps = 50
rnd = random.Random(1119)
def rec(theta, K):                      # receptor index of a direction, receptors uniform by turn, width (pi/2)/K
    return int(floor(K * (theta % (2*pi)) / (pi/2)))
def things(n):
    out = []
    for _ in range(n):
        d = mpf(10) ** mpf(rnd.uniform(-1.3, 4)); a = mpf(rnd.uniform(0.05, 1.5))
        out.append((d*cos(a), d*sin(a)))
    return out
T = things(400)
print("E1  pivot, a uniform sky")
for K in (8, 64, 256):
    shares = [((k+1)*(pi/2)/K - k*(pi/2)/K)/(pi/2) for k in range(K)]
    worst = max(abs(s - mpf(1)/K) for s in shares)
    print(f"   K={K:4d}  worst share off 1/K {mp.nstr(worst,3)}  median boundary slope {mp.nstr(tan((K//2)*pi/(2*K)),20)}")
print("E2  pivot, scaling and turning")
for K in (64, 1024):
    base = [rec(atan2(y, x), K) for x, y in T]
    for k in (mpf('1e-3'), mpf(7), mpf('1e3')):
        sc = [rec(atan2(k*y, k*x), K) for x, y in T]
        assert sc == base
    al = mpf('0.3')
    tu = [rec(atan2(y, x) - al, K) for x, y in T]
    gaps = max(abs((tu[i]-tu[j]) - (base[i]-base[j])) for i in range(0, 400, 7) for j in range(0, 400, 11))
    print(f"   K={K:5d}  scaling by 1e-3, 7, 1e3: every receptor the same; turned 0.3: largest gap change {gaps} receptor(s)")
def tri(E1, t1, E2, t2):                # cross two rays, return point
    (x1, y1), (x2, y2) = E1, E2
    c1, s1, c2, s2 = cos(t1), sin(t1), cos(t2), sin(t2)
    den = c1*s2 - s1*c2
    u = ((x2-x1)*s2 - (y2-y1)*c2) / den
    return (x1 + u*c1, y1 + u*s1)
def trace_eyes(D): return (mpf(1), mpf(0)), (cos(D), sin(D))
print("E3  trace, turning gives distance (exact directions)")
for D in (pi/6, pi/2, 5*pi/6):
    A, B = trace_eyes(D); worst = mpf(0); n = 0
    for (x, y) in T:
        ta, tb = atan2(y-A[1], x-A[0]), atan2(y-B[1], x-B[0])
        if abs(sin(ta - tb)) < mpf('1e-30'): continue
        p = tri(A, ta, B, tb); worst = max(worst, sqrt((p[0]-x)**2 + (p[1]-y)**2)/sqrt(x*x+y*y)); n += 1
    # scale the world (bar unchanged): places in bars move by k; scale all: unmoved
    x, y = T[3]; k = mpf(7)
    ta, tb = atan2(k*y-A[1], k*x-A[0]), atan2(k*y-B[1], k*x-B[0]); p = tri(A, ta, B, tb)
    Ak, Bk = (k*A[0], k*A[1]), (k*B[0], k*B[1])
    ta2, tb2 = atan2(k*y-Ak[1], k*x-Ak[0]), atan2(k*y-Bk[1], k*x-Bk[0]); q = tri(Ak, ta2, Bk, tb2)
    print(f"   turn {mp.nstr(D*180/pi,4)} deg: {n} things, worst relative place error {mp.nstr(worst,3)};"
          f" world x7: place moves by {mp.nstr(sqrt(p[0]**2+p[1]**2)/sqrt(x*x+y*y),6)} in bars;"
          f" all x7: place in bars {mp.nstr(sqrt(q[0]**2+q[1]**2)/k/sqrt(x*x+y*y),6)} of the unscaled")
print("E4  trace, K receptors (directions read to the receptor's middle), turn pi/2")
def qdir(t, K):
    eps = (pi/2)/K; return (floor(t/eps) + mpf(1)/2) * eps
mp.dps = 30
A, B = trace_eyes(pi/2); M = ((A[0]+B[0])/2, (A[1]+B[1])/2)
nb = (M[0], M[1]); nn = sqrt(nb[0]**2 + nb[1]**2); nb = (nb[0]/nn, nb[1]/nn)   # outward bisector from the pivot side
def med_err(d, K, m=81):
    errs = []
    for i in range(m):
        off = mpf(rnd.uniform(-0.5, 0.5)); c, s = cos(off), sin(off)
        dirx, diry = nb[0]*c - nb[1]*s, nb[0]*s + nb[1]*c
        x, y = M[0] + d*dirx, M[1] + d*diry
        ta, tb = qdir(atan2(y-A[1], x-A[0]), K), qdir(atan2(y-B[1], x-B[0]), K)
        if abs(sin(ta-tb)) < mpf('1e-25'): errs.append(mpf(10)); continue
        p = tri(A, ta, B, tb); errs.append(sqrt((p[0]-x)**2+(p[1]-y)**2)/d)
    errs.sort(); return errs[m//2]
for K in (64, 256, 1024):
    eps = (pi/2)/K; reach = 1/eps
    lo, hi = mpf('0.5'), 40*reach
    for _ in range(40):                 # bisect on log d for median error 1/2
        mid = sqrt(lo*hi)
        if med_err(mid, K) < mpf(1)/2: lo = mid
        else: hi = mid
    print(f"   K={K:5d}  sin(D)/eps = {mp.nstr(reach,5)} bars; median error 1/2 at {mp.nstr(lo,5)} bars, ratio {mp.nstr(lo/reach,4)};"
          f" at 4x reach {mp.nstr(med_err(4*reach, K),3)}")
mp.dps = 50
print("E5  both ends, still: relative error per unit direction error on the bisector")
def rel(d):
    th = atan2(d, mpf(1)/2)             # eye A at (0,0), B at (1,0), point (1/2, d)
    f = lambda t: tan(t)/2              # depth from A's direction, B's held at the mirror
    return diff(f, th) / d
dmin = findroot(lambda d: diff(rel, d), mpf('0.4'))
print(f"   least at d = {mp.nstr(dmin,20)} bars; rel(0.5) = {mp.nstr(rel(mpf('0.5')),15)}")
for d in (mpf('0.05'), mpf('0.2'), mpf(3), mpf(40)):
    print(f"   d={mp.nstr(d,4):>5}  rel {mp.nstr(rel(d),12)}  rel(1/(4d)) {mp.nstr(rel(1/(4*d)),12)}  diff {mp.nstr(abs(rel(d)-rel(1/(4*d))),3)}")
print("E6  the pivot's eye turned: baseline", mp.nstr(sqrt((mpf(0)-0)**2), 3), "(the eye does not move), so no distance")
