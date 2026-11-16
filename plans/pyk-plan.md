# PYK: the other two Pythagorases, 1 − s² and 1

16 Nov 2026. SPN R1058. Tom: "What's next", then, to Claude's proposal of testing the boost's and the stride's
Pythagoras as PYT tested the turn's: "Yes and proceed with tests".

## The question

PYT showed that the read's kit (shares, corner, composition, heat, rational directions, the n-party law) comes out of
1 + s² = (c/a)², and that it stops at π. CPX (R1014) found that composing directions by one linear map on [h : v] comes
in three kinds, set by a sign: turns (elliptic), boosts (hyperbolic), strides (parabolic). Write them as one family,

  s ⊕_κ a = (s + a)/(1 − κ·s·a),  with κ = +1 (turns), −1 (boosts), 0 (strides),

the matching "Pythagoras" being 1 + κ·s². For κ = −1 that is special relativity's γ = 1/√(1 − β²) with s = v/c, and
E² − p² = m². Does each kind carry its own corner, heat, composition, rational lattice and stopping point, and where do
they part from the turn's?

Known beforehand, so not discoveries: CPX (the three algebras), WLK run 2 (turn, fixed share and stride as elliptic,
hyperbolic and parabolic maps of Euler's circle), MOT run 3 (the Doppler pair's corner at rest, the sky's moved by a
boost), EMC (E² = (pc)² + (mc²)² as a unit circle of shares, Newton's and the ultra-relativistic forms each other's
flips), SRB (the rapidity the Poincaré distance), Yaglom's three geometries (archived OFS §6). Everything below is
classical; what is tested is that the three sort the way stated, and what the boost and the stride have that the turn
lacks, and lack that it has.

## Predictions (committed before any run; `runs/pyk/pyk.py`)

Exact: sympy for identities, fractions for counts, mpmath where a limit is checked.

- **K1. One identity, three signs.** 1 + κ(s ⊕_κ a)² = (1 + κs²)(1 + κa²)/(1 − κsa)², symbolically in κ. Cleared of
  denominators: (x² + κy²)(u² + κv²) = (xu − κyv)² + κ(xv + yu)², the norms of the complex (κ = 1), split-complex
  (κ = −1) and dual (κ = 0) numbers multiplying. For κ = −1 the composed slope is the relativistic addition of
  velocities, (s + a)/(1 + sa).
- **K2. The heat each kind keeps.** ds/(1 + κs²) is carried to itself by every s ↦ s ⊕_κ a (symbolically, each κ):
  turns dθ, boosts the rapidity dη, strides ds itself. No other density of the form (1 + κs²)^(−p) is kept for p ≠ 1
  (checked at p = ½, 2).
- **K3. Only the turn has a total.** Over the whole chart: κ = 1, ∫ ds/(1 + s²) over ℝ is π; κ = −1, ∫ ds/(1 − s²)
  over (−1, 1) diverges; κ = 0, ∫ ds over ℝ diverges. So only the turn's heat normalises into a probability, and only
  the turn carries a π. The boost and the stride have no invariant probability law at all (no Cauchy of their own, no
  median), as their groups are not compact.
- **K4. Shares and the corner.** For the boost, 1/(1 − s²) − s²/(1 − s²) = 1 (γ² − (γβ)² = 1): a difference, not a sum,
  so the terms are not shares (1/(1 − s²) ≥ 1, s²/(1 − s²) ≥ 0, their difference 1). The turn's corner (shares equal) has no
  boost counterpart for |s| < 1: the two terms are equal nowhere. The boost's fixed point is s = ±1, the light cone:
  1 ⊕₋₁ a = 1 for every a ≠ −1 (exactly), so the light cone is the one direction every boost leaves where it is, a
  fixed point of composition and never reached from |s| < 1. The stride has no fixed point but ∞.
- **K5. The exchange in each kind.** The turn's exchange s ↦ 1/s swaps its shares and fixes the corner. For the boost,
  the Doppler factor k(s) = √((1 + s)/(1 − s)) multiplies under composition, k(s ⊕₋₁ a) = k(s)·k(a) (exactly, as
  squares), and s ↦ −s sends k to 1/k; its fixed point is s = 0, rest. So the boost's exchange fixes rest and its
  horizon is the light cone, the reverse of the turn's arrangement (MOT run 3). The stride: s ↦ −s, fixed point 0, no
  horizon.
