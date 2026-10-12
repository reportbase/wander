"""EMC: E^2 = (pc)^2 + (mc^2)^2 through the corner. See plans/emc-plan.md.

Rationals from Pythagorean triples where the state can be rational; floats and the complex step elsewhere. c is the
bridge that makes p and m into energies; v = pc/E and h = mc^2/E are the unit relations, x = pc/mc^2 their reading.
"""
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(16)
def verdict(ok): return "not killed" if ok else "KILLED"
C = 299792458.0                                                    # m/s

def state():
    """a rational state (pc, mc^2, E) from a Pythagorean triple, scaled; either leg may be the momentum's"""
    a, b = sorted(int(t) for t in rng.integers(1, 2000, 2))
    if a == b: b += 1
    legs = (F(b*b - a*a), F(2*a*b)); hyp = F(b*b + a*a)
    s = F(int(rng.integers(1, 10**6)), int(rng.integers(1, 10**6)))
    pc, mc2 = legs if rng.random() < 0.5 else legs[::-1]
    return pc*s, mc2*s, hyp*s

# ---------------------------------------------------------------- P1: the circle; beta from the speed; h the clock's rate
m = 9.1093837015e-31                                               # kg; any mass would do
worst = 0
for x in np.logspace(-3, 3, 6001):
    p = x*m*C
    E = lambda q: np.sqrt((q*C)**2 + (m*C*C)**2)
    hh = p*1e-20; u = E(p + 1j*hh).imag/hh                         # u = dE/dp, from E(p) alone
    worst = max(worst, abs((u/C)/(p*C/E(p).real) - 1))
bad = 0
for _ in range(10**4):
    pc, mc2, E_ = state()
    v, h = pc/E_, mc2/E_; beta = v
    bad += not (v*v + h*h == 1 and 1 - beta*beta == h*h and h > 0)
ok1 = worst <= 1e-12 and bad == 0
print(f"P1 u/c from dE/dp against pc/E: worst {worst:.1e} over 0.001..1000; rational states failing v^2 + h^2 = 1 or "
      f"1 - beta^2 = h^2: {bad} of 10^4 ->", verdict(ok1))

# ---------------------------------------------------------------- P2: the three landmarks
mc2 = 1.0
Eof = lambda x: mc2*np.sqrt(1 + x*x)
uof = lambda x: (Eof(x + 1j*1e-20*max(x, 1)).imag/(1e-20*max(x, 1)))   # beta = dE/d(pc) with c = 1 units of energy
home = Eof(0.0) == mc2
horizon = abs(np.sqrt((5.0)**2 + 0.0**2) - 5.0) == 0               # m = 0: E = pc
b1 = uof(1.0); E1 = Eof(1.0); T1 = E1 - mc2
e2 = max(abs(b1 - 1/np.sqrt(2)), abs(E1/np.sqrt(2) - 1), abs(T1/(np.sqrt(2) - 1) - 1))
for name, rest in (("electron", 0.51099895000), ("proton", 938.27208816)):
    T = np.sqrt(2*rest*rest) - rest; e2 = max(e2, abs(T/((np.sqrt(2) - 1)*rest) - 1))
    print(f"   {name}: rest {rest} MeV; at the corner pc = mc^2, beta = {uof(1.0):.12f}, T = {T:.7f} MeV")
ok2 = home and horizon and e2 <= 1e-12
print(f"P2 home E = mc^2: {home}; horizon E = pc: {horizon}; corner beta, E, T against 1/sqrt 2, sqrt 2 mc^2,"
      f" (sqrt 2 - 1)mc^2: worst {e2:.1e} ->", verdict(ok2))

# ---------------------------------------------------------------- P3: Newton and the ultra-relativistic form are flips
xs = np.logspace(-3, 3, 6001)
eN = lambda x: (1 + x*x/2)/np.sqrt(1 + x*x) - 1
eU = lambda x: (x + 1/(2*x))/np.sqrt(1 + x*x) - 1
flip = np.max(np.abs(eN(xs) - eU(1/xs))/np.maximum(1, np.abs(eN(xs))))
off = xs != 1.0
newton_better = np.abs(eN(xs)) < np.abs(eU(xs))
wrong = int(np.sum(newton_better[off] != (xs[off] < 1)))
corner = max(abs(eN(1.0) - (np.sqrt(9/8) - 1)), abs(eU(1.0) - (np.sqrt(9/8) - 1)))
ok3 = flip <= 1e-12 and wrong == 0 and corner <= 1e-12
print(f"P3 e_N(x) against e_U(1/x): worst {flip:.1e}; points where the better form is the wrong one: {wrong} of"
      f" {int(off.sum())}; at the corner both {eN(1.0):.7f} (sqrt(9/8) - 1 = {np.sqrt(9/8) - 1:.7f}) ->", verdict(ok3))
for x in (0.1, 0.5, 1, 2, 10):
    print(f"   x = {x:>4}: Newton {eN(x):+.6f}, ultra-relativistic {eU(x):+.6f}")

# ---------------------------------------------------------------- P4: mass is the light-cone pair's corner
def boost(E, pc, kb):
    bb = (kb*kb - 1)/(kb*kb + 1); gb = (kb*kb + 1)/(2*kb)        # rational when kb is
    return gb*(E - bb*pc), gb*(pc - bb*E)                          # the Lorentz transformation of (E, pc)
bad = below = shares_moved = 0
for _ in range(10**4):
    pc, mc2r, E_ = state()
    kb = F(int(rng.integers(1, 10**4)), int(rng.integers(1, 10**4)))
    E2, pc2 = boost(E_, pc, kb)
    checks = [E2 + pc2 == (E_ + pc)/kb, E2 - pc2 == kb*(E_ - pc), (E2 + pc2)*(E2 - pc2) == mc2r*mc2r,
              E2*E2 - pc2*pc2 == mc2r*mc2r]
    k2 = F(int(rng.integers(1, 10**4)), int(rng.integers(1, 10**4)))
    checks.append(boost(*boost(E_, pc, kb), k2) == boost(E_, pc, kb*k2))
    bad += not all(checks)
    below += E2 < mc2r
    shares_moved += (pc2/E2 != pc/E_) == (kb != 1)
rest_bad = 0
for _ in range(1000):
    pc, mc2r, E_ = state()
    E2, pc2 = boost(E_, pc, (E_ + pc)/mc2r)
    rest_bad += not (E2 == mc2r and pc2 == 0)
ok4 = bad == 0 and below == 0 and rest_bad == 0
print(f"P4 rational states and boosts with an identity failing: {bad} of 10^4; E' below mc^2: {below}; the circle's share"
      f" v moved exactly when the boost was not 1: {shares_moved} of 10^4; boosts by (E + pc)/mc^2 not landing at rest"
      f" (E' = mc^2, p' = 0): {rest_bad} of 1000 ->", verdict(ok4))
