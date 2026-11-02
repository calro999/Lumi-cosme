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

def fetch_single(q):
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
        data = json.loads(res.read().decode('utf-8'))
        items = data.get("Items", [])
        if not items:
            return None
        chosen = None
        for it in items:
            item_obj = it["Item"]
            if item_obj.get("itemPrice", 0) > 0 and (item_obj.get("mediumImageUrls") or item_obj.get("smallImageUrls")):
                chosen = item_obj
                break
        if not chosen:
            chosen = items[0]["Item"]
            
        img_url = ""
        if chosen.get("mediumImageUrls"):
            img_url = chosen["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
        elif chosen.get("smallImageUrls"):
            img_url = chosen["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
        
        return {
            "rakuten_name": chosen.get("itemName", ""),
            "price": chosen.get("itemPrice", 0),
            "image": img_url,
            "affiliateUrl": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
            "reviewCount": chosen.get("reviewCount", 0),
            "reviewAverage": chosen.get("reviewAverage", "0.0")
        }

# Load current json
with open("fetched_3new_nov_dec_shea_jojoba_urea_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix Shea Butter Rank 9
print("Fixing Shea Rank 9...")
shea_9_data = fetch_single("ロクシタン シア ハンドクリーム 30ml")
shea_9_item = {
    "rank": 9,
    "brand": "L'OCCITANE (ロクシタン)",
    "name": "シア ハンドクリーム 30ml (高濃度シアバター20%配合)",
    "query": "ロクシタン シア ハンドクリーム 30ml",
    **shea_9_data
}
# insert at rank 9 (index 8)
shea_items = data["winter_shea_butter"]["items"]
shea_items.insert(8, shea_9_item)
# Ensure rank 10 is rank 10
for idx, it in enumerate(shea_items):
    it["rank"] = idx + 1

time.sleep(2)

# Fix Urea Cream Rank 2
print("Fixing Urea Rank 2...")
urea_2_data = fetch_single("フェルゼア クリーム")
urea_2_item = {
    "rank": 2,
    "brand": "ライオン フェルゼア",
    "name": "フェルゼア クリーム 80g (指定医薬部外品 / 尿素10%・角質柔軟配合)",
    "query": "フェルゼア クリーム",
    **urea_2_data
}
urea_items = data["winter_urea_cream"]["items"]
urea_items.insert(1, urea_2_item)
for idx, it in enumerate(urea_items):
    it["rank"] = idx + 1

with open("fetched_3new_nov_dec_shea_jojoba_urea_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nVerification of all 3 categories:")
for cat_k, cat_v in data.items():
    print(f"\nCategory: {cat_k} - {len(cat_v['items'])} items")
    for it in cat_v["items"]:
        print(f"  Rank {it['rank']}: {it['name'][:35]} | ¥{it['price']} | Img: {it['image'][:35]}... | Aff: {it['affiliateUrl'][:30]}...")
