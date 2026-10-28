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

def fetch_single(query):
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    raw_item = items[0]["Item"]
                    raw_img = ""
                    if raw_item.get("mediumImageUrls"):
                        raw_img = raw_item["mediumImageUrls"][0].get("imageUrl", "")
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    return {
                        "item_name": raw_item.get("itemName", ""),
                        "price": raw_item.get("itemPrice", 0),
                        "affiliate_url": raw_item.get("affiliateUrl", ""),
                        "image_url": high_res_img,
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", 0),
                        "shop_name": raw_item.get("shopName", "")
                    }
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2)
        time.sleep(1.5)
    return None

with open("rakuten_emulsion_oil_balm_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. ミノン乳液（単品）修正
print("Fixing Minon Milk...")
res_minon = fetch_single("ミノン モイストチャージ ミルク 100g")
if res_minon:
    data["winter_emulsion"]["items"][2]["item_name"] = res_minon["item_name"]
    data["winter_emulsion"]["items"][2]["price"] = res_minon["price"]
    data["winter_emulsion"]["items"][2]["affiliate_url"] = res_minon["affiliate_url"]
    data["winter_emulsion"]["items"][2]["image_url"] = res_minon["image_url"]
    data["winter_emulsion"]["items"][2]["review_count"] = res_minon["review_count"]
    print("Fixed Minon:", res_minon["price"])
time.sleep(1.5)

# 2. エリクシール乳液（単品）修正
print("Fixing Elixir Milk...")
res_elixir = fetch_single("資生堂 エリクシール リフトモイスト エマルジョン SP")
if res_elixir:
    data["winter_emulsion"]["items"][4]["item_name"] = res_elixir["item_name"]
    data["winter_emulsion"]["items"][4]["price"] = res_elixir["price"]
    data["winter_emulsion"]["items"][4]["affiliate_url"] = res_elixir["affiliate_url"]
    data["winter_emulsion"]["items"][4]["image_url"] = res_elixir["image_url"]
    data["winter_emulsion"]["items"][4]["review_count"] = res_elixir["review_count"]
    print("Fixed Elixir:", res_elixir["price"])
time.sleep(1.5)

# 3. リペアバーム Rank 5 キュレル モイスチャーバーム追加
print("Adding Curel Balm for Rank 5...")
res_curel = fetch_single("キュレル モイスチャーバーム 70g")
if res_curel:
    item_curel = {
        "rank": 5,
        "brand": "Curel (キュレル)",
        "display_name": "モイスチャーバーム 【医薬部外品】 (濃密セラミドバリア処方・顔からだ用)",
        "item_name": res_curel["item_name"],
        "price": res_curel["price"],
        "affiliate_url": res_curel["affiliate_url"],
        "image_url": res_curel["image_url"],
        "review_count": res_curel["review_count"],
        "review_average": res_curel["review_average"],
        "shop_name": res_curel["shop_name"]
    }
    # Rank 5に挿入（インデックス4の位置）
    balm_items = data["winter_repair_balm"]["items"]
    # 既存のアイテムのランク順序を整理
    # 現在balm_itemsには9件入っているので、rank5を挿入
    new_balm_items = []
    for it in balm_items:
        if it["rank"] < 5:
            new_balm_items.append(it)
    new_balm_items.append(item_curel)
    for it in balm_items:
        if it["rank"] >= 5:
            new_balm_items.append(it)
    
    # rank番号を1-10に再付与
    for i, it in enumerate(new_balm_items):
        it["rank"] = i + 1
    
    data["winter_repair_balm"]["items"] = new_balm_items
    print(f"Curel Balm inserted, total balm items: {len(new_balm_items)}")

with open("rakuten_emulsion_oil_balm_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All updates saved successfully!")
