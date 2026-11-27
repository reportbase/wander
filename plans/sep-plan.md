# SEP: separating overlapping Cauchys, standpoints and amounts

27 Nov 2026; SPN R1272. Tom: "To tease out the payload, you might need to separate multiple overlapping cauchies. We
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
