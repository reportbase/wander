"""LTR run 1: the distance ladder revisited (plans/ltr-plan.md, P1-P5).

Usage: python3 -I runs/ltr/ltr.py path/to/table2.dat
  (Cosmicflows-4, J/ApJ/944/94 table2; sha256 8e9089...332f, as in plans/lth-plan.md; not committed)
P1 and P5 are exact; P2 uses the per-object table recorded in plans/lth-plan.md (LTH run 1);
P3 and P4 read Cosmicflows-4.
"""
import sys, math, itertools, random, statistics as st
from fractions import Fraction as F
import mpmath as mp

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40
out = []
def say(s=""):
    print(s); out.append(s)

# ---------------------------------------------------------------- P1 (exact)
def p1():
    say("== P1 (exact: pan, stretch, loops)")
    bad = 0
    # (a) pan and stretch under scaling the world by k
    f = mp.mpf(2) ** mp.mpf("1.2")      # a pan of 1.2 levels
    s = mp.mpf("0.1")                   # a stretch of 0.1 mag/mag
    dp = mp.mpf(30)                     # the stretch's pivot, an amount (Mpc)
    def mu(d): return 5 * mp.log10(d) + 25
    def pan(d): return mu(f * d) - mu(d)
    def stretch(d): return mu(dp * (d / dp) ** (1 + s)) - mu(d)
    for k in [mp.mpf("1e-3"), mp.mpf(7), mp.mpf("1e6")]:
        for d in [mp.mpf(3), mp.mpf(50), mp.mpf(400)]:
            e1 = abs(pan(k * d) - pan(d))
            e2 = abs((stretch(k * d) - stretch(d)) - 5 * s * mp.log10(k))
            # slope d(dmu)/dmu by exact derivative in log: dmu = 5 s log10(d/dp) -> slope s
            sl = mp.diff(lambda x: stretch(mp.e ** x), mp.log(k * d)) / mp.diff(lambda x: mu(mp.e ** x), mp.log(k * d))
            e3 = abs(sl - s)
            if max(e1, e2) > TOL or e3 > mp.mpf(10) ** -30: bad += 1
    # slope unchanged by the H0 assumed: mu_flow shifts by a constant, a slope on it does not
    xs = [mp.mpf(33) + i for i in range(6)]; ys = [s * x + 1 for x in xs]
    def ols(x, y):
        mx, my = sum(x) / len(x), sum(y) / len(y)
        return sum((a - mx) * (b - my) for a, b in zip(x, y)) / sum((a - mx) ** 2 for a in x)
    for dH in [mp.mpf(-1), mp.mpf("0.3"), mp.mpf(2)]:
        if abs(ols([x + dH for x in xs], [y - s * dH + 0 for y in ys]) - s) > TOL: bad += 1
    say(f"(a) pan unchanged under k; stretch moved by 5 s log10 k; slopes s at every k and H0: {'ok' if bad == 0 else 'FAILED %d' % bad}")
    # (b) same objects: the loop of offsets and of slopes closes identically
    rnd = random.Random(1)
    b2 = 0
    for _ in range(200):
        A, B, C = (F(rnd.randint(-10**6, 10**6), 997) for _ in range(3))
        if (A - B) + (B - C) + (C - A) != 0: b2 += 1
    say(f"(b) three methods on one object, 200 draws: loop closure identically 0: {'ok' if b2 == 0 else 'FAILED'}")
    bad += b2
    # (c) networks: K3 and K4, each link read on its own objects; one link misread
    def triangles(nodes):
        return list(itertools.combinations(nodes, 3))
    def closure(tri, link):  # oriented sum a->b->c->a of link readings (true offsets cancel)
        a, b, c = tri
        def r(x, y): return link[(x, y)] if (x, y) in link else -link[(y, x)]
        return r(a, b) + r(b, c) + r(c, a)
    def network(n, mis_edge, mis):
        true = {i: F(rnd.randint(-500, 500), 7) for i in range(n)}
        link = {(i, j): true[i] - true[j] for i, j in itertools.combinations(range(n), 2)}
        link[mis_edge] += mis
        return link
    # K4: locate every one of the six links, as a factor (pan) and as a slope (stretch, same algebra)
    n4 = 0; ok4 = 0
    for e in itertools.combinations(range(4), 2):
        for mis in [F(3, 10), F(-1, 8)]:
            n4 += 1
            link = network(4, e, mis)
            fails = [t for t in triangles(range(4)) if closure(t, link) != 0]
            cands = [x for x in itertools.combinations(range(4), 2)
                     if all((x[0] in t and x[1] in t) == (t in fails) for t in triangles(range(4)))]
            sizes_ok = all(abs(closure(t, link)) == abs(mis) for t in fails)
            if cands == [e] and len(fails) == 2 and sizes_ok: ok4 += 1
    # K3: one loop; every link explains the closure equally (cannot locate)
    n3 = 0; loc3 = 0
    for e in itertools.combinations(range(3), 2):
        n3 += 1
        link = network(3, e, F(3, 10))
        c = closure((0, 1, 2), link)
        # each link, corrected by the closure (with its orientation), closes the loop
        fixes = 0
        for x in itertools.combinations(range(3), 2):
            for sgn in (1, -1):
                l2 = dict(link); l2[x] -= sgn * c
                if closure((0, 1, 2), l2) == 0: fixes += 1; break
        if fixes != 3: loc3 += 1
    say(f"(c) K4: {ok4} of {n4} single misread links located uniquely by their two failing triangles, closure = misread exactly")
    say(f"    K3: {n3 - loc3} of {n3} misread links indistinguishable (every link fixes the one loop)")
    if ok4 != n4 or loc3 != 0: bad += 1
    say(f"P1 {'KILLED' if bad else 'not killed'}")
    return bad

