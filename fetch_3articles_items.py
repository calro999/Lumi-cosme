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
    "winter_face_mask": {
        "title": "高保湿シートマスク＆夜用レスキューパック",
        "page_file": "winter-face-mask.html",
        "items": [
            {"rank": 1, "query": "トリデン ダイブイン マスク パック", "brand": "Torriden (トリデン)", "name": "ダイブイン マスク (低分子ヒアルロン酸シートマスク)"},
            {"rank": 2, "query": "ルルルン ハイドラ EX マスク 28枚", "brand": "LuLuLun (ルルルン)", "name": "ルルルン ハイドラ EX マスク (エクソソーム×グルタチオン)"},
            {"rank": 3, "query": "メディヒール N.M.F アクア アンプルマスク", "brand": "MEDIHEAL (メディヒール)", "name": "N.M.F アクア アンプルマスク JEX"},
            {"rank": 4, "query": "ミノン アミノモイスト ぷるぷるしっとり肌マスク", "brand": "MINON (ミノン)", "name": "アミノモイスト ぷるぷるしっとり肌マスク"},
            {"rank": 5, "query": "VT CICA デイリースージングマスク", "brand": "VT COSMETICS (ブイティー)", "name": "CICA デイリースージングマスク (30枚入)"},
            {"rank": 6, "query": "バイオダンス バイオコラーゲン リアルディープマスク", "brand": "BIODANCE (バイオダンス)", "name": "バイオコラーゲン リアルディープマスク"},
            {"rank": 7, "query": "クオリティファースト ダーマレーザー スーパーセラミド100", "brand": "QUALITY 1st (クオリティファースト)", "name": "ダーマレーザー スーパー セラミド100 マスク"},
            {"rank": 8, "query": "アビブ ドクダミフィット ガムシートマスク", "brand": "Abib (アビブ)", "name": "ガムシートマスクパック ドクダミステッカー"},
            {"rank": 9, "query": "エリクシール スリーピングジェルパック", "brand": "ELIXIR (エリクシール)", "name": "シュペリエル スリーピングジェルパック W (ナイトリペア)"},
            {"rank": 10, "query": "SK-II フェイシャルトリートメント マスク", "brand": "SK-II (エスケーツー)", "name": "フェイシャル トリートメント マスク (集中ピテラケア)"}
        ]
    },
    "winter_body_care": {
        "title": "高保湿ボディミルク＆濃厚ボディバター",
        "page_file": "winter-body-care.html",
        "items": [
            {"rank": 1, "query": "ニュートロジーナ インテンスリペア CICA ボディエマルジョン 250ml", "brand": "Neutrogena (ニュートロジーナ)", "name": "ノルウェーフォーミュラ インテンスリペア CICA エマルジョン"},
            {"rank": 2, "query": "ニベア スキンミルク しっとり 200g", "brand": "NIVEA (ニベア)", "name": "ニベア スキンミルク しっとり (超乾燥肌用)"},
            {"rank": 3, "query": "キュレル モイスチャーバーム 70g", "brand": "Curel (キュレル)", "name": "モイスチャーバーム 【医薬部外品】 (顔・からだ用)"},
            {"rank": 4, "query": "セタフィル モイスチャライジングローション 591ml", "brand": "Cetaphil (セタフィル)", "name": "モイスチャライジング ローション (高保湿乳液)"},
            {"rank": 5, "query": "サボン リペア ボディクリーム パチュリ ラベンダー バニラ", "brand": "SABON (サボン)", "name": "リペア ボディクリーム (パチュリ・ラベンダー・バニラ)"},
            {"rank": 6, "query": "ローラメルシエ セラム ボディクリーム アンバーバニラ", "brand": "laura mercier (ローラ メルシエ)", "name": "セラム ボディクリーム アンバーバニラ"},
            {"rank": 7, "query": "アベンヌ トリクセラNT フルイドミルク 400ml", "brand": "Avene (アベンヌ)", "name": "トリクセラNT フルイドミルク (全身用保湿ミルク)"},
            {"rank": 8, "query": "ロクシタン スノーシア ボディクリーム 200ml", "brand": "L'OCCITANE (ロクシタン)", "name": "クラシック シア リッチボディクリーム"},
            {"rank": 9, "query": "ヴェレダ スキンフード ボディバター 150ml", "brand": "WELEDA (ヴェレダ)", "name": "スキンフード ボディバター (高保湿ホイップバーム)"},
            {"rank": 10, "query": "メンソレータム ヘパソフト 薬用 顔ローション 100g", "brand": "メンソレータム (ロート製薬)", "name": "ヘパソフト 薬用 顔ローション / 乾燥かゆみ乳液 【医薬部外品】"}
        ]
    },
    "winter_eye_cream": {
        "title": "高保湿アイクリーム＆薬用リンクルケア",
        "page_file": "winter-eye-cream.html",
        "items": [
            {"rank": 1, "query": "エリクシール レチノパワー リンクルクリーム", "brand": "ELIXIR (エリクシール)", "name": "レチノパワー リンクルクリーム S 【医薬部外品】 (純粋レチノール)"},
            {"rank": 2, "query": "コスメデコルテ リポソーム アドバンスト リペアアイセラム", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアアイセラム (目元美容液)"},
            {"rank": 3, "query": "ポーラ リンクルショット メディカルセラム", "brand": "POLA (ポーラ)", "name": "リンクルショット メディカル セラム N 【医薬部外品】"},
            {"rank": 4, "query": "なめらか本舗 リンクルアイクリーム", "brand": "サナ なめらか本舗", "name": "リンクルアイクリーム N (ピュアレチノール×豆乳発酵液)"},
            {"rank": 5, "query": "キュレル 潤浸保湿 モイストリペア アイクリーム 25g", "brand": "Curel (キュレル)", "name": "潤浸保湿 モイストリペア アイクリーム 【医薬部外品】"},
            {"rank": 6, "query": "クラランス ダブル セーラム アイ 20ml", "brand": "CLARINS (クラランス)", "name": "ダブル セーラム アイ (2層式目元美容液)"},
            {"rank": 7, "query": "クリニーク スマート リペア アイ クリーム 15ml", "brand": "CLINIQUE (クリニーク)", "name": "スマート リペア アイ クリーム (次世代ペプチド)"},
            {"rank": 8, "query": "アスタリフト リンクルリペア", "brand": "ASTALIFT (アスタリフト)", "name": "ザ セラム リンクルリペア (薬用シワ改善美容液)"},
            {"rank": 9, "query": "キールズ アイクリーム PW 14g", "brand": "Kiehl's (キールズ)", "name": "キールズ アイクリーム PW (アボカドオイル高配合)"},
            {"rank": 10, "query": "資生堂 バイタルパーフェクション リンクルリフト ディープレチノホワイト5", "brand": "SHISEIDO (資生堂)", "name": "バイタルパーフェクション リンクルリフト ディープレチノホワイト5 【医薬部外品】"}
        ]
    }
}

