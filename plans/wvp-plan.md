# WVP: the exterior reader's pattern built by the interior reader's arrivals

*15 October 2026 (Tom's local date). Tom, about 15:45: "exterior - wave like,   interior - particle liike" (SPN R270),
then "yes" to a plan with its predictions first.*

## The claim

R270 reads the exterior reader as wave-like: it holds one facing whole, a pattern, and reads it in squares at twice the
angle (R265). The interior reader is particle-like: it takes arrivals one direction at a time from home, each at one
address. With R267 (the payload is a wave of some kind) both read one payload. If so, the interior reader's arrivals,
counted, must build the exterior reader's pattern, and the way they converge is fixed by the geometry alone.

Everything below is in unit relations. Each arrival is one direction θ of the facing, drawn evenly on [0, π/2] (the even
turn, OFS §7.1), read as s = v/h = tan θ and as the square h² = cos²θ. No amounts, so no bridge is needed. The exterior
reader's pattern is the law itself: the readings half-Cauchy, the squares the arcsine law (OFS §3.4; JAY P2). This is a
simulation of our own checked against that law, not real data; it tests whether the reading is consistent, not physics.
A real-data follow-up (single-photon counts building an interference pattern) is named at the end, not run.

## Predictions (written before any run)

N is the number of arrivals; each estimate below is taken over 400 seeded runs (numpy, seeds 0–399), at
N = 10², 10³, 10⁴, 10⁵.

- **P1. The pattern is built at the rate √N.** The largest gap between the interior's counted shares (the empirical law
  of θ) and the exterior's pattern, the Kolmogorov distance D_N, has mean falling as N^(−1/2): the fitted slope of
  log mean D_N against log N is −0.50. *Killed if* the slope is outside [−0.55, −0.45], or √N·mean D_N at N = 10⁵ is
  outside 0.869 ± 0.05 (Kolmogorov's mean, √(π/2)·ln 2).
- **P2. The corner is found by count, with spread π/2 per √N.** The median of the arrivals' levels, ln s, sits at the
  corner, 0, and its spread across runs is (π/2)/√N: the density of ln s at 0 is 1/π, so the median's standard error is
  1/(2·(1/π)·√N). The exterior reading, π/2, sets how fast the interior finds the corner. *Killed if* the mean median
  is off 0 by more than 3 standard errors at any N, or √N × the spread is outside π/2 ± 5% at N ≥ 10³.
- **P3. The mean never settles; it climbs 2/π·ln 10 a decade.** The running mean of the readings s does not converge:
  its median across runs grows by (2/π)·ln 10 = 1.466 per tenfold N (the half-Cauchy's truncated mean, (2/π)·ln N + c).
  The interior reading, 2/π, sets the climb. *Killed if* any decade's step in the median of the mean is outside
  1.466 ± 0.15, or the spread of the mean across runs (its interquartile range) shrinks by more than a factor 2 from
  N = 10² to 10⁵ (a settling mean would shrink it by √1000 ≈ 32).
- **P4. In squares, the arcsine pattern and its middle.** The arrivals' squares h² average ½ (the corner's square) and
  the share with h² ≤ ¼ is (2/π)·arcsin(½) = ⅓. *Killed if* at N = 10⁵ the mean over runs of either is off by more than
  4 standard errors of that mean (σ/√(400·N), with σ² = ⅛ for h² and σ² = 2/9 for the share).
- **P5. The two readers' product.** The exterior holds the pattern whole and reads the arc over its line, π/2; the
  interior's arrivals give the mean shadow, the average of cos θ, which settles (it is bounded) at 2/π; the product of
  π/2 and the interior's counted mean shadow tends to 1 at rate N^(−1/2). *Killed if* at N = 10⁵ the mean over runs of
  (π/2)·(mean of cos θ) is off 1 by more than 4 standard errors (σ_cos = √(½ − 4/π²)).

What a kill would mean: P1, P4 and P5 are ordinary laws of large numbers and would fail only by my set-up; P2 and P3
are the claims that the exterior reading and the interior reading set the interior reader's convergence (π/2 the
spread of the corner's estimate, 2/π the mean's climb). Those two are the content.

## Runs

### Run 1 (15 Oct, `runs/wvp/wvp.py`, output in `runs/wvp/run1.txt`; 4 s)

