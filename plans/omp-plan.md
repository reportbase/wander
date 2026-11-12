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

(none yet)
