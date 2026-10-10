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

### Run 1 (10 October 2026)

`python3 -I plans/gcn/gcn.py <the TSV>` (data checked against the sha256 above), output in `plans/gcn/gcn-run1.txt`. The
first pass printed the by-light slopes with the wrong sign: the script had not turned it, as the plan says and CNT's
script does. That was fixed in the script, and nothing else changed, before this output was recorded:

```
331312 GCNS rows; 7005 with no G, BP, RP or RUWE dropped; parallax >= 10 mas and >= 10 sigma: 295010; ruwe < 1.4: 246150
P1: KILLED. each kind, 25-100 pc, slope of log2 N(<d) in [2.85, 3.05] (3 for an even spread)
P2: KILLED. four kinds, 25-100 pc: plane (|b| < 15) 2.934 (33369), poles (|b| > 45) 3.141 (34796), difference -0.207
P3: KILLED. each kind, G_max - 3 to G_max, levels of number per level of light in [1.35, 1.55] (1.5 for an even spread)
P4: KILLED. within 50 pc, under 3% of each colour range off the band
  G        bp_rp 0.75-0.95: 10077 on the band within 100 pc (9921 past 25 pc); by distance 2.991; G_max 8.32 (1956 brighter), by light 1.552; within 50 pc 1706, off the band 20.28%
  K        bp_rp 1.0-1.5: 14986 on the band within 100 pc (14703 past 25 pc); by distance 2.882; G_max 10.35 (4890 brighter), by light 1.482; within 50 pc 2715, off the band 23.61%
  early M  bp_rp 2.0-2.5: 35480 on the band within 100 pc (34872 past 25 pc); by distance 2.984; G_max 13.26 (8969 brighter), by light 1.366; within 50 pc 4319, off the band 3.66%
  late M   bp_rp 2.5-3.0: 64054 on the band within 100 pc (63211 past 25 pc); by distance 3.138; G_max 14.57 (14401 brighter), by light 1.573; within 50 pc 8085, off the band 4.13%
```

- **P1 killed, by one kind.** G 2.991, K 2.882 and early M 2.984 are inside [2.85, 3.05]. Late M gives 3.138, steeper
  than 3 by more than the disc could allow.
- **P2 killed, the wrong way round.** The poles count *steeper* than the plane, 3.141 against 2.934, not flatter.
- **P3 killed, by two kinds at the edge.** K 1.482 and early M 1.366 are inside. G gives 1.552 and late M 1.573, past the
  ceiling of 1.55.
- **P4 killed, by every kind.** Within 50 pc, 20% of the G colour range and 24% of the K range lie off the band; early M
  3.7% and late M 4.1%.

## Reading (after the run; not ruled)

