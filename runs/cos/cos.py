# COS run 1: a cosine weight with no amount (plans/cos-plan.md). sympy for the ball and the shell, mpmath (30 digits)
# for the faced takes and the cube. The place at the origin; G = 1, rho = 1 unless said.
# Usage: python3 -I runs/cos/cos.py
import sympy as sp, mpmath as mp
mp.mp.dps = 30

# ---- K3, K4: the ball and the shell, in sympy (x = sin(theta) along the axis) ----
R, a, d, x = sp.symbols('R a d x', positive=True)
D_ball = sp.integrate(2*sp.pi*x, (x, 0, R/d))                       # 2 pi ∫ cos th sin th dth = 2 pi ∫ x dx
pull_ball = sp.integrate(2*sp.pi*x*2*sp.sqrt(R**2 - d**2*x**2), (x, 0, R/d))
print('K3 D of a ball:', sp.simplify(D_ball), ' equals pi (R/d)^2:', sp.simplify(D_ball - sp.pi*R**2/d**2) == 0)
print('K4 ball pull/(G rho) - (4/3) pi R^3/d^2:', sp.simplify(pull_ball - sp.Rational(4, 3)*sp.pi*R**3/d**2))
print('K4 ball <L> =', sp.simplify(pull_ball/D_ball))
# shell a < R: column = outer chord minus inner chord where the ray meets the inner ball
pull_shell = pull_ball - sp.integrate(2*sp.pi*x*2*sp.sqrt(a**2 - d**2*x**2), (x, 0, a/d))
L_shell = sp.simplify(pull_shell/D_ball)
print('K4 shell <L> =', sp.factor(L_shell), ' minus (4/3)(R^3-a^3)/R^2:',
      sp.simplify(L_shell - sp.Rational(4, 3)*(R**3 - a**3)/R**2))
print('K4 d appears in the ball and shell <L>:', d in sp.simplify(pull_ball/D_ball).free_symbols, d in L_shell.free_symbols)

# ---- K1: faced takes of the occupancy, by quadrature split at the cosine's zero ----
def vec(*c): return mp.matrix(list(c))
def dot(u, w): return sum(u[i]*w[i] for i in range(3))
def unit(u): return u/mp.sqrt(dot(u, u))
def frame(c):
    t = vec(1, 0, 0) if abs(c[0]) < 0.9 else vec(0, 1, 0)
    e1 = unit(t - c*dot(t, c)); e2 = mp.matrix([c[1]*e1[2]-c[2]*e1[1], c[2]*e1[0]-c[0]*e1[2], c[0]*e1[1]-c[1]*e1[0]])
    return e1, e2
def faced(ball, n):                  # ∫ over the ball's cap of max(0, u.n) dOmega
    ctr, rad = ball; dist = mp.sqrt(dot(ctr, ctr)); c = ctr/dist; al = mp.asin(rad/dist); e1, e2 = frame(c)
    A, B, C = dot(n, c), dot(n, e1), dot(n, e2); rho = mp.sqrt(B*B + C*C); ph0 = mp.atan2(C, B)
    def inner(th):
        f = lambda ph: max(mp.mpf(0), mp.cos(th)*A + mp.sin(th)*(B*mp.cos(ph) + C*mp.sin(ph)))
        pts = [ph0 - mp.pi, ph0 + mp.pi]
        if rho > 0 and mp.sin(th) > 0:
            q = -A*mp.cos(th)/(mp.sin(th)*rho)
            if -1 < q < 1:
                w = mp.acos(q); pts = sorted([ph0 - mp.pi, ph0 - w, ph0 + w, ph0 + mp.pi])
        return mp.sin(th)*mp.quad(f, pts)
    return mp.quad(inner, [0, al])
def Dvec(balls):                     # first moment of the occupancy (balls not overlapping in the sky)
    out = vec(0, 0, 0)
    for ctr, rad in balls:
        dist = mp.sqrt(dot(ctr, ctr)); out += (ctr/dist)*mp.pi*(rad/dist)**2
    return out
