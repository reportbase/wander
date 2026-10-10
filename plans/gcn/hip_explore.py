"""Where Hipparcos's bright stars lie (exploration for CNT's 1.2; HYG v3.8, path as argument, sha256 as in mag-plan)."""
import csv, gzip, hashlib, math, sys
raw = open(sys.argv[1], 'rb').read()
assert hashlib.sha256(raw).hexdigest() == '9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d'
Rm = [-0.8676661490, -0.1980763734, 0.4559837762]
st = []
for r in csv.DictReader(gzip.decompress(raw).decode().splitlines()):
    if not r['hip'] or not r['mag'] or not r['dist']: continue
    V, d = float(r['mag']), float(r['dist'])
    if V > 7.3 or d <= 0 or d >= 100000: continue
    a, de = math.radians(15 * float(r['ra'])), math.radians(float(r['dec']))
    z = d * (Rm[0] * math.cos(de) * math.cos(a) + Rm[1] * math.cos(de) * math.sin(a) + Rm[2] * math.sin(de))
    st.append((d, V, z, V + 5 - 5 * math.log10(d)))
st.sort(); n = len(st)
print(f'{n} Hipparcos stars brighter than V 7.3 with a distance')
for q in (0.1, 0.25, 0.5, 0.75, 0.9): print(f'  {int(q*100)}% are nearer than {st[int(q*n)][0]:.0f} pc')
print(f'  within 100 pc: {sum(1 for s in st if s[0] <= 100) / n:.1%}')
# 1.5 needs an even spread out to where each luminosity fades to V 7.3; check density of luminous stars (M_V < 0, visible to 290 pc) by distance
lum = [s for s in st if s[3] < 0]
print(f'luminous (M_V < 0, all seen to V 7.3 out to 288 pc): {len(lum)}; density by shell, relative to 50-100 pc:')
dens = {}
for a, b in [(50, 100), (100, 150), (150, 200), (200, 250), (250, 288)]:
    k = [s for s in lum if a <= s[0] < b]; dens[(a, b)] = len(k) / (b**3 - a**3)
    print(f'  {a}-{b} pc: {dens[(a, b)] / dens[(50, 100)]:.2f}  (|z| > 100 pc among them: {sum(1 for s in k if abs(s[2]) > 100)})')
print('the same, split by height: luminous stars by shell, |z| < 50 pc (the disc middle) and |z| > 50 pc')
for lab, f in [('|z| < 50', lambda s: abs(s[2]) < 50), ('|z| > 50', lambda s: abs(s[2]) >= 50)]:
    out = []
    for a, b in [(50, 100), (100, 150), (150, 200), (200, 250), (250, 288)]:
        k = [s for s in lum if a <= s[0] < b and f(s)]; out.append(f'{a}-{b}: {len(k)}')
    print('  ', lab, '  '.join(out))
# the count slope CNT measured, made from these distances: what slope would an even spread of these same stars give?
# for each star the distance at which it would fade to V 7.3 is its d * 10**((7.3 - V)/5); an even spread fills the
# sphere of that radius with equal density, so compare the observed N(<V) slope with one built from the measured
# density falling off: just report the shares by luminosity
for lo, hi in [(-9, -2), (-2, 0), (0, 2), (2, 4), (4, 9)]:
    k = [s for s in st if lo <= s[3] < hi]
    print(f'  M_V {lo:+d} to {hi:+d}: {len(k):5d} stars ({len(k)/n:.0%}), seen to {10 ** ((7.3 - hi + 5) / 5):.0f}-{10 ** ((7.3 - lo + 5) / 5):.0f} pc')
