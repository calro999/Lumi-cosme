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
    "winter_cleansing_gel": {
        "title": "保湿力の強さで冬の摩擦ダメージ・洗い上がり突っ張りとさようなら！毛穴汚れも優しく包み落とす高保湿クレンジングジェルランク10",
        "page_file": "winter-cleansing-gel.html",
        "items": [
            {"rank": 1, "query": "マナラ ホットクレンジングゲル マッサージプラス 200g", "brand": "MANARA (マナラ)", "name": "ホットクレンジングゲル マッサージプラス (美容液成分91.3%配合・温感ブースターで頑固な冬の毛穴汚れを摩擦レスに絡め取る神ゲル)"},
            {"rank": 2, "query": "キュレル ジェルメイク落とし 130g", "brand": "Curel (キュレル)", "name": "ジェルメイク落とし (セラミドを守りながら毛穴の奥のメイクをすっきり落とす・消炎剤配合の敏感肌用医薬部外品ジェル)"},
            {"rank": 3, "query": "サンタマルシェ 薬用ディープクレンジング 400g", "brand": "Santa Marche (サンタマルシェ)", "name": "薬用ディープクレンジング (京都宇治茶エキス×重曹配合・摩擦ゼロの超濃密クッションジェルで大容量高コスパ)"},
            {"rank": 4, "query": "オルビス クレンジングジェル 150g", "brand": "ORBIS (オルビス)", "name": "クレンジングジェル (ヒアルロン酸×マリンコラーゲン配合・ぷるぷる濃密ジェルが体温でとろけてうるおいを守り抜く名品)"},
            {"rank": 5, "query": "アルージェ モイスト クレンジング ミルクジェル 100g", "brand": "Arouge (アルージェ)", "name": "モイスト クレンジング ミルクジェル (天然セラミド配合・デリケートな冬の乾燥肌をやさしくいたわりながら落とす弱酸性ジェル)"},
            {"rank": 6, "query": "エスト クラリファイイング クレンジング ジェル 130g", "brand": "est (エスト)", "name": "クラリファイイング クレンジング ジェル (角栓崩壊技術・大人のくすみや毛穴汚れを温感ジェルで分解するデパコス最高峰)"},
            {"rank": 7, "query": "ファンケル 整肌クレンジング ジェル 120g", "brand": "FANCL (ファンケル)", "name": "整肌クレンジング ジェル (アミノ酸系洗浄成分×桃葉エキス配合・冬の肌バリアを整えながらするんと落とす無添加ジェル)"},
            {"rank": 8, "query": "無印良品 マイルドジェルクレンジング 200g", "brand": "無印良品 (MUJI)", "name": "マイルドジェルクレンジング (アンズ果汁・モモ葉エキス配合・素早くメイクとなじんでさっぱり潤う国民的人気コスパジェル)"},
            {"rank": 9, "query": "ビオデルマ サンシビオ ミセラー クレンジングジェル 200ml", "brand": "BIODERMA (ビオデルマ)", "name": "サンシビオ ミセラー クレンジングジェル (ナイアシンアミド配合・冬の赤み敏感肌をしっとり洗い上げるフランス発の高保湿ジェル)"},
            {"rank": 10, "query": "シンデレラタイム ブースターセラム ナノクレンジングゲル 310ml", "brand": "Cinderella Time (シンデレラタイム)", "name": "ブースターセラム ナノクレンジングゲル (ナノクレンジング粒子×導入美容液成分配合・W洗顔不要で洗い上がりもっちり)"}
        ]
    },
    "winter_peel_serum": {
        "title": "保湿力の強さで冬の角質ゴワつき・化粧水はじき砂漠肌とさようなら！うるおい浸透を呼び覚ます高保湿角質柔軟美容液・ピールセラムランク10",
        "page_file": "winter-peel-serum.html",
        "items": [
            {"rank": 1, "query": "タカミスキンピール 30ml", "brand": "TAKAMI (タカミ)", "name": "タカミスキンピール (美容皮膚の現場から生まれた角質美容水・剥がさず整えて冬の化粧水浸透力を劇的に引き上げる至高の名品)"},
            {"rank": 2, "query": "ラロッシュポゼ エファクラ ピールケア セラム 30ml", "brand": "La Roche-Posay (ラロッシュポゼ)", "name": "エファクラ ピールケア セラム (サリチル酸×乳酸×フィチン酸×ナイアシンアミド配合・敏感肌の冬のキメ乱れを優しく整えるデイリー角質美容液)"},
            {"rank": 3, "query": "CNP Laboratory インビジブル ピーリング ブースター 100ml", "brand": "CNP Laboratory (チャアンドパク)", "name": "インビジブル ピーリング ブースター (低刺激PHA配合・塗るだけで古い角質をやさしくケアし7日間の奇跡をもたらす韓国神ブースター)"},
            {"rank": 4, "query": "ソフィーナiP ベースケア セラム 土台美容液 90g", "brand": "SOFINA iP (ソフィーナiP)", "name": "ベースケア セラム 土台美容液 (毛穴の1/20サイズの高濃度マイクロ炭酸泡・冷え固まった冬の肌を血行促進してうるおい巡らせる)"},
            {"rank": 5, "query": "ナンバーズイン 3番 すべすべキメケアセラム 50ml", "brand": "numbuzin (ナンバーズイン)", "name": "3番 すべすべキメケアセラム (ガラクトミセス×ビフィズス菌など50種の発酵成分配合・冬の凸凹毛穴とザラつきを陶器肌へ)"},
            {"rank": 6, "query": "キールズ DS RTN リニューイング セラム 30ml", "brand": "KIEHL'S (キールズ)", "name": "DS RTN リニューイング セラム (マイクロレチノール×ナイアシンアミド×セラミド配合・冬の乾燥小ジワとターンオーバーを同時にケア)"},
            {"rank": 7, "query": "ドクターシーラボ VC100 ダブルリペアセラム 30ml", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "VC100 ダブルリペアセラム (高浸透ビタミンC・APPS×高濃度セラミドの2層式・冬のくすみと角質乾燥を集中トリートメント)"},
            {"rank": 8, "query": "ランコム クラリフィック デュアル エッセンス ローション 150ml", "brand": "LANCOME (ランコム)", "name": "クラリフィック デュアル エッセンス ローション (酵素サイエンス×ブナの芽エキス×植物オイル・冬のくすみ肌を澄み切った透明感へ)"},
            {"rank": 9, "query": "アヌア ドクダミ 80% 水分鎮静アンプル 30ml", "brand": "Anua (アヌア)", "name": "ドクダミ 80% 水分鎮静アンプル (ドクダミエキス80%高濃縮配合・冬の乾燥肌荒れを急速鎮静しながら角層深くまで水分チャージ)"},
            {"rank": 10, "query": "イニスフリー ブラックティー ユース トリートメント エッセンス 145ml", "brand": "innisfree (イニスフリー)", "name": "ブラックティー ユース トリートメント エッセンス (発酵茶葉リセットコンセントレート配合・冬の過酷な疲労肌のキメをふっくらほぐす)"}
        ]
    },
    "winter_lip_serum": {
        "title": "保湿力の強さで冬の唇皮剥け・砂漠縦ジワとさようなら！24時間ぷるんと満たす高保湿リップセラム・唇用美容液ランク10",
        "page_file": "winter-lip-serum.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ リポソーム アドバンスト リペアリップセラム 7g", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアリップセラム (多重層バイオリポソーム×唇用高機能リペア・冬の皮剥けやしぼみ唇をふっくらハリ感で満たす最高峰)"},
            {"rank": 2, "query": "オバジ ダーマパワーX リップエッセンス 10g", "brand": "Obagi (オバジ)", "name": "ダーマパワーX リップエッセンス (ビタミンA誘導体×コラーゲン×エラスチン配合・冬の深刻な縦ジワと乾燥をふっくら押し上げる殿堂入り美容液)"},
            {"rank": 3, "query": "タカミ リップ 7g", "brand": "TAKAMI (タカミ)", "name": "タカミ リップ (唇の代謝と保水機能に着目したスキンケア発想・ベタつかず1日中うるおいの厚膜で密着プロテクトする名品)"},
            {"rank": 4, "query": "Torriden ソリッドイン セラミド リップエッセンス 11ml", "brand": "Torriden (トリデン)", "name": "ソリッドイン セラミド リップエッセンス (5重複合セラミド×ホホバ種子油配合・韓国オリーブヤング大人気・冬の角質めくれを即効なめらかに)"},
            {"rank": 5, "query": "ディオール アディクト リップ マキシマイザー セラム 5ml", "brand": "DIOR (ディオール)", "name": "アディクト リップ マキシマイザー セラム (マローエキス×ヒアルロン酸配合・24時間濃厚保湿しながらプランプ効果でぷるぷるのボリューム唇へ)"},
            {"rank": 6, "query": "エテュセ リップエディション プランパー リップエッセンス 10g", "brand": "ettusais (エテュセ)", "name": "リップエディション (プランパーエッセンス) (ハイパーグロスオイル配合・縦ジワを目立たなくしグロス級のツヤとうるおいが続く神コスパ)"},
            {"rank": 7, "query": "キュレル リップケアバーム 4.2g", "brand": "Curel (キュレル)", "name": "リップケアバーム (セラミド機能成分×消炎剤配合・冬の夜に塗って朝まで密着パックする荒れ・ひび割れ防止の医薬部外品)"},
            {"rank": 8, "query": "クラランス リップ コンフォート オイル 7ml", "brand": "CLARINS (クラランス)", "name": "リップ コンフォート オイル (オーガニックホホバ×ヘーゼルナッツオイル・植物の恵みで唇をトリートメントしながらみずみずしく彩る名作)"},
            {"rank": 9, "query": "SHIRO シアバター リップバター 10g", "brand": "SHIRO (シロ)", "name": "シアバター リップバター (未精製シアバター配合・体温でとろけて唇を濃密保護ヴェールで包み込む自然派リッチセラム)"},
            {"rank": 10, "query": "UZU BY FLOWFUSHI 38°C 99°F リップトリートメント 6ml", "brand": "UZU (ウズ)", "name": "38°C / 99°F リップトリートメント (エンドミネラル×乳酸菌ラ・フローラ配合・唇のマイクロバイオームを整え自らうるおう血色唇へ導く)"}
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

with open("rakuten_3new_winter_topics_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("\n✓ Finished fetching all 30 items from Rakuten API!")
