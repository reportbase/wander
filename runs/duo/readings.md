# DUO readings (15 Oct 2026, about 21:20–21:50)

Read from the scan of Summhammer, Rauch and Tuppinger's (1987) figure embedded in slide 22 of Rauch's EmQM 2013 slides
(sha256 in `plans/duo-plan.md`). Native pixels of the 2,436 × 3,464 scan, x right, y down. Written down before
`duo.py` compared any of them with either form.

## Calibrations (axis ticks)

| panel | a from x | A from y | checked against the drawn curves |
|---|---|---|---|
| main plot | (x − 1490)/576 (frame 1490 = 0, ticks every 57.6 px = 0.1, frame 2066 = 1) | (3303 − y)/588 (ticks 2715, 2832.5, 2951, 3070 at 1, 0.8, 0.6, 0.4; frame 3303 = 0) | √a to 0.003, A = a to 0.003 |
| middle inset | 0.01·(x − 921)/47.1 (ticks 921, 971, 1016.5, 1061, 1109, 1156.5 at 0 … 0.05) | 0.1·(3229 − y)/237.25 (ticks 2754.5, 2993, 3229 at 0.2, 0.1, 0) | √a to 0.002 |
| left inset | 0.005·(x − 433.5)/272.5 (ticks 433.5 at 0 … 706 at 0.005) | 0.05·(3188.5 − y)/418.5 (frame 2770 = 0.05, 3188.5 = 0; the inner ticks sit up to 5 px off this line) | √a to 0.0005 at a = 0.002 |

## Points (marker centre; half the vertical error bar between its caps, or half the marker where no bar shows; half the
horizontal bar where one is drawn)

| id | panel | kind | x | y | half bar y (px) | half bar x (px) | note |
|---|---|---|---|---|---|---|---|
| S1 | main | stochastic | 1521.5 | 3165 | 8.5 | – | inside the callout box; no bar seen, half the marker |
| S2 | main | stochastic | 1552.5 | 3111 | 9 | – | |
| S3 | main | stochastic | 1572.5 | 3076 | 14.25 | – | |
| S4 | main | stochastic | 1616 | 3019.5 | 9.5 | – | |
| S5 | main | stochastic | 1712 | 2957 | 14.25 | – | top cap merges with the curve |
| S6 | main | stochastic | 1762 | 2914.5 | 15 | – | top cap merges with the curve |
| D1 | main | deterministic | 1630.5 | 3161 | 6 | – | no bar seen, half the marker |
| D2 | main | deterministic | 1770.5 | 3020 | 12 | 5.5 | |
| D3 | main | deterministic | 1912 | 2879.5 | 11.5 | 6 | |
| M2 | middle | stochastic (Gd) | 945.5 | 3127 | 15 | – | crossed by the curve and a label arrow; bars uncertain |
| M3 | middle | stochastic | 961 | 2992.5 | 17 | 11.5 | |
| M4 | middle | stochastic | 1034 | 2891 | 22 | 12.25 | |
| M5 | middle | stochastic | 1033.5 | 2837.5 | 23.5 | 12.25 | |
| L1 | left | stochastic (Si) | 460 | 3053.5 | 38.5 | 23.5 | |
| L2 | left | stochastic (Gd) | 487.5 | 3041 | 25.5 | 21 | |
| L3 | left | stochastic (Gd) | 605 | 2875.5 | 62.5 | 46 | |

Not read: the middle inset's lowest cluster (x ≈ 933, y ≈ 3175). It is the region the left inset magnifies.

A question found while reading: the middle inset's "NEW Gd MEASUREMENTS" label points to its lowest cluster and to M2,
and the left inset labels two points "Gd". So M2 may be L3 drawn at the coarser scale, but the two give different a
(0.0052 against 0.0031). Both readings are reported: M2 counted as its own point, and M2 taken as L3.

## The fringe panels (D3)

The thick bars at each panel's right edge, peak to trough, from their longest dark runs:

| panel | empty bar (y) | absorber bar (y) | ratio | a stated in the panel |
|---|---|---|---|---|
| stochastic (gold foil) | 1369.5–2031: 661.5 | 1761–2056.5: 295.5 | 0.4467 | 22.6 ± 0.8% |
| deterministic (beam chopper) | 1233–1895: 662 | 1826.5–1987.5: 161 | 0.2432 | 24.2 ± 0.2% |

Each bar end is read to about ±2 px.
