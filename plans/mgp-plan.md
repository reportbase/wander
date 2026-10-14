# MGP: the marginalization paradox and the reader's size

*14 October 2026 (Tom's local date). After WWP (SPN R245), Claude suggested answering the standard objection to
measures that cannot be normalized, Dawid, Stone and Zidek's marginalization paradoxes, before an outside reader raises
it; the corpus leans on dκ/κ for the other party's size. Tom, about 13:00: "yes". Exact arithmetic where it is
rational, mpmath at 50 digits elsewhere; predictions written before the script (`mgp/mgp.py`) exists.*

## The objection, as read

- **Stone and Dawid** (1972, *Biometrika* 59(2), 369–375) and **Dawid, Stone and Zidek** (1973, *JRSS B* 35(2),
  189–233; not read in full here): a Bayesian B₁ with parameters (η, ζ), interested in ζ, puts an improper prior on the
  nuisance η; the data split as x = (y, z) so that B₁'s posterior for ζ depends on z alone, while z's own sampling
  law depends on ζ alone. A second Bayesian B₂ reasons from z's law directly and cannot reproduce B₁'s posterior with
  any prior. The first example (as quoted in the literature): X, Y exponential with hazard rates θφ and φ; Z = Y/X has
  a law depending on θ alone.
- **Jaynes** (1980, "Marginalization and prior probabilities", in Zellner (ed.), essays in honour of Jeffreys;
  reprinted in Rosenkrantz (ed.) 1989, 337–375; his preprint's first six pages read, `margin.pdf` from bayes.wustl.edu,
  sha256 3b371bf67829927d3d6ce700a661465ba04bc74dd03b9cd190541ffd1a758ff1): the fault is not B₁'s improper prior but
  B₂'s neglect of prior information; and, reporting DSZ: "if the sampling distribution … has a certain group structure
  …, the paradox can be avoided by choosing the prior as the right-invariant measure on S(η)", the nuisance's space.
  His DSZ Example 1 (change point): x₁ … x_n exponential, rate η for the first ζ and cη after; y = x₁, z_i = x_i/x₁.
- **Wallstrom** (arXiv math/0310006; 0708.1350): B₂'s procedure is not justified, so there is no reason to expect
  agreement and no inconsistency of improper priors; read as abstracts.
- **Ghosh** (2011, read): Jeffreys's general rule "suffers from many problems" with nuisance parameters, the
  marginalization paradox among them.

## The claim to test

The situated reader's nuisance is the other party's size κ (OFS §2): a scale, acted on by rescaling alone, which
commutes with the turns acting on what the reader reads. The corpus gives it dκ/κ. The prediction, from DSZ's group
condition as Jaynes reports it: for a scale nuisance, B₁ and B₂ agree exactly when the nuisance carries its own
invariant measure, dη/η, with the parameter of interest held fixed; any other power η^(−k) produces the paradox. Which
measure that is in the original coordinates depends on which parameter is of interest: worked by hand before writing
(stated so), in the normal example with interest ζ = μ/σ the nuisance σ at fixed ζ carries dσ/σ, which in (μ, σ) is
dμ·dσ/σ², Jeffreys's general rule; Jaynes's dμ·dσ/σ gives the paradox there.

Agreement is tested as factorization: B₁'s posterior is π(ζ)·a(ζ, z), B₂'s is π₂(ζ)·b(ζ, z); some π₂ reproduces B₁
for every z exactly when a/b is a function of ζ times a function of z. Both a and b are computed by numerical
integration, never from a closed form: a by integrating the full likelihood times η^(−k) over η; b as the density of the
scale-free data by the classical integral over the scale group, ∫ λ^(n−1) f(λx | ζ, η = 1) dλ (Wijsman's representation),
which needs no prior.

## Predictions

- **P1. Stone and Dawid's exponentials.** X ~ Exp(θφ), Y ~ Exp(φ), interest θ, nuisance φ with prior φ^(−k).
  B₁ and B₂ agree for every z = y/x exactly when k = 1; for k = 0, ½, 3/2 and 2 they do not. **Killed if**, at k = 1,
  a/b varies with z by more than 1e-30 relative over 50 values of z and 20 of θ; or, at any other k, the factorization
  test (a/b at (θ₁, z₁)(θ₂, z₂) against (θ₁, z₂)(θ₂, z₁)) passes everywhere to 1e-6.
- **P2. DSZ's change point** (Jaynes's Example 1): n = 6, c = 2, ζ ∈ {1, …, 5}, nuisance η with η^(−k). The same: only
  k = 1 agrees. **Killed if** as P1, over 50 random z vectors.
- **P3. DSZ's normal, interest μ/σ.** x₁ … x₄ normal (μ, σ²), ζ = μ/σ, nuisance σ with prior σ^(−k) at fixed ζ.
  Only k = 1 agrees, which is dμ·dσ/σ² in (μ, σ) (Jeffreys's general rule, the left-invariant measure of location and
  scale); k = 0, dμ·dσ/σ in (μ, σ) (Jaynes's, the right-invariant one), gives the paradox. **Killed if** as P1, over 50
  random data vectors.
- **P4. A general scale nuisance; the reader's size.** Amounts ℓ_i = κ·w_i, w_i drawn from a law with a scale-free
  parameter ζ (here Gamma with shape ζ), κ the unknown size: B₁ with κ^(−k) and B₂ from the ratios ℓ_i/ℓ₁ alone agree
  exactly when k = 1. So a reader that integrates the other's size out with dκ/κ reaches the same conclusions about
  everything scale-free as a reader that uses the ratios alone, and with no other power. **Killed if** as P1, n = 4,
  over 50 random data vectors and 20 values of ζ.

## What the run would and would not show

It would show that the marginalization paradox, in its own examples, does not reach a measure that is the nuisance's
own invariant measure, and that the situated reader's dκ/κ is that measure for its size; with the reader's group
commuting, there is no second candidate. It would also correct a reading in OFS §2: which of the location-and-scale
measures avoids the paradox depends on the parameter of interest, so "later work has favoured" the right-invariant one
holds for location or scale of interest, not for μ/σ. It would not show that improper priors are consistent in general
(Wallstrom's question), nor anything about B₂'s justification.

## Runs
