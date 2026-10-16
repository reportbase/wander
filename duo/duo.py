"""DUO run 1 (plans/duo-plan.md): the 1987 neutron absorbers' fringe amplitude against the two forms, √a (a foil: every
arrival one pure pair, on the duality circle) and a (a chopper: a mixture of corner and home). Values are the readings in
duo/readings.md, taken by hand from the scan of Summhammer, Rauch and Tuppinger's figure. σ is half the vertical error
bar (or half the marker) with 3 px added in quadrature, as the plan fixed; a second column also carries a's own
horizontal bar through each form (post hoc, reported, not the verdict).
Run: python3 duo/duo.py
"""
from math import sqrt

CAL = {  # panel: (a from x, A from y, A per px, a per px)
    'main':   (lambda x: (x - 1490) / 576,          lambda y: (3303 - y) / 588,             1 / 588,       1 / 576),
    'middle': (lambda x: 0.01 * (x - 921) / 47.1,   lambda y: 0.1 * (3229 - y) / 237.25,    0.1 / 237.25,  0.01 / 47.1),
    'left':   (lambda x: 0.005 * (x - 433.5) / 272.5, lambda y: 0.05 * (3188.5 - y) / 418.5, 0.05 / 418.5, 0.005 / 272.5),
}
PTS = [  # id, panel, kind, x, y, half bar y, half bar x
    ('S1', 'main', 'sto', 1521.5, 3165, 8.5, 0), ('S2', 'main', 'sto', 1552.5, 3111, 9, 0),
    ('S3', 'main', 'sto', 1572.5, 3076, 14.25, 0), ('S4', 'main', 'sto', 1616, 3019.5, 9.5, 0),
    ('S5', 'main', 'sto', 1712, 2957, 14.25, 0), ('S6', 'main', 'sto', 1762, 2914.5, 15, 0),
    ('D1', 'main', 'det', 1630.5, 3161, 6, 0), ('D2', 'main', 'det', 1770.5, 3020, 12, 5.5),
    ('D3', 'main', 'det', 1912, 2879.5, 11.5, 6),
    ('M2', 'middle', 'sto', 945.5, 3127, 15, 0), ('M3', 'middle', 'sto', 961, 2992.5, 17, 11.5),
    ('M4', 'middle', 'sto', 1034, 2891, 22, 12.25), ('M5', 'middle', 'sto', 1033.5, 2837.5, 23.5, 12.25),
    ('L1', 'left', 'sto', 460, 3053.5, 38.5, 23.5), ('L2', 'left', 'sto', 487.5, 3041, 25.5, 21),
    ('L3', 'left', 'sto', 605, 2875.5, 62.5, 46),
]
form = {'sto': lambda a: sqrt(a), 'det': lambda a: a}
slope = {'sto': lambda a: 0.5 / sqrt(a), 'det': lambda a: 1.0}
other = {'sto': 'det', 'det': 'sto'}
rows = {}
print(f"{'id':3} {'kind':4} {'a':>8} {'A':>8} {'σ':>7} {'form':>8} {'z':>6} {'z (a too)':>9} {'z other':>8}")
for pid, panel, kind, x, y, hy, hx in PTS:
    fa, fA, dA, da = CAL[panel]
    a, A = fa(x), fA(y)
    s = sqrt(hy**2 + 9) * dA
    sa = sqrt(hx**2 + 9) * da if hx else 3 * da
    pred = form[kind](a)
    z = (A - pred) / s
    z2 = (A - pred) / sqrt(s**2 + (slope[kind](a) * sa)**2)
    zo = (A - form[other[kind]](a)) / s
    rows[pid] = (kind, a, A, s, z, z2)
    print(f"{pid:3} {kind:4} {a:8.5f} {A:8.4f} {s:7.4f} {pred:8.4f} {z:6.2f} {z2:9.2f} {zo:8.2f}")

def verdict(ids, col):
    zs = [abs(rows[i][col]) for i in ids]
    out2 = sum(z > 2 for z in zs); out3 = sum(z > 3 for z in zs)
    return out2, out3, len(zs), (out2 * 20 <= len(zs)) and out3 == 0

sto = [p for p in rows if rows[p][0] == 'sto']; det = [p for p in rows if rows[p][0] == 'det']
for label, ids in (("D1, M2 its own point", sto), ("D1, M2 taken as L3", [p for p in sto if p != 'M2']),
                   ("D1, a ≥ 0.05 only (main plot)", [p for p in sto if rows[p][1] >= 0.05])):
    o2, o3, n, ok = verdict(ids, 4); o2b, o3b, _, okb = verdict(ids, 5)
    print(f"{label}: outside 2σ {o2}/{n}, outside 3σ {o3} → {'not killed' if ok else 'KILLED'}"
          f"   (with a's bar: {o2b}, {o3b} → {'not killed' if okb else 'killed'})")
o2, o3, n, ok = verdict(det, 4)
print(f"D2: outside 2σ {o2}/{n}, outside 3σ {o3} → {'not killed' if ok else 'KILLED'}")

# D3: the fringe panels' bars
foil, chop = 295.5 / 661.5, 161 / 662
sf = foil * sqrt((2 / 295.5)**2 + (2 / 661.5)**2); sc = chop * sqrt((2 / 161)**2 + (2 / 662)**2)
af, saf, ac, sac = 0.226, 0.008, 0.242, 0.002
gap = (2 * sqrt(ac) / (1 + ac) - 2 * ac / (1 + ac))
print(f"D3: foil bar {foil:.4f} ± {sf:.4f} (√a {sqrt(af):.4f} ± {saf / (2 * sqrt(af)):.4f}, a {af});"
      f" chopper bar {chop:.4f} ± {sc:.4f} (a {ac}, √a {sqrt(ac):.4f})")
print(f"D3: foil − chopper = {foil - chop:.4f}, {(foil - chop) / sqrt(sf**2 + sc**2):.1f}σ;"
      f" the forms' gap in amplitude at a ≈ 0.24: {sqrt(ac) - ac:.4f} → {'not killed' if foil - chop > 2 * sqrt(sf**2 + sc**2) else 'KILLED'}")
print(f"   post hoc: the foil bar against √0.226: {(foil - sqrt(af)) / sqrt(sf**2 + (saf / (2 * sqrt(af)))**2):.2f}σ;"
      f" the chopper bar against 0.242: {(chop - ac) / sqrt(sc**2 + sac**2):.2f}σ")
