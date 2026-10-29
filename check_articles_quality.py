import os
import json
import re

files_to_check = [
    "winter-highlighter.html",
    "winter-hair-oil.html",
    "winter-lip-mask.html",
    "winter-hair-milk.html",
    "winter-cushion-foundation.html",
    "winter-body-scrub.html"
]

all_passed = True

for fname in files_to_check:
    print(f"\n==========================================")
    print(f"Checking {fname} ...")
    print(f"==========================================")
    
    if not os.path.exists(fname):
        print(f"❌ File does not exist: {fname}")
        all_passed = False
        continue
    
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()
    
    # 1. ファイルサイズ & 本文文字数
    clean_text = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
    clean_text = re.sub(r'<style.*?</style>', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'<[^>]+>', '', clean_text)
    clean_text = re.sub(r'\s+', '', clean_text)
    char_count = len(clean_text)
    print(f"File size: {len(html):,} bytes | Extracted text length: {char_count:,} characters")
    if char_count < 3000:
        print(f"❌ Text length is less than 3,000 characters! ({char_count})")
        all_passed = False
    else:
        print(f"✓ Text length requirement passed ({char_count:,} > 3,000 chars)")
        
    # 2. JSON-LD 構造化データの検証
    json_ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.DOTALL)
    if not json_ld_matches:
        print(f"❌ No JSON-LD structured data found!")
        all_passed = False
    else:
        for idx, j_str in enumerate(json_ld_matches):
            try:
                j_obj = json.loads(j_str.strip())
                print(f"✓ JSON-LD #{idx+1} valid: type={j_obj.get('@type')}, headline={j_obj.get('headline', '')[:30]}...")
            except Exception as e:
                print(f"❌ JSON-LD #{idx+1} syntax error: {e}")
                all_passed = False
                
    # 3. 楽天画像・アフィリエイトリンク・価格の検証
    img_matches = re.findall(r'<img[^>]*class="product-img"[^>]*>', html)
    print(f"Product cards with images: {len(img_matches)}/10")
    if len(img_matches) != 10:
        print("❌ Not all 10 products have product-img class!")
        all_passed = False
    
    aff_matches = re.findall(r'href="([^"]*)"[^>]*class="rakuten-btn"', html)
    print(f"Product cards with affiliate buttons: {len(aff_matches)}/10")
    if len(aff_matches) != 10:
        print("❌ Not all 10 products have affiliate buttons!")
        all_passed = False
    else:
        for a_url in aff_matches:
            if not a_url.startswith("http"):
                print(f"❌ Invalid affiliate URL: {a_url}")
                all_passed = False
                
    zero_prices = len(re.findall(r'¥0', html))
    if zero_prices > 0:
        print(f"❌ Found zero prices: {zero_prices}")
        all_passed = False
    else:
        print("✓ All product prices are valid (> ¥0)")
        
    # 4. OGPタグの検証
    og_title = bool(re.search(r'<meta property="og:title"', html))
    og_desc = bool(re.search(r'<meta property="og:description"', html))
    og_img = bool(re.search(r'<meta property="og:image"', html))
    canonical = bool(re.search(r'<link rel="canonical"', html))
    print(f"SEO Meta: og:title={og_title}, og:desc={og_desc}, og:image={og_img}, canonical={canonical}")
    if not (og_title and og_desc and og_img and canonical):
        print("❌ Missing critical SEO / OGP meta tags!")
        all_passed = False

if all_passed:
    print("\n🎉 ALL CHECKED ARTICLES PASSED ALL RIGOROUS CHECKS!")
else:
    print("\n⚠️ SOME CHECKS FAILED! Please inspect.")
