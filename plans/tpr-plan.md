# TPR: 2/π revisited, as address and payload

*22 October 2026. A revisit of TPI (`plans/tpi-plan.md`, `plans/tpi-report.md`) in the vocabulary OFS has settled since
15 October: the Cauchy is the uniform turn's (SPN R389); an arrival is an address (a direction laid by the turn) times a
payload (what arrives along it); an address is not a payload (R393); order (the median) is the address's, sums (the
mean) the payload's (Theorem 6(c)); the two sweeps of one turn, inscribed (rate 2, the chart s = v/h, unbounded) and
central (rate 1, the point ½(h² − v², 2hv), bounded) (OFS §4, R284, R332). Predictions written before the script
(`runs/tpr/tpr.py`) exists and before the catalogue is sorted (`runs/tpr/sorted.md`). Work only here and in `runs/tpr/`.*

## Known beforehand

- **TPI** (runs 1–4): 65 occurrences of 2/π; 55 from a turn taken evenly and read as a shadow or a share (43 open, 12
  hidden: an equal-spread normal pair or a Haar measure), 7 the circle held as a shape (route S), 1 a pole (C8), 2 not
  traced (C2, C26). Four forms: (i) mean shadow, (ii) share (2/π)θ, (iii) sin θ/θ at the quarter turn, (iv) a weight's
  normaliser. P4 (not killed): concentrating the turn (von Mises κ = ½, 1, 2) moves the mean shadow off 2/π (0.649,
  0.682, 0.763). Runs 3–4: the marks (V not known, a sweep made) sort derivations, not uses.
