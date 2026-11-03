"""TXT run 4: the report and the verdicts (plans/txt-plan.md, run 4).

    python3 runs/txt/txt4_report.py <txt4.json> > runs/txt/txt-run4.txt
"""
import sys, json, math
import tiktoken

E = tiktoken.get_encoding('o200k_base')
R = json.load(open(sys.argv[1]))
tok = lambda t: len(E.encode(t)) if t else None
k_ = lambda ok: 'not killed' if ok else 'KILLED'


def slope(xs, ys):
    n = len(xs)
    if n < 2:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx if sxx else None


def ranks(v):
    o = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.0] * len(v)
    i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]:
            j += 1
        for k in range(i, j + 1):
            r[o[k]] = (i + j) / 2
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    c = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    return c / math.sqrt(sum((x - ma) ** 2 for x in ra) * sum((y - mb) ** 2 for y in rb))


print('TXT run 4 (plans/txt-plan.md): four polygons, every corner rounded to radius r; τ = 5, o200k_base tokens.\n')
names = []
for p in R['polys']:
    if p['name'] not in names:
        names.append(p['name'])
U1, U2, U3, U4 = True, True, True, True
for nm in names:
    rows = [p for p in R['polys'] if p['name'] == nm]
    print(f'## {nm}')
    print(f'   {"r":>7} {"L/r":>7} {"corners":>7} | counts: TVF N, FD 2K+1, RAD N, SVG cubics, POLY vertices | tokens: TVF, SVG best, ratio')
    for p in rows:
        c = p['counts']
        tv, sv = tok(p['texts']['tvf']), min(x for x in (tok(p['texts']['svgabs']), tok(p['texts']['svgrel'])) if x)
        p['tok'] = (tv, sv)
        print(f'   {p["r"]:7.1f} {p["L"] / p["r"]:7.1f} {p["corners"]:7} | {c["tvf"]!s:>5} {c["fd"]!s:>5} {c["rad"]!s:>5} '
              f'{c["svg"]!s:>5} {c["poly"]!s:>5} | {tv!s:>5} {sv!s:>5} {tv / sv if tv and sv else float("nan"):6.2f}'
              + ('   (capped at r_max)' if p['capped'] else ''))
    for fm in ('tvf', 'fd', 'rad'):
        pts = [(math.log(p['L'] / p['r']), math.log(p['counts'][fm])) for p in rows if p['corners'] == 0 and p['counts'][fm]]
        a = slope([x for x, _ in pts], [y for _, y in pts])
        ok = a is not None and 0.7 <= a <= 1.3
        if fm == 'rad' and not pts:
            print(f'   U1 {fm}: does not apply'); continue
        U1 &= ok
        print(f'   U1 {fm} slope over {len(pts)} radii with no corner: {a if a is None else round(a, 3)} (0.7–1.3): {k_(ok)}')
    # for information: the slope over every radius
    for fm in ('tvf', 'fd', 'rad'):
        pts = [(math.log(p['L'] / p['r']), math.log(p['counts'][fm])) for p in rows if p['counts'][fm]]
        a = slope([x for x, _ in pts], [y for _, y in pts])
        print(f'      (all radii, {fm}: slope {a if a is None else round(a, 3)} over {len(pts)})')
    sv = [p['counts']['svg'] for p in rows]
    u2 = max(sv) / min(sv) <= 1.5
    U2 &= u2
    print(f'   U2 SVG cubics {min(sv)}–{max(sv)}, ×{max(sv) / min(sv):.2f} (≤ 1.5): {k_(u2)}')
    u3 = rows[-1]['counts']['poly'] > rows[0]['counts']['poly']
    U3 &= u3
    print(f'   U3 POLY {rows[0]["counts"]["poly"]} at the smallest r, {rows[-1]["counts"]["poly"]} at the largest: {k_(u3)}')
    small = rows[0]['tok']
    tgt = [p for p in rows if p['frac'] == 0.1][0] if any(p['frac'] == 0.1 for p in rows) else rows[-1]
    u4 = small[0] > small[1] and tgt['tok'][0] < tgt['tok'][1]
    U4 &= u4
    print(f'   U4 TVF/SVG {small[0] / small[1]:.2f} at the smallest r, {tgt["tok"][0] / tgt["tok"][1]:.2f} at 0.1 of the size '
          f'(> 1, < 1): {k_(u4)}\n')

lib = R['library']
D = [f['L'] / f['rmin'] for f in lib]
C = [f['corners'] for f in lib]
T = [tok(f['texts']['tvf']) for f in lib]
S = [min(tok(f['texts']['svgabs']), tok(f['texts']['svgrel'])) for f in lib]
rtd, rtc, rsd, rsc = spearman(T, D), spearman(T, C), spearman(S, D), spearman(S, C)
print(f'## library (73 figures): Spearman ρ')
print(f'   TVF tokens with D = L/r_min {rtd:.3f}, with corners {rtc:.3f}')
print(f'   SVG tokens with D {rsd:.3f}, with corners {rsc:.3f}\n')
print(f'U1 reader formats\' slopes in 0.7–1.3 on every polygon: {k_(U1)}')
print(f'U2 SVG within ×1.5 across the radii on every polygon: {k_(U2)}')
print(f'U3 POLY larger at the largest radius on every polygon: {k_(U3)}')
print(f'U4 TVF longer than SVG at the smallest radius and shorter at 0.1 on every polygon: {k_(U4)}')
print(f'U5 TVF with D {rtd:.3f} > with corners {rtc:.3f}, and SVG with corners {rsc:.3f} > with D {rsd:.3f}: '
      f'{k_(rtd > rtc and rsc > rsd)}')
