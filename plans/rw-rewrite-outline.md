# Rewriting *Reads and Writes*: outline, map and checklist

10 Nov 2026. SPN R788. Tom: "the write is the scale variant companion to the read."; "seems to me that ehule'rs captures
this idea nicely. lets build out from that equation, to settle on definitions."; "option 1"; "proceed with 1 and 2", to
archiving the paper and outlining a clean rewrite.

**Step 1, done.** The paper as it stood (version 17, 25,980 words, sha256 `f4e681ad…5abf03a`) is frozen as
`papers/archive/rw/reads-and-writes-record.md`, **a frozen record, never edited**, like OFS's records. Section numbers
cited before 10 Nov are the record's. Until the new paper's first draft is whole, `papers/readers-and-writers.md` stays
as it is and stands.

**Step 3, done 10 Nov** (Tom: "proceed", taking the outline and the open points as proposed, "place" kept): the new
paper written into `papers/readers-and-writers.md`, 18,500 words against the record's 25,980 (the target of half was
not met: every result was kept, and the cut came from repeats). Every checklist number below was found in the new text by
a scripted search (one paragraph, the thumb's lay as a turn on Euler's plane, was missing on the first pass and added to
§2). The open points stand in the new paper's §12 as O1–O7, renumbered there. Boxes below are left as the plan wrote them;
the search is the tick.

**Step 2, this note.** The new paper's definitions, its structure, a map from every section of the record to its place in
the new paper (or why it is dropped), a checklist of results and checked numbers that must survive, and the points still
open. Tom approves this before any prose is written. Then step 3: the new paper written into
`papers/readers-and-writers.md` (the file name kept, so links hold), section by section, each checked against the record.

**The paper's purpose.** Not for external publication: it is the source of truth that AI sessions iterate on (Tom, 10
Nov). So it is written as a specification: numbered definitions first, each claim marked **classical**, **checked**
(with where), or **reading** (ours), one home for each idea, and the open questions in one place. Length is secondary to
consistency; the target is half the record or less, by cutting repeats, not results.

## 0. The ruling the rewrite is for (R788)

The write is the scale-variant companion to the read, and of the two ways to state it (in conversation, 10 Nov) Tom
chose option 1, the one the mathematics gives:

- On Euler's plane, ln(z/H) = ln(d/H) + iθ, scaling the world by k (every length, **the reader's thumb and stride
  included**; units stay outside the world, R782) slides every point across by ln k. A slide keeps differences across
  and moves only where the across axis's zero sits against an outside unit.
