# CDW: a continuous read over discrete writes

27 Nov 2026, SPN R1268. Tom: "seems to me you can have a SHV sweep of a DHV sweep. in other words a continuous read heat
sweeping a discrete write heat." Then: "yes and merge".

## The case
The ring (`ring.html`, R1266) is the plainest one. The array is the discrete writes, an item at each whole number n. The
read is the continuous heat from a focus f with a thumb H, the item at the slope (n − f)/H, its weight
1/(πH(1 + ((n − f)/H)²)). Question: what does the continuous read make of the writes' discreteness?

## Known beforehand (not a prediction)
Poisson summation of the Cauchy (classical; the writer's mathematics, as every sum here is):

  S(H, f) = Σₙ H/(π(H² + (n − f)²)) = sinh(2πH)/(cosh(2πH) − cos(2πf)),
  S − 1 = 2 Σₖ e^(−2πkH) cos(2πkf).

So the run is a check of arithmetic, not a test that could kill a reading; nothing is predicted beyond the identity.

## Run 1 (`runs/cdw/cdw.py`, output `runs/cdw/cdw-out.txt`)
40 digits, H from 1/8 to 8, f at a write, a quarter and half way between. The sum over the writes equals the closed form
to 9·10⁻⁴¹ everywhere. The ripple S − 1 is 2e^(−2πH)·cos(2πf) to leading order: 0.0037 at H = 1, 7·10⁻⁶ at H = 2,
2.4·10⁻¹¹ at H = 4, 3·10⁻²² at H = 8; a quarter way between writes the first term vanishes and the second (e^(−4πH))
leads. At H = ¼ the read's total is 1.52 on a write and 0.66 half way between: the writes show through.

## Reading (Claude's, not ruled)
The writes' discreteness reaches the read only as a ripple of about 2e^(−2πH). Once a thumb spans a few writes the
continuous read cannot tell them from a continuum (the ring at H = 8 to 22 digits); below about one write a thumb it
sees which write it stands on. H ≈ 1, one write a thumb, is a corner: the read's fineness against the writes' spacing.
It is why the ring never needs the count N. Same composition as CRC and `gravity-ring.html` (a read's heat laid over
another density), the density underneath a comb, which is where the e^(−2πH) comes from. Wording kept to the rulings:
a write has no facing (R1138) and the DHV exists only as a synthesis (R1239), so "a DHV sweep" is said here as the
discrete writes laid out the writer's way; the read is the one sweep with a facing.

## Run 2: a row of masses, read and pulled back out (27 Nov 2026; Tom: "we use this for gravity", then "both")
Gravity as the case: each buried mass a write (an amount at a place), its pull on the ground the Cauchy of its depth d
weighted by its mass (GRV), a reader at height a adding its height (CRC, R1237), so only u = (a + d)/s enters, s the
spacing. P = 16 masses, period L = 16 s, masses seeded in [0.5, 1.5]; the pull sampled at 256 points a period, noise of
σ times the pull's largest value added, the masses recovered by least squares on the 16 masses' exact pulls.

Predictions, written before the run:
- Q1 (exact, an identity): an equal row's pull is (M/s)·sinh(2πu)/(cosh(2πu) − cos(2πx/s)); checked against the sum of
  the masses' Cauchys at 40 digits, to 10⁻³⁰.
- Q2 (exact): its ripple, (max − min)/mean, is coth(πu) − tanh(πu) = 2/sinh(2πu); at 40 digits to 10⁻³⁰.
- Q3: unequal masses' detail is held at frequencies up to 1/(2s), damped e^(−πu) (not e^(−2πu), which is the equal row's
  ripple at 1/s). So the recovered masses' rms error grows as e^(πu): the slope of ln(error) against u, fitted where the
  error is between 10σ and 0.05, within 10% of π, for σ = 10⁻⁶ and 10⁻³.
