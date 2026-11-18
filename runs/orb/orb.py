"""ORB run 1: an oscillator and an orbit from one standpoint (plans/orb-plan.md)."""
import random
from fractions import Fraction as Q
import mpmath as mp

mp.mp.dps = 50
random.seed(1103)
out = []
def say(*a):
    s = ' '.join(str(t) for t in a); print(s); out.append(s)
def fr(x): return mp.mpf(x.numerator) / x.denominator
def mulv(M, v): return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])

# O1-O3
o1 = o2 = 0; und = und_ok = damp = damp_none = 0
for _ in range(50):
    g = Q(random.randint(0, 5), 10)
    w2 = g * g + Q(random.randint(1, 40), 10)
    u = Q(1, random.randint(0, 6) + 4)
    x0 = (Q(random.randint(-5, 5), random.randint(1, 4)), Q(random.randint(-5, 5), random.randint(1, 4)))
    if x0 == (0, 0): x0 = (Q(1), Q(0))
    A = [[Q(0), Q(1)], [-w2, -2 * g]]
    P = [[1 + u * g, u], [-u * w2, 1 - u * g]]          # I + u(A + gI)
    v = x0
    for _ in range(6): v = mulv(P, v)
    Om2 = w2 - g * g; Om = mp.sqrt(fr(Om2))
    tau = mp.atan(fr(u) * Om) / Om
    lam = mp.e ** (-fr(g) * tau) / mp.sqrt(1 + fr(u) ** 2 * fr(Om2))
    E = mp.expm(6 * tau * mp.matrix([[fr(A[i][j]) for j in range(2)] for i in range(2)]))
    fx = E[0, 0] * fr(x0[0]) + E[0, 1] * fr(x0[1]); fy = E[1, 0] * fr(x0[0]) + E[1, 1] * fr(x0[1])
    # direction as a pair: cross product zero
    o1 += abs(fx * fr(v[1]) - fy * fr(v[0])) < mp.mpf(10) ** -40 * (1 + abs(fx) + abs(fy)) * (1 + abs(fr(v[0])) + abs(fr(v[1])))
    o2 += abs(lam ** 6 * fr(v[0]) - fx) < mp.mpf(10) ** -40 and abs(lam ** 6 * fr(v[1]) - fy) < mp.mpf(10) ** -40
    if g == 0:
        und += 1
        lam2 = Q(1) / (1 + u * u * w2)
        e0 = w2 * x0[0] ** 2 + x0[1] ** 2; v1 = mulv(P, x0); e1 = w2 * v1[0] ** 2 + v1[1] ** 2
        und_ok += (e0 / e1 == lam2) and abs(lam ** 2 - fr(lam2)) < mp.mpf(10) ** -45
    else:
        damp += 1
        damp_none += mp.pslq([lam ** 2, 1], maxcoeff=10 ** 4, maxsteps=10 ** 5) is None
say('O1 direction after 6 rational steps = flow (as a pair) to 1e-40:', o1, '/ 50')
say('O2 state = lambda^6 * rational steps to 1e-40:', o2, '/ 50')
say('O3 undamped lambda^2 = 1/(1 + u^2 w^2) exactly (energy ratio):', und_ok, '/', und,
    '; damped, no relation [lambda^2, 1] of height <= 1e4:', damp_none, '/', damp)

# K1
k1 = 0
for _ in range(500):
    l = Q(random.randint(4, 20), 4); e = Q(random.randint(1, 19), 20)
    t = Q(random.choice([-1, 1]) * random.randint(0, 30), random.randint(1, 12))
    r = l * (1 + t * t) / ((1 + e) + (1 - e) * t * t)
    x = r * (1 - t * t) / (1 + t * t); y = r * 2 * t / (1 + t * t)
    k1 += x * x + y * y == (l - e * x) ** 2
say('K1 rational points on the conic exactly:', k1, '/ 500')

# K2
k2 = 0
for _ in range(50):
    l = Q(random.randint(4, 20), 4); e = Q(random.randint(1, 19), 20); a = Q(1, random.randint(3, 40))
    t = Q(0)
    for _ in range(20): t = (t + a) / (1 - t * a) if t * a != 1 else None
    if t is None: continue
    r = l * (1 + t * t) / ((1 + e) + (1 - e) * t * t)
    x = r * (1 - t * t) / (1 + t * t); y = r * 2 * t / (1 + t * t)
    phi = 40 * mp.atan(fr(a)); rr = fr(l) / (1 + fr(e) * mp.cos(phi))
    k2 += abs(rr * mp.cos(phi) - fr(x)) < mp.mpf(10) ** -40 and abs(rr * mp.sin(phi) - fr(y)) < mp.mpf(10) ** -40
say('K2 twenty composed half-slopes land on the angle 40 atan(a):', k2, '/ 50')

# K3
k3 = 0; n3 = 0
while n3 < 50:
    e = Q(random.randint(1, 19), 20); t = Q(random.choice([-1, 1]) * random.randint(1, 30), random.randint(1, 12))
    n3 += 1
    E = 2 * mp.atan(mp.sqrt((1 - fr(e)) / (1 + fr(e))) * fr(t))
    M = E - fr(e) * mp.sin(E)
    k3 += mp.pslq([M, 1, mp.pi], maxcoeff=10 ** 4, maxsteps=10 ** 5) is None
say('K3 no relation [M, 1, pi] of height <= 1e4:', k3, '/ 50')

# K4
for e in (mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9')):
    M = mp.mpf(1) / 2; E = M if e < 0.8 else mp.pi; it = 0
    while True:
        f = E - e * mp.sin(E) - M
        if abs(f) < mp.mpf(10) ** -40: break
        E -= f / (1 - e * mp.cos(E)); it += 1
        if it > 100: break
    say('K4 e =', mp.nstr(e, 2), ': Newton iterations to 1e-40:', it)

open('runs/orb/orb-run1.txt', 'w').write('\n'.join(out) + '\n')
