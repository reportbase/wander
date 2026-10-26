"""FPV run 4: B5 and B6 again (plans/fpv-plan.md, run 4).
Run from the repository's root: python3 runs/fpv/fpv4.py"""
import mpmath as mp

mp.mp.dps = 40
pi, ok = mp.pi, True
tiny = mp.mpf(10) ** -20


def say(code, good, note):
    global ok
    ok = ok and good
    print(f"  {'ok  ' if good else 'FAIL'} {code}: {note}")


# A lay is a map from the address a in [0, 1] to depth d; K cells are a = k/K.
# Each lay carries its inverse, the address of a depth, in closed form.
def one(H):
    lay = lambda a: H * mp.tan(a * pi / 2)
    lay.inv = lambda d: (2 / pi) * mp.atan(d / H)
    return lay


def two(f1, f2):
    tm, m = mp.atan(mp.sqrt(f2 / f1)), mp.sqrt(f1 * f2)   # each half's angle, atan(e^{D/2})
    lay = lambda a: f1 * mp.tan(2 * a * tm) if a <= mp.mpf(1) / 2 else f2 * mp.tan(pi / 2 - 2 * (1 - a) * tm)
    lay.inv = lambda d: mp.atan(d / f1) / (2 * tm) if d <= m else 1 - (pi / 2 - mp.atan(d / f2)) / (2 * tm)
    # run 4: each half's slope in closed form, one-sided at a = 1/2 (run 3 differentiated across the join)
    lay.slope = lambda a: (f1 * 2 * tm * mp.sec(2 * a * tm) ** 2 if a < mp.mpf(1) / 2
                           else f2 * 2 * tm * mp.sec(pi / 2 - 2 * (1 - a) * tm) ** 2)
    return lay


def inv(lay, d):
    return lay.inv(d)


def rel(lay, d, K):                                # continuum relative cell at d: (dd/da)/d / K
    a = inv(lay, d)
    if hasattr(lay, 'slope'):
        return lay.slope(a) / d / K
    return mp.diff(lay, a) / d / K


def cellrel(lay, d, K, a=None):                    # the discrete cell holding d
    a = inv(lay, d) if a is None else a
    k = int(mp.floor(a * K + mp.mpf(10) ** -30))
    lo, hi = lay(mp.mpf(k) / K), lay(mp.mpf(k + 1) / K)
    return (hi - lo) / mp.sqrt(lo * hi)


f1, K = mp.mpf(50), 32
Ds = [mp.mpf(x) / 4 for x in range(1, 33)]          # 0.25 ... 8 nats
B1 = lambda D, K: pi / K * mp.cosh(D / 2)
B2 = lambda D, K: 4 * mp.atan(mp.exp(D / 2)) / K

print("B1, one corner")
w1 = w2 = 0
for D in Ds:
    f2 = f1 * mp.exp(D)
    Hs = mp.findroot(lambda h: rel(one(mp.exp(h)), f1, K) - rel(one(mp.exp(h)), f2, K), mp.log(f1) + D / 3)
    w1 = max(w1, abs(mp.exp(Hs) / mp.sqrt(f1 * f2) - 1))
    lay = one(mp.sqrt(f1 * f2))
    w2 = max(w2, abs(rel(lay, f1, K) - B1(D, K)), abs(rel(lay, f2, K) - B1(D, K)))
say("B1", w1 < tiny, f"the H equalising the two targets is sqrt(f1 f2) (worst {mp.nstr(w1, 3)}), the minimax since one "
    "target's cell grows and the other's shrinks as H moves")
say("B1", w2 < tiny, f"both targets' relative cell (pi/K) cosh(D/2) (worst {mp.nstr(w2, 3)})")

print("\nB2, two corners")
w = 0
for D in Ds:
    f2 = f1 * mp.exp(D); lay = two(f1, f2)
    w = max(w, abs(rel(lay, f1, K) - B2(D, K)), abs(rel(lay, f2, K) - B2(D, K)))
say("B2", w < tiny, f"each target's relative cell 4 atan(e^(D/2))/K (worst {mp.nstr(w, 3)})")

print("\nB3, the crossover")
Ds_ = mp.findroot(lambda D: pi * mp.cosh(D / 2) - 4 * mp.atan(mp.exp(D / 2)), 2)
say("B3", 1.9 <= Ds_ <= 2.1, f"D* = {mp.nstr(Ds_, 15)} nats, a distance ratio {mp.nstr(mp.exp(Ds_), 8)}, "
    f"{mp.nstr(Ds_ / mp.log(2), 6)} doublings; the cell there {mp.nstr(B1(Ds_, 1) / pi, 8)} x pi/K")
below = all(B1(D, K) < B2(D, K) for D in [Ds_ * i / 20 for i in range(1, 20)])
above = all(B1(D, K) > B2(D, K) for D in [Ds_ + mp.mpf(i) / 4 for i in range(1, 40)])
say("B3", below and above, "one corner strictly better below D* (19 points), two corners above (39 points to D* + 9.75)")

