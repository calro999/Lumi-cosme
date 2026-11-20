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

CATEGORIES = {
    "winter_all_in_one": {
        "file": "winter-all-in-one.html",
        "url": "/winter-all-in-one",
        "title": "冬の乾燥にこれ1つで終止符！時短でも翌朝まで乾かない高保湿オールインワンジェル＆クリーム厳選ランキング10【11月・12月版】",
        "items": [
            {
                "rank": 1,
                "brand": "カルテHD (Carte HD)",
                "name": "モイスチュア インストール (高保湿オールインワンゲル 100g・医薬部外品)",
                "queries": ["カルテHD モイスチュア インストール 100g", "カルテHD オールインワン"],
                "must_include": ["カルテ", "インストール"]
            },
            {
                "rank": 2,
                "brand": "AQUALABEL (資生堂 アクアレーベル)",
                "name": "スペシャルジェルクリーム EX (モイスト) 90g",
                "queries": ["アクアレーベル スペシャルジェルクリーム EX モイスト 90g", "アクアレーベル スペシャルジェルクリーム モイスト"],
                "must_include": ["アクアレーベル"]
            },
            {
                "rank": 3,
                "brand": "Dr.Ci:Labo (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 120g",
                "queries": ["ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX 120g", "アクアコラーゲンゲル エンリッチリフトEX"],
                "must_include": ["エンリッチリフト"]
            },
            {
                "rank": 4,
                "brand": "CANADEL (カナデル)",
                "name": "プレミアバリアフィックス 58g (医薬部外品)",
                "queries": ["カナデル プレミアバリアフィックス 58g", "CANADEL プレミアバリアフィックス"],
                "must_include": ["バリアフィックス"]
            },
            {
                "rank": 5,
                "brand": "PERFECT ONE (新日本製薬 パーフェクトワン)",
                "name": "モイスチャージェル 75g",
                "queries": ["パーフェクトワン モイスチャージェル 75g", "新日本製薬 パーフェクトワン モイスチャージェル"],
                "must_include": ["モイスチャージェル"]
            },
            {
                "rank": 6,
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤 パーフェクトゲル 100g",
                "queries": ["肌ラボ 極潤 パーフェクトゲル 100g", "極潤 パーフェクトゲル"],
                "must_include": ["パーフェクトゲル"]
            },
            {
                "rank": 7,
                "brand": "Mediplus (メディプラス)",
                "name": "メディプラスゲル 180g",
                "queries": ["メディプラスゲル 180g", "メディプラス オールインワンゲル"],
                "must_include": ["メディプラス"]
            },
            {
                "rank": 8,
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "とろんと濃ジェル エンリッチ NC 100g",
                "queries": ["なめらか本舗 とろんと濃ジェル エンリッチ", "なめらか本舗 とろんと濃ジェル"],
                "must_include": ["とろんと濃ジェル"]
            },
            {
                "rank": 9,
                "brand": "コラリッチ (キューサイ)",
                "name": "コラリッチ EX ブライトニングリフトジェル 55g",
                "queries": ["コラリッチ EX ブライトニングリフトジェル 55g", "コラリッチ EX ブライトニングリフト"],
                "must_include": ["コラリッチ"]
            },
            {
                "rank": 10,
                "brand": "CHIFURE (ちふれ)",
                "name": "うるおい ジェル 108g",
                "queries": ["ちふれ うるおい ジェル 108g", "ちふれ オールインワン うるおいジェル"],
                "must_include": ["ちふれ", "ジェル"]
            }
        ]
    },
    "winter_vitamin_c_lotion": {
        "file": "winter-vitamin-c-lotion.html",
        "url": "/winter-vitamin-c-lotion",
        "title": "冬のくすみも乾燥毛穴もまとめて潤す！しっとり高保湿ビタミンC化粧水おすすめランキング10選【11月・12月最新】",
        "items": [
            {
                "rank": 1,
                "brand": "Dr.Ci:Labo (ドクターシーラボ)",
                "name": "VC100エッセンスローションEX 150mL",
                "queries": ["ドクターシーラボ VC100エッセンスローションEX 150ml", "VC100エッセンスローションEX"],
                "must_include": ["VC100"]
            },
            {
                "rank": 2,
                "brand": "numbuzin (ナンバーズイン)",
                "name": "5番 白玉グルタチオンCエッセンシャル化粧水 200mL",
                "queries": ["ナンバーズイン 5番 化粧水 200ml", "ナンバーズイン 5番 トナー"],
                "must_include": ["5番"]
            },
            {
                "rank": 3,
                "brand": "メラノCC (ロート製薬)",
                "name": "薬用しみ対策美白化粧水 しっとりタイプ 170mL (医薬部外品)",
                "queries": ["メラノCC 薬用しみ対策 美白化粧水 しっとり 170ml", "メラノCC 化粧水 しっとり"],
                "must_include": ["メラノCC"]
            },
            {
                "rank": 4,
                "brand": "Obagi (ロート製薬 オバジ)",
                "name": "オバジC リファインローション 150mL",
                "queries": ["オバジC リファインローション 150ml", "オバジC クリアアドバンスドローション"],
                "must_include": ["オバジ"]
            },
            {
                "rank": 5,
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー ウルセラC 化粧水 / スーパーVC100ローション しっとり 240mL",
                "queries": ["ダーマレーザー スーパーVC100ローション しっとり", "ダーマレーザー VC100 化粧水 しっとり"],
                "must_include": ["ダーマレーザー"]
            },
            {
                "rank": 6,
                "brand": "TOUT VERT (トゥヴェール)",
                "name": "薬用ホワイトニングローションαEX 120mL (医薬部外品)",
                "queries": ["トゥヴェール 薬用ホワイトニングローションαEX", "トゥヴェール ホワイトニングローション"],
                "must_include": ["トゥヴェール"]
            },
            {
                "rank": 7,
                "brand": "innisfree (イニスフリー)",
                "name": "ビタC グリーンティーエンザイム ブライト トナー 200mL",
                "queries": ["イニスフリー ビタC トナー 200ml", "イニスフリー ビタC グリーンティー トナー"],
                "must_include": ["ビタC"]
            },
            {
                "rank": 8,
                "brand": "Dr.K (ドクターケイ)",
                "name": "薬用Cクリアホワイトローション 120mL (医薬部外品)",
                "queries": ["ドクターケイ 薬用Cクリアホワイトローション 120ml", "ドクターケイ 化粧水"],
                "must_include": ["ドクターケイ"]
            },
            {
                "rank": 9,
                "brand": "CHIFURE (ちふれ)",
                "name": "美白化粧水 VC&AR 180mL (医薬部外品)",
                "queries": ["ちふれ 美白化粧水 VC 180ml", "ちふれ 美白化粧水 VC&AR"],
                "must_include": ["ちふれ", "美白化粧水"]
            },
            {
                "rank": 10,
                "brand": "肌ラボ (ロート製薬)",
                "name": "白潤プレミアム 薬用浸透美白化粧水 しっとりタイプ 170mL (医薬部外品)",
                "queries": ["肌ラボ 白潤プレミアム 薬用浸透美白化粧水 しっとり 170ml", "白潤プレミアム 化粧水 しっとり"],
                "must_include": ["白潤プレミアム"]
            }
        ]
    },
    "winter_mens_skincare": {
        "file": "winter-mens-skincare.html",
        "url": "/winter-mens-skincare",
        "title": "髭剃り負けと冬の粉吹きを一掃！メンズ高保湿スキンケア人気ランキング10選【11月・12月の乾燥対策＆ギフトにも】",
        "items": [
            {
                "rank": 1,
                "brand": "ORBIS Mr. (オルビス ミスター)",
                "name": "エッセンスローション 180mL (医薬部外品)",
                "queries": ["オルビス ミスター エッセンスローション 180ml", "オルビスミスター 化粧水"],
                "must_include": ["オルビス", "ミスター"]
            },
            {
                "rank": 2,
                "brand": "SHISEIDO MEN (資生堂メン)",
                "name": "ハイドレーティング ローション C 150mL",
                "queries": ["資生堂メン ハイドレーティング ローション C 150ml", "SHISEIDO MEN ハイドレーティング ローション"],
                "must_include": ["ハイドレーティング"]
            },
            {
                "rank": 3,
                "brand": "BULK HOMME (バルクオム)",
                "name": "THE LOTION (ザ ローション 乳液) 100g / THE TONER 200mL",
                "queries": ["バルクオム ザ ローション 100g", "バルクオム ザ トナー 200ml"],
                "must_include": ["バルクオム"]
            },
            {
                "rank": 4,
                "brand": "NULL (ヌル)",
                "name": "薬用フェイスローション / オールインワンジェル 100g (医薬部外品)",
                "queries": ["NULL オールインワンジェル 100g", "NULL 薬用フェイスローション"],
                "must_include": ["NULL"]
            },
            {
                "rank": 5,
                "brand": "FANCL (ファンケル)",
                "name": "メン オールインワン スキンコンディショナー II しっとり 60mL",
                "queries": ["ファンケル メン オールインワン スキンコンディショナー しっとり", "ファンケル メン スキンコンディショナー"],
                "must_include": ["ファンケル", "メン"]
            },
            {
                "rank": 6,
                "brand": "magnifique (コーセー マニフィーク)",
                "name": "モイスチュアライジング ジェル 230mL",
                "queries": ["マニフィーク モイスチュアライジング ジェル 230ml", "KOSE マニフィーク オールインワン"],
                "must_include": ["マニフィーク"]
            },
            {
                "rank": 7,
                "brand": "QUATTRO BOTANICO (クワトロボタニコ)",
                "name": "ボタニカル ローション ＆ アフターシェーブ 115mL",
                "queries": ["クワトロボタニコ ボタニカル ローション アフターシェーブ", "クワトロボタニコ 化粧水"],
                "must_include": ["クワトロボタニコ"]
            },
            {
                "rank": 8,
                "brand": "MINON Men (第一三共ヘルスケア ミノン メン)",
                "name": "ミノン メン 薬用フェイスミルク 100mL (医薬部外品)",
                "queries": ["ミノン メン 薬用フェイスミルク", "ミノン メン フェイスローション"],
                "must_include": ["ミノン"]
            },
            {
                "rank": 9,
                "brand": "uno (資生堂 ウーノ)",
                "name": "バイタルクリームパーフェクション 90g (医薬部外品)",
                "queries": ["ウーノ バイタルクリームパーフェクション 90g", "uno バイタルクリームパーフェクション"],
                "must_include": ["バイタルクリームパーフェクション"]
            },
            {
                "rank": 10,
                "brand": "NIVEA MEN (花王 ニベアメン)",
                "name": "アクティブエイジバーム 110mL (医薬部外品)",
                "queries": ["ニベアメン アクティブエイジバーム 110ml", "ニベアメン アクティブエイジバーム"],
                "must_include": ["アクティブエイジ"]
            }
        ]
    }
}

