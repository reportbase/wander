# THM: three thumbs meeting at the corner

5 November 2026. Tom, of `crosshairs.html`: "seems to me your doing the 2d cauchy here. 3d cauchy would be centered at the
crosshair and extend out from there. you have the cauchy on the ground."; "seems to me there are three thumbs, and they all
intersect at the corner. one for vertical, on for horizontal and one for depth."; "the distance to the corner is the depth
sweep, 1 thumb. this is then intersected with the horizontal and vertical sweeps, each also 1 thumb."; then, of the build
(R670, the look down the thumbs' diagonal): "let the math tell us. this is one interpretation of it."

So the question is not how to draw it but what the geometry forces. Exact checks only (sympy, mpmath); nothing from
Wander's world. Known beforehand: WDG run 1 (the octant's even measure is the 2D Cauchy of (v/h, v₂/h), every pair at its
corner, the near field in both a third), AZM (the even octant even in azimuth and height), Proposition 5(e), `wedge.html`'s
view from home (the triangle, the pairs' corners its medians), the flat screen's cos³ (R312), draw's SMP census.

## Setting

Three thumbs, unit vectors e₁, e₂, e₃ square to each other at the eye (horizontal, vertical, depth). A direction n with
n·eᵢ ≥ 0 for all i is in the wedge (the octant). Its readings are the pair ratios (n·eᵢ)/(n·eⱼ); pair (i, j)'s corner is
n·eᵢ = n·eⱼ, a plane through the eye. Directions are laid evenly by turning (the uniform measure on the sphere). A look ℓ
(a unit direction) has a flat screen square to it; "the Cauchy centred on the crosshair" is read as: the density of
evenly laid directions on that screen is greatest at the crosshair (the screen's centre, ℓ).

The two conditions Tom gives: (A) the Cauchy is centred on the crosshair; (B) the crosshair is the corner of all three
thumbs at once (where every pair reads alike). And (C), each sweep one thumb at the corner.

## Predictions (written before any run)

- **T1.** For every look ℓ, the even directions' density on the flat screen at unit distance is cos³ of the angle off ℓ
  (in screen terms (1/2π)(1 + r²)^(−3/2) per unit area, r the screen radius), greatest at the crosshair. So (A) holds for
  every look: it does not pick one.
- **T2.** The three pairs' corner planes (n·e₁ = n·e₂, n·e₂ = n·e₃, n·e₁ = n·e₃) meet in exactly one line, the diagonal
  (e₁ + e₂ + e₃)/√3, and the wedge's half of it. So (B) holds only for the look down the diagonal.
- **T3.** (A) and (B) together force the look down the diagonal: the interpretation built in R670. The other reading
  offered (the look along the depth thumb, the crosshair reading v/h = v₂/h = 0) satisfies (A) but not (B): there the
  crosshair is home for two pairs, and their corners lie 45° off it.
- **T4.** At the corner each thumb reaches the same amount; if that is one thumb (C), the corner is √3 thumbs along the
  look (the cube's diagonal), and each thumb is arccos(1/√3) = 54.7356° off the look. Whether "the distance to the corner"
  is the reach along one thumb (one thumb) or the length along the look (√3) is (C)'s choice; the math gives both and
  their ratio √3, no third.
- **T5.** Down the diagonal, the wedge's edge (a thumb reading zero) is the plane n·eᵢ = 0, arcsin(1/√3) = 35.2644° off
  the look at its nearest; within that cone every direction is in the wedge; the wedge holds 1/8 of all directions; the
  share of each pair below its corner is ½; the share with one given thumb largest (that thumb's near field against both
  others) is ⅓; each of the six chambers 1/6 (WDG, AZM restated).
- **T6.** A view of half-angle 42° vertically by 53° horizontally (an 84° field across the short side of a 16:10 screen,
  as on the page), looking down the diagonal: the share of its screen area inside the wedge is less than ½ (stated before
  computing; the cone of T5 is inscribed, the view's corners lie past it).
- **T7.** Every reading (n·eᵢ)/(n·eⱼ), and each thing's reach in thumbs (p·eᵢ)/H, is unchanged when every length and H are
  multiplied by k.
- **T8.** Along the look (the diagonal), the density on the screen falls as cos³; at the wedge's nearest edge (35.26°) it
  is (2/3)^(3/2) = 0.5443 of its peak, at the thumbs' own directions (54.74°) (1/3)^(3/2) = 0.1925.

Kill conditions: any identity off by more than 10⁻²⁰ at 50 digits; T2 or T3 finding a second look where all three
corners meet; T6 at or above ½.

## Runs

(below this line, as they came out)

### Run 1 (5 Nov 2026; `runs/thm/thm.py`, output `runs/thm/thm-run1.txt`)

- T1 not killed: the hemisphere's (1/2π)(1 + r²)^(−3/2) integrates to 1 and falls from r = 0, for every look.
- T2 not killed: the three corner planes' normals have rank 2; their one common line is x = y = z, the diagonal.
- T3 not killed: looking along the depth thumb the crosshair reads 0 and 0 (home of two pairs, the third pair 0/0);
  looking down the diagonal it reads 1, 1, 1.
- T4 not killed: the corner √3 thumbs along the look; each thumb 54.735610° off it.
- T5 killed by my set-up: the quadrature across the corner's discontinuity gave P(v ≤ h) = 0.4999909, 9·10⁻⁶ from ½
  against my 10⁻⁶. The ½ is exact by the swap symmetry (and the ⅓, ⅙ by WDG run 1); my tolerance did not allow for a
  quadrature over a step. The edge 35.264390° off the look as predicted.
- T6 killed: the wedge takes 0.512 of the view's screen area (0.503 to 0.514 as the view turns about the look), not
  under ½. My guess was wrong: the inscribed cone (35.26°) is most of a 42° × 53° screen, and the wedge's triangular
  outline reaches past the screen's corners in three directions.
- T7 not killed: every reading unchanged by k.
- T8 not killed: cos³ at the wedge's nearest edge 2√6/9 = 0.5443, at the thumbs √3/9 = 0.1925.

What the math says. "The Cauchy centred on the crosshair" (A) holds for every look: it is the flat screen's cos³ about
whatever is looked at, so it picks nothing. "The crosshair the corner of all three thumbs" (B) holds for one look only,
down the thumbs' diagonal, since the three corners meet in one line. So (A) and (B) together force R670's construction;
it is not one interpretation among several. Looking along the depth thumb puts the crosshair at home, not the corner.
And with each thumb reaching one thumb at the corner (C), the corner is √3 thumbs along the look: "the distance to the
corner is the depth sweep, 1 thumb" holds for the reach along the depth thumb, not for the distance along the line of
sight; the two differ by √3, and no thumb lies along the line of sight.

## Run 2: the one-thumb circle (predictions written before the run)

5 November 2026. Tom, of the fidelity toggle (R672): "The blur does not look correct. Things don't blur, they get
compressed. Would there not be a 1 thumb circle around the cross hairs, no distortion at the corner and proportional
distortion around it. But that raised the question, where is the corner and home."; then "let the math tell us".

Setting as above: thumbs e₁, e₂, e₃ of length H, the look down their diagonal, the crosshair's point C = H(1, 1, 1) (each
thumb reaching one thumb, T4), the eye at the origin. Claude's answer before this run offered three sweeps (the thumbs'
pairs, a turn away from the look, a sideways offset at the target's distance) and guessed the sideways circle would follow
H. Predictions:

- **U1.** The ball of radius one thumb about C touches each face of the wedge (n·eᵢ = 0), at H(1, 1, 0), H(1, 0, 1),
  H(0, 1, 1): the cube's vertices one thumb back from C along each thumb. Seen from the eye its outline is the cone of
  half-angle arcsin(1/√3) = 35.2644° about the look, the largest cone about the look inside the wedge.
- **U2.** On that outline every reading is ≥ 0; at the three touch points one reading is 0 (home of two pairs, the
  horizon of their reciprocals) and the remaining pair reads 1; nowhere else on the outline is a reading 0.
- **U3.** In the plane the same construction (one thumb about (H, H)) touches both axes at (H, 0) and (0, H); its outline
  is ±45° about the look: home and the horizon, the whole quarter turn.
- **U4.** The cone holds 4(1 − √(2/3)) = 0.73401 of the wedge's directions (uniform measure); the rest lie in the
  triangle's three corners, out to the thumbs at 54.7356°.
- **U5.** The pair levels ℓᵢⱼ = ln(n·eᵢ/n·eⱼ) vanish at the crosshair with Σℓᵢⱼ² round about it to second order (no
  distortion at the corner); the worst pair's level max|ℓᵢⱼ| grows in proportion to the angle off the look, its contours
  hexagons, not circles (max/min ratio 2/√3 round the crosshair). The worst grain (π/K)·cosh(max|ℓ|) is stationary at the
  crosshair and grows without bound toward the touch points, as (reading)⁻¹/2: proportional.
- **U6.** The sideways reading at the target's distance, (lateral offset)/H, is √3·tan α, a reading (H follows the
  target, so the target's distance is √3 thumbs whatever H is); its corner, one thumb aside, is at 30° off the look, fixed.
  It does not follow H (Claude's guess before the run was that it would). Only with H held while the eye moves to distance
  D does it move, to atan(H/D).
- **U7.** A turn measured from the look has its corner at 45° (tan α = 1), unchanged by H, past the view's short edge
  (42°); the hemisphere's share within it 1 − 1/√2.

Kill conditions: an identity off by more than 10⁻²⁰ at 50 digits; a reading of 0 on the outline away from the touch points;
U4's share off its closed form by more than 10⁻⁸; U5's ratio not 2/√3.

### Run 2 (5 Nov 2026; `runs/thm/thm2.py`, output `runs/thm/thm-run2.txt`)

- U1 killed by my check, not by the geometry: the three touch points are H(0, 1, 1), H(1, 0, 1), H(1, 1, 0), each one
  thumb from C, each 35.2643896828° off the look, and the outline's half-angle the same; but sympy left
  acos(√6/3) − asin(√3/3) unsimplified, so the exact test read false. The difference is 0 to 191 digits.
- U2 not killed: on 3,600 points of the outline the least component never goes below 0 (−7·10⁻⁵²), and is 0 at exactly
  three, the touch points; there the remaining pair reads 1.
- U3 not killed: in the plane the outline runs from 0° to 90°, home to the horizon.
- U4 not killed: the cone holds 4 − 4√6/3 = 0.734013676 of the wedge.
- U5 killed by my set-up: Σℓ² = 9ε² (round, no φ) and the worst level's ratio 2/√3 hold, but my walk "toward the touch
  point" went the other way, toward the thumb e₃ (two readings falling together), so no reading reached 0. Read as it
  came out: toward a thumb the worst grain at the outline is only ×2.12 (the least reading 0.251), still finite.
- U6 not killed: the sideways corner at 30.0000000000°, whatever H.
- U7 not killed: the turn from the look has its corner at 45°, 1 − √2/2 = 0.2929 of the hemisphere within it.

## Run 3 (predictions written before the run)

- **U1′.** As U1, each angle checked to 10⁻⁴⁰ at 50 digits instead of by symbolic simplification.
- **U5′.** Walking from the crosshair toward a touch point, along the great circle to (1, 1, 0)/√2, the worst grain
  cosh(max|ℓ|) times the least reading tends to ½ as the walk reaches the outline (the grain proportional to 1/reading),
  and the worst grain passes ×2.12 (the value on the outline toward a thumb) before 35°, so the outline is not a contour of
  the grain: the grain is hexagonal-to-triangular, unbounded at the three touch points, bounded between them.

### Run 3 (5 Nov 2026; `runs/thm/thm3.py`, output `runs/thm/thm-run3.txt`)

- U1′ not killed: the three touch points lie exactly one thumb from C and on the 35.2644° outline (to 50 digits).
- U5′ not killed: toward a touch point the worst grain × the least reading goes 1, 0.84, 0.64, 0.53, 0.508, 0.5000 (at
  35.264°), so the grain grows as 1/(2·reading); it passes ×2.118 (the outline's value toward a thumb) at 25.2°.

What the math says (runs 2–3). One thumb about the crosshair's point is a ball that touches the wedge's three faces, at the
cube's vertices one thumb back along each thumb; from the eye its outline is the circle 35.26° about the look, the largest
circle about the crosshair inside the wedge, holding 73.4% of the wedge's directions. So Tom's one-thumb circle is there,
and it is fixed: H follows the target, so the circle never changes size on the screen. The corner is its centre, the
crosshair, where every pair reads 1. Home is on it, at the three touch points, where one reading is 0 (and its reciprocal
the horizon); in the plane the same circle runs from home to the horizon, the whole quarter turn. So the circle does not
mark where compression begins. It runs from the corner out to home. Inside it there is no distortion at the corner (Σℓ² =
9ε², round to second order, the grain stationary) and the distortion grows outward, in proportion to 1/reading toward
home. The grain is not round: its contours are hexagons near the corner (2/√3 between the worst and best ways), unbounded
at the three touch points and only ×2.12 at the outline between them, toward the thumbs. Past the circle at the touch
points lies another wedge (a reading below zero), and between them the triangle's corners, out to the thumbs at 54.74°. The
sideways reading at the target's distance has its own corner at 30°, also fixed (Claude's guess that it follows H was
wrong); a turn from the look has its corner at 45°, past the view's short edge.
