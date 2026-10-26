"""UNR run 3: noise, and a threshold to declare a turn. Predictions R1–R4 in plans/unr-plan.md, written first.
    python3 runs/unr/unr3.py > runs/unr/unr-run3.txt
"""
import sys
import math
import numpy as np
import mpmath as mp

sys.path.insert(0, "runs/unr")
import unr
import unr2

mp.mp.dps = 60
SIGMAS = [0.0, 0.002, 0.005]
TS = [0.01, 0.03]
TAS = [0.02, 0.06]
M = 3


def noise(name, n, sigma):
    seed = 7919 * (1 + [s for s, _, _ in unr2.STREAMS].index(name)) + int(sigma * 1e6)
    return np.random.default_rng(seed).standard_normal(n) * sigma


# --- the three detectors; xs and lx (ln x) are sequences of numbers, mp or float -----------------------
def det_D(xs, idx):
    turns, d, run, h = [], 0, 0, xs[idx[0]]
    for i in idx[1:]:
        x = xs[i]
        s = int(x > h) - int(x < h)
        h = x
        if s == 0:
            continue
        if d == 0:
            d = s
        elif s != d:
            run += 1
            if run >= M:
                turns.append(int(i)); d = s; run = 0
        else:
            run = 0
    return turns


def det_T(vals, idx, T):
    """vals: ln x (UT) or x (UA); hold moves when |val − hold| > T."""
    turns, d, h = [], 0, vals[idx[0]]
    for i in idx[1:]:
        v = vals[i]
        if abs(v - h) > T:
            s = 1 if v > h else -1
            if d and s != d:
                turns.append(int(i))
            d = s
            h = v
    return turns


