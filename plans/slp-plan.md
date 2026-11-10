# SLP: the reader's math, in slopes

*10 November 2026, SPN R794. Tom: "Yes, trig is an abstraction layer. Readers don't use it. So to study readers we need
to use the math they do." After R793 (the reader uses no trigonometry; readers hold v/h, writers hold angles) and draw's
`tb_algebra.md` (the slope chart, no trigonometric call). Exact arithmetic (sympy). Predictions written and committed
before any script; scripts in `runs/slp/`.*

## Known beforehand

- Tangent addition (s₁ + s₂)/(1 − s₁s₂) is the angle's addition in the slope; (1 + is)/(1 − is) is the doubled turn,
  a rational point on the circle (classical). ELM: n reads composed by tangent addition are exact at every n.
- The half-angle: a writer's angle φ of total 2π has slope t = tan(φ/2); a line's angle θ of total π has s = tan θ;
  s = 2t/(1 − t²) (classical; TB's convention table).
- SRA: aberration is t ↦ t/k on the stereographic coordinate t = tan(θ/2), θ from the motion's axis (classical).
- The heats in angles: cos²θ in the plane, cos³α on a screen (R706, R702).

## Predictions

**S1. The reader's results are rational in s.** Each of these, stated in the writer's angles in the corpus, equals a
rational function of its slope(s) with √(1 + s²) the only irrational step, identically: (a) the heat per unit of reading,
1/(1 + s²) = h²; (b) the screen's heat, 1/(1 + s² + s₂²)^(3/2) = h³ (h the share along the look); (c) with n thumbs,
h^(n+1); (d) the overlay's sech(ln x) = 2x/(1 + x²) = 2hv at s = x; (e) the composition of two reads; (f) the doubled turn
and its real and imaginary parts (1 − s²)/(1 + s²), 2s/(1 + s²); (g) the depth point d·(1 + iγ)/(1 − iγ) and its median
d·(1 − γ²)/(1 + γ²); (h) the thing-as-H distance 1/(2t); (i) essay 18's heat cos²(θ − 45°) = (1 + s)²/(2(1 + s²)); (j)
the corner as the fixed point of s ↦ 1/s. *Killed* if any identity fails.

**S2. π enters only at totals.** The share passed, (2/π)·arctan s, the half-Cauchy's normalization, and arc over chord
θ/sin θ in s, arctan(s)·√(1 + s²)/s, each need arctan or π: none equals a rational function of s with square roots (each
is not algebraic in s: its derivative is algebraic but it is not, shown by its limit behaviour, arctan s → π/2 as s → ∞
while every algebraic function of s with a finite limit at ∞ has a Puiseux expansion; checked by sympy's algebraic test
on the first few terms). A writer's sum over the turn; no reader's result in S1 contains π. *Killed* if any S1 form needs
π or arctan, or an S2 form is algebraic.

**S3. A boost is not a map of s.** The reader's read is a line's direction [h : v]: θ and θ + π are one s. A boost of the
moving sky (rapidity η along the axis) sends the directions θ and θ + π to directions that differ by other than π, so no
function of s gives the boosted s. Shown exactly: for some s, the two preimages give two different boosted s. *Killed* if
the boosted s is a function of s.

**S4. In t, turns and boosts are both Möbius.** On t = tan(φ/2) (oriented, total 2π), a turn by α is
t ↦ (t + a)/(1 − a·t), a = tan(α/2), and a boost is t ↦ t/k, k = e^η; their compositions are Möbius maps of t
(matrices of determinant one up to a factor), so the sky's motions are linear-fractional in t, rational, no angle.
*Killed* if a composition fails to be Möbius in t.

**S5 (the reading, not testable here).** If S3 and S4 hold, a reader of a single quarter turn holds s, and a reader of a
sky in motion needs the oriented slope t; the half-angle is the passage from the line of directions to the oriented
circle. Stated only as a reading of S3–S4.

## Runs

**Run 1** (`runs/slp/slp.py`, output `runs/slp/slp-run1.txt`; 10 Nov). S1 killed by my set-up; S2, S3, S4 not killed.
- S1: nine of ten identities hold symbolically and no slope form has π or arctan. (b), cos³α = 1/(1 + tan²α)^(3/2), was
  reported false: sympy does not reduce √(cos²α) to cos α without knowing α < π/2 (I declared α only positive). It holds
  to 3·10⁻⁵¹ at 156 angles in (0, π/2). My check, not the identity; the kill stands as recorded.
- S2: the share passed and arc over chord, written in s, carry arctan; the share reaches 1 at the horizon. That arctan is
  transcendental is classical (not shown here).
- S3: θ and θ + π have one s, and after a boost their s differ by
  2kt(k²t² + k² − t² − 1)/((k² − t²)(k²t² − 1)), −72/35 at t = ⅓, k = 2: **a boost is not a map of s.**
- S4: turns are t ↦ (t + a)/(1 − at) and boosts t ↦ t/k on the half-angle slope, their compositions Möbius, and t ↦ t·√((1 −
  β)/(1 + β)) is exactly the aberration cos θ′ = (cos θ + β)/(1 + β cos θ).

**Before run 2: S1′.** S1(b) checked with c = cos α declared positive and tan²α = (1 − c²)/c², so the root reduces
honestly; every other item of S1 as in run 1. *Killed* if any identity fails.

**Run 2** (`runs/slp/slp2.py`, output `runs/slp/slp-run2.txt`; 10 Nov). Nothing killed: S1′ holds, every item of S1
identically, no slope form with π or arctan; S2–S4 as in run 1.

**What SLP shows.** In the reader's own math the reader's results are rational, and the simplifications are real, not
relabelling: the heat is the share along the look raised to the number of thumbs plus one (h², h³, h^(n+1)); the
overlay's far-field heat is 2x/(1 + x²), the same form as the facing's height 2hv; composition, the doubled turn and the
depth error are rational. π and arctan appear only where the turn is summed whole (the share passed, the constant, arc
over chord): a writer's total. And one thing the angle chart hid: **a boost is not a map of the reader's slope s.** A read
holds a line's direction, [h : v], so θ and θ + π are one reading, and a motion distinguishes forward from back; on the
oriented half-angle slope t, turns and boosts are both Möbius and the sky's motions are rational. So the half-angle is
not a convention: it is the step from a read of directions as lines (s, period π) to directions with a front and a back
(t, period 2π), and a moving sky needs the second (S5, a reading). Open: what in the reader's situation supplies the
orientation (a front), since one quarter turn has none to choose.

**After run 2 (10 Nov): an over-claim corrected, and halving.** Tom: "What does the math say?", of whether the reader may
halve a turn (draw's *Tangent Bridge* builds its lattice with √(1 + s²); R592, R596 call halving a turn the writer's);
then "Proceed with your recommendations". Exact (sympy):
- From the ratio s alone, halving solves s = 2t/(1 − t²): t = s/(1 + √(1 + s²)), outside the rational operations (tangent
  addition, the reciprocal): from s = 1 they reach only 0, ±1, ∞, and tan(π/8) = √2 − 1 needs √2. Holding the shares h, v
  with h² + v² = 1, halving is rational, t = v/(1 + h) (doubling it gives back v/h, checked). That condition is the
  one-length circle, the writer's (R717), and √(1 + s²) = 1/h its measure. So doubling a turn is the reader's, halving one
  the writer's (R596 stands); TB's lattice is the writer's construction, met by the reader, not built.
- S1's summary above said the reader's results are rational in s "with √(1 + s²) the only irrational step". In the plane
  they are rational; in space the screen's heat h³ = (1 + s² + s₂²)^(−3/2) is not: it needs the root, the circle's measure,
  in the heat itself. S1's identities stand; the summary's "rational" holds in the plane only.
