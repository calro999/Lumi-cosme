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

time.sleep(2)
kw = "ネイチャーリパブリック シカ"
url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(kw)}&hits=5&format=json"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, context=ctx) as res:
    data = json.loads(res.read().decode("utf-8"))
    items = data.get("Items", [])
    for it in items:
        item = it["Item"]
        if item.get("itemPrice", 0) > 0 and item.get("mediumImageUrls"):
            price = item["itemPrice"]
            aff_url = item.get("affiliateUrl", "") or item.get("itemUrl", "")
            img = item["mediumImageUrls"][0]["imageUrl"]
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in img:
                img = img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in img:
                img = img.split("?_ex=")[0] + "?_ex=600x600"
            
            with open("rakuten_3latest_articles_data.json", "r", encoding="utf-8") as f:
                db = json.load(f)
            
            for idx, existing in enumerate(db["winter_cica_cream"]["items"]):
                if existing["rank"] == 8:
                    db["winter_cica_cream"]["items"][idx] = {
                        "rank": 8,
                        "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                        "name": "グリーンダーマ CICA デイリークリーム (プロポリスエキス×センテラ成分・冬の肌のカサつきと肌荒れを同時にうるおす大容量)",
                        "itemName": item.get("itemName", ""),
                        "price": price,
                        "img": img,
                        "url": aff_url
                    }
                    print("Successfully updated Rank 8:", price, img)
                    break
            with open("rakuten_3latest_articles_data.json", "w", encoding="utf-8") as f:
                json.dump(db, f, ensure_ascii=False, indent=2)
            break
