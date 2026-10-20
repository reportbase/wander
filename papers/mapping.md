# Mapping from addresses

*Started 19 October 2026, at Tom's word: "start a new paper that can fully explore this." A working paper: a reading,
revised as it is worked over, not a ruling. Its question is how a reader maps a room, or any scene, from the inscribed
sweep's addresses, what each stage needs, and how that compares with the methods that already exist. Tom set its stance
(SPN R387):*
- *"seems to me that this might provide an alternative to existing methods."*
- *"the prospect of an alternative method is interesting, even if exiisting methods are better. understanding the
  geometry is useful for its own sake."*

*So the paper does not need the address-first way to win. It needs it to be exact about what it uses, and honest about
where it agrees with established practice and where it parts from it.*

*It gathers what the corpus has on mapping:*
- *OFS §9: "A survey: many readings, one amount", "Closing a loop", "Inside a room", "Far off", "Turning in place",
  "From one place";*
- *the tests: STC, PXC, HTP, MOT, RWT, RSH, CFH, TRI and CIW;*
- *the pages: `room.html`, `room-walk.html` and `room-ratios.html`.*

*The rules are `papers/physics.md` §0: evidence is exact arithmetic or a simulation against a full referee, predictions
come first, keep the case and name the bridge. New tests are planned in `plans/`, with scripts in `runs/<code>/`. A result
goes into OFS only once it has been worked out here or in a plan.*

**Iterations**

- 19 October, first: written from the day's exchange.
  - Tom asked, in turn:
    - "so we can map out a room with ratios with the two inscribed sweeps.";
    - "how do we inject scale to get sizes";
    - "what new does the cauchy approach provide for mapping a room?".
  - Claude's answer to the last: the reconstruction is classical, and what the Cauchy reading adds has close relatives
    in photogrammetry and SLAM (§0).
  - Then the two messages that set the stance above.
- 19 October, evening (SPN R388).
  - Tom: "lidar sends out a pulse correct or lasers. cauchy is more passive, it rececives the signal..", then "Yes,
    that clarification is needed."
  - Added to §5, "Passive and active readers": the Cauchy belongs to the turn, whether it aims a receiver or an
    emitter, and ranging is the active reader's carried-in amount.
  - §9's lighthouse entry now says so too.
- 19 October, later (SPN R389). Tom: "yes, that clarification means that cauchy is an interesting combination
  capabilities. its not the reader, its not the writer, its the turn itself." §9 now opens with it.
- 19 October, later (SPN R389). Tom: "in draw.html we use the shape library to test cauchy against a. variety of shape,
  and it always returns a unit circle.", then "yes". §9 cites draw's SMP and RCC labs as the principle's controlled test.

**Standing marks.** Each claim carries one:
- **[classical]**: established outside this corpus (surveying, photogrammetry, computer vision, robotics), quoted;
- **[exact]**: exact arithmetic, checked in a plan;
- **[simulation]**: a simulation of our own, checked against a full referee, in a plan;
- **[reading]**: Claude's reading, unruled;
- **[open]**: proposed, not yet tested;
- **[illustration]**: a page, which shows and does not test.

**Keep the case.**
- **Unit relations:** h, v, v₂ are unit relations, 0 to 1. An address is a direction [h : v : v₂], read as two ratios:
  - v₂/h = tan ψ, the azimuth (left–right);
  - v/√(h² + v₂²) = tan a, the altitude (up–down).
- **The step is H.** It is the reader's own start, walked once and never measured, so every map in this paper is in H
  until an amount is carried in.
- **Amounts:** the stride, a door's height, the eye's height, a signal's speed and g are amounts, carried in from outside.
- **Ratios:** k = d/(B/2) is a ratio of two amounts, the pair's reading. Its corner is the pair's, not the reader's
  own h = v.

## 0. Known already: what this paper is, and is not

Mapping from directions is old and well worked:
- **Triangulation and the survey.** Two directions and one measured length fix a place, and a chain of triangles carries
  the length (Snellius 1617; Roy 1785). One base gives the scale; a second base only checks it. **[classical]**
