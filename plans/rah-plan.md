# RAH: what the read alone holds

*26 November 2026. Tom: "Merge, then 1 the 3", item 3 of Claude's list after DBR: TBH found the read alone (a bridge on
the hemisphere in front, each line through the look one read of period π) holding the shares and ratios exactly and
ringing on anything signed at the rim. Is "held by the read alone" exactly a class one can name? Predictions written
and committed before the script (`runs/rah/rah.py`, built on `runs/tbh/tbh.py`) exists.*

## The claim to test

A direction in front is d = (h, v, v₂), h > 0; its slopes are s₁ = v/h, s₂ = v₂/h, and h = 1/√(1 + s₁² + s₂²). The
read-alone bridge (TBH's meridian bridge, α of period π) closes each line through the look at one horizon point, so it
holds a function on the front as the function on the sphere that is *even*, f(−d) = f(d). The DHV's form (α of period
2π) holds both hemispheres and the content carried round the back by its own formula.

Candidate statement: **the read alone holds exactly the content that is rational in the slopes.** A monomial
h^a v^b v₂^c of total degree n = a + b + c is s₁^b s₂^c · h^n, rational in (s₁, s₂) when n is even and carrying the one
square root √(1 + s₁² + s₂²) when n is odd; even n is exactly even on the sphere. So: even degree held exactly by the read
alone; odd degree not, and of those, the ones with a ≥ 1 vanish at the rim (h = 0 there) and only kink, while those with
a = 0 jump at the rim and ring.

## Predictions

All 84 monomials h^a v^b v₂^c with a + b + c ≤ 6, on the front hemisphere (TBH's queries: 20,000 uniform directions and
the β = 0 line to the horizon), Nβ = Nα = N.

- **R1 (even degree held exactly by the read alone).** The 50 monomials of even degree are reproduced to ≤ 10⁻¹¹ (sup)
  at N = 16, 32, 64 with α of period π.
- **R2 (odd degree with h in it: held only in the limit).** The 22 of odd degree with a ≥ 1 have sup error ≥ 10⁻⁶ at
  N = 64 (never exact) and fall by ×1.6 or more per doubling from 16 to 64.
- **R3 (odd degree without h: never held).** The 12 of odd degree with a = 0 have sup error ≥ 0.05 at N = 16, 32 and 64.
- **R4 (the DHV's form holds them all).** With α of period 2π, all 84 are reproduced to ≤ 10⁻¹¹ at N = 16.
- **R5 (the line between them is the square root).** Written in the slopes (sympy, h = 1/√(1 + s₁² + s₂²)), the 50
  even-degree monomials simplify to rational functions of s₁, s₂ and the 34 odd-degree ones keep the square root: the
  split R1–R3 is exactly the split rational / not rational.
- **R6 (no trigonometric call).** The read-alone bridge's path (leaves, kernels, content from the slopes) makes zero
  trigonometric calls for every even-degree monomial.

Each is killed by its own number. Known beforehand: TBH runs 1–2 (hv, h², v², v·v₂ exact; h kinks; v, v₂ ring; the
back hemisphere holds h, v, v₂); the even functions on the sphere are the functions on the projective plane (classical).
R5 is algebra, a check of the statement, not a discovery; R1–R4 test that the bridge holds exactly the class it says.

## What would follow, if nothing is killed (a reading, to rule on)

The read alone holds exactly what is rational in its slopes: ratios and shares, quantities a direction has whatever its
sign. What needs the one square root √(1 + s²) is what the read alone cannot hold at the rim; holding it takes the back
hemisphere, the DHV's. *Reads and Writes* §9 already places that square root as where the DHV comes in (the halving's
one root, two lengths combined); here the same root marks what the read alone holds.

## Runs

### Run 1 (26 November 2026; `runs/rah/rah.py`, output `runs/rah/rah-run1.txt`)

- **R1 not killed.** The 50 even-degree monomials: largest sup error 4.2·10⁻¹³ over N = 16, 32, 64.
- **R2 killed, by my bound.** The 22 odd-degree monomials with h in them are never exact and fall by at least ×2.00 a
  doubling, but the smallest error at N = 64 is 2.9·10⁻⁸ (h⁵), not ≥ 10⁻⁶. Post hoc (`runs/rah/` table in the output and
  a follow-up listing): h⁵ falls 3.35·10⁻⁵, 9.4·10⁻⁷, 2.9·10⁻⁸ (about ×2⁵ a doubling), h⁴v and h⁴v₂ about ×2⁴, h³ and
  h³v₂², h³vv₂ about ×2³, h and the a = 1 family ×2: an odd monomial carrying h^a converges as N^(−a), the order to which it
  vanishes at the rim, since its even extension carries |h|^a, a corner of that order there. Not predicted.
- **R3 not killed.** The 12 odd-degree monomials without h: least sup error 0.174 over N = 16, 32, 64 (v, v₂ and their
  odd powers 0.97–1.00; v·v₂² 0.38; v·v₂⁴ 0.28), none falling.
- **R4 not killed.** The DHV's form (α of period 2π) holds all 84 to 6.4·10⁻¹⁵ at N = 16.
- **R5 not killed.** In the slopes 50 of the 84 are rational, and they are exactly the even-degree ones.
- **R6 not killed.** Zero trigonometric calls on the read-alone path for every even-degree monomial.

### Standing after run 1

Not killed: R1, R3, R4, R5, R6. Killed: R2 in its bound (none exact, as predicted; the fast ones faster than I allowed).

What the run shows, in the plan's reading (to rule on):
- **The read alone holds exactly what is rational in its slopes.** Of the 84 monomials up to degree six, the 50 that are
  rational in (s₁, s₂) are held to 4·10⁻¹³ by the read alone, with no trigonometric call; the 34 that carry the square
  root √(1 + s₁² + s₂²) are not held exactly at any N. Rational in the slopes, even on the sphere and held by the read
  alone are one class.
- **What carries the root splits by how it meets the rim.** With h to the power a in it, it vanishes at the rim to order a
  and the read alone reaches it as N^(−a), never exactly; without h it jumps at the rim and is never reached at all.
- **Both hemispheres hold everything.** The DHV's form holds all 84 exactly at N = 16.
- So the square root that *Reads and Writes* §9 places as where the DHV comes in (the halving's one root, two lengths
  combined) is also the line between what the read alone holds and what needs the back hemisphere.
