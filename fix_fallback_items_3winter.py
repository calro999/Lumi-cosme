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

with open("rakuten_3winter_nov_dec_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

targets = [
    # (category, rank, keyword)
    ("winter_body_milk", 1, "ニベア スキンミルク しっとり 200g"),
    ("winter_body_milk", 5, "ローラメルシエ アンバーバニラ ボディ"),
    ("winter_toner_pad", 4, "Abib 復活草 パッド"),
    ("winter_toner_pad", 6, "VT CICA マイルド トナーパッド"),
    ("winter_toner_pad", 8, "スキンフード キャロット パッド")
]

for cat, rank, kw in targets:
    print(f"Fetching for {cat} Rank {rank} with keyword: {kw}")
    time.sleep(2)  # レートリミット回避
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(kw)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            items = res_data.get("Items", [])
            chosen = None
            for it in items:
                io = it["Item"]
                if io.get("itemPrice", 0) > 0 and io.get("mediumImageUrls"):
                    # ニベアの場合は異常に高い価格(2万円等)を避ける
                    if rank == 1 and io.get("itemPrice", 0) > 3000:
                        continue
                    chosen = io
                    break
            if not chosen and items:
                chosen = items[0]["Item"]
            
            if chosen:
                raw_img = chosen["mediumImageUrls"][0]["imageUrl"] if chosen.get("mediumImageUrls") else ""
                high_res_img = raw_img
                if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                    high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                elif "?_ex=" in high_res_img:
                    high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                
                aff_url = chosen.get("affiliateUrl") or chosen.get("itemUrl")
                price = chosen.get("itemPrice", 0)
                item_name = chosen.get("itemName", "")

                for item_dict in data[cat]["items"]:
                    if item_dict["rank"] == rank:
                        item_dict["itemName"] = item_name
                        item_dict["price"] = price
                        item_dict["img"] = high_res_img
                        item_dict["url"] = aff_url
                        print(f"  -> SUCCESS! Price: ¥{price:,}, Img: {high_res_img[:45]}...")
                        break
            else:
                print(f"  -> No items found for {kw}")
    except Exception as e:
        print(f"  -> Error: {e}")

with open("rakuten_3winter_nov_dec_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nUpdated JSON saved.")
