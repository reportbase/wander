# TLP: three systems in a loop, reading each other's directions

17 November 2026. SPN R1072. Tom: "Yes, write the plan and run the test", to essay 30 §13's first open item (three
things reading each other round a triangle: does the exchange settle, cycle, or come back turned?).

## The question

MRL's loops closed, but they were loops of owned amounts (scalar slopes). Here each system also has its own facing, a
frame it reads directions in. Round a triangle of three systems, what do the mutual directions say about the frames, and
what happens when each system turns its frame toward agreement with the others? Does the exchange settle, cycle, or come
back turned for ever?

## The set-up

- **Three systems** at places P_1, P_2, P_3, each with its own frame. In the plane a frame is a unit complex number f_i;
  on a sphere, a unit tangent vector at P_i.
- **A direction read.** In the plane, i reads j as z_ij = (P_j − P_i)·conj(f_i): a direction in i's own frame (its size is
  the distance, which no comparison below uses). On the unit sphere, i reads j as the bearing β_ij of the great circle
  from P_i to P_j, measured from i's frame.
- **The owned turn on an edge.** From the two mutual readings alone: in the plane ρ_ij = −z_ij/z_ji; in angles
  r_ij = β_ij − β_ji + π (wrapped to (−π, π]). Turning frame i by φ_i lowers every β_ij by φ_i, so r_ij moves by
  φ_j − φ_i.
- **Loop sum** S = r_12 + r_23 + r_31.
- **Two exchange rules**, with a share α each round, all systems at once:
  - *mutual*: each turns toward both neighbours, φ_i += α(r_(i,i+1) − r_(i−1,i));
  - *cyclic*: each turns toward its next neighbour only, φ_i += α·r_(i,i+1).
- **Arithmetic.** The plane exactly: rational places and rational unit frames f = (1 − t² + 2it)/(1 + t²), the exchange
  in Fractions. The sphere at 50 digits (mpmath).

## Predictions (committed before any run)

- **T1. The turn is owned and read from directions alone.** In the plane ρ_ij = f_j/f_i exactly, a unit complex number:
  the distance cancels and so does every other system. Round the triangle ρ_12·ρ_23·ρ_31 = 1 exactly (S = 0), for 200
  random triangles and frames.
- **T2. Euler's −1 is the angle sum.** Each system's own reading of the angle it sees, z_(i,i−1)/z_(i,i+1), multiplied
  over the three systems, is exactly −1 in Gaussian rationals, whatever the frames: the interior angles add to π, read in
  three private frames that cancel.
