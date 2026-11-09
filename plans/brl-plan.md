# BRL: does a breath close? The loop of `breath-note.md` §2, checked exactly

9 Nov 2026. Tom: "yes", to the breath note's open item 1 (check §2's leftover exactly: the plane's loop closes to
rounding; the space loop's leftover against α·β and TWG's exact form).

## Known beforehand (stated so the predictions are not mistaken for discoveries)

- In the plane a turn and a scaling commute: e^(iα)·e^(λ) = e^(λ)·e^(iα) (R738; essay 18 §7).
- In space a uniform scaling k·I commutes with every turn (it is central in GL(3)); FLC (R743) says the log-polar
  cylinder ℝ × S² keeps scaling a slide commuting with every turn.
- Two turns of space about axes n₁, n₂ (angle φ apart), taken and undone in turn, leave a turn about n₁ × n₂ (the group
  commutator; Lie's bracket [L_x, L_y] = L_z). TWG run 3 (W7) has the case of equal angles exactly:
  cos(Ω/2) = 1 − 2·sin⁴(ε/2)·sin²φ, Ω = 4·arcsin(sin²(ε/2)·|sin φ|), to 10⁻⁹⁵.
- On reading the note's §2 again before this plan: its "breath in space" is two turns about two axes, that is, **two reads
  joined**, with no write in it. A breath in the note's own sense (§1, §2) is a read (a turn) and a write (a scaling). So
  this plan tests both, and the note is to be corrected by whichever result stands.

## Predictions (written before the run)

Exact arithmetic (mpmath, 60 digits): turns as 3 × 3 matrices from Rodrigues' formula, also as unit quaternions; scalings
as k·I; the plane as complex numbers. Loops applied left to right in time: first act A, then B, then A⁻¹, then B⁻¹, the
product M = B⁻¹·A⁻¹·B·A (acting on column vectors).

- B1. The plane's breath closes: for a turn e^(iα) and a scaling e^λ, M = 1 to 10⁻⁵⁸, at 20 seeded (α, λ), |α| ≤ π,
  |λ| ≤ 3.
- B2. A breath in space closes: a turn by α about any axis n and a scaling k = e^λ, M = I to 10⁻⁵⁸, at 20 seeded (n, α, λ).
  Kill: any entry of M − I above 10⁻⁵⁰.
- B3. Two reads joined do not close, and their leftover has the exact form, generalizing W7 to unequal angles:
  cos(Ω/2) = 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ, for turns α about n₁ and β about n₂, φ the angle between the axes. At 30
  seeded (α, β, φ) with α, β in (0, π]. Kill: any mismatch in Ω above 10⁻⁵⁰ (after checking the residual is a turn: M
  orthogonal, det 1).
- B4. Its leading order and sign: Ω = α·β·sin φ + O(third order), about the axis of n₂ × n₁ (for "first about n₁, then
  about n₂, then back, back"), i.e. with n₁ = x and n₂ = y, a turn by about α·β clockwise about z. Checked at
  α = β = ε for ε = 10⁻¹ … 10⁻⁶ (the ratio Ω/(αβ sin φ) → 1, the axis to within O(ε) of −z). Kill: the axis nearer +z.
- B5. A write anywhere in the two-read loop changes nothing: inserting a scaling k (and its inverse at any later place, or
  even unmatched) leaves the turn part of M the same as B3's, to 10⁻⁵⁰; an unmatched scaling leaves M = k·(B3's turn).
  Kill: any turn part that differs.
- B6. W7 recovered: at α = β = ε, B3's form reduces to 4·arcsin(sin²(ε/2)·|sin φ|), to 10⁻⁵⁰ (an identity, stated so).

Reading if nothing is killed: the breath (a read and a write) closes in the plane and in space alike, because a write in
the across sense is a scaling and scaling commutes with every turn. What leaves something behind in space is not
breathing but two reads in different directions joined into a loop: the leftover belongs to the reads' sphere (holonomy,
HOL's transport turn by solid angle; Berry's phase), and no write enters it. So the note's §2 "each breath in space comes
home turned" is wrong as worded and should say: a breath closes everywhere; a loop of reads in two directions does not.

## Runs

