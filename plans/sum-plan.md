# SUM: a sum of Cauchys, read as addresses

*18 October 2026 (Tom's local date). Tom: "what I'm not aware of is somone makng the clear and definitive statement that
cauchy is address, not payload. that is not a small distinction. that is everything."; then "It would be well known, if it
was know. we have done that search before."; then "yes" to two pieces: the rule stated plainly in OFS (done in §7.2: "a
Cauchy variable is a direction … never an amount"; "find the turn, and find the amount"), and the hard case worked
prediction-first. The hard case: a sum of independent Cauchy variables is again Cauchy (Lévy), which looks like adding
amounts. Exact mathematics and a seeded simulation; no physics.*

## The guess, withdrawn before any run

In conversation Claude guessed that the geometry reads a sum of Cauchys as composing directions, by tangent addition
(OFS §2, R327). Writing this plan, before any computation, that guess fails on its face. With X₁ = tan θ₁ and
X₂ = tan θ₂, θ uniform, the composed direction is tan(θ₁ + θ₂) = (X₁ + X₂)/(1 − X₁X₂). Its angle is uniform again, so
it is a standard Cauchy, scale 1. But X₁ + X₂ is a Cauchy of scale 2. So the sum is not the composition. The guess is
recorded here as withdrawn; P2 below checks the numbers.

## Known beforehand

These are classical, and are not tested as new:
- A Cauchy of centre m and scale γ is the landing point on a line of a uniform turn from the point (m, γ) above it. That
  is the lighthouse, and the Poisson kernel of the half-plane.
- Its characteristic function is e^{imt − γ|t|}, so independent Cauchys add their centres and their scales (Lévy). In
  complex form the point z = m + iγ adds (McCullagh 1996).
- A planar Brownian motion started at height γ lands on the line at a Cauchy of scale γ (harmonic measure). Watched at
  the times it first reaches each lower level, its horizontal place is the Cauchy process (Spitzer 1958).
- The mean of n standard Cauchys is a standard Cauchy.
- Normalized sums of symmetric variables whose tails fall as 1/x² tend to a Cauchy: the stable law of index 1.

## The reading, before the run

A sum of Cauchys is a relay of addresses: one turn's landing taken as the next standpoint's foot. Each summand is a
direction read in one chart: the landing of a uniform turn from a standpoint a height γᵢ above the line.

Relay two such readings. From a standpoint at height γ₁ + γ₂, turn uniformly and land on the line at height γ₂. From
that landing, now a standpoint γ₂ above the line, turn uniformly again and land on the line. Where it lands is X₁ + X₂.
- The reading's claim is that this is one uniform turn from height γ₁ + γ₂, not two.
- What adds is the standpoints' heights γᵢ (and feet mᵢ). These are amounts: the distance of a standpoint from the
  line, the payload's side.
- The sum itself stays a direction from the combined standpoint, read by its order. It still has no mean.

So the rule holds: in a sum of Cauchys, the turn is the combined standpoint's uniform turn; the amounts are the heights.

The stable limit is the case where no turn is visible in the summands. There the reading says the turn is in the limit
object: the Cauchy process is the horizontal place of a planar Brownian motion at the times it first reaches each level
(Spitzer). The summands themselves need not be directions; only the limit is.

### Predictions

- **P1 (the relay is one turn).** With γ₁ = 1 and γ₂ = 2:
  - exactly: the characteristic functions multiply to e^{−3|t|}, which is that of a uniform turn from height 3, at 200
    digits for t ∈ {0.1, 0.5, 1, 2, 5};
  - by simulation (seeded, 10⁶ draws each): the two-stage relay of uniform turns, from height 3 to height 2 to the line,
    and one uniform turn from height 3 have quartiles within 0.01 of ±3, and their Kolmogorov–Smirnov distance is under
    0.003.
  - *Killed* if either fails.
- **P2 (the sum is not tangent addition).** For γ₁ = γ₂ = 1 (seeded, 10⁶ draws):
  - the quartiles of X₁ + X₂ are within 0.01 of ±2;
  - those of (X₁ + X₂)/(1 − X₁X₂) are within 0.01 of ±1.
  - *Killed* if either fails.
- **P3 (averaging addresses gains nothing).** The mean of n standard Cauchys has quartiles within 0.01 of ±1, for
  n = 1, 10, 1000 (seeded, 10⁵ draws each). That is a relay from height n, rescaled by 1/n back to height 1.
  - Its spread does not fall as n grows.
  - *Killed* if any n's quartiles leave ±1 by more than 0.01.
- **P4 (the stable limit, the turn in the limit object).**
  - Normalized sums Sₙ/n of n symmetric variables with P(|Y| > y) = 1/y for y ≥ 1 (density 1/y², each sign alike; the
    centring is zero by symmetry) come close to the Cauchy of scale π/2.
  - The scale follows from tails c/y² on each side with c = ½: γ = πc. The Kolmogorov–Smirnov distance to Cauchy(0, π/2)
    falls with n: 0.02 or less at n = 1000 (10⁵ draws).
  - A planar Brownian motion started at height π/2, simulated in steps of 10⁻³ (10⁴ paths), lands with quartiles within
    0.05 of ±π/2.
  - *Killed* if the distance does not fall, or the landing quartiles miss.
- **P5 (the verdict).** A judgment, not a number: in every case above a turn and an amount can be named. The turn is
  the uniform turn from the combined standpoint (P1–P3) or the Brownian landing (P4). The amount is the heights. And no
  case has the Cauchy variable adding as an amount.
  - *Killed* if some case leaves no turn to name. Then the rule as written in OFS §7.2 needs narrowing, and I say so.

P1–P4 are classical, so a kill would be my set-up. P5 is the reading.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (18 Oct, `python3 sum/sum.py`; output `sum/sum-run1.txt`, 4 s)

- **P1 killed.**
  - The characteristic functions agree exactly (difference 0 at 200 digits).
  - The relay's quartiles are −3.0102 and 2.9924, against one turn's −2.9911 and 3.0021. The two-sample KS distance is
    0.00257.
  - The relay's lower quartile misses ±3 by 0.0102.
- **P2 not killed.** X₁ + X₂ has quartiles −1.9957 and 2.0022. Tangent addition has −0.9999 and 1.0030.
- **P3 killed.** The mean's quartiles, by n:

  | n | lower | upper |
  |---|---|---|
  | 1 | −1.0100 | 1.0062 |
  | 10 | −1.0049 | 0.9935 |
  | 1000 | −0.9952 | 1.0187 |

  n = 1's and n = 1000's miss ±1 by more than 0.01.
- **P4 killed.**
  - The KS distance of Sₙ/n to Cauchy(0, π/2) was 0.0068, 0.0019 and 0.0044 at n = 10, 100 and 1000. It did not fall
    at every step.
  - The stepped Brownian motion was not run as written: its hitting time has no mean, about 5.5·10⁶ steps a path at the
    median. The script used the exact construction instead (hitting time h²/Z², place √τ·N), quartiles −1.5748 and
    1.5609.

**Every kill is my set-up.** A sample quartile of a Cauchy of scale γ from M draws has standard error
2πγ·√(3/(16M)). That is 0.0082 at γ = 3 with M = 10⁶, and 0.0086 at γ = 1 with M = 10⁵. A tolerance of 0.01 is little
more than one standard error. P4's "falls at every step" asked for a difference below the KS noise floor, about
0.87/√M = 0.0027 at M = 10⁵. Every number agrees with the classical laws within its noise.

### Run 2: the thresholds in standard errors (written before it runs)

The same script and draws, with fresh seeds. Each threshold is now set by its noise:
- **Quartiles.** A quartile is within 3 standard errors, 3·2πγ·√(3/(16M)), of ∓γ.
- **Two-sample KS.** Below the 1% critical value, 1.63·√(2/N).
- **One-sample KS.** Below 1.63/√M.

The predictions:
- **P1′.** The relay and the one turn from height 3 each have quartiles within 3 standard errors of ±3, and their
  two-sample KS distance is below 1.63·√(2/N).
- **P2′.** X₁ + X₂ has quartiles within 3 standard errors of ±2, and tangent addition within 3 standard errors of ±1.
  These are scales 2 and 1, so the two are 2·γ standard errors apart, and the sum is not the composition.
- **P3′.** The mean of n has quartiles within 3 standard errors of ±1 at n = 1, 10 and 1000.
- **P4′.**
  - At n = 1000 the one-sample KS distance to Cauchy(0, π/2) is below 1.63/√M: consistent with the limit.
  - At n = 10 it may exceed that; no claim is made for n = 10.
  - The Brownian landing from height π/2, by the exact construction, has quartiles within 3 standard errors of ±π/2.
- **P5** as written.

*Killed* as before, with these thresholds.
