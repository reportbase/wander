"""DVG: restatements of runs/dvg/laws.md for runs/dvg/check2.py. Notation laws restate the whole relation in slopes and shares
(a circular angle by its slope s or half-slope, a hyperbolic angle by its hyperbolic slope b, with h = 1/sqrt(1+s^2), v = s/sqrt(1+s^2),
g = 1/sqrt(1-b^2)); a direction's angle given by an inverse function is restated as its slope equal to the same expression."""
import mpmath as mp; mp.mp.dps = 50
S = mp.sqrt
def R(x): return mp.mpf(x)
def N(n, reason): return dict(n=n, notation=False, verdict='none', reason=reason)
def T(n, reason, restated, orig, new, points):
    return dict(n=n, notation=True, verdict='notation', reason=reason, restated=restated, orig=orig, new=new, points=points)
P3 = [R('0.3'), R('1.7'), R('5')]
def h(s): return 1/S(1+s*s)
def v(s): return s/S(1+s*s)
def g(b): return 1/S(1-b*b)
B3 = [R('0.3'), R('-0.5'), R('0.8')]
D = lambda f, x: mp.diff(f, x)          # used only in originals

# rotation-matrix sample entries (any values in (-1, 1) serve: the laws are identities in their arguments)
RM = [(R('0.31'), R('-0.42'), R('0.27'), R('0.55'), R('0.18'), R('-0.63'), R('-0.36'), R('0.47'), R('0.22')),
      (R('-0.71'), R('0.12'), R('0.44'), R('0.33'), R('-0.58'), R('0.29'), R('0.61'), R('-0.25'), R('-0.4')),
      (R('0.5'), R('0.6'), R('-0.35'), R('-0.2'), R('0.66'), R('0.13'), R('0.28'), R('-0.17'), R('0.73'))]
def angles(spec):
    """spec: list of (kind, f) with kind 't' (arctan), 's' (arcsin), 'c' (arccos) of the algebraic argument f(M)."""
    def orig(M):
        out = []
        for k, f in spec:
            x = f(M)
            a = mp.atan(x) if k == 't' else mp.asin(x) if k == 's' else mp.acos(x)
            out.append(mp.tan(a))
        return out
    def new(M):
        out = []
        for k, f in spec:
            x = f(M)
            out.append(x if k == 't' else x/S(1-x*x) if k == 's' else S(1-x*x)/x)
        return out
    return orig, new
def E(i, j): return lambda M: M[3*(i-1)+(j-1)]

def ang_rate(s, sd, sdd=0):   # original: the angle and its first two rates from atan of the slope's path
    th = lambda t: mp.atan(s + sd*t + sdd*t*t/2)
    return th(0), mp.diff(th, 0), mp.diff(th, 0, 2)

LAWS = []
A = LAWS.append

A(T(1, 'rapidity by its hyperbolic slope', 'g(-b) = g(b), g(b) = 1/√(1-b²)',
    lambda b: [mp.cosh(-mp.atanh(b)), mp.cosh(mp.atanh(b))], lambda b: [g(-b), g(b)], B3))
A(T(2, 'rapidity by its hyperbolic slope', '(-b)·g(-b) = -(b·g(b))',
    lambda b: [mp.sinh(-mp.atanh(b)), -mp.sinh(mp.atanh(b))], lambda b: [(-b)*g(-b), -(b*g(b))], B3))
def o3(p):
    b, ct, x = p; w = mp.atanh(b); return [mp.cosh(w)*ct - mp.sinh(w)*x, -mp.sinh(w)*ct + mp.cosh(w)*x]
def n3(p):
    b, ct, x = p; G = g(b); return [G*(ct - b*x), G*(x - b*ct)]
A(T(3, 'boost in the hyperbolic slope', "(ct', x') = [[g, -bg], [-bg, g]]·(ct, x)", o3, n3,
    [(R('0.3'), R('2'), R('1')), (R('-0.6'), R('1.5'), R('-3')), (R('0.9'), R('0.2'), R('4'))]))
def o4(b):
    w = mp.atanh(b); M = mp.expm(mp.matrix([[0, -w], [-w, 0]])); return [M[0, 0], M[0, 1], M[1, 0], M[1, 1]]
def n4(b):
    G = g(b); return [G, -b*G, -b*G, G]
A(T(4, 'the boost matrix of a rapidity, by its hyperbolic slope', 'Λ = [[g, -bg], [-bg, g]] with b the rapidity\'s hyperbolic slope', o4, n4, B3))
A(N(5, 'matrix exponential of a general matrix times amounts s, t: an exponential of an amount'))
A(T(6, 'cosh of rapidity by its hyperbolic slope', 'γ = 1/√(1-β²) = g(β)',
    lambda b: [1/S(1-b*b), mp.cosh(mp.atanh(b))], lambda b: [g(b), g(b)], B3))
A(T(7, 'rapidity given by its hyperbolic slope', "the rapidity's hyperbolic slope b equals u/c",
    lambda p: [p[0]/p[1], mp.tanh(mp.atanh(p[0]/p[1]))], lambda p: [p[0]/p[1], p[0]/p[1]],
    [(R('1'), R('3')), (R('-2'), R('5')), (R('7'), R('8'))]))
A(T(8, 'cosh of artanh is algebraic', 'g(v/c) = 1/√(1-v²/c²) = γ',
    lambda b: [mp.cosh(mp.atanh(b)), 1/S(1-b*b)], lambda b: [g(b), g(b)], B3))
A(T(9, 'sinh of artanh is algebraic', 'b·g(b) = (v/c)/√(1-v²/c²) = βγ',
    lambda b: [mp.sinh(mp.atanh(b)), b/S(1-b*b)], lambda b: [b*g(b), b*g(b)], B3))
A(T(10, 'energy and momentum by the hyperbolic slope', 'E = mc²·g(b), |p| = mc·b·g(b)',
    lambda p: [p[0]*p[1]**2*mp.cosh(mp.atanh(p[2])), p[0]*p[1]*mp.sinh(mp.atanh(p[2]))],
    lambda p: [p[0]*p[1]**2*g(p[2]), p[0]*p[1]*p[2]*g(p[2])],
    [(R('2'), R('3'), R('0.4')), (R('1'), R('1'), R('-0.7')), (R('5'), R('0.5'), R('0.95'))]))
