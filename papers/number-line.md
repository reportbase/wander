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
- 7 October, eleventh: §4, irrational and transcendental numbers on a recursing line.
- 7 October, tenth: §4, observation costs calories (`plans/cal-plan.md`, run 1: logarithm of worth where detail
  fades fast; killed where it fades slowly).
- 7 October, ninth: §4, ARB run, the arithmetic baseline (`plans/arb-plan.md`).
- 7 October, eighth: §4, arithmetic on a line that recurses as needed, and a planned baseline (Tom: "how would we do
  basic math…"; "how would we create a baseline to compare these two").
- 7 October, seventh: §4, a number line that recurses as needed, against the ordinary line (`plans/anl-plan.md`, runs 1 and 2).
- 7 October, sixth: §4, the number line's depth is infinite, a perturbation's finite (Tom: "they conclude").
- 7 October, fifth: §4, "depth everywhere, and depth where needed" (Tom: the number line has depth everywhere, as its
  decimals; a situated reader recurses only into perturbations it has found). Lay of the land, no ruling.
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

**Depth everywhere, and depth where needed** (Tom, 7 October: "for the real number line, depth is just the number of
decimals"; then "no ruling, just creating the lay of the land, what we know to be true. situated observers only recurse
into known perturbations. there is no point to having depth everywhere, which what the number line does."). Laid side
by side, with no ruling on the word:

| | the number line | a situated reader |
|---|---|---|
| outward levels | the digits before the point: ones, tens, hundreds… | its window's reach past the corner |
| inward levels | the decimals: tenths, hundredths…, the same number of them for every number | entered only where the level above left something the reader can see |
| depth | everywhere: 3.000000 carries six inward levels that hold nothing | where needed, and only there |
| in the draw labs | the file that enters every level: 518 sweeps a shape | the file that enters a level only where something is left: 79 to 244 sweeps, with no loss |

- **The decimals are a grain.** Writing a number to n decimals reads it with a grain of 10⁻ⁿ: the number line's depth
  is its reader's dial, set once and applied everywhere.
- **A situated reader cannot know a perturbation before it sees it.** "Known" here means found: a remainder the
  current level left that the reader can detect. It then recurses there and nowhere else (draw: "recursion goes where
  the detail is").
- **The number line's depth is infinite; a perturbation's is finite** (Tom: "the number line has infinite depth, even
  though, perturbations are finite, they conclude"). The decimals never end, for every number. A perturbation ends: in
  the draw labs every shape's recursion stopped where nothing was left above the tolerance, 79 to 244 sweeps, not
  without end. So a situated reader's depth is finite because what it reads concludes, not because its levels run out.
  One nuance: whether digits end can depend on the reader's levels, not the thing. ⅓ never ends in decimals and is 0.1
  in base 3. A perturbation concluding is a fact about the thing; digits running on can be a fact about the levels used
  to write it.
- **A thought experiment: a number line that recurses as needed** (Tom: "lets create a number line that recurses as
  needed compared to just allowing an infinite number of decimals"; `plans/anl-plan.md`). Hold 1,000 numbers in binary.
  The ordinary line gives every number the digits its closest pair needs. The recursing line splits a cell only when it
  holds two or more, and pays for each split. With 5 numbers given a twin 10⁻⁹ away in an otherwise even line, the
  ordinary line writes 30 digits for every number. The recursing line writes about 10 for most and 30 only near the
  twins, a third of the cost (ratio 0.375). The gain shrinks as detail spreads: 0.45 with 50 perturbed places, 0.99
  with 500, and none for an evenly spaced line (1.10). For a set with every number inside a tight cluster it is small
  (0.77; the first run's prediction, under 0.3, was killed, because such a set is detail everywhere at a finer scale).
  So the ordinary line pays for its finest detail everywhere; a situated reader pays for it where it is.
- **The two senses of "depth" in this paper sit in this table.** One is the number line's inward levels, uniform. The
  other is a held thing's remainder, entered where found. They are not ruled the same or different.

**Still open.**

- **Why the draw labs' levels are octaves.** They are laid as doublings, as SPN's are: the layout's rule, not derived
  (SPN's open question, the ratio between rungs).
- **Depth in 3 and 4.** "None readable" assumes no held whole; a situated reader that builds one over time (SPN §2.1, "A
  system can change kind") would start to hold depth. When, and how much?
- **The walls between levels.** Read exactly at a doubling, the draw files miss by 1.9% of the departure, against a few
  millionths just off it (`draw/papers/tvf.md`, still open there).

### Arithmetic on a line that recurses as needed

Tom, 7 October: "how would we do basic math with a number line that only recursed as needed?" A reading, not a result.
On such a line a number is a **cell, not a point**: an interval as wide as its depth (3.14 held to two decimals is
somewhere in [3.14, 3.15)). A number that has concluded (3, ½, 0.25) is exact, a cell of no width.

- **Adding and subtracting: the coarser number sets the depth.** Widths add, so a sum is known only as deep as its
  shallowest part: 3.14159 + 2.1 is 5.2, not 5.24159. Scientists' significant-figures rule is this, by hand.
- **Multiplying and dividing: work in levels.** Write each number as a level and a place on it (a float's exponent and
  mantissa). Multiplying adds the levels and multiplies the places; dividing subtracts the levels; a reciprocal is the
  flip across the corner. Relative widths add, so a product is known to the significant digits of its least-known factor.
  Multiplication is native here, since it works on the levels, which are the logarithm.
- **A result that does not conclude is not expanded.** 1 ÷ 3 is kept as a rule and gives more digits only when more
  depth is asked for: digits on demand (exact, or lazy, real arithmetic).
- **Comparing: recurse until the cells part.** a < b is decided at the coarsest level first, going deeper only while the
  cells overlap; the cost is the depth at which they differ (the trie of `plans/anl-plan.md`).
- **Equality may never finish.** If a = b and neither concludes, the cells never part, and no finite recursion confirms
  it. For computable reals, equality is known to be undecidable. Asking whether a = b is asking whether a/b = 1, and a
  situated reader approaches its corner and never locates it. *A correspondence, to be checked, not a result:* the two
  may be one fact seen from two sides.

| practice | in these terms |
|---|---|
| significant figures | depth where needed, by hand, for + and × |
| floating point | levels and places, at a fixed depth everywhere |
| interval arithmetic | cells, with their widths carried through |
| exact real arithmetic | digits on demand; equality undecidable |

None of the operations is new. What is new is reading them as one situated reader's arithmetic, with the corner as
where it cannot finish.

**A baseline to compare the two lines** (planned first, then run as ARB, below).
- **The referee:** exact arithmetic (fractions, never rounded).
- **The contenders, given the same job** (the answer to the same requested depth):
  - the ordinary line: 53-digit floating point as computers use it, and separately a fixed depth set by the worst case;
  - the recursing line: cells with their own depth, exact numbers kept exact, digits on demand.
- **Tasks pulling different ways:**
  - a column of measurements at mixed depths;
  - cancellation, (10¹⁶ + 1) − 10¹⁶;
  - sorting numbers mostly far apart with a few close pairs;
  - a column of evenly spread numbers, the control, where no gain is expected;
  - ⅓ × 3 = 1.
- **Measures:** cost (digits stored and processed), correctness (is the truth inside the answer), and honesty (does the
  answer say how much it knows).
- **The prediction to fix before running:** the recursing line wins only where depth is uneven or where floating point
  hides a loss, and ties or loses a little on the control.

**Run (ARB, `plans/arb-plan.md`; predictions first, nothing killed).**
- **A column of 1,000 measurements at mixed depths:** the recursing line stored half as much (0.50) and its interval
  held the truth in 200 of 200 columns. Floating point's error exceeded what its digits imply in 200 of 200. The fixed
  line wrote 6 decimals for numbers known to 1 or 2, and its sum was off by about a million times what those decimals
  claim.
- **The control, all at one depth:** the recursing line cost a quarter more (1.25), for tags that told nothing new.
- **Cancellation, (10¹⁶ + 1) − 10¹⁶:** floating point gave 0; the other two gave 1.
- **Equality:** 0.1 + 0.2 = 0.3 is false in floating point and true exactly. √2 · √2 = 2 is false in floating point
  (2.0000000000000004) and undecided on the recursing line at every depth from 1 to 50.
- **So:** the recursing line is not better everywhere; it is the line whose answers say how much they know. The
  ordinary line's fault is less its cost than its claim.

**Observation costs calories** (Tom, 7 October: "but math is free, but real observation requires calories. how can we
add a cost calculation"; `plans/cal-plan.md`). Price each level a reader enters at c, value what it removes of the
unread remainder at V, and let detail fade by r per level. Then a reader enters a level only if it is worth its price.
That gives a third reason depth is finite, besides a thing that concludes and a grain that stops the reader: the next
level is not worth its calories. It holds even where the thing never concludes. In CAL run 1:
- **Where detail fades fast** (r = 0.3, 0.5), the priced reader stops at the best depth or next to it. Its depth grows
  by a fixed number of levels per doubling of V/c, within 4% of 1/log₂(1/r): depth is the logarithm of worth.
- **Where detail fades slowly** (r = 0.7), it was killed. The reader prices the next level from two noisy looks,
  underprices slow-fading detail, and quits early, below even "recurse everywhere". A better estimate would be a new run.

### Irrational and transcendental numbers on a recursing line

Tom, 7 October: "what would this mean for irrational and transcendental numbers, a recursive number line?" On a line
that recurses as needed every number is held the same way: a cell, and a rule for going deeper when asked. What sets
the kinds apart is what the rule is, and whether there is one.

| kind | its digits | its rule | on the recursing line |
|---|---|---|---|
| integers, and fractions that end (3, ¼) | conclude | none needed | exact, at a finite depth |
| other fractions (⅓, 1/7) | repeat for ever | the repeating block | after one period, every level is the same sweep again |
| algebraic irrationals (√2) | never conclude, never repeat | a short equation (x² = 2) | digits on demand, without end |
| computable transcendentals (π, e) | never conclude, never repeat | a series or an algorithm | digits on demand, without end |
| non-computable reals | no pattern that can be written | none | cannot be held at all |

- **Irrational numbers are not perturbations.** A perturbation concludes (above). An irrational never concludes, in any
  base: a fact about the number, unlike ⅓, which ends in base 3. A situated reader meets √2 or π as a rule, a finite
  description of infinite depth, unfolded only as far as asked.
- **Price sets how deep anyone goes.** By CAL's rule a reader stops where the next digit is not worth its calories. A
  carpenter uses π ≈ 3.14; spacecraft navigation uses about 15 digits; about 40 would give the circumference of the
  observable universe to within an atom. Every use of π stops at a priced, finite depth; π does not.
- **Equality can stay open.** e^(π√163) = 262537412640768743.99999999999925… agrees with an integer through 12
  decimals and is not one: a recursing line comparing the two stays undecided to depth 12 and parts at 13. Numbers
  that are equal and never conclude would never part (above, "Equality may never finish").
- **Most of the real line cannot be held.** Numbers with a finite rule can be counted, so they are vanishingly few among
  the reals. The rest, almost all of the continuum, have no rule, and no reader can produce their digits. The ordinary
  line's depth everywhere assumes them all; on a recursing line they do not appear. It holds exactly the numbers some
  reader could use.
- *A reading, not shown in general:* the best-known irrationals come from the unsituated whole. √2 is the diagonal at
  the corner (v = h = 1) and π the circle's half-turn. The circle (situation 1) holds them exactly, as a length and an
  angle, and a situated reader on the number line only approaches them, digit by digit: contained, and approached, as
  with the three landmarks. True of √2 and π; e does not fit as plainly.

The first four rest on standard mathematics: irrationality in every base, CAL's stopping rule, a known near-integer,
and the countability of computable numbers.

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