| N | √N·mean D | median ln s | √N·sd of median | median of mean s | IQR of mean s | mean h² | share h² ≤ ¼ | (π/2)·mean shadow |
|---|---|---|---|---|---|---|---|---|
| 10² | 0.8656 | +0.0106 | 1.5881 | 3.583 | 2.284 | 0.49776 | 0.33355 | 0.99800 |
| 10³ | 0.8454 | −0.0018 | 1.5587 | 5.541 | 3.559 | 0.50049 | 0.33251 | 1.00067 |
| 10⁴ | 0.8514 | −0.0005 | 1.5139 | 6.784 | 2.986 | 0.50014 | 0.33310 | 1.00018 |
| 10⁵ | 0.8537 | −0.0001 | 1.5012 | 8.344 | 3.358 | 0.50003 | 0.33323 | 1.00003 |

- **P1 not killed.** Slope −0.5015; √N·mean D at 10⁵ 0.8537 against 0.8687 (inside ± 0.05).
- **P2 not killed.** The medians sit at the corner within 3 standard errors at every N; √N × their spread 1.559,
  1.514, 1.501 against π/2 = 1.571 (inside 5%; the last is 4.4% low).
- **P3 killed.** The mean did not settle (its interquartile range across runs grew, ×1/0.68 from 10² to 10⁵, where a
  settling mean would shrink it 32-fold), but the decade steps of its median were 1.958, 1.243 and 1.560 against
  1.466 ± 0.15: two outside. Over the three decades the climb averages 1.587 a decade, 8% above (2/π)·ln 10. Post hoc,
  my set-up: the median over 400 runs of a quantity whose spread across runs is about 3 carries a standard error near
  0.2 by itself, so a ±0.15 band on each step was narrower than the noise I chose. The climb's size is not tested by
  this run.
- **P4 not killed.** Mean h² off ½ by 0.55 standard errors; the share with h² ≤ ¼ off ⅓ by 1.36.
- **P5 not killed.** (π/2)·mean shadow off 1 by 0.41 standard errors at 10⁵.

### Run 2, P3′ (prediction written before running)

The climb of the mean, with the noise counted. **P3′.** With 4,000 seeded runs per N (seeds 10,000–13,999) at
N = 10², 10³, 10⁴, 10⁵, the median across runs of the running mean of s climbs (2/π)·ln 10 = 1.466 a decade on
average over the three decades, (median at 10⁵ − median at 10²)/3. Its standard error is taken from 1,000 bootstrap
resamples of the runs. *Killed if* the average climb is off 1.466 by more than 3 bootstrap standard errors, or the
interquartile range of the mean across runs shrinks by more than a factor 2 from 10² to 10⁵.

### Run 2 (15 Oct, `runs/wvp/wvp2.py`, output in `runs/wvp/run2.txt`; 5 s)

The median of the mean across 4,000 runs: 3.7919 at N = 10², 8.0673 at 10⁵. Average climb 1.4252 a decade against
(2/π)·ln 10 = 1.4659, bootstrap standard error 0.0165: off by 2.47 standard errors, inside 3. The interquartile range of
the mean across runs 2.962 at 10², 2.893 at 10⁵ (×1.02: it does not shrink). **P3′ not killed**, close to its edge.

## What it shows

On the even turn, the interior reader's arrivals, counted, build the exterior reader's pattern: the law of the
directions at the rate √N (P1), the squares' arcsine law and its middle (P4), the mean shadow 2/π, whose product with
the exterior's π/2 tends to 1 (P5). The two vantages' numbers set how the interior converges: the corner is found by
count with spread (π/2)/√N in levels (P2), and the mean of the readings never settles but climbs (2/π)·ln 10 a decade
(P3′; P3 killed by my tolerance). So the reading of R270 is consistent: one payload, held whole as a pattern by the
exterior reader, met one arrival at a time by the interior reader, which reaches the pattern's shares and its corner
but never a mean. This is a simulation of our own on a law chosen beforehand; it says nothing yet about physical
waves or particles.

**Next, not run.** Real data: published single-photon (or single-electron) build-ups of an interference pattern, where
counted arrivals are recorded one by one (Tonomura et al. 1989 for electrons; Grangier, Roger and Aspect 1986 for single photons).
The prediction to write first: the counted pattern's Kolmogorov gap falls as N^(−1/2), and the pattern's own corner (in
whatever pair is named) is found by count with the spread its density sets. The bridge (counts and positions in amounts)
must be named before it is run.

### Run 3, real data: predictions (written 15 Oct about 20:05, before any frame's counts were read)

