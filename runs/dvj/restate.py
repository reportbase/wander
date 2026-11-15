import mpmath as mp; mp.mp.dps = 50
S = mp.sqrt
def R(x): return mp.mpf(x)
def N(n, reason): return dict(n=n, verdict='none', notation=False, reason=reason)
def T(n, reason, restated, orig, new, points): return dict(n=n, verdict='notation', notation=True, reason=reason, restated=restated, orig=orig, new=new, points=points)
P3 = [R('0.3'), R('1.7'), R('5')]
def h(s): return 1/S(1+s*s)
def v(s): return s/S(1+s*s)

# ---------- helpers (the ones 'new' calls are free of every transcendental) ----------
def sh(s): return (h(s), v(s))
def comp(p, q): return (p[0]*q[0] - p[1]*q[1], p[1]*q[0] + p[0]*q[1])      # directions composed
def dif(p, q): return (p[0]*q[0] + p[1]*q[1], p[1]*q[0] - p[0]*q[1])       # p turned back by q
def half(p): return (S((1 + p[0])/2), S((1 - p[0])/2))                     # half of a direction in (0, half turn)
def dot(u, w): return sum(x*y for x, y in zip(u, w))
def cross(u, w): return [u[1]*w[2]-u[2]*w[1], u[2]*w[0]-u[0]*w[2], u[0]*w[1]-u[1]*w[0]]
def nrm(u): return S(dot(u, u))
def unit(u): n = nrm(u); return [x/n for x in u]
QT = (0, 1)                       # quarter turn's shares
EIGHTH = (1/S(2), 1/S(2))         # eighth turn's shares

# planar triangle: C = (0,0), B = (a,0), A = (x,y); sides a = CB, b = CA, c = AB
def TN(p):
    x, y, a = p; b = S(x*x + y*y); c = S((a-x)**2 + y*y)
    return dict(a=a, b=b, c=c, cA=(y*y - x*(a-x))/(b*c), sA=a*y/(b*c), cB=(a-x)/c, sB=y/c, cG=x/b, sG=y/b)
def TA(p):
    x, y, a = p; b = S(x*x + y*y); c = S((a-x)**2 + y*y)
    ga = mp.atan2(y, x); be = mp.atan2(y, a-x); al = mp.atan2(abs(-(a-x)*y - y*x), -(a-x)*x + y*y)
    return dict(a=a, b=b, c=c, al=al, be=be, ga=ga, cA=mp.cos(al), sA=mp.sin(al), cB=mp.cos(be), sB=mp.sin(be),
                cG=mp.cos(ga), sG=mp.sin(ga))
P_T = [(R(1), R(2), R(3)), (R('0.4'), R('1.1'), R(2)), (R('-0.5'), R('1.3'), R('1.7'))]   # a > 2 b cos(gamma)
P_Tb = [(R(2), R(1), R(3)), (R('1.5'), R('0.7'), R(2)), (R(3), R(2), R(4))]               # a < 2 b cos(gamma)

# spherical triangle from three vectors (A, B, C)
def SVEC(P): return [unit([R(x) for x in u]) for u in P]
def sidesh(U, W): return dot(U, W), nrm(cross(U, W))
def angsh(X, U, W):
    tu = [u - dot(X, U)*x for u, x in zip(U, X)]; tw = [w - dot(X, W)*x for w, x in zip(W, X)]
    n = nrm(tu)*nrm(tw); return dot(tu, tw)/n, nrm(cross(tu, tw))/n
def SN(P, V=None):
    A, B, C = V if V else SVEC(P)
    t = {}
    for k, (U, W) in dict(a=(B, C), b=(C, A), c=(A, B)).items(): t['c'+k], t['s'+k] = sidesh(U, W)
    for k, (X, U, W) in dict(A=(A, B, C), B=(B, C, A), C=(C, A, B)).items(): t['c'+k], t['s'+k] = angsh(X, U, W)
    for k in 'abcABC':
        t['h'+k] = half((t['c'+k], t['s'+k])); t['q'+k] = half(t['h'+k])
    return t
def SA(P, V=None):
    A, B, C = V if V else SVEC(P)
    t = {}
    for k, (U, W) in dict(a=(B, C), b=(C, A), c=(A, B)).items():
        c0, s0 = sidesh(U, W); t['x'+k] = mp.atan2(s0, c0)
    for k, (X, U, W) in dict(A=(A, B, C), B=(B, C, A), C=(C, A, B)).items():
        c0, s0 = angsh(X, U, W); t['x'+k] = mp.atan2(s0, c0)
    for k in 'abcABC':
        x = t['x'+k]; t['c'+k], t['s'+k] = mp.cos(x), mp.sin(x)
        t['h'+k] = (mp.cos(x/2), mp.sin(x/2)); t['q'+k] = (mp.cos(x/4), mp.sin(x/4))
    return t
P_S = [((1, '0.2', '0.3'), ('0.3', 1, '0.1'), ('0.2', '0.4', 1)),
       ((1, 0, '0.1'), ('0.5', 1, '0.2'), ('0.1', '0.3', '1.2')),
       (('0.9', '-0.3', '0.4'), ('-0.2', 1, '0.5'), ('0.4', '0.2', 1))]
P_RT = [(('0.8', 0, '0.6'), (0, '0.5', '0.9'), (0, 0, 1)), (('0.3', 0, 1), (0, '0.7', '0.6'), (0, 0, 1)),
        ((1, 0, '0.4'), (0, 1, '0.8'), (0, 0, 1))]                          # right angle at C
P_QD = [((1, 0, 0), (0, 1, 0), ('0.3', '0.4', 1)), ((1, 0, 0), (0, 1, 0), ('0.5', '0.2', 1)),
        ((1, 0, 0), (0, 1, 0), ('0.7', '0.6', '0.5'))]                      # side c a quarter turn

def F(fn, src): return lambda p: fn(src(p))

# ---------- planar triangle laws ----------
def L1(t): a, b, c = t['a'], t['b'], t['c']; return [c*c, a*a+b*b-2*a*b*t['cG'], a*a, b*b+c*c-2*b*c*t['cA'], b*b, a*a+c*c-2*a*c*t['cB']]
def L2(t): a, b = t['a'], t['b']; return [t['c'], S(a*a+b*b-2*a*b*t['cG'])]
def L3(t): b, c = t['b'], t['c']; r = S(c*c - b*b*t['sG']**2); return [t['a'], b*t['cG'] + r, b*t['cG'] - r]
def L4(t): a, b, c = t['a'], t['b'], t['c']; return [a*a - 2*a*b*t['cG'] + b*b - c*c]
def L11(t): return [t['c'], t['a']*t['cB'] + t['b']*t['cA']]
def L12(t): a, b, c = t['a'], t['b'], t['c']; return [c*c, a*c*t['cB'] + b*c*t['cA']]
def L13(t): a, b, c = t['a'], t['b'], t['c']; return [a*a, a*c*t['cB'] + a*b*t['cG'], b*b, b*c*t['cA'] + a*b*t['cG']]
def L14(t):
    a, b, c = t['a'], t['b'], t['c']; A, B, G = t['cA'], t['cB'], t['cG']
    return [c*c - a*a - b*b, a*c*B + b*c*A - a*c*B - b*c*A - 2*a*b*G, c*c, a*a + b*b - 2*a*b*G]
def L18(t): a, b, c = t['a'], t['b'], t['c']; return [a*a + c*(c - 2*a*t['cB']), a*a + c*c - 2*a*c*t['cB'], b*b]
def L19(t): return [t['a'], 2*t['b']*t['cG']]
def L20(t): a, b = t['a'], t['b']; return [a*(a - 2*b*t['cG'])]
def L21(t): a, b, c = t['a'], t['b'], t['c']; return [c*c, b*b + a*(a - 2*b*t['cG'])]
def L22(t): a, b = t['a'], t['b']; return [a*(2*b*t['cG'] - a)]
def L23(t): a, b, c = t['a'], t['b'], t['c']; return [b*b, c*c + a*(2*b*t['cG'] - a)]
def L27(t):
    sA, sB, cA, cB, cG, sG = t['sA'], t['sB'], t['cA'], t['cB'], t['cG'], t['sG']
    return [sG**2, (sA*cB + cA*sB)**2, sA**2*cB**2 + 2*sA*sB*cA*cB + cA**2*sB**2,
            sA**2*cB**2 + 2*sA*sB*(sA*sB - cG) + cA**2*sB**2, sA**2*(cB**2 + sB**2) + sB**2*(cA**2 + sA**2) - 2*sA*sB*cG,
            sA**2 + sB**2 - 2*sA*sB*cG]
