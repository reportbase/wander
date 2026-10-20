"""MOT: motion and tracking from inside. See plans/mot-plan.md.

Exact where it can be (fractions); derivatives of readings by the complex step, exact to rounding, so no reading's
derivative is taken from its formula. Amounts: S (half-size), d (distance), u (closing speed), B (breadth), the tick.
Readings: x = S/d, the turn arctan x, the bearing, the convergence.
"""
from fractions import Fraction as F
import numpy as np
rng = np.random.default_rng(12)

def dt(f, t=0.0, h=1e-30):
    """d f/dt at t by the complex step: f must be analytic; no subtraction, so exact to rounding."""
    return f(t + 1j*h).imag/h

def verdict(ok): return "not killed" if ok else "KILLED"

# P1: tau = x/xdot is d/u, before and past the corner
xs = np.logspace(-3, 3, 601); worst = 0
for x0 in xs:
    S = 10**rng.uniform(-2, 2); d = S/x0; u = 10**rng.uniform(-2, 2)
    x = lambda t: S/(d - u*t)
    tau = x(0).real/dt(x)
    worst = max(worst, abs(tau/(d/u) - 1))
print(f"P1 tau = x/xdot against d/u, 0.001 <= x <= 1000: worst {worst:.1e} ->", verdict(worst <= 1e-12))

# P2: tau read from the turn, theta/thetadot = (d/u)*arctan(x)(1+x^2)/x
fac = lambda x: np.arctan(x)*(1 + x*x)/x
worst = 0; meas = []
for x0 in xs:
    S = 10**rng.uniform(-2, 2); d = S/x0; u = 10**rng.uniform(-2, 2)
    th = lambda t: np.arctan(S/(d - u*t))
    r = th(0).real/dt(th)/(d/u); meas.append(r)
    worst = max(worst, abs(r/fac(x0) - 1))
meas = np.array(meas); inc = bool(np.all(np.diff(meas) > 0))
at1 = abs(fac(1.0) - np.pi/2)
print(f"P2 turn's factor against arctan(x)(1+x^2)/x: worst {worst:.1e}; at the corner {fac(1.0):.15f} "
      f"(pi/2 off by {at1:.1e}); increasing: {inc} ->", verdict(at1 <= 1e-12 and inc and worst <= 1e-12))
print("   factor at x = 0.001, 0.1, 1, 10, 1000:", ", ".join(f"{fac(x):.6g}" for x in (1e-3, 0.1, 1, 10, 1e3)))

# P3: two looks a tick apart, exact in rationals
def rat(lo, hi): return F(int(rng.integers(1, 10**6)), 10**6)*(F(hi) - F(lo)) + F(lo)
bad_old = bad_new = 0; worst_old = worst_new = F(0); taus = []
for _ in range(10**4):
    S = rat(F(1, 100), 100); tick = rat(F(1, 1000), 1); u = rat(F(1, 100), 100)
    tau2 = rat(1, 10**4)                                # ticks left at the second look
    d2 = tau2*u*tick; d1 = d2 + u*tick
    x1, x2 = S/d1, S/d2
    old = x1/(x2 - x1); new = x2/(x2 - x1)
    worst_old = max(worst_old, abs(old - tau2)/tau2); worst_new = max(worst_new, abs(new - (tau2 + 1))/tau2)
    taus.append(float(tau2))
print(f"P3 x1/(x2-x1) against tau at the second look: worst {float(worst_old):.1e}; x2/(x2-x1) against tau + 1 tick:"
      f" worst {float(worst_new):.1e} (10^4 approaches, tau from {min(taus):.2f} to {max(taus):.0f} ticks) ->",
      verdict(worst_old <= F(1, 10**9) and worst_new <= F(1, 10**9)))

