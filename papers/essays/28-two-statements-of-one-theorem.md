# Two statements of one theorem: classical results from no standpoint and from one

*The twenty-eighth of a series of essays on what can be known from where one stands. Draft, 16 November 2026. It starts
from Tom's request: "Let's create a new essay that compares the dhv and shv versions of classical math theorems." One
test since, PYT, for Pythagoras (§3). Every formula is classical or checked by arithmetic in the runs named; where a statement is a reading, it is
marked so.*

The back pages of a geometry book list the theorems: the sides of a right triangle, the angles of a sum, the circle on a
diameter, the area under a bell. Each is stated the same way. A figure is drawn on the page, every part of it in view at
once, and the theorem says how its parts stand to each other.

That way of stating is the dual hemispherical vantage (DHV), the blueprint: the figure held whole, from no standpoint,
every side seen at once. It is the way classical mathematics is written, and nothing below is a complaint about it.

The same facts can also be stated from one standpoint, the single hemispherical vantage (SHV): one place, looking one
way, every direction read as a slope s = v/h in terms of one thumb, H. Some theorems come through with a short, exact,
rational form. Some come through only by renaming a constant. Some do not come through at all, because what they state
is a completion, and a single vantage never completes anything.

This essay goes through a dozen theorems that way, side by side, and sorts them into those three kinds.

The order: the two ways of stating (§1), the three kinds of outcome (§2), the theorems that come through whole (§3–§8),
the ones that come through only by renaming (§9), the ones that do not come through (§10), what the sorting rests on
(§11), what is classical and what is ours (§12), and what it changes (§13).

---

## 1. Two ways of stating a theorem

**From no standpoint.** The figure has amounts: lengths in a unit, an area, an angle measured round a completed turn.
Both signs of every axis are there. The circle is held whole, so π is available, and so are sine and cosine, which are
the turn's chart.

**From one standpoint.** There is a look and a thumb. Every direction in front is a slope, s = v/h, one number with no
size in it. Nothing behind the look is read; the horizon is where s runs off to infinity. Nothing is completed: a read
goes from home toward a horizon and closes no circle. What a read has is the slope, the exchange s ↔ 1/s, the corner
s = 1 where the exchange stands still, and the heat 1/(1 + s²) over the readings.

The two agree wherever both apply, since they describe one geometry (R950). The difference is in what each statement
needs: the blueprint's needs a completed turn or an amount; the single vantage's needs only slopes, and sometimes one
square root.

## 2. Three kinds of outcome

A classical theorem, restated from one standpoint, lands in one of three places (R847):

- **Whole.** There is an exact statement rational in the slope, with no limit and no π. The blueprint's form and the
  single vantage's form say the same thing, and each checks against the other to the last digit.
- **Only renamed.** π can be swapped for "the total of one sweep", which is always possible and says nothing new unless
  the statement then reads as being about one sweep.
- **Not at all.** The theorem is about closing a turn, completing a length or summing a whole. A single vantage has no
  form for it, because it never closes, completes or sums.

The tests NTN and DVA counted this on lists of laws: of the 82 laws in *Reads and Writes* that carry π or e, 30 lose it
when restated in slopes and shares; across two lists every law that rests on a limit kept its π or e (74 of 74). That is
the line between the first kind and the third (essay 24).

## 3. Pythagoras

**From no standpoint.** For a right triangle with legs a and b and hypotenuse c, a² + b² = c². Three lengths, one unit.

**From one standpoint.** Divide by the leg along the look. With s = b/a the reading of the far corner,

  1 + s² = (c/a)².

There are no lengths left. In shares of the hypotenuse the same fact is

  1/(1 + s²) + s²/(1 + s²) = 1,

the heat below a reading and the heat above it filling the whole. At s = 1, the corner, the two shares are equal. What
the single vantage does not have is the hypotenuse as a length: √(1 + s²) is the one square root a read meets (R793),
and the corner's share 1/√2 is not a fraction (R814). Exact whole-number triangles, 3, 4, 5 and the rest, are rational
slopes, s = 4/3 among them, and there the square root is a whole number too.

**Kind: whole.** The circle x² + y² = r² is the same theorem; divided by the thumb it is 1 + s² = (r/x)², and its heat
is 1/(1 + s²). *Reads and Writes* calls that "the paper in one equation" (R725).

**What comes out of it.** The single vantage's form is not just one theorem among the dozen. Most of the others in this
essay come out of it, and the test PYT (`plans/pyt-plan.md`, exact, predictions written first) checked each piece:

