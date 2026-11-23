# GRV: gravity sorted by direction

23 November 2026. Tom: "Let's compare the cauchy,  inverse square laws and gravity.    See read write paper", "Gravity requires two
writes.  Parallax requires two reads.", "in this case the read is not shv because the mass of both hemispheres is read.", "I think we
can look to cauchy for inspiration.   Gravity is the stage, physics is the play", then "Proceed" (to pinning it down as an exact check).

## The claim

Newton's pull on a point from the matter about it, g = G ∫ ρ r̂ / r² dV, sorted by direction instead of by place, loses its
distance: dV = r² dr dΩ, so g = G ∮ Σ(Ω) Ω̂ dΩ with Σ(Ω) = ∫ ρ dr, the mass lying along the line in direction Ω (a column). The
directions are the uniform sphere about the standpoint, given before any matter (the stage); what lies along each is the payload;
G is the one constant carried in. Unlike light, nothing on a line hides what is behind it (the column adds), and the sum is taken
with direction over the whole sphere, both hemispheres (opposite columns oppose). Above a flat sheet the vertical pull is 2πG times
the sheet's density averaged with the Cauchy of scale h, the height.

Known beforehand, stated so the run is not mistaken for discovery: every identity here is classical. The direction form is the
volume element in spherical coordinates; the ball's GM/d² and the empty shell are Newton's (*Principia* I, Props. 70, 71, 74), the
shell's cancellation by pairs of cones his own argument; the sheet's 2πGσ and the kernel h/(r² + h²)^(3/2) are the Poisson kernel
of the half-space (upward continuation in geophysics, the factor e^(−kh)); a uniform world's pull growing without bound from one
side is Seeliger's and Neumann's difficulty (1895–96). ISX (`plans/isx-plan.md`) has the light's side. draw's labs were searched
for gravity, the Poisson kernel and upward continuation: nothing. What is tested: that the sorting is exact, what the scale test
moves, and three places it could fail (V3's cube, V6's one hemisphere, V4's quadrature). It is arithmetic, not evidence about the
world, and no new physics.

## Predictions (committed before any run)

mpmath at 50 digits; "to 10⁻³⁰" means agreement past 30 digits. G = ρ = 1 unless said.

- **V1** A uniform ball of radius R seen from d > R: the pull by columns, 2π ∫₀^α 2√(R² − d² sin²θ)·cos θ·sin θ dθ (sin α = R/d),
  equals (4/3)πR³/d² at d/R = 1.01, 2, 10, 1000 (to 10⁻³⁰), which is (4/3)R times the cosine-weighted share π(R/d)². Kill: any miss
  past 10⁻²⁰.
- **V2** Inside a thick spherical shell (radii 1 and 1.5) at points 0.3 and 0.9 from the centre: along 40 seeded directions the
  column toward u equals the column toward −u (to 10⁻³⁰), so the pull is zero pair by pair. Kill: any pair unequal past 10⁻²⁰.
- **V3** The pairing is the sphere's: inside a shell between two concentric cubes (half-sides 1 and 1.5) at the point
  (0.3, 0.2, 0.1), opposite columns differ (by more than 10⁻³ on at least half of 40 seeded directions) and the pull is not zero
  (its size above 10⁻³). Kill: all pairs equal to 10⁻⁶, or the pull under 10⁻⁶. (Claude's guess, not derived.)
- **V4** Above a sheet of density σ(x) = 1 + ε·cos(kx) (no change along y), at height h: the vertical pull by quadrature of the
  kernel, ∫ σ(x′)·2h/((x − x′)² + h²) dx′, equals 2π(1 + ε·e^(−kh)·cos kx) at (k, h, x) = (1, 1, 0), (3, 0.5, 0.7), (0.2, 4, 2)
  with ε = 0.3 (to 10⁻²⁰); with ε = 0 it is 2π at h = 10⁻³, 1, 10³ (the height gone); the kernel over 2π is the Cauchy of scale h
  (it integrates to 1 to 10⁻³⁰), and in two dimensions h/(2π(r² + h²)^(3/2)) integrates to 1 over the plane (to 10⁻²⁰) and is a
  quarter of the wedge's 2/(π(1 + a² + b²)^(3/2)) at h = 1 on each quadrant. Kill: any miss past 10⁻¹⁰.
- **V5** Scale test on V1's ball and two test points (d = 2R and 5R): lengths × k at fixed density, each pull × k; at fixed mass,
  × 1/k²; in both the ratio of the two pulls (25/4) and the share π(R/d)² unchanged, for k = 10⁻³, 7, 10⁶ (exact fractions). So
  the pull is a write, its ratio and share reads. Kill: any.
- **V6** One hemisphere has no limit: a uniform half-ball of radius R (z > 0) pulls the point at its flat face's centre by exactly
  πR, by columns (each column R, weighted cos θ over the hemisphere) and by direct volume quadrature (to 10⁻²⁰), at R = 1, 10, 10⁶:
  it grows with the world's extent without end; the whole ball, both hemispheres, pulls its centre by 0 at every R. Kill: either
  form off πR, or the whole ball not 0.
- **V7** A shell's distance is not read: a thin cap of a sphere about the standpoint, surface density σ = 1, half-angle α = 0.4,
  pulls by π sin²α at radius 1, 10, 1000, by direct quadrature over the cap's area with 1/r² (to 10⁻³⁰). Kill: any dependence on
  the radius past 10⁻²⁰.

## Runs

(appended below as they come out; nothing above this line edited afterwards)

### Run 1 (23 Nov 2026; `runs/grv/grv.py`, output `runs/grv/grv-run1.txt`): V3 killed in one clause, by my guess

- V1 not killed: the ball's pull by columns is (4/3)πR³/d² at d/R = 1.01, 2, 10 and 1000 (worst 6·10⁻⁵¹), which is (4/3)R times
  the share π(R/d)².
- V2 not killed: inside the spherical shell the column toward u is the column toward −u on all 40 directions at both points (worst
  4·10⁻⁵¹): the pull is nothing pair by pair, not only in total.
- **V3 killed in its first clause.** Between the cubes the pull is not zero (0.01654, the same to 2·10⁻⁶ over 100,000 and 400,000
  directions), as predicted; but opposite columns differed by more than 10⁻³ on 12 of the 40 directions, not on half or more.
  Post hoc: a ray that leaves the inner and the outer cube through faces of one axis has the column 0.5/|uᵢ|, and so has its
  opposite; the pairs differ only where the two exits are on different axes, near the cubes' edges. So a cube's shell cancels pair
  by pair over most of the sky and fails only toward its edges. The count was my guess; the claim it stood for (the pairing is the
  sphere's) is not killed, but it is narrower than I wrote it.
- V4 not killed: the sheet's pull is 2π(1 + ε·e^(−kh)·cos kx) at the three cases (worst 10⁻⁵⁰); over a uniform sheet it is 2π at
  h = 10⁻³, 1 and 10³; the kernel over 2π totals 1; in the plane h/(2π(r² + h²)^(3/2)) totals 1 at h = ½, 1, 3 and is a quarter of
  the wedge's law.
- V5 not killed: at one density the pull goes as k, at one mass as 1/k²; the ratio of the two pulls stays 25/4 and the share ¼.
- V6 not killed: the half-ball pulls its face's centre by πR by columns and by cylinders at R = 1, 10 and 10⁶; the whole ball by 0.
- V7 not killed: the cap pulls by π·sin²(0.4) = 0.476411986899 at radius 1, 10 and 1000.

Said plainly: V5 is an identity of V1's closed form, V7's radius cancels inside its own integrand, and the wedge clause of V4 is
algebra; none of the three could fail as arithmetic. What could fail were V1 and V4 (quadrature against a closed form), V2 (a
geometric fact about chords), V3 (a guess, and it did in one clause) and V6's cylinder form against its column form.

What the run supports, as a sorting of known results and no more: Newton's pull is exactly a sum over the directions about a
standpoint of the mass along each, with no distance left in it (V1, V7); it adds along a line where light takes the first thing
met; it is taken over both hemispheres with direction, and only so does a uniform world give a finite answer (V2, V6: one
hemisphere of a uniform world pulls by πR, growing without end; both by 0); above a sheet it is the Cauchy of the height laid on
the density (V4), the height its level of detail, e^(−kh); and its size is a write while its ratios and shares are reads (V5).

### After run 1: Tom's reading (23 Nov 2026), recorded in his words; not a run, and no ruling is numbered here

Tom: "I think the idea that gravity is like a read, not a read, but the same in some ways,  an invarient like the cauchy heat map",
then "Gravity is  the invarient combined heat map of writes.  Not calculated but combined like paralax reads." Earlier the same day:
"Gravity requires two writes.  Parallax requires two reads.", "in this case the read is not shv because the mass of both hemispheres
is read.", "Gravity is the stage, physics is the play".

Against the run, what each part rests on:
- *The invariant heat map*: the weight over directions is fixed before any matter and the same whatever the matter is (V1, V7);
  above a sheet it is the Cauchy of the height, totalling 1 at every height (V4). Its total not changing with the arrangement is
  Gauss's law, conservation of flux in three dimensions (classical; not tested here).
- *Of writes*: what is laid on the map is mass, an amount; the pull's size moves with the scale, its ratios and shares do not (V5).
  So it is like a read in its map and not a read in what the map carries.
- *Combined, not calculated*: each mass lays its own map and the maps add, as two reads of a parallax cross: the geometry does the
  combining and no one works it out. Reads combine by crossing and give a place, with nothing carried in; writes combine by adding
  and give a pull. In Newton's gravity the adding is exact (superposition). **A limit, stated so it is not lost:** in general
  relativity the maps do not simply add (the field is its own source), so "combined" is exact only in the weak field.
- *Both hemispheres*: V2 and V6.

Standing: a reading of known physics; it predicts nothing new as it stands.

Tom, later the same day: "gravity is the dhv read, two dhv reads combinin cleanly like cauchy shv reads". What it rests on, and
where it stops:
- *Combining cleanly, exactly*: the Cauchy is the Poisson kernel of the half-plane, and two of them compose to a third with the
  heights added, P_h ∗ P_k = P_(h+k) (the family closed under its own combining; *Reads and Writes* §5, "The Cauchy averages to
  itself"). Carrying a sheet's pull up by h and then by k is the same composition, since V4's kernel is that Cauchy: one semigroup
  for both. And any two pulls add to a pull of the same kind (each is harmonic outside its matter, and sums of harmonic fields are
  harmonic). Classical; the composition is not tested in run 1.
- *Where it is not the Cauchy's closure*: two Cauchys sum to one Cauchy, exactly, at any separation. Two masses' pulls sum to one
  mass's pull (the total at the centre of mass) only far off, the next terms down by (size/distance) each order (PAY, P4).
- *The word*: the paper's dual hemispherical vantage is "held from no standpoint". Gravity's read is both hemispheres from one
  standpoint. If gravity is the DHV's read, the DHV has a read and not only a blueprint, and that sentence of the paper changes:
  Tom's to rule.

Tom: "The combined gravity dhv read creates the fingers thhe physics paints". What known physics has of it (nothing run here):
- *The fingers are the paths light takes*, and gravity lays them: with no mass they are straight and the uniform turn's; with mass
  they bend (gravitational lensing). At the standpoint the fingers are still the uniform turn, the Cauchy exact; what gravity
  sets is where each finger leads.
- *It moves addresses, not paint*: lensing keeps surface brightness along each line (Liouville's theorem; a static lens changes no
  colour); it re-maps directions and with them a source's share of the sky. That is the paper's own split, an operation on
  addresses that leaves the payload, as aberration is in "A moving sky".
- *By the same columns*: a thin lens bends by its mass projected along the line of sight, Σ, the column of this plan's claim, the
  bendings of separate masses adding in the weak field.
- *Limits*: the bending is twice what Newton's pull alone gives (general relativity; 1919); in a strong field the bendings do not
  simply add. Classical and observed; the sorting a reading. It asks one thing of *Reads and Writes*: "the fingers are given by the
  turn" holds at the standpoint, and where they lead is laid by the combined pull. Tom's to rule.
