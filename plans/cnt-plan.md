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