- So the sort is by invariance under the scaling group (Klein; the paper's Jaynes), not by whether something is counted.
  A count of strides is a whole-number record of a ratio d/stride; its discreteness is how it is kept, not what it is.
- Three kinds result, sorted by two independent questions:

| | moved by scaling the world? | held by one standpoint? | name |
|---|---|---|---|
| a direction [h : v] (up on the plane) | no | yes | **read** |
| a gap across: a distance in thumbs, one distance against another | no | no: needs a second standpoint and the step between (parallax) | **place** |
| the across axis's zero tied to a unit carried in (a metre, a second) | yes | no | **write** |

The first column is R788; the second is the record's Proposition 8 (one read holds no distance). The record's "write"
covered both "no" answers of the second column. Under R788 only the last row is a write.

"Place" is the working name for the middle kind (the record already says "places in thumbs", "places in strides");
Tom may rename it before step 3.

## 1. Definitions (the new §1, as drafted for Tom on 10 Nov)

1. **One point, two parts.** A point seen from a standpoint is, in the writer's notation, ln(z/H) = ln(d/H) + iθ, H the
   thumb held out: up the direction, across the distance in thumbs. In space the point is d·u, u a direction, and the
   across part is unchanged.
2. **A read** is the direction: [h : v], up on the plane. It is taken from one standpoint at one moment, with its heat
   given and the paint met along it. One read holds no distance.
3. **A place** is a gap across: a distance in thumbs (d/H), or one distance against another. Scaling the world leaves it
   unchanged, as it leaves a read; but no single read holds it. It needs a second standpoint and the step between
   (parallax). V\*/H is a place; so is a time to contact in the reader's own ticks.
4. **A write** is an amount: the across axis's zero tied to a unit carried in from outside (a metre, a second). Scaling
   the world moves it. One amount serves every place hung from the same thumb.
5. **The first test.** Scale the world by k: every length, the reader's thumb and stride included; units stay outside.
   What moves is a write; what stays is a read or a place.
6. **The second test.** Change what arrives, keeping the standpoint and the turn: it separates a direction and its heat
   (they stay) from the paint (it changes).
7. **Joining and recording.** Joining reads gives places and orders, not writes. A count or a mark kept is how a write
   is recorded; being an amount in a unit is what makes it one.

Each later section is checked against these seven. The standing vocabulary rules carry over unchanged: name the thumb
whenever H comes up (R618); a reader's far field in ratios (one in two, one in four), a writer's counted in thumbs, never
"doubling" or "level" (R622, R642); V is the mountain in the distance (R622); never give a reader a circle, sphere or any
shape, it has a vantage (R623, R643); V never enters a read, never "cancels" from one (R654); heat and paint for the
reader, "address" only as a computing metaphor or a writer's count (R706, R707); π/2, 2/π and the one-length circle the
writer's (R717); a read is the quarter turn, the hemisphere in front its whole (R696, R700); the Cauchy has no near or
far, H lays them as an overlay (R703); trigonometry the writer's tool (R742).

## 2. Structure of the new paper

| new | content | from the record |
|---|---|---|
| Abstract | the plane, its three kinds, the two tests, the heat given and the paint met; no new mathematics, a division of it | Abstract, rewritten round R788 |
| 1 Definitions | §1 above, with the room mapped without a ruler as the opening picture (one corner: reads; one step: places; the stride in metres: a write) | §1 "Words", the room, "The write", the two tests, "V" |
| 2 The plane | ln(z/H) = ln(d/H) + iθ; up, across, the across zero; the two corners as the plane's mirror lines (θ = 45°, d = H); the zeros of the two axes (home and the thumb); the asymmetry: up closes (a quarter turn per read, a horizon), across is open both ways; in space d·u; the sphere's equation divided by the thumb (the paper in one equation) as the same split | §1 "One plane", "The paper in one equation", "In space the one plane parts", §5 "π with the direction, e with the payload", §6 "Euler's plane" |
| 3 Up: the read | what a read is (every sweep of the thumb at once, given, no time); the uniform turn and the half-Cauchy; corner, quartiles, horizon, no mean (and why: a direction has no length to add); the heat (cos²θ, cos³α, cos^(n+1)); the heat depends on what it is counted per; Radon–Nikodym / Poisson kernel / harmonic measure; the Cauchy's routes and "find the z"; the standpoint m + iγ, closure under real Möbius maps, what breaks it; the distance between standpoints (Fisher–Rao) as a place; reads do not conflict; passive; the reader never sees a shape; a vantage, not a shape; the Cauchy derived from one length, two axes, a line in the world (the table); the circle's equation divided by its own length | §1 "What a read is", "Reads do not conflict", §2 entire, §7 "Where the heat comes from", "The heat depends…", "Heat maps combine…" |
| 4 The paint | the second test in full; the payload not lost (ratios, dividing the heat out, undoing the blur, averaging), except its overall size a₀; a shape about a centre ln r = a₀ + f(θ): f a set of places, a₀ a write; the lighthouse and Mercator as two-axis drawings; the moving sky (aberration the directions, Doppler the payload) | §2 "Heat and paint", "The payload is not lost", §3 "The lighthouse", "Mercator's map", "A moving sky" |
| 5 Near and far | H as the overlay on the read; the crosshairs; one thumb split on every direction; the near field in proportion, the far in ratios; the distance heat sech(ln(d/H)); the hot spot; H a zoom, K before H; K and N, the cull; laid by the heat (Lambert); the read as a control (the dial, the dome); drawing a shape from a height (epicycles, Takenaka–Malmquist) | §6 entire, §7 "The heat map reaches the horizon…", "The hot spot…", "Where the split falls" |
| 6 Across: places | parallax as a sum of reads (exact Cauchy depth, the two ways out); turning teaches the directions, walking the world; motion from reads (τ, τ̇, Lee) restated: τ in own ticks a place, seconds a write; walking to the mountain and the mountain's own corner (Z = (1 + is)/(1 − is), two paces, the telescoped product); knowing V by degrees restated: places by degrees, the write only at the agreed unit; the thing itself as H; the tower of places (one write at the top, loops check, the slide rule); turns, counts and corners (Gibbs, the 73 outlines) | §8 entire but the survey, §9's opening ("Ratios suffice") |
| 7 The zero: writes | the unit carried in; a survey (Snellius, Roy); what a blueprint adds (the seven capabilities); write once, then read again ("And back"); recovered, by writing; a read is geometry, a write is physics (the sheet of paper) restated: places are geometry too, physics enters with the unit; continuous and discrete as how writes are recorded | §8 "A survey", "Recovered", "And back", §9, §1 "A read is geometry…", "Two geometries", "Continuous and discrete" |
| 8 In space | three parties; the wedge the writer's description, the reader's heat map; one thumb, two, three; the sphere without V and the cone of one read (the table); setting H sets the near-field sphere (the writer's account); the shape swept, not each thumb; the writer's cube; what survives in space; the three loops (a turn and a scaling close; two turns leave Ω; a turn with an unequal stretch leaves ζ, conjugate to a squeeze, eigenvalues e^(±ζ)); two boosts joined (Thomas–Wigner) | §7 rest, §1 "A loop of a read and a write", §3 "Two hands", "Two boosts joined" |
| 9 Which numbers belong to whom | rates, not angles (the per and the of; the writer's rate 1; π/2 and 2/π the writer's measure of the sweeps; two 1's); the rationals, square roots, transcendentals; Euler's formula as a count of reads; the Cauchy's constant from the turn; one pole, the constant and the phasor; π with the direction (period), e with the across axis (base); met, not made | §4, §5 |
| 10 Worked example | the mountain and the thumb, with places and the write kept apart (walk one thumb: d = 10 thumbs, a place; count the thumb in miles: a write); the tower and two thumbs | §10 |
| 11 Cases in data | LIGO [H1 : L1], the quasar dipole, one photon at a time, Berry's phase; and the seed kernels, where it failed | §11 "Three cases in data", "And one where it failed" |
| 12 Open questions | in one place (below) | scattered through the record |
| Where the ideas come from, Code and data, References | carried over, Code and data updated | the same |

**Pictures.** The record's §3 "Five pictures" is dissolved: each picture goes where it does work (the hand and two hands
to §3 and §8, the lighthouse and Mercator to §4, the moving sky to §4 and §8). The breath (record §8, the walk's breath)
goes, see §4 below.

## 3. What R788 changes, passage by passage (to be rewritten, not carried)

| record | says | becomes |
|---|---|---|
| Abstract | "The passage from reading to writing is parallax" | parallax is the passage from a read to a place; the write comes with the unit |
| §1 "Reads are unconnected" | their order, and anything said across them, is a write; two reads joined only across a counted step, parallax, and so a write | joining reads gives places and orders; a single read carries nothing from the one before |
| §1 "A read is geometry, a write is physics" | a write is the recording of a read | a write is an amount in a unit; recording is how it is kept; places are geometry, physics enters with the unit |
| §1 "Continuous and discrete" | a write is a count | a write is recorded as a count; the count of thumbs is a place |
| §1 "One plane" | across is writing | the across axis carries places; only its zero, tied to a unit, is a write |
| §1 "A loop of a read and a write" | across by a scaling of the thumb is a write | the scaling is the first test's own motion; the loops are compositions, the writer's account (joining) |
| §2 "How far apart two standpoints are" | unmoved by scaling, yet a write | a place |
| §5 "One length, counted, makes the rationals" | counting is done in parallax and in writing | counting thumbs makes places; the rationals are places' |
| §8 "Parallax is the passage", "Motion, from reads", "Walking to the mountain", "Knowing V comes by degrees" (In what) | places in thumbs, τ in ticks, strides counted are writes; "V is written as V\*/H" | places; only the stride or the tick counted in an agreed unit writes |
| §8, the walk's breath | each stride is an exhale, a write | dropped (§4 below) |
| §10 "Walk one thumb" | "In thumbs, exactly. Count the thumb in miles" | d = 10 thumbs and V = 20 thumbs are places; miles the write |
| §11 "The roles move" | writes while it walks, counts | places while it walks and counts; writes when it agrees a unit |

A full sweep for the record's other uses of "write"/"writer" for scale-invariant things is part of step 3, section by
section, against definition 7. "The writer" as a vantage (both hemispheres held, every sign, the extents in amounts)
stays: the writer is who holds the across zero tied to a unit, and so every amount.

## 4. Dropped, and why

- **The walk's breath** (record §8, the paragraph after the telescoped product, R781). Under R788 a stride is a place, not
  an exhale, and the paragraph's "at rest the asymmetry is plain" rested on the stride being the write. The breath stays
  in `plans/breath-note.md`, a working note, as R727 and R779 first had it. If it returns, it returns as the plane's two
  parts of one observation (up the read, across the places, the zero the write), not as two moments.
- **Repeats.** The record says many things several times (the corner's roles, the heat's cos³α, "the reader has no
  shape", the thumb as H, π/2 and 2/π the writer's, the crosshairs). Each gets one home in the table above and is
  referred to from elsewhere.
- **Ruling-log phrasing.** "A first version drew it as a closed dome…" and similar self-corrections: the record keeps
  them, the new paper states the result.
- Nothing else is dropped. Results move; none is cut.

## 5. Checklist: results and checked numbers that must survive

Each item is ticked in step 3 when its new home is written, with the record's wording checked.

**The read and the heat**
- [ ] Half-Cauchy (2/π)/(1 + s²): median 1, quartiles √2 ∓ 1, horizon [0 : 1], no mean; averages climb (2/π)·ln 10 a tenfold
- [ ] the bounded chart s/(1 + s) averages ½; order statistics commute with every increasing map, the mean does not
- [ ] unit vectors over the quarter turn average (2/π)(1, 1), length 2√2/π ≈ 0.900
- [ ] a world capped at M: mean (1/π)·ln(1 + M²) over the share below M, ≈ 8.8 at M = 10⁶
- [ ] the density is the share squared: 1/(1 + s²) = h²; dθ = ds/(1 + s²)
- [ ] the three forms: one length (scale 1), two axes (scale V/H), a line in the world (C(m, d)); the ratio of normals the same three
- [ ] the reader at i; closure under real Möbius maps; what breaks it (an edge, a square, a sum of amounts)
- [ ] routes: turn, walk (Kakutani 1944), pole (γ/π)·|1/(x − z)|², sum, Möbius; one measure in the plane, flat boundaries in any dimension, parting on curved ones; "find the z"
- [ ] Fisher metric (dm² + dγ²)/(2γ²), KL 2·ln cosh(d/2), |ln r| at one foot (Chyzak and Nielsen)
- [ ] heat cos²θ (plane), cos³α (space), cos^(n+1) with n thumbs; 0.35 of peak at 45°, 0.125 at 60°; vignetting cos⁴α, three of four cosines the heat (0.35 against 0.25 at 45°)
- [ ] half the peak heat at 37.5°, a fifth of the directions inside; half within 60° (√3 thumbs out); share within α is 1 − cos α
- [ ] Radon–Nikodym: dν/dλ = (1/π)·d/(d² + y²); half-space kernel Γ(n/2)/π^(n/2)·d/|x|^n = (2/|S^(n−1)|)·d/|x|^n; Poisson semigroup e^(−d|k|); Laplace, not the heat equation; Gaussian e^(−tk²); box blur's zeros
- [ ] heat maps add without reconciling; readings added give one Cauchy (z₁ + z₂); averaging n readings no narrower

**The paint**
- [ ] payload recovered by ratios (every mode of f, not a₀), by dividing the heat out (ρ(θ)·2/(π(1 + s²))), by undoing the blur (e^(γ|k|)), by averaging; Faraday rotation RM·λ² a write, the intrinsic angle a read (Burn 1966)
- [ ] lighthouse (x − α)/β = tan θ; halfway flash at arctan c on a ruler c times the sea's; β from half the interquartile spread
- [ ] Mercator tan ψ′ = tan ψ/c, true only at c = 1; areas sec²φ; Greenland about as large as Africa, some fourteen times its area; equal area c = cos²φ
- [ ] moving sky: aberration z ↦ z/k, k = e^η; spherical Cauchy D²/4π; the sky's uniform heat (1/π)·dA/(1 + |z|²)², not the plane's 2D Cauchy; no law boost-invariant; Doppler D = √(1 − β²)/(1 − β cos θ′); D⁴ = D² × D²; pseudorapidity slide; the census condition
- [ ] two boosts: tan(Ω/2) = ab·sin φ/(1 + ab·cos φ); ε²·sin φ, curvature −1 against +1; next order −ε²/12 against (1/3 + cos φ/4)·ε²; checked to 10⁻⁵⁸; the Lorentz group enters by Liouville, not derived

**Near and far**
- [ ] the corner √2 thumbs along the look in the plane, √3 in space; one thumb splits every direction's distance heat in half
- [ ] far field in ratios; 1 + ln(d/H) and 2 − H/d the writer's numbers
- [ ] the one-thumb circle 35.26° about the look, 73% of the wedge's directions; ±45° in the plane; three pairs' corners 120° apart, home 35.26°, horizon 54.74°; squeeze one over twice the reading toward home; tan α/α 1.10 at 30°, 1.27 at 45°
- [ ] Lambert 2·sin(α/2): 0.9% at 15°, 3.4% at 30°, 7.6% at 45°; rings 0.765, 1.05, 1.23, 1.32 toward √2; shares 0.26, 0.20, 0.12, 0.12; the ground (2/π)·atan(D/ρ); a world culled at π/(8K)
- [ ] the dial: place H·sinh ζ, needle gd ζ; corner ζ = 0.881; one in two each ln 2 of ζ (2.31, 2.0037, 2 within 4·10⁻⁵); cos²θ; the dome cos³α; Shepard tones
- [ ] distance heat (2/π)·arctan x; per ln(d/H) (1/π)·sech(ln(d/H)): 0.8 at ×2, 0.47 at ×4, 0.25 at ×8; shares past 2, 4, 8 thumbs 0.295, 0.156, 0.079; K places at d/H = tan(kπ/2K), K/2 inside
- [ ] Euler's plane: a writer's line u = ln(p/H) − ln cos(θ − φ₀); a log spiral straight; g = ½ + gd(ln(d/H))/π; the sphere stereographically, one thumb the equator; tan(χ′/2) = tan(χ/2)/k; dθ·dκ/κ the plane's area; the read 1/sin χ per unit of the sphere's area; checked to thirty digits
- [ ] in space: line × sphere of directions; Lambert stretched 1/cos(φ/2) at the old look, up to 2 at a quarter turn; stereographic a quarter as hot at its rim; Gauss 1828, Euler 1777 (FLC)
- [ ] K and N: an infinite star field at N and 2N apart by under 10⁻⁷ at N = 2⁴⁰; O(K)
- [ ] epicycles: e^(−γ|k|); a dent in 11 aimed terms against 85 circles to 10⁻³; broad outline 10 against 19 (Qian and Wang 2011)
- [ ] heat-cube: 436 nearer, 1,291 farther from a corner of a 12-a-side box looking at its middle

**Places (across)**
- [ ] parallax: cot a + cot b = B/depth; D = B/conj(w_a + w_b), w = (c + iγ)/(1 − iγc), at every γ; at the corner D = d·e^(2i·atan γ); the lateral place's density infinite over each standpoint; two quarter turns: density (4/π²)·s near zero, tail 1/d³, a mean; repeated reads: the median narrows, the mean gains nothing (McCullagh 1992)
- [ ] error ε·cosh(ln k) = ε·(k + 1/k)/2; ε at the corner, ≈ ε·d/B far, a direction alone near d = B/ε; k = 20 in the worked example, 10.025 ε
- [ ] the thing itself as H: 1/(2·tan(α/2)) breadths off; as the focus, in passes
- [ ] Lee's τ̇ ≥ −½, the stop at −½; steady pace −1
- [ ] the walk: v/h = (V\*/d)/(H/L); d_c = V\*·L/H (thirty breadths for 2 cm at 60 cm); d and d_c²/d reciprocals; V\* = strides × H/L
- [ ] the mountain's own corner: Z = (1 + is)/(1 − is), Z = i at s = 1, −1 at the foot; d_c sixty times nearer; spans 14°, 28°, 53°, 90°, 127°, 152°, 166°, gains 14°, 25°, 37°, 37°, 25°, 14°; sech x per x = ln(V\*/2d); dα/dℓ = V\*/((V\*/2)² + d²); π/2 from the corner either way, π from home; ∏ Z_(j+1)/Z_j = Z_N/Z_0
- [ ] turns, counts and corners: Gibbs ≈9% (Wilbraham 1848, Gibbs 1899); 73 outlines, ρ 0.85 and 0.55 against 0.59 and 0.00; rounding a corner takes even samples from 2–3× a Bézier path to ½–¾
- [ ] tower of places: one amount at the top; a loop shows a misread, cannot place it

**Writes**
- [ ] the survey (Snellius 1617, Roy 1784–85); a second base checks, adds no scale
- [ ] seven capabilities of a blueprint
- [ ] a write is over and must be read; recovered exactly yet partially; completeness never a read

**In space**
- [ ] the wedge's 2D Cauchy 2/(π(1 + a² + b²)^(3/2)); every pair at its corner; near field a third; triple corner at azimuth 45°, altitude 35.26°
- [ ] the hemisphere's 2D Cauchy 1/(2π(1 + r²)^(3/2)); the wedge 35.26° at a home, 54.74° at a thumb
- [ ] sphere, Cauchy plane, cone: the table; a cone the one shape scaling about its apex keeps
- [ ] near-field sphere: inversion at H carries far onto near; along each ray 2H/(π(H² + d²))
- [ ] swept per thumb: v below h for 0.343, near field 0.233; swept together ½ and ⅓ (Haar, Euler); any linear map gives an elliptical Cauchy, five numbers in space
- [ ] a camera's look along h: home at the middle of the cross; triple corner 54.74° off; the look down the diagonal the only one putting all three corners under the crosshair
- [ ] three laws on the sphere (harmonic measure, spherical Cauchy, neither the other's image); quarter turns 120° apart by order; α = β = 10°: 1.741° against 1.745°
- [ ] loops: turn + scaling closes (plane and space); two turns cos(Ω/2) = 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ, ≈ αβ·sin φ, bounded; turn + stretch cosh ζ = 1 + 2·sin²α·sinh²(½ ln c), ζ ≈ |α·ln c|, same at c and 1/c, nζ after n loops, closed only at c = 1. Wording fix: ζ is from the trace (the loop's net map has eigenvalues e^(±ζ), conjugate to a squeeze), not its largest stretch (checked 10 Nov: at α = 0.3, c = 2 the largest stretch is 0.220 against ζ = 0.209; at α = 0.7, c = 5, 1.22 against 1.10)
- [ ] the tower and two thumbs: top (¼, ⅓), foot (0, ⅓); a step across: 1/12, 12 thumbs, 3 tall, 4 aside; epipolar check; a step forward (3/11, 4/11)

**Numbers**
- [ ] rates: the running rates 1.1107 and 0.9003 at the corner; θ/sin θ to π/2, sin θ/θ to 2/π, product 1; III.20
- [ ] tangent addition (a + b)/(1 − ab); two 1's: 1, 2, √2, Hölder ‖x‖₂² ≤ ‖x‖₁‖x‖∞
- [ ] bisecting a direction (√(1 + s²) − 1)/s; ∛2 beyond (Wantzel 1837)
- [ ] Madhava–Gregory–Leibniz; Machin: 1/5 four times is 120/119, less 1/239 by tangent subtraction is 1; Viète
- [ ] ln 2 = 1 − 1/2 + 1/3 − …; Bernoulli (1 + 1/n)ⁿ
- [ ] (1 + iθ/n)ⁿ: short by θ − n·arctan(θ/n) ≈ θ³/(3n²), length (1 + θ²/n²)^(n/2) ≈ θ²/(2n); a thousand reads of π/1000 at −1.005; −w²/(2n); Lie–Trotter (θ₁θ₂/2)·sin(φ/2)/(φ/2) (Trotter 1959)
- [ ] Cayley: w = (1 − s² + 2is)/(1 + s²), |w| = 1; (1/2i)·d(ln w)/ds = 1/(1 + s²); iπ gathered, ∫ = π/2; whole line π; (1 + ia)(1 + ib) = (1 − ab) + i(a + b) (Cayley 1846)
- [ ] one pole: e^(izt) = e^(imt − γt), t < 0 round z̄, e^(imt − γ|t|); total 1 normalized, π unnormalized; checked to 25 digits at z = 0.7 + 0.4i, t = 1.3; Student t₃ (1 + t)·e^(−t), two poles beat, sech's series, Gaussian and Laplace none (OPL)
- [ ] Lindemann 1882

**Data**
- [ ] LIGO: 512 s, ~2·10⁶ whitened samples each; block means n^(−½); [H1 : L1] median 1, angle near uniform, departure reproduced 8 s apart to 0.0001, predicted first (Abbott et al. 2023)
- [ ] quasar dipole: [2 + x(1 + α)]·β, 5.3–6.6 β, payload 60–70%; 0.018–0.023; one β 3.3·10⁻³ ± 0.3·10⁻³, 2.7× the CMB's; colour slices 2.3, 2.8, 4.6 (Ellis and Baldwin 1984; Secrest et al. 2021)
- [ ] double slit: 2hv bound, |h² − v²|; counts 9,026 : 10,465 and 11,993 : 11,891, 2hv 0.997 and 1.000; contrast 0.69 and 0.56 (Greenberger and Yasin 1988; Englert 1996; Aspden, Padgett and Spalding 2016)
- [ ] Berry's phase half the solid angle (Berry 1984; Tomita and Chiao 1986; Bitter and Dubbers 1987)
- [ ] seeds: Clark's 2Dt p = ½, r⁻³; 35 of 38 fitted, median p 0.10, tail ≈ r⁻² (Bullock et al. 2017)

**References.** Every reference in the record stays unless its passage is dropped; none is added unless Tom asks or a
referee names one (R562).

## 6. Open points, to settle before or during step 3

- **O1. The name "place".** Working name for the middle kind. Alternatives: "a place in thumbs", "a relation", "a
  ratio of distances". Tom's call.
- **O2. The thumb's status.** Under R788 the thumb scales with the world (the reader's body is in it), so every
  distance in thumbs is a place and H is the across axis's chosen zero, not a mark. R653 said the thumb "is not a mark, it
  is the read's own length". Proposed: keep R653's point (no read carries a scale) and state H as the across axis's zero
  chosen by the reader, as home is the up axis's.
- **O3. "The writer" as a vantage.** Proposed: the writer is who holds the across zero tied to a unit (so every amount),
  and both hemispheres. A reader who has walked and counted holds places, not writes, until it agrees a unit. Check that
  this fits R594 ("in doing it is writing") once restated: it becomes "in doing it is placing; with the unit, writing".
- **O4. Order of reads.** R652 made the order a write. Under R788 it is a place-like thing: unmoved by scaling, not in
  one read. Proposed: an order is a joining of reads, like a place, and is named as such in definition 7.
- **O5. Physics.** The record's "a read is geometry, a write is physics" becomes: reads and places are geometry; physics
  enters with the unit (R230: "a unit injects physics into the relation"). The sheet-of-paper picture to be restated so
  marks without units are places.
- **O6. The essays and demos.** They use the record's vocabulary. Not touched in this rewrite; a later pass, once the new
  paper stands (as R459 followed the new OFS).
- **O7. *Reads and Writes in Physics*.** Drawn from the record; it waits for the new paper, then a pass.
