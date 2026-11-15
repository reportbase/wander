"""DVH restatements of the 120 laws in runs/dvh/laws.md (checked by runs/dvh/check.py).
Convention: a direction's angle a is carried by its slope s = tan a (points are slopes); orig computes the law as written with
mpmath's transcendental functions, new computes the same relation from slopes and shares by rational operations and square
roots only. A rapidity's angle is carried by its slope u = tanh(rapidity), by settled call 1."""
import mpmath as mp; mp.mp.dps = 50
S = mp.sqrt
def R(x): return mp.mpf(x)
def N(n, reason): return dict(n=n, verdict='none', notation=False, reason=reason)
def T(n, reason, restated, orig, new, points): return dict(n=n, verdict='notation', notation=True, reason=reason, restated=restated, orig=orig, new=new, points=points)
P3 = [R('0.3'), R('1.7'), R('5')]
def h(s): return 1/S(1+s*s)
def v(s): return s/S(1+s*s)

# ---- helpers: arithmetic and sqrt only (used by both sides) ----
J1 = mp.mpc(0, 1)
def tt(s): return s/(1+S(1+s*s))            # half-slope of the direction with slope s
def hh(s): t = tt(s); return 1/S(1+t*t)      # half-direction's shares
def hv_(s): t = tt(s); return t/S(1+t*t)
def fl(M):
    if isinstance(M, mp.matrix): return [M[i, j] for i in range(M.rows) for j in range(M.cols)]
    return [x for row in M for x in row]
def mmul(A, B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def skew(u): return [[0, -u[2], u[1]], [u[2], 0, -u[0]], [-u[1], u[0], 0]]
def I3(): return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
def rod(u, c, sn):   # law 15's matrix from a turn's two shares c, sn
    x, y, z = u; k = 1-c
    return [[x*x*k+c, x*y*k-z*sn, x*z*k+y*sn], [x*y*k+z*sn, y*y*k+c, y*z*k-x*sn], [x*z*k-y*sn, y*z*k+x*sn, z*z*k+c]]
def compact(u, c, sn):
    K = skew(u)
    return [[c*I3()[i][j] + sn*K[i][j] + (1-c)*u[i]*u[j] for j in range(3)] for i in range(3)]
def halfR(u, c2, s2, sn):   # c2 = cos^2 of the half turn, s2 = sin^2 of it, sn = the turn's sin share
    eps = lambda j, k, l: [[[0,0,0],[0,0,1],[0,-1,0]],[[0,0,-1],[0,0,0],[1,0,0]],[[0,1,0],[-1,0,0],[0,0,0]]][j][k][l]
    return [[(c2 + s2*(2*u[j]**2-1)) if j == k else (2*u[j]*u[k]*s2 - sum(eps(j, k, l)*u[l] for l in range(3))*sn)
             for k in range(3)] for j in range(3)]
def ndots(n): return mp.matrix([[n[2], n[0]-J1*n[1]], [n[0]+J1*n[1], -n[2]]])
SX = mp.matrix([[0, 1], [1, 0]]); SY = mp.matrix([[0, -J1], [J1, 0]]); SZ = mp.matrix([[1, 0], [0, -1]]); I2 = mp.eye(2)
def adot(a): return a[0]*SX + a[1]*SY + a[2]*SZ
def dag(M): return M.H

# transcendental side only
C, Sn, Tn, At = mp.cos, mp.sin, mp.tan, mp.atan
U1 = [R(1)/3, R(2)/3, R(2)/3]; U2 = [R(2)/7, R(3)/7, R(6)/7]; U3 = [R('0.6'), R(0), R('0.8')]
X0 = [R('0.4'), R('-1.3'), R('2.1')]
D3 = [R(1), R(2), R(3)]   # dummy points for laws with no free variable
pts2 = [(R(2), R('0.3')), (R(3), R('1.7')), (R('0.5'), R(-5))]
def rot2(c, s_): return [c, -s_, s_, c]

def o13(p):
    s, u = p; a = At(s); Rm = rod(u, C(a), Sn(a)); tr = sum(Rm[i][i] for i in range(3)); th = mp.acos((tr-1)/2)
    return [C(th), Sn(th)]
def n13(p):
    s, u = p; Rm = rod(u, h(s), v(s)); tr = sum(Rm[i][i] for i in range(3)); c = (tr-1)/2
    return [c, S(1-c*c)]
def tr3(M): return sum(M[i][i] for i in range(3))
def o14(p):
    s, u = p; a = At(s); Rm = rod(u, C(a), Sn(a)); K = skew(u)
    return [C(a), Sn(a), (tr3(Rm)-1)/2, -tr3(mmul(K, Rm))/2]
def n14(p):
    s, u = p; Rm = rod(u, h(s), v(s)); K = skew(u)
    return [h(s), v(s), (tr3(Rm)-1)/2, -tr3(mmul(K, Rm))/2]
def o12(p):
    a, b, g = [At(x) for x in p]
    ca, sa, cb, sb, cg, sg = C(a), Sn(a), C(b), Sn(b), C(g), Sn(g)
    return [ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg, sa*cb, sa*sb*sg+ca*cg, sa*sb*cg-ca*sg, -sb, cb*sg, cb*cg]
def n12(p):
    ca, sa, cb, sb, cg, sg = h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2])
    return [ca*cb, ca*sb*sg-sa*cg, ca*sb*cg+sa*sg, sa*cb, sa*sb*sg+ca*cg, sa*sb*cg-ca*sg, -sb, cb*sg, cb*cg]
def rot3(c, s_):
    return [1,0,0, 0,c,-s_, 0,s_,c,  c,0,s_, 0,1,0, -s_,0,c,  c,-s_,0, s_,c,0, 0,0,1]
AL = [R(2)/3, R(1)/3, R(-2)/3]; BE = cross(U1, AL)
def frame(c, s_): return [c*AL[i]+s_*BE[i] for i in range(3)] + [-s_*AL[i]+c*BE[i] for i in range(3)] + U1
def voigt(c, s_): return [c*c, s_*s_, 2*s_*c, s_*s_, c*c, 2*s_*c, -s_*c, s_*c, c*c-s_*s_]
def inrange(p): return 1 if 0 <= mp.atan2(p[1], p[0]) <= mp.pi else 0
def inrange_new(p): return 1 if p[1] >= 0 else 0
PT = [(R(1), R(2)), (R(-1), R('0.5')), (R(1), R(-1))]

def o47(p):
    s, ay, ER, s0 = p; th = At(s); t0 = At(s0); D = (ER-1)/(ER+1); ax, az = D*Sn(2*t0), D*C(2*t0)
    n = [Sn(2*th), 0, C(2*th)]; Rn = mp.expm(-J1*(mp.pi/4)*ndots(n))
    a = [ax, ay, az]; rho = (I2 + adot(a))/2; Tt = (Rn*rho*dag(Rn))[0, 0].real
    T1 = (1 + ay*Sn(2*th) + (ax*Sn(2*th) + az*C(2*th))*C(2*th))/2
    T2 = (1 + ay*Sn(2*th) + D*(C(4*th-2*t0) + C(2*t0))/2)/2
    return [Tt, T1, T2]