def o11(p):
    m, c, P = p; En = S(P*P*c*c + m*m*c**4)
    w1 = mp.atanh(P*c/En); w2 = mp.log((En + P*c)/(En - P*c))/2; w3 = mp.log((En + P*c)/(m*c*c))
    return [mp.tanh(w1), mp.tanh(w2), mp.tanh(w3)]
def n11(p):
    m, c, P = p; En = S(P*P*c*c + m*m*c**4); q = (En + P*c)/(m*c*c)
    return [P*c/En, ((En + P*c)/(En - P*c) - 1)/((En + P*c)/(En - P*c) + 1), (q*q - 1)/(q*q + 1)]
A(T(11, 'rapidity given by inverse hyperbolic functions: its hyperbolic slope', "b = |p|c/E; with r = (E+|p|c)/(E-|p|c), b = (r-1)/(r+1); with q = (E+|p|c)/(mc²), b = (q²-1)/(q²+1)",
    o11, n11, [(R('1'), R('1'), R('0.5')), (R('2'), R('3'), R('7')), (R('0.3'), R('2'), R('-1'))]))
A(T(12, 'rapidity given by a logarithm: its hyperbolic slope', 'b_y = p_z c/E',
    lambda p: [mp.tanh(mp.log((p[0] + p[1]*p[2])/(p[0] - p[1]*p[2]))/2)], lambda p: [p[1]*p[2]/p[0]],
    [(R('5'), R('1'), R('2')), (R('3'), R('-2'), R('1')), (R('10'), R('0.3'), R('3'))]))
def o13(p):
    u, s, up, sp = p; a, ap = mp.atan(s), mp.atan(sp)
    return [u*mp.cos(a), u*mp.sin(a), up*mp.cos(ap), up*mp.sin(ap)]
def n13(p):
    u, s, up, sp = p; return [u*h(s), u*v(s), up*h(sp), up*v(sp)]
PT4 = [(R('0.4'), R('0.7'), R('0.6'), R('-1.3')), (R('0.9'), R('-2'), R('0.2'), R('0.5')), (R('0.1'), R('3'), R('0.8'), R('0.25'))]
A(T(13, 'direction as input, by its shares', "u_x = u·h, u_y = u·v, u_x' = u'·h', u_y' = u'·v'", o13, n13, PT4))
def sp14(up, ch, sh, V, c):
    return S(up*up + V*V + 2*V*up*ch - (V*up*sh/c)**2)/(1 + V*up*ch/c**2)
def o14(p):
    up, sp, V, c = p; a = mp.atan(sp); return [sp14(up, mp.cos(a), mp.sin(a), V, c)]
def n14(p):
    up, sp, V, c = p; return [S(up*up + V*V + 2*V*up*h(sp) - (V*up*v(sp)/c)**2)/(1 + V*up*h(sp)/c**2)]
PT14 = [(R('0.5'), R('0.7'), R('0.3'), R('1')), (R('2'), R('-1.5'), R('1'), R('3')), (R('0.9'), R('4'), R('0.6'), R('1'))]
A(T(14, "θ' a direction, by its shares", "u = √(u'² + V² + 2Vu'h' - (Vu'v'/c)²)/(1 + (V/c²)u'h')", o14, n14, PT14))
def f15(up, ch, sh, V, c):
    ux, uy = up*ch, up*sh; den = 1 + V*ux/c**2
    first = S(((ux + V)/den)**2 + (uy*S(1 - V*V/c**2)/den)**2)
    mid = S((ux + V)**2 + (1 - V*V/c**2)*uy**2)/den
    return [first, mid, S(up*up + V*V + 2*V*up*ch - (V*up*sh/c)**2)/den]
def o15(p):
    up, sp, V, c = p; a = mp.atan(sp); return f15(up, mp.cos(a), mp.sin(a), V, c)
def n15(p):
    up, sp, V, c = p; ux, uy = up*h(sp), up*v(sp); den = 1 + V*ux/c**2
    return [S(((ux + V)/den)**2 + (uy*S(1 - V*V/c**2)/den)**2), S((ux + V)**2 + (1 - V*V/c**2)*uy**2)/den,
            S(up*up + V*V + 2*V*up*h(sp) - (V*up*v(sp)/c)**2)/den]
A(T(15, "θ' a direction, by its shares; each form of the chain", "u = √(u_x² + u_y²) = √((u_x'+V)² + (1-V²/c²)u_y'²)/(1 + (V/c²)u_x') = √(u'² + V² + 2Vu'h' - (Vu'v'/c)²)/(1 + (V/c²)u'h'), u_x' = u'h', u_y' = u'v'",
    o15, n15, PT14))
def o16(p):
    sp, V, c = p; a = mp.atan(sp); be = V/c
    x1 = S(1 - be*be)*c*mp.sin(a)/(c*mp.cos(a) + V)
    return [mp.tan(mp.atan(x1)), S(1 - be*be)*mp.sin(a)/(mp.cos(a) + be)]
def n16(p):
    sp, V, c = p; be = V/c
    return [S(1 - be*be)*c*v(sp)/(c*h(sp) + V), S(1 - be*be)*v(sp)/(h(sp) + be)]
PT16 = [(R('0.7'), R('0.3'), R('1')), (R('-2'), R('1'), R('4')), (R('3.5'), R('0.45'), R('0.5'))]
A(T(16, 'aberration: the slope of θ in the shares of θ\'', "s_θ = √(1-V²/c²)·c·v'/(c·h' + V) = √(1-V²/c²)·v'/(h' + V/c)", o16, n16, PT16))
def o17(p):
    sp, V, c = p; a = mp.atan(sp); be = V/c
    th = mp.atan2(S(1 - be*be)*mp.sin(a), mp.cos(a) + be)
    return [mp.sin(th) - mp.sin(a), mp.sin(a)*(S(1 - be*be)/(1 + be*mp.cos(a)) - 1), -be*mp.sin(a)*mp.cos(a)]
