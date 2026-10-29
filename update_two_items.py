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

with open("rakuten_hair_cushion_scrub_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_single(query):
    time.sleep(1.0)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=1&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        if items:
            raw_item = items[0]["Item"]
            raw_img = raw_item["mediumImageUrls"][0].get("imageUrl", "") if raw_item.get("mediumImageUrls") else ""
            high_res_img = raw_img
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in high_res_img:
                high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
            return {
                "official_item_name": raw_item.get("itemName", ""),
                "price": raw_item.get("itemPrice", 0),
                "image_url": high_res_img,
                "affiliate_url": raw_item.get("affiliateUrl", ""),
                "shop_name": raw_item.get("shopName", ""),
                "review_count": raw_item.get("reviewCount", 0),
                "review_average": raw_item.get("reviewAverage", 0.0)
            }
    return None

# ヘアミルク Rank 7: BOTANIST ボタニカル ヘアミルク モイスト
print("Updating Hair Milk Rank 7 to BOTANIST...")
res_hair = fetch_single("ボタニスト ヘアミルク モイスト")
if res_hair:
    data["winter_hair_milk"]["items"][6] = {
        "rank": 7,
        "brand": "BOTANIST (ボタニスト)",
        "name": "ボタニカル ヘアミルク モイスト (植物由来スクワラン×セラミド・しっとり潤いまとまり)",
        "official_item_name": res_hair["official_item_name"],
        "price": res_hair["price"],
        "image_url": res_hair["image_url"],
        "affiliate_url": res_hair["affiliate_url"],
        "shop_name": res_hair["shop_name"],
        "review_count": res_hair["review_count"],
        "review_average": res_hair["review_average"]
    }
    print("✓ Updated Hair Milk Rank 7")

# ボディスクラブ Rank 3: LUSH パワーマスク SP
print("Updating Body Scrub Rank 3 to LUSH...")
res_scrub = fetch_single("LUSH パワーマスク SP")
if res_scrub:
    data["winter_body_scrub"]["items"][2] = {
        "rank": 3,
        "brand": "LUSH (ラッシュ)",
        "name": "パワーマスク SP (ハチミツ高配合×月見草オイル・全身ツルスベ清涼スクラブ)",
        "official_item_name": res_scrub["official_item_name"],
        "price": res_scrub["price"],
        "image_url": res_scrub["image_url"],
        "affiliate_url": res_scrub["affiliate_url"],
        "shop_name": res_scrub["shop_name"],
        "review_count": res_scrub["review_count"],
        "review_average": res_scrub["review_average"]
    }
    print("✓ Updated Body Scrub Rank 3")

with open("rakuten_hair_cushion_scrub_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All done!")
