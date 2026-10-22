# TPR P5: the 65 sorted by the address and the payload

*22 October 2026. Sorted by Claude (not blind) from each entry's derivation note in `plans/tpi/catalogue.md`,
`plans/tpi/neutral-list.md` and its computation in `plans/tpi/tpi.py`, after `plans/tpr-plan.md`'s predicted counts
were written and before they were tallied. Classes as the plan defines them:*

- **M**: a mean, over the turn's uniformly laid addresses, of a bounded amount that is a first power of the projection
  (|cos|, |sin|, a chord, a first Fourier coefficient, sin θ/θ at the quarter turn read as the mean of cos, an elliptic
  mean), or a ratio with such a mean in it. A payload operation over addresses; needs the turn uniform.
- **L**: the turn's total length only, or a normaliser by a square whose mean (½) the exchange fixes. Needs no
  uniformity.
- **B**: a share, the turn's measure of a set of addresses, (2/π)·θ (a distribution function, a sign or separation
  probability, a width as a share of the period). The address's: ½ at the corner under every fair weight.
- **S**: the circle held as a shape (TPI's route S).
- **O**: other (a pole, a dimension, a convention, not traced, or a log climb).

| ID | name | class | why (one line) |
|---|---|---|---|
| K1 | half-Cauchy distribution function | B | (2/π)·arctan s, the share of the quarter turn below s |
| K2 | Buffon's needle | M | crossing probability = (ℓ/d)·mean |cos θ| over the needle's angle |
| K3 | Viète's formula | M | the product is sin θ/θ at the quarter turn: the mean of cos over it |
| K4 | arcsine law | B | (2/π)·arcsin √t, the share of the quarter turn with sin²θ ≤ t |
| K5 | averaging AC meter | M | mean |sin| over a phase uniform in time |
| K6 | square pixel at Nyquist | M | mean of cos over a half turn of phase across the pixel |
| K7 | Van Vleck | B | 1 − 2·(share of directions separating the two signs), (2/π)·arcsin ρ |
| K8 | Kosterlitz–Thouless jump | O | the 2 is the plane's dimension; the π the winding's energy (a uniform winding the least) |
| K9 | ARE median vs mean (normal) | L | 4f(0)², f(0)² = 1/(2π): the pair's full turn's length, no projection averaged |
| K10 | (E|Z|)², one-bit loss | M | E[R²]·mean |cos φ sin φ| over the pair's uniform angle |
| K11 | half-wave dipole | M | mean of cos over the half turn of phase along the wire |
| K12 | rolling wheel's rim speed | M | mean |sin(φ/2)| over the wheel's turn, a chord |
| K13 | 2D effusion | M | mean of cos over the half turn of velocity directions |
| K14 | Jordan's inequality | M | the chord's slope sin θ/θ at the quarter turn |
| K15 | Flamant | L | 1/∫cos² over the half turn: the exchange's ½ times the half turn's length |
| K16 | Hertz line contact | S | a semi-ellipse's area on a given width |
| K17 | Wigner's semicircle | S | a semicircle's area on a given support |
| K18 | Sato–Tate | L | 1/∫sin² on [0, π] (Haar measure): the exchange's ½ times the half turn |
| K19 | Chebyshev / equilibrium measure | B | its law (2/π)·arcsin √x, a share of evenly spaced angles |
| K20 | Goemans–Williamson | B | separation probability θ/π, a share of normals; the ratio a minimum over it |
| C1 | Wallis product | M | sin x/x at x = π/2 (Euler's product), the quarter turn's mean of cos |
| C2 | Bauer–Ramanujan | O | step not traced |
| C3 | square-wave coefficient | M | ∫sin/∫sin² over a half turn: a first-power mean over a square's |
| C4 | Wilbraham–Gibbs | M | the square wave's 2/π (C3) times Si(π) |
| C5 | Fourier sine/cosine transform | L | the inversion's normaliser, Dirichlet's ∫ sin x/x = π/2: the half turn's length |
| C6 | Lebesgue constant (Chebyshev nodes) | O | (2/π) per e-fold of n: a mean of cot over even node angles, unbounded, climbing like the Cauchy's absent mean |
| C7 | Kac's real roots | M | crossings per unit length E|Y|·f_X(0) = 1/π, a mean over the pair's turn (then summed over a log range) |
| C8 | alternating permutations | O | the pole of sec + tan at π/2 |
| C9 | (2/π)K(k) = 1/agm | M | the mean of 1/√(1 − k²sin²θ) over the quarter turn |
| C10 | Struve H₁ − Y₁ → 2/π | L | 1/(Γ(½)Γ(3/2)): Γ(½)² the pair's full turn's length |
| C11 | Nesterov | B | (2/π)·arcsin, a sign-agreement share |
| C12 | Krivine | B | the same sign-rounding share |
| C13 | Kendall's τ | B | 4·(the whitened quadrant's share of the turn) − 1 |
| C14 | semicircular arc's centroid | M | mean sin over the arc's angle |
| C15 | mean chord on a circle | M | mean sin(θ/2) over the central angle |
| C16 | pendulum period | M | (2/π)K: the mean over u of the elliptic integrand |
| C17 | Onsager's Ising energy | M | (2/π)K, a mean over Fourier modes' angles |
| C18 | infinite resistor grid | M | the Brillouin zone's mean of a bounded function of the phases |
| C19 | random sticks' excluded area | M | mean |sin γ| over the relative angle |
| C20 | Stoner–Wohlfarth (in plane) | M | mean cos over the easy axes |
| C21 | Bell's local model | B | the share of hidden directions separating the outcomes, θ/π |
| C22 | Kramers–Kronig, one-sided | L | a half residue, iπ: the half turn's length about the pole |
| C23 | Gaussian beam | O | the 1/e² radius convention (the azimuth's 2π a length) |
| C24 | binary phase grating | M | a first Fourier coefficient of a ±1 wave |
| C25 | thin disc's capacitance | S | the radial arcsine integral on a given radius |
| C26 | Wheeler's microstrip | O | not traced (a Schwarz–Christoffel jump of iπ, by the classifier) |
| C27 | baffled piston | L | as C10 (and the face's area πa²) |
| C28 | penny-shaped crack (Irwin) | L | 1/E(0) = 1/∫dφ over the quarter turn: its length alone |
| C29 | Sneddon's cone | S | the Abel/arcsine integral on a given radius |
| C30 | Oliver–Pharr ε | S | from C29 |
| C31 | loaded circle on a half-space | M | the mean over the polar angle of a chord √(1 − sin²φ) |
| C32 | stress drop, long fault | S | the area under a semi-elliptic slip on a given width |
| C33 | fibres in a plane | M | mean |cos| over the fibre angle |
| C34 | relay describing function | M | the square wave's first coefficient |
| C35 | saturation describing function | M | a first Fourier coefficient of the clipped sine |
| C36 | six-step inverter | M | the square wave's first coefficient |
| C37 | switching mixer | M | the LO square wave's first coefficient, halved |
| C38 | class B stage | M | the rectified sine's mean |
| C39 | air-gap MMF | M | the rectangular MMF's first coefficient |
| C40 | square vs sine grating threshold | M | the square wave's first coefficient |
| C41 | Coltman's relation | M | the square wave's series, inverted |
| C42 | canopy G, vertical leaves | M | mean |cos φ| over leaf azimuth |
| C43 | animal encounter (2D gas) | M | mean sin(θ/2) over the relative heading |
| C44 | rotational broadening | S | a half disc's area (chords across a given disc) |
| C45 | Fabry–Pérot linewidth | B | the FWHM as a share of the round-trip phase's turn, (2/π)·arcsin |

## Counts

| class | count | predicted |
|---|---|---|
| M | 34 | 32 ± 5 |
| L | 8 | 10 ± 3 |
| B | 10 | 12 ± 3 |
| S | 7 | 7 |
| O | 6 | 5 ± 1 |

Total 65. Judgment calls, each of which could move one entry: C5 (L, or M as "the inner reading summed"), C6 (O, a log
climb, or M), C7 (M through the hidden pair, or O as a log climb like C6), K3, K14 and C1 (M, read as the quarter turn's
mean of cos; an identity has no weight to change), C17 and C18 (M; lattice integrals, no physical turn), K9 and C10 (L;
TPI's hidden turns, the pair's whole turn as a length).
