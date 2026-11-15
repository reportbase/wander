"""DVC: the laws of runs/dvc/laws.md, each restated in slopes and shares or judged content. Checked by runs/dvc/check.py."""
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

# trig-free helpers for the restatements
def UPS(a, b): return v(a)*h(b) + h(a)*v(b)      # up share of two directions joined
def ACS(a, b): return h(a)*h(b) - v(a)*v(b)      # across share of two directions joined
def UPD(a, b): return v(a)*h(b) - h(a)*v(b)      # up share of the first less the second
def ACD(a, b): return h(a)*h(b) + v(a)*v(b)
def add(a, b): return (a+b)/(1-a*b)
def sub(a, b): return (a-b)/(1+a*b)
def slope_of_up(u): return u/S(1-u*u)
def mv(M, x): return [sum(M[i][j]*x[j] for j in range(3)) for i in range(3)]

# helpers for the original forms only
A_ = mp.atan
def sn(s): return mp.sin(mp.atan(s))
def cs(s): return mp.cos(mp.atan(s))

r = R
P2 = [(r('0.3'), r('0.2')), (r('1.7'), r('0.9')), (r('5'), r('2.5'))]
PF = [(r('0.3'), r('0.2'), r('1.0'), r('1.5')), (r('1.7'), r('0.9'), r('1.2'), r('1.7')), (r('5'), r('2.5'), r('0.8'), r('2.1'))]
PI = [(r('0.3'), r('1.0'), r('1.5')), (r('1.7'), r('1.0'), r('1.5')), (r('5'), r('1.2'), r('1.33'))]
def ct_snell(si, n1, n2): return S(1 - (n1/n2*v(si))**2)
def ct_orig(si, n1, n2): return mp.cos(mp.asin(n1/n2*sn(si)))

LAWS = []
def add_law(x): LAWS.append(x)

add_law(T(1, 'sines of two directions', 'the ratio of the two up shares equals the index ratio',
    lambda p: sn(p[0])/sn(p[1]), lambda p: v(p[0])/v(p[1]), P2))
add_law(T(2, 'sines of two directions', 'the ratio of the two up shares equals the speed ratio',
    lambda p: sn(p[0])/sn(p[1]), lambda p: v(p[0])/v(p[1]), P2))
PXA = [(r('0.3'), r('1')), (r('2'), r('1.3')), (r('7'), r('1.4'))]
add_law(T(3, 'path geometry', 'x over the hypotenuse is the up share of the slope x/a',
    lambda p: mp.sin(mp.atan2(p[0], p[1])), lambda p: v(p[0]/p[1]), PXA))
PLX = [(r('5'), r('1'), r('2')), (r('4'), r('0.5'), r('1.3')), (r('9'), r('2'), r('0.7'))]
add_law(T(4, 'path geometry', 'the far leg over its hypotenuse is the up share of the slope (l - x)/b',
    lambda p: mp.sin(mp.atan2(p[0]-p[1], p[2])), lambda p: v((p[0]-p[1])/p[2]), PLX))
PV = [(r('0.3'), r('0.2'), r('1'), r('0.7')), (r('1.7'), r('0.9'), r('2'), r('1.1')), (r('5'), r('2.5'), r('3'), r('2.9'))]
add_law(T(5, 'sines of two directions', 'the up shares over the speeds, differenced',
    lambda p: sn(p[0])/p[2] - sn(p[1])/p[3], lambda p: v(p[0])/p[2] - v(p[1])/p[3], PV))
add_law(T(6, 'sines of two directions', 'each index times its up share, both sides',
    lambda p: [p[2]*sn(p[0]), p[3]*sn(p[1]), sn(p[0])/p[2]], lambda p: [p[2]*v(p[0]), p[3]*v(p[1]), v(p[0])/p[2]], PF))
PK = [(a, b, c, d, r('3.1')) for (a, b, c, d) in PF]
add_law(T(7, 'sines of two directions', 'index times wavenumber times up share, both sides',
    lambda p: [p[2]*p[4]*sn(p[0]), p[3]*p[4]*sn(p[1])], lambda p: [p[2]*p[4]*v(p[0]), p[3]*p[4]*v(p[1])], PK))
add_law(N(8, 'k0 = 2 pi / wavelength: the whole turn converts a length per cycle to a wavenumber, an amount'))
add_law(T(9, 'a direction and a normal', 'minus the normal dotted with the ray is its across share',
    lambda s: cs(s), lambda s: -(0*v(s) + 1*(-h(s))), P3))
add_law(T(10, 'reflection vector', 'the ray plus twice its across share along the normal',
    lambda s: [sn(s), -cs(s) + 2*cs(s)], lambda s: [v(s), -h(s) + 2*h(s)], P3))
PR = [(r('0.3'), r('0.6')), (r('1.7'), r('0.75')), (r('5'), r('0.9'))]
add_law(T(11, 'refraction', 'the index ratio times the up share, or times the root of one less the across share squared',
    lambda p: [p[1]*sn(p[0]), p[1]*S(1-cs(p[0])**2)], lambda p: [p[1]*v(p[0]), p[1]*S(1-h(p[0])**2)], PR))
