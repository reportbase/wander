# FRG run 1: the Fisher–Rao geometry of the Cauchy family (plans/frg-plan.md). mpmath at 50 digits; F6 seeded numpy.
import mpmath as mp, numpy as np
mp.mp.dps = 50
pi = mp.pi
def logp(x, m, g): return mp.log(g / pi) - mp.log(g*g + (x - m)**2)
def over(m, g, f, extra=()):
    # E_{C(m,g)} f(x) with x = m + g tan(phi), p dx = dphi/pi; break where a narrow second law sits
    pts = [-pi/2] + sorted(set(mp.atan((e - m)/g) for e in extra)) + [pi/2]
    return mp.quad(lambda ph: f(m + g*mp.tan(ph)), pts) / pi
def KLq(z1, z2):
    m1, g1 = z1; m2, g2 = z2
    ex = [m2 + k*g2 for k in (-8, -2, -0.5, 0, 0.5, 2, 8)]
    return over(m1, g1, lambda x: logp(x, m1, g1) - logp(x, m2, g2), ex)
def KLc(z1, z2):
    m1, g1 = z1; m2, g2 = z2
    return mp.log(((m1 - m2)**2 + (g1 + g2)**2) / (4*g1*g2))
def dP(z1, z2):
    m1, g1 = z1; m2, g2 = z2
    return mp.acosh(1 + ((m1 - m2)**2 + (g1 - g2)**2) / (2*g1*g2))
rel = lambda a, b: abs(a - b) / max(abs(b), mp.mpf(10)**-45)
out = []
def verdict(name, ok, msg): out.append(f"{name}: {'not killed' if ok else 'KILLED'}. {msg}"); print(out[-1])

# F1
worst = mp.mpf(0)
for m, g in [(0, 1), (3, mp.mpf('0.2')), (-7, 40)]:
    m, g = mp.mpf(m), mp.mpf(g)
    sm = lambda x: 2*(x - m)/(g*g + (x - m)**2)
    sg = lambda x: 1/g - 2*g/(g*g + (x - m)**2)
    Imm = over(m, g, lambda x: sm(x)**2); Igg = over(m, g, lambda x: sg(x)**2); Img = over(m, g, lambda x: sm(x)*sg(x))
    worst = max(worst, rel(Imm, 1/(2*g*g)), rel(Igg, 1/(2*g*g)), abs(Img)*g*g)
verdict("F1", worst < mp.mpf(10)**-40, f"I = diag(1/2γ², 1/2γ²), off-diagonal 0, worst {mp.nstr(worst, 3)}")

# F2
pairs = [((0, 1), (0, 2)), ((0, 1), (1, 1)), ((3, mp.mpf('0.2')), (-7, 40)), ((0, 1), (10, mp.mpf('0.01'))),
         ((mp.mpf('-1.5'), mp.mpf('0.3')), (2, 5)), ((100, 7), (99, 8))]
w = mp.mpf(0)
for a, b in pairs:
    a = tuple(map(mp.mpf, a)); b = tuple(map(mp.mpf, b))
    q, qr, c = KLq(a, b), KLq(b, a), KLc(a, b)
    w = max(w, rel(q, c), rel(qr, c), rel(2*mp.log(mp.cosh(dP(a, b)/2)), c))
verdict("F2", w < mp.mpf(10)**-40, f"KL closed form, symmetric, = 2 ln cosh(d/2), six pairs, worst {mp.nstr(w, 3)}")

# F3
def mob(a, b, c, d):
    def g(z):
        w = (a*mp.mpc(z[0], z[1]) + b) / (c*mp.mpc(z[0], z[1]) + d); return (w.real, w.imag)
    return g
maps = {'k=1e-3': mob(mp.mpf('1e-3'), 0, 0, 1), 'k=7': mob(7, 0, 0, 1), 'k=1e6': mob(10**6, 0, 0, 1),
        'shift': mob(1, mp.mpf('-4.25'), 0, 1), 'exchange -1/z': mob(0, -1, 1, 0),
        'g1': mob(2, 1, 1, 3), 'g2': mob(1, -5, mp.mpf('0.5'), mp.mpf('0.25'))}
