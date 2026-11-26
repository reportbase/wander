# The Tangent Bridge, in brief

*The thirty-fourth of a series of essays on what can be known from where one stands. Draft, 26 November 2026. A summary
of the draw project's four Tangent Bridge papers, read through on that day: *The Tangent Bridge Theorem* in its algebraic
presentation (`tb_algebra.md`, which carries forward everything of the earlier `tb_classical.md`), *The Tangent Bridge in
the Spectral Court* (§§17–22) and its preliminary §23 on the aperture. Every number below is the papers'; nothing was
rerun here, except §8, the series' own test of the bridge on the read's hemisphere (TBH). Essay 10 took up the same papers from the side of an array; this one gathers their results in one place and
says which are classical, which are the papers' own, and where the papers' wording goes further than this series' rulings.*

A dot-to-dot puzzle is a page of numbered dots. A child joins them in order and a picture appears. Where the dots are,
the picture is exactly right. Between them, the pencil makes a guess, and how good the guess is depends on how close the
dots are and how wild the picture is.

The Tangent Bridge is that puzzle made into a theorem, on a circle. Some finite set of places round the circle holds
readings. A fixed rule joins them into a continuous curve. The theorem says the curve is exact at the places, bounded
between them, and built with nothing but the places themselves. Most of that is classical interpolation. What the papers
add is where the places sit, which kernel joins them, and a second, quieter result: the whole construction can be
*proved* in angles and *run* in slopes, with no trigonometric function called anywhere in the running.

---

## 1. The theorem

Take a continuous function F on the circle and a depth d. Put N = 2^(d+1) places at the odd multiples of π/N:
±π/4 and ±3π/4 at d = 1, the eight odd multiples of π/8 at d = 2, and so on. The papers call these the **leaves**. In
the series' words, and in the algebraic paper's own §3.1, the leaves are the **addresses**, set before anything is read,
and F's value at each is the **payload** met there.

The forward map Φ reads F at the leaves. The reverse map Ψ gives them back through the kernel

  K_N(φ) = sin(Nφ/2) / (N·tan(φ/2)),  K_N(0) = 1,

which for an even count on this half-shifted grid needs the tangent in the denominator, not the sine of the familiar
Dirichlet form. The theorem then has five parts:

1. **(R1)** Φ∘Ψ is the identity on the N readings: give back, read again, get the same numbers.
2. **(R2)** Ψ∘Φ(F) equals F at every leaf.
3. **(R3)** Between the leaves the error is at most C·log N·ω_F(π/N), with ω_F the modulus of continuity and C an
   absolute constant.
4. **(R4)** As d grows the curve converges to F uniformly whenever ω_F(h)·log(1/h) → 0 (the Dini–Lipschitz class, every
   Hölder function included). The restriction cannot be dropped: some merely continuous F diverge.
5. **(R5)** Neither map uses anything about F but its values at the leaves. No integral, no norm, no total.

R1 and R2 come from two identities of the kernel: it is 1 at its own leaf and 0 at every other, and the N shifted copies
sum to 1 everywhere between (a partition of unity). R3 is the Lebesgue constant times Jackson's estimate, both classical.
R4's failure on some continuous F is Faber's theorem in its trigonometric form. R5 is the papers' point about the
operation: it is local, and it never needs the count of what lies beyond it. The papers separate N, the completed grid's
count, from K, the leaves actually drawn; the reconstruction runs at K and never has N, as in essay 4's K and N.

---

## 2. Proved in angles, run in slopes

The kernel above is written in angles. Change to the slope s = tan(φ/2) and the same kernel is

  K_N = Im[(1 + is)^N] / (N·s·(1 + s²)^⌊N/2⌋).

At N = 2 that is 1/(1 + s²), the Cauchy itself, with nothing left over. At N = 4 it is (1 − s²)/(1 + s²)², at N = 8
(1 − 7s² + 7s⁴ − s⁶)/(1 + s²)⁴: the Cauchy's curve raised to the power N/2, times a polynomial with integer
coefficients. A finer depth is a sharper Cauchy peak.

