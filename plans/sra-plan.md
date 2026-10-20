# SRA: special relativity's sky, addresses and payload

*19 October 2026 (Tom's local date), SPN R395.*

*Tom (20:19 MDT): "do you discuss the shape library in ofs, and how they all return the cauchy." (20:22): "you understand
why this is so important. SR itself uses these ideas, and no where does it mention the distinction between the payload
and the addres." (20:24), to putting it in OFS against R201's rule of no physics: "lets make this one exception because it
goes to our main thesis."*

*Checked at 50 digits (mpmath), at seeded points and on grids. Scripts in `runs/sra/`. Predictions written before the
script.*

## Known beforehand

- **Aberration.** cos θ′ = (cos θ + β)/(1 + β cos θ), equivalently tan(θ′/2) = tan(θ/2)/k with k = √((1 + β)/(1 − β)),
  for a source at angle θ from the motion in its own frame and θ′ in the observer's. It does not depend on frequency.
  The archived *Special Relativity, Through the Fisheye*, rechecked in `runs/srf/check.py` (C0). **[classical]**
- **Penrose 1959; Terrell 1959.** The Lorentz group acts on the celestial sphere as its group of Möbius maps,
  PSL(2, ℂ). A boost along an axis is, in the stereographic chart from that axis, the dilation z ↦ z/k. **[classical]**
- **Doppler and beaming.** The Doppler factor is D = 1/(γ(1 − β cos θ′)) = √(1 − β²)/(1 − β cos θ′).
  - A photon's energy scales by D.
  - Arrivals from a steady source scale by D.
  - I_ν/ν³ is invariant, so the bolometric intensity scales by D⁴ (Rybicki and Lightman 1979, §4.9). **[classical]**
- **Kato and McCullagh (2020), *Bernoulli* 26(4), "Möbius transformation and a Cauchy family on the sphere".**
  - The spherical Cauchy on S^d has density ∝ ((1 − ρ²)/(1 + ρ² − 2ρ μ·x))^d.
  - The family is closed under Möbius maps.
  - Its stereographic image is a multivariate t.
  - On the circle, d = 1, it is the wrapped Cauchy. **[classical]**
- **The archive's C1** (`plans/archive-gems.md`): in the stereographic chart a circle sky's readings are Cauchy, while a
  sphere sky's single signed coordinate is not (quartiles ±1/√3). This is a statement about one chart, and it stands.
- **MOT run 3.** A boost moves only the sky's corner, to tan(θ/2) = k. **CMP run 1.** The Poisson kernel carried by a
  map.

## Predictions

**A1 (aberration is a Möbius map of the addresses).**
- At 10³ seeded θ and β ∈ {0.1, 0.6, 0.99}, the cosine form and tan(θ′/2) = tan(θ/2)/k agree to 10⁻⁴⁵.
- In the stereographic chart z = tan(θ/2)·e^{iφ}, the boost is z ↦ z/k: φ is unchanged.
- *Killed* if not.

**A2 (a uniform sky, boosted, is the spherical Cauchy).**
- The density of directions seen, pushed forward from a sky uniform in the sources' frame, is
  (1 − β²)/(4π(1 − β cos θ′)²).
- This equals Kato and McCullagh's d = 2 member, μ along the motion and ρ = (k − 1)/(k + 1) = tanh(η/2), η the
  rapidity, to 10⁻⁴⁵ on a grid of θ′.
- In 2 + 1 dimensions the boosted uniform circle is the wrapped Cauchy (the d = 1 member) with the same ρ, to 10⁻⁴⁵.
- *Killed* if either fails.

**A3 (the addresses' density is D²).**
- (1 − β²)/(1 − β cos θ′)² = D², exactly, to 10⁻⁴⁵.
- So of beaming's D⁴ for an isotropic sky's bolometric intensity:
  - D² is the address law: the solid angle each source's address takes, the Jacobian of the Möbius map;
  - D² is the payload per source: energy D times arrival rate D.
- Checked by integrating I_ν = D³·I₀(ν/D) over ν for a blackbody I₀, against D⁴·∫I₀, to 10⁻⁴⁰.
- *Killed* if the identity fails, or the integral does not split as D² · D².

**A4 (each map leaves the other side alone).**
- The aberration formula has no ν, so changing every source's spectrum (the payload) moves no address.
- Changing the sources' directions in their own frame by any rotation about the motion leaves every source's D unchanged.
- For a direction off the axis, D is a function of θ′ alone: a function on the addresses, the payload's weighting, not a
  change of address.
- Checked at seeded points to 10⁻⁴⁵.
- *Killed* if not.

**A5 (the verdict).** A judgment. *Killed* if A1, A2 or A3 is killed.
- Special relativity transforms what is seen in two separate parts, written as separate formulas and never named as such:
  - the addresses, by a Möbius map that carries the uniform sky to the spherical (or wrapped) Cauchy and moves only its
    parameter ρ = tanh(η/2);
  - the payload, by the Doppler factor at each address.
- Beaming's D⁴ is their product, D² of address and D² of payload.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (19 Oct; `runs/sra/sra.py`, output `runs/sra/sra-run1.txt`)

- **A1 killed, by my set-up.**
  - The cosine and half-angle forms agree to 4·10⁻⁴⁶.
  - The stereographic clause missed by 1.5·10⁻⁴⁵ against 10⁻⁴⁵. I tested an absolute error on z, which is unbounded:
    near θ = π, |z| = tan(θ/2) runs to the thousands, and 50 digits leave ~10⁻⁴⁹ relative.
  - The azimuth is unchanged by construction in the script, so that clause was not tested independently.
- **A2 not killed.**
  - The pushed-forward uniform sky equals (1 − β²)/(4π(1 − β cos θ′)²) and Kato and McCullagh's d = 2 member to
    5·10⁻⁴⁸ or better.
  - The 2 + 1 circle is the wrapped Cauchy to 2·10⁻⁴⁹ or better.
  - ρ = (k − 1)/(k + 1) = tanh(η/2) exactly: 0.0501, 1/3 and 0.8676 at β = 0.1, 0.6 and 0.99.
- **A3 not killed.** The address density is D² to 10⁻⁵¹. The blackbody's bolometric intensity is D⁴ of the rest frame's
  to 3·10⁻⁵¹.
- **A4 not killed.**
  - A turn about the motion moves no D (0 at 50 digits).
  - That the aberration contains no frequency is true by its form, not tested.
- **A5 killed in its letter**, through A1.

**A1′ (before run 2).**
- The stereographic clause, as a relative error: |z′ − z/k| / |z/k| < 10⁻⁴⁵ at the same seeded points.
- The azimuth tested independently: compute the observed direction's unit vector by the Lorentz transformation of the
  photon's momentum (not by keeping φ), and read its azimuth.
- *Killed* if either fails. A5′ reads A1′ for A1.
