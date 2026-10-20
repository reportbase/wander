"""DYH run 2: the share of each level's detail a reader at height gamma keeps (plans/dyh-plan.md). Exact (mpmath)."""
import mpmath as mp
mp.mp.dps = 150
pi = mp.pi

def G(t, s):  # G'' = P_s, the Poisson kernel of height s
    return (t * mp.atan(t / s) - s / 2 * mp.log(t * t + s * s)) / pi

def box(a, b, c, d, s):  # the double integral of P_s(x - y) over [a, b] x [c, d]
    return G(b - c, s) - G(a - c, s) - G(b - d, s) + G(a - d, s)

def R_space(jp, k, gamma):  # Haar at level jp, index k, read from height gamma
    h = mp.mpf(2) ** (-jp - 1); a = k * 2 * h; c2 = mp.mpf(2) ** jp; s = 2 * gamma
    I = [(a, a + h, 1), (a + h, a + 2 * h, -1)]
    return c2 * sum(si * sj * box(p, q, r, t, s) for (p, q, si) in I for (r, t, sj) in I)

def R_H(u):
    return R_space(0, 0, mp.mpf(u))

def R_freq(u):  # numerical quadrature of 2 * int |psi_H^(eta)|^2 e^{-4 pi u eta}
    f = lambda e: 2 * mp.sin(pi * e / 2) ** 4 / (pi * e / 2) ** 2 * mp.exp(-4 * pi * u * e)
    top = int(min(6000, max(40, 80 / (4 * pi * u))))
    pts = list(range(0, top + 1, 2)) + [mp.inf]
    return mp.quad(f, pts)

def R_smooth(u, p):  # |psi^|^2 proportional to eta^p e^{-4 pi^2 eta^2}; p = 2 Gaussian derivative, 4 Mexican hat
    w = lambda e: e ** p * mp.exp(-4 * pi ** 2 * e * e)
    return mp.quad(lambda e: w(e) * mp.exp(-4 * pi * u * e), [0, 1, mp.inf]) / mp.quad(w, [0, 1, mp.inf])

ok = {}
# Q1
us = [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)]
worst = 0
for u in us:
    ref = R_H(u)
    for jp in (0, 3, 10, 30):
        for k in (0, 5):
            worst = max(worst, abs(R_space(jp, k, u * mp.mpf(2) ** (-jp)) - ref))
ok['Q1'] = worst < mp.mpf(10) ** -30
print('Q1 one variable: worst over levels and indices %s' % mp.nstr(worst, 3), ok['Q1'])
print('   R_H at u = 0.01, 0.1, 1, 10:', [mp.nstr(R_H(u), 12) for u in us])

# Q2
mp.mp.dps = 50
worst = 0
for u in us:
    worst = max(worst, abs(R_freq(u) - R_H(u)))
ok['Q2'] = worst < mp.mpf(10) ** -25
print('Q2 space against frequency: worst %s' % mp.nstr(worst, 3), ok['Q2'])

# Q3
grid = [mp.mpf(10) ** (e / mp.mpf(4)) for e in range(-32, 33)]
vals = [R_H(u) for u in grid]
mono = all(vals[i] > vals[i + 1] for i in range(len(vals) - 1)) and vals[0] > 1 - mp.mpf(10) ** -6 and vals[-1] < mp.mpf(10) ** -20
at = lambda r: mp.findroot(lambda lu: R_H(mp.e ** lu) - r, mp.log(0.05))
ustar = mp.e ** at(0.5); u9 = mp.e ** at(0.9); u1 = mp.e ** at(0.1)
width = mp.log(u1 / u9, 2)
ok['Q3'] = mono and 2 ** -6 <= ustar <= 2 ** -2 and R_H(0.5) < 0.5 and 2 <= width <= 10
print('Q3 monotone %s; half at u* = %s (log2 %s, so %s levels above the reader\'s own cell); R_H(1/2) = %s, R_H(1/4) = %s; 0.9 to 0.1 over %s levels'
      % (mono, mp.nstr(ustar, 6), mp.nstr(mp.log(ustar, 2), 4), mp.nstr(-mp.log(ustar, 2) - 1, 3), mp.nstr(R_H(0.5), 5), mp.nstr(R_H(0.25), 5), mp.nstr(width, 4)), ok['Q3'])
print('   by level, reader at its own cell J: j\' - J = ', ', '.join('%d: %s' % (d, mp.nstr(R_H(mp.mpf(2) ** (d - 1)), 4)) for d in range(-7, 3)))

# Q4
mp.mp.dps = 150
u = mp.mpf(10) ** -30
r4a = (1 - R_H(u)) / (u * mp.log(1 / u)) / (12 / pi)
r4b = R_H(mp.mpf(1000)) * mp.mpf(1000) ** 3 * 64 * pi
ok['Q4'] = abs(r4a - 1) < 0.05 and abs(r4b - 1) < 0.01
print('Q4 near: (1 - R)/(u ln 1/u) over 12/pi = %s; far: R u^3 over 1/(64 pi) = %s' % (mp.nstr(r4a, 8), mp.nstr(r4b, 8)), ok['Q4'])
for e in (-4, -8, -16, -30):
    uu = mp.mpf(10) ** e; print('   u = 1e%d: %s' % (e, mp.nstr((1 - R_H(uu)) / (uu * mp.log(1 / uu)) / (12 / pi), 8)))

# Q5
mp.mp.dps = 60
u = mp.mpf(10) ** -30
r5a = (1 - R_smooth(u, 2)) / u / (4 / mp.sqrt(pi))
r5b = R_smooth(mp.mpf(1000), 2) * mp.mpf(1000) ** 3 * mp.sqrt(pi)
slope = (mp.log(R_smooth(mp.mpf(1001), 4)) - mp.log(R_smooth(mp.mpf(999), 4))) / (mp.log(1001) - mp.log(999))
ok['Q5'] = abs(r5a - 1) < mp.mpf(10) ** -6 and abs(r5b - 1) < 0.01 and abs(slope + 5) < 0.05
print('Q5 smooth near: (1 - R_G)/u over 4/sqrt(pi) = %s; far: R_G u^3 over 1/sqrt(pi) = %s; Mexican hat slope %s' % (mp.nstr(r5a, 12), mp.nstr(r5b, 8), mp.nstr(slope, 6)), ok['Q5'])
# Gaussian derivative's half point, for the record (its width is its own convention)
mp.mp.dps = 30
ug = mp.e ** mp.findroot(lambda lu: R_smooth(mp.e ** lu, 2) - 0.5, mp.log(0.1))
u9g = mp.e ** mp.findroot(lambda lu: R_smooth(mp.e ** lu, 2) - 0.9, mp.log(0.01)); u1g = mp.e ** mp.findroot(lambda lu: R_smooth(mp.e ** lu, 2) - 0.1, mp.log(1))
print('   R_G half at u = %s (sigma = 1); 0.9 to 0.1 over %s levels' % (mp.nstr(ug, 6), mp.nstr(mp.log(u1g / u9g, 2), 4)))
ok['Q6'] = ok['Q1']  # the near tails differ in form by Q4, Q5: u ln(1/u) against u
print('Q6', all(ok.values()), ok)
