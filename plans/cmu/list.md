# Thirty occurrences of the Cauchy law and its kin, written from memory by a fresh agent on 25 November 2026 (no web searches; sources from memory, unchecked).

1. **Kuramoto model with Lorentzian natural frequencies** (nonlinear dynamics, biology)
- Variable that is Cauchy-type: the natural frequencies ω_i of the coupled oscillators.
- How it arises (the mechanism, 1–2 sentences): the frequencies are assumed drawn from g(ω) = (γ/π)/((ω − ω₀)² + γ²); with this choice the self-consistency equation for the order parameter can be solved in closed form.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Kuramoto chose the Lorentzian because it makes the mean-field problem exactly solvable. The critical coupling is K_c = 2γ, and above it the order parameter grows as r = √(1 − K_c/K). It is presented as the canonical solvable case of the synchronization transition.
- A source that account can be found in (author, title, year; from memory is fine, say so): Y. Kuramoto, *Chemical Oscillations, Waves, and Turbulence*, 1984; also S. H. Strogatz, "From Kuramoto to Crawford", Physica D, 2000 (from memory).

2. **Ott–Antonsen ansatz** (nonlinear dynamics)
- Variable that is Cauchy-type: the oscillator phases θ at fixed frequency, distributed as a Poisson kernel (wrapped Cauchy) on the circle.
- How it arises (the mechanism, 1–2 sentences): the continuum Kuramoto equation admits an invariant manifold on which the Fourier coefficients of the phase density are powers of one complex number α; the density on that manifold is the Poisson kernel.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Ott and Antonsen showed that the infinite-dimensional dynamics reduce exactly to a low-dimensional ODE for the order parameter on this manifold. Combined with Lorentzian frequencies the reduction gives a single complex ODE for the macroscopic order parameter, and it is used to analyse chimeras, driven ensembles and networks of phase oscillators.
- A source that account can be found in: E. Ott and T. M. Antonsen, "Low dimensional behavior of large systems of globally coupled oscillators", Chaos, 2008 (from memory).

3. **Exact firing-rate equations for quadratic integrate-and-fire neurons** (computational neuroscience)
- Variable that is Cauchy-type: the neurons' excitabilities (input currents) η_i, and the resulting membrane potentials across the population.
- How it arises (the mechanism, 1–2 sentences): with Lorentzian-distributed excitabilities, the population density of membrane voltages stays Lorentzian at all times (the "Lorentzian ansatz"), its centre and width giving the mean voltage and the firing rate.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Montbrió, Pazó and Roxin derived an exact two-variable mean-field model (firing rate r and mean voltage v) for an infinite QIF network. The width of the voltage Lorentzian equals π times the firing rate. It is described as a next-generation neural mass model bridging spiking networks and rate models.
- A source that account can be found in: E. Montbrió, D. Pazó and A. Roxin, "Macroscopic description for networks of spiking neurons", Physical Review X, 2015 (from memory).

4. **Turning angles in animal movement models** (movement ecology)
- Variable that is Cauchy-type: the turning angle between successive steps of a tracked animal, modelled as wrapped Cauchy.
- How it arises (the mechanism, 1–2 sentences): in correlated random walk and hidden Markov movement models the change of heading per step is given a concentrated circular distribution centred on zero, and the wrapped Cauchy is a standard choice alongside the von Mises.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Each behavioural state (e.g. foraging, travelling) gets its own step-length distribution and a wrapped Cauchy turning-angle distribution with its own concentration. High concentration means directed travel; low concentration means tortuous, area-restricted search. Parameters are fitted by maximum likelihood with the forward algorithm.
- A source that account can be found in: T. Michelot, R. Langrock and T. A. Patterson, "moveHMM: an R package for the statistical modelling of animal movement data using hidden Markov models", Methods in Ecology and Evolution, 2016 (from memory).