add_law(T(12, 'refraction', 'the second across share is the root of one less the ratio squared times one less the first across share squared',
    lambda p: mp.cos(mp.asin(p[1]*sn(p[0]))), lambda p: S(1 - p[1]**2*(1 - h(p[0])**2)), PR))
def o13(p):
    s, q = p; c1 = cs(s); c2 = mp.cos(mp.asin(q*sn(s)))
    return [q*sn(s), -q*c1 + (q*c1 - c2)]
def n13(p):
    s, q = p; c1 = h(s); c2 = S(1 - q*q*(1 - c1*c1))
    return [q*v(s), -q*c1 + (q*c1 - c2)]
add_law(T(13, 'refraction vector', 'ratio times the ray plus (ratio times first across share less second) along the normal', o13, n13, PR))
add_law(N(14, 'numerical example with rounded figures (0.707107, 0.771362); cannot agree exactly'))
add_law(N(15, 'numerical example at 50 degrees with rounded figures (0.766, 1.021)'))
add_law(T(16, 'critical direction', 'the critical direction has up share n2/n1, so slope n2/n1 over the root of one less its square',
    lambda q: mp.tan(mp.asin(q)), lambda q: q/S(1-q*q), [r('0.3'), r('0.6'), r('0.9')]))
add_law(T(17, 'sines of two directions', 'each index times its up share',
    lambda p: [p[2]*sn(p[0]), p[3]*sn(p[1])], lambda p: [p[2]*v(p[0]), p[3]*v(p[1])], PF))
add_law(T(18, 'across shares of two directions', 'impedances times across shares, differenced over summed, squared',
    lambda p: ((p[3]*cs(p[0]) - p[2]*cs(p[1]))/(p[3]*cs(p[0]) + p[2]*cs(p[1])))**2,
    lambda p: ((p[3]*h(p[0]) - p[2]*h(p[1]))/(p[3]*h(p[0]) + p[2]*h(p[1])))**2, PF))
add_law(T(19, 'across shares of two directions', 'impedances times across shares, differenced over summed, squared',
    lambda p: ((p[3]*cs(p[1]) - p[2]*cs(p[0]))/(p[3]*cs(p[1]) + p[2]*cs(p[0])))**2,
    lambda p: ((p[3]*h(p[1]) - p[2]*h(p[0]))/(p[3]*h(p[1]) + p[2]*h(p[0])))**2, PF))
add_law(T(20, 'across shares, the second from Snell by a square root', 'indices times across shares, the transmitted one the root of one less (n1/n2 times the up share) squared',
    lambda p: ((p[1]*cs(p[0]) - p[2]*ct_orig(*p))/(p[1]*cs(p[0]) + p[2]*ct_orig(*p)))**2,
    lambda p: ((p[1]*h(p[0]) - p[2]*ct_snell(*p))/(p[1]*h(p[0]) + p[2]*ct_snell(*p)))**2, PI))
add_law(T(21, 'across shares, the second from Snell by a square root', 'as law 20 for the other polarization',
    lambda p: ((p[1]*ct_orig(*p) - p[2]*cs(p[0]))/(p[1]*ct_orig(*p) + p[2]*cs(p[0])))**2,
    lambda p: ((p[1]*ct_snell(*p) - p[2]*h(p[0]))/(p[1]*ct_snell(*p) + p[2]*h(p[0])))**2, PI))
def f22(ci, ct, n1, n2):
    return [(n1*ci - n2*ct)/(n1*ci + n2*ct), 2*n1*ci/(n1*ci + n2*ct), (n2*ci - n1*ct)/(n2*ci + n1*ct), 2*n1*ci/(n2*ci + n1*ct)]
add_law(T(22, 'across shares', 'the four amplitude ratios in indices and across shares',
    lambda p: f22(cs(p[0]), cs(p[1]), p[2], p[3]), lambda p: f22(h(p[0]), h(p[1]), p[2], p[3]), PF))
PT = [(a, b, c, d, r('0.7')) for (a, b, c, d) in PF]
add_law(T(23, 'across shares', 'index and across share ratio times the amplitude squared',
    lambda p: p[3]*cs(p[1])/(p[2]*cs(p[0]))*p[4]**2, lambda p: p[3]*h(p[1])/(p[2]*h(p[0]))*p[4]**2, PT))
add_law(T(24, 'up shares', 'the first index times the ratio of up shares',
    lambda p: p[2]*sn(p[0])/sn(p[1]), lambda p: p[2]*v(p[0])/v(p[1]), PF))
add_law(T(25, 'difference and join of two directions', 'minus the up share of the difference over the up share of the join, by the addition rules in shares',
    lambda p: -mp.sin(A_(p[0]) - A_(p[1]))/mp.sin(A_(p[0]) + A_(p[1])), lambda p: -UPD(p[0], p[1])/UPS(p[0], p[1]), P2))
add_law(T(26, 'difference and join of two directions', 'the slope of the difference over the slope of the join, by slope addition',
    lambda p: mp.tan(A_(p[0]) - A_(p[1]))/mp.tan(A_(p[0]) + A_(p[1])), lambda p: sub(p[0], p[1])/add(p[0], p[1]), P2))
