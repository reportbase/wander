# DVF laws

1. **Malus's law**: I = I₀ cos²θᵢ (Polarizer)
2. **Malus's law with a Doppler-shifted frequency**: I = I₀ (f/f₀) [1 + λ(f₀ − f)/(2c)] cos²θᵢ (Polarizer)
3. **Equation of time, first-order form**: Δt_ey = −7.659 sin(D) + 9.863 sin(2D + 3.5932) (Equation of time)
4. **Eccentricity term, 365-day year**: a = −7.659 sin(6.24004077 + 0.01720197(365(y − 2000) + d)) (Equation of time)
5. **Obliquity term, 365-day year**: b = 9.863 sin(2(6.24004077 + 0.01720197(365(y − 2000) + d)) + 3.5932) (Equation of time)
6. **Mean anomaly from time since periapsis**: M = 2π(t − t_p)/t_Y (Equation of time)
7. **Kepler's equation**: M = E − e sin E (Equation of time)
8. **Eccentric anomaly, first order**: E ≈ M + e sin M (Equation of time)
9. **Eccentric anomaly, second order**: E ≈ M + e sin M + ½ e² sin 2M (Equation of time)
10. **True anomaly from eccentric anomaly**: ν = 2 arctan(√((1 + e)/(1 − e)) tan(E/2)) (Equation of time)
11. **Arctangent branch shift**: arctan x = arctan x + π (Equation of time)
12. **Branch point of the eccentric anomaly**: E = π (Equation of time)
13. **True anomaly from eccentric anomaly, series**: ν ≈ E + e sin E + ¼ e² sin 2E (Equation of time)
14. **Equation of the centre**: ν ≈ M + 2e sin M + (5/4) e² sin 2M (Equation of time)
15. **Ecliptic longitude of the Sun**: λ ≈ M + λ_p + 2e sin M + (5/4) e² sin 2M (Equation of time)
16. **Right ascension from ecliptic longitude**: α = arctan(cos ε tan λ) (Equation of time)
17. **Right ascension with branch**: α = arctan(cos ε tan λ + kπ) (Equation of time)
18. **Right ascension, implicit form**: α = λ − arcsin(y sin(α + λ)) (Equation of time)
19. **Obliquity parameter y**: y = tan²(ε/2) (Equation of time)
20. **Right ascension, iterated series**: α ≈ λ − y sin 2λ + ½ y² sin 4λ (Equation of time)
21. **Equation of time to first order in e and y**: Δt_ey = −2e sin M + y sin(2M + 2λ_p) = −7.659 sin M + 9.863 sin(2M + 3.5932) (Equation of time)
22. **Equation of time to second order**: Δt_e²y² = Δt_ey − (5/4) e² sin 2M + 4ey sin M cos(2M + 2λ_p) − ½ y² sin(4M + 4λ_p) (Equation of time)
23. **Mean anomaly from day count**: M = (2π/t_Y) n (Equation of time)
24. **Mean anomaly from a reference date**: M = M_D + (2π/t_Y) D (Equation of time)
25. **Mean anomaly at a full orbit**: M = 2π (Equation of time)
26. **Eccentricity term, 365.25-day year**: a = −7.659 sin(6.24004077 + 0.01720197(365.25(y − 2000) + d)) (Equation of time)
27. **Obliquity term, 365.25-day year**: b = 9.863 sin(2(6.24004077 + 0.01720197(365.25(y − 2000) + d)) + 3.5932) (Equation of time)
28. **Continuous arctangent**: arctan_η x = arctan x + π round((η − arctan x)/π) (Equation of time)
29. **Equation of time, continuous form**: Δt(M) = M + λ_p − arctan_(M + λ_p)(cos ε tan λ) (Equation of time)
30. **Corrected angle, alternative calculation**: B = A + 0.0167 · (360°/π) sin((D − 3) n) (Equation of time)
31. **Corrected angle, degrees**: B = A + 1.914° · sin((D − 3) n) (Equation of time)
32. **Equation of time, alternative calculation**: C = (A − arctan(tan B / cos 23.44°))/180° (Equation of time)
33. **Solar declination**: δ = −arcsin(sin 23.44° · cos B) (Equation of time)
34. **Lorentz boost in rapidity**: ct′ = ct cosh ζ − x sinh ζ, x′ = x cosh ζ − ct sinh ζ, y′ = y, z′ = z (Lorentz transformation)
35. **Hyperbolic identity**: cosh²ζ − sinh²ζ = 1 (Lorentz transformation)
36. **Hyperbolic tangent definition**: tanh ζ = sinh ζ / cosh ζ (Lorentz transformation)
37. **Cosh from tanh**: cosh ζ = 1/√(1 − tanh²ζ) (Lorentz transformation)
38. **Velocity, Lorentz factor and celerity from rapidity**: β = tanh ζ, γ = cosh ζ, βγ = sinh ζ (Lorentz transformation)
39. **Rapidity from velocity**: ζ = artanh β (Lorentz transformation)
40. **Inverse Lorentz boost in rapidity**: ct = ct′ cosh ζ + x′ sinh ζ, x = x′ cosh ζ + ct′ sinh ζ, y = y′, z = z′ (Lorentz transformation)
41. **Velocity vector from rapidity**: β = β n = n tanh ζ (Lorentz transformation)
42. **Rapidity vector**: ζ = ζ n = n artanh β (Lorentz transformation)
43. **Boost as a limit of infinitesimal boosts**: B_x = lim_(N→∞) (I − (ζ/N) K_x)^N = exp(−ζ K_x) (Lorentz transformation)
44. **Boost and rotation as exponentials**: B(ζ) = exp(−ζ·K), R(θ) = exp(θ·J) (Lorentz transformation)
45. **Boost matrix in closed form**: B(ζ) = I − sinh ζ (n·K) + (cosh ζ − 1)(n·K)² (Lorentz transformation)
46. **Rotation matrix in closed form (Rodrigues)**: R(θ) = I + sin θ (e·J) + (1 − cos θ)(e·J)² (Lorentz transformation)
47. **General Lorentz transformation as an exponential**: Λ(ζ, θ) = exp(−ζ·K + θ·J) (Lorentz transformation)
48. **Poincaré transformation of multiparticle states**: U(Λ, a) Ψ_(p₁σ₁n₁; p₂σ₂n₂; …) = exp(−i a_μ [(Λp₁)^μ + (Λp₂)^μ + …]) √((Λp₁)⁰(Λp₂)⁰…/(p₁⁰p₂⁰…)) (Σ_(σ₁′σ₂′…) D^(j₁)_(σ₁′σ₁)[W(Λ, p₁)] D^(j₂)_(σ₂′σ₂)[W(Λ, p₂)] …) Ψ_(Λp₁σ₁′n₁; Λp₂σ₂′n₂; …) (Lorentz transformation)
49. **Circumference of a circle**: C = 2πr (Circular motion)
50. **Angular velocity**: ω = 2π/T = 2πf = dθ/dt (Circular motion)
51. **Speed in uniform circular motion**: v = 2πr/T = ωr (Circular motion)
52. **Angle swept in uniform circular motion**: θ = 2π t/T = ωt (Circular motion)
53. **Circular position as a complex number**: z = x + iy = R(cos θ(t) + i sin θ(t)) = R e^(iθ(t)) (Circular motion)
54. **Circular velocity as a complex number**: v = ż = d/dt(R e^(iθ(t))) = R e^(iθ(t)) d/dt(iθ(t)) = iRθ̇(t) e^(iθ(t)) = iωR e^(iθ(t)) = iωz (Circular motion)
55. **Circular acceleration as a complex number**: a = v̇ = iω̇z + iωż = (iω̇ − ω²)z = (iω̇ − ω²) R e^(iθ(t)) = −ω²R e^(iθ(t)) + ω̇ e^(iπ/2) R e^(iθ(t)) (Circular motion)
56. **General solution of simple harmonic motion**: x(t) = c₁ cos(ωt) + c₂ sin(ωt) (Simple harmonic motion)
57. **Solution from initial position and velocity**: x(t) = x₀ cos(√(k/m) t) + (v₀/√(k/m)) sin(√(k/m) t) (Simple harmonic motion)
58. **Amplitude–phase form**: x(t) = A cos(ωt − φ) (Simple harmonic motion)
59. **Phase from the coefficients**: tan φ = c₂/c₁ (Simple harmonic motion)
60. **Phase sine and cosine**: sin φ = c₂/A, cos φ = c₁/A (Simple harmonic motion)
61. **Angular frequency from frequency**: ω = 2πf (Simple harmonic motion)
62. **Velocity in simple harmonic motion**: v(t) = dx/dt = −Aω sin(ωt − φ) (Simple harmonic motion)
63. **Acceleration in simple harmonic motion**: a(t) = d²x/dt² = −Aω² cos(ωt − φ) (Simple harmonic motion)
64. **Frequency of a mass on a spring**: f = (1/2π) √(k/m) (Simple harmonic motion)
65. **Period of a mass on a spring**: T = 2π √(m/k) (Simple harmonic motion; candidates 76 and 79 merged)
66. **Kinetic energy in simple harmonic motion**: K(t) = ½ m v²(t) = ½ m ω² A² sin²(ωt − φ) = ½ k A² sin²(ωt − φ) (Simple harmonic motion)
67. **Potential energy in simple harmonic motion**: U(t) = ½ k x²(t) = ½ k A² cos²(ωt − φ) (Simple harmonic motion)
68. **Period of a simple pendulum**: T = 2π √(l/g) (Simple harmonic motion; candidates 80 and 81 merged)
69. **Pendulum torque equation**: −mgl sin θ = Iα (Simple harmonic motion)
70. **Small-angle approximation**: sin θ ≈ θ (Simple harmonic motion)
71. **Sine form of simple harmonic motion**: x(t) = A sin(ωt + φ′) (Simple harmonic motion)
72. **Phase of the sine form**: tan φ′ = c₁/c₂ (Simple harmonic motion)
73. **Relativistic Doppler, receiver's angle**: f_r = f_s / (γ(1 + β cos θ_r)) (Relativistic Doppler effect; candidates 88 and 91 merged)
74. **Relativistic Doppler, source's angle**: f_r = γ(1 − β cos θ_s) f_s (Relativistic Doppler effect; candidates 89 and 92 merged)
75. **Relativistic aberration**: cos θ_r = (cos θ_s − β)/(1 − β cos θ_s) (Relativistic Doppler effect)
76. **Doppler transformation of the fields**: E_r = γ(1 − β cos θ_s) E_s, B_r = γ(1 − β cos θ_s) B_s (Relativistic Doppler effect)
77. **Planck spectral intensity**: I(f) ∝ f³/(e^(hf/kT) − 1) (Relativistic Doppler effect)
78. **Doppler for sound and light in a moving medium**: f_r/f_s = (1 − (|v_r|/|C|) cos θ_(C,v_r)) / (1 − (|v_s|/|C|) cos θ_(C,v_s)) · √((1 − (v_s/c)²)/(1 − (v_r/c)²)) (Relativistic Doppler effect)

## Dropped

- 2: fragment (cos²θ alone), states no relation.
- 8: fragment (the range 0 ≤ M ≤ 2π), states no relation.
- 13: fragment (the range 0 ≤ E < π), states no relation.
- 14: fragment (the range π < E ≤ 2π), states no relation.
- 17: fragment ("tan" alone), states no relation.
- 27: fragment (2λ_p − 2π, an expression), states no relation.
- 39: fragment ("tan⁻¹" alone), states no relation.
- 52: fragment (the map t → exp(tG)), states no relation.
- 56: fragment (an inequality, exp(−ζ·K + θ·J) ≠ exp(−ζ·K) exp(θ·J)), states no relation as an equation.
- 57: fragment (the map exp: so(3,1) → SO(3,1)), states no relation.
- 63: fragment (π/2 + θ, an expression), states no relation.
- 86: fragment ("cos θ =" truncated), states no relation.
- 87: fragment ("cos(ωt ± φ) =" truncated), states no relation.
- 90: fragment (v cos θ_r, an expression), states no relation.
