# HLX: are the holonomy laws rational in the leftover's half-slope?

14 November 2026. Tom: "merge, and run the holonomy ltest." (after NTN run 1, R990: the holonomy laws 89, 90 and 92
failed the notation rule only on their left side, cos(Θ/2), cosh ζ and tan(Θ/2); written with the leftover's own
half-slope each might be rational too, untested.)

## The question

Each holonomy law gives a loop's leftover (a turn Θ, or a squeeze ζ) in terms of its inputs. Write each input and the
leftover by its half-slope (a turn by its t = tan(angle/2), a squeeze by u = tanh(ζ/2), an angle between axes by its
cosine and sine from a rational unit vector). Is the leftover's half-slope then a rational function of the inputs'
(squared, so no sign is chosen), so that the law's π, e or angle is notation? And is it so when the loop is computed
directly from its four (or two) maps, not from the law's formula?

## Method (fixed before the run)

Exact rational arithmetic throughout (`runs/hlx/hlx.py`, Fractions). Inputs: half-slopes and rational unit axes
(Pythagorean triples), five cases per law.
- **89, the two-turn loop**: turns as unnormalised quaternions p = (1, t·n), the loop p_a·p_b·p̄_a·p̄_b; its scalar part
  over (1 + t_a²)(1 + t_b²) is cos(Θ/2), and τ² = |vector|²/scalar².
- **90, a turn and an unequal stretch**: the 2×2 loop L = S⁻¹·R(−α)·S·R(α), R from the turn's half-slope (rational), S =
  diag(√c, 1/√c) with c a square of a rational so S is rational; cosh ζ = tr(L)/2 (its eigenvalues e^(±ζ), the paper's
  §8; checked numerically against the law before this plan), u² = (cosh ζ − 1)/(cosh ζ + 1).
- **92, Thomas–Wigner**: two boosts as 4×4 Lorentz matrices with rational half-rapidities a, b (so β = 2a/(1 + a²) and
  γ = (1 + a²)/(1 − a²) are rational) along rational unit directions; the composite's boost read off its first column
  (rational), the rotation R = B(composite)⁻¹·B₂·B₁ (rational), cos Θ = (tr R − 1)/2, τ² = (1 − cos Θ)/(1 + cos Θ).
- **102, the Trotter leftover** (θ₁θ₂/2)·sin(φ/2)/(φ/2): a leading-order term of a limit, not an exact loop; predicted
  content (H4), checked by its form only.

## Predictions (committed before the run)

- **H1** For 89, τ² is rational at all five cases and equals the law's restatement: cos(Θ/2) = 1 − 2·(t_a²/(1 + t_a²))·
  (t_b²/(1 + t_b²))·(1 − (n_a·n_b)²), τ² = 1/cos²(Θ/2) − 1. Kill: any miss.
- **H2** For 90, u² is rational and equals the law's 1 + 2·(4t²/(1 + t²)²)·((c − 2 + 1/c)/4) as cosh ζ. Kill: any miss.
- **H3** For 92, τ² is rational and equals (ab·sin φ/(1 + ab·cos φ))², φ the angle between the boosts' directions.
  Kill: any miss.
- **H4** 102 is not restatable exactly: it is the leading term of a loop, and its φ/2 stands bare; by NTN's rule it stays
  content, a limit. Kill: an exact restatement in slopes is found.

If H1–H3 hold, the holonomy laws' angles are notation once the leftover is written by its half-slope, and what was left
of π and e as content in NTN is the limits and the charts or totals stated for themselves.

## Runs

(appended below as they come out; nothing above this line edited afterwards)
