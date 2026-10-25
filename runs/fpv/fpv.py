"""FPV run 1: the corner on the crosshair in a first-person view (plans/fpv-plan.md).
Run from the repository's root: python3 runs/fpv/fpv.py"""
import numpy as np
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 50
pi = mp.pi
n0, X0 = mp.mpf(1), mp.mpf(10) ** 7
verdicts = {}


def say(code, ok, note=""):
    verdicts[code] = verdicts.get(code, True) and ok
    print(f"  {'ok  ' if ok else 'FAIL'} {code}: {note}")


def rel(a, b):
    return (b - a) / mp.sqrt(a * b)


# the three schemes: the cell [a, b] that holds d
def T_cell(d, f, K):
    k = int(mp.floor(K * (2 / pi) * mp.atan(d / f)))
    a = f * mp.tan(k * pi / (2 * K))
    b = f * mp.tan((k + 1) * pi / (2 * K)) if k + 1 < K else mp.inf
    return a, b


def LOG_cell(d, n, X, K):
    k = int(mp.floor(K * mp.log(d / n) / mp.log(X / n)))
    return n * (X / n) ** (mp.mpf(k) / K), n * (X / n) ** (mp.mpf(k + 1) / K)


def Z_cell(d, n, X, K):
    span = 1 / n - 1 / X
    k = int(mp.floor(K * (1 / n - 1 / d) / span))
    return 1 / (1 / n - k * span / K), 1 / (1 / n - (k + 1) * span / K)


rT = lambda d, f, K: rel(*T_cell(d, f, K))
rL = lambda d, n, X, K: rel(*LOG_cell(d, n, X, K))
rZ = lambda d, n, X, K: rel(*Z_cell(d, n, X, K))
fm = mp.sqrt(n0 * X0)

print("G1, the focus grain is range-free")
for K in (256, 1024, 4096):
    t = mp.tan(pi / 4 - pi / (2 * K))
    r0 = rel(t, mp.mpf(1))
    say("G1", abs(r0 / (pi / K) - 1) < mp.mpf('0.001'), f"K = {K}: cell below the focus r = {mp.nstr(r0, 8)}, pi/K = {mp.nstr(pi / K, 8)}, off {mp.nstr(r0 / (pi / K) - 1, 3)}")
K = 1024
rs = [rel(f * mp.tan(pi / 4 - pi / (2 * K)), f) for f in (mp.mpf(1), mp.mpf(10) ** mp.mpf('3.5'), mp.mpf(10) ** 6, mp.mpf(37))]
say("G1", max(rs) - min(rs) < mp.mpf(10) ** -40, f"the same at f = 1, 10^3.5, 10^6, 37 (spread {mp.nstr(max(rs) - min(rs), 3)}); no n or X enters")
rTf = rs[0]
for (n, X) in ((n0, X0), (n0, mp.mpf(1000))):
    lg = rL(fm if X == X0 else mp.sqrt(n * X), n, X, K)
    ratio = lg / rTf
    say("G1", abs(ratio / (mp.log(X / n) / pi) - 1) < mp.mpf('0.01'), f"X/n = {mp.nstr(X / n, 3)}: LOG/T at the focus {mp.nstr(ratio, 5)}, ln(X/n)/pi {mp.nstr(mp.log(X / n) / pi, 5)}")
for f in (mp.mpf(1), mp.mpf(3), mp.mpf(4), mp.mpf(100), fm):
    z = rZ(f * (1 + mp.mpf(10) ** -30), n0, X0, K)
    print(f"      f = {mp.nstr(f, 5)}: Z {mp.nstr(z, 5)} against T {mp.nstr(rTf, 5)}  ({'T finer' if rTf < z else 'Z finer'}; Z/T {mp.nstr(z / rTf, 4)})")
zf = lambda f: rZ(f * (1 + mp.mpf(10) ** -30), n0, X0, K)
say("G1", zf(4) > rTf and zf(100) > rTf and zf(fm) > rTf and zf(3) < rTf and zf(1) < rTf,
    f"T finer than Z at the focus for f >= 4, Z finer for f <= 3; at f = n Z is {mp.nstr(rTf / zf(1), 4)} times finer")

