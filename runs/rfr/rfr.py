"""RFR run 1: REF revisited. See plans/rfr-plan.md (predictions written before this script).
Exact arithmetic (mpmath, 40 digits). Run from the repository root: python3 runs/rfr/rfr.py
"""
import re, random
import mpmath as mp
mp.mp.dps = 40
pi = mp.pi
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)
def f(x, n=12): return mp.nstr(x, n)

# ---------------- P1: the corner sphere is a0; depth a reading ----------------
rnd = random.Random(20261022)
a0 = mp.mpf('0.31')
terms = [(l, m, mp.mpf(rnd.uniform(-1, 1)) * mp.mpf(0.05) / l, rnd.random() < .5)
         for l in range(1, 7) for m in range(0, l + 1)]
def lnr(mu, ph):
    s = a0
    for l, m, c, sn in terms:
        s += c * mp.legenp(l, m, mu) * (mp.sin(m * ph) if (sn and m) else mp.cos(m * ph))
    return s
NM, NP = 12, 16                        # GL in mu exact to degree 23, trapezoid in azimuth exact to |m| < 16
xs, ws = zip(*[(mp.mpf(x), mp.mpf(w)) for x, w in
               zip(*[list(v) for v in __import__('numpy').polynomial.legendre.leggauss(NM)])])
# refine the nodes to 40 digits by Newton on P_NM
xs = [mp.findroot(lambda t: mp.legendre(NM, t), x) for x in xs]
ws = [2 / ((1 - x * x) * mp.diff(lambda t: mp.legendre(NM, t), x) ** 2) for x in xs]
pts = [(x, w, 2 * pi * j / NP) for x, w in zip(xs, ws) for j in range(NP)]
L = {(x, ph): lnr(x, ph) for x, w, ph in pts}
meanln = sum(w * L[(x, ph)] for x, w, ph in pts) / (2 * NP)
gm = mp.e ** meanln
e1a = abs(gm - mp.e ** a0) / mp.e ** a0
worst_depth, worst_rbar = mp.mpf(0), mp.mpf(0)
for k in [mp.mpf('1e-3'), mp.mpf(7), mp.mpf('1e6')]:
    meank = sum(w * (L[(x, ph)] + mp.log(k)) for x, w, ph in pts) / (2 * NP)
    rbark = mp.e ** meank
    worst_rbar = max(worst_rbar, abs(rbark / (k * gm) - 1))
    for x, w, ph in pts:
        d0 = (L[(x, ph)] - meanln) / mp.log(2)
        dk = (mp.log(k * mp.e ** L[(x, ph)]) - meank) / mp.log(2)
        worst_depth = max(worst_depth, abs(dk - d0))
p1 = e1a < mp.mpf('1e-30') and worst_depth < mp.mpf('1e-30') and worst_rbar < mp.mpf('1e-30')
say(f"P1: {'not killed' if p1 else 'KILLED'}. geometric mean over uniform directions vs exp(a0): rel {f(e1a,3)}; "
    f"depth change under k = 1e-3, 7, 1e6: {f(worst_depth,3)} levels; rbar/(k*rbar0) - 1: {f(worst_rbar,3)}. "
    f"({len(terms)} terms, degrees 1-6, {len(pts)} nodes)")

# ---------------- P2: the corner sphere is not the median sphere ----------------
BODIES = [('Earth', '6378.1', '6356.8', 'rocky'), ('Mars', '3396.2', '3376.2', 'rocky'), ('Moon', '1738.1', '1736.0', 'rocky'),
          ('Jupiter', '71492', '66854', 'giant'), ('Saturn', '60268', '54364', 'giant')]