Three details in that formula carry weight, and each was found by a measurement.

- **The half-angle.** The slope is tan(φ/2), never tan φ. Put tan φ in and the kernel misses by about 0.6 at every N
  tested, because the leaves land in the wrong places.
- **The floor.** An earlier draft had (1 + s²)^(N/2), which is right only for even N. With the floor the one formula
  covers both parities: at N = 33 the error against the angle form falls from 2.7·10⁻² to 5.6·10⁻¹⁶. And the floor form
  is a pure rational function at both parities; no square root survives inside the kernel.
- **Why the angle chart hid it.** With the wrong parity the kernel stays exact at every leaf and misses only between
  them, by 1/N at the antipode; the leaf test cannot see it, and only the unit total can (1.4·10⁻³ at N = 33).

The complex form explains the whole node structure in a line. Since 1 + is = e^(it)/cos t when s = tan t, raising to the
N-th power is de Moivre: the rotation comes back to the axis it started on at exactly the leaves, so the kernel's zeros are the
N-th roots of unity, and R1 and R2 follow with no interpolation theory at all (spectral companion, §17). The cos^N t that
would overflow any register cancels between top and bottom.

Read in slopes, the kernel's parts turn out to be one map used four ways. The tangent is the map from angle to slope.
The Cauchy 1/(1 + s²) is its Jacobian, dθ/ds. Tangent addition, (s − s_k)/(1 + s·s_k), is its group law, and it is how
each leaf's offset is formed. And the depth, N = 2^(d+1), is the tangent halved d times. That is why the Cauchy, Möbius
composition and dyadic refinement keep turning up together: they are the derivative, the group and the iteration of one
function.

The papers sort the work by result. The bound R3 is a theorem about the completed circle, a maximum over the whole loop,
and it is proved where its classical sources are stated, in angles. The round trip, exactness at the leaves, the
locality and every evaluation the operation makes run in slopes: rational in s, the trigonometric-call count measured at
zero (every entry point replaced by a counter before the run), agreement with the angle form to about 10⁻¹⁴ through
N = 1024.

---

## 3. The leaves are generated, not converted

One tangent survived the slope form for a while: the leaf slopes themselves were converted from angles once, at setup.
The algebraic paper (§11.1) removes it. Seed at s = 1, the corner, where run equals rise. Halve d times with
t/(1 + √(1 + t²)). Walk the odd multiples by tangent addition. Through N = 2048 the lattice agrees with the tangent
construction to 3·10⁻¹⁵, and a reconstruction at N = 128 over 512 queries, the lattice built from scratch, makes no
trigonometric call. What is left is log₂ N square roots for the descent and the one √(1 + s²) per kernel evaluation.

Three findings come with it.

- **The reachable counts are Gauss's.** tan(π/2N) is constructible exactly when 2N is a power of two times distinct
  Fermat primes, so the halving builds N = 2^m, and with the seeds tan(π/6) and tan(π/10) also 3·2^m and 5·2^m; at
  N = 33 or 72 the tangent comes back. The radix the papers force for tiling, 2, is also the one that keeps every leaf
  constructible.
- **The written form of the half-angle matters.** The textbook (√(1 + t²) − 1)/t is the same number and subtracts
  near-equals; built that way the lattice drifts to 1.6·10⁻⁹ by N = 2048, against 10⁻¹³ for the rationalised form. Four
  orders of magnitude between two expressions equal on paper.
- **The corner is the seed, not a leaf.** A leaf sits at s = 1 only when N ≡ 2 (mod 4), which among the powers of two is
  N = 2 alone. At every finer depth the corner is a place the curve passes through and no leaf names. It costs nothing
  here: on a uniform grid no node is privileged.

One more: the horizon needs an address. At s = ∞ the composition (∞ − s_k)/(1 + ∞·s_k) is ∞/∞, a NaN, and in the
generic code it falls silently into the kernel's antipode branch and returns 0, a wrong number rather than an error.
Given its two explicit forms (1/s_k when s = ∞, −1/s when s_k = ∞) the antipode is exact to 10⁻¹⁵.

