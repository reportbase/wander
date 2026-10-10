# CNT: star counts in levels

*Plan, predictions and kills written 10 October 2026, before the data was opened for counting (Claude; Tom: "yes" to the
first test in the queue of `papers/physics.md` §4). The lab rules hold: nothing above the "Runs" line is edited after the
run.*

## The claim

For things of one luminosity spread evenly through space, the number brighter than a flux F grows as F^(−3/2): the
volume out to the distance where they fade to F grows as that distance cubed, and the distance as F^(−1/2). In levels,
each level fainter brings 2^1.5 ≈ 2.83 times as many: **1.5 levels of number per level of light**. A mix of luminosities
changes nothing, since each kind alone gives the same slope. This is the counting form of the inverse square, the same
fact as OLB's "every shell fills the same share", and MAG's two levels of light per level of distance with the cube of
the volume put on it.

Our galaxy is not even. It is a disc a few hundred parsecs thick. Looking out of the disc, the stars run out sooner, and
the count rises more slowly than 1.5. So the theory predicts 1.5 where the stars counted lie well within the disc, and
less where the counts reach its edge.

## Keep the case

N (a count) and F (a flux) are amounts. Their levels, log₂ N and log₂ F, are ratios, and only slopes are used, so every
zero point drops out. The bridge is the assumption of an even spread, a density: an amount, given from outside. The disc
is where that bridge gives out.

## The data

The same file as MAG: HYG v3.8 (sha256 `9e914eb4544c1d8f4a87e1184bbc5322de1a7d1b9cb3110e870d15bc01c91f9d`).
- **Used:** stars with a Hipparcos number, their V magnitude, and their position (`ra`, `dec`), turned into galactic
  latitude b by the standard J2000 rotation.
- **Not used:** distances. Counts need none.
- **Limit:** Hipparcos is complete to about V = 7.3 over the whole sky, so every count stops there.
- **Light in levels** is −1.3288·V. N(<V) is the number brighter than V. The slope is that of log₂ N(<V) against light in
  levels, sign turned, fitted by least squares on the cumulative counts at steps of 0.1 magnitude.

## Predictions

