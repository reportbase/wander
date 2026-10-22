#!/usr/bin/env python3
"""SRR run 1: special relativity and motion revisited (plans/srr-plan.md).

Addresses (directions, aberration, pseudorapidity) against payload (Doppler factor D);
which kind of 'corner' each of MOT run 3's and EMC's corners is.
Identities at 50 digits (mpmath); estimates by seeded sampling (numpy, seed 22).
Run from the repository root: python3 runs/srr/srr.py
"""
import mpmath as mp
import numpy as np

mp.mp.dps = 50
TOL = mp.mpf('1e-40')
BETAS = [mp.mpf('0.1'), mp.mpf('0.6'), 1 / mp.sqrt(2), mp.mpf('0.99')]
verdict = {}


def kill(name, ok):
    verdict[name] = verdict.get(name, True) and bool(ok)


def kfac(b):
    return mp.sqrt((1 + b) / (1 - b))


def seen_cos(c, b):          # source-frame cos -> observer-frame cos (aberration)
    return (c + b) / (1 + b * c)


def source_cos(cp, b):       # inverse aberration
    return (cp - b) / (1 - b * cp)


def xi_of_cos(c):            # pseudorapidity -ln tan(theta/2) = atanh(cos theta)
    return mp.atanh(c)


def cos_of_xi(x):
    return mp.tanh(x)


def D_obs(cp, b):
    return mp.sqrt(1 - b * b) / (1 - b * cp)


grid = [mp.mpf(-6) + mp.mpf(12) * i / 40 for i in range(41)]

# ---------------- P1 ----------------
print("P1: the sky's corner is a median only where the sky is uniform")
w1 = mp.mpf(0)
for b in BETAS:
    eta = mp.atanh(b)
    # source frame: CDF of xi from cos theta uniform on [-1,1]: P(Xi <= x) = P(cos <= tanh x) = (1 + tanh x)/2
    for x in grid:
        F = (1 + cos_of_xi(x)) / 2
        w1 = max(w1, abs(F - 1 / (1 + mp.e ** (-2 * x))))
        t = mp.e ** (-x)
        Ft = lambda tt: (1 - mp.cos(2 * mp.atan(tt))) / 2   # P(T <= t) = P(theta <= 2 atan t)
        w1 = max(w1, abs(Ft(t) + Ft(1 / t) - 1))
    # observer frame, pushed through aberration (not the pan)
    def Fobs(x):
        cp = cos_of_xi(x)
        c = source_cos(cp, b)          # Xi' <= x  <=>  cos' <= tanh x  <=> cos <= source_cos
        return (1 + c) / 2
    for x in grid:
        w1 = max(w1, abs(Fobs(x) - 1 / (1 + mp.e ** (-2 * (x - eta)))))
        dens = mp.diff(Fobs, x)
        w1 = max(w1, abs(dens - mp.sech(x - eta) ** 2 / 2))
    med = mp.findroot(lambda x: Fobs(x) - mp.mpf(1) / 2, eta + mp.mpf('0.3'))
    mean = mp.quad(lambda x: x * mp.diff(Fobs, x), [-mp.inf, eta, mp.inf])
    ahead = 1 - (1 + source_cos(0, b)) / 2      # share seen with cos' > 0
    w1 = max(w1, abs(med - eta), abs(ahead - (1 + b) / 2))
    print(f"  beta={mp.nstr(b,6)}: eta={mp.nstr(eta,12)} median={mp.nstr(med,12)} "
          f"mean={mp.nstr(mean,12)} (|mean-eta|={mp.nstr(abs(mean-eta),3)}) share ahead={mp.nstr(ahead,12)}")
    # 2+1: theta uniform on [0, pi]
    def F2(x):
        cp = cos_of_xi(x)
        th = mp.acos(source_cos(cp, b))
        return (mp.pi - th) / mp.pi
    for x in grid:
        w1 = max(w1, abs(F2(x) - 2 / mp.pi * mp.atan(mp.e ** (x - eta))))
        w1 = max(w1, abs(mp.diff(F2, x) - mp.sech(x - eta) / mp.pi))
print(f"  worst identity miss {mp.nstr(w1,3)}")
kill('P1', w1 < TOL)

