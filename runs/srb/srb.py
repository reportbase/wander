# SRB run 1: the bridge from observer geometry to special relativity. See plans/srb-plan.md.
import sympy as sp, mpmath as mp, random
mp.mp.dps = 50
random.seed(788)
ok = {}

# ---- B1(a'): Mobius maps fixing 0 and inf, commuting with conj, continuous from identity
a, b, c, d, z = sp.symbols('a b c d z')
lam = sp.symbols('lam')
# fixing 0: f(0)=0 -> b=0; fixing inf: c=0 -> f = (a/d) z = lam z
f = lam*z
# commute with conj: conj(f(z)) == f(conj(z)) for all z  <=>  conj(lam) == lam
lr, li = sp.symbols('lr li', real=True)
fz = (lr+sp.I*li)*z
zz = sp.symbols('x y', real=True); Z = zz[0]+sp.I*zz[1]
lhs = sp.conjugate((lr+sp.I*li)*Z); rhs = (lr+sp.I*li)*sp.conjugate(Z)
cond = sp.simplify(sp.expand(lhs-rhs))
sol = sp.solve([sp.re(cond), sp.im(cond)], [li], dict=True)
ok['B1a_prime'] = (sol == [{li: 0}])
print('B1(a\'): conj-commuting forces Im(lam)=0:', sol)

# ---- B1(b): z' = z/k on stereographic chart -> Lorentz aberration
t, k = sp.symbols('t k', positive=True)
cos_t = (1-t**2)/(1+t**2)
tp = t/k
cos_tp = (1-tp**2)/(1+tp**2)
beta = (k**2-1)/(k**2+1)
diff_b = sp.simplify(cos_tp - (cos_t+beta)/(1+beta*cos_t))
eta = sp.symbols('eta', real=True)
diff_tanh = sp.simplify((sp.exp(2*eta)-1)/(sp.exp(2*eta)+1) - sp.tanh(eta))
ok['B1b'] = (diff_b == 0) and (sp.simplify(diff_tanh.rewrite(sp.exp)) == 0)
print('B1(b): aberration identity residual:', diff_b, '; beta=tanh(ln k):', sp.simplify(diff_tanh.rewrite(sp.exp)))

# ---- B1(c): composition
k1, k2 = sp.symbols('k1 k2', positive=True)
b_ = lambda kk: (kk**2-1)/(kk**2+1)
comp = sp.simplify(b_(k1*k2) - (b_(k1)+b_(k2))/(1+b_(k1)*b_(k2)))
ok['B1c'] = (comp == 0)
print('B1(c): velocity composition residual:', comp)

# ---- B1(d) and B2: stretch ratio and Doppler as stretch
def lorentz(th, be):
    return mp.acos((mp.cos(th)+be)/(1+be*mp.cos(th)))
def galileo(th, be):
    return mp.atan2(mp.sin(th), mp.cos(th)+be)
def ratio(fn, th, be):
    merid = mp.diff(lambda x: fn(x, be), th)
    trans = mp.sin(fn(th, be))/mp.sin(th)
    return merid/trans, merid, trans
be = mp.mpf('0.6')
grid = [mp.pi*(i+0.5)/400 for i in range(400)]
gdev = max(abs(ratio(galileo, th, be)[0]-1) for th in grid)
ldev = max(abs(ratio(lorentz, th, be)[0]-1) for th in grid)
ok['B1d'] = gdev > mp.mpf('0.1') and ldev < mp.mpf('1e-40')
print('B1(d): Galilean max |merid/trans - 1| =', mp.nstr(gdev, 6), '; Lorentz =', mp.nstr(ldev, 3))

worst = mp.mpf(0)
for be in [mp.mpf('0.1'), mp.mpf('0.6'), mp.mpf('0.99')]:
    for _ in range(1000):
        th = mp.mpf(random.random())*mp.pi*mp.mpf('0.998') + mp.pi*mp.mpf('0.001')
        thp = lorentz(th, be)
        r, merid, trans = ratio(lorentz, th, be)
        D = mp.sqrt(1-be**2)/(1-be*mp.cos(thp))
        worst = max(worst, abs(merid*D-1), abs(trans*D-1))
ok['B2'] = worst < mp.mpf('1e-40')
print('B2: max |stretch*D - 1| over 3000 points =', mp.nstr(worst, 3))

# ---- B3: SL(2,C) diag(k^1/2, k^-1/2) acting on Hermitian X gives the boost
T, X, Y, Zc = sp.symbols('T X Y Zc', real=True)
Xm = sp.Matrix([[T+Zc, X-sp.I*Y], [X+sp.I*Y, T-Zc]])
M = sp.diag(sp.sqrt(k), 1/sp.sqrt(k))
Xp = sp.simplify(M*Xm*M.H)
Tp = sp.simplify((Xp[0, 0]+Xp[1, 1])/2); Zp = sp.simplify((Xp[0, 0]-Xp[1, 1])/2)
Xpp = sp.simplify((Xp[0, 1]+Xp[1, 0])/2); Ypp = sp.simplify((Xp[1, 0]-Xp[0, 1])/(2*sp.I))
ch, sh = (k+1/k)/2, (k-1/k)/2
r3 = [sp.simplify(Tp-(ch*T+sh*Zc)), sp.simplify(Zp-(sh*T+ch*Zc)), sp.simplify(Xpp-X), sp.simplify(Ypp-Y),
      sp.simplify(Xp.det()-Xm.det())]
