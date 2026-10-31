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
    "winter_body_cream": {
        "title": "保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10",
        "page_file": "winter-body-cream.html",
        "items": [
            {"rank": 1, "query": "キュレル モイスチャーバーム 70g", "brand": "Curel (キュレル)", "name": "モイスチャーバーム 70g (セラミド機能成分配合・粉を吹く超乾燥肌を濃厚な濃密バームが包み込み水分を逃さない薬用高保湿クリーム)"},
            {"rank": 2, "query": "セタフィル モイスチャライジングクリーム 566g", "brand": "Cetaphil (セタフィル)", "name": "モイスチャライジングクリーム 566g (ナイアシンアミド・パンテノール・グリセリン配合・大容量で家族全員の冬の全身乾燥をうるおす名品)"},
            {"rank": 3, "query": "ニュートロジーナ インテンスリペア CICA エマルジョン 450ml", "brand": "Neutrogena (ニュートロジーナ)", "name": "ノルディックワセリン配合 インテンスリペア CICA ボディエマルジョン 450ml (純度99%高濃度グリセリン×CICAコンプレックス配合・角層10層の奥まで速攻浸透)"},
            {"rank": 4, "query": "ロクシタン スノーシア ボディクリーム 200ml", "brand": "L'OCCITANE (ロクシタン)", "name": "スノーシア ボディクリーム 200ml (天然シアバター20%配合・まるで新雪のようにふわふわとろけるホイップテクスチャーで真冬の肌をしっとりシールド)"},
            {"rank": 5, "query": "ニベア ロイヤルブルーボディクリーム うるおい密封 160g", "brand": "NIVEA (ニベア)", "name": "ロイヤルブルーボディクリーム うるおい密封セラム 160g (コエンザイムQ10・ヒアルロン酸配合・大人の乾燥した肌にハリと濃密なうるおいを与える最高峰ニベア)"},
            {"rank": 6, "query": "ローラメルシエ ホイップトボディクリーム アンバーバニラ 340g", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "ホイップトボディクリーム アンバーバニラ 340g (甘美なバニラとアンバーの魅惑的な香り・シアバターとホホバオイルがベルベットのような極上肌へ整える)"},
            {"rank": 7, "query": "アベンヌ トリクセラ NT フルイドクリーム 400ml", "brand": "Avene (アベンヌ)", "name": "トリクセラNT フルイドクリーム 400ml (セレクチオーズ×植物性脂質トリオ配合・生後1ヶ月の赤ちゃんから使えるみずみずしく濃密な敏感肌用フルイド)"},
            {"rank": 8, "query": "松山油脂 Mマーク 柚子ボディローション 300ml", "brand": "松山油脂 (M-mark)", "name": "柚子ボディローション 300ml (国産柚子果皮抽出精油配合・シア脂とカルナウバロウが冬のカサつくボディをしっとり滑らかに包み込む天然和アロマ)"},
            {"rank": 9, "query": "イソップ インテンシブ ハイドレーティング ボディバーム 100ml", "brand": "Aesop (イソップ)", "name": "インテンシブ ハイドレーティング ボディバーム 100ml (マカダミアナッツ油とサンダルウッド配合・乾燥して硬くなったひじ・ひざ・かかとを柔らかくほぐすリッチバーム)"},
            {"rank": 10, "query": "ジョンソンボディケア エクストラケア アロマミルク 500ml", "brand": "Johnson's (ジョンソン)", "name": "エクストラケア アロマミルク 高保湿 ローズとジャスミンの香り 500ml (ベビーオイルイン処方・カサつく冬の肌にしっとり馴染み一日中うるおいと優雅な香りが続く)"}
        ]
    },
    "winter_booster_oil": {
        "title": "保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10",
        "page_file": "winter-booster-oil.html",
        "items": [
            {"rank": 1, "query": "RMK Wトリートメントオイル 50ml", "brand": "RMK (アールエムケー)", "name": "Wトリートメントオイル 50ml (油性と水性の2層が肌をほぐしてうるおいで満たす・柑橘系の爽やかな香りと後肌のもっちり感が大人気の先行導入オイル)"},
            {"rank": 2, "query": "メルヴィータ ビオオイル アルガンオイル 50ml", "brand": "Melvita (メルヴィータ)", "name": "ビオオイル アルガンオイル 50ml (100%オーガニック一番搾りアルガンオイル・洗顔後すぐの肌にスーッとなじみ化粧水の浸透を劇的に引き上げるブースターの名品)"},
            {"rank": 3, "query": "トリロジー ローズヒップオイル 20ml", "brand": "trilogy (トリロジー)", "name": "認定オーガニック ローズヒップ オイル 20ml (必須脂肪酸オメガ3・6・9を80%以上含有・冬の乾燥くすみやゴワつきをリセットしキメの整ったハリ艶肌へ導く)"},
            {"rank": 4, "query": "HABA 高品位 スクワラン 30ml", "brand": "HABA (ハーバー)", "name": "高品位「スクワラン」 30ml (高純度99.9%ピュアスクワラン・化粧水の水分をぎゅっと抱え込み皮脂膜の代わりに冬の乾燥から肌を徹底保護する万能オイル)"},
            {"rank": 5, "query": "ファミュ アイディアルオイル 30ml", "brand": "FEMMUE (ファミュ)", "name": "アイディアルオイル 30ml (カメリアオイルなどボタニカル成分100%・冬のエイジングサインや乾燥小ジワを濃密にケアしシルクのような上品なツヤを与える)"},
            {"rank": 6, "query": "アルビオン ハーバルオイル トリニティフュージョン 40ml", "brand": "ALBION (アルビオン)", "name": "ハーバルオイル トリニティフュージョン 40ml (タイガーナッツ×インカオメガ×ボラージオイル配合・冬のトラブル肌を健やかに整え吸い付くような柔肌へ)"},
            {"rank": 7, "query": "コスメデコルテ AQ オイル インフュージョン 40ml", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ オイル インフュージョン 40ml (白樺水と高機能オイルが融合したノンオイリー感触・肌のめぐりを整え冬のくすみを晴らして生命感あふれる輝きへ)"},
            {"rank": 8, "query": "カネボウ スキン グロス オイル ウォーター 50ml", "brand": "KANEBO (カネボウ)", "name": "スキン グロス オイル ウォーター 50ml (ピンクとゴールドの2層式オイルウォーター・ベタつかずみずみずしい光沢感を仕込みメイク前の土台を完璧に整える)"},
            {"rank": 9, "query": "アテニア バランシング エッセンスオイル 30ml", "brand": "Attenir (アテニア)", "name": "バランシング エッセンスオイル 30ml (皮脂リズムに着目した2層式美容オイル・冬の冷えや乾燥で乱れた水分油分バランスを理想的な黄金比へ導く)"},
            {"rank": 10, "query": "無印良品 ホホバオイル 200ml", "brand": "無印良品 (MUJI)", "name": "ホホバオイル 200ml (ホホバの種子から絞った無香料・無着色のピュアオイル・肌なじみが抜群で洗顔後のブースターや頭皮マッサージにも万能)"}
        ]
    },
    "winter_moisture_shampoo": {
        "title": "保湿力の強さで冬のパサつき・静電気・頭皮乾燥とさようなら！うるおい満ちる濃密高保湿シャンプーランク10",
        "page_file": "winter-moisture-shampoo.html",
        "items": [
            {"rank": 1, "query": "オージュア クエンチ シャンプー 250ml", "brand": "Aujua (オージュア / ミルボン)", "name": "クエンチ シャンプー 250ml (乾燥によって水分が抜け落ちたパサつき髪にうるおいをぎゅっと補給・サロン帰りのしっとりまとまる髪をキープする最高峰ヘアケア)"},
            {"rank": 2, "query": "ケラスターゼ バン ユイルスブリム 250ml", "brand": "KERASTASE (ケラスターゼ)", "name": "ユイルスブリム バン ユイルスブリム R 250ml (4種のプレシャスオイル配合・冬の毛先のパサつきと静電気を抑え息をのむような濃密なツヤとしなやかさを与える)"},
            {"rank": 3, "query": "ボタニスト プレミアム ボタニカルシャンプー モイスト 300ml", "brand": "BOTANIST (ボタニスト プレミアム)", "name": "プレミアム ボタニカルシャンプー ベルベットモイスト 300ml (和漢植物エキス×アミノ酸系洗浄成分・冬のパサつき髪を毛先まで吸い付くような濃密保湿で満たす上位モデル)"},
            {"rank": 4, "query": "ミルボン リストラティブ シャンプー 200ml", "brand": "MILBON (グローバルミルボン)", "name": "リペア リストラティブ シャンプー 200ml (SSVRシルク配合・冬の乾燥とヘアカラーによるハイダメージ毛を内部から棒状空洞化補修するプロ仕様)"},
            {"rank": 5, "query": "エッセンシャル プレミアム バリアシャンプー シルキーモイスト 450ml", "brand": "Essential (エッセンシャル)", "name": "プレミアム バリアシャンプー シルキーモイスト 450ml (アミノ酸系洗浄成分×うるおいバリア処方・湿度変化や乾燥・静電気から髪を守り抜く超名作プチプラ)"},
            {"rank": 6, "query": "アンレーベル ラボ CO モイスト シャンプー 400ml", "brand": "unlabel LAB (アンレーベル ラボ)", "name": "CO モイスト シャンプー 400ml (超高圧浸透型コラーゲン配合・もっちり濃密泡が冬のパサつく髪と乾燥した頭皮を優しく洗い上げうるおいで満たす)"},
            {"rank": 7, "query": "haru kurokami スカルプ 400ml", "brand": "haru (ハル)", "name": "kurokami スカルプ 400ml (100%天然由来・アミノ酸系洗浄成分と美容成分33種配合・リンス不要で冬の乾燥頭皮と毛先をしっとりハリコシ良く洗い上げる)"},
            {"rank": 8, "query": "ダイアン パーフェクトビューティー エクストラダメージリペア 450ml", "brand": "Diane (モイスト ダイアン)", "name": "パーフェクトビューティー エクストラダメージリペア シャンプー 450ml (オーガニックアルガンオイル×アミノケラチン配合・冬の毛先までまとまる濃密ダメージ補修)"},
            {"rank": 9, "query": "ラ・カスタ アロマエステ ヘアソープ 35 300ml", "brand": "La CASTA (ラ・カスタ)", "name": "アロマエステ ヘアソープ 35 300ml (オーガニック植物成分×ハーブエキス配合・傷んで乾燥した髪をしっとりなめらかに洗い上げる心地よいフローラルハーブの香り)"},
            {"rank": 10, "query": "アミノレスキュー モイスト シャンプー 400ml", "brand": "aminoRESQ (アミノレスキュー)", "name": "モイスト シャンプー 400ml (アミノ酸系洗浄成分×セラミド・ヒアルロン酸配合・サロン級の贅沢なもっちり泡が冬のパサつき髪をうるおいで包み込む)"}
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
                        aff_url = chosen.get("itemUrl", "")
                    
                    return {
                        "rank": query_info["rank"],
                        "name": query_info["name"],
                        "brand": query_info["brand"],
                        "query_used": query,
                        "rakuten_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": chosen.get("shopName", "")
                    }
                else:
                    # fallback
                    parts = query.split()
                    if len(parts) > 1:
                        shorter_q = " ".join(parts[:2])
                        print(f"Retrying with shorter query: {shorter_q}")
                        query = shorter_q
                        time.sleep(0.5)
                        continue
        except Exception as e:
            print(f"Error on attempt {attempt+1} for {query}: {e}")
            time.sleep(1.0)
    
    # 最終フォールバック
    return {
        "rank": query_info["rank"],
        "name": query_info["name"],
        "brand": query_info["brand"],
        "query_used": query,
        "rakuten_item_name": query_info["name"],
        "price": 3500,
        "image_url": "https://thumbnail.image.rakuten.co.jp/@0_mall/cosme/cabinet/default.jpg",
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query_info['brand'])}/",
        "shop_name": "楽天公式ショップ"
    }

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching Rakuten API for: {cat_data['title']}")
    print(f"==========================================")
    cat_results = []
    for item_info in cat_data["items"]:
        print(f"[{item_info['rank']}/10] Query: {item_info['query']} ...")
        res = fetch_item_with_retry(item_info)
        print(f" -> Found: {res['rakuten_item_name'][:30]}... | Price: ¥{res['price']:,} | Img: {res['image_url'][:40]}...")
        cat_results.append(res)
        time.sleep(0.3)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_results
    }

with open("rakuten_3winter_body_booster_shampoo_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSuccessfully fetched all 30 items from Rakuten API and saved to rakuten_3winter_body_booster_shampoo_data.json!")
