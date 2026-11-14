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

def fetch_item(queries, rank, brand, name):
    chosen = None
    for q in queries:
        print(f"Trying query '{q}' ...")
        encoded_q = urllib.parse.quote(q)
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        try:
            time.sleep(2.0)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                for it in items:
                    cand = it["Item"]
                    price = cand.get("itemPrice", 0)
                    if price >= 300 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                        chosen = cand
                        break
            if chosen:
                break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(2.0)
    
    if chosen:
        img = extract_image_url(chosen)
        aff = chosen.get("affiliateUrl") or chosen.get("itemUrl")
        print(f"  -> Found: {chosen['itemName'][:40]} (¥{chosen['itemPrice']:,})")
        return {
            "rank": rank,
            "brand": brand,
            "display_name": name,
            "item_name": chosen["itemName"],
            "price": chosen["itemPrice"],
            "affiliate_url": aff,
            "image_url": img,
            "review_count": chosen.get("reviewCount", 0),
            "review_average": str(chosen.get("reviewAverage", "4.8"))
        }
    return None

with open("fetched_3new_cica_glutathione_hyaluronic.json", "r", encoding="utf-8") as f:
    full_data = json.load(f)

# 1. winter_cica_mask Rank 10
print("\n--- Fixing winter_cica_mask Rank 10 ---")
cica_10 = fetch_item(
    ["COSRX シートマスク", "コスアールエックス CICA パック", "シカ シートマスク 10枚"],
    10,
    "COSRX (コスアールエックス)",
    "ピュアフィット CICA カーム トゥルー シートマスク 10枚入 (独自CICA-7コンプレックス81%配合×極薄ヴィーガンシート・冬の乾燥性敏感肌を包み込み深いリラックスとうるおいを与える)"
)
if cica_10:
    # replace rank 10
    items = [it for it in full_data["winter_cica_mask"]["items"] if it["rank"] != 10]
    items.append(cica_10)
    items.sort(key=lambda x: x["rank"])
    full_data["winter_cica_mask"]["items"] = items

# 2. winter_glutathione_mask Rank 2
print("\n--- Fetching winter_glutathione_mask Rank 2 ---")
gluta_2 = fetch_item(
    ["ルルルン ハイドラ EX マスク 28枚", "ルルルン ハイドラ EX マスク", "ルルルン ハイドラ EX 7枚"],
    2,
    "LuLuLun (ルルルン)",
    "ルルルン ハイドラ EX マスク 28枚入 (白玉グルタチオン×浸透型ビタミンC×ヒト型セラミド・とろけるメルティシートが真冬のどんよりくすみと乾燥を同時に晴らす最新デイリー白玉マスク)"
)
if gluta_2:
    items = [it for it in full_data["winter_glutathione_mask"]["items"] if it["rank"] != 2]
    items.append(gluta_2)
    items.sort(key=lambda x: x["rank"])
    full_data["winter_glutathione_mask"]["items"] = items

# 3. winter_glutathione_mask Rank 5
print("\n--- Fetching winter_glutathione_mask Rank 5 ---")
gluta_5 = fetch_item(
    ["魔女工場 ガラク エッセンス マスク", "Manyo ガラク マスク 10枚", "魔女工場 シートマスク 10枚"],
    5,
    "魔女工場 (Manyo Factory)",
    "ガラク エッセンス マスク 10枚入 (高純度ガラクトミセス培養液×高濃度グルタチオン配合・真冬の冷風でくすんだキメを滑らかに整え透き通るような白玉ガラス肌へ導くベストセラー)"
)
if gluta_5:
    items = [it for it in full_data["winter_glutathione_mask"]["items"] if it["rank"] != 5]
    items.append(gluta_5)
    items.sort(key=lambda x: x["rank"])
    full_data["winter_glutathione_mask"]["items"] = items

# 4. winter_hyaluronic_lotion Rank 5
print("\n--- Fetching winter_hyaluronic_lotion Rank 5 ---")
hyal_5 = fetch_item(
    ["カルテHD 高保湿化粧水 150ml", "カルテHD モイスチュア ローション 150ml", "カルテHD 化粧水"],
    5,
    "Carte (カルテHD / コーセー マルホ)",
    "モイスチュア ローション 150mL (医薬部外品・保水有効成分ヘパリン類似物質HD×ヒアルロン酸・セラミド・まろやかな高保湿エマルジョンが真冬の深刻なインナードライを根本改善)"
)
if hyal_5:
    items = [it for it in full_data["winter_hyaluronic_lotion"]["items"] if it["rank"] != 5]
    items.append(hyal_5)
    items.sort(key=lambda x: x["rank"])
    full_data["winter_hyaluronic_lotion"]["items"] = items

with open("fetched_3new_cica_glutathione_hyaluronic.json", "w", encoding="utf-8") as f:
    json.dump(full_data, f, ensure_ascii=False, indent=2)

print("\nFinal check of ranks:")
for k, v in full_data.items():
    ranks = [it["rank"] for it in v["items"]]
    print(f"{k}: count={len(v['items'])}, ranks={ranks}")