# ---------------- P2 ----------------
print("P2: chi is the aberration of the seen median")
w2 = mp.mpf(0)
for b in BETAS:
    chi = mp.asin(b)
    eta = mp.atanh(b)
    # seen cap half-angle a with half the uniform source sky: P(theta' <= a) = P(cos >= source_cos(cos a))
    G = lambda a: (1 - source_cos(mp.cos(a), b)) / 2 - mp.mpf(1) / 2
    a = mp.findroot(G, mp.pi / 2 - chi + mp.mpf('0.01'))
    gd = 2 * mp.atan(mp.tanh(eta / 2))
    w2 = max(w2, abs(a - (mp.pi / 2 - chi)), abs(chi - gd))
    print(f"  beta={mp.nstr(b,6)}: median cap {mp.nstr(a*180/mp.pi,15)} deg, 90-chi {mp.nstr(90-chi*180/mp.pi,15)}")
for Z in [mp.mpf(1) + mp.mpf('0.5'), mp.mpf(2), mp.mpf(3), 2 * mp.asinh(1)]:
    eta1 = mp.findroot(lambda e: mp.sinh(e) - 1, 1)        # w = 1
    share = eta1 / Z if Z > eta1 else mp.mpf(1)
    w2 = max(w2, abs(share - mp.asinh(1) / Z))
    print(f"  uniform in eta on [0,{mp.nstr(Z,8)}]: share below w=1 {mp.nstr(share,15)}")
for half in [mp.mpf('0.1'), mp.mpf('0.5'), mp.pi / 4]:
    lo, hi = mp.pi / 4 - half, mp.pi / 4 + half
    chi1 = mp.findroot(lambda c: mp.tan(c) - 1, mp.mpf('0.7'))
    share = (chi1 - lo) / (hi - lo)
    w2 = max(w2, abs(share - mp.mpf(1) / 2))
for wv in [mp.mpf('0.01'), mp.mpf('0.3'), mp.mpf(3), mp.mpf(70)]:
    Fw = lambda u: 2 / mp.pi * mp.atan(u)
    w2 = max(w2, abs(Fw(wv) + Fw(1 / wv) - 1))
print(f"  2*asinh(1) = {mp.nstr(2*mp.asinh(1),15)}; worst miss {mp.nstr(w2,3)}")
kill('P2', w2 < TOL)

# ---------------- P3 ----------------
print("P3: D a payload function on the addresses; the Doppler swap a reflection about eta/2")
w3 = mp.mpf(0)
for b in BETAS:
    eta = mp.atanh(b)
    k = kfac(b)
    for x in grid:
        D = D_obs(cos_of_xi(x), b)
        w3 = max(w3, abs(D - mp.cosh(x) / mp.cosh(x - eta)))
        w3 = max(w3, abs(D * D_obs(cos_of_xi(eta - x), b) - 1))
        # seen density on levels from the pushforward (P1's Fobs) vs D^2 * (1/2) sech^2(x)
        Fobs = lambda y: (1 + source_cos(cos_of_xi(y), b)) / 2
        w3 = max(w3, abs(mp.diff(Fobs, x) - D ** 2 * mp.sech(x) ** 2 / 2))
    x1 = mp.findroot(lambda y: D_obs(cos_of_xi(y), b) - 1, eta / 2 + mp.mpf('0.1'))
    w3 = max(w3, abs(x1 - eta / 2), abs(cos_of_xi(x1) - mp.tanh(eta / 2)))
    w3 = max(w3, abs(D_obs(cos_of_xi(mp.mpf(60)), b) - k) / k, abs(D_obs(cos_of_xi(mp.mpf(-60)), b) - 1 / k) * k)
    print(f"  beta={mp.nstr(b,6)}: D=1 at xi'={mp.nstr(x1,15)} (eta/2={mp.nstr(eta/2,15)}), "
          f"theta'={mp.nstr(mp.acos(cos_of_xi(x1))*180/mp.pi,10)} deg; D(+60)/k-1={mp.nstr(D_obs(cos_of_xi(60),b)/k-1,3)}")
print(f"  worst miss {mp.nstr(w3,3)}")
kill('P3', w3 < TOL)

