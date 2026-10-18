# ADR: the address as a primitive

*18 October 2026 (Tom's local date). After R359 ("once a cauchy, always a cauchy"), Tom: "Lets explore what this means.
cauchy addresses are robust, can be combined, they are a kind of primititive in their own right." Claude proposed that the
primitive is a standpoint z = m + iγ in the upper half-plane, with an algebra, a distance, a level of detail and a way of
being read. Tom: "yes". Exact mathematics (mpmath) and seeded samples; no physics. Thresholds are in standard errors from
the start (SUM run 1's lesson).*

## Known beforehand (classical)

- Möbius maps carry the Cauchy family onto itself, with the parameter z = m + iγ moved by the same map (Knight 1976;
  McCullagh 1996). McCullagh's maximum-likelihood estimate is equivariant under them.
- Independent Cauchys combine linearly in their parameters: Σ wᵢXᵢ ~ C(Σ wᵢmᵢ, Σ |wᵢ|γᵢ). The characteristic function
  is e^{imt − γ|t|}.
- The Fisher information of the location–scale Cauchy is (1/(2γ²))·I, the hyperbolic metric of the upper half-plane up to
  a factor. The Fisher–Rao distance is d_H/√2, where cosh d_H = 1 + |z₁ − z₂|²/(2γ₁γ₂).
- The Cauchy kernel is the Poisson kernel of the half-plane. Smoothing a pattern by it from height γ multiplies its mode
  of frequency k by e^{−kγ}, and heights add (a semigroup).
- The sample median is not carried by a map whose pole lies inside the sample (LOM run 1, L1).
- JAY P7: the drawings V = cH lie on a hyperbolic line whose distance is the levels.

## The claim

The address is a primitive: one value z, operations closed on it, an invariant distance, a robust read.
- Its level of detail is its height γ.
- Errors along a relay grow linearly in γ, where amounts' errors grow as √n.

What is ours is the reading, not the mathematics.

### Predictions

- **A1 (combination is linear in z).**
  - Take z = (1 + 0.5i, −2 + i, 0.3 + 2i) and w = (0.5, −2, 1.5). Then Σ wᵢXᵢ is C(Σwᵢmᵢ, Σ|wᵢ|γᵢ), that is
    C(4.95, 5.25).
  - Exactly: characteristic functions at 100 digits for t ∈ {0.1, 1, 3}.
  - By sample (10⁶ draws, seeded): the median within 3 standard errors of 4.95 and the half-interquartile range within
    3 standard errors of 5.25.
  - *Killed* if either fails.
- **A2 (Möbius maps move z).**
  - (a) For X ~ C(0.5 + 0.8i) and g(x) = (2x + 1)/(x + 3), Y = g(X) has the law C(g(z)). The two distribution functions
    agree to 10⁻⁴⁰ at 20 points.
  - (b) The quartile read of z (median, half the interquartile range) follows every affine map: on one sample of 10⁵,
    read before and after x → 3x − 2, it agrees to rounding.
  - (c) It does not follow g when g's pole, −3 here, lies among the readings: reading z from g(X) and reading g(ẑ) from
    X differ by more than 10 standard errors. The maximum-likelihood read agrees under g to 10⁻⁶.
  - *Killed* if (a) or (b) fails, if (c)'s quartile read agrees, or if its maximum-likelihood read does not.
- **A3 (the distance is hyperbolic, and the levels are on it).**
  - The Fisher information of C(m, γ), by quadrature at 50 digits, is (1/(2γ²))·I at three points.
  - The hyperbolic distance of z₁ = i and z₂ = 2i is ln 2: one level per doubling of height.
  - Möbius maps leave d_H unchanged, to 10⁻⁴⁰, at three pairs and three maps.
  - *Killed* if any fails.
- **A4 (height is level of detail).**
  - The pattern f(x) = Σⱼ cos(2ʲx), j = 0 … 6, seven levels of frequency.
  - Seen from height γ (convolved with the Cauchy kernel of scale γ, by quadrature at 50 digits), each mode is multiplied
    by e^{−2ʲγ}, to 10⁻²⁰.
  - Counting the modes kept above 1/e: at γ = 2⁻ᵏ the count is k for k = 0 … 7. Each halving of height brings in one
    more level, and each doubling loses one. (Written first as k + 1 for k = 0 … 6; corrected before this plan was
    committed or anything run: 2ʲγ < 1 at γ = 2⁻ᵏ keeps j < k, which is k modes.)
  - *Killed* if any fails.
- **A5 (errors along a chain).** Seeded, 10⁵ draws.
  - A relay of n standpoints of height 1 has half-interquartile range n, within 3 standard errors, for n = 1, 4, 16.
  - The mean of n readings of one address has half-interquartile range 1, within 3 standard errors, for the same n.
  - For contrast, Gaussian amounts: the sum's sd is √n and the mean's sd 1/√n, within 3 standard errors.
  - *Killed* if any fails.
- **A6 (the verdict).** A judgment. The address meets the four marks of a primitive:
  - a value, z;
  - operations closed on it (A1, A2a);
  - an invariant distance (A3);
  - a robust read, the quartiles under affine maps and the likelihood under all Möbius maps (A2b, A2c).

  It also has a built-in level of detail (A4) and linear error growth (A5). *Killed* if any of A1–A5 is killed in a way
  that is not my set-up.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (18 Oct, `python3 adr/adr.py`; output `adr/adr-run1.txt`, 22 s)

- **A1 not killed.**
  - Exactly: the characteristic functions differ by at most 3.6·10⁻¹⁰².
  - By sample: the read is 4.9693 + 5.2425i against 4.95 + 5.25i. 3 standard errors are 0.0247.
- **A2 killed, in clause (c), by my set-up.**
  - (a) The law of g(X) is C(g(z)) to 1.3·10⁻⁵¹.
  - (b) The quartile read follows x → 3x − 2 to 1.1·10⁻¹⁶.
  - (c) Under g, with its pole among the readings (7% of X lies past −3):
    - the quartile read of g(X) is 0.6416 + 0.3122i;
    - g of the quartile read of X is 0.6419 + 0.3126i;
    - the two are 0.3 standard errors apart, not the more than 10 predicted.
  - The likelihood read agrees under g to 8.6·10⁻¹⁴.
- **A3 not killed.**
  - The Fisher information is I/(2γ²) to 1.3·10⁻⁵¹ at three points.
  - d_H(i, 2i) = ln 2 exactly.
  - The Möbius maps leave d_H unchanged (difference 0 at 50 digits).
- **A4 not killed.**
  - Each mode of the pattern is multiplied by e^{−kγ}, to 10⁻³¹.
  - The modes kept above 1/e at γ = 2⁻ᵏ number 0, 1, 2, …, 7 for k = 0 … 7.
- **A5 not killed.**

  | n | relay's half-IQR | mean's half-IQR | Gaussian sum, sd | Gaussian mean, sd |
  |---|---|---|---|---|
  | 1 | 0.996 | 1.003 | 0.997 | 0.9965 |
  | 4 | 4.021 | 0.998 | 2.002 | 0.5004 |
  | 16 | 15.941 | 1.004 | 4.002 | 0.2501 |

**A2(c) was my reasoning, not the primitive.** I took LOM's lesson, that a sample median is not carried over by a map whose
pole lies among the readings, and applied it to the read of z. But g(X) is exactly C(g(z)) (A2a). So the quartile read of
g(X) and g applied to the quartile read of X are both consistent for g(z), and differ only by sampling noise. They are
not exactly equal sample by sample, which the likelihood read is (8.6·10⁻¹⁴); but there is no systematic failure.

The contrast with LOM is the finding. There the readings were close to normal (amounts), and the reciprocal across zero
moved their median by 73%. Here the readings are Cauchy (addresses), the same kind of map leaves the read intact, and the
reason is the family's closure. Once a Cauchy, always a Cauchy is what protects the quartile read across a pole.

**A6, the verdict: not killed.** Every kill is my set-up. The address meets the four marks of a primitive:
- **a value:** z;
- **closed operations:** positive and mixed combinations linear in z, and Möbius maps moving z;
- **an invariant distance:** the hyperbolic one, whose unit along the height is the level, ln 2 a doubling;
- **a robust read:** the quartiles, consistent under every Möbius map, and the likelihood, exactly equivariant.

It also has two further properties:
- **A built-in level of detail.** The height γ keeps exactly the modes with kγ < 1, one level per halving.
- **Linear error growth.** Along a relay the error grows as n; averaging leaves it at 1. Amounts give √n and 1/√n.

The mathematics is classical (Knight, McCullagh, the Poisson kernel). The reading is ours.
