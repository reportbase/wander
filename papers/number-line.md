# How people meet the number line

*Started 7 October 2026, at Tom's word: "put this in a new paper because i want to iterate over this." A working paper:
a reading, to be revised as it is worked over, not a ruling. It leans on SPN (`papers/serial-parallel-nowhere.md`) for
its terms (the situations 0–4, the corner, home, the horizon, the sweep, levels) and states nothing SPN does not
already hold except where it says so. Nothing here is in SPN yet; a part goes there only after it has been tested or
ruled.*

**Iterations**

- 7 October: first draft, from two of Tom's notes: the number line's two infinities (§1), and "maybe the way humans
  access the number line can best be understood as situation 3, the parallel situated perspective" (§5).
- 7 October, second: the aim stated (Tom: "my hope is that we can map these concepts onto the number line itself. so
  all the ideas of the serial-parallel paper even apply to the most basic thing we take for granted"). Added a short
  plain explanation of the corner (below; the corner itself is SPN's), named the two sides front and back, near and far, in place of "breadth" and
  "fineness" (§1), and added the map of SPN's ideas onto the number line (§2).
- 7 October, fourth: §4 rebuilt on the draw repository's depth labs (Tom: "we have already explored depth in draw
  repository in the labs. lets build on that in the number line paper"); the third draft's "depth is the digits"
  corrected: digits are precision, depth is a new sweep over a level.
- 7 October, third: depth (§4), from Tom: "I think depth is the least understood idea. my current working hypothesis is
  the world is what it is, something like 3d, … however, observation is different, it is breadth, depth and the sweep";
  and "lets iterate over the idea of depth in the number-line paper."

## The corner, explained plainly

Tom, 7 October, a first attempt: "the corner separates the frontside from the back side, the near field from the far
field, it separates where the signal is less than your h unit from where the signal is greater than your h unit." And:
"we need a nice short statement about the corner, what it actually is."

The corner is already SPN's: v = h, the flip's one fixed point (SPN §3). This adds nothing to it; it says the same
thing more plainly (Tom: "the corner is already known, we are just giving a more nuanced explanation of it").

**Draft (for Tom to refine):** *The corner is where the signal equals your unit: below it, the signal is a part of your
unit; above it, your unit is a part of the signal.*

On the number line the corner is 1. Below 1 a number is a fraction of the unit (½ is half of one); above 1 the unit is a
fraction of the number (1 is half of 2). The part and the whole change places there, and nowhere else. Everything else
follows from that: the two sides (near and far, front and back), the flip that swaps them (s ↔ 1/s), and why it is
yours (it is set by your unit, not by the line).

## 1. The number line has two infinities, and they are one

Tom, 7 October: "notice that number line as we know it is fully expressed breadth and fully expressed depth. but
neither is actually fully expressed because it extends infinitely in breadth and infinitely in depth."

Measured against its unit, 1 = h, the line runs out without end (1, 2, 4, … → ∞) and divides in without end (1, ½,
¼, … → 0). The flip, s ↔ 1/s, swaps the two: every step outward past 1 has a matching step inward below it. So the two
infinities are not two properties of the line. They are its back side and its front side, seen from the two facings,
and both are a situated reader's unreached ends (SPN, "By the corner", the three landmarks):

| | the number line | in SPN |
|---|---|---|
| in without end: 1, ½, ¼, … → 0 | less than the unit | the front side, the near field; home, approached |
| 1 | the unit, h | the corner |
| out without end: 1, 2, 4, … → ∞ | greater than the unit | the back side, the far field; the horizon, approached |

That is why neither is fully expressed. **The number line is a situated object:** it holds its unit exactly, it has
two ends it never reaches, and it cannot be held whole. Laid on the sweep, g = (2/π)·atan(s), the whole line fits in g
from 0 to 1, and the ends are still only approached (g → 0, g → 1). The sweep bounds the line without completing it.
The levels run both ways: R172 already has halvings toward home as well as doublings toward the horizon, and the inward
side of the line is those inward levels.

*On words* (second iteration). Tom's first note said "breadth" and "depth". The corner names the two sides already:
the inward side is the **front side, the near field**, where the signal is less than the unit; the outward side is the
**back side, the far field**, where it is greater (Tom: "the near field from the far field"; SPN §3.1, R165). "Depth"
stays SPN's word for a shape's difference from the circle (situation 2 only).

## 2. SPN's ideas on the number line

The aim (Tom): "map these concepts onto the number line itself. so all the ideas of the serial-parallel paper even apply
to the most basic thing we take for granted." A first map; each row is a reading until checked.

| SPN | on the number line |
|---|---|
| h, the unit held | 1 |
| the reading, s = v/h | a number, read in units of 1 |
| the corner | 1: the signal equals the unit |
| home | 0, approached from the near side |
| the horizon | ∞, approached from the far side |
| front side, near field | (0, 1): proper fractions |
| back side, far field | (1, ∞) |
| the flip, s ↔ 1/s | the reciprocal, which swaps the two sides and fixes only 1 |
| proportional before the corner | below 1, equal steps are equal parts of the unit |
| levels past the corner, dyadic | 1, 2, 4, 8, …: each doubling one level; by the flip, ½, ¼, … toward home |
| the sweep, g = (2/π)·atan(s) | the whole positive line laid on 0 to 1, the corner at ½, both ends approached |
| facings, 2^(signs) | positive numbers: 1; with negatives: 2; the complex plane (signs of the real and imaginary parts): 4 |
| situated, not unsituated | the line holds its unit but cannot be held whole (§1) |
| static and dynamic; 3 and 4 | seen at once as a stretch, or counted one at a time (§5) |
| depth | none in the bare line: depth is what a held thing puts into the line's levels, as new sweeps (§4) |

*Checked so far:* the corner, the flip and its one fixed point, the sides, and the levels are ordinary arithmetic. The
facings row is a reading: the complex plane's four quadrants are four copies of the unit sweep by the signs of the
real and imaginary parts, as SPN's "unit sweep, repeated" counts them; whether anything more of SPN carries to complex
numbers is not looked at here.

## 3. Is the number line ever "fully expressed"?

On SPN's unit line, a perturbation is "fully expressed at g = 1" (Tom, 6 October). The number line as people know it
looks fully expressed, every size, large and small, there at once. But by §1 it holds neither end, only the approach
to both. What people hold is the unit and the rule for going on (add one, halve again), not the line. *Open:* whether
"fully expressed" should be kept for a held whole (situations 1, 2) and the number line called "fully specified" (its
rule known) instead.

## 4. Depth: breadth, sweep and depth

Tom, 7 October: "I think depth is the least understood idea. my current working hypothesis is the world is what it is,
something like 3d, or maybe something different, but 3d is a good working model of reality. however, observation is
different, it is breadth, depth and the sweep."

**The world's three and observation's three are not alike.** The world's x, y and z are interchangeable: a rotation
turns any one into another. Observation's three are reached in order, each through the one before, as SPN's R125 says
of situated observation ("not a number of anything"):

| | what it is | reached through |
|---|---|---|
| **breadth** | the unit held, h: the scale | nothing; the reader starts from it |
| **sweep** | the relation v/h laid on 0 to π/2: scale removed | dividing by the breadth |
| **depth** | what the breadth and the sweep leave unaccounted for, entered as a new sweep over its own level | the address the sweep gives |

That both count three is probably a coincidence; observation is not claimed to be "3d".

**Depth is the remainder, entered as a new sweep.** SPN uses "depth" for a shape's difference from the circle
(situation 2 only; Tom, 6 October) and for what an address points back to once the division has taken the scale out
(SPN §2.1, "How the depth comes back after division"). Both are what is left once the breadth is divided out and the
relation laid on the sweep. The draw repository's labs (October 5–7; `draw/papers/tvf.md`, "Breadth and depth" and
§2.8) sharpen this into a definition, and measure it:

- **Depth is not more breadth.** "Packing leaves tighter is more breadth, not depth."
- **Depth is not precision.** "Cascade levels are precision: residuals of one breadth, over the same leaves. They are
  not depth."
- **Depth is the remainder, held by a new sweep over its own level.** "Every octave of a reader's reading held by a
  whole sweep of its own, the same sweep again with its own home, corner and far wall." And "a level holds only what the
  levels above left": nothing is stored twice.

So the earlier worry, that "remainder" is too broad because noise is a remainder too, has its answer there. A remainder
kept in place, at the same level, is precision. A remainder entered as a new sweep over its own level is depth.

**What the draw labs measured** (24 library shapes, read from a standpoint on each outline; the unit circle is the
shape's mean radius; `draw/papers/tvf.md`, "What the recursion found"):

| finding | measured |
|---|---|
| every level is the same sweep | each child sweep lies the same way in its level, at every level (the nested-fisheye lab) |
| depth beats breadth | at an equal count of values, better on 24 of 24 shapes, by 18× to about 5×10⁴ |
| depth holds at a distance | the nested reader's error flat at 0.7% from 4 to 128 steps away; one sweep's grew 23-fold (an earlier run, not re-measured) |
| the cost follows the shape | entering a level only where something is left: 79 to 244 sweeps instead of 518, to about a millionth of the departure |
| recursion counts hiding, not intricacy | the levels needed count how often the way in turns out of sight; the deepest library spiral needs six |

One caution from this paper's own record: the circle needed 129 sweeps there, where by the definition it should need
none. That was traced (SPN §2.1, "The circle needs no recursion") to the drawing tool's reading set-up for its circle, which departs from a true circle by about
0.0073/s; the 129 sweeps hold that artifact, not depth.

By situation, then: **1, the circle:** nothing is left, since the circle is the sweep; no depth. **2, a shape:** a
remainder, held, entered level by level where something is left; depth. **3 and 4:** no held whole to subtract from,
so no depth can be read. The world has detail there; the reader cannot hold it as depth (Tom's "1, 3 and 4 do not",
read as "none readable").

**On the number line: levels, precision and depth.** The draw repository's levels are levels of the number line itself:
an address in level k lies between the doublings 2^(k−1) and 2^k, read over 2⁻⁶ to 2⁶. A floating-point number holds
two of observation's three and not the third:

| | a floating-point number | in observation |
|---|---|---|
| the exponent: which doubling | the level; the rung (draw's rung is the IEEE 754 exponent of a row) | breadth, at that level |
| the mantissa: where within the doubling | the place on that level's sweep | the sweep |
| more mantissa digits | the same level, read finer | **precision, not depth** |
| a further sweep entered over a level, holding what the level above left | not in a float | **depth** |

So the digits of a number are precision, not depth: π = 3.14159… read to more digits is the same breadth read finer. A
bare number has levels and a place on them, but no depth, because there is nothing for it to depart from. Depth
appears only when a number line holds something that departs from its unit (a shape against its circle, a payload
against its address), and then it is held by entering the line's levels again, as whole sweeps, where the departure is
left. This agrees with §2's map: the number line by itself has the levels, and depth is what a held thing puts into
them.

*Corrected, third iteration, same day.* An earlier draft of this section said "on the number line, depth is the
digits". The draw repository's distinction between precision and depth shows that was wrong: digits read one level
finer; depth enters a new level. The halving question it raised (SPN nests the next level only in the back half, a
binary expansion halves wherever the remainder falls) is answered by the same distinction: halving within a level is
precision; entering the next level is depth.

**Still open.**

- **Why the draw labs' levels are octaves.** They are laid as doublings, as SPN's are: the layout's rule, not derived
  (SPN's open question, the ratio between rungs).
- **Depth in 3 and 4.** "None readable" assumes no held whole; a situated reader that builds one over time (SPN §2.1, "A
  system can change kind") would start to hold depth. When, and how much?
- **The walls between levels.** Read exactly at a doubling, the draw files miss by 1.9% of the departure, against a few
  millionths just off it (`draw/papers/tvf.md`, still open there).

## 5. People meet the number line as situation 3, within a window

Tom, 7 October: "maybe the way humans access the number line can best be understood as situation 3, the parallel
situated perspective."

**Why 3 fits.**

- **The number line is static.** It does not change while it is looked at, and a static system is read in parallel
  (SPN §2.1, "Static and dynamic").
- **People stand outside it and take a stretch in at once.** A ruler, or a line from 0 to 10, is seen in one look, not
  walked. That is R155's best move for a parallel reader: lay the addresses over the whole stretch first, then fill
  them.
- **One facing at a time.** A parallel reader confirms only its own hemisphere, and the other side is turned away (SPN
  §2.1, "Access limits the facings a reader can confirm"). On the number line the turned-away side is the negatives,
  which children meet years after counting.
- **The parallel reader's bell is centred on the unit.** ½·sech(ln s) is sharpest at 1, the unit h, and falls by half
  every doubling away from it. That matches the familiar compression of large numbers (Dehaene 2003) and the sharp
  grasp of small ones.

**Where it is more than 3.**

- **Before 3 comes 4.** Children learn numbers by counting, one at a time: serial, from inside. The line then settles
  into something seen at once: a system changing kind, dynamic to static, in a learner (SPN §2.1, "A system can change
  kind").
- **Past the window, serial again.** No one sees a million at a glance. Beyond what one look resolves, people count,
  compute or step by orders of magnitude: serial, by levels. This is the finite-resolution window of
  `plans/resolution-recursion.md`, parallel inside it and recursion past it.
- **A bounded line is a whole, not a window.** With a line marked 0 to 100, both ends are given, and people use the
  endpoints and the midpoint as references (proportion judgment; Barth and Paladino 2011). That is division by the
  whole, nearer the unsituated view than 3. It may be why NLE run 1 killed the corner's prediction
  (`plans/nle-plan.md`): Chan and Mazzocco's kindergartners were given bounded lines, and proportion judgment beat the
  corner model in 53% of those that departed from a straight line on 0–100. Their ½ would be a midpoint of a whole, not a
  corner of a unit. A reading of a killed run, not a rescue: the kill stands.

| how the line is met | situation | the reference used |
|---|---|---|
| counting | 4, serial | each next number |
| an open line, a stretch seen at once | 3, parallel | the unit, h; compressed past it |
| a bounded line, 0 to N given | the whole held | the endpoints and the midpoint |
| far past the window | 4 again, by levels | orders of magnitude |

**Serial becomes parallel at the reader's grain, and the reader can move it** (Tom, 7 October: "a serial signal becomes
a parallel signal … the pixel is ours, not theirs"; "the geometry should tell us what to expect from signals"; "could
the reader move his h unit like a slider to get a better read on the situation"). Measured on synthetic readers in
`plans/grn-plan.md`. Let h be the reader's grain and s the system's size against it:

- **Below the corner (s < 1)** structure comes as a chance per look, with probability s, and costs about 1/s looks:
  serial (runs 3 and 4).
- **At the corner** "two" becomes certain: the smallest size that cannot fit in one of the reader's grains (run 3).
- **Past it** structure comes in every look, about s grains at once: parallel (run 4). The average grows smoothly
  through the corner; what changes there is certainty.
- **The cost below and the yield past are each other's flip:** looks 1/s, grains s.
- **A reader that can slide its h** reaches its corner in about one look per doubling, about log₂(1/s) looks instead of
  1/s (run 4). On the number line that is the window moved by levels, the last row of the table above: the logarithm is
  the cost of moving the corner.
- **A reader given the shape** can read below its grain (runs 1 and 2). That knowledge is situation 2's, borrowed, and it
  blurs the corner rather than moving it.
- **h as a dial** (Tom: "H as a dial would be very interesting idea in itself"). Charge the reader one unit for each
  grain the system spans on each look. Then one sure reading costs (1 + s)·max(1, 1/s): least, 2, at s = 1, and the
  same at s and 1/s (run 5). The best setting of the dial puts the system at the reader's corner. Finer, the reader pays
  for grains it does not need; coarser, it pays in looks; and missing by a factor costs the same either way. That
  holds under this cost; field of view, light per grain and an optical floor would move it.

## 6. What would test it

The table predicts a split. **Open-ended estimates** (no upper bound given: "how far is 1000 from 0, if this is 10?")
should centre on the person's unit and compress past it, the corner model's shape. **Bounded-line estimates** should
centre on the midpoint, proportion judgment's shape. The same people should show both, by task. Under the lab rules
this would be a new run with its own prediction and kill condition, written before any data is seen; run 1's kill
stays on the record. Not planned yet.

*On synthetic readers (7 October, `plans/nls-plan.md`).* Three kinds built to differ (situated throughout, whole where
given, switching) are told apart by NLE's instrument at noise sd 8 (58%, 82% and 64% of each kind; nothing killed). The
switch, whole on the bounded line and compressed on the open one, is the robust signal; telling the corner from a
plain logarithm is the fragile one and is lost at sd 12. So a real-data run should test the switch first.

## 7. Open

- **The window's size.** Is it fixed (a span of levels, set by resolution) or does it grow with familiarity, as the
  switch point does in development?
- **Fractions.** The inward side, below 1, is the proportional front side in SPN, yet fractions are notoriously hard
  for children (Siegler and others, 2011). Is the inward side read as a second window, with its own unit (½, a tenth)?
- **Zero and the negatives.** Is 0 home, approached, or a point people hold exactly? Are the negatives the turned-away
  facing, met only by turning (serial), as §5 suggests?

## Sources

- Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
  shift. *Developmental Science* 14.
- Chan and Mazzocco (2024), the number-line data of NLE run 1 (osf.io/kqe2w; `plans/nle-plan.md`).
- Dehaene, S. (2003). The neural basis of the Weber–Fechner law: a logarithmic mental number line. *Trends in Cognitive
  Sciences* 7.
- Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations
  of numerical quantity. *Psychological Science* 14.
- Siegler, R. S., Thompson, C. A. and Schneider, M. (2011). An integrated theory of whole number and fractions
  development. *Cognitive Psychology* 62.
- Also `plans/neighbours.md` (Gilinsky, Schwartz) and `plans/resolution-recursion.md`.
