# CKD: the corner's kinds, for COR and BAL (a ruling's ground)

*27 October 2026. Tom: "yes", to "start with COR and BAL, since they're the item waiting on you". BAL's note ends "The
prediction's 'the ball's corner is contact' (s = 1, the radius equal to the distance, a ratio of two amounts) awaits
Tom's ruling with COR"; SPN's "Rulings on V and h under review" and `plans/physics-vh-audit.md` (l. 65, 81) flag COR, which
set "the corner" at a ratio of two physical amounts equal to 1. This plan sorts each of COR's six cases and BAL's contact
by kind, so the ruling can be made on what each s = 1 is. Predictions written before `runs/ckd/ckd.py` exists. Exact
(sympy for identities; mpmath at 50 digits for integrals and roots).*

The labs themselves are not edited above their runs (THE LAB GUIDE). Whatever this finds goes in a dated note below BAL's
and COR's runs and, if Tom rules, in SPN.

## Known beforehand

- **COR** (3 Oct, not killed): six cases, s "the reader's own quantity over the world's":
  - two loops (EPC), sin = min(s, 1/s);
  - escape (ESC), 1 − s then 1 − 1/s;
  - sampling (CRY), a fold 2 − s;
  - parallax (LAD), giving out at a shift of one address;
  - the glowing disc, f(s) + f(1/s) = 1;
  - a filling sky (OLB), a control with no corner, f(1) = 1 − 1/e.

  The independent review (3 Oct) already said escape's inversion holds by definition and the disc's is a proved identity.
- **BAL** (3 Oct, not killed): a ball of radius a at distance d. Its share of the addresses (laid evenly in turn across and
  up over the front half) is s²/π far off, s = a/d, and 1 at contact and past it.
- **MOT run 2** (11 Oct): two kinds of corner for a quantity f of a pair through its ratio k.
  - Swap-symmetric, f(k) = f(1/k): stationary at the corner (f′(1) = 0).
  - Sign-odd under the swap: zero at the corner, a change of regime.
- **SRR** (22 Oct, R437): a corner is a median only under a reciprocal-symmetric law on what is counted.
- **POR** (22 Oct, R439): a time corner of two amounts that moves with k.
- **CLAUDE.md**: "The corner" is h = v of a named pair and has no scale. A point set by an amount the reader brings (one
  step across) is the resolution limit, not the corner.
- **PXC** (12 Oct): parallax's own corner is the Thales circle, d = B/2. Its band runs acosh(1/ε)/ln 2 levels each side,
  10.966 at ε = 10⁻³.
- **NRF** (10 Oct): the Lambertian disc's projected solid angle, halfway at s = d/a = 1 and flip-symmetric.

## The kinds (definitions, fixed before the run)

Each case names its pair (p, q) and its s = p/q. Its quantity f is the reading the lab took. The kinds are tested in the
order below, and the first that fits is the case's kind.

- **E, an end.** s ranges over [0, 1] only (or s = 1 is where the readable range stops). There is no 1/s side to read,
  so "the far side is the near side at 1/s" has nothing to say.
- **R, a resolution limit.** s = x/ε with ε an amount (or angle) the reader brings. The place where s = 1 moves when ε
  changes, and the pair's own corner, if it has one, does not.
- **F, a fold.** f(s) = f(2 − s): a reflection in linear s, not the reciprocal.
- **C, the reciprocal's corner, three sub-kinds,** each with a reciprocal side to read:
  - **C-even, smooth:** f(s) = f(1/s) and f′(1) = 0 (MOT's stationary).
  - **C-even, kinked (a hand-over):** f(s) = f(1/s) with the one-sided slopes at 1 opposite and non-zero. One form rules
    below and its reciprocal above.
  - **C-odd (a complement or regime):** f(s) + f(1/s) is constant, or sign f flips between s and 1/s with a zero at 1.
- **N, none.** None of the above.

Separately, two tags:
- **direction:** s is the reader's own reading v/h of one direction (so s = 1 is the turn's 45°), or not.
- **scale test:** s is unchanged when every world length is multiplied by k with the reader's grain fixed, or not.

## Predictions

- **P1. BAL: contact is an end (E), not the corner; the ball's corner is at s = 1/√2.**
  - The pair (a, d) has s = a/d ≤ 1, since the reader stands outside or on the ball. s = 1 is where the limb's direction
    reaches 90° from the axis, sin α = s, the end of that sweep.
  - The limb's own corner is where the tangent's length equals the radius (v = h for the pair radius and tangent length,
    tan α = 1): α = 45°, s = 1/√2.
  - Scale test: s unchanged.
  - In BAL's lay (equal steps in azimuth and in elevation over the front half, the share being the lay's measure of the
    cap of half-angle α), the share at the corner α = 45° is under ½, so BAL's middle (half the addresses filled) lies
    past the corner, s > 1/√2.
  - The far law s²/π, and the full share at α = 90°, are as BAL found.
  - **Killed if** s = 1 has a reciprocal side in BAL's set-up; or the share at α = 45° is ½ or more; or the share at
    α = 90° is not exactly 1, or share/s² as s → 0 is not 1/π (to 10⁻²⁰ at s = 10⁻¹⁰).
