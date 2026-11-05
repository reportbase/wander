# TCF: the test that can fail

5 Nov 2026 (Tom: "1", to "the test that can fail": take a Cauchy-type law whose source in print is not a turn, say
beforehand where the turn is and what the split between heat and paint predicts, and check it against published data).
Predictions first, written before any data is chosen or looked at. Nothing below the "Runs" line is edited afterwards.

## Why this test

*Reads and Writes* claims that a Cauchy met in the world is a turn's heat, read from a standpoint. The claim can fail.
It fails if the Cauchy is there and no turn can be named, or if a turn is named and the law it predicts is not the one
measured. Every case so far was chosen because a turn was already known: the lighthouse, LIGO's [H1 : L1], the dipole.
REA (`plans/rea/`) sorted 58 Cauchys from the literature, and two came out "D": the source names no turn, and the
reframing predicts something the source does not. This plan takes one of them, H54.

## The case: seeds falling from a height (REA H54)

**In print.** Wind-dispersed seed kernels are fat-tailed. The usual fit is Clark's 2Dt (Clark et al. 1999), the density
per unit area at distance r:

  f(r) = (p/(πu))·(1 + r²/u)^(−(p + 1)),

with a scale u and a shape p. It is read as a scale mixture of Gaussians, an amount mixed in (the spread of wind speeds
over seeds). Mechanistic models such as WALD (Katul et al. 2005) give the scale as the release height times the ratio of
wind speed to falling speed. No source we know reads the 2Dt as a turn.

**The turn named beforehand.** A seed leaves its release point at height h. Its line of travel, wind and fall together,
makes an angle α with the vertical. If it travels straight, it lands h·tan α away. Here:

- **The standpoint** is the release point, a height h above the ground: z = ih.
- **The heat** is the direction of travel, given before any seed falls.
- **The paint** is the seeds: how many there are, and when they fall.
- **What the turn reads** is the landing distance, r = h·tan α. It is the lighthouse with the shore laid flat around the
  foot.

If the directions are uniform over the downward hemisphere (every direction alike, as the uniform sky is), then:

  P(r ≤ R) = 1 − h/√(h² + R²),    f(r) = (1/2π)·h/(h² + r²)^(3/2).

That is the 2Dt with **p = ½** and **√u = h**. The shape is the turn's, the same for every species, plant and wind. The
scale is the release height.

Wind does not make the directions uniform; it tilts them toward its own way. In this geometry that is a two-axis drawing
whose sideways axis is drawn at c times the downward one, with c = (wind speed)/(falling speed). The writer's c from
*Reads and Writes* §2 is a real amount here. It moves the scale to √u = c·h and leaves the shape at p = ½: a two-axis
drawing at c ≠ 1 is the same Cauchy at scale c. So the turn reading splits the kernel as follows.

- **Shape: p = ½, read off.** It is the turn's, and no amount enters it.
- **Scale: √u = c·h.** h is a length and c a ratio of two speeds. Both are amounts, and both are the writer's.

The scale-mixture reading gives p freely, fitted per dataset. It has no reason for p to sit at ½.

## Predictions (written before any data)

- **T1. Shape.** Over published 2Dt fits to wind-dispersed seed kernels, the median fitted p lies in [0.3, 0.8]. Fits
  with p outside [0.15, 1.5] are a minority, under a third.
  - *Kill:* median p outside [0.3, 0.8], or a third or more of fits outside [0.15, 1.5].
- **T2. Shape is not set by size.** Across species, fitted p is uncorrelated with release height: |Spearman ρ| < 0.3.
  - *Kill:* |ρ| ≥ 0.3 with p < 0.05.
- **T3. Scale follows height.** Across species with both a fitted u and a reported release or plant height, log √u rises
  with log h. The slope lies in [0.5, 1.5]; the turn says 1, with c's spread across species as scatter.
  - *Kill:* slope outside [0.5, 1.5], or no significant rise (p ≥ 0.05).
- **T4. Within one study.** Where a study releases seeds at several heights under like wind, √u is in proportion to h
  within 25% across heights, and p does not move by more than its standard error.
  - *Kill:* either fails in a majority of such studies.
- **T5. The tail.** Where raw seed-trap counts are available, the counts per area at r ≫ √u fall as r^(−3), the
  exponent within [−3.6, −2.4].
  - *Kill:* outside it.

T1 and T5 can kill the turn reading of this case outright. T3 and T4 can kill the claim that the scale is the
standpoint's height. T2 checks that shape and scale come apart, which is what the heat/paint split says.

