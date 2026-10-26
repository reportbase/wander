# FPV: the corner on the crosshair, in a first-person view

*25 October 2026. Tom, after `focus.html`: "the insight might be useful for FPV games."; then, to a test first and a demo
after, "yes, lets push this idea. i'm intrested in the geometry, not realism." Exact arithmetic; no data; no page. SPN
R502.*

## The question

A first-person view has a crosshair. The focus is the thing under it, at some distance f. OFS §8's Corollary 6.1 says
the reader's corner should sit on the focus: in direction, on the crosshair; in distance, H = f. What does that give a
first-person view, in its geometry alone, against the ways depth and detail are laid now? Above all, what does it cost
(nearer things held coarser than the focus) and what does it buy (a grain at the focus that no near or far plane
enters)?

## Known beforehand

- **DPR** (`plans/dpr-plan.md`, run 1). The standard depth buffer is the in-place lay with its corner at the near plane:
  relative separation (d/n)/K, worse far out than first order. Log depth is the reader's lay at H = n: ln(X/n)/K
  everywhere. Reversed-Z in binary32 is relative 2^(−24) to 2^(−23) at every distance. The scene there: n = 1 m,
  X = 10⁷ m.
- **FOV** (`plans/fov-plan.md`). With the focus as an extent F and fields that only need a factor ρ, the fewest cells
  are ⌈F/δ⌉ + ⌈log_ρ(X/F)⌉; the turn gives the focus about a third of that optimum's fidelity. That was about an
  extent around the gaze; this plan is about the depth and the address grain of the turn itself.
- **OFS §8, Corollary 6.1** (`runs/ofs/focus.py`). The turn's relative cell is (π/2K)(s + 1/s) at s = d/H, least, π/K,
  at s = 1. The expected travel to the next look is least at its median.
- **HKO.** The best H for telling two amounts apart by angle is √(x₁x₂); the widest angle is arcsin((r − 1)/(r + 1)).
- **draw's TFE** ("two fisheyes on one array"). Two focuses on one array are two Möbius charts of one line: positions
  do not transfer between them, cross ratios do. So moving the focus is a change of chart. Classical (Möbius, cross
  ratio).
- **The flat screen.** A rectilinear projection with half field of view α and K pixels across gives each pixel an
  angle of about (2 tan α/K)·cos²φ at φ off the axis: the coarsest at the crosshair. Panini and equi-angular
  projections exist partly to undo this. Classical.

## The set-up