### Run 1 (9 Nov 2026), `runs/brl/brl.py` (60 digits), output `runs/brl/brl-run1.txt`; B3 killed by my measure

- B1 held: the plane's breath closes to 1.7·10⁻⁶¹.
- B2 held: a turn and a scaling in space close to 1.6·10⁻⁶¹.
- B3 **killed**: the residual is a turn (orthogonal, det 1, to 6·10⁻⁶¹), but |Ω − form| reached 2.86. Post hoc (a
  diagnostic replaying the same draws): 3 of 30 draws differ, all with the predicted Ω above π, which a rotation matrix's
  trace can only report as 2π − Ω; cos Ω matches the form's to 3.9·10⁻⁶¹ in all 30. So the kill is my measure (an angle
  read from a 3 × 3 matrix is folded into [0, π]), not the form. It stays killed; run 2 tests the form unfolded.
- B4 held: Ω/ε² = 1 − ε²/12 + …, as W7's c_T = −1/12 (0.99916798 at ε = 0.1, 0.999999999999917 at 10⁻⁶); the axis −z,
  tipped toward (1, −1, 0)·ε/2; at α = 2·10⁻⁵, β = 3·10⁻⁵, φ = 60°, Ω/(αβ sin φ) = 0.99999999995.
- B5 held: a scaling put in matched anywhere leaves M as the two-read loop's to 1.6·10⁻⁶¹; unmatched, M is k times it.
- B6 held: at α = β the form is W7's, to 9·10⁻⁶⁰.

## Run 2 predictions (written before run 2)

