"""TXT run 3, step 4: the report and the verdicts (plans/txt-plan.md, run 3).

    python3 runs/txt/txt3_report.py <forms3.json> <dist3.json> > runs/txt/txt-run3.txt
"""
import sys, json, statistics as st
import tiktoken

E = tiktoken.get_encoding('o200k_base')
INF = float('inf')
forms = json.load(open(sys.argv[1]))
dist = json.load(open(sys.argv[2]))
READ, WRITE = ['tvf', 'fd', 'rad'], ['svg', 'poly', 'step', 'turtle']
ALL = READ + WRITE + ['hyb']
med = lambda v: st.median(v) if v else float('nan')


def tokens(f):
    t = {k: len(E.encode(v)) for k, v in f['texts'].items()}
    if 'svgabs' in t:
        t['svg'] = min(t['svgabs'], t['svgrel'])
    return t


print('TXT run 3 (plans/txt-plan.md): readers\' and writers\' formats at τ = 5, o200k_base tokens.\n')
print(f'{"figure":<14}{"corners":>8}  ' + ''.join(f'{k:>8}' for k in ALL))
T = {}
for f in forms:
    t = tokens(f)
    T[f['key']] = (f['corners'], t, f['radApplies'])
    print(f'{f["key"]:<14}{f["corners"]:>8}  ' + ''.join(f'{(t[k] if k in t else ("n/a" if k == "rad" and not f["radApplies"] else "—")):>8}' for k in ALL))
print('(n/a: the radial function does not apply; —: no text within the limits reached τ)\n')

groups = {'smooth (0 corners)': lambda c: c == 0, 'one corner': lambda c: c == 1, 'cornered (2 or more)': lambda c: c >= 2}
M = {}
for g, sel in groups.items():
    keys = [k for k, (c, _, _) in T.items() if sel(c)]
    print(f'{g}: {len(keys)} figures; median tokens')
    for k in ALL:
        v = [T[x][1][k] if k in T[x][1] else INF for x in keys if not (k == 'rad' and not T[x][2])]
        M[(g, k)] = med(v)
        print(f'   {k:<7} {med(v):>8.1f}   over {len(v)} ({sum(x == INF for x in v)} unreached)')
print()

# per figure: best reader against best writer
def best(t, ks):
    v = [t[k] for k in ks if k in t]
    return min(v) if v else INF
sm = [k for k, (c, _, _) in T.items() if c == 0]
co = [k for k, (c, _, _) in T.items() if c >= 2]
r_sm = sum(best(T[k][1], READ) < best(T[k][1], WRITE) for k in sm) / len(sm)
r_co = sum(best(T[k][1], READ) > best(T[k][1], WRITE) for k in co) / len(co)
print(f'best reader shorter than best writer on {r_sm:.0%} of smooth figures; longer on {r_co:.0%} of cornered figures')
for k in sorted(T, key=lambda k: T[k][0]):
    c, t, _ = T[k]
    br, bw = best(t, READ), best(t, WRITE)
    print(f'   {k:<14} corners {c:>3}  best reader {br:>6}  best writer {bw:>6}  {"reader" if br < bw else ("writer" if bw < br else "tie")}'
          f'  hybrid {t.get("hyb", "—")}')
hy_short = sum(t.get('hyb', INF) <= min(t[k] for k in ALL if k in t) for _, t, _ in T.values()) / len(T)
hy_ratio = med([T[k][1].get('hyb', INF) / best(T[k][1], WRITE) for k in co])
print(f'HYB shortest (ties count) on {hy_short:.0%} of figures; median HYB / best writer on cornered figures {hy_ratio:.2f}\n')

# slips
print('slips (20 a figure a kind a format); broken: Hausdorff over 5% or nothing drawn; share disturbed: of the rebuilt '
      'outline more than 1% from the figure, median over those drawn')
