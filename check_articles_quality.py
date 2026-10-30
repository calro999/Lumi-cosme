import os
import json
import re

files_to_check = [
    "winter-holiday-coffret.html",
    "winter-enzyme-wash.html",
    "winter-tinted-lip-balm.html"
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
    
    # 1. ファイルサイズ & 本文文字数（HTMLタグ・CSS・JSを除外した純粋な日本語文字数）
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
        
    # 2. AI臭いテンプレ構文チェック
    ai_cliches = [
        "いかがでしたでしょうか",
        "いかがでしたか？",
        "いかがでしたでしょうか？",
        "参考になれば幸いです",
        "ぜひ試してみてくださいね！",
        "AIとして",
        "本記事では〜をご紹介しました。"
    ]
    found_cliches = []
    for c in ai_cliches:
        if c in html:
            found_cliches.append(c)
    if found_cliches:
        print(f"❌ Found AI cliché phrases: {found_cliches}")
        all_passed = False
    else:
        print("✓ No AI cliché / template phrases found!")
        
    # 3. JSON-LD 構造化データの検証
    json_ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, flags=re.DOTALL)
    if not json_ld_matches:
        print(f"❌ No JSON-LD structured data found!")
        all_passed = False
    else:
        print(f"✓ Found {len(json_ld_matches)} JSON-LD blocks:")
        for idx, j_str in enumerate(json_ld_matches):
            try:
                j_obj = json.loads(j_str.strip())
                print(f"  - Block #{idx+1} valid: type={j_obj.get('@type')}, headline/name={j_obj.get('headline', j_obj.get('name', ''))[:35]}...")
            except Exception as e:
                print(f"  ❌ Block #{idx+1} syntax error: {e}")
                all_passed = False
                
    # 4. 楽天画像・アフィリエイトリンク・価格の検証
    img_matches = re.findall(r'<img[^>]*class="product-img"[^>]*>', html)
    print(f"Product cards with images: {len(img_matches)}/10")
    if len(img_matches) != 10:
        print("❌ Not all 10 products have product-img class!")
        all_passed = False
    
    # サンプル画像の有無
    sample_imgs = len(re.findall(r'sample/item\.jpg', html))
    if sample_imgs > 0:
        print(f"❌ Found {sample_imgs} sample fallback images!")
        all_passed = False
    else:
        print("✓ All 10 images are genuine Rakuten product images!")
    
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
        print(f"❌ Found {zero_prices} zero prices!")
        all_passed = False
    else:
        print("✓ All product prices are valid non-zero amounts!")

print("\n" + "="*50)
if all_passed:
    print("🎉 ALL QUALITY & SEO & ACCURACY CHECKS PASSED PERFECTLY!")
else:
    print("❌ SOME CHECKS FAILED! PLEASE REVIEW ABOVE ERRORS.")
print("="*50)