# ---------------------------------------------------------------- P2 (Hubble 1929, recorded data)
HUB = {  # object: (rung, Hubble r Mpc, NED-D median Mpc), from plans/lth-plan.md run 1
    "SMC": ("a", 0.032, 0.062), "LMC": ("a", 0.034, 0.050), "N6822": ("a", 0.214, 0.479),
    "N598": ("a", 0.263, 0.855), "N221": ("a*", 0.275, 0.724), "N224": ("a", 0.275, 0.783),
    "N5457": ("b", 0.45, 6.900),  # M 101, moved to (b) as run 1 found post hoc
    "N4736": ("b", 0.5, 4.660), "N5194": ("b", 0.5, 8.580), "N4449": ("b", 0.63, 4.205),
    "N4214": ("b", 0.8, 2.935), "N3031": ("b", 0.9, 3.630), "N3627": ("b", 0.9, 10.550),
    "N4826": ("b", 0.9, 4.965), "N5236": ("b", 0.9, 4.610), "N1068": ("b", 1.0, 10.500),
    "N5055": ("b", 1.1, 9.095), "N7331": ("b", 1.1, 15.000), "N4258": ("b", 1.4, 7.510),
    "N4151": ("b", 1.7, 5.385),
}
def olsse(x, y):
    n = len(x); mx, my = st.mean(x), st.mean(y)
    sxx = sum((a - mx) ** 2 for a in x)
    b = sum((a - mx) * (c - my) for a, c in zip(x, y)) / sxx
    a0 = my - b * mx
    s2 = sum((c - a0 - b * a) ** 2 for a, c in zip(x, y)) / (n - 2)
    return b, math.sqrt(s2 / sxx), a0

def p2():
    say("\n== P2 (Hubble 1929: each rung a pan; slope of log2 d_H on log2 d_modern = 1)")
    bad = 0
    for rung in ["a", "b"]:
        rows = [(math.log2(m), math.log2(h)) for k, (r, h, m) in HUB.items() if r == rung]
        x, y = zip(*rows)
        b, se, a0 = olsse(list(x), list(y))
        kill = abs(b - 1) > 2 * se
        bad += kill
        say(f"rung ({rung}) n {len(rows)}: slope {b:.3f} +- {se:.3f}  (|slope-1|/se {abs(b-1)/se:.2f})"
            f"  sd(log2 d_modern) {st.stdev(x):.3f}{'  KILL' if kill else ''}")
        if rung == "b":
            r = [yy - xx for xx, yy in zip(x, y)]
            say(f"   corr(r, log2 d_modern) in (b): {st.correlation(list(x), [-v for v in r]):.3f}"
                f" (r = log2(d_mod/d_H)); a pan predicts 0")
    say(f"P2 {'KILLED' if bad else 'not killed'}")
    return bad

def p5():
    say("\n== P5 (a shared factor cancels from every same-rung ratio)")
    rb = {k: (math.log2(h), math.log2(m)) for k, (r, h, m) in HUB.items() if r == "b"}
    fa = st.mean([math.log2(m / h) for k, (r, h, m) in HUB.items() if r == "a"])
    def med(shift):
        errs = []
        for i, j in itertools.combinations(rb, 2):
            hi, mi = rb[i]; hj, mj = rb[j]
            errs.append(abs(((hi + shift) - (hj + shift)) - (mi - mj)))
        return st.median(errs)
    m0, m1 = med(0.0), med(fa)
    d = abs(m0 - m1)
    say(f"rung (b) median same-rung ratio error {m0:.12f}, with rung (a)'s {fa:.3f} levels taken out {m1:.12f}; diff {d:.1e}")
    say(f"P5 {'KILLED' if d > 1e-12 else 'not killed'}")
    return d > 1e-12