- **P1 (the bright stars, well within the disc's reach).** All sky, V from 1 to 4: the slope is 1.5 within 0.2. *Killed*
  if outside [1.3, 1.7].
- **P2 (fainter, flatter).** All sky, the slope over V from 5 to 7.3 is shallower than over V from 1 to 4, by at least
  0.1. *Killed* if not.
- **P3 (out of the disc, flatter still).** V from 4 to 7.3: the slope toward the galactic poles (|b| > 60°) is shallower
  than in the plane (|b| < 10°), by at least 0.1. *Killed* if not.
- **P4 (in the plane, nearest the theory).** In the plane (|b| < 10°), V from 4 to 7.3, the slope is at least 1.25.
  *Killed* if under 1.25.

## What would not be shown

- The density of stars in the disc, or its thickness. Those need distances and a model; here the disc only shows as a
  departure from 1.5.
- Anything about faint counts, past Hipparcos's completeness, where other catalogues are needed.

## Runs

### Run 1 (10 October 2026)

`python3 plans/cnt/cnt.py` (data checked against the sha256), output in `plans/cnt/cnt-run1.txt`:

```
117951 Hipparcos stars with V; brighter than 7.3: 21107 (plane 5608, poles 1883)
P1: not killed. all sky, V 1-4: 1.325 levels of number per level of light (518 stars to V 4); 1.5 for an even spread
P2: not killed. all sky, V 5-7.3: 1.216, shallower by 0.110
P3: KILLED. V 4-7.3: plane (|b| < 10) 1.229, poles (|b| > 60) 1.227, difference 0.002
P4: KILLED. in the plane 1.229
  all sky, V 0-2: 1.165
  all sky, V 2-3: 1.308
  all sky, V 3-4: 1.191
  all sky, V 4-5: 1.236
  all sky, V 5-6: 1.221
  all sky, V 6-7.3: 1.204
```

- **P1 not killed, at the band's edge.** The bright stars give 1.325 levels of number per level of light, against 1.5 for
  an even spread; the band's floor was 1.3.
- **P2 not killed, at the band's edge.** The fainter stars give 1.216, shallower by 0.110 (band: 0.1).
- **P3 killed.** The plane and the poles give the same slope, 1.229 and 1.227. The poles were predicted flatter by at
  least 0.1.
- **P4 killed.** The plane gives 1.229, under the predicted 1.25.
- **Across the range** the slope is near 1.2 throughout, from V = 0 to 7.3 (1.17 to 1.31 in single-magnitude steps),
  never 1.5.

## Reading (after the run; not ruled)

- **The counts rise about 1.2 levels per level of light, not 1.5, everywhere.** The even-spread bridge gives out from the
  brightest stars on, and it gives out the same way in the plane and toward the poles.
- **The disc alone does not explain it.** The disc, the cause the plan named, should flatten the poles more than the
  plane, and the run says it does not. Two things known to act in the plane could be offsetting it there:
  - dust dims distant stars along the plane, flattening the count there too;
  - the brightest stars are young, and young stars lie in a thin layer and in nearby groups (the Gould Belt), not spread
    evenly even within the disc.
  
  Neither is tested here. Each would be a new run with its own prediction, and both need distances or extinctions.
- **What holds.** Counting is the inverse square in its third form: light falls two levels per level of distance (MAG),
  the volume rises three, so number rises 1.5 per level of light, *if* the spread is even. The stars are not spread
  evenly at any brightness Hipparcos reaches. The departure from 1.5, about 0.3 levels of number per level of light, is
  the measure of that unevenness. It is physics' known non-uniformity, not a failure of the form.

### Run 2 (10 October 2026): prediction, written before it ran (Tom: "yes")

Run 1 counted by light, mixing kinds and distances. Run 2 counts one kind at a time by its distance (parallax), inside
the volume where the kind is complete (MAG's ranges). For an even spread the number within d grows as d³: **3 levels of
number per level of distance**, the same fact as run 1's 1.5 per level of light, since light falls 2 levels per level of
distance. Past the disc's thickness the count grows as a slab's, toward 2. So within the disc's thickness the theory
gives 3, and the disc shows first toward the poles.

Same data and sha256; `dist`, `spect`, `ra`, `dec`; kinds parsed as in MAG; no variable stars. Slope of log₂ N(<d)
against log₂ d, least squares on cumulative counts at 0.05-level steps of distance.
- **P5 (G dwarfs, near).** G0–G5 dwarfs, 8 ≤ d ≤ 23 pc: the slope is 3 within 0.5. *Killed* if outside [2.5, 3.5].
- **P6 (K0 giants, within their complete range).** All sky, 40 ≤ d ≤ 140 pc: the slope is 3 within 0.4. *Killed* if
  outside [2.6, 3.4].
- **P7 (the disc, by distance).** K0 giants, 40 ≤ d ≤ 140 pc: the slope toward the poles (|b| > 30°) is lower than in
  the plane (|b| < 30°) by at least 0.15. *Killed* if not.
- **P8 (the kind alone, by light).** K0 giants within their complete volume (d ≤ 140 pc, V ≤ 7.3), counted by light: the
  slope is 1.5 within 0.25. The light slope is the distance slope halved, so a kind alone in its complete volume should
  give the even spread's value that run 1's mix did not. *Killed* if outside [1.25, 1.75].

Run 2 output (`python3 plans/cnt/cnt2.py`, in `plans/cnt/cnt-run2.txt`):

```
G dwarfs within 23 pc: 83; K0 giants within 140 pc: 535 (|b| < 30: 272, |b| > 30: 263; V <= 7.3: 432)
P5: not killed. G dwarfs, 8-23 pc: 3.471 levels of number per level of distance; 3 for an even spread
P6: KILLED. K0 giants, 40-140 pc, all sky: 2.583
P7: KILLED. K0 giants, 40-140 pc: |b| < 30 2.617, |b| > 30 2.555, difference 0.062
P8: KILLED. K0 giants within 140 pc and V <= 7.3, by light over V 3-7.3: 1.096 levels of number per level of light; 1.5 for an even spread
```

- **P5 not killed.** The G dwarfs within 23 pc give 3.47, inside [2.5, 3.5] but near its top; there are 83 stars.
- **P6 killed, just.** The K0 giants from 40 to 140 pc give 2.58, under 2.6.
- **P7 killed.** The plane and the poles differ by 0.06, under 0.15.
- **P8 killed.** By light, the K0 giants within 140 pc give 1.10, not 1.5.
- **A premise of this plan, and of MAG, is false.** Of the 535 K0 giants within 140 pc, 103 are fainter than V = 7.3,
  past Hipparcos's completeness. The plans took 140 pc as complete for K0 giants, assuming none is fainter than absolute
  V about +1.5. MAG's P4 already found the kind spread wider than that. So the volume is not complete. Its far part
  loses the faint members of the kind, which flattens the count by distance (P6), and still more by light (P8). Whether
  the disc shows (P7) cannot be read through that. MAG's P1 used the same range; its 1.93 may be flattened by the same
  loss, which is the direction it sat from 2.

### Run 3 (10 October 2026): prediction, written before it ran

The range is set by completeness itself, read from the data without any slope or absolute magnitude. The **complete
distance** of a kind is the largest d such that, among the kind's stars nearer than d, under 2% are fainter than V = 7.3.
Counting stops at the complete distance, from a floor of a quarter of it (two levels of distance).
- **P9.** For the K0 giants, the slope of log₂ N(<d) against log₂ d over that range is 3 within 0.4. *Killed* if outside
  [2.6, 3.4], or the range holds fewer than 100 stars.
- **P10.** Counted by light inside that complete sphere (V ≤ 7.3 and d under the complete distance), over its full range
  of V, the slope is 1.5 within 0.3. *Killed* if outside [1.2, 1.8].

Run 3 output (`python3 plans/cnt/cnt3.py`): the script stopped before P9, because no distance met the rule. Measured after,
the share of K0 giants fainter than V = 7.3, by distance:

```
within 30 pc: 7 K0 giants, 0 fainter than V 7.3 (0.0%)
within 50 pc: 36 K0 giants, 4 fainter than V 7.3 (11.1%)
within 70 pc: 96 K0 giants, 8 fainter than V 7.3 (8.3%)
within 100 pc: 228 K0 giants, 23 fainter than V 7.3 (10.1%)
within 140 pc: 535 K0 giants, 103 fainter than V 7.3 (19.3%)
```

- **P9 and P10 killed: the kind has no complete distance.** Already within 50 pc, 4 of 36 stars labelled K0 III are
  fainter than V = 7.3, the nearest at 43.7 pc and V = 8.53. A real K0 giant at that distance would be about V = 4. From
  50 to 100 pc the faint share stays near 10%, and by 140 pc it is 19%. Under the run's rule (under 2% faint) no range
  qualifies.
- **What the faint near ones are.** Most likely they are dwarfs labelled giants: a K0 dwarf at 43 pc is about V = 8.5.
  They could also be giants behind dust, or wrong parallaxes. The spectral label "K0 III" is not one kind. About one
  star in ten is something else, which also feeds the 1.4-level scatter MAG's P4 found.
- **So the count cannot be made clean on this label.** Counting by kind needs a cleaner kind. The candidates:
  - a cut on colour as well as the label;
  - the red clump, picked by colour and parallax, though that edges toward using distance to choose;
  - a catalogue with luminosity classes checked against parallax.

  Each would be a new run with its own prediction. CNT stops here for now.

## Reading of runs 2 and 3 (not ruled)

- **The near G dwarfs count as an even spread does**: 3.47 levels of number per level of distance, against 3 (83 stars,
  noisy, at its band's top).
- **For the giants, the counting test could not be run cleanly.** The label mixes kinds and the catalogue's limit cuts
  the far ones. The 2.58 by distance and the 1.10 by light measure the catalogue and its labels, not space.
- **Run 1's 1.2 is still open.** Its cause is somewhere among the disc, the dust, the young stars' clumping and the
  catalogue's own cut. Separating them needs cleaner kinds or a deeper catalogue (Gaia), and Gaia's archive is blocked
  here.
