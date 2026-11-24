# FCL run 8: bodies with size (two uniform balls) and a lens of two masses on a line.
# Predictions in plans/fcl-plan.md, committed before this ran.  python3 runs/fcl/fcl8.py
from mpmath import mp, mpf, mpc, sqrt, polyroots, atan, pi, im, re, findroot, fabs
mp.dps = 40
ok = lambda b: 'ok' if b else 'KILLED'

def pulls(s, M1, M2, R1, R2, D):
    t = D - s
    g1 = M1/t**2 if t >= R1 else M1*t/R1**3
    g2 = M2/s**2 if s >= R2 else M2*s/R2**3
    return g1, g2

def balance(M1, M2, R1, R2, D):
    """Every balance point on (0, D), region by region, in closed form."""
    out = []
    c = M1*R2**3/M2                      # inside ball 2: s (D-s)^2 = c
    for r in polyroots([1, -2*D, D*D, -c], maxsteps=200, extraprec=200):
        if fabs(im(r)) < mpf(10)**-25 and 0 < re(r) < R2: out.append(('in 2', re(r)))
    sp = D*sqrt(M2)/(sqrt(M1) + sqrt(M2)) # both outside: the point meeting place
    if R2 <= sp <= D - R1: out.append(('between', sp))
    c = M2*R1**3/M1                      # inside ball 1: t (D-t)^2 = c
    for r in polyroots([1, -2*D, D*D, -c], maxsteps=200, extraprec=200):
        if fabs(im(r)) < mpf(10)**-25 and 0 < re(r) < R1: out.append(('in 1', D - re(r)))
    return sorted(out, key=lambda x: x[1])

def scan(M1, M2, R1, R2, D, n=20000):
    k = 0; prev = None
    for i in range(1, n):
        s = D*mpf(i)/n; g1, g2 = pulls(s, M1, M2, R1, R2, D); f = g1 - g2
        if prev is not None and (f > 0) != (prev > 0): k += 1
        prev = f
    return k

print('A1  three balance points; the outer one at rho = sqrt(mu), unmoved by the radii')
A1 = True
for M1, M2, R1, R2, D in [(1, 1, '0.2', '0.2', 1), (3, 1, '0.3', '0.15', 1), (10, 1, '0.1', '0.05', 1), (2, 5, '0.25', '0.3', 1)]:
    M1, M2, R1, R2, D = map(mpf, (M1, M2, R1, R2, D))
    b = balance(M1, M2, R1, R2, D); k = scan(M1, M2, R1, R2, D)
    mid = [s for w, s in b if w == 'between']
    rho = (D - mid[0])/mid[0] if mid else None
    e = fabs(rho - sqrt(M1/M2)) if mid else mpf(1)
    good = len(b) == 3 and k == 3 and e < mpf(10)**-25; A1 &= good
    print('  M1/M2 %s R1 %s R2 %s: %d points (scan %d) at s = %s; rho - sqrt(mu) = %s  %s' % (
        mp.nstr(M1/M2, 4), R1, R2, len(b), k, ', '.join(mp.nstr(s, 8) for w, s in b), mp.nstr(e, 3), ok(good)))
print('A1', ok(A1))

print('\nA2  the inner point at s ~ M1 R2^3/(M2 D^2); the exchange does not hold inside')
A2 = True
for M1, M2, R2 in [(1, 1, '0.1'), (1, 4, '0.2'), (3, 1, '0.1'), (1, 1, '0.2')]:
    M1, M2, R2, D, R1 = mpf(M1), mpf(M2), mpf(R2), mpf(1), mpf('0.05')
    b = balance(M1, M2, R1, R2, D); s = [x for w, x in b if w == 'in 2'][0]
    pred = M1*R2**3/(M2*D*D); rel = fabs(s/pred - 1)
    test = pred < D/100; good = (rel < mpf('0.02')) if test else True; A2 &= good
    print('  M1/M2 %s R2 %s: s = %s, predicted %s, off %s%%%s  %s' % (mp.nstr(M1/M2, 3), R2, mp.nstr(s, 10), mp.nstr(pred, 10),
          mp.nstr(100*rel, 3), '' if test else ' (past D/100, not tested)', ok(good)))
for M1, M2, R2, s in [(1, 1, '0.3', '0.1'), (3, 1, '0.4', '0.25'), (1, 2, '0.3', '0.2')]:
    M1, M2, R2, s, D, R1 = mpf(M1), mpf(M2), mpf(R2), mpf(s), mpf(1), mpf('0.01')
    mu = M1/M2; rho = (D - s)/s; rho2 = mu/rho; s2 = D/(1 + rho2)
    g1, g2 = pulls(s, M1, M2, R1, R2, D); h1, h2 = pulls(s2, M1, M2, R1, R2, D)
    prod = (g1/g2)*(h1/h2); good = fabs(prod - 1) > mpf(10)**-6; A2 &= good
    print('  place s %s inside ball 2 (R2 %s), partner at s %s: pull ratios multiply to %s (points: 1)  %s' % (
        s, R2, mp.nstr(s2, 6), mp.nstr(prod, 8), ok(good)))