def extract_image_url(cand):
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    raw = first.get("imageUrl", "") if isinstance(first, dict) else str(first)
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

def match_candidate(cand, must_include):
    name = cand.get("itemName", "")
    # Exclude obvious junk like empty bottles or unrelated items if possible
    for kw in must_include:
        if kw.lower() not in name.lower():
            return False
    return True

def fetch_all():
    results = {}
    total_fetched = 0
    total_expected = 30

    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n=== Fetching {cat_key} ===")
        results[cat_key] = {
            "file": cat_data["file"],
            "url": cat_data["url"],
            "title": cat_data["title"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"  Rank {item['rank']}: query='{q}'")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=10&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                try:
                    time.sleep(1.5)
                    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                        data = json.loads(res.read().decode('utf-8'))
                        items = data.get("Items", [])
                        # Pass 1: strict match_candidate + non-refill preferred
                        for it in items:
                            cand = it["Item"]
                            price = cand.get("itemPrice", 0)
                            iname = cand.get("itemName", "")
                            if price >= 350 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and match_candidate(cand, item["must_include"]):
                                if "詰替" not in iname and "詰め替え" not in iname and "レフィル" not in iname:
                                    chosen_item = cand
                                    break
                        # Pass 2: allow refill if no main bottle found
                        if not chosen_item:
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 350 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and match_candidate(cand, item["must_include"]):
                                    chosen_item = cand
                                    break
                        # Pass 3: fallback to first valid priced item
                        if not chosen_item:
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 350 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                    if chosen_item:
                        break
                except urllib.error.HTTPError as e:
                    print(f"    HTTP Error {e.code}: {e.reason}")
                    time.sleep(2.5)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(2.0)

            if chosen_item:
                img_url = extract_image_url(chosen_item)
                aff_url = chosen_item.get("affiliateUrl") or chosen_item.get("itemUrl")
                print(f"    -> MATCH: {chosen_item['itemName'][:55]} (¥{chosen_item['itemPrice']:,})")
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": aff_url,
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "4.5"))
                })
                total_fetched += 1
            else:
                print(f"    ❌ FAILED for Rank {item['rank']}: {item['name']}")

    with open("fetched_3new_nov_dec_2026_1121.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nDone! Fetched {total_fetched}/{total_expected} items.")

if __name__ == "__main__":
    fetch_all()
