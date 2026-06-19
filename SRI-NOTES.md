# SRI Subresource Integrity — NOT UYGULANDI

Google Fonts CSS link'lerine SRI hash ekleme **atlandı**.

## Neden

Google Fonts `css2` endpoint'i şu koşullarda **farklı body** döndürür:

1. **User-Agent** — Chrome, Firefox, Safari, mobile vs. farklı woff2 subset'leri alır
2. **Accept headers** — `woff2` vs `woff` vs eski formatlar
3. **Origin / Referer** — bazen farklı CORS varyantları

Hesaplanan hash yalnızca hesaplama anındaki UA+headers kombinasyonuna bağlı. Chrome 120 desktop'ta çalışan hash, Safari mobile'da body uyuşmazlığı yaratır ve tarayıcı **tüm font dosyasını bloklar** → font fallback'e düşer.

Hesaplanan örnek hash'ler (`compute_sri.py` ile):
- Cinzel+Outfit: `sha384-gr0JS3HKThsniuUOI+HIkr4WV5BocRl6sKfOHuSkEkO6SFzVTSogIjbfji0jdP+o`
- Material Symbols: `sha384-yY7w7NvWAFm8YdI8YO3Y79IrsfxfFhxL51iUf6wL1v129IeZhZqu0x8DzvmMYG9f`

## Google'ın resmi pozisyonu

Google Fonts dokümantasyonunda SRI **önerilmez**, çünkü dinamik font subsetting SRI ile uyumsuz.

## Mitigation

- CSP `style-src` zaten `'unsafe-inline'` içeriyor (Google AdSense/GTM inline script'leri için)
- Sayfa inline style kullanmıyor (extract edildi), bu yüzden `unsafe-inline` sadece 3rd-party inline için gerekli
- Risk yüzeyi az, font'lar kritik değil (system font fallback mevcut)

## Gerekirse SRI uygulamak için

Self-host fonts (download woff2, serve from `/fonts/`) → sonra SRI uygulanabilir.
