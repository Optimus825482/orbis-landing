# ORBIS AdSense/AdMob Setup Verification Script (PowerShell)
# Bu script, ads.txt dosyalarının doğru şekilde oluşturulduğunu ve
# deployment sonrası erişilebilir olduğunu kontrol eder.

Write-Host "🔍 ORBIS AdSense/AdMob Setup Verification" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# 1. Local dosya kontrolü
Write-Host "📁 Step 1: Local File Check" -ForegroundColor Yellow
Write-Host "----------------------------"

if (Test-Path "ads.txt") {
    Write-Host "✓ ads.txt found" -ForegroundColor Green
    Write-Host "   Content:"
    Get-Content "ads.txt" | ForEach-Object { Write-Host "   $_" }
} else {
    Write-Host "✗ ads.txt NOT found" -ForegroundColor Red
}
Write-Host ""

if (Test-Path "app-ads.txt") {
    Write-Host "✓ app-ads.txt found" -ForegroundColor Green
    Write-Host "   Content:"
    Get-Content "app-ads.txt" | ForEach-Object { Write-Host "   $_" }
} else {
    Write-Host "✗ app-ads.txt NOT found" -ForegroundColor Red
}
Write-Host ""

# 2. Publisher ID kontrolü
Write-Host "🔑 Step 2: Publisher ID Verification" -ForegroundColor Yellow
Write-Host "-------------------------------------"

$PUBLISHER_ID = "pub-2444093901783574"
if ((Test-Path "ads.txt") -and (Select-String -Path "ads.txt" -Pattern $PUBLISHER_ID -Quiet)) {
    Write-Host "✓ Publisher ID found in ads.txt: $PUBLISHER_ID" -ForegroundColor Green
} else {
    Write-Host "✗ Publisher ID NOT found in ads.txt" -ForegroundColor Red
}

if ((Test-Path "app-ads.txt") -and (Select-String -Path "app-ads.txt" -Pattern $PUBLISHER_ID -Quiet)) {
    Write-Host "✓ Publisher ID found in app-ads.txt: $PUBLISHER_ID" -ForegroundColor Green
} else {
    Write-Host "✗ Publisher ID NOT found in app-ads.txt" -ForegroundColor Red
}
Write-Host ""

# 3. AdSense code kontrolü (index.html)
Write-Host "📄 Step 3: AdSense Code in HTML" -ForegroundColor Yellow
Write-Host "--------------------------------"

if ((Test-Path "index.html") -and (Select-String -Path "index.html" -Pattern "ca-pub-2444093901783574" -Quiet)) {
    Write-Host "✓ AdSense code found in index.html" -ForegroundColor Green
} else {
    Write-Host "✗ AdSense code NOT found in index.html" -ForegroundColor Red
}
Write-Host ""

# 4. Vercel config kontrolü
Write-Host "⚙️  Step 4: Vercel Configuration" -ForegroundColor Yellow
Write-Host "--------------------------------"

if ((Test-Path "vercel.json") -and (Select-String -Path "vercel.json" -Pattern "ads.txt" -Quiet)) {
    Write-Host "✓ ads.txt header configuration found in vercel.json" -ForegroundColor Green
} else {
    Write-Host "⚠ ads.txt header configuration NOT found in vercel.json" -ForegroundColor Yellow
}
Write-Host ""

# 5. Remote URL kontrolü (deployment sonrası)
Write-Host "🌐 Step 5: Remote URL Check (Post-Deployment)" -ForegroundColor Yellow
Write-Host "----------------------------------------------"
Write-Host "ℹ  This check requires the site to be deployed" -ForegroundColor Yellow
Write-Host ""

$DOMAIN = "https://orbisastro.online"

Write-Host "Checking: $DOMAIN/ads.txt"
try {
    $response = Invoke-WebRequest -Uri "$DOMAIN/ads.txt" -UseBasicParsing -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "✓ ads.txt is accessible (HTTP $($response.StatusCode))" -ForegroundColor Green
        Write-Host "   Content:"
        $response.Content -split "`n" | ForEach-Object { Write-Host "   $_" }
    }
} catch {
    if ($_.Exception.Response) {
        Write-Host "✗ ads.txt returned HTTP $($_.Exception.Response.StatusCode.Value__)" -ForegroundColor Red
    } else {
        Write-Host "⚠ Cannot connect to $DOMAIN (not deployed yet or network issue)" -ForegroundColor Yellow
    }
}
Write-Host ""

Write-Host "Checking: $DOMAIN/app-ads.txt"
try {
    $response = Invoke-WebRequest -Uri "$DOMAIN/app-ads.txt" -UseBasicParsing -ErrorAction Stop
    if ($response.StatusCode -eq 200) {
        Write-Host "✓ app-ads.txt is accessible (HTTP $($response.StatusCode))" -ForegroundColor Green
        Write-Host "   Content:"
        $response.Content -split "`n" | ForEach-Object { Write-Host "   $_" }
    }
} catch {
    if ($_.Exception.Response) {
        Write-Host "✗ app-ads.txt returned HTTP $($_.Exception.Response.StatusCode.Value__)" -ForegroundColor Red
    } else {
        Write-Host "⚠ Cannot connect to $DOMAIN (not deployed yet or network issue)" -ForegroundColor Yellow
    }
}
Write-Host ""

# 6. Privacy Policy kontrolü
Write-Host "📋 Step 6: Privacy Policy Check" -ForegroundColor Yellow
Write-Host "--------------------------------"

if (Test-Path "legal/privacy.html") {
    Write-Host "✓ Privacy Policy found" -ForegroundColor Green
    $privacyContent = Get-Content "legal/privacy.html" -Raw
    if ($privacyContent -match "cookie|çerez") {
        Write-Host "✓ Cookie/Çerez information found in Privacy Policy" -ForegroundColor Green
    } else {
        Write-Host "⚠ Cookie/Çerez information NOT found in Privacy Policy" -ForegroundColor Yellow
    }
    if ($privacyContent -match "admob|adsense|reklam|advertisement") {
        Write-Host "✓ Ad/Reklam information found in Privacy Policy" -ForegroundColor Green
    } else {
        Write-Host "⚠ Ad/Reklam information NOT found in Privacy Policy" -ForegroundColor Yellow
    }
} else {
    Write-Host "✗ Privacy Policy NOT found" -ForegroundColor Red
}
Write-Host ""

# 7. Özet
Write-Host "📊 Summary" -ForegroundColor Cyan
Write-Host "=========="
Write-Host ""
Write-Host "Next Steps:"
Write-Host "1. If local checks pass: git add, commit, and push"
Write-Host "2. Wait for Vercel deployment (automatic)"
Write-Host "3. Run this script again to verify remote URLs"
Write-Host "4. Check AdSense dashboard after 24-48 hours"
Write-Host ""
Write-Host "Useful Commands:"
Write-Host "  git add ads.txt app-ads.txt vercel.json"
Write-Host "  git commit -m 'feat: Add ads.txt for AdSense approval'"
Write-Host "  git push origin main"
Write-Host ""
Write-Host "Verification URLs:"
Write-Host "  - https://orbisastro.online/ads.txt"
Write-Host "  - https://orbisastro.online/app-ads.txt"
Write-Host ""
