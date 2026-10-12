"""MOT run 2: motion in unit relations, the corners and their kinds. See plans/mot-plan.md, "Run 2: predictions".

Rates of readings by the complex step (exact to rounding) or, for braking, in exact rationals. Each reader is handed a
counting math namespace, so the transcendental calls it makes are counted (sqrt is algebraic and allowed).
"""
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(13)

def dt(f, t=0.0, h=1e-30): return f(t + 1j*h).imag/h
def verdict(ok): return "not killed" if ok else "KILLED"

class Count:
    """the reader's maths: arithmetic and sqrt are free; every trig call is counted"""
    def __init__(self): self.calls = 0
    def sqrt(self, z): return np.sqrt(z)
    def _c(self, f, z): self.calls += 1; return f(z)
    def tan(self, z): return self._c(np.tan, z)
    def sin(self, z): return self._c(np.sin, z)
    def cos(self, z): return self._c(np.cos, z)

# ---------------------------------------------------------------- P8: ranging by three readers of k = b/d
b = 1.0; eps = 1e-4; ds = b*np.logspace(-2, 2, 200001)
k = b/ds; phi = np.arctan(k); u = np.minimum(k, 1/k); far = ds >= b
def worst(read_lo, read_hi):
    return np.maximum(np.abs(read_lo/ds - 1), np.abs(read_hi/ds - 1))
# (a) the angle, even in phi: d = b/tan(phi)
wa = worst(b/np.tan(phi - eps/2), b/np.tan(phi + eps/2))
# (b) the unit relation, capped at 1, one bit for the side: d = b/u past the corner, b*u inside it
lo, hi = np.clip(u - eps/2, 0, 1), np.clip(u + eps/2, 0, 1)
wb = worst(np.where(far, b/lo, b*hi), np.where(far, b/hi, b*lo))
# (c) the plain ratio, uncapped: d = b/k
wc = worst(b/(k - eps/2), b/(k + eps/2))
def sens(kind, d):
    if kind == 'a': p = np.arctan(b/d); return abs(dt(lambda t: np.log(b/np.tan(p + t))))
    if kind == 'b':
        if d >= b: uu = b/d; return abs(dt(lambda t: np.log(b/(uu + t))))
        uu = d/b; return abs(dt(lambda t: np.log(b*(uu + t))))
    kk = b/d; return abs(dt(lambda t: np.log(b/(kk + t))))
flip = {}
for kind in 'abc':
    flip[kind] = max(abs(sens(kind, d)/sens(kind, b*b/d) - 1) for d in b*np.logspace(-2, 2, 2001))
best_a, best_b = ds[np.argmin(wa)], ds[np.argmin(wb)]
rises_c = bool(np.all(np.diff(wc) > 0))
ok8 = abs(best_a/b - 1) <= 0.01 and abs(best_b/b - 1) <= 0.01 and flip['a'] <= 1e-12 and flip['b'] <= 1e-12 and rises_c
print(f"P8 least worst error: angle at d = {best_a:.5f} b, unit relation at d = {best_b:.5f} b; flip-alike to "
      f"{flip['a']:.1e}, {flip['b']:.1e} (plain ratio {flip['c']:.1e}, not alike); plain ratio rises throughout: {rises_c} ->",
      verdict(ok8))
for d0 in (0.01, 0.1, 0.5, 1, 2, 10, 100):
    i = np.argmin(abs(ds - d0*b))
    print(f"   d = {d0:>5} b: worst in half-steps: angle {wa[i]/(eps/2):9.3f}, unit relation {wb[i]/(eps/2):9.3f},"
          f" plain ratio {wc[i]/(eps/2):9.3f}")

# ---------------------------------------------------------------- P9: equal budgets, the Cauchy's lay and the in-place lay
N = 1000
def per_address(d):
    ea = (np.pi/(2*N))*sens('a', d)          # N addresses over 0..90 degrees of phi
    eb = (2/N)*sens('b', d)                  # N/2 addresses in u on each side of the corner
    return eb/ea
dd = b*np.logspace(-3, 3, 60001)
rat = np.array([per_address(d) for d in dd]); uu = np.minimum(b/dd, dd/b)
pred = 4/(np.pi*(1 + uu**2))                 # = 4 cos^2(arctan u)/pi
miss9 = np.max(np.abs(rat - pred))
def cross(lo, hi):
    for _ in range(200):
        mid = np.sqrt(lo*hi)
        if (per_address(lo) - 1)*(per_address(mid) - 1) <= 0: hi = mid
        else: lo = mid
    return np.sqrt(lo*hi)
