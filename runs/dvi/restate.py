import mpmath as mp; mp.mp.dps = 50
S = mp.sqrt
def R(x): return mp.mpf(x)
def N(n, reason): return dict(n=n, verdict='none', notation=False, reason=reason)
def T(n, reason, restated, orig, new, points): return dict(n=n, verdict='notation', notation=True, reason=reason, restated=restated, orig=orig, new=new, points=points)
P3 = [R('0.3'), R('1.7'), R('5')]
def h(s): return 1/S(1+s*s)
def v(s): return s/S(1+s*s)

# ---- helpers. Directions are given by their half-slope t; the original's angle is 2*atan(t).
# Original side (may use transcendental functions):
def A(t): return 2*mp.atan(t)
def sph_o(r, th, ph): return [r*mp.sin(th)*mp.cos(ph), r*mp.sin(th)*mp.sin(ph), r*mp.cos(th)]
def units_o(th, ph):
    st, ct, sp, cp = mp.sin(th), mp.cos(th), mp.sin(ph), mp.cos(ph)
    return [st*cp, st*sp, ct], [ct*cp, ct*sp, -st], [-sp, cp, 0]
def jac_o(F, r, th, ph):
    return [[mp.diff(lambda a: F(a, th, ph)[i], r), mp.diff(lambda a: F(r, a, ph)[i], th),
             mp.diff(lambda a: F(r, th, a)[i], ph)] for i in range(3)]
# Restatement side (rational operations and square roots, derivatives in the half-slope):
def Hc(t): return (1-t*t)/(1+t*t)      # first share of the direction with half-slope t
def Hs(t): return 2*t/(1+t*t)          # second share
def D(t): return (1+t*t)/2             # turn per half-slope: d/d(turn) = D(t) d/dt
def W(t): return (1+1j*t)**2/(1+t*t)   # landing point h + i v
def sph_n(r, t, u): return [r*Hs(t)*Hc(u), r*Hs(t)*Hs(u), r*Hc(t)]
def units_n(t, u):
    st, ct, sp, cp = Hs(t), Hc(t), Hs(u), Hc(u)
    return [st*cp, st*sp, ct], [ct*cp, ct*sp, -st], [-sp, cp, 0]
def jac_n(F, r, t, u):
    return [[mp.diff(lambda a: F(a, t, u)[i], r), D(t)*mp.diff(lambda a: F(r, a, u)[i], t),
             D(u)*mp.diff(lambda a: F(r, t, a)[i], u)] for i in range(3)]
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def sc(k, a): return [k*x for x in a]
def add(*vs): return [sum(c) for c in zip(*vs)]
def qmul(p, q):
    w1, x1, y1, z1 = p; w2, x2, y2, z2 = q
    return [w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2, w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2]
def flat(m): return [x for row in m for x in row]
def f3(x, y, z): return x**3*y + y*z**2 - 2*x*z + x*y*z + z**3
def F3(x, y, z): return [x*y + z**2, y*z - x**3, x*z*y + y**2]
def grad3(f, X): return [mp.diff(f, X, (1, 0, 0)), mp.diff(f, X, (0, 1, 0)), mp.diff(f, X, (0, 0, 1))]
AX = [R(1)/3, R(2)/3, R(2)/3]; BX = [R(2)/3, R(-1)/3, R(2)/3]
PS = [(R('1.3'), R('0.4'), R('0.7')), (R('2'), R('1.5'), R('-0.6')), (R('0.8'), R('3'), R('2.2'))]
PQ = [(R('0.4'), R('1.3')), (R('2'), R('0.7')), (R('3'), R('5'))]
DUM = [1, 2, 3]
TAU = [R('0.3'), R('1.1'), R('-0.7')]
def rr(tau): return 1 + tau*tau/2 + tau/5
def TT(tau): return R('0.4') + tau/2 + tau*tau/3
def UU(tau): return R('-0.3') + tau + tau**3/4
def rate_n(F, tau):  # turn rate and its derivative from the half-slope path F
    f, f1, f2 = F(tau), mp.diff(F, tau), mp.diff(F, tau, 2)
    return 2*f1/(1+f*f), 2*f2/(1+f*f) - 4*f*f1*f1/(1+f*f)**2

# 1
def o1(p):
    x, y, z = p; rho = S(x*x+y*y); r = S(x*x+y*y+z*z)
    t1 = mp.acos(z/r)
    t2 = mp.atan(rho/z) if z > 0 else (mp.pi + mp.atan(rho/z) if z < 0 else mp.pi/2)
    return [mp.cos(t1), mp.sin(t1), mp.cos(t2), mp.sin(t2)]
def n1(p):
    x, y, z = p; rho = S(x*x+y*y); r = S(x*x+y*y+z*z)
    return [z/r, rho/r, z/r, rho/r]
# 2
def o2(p):
    x, y = p; rho = S(x*x+y*y)
    f1 = mp.sign(y)*mp.acos(x/rho)
    if x > 0: f2 = mp.atan(y/x)
    elif x < 0 and y >= 0: f2 = mp.atan(y/x) + mp.pi
    elif x < 0: f2 = mp.atan(y/x) - mp.pi
    else: f2 = mp.pi/2 if y > 0 else -mp.pi/2
    return [mp.cos(f1), mp.sin(f1), mp.cos(f2), mp.sin(f2)]
def n2(p):
    x, y = p; rho = S(x*x+y*y); return [x/rho, y/rho, x/rho, y/rho]
P2 = [(R(1), R(2)), (R(-1), R(2)), (R(-1), R(-2)), (R(0), R(3)), (R(0), R(-3))]
# 3
def o3(p): r, t, u = p; return sph_o(r, A(t), A(u))
def n3(p): r, t, u = p; return sph_n(r, t, u)
# 4
def o4(p):
    rho, z, u = p; r = S(rho*rho+z*z); a1 = mp.atan(rho/z); a2 = mp.acos(z/r)
    return [r, mp.cos(a1), mp.sin(a1), mp.cos(a2), mp.sin(a2), mp.cos(A(u)), mp.sin(A(u))]
def n4(p):
    rho, z, u = p; r = S(rho*rho+z*z); return [r, z/r, rho/r, z/r, rho/r, Hc(u), Hs(u)]
P4 = [(R('1.2'), R('0.5'), R('0.3')), (R('3'), R('2'), R('-1')), (R('0.4'), R('7'), R('2'))]
# 5
def o5(p): r, t, u = p; th = A(t); return [r*mp.sin(th), mp.cos(A(u)), mp.sin(A(u)), r*mp.cos(th)]
def n5(p): r, t, u = p; return [r*Hs(t), Hc(u), Hs(u), r*Hc(t)]
# 6
P6 = [(R('1.3'), R('0.4'), R('0.7'), R(2), R(3), R(5)), (R('2'), R('1.5'), R('-0.6'), R('0.5'), R(1), R(4)),
      (R('0.8'), R('3'), R('2.2'), R(7), R('1.5'), R('0.3'))]
def o6(p):
    r, t, u, a, b, c = p; th, ph = A(t), A(u)
    x, y, z = r*mp.sin(th)*mp.cos(ph)/S(a), r*mp.sin(th)*mp.sin(ph)/S(b), r*mp.cos(th)/S(c)
    return [x, y, z, a*x*x+b*y*y+c*z*z, r*r]
def n6(p):
    r, t, u, a, b, c = p
    x, y, z = r*Hs(t)*Hc(u)/S(a), r*Hs(t)*Hs(u)/S(b), r*Hc(t)/S(c)
    return [x, y, z, a*x*x+b*y*y+c*z*z, r*r]
# 7
def o7(p):
    r, t, u, a, b, c = p; th, ph = A(t), A(u)
    F = lambda rr_, th_, ph_: [rr_*mp.sin(th_)*mp.cos(ph_)/S(a), rr_*mp.sin(th_)*mp.sin(ph_)/S(b), rr_*mp.cos(th_)/S(c)]
    return [abs(mp.det(mp.matrix(jac_o(F, r, th, ph)))), r*r*mp.sin(th)/S(a*b*c)]
def n7(p):
    r, t, u, a, b, c = p
    F = lambda rr_, t_, u_: [rr_*Hs(t_)*Hc(u_)/S(a), rr_*Hs(t_)*Hs(u_)/S(b), rr_*Hc(t_)/S(c)]
    return [abs(mp.det(mp.matrix(jac_n(F, r, t, u)))), r*r*Hs(t)/S(a*b*c)]
# 8
def o8(p): t, u = p; return flat(units_o(A(t), A(u)))
def n8(p): t, u = p; return flat(units_n(t, u))
# 9
def o9(p):
    t, u = p; rh, thh, phh = units_o(A(t), A(u)); M = [[rh[i], thh[i], phh[i]] for i in range(3)]
    return flat(M) + [dot(M[i], [rh[j], thh[j], phh[j]]) for i in range(3) for j in range(3)]
def n9(p):
    t, u = p; rh, thh, phh = units_n(t, u); M = [[rh[i], thh[i], phh[i]] for i in range(3)]
    return flat(M) + [dot(M[i], [rh[j], thh[j], phh[j]]) for i in range(3) for j in range(3)]
