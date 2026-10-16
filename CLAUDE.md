# wander: notes for Claude

A world of solids you fly through, with a "lab" of experiments comparing what a
reader can recover from arriving signals against known physics. Two pages and the
world they share, served by GitHub Pages at https://reportbase.github.io/wander/. The owner works through
Claude Code: changes go on a branch, as a PR, and the owner merges. Merging to
`main` publishes.

## Files
Since 6 Oct 2026 (Tom's choice) the site is three files, no build step. Since 13 Oct things may load from outside (Tom:
"things can be loaded from outside"): Google Fonts, and three.js from the jsDelivr CDN for `sphere-cube.html`:
- `world.js`: **Wander's world, shared by both pages**: the constants, the solids,
  the systems and their ticks (`tickSystem`), the signals' speed and arrival
  pieces, the readout's distance step, and the reading functions the live readout
  shares with the labs (`plxTwoPart`, `twoAt`, …). A classic script whose top-level
  names both pages' scripts see (that is how both can assign `starsNow`). Moved
  out of the old single page line for line. **A change here changes the labs'
  world: run every lab after it.** Since 9 Oct it also holds brightness (`lightAt`, L·A/(4πd²), the
  inverse square), read only by LAD's third run (the standard-candle rung past the resolution limit).
- `index.html`: the flying page (the world drawn, the controls, the readout, the
  live-view test hooks). Its "lab" button opens `labs.html` and its "demos" button `demos.html`; `?lab=CODE` and
  `?lab=all` forward there; `?lab=0` hides the button.
- `labs.html`: **the lab, and the file to edit for any lab.** The explainer and a
  card per lab on top; then THE LAB BUDGET comment, the lab notes (`#labPane`,
  hidden, the cards are built from it), and the script with THE LAB GUIDE and every
  lab's code. `?lab=all` / `?lab=CODE` run outright and show the full report (the
  smoke test reads it); `?run=…` does the same on the cards.