**What a kill means.** It means this case is not a turn read from the release point, and *Reads and Writes* §11's "the
test that can fail" has failed once. It does not by itself withdraw the rule that a Cauchy is an address. That is Tom's
to rule.

**What survival means.** It means only that the shape and the scale split as the turn says, in this case. Classical
mechanics already gives straight-line flight and WALD's scale. What would be ours is the shape read as the turn's, and
p = ½ said beforehand.

## Data (to be found and checked before any value is looked at)

Candidates, in order:

1. Bullock et al. 2017, "A synthesis of empirical plant dispersal kernels", *J. Ecol.*. A compiled set of fitted kernels
   with species traits, if its data are open (Dryad).
2. Clark et al. 1999, *Ecology*, the 2Dt's own tree seed-trap fits.
3. Release-height experiments for T4 (wind-tunnel or field releases at several heights).

For each source used, the plan will record its licence, its sha256, and which fits are wind-dispersed. Animal-, water-
and ballistically-dispersed kernels are left out, since they have no fall from a height. The rule for which fits count is
written below before any p is read.

## Runs

### Before run 1: the data and the counting rule (5 Nov, written before any kernel value was read)

**The data.** Bullock, J.M. et al. (2017) "A synthesis of empirical plant dispersal kernels", *J. Ecol.* 105, 6–19.
- Data: Dryad doi:10.5061/dryad.mq2ff, version of 25 Aug 2017, licence CC0. Supplied by Tom as Dryad's zip, since Dryad
  refuses scripted downloads. Not committed.
- `Plantdispersaldata.csv`: md5 0f59aca7616794b1ca6623f2f29960bf (matches Dryad's), sha256
  c9fd5500370346725f401be2634f9368af4d17b35b3c63c5fc6cfffbf6af7a8b.
- `README_for_Plantdispersaldata.rtf`: md5 963352249ede1a6f5d056995d87c8057, sha256
  61b825e378ba0545c2d2fd59108c1da0f9658b864d55cc579cdb32cdff689617.
- The zip: sha256 5578989a0f60a0c75abd8a34c4fc05d49912ed46429c6293fdd850349a771a44.

**What the file is, and what it changes in the plan.** The plan expected fitted 2Dt parameters with species traits. The
file instead holds the raw kernels: for each of 169 datasets, the species, the source, and rows of distance (m), seed
density (m⁻²) and, where given, the replicate. Bullock's 2Dt fits are not in it. Nor is any dispersal vector or plant
height. So:
- p is fitted here, by the rule below.
- The wind-dispersed kernels are picked from labels alone (below).
- **T2, T3 and T4 cannot be tested from this file and are left untested.** They would need release or plant heights,
  which it does not have. I do not substitute other tests for them after the fact.
- T1 and T5 stand as written.

**Which kernels count.** A fresh agent sorts the 169 datasets by vector: wind, ballistic, gravity, animal, water,
human/machine or unsure, with a confidence. It sees only each dataset's number, species name and source reference, never
the CSV's values, and it may read a paper's title or abstract but no distances or fits. **The primary set is the kernels
classed wind with high or medium confidence.** T1 and T5 are decided on it alone. The other classes are reported beside
it and decide nothing.

**The fit, per kernel.**
- Points with density > 0 only (the number of zeros dropped is reported). Replicates are pooled into one fit, as Bullock
  analysed them. A kernel needs at least 4 distinct distances with positive density.
- Model: log ρ(r) = log A − (p + 1)·log(1 + r²/u). Unweighted least squares on log ρ, over (log A, log u, log p).
- Bounds: p in [0.02, 50]; u in [10⁻⁶·r_max², 10⁴·r_max²]. Started from a grid of p and u, the best kept.
- Fits that end on a bound are kept and counted, and reported as on a bound.
- A is free, since densities come as absolute counts or as proportions; the shape p and the scale u do not depend on it.

**T5's slope, per kernel.** The least-squares slope of log ρ on log r over the points with r ≥ 2·√u (the fitted u),
where there are at least 3 such points. The prediction (p = ½) is −3. T5 is decided on the median slope over the primary
set: kill if outside [−3.6, −2.4].

**A caution written now.** Many kernels stop at a few metres, inside or near their own scale. There p and u trade off,
and p is poorly fixed. The spread of p, and how many fits sit on a bound, will be reported. The kill conditions are not
changed for it.
