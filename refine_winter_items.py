import urllib.request
import urllib.parse
import json
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

APP_ID = "1a3cdfd9-2aec-4b42-8290-1c53603b0012"
ACCESS_KEY = "pk_XkZ5h9MDKSsuVr6T5CnLnlVNvFg3hiR5vMDGrQ75cU5"
AFF_ID = "54d2a438.4bc4abc2.54d2a439.aa1be583"

def fetch_rakuten(query):
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        data = json.loads(res.read().decode('utf-8'))
        items = data.get("Items", [])
        for it in items:
            item_obj = it["Item"]
            price = item_obj.get("itemPrice", 0)
            imgs = item_obj.get("mediumImageUrls", [])
            if price > 0 and imgs:
                raw_img = imgs[0].get("imageUrl", "")
                high_res_img = raw_img
                if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                    high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                elif "?_ex=" in high_res_img:
                    high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                
                aff_url = item_obj.get("affiliateUrl", "") or item_obj.get("itemUrl", "")
                return {
                    "name": item_obj.get("itemName", ""),
                    "price": price,
                    "image": high_res_img,
                    "affiliateUrl": aff_url,
                    "shopName": item_obj.get("shopName", "")
                }
    return None

# Load current data
with open("fetched_3winter_mist_bath_headspa_data.json", "r", encoding="utf-8") as f:
    full_data = json.load(f)

