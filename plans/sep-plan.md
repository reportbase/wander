# SEP: separating overlapping Cauchys, standpoints and amounts

27 Nov 2026; SPN R1274. Tom: "To tease out the payload, you might need to separate multiple overlapping cauchies. We
could test this and make the idea robust. Has any one done this?", then "Yes".

## The case

A sum of Cauchys, f = Σ aₖ·C(x; mₖ, γₖ), each Cauchy one standpoint zₖ = mₖ + iγₖ, each aₖ its amount. Separating them
recovers the standpoints (read geometry) and the amounts (the payload). The Cauchy family's own distance is the
hyperbolic (Poincaré) distance, cosh d = 1 + |z₁ − z₂|²/(2·Im z₁·Im z₂) (FRG: its Fisher metric is half the Poincaré).

Two ways the data can come:
- **Draws** (reads): N directions, each from a uniform turn about one of the standpoints. A real Möbius map g carries a
  draw from C(z) to a draw from C(g(z)) (McCullagh 1996), so carries one separation problem onto another.
- **A spectrum** (amounts): f sampled on a grid with additive noise per channel, as in spectroscopy or a gravity profile
  (since R1240 gravity's density is only Cauchy in form: a mass at depth d is at m + id).

## Known beforehand (not predictions)

Lorentzian peak fitting and deconvolution in spectroscopy; Prony's method, the matrix pencil (Hua and Sarkar 1990),
ESPRIT, filter diagonalization (Mandelshtam and Taylor 1997), Padé, vector fitting, AAA; Cauchy mixtures by EM;
geophysics' depth separation (Spector and Grant 1970); super-resolution limits (Donoho 1992; Candès and
Fernandez-Granda 2014); Möbius equivariance of Cauchy estimation (McCullagh 1996). Cited from memory. Since the
isometries of the half-plane act transitively on pairs at a given distance, S2 implies that in draws the difficulty of
separating two Cauchys depends on their hyperbolic distance alone (and the weights and N): a consequence of symmetry,
checked, not discovered.

## Predictions (committed before the script)

Pairs at hyperbolic distance d ∈ {1.5, 2, 3} with width ratio r = γ₂/γ₁ ∈ {1, 2, 4} (and r = 16 at d = 3), the
geometric mean width √(γ₁γ₂) = 1, weights ½ and ½.

- **S1, the method.** Noiseless, from the phasor Σ aₖ·e^(i·mₖ·t − γₖ·t) at 2K points, Prony's method recovers K = 1–4
  standpoints and amounts to 10⁻⁸.
- **S2, draws are Möbius-equivariant.** N = 2,000 draws, the two-component maximum likelihood fitted from the truth; the
  same draws mapped by a real Möbius map g that is not affine, fitted from g(truth): the fitted weight the same to 10⁻⁴
  and the fitted standpoints g of each other's to 10⁻⁴, in every one of 20 trials.
- **S3, draws on one curve.** 200 trials a case: the median weight error at each d the same across r, within 25% (the
  Monte Carlo scatter), and growing as d falls.
- **S4, a spectrum breaks it.** The same pairs sampled on [−200, 200] at 0.05 with white noise σ = 2·10⁻³ a channel,
  fitted by least squares (amounts free): at d = 1.5 and 2 the median weight error differs across r by more than 1.5×.
  Kill: within 1.2×.
- **S5, the total survives.** In S4 the total amount a₁ + a₂ is recovered at every d and r within 3× of its error for one
  Cauchy alone, while the weight error grows from d = 3 to d = 1.5 more than the total's does.
- **S6, a search.** Whether a resolution limit for Cauchy or Lorentzian mixtures has been stated in the hyperbolic
  distance before (expected: in the Fisher–Rao or Möbius-equivariance literature, at least implicitly).

The reading offered beforehand (not a prediction): the invariance is the read's (draws are directions about standpoints);
a spectrum's channels carry amounts with their own errors, so the write side breaks it.

