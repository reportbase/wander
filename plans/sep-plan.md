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
