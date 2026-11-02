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

with open("fetched_3new_nov_dec_rice_camellia_amino_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 欠損している椿油のアイテムを補完
missing_items = [
    {
        "rank": 3,
        "brand": "かづら清老舗 (京都祇園)",
        "name": "特製つばき油 100ml (長崎五島列島産手摘みヤブツバキ100%・最高級純椿油)",
        "queries": ["かづら清 つばき油", "かづら清老舗 椿油", "五島 椿油 100ml"]
    },
    {
        "rank": 4,
        "brand": "五島特産 (長崎五島)",
        "name": "純椿油 100ml (長崎五島列島産・一番搾り無添加コールドプレス)",
        "queries": ["五島 椿油 100ml", "五島列島 椿油", "純椿油 五島"]
    },
    {
        "rank": 6,
        "brand": "よーじや (京都)",
        "name": "うるおい椿オイル 30ml (高純度精製カメリアオイル・ベタつかない美肌処方)",
        "queries": ["よーじや 椿油", "よーじや オイル", "うるおい 椿油"]
    },
    {
        "rank": 7,
        "brand": "リバティライフ",
        "name": "国産 椿油 100ml (天然無添加ピュアカメリアオイル・全身マルチケア)",
        "queries": ["椿油 100ml 国産", "カメリアオイル 100ml", "天然 椿油 100ml"]
    },
    {
        "rank": 9,
        "brand": "自然化粧品研究所",
        "name": "国産 椿油 100ml (未精製ゴールドタイプ・オレイン酸リッチ保湿)",
        "queries": ["自然化粧品研究所 椿油", "ツバキ油 自然化粧品研究所", "国産 椿油 未精製"]
    }
]

def fetch_item(item_spec):
    for q in item_spec["queries"]:
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        for attempt in range(3):
            try:
                print(f"Fetching '{q}' (attempt {attempt+1})...")
                time.sleep(1.5)  # レート制限防止ウェイト
                with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                    res_data = json.loads(res.read().decode('utf-8'))
                    items = res_data.get("Items", [])
                    if not items:
                        break
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
                    
                    if chosen.get("itemPrice", 0) > 0 and img_url:
                        return {
                            "rank": item_spec["rank"],
                            "brand": item_spec["brand"],
                            "name": item_spec["name"],
                            "query": q,
                            "rakuten_name": chosen.get("itemName", ""),
                            "price": chosen.get("itemPrice", 0),
                            "rakuten_url": chosen.get("itemUrl", ""),
                            "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                            "img_url": img_url
                        }
            except urllib.error.HTTPError as e:
                print(f"  HTTP Error {e.code}: {e.reason}")
                if e.code == 429:
                    time.sleep(3.0)
            except Exception as e:
                print(f"  Error: {e}")
                time.sleep(2.0)
    return None

# 既存の椿油アイテム
existing_camellia = {it["rank"]: it for it in data["winter_camellia_oil"]["items"]}

for missing in missing_items:
    r = missing["rank"]
    if r not in existing_camellia:
        print(f"\nTargeting Rank #{r}: {missing['name'][:30]}")
        fetched = fetch_item(missing)
        if fetched:
            print(f"  -> SUCCESS! Price=¥{fetched['price']:,}, Img={fetched['img_url'][:40]}...")
            existing_camellia[r] = fetched
        else:
            print(f"  -> FAILED to fetch rank {r}")

# ランク順にソートして再格納
sorted_items = [existing_camellia[r] for r in sorted(existing_camellia.keys())]
data["winter_camellia_oil"]["items"] = sorted_items

with open("fetched_3new_nov_dec_rice_camellia_amino_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nFinal camellia oil item count: {len(sorted_items)}/10")
