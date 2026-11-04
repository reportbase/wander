# THM run 2: the one-thumb circle (plans/thm-plan.md). Exact (sympy) and 50-digit (mpmath).
import sympy as sp, mpmath as mp
mp.mp.dps = 50
ok = lambda c: 'not killed' if c else 'KILLED'
EPS = mp.mpf(10)**-20

# U1: ball radius 1 (H = 1) about C = (1,1,1); distance from C to face x_i = 0 is 1; foot of the perpendicular
C = sp.Matrix([1, 1, 1])
feet = []
for i in range(3):
    f = C.copy(); f[i] = 0; feet.append(f)
    print('U1 face', i + 1, 'distance from C', abs(C[i]), 'touch point', list(f))
half = sp.asin(1/sp.sqrt(3))      # outline half-angle: sin = radius / |C|
print('U1 outline half-angle', sp.N(half*180/sp.pi, 12), 'deg; |C| =', sp.sqrt(3))
look = C/sp.sqrt(3)
ang_feet = [sp.acos((f.dot(look))/f.norm()) for f in feet]
print('U1 touch points off the look:', [sp.N(a*180/sp.pi, 12) for a in ang_feet])
# largest cone inside the wedge: angle from look to plane x_i = 0 is asin(look_i) = asin(1/sqrt3)
U1 = all(abs(C[i]) == 1 for i in range(3)) and all(sp.simplify(a - half) == 0 for a in ang_feet) \
     and sp.simplify(sp.asin(look[0]) - half) == 0
print('U1', ok(U1))

# U2: walk the outline: unit directions at half-angle about the look
u1 = sp.Matrix([1, -1, 0])/sp.sqrt(2); u2 = sp.Matrix([1, 1, -2])/sp.sqrt(6)
L = [mp.mpf(1)/mp.sqrt(3)]*3; A = [mp.mpf(c) for c in (1/mp.sqrt(2), -1/mp.sqrt(2), 0)]
B = [1/mp.sqrt(6), 1/mp.sqrt(6), -2/mp.sqrt(6)]
ca, sa = mp.sqrt(mp.mpf(2)/3), 1/mp.sqrt(3)
mins = []
N = 3600
zeros = []
for k in range(N):
    p = 2*mp.pi*k/N
    d = [ca*L[i] + sa*(mp.cos(p)*A[i] + mp.sin(p)*B[i]) for i in range(3)]
    m = min(d); mins.append(m)
    if abs(m) < EPS: zeros.append((k, [mp.nstr(x, 6) for x in d]))
print('U2 least component on the outline', mp.nstr(min(mins), 6), '; zeros at', len(zeros), 'of', N, 'samples:', [z[0] for z in zeros])
# at a touch point, the remaining pair
tp = [mp.mpf(1)/mp.sqrt(2), mp.mpf(1)/mp.sqrt(2), 0]
print('U2 touch point (1,1,0)/√2: readings e1/e2 =', tp[0]/tp[1], ', e3/e1 = 0 (home), e1/e3 = ∞ (horizon)')
U2 = min(mins) > -EPS and len(zeros) == 3 and abs(tp[0]/tp[1] - 1) < EPS
# analytic: min component on outline vs phase is a cosine; zero only where it touches (its minimum = 0)
print('U2', ok(U2))

# U3: plane
C2 = sp.Matrix([1, 1]); half2 = sp.asin(1/sp.sqrt(2))
print('U3 outline half-angle', sp.N(half2*180/sp.pi, 12), 'deg about 45°: from', sp.N(45 - half2*180/sp.pi), 'to', sp.N(45 + half2*180/sp.pi))
U3 = sp.simplify(half2 - sp.pi/4) == 0
print('U3', ok(U3))