print("\nB4, the limits")
say("B4", abs(B1(0, K) - pi / K) < tiny and abs(B2(0, K) - pi / K) < tiny, "at D = 0 both pi/K")
e = mp.mpf(10) ** -8
s1 = (B1(e, K) / (pi / K) - 1) / e ** 2
s2 = (B2(e, K) / (pi / K) - 1) / e
say("B4", abs(s1 - mp.mpf(1) / 8) < mp.mpf(10) ** -7 and abs(s2 - 1 / pi) < mp.mpf(10) ** -7,
    f"near 0: one corner 1 + {mp.nstr(s1, 10)} D^2, two corners 1 + {mp.nstr(s2, 10)} D (1/8 and 1/pi = {mp.nstr(1/pi, 10)})")
big = mp.mpf(80)
say("B4", abs(B2(big, K) / (2 * pi / K) - 1) < mp.mpf(10) ** -15 and abs(B1(big, K) / (pi / (2 * K) * mp.exp(big / 2)) - 1)
    < mp.mpf(10) ** -15, "as D -> inf, two corners -> 2 pi/K, one corner ~ (pi/2K) e^(D/2) (both within 1e-15 at D = 80)")

print("\nB5, between the targets")
wc = wm = 0; finest = True
for D in Ds:
    f2 = f1 * mp.exp(D); m = mp.sqrt(f1 * f2); lay = two(f1, f2)
    lo = mp.diff(lambda a: f1 * mp.tan(2 * a * mp.atan(mp.exp(D / 2))), mp.mpf(1) / 2) / m / K
    hi = mp.diff(lambda a: f2 * mp.tan(pi / 2 - 2 * (1 - a) * mp.atan(mp.exp(D / 2))), mp.mpf(1) / 2) / m / K
    wc = max(wc, abs(lo - hi))
    wm = max(wm, abs(lo - 4 * mp.atan(mp.exp(D / 2)) * mp.cosh(D / 2) / K))
    grid = [f1 * mp.exp(D * i / 40) for i in range(41)]
    r = [rel(lay, d, K) for d in grid]
    finest = finest and max(r) == r[20] and abs(rel(one(m), m, K) - pi / K) < tiny
say("B5", wc < tiny, f"the two-corner grain continuous at m (worst jump {mp.nstr(wc, 3)})")
say("B5'", wm < tiny and finest, "m its coarsest point between the targets, 4 atan(e^(D/2)) cosh(D/2)/K; one corner finest "
    f"there, pi/K (worst {mp.nstr(wm, 3)})")
for D in (1, 2, 4, 8):
    D = mp.mpf(D)
    print(f"      D = {mp.nstr(D, 3)}: at the targets one {mp.nstr(B1(D, 1) / pi, 5)}, two {mp.nstr(B2(D, 1) / pi, 5)};"
          f" at m one 1, two {mp.nstr(4 * mp.atan(mp.exp(D / 2)) * mp.cosh(D / 2) / pi, 5)}  (x pi/K)")

print("\nB6, discrete cells")
mp.mp.dps = 30
for KK, top in ((32, 4), (1024, 8)):
    worst = 0
    for D in [mp.mpf(x) / 4 for x in range(1, 4 * top + 1)]:
        f2 = f1 * mp.exp(D)
        for lay, want in ((one(mp.sqrt(f1 * f2)), B1(D, KK)), (two(f1, f2), B2(D, KK))):
            for d in (f1, f2):
                e = abs(cellrel(lay, d, KK) / want - 1)
                worst = max(worst, e / want if KK == 32 else e)
    if KK == 32:
        say("B6'", worst <= 1, f"K = 32, D <= 4: each target's cell off the continuum by at most {mp.nstr(worst, 3)} "
            "of the continuum relative cell")
    else:
        say("B6", worst < 0.05, f"K = {KK}, D <= {top}: the cells holding the targets within {mp.nstr(100 * worst, 3)}% of the continuum")
KK = 1024; Dd = None
for i in range(1000, 3001, 2):
    D = mp.mpf(i) / 1000; f2 = f1 * mp.exp(D)
    one_w = max(cellrel(one(mp.sqrt(f1 * f2)), f1, KK), cellrel(one(mp.sqrt(f1 * f2)), f2, KK))
    two_w = max(cellrel(two(f1, f2), f1, KK), cellrel(two(f1, f2), f2, KK))
    if two_w < one_w:
        Dd = D; break
say("B6", Dd is not None and abs(Dd - Ds_) < 0.2, f"K = 1024: two corners first better on the cells at D = {Dd} "
    f"(D* = {mp.nstr(Ds_, 6)})")

print("\n" + ("nothing killed" if ok else "KILLED"))
