"""LGS run 1: light and gravity on one stage (plans/lgs-plan.md). Exact (sympy) and mpmath quadrature."""
import sympy as sp
import mpmath as mp
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

R, d, B, rho, G, w, k = sp.symbols('R d B rho G w k', positive=True)
# directions within the ball's cone, w = sin^2(theta) in [0, R^2/d^2]; cos(theta) sin(theta) dtheta = dw/2
# look: radiance B on every direction in the cone; flux along the axis
F = sp.integrate(B*2*sp.pi*sp.Rational(1, 2), (w, 0, R**2/d**2))
# pull: column 2 sqrt(R^2 - d^2 w) along each direction
g = sp.integrate(G*rho*2*sp.sqrt(R**2 - d**2*w)*2*sp.pi*sp.Rational(1, 2), (w, 0, R**2/d**2))
Dz = sp.pi*R**2/d**2
L1 = sp.simplify(F - B*Dz) == 0 and sp.simplify(g - G*rho*sp.Rational(4, 3)*R*Dz) == 0
say("L1: F =", sp.simplify(F), "; g =", sp.simplify(g), "; F = B D:", sp.simplify(F - B*Dz) == 0,
    "; g = G rho (4R/3) D:", sp.simplify(g - G*rho*sp.Rational(4, 3)*R*Dz) == 0)
say("L1", "not killed" if L1 else "KILLED")

# L2: flux from a small patch falls as d^-p; radiance = flux / solid angle (A cos/d^(D-1))
p, A, c, Dm = sp.symbols('p A c D', positive=True)
L2 = True
for Dd in (2, 3, 4):
    rad = d**(-p) / (A*c*d**(-(Dd - 1)))
    dd = sp.simplify(sp.diff(rad, d))
    sol = sp.solve(sp.Eq(sp.simplify(dd*d**(p - Dd + 2)), 0), p)
    say(f"L2: D={Dd}: radiance independent of d exactly when p in {sol}")
    L2 = L2 and sol == [Dd - 1]
say("L2", "not killed" if L2 else "KILLED")

# L3: absorption kappa; radiance from the near surface reduced by exp(-kappa r_near)
mp.mp.dps = 30
def F_abs(kap, dd, RR=1):
    # in v = sqrt(R^2 - d^2 w) (no cancellation at the edge): w = (R^2 - v^2)/d^2, dw = -2 v dv/d^2
    def f(v):
        ww = (RR**2 - v**2)/dd**2
        rnear = dd*mp.sqrt(1 - ww) - v
        return mp.pi*mp.exp(-kap*rnear)*2*v/dd**2
    return mp.quad(f, [0, RR])
def g_ball(dd, RR=1):
    return mp.quad(lambda v: 2*v*2*mp.pi*mp.mpf(1)/2*2*v/dd**2, [0, RR])  # G = rho = 1
L3 = True
for dd in (2, 5, 20):
    dd = mp.mpf(dd)
    Fa, F0 = F_abs(mp.mpf('0.1'), dd), mp.pi/dd**2
    say(f"L3: kappa R = 0.1, d = {mp.nstr(dd,3)} R: F/(B D) = {mp.nstr(Fa/F0, 8)}, g/F = {mp.nstr(g_ball(dd)/Fa, 8)}")
    if dd == 5: L3 = L3 and abs(Fa/F0 - 1) > 0.01
r2, r20 = g_ball(mp.mpf(2))/F_abs(mp.mpf('0.1'), mp.mpf(2)), g_ball(mp.mpf(20))/F_abs(mp.mpf('0.1'), mp.mpf(20))
L3 = L3 and abs(r20/r2 - 1) > 0.01
say("  (without absorption g/F = 4/3 at every d:", mp.nstr(g_ball(mp.mpf(5))/(mp.pi/25), 25), ")")
say("L3", "not killed" if L3 else "KILLED")

# L4: the ball's ratio, exactly; the cube's, numerically
ratio = sp.simplify(g/F)
say("L4: ball g/F =", ratio, "(no d)")
L4 = sp.diff(ratio, d) == 0
mp.mp.dps = 15
def cube(s):
    # unit cube, near face at distance s, place on its axis; only the near face is seen
    def Dz(x, y):
        r2_ = s*s + x*x + y*y
        return s*s/r2_**2
    def Lz(x, y):
        r2_ = s*s + x*x + y*y
        # path length inside the cube from the near face along the ray through (x, y, s)
        m = max(abs(x), abs(y))
        t_back = 1.0                                   # depth to the back face
        t_side = (0.5 - m)*s/m if m > 0 else mp.inf    # depth to a side face
        depth = min(t_back, t_side)
        return depth*mp.sqrt(r2_)/s * s*s/r2_**2
    D_ = mp.quad(Dz, [-0.5, 0.5], [-0.5, 0.5])
    g_ = mp.quad(Lz, [-0.5, 0, 0.5], [-0.5, 0, 0.5])
    return g_/D_
cs = {s: cube(mp.mpf(s)) for s in (0.5, 2, 20)}
for s, v in cs.items():
    say(f"  cube face-on at {s} sides: g/F = (G rho/B) x {mp.nstr(v, 6)}")
L4 = L4 and abs(cs[20]/cs[0.5] - 1) > 0.10
say("L4", "not killed" if L4 else "KILLED")

# L5: a small ball (r = 1/5, centre 8 along the axis) hidden behind a ball (R = 1 at 5): angular radii 0.025 < 0.2
F_two = F.subs({R: 1, d: 5})        # the look takes the first surface: the small ball is never met first
g_big = g.subs({R: 1, d: 5}); g_small = g.subs({R: sp.Rational(1, 5), d: 8})
g_two = g_big + g_small             # the pull sums every column along each direction
say("L5: F with the hidden ball =", F_two, "= F of the big ball alone; g rises by", sp.simplify(g_small),
    "= G (4/3) pi r^3 rho / 8^2:", sp.simplify(g_small - G*sp.Rational(4, 3)*sp.pi*sp.Rational(1, 125)*rho/64) == 0)
L5 = sp.simplify(g_small - G*sp.Rational(4, 3)*sp.pi*sp.Rational(1, 125)*rho/64) == 0
say("L5", "not killed" if L5 else "KILLED")

# L6: scale
Fk = F.subs({R: k*R, d: k*d}); gk = g.subs({R: k*R, d: k*d})
L6 = sp.simplify(Fk - F) == 0 and sp.simplify(gk - k*g) == 0
say("L6: lengths x k: F unmoved:", sp.simplify(Fk - F) == 0, "; g x k:", sp.simplify(gk - k*g) == 0)
say("L6", "not killed" if L6 else "KILLED")
open('runs/lgs/lgs-run1.txt', 'w').write("\n".join(out) + "\n")