- **K6. The rational lattice.** Every rational point of the hyperbola x² − y² = 1 with x > 0 is
  ((1 + t²)/(1 − t²), 2t/(1 − t²)) for exactly one rational t in (−1, 1): checked on every rational point with
  denominator up to 2,000 found by enumeration (x = c/d, y = e/d with c² − e² = d²), and every t = p/q, |p| < q ≤ 60,
  landing on the hyperbola. So the boost has its whole-number "triangles" (c² = d² + e², read the other way round, the
  same Pythagorean triples), and composing two gives a third (K1).
- **K7. Nothing closes.** For a rational t with 0 < t < 1, the boost's landing point w = ((1 + t²) + 2t·j)/(1 − t²)
  (j² = 1) has wⁿ ≠ 1 for every n ≤ 200 (exactly, in pairs of fractions); its Doppler factor kⁿ grows without bound.
  So, unlike the turn, no boost closes at all: no quarter turn, no exception. The stride's n-th power is n·s, never 0.
- **K8. Only the square, for boosts too.** With |x|^p − |y|^p in place of x² − y² (p = 1, 3, 4) one composed boost step
  (x, y) ↦ (x + ty, y + tx), scaled to bring (1, 0) back to the curve, moves some other point of the curve off it by
  more than 10⁻⁶; for p = 2 it keeps every point to 10⁻⁵⁰.
- **K9. The limits.** The boost's and the turn's compositions both tend to the stride's, s ⊕_κ a = s + a + κ·sa(s + a)
  + O(5th order) (series in a scaling ε → 0, symbolically): Galilean addition of velocities is the stride, and the
  first correction has the sign of κ. And the boost's Pythagoras at small s is 1 − s², the turn's 1 + s², their
  product 1 − s⁴: the two kinds are each other's mirror in s ↦ i·s (sympy: substituting s → i·s in the turn's identity
  gives the boost's).

Kill conditions are each prediction's own; a failed one stays failed, and a fix is a new run with its own prediction.

## Runs
**Run 1** (16 Nov, `runs/pyk/pyk.py`, output `runs/pyk/pyk-run1.txt`). 6 of 9 not killed; K2, K3, K7 killed, each by my
set-up or code, not by the mathematics.
- K1 not killed: 1 + κ(s ⊕_κ a)² = (1 + κs²)(1 + κa²)/(1 − κsa)² for every κ; the norms of complex, split-complex and
  dual numbers multiply; κ = −1 is the relativistic addition of velocities.
- K2 killed by my set-up: ds/(1 + κs²) is kept by composition for all three kinds, and for the turn and the boost the
  powers ½ and 2 are not; but for the stride 1 + 0·s² = 1, so every power is the same density and the clause "no
  other power is kept" was empty there.