# 10
def o10(p):
    r, t, u = p; th, ph = A(t), A(u); st, ct, sp, cp = mp.sin(th), mp.cos(th), mp.sin(ph), mp.cos(ph)
    return flat(jac_o(sph_o, r, th, ph)) + [st*cp, r*ct*cp, -r*st*sp, st*sp, r*ct*sp, r*st*cp, ct, -r*st, 0]
def n10(p):
    r, t, u = p; st, ct, sp, cp = Hs(t), Hc(t), Hs(u), Hc(u)
    return flat(jac_n(sph_n, r, t, u)) + [st*cp, r*ct*cp, -r*st*sp, st*sp, r*ct*sp, r*st*cp, ct, -r*st, 0]
# 11
def o11(p): r, t, u = p; th, ph = A(t), A(u); return [abs(mp.det(mp.matrix(jac_o(sph_o, r, th, ph)))), r*r*mp.sin(th)]
def n11(p): r, t, u = p; return [abs(mp.det(mp.matrix(jac_n(sph_n, r, t, u)))), r*r*Hs(t)]
# 12
def o12(p):
    r, t, u = p; th, ph = A(t), A(u); G = lambda a, b, c: f3(*sph_o(a, b, c))
    fr, fth, fph = mp.diff(lambda a: G(a, th, ph), r), mp.diff(lambda a: G(r, a, ph), th), mp.diff(lambda a: G(r, th, a), ph)
    rh, thh, phh = units_o(th, ph)
    return grad3(f3, sph_o(r, th, ph)) + add(sc(fr, rh), sc(fth/r, thh), sc(fph/(r*mp.sin(th)), phh))
def n12(p):
    r, t, u = p; G = lambda a, b, c: f3(*sph_n(a, b, c))
    fr, fth, fph = mp.diff(lambda a: G(a, t, u), r), D(t)*mp.diff(lambda a: G(r, a, u), t), D(u)*mp.diff(lambda a: G(r, t, a), u)
    rh, thh, phh = units_n(t, u)
    return grad3(f3, sph_n(r, t, u)) + add(sc(fr, rh), sc(fth/r, thh), sc(fph/(r*Hs(t)), phh))
# 13
def lap3(f, X): return mp.diff(f, X, (2, 0, 0)) + mp.diff(f, X, (0, 2, 0)) + mp.diff(f, X, (0, 0, 2))
def o13(p):
    r, t, u = p; th, ph = A(t), A(u); G = lambda a, b, c: f3(*sph_o(a, b, c)); st, ct = mp.sin(th), mp.cos(th)
    fr, frr = mp.diff(lambda a: G(a, th, ph), r), mp.diff(lambda a: G(a, th, ph), r, 2)
    fth, fthth = mp.diff(lambda a: G(r, a, ph), th), mp.diff(lambda a: G(r, a, ph), th, 2)
    fphph = mp.diff(lambda a: G(r, th, a), ph, 2)
    ang = (ct*fth + st*fthth)/(r*r*st) + fphph/(r*r*st*st)
    return [lap3(f3, sph_o(r, th, ph)), (2*r*fr + r*r*frr)/(r*r) + ang, frr + 2*fr/r + ang]
def n13(p):
    r, t, u = p; G = lambda a, b, c: f3(*sph_n(a, b, c)); st = Hs(t)
    fr, frr = mp.diff(lambda a: G(a, t, u), r), mp.diff(lambda a: G(a, t, u), r, 2)
    ft, ftt = mp.diff(lambda a: G(r, a, u), t), mp.diff(lambda a: G(r, a, u), t, 2)
    fu, fuu = mp.diff(lambda a: G(r, t, a), u), mp.diff(lambda a: G(r, t, a), u, 2)
    ang = D(t)*(ft + t*ftt)/(r*r*st) + D(u)*(u*fu + D(u)*fuu)/(r*r*st*st)
    return [lap3(f3, sph_n(r, t, u)), (2*r*fr + r*r*frr)/(r*r) + ang, frr + 2*fr/r + ang]
# 14
def div3(X): return mp.diff(lambda x, y, z: F3(x, y, z)[0], X, (1, 0, 0)) + mp.diff(lambda x, y, z: F3(x, y, z)[1], X, (0, 1, 0)) + mp.diff(lambda x, y, z: F3(x, y, z)[2], X, (0, 0, 1))
def o14(p):
    r, t, u = p; th, ph = A(t), A(u)
    def comp(a, b, c, k): return dot(F3(*sph_o(a, b, c)), units_o(b, c)[k])
    t1 = mp.diff(lambda a: a*a*comp(a, th, ph, 0), r)/(r*r)
    t2 = mp.diff(lambda a: mp.sin(a)*comp(r, a, ph, 1), th)/(r*mp.sin(th))
    t3 = mp.diff(lambda a: comp(r, th, a, 2), ph)/(r*mp.sin(th))
    return [div3(sph_o(r, th, ph)), t1 + t2 + t3]
def n14(p):
    r, t, u = p
    def comp(a, b, c, k): return dot(F3(*sph_n(a, b, c)), units_n(b, c)[k])
    t1 = mp.diff(lambda a: a*a*comp(a, t, u, 0), r)/(r*r)
    t2 = D(t)*mp.diff(lambda a: Hs(a)*comp(r, a, u, 1), t)/(r*Hs(t))
    t3 = D(u)*mp.diff(lambda a: comp(r, t, a, 2), u)/(r*Hs(t))
    return [div3(sph_n(r, t, u)), t1 + t2 + t3]
# 15
P15 = [(R('1.3'), R('0.4'), R('0.7'), R('2'), R('1.5'), R('-0.6')), (R('0.8'), R('3'), R('2.2'), R('1.1'), R('0.2'), R('5')),
       (R('4'), R('0.9'), R('-2'), R('0.5'), R('2.5'), R('0.1'))]
def o15(p):
    r, t, u, r2, t2, u2 = p; th, ph, th2, ph2 = A(t), A(u), A(t2), A(u2)
    X, Y = sph_o(r, th, ph), sph_o(r2, th2, ph2)
    return [S(sum((a-b)**2 for a, b in zip(X, Y))),
            S(r*r + r2*r2 - 2*r*r2*(mp.sin(th)*mp.sin(th2)*mp.cos(ph-ph2) + mp.cos(th)*mp.cos(th2)))]
def n15(p):
    r, t, u, r2, t2, u2 = p; X, Y = sph_n(r, t, u), sph_n(r2, t2, u2)
    return [S(sum((a-b)**2 for a, b in zip(X, Y))),
            S(r*r + r2*r2 - 2*r*r2*(Hs(t)*Hs(t2)*(Hc(u)*Hc(u2)+Hs(u)*Hs(u2)) + Hc(t)*Hc(t2)))]
# 16
def o16(p):
    t, u, t2, u2 = p; th, ph, th2, ph2 = A(t), A(u), A(t2), A(u2)
    g = mp.acos(dot(units_o(th, ph)[0], units_o(th2, ph2)[0]))
    c, s = mp.cos, mp.sin
    return [c(g), c(th)*c(th2) + s(th)*s(th2)*(c(ph)*c(ph2)+s(ph)*s(ph2)), c(th)*c(th2) + s(th)*s(th2)*c(ph-ph2)]
def n16(p):
    t, u, t2, u2 = p
    lhs = dot(units_n(t, u)[0], units_n(t2, u2)[0])
    rhs = Hc(t)*Hc(t2) + Hs(t)*Hs(t2)*(Hc(u)*Hc(u2)+Hs(u)*Hs(u2))
    return [lhs, rhs, rhs]
P16 = [(R('0.4'), R('0.7'), R('1.5'), R('-0.6')), (R('3'), R('2.2'), R('0.2'), R('5')), (R('0.9'), R('-2'), R('2.5'), R('0.1'))]
# 17
def o17(tau):
    th = lambda x: A(TT(x)); ph = lambda x: A(UU(x))
    r, r1, r2 = rr(tau), mp.diff(rr, tau), mp.diff(rr, tau, 2)
    a, a1, a2 = th(tau), mp.diff(th, tau), mp.diff(th, tau, 2)
    b, b1, b2 = ph(tau), mp.diff(ph, tau), mp.diff(ph, tau, 2)
    st, ct = mp.sin(a), mp.cos(a)
    acc = [mp.diff(lambda x: sph_o(rr(x), th(x), ph(x))[i], tau, 2) for i in range(3)]
    U = units_o(a, b)
    return [dot(acc, U[k]) for k in range(3)] + [r2 - r*a1**2 - r*b1**2*st**2, r*a2 + 2*r1*a1 - r*b1**2*st*ct,
                                                r*b2*st + 2*r1*b1*st + 2*r*a1*b1*ct]
def n17(tau):
    r, r1, r2 = rr(tau), mp.diff(rr, tau), mp.diff(rr, tau, 2)
    a1, a2 = rate_n(TT, tau); b1, b2 = rate_n(UU, tau)
    st, ct = Hs(TT(tau)), Hc(TT(tau))
    acc = [mp.diff(lambda x: sph_n(rr(x), TT(x), UU(x))[i], tau, 2) for i in range(3)]
    U = units_n(TT(tau), UU(tau))
    return [dot(acc, U[k]) for k in range(3)] + [r2 - r*a1**2 - r*b1**2*st**2, r*a2 + 2*r1*a1 - r*b1**2*st*ct,
                                                r*b2*st + 2*r1*b1*st + 2*r*a1*b1*ct]