def L28(t): return [t['a']/t['sA'], t['b']/t['sB'], t['c']/t['sG']]
def L29(t):
    a, b, c, sA, sB, sG = t['a'], t['b'], t['c'], t['sA'], t['sB'], t['sG']
    return [sG**2*c*c/sG**2, sA**2*a*a/sA**2 + sB**2*b*b/sB**2 - 2*sA*sB*t['cG']*a*b/(sA*sB), c*c, a*a + b*b - 2*a*b*t['cG']]

def o24(p):
    t = TA(p); s = t['al'] + t['be'] + t['ga']; return [mp.cos(s), mp.sin(s), mp.cos(mp.pi), mp.sin(mp.pi)]
def n24(p):
    t = TN(p); d = comp(comp((t['cA'], t['sA']), (t['cB'], t['sB'])), (t['cG'], t['sG'])); return [d[0], d[1], -1, 0]
def o25(p):
    t = TA(p); return [t['sG'], mp.sin(mp.pi - t['ga']), mp.sin(t['al'] + t['be']), t['sA']*t['cB'] + t['cA']*t['sB']]
def n25(p):
    t = TN(p); sup = (-t['cG'], t['sG']); ab = comp((t['cA'], t['sA']), (t['cB'], t['sB']))
    return [t['sG'], sup[1], ab[1], t['sA']*t['cB'] + t['cA']*t['sB']]
def o26(p):
    t = TA(p); return [t['cG'], -mp.cos(mp.pi - t['ga']), -mp.cos(t['al'] + t['be']), t['sA']*t['sB'] - t['cA']*t['cB']]
def n26(p):
    t = TN(p); sup = (-t['cG'], t['sG']); ab = comp((t['cA'], t['sA']), (t['cB'], t['sB']))
    return [t['cG'], -sup[0], -ab[0], t['sA']*t['sB'] - t['cA']*t['cB']]
def o34(p):
    t = TA(p); a, b = t['a'], t['b']
    return [t['c']**2, (a-b)**2 + 4*a*b*mp.sin(t['ga']/2)**2, (a-b)**2 + 4*a*b*(1 - mp.cos(t['ga']))/2]
def n34(p):
    t = TN(p); a, b = t['a'], t['b']; hs = half((t['cG'], t['sG']))
    return [t['c']**2, (a-b)**2 + 4*a*b*hs[1]**2, (a-b)**2 + 4*a*b*(1 - t['cG'])/2]

# ---------- one angle given by its slope ----------
def o3a(p): b, c, s = p; g = mp.atan(s); return [b*mp.sin(g), c, b]
def n3a(p): b, c, s = p; return [b*v(s), c, b]
def o6(p): b, s = p; return [b*mp.sin(mp.atan(s))]
def n6(p): b, s = p; return [b*v(s)]
def o7(p): a, s = p; g = mp.pi - mp.atan(s); return [a*mp.cos(mp.pi - g), -a*mp.cos(g)]
def n7(p): a, s = p; cg = -h(s); return [a*(-cg), -a*cg]
def o8(p): a, b, s = p; g = mp.atan(s); return [S(a*a+b*b-2*a*b*mp.cos(g)), S((b - a*mp.cos(g))**2 + (a*mp.sin(g))**2)]
def n8(p): a, b, s = p; return [S(a*a+b*b-2*a*b*h(s)), S((b - a*h(s))**2 + (a*v(s))**2)]
def o9(p): a, b, s = p; g = mp.pi - mp.atan(s); return [S(a*a+b*b-2*a*b*mp.cos(g)), S((b + a*abs(mp.cos(g)))**2 + (a*mp.sin(g))**2)]
def n9(p): a, b, s = p; cg, sg = -h(s), v(s); return [S(a*a+b*b-2*a*b*cg), S((b + a*abs(cg))**2 + (a*sg)**2)]
def o10(s): g = mp.atan(s); return [mp.cos(mp.pi - g), -mp.cos(g)]
def n10(s): sup = (-h(s), v(s)); return [sup[0], -h(s)]
def o15(p): b, s = p; th = mp.atan(s); return [b*mp.cos(th), b*mp.sin(th), R(0), R(0)]
def n15(p): b, s = p; return [b*h(s), b*v(s), R(0), R(0)]
def o16(p): a, b, s = p; th = mp.atan(s); return [S((a - b*mp.cos(th))**2 + (0 - b*mp.sin(th))**2), S(a*a+b*b-2*a*b*mp.cos(th))]
def n16(p): a, b, s = p; return [S((a - b*h(s))**2 + (0 - b*v(s))**2), S(a*a+b*b-2*a*b*h(s))]
def o17(p): a, c, s = p; B = mp.atan(s); return [a*mp.cos(B), c - 2*a*mp.cos(B)]
def n17(p): a, c, s = p; return [a*h(s), c - 2*a*h(s)]
def o30(p):
    a, b = p; ang = mp.atan2(nrm(cross(a, b)), dot(a, b)); c = [x - y for x, y in zip(a, b)]
    return [dot(c, c), dot(a, a) + dot(b, b) - 2*nrm(a)*nrm(b)*mp.cos(ang)]
def n30(p):
    a, b = p; c = [x - y for x, y in zip(a, b)]; ch = dot(a, b)/(nrm(a)*nrm(b))
    return [dot(c, c), dot(a, a) + dot(b, b) - 2*nrm(a)*nrm(b)*ch]
P_V = [([R(1), R(2), R(3)], [R(-1), R('0.5'), R(2)]), ([R('0.3'), R(1), R(0)], [R(2), R(1), R(1)]), ([R(1), R(0), R(0)], [R(-2), R(3), R(1)])]
def o31(p):
    a, s = p; g = mp.atan(s); c2 = (a*mp.cos(g) - a)**2 + (a*mp.sin(g))**2; return [mp.cos(g), 1 - c2/(2*a*a), c2, 2*a*a*(1 - mp.cos(g))]
def n31(p):
    a, s = p; c2 = (a*h(s) - a)**2 + (a*v(s))**2; return [h(s), 1 - c2/(2*a*a), c2, 2*a*a*(1 - h(s))]

# tetrahedron: face areas and dihedral angles
def tet(P):
    P = [[R(x) for x in u] for u in P]; ns = []
    for i in range(4):
        j, k, l = [m for m in range(4) if m != i]
        n = [x/2 for x in cross([a-b for a, b in zip(P[k], P[j])], [a-b for a, b in zip(P[l], P[j])])]
        if dot(n, [a-b for a, b in zip(P[i], P[j])]) > 0: n = [-x for x in n]
        ns.append(n)
    return ns
def o33(P):
    ns = tet(P); Ar = [nrm(n) for n in ns]
    def cphi(i, j): c = -dot(ns[i], ns[j])/(Ar[i]*Ar[j]); s = nrm(cross(ns[i], ns[j]))/(Ar[i]*Ar[j]); return mp.cos(mp.atan2(s, c))
    A, B, C, D = Ar
    return [A*A, B*B + C*C + D*D - 2*(B*C*cphi(1, 2) + C*D*cphi(2, 3) + D*B*cphi(3, 1))]
def n33(P):
    ns = tet(P); Ar = [nrm(n) for n in ns]
    def cphi(i, j): return -dot(ns[i], ns[j])/(Ar[i]*Ar[j])
    A, B, C, D = Ar
    return [A*A, B*B + C*C + D*D - 2*(B*C*cphi(1, 2) + C*D*cphi(2, 3) + D*B*cphi(3, 1))]
P_TET = [((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)), ((0, 0, 0), (2, '0.3', 0), ('0.5', '1.5', '0.2'), ('0.4', '0.6', '1.3')),
         ((1, 1, 1), (-1, 0, '0.5'), (0, 2, -1), ('0.3', '-1', 0))]

