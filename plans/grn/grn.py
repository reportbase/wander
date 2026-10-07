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


def run3(seed=31, trials=4000, flux=100.0, noise=1.0, thresh=10.0):
    """Run 3 (plans/grn-plan.md): pixels one grain wide, random grid offset, no model; count the lit pixels."""
    rng = np.random.default_rng(seed)
    out = []
    for s in list(S_GRID) + [0.25, 0.5, 0.75, 0.9, 1.0, 1.1]:
        two = 0
        for _ in range(trials):
            off = rng.uniform(0, 1)
            xs = np.array([-s / 2, s / 2]) + off
            pix = np.floor(xs).astype(int)
            lo = pix.min() - 1
            img = np.zeros(pix.max() - lo + 2)
            for p in pix:
                img[p - lo] += flux
            img += rng.normal(0, noise, img.size)
            two += int((img > thresh).sum() >= 2)
        p = two / trials
        exp = min(s, 1.0)
        se = math.sqrt(max(exp * (1 - exp), 1e-12) / trials)
        out.append((s, p, exp, (p - exp) / se if exp < 1 else (0.0 if p == 1 else float('inf'))))
    return sorted(out)


def look(s, rng, h=1.0):
    """One look by the model-free reader: two point stars s apart, a pixel grid of width h at a random offset.
    Returns how many pixels are lit (noise far below the threshold, as in run 3)."""
    off = rng.uniform(0, h)
    return len(set(np.floor((np.array([0.0, s]) + off) / h).astype(int)))


def span_pixels(s, rng, h=1.0):
    """Pixels lit by a continuous span of length s (for P2: the mean is 1 + s)."""
    off = rng.uniform(0, h)
    return int(math.floor((s + off) / h)) + 1


def run4(seed=41, trials=20000):
    rng = np.random.default_rng(seed)
    below, past, slider = [], [], []
    for s in [0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9]:
        n = []
        for _ in range(trials):
            k = 1
            while look(s, rng) < 2:
                k += 1
            n.append(k)
        n = np.array(n, float)
        below.append((s, n.mean(), 1 / s, (n.mean() - 1 / s) / (n.std(ddof=1) / math.sqrt(trials))))
        m, stop = [], []
        for _ in range(trials):
            h, k = 1.0, 1
            while look(s, rng, h) < 2:
                h, k = h / 2, k + 1
            m.append(k)
            stop.append(s / h)
        slider.append((s, float(np.mean(m)), math.log2(1 / s) + 2, float(np.min(stop)), float(np.max(stop))))
    for s in [1.0, 1.5, 2.0, 3.3, 5.0, 8.0]:
        px = np.array([span_pixels(s, rng) for _ in range(trials)], float)
        two = np.mean([look(s, rng) >= 2 for _ in range(trials)])
        past.append((s, px.mean(), 1 + s, (px.mean() - 1 - s) / max(px.std(ddof=1) / math.sqrt(trials), 1e-12), two))
    return below, past, slider


def run5(seed=53, trials=20000):
    """Run 5 (plans/grn-plan.md): each look charged one unit per grain the system spans; cost of the first sure "two"."""
    rng = np.random.default_rng(seed)
    out = []
    for s in [0.1, 0.2, 0.3, 0.5, 0.7, 0.85, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0]:
        costs = np.empty(trials)
        for i in range(trials):
            c = 0
            while True:
                n = span_pixels(s, rng)
                c += n
                if n >= 2:
                    break
            costs[i] = c
        pred = (1 + s) * max(1.0, 1 / s)
        out.append((s, costs.mean(), pred, (costs.mean() - pred) / (costs.std(ddof=1) / math.sqrt(trials))))
    return out


def steer(s0, rng, k=3, cap=10000):
    """Run 6: start at s0, turn h by the lit-pixel count of a unit span; return (looks, pixels read, final s)."""
    s, ok, looks, px = s0, 0, 0, 0
    while looks < cap:
        n = span_pixels(s, rng)
        looks += 1
        px += n
        if n == 1:
            s, ok = s * 2, 0
        elif n >= 4:
            s, ok = s / 2, 0
        else:
            ok += 1
            if ok == k:
                return looks, px, s
    return looks, px, s


def run6(seed=61, trials=20000):
    rng = np.random.default_rng(seed)
    out = []
    for s0 in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]:
        row = {'s0': s0, 'bound': abs(math.log2(s0)) + 5, 'fixed': (1 + s0) * max(1, 1 / s0)}
        for k in (3, 1):
            r = np.array([steer(s0, rng, k) for _ in range(trials)], float)
            fs = r[:, 2]
            row[k] = {'looks': r[:, 0].mean(), 'px': r[:, 1].mean(), 'in': np.mean((fs >= 0.5) & (fs <= 3)),
                      'low': np.mean(fs < 0.5)}
        out.append(row)
    return out


def parallel_flux(theta, rng, flux):
    img = flux * spots(theta) + rng.normal(0, PIX_SD, PIX.size)
    f = (TEMPL @ img) / TT
    rss = (img * img).sum() - f * (TEMPL @ img)
    return THETAS[int(np.argmin(rss))]


def run7(seed=77, trials=400):
    """Run 7 (plans/grn-plan.md): the parallel reader of runs 1-2 at four light levels."""
    rng = np.random.default_rng(seed)
    grid = np.exp(np.linspace(math.log(0.02), math.log(5), 28))
    out = {}
    for flux in (25.0, 100.0, 400.0, 1600.0):
        rows = []
        for s in grid:
            pe = np.array([parallel_flux(s, rng, flux) for _ in range(trials)])
            rows.append((s, float(np.sqrt(np.mean((pe - s) ** 2)))))
        plateau = float(np.mean([a for s, a in rows if s >= 2]))
        knee = max((s for s, a in rows if a >= 2 * plateau), default=None)
        # resolution limit: the smallest s from which on the error stays under s/2, log-interpolated at the crossing
        res = None
        for (s0, a0), (s1, a1) in zip(rows[:-1], rows[1:]):
            if a0 >= s0 / 2 and a1 < s1 / 2:
                f0, f1 = math.log(a0 / (s0 / 2)), math.log(a1 / (s1 / 2))
                res = math.exp(math.log(s0) + f0 / (f0 - f1) * (math.log(s1) - math.log(s0)))
        out[flux] = (plateau, knee, res)
    return out
