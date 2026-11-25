# MVM: a moving mass, a look and a pull

25 Nov 2026; Tom: "Merge and proceed". *Reads and Writes* §7, "Gravity on the stage", open item (4): what moving
masses and light's own delay do; everything there so far is at rest or in steady orbit. Exact arithmetic (sympy), no
data. A pull is not a read (R1183); what is sorted is what each points at and what each needs.

## Set-up

A point mass M moving at constant velocity v = βc along x, through the origin at t = 0; a place x₀ = (X, Y, 0) at
rest, the time t = 0 at the place. Units c = 1.
- **The look**: the light arriving at x₀ at t = 0 left the mass at the retarded time t_r < 0 with |x₀ − r(t_r)| = −t_r;
  its direction is toward r(t_r), the retarded place. The present place is r(0) = 0.
- **The pull**: linearized general relativity. In the mass's rest frame the metric perturbation is h′_μν = −2Φ′·diag(1,
  1, 1, 1) (signature −+++, Φ′ = −GM/R′); boosted to the place's frame by a Lorentz boost along x; a test body at rest
  at x₀ feels d²xⁱ/dt² = −Γⁱ₀₀ = ½∂ᵢh₀₀ − ∂₀hᵢ₀ to first order in G. Classical (Carlip 2000, "Aberration and the speed of
  gravity", from memory, to check).
- **For comparison, the field of a moving charge** (Liénard–Wiechert, uniform motion): E ∝ (1 − β²)(x₀ − r(0)) /
  (R³(1 − β² sin²ψ)^(3/2)), ψ the angle between x₀ − r(0) and v (Heaviside 1888).

## Predictions (committed before any code)

- **M1 (look).** The look points at the retarded place; the angle δ between the look and the present place obeys
  sin δ = β·sin θ_r exactly, θ_r the angle at the retarded place between v and the line to x₀ (aberration's form).
- **M2 (charge).** The Liénard–Wiechert field of the uniformly moving charge points exactly at the present place, at
  every β < 1.
- **M3 (pull).** The linearized pull on the body at rest points at the present place to first order in β; any departure
  is of order β² or higher.
- **M4 (scale).** Scaling every length and every time together by k (β fixed) moves no direction of M1–M3; the pull's
  strength moves by 1/k² (an amount, as GM/d² at rest).
- **M5 (what a direction gives).** From the look alone at one place, the present place is not given (the retarded and
  present places are one look apart only with β and the distance carried in); from the pull's direction alone it is, to
  first order in β. So a look and a pull, at rest the same direction, part when the mass moves: one points at where the
  mass was, the other (to first order) at where it is.

Kill conditions: M1 or M2 failing past an exact zero; M3's departure first order in β; M4 a direction moving.

## Runs

### Run 1 (`runs/mvm/mvm.py`, output `runs/mvm/mvm-run1.txt`; post hoc `runs/mvm/mvm1b.py`, `mvm-run1b.txt`)

- **M1 killed by my geometry**: sin δ − β·sin θ_r is 5·10⁻³ to 0.12, not zero. I left a ratio out: the retarded and
  present places are β·R_r apart along v, so the triangle gives sin δ = β·(R_r/R_p)·sin θ_r, which holds to 10⁻¹⁹¹ at
  all four places (post hoc, `mvm1b.py`). The look does point at the retarded place, by construction.
- **M2 not killed**: the Liénard–Wiechert field of the uniformly moving charge points at the present place to 10⁻¹⁹²
  at β = 0.1, 0.5, 0.6 and 0.9.
- **M3 not killed**: the linearized pull's departure from the present place is exactly
  G·M·β²·x·y·(…)·(β² − 3)·(1 − β²)/(…), whose series begins 3GMβ²·xy/r³: second order in β, none to first order. At
  β = 0.1 at (3, 4) the departure is 0.0145 rad, against the look's 0.080 rad.
- **M4 not killed**: scaling lengths and times together moves no direction (the pull's component ratio exactly, the
  look's δ to 12 digits at k = 5); the pull's strength moves by k⁻².
- **M5 not killed** by the above: one look gives the retarded place, the present one needs β and R_r carried in; the
  pull's direction gives the present place to first order in β.

Seen after the run, not predicted: the pull's radial part is −GM·(…)·(β⁴y² + 3β²x² − x² − y²), so on the line of motion
(y = 0) it changes sign at β = 1/√3, and square to it (x = 0) only at β = 1. Ahead of or behind a mass moving faster
than c/√3, a body at rest in linearized gravity is pushed away, not pulled (at β = 0.9, at (7, 1), 2.97 rad from the
present place). This is a known and debated result of the boosted weak field (the "c/√3" repulsion; Carlip 2000 and
later papers, from memory, unchecked) and is classical, not ours; recorded here because the plan did not foresee it.

Reading: a look and a pull, one direction for a mass at rest, part when it moves. The look points where the light left,
the retarded place, and getting the present place from it takes the speed and the distance, two amounts. The pull (and,
exactly, a uniformly moving charge's field) points where the mass is now, to first order in β, from the pull's direction
alone. Scaling every length and time together moves neither; only the pull's strength moves. Classical (Heaviside 1888;
Liénard–Wiechert; Carlip 2000 for gravity's aberration cancelling to first order).
