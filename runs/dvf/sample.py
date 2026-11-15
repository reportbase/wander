"""DVF (plans/dvf-plan.md): if runs/dvf/laws.md lists more than 120 laws, move it to runs/dvf/laws-all.md and write a
seeded sample of 120 (seed 15112026), in order, renumbered 1-120, each line keeping its number in the full list."""
import random, re, shutil
lines = open('runs/dvf/laws.md', encoding='utf-8').read().split('\n')
laws = [(int(m.group(1)), m.group(2)) for l in lines if (m := re.match(r'(\d+)\. (.*)', l))]
print(len(laws), 'laws')
if len(laws) > 120:
    shutil.copy('runs/dvf/laws.md', 'runs/dvf/laws-all.md')
    keep = sorted(random.Random(15112026).sample(range(len(laws)), 120))
    with open('runs/dvf/laws.md', 'w', encoding='utf-8') as f:
        f.write('# DVF laws (seeded sample of 120 from runs/dvf/laws-all.md, seed 15112026)\n\n')
        for i, k in enumerate(keep, 1):
            f.write(f'{i}. {laws[k][1]} [full list {laws[k][0]}]\n')
    print('sampled 120')
