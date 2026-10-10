# The inverse square

*Started 10 October 2026, at Tom's word: "lets give the inverse square law its own paper to iterate on." A working paper:
a reading, revised as it is worked over, not a ruling. It gathers what the corpus has on the law: SPN §3.2's disc and wave
fields, §3.3's "the same signal, a smaller share", and the plans ISQ, MAG, CNT, GCN and NRF. It also says what each piece
stands on. The rules are `papers/physics.md` §0: evidence is real data or exact arithmetic, predictions come first, keep
the case and name the bridge. A result goes into SPN only once it has been tested and ruled.*

**Iterations**

- 10 October, first: the paper started from the day's work. It covers the law as physics holds it (§1), the law in
  levels (§2), the two ways a reader meets it (§3), the near field (§4), the lay's form (§5), what stands on what (§6),
  and the questions open (§7).
- 10 October, second: "Known already" added (§0), after Tom: "this is a very well studied idea, so it would actually be
  suprising if we find something genuinly new about the inverse square law." The paper is kept as a calibration case
  and a translation into SPN's terms, with no claim of novelty.
- 10 October, third: "The law in SPN's words, in brief" added (Tom: "so we could at least explain the inverse square law
  using our vocabulay?", then "yes"): eight steps, with conservation and the exponent named as the bridges from physics.

**Standing marks.** Each claim carries one:
- **[physics]**: established outside this corpus, quoted;
- **[exact]**: exact arithmetic, checked in a plan;
- **[data]**: measured on published data, in a plan;
- **[reading]**: Claude's reading, unruled;
- **[illustration]**: Wander's world, which shows and does not test.

**Keep the case.** The law is physics: d, a (a size), L, E and N are amounts. A ratio of two amounts in one unit, such as
d/a, is a pure number. Its corner, where the two are equal, is the corner of *that pair* (SPN §1, "Every pair has its own
sweep: name the pair"), a point set by amounts, not the reader's h = v. Where this paper says "the corner", it names the
pair.

**Two conventions for s.** SPN §3.2 writes s = a/d, size over distance; NRF writes s = d/a. The flip exchanges them. Every
statement below holds either way, with s and 1/s exchanged; each passage says which it uses.

## 0. Known already: what this paper is, and is not

The inverse square has been studied for three centuries, unsituated and situated. Nearly everything below has a
standing counterpart in physics:
- **The radiance theorem** (radiometry). In empty space, radiance, the brightness per unit of view, is conserved along a
  ray. Irradiance is radiance times the projected solid angle the source fills. This is SPN's "per address, nothing
  changes" (§3), and it is already a situated account of the law: what one standpoint receives, from what it sees.
- **The view factor** (heat transfer, radiometry). The share of one surface's view that another fills, counted with the
  cosine at both ends, is tabulated for standard shapes. The disc's s²/(1 + s²) (§4) is a textbook view factor.
- **Reciprocity of view factors**, A₁F₁₂ = A₂F₂₁: the standing symmetry between the two ends. It is the nearest known
  counterpart of the flip's fairness in §4, though not the same statement.
- **Newton's cones** (Principia, Book I, Proposition 70). From a point inside a shell, opposite thin cones cut patches
  whose areas grow as the square of their distance while their pull falls as its inverse square, so they cancel. A proof
  from a standpoint, and the ground of Cavendish's null test (§1).
- **Le Sage's shadow gravity** (1700s), a caution. It derived the inverse square situatedly: each body shades the other
  from a rain of particles, the shadow shrinking as the solid angle. It got 1/d² right and failed on everything else
  (drag, heating). Reproducing a law from a standpoint does not show that the standpoint's picture is the physics.

So this paper is a **calibration case**. It is one of the few places where both the unsituated and the situated
explanations are known exactly. That makes it the place to check that SPN's situated terms (the reader's view, the
facing, the flip, the corner of a named pair, levels) reproduce what physics already has, before they are trusted where
it has nothing. It is a translation into SPN's terms, not a discovery. A result here that looks new should first be
looked for in radiometry and heat transfer.

## The law in SPN's words, in brief

Tom, 10 October: "so we could at least explain the inverse square law using our vocabulay?" Yes, as a reading of the
law, with two bridges to physics named. [reading; each step's physics is in §1–§4]

1. **The source sends unsituated; the reader receives situated.** The source sends to every direction alike, the full
   turn, from nowhere in particular. The reader is somewhere: one standpoint, holding one step H of view per address.
2. **Per address, nothing changes.** Wherever the reader stands, each address the source fills is as bright as ever (the
   radiance theorem, §0). Distance changes only how many addresses the source fills.
3. **Name the pair.** The pair is the source's size Δ and its distance d, and the reading is their ratio. Its corner is
   where they are equal, d = Δ. That is the corner of this pair, a point set by amounts, not the reader's h = v.
4. **Before that corner, near:** the source fills the view, and the reading is in proportion: stepping back costs
   almost nothing.
5. **Past that corner, far:** the reading is in levels. Each level of distance (a doubling) halves the source's size in
   each of the two directions across the line of sight, so it loses two levels of light per level of distance. That is
   the inverse square.
6. **The flip joins the two sides.** Near and far are one expression read through the flip; for a disc, s²/(1 + s²).
   It is half at the corner, symmetric about it, and a share of a two-part split, since both ends face each other
   (§4, NRF).
7. **The reader's own limit is a second pair:** the source's size against the reader's step.
   - While the source spans many addresses, distance costs addresses.
   - Once it is under one, distance costs brightness in that one.

   The switch is the resolution limit, again a corner of a named pair (§3). The photon gives a third limit, on the
   signal's side.
8. **Nothing is lost, only divided.** Summed over every standpoint at that distance, the light is all there. One reader
   holds one share. The inverse square is the cost of being situated (SPN §3.3).

**What the vocabulary explains:**
- where the switches are: at the corners of named pairs;
- that the near and far sides are one law, read through the flip;
- why levels are the natural bookkeeping past the corner;
- the difference between the source's view from nowhere and the reader's from somewhere.

**What physics supplies, the two bridges:**
- **Conservation:** that nothing is lost on the way (steps 2 and 8).
- **The exponent:** the 2 is the number of directions across the line of sight, which comes from space having three
  dimensions (step 5). SPN once read it from the sweep's two parties and withdrew that on 9 October. The geometry says
  how to read the fall-off, not how steep it is.

So this is an explanation of the law in SPN's terms, not a derivation of it.

## 1. The law as physics holds it

- **Derived from conservation and three dimensions** [physics]. A point source sends a fixed amount per second. With
  nothing lost on the way and no direction preferred, the same amount crosses every sphere about it, of area 4πd², so
  E = P/(4πd²). Gauss's law is the general form. In D dimensions the law is 1/d^(D−1).
- **Tested as a bound on the exponent** [physics]. The tests do not measure "2"; they bound a departure from it, as an
  exponent 2 + δ or a short-range correction, and every bound is consistent with zero.

  | force | test | how close to 2 |
  |---|---|---|
  | light | photometry on an optical bench, from Bouguer and Lambert on | percent level, limited by the source's size and evenness |
  | electric | Cavendish's null test (no field inside a charged shell), repeated by Williams, Faller and Hill (1971) | δ within about 10⁻¹⁶; equivalently, the photon's mass bounded |
  | gravity, large | planetary orbits, lunar laser ranging | about 10⁻⁹ over the solar system |
  | gravity, short | torsion balances (Eöt-Wash) | holds to about 50 µm; below that open, where extra dimensions would bend it |

- **Its scope** [physics]. The law is exact only:
  - for a point (§4 is the near field of a source with a size);
  - in empty space (dust and absorption subtract);
  - for flux, not for quanta. Light arrives in photons, and a reading by light gives out where too few arrive (SPN §14,
    "light has a limit too").

So the law is not this corpus's to test. What the corpus can test is its own bookkeeping of the law, and where its
geometry meets the law's edges.

## 2. The law in levels

- **Two levels of light per level of distance** [exact, from §1]. Write light and distance in levels, log₂. Then the law
  reads: each doubling of distance quarters the light, −2 levels per level. In D dimensions it is −(D − 1). Zero points
  drop out of every slope. The magnitude scale is levels times 2.5/log₂10: five magnitudes are 6.644 levels.
- **Measured on real stars** [data]. MAG (`plans/mag-plan.md`) used Hipparcos parallaxes and V magnitudes, with kind from
  the spectrum:
  - G0–G5 dwarfs within 23 pc: −2.02 levels per level (83 stars);
  - K0 giants: −1.93, on a sample later found not to be complete (CNT runs 2–3).

  This checks the bookkeeping, not the law.
- **Counts: three levels of number per level of distance, 1.5 per level of light** [exact, from §1]. For things of one
  kind spread evenly, the number within d grows as d³: 3 levels per level of distance. Light falls 2 per level of
  distance, so number rises 1.5 per level of light. A mix of kinds spread evenly gives the same 1.5, since each kind does.
- **Counts on real stars** [data].
  - On the Gaia Catalogue of Nearby Stars (`plans/gcn-plan.md`, read after run 1, without its distance-dependent cut),
    each main-sequence kind gives 2.93 to 3.00 levels of number per level of distance within 100 pc, and 1.46 to 1.52 by
    light.
  - Hipparcos's bright stars give about 1.2 by light (`plans/cnt-plan.md`). GCN's exploration points to the cause: those
    stars are mostly past 100 pc, of kinds that lie in a thin layer, seen through dust. A count past a layer's thickness
    turns from a sphere's toward a slab's, 1.5 toward 1.0. [reading; untested]
- **The slope reads the dimension** [reading]. Levels of number per level of distance is the counting dimension of what
  is counted: 3 in a ball, 2 in a slab. Levels of light per level of distance is D − 1, the dimension of the sphere the
  light thins over. This is the ordinary counting dimension, not a result of the corpus. (SPN §3.3 once read the 2 as
  the sweep's two parties across the line of sight; that was withdrawn on 9 October as a conclusion transfer. The 2 is
  physics.)

## 3. The two ways a reader meets it

SPN §3.3, "The same signal, a smaller share" [physics, read in SPN's terms; reading]:
- **Per address, nothing changes.** With nothing in between, the brightness per unit of view is the same at any
  distance. Only the number of addresses the object covers falls.
- **The rest thins over more room.** Summed over every standpoint at distance d, d²·(1/d²) is constant: nothing is lost,
  and the signal is divided among more addresses. One reader holds one address's share. The object sends unsituated, the
  reader receives situated; "the gap is the cost of being situated".
- **Two regimes, with the resolution limit between them.**
  - Resolved, while the object covers many addresses: each is as bright as ever, and the count of addresses falls as
    1/d².
  - Unresolved, once it is under one address: all its light lands in one, whose brightness falls as 1/d², the law in its
    textbook form.

  The switch is at one address across: the pair (object's size, the reader's step), an amount, so the resolution limit
  and not h = v.
- **The law has no scale** [physics]. 1/d² has the same form at every distance. A reader with a finite step puts one
  switch into it, and the photon puts another, on the signal's side. How the two limits combine is open (§7).

**In Wander's world** [illustration]:
- BAL: a ball's share of the reader's addresses, s²/π far off, to 0.10%;
- `thin.html`: grains lit times brightest grain is the light caught, 1/v² everywhere;
- GRN run 8: a pair receding under the law, lost at one grain across;
- LAD run 3: light past the resolution limit;
- OLB: the dark sky, each shell giving the same light.

These show the bookkeeping; they do not test it.

## 4. The near field: where a source with a size turns to the law

- **The glowing disc** [exact; SPN §3.2]. Light on the axis of a Lambertian disc of radius a, at distance d, received by
  a flat patch facing it, is E ∝ a²/(a² + d²). With s = a/d (SPN's convention), E/E_max = s²/(1 + s²):
  - inverse square on the far side (s small);
  - saturating near (s large);
  - exactly half at s = 1;
  - and f(1/s) = 1 − f(s): the near law is the far law read through the flip.
- **In levels: the switch is exact and symmetric** [exact; NRF P1]. NRF writes s = d/a. The local slope of the light is
  σ(s) = −2s²/(1 + s²):
  - −1 at s = 1, halfway between the near 0 and the far −2;
  - σ(s) + σ(1/s) = −2, an identity;
  - 10% to 90% of the way over log₂ 9 ≈ 3.17 levels of distance.
- **Other sources** [exact; NRF]:
  - a Lambertian sphere has no near field when distance is counted from its centre: E ∝ (R/d)² exactly, outside it;
  - counted from its surface (s = gap/R), σ = −2s/(1 + s): halfway at a gap of one radius, symmetric, and twice as wide;
  - a line seen by a flat patch: σ = −1 − s²/(1 + s²), halfway at s = 1, symmetric.
- **Where it fails** [exact; NRF P3, P4]:
  - the line counted from every direction (an angle, arctan) switches at s = 0.719, not symmetrically;
  - an isotropic emitter on a flat patch (a solid angle, 1 − cos θ) switches at s = 0.786.
- **The rule found** [reading, after NRF]. The switch sits exactly at the pair's corner, symmetric under the flip, when
  the light counted is a *share of a two-part split*, of the form A(s)/(A(s) + A(1/s)). That is the form
  `plans/near-far-classification.md` calls fair to the facings. The projected solid angle gives it. That is the cosine at
  the source and the cosine at the detector, the standard measure of irradiance: for the disc the share is sin²θ, θ the
  half-angle subtended, and its fairness is Pythagoras. Counting an angle, or a solid angle unprojected, does not give a
  share.
- **Wave fields** [exact; SPN §3.2, `vh/waves.py`].
  - The magnetic field of an oscillating dipole, with the unit λ/2π: the near term's share of the intensity is
    s²/(1 + s²), the disc's law term for term.
  - The electric field: its intensity's bracket is symmetric under the flip, but it is not a share.
  - Diffraction through a round opening, with the unit √(λL): the last bright maximum on the axis falls exactly at
    s = 1 (Fresnel number 1).

  The coil's on-axis field, s³/(1 + s²)^(3/2), is not a share and is not fair: it reaches half at s ≈ 1.30. Of the powers
  of sin θ, only the square is fair.
- **The practitioners' rules sit inside the boundary** [physics, read]. The photometrist's "inverse square to 1% beyond
  five diameters" is s = a/d = 0.1. The opticians' far-field distance 2D²/λ is Fresnel number 1/8. Both are tolerances
  chosen well on the far side; the boundary itself is at the pair's corner.

## 5. The lay has the law's form

ISQ (`plans/isq-plan.md`) [exact]:
- Past the corner the in-place lay places a reading s at 2 − 1/s. Its room per unit s is 1/s², the flip's Jacobian
  exactly, and each level gets 2^−(k+1) of the room.
- **Read with a bridge** [reading]. Read s as d/Δ, a distance in units of a size, the bridge being the size Δ. Then the
  lay places a thing at its angular size counted down from the horizon. Its 1/s² is how fast that angular size shrinks:
  an inverse square in one dimension. Light's inverse square is the angular size squared, the solid angle, in two.
- One form, one origin: the flip. This is not a claim that the lay *is* light. ISQ tested the form; the one-dimension
  against two-dimension reading is untested (§7).

## 6. What stands on what

| claim | standing | where |
|---|---|---|
| E ∝ 1/d² for a point in empty space; exponent 2 within 10⁻¹⁶ (electric) | physics | §1 |
| −2 levels of light per level of distance; 3 of number; 1.5 of number per level of light | exact (from the law) | §2 |
| the bookkeeping on real stars: 2.02; 2.93–3.00; 1.46–1.52 | data | MAG, GCN |
| Hipparcos's 1.2 from a thin layer and dust | reading, untested | GCN exploration |
| resolved and unresolved, switching at one address across | physics, read | SPN §3.3 |
| the disc's near field: halfway at the pair's corner, flip-symmetric | exact | SPN §3.2, NRF P1 |
| the corner exact where the light counted is a share (projected solid angle) | exact cases; the rule a reading | NRF |
| the lay's 1/s² is the flip's Jacobian | exact | ISQ |
| the lay as angular size, light as its square | reading | ISQ |
| the law in SPN's words: where its switches are, near and far as one law, levels past the corner | reading, with conservation and the exponent as bridges from physics | "In SPN's words" |
| the 2 as the sweep's two parties | withdrawn 9 October | SPN §3.3 |

## 7. Open

- **Why the projected solid angle gives a share** (check view factors and their reciprocity first, §0). The cosine at both ends turns a disc's light into sin²θ, and a
  share's fairness into Pythagoras. Is that general? Is every Lambertian source of any shape, seen by a flat patch, a
  share in some ratio of the pair? An exact test: sources of other shapes (an annulus, a square, an ellipse off axis),
  with predictions first.
- **The Cauchy shape.** The disc's light against distance, 1/(1 + (d/a)²), is the Cauchy density's shape in d/a. SPN
  §2.2 and `plans/normalizations.md` have a Cauchy on v/h. Is it the same object, or a coincidence of form? This needs
  the case kept: d/a is a ratio of amounts, v/h of fill levels.
- **One dimension against two.** ISQ's reading has angular size falling one level per level of distance, and light two.
  Stars with measured angular diameters and parallaxes would test the one-level half directly, on data (`papers/physics.md`
  §4).
- **The two limits together.** The resolution limit (one address across) and the photon limit (a few quanta) each end a
  reading. Where both act, which ends it first, and is the boundary between them a pair's corner?
- **D − 1 and the flip.** In D dimensions the law is −(D − 1) levels per level, and the disc's share would be a power of
  sin θ. Only the square is fair (§4). Does the flip's fairness single out D = 3 for light on a surface? This is to be
  worked in exact arithmetic before anything is claimed.
