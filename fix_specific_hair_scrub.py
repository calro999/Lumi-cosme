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
    time.sleep(0.5)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
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

# 1. ルベル シーソー リペアミルク モイスト
print("Refetching LebeL SEE SAW repair milk...")
res1 = fetch_single("ルベル SEE/SAW リペアミルク モイスト 100ml")
if res1:
    print("Found res1:", res1["official_item_name"][:30], res1["price"])
    data["winter_hair_milk"]["items"][6]["official_item_name"] = res1["official_item_name"]
    data["winter_hair_milk"]["items"][6]["price"] = res1["price"]
    data["winter_hair_milk"]["items"][6]["image_url"] = res1["image_url"]
    data["winter_hair_milk"]["items"][6]["affiliate_url"] = res1["affiliate_url"]
    data["winter_hair_milk"]["items"][6]["shop_name"] = res1["shop_name"]
    data["winter_hair_milk"]["items"][6]["review_count"] = res1["review_count"]
    data["winter_hair_milk"]["items"][6]["review_average"] = res1["review_average"]

# 2. オゥパラディ ボディスクラブ
print("Refetching AUX PARADIS body scrub...")
res2 = fetch_single("オゥパラディ ボディスクラブ 200g")
if not res2 or "スクラブ" not in res2["official_item_name"]:
    res2 = fetch_single("AUX PARADIS スクラブ")
if res2:
    print("Found res2:", res2["official_item_name"][:30], res2["price"])
    data["winter_body_scrub"]["items"][2]["official_item_name"] = res2["official_item_name"]
    data["winter_body_scrub"]["items"][2]["price"] = res2["price"]
    data["winter_body_scrub"]["items"][2]["image_url"] = res2["image_url"]
    data["winter_body_scrub"]["items"][2]["affiliate_url"] = res2["affiliate_url"]
    data["winter_body_scrub"]["items"][2]["shop_name"] = res2["shop_name"]
    data["winter_body_scrub"]["items"][2]["review_count"] = res2["review_count"]
    data["winter_body_scrub"]["items"][2]["review_average"] = res2["review_average"]

# 3. WEEED ブリススクラブ 単品
print("Refetching WEEED bliss scrub single...")
res3 = fetch_single("ウィード WEEED ブリススクラブ 360g 単品")
if not res3 or res3["price"] > 7000:
    res3 = fetch_single("WEEED ブリススクラブ 120g") or fetch_single("ウィード ブリススクラブ")
if res3:
    print("Found res3:", res3["official_item_name"][:30], res3["price"])
    data["winter_body_scrub"]["items"][7]["official_item_name"] = res3["official_item_name"]
    data["winter_body_scrub"]["items"][7]["price"] = res3["price"]
    data["winter_body_scrub"]["items"][7]["image_url"] = res3["image_url"]
    data["winter_body_scrub"]["items"][7]["affiliate_url"] = res3["affiliate_url"]
    data["winter_body_scrub"]["items"][7]["shop_name"] = res3["shop_name"]
    data["winter_body_scrub"]["items"][7]["review_count"] = res3["review_count"]
    data["winter_body_scrub"]["items"][7]["review_average"] = res3["review_average"]

# 4. ザボディショップ ボディスクラブ シア
print("Refetching THE BODY SHOP shea scrub...")
res4 = fetch_single("ザボディショップ ボディスクラブ シア")
if res4:
    print("Found res4:", res4["official_item_name"][:30], res4["price"])
    data["winter_body_scrub"]["items"][8]["official_item_name"] = res4["official_item_name"]
    data["winter_body_scrub"]["items"][8]["price"] = res4["price"]
    data["winter_body_scrub"]["items"][8]["image_url"] = res4["image_url"]
    data["winter_body_scrub"]["items"][8]["affiliate_url"] = res4["affiliate_url"]
    data["winter_body_scrub"]["items"][8]["shop_name"] = res4["shop_name"]
    data["winter_body_scrub"]["items"][8]["review_count"] = res4["review_count"]
    data["winter_body_scrub"]["items"][8]["review_average"] = res4["review_average"]

with open("rakuten_hair_cushion_scrub_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated rakuten_hair_cushion_scrub_data.json successfully!")
