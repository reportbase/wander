# COS: a cosine weight with no amount

25 Nov 2026; Tom: "1 then 3". *Reads and Writes* §7, "Gravity on the stage", open item (1): FCL run 10 found the read's
own odd moment (the heat met below the corner less the heat above) and the pull's (the paint's first moment, amounts
weighted by the cosine to a facing), and left open "whether any read-side moment carries a cosine weight without an
amount". Exact arithmetic (sympy) and 30-digit quadrature (mpmath); no data. A pull is not a read (R1183).

## The candidate

A read holds which directions are painted, not how much (the scale test moves nothing it holds). Take the paint as
presence only: o(u) = 1 where a direction from the place meets matter, 0 where it meets nothing. Its faced take is

  F_o(n) = ∫ o(u)·max(0, u·n) dΩ,

a cosine-weighted count of directions, with no amount in it. Its first moment is D = ∫ o(u)·u dΩ, the vector of
projected solid angle (the view factor of radiative transfer, Nusselt's unit-sphere construction, from memory).

The pull at the place, from matter of density ρ, is G·∫ u·ρ·L(u) dΩ-type sums: for uniform density, G·ρ·∫ o(u)·u·L(u) dΩ,
L(u) the length of matter along u (the column, GRV). So the pull is the same cosine-weighted integral with each
direction weighed by an amount, ρ·L(u). Write the pull as G·ρ·⟨L⟩·D, which defines ⟨L⟩, the cosine-weighted mean column,
along D.

## Predictions (committed before any code)

- **K1 (the identity).** F_o(n) − F_o(−n) = n·D for every facing n and every scene, and the six axis facings give D
  (checked on a ball and on two balls by quadrature to 10⁻¹²).
- **K2 (no amount).** D is unmoved by scaling every length by k and by any increasing map of the densities (ρ ↦ ρ³,
  ρ ↦ e^ρ): exactly, since o is presence only. The pull moves under both (by k, for ρ fixed, and by the map).
- **K3 (the ball's inverse square).** For a ball of radius R at distance d > R, D = π(R/d)²·n̂ exactly: an inverse
  square in a ratio of lengths, with no mass and no G.
- **K4 (the ball's constant).** For a uniform ball, ⟨L⟩ = 4R/3 at every d > R exactly; for a uniform shell between a and R,
  ⟨L⟩ = (4/3)(R³ − a³)/R², the same at every d > R. So outside any body of this kind the pull is the read's cosine
  weight D times one amount, G·ρ·⟨L⟩, fixed by the body alone.
- **K5 (not in general).** For a unit cube approached face-on along its axis, ⟨L⟩ changes with distance: between a place
  0.5 and 20 side lengths from its near face it changes by more than 1%. The constant of K4 is the ball's (and the
  shell's), not every body's.
- **K6 (occlusion).** A small ball hidden wholly behind a larger one leaves D unchanged and adds its whole GM/d² to the
  pull: D counts a direction once, the pull sums the whole column.

Kill conditions: K1 or K3 or K4 off by more than 10⁻¹² (quadrature) or not identities in sympy; K2 a change in D past
10⁻¹²; K5 a change under 1%; K6 a change in D past 10⁻¹² or a pull not raised by the hidden ball's whole share.

What it would answer: item (1), yes, if K1–K4 hold: a read-side moment with the cosine weight and no amount exists (the
occupancy's first moment, the projected solid angle), and a pull is it with each direction weighed by its column's
amount; for a spherical body the weighing is one number.

## Runs

### Run 1 (`runs/cos/cos.py`, output `runs/cos/cos-run1.txt`)

Nothing killed.
- **K1 not killed**: F_o(n) − F_o(−n) = n·D for two balls at four facings to 8.6·10⁻³², the six axis facings giving D to
  6·10⁻³² (pointwise max(0, x) − max(0, −x) = x, so it could fail only by the quadrature).
- **K2 not killed**: D unmoved by lengths × 7 (2·10⁻³²) and by any map of the densities (it holds none); the pull × 7,
  and its direction turned 0.355 rad by ρ ↦ ρ³ and 0.148 rad by ρ ↦ e^ρ.
- **K3 not killed**: D = π(R/d)² for a ball, exactly (sympy).
- **K4 not killed**: ⟨L⟩ = 4R/3 for the ball and (4/3)(R³ − a³)/R² for the shell, exactly, with no d in either.
- **K5 not killed**: the face-on unit cube's ⟨L⟩ 0.542, 0.583, 0.692, 0.837, 0.953, 0.995 at 0.5, 1, 2, 5, 20, 200 from
  its near face: 43% between 0.5 and 20.
- **K6 not killed**: a ball hidden behind a larger one adds nothing to D and its whole (4/3)πr³/64 to the pull.

Seen after the run, not predicted: the cube's ⟨L⟩ runs to 1 far off, its volume over the area it presents (the column a
far place meets is the cube's own depth), not to 4V/S = 2/3, Cauchy's mean chord; the ball's 4R/3 happens to be both.
And K4 is Newton's shell theorem read this way: outside a body with spherical symmetry the column's cosine-weighted mean
is one number fixed by the body, so the pull is the read's D times one amount.

Reading: item (1) answered, yes. A read holds a first moment with the cosine weight and no amount: the occupancy's, the
projected solid angle D (classical as the view factor). Its odd part over a facing and its opposite is n·D, as the
pull's is n·g. A pull is that same integral with each direction weighed by an amount, its column (the depth of R1192),
and the two part where the columns differ (a cube's near and far) or where a direction is occupied twice (K6): a read
counts a direction once, a pull sums all along it. Classical throughout (Lambert, Nusselt, Newton); the sorting ours.
