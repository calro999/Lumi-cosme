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

with open("rakuten_3winter_body_booster_shampoo_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_single_item(query):
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        for it in items:
            item_obj = it["Item"]
            if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                raw_img = item_obj["mediumImageUrls"][0].get("imageUrl", "")
                high_res_img = raw_img
                if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                    high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                elif "?_ex=" in high_res_img:
                    high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                
                aff_url = item_obj.get("affiliateUrl", "") or item_obj.get("itemUrl", "")
                return {
                    "rakuten_item_name": item_obj.get("itemName", ""),
                    "price": item_obj.get("itemPrice", 0),
                    "image_url": high_res_img,
                    "affiliate_url": aff_url,
                    "shop_name": item_obj.get("shopName", "")
                }
    return None

fixes = [
    # winter_body_cream
    ("winter_body_cream", 6, "ローラメルシエ アンバーバニラ ボディクリーム"),
    ("winter_body_cream", 7, "アベンヌ トリクセラ フルイド"),
    ("winter_body_cream", 10, "ジョンソンボディケア エクストラケア アロマミルク 500ml"),
    
    # winter_booster_oil
    ("winter_booster_oil", 5, "FEMMUE アイディアルオイル"),
    ("winter_booster_oil", 8, "カネボウ スキングロスオイルウォーター"),
    ("winter_booster_oil", 9, "アテニア エッセンスオイル"),
    
    # winter_moisture_shampoo
    ("winter_moisture_shampoo", 2, "ケラスターゼ ユイルスブリム シャンプー"),
    ("winter_moisture_shampoo", 3, "ボタニスト プレミアム シャンプー"),
    ("winter_moisture_shampoo", 5, "エッセンシャル プレミアム バリアシャンプー"),
]

for cat_key, rank, query in fixes:
    print(f"Fixing {cat_key} Rank {rank} with query: {query}...")
    for attempt in range(5):
        try:
            res = fetch_single_item(query)
            if res:
                for idx, it in enumerate(data[cat_key]["items"]):
                    if it["rank"] == rank:
                        data[cat_key]["items"][idx]["rakuten_item_name"] = res["rakuten_item_name"]
                        data[cat_key]["items"][idx]["price"] = res["price"]
                        data[cat_key]["items"][idx]["image_url"] = res["image_url"]
                        data[cat_key]["items"][idx]["affiliate_url"] = res["affiliate_url"]
                        data[cat_key]["items"][idx]["shop_name"] = res["shop_name"]
                        data[cat_key]["items"][idx]["query_used"] = query
                        print(f" -> Successfully updated: {res['rakuten_item_name'][:30]} | ¥{res['price']:,} | {res['image_url'][:40]}")
                        break
                time.sleep(1.2) # APIレート制限対策
                break
            else:
                print(f" -> Not found for {query}, retrying...")
                time.sleep(1.5)
        except Exception as e:
            print(f" -> Error (attempt {attempt+1}): {e}")
            time.sleep(2.0)

with open("rakuten_3winter_body_booster_shampoo_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nAll items successfully fixed and verified!")