p2 = True
for name, A, C, kind in BODIES:
    a, c = mp.mpf(A), mp.mpf(C)
    q = a * a / (c * c) - 1
    r = lambda mu: a / mp.sqrt(1 + q * mu * mu)
    lng = mp.quad(lambda mu: mp.log(r(mu)), [0, 1])          # mean of ln r over mu uniform on [-1, 1] (even)
    # the law of r: P(r <= x) = 1 - mu(x), mu(x) = sqrt((a^2/x^2 - 1)/q); bisect for 1/2 on x
    lo, hi = c, a
    for _ in range(200):
        mid = (lo + hi) / 2
        mux = mp.sqrt(max(a * a / (mid * mid) - 1, 0) / q)
        if 1 - mux > mp.mpf(1) / 2: hi = mid
        else: lo = mid
    rmed = (lo + hi) / 2
    mumed = mp.sqrt((a * a / (rmed * rmed) - 1) / q)
    Lf = mp.log(a / c, 2)
    dL = (mp.log(rmed) - lng) / mp.log(2)
    ratio = dL / Lf
    band = (mp.mpf('0.99'), mp.mpf(1)) if kind == 'rocky' else (mp.mpf('0.88'), mp.mpf('0.99'))
    ok = abs(mumed - mp.mpf(1) / 2) < mp.mpf('1e-25') and band[0] <= ratio <= band[1]
    p2 = p2 and ok
    say(f"  {name}: L = log2(a/c) {f(Lf,6)}; median at mu {f(mumed,30)}; median sphere above the geometric-mean sphere by "
        f"{f(dL,6)} levels; dL/L {f(ratio,6)} (band {band[0]}-{band[1]}){'' if ok else '  <-- outside'}; "
        f"arithmetic mean above geometric by {f((mp.log(mp.quad(r,[0,1])) - lng)/mp.log(2),4)} levels")
say(f"P2: {'not killed' if p2 else 'KILLED'}. the median sphere at latitude 30 deg (mu = 1/2) on every spheroid; the corner "
    f"sphere (geometric mean, a0) below it by about L/12")

# ---------------- P3: one octave per level of altitude at the foot ----------------
R = mp.mpf(1); eps = mp.mpf('1e-6')
def phi_of(t, d):          # central angle of the first hit of a ray t off nadir from distance d
    s = d * mp.cos(t) - mp.sqrt(R * R - d * d * mp.sin(t) ** 2)
    return mp.atan2(s * mp.sin(t), d - s * mp.cos(t))
p3 = True; rows = []
for aR in ['1e-3', '1e-1', '1', '10', '1e3']:
    a = mp.mpf(aR); d = R + a
    ratio = R * phi_of(eps, d) / (a * eps)
    rows.append(f"a/R {aR}: footprint/(a eps) - 1 = {f(ratio - 1, 3)}")
    p3 = p3 and abs(ratio - 1) < mp.mpf('1e-5')
alpha = lambda a: mp.asin(R / (R + a))
rate = lambda a: mp.diff(lambda la: mp.log(alpha(mp.e ** la)), mp.log(a)) / 1   # d ln alpha / d ln a = d log2 / d log2
r1 = rate(mp.mpf(1)); r1000 = rate(mp.mpf(1000))
disc_over_foot = alpha(mp.mpf(1)) * 1 / R          # (pi alpha/eps)/(pi R/(a eps)) at a = R
p3 = p3 and abs(r1 + mp.sqrt(3) / pi) < mp.mpf('1e-20') and abs(disc_over_foot - pi / 6) < mp.mpf('1e-30') and abs(r1000 + 1) < mp.mpf('0.002')
say("  " + "; ".join(rows))
say(f"  disc rule (run 2): octaves per level of altitude at a = R {f(r1,12)} (-sqrt3/pi = {f(-mp.sqrt(3)/pi,12)}); "
    f"at a = 1000R {f(r1000,8)}; l_disc/l* at a = R {f(disc_over_foot,10)} (pi/6)")
for aR in ['1e-3', '1e-2', '0.1', '1', '10', '100']:
    a = mp.mpf(aR)
    say(f"    a/R {aR:>5}: l_disc/l* = {f(alpha(a) * a / R, 6)}, disc rule octaves per level of altitude {f(rate(a), 6)}, "
        f"per level of distance d {f(rate(a) * (R + a) / a, 6)}")
say(f"P3: {'not killed' if p3 else 'KILLED'}. the foot's held degree l* = pi R/(a eps) halves exactly per level of altitude, "
    f"through a = R; run 2's disc rule is its far-field form")

# ---------------- P4: the Cauchy's height cut ----------------
p4 = True
worst_a = mp.mpf(0)
for l, a in [(8, mp.mpf('0.3')), (100, mp.mpf('1e-3')), (3, mp.mpf(2))]:
    worst_a = max(worst_a, abs(mp.e ** (-l * a / R) - mp.e ** (-(2 * l) * (a / 2) / R)))
