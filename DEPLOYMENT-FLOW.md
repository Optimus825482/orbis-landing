# 🔄 AdSense/AdMob Deployment Flow

## 📊 Deployment Akış Diyagramı

```
┌─────────────────────────────────────────────────────────────────┐
│                    BAŞLANGIÇ DURUMU                              │
│  ❌ ads.txt yok                                                  │
│  ❌ app-ads.txt yok                                              │
│  ⚠️  AdSense: "Müdahale edilmesi gerekiyor"                     │
│  ⚠️  ads.txt: "Bulunamadı"                                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 1: DOSYA OLUŞTURMA                       │
│  ✅ ads.txt oluşturuldu                                          │
│  ✅ app-ads.txt oluşturuldu                                      │
│  ✅ vercel.json güncellendi                                      │
│  ✅ Dokümantasyon eklendi                                        │
│  ⏱️  Süre: 5 dakika                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 2: GIT COMMIT & PUSH                     │
│  📝 git add .                                                    │
│  📝 git commit -m "feat: Add ads.txt"                           │
│  📝 git push origin main                                         │
│  ⏱️  Süre: 1 dakika                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 3: VERCEL DEPLOYMENT                     │
│  🚀 Otomatik deployment tetiklendi                              │
│  🔨 Build işlemi başladı                                         │
│  📦 Static dosyalar deploy ediliyor                             │
│  ✅ Deployment tamamlandı                                        │
│  ⏱️  Süre: 2-5 dakika                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 4: URL DOĞRULAMA                         │
│  🔍 https://orbisastro.online/ads.txt                           │
│  🔍 https://orbisastro.online/app-ads.txt                       │
│  ✅ HTTP 200 OK                                                  │
│  ✅ Content-Type: text/plain                                     │
│  ⏱️  Süre: Hemen                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 5: GOOGLE TARAMASI                       │
│  🤖 Google bot ads.txt'i taradı                                  │
│  🔍 Publisher ID doğrulandı                                      │
│  ✅ ads.txt durumu: "Doğrulandı"                                 │
│  ⏱️  Süre: 24-48 saat                                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ADIM 6: ADSENSE ONAY SÜRECİ                   │
│  👤 Google insan incelemesi                                      │
│  📊 İçerik kalitesi değerlendirmesi                              │
│  🔒 Politika uygunluğu kontrolü                                  │
│  ✅ Site onaylandı                                               │
│  ⏱️  Süre: 1-2 hafta                                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    HEDEF DURUM                                   │
│  ✅ ads.txt doğrulandı                                           │
│  ✅ app-ads.txt doğrulandı                                       │
│  ✅ AdSense: "Onaylandı"                                         │
│  ✅ Reklam gösterimi aktif                                       │
│  💰 Gelir akışı başladı                                          │
└─────────────────────────────────────────────────────────────────┘
```

## 🔀 Paralel İşlemler

### Web (AdSense) ve Mobile (AdMob) Aynı Anda

```
                    ┌─────────────────────┐
                    │   ads.txt & app-    │
                    │   ads.txt Deploy    │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
    ┌───────────────────┐         ┌───────────────────┐
    │   AdSense Flow    │         │   AdMob Flow      │
    │                   │         │                   │
    │ 1. ads.txt scan   │         │ 1. app-ads.txt    │
    │ 2. Site review    │         │    scan           │
    │ 3. Approval       │         │ 2. App review     │
    │ 4. Ad units       │         │ 3. Approval       │
    │                   │         │ 4. Ad units       │
    └───────────────────┘         └───────────────────┘
                │                             │
                └──────────────┬──────────────┘
                               ▼
                    ┌─────────────────────┐
                    │   Monetization      │
                    │   Active            │
                    └─────────────────────┘
```

## ⏱️ Zaman Çizelgesi (Timeline)

```
T+0 min     │ ✅ Dosyalar oluşturuldu
            │
T+1 min     │ 📝 Git push yapıldı
            │
T+5 min     │ 🚀 Vercel deployment tamamlandı
            │ ✅ URL'ler erişilebilir
            │
T+1 hour    │ 🔍 İlk Google tarama denemesi (olabilir)
            │
T+24 hours  │ 🤖 Google bot kesinlikle taradı
            │ ⏳ AdSense dashboard güncelleniyor
            │
T+48 hours  │ ✅ ads.txt durumu: "Doğrulandı"
            │ ⏳ Site inceleme süreci başladı
            │
T+1 week    │ 👤 İnsan incelemesi devam ediyor
            │ 📊 İçerik kalitesi değerlendiriliyor
            │
T+2 weeks   │ ✅ AdSense onayı alındı (ideal senaryo)
            │ 🎉 Reklam birimleri oluşturulabilir
            │
T+3 weeks   │ 💰 İlk reklam gösterimleri
            │ 📈 Gelir akışı başladı
```

## 🎯 Kritik Kontrol Noktaları