def n17(p):
    sp, V, c = p; be = V/c; nu = S(1 - be*be)*v(sp); de = h(sp) + be
    vth = nu/S(nu*nu + de*de)
    return [vth - v(sp), v(sp)*(S(1 - be*be)/(1 + be*h(sp)) - 1), -be*v(sp)*h(sp)]
A(T(17, 'directions by shares; the first-order form restated whole', "v_θ - v' = v'(√(1-V²/c²)/(1 + (V/c)h') - 1), with v_θ = √(1-V²/c²)v'/(1 + (V/c)h'); first order -(V/c)·v'·h'",
    o17, n17, PT16))
A(N(18, 'the small-angle form uses the angle difference θ\'-θ itself as an amount; not restatable in part'))
A(N(19, 'first-order aberration equates the angle difference itself (an amount of angle) to a share'))
def o20(p):
    V, c, nup, sv, s = p; return [nup*(1 + (V/sv)*mp.cos(mp.atan(s)))/S(1 - V*V/c**2)]
def n20(p):
    V, c, nup, sv, s = p; return [nup*(1 + (V/sv)*h(s))/S(1 - V*V/c**2)]
A(T(20, 'θ a direction, by its share', "ν = γ_V·ν'·(1 + (V/s')·h_θ)", o20, n20,
    [(R('0.3'), R('1'), R('2'), R('0.7'), R('0.5')), (R('1'), R('3'), R('5'), R('2'), R('-1.2')), (R('0.6'), R('1'), R('1'), R('0.9'), R('4'))]))
A(T(21, 'a stated direction: its shares', 'the direction θ has shares (h, v) = (0, 1)',
    lambda x: [mp.cos(mp.pi/2), mp.sin(mp.pi/2)], lambda x: [0, 1], [1, 2, 3]))
A(T(22, 'rapidities by hyperbolic slopes; their sum by slope addition', 'b_v = v/c, b_u\' = u\'/c, u/c = (b_v + b_u\')/(1 + b_v·b_u\')',
    lambda p: [mp.tanh(mp.atanh(p[0])), mp.tanh(mp.atanh(p[1])), mp.tanh(mp.atanh(p[0]) + mp.atanh(p[1]))],
    lambda p: [p[0], p[1], (p[0] + p[1])/(1 + p[0]*p[1])],
    [(R('0.3'), R('0.5')), (R('-0.6'), R('0.9')), (R('0.95'), R('0.99'))]))
def m23(b, dbr, ct, st, cp, sp, dth, dph):
    bv = [b*st*cp, b*st*sp, b*ct]
    rh = [st*cp, st*sp, ct]; thh = [ct*cp, ct*sp, -st]; phh = [-sp, cp, 0]
    db = [dbr*rh[i] + b*dth*thh[i] + b*st*dph*phh[i] for i in range(3)]
    cr = [bv[1]*db[2] - bv[2]*db[1], bv[2]*db[0] - bv[0]*db[2], bv[0]*db[1] - bv[1]*db[0]]
    f1 = (sum(x*x for x in db) - sum(x*x for x in cr))/(1 - b*b)**2
    f2 = dbr**2/(1 - b*b)**2 + b*b/(1 - b*b)*(dth**2 + st*st*dph**2)
    return [f1, f2]
def o23(p):
    b, s, t, dbr, ds, dt = p; th, ph = mp.atan(s), mp.atan(t)
    return m23(b, dbr, mp.cos(th), mp.sin(th), mp.cos(ph), mp.sin(ph), D(mp.atan, s)*ds, D(mp.atan, t)*dt)
def n23(p):
    b, s, t, dbr, ds, dt = p
    return m23(b, dbr, h(s), v(s), h(t), v(t), ds/(1 + s*s), dt/(1 + t*t))
PT23 = [(R('0.3'), R('0.7'), R('1.2'), R('0.1'), R('0.2'), R('-0.3')), (R('0.8'), R('2'), R('0.4'), R('-0.05'), R('0.1'), R('0.4')),
        (R('-0.5'), R('0.3'), R('3'), R('0.2'), R('-0.15'), R('0.05'))]
A(T(23, 'angles and their increments by slopes: dθ = ds/(1+s²)', 'dl² = (dβ² - (β×dβ)²)/(1-β²)² = dβ_r²/(1-β²)² + β²/(1-β²)·(ds²/(1+s²)² + v_θ²·dt²/(1+t²)²)',
    o23, n23, PT23))
A(T(24, 'rapidity given by artanh: its hyperbolic slope', "ζ's hyperbolic slope equals β",
    lambda b: [mp.tanh(mp.atanh(b))], lambda b: [b], B3))
def o25(p):
    b, s, t, db, ds, dt = p; z = mp.atanh(b); dz = D(mp.atanh, b)*db; th = mp.atan(s)
    return [dz**2 + mp.sinh(z)**2*((D(mp.atan, s)*ds)**2 + mp.sin(th)**2*(D(mp.atan, t)*dt)**2)]
def n25(p):
    b, s, t, db, ds, dt = p
    return [(db/(1 - b*b))**2 + b*b/(1 - b*b)*((ds/(1 + s*s))**2 + v(s)**2*(dt/(1 + t*t))**2)]
A(T(25, 'rapidity by its hyperbolic slope, angles by slopes', 'dl² = (db/(1-b²))² + b²/(1-b²)·(ds²/(1+s²)² + v_θ²·dt²/(1+t²)²)', o25, n25, PT23))
A(N(26, 'cos τ and sin τ of a running orbital phase (proper time): circular functions of an amount'))
A(N(27, 'circular functions of the running phase τ and a derivative in it'))
A(N(28, 'cos(γτ + φ): circular function of an amount γτ'))
A(T(29, 'a stated phase angle: its shares', 'the phase φ has shares (h, v) = (0, 1)',
    lambda x: [mp.cos(mp.pi/2), mp.sin(mp.pi/2)], lambda x: [0, 1], [1, 2, 3]))
