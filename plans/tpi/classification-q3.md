# Q3: is the angle or phase that π comes from traversed, held as a set, or absent? (65 entries)

Input: `neutral-list.md` and `classification.md` (Q1 and Q2) only. Q3 asks about the physical situation the formula describes, not its derivation.

The three classes:
- (a) Traversed in order by a process: a rotation, an oscillation, a wave advancing in time, or a scan.
- (b) Present all at once as a set: a population, a static field, or a wave pattern held across positions.
- (c) Not traversed: an identity, a definition or a convention, or a π from a shape, a pole or a constant, with no direction or phase varied.

How the borderline cases were marked:
- **Directions present together, (b).** The π comes from averaging over directions that all exist at once, seen from a point or in a static field: Flamant (K15), the vortex (K8), the loaded circle (C31). The other reading, (c) "the shape of the half-plane or disc", is given as alt.
- **A spatial wave held across positions, (b).** The π is a wave's phase across a length or a period that is all present at once: the pixel (K6), the dipole current (K11), the gratings and bar targets (C24, C40, C41), and the air-gap MMF at an instant (C39). The alt is (c) "a sinusoid's shape on a given length" or (a) "when scanned or rotated".
- **A length or area of a shape, (c).** The π is the shape's own length or area, such as the arc's length πr, the spot's area, or ∫√(a² − x²) over a given width: C14, C23, K16, K17, C25, C27–C30, C32, C44.
- **A wavevector integral in a static or equilibrium problem, (c).** These are the lattice problems (C17, C18): the wavevector integral is a way of decomposing the problem, and nothing physical turns or oscillates.

