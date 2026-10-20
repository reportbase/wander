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

### Run 1 (20 Oct; `runs/ber/ber.py`, output `runs/ber/ber-run1.txt`)

Data sha256 (archives from `thor.robots.ox.ac.uk/affine/`, not committed):
- bark f631c09a0f43fc1e092203f32f8f27e2e43e59b524918255d45474c50c91ea4f
- bikes 3b95c49accadfd71e63c2fa0f7602abcbadd87d7f53ff54eb1efb15210d19e0c
- boat 6e5721f37fbf9c3e974fd05935a42c1670f3e71aa3e5b218807ea046a068c603
- graf 999871b945ee968a00a0d5f9af957d1382fb9dae1511cdee9553366817b53b5b
- leuven 9b1ade6e64e5b27eee43463ff8f9ad2bd2f9c6911666e93de2634f3a5c0fe5dc
- trees 04a39f201bffbc5035a560136fb37d2b36ecaa1532113eebfb113c90b5327f5d
- ubc 26ab4ac94c8d0b2ded66c3bfaeb3f12589ec33005e5b4d5fcba4639f5b6e5414
- wall 3cb3df75f40471f093adf6647d13df6a9f4312f7a222fc591d03f6c08e086344

38,160 matches kept by the ratio test over the 24 pairs; median error 0.674 px.

- **B1 killed.** The slope of log P(|e| > x) over 2–32 px is −0.309, flatter than −0.5. It is the rival hypothesis's
  plateau:

  | range | slope |
  |---|---|
  | 0.5–2 px | −1.01 |
  | 2–8 px | −0.57 |
  | 8–32 px | −0.14 |
  | 32–256 px | −0.29 |

  5.1% of matches are off by more than 32 px and 2.7% by more than 256: wrong matches spread over the image, which the
  ratio test let through.
- **B2 not killed,** at its edge: the Cauchy's likelihood is higher in 6 of 8 sequences (graf, boat, bikes, trees,
  leuven, ubc); the normal is higher on wall and bark.
- **B3 not killed:** γ grows from (1, 2) to (1, 4) in 7 of 8 (not wall), and in order through (1, 3) in five.
- **B4 killed,** by B1.

Read after the run (post hoc, not tested):
- **B2 does not separate the Cauchy from the mixture.** The window ±8 px holds some wrong matches too, and a normal with
  no room for them loses to any heavy-tailed fit. A test that could tell them apart fits the Cauchy against a normal
  plus a flat floor. That would be run 2, with its own prediction.
- **The core.** Over 0.5–2 px the slope is −1.01, the Cauchy's. But the homographies are good to about a pixel, so that
  range mixes the keypoints' error with the ground truth's own. On this benchmark the core's shape cannot be read below
  a pixel or so.
- **The verdict, read past its letter.** On real images and a standard pipeline, a reading's error is a narrow core
  (γ 0.1–0.8 px, growing with difficulty) plus a few percent of wrong matches spread over the image. That is the
  mixture robust methods are built for. It is not a power tail across the range. So on this data, robust costs earn
  their place by the wrong matches, and the premise of item 1 fails here. It is not settled for far, low-parallax
  features, which these planar scenes do not have; there the error that matters is in depth, and it is heavy-tailed
  by the geometry alone (TRI), whatever the bearing's.
