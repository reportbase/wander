"""CLM run 1: the pull from columns (plans/clm-plan.md). Exact (sympy) and 30-digit quadrature (mpmath)."""
import sympy as sp
import mpmath as mp

mp.mp.dps = 40
out = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---------- C1: column only, D = 2, 3, 4 ----------
say("C1: a unit column (uniform density, integral of rho dr = 1) at r in [1,2] against [5,6]; pull per direction")
r = sp.symbols('r', positive=True)
c1_ok = True
for D in (2, 3, 4):
    for p in (sp.Rational(2*(D-1)-1, 2), D-1, sp.Rational(2*(D-1)+1, 2)):
        k = r**(-p) * r**(D-1)
        near = sp.integrate(k, (r, 1, 2)); far = sp.integrate(k, (r, 5, 6))
        rel = sp.N(far/near - 1, 30)
        exact = (p == D-1)
        say(f"  D={D} p={p}: far/near - 1 = {sp.nsimplify(rel) if exact else float(rel):}")
        if exact and rel != 0: c1_ok = False
        if not exact and abs(rel) <= 0.01: c1_ok = False
say("C1", "not killed" if c1_ok else "KILLED")

# ---------- C2: the shell from columns, by directions ----------
say("C2: thin shell radius a, density sigma; pull summed over directions, column sigma/|cos chi| per crossing (G = 1)")
a, d, sig, th = sp.symbols('a d sigma theta', positive=True)
M = 4*sp.pi*a**2*sig
# outside place at distance d > a on the axis; direction at angle theta from the line to the centre
s = sp.sqrt(a**2 - d**2*sp.sin(th)**2)
col = 2*sig*a/s                       # two crossings, each sigma*a/s
integrand = sp.cos(th)*col*2*sp.pi*sp.sin(th)
# substitute w = sin(theta)^2 (d w = 2 sin cos d theta), w in [0, a^2/d^2]
w = sp.symbols('w', positive=True)
integ_w = (2*sig*a/sp.sqrt(a**2 - d**2*w))*sp.pi
Fout = sp.simplify(sp.integrate(integ_w, (w, 0, a**2/d**2)))
say("  outside, summed over directions:", Fout, "; GM/d^2 =", sp.simplify(M/d**2),
    "; equal:", sp.simplify(Fout - M/d**2) == 0)
c2_ok = sp.simplify(Fout - M/d**2) == 0
# inside place at distance b < a: each direction crosses once, column sigma*a/s_in; theta and pi - theta pair
b = sp.symbols('b', positive=True)
s_in = sp.sqrt(a**2 - b**2*sp.sin(th)**2)
Fin = sp.integrate(sp.cos(th)*(sig*a/s_in)*2*sp.pi*sp.sin(th), (th, 0, sp.pi))
Fin = sp.simplify(Fin)
say("  inside, summed over directions:", Fin)
c2_ok = c2_ok and Fin == 0
# a 30-digit quadrature of the outside sum at a = 1, d = 3, sigma = 1, in theta directly
qa, qd = mp.mpf(1), mp.mpf(3)
qo = mp.quad(lambda t: mp.cos(t)*2*qa/mp.sqrt(qa**2 - qd**2*mp.sin(t)**2)*2*mp.pi*mp.sin(t), [0, mp.asin(qa/qd)])
say("  quadrature in theta, a=1, d=3:", mp.nstr(qo, 30), "against 4*pi/9 =", mp.nstr(4*mp.pi/9, 30),
    "diff", mp.nstr(qo - 4*mp.pi/9, 3))
c2_ok = c2_ok and abs(qo - 4*mp.pi/9) < mp.mpf('1e-25')
say("C2", "not killed" if c2_ok else "KILLED")

# ---------- C3: why inside is zero ----------
say("C3: from an inside place, a direction and its opposite meet the shell at equal angles (equal columns)")
bx, by, bz, ux, uy, uz = sp.symbols('b_x b_y b_z u_x u_y u_z', real=True)
A = sp.symbols('A', positive=True)
bu = bx*ux + by*uy + bz*uz
b2 = bx**2 + by**2 + bz**2
disc = sp.sqrt(bu**2 - b2 + A**2)
tp, tm = -bu + disc, -bu - disc           # forward and backward crossings (u assumed unit)
cos_p = (bu + tp)/A; cos_m = (bu + tm)/A   # u . (P + t u)/a
c3_ok = sp.simplify(cos_p + cos_m) == 0    # equal magnitude, opposite sign
say("  |cos chi| forward = |cos chi| backward, identically:", c3_ok, "(both = sqrt((b.u)^2 - b^2 + a^2)/a)")
# for p != 2 the two ends' pulls differ by (t+/|t-|)^(2-p); a numerical case
P = mp.matrix([0.3, 0.2, 0.1]); u = mp.matrix([0.6, 0.0, 0.8])
buv = sum(P[i]*u[i] for i in range(3)); bb = sum(P[i]**2 for i in range(3))
dd = mp.sqrt(buv**2 - bb + 1)
t1, t2 = -buv + dd, abs(-buv - dd)
for p in (2, 1.5, 2.5):
    ratio = (t1/t2)**(2-mp.mpf(p))
    say(f"  p={p}: the two ends' pulls in the ratio {mp.nstr(ratio, 12)}")
    if p == 2: c3_ok = c3_ok and ratio == 1
    else: c3_ok = c3_ok and abs(ratio - 1) > 1e-3
say("C3", "not killed" if c3_ok else "KILLED")

