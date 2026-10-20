"""IMS run 1: importance sampling a changing view without rebuilding tables (plans/ims-plan.md).
Run from the repository's root: python3 runs/ims/ims.py"""
import numpy as np
import mpmath as mp

# ---------- I1: closure, exact ----------
mp.mp.dps = 60
rng = np.random.default_rng(402)
PTS = []
for _ in range(200):
    v = [mp.mpf(float(t)) for t in rng.normal(size=3)]; nv = mp.sqrt(sum(t * t for t in v)); PTS.append([t / nv for t in v])
chart = lambda x: mp.mpc(x[0], x[1]) / (1 - x[2])
def unchart(z):
    a = abs(z) ** 2; return [2 * z.real / (a + 1), 2 * z.imag / (a + 1), (a - 1) / (a + 1)]
def push_density(M, w):
    (a, b), (c, d) = M
    z = (d * w - b) / (-c * w + a); dz = 1 / (-c * w + a) ** 2
    return (1 + abs(w) ** 2) ** 2 / (1 + abs(z) ** 2) ** 2 * abs(dz) ** 2 / (4 * mp.pi)
def KM(rho, mu, x):
    return ((1 - rho ** 2) / (1 + rho ** 2 - 2 * rho * sum(m * t for m, t in zip(mu, x)))) ** 2 / (4 * mp.pi)
boost = lambda eta: ((mp.e ** (eta / 2), 0), (0, mp.e ** (-eta / 2)))
worst_a = 0
for eta in (mp.mpf('0.5'), mp.mpf(2), mp.mpf(4)):
    for x in PTS:
        w = chart(x); p = push_density(boost(eta), w)
        worst_a = max(worst_a, abs(p / KM(mp.tanh(eta / 2), [0, 0, 1], unchart(w)) - 1))
i1a = worst_a < mp.mpf(10) ** -40
def mul(P, Q):
    return ((P[0][0] * Q[0][0] + P[0][1] * Q[1][0], P[0][0] * Q[0][1] + P[0][1] * Q[1][1]),
            (P[1][0] * Q[0][0] + P[1][1] * Q[1][0], P[1][0] * Q[0][1] + P[1][1] * Q[1][1]))
h = mp.pi / 4; Ry = ((mp.cos(h), -mp.sin(h)), (mp.sin(h), mp.cos(h)))
Ryi = ((mp.cos(h), mp.sin(h)), (-mp.sin(h), mp.cos(h)))
B1 = mul(mul(Ry, boost(mp.mpf(1))), Ryi)                     # a boost of 1 about the turned axis
Mc = mul(B1, boost(mp.mpf(2)))
X = []; Y = []
for x in PTS:
    w = chart(x); xx = unchart(w); X.append([1] + xx); Y.append(push_density(Mc, w) ** mp.mpf(-0.5))
A = mp.matrix(X); b = mp.matrix(Y); sol = mp.qr_solve(A, b)[0]
res = max(abs((A * sol)[i] - b[i]) / abs(b[i]) for i in range(len(Y)))
i1b = res < mp.mpf(10) ** -40
print(f"I1 (a) worst |push/KM - 1| over 600 points: {mp.nstr(worst_a, 3)}; (b) affine residual of p^-1/2 for the "
      f"composed boosts: {mp.nstr(res, 3)} (fit {[mp.nstr(t, 6) for t in sol]})")
print("I1", "not killed" if (i1a and i1b) else "KILLED")

# ---------- quadrature ----------
def grid(nc, nphi, g):
    """Gauss-Legendre points of an equal-area (cos theta, phi) grid: arrays c, phi, weight, and cell indices."""
    t, wt = np.polynomial.legendre.leggauss(g)
    ce = np.linspace(-1, 1, nc + 1); pe = np.linspace(0, 2 * np.pi, nphi + 1)
    hc, hp = 1 / nc, np.pi / nphi
    C = ((ce[:-1] + ce[1:]) / 2)[:, None] + hc * t[None, :]; P = ((pe[:-1] + pe[1:]) / 2)[:, None] + hp * t[None, :]
    WC = hc * wt[None, :].repeat(nc, 0); WP = hp * wt[None, :].repeat(nphi, 0)
    return C, P, WC, WP

KAPPA, TS = 500.0, np.radians(60)
MU_S = np.array([np.sin(TS), 0, np.cos(TS)])
def L2v(c, phi):   # 1 + 4*pi*p, p the vMF density
    s = np.sqrt(np.clip(1 - c * c, 0, None)); dot = s * np.cos(phi) * MU_S[0] + c * MU_S[2]
    p = KAPPA / (2 * np.pi * (1 - np.exp(-2 * KAPPA))) * np.exp(KAPPA * (dot - 1))
    return 1 + 4 * np.pi * p
L1v = lambda c, phi: np.ones(np.broadcast(c, phi).shape)

