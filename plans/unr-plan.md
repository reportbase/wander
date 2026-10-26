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

### Run 4: predictions (26 Oct; Tom: "yes", to a run on a recorded signal), written before any data was fetched

**The signal.** NOAA CO-OPS water level, verified six-minute heights (`product=water_level`, `units=metric`,
`time_zone=gmt`), at San Francisco (9414290, mixed tides) and Boston (8443970, semidiurnal, a range near 3 m), for
September 2026; if NOAA has not yet verified September 2026 at either station, September 2025 at both, decided on the
API's answer before any value is looked at. Each fetched in two datums, MLLW and STND (the station's own zero), the same
heights a constant apart. The independent turns are NOAA's verified highs and lows (`product=high_low`, MLLW), from
their own fit to the six-minute series, not from mine. Heights are read as whole millimetres (integers), so a datum
shift is exact. Looks missing from the verified series are left out (a real gap); a look's index is its minute over 6.
Licence: U.S. Government work (public domain); source, retrieval date and sha256 of each file recorded below; the data
not committed.

**The detectors** (run 3's, unchanged): D, order only, M = 3; UA, a threshold in amounts, T_a = 30 and 100 in the
numbers' own unit (mm as fetched); UT, a threshold in levels on ln(x + 2 m) with x in MLLW (the 2 m keeps it positive),
T = 0.01 and 0.03. Every look (6 min), and every third look (18 min). Lateness of a report: the minutes from the last
NOAA turn before it, over 6. A report is in excess (run 3's cumulative count) when the reports up to it outnumber the
NOAA turns before it. A NOAA turn is missed when no report falls after it and at or before the next NOAA turn.

**Predictions.**
- V1. D's turns are unchanged, at both stations and both rates, by the datum (MLLW to STND), by feet (× 3.28084) and
  by (x + 5 m)³. Killed if any turn moves.
- V2. UA's turns are unchanged by the datum and changed by feet in at least one of the eight cases (two stations, two
  rates, two T_a). UT's are unchanged by feet with its 2 m converted too (ln(3.28084(x + 2)) has the same differences)
  and changed by the datum shift (ln of the STND height + 2 m) in at least one case. The split of run 3, on a recorded
  signal: order keeps every increasing map, amounts keep a shift, levels keep a scale. Killed if any clause fails.
- V3. At 6 min D has an excess above 0 at both stations (the millimetre rounding and the harbour's own short waves
  turn the order often); UA 100 and UT 0.03 have none. Killed otherwise.
- V4. UA 100's median lateness at 6 min is 5 to 15 looks at each station (estimated from x near a turn,
  A − Aω²t²/2: √(2T/Aω²) to √(4T/Aω²) with A 0.5–1.5 m, ω = 2π/124 looks, about 6 to 14). Killed outside.
- V5. D's excess at 18 min is at most a quarter of its excess at 6 min at each station (the tide's change per look
  triples, the noise does not). Killed if more.
- V6. Every NOAA turn that UA 100 misses (6 min) has a range to one of its neighbouring NOAA turns under 250 mm.
  Killed by one that does not.
- V7. For the NOAA turns UA 100 reports at both rates (the first report after each), the two reports lie within 18 min
  of each other for at least 90% of them, at each station. Killed below.

### Run 4 (26 Oct; `runs/unr/unr4.py`, output `runs/unr/unr-run4.txt`)

Data, retrieved 26 Oct 2026 from `https://api.tidesandcurrents.noaa.gov/api/prod/datagetter` (format csv, gmt, metric,
1–30 September 2026). September 2026 was verified at both stations (every row flagged `v`), so no fallback; 7,200 looks
each, none missing; NOAA's highs and lows, 116 at each. STND − MLLW exactly 1,822 mm (San Francisco) and 1,074 mm
(Boston) at every look.

| file | sha256 |
|---|---|
| `wl_9414290_MLLW_2026.csv` | `3eb5429bc5766f09a426d6ca298483ad7dc69011540d8e776beb063a273dbcd1` |
| `wl_9414290_STND_2026.csv` | `f0a9bfc16c4b1954f8b5aef84bb91ff72aad1604d0fbe931360913c1f96830f4` |
| `hl_9414290_MLLW_2026.csv` | `4b03d2e8e04b13ae30558be7166db241a4fd02c3e6b655f27fb56e20184e1faf` |
| `wl_8443970_MLLW_2026.csv` | `8547da683536d9dc4a9703c3f47ef40c963dc204885f079687d4be9bbdcd84c0` |
| `wl_8443970_STND_2026.csv` | `573a98bb0abf7eaa8cb46cce6a7d022e3c09849f89e7f3663e6b18888062397f` |
| `hl_8443970_MLLW_2026.csv` | `5dbe3aadc437163f43260ffceb5deb602ba9f52e4f826c76da719be5e11a1498` |

