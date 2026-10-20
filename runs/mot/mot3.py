"""MOT run 3: special relativity in unit relations. See plans/mot-plan.md, "Run 3: predictions".

v = beta and h = 1/gamma (the bridge from a speed is c); the celerity w = gamma*beta is their reading; the Doppler
factor k is a ratio of the reader's own intervals, its levels the rapidity. Rationals where the arithmetic is rational,
the complex step for rates.
"""
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(15)

def dt(f, t=0.0, h=1e-30): return f(t + 1j*h).imag/h
def verdict(ok): return "not killed" if ok else "KILLED"
kof = lambda b: np.sqrt((1 + b)/(1 - b))

# ---------------------------------------------------------------- P13: three pairs, three corners
bs = rng.uniform(-0.99, 0.99, 10**4)
e_a = np.max(abs(kof(bs)*kof(-bs) - 1))
b = 1/np.sqrt(2); g = 1/np.sqrt(1 - b*b); w = g*b; k = kof(b)
e_b = max(abs(w - 1), abs(k - (1 + np.sqrt(2))), abs(np.log(k) - np.arcsinh(1)))
def seen(theta, beta):
    """the moving observer's direction for a rest-frame direction theta, from the cosine form (not the half-angle)"""
    c = (np.cos(theta) + beta)/(1 + beta*np.cos(theta)); s = np.sin(theta)/(np.sqrt(1/(1 - beta*beta))*(1 + beta*np.cos(theta)))
    return np.arctan2(s, c)
e_c = 0
for beta in rng.uniform(-0.99, 0.99, 1000):
    th = 2*np.arctan(kof(beta))                          # tan(theta/2) = k
    e_c = max(e_c, abs(seen(th, beta) - np.pi/2))
th135 = 2*np.arctan(1 + np.sqrt(2)); fore = seen(np.pi/2, 1/np.sqrt(2))
e_c2 = max(abs(np.degrees(th135) - 135), abs(np.degrees(fore) - 45))
ok13 = e_a <= 1e-12 and e_b <= 1e-12 and e_c <= 1e-12 and e_c2 <= 1e-12
print(f"P13 (a) k(beta)k(-beta) - 1 at most {e_a:.1e}; (b) at beta = 1/sqrt 2: w, k against 1 + sqrt 2, zeta against "
      f"asinh 1, worst {e_b:.1e} (zeta = {np.log(k):.6f}); (c) tan(theta/2) = k is seen at 90 deg to {e_c:.1e} rad; at (b)'s"
      f" corner that direction is {np.degrees(th135):.12f} deg and the forward hemisphere is seen within"
      f" {np.degrees(fore):.12f} deg ->", verdict(ok13))

# ---------------------------------------------------------------- P14: gamma even, gamma*beta odd, in rationals
bad = 0; drawn = 0
while drawn < 10**4:
    k = F(int(rng.integers(1, 10**6)), int(rng.integers(1, 10**6)))
    if not F(1, 1000) <= k <= 1000: continue
    drawn += 1
    G = lambda q: (q + 1/q)/2; GB = lambda q: (q - 1/q)/2
    beta = (k*k - 1)/(k*k + 1); ig = 2*k/(1 + k*k)
    checks = [G(k) == G(1/k), GB(1/k) == -GB(k), k == G(k) + GB(k), 1/k == G(k) - GB(k),
              beta == GB(k)/G(k), ig == 1/G(k), beta*beta + ig*ig == 1]
    bad += not all(checks)
gam = lambda z: 1/np.sqrt(1 - ((np.exp(2*z) - 1)/(np.exp(2*z) + 1))**2)        # gamma from beta(zeta), not cosh
gb = lambda z: gam(z)*(np.exp(2*z) - 1)/(np.exp(2*z) + 1)
d_g, d_gb = dt(gam), dt(gb)
ok14 = bad == 0 and abs(d_g) <= 1e-12 and abs(d_gb - 1) <= 1e-12
print(f"P14 identities failing in rationals: {bad} of {drawn}; d gamma/d zeta at rest {d_g:.1e}; d(gamma beta)/d zeta"
      f" {d_gb:.15f} ->", verdict(ok14))

# ---------------------------------------------------------------- P15: rapidity against the reader's lay of celerity
def lay(w): return np.where(w <= 1, w, 1 + np.log(np.where(w > 1, w, 1)))
ws = np.logspace(-6, 6, 120001)
slope_gap = np.array([dt(lambda t: (w + t) - np.arcsinh(w + t)) if w < 1 else dt(lambda t: 1 + np.log(w + t)
                      - np.arcsinh(w + t)) for w in ws])
rising = bool(np.all(slope_gap > 0))
gap1 = 1 - np.arcsinh(1.0); gapfar = 1 + np.log(1e6) - np.arcsinh(1e6)
ok15 = rising and abs(gap1 - (1 - np.log(1 + np.sqrt(2)))) <= 1e-9 and abs(gapfar - (1 - np.log(2))) <= 1e-9
print(f"P15 the gap's slope positive throughout 1e-6..1e6: {rising}; gap at the corner {gap1:.6f} (1 - ln(1 + sqrt 2) ="
      f" {1 - np.log(1 + np.sqrt(2)):.6f}); at 1e6 {gapfar:.9f} (1 - ln 2 = {1 - np.log(2):.9f}); slopes at 1e-6:"
      f" {1:.0f} and {1/np.sqrt(1 + 1e-12):.12f}; at 1e6 times w: {1:.0f} and {1e6/np.sqrt(1 + 1e12):.12f} ->", verdict(ok15))