And one claim was tried and killed: the slope chart is *not* better conditioned. Its partition of unity runs five to ten
times looser than the angle form's (1.3·10⁻¹² against 1.3·10⁻¹³ at N = 16384). The case for slopes is structural, what
is visible and what is generated, not numerical.

---

## 4. The price, and where its π sits

The price of joining dots by a linear rule is the Lebesgue constant Λ_N, the worst amplification of a reading's error.
On these leaves it grows as (2/π)·ln N + O(1): 1.848, 2.728, 3.610, 4.493 at N = 8, 32, 128, 512. Two classical floors
place it. Erdős (1961): every node set on [−1, 1] has Λ > (2/π)·log n − C, and Chebyshev's nodes attain it within a
constant. The leaves, projected by the cosine, are exactly Chebyshev's nodes of the first kind (the papers' Chord
Projection Corollary), so this grid is within an additive constant of the best any node set can do. Lozinski and
Kharshiladze: every bounded linear projection onto trigonometric polynomials of degree n has norm at least the Fourier
sum's, (4/π²)·log n. So the logarithm, and R4's restriction with it, belong to finite-rank linear recovery as such, not
to this grid.

Where the π in 2/π comes from is shown in a single line (algebraic paper, §7.5). The coefficient is the mean of |sin|
over the turn. Written in the slope,

  ∫₀^π |sin t| dt = 2·∫₀^∞ s·(1 + s²)^(−3/2) ds = 2,

rational in s with the one √(1 + s²), no π in the integrand, the antiderivative or the value. The π enters only as the
divisor, the turn's own total. The series has said the same of 2/π since R438: a ratio of two sums over the turn, its π
the DHV's count of the whole.

The logarithm itself belongs to the norm, not the recovery (spectral companion, §19). In energy the reconstruction is a
tight frame with bounds ½ and 1 at every N, so L² recovery carries no logarithm at all. The ½ is exact: for N = 2 the
Gram matrix of the two kernels, with the turn's π divided out, is the rational matrix with 3/4 on the diagonal and 1/4
off it, eigenvalues 1 and ½, and the same spectrum holds at every depth tested. That ½ turns up five times in the
papers: the top mode's half weight in the kernel, the Nyquist mode split evenly when frequencies fold, the one frame
direction attenuated, the Nyquist twiddle of the fast transform, and the mode the Fejér window removes. Each time it is
the one frequency the grid sees only up to sign.

---

## 5. Where it fails, and the cure

R4 fails on some continuous F because Λ_N grows without bound. The spectral companion's §22 gives the classical way out.
Weight the same leaf transform by Fejér's triangle. The kernel becomes non-negative and still sums to 1, so the operator's
norm is exactly 1 at every N, and the curve converges uniformly for every continuous F, with no restriction. What is paid
is exactness: the curve no longer passes through its leaves, and it converges only at rate O(1/N) even on a single band
mode (cos 3θ: 0.375 off at N = 16, 0.0234 at N = 256, where the bridge is exact). One operator meets its dots and may
ring; the other never rings and only approaches its dots.

Jumps get a third answer (algebraic paper, §15.1). One bridge swallowing a step never converges in the sup norm: Gibbs
pins it (the bridge kernel's overshoot constant is 0.14114, not Fourier's 0.0895, since it is a different interpolant).
Carry the jump as its own small record, its place and its height, three numbers, and bridge the smooth remainder: the
error falls from 0.75 to 8·10⁻¹⁵ at the same budget. And one observation cannot place an edge narrower than the leaf
spacing at all: moved anywhere inside one leaf interval, it gives the same readings, and the curve is identical to the
last bit.

---

## 6. Refining, transforming, windowing

