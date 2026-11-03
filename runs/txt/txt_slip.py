"""TXT step 2: token counts, and the slips (plans/txt-plan.md).

    python3 runs/txt/txt_slip.py <forms.json> <slips.json>      # writes the slipped texts
"""
import sys, json, random, re
import tiktoken

O200, CL100 = tiktoken.get_encoding('o200k_base'), tiktoken.get_encoding('cl100k_base')
NUMRE = re.compile(r'[+-]?(?:\d+\.?\d*|\.\d+)')
TRIALS = 20


def numbers(text, form):
    """Spans of the numbers in a text (TVF's header N, 1, 2 left out of the jitter, not of the wrong-number slip)."""
    return [(m.start(), m.end()) for m in NUMRE.finditer(text)]


def slip(text, form, kind, rnd):
    if kind == 'wrong':
        sp = numbers(text, form)
        (a, b), (c, d) = rnd.choice(sp), rnd.choice(sp)
        return text[:a] + text[c:d] + text[b:]
    if kind == 'drop':
        t = O200.encode(text)
        k = rnd.randrange(len(t))
        return O200.decode(t[:k] + t[k + 1:])
    if kind == 'jitter':
        head = text.index('\n') if form == 'tvf' else 0
        out, last = [], 0
        for m in NUMRE.finditer(text):
            if m.start() < head:
                continue
            v = float(m.group()) + rnd.uniform(-10, 10)
            dp = 1 if '.' in m.group() else 0
            s = f'{v:.{dp}f}'
            out.append(text[last:m.start()] + s)
            last = m.end()
        return ''.join(out) + text[last:]
    raise ValueError(kind)


if __name__ == '__main__':
    forms = json.load(open(sys.argv[1]))
    out = []
    for f in forms:
        F = f['forms']['5']
        for form in ('tvf', 'abs', 'rel'):
            if not F[form]:
                continue
            for kind in ('wrong', 'drop', 'jitter'):
                rnd = random.Random(f"{f['key']}|{form}|{kind}")
                for i in range(TRIALS):
                    out.append({'key': f['key'], 'form': form, 'kind': kind, 'i': i, 'text': slip(F[form], form, kind, rnd)})
    json.dump(out, open(sys.argv[2], 'w'))
    print(len(out), 'slipped texts')