def f27(vi, hi, vt, ht, n1, n2, k):
    return [n1*k*vi, n1*k*hi, n1*k*vi, -n1*k*hi, n2*k*vt, n2*k*ht]
add_law(T(27, 'wave vector components', 'index times wavenumber times up and across shares',
    lambda p: f27(sn(p[0]), cs(p[0]), sn(p[1]), cs(p[1]), p[2], p[3], p[4]),
    lambda p: f27(v(p[0]), h(p[0]), v(p[1]), h(p[1]), p[2], p[3], p[4]), PK))
PX = [(a, b, c, d, k, r('0.4'), r('1.3')) for (a, b, c, d, k) in PK]
def f28(vi, hi, ht, n1, n2, k, x, y):
    return [n1*k*(x*vi + y*hi), n1*k*(x*vi - y*hi), k*(n1*x*vi + n2*y*ht)]
add_law(T(28, 'phases as projections', 'index times wavenumber times x and y weighted by the shares',
    lambda p: f28(sn(p[0]), cs(p[0]), cs(p[1]), p[2], p[3], p[4], p[5], p[6]),
    lambda p: f28(v(p[0]), h(p[0]), h(p[1]), p[2], p[3], p[4], p[5], p[6]), PX))
add_law(T(29, 'phases at y = 0', 'at y = 0 all three phases are index times wavenumber times x times the up share',
    lambda p: f28(sn(p[0]), cs(p[0]), cs(p[1]), p[2], p[3], p[4], p[5], 0),
    lambda p: [p[2]*p[4]*p[5]*v(p[0])]*3, PX))
for n_ in (30, 31, 32, 37, 38):
    add_law(N(n_, 'a field as the exponential of a phase (an amount); renaming it is not a restatement'))
PH = [(r('0.3'), r('0.2'), r('1.1'), r('0.4'), r('0.6')), (r('1.7'), r('0.9'), r('0.8'), r('0.3'), r('0.9')), (r('5'), r('2.5'), r('2'), r('0.7'), r('1.5'))]
add_law(T(33, 'across shares', 'field values weighted by across shares, both sides; the first condition has no direction',
    lambda p: [p[2] + p[3], p[2]*cs(p[0]) - p[3]*cs(p[0]), p[4]*cs(p[1])],
    lambda p: [p[2] + p[3], p[2]*h(p[0]) - p[3]*h(p[0]), p[4]*h(p[1])], PH))
PY = [(a, b, c, d, r('0.3'), r('1.3')) for (a, b, c, d) in PF]
add_law(T(34, 'across shares', 'admittances and coefficients weighted by across shares, both sides',
    lambda p: [p[2]*cs(p[0]) - p[2]*p[4]*cs(p[0]), p[3]*p[5]*cs(p[1])],
    lambda p: [p[2]*h(p[0]) - p[2]*p[4]*h(p[0]), p[3]*p[5]*h(p[1])], PY))
def mk(f):  # f(ci, ct, A1, A2)
    return (lambda p: f(cs(p[0]), cs(p[1]), p[2], p[3]), lambda p: f(h(p[0]), h(p[1]), p[2], p[3]))
F = {
 35: lambda ci, ct, a, b: (a*ci - b*ct)/(a*ci + b*ct),
 36: lambda ci, ct, a, b: 2*a*ci/(a*ci + b*ct),
 41: lambda ci, ct, a, b: (b*ci - a*ct)/(b*ci + a*ct),
 42: lambda ci, ct, a, b: 2*a*ci/(b*ci + a*ct),
 43: lambda ci, ct, a, b: ((a*ci - b*ct)/(a*ci + b*ct))**2,
 44: lambda ci, ct, a, b: ((b*ci - a*ct)/(b*ci + a*ct))**2,
 45: lambda ci, ct, a, b: [1 - ((a*ci - b*ct)/(a*ci + b*ct))**2, 4*a*b*ci*ct/(a*ci + b*ct)**2],
 46: lambda ci, ct, a, b: [1 - ((b*ci - a*ct)/(b*ci + a*ct))**2, 4*a*b*ci*ct/(b*ci + a*ct)**2],
 47: lambda ci, ct, a, b: [(2*a*ci/(a*ci + b*ct))**2*(b/a)*(ct/ci), 4*a*b*ci*ct/(a*ci + b*ct)**2],
 48: lambda ci, ct, a, b: [(2*a*ci/(b*ci + a*ct))**2*(b/a)*(ct/ci), 4*a*b*ci*ct/(b*ci + a*ct)**2],
 49: lambda ci, ct, a, b: (a*ci - b*ct)/(a*ci + b*ct),
 50: lambda ci, ct, a, b: 2*a*ci/(a*ci + b*ct),
 51: lambda ci, ct, a, b: (b*ci - a*ct)/(b*ci + a*ct),
 52: lambda ci, ct, a, b: 2*a*ci/(b*ci + a*ct),
 53: lambda ci, ct, a, b: ((a*ci - b*ct)/(a*ci + b*ct))**2,
 54: lambda ci, ct, a, b: ((b*ci - a*ct)/(b*ci + a*ct))**2,
 57: lambda c1, c2, a, b: ((a*c2 - b*c1)/(a*c2 + b*c1))**2,
 58: lambda c1, c2, a, b: [b*c1, a*c2],
}
for n_ in (35, 36, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 57, 58):
    o, w = mk(F[n_])
    add_law(T(n_, 'across shares of two directions', 'the same rational form with each across share in place', o, w, PF))
