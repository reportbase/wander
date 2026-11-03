# EPI: epicycles, and the Cauchy drawing the same shape

*3 November 2026, SPN R633.*

*Tom: "It is interesting that it uses circles to draw the shapes pertibations, I wonder if cauchy here could do the same
thing". Claude read "it" as the Fourier epicycles (draw's `gallery/epicycles.html`: a closed shape as circles on circles,
circle k turning k times a lap) and answered two ways: the circle's Cauchy (the wrapped Cauchy, the Poisson kernel) shrinks
circle k by r^|k| and mixes none, so it draws the same shape with the fine circles faded; and a standpoint moved off the
centre turns each circle unevenly, the Takenaka–Malmquist basis, whose terms can be aimed at where the detail is. Tom:
"Merge pr and start the epi cycle test".*

*Numerical, double precision, 4,096 samples of the outline (FFT). No random numbers. Scripts in `runs/epi/`. Nothing is run
before this plan is committed.*

## Known beforehand

- **Epicycles are the Fourier series of the outline** z(t) = Σ c_k e^{ikt}, each term a circle of radius |c_k| turning k
  times a lap (Hipparchus and Ptolemy for the picture, Fourier for the series; draw's epicycles page draws it).
- **The Poisson kernel is the wrapped Cauchy** (CIW, `plans/ciw-plan.md`; SPN R384) and its Fourier coefficients are r^|k|,
  r = e^{−γ}: convolving with it is Abel–Poisson summation, the harmonic extension to radius r. The papers already read the
  Cauchy's height as a built-in level of detail, mode k kept while kγ < 1 (ADR, `plans/adr-plan.md`; DYH run 2).
- **Takenaka–Malmquist systems** (Takenaka 1925, Malmquist 1926): B_n(z) = √(1 − |a_n|²)/(1 − ā_n z) · ∏_{j<n} (z − a_j)/(1 − ā_j z),
  orthonormal in H² of the disc, a_n = 0 for all n giving 1, z, z², …, the Fourier basis. Their building block is the Szegő
  kernel 1/(1 − ā z), a Cauchy kernel; |e_a|² on the circle is the Poisson kernel at a, the wrapped Cauchy with its place at
  a/|a| and its height −ln|a|.
- **Adaptive Fourier decomposition** (Qian and Wang 2011; Qian 2010): choose each a_n greedily to take the most energy of
  what is left, |⟨g_n, e_a⟩|² = (1 − |a|²)|g_n(a)|², then divide the remainder by the Blaschke factor. It is reported to
  converge faster than Fourier on signals with local features. From memory; not read in full here.
- **draw.** `papers/tb_spectral.md` §18 uses the Cayley/Blaschke map to make the Fourier modes algebraic; no term is aimed.
  No lab in draw's `labs.html` tests aimed rational terms.

What is not known beforehand in this corpus: whether aimed Cauchy terms draw *these* shapes (a dent, two dents, a broad
shape) in fewer terms than the best Fourier circles, and whether the places they pick are where the detail is.

## Set-up

- An outline z(θ) = r(θ)·e^{iθ}, ln r = f(θ) (a₀ = 0; the size is not drawn and not read), sampled at θ_j = 2πj/4096.
- Its epicycles c_k by FFT. Split z = z₊ + z₋, z₊ the k ≥ 0 terms (H²), z₋ the k < 0 terms, conj(z₋) in H² after one shift.
- **Fourier, best n terms:** the n largest |c_k| over all k (the fairest Fourier: any n circles, not the first n).
- **Cauchy, aimed n terms (AFD):** on each part, greedy as above; at each step the part with the larger gain takes the term.
  The best a is found over a grid (|a| = 1 − 10^{−x}, x from 0 to log₁₀(1/0.006) in 60 steps, 4,096 angles, the values on a
  ring of radius ρ by one FFT of c_k ρ^k), then refined by Nelder–Mead; 1 − |a| ≥ 0.006 (four samples), so the kernel is
  resolved. a = 0 is allowed (a Fourier circle). The remainder is divided by (z − a)/(1 − ā z) on the samples and its
  negative frequencies (which should be zero) are measured and dropped.
- Error: relative L2, ‖z − approx‖/‖z − c₀‖, on the samples. Terms counted; a Fourier term is 2 reals and an index, an
  aimed term 4 reals (its coefficient and its a), both reported.
- Shapes:
  - **S1, one dent:** f = −0.25·Σ_m exp(−((θ − θ₀ + 2πm)/w)²/2), θ₀ = 1, w = 0.05.
  - **S2, two dents:** the same at θ₀ = 1 and θ₀ = 1 + 2.5, w = 0.05 each.
  - **S3, broad:** f = 0.10·cos 2θ + 0.05·sin 3θ.
  - **S4, one pole, exactly:** z₊(ζ) = ζ + 0.3/(1 − ā ζ) with a = 0.8·e^{i}, z₋ = 0 (its H² part has one pole, at 1/ā
    outside the disc).
- The mean c₀ is given to both methods free; terms are counted beyond it.

## Predictions

- **E1 (identity).** Convolving the outline with the wrapped Cauchy of height γ (by direct sum over the samples, not by FFT)
  equals scaling each epicycle by e^{−γ|k|}, to 10⁻¹² relative, at γ = 0.05, 0.2, 1, on S1. And the wrapped Gaussian with
  the same half-width does not: its shrinks' ratio from k to k + 1 is not constant (it varies by more than 10% over k = 1…20),
  where the Cauchy's is e^{−γ} at every k to 10⁻¹².
- **E2 (one pole).** On S4 the aimed terms reach 10⁻⁴ in at most 6 terms; best-n Fourier needs 38 or more (the tail
  0.3·|a|^n/√(1 − |a|²) < 10⁻⁴·‖z − c₀‖ gives n ≈ 38).
- **E3 (one dent).** On S1, to reach 10⁻³ the aimed terms need at most half as many terms as best-n Fourier.
- **E4 (broad control).** On S3 the aimed terms need no fewer than Fourier's count less one to reach 10⁻³ (no real gain
  where nothing is local).
