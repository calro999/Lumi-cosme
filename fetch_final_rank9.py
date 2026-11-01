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

with open("rakuten_scalp_bath_wipe_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

t = {
    "rank": 9,
    "query": "ミルボン プラーミア クリアスパフォーム 170g",
    "brand": "MILBON (ミルボン プラーミア)",
    "name": "プラーミア クリアスパフォーム 170g (高濃度炭酸マイクロ泡×カキタンニン配合・冬の凝り固まった頭皮の毛穴皮脂・ニオイをスッキリ落とし血行促進)"
}

query = t["query"]
for attempt in range(5):
    try:
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            items = res_data.get("Items", [])
            if items:
                chosen = None
                for it in items:
                    item_obj = it["Item"]
                    if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls") and "ふるさと納税" not in item_obj.get("itemName", ""):
                        chosen = item_obj
                        break
                if not chosen:
                    chosen = items[0]["Item"]

                raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "") if chosen.get("mediumImageUrls") else ""
                high_res_img = raw_img
                if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                    high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                elif "?_ex=" in high_res_img:
                    high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"

                aff_url = chosen.get("affiliateUrl", "")
                if not aff_url:
                    raw_item_url = chosen.get("itemUrl", "")
                    aff_url = f"https://hb.afl.rakuten.co.jp/hgc/{AFF_ID}/?pc={urllib.parse.quote(raw_item_url)}"

                price = chosen.get("itemPrice", 0)
                print(f"  [SUCCESS] rank 9 | {t['brand']} | ¥{price:,} | {chosen.get('itemName', '')[:40]}")
                item_dict = {
                    "rank": t["rank"],
                    "brand": t["brand"],
                    "name": t["name"],
                    "raw_item_name": chosen.get("itemName", ""),
                    "price": price,
                    "image_url": high_res_img,
                    "affiliate_url": aff_url
                }
                
                existing_items = data["winter_scalp_scrub"]["items"]
                found_idx = -1
                for i, it in enumerate(existing_items):
                    if it["rank"] == 9:
                        found_idx = i
                        break
                if found_idx >= 0:
                    existing_items[found_idx] = item_dict
                else:
                    existing_items.append(item_dict)
                break
    except Exception as e:
        print(f"Attempt {attempt+1} failed: {e}")
        time.sleep(3)

data["winter_scalp_scrub"]["items"] = sorted(data["winter_scalp_scrub"]["items"], key=lambda x: x["rank"])
print(f"winter_scalp_scrub total items: {len(data['winter_scalp_scrub']['items'])}/10")

with open("rakuten_scalp_bath_wipe_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved perfectly!")
