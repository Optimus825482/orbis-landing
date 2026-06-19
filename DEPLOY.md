# ORBIS Landing — Coolify Deploy Rehberi

Domain: **orbisastro.online** | Platform: Coolify | SSL: Cloudflare

## Akış

```
Kullanıcı → Cloudflare Edge (TLS) → CF Proxy → Coolify Reverse Proxy → Container :80 (nginx)
```

**Default Mode A** kullanılır (Cloudflare Proxy ON). Mode B (CF Proxy OFF + Origin Cert) opsiyonel — bkz `nginx/README.md`.

## Önkoşullar

- Coolify v4.x kurulu VPS (1 vCPU, 512MB RAM yeterli)
- Domain `orbisastro.online` Cloudflare'de yönetiliyor
- Repo GitHub/GitLab'da (veya Coolify'nin erişebildiği bir git remote)

## 1. Cloudflare DNS Ayarı

| Type | Name | Target | Proxy |
|---|---|---|---|
| A | `@` | `<VPS_IPv4>` | **Proxied** (turuncu bulut) |
| AAAA | `@` | `<VPS_IPv6>` | Proxied |
| CNAME | `www` | `orbisastro.online` | Proxied |

**SSL/TLS → Overview:**
- Encryption mode → **Full** (Coolify otomatik Let's Encrypt sağlar)
- Edge Certificates → TLS 1.3 ON
- Always Use HTTPS → ON
- Minimum TLS Version → TLS 1.2
- HSTS → Enable (CF edge bunu emit eder)

## 2. Coolify Service Oluşturma

1. Coolify dashboard → **+ New Resource** → **Application**
2. **Source:** Git Repository
   - Repo URL: `https://github.com/<user>/orbis-landing.git`
   - Branch: `main`
3. **Build Pack:** **Dockerfile**
4. **Docker Compose Location:** repo root (Coolify otomatik bulur)
5. **Ports Exposes:** `80`
6. **Healthcheck Path:** `/health`
7. **Env Variables:** `.env.example`'dan kopyala:
   ```
   DOMAIN=orbisastro.online
   CONTAINER_NAME=orbis-landing
   PUBLIC_PORT=80
   TZ=Europe/Istanbul
   ```
8. **Domains:** Ekle
   - `orbisastro.online`
   - `www.orbisastro.online` (auto-redirect to apex)
9. **Deploy** butonuna bas.

Coolify otomatik:
- Repo'yu clone eder
- `Dockerfile` ile image build eder
- `docker-compose.yaml`'ı parse eder
- Container'ı başlatır
- Reverse proxy'yi konfigüre eder
- Let's Encrypt cert alır (5-30sn)

## 3. Deploy Doğrulama

Deploy tamamlandıktan sonra:

```bash
# 1. Health check
curl -fsS https://orbisastro.online/health
# Beklenen: {"status":"ok"}

# 2. Critical dosyalar
for path in / /ads.txt /app-ads.txt /robots.txt /sitemap.xml \
            /.well-known/assetlinks.json /account-delete.html /blog/ /legal/privacy.html; do
  code=$(curl -s -o /dev/null -w '%{http_code}' https://orbisastro.online$path)
  printf "%-40s %s\n" "$path" "$code"
done
# Beklenen: tüm 200

# 3. Headers (Mode A: HSTS CF'den, CSP nginx'ten)
curl -sI https://orbisastro.online/ | grep -iE 'strict-transport|content-security|x-frame|referrer-policy'
# Beklenen:
#   strict-transport-security: max-age=... (CF'den, TEK)
#   content-security-policy: default-src 'self'; ... (nginx'ten)
#   x-frame-options: SAMEORIGIN
#   referrer-policy: strict-origin-when-cross-origin

# 4. AdSense doğrulama
curl -fsS https://orbisastro.online/ads.txt
# Beklenen: google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0

curl -fsS https://orbisastro.online/app-ads.txt
# Beklenen: aynı publisher satırı

# 5. Android App Links
curl -fsS https://orbisastro.online/.well-known/assetlinks.json
# Beklenen: valid JSON, package_name: com.orbis.astrology
```

## 4. AdSense & Cookie Banner

1. **Browser'da aç:** `https://orbisastro.online`
2. **DevTools → Network:**
   - Sayfa yüklenmeden önce `googletagmanager.com`, `googlesyndication.com`, `doubleclick.net` **YOK** olmalı (consent gate çalışıyor)
3. **"Tümünü Kabul Et"** butonuna tıkla
4. Reload → şimdi `googletagmanager.com` ve `googlesyndication.com` requestleri görünmeli
5. **AdSense Dashboard** → Sites → `orbisastro.online` → 24-48 saat içinde "✓ Doğrulandı" bekleniyor

## 5. Güncelleme / Redeploy

```bash
git add .
git commit -m "feat: ..."
git push origin main
```

Coolify otomatik webhook ile deploy tetikler. Manuel tetiklemek için Coolify dashboard → Deploy.

## Mode B — Cloudflare Proxy OFF + Origin Certificate

Daha fazla origin-side kontrol istiyorsan:

1. CF → **SSL/TLS** → **Origin Server** → **Create Certificate**
   - Hosts: `orbisastro.online`, `*.orbisastro.online`
   - Validity: 15 years
2. PEM → `certs/origin.pem`, Key → `certs/origin.key` (gitignored)
3. `docker-compose.yaml` mount satırını değiştir (`http.conf` → `cf-origin.conf` + cert volume'ları)
4. Dockerfile'da `EXPOSE 80` → `EXPOSE 80 443`
5. CF SSL/TLS mode → **Full (Strict)**
6. CF DNS'te proxy → **DNS only** (gri bulut)
7. Redeploy

Detay: `nginx/README.md`.

## Troubleshooting

| Sorun | Çözüm |
|---|---|
| 502 Bad Gateway | Coolify henüz container'ı başlatmamış. 30sn bekle, sonra Logs kontrol et. |
| ads.txt 404 | Container build'de dosya kopyalanmamış. `docker exec orbis-landing ls /usr/share/nginx/html/ads.txt` ile kontrol et. |
| CSP hatası browser console'da | Content-Security-Policy'de izin verilmeyen bir domain var. Network log'dan offending URL'i al, nginx `script-src` veya `connect-src`'a ekle. |
| CF "Bulunamadı" 48 saat sonra | `curl -I https://orbisastro.online/ads.txt` ile 200 dönüyor mu kontrol et. 200 dönüyorsa "Yeniden Tara" butonuna tıkla. |
| Container OOM kill | `mem_limit: 128m` VPS için az. `docker-compose.yaml`'da 256m yap. |

## Container Kaynak İzleme

Coolify dashboard → Resources sekmesinden:
- CPU kullanımı (AdSense + GA traffic burst'lerinde pik yapabilir)
- Memory (idle ≈ 5-15MB, AdSense load ≈ 30-50MB)
- Network I/O

Limit artışı gerekirse `docker-compose.yaml`'da `mem_limit` ve `cpus` değerlerini güncelle.

## Yedekleme / Rollback

Coolify otomatik image tag tutmaz, ama her deploy öncesi:
```bash
# Coolify'nin image'ı manuel tag'le
docker tag orbis-landing:latest orbis-landing:backup-$(date +%Y%m%d-%H%M%S)
```

Rollback için Coolify dashboard → Deployments → önceki build'i seç → Redeploy.

---

**Sorular için:** Coolify docs https://coolify.io/docs
**Cloudflare:** https://developers.cloudflare.com/ssl/origin-configuration/
**AdSense review süresi:** 1-3 gün (ilk kez). `ads.txt` ve `app-ads.txt` doğrulandıktan sonra başlar.
