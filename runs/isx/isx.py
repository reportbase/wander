# ISX run 1: the inverse square as a read and its exchange. Predictions in plans/isx-plan.md.
from fractions import Fraction as F
import mpmath as mp
mp.mp.dps = 50
out = []
def rep(code, ok, msg): out.append((code, ok, msg)); print(f"{code} {'ok' if ok else 'KILL'}  {msg}")
L = mp.mpf(1)

# X1 disc by quadrature
worst = 0
for s in [mp.mpf(1)/10, mp.mpf(1)/3, 1, 3, 10]:
    a, d = mp.mpf(1), mp.mpf(s)
    q = mp.quad(lambda r: L*d**2*2*mp.pi*r/(r**2+d**2)**2, [0, a])
    worst = max(worst, abs(q - mp.pi*L*a**2/(a**2+d**2)))
rep('X1', worst < mp.mpf(10)**-30, f"quadrature vs pi L a^2/(a^2+d^2), worst {mp.nstr(worst,3)}")

# X2 exact exchange over rationals; share = h^2 of slope s
share = lambda s: 1/(1+s*s)
rats = [F(p,q) for p in range(1,7) for q in range(1,6)][:30]
okx = all(share(s)+share(1/s) == 1 for s in rats)
okh = all(share(s) == (1/(1+s*s)) for s in rats)  # h^2 with h=1/sqrt(1+s^2): h^2 = 1/(1+s^2)
rep('X2', okx and okh, f"E(s)+E(1/s)=piL exactly on {len(rats)} rationals; share = h^2 of slope s")

# X3 corner and slope
sig = lambda s: -2*s*s/(1+s*s)
ok3 = share(F(1)) == F(1,2) and sig(F(1)) == -1 and all(sig(s)+sig(1/s) == -2 for s in rats)
# slope derivative check numerically
num = mp.diff(lambda x: mp.log(1/(1+mp.e**(2*x))), mp.log(3))
ok3 = ok3 and abs(num - (-2*9/mp.mpf(10))) < mp.mpf(10)**-40
rep('X3', ok3, "share 1/2 at s=1, sigma(1)=-1, sigma(s)+sigma(1/s)=-2, d lnE/d ln s checked at s=3")

# X4 charts
s = mp.mpf(1000)
far = s**2*share(s); near_s = mp.mpf(1)/1000
ok4 = abs((1-far) - 1/(1+s**2)) < mp.mpf(10)**-40 and abs(1-far) < 1e-6 and abs((1-share(near_s)) - near_s**2/(1+near_s**2)) < mp.mpf(10)**-40
rep('X4', ok4, f"far: 1 - s^2 E/piL = {mp.nstr(1-far,4)} = 1/(1+s^2); near: 1 - E/piL = s^2/(1+s^2)")

# X5 scale test
Ead = lambda a, d: F(1)*a*a/(a*a+d*d)
ok5 = all(Ead(F(k)*3, F(k)*5) == Ead(F(3), F(5)) for k in [F(1,1000), F(7), F(10**6)])
a0, d0 = F(1), F(20)
ok5b = all(Ead(a0, d0*k)/Ead(a0, d0) == (1+(d0/a0)**2)/(1+(k*d0/a0)**2) for k in [F(2), F(10), F(1000)])
rep('X5', ok5 and ok5b, "(ka,kd) leaves E exactly; a fixed, d->kd gives (1+s^2)/(1+k^2 s^2), 1/k^2 only far off")

# X6 coaxial discs view factors
def F12(r1, r2, d):
    R1, R2 = r1/d, r2/d; X = 1 + (1+R2**2)/R1**2
    return (X - mp.sqrt(X**2 - 4*(R2/R1)**2))/2
geos = [(1,1,1),(1,2,mp.mpf('0.5')),(3,1,2),(mp.mpf('0.2'),5,1),(2,3,7)]
wr = max(abs(mp.pi*r1**2*F12(r1,r2,d) - mp.pi*r2**2*F12(r2,r1,d)) for r1,r2,d in [(mp.mpf(a),mp.mpf(b),mp.mpf(c)) for a,b,c in geos])
r1, r2 = mp.mpf(1), mp.mpf(2); d = 2000*r2
A1, A2 = mp.pi*r1**2, mp.pi*r2**2
prod = F12(r1,r2,d)*F12(r2,r1,d)*(mp.pi*d**2)**2/(A1*A2)
rep('X6', wr < mp.mpf(10)**-30 and abs(prod-1) < 1e-5, f"reciprocity worst {mp.nstr(wr,3)}; far product {mp.nstr(prod,12)}")
# post hoc: F12 by direct quadrature at (1,1,1), lower precision
mp.mp.dps = 15
def ptF(rho, r2, d):
    f = lambda q, ph: q*d**2/(mp.pi*(d**2 + q**2 + rho**2 - 2*q*rho*mp.cos(ph))**2)
    return mp.quad(f, [0, r2], [0, 2*mp.pi])
qF = mp.quad(lambda rho: ptF(rho, 1, 1)*2*rho, [0, 1])  # (1/A1) * int dA1 with A1 = pi -> 2 rho drho
mp.mp.dps = 50
print(f"  post hoc: F12(1,1,1) quadrature {mp.nstr(qF,12)} closed form {mp.nstr(F12(mp.mpf(1),mp.mpf(1),mp.mpf(1)),12)}")

# X7 square plate
def Esq(u):  # E/L for square half-side u at unit distance; quadrant closed form x4
    t = u/mp.sqrt(1+u*u)
    return 4*2*(u/(2*mp.sqrt(1+u*u)))*mp.atan(t)
qchk = mp.quad(lambda x, y: 1/(1+x*x+y*y)**2, [-2, 2], [-2, 2])
print(f"  square closed form check at u=2: {mp.nstr(Esq(2)-qchk, 3)}")
vals = [Esq(1/s) + Esq(s) for s in [mp.mpf(1)/10, mp.mpf(1)/3, 1, 3, 10]]  # E at s plus at 1/s, s=d/b, u=b/d
spread = max(vals)-min(vals)
rep('X7', spread > 1e-3, f"square E(s)+E(1/s) over s in [1/10,10]: {[mp.nstr(v/mp.pi,8) for v in vals]} (x pi L), spread {mp.nstr(spread,4)}")

# X8 sphere
w8 = 0
for dd in [1, mp.mpf('1.5'), 3, 10, 100]:
    al = mp.asin(1/mp.mpf(dd))
    q = mp.quad(lambda th: 2*mp.pi*L*mp.cos(th)*mp.sin(th), [0, al])
    w8 = max(w8, abs(q/mp.pi - 1/mp.mpf(dd)**2))
rep('X8', w8 < mp.mpf(10)**-30, f"sphere E/piL = (a/d)^2 for d>=a, worst {mp.nstr(w8,3)}")
print("killed:", [c for c,ok,_ in out if not ok] or "none")
