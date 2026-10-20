# MAP: what it takes to map, the two readers made into a mapper

*19 October 2026 (Tom's local date), SPN R396.*

*Tom (20:33 MDT): "keep on exploring how to map the room with the payload and address reader. do a thought expirment,
what would be needed to turn the two readers into something that could map a room." Claude's thought experiment is
now `papers/mapping.md` §7½. Then (21:02): "both", the section and this plan.*

*Exact where a closed form exists (mpmath), seeded otherwise. Scripts in `runs/map/`. Predictions written before the
script. Distances in |AB|, the step's own length, which no reading gives.*

## Known beforehand

- **Epipolar geometry.** Given the relative pose, a point seen in one view lies on a line in the other; two rays from
  different centres generically do not meet unless they see the same point (Longuet-Higgins 1981; Hartley and Zisserman
  2004). **[classical]**
- **Descriptors.** A keypoint's descriptor is used to find the same point in another view; ambiguous matches are
  rejected by the ratio test (Lowe 2004). **[classical]**
- **Rotation from points at infinity.** Directions to very far points are unchanged by translation, so they fix the turn
  between views (Civera, Davison and Montiel 2008). Kabsch's or Horn's method recovers it from direction pairs.
  **[classical]**
- **draw's UDV:** standpoints give the figure up to size, and one agreed length the size. **RCC:** the readings carry the
  turn, not the size.
- **This corpus:**
  - `room-ratios.html`: two places, rays crossing, places in steps.
  - TRI: bearings read from a height γ, depth error Cauchy(0, 2γ·cosh ln k).
  - OFS §9's "Closing a loop": a tree cannot find its own error, a loop can.
  - WRD: ranging with a wrong held speed keeps the shape.

## The set-up

- **The room and its features.** A room 5 × 4 × 2.5 m. N = 80 feature points, a seeded mix:
  - 50 on the walls, floor and ceiling;
  - 30 on four things (`room-ratios`' table, cube, ball, cabinet);
  - 6 far features "through a window", at 10⁶ m.
- **The payload.** Each feature has a payload: a 16-number descriptor, drawn once per feature (seeded, standard normal),
  received at each standpoint with independent noise of standard deviation σ_p.
- **The standpoints.** A, B and C, each a unit step apart in a seeded direction, all inside the room, each turned by a
  seeded rotation.
- **What each standpoint reads.** Each standpoint reads every feature's address [h : v : v₂] in its own frame:
  - exact (ε = 0);
  - or with each direction perturbed by an angle of standard deviation ε.
- **The referee** holds every true place.
- **Nothing reads a length**, except where a prediction says so.

## Predictions

**M1 (addresses alone: exact matches the pair, finite resolution does not).** With the turn and the step's direction
known and ε = 0:
- each A ray meets exactly one B ray, its true partner's, to 10⁻⁴⁰ in |AB|;
- every other pair's closest approach is at least 10⁻⁶ |AB|, over all 80 × 79 wrong pairs in five seeded rooms.

At ε = 10⁻³ and 10⁻²:
- the share of A rays with more than one B ray within the reading's own reach (3ε times the ray's distance, on the
  common perpendicular) is above 0 and rises with ε;
- the share at 10⁻² is larger than at 10⁻³.

*Killed* if exact readings leave any wrong pair within 10⁻⁶, or the ambiguous share does not rise with ε.

**M2 (the payload names the pair).**
- With σ_p = 0.1 and each A feature matched to the B feature of nearest descriptor, all 80 matches are right, in five
  seeded rooms.
- Triangulated from those matches at ε = 0, every place equals the referee's, in |AB| and in A's frame, to 10⁻³⁰.

*Killed* if any match is wrong, or any place misses by more than 10⁻³⁰.

**M3 (the scale stays out).**
- Scaling the world, the step included, by k ∈ {10⁻³, 7, 10³} changes no address (10⁻⁴⁰), no match, and no place in
  |AB| (10⁻³⁰).
- One counted stride, the step's length carried in, writes metres equal to the referee's, to 10⁻³⁰.

*Killed* if not.

**M4 (each half checks the other).**
- In B's view, swap the payloads of two features (a wrong match, both ways) for 10 seeded pairs.
- At ε = 0, the two rays of every wrong match pass at least 10⁻⁶ |AB| apart, and every right match's meet to 10⁻⁴⁰.
  So the addresses flag every wrong payload match.
- With three standpoints, the place triangulated from (A, B) for a swapped feature differs from the one from (A, C) by
  at least 10⁻⁶ |AB|, while every unswapped feature agrees to 10⁻³⁰. So the loop locates the swap at the swapped features.

*Killed* if any wrong match passes as right, or any right one fails.

**M5 (a ranging payload in an unread unit: the shape from one place).**
- From A alone, the payload carries a range u·d along each address, u ∈ {0.73, 1, 1.27}: a wrong held speed, as with the
  bats.
- Every ratio of two distances between features equals the referee's, to 10⁻³⁰, at every u.
- Every place is off by the factor u exactly.

*Killed* if not.

**M6 (the turn from far features).**
- The rotation between A and B, recovered from the six far features' addresses alone (Kabsch on the direction pairs,
  ε = 0), is off by at most 10⁻⁵ rad. The far features' own parallax is |AB|·6 m / 10⁶ m at most, of order 10⁻⁶.
- M2's places triangulated with that recovered rotation miss the referee's by at most 10⁻⁴ |AB|.

*Killed* if either bound fails.

**M7 (the verdict).** A judgment. *Killed* if M1, M2, M4 or M6 is killed.
- The two readers become a mapper with four acts (turn, hold, step, match) and one amount.
- The address says where and the payload says which.
- At exact resolution the addresses could find every pair alone; at a finite one only the payload can.
- Each half checks the other: rays that do not meet flag a wrong match, and a loop places the error.
- The scale enters only at the end.

## What would and would not be shown

**Shown:** the division of labour between the two readers, exactly, in a synthetic room.

**Not shown:**
- that this beats the usual pipeline (that is AFM, `papers/mapping.md` §11 item 1);
- real images, where descriptors are not independent draws and features are found, not given;
- moving things.

## Runs

(Nothing above this line is edited after a run.)