# ---------- spherical laws ----------
def L35(t): return [t['ca'], t['cb']*t['cc'] + t['sb']*t['sc']*t['cA']]
def L36(t): return [t['ca'], (t['cA'] + t['cB']*t['cC'])/(t['sB']*t['sC'])]
def L43(t): return [t['sA']/t['sa'], t['sB']/t['sb'], t['sC']/t['sc']]
def L44(t): return [t['ca'], t['sc']*t['sb']*t['cA'] + t['cc']*t['cb']]
def L45(t): return [t['sA']**2, 1 - t['cA']**2]
def L46(t):
    ca, cb, cc, sb, sc = t['ca'], t['cb'], t['cc'], t['sb'], t['sc']
    return [t['sA']**2, 1 - ((ca - cb*cc)/(sb*sc))**2, ((1 - cb**2)*(1 - cc**2) - (ca - cb*cc)**2)/(sb**2*sc**2)]
def L47(t):
    ca, cb, cc = t['ca'], t['cb'], t['cc']
    return [t['sA']/t['sa'], S(1 - ca**2 - cb**2 - cc**2 + 2*ca*cb*cc)/(t['sa']*t['sb']*t['sc'])]
def ct(t, x, X, y, Y):   # cos(inner side) cos(inner angle) = cot(outer side) sin(inner side) - cot(outer angle) sin(inner angle)
    return [t['c'+x]*t['c'+X], t['c'+y]/t['s'+y]*t['s'+x] - t['c'+Y]/t['s'+Y]*t['s'+X]]
def L49(t): return ct(t, 'b', 'C', 'a', 'A')
def L50(t):
    return (ct(t, 'b', 'C', 'a', 'A') + ct(t, 'b', 'A', 'c', 'C') + ct(t, 'c', 'A', 'b', 'B') + ct(t, 'c', 'B', 'a', 'A')
            + ct(t, 'a', 'B', 'c', 'C') + ct(t, 'a', 'C', 'b', 'B'))
def L51(t):
    ca, cb, cc, sa, sb, sc, cA, sA, cC, sC = [t[k] for k in ('ca', 'cb', 'cc', 'sa', 'sb', 'sc', 'cA', 'sA', 'cC', 'sC')]
    cotA = cA/sA
    return [ca, cb*cc + sb*sc*cA, cb*(ca*cb + sa*sb*cC) + sb*sC*sa*cotA, ca*sb**2, cb*sa*sb*cC + sb*sC*sa*cotA]
def L59(t):
    ca, cb, cc, sa, sb, sc, cA, sA, cB, sB = [t[k] for k in ('ca', 'cb', 'cc', 'sa', 'sb', 'sc', 'cA', 'sA', 'cB', 'sB')]
    ta, tb, tc, tA, tB = sa/ca, sb/cb, sc/cc, sA/cA, sB/cB
    return [cc, ca*cb, sa, sA*sc, sb, sB*sc, ta, tA*sb, tb, tB*sa, tb, cA*tc, ta, cB*tc, cA, sB*ca, cB, sA*cb, cc, (cA/sA)*(cB/sB)]
def L60(t):
    ca, cb, sa, sb, cA, sA, cB, sB, cC, sC = [t[k] for k in ('ca', 'cb', 'sa', 'sb', 'cA', 'sA', 'cB', 'sB', 'cC', 'sC')]
    ta, tb, tA, tB, tC = sa/ca, sb/cb, sA/cA, sB/cB, sC/cC
    return [cC, -cA*cB, sA, sa*sC, sB, sb*sC, tA, ta*sB, tB, tb*sA, tB, -ca*tC, tA, -cb*tC, ca, sb*cA, cb, sa*cB, cC, -(ca/sa)*(cb/sb)]
def L61(t):
    ca, cb, cc, sa, sb, sc, cA, cB = [t[k] for k in ('ca', 'cb', 'cc', 'sa', 'sb', 'sc', 'cA', 'cB')]
    return [ca, (ca*cc + sa*sc*cB)*cc + sb*sc*cA, ca*sc**2, sa*cc*sc*cB + sb*sc*cA]
def L62(t): return [t['ca']*t['sc'], t['sa']*t['cc']*t['cB'] + t['sb']*t['cA']]
def L63(t):
    ca, cb, cc, sb, sc, cA, sA = [t[k] for k in ('ca', 'cb', 'cc', 'sb', 'sc', 'cA', 'sA')]
    return [ca*cA, cb*cc*cA + sb*sc - sb*sc*sA**2]
def L64(t):
    ca, sa, cA, cB, cC, sB, sC = [t[k] for k in ('ca', 'sa', 'cA', 'cB', 'cC', 'sB', 'sC')]
    return [ca*cA, -cB*cC*ca + sB*sC - sB*sC*sa**2]
def L65(t): return [t['sb']*t['sc']*t['sA']**2, t['sB']*t['sC']*t['sa']**2]
def L66(t):
    return [t['sb']*t['sc'] + t['cb']*t['cc']*t['cA'], t['sB']*t['sC'] - t['cB']*t['cC']*t['ca']]
def L71(t): return [t['cC'], t['sC'], R(0), R(1)]
def L72(t):    # E/2 = A/2 + B/2 + C/2 - quarter turn
    e = dif(comp(comp(t['hA'], t['hB']), t['hC']), QT); return [e[1]/e[0], (t['ha'][1]/t['ha'][0])*(t['hb'][1]/t['hb'][0])]
def o72(P):
    t = SA(P); E = t['xA'] + t['xB'] + t['xC'] - mp.pi; return [mp.tan(E/2), mp.tan(t['xa']/2)*mp.tan(t['xb']/2)]

# half-angle laws (spherical)
def sl(p): return p[1]/p[0]
def L52n(t):
    hs = comp(comp(t['ha'], t['hb']), t['hc'])               # s
    smb = dif(comp(t['ha'], t['hc']), t['hb'])               # s - b
    smc = dif(comp(t['ha'], t['hb']), t['hc'])               # s - c
    sma = dif(comp(t['hb'], t['hc']), t['ha'])               # s - a
    den = t['sb']*t['sc']
    return [t['hA'][1], S(smb[1]*smc[1]/den), t['hA'][0], S(hs[1]*sma[1]/den), sl(t['hA']), S(smb[1]*smc[1]/(hs[1]*sma[1]))]
def L52o(P):
    t = SA(P); a, b, c, A = t['xa'], t['xb'], t['xc'], t['xA']; s = (a + b + c)/2; den = mp.sin(b)*mp.sin(c)
    return [mp.sin(A/2), S(mp.sin(s-b)*mp.sin(s-c)/den), mp.cos(A/2), S(mp.sin(s)*mp.sin(s-a)/den), mp.tan(A/2),
            S(mp.sin(s-b)*mp.sin(s-c)/(mp.sin(s)*mp.sin(s-a)))]
def L53n(t):
    Sg = comp(comp(t['hA'], t['hB']), t['hC'])
    SmA = dif(comp(t['hB'], t['hC']), t['hA']); SmB = dif(comp(t['hA'], t['hC']), t['hB']); SmC = dif(comp(t['hA'], t['hB']), t['hC'])
    den = t['sB']*t['sC']
    return [t['ha'][1], S(-Sg[0]*SmA[0]/den), t['ha'][0], S(SmB[0]*SmC[0]/den), sl(t['ha']), S(-Sg[0]*SmA[0]/(SmB[0]*SmC[0]))]
def L53o(P):
    t = SA(P); a, A, B, C = t['xa'], t['xA'], t['xB'], t['xC']; Sg = (A + B + C)/2; den = mp.sin(B)*mp.sin(C)
    return [mp.sin(a/2), S(-mp.cos(Sg)*mp.cos(Sg-A)/den), mp.cos(a/2), S(mp.cos(Sg-B)*mp.cos(Sg-C)/den), mp.tan(a/2),
            S(-mp.cos(Sg)*mp.cos(Sg-A)/(mp.cos(Sg-B)*mp.cos(Sg-C)))]
def L55n(t):
    smb = dif(comp(t['ha'], t['hc']), t['hb']); smc = dif(comp(t['ha'], t['hb']), t['hc'])
    d1 = dif((t['cc'], t['sc']), (t['cb'], t['sb']))      # (s-b) - (s-c) = c - b
    d2 = comp(smb, smc)                                   # (s-b) + (s-c) = a
    cb, cc, sb, sc, cA = t['cb'], t['cc'], t['sb'], t['sc'], t['cA']
    return [2*smb[1]*smc[1], d1[0] - d2[0], d1[0] - t['ca'], cb*cc + sb*sc - (cb*cc + sb*sc*cA), sb*sc*(1 - cA), sb*sc*(2*t['hA'][1]**2)]