**The spaces nest; the leaves do not.** The leaves at depth d sit at odd multiples of π/2^(d+1), those at d + 1 at odd
multiples of π/2^(d+2), so the coarse leaves fall on the fine grid's *even* multiples and the two sets share no point at
any depth. What nests is the space of curves: every depth-d curve is exactly a depth-(d + 1) curve. So refining cannot
keep the old readings and append new ones between them; it reads again, or computes the new values through an exact
two-scale relation (the coarse kernel sampled at the fine leaves, to 10⁻¹⁵). With that relation the levels form the
periodic Shannon multiresolution analysis, detail spaces orthogonal across scales. One distinction remains: the bridge's
own operator is interpolation, an oblique projection, so editing at one level without disturbing the others needs the
orthogonal projection instead (measured 10⁻² against 10⁻¹⁷).

**The fast transform is the halving.** With N a power of two the readings-to-modes transform is a radix-2 Fourier
transform, and its Cooley–Tukey butterfly pairs leaf j with leaf j + N/2, exactly the two leaves the doubling map
θ ↦ 2θ sends to one coarser leaf. One butterfly stage is one level. The twiddles are the leaf slopes put through the
Cayley map, (1 − is)/(1 + is), so a full transform runs with no trigonometric call (to 1.6·10⁻¹² against numpy's at
N = 1024). Two traps are recorded: the papers' symmetric listing of the leaves and the transform's are a cyclic shift of
N/2 apart, worth a sign on every odd mode, which survives a round trip unseen and shows the moment a spectrum is read.

**A window on the leaves is cheap only in slopes** (§23, preliminary). Reading only the K leaves near a sample point is
what holding only the K in view means. Written in angles it costs two transcendental calls per sample and leaf, and the
papers measured the absurd result: a quarter of the leaves at 16.57 ms against all of them at 0.21 ms. Every kernel
argument on two power-of-two grids lands on one small constructible lattice, so the window becomes a band of rational
weights computed once; read so, the quarter costs 0.75 ms and a twentieth 0.14 ms, now cheaper than the whole. When the
output grid is no finer than the leaves the sine table collapses to {0, 1, 0, −1}, and R2 becomes a divisibility
condition on the lattice index.

**A window is a different operator, not an approximation.** Cut the kernel to K leaves and renormalise, and the
amplification grows with the logarithm of K, not N (1.00, 1.41, 2.22, 3.04, 3.89, 4.49 at K = 1, 3, 9, 33, 129, 513).
But the disagreement with the full reading floors near 0.4 (in units of a 200-unit figure) and is still 0.2 with half
the grid in hand, because the kernel's 1/s² tail carries what no window short of the whole recovers. Cutting the tails
cuts the logarithm and not the error. Read as its own object, the windowed curve is exact at its own leaves; read as an
approximation to the full curve, it never converges.

**Bridges can drive bridges** (algebraic paper, §12.5). A curve's readings can themselves be the outputs of other bridges,
a slow loop moving every leaf, local loops moving a few. The amplification then *adds* across layers instead of
multiplying, as it does on a product grid, because the spatial partition of unity cancels the driven bridge's factor:
a global driver is not amplified by the bridge it drives. Against a skeleton rig with the true joints given, the rig
wins coarse budgets on its own kind of motion, the bridge wins past about 500 numbers, and once a ripple travels over
the body the rig stops improving at all (7.3·10⁻³) while the bridge keeps going.

---

## 7. Coordinates, optimality and dimension

**Relabelling is free; moving the leaves is not** (algebraic paper, §10.2). Carry the whole scheme through any
order-preserving map, leaves and queries alike, and the curve is unchanged to 10⁻¹³–10⁻¹⁰ (the one limit is the register:
a map squeezing two leaves closer than machine epsilon). Move only the leaves and keep the native rule, and the
amplification explodes: a Möbius warp with a = 0.6 sends Λ from 2.29 to 2.5·10⁷ at N = 16. The cost tracks the largest
displacement times N, and crosses to explosive growth near 1.5.

