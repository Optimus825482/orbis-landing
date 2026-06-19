import urllib.request, hashlib, base64, sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

urls = [
    "https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Outfit:wght@300;400;500;600;700&display=swap",
    "https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,1,0",
]

for url in urls:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read()
        sha384 = hashlib.sha384(body).digest()
        integrity = "sha384-" + base64.b64encode(sha384).decode()
        print(f'URL: {url[:80]}...')
        print(f'  bytes: {len(body)}')
        print(f'  integrity: {integrity}')
        print()
    except Exception as e:
        print(f'FAIL {url}: {e}')
        sys.exit(1)
