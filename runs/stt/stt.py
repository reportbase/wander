# STT run 1: Student's t between the Cauchy and the Gaussian. plans/stt-plan.md, predictions S1-S6.
import random
from fractions import Fraction as F
from mpmath import mp, mpf, gamma, sqrt, pi, exp, log, quad, sin, findroot, diff

mp.dps = 50
def f(nu, t):
    nu = mpf(nu); t = mpf(t)
    return gamma((nu + 1) / 2) / (sqrt(nu * pi) * gamma(nu / 2)) * (1 + t * t / nu) ** (-(nu + 1) / 2)
def phi(t): return exp(-mpf(t) ** 2 / 2) / sqrt(2 * pi)
ok = {}
def say(k, good, msg):
    ok[k] = ok.get(k, True) and bool(good)
    print(f"  {k} {'ok  ' if good else 'FAIL'} {msg}")

print("S1  nu = 1 against 1/(pi(1+t^2))")
for t in ["0", "0.5", "1", "3", "10"]:
    d = abs(f(1, t) - 1 / (pi * (1 + mpf(t) ** 2)))
    say("S1", d < mpf(10) ** -40, f"t = {t}: diff {mp.nstr(d, 3)}")

print("S2  no e at finite nu; e as the limit")
for nu in [1, 3, 5]:
    for t in [F(1, 2), F(2), F(7, 3)]:
        r = (1 + t * t / nu) ** (-(nu + 1) // 2)            # exact rational
        d = abs(f(nu, mpf(t.numerator) / t.denominator) / f(nu, 0) - mpf(r.numerator) / r.denominator)
        say("S2", d < mpf(10) ** -40, f"nu = {nu}, t = {t}: f/f(0) = {r}, diff {mp.nstr(d, 3)}")
for nu in [2, 4]:
    for t in [F(1, 2), F(2)]:
        r = (1 + t * t / nu) ** (-(nu + 1))                 # the square, exact rational
        d = abs((f(nu, mpf(t.numerator) / t.denominator) / f(nu, 0)) ** 2 - mpf(r.numerator) / r.denominator)
        say("S2", d < mpf(10) ** -40, f"nu = {nu}, t = {t}: (f/f(0))^2 = {r}, diff {mp.nstr(d, 3)}")
for t in [1, 2]:
    lim = mpf(t) ** 4 / 4 - mpf(t) ** 2 / 2
    row = []
    for nu in [10, 100, 1000, 10000]:
        gap = (log(f(nu, t) / f(nu, 0)) + mpf(t) ** 2 / 2) * nu
        row.append(gap)
    say("S2", abs(row[-1] - lim) < mpf("0.01") * max(1, abs(lim)) and abs(row[-1] - lim) < abs(row[0] - lim),
        f"t = {t}: gap*nu at 10, 100, 1e3, 1e4 = {[mp.nstr(x, 6) for x in row]} -> {mp.nstr(lim, 6)}")

print("S3  t is a direction in nu + 1 dimensions")
rng = random.Random(832)
worst = 0.0
for _ in range(1000):
    nu = rng.randint(1, 8)
    z = rng.gauss(0, 1); w = [rng.gauss(0, 1) for _ in range(nu)]
    t0 = z / (sum(x * x for x in w) / nu) ** 0.5
    for k in (1e-3, 7.0, 1e3):
        tk = (k * z) / (sum((k * x) ** 2 for x in w) / nu) ** 0.5
        worst = max(worst, abs(tk - t0) / max(1.0, abs(t0)))
say("S3", worst < 1e-12, f"1,000 draws scaled by 1e-3, 7, 1e3: largest relative change in t {worst:.2e}")
for nu in range(1, 7):
    a = quad(lambda t: f(nu, t), [-sqrt(nu), 0, sqrt(nu)])
    cap = quad(lambda x: sin(x) ** (nu - 1), [pi / 4, pi / 2, 3 * pi / 4]) / quad(lambda x: sin(x) ** (nu - 1), [0, pi / 2, pi])
    say("S3", abs(a - cap) < mpf(10) ** -30, f"nu = {nu}: P(|t| <= sqrt(nu)) = {mp.nstr(a, 12)}, cap share {mp.nstr(cap, 12)}, diff {mp.nstr(abs(a - cap), 3)}")
say("S3", abs(quad(lambda t: f(1, t), [-1, 0, 1]) - mpf(1) / 2) < mpf(10) ** -40, "nu = 1: P(|t| <= 1) = 1/2")

print("S4  pi by the parity of nu")
want = {1: 1 / pi, 3: 2 / (pi * sqrt(3)), 5: 8 / (3 * pi * sqrt(5)), 2: 1 / (2 * sqrt(2)), 4: mpf(3) / 8}
for nu in [1, 2, 3, 4, 5]:
    d = abs(f(nu, 0) - want[nu])
    say("S4", d < mpf(10) ** -40, f"nu = {nu}: f(0) = {mp.nstr(f(nu, 0), 15)}, diff {mp.nstr(d, 3)}")

print("S5  the Gaussian approached at 1/nu")
tstar = sqrt(3 - sqrt(6))
lim = abs(tstar ** 4 - 2 * tstar ** 2 - 1) * phi(tstar) / 4
print(f"  limit max|t^4 - 2t^2 - 1| phi/4 at t^2 = 3 - sqrt6: {mp.nstr(lim, 8)}")
for nu, band in [(10, 0.30), (100, 0.05), (1000, 0.01)]:
    best = mpf(0)
    for i in range(0, 801):
        t = mpf(i) / 100
        best = max(best, abs(f(nu, t) - phi(t)))
    prod = best * nu
    say("S5", abs(prod / lim - 1) < band, f"nu = {nu}: sup|f - phi| * nu = {mp.nstr(prod, 8)}, off {mp.nstr(100 * (prod / lim - 1), 4)}% (band {int(band * 100)}%)")

print("S6  the reading offered (divisor known by degrees): killed if S3 holds")
print(f"  S6 {'killed' if ok['S3'] else 'not killed'}: t is unmoved by scaling at every nu tried")
print()
for k in ["S1", "S2", "S3", "S4", "S5"]:
    print(f"{k}: {'not killed' if ok[k] else 'KILLED'}")
print(f"S6: {'killed' if ok['S3'] else 'not killed'}")
