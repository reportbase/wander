"""PIE step 1: flag the laws of runs/lws/laws.md whose formula carries pi or e (plans/pie-plan.md)."""
import re
TOK = re.compile(r"π|Ω|e\^|e\(|\bexp\b|\bln\b|\blog\b|\bsin\b|\bcos\b|\btan\b|\bsec\b|\bcot\b|arctan|\batan|\basin|\bacos|"
                 r"\bsinh\b|\bcosh\b|\btanh\b|\bsech\b|\basinh\b|\batanh\b|\bgd\b|Γ|cos³|cos²|sin²|sec²|sin\(|cos\(|tan\(|"
                 r"sinh\(|cosh\(|tanh\(|sech\(|sin θ|cos θ|tan θ|e\b(?= =)")
out = []
for line in open('runs/lws/laws.md', encoding='utf-8'):
    m = re.match(r'(\d+)\. \*\*(.+?)\*\*:? ?(.*)$', line.strip())
    if not m:
        continue
    n, name, rest = int(m.group(1)), m.group(2), m.group(3)
    formula = re.sub(r'\s*\(§[^)]*\)\s*$', '', rest)
    formula = re.sub(r'\(Abstract[^)]*\)\s*$', '', formula)
    hits = sorted(set(TOK.findall(formula)))
    out.append((n, name, formula, hits))
flagged = [o for o in out if o[3]]
with open('runs/pie/flagged.md', 'w', encoding='utf-8') as f:
    f.write('Laws of runs/lws/laws.md whose formula carries π or e (mechanical flag, runs/pie/flag.py)\n\n')
    for n, name, formula, hits in flagged:
        f.write(f'{n}. **{name}**: {formula}\n')
print(f'{len(flagged)} of {len(out)} flagged:', [o[0] for o in flagged])
print('not flagged:', [o[0] for o in out if not o[3]])
