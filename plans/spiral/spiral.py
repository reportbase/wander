"""The reading as a spiral: checks and the figure behind plans/horizon-recursion.md.

    python3 plans/spiral/spiral.py            numbers
    python3 plans/spiral/spiral.py --svg OUT   also writes the figure
"""
import math
import sys

import numpy as np

P = math.pi


def theta_octaves(s, r=2.0):
    """The reading's turn, octave by octave: each octave (c/r to rc round its corner c = r^(2n)) is one quarter turn,
    read by the one projective map sending 1/r, 1 and r to 0, 1 and inf, then the turn. Returns radians."""
    s = np.asarray(s, float)
    n = np.floor(np.log(s * r) / np.log(r * r))          # which octave: c/r <= s < rc
    c = (r * r) ** n
    x = s / c
    rho = (r * x - 1) / (r - x)
    g = (2 / P) * np.arctan(rho)
    return (P / 2) * (n + g)


def theta_spiral(s, r=2.0):
    """The exact logarithmic spiral through the same corners: a quarter turn per factor r², the corners at 45°."""
    return (P / 2) * (np.log(np.asarray(s, float)) / np.log(r * r) + 0.5)


def theta_one_sweep(s):
    """One bounded sweep for the whole reading (no recursion): the turn of s itself, 0 to 90° from home to horizon."""
    return np.arctan(np.asarray(s, float))


def checks():
    S = np.exp(np.linspace(math.log(4.0 ** -6), math.log(4.0 ** 6), 400001))
    for r in (2.0, 3.0, (1 + 5 ** 0.5) / 2):
        T = theta_octaves(S, r)
        eq = np.max(np.abs(theta_octaves(S * r * r, r) - T - P / 2))
        w = T - theta_spiral(S, r)
        inside = np.log(S) < np.log(S[-1]) - math.log(r * r)          # where one octave out is still sampled
        per = np.max(np.abs(np.interp(np.log(S) + math.log(r * r), np.log(S), w) - w)[inside])
        mono = bool(np.all(np.diff(T) > 0))
        print(f'r = {r:.3f}: a factor r² turns 90° to {eq:.1e}; increasing everywhere: {mono}; '
              f'gap from the exact spiral periodic (one octave) to {per:.1e}, '
              f'at most {np.max(np.abs(w)) / (P / 2):.4f} of an octave ({math.degrees(np.max(np.abs(w))):.2f}°); '
              f'corners on the spiral: {np.max(np.abs(theta_octaves(np.array([(r*r)**k for k in range(-3,4)]), r) - theta_spiral(np.array([(r*r)**k for k in range(-3,4)]), r))):.1e}')
    # the flip: s -> 1/s mirrors the turn about the corner's 45°: theta(1/s) = 90° - theta(s) on the reader's own octave
    s0 = np.exp(np.linspace(math.log(0.5) + 1e-9, math.log(2) - 1e-9, 10001))
    print(f'flip on the reader\'s own octave: theta(1/s) + theta(s) = 90° to {np.max(np.abs(theta_octaves(1/s0) + theta_octaves(s0) - P/2)):.1e}')
    # one sweep crushes the far octaves
    print('one bounded sweep (no recursion): the turn each octave out gets, in degrees:',
          [round(math.degrees(float(theta_one_sweep(2 * 4 ** n) - theta_one_sweep(0.5 * 4 ** n))), 3) for n in range(0, 6)])
    print('octave by octave (recursion): every octave out gets 90°')
    # the growth rate: ln s = k * theta for the exact spiral, k = ln(r²)/(π/2); k = 0 is the circle
    for r in (2.0, 3.0):
        print(f'exact spiral for r = {r:g}: ln s = {math.log(r*r)/(P/2):.4f} · θ − {math.log(r*r)/2:.4f}  (×{r*r:g} each quarter turn, ×{r**8:g} each full turn)')


