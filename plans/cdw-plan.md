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
