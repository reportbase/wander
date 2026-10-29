# EUL run 1: the Cauchy and Euler's exponential, and what stops at the plane. Predictions in plans/eul-plan.md.
# Run from the repository's root: python3 runs/eul/eul.py
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
out = []
def say(s): print(s); out.append(s)

def verdict(name, ok, note=""):
    say(f"{name}: {'not killed' if ok else 'KILLED'} {note}")

# E1: E[e^{itX}] = e^{izt} (t>0), e^{i z̄ t} (t<0)
worst = mp.mpf(0)
for (m, g) in [(0, 1), (mp.mpf('0.7'), mp.mpf('0.3')), (-2, mp.mpf('2.5'))]:
    z = mp.mpc(m, g)
    for t in [mp.mpf('0.5'), 1, mp.mpf('2.3'), mp.mpf('-1.7')]:
        f = lambda x: mp.expj(t * x) * g / (pi * (g**2 + (x - m)**2))
        val = mp.quadosc(f, [-mp.inf, m], omega=abs(t)) + mp.quadosc(f, [m, mp.inf], omega=abs(t))
        exact = mp.expj(z * t) if t > 0 else mp.expj(mp.conj(z) * t)
        worst = max(worst, abs(val - exact))
say(f"E1 worst |E[e^(itX)] - e^(izt)| = {mp.nstr(worst, 5)}")
verdict("E1", worst < mp.mpf('1e-25'))

# E2: E[W^n] = w^n, W = (X-i)/(X+i), w = (z-i)/(z+i)
worst = mp.mpf(0)
for (m, g) in [(0, 1), (mp.mpf('0.7'), mp.mpf('0.3')), (-2, mp.mpf('2.5'))]:
    z = mp.mpc(m, g); w = (z - 1j) / (z + 1j)
    for n in range(1, 7):
        f = lambda ph: ((m + g * mp.tan(ph) - 1j) / (m + g * mp.tan(ph) + 1j))**n / pi
        val = mp.quad(f, [-pi/2, 0, pi/2])
        worst = max(worst, abs(val - w**n))
say(f"E2 worst |E[W^n] - w^n| = {mp.nstr(worst, 5)}")
verdict("E2", worst < mp.mpf('1e-25'))

# E3: theta uniform on [0, pi/2]: E[e^{2i theta}] = 2i/pi
val = mp.quad(lambda th: mp.expj(2 * th), [0, pi/2]) / (pi/2)
say(f"E3 E[e^(2i theta)] = {mp.nstr(val, 20)}, 2i/pi = {mp.nstr(2j/pi, 20)}, length {mp.nstr(abs(val), 20)}")
verdict("E3", abs(val - 2j/pi) < mp.mpf('1e-35'))

# E4: on the circle, Poisson kernel = Moebius image of uniform (wrapped Cauchy)
worst = mp.mpf(0)
for rho in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9')]:
    for k in range(200):
        a = 2 * pi * k / 200
        poisson = (1 - rho**2) / (2 * pi * (1 + rho**2 - 2 * rho * mp.cos(a)))
        # Moebius image of the uniform: uniform phi pushed by the disc automorphism u -> (u + rho)/(1 + rho u);
        # its density at e^{ia} is |d(phi)/d(a)| / (2 pi) with phi the preimage angle
        u = mp.expj(a); pre = (u - rho) / (1 - rho * u)
        dpre = (1 - rho**2) / (1 - rho * u)**2   # derivative of the inverse map
        moeb = abs(dpre) / (2 * pi)              # |dphi/da| = |d pre/du| on the circle
        worst = max(worst, abs(poisson - moeb))
say(f"E4 worst |Poisson - Moebius image| on the circle = {mp.nstr(worst, 5)}")
verdict("E4", worst < mp.mpf('1e-30'))

# E5: on S^2
def PH(r, t): return (1 - r**2) / (4 * pi * (1 + r**2 - 2 * r * t)**mp.mpf(1.5))
def PM(p, t): return (1 - p**2)**2 / (4 * pi * (1 + p**2 - 2 * p * t)**2)
def E(P, f): return mp.quad(lambda t: 2 * pi * P(t) * f(t), [-1, 1])
leg = lambda l: (lambda t: mp.legendre(l, t))
worst = mp.mpf(0)
for r in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('0.9')]:
    for l in range(0, 7):
        worst = max(worst, abs(E(lambda t: PH(r, t), leg(l)) - r**l))