def L55o(P):
    t = SA(P); a, b, c, A = t['xa'], t['xb'], t['xc'], t['xA']; s = (a + b + c)/2
    cb, cc, sb, sc, cA = mp.cos(b), mp.cos(c), mp.sin(b), mp.sin(c), mp.cos(A)
    return [2*mp.sin(s-b)*mp.sin(s-c), mp.cos((s-b)-(s-c)) - mp.cos((s-b)+(s-c)), mp.cos(c-b) - mp.cos(a),
            cb*cc + sb*sc - (cb*cc + sb*sc*cA), sb*sc*(1 - cA), sb*sc*(2*mp.sin(A/2)**2)]
def L57n(t):
    pAB = comp(t['hA'], t['hB']); mAB = dif(t['hA'], t['hB']); pab = comp(t['ha'], t['hb']); mab = dif(t['ha'], t['hb'])
    return [pAB[1]/t['hC'][0], mab[0]/t['hc'][0], mAB[1]/t['hC'][0], mab[1]/t['hc'][1],
            pAB[0]/t['hC'][1], pab[0]/t['hc'][0], mAB[0]/t['hC'][1], pab[1]/t['hc'][1]]
def L57o(P):
    t = SA(P); a, b, c, A, B, C = [t['x'+k] for k in 'abcABC']; cs, sn = mp.cos, mp.sin
    return [sn((A+B)/2)/cs(C/2), cs((a-b)/2)/cs(c/2), sn((A-B)/2)/cs(C/2), sn((a-b)/2)/sn(c/2),
            cs((A+B)/2)/sn(C/2), cs((a+b)/2)/cs(c/2), cs((A-B)/2)/sn(C/2), sn((a+b)/2)/sn(c/2)]
def L58n(t):
    return [sl(dif(t['hA'], t['hB']))/sl(comp(t['hA'], t['hB'])), sl(dif(t['ha'], t['hb']))/sl(comp(t['ha'], t['hb']))]
def L58o(P):
    t = SA(P); a, b, A, B = t['xa'], t['xb'], t['xA'], t['xB']
    return [mp.tan((A-B)/2)/mp.tan((A+B)/2), mp.tan((a-b)/2)/mp.tan((a+b)/2)]
def L69n(t):
    e4 = dif(comp(comp(t['qA'], t['qB']), t['qC']), EIGHTH)          # E/4 = A/4 + B/4 + C/4 - eighth turn
    s2 = comp(comp(t['qa'], t['qb']), t['qc'])                       # s/2
    sa2 = dif(comp(t['qb'], t['qc']), t['qa']); sb2 = dif(comp(t['qa'], t['qc']), t['qb']); sc2 = dif(comp(t['qa'], t['qb']), t['qc'])
    return [sl(e4), S(sl(s2)*sl(sa2)*sl(sb2)*sl(sc2))]
def L69o(P):
    t = SA(P); a, b, c, A, B, C = [t['x'+k] for k in 'abcABC']; E = A + B + C - mp.pi; s = (a + b + c)/2; tn = mp.tan
    return [tn(E/4), S(tn(s/2)*tn((s-a)/2)*tn((s-b)/2)*tn((s-c)/2))]
def L70n(t):
    e2 = dif(comp(comp(t['hA'], t['hB']), t['hC']), QT); k = sl(t['ha'])*sl(t['hb'])
    return [sl(e2), k*t['sC']/(1 + k*t['cC'])]
def L70o(P):
    t = SA(P); E = t['xA'] + t['xB'] + t['xC'] - mp.pi; k = mp.tan(t['xa']/2)*mp.tan(t['xb']/2)
    return [mp.tan(E/2), k*mp.sin(t['xC'])/(1 + k*mp.cos(t['xC']))]

# polar triangle
def polarV(P):
    A, B, C = SVEC(P)
    if dot(A, cross(B, C)) < 0: B, C = C, B
    return (A, B, C), (unit(cross(B, C)), unit(cross(C, A)), unit(cross(A, B)))
def o41(P):
    V, W = polarV(P); t, u = SA(None, V), SA(None, W); out = []
    for K, k in zip('ABC', 'abc'):
        out += [u['c'+K], u['s'+K], mp.cos(mp.pi - t['x'+k]), mp.sin(mp.pi - t['x'+k]),
                u['c'+k], u['s'+k], mp.cos(mp.pi - t['x'+K]), mp.sin(mp.pi - t['x'+K])]
    return out
def n41(P):
    V, W = polarV(P); t, u = SN(None, V), SN(None, W); out = []
    for K, k in zip('ABC', 'abc'):
        out += [u['c'+K], u['s'+K], -t['c'+k], t['s'+k], u['c'+k], u['s'+k], -t['c'+K], t['s'+K]]
    return out

# latitude / longitude quadrilateral
def quad73(p, mode):
    s1, s2, sl_ = p
    if mode == 'o':
        f1, f2, dl = mp.atan(s1), mp.atan(s2), mp.atan(sl_); c1, n1, c2, n2, cl, nl = mp.cos(f1), mp.sin(f1), mp.cos(f2), mp.sin(f2), mp.cos(dl), mp.sin(dl)
    else:
        c1, n1, c2, n2, cl, nl = h(s1), v(s1), h(s2), v(s2), h(sl_), v(sl_)
    P1 = [c1, 0, n1]; P2 = [c2*cl, c2*nl, n2]; Q1 = [1, 0, 0]; Q2 = [cl, nl, 0]
    return angsh(P1, Q1, P2), angsh(P2, P1, Q2)
def o73(p):
    a1, a2 = quad73(p, 'o'); E = mp.atan2(a1[1], a1[0]) + mp.atan2(a2[1], a2[0]) - mp.pi
    f1, f2, dl = mp.atan(p[0]), mp.atan(p[1]), mp.atan(p[2])
    return [mp.tan(E/2), mp.sin((f2 + f1)/2)/mp.cos((f2 - f1)/2)*mp.tan(dl/2)]
def n73(p):
    a1, a2 = quad73(p, 'n'); e2 = dif(comp(half(a1), half(a2)), QT)
    hf1, hf2, hl = half(sh(p[0])), half(sh(p[1])), half(sh(p[2]))
    return [sl(e2), comp(hf2, hf1)[1]/dif(hf2, hf1)[0]*sl(hl)]
P_73 = [(R('0.3'), R('0.9'), R('0.5')), (R('0.1'), R('1.4'), R('1.1')), (R('0.7'), R('2'), R('0.25'))]

# ---------- coordinates ----------
def o75(p):
    x, y = p; rho = S(x*x + y*y)
    if x >= 0: f = mp.asin(y/rho)
    elif y >= 0: f = -mp.asin(y/rho) + mp.pi
    else: f = -mp.asin(y/rho) - mp.pi
    return [rho, mp.cos(f), mp.sin(f)]
def n75(p): x, y = p; rho = S(x*x + y*y); return [rho, x/rho, y/rho]
def o77(p):
    x, y = p; rho = S(x*x + y*y)
    if x == 0: f = mp.pi/2*(y/abs(y))
    elif x > 0: f = mp.atan(y/x)
    elif y >= 0: f = mp.atan(y/x) + mp.pi
    else: f = mp.atan(y/x) - mp.pi
    return [mp.cos(f), mp.sin(f)]
def n77(p): x, y = p; rho = S(x*x + y*y); return [x/rho, y/rho]
P_XY = [(R(1), R(2)), (R(-1), R(2)), (R(-1), R(-2)), (R(0), R(3)), (R(0), R(-3)), (R('0.4'), R('-1.3'))]
def o76(u): f = mp.asin(u); return [mp.cos(f), mp.sin(f)]
def n76(u): return [S(1 - u*u), u]
def o78(p): f = mp.atan2(p[1], p[0]); return [mp.cos(f), mp.sin(f)]

# ---------- Euler's formula ----------
def z_o(s): x = mp.atan(s); return mp.mpc(mp.cos(x), mp.sin(x))
def z_n(s): return mp.mpc(h(s), v(s))
P_Z = [R('0.3'), R('-1.7'), R('5')]
def o74(p):
    s, u = p; u = unit(u); th = mp.atan(s); x, y, z = [c*th/2 for c in u]
    L = mp.matrix([[0, -x, -y, -z], [x, 0, -z, y], [y, z, 0, -x], [z, -y, x, 0]]); E = mp.expm(L)
    return [E[0, 0], E[1, 0], E[2, 0], E[3, 0]]