- **E5 (aimed at the dent).** On S1, of the first ten aimed terms with |a| > 0.5, at least eight have arg a within 0.3 of
  θ₀ (or of −θ₀ for terms in the conj(z₋) part); and the median 1 − |a| over terms 6–10 is smaller than over terms 2–5 (the
  standpoint steps toward the dent as the detail gets finer).
- **E6 (two dents).** On S2, of the terms with |a| > 0.5 among the first twenty, each dent's place gets at least 30%.

Kill: any prediction failing as stated. A killed run stays recorded; a fix is a new run with its own predictions.

## Runs

### Run 1 (3 Nov; `runs/epi/epi.py`, output `runs/epi/epi-run1.txt`)

- **E1 not killed.** The direct sum with the wrapped Cauchy equals each circle scaled by e^{−γ|k|} to 1.4·10⁻¹⁴ (γ = 0.05),
  1.2·10⁻¹⁵ (0.2, 1). The Cauchy's shrink ratio is e^{−γ} at every k to 10⁻¹⁶; the wrapped Gaussian's varies by 6.7,
  2,000 and 3·10¹⁶ over k = 1…20.
- **E2 killed.** On S4 the aimed terms reached 10⁻² in 11 terms and never 10⁻³ in 12; Fourier needed 37 terms for 10⁻⁴.
- **E3 not killed.** On S1, 24 aimed terms against 85 Fourier to 10⁻³ (96 reals against 170); 12 against 40 to 10⁻²,
  37 against 111 to 10⁻⁴.
- **E4 not killed.** On S3, 24 aimed against 10 Fourier to 10⁻³.
- **E5 killed.** 5 of the first 10 terms with |a| > 0.5 within 0.3 of θ₀. The median 1 − |a| fell from 0.42 (terms 2–5)
  to 0.37 (6–10).
- **E6 killed.** 4 and 3 of 19 at the two dents.
- Two dents: 13 aimed against 42 Fourier to 10⁻², 34 against 84 to 10⁻³, 58 against 108 to 10⁻⁴. No aimed run reached
  10⁻⁶ within its cap. The remainders' negative frequencies leaked at most 6.5·10⁻¹⁵.

**Killed by my set-up.** Qian's decomposition takes a₁ = 0 first: the constant, then the remainder divided by z. I
counted a term's worth only by its gain, |g(a)|²(1 − |a|²). With the mean given free, a = 0 gains nothing, so it was never
taken, and its real value is the division it makes possible. Without that shift, the outline's own circle (the e^{iθ}
term, most of every shape) can only be reached through off-centre kernels. g(a) = a has gain (1 − |a|²)|a|², which is
largest at |a| = 1/√2, and the greedy spent its first terms there (0.707, 0.708, 0.718 on S1, S2, S3), at the place
opposite the detail, chasing the circle.

Post hoc, seen only after the run: the conj(z₋) part had no such circle to chase, and its picks were at the dent from the
start (S1: |a| 0.957, 0.979, 0.926, 0.971 at arg 0.93–1.13; S2 likewise at both dents). E3 held despite the waste.

### Run 2, predictions (written before it runs)

The same script and shapes, with one change: each part takes a₁ = 0 first (Qian's first step, its coefficient the part's
constant, zero here), and that shift counts as a term. Thresholds as before.

- **E2′.** On S4 the aimed terms reach 10⁻⁴ in at most 6 terms (the shift, the circle, the pole, and room for the greedy's
  inexact a); Fourier 37 (run 1).