- B3′. In unit quaternions (q(n, α) = cos(α/2) + sin(α/2)·n), the loop's commutator Q = q₂⁻¹q₁⁻¹q₂q₁ has scalar part
  exactly 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ (independent of either quaternion's sign, so it fixes Ω in [0, 2π]), and its
  3 × 3 image is run 1's M. At the same 30 draws and 200 more with α, β in (0, 2π). Kill: any scalar part off by more
  than 10⁻⁵⁰, or the image off M by more than 10⁻⁵⁰.

### Run 2 (9 Nov 2026), `runs/brl/brl2.py` (60 digits), output `runs/brl/brl-run2.txt`; nothing killed

- B3′ held: over 230 draws and the four sign choices of the two lifts, the commutator's scalar part equals
  1 − 2·sin²(α/2)·sin²(β/2)·sin²φ to 3.9·10⁻⁶¹ (13 draws with Ω above π, where run 1's measure folded); its 3 × 3 image is
  run 1's M to 8.6·10⁻⁶¹.

Reading: the breath closes, in the plane and in space. A read (a turn) and a write (a scaling) commute everywhere, and a
write put anywhere into a loop changes nothing but its overall size (B5). What comes home turned in space is a loop of two
reads in different directions: cos(Ω/2) = 1 − 2·sin²(α/2)·sin²(β/2)·sin²φ, Ω ≈ αβ·sin φ about n₂ × n₁, W7 its equal-angle
case. The leftover is the reads' alone: the sphere of directions not being flat (HOL, Berry), with no write in it. The
note's §2 is corrected accordingly. Classical throughout (the scaling central; the SU(2) commutator); the reading ours.

## Run 3 predictions: the unsteady breath (9 Nov 2026, Tom: "yes", written before run 3)

The breath note's open item 3: what does not close? A breath closes because its write, a uniform scaling, commutes with
every turn. A write that does not is a stretch, one axis scaled and not the other: V = cH with c ≠ 1, the two-axis drawing
only a writer holds (R533). In the plane: turn R(α), stretch S = diag(c, 1), λ = ln c, loop M = S⁻¹R⁻¹SR. Derived by hand
before the run (from R⁻¹SR's entries): tr M = 2 + sin²α·(c + 1/c − 2).

- B7. The unsteady breath does not close, and its leftover is not a turn: det M = 1 and
  tr M = 2 + 4·sin²α·sinh²(λ/2) ≥ 2 exactly, so M is hyperbolic (a boost-like squeeze, real eigenvalues e^(±ζ)) with
  cosh ζ = 1 + 2·sin²α·sinh²(λ/2). At 40 seeded (α, λ), |λ| ≤ 3. Kill: any trace off by more than 10⁻⁵⁰, or det off 1.
- B8. It closes only where a factor vanishes: M = I to 10⁻⁵⁰ at c = 1 (V = H) for every α, and at α = π for every c
  (R(π) = −I); nowhere else among the draws (‖M − I‖ above 10⁻³ at every draw with |λ| > 0.05 and |sin α| > 0.05).
- B9. Small loops: ζ = |α·λ|·(1 + O(second order)), the same leading form as the two-read loop's αβ·sin φ (B4), the
  stretch's λ in place of the second turn. Checked at α = λ = ε, ε = 10⁻¹ … 10⁻⁶. Kill: ζ/(αλ) not tending to 1.
- B10. The exchange and the frame: ζ is the same at c and 1/c (λ ↦ −λ), the same for a stretch along any axis (S
  conjugated by a turn) and the same with a uniform scaling k put in (k·S): it depends on how unequal the two lengths are,
  not on their size or direction. To 10⁻⁵⁰ at the B7 draws.
- B11. Breathing unsteadily drifts: after n loops a vector's length grows at most like e^(nζ), and the largest growth over
  directions after n loops is e^(nζ) exactly (M symmetric-conjugate: its largest singular value of Mⁿ, against e^(nζ),
  within a factor bounded in n). Kill: growth rate per loop, ln σ_max(Mⁿ)/n at n = 400, off ζ by more than 10⁻².
- B12. In space: a turn by α about z and S = diag(c₁, c₂, c₃) close only if c₁ = c₂ (the two lengths square to the
  turn's axis written equal) or α ∈ πℤ (for α = π, any S); c₃ never matters. At 20 seeded draws each way. Kill: a
  closing with c₁ ≠ c₂ and α ∉ πℤ, or a failure to close with c₁ = c₂.

Reading if nothing is killed: a breath is steady exactly when its write is the one-length kind. A write in one length
(V = H, the reader's circle traced) commutes with every turn and the breath closes; a write in two unequal lengths (V = cH,
a writer's two axes) leaves a squeeze, not a turn, growing breath by breath at ζ ≈ |α·ln c| per loop and vanishing only
at c = 1. The unsteady breath is c ≠ 1. The leftover of two reads (B3) is a turn and stays bounded; the leftover of an
unequal write is a squeeze and accumulates.

### Run 3 (9 Nov 2026), `runs/brl/brl3.py` (60 digits), output `runs/brl/brl-run3.txt`; nothing killed

- B7 held: det M = 1 to 1.6·10⁻⁶¹, tr M = 2 + 4·sin²α·sinh²(λ/2) to 1.2·10⁻⁶⁰ at 40 draws: the leftover a squeeze, never a turn.
- B8 held: closes at c = 1 (1.6·10⁻⁶²) and at α = π (2.1·10⁻⁶⁰); open at every other draw.
- B9 held: ζ/(αλ) = 1 − ε²/8 + … (0.998746 at ε = 0.1, 0.999999999999875 at 10⁻⁶).
- B10 held: ζ the same at 1/c, with the stretch turned to any axis and with a uniform scaling put in, to 2.1·10⁻⁵⁹.
- B11 held: the growth per loop of Mⁿ's largest stretch at n = 400 is ζ to 3.6·10⁻⁴ (11 draws with ζ ≥ 0.01; the
  difference is the (ln κ)/400 of M's conditioning, falling as 1/n).
- B12 held: in space, a turn about z and diag(c₁, c₂, c₃) close exactly when c₁ = c₂ or α = π, 0 failures in 60 cases.

Reading: a breath is steady exactly when its write is the one-length kind. Written in one length (V = H) the write commutes
with every turn and the loop closes; written in two unequal lengths (V = cH, c ≠ 1, a writer's two axes) the loop leaves a
squeeze of rapidity ζ, cosh ζ = 1 + 2·sin²α·sinh²(½ ln c), about |α·ln c| when small, the same at c and 1/c, in any frame
and at any size, and breath after breath it accumulates. Two reads leave a turn, bounded (B3); an unequal write leaves a
squeeze, growing. Classical (the commutator of SO(2) with a diagonal matrix in SL(2)); the reading ours.
