# BLD: building π and e from counts of reads

15 Nov 2026. Tom: "Maybe we can reverse the derivation, build e and pi, from multiple reads", then "Yes".
SPN R1009. Exact arithmetic. Committed before any run.

## The question

`plans/discussion-note.md` item 18 read the classical π–e cancellations as the blueprint's way back to points a read
already has (+1, i, −1). Reverse it: start from reads and counts only, with no π, e, angle or trigonometric function
in the construction, and see what the counts tend to. By R890 and R922 no count, finite or carried to a limit, *makes*
the blueprint's π or e. What is tested is how fast the counts close in on them and from which side.

## The construction

**π along the turn.** One small read, slope 1/m. Composing it with itself by tangent addition is multiplying the
Gaussian integer h + iv by m + i (the pair [h : v], no division). Start at home, [1 : 0]. Count the reads until the
pair passes the horizon, i.e. the first n with Re((m + i)ⁿ) ≤ 0. Call it N(m). The candidate: 2N(m)/m → π. Found by
binary search on n using exact powers; the search uses only that the real part stays positive before the horizon,
the fact a read has (each composition turns the same way).

**e along the scale.** One small step, a fixed share 1/m of what is held, repeated m times: E(m) = (1 + 1/m)ᵐ =
(m + 1)ᵐ/mᵐ, an exact fraction. The candidate: E(m) → e.

**Both on one road.** The same N reads of slope 1/m, unnormalized, (1 + i/m)^N: its length is the scale part the
turn carries with it (ELM's θ²/(2n)). Its log length times m should go to π/4.

The referee (only to score, never in the construction): mpmath at 60 digits for π, e and logarithms.

m in {1, 2, 3, 5, 7, 10, 30, 100, 300, 1000, 3000, 10⁴, 3·10⁴, 10⁵}.

## Predictions (written before any run)

- **B0 (method).** N(m) from the integer search equals the referee's ⌈π/(2·arctan(1/m))⌉ at every m.
- **B1.** For every m ≥ 2: 0 < N(m) − πm/2 < 1 + 1/m.
- **B2.** For every m ≥ 2: 0 < 2N(m)/m − π < 2/m + 2/m². π approached from above only.
- **B3.** Re((m + i)^N) is exactly 0 only at m = 1 (N = 2, two corner reads, i·i = −1). At every other m the horizon
  is passed, not landed on (Niven).
- **B4.** For every m ≥ 2: 0 < e/2 − m·(e − E(m)) < 1.25/m. So e − E(m) ≈ e/(2m), approached from below only.
- **B5.** For every m ≥ 10: |m·(N/2)·ln(1 + 1/m²) − π/4| < 1/m.

Kill condition: any of B0–B5 false at any m in its range. A killed prediction stays killed; a fix is a new run.

## Runs

(below this line, nothing above is edited)