## Runs

### Run 1 (`runs/sep/sep.py`, output `runs/sep/sep-out.txt`)

S1 not killed (Prony exact to 10⁻⁴⁶ for K = 1–4). S2 not killed (the non-affine Möbius map (x + 1)/(1 − x/2) carries
every fit onto its image: weights to 7·10⁻⁷, standpoints to 5·10⁻⁶). S3 KILLED by my tolerance: the medians across r at
one d agree within 19% and 6% at d = 1.5 and 2 but 31% at d = 3; S2 and the transitivity of the isometries make the
law identical, so the spread is the Monte Carlo scatter of four medians of 200, which my 25% did not allow. The decline
with d held (0.062, 0.029, 0.013). S4 KILLED by its letter: the spectrum's spread across r was 1.46 and 1.30 at d = 1.5
and 2, under the predicted 1.5 and over the kill line 1.2, within reach of the same scatter, so run 1 cannot say whether
the spectrum breaks the invariance. S5 not killed (total amount within 2.2× of one Cauchy's in every case; from d = 3 to
1.5 the weight error ×3.45, the total ×1.02).

## Run 2: exact bounds in place of the scatter (predictions committed before the script)

The Cramér–Rao bound for the weight, computed exactly (no Monte Carlo): for draws, the Fisher matrix per draw by
quadrature (mpmath, 30 digits); for the spectrum, σ²·(JᵀJ)⁻¹ on the same grid. Same cases.
- **S3′.** Draws: the bound on the weight at each d the same across r to 10⁻⁸ relative (the symmetry, now without
  scatter), and decreasing in d.
- **S4′.** Spectrum: the bound at d = 1.5 differs across r by more than 5% (the additive noise not Möbius-invariant).
  Kill: within 5%.
- **S5′.** Spectrum: the bound on the total amount within 3× of one Cauchy's in every case.

### Run 2 (`runs/sep/sep2.py`, output `runs/sep/sep2-out.txt`)

Nothing killed. S3′: the draws' bound on the weight per draw is 3.9206, 1.9061, 0.8767 at d = 1.5, 2, 3, the same
across r = 1, 2, 4 (16) to 10⁻²⁸ relative: in draws, separating two Cauchys depends on their hyperbolic distance alone.
S4′: the spectrum's bound differs across r by 29%, 20% and 22% at d = 1.5, 2, 3 (not monotone in r at d = 1.5): the
additive noise per channel breaks the invariance, by tens of percent, not by orders. S5′: the total amount's bound within
2.0× of one Cauchy's in every case.

### S6, the search (27 Nov, two searches, snippet depth)

Found: McCullagh 1996 (*Ann. Statist.* 24(2), 787–808), the complex parameter m + iγ and Möbius equivariance of Cauchy
estimation; the Cauchy family's Fisher–Rao distance a rescaled Poincaré distance (Nielsen and colleagues; the Cauchy
Voronoi diagrams hyperbolic, *Entropy* 2020); a chapter on the mixture family of two prescribed Cauchys (not read). Not
found: the resolution limit for separating Cauchy components stated in the hyperbolic distance, or the split between
draws, where it holds exactly, and a spectrum, where it does not. S2–S3′ follow from McCullagh's equivariance and the
isometries' transitivity, so expected in effect; not found said.

### Reading (Claude's, not ruled)