- Q4: recovery fails (rms error past half the masses' spread) at a u that moves by ln(1000)/π = 2.20 between σ = 10⁻³ and
  10⁻⁶, within 0.3.
- Q5: the total mass (the zero harmonic, never damped) comes back to within 10σ relative at every u up to 8.

Run 2 (`runs/cdw/cdw2.py`, output `runs/cdw/cdw2-out.txt`):
- Q1 not killed: the equal row's pull equals the sum of the masses' Cauchys to 2·10⁻⁴¹.
- Q2 not killed: its ripple is 2/sinh(2πu) to 3·10⁻⁴¹; 0.87, 0.17, 0.0075 and 1.4·10⁻⁵ at u = ¼, ½, 1 and 2.
- Q3 not killed at σ = 10⁻⁶ (slope 2.906, 0.925 of π, over 12 points); untested at σ = 10⁻³ by its own letter, since only
  two points fell between 10σ and 0.05 (my window, too narrow for that noise). Not refitted.
- Q4 not killed: recovery fails at u = 5.0 (σ = 10⁻⁶) and 2.75 (σ = 10⁻³), a shift of 2.25 against 2.20.
- Q5 not killed: the total mass back to within 0.26σ at every u to 8, even where each mass's error is 10⁶.
Reading (Claude's, not ruled): each mass's share is had only while (a + d)/s stays under about ln(1/σ)/π spacings;
past it the reader still has the total mass per spacing exactly and nothing of how it is shared out. Only a + d enters,
so a mass's depth and the reader's height trade one for one, and the mass is never had apart from them (R1197). This is
potential-field geophysics' downward continuation, ill-posed for the same reason (classical).

## Run 3: a chain of reads, a telescope, a pixel layer (27 Nov 2026; Tom: "how deep does it go? human continuous reads a continuous tellisicope read of a discrete write", then "yes, run it and merge")

Predictions committed before the script (SPN R1271). On a line, the sky's writes at the whole numbers (spacing s = 1,
period 16, unequal amplitudes seeded 1271, and an equal row), read through layers, each layer a Cauchy (wrapped on the
period) applied by direct quadrature, not by Fourier, so the composition is computed, not assumed.

- **T1, the chain collapses.** An objective of height h₁ on the sky, a magnification M (y = Mx), an eyepiece h₂ and an
  eye h₃ on the image give exactly one Cauchy read on the sky of height u = h₁ + (h₂ + h₃)/M, for M = 1, 2, 10, to
  10⁻¹⁰ of the peak. At M = 1 the layers' order and split do not show: (0.1, 0.2, 0.3), (0.3, 0.2, 0.1) and (0.6, 0, 0)
  give one image (to 10⁻¹⁰).
- **T2, later layers count 1/M.** The equal row's ripple at the eye is exactly 2/sinh(2πu) with that u (to 10⁻⁹
  relative); with h₁ = h₂ = h₃ = 0.3, the ripple at M = 10 (u = 0.36) is more than 20 times that at M = 1 (u = 0.9).
- **T3, a pixel layer is a second write.** After the objective (h₁ = 0.3) and M = 8, a detector of pitch p = 1 (image
  units) integrates the image over each pixel, and the eye reads the pixel values as point writes at the pixels'
  middles with a Cauchy of height h₃. (a) A uniform sky reads with a ripple at the pixel spacing of exactly
  2/sinh(2πh₃/p) of its mean (h₃ = 0.5, to 10⁻⁹). (b) For the equal star row, the image's component at the stars'
  frequency 1/M is 2e^(−2πh₁)·sinc(πp/M)·e^(−2πh₃/M) (sinc x = sin x/x), to 10⁻⁵ relative, the pixel's box the one new
  factor. (c) The same image has a second ripple, at the pixel frequency 1/p, equal to 2e^(−2πh₃/p) of the mean to 1%
  (h₃ = 0.5): the sky's writes and the detector's writes each leave their own ripple.

Kill: any of T1–T3 outside its bound.

### Run 3's results (`runs/cdw/cdw3.py`, output `runs/cdw/cdw3-out.txt`; one second)

Nothing killed.
- T1: the objective, magnification and two later reads are one read on the sky at u = h₁ + (h₂ + h₃)/M, worst gap
  1.2·10⁻¹⁴, 6.4·10⁻¹⁴ and 2.0·10⁻¹² of the peak at M = 1, 2, 10; the three splits at M = 1 one image to 2.1·10⁻¹⁴.
- T2: the equal row's ripple 2/sinh(2πu) to 2.2·10⁻¹² relative; at M = 10 (u = 0.36) 30.1 times that at M = 1 (u = 0.9).
- T3: (a) the uniform sky's pixel ripple 0.1731790751 against 2/sinh(π) to ten digits; (b) the stars' component
  0.19981872 against 2e^(−2πh₁)·sinc(π/8)·e^(−2πh₃/8) = 0.19981906, relative 1.7·10⁻⁶ (the aliased harmonics, about
  e^(−2π·7h₁), as expected); (c) the pixel-frequency ripple 2e^(−π) to 2.6·10⁻¹³.

Reading (Claude's, not ruled). However deep the chain of continuous reads, it is one read, the heights summed, each
weighted by 1/M of the magnification before it; no layer brings back what an earlier one smoothed, and the order and
split of the layers do not show. A telescope rescales what follows it, so the objective's grain decides. A detector is
a write in the middle: its pixels leave a ripple of their own at their own spacing, by the same law, beside the sky's,
and its box adds one factor, sinc(πp/M), to the sky's. Classical optics (cascaded transfer functions, the pixel's
box); the sorting into reads, writes and the one place an amount enters is ours.
