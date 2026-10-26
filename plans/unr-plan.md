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

### Run 2 (26 Oct; `runs/unr/unr2.py`, output `runs/unr/unr-run2.txt`)

Nothing killed. 42 cases (7 streams × 6 patterns), 143 ties in the unmapped streams, each unchanged by every map.
**Q1′:** U and M changed by none of x³, √x, eˣ, ln(1 + x). **Q2′:** Tr changed by neither power, by eˣ in 37 and
ln(1 + x) in 36; Ta by x³ in 42 and √x in 36; E by x³ in 28 and √x in 15. **Q3′:** no rule changed by kx.
**Q5′:** 511 flips, every one within its turn's bound n₂ − m₁, every lone turn flipped exactly once.

## What UNR says

A carry's turns are unchanged by exactly the changes of payload its reference commutes with. The unit rule and the
median of three hold order only, so no strictly increasing change of what arrives moves a turn they report. The ratio
trend holds the ratio's motion, so powers leave it and other maps move it. The additive trend and the blend hold
amounts, so every non-affine map moves them. On noise-free streams the unit rule reports every turn once, with no false
flip, within the two received intervals after it, whatever the gaps; the trend rules report inflections or the zeros of
(ln x)″ instead, a fixed fraction of a cycle off (run 1 Q4).

So the archived paper's 7–14× is not a matter of tuning. It is Theorem 6(c) in a stream: the turn is an order statistic of
the arrivals, and a reference built from amounts answers a different question. The scale test (6(a)) does not separate the
rules (every one is homogeneous); the order test does.

Standing: exact on synthetic noise-free streams; the archived races were on recorded signals with noise and a threshold,
which this does not test. Next, with its own predictions: noise and a threshold (the archived lateness, threshold over
slope), and a recorded signal.

### Run 3: predictions (26 Oct; Tom: "proceed"), written before run 3

Noise, and a threshold to declare a turn. A threshold is a size, so it brings an amount back into the reader; OFS says
which maps of the payload each kind of threshold keeps. Three turn detectors, each holding one value and a direction bit:
- **D** (order only): a turn when the sign of arrival − hold has been opposite to the direction for m = 3 received looks
  running; the hold is the last arrival (the unit rule).
- **UT** (a threshold in levels): the hold moves to the arrival when |ln x − ln hold| > T; a turn when it moves against
  the direction bit. T = 0.01, 0.03.
- **UA** (a threshold in amounts): the same with |x − hold| > T_a, T_a = 0.02, 0.06 (the same sizes on S1's scale, x ≈ 2).
Streams S1–S3 and S4.0–S4.3; patterns as before. Noise multiplies each sample by e^(σz), z standard normal, seeded,
σ = 0, 0.002, 0.005; the maps act on the noisy samples. Turns are matched to the last true turn before them, as Q5′.

- **R1.** D's turns are unchanged by x³, √x, eˣ, ln(1 + x) and kx, with and without noise, in every case (60 digits).
  *Kill:* any change.
- **R2.** UT's turns are unchanged by kx in every case, and changed by x³ or √x in at least one; UA's are changed by kx
  in at least one. *Kill:* any clause off. (With a threshold, the scale test separates levels from amounts (6(a)), and
  the order test still separates order from both (6(c)).)
- **R3.** Without noise and with every look received, UT's lateness at each turn of S1 lies between
  √(2T/κ) − 1 and √(4T/κ) + 1 looks, κ = |(ln x)″| at the turn: the hold sits within T of the extreme when it turns, and
  the arrival must fall T below the hold. *Kill:* a turn outside.
- **R4.** With noise, UT makes no false turn (a turn with no true turn since its last one) at T ≥ 8σ, on every stream
  and pattern; at T = 2σ (T = 0.01, σ = 0.005) it makes false turns. *Kill:* either clause off. (A false flip needs the
  noise of two looks, sd σ√2, to pass T: about e^(−T²/4σ²), 10⁻⁷ at 8σ.)

Not predicted, measured: the mean lateness of D, UT and UA under noise and gaps.

### Run 3 (26 Oct; `runs/unr/unr3.py`, output `runs/unr/unr-run3.txt`)

One fix before R4's results: the float path raised run 1's numpy boolean TypeError (`int(x > h) - int(x < h)` now); R1–R3
had printed and came out the same on the rerun.

**R1 not killed.** D (order only) changed by no map and no kx, in all 126 cases, with and without noise. **R2 not
killed.** UT changed by no kx in any case, by x³ and √x in all 126; UA changed by kx in all 126. **R3 not killed.** On
S1, T = 0.01: maxima 9.00 looks late (bound 6.80–12.03), minima 5.00 (3.50–7.37); T = 0.03: 17.00 (12.50–20.10) and 8.00
(6.80–12.03); 40 of 40 turns. **R4 killed**: UT made "false" turns (no true turn since the turn before) with no noise
(12 at T = 0.01, 14 at 0.03), and 14 at T = 0.03, σ = 0.002 (15σ); the other clause held (3,779 false at T = 2σ).

Measured, not predicted (all patterns, seven streams): mean lateness with no noise D 7.40 looks, UT 11.42 and 18.32, UA
10.65 and 16.69. With noise D's false turns rise to 101 (σ = 0.002) and 456 (0.005), UT 0.03's stay at 14, UT 0.01's
reach 3,779 at σ = 0.005, UA 0.02's 8,680.

### After run 3 (post hoc; `runs/unr/unr3-posthoc.py`, `runs/unr/unr3-posthoc.txt`)

R4 by my definition. Every "false" turn without noise is at a burst of 80: the burst hides a turn not yet reported (the
report is late by up to 18 looks) and the next, so both reports come just after it, the second with no new true turn
since the first. Counted cumulatively (a report false only if the reports up to it outnumber the true turns before it),
UT's excess is 0 at σ = 0 and 0.002 for both T, 0 at T = 0.03, σ = 0.005 (6σ), and 5,613 at T = 2σ. The cumulative count
is weaker (a false report could hide behind a missed turn); with every look received S1 lost none (R3).

## What run 3 says

A threshold is an amount, and OFS's separation says which maps it costs. The order-only debounce keeps every increasing
change of the payload, with noise; a threshold in levels keeps only the scale of the world; a threshold in amounts keeps
neither. So with a threshold the scale test (6(a)) separates levels from amounts, and the order test (6(c)) separates
order from both, as R1–R2 predicted. The price is noise: the order-only debounce makes false turns once the noise is a
few percent of a look's change (101, 456), the level threshold none at five times the noise or more. Holding order alone
is free of the payload and not free of the noise; buying noise robustness spends some invariance, and the unit in which
the threshold is written decides which.
