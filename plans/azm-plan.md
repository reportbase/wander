# AZM: V₂ as the azimuth, the hand's second sweep

*14 October 2026 (Tom's local date). Tom, about 3:00: "we have to build out from a strong metaphor, like the sweep of the
hand from the horizontal to the vertical. Right now, our metaphor is a sweep of H to V. but there is another sweep V2,
that is the rotation from parallel to to perpindicular." Then, to Claude's naming of the two sweeps as altitude and
azimuth, about 3:06: "Parallel to perpendicular. are just my terms. Use the correct terms for V2 that you mentioned.
lean on classical theory to explain V2." It follows R236 (the unsituated view h + v + … = 1; the situated views
everything else built from the horizontal, the vertical and the rest) and R235 (the arc where the two facings' rays
cross). Exact arithmetic (mpmath quadrature at 50 digits); predictions written before the script (`azm/azm.py`)
exists.*

**Prior knowledge, stated.** Before this plan, a midpoint grid (1,200 × 1,200) in a scratch computation gave, for the
two angles swept evenly, P(v ≤ h) ≈ 0.3426, P(v₂ ≤ v) ≈ 0.6574 and the near field ≈ 0.2326; and, weighted by the
octant's area, 0.5, 0.5, 0.5 and 1/3. P3 and P5 are therefore not discoveries: they are checks that the closed forms
below are right and agree with a direct count.

## Set-up, with the case kept

**The reader's horizon coordinates.** The reader stands at the centre. The vertical is v. The horizontal plane holds h,
the forward direction toward the other party (home), and v₂, square to it. Two sweeps reach every direction of the
octant h, v, v₂ ≥ 0, all three parties drawn at H (OFS Proposition 3(f)):
- **altitude** a, from the horizontal (a = 0) up to the vertical (a = 90°): the hand raised, the sweep from H to V;
- **azimuth** z, around the horizontal plane from the forward direction h (z = 0) to v₂ square to it (z = 90°): the
  hand turned, the sweep that brings in V₂.

The direction is (h, v, v₂) = (cos a cos z, sin a, cos a sin z). No amount enters.

**Classical theory leaned on** (Tom: "lean on classical theory to explain V2"):
- *The horizontal (altitude–azimuth) coordinate system* of spherical astronomy (Smart 1977): altitude above the
  observer's horizon, azimuth round it from a chosen direction. Its horizon and zenith are the observer's own, set by
  where it stands; the equatorial system, by contrast, is fixed to the sky and the same for every observer. The
  theodolite of surveying reads the same two angles, the vertical and the horizontal.
- *Archimedes' hat-box theorem* (*On the Sphere and Cylinder*): a zone of a sphere between two parallel planes has the
  area of the band they cut from the circumscribed cylinder, so area on the sphere is proportional to height.
- *Lambert's cylindrical equal-area projection* (Lambert 1772), the map form of the same theorem: (azimuth, height) is
  equal-area.
- *The marginal of one coordinate on the n-sphere*, proportional to (1 − t²)^((n − 2)/2): flat only for the ordinary
  sphere, n = 2, which is why the hat-box theorem has no analogue in other dimensions.

## Predictions

- **P1. Each sweep reads its own pair and has its own corner.** The azimuth's reading is v₂/h = tan z, whatever the
  altitude; the altitude's reading is v/√(h² + v₂²) = tan a, whatever the azimuth; h² + v² + v₂² = 1. The azimuth's
  corner, z = 45°, is the vertical half-plane v₂ = h; the altitude's, a = 45°, is the cone where v equals the
  horizontal reach. **Killed if** any of these identities misses by more than 1e-50 on a 200 × 200 grid of (a, z).
- **P2. An even azimuth keeps its own pair's corner, whatever the altitude does.** With z even on [0, 90°], P(v₂ ≤ h) =
  ½ for every weighting of the altitude (tried: even in a, even in height v, and a weight piling up toward the
  horizon, cos² a normalised); and with a even, P(v ≤ √(h² + v₂²)) = ½. **Killed if** any of these, by quadrature,
  differs from ½ by more than 1e-40.
- **P3. Even in both angles is not the even octant.** With a and z both even, the pairs neither sweep reads leave their
  corners: P(v ≤ h) = (4/π²)∫₀^(π/2) arctan(cos z) dz, P(v₂ ≤ v) = 1 − P(v ≤ h) (the azimuth exchanges h and v₂), and the
  near field (h the largest) = (4/π²)∫₀^(π/4) arctan(cos z) dz. **Killed if** these closed forms, by quadrature, differ
  from a direct count over a 2,000 × 2,000 midpoint grid by more than 2 × 10⁻⁵, or if P(v ≤ h) ≥ 0.4 or the near
  field ≥ 0.3.