A(T(30, 'rapidity by its hyperbolic slope', 'Δθ_rot = -(g(b) - 1)·δθ_boost = -(γ - 1)·δθ_boost; Δα = b·g(b)·δθ_boost = γβ·δθ_boost',
    lambda p: [-(mp.cosh(mp.atanh(p[0])) - 1)*p[1], -(1/S(1 - p[0]**2) - 1)*p[1], mp.sinh(mp.atanh(p[0]))*p[1], p[0]/S(1 - p[0]**2)*p[1]],
    lambda p: [-(g(p[0]) - 1)*p[1], -(g(p[0]) - 1)*p[1], p[0]*g(p[0])*p[1], p[0]*g(p[0])*p[1]],
    [(R('0.3'), R('0.01')), (R('0.8'), R('-0.2')), (R('-0.6'), R('0.5'))]))
ZP = [R('-0.6'), R('0.3'), R('0.8')]
A(T(31, 'angle given by arccos: its share and slope', "β's share h_β = Z₃, its slope √(1-Z₃²)/Z₃",
    lambda Z: [mp.cos(mp.acos(Z)), mp.tan(mp.acos(Z))], lambda Z: [Z, S(1 - Z*Z)/Z], ZP))
A(T(32, 'a direction by its shares', 'v² = 1 - h²',
    lambda s: [mp.sin(mp.atan(s))**2, 1 - mp.cos(mp.atan(s))**2], lambda s: [v(s)**2, 1 - h(s)**2], P3))
A(T(33, 'the share v of the direction whose share h is Z₃', 'v_β = √(1 - Z₃²)',
    lambda Z: [mp.sin(mp.acos(Z)), S(1 - Z*Z)], lambda Z: [S(1 - Z*Z), S(1 - Z*Z)], ZP))
def o34(p):
    Z2, Z3, Y3 = p
    return [mp.tan(mp.acos(-Z2/S(1 - Z3*Z3))), mp.tan(mp.acos(Z3)), mp.tan(mp.acos(Y3/S(1 - Z3*Z3)))]
def n34(p):
    Z2, Z3, Y3 = p; a, b, c = -Z2/S(1 - Z3*Z3), Z3, Y3/S(1 - Z3*Z3)
    return [S(1 - a*a)/a, S(1 - b*b)/b, S(1 - c*c)/c]
PT34 = [(R('0.5'), R('0.3'), R('-0.4')), (R('-0.2'), R('-0.7'), R('0.6')), (R('0.1'), R('0.85'), R('0.3'))]
A(T(34, 'angles given by arccos: slopes √(1-x²)/x of the shares', 'α, β, γ have shares -Z₂/√(1-Z₃²), Z₃, Y₃/√(1-Z₃²); slope √(1-x²)/x for share x', o34, n34, PT34))
A(T(35, 'angle given by its v share', 'v_θ = -X₃, slope -X₃/√(1-X₃²)',
    lambda X: [mp.sin(mp.asin(-X)), mp.tan(mp.asin(-X))], lambda X: [-X, -X/S(1 - X*X)], ZP))
A(T(36, 'share h from share v', 'h_θ = √(1 - X₃²)',
    lambda X: [mp.cos(mp.asin(-X)), S(1 - X*X)], lambda X: [S(1 - X*X), S(1 - X*X)], ZP))
def o37(p):
    X2, X3, Y3 = p; return [mp.tan(mp.asin(X2/S(1 - X3*X3))), mp.tan(mp.asin(-X3)), mp.tan(mp.asin(Y3/S(1 - X3*X3)))]
def n37(p):
    X2, X3, Y3 = p; a, b, c = X2/S(1 - X3*X3), -X3, Y3/S(1 - X3*X3)
    return [a/S(1 - a*a), b/S(1 - b*b), c/S(1 - c*c)]
A(T(37, 'angles given by arcsin: slopes x/√(1-x²)', 'ψ, θ, φ have v-shares X₂/√(1-X₃²), -X₃, Y₃/√(1-X₃²); slope x/√(1-x²)', o37, n37, PT34))
def ng(x): return lambda M: -x(M)
def q(a, b): return lambda M: a(M)/b(M)
for n, spec, txt in [
    (38, [('t', q(E(3, 2), E(2, 2))), ('s', ng(E(1, 2))), ('t', q(E(1, 3), E(1, 1)))], 's_α = R₃₂/R₂₂; v_β = -R₁₂; s_γ = R₁₃/R₁₁'),
    (39, [('t', q(E(2, 1), ng(E(3, 1)))), ('c', E(1, 1)), ('t', q(E(1, 2), E(1, 3)))], 's_α = R₂₁/(-R₃₁); h_β = R₁₁; s_γ = R₁₂/R₁₃'),
    (40, [('t', q(ng(E(2, 3)), E(3, 3))), ('s', E(1, 3)), ('t', q(ng(E(1, 2)), E(1, 1)))], 's_α = -R₂₃/R₃₃; v_β = R₁₃; s_γ = -R₁₂/R₁₁'),
    (41, [('t', q(E(3, 2), ng(E(1, 2)))), ('c', E(2, 2)), ('t', q(E(2, 3), E(2, 1)))], 's_α = R₃₂/(-R₁₂); h_β = R₂₂; s_γ = R₂₃/R₂₁'),
    (42, [('t', q(ng(E(3, 1)), E(1, 1))), ('s', E(2, 1)), ('t', q(ng(E(2, 3)), E(2, 2)))], 's_α = -R₃₁/R₁₁; v_β = R₂₁; s_γ = -R₂₃/R₂₂'),
    (43, [('t', q(E(2, 3), E(1, 3))), ('t', lambda M: S(1 - M[8]**2)/M[8]), ('t', q(E(3, 2), ng(E(3, 1))))], 's_α = R₂₃/R₁₃; s_β = √(1-R₃₃²)/R₃₃; s_γ = R₃₂/(-R₃₁)'),
    (44, [('t', q(ng(E(1, 2)), E(2, 2))), ('s', E(3, 2)), ('t', q(ng(E(3, 1)), E(3, 3)))], 's_α = -R₁₂/R₂₂; v_β = R₃₂; s_γ = -R₃₁/R₃₃')]:
    o, nw = angles(spec)
    A(T(n, 'angles given by inverse circular functions: their slopes or shares equal the same expressions', txt + ' (slope from share: v gives v/√(1-v²), h gives √(1-h²)/h)', o, nw, RM))
