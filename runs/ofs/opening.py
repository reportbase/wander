"""How shapes open into the fisheye: the lay, not the shape, makes the Cauchy.

For observation-from-somewhere.md §7.4. Each shape is read from its centre as v/h = |y|/|x|, the tangent of the
direction, and laid two ways:
  - evenly by direction (equal steps of turn), the paper's sweep;
  - evenly along its own outline (equal steps of arc length).
Four numbers describe an opening (after SPN §2.4 and v-and-h.md item 331, whose 73-shape run used another page's
shape library; this script repeats the method on shapes defined exactly):
  corner  P(s < 1), the share before the corner
  middle  the median of s
  head    P(s < e)/e at e = 0.025: how the readings cross home
  tail    s·P(S > s) at s = 40: how they cross toward the horizon
For the circle these are 0.5, 1, 2/π and 2/π.
Prediction, written before running: by direction every shape gives (0.5, 1, 0.637, 0.637), the circle's, since the
reading is the direction alone; along the outline, shapes unchanged when x and y are swapped keep corner 0.5 and
middle 1 (the flip) and differ only in head and tail; a shape not so symmetric moves its corner and middle too.
Run: python3 runs/ofs/opening.py
"""
import numpy as np

N = 2_000_000          # points along each outline
E, S = 0.025, 40.0     # where the head and the tail are read

def outline(name):
    t = np.linspace(0.0, 2*np.pi, 400_001)
    if name == "circle":
        x, y = np.cos(t), np.sin(t)
    elif name == "square":                       # |x| + ... as a polygon: corners (±1, ±1)
        k = np.linspace(0, 4, 400_001)
        p = np.array([(1, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)], float)
        i = np.minimum(k.astype(int), 3); f = k - i
        xy = p[i] + (p[i + 1] - p[i]) * f[:, None]
        x, y = xy[:, 0], xy[:, 1]
    elif name == "astroid":
        x, y = np.cos(t)**3, np.sin(t)**3
    elif name == "ellipse, b = 2":               # twice as tall as wide: not unchanged when x and y swap
        x, y = np.cos(t), 2*np.sin(t)
    return x, y

def even_along(x, y, n):
    d = np.hypot(np.diff(x), np.diff(y)); c = np.concatenate([[0], np.cumsum(d)])
    u = np.linspace(0, c[-1], n, endpoint=False)
    return np.interp(u, c, x), np.interp(u, c, y)

def four(s):
    s = np.sort(s)
    return (np.mean(s < 1), np.median(s), np.mean(s < E)/E, S*np.mean(s > S))

print(f"{'shape':16} {'laid':10} {'corner':>7} {'middle':>7} {'head':>7} {'tail':>7}")
for name in ["circle", "square", "astroid", "ellipse, b = 2"]:
    x, y = outline(name)
    xa, ya = even_along(x, y, N)
    with np.errstate(divide="ignore"):
        s_out = np.abs(ya)/np.abs(xa)
    th = (np.arange(N) + 0.5) * 2*np.pi/N          # by direction: the reading is the direction's tangent
    s_dir = np.abs(np.tan(th))
    for laid, s in (("direction", s_dir), ("outline", s_out)):
        c, m, h, tl = four(s)
        print(f"{name:16} {laid:10} {c:7.4f} {m:7.4f} {h:7.3f} {tl:7.3f}")