PP = [x + (r('0.5'),) for x in PH]
add_law(T(39, 'across shares', 'field values weighted by across shares, both sides; the second condition has no direction',
    lambda p: [p[2]*cs(p[0]) - p[3]*cs(p[0]), p[4]*cs(p[1]), p[5] + p[3]],
    lambda p: [p[2]*h(p[0]) - p[3]*h(p[0]), p[4]*h(p[1]), p[5] + p[3]], PP))
add_law(T(40, 'across shares', 'coefficients weighted by across shares, both sides',
    lambda p: [cs(p[0]) - p[4]*cs(p[0]), p[5]*cs(p[1]), p[2] + p[2]*p[4]],
    lambda p: [h(p[0]) - p[4]*h(p[0]), p[5]*h(p[1]), p[2] + p[2]*p[4]], PY))
PN = [(r('1'), r('1.5')), (r('1.33'), r('1')), (r('1'), r('2.4'))]
add_law(T(55, 'Brewster direction', 'the Brewster direction is the one whose slope is n2/n1',
    lambda p: [mp.sin(mp.atan(p[1]/p[0])), mp.cos(mp.atan(p[1]/p[0]))], lambda p: [v(p[1]/p[0]), h(p[1]/p[0])], PN))
def o56(p):
    t = mp.atan(p[1]/p[0]); return [p[0]*mp.sin(t), p[1]*mp.sin(mp.pi/2 - t), p[1]*mp.cos(t)]
def n56(p):
    s = p[1]/p[0]; return [p[0]*v(s), p[1]*h(s), p[1]*h(s)]
add_law(T(56, 'Brewster direction and its complement', 'the complement swaps up and across shares; at slope n2/n1 both sides agree', o56, n56, PN))
add_law(T(59, 'shares squared', 'up share squared plus across share squared is one, weighted by the indices',
    lambda p: [p[2]**4*sn(p[0])**2 + p[3]**4*cs(p[0])**2, p[2]**2*p[3]**2*(sn(p[1])**2 + cs(p[1])**2), p[2]**2*p[3]**2, p[2]**2*p[3]**2*(sn(p[0])**2 + cs(p[0])**2)],
    lambda p: [p[2]**4*v(p[0])**2 + p[3]**4*h(p[0])**2, p[2]**2*p[3]**2*(v(p[1])**2 + h(p[1])**2), p[2]**2*p[3]**2, p[2]**2*p[3]**2*(v(p[0])**2 + h(p[0])**2)], PF))
add_law(T(60, 'a slope squared', 'the slope squared equals the index ratio squared',
    lambda s: mp.tan(mp.atan(s))**2, lambda s: s*s, P3))
PAD = [(r('0.3'), r('0.2')), (r('0.6'), r('0.4')), (r('0.5'), r('1.3'))]
add_law(T(61, 'half directions joined', 'up share of the two half directions joined, over the up share of the half apex',
    lambda p: mp.sin((2*A_(p[0]) + 2*A_(p[1]))/2)/mp.sin(A_(p[0])), lambda p: UPS(p[0], p[1])/v(p[0]), PAD))
add_law(T(62, 'up shares', 'the ratio of up shares', lambda p: sn(p[0])/sn(p[1]), lambda p: v(p[0])/v(p[1]), P2))
PAN = [(r('0.3'), r('1.5')), (r('0.5'), r('1.3')), (r('0.6'), r('1.2'))]
def o63(p):
    a, n = p; A = 2*A_(a); D = 2*mp.asin(n*mp.sin(A/2)) - A; return mp.tan(D/2)
def n63(p):
    a, n = p; u = n*v(a); return sub(slope_of_up(u), a)
add_law(T(63, 'half deviation', 'the half deviation has the slope of the direction with up share n times the half apex up share, less the half apex, by slope subtraction', o63, n63, PAN))
PD = [r('0.1'), r('0.3'), r('0.6')]
h30, v30 = S(3)/2, R(1)/2
add_law(T(64, 'a 60 degree prism: the half apex has up share one half and across share root three over two', 'up share of the half apex joined with half the deviation, over one half',
    lambda d: mp.sin((mp.pi/3 + 2*A_(d))/2)/mp.sin(mp.pi/6), lambda d: (v30*h(d) + h30*v(d))/v30, PD))
add_law(T(65, 'as law 64', 'up share of the half apex joined with half the deviation, over one half',
    lambda d: mp.sin(mp.pi/6 + A_(d))/mp.sin(mp.pi/6), lambda d: (v30*h(d) + h30*v(d))/v30, PD))
add_law(T(66, 'as law 64', 'up share of the half apex joined with half the deviation; the right side 3/4',
    lambda d: [mp.sin(mp.pi/6 + A_(d)), R('1.5')*R('0.5')], lambda d: [v30*h(d) + h30*v(d), R(3)/4], PD))