**V1 not killed.** D's turns the same under the datum, feet and (x + 5 m)³ at both stations and both rates. **V2 not
killed.** UA's unchanged by the datum in all 8 cases and changed by feet in all 8; UT's unchanged by feet in all 8 and
changed by the datum in all 8. **V3 killed**: D's excess at 6 min is 116 at San Francisco but 0 at Boston. **V4 not
killed**: UA 100's median lateness 14 looks (San Francisco), 9 (Boston). **V5 not killed**: D's excess at 18 min 0 at
both. **V6 killed**: Boston's first NOAA turn, a lower low 18 minutes into the month (range to the next 3,033 mm), missed
by UA 100 (and by every detector). **V7 killed**: at San Francisco 91 of 115 (0.791) within 18 min, the largest gap 15
looks; Boston 109 of 115 (0.948).

Measured, not predicted: D, with no threshold, reported exactly one turn between each pair of NOAA turns at Boston at
6 min and at both stations at 18 min, with median lateness 3 looks (Boston, 6 min), 10 and 9 (18 min), the least of any
detector at that rate.

### After run 4 (post hoc; `runs/unr/unr4-posthoc.py`, `runs/unr/unr4-posthoc.txt`)

V6 by my set-up: the turn was 18 minutes after the series began, before any detector had a direction to turn from; "a
NOAA turn missed" should have started at the second turn. Excluding it, nothing was missed with a range of 250 mm or
more.

V3 by the station, and my cumulative count overstated what it did find. Counted per interval between NOAA turns, D at
San Francisco at 6 min made 17 extra reports in 12 of 117 intervals and none in 6. Once one early extra report gets
ahead of the turns, the cumulative count marks every later report until a turn is missed, hence 116. The extras sit
by the mixed tide's small, flat turns and its 6-minute wiggles; Boston's tide changes enough per look that the order
never wavered.

V7 by my reasoning. I took the coarser rate to cost at most one coarse look. The hold, though, is set at whichever look
crosses T, so where it sits below the peak (anywhere in [peak − T, peak]) differs between the rates, and so does the
drop needed to report: a spread of √(4T/κ) − √(2T/κ), the same as V4's band. On San Francisco's slow small turns (κ
small) that is 4–9 looks. 18 of its 24 gaps over 3 looks have the 18-min report later.

## What run 4 says

On a recorded tide, with its own rounding and short waves, the separation held exactly. The turns read by order alone
are unchanged by every increasing change of the numbers (the datum, the unit, a cube). The turns read with a threshold
in amounts keep the datum and lose the unit. Those read with a threshold in levels keep the unit and lose the datum.
Which changes a reading survives is set by the unit its threshold is written in, as in run 3, now on data no one made
for the test.

The noise is where the reader looks from. Order alone was the earliest and exact wherever the tide changed more per look
than the water wiggled: Boston at 6 min, both stations at 18 min. Where it did not (San Francisco at 6 min), it made
extra reports. Looking less often bought order back with no threshold: a rate is a choice of looks, not an amount. A
threshold buys robustness at any rate, at the price of an invariance and of lateness.

### Run 5: predictions (26 Oct; Tom: "yes", to predicting when order alone is exact), written before any data was fetched

Run 4 found, unpredicted, that D (order only, M = 3, no threshold) reported exactly one turn between each pair of NOAA
turns wherever the tide changed more per look than the water wiggled between looks. Run 5 predicts that from the record
before the detector is run, and varies the rate of looking.

**The signal.** NOAA CO-OPS one-minute water level (`product=one_minute_water_level`, MLLW, metric, gmt; preliminary, the
only one-minute product), NOAA's one-minute harmonic predictions (`product=predictions`, `interval=1`), and NOAA's
verified highs and lows (`product=high_low`), September 2026, at Honolulu (1612340, a small range), Seattle (9447130,
strongly mixed), Los Angeles (9410660, a harbour with short waves), San Francisco (9414290) and Boston (8443970). A station
without one-minute data or verified highs and lows for the month is dropped and said so; if fewer than three remain,
August 2026 for all. Heights in whole millimetres; missing minutes left out. Source, licence (public domain), retrieval
date and sha256s recorded; the data not committed.

