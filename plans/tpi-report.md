# What marks the situated reader: 2/π, and the sweep over a horizon

*A report, 15 October 2026. Tom, about 04:32: "wrie. a report. Maybe a sweep is the better clue, there needs to b a
horizon and a sweep over it.." (SPN R255). It gathers what TPI found (`plans/tpi-plan.md`, runs 1–4) with the readings
after it (SPN R251–R254), and takes up the suggestion. Each finding is marked: **exact** (computed to the digits),
**classified** (by a fresh agent told nothing of the hypothesis), **reading** (Claude's, unruled) or **open** (Tom's to
rule).*

## In brief

- **The question.** Tom asked what reverse proofs there are of the situated reader: places where known results,
  worked backwards, show its marks. His conjecture: wherever 2/π shows up, the situation is situated.
- **What was found.** 65 occurrences of 2/π across about forty fields. Every constant that could be traced was
  computed from the step of its derivation where π enters, and matched. 55 come from a turn taken evenly and read as a
  shadow or a share. Seven come from the circle held as a shape, one from a pole, and two were not traced. 2/π is a
  strong fingerprint of the even turn.
- **What it does not show.** 2/π by itself does not pick out the situated reader: the circle held whole gives it too.
  Tom's further marks (V not known, a sweep actually made) sort the derivations but not the uses. Only two of the 65
  carry all three marks, the averaging AC meter and the relay's describing function. Both are the inner reading of
  OFS §3.4 built as an instrument.
- **Arc to chord (R254).** 2/π turns an arc into its chord. This says what the constant is. It covers the shape group
  as well, so it does not say who reads it.
- **The suggestion.** The sweep over a horizon may be the better clue. OFS already states its core: any sweep that
  treats the two parties alike puts its median at the corner and, if it reaches the horizon, has no mean (Theorem
  6(e)). 2/π is that sweep's measure only on one path, the circle. The sweep's own fingerprint, a median at the corner
  with no mean, appears on every path. It is classical in the lighthouse, a resonance's line shape, the ground seen
  from a height, and an inverted noisy parallax. A test on that side is proposed below. It has not been run.
- **The lighthouse, closely** (§7). The Cauchy is the shore offset over the lamp's distance, (x − α)/β = tan θ. The
  scale is removed in two places: within each flash, where the path length cancels from the ratio of the two legs
  (OFS Theorem 6(a)); and at the corner, where the shore readers find β as half the interquartile range. Averaging
  never removes it, since the mean of N flashes has exactly the law of one.

## 1. The question and the conjecture

On 14 October Tom asked: "what good reverse proofs do we have of the situated observer?" The strongest answers in the
corpus are these:
- parallax worked back from what astronomy already knows (`parallax.md` §6);
- the Cauchy worked back to the drawing V = H (OFS Proposition 5(d));
- the marginalization paradox, resolved only by the scale's own measure (OFS §11.2, question 7);
- von Mises's water and wine, where every fair answer puts the corner at ½ (OFS §11.2, question 2).

Tom then proposed a wider clue: "Possibly anytime 2/PI shows up, its the situated situation." He added that it is
"probably the best clue there is", and that there are many more examples.

## 2. What 2/π is in the geometry

OFS §3.4 has two vantages on one turn:
- **The outer reading.** The outer hemisphere's facing turns a half turn. Its arc of π/2 stands on the line of 1 as its
  chord, so it reads π/2.
- **The inner reading.** The inner bar turns a quarter turn, and its shadow is averaged over the turn:
  (2/π)∫₀^{π/2} cos θ dθ = 2/π. At any turn θ the inner reading is sin θ/θ, which is 0.9003 at the corner and 2/π at the
  horizon.
- **Together.** The product of the two readings is 1: together they return the line. Their difference does not.

TPI fixed four forms before searching:
- (i) the mean shadow;
- (ii) the share of a quarter turn, (2/π)θ;
- (iii) sin θ/θ at the quarter turn;
- (iv) the normaliser of a weighted half turn whose integral is π/2.

A hidden turn counted where one sits in the derivation. That means an angle made even by two equal-spread normal amounts,
a phase uniform in time, or a rotation group's Haar measure.

