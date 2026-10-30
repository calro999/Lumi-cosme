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

with open("rakuten_3latest_articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

targets = [
    {
        "cat": "winter_cleansing_balm",
        "rank": 3,
        "query": "クレンジングバーム ルルルン",
        "brand": "LuLuLun (ルルルン)",
        "name": "クレンジングバーム リッチモイスト (植物由来エモリエントオイル高配合・冬の乾燥肌をうるおいで包み込む濃密バーム)"
    },
    {
        "cat": "winter_cica_cream",
        "rank": 8,
        "query": "ネイチャーリパブリック シカクリーム",
        "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "name": "グリーンダーマ CICA デイリークリーム (プロポリスエキス×センテラ成分・冬の肌のカサつきと肌荒れを同時にうるおす大容量)"
    },
    {
        "cat": "winter_cica_cream",
        "rank": 10,
        "query": "Dr.G レッドブレミッシュ クリアスージングクリーム",
        "brand": "Dr.G (ドクタージー)",
        "name": "レッドブレミッシュ クリアスージングクリーム (韓国オリーブヤング1位・10-CICAコンプレックスが冬のゆらぎ赤みをみずみずしく鎮静)"
    }
]

for t in targets:
    cat = t["cat"]
    rank = t["rank"]
    q = t["query"]
    print(f"Testing {q}...")
    time.sleep(2.0)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        print(f"  Found {len(items)} items")
        if items:
            chosen = None
            for it in items:
                item_obj = it["Item"]
                if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                    chosen = item_obj
                    break
            if not chosen:
                chosen = items[0]["Item"]
            
            raw_img = chosen["mediumImageUrls"][0]["imageUrl"]
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in raw_img:
                high_res_img = raw_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in raw_img:
                high_res_img = raw_img.split("?_ex=")[0] + "?_ex=600x600"
            else:
                high_res_img = raw_img
            
            price = chosen.get("itemPrice", 0)
            aff_url = chosen.get("affiliateUrl", "") or chosen.get("itemUrl", "")
            item_name = chosen.get("itemName", "")
            
            for idx, existing in enumerate(data[cat]["items"]):
                if existing["rank"] == rank:
                    data[cat]["items"][idx] = {
                        "rank": rank,
                        "brand": t["brand"],
                        "name": t["name"],
                        "itemName": item_name,
                        "price": price,
                        "img": high_res_img,
                        "url": aff_url
                    }
                    print(f"  ✓ Updated Rank {rank}: {t['brand']} - ¥{price:,} - {high_res_img}")
                    break

with open("rakuten_3latest_articles_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All done!")
