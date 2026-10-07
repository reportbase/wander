"""GRN: serial or parallel is set by the reader's grain. See plans/grn-plan.md (prediction and kill written before this).

A binary of two equal stars, separation a, at distance D, apparent separation theta = a/D; the reader's grain h = 1, so
s = theta. The parallel reader fits one image; the serial reader fits the velocity difference over one orbit.

    python3 plans/grn/grn.py
"""
import math

import numpy as np

H = 1.0                       # the grain
SIG = H / 2                   # each star's spot width
PIX = np.arange(-12, 12.0001, H / 4)  # pixel centres, pixels H/4 wide
FLUX, PIX_SD = 100.0, 1.0     # light per star, noise per pixel
THETAS = np.linspace(0, 12, 4801)  # the parallel reader's search grid for the separation
N_EPOCH, SERIAL_REL = 20, 0.05
S_GRID = np.exp(np.linspace(math.log(0.1), math.log(5), 15))
TRIALS = 300


def spots(theta):
    g = lambda c: np.exp(-0.5 * ((PIX - c) / SIG) ** 2) / (SIG * math.sqrt(2 * math.pi)) * (H / 4)
    return g(-theta / 2) + g(theta / 2)


# the parallel reader's templates, one per candidate separation (flux fitted linearly for each)
TEMPL = np.array([spots(t) for t in THETAS])
TT = (TEMPL * TEMPL).sum(1)


def parallel(theta, rng):
    img = FLUX * spots(theta) + rng.normal(0, PIX_SD, PIX.size)
    f = (TEMPL @ img) / TT
    rss = (img * img).sum() - f * (TEMPL @ img)
    return THETAS[int(np.argmin(rss))]


def serial(a, rng, omega=2 * math.pi):
    t = np.arange(N_EPOCH) / N_EPOCH
    x = np.sin(omega * t)
    K = a * omega
    sd = SERIAL_REL * K * math.sqrt(N_EPOCH / 2)
    dv = K * x + rng.normal(0, sd, N_EPOCH)
    return float(x @ dv / (x @ x)) / omega


def rms_rel(est, true):
    est = np.asarray(est)
    return float(np.sqrt(np.mean((est / true - 1) ** 2)))


def run(seed=5):
    rng = np.random.default_rng(seed)
    rows = []
    for s in S_GRID:
        pe, se = [], []
        for _ in range(TRIALS):
            a, D = 1.0, 1.0 / s          # theta = a/D = s (grain 1)
            pe.append(parallel(a / D, rng) * D)
            se.append(serial(a, rng))
        rows.append((s, rms_rel(pe, 1.0), rms_rel(se, 1.0)))
    return rows


def sanity(s=0.8, seed=9):
    """Three systems of different size, at distances giving the same s: the parallel reader cannot tell them apart."""
    rng = np.random.default_rng(seed)
    out = []
    for a in (0.1, 1.0, 10.0):
        D = a / (s * H)
        out.append(rms_rel([parallel(a / D, rng) * D for _ in range(TRIALS)], a))
    return out


if __name__ == '__main__':
    rows = run()
    p5 = rows[-1][1]
    print(f'{"s":>6} {"parallel":>9} {"serial":>8}   (RMS relative error in a)')
    for s, p, q in rows:
        print(f'{s:6.3f} {p:9.4f} {q:8.4f}' + ('   <- parallel wins' if p < q else ''))
    # the knee: where the parallel error first reaches twice its value at s = 5, coming down from s = 5 (log-interpolated)
    knee = None
    for (s1, p1, _), (s0, p0, _) in zip(rows[::-1][:-1], rows[::-1][1:]):
        if p0 >= 2 * p5 > p1:
            w = (math.log(2 * p5) - math.log(p1)) / (math.log(p0) - math.log(p1))
            knee = math.exp(math.log(s1) + w * (math.log(s0) - math.log(s1)))
            break
    ser = [q for _, _, q in rows]
    cross = None
    for (s0, p0, q0), (s1, p1, q1) in zip(rows[:-1], rows[1:]):
        if p0 >= q0 and p1 < q1:
            cross = (s0, s1)
            break
    print(f'\nparallel error at s = 5: {p5:.4f}; knee (twice that): s = {knee:.3f}' if knee else '\nno knee found')
    print(f'serial error across s: {min(ser):.4f} to {max(ser):.4f} (spread {100 * (max(ser) / min(ser) - 1):.1f}%)')
    print(f'switch: parallel first wins between s = {cross[0]:.3f} and {cross[1]:.3f}' if cross else 'no switch')
    print('sanity, s = 0.8, a = 0.1, 1, 10: ' + ', '.join(f'{x:.4f}' for x in sanity()))


def run2(seed=23, trials=1000):
    """Run 2 (plans/grn-plan.md): the parallel reader's absolute error in theta, in grains; the serial reader's trend."""
    rng = np.random.default_rng(seed)
    rows = []
    for s in S_GRID:
        pe = np.array([parallel(s, rng) for _ in range(trials)])
        se = np.array([serial(1.0, rng) for _ in range(trials)])
        rows.append((s, float(np.sqrt(np.mean((pe - s) ** 2))), rms_rel(se, 1.0), rms_rel(pe, s)))
    plateau = float(np.mean([a for s, a, _, _ in rows if s >= 2]))
    knee = max((s for s, a, _, _ in rows if a >= 2 * plateau), default=None)
    ls = np.log([r[0] for r in rows])
    lq = np.log([r[2] for r in rows])
    slope = float(np.polyfit(ls, lq, 1)[0])
    cross = next((r[0] for r in rows if r[3] < r[2]), None)
    return rows, plateau, knee, slope, cross