def svg(out):
    W, H = 900, 440
    cx, cy, R = 250, 225, 23.0          # R px per unit of s (true scale: ×4 each quarter turn)
    surf, ink, ink2, grid = '#fcfcfb', '#1f1f1e', '#6b6a64', '#e4e3dd'
    c_circ, c_spir, c_read = '#1baf7a', '#2a78d6', '#eb6834'
    sup = str.maketrans('-0123456789', '⁻⁰¹²³⁴⁵⁶⁷⁸⁹')
    def pts(th, rad):
        return ' '.join(f'{cx + R * q * math.cos(t):.2f},{cy - R * q * math.sin(t):.2f}' for t, q in zip(th, rad))
    S = np.exp(np.linspace(math.log(4.0 ** -3), math.log(8.0), 3000))
    Tr, Ts = theta_octaves(S), theta_spiral(S)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="ui-monospace, Menlo, monospace" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="{surf}"/>',
         f'<text x="20" y="28" fill="{ink}" font-size="14">The reading as a spiral: one quarter turn per octave</text>',
         f'<text x="20" y="46" fill="{ink2}">true scale, r = 2: the radius (the reading s) grows ×4 each quarter turn</text>']
    for k in range(8):                      # the quarter-turn spokes, recessive
        a = k * P / 4
        o.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + 195 * math.cos(a):.1f}" y2="{cy - 195 * math.sin(a):.1f}" stroke="{grid}" stroke-width="1"/>')
    th = np.linspace(0, 2 * P, 200)
    o.append(f'<polyline points="{pts(th, np.ones_like(th))}" fill="none" stroke="{c_circ}" stroke-width="2" stroke-dasharray="5 4"/>')
    o.append(f'<polyline points="{pts(Ts, S)}" fill="none" stroke="{c_spir}" stroke-width="2"/>')
    o.append(f'<polyline points="{pts(Tr, S)}" fill="none" stroke="{c_read}" stroke-width="2"/>')
    for k in range(-3, 2):                  # the corners, at 45° + k·90°, radius 4^k
        q = 4.0 ** k
        t = P / 4 + k * P / 2
        o.append(f'<circle cx="{cx + R * q * math.cos(t):.2f}" cy="{cy - R * q * math.sin(t):.2f}" r="4" fill="{surf}" stroke="{ink}" stroke-width="1.5"/>')
    ly = H - 70                              # legend: a line sample beside each name
    items = [(c_read, '', 'situation 3: the reading, octave by octave (a quarter turn each)'),
             (c_spir, '', 'the exact logarithmic spiral through the same corners'),
             (c_circ, ' stroke-dasharray="5 4"', 'situations 1 and 2: the circle (no horizon, no growth)')]
    for i, (c, dash, label) in enumerate(items):
        y = ly + 18 * i
        o.append(f'<line x1="20" y1="{y - 4}" x2="44" y2="{y - 4}" stroke="{c}" stroke-width="2"{dash}/>')
        o.append(f'<text x="52" y="{y}" fill="{ink}">{label}</text>')
    o.append(f'<circle cx="32" cy="{ly + 50}" r="4" fill="{surf}" stroke="{ink}" stroke-width="1.5"/>')
    o.append(f'<text x="52" y="{ly + 54}" fill="{ink2}">corners, at 45° + 90°·n and radius 4ⁿ</text>')
    # right panel: the gap between them, against octaves
    x0, x1, ymid = 600, 870, 190
    o.append(f'<text x="{x0 - 40}" y="96" fill="{ink}">The reading less the exact spiral, in degrees</text>')
    o.append(f'<text x="{x0 - 40}" y="114" fill="{ink2}">repeats each octave; 0 at corners and edges</text>')
    L = np.linspace(-3, 1, 2000)
    Sw = 4.0 ** L
    wd = np.degrees(theta_octaves(Sw) - theta_spiral(Sw))
    ys = 9.0                                 # px per degree
    for d in (-5, 0, 5):
        o.append(f'<line x1="{x0}" y1="{ymid - d * ys:.1f}" x2="{x1}" y2="{ymid - d * ys:.1f}" stroke="{grid}" stroke-width="1"/>')
        o.append(f'<text x="{x0 - 8}" y="{ymid - d * ys + 4:.1f}" fill="{ink2}" text-anchor="end">{d:+d}°</text>' if d else f'<text x="{x0 - 8}" y="{ymid + 4}" fill="{ink2}" text-anchor="end">0°</text>')
    px = lambda l: x0 + (l + 3) / 4 * (x1 - x0)
    o.append('<polyline points="' + ' '.join(f'{px(l):.1f},{ymid - w * ys:.1f}' for l, w in zip(L, wd)) + f'" fill="none" stroke="{c_read}" stroke-width="2"/>')
    for k in range(-3, 2):
        o.append(f'<text x="{px(k):.1f}" y="{ymid + 70}" fill="{ink2}" text-anchor="middle">4{str(k).translate(sup)}</text>')
    o.append(f'<text x="{(x0 + x1) / 2:.0f}" y="{ymid + 90}" fill="{ink2}" text-anchor="middle">the reading s (corners at powers of 4)</text>')
    o.append(f'<text x="{x0 - 40}" y="{ymid + 122}" fill="{ink2}">at most {np.max(np.abs(wd)):.2f}°, 0.053 of an octave</text>')
    o.append('</svg>')
    open(out, 'w').write('\n'.join(o) + '\n')
    print('wrote', out)


if __name__ == '__main__':
    checks()
    if '--svg' in sys.argv:
        svg(sys.argv[sys.argv.index('--svg') + 1])
