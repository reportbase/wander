"""GCN exploration (not predictions; Tom: "just a quick test ... continue to test to see what the situation is").
Usage: python3 -I plans/gcn/explore.py <GCNS table1c TSV>"""
import io, contextlib, math, runpy, sys
with contextlib.redirect_stdout(io.StringIO()):
    g = runpy.run_path(__file__.replace('explore.py', 'gcn.py'))
stars, KINDS, in_kind, on_band, sd, sl = g['stars'], g['KINDS'], g['in_kind'], g['on_band'], g['slope_dist'], g['slope_light']
Rm = [[-0.0548755604, -0.8734370902, -0.4838350155], [0.4941094279, -0.4448296300, 0.7469822445], g['Rm']]
def xyz(s): return s   # placeholder; positions recomputed below
# rebuild galactic x, y, z from the raw file (gcn.py keeps only b)
raw = open(sys.argv[1], encoding='utf-8').read().split('\n')
pos = []
for l in [l for l in raw if l.strip() and not l.startswith('#')][3:]:
    f = [x.strip() for x in l.split('\t')]
    if not f[4] or not f[5] or not f[6] or not f[7]: continue
    plx, e = float(f[2]), float(f[3])
    if plx < 10 or plx / e < 10: continue
    a, d = math.radians(float(f[0])), math.radians(float(f[1])); D = 1000 / plx
    u = [math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d)]
    G = float(f[4]); c = float(f[5]) - float(f[6]); MG = G + 5 + 5 * math.log10(plx / 1000)
    pos.append((D, G, MG, c, [D * sum(r[i] * u[i] for i in range(3)) for r in Rm]))
ms = [p for p in pos if 0.5 <= p[3] <= 3.2 and abs(p[2] - (3.4 * p[3] + 1.9)) <= 1.5]
print(f'main-sequence band, no RUWE cut: {len(ms)} stars within 100 pc')
print('\n1. local slope of log2 N(<d) by distance, no RUWE cut (3 = even spread)')
for name, lo, hi in KINDS:
    k = [s for s in stars if on_band(s) and in_kind(s, lo, hi)]
    print(f'  {name:8s}', '  '.join(f'{a}-{b}: {sd([s[0] for s in k], a, b):.2f}' for a, b in [(10, 25), (25, 35), (35, 50), (50, 70), (70, 100)]))
print('\n2. by light, no RUWE cut, G_max - 3 to G_max (1.5 = even spread)')
for name, lo, hi in KINDS:
    k = [s for s in stars if on_band(s) and in_kind(s, lo, hi)]
    mg = sorted(s[2] for s in k); gmax = mg[int(0.01 * (len(mg) - 1))] + 5
    print(f'  {name:8s} G_max {gmax:.2f}: {sl([s[1] for s in k], gmax - 3, gmax):.3f}')
print('\n3. density against height z, main-sequence band, cylinder R < 60 pc (stars per 1000 pc^3)')
cyl = [p for p in ms if math.hypot(p[4][0], p[4][1]) < 60]
vol = math.pi * 60 ** 2 * 10 / 1000
rows = []
for z0 in range(-80, 80, 10):
    n = sum(1 for p in cyl if z0 <= p[4][2] < z0 + 10 and math.sqrt(p[4][0]**2 + p[4][1]**2 + p[4][2]**2) <= 100)
    rows.append((z0 + 5, n / vol)); print(f'  z {z0:+4d} to {z0+10:+4d}: {n / vol:7.2f}')
zs = [p[4][2] for p in cyl if abs(p[4][2]) < 80]
print(f'  mean z of the stars in |z| < 80 (0 if the Sun sits at the middle): {sum(zs)/len(zs):+.2f} pc')
inner = [r for r in rows if abs(r[0]) <= 25]; outer = [r for r in rows if abs(r[0]) >= 55]
print(f'  |z| <= 25 mean {sum(r[1] for r in inner)/len(inner):.2f}; |z| >= 55 mean {sum(r[1] for r in outer)/len(outer):.2f}')
for h in (100, 200, 300, 500):
    print(f'    an exponential with scale {h} pc would give outer/inner {math.exp(-(62.5 - 12.5) / h):.3f}')
print(f'    measured {sum(r[1] for r in outer)/len(outer) / (sum(r[1] for r in inner)/len(inner)):.3f}')
print('\n4. density in the plane slab |z| < 20, by distance in the plane R (stars per 1000 pc^3)')
for a, b in [(0, 20), (20, 40), (40, 60), (60, 80), (80, 98)]:
    n = sum(1 for p in ms if abs(p[4][2]) < 20 and a <= math.hypot(p[4][0], p[4][1]) < b)
    print(f'  R {a:3d}-{b:3d}: {n / (math.pi * (b*b - a*a) * 40 / 1000):7.2f}')
print('   toward the Galactic centre and away (x > 0 is toward the centre), |z| < 20, 40 < R < 98:')
for lab, f in [('toward', lambda p: p[4][0] > 0), ('away', lambda p: p[4][0] < 0)]:
    n = sum(1 for p in ms if abs(p[4][2]) < 20 and 40 <= math.hypot(p[4][0], p[4][1]) < 98 and f(p))
    print(f'    {lab}: {n / (math.pi * (98**2 - 40**2) * 40 / 2000):.2f}')
