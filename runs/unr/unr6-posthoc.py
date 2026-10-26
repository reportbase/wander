"""UNR run 6, post hoc (after the run): which part of the leftover wiggle separates the stations. The residual
(observed − predicted) split by running means into a fast part (under 10 min), a band of 10 to 60 min (harbour seiches)
and the slow rest (surge); each part's sd, mm, both months.
    python3 runs/unr/unr6-posthoc.py SEPT_DIR AUG_DIR > runs/unr/unr6-posthoc.txt
"""
import sys
import math
sys.path.insert(0, "runs/unr")
from unr6 import load, STATIONS, sd


def running(res, w):
    out = {}
    for m in res:
        v = [res[k] for k in range(m - w // 2, m + w // 2 + 1) if k in res]
        if len(v) > 0.8 * (w + 1):
            out[m] = sum(v) / len(v)
    return out


def main(sept, aug):
    print("sd of the residual's parts (mm): fast (< 10 min), band (10–60 min), slow (> 60 min); median two-leg κ")
    for st, name in STATIONS:
        for d, month in ((sept, "sep"), (aug, "aug")):
            x, p, tt, scored = load(d, st, month)
            res = {m: x[m] - p[m] for m in x if m in p}
            m10, m60 = running(res, 10), running(res, 60)
            keys = [m for m in res if m in m10 and m in m60]
            fast = sd([res[m] - m10[m] for m in keys])
            band = sd([m10[m] - m60[m] for m in keys])
            slow = sd([m60[m] for m in keys])
            kap = sorted(sum(abs(b[1] - a[1]) / 2 * (math.pi / (b[0] - a[0])) ** 2
                             for a, b in ((tt[k - 1], tt[k]), (tt[k], tt[k + 1]))) / 2 for k in scored)
            print(f"  {name:13s} {month}: fast {fast:5.1f}  band {band:5.1f}  slow {slow:6.1f}  κ median {kap[len(kap) // 2]:.4f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
