# MNY: many observers reading each other, facings and heat

17 November 2026. SPN R1073. Tom: "help me understand the read/write interpretation of how this scales to multiple
observers", then "proceed with additional tests". The open items from that answer: loops of more than three observers
on a curved world, and many observers with the Cauchy heat on each read.

## Part A: facings among many observers (exact, 50 digits)

### Set-up
- N observers at places P_i on the unit sphere (or the plane), each with its own frame (a unit tangent vector). Which
  pairs read each other is a graph G with E edges.
- On each edge, the owned turn read from the two mutual bearings, r_ij = β_ij − β_ji + π (wrapped), as TLP. r_ji = −r_ij.
  Turning frame i by φ_i moves r_ij by φ_j − φ_i.
- The loop sum of a closed path: the sum of r along it.
- **Mutual rule**: φ_i += α·Σ_(j ~ i) r_ij (each turns toward all its neighbours). **One-way rule on a ring**:
  φ_i += α·r_(i,i+1).

### Predictions (committed before any run)
- **A1. Polygons.** For a ring of N = 4, 5, 6 observers placed as a convex spherical polygon, |loop sum| equals the
  polygon's excess (its interior angles' sum less (N − 2)π, computed independently from the vertices) to 10⁻⁴⁰, for 20
  polygons each, whatever the frames.
- **A2. Independent loops.** On the complete graph K_N (N = 4, 5, 6) the loop sums of the (N − 1)(N − 2)/2 triangles
  through observer 1 determine every other triangle's loop sum (mod 2π) by addition: the cycle space has dimension
  E − N + 1. For K_4 on the sphere with the tetrahedron containing the centre, the four faces' excesses add to 4π
  exactly, and their loop sums, each read with the face oriented outward, add to 0 mod 2π.
- **A3. Mutual rule on any graph.** On a ring of 5 and on K_5, on the sphere: every loop sum is unchanged every round
  (to 10⁻⁴⁰); the frames stop; the resting residuals are the orthogonal projection of the starting residuals onto the
  cycle space (the vector r* with zero divergence at every observer, Σ_j r*_ij = 0, and the same loop sums); the
  deviation shrinks at the rate max|1 − α·λ| over the graph Laplacian's nonzero eigenvalues λ. In the plane (all loop
  sums 0) r* = 0: full agreement.
- **A4. One-way rule on a ring of N = 4, 5, 6.** The loop sum S is unchanged; the residuals tend to S/N each; at rest
  every frame turns by α·S/N every round, to 10⁻⁴⁰ after 400 rounds. In the plane the frames stop.

### Kill conditions
Any stated equality off by more than 10⁻⁴⁰; the cycle-space count wrong; frames stopping or drifting against A3, A4.

## Part B: the heat among many (seeded)