FORMS = ['tvf', 'fd', 'rad', 'svgabs', 'svgrel', 'poly', 'step', 'turtle', 'hyb']
S = {}
for kind in ('drop', 'wrong', 'jitter'):
    print(f'  {kind}')
    for fm in FORMS:
        ds = [d for d in dist if d['form'] == fm and d['kind'] == kind]
        if not ds:
            continue
        br = sum(d['dist'] is None or d['dist'] > 0.05 for d in ds) / len(ds)
        sh = med([d['share'] for d in ds if d['share'] is not None])
        md = med([d['dist'] for d in ds if d['dist'] is not None])
        S[(kind, fm)] = (br, sh)
        print(f'     {fm:<7} broken {br:6.1%}   share disturbed {sh:6.1%}   median distance {md * 100:6.2f}%   drawn '
              f'{sum(d["dist"] is not None for d in ds) / len(ds):.1%}')
print()

k_ = lambda ok: 'not killed' if ok else 'KILLED'
q1 = all(M[('smooth (0 corners)', r)] < M[('smooth (0 corners)', w)] for r in READ for w in WRITE)
q2 = all(M[('cornered (2 or more)', w)] < M[('cornered (2 or more)', r)] for r in READ for w in WRITE)
print(f'Q1 smooth: readers {[round(M[("smooth (0 corners)", r)]) for r in READ]} all below writers '
      f'{[round(M[("smooth (0 corners)", w)]) for w in WRITE]}: {k_(q1)}')
print(f'Q2 cornered: writers {[round(M[("cornered (2 or more)", w)]) for w in WRITE]} all below readers '
      f'{[round(M[("cornered (2 or more)", r)]) for r in READ]}: {k_(q2)}')
print(f'Q3 best reader shorter on {r_sm:.0%} of smooth (≥ 75%), longer on {r_co:.0%} of cornered (≥ 90%): {k_(r_sm >= 0.75 and r_co >= 0.9)}')
print(f'Q4 HYB shortest on {hy_short:.0%} (≥ 70%), HYB/best writer on cornered {hy_ratio:.2f} (≤ 1.0): {k_(hy_short >= 0.7 and hy_ratio <= 1.0)}')
W5 = ['svgabs', 'svgrel', 'poly', 'step', 'turtle']
wb = [S[('drop', w)][0] for w in W5]
q5 = all(S[('drop', r)][0] < min(wb) for r in ('tvf', 'rad')) and S[('drop', 'fd')][0] >= med(wb)
print(f'Q5 dropped token, broken: TVF {S[("drop", "tvf")][0]:.1%}, RAD {S[("drop", "rad")][0]:.1%} below every writer '
      f'(least {min(wb):.1%}); FD {S[("drop", "fd")][0]:.1%} ≥ writers\' median {med(wb):.1%}: {k_(q5)}')
sh = lambda f: S[('wrong', f)][1]
q6 = all(sh(a) < sh(r) for a in ('svgabs', 'poly') for r in ('tvf', 'rad')) and \
     all(sh(x) > sh(a) for x in ('svgrel', 'step', 'turtle') for a in ('svgabs', 'poly'))
print(f'Q6 wrong number, share disturbed: absolute writers {sh("svgabs"):.1%}, {sh("poly"):.1%} below TVF {sh("tvf"):.1%}, '
      f'RAD {sh("rad"):.1%}; relative writers {sh("svgrel"):.1%}, {sh("step"):.1%}, {sh("turtle"):.1%} above both: {k_(q6)}')
jb = lambda f: S[('jitter', f)][0]
q7 = all(jb(x) > jb(o) for x in ('svgrel', 'step', 'turtle') for o in ('svgabs', 'poly', 'tvf', 'fd', 'rad'))
print(f'Q7 imprecise numbers, broken: relative writers {jb("svgrel"):.1%}, {jb("step"):.1%}, {jb("turtle"):.1%} above every '
      f'other ({", ".join(f"{o} {jb(o):.1%}" for o in ("svgabs", "poly", "tvf", "fd", "rad"))}): {k_(q7)}')
