# Where it shows up

*The seventh of a series of essays on what can be known from where one stands. Draft, 28 October 2026.*

The first six essays built the geometry from the inside out. A reader holds one length, H, and turns it. The turn gives the
circle, the readings are the Cauchy, and the corner sits at their median. Ratios are free and amounts cost something
carried in.

This essay goes the other way. It looks at places where people met the geometry long before anyone named it: a lamp on a
cliff, a navigator's chart, a statistician dividing by a standard deviation, a graph drawn with equal axes, a camera with
square pixels, a sky seen from a moving ship. Each field found the same thing for its own reasons. Seen together, they
show one requirement and one freedom. The requirement is that whatever is drawn with two axes must be drawn with both at
one length, or the turn is lost. The freedom is the size, which every one of them leaves to be fixed some other way.

The third essay already took three cases from data: LIGO's two detectors, the quasar dipole, and photons arriving one at
a time. Those sorted the address from the payload. The cases here are older and more familiar, and they sort something
else: what the reader's circle looks like once it is drawn on a page, a shore or a chart, where a second axis exists and
can be stretched.

---

## 1. The lighthouse

A lamp stands on a rock at distance β out from a straight shore, opposite the shore's point α. It turns steadily and
sends flashes at random moments, so the angles θ of the flashes, measured from the perpendicular to the shore, are spread
uniformly over the half turn that faces land. Someone walks the beach and marks where each flash lands. From the marks
alone, where is the lamp?

This is the lighthouse problem of the Bayesian textbooks (Gull 1988; Sivia and Skilling 2006). It is used to teach that
the average of the marks is useless. The marks never settle toward a mean however many are collected, and the right
estimate of α is their median. Every essay so far has said why. A flash at angle θ lands at

  x = α + β·tan θ,

so the mark's offset from the foot, over the lamp's distance, is

  (x − α)/β = tan θ.

That is the reading of the second essay, v/h, with the sea as h and the shore as v. The landings carry the Cauchy because
the lamp's turn is uniform. Nothing about the shore, the sand or the light makes them so. Read on this line:
- **Zero** is the foot of the perpendicular, the flash straight at the shore.
- **The corners** are the flashes at ±45°, which land at α ± β, one lamp-distance either side of the foot.
- **The horizons** are the shore's two ends, which the flashes approach and never reach.

Half the landings fall within β of the foot, since half the turn lies within 45° of the perpendicular. That is the corner
as a median, the same half that every essay has found. It is also how the walker finds the lamp: α is the marks' median,
and β is half the spread of their middle half, the distance from the foot to either corner. The walker measures both in
paces along the sand. The paces are amounts, carried in by walking; the lamp's turn gives the rest.

**Where the path goes.** Each flash travels β/cos θ to reach the shore, a different length for every flash. That length
cancels. The landing depends only on the ratio of the flash's two legs, β out to sea and x − α along the shore, and one
length remains, β. It is the same for every flash because the shore is straight. So the lighthouse is one length turned,
the lamp's distance playing H.

**Drawing it with the shore stretched.** Now draw the picture on paper and make a mistake: draw the shore at c times the
scale of the sea. Write it as V = cH, the sea drawn at H and the shore at cH.
- The half-way flash, the true 45° one, now lands c drawn lamp-distances from the foot, and on the drawing it leaves the
  lamp at arctan c instead of 45°.
- The share of landings within one drawn lamp-distance of the foot is (2/π)·arctan(1/c), no longer a half.
- The drawn readings are a Cauchy of scale c, with median c. The reciprocal carries that to scale 1/c, so the near half of
  the drawing no longer mirrors the far half.

All three return to what they should be if and only if c = 1. The drawing with the shore and the sea at one length is the
only one in which the turn is still a turn: the median flash at 45°, half the landings within one lamp-distance, the near
side the mirror of the far.