scene = [(vec(3, 1, 2), mp.mpf(1)), (vec(-4, 2, -5), mp.mpf('1.5'))]
D = Dvec(scene); worst = 0
for n in [vec(0, 0, 1), unit(vec(1, -2, 0.5)), unit(vec(-0.3, 0.7, 0.64)), unit(vec(1, 1, 1))]:
    Fp = sum(faced(b, n) for b in scene); Fm = sum(faced(b, -n) for b in scene)
    worst = max(worst, abs((Fp - Fm) - dot(n, D)))
print('K1 two balls, four facings: max |F(n) - F(-n) - n.D| =', mp.nstr(worst, 3))
six = vec(*[sum(faced(b, e) for b in scene) - sum(faced(b, -e) for b in scene) for e in (vec(1,0,0), vec(0,1,0), vec(0,0,1))])
print('K1 six axis facings give D: error', mp.nstr(max(abs(six[i] - D[i]) for i in range(3)), 3))

# ---- K2: scaling and an increasing map of the densities ----
def pull(balls, rhos):
    out = vec(0, 0, 0)
    for (ctr, rad), r in zip(balls, rhos):
        dist = mp.sqrt(dot(ctr, ctr)); out += (ctr/dist)*r*mp.mpf(4)/3*mp.pi*rad**3/dist**2
    return out
k = mp.mpf(7)
Dk = Dvec([(c*k, r*k) for c, r in scene])
print('K2 D under lengths x7: change', mp.nstr(max(abs(Dk[i]-D[i]) for i in range(3)), 3),
      '; pull x', mp.nstr(mp.sqrt(dot(pull([(c*k, r*k) for c, r in scene], [1, 2]), pull([(c*k, r*k) for c, r in scene], [1, 2]))) /
                        mp.sqrt(dot(pull(scene, [1, 2]), pull(scene, [1, 2]))), 12))
def ang(u, w): return mp.acos(dot(u, w)/mp.sqrt(dot(u, u)*dot(w, w)))
for name, f in [('rho^3', lambda r: r**3), ('e^rho', mp.exp)]:
    print('K2 densities (1, 2) mapped by', name, ': D unchanged (presence only); pull direction moves by',
          mp.nstr(ang(pull(scene, [1, 2]), pull(scene, [f(1), f(2)])), 6), 'rad')

# ---- K5: a unit cube face-on, the near face at distance h ----
hw = mp.mpf('0.5')
def Dcube(h): return 4*mp.quad(lambda X: mp.quad(lambda Y: h*h/(X*X + Y*Y + h*h)**2, [0, hw]), [0, hw])
def Om(z): return 4*mp.atan(hw*hw/(z*mp.sqrt(2*hw*hw + z*z)))          # solid angle of the face-on square at z
def pullcube(h): return mp.quad(Om, [h, h + 1])
Ls = {}
for h in ['0.5', '1', '2', '5', '20', '200']:
    h = mp.mpf(h); Ls[h] = pullcube(h)/Dcube(h)
    print('K5 cube, near face %s away: <L> = %s' % (mp.nstr(h, 4), mp.nstr(Ls[h], 10)))
print('K5 change from 0.5 to 20: %s%%' % mp.nstr(100*(Ls[mp.mpf('0.5')]/Ls[mp.mpf(20)] - 1), 6))

# ---- K6: a small ball hidden behind a large one ----
big = (vec(0, 0, 5), mp.mpf(1)); small = (vec(0, 0, 8), mp.mpf('0.1'))
hidden = mp.asin(small[1]/8) < mp.asin(big[1]/5)
print('K6 small ball hidden:', hidden, '; D with it = D without (the union of caps is the big cap); pull added',
      mp.nstr(pull([small], [1])[2], 12), '= (4/3) pi r^3/64 =', mp.nstr(mp.mpf(4)/3*mp.pi*mp.mpf('0.001')/64, 12))
