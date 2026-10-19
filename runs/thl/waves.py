"""The outer vantage read as a wave is read: the classical identities behind SPN R265's reading (Tom, 15 Oct: "the
outside has wave like chartacteristics").

The outer's facing turns 2θ on the line [0, 1] as diameter where the inner's bar turns θ (OFS §3.4); its point is
THL's crossing. Unit relations h = cos θ, v = sin θ; s = v/h. Checked: the point is (h², hv), its foot h² (Malus), at
distances h and v from the ends; it is the normalized Stokes point of polarization at θ, square polarizations at the
diameter's ends; a series resonance's admittance in units of 1/R is the crossing mirrored, (1, -s)/(1 + s²) with
s = X/R, power share h², half power at the corner; a scattered wave's amplitude e^(iδ) sin δ on the unitarity circle,
S = e^(2iδ), the Breit–Wigner share sin²δ, quartiles of an even δ at the half-maximum; the Cauchy's characteristic
function e^(-|t|); a sine's RMS over its mean rectified value equal to the outer reading at 45°. All classical; checked
after they were stated, not predictions. And (15 Oct) two paths' visibility V = 2hv = sin 2θ and
predictability P = |h² − v²| = |cos 2θ|, V² + P² = 1 for a pure state (Greenberger and Yasin 1988; Englert 1996). R, X, E_R and Γ are amounts used only to draw; every stated result is a ratio.
Run: python3 runs/thl/waves.py   (mpmath, 30 digits; a few seconds)
"""
from mpmath import mp, mpf, mpc, cos, sin, tan, cot, atan, pi, sqrt, exp, quad, quadosc, inf, fabs, arg, degrees
mp.dps = 30
ok = True
def chk(name, got, want, tol=mpf(10)**-20):
    global ok; g = fabs(got - want) <= tol; ok &= g
    print(('ok ' if g else 'BAD'), name, mp.nstr(got, 12), mp.nstr(want, 12))
for th in (mpf('0.2'), pi/4, mpf('1.3')):
    h, v = cos(th), sin(th)
    P = mpc((1 + cos(2*th))/2, sin(2*th)/2)                     # the outer's point, facing 2θ, on the diameter [0, 1]
    chk(f"θ={mp.nstr(th,4)} foot = h² (Malus)", P.real, h**2); chk("height = hv", P.imag, h*v)
    chk("distance from A = h", fabs(P), h); chk("distance from B = v", fabs(P - 1), v)
    S1, S2 = cos(2*th), sin(2*th)                                # Stokes of polarization at θ (Jones (h, v))
    chk("point = (1 + S1, S2)/2", fabs(P - mpc(1 + S1, S2)/2), 0)
    Po = mpc((1 + cos(2*(th+pi/2)))/2, sin(2*(th+pi/2))/2)       # the orthogonal polarization
    chk("orthogonal is antipodal", fabs(P + Po - 1), 0)
for s in (mpf('-3'), mpf(-1), mpf('0.4'), mpf(1), mpf(7)):
    R, X = mpf(2), 2*s; Y = 1/mpc(R, X)
    pt = (R*Y).conjugate()
    chk(f"s={s}: R·conj(Y) = (1, s)/(1+s²)", fabs(pt - mpc(1, s)/(1 + s*s)), 0)
    chk("power share |RY|² = 1/(1+s²)", fabs(R*Y)**2, 1/(1+s*s))
    chk("facing from the centre = 2·phase", fabs(arg((pt - mpf(1)/2)*2) - 2*atan(s)) if fabs(s) < 1e9 else 0, 0)
chk("half power at the corner X = R: phase (deg)", degrees(atan(1)), 45)
Er, G = mpf(10), mpf(3)
for d in (pi/4, pi/2, 3*pi/4, mpf('0.3')):
    f = exp(1j*d)*sin(d)
    chk(f"δ={mp.nstr(d,4)} on the unitarity circle", fabs(f - mpc(0, 0.5)), mpf(1)/2)
    chk("S = 1 + 2if = e^(2iδ)", fabs(1 + 2j*f - exp(2j*d)), 0)
    E = Er - G/2*cot(d)
    chk("Breit–Wigner share sin²δ", sin(d)**2, (G/2)**2/((E-Er)**2 + (G/2)**2))
chk("even δ: P(E ≤ Er − Γ/2) is δ ≤ 45°, a quarter", (pi/4)/pi, mpf(1)/4)
for t in (mpf('0.5'), mpf(1), mpf(2)):
    cf = 2*quadosc(lambda x: cos(t*x)/(pi*(1 + x*x)), [0, inf], omega=t)
    chk(f"Cauchy characteristic function at t={t} = e^(-|t|)", cf, exp(-t), tol=mpf(10)**-15)
rms = sqrt(quad(lambda x: cos(x)**2, [0, pi/2])/(pi/2)); arv = quad(cos, [0, pi/2])/(pi/2)
chk("RMS of a sine = cos 45°, the corner", rms, cos(pi/4)); chk("mean shadow 2/π", arv, 2/pi)
chk("form factor RMS/mean = outer reading at 45°", rms/arv, (pi/4)/sin(pi/4))
chk("mean foot over an even facing = ½", quad(lambda x: cos(x)**2, [0, pi/2])/(pi/2), mpf(1)/2)
for th in (mpf('0.1'), pi/4, mpf('0.9'), mpf('1.4')):            # two paths, amplitudes h and v (unit relations)
    h, v = cos(th), sin(th); Vis, Pr = 2*h*v, fabs(h*h - v*v)    # visibility, predictability (Greenberger–Yasin)
    chk(f"θ={mp.nstr(th,4)}: V = sin 2θ", Vis, sin(2*th)); chk("P = |cos 2θ|", Pr, fabs(cos(2*th)))
    chk("V² + P² = 1 (Englert's equality, a pure state)", Vis**2 + Pr**2, 1)
    k = v/h; chk("V = 2k/(1 + k²) = sech(ln k)", Vis, 1/mp.cosh(mp.log(k)))
print('all match' if ok else 'MISMATCH')
