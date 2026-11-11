# CHS run 2: C6' and C7'. plans/chs-plan.md.
import statistics
from mpmath import mp, mpf, atan, pi
starts = ["0.3", "1.7", "0.428571", "2.2", "0.61"]
def orbit(s0, prec, steps):
    mp.prec = prec; s = mpf(s0); out = []
    for _ in range(steps):
        d = 1 - s * s
        s = abs(2 * s / d) if d != 0 else mpf(10) ** 30
        out.append(+s)
    return out
good = True; meds = []; ps = [24, 53, 113, 200]
for p in ps:
    steps = p + 40; firsts = []
    for s0 in starts:
        ref = orbit(s0, 3000, steps); low = orbit(s0, p, steps)
        mp.prec = 300
        firsts.append(next((i + 1 for i in range(steps) if abs(2 * atan(ref[i]) / pi - 2 * atan(low[i]) / pi) > mpf("0.1")), None))
    inb = all(f is not None and p - 4 <= f <= p + 8 for f in firsts)
    good = good and inb; meds.append(statistics.median(firsts))
    print(f"  p = {p}: first steps apart {firsts}, median {meds[-1]}, band {p - 4}..{p + 8}: {'ok' if inb else 'FAIL'}")
n = len(ps); mx = sum(ps) / n; my = sum(meds) / n
slope = sum((x - mx) * (y - my) for x, y in zip(ps, meds)) / sum((x - mx) ** 2 for x in ps)
print(f"  slope of the medians against p: {slope:.4f}")
good = good and abs(slope - 1) < 0.02
print(f"C6': {'not killed' if good else 'KILLED'}")
print(f"C7': {'not killed' if good else 'KILLED'} (C5 not killed in run 1)")
