"""HKO: H kicks off the chain. See plans/hko-plan.md (P1-P4).

H > 0 is the value the reader chooses to start the system (SPN R226); an amount x is read against it as s = x/H and laid
by the reader's lay L(s) (s to the corner, 1 + ln s past it) or the in-place lay I(s) (s, then 2 - 1/s). Directions are
read the same at every H; H enters only where amounts are placed. mpmath at 60 digits: derivatives, root-finding and
search, never the closed forms being tested.
Run: python3 runs/hko/hko.py   (a few seconds; needs mpmath)
"""
import mpmath as mp
mp.mp.dps = 60
def verdict(ok): return "not killed" if ok else "KILLED"
M = mp.mpf
L = lambda s: s if s <= 1 else 1 + mp.log(s)               # the reader's lay
I = lambda s: s if s <= 1 else 2 - 1 / s                   # the in-place lay
lay = {"reader": L, "inplace": I}

# ---------------------------------------------------------------- P1: the two limits of H are the corner-free rulers
windows = [(M(1), M(10)), (M('1e-3'), M('1e3')), (M(2), M('2.5'))]
def normalized(f, H, a, b):
    lo, hi = f(a / H), f(b / H)
    return lambda x: (f(x / H) - lo) / (hi - lo)
rulers = {"number line": lambda x, a, b: (x - a) / (b - a),
          "logarithm": lambda x, a, b: mp.log(x / a) / mp.log(b / a),
          "reciprocal": lambda x, a, b: (1 / a - 1 / x) / (1 / a - 1 / b)}
def pts(a, b, k=50):
    return [a * (b / a) ** (M(i) / (k - 1)) for i in range(k)]
w1, near1 = M(0), []
for a, b in windows:
    for H in (b, 10 * b, M('1e6') * b):                      # H at or past the window's top: proportional
        for name in lay:
            g = normalized(lay[name], H, a, b)
            w1 = max(w1, max(abs(g(x) - rulers["number line"](x, a, b)) for x in pts(a, b)))
    for H in (a, a / 10, a / M('1e6')):                      # H at or below its bottom: log, or reciprocal in place
        for name, ruler in (("reader", "logarithm"), ("inplace", "reciprocal")):
            g = normalized(lay[name], H, a, b)
            w1 = max(w1, max(abs(g(x) - rulers[ruler](x, a, b)) for x in pts(a, b)))
    H = mp.sqrt(a * b)                                        # the corner inside the window
    for name in lay:
        g = normalized(lay[name], H, a, b)
        near1.append(min(max(abs(g(x) - r(x, a, b)) for x in pts(a, b)) for r in rulers.values()))
# the corner is where the form changes: one-sided second derivatives
jump_at, jump_off = [], M(0)
for a, b in windows:
    H = mp.sqrt(a * b)
    for name in lay:
        f = lambda x: lay[name](x / H)
        l2, r2 = mp.diff(f, H, 2, direction=-1), mp.diff(f, H, 2, direction=1)
        jump_at.append(abs(l2 - r2) / max(abs(l2), abs(r2)))
        for x in pts(a, b, 22)[1:-1]:
            if abs(x / H - 1) < M('0.01'): continue
            jump_off = max(jump_off, abs(mp.diff(f, x, 2, direction=-1) - mp.diff(f, x, 2, direction=1)))
ok1 = w1 <= M('1e-30') and min(near1) > M('1e-3') and min(jump_at) >= M('1e-6') and jump_off <= M('1e-25')
print(f"P1 limits: lays vs their rulers past the window's ends, worst {mp.nstr(w1, 3)}; with the corner inside, nearest any"
      f" ruler {mp.nstr(min(near1), 4)}; the form's jump at x = H at least {mp.nstr(min(jump_at), 3)}, elsewhere at most"
      f" {mp.nstr(jump_off, 3)} ->", verdict(ok1))

# ---------------------------------------------------------------- P2: lost three ways under a finite count
world = [M(10) ** (M(k) / 5) for k in range(-15, 16)]
a, b, n, Lmax = world[0], world[-1], 32, 12
def held(H, name):
    if name == "reader":
        return len({int(mp.floor(n * L(x / H))) for x in world if L(x / H) <= Lmax})
    return len({min(int(mp.floor(n * I(x / H))), 2 * n - 1) for x in world})
th = {"home": n * b, "edge": a * mp.e ** (1 - Lmax), "horizon": a / n}
f = M('1.001')
c2 = {"home past": (held(th["home"] * f, "reader"), held(th["home"] * f, "inplace")),
      "home short": (held(th["home"] / f, "reader"), held(th["home"] / f, "inplace")),
      "edge past": held(th["edge"] / f, "reader"), "edge short": held(th["edge"] * f, "reader"),
      "horizon past": held(th["horizon"] / f, "inplace"), "horizon short": held(th["horizon"] * f, "inplace")}
