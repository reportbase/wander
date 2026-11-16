# PYT: Pythagoras from one standpoint, explored

16 Nov 2026. SPN R1057. Tom: "Wow, Pythagoras is powerful for the SHV", then, to adding it to essay 28: "Yes. This seems
foundational and supports the point of view or paper has taken. Let's make sure it explored completely."

## The question

From no standpoint (DHV) Pythagoras is a² + b² = c², three lengths in one unit. From one standpoint (SHV), divided by the
leg along the look, it is 1 + s² = (c/a)², no length left. R1056 says the read's kit comes out of that one line: the
shares, the Cauchy's heat, the exchange and corner, composition, the one square root, the whole-number triangles, the
same in space. "Explored completely" means checking each of those claims exactly, finding any the claim missed, and
saying where Pythagoras stops: what the read needs that it does not give.

Known beforehand, so not discoveries here: THL (the rays s and 1/s cross on the Thales circle, foot h², height hv);
ISX (a disc's light its share 1/(1 + s²)); WDG (the even wedge's readings the 2D Cauchy); draw's Tangent Bridge
(tb_algebra: the rational lattice from half-slopes, no trigonometric call); OFS Proposition 3(g) (a uniform sweep that
returns preserves an inner product) and §5 "The Euclidean choice" (π_p least at p = 2). Every identity below is classical;
what the plan tests is that each one is Pythagoras divided by the thumb, and nothing more.

## Predictions (committed before any run; `runs/pyt/pyt.py`)

Exact unless said: sympy for identities, fractions for counts.

- **P1. The shares.** For every rational s, 1/(1 + s²) + s²/(1 + s²) = 1; the exchange s ↦ 1/s swaps the two shares;
  they are equal only at s = 1 (and s = −1). Checked symbolically and on 10,000 seeded rationals.
- **P2. Composition is the product of sums of two squares.** With s ⊕ a = (s + a)/(1 − sa),
  1 + (s ⊕ a)² = (1 + s²)(1 + a²)/(1 − sa)², symbolically. Cleared of denominators this is the Brahmagupta–Fibonacci
  identity (x² + y²)(u² + v²) = (xu − yv)² + (xv + yu)², the product of Gaussian integers; so composing readings keeps
  Pythagoras, and that is what makes a composed turn rigid.
- **P3. The heat is unchanged by composing.** The measure ds/(1 + s²) is carried to itself by s ↦ s ⊕ a for every a:
  d(s ⊕ a)/ds divided by 1 + (s ⊕ a)², times 1 + s², is 1, symbolically; this follows from P2 alone. And by the
  exchange, d(1/s)/(1 + 1/s²) = −ds/(1 + s²).
- **P4. The landing point.** w(s) = (1 + is)/(1 − is) has |w|² = 1 because (1 + is)(1 − is) = 1 + s²;
  w(s)·w(a) = w(s ⊕ a); w(s)·w(1/s) = −1; w(1) = i. Symbolic.
- **P5. The rational directions.** Every rational point (x, y) on x² + y² = 1 other than (−1, 0) is
  ((1 − t²)/(1 + t²), 2t/(1 + t²)) for exactly one rational half-slope t = y/(1 + x). Checked exactly: every rational
  point with denominator up to 2,000 (found by enumerating primitive triples with c ≤ 2,000) has one t, and every t = p/q
  with |p|, q ≤ 60 gives a point on the circle. The whole-number triangles are exactly the rational slopes s whose
  √(1 + s²) is rational: s = 2t/(1 − t²).
- **P6. Rational directions never close a turn, but at the axes.** For a rational half-slope t, the landing point
  w = ((1 − t²) + 2ti)/(1 + t²) has wⁿ = 1 for some n ≥ 1 only for t ∈ {0, 1, −1} (and t = ∞): checked exactly in
  Gaussian rationals for every t = p/q with 0 ≤ p ≤ q ≤ 40 and n ≤ 200. So Pythagoras gives every rational direction and
  no closed turn among them but the quarter turns; closing needs the turn completed (Niven).
- **P7. Space, and n parties.** For n other parties, 1 + s₁² + … + sₙ² = (r/x)². The uniform law on the sphere Sⁿ, read
  on the flat screen square to the look (s = point/x), has density Γ((n + 1)/2)/π^((n+1)/2) · (1 + |s|²)^(−(n+1)/2):
  Pythagoras's sum raised to −(n + 1)/2. Checked symbolically by the Jacobian for n = 1, 2, 3 (the 1D Cauchy, the wedge's
  2D Cauchy, the 3D one), and numerically (a seeded sample of 200,000 points on S², the share within |s| ≤ 1 against
  1 − 1/√2, within 3 standard errors).
- **P8. Rational points in space.** Every rational point on the unit sphere but the south pole is the inverse
  stereographic image of a rational pair (t₁, t₂): ((2t₁, 2t₂, 1 − t₁² − t₂²)/(1 + t₁² + t₂²)). Checked on every primitive
  quadruple with d ≤ 300 (a² + b² + c² = d²).
- **P9. Only the square.** Replace a² + b² by |a|^p + |b|^p. For p = 1, 3, 4 and t = 1/3, the map (x, y) ↦ (x − ty, y + tx),
  scaled to bring (1, 0) back to the ℓ_p unit circle, takes some other point of that circle off it (by more than 10⁻⁶,
  60 digits); for p = 2 it keeps every point. So only Pythagoras's square gives a composition of directions that keeps
  one unit circle (OFS 3(g)'s inner product). Kill if any p ≠ 2 keeps all of 1,000 test points within 10⁻³⁰.
- **P10. Where it stops.** Three things the read uses that Pythagoras does not give, each checked:
  (a) the corner's share 1/√2 is irrational (the one root at the corner: 1 + 1² = 2 is not a square);
  (b) the heat's total ∫ ds/(1 + s²) over [0, ∞) is π/2, which no rational expression in s gives (π transcendental;
      sympy returns pi/2);
  (c) the median of the heat sits at s = 1 by the exchange alone, with no π: the heat below 1 equals the heat above it,
      by P3's exchange, symbolically, without computing either.
  So Pythagoras gives the relations and the corner; the total is the completion.

Kill conditions are each prediction's own; a failed one stays failed, and a fix is a new run with its own prediction.

## Runs
