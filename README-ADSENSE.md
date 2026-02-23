# 🎯 AdSense/AdMob Onay Rehberi - Hızlı Başlangıç

## 🚀 Hemen Başla (3 Adım)

### 1️⃣ Deployment Yap

```bash
git add .
git commit -m "feat: Add ads.txt for AdSense/AdMob approval"
git push origin main
```

### 2️⃣ Doğrula (5 dakika sonra)

```powershell
.\verify-adsense-setup.ps1
```

### 3️⃣ Bekle ve Kontrol Et

- **24-48 saat sonra:** [AdSense Dashboard](https://www.google.com/adsense/) → ads.txt durumu
- **1-2 hafta sonra:** AdSense onay durumu

---

## 📚 Dokümantasyon

| Dosya                                                    | Açıklama             | Ne Zaman Kullan         |
| -------------------------------------------------------- | -------------------- | ----------------------- |
| **[QUICK-REFERENCE.md](./QUICK-REFERENCE.md)**           | Hızlı referans kartı | Hızlı bilgi için        |
| **[DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md)** | Adım adım checklist  | Deployment yaparken     |
| **[ADSENSE-SETUP-GUIDE.md](./ADSENSE-SETUP-GUIDE.md)**   | Detaylı rehber       | Sorun giderme için      |
| **[DEPLOYMENT-FLOW.md](./DEPLOYMENT-FLOW.md)**           | Akış diyagramı       | Süreci anlamak için     |
| **[CHANGES-SUMMARY.md](./CHANGES-SUMMARY.md)**           | Değişiklik özeti     | Yapılanları görmek için |

---

## ✅ Oluşturulan Dosyalar

- ✅ **ads.txt** - AdSense publisher doğrulama
- ✅ **app-ads.txt** - AdMob publisher doğrulama
- ✅ **vercel.json** - Güncellenmiş (header config)
- ✅ **verify-adsense-setup.ps1** - Doğrulama scripti (Windows)
- ✅ **verify-adsense-setup.sh** - Doğrulama scripti (Linux/Mac)

---

## 🔍 Hızlı Kontrol

### Local Kontrol

```powershell
# Dosyaların varlığını kontrol et
Get-Content ads.txt
Get-Content app-ads.txt

# Doğrulama scriptini çalıştır
.\verify-adsense-setup.ps1
```

### Remote Kontrol (Deployment Sonrası)

```bash
# URL'leri kontrol et
curl https://orbisastro.online/ads.txt
curl https://orbisastro.online/app-ads.txt
```

---

## 📊 Beklenen Sonuç

### ads.txt İçeriği

```
google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0
```

### Zaman Çizelgesi

- **T+0:** Deployment
- **T+5 min:** URL'ler erişilebilir
- **T+24-48h:** Google taraması tamamlandı
- **T+1-2w:** AdSense onayı

---

## 🐛 Sorun mu Var?

### ads.txt 404 hatası

1. Vercel deployment'ı kontrol et
2. `vercel --prod` ile redeploy yap
3. 5 dakika bekle ve tekrar dene

### AdSense "Bulunamadı" hatası

1. URL'yi manuel kontrol et
2. 24-48 saat bekle
3. AdSense'de "Yeniden Tara" yap

### Detaylı Sorun Giderme

👉 [ADSENSE-SETUP-GUIDE.md](./ADSENSE-SETUP-GUIDE.md) dosyasına bakın

---

## 📞 Önemli Linkler

- [AdSense Dashboard](https://www.google.com/adsense/)
- [AdMob Dashboard](https://apps.admob.com/)
- [Google Play Console](https://play.google.com/console/)
- [Vercel Dashboard](https://vercel.com/dashboard)

---

## 💡 Pro Tips

1. **Sabırlı Ol:** Google taraması 24-48 saat sürer
2. **Düzenli Güncelle:** Blog'u düzenli olarak güncelle
3. **SEO Yap:** Organik trafik onayı hızlandırır
4. **Politikalara Uy:** AdSense politikalarını oku

---

## ✅ Checklist

- [x] ads.txt oluşturuldu
- [x] app-ads.txt oluşturuldu
- [x] vercel.json güncellendi
- [x] Dokümantasyon hazır
- [ ] Git push yapıldı
- [ ] Deployment tamamlandı
- [ ] URL'ler erişilebilir
- [ ] Google taraması tamamlandı
- [ ] AdSense onayı alındı

---

**Hazırlayan:** Kiro AI Assistant  
**Tarih:** 23 Ocak 2026  
**Durum:** ✅ Deployment için hazır  
**Sonraki Adım:** `git push origin main`

---

## 🎉 Başarılar!

Tüm hazırlıklar tamamlandı. Şimdi sadece deployment yapman ve beklemen gerekiyor.

**Sorularınız için:** [ADSENSE-SETUP-GUIDE.md](./ADSENSE-SETUP-GUIDE.md) dosyasına bakın.
