# CIW: the head's turn on an object, combined with the central sweep

*19 October 2026 (Tom's local date), SPN R384.*

*Tom (11:27 MDT): "doesn't rotating the head sweeping sweeping the object create the cauchy of it."*

*Claude:*
- *yes, on a flat object: the lighthouse;*
- *the Cauchy there is m + i·d, the reader's own standpoint in the object's terms;*
- *read on the object's marks, that is writing.*

*Tom (11:28): "yes, but combine that with the central sweep."*

*Exact (mpmath) where a closed form exists, seeded samples elsewhere, thresholds in standard errors. Scripts in
`runs/ciw/`.*

## Known beforehand

- **The flat object** (the lighthouse, OFS Proposition 5(f)). A uniform turn from a standpoint at height γ above a line,
  over its foot m, lands with law Cauchy(m, γ). The landing density is (1/π)·dθ/dx, the inscribed sweep alone.
- **The disc** (classical):
  - The harmonic measure from z, the law where a Brownian motion from z first meets the unit circle, is the Poisson
    kernel P_z(φ) = (1/2π)·|1 − |z|²|/|e^{iφ} − z|². That is the wrapped Cauchy centred on arg z.
  - Its concentration is ρ = |z| from inside and 1/|z| from outside.
  - Its first trigonometric moment is z from inside and 1/z̄ from outside. On the circle the horizon closes, and a
    mean returns (HZT H5).
- **The inscribed angle theorem.** Equal turns give equal arcs only from the centre (rate 1) or from a point of the
  circle (rate 2): OFS §4, "Why there are two sweeps, and only two".
- **In the corpus.**
  - OFS §4, "The address points at the payload": the inscribed ray and the central radius meet at one point (III.20).
  - R332: one read, two breakdowns.
  - SHG: only circles read evenly along their outline.
  - DYH and ADR: the Cauchy's point m + iγ is the standpoint.
- **draw's labs:** nothing on harmonic measure or the Poisson kernel (searched).

## The set-up

- **The object.** A circle of radius R centred at C. The reader stands at z, written in units of R about C (a complex
  number, unitless).
- **The central sweep** (from C) addresses each point of the outline by its central angle φ, uniform at rate 1. Only its
  directions are used here, not its radii, so no amount enters.
- **The inscribed sweep** (the head's turn at z) reads the direction to that same point, θ(φ) = arg(e^{iφ} − z).
- **Combining** the two pairs each landing's θ with its φ: the one point both reads meet.

The identity, derived before the run:

    d/dφ arg(e^{iφ} − z) = (1 − Re(z̄·e^{iφ}))/|e^{iφ} − z|²,

so

    2·dθ/dφ − 1 = (1 − |z|²)/|e^{iφ} − z|².

**Twice the inscribed rate less the central rate is the Poisson kernel:**
- from inside, 2π·P_z(φ) = 2·dθ/dφ − 1;
- from outside, 2π·P_z(φ) = 1 − 2·dθ/dφ.

Integrated over an arc of central angle α that subtends θ_z at z, from inside, ω_z(arc) = θ_z/π − α/(2π). This is the
classical arc formula for harmonic measure.

## Predictions

**K1 (the object's Cauchy is the two sweeps combined, exact).**
- At 10⁴ seeded (z, φ), with |z| drawn from (0, 0.99) and (1.01, 20), at 50 digits:
  - 2π·P_z(φ) equals ±(2·dθ/dφ − 1) to 10⁻⁴⁰ (+ inside, − outside), with dθ/dφ by numerical differentiation of
    arg(e^{iφ} − z);
  - for 10³ seeded arcs from inside, ω_z = θ_z/π − α/(2π), with ω_z the Poisson kernel's integral, to 10⁻³⁰.
- The coefficients are the two rates of OFS §4: 2 (the inscribed sweep at the circle) and 1 (the central). The object's
  Cauchy is neither sweep alone.
- *Killed* if either fails.

**K2 (from inside, the landings' mean is half the standpoint).**
- The central sweep's own mean of e^{iφ} is 0. From K1 the Poisson kernel's moment z is 2·E_I[e^{iφ}] − 0. So the
  landings of a uniform head turn from z, taken as points of the unit circle, have centroid z/2: halfway from the
  object's centre to the reader, in R.
- At |z| ∈ {0.1, 0.5, 0.9}, with N = 10⁶ seeded uniform turns, the sample centroid times 2 is within 3 standard errors
  of z in each component.
- The same centroid with the landings weighted by the Poisson kernel instead (importance weights 2π·P_z) is z itself,
  within 3 standard errors.
- *Killed* if either fails.

**K3 (from outside, the back is needed).**
- From outside, the identity runs φ once round the circle, so it uses both of each ray's crossings: the near one, seen,
  and the far one, behind. Only the central sweep reaches the far one.
- Exact (quadrature at 50 digits): −(1/π)·∮ e^{iφ} dθ = 1/z̄ at |z| ∈ {1.5, 2, 4, 100}, to 10⁻³⁰.
- The near crossings alone give a share of it that tends to ½ far off: within 1% of ½ at |z| = 100, and more than 1%
  from ½ at |z| = 1.5.
- So from outside the inscribed reader alone gets about half of the object's Cauchy, and the central reader supplies
  the back.
- *Killed* if either fails.

**K4 (the standpoint in the object's radius, with no unit).**
- From inside, ẑ = 2·mean(e^{iφ}) over N = 10⁴ landings recovers z, |z| = D/R, unitless.
- With the world scaled by k ∈ {10⁻³, 7, 10³} (R and the standpoint together), the φ of every landing is unchanged to
  10⁻¹², so ẑ is too.
- Over 200 seeded repeats at |z| = 0.5, the mean of ẑ is within 3 standard errors of z.
- *Killed* if not.

**K5 (only the circle).**
- An ellipse with semi-axes 2 and 1, with φ the central angle from its centre and the standpoint z = 0.8 on the major
  axis. The combination is the Poisson kernel only for the circle (SHG).
- The prediction: the combined density 2·dθ/dφ − 1 (φ the ellipse's central angle) is not a wrapped Cauchy. The best
  wrapped Cauchy fitted to it by least squares on a 4,096-point grid leaves a relative L1 residual above 1%.
- *Killed* if it is below 1%.

**K6 (the verdict).** A judgment. *Killed* if K1, K2 or K4 is killed.
- The head's turn alone lays the uniform turn's law on the object: the Cauchy on a flat object, with its centre and width
  the reader's foot and distance.
- On a round object, the object's own Cauchy (the wrapped Cauchy, the Poisson kernel, the law with a mean) is the
  combination: twice the inscribed sweep's rate less the central's.
- It places the reader in the object's own radius, with no unit. From inside, the landings' centroid is halfway to the
  reader. From outside, half of it lies behind the object and needs the central sweep.

## What would and would not be shown

**Shown:**
- that the two sweeps, combined, give the object's Cauchy exactly (on the circle), with the reader's standpoint as its
  parameters, in the object's radius;
- where each sweep is needed.

**Not shown:**
- anything about real objects or observers;
- any shape but the circle, beyond K5's negative.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (19 Oct, `python3 runs/ciw/ciw.py`; output `runs/ciw/ciw-run1.txt`, 55 s)

K6 is killed in its letter, by K1's arc clause.

- **K1 killed, by my quadrature.**
  - The pointwise identity holds: 2π·P_z(φ) = ±(2·dθ/dφ − 1) to 1.0·10⁻⁴⁸ at 10⁴ (z, φ), inside and outside. The closed
    form of dθ/dφ matches numerical differentiation to 10⁻⁴⁸.
  - The arcs failed: ω_z = θ_z/π − α/(2π) only to 5.1·10⁻⁵. The plain `mp.quad` over [φ₁, φ₂] missed the kernel's peak
    at arg z when |z| is near 0.99.
  - Post hoc, on the same 10³ arcs (the RNG replayed): with the peak as a breakpoint the error is 1.5·10⁻⁴⁸; with the
    Poisson kernel's closed-form antiderivative, 5·10⁻⁵⁰.
- **K2 not killed.** At |z| = 0.1, 0.5, 0.9, twice the landings' centroid is z within 2.2 standard errors in each
  component. The kernel-weighted centroid is z itself within 2.2.
- **K3 not killed.**
  - −(1/π)∮ e^{iφ} dθ equals 1/z̄ to 7·10⁻⁵² at |z| = 1.5, 2, 4, 100.
  - The near crossings' share (real to 10⁻⁵¹) is 0.6667, 0.6153, 0.5541 and 0.5021: within 0.5% of ½ at 100, and well off
    it at 1.5.
  - Post hoc: (share − ½)·|z| is 0.2501, 0.2307, 0.2163, 0.2122, approaching 2/(3π) = 0.2122.
- **K4 not killed.**
  - Scaling the world by 10⁻³, 7 and 10³ moves no landing's central angle by more than 4.4·10⁻¹⁶ rad.
  - Over 200 repeats of N = 10⁴, ẑ averages z within 0.9 standard errors; each ẑ is good to about 0.014.
- **K5 not killed.** For the ellipse the combined density integrates to 1 but dips below zero (to −0.0014). The best
  wrapped Cauchy leaves a relative L1 residual of 0.40.

### Run 2 predictions (19 Oct, written before the run; `runs/ciw/ciw2.py`)

**K1′.** The same 10³ arcs on a fresh seed. ω_z, computed by `mp.quad` with the kernel's peak at arg z (and its copies
2π apart) as breakpoints, equals θ_z/π − α/(2π) to 10⁻³⁰. *Killed* if not.

**K6′.** The verdict of K6. *Killed* if K1 (pointwise, run 1), K1′, K2 or K4 is killed.

### Run 2 (19 Oct, `python3 runs/ciw/ciw2.py`; output `runs/ciw/ciw-run2.txt`)

The predictions above were written to the plan before the script ran, but committed with the run, not before it.

- **K1′ not killed.** On 10³ fresh arcs, ω_z = θ_z/π − α/(2π) to 6·10⁻⁵⁰.
- **K6′, the verdict, not killed.**
  - **The head's turn alone** lays the uniform turn's law on an object, the same for every object. On a flat one this is
    the lighthouse's Cauchy, whose centre and width are the reader's foot and distance.
  - **Combined with the central sweep, on a round object,** the two give the object's own Cauchy exactly: the wrapped
    Cauchy (the Poisson kernel, the harmonic measure).
    - It is 2 × the inscribed rate − 1 × the central rate. These are the two rates of OFS §4, 2 at the circle and 1 at
      the centre.
    - Its parameters are the reader's standpoint in the object's own radius, z = (D/R)·e^{iψ}, with no unit carried in.
      The central sweep supplies the object's angle, not an amount.
    - The circle closes the horizon, so this Cauchy has a mean: z from inside, 1/z̄ from outside.
  - **From inside,** the landings of a uniform head turn have centroid z/2, halfway from the object's centre to the
    reader.
  - **From outside,** the identity needs both crossings of each ray. The inscribed reader sees only the near ones, about
    half of it (two thirds at 1.5 R, ½ far off). The back is the central sweep's.
  - **Only the circle.** For an ellipse the combination is not a wrapped Cauchy (40% residual) and is not a probability.

The mathematics is classical: the Poisson kernel, the arc formula for harmonic measure, the inscribed angle. The reading
is ours.
