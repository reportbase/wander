"""DVE (plans/dve-plan.md): if runs/dve/laws.md lists more than 120 laws, move it to runs/dve/laws-all.md and write a
seeded sample of 120 (seed 15112026), in order, renumbered 1-120, each line keeping its number in the full list."""
import random, re, shutil
lines = open('runs/dve/laws.md', encoding='utf-8').read().split('\n')
laws = [(int(m.group(1)), m.group(2)) for l in lines if (m := re.match(r'(\d+)\. (.*)', l))]
print(len(laws), 'laws')
if len(laws) > 120:
    shutil.copy('runs/dve/laws.md', 'runs/dve/laws-all.md')
    keep = sorted(random.Random(15112026).sample(range(len(laws)), 120))
    with open('runs/dve/laws.md', 'w', encoding='utf-8') as f:
        f.write('# DVE laws (seeded sample of 120 from runs/dve/laws-all.md, seed 15112026)\n\n')
        for i, k in enumerate(keep, 1):
            f.write(f'{i}. {laws[k][1]} [full list {laws[k][0]}]\n')
    print('sampled 120')
