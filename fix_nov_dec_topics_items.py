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

with open("rakuten_3winter_nov_dec_topics_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

targets = [
    {
        "cat": "winter_hand_cream",
        "rank": 10,
        "query": "オサジ ハンドクリーム",
        "brand": "OSAJI (オサジ)",
        "name": "リペア ハンドクリーム 50g (皮膚科学に基づく敏感肌設計・高純度セラミド形成を促しベタつかずスマホ操作も快適な国産名品)"
    },
    {
        "cat": "winter_ceramide_serum",
        "rank": 5,
        "query": "トゥヴェール ナノエマルジョン 60mL",
        "brand": "TOUT VERT (トゥヴェール)",
        "name": "ナノエマルジョン 60ml (インナードライ対策特化・高濃度浸透湿潤セラミド10%配合の超微細ナノ美容液)"
    },
    {
        "cat": "winter_ceramide_serum",
        "rank": 7,
        "query": "アンプルショット セラミド 美容液",
        "brand": "AMPLE SHOT (アンプルショット)",
        "name": "アクティベイティング モイスチャーセラム 48ml (高濃度セラミド原液カプセル×アミノ酸配合・冬の砂漠乾燥を集中レスキューする高浸透アンプル)"
    }
]

def fetch_single(target):
    q = target["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=3&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        if items:
            chosen = items[0]["Item"]
            raw_img = chosen["mediumImageUrls"][0]["imageUrl"]
            high_res_img = raw_img
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in high_res_img:
                high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
            
            price = chosen.get("itemPrice", 0)
            aff_url = chosen.get("affiliateUrl", "") or chosen.get("itemUrl", "")
            item_name = chosen.get("itemName", "")
            return {
                "rank": target["rank"],
                "brand": target["brand"],
                "name": target["name"],
                "itemName": item_name,
                "price": price,
                "img": high_res_img,
                "url": aff_url
            }
    return None

for t in targets:
    time.sleep(1.2)
    updated = fetch_single(t)
    if updated:
        cat_items = data[t["cat"]]["items"]
        for idx, it in enumerate(cat_items):
            if it["rank"] == t["rank"]:
                data[t["cat"]]["items"][idx] = updated
                print(f"Updated {t['cat']} Rank {t['rank']}: {updated['brand']} - ¥{updated['price']} - {updated['img'][:50]}")

with open("rakuten_3winter_nov_dec_topics_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Replacement complete!")
