# Reader geometry and physics

*Started 10 October 2026, at Tom's word: "lets create a new physics paper and iterate there." A working paper: a reading,
revised as it is worked over, not a ruling. It takes its terms from SPN (`papers/serial-parallel-nowhere.md`), and §1
gives what is needed to read it alone. Each result here names its plan in `plans/`, where its prediction was written
before its run. A result goes into SPN only once it has been tested and ruled.*

**What this paper is for** (Tom, 10 October: "wanderer priority was user experience, not physics. the physics then
became unexpextedly interesting. we should do the correct physics testing, UI is secondary or even not needed"). SPN is
geometry: fill levels, the sweep, the corner, the levels. Physics is amounts: distances, sizes, light, radii. This paper
collects where the two meet, and tests each meeting on real measurements or on exact arithmetic. The flying page and its
bodies are pictures. They are never evidence here.

**Iterations**

- 10 October, first: the paper started, from the four tests of the day (ISQ, HZN, REF, MAG) and the physics labs before
  them (BAL, LAD, OLB, GRN run 8); the rules (§0), the dictionary (§1), the results by standing (§2), the kills (§3) and
  the queue (§4).
- 10 October, second: CNT, star counts in levels, on the Hipparcos stars (§2.1, §3); P1 and P2 at their bands' edges,
  P3 and P4 killed: the counts rise about 1.2 levels per level of light, not 1.5, alike in the plane and toward the poles.
- 10 October, third: CNT runs 2 and 3, by kind and distance: the near G dwarfs give 3.47 levels of number per level of
  distance (3 for an even spread); the K0 giants cannot be counted cleanly, since about one in ten labelled K0 III is
  something fainter, and the kind has no complete distance (§3).
- 10 October, fourth: GCN, star counts within 100 pc on Gaia (the Catalogue of Nearby Stars, from Tom), by colour on
  the main sequence. All four predictions killed: the RUWE cut removes more near stars than far ones and steepens the
  counts, and the G and K colours hold the white dwarfs. Read without the cut, every kind gives 3 levels of number per
  level of distance within 0.07, and by light the kinds average 1.5: the even spread holds within 100 pc (§2.1, §3).
- 10 October, fifth: exploring the GCN data and Hipparcos freely (Tom: a quick test, not one to publish; nothing in it
  is a result). Within 100 pc the stars thin about 10% from the disc's middle to 55–80 pc above and below. 71% of
  Hipparcos's stars brighter than V 7.3 are past 100 pc, mostly luminous kinds in a thin layer, seen through dust: a
  count past the layer's thickness turns from a sphere's 1.5 toward a slab's 1.0, which is the likely source of CNT's
  1.2 (§4). Mixing kinds alone does not flatten a count; an uneven spread does.

## 0. The rules

- **Evidence is real data or exact arithmetic.** Published measurements (catalogues, fact sheets, shape models), or
  arithmetic checked to the last digit. Wander's world, the flying page, its bodies and the labs that run inside it,
  illustrate. A lab in Wander's world shows that a reader *could* recover something; it does not show that the world
  *is* so.
- **Prediction first, from the theory alone.** The plan is committed before the data is opened for anything but its
  column names. A killed prediction stays killed, and a fix is a new run with its own prediction.
- **Keep the case, and name the bridge.** h and v are fill levels, scale-free: geometry. H, V, d, Δ, L and R are
  amounts: physics. A result crosses from one to the other only by a named bridge, an amount supplied from outside: a
  size, a radius, a kind (SPN Part II).
- **Data.** Each dataset's source, licence and sha256 go in its plan, and large data is not committed. In this
  environment the astronomy archives (VizieR, CDS, ESA, NASA's PDS) are blocked; GitHub and PyPI are reachable.

## 1. The dictionary

What each piece of SPN's geometry meets in physics, and through which bridge. "Tested" names the plan that tests it.

| geometry (SPN) | physics | bridge | tested |
|---|---|---|---|
| the reading s = v/h, a ratio | a distance in units of a size, d/Δ | the size Δ | ISQ (form only) |
| levels: log₂ of a reading | log₂ of an amount ratio: magnitudes, decibels, octaves | a zero point, which drops out of every slope | MAG |
| the corner, h = v | where an amount pair is equal: one step across (the resolution limit), a radius | the pair's two amounts | GRN run 8; HZN |
| the in-place lay past the corner, 2 − 1/s | an angular size, Δ/d, counted down from the horizon | Δ | ISQ |
| the lay's room per unit s, 1/s² | how fast an angular size shrinks with distance (one dimension); light's 1/d² is its square (two) | Δ | ISQ; MAG |
| depth from the corner, log₂(r/r̄) | height above a world's own reference sphere | the size r̄ | REF |
| reading from the outline, chords 2 sin φ | standing on a world: the horizon at home; the horizon's distance √(2Rh) | the radius R | HZN |
| a ring thinner than a grain | a catalogue's or an instrument's limit: past it only the bright of a kind are read | the grain, an amount | MAG P3; HZN runs 1–3 |
| a known kind | a standard candle; a spectral class | the kind's luminosity | MAG (the kind is about a level wide) |
| V = H, the calibration | reading amounts with no unit of the other's | travel, a constant, a kind, a shared fact | LAD (in Wander's world) |

## 2. Results, by standing

### 2.1 On real data

- **Two levels of light per level of distance** (MAG, `plans/mag-plan.md`). On the Hipparcos stars, with distance from
  parallax and kind from the spectrum:
  - G0–G5 dwarfs within 23 pc lose 2.02 levels of light per level of distance (83 stars);
  - K0 giants where the catalogue is complete lose 1.93 (533 stars);
  - past the catalogue's limit the slope flattens to 1.61.
  This is the inverse square read in levels.
- **Star counts rise 1.2 levels per level of light, not 1.5** (CNT, `plans/cnt-plan.md`). For an even spread the
  inverse square and the cube of the volume give 1.5 levels of number per level of light. The Hipparcos stars brighter
  than V = 7.3 give about 1.2 at every brightness: 1.33 for V 1–4, 1.22 for V 5–7.3. And they give it alike in the
  galactic plane (1.229) and toward the poles (1.227). The even-spread bridge gives out, and the disc's thinness alone
  does not say why.
- **Within 100 pc, three levels of number per level of distance** (GCN, `plans/gcn-plan.md`, read after run 1). On the
  Gaia Catalogue of Nearby Stars, main-sequence stars picked by colour on the band (G, K, early M, late M; about 125,000):
  - by distance over 25–100 pc, 2.93 to 3.00 for each kind once no cut that depends on distance is used, against 3 for
    an even spread; plane and poles alike (2.937, 2.924);
  - by light, inside each kind's complete volume, 1.37 to 1.57, about 1.5 on average, against 1.5.

  The run's own predictions were killed (§3); these are readings of the same data after it, not ruled. They say the even
  spread holds within 100 pc, kind by kind, so CNT's 1.2 is not in the counting itself but in the spread past 100 pc.
- **Real worlds are their corner within a hundredth of a level** (REF, `plans/ref-plan.md`, P4 and P5). By published
  radii:
  - the rocky worlds' flattening: Earth 0.0048 levels, Mars 0.0085, the Moon 0.0017;
  - the spinning giants about a tenth: Jupiter 0.097, Saturn 0.149;
  - Earth's relief, Challenger Deep to Everest, 0.0045; with its flattening the whole Earth is within 0.0093 levels.

### 2.2 Exact arithmetic

- **The lay has the inverse square's form** (ISQ, `plans/isq-plan.md`). Past the corner the lay is proportion in h/v, so
  its room per unit s is 1/s², the flip's Jacobian, exactly. Each level gets 2^−(k+1) of the room.
- **Standing on the outline is standing on a world** (HZN, `plans/hzn-plan.md`). From a place on a circle the readings
  are chords 2 sin φ, and:
  - the reader's corner (the geometric mean) is the radius, 30° below the horizon;
  - on a ball it is 2/e of the radius, 21.6° below;
  - rising by e radii, the horizon is √(2e) radii off, half a level per doubling of height. With R given, that is
    √(2Rh).

### 2.3 In Wander's world (illustration, not evidence)

These labs ran inside Wander's world before 10 October. They show what a reader could recover; they do not show that
the world is so:
- BAL, the inverse square's resolved half;
- LAD, the distance ladder: parallax, then width, then light past the resolution limit;
- OLB, the dark sky and the world's age;
- GRN run 8, a pair receding under the inverse square, lost at one grain across.

They are kept as worked examples of the bridges (`labs.html`, `plans/grn-plan.md`).

## 3. What was killed, and what it taught

- **REF P1–P3: wander's bodies** are far rougher than real worlds. The Moon spans 0.25 levels against the real 0.0165.
  "Broad first" is the order in which bands are seen, not where the relief lies. Under §0 this was never evidence. It is
  kept as the example of what not to count.
- **MAG P4: K0 III scatters 1.4 levels**, not under 1.0. A known kind is a bridge about a level wide.
- **CNT P3 and P4: the plane and the poles count alike.** The disc was predicted to flatten the counts toward the poles
  more than in the plane. It does not: both give 1.23. Dust in the plane and the clumping of young bright stars are the
  likely offsets, untested.
- **CNT runs 2 and 3: "K0 III" is not one kind.** Within 50 pc, 4 of 36 stars so labelled are too faint to be giants:
  about one in ten throughout, 19% by 140 pc. So the K0 giants have no distance within which Hipparcos holds them all,
  and counting them by distance or light measures the label and the catalogue, not space. MAG's 140 pc "complete" range
  rested on the same false premise. Only the near G dwarfs counted cleanly: 3.47 levels of number per level of distance,
  against 3.
- **GCN run 1, all four: a cut that depends on distance, and a colour that is not a kind.** The RUWE cut (< 1.4) removes
  28% of stars at 25–35 pc and 18% at 70–100 pc, since near binaries wobble more in angle. It steepened the late M count
  to 3.14 (P1) and the poles past the plane (P2, the wrong way round). By light, G and late M sat just past the 1.55
  ceiling (P3). Within 50 pc a fifth of the G and K colours are white dwarfs (P4): colour alone is not a kind; colour
  with the parallax's magnitude is.
- **HZN run 1's P5 and run 2: a page reads only to its grain.** Near home, draw's levels page cannot read nearer than one
  segment or one direction, whichever is coarser. Run 3, with both grains doubled together, was not killed.

## 4. The queue

Tests that could be run next, each on real data or exact arithmetic. Each would need its plan written first.

- **Why the counts give 1.2.** GCN's exploration (not a result) points to a thin layer of luminous stars seen through
  dust: 71% of the stars Hipparcos counts are past 100 pc, and even in the disc's middle the luminous ones stop rising
  with volume past about 125 pc. A test needs a bright all-sky Gaia sample (G ≤ 10) with parallaxes and extinctions, and
  a plan written first: the count's slope by height above the plane, and whether correcting for dust moves 1.2 toward a
  slab's 1.0 or a sphere's 1.5.
- **Clusters as one kind at one distance.** The Hyades, Coma Berenices, the Pleiades and Praesepe each have their own
  distance, from their members' mean parallax. At a fixed colour their main sequences should step two levels of light
  per level of the clusters' distance. This needs membership lists. Hipparcos membership is published, but the archives
  are blocked here.
- **Real topography for REF.** The Moon (LOLA), Mars (MOLA) and Earth have spherical-harmonic shape models. With them:
  the depth spans in levels, and whether the relief's power falls by a fixed amount per level of wavenumber (Kaula-like).
  NASA's PDS is blocked here.
- **One dimension against two.** ISQ's reading separates an angular size (falling one level per level of distance) from
  its square, the light (two levels). Stars with measured angular diameters (interferometry) and parallaxes would test
  the one-level half directly.