### Checkpoint 1: Deployment Sonrası (T+5 min)

```bash
# URL'leri kontrol et
curl https://orbisastro.online/ads.txt
curl https://orbisastro.online/app-ads.txt

# Beklenen: HTTP 200 + Publisher ID görünür
```

**✅ Başarı Kriteri:** Her iki URL de 200 OK dönmeli

**❌ Hata Durumu:** 404 Not Found

- **Çözüm:** Vercel'de redeploy yap
- **Komut:** `vercel --prod`

---

### Checkpoint 2: Google Taraması (T+24-48 hours)

```
AdSense Dashboard → Sites → orbisastro.online → ads.txt durumu
```

**✅ Başarı Kriteri:** "✓ Doğrulandı" görünmeli

**❌ Hata Durumu:** "Bulunamadı" devam ediyor

- **Çözüm 1:** "Yeniden Tara" butonuna tıkla
- **Çözüm 2:** 24 saat daha bekle (cache)
- **Çözüm 3:** URL'yi manuel kontrol et

---

### Checkpoint 3: Site İncelemesi (T+1-2 weeks)

```
AdSense Dashboard → Home → Onay Durumu
```

**✅ Başarı Kriteri:** "Onaylandı" durumu

**❌ Hata Durumu:** "Müdahale edilmesi gerekiyor" devam ediyor

- **Olası Nedenler:**
  1. İçerik yetersiz (daha fazla blog yazısı ekle)
  2. Trafik düşük (SEO optimizasyonu yap)
  3. Politika ihlali (içeriği gözden geçir)
  4. Site çok yeni (1-2 hafta daha bekle)

---

## 🔄 Alternatif Senaryolar

### Senaryo A: Hızlı Onay (İdeal)

```
T+0     → Deployment
T+24h   → ads.txt doğrulandı
T+1w    → Site onaylandı
T+2w    → Reklam gösterimi başladı
```

### Senaryo B: Normal Onay (Tipik)

```
T+0     → Deployment
T+48h   → ads.txt doğrulandı
T+2w    → Site onaylandı
T+3w    → Reklam gösterimi başladı
```

### Senaryo C: Yavaş Onay (Olası)

```
T+0     → Deployment
T+48h   → ads.txt doğrulandı
T+4w    → Site onaylandı (ek inceleme gerekti)
T+5w    → Reklam gösterimi başladı
```

### Senaryo D: Red (Nadir)

```
T+0     → Deployment
T+48h   → ads.txt doğrulandı
T+2w    → Site reddedildi
         → Nedeni öğren
         → Düzeltmeleri yap
         → Yeniden başvur (T+4w)
```

## 📊 Başarı Metrikleri

### Teknik Metrikler

- ✅ ads.txt HTTP 200 response
- ✅ app-ads.txt HTTP 200 response
- ✅ Content-Type: text/plain
- ✅ Publisher ID doğru
- ✅ Encoding: UTF-8

### İçerik Metrikleri

- ✅ Privacy Policy mevcut
- ✅ Terms of Service mevcut
- ✅ Orijinal içerik (blog)
- ✅ 10+ sayfa (hedef: 20+)
- ✅ Düzenli güncelleme

### Onay Metrikleri

- ⏳ ads.txt doğrulandı (24-48h)
- ⏳ Site incelendi (1-2w)
- ⏳ AdSense onaylandı (1-2w)
- ⏳ Reklam gösterimi (2-3w)

## 🎓 Öğrenme Noktaları

### 1. ads.txt Önemi

- Reklam dolandırıcılığını önler
- Publisher kimliğini doğrular
- AdSense onayı için zorunlu

### 2. Deployment Süreci

- Git push → Vercel otomatik deploy
- Static dosyalar CDN'e dağıtılır
- Header'lar vercel.json'dan gelir

### 3. Google Tarama Mekanizması

- 24-48 saat aralıklarla tarama
- Cache süresi: 24 saat
- Manuel "Yeniden Tara" mümkün

### 4. Onay Süreci

- Otomatik + Manuel inceleme
- İçerik kalitesi önemli
- Politika uygunluğu kritik
- Site yaşı faktör olabilir

## 🔗 İlgili Kaynaklar

- [ADSENSE-SETUP-GUIDE.md](./ADSENSE-SETUP-GUIDE.md) - Detaylı rehber
- [DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md) - Checklist
- [QUICK-REFERENCE.md](./QUICK-REFERENCE.md) - Hızlı referans
- [CHANGES-SUMMARY.md](./CHANGES-SUMMARY.md) - Değişiklik özeti

---

**Not:** Bu akış diyagramı tipik bir deployment senaryosunu gösterir. Gerçek süreçte değişiklikler olabilir.

**Hazırlayan:** Kiro AI Assistant  
**Tarih:** 23 Ocak 2026  
**Durum:** ✅ Deployment için hazır
