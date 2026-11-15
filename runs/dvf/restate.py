import mpmath as mp
mp.mp.dps = 50
S = mp.sqrt
def R(x): return mp.mpf(x)
def N(n, reason): return {'n': n, 'verdict': 'NONE', 'reason': reason}
def T(n, reason, restated, orig, new, points):
    return {'n': n, 'verdict': 'notation', 'reason': reason, 'restated': restated,
            'orig': orig, 'new': new, 'points': points}
P3 = [R('0.3'), R('1.7'), R('5')]
def h(s): return 1/S(1+s*s)
def v(s): return s/S(1+s*s)
P2 = [(R('0.3'), R('0.8')), (R('1.7'), R('0.2')), (R('5'), R('2.5'))]

# constants
I0 = R(2); F = R('5.1'); F0 = R(5); LAM = R('0.3'); C = R(3)
ECC = R('0.3'); KE = S((1+ECC)/(1-ECC)); Y = R('0.04')
CT, X, YY, Z = R('2.3'), R('0.7'), R('1.1'), R('-0.4')
B = R('0.6'); G = 1/S(1-B*B)
M_, G_, L_, I_ = R(2), R('9.8'), R('0.5'), R('0.7')
RAD = R('1.5'); W = R('0.8'); WD = R('0.3')
ES, BS, FS = R(2), R('0.5'), R(7)
VR, VS, CM, CL = R('0.2'), R('0.3'), R('0.9'), R(1)

def half(s): return v(s)/(1+h(s))

def boost_orig(s, inv=False):
    z = mp.asinh(s); sg = 1 if inv else -1
    return [CT*mp.cosh(z) + sg*X*mp.sinh(z), X*mp.cosh(z) + sg*CT*mp.sinh(z), YY, Z]
def boost_new(s, inv=False):
    sg = 1 if inv else -1
    return [CT/h(s) + sg*X*s, X/h(s) + sg*CT*s, YY, Z]

def nK(s2):
    nx, ny = h(s2), v(s2)
    K = mp.zeros(4, 4)
    K[0, 1] = K[1, 0] = nx
    K[0, 2] = K[2, 0] = ny
    return K
def flat(Mx): return [Mx[i, j] for i in range(Mx.rows) for j in range(Mx.cols)]
def B45_orig(p):
    s, s2 = p; z = mp.asinh(s); K = nK(s2)
    return flat(mp.eye(4) - mp.sinh(z)*K + (mp.cosh(z)-1)*K*K)
def B45_new(p):
    s, s2 = p; K = nK(s2)
    return flat(mp.eye(4) - s*K + (1/h(s)-1)*K*K)

def eJ(s2):
    ex, ey = h(s2), v(s2)
    Jm = mp.zeros(3, 3)
    Jm[0, 2] = ey; Jm[2, 0] = -ey
    Jm[1, 2] = -ex; Jm[2, 1] = ex
    return Jm
def R46_orig(p):
    s, s2 = p; th = mp.atan(s); Jm = eJ(s2)
    return flat(mp.eye(3) + mp.sin(th)*Jm + (1-mp.cos(th))*Jm*Jm)
def R46_new(p):
    s, s2 = p; Jm = eJ(s2)
    return flat(mp.eye(3) + v(s)*Jm + (1-h(s))*Jm*Jm)

def eot2_orig(p):
    sM, sP = p; Mv = mp.atan(sM); Lp = mp.atan(sP)
    d1 = -2*ECC*mp.sin(Mv) + Y*mp.sin(2*Mv + 2*Lp)
    return [d1 - R(5)/4*ECC**2*mp.sin(2*Mv) + 4*ECC*Y*mp.sin(Mv)*mp.cos(2*Mv+2*Lp) - Y**2/2*mp.sin(4*Mv+4*Lp)]
def eot2_new(p):
    sM, sP = p
    hM, vM, hP, vP = h(sM), v(sM), h(sP), v(sP)
    hf = hM*hP - vM*vP; vf = vM*hP + hM*vP
    s2f = 2*vf*hf; c2f = hf*hf - vf*vf
    d1 = -2*ECC*vM + Y*s2f
    return [d1 - R(5)/4*ECC**2*(2*vM*hM) + 4*ECC*Y*vM*c2f - Y**2/2*(2*s2f*c2f)]

def ra18_orig(sl):
    L = mp.atan(sl)
    a = mp.findroot(lambda a: a - L + mp.asin(Y*mp.sin(a+L)), L)
    return mp.tan(a)