def n74(p):
    s, u = p; u = unit(u); hh = half(sh(s)); return [hh[0]] + [c*hh[1] for c in u]
P_Q = [(R('0.3'), [R(1), R(2), R(2)]), (R('1.7'), [R(0), R(0), R(1)]), (R('5'), [R(-1), R('0.5'), R(3)])]
def o99(x):
    th = mp.atan(x); E = mp.expm(th*mp.matrix([[0, -1], [1, 0]]))
    return [E[0, 0], E[0, 1], E[1, 0], E[1, 1], mp.cos(th), -mp.sin(th), mp.sin(th), mp.cos(th)]
def n99(s): return [h(s), -v(s), v(s), h(s), h(s), -v(s), v(s), h(s)]

# ---------- conics ----------
def o100(p): l, ec, s = p; return [l/(1 + ec*mp.cos(mp.atan(s)))]
def n100(p): l, ec, s = p; return [l/(1 + ec*h(s))]
def o101(p): l, ec, s = p; return [l/(1 - ec*mp.cos(mp.atan(s)))]
def n101(p): l, ec, s = p; return [l/(1 - ec*h(s))]
P_CON = [(R(1), R('0.3'), R('0.4')), (R(2), R('0.7'), R('-1.5')), (R('0.5'), R('0.95'), R(3))]
def o102(p): pp, s = p; f = mp.atan(s); return [2*pp*mp.cos(f)/mp.sin(f)**2, R(1) if (mp.cos(f) >= 0 and mp.sin(f) != 0) else R(0)]
def n102(p): pp, s = p; return [2*pp*h(s)/v(s)**2, R(1) if (h(s) >= 0 and v(s) != 0) else R(0)]
def o103(p): r, s = p; f = mp.atan(s); x, y = r*mp.cos(f), r*mp.sin(f); return [r*r, x*x + y*y, x]
def n103(p): r, s = p; x, y = r*h(s), r*v(s); return [r*r, x*x + y*y, x]
def o104(p): pp, s = p; f = mp.atan(s); return [pp/(1 - mp.cos(f))]
def n104(p): pp, s = p; return [pp/(1 - h(s))]
def o105(p): r, y, s, x = p; return [4*r*y*mp.cos(mp.atan(s)), x*x]
def n105(p): r, y, s, x = p; return [4*r*y*h(s), x*x]
def o108(p): x, s = p; a = mp.atan(s); return [4*x**3 - 3*x - mp.cos(3*a)]
def n108(p): x, s = p; c, d = h(s), v(s); return [4*x**3 - 3*x - (c**3 - 3*c*d*d)]
def o109(s): a = mp.atan(s); return [mp.cos(3*a), 4*mp.cos(a)**3 - 3*mp.cos(a)]
def n109(s): c, d = h(s), v(s); return [c**3 - 3*c*d*d, 4*c**3 - 3*c]

# ---------- orbit ----------
def orb_o(p):
    ec, s = p; nu = mp.atan(s); psi = mp.atan2(ec + mp.cos(nu), -mp.sin(nu)); return ec, nu, psi
def orb_n(p):
    ec, s = p; vel = (-v(s), ec + h(s)); n = S(vel[0]**2 + vel[1]**2); return ec, sh(s), (vel[0]/n, vel[1]/n)
def o111(p):
    ec, nu, psi = orb_o(p); phi = nu + mp.pi/2 - psi; ref = mp.atan(ec*mp.sin(nu)/(1 + ec*mp.cos(nu)))
    return [mp.cos(phi), mp.sin(phi), mp.cos(ref), mp.sin(ref)]
def n111(p):
    ec, nu, psi = orb_n(p); phi = dif(comp(nu, QT), psi); ref = sh(ec*nu[1]/(1 + ec*nu[0]))
    return [phi[0], phi[1], ref[0], ref[1]]
def o112(p):
    ec, nu, psi = orb_o(p); phi = nu + mp.pi/2 - psi; cn, sn = mp.cos(nu), mp.sin(nu)
    return [mp.cos(phi), mp.sin(psi - nu), mp.sin(psi)*cn - mp.cos(psi)*sn, (1 + ec*cn)/S(1 + ec**2 + 2*ec*cn)]
def n112(p):
    ec, nu, psi = orb_n(p); phi = dif(comp(nu, QT), psi); d = dif(psi, nu); cn, sn = nu
    return [phi[0], d[1], psi[1]*cn - psi[0]*sn, (1 + ec*cn)/S(1 + ec**2 + 2*ec*cn)]
def o113(p):
    ec, nu, psi = orb_o(p); phi = nu + mp.pi/2 - psi; return [mp.tan(phi), ec*mp.sin(nu)/(1 + ec*mp.cos(nu))]
def n113(p):
    ec, nu, psi = orb_n(p); phi = dif(comp(nu, QT), psi); return [phi[1]/phi[0], ec*nu[1]/(1 + ec*nu[0])]
P_ORB = [(R('0.3'), R('0.4')), (R('0.7'), R('-1.5')), (R('0.95'), R(3))]

# ---------- Mohr's circle ----------
def mtrig(s, mode):
    if mode == 'o':
        th = mp.atan(s); return mp.cos(th), mp.sin(th), mp.cos(2*th), mp.sin(2*th)
    c, d = h(s), v(s); dd = comp((c, d), (c, d)); return c, d, dd[0], dd[1]
def M114(p, m): sx, sy, tau, s = p; c, d, c2, s2 = mtrig(s, m); return [(sx + sy)/2 + (sx - sy)/2*c2 + tau*s2]
def M115(p, m): sx, sy, tau, s = p; c, d, c2, s2 = mtrig(s, m); return [-(sx - sy)/2*s2 + tau*c2]
def M116(p, m):
    sx, sy, tau, s = p; c, d, c2, s2 = mtrig(s, m); sn = sx*c*c + sy*d*d + 2*tau*d*c
    return [sn, sn - sx*c*c - sy*d*d - tau*c*d - tau*d*c, (sx + sy)/2 + (sx - sy)/2*c2 + tau*s2]
def M117(p, m): c, d, c2, s2 = mtrig(p, m); return [c*c, (1 + c2)/2, d*d, (1 - c2)/2, s2, 2*d*c]
def M118(p, m):
    sx, sy, tau, s = p; c, d, c2, s2 = mtrig(s, m)
    A = mp.matrix([[c, d], [-d, c]]); Sg = mp.matrix([[sx, tau], [tau, sy]]); out = A*Sg*A.T
    return [out[0, 0], out[0, 1], out[1, 0], out[1, 1]]
P_M = [(R(50), R(-10), R(40), R('0.3')), (R(3), R(7), R(-2), R('-1.7')), (R('1.5'), R('0.2'), R('0.9'), R(5))]
def o119(p): sx, sy, tau = p; ex = 2*tau/(sy - sx); thp = mp.atan(ex)/2; return [mp.tan(2*thp), ex, mp.tan(thp)]
def n119(p): sx, sy, tau = p; ex = 2*tau/(sy - sx); t = ex/(1 + S(1 + ex*ex)); return [2*t/(1 - t*t), ex, t]
def o120(_):
    a = mp.atan(R(2*40)/(-10 - 50)); return [mp.tan(a), mp.tan(-mp.atan(R(4)/3)), R(2*40)/(-10 - 50)]
def n120(_): return [R(-4)/3, R(-4)/3, R(2*40)/(-10 - 50)]