- **P2. Two loops (EPC): C-even, kinked, a hand-over.**
  - f(s) = min(s, 1/s), s = r_body/r_reader, so f(s) = f(1/s).
  - One-sided slopes at 1 are +1 and −1 in s, and ±1 in ln s (f = e^(−|ln s|)).
  - Not a direction (two radii, amounts); scale test: unchanged.
  - The corner is that of the capped pair (r_reader, r_body), the ℓ∞ cut, Copernicus's division into inner and outer.
  - **Killed if** the swap identity fails anywhere on a grid of 41 values of s in [1/50, 50], or a one-sided slope is not
    ±1.
- **P3. Escape (ESC): the shares C-even, kinked, by definition; the energy C-odd, a change of regime.**
  - The two shares as COR defined them, 1 − s below and 1 − 1/s above (s = kinetic over the pull's), are one function
    even under the swap with slopes ∓1 at 1: a hand-over by construction, as the 3 Oct review said.
  - The physical quantity, the total energy, is proportional to s − 1. It is zero at 1 and changes sign under the swap,
    but is not odd in value ((1/s − 1) = −(s − 1)/s): C-odd in sign only, a change of regime (bound to free).
  - Not a direction; scale test: unchanged (with Wander's mass as size cubed, both energies go as k⁵).
  - **Killed if** the shares fail the swap identity, or the energy's sign does not flip between s and 1/s for every s ≠ 1
    on the grid.
- **P4. Sampling (CRY): F, a fold, and an end (E) for what is read.**
  - The rate read, as a fraction of half a turn per reading, is f(s) = s mod 2 folded, min(s mod 2, 2 − s mod 2).
    f(s) = f(2 − s) exactly.
  - f(s) ≠ f(1/s) and f(s) + f(1/s) is not constant (at s = ½: f = ½, f(2) = 0).
  - s = 1 (Nyquist) is where the readable range ends: past it the readings repeat.
  - Not the reciprocal's corner. Scale test: unchanged (two rates).
  - **Killed if** f(s) = f(1/s) at every s on the grid, or f(s) + f(1/s) is the same at every s on it; or f(s) ≠ f(2 − s) anywhere in [0, 2].
- **P5. Parallax giving out (LAD): R, a resolution limit, ε apart from parallax's own corner.**
  - s = γ/ε, γ ≈ B/d the parallax angle, ε the reader's angular grain. s is unchanged by scaling the world (B and d
    together), but s = 1 moves with ε: halving ε doubles the distance at which parallax gives out (d ≈ B/ε).
  - The pair (B/2, d) has its own corner at d = B/2 (the Thales circle), independent of ε.
  - The two are apart by about log₂(2/ε) levels, 10.966 at ε = 10⁻³ by PXC's exact form acosh(1/ε)/ln 2.
  - **Killed if** the give-out distance does not double (to 10⁻⁶ relative) when ε halves, at ε = 10⁻², 10⁻³, 10⁻⁴; or the
    separation at 10⁻³ is not PXC's 10.966 (to 10⁻³).
- **P6. The glowing disc: C-odd (a complement), and the one case whose s is a direction the reader reads.**
  - A Lambertian disc of radius a seen on its axis from distance d. The share (projected solid angle over π) is
    f = 1/(1 + s²), s = d/a, so f(s) + f(1/s) = 1 exactly; f(1) = ½; f′(1) = −½, not zero.
  - The rim's direction from the axis reads v/h = a/d = 1/s. So s = 1 is the rim at the turn's 45°, and f = sin² of the
    rim's angle: the foot.
  - Scale test: unchanged.
  - **Killed if** the complement identity fails anywhere on the grid; or f is not sin²(arctan(1/s)) to 10⁻⁴⁰.
- **P7. The filling sky (OLB): N.**
  - f(s) = 1 − e^(−s), s = reach/mean free path.
  - f(1) = 1 − 1/e = 0.63212…; f(s) ≠ f(1/s); f(s) + f(1/s) not constant (1.269 at s = 2, as COR found); no sign change.
  - Not a direction; scale test: unchanged.
  - **Killed if** any of E, R, F or C fits at every s on the grid.
- **P8. The sort.** Of the seven:
  - **C:** three (two loops, escape, the disc), which have a reciprocal side, and only these are corners of their named
    pairs;
  - **E:** one (BAL's contact), and sampling's Nyquist is an end as well as a fold (F);
  - **R:** one (parallax);
  - **N:** one (the sky).

  Only the disc's s is the reader's own reading of a direction. Every s passes the scale test, but parallax's s = 1 moves
  with ε. **Killed if** the sort differs from this in any case.

## What a ruling could then say (for Tom; not decided here)

COR's "s = 1" is the corner of its named pair where the pair has a reciprocal side (two loops, escape, the disc). It is an
end where the ratio cannot pass 1 (BAL's contact, sampling's Nyquist). It is the resolution limit where one amount is the
reader's grain (parallax). There is none for the sky. BAL's own corner would then be the limb at 45°, s = 1/√2, not
contact.

## Runs

(none yet)
