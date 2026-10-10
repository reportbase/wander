"""GCN run 1 (plans/gcn-plan.md): star counts within 100 pc, by kind, on the Gaia Catalogue of Nearby Stars.
Usage: python3 -I plans/gcn/gcn.py <path to the GCNS table1c TSV from VizieR>"""
import bisect, hashlib, math, sys
SHA = '73b63a058a7e2afce4b655290d030eb1daa101aeabe62730c007deeab3e67c6c'
raw = open(sys.argv[1], 'rb').read()
assert hashlib.sha256(raw).hexdigest() == SHA, 'the data is not the file the plan names'
K = math.log2(10) / 2.5
Rm = [-0.8676661490, -0.1980763734, 0.4559837762]   # J2000 equatorial -> galactic, third row (gives b)
def gal_b(ra_d, dec_d):
    a, d = math.radians(ra_d), math.radians(dec_d)
    return math.degrees(math.asin(Rm[0] * math.cos(d) * math.cos(a) + Rm[1] * math.cos(d) * math.sin(a) + Rm[2] * math.sin(d)))
rows = [l for l in raw.decode('utf-8').split('\n') if l.strip() and not l.startswith('#')]
head = rows[0].split('\t'); assert head == ['RA_ICRS', 'DE_ICRS', 'Plx', 'e_Plx', 'Gmag', 'BPmag', 'RPmag', 'RUWE', 'GCNSprob'], head
total = nocol = 0; stars = []   # (d, G, M_G, bp_rp, b, ruwe) after parallax cuts
for l in rows[3:]:
    f = [x.strip() for x in l.split('\t')]; total += 1
    if not f[5] or not f[6] or not f[4] or not f[7]: nocol += 1; continue
    plx, eplx = float(f[2]), float(f[3])
    if plx < 10 or plx / eplx < 10: continue
    G = float(f[4]); c = float(f[5]) - float(f[6])
    stars.append((1000 / plx, G, G + 5 + 5 * math.log10(plx / 1000), c, gal_b(float(f[0]), float(f[1])), float(f[7])))
good = [s for s in stars if s[5] < 1.4]
def on_band(s): return 0.5 <= s[3] <= 3.2 and abs(s[2] - (3.4 * s[3] + 1.9)) <= 1.5
KINDS = [('G', 0.75, 0.95), ('K', 1.0, 1.5), ('early M', 2.0, 2.5), ('late M', 2.5, 3.0)]
def in_kind(s, lo, hi): return lo <= s[3] < hi
def slope(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (c - my) for a, c in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
def slope_dist(ds, lo=25, hi=100, step=0.05):
    v = sorted(math.log2(d) for d in ds); xs, ys = [], []; x = math.log2(lo)
    while x <= math.log2(hi) + 1e-9:
        n = bisect.bisect_right(v, x)
        if n: xs.append(x); ys.append(math.log2(n))
        x += step
    return slope(xs, ys)
def slope_light(gs, lo, hi):   # N brighter than G against light -K*G; sign turned so an even spread gives +1.5
    v = sorted(gs); xs, ys = [], []; g = lo
    while g <= hi + 1e-9:
        n = bisect.bisect_right(v, g)
        if n: xs.append(-K * g); ys.append(math.log2(n))
        g += 0.1
    return -slope(xs, ys)
print(f'{total} GCNS rows; {nocol} with no G, BP, RP or RUWE dropped; parallax >= 10 mas and >= 10 sigma: {len(stars)}; ruwe < 1.4: {len(good)}')
band = [s for s in good if on_band(s)]
out, p1ok, p3ok, p4ok, together = [], True, True, True, []
for name, lo, hi in KINDS:
    kind = [s for s in band if in_kind(s, lo, hi)]; together += kind
    s1 = slope_dist([s[0] for s in kind])
    p1ok &= 2.85 <= s1 <= 3.05
    mg = sorted(s[2] for s in kind); gmax = mg[int(0.01 * (len(mg) - 1))] + 5
    lit = [s[1] for s in kind if s[1] <= gmax]
    s3 = slope_light([s[1] for s in kind], gmax - 3, gmax)
    p3ok &= 1.35 <= s3 <= 1.55
    near = [s for s in good if s[0] <= 50 and in_kind(s, lo, hi)]
    off = sum(1 for s in near if not on_band(s)) / len(near)
    p4ok &= off < 0.03
    n25 = sum(1 for s in kind if 25 <= s[0])
    out.append(f'  {name:8s} bp_rp {lo}-{hi}: {len(kind)} on the band within 100 pc ({n25} past 25 pc); by distance {s1:.3f}; '
               f'G_max {gmax:.2f} ({len(lit)} brighter), by light {s3:.3f}; within 50 pc {len(near)}, off the band {100 * off:.2f}%')
plane = [s[0] for s in together if abs(s[4]) < 15]; poles = [s[0] for s in together if abs(s[4]) > 45]
sp, sq = slope_dist(plane), slope_dist(poles)
print(f'P1: {"not killed" if p1ok else "KILLED"}. each kind, 25-100 pc, slope of log2 N(<d) in [2.85, 3.05] (3 for an even spread)')
print(f'P2: {"not killed" if 0.03 <= sp - sq <= 0.3 else "KILLED"}. four kinds, 25-100 pc: plane (|b| < 15) {sp:.3f} ({len(plane)}), poles (|b| > 45) {sq:.3f} ({len(poles)}), difference {sp - sq:.3f}')
print(f'P3: {"not killed" if p3ok else "KILLED"}. each kind, G_max - 3 to G_max, levels of number per level of light in [1.35, 1.55] (1.5 for an even spread)')
print(f'P4: {"not killed" if p4ok else "KILLED"}. within 50 pc, under 3% of each colour range off the band')
print('\n'.join(out))