# 18
MM = R(3)
def o18(tau):
    th = lambda x: A(TT(x)); ph = lambda x: A(UU(x))
    X = sph_o(rr(tau), th(tau), ph(tau)); V = [mp.diff(lambda x: sph_o(rr(x), th(x), ph(x))[i], tau) for i in range(3)]
    a, a1, b1 = th(tau), mp.diff(th, tau), mp.diff(ph, tau)
    _, thh, phh = units_o(a, ph(tau))
    return sc(MM, cross(X, V)) + sc(MM*rr(tau)**2, add(sc(-b1*mp.sin(a), thh), sc(a1, phh)))
def n18(tau):
    X = sph_n(rr(tau), TT(tau), UU(tau)); V = [mp.diff(lambda x: sph_n(rr(x), TT(x), UU(x))[i], tau) for i in range(3)]
    a1, _ = rate_n(TT, tau); b1, _ = rate_n(UU, tau)
    _, thh, phh = units_n(TT(tau), UU(tau))
    return sc(MM, cross(X, V)) + sc(MM*rr(tau)**2, add(sc(-b1*Hs(TT(tau)), thh), sc(a1, phh)))
# 19, 37, 46
PP = [(R('1.3'), R('0.4')), (R('2'), R('-1.5')), (R('0.8'), R('3'))]
def o19(p): r, t = p; f = A(t); return [r*mp.cos(f), r*mp.sin(f)]
def n19(p): r, t = p; return [r*Hc(t), r*Hs(t)]
def o37(t): f = A(t); return [mp.cos(f), mp.sin(f)]
def n37(t): return [Hc(t), Hs(t)]
def o46(p): r, t, z = p; f = A(t); return [r*mp.cos(f), r*mp.sin(f), z]
def n46(p): r, t, z = p; return [r*Hc(t), r*Hs(t), z]
# 20
def o20(p):
    x, y = p
    if x > 0: f = mp.atan(y/x)
    elif x < 0 and y >= 0: f = mp.atan(y/x) + mp.pi
    elif x < 0: f = mp.atan(y/x) - mp.pi
    else: f = mp.pi/2 if y > 0 else -mp.pi/2
    return [mp.cos(f), mp.sin(f)]
def n20(p): x, y = p; r = S(x*x+y*y); return [x/r, y/r]
P20 = [(R(1), R(2)), (R(-1), R(2)), (R(-2), R(0)), (R(-1), R(-2)), (R(0), R(3)), (R(0), R(-3))]
# 21
def o21(p):
    x, y = p; r = S(x*x+y*y); f = mp.acos(x/r) if y >= 0 else -mp.acos(x/r); return [mp.cos(f), mp.sin(f)]
def n21(p): x, y = p; r = S(x*x+y*y); return [x/r, y/r]
P21 = [(R(1), R(2)), (R(-1), R(-2)), (R(3), R(0)), (R(-2), R(1))]
# 22, 23
def o22(p): r, t = p; f = A(t); return [r*(mp.cos(f) + 1j*mp.sin(f)), r*mp.expj(f)]
def n22(p): r, t = p; return [r*W(t), r*W(t)]
P23 = [(R('1.3'), R('0.4'), R('2'), R('-1.5')), (R('0.8'), R('3'), R('1.1'), R('0.2')), (R('4'), R('0.9'), R('0.5'), R('2.5'))]
def o23(p): r0, t0, r1, t1 = p; return [r0*mp.expj(A(t0))*r1*mp.expj(A(t1)), r0*r1*mp.expj(A(t0)+A(t1))]
def n23(p): r0, t0, r1, t1 = p; return [r0*W(t0)*r1*W(t1), r0*r1*W((t0+t1)/(1-t0*t1))]
# 26
def o26(t): return mp.sin(6*A(t)) + 2
def n26(t): c, s = Hc(t), Hs(t); return 6*c**5*s - 20*c**3*s**3 + 6*c*s**5 + 2
# 27
def o27(t):
    rf = lambda f: 2 + mp.sin(f) + mp.cos(2*f); f = A(t); return [rf(mp.pi - f), rf(f)]
def n27(t):
    rf = lambda c, s: 2 + s + c*c - s*s
    return [rf(-Hc(t), Hs(t)), rf(Hc(t), Hs(t))]
# 28, 30
P28 = [(R('1.3'), R('0.4'), R('2'), R('-1.5'), R('0.7')), (R('0.8'), R('3'), R('1.1'), R('0.2'), R(2)), (R('4'), R('0.9'), R('0.5'), R('2.5'), R(3))]
def o28(p): r, t, r0, g, a = p; return [r*r - 2*r*r0*mp.cos(A(t)-A(g)) + r0*r0, a*a]
def n28(p): r, t, r0, g, a = p; return [r*r - 2*r*r0*(Hc(t)*Hc(g)+Hs(t)*Hs(g)) + r0*r0, a*a]
def o30(p): t, r0, g = p; return r0*mp.sec(A(t)-A(g))
def n30(p): t, r0, g = p; return r0/(Hc(t)*Hc(g)+Hs(t)*Hs(g))
P30 = [(R('0.4'), R('2'), R('0.7')), (R('3'), R('1.1'), R('2')), (R('0.9'), R('0.5'), R('-0.3'))]
# 29
def o29(m): f = mp.atan(m); return [mp.cos(f), mp.sin(f)]
def n29(m): return [h(m), v(m)]
# 32
def u2(x, y): return x**3*y - 2*x*y*y + y**3 + x
def o32(p):
    r, t = p; f = A(t); x, y = r*mp.cos(f), r*mp.sin(f); q = x*x+y*y
    G = lambda a, b: u2(a*mp.cos(b), a*mp.sin(b))
    ur, uf = mp.diff(lambda a: G(a, f), r), mp.diff(lambda b: G(r, b), f)
    ux, uy = mp.diff(u2, (x, y), (1, 0)), mp.diff(u2, (x, y), (0, 1))
    return [ux, ur*x/S(q) - uf*y/q, mp.cos(f)*ur - mp.sin(f)*uf/r, uy, ur*y/S(q) + uf*x/q, mp.sin(f)*ur + mp.cos(f)*uf/r]
def n32(p):
    r, t = p; x, y = r*Hc(t), r*Hs(t); q = x*x+y*y
    G = lambda a, b: u2(a*Hc(b), a*Hs(b))
    ur, uf = mp.diff(lambda a: G(a, t), r), D(t)*mp.diff(lambda b: G(r, b), t)
    ux, uy = mp.diff(u2, (x, y), (1, 0)), mp.diff(u2, (x, y), (0, 1))
    return [ux, ur*x/S(q) - uf*y/q, Hc(t)*ur - Hs(t)*uf/r, uy, ur*y/S(q) + uf*x/q, Hs(t)*ur + Hc(t)*uf/r]
# 33, 34
def rf_o(f): return 2 + mp.cos(f) + mp.sin(2*f)
def rf_n(t): return 2 + Hc(t) + 2*Hs(t)*Hc(t)
def d33_o(t):
    f = A(t); r, r1 = rf_o(f), mp.diff(rf_o, f)
    dx = mp.diff(lambda b: rf_o(b)*mp.cos(b), f); dy = mp.diff(lambda b: rf_o(b)*mp.sin(b), f)
    return dx, dy, r1*mp.cos(f) - r*mp.sin(f), r1*mp.sin(f) + r*mp.cos(f)
def d33_n(t):
    r, r1 = rf_n(t), D(t)*mp.diff(rf_n, t)
    dx = D(t)*mp.diff(lambda b: rf_n(b)*Hc(b), t); dy = D(t)*mp.diff(lambda b: rf_n(b)*Hs(b), t)
    return dx, dy, r1*Hc(t) - r*Hs(t), r1*Hs(t) + r*Hc(t)
def o33(t): return list(d33_o(t))
def n33(t): return list(d33_n(t))
def o34(t): dx, dy, ax, ay = d33_o(t); return [dy/dx, ay/ax]
def n34(t): dx, dy, ax, ay = d33_n(t); return [dy/dx, ay/ax]
# 38
def o38(tau):
    ph = lambda x: A(UU(x)); f, f1 = ph(tau), mp.diff(ph, tau); r, r1 = rr(tau), mp.diff(rr, tau)
    pos = lambda x: [rr(x)*mp.cos(ph(x)), rr(x)*mp.sin(ph(x))]
    vel = [mp.diff(lambda x: pos(x)[i], tau) for i in range(2)]
    rh, fh = [mp.cos(f), mp.sin(f)], [-mp.sin(f), mp.cos(f)]
    return pos(tau) + sc(r, rh) + vel + add(sc(r1, rh), sc(r*f1, fh))
def n38(tau):
    f1, _ = rate_n(UU, tau); u = UU(tau); r, r1 = rr(tau), mp.diff(rr, tau)
    pos = lambda x: [rr(x)*Hc(UU(x)), rr(x)*Hs(UU(x))]
    vel = [mp.diff(lambda x: pos(x)[i], tau) for i in range(2)]
    rh, fh = [Hc(u), Hs(u)], [-Hs(u), Hc(u)]
    return pos(tau) + sc(r, rh) + vel + add(sc(r1, rh), sc(r*f1, fh))
