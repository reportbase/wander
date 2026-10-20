"""The tower of units: the worked example in observation-from-somewhere.md §9, after "Units within units".

A building of length L; two rooms read against it; two things in each room read against that room. Every reading is a
ratio, held as an exact fraction. The example's claims are checked exactly: the count of independent ratios, relations
across rooms from quotients of readings alone (one quotient per level), one length writing every other, scaling the
world moving every amount and no reading, one misread link moving its whole room by one factor, and a second route
closing the loop and exposing it.
Run: python3 runs/ofs/tower.py
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

# closing a loop: a direct reading of a1 against b1 exposes the misread link
direct = W["a1"] / W["b1"]                              # read with both in view: the true ratio
chain = (Rm["a1"] / Rm["b1"]) * (Rm["A"] / Rm["B"])    # through the misread link
check("direct reading a1/b1", direct, F(27, 16))
check("chain through the misread link", chain, F(15, 8))
check("closure error = the misread factor", chain / direct, F(10, 9))
check("with no misreading the loop closes", ((R["a1"] / R["b1"]) * (R["A"] / R["B"])) / direct, F(1))

# inside a room: the two sweeps. Home at the origin. A thing has a centre c and an outline: points c + r_i*u_i along
# fixed rational unit directions u_i, r_i = s*(1 + rho*g_i). The central sweep, from c, receives the radii (as squared
# distances, to stay exact); the inscribed sweep, from home, receives directions, the thing's address that of its centre.
U = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(-4, 5), F(3, 5))]
g = [F(0), F(1, 2), F(-1, 3), F(1, 4)]
def outline(c, s, rho):
    return [(c[0] + s * (1 + rho * gi) * u[0], c[1] + s * (1 + rho * gi) * u[1]) for u, gi in zip(U, g)]
def central(c, pts):                                    # squared radii from the centre, over the first: the shape
    r2 = [(p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2 for p in pts]
    return [x / r2[0] for x in r2]
def address(c):                                         # the centre's direction from home, v/h
    return c[1] / c[0]
c1, c2 = (F(3), F(2)), (F(5), F(1))
base = outline(c1, F(1, 2), F(1, 5))
check("moving a thing changes its address", address(c1) != address(c2), True)
check("moving a thing leaves its shape", central(c2, outline(c2, F(1, 2), F(1, 5))) == central(c1, base), True)
check("reshaping a thing changes its shape", central(c1, outline(c1, F(1, 2), F(2, 5))) != central(c1, base), True)
check("reshaping a thing leaves its address (its centre stays)", address(c1), F(2, 3))
check("the central sweep cannot read the size", central(c1, outline(c1, F(7), F(1, 5))) == central(c1, base), True)
# its size in the room's units: the thing (breadth s) and the room's wall (breadth Wr) read at once at one distance d
for d in (F(2), F(9), F(1000)):
    thing, wall = F(1, 2) / d, F(4) / d                 # two readings held at once, one denominator
    check(f"size in room units at d = {d}", thing / wall, F(1, 8))

# to move the furniture is to write: one known step b writes the room in the step's unit
def place(m1, m2, b):
    """A landmark read at slopes m1 from home and m2 after a step b along h: its place in b's unit."""
    x = b * m2 / (m2 - m1)
    return x, m1 * x
X, Y = F(3), F(2)                                        # the landmark, in metres (unknown to the reader)
m1, m2 = Y / X, Y / (X - 1)                              # the two readings; the step is 1 m
check("one known step writes the landmark's place", place(m1, m2, F(1)), (X, Y))
check("an unknown step leaves the scale free (taken as 2, all doubles)", place(m1, m2, F(2)), (2 * X, 2 * Y))

print("all exact" if ok else "MISMATCH")
