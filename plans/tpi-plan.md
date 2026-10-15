# TPI: where 2/π shows up

*14 October 2026 (Tom's local date). Tom, about 18:48: "what good reverse proofs do we have of the situated observer?";
then, to Claude's answer, 19:08: "Possibly anytime 2/PI shows up, its the situated situation."; and, to Claude's
sharper form of it, 19:16: "its probably the best clue there is. there are many more examples of 2/PI showing up."
(SPN R251). Predictions written before the catalogue is assembled and before the script (`tpi/tpi.py`) exists.*

## The claim, sharpened

2/π is the reciprocal of a quarter turn. In the corpus it is the inner reading: a turn read through its shadow, sin θ/θ
at θ = π/2, the mean shadow (2/π)∫₀^{π/2} cos θ dθ of a bar turned evenly through a quarter turn
(`observation-from-somewhere.md` §3.4, where Buffon's needle, Viète's formula and the arcsine law already stand). Read
so, π enters a result only through a turn, and 2/π through a quarter of one taken evenly and read as something never
negative.

**The bridge from the mathematics to "situated"** is the corpus's own, named, not tested here: a turn belongs to a
situated reader (the unsituated view is the chord, with no turn; SPN R233, R234), and a relation is never negative, so
the reader's directions are one quadrant, the wedge (R240). The test is whether every 2/π found comes from an even turn
read that way. If it does, 2/π is a fingerprint of the even turn, a fact about where the constant comes from; calling
that turn the situated reader's is the corpus's reading of it.

## The four forms (fixed before the search)

- **(i) Mean shadow.** The mean of |cos θ| (or of |sin θ|) over a turn measured evenly: (2/π)∫₀^{π/2} cos θ dθ = 2/π.
- **(ii) Share.** The share of a quarter turn done, (2/π)·θ, as in the laws (2/π)·arctan s and (2/π)·arcsin √x.
- **(iii) Inner reading at the quarter turn.** sin θ/θ at θ = π/2: the same function as (i), read at one turn instead of
  averaged.
- **(iv) Normaliser of a weighted half turn.** 1/∫ of a never-negative weight over a turn measured evenly whose integral
  is π/2, such as ∫₀^π sin²θ dθ or ∫_{−π/2}^{π/2} cos²θ dθ.

**Hidden turns** count when they are in the derivation: an angle made even by isotropy (two independent normal
amounts of equal spread have an even angle; with unequal spreads it is not, the drawing V = H), a phase uniform in
time, or the even (Haar) measure of a rotation group.

## What was known before writing

- In OFS already: the sweep's law (2/π)·arctan(v/h), Buffon's needle, Viète's formula, the arcsine law as Jeffreys's
  prior.
- Named by Claude in conversation (19:08): an averaging AC meter (2/π of the peak), a square pixel's response at the
  Nyquist frequency, one-bit correlators (Van Vleck's (2/π)·arcsin ρ), the Kosterlitz–Thouless universal jump, and
  Buffon's needle between planes (ℓ/(2d)).
- Thought of while writing this plan, before any search: the efficiency of the median against the mean for a normal
  law and of the sign test against the t test; (E|Z|)² for a standard normal Z; a one-bit quantiser's loss in
  signal-to-noise; a half-wave dipole's effective length λ/π; the mean speed of a point on a rolling wheel's rim, 4v/π;
  the flux of a two-dimensional gas through a line, n·v̄/π; Jordan's inequality sin x ≥ (2/π)x; Flamant's half-plane
  stress 2P cos θ/(πr); Hertz's line contact, p₀ = 2P/(πa); Wigner's semicircle (2/π)√(1 − x²); the Sato–Tate law
  (2/π) sin²θ; Chebyshev's equilibrium measure on an interval; Goemans and Williamson's random hyperplane; the √(2/π)
  of Bessel functions' far field.

The rest come from a search by a fresh agent, asked only for occurrences with their formula, field, source and the
step of the standard derivation where π enters. It is not given these predictions or forms.

## Predictions

- **P1 (an even turn).** Every occurrence in the catalogue comes from a turn measured evenly (uniform in an angle or a
  phase, the Haar measure of a rotation group, or an angle made even by an equal-spread pair) and read through something
  never negative (a size, a shadow, a share). *Killed* if any occurrence, its standard derivation traced, has no such
  turn, open or hidden. The Kosterlitz–Thouless jump is named in advance as the hardest case. Each entry gets the step
  of its derivation where the turn enters and an exact computation (mpmath) of the constant from that step.
- **P2 (one of four forms).** Each occurrence's 2/π is one of forms (i)–(iv). *Killed* if any is not.
- **P3 (the dimension rule).** Two families, written now:
  - built by averaging a shadow over directions in the plane (form (i)): over directions in space the same construction
    gives ½, in four dimensions 4/(3π) (OFS's family, the reciprocal of √π·Γ((n + 1)/2)/Γ(n/2), n the number of unit
    relations);
  - built as the shadow of an even disc (the semicircle, form (iv)): an even ball gives 3/4, an even four-ball 8/(3π)
    (the normaliser Γ(n/2 + 1)/(√π·Γ((n + 1)/2))).

  *Killed* if any occurrence of these two kinds, rebuilt in three or four dimensions, gives another value.
- **P4 (evenness is what gives it).** Where the two parties enter undivided (a ratio Y/X, a share X²/(X² + Y²), a
  projection of an orientation), an uneven turn moves the value off 2/π: orientations from a von Mises law of
  concentration κ, or a pair of spreads in ratio c, give 2/π only at κ = 0 or c = 1. Computed at κ = ½, 1, 2 and
  c = ½, 2. *Killed* if any such occurrence stays at 2/π for κ > 0 or c ≠ 1. Where each party is first divided by its own
  spread (a correlation coefficient), the drawing at one length is already done and P4 does not apply.

## What would and would not be shown

A catalogue where every 2/π traces to an even quarter turn read as something never negative would show that 2/π
fingerprints the even turn, across fields that do not otherwise talk to each other. It would not show that each
instrument or system is an observer: that is the corpus's reading of a turn (R233), named as the bridge. A kill would
bound the clue: a 2/π reached with no turn means the constant can arise another way, and the conjecture would hold
only for the forms that survive.

## Runs

### Run 1 (14 October; the twenty entries known before the search, the catalogue not yet in)

`python3 -I plans/tpi/tpi.py` as first written; output in `plans/tpi/tpi-run1.txt`. Seventeen entries matched their
written constants to 40 digits. Three did not, and P3 was killed, all by my set-up:
- the arcsine law and Chebyshev's equilibrium measure: a density singular at an end, integrated at 50 digits, came out
  2·10⁻²⁹ off, against a tolerance of 10⁻⁴⁰;
- Van Vleck's sign correlation: the breakpoints given to the quadrature were wrong (one negative, unsorted), so the
  indicator was integrated across its jumps;
- P3 killed: the mean |cos| over the sphere was integrated across the kink at π/2 without splitting there, 8·10⁻⁶ off
  (0.4999923 for ½, 0.6366148 for 2/π).

P4 not killed: von Mises concentrations ½, 1, 2 move the mean shadow to 0.649, 0.682, 0.763 (and |sin| to 0.624,
0.591, 0.506; a pixel with uneven phase to 0.737, 0.818, 0.910); spreads in ratio ½ and 2 move the sweep's median off
the corner (0.705, 0.295) and the share's law off the arcsine (0.585, 0.201 against 0.369 at x = 0.3).

**Run 2**, with the same predictions: the singular integrals at doubled precision, Van Vleck's breakpoints corrected,
the kink split; and the catalogue's entries added when the search returns.

### Run 2 (14–15 October; the twenty known entries and the catalogue's forty-five)

The catalogue (`plans/tpi/catalogue.md`) was gathered by a fresh agent told only to find occurrences with formula,
field, source and the step of the standard derivation where π enters; it was not given the predictions or the forms.
It found 45 main entries across about forty fields (37 seen in their sources, 3 partly, 5 from memory), and set apart
15 entries written as π/2 and 12 as √(2/π). `python3 -I plans/tpi/tpi.py`, ten seconds; output in
`plans/tpi/tpi-run2.txt`. Two of the new entries' checks first failed on quadrature (the loaded circle's |cos| across
its kink, Kramers–Kronig's principal value across the resonance); both were split and pass. The routes and forms are
my judgments, made from each derivation step as the catalogue (or the source) gives it, before the verdict lines were
read; the computations check the constants, not the judgments.

```
all constants match: True (63 of 63)
route E: 41   (an even turn in the standard derivation)
route H: 13   (a hidden turn of a kind named in the plan: an equal-spread normal pair, a Haar measure)
route S: 7    Hertz line contact; Wigner's semicircle; disc capacitance; Sneddon's cone; Oliver–Pharr's ε; the stress
              drop of a surface-breaking fault; rotational broadening
route P: 1    alternating permutations (A_n/n! ÷ 2(2/π)^{n+1} = 1 at n = 240, the zigzag numbers exactly)
route U: 1    the Bauer–Ramanujan series (step not seen)
P1: KILLED by the seven S entries and alternating permutations
P2: KILLED by Kosterlitz–Thouless [a dimension], the Gaussian beam [a convention], alternating permutations [a pole],
    the seven S entries [only after a substitution]; the infinite grid and Bauer–Ramanujan not traced
P3: KILLED. Shadows on an axis rebuild to ½ (Buffon between planes; the 3D gas, ¼ = ½·½; the arc's centroid as the
    hemispherical shell's; remanence, fibres and leaves random in space). Two others do not: rods' mean |sin γ| over the
    sphere is π/4, and the mean chord on a sphere (and the relative speed of animals moving in space) is 2/3 of 2r.
P4: not killed (as in run 1)
```

- **P1 killed, by eight of sixty-three.** Fifty-four come from a turn measured evenly and read through something never
  negative: forty-one with the turn in the standard derivation (orientations, phases in time, Fourier phases, the
  ellipse's or the pendulum's angle, a Brillouin zone) and thirteen through a hidden one of the kinds named beforehand
  (the equal-spread normal pair behind Van Vleck, Kendall's τ, Kac's roots, the median's efficiency, Γ(½)² in Struve's
  constant; the Haar measure behind Sato–Tate). Seven are one group: **the circle held as a shape.** π/2 there is a
  semicircle's area (Hertz's line contact, Wigner's semicircle, a star's rotational broadening, a fault's slip) or the
  arcsine integral ∫₀¹ dx/√(1 − x²) (a disc's capacitance, Sneddon's cone, the Oliver–Pharr constant). They come from
  square-root profiles that solve mixed boundary problems or moment problems, and the quarter turn appears only after
  the substitution x = sin θ, which those derivations do not make (Glauert's substitution, Muskhelishvili's map to the
  circle or the disc's shadow would supply one; Irwin's ellipse angle is why the penny-shaped crack is not in the
  group). The eighth is **a location**: alternating permutations grow as (2/π)ⁿ because sec x + tan x has its first pole
  at π/2, where tan runs off; no measure is taken.
- **P2 killed.** The four forms were too narrow: the Kosterlitz–Thouless 2 is the plane's dimension (the entropy of a
  vortex's place) over the energy of its even winding, π; the Gaussian beam's 2/π belongs to the 1/e² radius
  convention (with the 1/e radius it is 1/π); the S group fits form (iv) only after the substitution.
- **P3 killed.** In the plane three constructions coincide: the mean shadow of a direction on an axis, the mean |sin| of
  the angle between two directions, and the mean half-angle chord all give 2/π. In space they part: ½ (Archimedes'
  hat-box), π/4 and 2/3. The prediction's ½ belongs to the first only.
- **P4 not killed** where computed: concentrating the turn, or drawing the two parties unequally, moves every value off.

**Reading (after the run; not ruled).**
- *A strong clue, with a boundary.* Across about forty fields, 2/π overwhelmingly marks a turn taken evenly and read
  as a shadow or a share: the inner reading of OFS §3.4. Where it arises otherwise, it is the circle as a shape (an area,
  an arcsine integral) or the quarter turn as a place (a pole), with no turn taken.
- *In the corpus's terms* (the bridge, named in the plan, untested): the turn taken is the situated reader's (R233), and
  the circle held whole, drawn on the chord after the arc, is the completed view's (R234). So 2/π by itself does not
  identify the situated reader; 2/π reached through an even turn does, and the S group is where the circle appears
  with no one turning.
- *Measured occurrences* in the catalogue (Campbell and Robson's 4/π in human contrast thresholds; the
  Kosterlitz–Thouless jump in helium films; fibre factors in concrete; canopy extinction; one-bit correlators) each
  follow from their own derivation: they confirm the physics, not the reading.
- *Not counted:* the π/2 entries (the same relations read the other way) and the √(2/π) entries, whose π is the normal
  law's 1/√(2π); their squares are 2/π through the equal-spread pair, as (E|Z|)² is.

### Run 3: the second mark, V not known (predictions written 14 October, before the second classification)

*Tom, 20:12: "the other definining characteristic of the situated view is V is not known." (SPN R252; the corpus has it
since R205 and R226: known V is the unsituated view, and the situated reader never reads V*.) Then "yes", 20:31, to a
test. Written before a second fresh agent classifies the 63 entries; the run is recorded below this section.*

**What changes.** The situated view has two marks: a turn taken, and V not known. Run 2 tested only the first. The
second is a property of use as much as of derivation: the same 2/π serves a reader that knows the whole (Buffon's
crossing probability from a known needle and gap) and one that does not (stereology's unknown length from counted
crossings; an averaging meter's unknown peak).

**Method (fixed now).** A fresh agent, told nothing of turns, the situated view or these predictions, gets the 63
entries by name, field, formula and source (no route, no form, no "angle?" judgment) and answers, for each, with a
line of justification and an example of use:
- **Q1.** In the step of the standard derivation where π enters, what is integrated or evaluated over: (a) an angle or
  a phase (including a direction drawn at random or a phase uniform in time); (b) a position along a segment, or across
  a region, whose ends or boundary are given lengths; (c) something else (say what)?
- **Q2.** In the field's typical use, is the formula used (a) to compute a result from sizes or amplitudes all known
  beforehand; (b) to infer a size, an amplitude or another quantity not known beforehand from a measurement; (c) both,
  commonly?

**Predictions.**
- **P5 (the routes agree).** The second agent's Q1 matches run 2's routes (E or H with (a); S with (b)) on at least 57
  of the 63. *Killed* if fewer. A check of my judgments in run 2.
- **P6 (the circle as a shape has V known).** All seven route-S entries are (b) on Q1: each fixes its extent by both ends
  in advance. *Killed* if any is (a) or (c).
- **P7 (the two marks go together).** If 2/π marks the situated view, the turn it comes from should be read in place of
  a whole not known: among the turn entries (E and H), the share used to infer something not known beforehand (Q2 (b)
  or (c)) exceeds the share among the route-S entries. *Killed* if it does not exceed it. My prior, stated: I do not
  expect much difference; two S entries (Oliver–Pharr's ε, rotational broadening) are used to infer unknown sizes, and
  many turn entries (a pendulum's period, a known wave's Fourier coefficient, Onsager's energy) compute from known sizes.

Reported as well, not predicted: how many entries carry both marks (a turn, and Q2 (b) or (c)).

**Correction to run 2's counts** (found while preparing run 3's list, before its results): the script's 63 checks cover
62 distinct occurrences (C10b is a second check of C10's constant). Of the 65 occurrences gathered, three have no row of
their own: Wheeler's microstrip formula (C26: no derivation step seen, route U) and the machine MMF and Coltman's
relation (C39, C41: the square wave's fundamental, computed under C34, C36 and C40, route E). Counted by occurrence, the
routes are E 43, H 12, S 7, P 1, U 2 (65): fifty-five come from an even turn, not fifty-four of sixty-three. No verdict
changes. P5 is scored on run 2's 63 rows as written (C10b taking C10's answer).


### Run 3 (14–15 October; the blind classification)

A fresh agent, given only `plans/tpi/neutral-list.md` (the 65 by name, field, formula and source) and told nothing of
turns, the situated view or the predictions, answered Q1 and Q2 for each from standard references
(`plans/tpi/classification.md`, with its conventions and seven low-confidence rows: K4, K17, C2, C5, C20, C26, C28).
Scored by `python3 -I plans/tpi/run3.py plans/tpi/classification.md`:

```
P5: KILLED. routes agree on 51 of 63 rows (needs 57)
  disagreements: C2 (U vs c), C7 (H vs c), C10 (H vs c), C22 (E vs c), C27 (H vs b), C28 (E vs c), K4 (H vs c), K6 (E vs b), K9 (H vs c), K10 (H vs c), K11 (E vs b)
P6: not killed. route S on Q1: K16 b, K17 b, C25 b, C29 b, C30 b, C32 b, C44 b
P7: KILLED. inferring an unknown (Q2 b or c): turn entries 13 of 51 with a use (0.255; 13 of 55 counting identities, 0.236), route S 4 of 7 (0.571)
both marks (a turn, and used to infer): 13: K2 (c), K4 (c), K5 (b), K7 (b), K8 (b), K10 (c), K11 (c), C13 (b), C20 (b), C22 (b), C34 (c), C41 (b), C42 (c)
identities (no use): K3, K14, C1, C2, C9
```

- **P5 killed, partly by my set-up.** Six of the twelve disagreeing rows are run 2's hidden turns (the arcsine law,
  the median's efficiency, (E|Z|)², Kac's roots, Struve's constant twice), which the agent put in (c): Q1 asked where π
  enters at the step itself, and there it is a Gaussian or Gamma constant (the agent's own note: "its usual evaluation
  squares the integral and uses a polar angle"). Mapping H to (a) did not fit the question I wrote. The rest are
  disagreements in kind: the pixel and the dipole (b: a phase across a given length, by the agent's convention), the
  baffled piston (b: the π is the piston's area πa², the radiation mass having none), Kramers–Kronig (c: a half-residue),
  the penny-shaped crack (c: Sneddon's route, which the agent found more common; run 2 took Irwin's), Bauer–Ramanujan
  (U against c). Counting the six hidden turns as agreeing (after the run) gives 57, the threshold.
- **P6 not killed.** All seven circle-as-a-shape entries are (b) to a reader who did not know the question: positions
  across a segment or region whose ends are given. Their extent is fixed in advance; in the derivation V is known.
- **P7 killed, the other way round.** Turn formulas are mostly used to compute from known sizes (13 of 51 infer
  something); the circle-as-a-shape ones more often infer (4 of 7: Young's modulus from indentation curves through
  Sneddon's cone and the Oliver–Pharr constant, stress drops from slip, v sin i from line profiles). Whether V is known
  is not carried by the formula.

**Reading (after the run; not ruled).**
- *Two kinds of inference.* The shape formulas infer by fitting: a profile whose shape is known, scaled to the data,
  its extent the fitted number. The thirteen turn formulas used to infer read a whole they do not have through a shadow
  or a sign of an evenly turned quantity: an averaging meter's peak from the mean of |sin|, a correlation from sign
  agreements (Van Vleck) or from rank agreements (Kendall's τ), a length from crossings (Buffon, stereology), a
  superfluid density from the stiffness's jump, a refractive index from absorption (Kramers–Kronig), an MTF from bar
  targets (Coltman), leaf area from light extinction (the canopy G-function). These carry both marks: they are the
  clue's best cases.
- *What the second mark adds.* In the derivations, the circle-as-a-shape group has V known (P6) and the turn group
  does not need it; in use, either can serve a reader who lacks the whole. So the two marks sort the derivations
  cleanly and the uses not at all: the situated reading belongs to the use of a turn's 2/π to read an unknown whole,
  which thirteen of the fifty-five turn occurrences have.