# P4: holding the corner. H set to keep the thing at its corner is H proportional to x; d ln H/dt = 1/tau.
worst = 0
for _ in range(10**4):
    S = 10**rng.uniform(-2, 2); d = 10**rng.uniform(-2, 2); u = 10**rng.uniform(-2, 2); k = 10**rng.uniform(-3, 3)
    lnH = lambda t: np.log(k*S/(d - u*t))
    worst = max(worst, abs(dt(lnH)*(d/u) - 1))
ok_rate = worst <= 1e-12
# the levels: the reading doubles each level; time per level, exactly
bad_halve = 0; worst_sum = F(0); bad_half_tau = 0
for _ in range(1000):
    d0 = rat(F(1, 100), 100); u = rat(F(1, 100), 100); N = 60
    t = [(d0 - d0/2**k)/u for k in range(N + 1)]        # time the reading reaches 2^k times its first
    per = [t[k + 1] - t[k] for k in range(N)]
    bad_halve += sum(per[k + 1] != per[k]/2 for k in range(N - 1))
    bad_half_tau += sum(per[k] != (d0/2**k/u)/2 for k in range(N))   # each level: half the tau read at its start
    worst_sum = max(worst_sum, abs(sum(per) - d0/u)/(d0/u))
print(f"P4 d ln H/dt against 1/tau: worst {worst:.1e}; levels not halving: {bad_halve}; level not half the tau at its"
      f" start: {bad_half_tau}; 60 levels short of d0/u by {float(worst_sum):.1e} (= 2^-60) ->",
      verdict(ok_rate and bad_halve == 0 and worst_sum <= F(1, 10**12)))

# P5: bearing rate and tau give the closest approach as a share of the present distance
def course(r0, w):
    """readings at t = 0 in a frame turned so the thing is at bearing 0 (the bearing's zero is the reader's choice)"""
    c, s = r0/np.linalg.norm(r0)
    R = np.array([[c, s], [-s, c]]); p, q = R @ r0, R @ w
    S = 0.37
    bearing = lambda t: np.arctan((p[1] + q[1]*t)/(p[0] + q[0]*t))
    x = lambda t: S/np.sqrt((p[0] + q[0]*t)**2 + (p[1] + q[1]*t)**2)
    return dt(bearing), x(0).real/dt(x)
worst = 0
for _ in range(10**4):
    d = 10**rng.uniform(-1, 2); a = rng.uniform(0, 2*np.pi); r0 = d*np.array([np.cos(a), np.sin(a)])
    while True:
        w = 10**rng.uniform(-1, 1)*rng.normal(size=2)
        if r0 @ w < 0: break                             # approaching
    om, tau = course(r0, w)
    pred = d*abs(om*tau)/np.sqrt(1 + (om*tau)**2)
    tstar = -(r0 @ w)/(w @ w); true = np.linalg.norm(r0 + w*tstar)
    worst = max(worst, abs(pred - true)/d)
worst0 = 0
for _ in range(10**4):
    d = 10**rng.uniform(-1, 2); a = rng.uniform(0, 2*np.pi); r0 = d*np.array([np.cos(a), np.sin(a)])
    w = -10**rng.uniform(-1, 1)*r0/d                     # aimed at the reader
    om, tau = course(r0, w)
    tstar = -(r0 @ w)/(w @ w); worst0 = max(worst0, abs(om*tau), np.linalg.norm(r0 + w*tstar)/d)
om, tau = course(np.array([3.0, 0.0]), np.array([-1.0, 1.0]))  # tangential = radial: omega*tau = 1
print(f"P5 closest approach from omega*tau against the course: worst {worst:.1e} of d; bearing still: omega*tau and"
      f" miss at most {worst0:.1e}; at omega*tau = {om*tau:.15f} the pass is {abs(om*tau)/np.sqrt(1 + (om*tau)**2):.15f}"
      f" of d (1/sqrt 2 = {1/np.sqrt(2):.15f}) ->", verdict(worst <= 1e-9 and worst0 <= 1e-9))