- `res/`: the suns, planets and moons, as `.tvf3d` fields (the 3d studio's and the games
  page's format: radius and colour as series in cos(nπh) and cos/sin(mθ)), written by
  `node res/make-bodies.mjs` (seeded, so it writes the same files; add a body there and
  list it in `BODY_FILES` in `index.html`). The flying page fetches them in the background
  (`fieldGrid` folds each onto the solids' grid) and dresses each system's star as a sun, its
  planets, moons and belt, chosen by the body's key; they are lit by their own star
  (`lightOf`, the 8th vec4 of a body's record), and suns give light. Each body's radius is held as
  its ball plus relief in three bands (broad, middle, fine, by max(n, m); `fieldGrid`), and
  the shaders add each band only once its features cover a few pixels (`bandW`): far off a
  body is a plain ball, close up its craters and mountains show. Looks only: motion,
  reading and the labs are unchanged, and `world.js` is not touched. Until they load, plain balls.
- `sweep.html`: **the sweep device** (7 Oct 2026), a standalone page outside the world
  and the labs: an array of pairs of amounts, each divided by its own second amount, laid on the unit sweep
  g = (2/π)·atan(v/h) and read by a cursor, serially (4) or all at once (3), with the
  quarter circle (divided by the whole) beside it. `?ex=planets|shape|spread|line`,
  `?mode=parallel`. Not linked from index.html yet.
- `dial.html`: **the H dial** (7 Oct 2026), a standalone page like `sweep.html`: GRN runs 3–5
  (`plans/grn-plan.md`) on one screen. A model-free reader with pixels H wide reads two points one apart;
  turn the dial, look, slide h, approach from afar; charts of P("two") = min(s, 1) and of the cost of a sure
  "two", (1 + s)·max(1, 1/s), least at one pixel across (GRN's "corner", s = 1, is the resolution limit). `?s=` sets the dial; test hook `window.__dial`.
- `sphere.html`: **the sphere** (7 Oct 2026), a standalone page like `dial.html`: `number-line.md` §8 on one screen.
  Three unit relations and a scale k; the address on the octant (k changes nothing there); six chambers and the triple corner;
  the unit cube's faces; near and far for a reader holding H; a body with relief in three bands shown by its size in
  pixels (as `bandW`). `?v=&h=&f=&k=&P=&map=chambers|faces|reader|whole`; test hook `window.__sphere`.
- `facing.html`: **the facing** (9 Oct 2026, after SPN §1, "The line, the arc and the facing"; Tom: "a line does not account
  for a second degree of freedom"), a standalone page like `dial.html`. One sweep from A to B in unit relations: the facing
  2θ turns from toward B through square to the line (the corner, θ = 45°) to toward A; beside it the quarter arc off the
  line h + v = 1, most (1 − 1/√2) at the corner. `?t=` (θ in degrees); test hook `window.__facing`.
- `levels.html`: **the levels** (9 Oct 2026, Tom: "a demo that shows the circle in the middle of the page and the logritmic
  circles that halve outside the circle … until they can't be seen anymore"), a standalone page like `facing.html`. The unit
  circle holds the near field in proportion (radius s); past it each ring is one doubling of s, half as wide as the last
  (radius 2 − 1/s, the in-place lay), toward the horizon at radius 2. A ring narrower than one grain is not drawn (the
  resolution limit), so about log₂(R ÷ grain) show. A perturbed circle (Tom: "a pertibated circle that wrapped the circle that crossed the various
  levels") wraps it, s(θ) = s₀·exp(Σ aₙ cos(nθ + φₙ)), and the reader's level of detail is a circle at s = 2^k (Tom: "another
  circle the represents the LOD of the user"): inside it the shape keeps every bump, past it only its broad form (n ≤ 3).
  "Divide out the size" (10 Oct, Tom: "the corner is v = h … which is also the baseline from which depth is calcualted")
  moves the shape's middle onto the corner's circle and shades the depth, log₂ s(θ) levels, outward and inward.
  A combo box picks the shape (10 Oct, Tom: "add the ablity load a tvf file. add a combo box let the user select the shape"):
  the built-in one, a body in res/, or a file from disk: a .tvf curve (the draw tool's format, draw.html `parseTvfText`; read from
  its centroid, the nearest wall in each direction) or a .tvf3d cut at a height h (the equator by default); the outline
  read as s(θ) = s₀·(r/r̄)^k with a relief slider k. Since 11 Oct (SPN Prop 1.2 (g); Tom: "update levels.html") the default is
  the reader's lay, 1 + ln s past the corner, every level ln 2 wide, six drawn, no horizon on the lay; the in-place lay
  (2 − 1/s, horizon at 2) is kept at `?lay=inplace`: the same addresses by length, reality in 2H (Tom: "reality = 2H";
  "same length, not addresses"). "Depth" relabelled per R188.
  `?lay=inplace&g=&s=&shape=&lod=&depth=1&body=&relief=&cut=`; test hook `window.__levels` (now with `lay`).
- `walk.html`: **the walk** (10 Oct 2026, Tom: "the sweep is a walk from me to you … far away, you are increasinly difficult
  for me to get to you, and then acceleratingly difficult"; "You are vertical and I am horizontal. Show the sweep in terms of
  the horizontal's walk to the vertical"), a standalone page like `facing.html`. Me on the ground (breadth H, one step), you a
  vertical of height V = 10 steps, at distance d; the pair (V, d) is the bridge, s = V/d, v = min(1, s), h = min(1, 1/s). The
  sweep's angle is the angle I look up at your top, θ = atan(V/d): 0° on my horizon, 45° at d = V, 90° at your foot. Steps
  left V·h/v = V·cot θ; far, each level costs twice the next one in, the steps bunching toward the horizon (never reached);
  near, in proportion. Panels: the ground, the sweep in unit relations, steps left against θ. `?d=&walk=1`; hook `window.__walk`.
- `mountain.html`: **the mountain and the thumb** (11 Oct 2026, Tom: "build a demo about the worked example"), a standalone
  page like `walk.html`: OFS §10 on one screen, H the thumb and V the mountain (SPN R205). Thumb H = 1 mi, a range V = 20 mi
  wide at d = 10 mi. From nowhere, the blueprint from above; from the reader, 36 fingers spread evenly over the half turn,
  the corners at ±45° (the range's ends, the pair (V/2, d) at its corner), the ridge's elevation the ring on each finger
  that reaches it; "scale the world" (k multiplies V, d and the ridge) moves the blueprint and nothing in the reader's
  view (OFS Theorem 6, Proposition 8); mountain equals thumb on the reader's lay of distances (x, then 1 + ln x), read at
  0.5 H against the true 10 H, off by V/H = 20, 4.32 doublings; "walk one thumb" recovers d = H·s₂/(s₂ − s₁) and V.
  The two vantages (13 Oct, SPN R223; OFS §10 step 3): on the thumb's circle the outer reads π/2, the inner the fingers'
  mean shadow 2/π, product 1, H in H, the starting value returned (R226; it said "the thumb's true breadth"); to the
  ends 1.1107 × 0.9003 = 1; the mountain never enters.
  `?V=&d=&k=&walk=1`; hook `window.__mountain` (`reading`, `equalsThumb`, `walk`, `vantages`, `lay`, `set`).
- `zoom.html`: **H is a zoom** (12 Oct 2026, Tom: "create a demo that shows what the implications of setting H for near
  and far field zoom and LOD"), a standalone page like `mountain.html`: OFS §8 ("The count is the level of detail", "H is
  a zoom, not an escape") on one screen. Amounts x read against H as s = x/H (V = H); the lay s to the corner, then the
  reader's 1 + ln s (L levels) or the in-place 2 − 1/s (`lay=inplace`, the horizon's last address taking all s ≥ n);
  the level of detail n addresses across the near field, ε = 1/n, equal room everywhere. Panels: sizes from nowhere with
  the held window [H/n, H·2^L] (or [H/n, H·n]), its width in levels the same at every H; the lay address by address
  (things sharing an address not told apart; home; past the edge or at the horizon); addresses per level (n·2^k inward,
  n·ln 2 a level past the corner, or n·2^-(k+1) mirrored); detail across sizes (εH absolute inside the corner, εx or
  εx²/H past it). Worlds: nested clusters at every decade, the numbers 1–100, 200 scattered sizes; click a size to put it
  at the corner. `?H=&n=&L=&lay=inplace&world=even|scatter`; hook `window.__zoom` (`lay`, `addr`, `held`, `perLevel`,
  `detail`, `read`, `set`). Not in the flying page.
- `parallax.html`: **parallax from the corner** (12 Oct 2026, Tom: "show how parallax and situated observation are both needed. explore parallax from the perspecive of the corner."), a standalone page like
  `zoom.html`, PXC on one screen. Two standpoints A and B a baseline apart, each reading directions only; the plane laid
  as the reader lays it (by direction from the middle, distance in half-baselines, in proportion inside the corner circle
  and 1 + ln past it, H at the half-baseline), so parallax's corner, the Thales circle, is the reader's corner circle.
  Each target triangulated thirty times with directions off by the step ε: held (teal), stretched (gold), lost to a ray
  past the band's far edge (red). Modes: A alone or B alone (rays from the standpoint, no distance), both with the
  baseline. The bell: ε·cosh of the levels and the error's stretch d/(B/2), round at the corner. Presets for scale (two
  eyes; Earth's orbit with Hipparcos's 1 mas or Gaia's 20 µas, precisions of p = γ/2, so the step in γ is twice that:
  the band ends near 1 kpc and 50 kpc; corrected 12 Oct). `?mode=A|B|both&preset=eyes|hipparcos|gaia&eps=`; hook
  `window.__parallax` (`relErr`, `aspect`, `band`, `farEdge`, `triangulate`, `counts`, `set`). Not in the flying page.
- `sphere-cube.html`: **the sphere in the cube** (13 Oct 2026, Tom: "if we put a rotatable sphere inside the unit cube, we
  could show that every point on the sphere maps to every point on the inner cube. the inner cube could be any size,
  however its extent must be known"; "create a high quality 3d three.js full screen demo to explain the situation"; SPN
  R220, R221; WDG), full screen. three.js 0.160.0 (MIT) loads from jsDelivr, pinned, through an import map (Tom, 13 Oct:
  "remove three.js from the repositiory, use the cdn"; it was vendored for a day); the smoke test serves the same version
  from `node_modules` (the devDependency `three`, exact), since this environment's proxy blocks the CDNs, and the page says
  so if the CDN cannot be reached. The unit cube (h → x, v → y, v₂ → z, every party drawn at
  H), a sphere free to turn (drag it; tap it to choose the point followed; drag elsewhere to look; arrow keys), 1,500
  even points on it (a Fibonacci lattice) coloured by the face they land on, their rays to an inner cube of half-extent e
  (`e·d/‖d‖∞`, the face of the largest component), and the point inside at t, a unit relation. Six steps: the unit cube;
  the sphere; every point points; any size (e animates, the address unchanged, the amount e times it); the extent
  unknown (drawn at H, off by e/H); the wedge (h, v, v₂ ≥ 0, its three faces a third each). An inset draws the face hit
  as a reading plane with the Cauchy shading and its middle quarter's share (38%). Step 7 (14 Oct, SPN R237, AZM; Tom: "ok,
  proceed"): the two sweeps, the hand raised in altitude (H to V, teal) and turned in azimuth (V₂, violet) with their
  sectors, each sweep's corner (the cone a = 45°, the half-plane v₂ = h), the flat triangle h + v + v₂ = 1 (no sweep),
  1,600 points of the wedge swept evenly in both angles or over the wedge (height even), coloured by the largest of h, v,
  v₂, and an inset of Lambert's equal-area map (z, v); on the triangle (R238) the reader's drawing V = V₂ = H at its
  centre (⅓, ⅓, ⅓) and a true point (1, V*/H, V₂*/H)/sum beside it (`?vs=&v2s=`, 3 and ½ by default).
  `?step=1..7&e=&known=0&t=&wedge=1&rays=0&turn=1&alt=&az=&even=angles|area&vs=&v2s=`;
  hook `window.__sphereCube` (`address`, `point`, `faceOf`, `stats`, `turnBy`, `hud`, `set`, `state`, `frames`, `webgl`,
  `sweeps`: `direction`, `readings`, `exact`, `counted`, `topShare`, `lambert`, `truth`, `centre`).
  Not in the flying page.
- `wedge.html`: **the wedge** (14 Oct 2026, Tom: "this suggests a new UI paradigm, not a sphere, but a 3d wedge.", then
  "yes, proceed on wedge.html"; SPN R240), full screen, three.js like `sphere-cube.html` (the same pinned CDN version and
  test route). The reader's own space: every [h, v, v₂] a point of the unit cube, its directions one octant; a relation is
  never negative, so a sphere's other seven octants are only this wedge faced another way. Two looks: from outside
  (orbit), the three faces with the levels on them, the corner (s = 1, radius H) and the held edge; from home (the apex,
  looking down (1, 1, 1) through a flat screen), the wedge is the triangle h + v + v₂ = 1, each direction at its shares
  (a central projection; classical, Claude's note in R240), each pair's corner a median, the six chambers its small
  triangles. The hand by altitude and azimuth (drag from home, tap a thing, or tap the inset, Lambert's equal-area map
  with the corner curves and chambers). A world (280 things even over the wedge, d over five decades, or a cluster per
  decade) laid along the rays, s to the corner then 1 + ln s (or 2 − 1/s, `lay=inplace`), n = 32 addresses across the near
  field: nearer than H/32 merged into home, past H·2⁶ (or s ≥ 32) past the held edge; H slides things along their rays,
  never across; from home each thing as wide as it looks (Δ/d). The situations per party (known, 3 at once, 4 stepped):
  a camera, a fan-beam radar (3, 4), a line scanner (4, 3), a single-pixel scanner (4, 4), the seen fading behind the
  beam; a known breadth moves the drawing (1, V/H, V₂/H)/sum from the centre toward the truth. Seven steps: the wedge,
  from home, two sweeps, a world, H is a zoom, the situations, and (14 Oct, Tom: "show how the wedge could be positioned
  anywhere on the sphere, so there is two steps, position the wedge,then sweep it."; SPN R242) position, then sweep: the
  sphere with its three great circles; the wedge (everything of it, in one group) placed by a rotation R, set by where its
  triple corner points (longitude, latitude) and a turn about that, or on an octant (a turn of the first, two parties
  swapped where the signs would make a reflection), or anywhere (an even turn); then the hand sweeps in the wedge's own
  frame, on the sphere R·d; "position, then sweep" plays a turn and then the sweep; from home the camera turns with R, so
  the wedge looks the same and only the sphere's lines move. Leaving step 7 puts the wedge back in its first place.
  `?step=1..7&view=home|outside&H=<log10 H>&lay=inplace&world=scatter|decades|none&V=known|3|4&V2=known|3|4&alt=&az=&vs=&v2s=&rays=0&seed=&lon=&lat=&roll=`;
  hook `window.__wedge` (`homeProject`, `homeShares`, `shares`, `chamberShares`, `cornerHalf`, `placeAt`, `counts`,
  `coverage`, `drawingOf`, `situationName`, `set` (with `pos`: lon/lat/roll, `octant` or `q`), `state`, `hud`, and
  `position`: `quat`, `of`, `octant`, `octahedral`, `random`, `imageOctant`, `inWedge`, `world`, `handTip`, `homeNdc`).
  Not in the flying page.
- `wedge-browse.html`: **browsing the wedge** (14 Oct 2026, Tom: "the cool thing is we can attach array of data to this";
  "if the data is massive, than a fisheye dual control UI was explored, we should pull that forward. the situated view is
  typically over huge data"; "yes" to one thumb for both sweeps; SPN R241), a standalone page, plain canvas, no libraries.
  The calendar project's navigation dial (reportbase/calendar `city-dial.html`: a gold thumb that is a rate, a blue needle
  that is a place, the radius a window, a tap changing nothing) carried to the wedge. Data: 2⁵³ − 1 items made from their
  addresses, never stored: a binomial cascade on λ ∈ [−32, 32)² (λ the two log-ratios X₂/X₁ = 2^λ₁, X₃/X₁ = 2^λ₂), 60
  halvings, λ₁ and λ₂ in turn, one half getting m or 1 − m of the count (m from a hash in [0.5, 0.68]), counts exact;
  an item found by its index (descend by counts), placed by a hash in its finest cell, its total from a smooth field
  plus a jitter. View from home (the triangle, h ↙ v ↑ v₂ ↘): displayed reading = (true reading over the drawing)^(1/w),
  the drawing V = 2^μ₁·H, V₂ = 2^μ₂·H; at w = 1 the wedge itself; three pencils of rungs through the vertices, the
  medians the corners. LOD: cells opened largest-on-screen first (their image's area), to 7,000; cells of ≤ 16 items
  opened into their items; the rest drawn as totals coloured by density; the drawn always add to 2⁵³ − 1 exactly; cells
  at the finest address still holding many share it. Needles: press and pan, the gold (from the centre to the finger,
  tan in the screen's own units) adds rapidity at 0.4·tan a second; the blue sits at sinh of it inside the triangle;
  letting go re-centres (μ ← λ of the blue). Wheel: w, keeping the blue's place (or moving the window to it when it
  must); shift+wheel: H (colours only; from home nothing moves). Inset: the totals' sweep at the hand (a sample at
  atan(T/H)). A go-to box puts an item by index at the triple corner, its total at the corner.
  `?w=<log2 w>&H=<log2 H>&mu=μ₁,μ₂&seed=&i=`; hook `window.__browse` (`children`, `itemAt`, `cellAt`, `dispShares`,
  `trueShares`, `hold`, `release`, `placeBlue`, `set`, `goTo`, `under`, `screen`, `drawn`, `view`, `hud`). Not in the flying page.
- `paths.html`: **one sweep, three paths** (13 Oct 2026, Tom: "yes, proceed", to the visual from the ChatGPT exchange in
  `plans/ofs-review-6.md`; SPN R224), a standalone page like `facing.html`. Geometry only, in unit relations. The circle,
  the line h + v = 1 and the square's edges, each swept evenly along its own length; the reading v/h is the direction
  alone, the same on all three; b, the share of the sweep done at θ (2θ/π, tan θ/(1 + tan θ), tan θ/2 then
  1 − cot θ/2), agrees at home, the corner and the horizon and parts in between. Panels: the three paths with the chosen
  one cut into 24 equal lengths and their directions; b against θ, with the circle weighted by sin² 2θ dashed; the turn
  and its shadow on the circle (outer θ/sin θ, inner sin θ/θ, π/2 and 2/π at the horizon); the mean taking readings up to
  S, climbing ρ(0)·ln 10 a tenfold on each path, settling at 4/π for sin² 2θ. `?path=circle|line|square&t=`; hook
  `window.__paths` (`b`, `measure` (b along the path as chords, not the closed form), `bWeighted`, `tmean`,
  `tmeanWeighted`, `perDecade`, `vantages`, `hud`, `set`). Not in the flying page.
- `h-limits.html`: **what is H?** (13 Oct 2026, Tom: "explore what H acutally is. what is H of 0. what is H of infinity.
  Picking an H creates the unit relational space"; HKO; SPN R228), a standalone page like `zoom.html`. A world of 31
  amounts (10⁻³ … 10³) placed by H on the quarter turn (arctan(x/H)); three rulers (the number line, the reader's lay at
  H, the logarithm, or the reciprocal for the in-place lay), the middle one becoming the top at H past the world and the
  bottom below it, a corner only with H inside; the addresses a finite count holds for every H, the world lost whole
  into home, past the held edge or into the horizon; the angle between two tapped amounts against H, widest at their
  geometric mean. A fifth panel (13 Oct, SPN R229; Tom: "larger H moves the corner further away from the observer, which
  gives more proportional space. reader has fixed number of addresses, so more proportional space means each object is
  given less level of detail"): one object (the amount tapped last, a hundredth, a tenth or all of its distance across)
  and its detail in levels against H on both lays, nΔ/H inside the corner, flat past it on the reader's lay, most at
  √(x(x + Δ)) on the in-place lay. "Unlimited addresses and levels" (`?n=inf`; R230): every amount held apart at
  every H, the value of H idle, so a unit is needed because addresses are finite.
  `?h=<log10 H, 0, inf>&lay=inplace&n=8|32|128|inf&pair=i,j`; hook `window.__hlimits`
  (`normLay`, `deviation`, `held`, `thresholds`, `pairAngle`, `bestPair`, `objectSpan`, `objectPeak`, `hud`, `set`).
  Not in the flying page.
- `h-chain.html`: **the chain from H** (13 Oct 2026, Tom: "lets build stand alone demos of H kicks of the entire chain of
  logic … we sweep the cauchy fisheye of it. the shape is constructed virtually, over many observations, which implies
  that it might have something to do with parallax"; SPN R228; after draw's labs rcc and udv), six steps with one H:
  pick an H (the unit relational space, the same at every H; a world placed by it); the number of V's sets the shape
  (circle, sphere, a table to five); one observation sweeps the Cauchy fisheye of one facing (a reader at a figure's
  centre, v/h = tan a, the census given back as the unit circle for every figure and size); facings joined over
  observations; standpoints a baseline 2H apart (or three, the pair crossing squarest, as udv) build the figure, the
  Thales circle the corner circle, H of 0 rays, H of ∞ the baseline, best H √(d_near·d_far); physics assigns the value
  and nothing moves. `?step=1..6&h=&n=&fig=circle|egg|star|astroid&eps=0.1|0.5|2&sp=1|2|3&unit=mi|km|au`; hook
  `window.__hchain` (`fisheye`, `triangulate`, `bestH`, `figurePoints`, `hud`, `set`). Not in the flying page.
- `pool.html`: **pool from inside** (10 Oct 2026, Tom, sharing "Pool from Somewhere", an app from an earlier session: "each pool
  ball can explore its situation"; "Ours is most situated math, and could be all situated math"), a standalone page. Two tables,
  one rack, one strike: the referee (unsituated, world positions, d < r_a + r_b) and the table played from inside: each ball
  reads each other's direction and v = r_b/d, is told the other's reading h = r_a/d, touches at h + v = 1 (the line of
  `facing.html`; equal balls at the corner, 60° across), and works in its own size (size ratio v/h, masses (v/h)³, one
  material). Run 2: cushions read as the ball's own mirror image (v = r/(2·gap) = h, contact at the corner), pockets
  entered when they fill the view (v > 1); only one integrator and the clock unsituated, named; `?cushions=referee`. Run 3:
  a "signals" select reads the others late (c = 50), the late image taken as now or carried forward (`runLate`). Runs 5–6:
  a "table" select (the rack, or a field of four size levels, `rackField`) and an "ignore" select (`runField`). Panels: the table, the chosen ball's pairs as (h, v), its
  view round the turn. `?break=0..9&heavy=0`; hook `window.__pool` (`run(i, opts)`, the POL measures).
- `pool-infinite.html`: **the infinite table** (11 Oct 2026, Tom: "we could scale it up to infinite number of balls, but then
  zoom in to just see a small percentage of them, and only have to draw or calcualate the visible balls"; "yes"), a
  standalone page and POL runs 11–15's engine. A gas of hard discs (no cloth, e = 1, φ = 0.15, σ = 5) in a world 2^30 cells
  of 7.5 a side (10^19 balls): a window of balls round the reader (exact contact from inside, run 9), totals (N, P, E) in
  world-fixed dyadic cells beyond, each held at the level where it reads at the corner from the reader (a dozen a level);
  moving or zooming folds and unfolds cells exactly (seeded by place). The window's edge (what runs 11–15 found it needs): a
  mirror, and a band 2 deep held at the ring of cells' chemical potential (grand-canonical keeping at the activity from
  Henderson's equation of state, Γ = 1/s), its books charged to the ring, the mirror's pushes to the far field. The window
  follows the view while a ball is 6 px or more, then stays; zoomed out the cells show by level. Modes by `opts.mode`:
  edge (run 11), band (12), mirror (13), gc (14), ring (15, the page's); `opts.far` diffusion (the page's) | fluid | fluidwall
  (runs 16–18). `?zoom=&cells=0`; hook `window.__infinite`.
- `thin.html`, `ladder.html`, `sky.html`: **the physics correspondence** (9 Oct 2026, Tom: "create multiple demos that
  explain the physics correspndance"), standalone pages like `dial.html`. `thin.html`: the same signal, a smaller share
  (the inverse square; near, distance costs grains, far, light; the switch at one grain is the resolution limit;
  `?v=`, hook `window.__thin`). `ladder.html`: parallax, width and light, each giving out at its own limit (LAD;
  `?D=&photons=1`, hook `window.__ladder`). `sky.html`: Olbers' dark sky, the lit share 1 − e^(−L/λ) and every shell
  giving the same light (OLB; `?L=&always=1`, hook `window.__sky`).
- `play-points.html`, `play-resolve.html`, `play-ladder.html`, `play-sky.html`: **gameplay sketches** (9 Oct 2026, Tom:
  "explore game play possibilites in demos, each demo should focus on a narrow features. so they can be explored and
  iterated seperately"). Standalone, one mechanic each, nothing shared, so each can change alone: far bodies under a pixel
  (dim by 1/d², vanish, or a full-bright pixel; hook `__points`); events on approach (point, resolved, shape, terrain,
  surface; `__resolve`); distances earned rung by rung (parallax, then width and light per kind; `__navigator`); the sky
  filling as light arrives, the count a clock (`__skyfill`). `play-corner.html` (10 Oct, Tom: "situated is much better at
  certain things"): aiming a cut from the cue ball's view in the red's own size; f half-spans off its middle gives
  sin φ = f/2 at any distance (half-ball 30°, graze 90°: the ghost ball, h + v = 1; `__corner`). `play-trick.html` (10 Oct,
  Tom: "a fullscreen html canvas game … shows how that angle will propogate out, hitting all the other balls"): trick shots,
  full screen; the whole shot simulated ahead (pool.html's from-inside table, cloth MU 1.2) and drawn as paths, contacts
  and pots, then played from the same frames; drag any ball, undo; `?layout=rack|scatter|line&a=&p=&paths=&see=`; `__trick`.
  Contact is exact (POL run 9: each ball finds the moment h + v = 1 in its own units); "see" is the preview's horizon,
  each ball's motion shown while at most k contacts from the cue (3 by default, POL runs 8–9), a "?" past it.
  Two angles, as in pool (11 Oct, Tom: "you hit the white ball first … where you want to hit the white ball, and where you
  want the white ball to hit the first ball"): the cue's tip is a small ball (R_TIP 0.1) meeting the white on h + v = 1;
  where it meets the white is chosen on its face (the round inset, the white seen from behind the cue, in its own size).
  Spin (11 Oct, Tom: "lets see how far we can push it"): each ball carries its spin; it slips over the cloth (grip MU_S)
  until it rolls, then only the drag MU acts; a chalked tip grips inside tan φ ≤ 0.6 (the white on the cue's line, the
  off-centre push becoming spin: corners are draw/follow with side), past it a miscue; a bare tip turns the white
  sin φ = fx, no spin; side spin grips the rails. `spinChecks` reproduces the textbook results (rolls at once 2/5 up, a
  rolling white follows at 2/7 after a full hit, a stun stops, draw comes back, right English comes off the rail right).
  Throw, spin passed on, massé and jump (11 Oct, Tom: "push further on the three suggestions"): balls grip each other
  weakly (since CUE run 2, the published fit to measured throw, `gripOf`: 0.095 slow to 0.03 fast; it was MU_B 0.06): a
  cut throws the struck ball 1–5° toward the white's travel (more slow), side spin ~3° the other way, and passes
  opposite side spin; the cue can be raised (`cue ↑`, `?el=`): a tilted spin axis bends the path (massé), the press into
  the slate throws the white up (jump); off the cloth a ball falls (G) and bounces (E_TABLE), and contacts read h + v
  with the height included, so it can pass over a ball. Layouts `jump` (over the 1 to pot the 2) and `masse`.
  The grip acts on the whole slide, upright too (a rolling white passes backspin and follows by less than 2/7; the
  textbook checks run with it off); a ball in the air above the cushion's nose (1.27 R) flies off the table and is
  respotted. Tried and taken out: the cloth's grip during the slate press (at 0.195 it kinked massés instead of curving).
  Power 2–60; `?tip=fx,fy&chalk=0&el=`; hook `strikeOf`, `tip`, `chalk`, `elev`, `spinChecks`.
  Challenges (11 Oct, Tom: "yes", to a challenges mode): fifteen puzzles in the layout menu, one mechanic each (½-ball,
  bank, kick, jump, massé, a blind thin cut, stun, draw, follow, two rails, cannon, combination, the throw, the row of
  four, the break; two rails and the throw added with play and feel, Tom: "1,3": the throw is a frozen pair 8° off the
  pocket that only a slow hit grips in, power 10–17 on this engine, almost none with the grip off). Each
  fixes "see" (0 shows only the white to the ghost ball; the later ones put the pot past sight); balls can't be moved; a
  missed try puts them back and says why; par from the window of aim around a reference shot (`sol`, found by search on
  this engine). Best per challenge in localStorage only. `?challenge=<id>`; hook `challenges`, `setChallenge`, `trial`,
  `solve`, `check`, `challenge`. A challenge's layout or the engine changing can break its reference shot: the smoke test
  plays every one. Play and feel (11 Oct, Tom: "1,3"): sound made in the page (the cue's tap, ball on ball, the cushion,
  the pocket, each as loud as its impact, played as the shot's own frames reach it; `sound: on/off`, kept in
  localStorage); a strip at the side to pull down and let go (power by the pull; let go near the top and nothing is
  shot); controls a finger can hit on touch screens. Hooks `heard`, `sound`, `playing`, `grip` (a number, or null for the
  fit).
  Not in the flying page.
- `play-marbles.html`: **a bowl of marbles** (12 Oct 2026, Tom: "a huge collection of marbles, say 500? would this be
  helpful?", then "both", a physics test and a game). A gameplay sketch, standalone, and MRB part 2's engine (`MARBLES`,
  driven by `plans/mrb/run3.mjs` through the hook): soft spheres that stay touching, each pair in contact while its
  readings are past h + v = 1, pushed by the depth past the line, with a tangential spring of its own history capped by
  friction (Cundall and Strack); containers a floor, square walls, periodic sides or a bowl (a sphere's cap on a table).
  The game: 500 glass marbles poured into a shallow bowl (Rb 16, 2.5 deep, heaped above the rim); tap where to throw a
  steelie (mass 6), how hard (slider, or the pull strip); the dashed arc is the throw seen ahead to its first contact;
  ten throws, marbles landing on the felt count; "chains" draws each contact as bright as its push; sound made in the page
  (glass, bowl, felt, the loudest few a frame). Softer contacts than the lab's (k 3000 against 10⁵), stepped only while
  something moves, as many steps a frame as fit (slow motion on a slow device, the same throw). Best per marble count in
  localStorage. `?n=&seed=&p=&chains=1` (and `?Rb=&depth=&steel=&vmax=`); hook `window.__marbles` (`world`, `game`,
  `throwAt`, `arcOf`, `settleNow`, `chains`, `sound`, `heard`). Not in the flying page.
- `flight.html`: **the corner in flight** (10 Oct 2026, Tom: "you know how the transition from earth to the sky in flight
  sim games is awkward? ... i wonder if its because of the corner"; "only the geometry", wireframe). Level flight at height v;
  a ground line h ahead lands v/h below eye level, so the corner (h = v) keeps one screen row at every height. The main view is the grid alone (Tom: "remove the non-gridlines";
  the corner and level edges are on the strip) plus a few posts recovered from the sweep (Tom: "remove the pertibuated circle, focus on recovering the universe with a
  sweep"; "a circle is not needed. only the sweep is needed"; after draw's UDV lab, one reader moving instead of three
  standing): each post's foot and top read as (across, down) against the distance ahead, to a pixel; the readings from one
  v of travel back cross with today's at the place, the travel the one length, so places in v; same pixel twice leaves a
  bearing. The lay at bottom left (Tom: "the corner is the unit circle itself, by setting V = H"; "that unit circle contains
  the address space to the entire universe"; "think of the corner circle expanding logrithmically, but reality itself does
  not"; "it will look like the mercator map"): the ground laid on the addresses around home, radius ρ/v inside the corner
  circle (radius H), 1 + ln(ρ/v) past it, each doubling ln 2 wide; posts true (white), recovered (teal), bearings (rays). Placing gives out near
  h = √f·v (the step: physics, not the corner). Strip:
  the reading folded at the corner, h/v to home (even), v/h past it (2v, 4v … each half the room). LOD (`?lod=`; the chips removed, Tom: "remove the buttons in the upper left"): none / by metres
  (doubling at 500 m, 1 km …) / by v/h (levels split at v, 2v, 4v …, grain v/8 in the first two then doubling, 8 lines a level, so the count past the
  corner is log₂(h/v) and climbing changes nothing on the screen). One corner only (Tom, 10 Oct, superseding "each Level has
  its own corner": "there is only one corner that splits far field from the near field, which is just the split between the
  first and second octive"). Plain doublings, no depth or recursion (Tom: "its plain doublings, ordinary math. but now we know
  why, its a consequence of setting V = H, which creates the unit circle"; SPN R188 records it, restoring 8 Oct's reading over
  9 Oct's corrections); by metres the edges slide. `?v=&lod=none|metres|vh&still=1`; hook `recoverAt(h, x, y, grain)`; strip folded / h/v / v/h (Tom: "what happens if we don't flip at the corner?": unfolded, one side runs off); `?strip=`; hook also `stripAt(h/v, mode)`; hook `window.__flight`. Not in the flying page.
- `demos.html`: **the list of pages** (7 Oct 2026): the world, the lab and the demos (sweep, dial, sphere, facing, one sweep and three paths, what is H and the chain from H, levels, walk, the mountain and the thumb, H is a zoom, parallax from the corner, the sphere in the cube, the wedge, browsing the wedge, pool, the infinite table) and the three on the physics correspondence, the gameplay sketches (marbles among them), each
  with a description and a few direct links. No script. Add a card when a page is added. The flying page's "demos" button opens it.
- `papers/`: **the master copies of the owner's papers**, edited here from now on
  (branch, PR, merge, like the page). `serial-parallel-nowhere.md` (SPN) is the
  paper behind the labs (§9.9 the labs, §11.4 the conjecture, §12–§14 their
  standing); `v-and-h.md` gathers every idea about v and h, by item.
  `number-line.md` (7 Oct 2026) is a working paper Tom iterates on: how people meet the
  number line (its two infinities one under the flip; situation 3 within a window, 4 before
  and past it, a bounded line held whole). A reading; parts go to SPN only once tested or ruled.
  `serial-parallel-nowhere-record.md` is SPN as written 29 Sep – 1 Oct, before the
  rewrite: **a frozen record, never edited.** Section and proposition numbers cited
  in the corpus before the rewrite are the record's; SPN's opening note maps them to
  the current ones. SPN opens with the terms in order (relation, reading, corner, sweep,
  octave, recursion, spiral; since 8 Oct recursion is considered and rejected for
  level of detail: the levels exist whole, a thing's level is set by its size (smaller things have
  less detail; not a request), and nothing recurses), a map of how the parts depend, and the standing of each;
  then the central result and the open question (what fixes the ratio between rungs; demoted 8 Oct: the reader
  sweeps its level of detail, proportional then logarithmic, and the derivation of 2 is in Appendix D, with
  Proposition D.1 since 9 Oct: on a level with only its ends, order and flip, the halving is the only subdivision supplied;
  other branching factors need an added measure).
  `physics.md` (10 Oct 2026, Tom: "lets create a new physics paper and iterate there") is the working paper for the physics
  correspondences: the rules (real data or exact arithmetic, prediction first, keep the case, name the bridge), a
  dictionary from SPN's geometry to physics, the results by standing (real data, exact arithmetic, Wander's world as
  illustration only, simulations of our own checked against a full referee), the kills, and a queue of tests. New physics tests are planned in `plans/`, reported there, and
  promoted to SPN only once ruled.
  `inverse-square.md` (10 Oct 2026, Tom: "lets give the inverse square law its own paper to iterate on") gathers the law:
  as physics holds it (derived from conservation and three dimensions; tested as a bound on the exponent), in levels
  (2 of light, 3 of number per level of distance), the reader's two regimes, the near field (NRF: the pair's corner exact
  where the light is a share), the lay's form (ISQ), each claim marked physics / exact / data / reading / illustration.
  `parallax.md` (12 Oct 2026, Tom: "put it in a parallax paper and lets iterate there"; SPN R219) is the working paper on
  parallax, a calibration case like `inverse-square.md`: what is known already (triangulation, the inscribed angle,
  strength of figure, stereo's d² error, stellar parallax), the pair (half-baseline, distance) with γ/2 its sweep angle and
  γ its facing, why parallax and situated observation are both needed, the depth's bell (cosh(ln k), the facing's rate
  per level, the even turn's ½ sech), the error's shape (the depth is parallax's and has the corner, on the bisector only;
  the across error is the direction's; the total least at √2·(B/2); on the circle round only at its top; off the bisector
  the radial error least inside the circle), the band and the baseline as a second zoom, the ladder, open questions. Each
  claim marked classical / exact / data / simulation / reading / illustration. It was OFS Proposition 11(d) for an
  evening (R218) and was taken out; OFS keeps Proposition 11(a)–(c). Since 13 Oct its §6 works back from what parallax
  already knows (Tom: "work backwards from known results of paralax and show the forced logical chain"; SPN R223): d =
  a/tan p, the au measured outside and now agreed (IAU 2012), σ_d/d = σ_p/p (exactly γ/sin γ, the outer reading, π/2 on
  the Thales circle), not inverting noisy parallaxes (Bailer-Jones 2015; Lutz and Kelker 1973), best when square; each
  forces the next, down to one reading, two standpoints alike (the pair's V = H) and one outside amount. Its step 3 says
  where the π/2 falls (Tom: "can parallax be used to illustrate PI/2 * 2/PI = 1"; SPN R224): the turn in γ/sin γ is the
  pair's facing, twice its sweep angle, so π/2 comes at the pair's corner, where on OFS §10's thumb it comes at the
  sweep's horizon; one identity on two angles, not to be conflated.
  `observation-from-somewhere.md` (11 Oct 2026, Tom: "bring the key ideas from these papers together into a single paper
  for external review") is the one self-contained paper for outside reviewers. **A normal paper a human would read**
  (Tom, 11 Oct, SPN R202: "create a normal paper that a human would read"): abstract, introduction, setting, propositions
  with proofs, discussion, references. No standing marks, ruling numbers, file paths, quotations of rulings or revision
  history in it. **Tests only where they specifically help a core theme** (SPN R208: "we can add tests if they are
  specifically helpful to the core themes of the paper"; "dont just add tests just to add tests"): no failed tests (SPN
  R206, R207: "they are in other papers"), no checks of results that already have proofs; the record (rulings, standings, kills, sources) stays in the
  working papers and plans. **A geometry paper** (SPN
  R201): no physics (bridges, the inverse square, the near field, worlds, the matter fraction are in `physics.md`,
  `inverse-square.md` and SPN Part II). **Its main result** (SPN R200: "it is the primary result"): the Cauchy is the
  reader's addresses, not its payload (R47; SPN §4.3; its Theorem 6: the reach of whatever arrives cancels from every
  reading, order survives every change of payload, sums do not), introduced by the hand (fingers addresses, rings
  payload; SPN R205: the thumb is H and the mountain V, known V the unsituated view, unknown V mountain equals thumb).
  **The reader is explained in full** (SPN R203), its §3: the five situations, which division a reader can
  make, the number line laid twice, the three vantages and their seven-step chain, static and dynamic, what a reader holds
  and the reader as the pivot, the hand in full, and the one number a reader lacks; never fold these into a short table.
  §10 is a worked example (a mountain range). Before rewriting it, check the new text against the old for anything lost.
  It states no new results; where it differs from a working paper's latest dated entry, it is the one to fix.
  **It builds on Jaynes** (14 Oct, SPN R243; Tom: "It would be nice to find and lean on one paper that well cited that has
  overlap with our ideas, and we just build on that."; "ok, if we find another great paper to lean on, we can just add
  it to Jaynes."): his principle of transformation groups (1968, 1973) is the method, stated in §2 ("What we build on:
  the reader's ignorance as a group"), the introduction and the abstract; §11.1 is "The principle, after Jaynes".
  Further anchors are added beside Jaynes, not in place of him. Since R244 (Tom: "what has happend since then?"; "ok,
  proceed") §2 also says the reader's group commutes, so it has one invariant measure where the location-and-scale
  family's affine group has two (Jaynes's own eq. 49 group commutes; its measure coincides with the right-invariant one,
  which later work favours where the location or the scale is of interest; Ghosh 2011), cites Norton (2008: complete
  ignorance is not a probability) beside the pre-prior, and Liu and Adams (2019) beside the situated Bertrand.
  **Since R247 (review 9, `plans/ofs-review-9.md`)** OFS keeps two groups apart: the reader's ignorance (turns of θ,
  rescalings of κ = V*/H, and the exchange of the unit relations, which acts on readings and drawings, not on κ) and the
  Möbius action on readings (turns and changes of the drawing, PSL(2,ℝ)), a fact about the family of drawings used only
  to measure distances. The drawing is c (V = cH, required c = 1), the estimate ĉ (ĉH, Proposition 13), the true size κ;
  never run them together. V = H comes from the exchange on the law of readings (Proposition 5(d)); κ touches no
  reading, so dκ/κ gives the estimate and only through amounts motivates (S), still a premise. Front claims are
  conditional (a chosen group; the sweep a rigid bar's turn). Since R245 §11.2 question 2 also works von Mises's water and wine, the case Jaynes left open: every
  fair answer puts P(x ≤ 1) = ½, and one law unchanged by one liquid's unit plus the exchange gives the levels, ln 6/ln 9.
  Since R246 §11.2 question 7 answers the marginalization paradox (Dawid, Stone and Zidek): under a scale nuisance's own
  dη/η, integrating it out agrees with reasoning from ratios, same prior, for every law; the reader's dκ/κ is that
  measure. §2's preference for the right-invariant measure is qualified to the location or the scale of interest (for
  μ/σ the paradox-free one is Jeffreys's dμ·dσ/σ²).
  Since 13 Oct (SPN R220, R221) it has the three-party wedge: Propositions 3(f) (the sphere only if V = V₂ = H) and 5(e)
  (the even wedge's readings the two-dimensional Cauchy, every pair at its corner, the near field a third, with its
  converse), "More parties" after it (SPN R225: n other parties, every pair at its corner, the near field in all
  readings 1/(n + 1)), and "A sphere in a cube" after Proposition 8 (any size; the extent must be known for amounts). §10's step 3
  (SPN R223) shows π/2 · 2/π = 1 on the thumb: the two vantages joined return only what the reader put in, H in H.
  Since R226, H is the value the reader chooses to start the system, not a measured size ((P1), §2, §8); V is the drawn
  whole and V* the true breadth throughout; "What the geometry needs: a shape and one H" follows Proposition 3. §8 has
  "What a larger H gives and takes" (R229: nΔ/H inside the corner, the lays parting past it, the best H the corner of
  what is read) and §9, after Proposition 14, H of 0 and H of ∞ as its corner-free rulers (R228). §9's "What a unit
  is, and why a reader needs one" (R230; Tom: "A unit is needed, it injects physics into the relation"; "A unit is
  pre-measured relation. It says something like 5 ounces/ 1 foot"): a unit is a relation measured beforehand; within
  one reader its value is a zoom, needed because addresses are finite, where the world's scale first reaches the
  reader (in the laying, not the readings); between readers an agreement. The introduction says the same. Then §9's
  "Two ways to represent a thing" (R231; Tom: "if its unitless, than its geometric"; "something can be represented in
  terms of something else, that is unitless. or you can represent something in terms of an agreed upon unit"): in
  terms of something else in view, unitless and geometric; in terms of a unit agreed beforehand, where physics enters;
  unitless values fixed by the geometry, or read from the world (geometric in kind, found, not derived). §9
  opens with "Geometry first, then values" (R227): physics assigns the placeholders' values as multipliers on the
  amounts, never redrawing a whole, and the geometry is agnostic to that step.
  Its first external evaluation is in `plans/ofs-review-1.md` (V = H as representation; the Euclidean norm, the premise
  (S) and even turns named as the assumptions the circle, the logarithm and the Cauchy rest on). The fourth, an
  adversarial read, is in `plans/ofs-review-4.md`, with six edits taken (SPN R213): the paper's front now claims what its
  back proves (the address reading conditional on the even sweep being the reader's own; "a reason for" the missing mean,
  not "explains"; (S) scale invariance of the lay's increments, assumed; the vantages' assignment a reading; Propositions
  9–12 classical). Keep its verbs to what is proved. The fifth (Gemini, on the foundational axioms) is in
  `plans/ofs-review-5.md` with a response: the main result's core holds for every exchange-symmetric path and weight
  (the median at the corner; no mean too where the weight does not vanish at the horizon) (circle, square and line alike; only the Cauchy's exact shape needs the circle and
  the even turn); the claim to make is necessity relative to a stated ignorance (§11.1). Edits A–F made (SPN R217):
  Theorem 6(e) (the median needs only fairness, the missing mean also a weight that reaches the horizon), the norm entering only through the measure on
  directions, conditional necessity in §11.1, a disturbing reading out of scope, preferred scales setting where the lay
  stops; the SI's constants in `physics.md`. Its second part ("more reader situations with yet more geometries") is
  answered there too: each proposed situation lands in the payload, the amounts or a power of the reading; edit G made
  (four more entries in §3.1's "Cases that look like a sixth"). A comment from Grok (an empirical defense from ordinary
  perception and instruments) is recorded there and not taken: real instruments use several weights. The sixth (ChatGPT,
  13 Oct, "one sweep, two readers") is in `plans/ofs-review-6.md` with responses (SPN R224): its bounded reader a change
  of units unless the shadow is named, its corner the horizon, its question open question 2, answered by three paths;
  it caught the dropped horizon condition. Made: the three-path table in OFS §11.2, question 2 (circle, line, square
  agreeing at home, the corner and the horizon, parting between; none with a mean; sin² 2θ, fair but vanishing at the
  horizon, with the mean 4/π), checked exactly in `ofs/paths.py` (Q1–Q5; run 1's Q3 killed by my set-up, run 2 not),
  and `paths.html`. Its message 5 (five parties drawn at H, read as assuming their payloads equal) is answered by Tom's
  "from the geometry's perspective, its job is done, what ever the true breadth makes no difference" (SPN R225): the
  drawing is required and finishes the geometry; the true breadths enter only the amounts; the payload is what arrives.
  Made: WDG run 2 and OFS's "More parties" after Proposition 5(e). Message 6 (placeholders, not physical breadths;
  Tom: "so why even include breadth"), then Tom's "Even H is not a real breadth" (SPN R226): the geometry a shape and
  one H; the corner is v = h in any drawing, equal lengths make it 45° and the even sweep's median; no reading gives V*/H.
  The seventh (Grok, 13 Oct, an overall assessment: "ready for external scrutiny after the local clarifications") is in
  `plans/ofs-review-7.md` with a response (SPN R232): two of its five points already in the paper, the lighthouse
  contrast named in the abstract (edit A), serial marked as the look's in §7.1 (edit B), condensing declined (R203).
  **The arc is the head's turn, not the walk** (13 Oct, SPN R233; Tom: "this is a source of much confusion. the arc is
  drawn by the rotation of the head, not the walk. the outside reader turns his head the farthest … the inside reader
  turns his head the least. the unsituated reader does not turn his head at all"): the position crosses the line once;
  the outer's facing turns a half turn (facing = 2θ, on the line as diameter), the inner's bar a quarter turn (on it as
  radius), the unsituated none; the same arc π/2, read π/2 and 2/π; their product returns the line, not their difference
  (π/2 − 2/π = 0.934). In OFS §3.4 (a column for the turn), §4 and §10 step 3, SPN's head and §1. A note from another
  session that subtracted them is in `plans/facings-note.md` with corrections. **The unsituated view is the chord, the
  situated view is the arc; the chord is prior to the circle** (14 Oct, SPN R234): the chord needs only the two parties
  and their sum (h + v = 1, the sum norm), no turn; the arc adds a facing turned through and the Euclidean length; the
  circle is that arc over every facing, held whole by the completed view but drawn on the chord, after it. In OFS's
  abstract, introduction, §3.2 (a row dividing by the sum), §3.4, §5 and §7.5; SPN's head, §1, Proposition 1.2 (7).
  **The arc is where the two facings' rays cross** (14 Oct, SPN R235; Tom: "the arc is the intersection of the rays that
  are swept over the two facings from horizontal to vertical"; "lean on whatever classical theory best describes this
  situation"): on the chord, a ray from one end reading v/h and from the other h/v cross on the semicircle (Thales), at
  distances h and v; facing twice the ray's angle (inscribed angle); the flip a projective pairing of the two pencils,
  so a conic (Steiner 1832), round only at V = H. OFS §4 "The arc from the chord", with Euclid and Steiner cited.
  **One unsituated view; V₂ is the azimuth** (14 Oct, SPN R236, R237; Tom: "the unsituated view is h+v+?=1. the
  situated views are everything else that builds from horizontal, vertical and ?. Not just inside and outside"; "there
  is another sweep V2"; "Use the correct terms for V2 … lean on classical theory to explain V2"): the sum cut is the one
  drawing needing no standpoint; every other is situated, the two hemispheres two of many ("three vantages" kept as the
  named cases). The hand's two sweeps are horizon coordinates: altitude (H to V, v/√(h² + v₂²) = tan a) and azimuth
  (V₂, round the horizontal from h, v₂/h = tan z), each with its corner at 45°; the even octant is even in azimuth and
  in height (Archimedes' hat-box, Lambert's equal-area map). OFS §2 (two paragraphs), introduction, §3.4, §3.7, after
  Proposition 5(e), notation, references (Archimedes, Lambert, Smart). **The truth is the sum; the reader's drawing is
  its centre** (14 Oct, SPN R238; Tom: "so the truth is h+v+v2=1; user sets h zoom and assigns v and v2 to be equal to it,
  and the entire geometry is revealed"; "yes, that is what the math says"): the true breadths as shares are a point of
  h + v + v₂ = 1, scale-free; H sets the zoom; V = V₂ = H is the triangle's centre (⅓, ⅓, ⅓), the triple corner, from
  which the geometry follows; the truth lies off it by V*/H and V₂*/H. OFS §2 and the introduction. **The situations with
  V₂** (14 Oct, SPN R239; SIT): OFS §3.1 renamed "The situations", the relations first, the five for one party, then
  "Two other parties" (one entry per party; both known, half-situated, (3, 3), (4, 4), (3, 4), (4, 3), each in prose);
  the three-party reader where the parties' rays meet square (only home and its mirror); §3.4 "With three unit
  relations" (a hemisphere reads 2 at once, ½ one direction at a time).
  **The lighthouse and Mercator's map require V = H** (15 Oct, SPN R258; Tom: "all we need for this paper is to complete
  the well known metaphors of the mercator and lighthouses. If we can show that V must equal H in those to situations,
  that's enough for this paper."): Proposition 5(f), (g) after "Working back from the Cauchy" in §7.1, with proofs.
  The lighthouse: (x − α)/β = tan θ, the path cancelling from the two legs, the shore drawn at c times the sea putting
  the half-way flash at arctan c, the corner and the flip only at c = 1, any H a similar figure. Mercator's map: a
  cylindrical chart's c = f′(φ)·cos φ, bearings drawn at tan ψ′ = tan ψ/c, true everywhere only at c = 1 (Mercator),
  Tissot's indicatrix the bar in two units, areas sec²φ a zoom, equal area forcing c = cos²φ (Euler, Gauss); a table of
  four charts in v and h. Numbers checked in `ofs/charts.py`. The abstract, introduction, §6 and §7.8 point to them.
  That is the scope Tom set for OFS on this line: the 2/π catalogue and the sweep over a horizon stay in the plans.
  The tenth evaluation (ChatGPT, 15 Oct, of the 14 Oct draft: "8/10 as a working paper") is in `plans/ofs-review-10.md`
  with a response; edits A–H made (SPN R259): V = H "required for the sweep to be a turn" (abstract, introduction);
  Theorem 6 opens with its premises; "universal" addresses scoped to shapes laid evenly by direction; the sum is where
  the truth *would* lie, found only with the breadths (amounts), never by normalizing; (S) named as assumed in the
  abstract; **Theorem 6(c) fixed** (it was false for unrestricted f: Hamel-basis additive maps commute with every
  finite mean; now stated for strictly increasing f); the view from nowhere a representation, not a view anyone takes.
  Condensing again declined (R203).
  **Two choices, and a number that is not one** (15 Oct, SPN R260; Tom: "two degrees of freedom here, choose and H and
  than choosing to assign V to it."): OFS §5 after "What V = H means": H free (a zoom); c (V = cH) not free, c = 1 the
  only value giving the rigid turn (3(e)), the Cauchy at the corner (5(d)), the lighthouse's corner (5(f)), true
  bearings (5(g)); V*/H not a choice (Propositions 8, 13). A zoom changes both directions alike, a stretch one.
  **V = H shown for the construction, not claimed for readers** (15 Oct, SPN R261; Tom: "parallex assumes v=h and it
  works great. that is solid proof that at least the math works, not that readers actually do that. … a bridge to far
  for a single paper."): OFS §11.2 question 6 "Answered for the construction, open for readers" (triangulation and
  Mercator's chart show the mathematics holds; whether an eye, a brain or an instrument draws V = H is empirical, not
  taken up). Keep OFS from claiming that readers do it.
  **Should, not does** (15 Oct, SPN R262; Tom: "but they should  If the don't.  it offers many mathmatically
  interesting capabilities."): OFS claims that a reader should draw V = H (normative, as Jaynes's principle is), since
  only that drawing gives the turn (3(e)), the readings laid before anything arrives with the corner at their median
  and the near field a half (5(d)), every pair's corner (5(e)), the angles kept (5(f), (g)); the introduction and
  §11.2 question 6 say so. Whether readers do stays open.
  **Proposition 3(g): a uniform sweep that returns draws V = H in its own measure** (15 Oct, SPN R263; Tom: "yes", to
  Claude's answer to a ChatGPT follow-up, "Smoothness alone does not automatically establish uniqueness"): smoothness
  does not (an ellipse is smooth); a sweep uniform (one linear map per step) that returns after a full turn, all of v
  a quarter on, preserves an inner product unique up to a factor, in which V = H and (h, v) = (cos ωt, sin ωt). The
  rigid bar is derived; the factor is H; what stays assumed is uniform and linear. `ofs/periodic.py` checks it.
  Pointers in "Two choices", "The Euclidean choice", §11.2 question 2. The follow-up is in `plans/ofs-review-10.md`.
  **Neither choice can be declined** (15 Oct, SPN R264; Tom: "Not choosing a value is not an option either."): OFS §5's
  "Two choices" closes with it: no breadth for the other, no relation (3(a)); an H favouring no value is H at 0 or ∞, a
  corner-free ruler (Proposition 14) that loses what is read (§9); with nothing known the estimate is H (13(c)).
  **Situations 3 and 4 are vantages, their mechanism open** (15 Oct, SPN R266; Tom: "the exact mechanism has not been
  pinned down for either."): 3 the outer hemisphere, 4 the inner; OFS follows parallel and serial as a proposal, says
  so in §3.1 ("Vantage, not mechanism"), the rule's third question, §3.5 and §11.2 question 8, and never as the
  definition. **The payload is a wave of some kind** (15 Oct, SPN R267; Tom: "the payload is a wave of some kind, not
  the actual object(s) creating that payload wave."): OFS §2 says so; the reader reads the wave, not its sources.
  **No "parallel" or "serial" in OFS** (15 Oct, SPN R268; Tom: "yes, remove serial parallel."): OFS names situations 3
  and 4 the outer reader and the inner reader; where a result rests on holding, it states the condition. SPN keeps its
  words (and its name).
  **Exterior and interior** (15 Oct, SPN R269; Tom: "adopt math formal names for inner and outer, no need to invent new
  names."): OFS's situation 3 is the exterior reader (an exterior point, the arc's convex side, the exterior reading
  π/2), 4 the interior reader (an interior point, the concave side, the interior reading 2/π).
  **Exterior wave-like, interior particle-like** (15 Oct, SPN R270; Tom: "exterior - wave like, interior - particle
  liike"): a reading, in SPN only (physics, not OFS). Tested for consistency by WVP (`plans/wvp-plan.md` + `wvp/`):
  the interior's counted arrivals build the exterior's pattern at √N, find the corner with spread (π/2)/√N, never
  settle a mean (it climbs (2/π)·ln 10 a decade; P3 killed by my tolerance, P3′ not); real data queued.
  **Exterior: the payload's mean (Gaussian); interior: the addresses' median (Cauchy)** (15 Oct, SPN R271; Tom: "outside
  is gaussian, it is the mean, it measures the actual physical payoad … inside is cauchy, it is median, is the address and
  sweep of the gaussian center of gravity."): a reading; OFS §7.1 ("the exterior reader's bell") and §7.6 read
  otherwise. **Two sweeps, two results** (15 Oct, SPN R272; Tom: "remove the outside the apple, inside the apple metaphore
  … its two sweeps … the outside sweep gets the payloads, the inside sweep gets the addresses to the payloads."): OFS §3.1
  "Two sweeps, two results", the rule, the five, the introduction, the hand, §3.4, §7.1 "The addresses' bell", §7.6; no
  apple in OFS.
  **The address points at the payload; central and inscribed** (15 Oct, SPN R273; Tom: "can we confirm that the address
  we calculate on the inside points directly to the payload on the outside?"; "this is a major insight, lets explain it
  fully"): OFS §4 "The address points at the payload": A's ray at θ (the inscribed sweep, the address) and the radius
  at 2θ (the central sweep, the payload) end at one point (Euclid III.20), B's projection on the address (III.31),
  only at V = H. R269's exterior/interior replaced by the formal central/inscribed throughout OFS.
  **The density in full** (16 Oct, SPN R274; Tom: "the cauchy equation is missing the density parameter"; "the
  parameter is 0 to 1, 1 is the default"): ρ, the share of addresses met by a payload, ρ·2/(π(1 + (v/h)²)); ρ = 1
  simplified away; a constant ρ normalises out. OFS after Proposition 5(d). Reading to confirm.
  `plans/ofs-literature.md` (12 Oct): a prior-work search by a fresh agent (sources seen as search results only, details
  to check). The address/payload reading of the Cauchy was not found; its parts are in print (Jones 1999, Cacoullos 2014
  for 6(a); Stevens 1946 for 6(b)–(c); Cacoullos and Papadatos 2013, Jones 2008 for 6(e); Frank and Smith 2010 the
  nearest prior reading; Leonard 2011 for §11.1; Drory 2015 against Jaynes, bearing on question 2). Since 13 Oct (Tom:
  "ok, cite the prior work in OFS"; SPN R222) they are cited, each rechecked first (the plan's "Cited" table, with the
  corrections found): OFS §7.8 for Theorem 6 and Proposition 5, §9 for Propositions 8, 9, 11 and 14, §11.1, §11.3, and
  Drory answered in §11.2 question 2 (the selection is a choice; the median at the corner survives it, and the missing
  mean too where the weight does not vanish at the horizon).
  `vantages.md` (11 Oct 2026, Tom: "the core insight in our papers is that classical math and physics assume a completed
  perspective … three perspectives, completed "classical', outer-hemispherical and inner-hemispherical"; "lets start collecting
  those paradoxes, its not a short list"; SPN R191) is the catalogue of paradoxes read as vantage conflations: each entry
  with its vantages, the reading, what was already known, and its standing (worked / reading / candidate). It grows.
  `denominator-paradox.md` ("Each Sees the Other Smaller", an older paper Tom wrote with Claude in an earlier session, added 11 Oct) is a first course in
  denominator paradoxes: private rulers compared on one number line; dissolve, then purchase a shared denominator (the
  exchange: ratio and product of the two reads). `vantages.md` §F maps it onto the three vantages.
  `papers/archive/` (11 Oct 2026, from Tom: "older papers … archived but off many gems we should pull forward"): earlier
  papers kept as received, never edited: *Reader Geometry as Addressing* (rulings R1–R151 only; R152–R187 are
  quoted in SPN Appendix A), *The Relation Space*, *Browsing the Fisheye*, *The Radix*, *The Order of Limits*, *One
  Reader*, *Degrees of Freedom*; and since 11 Oct an eighth, *Special Relativity, Through the Fisheye* (4 Sep; Tom: "here is
  a earlier paper on SR"), its numbers rechecked in `srf/check.py` (all agree but C1, a Cauchy sky only in 2+1
  dimensions), its gems and one link to MOT run 2 (γ even, γβ odd in ln k; 1/γ = 2k/(1 + k²)) in `plans/archive-gems.md`.
  They predate 9 Oct: check every term (density, view from everywhere, inside/outside,
  fulcrum, arctan, h and v as breadths, recursive corners, depth, old situation numbers) before pulling anything forward.
  `plans/archive-gems.md` lists the gems, where each went and what is queued. **Where an archived paper conflicts with
  one that is not archived, the paper that is not archived stands** (Tom, 11 Oct; SPN R192).
  Other papers the corpus cites that are not in this repo (`plans/…` notes from other sessions): leave those references as they are. `_config.yml`
  keeps `papers/` and `plans/` off the Pages site.
- `plans/`: working notes, reviews and lab plans, as the corpus cites them
  (`plans/…`). `what-deserves-attention.md` is a review of what to take up next
  (6 Oct 2026): a reading, not a ruling. `hrt-plan.md` (the run for the 2: three
  runs, stopped) and `nle-plan.md` (number lines in people: run 1 on
  Chan and Mazzocco's kindergartners killed the corner's prediction) follow the lab rules: prediction first, runs recorded as they
  came out, nothing above a plan's "Runs" line edited afterwards.
  `nls-plan.md` (+ `nle/nls.py`, 7 Oct): the number-line split on synthetic readers (Tom: synthetic
  tests are fine for persuading each other); the switch is detectable at noise sd 8, the corner against a
  plain log is the fragile part.
  `grn-plan.md` (+ `grn/grn.py`, 7 Oct): serial or parallel set by the reader's grain (Tom: "serial and
  parallel is just our perspective"), on a synthetic binary. The reading depends only on size/grain (by
  construction); serial gives way to parallel near s ≈ 0.7; the knee at the corner was killed twice (runs 1, 2),
  a reader given the shape reading below its grain. Run 3, the pixel the reader's and no model: "two" is certain
  exactly from s = 1, and below it has probability s (not killed). Run 4: below the corner 1/s looks, past it s
  pixels a look; a reader sliding its h by halvings needs about log₂(1/s) looks (not killed). Run 5, h as a
  dial: paying per grain read, a sure reading costs (1+s)·max(1,1/s), least at one pixel across, same at s and 1/s.
  Run 6, steering by its own pixel count from any start (it cannot know its corner): about one look per
  doubling (P1 not killed); within [0.5, 3] killed at one start (luck at the last level below the corner); the
  gain is one-sided, large from below, none from above for a single answer.
  Run 7, the edge moved by light (reader given the shape): resolution limit ∝ light^(−0.499), knee steady
  (not killed).
  Run 8 (8 Oct), a pair receding under the inverse-square law: the reader given the shape loses it at
  v* ∝ a^0.51 F₀^0.25 (predicted ½, ¼); the model-free reader at one grain across, at any light (not killed).
  `anl-plan.md` (+ `anl/anl.py`, 7 Oct): a number line that recurses as needed against the ordinary line's
  depth everywhere. One close pair anywhere sets every number's depth on the ordinary line; with 5 twins the
  recursing line costs 0.375 of it, rising to 1 as detail spreads. Run 1's clustered prediction killed.
  `arb-plan.md` (+ `arb/arb.py`, 7 Oct): arithmetic baseline, an exact referee against float, fixed depth and
  a recursing line of cells: half the storage on mixed depths, 1.25 on the control; the fixed line overclaims
  by ~10⁶; √2·√2 = 2 undecided at every depth (nothing killed).
  `cal-plan.md` (+ `cal/cal.py`, 7 Oct): observation costs calories; a reader enters a level only if worth its
  price. Detail fading fast: depth is the log of worth (within 4%). Fading slowly (r = 0.7): killed, the reader
  prices from two noisy looks and quits early. Run 2 (running estimate): the log-of-worth slope holds within 3% at
  every r; the net still falls short at r = 0.7 (killed).
  `why2-plan.md` (+ `why2/why2.py`, 7 Oct): why the levels might be doublings (SPN's open question). A reader
  stepping its grain by ρ, paying per grain: content with a first sighting, no preferred step (run 1 killed);
  needing a sure reading (3 looks), cheapest ρ ≈ 2 on average and at worst (run 2). Broad valley. Run 3 (8 Oct): the 2
  holds for 2 to 5 confirming looks in one dimension (P1 not killed); when a look costs a whole image or volume, luck
  pulls the best step to ~1.25–1.35 or ~1.1 (P2 not killed, on its edge).
  `frc-plan.md` (+ `frc/frc.py`, 8 Oct): which ratios between levels are precomputable (Tom: "to prove 2 is forced, we
  must show that every other number is not pre-computable"). From the flip, its fixed point and nesting only powers of 2
  (P1 not killed); a chosen number, a root, arithmetic or 2/π each opens others. Bookkeeping for SPN's "A route to forcing
  2", not a proof; run 1's arithmetic row was capped (my set-up). Run 2 (exact fractions, no cap): base only powers of 2
  again; arithmetic opens a factor of 3 (P2a not killed). Run 3 (Tom: "does 2 allow us to do recursion without runtime
  logic"): on a level (identity and flip) only a split in 2 has every part of one kind, on the full turn every split does;
  a theorem (⌈b/2⌉ kinds), resting on the premise that a level's only symmetries are the identity and the flip.
  `isq-plan.md` (+ `isq/isq.py`, 10 Oct): is the in-place lay the inverse square? Past the corner it is 2 − 1/s,
  proportion in h/v, so its room per unit s is 1/s², the flip's Jacobian (all five predictions not killed); draw's piecewise
  lay is 1/s² at each level's geometric middle. Read s as d/Δ: the lay is an angular size, its 1/s² that size's rate,
  light's inverse square its square. A shared form with one origin, not a claim that the lay is light.
  `hzn-plan.md` (+ `hzn/`, 10 Oct): standing on the outline is standing on a world. From a place on a circle the readings
  are chords 2·sin φ; the corner is the radius, 30° below the horizon (on a ball 2/e of it); rising by e radii, the horizon
  is √(2e), half a level per doubling (P1–P4 not killed). Draw's levels page agrees to its grain: P5 and run 2 killed at a
  fixed grain; run 3, both grains doubled together, not killed.
  `ref-plan.md` (+ `ref/ref.mjs`, 10 Oct): the corner as the reference sphere. Published radii: rocky worlds within a
  hundredth of a level of their corner, giants a tenth (P4, P5 not killed). Wander's bodies (P1–P3 killed): one asteroid's
  corner 1.3% off its ball; the Moon 0.25 levels (the real one 0.0165), Mars 0.135; the middle band, not the broad, holds
  most relief in twelve bodies. Scaling `res/` relief to real levels is Tom's call.
  Run 2 (`ref/ref2.py`, 14 Oct; Tom: "whats new is the tvf3d signal. it shows how the signal itself is packed."; SPN
  R249): a reader drops one octave of degree per level of distance (exact); on seven published shape models (Mercury,
  Venus, Earth2014, LOLA, MOLA, Vesta, Ceres; Zenodo/Curtin, sha256 in the plan, not committed) the relief per octave,
  degrees 8–1023. All three killed: one power law (P6, by the airless bodies, which bend at a tenth to a fortieth of
  their radius), half per octave (P7: slopes −0.21 to −0.98), one slope for all (P8). Earth, Mars, Venus about −0.4 per
  octave. Then Tom (16:26, SPN R250): "no, real signals are not packed tvf3d. tvf3d is like a pre-read signal": a real
  signal arrives unpacked; a .tvf3d is the reader's levels with the payload already placed, coarse first, so a later
  reader takes a prefix and reads nothing again. The run's framing (does the world come packed?) was a misreading; its
  kills stand; it measures how real relief fills a pre-read signal's levels. A band's relief when first held is
  0.0002–0.07 of an address. The games page's Levels application was judged an illustration (its rule wander's; the
  shape any size-on-screen LOD's; geometry clipmaps, Losasso and Hoppe 2004, already do it).
  `mag-plan.md` (+ `mag/mag.py`, 10 Oct): on the Hipparcos stars (HYG v3.8 from GitHub, sha256 in the plan; parallax
  distance, V and spectral type only), light falls two levels per level of distance: G dwarfs 2.02, K0 giants 1.93 where
  complete (P1–P3 not killed), 1.61 past the limit; K0 III scatters 1.4 levels (P4 killed).
  `cnt-plan.md` (+ `cnt/cnt.py`, 10 Oct): star counts in levels on Hipparcos to V 7.3: about 1.2 levels of number per
  level of light at every brightness, not the even spread's 1.5 (P1, P2 not killed at their bands' edges); plane and poles
  alike, 1.229 and 1.227 (P3, P4 killed).
  `gcn-plan.md` (+ `gcn/gcn.py`, 10 Oct): star counts within 100 pc on the Gaia Catalogue of Nearby Stars (VizieR
  J/A+A/649/A6 table1c, from Tom; sha256 in the plan), kinds by colour on the main sequence. All four killed: the RUWE cut
  removes more near stars (steeper counts, poles past the plane), and a fifth of G/K colours within 50 pc are white dwarfs.
  Read after the run without the cut: 2.93–3.00 levels of number per level of distance for every kind, plane = poles.
  `grd-plan.md` (+ `grd/grd.py`; predictions 10 Oct, run 1 14 Oct, SPN R248): the ratio between levels in a measured
  reader, the grid cells' modules. Run 1 on Gardner et al. 2022 (figshare, CC0; data not committed, sha256 in the plan):
  pooled adjacent ratio 1.432 in the √2 band (P1 not killed); P2, P3 killed by too few animals; post hoc the largest
  module is not measured reliably in a 1.5 m box. Two rats; more animals needed. P1 was a halving, √2 (area) or 2
  (length), within 0.07; the plan states the published means known beforehand (~1.42, ~1.7).
  `grd-landscape.md` (10 Oct, a reading; Tom: "lets just establish the boundries, see how we might slot in"): the
  measured ratios, the coding theories (economy √e, nested codes) and the mechanism (Kang 2019), and SPN's slot as the
  measure-free baseline 2^(1/D), which the coding theories depart from by their added measure; told apart in 1D and 3D.
  `pol-plan.md` (+ `pol/pol.mjs`, 10 Oct): pool from inside (`pool.html`). Contact is h + v = 1 on the pair's two readings
  (P1, P2 identities, not killed); one ball's own reading decides contact only when all balls are alike, the calibration
  V = H (P3 not killed); played from inside in each ball's own size, the game equals the referee's to rounding, never 1e-3
  apart in 8 s (P4); each ball's world about 4.5 levels deep (P5). Run 2: a cushion is the reader's own flip, contact at
  the corner h = v = ½; a pocket is entered when it fills the view, v = 1 (P6–P8 not killed); the whole game from inside
  equals the referee's to ~1e-15. Run 3, each ball reading the others late at speed c: the naive reader's error saturates
  at ~a ball's radius until c ≈ 400, then falls as 1/c (P9 killed); carrying the image forward is 11–4,300× better (P10);
  its error collapses as the lateness at contact drops to about one tick (post hoc). Run 4 tested it over c × tick (P12 not
  killed): the error follows the lateness in ticks, small below ~1, a plateau (~2% of a radius) above 2, whatever c; a finer
  tick at fixed c can be worse. Three corners of named pairs: contact, the cushion (reader and its flip), time (one tick).
  Runs 5–6, level of detail as size (Tom: "smaller and smaller pool balls"): a field of 116 balls in four size levels
  (radius 0.45/2^k); a ball ignores balls K+ levels smaller. Run 5 had a bug (a gap ≤ 0 gave NaN; the cushion's reading is
  now signed, negative when the edge is behind), so run 6 repeated it: from inside still the referee's game to ~1e-9
  (P13′ killed narrowly by the smallest level); ignoring costs ~4× less per level, not the mass ratio's 8 (P14′ killed);
  skipping saves a third of contact responses at K = 1.
  Run 7, the cost per contact in the true game: one skipped contact is exactly (1+e)/(1+8^j) of the closing speed
  (P15); smaller balls close only 1.2–1.6× faster per level (P16 killed), so one contact costs 5–6× less per level (P17
  killed at its first step); with their numbers, the first-order drift falls 3.70 then 6.74 (P18 killed narrowly), the
  chaos lifting the last to the game's 4.2. The 4 is the field's mix, not a law; what one may ignore is set by momentum.
  Run 8, the prediction horizon on `play-trick.html`'s engine: a contact turns an aim error by s/(2r cos φ) (for a full hit
  2^L − 1, L the levels the pair started apart); P19, P20 killed: the fixed-tick contact (balls overlapping up to 0.077)
  made thin cuts cos²φ less sensitive. Run 9, contact made exact (each ball finds h + v = 1 in its own units): every
  contact and chain to rounding (P22–P24 not killed). On an open table a contact costs 1.5–2 levels, a 0.1° aim error
  passes half a pocket by the third contact (the preview's "see 3 deep"); inside a rack errors shrink (A ≪ 1).
  Run 10 (11 Oct), level of detail by time to contact: a ball reads the kick a smaller one would bring from v, h and two
  looks, (1 + e)·ρ³/(1 + ρ³)/(h·τ), ρ = v/h, τ = v/v̇ (Lee's). Matched in work, ignoring by the kick picks the same
  contacts as ignoring by size and plays the same game (P26 killed, factor 1.00): the share's 8 per level outweighs the
  closing speeds, so here a ball's level alone reads its momentum. τ alone is 3.4× worse at K = 2 (P27 killed at K = 3,
  a draw in the chaos). Two looks a tick apart read the kick 8% low (P25 killed; post hoc: the estimator divided by the
  newer reading, and the tick is a tenth of a fast pair's τ).
  Runs 11–15 (11 Oct, Tom: "scale it up to infinite number of balls … only calcualate the visible balls"; `pool-infinite.html`):
  a window of balls in a world of totals by dyadic level against a referee computing all 13,581 (a hard-disc gas). The
  referee is kinetic theory's gas (Enskog's 4.864 contacts per ball per second to 0.1%, once the 2D cross-section is two
  diameters: P29 killed by my derivation; Rayleigh to 4e-4; S(0) 0.526 against Henderson's 0.530). The work is the
  window's (+3.7%, −2.8%, +3.8%, +23.7% in the runaway, −1.6% for 256× the balls). The boundary took five runs: the open
  edge drained (run 11: flux without contacts, the virial push missing), an open band drained outward (12), a band held at
  a count was underfilled against its mirror (13: −6%), pushes stored beside the window ran away (14), and run 15 (mirror,
  band at the ring's chemical potential, pushes booked in the far field) passes all five: the view's density, warmth and
  contacts within 0.3%, its count's fluctuation within 12% of the referee's (a closed window's 33% less), books to rounding.
  Runs 16–18, a pressure pulse from 60 units away (a hot disc): the referee carries it as sound at the hard-disc gas's
  c = 9.76 (Henderson; half-maximum at 3.9 s, P34 not killed); diffusion cannot (nothing above the noise); a fluid far
  field (Euler, hard-disc pressure, Rusanov) first never ran (run 16: the setting named `far` was overwritten by run 15's
  list of coarsest cells, now `farCells`), then filled the window because its wall pushed nothing (run 17), then, with
  the wall's push p·n̂ (run 18), kept the window steady but lost the pulse (22% of the referee's peak, in the noise): the
  disc was averaged into a 60-unit level-3 cell before it moved. Level of detail by distance is right for what stays put,
  wrong for what travels toward the reader: a signal must be held at its own size until it arrives (refinement by the
  signal; untested). Modes: `opts.far` diffusion (default) | fluid | fluidwall.
  Written up (11 Oct) as a reading, unruled: SPN §3.3, "Level of detail tried in a simulation" (size reads momentum where
  the levels span more than the speeds; a reader that holds a world folds by distance only what arrives as totals, and
  holds what is coming at its own size), SPN §14, "From the pool runs"; `physics.md` §2.2, §2.4, §3; `v-and-h.md` 426–429 (§8p).
  `cue-plan.md` (+ `cue/`, 11 Oct, Tom: "1,3"): the trick-shot engine against the published laws of the game. The
  measurements are blocked here, so the reference is pooltool 0.6.0 (PyPI, Apache-2.0, sha256 in the plan), whose models
  name their sources, re-implemented from its source text. Run 1: the constant ball–ball grip killed (P1–P3: Alciatore's
  fit falls 0.095 to 0.03 from slow to fast, so throw is 4.8° slow and 1.7° fast at half-ball against the engine's 3.4°);
  the cushion agrees at medium speed (P5) and parts at slow (P6 killed: eN 0.62 against Han's 0.80 with e = 0.85); cloth
  and ball constants agree (P7, P8). Run 2: the grip made the fit (`gripOf`); the engine matches it to 0.13° at 30
  points (P9), textbook results and all 13 challenges unchanged (P11, P12); P10 killed by my set-up (the smoke test's
  white rolls part way, so its throws are 3.5°, not a stun's 4.8°). The slow cushion waits for measured data.
  `mrb-plan.md` (+ `mrb/`, 12 Oct, Tom: "a huge collection of marbles, say 500? would this be helpful?"; "both"). Part 1
  (`hcs.mjs`, event-driven, contact at h + v = 1): 500 smooth inelastic spheres cooling (Haff). Per contact −d ln T is
  (1 − e²)/3 to 0.8% at three densities and four e (P1, P3 not killed): density cancels from the count. The clock was
  killed at e = 0.7 (P2: −5.2%); run 2: the bias follows the box against the shear instability L_c ≈ 10.8ℓ₀/√(1 − e²)
  (P6–P8 not killed), the clock about twice the count's. At φ 0.3, e 0.5 the box's flow grows (R past 20; P4); no
  collapse (P5). Part 2 (`play-marbles.html`'s engine, `run3.mjs`, `run4.mjs`): a heap at rest, soft spheres with
  friction. Frictionless Z 6.18 (Maxwell's 2d; P10, P15), frictional 4.74 (P16), packings 0.642 and 0.589 (P12, against
  measured 0.637 and 0.60); killed: P9 and P11 (my protocol: an instant reading of a breathing pile; a rattler rule that
  strips a frictional pile empty), P13 (no Janssen in silos poured and left still: −3% to +26% on the walls). Open: level
  of detail carrying weight (the floor's reader, the pile above as a total).
  `nrf-plan.md` (+ `nrf/nrf.py`, 10 Oct, exact arithmetic): where an extended source turns from near to far, in levels.
  Lambertian disc σ = −2s²/(1+s²): halfway at s = d/a = 1 and flip-symmetric (P1), sphere from its surface likewise (P2);
  the line counted from every direction and the isotropic emitter's solid angle are not (P3, P4 killed); the width is
  log₂(81)/k for a share in s^k (P5 killed). The corner holds where the light counted is a share (projected solid angle).
  `cei-plan.md` (+ `cei/cei.py`, 11 Oct, exact): more points, less seen, from the archive: a parallel reader of step ε
  resolves (N/π)·arccos(εN/2π) of N points round a circle (within 2 points; P1, P3, P4 not killed), peak 1.1222/ε to
  0.11%, its place 2.6% off at ε = 10⁻³ (P2 killed narrowly). `tgt-plan.md` (+ `tgt/tgt.py`, 11 Oct, exact): closure
  between two readers' counted edges recovers the ratio of their holds, |S_A|/|S_B|, to 5×10⁻¹⁵, and nothing more
  (P1–P5 not killed): the denominator exchange made exact.
  `mot-plan.md` (+ `mot/mot.py`, 11 Oct, exact; Tom: "maybe h helps in object tracking and motion"): motion read from
  inside, the clock the only amount. x/ẋ (x = S/d) is time to contact at every distance; from the turn arctan x it is off
  by arctan(x)(1+x²)/x, π/2 at the corner; of two looks a tick apart the older gives τ now, the newer τ one tick ago (POL
  run 10's 8%); each level of an approach takes half the τ read at its start; m/d = ωτ/√(1+(ωτ)²), no bridge (P1–P5 not
  killed). A breadth B as a baseline reads distance best at the pair's corner, d = B/2, alike at d and (B/2)²/d (P7 not
  killed); the first-order stereo error killed past εd/B ≈ 0.18 (P6: x/(1−x) on the far side, the horizon at d = 2B/ε).
  Run 2 (`mot/mot2.py`; Tom: "a fuller geometric explanation of motion using our corner insights"): corners in motion
  come in two kinds, stationary where a quantity is unchanged by swapping its pair (a launch's range at 45°, the energy
  passed at equal masses, a baseline's conditioning; f(k) = f(1/k) gives f′(1) = 0) and a change of regime where swapping
  flips its sign (braking: τ̇ + 1 = d/(2s), Lee's −½ is stopping distance = distance) (P11, P12 not killed). Ranging: the
  capped unit relation and the angle are best at the corner, the plain ratio nowhere (P8); at one budget the in-place
  lay beats the even turn between 0.52 b and 1.91 b (P9). Ratio forms trig-free and exact; P10 killed in its angle
  clause (an angle holds a big ratio to ulp·(1 + x²)/x; the capped unit relation to 1.5e-16 at every size).
  Run 3 (`mot/mot3.py`; special relativity, after the archived SR paper; Tom: "yes"): v = β, h = 1/γ (c the bridge);
  three pairs, three corners (rest for the Doppler pair, β = 1/√2 for (β, 1/γ), the transverse plane for the sky; a
  boost moves only the sky's, to tan(θ/2) = k); γ the even and γβ the odd part of k in levels, 1/γ = 2k/(1 + k²);
  rapidity the reader's lay of celerity smoothed (within 1 − ln 2 nats); pseudorapidity a direction's level; the regime
  switch at pc = mc², symmetric for E (β², a share) and lopsided for T; uniform acceleration one level per ln 2/a of
  proper time (P13–P18 not killed).
  `emc-plan.md` (+ `emc/emc.py`, 11 Oct, exact; Tom: "how the corner helps understand the known equation"): E² = (pc)² +
  (mc²)² is the unit circle of (pc, mc²) in the one unit E, v = β (from dE/dp), h = 1/γ (the clock's rate); E = mc² home,
  E = pc the horizon; Newton's and the ultra-relativistic forms flips of each other, e_N(x) = e_U(1/x), both 6.07% high at
  pc = mc²; mass the light-cone pair's corner, fixed as a boost pans its levels (P1–P4 not killed; P2's quoted decimals
  my slip, recorded). Bertozzi's electrons queued (paper blocked).
  `pay-plan.md` (+ `pay/pay.py`, 11 Oct, exact; Tom: "all we see is the motion of the center of gravity as situated observers
  of serial streams"; SPN R210, two centres: the median of the addresses, the centroid of the unresolved payload): one
  stream cannot tell approach from growth; a same-depth neighbour read at once separates them (payloads relative, never
  scale); below the step the payload arrives as its moments, the photocentre first (a binary's a·|B − β|); a body far off
  is its total mass at its centre of mass, order l down by (R/r)^l, the two expansions meeting at the corner r = R and
  swapped by Kelvin's inversion (P1–P4 not killed; P3 (d)'s index my slip, recorded). Prior work in draw's labs
  (Tom: "we have explore this in the draw.html repository in the labs"; rerun at draw `ea07709`): `rcc` (one reader's
  readings carry the turn, not the size), `udv` (three standpoints give the figure up to size, one agreed length the
  size), `ref` (the median needs every arrival held at once, a parallel reference; a serial reader holds one arrival,
  one extra slot), `rec` (a serial record: scale-free, grain-free marks). So the median is the parallel reader's centre;
  holding (serial/parallel) and resolving (above/below the step) are two axes. **Before new work on readers, shapes or
  recovery, check draw's labs** (`labs.html` in the draw repo lists them; run one with `draw.html?lab=CODE`). The
  geometry is in the main papers (SPN R211: "this is pure geometry not physics actually"): SPN §4.7 (with §2.1's "What 3
  and 4 hold"), OFS §7.6 "Order needs holding", Propositions 9–12 in §9 and §8's "From far off"; `physics.md` keeps the
  physical instances (looming, unresolved binaries, gravity from far off).
  `stc-plan.md` (+ `stc/`, 12 Oct; Tom: "Physics already constructs the completed view from situated observations, and the
  framework supplies a geometric reason the construction can succeed"; SPN R216): a simulation of our own against a
  referee, a figure of 20 landmarks read by 16 to 4,096 standpoints plus one outside length (1% error) and a candle rung.
  More readings improve the figure (shape error N^(−0.49) with maximum likelihood), never the scale (the common shift at
  the outside length's 1% throughout, the landmarks' errors 99% correlated by 4,096); the rung carries 0.0150 whatever
  the number of far members (P2–P7 not killed). P1 killed by my estimator: least squares on noisy bearing lines leaves a
  floor more readings do not remove. Statistical against systematic error is address against payload.
  `pxc-plan.md` (+ `pxc/`, 12 Oct; Tom: "show how parallax and situated observation are both needed. explore parallax
  from the perspecive of the corner"): the pair (half-baseline, distance), its corner the Thales circle. Exact (mpmath,
  50 digits): the relative error per unit angle cosh(ln k), sin γ = sech(ln k), the parallel reader's bell (P1, P2); the
  band acosh(1/ε)/ln 2 levels each side, far edge d ≈ B/ε (P3). P4 killed by my measure (distance from the middle takes in
  the error along the baseline); run 2: depth follows the bell, the error round at the corner and stretched by d/(B/2)
  elsewhere (P5–P7 not killed). Past the band a point is a ray: parallax needs situated observation and returns to it.
  Run 3 (exact, after Tom's "does it belong in ofs?"): the corner is the depth's, on the bisector only; across the line
  of sight the error is the direction's, falling with distance; the total least at d = √2·(B/2); on the circle the error
  round only at its top (aspect cot(φ/2)); off the bisector the radial error least inside the circle (P8–P10 not killed).
  Corrections recorded under run 2: "doubling per level" only far off; the stars' presets off by 2 (p = γ/2). Briefly
  OFS Proposition 11(d) (SPN R218), then moved to `papers/parallax.md` (R219). Run 4 (exact; SPN R223), working back
  from known results: γ(d) + γ(a²/d) = π (P11); (σ_d/d)/(σ_p/p) = γ/sin γ, π/2 at the corner, 1 far off (P12); the round
  error at the corner needs σ₁ = σ₂, the depth's corner does not (P13); a noisy parallax's inverse has no mean and keeps
  its median, 16% of readings at or below zero at the band's edge (P14); the two parsecs differ by a·ε/3 = 242 km (P15).
  `wdg-plan.md` (+ `wdg/wdg.py`, 13 Oct; Tom: "the unit sphere could point every address in the universe", then "but that
  is the unsituated readers sphere, he would have to know the size if the universe. the situated reader has to sweep and
  set V = V2 = H. and create the sweep wedge using the cauchy"; SPN R220, R221): exact (mpmath). The even wedge's readings
  (v/h, v₂/h) are the two-dimensional Cauchy, 2/(π(1 + a² + b²)^(3/2)) (P1); every pair half-Cauchy, median at its corner
  (P2); six chambers 1/6 each, the near field in both readings a third (P3); drawn at V = c₁H, V₂ = c₂H the medians move to
  1/c₁, 1/c₂, c₂/c₁, so each pair's corner needs that pair drawn at one length and the wedge needs V = V₂ = H (P4); a
  rotatable sphere's rays point every point of a cube at any extent, the address (u, t) the same at every extent (P5); a
  face's middle quarter takes 38% of its directions (P6). Nothing killed. `sphere-cube.html` shows it. Run 2
  (`wdg/wdg2.py`, 13 Oct; Tom: "from the geometry's perspective, its job is done, what ever the true breadth makes no
  difference"; SPN R225): n other parties drawn at H, n = 1 … 5; the readings the n-dimensional Cauchy (P7); every
  reading the circle's law, every pair the wedge's (P8); the near field in all readings 1/(n + 1), the count past the
  corner even over 0 … n (P9); drawn unequally, the shares move (P10). Nothing killed.
  `hko-plan.md` (+ `hko/hko.py`, 13 Oct; Tom: "explore what H acutally is. what is H of 0. what is H of infinity"; SPN
  R228): exact (mpmath). Past the world's ends the lays are the corner-free rulers of OFS Proposition 14, the number line
  at H of ∞, the logarithm (reader's) or the reciprocal (in-place) at H of 0, a corner only with H inside (P1); a world
  lost whole three ways at H = n·b, a·e^(1 − L_max), a/n (P2); the best H for two amounts √(x₁x₂), widest angle
  arcsin((r − 1)/(r + 1)) (P3); parallax's error per step cosh(ln(d/H)), the best half-baseline over [a, b] √(ab) (P4).
  Nothing killed. `h-limits.html` and `h-chain.html` show it. Runs 2–3 (`hko2.py`, `hko3.py`; SPN R229), detail per
  object [d, d + Δ]: nΔ/H inside the corner; past it n·ln(1 + Δ/d) on the reader's lay whatever H is, nΔH/(d(d + Δ)) on
  the in-place lay. Run 2's P5 killed by my set-up (a grid too coarse to land inside [d, d + Δ]; the endpoint equalled my
  bound); run 3: the in-place peak at H = √(d(d + Δ)), the corner of the object's own ends (P5′ not killed).
  `thl-plan.md` (+ `thl/thl.py`, 14 Oct; Tom: "the arc is the intersection of the rays that are swept over the two
  facings from horizontal to vertical"; SPN R235): exact (fractions and mpmath). On the chord A = (0, 0), B = (1, 0), A's
  ray reading s = v/h and B's reading h/v cross at (1, s)/(1 + s²), on the semicircle (P1, Thales), at distances h and v,
  foot h² | v², height hv (P2, Euclid VI.8); facing 2·atan s, the half-angle form, Euclid's triples (P3); the corner at
  the top, the flip the mirror (P4); a conic at every V = cH, x² − x + y²/c² = 0, the pairing projective and not
  perspective (P5, Steiner); equal angles give the bisector (P6); the even sweep of one ray even along the arc, the
  half-Cauchy (P7); over x₁ + x₂ the height √(x₁x₂) (P8, Euclid VI.13). Nothing killed.
  `thl/waves.py` (15 Oct; SPN R265, Tom: "the outside has wave like chartacteristics"): the outer vantage reads the line
  as a power detector reads a wave, in squares at twice the angle: its foot h² (Malus), the Stokes point at 2θ
  (Poincaré), a resonance's admittance (1, s)/(1 + s²) with half power at the corner, the unitarity circle and
  Breit–Wigner, a sine's form factor 1.1107 the outer reading at 45°. Classical identities, a reading; not in OFS.
  `azm-plan.md` (+ `azm/azm.py`, 14 Oct; Tom: "there is another sweep V2 … lean on classical theory to explain V2"; SPN
  R237): exact (mpmath, a grid count, a seeded sample). V₂ is the azimuth: v₂/h = tan z and v/√(h² + v₂²) = tan a, each
  sweep's corner at 45° (P1); an even azimuth keeps its own corner under any altitude weighting (P2); even in both angles
  the pair neither sweep reads leaves its corner, P(v ≤ h) = 0.3426, near field 0.2326 (P3, numbers known beforehand,
  stated); the even octant is even in azimuth and height (P4, Archimedes' hat-box, Lambert), and then every pair at its
  corner, near field ⅓, the 2D half-Cauchy (P5); the even-in-height raise belongs to three unit relations only (P6).
  Nothing killed.
  `sit-plan.md` (+ `sit/sit.py`, `sit/sit2.py`, 14 Oct; Tom: "we should expand the readers situations. to accomodate V2";
  SPN R239): exact (mpmath; Gauss-Newton from 2,000 random starts). Rays from parties at the unit points meeting with
  every pair square meet only at t·(1, …, 1), t = 0 (the reader's home) or 2/(n + 1); with two parties on a whole circle
  through home (P1); a hemisphere reads √π·Γ((n + 1)/2)/Γ(n/2) at once and its reciprocal one direction at a time, π/2,
  2, 3π/4 (P2); P3 killed by my set-up (a 0.1 threshold wider than the 0.095 gap); run 2, P3′: 2 and ½ are (π/2)² and
  (2/π)² times 8/π² and π²/8 (not killed).
  `jay-plan.md` (+ `jay/jay.py`, 14 Oct; Tom: "lean on one paper … and we just build on that", Jaynes accepted; SPN
  R243): exact (fractions; mpmath). What Jaynes 1968 and 1973 prove, first from abstracts and secondary sources (marked
  "(check)"), then read in full once the network access was widened ("Jaynes's text, read": every item stands). The reader's unknowns, attitude θ and size
  κ = V*/H, under turns, rescalings and the exchange: dθ·dκ/κ, Jaynes's location and scale on a circle. Rescaling: only
  1/x, every level ln 2, on a share Haldane's prior (P1); turns: Cauchy(z) carried to Cauchy(g(z)), i fixed by every turn
  and the exchange, the arc's foot Jeffreys's arcsine, the Fisher–Rao length the facing 2θ, the octant's squares
  Dirichlet(½, ½, ½) (P2); the exchange fixes the corner and the median, not the law (Bayes–Laplace, Jeffreys, Haldane
  all fair; ¼, ⅓, 0.42 below t = ¼) (P3); the median of dκ/κ on bounds √(V₋V₊) (P4, OFS Proposition 13); Jaynes's
  Bertrand ½ rederived (Crofton), and from home arcsin(R/2D)/arcsin(R/D), ⅓ on the circle to ½ far off (P5); being
  situated, the measure dx·dy/(x² + y²), log-polar (P6); the drawings V = cH a hyperbolic line, levels its distance (P7).
  Run 1 killed P2 and P5 by my set-up (60-digit quadratures of densities singular at an end); run 2 at 200 digits, nothing
  killed. Run 3 (`jay/jay2.py`, R244): P8, location and scale have two Haar measures (1/a², 1/a), the reader's
  commuting group one (1/λ), the exchange keeping it; not killed. "Since 1973" in the plan: what later work did.
  `wwp-plan.md` (+ `wwp/wwp.py`, `wwp/wwp2.py`, 14 Oct; SPN R245): von Mises's water and wine, 1/3 ≤ x ≤ 3, P(x ≤ 2),
  exact. The literature read first (Mikkelson 5/6, Burock 0.764 via Gerville-Réache, Parker and Jeynes 0.816). Every
  fair law puts P(x ≤ 1) = ½, the corner (P2); one party's unit leaves the powers, the exchange picks dx/x (P1). Run 1
  killed P3: the mean of 5/8 and 15/16 also keeps its value under the unit. Run 2 with Jaynes's restriction rule (one
  law, its restriction the law on the smaller range): only the levels, ln 6/ln 9 ≈ 0.8155 (P3′ not killed). Jaynes's
  unbounded form: 1 − log₂ 3/L on [1, 2^L], the range held the missing number (P4).
  `mgp-plan.md` (+ `mgp/mgp.py`, `mgp/mgp2.py`, 14 Oct; SPN R246): the marginalization paradox, exact (both reasoners'
  likelihoods by quadrature). Stone and Dawid's exponentials, DSZ's change point and normal (μ/σ): agreement only at the
  nuisance's dη/η (P1–P3); the gamma killed P4 (other powers move the prior instead of producing the paradox); Weibull
  P4′ not killed. General: under dη/η integrating the scale out is ℓ₁^(−n) times the ratios' law. Runs take 57 and 35
  minutes.
  `tpi-plan.md` (+ `tpi/tpi.py`, `tpi/catalogue.md`, 14–15 Oct; Tom: "Possibly anytime 2/PI shows up, its the situated
  situation."; "its probably the best clue there is. there are many more examples of 2/PI showing up."; SPN R251): where
  2/π shows up. Twenty occurrences known beforehand and forty-five found by a fresh agent (not shown the predictions),
  each constant computed from its derivation step (63 checks of 62, all match; Wheeler's microstrip not traced).
  Fifty-five come from an even turn read as a shadow or a share (43 explicit, 12 via an equal-spread normal pair or a
  Haar measure). P1 killed by eight: the circle as a shape (semicircle area or arcsine integral: Hertz line contact,
  Wigner, disc capacitance, Sneddon cone, Oliver–Pharr, stress drop, rotational broadening) and one pole (alternating
  permutations); P2 killed (KT's 2 a dimension, the Gaussian beam's a convention); P3 killed (in space: axis shadow ½,
  relative angle π/4, half-angle chord 2/3); P4 not killed. Run 1 had three quadrature set-up errors of mine (P3 killed
  by one). A strong clue for the even turn, not by itself for the situated reader. Run 3 (`tpi/run3.py`,
  `tpi/classification.md`; Tom: "the other definining characteristic of the situated view is V is not known."; SPN
  R252): a second blind agent classed all 65 on where π enters and how each is used. P5 killed (51 of 63 agree with run
  2's routes; six disagreements are the hidden turns, put by my question at their Gaussian or Gamma constant), P6 not
  killed (all seven shape entries fix their extent in advance: V known), P7 killed the other way (13 of 51 turn formulas
  infer an unknown, 4 of 7 shape ones). The marks sort derivations, not uses; the best cases are turn formulas reading a
  missing whole through a shadow or a sign. Run 4 (`tpi/run4.py`, `tpi/classification-q3.md`; Tom: "there also needs to
  be a sweep, not ust an equation."; SPN R253): the same classifier asked whether the angle is traversed in order, held
  at once, or not traversed. P8 not killed (no shape entry or identity has a sweep); P9 killed: only the averaging AC
  meter and the relay's describing function carry all three marks, the inner reading as an instrument; ten if a
  population held at once (the parallel reader) counts, which is Tom's to rule. Then Tom: "2/PI  is needed to turn the
  arc into the chord, you want remove the curve and ge the straight line for some reason." (SPN R254): OFS §3.4 read
  the other way (the line of 1 over the arc of π/2); a reading, untested, covering the four forms and the shape group
  (a semicircle's area is ½·r·arc), KT, the Gaussian beam and the pole left over; Claude's candidate purpose a mean
  (the readings v/h have none, their shadows 2/π). Run 5 offered, not run. `tpi-report.md` (15 Oct; Tom: "wrie. a report. Maybe a sweep is
  the better clue, there needs to b a horizon and a sweep over it.."; SPN R255): the four runs and R251–R254 in one
  place, the 65 with their marks; the suggestion read as OFS Theorem 6(e) (a fair sweep reaching the horizon: median at
  the corner, no mean, on every path; 2/π only the circle's), its unbounded face classical (lighthouse, resonance,
  the ground from a height, inverted parallax); a horizon test proposed, not run; open: which horizon, populations,
  whose sweep. Run 4's counts corrected (the 13 equations are among the 30 not traversed). Its §7 (SPN R256; Tom: "where is the
  cauchy in the light house, where is the removal of the scale?"): (x − α)/β = tan θ; the scale removed within each flash
  (the path cancels from its two legs, OFS Theorem 6(a)) and found again at the corner by the shore (half the
  interquartile range), never by the mean; the straight shore makes the Cauchy; the lamp situated, the shore not. "V = H
  on the beach" (SPN R257; Tom: "can we show that V = H in the ligiht house metaphore?"): isotropy draws it for the lamp
  (Proposition 3(e)); the shore tests it with one outside amount (Proposition 5(d): read on a ruler c times the sea's,
  P(R ≤ r) = (2/π)·arctan(cr), the corner only at c = 1); a plate carrée chart is c = sec(latitude), Mercator's c = 1;
  c (a stretch, required 1) kept apart from κ = β/H (a zoom, free). Then Tom: "all we need for this paper is to complete the well
  known metaphors of the mercator and lighthouses. If we can show that V must equal H in those to situations, that's
  enough for this paper." (SPN R258): moved into OFS Proposition 5(f), (g) and SPN §2.1 (see the OFS entry).
  `opn-plan.md` (+ `ofs/opening.py`, 11 Oct): how shapes open into the fisheye, for OFS §7.4 (SPN §2.4's 73-shape run repeated on
  exact shapes): laid by direction every shape gives the circle's (0.5, 1, 2/π, 2/π); laid along its outline, swap-symmetric
  shapes keep corner and middle and differ at the ends (square 0.500, astroid 3.15), the ellipse b = 2 moves its corner (not killed).
  `omm-plan.md` (10 Oct, plan only, nothing worked): taking D6 forward (Tom's 23 Sep status note, Ω_m = ψ₁ψ₂ = 1/π, not
  in this repo; Tom: "it was set aside because we had gone as far we could at the time"). Stage 1 rederives the share in
  current terms (ψ₁ = 2/π as the sweep's average fill of h, ψ₂ = ½ as one facing; rulings needed); stage 2 rules what
  matter and dark energy are on the lay (candidate: payload and addresses); stage 3 compares with Planck and DESI DR2
  only after both stand. The archived ψ₁ paper is not used.
  `part-one-audit.md` checks SPN Part I's proofs and numbers (6 Oct 2026): sound,
  with six fixes, applied to SPN on 6 Oct (marked *Corrected* there).
  `near-far-classification.md` answers one of its open questions: which near/far
  laws are fair to the facings (shares of a two-part split are; components are not).
  `horizon-recursion.md` (+ `spiral/`): the horizon with no preferred rung forces
  recursion; each octave a quarter turn for any ratio; the reading a logarithmic
  spiral (situations 1–2 the circle, k = 0). In SPN §3.3 as Propositions 3.11–3.13.
  `wavelets.md` (+ `wavelets/`): the system on one page, and what filters, wavelets
  and hearing scales already have of it (much), and what the situated view adds.
  `resolution-recursion.md` (+ `spiral/resolution.py`): a reader of finite resolution
  facing a horizon must zoom without end, and far out every zoom is alike ((R) from the
  fisheye's tail); the quarter turn per level is still a premise. Unruled.
  `normalizations.md` (+ `normalizations/`): one relation divided by h (odds), by v + h
  (probability) and by the whole (the circle); two bells with dyadic tails; dividing by a noisy h
  gives a Cauchy tail. A reading.
  `neighbours.md`: who else works near this (a first search, 7 Oct): Gilinsky's perceived
  distance is the normalization by the sum, Schwartz's V1 map proportion-then-log; Barth and
  Paladino's proportion judgment bears on NLE.
  `standpoint-axis.md` (+ `standpoint/`): a second axis, the standpoint (nowhere,
  outside, inside) beside the breadths known; the hemisphere observer as outside with
  the breadths known. Superseded by Tom's situations list 0–4 (SPN §2.1).

SPN's situations, since 6 Oct 2026 (Tom): 0 nothing known; 1 the circle; 2 shapes;
3 parallel, one hemisphere counted (outside); 4 serial, one point at a time
(inside); 3 and 4 possibly approximate. Since 15 Oct (SPN R266; Tom: "situation 3 describes the vantage, reading the outer
hemisphere. situation 4 describes reading the inner hemisphere. the exact mechanism has not been pinned down for
either."): 3 and 4 are the outer and inner hemispheres; parallel and serial are the proposed mechanism, not the
definition (OFS §3.1, "Vantage, not mechanism"; §11.2 question 8). Since 14 Oct (SPN R239; Tom: "we should expand the readers situations. to
accomodate V2"; "i'm open to how to organize the situations, or relations"): the relations come first (h, v, v₂ each in
[0, 1] with its breadth, known unsituated, unknown situated; the situated reader draws V = V₂ = H, giving the set of every
[h, v, v₂]), and a situation is one entry per other party, 1 to 4 each; the five are the one-party case, 0 stays one
case; with V₂: both known, half-situated, (3, 3) a camera, (4, 4), and the mixed scanners (3, 4) and (4, 3) (OFS §3.1,
"Two other parties"). SPN uses these numbers throughout
(converted 6 Oct), except in quotations, Appendix A's rulings and the earlier table in
§2.1, which keep the old ones (old 3 = 3 and 4, old 4 = 0, old 5 = 3 or 4 approximately).
SPN §2.1 opens with "The five, in brief". Keep to the core: the sweep
(any two points; g from 0 to 1, the corner at ½; an angle, 0 to 90°, only in 1 and 2,
where nothing is situated), the level (home, corner, far wall; 2h in place; the next
level nests in the back half), dyadic levels (one doubling apart: the layout's rule,
not derived), and the logarithmic spiral as a drawing of the levels. Since 6 Oct
(Tom) SPN says "level" and "dyadic", not "octave", except in quotations, the musical
octave and R172's "octave with two facings".

The repo is public, so the papers can be read on GitHub; the owner is fine with
that for now (6 Oct 2026) and will decide later where they live. They are still
kept off the Pages site. Don't move or remove them without asking.

## Read this first: keep the case of h, v, H, V
Since 9 Oct 2026 (Tom): lowercase **h, v** are **unit relations**, 0 to 1 (h relates to H, v to V): the geometry,
scale-free. A relation requires two unit relations; a circle has two, a sphere three (Tom, 11 Oct, SPN R204: "I don't
like the term fill levels"). The papers, the pages and this file were converted on 11 Oct; the plans and the archive keep "fill level".
Uppercase **H, V** are breadths, written with the amounts (H the reader's, V the other's); with the distance **d**, a size **Δ** and the
reader's step **ε**, the physics. Since 13 Oct (SPN R226; Tom: "Even H is not a real breadth, Its the value needed to
kick off the system"; "how many relations are included in the systems definition, determine its shape"): no breadth in
the geometry is a measured size. H is the one value the reader chooses to start the system, any value, its size setting
only the zoom (small H fine near, large H fine far); V is the other party's whole as drawn, at H; **V*** is a party's
true breadth, an amount never read. The geometry is a shape and one H, the shape set by how many unit relations the
system includes (two the circle, three the sphere, n + 1 the sphere in n + 1 dimensions). Never read v as V or v/h as V/H ((v·V)/(h·H) = (v/h)·(V/H)); the only bridge is a fill
level times its breadth, where that breadth is known. Before verifying, editing or summarising any paper, plan or lab,
check each symbol's case and domain, and name the bridge for any conclusion that crosses from geometry to physics. Text
before 9 Oct often conflates them (SPN's opening warning and §1, "H and h kept apart"; `plans/vh-rulings-review.md`,
`plans/physics-vh-audit.md`). "The corner" is h = v, which has no scale; a point set by amounts (one step across, a photon
count) is physics (the resolution limit), not the corner.
Where things stand (SPN §1 opens with "The settled view, 9 October"; read it before working on the papers):
- The sweep is every way h and v relate, from all of H to all of V; v fills against a full h up to the corner, then h
  empties against a full v. Any two parties have a sweep: name the pair before saying "the corner".
- The corner h = v is found by every reader (geometry). It is at 45° because the facing (the second degree of freedom a
  straight line lacks) is square to the line there; facing = 2θ (`facing.html`).
- V = H is a calibration a situated reader must set to read amounts, not part of the geometry; under it amounts equal fill
  levels numerically, which is why the conflation is easy. (*10 October*, R188: Tom restores 8 October's reading, V = H
  creates the unit circle, and that is why the levels are plain doublings; R189: "v needs no V" stands, v and h on [0, 1]
  invariant, and there is one circle, its shape from the unit relations, its unit from V = H; SPN §1, "The settled view,
  10 October".) Every amount is then off by V/H, the same on both sides of the
  corner; physics' bridges (travel, a known constant, a known kind, a shared fact) remedy it (SPN Part II).
  (*12 October*, R215: the drawing V = H is **required** in situated geometry: only with all of h and all of v drawn at
  one length is the sweep a turn, the circle traced and the even turn one turn, and only then are the readings the
  Cauchy with its median at the corner; proved forward and back from the known Cauchy, OFS Proposition 3(e) and 5(d).
  What stays arbitrary is the estimate of the other's true size, a pan in levels.)
- The fisheye is the sweep in one facing, seen from the standpoint (geometry, the same for every shape); with V = H it is
  the situated fisheye reading.
- One corner (10 October, R188): the split between the first level (home to the corner, the near field) and the second;
  past it the levels are plain doublings with no corner of their own, and there is no depth and no recursion. R175 and
  R180 are superseded; the superseded passages stay in SPN as the record with dated notes.
- The ratio 2 between levels: dissolved (10 October, R189; Tom: "its just logrithimic doublings. this paper does. not need
  to prove the logrithm, it is fundemental"); Appendix D and the open question are kept as the record.
- Proposition 1.2 (11 October, R190; refined 12 October, R212, R215): from the two-party relation and one chosen H, the
  other party must be assigned a breadth, and the turn requires it drawn at H: V = H is required (R215, superseding
  R212's "not forced"; with c ≠ 1 no turn, no circle, and "even" splits three ways, only one a Cauchy at the corner; OFS
  Proposition 3(e), 5(d), "Working back from the Cauchy"). No unit relation and no single reading depends on c. What
  stays arbitrary is the estimate of the other's true size, cH, best at the median of what the reader knows (the corner
  √(V₋V₊) of any bounds; H with nothing either way; OFS Proposition 13, "the best estimate is the median"). The price of
  a geometry (R214): designating the other party, drawn at V = H, is free and gives the geometry; sizing it is the one
  arbitrary number, corrected by a pan in levels when an outside amount arrives; re-sizing is not zooming. The corner and the
  flip follow from the cap at 1; the logarithm past the corner follows when no rung is preferred, so the reader's lay is
  1 + ln s by address count; by length reality is 2H (the in-place lay, 2 − 1/s, the reader's own); two address spaces, proportional and logarithmic,
  around the corner; the count is the LOD; H is a zoom, not an escape (a large H loses the small below one address; the
  best H puts the thing read at the corner). Still assumed: no measure on a level.
- With two other parties (13 October, R220, R221): a sphere that places every place by its direction and distance needs
  every distance, the size of the universe: the unsituated reader's. The situated reader sets V = V₂ = H, makes one wedge
  per observation, and its even measure is the two-dimensional Cauchy: every pair keeps its corner, the near field in both
  readings is a third (OFS Propositions 3(f), 5(e)). A rotatable sphere's rays point every point of a cube of any size,
  the address the same at every size; the point in amounts needs the cube's extent (OFS §9, "A sphere in a cube").
  With n other parties (R225) the same, once per party: every pair keeps its corner, the near field in all readings is
  1/(n + 1). The drawing is the geometry's whole job (Tom: "from the geometry's perspective, its job is done, what ever
  the true breadth makes no difference"); the true breadths enter only the amounts.
- The unsituated view is the chord, the situated view is the arc, and the chord is prior to the circle (14 October,
  R233, R234): the arc is drawn by the head's turn, not walked; with no turn there is only the chord, needing just the
  two parties and their sum; the circle is the arc over every facing, drawn on the chord after it.
- One unsituated view and many situated ones (14 October, R236, R237): the sum h + v + v₂ + … = 1 needs no standpoint;
  every other drawing is built from a standpoint's sweeps, the altitude (H to V) and the azimuth (V₂), as horizon
  coordinates; the outer and inner hemispheres are two situated views among many. The truth is the sum (R238): the true
  breadths as shares are a point of it; the reader sets H (the zoom) and draws V = V₂ = H, the sum's centre, the triple
  corner, and the entire geometry follows; the truth lies off the centre by V*/H and V₂*/H. The situations follow the
  relations (R239): one entry per other party, the five the one-party case. The reader's space is the wedge, not a sphere (R240): a
  relation is never negative, so a sphere's other octants are only facings; seen from home it is the sum's triangle.
  The situated view is over huge data (R241): a dataset's columns are the parties, a row's ratios its direction and its
  total its depth; the reader holds a window round the hand and the rest as totals. Position, then sweep (R242): one
  rotation places the wedge on the sphere, the hand sweeps inside it; the readings are the same at every position, and
  only a frame fixed outside, the sphere's, records it.
- Building on Jaynes (14 October, R243; corrected R247): the method is his principle of transformation groups, the
  measure a group of undetectable transformations leaves unchanged. The reader's ignorance, as chosen: its attitude θ
  (turns), the other's size κ = V*/H (rescalings) and which unit relation a reading was divided by (the exchange, on
  readings and drawings, not on κ). Turns and rescalings leave dθ·dκ/κ. Given the sweep is a rigid bar's turn, the turns
  give the even turn (the Cauchy at i); the exchange gives the corner and, on the law of readings, V = H; dκ/κ gives the
  estimate's median and, through amounts, motivates (S). Situated means no translations (Jaynes's straw-thrower keeps them): from home the
  measure is log-polar. What is ours: the group (chosen, not derived), the corner and near field, and the measure read as
  addresses, not belief. Further anchors go beside Jaynes.
- Not even H is a measured size (13 October, R226): it is the value the reader chooses to start the system, any value,
  its size only the zoom. The geometry needs a shape and one H; the shape is set by how many unit relations the system
  includes. V is the drawn whole (at H), V* the true breadth. A unit is a relation measured beforehand (R230): its
  value matters to a lone reader only because its addresses are finite (a zoom), and between readers it is agreed.
  If it is unitless, it is geometric (R231): a thing given in terms of something else in view carries no unit; given
  in terms of an agreed unit, its second term was measured beforehand, and that is physics.
  Then physics assigns the values (R227; Tom: "once the
  geometry is defined, physics assigns the values of the placeholders. geometry is agnostic to that step"), as
  multipliers on the amounts, never redrawing a whole; the values decide only where things land, the zoom.
- Still open: the weight on the sweep is a choice (SPN §14, "Burdens of proof"). Since R217 the main result's core does
  not rest on it: any fair weight that does not vanish at the horizon puts the median at the corner and leaves no mean
  (OFS Theorem 6(e)); only the Cauchy's exact shape is the even turn's.

## Read this first: the physics comes first
Since 10 Oct 2026 (Tom: "wanderer priority was user experience, not physics. the physics then became unexpextedly
interesting. we should do the correct physics testing, UI is secondary or even not needed"):
- **Real data or exact mathematics, never wander's world, as evidence.** The flying page and its bodies (`res/`) were made
  for looks; they illustrate, they do not test. A correspondence is tested on published measurements, or on arithmetic
  checked to the last digit (`plans/ref-plan.md`, run 1, is the example of what not to count).
- **Prediction first, from the theory alone**, with the bridge from unit relations to amounts named (see "keep the case").
- **No page needed.** A test is a plan, a script and an entry in the papers; a demo only where it helps to see.
- **Data.** Until 14 Oct 2026 the cloud environment's network access was the default, Trusted, which reaches GitHub, PyPI
  and npm but not the astronomy archives (VizieR, CDS, ESA), arXiv, Wikipedia or the CDNs (jsDelivr, unpkg, cdnjs). On
  14 Oct Tom set it to Full (at claude.ai/code: the cloud button above the message box, the environment's gear, Network
  access); VizieR, arXiv and jsDelivr then answered. The smoke test still serves three.js from `node_modules`; GitHub's CI
  runner reaches the CDNs. Record each dataset's source, licence and sha256 in its plan, and do not commit large data.

## Read this first: THE LAB GUIDE
The labs have their own rules, written in `labs.html`. Read two comments
before touching anything lab-related:
- **THE LAB GUIDE**, at the top of the lab section of the script
- **THE LAB BUDGET** comment, before `#labPane`

In short:
- A lab's prediction and kill condition are written into its note **before** it
  runs.
- A killed run stays recorded as killed. A fix is a new run with its own
  prediction; never edit an old prediction to fit.
- After every change, run `labs.html?lab=all` (or its "run every lab"). A
  lab going from "not killed" to "killed" or "error" means something broke; fix
  that before adding anything.

## Testing
- `npm test` runs `tests/smoke.mjs` in headless Chromium:
  1. **Fly:** presses Fly, looks around, flies and taps a body. Then the bodies load and wear
     their files, and moving about works: holding W gathers speed (5 to 30 a second) and
     letting go glides; a tap beside a small planet takes it, going round brings it to about
     40° across, and, once that approach has settled, zooming brings it nearer by its distance (`where().dist`; never closer than 1.35 of its radius).
  2. **Labs:** runs `labs.html?lab=all` (a few minutes; TMP and TRK are the slow ones).
  3. **labs.html:** a card per lab, BAL run from its button, and `index.html?lab=`
     forwarding to `labs.html`.
  4. **sweep.html:** every example lays on the sweep, and the cursor sweeps.
  5. **dial.html:** a sure "two" costs about 3, 2 and 3 at s = 0.5, 1 and 2 (least at one pixel across).
  6. **sphere.html:** the address is the same at any scale, the octant's area is π/2, and the body's bands are off far
     away and on close up.
  7. **demos.html:** every page it links to is there, and the flying page's "demos" button opens it.
  8. **thin.html:** grains lit × brightest grain is the light caught, 1/v² everywhere; near full brightness, far one grain dimming 4× per doubling.
  9. **ladder.html:** parallax gives out by 30,000, width by 400,000, light reads past both (and gives out with photons counted).
  10. **sky.html:** the lit share within 0.01 of 1 − e^(−L/λ); always been, the whole sky lit.
  11. **Gameplay sketches:** each page's one mechanic through its hook (dimming, stages, the ladder's locks and light, the
      sky's count read back as time, a half-ball cut 30° near and far; trick shots: the preview is the shot, contacts exactly on
      h + v = 1 (but for a few in clusters, within 1%), the row of four's pot out of sight at 3 deep and in sight at 4, a bare tip
      turning the white 30° at f = ½, spin's textbook results, throw both ways, spin passed on, a massé bending, a jump clearing a ball,
      backspin passed and follow lessened by the grip, a ball jumped off the table; every challenge missed as set up and
      solved by its reference shot, a missed try put back and a solved one counted; the throw challenge missed with the
      grip off; a shot played through heard, the cue's tap, a contact and a pocket; the pull strip shooting at middling power).
  12. **facing.html:** the facing is 90° at the corner, 0° at A, 180° at B; the arc stands off the line 1 − 1/√2 there, its most.
  13. **levels.html:** by default the reader's lay, every level past the corner ln 2 wide, s = 8 at 1 + ln 8, six drawn; at
      `?lay=inplace` the near field in proportion, each level past the corner half the width of the last (s = 8 at 1.875),
      and one level fewer seen per doubling of the grain; the shape crosses ring edges, its broad form fewer; with the size divided out
      the depth averages 0 on the corner; a body from res/ chosen in the combo box crosses ring edges, a non-.tvf file refused; a draw .tvf curve read
      from its centroid (a 5-pointed star's tip over its dip as drawn).
  14. **walk.html:** 45° at d = V; far, v fills against a full h, near, h empties; steps per level V, 2V, 4V, …; steps left V·cot θ.
  15. **pool.html:** a break played from inside: every contact on h + v = 1, one reading alone decides only with all balls alike, the game the referee's;
      with cushions read as the ball's mirror image and pockets as filling the view, still the referee's game; read late (c = 50),
      carrying the image forward beats taking it as now.
  16. **flight.html:** the corner keeps its row from 50 m to 1.6 km; by v/h the level edges keep theirs, the first edge the corner,
      8 lines a level; by metres the edges slide; a post is recovered exactly with no step, within 10% at 2v at a pixel step, worse at 8v, a bearing only at 400v; the lay true to the corner, each doubling past it ln 2 wide; the strip folded holds 0.1v–100v, h/v throughout runs off the top, v/h off the bottom.
  17. **pool-infinite.html:** the books balance through 2 s and a pan, the window holds the world's density, the work for a world
      16 times wider within 10%, and zoomed out the window stops growing.
  18. **mountain.html:** the range's ends at 45°, 18 of 36 fingers on it, the same at a thousand times the scale; mountain
      equals thumb reads 1 mi at 0.5 mi, off by 20, log₂ 20 doublings; one thumb walked recovers d = 10 and V = 20; the
      two vantages on the thumb π/2 × 2/π = 1 (the 36 fingers' mean shadow within 0.001 of 2/π), to the ends at 45°
      1.1107 × 0.9003 = 1, the same at a thousand times the scale.

  19. **play-marbles.html:** the pour of 500 at rest in the bowl, the bowl and table carrying the weight within 1%; the arc seen
      ahead ends at its first contact; a throw near the rim knocks marbles out and is heard (glass, bowl, felt); the pull
      strip throws.
  20. **zoom.html:** the held window the same width in levels at every H (17 on the reader's lay, 10 on the in-place at
      n = 32, L = 12); doubling H shifts the levels exactly; addresses per level 4, 8, 16 inward, n·ln 2 past the corner,
      the in-place lay mirrored (4, 8, 16, 16, 8, 4); a cluster told apart at the corner and lost into home under a large
      H; detail absolute inside the corner, relative past it.
  21. **parallax.html:** the error per step 1 at the corner and 2.125 two levels either side, the same at k and 1/k; the
      band 10.966 levels each side at ε = 10⁻³; the error round at the corner, stretched by d/(B/2) elsewhere; one reader
      alone holding only rays.
  22. **sphere-cube.html:** every point of a turning sphere lands on one point of a cube and comes back to rounding at
      e = 10⁻³, ½ and 1, the address the same at every extent, the face its largest component's; the even sphere gives each
      face a sixth, a face's middle quarter 38%, the wedge's faces a third each; with the extent unknown the readout says
      off by e/H; WebGL drew frames (three.js served from `node_modules` in place of the CDN); step 7, the two sweeps:
      v₂/h = tan z and v/√(h² + v₂²) = tan a, even in both angles v ≤ h 0.3426 and h largest 0.2326, even over the wedge
      ½ and ⅓ (the 1,600 drawn within 0.02), the top quarter of height 25% of the even wedge, Lambert's map equal-area;
      the truth for V*/H = 3, V₂*/H = ½ at (2/9, 2/3, 1/9) and the drawing at the centre (⅓, ⅓, ⅓).
  23. **paths.html:** the share of the sweep measured along each path (as chords) is its closed form; all three fair and ½
      at the corner, 0.250, 0.293, 0.207 at 22.5°; the mean climbing ρ(0)·ln 10 a tenfold on each; sin² 2θ with its
      median at the corner and the mean 4/π; π/2 and 2/π at the horizon, product 1; v/h = ∞ at 90°.
  24. **h-limits.html:** past the world's ends the number line, the logarithm and the reciprocal exactly, a corner only
      with H inside; the world lost whole into home, past the edge, into the horizon at the thresholds; 24 and 17
      addresses at H = 1; a pair best told apart at √(x₁x₂), arcsin(1/3) for r = 2; one object's detail flat past the
      corner on the reader's lay, nΔ/H inside, most on the in-place lay at √(x(x + Δ)); with unlimited addresses all
      31 held apart at every H.
  25. **h-chain.html:** one reader's even sweep gives back the unit circle for every figure and size; two standpoints 2H
      apart hold all 72 points at the best H and none at 10⁻³ or 10³; H of 0 or one standpoint, only rays; five parties,
      the near field 1/6; physics relabels and nothing moves.
  26. **wedge.html:** from home the three parties at an equilateral triangle's corners and every direction at its shares
      (to rounding), the pairs' corners its medians; Lambert's map: six chambers a sixth each, v = h halving it, the
      corners meeting at v = 1/√3; H moves every thing along its own ray, never across, merging more into home as it
      grows and leaving more past the edge as it shrinks; every situation reaches every direction in one scan, holding
      1, 1/24, 1/24, 1/576 of the wedge at once; the drawing at the centre, (0.2, 0.6, 0.2) with V known, the truth with
      both known; step 7: positions round-trip through (longitude, latitude, turn), the hand on the sphere is R·d, the
      eight octants tile the sphere (3,000 directions, each in exactly one), the octahedron's 24 turns put the wedge on each
      octant three times, an even turn's wedge holds an eighth of 40,000 even directions within 0.01, and from home the
      wedge's points land in the same place at two positions.
  27. **wedge-browse.html:** 2⁵³ − 1 items, every halving's two counts adding exactly (200 descents to the finest
      address); the drawn cells and items adding to all of them in five states; at w = 1 and the drawing at 0 the view
      the wedge itself; the gold at tan 1 for a second moves the blue 0.4 in rapidity, letting go re-centres on it; the
      radius keeps the blue's place, or moves the window to it; items found by index in their finest cells; item
      4,503,599,627,370,495 at the triple corner with its total at the corner; from home nothing moves with H.

  It fails on an uncaught error, or on a lab returning "error" or no verdict.
  "Killed" is listed but doesn't fail the run, because the page treats it as a
  recorded result. When this was set up, WOB, ELV and EQV were the killed ones.
- Run `npm test` before every PR.

## Related repos
games, draw, 3d and flare are the owner's other projects. wander doesn't depend
on any of them.
