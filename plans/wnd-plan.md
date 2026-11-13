# WND: "find the z" in the wind

*13 November 2026, SPN R929. Tom: "1 and small things", to Claude's option 1: a third domain for "find the z" (R719,
SMN). Real data. The plan and its predictions are written and committed before any month is fetched. Nothing above the
"Runs" line is edited afterwards.*

## The question

SMN found that the 1–4 Hz seismic noise is a scale mixture in its amounts while its direction keeps its turn's law (the
Cauchy at z, found from half the data). The microseism band was directional and had no turn to name. Wind is different
physics: gusts make the amounts heavy-tailed, and terrain and the mean flow make the fluctuations anisotropic. Does the
direction of the wind's fluctuations keep a turn's law the way the 1–4 Hz band did, or not?

## Known beforehand

- SMN (R923, R924), checked here: in the 1–4 Hz band at 8 of 9 stations, the ratio was within 0.03 of the Cauchy at
  half A's z, and loudness moved it by under 0.03. Its method is copied below.
- From memory, not checked: surface-layer turbulence has σ_v/σ_u about 0.7 to 0.8 in the mean wind's frame (Panofsky and
  Dutton 1984). One-minute ASOS winds are 2-minute running averages, so they are smoothed and correlated minute to
  minute.
- What I looked at before writing this: one hour of Des Moines (DSM) on 1 October 2026, from the endpoint below, only to
  see the format. It has speed in whole knots and direction in whole degrees. No statistic was computed.

## Data (fixed now)

- **Source.** Iowa Environmental Mesonet, ASOS one-minute archive
  (`mesonet.agron.iastate.edu/cgi-bin/request/asos1min.py`, vars `drct`, `sknt`). The underlying NOAA ASOS data are public
  domain. sha256 of each download goes in this plan. The data are kept in the scratchpad and not committed.
- **Stations.** Six, chosen for spread of terrain before looking at any of them: DSM (Des Moines, plains), OKC (Oklahoma
  City, plains), DEN (Denver, high plains by mountains), MSP (Minneapolis), BOS (Boston, coast), SFO (San Francisco,
  coast and sea breeze).
- **Month.** 1–31 October 2026, UTC. Half A is days 1–15, half B is days 16–31.

## Method (fixed now)

1. **Clean.** Drop minutes with missing values or speed 0 (calm, no direction). Dequantize by adding seeded uniform
   jitter within each reading's cell (±0.5 kt, ±0.5°).
2. **Components.** u = −s·sin d, v = −s·cos d (east and north, the wind's travel).
3. **Hours.** Clock hours with at least 50 valid minutes and a mean speed of at least 5 kt are kept. Others are dropped.
4. **The variable.** Each hour is rotated into its own mean wind: x is the along-wind fluctuation and y the cross-wind
   fluctuation, both with that hour's mean removed. This is the standard frame for surface-layer turbulence, and I fix it
   so that the hours share one ellipse.
5. **The turn named.** The direction of the fluctuation, [x : y]. z = m + iγ from half A's covariance (the elliptical
   ratio, as in SMN: m = ρσ_y/σ_x, γ = (σ_y/σ_x)·√(1 − ρ²)). The ratio y/x on half B is tested against Cauchy(m, γ) by
   the KS distance.
6. **Loudness.** Half B's hours ranked by the fluctuation's root mean square. Compare the quietest quarter with the
   loudest by two-sample KS: on the ratio y/x, and on |x|/σ_x.
7. **Amounts.** The kurtosis of x and y over the month, and the KS distance of x from a Cauchy with the same median and
   quartiles.

## Predictions (written before any data)

- **W1 (the amounts are heavy-tailed, not Cauchy).** At at least 4 of 6 stations: excess kurtosis above 3 in both x and y,
  and x at least 0.05 from the Cauchy. *Killed* otherwise.
- **W2 (the direction keeps the turn's law).** At at least 4 of 6 stations, D(y/x on half B, Cauchy at half A's z) under
  0.03. *Killed* if 3 or more stations are at 0.03 or above.
- **W3 (loudness moves the direction, not just the amounts).** I predict loudness does not move the direction: at at
  least 4 of 6 stations, the quiet and loud quarters' ratio laws are under 0.03 apart, while their |x|/σ_x laws are at
  least 5 times as far apart. *Killed* if 3 or more stations have the ratio 0.03 or more apart.

