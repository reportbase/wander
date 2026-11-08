# OPL: is "one pole, the constant and the phasor" special to the Cauchy?

8 Nov 2026. Tom: "proceed", to the question left open after R753–R754 (ChatGPT: "ask whether the same
standpoint-centered construction explains other familiar transforms or kernels, or whether this unity is distinctive to
the Cauchy/Poisson kernel").

## What is being tested

R753: from a standpoint z = m + iγ the Cauchy kernel (1/π)·γ/((s − m)² + γ²) has one simple pole above the line, at z;
its characteristic function φ(t) = ∫ e^(its)·kernel ds is, for t > 0, that one residue, e^(izt): a pure phasor, the foot
turning it and the height damping it, and at t = 0 the same residue is the total. The question is whether any other
familiar kernel has this unity: one point off the line that gives both the total and the whole response to a turn as
one phasor.

Known beforehand (classical, stated so the predictions are not mistaken for discoveries): the Fourier transform is
one-to-one, so a φ equal to e^(imt − γ|t|) belongs to the Cauchy and nothing else; Jordan's lemma and the residue
theorem give the transform of a rational or meromorphic kernel as a sum over its poles in the upper half-plane, a pole
of order r giving a polynomial of degree r − 1 in t times e^(ipt); the Gaussian is entire; the hyperbolic secant has
poles at i(2k + 1); the Laplace kernel's transform is 1/(1 + t²) and the Cauchy's is e^(−|t|) (the two are each
other's transforms).

## Kernels

All normalized to total 1, centred at 0, scale 1:
- C: Cauchy, 1/(π(1 + s²)).
- G: Gaussian, e^(−s²/2)/√(2π).
- S: hyperbolic secant, ½·sech(πs/2).
- L: Laplace, ½·e^(−|s|).
- T3: Student t with 3 degrees of freedom, scaled to 2/(π(1 + s²)²) (one double pole at i).
- R2: two simple poles above the line, an even mixture of Cauchys at ±1 + i: ½[C(s − 1) + C(s + 1)].

## Predictions (written before the run)

- O1. For each kernel, φ(t) computed by quadrature agrees with its closed form to 10⁻¹⁰ on t ∈ {0, 0.5, 1, 2, 4}:
  C e^(−t); G e^(−t²/2); S sech(t); L 1/(1 + t²); T3 (1 + t)e^(−t); R2 cos(t)e^(−t).
- O2. Pure phasor test: on t ∈ [0.25, 5], fit ln|φ(t)| and arg φ(t) by straight lines in t. Only C gives both
  residuals under 10⁻⁹ (a pure phasor e^(ipt)). Kill: any of G, S, L, T3, R2 passing (for R2, arg φ is 0 or π, a step,
  and ln|φ| has the log-cosine's dips, so it should fail; T3 fails by its (1 + t)).
- O3. Pole sums: for the meromorphic kernels with poles above the line, φ(t) for t > 0 equals the sum of residues of
  e^(its)·kernel there, to 10⁻¹⁰: C one term; T3 one double pole; R2 two terms; S the alternating series
  2Σ(−1)^k e^(−(2k + 1)t) summed to 200 terms at t ≥ 0.5. Kill: any mismatch.
- O4. At t = 0 the total is a single residue only for kernels with one pole above the line (C and T3). For S the
  series at t = 0 is 1 − 1 + 1 − …, which does not converge (only an Abel sum gives 1); G and L have no residue
  account at all (G entire, L not analytic on the line). Kill: S's partial sums at t = 0 converging.
- O5. Among real, positive, even rational kernels decaying at least as 1/s² with exactly one simple pole above the
  line, the only one is C up to scale (a numerator of degree 0 is forced). Checked by symbolic algebra on
  P(s)/((s − z)(s − z̄)) with deg P ≤ 1: positivity and evenness force P constant. Kill: a counterexample.

## The reading, kept apart

If nothing is killed: the unity is the Cauchy's alone. One simple pole gives one phasor; more poles give sums of
phasors (R2's beat), a higher-order pole a polynomial in t times a phasor (T3), infinitely many a series that does not
total at t = 0 term by term (S), no poles no point to read from (G, L). "One standpoint, one pole, one phasor" is then a
characterization of the Cauchy among these kernels, which is classical by uniqueness of the Fourier transform; what
would be ours is only the reading of that one point as the standpoint.

## Runs

### Run 1 (8 Nov 2026), `runs/opl/opl.py`, output `runs/opl/opl-run1.txt`; nothing killed

- O1 held: every kernel's transform by quadrature matches its closed form to 10⁻³¹.
- O2 held: only C is a pure phasor on [0.25, 5] (ln|φ| and arg φ straight to 4·10⁻³¹); the rest miss by 0.25 to 3.5
  (G's ln|φ| a parabola, S, L and T3 bent, R2's beat with arg jumping by π).
- O3 held: C, T3 and R2 equal their residues above the line to 10⁻³⁹; S equals its alternating pole series (200 terms)
  to 10⁻³¹ for t ≥ 0.5.
- O4 held: S's partial sums at t = 0 alternate 0, 2, 0, 2 (only the Abel sum is 1); C and T3 get their total, 1, from
  the one residue at i.
- O5 held: for P(s)/((s − m)² + γ²) with deg P ≤ 1, evenness forces the linear term and m to 0, so P constant: the
  Cauchy. (deg P ≥ 2 does not decay; the check is narrow, rational kernels with one simple pole above the line.)

Reading: one simple pole above the line, one phasor, the total from that pole at t = 0, is the Cauchy's alone among
these kernels. A double pole (T3) still gives the total from one point but its response to a turn is (1 + t)e^(−t), not
a phasor; two poles (R2) beat; the secant's infinitely many poles cannot total term by term at t = 0; the Gaussian and
the Laplace kernel have no point to read from. Classical (uniqueness of the Fourier transform, the residue theorem);
what is ours is reading the one pole as the standpoint.
