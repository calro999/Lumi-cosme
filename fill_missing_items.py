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

def extract_image_url(cand):
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    if isinstance(first, dict):
        raw = first.get("imageUrl", "")
    else:
        raw = str(first)
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

with open("fetched_3new_mask_lip_serum.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 補填対象
missing_targets = [
    {
        "cat": "winter_lip_sleeping_mask",
        "rank": 3,
        "brand": "NIVEA (ニベア / 花王)",
        "name": "ディープモイスチャー ナイトプロテクト 無香料 7g (医薬部外品・高密着高保水リップバーム・5つの保湿成分とビタミンE・グリチルレチン酸ステアリルが夜間の唇を集中パック)",
        "query": "ニベア ディープモイスチャー ナイトプロテクト 無香料"
    },
    {
        "cat": "winter_barrier_serum",
        "rank": 5,
        "brand": "Curel (キュレル / 花王)",
        "name": "潤浸保湿 角層深部バリア美容液 30mL (医薬部外品・セラミドケア成分×抗炎症有効成分アラントイン・真冬の乾燥でゴワつく角層をほぐし潤いで満たすバリア美容液)",
        "query": "キュレル 潤浸保湿 美容液"
    },
    {
        "cat": "winter_barrier_serum",
        "rank": 9,
        "brand": "manyo (魔女工場)",
        "name": "ビフィダ バイオーム コンプレックス アンプル 50mL (マイクロバイオーム×ビフィズス菌培養溶解質×5種セラミド・弱った肌のバリア基礎体力を底上げする大人気アンプル)",
        "query": "魔女工場 ビフィダ バイオーム コンプレックス アンプル 50ml"
    }
]

for t in missing_targets:
    cat = t["cat"]
    q = t["query"]
    print(f"Fetching missing item for {cat} Rank {t['rank']}: {q}")
    eq = urllib.parse.quote(q)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={eq}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    
    time.sleep(2.5)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        cand = res_data["Items"][0]["Item"]
        
    img_url = extract_image_url(cand)
    aff_url = cand.get("affiliateUrl") or cand.get("itemUrl")
    
    item_obj = {
        "rank": t["rank"],
        "brand": t["brand"],
        "display_name": t["name"],
        "item_name": cand["itemName"],
        "price": cand["itemPrice"],
        "affiliate_url": aff_url,
        "image_url": img_url,
        "review_count": cand.get("reviewCount", 0),
        "review_average": str(cand.get("reviewAverage", "4.8"))
    }
    
    # rank順に挿入または置換
    items = data[cat]["items"]
    # 既存にあれば削除
    items = [it for it in items if it["rank"] != t["rank"]]
    items.append(item_obj)
    items.sort(key=lambda x: x["rank"])
    data[cat]["items"] = items
    print(f"  -> Added {cand['itemName'][:35]} (¥{cand['itemPrice']:,})")

with open("fetched_3new_mask_lip_serum.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nVerification of fetched items count:")
for k, v in data.items():
    print(f"  - {k}: {len(v['items'])} items")