us = np.sqrt(4/np.pi - 1); c_in, c_out = cross(0.1*b, b), cross(b, 10*b)
ok9 = miss9 <= 1e-12 and abs(c_in/(us*b) - 1) <= 1e-4 and abs(c_out/(b/us) - 1) <= 1e-4
print(f"P9 in-place over even turn against 4/(pi(1+u^2)): worst {miss9:.1e}; at the corner {per_address(b):.6f} "
      f"(2/pi = {2/np.pi:.6f}); at 10^3 b {per_address(1e3*b):.6f} (4/pi = {4/np.pi:.6f}); equal at d = {c_in:.6f} b and "
      f"{c_out:.6f} b (predicted {us:.6f}, {1/us:.6f}) ->", verdict(ok9))

# ---------------------------------------------------------------- P10: the catalogue
rows = []
# (A) time to contact, head-on, from two looks a tick apart
R, A_ = Count(), Count(); eA_r = eA_a = eA_lee = 0
for _ in range(1000):
    S = 10**rng.uniform(-2, 2); u_ = 10**rng.uniform(-2, 2); tick = 10**rng.uniform(-3, 0)
    tau2 = 10**rng.uniform(0, 3); d2 = tau2*u_*tick; d1 = d2 + u_*tick
    x1, x2 = S/d1, S/d2; th1, th2 = np.arctan(x1), np.arctan(x2)           # what each reader is given
    r_ = x1/(x2 - x1)                                                       # ratio reader, in ticks
    t1, t2 = A_.tan(th1), A_.tan(th2); a_ = t1/(t2 - t1)                    # angle reader, exact
    lee = th1/(th2 - th1)                                                   # angle reader with no call
    eA_r = max(eA_r, abs(r_/tau2 - 1)); eA_a = max(eA_a, abs(a_/tau2 - 1)); eA_lee = max(eA_lee, abs(lee/tau2 - 1))
rows.append(("A time to contact", eA_r, R.calls, eA_a, A_.calls, eA_lee))
# (B) stereo with parallel axes
R, A_ = Count(), Count(); eB_r = eB_a = 0
for _ in range(1000):
    Z = 10**rng.uniform(-1, 2); X = Z*rng.uniform(-3, 3); bb = Z*10**rng.uniform(-3, 1)
    qL, qR = (X + bb)/Z, (X - bb)/Z; aL, aR = np.arctan(qL), np.arctan(qR)
    Zr = 2*bb/(qL - qR); Xr = bb*(qL + qR)/(qL - qR)
    tL, tR = A_.tan(aL), A_.tan(aR); Za = 2*bb/(tL - tR); Xa = bb*(tL + tR)/(tL - tR)
    eB_r = max(eB_r, abs(Zr - Z)/Z, abs(Xr - X)/Z); eB_a = max(eB_a, abs(Za - Z)/Z, abs(Xa - X)/Z)
rows.append(("B stereo, parallel axes", eB_r, R.calls, eB_a, A_.calls, None))
# (C) closest approach, and (D) the collision test
def course(aim):
    d = 10**rng.uniform(-1, 2); S = d*10**rng.uniform(-2, 0.5)
    ax = rng.uniform(0, 2*np.pi)                                            # the reader's own axis, anywhere
    off = rng.uniform(-1, 1)                                                # the thing within 57 degrees of it
    r0 = d*np.array([np.cos(ax + off), np.sin(ax + off)])
    if aim: w = -10**rng.uniform(-1, 1)*r0/d
    else:
        while True:
            w = 10**rng.uniform(-1, 1)*rng.normal(size=2)
            tstar = -(r0 @ w)/(w @ w)
            if tstar > 0 and np.linalg.norm(r0 + w*tstar)/d > 1e-3: break
    c, s = np.cos(ax), np.sin(ax); Rm = np.array([[c, s], [-s, c]]); p, q = Rm @ r0, Rm @ w
    pos = lambda t: (p[0] + q[0]*t, p[1] + q[1]*t)
    x = lambda t: S/np.sqrt(pos(t)[0]**2 + pos(t)[1]**2)
    slope = lambda t: pos(t)[1]/pos(t)[0]
    th = lambda t: np.arctan(x(t)); beta = lambda t: np.arctan(slope(t))
    tstar = -(r0 @ w)/(w @ w); true = np.linalg.norm(r0 + w*tstar)/d
    return (x(0).real, dt(x), slope(0).real, dt(slope)), (th(0).real, dt(th), dt(beta)), true
def ratio_C(M, x, xd, q, qd):
    r = (qd/(1 + q*q))*(x/xd); return abs(r)/M.sqrt(1 + r*r), r