A(T(45, 'angles and increments by slopes: dα = da/(1+a²)', 'dV ∝ v_β·da/(1+a²)·db/(1+b²)·dc/(1+c²)',
    lambda p: [mp.sin(mp.atan(p[1]))*D(mp.atan, p[0])*D(mp.atan, p[1])*D(mp.atan, p[2])],
    lambda p: [v(p[1])/((1 + p[0]**2)*(1 + p[1]**2)*(1 + p[2]**2))],
    [(R('0.3'), R('1.7'), R('5')), (R('-1'), R('0.4'), R('2')), (R('2.5'), R('3'), R('-0.2'))]))
A(T(46, 'half-angle by its half-slope t', 'R = 1/√(1+t²) - I·u·t/√(1+t²)',
    lambda t: [mp.cos(mp.atan(t)), -mp.sin(mp.atan(t))], lambda t: [1/S(1 + t*t), -t/S(1 + t*t)], P3))
A(T(47, 'a direction by its shares', 'r̂ = h·x̂ + v·ŷ; q̂ = -v·x̂ + h·ŷ',
    lambda s: [mp.cos(mp.atan(s)), mp.sin(mp.atan(s)), -mp.sin(mp.atan(s)), mp.cos(mp.atan(s))], lambda s: [h(s), v(s), -v(s), h(s)], P3))
def k48(r, rd, rdd, c, sn, w, wd):
    rh = [c, sn]; qh = [-sn, c]
    return [r*c, r*sn] + [rd*rh[i] + r*w*qh[i] for i in range(2)] + [(rdd - r*w*w)*rh[i] + (r*wd + 2*rd*w)*qh[i] for i in range(2)]
def o48(p):
    r, rd, rdd, s, sd, sdd = p; th, w, wd = ang_rate(s, sd, sdd); return k48(r, rd, rdd, mp.cos(th), mp.sin(th), w, wd)
def n48(p):
    r, rd, rdd, s, sd, sdd = p; Q = 1 + s*s
    return k48(r, rd, rdd, h(s), v(s), sd/Q, sdd/Q - 2*s*sd*sd/(Q*Q))
PT48 = [(R('2'), R('0.3'), R('-0.1'), R('0.7'), R('0.4'), R('0.2')), (R('1'), R('-1'), R('0.5'), R('-2'), R('1.1'), R('-0.3')),
        (R('5'), R('0.2'), R('0.05'), R('3'), R('-0.2'), R('0.6'))]
A(T(48, 'direction by its slope, angle rates by the slope\'s: θ̇ = ṡ/(1+s²), θ̈ = s̈/(1+s²) - 2sṡ²/(1+s²)²',
    'r = r(h x̂ + v ŷ); ṙ = ṙ r̂ + r·θ̇·q̂; r̈ = (r̈ - r·θ̇²) r̂ + (r·θ̈ + 2ṙ·θ̇) q̂, with r̂ = (h, v), q̂ = (-v, h), θ̇ and θ̈ as stated', o48, n48, PT48))
def k49(r, rd, c, sn, w):
    x, y = r*c, r*sn; xd, yd = rd*c - r*sn*w, rd*sn + r*c*w
    return [abs(x*yd - y*xd), r*r*w]
def o49(p):
    r, rd, s, sd = p; th, w, _ = ang_rate(s, sd); return k49(r, rd, mp.cos(th), mp.sin(th), w)
def n49(p):
    r, rd, s, sd = p; return k49(r, rd, h(s), v(s), sd/(1 + s*s))
PT49 = [(R('2'), R('0.3'), R('0.7'), R('0.4')), (R('1'), R('-1'), R('-2'), R('1.1')), (R('5'), R('0.2'), R('3'), R('0.6'))]
A(T(49, 'direction by slope, its rate ṡ/(1+s²)', 'H = |(rh, rv, 0) × (ṙh - rv·θ̇, ṙv + rh·θ̇, 0)| = r²·ṡ/(1+s²)', o49, n49, PT49))
PTK = [(R('2'), R('3'), R('0.4'), R('0.7')), (R('1'), R('0.5'), R('0.9'), R('-2')), (R('5'), R('1.2'), R('0.1'), R('3'))]
A(T(50, 'the direction θ-θ₀ by its share', 's = (α/H²)·(1 + ecc·h_(θ-θ₀))',
    lambda p: [p[0]/p[1]**2*(1 + p[2]*mp.cos(mp.atan(p[3])))], lambda p: [p[0]/p[1]**2*(1 + p[2]*h(p[3]))], PTK))
A(T(51, 'θ by its share', 'r = p/(1 + ecc·h_θ)',
    lambda p: [p[0]/(1 + p[1]*mp.cos(mp.atan(p[2])))], lambda p: [p[0]/(1 + p[1]*h(p[2]))], [(R('2'), R('0.4'), R('0.7')), (R('1'), R('0.9'), R('-2')), (R('5'), R('0.1'), R('3'))]))
def o52(p):
    al, pp, ec, s = p; H = S(al*pp); a = mp.atan(s); return [H/pp*ec*mp.sin(a), S(al/pp)*ec*mp.sin(a)]
def n52(p):
    al, pp, ec, s = p; H = S(al*pp); return [H/pp*ec*v(s), S(al/pp)*ec*v(s)]
A(T(52, 'θ by its share', 'V_r = (H/p)·ecc·v_θ = √(α/p)·ecc·v_θ', o52, n52, PTK))
def o53(p):
    al, pp, ec, s = p; H = S(al*pp); c = mp.cos(mp.atan(s)); r = pp/(1 + ec*c); return [H/r, S(al/pp)*(1 + ec*c)]
def n53(p):
    al, pp, ec, s = p; H = S(al*pp); r = pp/(1 + ec*h(s)); return [H/r, S(al/pp)*(1 + ec*h(s))]
