# ✅ AdSense/AdMob Deployment Checklist

## 📦 Oluşturulan Dosyalar

- ✅ `ads.txt` - Google AdSense için publisher doğrulama dosyası
- ✅ `app-ads.txt` - Google AdMob (mobile app) için publisher doğrulama dosyası
- ✅ `vercel.json` - Güncellenmiş (ads.txt için doğru header'lar eklendi)
- ✅ `ADSENSE-SETUP-GUIDE.md` - Detaylı kurulum ve sorun giderme rehberi
- ✅ `verify-adsense-setup.ps1` - Otomatik doğrulama scripti (PowerShell)
- ✅ `verify-adsense-setup.sh` - Otomatik doğrulama scripti (Bash/Linux)

## 🎯 Yapılması Gerekenler

### 1. Git Commit & Push (ŞİMDİ)

```bash
git add ads.txt app-ads.txt vercel.json ADSENSE-SETUP-GUIDE.md DEPLOYMENT-CHECKLIST.md verify-adsense-setup.ps1 verify-adsense-setup.sh
git commit -m "feat: Add ads.txt and app-ads.txt for AdSense/AdMob approval"
git push origin main
```

### 2. Vercel Deployment Kontrolü (5-10 dakika sonra)

- Vercel otomatik deploy yapacak
- Deploy tamamlandığında şu URL'leri kontrol et:
  - https://orbisastro.online/ads.txt
  - https://orbisastro.online/app-ads.txt
- Her ikisi de publisher ID'nizi göstermeli: `pub-2444093901783574`

### 3. AdSense Dashboard Kontrolü (24-48 saat sonra)

1. [AdSense Dashboard](https://www.google.com/adsense/) → **Sites**
2. **orbisastro.online** sitesini bul
3. **ads.txt** durumunu kontrol et
4. "Bulunamadı" yerine "✓ Doğrulandı" görmeli

### 4. AdMob Dashboard Kontrolü (24-48 saat sonra)

1. [AdMob Dashboard](https://apps.admob.com/) → **Apps**
2. ORBIS uygulamanızı seç
3. **app-ads.txt** durumunu kontrol et

### 5. Google Play Console (Mobile App için)

1. [Google Play Console](https://play.google.com/console/)
2. **Monetization** → **Monetization setup**
3. **app-ads.txt** bölümünde website URL'yi doğrula: `https://orbisastro.online`

## 🔍 Doğrulama

### Otomatik Doğrulama (PowerShell)

```powershell
.\verify-adsense-setup.ps1
```

### Manuel Doğrulama

```bash
# ads.txt kontrolü
curl https://orbisastro.online/ads.txt

# app-ads.txt kontrolü
curl https://orbisastro.online/app-ads.txt

# Beklenen çıktı:
# google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0
```

## 📊 Mevcut Durum

### ✅ Tamamlanan

- [x] Publisher ID tespit edildi: `pub-2444093901783574`
- [x] ads.txt dosyası oluşturuldu
- [x] app-ads.txt dosyası oluşturuldu
- [x] Vercel config güncellendi
- [x] Privacy Policy'de reklam/çerez bilgisi mevcut
- [x] AdSense kodu index.html'de mevcut
- [x] Legal sayfalar mevcut (Privacy, Terms, KVKK)
- [x] Google Analytics entegrasyonu mevcut

### ⏳ Bekleyen (Deployment Sonrası)

- [ ] Git push yapılması
- [ ] Vercel deployment tamamlanması
- [ ] ads.txt URL'nin erişilebilir olması
- [ ] app-ads.txt URL'nin erişilebilir olması
- [ ] Google'ın dosyaları taraması (24-48 saat)
- [ ] AdSense onay durumunun güncellenmesi

## 🚨 Önemli Notlar

### ads.txt Formatı

- **Doğru:** `google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0`
- **Yanlış:** Boşluk, satır sonu veya karakter hatası olmamalı
- **Encoding:** UTF-8 (BOM olmadan)
- **Line Endings:** LF (Unix style) veya CRLF (Windows style) - her ikisi de çalışır

### Vercel Deployment

- Vercel otomatik olarak main branch'e push sonrası deploy yapar
- Deploy süresi: ~2-5 dakika
- Deploy loglarını kontrol et: https://vercel.com/dashboard

### Google Tarama Süresi

- Google, ads.txt dosyasını 24-48 saat içinde tarar
- Eğer acil ise, AdSense dashboard'da "Yeniden Tara" butonunu kullan
- Cache temizleme: Google'ın cache'i 24 saat sürebilir

## 📞 Sorun Giderme

### Problem: ads.txt 404 hatası veriyor

**Çözüm:**

1. Vercel deployment'ın tamamlandığını kontrol et
2. Dosyanın root dizinde olduğunu doğrula (`/ads.txt`, `/subfolder/ads.txt` değil)
3. Vercel'de manuel redeploy tetikle: `vercel --prod`

### Problem: AdSense hala "Bulunamadı" diyor

**Çözüm:**

1. URL'yi manuel kontrol et: https://orbisastro.online/ads.txt
2. Dosya görünüyorsa 24-48 saat bekle
3. AdSense'de "Yeniden Tara" butonuna tıkla
4. Browser cache'i temizle ve tekrar kontrol et

### Problem: "Müdahale edilmesi gerekiyor" durumu devam ediyor

**Olası Nedenler:**

1. **İçerik Yetersizliği:** Daha fazla orijinal içerik ekle
2. **Trafik Düşük:** SEO ve sosyal medya paylaşımlarını artır
3. **Politika İhlali:** Tüm içeriği AdSense politikalarına göre gözden geçir
4. **Site Yaşı:** Yeni siteler için 1-2 hafta bekleme süresi olabilir

## 📈 Sonraki Adımlar (Onay Sonrası)

### 1. Reklam Birimlerini Oluştur

- **Web:** Display ads, In-article ads, Multiplex ads
- **Mobile:** Banner ads, Interstitial ads, Rewarded ads

### 2. Reklam Yerleşimini Optimize Et

- Header banner (üst kısım)
- In-article ads (blog yazıları içinde)
- Sidebar ads (yan panel)
- Footer ads (alt kısım)

### 3. GDPR/KVKK Uyumluluğu

- Consent Management Platform (CMP) entegre et
- Kullanıcılara çerez tercihlerini sunma seçeneği ekle
- Privacy Policy'yi güncelle (reklam çerezleri detaylandır)

### 4. Performans İzleme

- AdSense dashboard'da günlük gelir takibi
- RPM, CTR, CPC metriklerini izle
- A/B testing ile reklam yerleşimini optimize et

## 🔗 Faydalı Linkler

- [AdSense Dashboard](https://www.google.com/adsense/)
- [AdMob Dashboard](https://apps.admob.com/)
- [Google Play Console](https://play.google.com/console/)
- [Vercel Dashboard](https://vercel.com/dashboard)
- [ads.txt Guide](https://support.google.com/adsense/answer/7532444)
- [AdSense Program Policies](https://support.google.com/adsense/answer/48182)

## ✅ Final Checklist

Deployment öncesi son kontrol:

- [x] ads.txt dosyası oluşturuldu ve doğru içeriğe sahip
- [x] app-ads.txt dosyası oluşturuldu ve doğru içeriğe sahip
- [x] vercel.json güncellendi (header konfigürasyonu)
- [x] Publisher ID doğru: `pub-2444093901783574`
- [x] Privacy Policy'de reklam/çerez bilgisi mevcut
- [x] AdSense kodu index.html'de mevcut
- [ ] Git commit & push yapıldı
- [ ] Vercel deployment tamamlandı
- [ ] URL'ler erişilebilir (https://orbisastro.online/ads.txt)
- [ ] AdSense dashboard'da 24-48 saat sonra kontrol edildi

---

**Hazırlayan:** Kiro AI Assistant
**Tarih:** 23 Ocak 2026
**Durum:** ✅ Deployment için hazır
**Sonraki Adım:** `git push origin main`