# ---------------- P4 ----------------
print("P4: the Doppler corner is the swap of who counts")
w4 = mp.mpf(0)
rng = np.random.default_rng(22)
worst_z = 0.0
for b in BETAS:
    k = kfac(b); g = 1 / mp.sqrt(1 - b * b)
    lo, hi = 1 / k, k
    # by source: D as a function of the source angle through aberration; CDF by root-finding in cos
    Dsrc = lambda c: D_obs(seen_cos(c, b), b)
    for i in range(21):
        d = lo + (hi - lo) * (mp.mpf(i) + mp.mpf('0.5')) / 21
        c0 = mp.findroot(lambda c: Dsrc(c) - d, (-1, 1), solver='illinois')   # D increasing in c
        Fsrc = (1 + c0) / 2
        w4 = max(w4, abs(Fsrc - (d - lo) / (hi - lo)))
        # by observer address: c' uniform; 1/D = (1 - b c')/sqrt(1-b^2); CDF of 1/D
        cp0 = mp.findroot(lambda cp: 1 / D_obs(cp, b) - d, (-1, 1), solver='illinois')
        Fobs = (1 - cp0) / 2          # 1/D <= d  <=> c' >= cp0
        w4 = max(w4, abs(Fobs - (d - lo) / (hi - lo)))
    msrc = mp.findroot(lambda c: c, 0)          # median source cos = 0
    msrc = Dsrc(msrc)
    mobs = D_obs(mp.mpf(0), b)                  # median address cos' = 0
    blue_src = (1 - mp.findroot(lambda c: Dsrc(c) - 1, (-1, 1), solver='illinois')) / 2
    blue_obs = (1 + mp.findroot(lambda cp: D_obs(cp, b) - 1, (-1, 1), solver='illinois')) / 2
    blue_obs = 1 - blue_obs
    w4 = max(w4, abs(msrc - g), abs(mobs - 1 / g), abs(msrc * mobs - 1),
             abs(blue_src - k / (1 + k)), abs(blue_obs - 1 / (1 + k)), abs(blue_src / blue_obs - k))
    print(f"  beta={mp.nstr(b,6)}: median D by source {mp.nstr(msrc,12)} (gamma {mp.nstr(g,12)}), by address "
          f"{mp.nstr(mobs,12)}; product {mp.nstr(msrc*mobs,15)}; blue by source {mp.nstr(blue_src,12)}, by address {mp.nstr(blue_obs,12)}")
    # seeded sampling, floats
    bf = float(b); kf = float(k); gf = float(g); N = 10 ** 6
    c = rng.uniform(-1, 1, N); cp = (c + bf) / (1 + bf * c)
    Ds = np.sqrt(1 - bf * bf) / (1 - bf * cp)
    cpo = rng.uniform(-1, 1, N); Do = np.sqrt(1 - bf * bf) / (1 - bf * cpo)
    se_med = (kf - 1 / kf) / (2 * np.sqrt(N))
    z1 = abs(np.median(Ds) - gf) / se_med
    # median of D by address: 1/D uniform, median of D = 1/median(1/D); delta method se
    z2 = abs(np.median(1 / Do) - gf) / se_med
    p1 = kf / (1 + kf); p2 = 1 / (1 + kf)
    z3 = abs(np.mean(Ds > 1) - p1) / np.sqrt(p1 * (1 - p1) / N)
    z4 = abs(np.mean(Do > 1) - p2) / np.sqrt(p2 * (1 - p2) / N)
    worst_z = max(worst_z, z1, z2, z3, z4)
    print(f"    sampled: z = {z1:.2f}, {z2:.2f}, {z3:.2f}, {z4:.2f}")
print(f"  worst identity miss {mp.nstr(w4,3)}; worst z {worst_z:.2f}")
kill('P4', w4 < TOL and worst_z < 5)

