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
    "winter_emulsion": {
        "title": "高保湿乳液＆エマルジョン",
        "page_file": "winter-emulsion.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ AQ アブソリュート エマルジョン", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ アブソリュート エマルジョン マイクロラディアンス (先行型・ツヤ弾力乳液)"},
            {"rank": 2, "query": "アルビオン フラルネ フルリファイン ミルク", "brand": "ALBION (アルビオン)", "name": "フラルネ フルリファイン ミルク EM (キメ美肌・先行高保湿乳液)"},
            {"rank": 3, "query": "ミノン アミノモイスト モイストチャージ ミルク", "brand": "MINON (ミノン)", "name": "アミノモイスト モイストチャージ ミルク (9種保水アミノ酸・濃厚ミルク)"},
            {"rank": 4, "query": "キュレル 潤浸保湿 乳液", "brand": "Curel (キュレル)", "name": "潤浸保湿 乳液 【医薬部外品】 (セラミド機能成分配合・乾燥肌用)"},
            {"rank": 5, "query": "エリクシール リフトモイスト エマルジョン SP", "brand": "ELIXIR (エリクシール)", "name": "リフトモイスト エマルジョン SP III とてもしっとり (つや玉・薬用ハリ乳液)"},
            {"rank": 6, "query": "ポーラ BA ミルク N", "brand": "POLA (ポーラ)", "name": "B.A ミルク N (最高峰エイジングケア・濃密ハリ感エマルジョン)"},
            {"rank": 7, "query": "カルテHD モイスチュア エマルジョン", "brand": "Carte (カルテHD)", "name": "モイスチュア エマルジョン 【医薬部外品】 (ヘパリン類似物質HD配合)"},
            {"rank": 8, "query": "dプログラム モイストケア エマルジョン", "brand": "d program (資生堂)", "name": "モイストケア エマルジョン MB 【医薬部外品】 (美肌菌サポート敏感肌用)"},
            {"rank": 9, "query": "なめらか本舗 リンクル乳液", "brand": "なめらか本舗 (SANA)", "name": "リンクル乳液 N (ピュアレチノール×豆乳イソフラボン配合)"},
            {"rank": 10, "query": "ソフィーナ ボーテ 高保湿乳液 とてもしっとり", "brand": "SOFINA beaute (ソフィーナ)", "name": "高保湿乳液 とてもしっとり 【医薬部外品】 (持続型セラミドケア処方)"}
        ]
    },
    "winter_face_oil": {
        "title": "高保湿フェイスオイル＆美容オイル",
        "page_file": "winter-face-oil.html",
        "items": [
            {"rank": 1, "query": "ハーバー 高品位 スクワラン 30ml", "brand": "HABA (ハーバー)", "name": "高品位「スクワラン」 (純度99.9%・うるおいシールド天然オイル)"},
            {"rank": 2, "query": "メルヴィータ ビオオイル アルガンオイル 50ml", "brand": "Melvita (メルヴィータ)", "name": "ビオオイル アルガンオイル (100%オーガニック・ブースター導入オイル)"},
            {"rank": 3, "query": "RMK Wトリートメントオイル 50ml", "brand": "RMK (アールエムケー)", "name": "Wトリートメントオイル (オイル層×うるおい層・2層式トリートメント)"},
            {"rank": 4, "query": "トリロジー ローズヒップ オイル 20ml", "brand": "trilogy (トリロジー)", "name": "ローズヒップ オイル (必須脂肪酸80%以上・極上ビタミンオイル)"},
            {"rank": 5, "query": "キールズ ミッドナイトボタニカル コンセントレート 30ml", "brand": "KIEHL'S (キールズ)", "name": "ミッドナイトボタニカル コンセントレート (夜用美容オイル・植物ブレンド)"},
            {"rank": 6, "query": "アルビオン ハーバルオイル トリニティフュージョン", "brand": "ALBION (アルビオン)", "name": "ハーバルオイル トリニティフュージョン (インカオメガ×ボラージ厳選オイル)"},
            {"rank": 7, "query": "コスメデコルテ AQ ボタニカル ピュアオイル", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ ボタニカル ピュアオイル (100%植物由来・艶めく濃密オイル)"},
            {"rank": 8, "query": "無印良品 ホホバオイル 200ml", "brand": "無印良品 (MUJI)", "name": "ホホバオイル (植物から搾ったピュアオイル・全身マルチケア)"},
            {"rank": 9, "query": "ニールズヤード フランキンセンス フェイシャルオイル", "brand": "NEAL'S YARD (ニールズヤード)", "name": "フランキンセンス フェイシャルオイル (濃密プレミアム植物オイル)"},
            {"rank": 10, "query": "クナイプ ビオ オイル ローズ 100ml", "brand": "Kneipp (クナイプ)", "name": "ビオ オイル ローズ (オーガニック野ばらオイル・高保湿エイジングケア)"}
        ]
    },
    "winter_repair_balm": {
        "title": "高保湿リペアバーム＆レスキューマルチバーム",
        "page_file": "winter-repair-balm.html",
        "items": [
            {"rank": 1, "query": "イハダ 薬用バーム 20g", "brand": "IHADA (イハダ)", "name": "薬用バーム 【医薬部外品】 (高精製ワセリン配合・密着保護シールド)"},
            {"rank": 2, "query": "ラロッシュポゼ シカプラスト リペアクリーム B5+", "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)", "name": "シカプラスト リペアクリーム B5+ (ダーマリペア処方・高保湿シールド)"},
            {"rank": 3, "query": "サンホワイト シルキー Y-1 80g", "brand": "Sun White (サンホワイト)", "name": "サンホワイト シルキー Y-1 (純度100%白色ワセリン・無添加低刺激)"},
            {"rank": 4, "query": "カルテHD モイスチュア バーム", "brand": "Carte (カルテHD)", "name": "モイスチュア バーム 【医薬部外品】 (保水有効成分ヘパリン類似物質HD配合)"},
            {"rank": 5, "query": "dプログラム バームリペア オー", "brand": "d program (資生堂)", "name": "バームリペア オー 【医薬部外品】 (肌荒れ・粉吹き集中ケア固型バーム)"},
            {"rank": 6, "query": "オバジ ダーマパワーX リップエッセンス", "brand": "Obagi (オバジ)", "name": "ダーマパワーX リップエッセンス (高密着ビタミンA誘導体バーム)"},
            {"rank": 7, "query": "カネボウ リップバーム", "brand": "KANEBO (カネボウ)", "name": "リップバーム モイスチャーフロー (濃密うるおい膜・マルチポイントバーム)"},
            {"rank": 8, "query": "ドクタージャルト シカペア クリーム 50ml", "brand": "Dr.Jart+ (ドクタージャルト)", "name": "シカペア インテンシブ スムージング リペア バームクリーム (高濃度CICA)"},
            {"rank": 9, "query": "ファミュ ビューティ バーム", "brand": "FEMMUE (ファミュ)", "name": "ビューティ バーム (カメリアオイル配合・ボタニカル濃厚バーム)"},
            {"rank": 10, "query": "トリロジー エブリシング バーム 45ml", "brand": "trilogy (トリロジー)", "name": "エブリシング バーム (マルーラオイル×ローズヒップ全身マルチバーム)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
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
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", 0),
                        "shop_name": raw_item.get("shopName", "")
                    }
                else:
                    print(f"  Warning: No item found for query '{query}', trying simplified query...")
                    if len(query.split()) > 1:
                        query = query.split()[0] + " " + query.split()[1]
                        time.sleep(1.2)
                        continue
        except Exception as e:
            print(f"  Attempt {attempt+1} error for '{query}': {e}")
            time.sleep(1.5 * (attempt + 1))
    
    print(f"FAILED TO FETCH: {raw_q}")
    return None

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_data['title']} ({cat_key})")
    print(f"==========================================")
    cat_results = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['brand']} - {item_info['query']}...")
        res = fetch_item_with_retry(item_info)
        if res:
            cat_results["items"].append(res)
            print(f"  -> OK! {res['display_name']} | ￥{res['price']:,} | Reviews: {res['review_count']}")
        else:
            print(f"  -> ERROR! Could not fetch item.")
        time.sleep(1.2)
    
    results[cat_key] = cat_results

with open("rakuten_emulsion_oil_balm_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nAll 30 items fetched and saved to rakuten_emulsion_oil_balm_data.json successfully!")
