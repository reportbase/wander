# A second axis: the standpoint

*Superseded the same day by Tom's own list (SPN §2.1, "The situations restated, on the sweep alone"): 0 nothing known; 1 the circle; 2 shapes; 3 parallel, one hemisphere counted (outside); 4 serial, one point projected at a time (inside); 3 and 4 possibly known approximately; and "keep it simple to the octave and the sweep and the 90 turn and the logarithmic spiral only". Kept as the exploration that led there; its outside/inside geometry is not part of the paper.*

*6 October 2026, by Claude, from Tom's three ways to observe ("the entire system, or one hemisphere of the system, or
as someone exists as a member of a system, where you exist within it": an array or an equation; an object held in the
hand; a molecule of an apple), his "the hemisphere observer is not fully captured by our 5 situated observers", and
"lets explore your second axis idea". Exploratory: a reading, not a ruling. Checks: `python3 plans/standpoint/checks.py`.*

## The idea

SPN's situations (§2.1) are set by **what the reader knows of the breadths**, and SPN ties the standpoint to that:
"situation 3 … the only view from somewhere". The hemisphere observer breaks the tie. Holding an apple, you know it is
bounded, about how large, and that it has a back; what you lack is the back itself. That is a standpoint *with* the
breadths known, a cell SPN rules out.

So: two axes, not one.

- **Knowledge**, as now: both breadths known (1, 2), h known and v not (3), v within bounds (5), neither (4).
- **Standpoint**, new: **nowhere** (no position: the whole at once), **outside** a closed thing (facing it), **inside**
  (within it, surrounded).

## The grid

| | **nowhere** | **outside** (facing a closed thing) | **inside** (within it) |
|---|---|---|---|
| **both breadths known** (1, 2) | SPN's view from nowhere: an array, an equation (Tom). Uniform, no back, no horizon: the circle, k = 0 | **the hemisphere observer**: an apple held in the hand (Tom). The back hidden; the horizon is the **limb**, near and finite | inside a known enclosure: a room you know; SPN's reader in the hollow (§6.3) |
| **h known, v not** (3) | none: dividing needs a standpoint (R146) | facing a thing whose far extent is unknown: a cloud bank, a coastline seen from the sea | **the member**: a molecule of an apple (Tom); *Wander*'s reader among the stars. The mathematical horizon; recursion; the spiral (§3.3) |
| **v within bounds** (5) | none | facing a thing known only to be bounded | inside something known to end, but not where |
| **neither** (4) | impossible | impossible | impossible |

Examples in the grid beyond Tom's three are Claude's.

**What the grid changes.** SPN's "situation 3 is the only view from somewhere" becomes two separate statements. A
standpoint has a back that it does not see, in every non-empty cell outside "nowhere". Only an *unknown breadth* makes
its horizon the mathematical horizon, out of reach. The outside observer's horizon, the limb, is near and in view.

## The outside observer, measured

A ball of radius a, seen from a point at distance d > a (checked by brute force over 200,000 surface points):

| d/a | the visible cap's half-angle (at the centre) | share of the sphere seen | the half-angle the ball fills in view |
|---|---|---|---|
| 1.1 | 24.6° | 0.045 | 65.4° |
| 1.5 | 48.2° | 0.167 | 41.8° |
| √2 ≈ 1.41 | **45°** | 0.146 | **45°** |
| 2 | 60.0° | 0.250 | 30.0° |
| 10 | 84.3° | 0.450 | 5.7° |
| far away | 90°: a **hemisphere** | 0.5 | 0° |

- **"Hemisphere" is the far limit.** Up close you see less than half; only from infinitely far do you see a whole
  hemisphere. Holding a thing in the hand is in between, and the closer you hold it, the less of it you see.
- **The outside view has its own quarter turn and its own corner.** The cap's half-angle, arccos(a/d), and the
  half-angle the ball fills in view, arcsin(a/d), always add to 90°: complementary, θ ↔ 90° − θ, SPN's flip. They are
  equal, 45° each, at d = √2·a: the distance at which how much of the thing you see equals how large it looks.
- **Across the visible cap, the surface turns a quarter.** The angle between the line of sight and the surface runs
  from 0° (facing you) to 90° (grazing, at the limb), whatever the distance. The visible half is one sweep of 0 to π/2;
  the limb is its end.

## Outside and inside are one structure, flipped

Inversion in the sphere, x ↦ a²x/|x|², swaps outside and inside and leaves the surface fixed: distance d goes to a²/d.
That is SPN's flip s ↦ 1/s, with s = d/a, the distance in the thing's own radius.

- **The limb is set by the inside twin.** Seen from an outside point P, the limb lies in the plane through P's inverse
  point P′ = a²/d, inside the ball (pole and polar; checked: every visible point lies beyond that plane). What the
  outside observer sees is cut off by where its inside twin stands.
- **The corner between outside and inside is contact**, d = a: the surface, fixed by the flip. *Wander*'s BAL lab already
  found this: "the ball's corner is contact" (far off the share goes as s²/π, inverse square; at contact and inside,
  every address is filled).
- **SPN has measured the reversal.** In the hidden-sides runs (§6.4, DMAP), readers nested from outside a spiral shape
  number its outer wall first (levels 0 to 6); from a reader in the hollow, the order reverses (0 to 9), and "the outer
  face is never seen from the hollow".

So the hemisphere observer and the member may be the two facings of one standpoint structure, with contact as the
corner, as the front and back sides of a reading are the two facings of one relation.

## Open, for Tom to rule

1. **Is standpoint a second axis**, or is the outside observer a sixth situation in the one list? The grid suggests an
   axis, since every knowledge row has an outside and an inside version.
2. **Whose unit.** SPN's reading is v over the reader's h; the inversion above uses the thing's radius. They agree when
   the thing is the reader's own size, which may be why holding is the natural example. That needs stating, not
   assuming.
3. **What happens to "the only view from somewhere"** (§2.1, R139): restated as "the only view whose horizon is out of
   reach", or kept, with outside and inside as kinds of standpoint within situation 3?
4. **The hollow and the room** (inside, both breadths known): SPN treats the reader in the hollow under situation 3;
   in the grid it is a separate cell.