# ---------- C4: the Hooke exception, f = A/r^2 + B r (direct shell integral, exact) ----------
say("C4: f = A/r^2 + B r, a thin shell integrated directly (sympy)")
al = sp.symbols('alpha', positive=True)
Bc = sp.symbols('B', real=True); Ac = sp.symbols('A_c', real=True)
def shell_pull(f, dist):
    R = sp.sqrt(dist**2 + a**2 - 2*a*dist*sp.cos(al))
    integrand = sig*2*sp.pi*a**2*sp.sin(al)*f(R)*(dist - a*sp.cos(al))/R  # toward the centre, along the axis
    return integrand
# Hooke part: f(R) = R, so integrand f*(d - a cos)/R = (d - a cos), elementary
hooke_out = sp.simplify(sp.integrate(sig*2*sp.pi*a**2*sp.sin(al)*(d - a*sp.cos(al)), (al, 0, sp.pi)))
hooke_in = sp.simplify(sp.integrate(sig*2*sp.pi*a**2*sp.sin(al)*(b - a*sp.cos(al)), (al, 0, sp.pi)))
say("  r term, outside:", hooke_out, "= M d:", sp.simplify(hooke_out - M*d) == 0, "; inside:", hooke_in,
    "= M b:", sp.simplify(hooke_in - M*b) == 0)
# inverse-square part, outside and inside, by the substitution R^2 = d^2 + a^2 - 2 a d cos(alpha)
Rv = sp.symbols('R', positive=True)
def isq(dist, lo, hi):
    # sin(alpha) d alpha = R dR/(a dist); (dist - a cos) = (R^2 + dist^2 - a^2)/(2 dist)
    e = sig*2*sp.pi*a**2*(Rv/(a*dist))*(1/Rv**2)*((Rv**2 + dist**2 - a**2)/(2*dist))/Rv
    return sp.simplify(sp.integrate(e, (Rv, lo, hi)))
isq_out = isq(d, d - a, d + a); isq_in = isq(b, a - b, a + b)
say("  1/r^2 term, outside:", isq_out, "= M/d^2:", sp.simplify(isq_out - M/d**2) == 0, "; inside:", isq_in)
c4_ok = (sp.simplify(hooke_out - M*d) == 0 and sp.simplify(hooke_in - M*b) == 0
         and sp.simplify(isq_out - M/d**2) == 0 and isq_in == 0)
say("  so with f = A/r^2 + B r: outside A M/d^2 + B M d (the point mass at the centre), inside B M b, zero only at B = 0")
say("C4", "not killed" if c4_ok else "KILLED")

# ---------- C5: power laws, 30 digits ----------
say("C5: f = r^-p, shell a = 1 (M = 4 pi), outside at d = 2, inside at b = 1/2 (mpmath, 40 digits)")
def num_shell(p, dist):
    f = lambda al_: (lambda R: 2*mp.pi*mp.sin(al_)*R**(-p)*(dist - mp.cos(al_))/R)(mp.sqrt(dist**2 + 1 - 2*dist*mp.cos(al_)))
    return mp.quad(f, [0, mp.pi])
c5_ok = True
for p in (1, 1.5, 2, 2.5, 3):
    p = mp.mpf(p)
    out_ = num_shell(p, mp.mpf(2)); point = 4*mp.pi*mp.mpf(2)**(-p)
    in_ = num_shell(p, mp.mpf('0.5'))
    rel_out = out_/point - 1; rel_in = in_/out_
    say(f"  p={mp.nstr(p,3)}: outside/point - 1 = {mp.nstr(rel_out, 6)}; inside/outside = {mp.nstr(rel_in, 6)}")
    if p == 2:
        c5_ok = c5_ok and abs(rel_out) < mp.mpf('1e-25') and abs(rel_in) < mp.mpf('1e-25')
    else:
        c5_ok = c5_ok and abs(rel_out) > 0.01 and abs(rel_in) > 0.01
# two dimensions, a ring, p = 1
def ring(dist):
    f = lambda al_: (dist - mp.cos(al_))/(dist**2 + 1 - 2*dist*mp.cos(al_))
    return mp.quad(f, [0, mp.pi, 2*mp.pi])
ro, ri = ring(mp.mpf(2)), ring(mp.mpf('0.5'))
say(f"  ring, p=1: outside {mp.nstr(ro, 25)} against 2 pi/2 = {mp.nstr(mp.pi, 25)}; inside {mp.nstr(ri, 3)}")
c5_ok = c5_ok and abs(ro - mp.pi) < mp.mpf('1e-25') and abs(ri) < mp.mpf('1e-25')
say("C5", "not killed" if c5_ok else "KILLED")

# ---------- C6: scale ----------
say("C6: two shells, a place off both axes; lengths x k at fixed volume density (sigma x k)")
kk = sp.symbols('k', positive=True)
def pull(scene, place):
    F = sp.zeros(3, 1)
    for (c, a_, s_) in scene:
        v = sp.Matrix(c) - sp.Matrix(place); dist = sp.sqrt(v.dot(v))
        F += (4*sp.pi*a_**2*s_)*v/dist**3
    return F
scene = [((0, 0, 0), 1, 1), ((5, 1, 0), 2, sp.Rational(1, 2))]
place = (2, 3, 1)
F1 = pull(scene, place)
Fk = pull([(tuple(kk*x for x in c), kk*a_, kk*s_) for (c, a_, s_) in scene], tuple(kk*x for x in place))
ratio = sp.simplify(Fk.applyfunc(lambda e: e) - kk*F1)
say("  F(scaled) - k F:", list(ratio), "(direction unmoved, strength x k)")
c6_ok = all(sp.simplify(e) == 0 for e in ratio)
say("C6", "not killed" if c6_ok else "KILLED")

open('runs/clm/clm-run1.txt', 'w').write("\n".join(out) + "\n")
