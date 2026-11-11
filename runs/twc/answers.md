# Answers

"Check" is the value from `check.py` (30 working digits), computed independently of the closed form.

1. **Mean distance between two uniform points in the unit square** = (2 + √2 + 5·ln(1 + √2))/15.
   π: no. e: no.
   Closed form: 0.521405433164721. Check: 0.521405433164721 (2D quadrature of 4(1 − u)(1 − v)√(u² + v²) over the unit square).
   Key step: the coordinate differences have triangular densities; the remaining integral is elementary in polar form.

2. **Limiting proportion of derangements** = 1/e.
   π: no. e: yes.
   Closed form: 0.367879441171442. Check: 0.367879441171442 (D₄₀/40! from the recurrence D_n = (n − 1)(D_{n−1} + D_{n−2})).
   Key step: inclusion–exclusion gives D_n/n! = Σ_{k≤n} (−1)^k/k!.

3. **Mean distance between two uniform points in the unit disc** = 128/(45π).
   π: yes. e: no.
   Closed form: 0.905414787367227. Check: 0.905414787367227 (2D quadrature: polar coordinates about the first point, chord length cubed over 3).
   Key step: Crofton's differential argument, or the distance density integrated directly.

4. **iⁱ (principal value)** = e^(−π/2).
   π: yes. e: yes.
   Closed form: 0.207879576350762. Check: 0.207879576350762 (exp(i·Log i), Log i by quadrature of dz/z along the segment from 1 to i; imaginary part below 10⁻²⁵).
   Key step: Log i = iπ/2, so iⁱ = exp(i·iπ/2).

5. **Input resistance of the infinite ladder of 1 Ω resistors** = (1 + √5)/2 Ω, the golden ratio.
   π: no. e: no.
   Closed form: 1.61803398874989. Check: 1.61803398874989 (200 iterations of R ← 1 + R/(1 + R)).
   Key step: R = 1 + R/(1 + R) gives R² − R − 1 = 0.

6. **∫₀¹ ln x · ln(1 − x) dx** = 2 − π²/6.
   π: yes. e: no.
   Closed form: 0.355065933151774. Check: 0.355065933151774 (direct quadrature).
   Key step: expand ln(1 − x) = −Σ xⁿ/n; the integral is Σ 1/(n(n + 1)²) = 2 − ζ(2).

7. **Σ_{n≥0} n³/n!** = 5e.
   π: no. e: yes.
   Closed form: 13.5914091422952. Check: 13.5914091422952 (direct summation).
   Key step: n³ = n(n−1)(n−2) + 3n(n−1) + n, each falling factorial summing to e; 1 + 3 + 1 = 5, the third Bell number (Dobiński).

8. **Lévy's constant, lim q_n^(1/n) for almost every x** = e^(π²/(12 ln 2)).
   π: yes. e: yes.
   Closed form: 3.27582291872181. Check: 3.27582291872181 (exp of −(1/ln 2)·∫₀¹ ln x/(1 + x) dx by quadrature).
   Key step: the ergodic theorem for the Gauss map gives (1/n)·ln q_n → −∫₀¹ ln x/((1 + x) ln 2) dx = π²/(12 ln 2).

9. **Density of squarefree integers** = 6/π² (= 1/ζ(2)).
   π: yes. e: no.
   Closed form: 0.607927101854027. Check: 0.607927101854027 (Euler product ∏(1 − p⁻²) as exp(−Σ_k P(2k)/k), prime zeta sums).
   Key step: the product over primes of (1 − p⁻²) is 1/ζ(2), and ζ(2) = π²/6.

10. **∫₀¹ arctan(x)/x dx** = G, Catalan's constant, Σ_{k≥0} (−1)^k/(2k + 1)².
    π: no. e: no.
    Closed form: 0.915965594177219. Check: 0.915965594177219 (direct quadrature against mpmath's `catalan`).
    Key step: integrate the arctangent series term by term.

11. **Smallest base a for which the tower a^a^a^… converges** = e^(−e).
    π: no. e: yes.
    Closed form: 0.0659880358453125. Check: 0.0659880358453125 (root of the system a^x = x, x·ln a = −1).
    Key step: the fixed point's multiplier is x·ln a = ln x; it equals −1 at x = 1/e, so a = (1/e)^e (Euler 1783).

12. **∫_{−∞}^{∞} cos x/(1 + x²) dx** = π/e.
    π: yes. e: yes.
    Closed form: 1.15572734979092. Check: 1.15572734979092 (oscillatory quadrature on the half line, doubled).
    Key step: the residue of e^(iz)/(1 + z²) at z = i is e^(−1)/(2i); 2πi times it is π/e.

13. **∫₀^∞ x³/(eˣ − 1) dx** = π⁴/15 (the Stefan–Boltzmann integral).
    π: yes. e: no.
    Closed form: 6.49393940226683. Check: 6.49393940226683 (direct quadrature).
    Key step: expand 1/(eˣ − 1) as Σ e^(−nx); the integral is Γ(4)·ζ(4) = 6·π⁴/90.

14. **Limiting probability that a fair walk is positive at most a quarter of the time** = 1/3.
    π: no. e: no.
    Closed form: 0.333333333333333. Check: 0.333333333333333 (the limit law, its normalisation by quadrature); 0.333333792771399 from the exact discrete law at 400,000 steps (finite-n error of order 1/n).
    Key step: the arcsine law, P = (2/π)·arcsin √(1/4) = (2/π)·(π/6); the π cancels.

15. **Expected number of uniform(0, 1) draws for the running sum to exceed 1** = e.
    π: no. e: yes.
    Closed form: 2.71828182845905. Check: 2.71828182845905 (exact rational sum of P(S_n ≤ 1), n < 40, each by repeated polynomial integration).
    Key step: P(S_n ≤ 1) = 1/n!, the simplex's volume, and E[N] = Σ_{n≥0} P(N > n) = Σ 1/n!.

Groups: π only 3, 6, 9, 13; e only 2, 7, 11, 15; both 4, 8, 12; neither 1, 5, 10, 14.