# 39, 40, 41, 42, 43
P39 = [(R('1.3'), R('0.4'), R('2'), R('-1.5')), (R('0.8'), R('3'), R('1.1'), R('0.2')), (R('4'), R('0.9'), R('0.5'), R('2.5'))]
def o39(p): r1, t1, r2, t2 = p; return (r2*mp.cos(A(t2)) - r1*mp.cos(A(t1)))**2
def n39(p): r1, t1, r2, t2 = p; return (r2*Hc(t2) - r1*Hc(t1))**2
def o40(p): r1, t1, r2, t2 = p; return (r2*mp.sin(A(t2)) - r1*mp.sin(A(t1)))**2
def n40(p): r1, t1, r2, t2 = p; return (r2*Hs(t2) - r1*Hs(t1))**2
def ds41(r1, r2, c1, s1, c2, s2):
    return [(r2*c2-r1*c1)**2 + (r2*s2-r1*s1)**2,
            r2*r2*c2*c2 - 2*r1*r2*c1*c2 + r1*r1*c1*c1 + r2*r2*s2*s2 - 2*r1*r2*s1*s2 + r1*r1*s1*s1,
            r2*r2*(c2*c2+s2*s2) + r1*r1*(c1*c1+s1*s1) - 2*r1*r2*(c1*c2+s1*s2),
            r1*r1 + r2*r2 - 2*r1*r2*(1 - 1 + c1*c2 + s1*s2),
            (r2-r1)**2 + 2*r1*r2*(1 - c1*c2 - s1*s2)]
def o41(p): r1, t1, r2, t2 = p; a, b = A(t1), A(t2); return ds41(r1, r2, mp.cos(a), mp.sin(a), mp.cos(b), mp.sin(b))
def n41(p): r1, t1, r2, t2 = p; return ds41(r1, r2, Hc(t1), Hs(t1), Hc(t2), Hs(t2))
def o42(p): t1, t2 = p; a, b = A(t1), A(t2); return [mp.cos(b-a), mp.cos(a)*mp.cos(b) + mp.sin(a)*mp.sin(b)]
def n42(p): t1, t2 = p; x = Hc(t1)*Hc(t2) + Hs(t1)*Hs(t2); return [x, x]
def o43(p):
    r1, t1, r2, t2 = p; a, b = A(t1), A(t2)
    return [(r2*mp.cos(b)-r1*mp.cos(a))**2 + (r2*mp.sin(b)-r1*mp.sin(a))**2, (r2-r1)**2 + 2*r1*r2*(1 - mp.cos(b-a))]
def n43(p):
    r1, t1, r2, t2 = p
    return [(r2*Hc(t2)-r1*Hc(t1))**2 + (r2*Hs(t2)-r1*Hs(t1))**2, (r2-r1)**2 + 2*r1*r2*(1 - Hc(t1)*Hc(t2) - Hs(t1)*Hs(t2))]
# 47, 48
def o47(t): a = A(t); return [mp.cos(a/2), mp.sin(a/2)]
def n47(t): return [h(t), v(t)]
def o48(t): a = A(t); return [mp.cos(a/2)**2 - mp.sin(a/2)**2, 2*mp.cos(a/2)*mp.sin(a/2), mp.cos(a), mp.sin(a)]
def n48(t): return [h(t)**2 - v(t)**2, 2*h(t)*v(t), Hc(t), Hs(t)]
# 49
def o49(t):
    a = A(t); w = sc(-a/2, AX); m = S(dot(w, w))
    return [mp.cos(m)] + sc(mp.sin(m)/m, w) + [mp.cos(a/2)] + sc(-mp.sin(a/2), AX)
def n49(t): return [h(t)] + sc(-v(t), AX) + [h(t)] + sc(-v(t), AX)
# 50, 51, 91
def o50(_): a = 2*mp.pi/3; return [mp.cos(a), mp.sin(a)]
def n50(_): return [R(-1)/2, S(3)/2]
def o51(_):
    a = 2*mp.pi/3; vv = [1, 1, 1]; nv = S(3)
    return ([mp.cos(a/2)] + sc(mp.sin(a/2)/nv, vv) + [mp.cos(mp.pi/3)] + sc(mp.sin(mp.pi/3)/S(3), vv)
            + [R(1)/2] + sc(S(3)/2/S(3), vv) + [R(1)/2]*4)
def n51(_):
    vv = [1, 1, 1]; hc, hs = R(1)/2, S(3)/2   # shares of the direction at the half angle: slope √3
    return ([hc] + sc(hs/S(3), vv) + [hc] + sc(hs/S(3), vv) + [R(1)/2] + sc(S(3)/2/S(3), vv) + [R(1)/2]*4)
def o91(_): return [mp.expj(mp.pi/2), 1j]
def n91(_): return [W(R(1)), 1j]
# 52, 53
def o52(t): a = A(t); return [mp.cos(a/2)] + sc(mp.sin(a/2), AX)
def n52(t): return [h(t)] + sc(v(t), AX)
def o53(p): ta, tb = p; return o52(ta) + [mp.cos(A(tb)/2)] + sc(mp.sin(A(tb)/2), BX)
def n53(p): ta, tb = p; return n52(ta) + [h(tb)] + sc(v(tb), BX)
# 54-59: quaternions of two rotations
def qa_o(ta, X): a = A(ta); return [mp.cos(a/2)] + sc(mp.sin(a/2), X)
def qa_n(ta, X): return [h(ta)] + sc(v(ta), X)
def o54(p):
    ta, tb = p; P = qmul(qa_o(tb, BX), qa_o(ta, AX)); g = 2*mp.acos(P[0]); C = sc(1/S(dot(P[1:], P[1:])), P[1:])
    return P + [mp.cos(g/2)] + sc(mp.sin(g/2), C)
def n54(p):
    ta, tb = p; P = qmul(qa_n(tb, BX), qa_n(ta, AX)); return P + P
def rhs55(ca, sa, cb, sb):
    return [cb*ca - dot(BX, AX)*sb*sa] + add(sc(sb*ca, BX), sc(sa*cb, AX), sc(sb*sa, cross(BX, AX)))
def o55(p):
    ta, tb = p; P = qmul(qa_o(tb, BX), qa_o(ta, AX)); a, b = A(ta), A(tb)
    return P + rhs55(mp.cos(a/2), mp.sin(a/2), mp.cos(b/2), mp.sin(b/2))
def n55(p):
    ta, tb = p; P = qmul(qa_n(tb, BX), qa_n(ta, AX)); return P + rhs55(h(ta), v(ta), h(tb), v(tb))
def o56(p):
    ta, tb = p; P = qmul(qa_o(tb, BX), qa_o(ta, AX)); g = 2*mp.acos(P[0]); a, b = A(ta), A(tb)
    return [mp.cos(g/2), mp.cos(b/2)*mp.cos(a/2) - dot(BX, AX)*mp.sin(b/2)*mp.sin(a/2)]
def n56(p):
    ta, tb = p; P = qmul(qa_n(tb, BX), qa_n(ta, AX)); return [P[0], h(tb)*h(ta) - dot(BX, AX)*v(tb)*v(ta)]
def rod(x, y):  # x = half-slope of α, y = half-slope of β
    return sc(1/(1 - dot(BX, AX)*y*x), add(sc(y, BX), sc(x, AX), sc(y*x, cross(BX, AX))))
def o57(p):
    ta, tb = p; P = qmul(qa_o(tb, BX), qa_o(ta, AX)); g = 2*mp.acos(P[0]); C = sc(1/mp.sin(g/2), P[1:])
    return sc(mp.tan(g/2), C) + rod(mp.tan(A(ta)/2), mp.tan(A(tb)/2))
def n57(p):
    ta, tb = p; P = qmul(qa_n(tb, BX), qa_n(ta, AX)); return sc(1/P[0], P[1:]) + rod(ta, tb)
def o58(p):
    ta, tb = p; a, b = A(ta), A(tb); r = rhs55(mp.cos(a/2), mp.sin(a/2), mp.cos(b/2), mp.sin(b/2))
    g = 2*mp.acos(r[0]); return [mp.cos(g/2)] + r[1:]
def n58(p): ta, tb = p; return rhs55(h(ta), v(ta), h(tb), v(tb))
def s59(cm, cp, sm, spl):  # cos((β−α)/2), cos((β+α)/2), sin((β−α)/2), sin((β+α)/2)
    ab = dot(AX, BX)
    return [(1-ab)*cm + (1+ab)*cp] + add(sc(spl+sm, AX), sc(spl-sm, BX), sc(cm-cp, cross(BX, AX)))
def o59(p):
    ta, tb = p; a, b = A(ta), A(tb); r = s59(mp.cos((b-a)/2), mp.cos((b+a)/2), mp.sin((b-a)/2), mp.sin((b+a)/2))
    g = 2*mp.acos(r[0]); return [mp.cos(g/2)] + r[1:]
def n59(p):
    ta, tb = p; ca, sa, cb, sb = h(ta), v(ta), h(tb), v(tb)
    return s59(cb*ca + sb*sa, cb*ca - sb*sa, sb*ca - cb*sa, sb*ca + cb*sa)