print("\nG2, both sides alike")
f = fm
edges = [f * mp.tan(k * pi / (2 * K)) for k in range(1, K)]
worst = max(abs(f * f / edges[k - 1] - edges[K - k - 1]) / edges[K - k - 1] for k in range(1, K))
say("G2", worst < mp.mpf(10) ** -40, f"every edge's mirror f^2/d is an edge (worst {mp.nstr(worst, 3)})")
xs = [mp.mpf(x) / 4 for x in range(1, 25)]
asym = max(abs(rT(f * mp.e ** x, f, K) - rT(f * mp.e ** -x, f, K)) / rT(f * mp.e ** x, f, K) for x in xs)
say("G2", asym < mp.mpf(10) ** -35, f"r(f e^x) = r(f e^-x) for x = 0.25 ... 6 (worst {mp.nstr(asym, 3)})")
bad = []
for x in xs:
    got, want = rT(f * mp.e ** x, f, K), (pi / K) * mp.cosh(x)
    if abs(got / want - 1) > mp.mpf('0.01'):
        bad.append((x, got / want - 1))
say("G2", not bad, "continuum (pi/K) cosh x within 1% for |x| <= 6" + ("" if not bad else f"; off at x = " + ", ".join(f"{mp.nstr(x, 3)} ({mp.nstr(e, 3)})" for x, e in bad)))
for x in (1, 3, 5, 5.5, 6):
    x = mp.mpf(x); a, b = T_cell(f * mp.e ** x, f, K)
    print(f"      x = {mp.nstr(x, 3)}: cell r {mp.nstr(rel(a, b), 5)}, (pi/K)cosh x {mp.nstr((pi / K) * mp.cosh(x), 5)}, cell spans {mp.nstr(mp.log(b / a), 4)} nats")
zs = [rZ(mp.mpf(10) ** (mp.mpf(j) / 4), n0, X0, K) for j in range(1, 28)]
lgs = [rL(mp.mpf(10) ** (mp.mpf(j) / 4), n0, X0, K) for j in range(1, 28)]
say("G2", all(zs[i] < zs[i + 1] for i in range(len(zs) - 1)) and max(lgs) - min(lgs) < mp.mpf(10) ** -40,
    f"Z rises with d everywhere (strictly; it never falls: {all(zs[i] <= zs[i + 1] for i in range(len(zs) - 1))}, {sum(1 for i in range(len(zs) - 1) if zs[i] == zs[i + 1])} of {len(zs) - 1} steps share a cell); LOG constant")

print("\nG3, the band where the turn wins (X/n = 1e7, f = sqrt(nX), K = 1024)")
lgc = rL(fm, n0, X0, K)
xf = mp.acosh(mp.log(X0 / n0) / pi)
k0 = K // 2
k = k0
while True:
    a, b = f * mp.tan(k * pi / (2 * K)), f * mp.tan((k + 1) * pi / (2 * K))
    if rel(a, b) > lgc:
        break
    k += 1
x_edge, cellw = mp.log(a / f), mp.log(b / a)
say("G3", abs(x_edge - xf) <= cellw, f"T first coarser than LOG at x = {mp.nstr(x_edge, 6)} (cell from there {mp.nstr(cellw, 3)} nats); formula acosh(ln(X/n)/pi) = {mp.nstr(xf, 6)} = {mp.nstr(xf / mp.log(2), 4)} doublings")
k = k0 - 1
while True:
    a, b = f * mp.tan(k * pi / (2 * K)), f * mp.tan((k + 1) * pi / (2 * K))
    if rel(a, b) > lgc:
        break
    k -= 1
x_lo, cellw = mp.log(b / f), mp.log(b / a)
say("G3", abs(x_lo + xf) <= cellw, f"below the focus at x = {mp.nstr(x_lo, 6)}; the band {mp.nstr((x_edge - x_lo) / mp.log(2), 4)} doublings of the scene's {mp.nstr(mp.log(X0 / n0) / mp.log(2), 4)}")

print("\nG4, the next look")
target = mp.log(X0 / n0) / pi
Ls = mp.findroot(lambda L: mp.sinh(L) / L - target, 3.6)
say("G4", mp.mpf('3.5') <= Ls <= mp.mpf('3.7'), f"L* = {mp.nstr(Ls, 6)} nats = {mp.nstr(Ls / mp.log(2), 4)} doublings each side")


def disc_mean(L, H):
    # mean over x uniform in [-L, L] of the discrete r of T(H) at d = f e^x: exact, cell by cell
    lo, hi = f * mp.e ** -L, f * mp.e ** L
    k = int(mp.floor(K * (2 / pi) * mp.atan(lo / H)))
    tot = 0
    while True:
        a = H * mp.tan(k * pi / (2 * K)); b = H * mp.tan((k + 1) * pi / (2 * K))
        s, e = max(a, lo), min(b, hi)
        if e > s:
            tot += rel(a, b) * mp.log(e / s)
        if b >= hi:
            break
        k += 1
    return tot / (2 * L)