**Looks.** Every r minutes, r in {1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30}, from every offset 0 … r − 1. D is
**exact at r** when, at every offset, it reports exactly one turn between each pair of consecutive NOAA turns (the stretch
before the first NOAA turn and after the last left out).

**The prediction, from the record alone** (computed and committed before D is run):
- The noise between looks: s_r, the standard deviation of res(t + r) − res(t), res = observed − predicted (one-minute).
- Each NOAA turn's sharpness: from its two legs (range R, duration τ), κ = (R/2)(π/τ)² for each, averaged; κ_min the
  flattest turn's.
- The flat zone: near a turn the tide changes κ·t·r a look at t minutes from it, under the noise s_r for |t| < s_r/(κ r),
  2·s_r/(κ r²) looks. D's three opposite signs can be noise there. **r_low**: the smallest grid r with
  2·s_r/(κ_min r²) ≤ 3.
- The shortest leg: D reports a turn 2 to 3 looks after it, so a report reaches its own interval only while
  3r < τ_min, the shortest time between consecutive NOAA turns. **r_high**: the largest grid r with 3r < τ_min.
- Predicted: D exact at every grid r from r_low to r_high, and at no other.

**Kill conditions.**
- W1. At each station the smallest rate at which D is exact lies within a factor 2 of r_low (if r_low ≤ r_high). Killed
  by a station outside it, or one never exact where the window is not empty.
- W2. Where r_high < 30, the largest exact rate lies within a factor 2 of r_high; where r_high ≥ 30, D is exact at 30.
- W3. The exact rates are one unbroken run on the grid at each station.
- W4. Where the predicted window is empty, D is exact at no rate.

