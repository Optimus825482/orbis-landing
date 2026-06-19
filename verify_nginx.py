import re, sys, os

# Determine which config to validate
config_path = os.environ.get('NGINX_CONFIG', 'nginx-http.conf')
if not os.path.exists(config_path):
    print(f"Config not found: {config_path}")
    print("Set NGINX_CONFIG env var or place file at nginx/http.conf")
    sys.exit(1)

print(f"Validating: {config_path}")
print('=' * 60)
conf = open(config_path, encoding='utf-8').read()

errors = []
warnings = []
ok = True

# 1. Strip comments (but preserve strings/quotes)
clean = re.sub(r'#[^\n]*', '', conf)

# 2. Brace balance (outside strings — naive but works for simple configs)
depth = 0
in_string = False
string_char = None
for i, c in enumerate(clean):
    if in_string:
        if c == string_char and (i == 0 or clean[i-1] != '\\'):
            in_string = False
    else:
        if c in ('"', "'"):
            in_string = True
            string_char = c
        elif c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0:
                errors.append(f'Unexpected closing brace at offset {i}')
                ok = False
if depth != 0:
    errors.append(f'Brace mismatch: depth={depth} at end')
    ok = False
else:
    print(f'Brace balance: OK ({depth} remaining)')

# 3. Required directives
required_server = ['listen', 'server_name', 'root', 'index']
for d in required_server:
    if not re.search(rf'^\s*{d}\s+', clean, re.MULTILINE):
        errors.append(f'Missing required server directive: {d}')
        ok = False

# 4. Security headers — Mode-aware
# Mode A (http.conf): HSTS expected MISSING (CF edge emits)
# Mode B (cf-origin.conf): HSTS required
is_mode_a = 'http.conf' in config_path and 'cf-origin' not in config_path
hsts_required = not is_mode_a

sec_headers = {
    'X-Frame-Options': (r'X-Frame-Options', True),
    'X-Content-Type-Options': (r'X-Content-Type-Options', True),
    'Referrer-Policy': (r'Referrer-Policy', True),
    'Content-Security-Policy': (r'Content-Security-Policy', True),
    'Strict-Transport-Security': (r'Strict-Transport-Security', hsts_required),
    'Permissions-Policy': (r'Permissions-Policy', True),
}
print('\nSecurity headers:')
for name, (pat, required) in sec_headers.items():
    found = bool(re.search(pat, clean))
    status = "OK" if found else ("EXPECTED-MISSING" if not required else "MISSING")
    print(f'  {status} {name}')
    if not found and required:
        errors.append(f'Missing security header: {name}')
        ok = False
    elif found and not required:
        warnings.append(f'{name} present in Mode A — CF edge also emits (duplicate)')

# 5. CSP analysis
csp = re.search(r'Content-Security-Policy\s+"([^"]+)"', clean)
if csp:
    csp_val = csp.group(1)
    print(f'\nCSP length: {len(csp_val)} chars')
    # required CSP directives
    for directive in ['default-src', 'script-src', 'style-src', 'img-src', 'connect-src', 'frame-ancestors']:
        if directive not in csp_val:
            warnings.append(f'CSP missing directive: {directive}')
    # check unsafe-inline
    if "'unsafe-inline'" in csp_val:
        warnings.append("CSP allows 'unsafe-inline' (script-src or style-src)")

# 6. HSTS preload check
hsts = re.search(r'Strict-Transport-Security\s+"([^"]+)"', clean)
if hsts:
    hsts_val = hsts.group(1)
    if 'max-age=' in hsts_val:
        m = re.search(r'max-age=(\d+)', hsts_val)
        if m and int(m.group(1)) < 31536000:
            warnings.append(f'HSTS max-age too low: {m.group(1)} (recommended >= 31536000)')
    if 'preload' not in hsts_val:
        warnings.append('HSTS missing preload directive')
    else:
        print('HSTS preload: present')

# 7. Location blocks
locations = re.findall(r'location\s+([^\s{]+)', clean)
print(f'\nLocation blocks ({len(locations)}):')
for loc in locations:
    print(f'  {loc}')

# 8. try_files validity
try_files = re.findall(r'try_files\s+([^;]+);', clean)
for tf in try_files:
    parts = tf.strip().split()
    if not parts:
        errors.append(f'Empty try_files: {tf}')
        ok = False

# 9. Health endpoint
if '/health' not in clean:
    warnings.append('No /health endpoint')

print('\n' + '='*60)
if errors:
    print(f'ERRORS ({len(errors)}):')
    for e in errors: print(f'  X {e}')
if warnings:
    print(f'WARNINGS ({len(warnings)}):')
    for w in warnings: print(f'  ! {w}')
if not errors:
    print('nginx.conf PASS' + (' with warnings' if warnings else ''))
else:
    sys.exit(1)
