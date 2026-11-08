# TWG: the Thomas-Wigner rotation read from directions alone. Predictions in plans/twg-plan.md.
import mpmath as mp, random
mp.mp.dps = 60
I = mp.mpc(0, 1)

def boost4(beta, n):  # pure boost of the observer by velocity beta*n, acting on (t, x, y, z)
    g = 1/mp.sqrt(1 - beta**2); n = [x/mp.sqrt(sum(y*y for y in n)) for x in n]
    L = mp.matrix(4, 4); L[0, 0] = g
    for i in range(3):
        L[0, i+1] = L[i+1, 0] = -g*beta*n[i]
        for j in range(3):
            L[i+1, j+1] = (1 if i == j else 0) + (g - 1)*n[i]*n[j]
    return L

def seen(L, d):  # a star in direction d sends photons along -d; the observer sees -p'/p'0
    p = mp.matrix([1, -d[0], -d[1], -d[2]]); q = L*p
    return [-q[1]/q[0], -q[2]/q[0], -q[3]/q[0]]

def stereo(d): return (d[0] + I*d[1])/(1 - d[2])

def T(z1, z2, z3):  # Moebius matrix sending z1, z2, z3 to 0, 1, infinity
    return mp.matrix([[z2 - z3, -z1*(z2 - z3)], [z2 - z1, -z3*(z2 - z1)]])

def fit(zs, ws):
    M = mp.inverse(T(*ws))*T(*zs); dt = mp.det(M); return M/mp.sqrt(dt)

def apply(M, z): return (M[0, 0]*z + M[0, 1])/(M[1, 0]*z + M[1, 1])

def dag(M): return mp.matrix([[mp.conj(M[0, 0]), mp.conj(M[1, 0])], [mp.conj(M[0, 1]), mp.conj(M[1, 1])]])

def polar_rot(M):  # M = H U, H = sqrt(M M^dagger); return the rotation angle of U and U
    A = M*dag(M); s = mp.sqrt(mp.det(A)); H = (A + s*mp.eye(2))/mp.sqrt(A[0, 0] + A[1, 1] + 2*s)
    U = mp.inverse(H)*M
    # run 2 (W3'): the angle from U's part along the Pauli matrices, 2*asin(|.|), which keeps every digit near 0
    sg = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -I], [I, 0]]), mp.matrix([[1, 0], [0, -1]])]
    s = mp.sqrt(sum(abs((sg[k]*U)[0, 0] + (sg[k]*U)[1, 1])**2/4 for k in range(3)))
    return 2*mp.asin(min(s, mp.mpf(1))), U

rng = random.Random(7)
def stars(k):
    out = []
    while len(out) < k:
        v = [mp.mpf(rng.gauss(0, 1)) for _ in range(3)]; r = mp.sqrt(sum(x*x for x in v))
        if r > 0.1: out.append([x/r for x in v])
    return out

def read(L, S):  # the reader's map, from the first three stars' directions; residual on the rest
    zs = [stereo(d) for d in S]; ws = [stereo(seen(L, d)) for d in S]
    M = fit(zs[:3], ws[:3]); res = max(abs(apply(M, z) - w) for z, w in zip(zs[3:], ws[3:]))
    return M, res

def nvec(phi): return [mp.cos(phi), mp.sin(phi), mp.mpf(0)]
worst = {}
def note(k, v): worst[k] = max(worst.get(k, 0), abs(v))

# W1: collinear
for z1, z2 in [(0.5, 0.8), (1.5, 2.0), (3, 0.2)]:
    z1, z2 = mp.mpf(z1), mp.mpf(z2); n = [mp.mpf(1)/3, mp.mpf(2)/3, mp.mpf(2)/3]
    S = stars(23)
    M1, r1 = read(boost4(mp.tanh(z1), n), S); note('W1 residual', r1)
    note('W1 zeta read', 2*mp.acosh(abs(mp.re(M1[0, 0] + M1[1, 1]))/2) - z1)
    M, r = read(boost4(mp.tanh(z2), n)*boost4(mp.tanh(z1), n), S); note('W1 residual', r)
    zr = 2*mp.acosh(abs(mp.re(M[0, 0] + M[1, 1]))/2); note('W1 sum', zr - (z1 + z2))
    b1, b2 = mp.tanh(z1), mp.tanh(z2); note('W1 velocity law', mp.tanh(zr) - (b1 + b2)/(1 + b1*b2))
    note('W1 rotation (collinear)', polar_rot(M)[0])
    # on the chart centred on +z (n = e_z) the map is z -> k z
    Mz, _ = read(boost4(mp.tanh(z1), [0, 0, 1]), S)
    note('W1 slide (off-diagonal)', abs(Mz[0, 1]) + abs(Mz[1, 0]))
    note('W1 slide (ln k = zeta)', abs(mp.log(abs(Mz[0, 0]/Mz[1, 1]))) - z1)

