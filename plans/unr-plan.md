# UNR: the unit rule's turns, against carries that model the payload

*Plan, 26 October 2026, SPN R509. Tom: "thats an interesting result considering our ofs paper.", then "yes" to a test
with its predictions written first. Predictions below are written before any run; nothing above "Runs" is edited after.*

## The question

*The Unit Rule* (archived; restated in `papers/unit-rule.md` §6–§7) measured two races. Tracking the level, a rule told
about the stream gained about 1.2×. Finding the stream's turns across gaps, the unit rule won by 7–14×. Read with OFS, this
is Theorem 6 in a stream: a turn is a crossing (order, the addresses), a carry that extrapolates is a model of the payload,
and order survives every change of payload while sums do not.

Those were the archived paper's numbers, not predicted from OFS beforehand. This plan predicts from OFS alone, then runs.

## Known beforehand

- The archived paper's tables (`papers/archive/the-unit-rule.md` §14a): unit rule 1.6–6.6% against trend 2–61% on its
  rod, decayed blend between.
- draw's REC lab (a serial record is scale-free and grain-free; cited in `plans/pay-plan.md`).
- Classical: the median commutes with every strictly increasing map, the mean only with affine ones (OFS Theorem 6(c));
  the second difference is the discrete curvature.

## Set-up

A **stream** is a sampled function x_n = x(n), n = 0 … N − 1, x > 0, with true turns at its local extrema (found on a
grid 1,000 times finer). A **pattern of looks** says which n are received. At each received look n, after the first
three, the reader compares the arrival with its **reference** ref_n, a function of what it received before n. Its
**sign** s_n = sign(x_n − ref_n). A **flip** is a change of s between two consecutive received looks; it is reported at
the later one. A flip is matched to the nearest true turn; the error is the distance in looks. A flip more than P/8 from
every turn is **false**; a turn with no flip within P/8 is **missed**.

Five references. With m the last received look, p the one before and g = n − m:
- **U**, the unit rule: x_m.
- **M**, median of the last three received values.
- **Ta**, additive trend: x_m + g·(x_m − x_p)/(m − p).
- **Tr**, ratio trend: x_m·(x_m/x_p)^(g/(m − p)).
- **E**, decayed blend: y updated at each received look, y ← y + α(x − y), α = 0.2; the reference is y before the update.

Streams (P = 200 looks a cycle unless stated, N = 4,000):
- **S1**, 2 + sin(2πn/P).
- **S2**, 0.2 + |sin(πn/P)|, a rod's extent, with a cusp at its low turns.
- **S3**, lopsided: 2 + sin(φ(n)) with φ = 2πn/P + 0.9·sin(2πn/P).
- **S4**, seeded: 3 + Σ_{j=1..4} a_j sin(2πn/P_j + φ_j), a_j uniform on [0.1, 0.5], P_j uniform on [80, 400], φ_j
  uniform; ten seeds.

Patterns: all looks; each look kept with probability 0.8, 0.5, 0.2 (seeded); bursts, 20% of looks lost in runs of 20 and
of 80 (seeded). Maps of the payload f: x³, √x, eˣ, ln(1 + x), and the world scaled, kx with k = 10⁻³, 7, 10³.

## Predictions

The OFS reading, in one line: a rule's flips are unchanged by exactly the maps of the payload its reference commutes
with. U and M hold order only (the addresses), so they commute with every increasing map; Tr holds a ratio's motion
(the levels), so it commutes with powers; Ta and E hold amounts, so they commute with affine maps only.

- **Q1.** U's and M's flips are identical under every f above, on every stream and pattern. *Kill:* any differing flip.
- **Q2.** Tr's flips are identical under x³ and √x, and differ under eˣ or ln(1 + x) on at least one stream and pattern.
  Ta's and E's flips differ under x³ on at least one. *Kill:* Tr changed by a power, or unchanged by both non-powers
  everywhere; Ta or E unchanged by x³ everywhere.
- **Q3.** Scaling the world (kx) changes no rule's flips, on every stream and pattern. *Kill:* any change. (So the scale
  test does not separate these rules; the order test does. This is 6(c), not 6(a).)
- **Q4.** With every look received, U finds every turn of S1–S3 within 1 look, with no false flips. Ta's flips sit within
  2 looks of S1's inflections (sin = 0), a quarter cycle from the turns: on S1 it finds no turn and every flip is false.
  Tr's flips on S1 sit within 2 looks of sin = −½, at least P/8 from a turn: none found. E's error on S1 is 3 to 5 looks
  (an exponential lag of (1 − α)/α looks seen at ωτ = 0.126, atan(ωτ)/ω ≈ 4.0). M's error on S1 is at most 2 looks.
  *Kill:* any clause off.
- **Q5.** On every noise-free stream and pattern, U makes no false flip, and its error at each turn is at most the sum of
  the two gaps either side of it (the received looks just before and just after the turn, in looks). *Kill:* a false flip,
  or one error past its bound. (Stated exactly: with m₁ the last received look before the turn and n₁ < n₂ the next two
  received after it, the bound is n₂ − m₁. A turn sharing [m₁, n₁] with another turn is excluded, and counted.)
- **Q6.** Under gaps, U's mean error is the least of the five on every stream at every pattern, or within 10% of the
  least. Ta's and Tr's are at least 3 times U's, counting a missed turn as P/8. *Kill:* either clause off on any
  stream and pattern.

## Not claimed

Noise is left out of this run: on a noise-free stream the comparisons are exact in double precision except for ties,
which are counted and reported. A run with noise (a threshold, the archived paper's lateness) is a later run with its own
predictions. These are synthetic streams, as the archived paper's rod was; the test is of the reading, not of any reader.

## Runs
