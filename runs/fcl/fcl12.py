# FCL run 12: observation's depth beside gravity's (plans/fcl-plan.md, "Run 12").
# Run from the repository's root: python3 runs/fcl/fcl12.py
from mpmath import mp, mpf, quad, sqrt, atan, pi, cosh, log, sin, cos
mp.dps = 40
def lookShare(d, H): return 2 / pi * atan(d / H)          # the thumb's lay along a direction (the blueprint's formula)

print("Z1: a cone of even matter from a to b, apex at the place: share of its pull from within d")
a, b = mpf(2), mpf(11)
worst = mpf(0)
for slope in (mpf(1) / 100, mpf(1) / 4, mpf(1)):
    th = atan(slope)
    def pull(d):   # Newton's integrand with r^2 written out: rho * (r^2 sin t dt dphi dr) * cos t / r^2
        return quad(lambda r: quad(lambda t: 2 * pi * (r * r) * sin(t) * cos(t) / (r * r), [0, th]), [a, d])
    tot = pull(b)
    for d in (3, 5, mpf(13) / 2, 8, 10):
        dev = abs(pull(mpf(d)) / tot - (mpf(d) - a) / (b - a)); worst = max(worst, dev)
print("  worst departure from (d - a)/(b - a) over 3 widths x 5 depths: %s" % mp.nstr(worst, 3))
print("  half the pull within d = %s (the middle of the matter)" % mp.nstr((a + b) / 2, 5))

print("\nZ2: whose the half point is")
for (aa, bb, H) in ((2, 11, 1), (6, 33, 1), (2, 11, 3)):
    print("  matter %s..%s, thumb %s: pull's half point %s, look's half point %s (share there %s)"
          % (aa, bb, H, mp.nstr(mpf(aa + bb) / 2, 5), H, mp.nstr(lookShare(mpf(H), mpf(H)), 5)))

print("\nZ3: the flat lay d/L and an exchange d <-> c^2/d")
L = mpf(1); F = lambda d: min(max(d / L, mpf(0)), mpf(1))
best = (mpf(9), None)
N = 2000
for i in range(1, N):
    al = mpf(i) / N; c = al * L; lo = c * c / L
    w = max(abs(F(d) + F(c * c / d) - 1) for d in [lo + (L - lo) * mpf(j) / 400 for j in range(401)])
    if w < best[0]: best = (w, al)
print("  least worst departure %s at c/L = %s   (3 - 2 sqrt 2 = %s, sqrt 2 - 1 = %s)"
      % (mp.nstr(best[0], 6), mp.nstr(best[1], 5), mp.nstr(3 - 2 * sqrt(2), 6), mp.nstr(sqrt(2) - 1, 5)))
H = mpf(7) / 3
print("  the look's lay at c = H: worst |F(d) + F(H^2/d) - 1| = %s"
      % mp.nstr(max(abs(lookShare(d, H) + lookShare(H * H / d, H) - 1) for d in [mpf(j) / 10 for j in range(1, 300)]), 3))

print("\nZ4: scaling")
col = lambda dens, a, b: dens * (b - a)
for k in (mpf(3), mpf(1) / 7):
    c0 = col(mpf(5), a, b)
    print("  k = %s: density kept, column x %s (k = %s); masses kept, x %s (1/k^2 = %s); look's share moved by %s"
          % (mp.nstr(k, 4), mp.nstr(col(mpf(5), k * a, k * b) / c0, 8), mp.nstr(k, 8),
             mp.nstr(col(mpf(5) / k ** 3, k * a, k * b) / c0, 8), mp.nstr(1 / k ** 2, 8),
             mp.nstr(abs(lookShare(k * 4, k * H) - lookShare(mpf(4), H)), 3)))

print("\nZ5: depth from two pull strengths a step apart along the line")
B = mpf(1)
for x in (mpf(1) / 10, 1, 10, 100):
    d = mpf(x) * B; errs = []
    for GM in (mpf(1) / 1000, 1, 1000):
        rho = (GM / d ** 2) / (GM / (d + B) ** 2); errs.append(abs(1 / (sqrt(rho) - 1) - mpf(x)))
    rho = ((d + B) / d) ** 2; eps = mpf(10) ** -6
    sens = abs(1 / (sqrt(rho * (1 + eps)) - 1) - mpf(x)) / mpf(x) / eps
    look = cosh(log(2 * mpf(x)))
    print("  x = %-5s depth off by %s; sensitivity %s against (x+1)/2 = %s (ratio %s); two looks' cosh(ln 2x) = %s"
          % (mp.nstr(mpf(x), 4), mp.nstr(max(errs), 3), mp.nstr(sens, 8), mp.nstr((mpf(x) + 1) / 2, 8),
             mp.nstr(sens / ((mpf(x) + 1) / 2), 8), mp.nstr(look, 6)))
xs = [mpf(10) ** (mpf(j) / 20 - 2) for j in range(101)]
ss = [(x + 1) / 2 for x in xs]
print("  (x+1)/2 increasing at every step over x = 0.01..1000: %s" % all(ss[i] < ss[i + 1] for i in range(100)))

print("\nZ6: depth from two pull directions a step across")
def pullAt(px, masses):
    gx = gy = mpf(0)
    for (mx, my, m) in masses:
        dx, dy = mx - px, my; r3 = (dx * dx + dy * dy) ** mpf(1.5); gx += m * dx / r3; gy += m * dy / r3
    return gx, gy
def cross(bb, masses):          # two places at (-bb, 0) and (bb, 0); each pull direction's slope across over along
    g1 = pullAt(-bb, masses); g2 = pullAt(bb, masses)
    s1 = g1[0] / g1[1]; s2 = -g2[0] / g2[1]        # inward slopes, as the two looks' 1/s
    return 2 * bb / (s1 + s2)
d = mpf(9)
print("  (a) one mass at depth 9, off the axis by 2: crossing depth off by %s"
      % mp.nstr(abs(cross(mpf(1) / 2, [(mpf(2), d, mpf(5))]) - d), 3))
for name, lay in (("across", lambda a: [(-a, d, 1), (a, d, 1)]), ("along", lambda a: [(0, d - a, 1), (0, d + a, 1)])):
    for q in (10, 20, 40):
        aa = d / q; off = cross(aa / 2, lay(aa)) / d - 1
        print("  (b) pair %s, d/a = %d: crossing off the centre by %s; over 3(a/d)^2: %s"
              % (name, q, mp.nstr(off, 6), mp.nstr(off / (3 * (aa / d) ** 2), 6)))
aa = d / 10
print("  two looks at one mass of the pair cross on it: off by %s" % mp.nstr(abs(cross(aa / 2, [(aa, d, 1)]) - d), 3))

print("\nZ7: the ball's exchange")
R = mpf(3); g = lambda r: r / R if r <= R else (R / r) ** 2
print("  worst |g(R^2/r) - g(r)^2| inside: %s"
      % mp.nstr(max(abs(g(R * R / r) - g(r) ** 2) for r in [R * mpf(j) / 6 for j in range(1, 6)]), 3))
print("  the look: near reading d/H against far reading H/d' at d' = H^2/d: worst difference %s"
      % mp.nstr(max(abs(dd / H - H / (H * H / dd)) for dd in [H * mpf(j) / 6 for j in range(1, 6)]), 3))
