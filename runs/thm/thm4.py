# THM run 4: distance and direction together (plans/thm-plan.md). 50-digit mpmath, seeded.
import mpmath as mp, random
mp.mp.dps = 50
ok = lambda c: 'not killed' if c else 'KILLED'
E = mp.mpf(10)**-40
rnd = random.Random(2026)
s3 = mp.sqrt(3)
def wedge_dir():
    while True:
        v = [abs(mp.mpf(rnd.gauss(0, 1))) for _ in range(3)]
        n = mp.sqrt(sum(x*x for x in v))
        if n > 0: return [x/n for x in v]
worst1 = worst2 = mp.mpf(0); maxterm = mp.mpf(-1e9); worst3 = mp.mpf(0)
for _ in range(10000):
    n = wedge_dir(); r = mp.mpf(rnd.uniform(0.01, 100))
    q = [r*s3*x for x in n]                      # reach in thumbs: |p| = r*sqrt3*H
    L = [mp.log(x) for x in q]; Lb = sum(L)/3
    lhs = sum(x*x for x in L); rhs = 3*Lb**2 + (sum((L[i]-L[j])**2 for i, j in ((0,1),(1,2),(0,2))))/3
    worst1 = max(worst1, abs(lhs - rhs))
    k = mp.mpf(rnd.uniform(0.1, 10)); L2 = [mp.log(k*x) for x in q]
    worst2 = max(worst2, max(abs((L2[i]-L[i]) - mp.log(k)) for i in range(3)), max(abs((L2[i]-L2[j]) - (L[i]-L[j])) for i, j in ((0,1),(1,2),(0,2))))
    term = sum(mp.log(s3*x) for x in n)/3
    maxterm = max(maxterm, term)
    worst3 = max(worst3, abs(Lb - (mp.log(r) + term)))
print('V1 worst |ΣL² − (3L̄² + Σpairs/3)| over 10⁴:', mp.nstr(worst1, 3)); print('V1', ok(worst1 < E))
print('V2 worst shift error:', mp.nstr(worst2, 3)); print('V2', ok(worst2 < E))
print('V3 L̄ − (ln r + term) worst', mp.nstr(worst3, 3), '; largest term', mp.nstr(maxterm, 6), '(≤ 0)')
term_look = sum(mp.log(s3*x) for x in [1/s3]*3)/3
print('V3 term on the look', term_look, '; toward home', [mp.nstr(sum(mp.log(s3*x) for x in (mp.cos(t)/s3 + mp.sin(t)/mp.sqrt(6), mp.cos(t)/s3 + mp.sin(t)/mp.sqrt(6), mp.cos(t)/s3 - 2*mp.sin(t)/mp.sqrt(6)))/3, 6) for t in (mp.mpf('0.3'), mp.asin(1/s3) - mp.mpf('1e-6'))])
print('V3', ok(worst3 < E and maxterm <= 0 and term_look == 0))
# V4: cosh(ln r) = 2 at r = 2 ± sqrt3
r_hi, r_lo = mp.exp(mp.acosh(2)), mp.exp(-mp.acosh(2))
print('V4 half size at r =', mp.nstr(r_lo, 12), 'and', mp.nstr(r_hi, 12), '; 2 ± √3 =', mp.nstr(2 - s3, 12), mp.nstr(2 + s3, 12))
# worst-thumb grain differs from the product: an example off the look at the corner distance
n = [mp.cos(mp.mpf('0.4'))/s3 + mp.sin(mp.mpf('0.4'))/mp.sqrt(6)*a for a in (1, 1, -2)]
q = [s3*x for x in n]; L = [mp.log(x) for x in q]
gw = mp.cosh(max(abs(x) for x in L)); gd = mp.cosh(max(abs(L[i]-L[j]) for i, j in ((0,1),(1,2),(0,2))))
print('V4 at r = 1, 0.4 rad toward a home: worst-thumb grain', mp.nstr(gw, 8), '; product (direction × distance)', mp.nstr(gd, 8))
print('V4', ok(abs(r_hi - (2 + s3)) < E and abs(r_lo - (2 - s3)) < E and abs(gw - gd) > 1e-3))
# V5: plane
worst5 = mp.mpf(0); maxt5 = mp.mpf(-1)
s2 = mp.sqrt(2)
for _ in range(10000):
    t = mp.mpf(rnd.uniform(0, 1))*mp.pi/2; r = mp.mpf(rnd.uniform(0.01, 100))
    n = [mp.cos(t), mp.sin(t)]
    if min(n) <= 0: continue
    q = [r*s2*x for x in n]; L = [mp.log(x) for x in q]
    term = (mp.log(s2*n[0]) + mp.log(s2*n[1]))/2; maxt5 = max(maxt5, term)
    worst5 = max(worst5, abs((L[0]+L[1])/2 - (mp.log(r) + term)), abs((L[0]**2 + L[1]**2) - (2*((L[0]+L[1])/2)**2 + (L[0]-L[1])**2/2)))
print('V5 plane: worst', mp.nstr(worst5, 3), '; largest term', mp.nstr(maxt5, 6), '; disc outline half-angle', mp.nstr(mp.degrees(mp.asin(1/s2)), 12), '°')
print('V5', ok(worst5 < E and maxt5 <= 0 and abs(mp.asin(1/s2) - mp.pi/4) < E))