## What would and would not be shown

- W2 and W3 not killed would mean the wind's fluctuations behave like SMN's 1–4 Hz band: a scale mixture in the amounts,
  with the direction keeping a turn's law that can be found from half the data. That would make three domains (seismic,
  and now wind), with the same sorting failing in SMN's microseism band.
- W2 killed would mean the fluctuations are not elliptical in their own frame (for example, the ellipse changing with
  stability through the day). In that case the turn cannot be named this way and the sorting says nothing about the wind
  (R719).
- It is classical either way. The elliptical ratio and scale mixtures are textbook; the sorting is ours.

## Runs

### Run 1 (13 November; `python3 -I runs/wnd/wnd.py <dir>`, output `runs/wnd/run1.txt`)

Data fetched after the plan was committed (8a53c18). sha256: BOS `5ed26335b4b6bb752953aeee88311d1ed3a5c9a614c8bfe44754a7ccb4e5bd85`,
DEN `6b3a4229973b59e79ffb650ac9a87ef15d9d2f8c784a092a115cf5df1af73790`, DSM `9029fbfe440231bfd7645ba40e4e7fb810b2ab454645b589043cd77e0cc00e1c`,
MSP `b5f9a9030b94cf2d788adaf22e51141058c53d206d1033bdfec5d2a74efc422e`, OKC `f84814d594ed85aeec5053a48087b7ce74c9d7dd94ff0671a80d61bc125bdb84`,
SFO `4b00a3b2add53497fded8828a425f9b49306edcbc7adcdd7f41c4f08cc35231c`.

| station | hours | z | D(y/x, Cauchy z) | ratio, quiet vs loud | \|x\|, quiet vs loud | kurtosis x, y |
|---|---|---|---|---|---|---|
| DSM | 482 | +0.001 + 0.995i | 0.032 | 0.101 | 0.418 | 3.0, 3.3 |
| OKC | 506 | −0.065 + 0.983i | 0.060 | 0.113 | 0.432 | 11.6, 4.5 |
| DEN | 514 | +0.052 + 1.029i | 0.028 | 0.061 | 0.423 | 4.7, 4.2 |
| MSP | 437 | −0.051 + 0.932i | 0.051 | 0.099 | 0.342 | 1.4, 5.0 |
| BOS | 526 | −0.025 + 1.005i | 0.029 | 0.088 | 0.411 | 1.1, 3.0 |
| SFO | 352 | +0.191 + 0.906i | 0.067 | 0.099 | 0.348 | 2.4, 3.0 |

- **W1: killed.** Both kurtoses were above 3 only at 3 of 6 stations (OKC, DEN, and DSM barely); x was at least 0.05 from
  the Cauchy at all six.
- **W2: killed.** The ratio was 0.03 or more from the Cauchy at half A's z at 4 of 6 stations (DSM 0.032, OKC 0.060, MSP
  0.051, SFO 0.067). It was under 0.03 at DEN and BOS.
- **W3: killed, at all six.** Loudness moves the direction's law by 0.061 to 0.113, so the condition that it moves only
  the amounts was not met anywhere.

**Post hoc, not tested** (`runs/wnd/posthoc.txt`, the same code with two lines added):
- The quiet quarter's fluctuations have a root mean square of 0.76 to 1.14 kt, the size of the data's one-knot step.
- The quiet quarter is the farther of the two from the Cauchy at five of six stations (0.042 to 0.104, against the loud
  quarter's 0.028 to 0.065).
- The ellipse is nearly round (σ_y/σ_x 0.93 to 1.03), not the 0.7 to 0.8 expected from memory for surface-layer
  turbulence. Two-minute running means and whole-knot, whole-degree readings may account for both, but that is not shown.

**In short.** On ASOS one-minute winds the turn cannot be named this way. The direction of the fluctuation does not keep
one Cauchy law across loud and quiet hours, and the amounts are not clearly heavy-tailed. By R719 the sorting says
nothing about the wind from these data. Unlike SMN's 1–4 Hz band, this is no third domain. Whether the cause is the wind
or the instrument (a step as large as the quiet hours' fluctuations) is open. Fast sonic anemometer data (for example
NEON's 20 Hz eddy covariance) would tell them apart.
