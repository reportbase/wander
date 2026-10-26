"""UNR run 7, post hoc (after the run): Juneau's break at 10 minutes, offset by offset.
    python3 runs/unr/unr7-posthoc.py JUL_DIR > runs/unr/unr7-posthoc.txt
"""
import sys
sys.path.insert(0, "runs/unr")
import unr7
from unr6 import load
from unr3 import det_D


def main(d):
    x, p, tt, scored = load(d, "9452210", "jul")
    t = [a for a, _ in tt]
    keys = sorted(x)
    for r in (8, 10, 12):
        bad = []
        for o in range(r):
            rep = det_D(x, [m for m in keys if m % r == o])
            for k in scored:
                c = sum(1 for q in rep if t[k] < q <= t[k + 1])
                if c != 1:
                    rng = [abs(tt[k][1] - tt[j][1]) for j in (k - 1, k + 1)]
                    bad.append((o, k, c, round(t[k] / 1440, 2), rng))
        print(f"Juneau, every {r} min: {len(bad)} interval-offsets off: {bad}")


if __name__ == "__main__":
    main(sys.argv[1])
