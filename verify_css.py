import re

css = open('styles.css', encoding='utf-8').read()

# Find linear-gradient( and balance parens correctly
results = []
i = 0
while True:
    idx = css.find('linear-gradient(', i)
    if idx < 0: break
    depth = 0
    j = idx + len('linear-gradient(')
    start = j
    while j < len(css):
        c = css[j]
        if c == '(':
            depth += 1
        elif c == ')':
            if depth == 0:
                break
            depth -= 1
        j += 1
    expr = css[start:j]
    results.append((idx, expr))
    i = j + 1

print(f'Total linear-gradient declarations: {len(results)}')

unbalanced = 0
for k, (pos, expr) in enumerate(results):
    # Walk expr and check internal balance
    d = 0
    bad = False
    for c in expr:
        if c == '(': d += 1
        elif c == ')':
            d -= 1
            if d < 0:
                bad = True
                break
    if d != 0 or bad:
        unbalanced += 1
        line_no = css[:pos].count('\n') + 1
        print(f'  [{k}] UNBALANCED line {line_no}: {expr[:80]}')

if unbalanced == 0:
    print(f'All {len(results)} gradients balanced.')

# Line 646
lines = css.split('\n')
print(f'Line 646: {lines[645].strip()}')

# Total brace balance
print(f'Braces: open={css.count(chr(123))}, close={css.count(chr(125))}, balanced={css.count(chr(123))==css.count(chr(125))}')
