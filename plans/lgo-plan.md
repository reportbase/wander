# LGO: LIGO's noise read through the address and the payload

*23 October 2026, SPN R468. Tom: "this is a test we ran to test these ideas for AI in another claude session. the tests
were successful. lets complete those tests, through the lense of our mathmatical framework." The test is `cauchy_test.py`
(an earlier session, its "BOMA prediction": single measurements follow Cauchy statistics, and accumulated ones move toward
the Gaussian). It fetches 512 s of LIGO Hanford (H1) strain from GWOSC, at GPS 1257000000 (O3b), whitens it, and compares
Cauchy and Gaussian fits of block means of length N = 1 … 2048. Tom asked for the ideas revisited from scratch, so the old
session logs were not read.*

*Real data, prediction first. GWOSC open data, CC BY 4.0 (LIGO Scientific Collaboration, Virgo Collaboration and KAGRA
Collaboration). Fetched through gwpy 4.1.0. The proxy's CA bundle does not cover gwosc.org's chain (InCommon under emSign
Root CA - G1), so it was joined to certifi's Mozilla bundle, which does; verification stayed on. The sha256 of each array
as fetched goes under the runs. Data not committed.*

## Known beforehand

- **The old script's result**, as Tom reports it: at N = 1 the Cauchy fits better than the Gaussian, and the preference
  falls as N grows, towards the Gaussian.
- **Whitened detector noise** is close to Gaussian, with non-Gaussian transients (glitches) and lines; this is the
  standard picture of LIGO noise (e.g. Abbott et al. 2016, 2020, on transient noise). A heavy tail at N = 1 from glitches
  is a scale mixture: Gaussian at most times, much wider at a few.
- **Classical:** a mean of n independent Cauchy readings is the same Cauchy, so its interquartile range does not shrink;
  a mean of n independent readings of finite variance shrinks as n^(−1/2) and tends to the Gaussian (the central limit
  theorem). A ratio X/Y whose denominator has a density above zero at 0 has a tail P(|X/Y| > x) ~ c/x, so means of such
  ratios fall in the Cauchy's domain of attraction, not the Gaussian's. A ratio of two independent centred normals of
  equal spread is the standard Cauchy, and their angle is uniform.
