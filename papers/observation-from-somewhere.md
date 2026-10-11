# Observation from Somewhere: one corner, the reader's circle, and two address spaces

*Tom Brinkman, with Claude. Prepared 11 October 2026 for external review.*

*This paper gathers the key ideas of five working papers into one self-contained account. Those papers are
`serial-parallel-nowhere.md` (SPN), `number-line.md`, `v-and-h.md`, `inverse-square.md` and `physics.md`, all in
`papers/`. It also draws on the test plans in `plans/`. The working papers keep the full record: every ruling with the
author's words, every correction, and every claim later withdrawn. This paper states only the current view, marks the
standing of each claim, and includes what failed. Where it and a working paper differ, the working paper's latest dated
entry is the record, and the difference is an error here. Appendix B maps each section to its sources. Revised the same day after a first evaluation (`plans/ofs-review-1.md`): V = H stated as a rule of representation, the
Euclidean choice and the scale-invariance premise (S) made explicit, the half-Cauchy named, and the three levels of
physics claim set apart. Then, after a second evaluation, a candidate single principle (§12.1), offered as a reading.
Then, at the author's word that it is the primary result (SPN R200), the Cauchy as addresses, not payload (R47; SPN
§4.3), stated in the abstract and §5 with its proof (Proposition 6), and the Cauchy's missing mean read as SPN reads it:
a question about the payload asked of addresses, not a census the horizon withholds.*

---

## How to read the claims

Every claim carries one of these marks.

| mark | meaning |
|---|---|
| **[proved]** | a proposition with a proof here, from the definitions alone |
| **[derived]** | a proof from named premises; the premises are listed and are where to push |
| **[ruled]** | a choice or reading the author has made, stated so the reader can reject it |
| **[exact]** | exact arithmetic, checked in a plan |
| **[data]** | measured on published data, prediction written before the data was opened |
| **[synthetic]** | measured on simulated readers built for the purpose |
| **[illustration]** | shown in a demo page; shows a thing is possible, tests nothing |
| **[open]** | not settled |

**Keep the case.** Lowercase **h** and **v** are *fill levels*, numbers from 0 (empty) to 1 (full). They are the
geometry and have no scale. Uppercase **H** and **V** are *breadths*, amounts. The same holds for a distance d, a size
Δ, a radius a or R, a light L and the reader's angular step ε: these are physics. The amounts are (v·V) and (h·H), so
(v·V)/(h·H) = (v/h)·(V/H). So **v/h is not V/H**. The only way from the geometry to an amount is a fill level times its
breadth, and that needs the breadth. Every conclusion below that passes from geometry to physics names the amount it
borrows. Earlier drafts of the working papers often blurred the two, and most of their corrections are of that kind.

---

## The core insight: three vantages, one line

*Foregrounded 11 October (Tom: "also forgeground into observation-from-somewhere"; SPN R191, R193–R199) [ruled].*

Classical mathematics and physics assume a completed perspective, best known as the equation or the drawing on the
page. There are three vantages, each with its own geometry, and they are easily conflated.

| vantage | its geometry | its reading of a line of true breadth 1 |
|---|---|---|
| **completed** (classical; the view from nowhere) | the circle; every breadth held; no facing | **1** |
| **outer hemisphere** (parallel; situated) | one facing, taken in at once; the hemisphere turns away from the reader | **π/2** |
| **inner hemisphere** (serial; situated) | one facing, swept from home: the fisheye, the Cauchy; the hemisphere turns toward the reader | **2/π** |

*Where the two numbers come from* [derived on the arc drawing; which reading belongs to which vantage is ruled,
R193]. Stand a half-turn on the line as its chord: a chord of 1 has radius ½, so the half-turn's arc is π·½ = π/2,
and read as arc over chord, the hemisphere turned away gives π/2. Sweep a bar of 1 through a quarter turn and average
its shadow on the line: the mean of the shadow over the turn is (2/π)·∫₀^{π/2} cos θ dθ = 2/π, and read as the
average facing, the hemisphere turned toward gives 2/π. Their product is 1. (Evaluation 2, `plans/ofs-review-2.md`,
asked for this.)

**The chain, step by step** (Tom, 11 October; SPN R193–SPN R199). Each step rests on the one before.

1. *The line has a true breadth, 1.* That is the completed view's reading (SPN R193).
2. *Each situated vantage reads it with a facing.* The outer hemisphere, turned away, reads π/2; the inner hemisphere,
   turned toward, reads 2/π; and π/2 · 2/π = 1 (SPN R193; the numbers derived above).
3. *Reading 1 assumes no facing.* The true breadth is what is read when nothing is turned toward or away from the
   reader. A situated reader always has a facing, so no situated observation reads 1 (SPN R197).
4. *Only the unsituated observer has no facing, so only it knows the true breadth.* A blueprint is the example: drawn
   from no standpoint, every line at its true length to one scale, nothing turned toward or away from anyone (SPN R198).
5. *To hold 1 is to hold both hemispheres in hand at once* (SPN R194), *which no single observation can do* (SPN R195).
   That is what "the view from nowhere" means: the true breadth belongs to no standpoint.
6. *So a situated reader must construct the truth from multiple observations* (SPN R196, SPN R199): the hemisphere turned
   away and the one turned toward, read in turn and joined. The construction represents the breadth 1; it does not
   observe it.
   A telescope is the working example: one exposure is one facing from one standpoint; the survey is the construction.
   Not every combination builds: re-exposing the same field lowers the noise and adds nothing; other pointings joined
   at their overlaps give the shape up to a scale; only a second standpoint with a known baseline (parallax, the
   Earth's orbit) gives a distance, because the baseline is a bridge (§7). An illustration, not a test
   (`plans/ofs-review-2.md`).
7. *There are therefore two ways to the true breadth, and only two:* held, unsituated, as in a blueprint; or
   constructed, situated, from several observations.

Each vantage's reading is right from where it stands. Many paradoxes come from reading one vantage's geometry as
another's, most often the completed view used as if one observation held it (the working paper `vantages.md` collects
them). The rest of this paper is the geometry of the two situated vantages and where it meets physics.

**What the completed view costs** [ruled; from the archived *The Relation Space* §6, §17]. Neither party to a relation
performs the comparison; something else settles it. A balance settles two weights and its pull cancels from the
answer. A page, a shared scale or an equation settles them too, but lends its own terms to the answer, as a spring
scale's spring does. Written as h² + v² = 1, h and v are not related to each other: each is related to the equation,
which supplies the common scale, the constant 1 and the equals sign. **The equation is a third party**, and the
completed view is what that third party makes. Two consequences follow. A completed account holds the whole figure at
once and cannot state a rate, since what is held all at once has no order of arrival; a situated account states the
rate of arrival and cannot hold the figure. And the corner, which the situated reading turns on, is an unremarkable
point of the completed drawing: the drawing displays no landmark there.

## Abstract

A reader that stands somewhere knows its own breadth and not the breadth of what it reads. This paper works out what
that one fact forces for the situated vantages, and tests where the result meets physics.

The object throughout is a pair of shares, h of H and v of V, each on [0, 1]. Every way the two can relate, from all h
to all v, is the *sweep*. Because neither share can pass 1, the sweep can go past the point v = h only by h emptying
while v stays full. That point, the *corner*, is the one place the swap v/h ↔ h/v leaves fixed, and every sweep passes
through it [proved].

A situated reader has exactly one breadth, its own H. For a relation to exist the other side must be given a breadth
too, and H is the only one the reader has, so it must set V = H [derived; close to definitional, §12]. With that one act
the corner lies at radius H/H = 1 whatever H was chosen. Drawn as a rigid bar of Euclidean length 1 in that one unit, the
relation's every attitude satisfies h² + v² = 1: a unit circle no one put a number into (the Euclidean choice is an
assumption, §3).

Inside the circle the reader reads in proportion, the near field at true scale. Past the corner, if no scale is
preferred, Cauchy's functional equation leaves only one lay by address count, the logarithm: every doubling gets the
same number of addresses [derived; the step to scrutinise is named, and it is where the argument passes through
amounts]. Drawn by length instead, the whole far field can be fitted in one more H, reality in 2H [ruled]. Proportional
inside, logarithmic outside: two address spaces, one corner between them, and no further corners.

Held whole, with no standpoint, the bar's even turn is the circle. Swept from home and read as v/h, the same even turn
counts out the Cauchy and draws the fisheye [derived, given the even turn]. One uniformity lies behind both. Situated
geometry is the Cauchy; unsituated geometry is the circle.

**The primary result: the Cauchy consists of addresses, not payload** [the cancelling and the statistics proved,
Proposition 6; the reading ruled, R47 and SPN R200]. Whatever arrives along a ray, at whatever reach ℓ (an amount, in the reader's
one unit), the reader reads (ℓ·v)/(ℓ·h) = v/h. The reach cancels in every single reading, not on average, so the readings tell rays apart, not
points. The Cauchy is therefore laid before anything arrives and is the same whatever arrives: it is where the reader
can put what arrives, never what arrives. Its order survives every change of payload, so it has a median, the corner. A
mean is a sum of sizes, a question about the payload, and addresses carry no size, so it has none. That is why the
Cauchy has a median but no mean.