def n47(p):
    s, ay, ER, s0 = p; D = (ER-1)/(ER+1)
    c0, q0 = h(s0)**2 - v(s0)**2, 2*h(s0)*v(s0); ax, az = D*q0, D*c0
    c2, q2 = h(s)**2 - v(s)**2, 2*h(s)*v(s); c4, q4 = c2*c2 - q2*q2, 2*c2*q2
    n = [q2, 0, c2]; Rn = (I2 - J1*ndots(n))/S(2)
    a = [ax, ay, az]; rho = (I2 + adot(a))/2; Tt = (Rn*rho*dag(Rn))[0, 0].real
    T1 = (1 + ay*q2 + (ax*q2 + az*c2)*c2)/2
    T2 = (1 + ay*q2 + D*(c4*c0 + q4*q0 + c0)/2)/2
    return [Tt, T1, T2]
def o50(p):
    n, a = p; Rn = mp.expm(-J1*(mp.pi/2)*ndots(n)); rho = (I2 + adot(a))/2
    return fl(Rn*rho*dag(Rn))
def n50(p):
    n, a = p; nd = dot(n, a)
    return fl((I2 - adot(a) + 2*nd*ndots(n))/2)
NA = [(U1, [R('0.1'), R('0.3'), R('-0.5')]), (U2, [R('0.6'), R('-0.2'), R('0.1')]), (U3, [R('-0.3'), R('0.4'), R('0.7')])]
def o54(p):
    a, b, f = [At(x) for x in p]; E = mp.expj
    c, s_ = C(b), Sn(b)
    L = [E(-a/2)*(c*c + E(a)*s_*s_), E(-a/2)*(1-E(a))*E(-f)*c*s_, E(-a/2)*(1-E(a))*E(f)*c*s_, E(-a/2)*(s_*s_ + E(a)*c*c)]
    Rr = [C(a/2) - J1*Sn(a/2)*C(2*b), -Sn(a/2)*Sn(f)*Sn(2*b) - J1*Sn(a/2)*C(f)*Sn(2*b),
          Sn(a/2)*Sn(f)*Sn(2*b) - J1*Sn(a/2)*C(f)*Sn(2*b), C(a/2) + J1*Sn(a/2)*C(2*b)]
    return L + Rr
def n54(p):
    sa, sb, sf = p
    wa = h(sa) + J1*v(sa); wh = hh(sa) - J1*hv_(sa); ch, sh = hh(sa), hv_(sa)
    wf = h(sf) + J1*v(sf); wfb = h(sf) - J1*v(sf); c, s_ = h(sb), v(sb); c2b, s2b = c*c - s_*s_, 2*c*s_
    L = [wh*(c*c + wa*s_*s_), wh*(1-wa)*wfb*c*s_, wh*(1-wa)*wf*c*s_, wh*(s_*s_ + wa*c*c)]
    Rr = [ch - J1*sh*c2b, -sh*v(sf)*s2b - J1*sh*h(sf)*s2b, sh*v(sf)*s2b - J1*sh*h(sf)*s2b, ch + J1*sh*c2b]
    return L + Rr
P3x3 = [(R('0.3'), R('-0.8'), R('1.2')), (R('1.7'), R('0.4'), R('-2')), (R('5'), R('2.5'), R('0.1'))]
def o57(p):
    a, b, l = [At(x) for x in p]; d = mp.acos(Sn(a)*Sn(b) + C(a)*C(b)*C(l)); return [C(d), Sn(d)]
def n57(p):
    c = v(p[0])*v(p[1]) + h(p[0])*h(p[1])*h(p[2]); return [c, S(1-c*c)]
def o59(p):
    a, b, l = [At(x) for x in p]; df = b - a
    return [2*S(Sn(df/2)**2 + C(a)*C(b)*Sn(l/2)**2), 2*S((Sn(l/2)*C((a+b)/2))**2 + (C(l/2)*Sn(df/2))**2)]
def n59(p):
    s1, s2, sl = p; h1, v1, h2, v2, hl = h(s1), v(s1), h(s2), v(s2), h(sl)
    cdf = h1*h2 + v1*v2; sdf2 = (1-cdf)/2; sl2 = (1-hl)/2; cl2 = (1+hl)/2; csum2 = (1 + h1*h2 - v1*v2)/2
    return [2*S(sdf2 + h1*h2*sl2), 2*S(sl2*csum2 + cl2*sdf2)]
def o60(p):
    a, b, l = [At(x) for x in p]
    d = mp.atan2(S((C(b)*Sn(l))**2 + (C(a)*Sn(b) - Sn(a)*C(b)*C(l))**2), Sn(a)*Sn(b) + C(a)*C(b)*C(l)); return [C(d), Sn(d)]
def n60(p):
    s1, s2, sl = p; h1, v1, h2, v2, hl, vl = h(s1), v(s1), h(s2), v(s2), h(sl), v(sl)
    num = S((h2*vl)**2 + (h1*v2 - v1*h2*hl)**2); den = v1*v2 + h1*h2*hl; r = S(num*num + den*den)
    return [den/r, num/r]
NN = [(U1, U2), (U2, U3), (U1, U3)]
def o61(p):
    a, b = p; d = dot(a, b); c = cross(a, b); n = S(dot(c, c))
    return [C(mp.acos(d)), Sn(mp.asin(n)), Tn(At(n/d))]
def n61(p):
    a, b = p; d = dot(a, b); c = cross(a, b); n = S(dot(c, c)); return [d, n, n/d]
P4 = [(R('0.3'), R('0.7'), R('-1.1'), R('2')), (R('1.7'), R('-0.4'), R('0.2'), R('5')), (R('5'), R('3'), R('-0.6'), R('-0.9'))]
def o62(p):
    f1, l1, f2, l2 = [At(x) for x in p]
    dX = C(f2)*C(l2) - C(f1)*C(l1); dY = C(f2)*Sn(l2) - C(f1)*Sn(l1); dZ = Sn(f2) - Sn(f1); return [dX, dY, dZ, S(dX**2+dY**2+dZ**2)]
def n62(p):
    f1, l1, f2, l2 = p
    dX = h(f2)*h(l2) - h(f1)*h(l1); dY = h(f2)*v(l2) - h(f1)*v(l1); dZ = v(f2) - v(f1); return [dX, dY, dZ, S(dX**2+dY**2+dZ**2)]
def o67(p):
    fo, lo, fs, ls = [At(x) for x in p]
    Sv = [C(fs)*C(ls), C(fs)*Sn(ls), Sn(fs)]; V = [C(fo)*C(lo), C(fo)*Sn(lo), Sn(fo)]
    return [dot(Sv, V), Sn(fo)*Sn(fs) + C(fo)*C(fs)*C(ls-lo)]
def n67(p):
    fo, lo, fs, ls = p
    Sv = [h(fs)*h(ls), h(fs)*v(ls), v(fs)]; V = [h(fo)*h(lo), h(fo)*v(lo), v(fo)]
    return [dot(Sv, V), v(fo)*v(fs) + h(fo)*h(fs)*(h(ls)*h(lo) + v(ls)*v(lo))]