**Drawing it at the wrong size.** Now make a different mistake: draw the picture at c = 1 but with the wrong lamp
distance, any H in place of β. Each landing is laid H·tan θ from the foot. Every angle is kept, and the 45° flash is still
the corner. Every length is off by β/H, along the shore and out to sea alike. That is not a distortion, it is a similar
figure. The picture is right in every way a reading can check and wrong only in its scale, which no reading fixes.

The two mistakes are different in kind. A stretch, c ≠ 1, breaks the turn and moves the median off the corner. A wrong
size, H ≠ β, breaks nothing that can be read. The first is a stretch, the second a zoom.

**Standing at the lamp.** A reader standing at the lamp, reading each flash by its direction, holds tan θ itself. It has
no β at all and no second length. Its one length gives the turn, so the requirement that c = 1 is met before it can
arise. The requirement only appears once someone draws the scene with two axes, a sea axis and a shore axis, and then has
to choose how long to make each. The uniformity in this picture is the lamp's, a fact about the world. Find the turn,
find the amount: here the lamp turns and the flash is the amount, and the beach records only where each flash landed.

---

## 2. Mercator's chart

The second familiar picture is a map. On a globe of radius 1, draw a chart whose parallels of latitude are horizontal
lines all of one length, with the longitude λ across, and put latitude φ at some height y = f(φ). The navigator wants one
thing from it: a course held at one compass bearing should be a straight line on the chart, at its true bearing.

Work out what the chart does to a small step.
- A step dφ north is dφ long on the globe and f′(φ)·dφ on the chart. So the chart draws north at f′(φ) times true.
- A step dλ east is cos φ·dλ long on the globe, since the circle of latitude shrinks toward the pole, and dλ on the chart.
  So the chart draws east at sec φ times true.

Call the ratio of the two scales c = f′(φ)·cos φ. At that place, the chart draws north at c times the scale of east:
V = cH, with H the step east.

A course of constant bearing ψ moves east and north in the ratio tan ψ, so cos φ·dλ = tan ψ·dφ on the globe. On the chart
its slope is dx/dy = dλ/(f′(φ)·dφ) = tan ψ/c. So the course is drawn at a bearing ψ′ with

  tan ψ′ = tan ψ/c.

Every bearing is drawn true, and the course northeast, the corner between north and east, is drawn at 45° at every
latitude, if and only if c = 1 everywhere. That means f′(φ) = sec φ, and integrating from the equator,

  y = ln tan(π/4 + φ/2) = asinh(tan φ).

That is Mercator's chart of 1569. Where c = 1 at every latitude, the slope tan ψ is the same all along the course, so the
course is a straight line. That is why navigators have laid compass courses on it for four and a half centuries.

**The small circle.** A circle of small radius δ on the globe, its points δ·(cos t, sin t) north and east, is drawn as
δ·(f′(φ)·cos t, sec φ·sin t): an ellipse whose axes stand in the ratio c. Cartographers call it Tissot's indicatrix
(Tissot 1881), and they use it to see at a glance what any chart does at each place. In the language of these essays, it
is the reader's one length traced in two units. It is a circle exactly where the chart keeps angles, and among the charts
of this kind, only Mercator's keeps it a circle everywhere.

**Four charts, one course.** In v and h, with v = sin φ (the height above the equator's plane) and h = cos φ (the distance
from the axis), four familiar cylindrical charts compare like this. The last column is the course northeast, drawn at
latitude 60°, where cos φ = ½.

| chart | height y | in v and h | c at latitude φ | the course northeast at 60° |
|---|---|---|---|---|
| plate carrée | φ | arctan(v/h), the turn | cos φ | 63.4° |
| Lambert's equal-area | sin φ | v | cos²φ | 76.0° |
| central cylindrical | tan φ | v/h, the division | sec φ | 26.6° |
| Mercator's | asinh(tan φ) | asinh(v/h) | 1 | 45° |

