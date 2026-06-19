import re, os, sys

ok = True
warnings = []
errors = []

df = open('Dockerfile', encoding='utf-8').read()
lines = df.split('\n')

# 1. FROM directive present
m = re.search(r'^FROM\s+(\S+)(?::(\S+))?', df, re.MULTILINE)
if not m:
    errors.append('No FROM directive')
    ok = False
else:
    print(f'Base image: {m.group(1)}:{m.group(2) or "(default)"}')

# 2. USER directive present and not root
users = re.findall(r'^USER\s+(\S+)', df, re.MULTILINE)
if not users:
    errors.append('No USER directive — runs as root')
    ok = False
elif users[-1] == 'root' or users[-1] == '0':
    errors.append(f'USER set to root/0: {users[-1]}')
    ok = False
else:
    print(f'USER directive: {users[-1]}')

# 3. EXPOSE present
expose = re.findall(r'^EXPOSE\s+(\S+)', df, re.MULTILINE)
print(f'EXPOSE ports: {expose}')

# 4. CMD present
cmds = re.findall(r'^CMD\s+(.+)$', df, re.MULTILINE)
print(f'CMD entries: {cmds}')

# 5. COPY . (whole context) — security risk
copies = re.findall(r'^COPY\s+(.+?)\s+(.+)$', df, re.MULTILINE)
print(f'\nCOPY instructions: {len(copies)}')
for src, dst in copies:
    src_files = src.split()
    if '.' in src_files or '..' in src_files:
        warnings.append(f'COPY {src} -> {dst}: possibly broad scope, verify files exist')
    print(f'  {src} -> {dst}')

# 6. Required production files exist
required = ['index.html', 'styles.css', 'script.js', 'account-delete.html',
            'sitemap.xml', 'robots.txt', 'ads.txt', 'app-ads.txt',
            'nginx.conf', 'images', 'blog', 'legal', '.well-known']
missing = [f for f in required if not os.path.exists(f)]
if missing:
    errors.append(f'Missing files referenced by Dockerfile: {missing}')
    ok = False
else:
    print(f'\nAll {len(required)} production files present')

# 7. HEALTHCHECK validity
hc = re.search(r'^HEALTHCHECK\s+(.+)$', df, re.MULTILINE)
if hc:
    print(f'HEALTHCHECK: {hc.group(1)[:80]}...')
else:
    warnings.append('No HEALTHCHECK')

# 8. .dockerignore check
if not os.path.exists('.dockerignore'):
    warnings.append('No .dockerignore — broad build context')

# 9. Chown before USER
chowns = df.count('chown -R')
print(f'\nchown directives: {chowns}')

# Report
print('\n' + '='*60)
if errors:
    print(f'ERRORS ({len(errors)}):')
    for e in errors:
        print(f'  X {e}')
if warnings:
    print(f'WARNINGS ({len(warnings)}):')
    for w in warnings:
        print(f'  ! {w}')
if not errors and not warnings:
    print('Dockerfile PASS — production ready')
elif not errors:
    print('Dockerfile PASS with warnings')
else:
    print('Dockerfile FAIL')
    sys.exit(1)
