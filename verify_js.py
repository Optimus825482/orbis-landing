import subprocess, sys, re

# 1. Static balance check
js = open('script.js', encoding='utf-8').read()
opens = js.count('{')
closes = js.count('}')
po = js.count('(')
pc = js.count(')')
print(f'Braces: {opens}/{closes} {"OK" if opens==closes else "FAIL"}')
print(f'Parens: {po}/{pc} {"OK" if po==pc else "FAIL"}')
print(f'Lines: {len(js.splitlines())}')

# 2. Try node --check
try:
    r = subprocess.run(['node', '--check', 'script.js'], capture_output=True, text=True, timeout=10)
    if r.returncode == 0:
        print('node --check: OK')
    else:
        print(f'node --check FAIL: {r.stderr}')
        sys.exit(1)
except FileNotFoundError:
    print('node not installed — static balance only')
except Exception as e:
    print(f'node error: {e}')
