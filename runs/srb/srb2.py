# SRB run 2: can the conformal sky (C) be had from reads? See plans/srb-plan.md, "Run 2".
import sympy as sp, mpmath as mp, random, itertools, time
mp.mp.dps = 50
random.seed(790)
ok = {}
x, y, z = sp.symbols('x y z', real=True)
n = sp.Matrix([x, y, z])
E = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]

# ---- R1: Galilean direction maps do not close; Lorentz ones do; Galilean velocities do
def gal(b, th): return mp.atan2(mp.sin(th), mp.cos(th) + b)
def lor(b, th): return mp.acos((mp.cos(th) + b) / (1 + b * mp.cos(th)))
ths = [mp.pi * (i + mp.mpf(1)/2) / 400 for i in range(400)]
b1 = b2 = mp.mpf('0.3')
def maxres(f, b, comp): return max(abs(f(b, th) - comp[i]) for i, th in enumerate(ths))
compG = [gal(b2, gal(b1, th)) for th in ths]
# best single beta by golden-section on the max residual (unimodal near the optimum); also scan first
grid = [mp.mpf(i)/1000 for i in range(1, 1000)]
bestg = min(grid, key=lambda b: maxres(gal, b, compG))
lo, hi = bestg - mp.mpf('0.002'), bestg + mp.mpf('0.002')
phi = (mp.sqrt(5) - 1) / 2
for _ in range(120):
    c1 = hi - phi * (hi - lo); c2 = lo + phi * (hi - lo)
    if maxres(gal, c1, compG) < maxres(gal, c2, compG): hi = c2
    else: lo = c1
bG = (lo + hi) / 2; rG = maxres(gal, bG, compG)
compL = [lor(b2, lor(b1, th)) for th in ths]
bL = (b1 + b2) / (1 + b1 * b2); rL = maxres(lor, bL, compL)
velres = max(abs(mp.atan2(mp.sin(th), mp.cos(th) + b1 + b2) - mp.atan2(mp.sin(th), (mp.cos(th) + b1) + b2)) for th in ths)
ok['R1'] = (rG > mp.mpf('1e-3')) and (rL < mp.mpf('1e-40')) and (velres < mp.mpf('1e-45'))
print('R1: Galilean composition, best single beta %s, max residual %s rad' % (mp.nstr(bG, 8), mp.nstr(rG, 5)))
print('    Lorentz composition at (b1+b2)/(1+b1 b2), max residual', mp.nstr(rL, 3))
print('    Galilean velocities (speed carried), two steps against one of b1+b2:', mp.nstr(velres, 3))

# ---- fields on the sphere, as polynomial fields on R^3 restricted to |n| = 1
def L(i): return E[i].cross(n)                                  # turns
def X(a, i):                                                    # the axial field along e_i
    ni = n.dot(E[i]); return (1 + a * ni**2) * (ni * n - E[i])
def br(A, B):                                                   # Lie bracket [A, B] = (A.grad)B - (B.grad)A
    J = lambda F: F.jacobian(n)
    return sp.expand(J(B) * A - J(A) * B)

# ---- R2: X_a's symmetries, flow direction, conformality
a = sp.symbols('a', real=True)
Xa = X(a, 2)
on_sph = lambda e: sp.simplify(e.subs(z**2, 1 - x**2 - y**2)) if e != 0 else 0
tang = on_sph(sp.expand(n.dot(Xa) .subs({})) - 0)
tang = sp.simplify(sp.expand(n.dot(Xa)).subs(z**2, 1 - x**2 - y**2))
c_turn = [sp.simplify(sp.expand(v).subs(z**2, 1 - x**2 - y**2)) for v in br(L(2), Xa)]
def mirror(M, F):  # pushforward of F by the linear isometry M: (M_* F)(n) = M F(M^-1 n)
    sub = dict(zip([x, y, z], list(M.inv() * n)))
    return M * F.subs(sub, simultaneous=True)
Sx = sp.diag(-1, 1, 1); Sz = sp.diag(1, 1, -1)
c_refl = sp.simplify(mirror(Sx, Xa) - Xa)
anti = sp.simplify(mirror(Sz, Xa) + Xa)
th = sp.symbols('theta', positive=True)
f = sp.sin(th) * (1 + a * sp.cos(th)**2)       # X_a = f(theta) e_theta, e_theta = (z n - e_z)/sin(theta)
etheta_check = sp.simplify((Xa / (1 + a * z**2)).subs({x: sp.sin(th), y: 0, z: sp.cos(th)}) -
                           sp.sin(th) * sp.Matrix([sp.cos(th), 0, -sp.sin(th)]))
confo = sp.simplify(sp.diff(f, th) - f * sp.cot(th))
ok['R2'] = (tang == 0 and all(v == 0 for v in c_turn) and c_refl == sp.zeros(3, 1) and anti == sp.zeros(3, 1)
            and etheta_check == sp.zeros(3, 1) and sp.simplify(confo.subs(a, 0)) == 0 and sp.simplify(confo) != 0)