P2 = [(R('0.3'), R('0.7')), (R('1.7'), R('-0.4')), (R('-2'), R('0.25'))]
def o70(p):
    a, b = [At(x) for x in p]; h0 = mp.acos(-Tn(a)*Tn(b)); return [C(h0), Sn(h0)]
def n70(p):
    c = -p[0]*p[1]; return [c, S(1-c*c)]
def dbl(c, s_): return [c*c - s_*s_, 2*c*s_]
EC = [R('1.3'), R('2'), R('7')]
def o73(e_): a = 2*mp.acos(-1/e_); return [C(a), Sn(a)]
def n73(e_): c = -1/e_; return dbl(c, S(1-c*c))
def o75(e_): th = mp.acos(-1/e_); a = 2*th - mp.pi; return [C(a), Sn(a)]
def n75(e_): c = -1/e_; s_ = S(1-c*c); d = dbl(c, s_); return [-d[0], -d[1]]
def o76(p):
    rp, vi, mu = p; a = 2*mp.asin(1/(1 + rp*vi**2/mu)); return [C(a), Sn(a)]
def n76(p):
    rp, vi, mu = p; q = 1/(1 + rp*vi**2/mu); return dbl(S(1-q*q), q)
P3b = [(R('0.5'), R('2'), R('1')), (R('3'), R('1.5'), R('4')), (R('0.1'), R('7'), R('2'))]
def o82(p):
    s, e_ = p; a = At(s); E = mp.acosh((C(a)+e_)/(1+e_*C(a))); return mp.tanh(E)
def n82(p):
    s, e_ = p; Cc = (h(s)+e_)/(1+e_*h(s)); return S(Cc*Cc-1)/Cc
SE = [(R('0.3'), R('1.5')), (R('1.7'), R('3')), (R('5'), R('1.1'))]
def o83(p):
    u, e_ = p; E = mp.atanh(u); th = 2*At(S((e_+1)/(e_-1))*mp.tanh(E/2)); return [C(th), Sn(th)]
def n83(p):
    u, e_ = p; t = S((e_+1)/(e_-1))*u/(1+S(1-u*u)); return [(1-t*t)/(1+t*t), 2*t/(1+t*t)]
UE = [(R('0.3'), R('1.5')), (R('-0.7'), R('3')), (R('0.95'), R('1.1'))]
def o84(p):
    s, e_ = p; E = 2*mp.atanh(S((e_-1)/(e_+1))*Tn(At(s)/2)); return mp.tanh(E)
def n84(p):
    s, e_ = p; w = S((e_-1)/(e_+1))*tt(s); return 2*w/(1+w*w)
def o87(p):
    pe, Rs, mu, vi = p
    X = S(1-pe/Rs)*S(1+pe/Rs-2*mu*pe/(vi**2*Rs**2))/(1+vi**2*pe/mu-2*pe/Rs); d = 2*mp.asin(X); return [C(d), Sn(d)]
def n87(p):
    pe, Rs, mu, vi = p
    X = S(1-pe/Rs)*S(1+pe/Rs-2*mu*pe/(vi**2*Rs**2))/(1+vi**2*pe/mu-2*pe/Rs); return dbl(S(1-X*X), X)
P87 = [(R(1), R(10), R(1), R(1)), (R(2), R(50), R(3), R('1.5')), (R('0.5'), R(5), R(2), R('0.7'))]
PU = [R('0.3'), R('-0.6'), R('0.9')]
ch_ = lambda u: mp.cosh(mp.atanh(u)); sh_ = lambda u: mp.sinh(mp.atanh(u))
def gC(u): return 1/S(1-u*u)
def gS(u): return u/S(1-u*u)
P90 = [(R(1), R(2), R('0.3'), R('-0.2'), R('0.5'), R('0.1')), (R(3), R('0.5'), R('-0.6'), R('0.7'), R('0.2'), R('-0.9')),
       (R('1.5'), R(4), R('0.9'), R('0.05'), R('-0.4'), R('0.8'))]
def o90(p):
    m1, m2, a, b, c, d = p
    return [m1*ch_(a)+m2*ch_(b), m1*ch_(c)+m2*ch_(d), m1*sh_(a)+m2*sh_(b), m1*sh_(c)+m2*sh_(d)]
def n90(p):
    m1, m2, a, b, c, d = p
    return [m1*gC(a)+m2*gC(b), m1*gC(c)+m2*gC(d), m1*gS(a)+m2*gS(b), m1*gS(c)+m2*gS(d)]
def o92(p):
    m1, m2, a, b, c, d = p
    return [2*m1*m2*(ch_(a)*ch_(b)-sh_(b)*sh_(a)), 2*m1*m2*(ch_(c)*ch_(d)-sh_(d)*sh_(c))]
def n92(p):
    m1, m2, a, b, c, d = p
    return [2*m1*m2*(gC(a)*gC(b)-gS(b)*gS(a)), 2*m1*m2*(gC(c)*gC(d)-gS(d)*gS(c))]
def o93(p):
    m1, m2, a, b, c, d = p; A = mp.atanh
    return [mp.cosh(A(a)-A(b)), mp.cosh(A(c)-A(d))]
def n93(p):
    m1, m2, a, b, c, d = p
    return [(1-a*b)/S((1-a*a)*(1-b*b)), (1-c*d)/S((1-c*c)*(1-d*d))]
def o94(p):
    out = []
    for u in p:
        s_ = mp.atanh(u); out += [mp.tanh(s_), (mp.exp(s_)-mp.exp(-s_))/(mp.exp(s_)+mp.exp(-s_))]
    return out
def n94(p):
    out = []
    for u in p:
        k = S((1+u)/(1-u)); out += [u, (k-1/k)/(k+1/k)]
    return out
P94 = [(R('0.3'), R('-0.2')), (R('-0.6'), R('0.7')), (R('0.9'), R('0.05'))]
def o95(p):
    u1, c = p; return [mp.exp(mp.atanh(u1/c)), S((c+u1)/(c-u1))]
def n95(p):
    u1, c = p; w = u1/c; return [S((1+w)/(1-w)), S((c+u1)/(c-u1))]
P95 = [(R('0.3'), R(1)), (R('-2'), R(3)), (R(250), R(299))]
def o97(p):
    m1, m2, s = p; a = At(s); return [m2*Sn(a)/(m1+m2*C(a)), Tn((mp.pi-a)/2)]
def n97(p):
    m1, m2, s = p; return [m2*v(s)/(m1+m2*h(s)), (1+h(s))/v(s)]
P97 = [(R(1), R(2), R('0.3')), (R(3), R('0.5'), R('1.7')), (R('1.5'), R(4), R(-5))]
def o98(p):
    v1, m1, m2, s = p; a = At(s)
    return [v1*S(m1**2+m2**2+2*m1*m2*C(a))/(m1+m2), v1*(2*m1/(m1+m2))*Sn(a/2)]
def n98(p):
    v1, m1, m2, s = p
    return [v1*S(m1**2+m2**2+2*m1*m2*h(s))/(m1+m2), v1*(2*m1/(m1+m2))*v(s)/S(2*(1+h(s)))]
