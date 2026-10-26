"""UNR run 5, post hoc (after the run): which Boston intervals D misses at slow rates, and how sharp Seattle's turns
really are against the two-leg estimate.
    python3 runs/unr/unr5-posthoc.py DATA_DIR > runs/unr/unr5-posthoc.txt
"""
import sys
import math
sys.path.insert(0, "runs/unr")
from unr3 import det_D
from unr5 import load, GRID


def curvature_at(x, t, half=30):
    """Least-squares parabola through the record ±half minutes about a NOAA turn: |second derivative|."""
    pts = [(m - t, x[m]) for m in range(t - half, t + half + 1) if m in x]
    n = len(pts)
    s = [sum(u ** k for u, _ in pts) for k in range(5)]
    b = [sum(y * u ** k for u, y in pts) for k in range(3)]
    A = [[s[0], s[1], s[2]], [s[1], s[2], s[3]], [s[2], s[3], s[4]]]
    det = lambda m: (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                     + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    A2 = [row[:2] + [b[i]] for i, row in enumerate(A)]
    return abs(2 * det(A2) / det(A)), n


def main(d):
    x, p, tt, big, scored = load(d, "8443970")
    t = [a for a, _ in tt]
    print("Boston: D every 30 min, intervals with no report, by offset")
    for o in range(0, 30, 5):
        idx = [m for m in sorted(x) if m % 30 == o]
        rep = det_D(x, idx)
        miss = [k for k in scored if not any(t[k] < q <= t[k + 1] for q in rep)]
        late = []
        for k in miss[:3]:
            nxt = [q for q in rep if q > t[k]]
            late.append((k, tt[k][1], t[k + 1] - t[k], (nxt[0] - t[k]) if nxt else None))
        print(f"  offset {o:2d}: missed {len(miss)}; first (turn, height mm, interval min, next report after it min) {late}")
    lat = {}
    for r in (10, 30):
        idx = [m for m in sorted(x) if m % r == 0]
        rep = det_D(x, idx)
        lat[r] = sorted(min((q - a for q in rep if q > a), default=None) for a in t[1:-1])
    print("  D's lateness after each NOAA turn (min), every 10 and 30 min, median and largest: "
          + "; ".join(f"{r}: {lat[r][len(lat[r]) // 2]}, {lat[r][-1]}" for r in lat))
    print()
    print("Sharpness at the turns: the two-leg estimate κ against a parabola fitted ±30 min, mm/min²")
    for st, name in [("9447130", "Seattle"), ("9414290", "San Francisco"), ("8443970", "Boston"),
                     ("1612340", "Honolulu"), ("9410660", "Los Angeles")]:
        x, p, tt, big, scored = load(d, st)
        rows = []
        for k in scored:
            if k < 1:
                continue
            legs = [abs(b[1] - a[1]) / 2 * (math.pi / (b[0] - a[0])) ** 2 for a, b in ((tt[k - 1], tt[k]), (tt[k], tt[k + 1]))]
            fit, n = curvature_at(x, tt[k][0])
            if n > 50:
                rows.append((sum(legs) / 2, fit))
        est = sorted(r[0] for r in rows)
        fit = sorted(r[1] for r in rows)
        flat_est = min(rows)
        print(f"  {name:13s} two-leg min {est[0]:.4f} median {est[len(est) // 2]:.4f};  fitted min {fit[0]:.4f} "
              f"median {fit[len(fit) // 2]:.4f};  fitted at the two-leg flattest turn {flat_est[1]:.4f}")


if __name__ == "__main__":
    main(sys.argv[1])


def noise_source(d):
    """Lag-1 spread of the observations' and the predictions' own second differences: which carries s_1."""
    print()
    print("Where s_1 comes from: sd of second differences x(t+1) − 2x(t) + x(t−1), mm")
    for st, name in [("9447130", "Seattle"), ("9414290", "San Francisco"), ("8443970", "Boston"),
                     ("1612340", "Honolulu"), ("9410660", "Los Angeles")]:
        x, p, tt, big, scored = load(d, st)

        def sd2(z):
            v = [z[m + 1] - 2 * z[m] + z[m - 1] for m in z if m - 1 in z and m + 1 in z]
            mu = sum(v) / len(v)
            return math.sqrt(sum((a - mu) ** 2 for a in v) / (len(v) - 1))
        print(f"  {name:13s} observed {sd2(x):6.2f}   predicted {sd2(p):6.2f}")


def without_first(d):
    print()
    print("Exact offsets per rate with every station's first interval left out (no look before the first turn)")
    from unr5 import exact_at
    for st, name in [("8443970", "Boston"), ("9447130", "Seattle"), ("9414290", "San Francisco")]:
        x, p, tt, big, scored = load(d, st)
        sc = [k for k in scored if k >= 1]
        print(f"  {name:13s} " + "  ".join(f"{r}:{exact_at(x, tt, sc, r)[0]}/{r}" for r in GRID))


if __name__ == "__main__":
    noise_source(sys.argv[1])
    without_first(sys.argv[1])