- **TPI's naming.** TPI, the report and `physics.md` §2.2 call the 2/π "the inner reading" and, later, the address
  reader's (OFS §3.4: "the inscribed is the projection over the turn, 2/π"); the report's §5 offers "to take a mean" as
  its purpose (Claude's candidate, R254).
- **OFS §4** ("What each sweep reads"): the central sweep's point ½(h² − v², 2hv) is bounded, "so every average over a
  uniform turn exists: cos 2θ averages 0 and sin 2θ averages 2/π". So the same 2/π is already in OFS as the mean of the
  payload point's height over its radius, beside §3.4's mean projection of the inscribed bar.
- **OFS Theorem 6(c), (e)** and §11.2 question 2 (`runs/ofs/paths.py`): the circle, the line h + v = 1 and the square's
  edges, each swept uniformly along its own length, are reciprocal-symmetric, agree at home, the corner and the horizon,
  have no mean of v/h; only the circle's share carries π. The median commutes with every increasing map, the mean only
  with affine ones.
- **THL P2**: A's ray reading s meets the Thales circle at distance h from A (and v from B): the amount along the
  inscribed reader's ray to the point it addresses is h = cos θ.

## The reading to test

Every turn-derived 2/π in the catalogue is a **mean over the uniformly laid addresses of a bounded amount** (the shadow
cos θ, which is also the length along the inscribed ray to its point, THL P2; the central point's height sin 2θ; a
chord; a first Fourier coefficient), or a **share**, the turn's own measure of a set of addresses, (2/π)·θ. The first is
a payload operation (a mean) taken over addresses: it needs the turn to be uniform, and moves under any other fair
weight. The second is the address's: at the corner it is ½ under every fair weight; elsewhere it is the uniform turn's.
A third kind, a **normaliser by a square** (∫cos²θ = π/2 and its like), needs only the exchange and the turn's total
length: cos²θ + sin²θ = 1 and the exchange give E[cos²θ] = ½ under every fair weight. So "the inner reading 2/π" is not
the address reader's holding (the address reader has no mean and receives no amount); it is a mean of amounts along the
inscribed reader's addresses, taken where the turn is uniform, i.e. a writer's or payload reader's number about the
inscribed vantage. The address reader's own number on the same turn is the median of cos θ, 1/√2, the corner.

Fair weight here: a weight w(θ) on the quadrant, reciprocal-symmetric (w(θ) = w(π/2 − θ)), of total π/2 (the same total
as the uniform turn), extended to the whole turn with period π/2 where an entry needs the whole turn.

## Predictions

Some closed forms below were worked by hand while writing (said so in each); the script is their first check. Nothing
else here has been computed.

- **P1 (the three paths' projection means; exact).** Each path swept uniformly along its own length, θ the direction
  of the point from home:
  - E[cos θ] (the shadow, = the inscribed ray's amount): circle 2/π; line (√2/2)·ln(1 + √2) = 0.62323; square
    (ln(1 + √2) + √2 − 1)/2 = 0.64779 (both by hand).
  - E[sin 2θ] (the central point's height over its radius): circle 2/π; line π/2 − 1 = 0.57080; square ln 2 = 0.69315
    (by hand).
  - E[cos²θ] = ½ and E[cos 2θ] = 0 on all three.
  - The median of cos θ is 1/√2 on all three.

  *Killed* if any computed value differs from the stated one by more than 10⁻³⁰, or if the line or the square gives
  2/π (within 10⁻³) for either mean.
- **P2 (median survives, mean does not; exact, not computed).** On the family w_a ∝ sin^a(2θ), a ∈ {−0.9, −0.5, 0, 0.5,
  1, 2, 4} (all reciprocal-symmetric, total π/2):
  - the medians of cos θ, sin²θ, tan θ/(1 + tan θ) and of the share of the quarter turn, θ/(π/2), are 1/√2, ½, ½, ½ at
    every a;
  - E[cos²θ] = ½ at every a;
  - E[cos θ] and E[sin 2θ] are strictly increasing in a and equal 2/π only at a = 0.

  *Killed* if a median differs from its corner value by more than 10⁻³⁰, E[cos²θ] from ½ by more than 10⁻³⁰, either
  mean is not strictly increasing over the seven a, or either mean is within 10⁻⁶ of 2/π at some a ≠ 0.
- **P3 (2/π alone does not identify the uniform turn; exact, not computed).** There is a fair, non-uniform weight with
  E[cos θ] = 2/π exactly: the mixture (1 − λ)·(the line's weight) + λ·w₂, with λ found in (0, 1). Its law of cos θ is not
  the uniform turn's: its E[cos 4θ] differs from the uniform turn's 0 by more than 10⁻³. *Killed* if no λ in (0, 1)
  solves it, or if |E[cos 4θ]| ≤ 10⁻³ there.
- **P4 (on the whole turn, 2/π on every axis is the axes' uniformity; exact).** With θ on [0, 2π) under a weight w
  of mean 1, the mean shadow on the axis at φ, E|cos(θ − φ)|:
  - w = 1 + ½·cos θ (directions uneven, axes even): 2/π at φ = 0, 0.3, 1 and π/2;
  - w = 1 + ½·cos 2θ: 2/π + cos 2φ/(3π) (7/(3π) at 0, 5/(3π) at π/2; by hand, from |cos x|'s Fourier series);
  - w = 1 + ½·cos 4θ (reciprocal-symmetric on the quadrant, uneven): 2/π − cos 4φ/(15π) (by hand).

  So 2/π on every axis holds exactly when the weight's even harmonics vanish: when the facing 2θ, the central sweep's
  angle, is uniform, not the direction θ. *Killed* if any value differs from the stated one by more than 10⁻³⁰.
- **P5 (the catalogue sorted by the split; a count, one of the two allowed).** Each of the 65 is put, from its
  derivation note in `plans/tpi/catalogue.md` (and `tpi.py`'s computation), in one class, recorded with a line in
  `runs/tpr/sorted.md`:
  - **M**, a mean of a bounded amount over the turn's uniformly laid addresses, a first power of the projection (|cos|,
    |sin|, a chord, a first Fourier coefficient, sin θ/θ at the quarter turn as the mean of cos, an elliptic mean),
    including ratios with such a mean in them: needs the turn uniform;
  - **L**, the turn's total length only, or a normaliser by a square whose mean (½) the exchange fixes (Flamant,
    Sato–Tate, Γ(½)² as the pair's full turn, a half residue): needs no uniformity;
  - **B**, a share: the turn's measure of a set of addresses, (2/π)·θ, including sign-agreement probabilities and a
    linewidth as a share of the period: the address's (½ at the corner under every fair weight);
  - **S**, the circle held as a shape (TPI's route S);
  - **O**, other: a pole, a dimension, a convention, not traced.

  Predicted counts: M 32 ± 5, L 10 ± 3, B 12 ± 3, S 7 exactly, O 5 ± 1. *Killed* if any count falls outside.
- **P6 (the classes predict which constants survive a fair weight; exact, not computed).** Representatives recomputed
  under three fair non-uniform weights (the line's, the square's, w₂):
  - M moves, by more than 10⁻⁶ under each weight: the mean |sin| (K5, C14, C34), the mean |cos| (K2, K6, C20, C33), the
    mean half-angle chord over a heading even on [0, π] (C15, C43, K12), (2/π)·K(0.6) as a mean (C9), the saturation
    describing function at T/A = ½ (C35), the square wave's coefficient ∫sin/∫sin² (C3);
  - L stays, to 10⁻⁴⁰: Flamant's 1/∫cos² over the half turn (K15), Sato–Tate's 1/∫sin² over [0, π] (K18), Irwin's
    1/∫dφ over the quarter turn (C28);
  - B at the corner stays, to 10⁻⁴⁰: the half-Cauchy at s = 1 (K1), the arcsine law at t = ½ (K4), sign disagreement
    between vectors a quarter turn apart (K7 at ρ = 0, C21 at θ = π/2), Kendall's quadrant at ρ = 0 (C13); B off the
    corner moves, by more than 10⁻⁶: s = 3, t = 0.3, the wedge at 0.9 and 1.1 rad, the quadrant at ρ = ½.

  *Killed* if any M or off-corner B value stays within 10⁻⁶, or any L or corner B value moves by more than 10⁻⁴⁰.

## What would and would not be shown

Not killed, the catalogue's 2/π would split by the address and payload: the share's 2/π (a quarter turn's measure,
order-side, its corner value the exchange's) and the mean's 2/π (a sum over addresses of a bounded amount, which needs
the uniform turn), with a third kind whose 2/π is only the turn's length. It would correct TPI's "the inner reading 2/π
is the address reader's" to "a mean of amounts taken over the address reader's uniformly laid addresses". It would not
say who reads any of the 65.

## Runs

### Run 1 (22 October; `python3 runs/tpr/tpr.py | tee runs/tpr/tpr-run1.txt`, 4½ minutes)

The first launch crashed before any P2 value: for a < 0, rounding left sin 2θ a hair below 0 at the quadrant's end and
the power went complex. `abs()` was put round it (commented in the script) and the run made again from the start; P1's
output was the same both times.

- **P1 not killed.** All six stated means to 20+ digits (circle 2/π twice; line E[cos θ] 0.623225, E[sin 2θ] π/2 − 1
  = 0.570796; square 0.647794 and ln 2 = 0.693147); E[cos²θ] = ½ and E[cos 2θ] = 0 (≤ 5·10⁻⁵²) and the median of cos θ
  1/√2 on all three. The line and the square fall on opposite sides of 2/π for E[cos θ], and E[sin 2θ] likewise.
- **P2 killed, by my set-up.** For a ≥ 0 every clause holds (medians at the corner and E[cos²θ] − ½ ≤ 7·10⁻⁵²; both
  means strictly increasing over all seven a: E[cos θ] 0.5303, 0.5991, 2/π, 0.6555, 2/3, 0.6791, 0.6898 and E[sin 2θ]
  0.1378, 0.4569, 2/π, 0.7295, π/4, 0.8488, 0.9054; neither at 2/π but at a = 0). At a = −0.9 the median was off by
  3.8·10⁻⁶ and E[cos²θ] by 3.6·10⁻⁷, at a = −0.5 by 2·10⁻²⁶ and 7·10⁻²⁷, against 10⁻³⁰: the weight (sin 2θ)^a is
  singular at both ends, and at the end π/2 the quadrature's nodes crowd within the rounding of π/2 itself, so sin 2θ
  is computed with a large relative error there (TPI run 1's kill was the same kind). Both are identities for a
  reciprocal-symmetric weight; the numbers say the quadrature, not the claim, failed.
- **P3 not killed.** λ = 0.23989 of w₂ mixed into the line's weight gives E[cos θ] = 2/π exactly; there E[cos 4θ] =
  −0.01232 (uniform 0) and E[sin 2θ] = 0.637493 (uniform 0.636620). 2/π alone does not identify the uniform turn.
- **P4 not killed.** With w = 1 + ½cos θ the mean shadow is 2/π on every axis; with 1 + ½cos 2θ, 7/(3π) = 0.742723
  at φ = 0 and 5/(3π) at π/2; with 1 + ½cos 4θ, 2/π − cos 4φ/(15π) (0.615399 at 0 and π/2, 0.650491 at 1).
- **P5 not killed** (`runs/tpr/sorted.md`, sorted by me, not blind): M 34, L 8, B 10, S 7, O 6 (O at its edge; C6, the
  Lebesgue constant's (2/π) per e-fold, is a log climb, a mean of cot over even angles, which I put in O).
- **P6 not killed.** Every M representative moves under the line's, the square's and w₂'s weights (the mean |sin| and
  |cos| by −0.0134, +0.0112, +0.0424; the half-angle chord −0.0032, +0.0027, +0.0101; (2/π)K(0.6) +0.0015, −0.0015,
  −0.0052; the saturation function and the square-wave coefficient likewise); every L representative (Flamant, Sato–Tate,
  Irwin) and every B value at the corner (K1 at s = 1, K4 at t = ½, Van Vleck and Bell a quarter turn apart, Kendall at
  ρ = 0) stays to ≤ 1.3·10⁻⁵¹; every B value off the corner moves (by 0.015 to 0.28).

**Reading (after the run; not ruled).** The 2/π of the 65 is three things. (1) **M, 34**: the mean over the turn's
uniformly laid addresses of a bounded amount, the shadow cos θ (= the length along the inscribed ray to the point it
addresses, THL P2) or the central point's height sin 2θ. It is a payload-side operation (a sum) taken over addresses;
it changes under every other fair weight, while the median of the same amount stays at the corner, 1/√2. So "the
inner reading 2/π" is not something the address reader holds: the address reader has the share and the median, never
the mean. It is a writer's or payload reader's number about the inscribed vantage, true only if the turn is uniform.
(2) **B, 10**: the share (2/π)·θ, the turn's own measure of a set of addresses; the address's quantity; its corner
value ½ is the exchange's and survives every fair weight, its other values are the uniform turn's. (3) **L, 8**: the
turn's length alone (with at most a square, whose mean ½ the exchange fixes); it survives every fair weight, so it does
not mark uniformity at all. P3 and P4 bound the fingerprint: a single 2/π never identifies the uniform turn (a fair
non-uniform weight hits it), and 2/π on every axis of the whole turn holds exactly when the facing 2θ is uniform.

### Run 2: P2′ (written after run 1, before `runs/tpr/tpr2.py` exists)

- **P2′.** On the same family, computed on [0, π/4] only, the upper half folded onto it by the exchange (θ ↦ π/2 − θ, so
  both singular ends sit at an exactly represented 0): W(π/4) = ½ and E[cos²θ] = ½ to 10⁻³⁰ at a = −0.9 and −0.5, and
  E[cos θ], E[sin 2θ] there agree with run 1's to 10⁻⁵ (they were not the failing clauses). *Killed* if any is not.

### Run 2 (22 October; `python3 runs/tpr/tpr2.py | tee runs/tpr/tpr-run2.txt`, seconds)

- **P2′ not killed.** Folded onto [0, π/4]: at a = −0.9, W(π/4) − ½ and E[cos²θ] − ½ = −7·10⁻⁵²; at a = −0.5, 0. The
  means agree with run 1's to 4·10⁻⁷ (a = −0.9: E[cos θ] 0.5302697, E[sin 2θ] 0.1377983) and 10⁻¹⁵ (a = −0.5). The
  check is close to an identity (the fold uses the exchange the clauses rest on); it shows that run 1's failure was the
  quadrature at π/2. With P2′, every clause of P2 stands: on this family the median of every monotone amount is the
  corner's and E[cos²θ] = ½, while both bounded means rise strictly with a and meet 2/π only at the uniform turn.

**Earlier statements this bears on** (not edited here; for Tom):
- `plans/tpi-plan.md` l. 10, l. 153; `plans/tpi-report.md` l. 50–51, l. 84; `papers/physics.md` l. 301: "the inner
  reading", read since R328–R329 as the address reader's. By M and P6 it is a mean of amounts over the address reader's
  uniformly laid addresses, not a reading the address reader holds (it has the share and the median, 1/√2, not a mean).
- `plans/tpi-report.md` l. 98 ("The evenness is what gives the value") and `plans/tpi-plan.md` l. 69 (P4's title):
  true of the M and B entries off the corner, false of the 8 L entries (Flamant, Sato–Tate, ARE, Struve twice,
  Kramers–Kronig, Irwin, the Fourier prefactor), whose 2/π is a length or a square's normaliser; P6 checked three of
  them (Flamant, Sato–Tate, Irwin), which survive every fair weight tried, and TPI's P4 tested none.
- `plans/tpi-report.md` l. 16 and `plans/tpi-plan.md` l. 19, 78 ("a fingerprint of the even turn"): by P3 a single 2/π
  does not identify the uniform turn (a fair, non-uniform weight hits it); it fingerprints the uniform turn only with
  more of the law (P4: 2/π on every axis of the whole turn, which is the facing 2θ's uniformity).
- `papers/physics.md` l. 133, 299–301 ("fifty-five come from a turn taken evenly"): of those 55, 8 are L and need no
  evenness, and 10 are shares whose corner value ½ needs only the exchange.