5. **Stress from random earthquake dislocations** (seismology)
- Variable that is Cauchy-type: components of the tectonic stress tensor at a point, produced by many randomly placed and oriented earthquake dislocations.
- How it arises (the mechanism, 1–2 sentences): the stress of a dislocation falls off as 1/r³ in three dimensions, and summing such contributions from sources scattered uniformly in space gives a stable law of index 1.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Kagan argued that the stress tensor in the seismogenic crust follows the Cauchy distribution, by analogy with the Holtsmark problem. This heavy-tailed stress explains the broad distribution of rotations between focal mechanisms of nearby earthquakes, which is modelled with a rotational Cauchy distribution.
- A source that account can be found in: Y. Y. Kagan, "Distribution of incremental static stress caused by earthquakes", Nonlinear Processes in Geophysics, 1994; Kagan, "Correlations of earthquake focal mechanisms", Geophys. J. Int., 1992 (from memory).

6. **Earth's free-oscillation spectral peaks** (global seismology)
- Variable that is Cauchy-type: the spectral amplitude of a normal mode as a function of frequency near its eigenfrequency.
- How it arises (the mechanism, 1–2 sentences): each mode excited by a large earthquake rings down exponentially because of anelastic attenuation, and the Fourier transform of a decaying sinusoid is a Lorentzian.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Multiplets are fitted as resonance peaks whose centre is the eigenfrequency and whose width gives the mode quality factor Q = ω/(2γ). Measured Q values across modes constrain the attenuation structure of mantle and core.
- A source that account can be found in: F. A. Dahlen and J. Tromp, *Theoretical Global Seismology*, 1998 (from memory).

7. **The Chandler wobble resonance** (geodesy)
- Variable that is Cauchy-type: the power spectral density of polar motion near the Chandler frequency (about 433 days).
- How it arises (the mechanism, 1–2 sentences): the Chandler wobble is a damped free nutation of the Earth driven by random atmospheric and oceanic excitation, so its spectrum is that of a damped harmonic oscillator, Lorentzian near the peak.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The period and quality factor Q of the wobble are estimated by fitting the resonance in the polar-motion spectrum. Q is commonly quoted in the range of roughly 50 to 200, constraining mantle anelasticity at long periods.
- A source that account can be found in: W. H. Munk and G. J. F. MacDonald, *The Rotation of the Earth*, 1960; K. Lambeck, *The Earth's Variable Rotation*, 1980 (from memory).

8. **Quasi-periodic oscillations in X-ray binaries** (high-energy astrophysics)
- Variable that is Cauchy-type: the Fourier power of the X-ray light curve as a function of frequency, around each QPO.
- How it arises (the mechanism, 1–2 sentences): the variability is decomposed into a sum of components each modelled as a Lorentzian, taken to represent exponentially damped oscillations (or shot noise for zero-centred ones).
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Power spectra of black-hole and neutron-star binaries are fitted with multiple Lorentzians, characterised by their characteristic frequency and coherence Q = ν₀/FWHM. Features with Q above about 2 are called QPOs, broader ones band-limited noise; correlations among the frequencies are used to test accretion-flow models.
- A source that account can be found in: T. Belloni, D. Psaltis and M. van der Klis, "A unified description of the timing features of accreting X-ray binaries", ApJ, 2002 (from memory).

9. **Damped random walk model of quasar variability** (optical astronomy)
- Variable that is Cauchy-type: the power spectral density of a quasar's optical light curve.
- How it arises (the mechanism, 1–2 sentences): the light curve is modelled as an Ornstein–Uhlenbeck (continuous autoregressive, CAR(1)) process, whose PSD is Lorentzian, flat below the inverse damping timescale and falling as f⁻² above it.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The damped random walk is described by a characteristic timescale τ and an amplitude, fitted to irregularly sampled survey photometry. The timescales of hundreds of days are related to black-hole mass and accretion-disc physics, and the model is used to select quasars and measure reverberation lags.
- A source that account can be found in: B. C. Kelly, J. Bechtold and A. Siemiginowska, "Are the variations in quasar optical flux driven by thermal fluctuations?", ApJ, 2009; C. L. MacLeod et al., ApJ, 2010 (from memory).

10. **FT-ICR and Orbitrap mass spectral peak shape** (analytical chemistry)
- Variable that is Cauchy-type: signal intensity versus frequency (and so versus m/z) of a peak in absorption-mode spectra.
- How it arises (the mechanism, 1–2 sentences): the image-current transient of each ion packet decays roughly exponentially through collisions and dephasing, and its Fourier transform is a Lorentzian.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The resolving power depends on the transient length and damping; for a fully damped signal the absorption-mode peak is Lorentzian and the magnitude-mode peak broader by about √3. Absorption-mode processing is promoted because it narrows the peaks and improves resolving power.
- A source that account can be found in: A. G. Marshall, C. L. Hendrickson and G. S. Jackson, "Fourier transform ion cyclotron resonance mass spectrometry: a primer", Mass Spectrometry Reviews, 1998 (from memory).