- **Structure from motion.** A moving camera recovers the scene and its own path up to a similarity: one unknown scale
  (Hartley and Zisserman 2003). **[classical]**
- **Bundle adjustment** refines every point and pose together by least squares on the reprojection errors (Triggs et al.
  2000). Robust cost functions replace the squares where errors have heavy tails; the Cauchy (Lorentzian) cost is among
  the standard ones. **[classical]**
- **Monocular SLAM.**
  - The scale is unobservable from one camera without an outside measure (odometry, a known object, an IMU).
  - A far feature, with little parallax, is kept as a direction with inverse depth near zero. It is "a perfect bearing
    reference for estimating rotation" and none for translation (Civera, Davison and Montiel 2008).
  - **[classical]**
- **Base-to-height ratio.** Photogrammetry's rule that depth is best when the baseline is a fair fraction of the
  distance. **[classical]**
- **Reliability.** One redundant reading detects a gross error but cannot locate it; two locate it (Baarda 1968).
  **[classical]**
- **Single-view metrology.** With the scene's planes and right angles assumed (vanishing points), one image gives
  proportions (Criminisi, Reid and Zisserman 2000). **[classical]**
- **Visual hull.** Silhouettes from many views bound a body from outside (Laurentini 1994). **[classical]**

So, like `parallax.md`, this paper is first a **calibration case**: the same mapping, written in the corpus's terms. What
the writing adds:
- a reason for each piece's shape (why scale is the one missing number, why bearing errors are heavy-tailed, why depth is
  best at a baseline about half the distance, why far things are kept as directions);
- a stage-by-stage account of what each needs;
- the prospect of an **address-first** pipeline built from those stages alone (§8).

A result here that looks new should first be looked for in the literature above.

## 1. The stance

The paper explores an alternative for understanding, not for performance (R387). A method built only from the geometry
shows what the geometry supplies and what has to come from outside. A comparison with existing methods is a measurement of
where they agree and where they part, not a contest. A gap either way is informative. **[reading]**, ruled as the stance.

## 2. The reader and its addresses

- **Two inscribed sweeps.** In three dimensions the inscribed sweep is two: the altitude (up–down) and the azimuth
  (left–right), horizon coordinates, each with its corner at 45° (OFS §2; SPN R237; AZM). **[exact]**
- **Even over the wedge.** The reader's uniform sweep of the wedge is even in azimuth and in height (sin a), not in both
  angles: Archimedes' hat-box, Lambert's equal-area map. Then every pair of unit relations is at its corner and the near
  field in both readings is a third. Even in both angles instead, v ≤ h holds for 0.3426, not ½ (AZM). **[exact]**
- **An address is a ratio, not an amount.**
  - The projection divides, not the reader (R306).
  - Each address returned by the sweep is the direction to what it meets.
  - Turning the head lays the addresses, the corner at halfway, the horizon at the end, whether or not anything is there
    (OFS §2, "Sweeping from zero").
  - **[exact]**, the statements; **[reading]**, "lays".
- **Looking down at flat ground,** the sweep from the feet to level is the lighthouse with the eye as the lamp: the
  landings on the floor are a Cauchy whose width is the eye's height, and the corner falls one eye-height out (SPN R386).
  **[classical]**, the lighthouse; **[reading]**, the eye as its lamp.

## 3. One place: a picture

- **What it gives.** From one standpoint, every corner of every thing is an address. So the reader has:
  - the whole layout as directions;
  - the angle between any two things;
  - each thing's angular size (a pair of addresses).

  **[exact]** (`room-ratios.html` step 1; smoke test 42).
- **No distance.** A thing at half or twice its size and distance, about the eye, gives exactly the same addresses (the
  ghosts). Scaling the whole world moves no address: OFS Proposition 8, Theorem 6(a). **[exact]**
- **The outline is free, the face is not.**
  - A thing crossing the view gives its visual hull from the looks alone, up to scale.
  - The face needs a range along each direction, an amount whose unit is the signal's speed. A ranging reader is a writer
    (CFH; OFS §9, "From one place").
  - **[simulation]**
