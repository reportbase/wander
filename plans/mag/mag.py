"""MAG (plans/mag-plan.md): two levels of light per level of distance, on the Hipparcos stars (HYG v3.8).
Uses only hip, dist (from parallax), mag (V) and spect; never absmag or lum. Downloads the data and checks its sha256."""
import csv, gzip, hashlib, io, math, os, sys, urllib.request
URL = 'https://raw.githubusercontent.com/astronexus/HYG-Database/main/hyg/v3/hyg_v38.csv.gz'
SHA = '9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d'
path = sys.argv[1] if len(sys.argv) > 1 else None
raw = open(path, 'rb').read() if path and os.path.exists(path) else urllib.request.urlopen(URL, timeout=120).read()
assert hashlib.sha256(raw).hexdigest() == SHA, 'the data is not the file the plan names'
rows = list(csv.DictReader(io.TextIOWrapper(gzip.GzipFile(fileobj=io.BytesIO(raw)), encoding='utf-8')))
K = math.log2(10) / 2.5                                    # levels of light per magnitude: 1.3288
stars = []
for r in rows:
    if not r['hip'] or not r['dist'] or not r['mag']: continue
    d = float(r['dist'])
    if d >= 100000 or d <= 0 or r['var'].strip(): continue
    stars.append((d, float(r['mag']), r['spect'].strip()))
def giant(sp):
    s = sp.replace(' ', '')
    return s.startswith('K0III') and not s.startswith('K0III-IV') and not s.startswith('K0IV')
def gdwarf(sp):
    s = sp.replace(' ', '')
    return len(s) >= 3 and s[0] == 'G' and s[1] in '012345' and (s[2:].startswith('V') or (s[2] == '.' and 'V' in s[3:5] and 'IV' not in s[3:6])) and not s[2:].startswith('IV')
def fit(sel):
    x = [math.log2(d) for d, m, s in sel]; y = [-K * m for d, m, s in sel]; n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    rms = math.sqrt(sum((c - (my + b * (a - mx))) ** 2 for a, c in zip(x, y)) / n)
    return n, b, rms, (min(x), max(x))
print(f'{len(stars)} Hipparcos stars with a distance and no variable flag; 5 magnitudes = {5 * K:.4f} levels of light')
g1 = [t for t in stars if giant(t[2]) and 20 <= t[0] <= 140]
n, b, rms, xr = fit(g1)
print(f'P1: {"not killed" if 100 <= n and -2.15 <= b <= -1.85 else "KILLED"}. K0 giants, 20-140 pc: n = {n}, slope {b:.3f} light levels per distance level, over {xr[1] - xr[0]:.2f} levels of distance')
p4 = rms
g2 = [t for t in stars if gdwarf(t[2]) and t[0] <= 23]
n2, b2, rms2, xr2 = fit(g2)
print(f'P2: {"not killed" if 20 <= n2 and -2.3 <= b2 <= -1.7 else "KILLED"}. G0-G5 dwarfs within 23 pc: n = {n2}, slope {b2:.3f}, over {xr2[1] - xr2[0]:.2f} levels of distance, rms {rms2:.3f} levels')
g3 = [t for t in stars if giant(t[2]) and 20 <= t[0] <= 400]
n3, b3, rms3, xr3 = fit(g3)
print(f'P3: {"not killed" if b3 > -1.8 else "KILLED"}. K0 giants out to 400 pc: n = {n3}, slope {b3:.3f}')
print(f'P4: {"not killed" if 0.3 <= p4 <= 1.0 else "KILLED"}. rms residual about P1\'s fit: {p4:.3f} levels of light ({p4 / K:.3f} mag)')
