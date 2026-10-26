"""UNR run 6: the persistence rule, calibrated on September 2026 (run 5's data) and tested on August 2026.
Rule and kill conditions in plans/unr-plan.md ("Run 6: predictions"). Three steps, each committed before the next:
    python3 runs/unr/unr6.py calibrate SEPT_DIR > runs/unr/unr-run6-calibrate.txt
    python3 runs/unr/unr6.py predict AUG_DIR   > runs/unr/unr-run6-predict.txt
    python3 runs/unr/unr6.py run AUG_DIR       > runs/unr/unr-run6.txt
"""
import sys
import csv
import math
from datetime import datetime

sys.path.insert(0, "runs/unr")
from unr3 import det_D

STATIONS = [("1612340", "Honolulu"), ("9447130", "Seattle"), ("9410660", "Los Angeles"),
            ("9414290", "San Francisco"), ("8443970", "Boston")]
GRID = [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30]
GAP = 30
MONTHS = {"sep": (datetime(2026, 9, 1), 30), "aug": (datetime(2026, 8, 1), 31)}


def minute(s, t0):
    return int((datetime.strptime(s.strip(), "%Y-%m-%d %H:%M") - t0).total_seconds() // 60)


def series(path, t0):
    out = {}
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if len(row) > 1 and row[1].strip():
                out[minute(row[0], t0)] = round(float(row[1]) * 1000)
    return out


def load(d, st, month):
    t0, days = MONTHS[month]
    n = days * 1440
    x = series(f"{d}/om_{st}.csv", t0)
    p = series(f"{d}/pr_{st}.csv", t0)
    with open(f"{d}/hl_{st}.csv") as f:
        r = csv.reader(f)
        next(r)
        tt = [(minute(row[0], t0), round(float(row[1]) * 1000)) for row in r]
    big, start = [], None
    for m in range(n + 1):
        if m < n and m not in x:
            start = m if start is None else start
        elif start is not None:
            if m - start > GAP:
                big.append((start, m - 1))
            start = None
    t = [a for a, _ in tt]
    scored = [k for k in range(1, len(t) - 1)
              if not any(g0 <= t[k + 1] and g1 >= t[k - 1] for g0, g1 in big)]
    return x, p, tt, scored


def sd(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1))


def q_of(res, r):
    """Share of places where three consecutive look-to-look increments share a sign, pooled over offsets."""
    hit = tot = 0
    keys = sorted(res)
    for o in range(r):
        v = [res[m] for m in keys if m % r == o]
        e = [b - a for a, b in zip(v, v[1:])]
        for k in range(len(e) - 2):
            tot += 1
            if (e[k] > 0 and e[k + 1] > 0 and e[k + 2] > 0) or (e[k] < 0 and e[k + 1] < 0 and e[k + 2] < 0):
                hit += 1
    return hit / tot


def rule(x, p, tt, scored):
    res = {m: x[m] - p[m] for m in x if m in p}
    out = {}
    tmin = min(tt[k + 1][0] - tt[k][0] for k in scored)
    for r in GRID:
        s = sd([res[m + r] - res[m] for m in res if m + r in res])
        q = q_of(res, r)
        Z = 0.0
        for k in scored:
            legs = [abs(b[1] - a[1]) / 2 * (math.pi / (b[0] - a[0])) ** 2
                    for a, b in ((tt[k - 1], tt[k]), (tt[k], tt[k + 1]))]
            kap = sum(legs) / 2
            tau = tt[k + 1][0] - tt[k][0]
            Z += min(2 * s / (kap * r * r), tau / r)
        out[r] = (q, s, q * Z, 3 * r < tmin)
    return out, tmin


def exact_at(x, tt, scored, r):
    t = [a for a, _ in tt]
    keys = sorted(x)
    good = 0
    for o in range(r):
        rep = det_D(x, [m for m in keys if m % r == o])
        good += all(sum(1 for q in rep if t[k] < q <= t[k + 1]) == 1 for k in scored)
    return good == r


