# CLM: the pull from columns, a derivation path

25 Nov 2026; Tom: "I think this is more than sorting, it shows a different derivation path.", then "yes". The static
gravity runs (GRV, FCL, COS) built a pull from a place outward: each direction from the place, weighed by the matter
along it, summed over directions. This plan asks what that route assumes and what it derives. Exact arithmetic (sympy)
and 30-digit quadrature (mpmath); no data. A pull is not a read (R1183); the route is a way to think about gravity, not
new physics (R1190).

## The premise, stated

A central, additive pull: a mass element dm at distance r along the unit direction u pulls a body at the place by
G·dm·f(r)·u. In D dimensions dm = ρ·r^(D−1)·dr·dΩ, so the pull from one direction is

  dF(u) = G·u·dΩ·∫ ρ(r u)·f(r)·r^(D−1) dr.

**The column premise (P):** the pull from a direction depends only on how much matter lies along it, the column
∫ ρ dr, and not on where along the direction it sits. Then the route is: directions from the place, each weighed by its
column, summed.

## What I know beforehand (said, so the predictions are not blind)

- (P) holds for every ρ exactly when f(r)·r^(D−1) is constant (a linear functional of ρ depending only on ∫ρ dr has a
  constant kernel): f ∝ r^(−(D−1)), the inverse square in three dimensions. That step is immediate; C1 only checks it.
- Newton, *Principia* Book I: Proposition 70 (no pull inside a shell, by pairing the two ends of each chord) and
  Proposition 71 (outside, the shell pulls as its mass at the centre); Propositions 77–78 treat the force growing as r,
  for which a shell also pulls from outside as its mass at the centre. From memory; to check.
- So the outside shell theorem does **not** single out the inverse square: f = A/r² + B·r passes it for every A, B. I
  said otherwise in the message before this plan ("the converse ... so the two are equivalent"); that was wrong, and the
  predictions below say what I now expect.

## Predictions (committed before any code)

- **C1 (column only).** In D = 2, 3, 4, sliding a fixed column along one direction (the same ∫ρ dr, placed at different
  distances) leaves that direction's pull unchanged exactly when p = D − 1 for f = r^(−p); for p = D − 1 ± ½ it changes
  (by more than 1% between a column at r ∈ [1, 2] and at r ∈ [5, 6]).
- **C2 (the shell from columns).** A thin shell of radius a and surface density σ in three dimensions. Summing over
  directions from the place, each direction's column being σ/|cos χ| at each crossing (χ the angle to the shell's normal
  there), gives at an outside place d > a exactly G·M/d² toward the centre, M = 4πa²σ (sympy), and at an inside place
  exactly zero.
- **C3 (why inside is zero).** From any inside place, the two ends of every chord meet the shell at equal angles, so a
  direction and its opposite carry equal columns (exact, sympy, for every inside place and direction). Under (P) the two
  pulls cancel direction by direction; for f = r^(−p), p ≠ 2, the two ends' pulls are in the ratio (r₁/r₂)^(2−p) and do
  not cancel.
- **C4 (the Hooke exception).** For f = A/r² + B·r in three dimensions, the outside shell pull equals the point mass at
  the centre for every A and B (exact); the inside pull is zero only when B = 0 (it is B·M times the place's offset from
  the centre). So the outside theorem allows the r term; outside and inside together leave only the inverse square in
  this family.
- **C5 (power laws).** For f = r^(−p), p ∈ {1, 1.5, 2.5, 3}, a shell at d = 2a fails the outside theorem (off by more than
  1%) and pulls inside (at half the radius from the centre, more than 1% of the outside value); at p = 2 both hold to
  10⁻²⁵. In two dimensions a ring at p = 1 has no inside pull and pulls from outside as its mass at the centre.
- **C6 (scale).** Lengths × k at fixed density: every direction unmoved, the strength × k (each column × k); a ratio of
  two places' pulls unmoved.