add_law(T(67, 'the direction with up share 3/4 has slope 3 over root 7', 'the slope of the half apex joined with half the deviation, and the slope 3 over root 7',
    lambda d: [mp.tan(mp.pi/6 + A_(d)), mp.tan(mp.asin(R('0.75')))], lambda d: [add(1/S(3), d), 3/S(7)], PD))
PQ = [r('0.2'), r('0.5'), r('0.8')]
def n68(q):
    u = v(q); return (3*u - 4*u**3)/(2*u*h(q))
def o68(q):
    A = 4*A_(q); return mp.sin((A + A/2)/2)/mp.sin(A/2)
add_law(T(68, 'quarter apex slope q: three quarters by the triple rule in shares, the half by the double rule', 'up share of three quarter directions over up share of two', o68, n68, PQ))
add_law(T(69, 'as law 68', 'the same ratio; the right side root 2 over 2',
    lambda q: [o68(q), (R(1)/2)/(1/mp.sqrt(2))], lambda q: [n68(q), S(2)/2], PQ))
add_law(T(70, 'as law 68; 45 and 30 degrees have exact shares', 'the same ratio; the right side root 2',
    lambda q: [o68(q), mp.sin(mp.pi/4)/mp.sin(mp.pi/6)], lambda q: [n68(q), S(2)], PQ))
PDV = [(r('1'), r('1.2'), r('1.5')), (r('1.7'), r('1.2'), r('1.5')), (r('0.6'), r('1.2'), r('1.5'))]
def o71(p):
    si, a, n = p; i = A_(si); A = A_(a)
    return mp.tan(i - A + mp.asin(n*mp.sin(A - mp.asin(mp.sin(i)/n))))
def n71(p):
    si, a, n = p; w = sub(a, slope_of_up(v(si)/n)); es = slope_of_up(n*v(w))
    return add(sub(si, a), es)
add_law(T(71, 'deviation direction', 'the deviation slope composed by slope addition from the incidence, apex and the inner directions', o71, n71, PDV))
def o72(p):
    si, a, u = p; i = A_(si); x = A_(a) - mp.asin(mp.sin(i)/u)
    return mp.cos(x)*mp.cos(i)/S((1 - u**2*mp.sin(x)**2)*(1 - mp.sin(i)**2/u**2))
def n72(p):
    si, a, u = p; w = sub(a, slope_of_up(v(si)/u))
    return h(w)*h(si)/S((1 - u**2*v(w)**2)*(1 - v(si)**2/u**2))
add_law(T(72, 'stationarity in shares', 'the same rational form with the inner direction by slope subtraction', o72, n72, PDV))
PB = [(r('0.3'), r('2')), (r('1.7'), r('1.1')), (r('5'), r('0.4'))]
add_law(T(73, 'glancing direction', 'twice the spacing times the up share', lambda p: 2*p[1]*sn(p[0]), lambda p: 2*p[1]*v(p[0]), PB))
add_law(T(74, 'glancing direction', 'spacing over up share, twice spacing over slope',
    lambda p: [p[1]/sn(p[0]), 2*p[1]/mp.tan(A_(p[0]))], lambda p: [p[1]/v(p[0]), 2*p[1]/p[0]], PB))
add_law(T(75, 'glancing direction', 'twice spacing over slope times across share, and its equal forms',
    lambda p: [2*p[1]/mp.tan(A_(p[0]))*cs(p[0]), 2*p[1]/sn(p[0])*cs(p[0])**2], lambda p: [2*p[1]/p[0]*h(p[0]), 2*p[1]/v(p[0])*h(p[0])**2], PB))
add_law(T(76, 'glancing direction', 'twice spacing over up share times one less across share squared, which is the up share squared',
    lambda p: [2*p[1]/sn(p[0]) - 2*p[1]/sn(p[0])*cs(p[0])**2, 2*p[1]/sn(p[0])*sn(p[0])**2],
    lambda p: [2*p[1]/v(p[0]) - 2*p[1]/v(p[0])*h(p[0])**2, 2*p[1]/v(p[0])*v(p[0])**2], PB))
PG = [(r('0.3'), r('0.2'), r('1.1')), (r('1.7'), r('0.9'), r('0.6')), (r('5'), r('2.5'), r('2'))]
add_law(T(77, 'two directions joined', 'twice the period times the up share of the join',
    lambda p: 2*p[2]*mp.sin(A_(p[0]) + A_(p[1])), lambda p: 2*p[2]*UPS(p[0], p[1]), PG))
add_law(N(78, 'd = 2 pi / |g|: the whole turn in the reciprocal lattice convention, an amount'))
add_law(N(79, 'plane spacing as 2 pi over a reciprocal length: the whole turn as an amount factor'))
PE = [(r('0.3'), r('0.2'), r('0.43'), r('0.5'), r('0.1')), (r('1.7'), r('0.9'), r('0.43'), r('1.2'), r('0.6')), (r('5'), r('2.5'), r('0.6'), r('3'), r('2'))]
def f80(ca, sa, cd, sd, td, ce, se, cl, sl, cb, sb, tb):
    return [(sa*ce + td*se)/ca, cd*sa*ce + sd*se, cd*ca, sd*ce - cd*se*sa,
            (sl*ce - tb*se)/cl, cb*sl*ce - sb*se, cb*cl, sb*ce + cb*se*sl]