P59 = [(R(3), R(3)), (R(2), R(4)), (R(5), R(3))]
# 60, 61
P60 = [(R('0.4'), R(1), R(-2), R('0.5')), (R('2'), R('0.3'), R(1), R(4)), (R('3'), R(-1), R('0.2'), R(2))]
def e60(c, s, vv):
    u = [0] + AX; q = [0] + vv
    E1 = add(sc(c*c, q), sc(s*c, add(qmul(u, q), sc(-1, qmul(q, u)))), sc(-s*s, qmul(qmul(u, q), u)))
    uxv = [0] + cross(AX, vv); udv = dot(AX, vv)
    E2 = add(sc(c*c, q), sc(2*s*c, uxv), sc(-s*s, qmul(add(uxv, [-udv, 0, 0, 0]), u)))
    E3 = add(sc(c*c, q), sc(2*s*c, uxv), sc(s*s, add(sc(2*udv, u), sc(-1, q))))
    return E1 + E2 + E3
def o60(p): t, x, y, z = p; a = A(t); return e60(mp.cos(a/2), mp.sin(a/2), [x, y, z])
def n60(p): t, x, y, z = p; return e60(h(t), v(t), [x, y, z])
def e61(c, s, C, Sn, vv):
    par = sc(dot(AX, vv), AX); per = add(vv, sc(-1, par)); uxv = cross(AX, vv)
    return add(sc(c*c+s*s, par), sc(2*s*c, uxv), sc(c*c-s*s, per)) + add(par, sc(Sn, uxv), sc(C, per))
def o61(p): t, x, y, z = p; a = A(t); return e61(mp.cos(a/2), mp.sin(a/2), mp.cos(a), mp.sin(a), [x, y, z])
def n61(p): t, x, y, z = p; return e61(h(t), v(t), Hc(t), Hs(t), [x, y, z])
# 62
P62 = [(R(1)/3, R(2)/3, R(2)/3), (R(2)/3, R(1)/3, R(2)/3), (R(2)/3, R(2)/3, R(1)/3)]
def o62(p):
    w, x, y = p; a1 = 2*mp.acos(w); a2 = 2*mp.asin(S(x*x+y*y))
    return [mp.cos(a1/2), mp.sin(a1/2), mp.cos(a2/2), mp.sin(a2/2)]
def n62(p): w, x, y = p; return [w, S(x*x+y*y), w, S(x*x+y*y)]
# 63, 64, 65
def o63(t): a = A(t); return [mp.sin(a/2)**2, (1 - mp.cos(a))/2]
def n63(t): return [v(t)**2, (1 - Hc(t))/2]
def o64(t): a = A(t); hv = mp.sin(a/2)**2; b = 2*mp.asin(S(hv)); return [mp.cos(b), mp.sin(b)]
def n64(t): return [Hc(t), Hs(t)]
P65 = [(R('0.4'), R('1.3'), R('0.7')), (R('2'), R('0.7'), R('3')), (R('3'), R('5'), R('0.2'))]
def o65(p):
    ta, tb, tC = p; a, b, C = A(ta), A(tb), A(tC)
    c = mp.acos(mp.cos(a)*mp.cos(b) + mp.sin(a)*mp.sin(b)*mp.cos(C))
    hav = lambda x: mp.sin(x/2)**2
    return [hav(c), hav(a-b) + mp.sin(a)*mp.sin(b)*hav(C)]
def n65(p):
    ta, tb, tC = p; ca, sa, cb, sb, cC = Hc(ta), Hs(ta), Hc(tb), Hs(tb), Hc(tC)
    cc = ca*cb + sa*sb*cC
    return [(1-cc)/2, (1 - (ca*cb + sa*sb))/2 + sa*sb*(1-cC)/2]
# 66
P66 = [(R('0.4'), R('0.3'), R('-0.2')), (R('2'), R('0.1'), R('0.6')), (R('-1.5'), R('-0.4'), R('0.25'))]
def o66(p):
    l, p1, p2 = p; L, f1, f2 = A(l), A(p1), A(p2)
    return [mp.cos(L)*mp.cos(f2), mp.sin(L)*mp.cos(f2), mp.sin(f2), mp.cos(0)*mp.cos(f1), mp.sin(0)*mp.cos(f1), mp.sin(f1),
            mp.cos(f1), 0, mp.sin(f1)]
def n66(p):
    l, p1, p2 = p
    return [Hc(l)*Hc(p2), Hs(l)*Hc(p2), Hs(p2), 1*Hc(p1), 0*Hc(p1), Hs(p1), Hc(p1), 0, Hs(p1)]
# 67
def o67(p): uu, t1, t2 = p; return [uu*mp.sin(A(t1)), uu*mp.sin(A(t2))]
def n67(p): uu, t1, t2 = p; return [uu*Hs(t1), uu*Hs(t2)]
P67 = [(R(3), R('0.4'), R('0.2')), (R('1.5'), R(2), R('0.7')), (R(2), R('0.1'), R(5))]
# 69, 74, 78, 79, 82, 83
K0 = R(2)
P69 = [(R(1), R('1.5'), R('0.4')), (R('1.2'), R('1.5'), R('0.7')), (R(1), R('1.33'), R('1.2'))]
def o69(p):
    n1, n2, t = p; ti = A(t); tt = mp.asin(n1*mp.sin(ti)/n2)
    return [n2*K0*mp.sin(tt), n2*K0*mp.cos(tt), K0*n1*mp.sin(ti), K0*n2*mp.cos(tt)]
def n69(p):
    n1, n2, t = p; vt = n1*Hs(t)/n2; ht = S(1 - vt*vt)
    return [n2*K0*vt, n2*K0*ht, K0*n1*Hs(t), K0*n2*ht]
P71 = [(R('1.5'), R(1), R(1)), (R(2), R(1), R('0.6')), (R('1.5'), R('1.1'), R('1.5'))]
def o71(p):
    n1, n2, t = p; ti = A(t); tt = mp.asin(n1*mp.sin(ti)/n2)
    return [mp.cos(tt), 1j*S((n1/n2)**2*mp.sin(ti)**2 - 1)]
def n71(p):
    n1, n2, t = p; vt = n1*Hs(t)/n2
    return [S(1 - vt*vt), 1j*S((n1/n2)**2*Hs(t)**2 - 1)]
def o74(p): n1, n2, t = p; ti = A(t); return [K0*S(n1*n1*mp.sin(ti)**2 - n2*n2), n1*K0*mp.sin(ti)]
def n74(p): n1, n2, t = p; return [K0*S(n1*n1*Hs(t)**2 - n2*n2), n1*K0*Hs(t)]
def o78(p):
    n1, n2, t = p; ti = A(t); tt = mp.asin(n1*mp.sin(ti)/n2); ci, ct = mp.cos(ti), mp.cos(tt)
    return [(n2*ci - n1*ct)/(n2*ci + n1*ct), 2*n1*ci/(n2*ci + n1*ct)]
def n78(p):
    n1, n2, t = p; vt = n1*Hs(t)/n2; ci, ct = Hc(t), S(1 - vt*vt)
    return [(n2*ci - n1*ct)/(n2*ci + n1*ct), 2*n1*ci/(n2*ci + n1*ct)]
def o79(p): return o78(p)[1]
def n79(p): return n78(p)[1]
P80 = [(R('1.5'), R(1)), (R(2), R('0.6')), (R('1.4'), R('1.5'))]
def o80(p):
    n, t = p; ti = A(t); q = 1j*S(n*n*mp.sin(ti)**2 - 1)
    return [(n*mp.cos(ti) - q)/(n*mp.cos(ti) + q), (mp.cos(ti) - n*q)/(mp.cos(ti) + n*q)]
def n80(p):
    n, t = p; q = 1j*S(n*n*Hs(t)**2 - 1)
    return [(n*Hc(t) - q)/(n*Hc(t) + q), (Hc(t) - n*q)/(Hc(t) + n*q)]
def o81(p): return o80(p)[1]
def n81(p): return n80(p)[1]
P82 = [(R('1.3'), R('0.4'), R('0.2')), (R(1), R(2), R('0.7')), (R('1.5'), R('0.1'), R(5))]
def o82(p): n1, ti, tt = p; return n1*mp.sin(A(ti))/mp.sin(A(tt))
def n82(p): n1, ti, tt = p; return n1*Hs(ti)/Hs(tt)
def o83(p): ti, tt = p; a, b = A(ti), A(tt); return -mp.sin(a-b)/mp.sin(a+b)
def n83(p):
    ti, tt = p; ca, sa, cb, sb = Hc(ti), Hs(ti), Hc(tt), Hs(tt); return -(sa*cb - ca*sb)/(sa*cb + ca*sb)
P83 = [(R('0.4'), R('0.2')), (R('0.7'), R('0.5')), (R(3), R('0.3'))]
# 84, 86
def o84(p):
    t, u = p; f = A(t); R1 = mp.sin(f)/(1 - mp.cos(f)); R2 = mp.cot(f/2); g = 2*mp.atan(1/R1)
    return [R1, R2, mp.cos(A(u)), mp.sin(A(u)), mp.cos(g), mp.sin(g)]
def n84(p):
    t, u = p; R1 = Hs(t)/(1 - Hc(t)); return [R1, 1/t, Hc(u), Hs(u), Hc(1/R1), Hs(1/R1)]