11. **Vibrational band shapes of molecules in liquids** (physical chemistry)
- Variable that is Cauchy-type: infrared absorbance versus wavenumber across a vibrational band.
- How it arises (the mechanism, 1–2 sentences): in the fast-modulation (motional narrowing) limit, the vibrational correlation function decays exponentially, so the band is Lorentzian with width set by the dephasing and population relaxation times.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Band shapes are interpreted through the Kubo stochastic lineshape theory, which interpolates between Gaussian (slow modulation) and Lorentzian (fast modulation) profiles. The Lorentzian width gives the homogeneous dephasing time T₂ via Γ = 1/(πcT₂).
- A source that account can be found in: R. Kubo, "A stochastic theory of line shape", in *Fluctuation, Relaxation and Resonance in Magnetic Systems*, 1962; W. G. Rothschild, *Dynamics of Molecular Liquids*, 1984 (from memory).

12. **Zero-phonon lines of single molecules at low temperature** (physical chemistry, solid-state spectroscopy)
- Variable that is Cauchy-type: fluorescence excitation intensity versus laser frequency for one molecule in a host crystal.
- How it arises (the mechanism, 1–2 sentences): at liquid-helium temperatures the purely electronic transition is homogeneously broadened by the excited-state lifetime and residual phonon dephasing, giving a Lorentzian line.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Single-molecule lines such as pentacene in p-terphenyl reach widths near the lifetime limit of tens of MHz. Linewidth versus temperature and laser power (saturation broadening) are used to study dephasing and spectral diffusion.
- A source that account can be found in: W. E. Moerner and L. Kador, "Optical detection and spectroscopy of single molecules in a solid", PRL, 1989; M. Orrit and J. Bernard, PRL, 1990 (from memory).

13. **Quartz crystal microbalance resonance** (sensor engineering, surface science)
- Variable that is Cauchy-type: the electrical conductance of the quartz resonator versus frequency near a harmonic.
- How it arises (the mechanism, 1–2 sentences): the crystal's thickness-shear mode behaves as a damped resonator (Butterworth–Van Dyke equivalent circuit), so the conductance peak is Lorentzian.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The resonance frequency shift gives adsorbed mass through the Sauerbrey equation, and the half-bandwidth Γ (or dissipation D = 2Γ/f) gives the viscoelastic losses of the adsorbed film. QCM-D instruments report both from fits or ring-down measurements.
- A source that account can be found in: D. Johannsmann, *The Quartz Crystal Microbalance in Soft Matter Research*, 2015 (from memory).

14. **Phase noise of electronic oscillators** (RF engineering)
- Variable that is Cauchy-type: the power spectrum of a free-running oscillator's output around its carrier.
- How it arises (the mechanism, 1–2 sentences): white noise drives a random walk (diffusion) of the oscillator phase, and a phase-diffusing sinusoid has a Lorentzian spectrum whose width is set by the diffusion constant.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Demir, Mehrotra and Roychowdhury showed that the true spectrum is Lorentzian near the carrier, removing the divergence of the 1/f² law of Leeson's model at small offsets. The single-sideband phase noise L(Δf) follows the Lorentzian's tail far from the carrier.
- A source that account can be found in: A. Demir, A. Mehrotra and J. Roychowdhury, "Phase noise in oscillators: a unifying theory and numerical methods for characterization", IEEE Trans. Circuits Syst. I, 2000 (from memory).

15. **Hanle effect** (atomic physics, spintronics)
- Variable that is Cauchy-type: the polarization of fluorescence (or spin signal) as a function of a transverse magnetic field.
- How it arises (the mechanism, 1–2 sentences): spins oriented by light precess in the field while decaying with lifetime τ, and averaging the precession over the exponential lifetime gives a Lorentzian dependence on Larmor frequency.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The width of the Hanle curve gives the product gτ, and is used to measure excited-state lifetimes in atoms and spin lifetimes in semiconductors and spin-injection devices. In non-local spin valves the Hanle curve is a broadened Lorentzian because of diffusion.
- A source that account can be found in: W. Hanle, Z. Phys., 1924; A. Corney, *Atomic and Laser Spectroscopy*, 1977 (from memory).

