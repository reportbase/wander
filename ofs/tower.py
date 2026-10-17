"""The tower of units: the worked example in observation-from-somewhere.md §9, after "Units within units".

A building of length L; two rooms read against it; two things in each room read against that room. Every reading is a
ratio, held as an exact fraction. The example's claims are checked exactly: the count of independent ratios, relations
across rooms from quotients of readings alone (one quotient per level), one length writing every other, scaling the
world moving every amount and no reading, and one misread link moving its whole room by one factor.
Run: python3 ofs/tower.py
"""
from fractions import Fraction as F

ok = True
def check(name, got, want):
    global ok
    good = got == want
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: {got} (stated {want})")

# the readings: each thing against its own hold
R = {"A": F(1, 2), "B": F(1, 3),                      # the rooms against the building
     "a1": F(3, 4), "a2": F(1, 2),                    # things in room A against A
     "b1": F(2, 3), "b2": F(1, 3)}                    # things in room B against B
hold = {"A": "L", "B": "L", "a1": "A", "a2": "A", "b1": "B", "b2": "B"}

def write(L, R=R):
    """Every length, given the one amount L and the readings."""
    out = {"L": L}
    for k in ("A", "B", "a1", "a2", "b1", "b2"):
        out[k] = R[k] * out[hold[k]]
    return out

# seven lengths, six readings: n - 1 independent ratios, grouped as 4 inside the 2 rooms and 2 between them
check("independent ratios for 7 lengths", len(R), 7 - 1)
check("inside the rooms", sum(1 for k in R if hold[k] != "L"), 4)
check("between the rooms", sum(1 for k in R if hold[k] == "L"), 2)

# relations from readings alone
check("a1/a2, same room: one quotient", R["a1"] / R["a2"], F(3, 2))
check("a1/b1, different rooms: two quotients", (R["a1"] / R["b1"]) * (R["A"] / R["B"]), F(27, 16))
W = write(F(12))
check("a1/b1 from the written lengths", W["a1"] / W["b1"], F(27, 16))

# one amount writes every other, wherever it is
check("L = 12 m writes a1", W["a1"], F(9, 2))
check("L = 12 m writes b2", W["b2"], F(4, 3))
L_from_b2 = F(1) / (R["b2"] * R["B"])                  # b2 = 1 m measured instead
W2 = write(L_from_b2)
check("b2 = 1 m writes L", W2["L"], F(9))
check("b2 = 1 m writes a1", W2["a1"], F(27, 8))

# scale the world: every amount by k, no reading
k = F(7)
Wk = write(12 * k)
check("scaled world: every amount by k", all(Wk[x] == k * W[x] for x in W), True)
check("scaled world: every reading unchanged", all(Wk[x] / Wk[hold[x]] == R[x] for x in R), True)

# one link misread: room B read as 0.3 of the building, not 1/3
Rm = dict(R, B=F(3, 10))
Wm = write(F(12), Rm)
check("misread link: b1 moved by", Wm["b1"] / W["b1"], F(9, 10))
check("misread link: b2 moved by the same factor", Wm["b2"] / W["b2"], F(9, 10))
check("misread link: b1/b2 unchanged", Wm["b1"] / Wm["b2"], W["b1"] / W["b2"])
check("misread link: room A untouched", (Wm["a1"], Wm["a2"]) == (W["a1"], W["a2"]), True)
check("misread link: a1/b1 off by the one factor", (Wm["a1"] / Wm["b1"]) / (W["a1"] / W["b1"]), F(10, 9))

print("all exact" if ok else "MISMATCH")