The physics correspondences are kept apart from the geometry and tested on published data or exact arithmetic. Light
falls two levels per level of distance on nearby Hipparcos dwarfs, as the inverse-square law requires [data]. In the
cases worked, the near field of an extended source turns exactly at the corner of the (size, distance) pair when the
light counted is a share, and off it when it is not [exact cases; the general rule is open]. Many predictions were
killed, and they are listed.

---

## 1. The one object: a share on [0, 1]

Everything here is built from **a share of all of something, none of it, or anything in between**. Take two such
shares, each of its own whole. They have no units, and neither knows the other's whole. Some examples:

- the fraction of a tank filled, and the fraction of a day gone;
- the share of a push that is vertical, and the share that is horizontal;
- the part of a road behind, and the part ahead;
- the share of a page a picture covers, and the share of the scene it shows.

Drawn geometrically, the two shares are h (horizontal) and v (vertical). H is the whole h is a share of, and V the whole
of v. A reader *is* H, its own breadth. h is not the reader but the reader's side of a relation.

**Where a reader can stand.** What a reader knows of the two breadths sets its situation, not where it is in the world.

| situation | H | V | standpoint |
|---|---|---|---|
| 0 | known | — | no relation, no h, nothing to read |
| 1 | known | known, equal to H | none: the circle, read evenly from nowhere |
| 2 | known | known, unequal | none: every other shape, also from nowhere |
| 3 | known | not known | a parallel reader: one hemisphere taken in at once |
| 4 | known | not known | a serial reader: one point at a time |

**The core claim: three vantages** [ruled, R191]. Classical mathematics and physics assume a completed perspective,
best known as the equation or the drawing on the page. There are three vantages: the completed one (situations 1 and 2),
the outer hemisphere (situation 3, parallel) and the inner hemisphere (situation 4, serial). Each has its own geometry:
the circle, the bell, and the fisheye (the Cauchy). One line of true breadth 1 shows it in three numbers [ruled, R193]:
the outer hemisphere, turned away, reads π/2; the inner, turned toward, reads 2/π; and π/2 · 2/π = 1. The classical
breadth, 1, is held only with both hemispheres in hand [ruled, R194], which no reader can do in one observation; that is why the
completed view is the view from nowhere [ruled, R195]. A reader can construct it from multiple observations [ruled,
R196], but cannot observe 1: reading the true breadth means reading with no facing, and only the unsituated observer has
none [ruled, R197]. They are easily conflated, and many paradoxes come from reading one
vantage's geometry as another's. Those collected so far, each marked by its standing and by what was already known, are
in the working paper `vantages.md`.

Situations 1 and 2 are the *view from nowhere*, the classical setting with all breadths in hand. They name a state of
knowledge, not a place anyone stands. Situations 3 and 4 are the *view from somewhere* and are what this paper is about.
Neither the serial nor the parallel reader knows how many things there are (N), and both meet horizons.

**Terms used throughout.**
- *Situated*: holding one breadth (H) and not the other's (V); situations 3 and 4.
- *Address*: a place in the reader's layout where a reading can be put, laid before anything arrives.
- *Payload*: what arrives at an address.
- *The hand* (the working papers' picture of the two): hold a hand flat (all h) and turn it upright (all v), the
  fingers spread between. Each finger is an address; a ring on it is the payload. Turning the hand changes no ring, and
  changing the rings changes no finger.
- *Lay*: a rule placing each reading at a position r in a drawing; *room* is how much of the drawing a stretch of
  readings receives, measured either by length or by number of addresses (each use says which).
- *Facing*: which way the relation's bar points, one of the corner's two sides in each freedom; a sweep from all h to
  all v is one facing. (Not to be confused with the *facing angle* of §2, the direction the reader faces along one
  sweep.)
- *Level*: the first level runs from home to the corner; past it, each level is one doubling of the reading.

**Geometry before payload.** The addresses a reader lays (the sweep, the corner, the levels, and the Cauchy that
counts them, §5) do not depend on what arrives at them. What arrives, the *payload*, is met at the addresses. Every "if" belongs to the payload, including which
side of the corner a given reading falls on. This paper is about the addressing. It is not a theory of perception or of
mind, and it makes no claim about the geometry of spacetime.

---

## 2. The sweep and the corner

**The sweep.** In one observation neither breadth changes. h runs from 0 to 1 and so does v. The sweep is every way h
and v can relate, from all of H (v empty) to all of V (h empty). Coming out from home, v fills against a full h. It can
fill only until it too is full, at v = h. The relation can go on only by h emptying against a full v. So the sweep has
two halves, joined at one point, and the change from one to the other is forced by the cap at 1 alone [proved].

**The reading.** On the first half the reader reads v in terms of h, the ratio v/h on [0, 1]. On the second half it
reads h in terms of v, the ratio h/v on [0, 1]. (SPN writes s = v/h; this paper keeps v/h.) Reading the pair the other
way round, the *swap* or *flip*, sends v/h to h/v.

**Three drawings of one sweep.** What the sweep fixes is the ratio of the two shares, so each pair (h, v) stands for a
ray of pairs with the same ratio. The ray can be drawn at different points, and the working papers use three:
- *the square*: each share capped at 1, the larger one full. This is where "v fills against a full h, then h empties
  against a full v" is literally true, and the corner is (1, 1);
- *the line* h + v = 1, the share by the sum, with the corner at (½, ½);
- *the arc* h² + v² = 1, a bar of fixed length, with the corner at (1/√2, 1/√2).

All three pass through every ratio once and meet the corner at v/h = 1. Statements about the sweep and the corner are
about the ratio and hold in any drawing. Statements about lengths, turns or areas belong to one drawing and say which.
The cap argument above is made on the square. §3 says why a situated reader's natural drawing is the arc.

**Proposition 1 (the corner separates the sides)** [proved]. Let the reading be x = v/h on [0, ∞), from home (x = 0)
toward the mathematical horizon (x → ∞, h → 0). Then x = 1 is the only point the swap x ↦ 1/x leaves fixed. The swap
carries the front side [0, 1) onto the back side (1, ∞) point for point, and every sweep from home passes through x = 1.
The point needs neither H nor V.

*Proof.* The swap is its own inverse and reverses order. If x < 1 then 1/x > 1, and the reverse. x = 1/x with x > 0
gives x = 1. A sweep from home grows continuously from 0, so it reaches 1 before it can pass it. And x = 1 is v = h, a
comparison of two fill levels, unchanged when both are scaled together. ∎

The corner is ordinary arithmetic, v/h = 1. Nothing about it is special beyond what follows from that.

**Proposition 2 (bounded readings flip at the corner)** [(a) proved; (b) derived on R162]. (a) Let a reader hold x in two registers: x itself
where x ≤ a, and 1/x where x > a. Both registers stay within [0, 1] if and only if a = 1. (b) Let f map [0, ∞) into
[0, 1], strictly increasing, and treat the two sides alike, f(1/x) = 1 − f(x). Then f(1) = ½, f puts the front side
below ½ and the back side above it, and past the corner f(x) = 1 − f(1/x).

*Proof.* (a) The registers take values [0, a] and (0, 1/a); both lie in [0, 1] exactly when a ≤ 1 and 1/a ≤ 1. (b) At
x = 1 the condition reads f(1) = 1 − f(1). The rest is monotonicity and the condition rewritten. ∎

Part (b) rests on a ruling, **R162** [ruled]: a situated reader's reading treats the two sides alike. Its *knowledge*
does not, since H is known and V is not; the ruling puts the symmetry in the reading. Without it a reading such as
x/(2 + x) would be bounded with its middle at x = 2. Examples that satisfy it are v/(v + h) = x/(1 + x) and the glowing
disc's share of its full light, x²/(1 + x²) with x its radius over its distance (§8.2 writes the same light with
distance over radius, where it decreases).

**The series stop at the corner** [proved]. 1/(1 + x²) = 1 − x² + x⁴ − … converges for x < 1 and diverges for x > 1;
past the corner the expansion in 1/x converges instead. The reason is that the kernel's singularities sit at x = ±i,
at distance one from home. So an expansion about home cannot be carried past the corner. This is a property of the
expansion, not a break in the function.

**Why 45°: the facing** [ruled: a reading of the arc drawing]. A straight line from A to B passes through every ratio
of the two, as the quarter arc does. The arc adds a second degree of freedom the line lacks: which way the reader faces
along the way, toward B at A and toward A at B. Let θ be the sweep's angle from all-h. The working papers measure this
direction as an angle, the *facing angle*, and take it to be 2θ, from 0° (toward B) to 180° (toward A); this is a definition, chosen so that the facing runs a half
turn while the sweep runs a quarter. At the corner, θ = 45°, the facing is 90°, square to the line,
leaning toward neither party. One sweep is a quarter by its angle and a half-turn by its facing angle (`facing.html`). The arc
stands off the line's midpoint by 1 − 1/√2, its greatest distance, at the corner.

