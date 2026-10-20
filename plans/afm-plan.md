# AFM: the address-first mapper against bundle adjustment

*19 October 2026 (Tom's local date), SPN R397.*

*`papers/mapping.md` §11 item 1, after MAP (item 0). Claude offered it at the end of MAP run 2; Tom (21:38 MDT): "ok".*

*A measurement, not a contest (`mapping.md` §1, SPN R387). Seeded; double precision (scipy). Scripts in `runs/afm/`.
Predictions written before the script.*

## Known beforehand

- **Bundle adjustment** minimizes the reprojection error over structure and poses (Triggs et al. 2000). With poses held
  fixed it is multi-view triangulation, and with a robust loss (Cauchy, Huber) it resists outliers (Hartley and
  Zisserman 2004, ch. 12; Huber 1981). **[classical]**
- **TRI.**
  - Bearings read from a height γ, tan δ ~ Cauchy(0, γ): the depth error is Cauchy too, and two standpoints' scales add.
  - Against normal errors of the same median the scale is √2 larger.
  - Rays not meeting ahead are a visible share.
- **STC run 1, P1 killed:** least squares on noisy bearing lines leaves a floor that more readings do not remove.
- **MAP:** with poses known the addresses alone pair points exactly; the payload pairs them at finite ε.
- **Robust statistics.** The median's breakdown point is ½. A median of pairwise quantities from K items, of which a
  share f is bad, is clean while (1 − f)² > ½, that is f < 1 − 1/√2 = 0.293 (the Hodges–Lehmann-type breakdown;
  Rousseeuw and Leroy 1987). **[classical]**

## The set-up

- **The room and the standpoints.**
  - MAP's room and its 80 features (no far ones), five seeded rooms.
  - K standpoints (K ∈ {4, 8, 16}), seeded inside [1.5, 3.5] × [1, 3] × [1, 2] m. Poses are known exactly, in |AB| (the
    first two standpoints' distance): structure only, the matching given. MAP showed the matching; this measures
    placing.
- **The readings.** Each standpoint reads each feature's direction, turned off the truth by an angle δ in a uniformly
  random direction:
  - **Cauchy:** tan δ = |C|, C ~ Cauchy(0, γ);
  - **normal:** δ = |N(0, σ)| with σ = γ/0.6745, the same median as the Cauchy;
  - γ = 10⁻³.
- **Outliers.** A share f of all readings is replaced by a direction uniform over the sphere: a wrong match.
- **The three mappers**, each given the same readings and poses:
  - **LS:** nonlinear least squares on the angular residuals (each ray's tangent-plane offset of the point over its
    distance), started from linear triangulation. This is bundle adjustment with the poses fixed.
  - **CB:** the same with Cauchy loss at scale γ (scipy `least_squares`, `loss='cauchy'`), started from LS.
  - **AF**, address-first: the coordinatewise median of the midpoints of closest approach of every pair of rays that
    meet ahead. If none meet ahead, the feature is reported as a direction.
- **The error.** |p̂ − p| over p's distance from the first standpoint. The figure of merit is the median over 80
  features × 5 rooms.

## Predictions

**F1 (Cauchy bearings, no outliers: least squares stalls).** Going from K = 4 to K = 16:
- LS's median error improves by less than a factor 1.5;
- CB's and AF's each improve by more than a factor 1.5.

*Killed* if any clause fails.

**F2 (normal bearings, no outliers: least squares is best).** At K = 8:
- LS's median error is at most 1.1 times CB's;
- AF's is more than 1.1 times LS's.

So the median costs efficiency where the errors are normal. *Killed* if either fails.

**F3 (outliers, Cauchy bearings, K = 8).**
- At f = 0.1, LS's median error is more than 10 times its own at f = 0.
- At f = 0.2, CB's and AF's are each within 3 times their own at f = 0.

*Killed* if any clause fails.

**F4 (AF's breakdown).** AF's breakdown point f* (the first f in steps of 0.05 at which its median error passes 10
times its f = 0 error, at K = 8) lies in [0.29, 0.60].
- Pairs of clean readings are a share (1 − f)², which falls below ½ at 0.293.
- Pairs that do not meet ahead are dropped, and those are mostly outlier pairs, so breakdown may come later than 0.293.

*Killed* if f* < 0.29 or f* > 0.60.

**F5 (cost).** At K = 16, AF takes more than 3 times LS's time per feature (its K(K − 1)/2 pairs against K rays).
Reported, with CB's.

**F6 (the verdict).** A judgment. *Killed* if F1, F2 or F3 is killed.
- Under the bearings' own heavy-tailed law, the address-first estimator keeps improving where least squares stalls.
- It survives wrong matches up to about the pairwise median's breakdown.
- It is less efficient under normal errors.
- A robust cost (CB) does as well or better without the pairwise cost.
- So the address-first mapper is one robust estimator among known ones, with its error law and breakdown predicted from
  the geometry: an alternative, measured, not a winner.

## What would and would not be shown

**Shown:** structure with poses known, against least squares and a Cauchy-cost bundle adjustment, on one synthetic room
family.

**Not shown:**
- poses estimated jointly;
- real images;
- far features;
- the ratio forms' exactness over a whole map (§11 item 3).

## Runs

(Nothing above this line is edited after a run.)

### Run 1 (19 Oct; `runs/afm/afm.py`, output `runs/afm/afm-run1.txt`)

- **F1 not killed.** Under Cauchy bearings, median relative errors at K = 4, 8 and 16:

  | | K = 4 | K = 8 | K = 16 | factor from K = 4 to 16 |
  |---|---|---|---|---|
  | LS | 3.35·10⁻³ | 2.55·10⁻³ | 2.41·10⁻³ | 1.39 (stalls, STC's floor) |
  | CB | 1.98·10⁻³ | 0.95·10⁻³ | 0.59·10⁻³ | 3.35 |
  | AF | 2.96·10⁻³ | 1.23·10⁻³ | 0.75·10⁻³ | 3.95 |

  AF improves fastest, and CB stays the most accurate.
- **F2 killed.**
  - Under normal bearings of the same median at K = 8: LS 9.13·10⁻⁴, CB 8.65·10⁻⁴, AF 9.65·10⁻⁴.
  - The first clause holds: LS is within 1.06 of CB.
  - The kill is AF: only 1.06 times LS, against my "more than 1.1". The median of pairwise crossings loses only 6% to least
    squares even where least squares is the right estimator. I expected it to cost more.
- **F3 killed, narrowly, in its LS clause.**
  - LS at f = 0.1 is 9.97 times its clean error, against "more than 10". It reaches 41 times at 0.15.
  - At f = 0.2, CB is 1.60 times and AF 1.58 times their clean errors; both hold.
- **F4 not killed.** AF's breakdown is f* = 0.45.
  - That is later than the all-pairs bound of 0.293, since pairs not meeting ahead are dropped.
  - CB gives way first: 4.7 times at 0.35, 36 times at 0.40, 354 times at 0.45. AF is 3.3, 5.1 and 17 times there.
- **F5 killed.** At K = 16, AF takes 0.96 ms a feature, against 2.11 for LS and 4.53 for CB.
  - Its 120 closed-form crossings and a median cost less than an iterative solver's evaluations. I had counted pairs
    against rays and forgotten the iterations.
- **F6 killed in its letter**, by F2 and F3.

The verdict, read past the letter, as a measurement:
- Under the bearings' own heavy-tailed law, least squares stalls.
  - The Cauchy-cost bundle adjustment is the most accurate when clean.
  - The address-first median improves fastest, and survives the most wrong matches: 0.45 against 0.35–0.40.
- Under normal errors, the address-first median costs only 6%.
- With poses fixed it is also the cheapest of the three.
- It is a robust estimator among known ones, close to the best and simpler, not a winner. Joint poses, far features
  and real images remain.

### Before run 2: the poses not given (19 Oct, written before run 2's script)

Tom (after run 1's explanation, which named the untested cases: "not knowing where you stood …, things very far away,
real photographs"): "test it". Run 2 takes the first: the poses estimated jointly. Far features enter only as the source
of the turn. Real photographs need a dataset, and are not this run.

**The set-up.**
- Run 1's rooms, with K = 8 standpoints and the 6 far features (10⁶ m) added.
- Every standpoint is turned by a seeded rotation. Nothing is given but the readings and which feature each is.
- The gauge: standpoint 1 at the origin in its own frame, |AB| = 1.
- Cauchy bearings, γ = 10⁻³; outliers f ∈ {0, 0.1, 0.2, 0.3}, as in run 1.

**The address-first pipeline (AF2), every stage a median of pairwise quantities:**
1. **The turn of each standpoint from standpoint 1.** Each pair of far features gives one rotation by the triad method
   (two direction pairs fix it). Take the coordinatewise median of the 15 rotations as quaternions, signs aligned, then
   normalize.
2. **The direction of each step from standpoint 1.**
   - With the turn known, each room feature gives a normal n = u₁ × R·u_k, which is perpendicular to the step.
   - Each pair of normals gives a candidate step direction, n × n′.
   - Take the median of the candidates, signs aligned, normalized.
   - The overall sign is the one that puts most features in front.
3. **The scale of each step after the first.** Each feature, placed from standpoints 1 and 2, gives the step length s
   along the step direction at which standpoint k's ray passes closest. Take the median.
4. **The places.** Run 1's AF (the median of pairwise crossings), with the poses from steps 1–3.

**Bundle adjustment.** All poses (the six numbers of each, standpoint 2's length held at 1) and all 86 points.
- **BA-LS:** least squares.
- **BA-CB:** Cauchy loss at γ.
- Both start from AF2's answer. That is generous to them, since bundle adjustment needs a starting point and AF2
  needs none.

**Predictions.**
- **G1 (clean, f = 0).**
  - AF2's median point error is within 3 times run 1's AF with poses given (1.23·10⁻³ at K = 8).
  - BA-CB from it is at most AF2's.
  - BA-LS is worse than BA-CB.
- **G2 (the weakest link, from theory).**
  - A rotation from a pair of far features is clean only if all four of its readings are, (1 − f)⁴, which falls below ½
    at f = 1 − 2^(−1/4) = 0.159.
  - So AF2's median error stays within 3 times its clean value at f = 0.1, and passes 10 times at f = 0.2.
- **G3.** At f = 0.1, BA-LS passes 10 times its clean error.
- **G4.** At f = 0.1, BA-CB started from AF2 stays within 3 times its clean error.
- **G5 (the verdict).** A judgment. *Killed* if G1 or G2 is killed.
  - With poses unknown, the address-first pipeline still works.
  - Its breakdown is set by its weakest median, the rotation from far features, and the share of clean pairs predicts it.
  - Bundle adjustment with a robust cost refines it.

*Each killed if its clauses fail.*

### Run 2 (19 Oct; `runs/afm/afm2.py`, output `runs/afm/afm-run2.txt`)

Median relative error of the room's 80 features over five rooms, and AF2's worst turn error:

| f | AF2 | BA-LS | BA-CB | AF2's turn, worst (median) |
|---|---|---|---|---|
| 0 | 8.71·10⁻³ | 7.21·10⁻³ | 1.82·10⁻³ | 2.44° (0.74°) |
| 0.1 | 2.04·10⁻² (2.3×) | 1.80·10⁻¹ (25×) | 1.42·10⁻² (7.8×) | 129° (18°) |
| 0.2 | 0.60 (69×) | 0.56 (78×) | 0.73 (403×) | 178° (110°) |
| 0.3 | 0.75 (86×) | 0.67 (93×) | 0.76 (416×) | 148° (96°) |

- **G1 killed.**
  - AF2's clean error is 8.7·10⁻³, against my bound of 3 times run 1's 1.23·10⁻³ (3.7·10⁻³).
  - The other two clauses hold: BA-CB from AF2 refines it to 1.8·10⁻³ (better than run 1's poses-given AF), and BA-LS is
    worse than BA-CB.
  - The turn is the cause: up to 2.4° off even when clean.
  - Post hoc (`runs/afm/afm2-posthoc.py`): my six far features lie through one window, 1.5° to 26° apart (median 11–18°).
    A pair's turn is off by about γ/sin(angle), four to forty times γ, and the Cauchy tails reach the median of 15 such
    pairs.
- **G2 not killed.** At f = 0.1, 2.3×; at f = 0.2, 69×. The breakdown came between the two, as the share of clean pairs,
  (1 − f)⁴, predicted.
- **G3 not killed.** BA-LS at f = 0.1 is 25×.
- **G4 killed.**
  - BA-CB at f = 0.1 is 7.8×, not within 3×.
  - Started from AF2, it inherits AF2's wrong turns in the rooms where they had already gone (a median room 18° off). A
    robust cost refines a good start; it cannot rescue a wrong one.
  - At f ≥ 0.2 BA-CB is worse than AF2 itself.
- **G5 killed in its letter**, by G1.

Read past the letter:
- With the poses unknown, the address-first pipeline is held back by its first stage: the turn from far features.
- That turn was badly conditioned here, because the far features sat in one narrow window, and it broke where the share
  of clean pairs said it would.
- Started from the pipeline's answer, the Cauchy-cost bundle adjustment gives the most accurate map when clean, 1.8·10⁻³.
  With wrong matches it is only as good as its start.
- What the address-first pipeline lacks against the usual one is a robust way to the turn.
  - Candidates: more far features, or features spread wider.
  - Or the rotation read from room features through the essential matrix, with a median over minimal sets (as RANSAC does
    with a vote).
  - A third route: the turn read in ratio forms from the vanishing points of the room's own edges.
