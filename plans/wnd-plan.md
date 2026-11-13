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
