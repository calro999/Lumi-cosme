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
    "winter_hair_milk": {
        "title": "髪のパサつき・静電気を防ぐ高保湿ヘアミルク＆アウトバストリートメント",
        "page_file": "winter-hair-milk.html",
        "items": [
            {"rank": 1, "query": "オルビス エッセンスインヘアミルク 140g", "brand": "ORBIS (オルビス)", "name": "エッセンスインヘアミルク (浸透美容液成分×高保水ミルク・無香料)"},
            {"rank": 2, "query": "ミルボン エルジューダ エマルジョン プラス 120g", "brand": "MILBON (ミルボン)", "name": "ディーセス エルジューダ エマルジョン+ (バオバブエキス×CMADK・普通〜太毛用高保湿)"},
            {"rank": 3, "query": "ミルボン エルジューダ エマルジョン 120g", "brand": "MILBON (ミルボン)", "name": "ディーセス エルジューダ エマルジョン (セラミド2配合・細毛軟毛用ふんわり保水)"},
            {"rank": 4, "query": "スティーブンノル モイスチュアソフニング エマルジョン N", "brand": "STEPHEN KNOLL (スティーブンノル)", "name": "モイスチュアソフニング エマルジョン N (高浸透インナーリペアカプセル配合)"},
            {"rank": 5, "query": "ナプラ N. エヌドット SHEA ミルク 150g", "brand": "napla (ナプラ)", "name": "N. SHEAミルク (高保湿シアバター×マルラオイル・超しっとり毛先補修)"},
            {"rank": 6, "query": "モロッカンオイル オールインワン リーブイン コンディショナー 160ml", "brand": "MOROCCANOIL (モロッカンオイル)", "name": "オールインワン リーブイン コンディショナー (高浸透アルガンオイル×アミノ酸スプレーミルク)"},
            {"rank": 7, "query": "ルベル SEE SAW シーソー リペアミルク モイスト 100ml", "brand": "LebeL (ルベル)", "name": "SEE/SAW ヘア＆スキャルプ リペアミルク モイスト (田中みな実愛用・光反射ツヤ保湿)"},
            {"rank": 8, "query": "ラサーナ 海藻 ヘア ミルク 120g", "brand": "La Sana (ラサーナ)", "name": "海藻 ヘア ミルク (海藻エキス×高純度植物オイル・朝の広がり＆UV遮断)"},
            {"rank": 9, "query": "ケラスターゼ RE シモン テルミック 150g", "brand": "KERASTASE (ケラスターゼ)", "name": "レジスタンス シモン テルミック (熱の力で浸透補修・ブロー熱ガード高機能ミルク)"},
            {"rank": 10, "query": "パンテーン 洗い流さないトリートメント インテンシブ ヴィタミルク", "brand": "P&G PANTENE (パンテーン)", "name": "エクストラダメージケア インテンシブ ヴィタミルク (プロビタミン高浸透カプセル)"}
        ]
    },
    "winter_cushion_foundation": {
        "title": "暖房直撃でも乾燥割れ・粉浮きしない高保湿クッションファンデーション",
        "page_file": "winter-cushion-foundation.html",
        "items": [
            {"rank": 1, "query": "TIRTIR マスクフィット クリスタルメッシュクッション", "brand": "TIRTIR (ティルティル)", "name": "マスクフィット クリスタルメッシュクッション (72時間水光ツヤ持続・微細メッシュ)"},
            {"rank": 2, "query": "CLIO クリオ キルカバー ハイグロウ クッション", "brand": "CLIO (クリオ)", "name": "キルカバー ハイグロウ クッション (72時間クリア水光グロウ・高密度ヒアルロン酸膜)"},
            {"rank": 3, "query": "ジョンセンムル エッセンシャル スキン ヌーダー クッション", "brand": "JUNG SAEM MOOL (ジョンセンムル)", "name": "エッセンシャル スキン ヌーダー クッション (天然保湿複合成分・プロ級生ツヤ肌)"},
            {"rank": 4, "query": "HERA ヘラ スキンラディアント グロウ クッション", "brand": "HERA (ヘラ)", "name": "スキンラディアント グロウ クッション (スキンケア成分64%配合・極上セミグロウ)"},
            {"rank": 5, "query": "ローラ メルシエ フローレス ルミエール ラディアンス パーフェクティング クッション", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "フローレス ルミエール ラディアンス パーフェクティング クッション (ダイヤモンド粉末配合)"},
            {"rank": 6, "query": "イヴ サンローラン ラディアント タッチ グロウパクト", "brand": "YVES SAINT LAURENT (イヴ・サンローラン)", "name": "ラディアント タッチ グロウパクト (マローエキス配合メッシュファンデ・光のヴェール)"},
            {"rank": 7, "query": "MISSHA ミシャ M クッション ファンデーション モイスチャー", "brand": "MISSHA (ミシャ)", "name": "M クッション ファンデーション モイスチャー (3種のフラワーウォーター×美容オイル)"},
            {"rank": 8, "query": "ディオールスキン フォーエヴァー イドラ グロウ クッション", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオールスキン フォーエヴァー イドラ グロウ クッション (フローラルエキス配合・濃密うるおい)"},
            {"rank": 9, "query": "アンドビー be クッションファンデーション", "brand": "&be (アンドビー)", "name": "クッションファンデーション (河北裕介プロデュース・石鹸オフ・高保湿ノンケミカル)"},
            {"rank": 10, "query": "ロムアンド ベアウォータークッション", "brand": "rom&nd (ロムアンド)", "name": "ベアウォータークッション (水分エッセンス70%配合・ヒアルロン酸10種・水滴ツヤ肌)"}
        ]
    },
    "winter_body_scrub": {
        "title": "頑固なゴワつき・粉吹きをオフしオイル膜で満たす高保湿ボディスクラブ",
        "page_file": "winter-body-scrub.html",
        "items": [
            {"rank": 1, "query": "SABON サボン ボディスクラブ 600g", "brand": "SABON (サボン)", "name": "ボディスクラブ (死海の塩×ボタニカルオイル4種・世界中で愛されるツルスベ肌の最高峰)"},
            {"rank": 2, "query": "ハウスオブローゼ Oh! Baby ボディ スムーザー N 570g", "brand": "HOUSE OF ROSE (ハウス オブ ローゼ)", "name": "Oh! Baby ボディ スムーザー N (由布院温泉水×体温37度で溶ける天然温泉スクラブ)"},
            {"rank": 3, "query": "オゥパラディ AUX PARADIS ボディ スクラブ 200g", "brand": "AUX PARADIS (オゥパラディ)", "name": "ボディ スクラブ (オーガニックシュガー×アルガンオイル・しっとり極上角質ケア)"},
            {"rank": 4, "query": "クナイプ シュガースクラブ 200ml", "brand": "Kneipp (クナイプ)", "name": "シュガースクラブ カメリア＆アルガン (天然シュガー×アルガンオイル・お風呂でそのまま保湿パック)"},
            {"rank": 5, "query": "イソップ レデンプション ボディスクラブ 180ml", "brand": "Aesop (イソップ)", "name": "レデンプション ボディスクラブ (微粉末軽石×竹の微粒子・精油のウッディなアロマ)"},
            {"rank": 6, "query": "ジョー マローン エクスフォリエイティング シャワージェル 200ml", "brand": "JO MALONE LONDON (ジョー マローン ロンドン)", "name": "エクスフォリエイティング シャワージェル (ホホバビーズ×極上の香り・デイリー角質ケア)"},
            {"rank": 7, "query": "ダヴ クリーミースクラブ", "brand": "Dove (ダヴ)", "name": "クリーミースクラブ (まるでホイップクリーム質感・高浸透うるおいミルク成分高配合)"},
            {"rank": 8, "query": "WEEED ブリススクラブ 360g", "brand": "WEEED (ウィード)", "name": "ブリススクラブ (医薬部外品・薬用殺菌＆背中お尻ニキビ予防×9種のオーガニックオイル)"},
            {"rank": 9, "query": "ザボディショップ ボディスクラブ シア 250ml", "brand": "THE BODY SHOP (ザ・ボディショップ)", "name": "ボディスクラブ シア (コミュニティフェアトレードシアバター・こっくり濃厚リッチケア)"},
            {"rank": 10, "query": "クラランス スムージング ボディスクラブ 200ml", "brand": "CLARINS (クラランス)", "name": "スムージング ボディスクラブ (微粒子バンブーパウダー×シアバター・引き締め＆ふっくら弾力)"}
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
                    
                    price = raw_item.get("itemPrice", 0)
                    aff_url = raw_item.get("affiliateUrl", "")
                    shop_name = raw_item.get("shopName", "")
                    reviews = raw_item.get("reviewCount", 0)
                    rev_avg = raw_item.get("reviewAverage", 0.0)
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "official_item_name": raw_item.get("itemName", query_info["name"]),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": shop_name,
                        "review_count": reviews,
                        "review_average": rev_avg
                    }
                else:
                    # フォールバック検索：最初の2単語で検索
                    words = query.split()
                    if len(words) > 2:
                        fallback_q = " ".join(words[:2])
                        fb_url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(fallback_q)}&hits=1&format=json&sort=standard"
                        req2 = urllib.request.Request(fb_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                        with urllib.request.urlopen(req2, context=ctx, timeout=10) as res2:
                            fb_data = json.loads(res2.read().decode('utf-8'))
                            fb_items = fb_data.get("Items", [])
                            if fb_items:
                                raw_item = fb_items[0]["Item"]
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
                                    "name": query_info["name"],
                                    "official_item_name": raw_item.get("itemName", query_info["name"]),
                                    "price": raw_item.get("itemPrice", 0),
                                    "image_url": high_res_img,
                                    "affiliate_url": raw_item.get("affiliateUrl", ""),
                                    "shop_name": raw_item.get("shopName", ""),
                                    "review_count": raw_item.get("reviewCount", 0),
                                    "review_average": raw_item.get("reviewAverage", 0.0)
                                }
        except Exception as e:
            print(f"Error fetching {query} (attempt {attempt+1}): {e}")
            time.sleep(1.0)
    
    print(f"FAILED TO FETCH: {raw_q}")
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "official_item_name": query_info["name"],
        "price": 0,
        "image_url": "",
        "affiliate_url": "",
        "shop_name": "",
        "review_count": 0,
        "review_average": 0.0
    }

def main():
    result = {}
    for cat_key, cat_val in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_val['title']}")
        print(f"==========================================")
        fetched_items = []
        for q_info in cat_val["items"]:
            print(f"Fetching [Rank {q_info['rank']}] {q_info['query']} ...")
            item_data = fetch_item_with_retry(q_info)
            print(f" -> Found: {item_data['official_item_name'][:35]}... | Price: ¥{item_data['price']:,} | Reviews: {item_data['review_count']} ({item_data['review_average']}★)")
            fetched_items.append(item_data)
            time.sleep(0.3)
        result[cat_key] = {
            "title": cat_val["title"],
            "page_file": cat_val["page_file"],
            "items": fetched_items
        }
    
    out_file = "rakuten_hair_cushion_scrub_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nSuccessfully saved all data to {out_file}!")

if __name__ == "__main__":
    main()