# P6: the reader's breadth as a baseline
B = 1.0; eps = 1e-3
gam = lambda d: 2*np.arctan(B/(2*d)); dist = lambda g: (B/2)/np.tan(g/2)
ex = max(abs(dist(gam(d))/d - 1) for d in np.logspace(-2, 4, 601))
print(f"P6 d = (B/2)/tan(gamma/2), 0.01 <= d/B <= 10^4: worst {ex:.1e}")
rows = []; worst_dev = 0; first_bad = None
for e_d in np.logspace(np.log10(0.01), np.log10(0.2), 400):
    d = e_d*B/eps; g = gam(d)
    far = dist(g - eps/2)/d - 1; near = 1 - dist(g + eps/2)/d   # gamma read up to half a step low or high
    worst_ = max(far, near); pred = eps*d/(2*B); dev = worst_/pred - 1
    if abs(dev) > 0.1 and first_bad is None: first_bad = e_d
    worst_dev = max(worst_dev, abs(dev)); rows.append((e_d, pred, far, near))
# the same with a fixed grid of steps and d swept finely, so the worst is found, not assumed
def swept(e_d):
    g0 = gam(e_d*B/eps); ds = dist(np.linspace(g0 - eps, g0 + eps, 20001))   # two whole steps of gamma
    g = np.round(gam(ds)/eps)*eps
    return np.max(np.abs(dist(g)/ds - 1)/(eps*ds/(2*B)))
for e_d, pred, far, near in rows[::133][:3] + [rows[-1]]:
    print(f"   eps*d/B = {e_d:.3f}: eps*d/2B = {pred:.4f}; far side {far:.4f} ({far/pred:.3f} of it), near side"
          f" {near:.4f} ({near/pred:.3f}); fixed grid swept {swept(e_d):.3f} of it")
x = lambda e_d: e_d/2
print(f"   worst against eps*d/2B: up to {worst_dev:.3f} off; first past 10% at eps*d/B = "
      f"{first_bad if first_bad is None else round(first_bad, 3)} ->", verdict(first_bad is None))
print(f"   far side against x/(1-x), x = eps*d/2B: worst "
      f"{max(abs(far/(x(e)/(1 - x(e))) - 1) for e, _, far, _ in rows):.1e}; near against x/(1+x): "
      f"{max(abs(near/(x(e)/(1 + x(e))) - 1) for e, _, _, near in rows):.1e}")

# P7: the baseline reads best at its corner
worst_sin = 0; worst_flip = 0
for d in np.logspace(-2, 2, 4001):
    g = gam(d)
    lnd = lambda t: np.log((B/2)/np.tan((g + t)/2))
    s = abs(dt(lnd)); worst_sin = max(worst_sin, abs(s*np.sin(g) - 1))
    df = (B/2)**2/d; gf = gam(df)
    sf = abs(dt(lambda t: np.log((B/2)/np.tan((gf + t)/2))))
    worst_flip = max(worst_flip, abs(sf/s - 1))
eps7 = 1e-4; ds = np.logspace(-2, 2, 200001)*B; g = gam(ds)
w7 = np.maximum(dist(g - eps7/2)/ds - 1, 1 - dist(g + eps7/2)/ds)
best = ds[np.argmin(w7)]
print(f"P7 |d ln d/dgamma|*sin(gamma) against 1: worst {worst_sin:.1e}; at d and (B/2)^2/d: worst {worst_flip:.1e};"
      f" least worst rounded error at d = {best:.5f} B (B/2 = 0.5), {abs(best/(B/2) - 1):.1e} off ->",
      verdict(worst_sin <= 1e-12 and worst_flip <= 1e-12 and abs(best/(B/2) - 1) <= 0.01))
for d in (0.05, 0.5, 5, 50):
    i = np.argmin(abs(ds - d)); print(f"   d = {d:g} B: worst rounded error {w7[i]:.2e} ({w7[i]/(eps7/2):.3f} half-steps)")
