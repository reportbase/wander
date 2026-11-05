# The routes into the Cauchy

5 Nov 2026 (Tom: "lets work on the math. I know cauchy shows up for a variety of reasons, not just ours.", then "ok").
This is a working note: classical results gathered side by side, and what they say about the reading. Nothing here is new
mathematics. Each route is checked against the Poisson kernel at 30 digits in `runs/crt/crt.py` (output `runs/crt/run2.txt`;
run 1's two misses were my quadrature, recorded in `run1.txt`). No paper changes until Tom rules.

## 1. One law

Every Cauchy is the Poisson kernel of the upper half-plane, seen from a point z = m + iγ:

  p(x) = (1/π)·γ/((x − m)² + γ²) = (1/π)·Im 1/(x − z),   F(x) = ½ + (1/π)·arctan((x − m)/γ).

That is, it is the harmonic measure of the real line seen from z. The family is C(z), indexed by a point of the upper
half-plane (McCullagh 1992 writes it this way). The question is never "is this a Cauchy?" but "what put a point at z, and
how did the line get reached from it?"

## 2. The routes

| # | Route | Mechanism | What z is | Check (`crt.py`) |
|---|---|---|---|---|
| 1 | **The turn** (the lighthouse) | a uniform direction from z, straight to the line: x = m + γ·tan θ | a standpoint; γ its distance to the line | 1 |
| 2 | **Isotropic ratio** | any rotation-invariant pair (X, Y): Y/X ~ C(i). Two normals is one case; uniform on a disc is another. | none of its own: the pair's direction is uniform, so this *is* route 1 | 2 |
| 3 | **Diffusion** (Kakutani 1944; Spitzer 1958) | Brownian motion from z, where it first leaves the half-plane | a starting point; γ its height | 3 |
| 3′ | **Hitting-time mixture** | N(m, T) mixed over T, the first time a Brownian motion falls by γ (Lévy's law). This is the Student t with one degree of freedom. | the same height, hidden in the mixing | 3 |
| 4 | **Pole / resonance** | (γ/π)·\|1/(x − z)\|² = p(x): a simple pole's response, its Fourier pair e^(imt − γ\|t\|), a damped oscillation | a pole; γ a decay rate, not a length | 4a, 4b |
| 5 | **Stable sums** | C(z₁) * C(z₂) = C(z₁ + z₂); the mean of n Cauchys is Cauchy; the attractor for symmetric tails ~\|x\|⁻² | a sum of points | 5 |
| 6 | **Möbius closure** | (aX + b)/(cX + d), ad − bc > 0, carries C(z) to C(g(z)); the reciprocal among them | carried along | 6 |
| 7 | **Stereographic / inscribed** | uniform on a circle, seen from a point of it: x = tan(φ/2) | the circle's point i | 7 |

Routes 1, 2 and 7 are one geometric fact: a uniform turn read on a line. Route 3 is a different mechanism (a random path,
not a straight one) that lands in the same place. Route 4 has no path at all: it is analytic. Route 5 is closure. Route 6 is
symmetry.

## 3. Why they agree, and where they part

**In the plane they are one measure.** A uniform turn from z, Brownian exit from z, the hyperbolic plane's visual measure
from z, and the Möbius image of the uniform law are the same measure on the line. The reason is that harmonic measure is
conformally invariant, and a turn about z is a conformal map fixing z. This is essay 13's "one law in four parts".

**On a flat boundary they agree in every dimension.** From height γ above a hyperplane in ℝⁿ, the uniform landing over
the hemisphere equals the half-space's Poisson kernel, Γ(n/2)/π^(n/2)·γ/(r² + γ²)^(n/2) (check 8, n = 3, 4, 5).

**On a curved boundary they part.** From radius ½ inside the unit ball in ℝ³, the share landing within 45° of the point's
own direction is:
- harmonic measure 0.48210;
- the uniform straight turn 0.35946.

They are apart by 0.123 (check 9). Straight lines and random paths agree only where the boundary is flat. This is EUL's
"the plane's one law parts on S²", seen from the boundary's side.

## 4. What tells the routes apart

The law alone never can: one sample's distribution is the same whichever route made it. Routes are told apart only by
extra structure.

- **What γ tracks.**
  - In the turn and in diffusion, γ is a distance, and it moves with the geometry (raise the standpoint, γ grows in
    proportion).
  - In a resonance, γ is a rate (a lifetime's inverse), unmoved by any distance.
  - In a stable sum, γ adds over the summands.
- **The boundary's shape.** Bend the boundary and the turn and diffusion part (check 9); a pole and a sum have no boundary
  to bend.
- **Correlation.** Readings from one standpoint share z. Readings from a mixture of standpoints (or a mixture of scales)
  do not, and their pooled law is no longer a Cauchy unless the mixing is exactly a hitting time (3′).

## 5. The seeds, in these terms (TCF run 1)

Clark's 2Dt, p/(πu)·(1 + r²/u)^(−(p+1)), is a two-dimensional Gaussian mixed over its variance with an inverse-gamma law of
shape p (check 10, at p = 0.1, ½ and 2). At p = ½, and only there, the mixing is the Lévy hitting time, and the 2Dt is the
3D hemisphere law: straight flight from a height and diffusion from a height alike (check 10b). The fitted p ≈ 0.1 says the
mixing over the seeds is heavier-tailed than any hitting time. So the kernel is not harmonic measure by any route: not a
turn, not a diffusion. That is a cleaner statement of TCF's kill than "no turn": the seed kernels are a mixture of amounts,
heavier than harmonic, and no standpoint z describes them.

## 6. What it means for the reading

- **The turn does not own the Cauchy.** It is one mechanism that realizes harmonic measure from a point, beside diffusion,
  a pole, a sum and symmetry.
- **What *Reads and Writes* can claim**, consistent with R719: where a standpoint is real, its Cauchy is the harmonic
  measure of the line seen from it, and the turn is one way, the reader's, to see that. The heat over a reader's directions
  is the turn's. Other Cauchys are other routes to the same measure, and a fat tail with no z is not a Cauchy at all.
- **"Find the turn"** becomes **"find the z"**: what puts a point off the line (a standpoint, a starting point, a pole, a
  sum), and how the line is reached from it (straight, random, analytically). The address/payload split survives in each:
  the landing is where, the amount carried there is what.

## Open

- Whether to bring §1–§4 into *Reads and Writes* (a short passage, "The Cauchy's routes", after §2's derivation), into
  essay 17 (whose walker already is route 3) or into essay 13 (which has the plane's agreement and the sphere's parting).
  That is Tom's call.
- Lévy foraging (REA H53) in these terms: a straight leg cut off by an edge is route 1 with γ the distance to the edge. Its
  test would be whether γ tracks that distance, which is §4's first discriminator.

## References

- Kakutani, S. (1944). Two-dimensional Brownian motion and harmonic functions. *Proc. Imp. Acad. Tokyo* 20, 706–714.
- Spitzer, F. (1958). Some theorems concerning 2-dimensional Brownian motion. *Trans. AMS* 87, 187–197.
- McCullagh, P. (1992). Conditional inference and Cauchy models. *Biometrika* 79, 247–259.
- Clark, J. S. et al. (1999). Seed dispersal near and far. *Ecology* 80, 1475–1494.
