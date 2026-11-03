"""TXT step 4: the report and the verdicts (plans/txt-plan.md).

    python3 runs/txt/txt_report.py <forms.json> <dist.json> > runs/txt/txt-run1.txt
"""
import sys, json, statistics as st
import tiktoken

ENC = {'o200k_base': tiktoken.get_encoding('o200k_base'), 'cl100k_base': tiktoken.get_encoding('cl100k_base')}
INF = float('inf')
forms = json.load(open(sys.argv[1]))
dist = json.load(open(sys.argv[2]))


def med(v):
    return st.median(v) if v else None


print('TXT run 1 (plans/txt-plan.md): draw library figures, box 0–1000.\n')
ratios = {}
for tau in ('5', '1'):
    print(f'## τ = {tau}' + (' (integers)' if tau == '5' else ' (one decimal)'))
    print(f'   {"figure":<14}{"corners":>8}{"N":>6}{"cubics":>7}   tokens o200k: TVF / SVG abs / SVG rel   ratio   chars TVF / SVG best')
    for enc in ENC:
        ratios[(tau, enc)] = []
    for f in forms:
        F = f['forms'][tau]
        row = {}
        for enc, E in ENC.items():
            tv = len(E.encode(F['tvf'])) if F['tvf'] else None
            sv = min(len(E.encode(F['abs'])), len(E.encode(F['rel']))) if F['abs'] else None
            r = (tv / sv) if tv and sv else (INF if sv else None)
            ratios[(tau, enc)].append((f['key'], f['corners'], r))
            row[enc] = (tv, len(E.encode(F['abs'])) if F['abs'] else None, len(E.encode(F['rel'])) if F['rel'] else None, r)
        tv, sa, sr, r = row['o200k_base']
        ct = len(F['tvf']) if F['tvf'] else None
        cs = min(len(F['abs']), len(F['rel'])) if F['abs'] else None
        print(f'   {f["key"]:<14}{f["corners"]:>8}{str(F["N"]):>6}{str(F["segs"]):>7}   {str(tv):>6} / {str(sa):>5} / {str(sr):>5}'
              f'   {("—" if r is None else ("over 1024 leaves" if r == INF else f"{r:5.2f}")):>6}   {ct} / {cs}')
    for enc in ENC:
        rs = [r for _, _, r in ratios[(tau, enc)] if r is not None]
        sm = [r for _, c, r in ratios[(tau, enc)] if r is not None and c == 0]
        co = [r for _, c, r in ratios[(tau, enc)] if r is not None and c > 0]
        print(f'   {enc}: median TVF/SVG {med(rs):.2f} over {len(rs)} figures ({sum(r == INF for r in rs)} beyond 1,024 leaves);'
              f' smooth {med(sm) if sm else float("nan"):.2f} ({len(sm)}), with corners {med(co):.2f} ({len(co)})')
    print()

# slips
print('## slips at τ = 5 (20 a figure a kind a form); broken = Hausdorff over 5% of the figure or nothing drawn')
by = {}
for d in dist:
    by.setdefault((d['form'], d['kind']), []).append(d)
summ = {}
for (form, kind), ds in sorted(by.items()):
    drawn = [d for d in ds if d['dist'] is not None]
    broken = sum(1 for d in ds if d['dist'] is None or d['dist'] > 0.05) / len(ds)
    m = med([d['dist'] for d in drawn])
    summ[(form, kind)] = (broken, m, len(drawn) / len(ds))
    extra = ''
    if form == 'tvf':
        extra = f', read strictly {sum(d["strict"] for d in ds) / len(ds):.1%}'
    print(f'   {form:<4} {kind:<7} drawn {len(drawn) / len(ds):6.1%}  broken {broken:6.1%}  median distance {m * 100 if m is not None else float("nan"):.2f}%{extra}')

# best SVG variant (as in T1, the shorter by o200k at τ = 5) per figure
best = {f['key']: ('abs' if len(ENC['o200k_base'].encode(f['forms']['5']['abs'])) <= len(ENC['o200k_base'].encode(f['forms']['5']['rel'])) else 'rel')
        for f in forms if f['forms']['5']['abs']}
def shares(kind):
    tv = [d for d in by[('tvf', kind)]]
    sv = [d for f2 in ('abs', 'rel') for d in by[(f2, kind)] if best.get(d['key']) == f2]
    b = lambda ds: sum(1 for d in ds if d['dist'] is None or d['dist'] > 0.05) / len(ds)
    return b(tv), b(sv), med([d['dist'] for d in tv if d['dist'] is not None]), med([d['dist'] for d in sv if d['dist'] is not None])
print('   against the shorter SVG variant per figure:')
S = {}
for kind in ('wrong', 'drop', 'jitter'):
    S[kind] = shares(kind)
    bt, bs, mt, ms = S[kind]
    print(f'   {kind:<7} broken TVF {bt:.1%}, SVG {bs:.1%}; median distance TVF {mt * 100:.2f}%, SVG {ms * 100:.2f}%')
print()

r5 = [r for _, _, r in ratios[('5', 'o200k_base')] if r is not None]
r1 = [r for _, _, r in ratios[('1', 'o200k_base')] if r is not None]
sm5 = [r for _, c, r in ratios[('5', 'o200k_base')] if r is not None and c == 0]
k = lambda ok: 'not killed' if ok else 'KILLED'
print(f'T1 median TVF/SVG tokens at τ = 5: {med(r5):.2f} (1.0–2.5): {k(1.0 <= med(r5) <= 2.5)}')
print(f'T2 median at τ = 1 {med(r1):.2f} > at τ = 5 {med(r5):.2f}: {k(med(r1) > med(r5))}')
print(f'T3 smooth figures at τ = 5: {med(sm5):.2f} over {len(sm5)} (< 1): {k(sm5 and med(sm5) < 1)}')
tvf_closed = sum(d['closed'] for d in dist if d['form'] == 'tvf') / sum(1 for d in dist if d['form'] == 'tvf')
svg_drawn = sum(d['dist'] is not None for d in dist if d['form'] != 'tvf') / sum(1 for d in dist if d['form'] != 'tvf')
print(f'T4 TVF read leniently draws a closed curve {tvf_closed:.1%} (100%), SVG draws something {svg_drawn:.1%} (≥ 95%): '
      f'{k(tvf_closed == 1 and svg_drawn >= 0.95)}')
bt, bs, _, _ = S['drop']
print(f'T5 dropped token: broken TVF {bt:.1%} ≤ half SVG {bs:.1%}: {k(bt <= bs / 2)}')
bt, bs, _, _ = S['wrong']
print(f'T6 wrong number: broken TVF {bt:.1%} ≤ SVG {bs:.1%}: {k(bt <= bs)}')
bt, bs, mt, ms = S['jitter']
print(f'T7 imprecise numbers: broken TVF {bt:.1%}, SVG {bs:.1%} (both < 5%); median TVF {mt * 100:.2f}% within 3× SVG '
      f'{ms * 100:.2f}%: {k(bt < 0.05 and bs < 0.05 and mt <= 3 * ms)}')