P98 = [(R(2), R(1), R(2), R('0.3')), (R(5), R(3), R('0.5'), R('1.7')), (R('0.7'), R('1.5'), R(4), R(-5))]
P117 = [(R('7.3'), R('0.3'), R(1), R(2), R(-3)), (R(1), R('1.7'), R('-0.5'), R('0.4'), R(2)), (R(2), R(-5), R(3), R(-1), R('0.2'))]
def o117(p):
    w, s, ve, vn, vu = p; a = At(s); Om = [0, w*C(a), w*Sn(a)]; V = [ve, vn, vu]
    return [-2*x for x in cross(Om, V)] + [2*w*(vn*Sn(a)-vu*C(a)), -2*w*ve*Sn(a), 2*w*ve*C(a)]
def n117(p):
    w, s, ve, vn, vu = p; Om = [0, w*h(s), w*v(s)]; V = [ve, vn, vu]
    return [-2*x for x in cross(Om, V)] + [2*w*(vn*v(s)-vu*h(s)), -2*w*ve*v(s), 2*w*ve*h(s)]
P118 = [(R('7.3'), R('0.3'), R('1.2'), R(1), R(2), R(-3)), (R(1), R('1.7'), R(-2), R('-0.5'), R('0.4'), R(2)),
        (R(2), R(-5), R('0.25'), R(3), R(-1), R('0.2'))]
def o118(p):
    w, st, sp, X, Y, Z = p; t, f = At(st), At(sp)
    return [-2*w*(Y*C(t)*Sn(f) + Z*Sn(t)), 2*w*(X*C(t)*Sn(f) + Z*C(t)*C(f)), 2*w*(X*Sn(t) - Y*C(t)*C(f))]
def n118(p):
    w, st, sp, X, Y, Z = p; ht, vt, hf, vf = h(st), v(st), h(sp), v(sp)
    return [-2*w*(Y*ht*vf + Z*vt), 2*w*(X*ht*vf + Z*ht*hf), 2*w*(X*vt - Y*ht*hf)]
AB = [(mp.mpc('0.6', '0'), mp.mpc('0', '0.8')), (mp.mpc('0.3', '0.4'), mp.mpc('0.5', '-0.5')*S(R(75)/50)), (mp.mpc(1, 0), mp.mpc(0, 0))]
P55 = [(R('0.3'),) + AB[0], (R('1.7'),) + AB[1], (R(-5),) + AB[2]]

AXP = [(R('0.3'), U1), (R('1.7'), U2), (R(-5), U3)]
AXX = [(R('0.3'), U1, X0), (R('1.7'), U2, [R(1), R(0), R('0.5')]), (R(-5), U3, [R(-2), R(3), R('0.7')])]

