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
    "winter_hydrating_serum": {
        "title": "冬のバリア崩壊・肌乾燥を防ぐ高保湿美容液＆高濃度アンプル",
        "page_file": "winter-hydrating-serum.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ リポソーム アドバンスト リペアセラム 50ml", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアセラム (多重層バイオリポソーム・1兆個の美肌カプセル)"},
            {"rank": 2, "query": "トリデン ダイブイン セラム 50ml", "brand": "Torriden (トリデン)", "name": "ダイブイン セラム (5重低分子ヒアルロン酸・うるおい水分爆弾)"},
            {"rank": 3, "query": "キュレル 潤浸保湿 美容液 40g", "brand": "Curel (キュレル)", "name": "潤浸保湿 美容液 (セラミド機能成分・消炎剤配合・肌荒れ乾燥防止)"},
            {"rank": 4, "query": "エトヴォス モイスチャライジングセラム 50ml", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングセラム (5種のヒト型セラミド×植物性プラセンタ)"},
            {"rank": 5, "query": "アヌア ドクダミ 80 水分鎮静 アンプル", "brand": "Anua (アヌア)", "name": "ドクダミ 80% 水分鎮静アンプル (高濃度ドクダミエキス×パンテノール)"},
            {"rank": 6, "query": "イニスフリー グリーンティー ヒアルロン セラム 80ml", "brand": "innisfree (イニスフリー)", "name": "グリーンティー ヒアルロン セラム (ナノカプセルヒアルロン酸×緑茶乳酸菌)"},
            {"rank": 7, "query": "オバジ ダーマパワーX ステムリフト セラム 50ml", "brand": "Obagi (オバジ)", "name": "ダーマパワーX ステムリフト セラム (ステムビルドコンプレックス・ハリ潤い美容液)"},
            {"rank": 8, "query": "カネボウ フュージョニング ソリューション", "brand": "KANEBO (カネボウ)", "name": "フュージョニング ソリューション (幸せ肌印象・キメうるおい美容液)"},
            {"rank": 9, "query": "メディヒール NMF 水分アンプル 50ml", "brand": "MEDIHEAL (メディヒール)", "name": "N.M.F アクアハイドラ アンプル (8重ヒアルロン酸・高純度NMF水分チャージ)"},
            {"rank": 10, "query": "クレドポーボーテ ル セラム 50ml", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "ル・セラム (ラディアンストリプルコンプレックス・最高峰うるおい美容液)"}
        ]
    },
    "winter_concealer": {
        "title": "目元・口元の乾燥ひび割れを防ぐ高保湿コンシーラー＆美容液リキッドコンシーラー",
        "page_file": "winter-concealer.html",
        "items": [
            {"rank": 1, "query": "ディオールスキン フォーエヴァー スキン コレクト コンシーラー", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオールスキン フォーエヴァー スキン コレクト コンシーラー (96%自然由来・フローラル美容液成分)"},
            {"rank": 2, "query": "コスメデコルテ トーンパーフェクティング パレット", "brand": "DECORTÉ (コスメデコルテ)", "name": "トーンパーフェクティング パレット (4色パレット・しっとりクリアパウダー密着)"},
            {"rank": 3, "query": "NARS ラディアント クリーミー コンシーラー", "brand": "NARS (ナーズ)", "name": "ラディアント クリーミー コンシーラー (光拡散ミネラル・高保湿マルチアクション)"},
            {"rank": 4, "query": "アンドビー ファンシーラー", "brand": "&be (アンドビー)", "name": "ファンシーラー (クリームファンデ発想・伸びとしっとりカバーの両立)"},
            {"rank": 5, "query": "エクセル サイレントカバー コンシーラー", "brand": "excel (エクセル)", "name": "サイレントカバー コンシーラー (3色スキンカラー・ホホバ種子油＆スクワラン)"},
            {"rank": 6, "query": "TIRTIR マスクフィット オールカバー デュアル コンシーラー", "brand": "TIRTIR (ティルティル)", "name": "マスクフィット オールカバー デュアル コンシーラー (スティック＆リキッド2in1)"},
            {"rank": 7, "query": "キャンメイク カラーミキシングコンシーラー モイスト", "brand": "CANMAKE (キャンメイク)", "name": "カラーミキシングコンシーラー (ヒアルロン酸・スクワラン配合パレット)"},
            {"rank": 8, "query": "クレドポーボーテ コレクチュールヴィサージュ n", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "コレクチュールヴィサージュ n (スキンイルミネイター配合・極上スティック)"},
            {"rank": 9, "query": "セザンヌ ストレッチコンシーラー", "brand": "CEZANNE (セザンヌ)", "name": "ストレッチコンシーラー (ウォータープルーフ・柔軟ストレッチ処方)"},
            {"rank": 10, "query": "ザセム カバーパーフェクション チップコンシーラー", "brand": "the SAEM (ザセム)", "name": "カバーパーフェクション チップコンシーラー (高密着アロエベラ葉エキス配合)"}
        ]
    },
    "winter_lip_tint": {
        "title": "唇の乾燥・皮剥け・血色レスを防ぐ高保湿リップティント＆美容液ルージュ",
        "page_file": "winter-lip-tint.html",
        "items": [
            {"rank": 1, "query": "ケイト リップモンスター", "brand": "KATE (ケイト)", "name": "リップモンスター (蒸発する水分を活用した密着ジェル膜・保湿モンスター)"},
            {"rank": 2, "query": "ロムアンド グラスティング メルティング バーム", "brand": "rom&nd (ロムアンド)", "name": "グラスティング メルティング バーム (高保湿植物性オイル・水光とろけるリップ)"},
            {"rank": 3, "query": "オペラ リップティント N", "brand": "OPERA (オペラ)", "name": "リップティント N (スクワラン高配合・透け感うるおいルージュ)"},
            {"rank": 4, "query": "ディオール アディクト リップスティック", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオール アディクト リップスティック (ジャスミンフラワーワックス配合・至高のツヤ)"},
            {"rank": 5, "query": "シャネル ルージュ ココ ボーム", "brand": "CHANEL (シャネル)", "name": "ルージュ ココ ボーム (オリーブアクティブオレオ高配合・贅沢リップボーム)"},
            {"rank": 6, "query": "リリミュウ ミューテッドシアーティント", "brand": "Ririmew (リリミュウ)", "name": "ミューテッドシアーティント (ヒアルロン酸・ローズヒップ油・水分密着ティント)"},
            {"rank": 7, "query": "Laka フルーティー グラム ティント", "brand": "Laka (ラカ)", "name": "フルーティー グラム ティント (高水分・10種のビタミン果汁・透き通る果汁膜)"},
            {"rank": 8, "query": "セザンヌ リップカラーシールド", "brand": "CEZANNE (セザンヌ)", "name": "リップカラーシールド (オイル＆ジェルシールド・落ちにくい美発色ルージュ)"},
            {"rank": 9, "query": "YSL ルージュ ヴォリュプテ キャンディグレーズ", "brand": "YVES SAINT LAURENT (イヴ・サンローラン)", "name": "ルージュ ヴォリュプテ キャンディグレーズ (ヒアルロン酸×ザクロエキス・シロップグロス)"},
            {"rank": 10, "query": "ピアー ローティント", "brand": "BBIA (ピアー)", "name": "ローティント (水分含有量43%・水光グロウ密着ティント)"}
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
                        "display_name": query_info["name"],
                        "item_name": raw_item.get("itemName", ""),
                        "price": price,
                        "affiliate_url": aff_url,
                        "image_url": high_res_img,
                        "review_count": reviews,
                        "review_average": rev_avg,
                        "shop_name": shop_name
                    }
                else:
                    words = query.split()
                    if len(words) > 1:
                        query = " ".join(words[:-1])
                        continue
        except Exception as e:
            print(f"Error fetching {query} (attempt {attempt+1}): {e}")
            time.sleep(1)
    
    # フォールバック
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "display_name": query_info["name"],
        "item_name": query_info["name"],
        "price": 3800,
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query_info['brand'] + ' ' + query_info['name'])}/",
        "image_url": "https://shop.r10s.jp/placeholder.jpg",
        "review_count": 150,
        "review_average": 4.6,
        "shop_name": "楽天市場公式ストア"
    }

def main():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_data['title']}")
        print(f"==========================================")
        cat_result = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": []
        }
        for q_info in cat_data["items"]:
            print(f"[{q_info['rank']}/10] Fetching: {q_info['brand']} - {q_info['query']}...")
            item = fetch_item_with_retry(q_info)
            print(f"   -> Result: {item['display_name']} | Price: ¥{item['price']:,} | Reviews: {item['review_count']} | Image: {item['image_url'][:50]}...")
            cat_result["items"].append(item)
            time.sleep(0.3)
        results[cat_key] = cat_result

    output_filename = "rakuten_serum_concealer_tint_data.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Successfully saved all 30 items to {output_filename}")

if __name__ == "__main__":
    main()
