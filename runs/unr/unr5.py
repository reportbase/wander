"""UNR run 5: when the order-only detector is exact, predicted from the record and then measured.
Predictions W1–W4 and T1–T4 in plans/unr-plan.md, written before the data. NOAA files (sha256 in the plan, not committed)
in DATA_DIR. Two steps, the first committed before the second is run:
    python3 runs/unr/unr5.py predict DATA_DIR > runs/unr/unr-run5-predict.txt
    python3 runs/unr/unr5.py run DATA_DIR > runs/unr/unr-run5.txt
"""
import sys
import csv
import math
from datetime import datetime

sys.path.insert(0, "runs/unr")
from unr3 import det_D, det_T

STATIONS = [("1612340", "Honolulu"), ("9447130", "Seattle"), ("9410660", "Los Angeles"),
            ("9414290", "San Francisco"), ("8443970", "Boston")]
GRID = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30]
T0 = datetime(2026, 9, 1)
M = 3
GAP = 30


def minute(s):
    return int((datetime.strptime(s.strip(), "%Y-%m-%d %H:%M") - T0).total_seconds() // 60)


def series(path):
    out = {}
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) > 1 and row[1].strip():
                out[minute(row[0])] = round(float(row[1]) * 1000)
    return out


def turns(path):
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        return [(minute(row[0]), round(float(row[1]) * 1000)) for row in r]


def gaps(have, n):
    out, start = [], None
    for m in range(n + 1):
        if m < n and m not in have:
            start = m if start is None else start
        elif start is not None:
            out.append((start, m - 1))
            start = None
    return [g for g in out if g[1] - g[0] + 1 > GAP]


def load(d, st):
    x = series(f"{d}/om_{st}.csv")
    p = series(f"{d}/pr_{st}.csv")
    tt = turns(f"{d}/hl_{st}.csv")
    big = gaps(x, 43200)
    t = [a for a, _ in tt]

    def clear(a, b):
        return not any(g0 <= b and g1 >= a for g0, g1 in big)
    scored = []
    for k in range(len(t) - 1):
        prev = t[k - 1] if k >= 1 else 0
        if clear(prev, t[k + 1]):
            scored.append(k)
    return x, p, tt, big, scored


def sd(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1))


def predict(d):
    print("UNR run 5, the prediction from the record alone (D not run). r in minutes; s_r in mm; κ in mm/min².\n")
    for st, name in STATIONS:
        x, p, tt, big, scored = load(d, st)
        res = {m: x[m] - p[m] for m in x if m in p}
        s = {r: sd([res[m + r] - res[m] for m in res if m + r in res]) for r in GRID}
        kap, tau = [], []
        for k in scored:
            tau.append(tt[k + 1][0] - tt[k][0])
            if k >= 1:
                legs = []
                for a, b in ((tt[k - 1], tt[k]), (tt[k], tt[k + 1])):
                    R, T = abs(b[1] - a[1]), b[0] - a[0]
                    legs.append(R / 2 * (math.pi / T) ** 2)
                kap.append(sum(legs) / 2)
        kmin, tmin = min(kap), min(tau)
        zone = {r: 2 * s[r] / (kmin * r * r) for r in GRID}
        rlow = next((r for r in GRID if zone[r] <= M), None)
        rhigh = max((r for r in GRID if 3 * r < tmin), default=None)
        print(f"{name} ({st}): intervals scored {len(scored)} of {len(tt) - 1}; long gaps {len(big)}")
        print("  s_r: " + "  ".join(f"{r}:{s[r]:.1f}" for r in GRID))
        print("  flat zone 2s_r/(κ_min r²): " + "  ".join(f"{r}:{zone[r]:.2g}" for r in GRID))
        print(f"  κ_min {kmin:.4g} (median {sorted(kap)[len(kap) // 2]:.4g}); τ_min {tmin} min")
        print(f"  r_low {rlow}, r_high {rhigh}; predicted exact at "
              f"{[r for r in GRID if rlow is not None and rhigh is not None and rlow <= r <= rhigh]}\n")


def exact_at(x, tt, scored, r):
    """For every offset, D's reports per scored interval; exact when all are 1. Returns (exact offsets, worst counts)."""
    t = [a for a, _ in tt]
    keys = sorted(x)
    ok, bad = 0, {}
    for o in range(r):
        idx = [m for m in keys if m % r == o]
        rep = det_D(x, idx)
        fine = True
        for k in scored:
            c = sum(1 for q in rep if t[k] < q <= t[k + 1])
            if c != 1:
                fine = False
                bad[c] = bad.get(c, 0) + 1
        ok += fine
    return ok, bad


