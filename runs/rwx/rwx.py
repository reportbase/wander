# RWX run 1: reads, writes and exchanges in physical situations. Predictions in plans/rwx-plan.md.
from fractions import Fraction as F
import mpmath as mp, numpy as np
from scipy.integrate import solve_ivp
mp.mp.dps = 50
res = []
def rep(c, ok, m): res.append((c, ok)); print(f"{c} {'ok' if ok else 'KILL'}  {m}")
tiny = mp.mpf(10)**-40
ks = [mp.mpf(x) for x in ['0.01','0.2','0.5','1','2','3.7','10','250']]

# R1: RC divider from impedances
w1 = 0; ok_sw = True
for s in ks:
    R, C = mp.mpf(3), s/3  # w = 1, so s = wRC
    Zc = 1/(1j*C); Hl = Zc/(R+Zc); Hh = R/(R+Zc)
    sl, sh = abs(Hl)**2, abs(Hh)**2
    phi = -mp.arg(Hl)
    w1 = max(w1, abs(sl-1/(1+s**2)), abs(sh-s**2/(1+s**2)), abs(sl+sh-1), abs(sl-mp.cos(phi)**2), abs(mp.tan(phi)-s))
    # exchange: low at s equals high at 1/s
    C2_ = (1/s)/3; Zc2 = 1/(1j*C2_); w1 = max(w1, abs(sl - abs(R/(R+Zc2))**2))
cross = abs(abs((1/(1j*mp.mpf(1)/3))/(3+1/(1j*mp.mpf(1)/3)))**2 - mp.mpf(1)/2)
rep('R1', w1 < tiny and cross < tiny, f"RC: shares 1/(1+s^2), s^2/(1+s^2), sum 1, s<->1/s swaps, cos^2(phase), tan phase = s; worst {mp.nstr(w1,3)}; crossover 1/2 at s=1")

# R2: level family from physics
lev = lambda k: 4*k/(1+k)**2
def coll(m1, m2):  # 1D elastic, m2 at rest, v=1
    v1p = (m1-m2)/(m1+m2); v2p = 2*m1/(m1+m2)
    assert m1*1 == m1*v1p + m2*v2p and m1 == m1*v1p**2 + m2*v2p**2
    return m2*v2p**2/m1
def match(Rs, RL):
    I = F(1)/(Rs+RL); return I*I*RL / (F(1)/(4*Rs))
def fresnel(n1, n2):  # solve Ei + Er = Et, n1(Ei - Er) = n2 Et, Ei = 1
    # from the two: Et = 1 + Er; n1 - n1 Er = n2 + n2 Er -> Er = (n1-n2)/(n1+n2)
    Er = (n1-n2)/(n1+n2); Et = 1+Er
    assert n1*(1-Er) == n2*Et
    return (n2/n1)*Et**2, Er**2
rk = [F(1,100), F(1,5), F(1,2), F(1), F(2), F(37,10), F(10), F(250)]
ok2 = True
for k in rk:
    ok2 &= coll(k, F(1)) == lev(k) == coll(F(1), 1/k) == lev(1/k)
    ok2 &= match(F(1), k) == lev(k)
    T, Rr = fresnel(F(1), k); ok2 &= T == lev(k) and T + Rr == 1 and fresnel(k, F(1))[0] == T
w2 = max(max(abs(mp.sech(mp.log(k)/2)**2 - 4*k/(1+k)**2), abs(mp.tanh(mp.log(k)/2)**2 - ((1-k)/(1+k))**2)) for k in ks)
slope = mp.diff(lambda x: mp.sech(x/2)**2, 0)
rep('R2', ok2 and w2 < tiny and abs(slope) < tiny and lev(F(1)) == 1,
    f"collision, matching, Fresnel all exactly 4k/(1+k)^2 (fractions, {len(rk)} ratios), k<->1/k unchanged, = sech^2(ln k/2), R = tanh^2, R+T=1, 1 at k=1, slope 0")

# R3: one share, two charts; RLC
w3 = max(abs(mp.sech(mp.log(k)/2)**2 - 1/(1+mp.sinh(mp.log(k)/2)**2)) for k in ks)
w3 = max(w3, max(abs(mp.sinh(mp.log(k)/2) - (mp.sqrt(k)-1/mp.sqrt(k))/2) for k in ks))
L_, C_, R_ = mp.mpf(2), mp.mpf('0.125'), mp.mpf('0.3'); w0 = 1/mp.sqrt(L_*C_); Q = w0*L_/R_
wr = 0
for x in ks:
    w = w0*x
    Z = R_ + 1j*(w*L_ - 1/(w*C_)); P = abs(1/Z)**2*R_; Pm = 1/R_
    s = Q*(w/w0 - w0/w)
    wb = w0**2/w; Zb = R_ + 1j*(wb*L_ - 1/(wb*C_)); Pb = abs(1/Zb)**2*R_
    wr = max(wr, abs(P/Pm - 1/(1+s**2)), abs(s - 2*Q*mp.sinh(mp.log(x))), abs(P-Pb), abs(mp.tan(mp.arg(Z)) - s))
