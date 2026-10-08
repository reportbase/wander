# FRC: which ratios between levels can be precomputed?

*Plan, prediction and kill written 8 October 2026, before the script was written or run (Claude; Tom: "to prove 2 is
forced, we must show that every other number is not pre-computable", and "yes" to running a check). It tests the route
to forcing 2 sketched in SPN's central open question ("A route to forcing 2"). The lab rules hold: nothing above the
"Runs" line is edited after the run.*

## What this can and cannot show

It is a bookkeeping check, not evidence about readers. It builds every point a level can name from a stated set of
operations, and lists the ratios between a level and the levels nested in it. It shows which operation each ratio needs.
Whether the geometry supplies only the base operations is the premise a proof must defend; the run cannot settle it.

## The model

A level is the place interval [0, 1]: home at 0, the far wall at 1 (SPN, "2h in place"). Its **named points** start as
{0, 1}. A nested level is the part of a level between two adjacent named points, rescaled to [0, 1]. The **ratio** of a
nesting is the parent's length over the part's. The ratios reported are those between a level and every level nested in
it, to depth 6.

**Base operations** (what the sketch says the geometry supplies):
- **the flip**, f ↦ 1 − f, applied to named points;
- **fixed points of the level's symmetries**: with fairness to the facings (R162) the symmetries are the identity and the
  flip, whose fixed point is ½;
- **nesting**: a part between adjacent named points becomes a level, with its own named points by the same rules, pulled
  back into the parent.

**Added operations** (each run alone on top of the base):
1. **a free number** c = 0.37, a cut chosen from outside;
2. **a root**: √p for every named p;
3. **arithmetic**: sums, differences, products and quotients of named points that land in (0, 1);
4. **the sweep's constant**: 2/π, as a cut;
5. **no fairness**: the symmetries are every order-preserving projective map fixing both ends (f ↦ f/(f + c(1 − f)),
   c > 0), with no flip;
6. **no symmetry at all**: the identity only, so every point is fixed.

## Prediction

- **P1 (the kill).** With the base operations alone, every ratio between a level and a level nested in it is a power of
  2, and the ratio between adjacent levels is 2. No other ratio appears, to depth 6.
- **P2 (reported, not a kill).** Each added operation opens ratios the base does not:
  - a free number: 1/c and 1/(1 − c), any ratio at all;
  - a root: √2 (from √½), and further roots;
  - arithmetic: 3, since ⅓ is a quotient of named points ((¼)/(¾)), and in time every rational ratio;
  - the sweep's constant: π/2;
  - no fairness: no interior point is fixed, so no level can be nested at all;
  - no symmetry: every point is fixed, so every ratio is available.

## Kill

**P1 killed** if any ratio other than 2ᵏ appears from the base operations alone. That would mean the base already names a
non-dyadic point, and the sketch's step "the only free cut is at the corner" is wrong.

## Runs
