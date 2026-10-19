"""LTH run 2: Cosmicflows-4, method against method (plans/lth-plan.md, P5, P6).

Usage: python3 -I runs/lth/lth2.py path/to/table2.dat   (J/ApJ/944/94; not committed, sha256 in the plan)
"""
import sys, math, itertools, statistics as st

# (label, value bytes, error bytes), 1-based inclusive, from the ReadMe
COLS = [("SNIa", (42, 47), (49, 52)), ("TF", (54, 59), (61, 64)), ("FP", (66, 71), (73, 76)),
        ("SBF", (78, 83), (85, 89)), ("SNII", (91, 96), (98, 101)), ("TRGB", (103, 107), (109, 112)),
        ("Ceph", (114, 119), (121, 125)), ("Maser", (127, 131), (133, 136))]

def field(line, a, b):
    s = line[a - 1:b].strip()
    return float(s) if s else None

def load(path):
    rows = []
    for line in open(path):
        r = {}
        for lab, (a, b), (c, d) in COLS:
            v, e = field(line, a, b), field(line, c, d)
            if v is not None and e is not None:
                r[lab] = (v, e)
        rows.append(r)
    return rows

def fit(x, y):
    n = len(x); mx, my = st.mean(x), st.mean(y)
    sxx = sum((xi - mx) ** 2 for xi in x)
    b = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / sxx
    a = my - b * mx
    res = [yi - a - b * xi for xi, yi in zip(x, y)]
    s2 = sum(r * r for r in res) / (n - 2)
    return b, math.sqrt(s2 / sxx)

def main(path):
    rows = load(path)
    print(f"{len(rows)} galaxies")
    k5 = k6 = 0
    print("pair         n   mean dmu   slope (mag/mag) +- se   |slope|/se   var/mean(eA2+eB2)")
    for A, B in itertools.combinations([c[0] for c in COLS], 2):
        both = [(r[A], r[B]) for r in rows if A in r and B in r]
        if len(both) < 30:
            continue
        d = [a[0] - b[0] for a, b in both]
        m = [(a[0] + b[0]) / 2 for a, b in both]
        ee = st.mean([a[1] ** 2 + b[1] ** 2 for a, b in both])
        slope, se = fit(m, d)
        ratio = st.variance(d) / ee
        kill5 = abs(slope) > 3 * se and abs(slope) > 0.02
        kill6 = not (0.5 <= ratio <= 2)
        k5 += kill5; k6 += kill6
        print(f"{A:5s}-{B:5s} {len(both):5d}  {st.mean(d):+7.3f}   {slope:+8.4f} +- {se:.4f}   {abs(slope)/se:6.2f}"
              f"{' KILL' if kill5 else ''}      {ratio:6.3f}{' KILL' if kill6 else ''}")
    print(f"P5 {'KILLED' if k5 else 'not killed'} ({k5} pairs past the kill line)")
    print(f"P6 {'KILLED' if k6 else 'not killed'} ({k6} pairs outside 0.5-2)")

if __name__ == "__main__":
    main(sys.argv[1])
