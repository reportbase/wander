"""OMM stage 2, B5 (10 Oct 2026): the share with epoch, both ways. Flat matter + Lambda (w = -1), radiation left out.
Omega_m(z) = Om (1+z)^3 / (Om (1+z)^3 + 1 - Om).
(i)  every epoch's own home reads the same share: Omega_m(z) constant in z.
(ii) one reader's whole lay: 1/pi is Omega_m averaged over the reader's past, under a weight along the lay. Two weights:
     W1 even in look-back time; W2 even in comoving distance. For each, the Om (today) that makes the average 1/pi.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import sympy as sp

# (i) symbolic: d/dz Omega_m(z) = 0 for all z  <=>  Om = 0 or Om = 1  (with Lambda constant)
z, Om = sp.symbols('z Om', positive=True)
Omz = Om*(1+z)**3/(Om*(1+z)**3 + 1 - Om)
print("(i) dOmega_m/dz =", sp.factor(sp.diff(Omz, z)), " -> zero for all z only if Om = 0 or 1")
print("    constant share at 1/pi would need dark energy to thin as (1+z)^3, i.e. w = 0, against B2 (w = -1)")

def omz(zz, om): return om*(1+zz)**3/(om*(1+zz)**3 + 1 - om)
def E(zz, om): return np.sqrt(om*(1+zz)**3 + 1 - om)
def avg(om, w):
    f = (lambda zz: 1/((1+zz)*E(zz, om))) if w == 'time' else (lambda zz: 1/E(zz, om))
    num = quad(lambda zz: omz(zz, om)*f(zz), 0, np.inf, limit=400)[0]
    den = quad(f, 0, np.inf, limit=400)[0]
    return num/den
target = 1/np.pi
def DC(zz, om): return quad(lambda x: 1/E(x, om), 0, zz, limit=400)[0]      # comoving distance, units c/H0
def avg_lay(om):
    # W3, the lay's own weight with the corner at the Hubble radius (D = 1 in units c/H0, a candidate, not ruled):
    # true scale to the corner (weight dD), then even per doubling (weight dD/D), out to the particle horizon
    f = lambda zz: (1/E(zz, om)) * (1 if DC(zz, om) <= 1 else 1/DC(zz, om))
    zc = brentq(lambda zz: DC(zz, om) - 1, 1e-6, 50)
    num = quad(lambda zz: omz(zz, om)*f(zz), 0, zc, limit=200)[0] + quad(lambda zz: omz(zz, om)*f(zz), zc, 1e4, limit=400)[0]
    den = quad(f, 0, zc, limit=200)[0] + quad(f, zc, 1e4, limit=400)[0]
    return num/den
print("lay average of Omega_m(z), by today's Om:")
print("  Om      W1 time   W2 distance   W3 the lay (corner at c/H0)")
for om in (0.01, 0.05, 0.1, 0.2, 0.3, 1/np.pi, 0.4):
    print(f"  {om:.4f}  {avg(om,'time'):.4f}    {avg(om,'dist'):.4f}        {avg_lay(om):.4f}")
for name, fn in (('W1', lambda o: avg(o,'time')), ('W2', lambda o: avg(o,'dist')), ('W3', avg_lay)):
    lo, hi = 1e-3, 0.999
    if (fn(lo)-target)*(fn(hi)-target) < 0:
        print(f"{name}: average = 1/pi needs Omega_m today = {brentq(lambda o: fn(o)-target, lo, hi):.4f}")
    else:
        print(f"{name}: no Omega_m today in (0.001, 0.999) gives an average of 1/pi")