### Set-up
- MUT's chain M5 (N observers on a line, gaps in amounts, each moving by ½α of the gap to its right less its corner and
  minus ½α of the gap to its left less its corner), with each read of a gap spread by an independent Cauchy of
  half-width γ (a read's heat): the read gap is g + γ·ξ, ξ standard Cauchy, fresh each read and round.
- The update is linear, x′ = A·x + c + B·ξ, so the stationary law of each gap is exactly a Cauchy with median at the
  noiseless fixed point and half-width γ·Σ_(k ≥ 0) Σ_j |(A^k B)_ij| (stable laws; worked before the run, classical).

### Predictions
- **B1.** For N = 5, 8 at α = 0.1, 0.5 and 0.9 of 2/λ_max: each gap's median within 0.02γ of the noiseless fixed point,
  and its half-interquartile range within 3% of the formula, on 100,000 seeded chains after 600 rounds.
- **B2.** For N = 2 the formula is essay 30's g(α + β)/(1 − |1 − α − β|) at α = β.
- **B3, measured, not a kill.** Whether a gap's half-width equals one read's γ, as the pair's does for α + β ≤ 1. Reported.

### Kill conditions
B1 off by more than its tolerances at any setting; B2's formula disagreeing.

## What this does not test
- Moving observers (boosts): TWG.
- Which rule any real system uses.
- Novelty: Gauss–Bonnet, discrete Hodge decomposition of edge data (a gradient part and a cycle part), graph-Laplacian
  consensus, and stable laws through linear maps are classical (R1071).

## Runs

**Run 1** (`runs/mny/mny.py`, output `runs/mny/mny-run1.txt`, 17 Nov).
- **Not killed: A1, A2, A3, A4, B2.**
  - A1: on 60 convex spherical polygons (N = 4, 5, 6) |loop sum| equals the excess to 2·10⁻⁶⁰, whatever the frames.
  - A2: the cycle space has dimension 3, 6, 10 for K₄, K₅, K₆, and every triangle's loop sum is the sum of those through
    observer 1 to 10⁻⁶⁰. For K₄ round the centre the four excesses add to 4π and the outward loop sums to 0 mod 2π.
  - A3: on a ring of 5 and on K₅ on the sphere every loop sum was kept, the frames stopped, and the rest was the projection
    onto the cycle space to 10⁻⁵⁹; the rates 0.8618034 and 0.5 equal max|1 − αλ|. On the sphere the resting residuals are
    not zero (up to 2.74 on K₅); in the plane they are (10⁻⁶⁴): full agreement.
  - A4: on rings of 4, 5, 6 on the sphere the residuals sit at S/N and every frame turns α·S/N a round for ever, to 10⁻⁶⁰;
    in the plane S = 0 and the frames stop.
  - B2: the pair's half-width from the formula equals essay 30's at every share tried, 0.1 to 1.3.
- **B1 killed, by my tolerance.** Every half-IQR matched the formula within 1.4% (the 3% held), but the medians were off by
  up to 0.177γ against my 0.02γ. A Cauchy sample's median has standard error π·s/(2√S), here s up to 12.6γ and S = 10⁵,
  so 0.06γ: the 0.177 is 2.8 standard errors, and my bound was below the sampling error.
- **B3, measured.** No gap keeps one read's width. Half-widths run 2.7γ to 12.6γ, the end gaps narrowest and the middle
  widest, growing with N (the middle 3.8γ at N = 5, 7.0γ at N = 8 for small and middle shares).

**Run 2 prediction** (committed before run 2):
- **B1′.** As B1 with a fresh seed, the medians within 4 standard errors, π·s/(2√S) with s the formula's half-width, of
  the noiseless fixed point, and each half-IQR within 3% of the formula.

**Run 2** (`runs/mny/mny2.py`, output `runs/mny/mny-run2.txt`). **B1′ not killed**: the medians within 3.0 standard
errors at every setting (the largest 2.99, over 33 gaps), every half-IQR within 1.1% of the formula.

**What the runs show.**
- **Facings among many split in two, by a classical decomposition.** The edge turns read between observers are a
  gradient part (differences of the observers' own facings, which an exchange of turns can remove) plus a cycle part (the
  loops' leftovers, which no exchange touches). There are E − N + 1 independent loops; on a sphere each carries its
  enclosed excess, area over radius squared; in the plane every one is zero.
- **Exchange keeps the leftovers and removes the rest.** A mutual rule on any graph settles at the cycle part alone: every
  loop sum kept, the frames stopped, at the rate the graph's Laplacian sets. A one-way rule round a ring cannot stop: its
  frames turn α·S/N a round for ever. In the plane both agree fully.
- **The heat grows with the many.** A chain of observers each reading its neighbours with the Cauchy heat on every read
  keeps every gap a Cauchy, its half-width the stable-law sum γ·Σ_k |row of M^k·B|. A pair keeps exactly one read's width
  (for shares up to 1); a chain does not: 2.7 to 12.6 reads' widths, widest in the middle, growing with the number of
  observers. Each gap is spread by every read in the chain, passed along it.
- **Classical**: Gauss–Bonnet, the discrete Hodge decomposition of edge data, graph-Laplacian consensus, stable laws
  through linear maps. The sorting is ours (R1071): the turn on an edge is two reads; each observer's facing is its own
  write; a loop's leftover belongs to no observer and needs a size (the radius); the heat is the reads', and the many pass
  it to one another.
