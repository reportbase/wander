"""PAY: what arrives of the payload, serially and at once. See plans/pay-plan.md.

Rationals where the numbers are rational (P4 c); floats with the complex step elsewhere.
"""
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(17)
def verdict(ok): return "not killed" if ok else "KILLED"
def dt(f, t=0.0, h=1e-30): return f(t + 1j*h).imag/h

# ---------------------------------------------------------------- P1: one stream, approach or growth
worst = worst_tau = 0
for _ in range(1000):
    S, d0, u = 10**rng.uniform(-2, 2, 3)
    T = 0.9*d0/u; ts = np.linspace(0, T, 201)
    xa = lambda t: S/(d0 - u*t)                                    # rigid, approaching
    Sg = lambda t: S*d0/(d0 - u*t); xb = lambda t: Sg(t)/d0        # at rest, growing
    worst = max(worst, np.max(abs(xa(ts)/xb(ts) - 1)))
    for t in ts[::50]:
        worst_tau = max(worst_tau, abs((xa(t)/dt(xa, t))/(xb(t)/dt(xb, t)) - 1))
ok1 = worst <= 1e-12 and worst_tau <= 1e-12
print(f"P1 approach against growth: streams apart by at most {worst:.1e}, their x/xdot by {worst_tau:.1e} ->", verdict(ok1))

# ---------------------------------------------------------------- P2: a second reading at once, sharing the denominator
same_drift = grow_miss = 0; other_min_drift = np.inf
for _ in range(1000):
    S1, S2, d0, u = 10**rng.uniform(-2, 2, 4)
    d2 = d0*10.0**(rng.choice([-1, 1])*rng.uniform(0.1, 1))          # another depth, 10^0.1 to 10 times nearer or farther
    ts = np.linspace(0, 0.9*min(d0, d2)/u, 201)
    r_app = (S1/(d0 - u*ts))/(S2/(d0 - u*ts))                       # both approached by the observer's motion
    same_drift = max(same_drift, np.max(abs(r_app/r_app[0] - 1)))
    S1t = S1*d0/(d0 - u*ts); r_grow = (S1t/d0)/(S2/d0)              # the thing grows, the neighbour does not
    grow_miss = max(grow_miss, np.max(abs((r_grow/r_grow[0])/(S1t/S1) - 1)))
    r_other = (S1/(d0 - u*ts))/(S2/(d2 - u*ts))
    other_min_drift = min(other_min_drift, np.max(abs(r_other/r_other[0] - 1)))
ok2 = same_drift <= 1e-12 and grow_miss <= 1e-12 and other_min_drift > 1e-6
print(f"P2 same depth: drift under approach {same_drift:.1e}; under growth the ratio against S1(t)/S1(0) {grow_miss:.1e};"
      f" another depth: the least drift under approach {other_min_drift:.3f} ->", verdict(ok2))

# ---------------------------------------------------------------- P3: below the step, the payload's moments
def blend(L1, L2, x1, x2, sig, xs):
    G = lambda y: np.exp(-0.5*(y/sig)**2)/(sig*np.sqrt(2*np.pi))
    return L1*G(xs - x1) + L2*G(xs - x2)
e_a = e_b = 0
for _ in range(1000):
    L1, L2 = 10**rng.uniform(-1, 1, 2); sig = 1.0; s = 10**rng.uniform(-2, 1); x1 = rng.uniform(-1, 1); x2 = x1 + s
    beta = L2/(L1 + L2)
    xs = np.arange(min(x1, x2) - 14*sig, max(x1, x2) + 14*sig, sig/40)
    f = blend(L1, L2, x1, x2, sig, xs)
    m0 = f.sum(); c1 = (f*xs).sum()/m0; m2 = (f*(xs - c1)**2).sum()/m0
    e_a = max(e_a, abs(c1 - (L1*x1 + L2*x2)/(L1 + L2))/sig)
    e_b = max(e_b, abs(m2/(sig**2 + beta*(1 - beta)*s*s) - 1))
def two_peaks(s, sig=1.0, h=1e-3):
    f = lambda x: blend(1.0, 1.0, -s/2, s/2, sig, np.array([x]))[0]
    return f(h) + f(-h) - 2*f(0.0) > 0                              # a dip at the middle