## 3. What was done

| run | asked | outcome |
|---|---|---|
| 1 | The twenty occurrences known beforehand, computed exactly. | Three quadrature set-up errors of mine. Corrected in run 2; run 1 recorded. |
| 2 | All 65, by derivation: is each 2/π an even turn read as something never negative? | 63 checks of 62 constants, all match (**exact**). Routes: 43 explicit turn, 12 hidden turn, 7 shape, 1 pole, 2 not traced. P1–P3 killed, P4 not. |
| 3 | Blind: where π enters (an angle, a bounded region, other); is the formula used to infer what is not known? | The routes agree on 51 of 63 rows; six of the disagreements were my question's fault. The seven shape entries all fix their extent in advance (V known). Use does not follow route: 13 of 51 turn formulas infer, against 4 of 7 shape formulas (**classified**). |
| 4 | Blind: is the angle traversed in order, held at once, or not traversed? | 11 in order, 24 at once, 30 not traversed. No shape entry and no identity has a sweep. Only the AC meter and the relay's describing function carry all three marks (**classified**). |

**The catalogue.** It was gathered by a fresh agent given only the task: find occurrences, with formula, field,
source and the derivation step. It was not shown the predictions. It found 45 occurrences beyond the twenty I knew;
37 of them were seen in their sources.

**The classifier.** A second fresh agent answered runs 3 and 4 from a neutral list (name, field, formula and source
only). It was told nothing of turns or of the situated reader. Its answers, with a line of justification each, are in
`plans/tpi/classification.md` and `classification-q3.md`. The appendix gathers every occurrence with its three marks.

## 4. What the runs show

### A strong clue for the even turn (exact)
55 of 65 come from a turn taken evenly and read as a shadow or a share: the inner reading. Where 2/π arises otherwise,
the circle is held as a shape:
- a semicircle's area (Hertz's line contact, Wigner's semicircle, a fault's slip, a rotating star's line profile);
- the arcsine integral (a disc's capacitance, Sneddon's cone, the Oliver–Pharr constant).

Or the quarter turn is a place: the pole of sec + tan behind alternating permutations. Three more were not in the
four forms:
- **Kosterlitz–Thouless:** its 2 is the plane's dimension.
- **The Gaussian beam:** its 2 is the 1/e² radius convention.
- **The shape group:** it fits form (iv) only after a substitution its derivations do not make.

### Concentration moves it off (exact)
Where the parties enter undivided, a turn concentrated by a von Mises law moves the mean shadow off 2/π. At
concentrations ½, 1 and 2 it becomes 0.649, 0.682 and 0.763. Drawing the parties unequally moves the median off the
corner. The evenness is what gives the value.

### The dimension rule holds only for shadows on an axis (exact)
In the plane three constructions coincide at 2/π:
- the mean shadow of a direction on an axis;
- the mean |sin| of the angle between two directions;
- the mean half-angle chord.