LAWS = [
T(1, 'a direction\'s turn by its shares', 'R = [[h, -v], [v, h]] with h, v the shares of the turn s',
  lambda s: rot2(C(At(s)), Sn(At(s))), lambda s: rot2(h(s), v(s)), P3),
T(2, 'polar x by the direction\'s share', 'x = r*h', lambda p: p[0]*C(At(p[1])), lambda p: p[0]*h(p[1]), pts2),
T(3, 'polar y by the direction\'s share', 'y = r*v', lambda p: p[0]*Sn(At(p[1])), lambda p: p[0]*v(p[1]), pts2),
T(4, 'turn composition in shares', 'Rv = r*(h1*h2 - v1*v2, h1*v2 + v1*h2)',
  lambda p: [p[0]*C(At(p[1])+At(p[2])), p[0]*Sn(At(p[1])+At(p[2])),
             p[0]*(C(At(p[1]))*C(At(p[2]))-Sn(At(p[1]))*Sn(At(p[2]))), p[0]*(C(At(p[1]))*Sn(At(p[2]))+Sn(At(p[1]))*C(At(p[2])))],
  lambda p: [p[0]*(h(p[1])*h(p[2])-v(p[1])*v(p[2])), p[0]*(h(p[1])*v(p[2])+v(p[1])*h(p[2]))]*2,
  [(R(2), R('0.3'), R('1.7')), (R(3), R('-0.4'), R(5)), (R('0.5'), R(2), R(3))]),
T(5, 'rotated coordinates by shares', "x' = x*h - y*v, y' = x*v + y*h",
  lambda p: [p[0]*C(At(p[2]))-p[1]*Sn(At(p[2])), p[0]*Sn(At(p[2]))+p[1]*C(At(p[2]))],
  lambda p: [p[0]*h(p[2])-p[1]*v(p[2]), p[0]*v(p[2])+p[1]*h(p[2])],
  [(R(1), R(2), R('0.3')), (R(-3), R('0.5'), R('1.7')), (R('0.2'), R(4), R(-5))]),
T(6, 'the reversed direction keeps its h share', 'h(-s) = h(s)', lambda s: [C(-At(s)), C(At(s))], lambda s: [h(-s), h(s)], P3),
T(7, 'reverse turn by shares', 'R(-s) = [[h, v], [-v, h]]',
  lambda s: rot2(C(-At(s)), Sn(-At(s))), lambda s: [h(s), v(s), -v(s), h(s)], P3),
T(8, 'h I + v J', 'R = h*[[1,0],[0,1]] + v*[[0,-1],[1,0]]',
  lambda s: [C(At(s))*1 + Sn(At(s))*0, C(At(s))*0 + Sn(At(s))*(-1), Sn(At(s))*1, C(At(s))] + rot2(C(At(s)), Sn(At(s))),
  lambda s: [h(s), -v(s), v(s), h(s)] + rot2(h(s), v(s)), P3),
T(9, 'shares square-sum to one', 'h^2 + v^2 = 1', lambda s: C(At(s))**2 + Sn(At(s))**2, lambda s: h(s)**2 + v(s)**2, P3),
T(10, 'the direction\'s landing point and its matrix', 'w = h + i*v = h*I + v*J = [[h, -v], [v, h]]',
  lambda s: [mp.expj(At(s)), C(At(s)) + J1*Sn(At(s))] + rot2(C(At(s)), Sn(At(s))),
  lambda s: [h(s) + J1*v(s), h(s) + J1*v(s)] + rot2(h(s), v(s)), P3),
T(11, 'basic 3D turns by shares', 'R_x, R_y, R_z with h, v in place of the trigonometric entries',
  lambda s: rot3(C(At(s)), Sn(At(s))), lambda s: rot3(h(s), v(s)), P3),
T(12, 'yaw-pitch-roll by shares', 'R entries as products of the three directions\' shares', o12, n12, P3x3),
T(13, 'call 1: the turn\'s share from the trace', 'h = (tr R - 1)/2, v = sqrt(1 - h^2)', o13, n13, AXP),
T(14, 'shares from traces', 'h = (tr R - 1)/2, v = -tr(K_n R)/2', o14, n14, AXP),
T(15, 'axis-angle matrix by shares', 'R entries with h for the turn\'s first share and v for its second',
  lambda p: fl(rod(p[1], C(At(p[0])), Sn(At(p[0])))), lambda p: fl(rod(p[1], h(p[0]), v(p[0]))), AXP),
T(16, 'compact axis-angle by shares', 'R = h I + v [u]x + (1 - h)(u u)',
  lambda p: fl(compact(p[1], C(At(p[0])), Sn(At(p[0])))), lambda p: fl(compact(p[1], h(p[0]), v(p[0]))), AXP),
T(17, 'half-turn squared shares (1 + h)/2 and (1 - h)/2', 'R_jj = (1+h)/2 + (1-h)/2*(2u_j^2 - 1); R_jk = 2u_j u_k (1-h)/2 - eps_jkl u_l v',
  lambda p: fl(halfR(p[1], C(At(p[0])/2)**2, Sn(At(p[0])/2)**2, Sn(At(p[0])))),
  lambda p: fl(halfR(p[1], (1+h(p[0]))/2, (1-h(p[0]))/2, v(p[0]))), AXP),
T(18, 'Rodrigues by shares', 'R x = u(u.x) + h (u x x) x u + v (u x x)',
  lambda p: [p[1][i]*dot(p[1], p[2]) + C(At(p[0]))*cross(cross(p[1], p[2]), p[1])[i] + Sn(At(p[0]))*cross(p[1], p[2])[i] for i in range(3)],
  lambda p: [p[1][i]*dot(p[1], p[2]) + h(p[0])*cross(cross(p[1], p[2]), p[1])[i] + v(p[0])*cross(p[1], p[2])[i] for i in range(3)], AXX),
T(19, 'Rodrigues second form by shares', 'R x = x h + u(x.u)(1 - h) - (x x u) v',
  lambda p: [p[2][i]*C(At(p[0])) + p[1][i]*dot(p[2], p[1])*(1-C(At(p[0]))) - cross(p[2], p[1])[i]*Sn(At(p[0])) for i in range(3)],
  lambda p: [p[2][i]*h(p[0]) + p[1][i]*dot(p[2], p[1])*(1-h(p[0])) - cross(p[2], p[1])[i]*v(p[0]) for i in range(3)], AXX),
T(20, 'frame turned by shares', 'R alpha = h alpha + v beta, R beta = -v alpha + h beta, R u = u',
  lambda s: frame(C(At(s)), Sn(At(s))), lambda s: frame(h(s), v(s)), P3),
T(21, 'call 2: the 30-degree turn is the direction with shares (sqrt3/2, 1/2)', 'Q = [[1,0,0],[0,sqrt(3)/2,1/2],[0,-1/2,sqrt(3)/2]]',
  lambda x: [1, 0, 0, 0, C(mp.pi/6), Sn(mp.pi/6), 0, -Sn(mp.pi/6), C(mp.pi/6)],
  lambda x: [1, 0, 0, 0, S(3)/2, R(1)/2, 0, -R(1)/2, S(3)/2], D3),
T(22, 'three shears with the half-slope t = v/(1 + h)', 'R = [[1,-t],[0,1]] [[1,0],[v,1]] [[1,-t],[0,1]]',
  lambda s: fl(mmul(mmul([[1, -Tn(At(s)/2)], [0, 1]], [[1, 0], [Sn(At(s)), 1]]), [[1, -Tn(At(s)/2)], [0, 1]])),
  lambda s: fl(mmul(mmul([[1, -tt(s)], [0, 1]], [[1, 0], [v(s), 1]]), [[1, -tt(s)], [0, 1]])), P3),
T(23, 'shear, shear and scaling by the slope and shares', 'R = [[1,0],[s,1]] [[1,-h v],[0,1]] [[h,0],[0,1/h]]',
  lambda s: fl(mmul(mmul([[1, 0], [Tn(At(s)), 1]], [[1, -Sn(At(s))*C(At(s))], [0, 1]]), [[C(At(s)), 0], [0, 1/C(At(s))]])),
  lambda s: fl(mmul(mmul([[1, 0], [s, 1]], [[1, -h(s)*v(s)], [0, 1]]), [[h(s), 0], [0, 1/h(s)]])), P3),
N(24, 'the exponential of a general matrix A against the Cayley map, a series remainder O(A^4): an approximation, not a relation among directions'),
T(25, 'the skew generator\'s turn written by its shares (the exponential of an angle generator)', 'R = I + v (u.L) + (1 - h)(u.L)^2',
  lambda p: fl(mp.expm(At(p[0])*mp.matrix(skew(p[1])))),
  lambda p: fl([[I3()[i][j] + v(p[0])*skew(p[1])[i][j] + (1-h(p[0]))*mmul(skew(p[1]), skew(p[1]))[i][j] for j in range(3)] for i in range(3)]), AXP),
T(26, 'Voigt rotation by shares', 'T = [[h^2, v^2, 2hv],[v^2, h^2, 2hv],[-hv, hv, h^2 - v^2]]',
  lambda s: voigt(C(At(s)), Sn(At(s))), lambda s: voigt(h(s), v(s)), P3),
T(27, 'call 2: the half-turn range as v >= 0', 'the direction (h, v) has v >= 0', inrange, inrange_new, PT),
T(28, 'qubit state by half-turn shares and the azimuth\'s landing point', 'psi = hh|0> + (h_phi + i v_phi) hv|1>, hh, hv the half-turn shares',
  lambda p: [C(At(p[0])/2), mp.expj(At(p[1]))*Sn(At(p[0])/2), (C(At(p[1])) + J1*Sn(At(p[1])))*Sn(At(p[0])/2)],
  lambda p: [hh(p[0]), (h(p[1]) + J1*v(p[1]))*hv_(p[0]), (h(p[1]) + J1*v(p[1]))*hv_(p[0])], P2),
T(29, 'call 2: the polar range as v >= 0', 'the direction (h, v) has v >= 0', inrange, inrange_new, PT),
T(30, 'call 2: the full turn is every direction once', 'every direction (h, v) with h^2 + v^2 = 1, each once',
  lambda p: 1 if 0 <= (mp.atan2(p[1], p[0]) % (2*mp.pi)) < 2*mp.pi else 0, lambda p: 1 if p[0]**2 + p[1]**2 > 0 else 0, PT),
T(31, 'Bloch vector by shares', 'a = (v_th h_ph, v_th v_ph, h_th)',
  lambda p: [Sn(At(p[0]))*C(At(p[1])), Sn(At(p[0]))*Sn(At(p[1])), C(At(p[0]))], lambda p: [v(p[0])*h(p[1]), v(p[0])*v(p[1]), h(p[0])], P2),
T(32, 'density matrix by shares', 'rho = [[(1+h)/2, (v/2)(h_ph - i v_ph)], [(v/2)(h_ph + i v_ph), (1-h)/2]]',
  lambda p: [C(At(p[0])/2)**2, Sn(At(p[0])/2)*C(At(p[0])/2)*mp.expj(-At(p[1])), Sn(At(p[0])/2)*C(At(p[0])/2)*mp.expj(At(p[1])), Sn(At(p[0])/2)**2],
  lambda p: [(1+h(p[0]))/2, (v(p[0])/2)*(h(p[1]) - J1*v(p[1])), (v(p[0])/2)*(h(p[1]) + J1*v(p[1])), (1-h(p[0]))/2], P2),
T(33, 'height is the h share', 'z = h', lambda s: C(At(s)), lambda s: h(s), P3),
T(34, 'Born probability by the half-turn share', '|<0|psi>|^2 = (1 + h)/2 = (1 + z)/2',
  lambda s: [C(At(s)/2)**2, (1+C(At(s)))/2], lambda s: [(1+h(s))/2, (1+h(s))/2], P3),
T(35, 'the turn about n written by its half-turn shares', 'R = hh I - i hv (n.sigma)',
  lambda p: fl(mp.expm(-J1*At(p[0])/2*ndots(p[1]))), lambda p: fl(hh(p[0])*I2 - J1*hv_(p[0])*ndots(p[1])), AXP),
N(36, 'U(s) = exp(iKs) with s a group parameter and K a general generator: the exponential of an amount'),
T(37, 'the doubled direction\'s landing point', 'L = |L| ((h^2 - v^2) + i 2hv) = Q + iU',
  lambda p: [(p[0]*mp.expj(2*At(p[1]))).real, (p[0]*mp.expj(2*At(p[1]))).imag],
  lambda p: [p[0]*(h(p[1])**2 - v(p[1])**2), p[0]*2*h(p[1])*v(p[1])], pts2),
T(38, 'turn of axes as the doubled landing point', "L -> (h' + i v')^2 L",
  lambda p: [(mp.expj(2*At(p[2]))*(p[0]+J1*p[1])).real, (mp.expj(2*At(p[2]))*(p[0]+J1*p[1])).imag],
  lambda p: [((h(p[2])+J1*v(p[2]))**2*(p[0]+J1*p[1])).real, ((h(p[2])+J1*v(p[2]))**2*(p[0]+J1*p[1])).imag],
  [(R(1), R(2), R('0.3')), (R(-3), R('0.5'), R('1.7')), (R('0.2'), R(4), R(-5))]),
T(39, 'Stokes by doubled shares', 'Q = (A^2 - B^2)(h^2 - v^2), U = (A^2 - B^2) 2hv',
  lambda p: [(p[0]**2-p[1]**2)*C(2*At(p[2])), (p[0]**2-p[1]**2)*Sn(2*At(p[2]))],
  lambda p: [(p[0]**2-p[1]**2)*(h(p[2])**2-v(p[2])**2), (p[0]**2-p[1]**2)*2*h(p[2])*v(p[2])],
  [(R(2), R(1), R('0.3')), (R(3), R('0.5'), R('1.7')), (R(1), R(4), R(-5))]),
T(40, 'call 2: polarizers at the directions (1,0), (1/sqrt2,1/sqrt2), (0,1)', 'I_l = (I + Q(h^2 - v^2) + U(2hv))/2 at those directions; I_q = (I + V)/2',
  lambda p: [(p[0] + p[1]*C(2*t) + p[2]*Sn(2*t))/2 for t in (0, mp.pi/4, mp.pi/2)] + [(p[0] + p[3]*Sn(2*mp.pi/4))/2],
  lambda p: [(p[0] + p[1]*(c*c - s_*s_) + p[2]*2*c*s_)/2 for c, s_ in ((1, 0), (1/S(2), 1/S(2)), (0, 1))] + [(p[0] + p[3])/2],
  [(R(1), R('0.3'), R('-0.2'), R('0.5')), (R(2), R(1), R('0.4'), R(-1)), (R(5), R(-2), R(3), R('0.1'))]),
T(41, 'polarization state by shares', '|th> = h|H> + v|V>', lambda s: [C(At(s)), Sn(At(s))], lambda s: [h(s), v(s)], P3),
T(42, 'call 1: the doubled direction\'s slope is a_x/a_z, so theta0\'s half-slope', 'half-slope of theta0 = q/(1 + sqrt(1 + q^2)), q = a_x/a_z (doubled slope q)',
  lambda p: Tn(At(p[0]/p[1])/2), lambda p: tt(p[0]/p[1]), [(R('0.3'), R(1)), (R(2), R('0.5')), (R(-1), R(3))]),
T(43, 'components by doubled shares', 'a_x = D 2hv, a_z = D (h^2 - v^2), D = (ER - 1)/(ER + 1)',
  lambda p: [(p[0]-1)/(p[0]+1)*Sn(2*At(p[1])), (p[0]-1)/(p[0]+1)*C(2*At(p[1]))],
  lambda p: [(p[0]-1)/(p[0]+1)*2*h(p[1])*v(p[1]), (p[0]-1)/(p[0]+1)*(h(p[1])**2-v(p[1])**2)],
  [(R(3), R('0.3')), (R(10), R('1.7')), (R('1.5'), R(-5))]),
T(44, 'the doubled Bloch turn by the single direction\'s shares', 'R_y = [[h, -v], [v, h]]',
  lambda s: fl(mp.expm(-J1*At(s)*SY)), lambda s: [h(s), -v(s), v(s), h(s)], P3),
T(45, 'call 2: the quarter-wave retarder has half-turn shares (1/sqrt2, 1/sqrt2)', 'R_n = (1/sqrt(2)) I - i (1/sqrt(2)) (n.sigma)',
  lambda n: fl(mp.expm(-J1*(mp.pi/4)*ndots(n))), lambda n: fl((I2 - J1*ndots(n))/S(2)), [U1, U2, U3]),
T(46, 'axis by doubled shares', 'n = z (h^2 - v^2) + x (2hv)',
  lambda s: [Sn(2*At(s)), 0, C(2*At(s))], lambda s: [2*h(s)*v(s), 0, h(s)**2 - v(s)**2], P3),
T(47, 'transmittance by doubled and quadrupled shares, the retarder by call 2', 'T = (1 + a_y q2 + (a_x q2 + a_z c2) c2)/2 = (1 + a_y q2 + D (c4 c0 + q4 q0 + c0)/2)/2',
  o47, n47, [(R('0.3'), R('0.2'), R(3), R('0.7')), (R('1.7'), R('-0.4'), R(10), R('-0.2')), (R(-5), R('0.1'), R('1.5'), R(2))]),
T(48, 'call 2: theta0 is the direction (0, 1)', 'theta0 has shares (h, v) = (0, 1)',
  lambda x: [C(mp.pi/2), Sn(mp.pi/2)], lambda x: [R(0), R(1)], D3),
T(49, 'transmittance by the quadrupled share', 'T = (1 - c4)/4, c4 = (h^2 - v^2)^2 - (2hv)^2',
  lambda s: (1 - C(4*At(s)))/4, lambda s: (1 - ((h(s)**2-v(s)**2)**2 - (2*h(s)*v(s))**2))/4, P3),
T(50, 'call 2: the half-wave retarder is R_n = -i n.sigma', 'R_n rho R_n^dagger = (I - a.sigma + 2(n.a)(n.sigma))/2', o50, n50, NA),
N(51, 'the phase kz - wt is an amount (distance and time); the exponential of an amount'),
T(52, 'call 2: a quarter-turn lead multiplies the landing point by i', 'w_y = i w_x, w_x = h + i v',
  lambda s: [mp.expj(At(s)+mp.pi/2).real, mp.expj(At(s)+mp.pi/2).imag],
  lambda s: [(J1*(h(s)+J1*v(s))).real, (J1*(h(s)+J1*v(s))).imag], P3),
T(53, 'call 2: the delays are the directions (1/sqrt2, +-1/sqrt2)', 'w_x = (1 + i)/sqrt(2), w_y = (1 - i)/sqrt(2)',
  lambda x: [mp.expj(mp.pi/4), mp.expj(-mp.pi/4)], lambda x: [(1+J1)/S(2), (1-J1)/S(2)], D3),
T(54, 'retarder by shares and half-turn shares of eta', 'both matrices with the landing points h + iv and the half-turn shares in place of the phase factors', o54, n54, P3x3),
T(55, 'the group\'s phase factor as a landing point w = h + i v', '{w [[alpha, -conj beta], [beta, conj alpha]] : |alpha|^2 + |beta|^2 = 1, |w| = 1}',
  lambda p: [mp.expj(At(p[0]))*x for x in (p[1], -mp.conj(p[2]), p[2], mp.conj(p[1]))],
  lambda p: [(h(p[0]) + J1*v(p[0]))*x for x in (p[1], -mp.conj(p[2]), p[2], mp.conj(p[1]))], P55),
T(56, 'Jones rotation by shares', 'R = [[h, v], [-v, h]]',
  lambda s: [C(At(s)), Sn(At(s)), -Sn(At(s)), C(At(s))], lambda s: [h(s), v(s), -v(s), h(s)], P3),
T(57, 'call 1: the central direction\'s share', 'h_sigma = v1 v2 + h1 h2 h_dl', o57, n57, P3x3),
T(58, 'haversine as (1 - h)/2', 'hav = (1 - h)/2', lambda s: Sn(At(s)/2)**2, lambda s: (1 - h(s))/2, P3),
T(59, 'chord by shares', 'c = 2 sqrt((1 - h1h2 - v1v2)/2 + h1 h2 (1 - h_l)/2) = 2 sqrt(((1-h_l)/2)((1 + h1h2 - v1v2)/2) + ((1+h_l)/2)((1 - h1h2 - v1v2)/2))',
  o59, n59, P3x3),
T(60, 'call 1: the central direction as the pair (den, num)', 'direction of sigma = (den, num)/sqrt(den^2 + num^2)', o60, n60, P3x3),
T(61, 'call 1: shares from dot and cross', 'h = n1.n2, v = |n1 x n2|, slope = |n1 x n2|/(n1.n2)', o61, n61, NN),
T(62, 'Cartesian chord by shares', 'dX = h2 h_l2 - h1 h_l1, dY = h2 v_l2 - h1 v_l1, dZ = v2 - v1', o62, n62, P4),
T(63, 'zenith share', 'h_z = v_Phi v_d + h_Phi h_d h_h',
  lambda p: Sn(At(p[0]))*Sn(At(p[1])) + C(At(p[0]))*C(At(p[1]))*C(At(p[2])), lambda p: v(p[0])*v(p[1]) + h(p[0])*h(p[1])*h(p[2]), P3x3),
T(64, 'noon zenith share', 'h_z = v_Phi v_d + h_Phi h_d',
  lambda p: [Sn(At(p[0]))*Sn(At(p[1])) + C(At(p[0]))*C(At(p[1])), C(At(p[0]) - At(p[1]))],
  lambda p: [v(p[0])*v(p[1]) + h(p[0])*h(p[1])]*2, P2),
T(65, 'subsolar vector by shares', 'S = (h_f h_l, h_f v_l, v_f)',
  lambda p: [C(At(p[0]))*C(At(p[1])), C(At(p[0]))*Sn(At(p[1])), Sn(At(p[0]))], lambda p: [h(p[0])*h(p[1]), h(p[0])*v(p[1]), v(p[0])], P2),
T(66, 'zenith vector by shares', 'V = (h_f h_l, h_f v_l, v_f)',
  lambda p: [C(At(p[0]))*C(At(p[1])), C(At(p[0]))*Sn(At(p[1])), Sn(At(p[0]))], lambda p: [h(p[0])*h(p[1]), h(p[0])*v(p[1]), v(p[0])], P2),
T(67, 'zenith share as a dot product', 'h_z = S.V = v_o v_s + h_o h_s (h_ls h_lo + v_ls v_lo)', o67, n67, P4),
T(68, 'minimum zenith share', 'h_min = h_o h_s + v_o v_s',
  lambda p: C(abs(At(p[0]) - At(p[1]))), lambda p: h(p[0])*h(p[1]) + v(p[0])*v(p[1]), P2),
T(69, 'maximum zenith share', 'h_max = -(h_o h_s - v_o v_s)',
  lambda p: C(mp.pi - abs(At(p[0]) + At(p[1]))), lambda p: -(h(p[0])*h(p[1]) - v(p[0])*v(p[1])), P2),
T(70, 'call 1: sunrise hour direction\'s share', 'h_0 = -s_Phi s_d', o70, n70, P2),
N(71, 'a mean over the hour angle taken as an amount (an integral in dh): it gives the angle h0 itself as a weight'),
T(72, 'cot as the reciprocal slope', 'mu = b v^2 / s',
  lambda p: p[0]*p[1]**2/Tn(At(p[2])), lambda p: p[0]*p[1]**2/p[2], [(R(2), R(3), R('0.3')), (R(1), R('0.5'), R('1.7')), (R(4), R(2), R(5))]),
T(73, 'call 1: the half-angle\'s share is -1/ecc, the asymptote angle its double', 'angle direction = (c^2 - (1 - c^2), 2c sqrt(1 - c^2)), c = -1/ecc', o73, n73, EC),
T(74, 'call 1: twice the direction with slope q = b/a, the full turn adds nothing', 'angle direction = ((1 - q^2)/(1 + q^2), 2q/(1 + q^2))',
  lambda q: [C(2*mp.pi + 2*At(q)), Sn(2*mp.pi + 2*At(q))], lambda q: [(1-q*q)/(1+q*q), 2*q/(1+q*q)], P3),
T(75, 'composition with the opposite facing', 'direction of (2 th - half turn) = -(h^2 - v^2, 2hv), h = -1/ecc', o75, n75, EC),
T(76, 'call 1: the half-angle\'s v share is 1/(1 + r_p v^2/mu)', 'angle direction = doubled (sqrt(1 - q^2), q)', o76, n76, P3b),
T(77, 'call 1: the asymptote direction\'s share', 'h = -1/ecc, v = sqrt(1 - 1/ecc^2)',
  lambda e_: [C(mp.acos(-1/e_)), Sn(mp.acos(-1/e_))], lambda e_: [-1/e_, S(1 - 1/e_**2)], EC),
T(78, 'eccentricity from the asymptote\'s share', 'ecc = -1/h',
  lambda s: -1/C(mp.pi - At(s)), lambda s: -1/(-h(s)), P3),
T(79, 'half-slope of the deflection', 'mu = b v^2 t, t = s/(1 + sqrt(1 + s^2))',
  lambda p: p[0]*p[1]**2*Tn(At(p[2])/2), lambda p: p[0]*p[1]**2*tt(p[2]), [(R(2), R(3), R('0.3')), (R(1), R('0.5'), R('1.7')), (R(4), R(2), R(5))]),
T(80, 'composition with the opposite facing', 'direction of delta = -(h^2 - v^2, 2hv), h = -1/ecc', o75, n75, EC),
T(81, 'orbit equation by the share', 'r = l/(1 + ecc h)',
  lambda p: p[0]/(1 + p[1]*C(At(p[2]))), lambda p: p[0]/(1 + p[1]*h(p[2])), [(R(2), R('1.3'), R('0.3')), (R(1), R(3), R('1.7')), (R(4), R('0.5'), R(-5))]),
T(82, 'call 1: the hyperbolic anomaly\'s slope u = tanh E', '1/sqrt(1 - u^2) = (h + ecc)/(1 + ecc h)', o82, n82, SE),
T(83, 'half-slopes on both sides', 't = sqrt((ecc+1)/(ecc-1)) u/(1 + sqrt(1 - u^2))', o83, n83, UE),
T(84, 'half-slopes on both sides', 'w = sqrt((ecc-1)/(ecc+1)) t, slope u = 2w/(1 + w^2)', o84, n84, SE),
N(85, 'Kepler\'s equation subtracts the anomaly E itself as an amount (e sinh E - E): no slope restates it'),
T(86, 'flight path slope', 'slope = ecc v/(1 + ecc h)',
  lambda p: p[0]*Sn(At(p[1]))/(1 + p[0]*C(At(p[1]))), lambda p: p[0]*v(p[1])/(1 + p[0]*h(p[1])), [(R('1.3'), R('0.3')), (R(3), R('1.7')), (R('0.5'), R(-5))]),
T(87, 'call 1: the half deflection\'s v share is X', 'delta direction = doubled (sqrt(1 - X^2), X)', o87, n87, P87),
T(88, 'call 1: the boost\'s slope is v/c', 'v/c = u', lambda u: mp.tanh(mp.atanh(u)), lambda u: u, PU),
T(89, 'call 1: the boost\'s share', 'sqrt(1 - u^2) = sqrt(1 - u^2)',
  lambda u: [S(1-u*u), mp.sech(mp.atanh(u))], lambda u: [S(1-u*u), S(1-u*u)], PU),
T(90, 'conservation in boost slopes', 'sum m/sqrt(1 - u^2) and sum m u/sqrt(1 - u^2) conserved', o90, n90, P90),
T(91, 'hyperbolic Pythagoras in the slope', '1/(1 - u^2) - u^2/(1 - u^2) = 1',
  lambda u: ch_(u)**2 - sh_(u)**2, lambda u: 1/(1-u*u) - u*u/(1-u*u), PU),
T(92, 'squared conservation in slopes', '2 m1 m2 (1 - u1 u2)/sqrt((1-u1^2)(1-u2^2)) both sides', o92, n92, P90),
T(93, 'relative boost in slopes', '(1 - u1 u2)/sqrt((1-u1^2)(1-u2^2)) = (1 - u3 u4)/sqrt((1-u3^2)(1-u4^2))', o93, n93, P90),
T(94, 'Doppler ratio k = sqrt((1+u)/(1-u))', 'v/c = u = (k - 1/k)/(k + 1/k)', o94, n94, P94),
T(95, 'the boost\'s Doppler ratio', 'k = sqrt((1 + w)/(1 - w)) = sqrt((c + u1)/(c - u1)), w = u1/c', o95, n95, P95),
T(96, 'the boost\'s Doppler ratio', 'k = sqrt((1 + w)/(1 - w)) = sqrt((c + u2)/(c - u2)), w = u2/c', o95, n95, P95),
T(97, 'deflection slopes', 'slope_1 = m2 v/(m1 + m2 h), slope_2 = (1 + h)/v', o97, n97, P97),
T(98, 'final speeds by shares', "v1' = v1 sqrt(m1^2 + m2^2 + 2 m1 m2 h)/(m1 + m2), v2' = v1 (2 m1/(m1 + m2)) v/sqrt(2(1 + h))", o98, n98, P98),
T(99, 'components by shares', 'v_x = v1 h, v_y = v1 v',
  lambda p: [p[0]*C(At(p[1])), p[0]*Sn(At(p[1]))], lambda p: [p[0]*h(p[1]), p[0]*v(p[1])], pts2),
N(100, 'Mercator y is the logarithm of a slope (an amount), and x uses the longitude as an amount'),
N(101, 'derivatives with respect to the angle as an amount (y prime per unit latitude)'),
N(102, 'integrals over the angle as a variable of integration'),
N(103, 'inverse Mercator: the angle from the exponential of an amount y/R, longitude as an amount'),
N(104, 'the slope of phi equals sinh(y/R), a hyperbolic function of an amount'),
N(105, 'small increments of angle taken as amounts in an approximation'),
N(106, 'a longitude increment as an amount'),
T(107, 'scale factor as 1/h', 'k = 1/h', lambda s: [mp.sec(At(s)), 1/C(At(s))], lambda s: [1/h(s), 1/h(s)], P3),
T(108, 'short-line distance by the share', 'distance = ruler h / RF',
  lambda p: p[0]*C(At(p[1]))/p[2], lambda p: p[0]*h(p[1])/p[2], [(R(2), R('0.3'), R(1000)), (R(5), R('1.7'), R(50)), (R(1), R(-5), R(7))]),
T(109, 'parallel distance by the share', 'distance = ruler h / RF',
  lambda p: p[0]*C(At(p[1]))/p[2], lambda p: p[0]*h(p[1])/p[2], [(R(2), R('0.3'), R(1000)), (R(5), R('1.7'), R(50)), (R(1), R(-5), R(7))]),
N(110, 'a meridian arc: the difference of latitudes as amounts, from sinh of amounts'),
N(111, 'R = W/(2 pi): a length from a full turn as an amount'),
T(112, 'call 2: the bearing is the direction (0, 1)', 'alpha has shares (h, v) = (0, 1)',
  lambda x: [C(mp.pi/2), Sn(mp.pi/2)], lambda x: [R(0), R(1)], D3),
N(113, 'the rhumb distance multiplies by the latitude difference as an arc amount'),
N(114, 'ellipsoidal Mercator: logarithms and inverse hyperbolic functions of amounts'),
T(115, 'Coriolis parameter by the share', 'f = 2 w v', lambda p: 2*p[0]*Sn(At(p[1])), lambda p: 2*p[0]*v(p[1]), pts2),
T(116, 'rotation vector by shares', 'Omega = w (0, h, v)',
  lambda p: [0, p[0]*C(At(p[1])), p[0]*Sn(At(p[1]))], lambda p: [0, p[0]*h(p[1]), p[0]*v(p[1])], pts2),
T(117, 'Coriolis acceleration by shares', 'a = -2 Omega x v = 2w(vn v - vu h, -ve v, ve h)', o117, n117, P117),
T(118, 'ballistic X by shares', 'A_X = -2w(V_Y h_t v_a + V_Z v_t)', lambda p: o118(p)[0], lambda p: n118(p)[0], P118),
T(119, 'ballistic Y by shares', 'A_Y = 2w(V_X h_t v_a + V_Z h_t h_a)', lambda p: o118(p)[1], lambda p: n118(p)[1], P118),
T(120, 'ballistic Z by shares', 'A_Z = 2w(V_X v_t - V_Y h_t h_a)', lambda p: o118(p)[2], lambda p: n118(p)[2], P118),
]
assert [L['n'] for L in LAWS] == list(range(1, 121))
