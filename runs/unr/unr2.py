"""UNR run 2: Q1′–Q3′ and Q5′ at 60 digits, ties under 1e-40 of the arrival, flips attributed to the turn before.

Predictions in plans/unr-plan.md ("Run 2: predictions"). Run from the repository's root:
    python3 runs/unr/unr2.py > runs/unr/unr-run2.txt
"""
import sys
import numpy as np
import mpmath as mp

sys.path.insert(0, "runs/unr")
import unr

mp.mp.dps = 60
N = 1000
TIE = mp.mpf("1e-40")
ALPHA = mp.mpf("0.2")
RULES = unr.RULES
P = unr.P
pi = mp.pi


def s1(n): return 2 + mp.sin(2 * pi * n / P)
def s2(n): return mp.mpf("0.2") + abs(mp.sin(pi * n / P))
def s3(n): return 2 + mp.sin(2 * pi * n / P + mp.mpf("0.9") * mp.sin(2 * pi * n / P))


def s4(seed):
    r = np.random.default_rng(1000 + seed)
    a, per, ph = r.uniform(0.1, 0.5, 4), r.uniform(80, 400, 4), r.uniform(0, 2 * np.pi, 4)
    a, per, ph = [list(map(mp.mpf, map(float, v))) for v in (a, per, ph)]
    return lambda n: 3 + sum(a[j] * mp.sin(2 * pi * n / per[j] + ph[j]) for j in range(4))


STREAMS = [("S1", s1, unr.s1), ("S2", s2, unr.s2), ("S3", s3, unr.s3)] + \
          [(f"S4.{k}", s4(k), unr.s4(k)) for k in range(4)]
MAPS = [("x^3", lambda x: x ** 3), ("sqrt x", mp.sqrt), ("e^x", mp.exp), ("ln(1+x)", mp.log1p)]
SCALES = [("k=1e-3", mp.mpf("1e-3")), ("k=7", mp.mpf(7)), ("k=1e3", mp.mpf(1000))]


def patterns():
    return [(name, idx[idx < N]) for name, idx in unr.patterns()]


def read(xs_all, idx, rule):
    xs = [xs_all[i] for i in idx]
    flips, ties, prev = [], 0, 0
    y = xs[0]
    for j in range(1, len(idx)):
        if j >= 3:
            m, p = idx[j - 1], idx[j - 2]
            g = int(idx[j] - m)
            if rule == "U":
                ref = xs[j - 1]
            elif rule == "M":
                ref = sorted(xs[j - 3:j])[1]
            elif rule == "Ta":
                ref = xs[j - 1] + g * (xs[j - 1] - xs[j - 2]) / int(m - p)
            elif rule == "Tr":
                ref = xs[j - 1] * (xs[j - 1] / xs[j - 2]) ** (mp.mpf(g) / int(m - p))
            else:
                ref = y
            d = xs[j] - ref
            if abs(d) < TIE * abs(xs[j]):
                ties += 1
            else:
                s = 1 if d > 0 else -1
                if prev and s != prev:
                    flips.append(int(idx[j]))
                prev = s
        y = y + ALPHA * (xs[j] - y)
    return flips, ties


def main():
    pats = patterns()
    print("UNR run 2 (plans/unr-plan.md). 60 digits, ties |d| < 1e-40·|x|, N = %d.\n" % N)
    base, vals, ties = {}, {}, 0
    for name, fn, _ in STREAMS:
        vals[name] = [fn(mp.mpf(n)) for n in range(N)]
        for pname, idx in pats:
            for r in RULES:
                f, t = read(vals[name], idx, r)
                base[(name, pname, r)] = f
                ties += t
    print(f"ties in the unmapped streams: {ties}\n")

    cases = len(STREAMS) * len(pats)
    print(f"Flips changed (cases of {cases})")
    changed = {}
    for mname, f in MAPS + [(s, (lambda k: (lambda x: k * x))(k)) for s, k in SCALES]:
        row = []
        for r in RULES:
            c = 0
            for name, _, _ in STREAMS:
                xm = [f(v) for v in vals[name]]
                for pname, idx in pats:
                    if read(xm, idx, r)[0] != base[(name, pname, r)]:
                        c += 1
            changed[(mname, r)] = c
            row.append(f"{r} {c:2d}")
        print(f"  {mname:8s} " + "   ".join(row))
    q1 = all(changed[(m, r)] == 0 for m, _ in MAPS for r in ("U", "M"))
    q2 = (changed[("x^3", "Tr")] == 0 and changed[("sqrt x", "Tr")] == 0 and changed[("e^x", "Tr")] > 0
          and changed[("ln(1+x)", "Tr")] > 0 and changed[("x^3", "Ta")] > 0 and changed[("x^3", "E")] > 0)
    q3 = all(changed[(s, r)] == 0 for s, _ in SCALES for r in RULES)
    print(f"  Q1′ {'not killed' if q1 else 'KILLED'}; Q2′ {'not killed' if q2 else 'KILLED'}; "
          f"Q3′ {'not killed' if q3 else 'KILLED'}\n")

    print("Q5′. U's flips attributed to the last turn before each")
    bad, lone_off, flips_n = 0, 0, 0
    for name, _, ffn in STREAMS:
        tr = unr.turns_of(ffn)
        tr = tr[tr < N - 1]
        for pname, idx in pats:
            fl = base[(name, pname, "U")]
            got = {}
            for q in fl:
                flips_n += 1
                before = tr[tr < q]
                if not len(before):
                    bad += 1
                    print(f"  {name} {pname}: flip at {q} with no turn before it")
                    continue
                t = before[-1]
                k = np.searchsorted(idx, t)
                if not (1 <= k < len(idx) - 1 and q <= idx[k + 1]):
                    bad += 1
                    print(f"  {name} {pname}: flip at {q} past its turn {t:.3f}'s bound")
                got[t] = got.get(t, 0) + 1
            for t in tr[(tr > idx[3]) & (tr < idx[-2])]:
                k = np.searchsorted(idx, t)
                if np.sum((tr > idx[k - 1]) & (tr < idx[k])) == 1 and got.get(t, 0) != 1:
                    lone_off += 1
                    print(f"  {name} {pname}: lone turn {t:.3f} with {got.get(t, 0)} flips")
    q5 = bad == 0 and lone_off == 0
    print(f"  flips {flips_n}; off their bound {bad}; lone turns without exactly one flip {lone_off}")
    print(f"  Q5′ {'not killed' if q5 else 'KILLED'}")


if __name__ == "__main__":
    main()
