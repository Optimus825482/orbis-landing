"""
ORBIS Coolify deploy full-stack validator.
Verifies: docker-compose.yaml + nginx/http.conf + nginx/cf-origin.conf + Dockerfile.
"""
import os, sys, re

try:
    import yaml
except ImportError:
    print("PyYAML missing — install: pip install pyyaml")
    sys.exit(1)

ok = True
errors = []
warnings = []

# 1. docker-compose.yaml
print("=" * 60)
print("docker-compose.yaml")
print("=" * 60)

with open('docker-compose.yaml') as f:
    compose = yaml.safe_load(f)

services = compose.get('services', {})
if 'orbis-landing' not in services:
    errors.append("Service 'orbis-landing' missing")
    ok = False
else:
    svc = services['orbis-landing']
    print(f"Service: orbis-landing")
    print(f"  image: {svc.get('image')}")
    print(f"  build: {svc.get('build')}")
    print(f"  restart: {svc.get('restart')}")
    print(f"  mem_limit: {svc.get('mem_limit')}")
    print(f"  cpus: {svc.get('cpus')}")
    print(f"  expose: {svc.get('expose')}")

    if 'ports' in svc:
        errors.append("Service uses `ports:` instead of `expose:` — Coolify reverse-proxy conflict")
        ok = False
    if svc.get('build', {}).get('dockerfile') != 'Dockerfile':
        errors.append("Build dockerfile path wrong")
        ok = False
    if not svc.get('healthcheck'):
        errors.append("No healthcheck")
        ok = False

    # Volume mount validation
    vols = svc.get('volumes', [])
    mount_paths = []
    for v in vols:
        if isinstance(v, str):
            mount_paths.append(v)
    http_conf_mounted = any('nginx/http.conf' in v for v in mount_paths)
    cf_origin_mounted = any('nginx/cf-origin.conf' in v for v in mount_paths)
    if not http_conf_mounted and not cf_origin_mounted:
        errors.append("Neither http.conf nor cf-origin.conf mounted")
        ok = False
    if http_conf_mounted:
        print(f"  Mode A mount: OK")
    if cf_origin_mounted:
        print(f"  Mode B mount: OK (certs required)")

    # Networks
    if 'orbis-net' not in svc.get('networks', []):
        warnings.append("Service not attached to orbis-net")

# Networks
networks = compose.get('networks', {})
if 'orbis-net' not in networks:
    errors.append("Network 'orbis-net' missing")
    ok = False
else:
    print(f"Network orbis-net: {networks['orbis-net'].get('driver', 'default')}")

# 2. nginx/http.conf
print("\n" + "=" * 60)
print("nginx/http.conf (Mode A)")
print("=" * 60)
if os.path.exists('nginx/http.conf'):
    with open('nginx/http.conf') as f:
        http_conf = f.read()
    print(f"  Size: {len(http_conf)} bytes")
    if 'listen 80' not in http_conf:
        errors.append("http.conf doesn't listen on 80")
        ok = False
    if 'Strict-Transport-Security' in http_conf:
        warnings.append("http.conf has HSTS — CF edge also emits (Mode A duplicate)")
    if 'upgrade-insecure-requests' in http_conf:
        warnings.append("http.conf has upgrade-insecure-requests — CF handles")
    if 'Content-Security-Policy' not in http_conf:
        errors.append("http.conf missing CSP")
        ok = False
    if 'orbisastro.online' not in http_conf:
        warnings.append("http.conf doesn't reference orbisastro.online domain")
    print("  listen 80: OK")
    print(f"  CSP: {'present' if 'Content-Security-Policy' in http_conf else 'MISSING'}")
else:
    errors.append("nginx/http.conf missing")
    ok = False

