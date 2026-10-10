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

