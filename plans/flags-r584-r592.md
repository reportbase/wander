# Flags: what the rulings of 30 October leave inconsistent

*Written 30 October 2026, at Tom's "Flag any inconsistencies for future consideration." A list, not a ruling: nothing
below has been changed. Each entry names where the older text stands, which new ruling it meets, and the choice it
leaves. Line numbers are as of commit 17e21a2 and will drift.*

The rulings behind it (SPN):
- **R584:** π/2, 2/π and 1 as rates of the sweep; tan and arctan the writer's.
- **R585:** the corner where the three rates meet.
- **R587:** the writer's cube.
- **R588:** two 1's.
- **R589:** two sweeps, three axes.
- **R591:** the sphere is the writer's read of the reader. The reader reads with the Cauchy. π is not a reader's number.
- **R594:** the reader reconstructs the writer's cube by parallax and becomes the writer in doing it; the labels are
  roles, not kinds. It narrows R442 ("a reader can't become a writer").
- **R592:** one variable, H, makes only rationals. Irrationals need two variables and π the whole turn, both the
  writer's. The reader meets irrational directions but does not make them.

Applied so far: essay 14, essay 2 §7's new paragraph, OFS §4 "Rates, not angles", one sentence in OFS §3.7.

---

## 1. π/2 and 2/π called the reader's

R591 makes both the writer's account of the reader's sweep. Older text gives them to the reader, or to "the two
vantages", as the reader's own readings.

