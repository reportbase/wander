"""CNT (plans/cnt-plan.md): star counts in levels, on the Hipparcos stars (HYG v3.8). V and position only."""
import csv, gzip, hashlib, io, math, os, sys, urllib.request
URL = 'https://raw.githubusercontent.com/astronexus/HYG-Database/main/hyg/v3/hyg_v38.csv.gz'
SHA = '9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d'
path = sys.argv[1] if len(sys.argv) > 1 else None
raw = open(path, 'rb').read() if path and os.path.exists(path) else urllib.request.urlopen(URL, timeout=120).read()
assert hashlib.sha256(raw).hexdigest() == SHA, 'the data is not the file the plan names'
K = math.log2(10) / 2.5
# J2000 equatorial -> galactic rotation (the standard matrix)
Rm = [[-0.0548755604, -0.8734370902, -0.4838350155], [0.4941094279, -0.4448296300, 0.7469822445], [-0.8676661490, -0.1980763734, 0.4559837762]]
def gal_b(ra_h, dec_d):
    a, d = math.radians(15 * ra_h), math.radians(dec_d)
    x, y, z = math.cos(d) * math.cos(a), math.cos(d) * math.sin(a), math.sin(d)
    return math.degrees(math.asin(Rm[2][0] * x + Rm[2][1] * y + Rm[2][2] * z))
stars = []
for r in csv.DictReader(io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(raw)), encoding='utf-8')):
    if not r['hip'] or not r['mag']: continue
    stars.append((float(r['mag']), gal_b(float(r['ra']), float(r['dec']))))
def slope(sel, lo, hi):
    mags = sorted(m for m, b in sel)
    xs, ys = [], []
    v = lo
    while v <= hi + 1e-9:
        n = sum(1 for m in mags if m <= v)
        if n > 0: xs.append(-K * v); ys.append(math.log2(n))
        v += 0.1
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    b = sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    return -b, sum(1 for m in mags if m <= hi)
allsky = stars; plane = [s for s in stars if abs(s[1]) < 10]; poles = [s for s in stars if abs(s[1]) > 60]
s14, n14 = slope(allsky, 1, 4); s57, n57 = slope(allsky, 5, 7.3)
sp, npl = slope(plane, 4, 7.3); sq, npo = slope(poles, 4, 7.3)
print(f'{len(stars)} Hipparcos stars with V; brighter than 7.3: {sum(1 for m, b in stars if m <= 7.3)} (plane {sum(1 for m, b in plane if m <= 7.3)}, poles {sum(1 for m, b in poles if m <= 7.3)})')
print(f'P1: {"not killed" if 1.3 <= s14 <= 1.7 else "KILLED"}. all sky, V 1-4: {s14:.3f} levels of number per level of light ({n14} stars to V 4); 1.5 for an even spread')
print(f'P2: {"not killed" if s14 - s57 >= 0.1 else "KILLED"}. all sky, V 5-7.3: {s57:.3f}, shallower by {s14 - s57:.3f}')
print(f'P3: {"not killed" if sp - sq >= 0.1 else "KILLED"}. V 4-7.3: plane (|b| < 10) {sp:.3f}, poles (|b| > 60) {sq:.3f}, difference {sp - sq:.3f}')
print(f'P4: {"not killed" if sp >= 1.25 else "KILLED"}. in the plane {sp:.3f}')
for lo, hi in [(0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7.3)]:
    s, n = slope(allsky, lo, hi); print(f'  all sky, V {lo}-{hi}: {s:.3f}')