- K3 killed by my code: the turn's total is π; the stride's ∫₀^∞ ds is ∞; sympy returned the boost's ∫₀¹ ds/(1 − s²) as
  ∞ + iπ/2 (its logarithm's branch), so my test `== oo` failed, though the integral diverges.
- K4 not killed: γ² − (γβ)² = 1, the two terms equal nowhere, the light cone s = ±1 fixed by every boost, composition
  keeping every |s| < 1 inside (9,801 pairs of fractions).
- K5 not killed: Doppler factors multiply under composition; s ↦ −s sends k to 1/k; its fixed point is s = 0, rest.
- K6 not killed: all 7,121 rational points of x² − y² = 1 with x > 0 and denominator ≤ 2,000 come from one rational t
  in (−1, 1) each; every t = p/q, q ≤ 60, lands on the hyperbola.
- K7 killed by my set-up: of 489 rational half-slopes in (0, 1) none closes within 200 steps (the prediction's main
  clause held); "the Doppler factor grows without bound" was tested as k²⁰⁰ > 10¹⁰, which fails for t = 1/40
  (k = 41/39, k²⁰⁰ ≈ 2·10⁴), though k > 1 makes kⁿ unbounded.
- K8 not killed: one composed boost keeps x² − y² = 1 to 7·10⁻⁶⁰ and moves |x|^p − |y|^p = 1 by 1.0, 0.38, 0.6 for
  p = 1, 3, 4.
- K9 not killed: s ⊕_κ a = s + a + κ·sa(s + a) + O(5th order); the turn's identity at s ↦ is is the boost's.

**Run 2** (predictions written before it runs; `runs/pyk/pyk2.py`):
- **K2′.** For κ = ±1 only, (1 + κs²)^(−p) at p = ½ and 2 is not kept by composition (at seeded rational s, a, the
  ratio ≠ 1); for κ = 0 every power reduces to 1, so the stride's kept measure is ds and the question is empty.
- **K3′.** The boost's ∫₀^(1 − δ) ds/(1 − s²) equals ½·ln((2 − δ)/δ) exactly (symbolically), so it exceeds any bound as
  δ → 0 (at δ = 10⁻ⁿ for n = 1 … 50 it equals ½·ln(2·10ⁿ − 1) to 10⁻⁴⁰).
- **K7′.** For every rational t = p/q in (0, 1) with q ≤ 40, the Doppler factor k = (1 + t)/(1 − t) > 1 exactly, so
  kⁿ is strictly increasing in n (k²⁰⁰ > k¹⁰⁰ > 1 exactly).
Kill if any differs.

Run 2 result (`runs/pyk/pyk2.py`, output `runs/pyk/pyk-run2.txt`): K2′ and K7′ not killed (the powers ½ and 2 not kept
by turns or boosts; every rational Doppler factor > 1, its powers strictly increasing). K3′ killed by my precision: the
symbolic clause held (∫₀^(1 − δ) ds/(1 − s²) = ½·ln((2 − δ)/δ) exactly), and the numerical clause held at δ = 10⁻¹, 10⁻⁵,
10⁻¹⁰, 10⁻²⁰ (to 10⁻⁴²), but at δ = 10⁻⁵⁰ with 60 working digits 1 − δ keeps 10 significant digits of the gap and the
quadrature (and atanh itself) missed by 1.1·10⁻¹².

**Run 3** (prediction written before it runs; `runs/pyk/pyk3.py`): K3″, the same numerical clause at 120 working digits:
∫₀^(1 − δ) ds/(1 − s²) within 10⁻⁴⁰ of ½·ln(2·10ⁿ − 1) at δ = 10⁻ⁿ, n = 1, 5, 10, 20, 50. Kill if any differs.

Run 3 result (`runs/pyk/pyk3.py`, output `runs/pyk/pyk-run3.txt`): K3″ killed by my set-up: errors 2·10⁻¹²¹ to
4·10⁻⁹⁵ for n ≤ 20, but 1.7·10⁻³⁸ at n = 50, the quadrature itself, not the precision, failing to resolve an integrand
that rises to 10⁵⁰ within 10⁻⁵⁰ of the end. No further numerical run: the divergence rests on run 2's exact identity,
∫₀^(1 − δ) ds/(1 − s²) = ½·ln((2 − δ)/δ), and the numbers to n = 20 agree with it.

What the runs show (every identity classical; the sorting ours):
- One composition, s ⊕_κ a = (s + a)/(1 − κsa), and one identity, 1 + κ(s ⊕_κ a)² = (1 + κs²)(1 + κa²)/(1 − κsa)²,
  cover all three kinds: Pythagoras's sum for turns, its difference for boosts (relativistic velocity addition,
  γ² − (γβ)² = 1), and nothing at all for strides (Galilean addition). The boost's is the turn's at s ↦ is.
- Each keeps one heat, ds/(1 + κs²): the turn's angle, the boost's rapidity, the stride's plain ds. Only the turn's has
  a total; it is π. The boost's and the stride's diverge, so neither has an invariant probability, a Cauchy of its own
  or a median: the Cauchy and π both belong to the one compact kind.
- The turn has a corner where its two shares are equal, inside the read, and its horizon at s = ∞. The boost has no
  such corner; its exchange s ↦ −s (k ↦ 1/k) fixes rest, and its fixed point under composition is the light cone,
  s = ±1, which no boost reaches or leaves. The arrangement reverses: for the turn the corner is in the middle and the
  horizon at the end; for the boost the corner is rest and the horizon is the speed of light.
- Both curved kinds have the same rational lattice from a half-slope (all 7,121 rational points of the hyperbola to
  denominator 2,000, all 2,556 of the circle in PYT): the Pythagorean triples read as a sum or a difference.
- The turn closes only at the quarter turns (PYT); no rational boost closes at all; the stride never returns. So
  "where it stops" is π for the turn, and for the boost and the stride there is nothing to complete.
- Only the square keeps the curve: for boosts as for turns, any other power p moves points off by 0.38 to 1.0 in one
  step.
- Small readings compose as the stride, s + a, the first correction κ·sa(s + a): turns and boosts depart from Galilean
  addition in opposite directions.
