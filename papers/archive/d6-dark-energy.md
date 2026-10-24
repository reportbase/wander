**Updated D6 — Dark Energy and Matter Fractions; Redshift Predictions**  
*(Status as of 23 September 2026)*

**Assumes:** Geometric Foundation (\(\psi_1\) projection rate, \(\psi_1\psi_2\) per observation). D16/D17 (Einstein equations, Friedmann cosmology as specialization).  
**Inputs:** None. No free parameters.  
**Derives:** \(\Omega_m = \psi_1\psi_2\); \(\Omega_\Lambda = 1 - \psi_1\psi_2\); \(\Omega_{\rm total} = 1\) (topological); \(w = -1\) (Schur / scale-invariance); \(z_{\rm eq} \approx 0.289\); \(z_{\rm acc} \approx 0.624\).

**The claim:** Matter and dark energy together partition the sphere. The inside observer’s projection rate gives matter; the arc residual gives dark energy. Both fractions are determined by the binding constant \(\psi_1\psi_2\) alone.

---

**The derivation.** The inside observer reads \(\psi_1 \times \psi_2 = \psi_1\psi_2\) of the sphere per observation. This is chord content — it interacts, clusters, and localizes. The arc residual:

\[
\boxed{\Omega_m = \psi_1\psi_2 \approx 31.83\%} \qquad \boxed{\Omega_\Lambda = 1 - \psi_1\psi_2 \approx 68.17\%}
\]

**The physical identification.** Matter is chord content: particles at definite positions, galaxy clusters at measured redshifts — projected, flat-representable, localizable quantities. Dark energy is arc content: isotropic, uniform, not associated with any specific direction or position. The arc is everywhere; the chord is at one point.

**Flatness is a topological identity.** The partition is complete by construction:

\[
\Omega_m + \Omega_\Lambda = \psi_1\psi_2 + (1 - \psi_1\psi_2) = 1.
\]

This holds at every scale, for every bounded observer on a closed arc. \(\Omega_{\rm total} = 1\) is not a consequence of inflation or a measured coincidence — it is the identity \(\psi_1\psi_2 + (1 - \psi_1\psi_2) = 1\).

**Equation of state.** The residual is isotropic — no preferred direction, forced by SO(3) symmetry of the boundary. By Schur’s lemma, the only isotropic, Lorentz-invariant symmetric 2-tensor is \(\Lambda g_{\mu\nu}\). Therefore \(p = -\rho\), \(w = -1\) exactly at the monopole (\(l=0\)) level. The same conclusion follows from the scale invariance of the projection rate \(\psi_1 = 2/\pi\) (Theorem F): a scale-invariant energy density has \(w = -1\) by definition.

---

**Redshift predictions — zero free parameters.**

Matter dilutes as \((1+z)^3\); dark energy is constant at \(w=-1\). Equality at \(z_{\rm eq}\):

\[
(1 + z_{\rm eq})^3 = \pi - 1 \implies z_{\rm eq} = (\pi - 1)^{1/3} - 1 = 0.2890.
\]

Acceleration onset occurs when \(\rho_m = 2\rho_\Lambda\) (the factor 2 from the spatial trace with 3 dimensions, \(-(1+3w)=2\)):

\[
(1 + z_{\rm acc})^3 = 2(\pi - 1) \implies z_{\rm acc} = (2(\pi - 1))^{1/3} - 1 = 0.6240.
\]

---

**Updated comparison table (23 September 2026)**

Observed values are taken from the most recent published combinations available as of this date. Uncertainties are approximate 68 % intervals; significances relative to the geometric prediction are computed under the assumption \(w=-1\) where relevant.

| Result           | Geometric prediction     | Planck PR4 / updates          | DESI DR2 BAO alone          | DESI DR2 + CMB              | DESI DR2 + CMB + SNe (range) |
|------------------|--------------------------|-------------------------------|-----------------------------|-----------------------------|------------------------------|
| \(\Omega_m\)     | \(1/\pi \approx 31.83\%\) | \(\approx 31.5\)–\(32.0\%\)   | \(29.75 \pm 0.86\%\)        | \(\approx 30.0\)–\(31.0\%\) | \(\approx 30.0\)–\(31.5\%\)  |
| \(\Omega_\Lambda\) | \((\pi-1)/\pi \approx 68.17\%\) | \(\approx 68.0\)–\(68.5\%\) | \(\approx 70.25\%\)         | \(\approx 69\)–\(70\%\)     | \(\approx 68.5\)–\(70\%\)    |
| \(\Omega_{\rm total}\) | 1 (exact)            | consistent with 1             | —                           | consistent with 1           | consistent with 1            |
| \(w\)            | \(-1\) (monopole exact)  | consistent with \(-1\)        | mild preference for evolution | \(3.1\sigma\) preference for \(w_0w_a\) | \(2.8\)–\(4.2\sigma\) preference (sample-dependent) |
| \(z_{\rm eq}\)   | **0.289**                | \(\approx 0.30\)              | higher                      | higher                      | higher                       |
| \(z_{\rm acc}\)  | **0.624**                | \(\approx 0.63\)              | higher                      | higher                      | higher                       |

