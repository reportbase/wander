# UWR: the unequal write on a bench, a polarizer stack

9 Nov 2026. Tom: "1,2,3,4", the second "the unequal write in data" (after BRL run 3, SPN R784: a turn and a stretch V = cH,
taken and undone, leave a squeeze of rapidity ζ, cosh ζ = 1 + 2·sin²α·sinh²(½ ln c), growing each loop).

## The physical instance (stated before the run)

In Jones calculus a rotator turning the polarization by α is R(α), and a partial (linear) polarizer with amplitude
transmissions 1 along x and t = 1/c along y is diag(1, 1/c) = (1/c)·diag(c, 1): the stretch, up to a scale. Its inverse is
not passive, but up to a scale it is the same polarizer turned a quarter: diag(1, c) = R(90°)·diag(c, 1)·R(−90°). So BRL's
loop S⁻¹R⁻¹SR is, up to an overall loss, the passive stack: rotator α, polarizer along x, rotator −α, polarizer along y
(both of extinction ratio t = 1/c). The squeeze shows as the stack's net diattenuation D, which a polarimeter measures.

Known beforehand: Jones (1941); diattenuation from the Jones matrix's singular values, D = (σ₁² − σ₂²)/(σ₁² + σ₂²); Lu and
Chipman (1996). Nothing here is new physics; it is BRL's squeeze put where a bench reads it.

## Predictions (written before the run; exact, mpmath 60 digits)

- U1. The identity diag(1, c) = R(90°)·diag(c, 1)·R(−90°), and the stack's Jones matrix equals (1/c²)·M·(a turn), M = BRL's
  loop matrix, to 10⁻⁵⁰ at 40 seeded (α, c). (The stack's last element is the y-polarizer; the order fixed as in BRL.)
- U2. The stack's net diattenuation D = √(F² − 4)/F with F = ‖M‖²_F (det M = 1), zero exactly when c = 1 or α ∈ πℤ; at
  α = 40°, c = 2 a number in (0, 1), stated by the run.
- U3. D ≥ tanh 2ζ for every draw (a matrix's largest stretch is at least its eigenvalue), equality only where M is
  symmetric.
- U4. n stacks in a row: 1 − D_n falls as about 2·e^(−4nζ) (the squeeze accumulating, B11's growth seen as polarization).
  Checked at n = 1 … 8 for three draws: the slope of ln(1 − D_n) against n within 2% of −4ζ by n = 8.
- Kill: any of U1–U4 failing at the stated tolerance.

## What a data test would need

A bench measurement of D for the stack at several α and t, against U2. No published dataset of this exact stack was
looked for in run 1; the run below only checks that the instance is exact.

## Runs

### Run 1 (9 Nov 2026), `runs/uwr/uwr.py` (60 digits), output `runs/uwr/uwr-run1.txt`; nothing killed

- U1 held: diag(1, c) = R(90°)·diag(c, 1)·R(−90°) to 6·10⁻⁶¹. The stack (rotator α, polarizer along x, rotator −α,
  polarizer along y, each polarizer's extinction ratio 1/c), divided by the square root of its determinant, is BRL's M
  itself up to sign, to 1.2·10⁻⁶⁰. The predicted extra turn is not there: the stack is M times a scalar.
- U2 held: D = √(F² − 4)/F matches the stack's own singular values to 1.2·10⁻⁶⁰. It vanishes at c = 1 and at α = π (to
  10⁻³⁰, the square root of a 10⁻⁶⁰ residue). At α = 40°, c = 2: D = 0.7307, with ζ = 0.4507.
- U3 held: D ≥ tanh 2ζ (0.7170 at α = 40°, c = 2) at every draw.
- U4 held: n stacks in a row, the slope of ln(1 − D_n) at n = 8 is −4ζ to 10⁻⁶ (−4.01798, −3.93801, −8.50262).

Reading: the unsteady breath has a passive instance on any optical bench. Four elements (two rotators, two partial
polarizers crossed) make BRL's loop exactly; the squeeze is the stack's diattenuation, and repeating the stack drives it
toward a perfect polarizer at 4ζ a stack in ln(1 − D). With the polarizers equal in both axes (c = 1, no polarization,
the one-length write) it vanishes. Classical Jones calculus; the reading ours.

What a data test still needs: a polarimeter's measurement of D for this stack at several α and t, against U2's numbers.
None was looked for; a bench of two wave plates and two polarizers would do it.