ok['B3'] = all(r == 0 for r in r3)
print('B3: boost residuals (t, z, x, y, det):', r3)

# ---- B4(a): cross ratio
def cr(p, q, r, s): return ((p-r)*(q-s))/((p-s)*(q-r))
w4 = mp.mpf(0)
for _ in range(100):
    A, B, C, Dd = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(4)]
    if abs(A*Dd-B*C) < mp.mpf('1e-3'): continue
    mob = lambda u: (A*u+B)/(C*u+Dd)
    pts = [mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(4)]
    w4 = max(w4, abs(cr(*map(mob, pts))/cr(*pts)-1))
ok['B4a'] = w4 < mp.mpf('1e-40')
print('B4(a): max cross-ratio change =', mp.nstr(w4, 3))

# ---- B4(b): Poincare ball distance centre -> tanh(eta/2) is eta
w4b = max(abs(2*mp.atanh(mp.tanh(e/2))-e) for e in [mp.mpf(x) for x in ('0.1', '1', '3', '7')])
ok['B4b'] = w4b < mp.mpf('1e-40')
print('B4(b): max |d_P - eta| =', mp.nstr(w4b, 3), '(an identity once rho = tanh(eta/2), SRA A2)')

# ---- B4(c): circle sky in t = tan(theta/2): C(0,1) -> C(0,1/k); height e^-eta, gamma = cosh(d_P)
s_ = sp.symbols('s', real=True)
cauchy = lambda x, g: g/(sp.pi*(x**2+g**2))
push = cauchy(k*s_, 1)*k            # density of s = t/k when t ~ C(0,1)
r4c = sp.simplify(push - cauchy(s_, 1/k))
dP = sp.log(k)                       # Poincare distance between i and i/k
r4c2 = sp.simplify(sp.cosh(dP) - (k+1/k)/2)
heights_equal_gamma = [mp.mpf(1)/mp.e**e for e in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)]]
gam = [mp.cosh(e) for e in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)]]
ok['B4c'] = (r4c == 0) and (sp.simplify(r4c2.rewrite(sp.exp)) == 0) and all(abs(h-g) > mp.mpf('0.01') for h, g in zip(heights_equal_gamma, gam))
print('B4(c): pushforward residual', r4c, '; cosh(d_P) - gamma =', sp.simplify(r4c2.rewrite(sp.exp)))
print('       heights e^-eta', [mp.nstr(h, 6) for h in heights_equal_gamma], 'against gamma', [mp.nstr(g, 6) for g in gam])

# ---- B4(d): KL(uniform circle || wrapped Cauchy rho = tanh(eta/2)) = 2 ln cosh(eta/2)
w4d = mp.mpf(0)
for e in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)]:
    rho = mp.tanh(e/2)
    wc = lambda th: (1-rho**2)/(2*mp.pi*(1+rho**2-2*rho*mp.cos(th)))
    kl = mp.quad(lambda th: (1/(2*mp.pi))*mp.log((1/(2*mp.pi))/wc(th)), [-mp.pi, 0, mp.pi])
    pred = 2*mp.log(mp.cosh(e/2))
    w4d = max(w4d, abs(kl/pred-1))
    print('       eta', mp.nstr(e, 3), 'KL', mp.nstr(kl, 20), 'pred', mp.nstr(pred, 20))
ok['B4d'] = w4d < mp.mpf('1e-30')
print('B4(d): max rel. err =', mp.nstr(w4d, 3))

# ---- B5: sphere KL, exploratory
print('B5: KL(uniform sphere || spherical Cauchy rho = tanh(eta/2))')
for e in [mp.mpf('0.1'), mp.mpf('0.3'), mp.mpf(1), mp.mpf(3)]:
    rho = mp.tanh(e/2)
    lf = lambda th: 2*mp.log((1-rho**2)/(1+rho**2-2*rho*mp.cos(th)))   # ln(4 pi f)
    kl = -mp.quad(lambda th: mp.sin(th)*lf(th), [0, mp.pi])/2
    print('       eta', mp.nstr(e, 3), 'KL', mp.nstr(kl, 15), 'KL/eta^2', mp.nstr(kl/e**2, 10),
          '4 ln cosh(eta/2)', mp.nstr(4*mp.log(mp.cosh(e/2)), 15))

# ---- B6 candidate 4: pseudorapidity of a uniform sky is logistic scale 1/2; median efficiency 3/4
fx = lambda x: mp.sech(x)**2/2
fisher = mp.quad(lambda x: (mp.diff(fx, x)**2)/fx(x), [-40, 0, 40])
medvar = 1/(4*fx(0)**2)
eff = (1/fisher)/medvar
print('B6.4: Fisher info', mp.nstr(fisher, 15), 'median var', mp.nstr(medvar, 6), 'efficiency', mp.nstr(eff, 15))
ok['B6_4_eff'] = abs(eff - mp.mpf(3)/4) < mp.mpf('1e-30')

print('\nSUMMARY', ok)