**But a free relabelling can still change what the content needs** (§10.3). A contour r = 1 + a·sin(kθ) has one
frequency in θ; sampled evenly along its own length it acquires higher ones, and the leaves it needs rise up to eight
times the Nyquist count, falling back to exactly the Nyquist count as the lobes flatten into a circle.

**The grid is a critical point of its own price** (§15.3, working-paper grade). Nudge the leaves by a displacement field
and the first-order change in Λ vanishes exactly for turns and, asymptotically at rate 4/(πN), for the two Möbius
boosts; every other mode costs at first order. So the degenerate directions of the Lebesgue functional, a classical
object with none of the papers' premises in it, are sl(2, ℝ), the Möbius algebra, and the exact symmetries of Λ are
the turns and the reflection. Whether this grid is the global optimum over all schemes is open.

**Higher dimension.** Product tori (sound, images, surfaces, animation) take the theorem axis by axis, with no new
mathematics. A sphere does not: it is not a product of circles. The papers' conditional verdict reads the sphere as a
torus of pan and tilt with its poles collapsed, the oriented sphere rather than the projective plane. And the even pan ×
tilt grid is not the uniform measure on directions: on one octant v ≤ h holds 0.34258 of it, not ½, and the near field
0.23263, not ⅓, the numbers the series found in AZM; giving each tilt ring the weight cos a brings it back.

---

## 8. On the read's hemisphere (TBH)

The papers' sphere is read by pan and tilt about a pole on the horizon. The read in *Reads and Writes* is the hemisphere
in front of the look, so on 26 November this series laid the bridge there itself (TBH, `plans/tbh-plan.md`, predictions
committed before the script). Each line through the look is one ordinary read of period π, its slope the reading off the
look, r = tan α; these lines are combined with the azimuth round the look. The places come from halving and tangent
addition, the kernels are rational in the composed slopes, and the trigonometric-call count stays at zero.

- **The read's own content is held exactly.** The shares h², v², hv and v·v₂ come back to 10⁻¹⁴ from 8 × 4 places up,
  and a smooth function to 10⁻¹² by N = 64.
- **The horizon is glued.** Period π makes a line's two ends one point, so opposite directions on the rim are one place's
  business. The signed components v and v₂, which differ there, ring at the rim at every N; h, whose sign the front never
  changes, only kinks, its error falling as 1/N.
- **The back hemisphere holds what the front cannot.** With the turn off the look given period 2π and the content carried
  round the back by its own formula, h, v and v₂ are exact to 10⁻¹⁴. That is the DHV's two hemispheres, and the choice of
  how to carry the content round the back is the DHV's too.
- **The places are finest at the look.** Half of them lie within one thumb of the look, where the heat puts 29%, and the
  places per unit of heat at the look double with each doubling of N. Moving the bridge onto the heat's even measure costs:
  with the native kernel the Lebesgue constant reaches 6.4·10⁷ at 32 places; with the coordinate changed instead it stays
  2.73, but a cusp appears at the look and hv converges only as N^(−0.52), where the meridian bridge held it exactly.

Three predictions were killed, all by me: P1 by my code (the horizon left without its address, the very case the papers'
§11.2 names; a second run with it guarded agrees to 10⁻¹³), P4 and P7 in their letters (a bound on the core too tight, and
an "exactly ⅔" that is only a limit). The parts are classical (the tensor bridge; the full meridian's double cover, the
"double Fourier sphere" of Merilees 1973 and Orszag 1974); the sorting is the series'. So the read alone holds ratios and
shares exactly and does best where it looks, and a sign at the rim takes both hemispheres.

A second test (RAH) named the line. Of the 84 monomials h^a v^b v₂^c up to degree six, the 50 rational in the slopes (the
even-degree ones) are held by the read alone to 4·10⁻¹³ with no angle; the 34 that carry the one square root
√(1 + s₁² + s₂²) are never held exactly, those with h^a reached as N^(−a), those without h never; both hemispheres hold
all 84. Rational in the slopes, even on the sphere and held by the read alone are one class, and the square root is the
line.

---