In space they part: ½ (Archimedes' hat-box), π/4 and 2/3. OFS's family, the reciprocal of
√π·Γ((n + 1)/2)/Γ(n/2), belongs to the first only.

### Not by itself a clue for the situated reader (reading)
In the corpus, the turn taken is the situated reader's (R233). The circle held whole is the completed view's, drawn on
the chord after the arc (R234). The shape group is 2/π with no one turning.

### The marks sort derivations, not uses (classified)
In derivation, every shape entry has V known (its extent fixed by both ends) and no sweep. Every identity has no sweep.
In use, either kind serves a reader that lacks the whole:
- The shape formulas infer by fitting a known profile to data.
- Thirteen turn formulas read a whole they do not have through a shadow or a sign. Examples: an averaging meter's peak,
  a correlation from sign agreements (Van Vleck) or rank agreements (Kendall), a length from crossings (Buffon), a
  refractive index from absorption (Kramers–Kronig), leaf area from light extinction.

### Where all three marks meet (classified)
Two entries carry all three: the averaging AC meter (K5) and the relay's describing function (C34).
- **The meter.** A phase advances evenly in time. The meter reads the mean of its shadow and infers a peak it does
  not have: the mean is 2/π of the peak.
- **The relay.** Its describing function reads the fundamental of a switched output as the phase sweeps, and infers
  the amplitude.

Both are the inner vantage made into an instrument. Eight more would join if a population held at once counted as a
sweep, ten in all. That would be the parallel reader's way of meeting the directions (situation 3), as traversal in
order is the serial reader's (situation 4). This is **open**.

### A bias in the catalogue
It was gathered by searching for formulas, which favours equations:
- 30 of 65 traverse nothing. Twenty of them are turn formulas whose angle lives only in the derivation; the other ten
  are the shape group, the pole and the two untraced.
- 24 are populations held at once.
- 11 are traversed in order.

A catalogue of instruments and perceivers might weigh differently. *(This corrects the run 4 reading as first written
and SPN R253, which gave 13, 24 and 30 as if separate. The 13 are the turn formulas that compute from known sizes,
among the 30.)*

## 5. The arc and the chord (R254)

Tom: "2/PI is needed to turn the arc into the chord, you want remove the curve and ge the straight line for some
reason." This is OFS §3.4 read the other way. The semicircle on the line of 1 has an arc of π/2, so the line over the
arc is 2/π. The inner bar's quarter turn has an arc of π/2 over a shadow of 1.

The reading covers the four forms (**exact**, classical):
- **The mean shadow** averages each angle's straight shadow.
- **The share (2/π)θ** unrolls the arc onto [0, 1].
- **sin θ/θ** is chord over arc. Viète's product is that ratio reached by halving the arc: each level lengthens the
  inscribed polygon by 1/cos(π/2^(n+2)). The first step is cos 45°, where the two chords meet at the corner, and plain
  halvings follow.
- **The normaliser** is the arc's length.

It also covers the shape group. A semicircle's area is half its radius times its arc (Archimedes), so a profile
flattened to its rectangle of equal area is arc over chord again:
- Hertz's and Wigner's peak over mean is 4/π.
- A disc's capacitance is 2/π of a sphere's.
- The square wave is the sine with its curve removed: its fundamental is 4/π.

Left over are the Kosterlitz–Thouless jump, the Gaussian beam and, as a stretch, the pole. The pole is
tan(45° + x/2) running from the corner to the horizon, laid out as a straight radius.

So arc to chord says what the 2/π is, whether the arc is swept or held whole. The marks say whether a reader was
situated. Tom left the purpose open ("for some reason"). Claude's candidate is to take a mean: the readings on the arc
have none, and their shadows on the line do (**reading**).

## 6. The suggestion: a sweep over a horizon

### 6.1 The two words in the corpus
- **The sweep** runs from home (0°: all of H, none of V), through the corner (45°, h = v), to the horizon.
- **The horizon** is at 90°: all of V, none of H. There the reading v/h runs off. The turn to the horizon is finite, a
  quarter turn; the reading is not. The walk's steps bunch toward it without reaching it (`walk.html`). The ground runs
  into it seen from the air (`flight.html`).
- **OFS already states the clue in this form**, in its abstract and Theorem 6(e): any sweep that treats the two parties
  alike puts its median at the corner and, if it reaches the horizon, has no mean. The even turn adds only the Cauchy's
  exact shape.

### 6.2 Why the sweep may be the better clue (reading, on exact facts)
1. **2/π belongs to one path.** Sweep three paths evenly along their own lengths from home to the horizon: the circle,
   the line h + v = 1 and the square's edges (`paths.html`; OFS §11.2, question 2).
   - All three agree at home, the corner and the horizon.
   - All put the median at the corner, and none has a mean.
   - Only the circle's share, 2θ/π, carries π. At 22.5° the three shares are 0.250, 0.293 and 0.207.

   So 2/π marks the turn, one way of sweeping. The sweep over a horizon is what all three share.
2. **2/π needs the horizon.**
   - sin θ/θ is 2/π only when the turn reaches the horizon; at the corner it is 0.9003.
   - The share (2/π)θ measures the turn in units of the turn to the horizon.
   - A weight that vanishes at the horizon, sin² 2θ, has a mean (4/π).

   Every 2/π in the catalogue has the horizon built in, as the end of its quarter turn. That is why the horizon could
   not sort the catalogue: there it is never absent.
3. **The horizon is where the reader's own division meets its limit.** Dividing by the sum never meets a horizon: the
   chord h + v = 1 is the unsituated view, and v/(h + v) stays in [0, 1] and has a mean. The reading v/h divides by the
   reader's own unit relation, and meets the horizon where that relation vanishes. So a sweep over a horizon carries two
   of the situated reader's acts at once: a standpoint that turns, and a division by its own party.

### 6.3 Its fingerprint: two faces
- **The bounded face** is the sweep's share or shadow. On the circle it is 2/π and π/2, which is what TPI catalogued.
  On the line it is s/(1 + s), with no π.
- **The unbounded face** is the reading laid on a line: the median at the corner and no mean. Where the sweep is an
  even turn, it is the Cauchy.

Classical places where the unbounded face appears. Each is checked here where a number is given (**exact**); none is
new:
- **The lighthouse** (Gull 1988; Sivia and Skilling 2006). A lamp turning evenly lands its flashes on a straight shore
  as a Cauchy. The lamp is found from the median or the likelihood, never the mean.
- **A resonance.** As the energy crosses the whole line, the scattering phase δ sweeps from 0 to π. The extra states
  per unit energy are (1/π)·dδ/dE, the Lorentzian (Beth and Uhlenbeck 1937). Half of them lie within one half-width of
  the resonance: the corner, where the detuning equals the half-width and the phase is 45° from its middle. The mean
  detuning grows with the logarithm of the range and has no limit.
- **The ground from a height.** A point at height y meets each stretch of ground in proportion to the angle it
  subtends: the half-plane's harmonic measure, y/(π(x² + y²)). Brownian motion started there hits the ground with the
  same law (Kakutani 1944). Half the ground on one side lies within y of the foot, at 45°: the corner. This is
  `flight.html`'s geometry.
- **A noisy parallax inverted** (`parallax.md` §6; Bailer-Jones 2015). As the parallax approaches zero the distance
  runs to the horizon. The inverse has no mean and keeps its median.

### 6.4 Whose sweep
OFS separates two cases (§7.8). When the evenness belongs to the reader's own sweeping, the law is the reader's
addresses. When it belongs to the sources, as with the lighthouse's lamp, it is a fact about the world.
- **The lamp's:** the lighthouse.
- **The system's phase:** the resonance.
- **The reader's own, plainly:** the gaze from a height swept from the foot to the horizon.
- **Hard to place:** the averaging meter's phase is the source's, but the meter's sampling is even in time.

A clue for the situated reader would need the sweep to be the reader's own. That is a fourth question beside run 4's
three marks.

### 6.5 A test, proposed and not run
Gather the unbounded face as TPI gathered the bounded one. A fresh agent would collect occurrences of the Cauchy and its
kin (the Lorentzian and Breit–Wigner shapes, the Poisson kernel of a half-plane, ratios with the median at 1 and no
mean), each with its derivation step. The blind classifier would then answer, for each:
- whether an angle or phase is taken evenly, or a line swept evenly, to where one party vanishes (a sweep reaching a
  horizon);
- whether it is traversed in order or held at once;
- whose evenness it is: the observer's or instrument's, the source's, or a population's.

Predictions would be written in a plan before the search. A kill can already be named as likely: the Cauchy reached as
the stable limit of summed heavy-tailed amounts. That gives a median at the corner and no mean, from a reciprocal that
reaches its horizon, with no turn. It would bound the clue to the sweep, not the turn, which is Tom's suggestion.

### 6.6 What it would and would not show
If every occurrence of the unbounded face traces to a sweep reaching a horizon, the structure would be shown across
fields, as TPI showed the even turn. It would not show that each system is a reader. That reading is the corpus's
bridge (R233), named and not tested. The fourth question would show how often the sweep is the reader's own. If it is
rare in the textbooks, as the sweep was in run 4, that would say where the situated reader has been left out.

## 7. The lighthouse, closely

*Tom, about 04:44: "lets look more closely at the lighthouse, more closely that seems to be a common metaphore. where
is the cauchy in the light house, where is the removal of the scale?" (SPN R256). Everything below is classical. The
numbers are checked exactly with α = 3, β = 2. The reading of it in the corpus's terms is Claude's.*

**The set-up** (Gull 1988; Sivia and Skilling 2006):
- A lamp stands a distance β out to sea, opposite the point α on a straight shore.
- It sends flashes at angles θ spread evenly over the half turn toward the shore.
- Detectors along the shore record only where each flash lands, as a position x on the shore's ruler.
- Find the lamp.

### Where the Cauchy is
A flash at θ lands at x = α + β·tan θ. Measure from the foot of the perpendicular and divide by the lamp's distance:
(x − α)/β = tan θ.
- That is the reading v/h of a sweep.
  - **Home** is the foot (θ = 0).
  - **The corners** are at ±45°, landing at α ± β.
  - **The horizons** are the two ends of the shore (θ → ±90°), where a flash runs parallel to the shore and never lands.
- An even θ makes tan θ the standard Cauchy. The shore receives density β/(π(β² + (x − α)²)): a Cauchy centred on the
  foot, with scale the lamp's distance.
- **The corner holds half the flashes.** Half land within β of the foot.
- **The shares are flip-symmetric about the corner.** Counted in doublings of distance from the foot, the shares are
  the same on both sides of it: 0.205, 0.139, 0.077, 0.039, 0.020 outward, and the same inward.

### Where the scale is removed
It is removed in two places. In a third place it is not.
1. **Within each flash: the reach cancels.**
   - A flash travels a distance r = β/cos θ, different for every flash.
   - Its two legs, out to sea and along the shore, are r cos θ and r sin θ. Their ratio is tan θ, and r is gone.
   - At θ = 0.3 the path is 2.094, the legs 2.000 and 0.619. At θ = 1.2 the path is 5.519, the legs 2.000 and 5.144.
     The ratio is tan θ both times.

   This is OFS Theorem 6(a) exactly. Its reach ℓ is the flash's path, and its components ℓ·h and ℓ·v are the two
   legs.
2. **Across flashes: one scale is left, and it is the lamp's H.**
   - The out-to-sea leg is β for every flash, because the shore is straight. The straight shore holds h at all of β, so
     every landing is the reading times β.
   - Divide by β and the law is scale-free.
   - The straightness is what makes the Cauchy. Curve the shore into a circle round the lamp and the flashes land
     evenly along it, with no Cauchy.

   So the Cauchy is what an even turn looks like laid on a straight line: a turn read on a line, the same meeting as
   R254's arc and chord. On this side it gives the Cauchy's law, where on the other it gave 2/π, the mean of the
   shadow.
3. **On the shore it is not removed.**
   - The detectors read x in metres, on an agreed ruler along a known line. That is the unsituated view (R231, R234).
   - They know neither α nor β, so their Cauchy carries the scale.
   - **Summing cannot take it out.** The mean of N flashes has exactly the law of one flash, the same α and the same β:
     the characteristic function e^{iαt − β|t|} is unchanged by averaging. The mean of |x − α| has no limit; out to
     10⁶ from the foot it is 16.7 and still growing with the logarithm.
   - **Order gives it back, at the corner.** The median of the landings is the foot, α. Half land within β of it, so
     half the interquartile range is β. The shore readers recover both numbers from order, and neither from sums: OFS
     Theorem 6(b)–(e), worked on a beach.

### Whose sweep, and why the metaphor is so common
The textbook lighthouse has both views in one picture.
- **The lamp is situated.** It stands somewhere, turns evenly, and needs no distance at all. Its sweep reaches the
  horizon at both ends of the shore, which is why there is no mean. A bay of finite length would have one.
- **The shore is unsituated.** It is a straight line with a ruler, on which the turn is laid.

The Cauchy is the meeting of the two. Because the sweep is the lamp's, the textbook's Cauchy belongs to the world
(OFS §7.8: "There the evenness belongs to the lamp, a fact about the world.").

OFS's own case is the mirror image. Put the reader at the lamp, sweeping, and let it read each landing by its angle.
Its readings are tan θ, with no β anywhere. β enters only when it lays those readings out as distances along the shore:
amount = reading × breadth, the one bridge. If it lays them at a chosen H in place of β, the median of |x − α|/H falls
at β/H, not at 1. It is off by the lamp's true distance in units of its H, the size the geometry never reads.

So the answer to "where is the removal of the scale" is that it happens in two places:
- **at the lamp**, in the ratio of a flash's two legs, which carry the same path length;
- **at the corner**, where the shore readers find the β they lack.

The mean never removes it.

### V = H on the beach
*Tom, about 04:49: "can we show that V = H in the ligiht house metaphore?" (SPN R257). The numbers are exact. The
reading in the corpus's terms is Claude's.*

Yes. The lighthouse shows V = H in three ways, and it also shows what V = H is not.

1. **Physics has drawn it for the lamp.**
   - The lamp turns rigidly in a plane where a metre out to sea is a metre along the shore.
   - A flash's two legs are β (h, all of H) and x − α (v). Its direction (cos θ, sin θ) lies on one unit circle, and
     the shore is met at the reach β/cos θ.
   - This is OFS Proposition 3(e): a rigid turn carries all of h into all of v only if both are drawn at one length.

   In the lighthouse, the isotropy of space draws V = H. The situated reader has to draw it for itself.
2. **The beach can test it: OFS Proposition 5(d) on the shore.**
   - Read the landings on a shore ruler whose unit is c sea units. Read the lamp's distance on the sea's ruler. Form
     R = (offset from the foot) / (lamp's distance).
   - The lamp's even turn gives P(R ≤ r) = (2/π)·arctan(c·r), with median 1/c.
   - **At c = 1**, half the landings lie within one lamp-distance of the foot. The law is unchanged by the flip
     R ↦ 1/R: the near half is the mirror of the far half.
   - **At c = 2**, 70.5% lie within "one lamp-distance", the median is ½, and the flip fails (by 0.25 at r = 0.3).

   The law sits at the corner, and is unchanged by the flip, exactly when c = 1. V = H is the condition for the 45°
   flash to be the corner. Testing it needs one outside amount, the lamp's distance read out to sea. The landings alone
   cannot test it, because a Cauchy read on any ruler is still a Cauchy.
3. **Charts show c ≠ 1.** A plate carrée chart, with latitude and longitude drawn at one scale, draws east–west
   lengths at sec(latitude) times their ground length. Take a shore running east–west and a lamp due north of it.

   | latitude | stretch | true 45° flash drawn at | landings within one drawn lamp-distance |
   |---|---|---|---|
   | 30°N | 1.155 | 49.1° | 45.4% |
   | 60°N | 2 | 63.4° | 29.5% |

   At 60°N the flip fails too. Mercator's chart stretches north–south by the same sec(latitude) (dy/dφ = sec φ, 2.000
   at 60°N), so locally c = 1. It keeps V = H at every point, which is why angles read on it are true (it is
   conformal), and there the 45° flash is drawn at 45°. OFS §6 already uses Mercator's map, for the two address spaces.
4. **What it does not show: the true size.** The lighthouse keeps apart the two numbers OFS keeps apart.
   - **c is the drawing**, V = cH. It must be 1. With c ≠ 1 the figure is stretched: its angles change and the corner
     leaves 45°.
   - **κ = β/H is the true size**, and it is free.
     - **The lamp's reader.** It reads by angle, so it has tan θ and no β. Choosing an H, it lays the shore at
       H·tan θ. That is off from the truth by β/H in both directions alike: a similar figure, every angle kept, the
       45° flash still the corner. This is a zoom, fixed by one outside amount (the lamp's distance in metres).
     - **The shore readers.** With no sea ruler, they take β from the corner (half the interquartile range). This is
       OFS Proposition 13's estimate at the median: the lamp drawn as far out as the half-way landing is along.

So the lighthouse shows V = H as the condition for its corner, and shows it apart from H. The lamp may be drawn at any
distance (a zoom), but not at different lengths along and across (a stretch).

## 8. Open for Tom

1. **Does a population held at once count as a sweep?** It is the parallel reader's way. With it, ten of the 65
   carry all three marks rather than two.
2. **Which horizon?** It may be the end of the turn, where the reader's own party vanishes (the corpus's use). It may be
   the line the sweep falls on (the shore, the ground). Or it may be the azimuth, a sweep along the horizon. The first
   two lead to the same unbounded face.
3. **Must the sweep be the reader's own** (OFS's addresses), or does a source's sweep, like the lighthouse's, count?
4. **Should the horizon test (§6.5) be run?** Predictions first.

