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
    "winter_highlighter": {
        "title": "暖房の乾燥くすみを一掃！内側から発光する濡れツヤ＆立体感を宿す高保湿ハイライト厳選10",
        "page_file": "winter-highlighter.html",
        "items": [
            {"rank": 1, "query": "シャネル ボーム エサンシエル スカルプティング", "brand": "CHANEL (シャネル)", "name": "ボーム エサンシエル (濡れツヤ肌の最高峰・体温でとろけるグロウスティック)"},
            {"rank": 2, "query": "hince トゥルーディメンション ラディアンスバーム", "brand": "hince (ヒンス)", "name": "トゥルーディメンション ラディアンスバーム (繊細な生ツヤ×透明感・乾燥知らずのマルチバーム)"},
            {"rank": 3, "query": "ディオール バックステージ フェイス グロウ パレット 001", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオール バックステージ フェイス グロウ パレット (極微細パール・4色で光と立体感を自在に操る神パレット)"},
            {"rank": 4, "query": "ローラ メルシエ フェイスイルミネーター ディボーション", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "フェイスイルミネーター (しっとりシルキー質感・乾燥小じわに入り込まない自然な発光)"},
            {"rank": 5, "query": "クレ・ド・ポー ボーテ ル・レオスールデクラ 21", "brand": "cle de peau BEAUTE (クレ・ド・ポー ボーテ)", "name": "ル・レオスールデクラ (宝石の輝きを再現・スキンケア成分配合の最高級プレシャスオパール)"},
            {"rank": 6, "query": "RMK グロースティック 3.4g", "brand": "RMK (アールエムケー)", "name": "グロースティック (パウダーの上からもヨレずに密着・ヌードな濡れツヤを瞬時に仕込む)"},
            {"rank": 7, "query": "コスメデコルテ ディップイン グロウ クリーム ハイライター", "brand": "DECORTÉ (コスメデコルテ)", "name": "ディップイン グロウ クリーム ハイライター (オーガニックムルムルバター高配合・メルティな光沢膜)"},
            {"rank": 8, "query": "&be アンドビー グロウハイライター", "brand": "&be (アンドビー)", "name": "グロウハイライター (河北裕介プロデュース・植物由来オイル×天然ミネラルの肌に優しい生ツヤ)"},
            {"rank": 9, "query": "エクセル ドレープド シマーグロウ", "brand": "excel (エクセル)", "name": "ドレープド シマーグロウ (シアバター配合の高密着パウダー・冬の肌にしっとり溶け込むプチプラ名品)"},
            {"rank": 10, "query": "セザンヌ パールグロウハイライト 01", "brand": "CEZANNE (セザンヌ)", "name": "パールグロウハイライト (まるで塗るレフ板・高輝度パールが乾燥くすみを瞬時に飛ばす)"}
        ]
    },
    "winter_hair_oil": {
        "title": "パサつき・静電気・マフラー摩擦を完全防御！毛先までしっとりまとまる高保湿＆熱補修ヘアオイル厳選10",
        "page_file": "winter-hair-oil.html",
        "items": [
            {"rank": 1, "query": "モロッカンオイル トリートメント 100ml ポンプ付き", "brand": "MOROCCANOIL (モロッカンオイル)", "name": "トリートメント (高純度アルガンオイル×ビタミンE・世界中で愛されるツヤ髪オイルの原点)"},
            {"rank": 2, "query": "ミルボン ディーセス エルジューダ MO 120ml", "brand": "MILBON (ミルボン)", "name": "ディーセス エルジューダ MO (オリーブスクワラン配合・硬い髪やゴワつきをしなやかに整える)"},
            {"rank": 3, "query": "ケラスターゼ CH ユイル クロノロジスト R 100ml", "brand": "KERASTASE (ケラスターゼ)", "name": "CH ユイル クロノロジスト R (最高峰キャビアエッセンス×ヒアルロン酸・熱と乾燥から徹底保護)"},
            {"rank": 4, "query": "ナプラ N. エヌドット ポリッシュオイル 150ml", "brand": "napla (ナプラ)", "name": "N. ポリッシュオイル (シアバター×天然由来原料100%・静電気防止＆束感ウェットツヤ)"},
            {"rank": 5, "query": "トラック オイル ナンバースリー track oil No.3 90ml", "brand": "track (トラック)", "name": "トラック オイル No.3 (金木犀の優雅な香り・濃厚な植物ブレンドでハイダメージ毛を集中補修)"},
            {"rank": 6, "query": "アンドハニー ディープモイスト ヘアオイル 3.0 100ml", "brand": "&honey (アンドハニー)", "name": "ディープモイスト ヘアオイル 3.0 (水分量14%に着目したハチミツ美容・パサつく毛先を超保湿)"},
            {"rank": 7, "query": "フィーノ プレミアムタッチ 浸透美容液ヘアオイル 70ml", "brand": "fino (フィーノ)", "name": "プレミアムタッチ 浸透美容液ヘアオイル (Wオイル処方・濃密なのにベタつかずちゅるん髪に)"},
            {"rank": 8, "query": "スティーブンノル モイスチュア リペア ヘアオイル 100ml", "brand": "STEPHEN KNOLL (スティーブンノル)", "name": "モイスチュア リペア ヘアオイル (W外部補修カプセル×熱プロテクト・枝毛や摩擦ダメージを防ぐ)"},
            {"rank": 9, "query": "ロレアル パリ エルセーヴ エクストラオーディナリー オイル エクストラリッチ フィニッシュ 100ml", "brand": "L'OREAL PARIS (ロレアル パリ)", "name": "エクストラオーディナリー オイル エクストラリッチ (6種のフラワーエキストラクトオイル・冬の深刻なパサつき用)"},
            {"rank": 10, "query": "大島椿 椿油 60ml", "brand": "大島椿 (オオシマツバキ)", "name": "椿油 100% (天然椿油100%・静電気と乾燥を完全シャットアウトする無添加の伝統名品)"}
        ]
    },
    "winter_lip_mask": {
        "title": "朝の唇に感動！就寝中の乾燥・皮剥け・縦ジワを濃厚ラップで集中リペアする高保湿リップマスク厳選10",
        "page_file": "winter-lip-mask.html",
        "items": [
            {"rank": 1, "query": "ラネージュ リップスリーピングマスク 20g ベリー", "brand": "LANEIGE (ラネージュ)", "name": "リップスリーピングマスク ベリー (ベリーフルーツコンプレックス×ビタミンC・翌朝角質オフでぷるぷる)"},
            {"rank": 2, "query": "キュレル リップケア バーム 4.2g", "brand": "Curel (キュレル)", "name": "リップケア バーム (医薬部外品・セラミド機能成分×消炎剤配合・夜のひび荒れ密着パック)"},
            {"rank": 3, "query": "Torriden トリデン ソリッドイン セラミド リップエッセンス 11ml", "brand": "Torriden (トリデン)", "name": "ソリッドイン セラミド リップエッセンス (5D複合セラミド配合・皮剥け唇を角質層からしっとりほぐす)"},
            {"rank": 4, "query": "CNP プロポリス リップ セラム 15ml", "brand": "CNP Laboratory (シーエヌピー)", "name": "プロポリス リップ セラム (高純度プロポリスエキス配合・寝ている間に濃密なハチミツのうるおいシールド)"},
            {"rank": 5, "query": "タカミリップ 7g TAKAMI", "brand": "TAKAMI (タカミ)", "name": "タカミリップ (美容皮膚発想・唇のターンオーバーと皮脂膜をサポートするエイジングケア美容液)"},
            {"rank": 6, "query": "クラランス コンフォート リップオイル 01 ハニー", "brand": "CLARINS (クラランス)", "name": "コンフォート リップオイル (植物オイルのジュレ・トリートメント効果で縦ジワをふっくら満たす)"},
            {"rank": 7, "query": "ディオール アディクト リップ マキシマイザー セラム 000", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオール アディクト リップ マキシマイザー セラム (マローエキス×ヒアルロン酸・24時間うるおい集中トリートメント)"},
            {"rank": 8, "query": "資生堂 モアリップ 8g 第3類医薬品", "brand": "SHISEIDO (資生堂)", "name": "モアリップN (第3類医薬品・アラントイン×ビタミンE・口唇のひび割れやただれを治す救急リップ)"},
            {"rank": 9, "query": "ジョンマスターオーガニック リップカーム 4g", "brand": "john masters organics (ジョンマスターオーガニック)", "name": "リップカーム (オリーブ果実油×ミツロウ・ひと塗りで長時間うるおいが持続するオーガニックバーム)"},
            {"rank": 10, "query": "ロート製薬 メンソレータム プレミアムメルティクリームリップ", "brand": "メンソレータム (ロート製薬)", "name": "プレミアムメルティクリームリップ (体温でとろけて唇の水分を抱え込むモイストバンク技術・夜用高保湿)"}
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
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    # 価格が0でないものを探す
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]

                    raw_img = ""
                    if chosen.get("mediumImageUrls"):
                        raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    price = chosen.get("itemPrice", 0)
                    aff_url = chosen.get("affiliateUrl", "")
                    shop_name = chosen.get("shopName", "")
                    reviews = chosen.get("reviewCount", 0)
                    rev_avg = chosen.get("reviewAverage", 0.0)
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "search_query": raw_q,
                        "raw_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "formatted_price": f"¥{price:,}",
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": shop_name,
                        "review_count": reviews,
                        "review_average": rev_avg
                    }
                else:
                    # 検索語を少し短くして再試行
                    parts = query.split()
                    if len(parts) > 2:
                        query = " ".join(parts[:2])
                        continue
        except Exception as e:
            print(f"Error on {query_info['name']} (attempt {attempt+1}): {e}")
            time.sleep(1)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "search_query": raw_q,
        "raw_item_name": query_info["name"],
        "price": 0,
        "formatted_price": "¥0",
        "image_url": "",
        "affiliate_url": "",
        "shop_name": "",
        "review_count": 0,
        "review_average": 0.0
    }

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\nFetching items for {cat_key}: {cat_data['title']}...")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"  Rank {item_info['rank']}: {item_info['brand']} {item_info['name']} (Query: {item_info['query']})")
        item_res = fetch_item_with_retry(item_info)
        print(f"    -> Result: {item_res['formatted_price']} | Shop: {item_res['shop_name'][:20]} | Img: {bool(item_res['image_url'])}")
        results[cat_key]["items"].append(item_res)
        time.sleep(0.3)

with open("rakuten_highlighter_hairoil_lipmask_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSuccessfully saved all item data to rakuten_highlighter_hairoil_lipmask_data.json")