def fetch_item_with_retry(query_info):
    query = query_info["query"]
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    raw_item = items[0]["Item"]
                    raw_img = ""
                    if raw_item.get("mediumImageUrls"):
                        raw_img = raw_item["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "display_name": query_info["name"],
                        "item_name": raw_item.get("itemName", ""),
                        "price": raw_item.get("itemPrice", 0),
                        "affiliate_url": raw_item.get("affiliateUrl", ""),
                        "image_url": high_res_img,
                        "shop_name": raw_item.get("shopName", ""),
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", 0)
                    }
                else:
                    print(f"No item found for query '{query}'")
                    return None
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 2.0 * (attempt + 1)
                print(f"  [429 Rate limited] waiting {wait_time}s on '{query}'...")
                time.sleep(wait_time)
            else:
                print(f"  [HTTPError {e.code}] on '{query}'")
                time.sleep(1.5)
        except Exception as e:
            print(f"  [Exception] {e} on '{query}'")
            time.sleep(1.5)
    return None

def main():
    final_data = {}
    for cat_id, cat_meta in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"▶ Fetching: {cat_meta['title']} ({cat_id})")
        print(f"==========================================")
        final_data[cat_id] = {
            "title": cat_meta["title"],
            "page_file": cat_meta["page_file"],
            "items": []
        }
        for item in cat_meta["items"]:
            print(f"Fetching [Rank {item['rank']}] {item['brand']} - {item['name']}...")
            res = fetch_item_with_retry(item)
            if res:
                print(f"  ✓ SUCCESS: {res['item_name'][:40]} | ¥{res['price']:,} | ★{res['review_average']} ({res['review_count']}件)")
                final_data[cat_id]["items"].append(res)
            else:
                print(f"  ✗ FAILED: {item['name']}")
            time.sleep(1.2) # APIレートリミット対策

    with open("rakuten_latest_3articles_data.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    total_count = sum(len(cat["items"]) for cat in final_data.values())
    print(f"\n==========================================")
    print(f"Successfully collected {total_count} / 30 items!")
    print(f"Saved to rakuten_latest_3articles_data.json")

if __name__ == "__main__":
    main()