**Comparing two readings without dividing** [proved; from the archived *The Relation Space* §25]. For two readings
A = (h_A, v_A) and B = (h_B, v_B) let D(A, B) = v_A·h_B − v_B·h_A, the disagreement. With h_A, h_B > 0, D = 0 exactly
when v_A/h_A = v_B/h_B (the same ratio), and D > 0 exactly when v_A/h_A > v_B/h_B (order). Comparing a reading with its
own swap, D = v² − h², which is zero exactly at the corner. So sameness, order and the corner need no division; only
the size of D needs more, since it changes when either reading is rescaled.

**Every pair has its own sweep** [ruled]. Any two parties have a sweep and a corner. A corner means nothing until its
pair is named. In particular, the point where a thing is one of the reader's steps across, Δ/(d·ε) = 1, is the corner
of the (size, step) pair. It is set by amounts, so it is physics: the *resolution limit*. It is not the corner of the
reader's sweep of the other. Much of the working papers' early text conflated the two.

---

## 3. The reader's circle

This section is the paper's central derivation (SPN Proposition 1.2, ruling R190).

**Premises.**
- **(P0) A relation has two parties, each a share of an assigned breadth**: h of H, v of V. Assigned is not known. The
  value of v on [0, 1] does not depend on how big V is ("v needs no V", R189), but v must be a share *of something*.
- **(P1) A situated reader chooses one breadth, H, and holds no whole of the system.** Any H will do; it must choose
  exactly one.
- **(P2) A level carries no measure**: nothing on it but its two ends, their order and the flip between them.