16. **Lamb dip in saturated absorption spectroscopy** (laser spectroscopy)
- Variable that is Cauchy-type: the depth of the narrow dip in absorption (or laser output) versus frequency at the centre of a Doppler-broadened line.
- How it arises (the mechanism, 1–2 sentences): counter-propagating beams interact with the same velocity class only near line centre, burning a hole whose shape is the homogeneous (Lorentzian) profile.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Saturated absorption resolves features hidden by the Doppler width, with a dip width set by the natural and power-broadened homogeneous linewidth. It is the basis of Doppler-free frequency standards and laser locking.
- A source that account can be found in: W. Demtröder, *Laser Spectroscopy*, (many editions, e.g. 2008); W. E. Lamb, "Theory of an optical maser", Phys. Rev., 1964 (from memory).

17. **Ferromagnetic resonance linewidth** (magnetism)
- Variable that is Cauchy-type: microwave absorption (imaginary susceptibility) versus applied field or frequency.
- How it arises (the mechanism, 1–2 sentences): the magnetization precesses according to the Landau–Lifshitz–Gilbert equation with damping α, giving a Lorentzian susceptibility near the Kittel resonance.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The field-swept linewidth ΔH grows linearly with frequency with slope proportional to the Gilbert damping α, plus a zero-frequency inhomogeneous offset. FMR linewidth is the standard measurement of damping in magnetic thin films for spintronics.
- A source that account can be found in: C. Kittel, "On the theory of ferromagnetic resonance absorption", Phys. Rev., 1948; D. D. Stancil and A. Prabhakar, *Spin Waves*, 2009 (from memory).

18. **Crystallite-size broadening of X-ray diffraction peaks** (crystallography, materials science)
- Variable that is Cauchy-type: diffracted intensity versus scattering angle 2θ in a powder pattern.
- How it arises (the mechanism, 1–2 sentences): finite crystallite sizes with a broad size distribution, and some strain distributions, give peak profiles close to Lorentzian; instruments add Gaussian parts.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Peaks are fitted with pseudo-Voigt or Voigt functions in Rietveld refinement, the Lorentzian part attributed mainly to size and the Gaussian to strain and instrument. The Scherrer equation and Williamson–Hall plots convert integral breadths into crystallite size and microstrain.
- A source that account can be found in: B. D. Cullity, *Elements of X-ray Diffraction*, 1956/1978; R. A. Young (ed.), *The Rietveld Method*, 1993 (from memory).

19. **Plasmon peak in electron energy-loss spectra** (electron microscopy, condensed matter)
- Variable that is Cauchy-type: the energy-loss function Im(−1/ε(ω)) versus energy loss near the bulk plasmon energy.
- How it arises (the mechanism, 1–2 sentences): with a Drude dielectric function the loss function is a Lorentzian-like peak at the plasmon energy whose width is set by the damping rate of the free-electron gas.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The plasmon peak position gives the valence-electron density and its width the plasmon lifetime. The ratio of plasmon to zero-loss intensity measures specimen thickness in units of the inelastic mean free path.
- A source that account can be found in: R. F. Egerton, *Electron Energy-Loss Spectroscopy in the Electron Microscope*, 1986/2011 (from memory).

20. **Instrumental-variables estimator with an irrelevant instrument** (econometrics)
- Variable that is Cauchy-type: the just-identified IV estimator of a structural coefficient when the instrument is uncorrelated with the regressor.
- How it arises (the mechanism, 1–2 sentences): the estimator is a ratio of the instrument's covariance with the outcome to its covariance with the regressor, both asymptotically normal with the denominator centred at zero.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Under weak or irrelevant instruments the IV estimator has no moments, heavy tails, and is centred at the OLS probability limit rather than the true value. This is used to explain the poor performance of IV with weak instruments and motivates first-stage F tests and weak-instrument-robust inference.
- A source that account can be found in: P. C. B. Phillips, "Partially identified econometric models", Econometric Theory, 1989; D. Staiger and J. H. Stock, "Instrumental variables regression with weak instruments", Econometrica, 1997 (from memory).