Everything below was looked at after the run (`gcn_look.py`, kept in the session's scratchpad, not committed). None of it
is a prediction, and a second run on this file could not be blind to it.

- **The RUWE cut depends on distance, and that is what steepened P1 and turned P2.** Among the four kinds on the band,
  the cut removes 28% of stars at 25–35 pc, 22% at 35–50, 19% at 50–70 and 18% at 70–100. A binary's wobble is larger in
  angle when it is near, so near binaries are flagged more often. Removing more near stars than far ones makes the count
  rise faster with distance. Without the cut, every kind gives 2.93 to 3.00 by distance (G 2.998, K 2.959, early M 2.933,
  late M 2.928), and the plane and the poles give 2.937 and 2.924, a difference of 0.013. The plan took the RUWE cut to
  keep "single, well-measured sources"; it does, and it does so unevenly in distance. The cut was the plan's, and the
  kills stand.
- **Without the cut, the disc does not show within 100 pc.** The plane–pole difference, 0.013, is under P2's floor of
  0.03. A disc falling by e every 300 pc from the Sun's height would lower the polar slope over 25–100 pc by about 0.1
  (the slope of N(<d) is about 3 − ¾·d/300 toward a pole), inside P2's band. The measured 0.013 says the stars' density
  is nearly flat within 100 pc of the Sun, toward the poles as in the plane. That fits a disc that is flat at its middle
  (as a sech² profile is) rather than one falling exponentially from it. It is a reading, not tested here.
- **The colour ranges of G and K hold the white dwarfs.** Of the off-band stars within 50 pc, nearly all in the G and K
  ranges sit 8 to 10 magnitudes below the band's line: white dwarfs, about 330 in the G range and 570 in the K range.
  Cool white dwarfs have the colours of G and K dwarfs. The plan expected the band to separate them, and it does. But P4
  asked whether colour alone is a clean kind, and for G and K it is not: about one star in five of those colours within
  50 pc is a white dwarf. This is the same lesson as CNT run 3's "K0 III", at about twice the rate. Colour with the
  parallax's magnitude (the band) is a clean kind; colour alone is not.
- **What did hold: three levels of number per level of distance.** The four kinds count as an even spread does, within
  0.15 of 3, over two levels of distance, on about 125,000 stars, once nothing that depends on distance is used to choose them.
  By light, with the RUWE cut, the four kinds give 1.37 to 1.57, about 1.5 on average. That is the even spread's value,
  which CNT's mixed Hipparcos sample (about 1.2) never reached. So the 1.2 of CNT run 1 comes from mixing kinds and
  distances past 100 pc, not from the inverse square or the volume.

## Exploration after run 1 (10 October 2026; not predictions)

Tom: "this is just a quick test, not a test that will be published. continue to test to see what the situation is." So
what follows was looked at freely, with no predictions first. It is a map of the situation for planning the next real
test, and nothing in it is a result. Scripts `plans/gcn/explore.py` (GCNS) and `plans/gcn/hip_explore.py` (HYG), outputs
beside them.

**A correction to the reading above.** It said CNT's 1.2 comes "from mixing kinds". That is wrong as stated: CNT's own
plan notes that a mix of luminosities spread evenly still gives 1.5, since each kind alone does. A mix flattens the count
only if the spread is uneven over the distances the kinds reach. The exploration below finds that it is.

1. **Within 100 pc, an even spread, near enough.** Without the RUWE cut, the local slope of the count by distance is
   between 2.75 and 3.07 for every kind in every range from 25 to 100 pc, mostly 2.9 to 3.0. By light the kinds give
   1.46, 1.52, 1.49 and 1.50 (G, K, early M, late M), against 1.5.
2. **The disc does show, as density against height.** In a cylinder 60 pc in radius about the Sun, the main-sequence
   stars thin from about 52 per 1000 pc³ within 25 pc of the Sun's height to about 47 at 55–80 pc above and below: a
   fall of 10%, what an exponential with a scale of about 500 pc would give over that range, or a disc flat at its
   middle. It peaks a little below the Sun (z −20 to −10 pc), as expected if the Sun sits some 10–20 pc above the
   middle. The count slopes hardly feel a 10% fall spread over 100 pc, which is why P2 could not see it.
3. **In the plane, flat.** In the slab |z| < 20 pc the density is 51 to 53 out to 98 pc in the plane, a percent or two
   higher toward the Galactic centre than away.
4. **Hipparcos's bright stars are mostly far, and of a thin kind.** Of the 20,477 stars brighter than V 7.3 with a
   distance, only 29% are within 100 pc; half are past 152 pc, a tenth past 385 pc. 81% have M_V brighter than +2, so
   they are seen out to 115–724 pc. These are mostly A and B stars and giants, whose layer in the disc is thinner than
   the M dwarfs' (tens of parsecs to about a hundred, against several hundred), and they are dimmed by dust in the plane.
5. **Even in the disc's middle their density falls with distance.** Stars with M_V < 0, all brighter than V 7.3 out to
   288 pc if there were no dust, counted within |z| < 50 pc: 319, 318, 321, 299 in the shells 100–150, 150–200, 200–250
   and 250–288 pc. A slab spread evenly would give counts rising about 1.8 times from the first shell to the third. The
   counts stay flat. Dust, the Gould Belt's clump at 100–150 pc, and Hipparcos's parallax errors at these distances
   (about 25% at 250 pc) all act, and are not separated here.

**The situation, as it now looks.** The inverse square and the volume give 1.5 by light and 3 by distance, and on Gaia's
nearby stars, counted kind by kind within 100 pc, that is what is found. Hipparcos's 1.2 is a count of stars that are
mostly past 100 pc, of kinds that lie in a thin layer, through dust: past the layer's thickness a count turns from a
sphere's (1.5) toward a slab's (1.0), and dust flattens it further. 1.2 sits between. Under §0 none of this is a result
until a test with its prediction written first measures it: the natural one is a bright Gaia sample with parallaxes and
extinctions, counted by height above the plane.
