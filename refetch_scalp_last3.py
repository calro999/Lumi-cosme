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

targets = [
    {
        "rank": 2,
        "query": "ロクシタン ピュアフレッシュネス",
        "brand": "L'OCCITANE (ロクシタン)",
        "name": "ファイブハーブス ピュアフレッシュネス スカルプエッセンス 75ml (5つのハーブエッセンシャルオイル配合・冬の頭皮のベタつきやニオイを抑え根元から健やかな髪を育む)"
    },
    {
        "rank": 8,
        "query": "モロッカンオイル スカルプ トリートメント",
        "brand": "MOROCCANOIL (モロッカンオイル)",
        "name": "ドライ スカルプ トリートメント 45ml (アルガンオイル×ラベンダー・ゼラニウム精油配合・冬の乾燥した頭皮を濃厚に潤してかゆみやフケを予防)"
    },
    {
        "rank": 9,
        "query": "キールズ スカルプ トリートメント",
        "brand": "KIEHL'S (キールズ)",
        "name": "スカルプ マジック トリートメント 100ml (サリチル酸×植物オイル配合・冬のこわばった頭皮の角質を穏やかに整えてうるおいを満たす)"
    }
]

def fetch_item(t):
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
                    print(f"  [SUCCESS] rank {t['rank']} | {t['brand']} | ¥{price:,} | {chosen.get('itemName', '')[:40]}")
                    return {
                        "rank": t["rank"],
                        "brand": t["brand"],
                        "name": t["name"],
                        "raw_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url
                    }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 4.0 * (attempt + 1)
                print(f"  [429 Rate limited] waiting {wait_time}s on '{query}'...")
                time.sleep(wait_time)
            else:
                print(f"  [HTTPError {e.code}] on '{query}'")
                time.sleep(2)
        except Exception as e:
            print(f"  [ERROR] {e} on '{query}'")
            time.sleep(2)
    return None

for t in targets:
    print(f"\nFetching rank {t['rank']} ({t['query']})...")
    res = fetch_item(t)
    if res:
        # 既存リスト内を探すか、追加するか
        existing_items = data["winter_scalp_scrub"]["items"]
        found_idx = -1
        for i, it in enumerate(existing_items):
            if it["rank"] == t["rank"]:
                found_idx = i
                break
        if found_idx >= 0:
            existing_items[found_idx] = res
        else:
            existing_items.append(res)
    time.sleep(3.0)

data["winter_scalp_scrub"]["items"] = sorted(data["winter_scalp_scrub"]["items"], key=lambda x: x["rank"])
print(f"\nwinter_scalp_scrub total items: {len(data['winter_scalp_scrub']['items'])}/10")

with open("rakuten_scalp_bath_wipe_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved!")