def calibrate(d):
    print("UNR run 6, calibration on September 2026 (run 5's record; first interval left out at every station).\n")
    pts = []
    for st, name in STATIONS:
        x, p, tt, scored = load(d, st, "sep")
        R, tmin = rule(x, p, tt, scored)
        print(f"{name} ({st}): {len(scored)} intervals scored, τ_min {tmin} min")
        for r in GRID:
            q, s, E, ok_hi = R[r]
            ex = exact_at(x, tt, scored, r)
            pts.append((E, ex, ok_hi, name, r))
            print(f"  r {r:2d}: q {q:.4f}  s {s:5.1f}  E {E:10.4g}  3r<τ_min {ok_hi}  measured exact {ex}")
        print()
    use = [(E, ex) for E, ex, hi, _, _ in pts if hi]
    exE = [E for E, ex in use if ex]
    inE = [E for E, ex in use if not ex]
    if exE and inE and max(exE) < min(inE):
        c = math.sqrt(max(exE) * min(inE))
        how = "separated"
    else:
        vals = sorted(set(E for E, _ in use))
        cands = [math.sqrt(a * b) for a, b in zip(vals, vals[1:])]
        def miss(c):
            return sum((E < c) != ex for E, ex in use)
        c = min(cands, key=lambda c: (miss(c), c))
        how = f"not separated; {miss(c)} misclassified"
    wrong = [(n, r) for E, ex, hi, n, r in pts if hi and (E < c) != ex]
    print(f"c = {c:.6g} ({how}); largest E exact {max(exE):.4g}, smallest E inexact {min(inE):.4g}")
    print(f"misclassified (station, r): {wrong}")


def cfile():
    for line in open("runs/unr/unr-run6-calibrate.txt"):
        if line.startswith("c = "):
            return float(line.split()[2])


def predict(d):
    c = cfile()
    print(f"UNR run 6, August 2026 predicted from its own record with c = {c:.6g} from September (D not run).\n")
    for st, name in STATIONS:
        x, p, tt, scored = load(d, st, "aug")
        R, tmin = rule(x, p, tt, scored)
        pred = [r for r in GRID if R[r][2] < c and R[r][3]]
        print(f"{name} ({st}): {len(scored)} intervals scored, τ_min {tmin} min")
        print("  E_r: " + "  ".join(f"{r}:{R[r][2]:.3g}" for r in GRID))
        print(f"  predicted exact at {pred}\n")


def run(d):
    pred = {}
    cur = None
    for line in open("runs/unr/unr-run6-predict.txt"):
        if "(" in line and "):" in line and line[0] != " ":
            cur = line.split("(")[1].split(")")[0]
        if "predicted exact at" in line:
            pred[cur] = eval(line.split("at", 1)[1])
    print("UNR run 6: D on August 2026, every r minutes from every offset, first interval left out.\n")
    ok = {"X1": True, "X2": True, "X3": True}
    for st, name in STATIONS:
        x, p, tt, scored = load(d, st, "aug")
        meas = [r for r in GRID if exact_at(x, tt, scored, r)]
        P = pred[st]
        agree = sum((r in meas) == (r in P) for r in GRID)
        runs = sum(1 for i, r in enumerate(GRID) if r in meas and (i == 0 or GRID[i - 1] not in meas))
        if not P:
            x1 = not meas
        else:
            x1 = bool(meas) and P[0] / 2 <= meas[0] <= P[0] * 2
        ok["X1"] &= x1
        ok["X2"] &= agree >= 11
        ok["X3"] &= runs <= 1
        print(f"{name} ({st}): predicted {P}; measured {meas}; agree at {agree} of 13; "
              f"{runs} unbroken run{'s' if runs != 1 else ''}; X1 {'held' if x1 else 'failed'}")
    print()
    for k, v in ok.items():
        print(f"{k} {'not killed' if v else 'KILLED'}")


if __name__ == "__main__":
    {"calibrate": calibrate, "predict": predict, "run": run}[sys.argv[1]](sys.argv[2])