**Proposition 3 (the unit circle by necessity)** [derived from P0–P2, with (c) a definition of the drawing and (f)'s single 2 a reading].

(a) *The reader must set V = H.* By (P0) V must be assigned a breadth for there to be a relation. By (P1) the reader's
H is the only breadth it has to assign. Without the assignment there is no second party, only h. *What this means:* V = H
is a rule of representation, the reader's own breadth used as the unit for the other party. It is not a claim that the
other's physical breadth equals H. The other has whatever breadth it has; where that differs from H, every amount the
reader reads is off by the true V/H (§7). The rule constructs a relation calibrated in one unit; it discovers nothing
about the world.

(b) *The corner is at radius 1* (on the arc drawing, and at position 1 on either lay of §4). It lies one H from home, measured in H: H/H = 1, whichever H was chosen. No number is
put in, and the size of H never enters. Which H is chosen is a free convention: a reader with unit λH reading a world
scaled by λ receives the same readings, address for address (SPN Proposition 3.6), so nothing in the readings can tell
it which rung it stands on.

(c) *The circle.* With V = H both shares are measured in one unit, so the relation can be drawn as one bar of a fixed
length, 1: all h lying flat, all v upright, every attitude between them one mix. Its length is 1 at every attitude, so
every mix satisfies h² + v² = 1. This is the arc drawing of §2, and taking h and v as the bar's two components is a
definition, not a theorem. What V = H adds is that the drawing is a circle and not an ellipse: with two units the same
bar would trace an ellipse stretched by V/H. The square and the line remain valid drawings of the same ratios. *An assumption made here:* one unit for both
directions makes the axes commensurable, but a "fixed length" also needs a choice of norm. The square is the bar of
fixed length under the largest-component norm and the line under the sum norm; the circle is the Euclidean choice. The
circle follows if the attitudes are taken to be turns of one rigid bar, since the Euclidean norm (up to scale) is the
only one left unchanged by every turn. That moves the burden to why the sweep is a turn, which the facing (§2) motivates
and does not prove. Until that is settled the circle is the canonical drawing, not a forced one.

(d) *The facings.* Once H and V share a unit, nothing prefers one side of either freedom, and each freedom has two
facings, the corner's two sides. That gives 2 × 2 = 4 facings: the bar sweeping horizontal, vertical, horizontal,
vertical and back, which is the circle closed. Add a second v, v₂, read against the same h and also set to H: then
h² + v² + v₂² = 1, the sphere, with 2 × 2 × 2 = 8 octants and a triple corner h = v = v₂ in each. In general, n
freedoms each set to the one chosen H give 2ⁿ facings. The equation and the count come from the same act. *The count
needs no angle* [proved; from the archived *Degrees of Freedom* §5.1]: each join between facings flips one freedom's
side, and a closed walk must flip each side an even number of times to return, so the facings are the 2ⁿ corners of an
n-cube walked as a Gray code. *What is borrowed:* that the 2ⁿ facings tile a circle or sphere in equal shares (a quarter
turn each, π/2 of the sphere's area each) is the Euclidean measure of (c), not part of the count.

(e) *The flip is forced, and V = H puts the corner where the amounts are equal.* The corner v = h and the flip there
follow from the cap at 1 alone (§2); they are geometry and need no V. In general the amounts are equal, v·V = h·H, where
v/h = H/V. Under V = H that is v = h. So the corner the reader finds in its own amounts is the geometric corner, and it
is the edge of the unit circle.

(f) *Diameter 2, and the doublings.* The corner has two sides and only two. The reader's own level runs from home to
the corner in every facing: radius 1, diameter 2, the near field. Measured in the reading v/h, the next level runs from
1 to 2 and level k ends at 2ᵏ. (On a drawing the level edges sit elsewhere: at 1 + k·ln 2 on the logarithmic lay, at
2 − 2⁻ᵏ on the in-place lay; §4.) The author reads the 2 across the reader's own level and the 2 between levels as the
same 2, the corner's two sides [ruled: a reading].

**Where the reader lives** [ruled]. The reader lives *in* the circle its own choice creates, at home at its centre. It
is not the circle. The circle read evenly from no standpoint is the view from nowhere; how the reader reads from inside
it is the fisheye (§5).

**The ratio between levels** [D.1 derived on its premises; the rest ruled]. The working papers long asked what fixes the
ratio between a reader's levels. Two pieces bear on it.

*Proposition D.1* [derived]. Premises: a level has only its two ends, their order and the flip f ↦ 1 − f (no measure);
a point or set of cuts is supplied by the geometry when every symmetry of that structure keeps it (Klein's test); a
nested level has its parent's structure. Then the only subdivision supplied is the cut at the corner into two. Any
interior point other than the corner can be moved anywhere in its open half by an order-keeping map that commutes with
the flip, so no finite set of b − 1 ≥ 2 cuts is kept. By the nesting premise each half is again a level, so the
subdivisions supplied are repeated halvings. Supplying three parts needs an added measure.

*What D.1 does not give.* Binary branching is not by itself a ratio of 2 between level edges: where the edges fall
depends on how the readings are laid out. SPN's Appendix D records this caution (9 October). The current view (R189,
R190) takes the levels as doublings of the reading v/h and the logarithm past the corner as fundamental, and §4 offers a
derivation of the logarithm from "no rung is preferred". Whether that closes the gap is one of the questions put to
reviewers (§12).

*What another ratio costs* [reading; from the archived *The Radix* §5, §11]. A reader whose own step multiplies by r
steps exactly one level per step when the levels are powers of r: a reader with r = 3 matches levels of three exactly,
as one with r = 2 matches doublings. So any ratio but the halving can be matched, and D.1 says what it costs: the
reader's step is then a measure added to the level. A layout whose levels are uneven (a calendar's 100, 12, 31, 24,
60, 60) matches no single step and costs a table of its levels, which a reader given nothing does not have. The Radix
put it in one line: "uniformity can be free; variation has to be represented somewhere, in the reader's grain or in
information handed to it." Its evidence was one synthetic instrument, so only the principle is carried here.

**Escapes** (where the conclusion does not follow):
- a reader that keeps two independent breadths and chooses neither has no relation (not P0). It lies outside the
  framework rather than against it;
- a level with more structure than the flip, such as a measure (not P2), allows other subdivisions;
- plain proportion past the corner keeps true scale but cannot fit the far field on bounded addresses.

**Standing.** (P0) is the framework's first assumption. (P1) defines the situated reader. (P2) is assumed and is the
open premise. Step (a) may strike a reviewer as close to a definition, and the authors agree it is close. The claim is
only that a relation needs two assigned breadths and a situated reader has one, so the assignment is not a free modelling
choice but the only one available. Steps (b)–(f) then follow, with (c) a choice of drawing and (f)'s single 2 a reading.

---

## 4. Past the corner: the logarithm and two address spaces

**The question.** Past the corner the flip makes the reading h/v on [0, 1]. The flip does not say how that reading is
laid out. Write the far reading as v/h ≥ 1 and let a lay place it at position r(v/h), where r counts addresses from
home. Require only that farther is laid farther, and that the corner is at the unit circle, r(1) = 1.

**Proposition 4 (the logarithm past the corner)** [derived; the link is the step to scrutinise].

*The link.* The room (number of addresses) the lay gives between v/h and λ·v/h (λ ≥ 1) depends on λ alone, not on where
the reading sits. Two reasons are offered:
- *by (P1), through amounts.* A fill-level ratio does not change with H. What changes is the reader's readings as
  amounts: under the calibration V = H, a far thing at distance d is read as d/H, and choosing a different H multiplies
  every such reading by one factor. A lay whose room depended on where a reading sits, and not only on the ratio, would
  then depend on which H was chosen, which Proposition 3(b) says is a free convention. *This reason crosses from
  geometry to amounts, and its bridge is V = H.*
- *by (P2).* No measure is carried past the corner, so nothing supplies a scale for the room to depend on.

This is "no rung is preferred" applied to the lay. Stated exactly, the premise is

> **(S)** r(λx) − r(x) depends on λ alone, for all x, λ ≥ 1.

Proposition 4 proves that (S) with monotonicity forces the logarithm. It does not prove that a situated reader must
satisfy (S). Monotonicity, a fixed corner and a matched slope are not enough by themselves: r(x) = 1 + ln x + α(ln x)²,
α > 0, meets all three and gives each doubling a different number of addresses. Such a lay would make the reader's
address differences depend on which H it chose, which is what (P1) is offered to exclude. Whether (P1) and (P2) entail
(S), or (S) is an added principle, is question 1 in §12.

*The arithmetic.* Write g(λ) = r(λ) − 1. Then r(λ·μ) − r(μ) = g(λ) for all λ, μ ≥ 1, so g(λμ) = g(λ) + g(μ). That is
Cauchy's functional equation in multiplicative form. With g increasing, its only solutions are g(λ) = c·ln λ. So
r(v/h) = 1 + c·ln(v/h): equal room per doubling, c·ln 2. A further condition, that the far lay join the near field's
slope with no kink at the corner, gives c = 1 (inside the corner r = v/h, whose slope at 1 is 1, as is that of
1 + ln(v/h)). The flip fixes where the two spaces meet; the smooth join is this added condition, not a consequence of
the flip.

*Room means addresses.* The room here is the number of addresses a doubling receives, not its length.

**Reality in 2H** [ruled; the in-place lay is one drawing, not shown to be forced]. Drawn by length instead, the far
field can be fitted in one more H: under V = H it is in the reader's own unit, and the flip folds everything past the
corner into [0, 1] once more. The *in-place lay*,
which places a far reading at a length (not an address count) 2 − h/v from home, gives each doubling half the length of the last, so the whole far field out to the
mathematical horizon lies between radius 1 and radius 2. Its room per unit of v/h is (h/v)², the flip's Jacobian; level
k past the corner (v/h from 2^(k−1) to 2^k, k = 1, 2, …) receives a length 2^−k. It holds the same addresses as the logarithmic lay, the same number per
doubling, so they crowd toward radius 2 without end. A reader with a finite step stops at its *far horizon*, where its
addresses run out. The in-place lay is the reader's own lay by length; the logarithmic lay is the same addresses by
count. (The working papers first called the in-place lay "not the reader's own". That confused length with count and
was withdrawn on 11 October.)

**Two address spaces** [derived, on Proposition 4]. Inside the corner the addresses are proportional: the near field at true scale, v
read in terms of h. Past it they are logarithmic: the far field, h read in terms of v, every doubling the same number of
addresses. The corner is where one gives way to the other, with no kink. Neither space is chosen: the cap forces the
corner and the flip, and no preferred rung forces the logarithm.

**One corner, plain doublings** [ruled, R188–R189]. "One corner" means one corner intrinsic to the relation, the one
fixed point of the flip; it does not rule out other thresholds a particular reader's layout might have. There is only
one such corner, the split between the first level (home
to the corner, the near field) and the second. Past it the levels are plain doublings laid side by side. They have no
corners of their own, nothing nested in them and nothing read again inside them: no depth and no recursion. Earlier
working-paper readings that gave each level its own corner, or counted depth as nested sweeps, are superseded and kept
in SPN as the record.

*Which doubling* [proved; from the archived *One Reader* §2.1a and *The Order of Limits*]. Two operations are called
doubling. The scale doubling sends v/h to 2·v/h. The angle doubling, the reading of twice the turn, sends v/h to
2(v/h)/(1 − (v/h)²). Near home they agree (2(v/h)/(1 − (v/h)²) ≈ 2·v/h when v/h is small); at the corner they part, the
angle doubling sending the corner to the mathematical horizon. The levels past the corner are scale doublings.

| drawing of the same addresses | measured by | bounded? | corner at |
|---|---|---|---|
| the fisheye | steps of turn | yes, a quarter turn | the middle (half the turn) |
| the in-place lay | length | yes, 2H | the middle (radius 1 of 2) |
| the logarithmic lay | address count | no | radius 1, the start of the even doublings |

---

## 5. The circle and the Cauchy: addresses, not payload

**Proposition 5 (the Cauchy and the fisheye from one sweep)** [derived, given the even turn on the arc drawing].

With V = H the relation is a bar of length 1. A reader at home sweeps it from flat (all h) to upright (all v) in even
steps of its turn, and at each step holds one reading, v/h.
1. Even steps in the turn give uneven readings. Near home a step barely changes v/h. At the corner, v = h, the sweep is
   halfway through its turn. Near upright each step changes v/h more and more, without bound as h → 0.
2. When the bar turns a little, v/h changes by that turn times 1/h². Since h² + v² = 1,
   1/h² = (h² + v²)/h² = 1 + (v/h)².
3. *Counting gives the Cauchy.* Steps per unit of v/h go as 1/(1 + (v/h)²). Over one facing's quarter turn that is
   2/(π(1 + (v/h)²)) on [0, ∞), the half-Cauchy. Half its steps fall before the corner and half after, so the corner is
   the half-Cauchy's median, and the flip leaves the count unchanged. Over the reader's two facings, with v/h signed, it
   is the standard Cauchy 1/(π(1 + (v/h)²)) on the whole line; its median is home (0), and the corners at ±1 are its
   quartiles.
4. *Drawing gives the fisheye.* Place each reading at its step of turn rather than at its value. Near home the world is
   at true scale; it compresses gently toward the corner, and past it more and more of the world falls into each step.
   The mathematical horizon sits at the edge of the turn and is never reached.

(In classical terms, step 2 is the derivative of the tangent, and the readings are the tangent of a uniform angle. The
working papers avoid the inverse tangent in a sweep, because a sweep is swept step by step from home; it is the
shortcut that turns a sweep into an index.)

**The primary result: the Cauchy consists of addresses, not payload** [Proposition 6 proved; that it makes the Cauchy
the reader's addresses ruled: R47 (26 September), restated by the author on 8 October (SPN §4.3) and named the primary
result on 11 October (SPN R200)].

> **The Cauchy is not the payload; it is the address to the payload.** (R47)

**Proposition 6 (address and payload)** [proved; (b)–(d) from the archived *Reader Geometry as Addressing*,
Proposition 14]. Call a statistic of a set of readings an *address statistic* if it uses only their order (the ranks,
the median, the quartiles, which side of the corner each falls), and a *payload statistic* if it uses their sizes (the
mean, every sum).

(a) *Nothing that arrives changes the Cauchy.* Let whatever arrives along the ray at each step of the turn sit at any
   reach ℓ > 0, an amount, different on every ray and unknown to the reader. In the reader's one unit (V = H) its two
   components are ℓ·h and ℓ·v, and the reading is (ℓ·v)/(ℓ·h) = v/h. The reach cancels in every single reading, not on
   average. So the readings of Proposition 5, their count 2/(π(1 + (v/h)²)) and the fisheye are the same whatever
   arrives, and are fixed before anything does: the readings tell rays apart, not points.

(b) *Address statistics ignore the payload.* Let X be a finite set of readings and f any strictly increasing map of them
   (any change of the sizes that keeps their order). The ranks of f(X) are the ranks of X, so every address statistic
   picks the same reading: median f(X) = f(median X) for an odd count. Conversely, if two sets have the same ranks, some
   strictly increasing f carries one onto the other, so the ranks keep exactly what survives every such change, and
   nothing more.

(c) *Payload statistics do not.* The mean commutes with f only where f is affine on the data; for a convex f,
   mean f(X) ≥ f(mean X), with equality only when f is affine there or X is constant (Jensen).

(d) *The Cauchy is an address law.* Over one facing its median is v/h = 1, the corner, and its quartiles are
   √2 − 1 and √2 + 1, a flip pair; its mean diverges, since ∫₀^M x·2/(π(1 + x²)) dx = (1/π)·ln(1 + M²) grows without
   bound. It supports order, not sums.

*Proof.* (a) is the line above. (b) and (c) are immediate, the converse in (b) by interpolating monotonically between
the matched readings. (d): the count over one facing has distribution (2/π)·atan(v/h), which is ½ at v/h = 1 and ¼, ¾ at
tan(π/8) = √2 − 1 and tan(3π/8) = √2 + 1; the integral is elementary. ∎

**What it means** [ruled; SPN §4.3]. The sweep counted evenly is the Cauchy, and each reading in it is a ray, an address,
laid before anything arrives. What arrives is the payload, met at the addresses, and none of it is in the Cauchy. In the
hand (§1): spread the fingers evenly by turn and read each as v over h, and the readings are the Cauchy; nothing of the
rings is in it.
- *The median is an address.* The corner is where the readings divide in half. Order, ranks, quartiles and the corner
  are address statistics, and they ignore what arrives.
- *The missing mean is a question about the payload asked of addresses.* A mean is a sum of sizes; the Cauchy's
  readings carry no size, so it has no answer. The median, the address question, is always there.
- *More looking buys more addresses, not more payload.* A finer sweep lays more readings: "precision about where and
  when, and never about what" (*The Cauchy*, 22 August, §14d, an earlier paper of the author's quoted in SPN §4.3).
  What is at the addresses comes only from a payload held beside them, through a bridge (§7).

**Where it holds** [open beyond it]. Proposition 6(a) takes the payload to be something met along one ray, a value at
an address. Occlusion and contact use more than that: that the sweep is a straight line and the payload is the first
thing it meets (SPN §4.3, "The boundary"). For those, the addressing results are untested.

**Situated is the Cauchy; unsituated is the circle** [derived as stated; the reading is ruled]. Unsituated, nobody
stands anywhere: the bar is held whole, all four facings at once, and its end traces h² + v² = 1. Every point is like
every other: there is no home, no corner set apart and no horizon. Situated, one reader at home sweeps one facing and
reads v/h: counted, the Cauchy; drawn, the fisheye. Home, the corner and the horizon appear because the reading is taken
from somewhere. It is the same bar under V = H, held whole or swept from home: the Cauchy is the circle's even turn
received as a ratio.

**One uniformity behind both** [ruled]. Proposition 5 assumes the turn is stepped evenly. That is a choice of weight on
the sweep. But it is not a weight chosen for the Cauchy: stepping the turn evenly is what makes the circle uniform in the
first place. One choice, uniformity, lies behind the circle and the Cauchy alike. Two things are distinct here: the circle's own
symmetry under turning, and a reader's choice to sample it in even turns. The second respects the first but is not
implied by it; a reader may sample unevenly. The claim is therefore that a reader who sweeps the Euclidean circle in
even turns gets the Cauchy, and that this is the sampling that prefers no attitude. Other fair weights exist, for instance
the straight line's share v/(v + h), and any weight fair to the two facings puts the corner at its middle (Proposition
2(b)). They give other drawings, not the Cauchy.

