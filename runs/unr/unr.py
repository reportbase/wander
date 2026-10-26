"""UNR run 1: the unit rule's turns against carries that model the payload.

Predictions in plans/unr-plan.md, written before this script. Run from the repository's root:
    python3 runs/unr/unr.py > runs/unr/unr-run1.txt
"""
import math
import numpy as np

N, P, ALPHA, WIN = 4000, 200, 0.2, 200 / 8          # WIN = P/8, the match window, in looks
RULES = ["U", "M", "Ta", "Tr", "E"]


# --- streams -------------------------------------------------------------------------------------------
def s1(t): return 2 + np.sin(2 * np.pi * t / P)
def s2(t): return 0.2 + np.abs(np.sin(np.pi * t / P))
def s3(t): return 2 + np.sin(2 * np.pi * t / P + 0.9 * np.sin(2 * np.pi * t / P))


def s4(seed):
    r = np.random.default_rng(1000 + seed)
    a, per, ph = r.uniform(0.1, 0.5, 4), r.uniform(80, 400, 4), r.uniform(0, 2 * np.pi, 4)
    return lambda t: 3 + sum(a[j] * np.sin(2 * np.pi * t / per[j] + ph[j]) for j in range(4))


STREAMS = [("S1", s1), ("S2", s2), ("S3", s3)] + [(f"S4.{k}", s4(k)) for k in range(10)]


def turns_of(fn):
    """Local extrema of the continuous stream, found on a grid 1,000 times finer than the looks."""
    t = np.arange(0, N - 1, 1e-3)
    x = fn(t)
    d = np.sign(np.diff(x))
    k = np.nonzero(d[1:] * d[:-1] < 0)[0] + 1
    return t[k]


# --- patterns of looks ---------------------------------------------------------------------------------
def patterns():
    out = [("all", np.arange(N))]
    for keep, sd in [(0.8, 1), (0.5, 2), (0.2, 3)]:
        r = np.random.default_rng(sd)
        m = r.random(N) < keep
        m[:4] = True
        out.append((f"keep {keep}", np.nonzero(m)[0]))
    for B, sd in [(20, 4), (80, 5)]:
        r = np.random.default_rng(sd)
        m = np.ones(N, bool)
        lost, target = 0, int(0.2 * N)
        while lost < target:
            s = r.integers(4, N - B)
            if m[s:s + B].all():
                m[s:s + B] = False
                lost += B
        out.append((f"bursts {B}", np.nonzero(m)[0]))
    return out


# --- the reader ------------------------------------------------------------------------------------------
def read(x, idx, rule):
    """Flips (look indices), the number of ties, and the least |arrival − ref|/|arrival| seen."""
    xs = x[idx]
    flips, ties, margin = [], 0, math.inf
    prev = 0
    y = xs[0]
    for j in range(1, len(idx)):
        if rule == "E":
            ref = y
        elif j >= 3:
            m, p = idx[j - 1], idx[j - 2]
            g = idx[j] - m
            if rule == "U":
                ref = xs[j - 1]
            elif rule == "M":
                a3, b3, c3 = xs[j - 3], xs[j - 2], xs[j - 1]; ref = max(min(a3, b3), min(max(a3, b3), c3))
            elif rule == "Ta":
                ref = xs[j - 1] + g * (xs[j - 1] - xs[j - 2]) / (m - p)
            elif rule == "Tr":
                ref = xs[j - 1] * (xs[j - 1] / xs[j - 2]) ** (g / (m - p))
        if rule == "E" or j >= 3:
            if j >= 3:
                d = xs[j] - ref
                margin = min(margin, abs(d) / abs(xs[j]))
                s = int(d > 0) - int(d < 0)
                if s == 0:
                    ties += 1
                elif prev != 0 and s != prev:
                    flips.append(int(idx[j]))
                if s != 0:
                    prev = s
        y = y + ALPHA * (xs[j] - y)
    return flips, ties, margin


