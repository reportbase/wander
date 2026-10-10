"""CNT run 2 (plans/cnt-plan.md): counts by kind and distance, on the Hipparcos stars (HYG v3.8)."""
import csv, gzip, hashlib, io, math, os, sys, urllib.request
URL = 'https://raw.githubusercontent.com/astronexus/HYG-Database/main/hyg/v3/hyg_v38.csv.gz'
SHA = '9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d'
path = sys.argv[1] if len(sys.argv) > 1 else None
raw = open(path, 'rb').read() if path and os.path.exists(path) else urllib.request.urlopen(URL, timeout=120).read()
assert hashlib.sha256(raw).hexdigest() == SHA, 'the data is not the file the plan names'
K = math.log2(10) / 2.5
Rm = [-0.8676661490, -0.1980763734, 0.4559837762]
def gal_b(ra_h, dec_d):
    a, d = math.radians(15 * ra_h), math.radians(dec_d)
    return math.degrees(math.asin(Rm[0] * math.cos(d) * math.cos(a) + Rm[1] * math.cos(d) * math.sin(a) + Rm[2] * math.sin(d)))
def giant(sp):
    s = sp.replace(' ', ''); return s.startswith('K0III') and not s.startswith('K0III-IV') and not s.startswith('K0IV')
def gdwarf(sp):   # as MAG's
    s = sp.replace(' ', '')
    return len(s) >= 3 and s[0] == 'G' and s[1] in '012345' and (s[2:].startswith('V') or (s[2] == '.' and 'V' in s[3:5] and 'IV' not in s[3:6])) and not s[2:].startswith('IV')
stars = []
for r in csv.DictReader(io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(raw)), encoding='utf-8')):
    if not r['hip'] or not r['dist'] or not r['mag'] or r['var'].strip(): continue
    d = float(r['dist'])
    if d <= 0 or d >= 100000: continue
    stars.append((d, float(r['mag']), r['spect'].strip(), gal_b(float(r['ra']), float(r['dec']))))
def slope_cum(vals, lo, hi, step):
    vals = sorted(vals); xs, ys = [], []; x = lo
    while x <= hi + 1e-9:
        n = sum(1 for v in vals if v <= x)
        if n: xs.append(x); ys.append(math.log2(n))
        x += step
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
g = [s for s in stars if gdwarf(s[2]) and s[0] <= 23]
s5 = slope_cum([math.log2(s[0]) for s in g], math.log2(8), math.log2(23), 0.05)
k = [s for s in stars if giant(s[2]) and s[0] <= 140]
s6 = slope_cum([math.log2(s[0]) for s in k], math.log2(40), math.log2(140), 0.05)
kp = [s for s in k if abs(s[3]) < 30]; kq = [s for s in k if abs(s[3]) > 30]
sp = slope_cum([math.log2(s[0]) for s in kp], math.log2(40), math.log2(140), 0.05)
sq = slope_cum([math.log2(s[0]) for s in kq], math.log2(40), math.log2(140), 0.05)
kv = [s for s in k if s[1] <= 7.3]
# counted by light: N brighter than V, against light -K*V (brighter = more light); slope of log2 N against light, sign turned
mags = sorted(s[1] for s in kv); xs, ys = [], []; v = 3.0
while v <= 7.3 + 1e-9:
    n = sum(1 for m in mags if m <= v)
    if n: xs.append(-K * v); ys.append(math.log2(n))
    v += 0.1
mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
s8 = -sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
print(f'G dwarfs within 23 pc: {len(g)}; K0 giants within 140 pc: {len(k)} (|b| < 30: {len(kp)}, |b| > 30: {len(kq)}; V <= 7.3: {len(kv)})')
print(f'P5: {"not killed" if 2.5 <= s5 <= 3.5 else "KILLED"}. G dwarfs, 8-23 pc: {s5:.3f} levels of number per level of distance; 3 for an even spread')
print(f'P6: {"not killed" if 2.6 <= s6 <= 3.4 else "KILLED"}. K0 giants, 40-140 pc, all sky: {s6:.3f}')
print(f'P7: {"not killed" if sp - sq >= 0.15 else "KILLED"}. K0 giants, 40-140 pc: |b| < 30 {sp:.3f}, |b| > 30 {sq:.3f}, difference {sp - sq:.3f}')
print(f'P8: {"not killed" if 1.25 <= s8 <= 1.75 else "KILLED"}. K0 giants within 140 pc and V <= 7.3, by light over V 3-7.3: {s8:.3f} levels of number per level of light; 1.5 for an even spread')
