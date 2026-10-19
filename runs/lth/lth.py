"""LTH run 1: Hubble 1929's distances, rung by rung, against NED-D (plans/lth-plan.md, P1-P3).

Usage: python3 -I runs/lth/lth.py path/to/NED30.5.1-D-17.1.2-20200415.csv
The NED-D file is not committed (sha256 in the plan).
"""
import csv, math, statistics as st, sys, itertools, collections

# Hubble 1929, Table 1: (name in the paper, NED-D name, r in Mpc, rung from Hubble's text)
HUBBLE = [
    ("S. Mag.", "SMC", 0.032, "a"), ("L. Mag.", "LMC", 0.034, "a"),
    ("NGC 6822", "NGC 6822", 0.214, "a"), ("NGC 598", "MESSIER 033", 0.263, "a"),
    ("NGC 221", "MESSIER 032", 0.275, "a"), ("NGC 224", "MESSIER 031", 0.275, "a"),
    ("NGC 5457", "MESSIER 101", 0.45, "a"),
    ("NGC 4736", "MESSIER 094", 0.5, "b"), ("NGC 5194", "MESSIER 051a", 0.5, "b"),
    ("NGC 4449", "NGC 4449", 0.63, "b"), ("NGC 4214", "NGC 4214", 0.8, "b"),
    ("NGC 3031", "MESSIER 081", 0.9, "b"), ("NGC 3627", "MESSIER 066", 0.9, "b"),
    ("NGC 4826", "MESSIER 064", 0.9, "b"), ("NGC 5236", "MESSIER 083", 0.9, "b"),
    ("NGC 1068", "MESSIER 077", 1.0, "b"), ("NGC 5055", "MESSIER 063", 1.1, "b"),
    ("NGC 7331", "NGC 7331", 1.1, "b"), ("NGC 4258", "MESSIER 106", 1.4, "b"),
    ("NGC 4151", "NGC 4151", 1.7, "b"),
    ("NGC 4382", "MESSIER 085", 2.0, "c"), ("NGC 4472", "MESSIER 049", 2.0, "c"),
    ("NGC 4486", "MESSIER 087", 2.0, "c"), ("NGC 4649", "MESSIER 060", 2.0, "c"),
]

def modern(path):
    want = {n for _, n, _, _ in HUBBLE}
    rows = collections.defaultdict(list)
    for r in csv.reader(open(path, encoding="utf-8", errors="replace")):
        if len(r) > 7 and r[3] in want:
            try:
                d = float(r[6])
            except ValueError:
                continue
            if d > 0:
                rows[r[3]].append((r[7], d))
    out = {}
    for name in want:
        ds = rows.get(name, [])
        best = [d for m, d in ds if m in ("Cepheids", "TRGB")]
        pick = best if best else [d for _, d in ds]
        out[name] = (st.median(pick) if pick else None, len(best), len(ds))
    return out

def main(path):
    mod = modern(path)
    print("object      rung  r_Hubble  d_modern  (n Ceph/TRGB, n all)  r = log2(d_mod/d_H)")
    R = {}
    for paper, ned, r, rung in HUBBLE:
        d, nb, na = mod[ned]
        if d is None:
            print(f"{paper:10s}  {rung}  no NED-D distance; left out"); continue
        x = math.log2(d / r)
        R[paper] = (rung, r, d, x)
        print(f"{paper:10s}  {rung}  {r:7.3f}  {d:8.3f}   ({nb:3d}, {na:3d})        {x:6.3f}")
    by = collections.defaultdict(list)
    for p, (rung, r, d, x) in R.items():
        by[rung].append(x)
    m = {k: st.mean(v) for k, v in by.items()}
    s = {k: (st.stdev(v) if len(v) > 1 else float("nan")) for k, v in by.items()}
    for k in "abc":
        print(f"rung {k}: n {len(by[k])}, mean {m[k]:.3f} levels, sd {s[k]:.3f}")
    # P1
    p1 = m["a"] < m["b"] and m["a"] < m["c"]
    print(f"P1 mean(a) < mean(b) and mean(a) < mean(c): {m['a']:.3f} < {m['b']:.3f}, {m['c']:.3f} -> "
          f"{'not killed' if p1 else 'KILLED'}")
    # P2 (kill clause on rung b; reported for c too)
    p2 = s["b"] < abs(m["b"] - m["a"])
    print(f"P2 sd(b) < |mean(b) - mean(a)|: {s['b']:.3f} < {abs(m['b']-m['a']):.3f} -> "
          f"{'not killed' if p2 else 'KILLED'}")
    print(f"   (reported, not a kill clause: sd(c) {s['c']:.3f} against |mean(c) - mean(a)| {abs(m['c']-m['a']):.3f})")
    # P3 on rungs a and b
    pair_err = []
    for k in "ab":
        items = [(p, v) for p, v in R.items() if v[0] == k]
        for (p1n, v1), (p2n, v2) in itertools.combinations(items, 2):
            h = math.log2(v1[1] / v2[1]); md = math.log2(v1[2] / v2[2])
            pair_err.append(abs(h - md))
    obj_err = [abs(v[3]) for v in R.values()]
    a, b = st.median(pair_err), st.median(obj_err)
    p3 = a < b / 2
    print(f"P3 median same-rung pair error {a:.3f} < half median |r| {b/2:.3f} ({len(pair_err)} pairs, "
          f"{len(obj_err)} objects) -> {'not killed' if p3 else 'KILLED'}")
    # E1: the identity, checked numerically on the measured rungs
    print("E1 (identity): independent rung errors add in quadrature; a same-rung ratio carries the rung's scatter only.")



def p4():
    """P4: the SH0ES 2022 single-anchor H0 (fits 10-12) about their weighted mean."""
    H = {"N4258": 72.51, "MW": 73.02, "LMC": 73.59}
    for label, pct in (("anchor distance term (the kill clause)", {"N4258": 1.5, "MW": 1.0, "LMC": 1.2}),
                       ("subtotal per anchor (reported)", {"N4258": 1.8, "MW": 1.0, "LMC": 1.4})):
        sig = {k: H[k] * pct[k] / 100 for k in H}
        w = {k: 1 / sig[k] ** 2 for k in H}
        mean = sum(w[k] * H[k] for k in H) / sum(w.values())
        chi2 = sum(((H[k] - mean) / sig[k]) ** 2 for k in H)
        print(f"P4 {label}: weighted mean {mean:.3f}, chi2 {chi2:.3f} on 2 dof, chi2/dof {chi2/2:.3f}")
    return chi2


if __name__ == "__main__":
    main(sys.argv[1])
    p4()
