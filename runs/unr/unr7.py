"""UNR run 7: the band rule, fitted on September and August 2026 (runs 5–6) and tested on July 2026 at ten stations.
Rule and kill conditions in plans/unr-plan.md ("Run 7: predictions"). Three steps, each committed before the next:
    python3 runs/unr/unr7.py fit SEPT_DIR AUG_DIR > runs/unr/unr-run7-fit.txt
    python3 runs/unr/unr7.py predict JUL_DIR      > runs/unr/unr-run7-predict.txt
    python3 runs/unr/unr7.py run JUL_DIR          > runs/unr/unr-run7.txt
"""
import sys
import math
from datetime import datetime

sys.path.insert(0, "runs/unr")
import unr6
from unr6 import load, exact_at, sd, GRID

unr6.MONTHS["jul"] = (datetime(2026, 7, 1), 31)
OLD = unr6.STATIONS
NEW = [("8518750", "The Battery"), ("8665530", "Charleston"), ("8724580", "Key West"),
       ("9410170", "San Diego"), ("9452210", "Juneau")]


def smooth(res, n, w):
    """Running mean over w + 1 minutes, kept where 80% of the window is present."""
    s, c = [0.0] * (n + 1), [0] * (n + 1)
    for m in range(n):
        v = res.get(m)
        s[m + 1] = s[m] + (v if v is not None else 0)
        c[m + 1] = c[m] + (v is not None)
    out, h = {}, w // 2
    for m in res:
        a, b = max(0, m - h), min(n, m + h + 1)
        if c[b] - c[a] > 0.8 * (w + 1):
            out[m] = (s[b] - s[a]) / (c[b] - c[a])
    return out


def B_of(x, p, tt, scored, n):
    res = {m: x[m] - p[m] for m in x if m in p}
    m10, m60 = smooth(res, n, 10), smooth(res, n, 60)
    band = sd([m10[m] - m60[m] for m in res if m in m10 and m in m60])
    kap = sorted(sum(abs(b[1] - a[1]) / 2 * (math.pi / (b[0] - a[0])) ** 2
                     for a, b in ((tt[k - 1], tt[k]), (tt[k], tt[k + 1]))) / 2 for k in scored)
    tmin = min(tt[k + 1][0] - tt[k][0] for k in scored)
    return band / kap[len(kap) // 2], band, kap[len(kap) // 2], tmin


def nearest(r):
    return min(GRID, key=lambda g: abs(math.log(g / r)))


def fit(sept, aug):
    print("UNR run 7, the rule fitted on September and August 2026 (runs 5–6's records).\n")
    rows = []
    for d, month in ((sept, "sep"), (aug, "aug")):
        n = unr6.MONTHS[month][1] * 1440
        for st, name in OLD:
            x, p, tt, scored = load(d, st, month)
            B, band, kap, tmin = B_of(x, p, tt, scored, n)
            meas = [r for r in GRID if exact_at(x, tt, scored, r)]
            rows.append((B, meas[0] if meas else None))
            print(f"  {name:13s} {month}: band {band:5.2f} mm  κ_med {kap:.4f}  B {B:7.1f}  smallest exact {meas[0] if meas else 'never'}")
    ex = [B for B, r in rows if r is not None]
    nv = [B for B, r in rows if r is None]
    Bstar = math.sqrt(max(ex) * min(nv))
    a = math.exp(sum(math.log(r / B) for B, r in rows if r is not None) / len(ex))
    sep = max(ex) < min(nv)
    print(f"\nB* = {Bstar:.6g} ({'separated' if sep else 'NOT separated'}: largest exact {max(ex):.4g}, smallest never {min(nv):.4g})")
    print(f"a = {a:.6g}")


def params():
    for line in open("runs/unr/unr-run7-fit.txt"):
        if line.startswith("B* = "):
            Bs = float(line.split()[2])
        if line.startswith("a = "):
            a = float(line.split()[2])
    return Bs, a


def predict(d):
    Bs, a = params()
    n = unr6.MONTHS["jul"][1] * 1440
    print(f"UNR run 7, July 2026 predicted from its own record with B* = {Bs:.6g}, a = {a:.6g} (D not run).\n")
    for st, name in OLD + NEW:
        try:
            x, p, tt, scored = load(d, st, "jul")
        except FileNotFoundError:
            print(f"{name} ({st}): dropped (no data)\n")
            continue
        B, band, kap, tmin = B_of(x, p, tt, scored, n)
        if B > Bs:
            pred = []
        else:
            r0 = nearest(a * B)
            pred = [r for r in GRID if r >= r0 and 3 * r < tmin]
        print(f"{name} ({st}): {len(scored)} intervals scored; band {band:.2f} mm, κ_med {kap:.4f}, B {B:.1f}, τ_min {tmin}")
        print(f"  predicted exact at {pred}\n")


def run(d):
    pred, Bv, cur = {}, {}, None
    for line in open("runs/unr/unr-run7-predict.txt"):
        if "(" in line and "):" in line and line[0] != " ":
            cur = line.split("(")[1].split(")")[0]
            if ", B " in line:
                Bv[cur] = float(line.split(", B ")[1].split(",")[0])
        if "predicted exact at" in line:
            pred[cur] = eval(line.split("at", 1)[1])
    print("UNR run 7: D on July 2026, every r minutes from every offset, first interval left out.\n")
    cls = y2 = y3 = 0
    y2n = 0
    ranks = []
    for st, name in OLD + NEW:
        if st not in pred:
            continue
        x, p, tt, scored = load(d, st, "jul")
        meas = [r for r in GRID if exact_at(x, tt, scored, r)]
        P = pred[st]
        right = bool(meas) == bool(P)
        cls += right
        within = None
        if meas and P:
            y2n += 1
            within = P[0] / 2 <= meas[0] <= P[0] * 2
            y2 += within
        runs = sum(1 for i, r in enumerate(GRID) if r in meas and (i == 0 or GRID[i - 1] not in meas))
        y3 += runs <= 1
        ranks.append((Bv[st], meas[0] if meas else 1e9))
        print(f"{name} ({st}): B {Bv[st]:.1f}; predicted {P}; measured {meas}; class {'right' if right else 'wrong'}"
              + (f"; smallest within 2× {within}" if within is not None else ""))
    k = len(ranks)

    def rk(v):
        o = sorted(range(k), key=lambda i: v[i])
        r = [0.0] * k
        i = 0
        while i < k:
            j = i
            while j + 1 < k and v[o[j + 1]] == v[o[i]]:
                j += 1
            for t in range(i, j + 1):
                r[o[t]] = (i + j) / 2
            i = j + 1
        return r
    ra, rb = rk([a for a, _ in ranks]), rk([b for _, b in ranks])
    ma, mb = sum(ra) / k, sum(rb) / k
    rho = sum((u - ma) * (w - mb) for u, w in zip(ra, rb)) / math.sqrt(
        sum((u - ma) ** 2 for u in ra) * sum((w - mb) ** 2 for w in rb))
    print(f"\nclass right {cls} of {k}; within 2× {y2} of {y2n}; one unbroken run {y3} of {k}; Spearman {rho:.3f}")
    print(f"Y1 {'not killed' if cls >= 9 else 'KILLED'}")
    print(f"Y2 {'not killed' if y2n - y2 <= 2 else 'KILLED'}")
    print(f"Y3 {'not killed' if y3 == k else 'KILLED'}")
    print(f"Y4 {'not killed' if rho >= 0.6 else 'KILLED'}")


if __name__ == "__main__":
    if sys.argv[1] == "fit":
        fit(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "predict":
        predict(sys.argv[2])
    else:
        run(sys.argv[2])