- **Turning in place adds nothing.** A turn about the point seen from moves every direction alike: the frame and the
  corner, no place (HTP P1). A head's eye sits off its axis, so a head turn is a small step (HTP). **[exact]**
- **With a known shape, more.** If the room is known to be a box, its proportions follow from one view (single-view
  metrology). That is a shape carried in, situation 2, not something the sweep supplies. **[classical]**

## 4. One step: the map in H

- **The map.** A second standpoint one step to the side, the step unmeasured (H), and each corner's two rays cross. Every
  place, distance and size then comes out in steps, and ratios between things in no unit at all. **[exact]**
  (`room-ratios.html` steps 2–3; `room-walk.html`; RWT: one known move writes in the reader's own H.)
- **More standpoints sharpen the shape, never the scale.**
  - With 16 to 4,096 standpoints the shape error falls as N^(−0.49) under maximum likelihood.
  - The scale stays at the one outside length's error, and the landmarks' errors are 99% correlated (STC).
  - **[simulation]**
- **Where to step.**
  - Depth per unit angular error is cosh(ln k), least at the pair's corner, d = B/2: the Thales circle (PXC).
  - The total error, depth and across together, is least at d = √2·(B/2) (PXC run 3).
  - Past d ≈ B/ε a place is a ray (PXC; OFS Proposition 11).
  - **[exact]**; the base-to-height rule is its **[classical]** counterpart.
- **The error law of read bearings** (TRI run 1). Bearings read from a height γ (tan δ ~ Cauchy(0, γ)) give:
  - a depth error Cauchy(0, 2γ·cosh(ln k));
  - two standpoints' scales add, never averaging down: √2 over a normal model at the same median error;
  - rays that fail to meet in front as a visible share, 2.6% at k = 8 and γ = 10⁻², against 10⁻³² for normal errors;
  - depth told apart past Δ*/d = (4/√3)·γ·cosh(ln k).

  **[exact]** and **[simulation]**. The reconstruction is unchanged: a different representation of the classical
  solution, with its own error law.
- **Least squares on bearing lines leaves a floor.** STC's P1 was killed by its estimator: least squares on noisy bearing
  lines left an error floor that more readings did not remove, where maximum likelihood kept improving. **[simulation]**
  It bears on §8.

## 5. The second reader

- **The payload ratio is the pair's second coordinate.**
  - The pair's natural coordinates are bipolar: σ, the parallax angle, read by the bearings; and τ = ln(r_A/r_B), read by
    a ratio of amounts received at both standpoints, the unit cancelling.
  - The bridge is named: for light, the inverse square.
  - The σ curves (circles through A and B) and the τ curves (Apollonius's circles) are orthogonal, with one scale factor.
  - Each has its corner: σ's the Thales circle, τ's the perpendicular bisector, where the two amounts are equal.
  - (TRI runs 2–3.) **[exact]**, the coordinates; **[simulation]**, the rest.
- **What the ratio adds:**
  - **On the bisector, nothing to the depth,** but for a second-order pull, −(1 + k²)τ̂²/4.
  - **The lateral place, near the baseline:** better than the bearings for k < 2γ/(0.6745·s).
  - **A stand-in for a missing bearing:** the same law, no better; it rescues 97–99% of the readings whose rays miss.
  - **A check that detects a misread bearing and cannot say which,** since the three w-tests are equal.
    - Against Cauchy bearings it catches only gross misreads, its threshold being the tail's.
    - Far off it cannot tell α from π − α.
  - **[simulation]**
- **Angular size, a bridge-free ratio.**
  - It gives the breadth in H: R̂/R − 1 ~ Cauchy(0, γ(cot β + cosh(ln k))).
  - It gives τ with no physics, but beats the bearings only for an object larger than its distance from the baseline.
  - **[simulation]**
- **The two sweeps together, on a round object.**
  - The object's own Cauchy is the wrapped Cauchy: the Poisson kernel, the harmonic measure from the reader's place.
  - It equals ±(2·dθ/dφ − 1)/2π: twice the inscribed rate less the central rate (CIW).
  - Its parameters are the reader's place in the object's radius, with no unit.
  - From outside it needs each ray's far crossing, which only the central sweep reaches.
  - Only the circle has it.
  - **[exact]**

### Passive and active readers

- **Passive.** A head, an eye or a camera sends nothing out. It receives what arrives. Its turn aims a receiver: each
  direction is an address, and what arrives along it is the payload. From one place it has directions only, no distance
  (§3). **[exact]**
- **Active.** A lidar or a sonar sends out a pulse and times its return. The range along each direction is c·t/2, so it
  needs the signal's speed c and a clock. **[classical]**
  - The range is an amount whose unit is the signal's speed. A ranging reader is therefore a writer: it carries c in
    (CFH; OFS §9, "From one place"; SPN R356). **[simulation]**, CFH; **[reading]**, "a writer".
  - It is a central-sweep reader: amounts along directions it gives itself (OFS §3.1; SPN R309). **[reading]**
  - A held speed that is wrong makes every range off by one factor. Bats in heliox, where sound runs faster (15% in the
    experiment), kept their built-in speed and read every distance closer (WRD; Amichai et al. 2021). **[classical]**, the
    measurement; **[reading]**, the account.
- **The Cauchy is not the passive reader's alone.** It belongs to the uniform turn, whichever way the signal travels.
  - The lighthouse is active. Its lamp's turn lays the Cauchy on the shore (OFS Proposition 5(f)).
  - A scanning lidar's beam sweep does the same, so its directions are addresses laid by its own turn.
  - **[exact]**
- **What each adds beyond directions:**

  | | directions | distance from one place | carried in |
  |---|---|---|---|
  | passive reader | the addresses | none | one amount: a step, a known length, … (§6) |
  | active, ranging reader | the addresses of its own scan | a range per direction | the signal's speed c and a clock |

  **[reading]**, the table.
- **The trade in mapping.**
  - Passive: nothing sent and nothing to calibrate, and it works as far as light arrives from. But it needs a step or a
    known length for size.
  - Active: distance from one place at once. But it costs an emitter, a clock and a speed that must be trusted, and it
    reaches only as far as its own pulse returns.
  - **[reading]**

## 6. The one amount

Sizes need one amount carried in. Any one will do. **[exact]** (RWT: one known move, one exchanged number, one agreed
notch.)

| way in | the amount carried in | in a room |
|---|---|---|
| count the step | the stride, measured once | `room-ratios.html` step 3 |
| a known length in view | a known kind (a door, a brick) | the door's height in steps, so steps → metres |
| the eye's height | the reader's own height | the floor's corner one eye-height out (§2) |
| two eyes | the distance between them | a baseline without walking |
| ranging | a signal's speed | a range per direction (CFH) |
| a falling thing | g | h = ½gt² |
| an agreed unit | a ruler, a notch | between readers (RWT) |

- **One suffices; a second checks.** One amount multiplies every ratio in the map and redraws nothing. A second adds no
  scale; it only agrees or disagrees (OFS §9, "A survey"; Roy's second base). **[classical]**
- **A wrong amount is one factor.** Every size is off by the same factor, on both sides of the corner: one rigid shift
  in levels (OFS §10, step 5). **[exact]**
- **The amount is best near the corner of what it measures.** A step suits a room, a walked base a mountain range
  (PXC; HKO P4: the best half-baseline over [a, b] is √(ab)). **[exact]**
- **Units within units.** A hierarchy of units is held in ratios alone, and writing still costs one amount at the top
  (OFS §9, "Units within units"; the worked example in `runs/ofs/tower.py`). **[exact]**

## 7. Resolution: the lay

- **The lay.** A reader with finite addresses lays them in proportion inside the corner and logarithmically past it (the
  reader's lay 1 + ln s, each level ln 2), so a level holds the same count at every distance (OFS §8; ZOOM; HKO).
  **[exact]**
- **H is a zoom.**
  - A larger H gives more of the near field and less detail to each thing in it.
  - The best H puts the thing read at the corner.
  - Past the held edge a thing is a direction only.
  - **[exact]**
- **Far things as directions.** This is monocular SLAM's inverse depth near zero, reached from the other side: a thing
  past the band is kept as an address (OFS §9, "Far off"). **[reading]**, the correspondence.
- **The address is continuous.**
  - The floor keeps a cell; the reader's point m + iγ keeps a window 2γ that no payload enters (OFS §8, "What the height
    fixes"; DYH).
  - A map's resolution is set by γ and the corner, not by a grid.
  - **[exact]**

## 7½. What it takes to map: the two readers made into a mapper

A thought experiment: start from the two readers as they are, and add only what a map cannot be made without. **[reading]**,
the section; each claim's own mark where it has one; MAP (`plans/map-plan.md`) tests the claims marked *(MAP)*.

**Each reader alone, from one place.**
- **The address reader.** A turn gives a direction to everything met: every corner of every thing, the lines where walls
  meet. It also gives what is in front of what, since occlusion orders things (RSH), but no distance and no size: ghosts
  at half or twice the size and distance sit on the same rays (§3). **[exact]**
- **The payload reader.** It receives what arrives along each direction. Strictly the central sweep stands at a thing's
  centre, which a reader in a room cannot do. From home, the payload is the wave itself: colour, brightness, texture, and,
  if the reader ranges, an amount (§5).

Neither maps alone: the first has where without how far, the second what without where.

**Joined at one place.** The payload labels each address: this direction is brick, that one the table's edge. Its first
job is identity, not geometry.
- **Ranging with the unit unknown.** If the payload carries an amount in proportion to distance, such as an echo's time
  with the speed of sound unknown, one place gives the whole room up to one scale. The unknown unit cancels from every
  ratio of amounts, so the shape comes out in the payload's own unit (WRD's bats in heliox: the unit wrong, the shape
  right). *(MAP M5)*
- **Brightness.** Distance comes only by assuming a known kind, the same paint under the same light. That is carried in.

**What a passive reader adds to map.**
1. **A second standpoint and the turn between the views.** The step's length is never read. The turn comes from far
   features that show no parallax, which fix rotation and not position (Civera, Davison and Montiel 2008). *(MAP M6)*
2. **Correspondence: the same point at both standpoints.**
   - With exact readings and the turn known, the addresses alone find it: in three dimensions two rays generically do
     not meet, so only the true partner's ray crosses (the epipolar constraint, Longuet-Higgins 1981).
   - At a finite resolution ε, many rays pass within reach of each other, and geometry alone becomes ambiguous.
     *(MAP M1)*
   - The payload resolves that. The same brick or the same edge, received at both standpoints, names the pair.
     *(MAP M2)*
   - So: **the address says where, the payload says which.** Each also checks the other. A wrong match pairs two rays
     that do not meet, and the geometry flags it. *(MAP M4)*
3. **Holding.** Two addresses compared must be held together, at once or in order. Each hold gives one ratio.
4. **The band.** Places come out only inside d ≲ B/ε; past it, directions (§4, §7).
5. **More standpoints.** These fill in what occlusion hides, and the visual hull tightens with each view (CFH).
6. **A second route.** A loop that fails to close says something was misread (OFS §9, "Closing a loop"). *(MAP M4)*
7. **A still room, or swaps told apart.** A step moves every address by a pattern parallax fixes. A payload changing at
   fixed addresses is something moving (MON, SKY).
8. **One amount, for metres only.** Until then every place is in steps. *(MAP M3)*

| part | supplied by | cost |
|---|---|---|
| directions | the turn (address reader) | free |
| which point is which | the payload | free, where the payload is distinctive |
| distance up to scale, from one place | a ranging payload in an unread unit | free only with ranging |
| places in steps | a second standpoint plus correspondence | a move |
| the turn between views | far features with no parallax | free |
| an error check | the rays of a match meeting; a closed loop | free; a second route |
| metres | one counted stride | carried in |

So the mapper is the two readers, four acts (turn, hold, step, match) and one amount. The match is the act the address
reader cannot finish alone at finite resolution, and the one the payload reader exists to do.

**Known already.** Structure from motion works exactly so. A keypoint's position in the image is its address, and its
descriptor (Lowe 2004) is its payload, used only to find the same point in another view. The epipolar check is the
address checking the payload. **[classical]** None of it is described as address and payload. What the framing adds is
the division of labour stated as a rule, with three consequences:
- each half can be tested apart from the other;
- the bearings' error law (§4) points the estimator to medians;
- a range in an unread unit is a reader, not a writer, so scale stays out of every stage but the last.

**MAP, runs 1–2.** **[exact]**, in a synthetic room of 80 features and 6 far ones.
- **Pairing.** With exact readings the addresses pair every point alone; the nearest wrong pair passes 2.8·10⁻⁴ |AB|
  apart. At 1 mrad a seventh of the rays have a rival within reach, at 10 mrad five in eight.
- **Matching by payload.** It gets all 86 right, and places come out to 10⁻⁴⁸.
- **Checking.** A wrong match's rays pass at least 0.011 |AB| apart, and a third standpoint separates the swapped
  features.
- **Scale.** Scaling the world moves nothing until the stride writes metres.
- **One place.** A ranging payload in an unread unit gives every distance ratio from there, and every place off by its
  unit.
- **The turn.** Six far features give the rotation between views to 10⁻⁶ rad. Places with it are worst for features
  seen across little parallax, about δ·d/γ. The plan's bound of 10⁻⁴ |AB| was missed narrowly, at 1.02·10⁻⁴.

## 8. An address-first pipeline

What a mapper built only from the stages above would do, against the usual pipeline. **[reading]**, the whole section;
**[open]**, whether it works.

| | the usual pipeline | address-first |
|---|---|---|
| what is stored per feature | a 3D point, or inverse depth | its addresses from each standpoint, [h : v : v₂] |
| units | metres from the start, or a scale fixed early | none: everything in H, one multiplier at the end (§6) |
| estimating | least squares, often with a robust cost | the addresses' own statistics: medians and quartiles, at the corner |
| far features | inverse depth near zero | directions past the held edge, kept as addresses (§7) |
| resolution | uniform pixels | in proportion near, logarithmic past the corner (§7) |
| arithmetic | trigonometry and matrix solves | ratio forms: tangent addition, exact and trig-free |
| checks | residuals after the fit | closure (OFS §9, "Closing a loop") and the payload ratio (§5), detection by construction |
| the second reader | rarely used for structure | the payload ratio's coordinate τ, angular size, and on round things the combined sweeps (§5) |

The stages, each with what it needs:
1. **Lay the addresses:** H, and the drawing V = V₂ = H. Nothing else.
2. **Read one place:** the sweeps. The layout, angles and angular sizes. No amount.
3. **Take a step:** H, walked. Places and sizes in H.
4. **Add standpoints:** more of the same. The shape improves, the scale does not.
5. **Close loops:** a second route. Errors detected, located with two redundancies.
6. **Add the second reader:** a payload received at two standpoints, with its bridge named. τ, a check, rescues.
7. **Write:** one amount. Metres.

Why it might hold up, each a prediction to test:
- **Exactness far off.** Ratio forms keep their precision where angles lose it. An angle holds a large ratio only to
  ulp·(1 + x²)/x; the capped unit relation holds it to 1.5·10⁻¹⁶ at every size (MOT P10). **[exact]**, for single ratios;
  **[open]**, for a whole map.
- **Robustness by construction.** Medians suit the heavy-tailed error law of §4, where means do not settle. **[exact]**,
  the law; **[open]**, the estimator's performance.
- **Simplicity.** No scale decision until the end, and views compose by tangent addition. **[reading]**

Why it might not: least squares with a good robust cost is hard to beat on accuracy, and decades of engineering sit behind
it (§0). The Cauchy cost is already one of those costs. **[reading]**

## 9. The Cauchy's place

The Cauchy is the law of the uniform turn itself: not the reader's, not the writer's, not the payload's (SPN R389). Any
uniform turn lays it, whether it aims a receiver (an eye) or an emitter (a lamp, a lidar's beam), and whatever uses the
turn inherits it. That is why one law serves a passive eye, an active lamp and a ranging scanner, each adding its own
amount, or none, on top. **[exact]**, that the law is the turn's (OFS Theorem 6(a)); **[reading]**, the wording.

Its earliest controlled test is draw's SMP lab (`reportbase/draw`, `draw.html?lab=smp`). The lab reads each shape of the
shape library twice:
- **stepped evenly in the turn:** the census comes back as the unit circle for every shape;
- **walked at constant speed along the outline:** what comes back is the shape's own arc element, different for each
  shape.

The shape enters the turn only as what is met along each direction (the central reader's radii). A walk paced by the
outline's length is not a turn, so the shape shows in it. draw's RCC lab says the same of one reader: its readings carry
the turn, not the size. The corpus met it again in RSH (the census one sphere), in `h-chain.html` step 3 and in HZT.
**[simulation]**, the labs.

Nothing in §§3–7 needs the Cauchy by name. It enters in four places:
- **as the uniform sweep's law,** which lays the addresses (§2);
- **as the error law of bearings read at finite resolution** (§4);
- **as the lighthouse,** when the sweep lands on a flat surface (§2). The turn may aim a receiver (an eye) or an emitter (a
  lamp, a lidar's beam); the law is the turn's either way (§5, "Passive and active readers");
- **as the wrapped Cauchy on a round object,** when the two sweeps are combined (§5).

In each, it is the law of addresses, not of what arrives (OFS §7.2, "The rule"). **[exact]**, the four statements;
**[reading]**, that this is why the pieces of mapping have their shapes.

## 10. What stands on what

- **[exact]** throughout: the addresses (§2), one place (§3), the map in H (§4), the payload coordinate (§5), the one
  amount (§6), the lay (§7).
- **[simulation]** on our own referees: STC, TRI runs 1–3, CFH.
- **[classical]**, every reconstruction step (§0).
- **[reading]**: the address-first pipeline (§8) and the Cauchy's place (§9).
- **[open]**: whether the pipeline works, and where it parts from bundle adjustment (§11).

## 11. Open questions and the test queue

0. **MAP: what it takes to map** (§7½). Predictions in `plans/map-plan.md`, exact and seeded, run before AFM. **[open]**
1. **AFM: the address-first mapper against bundle adjustment.**
   - The setting: a synthetic room (the `room-ratios` scene, scaled up to many features) with bearings read at a finite
     resolution γ, outliers mixed in, and a referee.
   - The comparison: the address-first mapper against least squares and against a Cauchy-cost bundle adjustment, on the
     same readings.
   - The measures:
     - accuracy near and far;
     - breakdown as outliers rise;
     - behaviour far off (k = 100–1,000);
     - computation;
     - what each needs carried in.
   - A measurement, not a contest (§1). Predictions first, in `plans/afm-plan.md`.
   - **Run 1, structure only (poses fixed), [simulation].** Under Cauchy bearings, least squares stalls: its error falls
     by 1.39 from 4 to 16 standpoints. The Cauchy-cost adjustment (CB) stays the most accurate: 0.59·10⁻³ at 16. The
     address-first median (AF) improves fastest (factor 3.95, to 0.75·10⁻³).
   - Under normal bearings AF is within 6% of least squares, and with poses fixed it is the cheapest of the three.
   - AF survives wrong matches to 45% (0.293 for all pairs, later because pairs not meeting ahead drop out). CB gives
     way at 35–40%.
   - Killed in that run: F2 (AF was less costly under normal errors than predicted), F3 narrowly (least squares at 10%
     outliers was 9.97 times, not more than 10) and F5 (AF was faster, not slower).
   - **Run 2, the poses not given, [simulation].** Every stage was a median of pairwise quantities: the turn from pairs
     of far features, the step's direction from pairs of the epipolar constraint's normals, its length, then the places.
     - Clean, it reached 8.7·10⁻³. A Cauchy-cost bundle adjustment started from it reached 1.8·10⁻³.
     - It broke between 10% and 20% wrong matches, as the share of clean four-reading pairs, (1 − f)⁴, predicted
       (0.159).
     - Its weak stage is the turn: six far features in one window, 1.5°–26° apart, fix it to about γ/sin(angle).
     - Started from a broken turn, the robust adjustment does not recover.
     - Killed: G1 (the clean error, against my 3.7·10⁻³) and G4 (the robust adjustment's 7.8× at 10%).
   - **Run 3, a robust turn, [simulation].** Twelve far features spread over the sphere, and at each pose stage the
     candidate with the most agreeing readings kept before the median (RANSAC's consensus, Fischler and Bolles 1981).
     - Spreading fixes the conditioning: clean, 2.39·10⁻³ with medians alone. The medians still break between 10% and
       20% wrong matches (232× at 20%).
     - Consensus fixes the breakdown: 1.98·10⁻³ clean, 2.68 times that at 30% wrong matches. A Cauchy-cost bundle
       adjustment started from it holds to 2.23 times, better than its start.
     - Killed: H1 narrowly in its turn clause (the worst turn 0.251°, against my 0.2°).
   - Open: minimal sets of room features in place of far ones, far features as targets, real images.
2. **Medians against least squares on bearing lines.** STC's floor (§4) suggests least squares on Cauchy-like bearings
   stops improving. At what rate does a median-of-crossings estimator improve, and does it keep improving? **[open]**
3. **Exactness of a whole map in ratio forms.** Does MOT P10's exactness survive composition over many standpoints and a
   closed loop? **[open]**
4. **Where to put the next standpoint.** The corner says where one step is best (§4). Is there a corner rule for choosing
   the next of many, and is it the base-to-height rule? **[open]**
5. **Closure with the payload ratio.** Two redundancies locate a misread (Baarda). How far does a loop with payload ratios
   at each standpoint take that, against Cauchy bearings? **[open]**
6. **One view with a known kind.** A box room from one place (§3). Which proportions does a known right angle give, and
   how do its errors compare with a step's? **[open]**
7. **Moving things.** A room with a thing moving through it: what the detections alone give (MON, SKY), and what a map
   held in H does with them. **[open]**
8. **Real data.** A published multi-view dataset with known geometry, once the synthetic runs stand. **[open]**

## References

- Amichai, E. et al. (2021). *Proceedings of the National Academy of Sciences*, doi:10.1073/pnas.2024352118.
- Baarda, W. (1968). *A Testing Procedure for Use in Geodetic Networks*. Netherlands Geodetic Commission, Publications on
  Geodesy 2(5).
- Civera, J., Davison, A. J. and Montiel, J. M. M. (2008). Inverse depth parametrization for monocular SLAM. *IEEE
  Transactions on Robotics* 24(5), 932–945.
- Criminisi, A., Reid, I. and Zisserman, A. (2000). Single view metrology. *International Journal of Computer Vision*
  40(2), 123–148.
- Fischler, M. A. and Bolles, R. C. (1981). Random sample consensus: a paradigm for model fitting with applications to
  image analysis and automated cartography. *Communications of the ACM* 24, 381–395.
- Hartley, R. and Zisserman, A. (2003). *Multiple View Geometry in Computer Vision*, 2nd ed. Cambridge University Press.
- Laurentini, A. (1994). The visual hull concept for silhouette-based image understanding. *IEEE Transactions on Pattern
  Analysis and Machine Intelligence* 16(2), 150–162.
- Longuet-Higgins, H. C. (1981). A computer algorithm for reconstructing a scene from two projections. *Nature* 293,
  133–135.
- Lowe, D. G. (2004). Distinctive image features from scale-invariant keypoints. *International Journal of Computer
  Vision* 60(2), 91–110.
- Roy, W. (1785). An account of the measurement of a base on Hounslow-Heath. *Philosophical Transactions of the Royal
  Society of London* 75, 385–480.
- Snellius, W. (1617). *Eratosthenes Batavus*. Leiden.
- Triggs, B., McLauchlan, P. F., Hartley, R. I. and Fitzgibbon, A. W. (2000). Bundle adjustment: a modern synthesis. In
  *Vision Algorithms: Theory and Practice*, LNCS 1883, 298–372. Springer.
