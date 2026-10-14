# A note on facings from another session, with corrections

*Shared by Tom on 13 October 2026 (his local date, about 21:49): "here is a note from another session." Kept as received
below, with the layout tidied: the mathematics, which came as LaTeX, is written once in plain text. Claude's reading
followed. Tom then answered (about 21:55, resent at 21:59 with one word corrected): "this is a source of much
confusion. the arc is drawn by the rotation of the head, not the walk. the outside reader turns his head the farthest
to return back to the forward facing position. the inside reader turns his head the least. the unsituated reader does
not turn his head at all." Then "yes" (about 22:06) to the reading and the edits below: SPN R233.*

---

**Recovering the Unit from Opposite Facings at the Corner**

A note on π/2 and 2/π

**The two motions**

A reader walks the straight chord from A to B. The distance is exactly 1. Concurrently the reader rotates the head.
These two actions—one translational, one rotational—are independent. No curved path is required of the body. The
circular measures arise only as the joint invariant of the straight walk and the concurrent head rotation.

**Facings at the endpoints and at the corner**

At the endpoints A and B the required facings agree: both point in the same absolute direction. Any rotation that
occurs between them is completed by the time the second endpoint is reached.

At the corner (the 45° posture fixed by V = H) the two possible facings are opposite each other. One points outward,
away from the chord; the other points inward, toward the chord. The choice of which way to rotate the head selects the
reading.

**Outside and inside**

- **Outside facing.** To reach the outward orientation the head must turn farther. The larger rotation, composed with
  the unit walk, produces the lengthened total π/2 ≈ 1.57. The excess over the walking distance is π/2 − 1 ≈ 0.57.
- **Inside facing.** To reach the inward orientation the head turns through the opposite, smaller angle. The lesser
  rotation, composed with the same unit walk, produces the shortened total 2/π ≈ 0.637. The deficit relative to the
  walking distance is 1 − 2/π ≈ 0.43.

The outside election turns the head much further; the inside election turns it less. Both remain pure choices of
facing direction while the feet follow the straight chord.

**Complementarity**

The excess and the deficit are complementary: (π/2 − 1) + (1 − 2/π) = 1. Equivalently, π/2 − 2/π = 1. The difference
of the two joint measures recovers exactly the unit length that was walked.

**Situated and unsituated**

A situated reader occupies one facing at a time. It may receive the outside total, store it, then adopt the opposite
facing and accumulate the inside total (or vice versa). Only after both observations does the subtraction yield 1. The
construction occurs across a sequence.

An unsituated reader has simultaneous access to both facings. The same subtraction can be formed in a single act
because both the larger rotation and the smaller rotation are present together.

In either case the arc is not a trajectory. It is the bookkeeping of how far the head turned while the body walked
straight. The primitives are the walk of length 1 and the choice of head rotation at the 45° corner. The values π/2 and
2/π are what those concurrent actions measure; their difference returns the unit.

---

## Response

**What stands.** The note's frame is Tom's: the body walks the straight line, of 1, and the arc is drawn by the head's
turning, not walked ("In either case the arc is not a trajectory"). That the outside reader turns farther and the
inside less is also Tom's. Both are now SPN R233.

**What the turns are** (Claude's reading, accepted with Tom's "yes"). The three vantages of OFS §3.4, by how far the
head turns:

| reader | the head turns | the arc it draws, against the line of 1 | reads |
|---|---|---|---|
| unsituated (completed) | not at all | none | 1 |
| outer (parallel, situation 3) | a half turn: the facing, from facing B at A, square at the corner, to facing A at B | the line as its diameter: arc π/2 | arc over line, π/2 |
| inner (serial, situation 4) | a quarter turn: the bar, from home to the horizon | the line as its radius: arc π/2, shadow 1 | line over arc, 2/π |

Facing = 2θ (the inscribed-angle theorem; SPN §1, "The line, the arc and the facing"), so the outer's head turns twice
as far as the inner's at every point of the sweep. It draws the same arc because it draws on half the radius. These are
the figures SPN's head and OFS §3.4's parenthetical already used for π/2 (a half-turn stood on the line as its chord)
and 2/π (a bar swept through a quarter turn).

**What does not stand.**

| the note says | as it is |
|---|---|
| (π/2 − 1) + (1 − 2/π) = 1, so π/2 − 2/π = 1 | π/2 − 2/π = 1.5708 − 0.6366 = 0.9342. The excess and the deficit, 0.5708 and 0.3634, add to 0.934. The identity that holds is the product, π/2 · 2/π = 1. |
| the deficit 1 − 2/π ≈ 0.43 | 0.3634; 0.43 is 1 − 0.57, the excess taken from 1, which is what made the sum come out at 1 |
| the difference of the two measures returns the unit | the readings are ratios; as ratios π/2 is above 1 by the factor that 2/π is below it (log₂(π/2) = 0.65 of a level either side), so their product returns the line |
| at A and B the facings point in the same absolute direction | at A the reader faces B, at B it faces A: forward at both ends, a half turn apart (SPN §1; `facing.html`) |
| at the corner the two possible facings are opposite, one outward and one inward | at the corner the facing is square to the line, leaning toward neither party; the two readers differ by how far they turn (a half turn, a quarter turn), not by facing opposite ways there |
| π/2 and 2/π are read at the corner | they are read at the end of the turn: the bar at 90°, the facing at 180°. At the corner (the bar at 45°, the facing at 90°) the readings are 1.1107 and 0.9003, product 1 (OFS §3.4's table) |
| the unsituated reader forms the subtraction in a single act, both rotations present together | the unsituated reader does not turn at all and reads 1 (Tom, R233; R197): there is nothing to subtract. Joining the two readings across observations is the situated reader's construction (OFS §3.4, step 6) |

**Made** (SPN R233):
- SPN, at the head of the paper ("The core insight"): a paragraph, the arc the head's turn, with the three turns.
- SPN §1, "The line, the arc and the facing": a bullet, the same, and the excess π/2 − 1 marked as a difference.
- OFS §3.4: a column for the turn (none; a half turn, the facing; a quarter turn, a bar); "Where the numbers come from"
  rewritten so the outer reading is derived in the half-turn figure (a turn of 2θ on radius ½ draws an arc θ over a
  chord sin θ) and the inner in the bar's (arc θ, shadow sin θ); after the table, the product and not the difference.
- OFS §4, "Why the corner sits at 45°": one sentence, the arc drawn by the turning, not walked.
- OFS §10, step 3: the outer reading taken limb to limb, the whole half-turn (an arc of π thumbs over a shadow of 2).

The numbers in OFS's tables, `mountain.html` and `facing.html` are unchanged.