**What being situated costs** [reading, on Proposition 6]. A situated reader keeps order and loses sums: from somewhere
there is a reading at every distance, and no census of the whole. The Cauchy's median and its symmetry under the flip
are what survive. The Cauchy is the extreme case, an order law with no sum.

**Two absences, kept apart** [reading; after the archived *Browsing the Fisheye*, read with SPN §4.3]. Two different
things are missing from a situated reading, and they are easily run together. The amounts, V and H, are missing from
*every single reading*: v/h cancels them, as it cancels the reach of whatever arrives (Proposition 6(a)), and only a
bridge (§7) restores them. The total of the whole is missing because the reader's set *has no end*: the mathematical
horizon is never reached, so no census can be taken. The first is a fact about the ratio; the second a fact about
delivery. The Cauchy's missing mean belongs to the first, not the second: it is not a census that more delivery would
complete. Over the reader's two facings the mean of n readings is distributed exactly as one reading, whatever n
[classical], so averaging never settles. The readings are addresses, and a mean asks them for sizes they do not carry.

**Known already.** The Cauchy as the image of a uniform angle (the gnomonic image of uniform measure on a hemisphere),
and its invariance under Möbius maps, are classical (Knight 1976; McCullagh 1996): a pinhole projecting evenly spread
directions onto a line gives the Cauchy (Cuadras 2002), and Möbius maps of Cauchy variates are Cauchy (Pitman and
Williams 1967). Its missing mean, long called a pathology, has its history in Stigler (1974); that the mean of n Cauchy
variates is again Cauchy, and that order statistics follow every increasing map, are textbook facts. What this paper
adds is the reading: which reader, knowing what, gets which object, and that the object is the reader's addresses, not
its payload.

---

## 6. Level of detail, and the choice of H

**The count is the level of detail** [ruled, R190]. Reading the near field in proportion would mean dividing H into some
number of parts. The reader never knows that number, and the geometry does not use it. Past the corner, likewise, what
is forced is that each doubling gets the same count, not what the count is. In both spaces the count is the *level of
detail*. The geometry gives the forms (proportional, logarithmic); the level of detail gives the count.

**What sets it** [ruled; physics where amounts enter]. All else equal, a smaller thing shows less detail. A thing of size
Δ met at distance d, read by a reader whose angular step is ε, spans Δ/(d·ε) addresses. Past one step across it is
resolved to k = log₂(Δ/(d·ε)) levels, one fewer per doubling of distance. This is a ratio of amounts, so it is physics,
and its switch at Δ/(d·ε) = 1 is the resolution limit, not the corner. Nothing is requested or chosen: the size and the
distance set the level a thing shows.

**H is a zoom, not an escape** [a reading, worked out at the author's question; it assumes the reader's count of addresses is finite]. Any H will do, and every H gives the same circle,
corner, 1 and 2. So nothing stops a reader choosing a very large H, which would put everything it will ever look at
inside the near field, at true scale, with no logarithm. The cost is the level of detail. The near field spreads the
reader's finite count of addresses evenly across H. With H very large each address spans a great extent, and everything
at the reader's own scale falls inside the first address beside home and is a point. A small H holds the small at true
scale and the large logarithmically; a large H holds the large at true scale and loses the small. Since there is always
something smaller than any H's first address, as there is always something larger past any corner, no H holds every
scale at true scale with a finite level of detail. The best move is to set H to the scale of the thing being read, which
puts that thing at the corner. An eye focusing and a telescope zooming do this. (An earlier form, from the archived
*Degrees of Freedom* §5.15: for a thing at x read from a standpoint at d, the kernel d/(x² + d²) is largest when d = x,
v = h. Prior art for the count as the level of detail: the hyperbolic browser draws only nodes at least a pixel across,
a bound independent of how many there are (Lamping, Rao and Pirolli 1995); mipmaps halve an image per level (Williams
1983); and a web-map tile's key has one digit per level, "the length of a quadkey equals the level of detail"
(Microsoft, Bing Maps Tile System).)

**A cost model agrees** [synthetic, GRN runs 3–6, `plans/grn-plan.md`]. A model-free reader whose pixel is its step
reads "two points" with probability min(r, 1), where r is the pair's separation in steps: certain from one step across,
by chance below it. Charged one unit per step spanned per look, a sure reading costs (1 + r)·max(1, 1/r): least, 2, at
r = 1, and the same at r and 1/r. A reader that slides its H by halvings reaches one step across in about log₂(1/r) looks
instead of 1/r. These are one cost model on simulated readers.


**More points, less seen** [exact, with one prediction killed; `plans/cei-plan.md`, after the archived *One Reader* and
*The Order of Limits* §3.2]. A parallel reader looks side-on at N points spaced evenly round a circle of radius R and
reads each one's position across its view to a step ε_len; only ε = ε_len/R enters (a ratio of amounts, its bridge the
radius). Neighbours at angle θ from the middle of the view stand about (2π/N)·cos θ apart, which is at least ε while
cos θ ≥ εN/2π, so it resolves R(N) = (N/π)·arccos(εN/2π) of them. With x = εN/2π that is (2/ε)·x·arccos x, which peaks
at x ≈ 0.6522 at about 1.1222/ε points and then falls to none at N = 2π/ε: past the peak, more points mean fewer told
apart. Checked by brute force at ε = 10⁻³ and 10⁻⁴: the formula holds to within 2 points, the peak's height to 0.11%,
nothing is resolved past 2π/ε, and the share depends on εN alone. The peak's place was predicted within 2% of 4.098/ε
and came in 2.6% low at ε = 10⁻³, a narrow kill on a flat maximum, kept as recorded. The address never overflows; the
resolution does: the completed view's N against what one standpoint resolves.
---

## 7. From addresses to amounts: what physics supplies

**The calibration error** [derived]. Under V = H the amounts equal the fill levels numerically, which is why the two
are so easily confused. Where the true V differs from H, every amount is off by the factor V/H, the same on both sides
of the corner. The addresses are exact; the amounts are not. In one observation a reader cannot tell V = 10² from
V = 10¹⁶.

**Bridges** [ruled]. Physics supplies amounts across observations: the reader's own travel, a law with a known constant,
a known kind (a standard candle), or a fact shared with another reader. Each is a named bridge from fill levels to
amounts. Every physics result below names its bridge.