half = [w0*(mp.sqrt(1+1/(4*Q**2)) + sg/(2*Q)) for sg in (-1, 1)]
hp = max(abs(abs(1/(R_+1j*(w*L_-1/(w*C_))))**2*R_*R_ - mp.mpf(1)/2) for w in half)
rep('R3', w3 < tiny and wr < tiny and hp < tiny,
    f"sech^2 = 1/(1+sinh^2) on s = (sqrt k - 1/sqrt k)/2; RLC P/Pmax = 1/(1+s^2), s = 2Q sinh(ln w/w0), w<->w0^2/w unchanged, tan phase = s; half power at s=+-1; worst {mp.nstr(max(w3,wr,hp),3)}")

# R4: scaling
ok4 = True
for kk in [F(1,1000), F(7), F(10**6)]:
    ok4 &= coll(3*kk, 5*kk) == coll(F(3), F(5)) and match(2*kk, 9*kk) == match(F(2), F(9)) and fresnel(kk, F(3,2)*kk) == fresnel(F(1), F(3,2))
# RC: R->kR, C->C/k
for kk in [mp.mpf('0.001'), 7, mp.mpf(10)**6]:
    R, C = 3*kk, mp.mpf('0.4')/kk; Zc = 1/(1j*C)
    ok4 &= abs(abs(Zc/(R+Zc))**2 - 1/(1+mp.mpf('1.2')**2)) < tiny
rep('R4', ok4, "scaling each pair by k (masses, resistances, indices, R and C as kR, C/k) moves no share")

# R5: pendulum and Kepler by integration
def pend_T(l, th0, g=9.81):
    f = lambda t, y: [y[1], -(g/l)*np.sin(y[0])]
    ev = lambda t, y: y[0]; ev.terminal = True; ev.direction = -1
    sol = solve_ivp(f, [0, 1e3], [th0, 0], method='DOP853', rtol=1e-12, atol=1e-14, events=ev)
    return 4*sol.t_events[0][0]
ok5 = True; rows = []
for th0 in [0.1, 1.0, 2.5]:
    vals = [pend_T(l, th0)*np.sqrt(9.81/l) for l in [1, 7, 100]]
    exact = float(2*mp.pi/mp.agm(1, mp.cos(th0/2)))
    ok5 &= max(vals)-min(vals) < 1e-9 and abs(vals[0]-exact) < 1e-9
    rows.append(f"th0={th0}: T*sqrt(g/l)={vals[0]:.10f} (exact {exact:.10f})")
    # write: counted period with g carried in gives l
    T7 = pend_T(7, th0); l_written = 9.81*(T7/exact)**2; ok5 &= abs(l_written-7) < 1e-8
def kep_T(a, e, GM=1.0):
    r0 = a*(1-e); v0 = np.sqrt(GM*(1+e)/(a*(1-e)))
    f = lambda t, y: [y[2], y[3], -GM*y[0]/np.hypot(y[0],y[1])**3, -GM*y[1]/np.hypot(y[0],y[1])**3]
    ev = lambda t, y: y[1]; ev.terminal = True; ev.direction = -1
    sol = solve_ivp(f, [0, 1e12], [r0, 0, 0, v0], method='DOP853', rtol=1e-13, atol=1e-16*a, events=ev)
    yf = sol.y_events[0][0]; ea = -np.hypot(yf[0], yf[1])  # aphelion distance
    return 2*sol.t_events[0][0], (abs(ea) - r0)/(abs(ea) + r0)
worst7 = 0; ecc = 0
for e in [0.0, 0.5, 0.9]:
    for a in [1, 10, 1000]:
        T, e_back = kep_T(a, e)
        worst7 = max(worst7, abs(T*np.sqrt(1/a**3) - 2*np.pi)); ecc = max(ecc, abs(e_back - e))
ok5 &= worst7 < 1e-8 and ecc < 1e-9
rep('R5', ok5, "; ".join(rows) + f"; Kepler T*sqrt(GM/a^3)-2pi worst {worst7:.1e}, e read back worst {ecc:.1e}; a counted period with g carried in writes l=7 to 1e-8")

ok6 = all(ok for _, ok in res)
rep('R6', ok6, "C1 turn's share (crossover); C2-C5 level's share (stationary corner), one share on the sinh chart; C6, C7 counts that write with g, GM carried in")
print("killed:", [c for c, ok in res if not ok] or "none")
