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

### Run 1 (8 October, `python3 plans/frc/frc.py`): P1 not killed

| operations | interior points named on a level | ratios between adjacent levels | ratios, level to descendant | not a power of 2 |
|---|---|---|---|---|
| **base** (flip, its fixed point, nesting), depth 6 | 1 (the corner, ½) | **2** | 6 (2 to 64) | **0** |
| + a free number (c = 0.37), depth 3 | 3 | 2.70, 7.69 | 9 | 9 |
| + a root, depth 3 | 7 | 4.83, 6.03, 6.29, … | 120 | 120 |
| + arithmetic, depth 2 | 25 (capped) | 16, 24, 32, 48, … | 28 | 19 |
| + the sweep's constant (2/π), depth 3 | 3 | 2.75, 7.32 | 9 | 9 |
| no fairness (no flip), depth 6 | 0 | none: nothing to nest in | none | — |

- **P1 not killed.** From the flip, its fixed point and nesting alone, the only interior point a level names is its
  corner; adjacent levels stand in ratio 2, and every ratio to a descendant is a power of 2.
- **P2, reported.** Each added operation opens ratios that are not powers of 2, and dropping fairness leaves no interior
  point to nest in, as predicted. Two of P2's specific figures did not appear as stated:
  - *a root*: √2 itself is not among the ratios. √½ is named, but further roots name points between it and its
    neighbours, so the part it bounds is subdivided; the ratios carry √2 in other forms (4.83 = 2 + 2√2).
  - *arithmetic*: 3 itself is not among the ratios, though ratios with a factor 3 are (24 = 3 · 8, 48). The script capped
    the named points at 400, keeping the smallest, a fault of my set-up that cut off points near 1; the arithmetic row is
    incomplete, and "every rational ratio" is not shown. A fix would be a new run with its own prediction.
- **No symmetry at all** was not run: with every point fixed, every point is named by definition.

**What it says.** The bookkeeping holds: with the operations the sketch says the geometry supplies, the levels come out
dyadic and nothing else; each other ratio enters with an operation the sketch says is supplied at runtime (a chosen number,
a root, counting, a constant). It is a check of the sketch's arithmetic, not a proof: the premise that the geometry
supplies only the flip, its fixed point and nesting is what a proof must defend, and the run cannot.

### Run 2: the arithmetic row without the cap (prediction written 8 October, before run 2; Tom: "yes, run frc")

Run 1 capped each level at 400 named points, keeping the smallest, which cut off points near 1 (my set-up). Run 2 drops
the cap and bounds the work another way: points are kept as exact fractions, arithmetic runs two rounds, and a point whose
denominator exceeds 64 is dropped. Ratios are kept as exact fractions, and their prime factors reported. The base and the
other rows are rerun with exact fractions where they can be (the root and 2/π rows stay in floating point).

**Informed by run 1, and said so.** Run 1's P2 said 3 itself would appear with arithmetic. It cannot appear between
adjacent levels: ⅓ is named, but so is ¼, which cuts the part [0, ⅓]. The prediction is restated as a factor.

- **P1 (the kill, again).** The base alone gives only powers of 2, now checked with exact fractions, to depth 6.
- **P2a (a kill for my account of arithmetic).** With arithmetic, ratios with a prime factor other than 2 appear, and 3
  is among those factors. Killed if no ratio has a factor of 3: then arithmetic on named points does not open the ratios I
  said it does.
- **P2b (reported).** Which primes appear with arithmetic; and, for the root row, which forms √2 takes among the ratios.