# W2, W4, W5
print('phi  z1   z2   Omega_read        Omega_formula     |diff|')
for phi_deg in [30, 60, 90, 135]:
    for z1, z2 in [(0.5, 0.8), (1.5, 2.0), (3, 0.2)]:
        phi = mp.radians(phi_deg); z1, z2 = mp.mpf(z1), mp.mpf(z2)
        L = boost4(mp.tanh(z2), nvec(phi))*boost4(mp.tanh(z1), nvec(0))
        oms = []
        for t in range(5):
            M, r = read(L, stars(23)); note('W2 residual (20 more stars)', r); oms.append(polar_rot(M)[0])
        a, b = mp.tanh(z1/2), mp.tanh(z2/2)
        om_f = 2*mp.atan2(a*b*mp.sin(phi), 1 + a*b*mp.cos(phi))
        note('W2 vs half-rapidity formula', oms[0] - om_f)
        note('W4 spread over five triples', max(oms) - min(oms))
        if phi_deg == 90:
            g1, g2 = mp.cosh(z1), mp.cosh(z2); note('W2 vs gamma formula (90 deg)', mp.cos(oms[0]) - (g1 + g2)/(1 + g1*g2))
        # W5: velocity triangle, sides z1, z2, included angle pi - phi
        C = mp.pi - phi; cc = mp.cosh(z1)*mp.cosh(z2) - mp.sinh(z1)*mp.sinh(z2)*mp.cos(C); c = mp.acosh(cc)
        def ang(opp, s1, s2): return mp.acos((mp.cosh(s1)*mp.cosh(s2) - mp.cosh(opp))/(mp.sinh(s1)*mp.sinh(s2)))
        A = ang(z2, z1, c); B = ang(z1, z2, c)
        note('W5 area (defect) vs Omega', (mp.pi - (A + B + C)) - oms[0])
        print(phi_deg, float(z1), float(z2), mp.nstr(oms[0], 15), mp.nstr(om_f, 15), mp.nstr(abs(oms[0] - om_f), 3))

# W3: one read
for z1 in [0.3, 1.0, 4.0]:
    for n in [[1, 0, 0], [0, 0, 1], [1, 2, 3]]:
        M, r = read(boost4(mp.tanh(mp.mpf(z1)), [mp.mpf(x) for x in n]), stars(23)); note('W3 one read, rotation', polar_rot(M)[0])

# W6: small loops of boosts and of turns, in SL(2,C)
sig = [mp.matrix([[0, 1], [1, 0]]), mp.matrix([[0, -I], [I, 0]]), mp.matrix([[1, 0], [0, -1]])]
def ndots(n): return sum((n[i]*sig[i] for i in range(3)), mp.zeros(2))
def expm2(A): return mp.expm(A)
def axis_angle(U):  # U = cos(w/2) - i sin(w/2) u.sigma (up to sign)
    if mp.re(U[0, 0] + U[1, 1]) < 0: U = -U
    c = mp.re(U[0, 0] + U[1, 1])/2; w = 2*mp.acos(min(c, mp.mpf(1)))
    u = [-mp.im((sig[k]*U)[0, 0] + (sig[k]*U)[1, 1])/2 for k in range(3)]  # tr(sigma_k U) = -2i sin(w/2) u_k
    nn = mp.sqrt(sum(x*x for x in u)); return w, [x/nn for x in u]
print('\nW6  eps     boost loop angle/(eps^2 sin phi)   turn loop    axes dot')
for phi_deg in [60, 90]:
    phi = mp.radians(phi_deg); n1, n2 = nvec(0), nvec(phi)
    for eps in [mp.mpf('1e-2'), mp.mpf('1e-4')]:
        def loop(gen):
            a, b = gen(n1), gen(n2)
            return expm2(a)*expm2(b)*expm2(-a)*expm2(-b)
        Lb = loop(lambda n: eps/2*ndots(n)); Lt = loop(lambda n: -I*eps/2*ndots(n))
        wb, ub = axis_angle(polar_rot(Lb)[1]); wt, ut = axis_angle(Lt)
        rb, rt = wb/(eps**2*mp.sin(phi)), wt/(eps**2*mp.sin(phi)); dot = sum(x*y for x, y in zip(ub, ut))
        note('W6 ratio-1 at eps=%s' % mp.nstr(eps, 1), max(abs(rb - 1), abs(rt - 1)))
        note('W6 axes dot +1 (should be ~2)', dot + 1 + 2)  # report dot+1: ~0 if antiparallel
        print(phi_deg, mp.nstr(eps, 2), mp.nstr(rb, 12), mp.nstr(rt, 12), mp.nstr(dot, 12))

print('\nworst:')
for k, v in worst.items(): print('  %-36s %s' % (k, mp.nstr(v, 3)))