21. **Impulsive noise and the myriad filter** (signal processing)
- Variable that is Cauchy-type: the additive noise samples in impulsive channels (atmospheric, switching, underwater acoustic noise), modelled as symmetric α-stable with α = 1.
- How it arises (the mechanism, 1–2 sentences): noise made of many sporadic, heavy-tailed impulses is modelled by stable laws, and the Cauchy case gives a closed-form density for which the maximum-likelihood location estimate is the sample myriad.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Linear filters fail under such noise because it has infinite variance. The weighted myriad filter, the ML estimator under Cauchy noise with a tunable linearity parameter, ranges from the sample mean to a mode-like selector, and is used for robust filtering of images and communications signals.
- A source that account can be found in: C. L. Nikias and M. Shao, *Signal Processing with Alpha-Stable Distributions and Applications*, 1995; J. G. Gonzalez and G. R. Arce, "Optimality of the myriad filter in practical impulsive-noise environments", IEEE Trans. Signal Processing, 2001 (from memory).

22. **t-SNE's low-dimensional similarity kernel** (machine learning)
- Variable that is Cauchy-type: the similarity kernel between embedded points, q_ij ∝ (1 + ‖y_i − y_j‖²)⁻¹, a Student t with one degree of freedom.
- How it arises (the mechanism, 1–2 sentences): the embedding matches high-dimensional Gaussian neighbour probabilities to low-dimensional ones, and a heavy-tailed kernel is used in the low-dimensional space.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Van der Maaten and Hinton replaced SNE's Gaussian with a Cauchy kernel to relieve the "crowding problem", letting moderately distant points sit far apart in the map. The heavy tails make clusters well separated and the gradient cheap to compute.
- A source that account can be found in: L. van der Maaten and G. Hinton, "Visualizing data using t-SNE", JMLR, 2008 (from memory).

23. **Cauchy sketches for the L1 norm in data streams** (algorithms)
- Variable that is Cauchy-type: the random projection coefficients, and hence each sketch entry Σ_i a_i x_i.
- How it arises (the mechanism, 1–2 sentences): by 1-stability, a sum of Cauchy variables weighted by x_i is Cauchy with scale ‖x‖₁, so the L1 norm can be read from the median of the absolute sketch entries.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Indyk showed that p-stable random projections give small-space streaming estimators of Lp norms for 0 < p ≤ 2, the Cauchy giving the L1 case. The estimator uses the median because the Cauchy has no mean, and pseudorandom generators keep the memory polylogarithmic.
- A source that account can be found in: P. Indyk, "Stable distributions, pseudorandom generators, embeddings, and data stream computation", JACM, 2006 (from memory).

24. **Locality-sensitive hashing with p-stable distributions** (computing, nearest-neighbour search)
- Variable that is Cauchy-type: the entries of the random projection vector a in the hash h(x) = ⌊(a·x + b)/w⌋, for the L1 metric.
- How it arises (the mechanism, 1–2 sentences): with Cauchy entries, a·x − a·y is Cauchy with scale ‖x − y‖₁, so nearby points collide in the same bucket with higher probability.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Datar et al. gave LSH families for Lp distances using p-stable distributions, Gaussian for L2 and Cauchy for L1. The collision probability is computed in closed form as a function of distance and bucket width, giving sublinear-time approximate nearest-neighbour search.
- A source that account can be found in: M. Datar, N. Immorlica, P. Indyk and V. Mirrokni, "Locality-sensitive hashing scheme based on p-stable distributions", SoCG, 2004 (from memory).

25. **Fast simulated annealing (the Cauchy machine)** (optimisation)
- Variable that is Cauchy-type: the size of each proposed move in the state space.
- How it arises (the mechanism, 1–2 sentences): candidate states are drawn from a Cauchy distribution about the current state with a scale that shrinks as the temperature is lowered.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Szu and Hartley showed that with Cauchy moves the temperature can be lowered as T₀/k rather than the logarithmic schedule required for Gaussian moves, while keeping convergence. The occasional long jumps let the search escape local minima.
- A source that account can be found in: H. Szu and R. Hartley, "Fast simulated annealing", Physics Letters A, 1987 (from memory).