**A shared fact buys exactly one factor** [exact; `plans/tgt-plan.md`, after the archived *The Order of Limits* §4.4].
Two readers share one closed figure. Reader A records its part as edges, each an exact direction and a length counted
in its own hold H_A; reader B records the rest in its own hold H_B. Neither knows the other's hold. Closure, the one
shared fact, gives H_A·S_A + H_B·S_B = 0, where S_A and S_B are the sums of each reader's counted edges; so the two sums
are parallel and opposite, and **H_B/H_A = |S_A|/|S_B|**. Closure recovers the ratio of the holds and nothing more: both
holds scaled together leave every count unchanged. It fails only when each part closes on its own. Checked: on 2000
random closed polygons the ratio comes back to 5×10⁻¹⁵; the archive's three values, 0.5, 2 and 3.7, come back as
0.5000, 2.0000 and 3.7000; rounding counts to a step of 10⁻¹ to 10⁻⁴ of the unit gives errors of 10⁻¹ falling to
2×10⁻⁴. This is the denominator exchange (`denominator-paradox.md`) made exact: between two private rulers, the shared
fact purchases the one factor that crosses.

**Recovering places from the sweep** [illustration; the geometry is classical]. `flight.html` flies a reader at a height z
over a flat ground (the page itself writes the height as v). For each of a few posts it holds only readings: how far down and how far across, each against the
distance ahead, rounded to its pixel. It keeps the readings from one height's worth of travel back. The two standpoints' lines cross
at the post; the reader's own travel is the one length, so places come out in units of that travel. With no rounding, recovery is
exact. With a pixel step it holds to within 10% out to about twice the height ahead and gives out beyond, until only a bearing
is left. This is triangulation on a baseline (Snellius 1617; the geometry of two views, Longuet-Higgins 1981). It is
included to show that the sweep's readings, with one bridge, are enough to place things.

---

## 8. Physics correspondences, tested

**The rules** [ruled, 10 October]. Evidence is published measurement or exact arithmetic. The demo world in this
repository (`index.html`, `labs.html`, `res/`) was built for looks; it illustrates and never counts as evidence. The
prediction is written before the data is opened. A killed prediction stays killed; a fix is a new run with its own
prediction.

**Three levels of claim, kept apart.** (1) *Correspondence*: a physical formula has the same form as a relation in the
framework. (2) *Agreement*: measurements fit a prediction written before they were opened. (3) *Explanation*: the
framework says why a law holds, or predicts what physics does not already supply. Everything in §8 is at level 1 or 2.
Nothing here reaches level 3: the inverse-square law, the disc's near field and the planets' roundness are all already
explained by physics. A correspondence recognised after seeing a formula is weak evidence; the tests that count are
those that could have gone the other way, and the killed ones in §10 show that some did.

### 8.1 The inverse square as a calibration case

The inverse-square law is derived in physics from conservation and three dimensions of space, and its exponent is bounded
experimentally (within about 10⁻¹⁶ of 2 for the electric force). It is not this paper's to test. It is used as a
calibration case: a law whose unsituated and situated accounts (the radiance theorem, view factors) are already exact,
so that the paper's terms can be checked where the answer is known.

**In levels** [exact, from the law]. Write light and distance as log₂. Each doubling of distance quarters the light:
−2 levels of light per level of distance. For things spread evenly in three dimensions, number grows 3 levels per level
of distance, so 1.5 levels of number per level of light.

**On real stars** [data].
- *MAG* (`plans/mag-plan.md`; Hipparcos, HYG v3.8, parallax distances): G0–G5 dwarfs within 23 pc lose 2.02 levels of
  light per level of distance (83 stars). K0 giants gave 1.93, on a sample later found not to be complete.
- *GCN* (`plans/gcn-plan.md`; Gaia Catalogue of Nearby Stars, about 125,000 main-sequence stars by colour): all four
  predictions were killed, by a quality cut that depends on distance and by white dwarfs inside the colour bands. Read
  afterwards without the cut, each kind gives 2.93–3.00 levels of number per level of distance within 100 pc, alike in
  the plane and toward the poles, and about 1.5 by light. This reading is after the run and is not ruled.
- *CNT* (`plans/cnt-plan.md`; Hipparcos to V = 7.3): about 1.2 levels of number per level of light, not 1.5, alike in
  the plane (1.229) and toward the poles (1.227). The cause is open: the disc, dust, the clumping of young stars and the
  catalogue's own cut are all candidates, and none is tested.

These check the bookkeeping in levels, not the law.

**The two regimes** [physics, read]. Per address, nothing changes with distance: radiance is conserved along a ray.
While a source covers many addresses, distance costs addresses. Once it is under one, distance costs brightness in that
one. The switch is the resolution limit, the corner of the (size, step) pair.

### 8.2 The near field turns at the corner of the pair, where the light is a share

**The disc** [exact; `plans/nrf-plan.md`]. Light on the axis of a Lambertian disc of radius a at distance d, received by
a flat patch facing it, is proportional to a²/(a² + d²). Write x = d/a, the distance in radii, a ratio of two amounts
(the pair's corner is x = 1, a = d). The light is f(x) = 1/(1 + x²) of its maximum: saturating near, inverse square far
off, exactly half at x = 1, and f(1/x) = 1 − f(x). In levels the local slope is σ = −2x²/(1 + x²): −1 at x = 1, halfway between the near 0 and the far −2, with σ(x) + σ(1/x) = −2 exactly. The turn
from 10% to 90% of the way takes log₂ 9 ≈ 3.17 levels of distance.

**The rule** [exact in the cases worked; the general rule is a reading]. The switch sits exactly at the pair's corner, symmetric under the
flip, when the light counted is a share of a two-part split, A(x)/(A(x) + A(1/x)). The projected solid angle, the
standard measure of irradiance, gives such a share: for the disc it is sin²θ with θ the half-angle subtended, and its
fairness under the flip is Pythagoras. A line seen by a flat patch and a sphere counted from its surface behave the
same way. Counting an angle, or an unprojected solid angle, does not: the switch moves off x = 1 (to 0.719 and 0.786)
and loses its symmetry (NRF P3, P4, killed). The width of the switch is not one band for all shares either: 3.17
levels for the disc, 6.34 for the sphere counted from its surface (NRF P5, killed).

**The lay has the law's form** [exact; `plans/isq-plan.md`]. Past the corner the in-place lay's room per unit of v/h is
(h/v)², the flip's Jacobian. Read v/h as d/Δ, which needs two bridges: the calibration V = H, so that a ratio of
fill levels can stand for a ratio of amounts, and the size Δ as the unit. Then the lay places a thing at its angular size counted
down from the horizon, and its 1/(d/Δ)² is how fast that angular size shrinks: an inverse square in one direction
across. Light's inverse square is that angular size squared. This is a shared form with one origin, the flip, not a
claim that the lay is light. The one-direction half is untested.

### 8.3 Standing on a world

**From the outline** [exact; `plans/hzn-plan.md`]. From a place on a circle the readings to the rest of the circle are
chords 2 sin φ, with φ measured from the tangent. Their geometric mean over the half-turn is exactly the radius,
since ∫₀^π ln(2 sin φ) dφ = 0, and a chord equals the radius at φ = 30°. On a ball, weighting each direction by its solid
angle (cos φ dφ over the half-turn of directions), the geometric mean is 2/e of the radius, since
∫₀^{π/2} cos φ·ln(2 sin φ) dφ = ln 2 − 1. Taking the geometric mean as the reader's corner is a choice (the reading
past the corner is laid in levels, so its middle is a geometric one); the integrals are exact.

**Real worlds, in levels** [data; `plans/ref-plan.md`]. This restates a known fact, that planets are nearly round, in
levels. The flattening log₂(a/c), equatorial against polar radius, is 0.0048 levels for Earth, 0.0085 for Mars and
0.0017 for the Moon; Earth's relief from Challenger Deep to Everest spans 0.0045. The spinning giants' flattening is about
a tenth of a level: Jupiter 0.097, Saturn 0.149. The same predictions made for the demo world's bodies were killed
(P1–P3): one asteroid's mean sphere sat 1.3% off its ball, the Moon's relief spans 0.25 levels against the real 0.0165,
and the relief sat in a different band than predicted. They are kept as the example of what not to count.

---

## 9. Exploratory: the matter fraction

*This section reports a plan in progress (`plans/omm-plan.md`). It claims no result about cosmology.*

An earlier paper of the author's, set aside in September 2026, derived the matter fraction Ω_m = 1/π from the geometry
of its day. The plan asks whether the current terms carry it, and works each step both ways rather than ruling.

- **Stage 1, the share** [exact]. With the turn stepped evenly, the average share of the bar on h over one facing's sweep
  is 2/π; one facing of the reader's two halves it, giving 1/π. Stepped evenly by length instead (the in-place lay), the
  same share is (√2 − 1 + ln(1 + √2))/4 ≈ 0.3239, which is not 1/π.
- **Stage 2, what matter and dark energy are** [argued, no data]. Matter as payload and dark energy as addresses (X)
  fits the settled behaviour: matter clusters, thins with expansion, and differs by direction; dark energy does none of
  these. The swap (Y) contradicts all three and is killed.
