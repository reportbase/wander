# ACC run 2: the pair's whole first post-Newtonian field at a test body at rest (plans/acc-plan.md, run 2). sympy.
# Harmonic-gauge 1PN metric g00 = -1 + 2V - 2V^2, g0i = -4V_i, gij = delta(1 + 2V), retardation of V expanded with the
# superpotential; eps = 1/c^2 marks the 1PN order. Usage: python3 -I runs/acc/acc2.py
import sympy as sp, mpmath as mp
t, G, eps = sp.symbols('t G epsilon', positive=True)
X = sp.Matrix(sp.symbols('x1:4', real=True))
m = sp.symbols('m1 m2', positive=True)
z = [sp.Matrix([sp.Function('z%d%d' % (A, i))(t) for i in range(1, 4)]) for A in (1, 2)]
r = [sp.sqrt(((X - zA).T*(X - zA))[0]) for zA in z]
r12 = sp.sqrt(((z[0] - z[1]).T*(z[0] - z[1]))[0])
vel = [zA.diff(t) for zA in z]
U = [G*m[1]/r12, G*m[0]/r12]                           # the other mass's potential at each mass
VN = sum(G*m[A]/r[A] for A in (0, 1))
V1 = sum(G*m[A]*(sp.Rational(3, 2)*(vel[A].T*vel[A])[0] - U[A])/r[A] for A in (0, 1)) \
     + sp.Rational(1, 2)*G*sum(m[A]*r[A].diff(t, 2) for A in (0, 1))
Vi = [sum(G*m[A]*vel[A][i]/r[A] for A in (0, 1)) for i in range(3)]
acc = [VN.diff(X[i]) + eps*(V1.diff(X[i]) - 4*VN*VN.diff(X[i]) + 4*Vi[i].diff(t)) for i in range(3)]

# replace derivatives of the paths by symbols: positions p, velocities v, accelerations a
p = [sp.Matrix(sp.symbols('p%d_1:4' % A, real=True)) for A in (1, 2)]
v = [sp.Matrix(sp.symbols('v%d_1:4' % A, real=True)) for A in (1, 2)]
a = [sp.Matrix(sp.symbols('a%d_1:4' % A, real=True)) for A in (1, 2)]
rep = {}
for A in (0, 1):
    for i in range(3):
        rep[z[A][i].diff(t, 2)] = a[A][i]; rep[z[A][i].diff(t)] = v[A][i]
def plain(e):
    e = e.subs(rep)
    for A in (0, 1):
        e = e.subs({z[A][i]: p[A][i] for i in range(3)})
    return e
acc = [plain(e) for e in acc]

# B1: the coefficient of every acceleration component against ACC's term
rr = [sp.sqrt(((X - p[A]).T*(X - p[A]))[0]) for A in (0, 1)]
n = [(X - p[A])/rr[A] for A in (0, 1)]                  # from the mass to the test body
expect = [sum(G*m[A]/rr[A]*(sp.Rational(7, 2)*a[A][i] + sp.Rational(1, 2)*(a[A].T*n[A])[0]*n[A][i]) for A in (0, 1))
          for i in range(3)]
ok1 = True; noa = True
for i in range(3):
    e = sp.expand(acc[i].coeff(eps, 1))
    lin = sum(e.diff(a[A][j]).subs({a[B][k]: 0 for B in (0, 1) for k in range(3)})*a[A][j] for A in (0, 1) for j in range(3))
    ok1 &= sp.simplify(lin - expect[i]) == 0
    rest = sp.expand(e - lin)
    noa &= all(rest.diff(a[A][j]) == 0 for A in (0, 1) for j in range(3))
print('B1 the accelerations enter only as sum G m (7/2 a + 1/2 (a.n) n)/r:', ok1, '; nothing else holds an acceleration:', noa)

# B2: against the EIH equation's limit for a test body at rest (as remembered)
R12 = sp.sqrt(((p[0] - p[1]).T*(p[0] - p[1]))[0])
eih = []
for i in range(3):
    tot = 0
    for b in (0, 1):
        c = 1 - b; nba = (p[b] - X)/rr[b]; nab = -nba
        br = 1 + eps*(-4*(G*m[0]/rr[0] + G*m[1]/rr[1]) - G*m[c]/R12 + 2*(v[b].T*v[b])[0]
                      - sp.Rational(3, 2)*((v[b].T*nab)[0])**2 + sp.Rational(1, 2)*((p[b] - X).T*a[b])[0])
        tot += G*m[b]*nba[i]/rr[b]**2*br
        tot += eps*G*m[b]/rr[b]**2*((nab.T*(-3*v[b]))[0])*(-v[b][i])
        tot += eps*sp.Rational(7, 2)*G*m[b]*a[b][i]/rr[b]
    eih.append(tot)
diffs = [sp.simplify(sp.expand(acc[i] - eih[i])) for i in range(3)]
print('B2 the whole 1PN expression minus EIH (test body at rest), components:', diffs)

# B3: a circular pair, lengths x k and masses x k
mp.mp.dps = 40
def num(k):
    m1, m2, Dd = mp.mpf(1)*k, mp.mpf(2)*k, mp.mpf(100)*k
    w = mp.sqrt((m1 + m2)/Dd**3); ph = mp.mpf('0.7')
    c1 = -m2/(m1 + m2)*Dd; c2 = m1/(m1 + m2)*Dd
    P = [[c*mp.cos(ph), c*mp.sin(ph), 0] for c in (c1, c2)]
    Vv = [[-c*w*mp.sin(ph), c*w*mp.cos(ph), 0] for c in (c1, c2)]
    Aa = [[-c*w*w*mp.cos(ph), -c*w*w*mp.sin(ph), 0] for c in (c1, c2)]
    vals = {G: 1, eps: 1, m[0]: m1, m[1]: m2}
    for A in (0, 1):
        for i in range(3):
            vals[p[A][i]] = P[A][i]; vals[v[A][i]] = Vv[A][i]; vals[a[A][i]] = Aa[A][i]
    for i, val in enumerate([300*k, 170*k, 90*k]): vals[X[i]] = val
    f = sp.lambdify(list(vals.keys()), acc, 'mpmath')
    return mp.matrix(f(*vals.values()))
base = num(1)
for k in (5, 1000):
    s = num(k); cosang = sum(base[i]*s[i] for i in range(3))/mp.sqrt(sum(x**2 for x in base)*sum(x**2 for x in s))
    print('B3 k = %d: direction moved by %s rad; size x k = %s' % (k, mp.nstr(mp.acos(min(1, cosang)), 3),
          mp.nstr(mp.sqrt(sum(x**2 for x in s))/mp.sqrt(sum(x**2 for x in base))*k, 20)))
