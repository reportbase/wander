"""PXC run 4: working back from parallax's known results. See plans/pxc-plan.md.

Half-baseline a = 1 unless said, a place on the bisector at distance d, k = a/d, gamma the angle the baseline subtends,
p = gamma/2 the parallax. mpmath at 50 digits; derivatives by complex step and Jacobians from the exact intersection,
never from the closed forms tested. Needs mpmath (PyPI, BSD).
"""
import mpmath as mp
mp.mp.dps = 50
def verdict(ok): return "not killed" if ok else "KILLED"
H = mp.mpf('1e-40')
grid = [mp.mpf(2) ** (mp.mpf(j) / 10) for j in range(-300, 301)]          # d from 2^-30 to 2^30
gam = lambda d, a=mp.mpf(1): 2 * mp.atan(a / d)

# ---------------------------------------------------------------- P11: the flip of the pair is the supplement
w11 = max(abs(gam(d) + gam(1 / d) - mp.pi) for d in grid)
print(f"P11 |gamma(d) + gamma(a^2/d) - pi|, d = 2^-30..2^30: worst {mp.nstr(w11, 3)} ->", verdict(w11 <= mp.mpf('1e-40')))

# ---------------------------------------------------------------- P12: K3 is the outer reading gamma/sin gamma
def ratio(p):
    """(sigma_d/d)/(sigma_p/p) = |p * d ln d/dp|, by complex step through d(p) = a/tan p"""
    return abs(p * mp.im(mp.log(1 / mp.tan(mp.mpc(p, H)))) / H)
w12 = mp.mpf(0)
for d in grid:
    g = gam(d); w12 = max(w12, abs(ratio(g / 2) / (g / mp.sin(g)) - 1))
r_corner = ratio(mp.pi / 4)
r_far = ratio(gam(mp.mpf(2) ** 30) / 2)
ok12 = w12 <= mp.mpf('1e-40') and abs(r_corner - mp.pi / 2) <= mp.mpf('1e-40') and abs(r_far - 1) <= mp.mpf('1e-17')
print(f"P12 ratio vs gamma/sin gamma: worst {mp.nstr(w12, 3)}; at the corner {mp.nstr(r_corner, 20)} (pi/2 = {mp.nstr(mp.pi / 2, 20)});"
      f" at k = 2^-30, 1 + {mp.nstr(r_far - 1, 3)} ->", verdict(ok12))
for j in (-10, -2, 0, 1, 2, 4):
    d = mp.mpf(2) ** j; g = gam(1 / d)
    print(f"   k = 2^{j:+d}: gamma {mp.nstr(mp.degrees(g), 8):>10} deg, (sigma_d/d)/(sigma_p/p) = {mp.nstr(ratio(g / 2), 10)}")

# ---------------------------------------------------------------- P13: the round error needs the two standpoints alike
A, B = (mp.mpf(-1), mp.mpf(0)), (mp.mpf(1), mp.mpf(0))
def meet(ta, tb):
    ca, sa, cb, sb = mp.cos(ta), mp.sin(ta), mp.cos(tb), mp.sin(tb)
    s = ((B[0] - A[0]) * (-sb) - (B[1] - A[1]) * (-cb)) / (ca * (-sb) - sa * (-cb))
    return A[0] + s * ca, A[1] + s * sa
def cov(x, y, s1, s2):
    ta, tb = mp.atan2(y - A[1], x - A[0]), mp.atan2(y - B[1], x - B[0])
    c1 = [mp.im(v) / H for v in meet(mp.mpc(ta, H), tb)]
    c2 = [mp.im(v) / H for v in meet(ta, mp.mpc(tb, H))]
    J = mp.matrix([[c1[0] * s1, c2[0] * s2], [c1[1] * s1, c2[1] * s2]])
    return J * J.T
w13, rows13 = mp.mpf(0), []
for r in (1, 2, 4):
    C = cov(mp.mpf(0), mp.mpf(1), mp.mpf(1), mp.mpf(r))
    ev = sorted(mp.re(e) for e in mp.eig(C)[0]); asp = mp.sqrt(ev[1] / ev[0])
    w13 = max(w13, abs(asp / r - 1)); rows13.append((r, asp))
