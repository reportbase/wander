# CXB: where the sweep reading of chaos ends

*13 November 2026, SPN R928. Tom: "4", to Claude's option 4: check where essay 21 §9's reading of chaos ends. Exact and
seeded arithmetic, no data. The plan and its predictions are written and committed before any run. Nothing above the
"Runs" line is edited afterwards.*

## The question

Essay 21 §9 says that the logistic map at its fullest setting, y ↦ 4y(1 − y), is a sweep composed with itself seen in
another chart. In the weight chart it becomes the tent map, which stretches by exactly 2 everywhere, so its rate is ln 2
a step with no averaging, and a run spends one binary digit of its start per step. R927 adds that chaos's stretch belongs
to the rule and its unpredictability to the write.

Two things need checking. Does the sweep picture, meaning a chart in which the rule is a constant stretch, reach ordinary
chaos at all? And does "a run spends its start's digits at the rule's rate" hold where it does not?

## Known beforehand (from memory, not checked for this plan)

- At r = 4 the chart y = sin²(πw/2) turns the logistic map into the tent map exactly (Ulam and von Neumann 1947).
- Every unimodal map with positive entropy is semiconjugate to a tent map of slope e^(h_top) (Milnor and Thurston 1988),
  but the conjugacy is generally not smooth.
- For a map of an interval with an absolutely continuous invariant measure μ, the measure's entropy equals its Lyapunov
  exponent, h_μ = λ (Ledrappier 1981; Pesin's formula), and h_μ ≤ h_top (the variational principle).
- For rational maps, the maximal-entropy measure is smooth only for the exceptional maps: power maps, Chebyshev
  polynomials and Lattès maps (Zdunik 1990). I take the interval form of this as known but have not checked a source.
- The step this plan relies on: if a smooth chart turned the map into a constant stretch s, then λ = ln s = h_top. So
  **λ < h_top strictly shows that no such chart exists**, and λ = h_top is the mark of the exceptional case.
- CHS (R833) computed the r = 4 case. draw's labs are not attached to this session and were not checked.

## Method (fixed now)

- **The map.** f_r(y) = r·y·(1 − y) on [0, 1], at r = 4 (exceptional) and r = 3.7, 3.8, 3.9 (generic). A second
  exceptional case: the Chebyshev cubic T₃(x) = 4x³ − 3x on [−1, 1].
- **λ, the rate.** The mean of ln|f′| along orbits: 200 seeded starts, 10⁴ transient steps dropped, 10⁵ steps kept, in
  binary64. The standard error is taken over the starts.
- **h_top, the entropy.** From the growth of the count N_k of k-th preimages of the critical point (y = ½ for the
  logistic map; x = ±½ for T₃), each preimage solved in closed form. h_top is the least-squares slope of ln N_k against k
  over the last eight k before N_k passes 2·10⁷.
- **The chart at r = 4.** The identity f₄(sin²(πw/2)) = sin²(π·T(w)/2), with T the tent map, checked at 1,000 seeded w
  to 60 digits.
- **Digits per step.** Orbits carried in mpmath at p = 53, 100 and 200 bits, against the same start carried at p + 400
  bits. The parting step is the first n with |y_p − y_ref| > 0.1, averaged over 50 seeded starts at each p and r. The
  prediction is n ≈ p·ln 2/λ.

## Predictions (written before any run)

- **X1 (the exceptional case closes).** At r = 4: the chart identity holds to 10⁻⁵⁰ at every point; λ = ln 2 within 3
  standard errors; h_top = ln 2 within 0.01. For T₃: λ = ln 3 within 3 standard errors, and h_top = ln 3 within 0.01.
  *Killed* otherwise.
- **X2 (generic chaos has no such chart).** At each of r = 3.7, 3.8, 3.9: 0 < λ < h_top < ln 2, with h_top − λ ≥ 0.02.
  *Killed* if any gap is under 0.02 while λ > 0. Separately, a gap below −0.01 would break the variational principle,
  which I would read as a fault in the code.
- **X3 (digits per step hold in general).** At every r tested (4, 3.7, 3.8, 3.9) and every p, the mean parting step is
  within 20% of p·ln 2/λ. *Killed* if it is off by more than 20% at more than two of the twelve (r, p) points.

## What would and would not be shown

- X1–X3 not killed:
  - The sweep reading (a chart with a constant stretch, the rate read off the rule) is the exceptional case only, marked
    by λ = h_top.
  - Ordinary chaos at r = 3.7 to 3.9 has no such chart.
  - Spending the start's digits at λ/ln 2 bits a step holds in both cases. So R927's "the unpredictability is the write's"
    stands for chaos in general, and essay 21 §9's sweep picture does not.
- All of this is classical (Ulam–von Neumann, Milnor–Thurston, Ledrappier, Pesin, Zdunik). The test checks where the
  essay's reading stops; it finds nothing new about chaos.

## Runs
