# Where the corner on the focus might be useful: games and simulations

*25 October 2026. SPN R502–R505. Tom: "the insight might be useful for FPV games."; "i'm intrested in the geometry, not
realism."; of OFS: "No, keep it out ofs. this is just a playground to see how it might be used. what is worth
exploring?"; then "proceed. create a note that saves your insights about where this might be useful in games and
simulations."*

A note, not a ruling and not OFS. It gathers what FPV (`plans/fpv-plan.md`, runs 1–2) and the two pages (`focus.html`,
`fpv.html`) suggest for games and simulations. Each idea is marked:
- **shown**: checked exactly in FPV;
- **known**: already engineering practice under another name;
- **guess**: untested, a direction for the playground.

Nothing here says a game should do it. That would need a renderer, real scenes and players, none of which we have tested.

## The one idea

Hold a fixed count K of addresses in depth (and in direction) and lay them by the turn with its corner on the thing in
focus: H = the focus's distance, the crosshair the direction corner. Then:

- **The focus gets the finest cell there is, π/K of its own distance, whatever the scene's range.** No near or far plane
  enters. *(shown, G1)*
- **Detail falls off in levels on both sides of the focus, in mirror image.** A thing at half the focus's distance is held
  exactly as coarsely as one at twice it (the edges map onto themselves under d ↦ f²/d). This is the departure from
  practice, where nearest is finest. *(shown, G2)*
