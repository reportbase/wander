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

### Run 1 (26 Oct; `runs/unr/unr.py`, output `runs/unr/unr-run1.txt`)

One fix before any result: a numpy boolean subtraction raised a TypeError on the first call (the sign is now
`int(d > 0) - int(d < 0)`), and the median of three is taken by comparisons rather than `np.median`, for speed.

**Q1 killed.** U's flips changed under √x in 1 of 78 cases, M's under √x and ln(1 + x) in 3 each; none under x³ or eˣ.
**Q2 not killed.** Tr unchanged under x³ and √x in all 78 cases, changed under eˣ (73) and ln(1 + x) (72); Ta changed
under x³ in all 78, E in 67. **Q3 killed.** Ta's flips changed under kx in 5, 9 and 7 cases; no other rule's. **Q4
killed**: U on S3 worst 1.05 looks (not within 1); E on S3 up to 5.05 looks (not within 5). The other clauses held: U
found every turn of S1–S3 with no false flip, Ta's 39 flips on S1 within 2.00 looks of the inflections and Tr's 40 within
1.67 of sin = −½, neither finding a turn of S1, M's worst 2.00. **Q5 killed**: U had false flips and missed turns in 20 of
78 cases (19 of them bursts of 80 or keep 0.2, and S4.8 at every pattern), none past its bound. **Q6 killed** at keep 0.2
on five streams (Ta 2.0–2.9 × U); held at every other pattern, U the least of the five everywhere.

### After run 1 (post hoc; `runs/unr/unr1-posthoc.py`, `runs/unr/unr1-posthoc.txt`)

- Q1 and Q3 by my set-up. Every comparison whose sign a map or a scale changed had an original difference of at most
  2.2·10⁻¹⁶ of the arrival, or exactly 0: ties in double precision (158 exact ties in the run). √x and ln(1 + x) round
  differently from x itself near a tie; Ta's second difference passes through zero at every inflection, at rounding size.
  Mathematically U and M commute with every increasing map and every rule with kx; the floats do not keep the ties.
- Q4 by my set-up and my arithmetic. A turn between two looks puts U's flip up to 2 looks after it (S3, 0.953–1.047), so
  "within 1" held only for turns on a look (S1, S2: exactly 1.000). E's reference is the blend before the update, a look
  later than the continuous lag I used: S1 5.000 exactly, S3 4.953–5.047, S2 4.0–5.0 (the cusps).
- Q5 by my scoring. The P/8 window pairs a flip with its nearest turn; a turn inside a burst of 80 is flipped up to 80
  looks later, outside the window, and scored false and missed. S4.8's one false flip at every pattern is at look 4, from
  a turn before the first comparison. Attributing each U flip to the last turn before it: all 3,836 flips within their
  turn's bound n₂ − m₁, none with no turn before it; 13 turns with two flips, every one a burst holding two turns (both
  flipped at its end) or, once, a min and a max in consecutive intervals (each flipped once, the first credited to the
  second); 2 turns with none, the same cases. No false flip in any case.
- Q6 stands as killed: at keep 0.2, Ta and Tr miss nearly every turn, scored P/8 each, and U's own error is 5–7 looks, so
  the ratio could not reach 3. Ta and Tr missed most turns at every pattern (means 12.7–25 against U's 1.3–7.2).

What run 1 shows of the reading: the maps each rule's flips are unchanged by are the maps its reference commutes with,
exactly as predicted, but floating-point ties hide it. U and M (order) are unchanged by every increasing map, Tr (the
ratio's motion) by powers and not by eˣ or ln(1 + x), and Ta and E (amounts) by neither. Every rule passes the scale test
alike, so it is the order test (6(c)) that separates them, not the scale test (6(a)).

### Run 2: predictions (written after run 1, before run 2)

Run 2 repeats Q1–Q3 and Q5 with run 1's set-up errors removed: mpmath at 60 digits, a difference under 10⁻⁴⁰ of the
arrival counted as a tie (a tie is unchanged by every increasing map), and each U flip attributed to the last turn before
it. To keep it short: N = 1,000, streams S1–S3 and S4.0–S4.3, the same six patterns (seeded as run 1, on the first 1,000
looks), the same maps. Q4 and Q6 are not repeated: their numbers have been seen.

- **Q1′.** U's and M's flips are identical under x³, √x, eˣ and ln(1 + x), in every case. *Kill:* any differing flip.
- **Q2′.** Tr's identical under x³ and √x in every case, different under eˣ and ln(1 + x) in at least one each; Ta's and
  E's different under x³ in at least one. *Kill:* any clause off.
- **Q3′.** Every rule's flips identical under kx, k = 10⁻³, 7, 10³, in every case. *Kill:* any differing flip.
- **Q5′.** Every U flip has a turn before it and lies within that turn's bound n₂ − m₁; every turn whose received
  interval holds no other turn gets exactly one flip. *Kill:* one flip or one such turn off.