# ---------------------------------------------------------------- P16: pseudorapidity, a boost a pan in levels
e_pan = e_swap = e_m = 0
for _ in range(10**4):
    th = rng.uniform(0.05, np.pi - 0.05); beta = rng.uniform(-0.99, 0.99)
    c = (np.cos(th) + beta)/(1 + beta*np.cos(th)); s = np.sin(th)/(np.sqrt(1/(1 - beta*beta))*(1 + beta*np.cos(th)))
    t2 = s/(1 + c) if c >= 0 else (1 - c)/s                                  # tan of half the seen angle
    eta, eta2 = -np.log(np.tan(th/2)), -np.log(t2)
    e_pan = max(e_pan, abs((eta2 - eta) - np.log(kof(beta))))
    e_swap = max(e_swap, abs(-np.log(np.tan((np.pi - th)/2)) + eta))
    e_m = max(e_m, abs(0.5*np.log((1 + np.cos(th))/(1 - np.cos(th))) - eta))
ok16 = max(e_pan, e_swap, e_m) <= 1e-12
print(f"P16 eta' - eta against ln k: {e_pan:.1e}; fore-aft eta -> -eta: {e_swap:.1e}; massless rapidity against eta:"
      f" {e_m:.1e} (theta in 0.05..pi - 0.05) ->", verdict(ok16))

# ---------------------------------------------------------------- P17: the regime switch, the energy and the kinetic energy
xs = np.logspace(-3, 3, 6001)
sE = np.array([dt(lambda L: 0.5*np.log(np.exp(2*(np.log(x) + L)) + 1)) for x in xs])
sEf = np.array([dt(lambda L: 0.5*np.log(np.exp(2*(-np.log(x) + L)) + 1)) for x in xs])
def lnT(L, x):
    y = np.exp(np.log(x) + L); return np.log(y*y/(np.sqrt(1 + y*y) + 1))        # T/mc^2 = sqrt(1+x^2) - 1, stably
sT = np.array([dt(lambda L: lnT(L, x)) for x in xs]); sTf = np.array([dt(lambda L: lnT(L, 1/x)) for x in xs])
eE = np.max(abs(sE - xs**2/(1 + xs**2))); eflip = np.max(abs(sE + sEf - 1))
i1 = 3000; eT1 = abs(sT[i1] - (1 + 1/np.sqrt(2))); spread = np.max(sT + sTf) - np.min(sT + sTf)
ok17 = eE <= 1e-12 and eflip <= 1e-12 and eT1 <= 1e-12 and spread > 1e-6
print(f"P17 E's level-slope against beta^2: {eE:.1e}; s(x) + s(1/x) - 1: {eflip:.1e}; at the corner {sE[i1]:.15f}."
      f" T's level-slope at 1e-3, 1, 1e3: {sT[0]:.6f}, {sT[i1]:.15f}, {sT[-1]:.6f} (1 + 1/sqrt 2 = {1 + 1/np.sqrt(2):.15f});"
      f" T's swap sum from {np.min(sT + sTf):.6f} to {np.max(sT + sTf):.6f} ->", verdict(ok17))

# ---------------------------------------------------------------- P18: levels of motion under uniform proper acceleration
bad = 0; worst = 0
for n in range(0, 41):
    ch, sh = (F(2)**n + F(2)**-n)/2, (F(2)**n - F(2)**-n)/2                  # cosh, sinh of n ln 2, exactly
    x, t = ch - 1, sh                                                          # a = 1: the worldline at tau = n ln 2
    beta = sh/ch; k2 = (1 + beta)/(1 - beta)
    bad += (x + 1)**2 - t*t != 1                                               # hyperbolic motion, proper acceleration 1
    bad += k2 != F(4)**n                                                       # the Doppler factor is 2^n: level n
    bad += t != (F(2)**n - F(2)**-n)/2
    if n < 40:
        tn1 = (F(2)**(n + 1) - F(2)**-(n + 1))/2
        bad += tn1 - t != (F(2)**n + F(2)**(-n - 1))/2
    if n: worst = max(worst, abs(float(t)/np.sinh(n*np.log(2)) - 1))
D = lambda n: (F(2)**n + F(2)**(-n - 1))/2
r20 = D(20)/D(19)
ok18 = bad == 0 and worst <= 1e-12 and abs(float(r20) - 2) <= 1e-9
print(f"P18 inexact in rationals: {bad}; t_n against sinh(n ln 2): {worst:.1e}; launch-frame time per level, ratio to the"
      f" last: n = 1 {float(D(1)/D(0)):.4f}, 2 {float(D(2)/D(1)):.4f}, 5 {float(D(5)/D(4)):.6f}, 20 {float(r20):.12f};"
      f" proper time per level ln 2 = {np.log(2):.6f} ->", verdict(ok18))