def score(flips, turns):
    """Per-turn error (nearest flip within WIN, else None), and the false flips."""
    f = np.array(flips, float)
    tt = turns[(turns > 4) & (turns < N - 2)]
    errs = []
    for t in tt:
        if len(f) and np.min(np.abs(f - t)) <= WIN:
            errs.append(float(np.min(np.abs(f - t))))
        else:
            errs.append(None)
    false = int(sum(1 for q in f if len(tt) == 0 or np.min(np.abs(tt - q)) > WIN))
    return tt, errs, false


def mean_err(errs):
    return float(np.mean([WIN if e is None else e for e in errs])) if errs else float("nan")


MAPS = [("x^3", lambda x: x ** 3), ("sqrt x", np.sqrt), ("e^x", np.exp), ("ln(1+x)", np.log1p)]
SCALES = [("k=1e-3", 1e-3), ("k=7", 7.0), ("k=1e3", 1e3)]


def main():
    pats = patterns()
    data = {}
    for name, fn in STREAMS:
        x = fn(np.arange(N, dtype=float))
        tr = turns_of(fn)
        for pname, idx in pats:
            for r in RULES:
                data[(name, pname, r)] = read(x, idx, r) + (tr,)

    print("UNR run 1 (plans/unr-plan.md). N = %d looks, P = %d, match window P/8 = %g looks.\n" % (N, P, WIN))

    # Q1, Q2, Q3: maps of the payload and the scale of the world
    print("Q1–Q3. Flips changed by a map of the payload (count of stream × pattern cases changed, of %d)"
          % (len(STREAMS) * len(pats)))
    changed = {}
    for mname, f in MAPS + [(s, (lambda k: (lambda x: k * x))(k)) for s, k in SCALES]:
        row = []
        for r in RULES:
            c = 0
            for name, fn in STREAMS:
                x = f(fn(np.arange(N, dtype=float)))
                for pname, idx in pats:
                    if read(x, idx, r)[0] != data[(name, pname, r)][0]:
                        c += 1
            changed[(mname, r)] = c
            row.append(f"{r} {c:3d}")
        print(f"  {mname:8s} " + "   ".join(row))
    least = min(data[k][2] for k in data)
    print("  least |arrival − ref|/|arrival| over every comparison: %.3g; ties: %d"
          % (least, sum(data[k][1] for k in data)))
    q1 = all(changed[(m, r)] == 0 for m, _ in MAPS for r in ("U", "M"))
    q2 = (changed[("x^3", "Tr")] == 0 and changed[("sqrt x", "Tr")] == 0
          and (changed[("e^x", "Tr")] > 0 or changed[("ln(1+x)", "Tr")] > 0)
          and changed[("x^3", "Ta")] > 0 and changed[("x^3", "E")] > 0)
    q3 = all(changed[(s, r)] == 0 for s, _ in SCALES for r in RULES)
    print(f"  Q1 {'not killed' if q1 else 'KILLED'}; Q2 {'not killed' if q2 else 'KILLED'}; "
          f"Q3 {'not killed' if q3 else 'KILLED'}\n")

    # Q4: every look received
    print("Q4. Every look received: per rule, turns found / turns, worst and mean error, false flips")
    q4 = True
    for name in ["S1", "S2", "S3"]:
        for r in RULES:
            flips, _, _, tr = data[(name, "all", r)]
            tt, errs, false = score(flips, tr)
            found = [e for e in errs if e is not None]
            worst = max(found) if found else float("nan")
            print(f"  {name} {r:2s} found {len(found):2d}/{len(tt):2d}  worst {worst:6.2f}  mean "
                  f"{(np.mean(found) if found else float('nan')):6.2f}  false {false:3d}")
            if name in ("S1", "S2", "S3") and r == "U" and (len(found) < len(tt) or worst > 1 or false):
                q4 = False
    # Ta on S1 at the inflections, Tr at sin = −1/2
    f_ta = np.array(data[("S1", "all", "Ta")][0], float)
    infl = np.arange(0, N, P / 2)
    d_ta = max(np.min(np.abs(infl - q)) for q in f_ta) if len(f_ta) else math.inf
    f_tr = np.array(data[("S1", "all", "Tr")][0], float)
    half = np.sort(np.concatenate([np.arange(0, N, P) + P * 7 / 12, np.arange(0, N, P) + P * 11 / 12]))
    d_tr = max(np.min(np.abs(half - q)) for q in f_tr) if len(f_tr) else math.inf
    _, e_ta, _ = score(data[("S1", "all", "Ta")][0], data[("S1", "all", "Ta")][3])
    _, e_tr, _ = score(data[("S1", "all", "Tr")][0], data[("S1", "all", "Tr")][3])
    _, e_e, _ = score(data[("S1", "all", "E")][0], data[("S1", "all", "E")][3])
    _, e_m, _ = score(data[("S1", "all", "M")][0], data[("S1", "all", "M")][3])
    print(f"  S1: Ta's flips within {d_ta:.2f} looks of the inflections ({len(f_ta)} flips); "
          f"Tr's within {d_tr:.2f} of sin = −½ ({len(f_tr)} flips)")
    print(f"  S1: turns found by Ta {sum(e is not None for e in e_ta)}, by Tr {sum(e is not None for e in e_tr)}; "
          f"E's errors {min(e for e in e_e if e is not None):.2f}–{max(e for e in e_e if e is not None):.2f}; "
          f"M's worst {max(e for e in e_m if e is not None):.2f}")
    q4 = (q4 and d_ta <= 2 and d_tr <= 2 and all(e is None for e in e_ta) and all(e is None for e in e_tr)
          and all(e is not None and 3 <= e <= 5 for e in e_e) and all(e is not None and e <= 2 for e in e_m))
    print(f"  Q4 {'not killed' if q4 else 'KILLED'}\n")

    # Q5: U's bound and false flips under every pattern
    print("Q5. U under every pattern: false flips, turns past the bound n2 − m1, turns excluded (two in one interval)")
    q5 = True
    for name, fn in STREAMS:
        for pname, idx in pats:
            flips, _, _, tr = data[(name, pname, "U")]
            tt, errs, false = score(flips, tr)
            fa = np.array(flips, float)
            over, excl, miss = 0, 0, 0
            for t, e in zip(tt, errs):
                k = np.searchsorted(idx, t)          # idx[k] the first received after t
                if k < 1 or k + 1 >= len(idx):
                    continue
                m1, n1, n2 = idx[k - 1], idx[k], idx[k + 1]
                if np.sum((tr > m1) & (tr < n1)) > 1:
                    excl += 1
                    continue
                if e is None:
                    miss += 1
                    continue
                if e > n2 - m1:
                    over += 1
            if false or over or miss:
                q5 = False
                print(f"  {name:6s} {pname:10s} false {false} over {over} missed {miss} excluded {excl}")
    print(f"  (cases not listed: no false flip, none over, none missed)\n  Q5 {'not killed' if q5 else 'KILLED'}\n")

    # Q6: mean error under gaps
    print("Q6. Mean error in looks under gaps (a missed turn counted as P/8), per stream and pattern")
    q6 = True
    print("  stream pattern     " + "".join(f"{r:>8s}" for r in RULES))
    for name, _ in STREAMS:
        for pname, _ in pats[1:]:
            me = {r: mean_err(score(data[(name, pname, r)][0], data[(name, pname, r)][3])[1]) for r in RULES}
            best = min(me.values())
            ok = me["U"] <= 1.1 * best and me["Ta"] >= 3 * me["U"] and me["Tr"] >= 3 * me["U"]
            q6 &= ok
            print(f"  {name:6s} {pname:10s} " + "".join(f"{me[r]:8.2f}" for r in RULES) + ("" if ok else "   <-"))
    print(f"  Q6 {'not killed' if q6 else 'KILLED'}")


if __name__ == "__main__":
    main()
