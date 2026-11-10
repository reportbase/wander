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
