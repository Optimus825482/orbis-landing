# 🚀 AdSense/AdMob Quick Reference

## 📋 Hızlı Bilgiler

| Özellik               | Değer                                 |
| --------------------- | ------------------------------------- |
| **Publisher ID**      | `pub-2444093901783574`                |
| **Domain**            | `orbisastro.online`                   |
| **ads.txt URL**       | https://orbisastro.online/ads.txt     |
| **app-ads.txt URL**   | https://orbisastro.online/app-ads.txt |
| **AdSense Dashboard** | https://www.google.com/adsense/       |
| **AdMob Dashboard**   | https://apps.admob.com/               |

## ⚡ Hızlı Komutlar

### Deployment

```bash
# Tüm değişiklikleri commit et
git add .
git commit -m "feat: Add ads.txt for AdSense approval"
git push origin main
```

### Doğrulama

```bash
# PowerShell (Windows)
.\verify-adsense-setup.ps1

# Bash (Linux/Mac)
bash verify-adsense-setup.sh

# Manuel URL kontrolü
curl https://orbisastro.online/ads.txt
curl https://orbisastro.online/app-ads.txt
```

### Vercel

```bash
# Manuel deployment tetikle
vercel --prod

# Deployment loglarını görüntüle
vercel logs
```

## 🎯 Beklenen Sonuçlar

### ads.txt İçeriği

```
google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0
```

### HTTP Response

```
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Cache-Control: public, max-age=3600
```

## 📊 Zaman Çizelgesi

| Adım              | Süre       | Durum       |
| ----------------- | ---------- | ----------- |
| Git push          | 1 dakika   | ⏳ Bekliyor |
| Vercel deployment | 2-5 dakika | ⏳ Bekliyor |
| URL erişilebilir  | Hemen      | ⏳ Bekliyor |
| Google taraması   | 24-48 saat | ⏳ Bekliyor |
| AdSense onayı     | 1-2 hafta  | ⏳ Bekliyor |

## ✅ Kontrol Listesi

### Deployment Öncesi

- [x] ads.txt oluşturuldu
- [x] app-ads.txt oluşturuldu
- [x] vercel.json güncellendi
- [x] Publisher ID doğru
- [ ] Git push yapıldı

### Deployment Sonrası

- [ ] Vercel deployment tamamlandı
- [ ] ads.txt erişilebilir
- [ ] app-ads.txt erişilebilir
- [ ] AdSense'de kontrol edildi (24-48 saat sonra)

## 🐛 Hızlı Sorun Giderme

### ads.txt 404 hatası

```bash
# 1. Dosyanın varlığını kontrol et
ls -la ads.txt

# 2. Vercel'de redeploy
vercel --prod

# 3. URL'yi kontrol et
curl -I https://orbisastro.online/ads.txt
```

### AdSense "Bulunamadı" hatası

1. URL'yi manuel kontrol et
2. 24-48 saat bekle
3. AdSense'de "Yeniden Tara" yap
4. Browser cache'i temizle

### Vercel deployment hatası

```bash
# Deployment loglarını kontrol et
vercel logs

# Vercel status kontrol et
vercel inspect
```

## 📞 Destek Linkleri

| Kaynak       | URL                                 |
| ------------ | ----------------------------------- |
| AdSense Help | https://support.google.com/adsense/ |
| AdMob Help   | https://support.google.com/admob/   |
| Vercel Docs  | https://vercel.com/docs             |
| ads.txt Spec | https://iabtechlab.com/ads-txt/     |

## 💡 İpuçları

1. **Sabırlı Ol:** Google'ın ads.txt taraması 24-48 saat sürebilir
2. **Cache Temizle:** Browser cache'i temizleyerek test et
3. **HTTPS Kullan:** Her zaman HTTPS URL'leri kullan
4. **Encoding:** ads.txt dosyası UTF-8 (BOM olmadan) olmalı
5. **Line Endings:** LF veya CRLF - her ikisi de çalışır

## 🎓 Öğrenme Kaynakları

- [AdSense Başlangıç Rehberi](https://support.google.com/adsense/answer/6242051)
- [ads.txt Nedir?](https://support.google.com/adsense/answer/7532444)
- [AdMob Entegrasyonu](https://developers.google.com/admob)
- [Vercel Deployment](https://vercel.com/docs/deployments/overview)

---

**Not:** Bu dosya hızlı referans içindir. Detaylı bilgi için `ADSENSE-SETUP-GUIDE.md` dosyasına bakın.
