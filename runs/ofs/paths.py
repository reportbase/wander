"""One sweep, three paths: what fairness fixes and what the circle adds.

For plans/ofs-review-6.md (Q1-Q5) and observation-from-somewhere.md §11.2, question 2. Unit relations h, v in [0, 1];
the reading s = v/h; the direction theta = atan s from home (0, all of h) to the horizon (90 degrees, all of v); the
corner s = 1, 45 degrees. No amounts. A path runs from (1, 0) to (0, 1) and is swept evenly along its own length; b is
the share of the sweep done when the ray at theta is reached, measured here (arc length by quadrature up to the ray's
crossing, found by bisection), not taken from the closed forms it is checked against:
  circle  h^2 + v^2 = 1         b = 2 theta/pi
  line    h + v = 1             b = tan theta/(1 + tan theta)
  square  the larger of h, v 1  b = tan theta/2 to the corner, 1 - cot theta/2 past it
Run: python3 runs/ofs/paths.py   (mpmath, 40 digits; about a minute)
"""
from mpmath import mp, mpf, pi, sqrt, atan, atan2, tan, cot, sin, cos, quad, log, diff, inf, findroot

mp.dps = 40
D = pi / 180

# Each path as a curve P(u), u in [0, 1], with its speed |P'(u)| and the points where it bends.
PATHS = {
    "circle": (lambda u: ((1 - u*u) / (1 + u*u), 2*u / (1 + u*u)), lambda u: 2 / (1 + u*u), []),
    "line":   (lambda u: (1 - u, u), lambda u: sqrt(2), []),
    "square": (lambda u: (mpf(1), 2*u) if u <= mpf(1)/2 else (2 - 2*u, mpf(1)), lambda u: mpf(2), [mpf(1)/2]),
}

def length(name, u):
    _, speed, bends = PATHS[name]
    pts = [mpf(0)] + [k for k in bends if k < u] + [u]
    return quad(speed, pts)

def crossing(name, th):
    """The u at which the path meets the ray at angle th (bisection; the direction rises along every path)."""
    P = PATHS[name][0]
    lo, hi = mpf(0), mpf(1)
    for _ in range(mp.prec + 10):         # to the working precision (run 2; run 1 stopped at 150)
        mid = (lo + hi) / 2
        h, v = P(mid)
        if atan2(v, h) < th: lo = mid
        else: hi = mid
    return (lo + hi) / 2

TOTAL = {n: length(n, mpf(1)) for n in PATHS}

def b(name, th):
    return length(name, crossing(name, th)) / TOTAL[name]

CLOSED = {
    "circle": lambda th: 2*th/pi,
    "line":   lambda th: tan(th) / (1 + tan(th)),
    "square": lambda th: tan(th)/2 if th <= pi/4 else 1 - cot(th)/2,
}

def worst(xs):
    return max(abs(x) for x in xs)

out = []
def verdict(name, ok, line):
    out.append(f"{name}: {'not killed' if ok else 'KILLED'}  {line}")
    print(out[-1])

print("path lengths:", {n: mp.nstr(L, 12) for n, L in TOTAL.items()}, "(pi/2, sqrt 2, 2)")

# Q1. Home, the corner and the horizon agree; between, the paths part.
r2 = sqrt(2)
want = {
    "circle": {0: 0, 22.5: mpf(1)/4, 45: mpf(1)/2, 67.5: mpf(3)/4, 90: 1},
    "line":   {0: 0, 22.5: 1 - 1/r2, 45: mpf(1)/2, 67.5: 1/r2, 90: 1},
    "square": {0: 0, 22.5: (r2 - 1)/2, 45: mpf(1)/2, 67.5: (3 - r2)/2, 90: 1},
}
errs, apart = [], []
for n, tbl in want.items():
    row = []
    for deg, w in tbl.items():
        th = mpf(deg) * D
        got = b(n, th) if 0 < deg < 90 else (mpf(0) if deg == 0 else mpf(1))
        if deg in (0, 90):          # the ends measured too: the length to the first and last point
            got = length(n, mpf(0)) / TOTAL[n] if deg == 0 else length(n, mpf(1)) / TOTAL[n]
        errs.append(got - w)
        row.append(mp.nstr(got, 10))
        if n != "circle" and deg in (22.5, 67.5):
            apart.append(abs(got - 2*th/pi))
    print(f"  {n:7s} b at 0, 22.5, 45, 67.5, 90 deg:", ", ".join(row))
verdict("Q1", worst(errs) < mpf("1e-30") and min(apart) > mpf("1e-3"),
        f"closed forms to {mp.nstr(worst(errs), 3)}; line and square off 2theta/pi by at least {mp.nstr(min(apart), 6)}")

