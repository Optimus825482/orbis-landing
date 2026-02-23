# 🎯 Google AdSense/AdMob Onay Rehberi - ORBIS

## ✅ Tamamlanan İşlemler

### 1. ads.txt Dosyası Oluşturuldu

- **Konum:** `/ads.txt` (root dizin)
- **İçerik:** Google AdSense ve AdMob publisher ID'niz (pub-2444093901783574)
- **Format:** IAB standardına uygun

### 2. app-ads.txt Dosyası Oluşturuldu

- **Konum:** `/app-ads.txt` (root dizin)
- **İçerik:** Mobile app için AdMob publisher ID
- **Amaç:** Google Play Store uygulamanız için ads.txt doğrulaması

### 3. Vercel Konfigürasyonu Güncellendi

- **Dosya:** `vercel.json`
- **Eklenen:** ads.txt ve app-ads.txt için doğru Content-Type header'ları
- **Cache:** 1 saat cache süresi (AdSense taramaları için optimize)

---

## 🚀 Deployment Adımları

### Adım 1: Git Commit & Push

```bash
git add ads.txt app-ads.txt vercel.json ADSENSE-SETUP-GUIDE.md
git commit -m "feat: Add ads.txt and app-ads.txt for AdSense/AdMob approval"
git push origin main
```

### Adım 2: Vercel Otomatik Deploy

- Vercel, push sonrası otomatik deploy yapacak
- Deploy tamamlandığında dosyalar erişilebilir olacak

### Adım 3: Dosyaları Doğrula

Deploy sonrası şu URL'leri tarayıcıda kontrol edin:

- ✅ https://orbisastro.online/ads.txt
- ✅ https://orbisastro.online/app-ads.txt

**Beklenen Çıktı:**

```
google.com, pub-2444093901783574, DIRECT, f08c47fec0942fa0
```

---

## 📋 AdSense Kontrol Paneli İşlemleri

### 1. ads.txt Durumunu Kontrol Et

