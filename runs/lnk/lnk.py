"""LNK (plans/lnk-plan.md). Run from the repository's root: python3 runs/lnk/lnk.py"""
import json, os
from collections import Counter
import numpy as np
from scipy.optimize import minimize_scalar, minimize

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lnk-results.json")
DS = [1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512]
V = 2000


def words():
    from datasets import load_dataset
    d = load_dataset("Salesforce/wikitext", "wikitext-2-v1")["train"]["text"]
    w = " ".join(d).split()
    top = {x: i for i, (x, _) in enumerate(Counter(w).most_common(V))}
    return np.array([top.get(x, V) for x in w], dtype=np.int64)


def mi(a, b):
    n = len(a); K = V + 1
    j = np.bincount(a * K + b, minlength=K * K).astype(float) / n
    pa = np.bincount(a, minlength=K) / n; pb = np.bincount(b, minlength=K) / n
    j = j.reshape(K, K); m = j > 0
    return float((j[m] * np.log2(j[m] / np.outer(pa, pb)[m])).sum())


def main():
    x = words(); rng = np.random.default_rng(0); n = len(x)
    print("words", n)
    rows = {}
    for d in DS:
        a, b = x[:-d], x[d:]
        raw = mi(a, b); sh = mi(a, rng.permutation(b))
        parts = []
        for p in range(5):
            s = slice(p * len(a) // 5, (p + 1) * len(a) // 5)
            pa, pb = a[s], b[s]
            parts.append(mi(pa, pb) - mi(pa, rng.permutation(pb)))
        shs = [mi(a[p * len(a) // 5:(p + 1) * len(a) // 5], rng.permutation(b[p * len(a) // 5:(p + 1) * len(a) // 5])) for p in range(5)]
        rows[d] = {"I": raw - sh, "raw": raw, "shuffled": sh, "spread": float(np.std(parts) / np.sqrt(5)),
                   "shuffled_spread": float(np.std(shs) / np.sqrt(5))}
        print(d, rows[d], flush=True)
    counted = [d for d in DS if rows[d]["I"] > 3 * max(rows[d]["spread"], rows[d]["shuffled_spread"])]
    I = {d: rows[d]["I"] for d in DS}
    v = {}
    v["L1"] = all(I[d2] <= I[d1] + 2 * rows[d2]["spread"] for d1, d2 in zip(DS, DS[1:]) if d2 in counted)
    def cauchy_err(lH):
        H = np.exp(lH); pred = {d: I[1] * (1 + 1 / H**2) / (1 + (d / H) ** 2) for d in counted}
        return max(abs(pred[d] / I[d] - 1) for d in counted)
    best = minimize_scalar(cauchy_err, bounds=(-3, 8), method="bounded")
    v["L2"] = best.fun <= 0.25
    far = [d for d in counted if d >= 8]
    ld, lI = np.log(far), np.log([I[d] for d in far])
    c = np.polyfit(ld, lI, 1); err_pow = float(((np.polyval(c, ld) - lI) ** 2).sum())
    f = lambda p: float(((p[0] - np.log1p((np.array(far) / np.exp(p[1])) ** 2) - lI) ** 2).sum())
    fc = min((minimize(f, [lI[0], h], method="Nelder-Mead") for h in np.linspace(-2, 7, 10)), key=lambda r: r.fun)
    v["L3"] = err_pow < fc.fun
    ratios = [I[2 * d] / I[d] for d in counted if d >= 16 and 2 * d in counted]
    v["L4"] = (max(ratios) - min(ratios)) <= 0.30 if ratios else False
    out = {"rows": rows, "counted": counted, "cauchy_best_H": float(np.exp(best.x)), "cauchy_max_rel_err": float(best.fun),
           "power_slope": float(c[0]), "power_sq_err": err_pow, "cauchy_free_sq_err": float(fc.fun),
           "cauchy_free_H": float(np.exp(fc.x[1])), "ratios_2d": ratios,
           "verdicts": {k: ("not killed" if x_ else "KILLED") for k, x_ in v.items()}}
    json.dump(out, open(OUT, "w"), indent=1)
    print(json.dumps({k: out[k] for k in out if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
