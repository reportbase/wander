# BER: are real bearing errors heavy-tailed?

*20 October 2026 (Tom's local date), SPN R400.*

*Tom (05:11 MDT) asked "why are existing methods better", then "what would a cauchy based system need to make it competitive".
Claude's answer listed seven needs, item 1 first: the case for a Cauchy-based mapper exists only if real reading errors
have heavy tails. Tom (05:22): "but  cauchy is passive so". That narrows the rivals to passive mappers (cameras), not active
ranging. Tom (05:27) then said "ok" to running item 1.*

*Real data. Scripts in `runs/ber/`. Predictions written before the script.*

## Why

AFM's runs assumed Cauchy bearing errors, tan δ ~ Cauchy(0, γ), as TRI did. Under normal errors least squares is optimal
by theorem, and AFM run 1 found the address-first median within 6% of it but never ahead. So the competitive case for a
Cauchy-based passive mapper rests on a measurement: do real readings of direction have tails that fall as a power, or do
they fall like a Gaussian with a few gross mismatches on top?

## Known beforehand

- **Robust costs in vision.** Bundle adjustment uses Huber and Cauchy losses because real matches include outliers
  (Triggs et al. 2000; Hartley and Zisserman 2003). That is evidence of outliers. It says nothing about whether the
  errors of correct matches have a power tail.
- **Keypoint error in this benchmark.** The benchmark's homographies are given as accurate to about a pixel or better
  (Mikolajczyk et al. 2005). Localization of SIFT keypoints is usually quoted as subpixel for correct matches.
- **Ratio test.** Lowe's 0.8 ratio test removes most wrong matches (Lowe 2004), not all.
- **The rival hypothesis.** A mixture: a thin core (normal, about a pixel wide) plus wrong matches spread over the image.
  Its survival function falls fast through the core, then lies nearly flat until the image's size.
- **This corpus.** TRI and AFM assume the Cauchy. LOM found that a ratio of normal amounts behaves as a Cauchy near zero
  (classical: Geary). None measured real errors.

## The data

The Oxford affine-covariant regions benchmark (Mikolajczyk et al. 2005, "A comparison of affine region detectors",
IJCV 65), from `thor.robots.ox.ac.uk/affine/`. It has eight sequences of six images each:
- viewpoint: graf, wall;
- zoom and rotation: boat, bark;
- blur: bikes, trees;
- light: leuven;
- JPEG: ubc.

Each pair (1, k) has a ground-truth homography H1to{k}p. The scenes are planar or nearly so. It is free for research use,
as the page states; the archives are not committed, and their sha256s are recorded under the runs.

## The measurement

- **Matching.** SIFT keypoints (OpenCV 5.0, default settings) in image 1 and image k. Each keypoint of image 1 is matched
  to its nearest neighbour in image k by descriptor, and kept if it passes Lowe's ratio test at 0.8.
- **The error.** For each kept match, the error is e = H·x₁ − x₂ in pixels. Its signed components are e_x and e_y, and
  |e| is its length.
- **Pixels for angles.** A pixel error is a bearing error divided by the focal length, which is unknown here. A fixed
  factor moves no tail exponent and no comparison of fits, so everything is in pixels.
- **Pairs.** The pairs (1, 2), (1, 3) and (1, 4), the three easiest of each sequence: 24 pairs.

## Predictions

The theory used so far (TRI, AFM) takes the bearing error as Cauchy. Each prediction states that and what would kill it.

**B1 (the tail is a power, not a plateau).**
- Pool every kept match of the 24 pairs.
- The slope of log P(|e| > x) against log x, fitted over 2 ≤ x ≤ 32 px, lies between −2 and −0.5. The 2D isotropic
  Cauchy's is −1.
- *Killed* if it is steeper than −2 (a thin tail) or flatter than −0.5 (a plateau of wrong matches).

**B2 (Cauchy beats normal on the components).**
- On the signed components e_x and e_y within |e_x|, |e_y| ≤ 8 px, pooled per sequence over its three pairs.
- Fit a Cauchy and a normal, each with its own location and scale, by maximum likelihood truncated to the window.
- The Cauchy's log-likelihood is higher in at least 6 of the 8 sequences.
- *Killed* if fewer than 6.

**B3 (harder pairs, wider spread).**
- The fitted Cauchy scale γ (from B2's fit, per pair) grows from (1, 2) to (1, 4) in at least 6 of the 8 sequences.
- *Killed* if fewer than 6.

**B4 (the verdict).** A judgment. *Killed* if B1 or B2 is killed.
- If neither is killed, the premise of a Cauchy-based passive mapper holds on this data: real bearing errors from a
  standard pipeline have a power tail, and robust estimators are not only for outliers.
- If either is killed, the premise fails here: the errors are a thin core plus wrong matches, and least squares with
  outlier rejection is the right tool for this regime.

## What would and would not be shown

**Shown:** the shape of real keypoint errors, correct and wrong matches together, in a standard pipeline on a standard
benchmark.

**Not shown:**
- far, low-parallax features: these scenes are planar and have no depth. The regime where passivity matters most needs a
  dataset with 3D ground truth (ETH3D, KITTI), which is the next run if this one stands;
- errors in depth, only in the readings;
- other detectors, or learned features.

## Runs

(Nothing above this line is edited after a run.)
