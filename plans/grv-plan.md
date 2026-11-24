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

Tom's summing up: "Gravity is just the dhv version of the shv cauchy read." Side by side, each line marked:
- one hemisphere, with a look | both hemispheres, no look (V2, V6).
- no amount laid on it | mass laid on it (V5).
- unsigned: no reading carries a sign | signed: opposite sides oppose (V2).
- no mean (the tail does not total) | a mean, the centre of gravity; with one hemisphere only, no limit either (V6, πR).
- totals 1 | totals the mass enclosed (Gauss's law; classical, not run).
- two combine to another, heights adding | two add to another pull; above a sheet the same kernel and the same adding (V4).
- the first thing on a line | everything on the line (the column; V1, V7).
"Just" is the part not shown: the list is of likenesses and exact identities in particular cases (the sheet), not a derivation of
gravity from the Cauchy. A reading; nothing new is predicted.

Tom: "Gravity is not a substance or particle.  Its a heat map." Against what is observed (nothing run):
- *Not a substance*: general relativity's own position (the shape of space and time, no medium). Consistent.
- *Not a particle*: no experiment has seen gravity come in quanta; the graviton is a hypothesis. Consistent with everything observed,
  and not established: nothing has shown it is not quantised either.
- *What a heat map must still carry*: gravity's changes travel, at light's speed, as waves (seen directly since 2015), and they
  take energy from their sources (the Hulse–Taylor pulsar's orbit shrinking at the rate predicted, 1975 on). A map that is redrawn
  outward with a delay gives the waves (the read is of an earlier write); that the redrawing costs the sources energy is not in
  the heat-map picture as it stands. An open point for the reading, not a kill: nothing here was predicted.

Tom (24 Nov): "Let's say gravity sweeps outwards from the center of gravity in every directions.   Think cauchy in all directions at
once." What it comes to, from results already in the corpus (nothing run here):
- *The source's side of the same kernel.* A point mass's pull, counted as flux, is uniform over the sphere of directions about it
  (Gauss: 4πGM in all, whatever surface catches it). On any flat plane a distance d off, the flux through the plane is
  GM·d/(d² + r²)^(3/2), which is 2πGM times the two-dimensional Cauchy of scale d: the lighthouse, sending in every direction at
  once, its standpoint the mass, m + i·d. Half of all the flux crosses any plane, at every d; a share 1 − 1/√(1 + (r/d)²) lands
  within r of the foot (half within √3·d); the inverse square GM/d² is the kernel's height at the foot. ISR has the same for light
  (`plans/isr-plan.md`); V4 here is the receiver's side, the same kernel with source and receiver exchanged (reciprocity).
- *"From the centre of gravity"* is exact outside a spherically symmetric body (Newton; V1) and for one point mass; for any other
  body it is the first term, the next down by (size/distance) each order (PAY, P4).
- *"Sweeps"* in the paper's sense (R454): the geometry's, not an act in time; nothing travels in a steady pull. A change in the
  source does travel, at light's speed.
A reading of known results; the sorting ours.

Tom (24 Nov): "Classical says not much about cauchy". Agreed, in this sense. The kernel is in classical potential theory under
another name, the Poisson kernel of the half-space (geophysics' upward continuation of gravity data, e^(−kh), is the same fact);
what the classical texts do not say is that it is the Cauchy, the law of the uniform turn from a standpoint, so that the pull on a
plane is a read's own measure laid over the mass (R1071: the classical tools are not the explanation). From memory, no search made;
no claim that the naming is absent from print.

Tom (24 Nov): "The tell is that when a body moves in lock step with another body, their center gravity combines, if not it is
reduced." Claude's reading, not ruled, nothing run:
- *What holds whatever the motion.* Pulls add (the heat maps overlay; V4's linearity), and from far off any system reads as its total
  mass at its centre of mass, the next term down by (size/distance)² (PAY P4). In Newton's gravity neither needs lock step: two
  bodies flying apart still have one centre of mass, moving steadily, carrying the whole mass.
- *Where lock step does matter.* Bodies that keep their arrangement (rigid, or bound and co-moving) keep the same size, so the
  one-centre reading holds as well tomorrow as today and the pair can stand as one body in a larger system (the tower: Earth and Moon
  as one mass to the Sun, to about (384,000 km / 1 au)² ≈ 7·10⁻⁶). Bodies not in step spread, the size grows, and the one-centre
  reading gets worse with time: the combination is not lost but its accuracy is. That is the sense in which "reduced" is exact.
- *Where the amount itself changes* (relativity, classical results): a system's gravitating mass is its total energy, so a bound
  pair weighs less than its parts by the binding energy and relative motion adds kinetic energy; the sign is the other way round
  from "not in step, reduced" if "reduced" meant the total. A changing arrangement also radiates (the open point above).
Open: which of these Tom means by "reduced".

Tom (24 Nov): "The read write paper shows that there is a clean separation between the address and the payload. I'm saying that
gravity is no different." What run 1 already shows of it, and where it stops (Claude's sorting, not ruled):
- *Exact for Newton's static pull.* g = G∮Σ(Ω)·Ω̂ dΩ is a fixed kernel over directions (on a plane the Cauchy) times the mass met
  along each (the column Σ). The paper's second test passes: change the mass and no direction and no weight of the kernel moves
  (V4: any density under the same Cauchy; V2, V3: the shell's shape changes the columns, never the kernel); and the kernel is the
  same at every size (V5, V7), the amount entering only through the mass and G. Pulls add for the same reason heat maps do.
- *Where it stops.* The separation is linearity. In general relativity the mass also bends the paths (lensing: the payload moves
  light's addresses, noted above) and the field's own energy is a source, so two strong fields do not simply add. Exact in the
  weak, static case; approximate beyond it.

Tom (24 Nov): "I'm saying gravity and observation are similar, not the same.   We can therefor learn about gravity by studying
observation." Taken as a method: carry a result across, state it for gravity before checking, and see whether it is already known
there. Candidates (Claude's, none run, each expected to be classical):
- *One standpoint gives no size.* A read has no V; one reading of a pull gives only M/d², never M or d. *Parallax:* two pulls a
  counted step apart place the source in steps, d₁ = step/(√(g₁/g₂) − 1) for a point mass (the tidal gradient), and the mass then
  needs G carried in.
- *Stepping back blurs, and undoing it is unique but not stable* (R605, R629): a pull read higher is the lower one under the
  Cauchy; continuing it downward multiplies e^(+kh).
- *Order survives, sums do not* (Theorem 6): to try on a pull's direction against its size.
Where they part: a read has one hemisphere and its paint does not add; a pull takes every direction and is a sum of amounts, with a
mean. So results resting on "no sum" should not carry.

Tom (24 Nov): "Notice how my cauchy does not affect your cauchy". In observation: reads are unconnected and do not conflict (R652,
R659); each standpoint has its own heat, the same law, and another observer enters mine only as paint. Carried to gravity
(Claude's, not ruled): each mass's kernel is its own and unaltered by any other mass (superposition; why V4's sheet can be summed
piece by piece), and another mass enters my pull only as payload, a column along some direction. So in both, the other is never in
my addresses, only in what lands on them. Limit as above: exact while pulls add (Newton, weak fields); in general relativity one
mass does alter the other's field.

Tom (24 Nov): "Each write occupies a discreet position in reality  and this means it's affect goes beyond its extent.  Think of
gravity the full extent of the object.    Very strong closs, very weak far away.    So a write has a gradient". Claude's reading,
not ruled, nothing run (the formulas Newton's, checked in V1 and V5):
- *A bounded thing, an unbounded reach.* A write has a size (R896); its pull has no edge, GM/d² at every distance, never zero: like
  the heat's tail, it does not close. "The full extent of the object" as the reach of its pull is then without end.
- *The gradient is the geometry's, not the write's fading.* The flux through any surface round the body is 4πGM at every distance
  (Gauss): the amount is the same far and near, spread over more directions' worth of area. The payload is constant; 1/d² is the
  share. The separation again.
- *The shape of the gradient, in the body's own radii x = d/R (uniform ball):* inside the pull is x times the surface's (in
  proportion, zero at the centre), outside 1/x²; strongest at the surface, not at the centre. The surface is where proportion gives
  way to ratio, as the corner does for near and far; not the exact exchange (x against 1/x², not 1/x). The shape has no unit; the
  amount at the surface, (4/3)πGρR, does.

Tom (24 Nov): "Interesting idea.    The physical border is the near field beyond is the far field." Claude's reading, not ruled,
nothing run. It is R1116 for a thing ("the near field is the bar itself … the far field is what is beyond the bar"), the body's
radius R in the thumb's place. What is already in the corpus for it: PAY P4 (inside a body's radius the expansion runs in powers
of r/R, outside in R/r, the two meeting at r = R and exchanged by Kelvin's inversion r ↦ R²/r, which is the exact exchange here,
on the potential, where the pull's x against 1/x² is not); ISX and NRF (a disc's light half at d = a, E(s) + E(1/s) = πL). The
difference from a read: a read's thumb is chosen and the split moves with it; a thing's border is its own, a size, a write.

Tom (24 Nov): "But the main point is that this is a heat map that every write has intrinsically." The main point of the day's
statements, as Tom gives it. Claude's reading, not ruled: the counterpart of R1119 ("the geometry is … intrinsic to any extent;
the bar has it, does not make it"). A read's heat belongs to any standpoint, the same for all, with no amount in it; a write's
heat map belongs to any thing, the same form for all (the kernel, and the near and far about its own border), with one amount in
it, its mass. "Every" holds in known physics: whatever has energy gravitates, so no write is without one. What differs between
writes is only the amount and the border, both the write's own. No new physics claimed: Newton's law sorted.

Tom (24 Nov): "Two points create the read  geometry, the write of those two points creates the write geometry which is gravity."
Claude's reading, not ruled, nothing run:
- *The same two points, twice.* Taken and picked (R1157), two points give the read geometry: a direction, the turn, the heat, no
  size, one point the pivot and one the trace. Written (each a thing with an amount, their separation an amount), the same two
  points give G·M·m/d²: sizes throughout, and no pivot or trace, the pull the same on both (Newton's third law), which is "a write
  has no face" (R1039) and the dual hemispherical vantage's both-at-once.
- *What it would change, flagged.* R1094 has write geometry as "a thing's own shape with a size, its maker's". "Which is gravity"
  either extends that (a thing's shape and its pull, both sized by the thing) or replaces it; Tom's to say. Known physics leans the
  same way without our help: in general relativity gravity is a geometry (the metric), set by mass and energy. No claim made here
  that the two are one.

Tom (24 Nov), to the flag above: "A write has mass.  Having mass is gravity." Taken as the answer: gravity is not a second thing
added to a write's shape; a write is a thing with a size and a mass, and its pull is what having the mass is. So write geometry
(R1094) stays "a thing's own, with a size", the mass among what is its own. Two precisions from known physics (Claude's): mass
also resists a push (inertia), and that the two masses are one is the equivalence principle, measured, not defined (to about
10⁻¹⁵, MICROSCOPE; from memory); and light, with energy and no mass, gravitates too, so strictly "having energy".

Tom (24 Nov): "So a write has energy not mass?" Claude's answer, not ruled: both, and "a write has mass" stands. Mass is the
energy a thing has in its own rest frame (E = mc²). A write "occupies a discreet position" (Tom, above), so it has a frame in
which it is at rest, and whatever has such a frame has mass. Light has no rest frame and occupies no position: by that it is not
a write but what arrives, and it has energy with no mass. So: every write has mass, and so a pull; the precision "energy" only
says the source of gravity is wider than the writes, light gravitating too (weakly: its energy over c²).

Tom (24 Nov): "So we are taking a static universe,  what it is at one moment." The scope, as Tom sets it; Claude's notes, not
ruled. It is the scope in which the day's statements are exact: Newton's law (Poisson's equation) has no time in it, the heat
maps of all the writes at one moment simply overlaid, as a read is one moment from one standpoint (R648). Left outside by the
scope: anything that changes (a change in a source reaching others at light's speed; waves and the energy they carry, the open
point above). Still inside it: "one moment" across distant things is a convention (R1049), harmless only while nothing moves; and
the strong-field failure of adding, which needs no change in time.

Tom (24 Nov): "So what I'm wondering is if mass has fingers \"gravity\", just like read geometry." Claude's answer, not ruled,
nothing run: yes, and physics has the picture under another name, lines of force (Faraday; Gauss's law is their count). A point
mass's lines leave it evenly over every direction, the uniform turn in all directions at once; on a plane they land as the Cauchy
(the note above); the pull at a place is how thickly they pass through it; they never end (no negative mass to end on), as the
heat's tail never closes. Like and unlike a read's fingers:
- *Like:* laid by the geometry alone, evenly by direction, the same form for every mass; another mass never moves mine (each
  mass's own lines stay straight; only the summed pull's lines curve).
- *Unlike:* all directions, not one hemisphere; and their number is the mass, an amount, where a read's K is a fineness with no
  amount. A read's fingers are painted by what arrives; a mass's fingers are what other masses feel.
Counting lines works exactly only for the inverse square in three dimensions; the lines are a picture, not things.

Tom (24 Nov): "Writing sffects the previous writes around where its written.  Lots of writes in the same location creates mass.
Writes can move, it's not static." Claude's reading, not ruled, nothing run:
- *A new write affects those already there:* its heat map is overlaid on theirs and each feels it, most nearby; and it feels
  theirs, equally (the pull is mutual). R1065's "everything reads and writes", for the pull.
- *Many writes in one place:* the amounts add, so the place's heat map is the sum (V4's piece-by-piece sum). Against "a write has
  mass" (above) this reads as more mass, not mass from none; Tom's to say which. Known physics has a version of "creates": most of
  an ordinary thing's mass is the energy of its parts' motion and binding, not the parts' own masses.
- *Writes move:* this leaves the static scope set just above. In Newton's account it costs nothing: each moment is still a static
  overlay, and each write moves as the sum of the others' maps directs, carrying its own map with it (the N-body problem; the
  record of where each has been is the history, R1050). What Newton leaves out is the delay: a moved write's map is updated
  elsewhere only at light's speed, and the update carries energy (the open point).

Tom (24 Nov): "We need to make some simplifying assumptions about the write". Proposed by Claude, awaiting Tom; none adopted:
1. A write is a point: a place and nothing else, no shape of its own.
2. Every write is alike, one unit. Then the mass at a place is the count of writes there (a count laid over writes, R896), which
   squares "a write has mass" with "lots of writes in the same location creates mass".
3. One moment at a time: each moment a static overlay; motion is a sequence of them, no delay.
4. Pulls add (Newton, weak fields), in flat space of three dimensions.
5. Only writes are sources: what arrives (light) is left out.
6. Writes are neither made nor unmade within a run; "writing" places or moves one. (Known physics conserves mass-energy, so a
   write from nothing would need saying where its energy came from.)
What these give up: shape (the border, near and far about it, returns only for a cluster of writes), delay and waves, strong
fields, and light's own pull.
