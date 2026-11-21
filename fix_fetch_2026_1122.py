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

def search_rakuten(query):
    encoded_q = urllib.parse.quote(query)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=15&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    time.sleep(1.5)
    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
        return json.loads(res.read().decode('utf-8')).get("Items", [])

def extract_image_url(cand):
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    raw = first.get("imageUrl", "") if isinstance(first, dict) else str(first)
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

with open("fetched_3new_nov_dec_2026_1122.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Candidates to fetch/replace cleanly
targets = [
    # Clay mask rank 5 & 8
    ("winter_clay_mask", 5, "THREE (スリー)", "ピュリファイング クレイマスク 120g",
     ["THREE ピュリファイング クレイマスク", "SABON フェイシャル マッド スクラブ", "CLAYD ワンタイム 30g"],
     ["クレイ"], ["ケース", "サンプル", "パウチ"]),
    ("winter_clay_mask", 8, "CLAYD (クレイド)", "CLAYD ONE TIME (クレイド ワンタイム 30g×7袋 / パック)",
     ["CLAYD クレイド パック", "CLAYD マスク", "毛穴撫子 お米のパック 170g"],
     ["パック"], ["入浴剤のみ"]),
    # Acne moisture rank 8 & 10
    ("winter_acne_moisture", 8, "Carte HD (コーセー カルテHD)", "バランスケア エマルジョン 120mL (医薬部外品)",
     ["カルテHD バランスケア エマルジョン 120ml", "カルテHD バランスケア ゲル 100g 単品"],
     ["バランスケア"], ["セット", "2個", "詰替"]),
    ("winter_acne_moisture", 10, "肌美精 (クラシエ)", "大人のニキビ対策 薬用美白保湿クリーム 50g (医薬部外品)",
     ["肌美精 大人のニキビ対策 薬用美白保湿クリーム", "肌ラボ 極潤 スキンコンディショナー", "ペアアクネ クリーンローション"],
     ["ニキビ"], ["セット"]),
    # Powder foundation rank 2, 5, 8
    ("winter_powder_foundation", 2, "ALBION (アルビオン)", "プリンプ パウダレスト (レフィル)",
     ["アルビオン プリンプ パウダレスト レフィル", "アルビオン パウダレスト 040", "コスメデコルテ ゼン ウェア パウダーファンデーション"],
     ["パウダ"], ["ケース", "マット", "スポンジ", "パフ"]),
    ("winter_powder_foundation", 5, "ESPRIQUE (コーセー エスプリーク)", "シンクロフィット パクト EX (レフィル)",
     ["エスプリーク シンクロフィット パクト EX OC", "エスプリーク シンクロフィット パクト EX レフィル"],
     ["シンクロフィット"], ["限定", "キット", "ケース"]),
    ("winter_powder_foundation", 8, "VINTORTE (ヴァントルテ)", "ミネラルシルクファンデーション (パフ付)",
     ["ヴァントルテ ミネラルシルクファンデーション", "オンリーミネラル 薬用ホワイトニングファンデーション"],
     ["ミネラル"], ["訳あり", "サンプル", "パフのみ", "ケースのみ"])
]

for cat_key, rank, brand, disp_name, queries, must_inc, exclude_words in targets:
    chosen = None
    for q in queries:
        print(f"Searching {cat_key} Rank {rank}: {q}")
        try:
            items = search_rakuten(q)
            for it in items:
                cand = it["Item"]
                iname = cand.get("itemName", "")
                price = cand.get("itemPrice", 0)
                if price < 600 or not (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                    continue
                if any(ex in iname for ex in exclude_words):
                    continue
                if all(k.lower() in iname.lower() for k in must_inc):
                    chosen = cand
                    break
            if not chosen:
                for it in items:
                    cand = it["Item"]
                    iname = cand.get("itemName", "")
                    price = cand.get("itemPrice", 0)
                    if price >= 600 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and not any(ex in iname for ex in exclude_words):
                        chosen = cand
                        break
            if chosen:
                break
        except Exception as e:
            print("  err:", e)
    if chosen:
        entry = {
            "rank": rank,
            "brand": brand,
            "display_name": disp_name,
            "item_name": chosen["itemName"],
            "price": chosen["itemPrice"],
            "affiliate_url": chosen.get("affiliateUrl") or chosen.get("itemUrl"),
            "image_url": extract_image_url(chosen),
            "review_count": chosen.get("reviewCount", 0),
            "review_average": str(chosen.get("reviewAverage", "4.5"))
        }
        print(f"  -> MATCH: {entry['item_name'][:60]} (¥{entry['price']:,})")
        # replace or insert
        arr = data[cat_key]["items"]
        arr = [x for x in arr if x["rank"] != rank]
        arr.append(entry)
        arr.sort(key=lambda x: x["rank"])
        data[cat_key]["items"] = arr
    else:
        print(f"  ❌ STILL FAILED for {cat_key} Rank {rank}")

with open("fetched_3new_nov_dec_2026_1122.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for k in data:
    print(k, "count:", len(data[k]["items"]))