- **Refocusing slides everything in levels and changes nothing else:** order, level differences and cross ratios are
  kept. *(shown, G5; known from draw's TFE)*

## Where it might be used

### 1. Depth precision (the depth buffer)
- The standard 24-bit buffer is the in-place lay with its corner at the near plane: finest at the near plane and
  hopeless far out. *(known, DPR)*
- Log depth and reversed-Z floats are nearly even in levels everywhere: no focus at all. *(known)*
- **The turn at the focus**:
  - against log depth over a range of 10⁷, finer by ln(X/n)/π = 5.13 at the focus, and finer within ±2.3 nats
    (3.3 doublings); *(shown, G1, G3)*
  - at 32 bits, 97 times finer than reversed-Z at the focus, and finer for about 7 doublings either way. *(shown, G7)*
- **Where it could pay:**
  - **Decals and coplanar surfaces on the thing aimed at.** Z-fighting there is a grain problem: two surfaces at a
    ratio r are told apart only if r is wider than the cell, (1 + tan(π/4K))/(1 − tan(π/4K)) at the corner. *(shown, the
    twins; guess that it matters in practice)*
  - **Huge ranges with one thing that matters:** space games, planet-to-surface flight, astronomy viewers.
    *(guess)*
- **Costs:**
  - Every frame's depth is laid by that frame's focus, so depths stored from earlier frames (temporal anti-aliasing,
    reprojection, shadow caches) must be re-laid. The re-laying is exact (a slide in levels), but it is work.
    *(shown that the map is a slide; guess about the cost)*
  - With the focus at the scene's edge, half of K is wasted beyond the near or far plane. Under 2% for a focus anywhere
    in [64n, X/64]. *(shown, G6)*

### 2. Level of detail by levels from the focus
- Mesh, texture and shader detail set by a thing's cell rather than its distance from the camera:
  - full detail at the focus distance, coarser in both directions;
  - the number of detail levels a scene needs is about log₂ of its range over the focus, plus the focus's own.
    *(guess; FOV gives the least count ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉ for an extent about the gaze, shown)*
- Screen-size LOD already does most of this for far things. *(known)* What the corner adds is near things coarsened
  too.
- **It would collide with practice where near things matter for reasons of their own:** collision, the player's hands,
  anything that fills the screen. Two rules side by side is the likely shape: screen size for how many pixels, the
  focus for how much attention. *(guess)*

### 3. Simulation level of detail (fidelity, tick rate, AI)
- The same allocation for what is computed, not drawn:
  - physics substeps, AI think rates, crowd and traffic fidelity and network update rates (an MMO's area of interest)
    set by levels from the focus;
  - fine where the player looks and acts, coarse in both directions. *(guess)*
- The pool runs warn about a limit: what travels toward the reader must be held at its own size until it arrives
  (POL runs 16–18, a pulse lost in a coarse far cell). Focus-centred fidelity fits what stays put, not what is
  incoming. *(shown in POL; applies here as a guess)*

### 4. Flying at the target: a budget known in advance
- With H locked on the target and the eye closing at speed u:
  - the target never moves in the addresses;
  - the world beyond streams through the corner's cells at K/(πτ) a unit time (τ = d/u, the time to contact), falling as
    sech of the levels away from it;
  - things between stream toward home. *(shown, FPV run 2)*
- So the rate at which detail must be refreshed is read off the game's own τ, highest at the crosshair, before anything
  is drawn. Streaming and LOD transitions could be scheduled from it. *(guess)*
- Flight sims: `flight.html` showed the corner holding one screen row at every height when the corner is the eye's
  height. The ground-to-sky transition may be easier to lay by levels from there. *(shown in FLIGHT's page; guess for
  games)*

### 5. Where to look next: streaming and prefetch
- Corollary 6.1(c): the expected travel to the next look is least from the median of where the next look will be, on
  every ruler. So prefetch, cache and stream around the median of the likely next targets, not the current one and not
  the screen's centre. *(shown as geometry; guess as policy)*
- Kept at the focus, the turn beats log depth on average while the next look stays within ±3.6 nats of it. *(shown,
  G4)*

### 6. Two things at once
- With one corner and two targets (the crosshair and a tracked enemy), the best H is their geometric mean √(d₁d₂)
  (HKO's). Each target then gets (π/K)·cosh(D/2), with D = ln(d₂/d₁). *(shown, FPV run 3)*
- Two corners, K split at the geometric mean, give each target 4·atan(e^{D/2})/K, never worse than 2π/K. *(shown)*
- **The crossover is at D* = 2.02 nats, a distance ratio of 7.55, about three doublings.** *(shown, FPV runs 3–4)*
  - Nearer together, keep one corner between them.
  - Farther apart, split.
  - Splitting costs at once (first order in D); one corner loses only slowly (second order).
- The two put their worst grain in opposite places: two corners are coarsest between the targets, where one corner is
  finest. If the next look tends to fall between them, one corner keeps its advantage past D*. *(shown as geometry;
  guess as policy)*
- A game could switch on the ratio alone (a single test, d₂/d₁ > 7.55), with some hysteresis (§7). *(guess)*

### 7. When to move the focus
- Moving H every time the crosshair flickers churns every cell. Hysteresis, only moving past some number of levels or
  easing H toward the target, is the practical question a game faces. It is the time version of the next-look rule.
  *(guess)*

### 8. Volumes
- Games already slice the view volume into a 3D grid of cells for clustered lighting and volumetric fog, usually with
  depth slices even in levels. *(known)*
- Laid by the turn in depth, and by equal angles about the crosshair in direction, the triple corner gives a
  "focus cube" of finest cells. *(guess)*
- The flat screen gives the crosshair its coarsest angle (tan α/α of equal angle: 1.27 at 90°). Equal-angle and Panini
  projections already undo part of that. *(shown G8; known)*

### 9. Beyond games
- **Scientific and astronomy viewers** over many decades of scale: one thing studied, the rest context.
- **Robotics and sensing budgets**: a sensor's range resolution centred on the object being grasped or tracked.
- **Data browsers over huge sets**: `wedge-browse.html` and `star-dial.html` already put the corner where the user
  looks.

All guesses, listed for where the same geometry would apply.

## What it does not claim
- It does not claim any game would look or play better; nothing was rendered, timed or played.
- It makes no claim about eyes. The corner on the gaze is a "should" (OFS §8, Corollary 6.1), and FOV's allocation is a
  neighbour of foveation, not evidence for it.
- "Nearest is finest" has reasons: occlusion, collision, screen size. The note proposes a second rule beside it, not a
  replacement.

## Next in the playground
In order:
1. ~~two targets, one corner or two~~ (done: FPV runs 3–4, D* = 2.02 nats);
2. refocus policy over a gaze trace (churn against grain);
3. the focus cube in 3D;
4. a small game with 8–16 depth bands.
