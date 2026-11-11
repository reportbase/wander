# STT: Student's t between the Cauchy and the Gaussian

11 Nov 2026. SPN R832. Tom: "lets focus on the equations of observation and how they overlap. interesting that e shows
up in gaussian."; "is there any other equations that deserve to be on this list?"; "yes" (to adding Student's t and the
law-versus-chart distinction to *Reads and Writes* §9, after a short exact check).

## The question

Student's t with ν degrees of freedom is a standard Gaussian amount Z divided by √(χ²_ν/ν), the root mean square of ν
further independent Gaussian amounts W₁ … W_ν. At ν = 1 it is the Cauchy, as ν → ∞ the Gaussian. Where do π and e sit
along the way, and is t at finite ν a law of directions or of amounts?

In my message to Tom before this plan I offered a reading: "divisor unknown gives the reader's law, divisor fully
known gives the writer's", matching knowing V by degrees (R598). It was marked unchecked. It is tested here as S6.

## Known beforehand

- Classical: t_ν's density Γ((ν+1)/2)/(√(νπ)·Γ(ν/2)) · (1 + t²/ν)^(−(ν+1)/2) (Gosset 1908; Fisher 1925).
- Classical: a uniform direction on the sphere in n dimensions, its first coordinate times √n, tends to the standard
  Gaussian (Maxwell; Borel 1914; called Poincaré's lemma).
- The corpus: WDG run 2 (n other parties, the readings the n-dimensional Cauchy); *Reads and Writes* §9 (the Gaussian a
  turn times a payload, the division taking the e and leaving the π; R800, R816); GRS run 3 (ℚ + ℚπ for even k,
  ℚ + ℚ/π for odd); `cauchy-map.html`'s hemisphere constants.
- (1 + x/n)ⁿ → eˣ (Bernoulli), in §9 as the writer's limit.

## Set-up

mpmath at 50 digits, and exact rationals where the claim is rational (`runs/stt/stt.py`). A seeded sample only for S3.

## Predictions (committed before the run; derived on paper first, the run checks them)

- **S1. ν = 1 is the standard Cauchy.** The density at ν = 1 equals 1/(π(1 + t²)) at t = 0, ½, 1, 3, 10 to 10⁻⁴⁰.
  Kill: any differs.
- **S2. No e at any finite ν.** The density is a constant times a rational function of t (even ν + 1) or its square
  root (odd ν + 1): for ν = 1, 3, 5 the ratio f(t)/f(0) at rational t is an exact rational, (1 + t²/ν)^(−(ν+1)/2);
  for ν = 2, 4 its square is. The e arrives only as Bernoulli's limit: ln[f_ν(t)/f_ν(0)] → −t²/2, the gap falling as
  1/ν (gap·ν → t⁴/4 − t²/2 at t = 1, 2). Kill: a gap not falling as 1/ν, or a non-rational ratio.
- **S3. t is a direction, in ν + 1 dimensions.** t/√ν = Z/|W| depends only on the direction of (Z, W₁ … W_ν): scaling
  all ν + 1 amounts by k = 10⁻³, 7, 10³ moves no t (exact in a seeded sample of 1,000, to rounding). The direction is
  uniform on the sphere, so with χ the direction's angle off the Z axis (the writer's), t = √ν·cot χ and
  P(|t| ≤ √ν) = P(|Z| ≤ |W|) is ½ at ν = 1 (the corner), and by quadrature equals the sphere's cap share
  ∫ sin^(ν−1) over [π/4, 3π/4] / ∫ over [0, π] for ν = 1 … 6. Kill: a t moved by k, or the shares differing by 10⁻³⁰.
- **S4. π comes and goes with the parity of ν.** The normalising constant is rational/π times √ν-type surds for odd ν
  (ν = 1: 1/π; ν = 3: 2/(π√3); ν = 5: 8/(3π√5)) and has no π for even ν (ν = 2: 1/(2√2); ν = 4: 3/8). Kill: any of the
  five differs at 10⁻⁴⁰.
- **S5. The Gaussian is approached at rate 1/ν.** sup over t of |f_ν(t) − φ(t)| times ν tends to
  max |t⁴ − 2t² − 1|·φ(t)/4, attained at t² = 3 − √6, about 0.1362; at ν = 10, 100, 1,000 the product is within 30%,
  5% and 1% of it. Kill: outside those bands.
- **S6. (The reading offered to Tom, expected killed.)** "The dial is how well the divisor is known: unknown gives the
  reader's law, known the writer's." If S3 holds, t is unmoved by scaling at every ν and is a function of direction
  alone, so nothing is written at any ν and V is known at none; what ν counts is the number of other parties the
  direction is taken among. The reading stands only if some finite-ν t moves under scaling. Kill: S3 not killed.

## Runs

### Run 1 (11 Nov 2026; `python3 runs/stt/stt.py`, output `runs/stt/stt-run1.txt`)

- S1 not killed: ν = 1 equals 1/(π(1 + t²)) at all five t, to 10⁻⁵⁰.
- S2 not killed: f(t)/f(0) exact rationals for ν = 1, 3, 5 (4/5, 144/169, 8000/9261 at t = ½ …), its square for
  ν = 2, 4; the gap from −t²/2, times ν, −0.2421, −0.2492, −0.2499, −0.25000 at t = 1 (limit −¼) and 1.494, 1.935,
  1.993, 1.9993 at t = 2 (limit 2).
- S3 not killed: 1,000 seeded draws scaled by 10⁻³, 7, 10³ move t by at most 4·10⁻¹⁶ (rounding);
  P(|t| ≤ √ν) = the cap share to 10⁻⁵⁰ for ν = 1 … 6: ½, 0.70711 (1/√2), 0.81831 (½ + 1/π), 0.88388, 0.92441, 0.95017.
- S4 not killed: f(0) = 1/π, 1/(2√2), 2/(π√3), 3/8, 8/(3π√5) for ν = 1 … 5, to 10⁻⁵⁰.
- S5 not killed: the limit 0.13617; sup|f − φ|·ν = 0.13174, 0.13572, 0.13613 at ν = 10, 100, 1,000 (3.3%, 0.33%,
  0.034% under).
- S6 killed, as expected: t is unmoved by scaling at every ν.

### Reading

The reading I offered Tom before the plan (ν as how well the divisor is known, V by degrees) is wrong. Student's t
is the law of one direction among ν + 1 equal parties, read as one share against the others' length; nothing is
written at any ν. What ν counts is parties. The e is absent at every finite ν and arrives as Bernoulli's limit; the
π is present only for odd ν. The Gaussian as the limit of such a direction is classical (Maxwell; Borel 1914). The
closed forms 1/√2 and ½ + 1/π in S3 were not predicted; they were noticed in the output.