# ---------------- P5 ----------------
print("P5: the boost read from addresses alone")
N, T = 2000, 400
ok5 = True
for b in BETAS:
    bf = float(b); eta = float(mp.atanh(b)); kf = float(kfac(b))
    em, ea = [], []
    worst_scale = 0.0
    for trial in range(T):
        n = rng.normal(size=(N, 3)); n /= np.linalg.norm(n, axis=1)[:, None]
        r = rng.uniform(0.1, 10, N)
        pos = n * r[:, None]
        ests = []
        for s in (1.0, 1e-3, 1e3):
            p = pos * s
            u = p / np.linalg.norm(p, axis=1)[:, None]
            c = u[:, 2]
            cp = (c + bf) / (1 + bf * c)
            xi = np.arctanh(cp)
            ests.append((np.median(xi), np.mean(xi)))
        worst_scale = max(worst_scale, max(abs(ests[j][i] - ests[0][i]) for j in (1, 2) for i in (0, 1)))
        em.append(ests[0][0] - eta); ea.append(ests[0][1] - eta)
    rm = np.sqrt(np.mean(np.square(em))); ra = np.sqrt(np.mean(np.square(ea)))
    pm, pa = 1 / np.sqrt(N), (np.pi / (2 * np.sqrt(3))) / np.sqrt(N)
    ratio = rm / ra
    # payload: frequency of a source straight ahead, nu' = D(0) nu0; estimate ln(nu'/nu0_assumed)
    nu0 = 5.0e14
    nup = float(D_obs(mp.mpf(1), b)) * nu0
    fmiss = max(abs((np.log(nup / (f * nu0)) - eta) - (-np.log(f))) for f in (1.5, 0.8))
    good = (abs(rm / pm - 1) <= 0.15 and abs(ra / pa - 1) <= 0.15 and 1.0 <= ratio <= 1.2
            and worst_scale <= 1e-12 and fmiss <= 1e-12)
    ok5 = ok5 and good
    print(f"  beta={float(b):.4f}: RMS median {rm:.5f} (pred {pm:.5f}, {rm/pm-1:+.3f}), mean {ra:.5f} "
          f"(pred {pa:.5f}, {ra/pa-1:+.3f}), ratio {ratio:.4f}; scaling moved {worst_scale:.1e}; "
          f"frequency estimate's move vs -ln f off by {fmiss:.1e}")
kill('P5', ok5)

# ---------------- P6 ----------------
print("P6: EMC's mass a stationary point; the Newton/massless hand-over")
w6 = mp.mpf(0)
mp_rng = np.random.default_rng(220)
mc2 = mp.mpf('0.51099895000')
for i in range(21):
    eta, etab, dl = [mp.mpf(float(v)) for v in mp_rng.uniform([-3, -3, 0.01], [3, 3, 2])]
    E, pc = mc2 * mp.cosh(eta), mc2 * mp.sinh(eta)
    def Ep(eb):
        bb = mp.tanh(eb); gb = mp.cosh(eb)
        return gb * (E - bb * pc)
    w6 = max(w6, abs(Ep(etab) - mc2 * mp.cosh(eta - etab)))
    w6 = max(w6, abs(mp.diff(Ep, eta)), abs(Ep(eta) - mc2), abs(Ep(eta + dl) - Ep(eta - dl)))
    if abs(etab - eta) > mp.mpf('0.01'):
        w6 = max(w6, mp.mpf(0) if abs(mp.diff(Ep, etab)) > mp.mpf('1e-3') * mc2 else mp.mpf(1))
eN = lambda x: (1 + x * x / 2) / mp.sqrt(1 + x * x) - 1
eU = lambda x: (x + 1 / (2 * x)) / mp.sqrt(1 + x * x) - 1
roots = set()
for s in [mp.mpf(v) for v in ('0.01', '0.1', '0.5', '2', '10', '100')]:
    try:
        r = mp.findroot(lambda lx: eN(mp.e ** lx) - eU(mp.e ** lx), mp.log(s))
        roots.add(mp.nstr(mp.e ** r, 30))
        w6 = max(w6, abs(mp.e ** r - 1))
    except Exception as ex:
        print("  no root from", s, ex)
print(f"  crossings found: {sorted(roots)}")
a1 = mp.findroot(lambda e: eN(mp.sinh(e)) - eU(mp.sinh(e)), 1)
for Z in [mp.mpf(1) + mp.mpf('0.5'), mp.mpf(3), 2 * mp.asinh(1)]:
    share = a1 / Z
    w6 = max(w6, abs(share - mp.asinh(1) / Z))
    print(f"  rapidity uniform on [0,{mp.nstr(Z,8)}]: Newton better in {mp.nstr(share,15)}")
c1 = mp.findroot(lambda ch: eN(mp.tan(ch)) - eU(mp.tan(ch)), mp.mpf('0.7'))
w6 = max(w6, abs(c1 / (mp.pi / 2) - mp.mpf(1) / 2))
print(f"  chi uniform on [0,pi/2]: Newton better in {mp.nstr(c1/(mp.pi/2),15)}; worst miss {mp.nstr(w6,3)}")
kill('P6', w6 < TOL)

print()
for p in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
    print(p, 'not killed' if verdict[p] else 'KILLED')