add_law(T(80, 'rotation about the equinox', 'each component as products of up and across shares of the two directions and the obliquity',
    lambda p: f80(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), mp.tan(A_(p[1])), cs(p[2]), sn(p[2]), cs(p[3]), sn(p[3]), cs(p[4]), sn(p[4]), mp.tan(A_(p[4]))),
    lambda p: f80(h(p[0]), v(p[0]), h(p[1]), v(p[1]), p[1], h(p[2]), v(p[2]), h(p[3]), v(p[3]), h(p[4]), v(p[4]), p[4]), PE))
PH3 = [(r('0.3'), r('0.2'), r('0.8')), (r('1.7'), r('0.9'), r('1.1')), (r('5'), r('0.4'), r('0.3'))]
def f81(ch, sh, cd, sd, td, cf, sf):
    return [sh/(ch*sf - td*cf), cd*sh, cd*ch*sf - sd*cf, sf*sd + cf*cd*ch]
add_law(T(81, 'rotation about the observer', 'each component in up and across shares of hour angle, declination and latitude',
    lambda p: f81(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), mp.tan(A_(p[1])), cs(p[2]), sn(p[2])),
    lambda p: f81(h(p[0]), v(p[0]), h(p[1]), v(p[1]), p[1], h(p[2]), v(p[2])), PH3))
def f82(ch, sh, cd, sd, cf, sf): return [-sf*cd*ch + cf*sd, cd*sh]
add_law(T(82, 'rotation about the observer', 'the two arguments in shares',
    lambda p: f82(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), cs(p[2]), sn(p[2])),
    lambda p: f82(h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2])), PH3))
P83 = [(r('0.3'), r('0.2'), r('0.8'), r('0.7'), r('0.4'), r('0.5')), (r('1.7'), r('0.9'), r('1.1'), r('0.3'), r('2'), r('0.2')), (r('5'), r('0.4'), r('0.3'), r('1.2'), r('0.6'), r('1.6'))]
def f83(cL, sL, ca, sa, cd, sd, cf, sf, cA, sA, cal, sal, tal):
    M1 = [[sf, 0, -cf], [0, 1, 0], [cf, 0, sf]]; M2 = [[cL, sL, 0], [sL, -cL, 0], [0, 0, 1]]
    out = mv(M1, mv(M2, [cd*ca, cd*sa, sd]))
    return out + [sA/(cA*sf + tal*cf), cal*sA, sal*cf + cal*cA*sf, sf*sal - cf*cal*cA]
add_law(T(83, 'rotations composed', 'the matrices filled with up and across shares; the inverse components likewise',
    lambda p: f83(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), cs(p[2]), sn(p[2]), cs(p[3]), sn(p[3]), cs(p[4]), sn(p[4]), cs(p[5]), sn(p[5]), mp.tan(A_(p[5]))),
    lambda p: f83(h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2]), h(p[3]), v(p[3]), h(p[4]), v(p[4]), h(p[5]), v(p[5]), p[5]), P83))
P84 = [(r('0.3'), r('0.2'), r('0.8'), r('0.7')), (r('1.7'), r('0.9'), r('1.1'), r('0.3')), (r('5'), r('0.4'), r('0.3'), r('1.2'))]
def f84(cf, sf, cal, sal, cA, sA, cL, sL):
    M3 = [[sf, 0, cf], [0, 1, 0], [-cf, 0, sf]]; M2 = [[cL, sL, 0], [sL, -cL, 0], [0, 0, 1]]
    w = mv(M3, [cal*cA, cal*sA, sal])
    return [sf*cal*cA + cf*sal, cal*sA] + w + mv(M2, w)
add_law(T(84, 'rotations composed', 'the matrices filled with up and across shares',
    lambda p: f84(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), cs(p[2]), sn(p[2]), cs(p[3]), sn(p[3])),
    lambda p: f84(h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2]), h(p[3]), v(p[3])), P84))
def f85(cd, sd, cg, sg, cw, sw): return [sd*cg - cd*sg*cw, cd*sw, sd*sg + cd*cg*cw]
add_law(T(85, 'rotation to the galactic pole', 'each component in shares (each angle difference taken as one direction)',
    lambda p: f85(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), cs(p[2]), sn(p[2])),
    lambda p: f85(h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2])), PH3))
def f86(cb, sb, cg, sg, cm, sm): return [cb*sm, sb*cg - cb*sg*cm, sb*sg + cb*cg*cm]
add_law(T(86, 'rotation from the galactic pole', 'each component in shares',
    lambda p: f86(cs(p[0]), sn(p[0]), cs(p[1]), sn(p[1]), cs(p[2]), sn(p[2])),
    lambda p: f86(h(p[0]), v(p[0]), h(p[1]), v(p[1]), h(p[2]), v(p[2])), PH3))