The plate carrée, latitude drawn straight as height, looks the most innocent, but at 60° it draws north at half the
scale of east, so the northeast course leans toward east and is drawn at arctan 2 from north. Lambert's equal-area chart
draws north at a quarter of east's scale there, and the central projection at twice it. Only Mercator's draws the course
at 45°.

The lighthouse and the chart meet. A lighthouse charted on Mercator's map, with its shore running east and west, is drawn
true at every latitude. On a plate carrée at 60°, its half-way flash is drawn at 63.4°.

**What Mercator lets go.** Mercator's chart draws lengths at sec φ in both directions at latitude φ. Its areas are
therefore sec²φ times true. That is a zoom that changes from place to place, growing toward the poles, and it keeps every
angle. It is the same kind of freedom as the lighthouse drawn at the wrong size: the stretch must be 1, the scale may be
anything, and Mercator lets the scale vary from latitude to latitude.

The fourth essay made a further point, which is worth repeating here only briefly. Mercator's chart is not a picture of
what a reader sees. It is a chart of the whole field, every far level drawn alike, with no focus. A reader's turn is
centred on what it looks at, its far field in proportion. Mercator's levels belong to distance laid by a count of places,
not to the picture.

---

## 3. Two charts, and Greenland

Every schoolchild learns the complaint about Mercator's map: it draws Greenland looking comparable to Africa, about
two-thirds its size, when Africa is in fact about fourteen times larger. The complaint is correct, and the essays so far
say what it is a complaint about.

Mercator's chart keeps local angles. A course at constant bearing is a straight line, and a small shape is drawn with its
proportions. That keeps what these essays call the addresses: the relation that matters to a navigator is a direction,
the ratio of a step east to a step north. It does so by the area scale sec²φ, which is a zoom, and areas are amounts. A
country's size is payload.

An equal-area chart, such as Lambert's, keeps the relative areas instead, at the cost of the bearings. Its c is cos²φ, 1
only on the equator. Northeast at 60° is drawn at 76°.

No flat chart keeps both. Keeping angles makes a chart's two scales equal at each place; keeping areas makes their product
1. Both together make every scale 1, a drawing of the sphere on the plane without stretch, which the sphere's curvature
forbids. Euler proved there is no such chart (Euler 1777), and Gauss's theorema egregium says why: curvature is intrinsic,
and a flat sheet has none (Gauss 1828).

So the familiar argument about which projection is "right" is an argument about which property to keep. Mercator kept the
directions and let the sizes go. Lambert kept the sizes and let the directions go. Nothing obliges anyone to use either.
Each chart follows from the property it keeps, and only the globe itself, the complete object, keeps every direction and
every area at once. The globe is the writer's: it holds both hemispheres, every amount, every angle. The charts are two
ways of laying it on a sheet, each keeping one kind of thing.

The complaint about Greenland is a complaint about the zoom, not about the drawing.

---

## 4. Already drawn, under other names

The lighthouse and the chart are the two pictures where c = 1 is easiest to see. It turns up in many more places, under
other names, wherever directions or ratios are read from something with two axes and the answer must not depend on the
units. Each field found it for its own reason.

**Standardizing.** Karl Pearson's correlation coefficient (Pearson 1896) divides each of two variables by its own spread
before comparing them. One variable in kilograms and another in centimetres, plotted raw, are drawn with c equal to
whatever ratio of units happened to be chosen. Divide each by its standard deviation and the two axes are drawn at one
length. A cloud of points that would lie along a line at 45° if the two varied together is then drawn at 45°, whatever
the units. The correlation is unchanged by any change of units in either variable, which is exactly the property a
reading has and an amount lacks.

**Whitening.** Mahalanobis's distance (Mahalanobis 1936), and the map that sends each data point x to Σ^(−1/2)x, go one
step further: they draw every axis at one length and also at right angles, undoing the correlations as well as the
spreads. That is the one measure of length the second essay found a returning turn leaves unchanged, every direction at one
length and forward square to up. Whitening is unique only up to a turn,
and that turn is exactly the part of a reader's ignorance the drawing leaves free.