- **E3′.** On S1, aimed ≤ half of Fourier's 85 to 10⁻³.
- **E4′.** On S3, aimed ≥ Fourier's count less one to 10⁻³ (no gain where nothing is local).
- **E5′.** On S1, of the first ten aimed terms with |a| > 0.5, at least eight within 0.3 of θ₀; the median 1 − |a| over
  terms 6–10 smaller than over terms 2–5.
- **E6′.** On S2, of the terms with |a| > 0.5 among the first twenty, each dent gets at least 30%.

### Run 2 (3 Nov; `python3 runs/epi/epi.py 2`, output `runs/epi/epi-run2.txt`)

- **E1** is unchanged (the same check, 1.4·10⁻¹⁴).
- **E2′ killed.** On S4 the aimed terms reached 10⁻² in 8 and 10⁻³ in 10, but not 10⁻⁴ within the cap of 12; Fourier needs
  37. The greedy never took the pole. It alternated between 0.869·e^{i·1.000} and 0.225 at the opposite place, and the
  pole is at 0.8·e^{i}. My prediction assumed that taking the most energy finds the pole. It does not: the energy's maximum
  for 1 + 0.3ā/(1 − āζ) lies beyond the pole, and the greedy closes the gap only slowly. Killed by my reasoning; the place
  (arg 1.000) was found exactly.
- **E3′ not killed.** On S1, 11 aimed terms against 85 Fourier to 10⁻³ (44 reals against 170). The rest:
  - 5 against 40 to 10⁻²;
  - 18 against 111 to 10⁻⁴;
  - 45 against 200 to 10⁻⁶.
- **E4′ not killed.** On S3, 19 aimed against 10 Fourier to 10⁻³. Where nothing is local, the even circles win.
- **E5′ not killed.** All 10 of the first ten with |a| > 0.5 lie within 0.3 of θ₀. Their places were 0.91–1.13, against
  the dent's width of 0.05. The median 1 − |a| fell from 0.52 (terms 2–5) to 0.041 (terms 6–10). Terms 2–5 include
  the second shift (|a| = 0), which raises that median; the terms after it lie at 1 − |a| = 0.03–0.06, and that is the
  reader stepping toward the dent.
- **E6′ not killed.** Of the 16 terms with |a| > 0.5 among the first twenty, 8 lie at each dent. Two dents: 7 aimed
  against 42 Fourier to 10⁻², 22 against 84 to 10⁻³, 39 against 108 to 10⁻⁴.

## What it comes to

- **The Cauchy draws with the same circles.** Its blur (the Poisson kernel, the wrapped Cauchy) leaves every epicycle
  where it is and shrinks circle k by e^{−γ|k|}: exactly, and as no other blur tried does. The reader's height is the
  level of detail.
- **Aimed Cauchy terms draw local detail with far fewer terms.** Each term is a standpoint stepped off the centre toward a
  place, its Szegő kernel the wrapped Cauchy there. On a dent the aimed terms took a seventh to an eighth as many terms as
  the best Fourier circles, and a quarter as many reals. Their standpoints went to the dent (within the dent's own width of
  it) and stepped nearer the outline as the detail got finer: 1 − |a| from about 0.05 to 0.02. Two dents split them evenly.
- **Where nothing is local, the even circles win.** The broad shape needed twice the terms and four times the reals. The
  reader at the centre is the right one for a shape with no place to step toward: Corollary 6.1's focus has nothing to
  follow.
- **The greedy finds places, not exact poles.** On the one-pole shape it found the pole's direction exactly, but took the
  energy's maximum, not the pole, and converged slowly.
- Classical throughout: Abel–Poisson summation, Takenaka–Malmquist, Qian's adaptive Fourier decomposition. The reading is
  ours: the even circles are one standpoint at the centre, and the aimed terms are standpoints moved toward the detail, the
  focus as the corner, applied to drawing a shape.

### After the runs: the demo and the papers (3 Nov, R634)

`epicycles.html` redoes the arithmetic at 2,048 samples (1 − |a| ≥ 0.012), with up to 60 aimed terms. The numbers move
a little: the dent takes 13 aimed terms to 10⁻³ against 85 circles. The two dents take 22 against 84 and the broad shape
19 against 10, and the blur matches its direct sum to 3·10⁻¹⁴. Seen there after the runs, and not a test: with no cap at
12, the one-pole shape reaches 10⁻⁴ in 13 aimed terms against 37 circles. The greedy still never takes the pole itself
(|a| 0.869 against 0.8). Its error falls below run 2's cap shortly after. E2′ stays killed as stated.

Into the papers: *Reads and Writes* §6, "Drawing a shape: the circles, a height, a step toward the detail"; essay 10 §3,
"A third kernel: the Cauchy's own"; a paragraph in essay 4 §13. The references (Takenaka 1925, Malmquist 1926, Qian and
Wang 2011) are from memory and are to be checked.