depth = lambda k: mp.sqrt(cov(mp.mpf(0), 1 / k, mp.mpf(1), mp.mpf(4))[1, 1]) * k
lo, hi, gr = mp.mpf('0.2'), mp.mpf('5'), (mp.sqrt(5) - 1) / 2
for _ in range(160):
    x1, x2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
    (lo, hi) = (lo, x2) if depth(x1) < depth(x2) else (x1, hi)
kmin = (lo + hi) / 2
ok13 = w13 <= mp.mpf('1e-12') and abs(kmin - 1) <= mp.mpf('1e-9')
print(f"P13 the aspect at the corner vs sigma2/sigma1: {', '.join(f'{r}: {mp.nstr(a, 12)}' for r, a in rows13)};"
      f" the depth least at k = {mp.nstr(kmin, 15)} with sigma2/sigma1 = 4 ->", verdict(ok13))

# ---------------------------------------------------------------- P14: past the band the flip leaves no mean
phi_n = lambda p, p0, s: mp.exp(-(p - p0) ** 2 / (2 * s * s)) / (s * mp.sqrt(2 * mp.pi))
Phi = lambda z: mp.ncdf(z)
w14a = w14b = mp.mpf(0); rows14 = []
for rel in ('0.2', '0.5', '1'):
    p0, s = mp.mpf(1), mp.mpf(rel)
    target = phi_n(0, p0, s) * mp.log(10)
    for e in range(10, 20):
        x = mp.mpf(10) ** (-e)
        inc = mp.quad(lambda p: phi_n(p, p0, s) / p, [x / 10, x])
        w14a = max(w14a, abs(inc / target - 1))
    pos = 1 - Phi(-p0 / s)                                                        # the share of positive readings
    m_plus = mp.findroot(lambda q: (Phi((q - p0) / s) - Phi(-p0 / s)) / pos - mp.mpf(1) / 2, p0)
    # the distance's law over positive readings, from its own density, then its median by root-finding
    fD = lambda t: phi_n(1 / t, p0, s) / t ** 2 / pos
    tail = lambda t: mp.quad(fD, [t, 10 * t, mp.inf])
    t_med = mp.findroot(lambda t: tail(t) - mp.mpf(1) / 2, 1 / m_plus)
    w14b = max(w14b, abs(t_med - 1 / m_plus))
    rows14.append((rel, Phi(-p0 / s), m_plus, t_med))
ok14 = w14a <= mp.mpf('1e-6') and w14b <= mp.mpf('1e-25')
print(f"P14 per-decade growth of the expected distance vs phi(0) ln 10: worst {mp.nstr(w14a, 3)}; median of a/p over positive"
      f" readings vs a/median: worst {mp.nstr(w14b, 3)} ->", verdict(ok14))
for rel, neg, mp_, tm in rows14:
    print(f"   sigma/p0 = {rel}: share at or below zero {mp.nstr(neg, 6)}; median positive reading {mp.nstr(mp_, 10)};"
          f" median distance {mp.nstr(tm, 10)} (a/p0 = 1)")
print(f"   K4's 20% lies log2(5) = {mp.nstr(mp.log(5, 2), 6)} levels inside the band's far edge")

# ---------------------------------------------------------------- P15: the parsec is defined in the far field
au = mp.mpf(149597870700); eps = mp.pi / (180 * 3600)
diff = au * (1 / eps - 1 / mp.tan(eps)); approx = au * eps / 3
lev = mp.log(1 / mp.tan(eps), 2)
ok15 = abs(diff / approx - 1) <= mp.mpf('1e-9') and abs(lev - mp.mpf('17.654')) <= mp.mpf('1e-3')
print(f"P15 IAU parsec - tangent parsec = {mp.nstr(diff, 10)} m (a*eps/3 = {mp.nstr(approx, 10)} m); 1 pc lies"
      f" {mp.nstr(lev, 8)} levels past the corner ->", verdict(ok15))