add_law(N(87, 'an angle as a sum of degree amounts times sines of the anomaly (a series in the eccentricity); angles added as amounts'))
add_law(T(88, 'across shares of one and two anomaly directions', 'constants less multiples of the across share and of (1 - s^2)/(1 + s^2)',
    lambda s: R('1.00014') - R('0.01671')*cs(s) - R('0.00014')*mp.cos(2*A_(s)),
    lambda s: R('1.00014') - R('0.01671')*h(s) - R('0.00014')*(1 - s*s)/(1 + s*s), P3))
PLE = [(r('0.3'), r('0.43')), (r('1.7'), r('0.43')), (r('5'), r('0.6'))]
add_law(T(89, 'the right ascension direction', 'its slope is the obliquity across share times the longitude slope',
    lambda p: mp.tan(mp.atan(cs(p[1])*mp.tan(A_(p[0])))), lambda p: h(p[1])*p[0], PLE))
def o90(p):
    a = mp.atan2(cs(p[1])*sn(p[0]), cs(p[0])); return [mp.cos(a), mp.sin(a)]
def n90(p):
    x = h(p[0]); y = h(p[1])*v(p[0]); m = S(x*x + y*y); return [x/m, y/m]
add_law(T(90, 'the right ascension direction', 'its shares are the vector (across, obliquity across times up) divided by its length', o90, n90, PLE))
add_law(T(91, 'the declination direction', 'its up share is the product of the two up shares; slope that over the root of one less its square',
    lambda p: mp.tan(mp.asin(sn(p[1])*sn(p[0]))), lambda p: slope_of_up(v(p[1])*v(p[0])), PLE))
PLR = [(a, b, r('0.983')) for (a, b) in PLE]
add_law(T(92, 'across share', 'distance times across share', lambda p: p[2]*cs(p[0]), lambda p: p[2]*h(p[0]), PLR))
add_law(T(93, 'shares', 'distance times obliquity across share times longitude up share', lambda p: p[2]*cs(p[1])*sn(p[0]), lambda p: p[2]*h(p[1])*v(p[0]), PLR))
add_law(T(94, 'shares', 'distance times both up shares', lambda p: p[2]*sn(p[1])*sn(p[0]), lambda p: p[2]*v(p[1])*v(p[0]), PLR))
add_law(N(95, 'the obliquity given as 23.44 degrees, an amount; its slope has no exact rational-and-root form'))
add_law(N(96, 'an angle from a day count (360/365 degrees a day) and an angle proportional to a share: amounts'))
add_law(N(97, 'day counts made angles, an angle proportional to a share, and an explicit 360/pi'))
add_law(N(98, 'day counts made angles and an angle proportional to a share; degree amounts'))
PFD = [(r('0.3'), r('0.4')), (r('0.5'), r('0.8')), (r('1.2'), r('0.3'))]
add_law(T(99, 'hour angle', 'the across share of the half day is minus the product of the two slopes',
    lambda p: mp.cos(mp.acos(-mp.tan(A_(p[0]))*mp.tan(A_(p[1])))), lambda p: -p[0]*p[1], PFD))
add_law(T(100, 'slopes', 'the product of the two slopes exceeds one in size',
    lambda p: abs(mp.tan(A_(p[0]))*mp.tan(A_(p[1]))), lambda p: abs(p[0]*p[1]), PFD))
add_law(T(101, 'the opposite facing', 'half a turn on flips the across share',
    lambda s: [-cs(s), mp.cos(-mp.pi - A_(s))], lambda s: [-h(s), -h(s)], P3))
PSR = [(r('-0.0145'), r('0.8'), r('0.3')), (r('-0.1'), r('0.5'), r('-0.4')), (r('0.05'), r('1.2'), r('0.2'))]
add_law(T(102, 'shares', 'the altitude up share less the product of up shares, over the product of across shares',
    lambda p: (sn(p[0]) - sn(p[1])*sn(p[2]))/(cs(p[1])*cs(p[2])), lambda p: (v(p[0]) - v(p[1])*v(p[2]))/(h(p[1])*h(p[2])), PSR))
add_law(N(103, 'an altitude difference in degrees over 360 degrees: angles as amounts, a fraction of a day'))
PU = [(r('0.4'), r('1.2')), (r('1.7'), r('0.3')), (r('-2'), r('0.9'))]
add_law(T(104, 'a direction from components', 'the slope is the ratio of the components',
    lambda p: mp.tan(mp.atan2(p[0], p[1])), lambda p: p[0]/p[1], PU))
PBt = [(r('0.3'), r('0.1')), (r('1.7'), r('0.3')), (r('5'), r('0.6'))]
add_law(T(105, 'aberration', 'the seen slope is the up share over (speed ratio plus across share)',
    lambda p: mp.tan(mp.atan2(sn(p[0]), p[1] + cs(p[0]))), lambda p: v(p[0])/(p[1] + h(p[0])), PBt))
add_law(T(106, 'difference of two directions', 'the slope of the difference by slope subtraction',
    lambda p: mp.tan(A_(p[0]) - A_(p[1])), lambda p: sub(p[0], p[1]), P2))
