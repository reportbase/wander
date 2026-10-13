"""HKO run 3: the in-place lay's peak found by search. See plans/hko-plan.md (P5').

Run 2 (hko/hko2.py) is kept as it ran. Here the largest in-place span is found by golden-section search in ln H and
compared with H = sqrt(d(d + D)) and 2n(1 - sqrt(d/(d + D))); monotone rise and fall checked on log grids.
Run: python3 hko/hko3.py
"""
import mpmath as mp
mp.mp.dps = 60
M = mp.mpf
L = lambda s: s if s <= 1 else 1 + mp.log(s)
I = lambda s: s if s <= 1 else 2 - 1 / s
n = 32
def span(lay, d, D, H): return n * (lay((d + D) / H) - lay(d / H))
gr = (mp.sqrt(5) - 1) / 2
wH, wV, mono = M(0), M(0), True
for d in (M(1), M(10), M(1000)):
    for r in (M('1e-3'), M('0.1'), M(1)):
        D = r * d
        f = lambda u: span(I, d, D, mp.e ** u)
        lo, hi = mp.log(d) - mp.log(1000), mp.log(d) + mp.log(1000)
        for _ in range(260):
            c, e = hi - gr * (hi - lo), lo + gr * (hi - lo)
            if f(c) > f(e): hi = e
            else: lo = c
        u = (lo + hi) / 2; Hp = mp.e ** u
        wH = max(wH, abs(Hp / mp.sqrt(d * (d + D)) - 1))
        wV = max(wV, abs(f(u) / (2 * n * (1 - mp.sqrt(d / (d + D)))) - 1))
        up = [span(I, d, D, d * M('1e-3') * (Hp / (d * M('1e-3'))) ** (M(k) / 399)) for k in range(400)]
        dn = [span(L, d, D, d * M(1000) ** (M(k) / 399)) for k in range(400)]
        mono = mono and all(b > a for a, b in zip(up, up[1:])) and all(b < a for a, b in zip(dn[1:], dn[2:]))
        print(f"   d = {mp.nstr(d, 4)}, D/d = {mp.nstr(r, 3)}: in-place peak at H/d = {mp.nstr(Hp / d, 15)}"
              f" (sqrt(1 + D/d) = {mp.nstr(mp.sqrt(1 + r), 15)}), span {mp.nstr(f(u), 12)}")
ok = wH <= M('1e-20') and wV <= M('1e-30') and mono
print(f"P5' peak vs sqrt(d(d + D)), worst {mp.nstr(wH, 3)}; value vs 2n(1 - sqrt(d/(d + D))), worst {mp.nstr(wV, 3)};"
      f" rise to the peak and the reader's-lay fall past d strictly monotone: {mono} ->", "not killed" if ok else "KILLED")