- **The share with epoch** [exact, under the standard flat model]. If every epoch's own home read 1/π, dark energy would
  have to thin like matter, which it does not: killed. If 1/π were the average over one reader's whole past, today's Ω_m
  would have to be 0.0076, 0.0017 or nothing at all under three weights: killed. What survives is that 1/π is the share
  at the reader's home now. That restates physics' coincidence problem (why the two shares are comparable now); it does
  not answer it.

The comparison with Planck and DESI (stage 3) has not been run. A number close to a measurement would show a number, not
a reason, while the coincidence problem stays open.

---

## 10. What was killed or withdrawn

A framework that only reports successes cannot be judged. These failed, and stay recorded as failed.

| test or claim | what happened | source |
|---|---|---|
| NLE run 1 (P1): children's number-line placements follow proportion up to a fitted unit, then equal length per doubling, better than proportion judgment | killed on Chan and Mazzocco's kindergartners (proportion judgment won for 40 of 75 at Time 1, more clearly elsewhere) | `plans/nle-plan.md` |
| NLE run 1 (P1b): that model beats a plain logarithm | failed: it won for only 6 of 75 | `plans/nle-plan.md` |
| GRN runs 1–2: a knee in reading at one step across | killed twice; a reader given the shape reads below its step | `plans/grn-plan.md` |
| GRN run 6 (P2): steering by its own pixel count, at least 90% of runs stop with the pair 0.5–3 steps across, from every start | killed at one start (87.3% from s₀ = 0.03) | `plans/grn-plan.md` |
| HRT runs 1–3: readers taking their unit from what the parent could not see settle on a ratio between levels | stopped: run 1 did not nest, run 2's apparent 2 was the landscape's, run 3 found almost nothing to nest into | `plans/hrt-plan.md` |
| WHY2 run 1: a preferred step for a reader content with a first sighting | killed: finer is always better | `plans/why2-plan.md` |
| CNT P3–P4: the disc flattens counts toward the poles more than in the plane | killed: both give 1.23 | `plans/cnt-plan.md` |
| CNT P6–P10: K0 giants count as an even spread | killed: the label mixes kinds and the catalogue cuts the far ones | `plans/cnt-plan.md` |
| GCN P1–P4 | killed by a distance-dependent cut and by white dwarfs in the colour bands | `plans/gcn-plan.md` |
| NRF P3–P4: an angle and an unprojected solid angle switch at the pair's corner | killed: they switch off it, unsymmetrically | `plans/nrf-plan.md` |
| NRF P5: one width of switch for all shares | killed by the sphere counted from its surface | `plans/nrf-plan.md` |
| HZN P5, P5b, P5c: the drawing tool's levels page agrees with the exact chords | killed: it reads only to its grain; with both grains doubled together (run 3), not killed | `plans/hzn-plan.md` |
| MAG P4: a known kind is a bridge under a level wide | killed: K0 III scatters 1.4 levels | `plans/mag-plan.md` |
| REF P1–P3: the demo world's bodies sit near their corner | killed; never evidence | `plans/ref-plan.md` |
| OMM stage 1 under the in-place weight: the share is 1/π | killed for that weight (0.3239) | `plans/omm-plan.md` |
| OMM B5 (i), (ii): 1/π at every epoch, or over one reader's past | killed | `plans/omm-plan.md` |
| the 2 in the inverse square as "the sweep's two parties" | withdrawn: the 2 is the number of directions across the line of sight, physics | SPN §3.3, 9 Oct |
| a corner for every level; depth as nested sweeps; recursion | withdrawn: one corner, plain doublings | R188 |
| "the corner is approached, never found" | withdrawn: v = h is two fill levels, found by every reader | SPN §1, 9 Oct |
| the in-place lay "is not the reader's own" | withdrawn: it is the reader's by length | R190 |

---

## 11. What is classical, and what is claimed

**Classical.** The swap x ↦ 1/x; the Cauchy as the image of a uniform angle and its Möbius invariance (Knight 1976;
McCullagh 1996); Cauchy's functional equation; Klein's test that a geometry is what its symmetries preserve (1872), used
in D.1; triangulation and two-view reconstruction; the radiance theorem, view factors and their reciprocity; the
inverse-square law itself. Near neighbours in measured perception: Gilinsky's perceived distance with a finite horizon
(1951); Schwartz's log-polar map of visual cortex, proportional near the fovea and logarithmic beyond (1977); the
number-line literature, from logarithmic-to-linear shifts (Siegler and Opfer 2003; Dehaene et al. 2008) to proportion
judgment on bounded lines (Barth and Paladino 2011). The view from nowhere is Nagel's phrase (1986); Haraway (1988)
called the ideal of seeing everything from nowhere "the god trick". What the completed view assumes can be stated
exactly as an order of limits (from the archived *The Order of Limits*): classical work takes the reader's step to zero
first and then lets the count grow without bound; a reader has a fixed step and an unknown count.

**Claimed.** Not the pieces, which are classical, but reading them as one structure set by what a reader knows of the
two breadths:
1. near and far are one geometry, read through the flip at the corner, and the corner is forced (Propositions 1–2);
2. a situated reader's one breadth forces V = H, which puts the corner at radius 1 with no number put in, and makes
   the bar drawing, with Euclidean length, a circle (Proposition 3);
3. past the corner the logarithm follows from no rung being preferred: two address spaces, proportional and
   logarithmic, one corner (Proposition 4); drawn by length, the far field fits in one more H;
4. the circle and the Cauchy are one uniform turn, held whole or read from home (Proposition 5);
5. **the primary result:** the Cauchy consists of the reader's addresses, not its payload. The reach of whatever arrives
   cancels from every reading, so the Cauchy is laid before anything arrives; it keeps order, its median the corner,
   and has no sum (Proposition 6);
6. the level of detail is the count, set by size, and H is a zoom (§6).

Whether this is a better or worse way to compute anything is an engineering question and not this paper's concern. The
aim is to explain things that are known but not well understood: why near and far fields seem to obey different
mathematics, why logarithmic scales appear wherever a range is too wide to hold in proportion, and why the Cauchy has a
median but no mean (it is addresses, and addresses have an order but no sum).

---

## 12. Open problems, and questions for reviewers

The questions come down to one. Five steps carry the structure, and each rests on its own premise: the corner on the
flip; the circle on Euclidean length in one unit; the logarithm on (S); the Cauchy on even turns; every amount on a
bridge. Can the circle and the logarithmic lay be derived from a minimal, explicit definition of a situated reader, or
must they be added as principles? If they must be added, the contribution is a principled construction of a reader's
geometry, not a proof that observation alone forces it. The first three questions below are the ones that decide this.

### 12.1 A candidate answer: one principle

*Added 11 October, after a second evaluation asked for "the smallest underlying principle from which these ideas can
all be recovered" (`plans/ofs-review-1.md`). A reading, offered for review; the author has not ruled on it.*

> **A situated reader gives equal addresses to whatever its readings cannot tell apart.**

Formally: the reader's addresses are the measure left unchanged by the transformations it cannot detect. This is Klein's
test, already used in D.1 for points, applied to measures. A situated reader's definition (it holds H, not V, and has no
preferred standpoint among attitudes) names three such transformations.

1. *Which party is which.* Swapping v and h changes nothing the reader can check. The swap's one fixed point is v = h:
   the corner and the flip (Proposition 1). R162's fair reading (Proposition 2(b)) is this invariance written as a rule.
2. *Which attitude the bar is in.* If no turn is preferred, two classical uniqueness facts apply. The Euclidean norm (up
   to scale) is the only norm every turn preserves, so the bar of fixed length traces the circle (Proposition 3(c)). The
   uniform measure on angle is the only probability measure on the circle every turn preserves (the Haar measure of the
   turns), so the reader steps the turn evenly, and read as v/h that gives the Cauchy and the fisheye (Proposition 5).
   The circle and the Cauchy then come from one premise, and the even turn is the invariance itself, not a further choice.
3. *How big V is.* V is unknown, so multiplying every far reading by one factor changes nothing the reader can check.
   The measure rescaling leaves unchanged is dx/x (the Haar measure of the positive numbers under multiplication), which
   gives every doubling the same number of addresses: premise (S), and so the logarithm (Proposition 4).

*Inside the corner.* The reader does hold H. Its one unit breaks the scale symmetry there, and what is left is that no
position within H is preferred: the measure unchanged by shifts, equal addresses per unit of H, which is proportion. So
the two address spaces are one principle on either side of what the reader knows: its unit holds inside the corner and
there is none past it. Their spacings, 1 per unit and 1/x per unit, agree at x = 1, which under V = H is v = h. The
flip's fixed point and the meeting of the two spaces are the same point.

*D.1 too.* "No measure on a level, so only the halving is supplied" is Klein's test on points, the same principle.

*The three transformations make one group* [classical; from the archived *One Reader* §2.1a]. On the ratio v/h, a turn
acts as a Möbius map, v/h ↦ ((v/h)·cos α + sin α)/(cos α − (v/h)·sin α), and a rescaling as v/h ↦ λ·v/h. Turns and
rescalings together generate PSL(2,ℝ): every element factors as turn, rescaling, turn (the Cartan or KAK
decomposition), and each register alone gives only half. Adding the swap v/h ↦ h/v, which reverses orientation, gives
PGL(2,ℝ), the group that keeps cross ratios. The Cauchy family is the one family of laws this group carries into itself
(Knight 1976; McCullagh 1996). So the reader's three undetectable transformations are not three separate premises but
three parts of the one group of the ratio.