A(T(53, 'θ by its share', 'V_t = H/r = √(α/p)·(1 + ecc·h_θ), r = p/(1 + ecc·h_θ)', o53, n53, PTK))
A(T(54, 'eccentric anomaly as a direction from the centre, by its share', 'y = b·v_E',
    lambda p: [p[0]*mp.sin(mp.atan(p[1]))], lambda p: [p[0]*v(p[1])], [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
PTE = [(R('2'), R('0.7'), R('0.4')), (R('1'), R('-2'), R('1.1')), (R('5'), R('3'), R('-0.6'))]
def o55(p):
    a, s, sd = p; E_, w, _ = ang_rate(s, sd); return [-a*mp.sin(E_)*w]
A(T(55, 'E by its slope S, Ė = Ṡ/(1+S²)', 'ẋ = -a·v_E·Ṡ/(1+S²)', o55, lambda p: [-p[0]*v(p[1])*p[2]/(1 + p[1]**2)], PTE))
def o56(p):
    b, s, sd = p; E_, w, _ = ang_rate(s, sd); return [b*mp.cos(E_)*w]
A(T(56, 'E by its slope S, Ė = Ṡ/(1+S²)', 'ẏ = b·h_E·Ṡ/(1+S²)', o56, lambda p: [p[0]*h(p[1])*p[2]/(1 + p[1]**2)], PTE))
A(N(57, "Kepler's equation: the anomaly E as an amount beside its share (E - ecc·v_E), equated to a time"))
A(N(58, "Kepler's equation: E as an amount beside its share, equated to a time"))
def hyp(T_, Td):
    Ef = lambda t: mp.atanh(T_ + Td*t); return Ef(0), mp.diff(Ef, 0)
def o59(p):
    b, T_, Td = p; E_, Ed = hyp(T_, Td); return [b*mp.cosh(E_)*Ed]
PTH = [(R('2'), R('0.3'), R('0.2')), (R('1'), R('0.8'), R('-0.1')), (R('5'), R('-0.5'), R('0.4'))]
A(T(59, 'hyperbolic anomaly by its hyperbolic slope T, Ė = Ṫ/(1-T²)', 'ẏ = b·g(T)·Ṫ/(1-T²)', o59,
    lambda p: [p[0]/S(1 - p[1]**2)*p[2]/(1 - p[1]**2)], PTH))
def k60(a, b, ec, ch, shh, Ed):
    x, y = a*(ec - ch), b*shh; xd, yd = -a*shh*Ed, b*ch*Ed
    return [x*yd - y*xd, a*b*(ec*ch - 1)*Ed]
def o60(p):
    a, b, ec, T_, Td = p; E_, Ed = hyp(T_, Td); return k60(a, b, ec, mp.cosh(E_), mp.sinh(E_), Ed)
def n60(p):
    a, b, ec, T_, Td = p; return k60(a, b, ec, g(T_), T_*g(T_), Td/(1 - T_*T_))
A(T(60, 'hyperbolic anomaly by its hyperbolic slope', 'H = xẏ - yẋ = ab(ecc·g(T) - 1)·Ṫ/(1-T²), x = a(ecc - g(T)), y = b·T·g(T)', o60, n60,
    [(R('2'), R('1'), R('1.5'), R('0.3'), R('0.2')), (R('1'), R('3'), R('2'), R('0.8'), R('-0.1')), (R('5'), R('0.5'), R('1.2'), R('-0.5'), R('0.4'))]))
def o61(p):
    ec, t = p; E_ = 2*mp.atan(t); th = 2*mp.atan2(S(1 + ec)*mp.sin(E_/2), S(1 - ec)*mp.cos(E_/2)) + 2*mp.pi
    return [mp.tan(th/2)]
A(T(61, 'true anomaly given by arg: its half-slope', 'half-slope of θ = √((1+ecc)/(1-ecc))·(half-slope of E)', o61,
    lambda p: [S((1 + p[0])/(1 - p[0]))*p[1]], [(R('0.3'), R('0.7')), (R('0.9'), R('-2')), (R('0.1'), R('3'))]))
PTH2 = [(R('2'), R('1.5'), R('0.3')), (R('1'), R('2'), R('0.8')), (R('5'), R('1.2'), R('-0.5'))]
A(T(62, 'hyperbolic anomaly by its hyperbolic slope', 'r = a(ecc·g(T) - 1)',
    lambda p: [p[0]*(p[1]*mp.cosh(mp.atanh(p[2])) - 1)], lambda p: [p[0]*(p[1]*g(p[2]) - 1)], PTH2))
def o63(p):
    a, ec, T_ = p; c = mp.cosh(mp.atanh(T_)); return [a*(ec - c)/(a*(ec*c - 1)), (ec - c)/(ec*c - 1)]
def n63(p):
    a, ec, T_ = p; c = g(T_); return [a*(ec - c)/(a*(ec*c - 1)), (ec - c)/(ec*c - 1)]
A(T(63, 'θ by its share, E by its hyperbolic slope', 'h_θ = x/r = (ecc - g(T))/(ecc·g(T) - 1)', o63, n63, PTH2))
def o64(p):
    ec, T_ = p; E_ = mp.atanh(T_); th = mp.acos((ec - mp.cosh(E_))/(ec*mp.cosh(E_) - 1))
    return [mp.tan(th/2), S((ec + 1)/(ec - 1))*mp.tanh(E_/2)]
def n64(p):
    ec, T_ = p; c = (ec - g(T_))/(ec*g(T_) - 1); return [S((1 - c)/(1 + c)), S((ec + 1)/(ec - 1))*T_/(1 + S(1 - T_*T_))]
A(T(64, 'half-slopes: of θ from its share, of E from its hyperbolic slope', 'half-slope of θ, √((1-h_θ)/(1+h_θ)), = √((ecc+1)/(ecc-1))·T/(1 + √(1-T²))', o64, n64,
    [(R('1.5'), R('0.3')), (R('2'), R('0.8')), (R('1.2'), R('0.5'))]))
A(N(65, 'period 2π·a·√(a/α): the whole turn as an amount of time'))
A(T(66, 'θ by its share', 'r = 2f/(1 + h_θ)', lambda p: [2*p[0]/(1 + mp.cos(mp.atan(p[1])))], lambda p: [2*p[0]/(1 + h(p[1]))],
    [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
def o67(p):
    qq, s = p; th = mp.atan(s); r = 2*qq/(1 + mp.cos(th)); x, y = r*mp.cos(th), r*mp.sin(th)
    return [y/x, mp.tan(th), S(x*x + y*y), qq/mp.cos(th/2)**2, 2*qq/(1 + mp.cos(th))]
def n67(p):
    qq, s = p; u = s/(1 + S(1 + s*s)); r = 2*qq/(1 + h(s)); x, y = r*h(s), r*v(s)
    return [y/x, s, S(x*x + y*y), qq*(1 + u*u), 2*qq/(1 + h(s))]
A(T(67, 'θ by slope s and half-slope u = s/(1+√(1+s²))', 'y/x = s; r = √(x²+y²) = q(1 + u²) = 2q/(1 + h_θ)', o67, n67,
    [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
def o68(p):
    K, u, ud = p; th = lambda t: 2*mp.atan(u + ud*t); return [mp.diff(th, 0), 2*K*mp.cos(th(0)/2)**4]
A(T(68, 'θ by its half-slope u: θ̇ = 2u̇/(1+u²)', '2u̇/(1+u²) = 2K/(1+u²)²', o68, lambda p: [2*p[2]/(1 + p[1]**2), 2*p[0]/(1 + p[1]**2)**2],
    [(R('2'), R('0.7'), R('0.4')), (R('1'), R('-2'), R('1.1')), (R('5'), R('3'), R('-0.6'))]))
A(T(69, 'true anomaly by its half-slope', 'half-slope of θ = B - 1/B', lambda B: [mp.tan(mp.atan(B - 1/B))], lambda B: [B - 1/B], P3))
A(T(70, 'a direction by its shares', 'x̂ = h·r̂ - v·t̂', lambda s: [mp.cos(mp.atan(s)), -mp.sin(mp.atan(s))], lambda s: [h(s), -v(s)], P3))
A(T(71, 'a direction by its shares', 'ŷ = v·r̂ + h·t̂', lambda s: [mp.sin(mp.atan(s)), mp.cos(mp.atan(s))], lambda s: [v(s), h(s)], P3))
for n, rs in [(72, 'sin(ωt + φ): circular function of an amount ωt'), (73, 'period 2π/ω: the whole turn as an amount'),
              (74, '2π × energy ratio: the whole turn as an amount'), (75, 'decaying exponential and circular function of time'),
              (76, 'sin(ωt): circular function of time'), (77, 'sin(ωt + φ): circular function of time'),
              (78, 'cos(ωt) = cos(ωτ): circular function of an amount, rescaled time'),
              (79, 'exponentials of the amount τ'), (80, "Euler's formula at the amount ωτ"), (81, 'exponential of an amount i(ωτ+φ)'),
              (82, 'exponential of an amount and its derivatives in τ')]:
    A(N(n, rs))
PTZ = [(R('0.2'), R('0.7')), (R('0.5'), R('1.6')), (R('1.1'), R('0.3'))]
def shz(ze, om):
    Dd = (1 - om*om)**2 + (2*ze*om)**2; return Dd, (1 - om*om)/S(Dd), -2*ze*om/S(Dd)
def phz(ze, om):
    return mp.atan2(-2*ze*om, 1 - om*om)
def o83(p):
    ze, om = p; Dd = (1 - om*om)**2 + (2*ze*om)**2; A_ = 1/S(Dd); ph = phz(ze, om)
    L_ = -om*om*A_ + 2j*ze*om*A_ + A_; r1 = mp.exp(-1j*ph); r2 = mp.cos(ph) - 1j*mp.sin(ph)
    return [L_.real, L_.imag, r1.real, r1.imag, r2.real, r2.imag]
def n83(p):
    ze, om = p; Dd, hp, vp = shz(ze, om); A_ = 1/S(Dd)
    return [-om*om*A_ + A_, 2*ze*om*A_, hp, -vp, hp, -vp]
A(T(83, 'the phase φ a direction of the complex amplitude, by its shares', '-ω²A + 2ζiωA + A = h_φ - i·v_φ', o83, n83, PTZ))
def o84(p):
    ze, om = p; Dd = (1 - om*om)**2 + (2*ze*om)**2; A_ = 1/S(Dd); ph = phz(ze, om)
    return [A_*(1 - om*om), mp.cos(ph), 2*ze*om*A_, -mp.sin(ph)]
def n84(p):
    ze, om = p; Dd, hp, vp = shz(ze, om); A_ = 1/S(Dd); return [A_*(1 - om*om), hp, 2*ze*om*A_, -vp]
A(T(84, 'φ by its shares', 'A(1-ω²) = h_φ; 2ζωA = -v_φ', o84, n84, PTZ))
def o85(p):
    ze, om = p; Dd = (1 - om*om)**2 + (2*ze*om)**2; A_ = 1/S(Dd); ph = phz(ze, om)
    return [A_**2*(1 - om*om)**2, mp.cos(ph)**2, (2*ze*om*A_)**2, mp.sin(ph)**2, A_**2*Dd]
def n85(p):
    ze, om = p; Dd, hp, vp = shz(ze, om); A_ = 1/S(Dd); return [A_**2*(1 - om*om)**2, hp**2, (2*ze*om*A_)**2, vp**2, 1]
A(T(85, 'φ by its shares', 'A²(1-ω²)² = h_φ², (2ζωA)² = v_φ² ⇒ A²[(1-ω²)² + (2ζω)²] = h_φ² + v_φ² = 1', o85, n85, PTZ))
def o86(p):
    ze, om = p; Dd = (1 - om*om)**2 + (2*ze*om)**2; ph = phz(ze, om)
    return [1/S(Dd), mp.sign(-mp.sin(ph)/(2*ze*om))/S(Dd)]
def n86(p):
    ze, om = p; Dd, hp, vp = shz(ze, om); return [1/S(Dd), mp.sign(-vp/(2*ze*om))/S(Dd)]
A(T(86, 'φ by its share v', 'A = sgn(-v_φ/(2ζω))/√((1-ω²)² + (2ζω)²)', o86, n86, PTZ))
def o87(p):
    ze, om = p; ph = phz(ze, om)
    return [mp.tan(ph), -2*ze*om/(1 - om*om), mp.tan(mp.atan(2*ze*om/(om*om - 1)) + mp.pi)]
def n87(p):
    ze, om = p; Dd, hp, vp = shz(ze, om); return [vp/hp, -2*ze*om/(1 - om*om), 2*ze*om/(om*om - 1)]
A(T(87, 'phase given by arctan + nπ: its slope', 's_φ = v_φ/h_φ = -2ζω/(1-ω²) = 2ζω/(ω²-1)', o87, n87, PTZ))
A(N(88, 'cos(ωτ + φ): circular function of the amount ωτ'))
A(N(89, '1/2π: the whole turn as an amount (frequency from angular frequency)'))
A(N(90, '1/2π: the whole turn as an amount'))
def o91(p):
    n1, n2, si = p; i_ = mp.atan(si); r_ = mp.asin(n1*mp.sin(i_)/n2); return [n1*mp.sin(i_), n2*mp.sin(r_)]
def n91(p):
    n1, n2, si = p; w = n1*v(si)/n2; sr = w/S(1 - w*w); return [n1*v(si), n2*v(sr)]
A(T(91, 'directions by their shares', 'n₁·v_i = n₂·v_r', o91, n91, [(R('1'), R('1.5'), R('0.7')), (R('1.3'), R('2'), R('-2')), (R('1'), R('1.33'), R('3'))]))
def o92(p):
    si, st, sr = p; i_, t_, r_ = mp.atan(si), mp.atan(st), mp.atan(sr); return [mp.tan(i_ - t_), mp.tan(t_ - r_), mp.sin(t_)]
def n92(p):
    si, st, sr = p; return [(si - st)/(1 + si*st), (st - sr)/(1 + st*sr), v(st)]
A(T(92, 'directions by slopes, differences by slope subtraction', 'height/u = (s_i - s_θ)/(1 + s_i s_θ); height/v = (s_θ - s_r)/(1 + s_θ s_r); v_θ = height/R', o92, n92,
    [(R('0.7'), R('0.3'), R('0.1')), (R('2'), R('-0.4'), R('1')), (R('-1'), R('0.4'), R('-0.2'))]))
A(T(93, 'θ by its share', 'd·v_θ = λ', lambda p: [p[0]*mp.sin(mp.atan(p[1]))], lambda p: [p[0]*v(p[1])], [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
A(N(94, 'sinc of (dπ/λ)·sin θ: a circular function of an amount carrying π'))
A(N(95, 'sinc x = sin x / x: circular function of an amount x'))
def o96(p):
    d, sm, si = p; a, b = mp.atan(sm), mp.atan(si); return [d*(mp.sin(a) + mp.sin(b)), d*(mp.sin(a) - mp.sin(b))]
A(T(96, 'directions by shares', 'd(v_m ± v_i) = mλ', o96, lambda p: [p[0]*(v(p[1]) + v(p[2])), p[0]*(v(p[1]) - v(p[2]))],
    [(R('2'), R('0.7'), R('0.1')), (R('1'), R('-2'), R('1')), (R('5'), R('3'), R('-0.4'))]))
for n, rs in [(97, 'e^(ikr)/(4πr): exponential of an amount, whole sphere 4π'), (98, 'exponential of an amount, 4π'),
              (99, 'exponentials of amounts, 4π'), (100, 'integral of an exponential of an amount')]:
    A(N(n, rs))
A(T(101, 'θ by its share', 'mλ = 2d·v_θ', lambda p: [2*p[0]*mp.sin(mp.atan(p[1]))], lambda p: [2*p[0]*v(p[1])], [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
for n, rs in [(102, 'k = 2π/λ: the whole turn as an amount'), (103, 'ω = 2πf: the whole turn as an amount'),
              (104, 'cos(kx - ωt + φ): circular function of amounts'), (105, 'circular functions of amounts kx - ωt')]:
    A(N(n, rs))
NP = [R(0), R(1), R(-2)]
A(T(106, 'phases of constructive interference: the phase direction is home', 'the phase has shares (h, v) = (1, 0)',
    lambda n: [mp.cos(2*mp.pi*n), mp.sin(2*mp.pi*n)], lambda n: [1, 0], NP))
A(N(107, 'cos(kx - ωt): circular function of amounts'))
A(T(108, 'phases of destructive interference: the phase direction is opposite home', 'the phase has shares (h, v) = (-1, 0)',
    lambda n: [mp.cos((2*n + 1)*mp.pi), mp.sin((2*n + 1)*mp.pi)], lambda n: [-1, 0], NP))
A(N(109, 'Δφ = 2πd/λ: a phase as an amount carrying 2π'))
def o110(p):
    x, lam, n = p; th = mp.asin((n + R('0.5'))*lam/x); return [x*mp.sin(th)/lam]
def n110(p):
    x, lam, n = p; w = (n + R('0.5'))*lam/x; s = w/S(1 - w*w); return [x*v(s)/lam]
A(T(110, 'θ by its share', 'x·v_θ/λ = ±½, ±3/2, …', o110, n110, [(R('5'), R('1'), 0), (R('10'), R('2'), 1), (R('7'), R('0.5'), -3)]))
A(T(111, 'θ by its share', 'd_f = λ/v_θ', lambda p: [p[0]/mp.sin(mp.atan(p[1]))], lambda p: [p[0]/v(p[1])], [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
A(N(112, 'equally spaced phasors: N-th roots of unity, for general N not given by square roots'))
A(N(113, 'exponential of an amount φ₁(r) - ωt'))
A(N(114, 'time integral of products of exponentials of amounts'))
A(T(115, 'the phase difference as the direction between the two phasors, by its share', 'I = I₁ + I₂ + 2√(I₁I₂)·h_(φ₁-φ₂)',
    lambda p: [p[0] + p[1] + 2*S(p[0]*p[1])*mp.cos(mp.atan(p[2]))], lambda p: [p[0] + p[1] + 2*S(p[0]*p[1])*h(p[2])],
    [(R('2'), R('0.7'), R('0.3')), (R('1'), R('3'), R('-2')), (R('5'), R('0.5'), R('4'))]))
A(T(116, 'the home direction: share h = 1', 'τ·dθ = |τ||dθ|·1 = τ dθ', lambda p: [p[0]*p[1]*mp.cos(0)], lambda p: [p[0]*p[1]*1],
    [(R('2'), R('0.7')), (R('1'), R('-2')), (R('5'), R('3'))]))
for n in (117, 118, 119, 120):
    A(N(n, '2π rad/rev: the whole turn as an amount converting a rate'))
assert [L['n'] for L in LAWS] == list(range(1, 121)), [L['n'] for L in LAWS]
