# LTR: the distance ladder revisited (LTH in the light of reading and writing)

*Plan, predictions and kills written 22 October 2026 (Claude, a subagent asked to revisit LTH; SPN R436–R437's series of
revisits, "we have learned alot, lets revisit our physics results"), before any number below the "Runs" line was
computed. Cosmicflows-4's table2 and ReadMe were re-downloaded from the source recorded in `plans/lth-plan.md` and their
sha256 checked against it (all three match) before this plan was written; no column but the layout has been read
since. The lab rules hold: nothing above the "Runs" line is edited after the run.*

## Known beforehand

- **LTH run 1** (`plans/lth-plan.md`; Hubble 1929 against NED-D 17.1.0): one factor per rung, compounding (rung means
  1.6, 2.8, 3.0 levels; post hoc, M 101 is a brightest-star distance, and rung (a) without it is 1.2 levels, near
  Baade's factor of 2). The per-object table (Hubble's r and NED-D's median) is recorded there and is used here as it
  stands: no new download of NED-D is needed.
- **LTH run 2** (Cosmicflows-4, method against method): P5 killed; post hoc, regressing on the more precise method's
  modulus, SN Ia − FP −0.145 ± 0.047 and SN Ia − SBF +0.083 ± 0.024 mag/mag remain, FP − SBF −0.012 ± 0.046, SN Ia − TF
  −0.049 ± 0.032. These are on different x's and samples, but taken at face value the loop SN Ia → FP → SBF → SN Ia sums
  to −0.145 − 0.012 − 0.083 = −0.240 mag/mag, about 3.5 combined standard errors. **So P4 below is not blind**: I have
  seen a hint that the loop does not close. Run 2's plan named the fix (regress on an independent distance, the velocity
  in the Hubble flow) and declined it as no longer blind; it is done here, marked as not blind.
- **OFS §9** (settled): a reading is unchanged when every length is scaled by k, a writing changes by k; in a tower of
  holds the link between levels is a ratio read one level up, n lengths give n − 1 ratios, one amount anywhere writes
  all, a misread link moves everything it holds by one factor and leaves ratios inside it alone; a tree cannot find its
  own error, a second route (a loop) can, its closure error the misread factor exactly.
- **Classical, from training:** brightest-star distances depend on the host's luminosity (Sandage and Tammann 1974;
  the brightest stars of larger galaxies are brighter), which would compress a brightest-star rung, the far galaxies
  read too near by more. Malmquist-type selection in magnitude-limited samples makes a method's offset drift with
  distance, and depends on the sample, not only on the method. The Hubble flow at small z is d_L =
  (cz/H₀)[1 + (1 − q₀)z/2 − (1 − q₀ − 3q₀² + j₀)z²/6].

## The reading to test

**Sorting the ladder.** Under "scale the world" (every length, the au included, by k; times unchanged, so speeds by k):
- *Readings* (unchanged): every parallax angle (an address); the ratio of two distances found from the same kind of
  candle in two places (the flux ratio, (d₁/d₂)², the unknown luminosity cancelling, given the inverse square and the
  kind); every ratio between rungs; a rung's within-rung ratios; the Hubble flow's *shape* (log v linear in log d,
  slope 1, and its curvature q₀, a pure number).