*What this does and does not settle.*
- If it stands, questions 1, 2 and 5 below become one question: whether the reader's ignorance is exactly these three
  transformations. Answering "why Euclidean?" would answer "why even turns?" with it.
- The principle is classical: choosing a measure by the transformations one is ignorant of is Jaynes's method of
  transformation groups (1968), and dx/x for an unknown scale is Jeffreys's prior (1939). The Cauchy is the family the
  ratio's transformations carry into itself (Knight 1976; McCullagh 1996). What would be claimed is not the principle
  but that a situated reader's state of knowledge selects the transformations, and the structure follows.
- Invariant measures are fixed only up to a constant. Joining the two spaces with no jump in address spacing at the
  corner (c = 1 in Proposition 4) stays an added condition, a mild one: the level of detail does not jump at the corner.
- "No attitude preferred" still treats the sweep as a turn of a rigid bar. It is a cleaner premise than "choose the
  Euclidean norm", but it is a premise; the facing (§2) motivates it and does not prove it.

1. **The link in Proposition 4.** Is "the room depends on the ratio alone" justified by "any H will do", or is it an
   independent assumption of scale invariance under another name?
2. **Why Euclidean?** Proposition 3(c) takes the bar's length to be Euclidean. If the sweep is a turn of a rigid bar, the
   Euclidean norm is the only one every turn preserves. Is there a reason, from the reader's premises, that the sweep must
   be a turn, rather than the square's or the line's path through the same ratios?
3. **(P2), no measure on a level.** D.1 is airtight given it. Is there a principled reason a level could not carry a
   measure before anything arrives?
4. **R162, the fair reading.** Proposition 2(b) needs the reading to treat the two sides alike although the reader's
   knowledge does not. Is that defensible as more than a choice?
5. **Uniformity as the weight.** §5 argues that the even turn is not an extra assumption for the Cauchy, since it is
   what makes the circle uniform. Does that remove the burden, or only move it to "why the circle"?
6. **Proposition 3(a).** Is "V = H is forced" more than a restatement of having only one breadth? Where would a reviewer
   draw the line between a derivation and a definition here?
7. **A measured reader.** Grid cells in the entorhinal cortex map space in modules whose spacing ratio no physics law
   sets. D.1 allows only binary branching without an added measure; if levels are doublings, that is 2 along a line, or
   √2 if a level doubles an area. Published means near 1.42 (Stensola et al. 2012) and others near 1.7 (listed in `plans/grd-landscape.md`) are known to the authors, so the plan (`plans/grd-plan.md`) runs only on per-animal data not yet
   opened. Suggestions for data are welcome.
8. **The near field.** Is every Lambertian source of any shape, seen by a flat patch, a share in some ratio of the pair?
   This is to be tested in exact arithmetic on other shapes.
9. **The coincidence problem.** §9 leaves it restated, not answered. Is there anything in a reader's geometry that could
   say why its home falls now?

---

## Appendix A. Notation

| symbol | domain | meaning |
|---|---|---|
| h, v, v₂ | geometry, [0, 1] | fill levels: how much of H, V, V₂ |
| H, V, V₂ | physics, amounts | breadths: the reader's, the other's, a second other's |
| v/h, h/v | geometry | the reading before and past the corner (SPN writes s) |
| the corner | geometry | v = h |
| d, Δ, a, R, L | physics | distance, size, radius, radius, light |
| ℓ | physics | the reach of what arrives along a ray (Proposition 6(a)); it cancels from every reading |
| ε | physics | the reader's angular step |
| Δ/(d·ε) | physics | addresses a thing spans; = 1 is the resolution limit |
| level | geometry | home to corner (the first); one doubling of v/h past it |
| in-place lay | geometry | position by length: v/h inside, 2 − h/v past the corner |
| logarithmic lay | geometry | position by address count: v/h inside, 1 + ln(v/h) past the corner |

## Appendix B. Where each part comes from

| here | working papers | plans and pages |
|---|---|---|
| §1 | SPN §1 ("What a sweep is"), §2.1; `number-line.md` Background | — |
| §2 | SPN §1 ("The line, the arc and the facing"), Propositions 3.1–3.3, R162 | `facing.html` |
| §3 | SPN Proposition 1.2 (a)–(f), Appendix D (D.1), R188–R190; `v-and-h.md` §8o | `levels.html`, `sphere.html` |
| §4 | SPN Proposition 1.2 (g), "Reality in 2H", "Two address spaces" | `levels.html`, `flight.html`, `isq-plan.md` |
| §5 | SPN Proposition 1.2, "The Cauchy and the fisheye, derived" (1)–(7); SPN §4.3, "The Cauchy consists of addresses, not payloads", R47, R200; §14 burdens; `number-line.md` §8; `v-and-h.md` 423–424; archived *Reader Geometry as Addressing* §7.5 (Proposition 14) | — |
| §6 | SPN Proposition 1.2 ("The count", "H is a zoom"), §3.3; `number-line.md` §5 | `grn-plan.md` |
| §7 | SPN §1 ("Powerless in one observation"), Part II | `flight.html` |
| §8 | `inverse-square.md`; `physics.md` §2 | `mag-`, `gcn-`, `cnt-`, `nrf-`, `isq-`, `hzn-`, `ref-plan.md` |
| §9 | — | `omm-plan.md`, `omm/` |
| §10 | SPN Appendix C; `physics.md` §3 | the plans named |

**Reproducing.** Each plan in `plans/` names its script (Python or Node), its data source with sha256, and its runs in
the order they came out. `npm test` runs the demo pages' checks in headless Chromium. Large data is not committed; the
plans say where to get it.

## References

Barth, H. C. and Paladino, A. M. (2011). The development of numerical estimation: evidence against a representational
shift. *Developmental Science* 14(1), 125–135.
Cuadras, C. M. (2002). Geometrical understanding of the Cauchy distribution. *Qüestiió* 26(1–2), 283–287.
Dehaene, S., Izard, V., Spelke, E. and Pica, P. (2008). Log or linear? Distinct intuitions of the number scale in Western
and Amazonian indigene cultures. *Science* 320, 1217–1220.
Gilinsky, A. S. (1951). Perceived size and distance in visual space. *Psychological Review* 58, 460–482.
Haraway, D. (1988). Situated knowledges: the science question in feminism and the privilege of partial perspective.
*Feminist Studies* 14(3), 575–599.
Klein, F. (1872). *Vergleichende Betrachtungen über neuere geometrische Forschungen* (the Erlangen programme).
Knight, F. B. (1976). A characterization of the Cauchy type. *Proceedings of the American Mathematical Society* 55,
130–135.
Lamping, J., Rao, R. and Pirolli, P. (1995). A focus+context technique based on hyperbolic geometry for visualizing
large hierarchies. *Proceedings of CHI '95*, 401–408.
Longuet-Higgins, H. C. (1981). A computer algorithm for reconstructing a scene from two projections. *Nature* 293,
133–135.
McCullagh, P. (1996). Möbius transformation and Cauchy parameter estimation. *The Annals of Statistics* 24, 787–808.
Microsoft. Bing Maps Tile System (documentation).
Nagel, T. (1986). *The View from Nowhere*. Oxford University Press.
Pitman, E. J. G. and Williams, E. J. (1967). Cauchy-distributed functions of Cauchy variates. *Annals of Mathematical
Statistics* 38(3), 916–918.
Schwartz, E. L. (1977). Spatial mapping in the primate sensory projection: analytic structure and relevance to
perception. *Biological Cybernetics* 25, 181–194.
Jaynes, E. T. (1968). Prior probabilities. *IEEE Transactions on Systems Science and Cybernetics* 4(3), 227–241.
Jeffreys, H. (1939). *Theory of Probability*. Oxford University Press.
Siegler, R. S. and Opfer, J. E. (2003). The development of numerical estimation: evidence for multiple representations of
numerical quantity. *Psychological Science* 14(3), 237–243.
Snellius, W. (1617). *Eratosthenes Batavus*. Leiden.
Stensola, H., Stensola, T., Solstad, T., Frøland, K., Moser, M.-B. and Moser, E. I. (2012). The entorhinal grid map is
discretized. *Nature* 492, 72–78.
Stigler, S. M. (1974). Cauchy and the witch of Agnesi: an historical note on the Cauchy distribution. *Biometrika*
61(2), 375–380.
Williams, L. (1983). Pyramidal parametrics. *Computer Graphics* (Proceedings of SIGGRAPH '83) 17(3), 1–11.

Data: Hipparcos via the HYG database v3.8 (GitHub); the Gaia Catalogue of Nearby Stars (Gaia Collaboration, Smart et al.
2021, *A&A* 649, A6). Sources, licences and checksums are in the plans.