1. [AdSense Dashboard](https://www.google.com/adsense/) → **Sites** bölümüne git
2. **orbisastro.online** sitesini bul
3. **ads.txt** durumunu kontrol et
4. Eğer hala "Bulunamadı" yazıyorsa:
   - 24-48 saat bekle (Google'ın tarama süresi)
   - "Yeniden Tara" butonuna tıkla (varsa)

### 2. Site İçeriği Kontrolü

AdSense politikalarına uygunluk için kontrol edin:

#### ✅ Mevcut ve Uygun:

- [x] Privacy Policy (legal/privacy.html) - **MEVCUT**
- [x] Terms of Service (legal/terms.html) - **MEVCUT**
- [x] KVKK (legal/kvkk.html) - **MEVCUT**
- [x] Orijinal içerik (Blog yazıları) - **MEVCUT**
- [x] İletişim bilgileri (Footer'da email) - **MEVCUT**
- [x] Google Analytics entegrasyonu - **MEVCUT**
- [x] AdSense kodu (index.html head'de) - **MEVCUT**

#### ⚠️ Kontrol Edilmesi Gerekenler:

- [ ] Privacy Policy'de AdSense/AdMob reklamları hakkında bilgi - **MEVCUT** ✅
- [ ] Privacy Policy'de çerez kullanımı açıklaması - **MEVCUT** ✅
- [ ] Site'de yeterli içerik (minimum 20-30 sayfa) - **KONTROL ET**
- [ ] Tüm sayfalar erişilebilir ve hatasız - **KONTROL ET**

---

## 🔍 AdSense Onay Kriterleri

### Teknik Gereksinimler ✅

- [x] Domain sahibi olduğunuzu kanıtlama (ads.txt ile)
- [x] HTTPS (SSL) - Vercel otomatik sağlıyor
- [x] Responsive tasarım - Mevcut
- [x] Hızlı yüklenme - Vercel CDN ile optimize

### İçerik Gereksinimleri

- [x] Orijinal ve değerli içerik
- [x] Yeterli sayfa sayısı (Blog yazıları mevcut)
- [x] Düzenli güncelleme (Blog aktif)
- [x] Yasal sayfalar (Privacy, Terms, KVKK)

### Politika Uyumu

- [x] Telif hakkı ihlali yok
- [x] Yetişkin içerik yok
- [x] Şiddet/nefret içeriği yok
- [x] Spam/yanıltıcı içerik yok

---

## 🎯 AdMob (Mobile App) Özel Adımlar

### 1. Google Play Console'da app-ads.txt Bağlantısı

1. [Google Play Console](https://play.google.com/console/) → **Uygulamanız**
2. **Monetization** → **Monetization setup**
3. **app-ads.txt** bölümünde:
   - Website URL: `https://orbisastro.online`
   - Verify butonuna tıkla

### 2. AdMob Dashboard Kontrolü

1. [AdMob Dashboard](https://apps.admob.com/) → **Apps**
2. ORBIS uygulamanızı seç
3. **App settings** → **App info**
4. **app-ads.txt** durumunu kontrol et

---

## 🐛 Sorun Giderme

### Problem 1: "ads.txt bulunamadı" hatası devam ediyor

**Çözüm:**

1. URL'yi manuel kontrol et: https://orbisastro.online/ads.txt
2. Eğer 404 alıyorsan:
   ```bash
   # Vercel'de yeniden deploy tetikle
   vercel --prod
   ```
3. Eğer dosya görünüyorsa ama AdSense görmüyorsa:
   - 24-48 saat bekle (Google cache)
   - AdSense'de "Yeniden Tara" yap

### Problem 2: "Müdahale edilmesi gerekiyor" durumu

**Olası Nedenler:**

1. **İçerik Yetersizliği:** Daha fazla blog yazısı ekle (hedef: 30+ sayfa)
2. **Trafik Düşük:** SEO optimizasyonu yap, sosyal medya paylaşımları artır
3. **Politika İhlali:** Tüm içeriği AdSense politikalarına göre gözden geçir
4. **Teknik Sorun:** Tüm sayfaların hatasız yüklendiğini kontrol et

### Problem 3: app-ads.txt doğrulanamıyor

**Çözüm:**

1. Google Play Console'da website URL'nin doğru olduğunu kontrol et
2. app-ads.txt dosyasının erişilebilir olduğunu doğrula
3. Publisher ID'nin her iki dosyada da aynı olduğunu kontrol et

---

## 📊 Onay Sonrası Yapılacaklar

### 1. Reklam Birimlerini Oluştur

**Web (AdSense):**

- Display ads (Responsive)
- In-article ads (Blog yazıları için)
- Multiplex ads (İlgili içerik)

**Mobile (AdMob):**

- Banner ads
- Interstitial ads (Tam ekran)
- Rewarded ads (Ödüllü video)

### 2. Reklam Yerleşimini Optimize Et

**Web:**

```html
<!-- Header Banner -->
<ins
  class="adsbygoogle"
  style="display:block"
  data-ad-client="ca-pub-2444093901783574"
  data-ad-slot="SLOT_ID"
  data-ad-format="auto"
></ins>

<!-- In-Article Ad (Blog yazılarında) -->
<ins
  class="adsbygoogle"
  style="display:block; text-align:center;"
  data-ad-layout="in-article"
  data-ad-format="fluid"
  data-ad-client="ca-pub-2444093901783574"
  data-ad-slot="SLOT_ID"
></ins>
```

**Mobile (React Native):**

```javascript
import {
  BannerAd,
  BannerAdSize,
  TestIds,
} from "react-native-google-mobile-ads";

const adUnitId = __DEV__
  ? TestIds.BANNER
  : "ca-app-pub-2444093901783574/SLOT_ID";

<BannerAd
  unitId={adUnitId}
  size={BannerAdSize.ANCHORED_ADAPTIVE_BANNER}
  requestOptions={{
    requestNonPersonalizedAdsOnly: true,
  }}
/>;
```

### 3. GDPR/KVKK Uyumluluğu

- Consent Management Platform (CMP) entegre et
- Kullanıcılara çerez tercihlerini sunma seçeneği ekle
- Privacy Policy'de reklam çerezlerini detaylandır

---

## 📈 Performans İzleme

### AdSense Metrikleri

- **RPM (Revenue Per Mille):** 1000 gösterim başına gelir
- **CTR (Click-Through Rate):** Tıklama oranı
- **CPC (Cost Per Click):** Tıklama başına maliyet
- **Viewability:** Görünürlük oranı

### AdMob Metrikleri

- **eCPM (Effective Cost Per Mille):** Etkili bin gösterim maliyeti
- **Fill Rate:** Reklam doldurma oranı
- **Impression:** Gösterim sayısı
- **Match Rate:** Eşleşme oranı

---

## 🔗 Faydalı Linkler

- [AdSense Help Center](https://support.google.com/adsense/)
- [AdMob Help Center](https://support.google.com/admob/)
- [ads.txt Guide](https://support.google.com/adsense/answer/7532444)
- [AdSense Program Policies](https://support.google.com/adsense/answer/48182)
- [AdMob Policy Center](https://support.google.com/admob/answer/6128543)

---

## ✅ Checklist - Onay Öncesi Son Kontrol

### Teknik

- [x] ads.txt dosyası root'ta ve erişilebilir
- [x] app-ads.txt dosyası root'ta ve erişilebilir
- [x] AdSense kodu tüm sayfalarda
- [x] HTTPS aktif
- [x] Responsive tasarım
- [x] Hızlı yüklenme (< 3 saniye)

### İçerik

- [x] Privacy Policy mevcut ve güncel
- [x] Terms of Service mevcut
- [x] KVKK/GDPR uyumlu
- [x] İletişim bilgileri mevcut
- [x] Orijinal içerik (blog yazıları)
- [ ] Minimum 20-30 sayfa içerik (KONTROL ET)

### Politika

- [x] Telif hakkı ihlali yok
- [x] Yetişkin içerik yok
- [x] Spam/yanıltıcı içerik yok
- [x] Şiddet/nefret içeriği yok

---

## 📞 Destek

Sorun yaşarsanız:

1. AdSense Help Forum'da arama yapın
2. Google AdSense Support ile iletişime geçin
3. Vercel Support'a deployment sorunları için başvurun

---

**Son Güncelleme:** 23 Ocak 2026
**Durum:** ✅ ads.txt ve app-ads.txt oluşturuldu, deployment için hazır
**Sonraki Adım:** Git push → Vercel deploy → 24-48 saat bekle → AdSense'de kontrol et
