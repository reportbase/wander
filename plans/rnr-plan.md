# RNR: lay the range first, revisited (what the gap reads)

*27 October 2026. Tom: "yes, rule it and move to RNG". RNG (3 Oct, `labs.html`; SPN §4.2's "In a lab") is the earliest
test of what OFS now leads with, that the addresses are given before anything arrives and payloads are met
(R454, R458). It ran two readers on the same arrivals:
- **L** lays its range first, its corner at the middle of its laid addresses;
- **B** has only the addresses its arrivals make.

It found three things:
- L reads a shape's breadth ratio b as the gap between the arrivals' middle and its own corner (0.5000, 1.0000, 2.0001,
  4.0002 for b = ½, 1, 2, 4), and B reads 1 for every shape;
- L reads the dark (filled share 0.0478 against the world's 0.0476) and B has no empty entries;
- laying on arrival with the count unknown keeps two of order, place and evenness (SPN Proposition 5.4).

SPN already noted that the rival's failure is "by construction" and that optimality stays open. This revisit asks what
the gap reads, in OFS's terms, now that the Cauchy is the turn's and an arrival's direction is the payload's. Predictions
written before `runs/rnr/rnr.py` exists. Exact: mpmath at 50 digits; fractions for Proposition 5.4.*

## Known beforehand

- **RNG's set-up.** The arrivals are points (cos t, b·sin t) of a quarter ellipse, with t even over [0, π/2], seen from the
  ellipse's centre. So their directions are tan θ = b·tan t, and their median is at tan θ = b. The 3 Oct numbers are that
  identity counted on 2,000 arrivals in 10⁴ addresses.
- **OFS Theorem 6(a) and Proposition 8.** No address moves with what arrives; no reading gives a size. What a reading of
  arrivals can give is a ratio within the world (a shape), and only where something about the arrivals is known.
- **SRR** (R437): the median of what arrives is the payload's median direction; a corner is a median only under a
  reciprocal-symmetric law on what is counted.
- **POR P4(d)** (R439): a kind carried in (a known σ) is what lets totals give back a shape. A known kind is one of
  physics' bridges (CLAUDE.md).
- **payload-free.html** (R405): the turn's readings come back exactly whatever the world, and the median sits at the corner
  whatever paints the rays.

## The reading to test

In RNG's set-up, L's gap is **the median of the arrivals' directions read against a corner the turn gave beforehand**.
- That median is the payload's (where the arrivals fall), not the addresses'.
- It equals the shape's breadth ratio b only because the arrivals were spread evenly in the ellipse's own parameter t.
  That is a known kind carried in about how the world sends, not something the geometry supplies.
- Change how the arrivals are spread and the same shape gives a different gap.
- What laying the range first gives is the fixed thing to read against. L's addresses and corner are the same in every
  world; B has nothing that stays put.

## Predictions

Shapes b ∈ {¼, ½, 1, 2, 4}. Three ways the same quarter ellipse sends its arrivals:
- **(i) even in its parameter t:** RNG's law;
- **(ii) even along its arc:** equal lengths of outline;
- **(iii) even by turn from the centre:** the arrivals even in θ, as on the payload-free page.

L's addresses are K = 10⁴ even by turn over the quarter, its corner at the 5,000th boundary (θ = 45°).

- **Q1. L's addresses are the same in every world.**
  - L's boundaries and corner are fixed before anything arrives. They are identical, to the bit, across all 15 pairs of
    shape and spread and under scaling the world by k = 10⁻³ and 10³.
  - **Killed if** any boundary differs.
- **Q2. The gap is the median of the spread's directions, exactly.**
  - With tan θ_med the arrivals' median direction (as a continuous law, by root-finding to 10⁻⁴⁰), L's gap is
    tan θ_med / tan 45° = tan θ_med. For each spread:
    - **(i)** b exactly, for every b (RNG's result);
    - **(ii)** some g(b) that is neither b nor 1 for b ≠ 1, with g(1/b) = 1/g(b) (the exchange of the axes), g(1) = 1,
      and 1 < g(2) < 2;
    - **(iii)** 1 for every b: the arrivals then carry no trace of b in their median.
  - **Killed if** (i) misses b by 10⁻⁴⁰; (ii) has g(b) = b or g(b) = 1 for some b ≠ 1, or g(b)·g(1/b) misses 1 by 10⁻⁴⁰,
    or g(2) is outside (1, 2); (iii) misses 1 by 10⁻⁴⁰.
- **Q3. Scaling the world moves no gap.**
  - The ellipse's two breadths scaled together by k leave every arrival's direction, and so every gap, unchanged.
  - b is the shape's aspect, a ratio of two of the world's lengths; it is not V*/H.
  - **Killed if** any gap moves under k = 10⁻³ or 10³ (to 10⁻⁴⁰).
- **Q4. B reads 1 whatever the shape and the spread, by construction.**
  - B's only middle is its arrivals'.
  - **Killed if** B's reading is other than 1 in any of the 15.
- **Q5. Counted, L's gap carries the address grain and nothing else.**
  - With 2,000 arrivals per spread (as RNG), placed deterministically at the spread's quantiles, and L's K addresses, the
    counted gap misses the exact median by at most the width of one address there (the cell's width in tan θ).
  - **Killed if** the miss exceeds one cell at any b and spread.
- **Q6. Proposition 5.4, exactly.**
  - (a) Taking addresses one per arrival, each past the last and never moved, in a bounded span: the gaps tend to zero.
    Checked on the sequence 1 − 2^(−n): gap 2^(−n−1).
  - (b) Placing by halving (van der Corput, base 2) never moves an address. It is even exactly at every count 2^m, and at
    2^m + 1 it is not. Its order of placement is not its order in the span from the third address on.
  - (c) Re-laying evenly at every arrival keeps order and evenness and moves addresses: the place of the first address
    changes at every count n ≥ 2.
  - **Killed if** any of these fails in exact fractions, for m up to 10 and n up to 1,025.

## Runs

(none yet)
