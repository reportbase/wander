# DPR: depth precision when drawing a first-person view

*20 October 2026 (Tom's local date), SPN R401.*

*Tom (06:42 MDT): "what about synthetic situations, where the blueprint is known, but you want to provide a first person
view." Claude's answer: drawing a known blueprint as a first-person view is turning a writing into a reading, which is
rendering. A synthetic view has no noise, so the question becomes representation: precision, level of detail and cost.
Much of the papers' geometry is already standard rendering practice under other names: home is camera-relative rendering,
the in-place lay is the hardware depth buffer, the reader's lay is the logarithmic depth buffer, and level of detail is
set by size on screen. Claude offered a test of depth precision against the standard schemes. Tom (06:49): "yes".*

*Exact. A script in `runs/dpr/`. Predictions written before the script.*

## Correction before writing

The answer to Tom predicted that the reader's lay at H = √(near·far) holds a constant relative precision at every level.
Worked out before writing the predictions, that is wrong inside the corner. There the reader's lay is proportional, so its
precision is absolute (εH), and relative precision gets worse toward the near plane. This is what `zoom.html` already
shows: "detail absolute inside the corner, relative past it". The predictions below are the corrected ones.

## Known beforehand

- **The standard depth buffer.** It stores w = (f/(f − n))·(1 − n/d), linear in 1/d, in fixed point, usually 24 bits.
  Its relative precision falls as d/n, so a scene with a near plane at 1 m and objects at thousands of kilometres
  z-fights (overlapping surfaces flicker because their depths round to the same value). This is classical (Reed 2015,
  "Depth precision visualized"; Akeley and Su 2006).
- **Reversed-Z.** Store w = n/d in a 32-bit float, with the far plane at infinity. The float's exponent spaces values
  logarithmically near 0, so relative precision is nearly constant (Lapidous and Jiao 1999; Reed 2015).
- **The logarithmic depth buffer.** Store w = ln(d/n)/ln(f/n). It gives constant relative precision ln(f/n)·2^(−b)
  (Kemen 2009, the Outerra blog).
- **Floating point.** IEEE 754 binary32 has a fixed count of values in each power-of-two interval (2²³) and, below the
  smallest normal 2^(−126), subnormals spaced evenly at 2^(−149). This is classical.
- **This corpus.**
  - The reader's lay is s up to the corner, then 1 + ln s past it, where s = d/H.
  - The in-place lay is 2 − 1/s past the corner.
  - `zoom.html`: detail is absolute inside the corner and relative past it.
  - ISQ: the in-place lay's room per unit s is 1/s², the reciprocal's Jacobian.
  - HKO: the best H for two amounts is √(x₁x₂), for telling them apart by angle.

## The set-up

- **The scene.** Near plane n = 1 m, far plane f = 10⁷ m (10,000 km). Distances are tested at d = 10^k m, k = 0 … 7.
- **Each scheme.** A depth scheme maps d to a stored w in [0, 1] (or, for reversed-Z, to a float). It is stored either
  as 24-bit fixed point (2²⁴ equal steps) or as an IEEE binary32 float.
- **Resolvable separation.** Δd(d) is the distance to the nearest farther depth that stores a different value: the
  smallest separation the buffer can tell apart. It is computed exactly, the stored value's next step inverted with
  rational or 50-digit arithmetic, not estimated. The measure reported is the relative separation r(d) = Δd/d.

## The schemes

1. **Z24, the standard buffer.** w = (f/(f − n))·(1 − n/d), in 24-bit fixed point.
2. **RZ32, reversed-Z.** w = n/d, as a 32-bit float.
3. **LOG24, log depth.** w = ln(d/n)/ln(f/n), in 24-bit fixed point.
4. **RL24(H), the reader's lay.** w = (L(d/H) − L(n/H))/(L(f/H) − L(n/H)), with L(s) = s for s ≤ 1 and 1 + ln s past
   it, in 24-bit fixed point. Tried at H = √(nf) ≈ 3,162 m and at H = n.
5. **IP24(H), the in-place lay.** L(s) = s for s ≤ 1 and 2 − 1/s past it, at H = n, in 24-bit fixed point.

## Predictions

**D1 (the standard buffer, the in-place lay).**
- Z24's r(d) is (d/n)·(1 − n/f)·2^(−24), to within 1% at every tested d: about 6·10⁻⁸ at 1 m, and 0.6 at 10⁷ m.
- IP24(H = n) gives the same r(d) to within 1%, since past the corner the in-place lay is the reciprocal: the standard
  buffer is the in-place lay with its corner at the near plane.
- *Killed* if either is off by more than 1% at any tested d.

**D2 (reversed-Z is constant).** RZ32's r(d) lies between 2^(−24) and 2^(−23) at every tested d. *Killed* if not.

**D3 (log depth is constant).** LOG24's r(d) is ln(f/n)·2^(−24) ≈ 9.61·10⁻⁷, to within 1% at every tested d.
*Killed* if not.

**D4 (the reader's lay at the pair's corner, H = √(nf)).** Let L_span = L(f/H) − L(n/H) ≈ 9.06.
- Inside the corner (d ≤ H) its precision is absolute: Δd = H·L_span·2^(−24) ≈ 1.71·10⁻³ m, to within 1%. So r(d) is
  1.7·10⁻³ at 1 m, 1,800 times log depth's.
- Past the corner it is relative: r(d) = L_span·2^(−24) ≈ 5.40·10⁻⁷, to within 1%. That is better than log depth by
  ln(f/n)/L_span ≈ 1.78.
- *Killed* if any of these is off by more than 1%.

**D5 (the reader's lay at H = n is log depth).** RL24(H = n) gives LOG24's r(d) to within 1% at every tested d: with
the corner at the near plane, everything in view is past it. So for constant relative precision the best H is the near
plane, not √(nf). *Killed* if not.

**D6 (a float is a reader's lay).**
- Over every finite positive binary32 value x, the spacing to the next value is 2^(−149) exactly for x < 2^(−126):
  absolute, the proportional part inside a corner at 2^(−126).
- For x ≥ 2^(−126), the spacing over x lies in (2^(−24), 2^(−23)]: relative, 2²³ addresses in every level.
- So binary32 is the reader's lay in base 2, with its corner at the smallest normal and n = 2²³. Classical; the reading
  is ours.
- *Killed* if any value breaks either clause. All 2³¹ − 2²³ finite positive values are checked, by exponent and by the
  first and last mantissa of each.

**D7 (the verdict).** A judgment. *Killed* if any of D1–D6 is killed.
- On depth precision the geometry adds no new scheme. It names the existing ones:
  - the standard buffer is the in-place lay with H at the near plane (D1);
  - log depth is the reader's lay with H at the near plane (D5);
  - a float is itself a reader's lay (D6), so reversed-Z is the in-place lay read through a reader's lay, which is why
    its relative precision is constant.
- The pair's corner, H = √(nf), trades precision near for precision far (D4). It is the right H only where absolute
  precision is wanted near, not for rendering, where what matters is relative.

## What would and would not be shown

**Shown:** exactly how each depth scheme spends its stored values over distance, and which of the papers' lays each is.

**Not shown:**
- rendering itself, rasterizing or interpolating depth across a triangle. Log depth is not linear in screen space, which
  costs it in practice (writing depth from the fragment shader disables early depth tests);
- level of detail, or camera-relative positions;
- any gain on a real GPU.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (20 Oct; `runs/dpr/dpr.py`, output `runs/dpr/dpr-run1.txt`)

The relative separation r(d) = Δd/d, one stored step farther, computed exactly (50 digits; the floats' neighbours from
binary32 itself):

| d (m) | Z24 | IP24(n) | RZ32 | LOG24 | RL24(√(nf)) | RL24(n) |
|---|---|---|---|---|---|---|
| 1 | 5.96·10⁻⁸ | 5.96·10⁻⁸ | 5.96·10⁻⁸ | 9.61·10⁻⁷ | 1.71·10⁻³ | 9.61·10⁻⁷ |
| 10 | 5.96·10⁻⁷ | 5.96·10⁻⁷ | 7.45·10⁻⁸ | 9.61·10⁻⁷ | 1.71·10⁻⁴ | 9.61·10⁻⁷ |
| 10² | 5.96·10⁻⁶ | 5.96·10⁻⁶ | 9.31·10⁻⁸ | 9.61·10⁻⁷ | 1.71·10⁻⁵ | 9.61·10⁻⁷ |
| 10³ | 5.96·10⁻⁵ | 5.96·10⁻⁵ | 1.16·10⁻⁷ | 9.61·10⁻⁷ | 1.71·10⁻⁶ | 9.61·10⁻⁷ |
| 10⁴ | 5.96·10⁻⁴ | 5.96·10⁻⁴ | 7.28·10⁻⁸ | 9.61·10⁻⁷ | 5.40·10⁻⁷ | 9.61·10⁻⁷ |
| 10⁵ | 6.00·10⁻³ | 6.00·10⁻³ | 9.09·10⁻⁸ | 9.61·10⁻⁷ | 5.40·10⁻⁷ | 9.61·10⁻⁷ |
| 10⁶ | 0.0634 | 0.0634 | 1.14·10⁻⁷ | 9.61·10⁻⁷ | 5.40·10⁻⁷ | 9.61·10⁻⁷ |
| 10⁷ | 1.48 | 1.48 | 7.11·10⁻⁸ | 9.61·10⁻⁷ | 5.40·10⁻⁷ | 9.61·10⁻⁷ |

- **D1 killed, by my set-up, in its first clause.**
  - Z24 follows (d/n)(1 − n/f)·2^(−24) within 1% from 1 m to 10⁵ m. At 10⁶ m it is 6% over (0.0634 against 0.0596),
    and at 10⁷ m 1.48 against 0.6.
  - My formula was the first-order step, true only while the step is small. Far out one step of the buffer is no longer
    small against what is left of 1 − n/d, and the separation runs away faster than d/n. The buffer is worse far out
    than I predicted, not better.
  - The second clause holds exactly: IP24 at H = n gives Z24's r(d) at every d. Its stored value is Z24's,
    (1 − n/d)/(1 − n/f), so the standard depth buffer is the in-place lay with its corner at the near plane.
- **D2 not killed:** reversed-Z lies in (2^(−24), 2^(−23)] at every d, from 5.96·10⁻⁸ to 1.16·10⁻⁷.
- **D3 not killed:** log depth is 9.607·10⁻⁷ at every d.
- **D4 not killed.** The reader's lay at √(nf) is absolute inside the corner, Δd = 1.707·10⁻³ m (r = 1.7·10⁻³ at 1 m,
  1,800 times log depth's), and relative past it, 5.399·10⁻⁷, 1.78 times better than log depth.
- **D5 not killed:** the reader's lay at H = n is log depth, to the digit.
- **D6 not killed.** Every exponent of binary32 was checked at its first two and last two mantissas, 1,018 values (the
  spacing is constant within an exponent, so these cover all). Every value keeps both clauses: subnormals spaced
  2^(−149), and normals relatively in (2^(−24), 2^(−23)].
- **D7 killed in its letter**, by D1's first clause.

The verdict, read past that letter:
- The standard depth buffer is the in-place lay with its corner at the near plane. Log depth is the reader's lay with its
  corner at the near plane. A binary32 float is a reader's lay in base 2: proportional below its corner at the smallest
  normal, then 2²³ addresses in every level. Reversed-Z stores the in-place lay's reciprocal in that float, which is why
  its relative precision is constant.
- On depth precision the geometry adds no new scheme: it names the existing ones. The pair's corner, √(nf), trades
  precision near for precision far, so it is the right H only where absolute precision is wanted near. Rendering wants
  relative precision, and for that the corner belongs at the near plane, or below it, as floats put it.
