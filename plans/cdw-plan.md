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