for L in (mp.mpf(1), mp.mpf(2), Ls):
    dm, want = disc_mean(L, f), (pi / K) * mp.sinh(L) / L
    say("G4", abs(dm / want - 1) < mp.mpf('0.01'), f"L = {mp.nstr(L, 4)}: discrete mean {mp.nstr(dm, 6)}, (pi/K) sinh L/L {mp.nstr(want, 6)}, LOG {mp.nstr(lgc, 6)}")
cont = lambda h, L: mp.quad(lambda x: mp.cosh(x - h), [-L, h, L]) / (2 * L)
hbest = mp.findroot(lambda h: mp.diff(lambda u: cont(u, Ls), h), mp.mpf('0.3'))
say("G4", abs(hbest) < mp.mpf(10) ** -6, f"the least mean at H = f e^{mp.nstr(hbest, 3)} (the spread's middle)")
dm0 = disc_mean(Ls, f)
side = [disc_mean(Ls, f * mp.e ** h) for h in (mp.mpf('-0.05'), mp.mpf('0.05'))]
print(f"      discrete: H moved 0.05 nats either way raises the mean by {mp.nstr(side[0] / dm0 - 1, 3)}, {mp.nstr(side[1] / dm0 - 1, 3)}")

print("\nG5, refocusing changes the grain only")
ds = [mp.mpf(v) for v in ('3.7', '41', '600', '22000')]
cr = lambda s: ((s[2] - s[0]) * (s[3] - s[1])) / ((s[2] - s[1]) * (s[3] - s[0]))
for f1, f2 in ((mp.mpf(10), mp.mpf(5000)), (mp.mpf('0.3'), mp.mpf(10) ** 6)):
    s1, s2 = [d / f1 for d in ds], [d / f2 for d in ds]
    lv = max(abs((mp.log(s1[i + 1]) - mp.log(s1[i])) - (mp.log(s2[i + 1]) - mp.log(s2[i]))) for i in range(3))
    say("G5", abs(cr(s1) - cr(s2)) < mp.mpf(10) ** -40 and lv < mp.mpf(10) ** -40 and sorted(s2) == s2,
        f"f {mp.nstr(f1, 3)} -> {mp.nstr(f2, 3)}: a slide of {mp.nstr(mp.log(f1 / f2), 5)} nats; cross ratio {mp.nstr(cr(s1), 8)} both; level differences kept")
for d1, d2 in ((mp.mpf(2), mp.mpf(50)), (mp.mpf(100), mp.mpf(10) ** 5)):
    cnt = lambda lf: K * (2 / pi) * (mp.atan(d2 / mp.e ** lf) - mp.atan(d1 / mp.e ** lf))
    lbest = mp.findroot(lambda u: mp.diff(cnt, u), mp.log(d1 * 3))
    r = d2 / d1
    peak = (2 * K / pi) * mp.asin((r - 1) / (r + 1))
    fb = mp.e ** lbest
    disc = sum(1 for k in range(1, K) if d1 < fb * mp.tan(k * pi / (2 * K)) < d2)
    say("G5", abs(lbest - mp.log(mp.sqrt(d1 * d2))) < mp.mpf(10) ** -6 and abs(cnt(lbest) - peak) < mp.mpf(10) ** -30 and abs(disc - peak) <= 1,
        f"pair {mp.nstr(d1, 3)}, {mp.nstr(d2, 3)}: most addresses between at f = {mp.nstr(fb, 8)} (sqrt {mp.nstr(mp.sqrt(d1 * d2), 8)}), {mp.nstr(peak, 7)} = (2K/pi) asin((r-1)/(r+1)); discrete edges {disc}")

print("\nG6, what the turn wastes (n = 1, X = 1e7, K = 1024)")


def waste(f):
    before = sum(1 for k in range(K) if f * mp.tan((k + 1) * pi / (2 * K)) <= n0)
    after = sum(1 for k in range(K) if f * mp.tan(k * pi / (2 * K)) >= X0)
    form = K * ((2 / pi) * mp.atan(n0 / f) + 1 - (2 / pi) * mp.atan(X0 / f))
    return before + after, form


