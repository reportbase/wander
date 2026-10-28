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
  H1's core is drawn about 7% larger than L1's. That is a drawing at c ≈ 0.93 for this ratio's two parties, and the median sits at c: the corner
  moves with the drawing, as Proposition 5(d) says. My prediction assumed the whitening drew
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

### Run 2 (23 Oct, `python3 runs/lgo/lgo2.py`; output `runs/lgo/lgo-run2.txt`)

- **G1′ not killed.** Over N = 1 … 64 the block means' IQR falls with slope −0.521 (H1) and −0.501 (L1).
- **G3′ not killed.** c = IQR(L1)/IQR(H1) = 0.9323; median |r| 0.9315, quartiles −0.9302 and +0.9327, each within 0.2% of
  c. The ratio's corner is where the two channels' drawings put it, measured from their own readings.
- **G8 not killed.** With each channel divided by its own IQR, a drawing made from order: median |r| 0.9990, quartiles
  −0.9977 and +1.0004, and the block means' IQR slope −0.006 over N = 1 … 1024. The direction of the two detectors is the
  standard Cauchy at its corner once V = H is drawn, and averaging it gains nothing.
- **G9 killed in its letter, by my set-up.** Removing the loudest 0.1% of H1's samples moves the angle's distance from
  uniform from 0.00866 to 0.00857 (as predicted), and H1's excess kurtosis from 74,305 to −0.057. My test was a ratio
  above 100, and the second value went below zero, so the ratio is negative; a kurtosis can cross zero, and a ratio was
  the wrong measure. What it was for stands: the transient is the whole of the heavy tail and moves no address. (The
  slightly negative value is partly the cut itself, which removes a tail.)

**Where LGO stands.** Read through the framework, the old test sorts this way:
- its N = 1 preference for the Cauchy over the Gaussian is a finite-variance tail (a t with ν = 15.9) made by one loud
  transient: the payload's;
- its transition toward the Gaussian is the amounts' central limit (the means shrink as n^(−½) through the whitened
  band): an amount with a spread, which a Cauchy could not be, since averaging Cauchy readings changes nothing;
- the Cauchy is in the data where the turn is: the direction [H1 : L1] of the two detectors read at one instant, the
  standard Cauchy once each is drawn at one length by its own readings (V = H), its angle uniform to 0.009, its averages
  not shrinking at all, and the transient leaving it where it was.

The old test was right that something in LIGO's noise is a Cauchy; it looked for it in the amount, where it is not, and
its "transition" is the evidence that it is not. Nothing here is new physics: ratios of independent centred normals,
the central limit theorem and the stable law of index 1 are classical, and so is LIGO's transient noise. What is ours is
the sort.

### Run 3: predictions (28 October 2026, written and committed before any new data is fetched; SPN R560)

Tom: "fix the errors and design and run the test". The fourth referee read of the submission objected that the paper's
test cannot fail as stated, and that its LIGO case reported a direction as uniform when, at two million samples, a
Kolmogorov distance of 0.009 rejects uniformity. This run takes the claim the paper now makes, "counted against what
arrives, the readings' law is the turn's law weighted by how what arrives is spread over the directions, and that spread
can be measured on its own", and tests it on data not yet seen.

