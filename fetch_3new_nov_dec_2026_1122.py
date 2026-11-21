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
    "winter_clay_mask": {
        "file": "winter-clay-mask.html",
        "url": "/winter-clay-mask",
        "title": "お風呂で温まりながらくすみ・ゴワつきを潤いオフ！つっぱらない高保湿クレイマスク＆洗い流す泥パック厳選ランク10【11月・12月】",
        "items": [
            {
                "rank": 1,
                "brand": "IPSA (イプサ)",
                "name": "ルミナイジング クレイex 100g",
                "queries": ["イプサ ルミナイジング クレイex 100g", "IPSA ルミナイジング クレイ"],
                "must_include": ["ルミナイジング", "クレイ"]
            },
            {
                "rank": 2,
                "brand": "Kiehl's (キールズ)",
                "name": "レアアース マスク 125mL",
                "queries": ["キールズ レアアース マスク 125ml", "キールズ レアアース マスク"],
                "must_include": ["レアアース"]
            },
            {
                "rank": 3,
                "brand": "beplain (ビープレーン)",
                "name": "緑豆毛穴クレイパック 120mL",
                "queries": ["ビープレーン 緑豆 クレイパック 120ml", "beplain 緑豆 クレイ"],
                "must_include": ["緑豆"]
            },
            {
                "rank": 4,
                "brand": "innisfree (イニスフリー)",
                "name": "スーパーヴォルカニック ポア クレイマスク 100mL",
                "queries": ["イニスフリー スーパーヴォルカニック ポア クレイマスク 100ml", "イニスフリー クレイマスク"],
                "must_include": ["ヴォルカニック", "クレイ"]
            },
            {
                "rank": 5,
                "brand": "SABON (サボン)",
                "name": "デッドシー 3in1 フェイシャルマッドスクラブマスク 150mL",
                "queries": ["サボン フェイシャルマッドスクラブマスク", "SABON デッドシー マッドスクラブ"],
                "must_include": ["スクラブマスク"]
            },
            {
                "rank": 6,
                "brand": "SKIN1004 (スキン1004)",
                "name": "マダガスカル センテラ ポアマイジング クイッククレイスティックマスク 27g",
                "queries": ["SKIN1004 ポアマイジング クレイスティック", "スキン1004 クレイスティックマスク"],
                "must_include": ["クレイ", "スティック"]
            },
            {
                "rank": 7,
                "brand": "VT COSMETICS (ブイティー)",
                "name": "CICA カプセルマスク 7.5g×10個",
                "queries": ["VT シカ カプセルマスク 10個", "VT CICA カプセルマスク"],
                "must_include": ["カプセルマスク"]
            },
            {
                "rank": 8,
                "brand": "FANCL (ファンケル)",
                "name": "ポア クレンジング パック 40g",
                "queries": ["ファンケル ポア クレンジング パック 40g", "FANCL ポアクレンジングパック"],
                "must_include": ["ポア", "パック"]
            },
            {
                "rank": 9,
                "brand": "naiad (ナイアード)",
                "name": "ガスール固形 500g / 粉末",
                "queries": ["ナイアード ガスール 500g", "ナイアード ガスール 固形"],
                "must_include": ["ガスール"]
            },
            {
                "rank": 10,
                "brand": "CLAYGE (クレージュ)",
                "name": "ミネラル クレイパック / モイストクレイ",
                "queries": ["クレージュ クレイパック フェイス", "クレージュ ウォームクレイパック", "DROAS クレイクリアウォッシュ"],
                "must_include": ["クレイ"]
            }
        ]
    },
    "winter_acne_moisture": {
        "file": "winter-acne-moisture.html",
        "url": "/winter-acne-moisture",
        "title": "冬の乾燥大人ニキビを乾かさず鎮静！高保湿×ノンコメドジェニック薬用スキンケアおすすめランク10【11月・12月】",
        "items": [
            {
                "rank": 1,
                "brand": "d program (資生堂 dプログラム)",
                "name": "アクネケア ローション MB 125mL (医薬部外品)",
                "queries": ["dプログラム アクネケア ローション MB 125ml", "dプログラム アクネケア ローション"],
                "must_include": ["アクネケア", "ローション"]
            },
            {
                "rank": 2,
                "brand": "ORBIS (オルビス)",
                "name": "クリアフル モイスチャー M しっとりタイプ 50g (医薬部外品)",
                "queries": ["オルビス クリアフル モイスチャー しっとり 50g", "オルビス クリアフル モイスチャー M"],
                "must_include": ["クリアフル", "モイスチャー"]
            },
            {
                "rank": 3,
                "brand": "MINON (第一三共ヘルスケア ミノン)",
                "name": "アミノモイスト 薬用アクネケア ミルク 100g (医薬部外品)",
                "queries": ["ミノン アミノモイスト 薬用アクネケア ミルク 100g", "ミノン 薬用アクネケア ミルク"],
                "must_include": ["アクネケア", "ミルク"]
            },
            {
                "rank": 4,
                "brand": "NOV (常盤薬品 ノブ)",
                "name": "ACアクティブ モイスチュアミルク 50mL (医薬部外品)",
                "queries": ["ノブ ACアクティブ モイスチュアミルク 50ml", "NOV ACアクティブ モイスチュアミルク"],
                "must_include": ["ACアクティブ", "ミルク"]
            },
            {
                "rank": 5,
                "brand": "Curel (花王 キュレル)",
                "name": "皮脂トラブルケア 保湿ジェル 120mL (医薬部外品)",
                "queries": ["キュレル 皮脂トラブルケア 保湿ジェル 120ml", "キュレル 皮脂トラブルケア 保湿ジェル"],
                "must_include": ["皮脂トラブルケア", "保湿ジェル"]
            },
            {
                "rank": 6,
                "brand": "FANCL (ファンケル)",
                "name": "アクネケア 化粧液 30mL (医薬部外品)",
                "queries": ["ファンケル アクネケア 化粧液 30ml", "FANCL アクネケア 化粧液"],
                "must_include": ["アクネケア", "化粧液"]
            },
            {
                "rank": 7,
                "brand": "IHADA (資生堂 イハダ)",
                "name": "薬用クリアバーム 18g (医薬部外品)",
                "queries": ["イハダ 薬用クリアバーム 18g", "IHADA 薬用クリアバーム"],
                "must_include": ["クリアバーム"]
            },
            {
                "rank": 8,
                "brand": "Carte HD (コーセー カルテHD)",
                "name": "バランスケア ゲル 100g / エマルジョン (医薬部外品)",
                "queries": ["カルテHD バランスケア ゲル 100g", "カルテHD バランスケア エマルジョン"],
                "must_include": ["バランスケア"]
            },
            {
                "rank": 9,
                "brand": "Torriden (トリデン)",
                "name": "バランスフル シカクリーム 80mL",
                "queries": ["トリデン バランスフル シカクリーム 80ml", "Torriden バランスフル シカクリーム"],
                "must_include": ["バランスフル", "クリーム"]
            },
            {
                "rank": 10,
                "brand": "肌ラボ (ロート製薬)",
                "name": "薬用 極潤 スキンコンディショナー しっとりタイプ 170mL (医薬部外品)",
                "queries": ["肌ラボ 薬用 極潤 スキンコンディショナー しっとり 170ml", "極潤 スキンコンディショナー しっとり"],
                "must_include": ["スキンコンディショナー"]
            }
        ]
    },
    "winter_powder_foundation": {
        "file": "winter-powder-foundation.html",
        "url": "/winter-powder-foundation",
        "title": "保湿力の強さで粉吹き肌とさようなら！真冬もしっとり密着する保湿力高めパウダーファンデーションランク10【11月・12月】",
        "items": [
            {
                "rank": 1,
                "brand": "MAQuillAGE (資生堂 マキアージュ)",
                "name": "ドラマティックパウダリー EX (レフィル)",
                "queries": ["マキアージュ ドラマティックパウダリー EX オークル10", "マキアージュ ドラマティックパウダリー EX"],
                "must_include": ["ドラマティックパウダリー"]
            },
            {
                "rank": 2,
                "brand": "ALBION (アルビオン)",
                "name": "プリンプ パウダレスト / アルビオン パウダレスト",
                "queries": ["アルビオン プリンプ パウダレスト", "アルビオン シュクルホワイト パウダレスト"],
                "must_include": ["パウダレスト"]
            },
            {
                "rank": 3,
                "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)",
                "name": "タンプードルエクラII",
                "queries": ["クレドポーボーテ タンプードルエクラII", "タンプードルエクラII"],
                "must_include": ["タンプードルエクラ"]
            },
            {
                "rank": 4,
                "brand": "COVERMARK (カバーマーク)",
                "name": "モイスチュア ヴェール LX",
                "queries": ["カバーマーク モイスチュア ヴェール LX", "カバーマーク シルキー フィット"],
                "must_include": ["カバーマーク"]
            },
            {
                "rank": 5,
                "brand": "ESPRIQUE (コーセー エスプリーク)",
                "name": "シンクロフィット パクト EX",
                "queries": ["エスプリーク シンクロフィット パクト EX", "エスプリーク パクト EX"],
                "must_include": ["シンクロフィット"]
            },
            {
                "rank": 6,
                "brand": "Primavista (花王 プリマヴィスタ)",
                "name": "ブライトチャージ パウダー",
                "queries": ["プリマヴィスタ ブライトチャージ パウダー", "ソフィーナ プリマヴィスタ ブライトチャージ"],
                "must_include": ["ブライトチャージ"]
            },
            {
                "rank": 7,
                "brand": "ETVOS (エトヴォス)",
                "name": "タイムレスフォギーミネラルファンデーション",
                "queries": ["エトヴォス タイムレスフォギーミネラルファンデーション", "ETVOS タイムレスフォギー"],
                "must_include": ["タイムレスフォギー"]
            },
            {
                "rank": 8,
                "brand": "VINTORTE (ヴァントルテ)",
                "name": "ミネラルシルクファンデーション",
                "queries": ["ヴァントルテ ミネラルシルクファンデーション", "VINTORTE ミネラルシルク"],
                "must_include": ["ミネラルシルク"]
            },
            {
                "rank": 9,
                "brand": "ORBIS (オルビス)",
                "name": "カシミアフィットファンデーション",
                "queries": ["オルビス カシミアフィットファンデーション", "ORBIS カシミアフィット"],
                "must_include": ["カシミアフィット"]
            },
            {
                "rank": 10,
                "brand": "CEZANNE (セザンヌ)",
                "name": "ウルトラカバーUVパクト / シフォンフィットクッション? No: ウルトラカバーUVファンデーション",
                "queries": ["セザンヌ ウルトラカバーUVパクト", "インテグレート プロフィニッシュファンデーション"],
                "must_include": ["パクト"]
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
                        # Pass 1: strict match_candidate + non-refill/case-only preferred
                        for it in items:
                            cand = it["Item"]
                            price = cand.get("itemPrice", 0)
                            iname = cand.get("itemName", "")
                            if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and match_candidate(cand, item["must_include"]):
                                if "ケースのみ" not in iname and "パフのみ" not in iname and "スポンジのみ" not in iname and "詰替" not in iname and "詰め替え" not in iname:
                                    chosen_item = cand
                                    break
                        # Pass 2: allow refill if needed
                        if not chosen_item:
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                iname = cand.get("itemName", "")
                                if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and match_candidate(cand, item["must_include"]):
                                    if "ケースのみ" not in iname and "パフのみ" not in iname and "スポンジのみ" not in iname:
                                        chosen_item = cand
                                        break
                        # Pass 3: fallback
                        if not chosen_item:
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
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
                print(f"    -> MATCH: {chosen_item['itemName'][:65]} (¥{chosen_item['itemPrice']:,})")
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

    with open("fetched_3new_nov_dec_2026_1122.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nDone! Fetched {total_fetched}/{total_expected} items.")

if __name__ == "__main__":
    fetch_all()
