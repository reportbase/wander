# OMP: Ω or π, sorted blind

12 Nov 2026. SPN R917. Tom: "ok, lets turn our attention to more tests.", then "1" (this test).

## The question

R916 writes *Reads and Writes* in Ω (= π/2) where it helps and π where it does not: Ω for one sweep, π for a whole
turn, a whole line and the classical statements. Is that rule a fact about where each constant comes from, or a matter
of taste? If it is a fact, a result's π should be helped by Ω exactly when that π comes from one quarter turn, and a
judge who knows nothing of the rule should be able to say which results those are.

## What "helped" means (fixed before any result is seen)

Each result is reduced to one constant of the form c·π^k, with k a non-zero rational and c > 0 with c² rational (so c
may carry a square root, as 1/√(2π) does). Results whose π appears in a sum of terms (1 − π/4) or inside a
transcendental function are excluded and counted, not scored.

With π = 2Ω the same constant is c′·Ω^k, c′ = c·2^k. Its size is S = H(c²), the larger of numerator and denominator of
c² in lowest terms; in Ω, S′ = H(c′²). **Ω helps when S′ < S**, hurts when S′ > S, ties when equal. (2/π: S = 4,
S′ = 1, helps. 1/π: S = 1, S′ = 4, hurts. π²/6: S = 36, S′ = 9, helps.) The metric is mechanical; the script computes
it from (c², k) alone.

## Procedure

1. A fresh agent (A) gathers about 40 standard results from across mathematics, physics, probability and engineering
   whose closed form contains π as one monomial c·π^k, with a one-line derivation each and the place in the derivation
   where π enters. It is told nothing of this corpus, of Ω, of sweeps or of the rule; it is asked for variety and told
   to include results whose constant is π, 2π, π/2, 2/π, 1/π, √π and powers of π.
2. A second fresh agent (B) is shown A's list with the constants removed (the derivation step kept) and asked, for each,
   where π enters: (Q) one quarter turn, an angle running from 0 to a right angle, or a slope or ratio running from 0
   to infinity; (T) a whole turn or a closed circle (0 to 2π, a full period, a full disc or sphere, a Gaussian's angle);
   (L) a whole line or a half turn (a ratio from −∞ to ∞, 0 to π, a semicircle); (O) other, with a note. B is told
   nothing of Ω, of the metric or of the predictions.
3. The script `runs/omp/omp.py` computes S and S′ for every result and crosses them with B's classes.

## Predictions (written before step 1)

- **O1. Ω helps the quarter turn.** Of the results B puts in Q, at least 80% are helped by Ω. Killed below 80%.
- **O2. Ω does not help the whole turn or the whole line.** Of the results B puts in T or L, at most 20% are helped.
  Killed above 20%.
- **O3. The sort is not trivial.** Q holds at least 8 results and T ∪ L at least 8. If not, the test is void (no kill,
  no pass), and a second list is gathered.
- **O4. Most of the effect is one factor of 2.** Among the results O1 and O2 score, the helped ones are those whose
  coefficient c carries 2^(−k) or a higher power of 2 against π's exponent (Q's 2/π, ½Ω² for π²/8), and the hurt
  ones those with no factor of 2 to absorb (1/π, π, √π). Not a kill condition; reported, since it says what the test
  measures: whether the factor of 2 beside π tracks where π came from.

## Known beforehand

- *Reads and Writes* and essay 21 (this corpus) already rewrote about a hundred constants; I know which were helped
  there (the half-Cauchy, the odd sums, Wallis) and which were not (the standard Cauchy, the Gaussian, Euler). A's list
  is meant to be mostly new; overlaps are marked in the results.
- TWC (`plans/twc-plan.md`, R834) killed "π exactly when a turn is taken whole" as a rule for where π appears: π
  showed up in ζ(2) and ζ(4) cases with no turn taken. O1–O2 ask a narrower thing: not whether π appears, but which
  coefficient it carries.
- Basel's π²/6 is helped (S 36 → 9) though its sum runs over a whole line of integers; the paper reads ζ(2)'s π as the
  quarter turn's (the odd sums ½Ω², R836). B's class for it, whatever it is, is scored as given.

## Runs

### Run 1 (12 Nov 2026)

`runs/omp/list.tsv` (41 results, gathered by agent A from its own knowledge, no repository or web; every constant
checked here against c·π^k to 10⁻¹²), `runs/omp/blind.tsv` (constants removed), `runs/omp/classes.tsv` (agent B's
classes), `runs/omp/omp.py`, output `runs/omp/run1.txt`.

B's classes: Q 5, T 27, L 9, O 0.

| class | n | Ω helps | tie | hurts |
|---|---|---|---|---|
| Q | 5 | 3 (60%) | 0 | 2 |
| T | 27 | 8 (30%) | 1 | 18 |
| L | 9 | 6 (67%) | 0 | 3 |
| T ∪ L | 36 | 14 (39%) | 1 | 21 |

- **O3: void.** Q holds 5, under the 8 required. By the plan no kill and no pass on O1 and O2.
- Scored anyway, for the record and not as a verdict: O1 would be killed (60% < 80%) and O2 would be killed (39% > 20%).
  The two Q misses are the sinc² integral (π, over the whole line in A's derivation) and the arcsine density (1/π);
  the T and L hits are mostly 2/π and √(2/π): averages over a half turn (Buffon, the semicircle law, the rectified
  sine, |sin| on [0, π]) and the Gaussian's half-line moments (the median's efficiency, E|Z|, √(8/π)), plus ζ(2) and
  ζ(4).
- **O4**, as reported: by the metric's construction Ω helps exactly when c carries a factor 2^(−k); what the run shows
  is that this factor of 2 does not follow B's source classes. It follows something else: whether the constant is a
  *mean or share over half of a range* (a half turn, a half line, the odd terms of a sum) against a *total over the
  whole* (the circle's 2π, the sphere's 4π, the Gaussian's √(2π), the standard Cauchy's 1/π). That reading was formed
  after seeing the table and is not tested here.

**Standing.** Void by its own condition. Not a pass: on this list the factor Ω removes does not track "one quarter
turn" as B judged it, and the quarter turn is rare in standard results (5 of 41). A second list, as the plan says,
would need its Q count fixed in advance (for example by asking A for at least 12 results whose derivation runs over a
right angle or 0 to ∞), which no longer leaves B's sort fully blind to the aim; and the post hoc reading above (half of
a range against the whole) would need its own predictions and class definitions before it is run.