**Principal components and canonical correlations.** Harold Hotelling's principal components (Hotelling 1933) are taken
from the correlation matrix, the standardized variables, when the variables are in different units. Taken from the raw
covariance matrix, whichever axis happens to be drawn longest takes the first component, a result about the units, not the
data. His canonical correlations (Hotelling 1936) whiten each set of variables before reading the angles between them, and
so are unchanged by every change of units within a set. They are angles, readings, in the full sense.

**Banking to 45°.** William Cleveland and his colleagues studied how people judge slopes on a graph and found that the eye
judges best when the slopes it compares centre on 45°. They chose a graph's aspect ratio to put them there (Cleveland,
McGill and McGill 1988), a practice now called banking to 45°. In these essays' terms, they chose the drawing so that the
middle direction falls on the corner. A line at 45° means "equal" only on equal axes; banking sets the axes so that the
typical slope reads as the corner.

**Square pixels and stereo pairs.** A camera with square pixels draws its two directions at one length. Two cameras of a
stereo pair calibrated alike draw their two standpoints at one length. Both are engineering decisions with long
histories, and both are c = 1 made in hardware.

**Skipped on purpose.** Where the drawing is skipped on purpose, amounts are being read. Variables already in one shared
unit need no standardizing, since the shared unit has already made c = 1. An equal-area map keeps areas, not bearings. A
weighting of features chosen for a task sets c deliberately, because the task cares about the amounts.

None of these fields cites another for the idea. Statisticians standardize to make a coefficient unit-free, cartographers
want straight rhumb lines, graph designers want legible slopes, camera makers want isotropic images. The geometry gives
the common reason. The drawing with both axes at one length is the only two-axis drawing that has the reader's circle,
so it is the only one in which the sweep is a turn and the median of every pair's readings sits on the corner.

---

## 5. Where c ≠ 1 comes from

The cases above invite an objection: "V = H is still a choice. Someone decided to draw both axes at one length, and
could have decided otherwise." The second essay answered it. It is a writer's objection, supposing someone who holds both
axes and sets c; a reader whose sweep is a turn holds one length and has no c to set.

But a c ≠ 1 can still appear in what a reader's readings are taken through, imposed rather than chosen. When it does, it
has a signature, and the cases above sort into four.
- **It is writing, not reading.** Amounts are wanted in a shared unit, so c is the ratio of real units, measured. The
  equal-area map and the task-weighted features are of this kind: they keep amounts on purpose.
- **It is uncalibrated.** Unequal gains, pixels that are not square, variables left in their own units: c is imposed by
  the instrument or the data's units. The median of the readings then sits at c instead of on the corner, and
  standardizing restores it. Whitening, square pixels and calibrated stereo pairs are cures for this case.
- **An estimate has been taken for the circle.** What is known or guessed of the other's true size belongs to the
  amounts, a shift in levels. Redrawing the circle with it runs the estimate together with c. The lighthouse drawn with the
  shore stretched because someone thought the shore "should" look longer is this mistake.
- **It does not turn.** If the measure is not a turn at all, a boost or some other group, there is no circle to stretch.
  It has another geometry, with no corner at its median and other tails. Section 7 meets a boost, and finds that its
  readings still come back to a turn in the right chart.

Each of the four leaves a mark. A median off the corner, at c, says uncalibrated. A median off the corner that moves with
an estimate says the estimate was drawn in. A median that tracks a shared unit says writing. And a law that is not a
Cauchy at all says the measure was never a turn.

---

## 6. Why so many things are Gaussian, and their ratio Cauchy

The textbooks give a second route to the Cauchy, and it shows up even more often than the lighthouse: the ratio of two
independent normal variables, each centred on zero, is Cauchy. Why should the familiar bell curve and the Cauchy be so
close?