def windows():
    """r_low and r_high per station, read back from the committed prediction."""
    out, cur = {}, None
    for line in open("runs/unr/unr-run5-predict.txt"):
        if "(" in line and line[0] != " " and "):" in line:
            cur = line.split("(")[1].split(")")[0]
        if line.strip().startswith("r_low"):
            a, b = line.split(";")[0].replace("r_low", "").split(", r_high")
            out[cur] = (None if a.strip() == "None" else int(a), None if b.strip() == "None" else int(b))
    return out


def run(d):
    print("UNR run 5: D (order only, M = 3) on one-minute water level, every r minutes from every offset.\n")
    win = windows()
    ok = {"W1": True, "W2": True, "W3": True, "W4": True}
    for st, name in STATIONS:
        x, p, tt, big, scored = load(d, st)
        exact = []
        print(f"{name} ({st}): {len(scored)} intervals scored; predicted r_low {win[st][0]}, r_high {win[st][1]}")
        for r in GRID:
            good, bad = exact_at(x, tt, scored, r)
            if good == r:
                exact.append(r)
            print(f"  r {r:2d}: exact at {good:2d} of {r:2d} offsets; intervals off by count {dict(sorted(bad.items()))}")
        lo, hi = win[st]
        empty = lo is None or hi is None or lo > hi
        runs = sum(1 for i, r in enumerate(GRID) if r in exact and (i == 0 or GRID[i - 1] not in exact))
        if empty:
            ok["W4"] &= not exact
        else:
            if not exact or not (lo / 2 <= exact[0] <= lo * 2):
                ok["W1"] = False
            if hi < 30:
                ok["W2"] &= bool(exact) and hi / 2 <= exact[-1] <= hi * 2
            else:
                ok["W2"] &= 30 in exact
        ok["W3"] &= runs <= 1
        print(f"  measured exact at {exact} ({runs} unbroken run{'s' if runs != 1 else ''})\n")
    for k, v in ok.items():
        print(f"{k} {'not killed' if v else 'KILLED'}")
    print()


def temperature(d):
    print("Side prediction: Boston air temperature, September 2026, six-minute.")
    c10 = {}
    with open(f"{d}/at_8443970.csv") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) > 1 and row[1].strip():
                c10[minute(row[0]) // 6] = round(float(row[1]) * 10)
    n = max(c10) + 1
    C = [c10.get(i) for i in range(n)]
    F = [None if v is None else 18 * v + 3200 for v in C]              # °F × 100, exact
    K = [None if v is None else 10 * v + 27315 for v in C]             # K × 100
    R = [None if k is None else 18 * k for k in K]                     # °R × 1000
    out = {}
    for rate in (1, 3):
        idx = [i for i in range(0, n, rate) if C[i] is not None]
        t1 = det_D(C, idx) == det_D(F, idx)
        t2 = det_T(C, idx, 5) != det_T(F, idx, 50)
        lK = [None if v is None else math.log(v / 100) for v in K]
        lR = [None if v is None else math.log(v / 1000) for v in R]
        t3 = det_T(lK, idx, 0.003) == det_T(lR, idx, 0.003)
        lC = [None if v is None else math.log(v / 10 + 50) for v in C]
        lF = [None if v is None else math.log(v / 100 + 50) for v in F]
        t4 = det_T(lC, idx, 0.003) != det_T(lF, idx, 0.003)
        print(f"  every {6 * rate} min: looks {len(idx)}; D turns {len(det_D(C, idx))}, same in °F {t1}; "
              f"UA 0.5 changed {t2}; UT on K and °R same {t3}; UT on reading + 50 changed {t4}")
        out[rate] = (t1, t2, t3, t4)
    print(f"  T1 {'not killed' if all(o[0] for o in out.values()) else 'KILLED'}; "
          f"T2 {'not killed' if any(o[1] for o in out.values()) else 'KILLED'}; "
          f"T3 {'not killed' if all(o[2] for o in out.values()) else 'KILLED'}; "
          f"T4 {'not killed' if any(o[3] for o in out.values()) else 'KILLED'}")


if __name__ == "__main__":
    if sys.argv[1] == "predict":
        predict(sys.argv[2])
    else:
        run(sys.argv[2])
        temperature(sys.argv[2])