add_law(T(107, 'aberration', 'the up share over the Lorentz factor (a square root) times speed ratio plus across share',
    lambda p: mp.tan(mp.atan2(sn(p[0]), (1/mp.sqrt(1 - p[1]**2))*(p[1] + cs(p[0])))), lambda p: v(p[0])/((1/S(1 - p[1]**2))*(p[1] + h(p[0]))), PBt))
def o108(p):
    t, b = p; th = 2*mp.atan(t); ph = mp.atan2(mp.sin(th), (1/mp.sqrt(1 - b*b))*(b + mp.cos(th))); return mp.tan(ph/2)
add_law(T(108, 'half directions', 'the seen half slope is the root of (1 - b)/(1 + b) times the source half slope',
    o108, lambda p: S((1 - p[1])/(1 + p[1]))*p[0], [(r('0.3'), r('0.1')), (r('0.8'), r('0.3')), (r('2'), r('0.6'))]))
add_law(T(109, 'difference of two directions', 'the up share of the difference by the subtraction rule in shares',
    lambda p: mp.sin(A_(p[0]) - A_(p[1])), lambda p: UPD(p[0], p[1]), P2))
add_law(N(110, 'the small-angle step sets the angle itself (in radians) equal to a ratio: the angle as an amount'))
add_law(N(111, 'an angle given in radians (0.00009793) and an explicit half pi: amounts'))
PBh = [(r('0.3'), r('0.1'), r('2')), (r('1.7'), r('0.3'), r('0.5')), (r('5'), r('0.6'), r('3'))]
add_law(T(112, 'aberration', 'the up share over speed ratio plus across share, with and without the common length',
    lambda p: [p[2]*sn(p[0])/(p[2]*p[1] + p[2]*cs(p[0])), sn(p[0])/(p[1] + cs(p[0]))],
    lambda p: [p[2]*v(p[0])/(p[2]*p[1] + p[2]*h(p[0])), v(p[0])/(p[1] + h(p[0]))], PBh))
PBn = [(r('0.3'), r('0.1'), r('1.33')), (r('1.7'), r('0.3'), r('1.5')), (r('5'), r('0.6'), r('1.2'))]
add_law(T(113, 'aberration in a medium', 'the up share over (index times speed ratio plus across share)',
    lambda p: sn(p[0])/(p[1]/(1/p[2]) + cs(p[0])), lambda p: v(p[0])/(p[1]*p[2] + h(p[0])), PBn))
P114 = [(r('0.9'), r('0.2'), r('0.5'), r('1.5')), (r('2'), r('0.3'), r('1.2'), r('1.33')), (r('5'), r('1'), r('3'), r('1.2'))]
add_law(T(114, 'differences of directions', 'the up shares of the two differences, by the subtraction rule',
    lambda p: [mp.sin(A_(p[0]) - A_(p[1])), p[3]*mp.sin(A_(p[2]) - A_(p[1]))], lambda p: [UPD(p[0], p[1]), p[3]*UPD(p[2], p[1])], P114))
P115 = [(r('0.3'), r('2'), r('0.1')), (r('1.7'), r('1'), r('0.4')), (r('5'), r('3'), r('1.1'))]
add_law(T(115, 'telescope geometry', 'the slope is length times up share over (travel plus length times across share)',
    lambda p: mp.tan(mp.atan2(p[1]*sn(p[0]), p[2] + p[1]*cs(p[0]))), lambda p: p[1]*v(p[0])/(p[2] + p[1]*h(p[0])), P115))
P116 = [(r('0.3'), r('1.33'), r('0.1')), (r('1.7'), r('1.5'), r('0.2')), (r('5'), r('1.2'), r('0.05'))]
def comps_o(p):
    s, n, w = p; X = (1/n)*cs(s) - (1 - 1/n**2)*w; Y = (1/n)*sn(s); return mp.atan2(Y, X)
def comps_n(p):
    s, n, w = p; X = (1/n)*h(s) - (1 - 1/n**2)*w; Y = (1/n)*v(s); return X, Y, S(X*X + Y*Y)
add_law(T(116, 'dragged light direction', 'its up share is the up component over the light speed (the root of the sum of squares)',
    lambda p: mp.sin(comps_o(p)), lambda p: comps_n(p)[1]/comps_n(p)[2], P116))
add_law(T(117, 'dragged light direction', 'its across share is the across component over the light speed',
    lambda p: mp.cos(comps_o(p)), lambda p: comps_n(p)[0]/comps_n(p)[2], P116))
add_law(T(118, 'aberration with drag', 'the up share over (speed ratio over index plus across share)',
    lambda p: mp.tan(mp.atan2(sn(p[0]), p[1]/p[2] + cs(p[0]))), lambda p: v(p[0])/(p[1]/p[2] + h(p[0])), PBn))
PW = [(r('0.3'), r('0.5')), (r('2'), r('0.1')), (r('5'), r('0.7'))]
add_law(T(119, 'a tilt direction', 'the slope is time times the gradient',
    lambda p: mp.tan(mp.atan(p[0]*p[1])), lambda p: p[0]*p[1], PW))

LAWS.sort(key=lambda L: L['n'])