Take a payload with two components, X on h's side and Y on v's, both amounts. Its reading is their ratio, |Y|/|X|, which
keeps the direction and drops the size. Two premises are needed, and the geometry does not supply them.
- The payload's law is unchanged by every turn. That the reader cannot detect its own turns is a fact about what the
  reader knows, not about the payload. It makes the turn-invariant law the representation an ignorant reader should
  choose, in Jaynes's sense, and that is all it does.
- The two components vary independently.

Given both, the payload's law is the isotropic normal. It is the only law of two independent components that every turn
leaves unchanged, which John Herschel argued in 1850 for errors in astronomical position and James Clerk Maxwell in 1860 for
the velocities of a gas's molecules (Herschel 1850; Maxwell 1860). Three things follow, each classical.
- **Its direction is uniform over the turn.** So its reading is the half-Cauchy, P(|Y|/|X| ≤ r) = (2/π)·arctan r, with the
  median at the corner. The normal payload's ratio has the addresses' law.
- **Its size is independent of its direction.** The length √(X² + Y²) and the angle separate exactly. What arrives and
  where it is addressed come apart, which is the third essay's main theorem seen from the payload's side.
- **With unequal spreads**, σ_v ≠ σ_h, the reading is still a half-Cauchy, now of scale σ_v/σ_h, its median there. That
  is c = σ_v/σ_h, the uncalibrated case of section 5. Equal spreads are c = 1. With the payload's centre off the origin
  the reading is no longer a Cauchy at all, and its median leaves the corner. With the centre one spread out along v,
  at (0, σ), the median moves to about 1.515.

The two routes to the Cauchy should be kept apart. The address law is the sweep's own: it needs only the uniform turn,
and it holds whatever the payload is, Gaussian or not. The normal payload is a second route that arrives at the same law,
a model consistent with the addresses, not their cause. These essays make no claim that payloads are Gaussian. They say
only that if a payload's law is taken to be unchanged by turns, with independent components, it is the normal, and its
ratio is then the Cauchy the addresses already were.

The mean tells the routes apart. The payload has a mean: each component's size averages √(2/π)·σ. Its ratio, which has
the addresses' law, has none. The part of its mean contributed by readings up to s is (1/π)·ln(1 + s²), growing without
limit as s grows. The
central limit theorem is a third matter again: it makes a sum of many independent contributions normal, and it says
nothing about a single payload's direction.

---

## 7. A moving sky

The last case is the one place in these essays where a whole physical theory is read through the split, and it is read
here because the theory already makes the split in its formulas without naming it.

An observer moving through a field of stars at speed β, a fraction of the speed of light, sees each star change in two
ways, which special relativity writes as two formulas.

**Where the star is seen moves.** This is aberration:

  cos θ′ = (cos θ + β)/(1 + β cos θ),

the same at every frequency. Stars crowd toward the direction of motion. Draw the sky on the stereographic chart, which
lays each direction on the sphere as a point z of the plane (or of the complex numbers). Then aberration is z ↦ z/k, with
k = √((1 + β)/(1 − β)) = e^η, η the rapidity. It is a Möbius map of the celestial sphere, which is how Roger Penrose and
James Terrell, independently in 1959, showed that a moving sphere still looks round and that the Lorentz contraction cannot
be seen in a photograph (Penrose 1959; Terrell 1959).

**What arrives at each place changes.** This is the Doppler factor,

  D = √(1 − β²)/(1 − β cos θ′),

which scales each photon's energy and the rate at which photons arrive.

The first is a map of addresses. The third essay showed that Möbius maps carry the Cauchy's family onto itself, moving
only its point, and here they do.
- A sky uniform in the stars' own frame is seen from the moving frame as the spherical Cauchy, with density
  (1 − β²)/(4π(1 − β cos θ′)²) (Kato and McCullagh 2020). Its parameter is ρ = tanh(η/2). With one dimension fewer it is
  the wrapped Cauchy with the same ρ. On the circle that law is also where a random walk from the standpoint lands, its
  mean ρ; on the sphere those two come apart, and the boosted sky is the Möbius law alone, its mean cosine
  coth η − η/sinh² η (the second essay, section 9).