print('A2', ok(A2))

print('\nA3  three or one, never two; the pair meet at D/3 when M2/M1 = (27/4)(R2/D)^3')
A3 = True
for R2, R1 in [('0.45', '0.2'), ('0.5', '0.3'), ('0.6', '0.1')]:
    R2, R1, D, M1 = mpf(R2), mpf(R1), mpf(1), mpf(1)
    crit = mpf(27)/4*(R2/D)**3
    na = len(balance(M1, crit*mpf('1.01'), R1, R2, D)); nb = len(balance(M1, crit*mpf('0.99'), R1, R2, D))
    ka = scan(M1, crit*mpf('1.01'), R1, R2, D); kb = scan(M1, crit*mpf('0.99'), R1, R2, D)
    # at the ratio itself: the double root of s (D-s)^2 = 4 D^3/27
    c = M1*R2**3/crit; ds = findroot(lambda s: (D - s)**2 - 2*s*(D - s), D/4)   # where d/ds of s(D-s)^2 is zero
    resid = fabs(ds*(D - ds)**2 - c)
    good = na == 3 and nb == 1 and ka == 3 and kb == 1 and fabs(ds - D/3) < mpf(10)**-6 and resid < mpf(10)**-30 and ds < R2
    A3 &= good
    print('  R2 %s: M2/M1 crit %s; 1%% above %d points (scan %d), 1%% below %d (scan %d); meet at s = %s, residual there %s  %s' % (
        R2, mp.nstr(crit, 8), na, ka, nb, kb, mp.nstr(ds, 12), mp.nstr(resid, 3), ok(good)))
print('A3', ok(A3))

# ---- B: two lens masses on a line
def F(u, z):   # distribution function of the Cauchy with point z = m + i g
    return mpf(1)/2 + atan((u - re(z))/im(z))/pi
def dens(u, z):
    return im(z)/((u - re(z))**2 + im(z)**2)/pi
def roots3(y, a, b, e1, e2):   # f(u) = y, f(u) = u - e1/(u-a) - e2/(u-b)
    # (u-y)(u-a)(u-b) - e1 (u-b) - e2 (u-a) = 0
    return polyroots([1, -(y + a + b), a*b + y*(a + b) - e1 - e2, -y*a*b + e1*b + e2*a], maxsteps=300, extraprec=300)

print('\nB1  images Cauchy(z) along the line come from sources Cauchy(z - e1/(z-a) - e2/(z-b))')
B1 = True
for a, b, e1, e2 in [('-0.6', '0.6', '0.5', '0.5'), ('-0.3', '0.9', '0.8', '0.2')]:
    a, b, e1, e2 = map(mpf, (a, b, e1, e2))
    for z in [mpc('0.2', '0.7'), mpc('-1.1', '0.3'), mpc('0.5', '2')]:
        w = z - e1/(z - a) - e2/(z - b); worst = mpf(0)
        for y in ['-3', '-1', '-0.25', '0', '0.4', '1.5', '4']:
            y = mpf(y); r = sorted(re(x) for x in roots3(y, a, b, e1, e2))
            assert r[0] < a < r[1] < b < r[2]
            lhs = F(r[0], z) + F(r[1], z) - F(a, z) + F(r[2], z) - F(b, z)
            worst = max(worst, fabs(lhs - F(y, w)))
        good = worst < mpf(10)**-20; B1 &= good
        print('  masses %s, %s at %s, %s; z %s -> w %s: worst gap %s  %s' % (e1, e2, a, b, mp.nstr(z, 3), mp.nstr(w, 6), mp.nstr(worst, 3), ok(good)))
print('B1', ok(B1))

print('\nB2  sources Cauchy(w) are seen as three Cauchys, their points adding to w + a + b')
B2 = True
for a, b, e1, e2 in [('-0.6', '0.6', '0.5', '0.5'), ('-0.3', '0.9', '0.8', '0.2')]:
    a, b, e1, e2 = map(mpf, (a, b, e1, e2))
    for w in [mpc('0.1', '0.5'), mpc('1.3', '0.2'), mpc('-0.4', '1.5')]:
        zs = roots3(w, a, b, e1, e2); up = all(im(z) > 0 for z in zs)
        ssum = fabs(sum(zs) - (w + a + b)); worst = mpf(0)
        for u in ['-4', '-2', '-1', '-0.7', '-0.45', '-0.1', '0.2', '0.5', '0.75', '1.2', '2', '5']:
            u = mpf(u); fu = u - e1/(u - a) - e2/(u - b); fp = 1 + e1/(u - a)**2 + e2/(u - b)**2
            worst = max(worst, fabs(dens(fu, w)*fp - sum(dens(u, z) for z in zs)))
        good = up and ssum < mpf(10)**-25 and worst < mpf(10)**-20; B2 &= good
        print('  w %s: z = %s; all above the line %s; sum off %s; density gap %s  %s' % (
            mp.nstr(w, 3), ', '.join(mp.nstr(z, 5) for z in zs), up, mp.nstr(ssum, 3), mp.nstr(worst, 3), ok(good)))
print('B2', ok(B2))