ok6 = True
for f in (mp.mpf(1), mp.mpf(64), fm, X0 / 64, X0):
    w, form = waste(f)
    ok6 &= abs(w - form) <= 1
    print(f"      f = {mp.nstr(f, 6)}: {w} of {K} wholly outside [n, X] ({mp.nstr(mp.mpf(w) / K, 4)}); formula {mp.nstr(form / K, 4)}")
grid = [mp.mpf(64) * (X0 / 64 / 64) ** (mp.mpf(j) / 40) for j in range(41)]
mx = max(mp.mpf(waste(g)[0]) / K for g in grid)
say("G6", ok6, "the discrete waste within one address of the formula")
say("G6", mx < mp.mpf('0.02'), f"under 2% for every f in [64n, X/64] (most {mp.nstr(mx, 4)}); about 4e-4 at sqrt(nX), about 1/2 at n and X")
w_mid = waste(fm)[0] / K; w_n = waste(n0)[0] / K
say("G6", abs(waste(fm)[0] - waste(fm)[1]) <= 1, f"at sqrt(nX): {waste(fm)[0]} address(es), the formula {mp.nstr(waste(fm)[1], 3)} (about 4e-4 of K), within one address")
say("G6", abs(mp.mpf(waste(n0)[0]) / K - mp.mpf('0.5')) < mp.mpf('0.01') and abs(mp.mpf(waste(X0)[0]) / K - mp.mpf('0.5')) < mp.mpf('0.01'), "at n and at X")

print("\nG7, the same 32 bits (f = sqrt(nX))")
K32 = 2 ** 32


def rz32(d):
    w0 = np.float32(float(n0 / d)); w1 = np.nextafter(w0, np.float32(0))
    q0, q1 = Fraction(float(w0)), Fraction(float(w1))
    d0, d1 = n0 / (mp.mpf(q0.numerator) / q0.denominator), n0 / (mp.mpf(q1.numerator) / q1.denominator)
    return (d1 - d0) / d0


for x in (0, 5, -5, 6, -6):
    d = f * mp.e ** x * (1 + mp.mpf(10) ** -30)
    t, z = rT(d, f, K32), rz32(d)
    print(f"      x = {x:+d}: T32 {mp.nstr(t, 5)}, RZ32 {mp.nstr(z, 5)}, RZ/T {mp.nstr(z / t, 5)}")
t0 = rT(f * (1 + mp.mpf(10) ** -30), f, K32); z0 = rz32(f * (1 + mp.mpf(10) ** -30))
say("G7", 82 <= z0 / t0 <= 164 and abs(t0 / (pi / K32) - 1) < mp.mpf(10) ** -6, f"at the focus T32 {mp.nstr(t0, 5)} (pi/2^32 {mp.nstr(pi / K32, 5)}), RZ32/T32 = {mp.nstr(z0 / t0, 5)}")
for lim, name in ((mp.mpf(2) ** -24, "2^-24"), (mp.mpf(2) ** -23, "2^-23")):
    xc = mp.acosh(lim * K32 / pi)
    ok = all(rT(f * mp.e ** (sg * (xc - mp.mpf('0.05'))), f, K32) < lim < rT(f * mp.e ** (sg * (xc + mp.mpf('0.05'))), f, K32) for sg in (1, -1))
    say("G7", ok, f"T32 crosses {name} at |x| = {mp.nstr(xc, 5)} nats ({mp.nstr(xc / mp.log(2), 4)} doublings), within 0.05 either side")

print("\nG8, the crosshair in direction (K = 1024 pixels)")
for deg in (90, 120):
    al = mp.radians(deg) / 2
    edges = [mp.atan(mp.tan(al) * (-1 + mp.mpf(2 * i) / K)) for i in range(K + 1)]
    px = [edges[i + 1] - edges[i] for i in range(K)]
    c, e = px[K // 2], px[-1]
    eq = 2 * al / K
    ok = abs((c / eq) / (mp.tan(al) / al) - 1) < mp.mpf('0.005') and abs((e / c) / mp.cos(al) ** 2 - 1) < mp.mpf('0.005')
    say("G8", ok, f"{deg} deg: flat screen at the crosshair {mp.nstr(c / eq, 5)} x equal-angle (tan a/a {mp.nstr(mp.tan(al) / al, 5)}); edge/crosshair {mp.nstr(e / c, 5)} (cos^2 a {mp.nstr(mp.cos(al) ** 2, 4)})")

print("\nVerdicts:")
for k in sorted(verdicts):
    print(f"  {k}: {'not killed' if verdicts[k] else 'KILLED'}")
