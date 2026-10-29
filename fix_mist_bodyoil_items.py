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

with open("rakuten_mist_lipoil_bodyoil_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 更新対象
updates = [
    {
        "category": "winter_make_keep_mist",
        "rank": 3,
        "query": "ディオール フィックス ミスト",
        "brand": "DIOR (クリスチャン・ディオール)",
        "name": "ディオールスキン フォーエヴァー メイクアップ フィックス ミスト (野生パンジーエキス配合・97%自然由来成分で一日中みずみずしくフィックス)"
    },
    {
        "category": "winter_make_keep_mist",
        "rank": 7,
        "query": "アディクション スムースグロウ ロックミスト",
        "brand": "ADDICTION (アディクション)",
        "name": "スムースグロウ ロックミスト (微細ミスト・オリーブ果実油などの植物美容オイルが乾燥崩れを完全ブロックしツヤを固定)"
    },
    {
        "category": "winter_make_keep_mist",
        "rank": 9,
        "query": "マジョリカマジョルカ モイストカクテルフィクサー",
        "brand": "MAJOLICA MAJORCA (資生堂 / マジョリカ マジョルカ)",
        "name": "モイストカクテルフィクサー EX (化粧水・美容液・オイルの3層構造・冬の乾燥崩れと粉浮きを完全に防ぐ高保湿カクテルミスト)"
    },
    {
        "category": "winter_body_oil",
        "rank": 5,
        "query": "クナイプ ビオ オイル 100ml",
        "brand": "Kneipp (クナイプ)",
        "name": "クナイプ ビオ オイル (100%天然由来・オーガニックサフラワー油×オリーブ油配合で冬の乾燥キメ乱れや完治したキズ跡をしっとり滑らかにケア)"
    }
]

def fetch_single(query):
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                d = json.loads(res.read().decode('utf-8'))
                items = d.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]
                    
                    raw_img = chosen.get("mediumImageUrls", [{}])[0].get("imageUrl", "")
                    high_res = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res:
                        high_res = high_res.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res:
                        high_res = high_res.split("?_ex=")[0] + "?_ex=600x600"
                        
                    return {
                        "rakuten_item_name": chosen.get("itemName", ""),
                        "price": chosen.get("itemPrice", 0),
                        "image_url": high_res,
                        "affiliate_url": chosen.get("affiliateUrl", "") or chosen.get("itemUrl", ""),
                        "review_count": chosen.get("reviewCount", 0),
                        "review_average": str(chosen.get("reviewAverage", "0.0")),
                        "shop_name": chosen.get("shopName", "")
                    }
        except Exception as e:
            print(f"Error on {query}: {e}")
        time.sleep(1.5)
    return None

for up in updates:
    time.sleep(1.2)
    print(f"Updating {up['category']} rank {up['rank']} ({up['query']})...")
    res = fetch_single(up["query"])
    if res:
        print(f"  -> Found: {res['rakuten_item_name'][:35]} | ¥{res['price']} | {res['image_url'][:40]}")
        # update in data
        target_list = data[up["category"]]["items"]
        for idx, item in enumerate(target_list):
            if item["rank"] == up["rank"]:
                target_list[idx]["brand"] = up["brand"]
                target_list[idx]["name"] = up["name"]
                target_list[idx]["search_query"] = up["query"]
                target_list[idx]["rakuten_item_name"] = res["rakuten_item_name"]
                target_list[idx]["price"] = res["price"]
                target_list[idx]["image_url"] = res["image_url"]
                target_list[idx]["affiliate_url"] = res["affiliate_url"]
                target_list[idx]["review_count"] = res["review_count"]
                target_list[idx]["review_average"] = res["review_average"]
                target_list[idx]["shop_name"] = res["shop_name"]
                break

with open("rakuten_mist_lipoil_bodyoil_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated all target items!")
