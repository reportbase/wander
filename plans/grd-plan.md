# GRD: the ratio between levels, in a measured reader (grid cells)

*Plan, predictions and kills written 10 October 2026, before any grid-cell data was in this environment (Claude; Tom:
"yes" to drafting a test of SPN's open question, the ratio 2 between levels, on a measured system). The lab rules hold:
nothing above the "Runs" line is edited after the run.*

## Why this system

SPN's deepest open question is why the levels are doublings (Appendix D). Proposition D.1: on a level with only its
ends, its order and its flip, the halving is the only subdivision the geometry supplies; any other ratio needs an added
measure. Physics has many hierarchies, but most have their ratio set by their own physics (harmonics give the musical
octave; Murray's law gives the airways' 2^(1/3)). A test needs a *reader* that lays levels of scale for itself.

The entorhinal grid cells are one. Each grid cell fires on a hexagonal lattice over the space an animal moves through.
The cells come in a few discrete **modules**, each with its own lattice spacing λ, and the spacings step up from the top
of the brain region downward by a ratio that has been measured. The modules are the animal's levels of detail of where
it is: discrete, nested, read together. The ratio between them is a measurement no physics law fixes.

## What is already known to me (stated so the test is not mistaken for blind where it is not)

From training, before this plan: Stensola et al. (Nature 2012) reported a mean ratio between adjacent modules of about
1.42 in rats, near √2, roughly constant from module to module; Barry et al. (2007) earlier reported about 1.7; a
theory of optimal grid coding (Wei, Prentice and Balasubramanian, eLife 2015) predicts about √e ≈ 1.65 in two
dimensions, or about 1.4 to 1.6 under its variants. I have not seen any per-animal data, and the run must use only data
not opened before the plan is committed.

## Keep the case

A spacing λ is an amount (cm). The ratio of two spacings, λ_{k+1}/λ_k, is a pure number: geometry, the same in any
unit. **The bridge** is the identification itself: *a grid module is one level of the reader's level of detail*. That
is the claim under test; nothing else crosses from fill levels to amounts, since only ratios are used.

## What the theory says, and the dimension it leaves open

SPN's levels are doublings of a one-dimensional reading: s = v/h, the next level nesting in the back half. A grid
module reads a two-dimensional place. The theory as written does not say whether a level of a map in two dimensions is
a doubling of its length or of its area (the room a cell holds):
- **length** (the reading counted along a line): λ_{k+1}/λ_k = 2;
- **area** (the room per cell, the lay's "room" of ISQ, counted in the plane): λ_{k+1}/λ_k = 2^(1/2) ≈ 1.414.

Either is a halving in D.1's sense, in its own dimension: 2^(1/D) with D = 1 or 2. Any other ratio needs a measure D.1
does not supply. Because of what is known above, the area reading must not be counted as a success of the theory on its
own: it was available to be chosen after the fact. It is written here as the theory's second reading, and the test is
whether the ratio is a halving *in either dimension* against the named alternatives, which differ from both by more than
the kill bands.

## The data (to be supplied)

Per-animal spacings of the grid modules, from a published dataset not yet opened here. Candidates, in order of
preference:
1. Stensola et al. 2012's per-animal module spacings (supplementary data), or any later release of them;
2. Gardner et al. 2022 (Nature, "Toroidal topology of population activity in grid cells"), rat recordings with several
   modules per animal, released on figshare;
3. any other published per-animal module spacings (mouse or rat), e.g. Giocomo-lab releases on DANDI.

Its source, licence and sha256 go here when it arrives, before the run. If the dataset is not the one named in an
earlier candidate, its choice is recorded with the reason, before opening it for anything but its column names.

**If the data gives modules** (each cell assigned a module by the authors): use the authors' assignment; each module's
spacing is the median spacing of its cells.

**If it gives only cells with spacings**, modules are found the same way for every animal, fixed now: sort the animal's
cells by log₂ λ, split wherever two neighbours differ by more than 0.25 levels, and keep groups of at least 5 cells.

**The ratio** for an animal with modules M1 < M2 < … is each λ_{k+1}/λ_k between adjacent modules. Pooled ratios are
combined by their geometric mean (the mean of log₂ ratio), with a bootstrap 95% interval over animals (10,000
resamples, seed 1).

**Seen while looking for data (10 October 2026, before any data was opened).** A web search summary quoted, from
arXiv 1405.0044 (which re-analyses the Sargolini et al. 2006 recordings), module spacings of about 46, 46 and 93 cm in
one rat and about 31 cm in another. So that dataset is not blind for those two rats, and the run prefers the others.
The same summary repeated Stensola's mean of about 1.42, already stated above. No other per-animal values were seen.
The code repository of Gardner et al. 2022 (github.com/erikher/GridCellTorus) was cloned to check whether it holds
data. It holds code and notebooks; the notebooks' outputs were not opened.

**Supplied (14 October 2026), recorded before the data was opened beyond its file listing.** This environment could not
reach the data sources on 10 October; Tom widened its network access on 14 October, and Tom said "ok" (about 15:22)
to running this test. Candidate 1: Stensola et al. 2012's supplementary material is a Materials and Methods PDF and a
PDF of Supplementary Figures 1–20 (from the article page's descriptions; neither opened), with no per-animal table, so
it gives no per-animal spacings to use. Candidate 2 is used: Gardner et al. 2022, figshare article 16764508
(doi 10.6084/m9.figshare.16764508.v6), licence CC0, one file `Toroidal_topology_grid_cell_data.zip`, 319.9 MB, md5
379bfdca61cd54d5f58cab9d3ba477de as listed by figshare; its sha256 is recorded under Runs once downloaded. The data is
spike times and tracked positions with the authors' module assignment, not spacings, so each cell's spacing is
computed, by a method fixed here before any value is seen:
- **Session.** Each rat's open-field sessions (no wagon wheel, no sleep); where a rat has more than one, its first in the
  dataset's own naming order.
- **Rate map.** Square bins of 2.5 cm over the tracked extent (positions taken as metres if their range is under 10,
  otherwise centimetres); spike counts and occupancy each smoothed by a Gaussian of σ = 2.5 cm; rate = counts/occupancy;
  bins with less than 0.1 s of smoothed occupancy left out.
- **Autocorrelogram.** Pearson correlation of the rate map with itself at every two-dimensional lag, over the bins valid
  in both, where at least 20 are.
- **Spacing.** Local maxima of the autocorrelogram (3 × 3 neighbourhood) with r > 0, the zero-lag peak excluded; the six
  nearest the centre; the cell's spacing is the median of their distances from the centre. A cell with fewer than six
  such maxima is left out.
- **Modules.** The authors' module assignment; each module's spacing is the median of its cells' spacings (as the plan
  says above); within a rat, modules are ordered by spacing.
What this dataset can and cannot test, from the paper as known before this plan (not from the data): it holds three rats, so P2 (at least 3
animals with three modules) and P3 (at least 5 with two) may fall to their own minimum counts; that is recorded as their
kill conditions say, not relaxed.

## Predictions

- **P1 (a halving, in one dimension or two).** The pooled geometric-mean ratio between adjacent modules is within 0.07
  of √2 (1.344–1.484) or within 0.07 of 2 (1.93–2.07). *Killed* if it is in neither band. The named alternatives fall
  outside both: √e ≈ 1.649, 3/2, 1.7 and e all kill P1.
- **P2 (the same ratio at every step).** For the steps M1→M2 and M2→M3 (pooled over animals with at least three
  modules), the geometric-mean ratios differ by less than 0.1 in log₂ (a factor of about 1.07). Levels laid by one rule
  step alike; a ratio that grows or shrinks down the axis is not a fixed level. *Killed* if the difference is 0.1 or
  more, or fewer than 3 animals have three modules.
- **P3 (no scale, only the ratio).** Across animals, the spread of the smallest module's spacing, as the standard
  deviation of log₂ λ₁, is larger than the spread of the ratio, as the standard deviation of log₂(λ₂/λ₁). The corner
  has no scale; the levels are set by ratio, while the absolute size is whatever the animal's body and world give it.
  *Killed* if the ratio's spread is the larger, or fewer than 5 animals have two modules.
- **P4 (distinct levels).** No pair of adjacent modules, in any animal, has a ratio under 1.2. *Killed* if more than
  5% of the adjacent pairs do (a split that the gap rule above made, or the authors made, between cells of one level).

## What would not be shown

- That the brain uses SPN's geometry. A ratio of √2 is also what an optimal-coding theory can give; P1 would show the
  ratio is a halving in the plane, not why.
- The dimension. If P1 lands on √2, "a level doubles a map's area" is a reading to be tested on a second reader whose
  map is one-dimensional (head-direction or time cells, if any have discrete modules), with its own plan.
- If P1 is killed near √e or 1.7, then this reader's ratio is set by a measure D.1 does not supply, as SPN's open
  question allows; it would be recorded as the ratio set "by the scene", as the earlier runs (why2, frc) found.

## Runs


### Run 1 (14 October; `python3 runs/grd/grd.py <data dir>`, 39 seconds)

Data: Gardner et al. 2022, figshare 16764508 v6, CC0; `Toroidal_topology_grid_cell_data.zip`, 319,902,753 bytes, md5
379bfdca61cd54d5f58cab9d3ba477de (matching figshare's listing), sha256
56842a7ae8e8f9144e390c9cdd72494d8ea2c48f2ce89cdee4780a49ed495372; not committed. Contents: rats Q (modules 1, 2),
R (modules 1, 2, 3; day 1 and day 2 files) and S (module 1), each an npz of spike times per cell by module and tracking
(x, y, t in metres and seconds), with a sessions file. Before the run, the method was checked on synthetic grids of
known spacing (35, 50, 71, 100 cm read as 34.0, 49.8, 71.2, 99.5). Set-up decided from the sessions files only, before
any value: rat R's open field lists valid-time windows, and only those windows are used.

```
rat Q: open_field_1 [(27826.0, 31223.0)], positions x100 to cm; spikes_mod1: 97 of 97 cells, spacing 68.0 cm; spikes_mod2: 66 of 66 cells, spacing 95.0 cm
rat R: open_field_1 [(7457.0, 14778.0), (14890.0, 16045.0)], positions x100 to cm; spikes_mod1: 166 of 166 cells, spacing 56.2 cm; spikes_mod2: 168 of 168 cells, spacing 83.6 cm; spikes_mod3: 149 of 149 cells, spacing 118.0 cm
rat S: open_field_1 [(9939.0, 12363.0)], positions x100 to cm; spikes_mod1: 140 of 140 cells, spacing 54.7 cm
adjacent ratios: {'Q': [1.397], 'R': [1.487, 1.412], 'S': []}
P1: not killed. pooled geometric-mean ratio 1.432 over 3 ratios from 2 animals (bootstrap over animals 95%: 1.397-1.449); bands 1.344-1.484 and 1.93-2.07
P2: KILLED. animals with three modules: 1 (needs 3); for information, log2 step difference [np.float64(0.075)]
P3: KILLED. animals with two modules: 2 (needs 5); for information, sd log2 lambda1 0.138, sd log2 ratio 0.045
P4: not killed. adjacent pairs under 1.2: 0 of 3
```

P1 not killed: the pooled ratio 1.432 lies in the √2 band, 0.018 from √2, and outside 2's; of the named alternatives
√e (1.649), 1.7 and e are far off, 3/2 is 0.068 away. P2 and P3 killed by their own minimum counts (one rat with three
modules; two with two), as the plan said they might be; for information only, both point the predicted way (rat R's
two steps differ by 0.075 in log₂, under 0.1; the smallest module's spacing spreads 0.138 in log₂ across the two rats,
the ratio 0.045). P4 not killed. Two animals make the bootstrap interval nearly meaningless; the run is weak evidence.

**Post hoc, not a test** (the method fixed rat R's first file; its second day was run afterwards, same method, to see
whether the spacings repeat): rat R day 2, open_field_1 (10617–13004 s): modules 53.0, 79.1, 90.2 cm, ratios 1.491 and
1.141. The first step repeats (1.487 on day 1, 1.491 on day 2); the second does not (1.412, 1.141), and on day 2 it would
fall under P4's 1.2. The tracked box is the same both days (148 × 147 cm and 156 × 146 cm; Q 146, S 143), and day 2 has
2,387 s of tracking against day 1's 8,476 s. Reading: the largest module's spacing, about 0.8 of the box, puts its six
autocorrelogram peaks where few bins overlap, and with less data the method finds nearer maxima; the method does not
measure the largest module reliably in a 1.5 m box. The ratios it measures reliably here are the two first steps,
1.397 (Q) and 1.487–1.491 (R), geometric mean about 1.44: still in the √2 band, from two rats.

**What it shows.** On the one per-animal dataset reached, the step between the two smaller grid modules is near √2 in
both rats that have two (1.40 and 1.49), as Stensola et al.'s mean of about 1.42 already said, and far from √e, 1.7 or
2; the third module cannot be measured reliably in this arena by this method. That is consistent with a halving of a
map's area, the plan's second reading, which was available to be chosen after the fact (the plan said so before the
run); it is not a test of the dimension, and two rats are not a population. P2 and P3 need more animals: a further run
needs a dataset with five or more animals with two modules (Stensola et al. 2012's recordings, if released, or the
Giocomo lab's on DANDI), with its own data section fixed before it is opened.

### Re-read, 22 October (GDR, `plans/gdr-plan.md`; SPN R439)
Appended; nothing above is changed. "Either is a halving in D.1's sense, in its own dimension: 2^(1/D)": OFS's lay doubles
distance, 2 in every dimension; √2 needs levels counted by area on a proportional (writer's) plane, which is itself an
added choice. The ratio is a reading, but the autocorrelogram method carries a bin, a smoothing and an occupancy floor and
holds only within a band of them (GDR P1 (b) killed: +0.13 at twice the scale, rat Q's small module 58 cm against 136);
run 1 sat inside the band. Five animals is the right size (GDR P4); only the step profile across six or more modules in
one animal tells √2, √e and the turn's layout (cosh-growing steps, flat over at most five modules) apart.