# Fix winter_oil_mist
print("Fixing winter_oil_mist items...")
# Rank 5: RMK フィックスミスト or グローミスト
res = fetch_rakuten("RMK コンディショニング フィックス ミスト") or fetch_rakuten("RMK フィックスミスト")
if res:
    full_data["winter_oil_mist"]["items"][4]["name"] = res["name"]
    full_data["winter_oil_mist"]["items"][4]["price"] = res["price"]
    full_data["winter_oil_mist"]["items"][4]["image"] = res["image"]
    full_data["winter_oil_mist"]["items"][4]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_oil_mist"]["items"][4]["brand"] = "RMK (アールエムケー)"
    print("  ✓ RMK fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 9: コスメデコルテ コンフォート デイミスト バランシング
res = fetch_rakuten("コスメデコルテ コンフォート デイミスト バランシング") or fetch_rakuten("コスメデコルテ デイミスト")
if res:
    full_data["winter_oil_mist"]["items"][8]["name"] = res["name"]
    full_data["winter_oil_mist"]["items"][8]["price"] = res["price"]
    full_data["winter_oil_mist"]["items"][8]["image"] = res["image"]
    full_data["winter_oil_mist"]["items"][8]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_oil_mist"]["items"][8]["brand"] = "DECORTÉ (コスメデコルテ)"
    print("  ✓ DECORTÉ fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 10: ドクタージャルト セラマイディン クリーム ミスト
res = fetch_rakuten("ドクタージャルト セラマイディン クリーム ミスト") or fetch_rakuten("セラマイディン ミスト")
if res:
    full_data["winter_oil_mist"]["items"][9]["name"] = res["name"]
    full_data["winter_oil_mist"]["items"][9]["price"] = res["price"]
    full_data["winter_oil_mist"]["items"][9]["image"] = res["image"]
    full_data["winter_oil_mist"]["items"][9]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_oil_mist"]["items"][9]["brand"] = "Dr.Jart+ (ドクタージャルト)"
    print("  ✓ Dr.Jart+ fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Fix winter_carbonic_bath
print("Fixing winter_carbonic_bath items...")
# Rank 8: アース製薬 温素 白華の湯 入浴剤
res = fetch_rakuten("温素 白華の湯 600g") or fetch_rakuten("温素 入浴剤 白華")
if res:
    full_data["winter_carbonic_bath"]["items"][7]["name"] = res["name"]
    full_data["winter_carbonic_bath"]["items"][7]["price"] = res["price"]
    full_data["winter_carbonic_bath"]["items"][7]["image"] = res["image"]
    full_data["winter_carbonic_bath"]["items"][7]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_carbonic_bath"]["items"][7]["brand"] = "温素 (アース製薬)"
    print("  ✓ 温素 fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 10: バスクリン きき湯 マグネシウム炭酸湯 or クナイプ バスソルト
res = fetch_rakuten("きき湯 マグネシウム炭酸湯 つめかえ") or fetch_rakuten("きき湯 マグネシウム炭酸湯 360g")
if res:
    full_data["winter_carbonic_bath"]["items"][9]["name"] = res["name"]
    full_data["winter_carbonic_bath"]["items"][9]["price"] = res["price"]
    full_data["winter_carbonic_bath"]["items"][9]["image"] = res["image"]
    full_data["winter_carbonic_bath"]["items"][9]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_carbonic_bath"]["items"][9]["brand"] = "きき湯 (バスクリン)"
    print("  ✓ きき湯 fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Fix winter_hot_treatment
print("Fixing winter_hot_treatment items...")
# Rank 2: ヘッドスパ7 トリートメント
res = fetch_rakuten("ヘッドスパ7 トリートメント 215ml") or fetch_rakuten("headspa7") or fetch_rakuten("ヘッドスパ7")
if res:
    full_data["winter_hot_treatment"]["items"][1]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][1]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][1]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][1]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][1]["brand"] = "HEAD SPA 7 (ヘッドスパセブン)"
    print("  ✓ HEAD SPA 7 fixed:", res["name"][:30], res["price"])
else:
    # fallback to TSUBAKI プレミアムリペアマスク
    res2 = fetch_rakuten("TSUBAKI プレミアムリペアマスク")
    if res2:
        full_data["winter_hot_treatment"]["items"][1]["name"] = res2["name"]
        full_data["winter_hot_treatment"]["items"][1]["price"] = res2["price"]
        full_data["winter_hot_treatment"]["items"][1]["image"] = res2["image"]
        full_data["winter_hot_treatment"]["items"][1]["affiliateUrl"] = res2["affiliateUrl"]
        full_data["winter_hot_treatment"]["items"][1]["brand"] = "TSUBAKI (ツバキ / 資生堂)"
        print("  ✓ TSUBAKI (alt) fixed:", res2["name"][:30], res2["price"])
time.sleep(1)

# Rank 5: クンダル トリートメント or ビオリス ウォータートリートメント
res = fetch_rakuten("ビオリス ボタニカル ウォータートリートメント") or fetch_rakuten("SS ビオリス ボタニカル ウォータートリートメント")
if res:
    full_data["winter_hot_treatment"]["items"][4]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][4]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][4]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][4]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][4]["brand"] = "BIOLISS (ビオリス / コーセー)"
    print("  ✓ BIOLISS fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 6: スカルプD ボーテ トリートメント 単品
res = fetch_rakuten("スカルプD ボーテ 薬用トリートメントパック ボリューム") or fetch_rakuten("スカルプD ボーテ 薬用トリートメント")
if res:
    full_data["winter_hot_treatment"]["items"][5]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][5]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][5]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][5]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][5]["brand"] = "スカルプD ボーテ (アンファー)"
    print("  ✓ スカルプD ボーテ fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 7: fino プレミアムタッチ 浸透美容液ヘアマスク
res = fetch_rakuten("fino フィーノ プレミアムタッチ 浸透美容液ヘアマスク") or fetch_rakuten("フィーノ 浸透美容液ヘアマスク 230g")
if res:
    full_data["winter_hot_treatment"]["items"][6]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][6]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][6]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][6]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][6]["brand"] = "fino (フィーノ / ファイントゥデイ)"
    print("  ✓ fino fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 8: エッセンシャル ザビューティ バリアトリートメント
res = fetch_rakuten("エッセンシャル ザビューティ 素髪を守るバリアトリートメント") or fetch_rakuten("エッセンシャル バリアトリートメント")
if res:
    full_data["winter_hot_treatment"]["items"][7]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][7]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][7]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][7]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][7]["brand"] = "Essential (エッセンシャル / 花王)"
    print("  ✓ Essential fixed:", res["name"][:30], res["price"])
time.sleep(1)

# Rank 10: YOLU カームナイトリペア ジェルヘアマスク
res = fetch_rakuten("YOLU ヨル カームナイトリペア ジェルヘアマスク") or fetch_rakuten("ヨル カームナイトリペア ジェルヘアマスク")
if res:
    full_data["winter_hot_treatment"]["items"][9]["name"] = res["name"]
    full_data["winter_hot_treatment"]["items"][9]["price"] = res["price"]
    full_data["winter_hot_treatment"]["items"][9]["image"] = res["image"]
    full_data["winter_hot_treatment"]["items"][9]["affiliateUrl"] = res["affiliateUrl"]
    full_data["winter_hot_treatment"]["items"][9]["brand"] = "YOLU (ヨル / I-ne)"
    print("  ✓ YOLU fixed:", res["name"][:30], res["price"])

# Save refined data
with open("fetched_3winter_mist_bath_headspa_data_perfect.json", "w", encoding="utf-8") as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print("\nRefined and perfected data saved to fetched_3winter_mist_bath_headspa_data_perfect.json")