- **OFS:** a Cauchy variable is a direction, never an amount; find the turn, find the amount (§7.2, "The rule, and a
  test"). Averaging n Cauchy readings gains nothing ("Once a Cauchy, always a Cauchy"). An amount entering as a varying
  multiplier breaks the Cauchy into a mixture of scales ("What breaks it"). The Cauchy's corner at v/h = 1 needs the two
  parties drawn at one length, V = H (Proposition 5(d)).

## The reading, before the run

Whitened strain at one time is an amount: a number in the detector's own unit, here the noise's own spread. There is no
turn in it, so OFS predicts no address law in it. Its heavy tail is the payload's (a mixture of quiet and loud times),
and averaging it is an operation on amounts, which the central limit theorem governs. So the old test's own transition
toward the Gaussian is the mark of an amount with a finite spread, not of a Cauchy: a Cauchy would not move at all.

Where the framework does put a Cauchy is a direction. Two detectors 3,000 km apart, read at the same instant, give a
pair (H1, L1); the pair is a direction [h : v], and whitening each to unit noise is the drawing V = H. Its reading
r = L1/H1 should then be close to the standard Cauchy, with its median |r| at the corner, and averaging it should gain
nothing.

## Predictions

The data: H1 and L1, GPS 1257000000 to 1257000512, 4096 Hz, each whitened as the old script does (fftlength 4 s, overlap
2 s), 2 s trimmed from each end.

- **G0 (the old test, reproduced).** The old script's comparison on H1 gives ΔLL (Cauchy − Gaussian) > 0 at N = 1, and
  falling as N grows. *Killed* if ΔLL ≤ 0 at N = 1. (A reproduction, not a test of the framework.)
- **G1 (the amounts shrink: not a Cauchy).** The interquartile range of block means of H1, over N = 1, 2, 4 … 1024, falls
  with log-log slope within 0.05 of −½. *Killed* if the slope is above −0.4 (a Cauchy's is 0).
- **G2 (the tail is a mixture, with a finite spread).** A Student-t fitted to H1 at N = 1 has ν > 2, and beats the
  Cauchy by more than 100 in log-likelihood. *Killed* if ν ≤ 2 or the margin is 100 or less. So the old N = 1 result
  says only "heavier than Gaussian", which the Cauchy and the t share.
- **G3 (the direction is a Cauchy at its corner).** For r = L1/H1, sample by sample: the median of |r| within 0.05 of 1,
  and the quartiles of r within 0.05 of −1 and +1. *Killed* if any is off by more than 0.05.
- **G4 (the angle is uniform).** φ = atan2(L1, H1) has a Kolmogorov distance from the uniform law on (−π, π] under 0.02.
  *Killed* at 0.02 or more.
- **G5 (averaging the direction gains nothing).** The interquartile range of block means of r, over N = 1 … 1024, has a
  log-log slope within 0.1 of 0. *Killed* if the slope is below −0.1 (it would then be shrinking like an amount).
- **G6 (the drawing sets the corner).** Rescaling L1 by c before the ratio (c = ½, 2) moves the median of |r| to within
  0.05·c of c. *Killed* otherwise. (Proposition 5(d) on data: the corner belongs to the drawing V = H.)
- **G7 (the verdict).** If G1–G5 stand, the framework sorts the old test: its N = 1 preference is the payload's
  mixture, its transition the amounts' central limit, and the Cauchy is found where the turn is, in the direction of
  two detectors' pair, where averaging leaves it unchanged. *Killed* if G1, G2 or G5 is killed.

What would not be shown: anything about gravitational waves, about glitches' sources, or about the detectors' design;
that LIGO noise "is" Cauchy or Gaussian in any physical sense. The direction test needs the two detectors' noise nearly
independent at the same instant, which is what their separation is for; correlated lines would show as a departure in G4.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (23 Oct, `python3 runs/lgo/lgo.py`; output `runs/lgo/lgo-run1.txt`)

Data: H1 and L1, GPS 1257000000–1257000512, 2,097,152 samples each at 4096 Hz; sha256 of the float64 strain as fetched,
H1 `291a4b24ebc777f8ac416e1f052edf63d276140ccbefc1b45716454a613f90dc`, L1
`1f0f37d45750f4b0a1d9103e0c36fe18574ec85632015067b9dc785689a9023c`. After whitening and trimming, 2,080,768 samples each;
H1's sd 2.31 and excess kurtosis 74,305 (a loud transient in the window), L1's sd 1.03.

- **G0 not killed.** The old comparison reproduces: ΔLL (Cauchy − Gaussian) +1,149,014 at N = 1, falling through +604 at
  N = 128, and negative from N = 256 (−1,275, then −704, −343, −188).
- **G1 killed in its letter, by my set-up.** The IQR of H1's block means falls from 1.494 to 0.0183 over N = 1 … 1024, a
  slope of −0.611. Over N = 1 … 64 it is −0.510, as predicted; past N = 64 it steepens (−0.82 from 64 to 1024). A block of
  64 samples is 16 ms, and the means past it sit below the band the whitening keeps, so the whitened noise has less
  there than a flat spectrum would: the range I chose ran past the whitening's own low-frequency edge. What the
  prediction was for stands: the amounts' means shrink, eightyfold, as a Cauchy's never would.
- **G2 not killed.** A Student-t at N = 1 has ν = 15.9 (finite variance), and beats the Cauchy by 363,188 in
  log-likelihood and the Gaussian by 1,512,202. The old N = 1 result says "heavier than Gaussian", which here is a t with
  sixteen degrees of freedom and a loud transient, not a Cauchy.
- **G3 killed.** For r = L1/H1 the median |r| is 0.9315 and the quartiles −0.9302 and +0.9327: a Cauchy shape, centred,
  its quartiles a reciprocal-symmetric pair about the median, but at 0.93 and not 1. The two whitenings are not quite
  the same drawing: each channel was divided by its own spectrum's estimate, and H1's estimate carries the transient, so
  H1's core is drawn about 7% larger than L1's. That is V = cH with c ≈ 0.93, and Proposition 5(d)'s median at 1/c… at c
  for this ratio: the corner moves with the drawing, as the proposition says. My prediction assumed the whitening drew
  them at one length.
- **G4 not killed.** The angle atan2(L1, H1) is 0.0087 in Kolmogorov distance from the uniform.
- **G5 not killed.** The IQR of block means of r stays 1.86 from N = 1 to 1,024 (1.863, 1.861, … 1.777): slope −0.006.
  Averaging the direction gains nothing, while averaging the amount (G1) shrinks it eightyfold over the same blocks.
- **G6 killed by my set-up.** Rescaling L1 by c = ½ and 2 moves the median |c·r| to 0.4657 and 1.8629, which is
  0.49995 and 1.99989 of the unscaled 0.9315: exactly c times, as Proposition 5(d) says. The kill is the prediction's
  reference, 1, which assumed G3.
- **G7 killed,** since G1 was. Post hoc, what was meant stands: the old N = 1 preference is a finite-variance tail with a
  transient (G2), the amounts shrink under averaging (G1 over its proper range), the direction is a Cauchy whose median
  sits where the drawing puts it (G3, G6) and whose averages do not shrink (G5).

### Run 2: predictions (23 Oct, before the run, after reading run 1)

Run 1 informs these, which is said here: the band edge of G1 and the 7% of G3 were seen first.

- **G1′.** The IQR of H1's block means over N = 1 … 64 has slope within 0.05 of −½; and L1's the same. *Killed* otherwise.
- **G3′ (the drawing measured, not assumed).** Let c = IQR(L1)/IQR(H1) at N = 1, each read by its order statistics.
  The median |r| is within 1% of c, and the quartiles of r within 1% of ∓c. *Killed* otherwise.
- **G8 (V = H drawn by order).** Divide each channel by its own IQR before the ratio, a drawing made from the readings'
  order and not from a spectrum the transient inflates. Then the median |r| is within 0.01 of 1 and the quartiles within
  0.01 of ∓1, and averaging still gains nothing (the IQR of r's block means over N = 1 … 1024 has slope within 0.1 of 0).
  *Killed* otherwise.
- **G9 (the transient is payload: it moves no address).** Remove the loudest 0.1% of H1's samples (by |H1|) and the same
  instants from L1. The angle's Kolmogorov distance from uniform changes by less than 0.005, while H1's excess kurtosis
  falls by more than a factor of 100. *Killed* otherwise.