def o86(t): x = A(t); return [mp.cos(x), mp.sin(x)]
def n86(t): return [(1 - t*t)/(1 + t*t), 2*t/(t*t + 1)]
# 92, 94
P92 = [(R(2), R(3), R(5), R('0.4')), (R(1), R(7), R('0.5'), R('0.2')), (R(3), R('1.5'), R(2), R('-0.6'))]
def o92(p): Is, ws, Ip, t = p; return Is*ws/(Ip*mp.cos(A(t)))
def n92(p): Is, ws, Ip, t = p; return Is*ws/(Ip*Hc(t))
P94 = [(R(2), R('9.8'), R('0.3'), R(5), R(7), R('0.4')), (R(1), R(3), R(2), R('0.5'), R(4), R(2)), (R(3), R('1.6'), R('0.7'), R(2), R('0.9'), R('0.1'))]
def o94(p): m, g, r, Is, ws, t = p; th = A(t); tau = m*g*r*mp.sin(th); return [m*g*r/(Is*ws), tau/(Is*ws*mp.sin(th))]
def n94(p): m, g, r, Is, ws, t = p; tau = m*g*r*Hs(t); return [m*g*r/(Is*ws), tau/(Is*ws*Hs(t))]
# 96-112 (the ellipse)
PE = [(R(3), R(2), R('0.4')), (R(5), R('1.5'), R('-2')), (R('2.5'), R(4), R('7'))]
def o96(p): a, b, u = p; t = A(u); return [a*mp.cos(t), b*mp.sin(t)]
def n96(p): a, b, u = p; return [a*Hc(u), b*Hs(u)]
P97 = [(R(3), R(2), R('0.4'), R(1), R(-2)), (R(5), R('1.5'), R('-2'), R('0.3'), R('0.7')), (R('2.5'), R(4), R(7), R(-1), R(2))]
def coef97(a, b, s, c, x0, y0):
    Aa = a*a*s*s + b*b*c*c; B = 2*(b*b - a*a)*s*c; C = a*a*c*c + b*b*s*s
    return [Aa, B, C, -2*Aa*x0 - B*y0, -B*x0 - 2*C*y0, Aa*x0*x0 + B*x0*y0 + C*y0*y0 - a*a*b*b]
def o97(p): a, b, u, x0, y0 = p; t = A(u); return coef97(a, b, mp.sin(t), mp.cos(t), x0, y0)
def n97(p): a, b, u, x0, y0 = p; return coef97(a, b, Hs(u), Hc(u), x0, y0)
P98 = [(R(3), R(2), R(1), R(-2), R('0.4')), (R(5), R('1.5'), R('0.3'), R('0.7'), R(-2)), (R('2.5'), R(4), R(-1), R(2), R(7))]
def o98(p):
    x, y, x0, y0, u = p; t = A(u); c, s = mp.cos(t), mp.sin(t)
    return [(x-x0)*c + (y-y0)*s, -(x-x0)*s + (y-y0)*c]
def n98(p):
    x, y, x0, y0, u = p; c, s = Hc(u), Hs(u)
    return [(x-x0)*c + (y-y0)*s, -(x-x0)*s + (y-y0)*c]
def o99(p): a, b, u = p; t = A(u); return [b*mp.sin(t)/(a*mp.cos(t)), (b/a)*mp.tan(t), mp.tan(t)]
def n99(p): a, b, u = p; s = Hs(u)/Hc(u); return [(b/a)*s, (b/a)*s, s]
def o100(u): t = A(u); return mp.tan(t/2)
def n100(u): return u
def o101(p):
    a, b, u = p; t = A(u)
    xp = mp.diff(lambda q: a*mp.cos(q), t); yp = mp.diff(lambda q: b*mp.sin(q), t); m = yp/xp
    return [xp, yp, -a*mp.sin(t), b*mp.cos(t), m, -(b/a)*mp.cot(t), mp.cot(t), -m*a/b]
def n101(p):
    a, b, u = p
    xp = D(u)*mp.diff(lambda q: a*Hc(q), u); yp = D(u)*mp.diff(lambda q: b*Hs(q), u); m = yp/xp
    return [xp, yp, -a*Hs(u), b*Hc(u), m, -(b/a)*Hc(u)/Hs(u), Hc(u)/Hs(u), -m*a/b]
P102 = [(R(3), R(1), R(1), R(1)), (R(4), R(0), R(1), R(1)), (R(3), R(2), R(1), R(0))]
def c102(p): a, b, c, d = p; return (a*a + b*b - c*c - d*d)/(2*(a*c + b*d))
def o102(p): t0 = mp.acot(c102(p))/2; return [mp.cot(2*t0), c102(p)]
def n102(p):
    c = c102(p); s0 = S(1 + c*c) - c   # slope of t0
    return [(1 - s0*s0)/(2*s0), c]
P103 = [(R(3), R(1), R(-1), R(2), R('0.4')), (R(2), R('0.5'), R(1), R(3), R(-2)), (R(1), R(4), R(2), R(-1), R(3))]
def o103(p):
    a, b, c, d, u = p; t = A(u); f1, f2 = [a, b], [c, d]
    return dot(add(sc(-mp.sin(t), f1), sc(mp.cos(t), f2)), add(sc(mp.cos(t), f1), sc(mp.sin(t), f2)))
def n103(p):
    a, b, c, d, u = p; f1, f2 = [a, b], [c, d]
    return dot(add(sc(-Hs(u), f1), sc(Hc(u), f2)), add(sc(Hc(u), f1), sc(Hs(u), f2)))
def o104(u): t = A(u); return [mp.cos(t)**2 - mp.sin(t)**2, mp.cos(2*t), 2*mp.sin(t)*mp.cos(t), mp.sin(2*t)]
def n104(u):
    c, s = Hc(u), Hs(u); sl = 2*u/(1 - u*u)   # slope of t, which is the half-slope of 2t
    return [c*c - s*s, Hc(sl), 2*s*c, Hs(sl)]
def o106(p): a, b, u = p; t = A(u); return [0, 0, a*mp.cos(t), a*mp.sin(t), -b*mp.sin(t), b*mp.cos(t)]
def n106(p): a, b, u = p; return [0, 0, a*Hc(u), a*Hs(u), -b*Hs(u), b*Hc(u)]
P107 = [(R(3), R('0.5'), R('0.4')), (R(5), R('0.2'), R(-2)), (R('2.5'), R('0.9'), R(7))]
def o107(p): a, ec, u = p; t = A(u); return [a*(1 - ec*ec)/(1 + ec*mp.cos(t)), a*(1 - ec*ec)/(1 - ec*mp.cos(t))]
def n107(p): a, ec, u = p; return [a*(1 - ec*ec)/(1 + ec*Hc(u)), a*(1 - ec*ec)/(1 - ec*Hc(u))]
def o108(p):
    a, b, u = p; t = A(u); c, s = mp.cos(t), mp.sin(t)
    return [a*c, b*s, -a*c, -b*s, -a*s, b*c, a*s, -b*c]
def n108(p):
    a, b, u = p; c, s = Hc(u), Hs(u)
    return [a*c, b*s, -a*c, -b*s, -a*s, b*c, a*s, -b*c]
def o109(p): c1, c2, u = p; d1 = c1*mp.sin(A(u)); return [c2*d1/2, c1*c2*mp.sin(A(u))/2]
def n109(p): c1, c2, u = p; d1 = c1*Hs(u); return [c2*d1/2, c1*c2*Hs(u)/2]
def o111(p):
    a, b, u = p; t = A(u); q = t + mp.pi/2
    return [a*mp.cos(q), b*mp.sin(q), -a*mp.sin(t), b*mp.cos(t)]
def n111(p): a, b, u = p; return [-a*Hs(u), b*Hc(u), -a*Hs(u), b*Hc(u)]
P112 = [(R('0.3'), R(2)), (R(-1), R('0.5')), (R(3), R(-4))]
def o112(p): m1, m2 = p; th = mp.atan(m2) - mp.atan(m1); return [(1 + m1*m2)/(m2 - m1), mp.cot(th)]
def n112(p): m1, m2 = p; sl = (m2 - m1)/(1 + m1*m2); return [(1 + m1*m2)/(m2 - m1), 1/sl]

