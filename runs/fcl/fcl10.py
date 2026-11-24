# FCL run 10: the subtraction on the read's side.  Predictions in plans/fcl-plan.md, committed before this ran.
# python3 runs/fcl/fcl10.py   (mpmath at 40 digits for T2-T4; numpy doubles for T1, T5)
import numpy as np
from mpmath import mp, mpf, quad, findroot, legendre, pi, sin, cos, fabs, arg, mpc, exp, degrees
mp.dps = 40
ok = lambda b: 'ok' if b else 'KILLED'
Om = pi/2

print('T1  the pull is the first moment of the paint m/d^2 over two looks back to back')
T1 = True; worst = 0
for seed in range(20):
    R = np.random.default_rng(seed); N = 25
    P = R.normal(size=(N, 3))*R.uniform(0.5, 4, (N, 1)); m = R.uniform(0.2, 2, N)
    d = np.linalg.norm(P, axis=1); u = P/d[:, None]; paint = m/d**2
    g = (paint[:, None]*u).sum(0)                                   # first moment, every source
    n = R.normal(size=3); n /= np.linalg.norm(n); c = u @ n
    front = (paint*c)[c > 0].sum(); back = (paint*(-c))[c < 0].sum()
    dip = ((3.7*m/(4*np.pi*d**2))[:, None]*u).sum(0)                # brightness dipole, light in proportion to mass
    ang = np.degrees(np.arccos(np.clip(dip @ g/np.linalg.norm(dip)/np.linalg.norm(g), -1, 1)))
    worst = max(worst, abs(front - back - n @ g), ang if ang > 1e-5 else 0)
T1 = worst < 1e-12
print('  20 scenes: worst of |front - back - n.g| and the dipole\'s angle off the pull: %.2e  %s' % (worst, ok(T1)))

print('\nT2  an even paint gives no odd moment')
T2 = True
for eps, a, b in [(mpf('0.3'), 1, 0), (mpf('0.5'), mpf('0.4'), mpf('-0.7')), (mpf('0.9'), -1, mpf('0.2'))]:
    gz = 2*pi*quad(lambda x: x*(1 + eps*(a*legendre(2, x) + b*legendre(4, x))), [-1, 0, 1])
    good = fabs(gz) < mpf(10)**-25; T2 &= good
    print('  (a) sky 1 + %s(%s P2 + %s P4): pull %s  %s' % (mp.nstr(eps, 2), mp.nstr(a, 2), mp.nstr(b, 2), mp.nstr(gz, 3), ok(good)))
def median(w):
    tot = quad(w, [0, Om/2, Om])
    return findroot(lambda t: quad(w, [0, t]) - tot/2, Om/2)
for name, f in [('sin 2θ', lambda t: sin(2*t)), ('cos 4(θ − Ω/2)', lambda t: cos(4*(t - Om/2))), ('(θ − Ω/2)²', lambda t: (t - Om/2)**2)]:
    mth = median(lambda t: 1 + mpf('0.3')*f(t)); good = fabs(mth - Om/2) < mpf(10)**-25; T2 &= good
    print('  (b) quarter turn 1 + 0.3·%s: median off the corner by %s  %s' % (name, mp.nstr(mth - Om/2, 3), ok(good)))
print('T2', ok(T2))

print('\nT3  of an odd paint each takes one moment')
T3 = True
for eps, a, b, c in [(mpf('0.3'), 1, 0, 0), (mpf('0.3'), 1, mpf('0.8'), mpf('-0.5')), (mpf('0.6'), mpf('-0.4'), 1, 1)]:
    gz = 2*pi*quad(lambda x: x*(1 + eps*(a*legendre(1, x) + b*legendre(3, x) + c*legendre(5, x))), [-1, 0, 1])
    good = fabs(gz - eps*a*4*pi/3) < mpf(10)**-25; T3 &= good
    print('  (a) sky 1 + %s(%s P1 + %s P3 + %s P5): pull %s, eps·a·4π/3 = %s  %s' % (mp.nstr(eps, 2), mp.nstr(a, 2), mp.nstr(b, 2), mp.nstr(c, 2), mp.nstr(gz, 12), mp.nstr(eps*a*4*pi/3, 12), ok(good)))
