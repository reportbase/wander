# MON: one moon moving across the sky, detected by the inscribed sweep, painted by the central

*17 October 2026 (Tom's local date). Tom, 21:08: "lets say we have a single moon moving across the sky. nothing else.
we can see the front side of the moon and should use central sweep for that. the moon is moving, we should use the
inscribed sweep for that."; 21:10: "the inscribed sweep would encompass the entire wedge, the moon would just be a small
part of the inscribed sweep."; 21:12: "yes, I'm thinking that we can show the inscribed sweep detects ratios of moving
bodies, and the central sweep paints them." Geometry plus a clock; the predictions are written before any code.*

## Known beforehand

- MOT (`plans/mot-plan.md`, run 1): x/ẋ is time to contact at every distance (x a size over a distance); m/d =
  ωτ/√(1 + (ωτ)²), no bridge; the clock the only amount. Lee's τ.
- RSH run 4 (`plans/rsh-plan.md`): the inscribed reader's addresses are the sweep's own whatever is met; a body's share
  of them times π/2 is its solid angle (first numbers 0.09% and −0.13%); scaling the world repaints none of 4,194,304.
- RSH run 3, P7′(d): a body's seen share departs from the cap law by its relief; draw's OCC: from outside a reader sees
  part. `two-readers.html`, `room.html`: the central reader, directions given, the radius arriving, the shape over its
  geometric mean, the size unread.
- Classical: the union of the hemispheres seen from directions spanning an arc Δ (in one plane) covers (π + Δ)/(2π) of a
  sphere; an approaching body's solid angle grows as 1/d².

## Set-up

The moon: Levels body 3's waves (`bodyOf(3)`, every band in full), stretch (1, 1, 1), mean radius R̄ (about ½). The
reader at home O. The moon's centre moves in a straight line at constant velocity, from 40 units out in the direction
of azimuth ψ = 30°, altitude a = 25° (inside the wedge), at speed 1 a tick, its velocity 20° off straight toward O, in the
plane of that direction and the wedge's v axis; ticks t = 0, 1, … while its distance d > 12, each tick one sweep.

**The inscribed sweep** covers the whole wedge every tick: 4096 × 4096 addresses even in azimuth and height (equal
shares of the sweep, as RSH run 4), each read at its middle; an address is a detection when its ray meets the moon. Only
the cells near the moon are tested (those inside its bounding cone); every other cell is sky by construction. From the
detections alone: the share s(t) (detections × (π/2)/N, a solid angle), the patch's direction c(t) (the mean of its cells'
directions, normalised), ω(t) (the angle between c(t − 1) and c(t + 1), over 2 ticks), τ(t) = 2s/(ds/dt) by the central
difference (s ∝ d⁻², so 2s/ṡ = d/(−ḋ)), and the path's angle to the line of sight β = atan(ωτ).

**The central sweep** reads the moon about its own centre: 4,096 fixed directions u (a Fibonacci lattice), along each the
radius R(u) arriving, an amount, held for the directions whose surface point is seen from O that tick (the ray from O
meets no inside before it). Its painting is R(u) over the geometric mean of what it holds.

### Predictions

- **M1 (the detections are ratios).** Scaling the world by k = 10⁻³, 7, 10³ (the moon's size, its place and its speed
  together, the same ticks) leaves every tick's set of detections the same, but for at most 10⁻⁴ of the cells tested.
  *Killed* if more differ.
- **M2 (the motion read from the detections alone).** At every tick from the second to the last but one: τ(t) within 3% of
  the true d/(−ḋ); ω(t) within 1% of the true angular rate of the moon's centre seen from O; β(t) = atan(ωτ) within 2° of
  the true angle between the velocity and the line from the moon to O. *Killed* if any tick misses.
