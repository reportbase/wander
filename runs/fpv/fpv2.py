"""FPV run 2: flying at the focus with H locked on it (plans/fpv-plan.md, run 2).
Run from the repository's root: python3 runs/fpv/fpv2.py"""
import mpmath as mp

mp.mp.dps = 40
pi, ok = mp.pi, True


def say(code, good, note):
    global ok
    ok = ok and good
    print(f"  {'ok  ' if good else 'FAIL'} {code}: {note}")


u, K = mp.mpf(3), 1024
d0 = mp.mpf(1000)
dist = lambda t: d0 - u * t                       # the target straight ahead
def thing(t, D0, beta):                           # a thing fixed in the world at D0, angle beta off the line of flight
    x, y = D0 * mp.cos(beta) - u * t, D0 * mp.sin(beta)
    return mp.sqrt(x * x + y * y)
lvl = lambda t, D0, beta: mp.log(thing(t, D0, beta) / dist(t))
adr = lambda t, D0, beta: (2 / pi) * mp.atan(thing(t, D0, beta) / dist(t))

print("A1, the level flow")
worst = 0
for D0, beta, t in [(5000, 0.3, 50), (2e4, 1.1, 120), (300, 0.0, 10), (800, 2.5, 200)]:
    D0, beta, t = mp.mpf(D0), mp.mpf(beta), mp.mpf(t)
    num = mp.diff(lambda tt: lvl(tt, D0, beta), t)
    D, d = thing(t, D0, beta), dist(t)
    cosb = (D0 * mp.cos(beta) - u * t) / D
    worst = max(worst, abs(num - (u / d - u * cosb / D)))
say("A1", worst < mp.mpf(10) ** -20, f"dx/dt = u/d - u cos(beta)/D at four things (worst {mp.nstr(worst, 3)})")
t = mp.mpf(100); tau = dist(t) / u
far = [mp.diff(lambda tt: lvl(tt, mp.mpf(10) ** k, mp.mpf('0.2')), t) * tau for k in (5, 7, 9, 12)]
say("A1", abs(far[-1] - 1) < mp.mpf(10) ** -8 and all(abs(far[i + 1] - 1) < abs(far[i] - 1) for i in range(3)),
    "far beyond the focus dx/dt -> 1/tau: " + ", ".join(mp.nstr(f, 12) for f in far) + " tau^-1 at D = 1e5, 1e7, 1e9, 1e12")
near = mp.diff(lambda tt: lvl(tt, mp.mpf(400), mp.mpf(0)), t)
say("A1", near < 0, f"a thing on the line nearer than the focus slides toward home: dx/dt = {mp.nstr(near * tau, 6)}/tau")

print("\nA2, the address flow")
worst = 0
for D0, beta in [(5000, 0.3), (2e4, 1.1), (300, 0.0), (1500, 0.05)]:
    D0, beta = mp.mpf(D0), mp.mpf(beta)
    num = mp.diff(lambda tt: adr(tt, D0, beta), t)
    x = lvl(t, D0, beta)
    want = (1 / pi) * mp.sech(x) * mp.diff(lambda tt: lvl(tt, D0, beta), t)
    worst = max(worst, abs(num - want))
say("A2", worst < mp.mpf(10) ** -20, f"da/dt = (1/pi) sech(x) dx/dt (worst {mp.nstr(worst, 3)})")
rates = [(x, K * (1 / pi) * mp.sech(x) / tau) for x in (0, 1, 2, 4)]
say("A2", rates[0][1] == max(r for _, r in rates), "for one level rate 1/tau, cells a unit time: " +
    ", ".join(f"x = {x}: {mp.nstr(r, 5)}" for x, r in rates) + f"  (K/(pi tau) = {mp.nstr(K / (pi * tau), 5)}, tau = {mp.nstr(tau, 4)})")

print("\nA3, the focus stays put")
dev = max(abs((2 / pi) * mp.atan(dist(tt) / dist(tt)) - mp.mpf(1) / 2) for tt in (0, 50, 200, 330))
say("A3", dev < mp.mpf(10) ** -12, f"the target's address at t = 0, 50, 200, 330: off 1/2 by at most {mp.nstr(dev, 3)}")

print("\nA4, halving")
th = d0 / (2 * u)
say("A4", abs(th - (d0 / u) / 2) < mp.mpf(10) ** -30, f"d0 to d0/2 takes {mp.nstr(th, 6)} = tau0/2 = {mp.nstr(d0 / u / 2, 6)}")
D0 = mp.mpf(10) ** 15
dx = lvl(th, D0, mp.mpf('0.3')) - lvl(0, D0, mp.mpf('0.3'))
say("A4", abs(dx - mp.log(2)) < mp.mpf(10) ** -10, f"a thing far beyond moves {mp.nstr(dx, 12)} nats over that halving (ln 2 = {mp.nstr(mp.log(2), 12)})")

print("\nALL NOT KILLED" if ok else "\nSOME KILLED")