In draws (directions from a uniform turn about each standpoint, a read) how hard two Cauchys are to separate is set by
the one number the read's geometry gives them, their hyperbolic distance; widths and gaps in a unit do not enter. In a
spectrum (an amount per channel with its own error, the write side) the same pairs part by up to 29%: the channel's
noise is an amount, and amounts are not unmoved by the turn's maps. Either way the total amount survives where the
split between the two does not (CDW run 2's total mass). The arithmetic is classical; the sorting is ours.

## Run 3: measured data, a ¹H spectrum's multiplets (predictions committed before the data were downloaded)

27 Nov 2026; Tom: "Merge, then 1 and 2". BMRB metabolomics entry bmse000297, ethanol, set01, the 1D ¹H free induction
decay (Bruker), read with nmrglue. Chosen before looking: a J-coupled multiplet is a sum of overlapping Cauchys whose
amounts are known beforehand (first order: the CH₃ triplet 1:2:1, the CH₂ quartet 1:3:3:1, the CH₂ : CH₃ total 2 : 3 by
proton count), equally spaced by one J (about 7.1 Hz, known beforehand). Each line is one standpoint m + iγ. In the
free induction decay each is one pole, e^(i·m·t − γ·t) (essay 2 §9's phasor), so two methods: M1, a least-squares fit of
Lorentzians to the phased spectrum in a window about each multiplet; M2, the matrix pencil (Prony's family) on the
decay itself, shifted to the window and low-passed, poles kept inside the window. Known sources of error, stated now:
second-order roofing (about J/Δν, under 1%), the recycle delay (totals off if relaxation is incomplete), shimming (lines
not quite Lorentzian), the HDO presaturation.

- **N1.** In both multiplets and by both methods the lines are equally spaced, J between 6.9 and 7.3 Hz, the CH₃'s and
  the CH₂'s J agreeing within 0.05 Hz.
- **N2.** The total amount, the payload of each multiplet: CH₂/CH₃ = 2/3 within 5%, by both methods.
- **N3.** The split: each line's share of its multiplet within 10% of 1:2:1 and 1:3:3:1, by both methods.
- **N4 (the reading).** The two methods disagree less on each multiplet's total than on its single lines (largest
  relative disagreement over lines larger than over totals).
- **N5.** The lines of one multiplet share one width within 10% (one height for the standpoints of one group).

Reported, not predicted: each adjacent pair's hyperbolic distance acosh(1 + J²/(2γ²)), and how each line's error stands
against it.

### Run 3 (`runs/sep/sep3.py`, output `runs/sep/sep3-out.txt`)

Data: BMRB bmse000297 (ethanol), nmr/set01/1H, from bmrb.io (BMRB's data are freely available); 400.13 MHz, zg, one
scan, D1 5 s, AQ 3.4 s; `fid` sha256 2d4eb82cc62be0897d0b583625cecf097c2ac7211eeb00b4b1132da3e3e0ad64, `acqus`
7514424ca61b297a9f6d7ba915553fad4592c7606132ad9374cc8e39f478731b; not committed. Read with `python3 -I`.

The first execution was KILLED by my code, four faults found one after another and fixed before any verdict was taken:
the windows (the sample is referenced so the CH₃ triplet sits at 1.06 ppm and the CH₂ quartet at 3.55, not where I
assumed); M1's Lorentzian written with the wrong sign of i; M2's singular vectors conjugated (every frequency shifted;
found on a synthetic decay, which then came back exact); and spinning sidebands at ±15.0 Hz, which both methods modelled,
lying on twice the spacing (2J = 14.17 Hz), so the "sideband" terms took the multiplets' own outer lines. The sidebands
(about 1% of each line) were dropped from both methods and M2 kept only poles narrower than 30 s⁻¹ within 2.5 Hz of a
line, a rule set on a synthetic decay with M1's lines (each line back within 6%) before the real data were run again,
once. The script as committed is that last version.

M1 (Lorentzians fitted to the spectrum), every prediction holds: J = 7.097, 7.081 (CH₃) and 7.093, 7.090, 7.070 Hz
(CH₂), the two groups' mean J 0.004 Hz apart (N1); CH₂/CH₃ = 0.6746, 1.2% over 2/3 (N2); shares 0.2500 : 0.4976 : 0.2524
and 0.1322 : 0.3766 : 0.3683 : 0.1229, every line within 5.8% of 1:2:1 and 1:3:3:1 (N3); widths within 3.2% and 6.2%
(N5); residual 1.3% of the peak. The adjacent lines sit 5.5 apart in hyperbolic distance (J ≈ 7.1 Hz against
γ ≈ 2.8 s⁻¹, a linewidth about 0.9 Hz), well apart, where SEP run 2 puts the split's error small.
M2 (the matrix pencil on the decay, as built) fails: CH₂/CH₃ = 1.13 (N2), the triplet's shares off by up to 31% (N3),
the spacings 7.02–7.27 Hz (N1), widths spread 1.65× (N5); so N1, N2, N3 and N5 are KILLED by their letter ("by both
methods"), by my second method, not by the data: on a real line the pencil finds several poles (a narrow one near
γ ≈ 3 s⁻¹ and broader ones: the lines are not quite single Cauchys, as shimming leaves them), and its rule for
gathering them loses part of the tallest multiplet's amount (CH₃'s total 1,094 against M1's 1,832). N4 not killed in
its letter (single lines disagree by up to 59%, totals by up to 40%), but with M2 failing it says nothing.

Reading (Claude's, not ruled). On measured data the payload came out where the chemistry puts it, from the fit that
treats each line as one Cauchy: the totals to 1.2% and the splits to 6%, the overlap no obstacle at a hyperbolic
distance of 5.5. Where it would bite (a doublet whose lines sit within one or two of each other in that distance) is
untested here. The second route, poles from the decay, needs a model of a real line as more than one pole; that is a
run of its own, not attempted.

## Run 4: channels laid by the turn (27 Nov 2026; SPN R1279; Tom: "1")

Run 2 found draws keep the separation's difficulty a function of the hyperbolic distance alone, and a spectrum with the
same noise in every channel breaks it by 20–29%. I offered to lay the channels evenly in the turn about a reference
standpoint and said the equality should come back. Working it through before any code changed that prediction, and the
predictions below are the changed ones, committed before the script.

The reasoning. In the continuum a spectrum's information is ∫ ∂f ∂f · w(x) dx, with w set by the noise: the same noise
in channels spread with density ρ(x) gives w ∝ 1/ρ; noise that is the paint's own count (a channel's variance its
expected amount) gives w = 1/f. A Möbius map carries each Cauchy onto a Cauchy as a density (f ↦ f/g′), so the
information is unchanged by the map exactly when w transforms the same way. With w = 1/f it does, for every map (that is
the draws' case, binned). With w = 1/ρ it does only for maps with g′(x)·ρ(g(x)) = ρ(x), and no positive ρ on the line
satisfies that for every real Möbius map (they act on the line with no invariant measure). The Cauchy about i satisfies
it for the turns about i, and only those. So:

- T1 (exact): the Cauchy density about i keeps g′(x)·ρ(g(x)) = ρ(x) for turns about i (three turns, to 10⁻²⁵) and fails it
  for a translation and a dilation (by more than 10⁻³ at some x).
- T2 (counts): with each channel's noise its own count, the bound on the split at d = 1.5, 2, 3 is the same for width
  ratios r = 1, 2, 4 (and 16 at d = 3) to 10⁻²⁰, and bound × √(total) equals run 2's draws bound (3.9206025055,
  1.90607019581, 0.876654356749) to 10⁻¹⁵.
- T3 (the same noise, channels even in frequency, the whole line): the spread across r at d = 1.5 above 5%.
- T4 (the same noise, channels even in the turn about i): the spread across r at d = 1.5 also above 5%. The equality does
  not come back for pairs that are not turns of one another about i.
- T5 (the same noise, channels even in the turn about i): run 2's pair at d = 1.5, r = 1 and its images under turns about
  i by 0.3, 1.0 and 2.0 radians give one bound to 10⁻²⁰; with channels even in frequency they differ by more than 1%.

If T4 fails (the spread under 5%), laying channels by one turn restores more than its own stabilizer, and the reasoning
above is wrong. Exact at 30 digits (mpmath), continuum, the whole line by x = tan t.