lo, hi = 1.9, 2.1
for _ in range(60):
    mid = (lo + hi)/2
    if two_peaks(mid): hi = mid
    else: lo = mid
sparrow = (lo + hi)/2
# (d) the binary: photocentre against barycentre
a = 1.0; ph = np.linspace(0, 2*np.pi, 721)
n = np.c_[np.cos(ph), np.sin(ph)]
def photo(B, beta):
    r1, r2 = -B*a*n, (1 - B)*a*n                                     # about the barycentre (B = M2/(M1 + M2))
    return (1 - beta)*r1 + beta*r2
e_deg = 0; e_size = 0; e_rec = 0
for _ in range(1000):
    B, beta = rng.uniform(0.05, 0.95, 2); dlt = rng.uniform(-0.04, 0.04)
    B2, beta2 = B + dlt, beta + dlt                                   # the same B - beta
    if not (0 < B2 < 1 and 0 < beta2 < 1): continue
    e_deg = max(e_deg, np.max(abs(photo(B, beta) - photo(B2, beta2))))
    e_size = max(e_size, abs(np.max(np.linalg.norm(photo(B, beta), axis=1)) - a*abs(B - beta)))
    r1, r2 = -B*a*n, (1 - B)*a*n; L1, L2 = 1 - beta, beta              # resolved: each star read against the background
    a1, a2 = np.max(np.linalg.norm(r1, axis=1)), np.max(np.linalg.norm(r2, axis=1))
    e_rec = max(e_rec, abs(a1/(a1 + a2) - B), abs(L2/(L1 + L2) - beta))
ok3 = e_a <= 1e-9 and e_b <= 1e-9 and abs(sparrow - 2) <= 1e-6 and e_deg <= 1e-12 and e_rec <= 1e-12
print(f"P3 (a) first moment against the photocentre {e_a:.1e} of sigma; (b) second against sigma^2 + beta(1 - beta)s^2"
      f" {e_b:.1e}; (c) two maxima from s = {sparrow:.7f} sigma; (d) equal B - beta, photocentre streams apart by"
      f" {e_deg:.1e}, orbit size against a|B - beta| {e_size:.1e}; resolved, B = a1/a and beta recovered to {e_rec:.1e}"
      f" ->", verdict(ok3))
for s in (0.1, 0.5, 1, 2, 4):
    print(f"   s = {s} sigma, beta = 1/2: the payload's share of the second moment beta(1 - beta)(s/sigma)^2 = {0.25*s*s:.4f}")