| ID | name | Q3 (a/b/c) | justification (one line) | confidence |
|---|---|---|---|---|
| K1 | Half-Cauchy distribution function | c | As used (a law, a prior on a scale) no direction is varied; π is the normaliser. Alt (b): the lighthouse reading, flashes at random azimuths counted as a set. | medium |
| K2 | Buffon's needle | b | Many needle throws at random angles, counted as a set of crossings. | high |
| K3 | Viète's formula | c | Mathematical identity. | high |
| K4 | Arcsine law | c | Jeffreys's prior has no physical angle. In Lévy's law the walk runs in time, but its π comes from a Gamma or Stirling constant, not from a phase being traversed. | medium |
| K5 | Full-wave rectified sine average | a | The AC phase advances in time, and the meter averages over it. | high |
| K6 | Square pixel MTF at Nyquist | b | The pixel sums the pattern's phases across its width in one exposure. Alt (c): a sinusoid's shape on a given width. | low |
| K7 | Van Vleck relation | b | The angle is that of a correlated noise pair; the correlation is averaged over the set of samples. No phase advances, even though the samples come in time. | medium |
| K8 | KT universal jump | b | The phase winds 2π around a static vortex, in all directions from the core at once; the transition concerns a thermal population of vortex pairs. Alt (c): a constant, with the 2 a dimension count. | low |
| K9 | ARE median vs mean | c | The π is the Gaussian normalising constant; nothing in the sampling situation turns. | high |
| K10 | (E\|Z\|)²; one-bit quantiser loss | c | The π is the Gaussian normalising constant; no phase or direction is involved. | high |
| K11 | Half-wave dipole effective length | b | The standing-wave current along the dipole is present at once and summed along the wire. Alt (c): a half-cosine's shape on a given length. | low |
| K12 | Mean rim speed of a rolling wheel | a | The wheel's rotation phase advances in time. | high |
| K13 | 2D gas flux through a segment | b | A population of particles moving in all directions at once. | high |
| K14 | Jordan's inequality | c | Mathematical inequality. | high |
| K15 | Flamant line load | b | A static stress field, radial in every direction of the half-plane at once, summed to balance the load. Alt (c): the half-plane's shape. | low |
| K16 | Hertz line contact | c | The π is the area of the semi-elliptical pressure profile on a given width (a shape). | high |
| K17 | Wigner semicircle | c | The π is the area of the semicircular density on a given support (a shape). | medium |
| K18 | Sato–Tate density | b | Frobenius angles of many primes, counted as a set. The primes come in order, but the law is the set's. | medium |
| K19 | Equilibrium measure of an interval | c | Charge on a strip: the π is the arcsine density's shape on a given width. Alt (b): Chebyshev nodes, a set of equally spaced angles. | medium |
| K20 | Goemans–Williamson ratio | b | A random hyperplane direction drawn from an isotropic population; the guarantee averages over it, and over all edges at once. | medium |
| C1 | Wallis product | c | Mathematical identity. | high |
| C2 | Bauer–Ramanujan series | c | Mathematical identity. | high |
| C3 | Square-wave Fourier series | a | A periodic waveform whose phase advances in time. | high |
| C4 | Wilbraham–Gibbs overshoot | a | Ringing of a band-limited step or a truncated periodic wave, in time. | medium |
| C5 | Fourier sine/cosine transforms | c | A transform's definition; putting 2/π on one side is a convention. | high |
| C6 | Lebesgue constant, Chebyshev nodes | c | A mathematical property of an interpolation scheme with no physical situation; the angles only parametrise the nodes. Alt (b): the nodes as a set held at once. | low |
| C7 | Kac's real roots | c | The π is a Gaussian constant (Kac–Rice). Alt (b): Crofton's population of random great circles. | low |
| C8 | Alternating permutations | c | The pole of sec x + tan x. | high |
| C9 | Complete K and the AGM | c | Mathematical identity. | high |
| C10 | Struve H₁ → 2/π | c | A special function's limit, from Gamma constants. | high |
| C11 | Nesterov's π/2 theorem | b | A random direction drawn from an isotropic population for the rounding; the expectation is over that population. | medium |
| C12 | Krivine's bound / cut norm | b | The rounding by random directions (Grothendieck identity) averages over an isotropic population. Alt (c): read as a bound on a mathematical constant. | low |
| C13 | Kendall's τ | b | Pairs of observations counted as concordant or discordant as a set. | high |
| C14 | Centroid of a semicircular arc | c | The π is the arc's length πr; the moment ∫y ds = 2r² has none. | medium |
| C15 | Mean chord on a circle | b | Random pairs of points on the circle, averaged as a set. | high |
| C16 | Pendulum period | a | An oscillation whose phase advances in time (T₀ = 2π√(L/g)). | high |
| C17 | 2D Ising internal energy | c | Thermal equilibrium; the wavevector integral decomposes the exact solution, and nothing turns or oscillates. Alt (b): the lattice's modes all present at once. | medium |
| C18 | Infinite resistor grid | c | A DC network; the wavevector integral is the lattice Green's function, and no phase is physical. | medium |
| C19 | Excluded area of random sticks | b | A population of sticks with random orientations. | high |
| C20 | Stoner–Wohlfarth, in-plane | b | A population of particles with random in-plane easy axes. | high |
| C21 | Bell's linear local model | b | An ensemble of pairs, each with a random hidden direction λ. | high |
| C22 | Kramers–Kronig | c | The π is a half-residue at a pole (analyticity from causality). | high |
| C23 | Gaussian beam peak intensity | c | The π is the circular spot's area; the 2 is a convention. | medium |
| C24 | Binary phase grating | b | The grating's square-wave phase profile is illuminated across all periods at once. Alt (c): a profile's shape. | low |
| C25 | Disc capacitance | c | The π comes from the disc's arcsine charge density on a given radius (a shape). | high |
| C26 | Wheeler microstrip synthesis | c | The π comes from a conformal-map constant (the half-plane's iπ). | high |
| C27 | Baffled piston reactance | c | The π is the piston's area πa². | high |
| C28 | Penny-shaped crack | c | The π comes from the crack's elliptical opening, a constant of Sneddon's solution (a shape). | high |
| C29 | Sneddon conical indenter | c | The π comes from the arcsine integrals across the contact radius (a shape). | high |
| C30 | Oliver–Pharr ε for a cone | c | The same shape integrals as Sneddon's cone. | high |
| C31 | Uniformly loaded circle | b | Seen from the point, the loaded disc surrounds it in all directions at once (a full turn at the centre, chords at the edge). Alt (c): the circular load's shape. | low |
| C32 | Stress drop, long fault | c | The π is the mean of the elliptical slip profile across a given width (a shape). | high |
| C33 | Fibre orientation factor, 2D | b | A population of fibres with random in-plane angles. | high |
| C34 | Relay describing function | a | The input's sinusoidal phase advances in time through the relay. | high |
| C35 | Saturation describing function | a | The input's sinusoidal phase advances in time through the clipping. | high |
| C36 | Six-step inverter | a | The output waveform's electrical phase advances in time. | high |
| C37 | Switching mixer | a | The LO phase advances in time and switches the signal. | high |
| C38 | Class-B output stage | a | The signal's phase advances in time; supply current is averaged over it. | high |
| C39 | Air-gap MMF of a full-pitch coil | b | The MMF round the air gap at one instant is a spatial pattern present at once. Alt (a): the rotor's turn sweeps through it in a running machine. | low |
| C40 | Square- vs sine-grating threshold | b | A displayed spatial grating, all periods viewed at once. Alt (a): if drifted or scanned. | low |
| C41 | Coltman's relation | b | A bar target imaged all at once. Alt (a): a scanning microdensitometer or slit traversing it, as in older practice. | low |
| C42 | Canopy G-function, vertical leaves | b | A population of leaves with random azimuths. | high |
| C43 | Ideal-gas animal encounter | b | A population of animals with random headings; pairs are averaged over relative heading. | high |
| C44 | Rotational broadening (ε = 0) | c | The star rotates, but the π is the projected disc's area (chords 2√(1 − x²)), all seen at once; no phase is traversed. | medium |
| C45 | Fabry–Pérot linewidth | a | The round-trip phase advances as light propagates in the cavity, and the line is measured by scanning frequency or length. | medium |

## Counts

Q3: a 11, b 24, c 30.

Low confidence (12): K6, K8, K11, K15, C6, C7, C12, C24, C31, C39, C40, C41.