def run(eta, k, Lf, g, N=64, NC=128, NP=256):
    be, ga = np.tanh(eta), np.cosh(eta)
    C, P, WC, WP = grid(NC, NP, g)
    # obs-frame table T(N): cell centres in obs frame, f there
    oc = np.linspace(-1, 1, N + 1); oce = (oc[:-1] + oc[1:]) / 2; op = (np.arange(2 * N) + 0.5) * np.pi / N
    yc = (oce - be) / (1 - be * oce); Dob = 1 / (ga * (1 - be * oce))
    fT = (Dob[:, None] ** k) * Lf(yc[:, None], op[None, :]); cell = (2 / N) * (np.pi / N)
    qT = fT / (fT.sum() * cell)
    # rest-frame payload table for M(N)
    rce = (oc[:-1] + oc[1:]) / 2
    LT = Lf(rce[:, None], op[None, :]); qM_tab = LT / (LT.sum() * cell)
    acc = dict(F=0.0, U=0.0, C=0.0, T=0.0, M=0.0)
    for i in range(NC):
        c = C[i][:, None, None]; wc = WC[i][:, None, None]
        ph = P.reshape(-1)[None, None, :]; wp = WP.reshape(-1)[None, None, :]
        w = (wc * wp)                                     # rest-frame solid angle weights
        D = ga * (1 + be * c)                             # Doppler factor at the rest direction
        L = Lf(c, ph); D = np.broadcast_to(D, L.shape)
        acc['F'] += (D ** (k - 2) * L * w).sum()
        acc['U'] += (4 * np.pi * D ** (2 * k - 2) * L ** 2 * w).sum()
        acc['C'] += (4 * np.pi * D ** (2 * k - 4) * L ** 2 * w).sum()
        cobs = (c + be) / (1 + be * c); cobs = np.broadcast_to(cobs, L.shape)
        ic = np.clip(((cobs + 1) / 2 * N).astype(int), 0, N - 1); ip = np.clip((ph / (np.pi / N)).astype(int), 0, 2 * N - 1)
        ip = np.broadcast_to(ip, L.shape)
        acc['T'] += (D ** (2 * k - 2) * L ** 2 / qT[ic, ip] * w).sum()    # f^2/q dOmega_obs = D^(2k) L^2 /q * D^-2 dOmega_rest
        jc = np.clip(((np.broadcast_to(c, L.shape) + 1) / 2 * N).astype(int), 0, N - 1)
        acc['M'] += (D ** (2 * k - 4) * L ** 2 / qM_tab[jc, ip] * w).sum()
    F = acc['F']
    return {s: acc[s] / F ** 2 - 1 for s in ('U', 'C', 'T', 'M')}

ETAS = (0.5, 2.0, 4.0)
R = {}
for g in (16, 24):
    for eta in ETAS:
        for k in (2, 4):
            for name, Lf in (('L1', L1v), ('L2', L2v)):
                R[(g, eta, k, name)] = run(eta, k, Lf, g)
    print(f"quadrature at {g} x {g} done", flush=True)
err = lambda key, s: abs(R[(16,) + key][s] - R[(24,) + key][s])
print("\neta   k  payload   V_U            V_C            V_T(64)        V_M(64)      (16x16; |16 - 24| in brackets)")
for eta in ETAS:
    for k in (2, 4):
        for name in ('L1', 'L2'):
            r = R[(16, eta, k, name)]
            print(f"{eta:<5} {k}  {name}       " + "  ".join(f"{r[s]:.6e} [{err((eta, k, name), s):.1e}]" for s in 'UCTM'))
V = lambda eta, k, name, s: R[(16, eta, k, name)][s]
tol = lambda eta, k, name, s: 10 * err((eta, k, name), s) + 1e-12
i2a = all(abs(V(e, 2, 'L1', 'C')) <= tol(e, 2, 'L1', 'C') for e in ETAS)
i2b = all(V(e, 4, 'L1', 'C') > tol(e, 4, 'L1', 'C') and V(e, 4, 'L1', 'C') < V(e, 4, 'L1', 'U') for e in ETAS)
print("\nI2", "not killed" if (i2a and i2b) else "KILLED", f"(k=2 V_C {[f'{V(e,2,chr(76)+chr(49),chr(67)):.1e}' for e in ETAS]})")
vc = [V(e, 2, 'L2', 'C') for e in ETAS]; t3 = max(tol(e, 2, 'L2', 'C') for e in ETAS)
i3a = max(vc) - min(vc) <= t3
i3b = all(V(e, k, 'L2', 'T') < V(e, k, 'L2', 'C') for e in ETAS for k in (2, 4))
print(f"I3 (a) k=2 V_C across eta {[f'{v:.6f}' for v in vc]}:", "not killed" if i3a else "KILLED",
      "; (b) T(64) below C everywhere:", "not killed" if i3b else "KILLED")
vm = [V(e, 2, 'L2', 'M') for e in ETAS]; t4 = max(tol(e, 2, 'L2', 'M') for e in ETAS)
i4a = max(vm) - min(vm) <= t4
i4b = all(V(e, 2, 'L2', 'M') <= V(e, 2, 'L2', 'T') for e in (2.0, 4.0))
i4c = all(V(e, 4, 'L2', 'M') < V(e, 4, 'L2', 'C') for e in ETAS)
print(f"I4 (a) k=2 V_M across eta {[f'{v:.6f}' for v in vm]}:", "not killed" if i4a else "KILLED",
      "; (b) M <= T at eta 2, 4:", "not killed" if i4b else "KILLED", "; (c) k=4 M < C:", "not killed" if i4c else "KILLED")
print("I5 a view change: T(64) 8,192 evaluations of f plus its sums; C and M none (one 2x2 product); M's table built once")
print("I6", "not killed" if (i1a and i1b and i3a and i4a) else "KILLED")