SH = 'Each direction is given by its half-slope t; its shares are (1 − t²)/(1 + t²) and 2t/(1 + t²), its half-angle shares h(t), v(t). '
LAWS = [
 T(1, 'angle by an inverse function, piecewise (call 1); the z = 0 value a direction (call 2)',
   'The inclination is the direction whose shares are (z/r, ρ/r), ρ = √(x² + y²), r = √(x² + y² + z²), in every case where it is defined.',
   o1, n1, [(R(1), R(2), R(3)), (R(1), R(-2), R(-3)), (R(3), R(4), R(0))]),
 T(2, 'angle by inverse functions, piecewise (call 1); values ±π/2 directions (call 2)',
   'The azimuth is the direction whose shares are (x/ρ, y/ρ), ρ = √(x² + y²), in every case where it is defined.', o2, n2, P2),
 T(3, 'shares of θ and φ', SH + 'x = r·sθ·cφ, y = r·sθ·sφ, z = r·cθ with (cθ, sθ), (cφ, sφ) the shares of θ and φ.', o3, n3, PS),
 T(4, 'angle by inverse functions (call 1)', 'r = √(ρ² + z²); the direction θ has slope ρ/z and shares (z/r, ρ/r); φ keeps its shares.', o4, n4, P4),
 T(5, 'shares', SH + 'ρ = r·sθ, z = r·cθ, φ keeps its shares.', o5, n5, PS),
 T(6, 'shares', SH + 'x = r·sθ·cφ/√a, y = r·sθ·sφ/√b, z = r·cθ/√c, and ax² + by² + cz² = r².', o6, n6, P6),
 T(7, 'shares; the turn element as 2·dt/(1 + t²)', SH + 'The Jacobian taken per unit turn, ((1 + t²)/2)·∂/∂t, has absolute determinant r²·sθ/√(abc).', o7, n7, P6),
 T(8, 'shares', SH + 'r̂ = (sθcφ, sθsφ, cθ), θ̂ = (cθcφ, cθsφ, −sθ), φ̂ = (−sφ, cφ, 0).', o8, n8, PQ),
 T(9, 'shares', SH + 'The matrix [[sθcφ, cθcφ, −sφ], [sθsφ, cθsφ, cφ], [cθ, −sθ, 0]] carries (r̂, θ̂, φ̂) to (x̂, ŷ, ẑ).', o9, n9, PQ),
 T(10, 'shares; d/dθ as ((1 + t²)/2)·d/dt', SH + 'The Jacobian (per unit turn, ((1 + t²)/2)·∂/∂t) equals [[sθcφ, r·cθcφ, −r·sθsφ], [sθsφ, r·cθsφ, r·sθcφ], [cθ, −r·sθ, 0]].', o10, n10, PS),
 T(11, 'shares; turn element', SH + '|det| of the Jacobian per unit turn is r²·sθ.', o11, n11, PS),
 T(12, 'shares; d/dθ as ((1 + t²)/2)·d/dt', SH + 'grad f = f_r·r̂ + (1/r)·D(t)·f_t·θ̂ + (1/(r·sθ))·D(u)·f_u·φ̂, D(t) = (1 + t²)/2; checked on a polynomial f.', o12, n12, PS),
 T(13, 'shares; sθ·∂/∂θ = t·∂/∂t', SH + 'Laplacian f = (1/r²)(r²f_r)_r + D(t)(f_t + t·f_tt)/(r²·sθ) + D(u)(u·f_u + D(u)·f_uu)/(r²·sθ²), and the second form likewise; checked on a polynomial f.', o13, n13, PS),
 T(14, 'shares; turn derivatives', SH + 'div A = (1/r²)(r²A_r)_r + D(t)·(sθ·A_θ)_t/(r·sθ) + D(u)·(A_φ)_u/(r·sθ); checked on a polynomial field.', o14, n14, PS),
 T(15, 'shares; difference of directions', SH + 'D = √(r² + r′² − 2rr′(sθ·sθ′·(cφcφ′ + sφsφ′) + cθ·cθ′)).', o15, n15, P15),
 T(16, 'shares; γ given by its first share', SH + 'The first share of γ equals cθcθ′ + sθsθ′(cφcφ′ + sφsφ′), in both forms.', o16, n16, P16),
 T(17, 'shares; turn rates 2ṫ/(1 + t²)', SH + 'With θ̇ = 2ṫ/(1 + t²), θ̈ = 2ẗ/(1 + t²) − 4tṫ²/(1 + t²)², the acceleration components are r̈ − rθ̇² − rφ̇²sθ², rθ̈ + 2ṙθ̇ − rφ̇²sθcθ, rφ̈sθ + 2ṙφ̇sθ + 2rθ̇φ̇cθ; checked on a path.', o17, n17, TAU),
 T(18, 'shares; turn rates', SH + 'r × mv = m·r²·(−φ̇·sθ·θ̂ + θ̇·φ̂), with the turn rates 2ṫ/(1 + t²); checked on a path.', o18, n18, TAU),
 T(19, 'shares', SH + 'x = r·cφ, y = r·sφ.', o19, n19, PP),
 T(20, 'angle by inverse functions (call 1), values (call 2)', 'atan2(y, x) names the direction with shares (x/r, y/r), r = √(x² + y²), in every case where it is defined.'.replace('atan2(y, x)', 'The two-argument angle'), o20, n20, P20),
 T(21, 'angle by inverse function (call 1)', 'The polar angle is the direction with shares (x/r, y/r), wherever r ≠ 0.', o21, n21, P21),
 T(22, 'landing point', SH + 'z = r(cφ + i·sφ) = r·(1 + it)²/(1 + t²).', o22, n22, PP),
 T(23, 'landing points; directions composed by half-slope addition', SH + 'r₀w(t₀)·r₁w(t₁) = r₀r₁·w((t₀ + t₁)/(1 − t₀t₁)), w(t) = (1 + it)²/(1 + t²).', o23, n23, P23),
 N(24, 'dividing a direction by n needs n-th roots, not square roots alone (the principal n-th root)'),
 N(25, 'the circular function of an amount x'),
 T(26, 'shares; a multiple of a direction is a polynomial in its shares', SH + 'r = 6c⁵s − 20c³s³ + 6cs⁵ + 2 with (c, s) the shares of θ.', o26, n26, P3),
 T(27, 'mirror direction (−c, s); checked on r = 2 + s + c² − s²', SH + 'r at the direction with shares (−c, s) equals r at (c, s).', o27, n27, P3),
 T(28, 'shares; difference of directions', SH + 'r² − 2r·r₀·(cφcγ + sφsγ) + r₀² = a².', o28, n28, P28),
 T(29, 'angle by inverse function (call 1)', 'The direction φ has slope m: shares (1/√(1 + m²), m/√(1 + m²)).', o29, n29, P3),
 T(30, 'shares', SH + 'r = r₀/(cφcγ + sφsγ).', o30, n30, P30),
 N(31, 'whole turns 2kπ carried as an amount in the curves’ argument (call 3)'),
 T(32, 'shares; d/dφ as ((1 + t²)/2)·d/dt', SH + 'du/dx = u_r·x/√(x² + y²) − u_φ·y/(x² + y²) = cφ·u_r − (1/r)·sφ·u_φ, du/dy likewise, u_φ = D(t)·u_t; checked on a polynomial u.', o32, n32, PP),
 T(33, 'shares; turn derivative', SH + 'With ′ = D(t)·d/dt: x′ = r′·cφ − r·sφ, y′ = r′·sφ + r·cφ; checked on r = 2 + c + 2sc.', o33, n33, P3),
 T(34, 'shares; turn derivative', SH + 'dy/dx = (r′·sφ + r·cφ)/(r′·cφ − r·sφ), ′ = D(t)·d/dt; checked on r = 2 + c + 2sc.', o34, n34, P3),
 N(35, 'a sector’s area: the angle Δφ as an amount of turn'),
 N(36, 'a total over the line (the Gaussian integral)'),
 T(37, 'shares', SH + 'r̂ = (cφ, sφ).', o37, n37, P3),
 T(38, 'shares; turn rate', SH + 'r = r·(cφ, sφ); ṙ = ṙ·(cφ, sφ) + r·φ̇·(−sφ, cφ), φ̇ = 2u̇/(1 + u²); checked on a path.', o38, n38, TAU),
 T(39, 'shares', SH + 'dx² = (r₂c₂ − r₁c₁)².', o39, n39, P39),
 T(40, 'shares', SH + 'dy² = (r₂s₂ − r₁s₁)².', o40, n40, P39),
 T(41, 'shares', SH + 'Each form of ds² with (c₁, s₁), (c₂, s₂) the shares of θ₁, θ₂.', o41, n41, P39),
 T(42, 'shares', SH + 'The first share of the difference direction is c₁c₂ + s₁s₂.', o42, n42, PQ),
 T(43, 'shares', SH + 'ds² = dr² + 2r₁r₂(1 − (c₁c₂ + s₁s₂)).', o43, n43, P39),
 N(44, 'an approximation (call 4)'),
 N(45, 'an approximation (call 4)'),
 T(46, 'shares', SH + 'x = r·c, y = r·s, z = z.', o46, n46, [(R('1.3'), R('0.4'), R(2)), (R(2), R('-1.5'), R(-1)), (R('0.8'), R(3), R(5))]),
 T(47, 'half-angle shares', 'C = 1/√(1 + t²), S = t/√(1 + t²), t the half-slope of θ.', o47, n47, P3),
 T(48, 'shares', SH + '(h² − v²)·n + 2hv·n_T = c·n + s·n_T, with h, v the half-angle shares.', o48, n48, P3),
 T(49, 'half-angle shares', SH + 'q⁻¹ = h(t) − u·v(t) on both sides.', o49, n49, P3),
 T(50, 'value of a direction (call 2)', 'α is the direction with shares (−1/2, √3/2).', o50, n50, DUM),
 T(51, 'value of a direction (call 2)', 'The half angle has shares (1/2, √3/2), so u = 1/2 + (√3/2)(1/√3)·v = (1 + i + j + k)/2 at every step.', o51, n51, DUM),
 T(52, 'half-angle shares', SH + 'S = h(t) + S·v(t).', o52, n52, P3),
 T(53, 'half-angle shares', SH + 'A = h(tα) + A·v(tα), B = h(tβ) + B·v(tβ).', o53, n53, PQ),
 T(54, 'half-angle shares; γ by its half shares', SH + 'The product of the two quaternions in half shares is the quaternion of the composed turn.', o54, n54, PQ),
 T(55, 'half-angle shares', SH + 'The product equals (h_βh_α − B·A v_βv_α) + (B v_βh_α + A v_αh_β + B × A v_βv_α).', o55, n55, PQ),
 T(56, 'half-angle shares', SH + 'The first half share of γ equals h_βh_α − B·A·v_βv_α.', o56, n56, PQ),
 T(57, 'half-slopes directly', 'With t_α, t_β, t_γ the half-slopes: C·t_γ = (B·t_β + A·t_α + B × A·t_βt_α)/(1 − B·A·t_βt_α).', o57, n57, PQ),
 T(58, 'angle by inverse function (call 1)', SH + 'γ is the direction whose half first share is h_βh_α − B·A·v_βv_α; D = B v_βh_α + A v_αh_β + B × A v_βv_α.', o58, n58, PQ),
 T(59, 'angle by inverse function (call 1); sums of half directions by shares', SH + 'γ’s half first share is (1 − A·B)(h_βh_α + v_βv_α) + (1 + A·B)(h_βh_α − v_βv_α); D likewise in half shares.', o59, n59, P59),
 T(60, 'half-angle shares', SH + 'The three forms of v′ with h², hv, v² in place of the half-angle products.', o60, n60, P60),
 T(61, 'shares', SH + 'v′ = v∥(h² + v²) + (u × v)(2hv) + v⊥(h² − v²) = v∥ + (u × v)·s + v⊥·c.', o61, n61, P60),
 T(62, 'angle by inverse functions (call 1)', 'α is the direction whose half shares are (w, √(x² + y²)), in both forms.', o62, n62, P62),
 T(63, 'half-angle share', SH + 'hav θ = v(t)² = (1 − c)/2.', o63, n63, P3),
 T(64, 'angle by inverse function (call 1)', SH + 'θ is the direction whose half second share is √(hav θ).', o64, n64, P3),
 T(65, 'shares', SH + 'hav c = (1 − c_c)/2 with c_c = c_a c_b + s_a s_b c_C; hav(a − b) = (1 − (c_a c_b + s_a s_b))/2; hav C = (1 − c_C)/2.', o65, n65, P65),
 T(66, 'shares; the zero direction (call 2)', SH + 'p₂′ = (c_λ c₂, s_λ c₂, s₂), p₁′ = (1·c₁, 0·c₁, s₁) = (c₁, 0, s₁).', o66, n66, P66),
 T(67, 'shares', SH + 'v₁ = u·s₁, v₂ = u·s₂.', o67, n67, P67),
 N(68, 'the exponential of a phase, an amount'),
 T(69, 'shares; Snell in shares', SH + 'With s_t = n₁s_i/n₂, c_t = √(1 − s_t²): k_t = n₂k₀(s_t, c_t) = k₀(n₁s_i, n₂c_t).', o69, n69, P69),
 N(70, 'the exponential of a phase, an amount'),
 T(71, 'shares under total reflection', SH + 'With s_t = n₁s_i/n₂ > 1, c_t = √(1 − s_t²) = i·√((n₁/n₂)²s_i² − 1).', o71, n71, P71),
 N(72, 'exponentials of amounts (decay and phase)'),
 N(73, 'exponentials of amounts'),
 T(74, 'shares', SH + 'κ = k₀√(n₁²s_i² − n₂²), k_x = n₁k₀s_i.', o74, n74, P71),
 N(75, 'the 2π of a wavelength per turn of phase: a whole turn as an amount'),
 N(76, 'the 2π of a wavelength per turn of phase'),
 N(77, 'the 2π of a wavelength per turn of phase'),
 T(78, 'shares; Snell in shares', SH + 'r_p = (n₂c_i − n₁c_t)/(n₂c_i + n₁c_t), c_t = √(1 − (n₁s_i/n₂)²).', lambda p: o78(p)[0], lambda p: n78(p)[0], P69),
 T(79, 'shares; Snell in shares', SH + 't_p = 2n₁c_i/(n₂c_i + n₁c_t), c_t = √(1 − (n₁s_i/n₂)²).', o79, n79, P69),
 T(80, 'shares', SH + 'r_s = (n·c_i − i√(n²s_i² − 1))/(n·c_i + i√(n²s_i² − 1)).', lambda p: o80(p)[0], lambda p: n80(p)[0], P80),
 T(81, 'shares', SH + 'r_p = (c_i − in√(n²s_i² − 1))/(c_i + in√(n²s_i² − 1)).', o81, n81, P80),
 T(82, 'shares', SH + 'n₂ = n₁s_i/s_t.', o82, n82, P82),
 T(83, 'shares; difference and sum of directions', SH + 'r_s = −(s_ic_t − c_is_t)/(s_ic_t + c_is_t).', o83, n83, P83),
 T(84, 'shares; inverse by half-slope (call 1)', SH + 'R = s_φ/(1 − c_φ) = 1/t; Θ keeps θ’s shares; back, φ is the direction with half-slope 1/R.', o84, n84, PQ),
 N(85, 'the exponential of an angle as an amount (turns counted)'),
 T(86, 'half-slope substitution', 'The direction with half-slope t has shares (1 − t²)/(1 + t²) and 2t/(t² + 1).', o86, n86, P3),
 N(87, 'rapidity, a hyperbolic amount; tanh of it renames an exponential'),
 N(88, 'rapidity, a hyperbolic amount'),
 N(89, 'retardance, a phase amount 2π per wavelength'),
 N(90, 'the phase factor, an exponential of an amount, on both sides'),
 T(91, 'value of a direction (call 2)', 'The landing point of the quarter-turn direction (half-slope 1): (1 + i)²/2 = i.', o91, n91, DUM),
 T(92, 'shares', SH + 'ω_p = I_sω_s/(I_p·c_α).', o92, n92, P92),
 N(93, 'an approximation (call 4)'),
 T(94, 'shares', SH + 'ω_p = mgr/(I_sω_s) = τ/(I_sω_s·s_θ) with τ = mgr·s_θ.', o94, n94, P94),
 N(95, 'a period from 2π per turn: whole turns as an amount'),
 T(96, 'shares; the range is every direction (call 3)', SH + '(x, y) = (a·c, b·s) over every direction.', o96, n96, PE),
 T(97, 'shares', SH + 'A = a²s² + b²c², B = 2(b² − a²)sc, C = a²c² + b²s², D, E, F as stated.', o97, n97, P97),
 T(98, 'shares', SH + 'X = (x − x∘)c + (y − y∘)s, Y = −(x − x∘)s + (y − y∘)c.', o98, n98, P98),
 T(99, 'slope', SH + 'y/x = b·s/(a·c) = (b/a)·σ, σ = s/c the slope, and (b/a)σ ≠ σ.', o99, n99, PE),
 T(100, 'half-slope', 'u is the half-slope of t.', o100, n100, P3),
 T(101, 'shares; turn derivative', SH + "x′ = (−a·s, b·c) with ′ = D(u)·d/du; m = −(b/a)·c/s; c/s = −ma/b.", o101, n101, PE),
 T(102, 'angle by function of quantities (call 1)', 'With σ the slope of t₀, (1 − σ²)/(2σ) = (f₁² − f₂²)/(2f₁·f₂).', o102, n102, P102),
 T(103, 'shares', SH + '(−f₁·s + f₂·c)·(f₁·c + f₂·s) as a function of the direction t.', o103, n103, P103),
 T(104, 'shares; 2t has half-slope equal to the slope of t', SH + 'c² − s² = (1 − σ²)/(1 + σ²), 2sc = 2σ/(1 + σ²), σ = 2u/(1 − u²).', o104, n104, P3),
 N(105, 'the area of an ellipse, a total'),
 T(106, 'shares', SH + 'f₀ = (0, 0), f₁ = a(c, s), f₂ = b(−s, c).', o106, n106, PE),
 T(107, 'shares (ε the eccentricity)', SH + 'r = a(1 − ε²)/(1 ± ε·c).', o107, n107, P107),
 T(108, 'shares', SH + '(±a·c, ±b·s), (∓a·s, ±b·c).', o108, n108, PE),
 T(109, 'shares', SH + 'A = ½c₂d₁ = ½c₁c₂·s_α, d₁ = c₁s_α.', o109, n109, PE),
 N(110, 'the area of an ellipse, a total'),
 T(111, 'quarter-turn direction (−s, c) (call 2)', SH + 'p at the direction a quarter on, shares (−s, c), is (−a·s, b·c).', o111, n111, PE),
 T(112, 'angle by function (call 1); slope by subtraction', 'The direction between the lines has slope (m₂ − m₁)/(1 + m₁m₂); its reciprocal is (1 + m₁m₂)/(m₂ − m₁).', o112, n112, P112),
 N(113, 'the area of an ellipse, a total'),
 N(114, 'an elliptic integral, a total'),
 N(115, 'a series carried to its limit'),
 N(116, 'a series carried to its limit'),
 N(117, 'an approximation (call 4)'),
 N(118, 'a bound on a numerical value carrying π'),
 N(119, 'an integral with arc limits, a total'),
 N(120, 'bounds on a total (the circumference)'),
]
