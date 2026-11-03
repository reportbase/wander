"""TXT run 3, step 2: the slips for every format (plans/txt-plan.md, run 3).

    python3 runs/txt/txt3_slip.py <forms3.json> <slips3.json>
"""
import sys, json, random, re
import tiktoken

O200 = tiktoken.get_encoding('o200k_base')
NUMRE = re.compile(r'[+-]?(?:\d+\.?\d*|\.\d+)')
TRIALS = 20


def slip(text, form, kind, rnd):
    if kind == 'wrong':
        sp = [(m.start(), m.end()) for m in NUMRE.finditer(text)]
        (a, b), (c, d) = rnd.choice(sp), rnd.choice(sp)
        return text[:a] + text[c:d] + text[b:]
    if kind == 'drop':
        t = O200.encode(text)
        k = rnd.randrange(len(t))
        return O200.decode(t[:k] + t[k + 1:])
    if kind == 'jitter':
        # every number after the header line by ±1% of its own range: ±10 units, a turtle's turn ±3.6°
        head = 0 if form.startswith('svg') else (text.index('\n') if '\n' in text else len(text))
        out, last, i = [], 0, 0
        for m in NUMRE.finditer(text):
            if m.start() < head:
                continue
            ang = form == 'turtle' and (i == 2 or (i >= 3 and (i - 3) % 2 == 0))
            i += 1
            v = float(m.group()) + rnd.uniform(-3.6, 3.6) if ang else float(m.group()) + rnd.uniform(-10, 10)
            dp = len(m.group().split('.')[1]) if '.' in m.group() else 0
            out.append(text[last:m.start()] + f'{v:.{dp}f}')
            last = m.end()
        return ''.join(out) + text[last:]
    raise ValueError(kind)


if __name__ == '__main__':
    forms = json.load(open(sys.argv[1]))
    out = []
    for f in forms:
        for form, text in f['texts'].items():
            if form == 'hyb' and text.startswith('TVF'):
                pass                      # a smooth figure's hybrid is its TVF; slipped all the same, as its own row
            for kind in ('wrong', 'drop', 'jitter'):
                rnd = random.Random(f"{f['key']}|{form}|{kind}")
                for i in range(TRIALS):
                    out.append({'key': f['key'], 'form': form, 'kind': kind, 'i': i, 'text': slip(text, form, kind, rnd)})
    json.dump(out, open(sys.argv[2], 'w'))
    print(len(out), 'slipped texts')