- That density is D²/4π. The Doppler factor squared is the crowding of addresses toward the motion.
- It keeps the cross ratio of any four stars' places, read as complex numbers in that chart. Three stars seen in both
  frames fix the whole boost and turn, because the Möbius maps of the sphere are the Lorentz group, and a Möbius map is
  fixed by three points (Penrose and Rindler 1984).

The second is a weighting of the payload at each address, and it moves no address.
- An isotropic sky's intensity brightens ahead by D⁴ (Rybicki and Lightman 1979). Of that, D² is the addresses'
  crowding, and D² is the payload: energy and arrival rate, D each. The D⁴ is standard. The split into two squares, one
  for addresses and one for payload, is these essays' reading.

**Reading one's own speed from directions alone.** Lay each direction on the level ξ = −ln tan(θ/2), the quantity
particle physicists call pseudorapidity. On that axis aberration is a shift by η exactly: every star slides the same
distance. A sky uniform in the stars' frame lies as ½·sech²ξ, a bell whose median is the plane square to the motion. Seen
from the moving frame it lies as ½·sech²(ξ′ − η), the same bell with its median moved to η.

So a reader holding directions alone can read its own rapidity, a reading, with no clock, no frequency and no speed of
light carried in. It needs two things of the sky: that every source is counted whatever its brightness, and that the
sources are uniform in their own frame. The third essay's quasar dipole showed what happens when the first fails. A
census cut by brightness adds a weighting of the addresses, D raised to a power read from the census's own counts and
colours. That is still a reading, needing no rest frequency, but no longer of directions alone. And to read the Doppler
factor as a frequency, a shift of a spectral line, needs the line's rest frequency carried in, a known kind of atom: a
writing.

The `boost-sky.html` demo shows the slide. A sky drawn on the level ξ moves bodily by η as the boost grows, and the
directions sampled from it follow the slide with no table rebuilt.

**Three rulers again.** The fourth essay laid one reading x three ways: the writer's number line x, the turn θ = arctan x,
and the hyperbolic angle ζ = asinh x. Special relativity runs on the same three. A velocity's celerity γβ, distance per
unit of the traveller's own time, is x. Its rapidity η is ζ. And with χ the turn ruler's angle, its speed β = tanh η =
sin χ and the Lorentz factor γ = sec χ. Rapidities add along a line, as hyperbolic angles do. Uniform acceleration is
uniform in η, not in χ, so its corner, γβ = 1 (β = 1/√2), is where its two regimes hand over, slow to fast, and not a
median of anything.

**What the theory already had.** None of this is new physics, and these essays claim none. The split between addresses
and payload is already in the formulas: aberration on one line, Doppler shift and beaming on another. What the formulas do
not do is name the two as a transformation of addresses and a weighting of payload, and so they do not say why the first
is a Möbius map carrying the Cauchy and the second is not. The identities are exact. The reading is ours.

---

## 8. What it comes to

**Reading and writing.** Every case in this essay leaves the size free and fixes something else exactly. The lighthouse
can be drawn at any lamp distance; Mercator's chart at any scale, varying from place to place; a standardized variable
in any unit, since the unit cancels; a moving sky at any distance, since only directions were used. What each fixes is a
reading. Where a size is needed, each case says where it must come from: the lamp's distance from a survey, the globe's
radius from an arc measured on the ground, a shared unit for amounts, a rest frequency for the Doppler shift. Each is one
amount carried in, and each is a writing.

The first test of the first essay, scale the world, sorts them at once. Scale the lighthouse's world by k and every mark
moves by k while every angle stays. Scale the globe and Mercator's chart is redrawn at a new scale with the same courses.
Rescale a variable and its correlations stand. Move every star k times farther and the moving sky is unchanged.

