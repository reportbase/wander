# CPX: when composing reads forces i

15 Nov 2026. A pasted note on the composition rule ("under what exact conditions does a family of linear
read-composition maps on the projective line admit a common operator J with J² = −I?"), Claude's reply, then a second
pasted note recommending it be recorded as a conditional lemma with an open derivation obligation. SPN R1014. Exact
rational arithmetic (Python `fractions`), seeded. Committed before any run.

## The question

Reads composed as real 2 × 2 linear maps on pairs [h : v] (tangent addition is the case A = [[1, −a], [a, 1]] up to
scale). Given a non-scalar map A in the family and every other map commuting with A, is the family forced to be
{pI + qJ} with J² = −I, so that i is derived from the maps rather than brought in with the chart W(s) = (1 + is)/(1 − is)?
And which of the premises does the work: linearity, commuting with A, A fixing no real direction?

Known beforehand: the linear algebra is classical (Cayley–Hamilton; the centralizer of a non-derogatory matrix is the
polynomials in it). The archived OFS Proposition 3(g) and R547 derived the imaginary rate from a sweep that returns.
WLK run 2 (R868) sorted a turn, a fixed share and a stride as elliptic, hyperbolic and parabolic maps; the archived
OFS §6 named the three rulers as the complex, split-complex and dual numbers (Yaglom; R472). What is tested is that
these join: the sign of one number decides which, and only the elliptic kind returns.

## Predictions (written before any run)

For seeded real 2 × 2 matrices A with rational entries (2,000 non-scalar), a = tr A/2, B = A − aI,
Δ = (tr A)² − 4·det A:

- **J1.** B² = (Δ/4)·I exactly, at every sample. So Δ < 0 gives J = B/√(−Δ/4) with J² = −I.
- **J2.** The rational solutions C of CA = AC form a space of dimension exactly 2, spanned by I and A (so by I and B),
  at every sample, whatever the sign of Δ.
- **J3.** The sign of Δ decides the algebra of that commutant: with p + q·u standing for pI + qB/|Δ/4|^½, u² = −1 for
  Δ < 0 (complex), +1 for Δ > 0 (split-complex), u = B nilpotent, B² = 0, for Δ = 0 (dual). Checked as exact products
  (p₁I + q₁B)(p₂I + q₂B) = (p₁p₂ + q₁q₂·Δ/4)I + (p₁q₂ + p₂q₁)B at every sample.
- **J4.** Fixed directions: A has 0 real eigen-directions for Δ < 0, 2 for Δ > 0, 1 for Δ = 0 (non-scalar), at every
  sample.
- **J5.** Return: among all samples and the constructed maps [[0, −1], [1, 0]], [[1, −1], [1, 1]], [[−1, −1], [1, 0]],
  [[1, −1], [1, 0]], every A with a power Aⁿ (1 ≤ n ≤ 64) equal to a scalar times I has Δ < 0; no sample with Δ ≥ 0
  has one. The constructed maps return at n = 2, 4, 3, 6.
- **J6.** Dropping commutativity: K_c = [[0, −c²], [1, 0]] (its own K_c² = −c²·I) commutes with J₀ = [[0, −1], [1, 0]]
  exactly when c² = 1, for c² in {1/4, 1/2, 1, 2, 4, 9}. And the quadratic forms Q with AᵀQA = det(A)·Q, for A elliptic,
  form a space of dimension exactly 1 (one inner product up to scale); for J₀ that form is h² + v², for K_c it is
  h² + v²/c², the ellipse V = cH.

Kill condition: any of J1–J6 false at any sample. A killed prediction stays killed; a fix is a new run.

## What it would and would not show

If nothing is killed: a conditional lemma. Linear maps on the pair, commuting with one map that fixes no real direction,
are the complex numbers; the same family fixing two directions or one is the split-complex or dual numbers; only the
first returns. It would not show that a read's composition is linear, commutative or returning: those stay premises
(the open obligation), to be named in the note, not claimed.

## Runs

(below this line, nothing above is edited)
