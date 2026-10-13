"""HKO run 2: detail per object against H. See plans/hko-plan.md (P5).

An object spans the amounts [d, d + D]; a reader with n addresses across its near field gives it n times the stretch of
lay it covers. The reader's lay L(s) = s, then 1 + ln s; the in-place lay I(s) = s, then 2 - 1/s; s = x/H. mpmath at 60
digits: spans counted from the lays, against the closed forms.
Run: python3 hko/hko2.py
"""
import mpmath as mp
mp.mp.dps = 60
M = mp.mpf
L = lambda s: s if s <= 1 else 1 + mp.log(s)
I = lambda s: s if s <= 1 else 2 - 1 / s
n = 32
def span(lay, d, D, H): return n * (lay((d + D) / H) - lay(d / H))
wa, wb, wflat, okc, rows = M(0), M(0), M(0), True, []
for d in (M(1), M(10), M(1000)):
    for r in (M('1e-3'), M('0.1'), M(1)):
        D = r * d
        Hs = [d * M(10) ** (M(k) / 1000 * 6 - 3) for k in range(2001)] + [d, d + D]
        for H in Hs[::50] + [d, d + D]:
            if d + D <= H: wa = max(wa, abs(span(L, d, D, H) / (n * D / H) - 1), abs(span(I, d, D, H) / (n * D / H) - 1))
            if d >= H:
                wb = max(wb, abs(span(L, d, D, H) / (n * mp.log(1 + D / d)) - 1), abs(span(I, d, D, H) / (n * D * H / (d * (d + D))) - 1))
        flat = [span(L, d, D, H) for H in Hs if H <= d]
        wflat = max(wflat, max(flat) - min(flat))
        vals = [(span(I, d, D, H), H) for H in Hs]
        best, Hbest = max(vals)
        inside = d - d * M('1e-40') <= Hbest <= d + D + d * M('1e-40')
        within = best <= n * D / d * (1 + D / d) and best >= n * D / d / (1 + D / d)
        okc = okc and inside and within
        rows.append(f"   d = {mp.nstr(d, 4)}, D/d = {mp.nstr(r, 3)}: in-place largest {mp.nstr(best, 8)} at H/d = {mp.nstr(Hbest / d, 8)}"
                    f" (n D/d = {mp.nstr(n * D / d, 8)}); reader's lay past the corner {mp.nstr(span(L, d, D, d / 10), 8)}")
for r in rows: print(r)
ok = wa <= M('1e-30') and wb <= M('1e-30') and wflat <= M('1e-30') and okc
print(f"P5 inside the corner vs nD/H, worst {mp.nstr(wa, 3)}; past it vs n ln(1 + D/d) and nDH/(d(d + D)), worst {mp.nstr(wb, 3)};"
      f" the reader's lay flat over H <= d to {mp.nstr(wflat, 3)}; the in-place peak with the object at the corner: {okc} ->",
      "not killed" if ok else "KILLED")