ok2 = (c2["home past"] == (1, 1) and c2["home short"][0] != 1 and c2["home short"][1] != 1 and c2["edge past"] == 0
       and c2["edge short"] != 0 and c2["horizon past"] == 1 and c2["horizon short"] != 1)
mid = mp.sqrt(a * b)
print(f"P2 a world of 31 amounts, 1e-3 .. 1e3, n = {n}, L_max = {Lmax}: at H = 1 the lays hold {held(mid, 'reader')} and"
      f" {held(mid, 'inplace')} addresses; {c2} ->", verdict(ok2))

# ---------------------------------------------------------------- P3: the best H to tell two amounts apart
w3h, w3m, w3e = M(0), M(0), M(0)
for x1, r in ((M(1), M(2)), (M(7), M(10)), (M('1e-3'), M('1e6'))):
    x2 = x1 * r
    sep = lambda u: mp.atan(x2 / mp.e ** u) - mp.atan(x1 / mp.e ** u)
    u = mp.findroot(lambda u: mp.diff(sep, u), (mp.log(x1), mp.log(x2)), solver='anderson')
    Hbest = mp.e ** u
    w3h = max(w3h, abs(Hbest / mp.sqrt(x1 * x2) - 1))
    w3m = max(w3m, abs(sep(u) - (2 * mp.atan(mp.sqrt(r)) - mp.pi / 2)))
    w3e = max(w3e, sep(mp.log(x1 * M('1e-8'))), sep(mp.log(x2 * M('1e8'))))
    print(f"   r = {mp.nstr(r, 6)}: best H {mp.nstr(Hbest, 12)} (sqrt(x1 x2) = {mp.nstr(mp.sqrt(x1 * x2), 12)}),"
          f" widest angle {mp.nstr(mp.degrees(sep(u)), 10)} deg")
ok3 = w3h <= M('1e-25') and w3m <= M('1e-30') and w3e <= M('1e-6')
print(f"P3 best H vs the geometric mean, worst {mp.nstr(w3h, 3)}; widest angle vs 2 atan(sqrt r) - 90 deg, worst"
      f" {mp.nstr(w3m, 3)}; at the ends at most {mp.nstr(w3e, 3)} rad ->", verdict(ok3))

# ---------------------------------------------------------------- P4: parallax's half-baseline is an H
def relerr(d, H):
    """Relative error of d per unit error of the angle the baseline subtends, from d(gamma) = H/tan(gamma/2)."""
    g = 2 * mp.atan(H / d)
    dd = mp.diff(lambda t: H / mp.tan(t / 2), g)
    return abs(dd) / d
w4a = max(abs(relerr(d, M(1)) / mp.cosh(mp.log(d)) - 1) for d in [M(10) ** (M(k) / 5) for k in range(-15, 15)])
w4h, w4w = M(0), M(0)
for a, b in ((M(1), M(100)), (M('1e-3'), M('1e3')), (M(5), M(6))):
    worst = lambda u: max(relerr(a, mp.e ** u), relerr(b, mp.e ** u))
    lo, hi = mp.log(a), mp.log(b)
    gr = (mp.sqrt(5) - 1) / 2
    for _ in range(170):                                      # golden-section search in ln H
        c, e = hi - gr * (hi - lo), lo + gr * (hi - lo)
        if worst(c) < worst(e): hi = e
        else: lo = c
    u = (lo + hi) / 2
    w4h = max(w4h, abs(mp.e ** u / mp.sqrt(a * b) - 1))
    w4w = max(w4w, abs(worst(u) - mp.cosh(mp.log(b / a) / 2)))
    print(f"   [{mp.nstr(a, 4)}, {mp.nstr(b, 4)}]: best half-baseline {mp.nstr(mp.e ** u, 12)} (sqrt(ab) ="
          f" {mp.nstr(mp.sqrt(a * b), 12)}), least worst error per step {mp.nstr(worst(u), 12)}")
ends = min(relerr(M(3), M(3) * M('1e-7')), relerr(M(3), M(3) * M('1e7')))
ok4 = w4a <= M('1e-25') and w4h <= M('1e-12') and w4w <= M('1e-20') and ends >= M('1e6')
print(f"P4 error per step vs cosh(ln(d/H)), worst {mp.nstr(w4a, 3)}; best half-baseline vs sqrt(ab), worst {mp.nstr(w4h, 3)};"
      f" least worst error vs cosh(ln(b/a)/2), worst {mp.nstr(w4w, 3)}; at H = d*1e-7 and d*1e7 at least {mp.nstr(ends, 4)} ->",
      verdict(ok4))