e = mpf(10)**-3
for name, f in [('sin 2(θ − Ω/2)', lambda t: sin(2*(t - Om/2))), ('θ − Ω/2', lambda t: t - Om/2), ('sin 6(θ − Ω/2)', lambda t: sin(6*(t - Om/2)))]:
    dm = median(lambda t: 1 + e*f(t)) - Om/2; pred = -e*quad(f, [0, Om/2]); good = fabs(dm/pred - 1) < mpf('0.02'); T3 &= good
    print('  (b) 1 + 10⁻³·%s: median moves %s, predicted %s, ratio %s  %s' % (name, mp.nstr(dm, 8), mp.nstr(pred, 8), mp.nstr(dm/pred, 8), ok(good)))
f8 = lambda t: sin(8*(t - Om/2)); w8 = lambda t: 1 + mpf('0.3')*f8(t)
dm = median(w8) - Om/2; mean = quad(lambda t: t*w8(t), [0, Om/2, Om])/quad(w8, [0, Om/2, Om]) - Om/2
good = fabs(dm) < mpf(10)**-25 and fabs(mean) > mpf('0.01'); T3 &= good
print('  (b) 1 + 0.3·sin 8(θ − Ω/2): near-half integral %s; median off the corner by %s; mean angle off by %s  %s' % (
    mp.nstr(quad(f8, [0, Om/2]), 3), mp.nstr(dm, 3), mp.nstr(mean, 8), ok(good)))
print('T3', ok(T3))

print('\nT4  same parity, different moments: the first moment and the balance axis part')
T4 = True; res = []
for eps in [mpf('0.01'), mpf('0.1'), mpf('0.5')]:
    rho = lambda t: 1 + eps*(cos(t) + mpf('0.8')*cos(3*t - 1))
    M = quad(lambda t: rho(t)*exp(mpc(0, 1)*t), [0, pi, 2*pi]); first = arg(M)
    bal = lambda p: quad(rho, [p, p + pi]) - quad(rho, [p - pi, p])       # paint on the left less paint on the right
    phi = findroot(bal, mpf('0.15')); res.append(phi)
    good = fabs(first) < mpf(10)**-20 and 5 < degrees(phi) < 15; T4 &= good
    print('  eps %s: first moment points at %s°; balance axis at %s°  %s' % (mp.nstr(eps, 2), mp.nstr(degrees(first), 3), mp.nstr(degrees(phi), 10), ok(good)))
same = fabs(res[0] - res[2]) < mpf(10)**-20; T4 &= same
print('  the balance axis the same at every eps: %s' % ok(same)); print('T4', ok(T4))

print('\nT5  one is a sum, the other a count')
moved = unmoved = 0
grid = np.linspace(0, np.pi, 3600, endpoint=False)
for seed in range(20):
    R = np.random.default_rng(100 + seed); N = 30
    th = R.uniform(0, 2*np.pi, N); d = R.uniform(0.5, 4, N); m = R.uniform(0.2, 2, N)
    def pulldir(mm): g = ((mm/d**2)*np.exp(1j*th)).sum(); return np.angle(g)
    def balance(mm):         # directions with as many sources on the left as on the right: uses no amount
        return tuple(int(np.sum(np.sin(th - p) > 0) == N//2) for p in grid)
    dth = abs(np.degrees(np.angle(np.exp(1j*(pulldir(m**3) - pulldir(m))))))
    moved += dth > 1; unmoved += balance(m) == balance(m**3)
T5 = moved >= 18 and unmoved == 20
print('  m -> m³: the pull\'s direction moved more than 1° in %d of 20; the count\'s balance axis unmoved in %d of 20  %s' % (moved, unmoved, ok(T5)))
