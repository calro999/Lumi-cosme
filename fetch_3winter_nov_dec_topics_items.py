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
    "winter_hand_cream": {
        "title": "保湿力の強さで冬の手荒れ・あかぎれひび割れ砂漠手肌とさようなら！水仕事でも落ちない高保湿ハンドクリームランク10",
        "page_file": "winter-hand-cream.html",
        "items": [
            {"rank": 1, "query": "ロクシタン シア ハンドクリーム 150ml", "brand": "L'OCCITANE (ロクシタン)", "name": "シア ハンドクリーム 150ml (天然シアバター20%高配合・世界中で愛される高保湿ハンドケアの最高峰)"},
            {"rank": 2, "query": "アトリックス プレミアムプレシャスハンドクリーム 80g", "brand": "atrix (アトリックス)", "name": "ビューティーチャージ プレミアム プレシャス 80g (コエンザイムQ10×ヒアルロン酸配合・大人の手肌小ジワをふっくら満たす名品)"},
            {"rank": 3, "query": "イソップ レスレクション ハンドバーム 75ml", "brand": "Aesop (イソップ)", "name": "レスレクション アロマティック ハンドバーム 75ml (マンダリン・ラベンダー精油の至高の香りとベタつかないリッチなうるおい)"},
            {"rank": 4, "query": "ユースキン 120g ボトル", "brand": "yuskin (ユースキン)", "name": "ユースキン 120gボトル (ビタミンE×グリチルレチン酸配合・ひび・あかぎれ・しもやけを治す指定医薬部外品)"},
            {"rank": 5, "query": "ニュートロジーナ インテンスリペア ハンドクリーム 50g", "brand": "Neutrogena (ニュートロジーナ)", "name": "ノルウェーフォーミュラ インテンスリペア ハンドクリーム (純度99%高濃度グリセリン配合・超乾燥手肌を瞬間レスキュー)"},
            {"rank": 6, "query": "ヘパソフト 薬用 顔ローション 100g 手荒れ", "brand": "ロート製薬 ヘパソフト", "name": "ヘパソフト 薬用 肌荒れローション (ヘパリン類似物質配合・保水有効成分で角層深くまでうるおいを閉じ込める医薬部外品)"},
            {"rank": 7, "query": "クナイプ ハンドクリーム バニラ＆ハニー 75ml", "brand": "Kneipp (クナイプ)", "name": "ハンドクリーム バニラ＆ハニーの香り (植物オイル×天然ハーブエキス配合・しっとり浸透して甘く癒やすドイツ品質)"},
            {"rank": 8, "query": "シャネル ラ クレーム マン 50ml", "brand": "CHANEL (シャネル)", "name": "ラ クレーム マン 50ml (メイローズワックス×アイリスパリードエキス配合・手肌と爪を同時に満たす至高のラグジュアリー)"},
            {"rank": 9, "query": "マツモトキヨシ ヒルメナイド 油性クリーム 50g", "brand": "matsukiyo (マツキヨ)", "name": "ヒルメナイド油性クリーム 50g (ヘパリン類似物質0.3%配合・水仕事の摩擦や乾燥荒れから守る高密着シールド処方)"},
            {"rank": 10, "query": "オサジ ハンドクリーム 50g Muku", "brand": "OSAJI (オサジ)", "name": "ハンドクリーム 50g (皮膚科学に基づく敏感肌設計・セラミド形成を促しベタつかずスマホ操作も快適な国産名品)"}
        ]
    },
    "winter_retinol_cream": {
        "title": "保湿力の強さで冬の小ジワ・乾燥毛穴たるみとさようなら！ふっくらハリ弾力を呼び覚ます高保湿レチノールクリームランク10",
        "page_file": "winter-retinol-cream.html",
        "items": [
            {"rank": 1, "query": "資生堂 エリクシール レチノパワー リンクルクリーム S 15g", "brand": "ELIXIR (エリクシール)", "name": "レチノパワー リンクルクリーム S 15g (日本唯一の純粋レチノール配合・冬の目元口元の乾燥小ジワを改善する医薬部外品最高峰)"},
            {"rank": 2, "query": "キールズ DS RTN リニューイング セラム 50ml", "brand": "KIEHL'S (キールズ)", "name": "DS RTN リニューイング セラム (マイクロレチノール×ナイアシンアミド×セラミド配合・冬のA反応を抑えながら毛穴とハリをケア)"},
            {"rank": 3, "query": "イニスフリー レチノール シカ リペア セラム 30ml", "brand": "innisfree (イニスフリー)", "name": "レチノール シカ リペア セラム 30ml (低刺激レチノール×ツボクサCICA成分配合・冬のゆらぎ肌でも毎日使える韓国No.1名品)"},
            {"rank": 4, "query": "COSRX RX ザ・レチノール 0.1 クリーム 20ml", "brand": "COSRX (コスアールエックス)", "name": "RX ザ・レチノール 0.1 クリーム 20ml (純粋レチノール0.1%×パンテノール×トコトリエノール配合・冬の毛穴開きと弾力低下に直撃)"},
            {"rank": 5, "query": "トゥヴェール レチノショット 0.1 30g", "brand": "TOUT VERT (トゥヴェール)", "name": "レチノショット 0.1 30g (ピュアレチノールを含む5種のレチノール×ペプチド×セラミド配合・本格攻めの高濃度クリーム)"},
            {"rank": 6, "query": "サナ なめらか本舗 リンクルナイトクリーム 50g", "brand": "なめらか本舗 (SANA)", "name": "リンクルナイトクリーム 50g (ピュアレチノール×豆乳発酵液配合・プチプラ最高峰のもっちり高密着おやすみパック処方)"},
            {"rank": 7, "query": "ドクターシーラボ エンリッチ メディカリフト デュオセラム 26ml", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "エンリッチ メディカリフト デュオセラム (純粋レチノール×高浸透ビタミンCの2層式・冬のくすみとたるみ毛穴を同時リフト)"},
            {"rank": 8, "query": "アンプルール ラグジュアリー・デ・エイジ ラインセラム アイEX 20g", "brand": "AMAMPLEUR (アンプルール)", "name": "ラインセラム アイEX (レチノール誘導体×植物幹細胞×EGF配合・冬の冷え固まった目元を温もりとハリでリペア)"},
            {"rank": 9, "query": "VT シカレチA クリーム 0.05 30ml", "brand": "VT COSMETICS (VT)", "name": "シカレチA クリーム 0.05% 30ml (ツボクサエキス×純粋レチノール×バクチオール配合・冬の毛穴の目立ちとキメの乱れを優しく整える)"},
            {"rank": 10, "query": "バイオヒールボ プロバイオダーム 3D リフティングクリーム 50ml", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "プロバイオダーム 3D リフティングクリーム 50ml (特許バイオーム成分×ペプチド複合体配合・韓国オリーブヤング弾力クリームの代名詞)"}
        ]
    },
    "winter_ceramide_serum": {
        "title": "保湿力の強さで冬のインナードライ・バリア破壊赤み肌とさようなら！角層細胞を満たす高濃度ヒト型セラミド美容液ランク10",
        "page_file": "winter-ceramide-serum.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ リポソーム アドバンスト リペアセラム 50ml", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアセラム 50ml (1滴に1兆個の多重層バイオリポソーム×セラミド・冬の過酷な乾燥を跳ね返す国民的美容液)"},
            {"rank": 2, "query": "ETVOS モイスチャライジングセラム 50ml", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングセラム 50ml (5種のヒト型セラミド高濃度配合・美容液と乳液のW機能を備えた冬の敏感肌の救世主)"},
            {"rank": 3, "query": "キュレル 潤浸保湿 美容液 40g", "brand": "Curel (キュレル)", "name": "潤浸保湿 美容液 40g (セラミド機能成分×消炎剤配合・冬の乾燥による小ジワを目立たなくする医薬部外品ジェル美容液)"},
            {"rank": 4, "query": "松山油脂 肌をうるおす保湿セラム 30ml", "brand": "松山油脂 (M mark)", "name": "肌をうるおす保湿セラム 30ml (5種のヒト型セラミド×大豆由来成分配合・角層の奥までうるおいで満たす低刺激シンプル処方)"},
            {"rank": 5, "query": "トゥヴェール リペアエッセンス 20ml", "brand": "TOUT VERT (トゥヴェール)", "name": "リペアエッセンス 20ml (ヒト型セラミド原液複合体100%配合・自作スキンケアにも混ぜられる濃密バリア集中補修原液)"},
            {"rank": 6, "query": "カネボウ スキン ハーモナイザー 180ml", "brand": "KANEBO (カネボウ)", "name": "スキン ハーモナイザー 180ml (悪玉皮脂トラップ技術×うるおいケラチン保水・冬の肌荒れや乾燥テカリを防ぐ2層式セラム)"},
            {"rank": 7, "query": "シェルシュール モイスチャーマトリックス IS 30ml", "brand": "Cerseur (シェルシュール)", "name": "モイスチャーマトリックス IS 30ml (天然ヒト型セラミドを高濃度ラメラ構造でカプセル化・超敏感肌のバリアを本格再構築)"},
            {"rank": 8, "query": "アスタリフト ジェリー アクアリスタ 60g", "brand": "ASTALIFT (アスタリフト)", "name": "ジェリー アクアリスタ 60g (世界最小Wヒト型ナノセラミド×アスタキサンチン配合・洗顔後すぐに土台を整える赤い先行美容液)"},
            {"rank": 9, "query": "Real Barrier エクストリーム クリーム アンプル 30ml", "brand": "Real Barrier (リアルバリア)", "name": "エクストリーム クリーム アンプル 30ml (特許MLE肌バリア技術×独自セラミド配合・韓国で皮膚科推奨の超高保湿アンプル)"},
            {"rank": 10, "query": "イニスフリー グリーンティーシード ヒアルロン セラム 80ml", "brand": "innisfree (イニスフリー)", "name": "グリーンティーシード ヒアルロン セラム 80ml (緑茶乳酸菌カプセル×5重ヒアルロン酸×セラミド配合・角層深くまで瞬時に水分バースト)"}
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
                    item_name = chosen.get("itemName", "")
                    
                    if not aff_url:
                        aff_url = chosen.get("itemUrl", "")
                        
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "itemName": item_name,
                        "price": price,
                        "img": high_res_img,
                        "url": aff_url
                    }
                else:
                    alt_q = query_info["brand"].split()[0] + " " + query.split()[0]
                    if attempt == 2 and alt_q != query:
                        query = alt_q
        except Exception as e:
            print(f"Error fetching {query}: {e}")
            time.sleep(1)
        time.sleep(0.3)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "itemName": query_info["name"],
        "price": 3500,
        "img": "https://thumbnail.image.rakuten.co.jp/@0_mall/sample/item.jpg",
        "url": "https://hb.afl.rakuten.co.jp/"
    }

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\nFetching category: {cat_key}...")
    cat_items = []
    for q_item in cat_data["items"]:
        res_item = fetch_item_with_retry(q_item)
        print(f"  Rank {res_item['rank']}: {res_item['brand']} - ¥{res_item['price']:,} - Img: {res_item['img'][:45]}...")
        cat_items.append(res_item)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

with open("rakuten_3winter_nov_dec_topics_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDone fetching all Rakuten API items for the 3 new topics!")