- *The shares and the corner.* 1/(1 + s²) and s²/(1 + s²) add to 1; the exchange s ↦ 1/s swaps them; they are equal
  only at s = 1. That is the corner, and it needs nothing but the theorem.
- *Composition.* Put two readings together by tangent addition and the sums of squares multiply:
  1 + (s ⊕ a)² = (1 + s²)(1 + a²)/(1 − sa)². Cleared of fractions this is the Brahmagupta–Fibonacci identity,
  (x² + y²)(u² + v²) = (xu − yv)² + (xv + yu)², and the direction (xu − yv : xv + yu) is exactly the composed slope. So
  a turn built from turns keeps one unit circle: it is rigid because Pythagoras multiplies.
- *The heat.* From that one identity, ds/(1 + s²) is carried to itself by every composed turn and reversed by the
  exchange. The Cauchy's heat is the one weight on the readings that turning leaves alone, and its denominator is
  Pythagoras's.
- *The landing point.* (1 + is)(1 − is) = 1 + s², so w(s) = (1 + is)/(1 − is) sits on the unit circle; w(s)·w(a) =
  w(s ⊕ a) and w(s)·w(1/s) = −1 (§5) follow.
- *Every rational direction.* Every rational point of the unit circle but one is ((1 − t²)/(1 + t²), 2t/(1 + t²)) for
  one rational half-slope t, which is Euclid's rule for the whole-number triangles; all 2,556 rational points with
  denominator up to 2,000 came from one t each. This is the lattice draw's Tangent Bridge runs on, with no
  trigonometric call (§11).
- *Space, and any number of parties.* With more legs it is 1 + s₁² + … + sₙ² = (r/x)², and the law of uniform
  directions on a flat screen is that sum raised to the power −(n + 1)/2 (the surface element's determinant checked
  exactly for n = 1 to 4): the Cauchy in the plane, the wedge's in space, and so on up. The rational points of the
  sphere come the same way, from two half-slopes.

It is the square that does this. With |a|^p + |b|^p in place of a² + b², for p = 1, 3 or 4, one composed step moves
points off their unit "circle" by 0.12 to 0.37; for p = 2 it keeps every point to 10⁻⁶¹. No other power gives
directions that compose into a rigid turn, so no other gives the corner where it is or the Cauchy.

And it is where the theorem stops that shows what it does not give. A rational direction, turned over and over, never
comes back to where it started, except the quarter turns (of 491 rational half-slopes in [0, 1], only 0 and 1 closed
within 200 steps; Niven). The corner's share 1/√2 is the one square root a read meets at the corner, 1 + 1² = 2 not being
a square. And the heat's total, π/2, is no expression in s: Pythagoras gives every relation among directions, and the
median at the corner without any total (the heat below 1 equals the heat above by the exchange alone), but π only comes
from completing the turn, which a single vantage never does (§10).

So of the dozen theorems here, this one is not merely whole. It is where the others come from.

## 4. Adding angles

**From no standpoint.** tan(α + β) = (tan α + tan β)/(1 − tan α·tan β), and likewise for sine and cosine. The angles
are measured round the completed turn.

**From one standpoint.** Two readings s and a compose as

  s ⊕ a = (s + a)/(1 − s·a),

rational in both. There is no angle in it. A read that has passed s and then passes a further a has passed s ⊕ a. When
the product s·a reaches 1 the denominator is zero: the two together reach the horizon. With a = 1/s that happens
exactly: s ⊕ (1/s) is the horizon, a reading and its exchange making the whole sweep. A check: 0.4 ⊕ 1.3 = 3.5417, and
tan(atan 0.4 + atan 1.3) gives the same to rounding.

**Kind: whole.** The sine and cosine laws for sums are the same fact in the turn's chart. What the single vantage does
not have is the angle α as a number, which needs π; it has the slope it reached, by composing (R841).

## 5. Euler's identity

**From no standpoint.** e^(iπ) = −1. It needs the exponential, i and π, the turn carried round half way.

**From one standpoint.** Put each slope on a circle by its landing point, w(s) = (1 + is)/(1 − is). Then for every
s between 0 and ∞,

  w(s)·w(1/s) = −1.

A reading and its exchange land on points whose product is −1. At the corner, s = 1, both are i, and the statement is
i·i = −1. Checked at s = 0.3, 1 and 2.7: the product is −1 to rounding each time. Euler's identity is the one member of
this family that pairs home with the horizon, s = 0 with 1/s = ∞, and it is the only member that needs π (R848). Every
other member is a pair of directions of one read, and holds with no limit.