## 9. What the constraints rebuild

The algebraic paper's Appendix A runs the arrow backward, asking which classical theorems follow from the operation's own
means: the round trip, order, the halving and squaring. The constructive half does.

- **Lebesgue's lemma** from R1 and the triangle inequality: the curve is within (1 + Λ) of any curve the grid can hold.
- **The logarithmic growth** from the self-similarity alone: each doubling adds a bounded, positive amount, so Λ grows
  as log₂ N; and the amount per doubling, measured as the mass per dyadic shell, is (2/π)·ln 2 = 0.44127, the same
  constant read two ways.
- **Aliasing** by counting: N independent readings, and the (N + 1)-th tells nothing new.
- **Jackson's estimate** by squaring twice: Fejér's kernel is a squared sum, positive; squared again it is local enough
  for the sharp bound, closed with one order inequality and the geometric series 8/7.
- **Bernstein's inequality**, sharp constant ½ on the leaves, which is the classical 1 once the leaf count is converted
  to degree.

The variational half does not: the existence of a best approximation, Weierstrass density as a completed limit
(replaced by a residual ladder that settles, testably), equioscillation, and the universal lower bound over all node
sets, which stays open. The paper pins its difficulty down to one step, an average floor whose logarithm lives in the
kernels' far tails, where every proof found uses the conjugate function.

That step has since been closed, though not by those means. Tao (2026, arXiv:2603.21453) proves the floor on an
interval for any places with the sharp constant, (4|I|/π²)·log n, by an L¹ duality on the square wave's Fourier series
and the residue theorem round closed contours, the completed turn's tools. This series checked his trigonometric toy
(FAB): its sharp 8 is 4 × 2, two factors computed with no angle, π only in the mean; and on the circle evenly spaced places
gave the least average in every minimization tried, climbing at (4/π²)·ln N.

And behind the calendar's dial, which browses a list without end (DBR), a bridge laid in ratios round the needle holds
ratio content to the same error from 10 to 10¹² thumbs out, each read K terms with no N and no angle, its Lebesgue
constant Chebyshev's: the moving window is a whole bridge, not a cut of a larger one. Content with a size in records
needs a window in records; one bridge over the whole list holds neither well. The page `dial-bridge.html` shows it: push the needle out
to a trillion thumbs and watch the error, the terms a read and the trigonometric calls (none) stay put.

Then on measured content (MSR). Word frequency by rank in a hundred million words is held in ratios by 6 leaves from rank
about 300 to 30,000, whatever the corpus's size, but not in its head, where the commonest words need 32 and 16: Zipf's
list is ratio content in its tail only. A tide, whose period of 12.42 hours is a size, is held by a window of fixed width
in hours with the same 48 leaves anywhere along a year, and by a window in ratios nowhere past a day.

And on a program (PEB). A pool engine run with every aim a half-slope plays as it did and calls no trigonometric function.
What one shot does across all aims is a function broken at the aims where its contacts change, so the bridge is laid piece
by piece, the breaks kept as records, as §5's cure says. It held only once the engine's clock was exact: a fixed tick puts
jumps inside the pieces wherever an event slides from one step to the next, and an integrator that places each event at
its own moment takes them away. The edges left are the table's, smooth where a cushion or an order changes and a square
root at a graze, held in the root's chart. About a third of the pieces still need more than 128 leaves, not yet explained.

---

## 10. What it comes to

**What is classical.** Trigonometric interpolation at equispaced nodes, the Lebesgue constant, Jackson, Erdős's and
Lozinski's floors, Faber's divergence, Fejér's cure, Chebyshev nodes, de Moivre, aliasing, Parseval, the Shannon
multiresolution analysis, Cooley and Tukey, Gauss's constructible polygons. The papers say so throughout and claim none
of it.

**What is the papers' own.** The choice of grid (odd multiples of π/N, N a power of two) and the half-shifted even
kernel that goes with it; the slope form, rational at both parities, and its four readings as one map; the lattice
generated from the corner by halving and tangent addition with no trigonometric call; the horizon's explicit address;
the location of 2/π's π; the energy face's exact ½; the windowed band; composition's additive amplification; the
critical-point result; and the many killed claims, kept so they are not tried again.

