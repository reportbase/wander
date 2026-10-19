"""Checks of the numbers in the archived paper "Special Relativity, Through the Fisheye" (papers/archive/
sr-through-the-fisheye.md), as far as they can be recomputed here, and of one link to MOT run 2. An audit of a record,
not a test with predictions. See plans/archive-gems.md, "Special Relativity, Through the Fisheye"."""
import numpy as np
rng = np.random.default_rng(14)
kof = lambda b: np.sqrt((1 + b)/(1 - b))

# C0: the half-angle aberration against the cosine form
b = 0.6; k = kof(b); th = np.linspace(0.01, np.pi - 0.01, 1001)
half = 2*np.arctan(np.tan(th/2)/k); cosf = np.arccos((np.cos(th) + b)/(1 + b*np.cos(th)))
print(f"C0 half-angle against the cosine form, beta 0.6: worst {np.max(abs(half - cosf)):.1e} rad")

# C1: the stereographic reading of an isotropic sky, on a circle (2+1) and on a sphere (3+1)
n = 200001
t_circle = np.tan(np.linspace(-np.pi, np.pi, n + 2)[1:-1]/2)
for b in (0.0, 0.5, 0.9):
    q = np.quantile(t_circle/kof(b), [0.25, 0.5, 0.75])
    print(f"C1 circle sky, beta {b}: quartiles {q[0]:+.5f} {q[2]:+.5f} (1/k = {1/kof(b):.5f}), median {q[1]:+.1e}")
u = rng.uniform(-1, 1, 10**6); ph = rng.uniform(0, 2*np.pi, 10**6); r = np.sqrt((1 - u)/(1 + u))   # tan(theta/2)
x = r*np.cos(ph)
print(f"C1 sphere sky: radius tan(theta/2) median {np.median(r):.4f} (CDF r^2/(1+r^2): 1); one signed coordinate's "
      f"quartiles {np.quantile(x, 0.25):+.4f} {np.quantile(x, 0.75):+.4f} (Cauchy would be -1, +1; 1/sqrt 3 = 0.5774)")

# C2: the lens faces aft
for b in (0.5, 0.9):
    k = kof(b); img90 = 2*np.degrees(np.arctan(1/k))
    print(f"C2 beta {b}: magnification fore {1/k:.3f}, aft {k:.3f}; the forward hemisphere seen within {img90:.1f} deg")
k = kof(1/np.sqrt(2)); print(f"C2 beta 1/sqrt 2: k = {k:.6f} (1 + sqrt 2 = {1 + np.sqrt(2):.6f}); forward hemisphere within"
                              f" {2*np.degrees(np.arctan(1/k)):.6f} deg")

# C3: the k-ladder
for m in range(1, 7):
    k = 2.0**m; beta = (k*k - 1)/(k*k + 1); cel = (k - 1/k)/2
    print(f"C3 k = 2^{m}: beta = {4**m - 1}/{4**m + 1}; celerity {cel:.4f}; rapidity in doublings minus log2 celerity"
          f" {m - np.log2(cel):.4f}")

# C4: pseudorapidity shifts by ln k under a boost along the axis
b = 0.6; k = kof(b); th = np.array([0.2, 0.9, 1.6, 2.5])
eta = -np.log(np.tan(th/2)); eta2 = -np.log(np.tan(np.arctan(np.tan(th/2)/k)))
print(f"C4 eta' - eta = {', '.join(f'{d:.12f}' for d in eta2 - eta)}; ln k = {np.log(k):.12f}")

# C8: two boosts at an angle, in 2+1 dimensions
def boost(z, a):
    c, s = np.cosh(z), np.sinh(z); nx, ny = np.cos(a), np.sin(a)
    return np.array([[c, s*nx, s*ny], [s*nx, 1 + (c - 1)*nx*nx, (c - 1)*nx*ny], [s*ny, (c - 1)*nx*ny, 1 + (c - 1)*ny*ny]])
L = boost(np.log(3), 0.70) @ boost(np.log(4), 0.0)
zc = np.arccosh(L[0, 0]); nvec = L[1:, 0]/np.sinh(zc); B = boost(zc, np.arctan2(nvec[1], nvec[0]))
R = np.linalg.inv(B) @ L; w = np.degrees(np.arctan2(R[2, 1], R[1, 1]))
tw = 2*np.degrees(np.arctan(np.sin(0.7)/(np.cos(0.7) + (5/3)*2)))
print(f"C8 rapidities ln 4, ln 3 at 0.70 rad: composite k = {np.exp(zc):.4f}; Wigner rotation {abs(w):.2f} deg"
      f" (closed form {tw:.2f})")

# C9: the Breit-Wigner line as an evenly spread phase
ER, G = 1.0, 0.4; d = np.linspace(0, np.pi, 200003)[1:-1]; E = ER - (G/2)/np.tan(d)
q = np.quantile(E, [0.25, 0.5, 0.75])
print(f"C9 quartiles {q[0]:.6f} {q[2]:.6f} (E_R -+ Gamma/2 = 0.8, 1.2), median {q[1]:.6f}")

# C10: two Lorentzians convolved: half-widths add (closed form); the paper's grid read 0.795
print("C10 half-widths 0.3 and 0.5 convolve to 0.8 exactly (Cauchy scales add); the paper's grid value 0.795")

# The link to MOT run 2: in the Doppler pair's levels zeta = ln k, gamma is even and gamma*beta odd, and 1/gamma is
# the facing's sine 2k/(1 + k^2), the form of a launch's range and a baseline's conditioning
ks = np.logspace(-3, 3, 6001)
g = (ks + 1/ks)/2; gb = (ks - 1/ks)/2; beta = (ks*ks - 1)/(ks*ks + 1)
print(f"MOT link: gamma(k)/gamma(1/k) - 1 at most {np.max(abs(g/((1/ks + ks)/2) - 1)):.1e}; gamma*beta odd to "
      f"{np.max(abs(gb + (1/ks - ks)/2)):.1e}; 1/gamma against 2k/(1+k^2) {np.max(abs(1/g - 2*ks/(1 + ks*ks))):.1e};"
      f" beta^2 + 1/gamma^2 - 1 at most {np.max(abs(beta**2 + 1/g**2 - 1)):.1e}")