# U4: cone solid angle 2π(1 - cos half) over the wedge π/2
share = sp.simplify(2*sp.pi*(1 - sp.cos(half))/(sp.pi/2))
print('U4 share inside the cone', share, '=', sp.N(share, 12))
# check numerically: uniform directions in the octant by quadrature of the indicator in polar angle about the look
num = mp.quad(lambda t: mp.sin(t), [0, mp.asin(1/mp.sqrt(3))])*2*mp.pi/(mp.pi/2)
U4 = abs(num - (4*(1 - mp.sqrt(mp.mpf(2)/3)))) < 1e-8 and sp.simplify(share - 4*(1 - sp.sqrt(sp.Rational(2, 3)))) == 0
print('U4', ok(U4))

# U5: levels near the crosshair
e, ph = sp.symbols('epsilon phi', real=True)
u = sp.cos(ph)*u1 + sp.sin(ph)*u2
n = look*sp.cos(e) + u*sp.sin(e)
lv = [sp.log(n[i]/n[j]) for i, j in ((0, 1), (1, 2), (2, 0))]
S = sum(l**2 for l in lv)
S2 = sp.simplify(sp.series(S, e, 0, 3).removeO())
print('U5 Σℓ² to second order:', S2, '(no φ: round)')
lin = [sp.simplify(sp.diff(l, e).subs(e, 0)) for l in lv]
print('U5 dℓ/dε at the crosshair:', lin)
f = sp.lambdify(ph, sp.Max(*[sp.Abs(x) for x in lin]), 'mpmath')
vals = [f(2*mp.pi*k/720) for k in range(720)]
ratio = max(vals)/min(vals)
print('U5 worst level per unit angle: max', mp.nstr(max(vals), 12), 'min', mp.nstr(min(vals), 12), 'ratio', mp.nstr(ratio, 12), '(2/√3 =', mp.nstr(2/mp.sqrt(3), 12), ')')
# grain toward a touch point: n(t) from look to (1,1,0)/√2; worst cosh vs reading r = n3/n1
def grain(t):
    d = [mp.cos(t)*L[i] + mp.sin(t)*(-B[i]) for i in range(3)]  # -B points to (1,1,-2)->(-.., ..) ; use toward e3 = 0 side
    ls = [mp.log(d[i]/d[j]) for i, j in ((0, 1), (1, 2), (2, 0))]
    return mp.cosh(max(abs(x) for x in ls)), d
for tdeg in (0, 1, 5, 15, 25, 30, 34, 35, 35.2):
    g, d = grain(mp.mpf(tdeg)*mp.pi/180)
    r = min(d)/max(d)
    print('U5 toward the touch point at %5.1f°: worst grain ×%s, least reading %s, grain × reading %s' % (tdeg, mp.nstr(g, 8), mp.nstr(r, 8), mp.nstr(g*r, 8)))
gs = [sp.diff(S, e).subs(e, 0)]
U5 = sp.simplify(S2.diff(ph)) == 0 and abs(ratio - 2/mp.sqrt(3)) < 1e-9 and abs(grain(mp.asin(1/mp.sqrt(3))*(1 - mp.mpf(10)**-12))[0]*min(grain(mp.asin(1/mp.sqrt(3))*(1 - mp.mpf(10)**-12))[1])/max(grain(mp.asin(1/mp.sqrt(3))*(1 - mp.mpf(10)**-12))[1]) - mp.mpf(1)/2) < 1e-6
print('U5', ok(U5))

# U6: sideways at the target's distance D = sqrt3 H: offset x = D tan a; x/H = sqrt3 tan a; corner x = H
a6 = sp.atan(1/sp.sqrt(3))
print('U6 sideways corner off the look', sp.N(a6*180/sp.pi, 12), 'deg; for any H since D/H = √3')
U6 = sp.simplify(a6 - sp.pi/6) == 0
print('U6', ok(U6))

# U7: turn from the look: corner tan a = 1 -> 45°; hemisphere share within: 1 - cos 45°
sh7 = 1 - sp.cos(sp.pi/4)
print('U7 corner 45°, share of the hemisphere within', sp.nsimplify(sh7), '=', sp.N(sh7, 10))
U7 = sp.simplify(sh7 - (1 - 1/sp.sqrt(2))) == 0
print('U7', ok(U7))