Tom, 15 Oct about 20:00: "yes" (to this follow-up, the real-data test named above). **Data.** Aspden, Padgett and
Spalding (2016), *Video recording true single-photon double-slit interference*, Am. J. Phys. 84, 671–677; raw frames
at Enlighten Research Data, doi:10.5525/gla.researchdata.281, CC BY 4.0. `Video_data.zip` (1,001,556,516 bytes,
sha256 f81834b586f301b6697ec9b9696b9198a2975146f9853f0758371d8aa2e70d42), not committed. Ten sets of 512 × 512 frames,
thresholded and binarised by the authors, each frame a few heralded photons. Used here: heralded diffraction with a
single-mode herald (D_SM, 4,070 frames) and multi-mode (D_MM, 1,500), heralded imaging of the slits single-mode (I_SM,
4,070), and the ghost pair as a replicate (G_SM diffraction, GI_SM imaging, 4,070 each).

**Known beforehand** (the paper's text and captions, read before writing this): slits 100 µm wide, 500 µm apart
centre to centre; λ = 710 nm (10 nm filter); f = 500 mm, fringe spacing fλ/d; the figures' axis 0 to 6,500 µm across
the frame; the single-mode herald gives high-contrast fringes, the multi-mode largely erases them, imaging is little
affected; the ghost and heralded diffraction planes are 1 : 1. Read: one frame's format (512 rows of 512 tab-separated
values). Not read: any count, profile or figure value.

**The bridge.** A detection is a pixel; its place x along the fringes is an amount, carried into the unit relations by
the fringe period P (the phase φ = 2π(x − x₀)/P + δ) and, for Q4, by the Born rule: each slit's amplitude is the square
root of its share of the counts, h = √(n₁/(n₁ + n₂)), v = √(n₂/(n₁ + n₂)), read from the imaging run, which is assumed to
light the slits as the diffraction run did (same source and slits, another lens).

**Procedure, fixed now.** An arrival is a nonzero pixel (a value k > 1 counted k times); order by frame, within a frame
shuffled (seed 0). The fringe axis is the one (rows or columns summed) with more power at periods 30–90 px. The summed
profile is fitted by Poisson maximum likelihood to n(x) = B + A·sinc²(π(x − x₀)/W)·(1 + C cos(2π(x − x₀)/P + δ)), all
seven free; standard errors from 200 bootstrap resamples of frames (seed 1). The imaging profile's two stripes are
split at the lowest pixel between their peaks, with B taken from the frame's outer quarters, per pixel.

- **Q1. The bridge.** The fitted P in D_SM and G_SM is fλ/d at the figures' 12.70 µm a pixel, 55.9 px, within 10%.
  *Killed if* outside: then the pixel scale or the optics are not as read; the rest runs on the fitted P.
- **Q2. The pattern built at √N.** Consecutive blocks of N arrivals, N = 25·2^k while N ≤ M/16 (M the set's total), each
  compared with every arrival outside it by the Kolmogorov distance of its profile along x. *Killed if* the slope of
  log mean D against log N is outside [−0.55, −0.45] in D_SM, D_MM or G_SM, or √N·mean D at the largest N is more than
  20% above its value at the smallest (a drifting pattern).
- **Q3. The address found by count, with the spread the pattern sets.** In blocks of N arrivals (N = 50, 100, 200, at
  least 30 blocks), the phase estimate φ̂ = arg Σ e^(iφ_j). Predicted: √N·sd(φ̂) = √⟨sin²φ⟩/⟨cos φ⟩, the moments over all
  arrivals (√2/C for a fold that is exactly 1 + C cos φ). *Killed if* off by more than 3 of the sd's own standard errors,
  1/√(2(b − 1)) for b blocks, at any N in D_SM or G_SM.
- **Q4. The contrast is the pair's facing, at most.** Two beams of amplitudes h and v give 1 + 2hv·|γ| cos φ: the
  contrast is the facing sin 2θ = 2hv (tan θ = v/h) times a coherence |γ| ≤ 1, so it reaches 1 only at the corner,
  h = v. *Killed if* C(D_SM) > 2hv(I_SM) + 3 standard errors (the two combined), or C(G_SM) >
  2hv(GI_SM) + 3 standard errors, or C(D_MM) is not below C(D_SM) by 3 standard errors (the last known beforehand, in
  kind).

What a kill would mean: Q1 is the bridge's amounts. Q2 and Q3 fail if photons are not independent draws from one
pattern (bunching, drift, dead time): physics or the apparatus, not the geometry. Q4 fails if the contrast exceeds the
two slits' facing, against two-beam interference, or if the bridge (one illumination for both runs) is wrong. None
tests the geometry itself; together they test R270's reading on real arrivals: one payload, a pattern whose contrast is
the pair's facing, met one arrival at a time and built at √N.

**A correction to the procedure, before any result** (15 Oct about 20:15). The frames are cumulative: each holds every
photon so far (D_SM's counts climb 5, 19, 31, … to 40,110 by its last frame; in 150 frames checked no pixel ever falls,
none rises by more than one between frames). The first run of the script took each frame's nonzero pixels as its
arrivals, counting every photon again in every later frame; it was stopped before any fit or test was printed. An
arrival is now a frame's gain on the frame before (the first frame's own pixels); the script stops if any pixel falls.
Nothing else changes.

