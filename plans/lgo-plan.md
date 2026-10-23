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