**Side prediction: temperature.** NOAA air temperature (`product=air_temperature`, six-minute, metric) at Boston for
September 2026 (San Francisco if Boston has none), in tenths of a degree C as integers; °F computed exactly as
F × 100 = 18·C₁₀ + 3200 (not NOAA's separately rounded °F); K and °R likewise exact. Every look and every third.
- T1. D's turns are the same in °C and °F (an increasing map).
- T2. UA, a threshold of 0.5 in the numbers' own unit, changes from °C to °F in at least one of the two rates.
- T3. UT, a threshold of 0.003 in levels on the absolute temperature, is the same in K and °R (a scale).
- T4. UT, the same threshold on ln(reading + 50) in the units reported, changes from °C to °F in at least one rate (a
  shift and a scale together: neither amounts nor levels keep it, only order).

**Amendment, written after the fetch and before any number below was computed.** All five stations have one-minute
data for September 2026, so none is dropped. Los Angeles misses 7,421 of 43,200 minutes, many in runs of hours; the others
7 to 87, the longest 68 minutes. A gap of hours hides whole turns, so D could not be exact there at any rate. The rule:
an interval between consecutive NOAA turns is scored only if it and the interval before it hold no gap longer than 30
minutes; shorter gaps are simply looks not received. s_r is taken over pairs of minutes both present. κ and τ come from
NOAA's turns, unaffected. The counts of intervals scored are reported per station.

### Run 5 (26 Oct; `runs/unr/unr5.py`, outputs `runs/unr/unr-run5-predict.txt`, committed before D was run, and `runs/unr/unr-run5.txt`)

Data, retrieved 26 Oct 2026 from `https://api.tidesandcurrents.noaa.gov/api/prod/datagetter` (csv, gmt, metric, MLLW;
one-minute water level and one-minute predictions fetched in four-day pieces and joined; air temperature six-minute,
Boston). Public domain. Every station had one-minute data, so none was dropped; the gaps are in the amendment above. Not
committed; sha256 of each joined file:

| file | sha256 |
|---|---|
| `om_1612340.csv` | `0aaeb26262bb1757f25bd22a3f972213ef8e94ec787d5cd7ea5cf4e19a97904c` |
| `pr_1612340.csv` | `9a15444641920501305ad6754ac6b2ab07253a5c6e93d70b7d1e81e9ad79407c` |
| `hl_1612340.csv` | `77def9b5c6ba2b04a418e9a3b05db6851713a98c87a3d358b4eafd3c6ef990b1` |
| `om_9447130.csv` | `b3a7a6d3a199a9158f7bb4305da0a6c004f422a69b485b478ac6b81765ca8301` |
| `pr_9447130.csv` | `c0f607e2f6d878decf4f61f9c0c671903051072473b30bead1d1f2844578db4c` |
| `hl_9447130.csv` | `631cd840032e688cf7df51ccb73248d84a100c0cc91e997d798a1d02f889898f` |
| `om_9410660.csv` | `49f52e81a8e51cb4a59b6a40fcec9a73f930951bd287ab3d2d3288aa3adb6d8c` |
| `pr_9410660.csv` | `ece7d6b84411f8a20697b121996ba95ad7da5a24aa0bb059bb312ad0b95d298c` |
| `hl_9410660.csv` | `31960992ddd7a27f5ace3618bac7a1e30480d6035ef7a5c69ab0baee2e0008df` |
| `om_9414290.csv` | `4b1357c28e4398073b04916851f1ff4bf86b9bd1b67bbfbfa9acae2433f52529` |
| `pr_9414290.csv` | `b2adf82266ab44a167f25efe3aeb0c8b19dbac455c98043042c6c55e649d28dd` |
| `hl_9414290.csv` | `4b03d2e8e04b13ae30558be7166db241a4fd02c3e6b655f27fb56e20184e1faf` |
| `om_8443970.csv` | `ebe519765c1f6786da4c3d0a5c3794ea9f0856f8129f730690a24fce490b8f3e` |
| `pr_8443970.csv` | `8deea187b55706fb1bc266d492fec654b786a240be3de8e8a1efc74175f2fdb9` |
| `hl_8443970.csv` | `5dbe3aadc437163f43260ffceb5deb602ba9f52e4f826c76da719be5e11a1498` |
| `at_8443970.csv` | `005aaa9f339c37c86fce78d2dde1cba6363dabe2bf0b63d63d1c507bdb6baa1d` |

Predicted (from the record alone): Honolulu and Los Angeles exact at no rate, Seattle and San Francisco at 30 min only,
Boston at 20, 24 and 30. Measured: Honolulu and Los Angeles at none; Seattle at 6 to 30; San Francisco at 20, 24, 30;
Boston at 10 and 12.

**W1 killed** by Seattle, exact from 6 min against r_low 30. **W2 killed** by Boston, not exact at 15 to 30. **W3 not
killed**: the exact rates one unbroken run at every station. **W4 not killed**: Honolulu and Los Angeles exact at no rate
(Los Angeles exact at 7 of 30 offsets at 30 min). San Francisco matched (20 against r_low 30, and 30).

**T1–T4 not killed** (Boston air temperature, 7,184 looks; 190 order turns every 6 min, 119 every 18): D's turns the
same in °C and °F; UA 0.5 changed; UT on K and °R the same; UT on reading + 50 changed, at both rates.

One fix before the side prediction printed: my °R line named the wrong variable (a NameError); D's results came out the
same on the rerun.

### After run 5 (post hoc; `runs/unr/unr5-posthoc.py`, `runs/unr/unr5-posthoc.txt`)

W2 by my set-up. Boston's slow-rate misses are all but one the interval after its first NOAA turn, a lower low 18
minutes into the month (run 4's V6 again): at a slow rate no look falls before it, so D has no direction to turn from.
My gap rule scored that interval because the stretch before the first turn had no gap. Left out (every station's
first interval), Boston is exact at every rate from 5 to 30 min: W2 holds, but its smallest exact rate, 5 against r_low
20, is a factor 4, so Boston too would kill W1. Seattle and San Francisco are unchanged by it (6 and 20).

W1 by my model of the noise. Seattle's two-leg κ is right (a parabola fitted ±30 min at its flattest turn gives 0.0185
against 0.0198), and the noise is in the water, not the predictions (second differences 34 mm observed, 0.7 predicted).
What my rule got wrong is what noise does to order. The flat zone treated each look as a coin toss, but D reports a turn
only after three steps the same way in a row. Noise that is new every minute (white) makes three falls in a row 1 time in
24; Seattle's and Boston's s_r are nearly flat in r (19.7 to 25.9, 27.5 to 38.5), so their noise is close to white, and D
was exact from 6 and 5 min. Noise
that keeps its direction for minutes (a seiche, a harbour's slow wiggle) makes three in a row easily: San Francisco's,
Honolulu's and Los Angeles's s_r roughly double from 1 to 30 min. So what fools order alone is how long the wiggle holds
its direction, against the look, not how large it is.

## What run 5 says

Where the noise held its direction for several minutes, the flat-zone rule was right: Honolulu and Los Angeles never
exact, San Francisco exact from 20 min, as predicted. Where the noise was new every minute (Seattle, Boston) it was too pessimistic, by a factor 4 to 5 in the rate,
because order is not fooled by noise that doesn't keep a direction. The reader's one setting, how often to look, works by
looking past the wiggle's own persistence: the right rate depends on how long the noise keeps its sign, not on its size.
The temperature check repeats run 4's split on a shift and a scale together: only order keeps °C to °F.

### Run 6: predictions (26 Oct; Tom: "yes", to a rule from the noise's persistence, calibrated on September and tested on August), written before the rule was calibrated or any August data fetched

Run 5 found, after the fact, that what fools D is noise that keeps its direction for three looks, not noise that is
large. Run 6 states that as a rule with one constant, fits the constant on run 5's September record (seen, so used only
to fit), and predicts August 2026 at the same five stations from August's own record before D is run on it.

**The rule.** At a rate r (looks every r minutes, from every offset):
- res = observed − predicted (one-minute, mm); its increments between consecutive looks present.
- q_r: the share of places where three consecutive increments have one sign (zeros break a run), averaged over offsets.
  It is 1/12 for noise new at every look; noise that keeps its direction raises it.
- For each scored NOAA turn i (its interval and the one before free of gaps over 30 min; **every station's first
  interval left out**, run 5's set-up kill): κ_i from its two legs as in run 5, s_r as in run 5, and its flat zone
  Z_i = min(2·s_r/(κ_i r²), τ_i/r) looks, τ_i the interval it reports into.
- E_r = q_r · Σ_i Z_i, the expected number of false three-runs near turns in the month.
- **D exact at r** predicted when E_r < c and 3r < τ_min.

**Calibrating c** (on September only): for each station and grid rate, E_r and run 5's measured exactness with the first
interval left out (Boston 5–30, Seattle 6–30, San Francisco 20–30, Honolulu and Los Angeles none). If the exact and
inexact (station, r) pairs are separated by E_r, c is the geometric mean of the largest E_r among the exact and the
smallest among the inexact; if not, the c (from the observed E_r values' geometric midpoints) misclassifying fewest pairs,
ties to the smaller c. c and its misclassifications are committed before August is fetched.

**The August test.** NOAA one-minute water level and one-minute predictions, and verified highs and lows, 1–31 August
2026, the same five stations (a station without verified highs and lows for August is dropped and said so). Sources and
sha256s recorded, not committed. The predicted exact rates per station committed before D is run.
- X1. At each station, the smallest exact rate measured lies within a factor 2 of the smallest predicted; a station
  predicted never exact is exact at no rate, and one predicted exact somewhere is exact somewhere.
- X2. At each station, the predicted and measured exactness agree at 11 or more of the 13 grid rates.
- X3. The measured exact rates are one unbroken run at each station (W3 again).

### Run 6 (26 Oct; `runs/unr/unr6.py`, outputs `runs/unr/unr-run6-calibrate.txt` and `runs/unr/unr-run6-predict.txt`, each committed before the next step, and `runs/unr/unr-run6.txt`)

Calibration (September, run 5's record): **the rule did not separate** exact from inexact; the best c, 52.7, still
misclassified 17 of 65 (station, rate) pairs, all of Seattle's and Boston's exact rates but 30 and three of Los Angeles's
inexact ones. q_r rose with r at Seattle and Boston (to 0.52 and 0.40): the increments keep their sign over hours. As the
protocol said, c was committed and August predicted with it anyway.

August data, retrieved 26 Oct 2026 from the same API (MLLW, metric, gmt; one-minute in four-day pieces, joined). Every
station had verified highs and lows, none dropped; Los Angeles misses 14,300 of 44,640 minutes (the gap rule as in run 5).
Public domain, not committed:

| file | sha256 |
|---|---|
| `om_1612340.csv` (Aug) | `c537ac5fb71cb77878dcd4dd50311ffe52ac990f0b2447f2c834c4db13c8f7bd` |
| `om_9447130.csv` (Aug) | `fdb638e696e6b8666bccda2f4c138129eaa1dad7bbbfefd79f77c4da376e35c2` |
| `om_9410660.csv` (Aug) | `04b4817f553e87069e7605dbfcef36655694269ed105fcec290d90ec51f991e3` |
| `om_9414290.csv` (Aug) | `125c1508b54b9e784db8fd2b1fe9e7076880437aaf04cbd5978b4d6d5302944c` |
| `om_8443970.csv` (Aug) | `53cc83c8bd19da949f8ea26948fc19d44fe5836342d926cc12938256d039a7bb` |
| `pr_1612340.csv` (Aug) | `d069a081b241aea6fc5e2352a9a462fd98d667881a4857fc8ff14a46b312835b` |
| `pr_9447130.csv` (Aug) | `f027d72b52fc76fda72ab9436cf7caf788ddbd472cd8417e0a5608345c7893c0` |
| `pr_9410660.csv` (Aug) | `30ef4a9a4a466e1510acdd016a1e11ec1086aab287ad3f5e05bbcde73c90f6ae` |
| `pr_9414290.csv` (Aug) | `53bf51e1ac6dd2c89aadef45ffd009e328a496298a2f51ba75533de7b518ebdc` |
| `pr_8443970.csv` (Aug) | `ab74d2865e77f33cf9cc5e59c1d44bd782e1d1819f26ced35357757b5ebb8916` |
| `hl_1612340.csv` (Aug) | `d030a0cb7f06816c6f03304d1038c248f89a4ca1ae78328e6a4c3110650d57a6` |
| `hl_9447130.csv` (Aug) | `e721c0919802b8944fd873f2042a056cf3005f219724b0ec2a02d9a891f71327` |
| `hl_9410660.csv` (Aug) | `4c1c2d413638c50128c87faa992410d5e05df5c1cb978548bdda8b428ad8170b` |
| `hl_9414290.csv` (Aug) | `f93ab97374dc6f6f5d8f4e293714d0d3ac57c32be32f2e83e75fac1b8cf47460` |
| `hl_8443970.csv` (Aug) | `f79c5ec5373c076484e1563c85b6ba868a5da3eae9cd3ab3e28092df3e1116a2` |

Predicted (August's own record, c from September): Honolulu 30; Seattle 24, 30; Los Angeles 15–30; San Francisco 20–30;
Boston 24, 30. Measured: Honolulu and Los Angeles none; Seattle 6–30; San Francisco 12–30; Boston 10–30.

**X1 killed** at four stations of five (San Francisco held: 12 against 20). **X2 killed**: agreement 12, 7, 9, 11 and 9 of
13. **X3 not killed**: each station's exact rates one unbroken run.

Measured, not predicted: the stations kept their behaviour from September to August. Honolulu and Los Angeles were exact at
no rate in either month, Seattle from 6 min in both, San Francisco from 20 and then 12, Boston from 5 and then 10.

### After run 6 (post hoc; `runs/unr/unr6-posthoc.py`, `runs/unr/unr6-posthoc.txt`)

The rule counted the wrong persistence. Its q_r is high wherever the residual has a slow surge, and a surge keeping its
sign for hours only shifts a turn a little; it cannot make three false steps against the tide. Split by running means,
the residual's fast part (under 10 min) is largest at Boston (18 mm) and its slow part largest there too, yet Boston is
exact early. The band between, 10 to 60 minutes (a harbour's seiches), over the tide's median sharpness κ orders the
stations as their exactness: Seattle 58 and 35 (Sept, Aug), Boston 89 and 84, San Francisco 151 and 167, Los Angeles 347
and 265, Honolulu 340 and 333. A reading from five stations and two months, after the fact; a candidate for run 7, not
a result.

## What run 6 says

A rule written from one month's hindsight did not survive the next month: the persistence it measured was the slow
surge's, which order alone does not mind. What the two months do show is that each station's behaviour is its own and
stable, and that it lines up with the wiggle in the 10 to 60 minute band against how sharp the tide turns. The reader's
setting, how often to look, is set by the part of the noise that lives at the scale of a few looks near a turn, which is
not the fastest part and not the slowest.

### Run 7: predictions (26 Oct; Tom: "yes", to predicting from the 10–60 minute band on a fresh month), written before the rule was fitted or any July data fetched

**The predictor.** B = sd(band) / κ_med (minutes², roughly): band the residual (observed − predicted, one-minute)
smoothed over 10 minutes less the same smoothed over 60 (running means, a window kept where 80% of its minutes are
present), κ_med the median two-leg sharpness of the scored turns (as in runs 5–6, first interval left out, the 30-minute
gap rule).

**The rule, fitted on September and August (runs 5–6, seen, used only to fit):**
- never exact (at any grid rate to 30 min) when B > B*, B* the geometric mean of the largest B among station-months
  exact somewhere and the smallest among those exact nowhere;
- otherwise exact from r_pred = a·B, a the geometric mean of (smallest exact rate)/B over the station-months exact
  somewhere, taken to the grid rate nearest in log, and up to the largest grid rate with 3r < τ_min.
B* and a are committed before July is fetched.

**The test: July 2026**, the five stations of runs 5–6 and five not used before: The Battery, New York (8518750),
Charleston (8665530), Key West (8724580), San Diego (9410170), Juneau (9452210). One-minute water level and predictions,
verified highs and lows; a station without one-minute data or verified highs and lows for July is dropped and said so.
Sources and sha256s recorded, not committed. Each station's B and predicted window committed before D is run.
- Y1. The rule's class (never exact, or exact somewhere) is right at 9 or more of the station-months kept.
- Y2. Where predicted and measured exact somewhere, the smallest measured exact rate is within a factor 2 of r_pred at
  all but at most two.
- Y3. The measured exact rates are one unbroken run at every station.
- Y4. Across the stations kept, B and the smallest measured exact rate (never exact ranked last) have Spearman's rank
  correlation 0.6 or more.

### Run 7 (26 Oct; `runs/unr/unr7.py`, outputs `runs/unr/unr-run7-fit.txt` and `runs/unr/unr-run7-predict.txt`, each committed before the next step, and `runs/unr/unr-run7.txt`)

Fit (September and August, runs 5–6's records): the classes separated, the largest B exact somewhere 168.1 (San Francisco,
August), the smallest exact nowhere 264.5 (Los Angeles, August), so **B* = 210.874**; **a = 0.101813**.

July 2026, retrieved 26 Oct from the same API (one-minute in four-day pieces, joined). Every station had one-minute data
and verified highs and lows, none dropped. Public domain, not committed:

| file | sha256 |
|---|---|
| `om_1612340.csv` (Jul) | `46cf4b333d7089543e74fbbe3638b298079657d3883c054c7a56e922ba4e8318` |
| `pr_1612340.csv` (Jul) | `014e7f0df28ee100e3f7b340d9e067c134e51378f5cd0bb6e8a0f7ac56f0e455` |
| `hl_1612340.csv` (Jul) | `13faedcc8235c14f906a2067ece904b8a612c1073a5d188a764a85878686e217` |
| `om_9447130.csv` (Jul) | `b5c6b46072bd20a7c6dbc689db27d564cea03ce60f5d2f0fe3a7a6514d925e19` |
| `pr_9447130.csv` (Jul) | `aa9043307f6086c070fe80769498478371577a6fb02e15b1bfa86eda115a043b` |
| `hl_9447130.csv` (Jul) | `b33554ba83312861b6d4f935eb34f685bd56a1f0310baea3b550fe6f99f06ed4` |
| `om_9410660.csv` (Jul) | `d21860b5ff0b9fa9d5f80cbabb59186287222e59934b8dd8c31329f457756ccd` |
| `pr_9410660.csv` (Jul) | `48147a8697a440c57953af816772886bc6dba70bac4a11f970da322ff6a17203` |
| `hl_9410660.csv` (Jul) | `4aaec8af9f4a76b88b8c1274722547bf566a58103bb5f9766dce7e7e701b23b9` |
| `om_9414290.csv` (Jul) | `faee385a8a07c586a1eaea8af18d6c4e82db7c621edba6f3998b7bcc990913ff` |
| `pr_9414290.csv` (Jul) | `e51d4287087456f8473e8f0b507a45f94c8bf3de35d3cc089c9cf339df10e417` |
| `hl_9414290.csv` (Jul) | `bba10474b0a9b68509137a3b3e9c52aa55151e7ab6adcaeb9fd3733f955a278e` |
| `om_8443970.csv` (Jul) | `d8415f3d64d9ef1ce61c10e2f172b6e16125e195e59127e4c9e9877b839105a5` |
| `pr_8443970.csv` (Jul) | `688b9aea5df45de46a06e918b7b9f852d8e9ad6bc1a5aebe7fc1d5c40574351d` |
| `hl_8443970.csv` (Jul) | `399660d1d0f8778fd0ef119e525a8c1d8ea15e96823202c1591367019ca4646d` |
| `om_8518750.csv` (Jul) | `a92c4fab807dc72dab2728abd253ad081216af7b6b6389f0efb7519533b47c26` |
| `pr_8518750.csv` (Jul) | `538b5ebef54ce5c90af8be4ed92ce50cdc60b74bc0ba239083f1d36025f502aa` |
| `hl_8518750.csv` (Jul) | `2aa9055be81b00e1882e8aee11a83ccfbaf0d47a578561a089e39f6df9c936b2` |
| `om_8665530.csv` (Jul) | `67b1f7129d2b4e041b85c0f603d9ffa634ae948c8db13c3cb3ecb7fe1c751814` |
| `pr_8665530.csv` (Jul) | `4309b7ee6f1bc1f4e8d1ee54c499f4ce0d8b159007020d4433ea0aeddab5ca5b` |
| `hl_8665530.csv` (Jul) | `698b80e30534275319344185ba766e7fc11ad152281bffea9e2b57bd3155a2d0` |
| `om_8724580.csv` (Jul) | `883912a8434ba5ce48d6f90cc1c9d040c03c9e3443caa7b079479959439371a5` |
| `pr_8724580.csv` (Jul) | `2b45c2d4b181b763eadac3041091ad94b9e47128cfaa86325c848b21754de0bd` |
| `hl_8724580.csv` (Jul) | `ea1b3f6b7d2b84c88e19f4c13b4c98d8f89178d92ca5ae76de4433ed646afc16` |
| `om_9410170.csv` (Jul) | `0d9b55966b17b1414494335857bcac61f1caf982a9514487c4294109d563369a` |
| `pr_9410170.csv` (Jul) | `bcbb021bfa6820cd43ec20e35991a777a2d67d8b0e68ee8b81c6673fe8221f3c` |
| `hl_9410170.csv` (Jul) | `0ae70656c548d6309e9ecca033d7030e73ae4676d3608faf13e920414eee8bb4` |
| `om_9452210.csv` (Jul) | `e8685b67b155ac7929504d341d3346cc5e1ec7673ed52dd2f8435c724a967e99` |
| `pr_9452210.csv` (Jul) | `c785c6ceba7920a07d8684cdaf425c57d18e9dadbc20e3f572bdda8f7f9828d9` |
| `hl_9452210.csv` (Jul) | `fc31d3871379960871c87d7e7c6cd1d60779ca65ce470bba9a79861f6e3b3203` |

| station | B | predicted exact from | measured exact |
|---|---|---|---|
| Honolulu | 437.0 | never | never |
| Seattle | 41.6 | 4 | 4–30 |
| Los Angeles | 447.9 | never | never |
| San Francisco | 183.0 | 20 | 15–30 |
| Boston | 85.7 | 8 | 8–30 |
| The Battery (new) | 202.1 | 20 | never |
| Charleston (new) | 106.8 | 10 | 10–30 |
| Key West (new) | 322.7 | never | never |
| San Diego (new) | 337.0 | never | never |
| Juneau (new) | 36.7 | 4 | 5, 6, 8, 12–30 |

**Y1 not killed**: the class right at 9 of 10 (The Battery wrong, its B 202.1 just under B* 210.9). **Y2 not killed**: the
smallest exact rate within a factor 2 at all 5 where both say exact (equal at Seattle, Boston, Charleston). **Y3
killed** by Juneau, not exact at 10 min. **Y4 not killed**: Spearman 0.925.

### After run 7 (post hoc; `runs/unr/unr7-posthoc.py`, `runs/unr/unr7-posthoc.txt`)

Y3 by one event. At 10 min, Juneau's offset 3 put one report into the interval after its own (counts 2 then 0, day
20.6, a 2.9 m tide): 2 of 1,180 interval-offsets off, none at 8 or 12 min. A late report at the edge of its interval,
not a false turn; my "every station" clause had no room for one.

## What run 7 says

The rule found after the fact in run 6, written down with two constants fitted on September and August, predicted July
at ten stations, half of them new: which harbours are never exact by order alone, which are, and from what rate, within a
factor 2 wherever both said exact, and in the right order (rank correlation 0.93). The one wrong class sat at the
threshold. What decides how often a reader must look for order alone to be exact is the part of the noise at the scale
of a few looks, the 10 to 60 minute band, against how sharply the signal turns: r ≈ 0.1 · sd(band)/κ minutes, and never
past B ≈ 210. A rate is the reader's to choose and costs no invariance; this says which rate.
