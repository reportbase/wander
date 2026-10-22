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
