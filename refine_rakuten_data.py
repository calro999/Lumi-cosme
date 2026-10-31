import json
import urllib.request
import urllib.parse
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

APP_ID = "1a3cdfd9-2aec-4b42-8290-1c53603b0012"
ACCESS_KEY = "pk_XkZ5h9MDKSsuVr6T5CnLnlVNvFg3hiR5vMDGrQ75cU5"
AFF_ID = "54d2a438.4bc4abc2.54d2a439.aa1be583"

with open("rakuten_3winter_latest_topics_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_single(query):
    time.sleep(1)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                res_data = json.loads(res.read().decode('utf-8'))
                items = res_data.get("Items", [])
                if items:
                    chosen = items[0]["Item"]
                    raw_img = chosen.get("mediumImageUrls", [{}])[0].get("imageUrl", "")
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    return {
                        "rakuten_item_name": chosen.get("itemName", ""),
                        "price": chosen.get("itemPrice", 0),
                        "image_url": high_res_img,
                        "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                        "review_count": chosen.get("reviewCount", 0),
                        "review_average": chosen.get("reviewAverage", "0.0"),
                        "shop_name": chosen.get("shopName", "")
                    }
        except Exception as e:
            print(f"Error ({attempt+1}) fetching {query}: {e}")
            time.sleep(2)
    return None

# 1. クレンジングクリーム Rank 4: アルビオン エクシア クレンジングクリーム
print("Updating Cleansing Cream Rank 4 (ALBION)...")
albion_res = fetch_single("アルビオン エクシア クレンジングクリーム")
if albion_res:
    data["winter_cleansing_cream"]["items"][3]["brand"] = "ALBION (アルビオン)"
    data["winter_cleansing_cream"]["items"][3]["name"] = "エクシア クレンジングクリーム 150g (濃厚リッチなベースが肌を包み込みキメの奥の老廃物まで優しくオフする至高のエイジングケア)"
    data["winter_cleansing_cream"]["items"][3].update(albion_res)
    print("  -> Updated ALBION successfully!")

# 2. ナイアシンアミド Rank 6: 肌ラボ 極潤 薬用ハリパーフェクトゲル
print("Updating Niacinamide Serum Rank 6 (Hada Labo)...")
hadalabo_res = fetch_single("肌ラボ 極潤 薬用 ハリ パーフェクトゲル")
if hadalabo_res:
    data["winter_niacinamide_serum"]["items"][5]["brand"] = "肌ラボ (ロート製薬)"
    data["winter_niacinamide_serum"]["items"][5]["name"] = "極潤 薬用ハリパーフェクトゲル 100g (有効成分ナイアシンアミド×3種のヒアルロン酸配合・シワ改善とシミ対策をプチプラで両立)"
    data["winter_niacinamide_serum"]["items"][5].update(hadalabo_res)
    print("  -> Updated Hada Labo successfully!")

# 3. ナイアシンアミド Rank 7: ディセンシア リンクルO/L コンセントレート
print("Updating Niacinamide Serum Rank 7 (DECENCIA)...")
decencia_res = fetch_single("ディセンシア リンクル コンセントレート")
if decencia_res:
    data["winter_niacinamide_serum"]["items"][6]["brand"] = "DECENCIA (ディセンシア)"
    data["winter_niacinamide_serum"]["items"][6]["name"] = "リンクルO/L コンセントレート 30ml (有効成分D-リンクルアミド・ナイアシンアミド配合・冬の敏感肌の表情ジワを跳ね返すオイル状美容液)"
    data["winter_niacinamide_serum"]["items"][6].update(decencia_res)
    print("  -> Updated DECENCIA successfully!")

# 4. ナイアシンアミド Rank 8: ドクターケイ 薬用Cリンクルホワイトミルク
print("Updating Niacinamide Serum Rank 8 (Dr.K)...")
drk_res = fetch_single("ドクターケイ 薬用Cリンクルホワイトミルク")
if drk_res:
    data["winter_niacinamide_serum"]["items"][7]["brand"] = "Dr.K (ドクターケイ)"
    data["winter_niacinamide_serum"]["items"][7]["name"] = "薬用Cリンクルホワイトミルク 70ml (シワ改善美白有効成分ナイアシンアミド×カフェイン×ビタミンカクテル配合・冬の毛穴とくすみを晴らす)"
    data["winter_niacinamide_serum"]["items"][7].update(drk_res)
    print("  -> Updated Dr.K successfully!")

with open("rakuten_3winter_latest_topics_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nRefinements complete! Saved to rakuten_3winter_latest_topics_data.json")