- **OFS:**
  - abstract and introduction (around lines 42 and 241: "the central … as π/2, the inscribed as 2/π, and their product
    gives the 1 back");
  - §3.1's table (the reader's inscribed sweep, 2/π);
  - §3.4 (both tables; "Where the numbers come from", which says the reader holds no mean and that 2/π is the uniform
    turn's);
  - §4 "Why the corner sits at 45°" ("the arc faced … is where π/2 and 2/π come from");
  - §10 step 3 (the thumb's two vantages).
- **SPN:**
  - R329: "the writer knows 1, readers read 1 as 2/π or π/2";
  - R450: Tom's "the reader only faces the arc … thats where the numbers PI/2 and 2/PI come from";
  - R570: π/2 attained from the centre, 2/π approached from home.
- **Companions:**
  - submission, around line 621;
  - physics companion, around line 705 ("OFS's reader, counting by its inscribed …");
  - CS companion wherever it repeats §3.4.
- **Essays:**
  - essay 2 §7's original text, "the writer's 1, read twice", and §10, "π/2 and 2/π, whose product returns the reader's
    own length";
  - essay 12 (π/2 attained, 2/π approached);
  - README row 2.
- **Demos:**
  - `mountain.html` ("the two vantages": "the outer reads π/2, the inner the fingers' mean shadow 2/π");
  - `one-read.html`, `paths.html`, `writer-readers.html` (one standpoint, the frame, π/2 · 2/π = 1);
  - `central-reader.html` step 6.

*Choice:* reword each as "the writer measures the reader's sweep at …", keeping the identities. The open question is
whether R329 and R450 are withdrawn, or read again as the writer's account. They are Tom's words and should be kept as
the record either way.

## 2. The circle as the reader's

R533 says the reader's one length, turned, traces the circle, and that "V = H is the writer's name for the reader's
circle". R591 makes the sphere the writer's picture of the reader. Does the circle go with it? Some text already pointed
that way:
- R368: the closed circle is the writer's join of the reader's arrays.
- R432: the reader never holds the sphere whole.

Where the circle is called the reader's:
- **OFS:**
  - "reader's circle", about 21 times;
  - §5's title, "The reader's circle";
  - Proposition 3(g), "the reader's own derivation" of the circle;
  - "the reader's unit circle", around lines 1489 and 2427.
- **CS companion:** 7 times. **Submission:** 6. **Physics companion:** 1.
- **Essays:** 1 (×4), 2 (×3, and its whole thesis: "the circle is the reader's before it is the writer's"), 7 (×3),
  8, 10, and the README.

*Choice:*
- **(a)** The circle, like the sphere, is the writer's picture of what the reader's one length does. The reader has only
  its open quarter of readings, the Cauchy.
- **(b)** The reader's one length traces the circle, but holds it only as a turn met, never as a closed whole or a total.
  The closed circle, with its 2π, is the writer's.

R591's wording suggests (a). R533 and essay 2 are built on something like (b).

## 3. "The reader's sphere", after Gibson

The same question in three dimensions.
- **OFS:** §3.7's sphere paragraph (R426–R428; one sentence added on 30 Oct says it is the writer's picture), and line
  1426, "the reader's sphere is …".
- **Essay 5:** line 262, "the reader's sphere in §5".
- **Demos:**
  - `blueprint.html` and `blueprint-3d.html`: "the reader is a sphere", R426;
  - `glass-box.html` and `writer-box.html`: "a sphere of radius H round its standpoint";
  - `sphere-cube.html`;
  - `recover.html`: "the census … the unit sphere".

*Choice:* as entry 2.

## 4. Halving with a square root

R592 puts bisecting a direction, s′ = (√(1 + s²) − 1)/s, on the writer's side: it takes the Pythagorean length of
[1 : s], two variables combined. The same goes for halving a level at its geometric middle (√2 on the first). The
doublings 2ᵏ stay the reader's.

- **OFS:**
  - §5 "Why halving" (Klein's criterion, Wantzel; "square roots reach every halving of the turn");
  - Appendix A "What square roots reach";
  - Appendix A's Viète entry ("the turn gives the halvings without a polygon");
  - line 809 ("halvings give Viète's product").
- **CS companion:** "Why halving".
- **Essay 4:** "Why halving".
- **SPN:** Appendix D and Proposition D.1, "on a level with only its ends, order and flip, the halving is the only
  subdivision supplied".

*Choice:* split "halving" in two.
- *Halving the length* (H to H/2, a level's count) is the reader's and rational.
- *Halving the angle or the level's ratio* (a geometric mean, a bisector) is the writer's.

The question is whether D.1's halving of a level, its middle on the ratio, is the reader's at all.

## 5. The lay 1 + ln s, and ζ = asinh x

A logarithm is transcendental, and by R591 and R592 the reader makes no transcendental. OFS's reader's lay (past the
corner, 1 + ln s by address count) and §6's hyperbolic ruler ("the reader's lay made smooth", ζ = asinh x) are written
with ln and asinh.

- **OFS:** 3 times, plus §6 "One figure, three rulers".
- **CS companion:** 3 times. **Submission:** 1. **Essays:** 8 (×2), 11.
- **Demos:** `levels.html`, `zoom.html`, `h-limits.html`, `star-field*.html`, `wedge.html` and the rest of the lay rulers.

*Choice:* the reader's lay is the count of doublings, an integer, so rational and the reader's. The smooth 1 + ln s, and
its ln 2 per level, are the writer's formula for that count.

## 6. The K distance addresses at H·tan(kπ/2K)

OFS §8 lays the reader's K addresses along distance at H·tan(kπ/2K): a tangent, and π. By R584 and R591 that formula is
the writer's, as laying an array on the quarter turn already is (R572, OFS §7.3's note of 30 Oct).

- **OFS** §8 (×3). **CS companion** (×2). **Submission.** **Essay 8.**
- **Demos:** `star-field*.html`'s ruler, `focus.html`, `fpv.html`.

*Choice:* the addresses are the reader's; the formula placing them is the writer's account. Say so where it appears.

## 7. Euler's formula as "the reader's notation"

R580, essay 2 §9 "Euler's formula, the reader's notation", OFS Appendix A "Polar form and the complex logarithm", and
`one-read.html`'s e^(2iθ) and e^(iπ) = −1 all write the reader's turn with exp, an angle θ, and π. By R591 these are the
writer's.

*Choice:* keep the content and rename it, "Euler's formula, the writer's notation for the reader's turn". The reader's
part is the address-times-payload split and the rational composition (tangent addition); the exponential and its π are
the writer's.

## 8. The hemisphere's 2 and ½

OFS §3.4 "With three unit relations" (R239, SIT) has "a hemisphere reads 2 at once, ½ one direction at a time". By R591
these are the writer's measure, though they are rational (2πr²/πr²: the π cancels).

*Choice:* the writer's, because they come from the sphere's totals, with a note that the π cancels. It may be worth
asking whether a rational outcome of a writer's measure is something the reader can hold.

## 9. The Cauchy's normalization and quartiles

R591 gives the reader the Cauchy up to its total: 1/(1 + s²) and the corner. The 2/π normalizing it, and its quartiles
√2 ∓ 1, are not the reader's to make (R592: met, not made).

- **OFS:** Proposition 5(d) and its proof (around lines 2094 and 2112, "quartiles √2 − 1 …, the integral is
  elementary"); §11.2's table (line 3655, "The exact Cauchy, its 2/π and quartiles …").
- **Essay 3** and the **submission**, wherever they state the law as the reader's with its constant.

*Choice:* state the law as the turn's; the reader holds it as order and the corner; the constant and the quartiles as
numbers are the writer's.

## 10. Several 1's in one essay

Essay 14 now has five things called 1:
- the writer's rate (the angle, arc per radius);
- the corner's reading, v/h = 1;
- the cube's edge and the diamond's h + v = 1, the "two 1's" (R588);
- the product π/2 · 2/π = 1;
- the sweep's running rates at zero.

They are kept apart in the text, but a reader of the essay may not keep them apart.

*Choice:* name them, for example the writer's rate, the corner, the edge, the sum, the product. Give each one name
throughout the series.

## 11. "The round 1 belongs to the turn"

R588 says the turn picks Pythagoras, the only measure every turn leaves unchanged. R592 says measuring with it (√2) is
the writer's. OFS §5 "The Euclidean choice" says the norm enters only through the measure on directions, the turn.

These can be reconciled: the turn fixes which measure, and using it on lengths is the writer's. But the three passages
do not yet say this the same way.

## 12. "Constructible" in the older corpus

R591's first wording, "the reader's operations reach the constructible numbers", was withdrawn the same day by R592:
only rationals are the reader's. But the archive's *The Algebra of Discrete Observation* gives its observer the field
operations and the halving square root, and the essays and OFS cite it. Its gems pulled forward (`plans/archive-gems.md`)
and essay 14 §6's quotation, "algebra kept, evaluation declined", should be checked against R592.

## 13. Demos' wording generally

Several demos (listed in entries 1, 3, 5 and 6) show π/2, 2/π, the sphere and the lay as the reader's.
`demos.html`'s cards and the CLAUDE.md entries describing them use the older wording too.

A wording pass, as R459 and R533 did, is needed once entries 1–3 are decided. Hooks, parameters and ids would stay as
they are.

---

## A proposed way through 1–3 (R594, 30 Oct)

Tom: "Seems to me the reader uses paralax to reconstruct the writers cube. And I'm the process becomes the writer, so the
labels are not static." If the labels name the act and not the observer, entries 1–3 can be read this way. Holding the
closed circle, the whole sphere, π, or π/2 and 2/π as totals of a completed turn, is something an observer does while
writing: joining facings or standpoints, holding what no one standpoint holds. The same observer reading from one place
has the open quarter and the Cauchy. So "the reader's circle" in OFS §5 and essay 2 would become the circle the
observer's one length traces, held whole only by the observer writing. That is consistent with R533 (one length, no V)
and R591 (the sphere is the writer's read). It still needs Tom's word before any rewording.

*Applied 30 Oct (R595, Tom: "Yes."):* "the one-length circle" throughout OFS, the companions and the essays; §5's opening
paragraph in OFS, the CS companion and the submission; π/2 and 2/π made the writer's measure in OFS's introduction,
§3.3, §3.4, §4 and §10 step 3, and in essay 2. Not yet: the π/2 and 2/π sentences in the companions and in essays other
than 2 and 14, R329/R450/R570 (kept as the record), and the demos (entry 13).

## Carried through (R596, 30 Oct, Tom: "Proceed")

Entries 4–13 applied in the papers, the essays and the demos' visible wording; see SPN R596 for the list. A consequence
to keep in view: being unmoved by scaling (the scale test, R568) is necessary for a reading and no longer sufficient;
a ratio that combines two lengths or takes the whole turn is made while writing. What remains: code comments and page
header comments that carry the older wording as history, and any passage this pass missed.

## Order suggested

Entries 1 to 3 are one decision for Tom: whether the circle goes the way of the sphere. Once that is made:
1. Entries 4–9 are mostly rewording.
2. Then 10–12.
3. The demos (13) last.
