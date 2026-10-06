# Three normalizations, and dividing by a noisy h

*6 October 2026, by Claude, at Tom's "proceed" after "Two normalizations, the two layings" (SPN §2.1): working up two
of the possibilities raised then. A reading, not a ruling. Checks: `python3 plans/normalizations/checks.py`.*

## 1. One relation, three normalizations

Divide a system (h, v) by three different things:

| divide by | gives | name elsewhere | lies on |
|---|---|---|---|
| h | s = v/h | **odds** | the number line, unbounded |
| the sum, v + h | p = v/(v + h) = s/(1 + s) | **probability** (the share of distance along the chord, SPN §2.1, "The first level is half the distance") | the straight chord from A to B, bounded |
| the whole, √(h² + v²) | g = atan(s)/(π/2) | **the circle's share** | the quarter circle, bounded |

Checked:

| s | odds | probability | circle's share g | log-odds, ln s |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | −∞ |
| ¼ | 0.25 | 0.200 | 0.156 | −1.386 |
| ½ | 0.5 | 0.333 | 0.295 | −0.693 |
| **1** | **1** | **½** | **½** | **0** |
| 2 | 2 | 0.667 | 0.705 | 0.693 |
| 4 | 4 | 0.800 | 0.844 | 1.386 |
| → ∞ | → ∞ | → 1 | → 1 | → ∞ |

- **The corner is the same in all three:** even odds, probability ½, the circle's share ½ (45°), log-odds 0.
- **All three are fair to the facings.** The flip s ↔ 1/s sends p to 1 − p and g to 1 − g, exactly (to 10⁻¹²), and
  sends the log-odds to its negative. Probability and the circle's share are the two bounded readings of one relation;
  odds is the unbounded one, and log-odds its additive form (SPN §2.1, "The relation forces the logarithm").
- **Statistics already works this way.** Odds and probability are the same quantity normalized by a part and by the
  whole, and the logit, ln(p/(1 − p)) = ln s, is the logarithm reading. This is standard; what the situated view adds is
  that dividing by a part needs only that part (h), while dividing by the whole needs both. A reader who knows only
  its h has the odds; the probability, like the circle, needs the whole.

### Two bells

On the log axis x = ln s, each bounded reading has a bell, its share per unit of x, both of area 1 (checked):

- the circle's: (1/π)·sech x, SPN's "parallel reader's bell";
- probability's: p(1 − p) = ¼·sech²(x/2), the **logistic** density.

Far out both **halve every doubling** (the circle's by 1.25, 1.70, 1.91, … → 2; the logistic's by 1.13, 1.39, 1.62, … →
2, more slowly). So both bounded readings give dyadic tails far from the corner; they differ near it. The normal curve,
for comparison, has no such tail (SPN §2.1).

## 2. Dividing by a noisy h

Take h = 1 and v = 1 (a reader at its corner), each with independent normal noise of spread σ, and read s = v/h.
Simulated, 2 million readings each (checked):

| σ | P(s > 10) | P(s > 100) | ratio per tenfold |
|---|---|---|---|
| 0.05 | none seen | none seen | |
| 0.2 | 4.0 × 10⁻⁶ | 5.0 × 10⁻⁷ | 8 |
| 0.5 | 2.25 × 10⁻² | 2.19 × 10⁻³ | 10.3 |

- **The tail falls tenfold per tenfold:** P(s > X) goes as 1/X, the Cauchy tail. This is the standard result for a
  ratio whose denominator can come near 0 (the ratio of two independent normals is Cauchy).
- **How much tail depends on how near h can come to 0.** At σ = 0.05 the denominator almost never gets there and no far
  readings appear; the tail is there in principle but with negligible weight.
- **So the horizon shows up as statistics.** A reader that divides by a noisy unit gets heavy tails, the far end of its
  number line, as a matter of course, and they are heavier the less sure it is of its own h. In the terms of SPN §2.1
  ("h as the focus"): an uncertain focus throws readings toward the horizon.

## What a lab could test

A *Wander* lab could give a reader a noisy h (its own unit measured with error) and predict, before running, that its
readings past the corner have a 1/X tail whose weight grows with the noise, while a reader normalizing by a known whole
shows none. Not built; it would follow the lab rules (prediction and kill condition first).
