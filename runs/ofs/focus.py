# OFS §8, "The corner is the best focus" (Corollary 6.1): exact checks.
# Run from the repository's root: python3 runs/ofs/focus.py
#
# (a) The turn's K addresses laid along distance at H·tan(kπ/2K): a cell's width relative to its place is least at the
#     corner, (π/2K)(s + 1/s) in the continuum, and in the discrete cells the two beside the corner are the finest and
#     equal. Any cost f with f(s) = f(1/s) and convex in ln s is least at s = 1; without convexity it need not be.
# (c) The next look's place X follows a reciprocal-symmetric law (the uniform turn here). The focus c that makes the
#     expected travel E|g(X) − g(c)| least is the median, s = 1, on every ruler g tried: the angle, the levels ln s and
#     the in-place lay. A lopsided law (density ∝ 1 + a·cos 2θ) moves the best focus to its own median, the same on
#     every ruler.
from mpmath import mp, mpf, pi, tan, atan, log, cos, sin, quad, findroot, sqrt, diff, exp

mp.dps = 40
ok = True

def check(name, err, tol):
    global ok
    good = abs(err) <= tol
    ok = ok and good
    print(("pass " if good else "FAIL ") + f" {name}: {mp.nstr(err, 5)}")

# (a) continuum: the relative cell (dd/d)/(dθ) at d = H·tan θ is sec²θ/tan θ = s + 1/s, times π/2K per address.
K = 64
rel = lambda s: (pi/(2*K))*(s + 1/s)
for s in [mpf(1)/8, mpf(1)/2, mpf(2), mpf(8)]:
    t = atan(s)
    check(f"relative cell at s = {mp.nstr(s,3)} from the turn - (π/2K)(s + 1/s)",
          diff(lambda u: log(tan(u)), t)*(pi/(2*K)) - rel(s), mpf(10)**-30)
check("d/ds (s + 1/s) at the corner", diff(lambda s: s + 1/s, mpf(1)), mpf(10)**-30)
print("      relative cell at the corner:", mp.nstr(rel(mpf(1)), 8), "= π/K")

# (a) discrete: cells [tan(kπ/2K), tan((k+1)π/2K)], their width over their geometric middle.
cells = []
for k in range(1, K - 1):
    a, b = tan(k*pi/(2*K)), tan((k + 1)*pi/(2*K))
    cells.append(((b - a)/sqrt(a*b), k))
best = min(cells)
ks = sorted(k for w, k in cells if abs(w - best[0]) < mpf(10)**-30)
check("finest discrete cells are the two beside the corner (k = K/2 − 1, K/2)", (ks == [K//2 - 1, K//2]) - 1, 0)
print("      finest relative width:", mp.nstr(best[0], 8), "at k =", ks)

# (a) reciprocal-symmetric costs convex in ln s, least at the corner; an even but non-convex one is not.
for name, f in [("s + 1/s", lambda s: s + 1/s), ("(ln s)²", lambda s: log(s)**2), ("|ln s|", lambda s: abs(log(s)))]:
    m = findroot(lambda x: diff(lambda u: f(exp(u)), x), mpf('0.3')) if name != "|ln s|" else mpf(0)
    check(f"argmin of {name} in levels", m, mpf(10)**-25)
g = lambda x: (x**2 - 1)**2   # even in ξ = ln s, not convex: least at s = e and 1/e, the corner a local maximum
check("non-convex even cost: least away from the corner (ξ = ±1)", findroot(lambda x: diff(g, x), mpf('0.9')) - 1, mpf(10)**-25)

# (c) expected travel on three rulers, under the uniform turn and a lopsided weight.
rulers = {
    "angle θ": lambda th: th,
    "levels ln s": lambda th: log(tan(th)),
    "in-place lay": lambda th: tan(th) if th <= pi/4 else 2 - 1/tan(th),
}
def density(a):
    return lambda th: (1 + a*cos(2*th))*2/pi
def travel(gfun, dens, phi):
    # the focus at angle φ, c = g(φ); the integrand's kink is at θ = φ, so the quadrature is split there
    c = gfun(phi)
    pts = sorted(set([mpf(0), pi/4, phi, pi/2]))
    return quad(lambda th: abs(gfun(th) - c)*dens(th), pts)
def best_focus(gfun, dens):
    # minimise the expected travel over the focus's angle φ by golden section (g increasing, so φ ↔ c one to one)
    lo, hi = mpf('0.05'), pi/2 - mpf('0.05')
    r = (sqrt(5) - 1)/2
    x1, x2 = hi - r*(hi - lo), lo + r*(hi - lo)
    f1, f2 = travel(gfun, dens, x1), travel(gfun, dens, x2)
    for _ in range(70):
        if f1 < f2:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - r*(hi - lo); f1 = travel(gfun, dens, x1)
        else:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + r*(hi - lo); f2 = travel(gfun, dens, x2)
    return tan((lo + hi)/2)

mp.dps = 20
for a in [mpf(0), mpf('0.2'), mpf('-0.2'), mpf('0.5')]:
    th_m = findroot(lambda t: t + (a/2)*sin(2*t) - pi/4, pi/4)   # the lopsided law's median
    s_m = tan(th_m)
    for name, gfun in rulers.items():
        s = best_focus(gfun, density(a))
        check(f"a = {mp.nstr(a,2)}: best focus on {name} - the median {mp.nstr(s_m,6)}", s - s_m, mpf(10)**-8)
    print(f"      a = {mp.nstr(a,2)}: best focus s = {mp.nstr(s_m, 8)} ({mp.nstr(log(s_m)/log(2), 6)} levels from the corner)")

print("ALL PASS" if ok else "SOME FAILED")
