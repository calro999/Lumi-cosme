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

def fetch_single(query):
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

# Rank 5: FEMMUE
res5 = fetch_single("ファミュ オイル")
if res5:
    for idx, it in enumerate(data["winter_booster_oil"]["items"]):
        if it["rank"] == 5:
            data["winter_booster_oil"]["items"][idx]["rakuten_item_name"] = res5["rakuten_item_name"]
            data["winter_booster_oil"]["items"][idx]["price"] = res5["price"]
            data["winter_booster_oil"]["items"][idx]["image_url"] = res5["image_url"]
            data["winter_booster_oil"]["items"][idx]["affiliate_url"] = res5["affiliate_url"]
            data["winter_booster_oil"]["items"][idx]["shop_name"] = res5["shop_name"]
            print(f"Updated FEMMUE: {res5['rakuten_item_name'][:30]}")
time.sleep(1.0)

# Rank 8: KANEBO ドロッピング オイル
res8 = fetch_single("KANEBO オイル")
if res8:
    for idx, it in enumerate(data["winter_booster_oil"]["items"]):
        if it["rank"] == 8:
            data["winter_booster_oil"]["items"][idx]["rakuten_item_name"] = res8["rakuten_item_name"]
            data["winter_booster_oil"]["items"][idx]["name"] = "ドロッピング オイル 40ml (みずみずしい光沢感を仕込みメイク前の土台を完璧に整える名作)"
            data["winter_booster_oil"]["items"][idx]["price"] = res8["price"]
            data["winter_booster_oil"]["items"][idx]["image_url"] = res8["image_url"]
            data["winter_booster_oil"]["items"][idx]["affiliate_url"] = res8["affiliate_url"]
            data["winter_booster_oil"]["items"][idx]["shop_name"] = res8["shop_name"]
            print(f"Updated KANEBO: {res8['rakuten_item_name'][:30]}")
time.sleep(1.0)

# Rank 9: ロクシタン イモーテル ディヴァイン オイル
res9 = fetch_single("ロクシタン イモーテル ディヴァイン オイル")
if res9:
    for idx, it in enumerate(data["winter_booster_oil"]["items"]):
        if it["rank"] == 9:
            data["winter_booster_oil"]["items"][idx]["brand"] = "L'OCCITANE (ロクシタン)"
            data["winter_booster_oil"]["items"][idx]["name"] = "イモーテル ディヴァインインテンシヴオイル 30ml (洗顔後すぐの肌に奇跡の一滴・肌密度を高め内側から跳ね返すようなハリと輝きを与える先行型プレオイル)"
            data["winter_booster_oil"]["items"][idx]["rakuten_item_name"] = res9["rakuten_item_name"]
            data["winter_booster_oil"]["items"][idx]["price"] = res9["price"]
            data["winter_booster_oil"]["items"][idx]["image_url"] = res9["image_url"]
            data["winter_booster_oil"]["items"][idx]["affiliate_url"] = res9["affiliate_url"]
            data["winter_booster_oil"]["items"][idx]["shop_name"] = res9["shop_name"]
            print(f"Updated LOccitane: {res9['rakuten_item_name'][:30]}")

with open("rakuten_3winter_body_booster_shampoo_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Finished final Rakuten API sync!")