def main():
    pats = unr2.patterns()
    print("UNR run 3 (plans/unr-plan.md). M = %d; T in levels %s; T_a in amounts %s; sigma %s.\n" % (M, TS, TAS, SIGMAS))

    # R1, R2 at 60 digits, N = 1000
    maps = unr2.MAPS + [(s, (lambda k: (lambda x: k * x))(k)) for s, k in unr2.SCALES]
    changed = {}
    for name, fn, _ in unr2.STREAMS:
        base_x = [fn(mp.mpf(n)) for n in range(unr2.N)]
        for sigma in SIGMAS:
            z = noise(name, unr2.N, sigma)
            x0 = [base_x[n] * mp.exp(mp.mpf(float(z[n]))) for n in range(unr2.N)]
            ref = {}
            for mname, f in [("id", lambda x: x)] + maps:
                xm = [f(v) for v in x0]
                lx = [mp.log(v) for v in xm]
                for pname, idx in pats:
                    out = {"D": det_D(xm, idx)}
                    for T in TS:
                        out[f"UT {T}"] = det_T(lx, idx, mp.mpf(T))
                    for Ta in TAS:
                        out[f"UA {Ta}"] = det_T(xm, idx, mp.mpf(Ta))
                    for r, tv in out.items():
                        if mname == "id":
                            ref[(pname, r)] = tv
                        else:
                            key = (mname, r)
                            changed.setdefault(key, 0)
                            if tv != ref[(pname, r)]:
                                changed[key] += 1
    rules = ["D"] + [f"UT {T}" for T in TS] + [f"UA {Ta}" for Ta in TAS]
    cases = len(unr2.STREAMS) * len(pats) * len(SIGMAS)
    print(f"R1–R2. Turns changed by a map (cases of {cases}: streams × patterns × noise levels)")
    print("  map      " + "".join(f"{r:>10s}" for r in rules))
    for mname, _ in maps:
        print(f"  {mname:8s} " + "".join(f"{changed[(mname, r)]:10d}" for r in rules))
    r1 = all(changed[(m, "D")] == 0 for m, _ in maps)
    sc = [s for s, _ in unr2.SCALES]
    r2 = (all(changed[(s, f"UT {T}")] == 0 for s in sc for T in TS)
          and all(changed[("x^3", f"UT {T}")] + changed[("sqrt x", f"UT {T}")] > 0 for T in TS)
          and all(sum(changed[(s, f"UA {Ta}")] for s in sc) > 0 for Ta in TAS))
    print(f"  R1 {'not killed' if r1 else 'KILLED'}; R2 {'not killed' if r2 else 'KILLED'}\n")

    # R3: noise-free lateness of UT on S1, every look, against the bound from kappa
    N = unr.N
    w = 2 * np.pi / unr.P
    x = unr.s1(np.arange(N, dtype=float))
    tr = unr.turns_of(unr.s1)
    print("R3. UT on S1, no noise, every look: lateness against [sqrt(2T/kappa) - 1, sqrt(4T/kappa) + 1]")
    r3 = True
    for T in TS:
        turns = det_T(np.log(x), np.arange(N), T)
        lat = {"max": [], "min": []}
        out = 0
        for q in turns:
            t = tr[tr < q][-1]
            xt = unr.s1(np.array([t]))[0]
            kind = "max" if xt > 2 else "min"
            kap = w * w / 3 if kind == "max" else w * w      # |(ln x)''| at the turn: x''/x there, x' = 0
            lo, hi = math.sqrt(2 * T / kap) - 1, math.sqrt(4 * T / kap) + 1
            lat[kind].append(q - t)
            if not (lo <= q - t <= hi):
                out += 1
        for kind in ("max", "min"):
            kap = w * w / 3 if kind == "max" else w * w
            print(f"  T {T}: {kind}s lateness {min(lat[kind]):.2f}–{max(lat[kind]):.2f} looks, bound "
                  f"{math.sqrt(2*T/kap)-1:.2f}–{math.sqrt(4*T/kap)+1:.2f}")
        print(f"  T {T}: turns {len(turns)} of {len(tr[(tr > 2) & (tr < N - 40)])}, outside the bound {out}")
        r3 &= out == 0
    print(f"  R3 {'not killed' if r3 else 'KILLED'}\n")

    # R4 and the measured lateness: float64, N = 4000, the seven streams, every pattern
    print("R4. False turns (no true turn since the turn before), per detector, summed over streams and patterns;")
    print("    and the mean lateness of the turns that are not false, in looks")
    full = unr.patterns()
    streams = [(n, f) for n, _, f in unr2.STREAMS]
    r4 = True
    for sigma in SIGMAS:
        tot = {}
        for name, fn in streams:
            z = np.random.default_rng(7919 * (1 + [s for s, _ in streams].index(name)) + int(sigma * 1e6)) \
                .standard_normal(N) * sigma
            xs = fn(np.arange(N, dtype=float)) * np.exp(z)
            lx = np.log(xs)
            tr = unr.turns_of(fn)
            for pname, idx in full:
                outs = {"D": det_D(xs, idx)}
                for T in TS:
                    outs[f"UT {T}"] = det_T(lx, idx, T)
                for Ta in TAS:
                    outs[f"UA {Ta}"] = det_T(xs, idx, Ta)
                for r, turns in outs.items():
                    false, lats, prev = 0, [], -1
                    for q in turns:
                        between = tr[(tr > prev) & (tr < q)]
                        if not len(between):
                            false += 1
                        else:
                            lats.append(q - between[-1])
                        prev = q
                    a = tot.setdefault(r, [0, [], 0])
                    a[0] += false; a[1] += lats; a[2] += len(turns)
        print(f"  sigma {sigma}:")
        for r in rules:
            f_, l_, n_ = tot[r]
            print(f"    {r:8s} turns {n_:6d}  false {f_:6d}  mean lateness {np.mean(l_) if l_ else float('nan'):7.2f}")
        for T in TS:
            if sigma > 0 and T >= 8 * sigma and tot[f"UT {T}"][0] > 0:
                r4 = False
        if sigma == 0.005 and tot["UT 0.01"][0] == 0:
            r4 = False
        if sigma == 0 and any(tot[f"UT {T}"][0] for T in TS):
            r4 = False
    print(f"  R4 {'not killed' if r4 else 'KILLED'}")


if __name__ == "__main__":
    main()
