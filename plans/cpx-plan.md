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

### Run 1 (15 Nov 2026; `runs/cpx/cpx.py`, output `runs/cpx/cpx-run1.txt`)

2,000 seeded rational maps (800 elliptic, 800 hyperbolic, 400 parabolic). J1–J4 not killed; J5 and J6 killed, both by
my arithmetic.

- **J1.** B² = (Δ/4)·I exactly at all 2,000: Δ < 0 gives J with J² = −I from the map itself, no chart brought in.
- **J2.** The commutant of every map is exactly two-dimensional, spanned by I and A, at every sign of Δ.
- **J3.** Its products are the complex numbers for Δ < 0, the split-complex for Δ > 0, the dual numbers for Δ = 0, at
  every sample. The three kinds of map (WLK run 2) and the three rulers (Yaglom) are one family split by the sign of Δ.
- **J4.** Parabolic samples fix one direction (B ≠ 0, det B = 0) at all 400. (For Δ ≠ 0 the count is the sign of Δ,
  so this part was nearly definitional.)
- **J5 killed** (30 failures). 29 hyperbolic samples return at n = 2: every one has trace 0 and det < 0, a reflection, which
  fixes two directions yet squares to a scalar. I noticed this case after committing the
  plan and before running; the plan was not edited. And I predicted [[1, −1], [1, 0]] returns at 6: its cube is −I, a
  scalar, so projectively 3 (I counted the linear order, not the projective one). Post hoc (`runs/cpx/cpx1-posthoc.py`):
  of the 640 samples with det > 0 and Δ ≥ 0 none returns, so among maps that keep orientation only the elliptic return.
- **J6 killed** (1 failure). K_c commutes with J₀ exactly at c² = 1 (held), the preserved form is one-dimensional for
  all 800 elliptic samples and for every K_c (held), but the form K_c keeps is h² + c²·v², not h² + v²/c² as I wrote
  (post hoc, checked at c² = ¼, 2, 9): my slip in which axis carries c. The content stands: two turns with different c
  are two ellipses, and a shared J is one inner product.

How hard a test it was: J1–J3 are Cayley–Hamilton and the centralizer of a non-scalar 2 × 2 matrix, so they could not
fail as linear algebra; the run checks the arithmetic and the joining of the three kinds. What a run cannot give is the
open obligation: that a read's composition is linear, commutes, keeps orientation and returns. Those stay premises.
