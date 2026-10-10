# GCN: star counts within 100 pc, on Gaia

*Plan, predictions and kills written 10 October 2026, before any Gaia data was in this environment (Claude; Tom: "I can
try to find the data you need for a proper test"). CNT (`plans/cnt-plan.md`) could not count by kind on Hipparcos, since
its spectral labels mix kinds and its limit cuts the far ones. Gaia's parallaxes are about a hundred times finer, and its
catalogue holds every ordinary star within 100 pc, so kinds can be picked by colour and the volume is complete. The lab
rules hold: nothing above the "Runs" line is edited after the run.*

## The data (to be supplied)

Gaia DR3, every source with parallax ≥ 10 mas and parallax_over_error ≥ 10, with columns source_id, ra, dec, l, b,
parallax, parallax_error, phot_g_mean_mag, bp_rp and ruwe. The Gaia Catalogue of Nearby Stars (Smart et al. 2021) will
do in its place. Gaia data is © ESA/Gaia/DPAC, CC BY-SA 3.0 IGO. Its source and sha256 are recorded here when it
arrives, before the run.

**Cuts:**
- ruwe < 1.4, which keeps single, well-measured sources;
- d = 1000/parallax pc;
- the main sequence: stars between two lines in (bp_rp, M_G), with M_G = G + 5 + 5·log₁₀(parallax/1000) (the band
  below).

M_G uses the parallax, so it is never used where flux is tested against distance (P3 avoids it). It is used only to pick
a kind for counting by distance, where it cannot bias the slope, because the volume is complete for every kind kept.

**The band:** M_G within 1.5 magnitudes of 3.4·bp_rp + 1.9, for bp_rp from 0.5 to 3.2. That line runs through the main
sequence (a G dwarf at bp_rp 0.8 is about M_G 4.6; an M dwarf at 2.5 about 10.4). The band holds the main sequence and its
unresolved binaries, and leaves out giants, about five magnitudes above it, and white dwarfs, about five below it.

**Kinds**, by colour on the band: G (bp_rp 0.75–0.95), K (1.0–1.5), early M (2.0–2.5), late M (2.5–3.0).

**The data as supplied** (10 October 2026, recorded before the run). Tom downloaded the GCNS main table from VizieR,
J/A+A/649/A6/table1c (Gaia Collaboration, Smart et al. 2021, doi:10.26093/cds/vizier.36490006), as tab-separated values,
whole sky, no row limit: 331,312 rows with the columns RA_ICRS, DE_ICRS, Plx, e_Plx, Gmag, BPmag, RPmag, RUWE and GCNSprob.
The file is 26.2 MB, sha256 `73b63a058a7e2afce4b655290d030eb1daa101aeabe62730c007deeab3e67c6c`. It is not committed.
GCNS is built on Gaia EDR3, whose astrometry and G, BP and RP photometry are the same as DR3's. The table has no l, b or
bp_rp, so:
- bp_rp = BPmag − RPmag; the 7,002 rows with no BP or RP have no colour and are dropped;
- b is computed from RA and Dec by the standard J2000 rotation (ICRS and J2000 differ by far less than a degree's use here);
- the plan's cuts are applied as written: parallax ≥ 10 mas, parallax/error ≥ 10, ruwe < 1.4, in every prediction,
  P4 included. GCNSprob is not used.

**Fits, where the plan is silent** (fixed now, before the run, as CNT fixed them): every slope is least squares on
cumulative counts; by distance at steps of 0.05 levels of log₂ d, from 25 to 100 pc inclusive; by light at steps of 0.1
magnitude, from G_max − 3 to G_max inclusive. In P3 a kind's members are those on the band in its colour range, and its
1st percentile of M_G is taken over all of them within 100 pc.

## Predictions

- **P1 (an even spread, by kind).** For each kind, the slope of log₂ N(<d) against log₂ d over 25 ≤ d ≤ 100 pc is 3
  within 0.15. None is steeper than 3.05: the disc can only thin the stars outward, never thicken them. *Killed* if any
  kind is outside [2.85, 3.15], or any is steeper than 3.05.
- **P2 (the disc, toward the poles).** For the four kinds together, over 25 ≤ d ≤ 100 pc, the slope toward the poles
  (|b| > 45°) is lower than in the plane (|b| < 15°) by between 0.03 and 0.3.
  - The reason: a disc whose density falls by e over about 300 pc, from near its middle, thins a polar cone by about a
    third of a level of density by 100 pc, and the plane hardly at all.
  - *Killed* if the difference is outside [0.03, 0.3].
- **P3 (by light, inside the complete volume).** For each kind, let G_max = (the kind's brightest M_G, its 1st
  percentile) + 5. Every star of the kind brighter than G_max is then within 100 pc, so the count by light is not cut by
  the volume. Count N(<G) for G from G_max − 3 to G_max, against light in levels (−1.3288·G). The slope is 1.5 within
  0.15, and not steeper than 1.55. *Killed* if any kind is outside [1.35, 1.65], or steeper than 1.55.
- **P4 (colour is nearly a clean kind nearby).** Within 50 pc, of all the stars in each kind's colour range (before the
  band's cut), under 3% fall outside the band. CNT run 3 could not have this cleanliness: there, one "K0 III" in ten was
  something else. *Killed* if any kind is over 3%.

## What would not be shown

- Hipparcos's 1.2 at the bright end. Bright stars are far off, past 100 pc. That needs the bright all-sky sample (Tom's
  second query), with a plan of its own.
- The disc's thickness, which would need a fitted model. P2 only asks that the disc be seen, in the right direction and
  to the right order.

## Runs

