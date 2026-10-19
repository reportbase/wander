# CFH: the central sweep earned from home: ranges, or silhouettes alone

*18 October 2026 (Tom's local date). Tom asked: "do we have both an inscribed and central sweep views of the moon and. it is
possible to have both?" Claude answered yes, and moon.html shows both. But MON's central painting is taken from the moon's
centre, a vantage the reader at home does not hold: from home only directions arrive. Claude offered a run that derives the
painting from what home actually receives, either ranges per address or silhouettes over the pass. Tom: "yes". Geometry
plus a clock, with one bridge named below. The predictions are written before any code.*

## Known beforehand

- **MON** (`plans/mon-plan.md`, run 2 and the smooth post hoc). The moon is a small patch of the inscribed sweep. Its
  detections are ratios: scaling the world changes none of them.
  - Relief mixes the turning profile into the share. From detections alone, approach cannot be told from turning: τ was
    off 9% and the distance 5.5%.
  - The central painting from the moon's centre is R/GM. It holds 0.48 of the moon at one tick and 0.58 over the pass, a
    44° turn of the line of sight.
- **R309.** Situations 3 and 4 are set by what is received: amounts along given directions (central), or directions alone
  (inscribed). A lidar or sonar is central.
- **R325** (`room-walk.html`). Far off, parallax takes the place of the central sweep. The shape needs a good share of the
  turn; the place needs only an angle above ε.
- **draw's labs.**
  - OCC: from outside, over 16 turns, a reader does not see a curled shape's pockets.
  - UDV: three standpoints crossing their lines give the figure up to its size; one length gives its size.
- **RSH runs 1 and 3** (`plans/rsh-plan.md`). Readers holding only directions place points they can name. Here no point is
  named, so silhouettes are all there is.
- **Classical.**
  - Radar and lidar ranging: the range is half the round-trip time times the signal's speed.
  - The visual hull (Laurentini 1994) is the intersection of the silhouette cones. It contains the body and loses every
    concavity that no silhouette touches.
  - Space carving (Kutulakos and Seitz 2000) and shape from silhouettes under known motion.
  - A least-squares sphere fit to a partial cap is biased by what is not seen.
- **The body** (a set-up fact, computed before any prediction). Body 3 has mean radius R̄ = 0.5007. Its relief is 8.6% rms
  of R̄; its radius runs from 0.73 R̄ to 1.22 R̄.

## Set-up

The moon, path, ticks and inscribed sweep are MON run 2's:

- Body 3, every band in full, its frame fixed (it does not spin).
- The path runs from 40 out at ψ = 30°, a = 25°, speed 1 a tick, 20° off straight toward home, for ticks t = 0 … 31.
- The sweep is 4096 × 4096 addresses even in azimuth and height over the whole wedge. An address is a detection when its
  ray meets the moon.

The truth (the referee's) is the body's R(u) about its centre, over MON's 4,096 lattice directions. Each painting is compared
on two sets:

- **held**: the directions seen from home at some tick (MON's visibility test);
- **rim**: the directions within 3° of square to the line from the centre to home at some tick.

A painting is the radius over its geometric mean on the set compared. Its error at a direction is the difference from the
true painting there.

**(A) Ranging.** Each detected address also carries its range ρ, the distance along its ray to the first surface point. ρ
is an amount, in the unit of the signal's speed times the clock. **That is the bridge: the signal's speed, carried in.**
The reader's point is ρ·d.

- **A1, centre given.** The reader is handed the true centre track c(t). Each point's direction from the centre is
  u = (ρd − c)/|ρd − c|, and its radius |ρd − c|.
- **A2, centre from the ranges.** At each tick the reader fits a sphere to its points by linear least squares (centre and
  radius). It then fits a straight line at constant speed to the 32 centres, its one assumption about the motion. The
  painting along MON's lattice is the radius of the ranged point nearest each direction, within 2° of it, from any tick.

**(B) Silhouettes alone.** No ranges. The visual hull in the moon's frame: a point x is kept when, at every tick, the ray
from home through c(t) + x lands in a detected address. R_hull(u) is found along each lattice direction u from the centre:
the first r at which x = r·u is not kept, marched outward in steps of 0.001, up to 3 R̄.

- **B1, track given.** The track c(t) is given. It is needed only up to scale, since the painting is R/GM; it is used in
  world units here.
- **B2, track from detections alone.** Each tick's direction is the patch's mean direction. Its distance is
  1/√(share), in a unit fixed by d(0) = 1, a ratio. A straight line at constant speed is fitted to those 32 points, in that
  unit.

### Predictions

- **C1 (ranging is the central reading carried home).** With the centre given (A1), every ranged point lies on the body:
  |ρd − c| = R(u) to 10⁻⁹ of R̄, at every detection and every tick. The directions u it reaches cover the held set: every
  held lattice direction has a ranged point within 2°. *Killed* if either fails.
- **C2 (the ranges are amounts and write).**
  - Scaling the world by k = 10⁻³, 7, 10³ moves every range by k to 10⁻¹². The A1 painting is unchanged to 10⁻⁹.
  - With the ranges, A2's fitted track gives the distance to within 1% and the speed to within 1% of 1 a tick, at every
    tick. No other amount is carried in: the ranges write, since the signal's speed is the amount.
  - *Killed* if any part fails.
- **C3 (centre from the ranges).**
  - A2's fitted centre is within 0.1 R̄ of the true centre at every tick.
  - Its painting on the held set is within 0.05 rms of the true painting, worst 0.12, and correlates with it at 0.8 or more.
  - *Killed* if any part fails.
- **C4 (silhouettes, track given: the hull).**
  - B1's hull contains the body: R_hull(u) ≥ R(u) − 0.02 R̄ on every lattice direction (the slack is about a cell at the
    nearest tick).
  - On the rim set it is tight: within 3% of R(u) for at least 80% of rim directions.
  - On held directions never on the rim, its median error is at least twice the rim set's. The face toward home is where
    concavities hide.
  - *Killed* if any part fails.
- **C5 (silhouettes from detections alone).** B2's hull painting correlates with the true painting at 0.5 or more on the rim
  set, and less than B1's. The track inherits MON's relief bias. *Killed* if either fails.
- **C6 (the hull is a ratio).** Scaling the world by k = 10⁻³, 7, 10³ leaves B2's painting the same to 10⁻⁹ (its
  detections do not move, MON's M1). *Killed* if it moves.

C1 and C6 are near identities; a kill there would be my code. C2 says ranging is writing, because its bridge (the signal's
speed) is an amount. C3 is the honest ranging case. C4 is Laurentini's hull read on the moon. C5 is the inscribed sweep
alone, end to end.

## What would and would not be shown

What a reader at home can have of the central sweep without standing at the moon:

- with a ranging signal, the face in amounts, and with it distance and speed, since the signal's speed is an amount
  carried in;
- with silhouettes alone, the face's outline swept by the turn, up to size, its concavities lost where no rim passed.

Not light, not noise in the ranges or the cells beyond their own size, not a spinning moon, and not a real radar.

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (18 Oct, `node runs/cfh/cfh.mjs`; output `runs/cfh/cfh-run1.txt`, 9 min)

Run 1 used MON run 2's 32 ticks (d from 40 down to 15.2). 2,359 of the 4,096 lattice directions are held at some tick
(0.576), 1,224 are on the rim at some tick, and 1,460 are held but never on the rim.

- **C1 killed.** Every one of 543,451 ranged points lies on the body, |ρd − c| = R(u) to 1.2·10⁻¹² of R̄. But 7 held
  directions have no ranged point within 2°.
  - On the other 2,352, A1's painting matches the true one: rms 0.0017, correlation 0.9998.
- **C2 not killed.**
  - Under k = 10⁻³, 7 and 10³ the detections are the same; the ranges move by k to 1.5·10⁻¹⁴ and A1's radii by k to
    3·10⁻¹³.
  - The ranges alone write the distance to within 0.25% and the speed to within 0.055%.
- **C3 not killed.**
  - The centre fitted from the ranges is within 0.082 R̄ of the true centre. Each tick's sphere fit is off by up to 0.085 R̄;
    the line over the 32 ticks takes little of that off.
  - The painting on 2,331 of 2,359 held directions: rms 0.043, worst 0.112, correlation 0.88.
- **C4 killed in one part.**
  - The hull contains the body: worst −0.014 R̄.
  - On held directions never on the rim, the median error is 0.161, against 0.014 on the rim. That is more than twice
    the rim's in both the relative radius and the painting (0.111 against 0.031).
  - But only 64.6% of rim directions are within 3%, against the 80% predicted.
  - The hull's painting correlates with the true painting at 0.87 on the rim and 0.16 on held directions never on the rim.
- **C5 not killed.**
  - From the detections alone the track's speed is 0.02478 d(0) a tick, against the true 0.02500.
  - The hull's painting correlates with the true painting at 0.57 on the rim (rms 0.076), below B1's 0.87.
  - Over all held directions it correlates at 0.03.
- **C6 not killed.** The detections-alone hull under k is the same to the last bit.

**Post hoc** (`runs/cfh/cfh1-posthoc.mjs`, output `runs/cfh/cfh1-posthoc.txt`).

- **C1.** The 7 uncovered directions have their nearest ranged point 2.02° to 2.42° away. They are not limb grazers: their
  largest cosine to home while held is 0.09 to 0.66. At the far ticks one address spans about 1.7° of the moon's directions
  about its centre, square on, and more on slopes. My 2° was at the address spacing: my threshold, not the reading.
- **C4.** The rim's error follows the size of one cell at the nearest tick where that direction was on the rim:

  | d at that tick | median error | one cell |
  |---|---|---|
  | 15–20 | 1.6% | 1.3% |
  | 20–25 | 0.2% | 1.7% |
  | 25–30 | 1.2% | 2.1% |
  | 30–35 | 2.8% | 2.5% |
  | 35–41 | 3.3% | 2.9% |

  53%, 66% and 75% of rim directions are within 1, 2 and 3 cells. My 3% took no account of the cell, which reaches 3% of
  R at the far ticks. Two more reasons:
  - The rim set is geometric (square to the line of sight). A body with relief has its true contour off that band.
  - A silhouette is tight only on the contour itself.

**Reading.**

- **Ranging carries the central sweep home.** With the centre given, ranging gives the moon's face exactly. With the centre
  fitted from the ranges, it gives the face to 4% rms (correlation 0.88), the error being the sphere fit's bias from a
  half-seen lumpy body.
- **The ranges write.** They give distance and speed to a quarter of a percent, because their bridge, the signal's speed,
  is an amount: ranging is writing.
- **Silhouettes alone give only the outline the turn swept,** and only up to size:
  - on the rim, the face to about a cell (correlation 0.87, or 0.57 with the track also read from the detections);
  - elsewhere, a hull that keeps none of the face's relief (correlation 0.16): the concavities no rim passed are lost, as
    Laurentini's hull says.
  - Nothing in it moves when the world is scaled.
- **The inscribed sweep alone does not earn the central painting.** It earns the rim's outline. The face needs an amount
  along each direction, from a ranging signal or from a vantage at the moon.