26. **Cauchy mutation in fast evolutionary programming** (evolutionary computation)
- Variable that is Cauchy-type: the mutation perturbation added to each component of a candidate solution.
- How it arises (the mechanism, 1–2 sentences): the Gaussian mutation of classical evolutionary programming is replaced by a Cauchy random variable scaled by self-adapted step sizes.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Yao, Liu and Lin found fast EP outperformed classical EP on multimodal benchmark functions with many local minima, attributing it to the higher probability of large jumps. On unimodal functions Gaussian mutation can be better at fine-tuning, which motivated mixed and adaptive schemes.
- A source that account can be found in: X. Yao, Y. Liu and G. Lin, "Evolutionary programming made faster", IEEE Trans. Evolutionary Computation, 1999 (from memory).

27. **Random Fourier features for the Laplacian kernel** (machine learning)
- Variable that is Cauchy-type: the random frequencies ω sampled to approximate the kernel k(x, y) = exp(−‖x − y‖₁/σ).
- How it arises (the mechanism, 1–2 sentences): by Bochner's theorem a shift-invariant kernel is the Fourier transform of a probability density, and the transform of exp(−|t|) is the Cauchy density, so frequencies are drawn from (products of) Cauchys.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Rahimi and Recht map inputs to cos(ω·x + b) features whose inner products approximate the kernel, turning kernel machines into fast linear models. The sampling distribution is listed per kernel: Gaussian for the RBF kernel, Cauchy for the Laplacian, Laplace for the Cauchy kernel.
- A source that account can be found in: A. Rahimi and B. Recht, "Random features for large-scale kernel machines", NIPS, 2007 (from memory).

28. **Cauchy proposals in random-walk Metropolis** (computational statistics)
- Variable that is Cauchy-type: the increment proposed at each step of a Metropolis–Hastings chain.
- How it arises (the mechanism, 1–2 sentences): heavy-tailed proposals are used instead of Gaussian ones so the chain can make occasional large jumps when sampling heavy-tailed or multimodal targets.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): Theory on geometric ergodicity shows Gaussian random-walk Metropolis fails to be geometrically ergodic for heavy-tailed targets, and heavy-tailed proposals can restore better convergence properties. Cauchy and t proposals are standard options in MCMC software and are compared through tuning and efficiency studies.
- A source that account can be found in: S. F. Jarner and G. O. Roberts, "Convergence of heavy-tailed Monte Carlo Markov chain algorithms", Scandinavian Journal of Statistics, 2007 (from memory).

29. **Dark resonances in coherent population trapping and EIT** (quantum optics)
- Variable that is Cauchy-type: transmission (or fluorescence reduction) versus two-photon (Raman) detuning near the dark resonance.
- How it arises (the mechanism, 1–2 sentences): in a Λ system two fields pump atoms into a dark superposition of ground states, and the narrow transparency window has a Lorentzian shape with width set by ground-state decoherence plus power broadening.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): The resonance can be far narrower than the optical natural linewidth, limited by ground-state coherence times. Its width grows linearly with light intensity, and it is used in chip-scale atomic clocks, magnetometers and slow-light experiments.
- A source that account can be found in: E. Arimondo, "Coherent population trapping in laser spectroscopy", Progress in Optics, 1996; M. Fleischhauer, A. Imamoglu and J. P. Marangos, Rev. Mod. Phys., 2005 (from memory).

30. **Brillouin scattering lines** (condensed matter, materials characterisation)
- Variable that is Cauchy-type: scattered light intensity versus frequency shift in each Brillouin doublet line.
- How it arises (the mechanism, 1–2 sentences): light scatters from thermally excited acoustic phonons whose amplitudes decay through sound attenuation, and the damped hydrodynamic modes give Lorentzian lines shifted by the sound frequency.
- How the standard account describes it (2–3 sentences, as textbooks or papers in that field usually do): In the hydrodynamic Rayleigh–Brillouin triplet, the shift of each Brillouin line gives the sound velocity and its width the sound attenuation (longitudinal viscosity). Brillouin spectroscopy and microscopy use the shift and linewidth to measure elastic moduli and viscous losses in liquids, glasses and biological tissue.
- A source that account can be found in: B. J. Berne and R. Pecora, *Dynamic Light Scattering*, 1976; J. P. Boon and S. Yip, *Molecular Hydrodynamics*, 1980 (from memory).