**Kind: whole**, for every member but the endpoint, which is the blueprint's. The same relation held two ways is the
central example in *Reads and Writes* §1.

## 6. The angle in a semicircle

**From no standpoint.** Thales: an angle inscribed in a semicircle is right. Euclid III.31.

**From one standpoint.** Stand at one end of a segment, A, and read the slope s to a point. Stand at the other end, B,
and read the slope to the same point, measured against the segment. If the point is on the semicircle, B reads 1/s.
The two readings multiply to 1, and the rays cross square: their directions (1, s) and (−s², s) have dot product
−s² + s² = 0. The crossing point is (1, s)/(1 + s²), the same shares as §3.

**Kind: whole.** The right angle is not measured; it is the exchange. The semicircle itself, drawn as a curve, is the
blueprint's picture of every such crossing at once (R235, THL).

## 7. The reciprocal product

**From no standpoint.** π/2 × 2/π = 1. The quarter arc against its chord, and the chord against the arc, in the
measure of the completed turn.

**From one standpoint.** s × (1/s) = 1, at every reading. The near reading, V in terms of H, and the far reading, H in
terms of V, multiply to one thumb: no facing, the discrete faceless value (R1042). At the corner both are 1.

**Kind: whole.** The 1 never needed π (R809). The blueprint's form carries π in both factors and cancels it; the
single vantage's form has it in neither.

## 8. Parallax

**From no standpoint.** Two stations a baseline B apart, with angles α₁ and α₂ to a point: the distance from the
law of sines, or d = B/(cot α₁ + cot α₂).

**From one standpoint.** Two readings, s₁ and s₂, taken a counted step B apart:

  B/d = 1/s₁ + 1/s₂.

Rational, exact, no angle. A check: with the point 3 out and 2 and 5 along from the two stations, B/d = 7/3, and
1/s₁ + 1/s₂ = 2/3 + 5/3. The cotangent is the blueprint's name for 1/s. π enters only where a slope is turned into an
angle, as in the parsec's 648000/π (R818).

**Kind: whole**, with a caution: this is two reads joined by a counted step, not one read. The step is a write; its
count is the B.

The same goes for the inverse square law. From no standpoint, L/(4πd²); from one, a round flat source of radius a seen on
its axis from d lights the receiver by its share 1/(1 + s²) of the hemisphere, s = d/a, whose far form is 1/s²; the
shares at s and 1/s add to the whole, half each at d = a (ISX). The 4π is the blueprint's, the whole sphere counted.

## 9. Only renamed

Some theorems keep a π that can be renamed but not removed. The Cauchy's normalising constant is one:

  (2/π)·∫₀^∞ ds/(1 + s²) = 1.

From one standpoint the heat 1/(1 + s²) is there with no π, and so are its ratios, its median at the corner and the
equality of the heat below the corner with the heat above it. What needs π is the total: the 2/π that makes the heat
add to 1. Write Ω for the total of one sweep and the constant is 1/Ω (essay 21). That makes the statement shorter and
says it is about one sweep. It does not make the total a single vantage's, since no finite count of a sweep reaches it.

**Kind: only renamed.** The equal halves are whole; the total is renamed.

## 10. Not at all

Some theorems have no single vantage form, because what they state is a completion.

- **The circle's area and circumference.** πr² and 2πr state the turn closed and the figure summed. A read closes
  nothing (R837).
- **The sum of reciprocal squares.** Σ 1/n² = π²/6 (Euler 1734). Its π comes from the slope's horizons at every odd
  multiple of the quarter turn, the slope carried past one read round the whole turn (R836).
- **The Gaussian.** The bell's (1/√(2π))·e^(−x²/2) is a law of amounts held from no standpoint; it says nothing about
  facing (R1036). What a single vantage holds of it is the ratio of two equal-spread Gaussians, which is the Cauchy,
  the turn's law, with no e and no π in its heat.
- **The exponential's limit.** e = lim (1 + 1/n)ⁿ is a length completed by repeated proportional steps. Every finite n
  gives a fraction, never e (BLD, essay 25).

**Kind: not at all.** These are the blueprint's statements in the strict sense: completions held whole. They are
exactly the laws where π or e is content, not notation (NTN, DVA).

## 11. What the sorting rests on

The table, gathered:

