# FRD: a polarization angle's turn, read alone, against the full response

25 Nov 2026. SPN R1211. Tom: "Merge 506, then Faraday test", taking up Claude's proposal: *Reads and Writes* §2 uses
Faraday rotation as a payload recovered by its ratios; here the polarization angle χ = χ₀ + RM·λ² is the turn and the
polarized amplitude the payload, and the test is whether the angle read alone gives the same rotation measure as the
full complex response, as PHR asked of a resonance's phase.

## Data, recorded before any analysis

Anderson, Gaensler, Feain et al. 2016, "A study of broadband Faraday rotation and polarization behavior over 1.3–10 GHz
in 36 discrete radio sources", ApJ 825, 59; VizieR J/ApJ/825/59 (fetched through the CfA mirror
vizier.cfa.harvard.edu, the CDS host not answering here), VizieR licence. Table 6, "The spectropolarimetric data": per
channel, frequency and Stokes I, Q, U with uncertainties (V not used), 4,744 rows. Table 2, the sample's properties.
Downloaded 25 Nov 2026 as TSV (sha256 of these downloads, whose headers carry the fetch date: table6
a800d7fd916653de73c85d251de339a04f5058d24a9b4ee5d541931f674e99d3, table2
45fbe8f2300385b89e777711aa9899a93fbf301a5dfab7366ac02dfd18e6fe44); not committed. Seen before this record: the column
list and the first data row. The SPICE-RACS DR1 spectra (CSIRO, 10.25919/w37t-nw98) were the first choice; their files
could not be listed or fetched (Tom: "Data is no longer available").

Known beforehand: Anderson et al. found most of these sources Faraday-complex (their models with more than one
component preferred), so a single rotation measure is expected to fit only some.

## Method, fixed now

For each source, channels with |P| = |Q + iU| ≥ 3σ_P (σ_P the mean of e_Q and e_U) are kept; a source is analysed if it
keeps at least 20 channels.
- **The angle alone.** χ = ½·atan2(U, Q), unwrapped in order of λ² with period π; σ_χ = σ_P/(2|P|); a weighted straight
  line χ = χ₀ + RM_a·λ² gives RM_a, its error from the fit, and its χ²/dof.
- **The full response.** Q + iU = p(λ²)·exp(2i(χ₀ + RM_c·λ²)) with p a real quadratic in λ² (the payload: its amplitude
  and depolarization), fitted to Q and U together with their errors; RM_c, its error, its χ²/dof, started from RM_a and
  from the RM-synthesis peak over |RM| ≤ 2000 rad m⁻², the least cost kept.
- A source's one-component fit is **adequate** if the full fit's χ²/dof < 2.

## Predictions

- **F1.** Among adequate sources, |RM_a − RM_c| ≤ 3σ (σ the two errors in quadrature) on at least 90%.
- **F2.** Among adequate sources, the median |RM_a − RM_c|/σ is under 1.
- **F3.** Where the two part beyond 3σ, at least 80% of those sources are inadequate (the full fit χ²/dof ≥ 2): parting
  belongs to Faraday complexity, not to the angle's reading.
- **F4.** Among adequate sources, the angle's own line fits (its χ²/dof < 2) on at least 80%: within them the angle turns
  at one steady rate per unit λ².
- **F5 (the payload test).** Dividing Q and U by I (fractional polarization) changes every amplitude and leaves every
  angle: RM_a unchanged to 10⁻⁹ rad m⁻² with the weights held fixed, while RM_c moves on at least half the adequate sources
  by more than 10⁻⁶ rad m⁻² (a check that the full fit uses the payload and the angle does not).

If F1–F4 hold, Faraday rotation on these sources is a turn readable from the angle alone, its amount (RM, an amount in
rad m⁻², with λ carried in) set by the turn's rate; if F1 fails where fits are adequate, the angle read alone does not
carry the rotation measure. Classical (Burn 1966; Brentjens and de Bruyn 2005); what is tested is the separation.

## Runs
