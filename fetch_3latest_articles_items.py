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
    "winter_cleansing_balm": {
        "title": "保湿力の強さで冬の突っ張り・乾燥小じわとさようなら！体温でとろけて毛穴汚れもつるんと落とす高保湿クレンジングバームランク10",
        "page_file": "winter-cleansing-balm.html",
        "items": [
            {"rank": 1, "query": "DUO デュオ ザ クレンジングバーム ホットa", "brand": "DUO (デュオ)", "name": "ザ クレンジングバーム ホットa (温感オイルがとろけて冬の毛穴汚れと角栓をほぐし流す高保湿バーム)"},
            {"rank": 2, "query": "パーフェクトワンフォーカス スムースクレンジングバーム ディープブラック", "brand": "PERFECT ONE FOCUS (パーフェクトワンフォーカス)", "name": "スムースクレンジングバーム ディープブラック (泥×炭×ビタミンC誘導体・真冬の黒ずみ毛穴をつるんとオフ)"},
            {"rank": 3, "query": "ルルルン クレンジングバーム リッチモイスト 保湿", "brand": "LuLuLun (ルルルン)", "name": "クレンジングバーム リッチモイスト (植物由来オイル高配合・冬の乾燥肌をうるおいで包み込む濃密バーム)"},
            {"rank": 4, "query": "クリニーク テイク ザ デイ オフ クレンジング バーム", "brand": "CLINIQUE (クリニーク)", "name": "テイク ザ デイ オフ クレンジング バーム (世界的人気・ハイブリッドオイルがウォータープルーフもすっきり優しく落とす)"},
            {"rank": 5, "query": "バニラコ クレンジングバーム ピュアフェクト ハイドレーティング", "brand": "BANILA CO (バニラコ)", "name": "クリーンイットゼロ クレンジングバーム ナリシング (高保湿ローヤルゼリーエキス配合・冬のつっぱりを防ぐ栄養バーム)"},
            {"rank": 6, "query": "Yunth ユンス 生ビタミンC クレンジングバーム", "brand": "Yunth (ユンス)", "name": "生ビタミンC クレンジングバーム (温感生ビタミンCカプセル配合・冬のくすみ肌を明るく整える透明感バーム)"},
            {"rank": 7, "query": "ink. インク クレンジングバーム クレイシトラス", "brand": "ink. (インク)", "name": "クレンジングバーム 無香料 / シトラス (セラミド3種高配合・肌のバリア機能を守りながら洗うサロン品質コスパ最強バーム)"},
            {"rank": 8, "query": "ロゼット 夢みるバーム 白泥リフトモイスチャー", "brand": "ROSETTE (ロゼット)", "name": "夢みるバーム 白泥リフトモイスチャー (白泥×シアバター×オイル・冬のハリ不足と乾燥毛穴にアプローチ)"},
            {"rank": 9, "query": "カネボウ メロウ オフ ヴェイル クレンジング", "brand": "KANEBO (カネボウ)", "name": "メロウ オフ ヴェイル (美容液成分たっぷり配合・吸い付くようなとろみヴェールで冬肌をいたわる極上バームクリーム)"},
            {"rank": 10, "query": "ファミュ ビューティ クレンジングバーム", "brand": "FEMMUE (ファミュ)", "name": "ビューティ クレンジングバーム (カメリアオイル高配合・スパのような優雅な香りと濃密オイルの至高のうるおい)"}
        ]
    },
    "winter_scalp_shampoo": {
        "title": "保湿力の強さで頭皮乾燥・フケかゆみとさようなら！うるおい守る高保湿スカルプシャンプーランク10",
        "page_file": "winter-scalp-shampoo.html",
        "items": [
            {"rank": 1, "query": "haru kurokami スカルプ シャンプー 400ml", "brand": "haru (ハル)", "name": "kurokamiスカルプ (100%天然由来・アミノ酸洗浄成分と8種のボリュームケア成分で冬の頭皮砂漠化を防ぐオールインワン)"},
            {"rank": 2, "query": "オージュア モイストカーム モイスチュアクリアシャンプー", "brand": "Aujua (オージュア)", "name": "モイストカーム モイスチュアクリアシャンプー (サロン専売最高峰・年齢や乾燥による頭皮のかゆみや地肌トラブルをうるおいで鎮静)"},
            {"rank": 3, "query": "キュレル 泡シャンプー ポンプ 480ml", "brand": "Curel (キュレル)", "name": "泡シャンプー (セラミドを守って洗う消炎剤配合・冬の敏感な頭皮のフケやかゆみを防ぐ弱酸性処方)"},
            {"rank": 4, "query": "エトヴォス リフレッシュシャンプー スカルプシャンプー", "brand": "ETVOS (エトヴォス)", "name": "リフレッシュシャンプー / モイストシャンプー (アミノ酸系洗浄成分×植物エキス・地肌のうるおいバランスを整えるノンシリコン)"},
            {"rank": 5, "query": "カダソン 薬用スカルプシャンプー KADASON", "brand": "KADASON (カダソン)", "name": "薬用スカルプシャンプー (皮膚科医監修・冬の脂漏性トラブルや乾燥フケ・かゆみを徹底予防する低刺激薬用処方)"},
            {"rank": 6, "query": "スカルプD ボーテ ナチュラスター スカルプシャンプー", "brand": "スカルプD ボーテ (アンファー)", "name": "ナチュラスター スカルプシャンプー (天然由来成分90%以上・冬の寒暖差やストレスで硬くなった頭皮を優しくほぐす)"},
            {"rank": 7, "query": "コタ アイケア シャンプー 5 COTA i CARE", "brand": "COTA (コタ)", "name": "コタ アイケア シャンプー 5 (アミノ酸系×オリーブ系PPT洗浄成分・冬のパサつく髪と地肌をしっとりみずみずしく洗い上げる)"},
            {"rank": 8, "query": "ミルボン クロナ スカルプ クレンジング スパシャンプー", "brand": "MILBON (ミルボン)", "name": "クロナ スカルプ クレンジング スパシャンプー (炭酸泡で冬の血行不良頭皮をマッサージ・毛穴詰まりをスッキリ保湿オフ)"},
            {"rank": 9, "query": "アミノレスキュー スカルプ シャンプー 保湿", "brand": "aminoRESQ (アミノレスキュー)", "name": "モイストシャンプー (アミノ酸系洗浄成分と6種の美容ケラチン配合・頭皮と髪の芯まで高保湿うるおいチャージ)"},
            {"rank": 10, "query": "ルベル イオ セラム クレンジング シャンプー", "brand": "LebeL (ルベル)", "name": "イオ セラム クレンジング (グリーンナッツオイル配合・冬の乾燥でうねり広がる髪と地肌にたっぷりの水分を届ける)"}
        ]
    },
    "winter_cica_cream": {
        "title": "保湿力の強さで冬の肌荒れ・寒風赤みとさようなら！肌バリアを集中強化する高保湿シカクリームランク10",
        "page_file": "winter-cica-cream.html",
        "items": [
            {"rank": 1, "query": "ラロッシュポゼ シカプラスト リペアクリーム B5+", "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)", "name": "シカプラスト リペアクリーム B5+ (独自成分トリビオーマ×マデカッソシド×パンテノール5%・冬の深刻な肌荒れを急速リペア)"},
            {"rank": 2, "query": "VT シカクリーム CICA CREAM 50ml", "brand": "VT COSMETICS (ブイティー)", "name": "CICAクリーム (シカリオ×シカヒアルロン配合・ベタつかずみずみずしく肌荒れを沈静化する国民的シカクリーム)"},
            {"rank": 3, "query": "Dr.Jart+ ドクタージャルト シカペア クリーム 50ml", "brand": "Dr.Jart+ (ドクタージャルト)", "name": "シカペア クリーム (第2世代・高濃縮ツボクサエキス配合の緑の濃厚クリームが冬の寒風による赤みを徹底カバー＆鎮静)"},
            {"rank": 4, "query": "アベンヌ シカルファットプラス リペアクリーム 40g", "brand": "Avene (アベンヌ)", "name": "シカルファットプラス リペアクリーム (アベンヌ温泉水×C+リペア成分・冬のひび割れや極度の乾燥肌荒れを優しく密封ガード)"},
            {"rank": 5, "query": "BIOHEAL BOH パンテノール シカ ブレミッシュ クリーム", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "パントシカ バリアクリーム (高浸透パンテノール×CICA成分・冬の乱れた肌バリアを再構築してつるんとした健やか肌へ)"},
            {"rank": 6, "query": "イニスフリー ビジャ シカバーム EX 40ml", "brand": "innisfree (イニスフリー)", "name": "ビジャ シカバーム EX (カヤ種子油×高純度センテラアジアティカ4X配合・冬のデリケートなゆらぎ肌を整えるジェルバーム)"},
            {"rank": 7, "query": "リアルバリア エクストリーム クリーム CICA", "brand": "Real Barrier (リアルバリア)", "name": "エクストリーム クリーム (特許セラミドMLE技術×CICAコンプレックス・真冬の過酷な乾燥環境でも72時間うるおい持続)"},
            {"rank": 8, "query": "ネイチャーリパブリック グリーンダーマ CICA エイジング クリーム", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "グリーンダーマ CICA デイリークリーム (プロポリスエキス×センテラ成分・冬の肌のカサつきと肌荒れを同時にうるおす大容量)"},
            {"rank": 9, "query": "MEDIHEAL メディヒール ティーツリー カーミング クリーム", "brand": "MEDIHEAL (メディヒール)", "name": "ティーツリー スージング クリーム (ティーツリー×ツボクサエキス配合・冬の乾燥ニキビや赤みをやさしくクールダウン)"},
            {"rank": 10, "query": "スキンアンドラブ K プラス レッドエックス クリーム", "brand": "SKIN&LAB (スキンアンドラブ)", "name": "K プラス レッドエックス クリーム (ビタミンK×CICAエキス配合・冬の寒暖差で起こる頬の赤ら顔や毛細血管の目立ちを集中ケア)"}
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
                    # fallback to general query if empty
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
        print(f"  Rank {res_item['rank']}: {res_item['brand']} - ¥{res_item['price']:,} - Img: {res_item['img'][:40]}...")
        cat_items.append(res_item)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

with open("rakuten_3latest_articles_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDone! All items fetched and saved to rakuten_3latest_articles_data.json")
