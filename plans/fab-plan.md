# FAB: the Tangent Bridge's open floor, and what proves it

*26 November 2026. Tom: "Proceed with B", Claude's item B after TBH: the one step the Tangent Bridge leaves open
(draw, `papers/tb_algebra.md`, Appendix A.6). That step is the floor on the *average* Lebesgue function over every set of
places, the bound that would make Faber's envelope reachable from the operation's own means. The appendix found the floor
not reachable by order and counting (its logarithm lives in the kernels' far tails), so far reached only by the conjugate
function, a completed dual. It names the combination law's rotation as the candidate replacement. Predictions written and
committed before the script (`runs/fab/fab.py`) exists; float64 and numpy/scipy.*

## Known beforehand (a search before the plan, not a discovery)

- **Erdős and Szabados (1978)**, *On the integral of the Lebesgue function of interpolation*, Acta Math. Hungar. 32,
  191–195: ∫_I λ ≫ |I| log n for any n nodes in [−1, 1], n large depending on I; constants not sharp.
- **Tao (2026)**, *Local Bernstein theory, and lower bounds for Lebesgue constants*, arXiv:2603.21453 (v3, 22 April 2026;
  read here through its abstract, the first part of the v2 HTML and the author's blog post of 23 March, by a fetch agent;
  not checked against peer review). Theorem 1.10: for any distinct x₁ < … < x_n in [−1, 1] and a fixed I,
  ∫_I λ ≥ (4|I|/π²)·log n − o(log n), sharp (Chebyshev nodes), and sup_I λ ≥ (2/π)·log n − O(1). A trigonometric toy
  model (the blog's Problem 3): for a real trigonometric polynomial P of degree n with 2n roots x_k in [0, 2π),
  ∫₀^{2π} Σ_k |P(x)|/|P′(x_k)| dx ≥ 8, sharp for the sinusoid. Its proof factors the integral as
  (∫|P|)·(Σ 1/|P′(x_k)|), bounds the first by an L¹ duality "based ultimately on the Fourier expansion of the square
  wave", the second through the residue theorem applied to e^{inz}/P(z), and passes to the real line by contour shifts
  (Paley–Wiener) and the author's local Bernstein theory (Nevanlinna's two-constant theorem, harmonic measure on
  rectangles).

So the floor TB A.6 left open is **proved**, on the interval, for arbitrary nodes, with the sharp constant, and the known
proof uses exactly what the appendix expected: a completed dual (the square wave's Fourier series) and contour integrals
round closed loops (residues). Whether it can be reached by order and counting alone stays open, and is not what this run
can settle.

## What the run tests

The toy model on the circle, the circle's own Lebesgue function at arbitrary places, and where π sits in the toy's
constant (TB §7.5 located 2/π's π in the normalization).

## Predictions

- **F1 (the toy floor holds and the sinusoid meets it).** For P(x) = ∏ sin((x − x_k)/2) over 2n roots: the product
  (∫₀^{2π} |P|)·(Σ_k 1/|P′(x_k)|) equals 8 to ≤ 10⁻⁹ for equally spaced roots (n = 2, 4, 8, 16), and is ≥ 8 for
  10,000 random root sets per n (n = 4, 8) and at the end of 20 local minimizations from random starts per n, each ending
  at ≥ 8 − 10⁻⁶.
- **F2 (the toy's constant has no π).** For the sinusoid sin(nx) the two factors are ∫|P| = 4 and Σ 1/|P′| = 2 (A = 1):
  rational, each computed with zero trigonometric calls (the first from the slope form 2·[−1/√(1 + s²)]₀^∞ per arch, the
  second from P′ at the roots by the leaf lattice of TB §11.1 and rational double-angle steps). π enters only when the
  integral is turned into a mean, dividing by the turn's 2π.
- **F3 (on the circle, equal spacing is the least average).** For trigonometric interpolation of degree n at N = 2n + 1
  places, the mean of the Lebesgue function over the circle is least, among 20 local minimizations from random starts per
  N (N = 9, 17), at the equally spaced places: no start ends below the equally spaced mean by more than 10⁻⁶.
- **F4 (the equally spaced mean's slope is 4/π²).** For N = 2n + 1 from 65 to 4097 the mean of λ at equal spacing fits
  a·ln N + b with a within 2% of 4/π² = 0.40528.
- **F5 (the rotation alone gives no floor).** The mean of λ over the circle equals the mean, over uniform turns of the
  places, of λ at one fixed point (Fubini, to ≤ 10⁻¹⁰ on the grid). So TB A.6's candidate, read as a turn of the places,
  restates the average and supplies no lower bound by itself: for some set of places at every N tried (N = 9, 17, 33), λ
  at one fixed point is below 1.1 for a positive share (≥ 10%) of turns, so a floor must come from the whole average,
  not from any one turned read.

Each is killed by its own number. F1 restates a proved theorem and F4 a classical asymptotic; they are checks of the
script. F3 is the circle's counterpart of a conjecture Erdős's group stated for Chebyshev nodes on the interval (Tao's
reference [12]) and can fail. F5 is an argument with a measurement.

## What would follow, if nothing is killed (a reading, to rule on)

The open step of the Tangent Bridge's inversion is closed in the classical literature, and closed with the DHV's tools: a
completed dual and integrals round closed contours. That fits the bridge's own sorting: the floor over every set of
places is a quantifier over objects no read constructs, and its known proof completes the circle. The toy shows the same
split as TB §7.5: its sharp constant 8 is rational and computed with no angle; π appears only when the total becomes a
mean over the turn. The residue theorem is the Cauchy kernel 1/(x − z) integrated round a whole loop: the read's own
kernel (its density the imaginary part), completed. The candidate rotation reduces to a change of order of averaging and
carries no floor.

## Runs