**The Cauchy.** Each case is the reader's circle drawn on something with two axes, and each requires the two axes at one
length for the circle to survive. The lighthouse's corner, Mercator's 45° northeast, the correlation of standardized
variables, the eye's best judgment of slopes, a sky's median moving by exactly η: in every one, c = 1 is what keeps the
turn a turn and puts the median on the corner. Every field met the requirement for its own reasons. The geometry says why
it is one requirement.

And each separates two kinds of mistake. A stretch breaks the turn and moves the median off the corner. A wrong size breaks
nothing that can be read. Practice has always treated these differently, calibrating the first and measuring the second,
and the geometry says why: the first is in the drawing, the second in the amounts.

Back to the beach. The marks never settle toward a mean because the lamp turns. Half of them fall within one
lamp-distance of the foot because the lamp's turn has a corner. And the walker, pacing the sand, finds where the lamp stands
along the shore at the marks' median and how far out it stands at half their spread. The turn supplies the corner; the
paces supply the only amount.

---

## Sources

- Gull, S. F. (1988). Bayesian inductive inference and maximum entropy. In G. J. Erickson and C. R. Smith (eds),
  *Maximum-Entropy and Bayesian Methods in Science and Engineering*, vol. 1, 53–74. Kluwer, Dordrecht.
- Sivia, D. S. and Skilling, J. (2006). *Data Analysis: A Bayesian Tutorial*, 2nd ed. Oxford University Press.
- Mercator, G. (1569). *Nova et aucta orbis terrae descriptio ad usum navigantium emendate accommodata*. Duisburg.
- Tissot, N. A. (1881). *Mémoire sur la représentation des surfaces et les projections des cartes géographiques*.
  Gauthier-Villars, Paris.
- Euler, L. (1777). De repraesentatione superficiei sphaericae super plano. *Acta Academiae Scientiarum Imperialis
  Petropolitanae* 1777(1), 107–132.
- Gauss, C. F. (1828). *Disquisitiones generales circa superficies curvas*. Göttingen.
- Pearson, K. (1896). Mathematical contributions to the theory of evolution. III. Regression, heredity, and panmixia.
  *Philosophical Transactions of the Royal Society of London, Series A* 187, 253–318.
- Mahalanobis, P. C. (1936). On the generalised distance in statistics. *Proceedings of the National Institute of
  Sciences of India* 2(1), 49–55.
- Hotelling, H. (1933). Analysis of a complex of statistical variables into principal components. *Journal of
  Educational Psychology* 24, 417–441, 498–520.
- Hotelling, H. (1936). Relations between two sets of variates. *Biometrika* 28(3–4), 321–377.
- Cleveland, W. S., McGill, M. E. and McGill, R. (1988). The shape parameter of a two-variable graph. *Journal of the
  American Statistical Association* 83(402), 289–300.
- Herschel, J. F. W. (1850). Quetelet on probabilities. *Edinburgh Review* 92, 1–57.
- Maxwell, J. C. (1860). Illustrations of the dynamical theory of gases. *Philosophical Magazine* 19, 19–32.
- Penrose, R. (1959). The apparent shape of a relativistically moving sphere. *Proceedings of the Cambridge
  Philosophical Society* 55, 137–139.
- Terrell, J. (1959). Invisibility of the Lorentz contraction. *Physical Review* 116(4), 1041–1045.
- Kato, S. and McCullagh, P. (2020). Some properties of a Cauchy family on the sphere derived from the Möbius
  transformations. *Bernoulli* 26(4), 3224–3248.
- Penrose, R. and Rindler, W. (1984). *Spinors and Space-Time*, Vol. 1. Cambridge University Press.
- Rybicki, G. B. and Lightman, A. P. (1979). *Radiative Processes in Astrophysics*. Wiley, New York.

The geometry is set out with proofs in *Observation from Somewhere*: Proposition 5(f) and (g), "Two charts" and "What the
two pictures show" in §7.1; "Already drawn, under other names" and "Where c ≠ 1 comes from" in §5; "Special relativity's
sky" in §11; Appendix A, "V = H under other names" and "Why the payload is Gaussian".