**Known beforehand.** Runs 1–2's segment (GPS 1257000000) and its numbers, read above, including the angle's distance
0.0087 there. While deciding the design I estimated, for that segment only, that unequal Gaussian spreads at c = 0.93
alone would give a distance near 0.006, below the 0.0087 observed: so something besides the two spreads shapes the angle
there (the channels' non-Gaussian shapes, or a joint dependence). Nothing below uses any new data.

**The claim made operational.** "Measured on its own" is taken to mean: from each detector's readings separately, with no
use of which H1 sample goes with which L1 sample. Pairing H1 with L1 shifted in time by 8 s keeps both channels' own laws
and destroys their joint timing. If the angle's law is the turn's law weighted only by the spread of what arrives, as the
two channels' own laws give it, then the simultaneous pair and the shifted pair have the same angle law. If the two
detectors' noises share something at one instant, the simultaneous pair's angle law differs, and the claim in that form
fails.

**Data.** Three new segments, chosen by a rule fixed now: for each start S in 1240000000, 1250000000 and 1262000000 (O3a,
O3a, O3b), the first of S, S + 512, S + 1024, … (at most 40 tries) for which 512 s of both H1 and L1 fetch from GWOSC with
no gap or NaN. Each is whitened as in runs 1–2 (fftlength 4 s, overlap 2 s, 2 s trimmed each end). Drawn at one length:
each channel divided by its own interquartile range.

**Predictions, for each of the three segments** (all three must hold; any one segment's failure kills):
- **L1 (the amounts shrink).** The IQR of each channel's block means over N = 1 … 64 falls with log-log slope within 0.07
  of −½. *Killed* otherwise.
- **L2 (the direction does not).** The IQR of the block means of r = L1/H1 (drawn) over N = 1 … 1024 has slope within 0.1
  of 0. *Killed* otherwise.
- **L3 (the corner, drawn at one length).** Median |r| within 0.01 of 1; quartiles of r within 0.01 of −1 and +1. *Killed*
  otherwise.
- **L4 (the drawing sets the corner).** Undrawn, with c = IQR(L1)/IQR(H1) from each channel alone: median |L1/H1| and the
  quartiles within 1% of c and ∓c. *Killed* otherwise.
- **L5 (the angle's law is the spread of what arrives, from each channel alone).** With φ = atan2(L1, H1) on the drawn
  pair, D_sim its Kolmogorov distance from the uniform law and D_shift the same with L1 shifted circularly by 8 s:
  |D_sim − D_shift| ≤ 0.001, and the two-sample Kolmogorov distance between the two sets of angles ≤ 0.003. *Killed*
  otherwise.

What would not be shown: anything about gravitational waves or the detectors. A pass says the direction's law, its
corner and its departure from the uniform turn are accounted for by the two channels' own laws; it does not say that a
classical analysis would predict otherwise (it would not: this is a test that the reading's claim holds, not that a rival
fails). L5 is the one that can fail for a reason the reading did not build in: a shared disturbance at one instant.

### Run 3 (28 Oct, `python3 runs/lgo/lgo3.py`; output `runs/lgo/lgo-run3.txt`)

The segment rule found two of the three segments. From GPS 1240000000 none of the 40 starts (1240000000 … 1240019968)
had data: GWOSC holds no H1 dataset there ("Cannot find a GWOSC dataset for H1 covering [1240000000, 1240000512)"), a gap
in the run, not a failed prediction. The run therefore has two segments, not the three planned; nothing was substituted.
- **Segment 1250017408** (the rule's 35th start from 1250000000). sha256 of the strain as fetched: H1
  `e53d6f1ccfe6f7b0a14de33f6f4d635442784b38cdb6b6c91251605f780e8aee`, L1
  `a69e45659304d43a6878d5b3e5781a81e6ff365bcb98b61be8f95dac529b4061`.
  L1 not killed (slopes −0.536, −0.483); L2 not killed (−0.002); L3 not killed (median |r| 1.0010, quartiles −1.0033,
  0.9988); L4 not killed (c = 0.8694; median 0.8702, quartiles −0.8722, 0.8683); L5 not killed (D_sim 0.00764, D_shift
  0.00774, difference 0.00009; two-sample 0.00051).
- **Segment 1262000000** (the rule's first start). sha256: H1
  `b519186ab440176e3f646a4196e1f88185592bb1484e1f615e98ab8d21af99ea`, L1
  `3b8f1d925e5ef13e77b85de462dc57676c29b34ad0e039159a8e959a6d614413`.
  L1 not killed (−0.518, −0.502); L2 not killed (−0.008); L3 not killed (0.9996; −0.9999, 0.9993); L4 not killed
  (c = 0.9468; 0.9464; −0.9467, 0.9461); L5 not killed (D_sim 0.00613, D_shift 0.00608, difference 0.00005; two-sample
  0.00039).

**Where run 3 stands.** On data not seen when the predictions were written, every prediction held on both segments. The
angle is detectably not uniform in each (0.0076 and 0.0061 against a sampling scale of 0.00094), and pairing each H1
sample with the L1 sample 8 s away, which keeps each channel's own law and destroys their joint timing, reproduces that
departure to 0.0001, the two sets of angles indistinguishable at 0.0005. So the direction's law, its corner and its
departure from the uniform turn are accounted for by the two channels' own laws, measured separately, as the paper's
claim says. L5 could have failed, through a disturbance shared at one instant; it did not. As the predictions said, a
classical analysis would not predict otherwise: this shows the claim holds where it can be checked, not that a rival
fails. Two segments, not three.
