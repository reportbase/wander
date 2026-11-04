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