def angle_C(M, th, thd, bd):
    r = bd*M.sin(2*th)/(2*thd); return abs(r)/M.sqrt(1 + r*r), r
R, A_ = Count(), Count(); eC_r = eC_a = 0
for _ in range(1000):
    rr, aa, true = course(False)
    eC_r = max(eC_r, abs(ratio_C(R, *rr)[0] - true)); eC_a = max(eC_a, abs(angle_C(A_, *aa)[0] - true))
rows.append(("C closest approach (m/d)", eC_r, R.calls, eC_a, A_.calls, None))
R, A_ = Count(), Count(); wrongR = wrongA = 0
for i in range(1000):
    aim = i % 2 == 0; rr, aa, true = course(aim)
    r = ratio_C(R, *rr)[1]; wrongR += (abs(r) < 1e-9) != aim
    th, thd, bd = aa; wrongA += (abs(bd*th/thd) < 1e-9) != aim                 # bearing still, against Lee's tau
rows.append(("D collision test (misclassified)", wrongR, R.calls, wrongA, A_.calls, None))
print("P10 catalogue: ratio reader against the referee, its calls; angle reader, its calls:")
for name, er, cr, ea, ca, lee in rows:
    extra = f"; the angle reader with no call (Lee's): {lee:.3f}" if lee is not None else ""
    print(f"   {name:34s} ratio {er:.1e} ({cr} calls); angle {ea:.1e} ({ca} calls){extra}")
okABC = all(r[1] <= 1e-12 and r[2] == 0 and r[4] >= 1 for r in rows[:3]) and rows[3][1] == 0 and rows[3][3] == 0 \
    and rows[3][2] == 0 and rows[3][4] == 0
okAng = all(r[3] <= 1e-12 for r in rows[:3])      # the plan: the angle forms agree (to the same 1e-12) by calling
print(f"   the ratio forms exact with no call: {okABC}; the angle forms, with their calls, within 1e-12: {okAng}")
# post hoc, not a prediction: where the angle forms lose it. A double spaces the angle evenly near 90 degrees, so the
# ratio read back through tan has relative step ulp*(1 + x^2)/x: P8's angle reader with the step one ulp.
for x in (0.1, 1, 10, 1e3, 1e5):
    a = np.arctan(x)
    print(f"   post hoc: x = {x:g}: tan(arctan x)/x - 1 = {abs(np.tan(a)/x - 1):.1e}; ulp of the angle {np.spacing(a):.1e},"
          f" so x is held to {np.spacing(a)*(1 + x*x)/x:.1e}; the capped unit relation min(x, 1/x) to"
          f" {np.spacing(min(x, 1/x))/min(x, 1/x):.1e}")
# (F) steady turning
th0 = 0.3; steps = 10**4; okF = True
for delta in (0.1, 0.01, 0.001):
    A_, P = Count(), Count()
    th = th0; C, Sd = P.cos(delta), P.sin(delta)                          # two constants, once
    c, s = np.cos(th0), np.sin(th0); m = max(abs(c), abs(s)); c, s = c/m, s/m   # the capped pair
    werr_a = werr_p = 0; maxu = 0
    for n in range(1, steps + 1):
        th += delta
        c, s = C*c - Sd*s, Sd*c + C*s; m = max(abs(c), abs(s)); c, s = c/m, s/m
        maxu = max(maxu, min(abs(c), abs(s)))
        if n % 97 == 0 or n == steps:                                      # read a place now and then
            ref = np.array([np.cos(th0 + n*delta), np.sin(th0 + n*delta)])
            pa = np.array([A_.cos(th), A_.sin(th)]); L = P.sqrt(c*c + s*s); pp = np.array([c, s])/L
            werr_a = max(werr_a, np.max(abs(pa - ref))); werr_p = max(werr_p, np.max(abs(pp - ref)))
    reads = steps//97 + 1
    T = np.tan(delta); t = np.tan(th0); maxt = 0
    for n in range(int(np.ceil(2*np.pi/delta)) + 1):                       # one whole turn of the plain ratio
        t = (t + T)/(1 - T*t); maxt = max(maxt, abs(t))
    cot = 1/np.tan(delta/2)
    okF &= werr_a <= 1e-9 and werr_p <= 1e-9 and maxt >= cot*(1 - 1e-9) and maxu <= 1
    print(f"   F turning, step {delta:g}: angle {werr_a:.1e} ({A_.calls} calls for {reads} reads, 0 a step); capped pair"
          f" {werr_p:.1e} ({P.calls} calls, the 2 constants, 0 a step); its unit relation at most {maxu:.6f}; plain"
          f" ratio's largest {maxt:.4g} (cot of half a step {cot:.4g})")