print('R2: n.X_a on sphere:', tang, '; [L_z, X_a]:', list(c_turn), '; mirror x:', list(c_refl), '; anti z:', list(anti))
print('    X_a = sin(th)(1 + a cos^2 th) e_theta, > 0 on (0, pi) for a > -1; f\' - f cot th =', sp.factor(confo))

# ---- exact rational points on the sphere for ranks
def rpt(u, v):
    q = 1 + u*u + v*v; return (sp.Rational(2*u, 1)/q, sp.Rational(2*v, 1)/q, (1 - u*u - v*v)/q)
pts = []
while len(pts) < 40:
    u = sp.Rational(random.randint(-9, 9), random.randint(1, 7)); v = sp.Rational(random.randint(-9, 9), random.randint(1, 7))
    p = rpt(u, v)
    if p not in pts: pts.append(p)
def vec(F):
    fl = [sp.lambdify((x, y, z), c) for c in F]
    return [sp.nsimplify(g(*p)) if False else sp.Rational(sp.sympify(c).subs({x: p[0], y: p[1], z: p[2]})) for p in pts for c, g in zip(F, fl)]
def vecq(F):
    out = []
    for p in pts:
        s = {x: p[0], y: p[1], z: p[2]}
        out += [sp.nsimplify(c.subs(s)) for c in F]
    return out
def basis_add(basis, rows, F):
    r = vecq(F)
    M = sp.Matrix(rows + [r])
    if M.rank() > len(rows): basis.append(F); rows.append(r); return True
    return False

def generate(aval, depth):
    gens = [L(0), L(1), L(2), X(aval, 0), X(aval, 1), X(aval, 2)]
    basis, rows = [], []
    for F in gens: basis_add(basis, rows, sp.expand(F))
    dims = [len(basis)]
    new = list(basis)
    for d in range(depth):
        added = []
        for A in basis[:]:
            for B in new:
                if A is B: continue
                C = br(A, B)
                if all(c == 0 for c in C): continue
                if basis_add(basis, rows, C): added.append(C)
                if len(basis) >= 120: break
        new = added
        dims.append(len(basis))
        if not added: dims += [len(basis)] * (depth - d - 1); break
    return dims

t0 = time.time()
res3 = {}
for aval in [sp.Integer(0), sp.Integer(1), sp.Rational(1, 2), sp.Rational(-1, 2)]:
    res3[aval] = generate(aval, 3)
    print('R3: a = %s, dimension at depth 0..3: %s  (%.0f s)' % (aval, res3[aval], time.time() - t0))
r3a = res3[0] == [6, 6, 6, 6]
r3b = all(res3[v][1] > 6 and res3[v][1] < res3[v][2] < res3[v][3] for v in [sp.Integer(1), sp.Rational(1, 2), sp.Rational(-1, 2)])
ok['R3'] = r3a and r3b

# ---- R4: sl(3,R) on directions
Bs = sp.symbols('b0:9', real=True); B = sp.Matrix(3, 3, Bs)
VB = sp.expand(B * n - (n.dot(B * n)) * n)
def lin_rows(F):  # rows of the linear map B -> F(n) at the points, coefficient matrix in b0..b8
    rows = []
    for p in pts:
        s = {x: p[0], y: p[1], z: p[2]}
        for c in F: rows.append([sp.nsimplify(sp.expand(c.subs(s)).coeff(bb)) for bb in Bs])
    return sp.Matrix(rows)
rank8 = lin_rows(VB).rank()
so3_in = all(sp.simplify(sp.expand(VB.subs(dict(zip(Bs, list(sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])))))) - L(2)) == sp.zeros(3, 1) for _ in [0])
comm = br(L(2), VB)
Ncomm = lin_rows(comm).nullspace()
# fields commuting with turns about z, modulo the trace (which gives the zero field)
Kmat = lin_rows(VB)
comm_fields = [sp.expand(VB.subs(dict(zip(Bs, list(v))))) for v in Ncomm]
cf_rank = sp.Matrix([vecq(F) for F in comm_fields]).rank()
anti_req = sp.expand(mirror(Sz, VB) + VB)
both = sp.Matrix.vstack(lin_rows(comm), lin_rows(anti_req)).nullspace()
anti_fields = [sp.expand(VB.subs(dict(zip(Bs, list(v))))) for v in both]
anti_nonzero = [F for F in anti_fields if any(sp.simplify(c.subs(z**2, 1 - x**2 - y**2)) != 0 for c in F)]
ok['R4'] = rank8 == 8 and so3_in and cf_rank == 2 and len(anti_nonzero) == 0
print('R4: rank of sl(3,R) fields:', rank8, '; so(3) inside:', so3_in,
      '; fields commuting with turns about z: rank', cf_rank, [list(F) for F in comm_fields])
print('    commuting with turns and anti-commuting with z -> -z, nonzero fields:', len(anti_nonzero))

print('SUMMARY:', ok)