say(f"E5a worst |E_H[P_l] - r^l| (l = 0..6) = {mp.nstr(worst, 5)}")
verdict("E5a", worst < mp.mpf('1e-25'))

ok_b = True; rows = []
for k in range(1, 10):
    p = mp.mpf(k) / 10
    f1 = E(lambda t: PM(p, t), leg(1)); f2 = E(lambda t: PM(p, t), leg(2)); f0 = E(lambda t: PM(p, t), leg(0))
    rows.append((p, f1, f2, f1**2))
    if not (f1 > p) or abs(f2 - f1**2) < mp.mpf('1e-20'): ok_b = False
    if abs(f0 - 1) > mp.mpf('1e-25'): ok_b = False
for p, f1, f2, f1s in rows:
    say(f"E5b rho {mp.nstr(p,2)}: E_M[t] = {mp.nstr(f1, 10)}  E_M[P2] = {mp.nstr(f2, 10)}  (E_M[t])^2 = {mp.nstr(f1s, 10)}")
# closed form guess check: 2 rho/(1+rho^2)
say("E5b E_M[t] against 2rho/(1+rho^2): " + ", ".join(mp.nstr(f1 - 2*p/(1+p**2), 3) for p, f1, _, _ in rows))
verdict("E5b", ok_b)

ts = [mp.mpf(-1) + 2 * mp.mpf(i) / 400 for i in range(401)]
def gap(Pa, Pb):
    peak = max(Pb(t) for t in ts)
    return max(abs(Pa(t) - Pb(t)) for t in ts) / peak
def best_r(target):
    f = lambda r: gap(lambda t: PH(r, t), target)
    lo, hi = mp.mpf('1e-6'), mp.mpf('0.999999')
    for _ in range(80):            # golden-section search over r
        a = hi - (hi - lo) / mp.phi; b = lo + (hi - lo) / mp.phi
        if f(a) < f(b): hi = b
        else: lo = a
    r = (lo + hi) / 2
    return r, f(r)
mp.mp.dps = 20
least = mp.inf
for k in range(1, 10):
    p = mp.mpf(k) / 10
    r, g = best_r(lambda t: PM(p, t))
    least = min(least, g)
    say(f"E5c rho {mp.nstr(p,2)}: best r {mp.nstr(r, 6)}, least sup gap {mp.nstr(g, 4)} of P_M's peak")
verdict("E5c", least > mp.mpf('1e-3'))

def boost(P, eta):
    b = mp.tanh(eta)
    return lambda tp: P((tp - b) / (1 - b * tp)) * (1 - b**2) / (1 - b * tp)**2
mp.mp.dps = 40
e1, e2 = mp.mpf('0.4'), mp.mpf('0.7')
B = boost(lambda t: PM(mp.tanh(e1 / 2), t), e2)
d_close = max(abs(B(t) - PM(mp.tanh((e1 + e2) / 2), t)) for t in ts)
say(f"E5d boosted spherical Cauchy against tanh((eta1+eta2)/2): worst {mp.nstr(d_close, 5)}")
mp.mp.dps = 20
BH = boost(lambda t: PH(mp.mpf('0.3'), t), mp.mpf('0.5'))
r, g = best_r(BH)
say(f"E5d boosted harmonic measure (r 0.3, eta 0.5): best r {mp.nstr(r, 6)}, least sup gap {mp.nstr(g, 4)}")
verdict("E5d", d_close < mp.mpf('1e-25') and g > mp.mpf('1e-3'))

# E6: a*L + b/(4 pi) against P_H
def L(r, t): return (1 - r * t) / (4 * pi * (1 + r**2 - 2 * r * t)**mp.mpf(1.5))
worst_fit = mp.inf
for r in [mp.mpf('0.3'), mp.mpf('0.7')]:
    A = mp.matrix([[L(r, t), 1 / (4 * pi)] for t in ts]); y = mp.matrix([PH(r, t) for t in ts])
    sol = mp.lu_solve(A.T * A, A.T * y)
    res = max(abs((A * sol)[i] - y[i]) for i in range(len(ts))) / max(y)
    worst_fit = min(worst_fit, res)
    say(f"E6 r {r}: best a {mp.nstr(sol[0], 6)}, b {mp.nstr(sol[1], 6)}, residual {mp.nstr(res, 4)} of the peak")
verdict("E6", worst_fit > mp.mpf('1e-6'))
open('runs/eul/eul-run1.txt', 'w').write('\n'.join(out) + '\n')