- **M3 (the painting is amounts, its size unread).** At every tick the painting R(u)/GM over the held directions equals the
  body's own R(u)/GM over the same directions to 10⁻¹² (an identity: the central reader receives the radius), and is the same
  at k = 10⁻³, 7, 10³ to 10⁻¹² while the radii themselves move by k. Over the pass the directions ever held cover a share F
  of the moon within 0.08 of (π + Δ)/(2π), Δ the angle between the first and the last directions from the moon's centre to
  O, and more than at any single tick. *Killed* if any part fails.
- **M4 (writing needs one amount).** With R̄ carried in (an amount the sweeps never read), d(t) = R̄·√(π/s(t)) is within 2% of
  the true distance at every tick, and the speed d·√(ω² + 1/τ²) within 3% of 1 a tick at every tick from the second to the
  last but one; without it, M1 says no reading moves when the world is scaled. *Killed* if either misses.

M1 and M3's identity are near identities (a kill would be my code); M2 is MOT's motion read from a patch of the inscribed
sweep; M3's coverage the classical lune, met by a body with relief; M4 the one amount that writes.

## What would and would not be shown

That a single moon is a small patch of the inscribed sweep, whose motion over addresses that stay put gives its track,
its time to contact and its path's angle, in ratios and ticks, never sizes; that the central sweep paints its face in
amounts of an unread unit, more of it as the moon crosses; and that one amount carried in writes distance and speed.
Not light, not a real moon, and not how the moon is told from the sky (a detection is given as met or not).

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (17 Oct, `node runs/mon/mon.mjs`): did not run

My set-up was impossible: the path's closest approach to O is 40·sin 20° ≈ 13.7, so "while d > 12" never ends and the
script stopped (by its own check) when the moon left the wedge, before any sweep. Nothing was measured.

### Run 2: the set-up corrected (written before it runs)

The same moon, path and sweeps, the ticks t = 0, 1, … while d > 15 (the approach, t = 0 to 31, d from 40 to about 15.3),
so τ is positive throughout. M1–M4 unchanged, thresholds and all.

### Run 2 (17 Oct, `node runs/mon/mon.mjs`; output `runs/mon/mon-run2.txt`, 9 min)

- **M1 not killed:** under k = 10⁻³, 7, 10³ no detection of 3,271,236 cells tested changes (32 ticks, 5,845 to 38,623
  addresses met).
- **M2 killed:** ω within 0.25% at every tick, but τ off by up to 9.2% and β by up to 2.4° (late in the pass, d 21 to 15:
  τ read 29.2 against 27.9 at t = 21, 34.6 against 32.3 at t = 30).
- **M3 not killed:** the painting is the body's own R/GM to 5·10⁻¹⁵, the same under k to 3·10⁻¹⁴ while the radii move by
  k; over the pass 0.576 of the moon held against (π + Δ)/(2π) = 0.623 (Δ = 44.3°), more than the 0.481 at any one tick.
- **M4 killed:** with R̄ carried in, the distance off by up to 5.5% and the speed by up to 8.0%.

**Post hoc** (`runs/mon/mon2-smooth.mjs`, output `runs/mon/mon2-smooth.txt`): the same pass with the relief taken off (R = ½):
τ within 1.2%, ω within 0.13%, β within 0.25°, the distance within 0.05%, the speed within 1.1%: all four of M2 and M4's
thresholds met. So the kills are the moon's relief: as the line of sight turns (44° over the pass) the moon shows another
profile, and its share of the sweep changes with the face it turns as well as with its distance. From detections alone
the inscribed sweep cannot tell approach from a turning profile (PAY's one stream: approach from growth); and the one
amount carried in must be the silhouette's breadth, not the mean radius (with relief they differ by up to 5.5% here).
The central sweep is what tells them apart: it paints the face that turns.

**Reading.** One moon is a small patch of the inscribed sweep. Its detections are ratios (nothing in them moves when the
world is scaled), and its motion over addresses that stay put gives its angular rate exactly, its time to contact and
path angle exactly for a round moon, and approximately for one with relief, whose turning profile the share mixes in.
The central sweep paints the face in amounts of an unread unit, more of it as the moon crosses (0.58 of it over a 44°
turn, 0.48 at once). Distance and speed need one amount carried in.