- **T3. The count.** In the plane the six bearings depend on 3 frame angles and 6 coordinates; the Jacobian has rank 5 at
  random rational points (9 variables less the 4 of one turn, two translations and one scale; the one relation among the
  six is T2's angle sum). In space, with each frame a full rotation, the six unit bearings (12 numbers) depend on 18
  variables; rank 11 (less 3 turns, 3 translations, 1 scale; one relation, the angle sum).
- **T4. On the sphere the loop comes back turned by the area.** |S| equals the spherical excess E (computed independently
  from the three side lengths by L'Huilier) to 10⁻⁴⁰ for 50 random triangles, whatever the frames; reversing the order of
  the loop flips the sign of S. Shrinking a triangle toward a point by k, S/k² tends to a constant (the flat area), so
  S → 0 like the area.
- **T5. Scaling.** In the plane S = 0 at every scale. On the sphere, S depends on the triangle's size against the
  sphere's radius: a triangle with the same side lengths in amounts on a sphere of radius R has excess area/R² (to
  leading order), and scaling the whole world (sphere and places) by k leaves S unchanged. So a loop comes back turned
  only where an amount, the radius of curvature, enters.
- **T6. Mutual exchange.** The sum S is preserved every round. The edge residuals e_i = r_(i,i+1) tend to S/3 each, the
  deviation multiplied by exactly (1 − 3α) a round (exactly in Fractions in the plane, where S = 0 and the frames come to
  agree); stable for 0 < α < 2/3. On the sphere the frames stop, every edge left disagreeing by S/3: no drift, but no
  agreement.
- **T7. Cyclic exchange.** S preserved; the residuals tend to S/3 each, the squared deviation multiplied by exactly
  (1 − 3α + 3α²) a round, spiralling (complex eigenvalues 1 − α(1 − ω), ω a cube root of 1). In the plane the frames
  settle (S = 0). On the sphere they never do: at rest every frame turns by α·S/3 every round for ever, to 10⁻⁴⁰ after 400
  rounds. The loop comes back turned.

## Kill conditions

Any exact equality failing in Fractions; a rank other than 5 or 11; |S| − E above 10⁻⁴⁰; S not flipping with the order;
an exchange's rate or rest value off its formula beyond 10⁻⁴⁰; a frame drifting in the plane or not drifting on the
sphere under the cyclic rule.

## What this does not test

- Moving systems (boosts): TWG already has the Thomas–Wigner loop.
- Whether any real system uses either rule. The rules are chosen, as in MUT.
- Novelty: holonomy on the sphere (Girard, Gauss–Bonnet), the Laplacian of a cycle and consensus rates, and frustrated
  cyclic consensus are classical. What is ours is the sorting (R1071).

## Runs

**Run 1** (`runs/tlp/tlp.py`, output `runs/tlp/tlp-run1.txt`, 17 Nov).
- **Not killed: T1, T2, T3, T4, T6, T7.**
  - T1: ρ_ij = −z_ij/z_ji = f_j/f_i exactly on 200 triangles, a unit complex number, the loop product 1.
  - T2: the three systems' own angle readings multiply to −1 exactly, in three private frames.
  - T3: rank 5 in the plane (exact) and 11 in space (the 12th singular value about 10⁻⁶¹ at 60 digits).
  - T4: |S| equals the excess to 5·10⁻⁵⁹ on 50 random triangles; reversing the loop gives −S; shrunk by k, |S|/k² settles
    (0.3815, 0.3592, 0.35707, 0.35685).
  - T6: in the plane every residual times (1 − 3α) a round exactly, S = 0 kept, α = 7/10 diverging; on the sphere
    (S = 2.2969) S kept to 4·10⁻⁶⁰, the residuals at S/3, the frames stopped.
  - T7: in the plane the squared deviation times (1 − 3α + 3α²) a round exactly; on the sphere the residuals at S/3 to
    7·10⁻⁵⁸ and every frame turning α·S/3 = 0.15313 a round for ever, off by 2·10⁻⁵⁸ after 400 rounds.
- **T5 killed, by my code.** The plane's ρ was unchanged by 50 scalings exactly, and the 3-4-5 triangle's E·R²/area went
  1.0213, 1.00021, 1.0000021 at R = 10, 100, 1000. But the world scaled by 7 moved S by 0.564. My bearing took the tangent
  as P_j − (P_i·P_j)·P_i, which is right only for unit vectors; on a sphere of radius 7 it is not the tangent.

**Run 2 prediction** (committed before run 2):
- **T5′.** With the tangent P_j − (P_i·P_j/|P_i|²)·P_i and the frame's second axis P_i × e_i/|P_i|, scaling the whole
  world (sphere and places) by 7, 1/3 and 1000 leaves S unchanged to 10⁻⁴⁰ for 20 random triangles and frames.

**Run 2** (`runs/tlp/tlp2.py`, output `runs/tlp/tlp-run2.txt`). **T5′ not killed**: scaling the world by 7, 1/3 and 1000
moved S by at most 2·10⁻⁶⁰ on 20 triangles.

**What the runs show.**
- **In the plane the loop closes, and the exchange settles.** Each edge's turn between two frames is read from the two
  mutual directions alone (ρ = −z_ij/z_ji): the distance cancels, and so does every other system. Round the triangle the
  turns multiply to 1, a cocycle with a potential (each system's own facing), so both rules bring the frames to agree.
- **Euler's −1 is the triangle's angle sum, read from three private frames.** The three systems' own angle readings
  multiply to −1 exactly, whatever their frames.
- **The count.** Six mutual bearings carry 5 numbers in the plane, 11 of 12 in space: everything but one turn, the
  translations and one scale, with the angle sum the one relation.
- **On the sphere the loop comes back turned, by the area.** The turns round the triangle add to the spherical excess,
  the same in every frame and changing sign with the loop's order. The mutual rule then stops with every edge left
  disagreeing by S/3; the cyclic rule never stops, every frame turning α·S/3 a round for ever.
- **The turn needs an amount.** Scaling the whole world moves nothing; the excess is area/R², the triangle against the
  sphere's radius. In the plane there is no such amount, and no turn is left.
- **Classical**: Girard's theorem and Gauss–Bonnet, holonomy, the cycle's Laplacian and consensus rates, frustrated
  cyclic consensus. The sorting is ours (R1071): the turn on an edge is read; the loop's leftover is the world's
  curvature, which a read meets but a size sets; whether the exchange settles or turns for ever is the rule, each
  system's own write.