# 3. nginx/cf-origin.conf
print("\n" + "=" * 60)
print("nginx/cf-origin.conf (Mode B)")
print("=" * 60)
if os.path.exists('nginx/cf-origin.conf'):
    with open('nginx/cf-origin.conf') as f:
        cf_conf = f.read()
    if 'listen 443' not in cf_conf:
        errors.append("cf-origin.conf missing listen 443")
        ok = False
    if 'ssl_certificate' not in cf_conf:
        errors.append("cf-origin.conf missing ssl_certificate directive")
        ok = False
    if 'Strict-Transport-Security' not in cf_conf:
        warnings.append("cf-origin.conf missing HSTS (Mode B needs it)")
    if '/etc/nginx/ssl/' not in cf_conf:
        errors.append("cf-origin.conf mount path missing")
        ok = False
    print("  listen 443: OK")
    print("  ssl_certificate: present")
    print("  HSTS: " + ("present" if 'Strict-Transport-Security' in cf_conf else "MISSING"))
else:
    errors.append("nginx/cf-origin.conf missing")
    ok = False

# 4. Dockerfile
print("\n" + "=" * 60)
print("Dockerfile")
print("=" * 60)
with open('Dockerfile') as f:
    df = f.read()
if 'nginx/http.conf' in df:
    print("  COPY nginx/http.conf: OK")
else:
    errors.append("Dockerfile doesn't COPY nginx/http.conf")
    ok = False
if 'USER nginx' in df:
    print("  USER nginx: OK")
else:
    errors.append("Dockerfile missing USER nginx")
    ok = False
if 'HEALTHCHECK' in df:
    print("  HEALTHCHECK: OK")
else:
    warnings.append("Dockerfile HEALTHCHECK missing")

# 5. .env.example
print("\n" + "=" * 60)
print(".env.example")
print("=" * 60)
if os.path.exists('.env.example'):
    with open('.env.example') as f:
        env = f.read()
    for key in ['DOMAIN', 'CONTAINER_NAME', 'PUBLIC_PORT', 'TZ']:
        if f'{key}=' in env:
            print(f"  {key}: OK")
        else:
            errors.append(f".env.example missing {key}")
            ok = False
    if 'orbisastro.online' not in env:
        warnings.append(".env.example doesn't set orbisastro.online as default DOMAIN")
else:
    errors.append(".env.example missing")
    ok = False

# 6. DEPLOY.md
print("\n" + "=" * 60)
print("DEPLOY.md")
print("=" * 60)
if os.path.exists('DEPLOY.md'):
    with open('DEPLOY.md') as f:
        lines = f.readlines()
    print(f"  Lines: {len(lines)}")
    if 'orbisastro.online' in ''.join(lines):
        print(f"  Domain ref: OK")
    if 'Coolify' in ''.join(lines):
        print(f"  Coolify ref: OK")
    if 'Cloudflare' in ''.join(lines):
        print(f"  Cloudflare ref: OK")
else:
    errors.append("DEPLOY.md missing")
    ok = False

# 7. nginx/README.md
print("\n" + "=" * 60)
print("nginx/README.md")
print("=" * 60)
if os.path.exists('nginx/README.md'):
    print(f"  Exists: OK")
else:
    errors.append("nginx/README.md missing")
    ok = False

# 8. .dockerignore
print("\n" + "=" * 60)
print(".dockerignore")
print("=" * 60)
with open('.dockerignore') as f:
    di = f.read()
checks = ['docker-compose.yml', 'docker-compose.yaml', '.env', 'verify_*.py', '*.md']
for c in checks:
    if c in di:
        print(f"  excludes {c}: OK")
    else:
        warnings.append(f".dockerignore doesn't exclude {c}")

# Summary
print("\n" + "=" * 60)
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors: print(f"  X {e}")
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings: print(f"  ! {w}")
if not errors:
    print("=" * 60)
    print("DEPLOY STACK: " + ("PASS" + (" with warnings" if warnings else "")))
else:
    print("DEPLOY STACK: FAIL")
    sys.exit(1)