- **P4. Archimedes: the even octant is even in azimuth and even in height, not in altitude.** The octant's area between
  heights v₁ and v₂ and azimuths z₁ and z₂ is (z₂ − z₁)(v₂ − v₁), whatever the patch: Lambert's map (z, v) is
  equal-area, and the altitude's density on the even octant is cos a. **Killed if**, for 100 random patches, the area
  integrated from the sphere's element cos a da dz differs from (Δz)(Δv) by more than 1e-45.
- **P5. Swept that way, every pair keeps its corner.** With z even and v even, P(v ≤ h) = (2/π)∫₀^1 du/√(2 − u²) = ½,
  likewise for the other two pairs; the near field is (2/π)·arcsin(½) = 1/3; and the readings (v/h, v₂/h) have the
  two-dimensional half-Cauchy of OFS Proposition 5(e): P(v/h ≤ A, v₂/h ≤ B) = (2/π)∫₀^(atan B) A cos z/√(1 + A² cos² z) dz
  equals ∫₀^A∫₀^B 2/(π(1 + a² + b²)^(3/2)) db da. **Killed if** any median differs from ½ or the near field from 1/3 by
  more than 1e-40, or the joint distribution at (A, B) = (1, 1), (2, ½), (½, 3), (10, 10) differs from the
  two-dimensional half-Cauchy's by more than 1e-30.
- **P6. The hat-box belongs to three unit relations.** On the even quarter circle (two unit relations, one sweep) the
  height v = sin θ of an even turn has density (2/π)/√(1 − v²), not flat; on the even octant (three) it is flat; on the
  even orthant of four unit relations it is (4/π)·√(1 − t²) on [0, 1]. So "raise evenly in height" is the even sweep
  for three parties only; with two the even sweep is the turn itself (the Cauchy), and with more the raise is weighted
  otherwise. **Killed if** a direct count of the height, on 10⁶ even directions of each (drawn from the even measure by
  the method of normal coordinates, seeded), departs from the stated density by more than 4 standard errors in any of
  10 equal bins.

## What the run would and would not show

All six are classical; the run checks that V₂ read as the azimuth is stated without a slip, and what "evenly" must mean
when a reader reaches the octant by two sweeps. It does not show that a reader sweeps this way; that is the metaphor
(R237).

## Runs

### Run 1 (14 October; `python3 azm/azm.py`, about 50 s)

```
P1: not killed. v2/h = tan z, v/√(h² + v2²) = tan a, h² + v² + v2² = 1; worst 5.97e-59
P2: not killed. P(v2 ≤ h) = ½ under each altitude weight, P(v ≤ reach) = ½; worst 0.0
P3: not killed. P(v ≤ h) = 0.3425834779, P(v2 ≤ v) = 0.6574165221, near field 0.2326315334; grid 0.342576, 0.657424, 0.232632; closed forms vs grid 7.7e-06
P4: not killed. 100 patches: area = Δz·Δv to 4.86e-62 (Lambert's map equal-area; altitude density cos a)
P5: not killed. medians ½, ½, ½ and near field ⅓ to 0.0; joint law = the 2D half-Cauchy to 7.78e-62
P6: not killed. 2 relations: worst 2.07 s.e.; 3 relations: worst 1.51 s.e.; 4 relations: worst 1.73 s.e. (densities (2/π)/√(1 − t²), 1, (4/π)√(1 − t²))
```

Nothing killed. Before the first run three things in the script were set right, none a prediction: P1's bound had been
written as ten times the plan's 1e-50, and was put back to 1e-50 with the working precision raised to 60 digits; a
duplicated line in P5 was removed; and P6's bin probabilities were moved from floats to mpmath (a float at t → 1 would
have divided by zero in the two-relation density).

**What it shows.** V₂ is the azimuth: the reader's second sweep, round the horizontal plane from the forward direction
to square to it, with its own reading v₂/h = tan z and its own corner at 45°, as the altitude, the sweep from H to V,
has v/√(h² + v₂²) = tan a and its corner at 45°. Together they reach every direction of the octant, as altitude and
azimuth reach every direction of an observer's sky. An even azimuth keeps its own corner however the altitude is
weighted. But "evenly" has to be said per sweep: even in both angles, the pairs neither sweep reads leave their corners
(v against h at 0.343, the near field 0.233 instead of a third). Swept evenly over the octant, the azimuth is even in
angle and the altitude even in height, Archimedes' hat-box theorem and Lambert's equal-area map; then every pair keeps
its corner, the near field is a third, and the readings are OFS Proposition 5(e)'s two-dimensional half-Cauchy. The
even-in-height raise belongs to three unit relations only: with two the even sweep is the turn itself, and with four
the height is weighted √(1 − t²).