# ---------------------------------------------------------------- P3, P4 (Cosmicflows-4)
COLS = [("SNIa", (42, 47), (49, 52)), ("TF", (54, 59), (61, 64)), ("FP", (66, 71), (73, 76)),
        ("SBF", (78, 83), (85, 89)), ("SNII", (91, 96), (98, 101)), ("TRGB", (103, 107), (109, 112)),
        ("Ceph", (114, 119), (121, 125)), ("Maser", (127, 131), (133, 136))]
C = 299792.458; Q0, J0, H0 = -0.55, 1.0, 75.0; VMIN = 3000; SIGV = 300.0

def field(line, a, b):
    s = line[a - 1:b].strip()
    return float(s) if s else None

def muflow(v):
    z = v / C
    dl = (C * z / H0) * (1 + (1 - Q0) * z / 2 - (1 - Q0 - 3 * Q0 ** 2 + J0) * z ** 2 / 6)
    return 25 + 5 * math.log10(dl)

def load(path):
    rows = []
    for line in open(path):
        v = field(line, 23, 27)
        if v is None or v < VMIN: continue
        r = {"x": muflow(v), "ex": 5 / math.log(10) * SIGV / v}
        for lab, (a, b), (c, d) in COLS:
            m, e = field(line, a, b), field(line, c, d)
            if m is not None and e is not None: r[lab] = m
        rows.append(r)
    return rows

def p3p4(path):
    rows = load(path)
    say(f"\n== Cosmicflows-4: {len(rows)} galaxies with Vcmb >= {VMIN} km/s; mu_flow with q0 {Q0}, j0 {J0}, H0 {H0}")
    say("\n== P3 (each method a pan against the flow)")
    S = {}; bad3 = 0
    for lab, _, _ in COLS:
        g = [r for r in rows if lab in r]
        if len(g) < 30:
            say(f"{lab:5s} n {len(g):5d} (under 30, not tested)"); continue
        x = [r["x"] for r in g]; y = [r[lab] - r["x"] for r in g]
        b, se, _ = olsse(x, y)
        dil = -st.mean([r["ex"] ** 2 for r in g]) / st.variance(x)
        kill = abs(b) > 3 * se and abs(b) > 0.03
        bad3 += kill; S[lab] = (b, se, len(g))
        say(f"{lab:5s} n {len(g):5d}  slope {b:+.4f} +- {se:.4f}  ({abs(b)/se:5.1f} se)  expected dilution {dil:+.4f}"
            f"  x range {min(x):.1f}-{max(x):.1f}{'  KILL' if kill else ''}")
    say(f"P3 {'KILLED' if bad3 else 'not killed'} ({bad3} methods past the line)")

    say("\n== P4 (loops of slopes close)")
    labs = [l for l, _, _ in COLS]
    P = {}
    for A, B in itertools.combinations(labs, 2):
        g = [r for r in rows if A in r and B in r]
        if len(g) < 20: continue
        b, se, _ = olsse([r["x"] for r in g], [r[A] - r[B] for r in g])
        P[(A, B)] = (b, se, len(g))
        say(f"pair {A:5s}-{B:5s} n {len(g):5d}  b {b:+.4f} +- {se:.4f}")
    def pb(A, B):
        if (A, B) in P: b, se, n = P[(A, B)]; return b, se
        if (B, A) in P: b, se, n = P[(B, A)]; return -b, se
        return None
    bad4 = 0
    say("(i) triangles of methods, b_AB + b_BC + b_CA:")
    for A, B, Cc in itertools.combinations(labs, 3):
        t = [pb(A, B), pb(B, Cc), pb(Cc, A)]
        if None in t: continue
        c = sum(v[0] for v in t); se = math.sqrt(sum(v[1] ** 2 for v in t))
        kill = abs(c) > 3 * se and abs(c) > 0.03; bad4 += kill
        say(f"   {A}-{B}-{Cc}: {c:+.4f} +- {se:.4f} ({abs(c)/se:4.1f} se){'  KILL' if kill else ''}")
    say("(ii) each pair against the flow, b_AB - (s_A - s_B):")
    for (A, B), (b, se, n) in P.items():
        if A not in S or B not in S: continue
        c = b - (S[A][0] - S[B][0]); e = math.sqrt(se ** 2 + S[A][1] ** 2 + S[B][1] ** 2)
        kill = abs(c) > 3 * e and abs(c) > 0.03; bad4 += kill
        say(f"   {A}-{B}: {c:+.4f} +- {e:.4f} ({abs(c)/e:4.1f} se){'  KILL' if kill else ''}")
    say(f"P4 {'KILLED' if bad4 else 'not killed'} ({bad4} loops past the line)")
    return rows, S, P

if __name__ == "__main__":
    p1(); p2(); p5()
    if len(sys.argv) > 1:
        p3p4(sys.argv[1])
    with open("runs/ltr/ltr-run1.txt", "w") as fh:
        fh.write("\n".join(out) + "\n")