# ---------------------------------------------------------------- P4: multipoles, the corner, Kelvin's flip
def ball(nm):
    r = rng.uniform(0, 1, nm)**(1/3); v = rng.normal(size=(nm, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    return v*r[:, None], rng.uniform(0.1, 1, nm)
P, m = ball(20); M = m.sum(); cm = (m[:, None]*P).sum(0)/M
dirs = rng.normal(size=(200, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
rs = np.logspace(2, 3, 21)
def rms_err(centre):
    out = []
    for r in rs:
        pts = dirs*r
        true = (m[None, :]/np.linalg.norm(pts[:, None, :] - P[None, :, :], axis=2)).sum(1)
        mono = M/np.linalg.norm(pts - centre, axis=1)
        out.append(np.sqrt(np.mean(((mono - true)/true)**2)))
    return np.polyfit(np.log2(rs), np.log2(out), 1)[0]
off = cm + 0.3*np.array([1.0, 0, 0])
sl_cm, sl_off = rms_err(cm), rms_err(off)
# (b) one mass at rho: the series inside and outside the corner
def legendre(L, c):
    p = [np.ones_like(c), c]
    for l in range(1, L): p.append(((2*l + 1)*c*p[l] - l*p[l - 1])/(l + 1))
    return np.array(p)
conv_out = div_in = 0
for _ in range(1000):
    rho = 1.0; cg = rng.uniform(-1, 1)
    for ratio in (1.1, 0.9):
        r = ratio*rho; true = 1/np.sqrt(r*r + rho*rho - 2*r*rho*cg)
        Pl = legendre(200, np.array(cg)); terms = np.array([rho**l/r**(l + 1) for l in range(201)])*Pl
        err = abs(terms.sum() - true)/true
        if ratio > 1: conv_out += err < 1e-6
        else: div_in += err > 1
corner_terms = [F(1)**l/F(1)**(l + 1) for l in range(31)]          # rho = r = 1, gamma = 0: P_l(1) = 1
ok_corner = all(t == 1 for t in corner_terms)
# (c) Kelvin's inversion, term by term, in rationals
def legendre_q(L, c):
    p = [F(1), c]
    for l in range(1, L): p.append(((2*l + 1)*c*p[l] - l*p[l - 1])/(l + 1))
    return p
bad_k = 0
for _ in range(300):
    rho = F(int(rng.integers(1, 100)), int(rng.integers(1, 100))); r = F(int(rng.integers(1, 100)), int(rng.integers(1, 100)))
    c = F(int(rng.integers(-99, 100)), 100); Pq = legendre_q(30, c)
    for l in range(31):
        inner = lambda rr: rr**l/rho**(l + 1)*Pq[l]
        bad_k += (rho/r)*inner(rho*rho/r) != rho**l/r**(l + 1)*Pq[l]
e_self = 0
for _ in range(1000):
    rho = 10**rng.uniform(-1, 1); sp = rng.normal(size=3); sp *= rho/np.linalg.norm(sp)   # a source on the sphere
    x = rng.normal(size=3)*10**rng.uniform(-1, 1); rx = np.linalg.norm(x)
    f = lambda y: 1/np.linalg.norm(y - sp)
    e_self = max(e_self, abs((rho/rx)*f(rho*rho*x/rx**2)/f(x) - 1))
# (d) orders needed against the bound
eps = 1e-6; broken = 0; tight = []
for _ in range(1000):
    P, m = ball(int(rng.integers(2, 30))); M = m.sum()
    q = rng.choice([1/1.05, 1/1.2, 1/1.5, 1/2, 1/4, 1/10]); r = 1/q
    d = rng.normal(size=3); d /= np.linalg.norm(d); pt = d*r
    true = (m/np.linalg.norm(pt - P, axis=1)).sum()
    rho = np.linalg.norm(P, axis=1); cg = (P @ d)/np.where(rho > 0, rho, 1)
    Lmax = 400; Pl = legendre(Lmax, cg)                               # shape (Lmax+1, n)
    terms = ((m[None, :]/r)*(rho[None, :]/r)**np.arange(Lmax + 1)[:, None]*Pl).sum(1)    # m rho^l / r^(l+1) P_l
    part = np.cumsum(terms); errs = abs(part - true)/(M/r)
    need = int(np.argmax(errs <= eps)) if (errs <= eps).any() else Lmax + 1      # never reached: counts as broken
    bound = np.log(eps*(1 - q))/np.log(q) - 1
    broken += need > bound; tight.append((r, need, bound))
ok4 = abs(sl_cm + 2) <= 0.02 and abs(sl_off + 1) <= 0.02 and conv_out == 1000 and div_in == 1000 and ok_corner \
    and bad_k == 0 and e_self <= 1e-12 and broken == 0
print(f"P4 (a) slopes in levels, 100 R to 1,000 R: about the centre of mass {sl_cm:.4f}, about a centre 0.3 R off"
      f" {sl_off:.4f}; (b) outside (r = 1.1 rho) converged {conv_out}/1000, inside (0.9 rho) failed {div_in}/1000, at the"
      f" corner every term 1/r: {ok_corner}; (c) Kelvin term by term inexact: {bad_k} of 300 x 31; a source on the sphere"
      f" its own image to {e_self:.1e}; (d) orders needed above the bound: {broken} of 1000 ->", verdict(ok4))
for rr in (1.05, 1.2, 1.5, 2, 4, 10):
    sel = [t for t in tight if abs(t[0] - rr) < 1e-9]
    if sel: print(f"   r = {rr} R: orders needed for 1e-6 at most {max(t[1] for t in sel)}, bound {sel[0][2]:.1f}")