Kill: an identity (C2, C3, C4's exact parts, C6) not exact in sympy or off past 10⁻²⁵ in quadrature; C1 or C5 a
threshold not met.

What it would answer: whether "directions weighed by columns" is a starting point equivalent to Newton's law. If C1–C4
hold: (P) is equivalent to the inverse square (in D dimensions, 1/r^(D−1)); from (P) the shell theorems follow by
summing directions, no field equation solved; the outside theorem alone is weaker (it admits the r term), and (P)'s
direction-by-direction pairing is what removes it. Classical in its parts (Newton 70, 71, 77); the claim to check is
whether the column premise as the starting point, and its equivalences, are stated in print.

## Runs

### Run 1 (`runs/clm/clm.py`, output `runs/clm/clm-run1.txt`)

**C2 killed, by my set-up.** The shell summed over directions is exactly G·M/d² outside and exactly zero inside in
sympy (the identity holds), but the 30-digit quadrature in θ came out 2.6·10⁻²¹ off with a complex part of 8·10⁻²¹, past
my 10⁻²⁵: the column σa/√(a² − d² sin²θ) is infinite at the edge direction θ = asin(a/d), the endpoint is rounded, and
the root of a tiny negative number went complex. My quadrature, not the identity; killed by its letter all the same.
- **C1 not killed**: a column slid from [1, 2] to [5, 6] leaves its direction's pull unchanged exactly at p = D − 1 in
  D = 2, 3, 4, and moves it by +92% and −48% at p = D − 1 ∓ ½.
- **C3 not killed**: from any inside place a direction and its opposite meet the shell at equal |cos χ|, identically
  (sympy); at p = 2 the two ends' pulls equal, at p = 1.5 and 2.5 in the ratio 0.758 and 1.319.
- **C4 not killed**: f = A/r² + B·r pulls from outside as the point mass at the centre (A·M/d² + B·M·d) for every A, B,
  and from inside B·M·b, zero only at B = 0 (exact).
- **C5 not killed**: at p = 1, 1.5, 2.5, 3 the outside shell is off the point mass by −8.8%, −5.7%, +8.9%, +21.6% and
  pulls inside (0.39, 0.28, −0.55, −1.54 of the outside value); at p = 2 both exact to 10⁻⁴⁷; a ring at p = 1 in two
  dimensions to 10⁻⁴².
- **C6 not killed**: two shells and a place off both axes, lengths × k at fixed density: the pull × k exactly, its
  direction unmoved.

### Run 2, predictions (committed before its code)

- **C2′.** The same outside sum by quadrature in w = sin²θ over [0, a²/d²] with the endpoint exact (a = 1, d = 3, σ = 1),
  real throughout, equals 4π/9 to 10⁻²⁵; and at d = 1.5 and d = 10 equals 4π/d² to 10⁻²⁵. Kill past 10⁻²⁵.

### Run 2 (`runs/clm/clm2.py`, output `runs/clm/clm-run2.txt`)

**C2′ killed, by my set-up again.** Real now, but off 2.4·10⁻²¹, 9.5·10⁻²¹ and 1.1·10⁻²² at d = 3, 1.5, 10, past my
10⁻²⁵. The cause, seen after the run: 1 − d²w is computed near the edge direction by subtracting two nearly equal
numbers, so at 40 digits it keeps about half of them, and an inverse square root there limits the sum to about
√(10⁻⁴⁰) = 10⁻²⁰. A quadrature measured from the edge (v = 1 − d²w) would remove the cancellation, but it is the integral
of 1/√v, which is the sympy identity written again, so I stop: C2's identity stands exactly in sympy (run 1), and the
two numerical checks of it were killed by my numerics, not by the shell.

Reading of runs 1–2: the column premise (P), "the pull from a direction depends only on how much matter lies along it,
not where", is equivalent to the inverse square (1/r^(D−1) in D dimensions; C1). From (P) alone, summing directions
gives both of Newton's shell theorems with no field equation solved: outside, each direction's two crossings carry
σa/s each and the sum is G·M/d² (C2, exact); inside, every direction and its opposite carry equal columns because a
chord meets a sphere at equal angles at its two ends, so the pulls cancel direction by direction (C3). The outside
theorem alone is weaker: the force growing as r passes it too (C4). The inside theorem is where (P) is used whole, and
among A/r² + B·r and among powers it leaves only the inverse square (C4, C5). Scaling moves no direction (C6).
Classical in its parts (Newton, *Principia* I, 70, 71, 77, from memory); whether the column premise is stated in print
as a starting point equivalent to the law is the open question for the search.

### The search (one round, 25 Nov, at snippet depth)

- Wikipedia's *Shell theorem* has the converse: a central force law that adds over the shell allows the extra term
  (the r law), and requiring no force inside a hollow ball excludes it, leaving the inverse square unique. So C4 and C5
  are in the standard account (R1206: well known).
- Newton's Proposition 70 proves the inside case by pairing opposite parts of the sphere, and the cone of small solid
  angle cutting a shell on its near and far sides is the classical form of the argument (Cavendish's null method, as
  told in arXiv:1608.01520). C3 is that argument.
- Proofs of Proposition 71 by the solid angle a sphere subtends are in print ("Newton revisited", arXiv:0910.4807;
  "On Newton's shell theorem", ResearchGate). So C2's route by directions is known too.
- Not found: the premise (P) stated by itself, "a direction's pull is its column", as a starting point equivalent to
  the law. It is one line away from what is in print (the r² of the cone's cross-section cancelling the 1/r²), and Gauss's
  law is the same fact in flux form, so I would not call it new.

Plain assessment: the derivation path is real and exact, and it is Newton's own (the cone argument of Propositions 70
and 71), with Gauss's law its field-equation form. What the stage adds is where it sits: the pull as the read's cosine
weight over directions with each direction weighed by its column (COS), so the inverse square is the condition that a
direction's weight is its amount alone, wherever along it the amount lies.
