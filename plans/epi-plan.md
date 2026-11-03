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

(none yet)
