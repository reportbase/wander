"""UNR run 1, post hoc (after the run; changes no prediction). Why each kill happened."""
import sys, numpy as np
sys.path.insert(0, "runs/unr")
import unr
from unr import N, STREAMS, patterns, read, score, MAPS, SCALES

pats = patterns()

def comparisons(x, idx, rule):
    """Every comparison's signed difference, as read() makes them (same code path, kept here)."""
    xs = x[idx]; out = {}; y = xs[0]
    for j in range(1, len(idx)):
        if j >= 3:
            m, p = idx[j-1], idx[j-2]; g = idx[j] - m
            ref = {"U": xs[j-1],
                   "M": sorted(xs[j-3:j])[1],
                   "Ta": xs[j-1] + g*(xs[j-1]-xs[j-2])/(m-p),
                   "Tr": xs[j-1]*(xs[j-1]/xs[j-2])**(g/(m-p)),
                   "E": y}[rule]
            out[int(idx[j])] = (xs[j] - ref) / abs(xs[j])
        y = y + unr.ALPHA*(xs[j]-y)
    return out

print("1. Every case a map changed, for U, M (any map) and Ta (scaling): the comparisons whose sign differs")
for mname, f in MAPS + [(s, (lambda k: (lambda x: k*x))(k)) for s, k in SCALES]:
    for rule in ("U", "M", "Ta"):
        if rule == "Ta" and not mname.startswith("k="): continue
        for name, fn in STREAMS:
            x0 = fn(np.arange(N, dtype=float)); x1 = f(x0)
            for pname, idx in pats:
                if read(x0, idx, rule)[0] == read(x1, idx, rule)[0]: continue
                c0, c1 = comparisons(x0, idx, rule), comparisons(x1, idx, rule)
                bad = [(n, c0[n], c1[n]) for n in c0 if np.sign(c0[n]) != np.sign(c1[n])]
                worst = max(abs(b[1]) for b in bad) if bad else None
                print(f"  {mname:8s} {rule:2s} {name:6s} {pname:10s} signs differing {len(bad)}, "
                      f"largest original |diff|/|x| among them {worst:.2e}")

print("\n2. Q4: the errors exactly")
for name in ("S1", "S2", "S3"):
    for rule in ("U", "E"):
        fl, _, _, tr = (*read(STREAMS[[s for s,_ in STREAMS].index(name)][1](np.arange(N, dtype=float)),
                              np.arange(N), rule), unr.turns_of(STREAMS[[s for s,_ in STREAMS].index(name)][1]))
        _, e, _ = score(fl, tr)
        e = [v for v in e if v is not None]
        print(f"  {name} {rule}: errors {min(e):.4f} … {max(e):.4f}")

print("\n3. Q5: U's 'false' flips and 'missed' turns. For each false flip: the nearest turn, and whether the flip")
print("   lies within that turn's bound n2 − m1 (a turn inside a long gap, flipped after the window)")
for name, fn in STREAMS:
    x = fn(np.arange(N, dtype=float)); tr = unr.turns_of(fn)
    for pname, idx in pats:
        fl = read(x, idx, "U")[0]
        tt, errs, false = score(fl, tr)
        if not false: continue
        inb, outb = 0, []
        for q in fl:
            if np.min(np.abs(tt - q)) <= unr.WIN: continue
            t = tt[np.argmin(np.abs(tt - q))]
            k = np.searchsorted(idx, t)
            if 1 <= k < len(idx)-1 and q <= idx[k+1] and q >= t: inb += 1
            else: outb.append((q, float(t), float(tr[(tr > q-60) & (tr < q+60)].size)))
        print(f"  {name:6s} {pname:10s} false {false}: within the turn's bound {inb}; other {outb}")

print("\n4. Q5 again, each U flip attributed to the last true turn before it (U can only flip after a turn):")
print("   is every flip within that turn's bound n2 − m1, and does every turn get exactly one flip?")
bad = 0; total = 0; extra = 0; none = 0
for name, fn in STREAMS:
    x = fn(np.arange(N, dtype=float)); tr = unr.turns_of(fn)
    for pname, idx in pats:
        fl = read(x, idx, "U")[0]
        got = {}
        for q in fl:
            before = tr[tr < q]
            if not len(before): bad += 1; continue
            t = before[-1]; k = np.searchsorted(idx, t)
            total += 1
            if not (1 <= k < len(idx)-1 and q <= idx[k+1]): bad += 1
            got[t] = got.get(t, 0) + 1
        extra += sum(v - 1 for v in got.values())
        inner = tr[(tr > idx[3]) & (tr < idx[-2])]
        for t in inner:
            k = np.searchsorted(idx, t)
            alone = np.sum((tr > idx[k-1]) & (tr < idx[k])) == 1
            if alone and t not in got: none += 1
print(f"   flips {total}; outside the bound or with no turn before them {bad}; turns with two flips {extra}; "
      f"lone turns with no flip {none}")

print("\n5. The turns with two flips or none: does each share a received interval, or its neighbour's, with another turn?")
for name, fn in STREAMS:
    x = fn(np.arange(N, dtype=float)); tr = unr.turns_of(fn)
    for pname, idx in pats:
        fl = read(x, idx, "U")[0]
        got = {}
        for q in fl:
            b = tr[tr < q]
            if len(b): got.setdefault(b[-1], []).append(q)
        for t, qs in got.items():
            if len(qs) > 1:
                k = np.searchsorted(idx, t); lo, hi = idx[k-1], idx[min(k+1, len(idx)-1)]
                near = tr[(tr > lo - 1) & (tr < hi + 1)]
                print(f"  {name:6s} {pname:10s} turn {t:8.3f} flips {qs}; received {lo}..{hi}; turns there {np.round(near,2).tolist()}")