# ---------- texts ----------
TRI = 'the angles as directions with shares (h_X, v_X) of their slopes; '
LAWS = [
 T(1, 'angles of a triangle are directions', TRI + 'c^2 = a^2 + b^2 - 2ab h_G, a^2 = b^2 + c^2 - 2bc h_A, b^2 = a^2 + c^2 - 2ac h_B',
   F(L1, TA), F(L1, TN), P_T),
 T(2, 'angle a direction', TRI + 'c = sqrt(a^2 + b^2 - 2ab h_G)', F(L2, TA), F(L2, TN), P_T),
 T(3, 'angle a direction', TRI + 'a = b h_G +- sqrt(c^2 - b^2 v_G^2)', F(L3, TA), F(L3, TN), P_T),
 T(4, 'angle a direction', TRI + 'a^2 - 2ab h_G + b^2 - c^2 = 0', F(L4, TA), F(L4, TN), P_T),
 T(5, 'angle a direction', 'b v_G < c < b', o3a, n3a, [(R(2), R('1.5'), R('0.5')), (R(3), R(2), R(1)), (R(1), R('0.9'), R('0.2'))]),
 T(6, 'angle a direction', 'c = b v_G', o6, n6, [(R(2), R('0.5')), (R(3), R(1)), (R(1), R(4))]),
 T(7, 'supplement a mirrored direction', 'CH = a(-h_G) = -a h_G, the supplement having shares (-h_G, v_G)', o7, n7,
   [(R(2), R('0.5')), (R(3), R(1)), (R(1), R(4))]),
 T(8, 'angle a direction', 'c = sqrt((b - a h_G)^2 + (a v_G)^2)', o8, n8, [(R(2), R(3), R('0.5')), (R(1), R(1), R(2)), (R(4), R(1), R('0.1'))]),
 T(9, 'obtuse angle a direction with shares (-h, v)', 'with the direction of G having shares (-h, v): c = sqrt((b + a h)^2 + (a v)^2)', o9, n9,
   [(R(2), R(3), R('0.5')), (R(1), R(1), R(2)), (R(4), R(1), R('0.1'))]),
 T(10, 'supplement a mirrored direction', 'the supplement of a direction (h, v) has shares (-h, v); its first share is -h', o10, n10, P3),
 T(11, 'angles directions', TRI + 'c = a h_B + b h_A', F(L11, TA), F(L11, TN), P_T),
 T(12, 'angles directions', TRI + 'c^2 = ac h_B + bc h_A', F(L12, TA), F(L12, TN), P_T),
 T(13, 'angles directions', TRI + 'a^2 = ac h_B + ab h_G, b^2 = bc h_A + ab h_G', F(L13, TA), F(L13, TN), P_T),
 T(14, 'angles directions', TRI + 'c^2 - a^2 - b^2 = ac h_B + bc h_A - ac h_B - bc h_A - 2ab h_G, so c^2 = a^2 + b^2 - 2ab h_G',
   F(L14, TA), F(L14, TN), P_T),
 T(15, 'angle a direction', 'A = (b h, b v), B = (a, 0), C = (0, 0)', o15, n15, [(R(2), R('0.5')), (R(3), R(-1)), (R(1), R(4))]),
 T(16, 'angle a direction', 'c = sqrt((a - b h)^2 + (0 - b v)^2)', o16, n16, [(R(2), R(3), R('0.5')), (R(1), R(1), R(2)), (R(4), R(1), R('0.1'))]),
 T(17, 'angle a direction', 'BF = AE = a h_B, DC = c - 2a h_B', o17, n17, [(R(1), R(5), R('0.5')), (R(2), R(7), R(1)), (R('0.5'), R(3), R(3))]),
 T(18, 'angle a direction', TRI + 'a^2 + c(c - 2a h_B) = b^2, a^2 + c^2 - 2ac h_B = b^2', F(L18, TA), F(L18, TN), P_T),
 T(19, 'angle a direction', 'a > 2b h_G', F(L19, TA), F(L19, TN), P_T),
 T(20, 'angle a direction', 'h^2 (a length) = a(a - 2b h_G)', F(L20, TA), F(L20, TN), P_T),
 T(21, 'angle a direction', 'c^2 = b^2 + a(a - 2b h_G)', F(L21, TA), F(L21, TN), P_T),
 T(22, 'angle a direction', 'h^2 (a length) = a(2b h_G - a)', F(L22, TA), F(L22, TN), P_Tb),
 T(23, 'angle a direction', 'b^2 = c^2 + a(2b h_G - a)', F(L23, TA), F(L23, TN), P_Tb),
 T(24, 'a value of the composed directions (settled call 2)', 'the three directions composed, (h_A, v_A)(h_B, v_B)(h_G, v_G), have shares (-1, 0)',
   o24, n24, P_T),
 T(25, 'angles directions, composed', 'v_G = (second share of the supplement (-h_G, v_G)) = (second share of A composed with B) = v_A h_B + h_A v_B',
   o25, n25, P_T),
 T(26, 'angles directions, composed', 'h_G = -(first share of the supplement) = -(first share of A composed with B) = v_A v_B - h_A h_B',
   o26, n26, P_T),
 T(27, 'angles directions', 'v_G^2 = (v_A h_B + h_A v_B)^2 = ... = v_A^2 + v_B^2 - 2 v_A v_B h_G', F(L27, TA), F(L27, TN), P_T),
 T(28, 'angles directions', 'a/v_A = b/v_B = c/v_G = k', F(L28, TA), F(L28, TN), P_T),
 T(29, 'angles directions', 'v_G^2 c^2/v_G^2 = v_A^2 a^2/v_A^2 + v_B^2 b^2/v_B^2 - 2 v_A v_B h_G ab/(v_A v_B), so c^2 = a^2 + b^2 - 2ab h_G',
   F(L29, TA), F(L29, TN), P_T),
 T(30, 'the angle between vectors a direction', '|c|^2 = |a|^2 + |b|^2 - 2|a||b| h, h = a.b/(|a||b|) the first share of the direction between them',
   o30, n30, P_V),
 T(31, 'angle a direction', 'h_G = 1 - c^2/(2a^2)', o31, n31, [(R(2), R('0.5')), (R(3), R(1)), (R(1), R(4))]),
 T(32, 'angle a direction', 'c^2 = 2a^2(1 - h_G)', o31, n31, [(R(2), R('0.5')), (R(3), R(1)), (R(1), R(4))]),
 T(33, 'dihedral angles directions', 'A^2 = B^2 + C^2 + D^2 - 2(BC h_bc + CD h_cd + DB h_db), h the first share of each dihedral direction',
   o33, n33, P_TET),
 T(34, 'half of a direction by a square root', 'c^2 = (a - b)^2 + 4ab (1 - h_G)/2, the half-direction having second share sqrt((1 - h_G)/2)',
   o34, n34, P_T),
 T(35, 'sides and angles directions', 'h_a = h_b h_c + v_b v_c h_A', F(L35, SA), F(L35, SN), P_S),
 T(36, 'sides and angles directions', 'h_a = (h_A + h_B h_C)/(v_B v_C)', F(L36, SA), F(L36, SN), P_S),
 N(37, 'cosh and sinh of the sides, lengths in the hyperbolic plane: exponentials of amounts'),
 N(38, 'cosh of a side, a length: an exponential of an amount'),
 N(39, 'the sum of the sides bounded by a whole turn as an amount; a direction drops the turns (settled call 3)'),
 N(40, 'the angle sum bounded between a half turn and three half turns as amounts (settled call 3)'),
 T(41, 'a value of a direction relation (settled call 2): the supplement',
   "the polar triangle's angle A' has shares (-h_a, v_a), its side a' shares (-h_A, v_A), and likewise for B, C", o41, n41, P_S),
 N(42, 'an approximation (settled call 4)'),
 T(43, 'sides and angles directions', 'v_A/v_a = v_B/v_b = v_C/v_c', F(L43, SA), F(L43, SN), P_S),
 T(44, 'sides and angles directions', 'OB.OC = h_a = v_c v_b h_A + h_c h_b', F(L44, SA), F(L44, SN), P_S),
 T(45, 'angle a direction', 'v_A^2 = 1 - h_A^2', F(L45, SA), F(L45, SN), P_S),
 T(46, 'sides and angles directions', 'v_A^2 = 1 - ((h_a - h_b h_c)/(v_b v_c))^2 = ((1 - h_b^2)(1 - h_c^2) - (h_a - h_b h_c)^2)/(v_b^2 v_c^2)',
   F(L46, SA), F(L46, SN), P_S),
 T(47, 'sides and angles directions', 'v_A/v_a = sqrt(1 - h_a^2 - h_b^2 - h_c^2 + 2 h_a h_b h_c)/(v_a v_b v_c)', F(L47, SA), F(L47, SN), P_S),
 N(48, 'differential variations: increments of angles as amounts, a first-order relation (settled call 4)'),
 T(49, 'sides and angles directions', 'h_(inner side) h_(inner angle) = (h/v)_(outer side) v_(inner side) - (h/v)_(outer angle) v_(inner angle)',
   F(L49, SA), F(L49, SN), P_S),
 T(50, 'sides and angles directions', 'h_b h_C = (h_a/v_a) v_b - (h_A/v_A) v_C, and the five others alike', F(L50, SA), F(L50, SN), P_S),
 T(51, 'sides and angles directions', 'h_a = h_b h_c + v_b v_c h_A = h_b(h_a h_b + v_a v_b h_C) + v_b v_C v_a (h_A/v_A); h_a v_b^2 = h_b v_a v_b h_C + v_b v_C v_a (h_A/v_A)',
   F(L51, SA), F(L51, SN), P_S),
 T(52, 'half-sums of sides as directions composed from half-directions', 'with s, s - a, s - b, s - c the half-directions of a, b, c composed: '
   'second share of half A = sqrt(v_(s-b) v_(s-c)/(v_b v_c)), first share = sqrt(v_s v_(s-a)/(v_b v_c)), slope = sqrt(v_(s-b) v_(s-c)/(v_s v_(s-a)))',
   L52o, F(L52n, SN), P_S),
 T(53, 'half-sums of angles as directions composed from half-directions', 'with S, S - A, S - B, S - C composed from the half-directions of A, B, C: '
   'second share of half a = sqrt(-h_S h_(S-A)/(v_B v_C)), first share = sqrt(h_(S-B) h_(S-C)/(v_B v_C)), slope = sqrt(-h_S h_(S-A)/(h_(S-B) h_(S-C)))',
   L53o, F(L53n, SN), P_S),
 T(54, 'half of a direction by a square root', '2 (second share of half A)^2 = 1 - h_A', F(lambda t: [2*t['hA'][1]**2, 1 - t['cA']], SA),
   F(lambda t: [2*t['hA'][1]**2, 1 - t['cA']], SN), P_S),
 T(55, 'half-sums as composed directions', '2 v_(s-b) v_(s-c) = h_(c-b) - h_a = h_b h_c + v_b v_c - (h_b h_c + v_b v_c h_A) = v_b v_c (1 - h_A) = v_b v_c (2 (second share of half A)^2)',
   L55o, F(L55n, SN), P_S),
 T(56, 'half of a direction by a square root', '2 (first share of half A)^2 = 1 + h_A', F(lambda t: [2*t['hA'][0]**2, 1 + t['cA']], SA),
   F(lambda t: [2*t['hA'][0]**2, 1 + t['cA']], SN), P_S),
 T(57, 'half-sums as composed directions', 'each half-sum and half-difference the half-directions composed; the four ratios of their shares equal as stated',
   L57o, F(L57n, SN), P_S),
 T(58, 'half-sums as composed directions', 'slope of (half A minus half B)/slope of (half A plus half B) = slope of (half a minus half b)/slope of (half a plus half b)',
   L58o, F(L58n, SN), P_S),
 T(59, 'sides and angles directions', 'h_c = h_a h_b; v_a = v_A v_c; v_b = v_B v_c; s_a = s_A v_b; s_b = s_B v_a; s_b = h_A s_c; s_a = h_B s_c; h_A = v_B h_a; h_B = v_A h_b; h_c = (1/s_A)(1/s_B)',
   F(L59, SA), F(L59, SN), P_RT),
 T(60, 'sides and angles directions', 'h_C = -h_A h_B; v_A = v_a v_C; v_B = v_b v_C; s_A = s_a v_B; s_B = s_b v_A; s_B = -h_a s_C; s_A = -h_b s_C; h_a = v_b h_A; h_b = v_a h_B; h_C = -(1/s_a)(1/s_b)',
   F(L60, SA), F(L60, SN), P_QD),
 T(61, 'sides and angles directions', 'h_a = (h_a h_c + v_a v_c h_B) h_c + v_b v_c h_A; h_a v_c^2 = v_a h_c v_c h_B + v_b v_c h_A', F(L61, SA), F(L61, SN), P_S),
 T(62, 'sides and angles directions', 'h_a v_c = v_a h_c h_B + v_b h_A', F(L62, SA), F(L62, SN), P_S),
 T(63, 'sides and angles directions', 'h_a h_A = h_b h_c h_A + v_b v_c - v_b v_c v_A^2', F(L63, SA), F(L63, SN), P_S),
 T(64, 'sides and angles directions', 'h_a h_A = -h_B h_C h_a + v_B v_C - v_B v_C v_a^2', F(L64, SA), F(L64, SN), P_S),
 T(65, 'sides and angles directions', 'v_b v_c v_A^2 = v_B v_C v_a^2', F(L65, SA), F(L65, SN), P_S),
 T(66, 'sides and angles directions', 'v_b v_c + h_b h_c h_A = v_B v_C - h_B h_C h_a', F(L66, SA), F(L66, SN), P_S),
 N(67, 'the area is an amount, the angle sum less (N - 2) half turns counted as an amount (settled call 3)'),
 N(68, 'areas as amounts and a half turn added as an amount (settled call 3)'),
 T(69, 'the quarter excess a direction composed from quarter-directions less an eighth turn',
   'slope of (quarter A + quarter B + quarter C less the eighth turn (1/sqrt2, 1/sqrt2)) = sqrt(slope(s/2) slope((s-a)/2) slope((s-b)/2) slope((s-c)/2)), each a composition of quarter-directions of the sides',
   L69o, F(L69n, SN), P_S),
 T(70, 'the half excess a direction composed from half-directions less a quarter turn',
   'slope of (half A + half B + half C less the quarter turn) = k v_C/(1 + k h_C), k = slope(half a) slope(half b)', L70o, F(L70n, SN), P_S),
 T(71, 'a value of a direction (settled call 2)', 'the right angle C has shares (0, 1): h_C = 0, v_C = 1', F(L71, SA), F(L71, SN), P_RT),
 T(72, 'the half excess a composed direction', 'slope of (half A + half B + half C less the quarter turn) = slope(half a) slope(half b)', o72, F(L72, SN), P_RT),
 T(73, 'the half excess and the half-sums as composed directions',
   'slope of (half of the angle at P1 + half of the angle at P2 less the quarter turn) = (second share of (half f2 + half f1))/(first share of (half f2 - half f1)) times slope(half of the longitude difference)',
   o73, n73, P_73),
 T(74, 'the rotation angle a direction; its half by a square root', 'q = (sqrt((1 + h)/2), u sqrt((1 - h)/2)), u the unit axis, h the first share of the rotation',
   o74, n74, P_Q),
 T(75, 'an angle given by an inverse function (settled call 1)', 'rho = sqrt(x^2 + y^2); the direction of phi has shares (x/rho, y/rho), none if x = y = 0', o75, n75, P_XY[:3] + P_XY[5:]),
 T(76, 'a range of directions (settled call 3)', 'the directions with first share h >= 0: shares (sqrt(1 - u^2), u) for u = y/rho', o76, n76,
   [R('-0.9'), R('0.2'), R('0.7')]),
 T(77, 'an angle given by an inverse function (settled call 1)', 'the direction of phi has shares (x/rho, y/rho), none if x = y = 0', o77, n77, P_XY),
 T(78, 'a range of directions (settled call 3)', 'every direction but the opposite one (-1, 0): shares (x/rho, y/rho)', o78, n77, P_XY),
 T(79, 'the angle a direction', 'the point at the direction (h, v) is h + iv: h + iv = h + iv', lambda s: [mp.expj(mp.atan(s)), z_o(s)],
   lambda s: [z_n(s), z_n(s)], P_Z),
 T(80, 'a value of a direction (settled call 2)', 'the opposite direction has shares (-1, 0): the point -1 + 0i = -1, and adding 1 gives 0',
   lambda _: [mp.exp(1j*mp.pi), -1, mp.exp(1j*mp.pi) + 1], lambda _: [mp.mpc(-1, 0), -1, mp.mpc(-1, 0) + 1], P3),
 N(81, 'CE times the angle is an arc length, an angle carried as an amount'),
 T(82, 'an angle given by an inverse function, the logarithm on the unit circle (settled call 1)',
   'the direction given by the point h + iv has shares (h, v), its slope v/h', lambda s: (lambda L, x: [mp.cos(mp.re(L)), mp.sin(mp.re(L)), mp.im(L), mp.cos(x), mp.sin(x)])(
       mp.log(mp.cos(mp.atan(s)) + 1j*mp.sin(mp.atan(s)))/1j, mp.atan(s)), lambda s: [h(s), v(s), 0, h(s), v(s)], P_Z),
 N(83, 'a power series of an amount z'),
 N(84, 'a limit of powers of an amount'),
 T(85, 'the angle a direction', 'f = (h + iv)/(h + iv) = (h - iv)(h + iv)', lambda s: [z_o(s)/mp.expj(mp.atan(s)), mp.expj(-mp.atan(s))*z_o(s)],
   lambda s: [z_n(s)/z_n(s), mp.conj(z_n(s))*z_n(s)], P_Z),
 N(86, 'a derivative with respect to the angle as an amount'),
 N(87, 'a power series in the angle as an amount'),
 T(88, 'angles directions', 'h_x + i v_x = r(h_t + i v_t)', lambda p: [mp.expj(mp.atan(p[0])), p[1]*z_o(p[2])], lambda p: [z_n(p[0]), p[1]*z_n(p[2])],
   [(R('0.3'), R(1), R('0.3')), (R('1.7'), R(2), R('-0.5')), (R(5), R('0.5'), R(4))]),
 N(89, 'a derivative with respect to x as an amount'),
 T(90, 'the angle C a direction, 0 the home direction (settled call 2)', '1 = r (h_C + i v_C)(1 + 0i) = r (h_C + i v_C)',
   lambda p: [1, p[0]*mp.expj(mp.atan(p[1]))*(mp.cos(0) + 1j*mp.sin(0)), p[0]*mp.expj(mp.atan(p[1]))*(1 + 0j), p[0]*mp.expj(mp.atan(p[1]))],
   lambda p: [1, p[0]*z_n(p[1])*mp.mpc(1, 0), p[0]*z_n(p[1])*mp.mpc(1, 0), p[0]*z_n(p[1])], [(R(1), R(0)), (R(2), R('0.5')), (R('0.5'), R(-3))]),
 T(91, 'an angle given by an inverse function (settled call 1)', 'the slope of phi is y/x: its shares (x, y)/sqrt(x^2 + y^2)',
   lambda p: [mp.cos(mp.atan(p[1]/p[0])), mp.sin(mp.atan(p[1]/p[0]))], lambda p: [p[0]/S(p[0]**2 + p[1]**2), p[1]/S(p[0]**2 + p[1]**2)],
   [(R(1), R(2)), (R(3), R(-1)), (R('0.2'), R(5))]),
 T(92, 'the slope of a direction', 'the slope of phi = y/x', lambda p: [mp.tan(mp.atan2(p[1], p[0])), p[1]/p[0]], lambda p: [p[1]/p[0], p[1]/p[0]],
   [(R(1), R(2)), (R(-3), R(-1)), (R('0.2'), R(5))]),
 N(93, 'the exponential of the logarithm of an amount'),
 N(94, 'the exponential of ln|z|, an amount'),
 N(95, 'the logarithm of |z|, an amount'),
 T(96, 'the angle a direction', 'h = Re(h + iv) = ((h + iv) + (h - iv))/2', lambda s: [mp.cos(mp.atan(s)), mp.re(mp.expj(mp.atan(s))), (mp.expj(mp.atan(s)) + mp.expj(-mp.atan(s)))/2],
   lambda s: [h(s), mp.re(z_n(s)), (z_n(s) + mp.conj(z_n(s)))/2], P_Z),
 T(97, 'the angle a direction, its negative the mirrored direction', 'the mirrored direction (h, -v): h - iv = h + i(-v) = h - iv',
   lambda s: [mp.expj(-mp.atan(s)), mp.cos(-mp.atan(s)) + 1j*mp.sin(-mp.atan(s)), mp.cos(mp.atan(s)) - 1j*mp.sin(mp.atan(s))],
   lambda s: [mp.conj(z_n(s)), mp.mpc(h(s), -v(s)), mp.mpc(h(s), 0) - 1j*v(s)], P_Z),
 N(98, 'a whole turn stated as an amount (settled call 3)'),
 T(99, 'the angle a direction', 'for r with r^2 = -1, the element at the direction (h, v) is h + r v', o99, n99, P_Z),
 T(100, 'the angle a direction; e here is the eccentricity, a variable', 'r = l/(1 + ecc h)', o100, n100, P_CON),
 T(101, 'the angle a direction; e the eccentricity', 'r = l/(1 - ecc h)', o101, n101, P_CON),
 T(102, 'the angle a direction, its range a set of directions (settled call 3)', 'r = 2p h/v^2, for the directions with h >= 0 and v nonzero',
   o102, n102, [(R(1), R('0.3')), (R(2), R(-2)), (R('0.5'), R(7))]),
 T(103, 'the angle a direction', 'r^2 = x^2 + y^2, x = r h', o103, n103, [(R(1), R('0.3')), (R(2), R(-2)), (R('0.5'), R(7))]),
 T(104, 'the angle a direction; the excluded set is one direction, home (settled call 3)', 'r = p/(1 - h), for every direction but (1, 0)',
   o104, n104, [(R(1), R('0.3')), (R(2), R(-2)), (R('0.5'), R(7))]),
 T(105, 'the angle a direction', '4ry h = x^2', o105, n105, [(R(1), R(2), R('0.3'), R(3)), (R(2), R('0.5'), R(-2), R(1)), (R('0.5'), R(4), R(7), R(2))]),
 N(106, 'the logarithm of a ratio of lengths, amounts'),
 N(107, 'the logarithm of a ratio of lengths, amounts'),
 T(108, 'three times a direction composed', '4x^3 - 3x - (h^3 - 3h v^2) = 0', o108, n108, [(R('0.3'), R('0.4')), (R(2), R(-2)), (R('-0.7'), R(3))]),
 T(109, 'three times a direction composed', 'h^3 - 3h v^2 = 4h^3 - 3h', o109, n109, P_Z),
 N(110, 'the period carries a whole turn as an amount'),
 T(111, 'directions composed with a quarter turn (settled call 2)', 'the direction of phi is nu composed with the quarter turn (0, 1) and turned back by psi',
   o111, n111, P_ORB),
 T(112, 'directions composed', 'h_phi = v_(psi - nu) = v_psi h_nu - h_psi v_nu = (1 + ecc h_nu)/sqrt(1 + ecc^2 + 2 ecc h_nu)', o112, n112, P_ORB),
 T(113, 'directions composed', 'slope of phi = ecc v_nu/(1 + ecc h_nu)', o113, n113, P_ORB),
 T(114, 'the double direction composed', 'sigma_n = (sx + sy)/2 + (sx - sy)/2 (h^2 - v^2) + tau 2hv', lambda p: M114(p, 'o'), lambda p: M114(p, 'n'), P_M),
 T(115, 'the double direction composed', 'tau_n = -(sx - sy)/2 (2hv) + tau (h^2 - v^2)', lambda p: M115(p, 'o'), lambda p: M115(p, 'n'), P_M),
 T(116, 'the angle a direction', 'sigma_n dA - sx dA h^2 - sy dA v^2 - tau dA h v - tau dA v h = 0; sigma_n = sx h^2 + sy v^2 + 2 tau v h',
   lambda p: M116(p, 'o'), lambda p: M116(p, 'n'), P_M),
 T(117, 'the double direction composed', 'h^2 = (1 + (h^2 - v^2))/2, v^2 = (1 - (h^2 - v^2))/2, 2hv = 2 v h', lambda p: M117(p, 'o'),
   lambda p: M117(p, 'n'), P_Z),
 T(118, 'the angle a direction', "sigma' = [h v; -v h] sigma [h -v; v h]", lambda p: M118(p, 'o'), lambda p: M118(p, 'n'), P_M),
 T(119, 'an angle given by its slope (settled call 1)', 'the slope of the double of theta_p is 2tau/(sy - sx): with t the half-slope, 2t/(1 - t^2) = 2tau/(sy - sx)',
   o119, n119, [(R(50), R(-10), R(40)), (R(3), R(7), R(-2)), (R('1.5'), R('0.2'), R('0.9'))]),
 T(120, 'an angle given by an inverse function (settled call 1)', 'the slope of the double of theta_p is 2*40/(-10 - 50) = -4/3', o120, n120, P3),
]