**Where the series reads them differently.** The papers were written in an older vocabulary and still speak of a reader
who "declines" π and a writer who holds the completed circle, and they call the grid, the halving and the Cauchy
"forced". This series says less. There are reads and writes, no reader or writer (R887); the completed circle is the
DHV's, a synthesis and not a vantage (R1239); π is its total, met by no read (R909); and the Cauchy is the uniform turn's
density read in the slope, the papers' own 29 October revision having already dropped "the unique Möbius-invariant
distribution" for rotation-invariant. None of that touches the mathematics, which is exact where it is said to be and
checked.

**For the series.** The Tangent Bridge is the cleanest place where the two forms of one result can be laid side by side
and both checked. The DHV's form is the angle chart: the completed turn, its Fourier modes, its maximum over the whole
loop, its π. The read's form is the slope chart: ratios, tangent addition, the halving, the one square root, and no π in
anything it computes. They agree to the last digit wherever both apply, and the theorem's own sorting, bound in one
chart and operation in the other, is the series' sorting of what each form needs (R1062). *The heat is given; the paint
is met*: the leaves are laid before anything arrives, and the kernel that joins them is the Cauchy's own curve, raised
to the depth.

**What today's tests add up to.** Taken together, the series' own tests of the bridge (§8 and §9) give ten results.
Approximation theory splits along the line between the two forms, and its open floor has been proved by the completed
circle's tools. The sharp constants are computed with no angle, π entering only in the mean. The logarithm belongs to the
worst point, not the recovery. One hemisphere holds exactly what is rational in its slopes, and glues its horizon; the
square root is the line. The bridge is finest where the read looks. A window rebuilt as its own bridge never asks for N.
Content with a size is the write's, held only in its units. And on measured lists the sorting held, and once said no,
to the head of Zipf's law. Every kill on the way was the tester's.

Back to the dot-to-dot. The dots were placed before the picture was drawn, and the rule that joins them never looks
past them. Where they stand, the picture is exact; between them it is a guess with a price, and the price is a
logarithm that every scheme of its kind must pay. And the whole puzzle, dots, rule and refinement, can be worked with a
ruler and ratios alone.

---

## Sources

The four Tangent Bridge papers in the draw project (`reportbase/draw`, `papers/`): *The Tangent Bridge Theorem*,
algebraic presentation (`tb_algebra.md`, §§1–16 and Appendices A–B; the classical presentation `tb_classical.md` is its
earlier draft), *The Tangent Bridge in the Spectral Court* (`tb_spectral.md`, §§17–22) and *§23 — The aperture band is
constructible* (`tb_spectral_notes.md`, preliminary). The classical results they restate are Lebesgue's lemma, Jackson's
estimate, Erdős and Turán's bound, Erdős (1961), Lozinski and Kharshiladze, Faber's theorem, Fejér's summation,
Bernstein's inequality, Chebyshev interpolation, the periodic Shannon multiresolution analysis, the Cooley–Tukey
factorization and Gauss's constructibility theorem, as presented there.

The series' rulings cited: R438 (2/π as a ratio of sums over the turn), R887 (reads and writes, no reader or writer),
R909 (π the DHV's), R1062 (the sorting of mathematics by what each form needs), R1239 (the DHV a synthesis). Essay 10,
*Arrays and the circle*, takes up the same papers from the array; essay 4 has K and N; AZM (`plans/azm-plan.md`) the
pan × tilt numbers.

TBH: `plans/tbh-plan.md`, `runs/tbh/` (runs 1–2). *Reads and Writes* §9, "The bridge sorts its own field, and the
read's hemisphere" (R1247).

*Demos: `dial-bridge.html` (a bridge behind the dial); `array-sweeps.html` (K places on the quarter turn, the index alone and the values on it).*
