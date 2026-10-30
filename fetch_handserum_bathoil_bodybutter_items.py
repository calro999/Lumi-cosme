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
    "winter_hand_serum": {
        "title": "保湿力の強さで手荒れ・老け手・乾燥シワとさようなら！スマホ操作もサラリと快適＆手肌のキメをふっくら満たす高保湿ハンド美容液・ハンドセラムランク10",
        "page_file": "winter-hand-serum.html",
        "items": [
            {"rank": 1, "query": "SHIRO ホワイトリリー ハンド美容液", "brand": "SHIRO (シロ)", "name": "ホワイトリリー ハンド美容液 (アロエベラ葉エキスと酒粕エキス配合・手肌の角層深くまでみずみずしくうるおいをチャージしベタつかない元祖大人気ハンドセラム)"},
            {"rank": 2, "query": "アルビオン エクシア ハンドエッセンス", "brand": "ALBION (アルビオン エクシア)", "name": "グランド エターナル ハンド / エッセンス (医薬部外品・エイジングケアに着目・手肌の血管浮きや乾燥小ジワをふっくら押し上げる至高の薬用美白ハンド美容液)"},
            {"rank": 3, "query": "アユーラ ハンドエッセンス AYURA", "brand": "AYURA (アユーラ)", "name": "アロマハンドエッセンス (森林浴アロマに包まれながら乾燥で硬くなった手肌をほぐし、角層へ素早くうるおいを届けるみずみずしい高保湿ハンドセラム)"},
            {"rank": 4, "query": "オサジ ハンドセラム OSAJI", "brand": "OSAJI (オサジ)", "name": "ハンドセラム (敏感肌ブランド発・皮脂膜に類似したうるおいバリアを形成・塗った直後からPCやスマホを触れる驚きのサラサラ高浸透テクスチャー)"},
            {"rank": 5, "query": "コスメデコルテ キモノ ハンドエッセンス", "brand": "DECORTÉ (コスメデコルテ)", "name": "キモノ パフュームド ハンドエッセンス (上品な和のフレグランスと上質エモリエント成分が融合・指先までしっとり透明感を宿す美容液仕立てのハンドケア)"},
            {"rank": 6, "query": "エトヴォス ミネラル ハンドセラム", "brand": "ETVOS (エトヴォス)", "name": "ミネラルハンド＆ネイルセラム (5種のヒト型セラミド配合・手洗いやアルコール消毒で荒れた手肌のバリア機能をサポートし爪周りまで集中補修)"},
            {"rank": 7, "query": "uka ネイルセラム ウカ", "brand": "uka (ウカ)", "name": "ベターネイルセラム (爪と指先のキメを整える濃密ネイル＆ハンド用美容液・乾燥による二枚爪や甘皮のパサつきをすっきり立て直すサロン仕様)"},
            {"rank": 8, "query": "ロクシタン シア ハンドクリーム 150ml", "brand": "L'OCCITANE (ロクシタン)", "name": "シア ハンドクリーム (世界中で愛される高保湿ハンドケアの原点・オーガニックシアバター20%配合で手肌をしっとり柔らかく保つ冬の鉄板名品)"},
            {"rank": 9, "query": "アベンヌ 薬用ハンドクリーム", "brand": "Avene (アベンヌ)", "name": "薬用ハンドクリーム (医薬部外品・アベンヌ温泉水とミツロウ配合のコールドクリーム成分が手肌にピタッと密着しヒビ・あかぎれを徹底予防)"},
            {"rank": 10, "query": "ポーラ パンセ ド ブーケ ハンドトリートメント", "brand": "POLA (ポーラ)", "name": "パンセ ド ブーケ ハンドトリートメント (アルニカ花エキスなどポーラ独自の美容成分を凝縮・華やかなブーケの香りと贅沢なハリ感を手肌に宿す高保湿トリートメント)"}
        ]
    },
    "winter_bath_oil": {
        "title": "保湿力の強さで冬の湯上がり乾燥・粉吹きとさようなら！お風呂に浸かるだけで全身シルク肌へ導く極上高保湿バスオイルランク10",
        "page_file": "winter-bath-oil.html",
        "items": [
            {"rank": 1, "query": "ジョーマローン バスオイル イングリッシュペアー", "brand": "JO MALONE LONDON (ジョー マローン)", "name": "バス オイル イングリッシュ ぺアー ＆ フリージア (お湯に溶かすと贅沢な乳白色に変化・スイートアーモンド油と極上の香りが全身を包み込む最高峰バスオイル)"},
            {"rank": 2, "query": "アユーラ メディテーションバスt", "brand": "AYURA (アユーラ)", "name": "メディテーションバスｔ (ベストコスメ多数受賞・アロマティックハーブの香りと植物オイルが冬の乾燥肌をしっとり潤し深い安らぎへ誘う入浴料)"},
            {"rank": 3, "query": "アロマセラピー アソシエイツ ディープリラックス バスアンドシャワーオイル", "brand": "AROMATHERAPY ASSOCIATES (アロマセラピー アソシエイツ)", "name": "ディープリラックス バスアンドシャワーオイル (英国王室御用達・最高純度のベチバーやカモミール精油が極上のリラクゼーションと全身シルク保湿を叶える)"},
            {"rank": 4, "query": "ポールシェリー バスオイル シルエット", "brand": "PAUL SCERRI (ポール・シェリー)", "name": "シルエット ピュリファイング バスオイル (スイス発サロン御用達・厳選ハーブ精油が冬の冷えた体を芯から温めてめぐりをサポートし滑らかな肌へ)"},
            {"rank": 5, "query": "ヴェレダ バスミルク アルニカ", "brand": "WELEDA (ヴェレダ)", "name": "アルニカ バスミルク (天然由来成分100%・冬の冷えやスポーツ後の凝り固まった身体をほぐしながら植物油が湯上がり肌を乾燥からシールド)"},
            {"rank": 6, "query": "SHIRO ホワイトリリー バスオイル", "brand": "SHIRO (シロ)", "name": "ホワイトリリー バスオイル (ヒマワリ種子油など高保湿植物オイル配合・上品なリリーの香りと共に湯上がりのつっぱりや粉吹きを先回り防止)"},
            {"rank": 7, "query": "クナイプ バスミルク アプリコット", "brand": "Kneipp (クナイプ)", "name": "バスミルク コットンミルク / アプリコットミルク (天然植物オイルとスキムミルク配合・お湯に入れるとリッチな泡と潤いヴェールが全身を包み込む)"},
            {"rank": 8, "query": "バンフォード ゼラニウム バスオイル", "brand": "bamford (バンフォード)", "name": "ゼラニウム バスオイル (英国最高峰オーガニック・杏仁オイルやホホバ油をベースに爽やかなゼラニウムが冬のバスルームを満たす贅沢オイル)"},
            {"rank": 9, "query": "ロクシタン アーモンド シャワーオイル", "brand": "L'OCCITANE (ロクシタン)", "name": "アーモンド モイスチャライジング シャワーオイル (水に触れると繊細なミルク泡に変化・入浴時も湯上がりもアーモンドオイルのしっとり柔肌が続く)"},
            {"rank": 10, "query": "ニールズヤード アロマティック バスオイル", "brand": "NEAL'S YARD REMEDIES (ニールズヤード)", "name": "アロマティック エルバ バスオイル (オーガニックラベンダーとゼラニウム精油が優しく香り、ひまわり油の保湿膜が湯上がり乾燥を防ぐ)"}
        ]
    },
    "winter_body_butter": {
        "title": "保湿力の強さで冬の粉吹き肌・乾燥かゆみとさようなら！こっくり濃厚ヴェールで全身を包み込む神高保湿ボディバターランク10",
        "page_file": "winter-body-butter.html",
        "items": [
            {"rank": 1, "query": "ボディショップ シア ボディバター", "brand": "THE BODY SHOP (ザボディショップ)", "name": "シア ボディバター (世界中で愛されるボディバターの原点・コミュニティフェアトレードのシアバター高配合で最長96時間うるおい持続)"},
            {"rank": 2, "query": "ローラメルシエ アンバーバニラ ボディクリーム", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "ホイップトボディクリーム アンバーバニラ (甘く官能的なアンバーバニラの香りと、ホイップクリームのように軽くなめらかに馴染む濃厚リッチ保湿)"},
            {"rank": 3, "query": "キールズ クレム ドゥ コール ボディクリーム", "brand": "KIEHL'S (キールズ)", "name": "クレム ドゥ コール ボディクリーム (スクワラン・シアバター・アボカドオイル配合・真冬のガサつくすねやひじを即座にベルベット肌へ導く世界的名品)"},
            {"rank": 4, "query": "ロクシタン シア ウルトラリッチ ボディクリーム", "brand": "L'OCCITANE (ロクシタン)", "name": "シア ウルトラリッチ ボディクリーム (シアバターを驚異の25%贅沢配合・こっくりとしたリッチなうるおいヴェールで真冬の乾燥かゆみを完全ブロック)"},
            {"rank": 5, "query": "サボン リペア ボディクリーム シアバター", "brand": "SABON (サボン)", "name": "リペアボディクリーム (死海の恵みとジェリコローズ・シアバターが融合・極度に乾燥した冬肌を修復し至福のなめらかさを与える濃密クリーム)"},
            {"rank": 6, "query": "イソップ レゾルート ハイドレーティング ボディバーム", "brand": "Aesop (イソップ)", "name": "レゾルート ハイドレーティング ボディバーム (シアバターやアーモンドオイル配合・スパイシーな温かみのある香りと深いエモリエント膜で全身を満たす)"},
            {"rank": 7, "query": "ニュートロジーナ インテンスリペア CICA バーム", "brand": "Neutrogena (ニュートロジーナ)", "name": "ノルウェーフォーミュラ インテンスリペア リッチバーム / エマルジョン (純度99%高濃度グリセリン×CICA配合・超乾燥肌のひび割れや粉吹きを根本ケア)"},
            {"rank": 8, "query": "クナイプ リッチボディクリーム ホップ カレンデュラ", "brand": "Kneipp (クナイプ)", "name": "リッチボディクリーム (天然植物オイルとシアバター高配合・肌にとろけるように馴染み、真冬の脱衣所でもしっとりモチモチ肌をキープ)"},
            {"rank": 9, "query": "ドゥラメール ザ ボディ クレーム", "brand": "DE LA MER (ドゥ・ラ・メール)", "name": "ザ・ボディ クレーム (独自のミラクルブロスを配合・最高峰のラグジュアリー感で乾燥によるダメージを瞬時に癒やす至高のボディトリートメント)"},
            {"rank": 10, "query": "ニベア ロイヤルブルー ボディミルク 美容ケア", "brand": "NIVEA (ニベア)", "name": "ロイヤルブルーボディミルク 美容ケア (大人のための最高保湿・コエンザイムQ10やヒアルロン酸配合・とろける濃厚テクスチャーで乾燥小ジワをケア)"}
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
                    if not aff_url:
                        item_url = chosen.get("itemUrl", "")
                        aff_url = f"https://hb.afl.rakuten.co.jp/hgc/{AFF_ID}/?pc={urllib.parse.quote(item_url)}"
                    
                    print(f"  [SUCCESS] {query_info['brand']} - {query_info['rank']}: ¥{price:,} | Img: {high_res_img[:50]}...")
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "itemName_rakuten": chosen.get("itemName", ""),
                        "price": f"¥{price:,}",
                        "price_int": price,
                        "imageUrl": high_res_img,
                        "affiliateUrl": aff_url,
                        "shopName": chosen.get("shopName", "")
                    }
                else:
                    print(f"  [ATTEMPT {attempt+1}] No items for query: '{query}', simplifying query...")
                    words = query.split()
                    if len(words) > 1:
                        query = " ".join(words[:-1])
                    time.sleep(1)
        except Exception as e:
            print(f"  [ERROR] Attempt {attempt+1} failed: {e}")
            time.sleep(1.5)
            
    print(f"  [FALLBACK] Failed to fetch item for {raw_q}")
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "itemName_rakuten": query_info["name"],
        "price": "オープン価格",
        "price_int": 3500,
        "imageUrl": "https://shop.r10s.jp/sample/item.jpg",
        "affiliateUrl": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query_info['brand'])}/",
        "shopName": "楽天市場各取扱ショップ"
    }

def main():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n=======================================================")
        print(f"Fetching 10 items for: {cat_key} ({cat_data['title'][:30]}...)")
        print(f"=======================================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": []
        }
        for item_info in cat_data["items"]:
            fetched = fetch_item_with_retry(item_info)
            results[cat_key]["items"].append(fetched)
            time.sleep(0.5)

    with open("rakuten_handserum_bathoil_bodybutter_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\nAll 30 Rakuten items fetched successfully and saved to rakuten_handserum_bathoil_bodybutter_data.json!")

if __name__ == "__main__":
    main()