Notes on the table:  
- DESI DR2 BAO alone yields \(\Omega_m = 0.2975 \pm 0.0086\).  
- A DESI DR2 Ly\(\alpha\) Alcock–Paczyński measurement gives \(\Omega_m = 0.325 \pm 0.018\) (closer to the geometric value).  
- Preference for dynamical dark energy (\(w_0 > -1\), \(w_a < 0\)) reaches \(3.1\sigma\) (DESI+CMB) and \(2.8\)–\(4.2\sigma\) once supernovae are added (Pantheon+, Union3, DESY5). Some later analyses with alternative redshift cuts or Bayesian evidence metrics find the preference weaker or dataset-dependent.  
- Planck-side numbers remain essentially unchanged from 2018/PR4 and continue to sit within \(\lesssim 0.5\sigma\) of the geometric prediction.

---

**Reading the tension (updated).**  
The framework predicts \(\Omega_m = \psi_1\psi_2 = 31.83\%\). Planck continues to agree at \(\lesssim 0.5\sigma\). DESI DR2 BAO prefers lower values (\(\approx 29.8\)–\(30.5\%\) in most combinations), producing a persistent \(1\)–\(2\sigma\) tension that propagates directly into \(z_{\rm eq}\) and \(z_{\rm acc}\). The tension is therefore of the same character and magnitude already noted in the April 2026 status, with no decisive worsening or resolution.

The more significant pressure remains the preference for \(w(z) \neq -1\). DESI DR2 + CMB + SNe combinations continue to favour dynamical dark energy at the \(3\sigma\) level in several analyses. As previously argued, this does not immediately refute the monopole derivation of \(w=-1\). Structure formation is the growth of the \(l=2\) quadrupole of the directional depth field \(\phi(x,\hat n)\). The partition identity \(\Omega_m + \Omega_\Lambda = 1\) must hold in every direction; an \(l=2\) anisotropy in the chord fraction therefore induces an equal-and-opposite \(l=2\) back-reaction on the arc residual. The monopole remains isotropic and forces \(w=-1\); the quadrupole supplies a calculable, late-time deviation \(w(z) \neq -1\) whose amplitude tracks the growth of structure. This is still the natural internal resolution offered by the framework.

**Status (23 September 2026).**  
- Geometric \(\Omega_m\) consistent with Planck at \(<0.5\sigma\); mild (\(1\)–\(2\sigma\)) tension with DESI DR2 BAO remains.  
- Exact monopole \(w=-1\) under continued pressure from DESI DR2 dynamical-dark-energy signals (\(2.8\)–\(4.2\sigma\) depending on supernova sample).  
- The \(l=2\) back-reaction calculation (open item M2) has not yet been completed. Until it is performed, the honest statement is unchanged: *exact \(w=-1\) at the monopole level; \(l=2\) structure-formation back-reaction remains the candidate mechanism for observed \(w(z)\) deviations; quantitative test still pending.*  
- DESI DR3 is expected \(\sim\)2027 and will provide the next decisive data set.

**Falsification conditions (unchanged in substance).**  
The ratio \(\Omega_m = \psi_1\psi_2\) is structural. Deviations are expected and are interpreted as local \(l=2\) anisotropy. The framework is falsified by:

(a) \(\Omega_m\) evolving with epoch in a pattern inconsistent with \(l=2\) structure-formation back-reaction;  
(b) \(w(z)\) evolution whose magnitude and redshift dependence cannot be accounted for by the \(l=2\) calculation once it is performed;  
(c) any detection that dark energy clusters.

None of these conditions has been met as of September 2026.

---

**The larger picture and open items remain as previously stated.**  
The derivation of \(\Omega_m = \psi_1\psi_2\) is the entry point. The larger program is reading the full geometry of the shared \(2\pi\) system from the inside. The three further directions listed earlier (Jacobian of position, CMB as coordinate singularity, \(\pi/2\) inter-observer rate) are still uncalculated. The conjecture D6-C1 on the coupling coefficient \(\alpha \approx 1/(\pi(\pi-1))\) likewise remains open and precisely testable against future DESI DR3 measurements of both \(w(z)\) and \(f\sigma_8(z)\).

The geometric numbers continue to organise the data; the tensions are real but of the same character already confronted; the internal resolution mechanism has not been ruled out.
