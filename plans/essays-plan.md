# The long essays: a plan

28 Oct 2026, SPN R562. Tom, after four referee reads of the submission at 4/10:
- "i'm not in a hurry to submit to journals. the low score is simply large claims require large and very persuasive
  evidence. A good is no enought, it needs to be great."
- "Much of this is educational, these ideas are not mainstream, they are tucked away in dusty old papers that have
  themselves only offered partial pictures of the situation."
- "what about the other way, instead of smaller, go bigger, longer essays, that actually explain the situation."
- "in the process, we can pull out very short targeted paper that say one thing and sumbit them to journals, thats what
  they like, but that is not the priority, and only if well argued in the mani paper/book."

## What changes

- **The priority is a long work that explains.** It is a series of long essays read in order, a book written in
  public. The ideas are in print in pieces (Jaynes's measure, Euclid III.20, Poincaré's rescaling, Bridgman's
  ratios, Martens's standard, Sedgwick's eye height, the gauge of bundle adjustment). Each piece gave a partial
  picture; the essays draw the whole.
- **Journals come second.** A short paper that says one thing is pulled out for a journal only once the main work
  argues it well. It is drawn from the essays and OFS, the way the submission is drawn from OFS (R421). It is never
  written first.
- **OFS stays the single source of truth.** The essays explain it and claim nothing it does not hold. A change goes into
  OFS first.
- **Citations** go into the essays as history: who saw which piece, and what it missed. Never as defence. The record of
  everything searched stays in `plans/` (`rwf-literature.md`, `ofs-literature.md`).
- **The submission** (`papers/ofs-submission.md`) is kept as it is, and is not sent until it is argued well in the main
  work.

## Each essay

1. **Opens on something everyone knows:** a thumb against a mountain, a camera, a map, a survey, a lighthouse.
2. **Shows the geometry in full.** Every step is worked, nothing is left to "it can be shown", and there is a demo
   wherever seeing helps.
3. **Says where the pieces came from:** the old paper that saw each part, and what it left out.
4. **Ends with what it changes:** what a reader now understands, and the two tests (scale the world; change what
   arrives) applied to its cases.

Long is allowed. Explaining comes before compressing. The case of h, v, H, V is kept as everywhere else.

## A first sequence (to reorder and cut)

| # | essay | opens on | demos | where the pieces came from |
|---|---|---|---|---|
| 1 | **Reading and writing** | Poincaré's universe a thousand times larger overnight | `writer-readers.html`, `room-ratios.html`, `blueprint.html` | Poincaré 1914, Bridgman 1922, Stevens 1946, Martens 2021 |
| 2 | **One length turned** | holding up a thumb | `one-read.html`, `facing.html`, `paths.html` | Euclid III.20 and III.31, Thales, Cauchy's functional equation |
| 3 | **Addresses given, payloads met** | turning one's head along a row of trees | `payload-free.html`, `sweep-zero.html`, `theorem6.html`, `central-reader.html` | Jaynes 1968, Kato and McCullagh, Stevens's permissible statistics |
| 4 | **Near and far** | the depth buffer, or Mercator's map | `levels.html`, `zoom.html`, `h-limits.html`, `focus.html` | Mercator, Luce's ruler, the depth buffer |
| 5 | **Three parties** | a camera's frame | `wedge.html`, `sphere-cube.html`, `writer-box.html`, `glass-box.html` | Archimedes' hat-box, Lambert |
| 6 | **Many standpoints** | Roy's base on Hounslow Heath | `parallax.html`, `room-walk.html`, `slide-rule.html`, `mountain.html` | Snellius, Roy, Triggs et al., Sedgwick |
| 7 | **Where it shows up** | the lighthouse | `boost-sky.html`, `pinhole.html`, `ground.html`, `moon.html` | Lighthouse problem, Mercator, aberration, LIGO |
| 8 | **What the geometry gives free** | scrolling a list without end | `wedge-browse.html`, `star-dial.html`, `fpv.html` | depth buffers, level of detail, fisheye views |

## What already exists (Tom, 28 Oct: "we also have essays cauchy, computer science application, physics and the
number line, tangent bridge, among others.")

The series starts from these, rewritten in the present frame (one length H, the two tests, addresses and payloads),
not from nothing. Each older piece predates some rulings, so every term is checked first (CLAUDE.md, "check every
term"); where one differs from OFS, OFS stands.

| existing work | where | essay it feeds |
|---|---|---|
| *The Cauchy*, *The Cauchy, Inside and Out*, *The Cauchy Distribution as the Measure* | `papers/archive/` | 3 Addresses given, payloads met |
| the computer-science companion | `papers/observation-from-somewhere-cs.md` | 8 What the geometry gives free (and a CS essay of its own) |
| the physics companion, `physics.md`, `inverse-square.md`, `parallax.md` | `papers/` | 6 Many standpoints, 7 Where it shows up |
| *The number line* | `papers/number-line.md` | 1 Reading and writing (the writer's ruler), 4 Near and far |
| *The Tangent Bridge Theorem* (algebra, classical, spectral) and *TVF* | reportbase/draw `papers/` | a new essay, "Arrays and the circle": a finite set of readings carrying a signal, the kernel at N = 2 the Cauchy |
| *The Unit Rule* | `papers/unit-rule.md` | the essay on holding in order (time) |
| *Each Sees the Other Smaller* | `papers/denominator-paradox.md` | 1 Reading and writing (two readers, one exchanged number) |
| `vantages.md` (paradoxes as vantage conflations) | `papers/` | 9 (below) |
| *The dial's geometry*, *Special relativity, sorted* | reportbase/calendar `GEOMETRY.md`, `RELATIVITY.md` | 4 Near and far (three rulers), 7 (the boosted sky) |
| *Special Relativity, Through the Fisheye*, *Browsing the Fisheye*, *The Radix* | `papers/archive/` | 7, 8 |
| `mapping.md` | `papers/` | 6 Many standpoints |

So the sequence grows to about eleven:
1. Reading and writing
2. One length turned
3. Addresses given, payloads met
4. Near and far
5. Three parties
6. Many standpoints
7. Where it shows up
8. What the geometry gives free
9. Paradoxes as vantages
10. Arrays and the circle (the Tangent Bridge)
11. Holding in order (the Unit Rule)

Some of these may stand as existing essays lightly reframed rather than new writing. Which of them come first is Tom's.

## Short papers to pull out later

Each only once its essay argues it well. Candidates:
- The Cauchy as the invariant measure of directions, and why the median (essay 3; the present submission, cut down).
- Scale the world: reading and writing as a test of what a standpoint can know (essay 1; measurement theory or
  philosophy of science).
- The corner as the best focus, and the turn as a depth scheme (essays 4 and 8; graphics).

## First step

Essay 1, Reading and writing. It is the widest idea and the one with the clearest history. Its outline goes to Tom
first.
