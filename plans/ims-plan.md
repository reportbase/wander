# IMS: importance sampling a changing view without rebuilding tables

*20 October 2026 (Tom's local date), SPN R402.*

*Tom (06:55 MDT): "seems like cauchy could provide more run-time options, not have to precalculate so much". Claude's
answer: the Cauchy can make the addresses (where things are, how they are seen) a runtime matter, but not the payload
(lighting, textures), and most of what rendering precomputes is payload. It proposed this test: sample directions under
a changing view, pushing a Cauchy through the composed Möbius map with no table, against the usual tabulated
distribution rebuilt at each view. Tom (07:00): "yes".*

*Exact where a closed form exists (mpmath), quadrature otherwise. A script in `runs/ims/`. Predictions written before
the script.*

## Known beforehand

- **Importance sampling an environment map.** A renderer that samples incoming light from a sky (an environment map)
  builds a table: the map's luminance on a latitude–longitude grid, its marginal and conditional cumulative sums, then
  inverts them. The table is rebuilt whenever what is being sampled changes (Pharr, Jakob and Humphreys, *Physically
  Based Rendering*, ch. 13–14). This is classical.
- **Normalizing flows.** A sample pushed through any invertible map is a sample of the pushed distribution, and its
  density follows from the Jacobian. So skipping a table is not, by itself, special to the Cauchy. What the Cauchy adds
  is closure: after any number of Möbius maps the distribution is still one member of the family, with its density in
  closed form and no chain of Jacobians.
- **The spherical Cauchy.** Kato and McCullagh 2020: the uniform distribution on the sphere carried by a Möbius map
  (on S², a Lorentz transformation) is a spherical Cauchy, with density (1/4π)·((1 − ρ²)/(1 + ρ² − 2ρ μ·x))². The family
  is closed under Möbius maps.
- **This corpus.**
  - SRA: aberration is a Möbius map of the addresses, and a uniform sky boosted is the spherical Cauchy with
    ρ = tanh(η/2) and density D²/4π. Doppler is the payload's weighting, and beaming's D⁴ = D² (addresses) × D² (payload).
  - SUM, ADR: Cauchys compose, and the point z moves by formula.
  - OFS §7.2: an address is not a payload.

## The set-up

- **The view change.** An observer boosted along +z with rapidity η ∈ {0.5, 2, 4}. Rest-frame directions y map to
  observed directions x by aberration; D(y) = 1/(γ(1 − β cos θ_y)) is the Doppler factor.
- **The targets.** Over the observed sphere, f_k(x) = D^k · L(y), for two values of k:
  - k = 2: the addresses only, the uniform sky's own arrival density;
  - k = 4: bolometric beaming, D² of addresses times D² of payload, as in SRA.
- **The payloads.** Two choices of L:
  - L₁ ≡ 1, a uniform sky;
  - L₂ = 1 + 4π·p(y), a sun: p is a von Mises–Fisher spot of concentration κ = 500 (about 2.6° wide) at rest-frame
    polar angle 60°. At rest the sun carries half of the sky's flux.
- **The samplers.** Each is a density q on the observed sphere.
  - **U**, uniform: q = 1/4π.
  - **C**, the Cauchy: uniform rest-frame directions pushed through the boost, q = D²/4π. It needs no table. A view
    change costs one 2×2 complex matrix product, and nothing is evaluated.
  - **T(N)**, the usual table, rebuilt for each view. f is evaluated at the centres of an equal-area grid on the observed
    sphere: N bins in cos θ and 2N in φ. Sampling is piecewise constant in proportion to those values. Each rebuild costs
    2N² evaluations of f.
  - **M(N)**, a mixed sampler. A table of the payload L alone is built once, on the same grid but in the rest frame, and
    never rebuilt. Its samples are pushed through the current boost, so q = q_tab(y)·D². The table carries the payload
    and the Cauchy carries the addresses.
- **The measure.** The relative variance of one importance-sampled estimate of F = ∫ f dΩ:
  V = (∫ f²/q dΩ)/F² − 1. It is computed by quadrature: Gauss–Legendre, 16 × 16 points in each of 128 × 256 equal-area
  cells, taken in whichever frame keeps the integrand piecewise smooth. Its accuracy is checked by repeating at 24 × 24
  points.

## Predictions

**I1 (closure, exact).**
- (a) In the stereographic chart, the boost is z ↦ e^η·z. The pushforward of the uniform sphere by it has density
  KM(ρ = tanh(η/2), μ = +e₃), to 10⁻⁴⁰. This is checked at 200 seeded points for each η, with the density from the map's
  exact derivative.
- (b) Two boosts about non-collinear axes (η = 2 along e₃, then η = 1 along e₁), composed as a product of 2×2 matrices,
  push the uniform sphere to a single spherical Cauchy: p^(−1/2) is affine in x, to 10⁻⁴⁰ in a least-squares fit over
  200 seeded points.
- *Killed* if either fails.

**I2 (the uniform sky).**
- For k = 2 and L₁, V_C = 0 at every η: f/q is constant. The view change cancels exactly from the Cauchy sampler.
- For k = 4 and L₁, V_C > 0, since the payload's D² is left over, but V_C < V_U at every η.
- *Killed* if either clause fails, beyond the quadrature's own error.

**I3 (the sun, the Cauchy alone).**
- (a) For k = 2 and L₂, V_C is the same at every η, to within the quadrature's error. It equals the rest-frame variance
  of L₂ under uniform sampling: the boost cancels and only the payload is left.
- (b) For k = 2 and k = 4, T(64) has a smaller V than C at every η: the table sees the sun and the Cauchy does not.
- *Killed* if either fails.

**I4 (the split: payload tabled once, addresses by the Cauchy).**
- (a) For k = 2, V_M(64) is the same at every η, to within the quadrature's error. It equals the rest-frame table's own
  variance on L₂.
- (b) For k = 2, V_M(64) ≤ V_T(64) at η = 2 and η = 4. The table rebuilt in the observed frame sees the sun stretched or
  squeezed by the aberration and resolves it worse than the rest-frame table that is never rebuilt.
- (c) For k = 4, V_M(64) < V_C at every η.
- *Killed* if any fails.

**I5 (the cost).** Counted, not timed.
- A view change costs T(64) 8,192 evaluations of f, plus its cumulative sums.
- It costs C and M none: one 2×2 complex product each, and M's payload table, built once, is never rebuilt.
- A statement of the construction, reported, not killable.

**I6 (the verdict).** A judgment. *Killed* if I1, I3(a) or I4(a) is killed.
- The Cauchy removes the precomputation tied to the view. The address part of a view change cancels exactly from the
  sampler, at any rapidity and through any composition of Möbius maps.
- It does not remove the payload's table. That still has to be built, but once, in the payload's own frame, and never
  again as the view changes.
- What a view change leaves over is the payload's own weighting (the second D² in beaming), not the addresses.

## What would and would not be shown

**Shown:** for view changes that are Möbius maps (turns, zooms of the stereographic chart, boosts), how much of an
importance-sampling table the Cauchy makes unnecessary, and what remains.

**Not shown:**
- warps that are not Möbius maps (lens distortion, a flat screen's own projection), where closure fails;
- rendering itself, BRDF sampling or multiple importance sampling;
- time on a GPU.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (20 Oct; `runs/ims/ims.py`, output `runs/ims/ims-run1.txt`, 42 s)

- **I1 not killed.**
  - (a) The boost z ↦ e^η·z pushes the uniform sphere to KM(tanh(η/2), e₃) to 5.8·10⁻⁶⁰, over 600 points.
  - (b) Two non-collinear boosts composed push it to one spherical Cauchy: p^(−1/2) is affine in x to 1.0·10⁻⁶⁰.

The relative variance of one sample, V, at 16 × 16 points a cell. The quadrature's own error, |16 − 24|, is at most
7·10⁻⁴ and mostly below 10⁻¹⁰.

| η | k | sky | V_U | V_C | V_T(64), rebuilt | V_M(64), built once |
|---|---|---|---|---|---|---|
| 0.5 | 2 | uniform | 0.362 | 0 | 1.3·10⁻⁴ | 0 |
| 0.5 | 2 | sun | 241 | 124.75 | 0.168 | 0.0684 |
| 0.5 | 4 | uniform | 1.44 | 0.252 | 6.5·10⁻⁴ | 0.252 |
| 0.5 | 4 | sun | 332 | 172 | 0.197 | 0.210 |
| 2 | 2 | uniform | 17.5 | 0 | 0.075 | 0 |
| 2 | 2 | sun | 3,904 | 124.75 | 6.17 | 0.0684 |
| 2 | 4 | uniform | 67.9 | 0.767 | 0.470 | 0.767 |
| 2 | 4 | sun | 6,155 | 197 | 6.52 | 0.388 |
| 4 | 2 | uniform | 993 | 0 | 18.3 | 0 |
| 4 | 2 | sun | 210,661 | 124.75 | 4,098 | 0.0684 |
| 4 | 4 | uniform | 3,830 | 0.799 | 59.9 | 0.799 |
| 4 | 4 | sun | 333,724 | 197 | 5,299 | 0.397 |

- **I2 not killed.** For the uniform sky with k = 2, V_C is 3.6·10⁻¹⁵, zero to rounding, at every η. For k = 4 it is
  0.25–0.80, always below V_U.
- **I3(a) not killed:** with the sun and k = 2, V_C is 124.750000 at every η. The boost cancels and only the payload is
  left.
- **I3(b) killed.** The table rebuilt per view beats the Cauchy at η = 0.5 and 2, but not at η = 4: 4,098 against 124.75
  for k = 2, and 5,299 against 197 for k = 4.
  - My prediction assumed a rebuilt table is always the better sampler.
  - At η = 4 the boost squeezes the sun to about a twentieth of its rest width, and squeezes the forward cap where D² is
    largest. A 64 × 128 table built from cell centres no longer resolves either. Its V is 18 even for the uniform sky,
    where the Cauchy is exact.
  - Post hoc: a finer table, cell averages in place of centres, or a table that adapts to the view would do better. That
    is more precomputation per view, the cost the Cauchy avoids.
- **I4 not killed.**
  - (a) With the sun and k = 2, V_M is 0.068407 at every η, the rest-frame table's own variance.
  - (b) V_M ≤ V_T at η = 2 and 4, by a factor of 90 at η = 2 and 60,000 at η = 4.
  - (c) For k = 4, V_M < V_C at every η.
  - Post hoc: at η = 0.5 with k = 4, M (0.210) is slightly above T (0.197). That was not predicted, and does not kill (b),
    which named η = 2 and 4 only.
- **I5.** A view change costs T(64) 8,192 evaluations of f plus its sums. C and M cost one 2×2 product, and M's table was
  built once.
- **I6 not killed.**

The verdict:
- The Cauchy removes the precomputation tied to the view. The address part of a view change cancels exactly from the
  sampler, at any rapidity and through composed maps.
- The payload's table is still needed, but built once, in the payload's own frame. Paired with the Cauchy for the
  addresses, it keeps the same variance under every view change: 0.068 at η = 0.5, 2 and 4 alike.
- The table rebuilt for each view at fixed resolution degrades as the view changes more, and at η = 4 it is worse than
  the Cauchy alone.
- What a view change leaves over is the payload's own weighting (the second D² of beaming), as k = 4 shows: M rises from
  0.068 to 0.21–0.40.

Not shown: warps that are not Möbius maps, and time on a GPU.

### Read after the run (20 Oct, SPN R403)

Tom: "the advantage that cauchy has is it does not need to know N.", then "so tie with classical is good news actually."
I3(b)'s kill is this run's clearest case: the rebuilt table has an N (its 64 × 128 cells) and fails when they are too
coarse; the Cauchy has none. The payload's table, built once, is where N stays. The lens in `boost-sky.html` (not a run of
this plan; no predictions were committed for it) restates draw's Tangent Bridge §10.2–10.3 for sampling, known beforehand
and not checked first.