## Sources

**In the corpus:**
- `plans/tpi-plan.md`: runs 1–4, with the predictions as written and the outputs;
- `plans/tpi/catalogue.md` and `plans/tpi/tpi.py`: the catalogue and the exact checks;
- `plans/tpi/classification.md` and `classification-q3.md`: the blind answers;
- `plans/tpi/run3.py` and `run4.py`: the scoring;
- OFS §3.4, Theorem 6 and §7.8, §11.2 questions 2 and 7;
- `paths.html`, `walk.html`, `flight.html`, `parallax.md` §6;
- SPN R233, R234, R251–R255.

**Classical:**
- Archimedes, *On the Sphere and Cylinder*;
- Viète (1593);
- Buffon (1777);
- Beth, E. and Uhlenbeck, G. E. (1937), *Physica* 4, 915;
- Kakutani, S. (1944), *Proc. Imp. Acad. Tokyo* 20, 706;
- Gull (1988) and Sivia and Skilling (2006), as cited in OFS;
- Bailer-Jones, C. A. L. (2015), *PASP* 127, 994.

## Appendix: the 65 occurrences and their marks

The columns:
- **route:** run 2's judgment of where the 2/π comes from;
- **use:** run 3's blind answer;
- **sweep:** run 4's blind answer (traversed in order, held at once, or none).