- **Depth only**, the line of sight through the crosshair. A scene from the near plane n = 1 to X = 10⁷ (DPR's), or
  other ranges where named.
- **K addresses** (cells) laid on depth by a scheme. Each scheme's cell edges:
  - **T(f), the turn at the focus.** d_k = f·tan(kπ/2K), k = 0 … K (the last edge at infinity). Needs neither n nor X.
  - **LOG, log depth.** d_k = n·(X/n)^(k/K). Needs n and X.
  - **Z, the standard buffer.** 1/d_k = 1/n − (k/K)(1/n − 1/X). Needs n and X.
- **The measure.** A thing at d lies in one cell [a, b]. Its relative cell is r(d) = (b − a)/√(ab). Every cell edge is
  computed exactly (50-digit mpmath), not estimated.
- **The levels.** x = ln(d/f), in nats; a doubling is ln 2.

## Predictions, before any run

**G1, the focus grain is range-free.**
- For T(f), K even, the cell just below the focus is [f·tan(π/4 − π/2K), f]. Its r is π/K to within 0.1% at
  K = 256, 1024 and 4096. It is the same, to 10⁻⁴⁰, for every f, n and X tried (f = 1, 10³·⁵, 10⁶ with n = 1,
  X = 10⁷; and X/n = 10³).
- At the focus LOG's r is 2·sinh(ln(X/n)/2K) ≈ ln(X/n)/K. The ratio LOG/T at the focus is ln(X/n)/π, to within 1% at
  K = 1024: 5.13 at X/n = 10⁷, 2.20 at 10³.
- Z's r at the focus is about (f/n)(1 − n/X)/K, so T is finer than Z at the focus when f/n > π. At f = n, Z is about
  π times finer than T.
- *Killed* if any of these is off.

**G2, both sides alike.**
- T(f)'s edge set is closed under the reciprocal about f, d ↦ f²/d: every edge's mirror is an edge (to 10⁻⁴⁰), and
  r(f·e^x) = r(f·e^(−x)) for every x tried.
- In the continuum, r(f·e^x) = (π/K)·cosh x, to within 1% at K = 1024, for |x| ≤ 6.
- Z's r rises with d everywhere; LOG's is constant. Neither is symmetric about f.
- *Killed* if any of these fails.

**G3, the band where the turn wins.**
- T(f) is finer than LOG wherever cosh(ln(d/f)) < ln(X/n)/π.
- At X/n = 10⁷ and f = √(nX) that is |x| < acosh(5.13) = 2.32 nats (3.35 doublings) each side: 6.7 doublings of the
  scene's 23.3. At K = 1024, the band's measured edges (where T's discrete cell first exceeds LOG's) lie within one
  cell of the formula.
- *Killed* if an edge is off by more than one cell.

**G4, the next look.**
- Suppose the next focus is spread uniformly in levels over ±L nats about f, and T is kept at f. Then T's mean r over
  that spread is (π/K)·sinh(L)/L. It is below LOG's while sinh(L)/L < ln(X/n)/π.
- At X/n = 10⁷ that holds for L < L* ≈ 3.6 nats (about 5.2 doublings either side). L* is computed exactly in the run;
  the prediction is between 3.5 and 3.7.
- Among focuses H, the mean is least at H = f, the spread's middle (Corollary 6.1(c) on this cost).
- The discrete mean at K = 1024 matches the formula to within 1%.
- *Killed* if L* falls outside [3.5, 3.7], the discrete mean is off by 1%, or the least H is not the middle (to 10⁻⁶
  in levels).

**G5, refocusing changes the grain only.**
- Moving the focus from f to f′ slides every reading s = d/f to s·f/f′: a slide of ln(f/f′) in levels. The order of
  things, their level differences and the cross ratio of any four readings are unchanged (to 10⁻⁴⁰). Known (TFE).
- For two things d₁ < d₂, the addresses between them, K·(2/π)(atan(d₂/f) − atan(d₁/f)), are most at f = √(d₁d₂). There
  they equal (2K/π)·arcsin((r − 1)/(r + 1)), r = d₂/d₁. Known (HKO); checked again here.
- *Killed* if any of these fails.

**G6, what the turn wastes.**
- T(f) puts (2/π)·atan(n/f) of its K addresses before the near plane and 1 − (2/π)·atan(X/f) past the far plane.
- The waste is under 2% for every f in [64n, X/64], about 4·10⁻⁴ at f = √(nX), and about ½ at f = n or f = X.
- *Killed* if any of these fails (the waste counted from the discrete edges, to one address).

**G7, the same 32 bits.**
- Store T(f) as 32-bit fixed point (K = 2³²): w = (2/π)·atan(d/f). At the focus r = π/2³² ≈ 7.31·10⁻¹⁰.
- Reversed-Z binary32 there is 5.96·10⁻⁸ to 1.19·10⁻⁷ (DPR D2). So T is 82 to 163 times finer at the focus.
- T, at (π/2³²)·cosh x, stays finer than reversed-Z's best case (2^(−24)) while cosh x < 2⁸/π: |x| < 5.09 nats
  (7.3 doublings each side). It stays finer than reversed-Z's worst case (2^(−23)) while cosh x < 2⁹/π: |x| < 5.79
  nats (8.4 doublings).
- Exact at d = f·e^x for x = 0, ±5, ±6.
- *Killed* if the ratio at the focus falls outside [82, 164], or the crossings are off by more than 0.05 nats.

**G8, the crosshair in direction (classical).**
- For the flat screen with K pixels over a field of 2α, the angle per pixel at the crosshair over the equal-angle
  screen's 2α/K is tan α/α: 1.273 at 90°, 1.654 at 120°.
- At the edge over the crosshair it is cos²α: ½ at 90°, ¼ at 120°.
- The equal-angle screen (the turn about the crosshair, laid in angle) is the same everywhere.
- Exact for the discrete pixels at K = 1024, to 0.5%.
- *Killed* if not.

## What would follow

If G1–G8 stand, a first-person view gets two corners from its focus.
- **In direction**, the crosshair. The equal-angle screen holds it no worse than the edges; the flat screen holds it
  worst.
- **In distance**, H = f. Its grain at the focus is π/K whatever the scene's range, with no near or far plane chosen.
  It is symmetric in levels about the focus: nearer things are held exactly as coarsely as equally farther ones. That
  is the cost a game pays and the departure from "nearest is finest". It beats log depth within a band of
  ±acosh(ln(X/n)/π) levels, and in expectation for next looks within ±L*. At 32 bits it is about a hundred times
  finer than reversed-Z at the focus, for about seven doublings either side.
- **Refocusing** is a slide in levels: the grain moves, nothing else does.

If G3 or G4 fail, the band or the expectation is not as simple as the cosh, and the demo shows the measured one
instead.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (25 October 2026, `runs/fpv/fpv.py`, output `runs/fpv/fpv-run1.txt`, exact, 4 s)

The script's first pass crashed in G7 (mpmath would not take a `Fraction`), so G7 and G8 did not run. In the same pass,
G6's third check was coded stricter than its prediction: it compared the discrete waste with 4·10⁻⁴ of K, where the
prediction says to one address. Both were fixed in the code before the run recorded here. No prediction was changed.

- **G1 not killed.**
  - The cell below the focus is π/K to 3·10⁻⁵ at K = 256, 2·10⁻⁶ at 1024 and 1·10⁻⁷ at 4096.
  - It is the same at f = 1, 10³·⁵, 10⁶ and 37, to 10⁻⁵¹.
  - LOG/T at the focus is 5.1306 at X/n = 10⁷ (ln(X/n)/π = 5.1305), and 2.1988 at 10³.
  - Against Z: Z is finer at f ≤ 3 (3.14 times at f = n) and T is finer from f = 4. At f = √(nX), Z's cell is 32,000
    times T's.
- **G2 killed in two clauses, both by my set-up.**
  - Its symmetry holds exactly. Every edge's mirror f²/d is an edge (to 10⁻⁴⁸), and r(f·e^x) = r(f·e^(−x)) at every
    x tried.
  - The continuum clause fails from |x| = 3.75. There one cell spans 0.03 to 0.7 nats, so the discrete r is the cell's,
    not the point's: at x = 6, 0.707 against (π/K)·cosh 6 = 0.619. The prediction's "|x| ≤ 6" asked for more than
    K = 1024 holds there. Within |x| ≤ 3.5 it is within 1%.
  - "Z rises everywhere", checked strictly, fails because 15 of 26 steps fall in one cell. Z never falls. At
    K = 1024 the standard buffer's last cell runs from about 1,000 m to 10⁷ m: everything from 10^3.25 up shares it.
- **G3 not killed.** T is first coarser than LOG at x = ±2.3178. The formula gives 2.3187, and a cell there is
  0.016 nats. The band is 6.69 doublings of the scene's 23.25.
- **G4 not killed.**
  - L* = 3.614 nats (5.21 doublings each side).
  - The discrete mean matches (π/K)·sinh L/L to 10⁻⁵ at L = 1 and 2, and to 4·10⁻⁴ at L*, where it equals LOG's
    0.01574.
  - The least mean is at the spread's middle. Moving H 0.05 nats either way raises it by 0.12% each way.
- **G5 not killed.**
  - Refocusing by 6.2 and 15.0 nats keeps the cross ratio (1.0649174) and every level difference, to 10⁻⁴⁰.
  - Most addresses fall between a pair at f = √(d₁d₂) exactly: 766.64 and 982.78, the HKO arcsine. The discrete edge
    counts are 767 and 983.
- **G6 not killed.** The waste is 513 of 1,024 at f = n and f = X. It is 11 (1.07%) at f = 64n and X/64, the most
  within [64n, X/64]. At √(nX) it is 1 (the formula 0.41). Every count is within one address of the formula.
- **G7 not killed.**
  - At the focus T32 is 7.3146·10⁻¹⁰ = π/2³². Reversed-Z there is 7.11·10⁻⁸, 97 times coarser.
  - T32 crosses 2^(−24) at |x| = 5.094 nats (7.35 doublings) and 2^(−23) at 5.787 (8.35), within 0.05 either side.
  - Five nats nearer, reversed-Z is already only 1.13 times coarser; six nats either side it is finer. Reversed-Z's
    float favours the near side slightly, while T is even about the focus.
- **G8 not killed.** At the crosshair the flat screen is 1.2732 times equal-angle at 90° and 1.654 at 120° (tan α/α).
  At the edge over the crosshair it is 0.5005 and 0.2504 (cos²α).

**What it says.**
- A first-person view whose depth addresses are laid by the turn about the focus distance gets a grain of π/K at the
  focus. It needs no near or far plane, and that grain is the same whatever the scene's range.
- The addresses are laid in mirror image about the focus, cell for cell, under d ↦ f²/d. A thing at half the focus's
  distance is held exactly as coarsely as one at twice it. That is the departure from "nearest is finest", and it is
  exact.
- Against log depth over a range of 10⁷ it is 5.13 times finer at the focus and wins within ±2.32 nats (3.3 doublings).
  In expectation it wins for next looks spread within ±3.6 nats.
- At 32 bits it is 97 times finer than reversed-Z at the focus, for about seven doublings either way.
- Refocusing is a slide in levels; it moves only the grain.
- The cost is the far tails and the near ones alike. Coarse past ±5 nats, and half the addresses wasted if the focus
  sits on the scene's edge.
- Classical in its pieces: the tangent's mirror, the arcsine, cosh. What is new here is only the choice of H at the
  focus.

### Run 2: flying at the focus (predictions written 25 October 2026, before the run)

*Tom: "proceed", to the approach first among the playground's next steps ("Fly at a thing with H locked on it").*

The eye moves straight at the focused thing at a steady speed u, and H stays its distance d, so τ = d/u is its time to
contact. Another thing at distance D has s = D/d and level x = ln s. The turn's address is a = (2/π)·atan(s).

- **A1. The level flow.** dx/dt = u/d − u·cos β/D, where β is the angle between the thing and the line of flight.
  - For a thing far beyond the focus (D/d → ∞), this tends to 1/τ: one nat per τ.
  - A thing on the line of flight, nearer than the focus, has dx/dt < 0: it slides toward home in levels.
  - Exact, by differentiating the closed form.
- **A2. The address flow.** da/dt = (1/π)·sech(x)·dx/dt. For things sliding at one level rate it is fastest at the corner.
  For things far beyond the focus it is K/(πτ) cells per unit time at x = 0, falling as sech x away from it. Exact.
- **A3. The focus stays put.** The thing flown at keeps address ½ at every moment of the approach, to rounding.
- **A4. Halving.** Each halving of the target's distance takes τ/2 of the τ read at its start, as MOT run 1 found.
  - A thing fixed in the world, far beyond the focus, crosses one level of x per halving of d.
  - So the world behind the target passes through the corner's cells at K/(πτ), growing as the eye closes.

*Killed* if any identity is off by more than 10⁻²⁰ at 40 digits, or A3's address leaves ½ by more than 10⁻¹².

#### Run 2 (25 October 2026, `runs/fpv/fpv2.py`, output `runs/fpv/fpv-run2.txt`)

Nothing killed.
- **A1.** The level flow, dx/dt = u/d − u·cos β/D, holds at four things to 10⁻⁴³.
  - Far beyond the focus it tends to 1/τ: 0.99312, 0.99993, 0.9999993 and 1 − 7·10⁻¹⁰ (in units of 1/τ) at D = 10⁵,
    10⁷, 10⁹ and 10¹² with d = 700.
  - A thing on the line at 400, nearer than the focus, slides toward home at −6.0/τ.
- **A2.** The address flow da/dt = (1/π)·sech(x)·dx/dt holds to 10⁻⁴⁴. At one level rate 1/τ the cells crossed a unit
  time are 1.397 at the corner (K/(πτ), K = 1024, τ = 233), 0.905 one nat off, 0.371 two off and 0.051 four off.
- **A3.** The target keeps address ½ throughout, to 10⁻⁴¹.
- **A4.** A halving of the target's distance takes τ₀/2, and a thing far beyond moves ln 2 over it, to 10⁻¹².

**What it says.**
- Flying at the focus with H locked on it, the target never moves in the addresses.
- The world beyond the target streams through the corner at one nat per τ: the fastest cell turnover is at the focus,
  K/(πτ), and it falls as sech away.
- Things between the eye and the target stream the other way, toward home.
- A game holding detail by these cells would refresh fastest at the crosshair, at a rate it can read off its own τ. That
  is a budget known in advance, not a measurement.
- Classical in its pieces: Lee's τ, the derivative of atan.

### Run 3: two targets, one corner or two (predictions written 25 October 2026, before the run)

*Tom: "Yes, continue", to the playground's next step in `plans/fpv-games-note.md`: two targets, one corner or two.*

Two things matter at once, at f₁ < f₂, their separation D = ln(f₂/f₁) nats. The reader still has K depth addresses.
The measure is the worse of the two targets' relative cells (cell width over its geometric middle), in the continuum
first. Two ways:
- **One corner**, the turn about some H.
- **Two corners**, K split evenly at m = √(f₁f₂): below m a turn about f₁, its K/2 cells spread over [0, m]; above m a
  turn about f₂, its K/2 cells over [m, ∞). Each turn's angle there is atan(e^{D/2}), so the two halves are mirror images
  about m.

Predictions:
- **B1. One corner.** The best H is √(f₁f₂) (HKO's), and both targets' relative cell is then (π/K)·cosh(D/2). Exact.
- **B2. Two corners.** Each target's relative cell is 4·atan(e^{D/2})/K. Exact.
- **B3. The crossover.** The two are equal at the D* solving π·cosh(D/2) = 4·atan(e^{D/2}). From a hand estimate, D* is
  about 2.0 nats, a distance ratio of about 7.4 (2.9 doublings).
  - Below D*, one corner at the geometric mean is strictly better for both targets.
  - Above D*, two corners are.
- **B4. The limits.**
  - At D = 0 both are π/K.
  - Near 0, one corner's excess is second order, (π/K)(1 + D²/8). Two corners' is first order, (π/K)(1 + D/π): splitting
    costs at once.
  - As D → ∞, two corners tend to 2π/K, the price of halving K. One corner grows as (π/2K)·e^{D/2}.
- **B5. Between the targets.**
  - The two-corner lay's relative grain is continuous at m.
  - m is its coarsest point between the targets: 4·atan(e^{D/2})·cosh(D/2)/K.
  - The one-corner lay is finest there, π/K.
- **B6. Discrete cells.**
  - The cell holding each target matches the continuum within 5% at K = 32 for D ≤ 4, and at K = 1024 for D ≤ 8.
  - The crossover, read off the discrete cells, lies within 0.2 nats of D* at K = 1024.

*Killed* if any identity is off by more than 10⁻²⁰ at 40 digits, if D* falls outside [1.9, 2.1], or if B6 misses its
tolerances.

#### Run 3 (25 October 2026, `runs/fpv/fpv3.py`, output `runs/fpv/fpv-run3.txt`, under a second)

**Killed**, both times by my set-up; the rest not killed. The script's first try stopped with an error before any
verdict: it inverted the lays numerically and the root finder failed on the two-corner lay. The lays now carry their
inverses in closed form, and that run is the one recorded.
- **B1.** One corner's best H is √(f₁f₂) to 10⁻⁴⁰, and both targets' relative cell is (π/K)·cosh(D/2) to 10⁻³⁸ at 32
  separations from 0.25 to 8 nats.
- **B2.** With two corners each target's relative cell is 4·atan(e^{D/2})/K, to 10⁻⁴¹.
- **B3.** D* = 2.02093620370845 nats, a distance ratio of 7.5454 (2.916 doublings); the cell there is 1.5555 × π/K. One
  corner is strictly better below it and two above it.
- **B4.** Both are π/K at D = 0. Near 0 the excesses are (1 + D²/8) and (1 + D/π), to 10⁻⁷. As D → ∞, two corners tend
  to 2π/K and one corner to (π/2K)·e^{D/2} (within 10⁻¹⁵ at D = 80).
- **B5.** The grain is continuous at m (jump 10⁻⁴⁰). **Killed by my set-up** in its second clause: the check took a
  numerical derivative at a = ½ itself, straddling the two halves of the piecewise lay. That gave nonsense at m (41 in
  place of 0.235 at D = 2), so a neighbouring grid point came out coarsest. On either side the grain rises toward m:
  0.2037, 0.2107, 0.2182, 0.2263 (×1 at K = 32, D = 2) coming in from below, the same mirrored from above.
- **B6.** At K = 1024 for D ≤ 8 the cells holding the targets are within 3.9% of the continuum, and the crossover read
  off the cells is at D = 2.018 (D* = 2.021). **Killed by my tolerance** at K = 32: one corner's cells were off by up
  to 13.7% (at D = 3.25), against my 5%. There a cell is 27% of its own distance wide, the target can sit anywhere in it,
  and the grain changes across one cell by about its own width. Two corners stayed within 5% at K = 32.

### Run 4: B5 and B6 again (predictions written 25 October 2026, before the run)

- **B5′.** Take the grain on each half by its own closed form, a one-sided derivative. Then m is the coarsest of 41
  points evenly spaced in levels between the targets, at 4·atan(e^{D/2})·cosh(D/2)/K, and one corner is finest there,
  at π/K. This holds at every D from 0.25 to 8.
- **B6′.** At K = 32 and D ≤ 4, the cell holding each target is off from the continuum by no more than the continuum
  relative cell itself (the grain's change across one cell). Written after seeing run 3's K = 32 deviations, so a
  weaker test than B6.

*Killed* as for run 3.

#### Run 4 (25 October 2026, `runs/fpv/fpv4.py`, output `runs/fpv/fpv-run4.txt`)

Nothing killed.
- **B5′.** With each half's slope one-sided, m is the coarsest point between the targets at every D: 4·atan(e^{D/2})·
  cosh(D/2)/K, to 10⁻⁴⁰. In units of π/K it is 1.47, 2.39, 6.88 and 54.0 at D = 1, 2, 4 and 8, where one corner gives 1.
- **B6′.** At K = 32 the worst target cell is off the continuum by 0.53 of the continuum relative cell.
- B1–B4 and B6's K = 1024 clauses come out as in run 3.

**What runs 3–4 say.**
- **One corner at the geometric mean** serves two targets better than two corners until they are D* = 2.02 nats apart:
  a distance ratio of 7.55, about three doublings.
  - At D*, both ways give each target 1.56 × π/K.
  - Past D*, one corner's cells grow as e^{D/2}, while two corners never get coarser than 2π/K at the targets.
- **Splitting costs at once and pays only slowly.** Two corners lose to first order in D, one corner only to second.
- **The two ways put their worst grain in opposite places.** Two corners make the space between the targets coarsest,
  exactly where one corner is finest. That matters if the next look is likely to fall between the two targets (the
  next-look median, Corollary 6.1(c)) rather than on either.
- Classical in its pieces: HKO's √(x₁x₂), and the turn's grain.

### Run 5: when to move the focus (predictions written 25 October 2026, before the run)

*Tom: "Yes", to the playground's next step: a refocus policy over a gaze trace (the cost of re-laying against the
grain).*

**Set-up.** Everything is in levels, x = ln d.
- **The gaze trace** is seeded, N = 200,000 looks.
  - The eye fixes on a target uniform on [0, 8] nats (a range of about 3,000), stays a geometric number of looks
    (mean 20, so a jump with p = 0.05 a look), then jumps to a fresh target.
  - Each look is the target plus a normal jitter of σ = 0.1 nats.
- **A policy** sees the look x_t and sets the corner c_t before that frame is laid.
- **Two costs:**
  - **G**, the mean grain at the look, (π/K)·cosh(x_t − c_t), in units of π/K (1 is best).
  - **R**, the share of looks on which the corner moves.
  - A move re-lays every cell whatever its size (the turn's edges all move), so R counts moves, not distance. The levels
    slid, S per look, are reported beside it.
- **Policies:**
  - **follow**, c = x_t;
  - **hold L**, hysteresis: move to x_t only when |x_t − c| > L, else stay;
  - **ease α**: c ← c + α(x_t − c);
  - **median m**: c = the median of the last m looks.

**Predictions.**
- **F1. follow.** G = 1 exactly, R = 1, and S is the trace's mean |x_t − x_{t−1}|.
- **F2. hold, L = 0.4 nats (four σ).**
  - R is in [0.04, 0.06]. The prediction is about 0.045 from the jumps (90% of jumps are larger than L), plus about 0.005
    from jitter crossing L. That is about twenty times fewer re-lays than follow.
  - G is in [1.005, 1.02]. The prediction is e^{σ²} = 1.010 from jitter about the look the corner was set on, plus a little
    from jumps smaller than L, which are never followed.
  - In short: about a 1% coarser grain for about 5% of the re-lays.
- **F3. ease, α = 0.5.**
  - It moves every look (R = 1).
  - Each jump leaves a geometric tail of large errors, so G is in [1.05, 1.2].
  - It is worse than hold 0.4 on both costs.
- **F4. median, m = 5.**
  - It lags two looks behind every jump, at the jump's whole error (E cosh J over a uniform range of 8 nats is in the
    hundreds), so G > 2.
  - Corollary 6.1's median is the best place to wait before a look is known. Once the look is seen it is only a lag.
- **F5. The one-or-two-corners switch with a band.**
  - The rule is: two corners once D > D* + b, one corner once D < D* − b, and keep the current layout inside the band.
  - Within the band, the worst loss against the better layout is within 5% of s·b, where s is the slope of the difference
    of the two grains at D*: s = sinh(D*/2)/2 − (2/π)·e^{D*/2}/(1 + e^{D*}) ≈ 0.391 (in π/K per nat).
  - On a seeded random walk of D (step sd 0.05 nats, reflected in [1, 3], 200,000 steps), b = 0.25 switches at least ten
    times less often than b = 0.

*Killed* if F1 is off by more than 10⁻¹², or any interval or inequality above fails.

#### Run 5 (25 October 2026, `runs/fpv/fpv5.py`, output `runs/fpv/fpv-run5.txt`, seeded, 17 s)

**Killed**: F1 and F3 in their R clause by my set-up, and F5 in both clauses, by my arithmetic and my guess. F2 and F4
not killed. The trace had 9,914 jumps in 200,000 looks.
- **F1.** follow's G = 1 to 10⁻¹⁵, and S = 0.2386 levels a look. **Killed by my set-up**: R = 0.999995, not 1, because
  the corner starts on the first look, so that look is no move.
- **F2.** hold 0.4 re-lays on 5.09% of looks, 19.6 times fewer than follow, at G = 1.0098 (e^{σ²} = 1.0100). Not
  killed.
- **F3.** ease 0.5: G = 1.131, worse than hold 0.4 on both costs. **Killed by the same set-up** in its R clause
  (0.999995).
- **F4.** median 5: G = 4.93. It re-lays on 63% of looks: a lag, as predicted. Not killed.
- **F5.** D* = 2.02094 and s = 0.3911. **Both clauses killed:**
  - The worst in-band loss is 0.1128 against s·b = 0.0978 (+15%). I left out the second-order term. With
    κ = cosh(D*/2)/4 − (1/π)·u(1 − u²)/(1 + u²)² = 0.467 (u = e^{D*/2}), s·b + κb²/2 = 0.1124, within 0.3%. That is
    post hoc, not a prediction.
  - The band cut the switches from 3,905 to 451, 8.7 times fewer, against my 10. The mean extra grain is 0.0027 π/K
    (0.17% of the 1.56 at D*).

The frontier of hold L (not predicted):

| L (nats) | G | R | S |
|---|---|---|---|
| 0.1 | 1.0008 | 0.505 | 0.215 |
| 0.2 | 1.0041 | 0.198 | 0.171 |
| 0.3 | 1.0077 | 0.080 | 0.143 |
| 0.4 | 1.0098 | 0.051 | 0.133 |
| 0.6 | 1.0133 | 0.044 | 0.130 |
| 0.8 | 1.0203 | 0.042 | 0.129 |
| 1.0 | 1.0329 | 0.040 | 0.128 |
| 1.5 | 1.1077 | 0.034 | 0.121 |

The other policies, beside it:
- ease 0.25 has G = 1.68, and ease 0.75 has 1.020; both re-lay every look.
- median 3 has G = 3.05 and median 9 has 8.26; both re-lay on 60–68% of looks.

**What run 5 says.**
- **Hold the corner, and move it only past a band of three to four times the gaze's jitter** (in levels). Here that is
  20 times fewer re-lays for 1% of grain.
  - Past that, R stops falling: it reaches the floor set by the jumps themselves (p = 0.05), and only G keeps growing.
  - The knee is where the band clears the jitter. The jumps set the floor.
- **Easing toward the look** re-lays every frame and trails every jump.
- **The median of recent looks** is worse still: a lag. Corollary 6.1's median is for choosing a corner before the look
  is known, not after it is seen.
- **The one-or-two-corners switch takes a band too.** At b = 0.25 nats it switches 8.7 times less often, for 0.17% of
  the grain.
- Hysteresis is classical (Schmitt triggers, LOD switching with a dead band). What the geometry adds is where to set the
  band: in levels, against the jitter.
