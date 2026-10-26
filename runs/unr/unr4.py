"""UNR run 4: the turn detectors on a recorded tide. Predictions V1–V7 in plans/unr-plan.md, written before the data.
NOAA CO-OPS files (sha256 in the plan, not committed) in a directory given as the argument:
    python3 runs/unr/unr4.py DATA_DIR > runs/unr/unr-run4.txt
"""
import sys
import csv
import math
from datetime import datetime

sys.path.insert(0, "runs/unr")
from unr3 import det_D, det_T

STATIONS = [("9414290", "San Francisco"), ("8443970", "Boston")]
T0 = datetime(2026, 9, 1)
TAS = [30, 100]
TS = [0.01, 0.03]
FT = 3.28084


def look(s):                     # minutes since T0, over 6
    return (datetime.strptime(s.strip(), "%Y-%m-%d %H:%M") - T0).total_seconds() / 360


def series(path):
    out = {}
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            if row[1].strip():
                out[round(look(row[0]))] = round(float(row[1]) * 1000)       # whole millimetres
    return out


def turns_noaa(path):
    with open(path) as f:
        r = csv.reader(f)
        next(r)
        return [(look(row[0]), round(float(row[1]) * 1000), row[2].strip()) for row in r]


def excess(reports, tt):
    return sum(1 for k, q in enumerate(reports, 1) if k > sum(1 for t in tt if t < q))


def first_after(reports, tt):
    """For each NOAA turn, its first report after it and at or before the next turn (None if missed)."""
    out = []
    for i, t in enumerate(tt):
        nxt = tt[i + 1] if i + 1 < len(tt) else math.inf
        q = [r for r in reports if t < r <= nxt]
        out.append(q[0] if q else None)
    return out


