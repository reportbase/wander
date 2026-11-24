# FCL run 2b: C4' (the ball's pull by its shells, no gap). See plans/fcl-plan.md.
# Run from the repository root: python3 runs/fcl/fcl2b.py
from mpmath import mp, mpf, pi, quad, sin, cos

mp.dps = 20


def shell_pull(x, rp):
    def f(th):
        den = x * x + rp * rp - 2 * x * rp * cos(th)
        if den == 0:                       # a node rounded onto the shell through the point: the integrand's limit there
            return 1 / (4 * x * x)
        return (x - rp * cos(th)) * sin(th) / 2 / den ** mpf("1.5")
    return quad(f, [0, pi / 16, pi / 4, pi / 2, pi])


def ball_pull(x):
    dens = lambda rp: 3 * rp * rp
    g = lambda rp: dens(rp) * shell_pull(x, rp)
    if x < 1:
        # the end points are never evaluated by the quadrature, so the shell through the point is approached, not met
        return quad(g, [0, x / 2, x]) + quad(g, [x, (x + 1) / 2, 1])
    return quad(g, [0, mpf(1) / 2, 1])


worst = mpf(0)
for xs in ("0.2", "0.5", "0.9", "1.1", "2", "5"):
    x = mpf(xs)
    got, want = ball_pull(x), (x if x < 1 else 1 / x ** 2)
    print(f"  C4' x = {xs}: pull {mp.nstr(got, 14)} against {mp.nstr(want, 14)}")
    worst = max(worst, abs(got - want))
print(f"C4': {'not killed' if worst < mpf(10) ** -10 else 'KILLED'} (largest miss {mp.nstr(worst, 3)})")