**Not tested here: the mean's climb.** Read per arrival as s = tan(φ/2) (φ the facing, φ/2 the inscribed sweep), the
arrivals have density (1 + C cos φ) over the turn, so near the dark fringe a share (1 − C) of the even turn's: the
running mean of |s| climbs (1 − C)·(2/π)·ln 10 a decade (the even turn's (2/π)·ln 10 at C = 0, and a mean at C = 1).
With about 56 px a fringe, the pixel's step caps |s| near 35, and the climb is a few hundredths a decade: below what
these counts resolve. Stated, not run.

### Run 3 (15 Oct about 20:28, `runs/wvp/wvp3.py`, output in `runs/wvp/run3.txt`; 9 min)

Arrivals: D_SM 40,110, D_MM 589,498, G_SM 26,902, I_SM 65,316, GI_SM 928,175 (pixels, as defined above).

- **Q1 killed by my set-up.** Fitted P: D_SM 63.4, G_SM 70.1 px against 55.9 (D_MM, not required, 56.6: 1.3% off).
- **Q2 killed.** Slopes −0.434 (D_SM), −0.419 (D_MM), −0.496 (G_SM); √N·mean D rose 1.33×, 1.72×, 1.01×, and sat at
  1.4–1.9 where independent arrivals give about 0.87.
- **Q3 killed by my set-up.** √N·sd(φ̂) 2.2–2.5 times the prediction in D_SM and G_SM.
- **Q4 "not killed", but void.** 2hv 0.998 and 1.000; C 0.615 and 0.550; C(D_MM) 0.145. It was measured on the wrong
  axis (below), so it counts for nothing.

Post hoc, three errors of mine, found by looking at the profiles after the run:
1. **The axis.** For the single-mode sets the rule picked columns, where the profile is one narrow peak (the beam's
   width along the slits, whose low frequencies leak into the 30–90 px band). The fringes run along rows, about 56 px
   a period, as in D_MM, where the rule chose rows and P came out at fλ/d. The imaging runs agree: along rows they show
   the two slits' stripes 49 px apart; along columns, nothing. So Q1, Q3 and Q4 were fitted to the wrong profile.
2. **The arrival.** One photon lights a cluster of adjacent pixels (the intensifier's spot). In frames 1–399 there were
   2.58 pixels a cluster in D_SM and 2.18 in G_SM, and 1.45 in D_MM, whose clusters are mostly single pixels. Counting
   pixels counts most photons two to five times, in neighbouring places: the arrivals clump. That alone raises
   √N·mean D and the phase's spread above independent arrivals'. Q2's kill is my set-up as much as the photons.
3. **The phase estimator.** Q3's prediction used ⟨cos φ⟩ for the resultant's length, which holds only if the mean
   direction is at 0. It also needs N·R̄² large, and at N = 50 this was not so.

### Run 4: predictions (written 15 Oct about 20:30, before running)

The same data and tests, with the three errors removed. Fixed now:
- An arrival is a cluster: the 8-connected pixels of one frame's gain, placed at its centroid along the fringe axis,
  floored to a pixel.
- The fringe axis is rows for every set, fixed by the slits: rows is the axis along which the imaging runs show the
  two stripes.
- The phase estimator uses R̄ = |⟨e^(iφ)⟩| over all arrivals and the mean direction μ.

Known beforehand, from the diagnosis: the single-mode profiles along rows ripple at about 56 px, and the imaging
stripes' heights above background differ by roughly a fifth in GI_SM. Not computed: any fit, distance, spread or
share on rows with clusters.

- **Q1′.** Fitted P in D_SM and G_SM within 10% of 55.9 px. *Killed if* outside.
- **Q2′.** As Q2, on clusters: the slope in [−0.55, −0.45] and √N·mean D at the largest N at most 1.2 times its value
  at the smallest, in D_SM, D_MM and G_SM. *Killed if* not.
- **Q3′.** Blocks of N, N₀·2^k for k = 0, 1, 2, where N₀ is the least multiple of 10 with N₀·R̄² ≥ 20; at least 30
  blocks. Predicted √N·sd(φ̂) = √⟨sin²(φ − μ)⟩/R̄. *Killed if* off by more than 3/√(2(b − 1)) at any N, in D_SM or
  G_SM.
- **Q4′.** As Q4, on rows and clusters. *Killed if* C(D_SM) > 2hv(I_SM) + 3 se, or C(G_SM) > 2hv(GI_SM) + 3 se, or
  C(D_MM) is not below C(D_SM) by 3 se.

### Run 4 (15 Oct about 20:38, `runs/wvp/wvp4.py`, output in `runs/wvp/run4.txt`; 8 min)

| set | arrivals (clusters) | pixels each | P (px) | P/(fλ/d) | C | √N·mean D, N = 25 → largest | slope |
|---|---|---|---|---|---|---|---|
| D_SM | 15,551 | 2.58 | 56.08 ± 0.12 | 1.003 | 0.686 ± 0.016 | 0.839 → 0.877 (×1.045) | −0.483 |
| D_MM | 406,836 | 1.45 | 55.72 ± 0.73 | 0.997 | 0.090 ± 0.010 | 0.832 → 0.911 (×1.095) | −0.487 |
| G_SM | 12,310 | 2.19 | 54.95 ± 0.24 | 0.983 | 0.564 ± 0.014 | 0.851 → 0.985 (×1.157) | −0.452 |

- **Q1′ not killed.** The fringe period is fλ/d to 0.3% (D_SM) and 1.7% (G_SM), and to 0.3% in D_MM.
- **Q2′ not killed.** The slopes are −0.48, −0.49 and −0.45 (G_SM at its band's edge). √N·mean D sits at 0.83–0.99,
  around Kolmogorov's 0.87, where run 3's pixels gave 1.4–1.9. Counted as photons, the arrivals are independent draws
  from one pattern that does not drift, to within this test.
- **Q3′ not killed, but thinly.** The phase found by count spreads 0.939 (D_SM, N = 280, 55 blocks) and 0.935 (G_SM,
  N = 390, 31 blocks) times the spread the pattern sets, allowed ±0.29 and ±0.39. Only the first N had 30 blocks in
  each set. D_MM's resultant (0.016) needs N₀ = 78,960, five blocks: not tested.
- **Q4′ not killed.** The imaging runs give the two slits' shares 9,026 : 10,465 (I_SM) and 11,993 : 11,891 (GI_SM):
  2hv = 0.9973 ± 0.0018 and 0.99999 ± 0.0038. The pair sits at its corner. The contrast is below that facing: 0.686
  (19 se under) and 0.564 (30 se under), so the coherence |γ| = C/2hv is 0.69 and 0.56. The multi-mode herald's contrast
  is 0.090, 32 se under the single-mode's.

Post hoc, not predicted: the envelope's width over the period, W/P, is 5.12 in D_SM, against the slits' d/a = 5
(a single slit's sinc² has its first zero at fλ/a). G_SM gives 3.82 and D_MM 7.48: the ghost and multi-mode envelopes
are not one slit's.

## What runs 3 and 4 show

On real single photons, the reading of R270 holds as far as these four tests reach:
- arrivals met one at a time build one pattern at √N, as independent draws (Q2′);
- the pattern's period is the slits' (Q1′);
- the place of the fringes is found by count with the spread the pattern sets (Q3′, at one block size per set);
- the pattern's contrast is at most the two slits' facing, 2hv, and that facing is 1 only at the pair's corner (Q4′).
  Here the apparatus lit the slits equally, so the pair sat at its corner, and the contrast fell short only by the
  source's coherence.

All of this is classical: two-beam interference and the statistics of independent counts. What it adds is that nothing
in the data contradicts the reading: a payload read whole as a pattern, its contrast the pair's facing, and met one
arrival at a time.

Run 3 was killed by my set-up three times over: the wrong axis, pixels counted as photons, and a phase estimator
centred at 0. Run 4 removed those three errors, with predictions written first.

Not tested: whether the corner itself is visible in the counts beyond the contrast. That would need a set where the
two slits' shares vary (a slit partly covered), with the contrast falling as 2hv = sech of the levels between them.
That is the next real-data test, if such data exist. The mean's climb is stated above, not run.

### Re-read, 22 October (WVR, `plans/wvr-plan.md`; SPN R437)
The fringe phase found from arg Σe^{iφ} (Q3, "the address found by count") is a central reading, a circular mean, not
an address. Runs 1–2 drew uniform θ: that is the address law with no payload, so those draws are not arrivals; real
arrivals are Born-weighted. Read as tan(φ/2), a fringe's arrivals are a share V on the payload's law and 1 − V on the bare
turn's Cauchy, the mean climbing (1 − V)·(2/π)·ln 10 a decade (WVR P5).