def median(v):
    v = sorted(v)
    n = len(v)
    return (v[n // 2] + v[(n - 1) // 2]) / 2 if n else float("nan")


def main(d):
    print("UNR run 4 (plans/unr-plan.md): NOAA verified six-minute water level, September 2026.\n")
    ok = {k: True for k in ("V1", "V2a", "V2b", "V2c", "V3", "V4", "V5", "V6", "V7")}
    ua_ft_changed = ut_stnd_changed = 0
    for st, name in STATIONS:
        m = series(f"{d}/wl_{st}_MLLW_2026.csv")
        s = series(f"{d}/wl_{st}_STND_2026.csv")
        hl = turns_noaa(f"{d}/hl_{st}_MLLW_2026.csv")
        tt = [t for t, _, _ in hl]
        keys = sorted(m)
        shift = {s[k] - m[k] for k in keys}
        print(f"{name} ({st}): {len(keys)} looks, {len(set(range(keys[0], keys[-1] + 1)) - set(keys))} missing; "
              f"STND − MLLW {sorted(shift)} mm; NOAA turns {len(tt)}; MLLW range {min(m.values())}–{max(m.values())} mm")
        N = keys[-1] + 1
        xm = [m.get(i) for i in range(N)]
        xs = [s.get(i) for i in range(N)]
        res = {}
        for rate in (1, 3):
            idx = [i for i in range(0, N, rate) if xm[i] is not None]
            var = {
                "MLLW": xm,
                "STND": xs,
                "feet": [None if v is None else v * FT for v in xm],
                "(x+5m)^3": [None if v is None else float(v + 5000) ** 3 for v in xm],
            }
            lev = {
                "MLLW": [None if v is None else math.log(v / 1000 + 2) for v in xm],
                "STND": [None if v is None else math.log(v / 1000 + 2) for v in xs],
                "feet": [None if v is None else math.log(FT * (v / 1000) + FT * 2) for v in xm],
            }
            out = {}
            for vn, vals in var.items():
                out[("D", vn)] = det_D(vals, idx)
                for Ta in TAS:
                    out[(f"UA {Ta}", vn)] = det_T(vals, idx, Ta)
            for vn, vals in lev.items():
                for T in TS:
                    out[(f"UT {T}", vn)] = det_T(vals, idx, T)
            res[rate] = out
            print(f"  every {6 * rate} min: changed by a map (turns reported, MLLW)")
            for det in ["D"] + [f"UA {a}" for a in TAS] + [f"UT {t}" for t in TS]:
                base = out[(det, "MLLW")]
                row = []
                for vn in ("STND", "feet", "(x+5m)^3"):
                    if (det, vn) in out:
                        ch = out[(det, vn)] != base
                        row.append(f"{vn} {'CHANGED' if ch else 'same'}")
                        if det == "D" and ch:
                            ok["V1"] = False
                        if det.startswith("UA") and vn == "STND" and ch:
                            ok["V2a"] = False
                        if det.startswith("UA") and vn == "feet" and ch:
                            ua_ft_changed += 1
                        if det.startswith("UT") and vn == "feet" and ch:
                            ok["V2b"] = False
                        if det.startswith("UT") and vn == "STND" and ch:
                            ut_stnd_changed += 1
                print(f"    {det:8s} {len(base):4d}   " + "   ".join(row))
            print(f"  every {6 * rate} min: excess, missed, lateness in looks (from the last NOAA turn) against {len(tt)} NOAA turns")
            for det in ["D"] + [f"UA {a}" for a in TAS] + [f"UT {t}" for t in TS]:
                rep = out[(det, "MLLW")]
                ex = excess(rep, tt)
                fa = first_after(rep, tt)
                miss = sum(q is None for q in fa)
                lat = [q - max([t for t in tt if t < q]) for q in rep if any(t < q for t in tt)]
                print(f"    {det:8s} reports {len(rep):4d}  excess {ex:4d}  missed {miss:3d}  "
                      f"lateness median {median(lat):6.2f}  (6-min looks)")
                res[(rate, det)] = (ex, fa, lat)
        ex6 = res[(1, "D")][0]
        ex18 = res[(3, "D")][0]
        if not (ex6 > 0 and res[(1, "UA 100")][0] == 0 and res[(1, "UT 0.03")][0] == 0):
            ok["V3"] = False
        med = median(res[(1, "UA 100")][2])
        if not (5 <= med <= 15):
            ok["V4"] = False
        if ex18 > ex6 / 4:
            ok["V5"] = False
        print(f"  V3: D's excess {ex6}, UA 100's {res[(1, 'UA 100')][0]}, UT 0.03's {res[(1, 'UT 0.03')][0]}")
        print(f"  V4: UA 100's median lateness {med:.2f} looks")
        print(f"  V5: D's excess at 18 min {ex18} against {ex6} at 6 min")
        fa = res[(1, "UA 100")][1]
        for i, q in enumerate(fa):
            if q is None:
                rng = [abs(hl[i][1] - hl[j][1]) for j in (i - 1, i + 1) if 0 <= j < len(hl)]
                print(f"  V6: missed {hl[i][2]:2s} at look {hl[i][0]:.1f}, {hl[i][1]} mm, ranges to neighbours {rng} mm")
                if min(rng) >= 250:
                    ok["V6"] = False
        f6, f18 = res[(1, "UA 100")][1], res[(3, "UA 100")][1]
        both = [(a, b) for a, b in zip(f6, f18) if a is not None and b is not None]
        near = sum(abs(a - b) <= 3 for a, b in both)
        print(f"  V7: reported at both rates {len(both)}, within 18 min {near} ({near / len(both):.3f}); "
              f"largest gap {max(abs(a - b) for a, b in both)} looks\n")
        if near < 0.9 * len(both):
            ok["V7"] = False
    if ua_ft_changed == 0:
        ok["V2a"] = False
    if ut_stnd_changed == 0:
        ok["V2c"] = False
    print(f"UA changed by feet in {ua_ft_changed} of 8 cases; UT changed by the datum in {ut_stnd_changed} of 8")
    v2 = ok["V2a"] and ok["V2b"] and ok["V2c"]
    for k in ("V1",):
        print(f"{k} {'not killed' if ok[k] else 'KILLED'}")
    print(f"V2 {'not killed' if v2 else 'KILLED'} (UA by the datum and feet {ok['V2a']}, UT by feet {ok['V2b']}, "
          f"UT by the datum {ok['V2c']})")
    for k in ("V3", "V4", "V5", "V6", "V7"):
        print(f"{k} {'not killed' if ok[k] else 'KILLED'}")


if __name__ == "__main__":
    main(sys.argv[1])
