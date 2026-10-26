"""UNR run 3, post hoc. R4's false turns at sigma = 0: is every one the second report after a gap that hid two turns?"""
import sys, numpy as np
sys.path.insert(0, "runs/unr"); import unr, unr2, unr3
N = unr.N; full = unr.patterns(); streams = [(n, f) for n, _, f in unr2.STREAMS]
for sigma in unr3.SIGMAS:
    for T in unr3.TS:
        hid, other = 0, 0
        for name, fn in streams:
            z = np.random.default_rng(7919 * (1 + [s for s, _ in streams].index(name)) + int(sigma * 1e6)).standard_normal(N) * sigma
            xs = fn(np.arange(N, dtype=float)) * np.exp(z); tr = unr.turns_of(fn)
            for pname, idx in full:
                turns = unr3.det_T(np.log(xs), idx, T); prev = -1
                for q in turns:
                    if not len(tr[(tr > prev) & (tr < q)]):
                        # the gap of received looks before the previous report: did it hide two or more turns?
                        k = np.searchsorted(idx, prev)
                        lo = idx[k - 1] if k >= 1 else 0
                        if len(tr[(tr > lo) & (tr < prev)]) >= 2: hid += 1
                        else: other += 1
                    prev = q
        print(f"sigma {sigma} T {T}: false turns after a gap that hid two turns {hid}; other false turns {other}")

print("\nCounted the other way: a report is false only if, up to it, the reports outnumber the true turns before it")
print("(a late report and the next one both after one turn is then not false). Excess reports, summed:")
for sigma in unr3.SIGMAS:
    row = []
    for T in unr3.TS:
        ex = 0
        for name, fn in streams:
            z = np.random.default_rng(7919 * (1 + [s for s, _ in streams].index(name)) + int(sigma * 1e6)).standard_normal(N) * sigma
            xs = fn(np.arange(N, dtype=float)) * np.exp(z); tr = unr.turns_of(fn)
            for pname, idx in full:
                turns = unr3.det_T(np.log(xs), idx, T)
                for j, q in enumerate(turns, 1):
                    ex += j > np.sum(tr < q)
        row.append(f"T {T}: {ex}")
    print(f"  sigma {sigma}: " + "; ".join(row))