The constants are checked in `plans/tpi/tpi.py`. Formulas and sources are in `plans/tpi/neutral-list.md` and
`catalogue.md`.

| ID | occurrence | field | route | use | sweep |
|---|---|---|---|---|---|
| K1 | Half-Cauchy distribution function | Probability | turn | computes | none |
| K2 | Buffon's needle | Geometric probability | turn | both | at once |
| K3 | Viète's formula | Analysis | turn | identity | none |
| K4 | Arcsine law (Jeffreys's prior; Lévy) | Probability / statistics | hidden turn | both | none |
| K5 | Average of a full-wave rectified sine (averaging AC meters) | Electrical measurement | turn | infers | in order |
| K6 | Square pixel (100% fill) MTF at the Nyquist frequency | Imaging | turn | computes | at once |
| K7 | Van Vleck relation for one-bit (sign) correlators | Radio astronomy / signal processing | hidden turn | infers | at once |
| K8 | Kosterlitz–Thouless universal jump of the superfluid stiffness | Condensed matter | turn | infers | at once |
| K9 | Efficiency of the median against the mean, and the sign test against the t test, under a normal law | Statistics | hidden turn | computes | none |
| K10 | Squared mean absolute value of a standard normal; one-bit quantiser loss | Statistics / communications | hidden turn | both | none |
| K11 | Effective length of a half-wave dipole | Antennas | turn | both | at once |
| K12 | Mean speed of a point on the rim of a rolling wheel | Mechanics | turn | computes | in order |
| K13 | Particle flux through a line segment in a 2D ideal gas | Kinetic theory | turn | computes | at once |
| K14 | Jordan's inequality | Analysis | turn | identity | none |
| K15 | Flamant's solution: line load on an elastic half-plane | Elasticity | turn | computes | at once |
| K16 | Hertz line contact (cylinders) | Contact mechanics | shape | computes | none |
| K17 | Wigner's semicircle law | Random matrices | shape | computes | none |
| K18 | Sato–Tate distribution | Number theory | hidden turn | computes | at once |
| K19 | Equilibrium measure of an interval (a charged strip; Chebyshev nodes) | Potential theory / approximation | turn | computes | none |
| K20 | Goemans–Williamson max-cut approximation ratio | Algorithms | hidden turn | computes | at once |
| C1 | Wallis product | Analysis | turn | identity | none |
| C2 | Bauer–Ramanujan series | Series / number theory | not traced | identity | none |
| C3 | Square-wave Fourier series | Fourier analysis | turn | computes | in order |
| C4 | Wilbraham–Gibbs overshoot | Fourier analysis | turn | computes | in order |
| C5 | Fourier sine/cosine transforms | Analysis | turn | computes | none |
| C6 | Lebesgue constant, Chebyshev nodes | Approximation theory | turn | computes | none |
| C7 | Kac's real roots | Probability | hidden turn | computes | none |
| C8 | Alternating permutations | Combinatorics | pole | computes | none |
| C9 | Complete elliptic K and the AGM | Special functions | turn | identity | none |
| C10 | Struve H₁ at large argument | Special functions | hidden turn | computes | none |
| C11 | Nesterov's π/2 theorem | Optimisation / algorithms | hidden turn | computes | at once |
| C12 | Krivine's bound / cut norm | Functional analysis / algorithms | hidden turn | computes | at once |
| C13 | Kendall's τ (Greiner) | Statistics | hidden turn | infers | at once |
| C14 | Centroid of a semicircular arc | Statics / geometry | turn | computes | none |
| C15 | Mean chord between random points on a circle | Geometric probability | turn | computes | at once |
| C16 | Pendulum period | Classical mechanics | turn | computes | in order |
| C17 | 2D Ising internal energy | Statistical mechanics | turn | computes | none |
| C18 | Infinite resistor grid, diagonal | Electrical networks | turn | computes | none |
| C19 | Excluded area of random sticks | Percolation / condensed matter | turn | computes | at once |
| C20 | Stoner–Wohlfarth, in-plane random axes | Magnetism | turn | infers | at once |
| C21 | Bell's linear local model | Quantum foundations | turn | computes | at once |
| C22 | Kramers–Kronig, one-sided | Optics / EM / condensed matter | turn | infers | none |
| C23 | Gaussian beam peak intensity | Laser optics | turn | computes | none |
| C24 | Binary phase grating | Diffractive optics | turn | computes | at once |
| C25 | Capacitance of a thin disc | Electrostatics | shape | computes | none |
| C26 | Microstrip synthesis (Wheeler) | Microwave engineering | not traced | computes | none |
| C27 | Baffled piston reactance | Acoustics | hidden turn | computes | none |
| C28 | Penny-shaped crack | Fracture mechanics | turn | computes | none |
| C29 | Sneddon's conical indenter | Contact mechanics | shape | infers | none |
| C30 | Oliver–Pharr ε for a cone | Nanoindentation | shape | infers | none |
| C31 | Uniformly loaded circle on a half-space | Elasticity / geotechnics | turn | computes | at once |
| C32 | Earthquake stress drop, long fault | Seismology | shape | infers | none |
| C33 | Fibre orientation factor, 2D random | Civil engineering (fibre-reinforced concrete) | turn | computes | at once |
| C34 | Ideal relay describing function | Control | turn | both | in order |
| C35 | Saturation describing function | Control | turn | computes | in order |
| C36 | Six-step inverter | Power electronics | turn | computes | in order |
| C37 | Single-balanced switching mixer | RF / communications | turn | computes | in order |
| C38 | Class-B output stage | Analog electronics | turn | computes | in order |
| C39 | Air-gap MMF of a full-pitch coil | Electric machines | turn | computes | at once |
| C40 | Square- vs sine-wave grating threshold | Perception / psychophysics | turn | computes | at once |
| C41 | Coltman's square-wave/sine-wave relation | Imaging | turn | infers | at once |
| C42 | Canopy G-function, vertical leaves | Plant ecology | turn | both | at once |
| C43 | Ideal-gas model of animal encounter | Animal ecology | turn | computes | at once |
| C44 | Rotational broadening kernel (ε = 0) | Astrophysics | shape | infers | none |
| C45 | Fabry–Pérot Airy linewidth | Optics / interferometry | turn | computes | in order |
