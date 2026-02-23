#!/bin/bash

# ORBIS AdSense/AdMob Setup Verification Script
# Bu script, ads.txt dosyalarının doğru şekilde oluşturulduğunu ve
# deployment sonrası erişilebilir olduğunu kontrol eder.

echo "🔍 ORBIS AdSense/AdMob Setup Verification"
echo "=========================================="
echo ""

# Renk kodları
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Local dosya kontrolü
echo "📁 Step 1: Local File Check"
echo "----------------------------"

if [ -f "ads.txt" ]; then
    echo -e "${GREEN}✓${NC} ads.txt found"
    echo "   Content:"
    cat ads.txt | sed 's/^/   /'
else
    echo -e "${RED}✗${NC} ads.txt NOT found"
fi
echo ""

if [ -f "app-ads.txt" ]; then
    echo -e "${GREEN}✓${NC} app-ads.txt found"
    echo "   Content:"
    cat app-ads.txt | sed 's/^/   /'
else
    echo -e "${RED}✗${NC} app-ads.txt NOT found"
fi
echo ""

# 2. Publisher ID kontrolü
echo "🔑 Step 2: Publisher ID Verification"
echo "-------------------------------------"

PUBLISHER_ID="pub-2444093901783574"
if grep -q "$PUBLISHER_ID" ads.txt 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Publisher ID found in ads.txt: $PUBLISHER_ID"
else
    echo -e "${RED}✗${NC} Publisher ID NOT found in ads.txt"
fi

if grep -q "$PUBLISHER_ID" app-ads.txt 2>/dev/null; then
    echo -e "${GREEN}✓${NC} Publisher ID found in app-ads.txt: $PUBLISHER_ID"
else
    echo -e "${RED}✗${NC} Publisher ID NOT found in app-ads.txt"
fi
echo ""

# 3. AdSense code kontrolü (index.html)
echo "📄 Step 3: AdSense Code in HTML"
echo "--------------------------------"

if grep -q "ca-pub-2444093901783574" index.html; then
    echo -e "${GREEN}✓${NC} AdSense code found in index.html"
else
    echo -e "${RED}✗${NC} AdSense code NOT found in index.html"
fi
echo ""

# 4. Vercel config kontrolü
echo "⚙️  Step 4: Vercel Configuration"
echo "--------------------------------"

if grep -q "ads.txt" vercel.json; then
    echo -e "${GREEN}✓${NC} ads.txt header configuration found in vercel.json"
else
    echo -e "${YELLOW}⚠${NC}  ads.txt header configuration NOT found in vercel.json"
fi
echo ""

# 5. Remote URL kontrolü (deployment sonrası)
echo "🌐 Step 5: Remote URL Check (Post-Deployment)"
echo "----------------------------------------------"
echo -e "${YELLOW}ℹ${NC}  This check requires the site to be deployed"
echo ""

DOMAIN="https://orbisastro.online"

echo "Checking: $DOMAIN/ads.txt"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/ads.txt" 2>/dev/null)
if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✓${NC} ads.txt is accessible (HTTP $HTTP_CODE)"
    echo "   Content:"
    curl -s "$DOMAIN/ads.txt" | sed 's/^/   /'
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "${YELLOW}⚠${NC}  Cannot connect to $DOMAIN (not deployed yet or network issue)"
else
    echo -e "${RED}✗${NC} ads.txt returned HTTP $HTTP_CODE"
fi
echo ""

echo "Checking: $DOMAIN/app-ads.txt"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$DOMAIN/app-ads.txt" 2>/dev/null)
if [ "$HTTP_CODE" = "200" ]; then
    echo -e "${GREEN}✓${NC} app-ads.txt is accessible (HTTP $HTTP_CODE)"
    echo "   Content:"
    curl -s "$DOMAIN/app-ads.txt" | sed 's/^/   /'
elif [ "$HTTP_CODE" = "000" ]; then
    echo -e "${YELLOW}⚠${NC}  Cannot connect to $DOMAIN (not deployed yet or network issue)"
else
    echo -e "${RED}✗${NC} app-ads.txt returned HTTP $HTTP_CODE"
fi
echo ""

# 6. Privacy Policy kontrolü
echo "📋 Step 6: Privacy Policy Check"
echo "--------------------------------"

if [ -f "legal/privacy.html" ]; then
    echo -e "${GREEN}✓${NC} Privacy Policy found"
    if grep -q -i "cookie\|çerez" legal/privacy.html; then
        echo -e "${GREEN}✓${NC} Cookie/Çerez information found in Privacy Policy"
    else
        echo -e "${YELLOW}⚠${NC}  Cookie/Çerez information NOT found in Privacy Policy"
    fi
    if grep -q -i "admob\|adsense\|reklam\|advertisement" legal/privacy.html; then
        echo -e "${GREEN}✓${NC} Ad/Reklam information found in Privacy Policy"
    else
        echo -e "${YELLOW}⚠${NC}  Ad/Reklam information NOT found in Privacy Policy"
    fi
else
    echo -e "${RED}✗${NC} Privacy Policy NOT found"
fi
echo ""

# 7. Özet
echo "📊 Summary"
echo "=========="
echo ""
echo "Next Steps:"
echo "1. If local checks pass: git add, commit, and push"
echo "2. Wait for Vercel deployment (automatic)"
echo "3. Run this script again to verify remote URLs"
echo "4. Check AdSense dashboard after 24-48 hours"
echo ""
echo "Useful Commands:"
echo "  git add ads.txt app-ads.txt vercel.json"
echo "  git commit -m 'feat: Add ads.txt for AdSense approval'"
echo "  git push origin main"
echo ""
echo "Verification URLs:"
echo "  - https://orbisastro.online/ads.txt"
echo "  - https://orbisastro.online/app-ads.txt"
echo ""