- *Writings* (move by k): the au in metres (radar: c and a clock), each geometric anchor (NGC 4258's masers, through a
  Doppler speed in km/s; Milky Way parallaxes, through the au; the LMC's eclipsing binaries, through Doppler radii);
  every distance in Mpc, and H₀ (by 1/k). The one amount the ladder carries is the anchors' metre, which in every case
  enters through a speed and a clock.

**A link is a pan; a drifting link is a stretch.** In the tower each link is one factor: in levels a *pan*, the
method's modulus offset Δμ the same at every distance. An offset that drifts linearly with distance, Δμ = a + s·μ, is a
*stretch* in levels: distances read as d^(1+s), the method read on a different lay. A stretch is not scale-free: it is
zero at a pivot distance, and scaling the world moves the pivot's place, so a stretched link carries a hidden amount
(the pivot) where a pan carries none. The stretch's slope s is itself a reading (unchanged by k and by the H₀ assumed).

**Where a drift lives.** If the stretch is a property of the link (the method's own lay), it composes like any link:
pairwise slopes are differences s_A − s_B, and every loop of slopes closes. If it is a property of *which objects*
each comparison uses (selection), loops measured on different samples do not close. A loop on the *same* objects
closes identically (an identity, not a test). A single loop cannot say which of its links is misread; a network can,
by which of its loops fail.

## Predictions

**P1 (exact, the tower's arithmetic).** Checked with exact fractions and mpmath at 50 digits:
(a) a pan's Δμ is unchanged under every scaling k; a stretch's Δμ at a fixed object moves by 5s·log₁₀k; both slopes are
unchanged by k and by the H₀ assumed;
(b) on three methods compared on the same objects the loop of offsets (and of slopes) closes identically;
(c) in a network of methods whose links are each read on their own objects, a single misread link (a factor f, or a
slope s) gives a closure error of exactly f (or s) in every loop containing it and none elsewhere; on a triangle (K₃,
one loop) the misread link cannot be located (all three links fit equally); on K₄ (four methods, six links, the four
triangles) it is located uniquely by its two failing triangles, for every one of the six links.
*Kill:* any identity off by more than 10⁻⁴⁰, or a link on K₄ not located uniquely, or one on K₃ located.

**P2 (Hubble 1929: each rung a pan).** Within a rung, a pan moves every distance by one factor, so log₂ d_Hubble against
log₂ d_modern has slope 1. Rung (a) = the five of Hubble's first seven placed by their own stars (SMC, LMC, NGC 6822,
M 33, M 31; M 32 by association and M 101 by its brightest stars left out, as run 1 found post hoc); rung (b) = the
thirteen brightest-star objects plus M 101 (14). OLS of log₂ d_H on log₂ d_modern (modern distances being the far more
precise, the regression is on them). *Kill:* for either rung, |slope − 1| > 2 se.
(Claude's expectation, recorded and not the theory's: (a) holds; (b) is compressed, slope below 1, by the classical
host-luminosity dependence above. If so, rung (b)'s link was a stretch, not a pan.)

**P3 (Cosmicflows-4 against the flow: each method a pan).** For each method with ≥ 30 galaxies at Vcmb ≥ 3000 km/s,
Δ = μ_X − μ_flow regressed on μ_flow (OLS), with μ_flow = 25 + 5·log₁₀(d_L/Mpc), d_L from z = Vcmb/c by the expansion
above with q₀ = −0.55, j₀ = 1 and H₀ = 75 (the H₀ only offsets μ_flow and moves no slope). The tower predicts every
method a pan: slope 0. *Kill:* any method with |slope| > 3 se and |slope| > 0.03 mag/mag (0.03, not run 2's 0.02, to
allow for the dilution by peculiar velocities, about −var(e)/var(μ_flow) with σ_v = 300 km/s, which the script reports
beside each slope). Not blind in part (run 2).

**P4 (loops of slopes close: the drift is the link's).** Pairwise slopes b_AB of μ_A − μ_B on μ_flow, each on its own
overlap (both methods, Vcmb ≥ 3000 km/s, at least 20 galaxies). (i) Every triangle of methods all of whose pairs qualify:
b_AB + b_BC + b_CA = 0; (ii) every pair against the flow: b_AB − (s_A − s_B) = 0, s from P3's full samples. If the drift
is a property of the method (a stretched link), all close; if of the samples (selection), they do not, and no single
method can be named. *Kill:* any loop with |closure| > 3 combined se (in quadrature, treating the pieces as
independent, which they are not wholly: overlapping samples) and |closure| > 0.03 mag/mag. Not blind (see above).

**P5 (Hubble's rung factors are the misread links).** The tower says rung (b)'s offset over rung (a) is one link and
rung (c)'s over (b) another; a misread link shared up the ladder moves every rung above it alike. So the *same-rung*
log ratios' errors (run 1's P3) carry no trace of rung (a)'s factor: the median same-rung ratio error in rung (b) is the
same whether or not the 1.2 levels of rung (a) are taken out of rung (b)'s distances. This is an identity of the model
(a common factor cancels from every ratio inside a rung) checked on the recorded data. *Kill:* the two medians differ
by more than 10⁻¹².

## Not yet computed

Every per-method count at Vcmb ≥ 3000 km/s; every slope; P2's slopes; which loops qualify for P4.

## Runs

### Run 1 (22 October 2026; `runs/ltr/ltr.py`, output `runs/ltr/ltr-run1.txt`)

`python3 -I runs/ltr/ltr.py /tmp/ltrdata/table2.dat` (under a second). Cosmicflows-4 table2.dat.gz, table2.dat and ReadMe
re-downloaded from cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/; sha256 01da4042…ad79, 8e908928…332f and 2cfed141…4edb4, all
three matching `plans/lth-plan.md`; kept in /tmp, not committed. NED-D was not re-downloaded: P2 and P5 use run 1's
recorded table.

- **P1 not killed.** (a) A pan's Δμ unchanged under k = 10⁻³, 7, 10⁶ to 10⁻⁴⁰; a stretch's moved by exactly 5s·log₁₀k
  with its pivot held; the slope s the same at every k and every H₀ assumed. (b) 200 draws, the loop of three methods on
  one object 0 exactly. (c) K₄: 12 of 12 single misread links (six links, a factor of each sign) located uniquely by their
  two failing triangles, each closure the misread exactly; K₃: 3 of 3 not locatable (any link closes the one loop).
- **P2 killed, both rungs.** Slope of log₂ d_H on log₂ d_modern: rung (a), n 5, 0.793 ± 0.051 (4.1 se from 1); rung
  (b), n 14, 0.158 ± 0.234 (3.6 se). In (b), r = log₂(d_mod/d_H) correlates +0.72 with log₂ d_modern: the farther the
  galaxy truly is, the more Hubble's brightest-star distance falls short. Rung (b) is not a pan but a stretch; its
  distances carry almost no ranking within the rung. (My recorded expectation for (b) held; for (a) it did not.)
- **P3 not killed.** Against the Hubble flow (Vcmb ≥ 3000 km/s, 52,813 galaxies): SN Ia −0.021 ± 0.005 (3.8 se), TF
  −0.007 ± 0.005, FP +0.011 ± 0.002 (4.7 se), SBF +0.003 ± 0.088, SN II −0.077 ± 0.033 (2.3 se); none past both 3 se and
  0.03 mag/mag. SN Ia and FP are significant but under 0.03; TRGB, Cepheids, masers have under 30 galaxies past 3000 km/s.
- **P4 killed, one loop of six.** Triangle SN Ia–TF–FP +0.244 ± 0.133 (1.8 se); against the flow, SN Ia–FP
  b − (s_SN − s_FP) = −0.240 ± 0.074 (3.2 se), the rest under 1.4 se. The SN Ia − FP pair drifts −0.271 ± 0.074 mag/mag on
  its own 58 galaxies, while the two methods, each on its full sample, differ in drift by only −0.032.
- **P5 not killed.** Rung (b)'s median same-rung ratio error 0.812492 with or without rung (a)'s 1.177 levels taken
  out; difference 1.1·10⁻¹⁶.

**Read after the run (post hoc, `runs/ltr/ltr_posthoc.py`, `runs/ltr/ltr-run1-posthoc.txt`; not tests):**
- *The SN Ia − FP drift is the overlap's, not either method's.* On the 58 galaxies with both, SN Ia drifts −0.129 ±
  0.036 and FP +0.143 ± 0.071 against the flow; off the overlap, SN Ia −0.016 ± 0.005 (854) and FP +0.011 ± 0.002
  (41,973). The loop's failure says what the plan said it would mean: the drift belongs to which galaxies are compared
  (selection), so no link can be named as stretched. LTH run 2's "FP and SBF drift against the supernovae by ~0.1
  mag/mag" stands as a fact about those overlaps, not as a property of the FP or SBF rung. (Why this overlap: not
  tested; galaxies hosting both an SN Ia and an FP distance are cluster ellipticals, whose individual velocities scatter
  by a cluster's dispersion, far above the 300 km/s assumed; that would dilute both slopes, but not in opposite signs.)
- *SN Ia and FP against the flow by band:* SN Ia − flow +0.007, −0.002, −0.056, −0.053 mag over μ_flow 33–35, 35–36,
  36–37, 37–38.5; FP −0.057, −0.029, −0.043, −0.020. SN Ia's small slope is a step near μ 36 (about 160 Mpc), not a line.
  Not tested further.
- *Rung (a) is two links.* Shapley's Clouds sit at r 0.95 and 0.56 (mean 0.76), Hubble's own Cepheid galaxies (NGC
  6822, M 33, M 31) at 1.16, 1.70, 1.51 (mean 1.46). Two calibrations under one rung: the near pair's link and Hubble's
  differ by 0.7 levels, so a single regression across them reads as a stretch. Grouped by calibration, not by Hubble's
  "first seven", the tower would have four rungs, not three. Hubble's three alone: slope 0.41 ± 0.13 over 0.8 levels of
  modern distance, too short a span to say.
- *Rung (b) is a stretch, and run 1's P2 and P3 did not see it.* Run 1's P2 (spread within a rung smaller than the step
  between rungs) and P3 (same-rung ratios better than distances) hold for a stretch as for a pan when the rung's span is
  short against its offset; they test the mean, not the shape. P5 shows the identity under them: a shared factor cancels
  from every same-rung ratio, so same-rung ratio errors are the rung's own scatter, here mostly the stretch.

**Standing.** Sorted by "scale the world": every parallax angle, every same-kind flux ratio, every inter-rung ratio and
the Hubble flow's shape are readings; the au, the anchors (each through a speed and a clock), every Mpc and H₀ are
writings. The tower's arithmetic is exact (P1, P5): a misread link is one factor, a loop finds it only when its routes run
through different objects, and a network of loops, not one loop, says which link. On the data: Hubble's brightest-star
rung was a stretch (slope 0.16 against 1), not one factor; his Cepheid rung was two links. In Cosmicflows-4, every method
read against the flow is a pan within 0.03 mag/mag (a link is one factor), and the drift LTH run 2 found between SN Ia and
FP fails to close against the flow: it belongs to the overlap sample, a selection, not to a rung.