p4 = p4 and worst_a < mp.mpf('1e-30')
worst_b = mp.mpf(0)
for dR in ['1.5', '3', '10']:
    d = mp.mpf(dR)
    P = lambda ph: (d * d - R * R) / (2 * pi * (d * d - 2 * d * R * mp.cos(ph) + R * R))
    for n in range(1, 9):
        cn = 2 * mp.quad(lambda ph: P(ph) * mp.cos(n * ph), mp.linspace(0, 2 * pi, 9))
        worst_b = max(worst_b, abs(cn - (R / d) ** n))
p4 = p4 and worst_b < mp.mpf('1e-20')
mv = lambda aR: mp.log(mp.log(1 + 2 * aR) / mp.log(1 + aR), 2)
vals = {aR: mv(mp.mpf(aR)) for aR in ['1e-4', '1e-2', '0.05', '0.1', '0.25', '1', '10', '100', '1e4']}
p4 = p4 and all(vals[x] >= mp.mpf('0.93') for x in ['1e-4', '1e-2', '0.05', '0.1']) \
     and abs(vals['1'] - mp.log(mp.log(3, 2), 2)) < mp.mpf('1e-30') and abs(vals['1'] - mp.mpf('0.6644')) < mp.mpf('1e-4') \
     and vals['100'] < mp.mpf('0.25')
K = 512; epsK = pi / (2 * K)
gap = [(pi * R / (a * epsK)) / (R / a) for a in [mp.mpf('1e-3'), mp.mpf(1), mp.mpf(50)]]
p4 = p4 and all(abs(g - 2 * K) < mp.mpf('1e-30') for g in gap)
say(f"  (a) planar e^(-la/R) at (l, a) vs (2l, a/2): {f(worst_a,3)}; (b) exterior Poisson coefficients vs (R/d)^n, n 1-8, "
    f"d/R 1.5, 3, 10: {f(worst_b,3)}; (c) K-address cut over planar cut at K = 512: {f(gap[0],10)} = 2K, log2 {f(mp.log(gap[0],2),6)} octaves")
say("  world's own Cauchy, octaves its 1/e cut moves per level of altitude: " +
    ", ".join(f"a/R {k} {f(v,5)}" for k, v in vals.items()))
say(f"P4: {'not killed' if p4 else 'KILLED'}. one octave per level from the height only on the plane; the world's own Cauchy "
    f"drops {f(vals['1'],5)} at a = R and {f(vals['100'],4)} at a = 100R")

# ---------------- P5: rho_k is the payload's ----------------
p5 = True; worst5 = mp.mpf(0)
for dR in ['1.01', str(mp.sqrt(2)), '2', '10', '1000']:
    d = mp.mpf(dR); ell = mp.sqrt(d * d - R * R)
    for k in range(3, 10):
        for hR in ['1e-5', '1e-4']:
            h = mp.mpf(hR)
            e = pi * R / (2 ** (k + 1) * ell)
            shift = (mp.asin((R + h) / d) - mp.asin(R / d)) / e
            rho = h * 2 ** (k + 1) / (pi * R)
            worst5 = max(worst5, abs(shift / rho - 1))
p5 = worst5 < mp.mpf('1e-3')
say(f"P5: {'not killed' if p5 else 'KILLED'}. outline shift at first hold over run 2's rho, worst |ratio - 1| over "
    f"d/R 1.01..1000, k 3..9, h/R 1e-5, 1e-4: {f(worst5,3)}; so rho_k = 2 RMS_k/lambda_k, free of d and K")
# bookkeeping: run 2's printed rho from its printed RMS
txt = open('plans/ref/ref-run2.txt').read()
worstbk = 0.0; n = 0
for block in re.split(r'\n(?=\S)', txt):
    mR = re.search(r'R ([\d.]+) km', block)
    if not mR: continue
    Rk = float(mR.group(1)) * 1000
    for k, rms, rho in re.findall(r'k (\d) \[.*?RMS\s+([\d.]+) m.*?rho ([\d.]+)', block):
        lam = 2 * 3.141592653589793 * Rk / 2 ** (int(k) + 1)
        worstbk = max(worstbk, abs(2 * float(rms) / lam - float(rho))); n += 1
say(f"  bookkeeping: run 2's printed rho = 2 RMS/lambda for {n} octaves, worst difference {worstbk:.5f} (printed to 0.0001)")

open('runs/rfr/rfr-run1.txt', 'w').write('\n'.join(out) + '\n')
