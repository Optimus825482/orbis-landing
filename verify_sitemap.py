import xml.etree.ElementTree as ET
import re, sys
from urllib.parse import urlparse

ok = True
errors = []
warnings = []

# 1. Well-formed XML
try:
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    print(f'XML well-formed. Root: {root.tag}')
except ET.ParseError as e:
    print(f'FATAL: XML parse error: {e}')
    sys.exit(1)

# 2. Namespace check
NS_SITEMAP = 'http://www.sitemaps.org/schemas/sitemap/0.9'
NS_XHTML = 'http://www.w3.org/1999/xhtml'
ns = {'sm': NS_SITEMAP, 'xhtml': NS_XHTML}

# 3. URL count
urls = root.findall('sm:url', ns)
print(f'URL entries: {len(urls)}')

# 4. Validate each URL
valid_changefreq = {'always', 'hourly', 'daily', 'weekly', 'monthly', 'yearly', 'never'}
date_re = re.compile(r'^\d{4}-\d{2}-\d{2}$')
seen_locs = set()

for u in urls:
    loc = u.find('sm:loc', ns)
    if loc is None or not loc.text:
        errors.append('Missing <loc>')
        ok = False
        continue
    loc_url = loc.text.strip()

    # duplicate check
    if loc_url in seen_locs:
        errors.append(f'Duplicate loc: {loc_url}')
        ok = False
    seen_locs.add(loc_url)

    # URL parse
    p = urlparse(loc_url)
    if p.scheme not in ('http', 'https'):
        errors.append(f'Bad scheme in {loc_url}')
        ok = False
    if not p.netloc:
        errors.append(f'No host in {loc_url}')
        ok = False
    if p.netloc and 'orbisastro.online' not in p.netloc:
        warnings.append(f'External host: {loc_url}')

    # lastmod
    lm = u.find('sm:lastmod', ns)
    if lm is None or not lm.text:
        warnings.append(f'Missing lastmod: {loc_url}')
    else:
        lm_text = lm.text.strip()
        if not date_re.match(lm_text):
            warnings.append(f'lastmod not YYYY-MM-DD: {lm_text}')

    # changefreq
    cf = u.find('sm:changefreq', ns)
    if cf is not None and cf.text:
        if cf.text.strip() not in valid_changefreq:
            errors.append(f'Invalid changefreq {cf.text} in {loc_url}')
            ok = False

    # priority
    pr = u.find('sm:priority', ns)
    if pr is not None and pr.text:
        try:
            pval = float(pr.text.strip())
            if not (0.0 <= pval <= 1.0):
                errors.append(f'Priority out of range {pr.text} in {loc_url}')
                ok = False
        except ValueError:
            errors.append(f'Priority not a number: {pr.text}')

    # hreflang xhtml:link
    xhtml_links = u.findall('xhtml:link', ns)
    for xl in xhtml_links:
        href = xl.get('href')
        hreflang = xl.get('hreflang')
        rel = xl.get('rel')
        if not href or not hreflang or rel != 'alternate':
            errors.append(f'Bad xhtml:link in {loc_url}')
            ok = False

# 5. Required URLs present
required_paths = ['/', '/account-delete', '/blog/index.html', '/legal/privacy.html']
present_paths = {urlparse(l).path for l in seen_locs}
for req in required_paths:
    if req not in present_paths:
        warnings.append(f'Recommended URL missing: {req}')

# 6. Old date check
print('\nLastmod summary:')
lastmods = []
for u in urls:
    lm = u.find('sm:lastmod', ns)
    if lm is not None and lm.text:
        lastmods.append(lm.text.strip())
        print(f'  {u.find("sm:loc", ns).text.strip():60s}  {lm.text.strip()}')

print('\n' + '='*60)
print(f'Total URLs: {len(urls)}')
print(f'Distinct hosts: {len(set(urlparse(l).netloc for l in seen_locs))}')

if errors:
    print(f'ERRORS ({len(errors)}):')
    for e in errors: print(f'  X {e}')
if warnings:
    print(f'WARNINGS ({len(warnings)}):')
    for w in warnings: print(f'  ! {w}')
if not errors:
    print('sitemap.xml PASS' + (' with warnings' if warnings else ''))
else:
    sys.exit(1)