# Q2. Each is fair: b(theta) + b(90 - theta) = 1, so the median of s is 1.
sums = []
for n in PATHS:
    for deg in range(1, 90):
        sums.append(b(n, deg * D) + b(n, (90 - deg) * D) - 1)
verdict("Q2", worst(sums) < mpf("1e-30"), f"b(theta) + b(90 - theta) = 1 at 1..89 deg on all three, to {mp.nstr(worst(sums), 3)}")

# Q3. Each has no mean, at its own rate rho(0) ln 10 per decade.
def bs(n, s):
    return b(n, atan(s))
DENS = {
    "circle": lambda s: 2 / (pi * (1 + s*s)),
    "line":   lambda s: 1 / (1 + s)**2,
    "square": lambda s: mpf(1)/2 if s <= 1 else 1 / (2*s*s),
}
mp.dps = 30                         # the numerical derivative of a measured b, at 30 digits
derr = []
for n in PATHS:
    for s in (mpf(1)/4, mpf(1)/2, mpf(2), mpf(4)):
        derr.append((diff(lambda x: bs(n, x), s) - DENS[n](s)) / DENS[n](s))
mp.dps = 40
rho0 = {n: DENS[n](mpf(0)) for n in PATHS}
def tmean(n, S):
    pts = [mpf(0), mpf(1)] + [mpf(10)**k for k in range(1, 40) if mpf(10)**k < S] + [mpf(S)]
    return quad(lambda s: s * DENS[n](s), pts)
q3ok, lines = True, []
for n in PATHS:
    grow = [tmean(n, mpf(10)**(k+1)) - tmean(n, mpf(10)**k) for k in range(3, 10)]
    rate = rho0[n] * log(10)
    rel = abs(grow[-1] - rate) / rate
    q3ok &= rel < mpf("1e-8") and min(grow) > rate / 2
    lines.append(f"{n} rho(0) {mp.nstr(rho0[n], 6)}, per decade {mp.nstr(grow[0], 8)} .. {mp.nstr(grow[-1], 12)}"
                 f" against {mp.nstr(rate, 12)} (rel {mp.nstr(rel, 2)})")
q3ok &= worst(derr) < mpf("1e-25")
for l in lines: print("  " + l)
verdict("Q3", q3ok, f"densities from the measured b to {mp.nstr(worst(derr), 2)}; the truncated mean grows by rho(0) ln 10 a decade on all three")

# Q4. A fair weight that vanishes at the horizon has a mean: sin^2 2theta on the circle.
w = lambda th: (4/pi) * sin(2*th)**2
cdf = lambda th: quad(w, [0, th])
total = cdf(pi/2)
fair = worst([w(k*D) - w((90 - k)*D) for k in range(0, 91)])
med = tan(findroot(lambda th: cdf(th) - mpf(1)/2, pi/5))
dens_s = lambda s: 16 * s*s / (pi * (1 + s*s)**3)
S = mpf(10)**10
pts = [mpf(0), mpf(1)] + [mpf(10)**k for k in range(1, 10)] + [S]
mean_S = quad(lambda s: s * dens_s(s), pts)
mean_all = quad(lambda s: s * dens_s(s), [0, 1, inf])
short = 4/pi - mean_S
print(f"  sin^2 2theta: total {mp.nstr(total, 20)}, fair to {mp.nstr(fair, 2)}, median s {mp.nstr(med, 20)},"
      f" mean {mp.nstr(mean_all, 20)} (4/pi {mp.nstr(4/pi, 20)})")
print(f"  truncated mean at 1e10 short of 4/pi by {mp.nstr(short, 6)}; 8/(pi S^2) = {mp.nstr(8/(pi*S*S), 6)};"
      f" its density at the horizon (s -> inf, times s^2) {mp.nstr(dens_s(mpf(10)**20) * mpf(10)**40, 4)}")
verdict("Q4", abs(med - 1) < mpf("1e-30") and abs(short) < mpf("1e-19") and abs(total - 1) < mpf("1e-30"),
        f"median at the corner to {mp.nstr(abs(med - 1), 2)}; the mean 4/pi, short by {mp.nstr(short, 3)} at S = 1e10")

# Q5. On the circle, the turn and its shadow.
prod = worst([(k*D / sin(k*D)) * (sin(k*D) / (k*D)) - 1 for k in range(1, 91)])
outer, inner = (pi/2) / sin(pi/2), sin(pi/2) / (pi/2)
shadow = quad(sin, [0, pi/2]) / (pi/2)
e5 = worst([prod, outer - pi/2, inner - 2/pi, shadow - 2/pi])
verdict("Q5", e5 < mpf("1e-30"), f"outer x inner = 1 at 1..90 deg; at the horizon pi/2 and 2/pi; the even turn's mean shadow 2/pi; to {mp.nstr(e5, 2)}")