print("P10 ->", verdict(okABC and okAng and okF))

# ---------------------------------------------------------------- P11: braking reads its corner, in exact rationals
def rat(lo, hi): return F(int(rng.integers(1, 10**6)), 10**6)*(F(hi) - F(lo)) + F(lo)
def tau_dot(S, d, u, a):
    """the world gives x and its rates at t = 0; the reader computes 1 - x*xdd/xd^2 with no call"""
    D, D1, D2 = d, -u, a                                                   # D(t) = d - u t + a t^2/2
    x = S/D; xd = -S*D1/D**2; xdd = S*(2*D1*D1 - D*D2)/D**3
    return 1 - x*xdd/(xd*xd)
bad_formula = bad_class = 0
for _ in range(10**4):
    S, d, u = rat(F(1, 100), 100), rat(F(1, 100), 100), rat(F(1, 100), 100)
    s = d*rat(F(1, 10), 10)                                                # stopping distance, 0.1 d to 10 d
    a = u*u/(2*s)
    td = tau_dot(S, d, u, a)
    bad_formula += td != -1 + d/(2*s)
    bad_class += (td > F(-1, 2)) != (s < d) or (td < F(-1, 2)) != (s > d)
bad_corner = 0
for _ in range(1000):
    S, d, u = rat(F(1, 100), 100), rat(F(1, 100), 100), rat(F(1, 100), 100)
    bad_corner += tau_dot(S, d, u, u*u/(2*d)) != F(-1, 2)
print(f"P11 tau-dot against -1 + d/2s: {bad_formula} of 10^4 off; classified wrongly by tau-dot against -1/2: {bad_class};"
      f" built at s = d and off -1/2: {bad_corner} of 1000 (exact rationals) ->",
      verdict(bad_formula == 0 and bad_class == 0 and bad_corner == 0))
# not a prediction: the same test read from the angle with no call, Lee's theta/thetadot, by how large the thing is
def lee_dot(S, d, u, a):
    D, D1, D2 = d, -u, a
    x = S/D; xd = -S*D1/D**2; xdd = S*(2*D1*D1 - D*D2)/D**3
    x, xd, xdd = float(x), float(xd), float(xdd)
    th = np.arctan(x); thd = xd/(1 + x*x); thdd = xdd/(1 + x*x) - 2*x*xd*xd/(1 + x*x)**2
    return 1 - th*thdd/(thd*thd)
for lo, hi in ((0.01, 0.1), (0.1, 1), (1, 10)):
    wrong = 0
    for _ in range(2000):
        d = F(1); S = F(10**rng.uniform(np.log10(lo), np.log10(hi))); u = F(1)
        s_ = F(10**rng.uniform(-1, 1)); a = u*u/(2*s_)
        wrong += (lee_dot(S, d, u, a) > -0.5) != (s_ < d)
    print(f"   not a prediction: braking judged from theta/thetadot with no call, S/d in [{lo:g}, {hi:g}): {wrong} of 2000"
          f" wrong (s/d log-even in [0.1, 10])")

# ---------------------------------------------------------------- P12: swap-symmetric quantities are stationary at the corner
M = Count()
sym = {"range of a launch, k/(1+k^2)": lambda k: k/(1 + k*k),
       "energy passed, 4k/(1+k)^2": lambda k: 4*k/((1 + k)*(1 + k)),
       "baseline conditioning, 2k/(1+k^2)": lambda k: 2*k/(1 + k*k)}
non = {"time of flight, k/sqrt(1+k^2)": lambda k: k/M.sqrt(1 + k*k),
       "greatest height, k^2/(1+k^2)": lambda k: k*k/(1 + k*k)}
ks = np.logspace(-3, 3, 6001); i1 = 3000; ok12 = True
for name, f in sym.items():
    fs = f(ks); swap = np.max(np.abs(fs/f(1/ks) - 1)); d1 = dt(f, 1.0); am = int(np.argmax(fs))
    ok12 &= swap <= 1e-12 and abs(d1) <= 1e-12 and am == i1
    print(f"   {name:38s} f(k)/f(1/k) - 1 at most {swap:.1e}; f'(1) = {d1:.1e}; greatest at k = {ks[am]:.4f}")
for name, f in non.items():
    fs = f(ks); inc = bool(np.all(np.diff(fs) > 0)); d1 = dt(f, 1.0)
    ok12 &= inc and d1 > 0
    print(f"   {name:38s} increasing throughout: {inc}; f'(1) = {d1:.4f}")
ok12 &= M.calls == 0
print(f"P12 calls: {M.calls} ->", verdict(ok12))
