# NFS: where the near-field sphere goes

19 Nov 2026. SPN R1115. Tom: "The three bars as a 3d cross hair is the cauchy near field sphere. Where that sphere goes
is not entirely clear."; then "Yes", to an exact check.

The three bars are one thumb each (H = 1). There are two candidate places for the sphere of one thumb:

- **S1**, about the eye, radius 1. This is the bars' traces with their pivots at the eye, and R723's near-field sphere.
- **S2**, about the crosshair c = (1, 1, 1), radius 1. This is the bars crossing at the triple corner, and THM's
  one-thumb sphere. The look runs along (1, 1, 1)/√3 and c sits √3 thumbs out.

The read's laws:

- **Direction.** The directions in front are uniform over the hemisphere about the look. On a flat screen square to
  the look, at r = tan α, this is the 2D Cauchy. The share within r is 1 − 1/√(1 + r²), and the heat per unit of screen
  is cos³α.
- **Distance.** The overlay laid by H (R702, R703) is heat per ratio sech(ln d). Normalized, its density in u = ln d is
  (1/π)·sech u, and the share below d is (2/π)·atan d.
- The combined heat is the two together.

## Predictions (written before any run)

- **N1.** S2's rim from the eye is at sin α₀ = 1/√3, r₀ = tan α₀ = 1/√2 exactly. The directions it covers are
  1 − √(2/3) = 0.18350 of the hemisphere.
- **N2.** The rim is not at half heat. cos³α₀ = (2/3)^(3/2) = 0.54433. Half heat is at r = √(2^(2/3) − 1) = 0.76642,
  share 1 − 2^(−1/3) = 0.20630.
- **N3.** The rim at r = 1/√2 is where the three homes (0, 1, 1), (1, 0, 1), (1, 1, 0) land, the points where S2
  touches the faces. It is the exchange partner, about r = 1 (45° off the look), of the thumbs' tips at r = √2:
  (1/√2)·√2 = 1. The tangent length from the eye to S2 is √2.
- **N4.** S1 and S2 meet in a circle at α = 30° (r = 1/√3), its radius ½, in the plane at distance √3/2 from the eye.
- **N5.** S1 holds exactly ½ of the combined heat. The distance law's median is d = 1 on every direction, so the result
  holds whatever the direction law.
- **N6.** S2 holds less than ½ of the combined heat. Computed, not guessed, to 30 digits. Kill if it is ≥ ½.
- **N7.** The combined heat's single hottest point, d = 1 along the look at (1, 1, 1)/√3, lies on S1 and inside S2.
  Its distance from c is √3 − 1 = 0.73205 < 1.
- **N8.** The combined heat is not constant on S2. Kill if its spread over S2 is under 10⁻⁶ of its mean. If it were
  constant, S2 would be a level surface of the heat, a natural place for the sphere.

Classical throughout (tangent cones, the hemisphere's measure). What would be the series' own is which place the
geometry gives the sphere.

## Runs

### Run 1 (19 Nov; `runs/nfs/nfs.py`, output `runs/nfs/nfs-run1.txt`, mpmath 30 digits)

Nothing was killed.

- **N1.** S2's rim is at r = 1/√2 exactly. It covers 0.183503419 of the hemisphere, which is 1 − √(2/3).
- **N2.** The heat at the rim is 0.544331, so the rim is not at half heat. Half heat is at r = 0.766421, share 0.206299.
- **N3.** All three homes land at r = 1/√2, at √2 from the eye. The thumbs' tips land at r = √2. The rim and the
  thumbs are exchange partners about r = 1. The tangent length is √2.
- **N4.** S1 and S2 meet in a circle at 30°, radius ½, in the plane √3/2 from the eye.
- **N5.** S1 holds 0.5 of the combined heat.
- **N6.** S2 holds 0.04711 of the combined heat, under ½ as predicted. This is small because S2 covers only 35.26° and,
  along each of its directions, only the stretch from d₁ to d₂.
- **N7.** The hot point is 0.732 from c, so it is inside S2.
- **N8.** The heat on S2 is far from constant: its spread is 0.80 of its mean, so S2 is no level surface of the heat.

**Post hoc, not predicted** (`runs/nfs/nfs-posthoc.py`, output `nfs-posthoc.txt`). The heat cos³α·sech(ln d) has its
maximum, 1, at the hot point. On S2 its least value is ½: 0.5 − 4.9·10⁻³², reached on S2's far side at α = 34.2646°,
d = 1.65289. So S2 lies wholly inside the region where the heat is at least half its peak. It touches that region's
boundary along one ring and crosses it nowhere. This is found to 31 digits and not yet proved. A proof would show
4c³d − 2√3·c·d + 1 ≥ 0 on S2's far branch, with equality only at the touching ring (using 1 + d² = 2√3·c·d − 1 on S2).

**Reading.** Only S1 is the distance law's median surface (½ of the heat, on every direction, whatever the direction
law). S2 is where the three bars cross. Its rim is the homes' ring, the thumbs' exchange partner. It holds about a
twenty-first of the heat, and it fits inside the half-heat region. Where the sphere goes is still open between the two.
Tom's ruling is needed on whether the post hoc fit (S2 inside the half-heat surface, tangent to it) is the place.

**Ruled (R1116, 19 Nov).** Tom: "The near field is the bar itself, the far field is what is beyond the bar." The bars
pivot at the eye, one thumb long; their tips, swung every way, are S1. So the near-field sphere is S1, the distance
median, ½ of the heat. S2 is where the bars cross, not the near field; its half-heat tangency (post hoc above) stays
unproved and has no role.
