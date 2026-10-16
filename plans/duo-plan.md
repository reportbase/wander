# DUO: the contrast against the two paths' shares, on published neutron data

*15 October 2026 (Tom's local date). Tom, about 21:04: "whats next while I try to download the pdf". The PDF is
Summhammer, Rauch and Tuppinger (1987), "Stochastic and deterministic absorption in neutron-interference experiments",
Phys. Rev. A 36, 4447–4455, doi:10.1103/PhysRevA.36.4447. These predictions were written before the paper was read.*

## The claim

WVP run 4 (`plans/wvp-plan.md`) found single photons' contrast at most the two slits' facing 2hv, with the pair at its
corner (equal shares). It could not show the facing away from the corner. SPN R279 read that bound as the duality relation
V² + P² ≤ 1 (Greenberger and Yasin 1988; Englert 1996), with V = 2hv = sin 2θ and P = |h² − v²| = |cos 2θ|. This test
takes the pair off its corner, on a published measurement. One path of a neutron interferometer is attenuated to
transmission a, so the two paths' shares are 1 : a.

**The bridge.** The transmission a is an amount, measured by the paper as the counts with the absorber over the counts
without it, in that path alone. The shares carry it into unit relations by the Born rule: h = 1/√(1 + a), v = √(a/(1 + a)),
tan θ = √a. The contrast is read relative to the empty interferometer's, C/C₀, which divides out the instrument's own
coherence.

## The two ways to attenuate, read in the geometry

- **Stochastic (a foil):** each neutron passes with probability a, independently. Every neutron that arrives is one pure
  pair with amplitudes 1 and √a. The contrast is the facing: C/C₀ = 2hv = 2√a/(1 + a) = sech(½ ln(1/a)). The pair
  stands ½·log₂(1/a) levels from its corner. On the duality circle: V² + P² = 1.
- **Deterministic (a chopper open a share a of the time, or a lattice of bars):** for a share a of the time both paths
  are open, a pair at its corner. For the rest one path is shut. The counts are a mixture, not one pair. The mean
  intensity is the foil's (1 + a)/2, so P is the same, (1 − a)/(1 + a). But C/C₀ = 2a/(1 + a), below the facing for every
  a < 1, so V² + P² < 1.

Same counts, same P, two contrasts: only the pure pair reaches its facing. If the paper reports the interference
amplitude rather than the contrast, the forms are √a (stochastic) and a (deterministic), relative to the empty
instrument's. Both forms are classical quantum mechanics, and the paper's abstract says the two were "observed in
agreement with prediction". Known beforehand: that sentence, and the √a and a forms (from a later preprint quoting the
paper). What is ours is only the reading: the foil's contrast is the facing in levels, 2hv = sech of the levels between
the amplitudes, and the chopper's is a mixture of corner and home.

## Predictions (written before the paper was read)

For every measured point, with the paper's own error bars (σ, the combined error of C/C₀ if it gives C and C₀ apart):

- **D1. Foils on the facing.** Each foil's C/C₀ within 2σ of 2√a/(1 + a), or its amplitude within 2σ of √a. *Killed if*
  more than one point in twenty is outside, or any is outside 3σ.
- **D2. Chopper below it.** Each chopper point within 2σ of 2a/(1 + a) (amplitude a), with the same allowance. *Killed if*
  as for D1.
- **D3. The two told apart.** Where the paper has a foil and a chopper at about the same a (within 0.05), the foil's
  C/C₀ is the larger, by at least 2σ wherever 2√a/(1 + a) − 2a/(1 + a) exceeds 4σ. *Killed if* not.
- **D4. The lattice.** An absorbing lattice whose bars are wider than the neutron's lateral coherence acts as a
  deterministic attenuator in space: C/C₀ within 2σ of 2a/(1 + a), where a is the lattice's open share. *Killed if* its
  points sit on the foil's form instead (more than half within 2σ of 2√a/(1 + a) and outside 2σ of 2a/(1 + a)). If the
  paper gives the bars as narrower than the coherence, D4 is not tested.

What a kill would mean: D1 or D2 failing means that either the paper's numbers, or my reading of its set-up (what a and
C₀ are), differs from the textbook forms. That is not a test of the geometry, since the forms are classical. D3 failing
would mean the measurement cannot tell a pure pair from a mixture at these errors. D4 is my guess at an experiment
whose set-up I have not yet read.

## Procedure, fixed now

- Read the paper's tables first. If the values exist only as figure points, read them from the figure by the axis
  ticks, and record each reading and its uncertainty (half a marker) before comparing.
- Take a from the paper's own transmission measurement for each absorber, not from nominal thicknesses.
- If the paper corrects for the absorber's small-angle scattering or phase shift, use its corrected values and say so.
- The script (`duo/duo.py`) holds the values transcribed by hand, with page and table numbers, and prints each point
  against both forms.
- The PDF is not committed. Its sha256 goes here when it arrives.

## Runs
