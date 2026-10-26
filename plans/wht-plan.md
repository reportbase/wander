# WHT: whitening is drawing V = H

26 Oct 2026. Tom: "so whitening is setting V = H", "that actually, in strange kind of way, significantly strengthens our
argument. we are just identifying what they have been doing.", "empirical tests are needed to confirm the geometry", then
"do the whitening test". After CCA and FLR.

## The claim

Statistics standardizes (each variable over its own spread) or whitens (x ↦ Σ^(−1/2)x) before reading directions:
PCA on the correlation matrix, distances in Mahalanobis units, "scale your features first". In OFS's terms that is drawing
every party at one length, c = 1, V = H; skipping it is V = cH with c = σ_j/σ_i, the ratio of two variables' spreads. The
geometry then says where the known failures sit, from c alone, before looking:

- a ratio x_j/x_i of two centred variables is a direction; drawn at c ≠ 1 its median |x_j/x_i| moves from the corner (1)
  to c (for a normal pair exactly, Proposition 5(d) with V = cH: a Cauchy of scale c about the correlation's slope);
- standardizing puts it back on the corner; for a normal pair exactly, at every correlation, because standardized
  (z_i, z_j) is unchanged by swapping the two: the exchange, Theorem 6(e);
- an axis drawn c times longer than the others takes a direction-based method over: PCA's first component, nearest
  neighbours.

Known beforehand: all three failures are textbook (PCA on unscaled wine data is a standard example; "standardize before
k-NN"); the median of a ratio of normals (the Cauchy from Geary 1930, Marsaglia 1965). What is ours is the reading: one
number, c, places every failure, and the remedy is c = 1.

## Data

Real measurements, not ours, downloaded 26 Oct 2026, not committed:

- UCI Wine (Forina et al., 1991; Aeberhard, Coomans and de Vel 1992): 178 wines, 13 chemical features, 3 cultivars.
  `https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data`, sha256
  6be6b1203f3d51df0b553a70e57b8a723cd405683958204f96d23d7cd6aea659. CC BY 4.0 (UCI).
- UCI Breast Cancer Wisconsin (Diagnostic) (Street, Wolberg and Mangasarian 1993): 569 cases, 30 features, 2 classes.
  `https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data`, sha256
  d606af411f3e5be8a317a5a8b652b425aaf0ff38ca683d5327ffff94c3695f4a. CC BY 4.0 (UCI).

Only the shapes (178 × 13, 569 × 30) were looked at before these predictions; no spread, median or loading.

## Set-up

`runs/wht/wht.py` (numpy, scipy, mpmath), the data path as an argument. Each feature centred at its mean; σ its standard
deviation; for each pair i < j, c_ij = σ_j/σ_i; z = x/σ the standardized feature.

## Predictions (written before any script)

- **W0 (the theory, exact).** For a bivariate normal pair with spreads σ_i, σ_j and any correlation r, median
  |X_j/X_i| = σ_j/σ_i exactly, and for the standardized pair median |Z_j/Z_i| = 1 exactly, at every r. Checked by 40-digit
  quadrature of the ratio's law at r ∈ {−0.9, −0.5, 0, 0.3, 0.9} and c ∈ {10⁻³, 0.1, 1, 7, 10³}. Kill: any off by
  more than 10⁻²⁵.
- **W1 (raw ratios sit at c; standardized at the corner).** In both datasets, for every pair, median |x_j/x_i| equals
  c_ij × median |z_j/z_i| (an identity, to 10⁻¹²); the standardized medians sit near the corner, |log₂ median| ≤ 0.5 for
  at least 90% of pairs in each dataset; so the raw medians follow c: the correlation of log median |x_j/x_i| with
  log c_ij is at least 0.99 in each. Kill: fewer than 90% within, or a correlation below 0.99.
- **W2 (the long axes take PCA over).** Raw PCA (covariance): the first component's squared loadings on the features
  with σ ≥ σ_max/10 sum to at least 0.99, in each dataset. Standardized PCA (correlation): no feature's loading on the
  first component exceeds 0.5 in absolute value. Kill: either fails in either dataset.
- **W3 (the long axes take the neighbours over).** Leave-one-out 1-nearest-neighbour classification, Euclidean: raw
  accuracy within 0.05 of the accuracy using only the features with σ ≥ σ_max/10; standardized accuracy at least 0.10
  above raw. In each dataset. Kill: either fails in either.

## Not claimed

Nothing about any study's scaling choices (R364). The test is whether c alone places the failures and c = 1 removes them,
on real measurements.

## Runs

### Run 1 (26 Oct; `runs/wht/wht.py`, output `runs/wht/wht-run1.txt`, 1 s)

The first launch stopped in W0 before any result: mpmath's secant root-finder diverged from my starting point (a script
fault); the root is now bracketed (Illinois). Nothing else changed.

- **W0 not killed.** For 25 (r, c), median |X_j/X_i| = c, median |Z_j/Z_i| = 1 and P(|X_j/X_i| ≤ c) = ½ to 6·10⁻⁴²:
  standardizing puts a normal pair's ratio on the corner at every correlation.
- **W1 not killed.** Wine (78 pairs): spreads from 0.124 to 314; raw medians |x_j/x_i| from 0.0093 to 2,370;
  standardized medians 0.83 to 1.38, all 78 within a factor √2 of 1; corr(log raw median, log c) 0.99915. WDBC (435
  pairs): spreads 0.0026 to 569; raw medians 6·10⁻⁶ to 2.5·10⁵; standardized 0.68 to 1.56, 97.0% within √2;
  correlation 0.99951. The identity to 4·10⁻¹⁶ in both. On real measurements one number, c, places each pair's median, and
  c = 1 puts it near the corner.
- **W2 not killed.** Wine: one feature (proline) with σ ≥ σ_max/10, carrying 0.99965 of raw PC1 (99.8% of the variance);
  standardized, the largest loading 0.423. WDBC: two (the two areas), 0.99312 of raw PC1 (98.2%); standardized 0.261.
- **W3 killed**, in two clauses. Wine: raw 1-NN 0.770, proline alone 0.669 (0.10 apart, over my 0.05); standardized
  0.955 (+0.19, as predicted). WDBC: raw 0.916, the two areas alone 0.912 (as predicted); standardized 0.951 (+0.035,
  under my +0.10).

Post hoc (not a prediction): a nearest neighbour is decided by small differences, where what counts is each feature's
spacing between neighbouring points, not its global σ; in wine, proline's neighbours differ in it by little more than
magnesium's do, so the smaller axes still vote. c places what is read from the global drawing (directions, medians, the
first component) exactly; it does not place a local decision. WDBC's raw neighbours were already mostly right (0.916),
leaving standardizing little to gain.

## What WHT says

On real measurements (wine chemistry, cell nuclei), the ratio of two variables' spreads, c, places every pair's median
direction (correlation 0.999 in both datasets) and which axes take PCA over (99.97% and 99.3%); standardizing, c = 1,
puts the medians within √2 of the corner (100% and 97%) and no feature over 0.43 in the first component. For a normal pair
it is exact at every correlation: whitening draws V = H, and the corner returns by the exchange. Nearest neighbours were
not placed by c alone (W3 killed): a local decision reads local spacing, not the drawing.
