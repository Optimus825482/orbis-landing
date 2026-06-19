# ORBIS Nginx Config — Mode Switch Cheatsheet

Bu dizinde iki nginx konfigürasyonu var. Hangisini kullanacağın Cloudflare Proxy moduna göre değişir.

## Mode Karar Tablosu

| Senaryo | Mode | Config | CF Proxy | CF SSL Mode |
|---|---|---|---|---|
| **Default (önerilen)** | A | `http.conf` | **ON** (turuncu bulut) | Full |
| Full origin control, edge cache kapalı | B | `cf-origin.conf` | **OFF** (gri bulut) | Full (Strict) |

## Mode A — `http.conf` (Default)

**Ne zaman:** Cloudflare Proxy **ON** (turuncu bulut).

**Akış:**
```
Kullanıcı → CF Edge (TLS 443) → CF Proxy (HTTP) → Coolify Proxy (HTTP) → Container :80
```

**Özellikler:**
- Container sadece HTTP 80 dinler
- TLS tamamen CF + Coolify tarafından terminate edilir
- HSTS ve `upgrade-insecure-requests` CF edge'den gelir — nginx'te YOK (duplicate olmasın diye)
- Coolify otomatik Let's Encrypt sağlar (SSL/TLS termination Coolify tarafında)

**docker-compose.yaml mount:**
```yaml
volumes:
  - ./nginx/http.conf:/etc/nginx/conf.d/default.conf:ro
```

## Mode B — `cf-origin.conf` (Opsiyonel)

**Ne zaman:** Cloudflare Proxy **OFF** (gri bulut) + tam origin-side kontrol istiyorsun.

**Akış:**
```
Kullanıcı → CF Edge (TLS 443, Full Strict) → Container :443 (Origin Cert ile)
```

**Özellikler:**
- Container HTTPS 443 dinler, TLS terminate eder
- Cloudflare Origin Certificate (15 yıl RSA 2048) gerekli
- HSTS nginx'ten gelir (CF edge yok)
- HTTP 80 → 301 redirect to HTTPS

**Setup adımları:**
1. CF Dashboard → **SSL/TLS** → **Origin Server** → **Create Certificate**
   - Hosts: `orbisastro.online`, `*.orbisastro.online`
   - Validity: 15 years
2. PEM'i `certs/origin.pem` olarak kaydet (container mount yolu: `/etc/nginx/ssl/origin.pem`)
3. Private key'i `certs/origin.key` olarak kaydet (container mount yolu: `/etc/nginx/ssl/origin.key`)
4. CF Dashboard → **SSL/TLS** → **Overview** → encryption mode = **Full (Strict)**
5. CF DNS'te `orbisastro.online` A record → Proxy **OFF** (gri bulut)
6. `docker-compose.yaml`'da mount satırlarını güncelle:

```yaml
volumes:
  - ./nginx/cf-origin.conf:/etc/nginx/conf.d/default.conf:ro
  - ./certs/origin.pem:/etc/nginx/ssl/origin.pem:ro
  - ./certs/origin.key:/etc/nginx/ssl/origin.key:ro
```

7. Dockerfile'da `EXPOSE 80` → `EXPOSE 80 443` (veya Mode B variant Dockerfile kullan)

## Mode Değiştirme

docker-compose.yaml'da tek bir mount satırını değiştirmen yeterli. Coolify redeploy otomatik tetikler.

```yaml
# Mode A (default)
- ./nginx/http.conf:/etc/nginx/conf.d/default.conf:ro

# Mode B (origin-side TLS)
- ./nginx/cf-origin.conf:/etc/nginx/conf.d/default.conf:ro
- ./certs/origin.pem:/etc/nginx/ssl/origin.pem:ro
- ./certs/origin.key:/etc/nginx/ssl/origin.key:ro
```

## Hangi Mode Production İçin?

**Mode A önerilir** çünkü:
- Daha az konfigürasyon (cert rotation yok)
- DDoS koruması CF edge'de
- Coolify Let's Encrypt otomatik halleder
- Container reboot'larında cert kaybı riski yok
- HTTP/3 (QUIC) desteği CF edge'de

**Mode B ancak şu durumlarda:**
- CF edge cache'ini BYPASS etmen gerekiyor
- Origin'e doğrudan test erişimi istiyorsun (CF'yi devre dışı bırak)
- Kendi sertifikanla (Let's Encrypt wildcard) çalışmak istiyorsun