LAWS = [
 T(1, "the angle enters only as the polarizer's direction",
   "the intensity is the incident intensity times the square of the polarizer direction's across share",
   lambda s: I0*mp.cos(mp.atan(s))**2, lambda s: I0*h(s)**2, P3),
 T(2, "the angle enters only as the polarizer's direction; the Doppler factor is rational in amounts",
   "the intensity is the incident intensity times f/f0 times (1 + lambda(f0 - f)/(2c)) times the square of the polarizer direction's across share",
   lambda s: I0*(F/F0)*(1+LAM*(F0-F)/(2*C))*mp.cos(mp.atan(s))**2,
   lambda s: I0*(F/F0)*(1+LAM*(F0-F)/(2*C))*h(s)**2, P3),
 N(3, "D is a day count turned to an angle by a rate, the phase a stated value, the coefficients minutes carrying the radian conversion"),
 N(4, "the argument is an amount of days times a rate; a stated phase"),
 N(5, "the argument is an amount of days times a rate; a stated phase"),
 N(6, "the whole turn's 2 pi converts a time to an angle"),
 N(7, "Kepler's equation adds the angle itself to its sine: transcendental"),
 N(8, "series adding the angle itself to its sine"),
 N(9, "series adding the angle itself to its sines"),
 T(10, "a relation between two directions by their half-angles",
   "the half-slope of the true anomaly is the root of (1 + ecc)/(1 - ecc) times the half-slope of the eccentric anomaly, the half-slope of a slope s being its up share over one plus its across share; the slope is twice the half-slope over one minus its square",
   lambda s: mp.tan(2*mp.atan(KE*mp.tan(mp.atan(s)/2))),
   lambda s: (lambda t: 2*t/(1-t*t))(KE*half(s)), P3),
 N(11, "a branch shift of the angle chart; the half turn stated itself"),
 N(12, "a stated value of an angle, the half turn itself"),
 N(13, "series adding the angle itself to its sines"),
 N(14, "series adding the angle itself to its sines"),
 N(15, "series adding the angle itself to its sines"),
 T(16, "a relation between three directions",
   "the slope of the right ascension is the obliquity's across share times the slope of the ecliptic longitude",
   lambda p: mp.tan(mp.atan(mp.cos(mp.atan(p[0]))*mp.tan(mp.atan(p[1])))),
   lambda p: h(p[0])*p[1], P2),
 N(17, "a half turn's multiple added inside an amount argument; a branch chart"),
 T(18, "an implicit relation between directions; expanding the shares gives a slope relation",
   "the slope of the right ascension is (1 - y)/(1 + y) times the slope of the ecliptic longitude",
   ra18_orig, lambda sl: sl*(1-Y)/(1+Y), P3),
 T(19, "y is the squared half-slope of the obliquity",
   "y is the square of the obliquity's up share over one plus its across share",
   lambda s: mp.tan(mp.atan(s)/2)**2, lambda s: half(s)**2, P3),
 N(20, "series subtracting from the angle itself"),
 N(21, "the numeric form's coefficients are minutes per radian (a conversion carrying the turn) and a stated phase"),
 T(22, "every term is a share of the directions M and M + lambda_p; no angle enters as itself",
   "with M's shares (a, b) and the shares of M plus the perihelion direction (c, d) by the sum rule, the first-order value is -2 ecc b + y 2cd; the second-order value is that minus (5/4) ecc squared 2ab plus 4 ecc y b (c^2 - d^2) minus half y squared times 2(2cd)(c^2 - d^2)",
   eot2_orig, eot2_new, P2),
 N(23, "the whole turn converts a day count to an angle"),
 N(24, "the whole turn converts a day count to an angle"),
 N(25, "a stated value, the whole turn"),
 N(26, "the argument is an amount of days times a rate; a stated phase"),
 N(27, "the argument is an amount of days times a rate; a stated phase"),
 N(28, "a branch chart of the angle; the half turn stated itself"),
 N(29, "the angles themselves are subtracted as amounts"),
 N(30, "angle from a day count; degrees per radian"),
 N(31, "angle from a day count in degrees"),
 N(32, "angles subtracted as amounts and divided by 180 degrees"),
 N(33, "a stated obliquity in degrees and B from a day count"),
 T(34, "the rapidity's functions are the celerity and the Lorentz factor",
   "with celerity slope s, ct' = ct root(1+s^2) - x s, x' = x root(1+s^2) - ct s, y' = y, z' = z",
   lambda s: boost_orig(s), lambda s: boost_new(s), P3),
 T(35, "the identity among the celerity and the Lorentz factor",
   "(1 + s^2) - s^2 = 1",
   lambda s: [mp.cosh(mp.asinh(s))**2 - mp.sinh(mp.asinh(s))**2, 1],
   lambda s: [(1+s*s) - s*s, 1], P3),
 T(36, "the velocity is celerity over Lorentz factor",
   "the velocity, the celerity slope's up share, equals the celerity over root(1 + s^2)",
   lambda s: [mp.tanh(mp.asinh(s)), mp.sinh(mp.asinh(s))/mp.cosh(mp.asinh(s))],
   lambda s: [v(s), s*h(s)], P3),
 T(37, "the Lorentz factor from the velocity",
   "root(1 + s^2) equals one over root(1 minus the square of the up share)",
   lambda s: [mp.cosh(mp.asinh(s)), 1/S(1-mp.tanh(mp.asinh(s))**2)],
   lambda s: [1/h(s), 1/S(1-v(s)**2)], P3),
 T(38, "velocity, Lorentz factor and celerity from one slope",
   "the velocity is the celerity slope's up share, the Lorentz factor one over its across share, the celerity the slope",
   lambda s: [mp.tanh(mp.asinh(s)), mp.cosh(mp.asinh(s)), mp.sinh(mp.asinh(s))],
   lambda s: [v(s), 1/h(s), s], P3),
 N(39, "the rapidity itself as an amount, a logarithm"),
 T(40, "the inverse boost by the celerity and the Lorentz factor",
   "with celerity slope s, ct = ct' root(1+s^2) + x' s, x = x' root(1+s^2) + ct' s, y = y', z = z'",
   lambda s: boost_orig(s, True), lambda s: boost_new(s, True), P3),
 T(41, "the velocity vector is a unit direction times the velocity",
   "the velocity vector is the unit direction (shares of the second slope) times the celerity slope's up share",
   lambda p: [mp.cos(mp.atan(p[1]))*mp.tanh(mp.asinh(p[0])), mp.sin(mp.atan(p[1]))*mp.tanh(mp.asinh(p[0])), 0],
   lambda p: [h(p[1])*v(p[0]), v(p[1])*v(p[0]), 0], P2),
 N(42, "the rapidity itself as an amount"),
 N(43, "a limit of a product; the matrix exponential of an amount"),
 N(44, "the exponential map of generators scaled by amounts"),
 T(45, "the closed form's functions are celerity and Lorentz factor",
   "the boost matrix is I minus s (n.K) plus (root(1+s^2) - 1)(n.K)^2, n a unit direction by shares",
   B45_orig, B45_new, P2),
 T(46, "the rotation's functions are the shares of its direction",
   "the rotation matrix is I plus the up share (u.J) plus (1 minus the across share)(u.J)^2, u the unit axis",
   R46_orig, R46_new, P2),
 N(47, "the exponential map of generators scaled by amounts"),
 N(48, "a phase that is the exponential of an amount a.p"),
 N(49, "the whole turn as a total, a length"),
 N(50, "the whole turn per period, an angular rate"),
 N(51, "the whole turn per period"),
 N(52, "angle as a time times a rate"),
 T(53, "the exponential of the direction names the point on the circle",
   "z = R(a + i b), a and b the direction's across and up shares, the same in both written forms",
   lambda s: [mp.re(RAD*mp.expj(mp.atan(s))), mp.im(RAD*mp.expj(mp.atan(s))), RAD*mp.cos(mp.atan(s)), RAD*mp.sin(mp.atan(s))],
   lambda s: [RAD*h(s), RAD*v(s), RAD*h(s), RAD*v(s)], P3),
 T(54, "the velocity is i omega times the point; the direction enters by its shares",
   "the velocity is i omega R (a + i b), that is (-omega R b, omega R a), a and b the direction's shares",
   lambda s: [mp.re(1j*W*RAD*mp.expj(mp.atan(s))), mp.im(1j*W*RAD*mp.expj(mp.atan(s)))],
   lambda s: [-W*RAD*v(s), W*RAD*h(s)], P3),
 T(55, "the acceleration is (i omega-dot minus omega squared) times the point; the quarter turn factor is i",
   "the acceleration is (i wd - w^2) R (a + i b) = (-w^2 R a - wd R b, wd R a - w^2 R b), the quarter turn factor being i",
   lambda s: [mp.re((1j*WD - W**2)*RAD*mp.expj(mp.atan(s))), mp.im((1j*WD - W**2)*RAD*mp.expj(mp.atan(s))),
              mp.re(-W**2*RAD*mp.expj(mp.atan(s)) + WD*mp.expj(mp.pi/2)*RAD*mp.expj(mp.atan(s))),
              mp.im(-W**2*RAD*mp.expj(mp.atan(s)) + WD*mp.expj(mp.pi/2)*RAD*mp.expj(mp.atan(s)))],
   lambda s: [-W**2*RAD*h(s) - WD*RAD*v(s), WD*RAD*h(s) - W**2*RAD*v(s),
              -W**2*RAD*h(s) - WD*RAD*v(s), WD*RAD*h(s) - W**2*RAD*v(s)], P3),
 N(56, "the circular functions of an amount omega t"),
 N(57, "the circular functions of an amount of time"),
 N(58, "the circular function of an amount of time"),
 T(59, "the phase is the direction of the point (c1, c2)",
   "the slope of the phase is c2/c1",
   lambda p: mp.tan(mp.atan2(p[1], p[0])), lambda p: p[1]/p[0], P2),
 T(60, "the phase's shares are the coefficients over the amplitude",
   "the phase's up share is c2/A and its across share c1/A, A = root(c1^2 + c2^2)",
   lambda p: [mp.sin(mp.atan2(p[1], p[0])), p[1]/S(p[0]**2+p[1]**2), mp.cos(mp.atan2(p[1], p[0])), p[0]/S(p[0]**2+p[1]**2)],
   lambda p: [v(p[1]/p[0]), p[1]/S(p[0]**2+p[1]**2), h(p[1]/p[0]), p[0]/S(p[0]**2+p[1]**2)], P2),
 N(61, "the whole turn converts a frequency to an angular rate"),
 N(62, "the circular function of an amount of time"),
 N(63, "the circular function of an amount of time"),
 N(64, "the whole turn converts an angular rate to a frequency"),
 N(65, "the whole turn in a period"),
 N(66, "the circular function of an amount of time"),
 N(67, "the circular function of an amount of time"),
 N(68, "the whole turn in a period"),
 T(69, "the angle enters only as the pendulum's direction",
   "the angular acceleration is -m g l times the direction's up share over I",
   lambda s: -M_*G_*L_*mp.sin(mp.atan(s))/I_, lambda s: -M_*G_*L_*v(s)/I_, P3),
 N(70, "compares the angle itself with its share"),
 N(71, "the circular function of an amount of time"),
 T(72, "the phase is the direction of the point (c2, c1)",
   "the slope of the phase is c1/c2",
   lambda p: mp.tan(mp.atan2(p[0], p[1])), lambda p: p[0]/p[1], P2),
 T(73, "the angle enters only as the receiver's direction",
   "f_r = f_s / (gamma (1 + beta a)), a the receiver direction's across share",
   lambda s: FS/(G*(1+B*mp.cos(mp.atan(s)))), lambda s: FS/(G*(1+B*h(s))), P3),
 T(74, "the angle enters only as the source's direction",
   "f_r = gamma (1 - beta a) f_s, a the source direction's across share",
   lambda s: G*(1-B*mp.cos(mp.atan(s)))*FS, lambda s: G*(1-B*h(s))*FS, P3),
 T(75, "a relation between two directions' across shares",
   "the received direction's across share is (a - beta)/(1 - beta a), a the source direction's across share",
   lambda s: mp.cos(mp.acos((mp.cos(mp.atan(s))-B)/(1-B*mp.cos(mp.atan(s))))),
   lambda s: (h(s)-B)/(1-B*h(s)), P3),
 T(76, "the angle enters only as the source's direction",
   "E_r = gamma (1 - beta a) E_s and B_r = gamma (1 - beta a) B_s, a the source direction's across share",
   lambda s: [G*(1-B*mp.cos(mp.atan(s)))*ES, G*(1-B*mp.cos(mp.atan(s)))*BS],
   lambda s: [G*(1-B*h(s))*ES, G*(1-B*h(s))*BS], P3),
 N(77, "the exponential of an amount hf/kT"),
 T(78, "the angles enter only as two directions",
   "f_r/f_s = (1 - (v_r/C) a_r)/(1 - (v_s/C) a_s) times root((1 - (v_s/c)^2)/(1 - (v_r/c)^2)), a_r and a_s the directions' across shares",
   lambda p: (1-(VR/CM)*mp.cos(mp.atan(p[0])))/(1-(VS/CM)*mp.cos(mp.atan(p[1])))*S((1-(VS/CL)**2)/(1-(VR/CL)**2)),
   lambda p: (1-(VR/CM)*h(p[0]))/(1-(VS/CM)*h(p[1]))*S((1-(VS/CL)**2)/(1-(VR/CL)**2)), P2),
]