| theorem | from no standpoint | from one standpoint | kind |
|---|---|---|---|
| Pythagoras | a² + b² = c² | 1 + s² = (c/a)²; shares 1/(1 + s²) + s²/(1 + s²) = 1 | whole |
| angle addition | tan(α + β) = … | s ⊕ a = (s + a)/(1 − sa) | whole |
| Euler | e^(iπ) = −1 | w(s)·w(1/s) = −1; i·i = −1 at the corner | whole, but the endpoint |
| Thales | angle in a semicircle is right | readings s and 1/s cross square | whole |
| reciprocal product | π/2 × 2/π = 1 | s × (1/s) = 1 | whole |
| parallax | d = B/(cot α₁ + cot α₂) | B/d = 1/s₁ + 1/s₂ | whole (two reads, one count) |
| inverse square | L/(4πd²) | share 1/(1 + s²), far 1/s² | whole |
| Cauchy's total | (2/π)∫ ds/(1 + s²) = 1 | equal halves at the corner; the total 1/Ω | only renamed |
| circle's area | πr² | none | not at all |
| Basel | Σ 1/n² = π²/6 | none | not at all |
| Gaussian | (1/√(2π))·e^(−x²/2) | its ratio, the Cauchy | not at all |
| e | lim (1 + 1/n)ⁿ | every n a fraction | not at all |

The line runs where it was found to run on the lists: the single vantage restates exactly what relates directions to
each other, and has no form for what completes a turn, a length or a sum. The second kind is the narrow ground between,
where the relation is a single vantage's and the number that normalises it is a completion.

One algorithm holds both forms at once: draw's Tangent Bridge proves the rebuilding of a curve from an even lattice
in the angle chart, over the whole turn, and runs it in the slope chart with no trigonometric call, the two joined by
the half-angle s = tan(φ/2) (essay 10; essay 29 §7). It is the clearest single case of a theorem stated from no
standpoint and carried out from one.

Two cautions. The sorting is a reading, made one theorem at a time, and the tests that back it (NTN, DVA and the lists
after them) found the line moving each time it was named exactly (essay 24 §10). And "whole" does not mean shorter in
every case: the single vantage's forms are rational, which is the kind of thing they need, not always fewer symbols.

## 12. What is classical and what is ours

Classical: every theorem above, in both forms. The tangent addition formula, the stereographic landing point
(1 + is)/(1 − is) and its products, Thales and Euclid VI.8, the parallax formula in cotangents, the disc's on-axis
illuminance, the Cauchy's constant, Euler's sums, the Gaussian's ratio. None of the single vantage forms is a new
theorem.

Ours: the sorting. Which form belongs to which vantage; that the whole kind is exactly the theorems relating
directions, the not-at-all kind exactly the completions; that the reciprocal product and Euler's identity are members
of families whose other members need no π; and the reading that the blueprint's statement is the single vantage's
carried to its completion, where it can be, and stated whole, where it cannot.

## 13. What it changes

Nothing in the theorems. Each is as true in one form as in the other, and the blueprint's form is the one the books
will keep.

What it changes is what can be asked of a theorem. Ask "does this need the turn completed?" and most classical
statements about directions answer no: they have a form in slopes, rational, checkable to the last digit, with π only as
the name the blueprint gives a total no single vantage reaches. Ask it of the area of a circle, or of e, and the answer
is yes, and that answer is the content of the theorem. The two vantages share the geometry; what they differ in is
whether they ever hold it whole.

---

## Sources

- Tom, 16 November 2026: "Let's create a new essay that compares the dhv and shv versions of classical math theoroms".
- *Reads and Writes* (`../readers-and-writers.md`) §1 ("The same relation, held two ways", "The paper in one equation"),
  §6, §9 ("Facing V and facing away from V", "What is free, and what π costs").
- Essay 21 (`21-omega.md`): Ω. Essay 23 (`23-one-share-and-the-shape-of-a-law.md`): the disc's share, ISX. Essay 24
  (`24-only-a-name.md`): NTN, DVA and the lists after them. Essay 25 (`25-counted-toward.md`): BLD. Essay 27
  (`27-one-standpoint-or-none.md`): the two vantages side by side in AI.
- `plans/pyt-plan.md` (R1057; Tom: "Wow, Pythagoras is powerful for the SHV", "This seems foundational … Let's make
  sure it explored completely."), `plans/thl-plan.md`, `plans/ntn-plan.md`, `plans/dva-plan.md`, `plans/isx-plan.md`, `plans/bld-plan.md`.
- SPN rulings cited: R235, R725, R793, R809, R814, R818, R836, R837, R841, R847, R848, R950, R1036, R1037, R1042.
