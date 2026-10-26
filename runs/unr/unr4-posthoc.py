"""UNR run 4, post hoc (after the run): where D's extra reports fall at San Francisco, a per-turn count of
excess, and what the large 6-min/18-min gaps of UA 100 have in common.
    python3 runs/unr/unr4-posthoc.py DATA_DIR > runs/unr/unr4-posthoc.txt
"""
import sys
sys.path.insert(0, "runs/unr")
from unr3 import det_D, det_T
from unr4 import series, turns_noaa, first_after


def per_interval(rep, tt, end):
    """Reports between each pair of NOAA turns (and before the first): a count per interval, 1 the right one."""
    bounds = [-1e9] + tt + [end]
    return [sum(1 for q in rep if a < q <= b) for a, b in zip(bounds[:-1], bounds[1:])]


def main(d):
    for st, name in [("9414290", "San Francisco"), ("8443970", "Boston")]:
        m = series(f"{d}/wl_{st}_MLLW_2026.csv")
        hl = turns_noaa(f"{d}/hl_{st}_MLLW_2026.csv")
        tt = [t for t, _, _ in hl]
        N = max(m) + 1
        xm = [m[i] for i in range(N)]
        print(f"{name}")
        for rate in (1, 3):
            idx = list(range(0, N, rate))
            rep = det_D(xm, idx)
            c = per_interval(rep, tt, N)
            print(f"  D every {6 * rate} min: reports per interval between NOAA turns: "
                  f"0 in {c.count(0)}, 1 in {c.count(1)}, 2+ in {sum(1 for v in c if v >= 2)} "
                  f"(extra reports {sum(v - 1 for v in c if v >= 2)}); first interval (before the first turn) {c[0]}")
            if rate == 1:
                for k, v in enumerate(c):
                    if v >= 2 or (v == 0 and k > 0):
                        i = k - 1
                        lo = hl[i] if i >= 0 else None
                        rng = [abs(hl[i][1] - hl[j][1]) for j in (i - 1, i + 1) if 0 <= j < len(hl)] if lo else []
                        print(f"    after turn {i:3d} ({lo[2] if lo else '-':2s} {lo[1] if lo else 0:5d} mm), "
                              f"reports {v}, ranges to neighbours {rng}")
        f6 = first_after(det_T(xm, list(range(N)), 100), tt)
        f18 = first_after(det_T(xm, list(range(0, N, 3)), 100), tt)
        big = [(i, a, b) for i, (a, b) in enumerate(zip(f6, f18)) if a is not None and b is not None and abs(a - b) > 3]
        print(f"  UA 100, gaps over 3 looks between the rates: {len(big)}")
        for i, a, b in big:
            rng = [abs(hl[i][1] - hl[j][1]) for j in (i - 1, i + 1) if 0 <= j < len(hl)]
            print(f"    turn {i:3d} {hl[i][2]:2s} {hl[i][1]:5d} mm: 6 min {a - hl[i][0]:5.1f}, 18 min {b - hl[i][0]:5.1f} "
                  f"looks late; ranges to neighbours {rng}")
        print()


if __name__ == "__main__":
    main(sys.argv[1])