w = mp.mpf(0)
for nm, g in maps.items():
    for a, b in pairs[:4]:
        a = tuple(map(mp.mpf, a)); b = tuple(map(mp.mpf, b))
        w = max(w, rel(KLq(g(a), g(b)), KLc(a, b)))
verdict("F3", w < mp.mpf(10)**-40, f"KL unmoved by 7 real Möbius maps (scale the world among them), worst {mp.nstr(w, 3)}")

# F4
w = mp.mpf(0); sym = mp.mpf(0)
for r in [mp.mpf(x) for x in ('0.001', '0.5', '1', '2', '3', '1000')]:
    a, b = (mp.mpf(0), mp.mpf(1)), (mp.mpf(0), r)
    q = KLq(a, b); c = mp.log((1 + r)**2/(4*r))
    w = max(w, rel(q, c) if r != 1 else abs(q), abs(dP(a, b) - abs(mp.log(r))), abs(c + 2*mp.log(mp.sech(mp.log(r)/2))))
    sym = max(sym, abs(c - mp.log((1 + 1/r)**2/(4/r))))
verdict("F4", w < mp.mpf(10)**-40 and sym < mp.mpf(10)**-40,
        f"one foot: d = |ln r|, KL = ln((1+r)²/4r) = −2 ln sech(½ ln r), r ↔ 1/r, worst {mp.nstr(max(w, sym), 3)}")

# F5
ok = True; tail = mp.mpf(0); spot = mp.mpf(0)
ss = [mp.mpf(10)**(e/4) for e in range(-12, 13)]
for a, b in pairs[:4]:
    a = tuple(map(mp.mpf, a)); b = tuple(map(mp.mpf, b))
    prevK, prevd = KLc(a, b), dP(a, b)
    for s in ss:
        A, B = (a[0], a[1] + s), (b[0], b[1] + s)
        K, d = KLc(A, B), dP(A, B)
        ok = ok and K < prevK and d < prevd; prevK, prevd = K, d
    tail = max(tail, KLc((a[0], a[1] + 10**6), (b[0], b[1] + 10**6)))
    A, B = (a[0], a[1] + 1), (b[0], b[1] + 1); spot = max(spot, rel(KLq(A, B), KLc(A, B)))
verdict("F5", ok and tail < mp.mpf(10)**-6 and spot < mp.mpf(10)**-40,
        f"stepping back lowers KL and d at every step; KL at s = 10⁶ at most {mp.nstr(tail, 3)}; quadrature check {mp.nstr(spot, 3)}")

# F6
rng = np.random.default_rng(787); n, R = 1001, 20000
med = np.empty(R); mle = np.empty(R)
for i in range(R):
    x = np.tan(np.pi*(rng.random(n) - 0.5))
    m = np.median(x); med[i] = m
    for _ in range(30):
        u = x - m; s1 = np.sum(2*u/(1 + u*u)); s2 = np.sum(2*(1 - u*u)/(1 + u*u)**2)
        m = m + s1/s2
    mle[i] = m
vm, vl = n*med.var(), n*mle.var()
eff = mp.mpf(8)/pi**2
okf6 = abs(vm/(float(pi)**2/4) - 1) < 0.03 and abs(vl/2 - 1) < 0.03
verdict("F6", okf6, f"efficiency 8/π² = {mp.nstr(eff, 6)}; n·var(median) {vm:.4f} (π²/4 = {float(pi)**2/4:.4f}), "
        f"n·var(MLE) {vl:.4f} (2), ratio {vl/vm:.4f}")

# F7
w = max(abs(mp.quad(lambda g: mp.mpf(2)**(-j)/(2*g*g), [mp.mpf(2)**(-j-1), mp.mpf(2)**(-j)]) - mp.mpf(1)/2) for j in range(-3, 11))
verdict("F7", w < mp.mpf(10)**-40, f"every dyadic cell's Fisher area ½, j = −3 … 10, worst {mp.nstr(w, 3)}")
open('runs/frg/frg-run1.txt', 'w').write('\n'.join(out) + '\n')
