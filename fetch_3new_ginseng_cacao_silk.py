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
    "winter_ginseng": {
        "title": "保湿力の強さで肌乾燥とさようなら！高麗人参（オタネニンジン）のサポニン温感・滋養パワーが真冬の冷え固まり枯れ肌を蘇らせる高保湿ジンセンコスメランク10",
        "file": "winter-ginseng.html",
        "items": [
            {
                "rank": 1,
                "queries": ["雪花秀 滋陰生 アンプル", "Sulwhasoo 滋陰生 アンプル"],
                "brand": "Sulwhasoo (雪花秀 / ソルファス)",
                "name": "滋陰生(ジャウムセン) アンプル 20g (高麗人参の希少サポニンを高濃縮配合・冬の寒冷で代謝が落ちた肌をふっくら持ち上げ濃密な潤いで満たす韓国最高峰エイジングケア美容液)"
            },
            {
                "rank": 2,
                "queries": ["朝鮮美女 ジンセン エッセンスウォーター", "Beauty of Joseon 高麗人参 エッセンス"],
                "brand": "Beauty of Joseon (朝鮮美女)",
                "name": "ジンセン エッセンスウォーター 150ml (オタネニンジン根水80%配合・ナイアシンアミドとアデノシンが真冬の乾燥くすみを一掃し角層深くみずみずしいツヤを巡らせる大人気韓方トナー)"
            },
            {
                "rank": 3,
                "queries": ["Beauty of Joseon リバイブ アイセラム", "Beauty of Joseon ジンセン アイセラム"],
                "brand": "Beauty of Joseon (朝鮮美女)",
                "name": "リバイブ アイセラム (ジンセン＋レチナール) 30ml (高麗人参エキス10%×レチナール2%配合・真冬の冷気と暖房で乾燥小ジワが深まりやすいデリケートな目元をふっくら持ち上げる韓方アイセラム)"
            },
            {
                "rank": 4,
                "queries": ["The history of 后 津率享 津率", "The history of 后 津率享"],
                "brand": "The History of Whoo (後 / ドフー)",
                "name": "津率享(ジンユルヒャン) 津率クリーム 50ml (宮廷秘伝の紅参・オタネニンジンエキス高配合・真冬の寒さで皮脂が枯渇した大人の肌を贅沢なコクで包み込む濃密高保湿クリーム)"
            },
            {
                "rank": 5,
                "queries": ["ドンインビ 1899 シグネチャー オイル", "DONGINBI 1899 オイル"],
                "brand": "DONGINBI (ドンインビ / 正官庄)",
                "name": "1899 シグネチャー オイル 25g (正官庄が誇る高純度紅参オイル100%・1本の高麗人参からごくわずかしか採れない希少オイルが真冬の乾燥砂漠肌を即座にリッチなツヤ肌へ導く至高のフェイスオイル)"
            },
            {
                "rank": 6,
                "queries": ["朝鮮美女 Beauty of Joseon 韓方美容液 30ml", "Beauty of Joseon グロウセラム"],
                "brand": "Beauty of Joseon (朝鮮美女)",
                "name": "リバイブ セラム (高麗人参×カタツムリムチン) 30ml (オタネニンジン根水63%×カタツムリ分泌液3%・真冬のダメージを受けた肌のキメをなめらかに修復し濃密な弾力をもたらす集中美容液)"
            },
            {
                "rank": 7,
                "queries": ["水橋保寿堂製薬 UMOR ウモール オールインワンクリーム", "ウモール オールインワンクリーム"],
                "brand": "水橋保寿堂製薬 (UMOR)",
                "name": "ウモール (UMOR) 保湿オールインワンクリーム 100g (高麗人参エキス×かたつむりエキス×植物エキス配合・真冬の乾燥による小ジワや乾燥くすみをひと塗りで満たす濃厚ジェルクリーム)"
            },
            {
                "rank": 8,
                "queries": ["菅貞子保湿シートマスクパック オタネニンジン", "菅貞子保湿シートマスクパック"],
                "brand": "KANコルギセラピー (菅貞子)",
                "name": "菅貞子 モイスチャー シートマスクパック (オタネニンジン根エキス×植物性コラーゲン配合・真冬の冷えた肌に濃密な和漢美容液をピタッと密着させて蘇らせるサロン級シートマスク)"
            },
            {
                "rank": 9,
                "queries": ["大木製薬 人参石鹸 紅蔘石鹸", "コウジンソープ 90g 大木製薬"],
                "brand": "大木製薬 (コウジンソープ)",
                "name": "紅蔘石鹸 コウジンソープ 90g (天然高麗人参エキス配合・クリーミーな弾力泡が冬の乾燥肌をやさしく包み込み、毛穴の汚れを落としながらしっとりなめらかに洗い上げる伝統石鹸)"
            },
            {
                "rank": 10,
                "queries": ["オルフェス イエロー シートマスク", "オルフェス ALFACE シートマスク イエロー"],
                "brand": "ALFACE+ (オルフェス)",
                "name": "イエローエッセンシャルマスク (高麗人参エキス×ビタミン誘導体配合・真冬の冷えや乾燥で疲れた肌にぐんぐん潤いを浸透させ毛穴の目立たない透明ハリ肌へ導く密着シートマスク)"
            }
        ]
    },
    "winter_cacao_butter": {
        "title": "保湿力の強さで肌乾燥とさようなら！人肌でとろける高純度カカオバターが真冬の粉吹き・カチコチひび割れ肌をベルベット密着膜で包み込む高保湿ココアバターコスメランク10",
        "file": "winter-cacao-butter.html",
        "items": [
            {
                "rank": 1,
                "queries": ["Palmer's ココアバター ボディローション", "パーマーズ ココアバター ボディローション 250ml"],
                "brand": "Palmer's (パーマーズ)",
                "name": "ココアバター フォーミュラ 保湿ボディローション 250ml / 400ml (純粋カカオバター×ビタミンE配合・真冬の粉吹き脚や肘・膝を極上の甘いショコラの香りと共に滑らかに保つ世界的人気ボディケア)"
            },
            {
                "rank": 2,
                "queries": ["ココアバターリップバーム クリーミーココア バジャー", "バジャー ココアバター リップバーム"],
                "brand": "Badger (バジャー)",
                "name": "オーガニック ココアバター リップバーム (クリーミーココア) 7g (USDAオーガニック認定・人肌でじんわりとろける濃密カカオ脂が冬の極冷風から唇のバリア膜を死守する万能リップバーム)"
            },
            {
                "rank": 3,
                "queries": ["WELEDA ヴェレダ スキンフード ボディバター", "ヴェレダ スキンフード ボディバター 150ml"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "スキンフード ボディバター 150ml (天然カカオバター×シアバター×パンジーエキス・ホイップクリームのようにとろけて真冬のガサガサ粉吹き肌を長時間しっとり包み込む濃厚ボディクリーム)"
            },
            {
                "rank": 4,
                "queries": ["SH ココアバター 100g カカオ", "&SH ココアバター 100g"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100% ピュア カカオバター (ココアバター) 100g (低温圧搾コールドプレス・天然カカオ特有の甘く濃厚な香りを保持・真冬のカチコチかかとや指先のひび割れを体温で溶かして集中ラッピングする純粋植物バター)"
            },
            {
                "rank": 5,
                "queries": ["Palmer's リップバーム SPF15 ココアバター", "パーマーズ リップバーム SPF15"],
                "brand": "Palmer's (パーマーズ)",
                "name": "ココアバター モイスチャライジング リップバーム SPF15 4g (カカオバター×ビタミンE配合・真冬の強烈な乾燥と冬紫外線からデリケートな唇を守り抜き、縦ジワや皮むけを長時間防ぐ高保湿リップスティック)"
            },
            {
                "rank": 6,
                "queries": ["ナイアード チウリモイスチャークリーム 40ml", "ナイアード チウリモイスチャークリーム"],
                "brand": "naiad (ナイアード)",
                "name": "チウリモイスチャークリーム 40ml (ヒマラヤの野生チウリバター×天然カカオ脂×ミツロウ・人肌でじんわりとろけて真冬の過酷な乾燥・粉吹き・あかぎれ手肌を贅沢にうるおす高保湿マルチバーム)"
            },
            {
                "rank": 7,
                "queries": ["SH ココアバター 200g カカオ", "&SH ココアバター 200g"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "大容量 カカオバター (ココアバター) 200g (無添加・国産充填・手持ちの乳液やオイルと混ぜて真冬の極上ハンドクリームやフットバームを自作できる高純度ピュアバター)"
            },
            {
                "rank": 8,
                "queries": ["Palmer's ココアバター ボディローション 400ml", "パーマーズ ココアバター ボディローション"],
                "brand": "Palmer's (パーマーズ)",
                "name": "ココアバター フォーミュラ エモリエント ボディローション 400ml (大容量ポンプタイプ・純粋カカオバター高配合・冬のお風呂上がりに全身に伸ばすだけで翌朝までベルベットのような極上の潤いが続くロングセラー)"
            },
            {
                "rank": 9,
                "queries": ["パーマーズ マッサージローション ココアバター", "Palmer's マッサージローション ココアバター"],
                "brand": "Palmer's (パーマーズ)",
                "name": "ココアバター マッサージローション 250ml (純粋カカオバター×アルガンオイル×コラーゲン配合・真冬の急激な乾燥で突っ張るボディの柔軟性を保ち皮膚を柔らかく整える高保湿ローション)"
            },
            {
                "rank": 10,
                "queries": ["Nubian Heritage ブラックソープ", "アフリカンブラックソープ 141g"],
                "brand": "Nubian Heritage (ヌビアンヘリテージ)",
                "name": "アフリカンブラックソープ (シアバター＆カカオ脂配合) 141g (伝統的な天然植物油脂ベース・冬の乾燥肌でも皮脂を落としすぎず、もっちりとした潤いヴェールを残す高保湿ソープ)"
            }
        ]
    },
    "winter_silk": {
        "title": "保湿力の強さで肌乾燥とさようなら！人肌と酷似した18種のアミノ酸が真冬の摩擦・暖房乾燥から素肌を守り抜く高保湿加水分解シルクコスメランク10",
        "file": "winter-silk.html",
        "items": [
            {
                "rank": 1,
                "queries": ["初絹ピュアレストシルククリーム 35g", "アーダン 初絹 シルククリーム"],
                "brand": "Adan (アーダン / 初絹)",
                "name": "初絹 ピュアレスト シルククリーム 35g (国産高純度シルク抽出液主原料・人間の肌組成と酷似した天然セリシンが真冬の冷風や摩擦で荒れた角層を優しく包み込み翌朝まで潤い膜を維持する最高峰シルククリーム)"
            },
            {
                "rank": 2,
                "queries": ["シルクエキス 原液 100％ 美容液 20mL", "シルクエキス 原液 美容液 20ml"],
                "brand": "自然化粧品研究所",
                "name": "シルクエキス 原液 100％ 美容液 20ml (天然加水分解シルク・18種のアミノ酸が真冬のエアコン乾燥でパサつく肌と髪を集中リペアする濃厚アンプル原液)"
            },
            {
                "rank": 3,
                "queries": ["心髪 PREMIUM シルキートナーミスト 200ml", "シルキートナーミスト 200ml 心髪"],
                "brand": "心髪 (cocorogami)",
                "name": "PREMIUM シルキートナーミスト 200ml (加水分解シルク×フラーレン×ヒアルロン酸配合・冬の暖房で乾いた頭皮と髪、お風呂上がりの肌にシュッと吹きかけて瞬時にシルクのような手触りへ導く高保湿ミスト化粧水)"
            },
            {
                "rank": 4,
                "queries": ["アーダン化粧品 シルクパウダー15g", "アーダン シルクパウダー 15g"],
                "brand": "Adan (アーダン)",
                "name": "シルクパウダー 15g (高純度フィブロイン100%・アミノ酸だけで作られたスキンケアパウダー・真冬のメイク仕上げに使うことで日中の水分蒸発を防ぎ暖房下でも乾燥崩れを起こさない極上フェイスパウダー)"
            },
            {
                "rank": 5,
                "queries": ["シルク 100% フェイスパック 大容量 30枚", "シルク フェイスマスク 大容量 30枚"],
                "brand": "絹肌 (Kinuhada)",
                "name": "シルク 100% フェイスパック 大容量 30枚入り (天然加水分解シルクアミノ酸×ヒアルロン酸・毎晩の密着シートマスクで冬の過酷な乾燥にさらされた角層を潤いでひたひたに満たす高保湿デイリーマスク)"
            },
            {
                "rank": 6,
                "queries": ["MOTON 公式 シルクヘアオイル", "モトン シルクヘアオイル 100ml"],
                "brand": "MOTON (モトン)",
                "name": "シルクヘアオイル 100ml (加水分解シルク×植物オイル処方・真冬のセーターやマフラーの静電気摩擦から髪を守り、毛先までパサつかずベルベットのようなシルクツヤ髪に仕上げる大人気ヘアオイル)"
            },
            {
                "rank": 7,
                "queries": ["MOTON 公式 ハンドクリーム 選べる3つの香り モトン", "MOTON ハンドクリーム シルク 50ml"],
                "brand": "MOTON (モトン)",
                "name": "シルクハンドクリーム 50ml (シルクエキス配合・ベタつかないのに角層の奥までうるおいを閉じ込め、冬の水仕事や外気で荒れやすい手肌をしっとりなめらかに保つ上品なフレグランスハンドケア)"
            },
            {
                "rank": 8,
                "queries": ["ジューニ ダメージリペアヘアミルク 150ml", "12/JU-NI ヘアミルク 150ml"],
                "brand": "木村石鹸 (12/JU-NI)",
                "name": "ジューニ (12/JU-NI) ダメージリペアヘアミルク 150ml (加水分解シルク×コラーゲンアミノ酸高配合・真冬の酷い毛先のパサつき・枝毛・広がりを芯から保湿してまとまりを一日中キープする集中リペアミルク)"
            },
            {
                "rank": 9,
                "queries": ["ミネソワWソープ 100g シルク石けん", "ミネソワ シルク石鹸 100g"],
                "brand": "ミネソワ (Minesowa)",
                "name": "ミネソワ Wソープ 100g (純国産シルクエキス×枠練り製法・シルクセリシンの濃密クリーミー泡が冬の乾燥肌を優しく包み込み、洗顔後もつっぱらず化粧水をつけたかのような滑らかさを叶える美容石鹸)"
            },
            {
                "rank": 10,
                "queries": ["絹肌日和 フェイスマスク シルクセリシン", "絹肌日和 フェイスマスク1枚入り"],
                "brand": "絹肌日和 (Kinuhada Biyori)",
                "name": "絹肌日和 フェイスマスク (高純度シルクセリシン高配合・真冬の特別な日の前夜に使う集中リペアウェットマスク・肌のバリア機能を瞬時に整え陶器のような滑らかさを引き出すプレミアムシートパック)"
            }
        ]
    }
}

def fetch_and_save():
    results = {}
    total_needed = sum(len(c["items"]) for c in CATEGORIES.values())
    total_success = 0

    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title']})")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Trying Rank {item['rank']}: '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                for attempt in range(3):
                    try:
                        time.sleep(2.5)
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 300 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(3)
                
                if chosen_item:
                    print(f"  -> Found item: {chosen_item['itemName'][:40]}... (¥{chosen_item['itemPrice']:,})")
                    break

            if chosen_item:
                total_success += 1
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]["imageUrl"]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]["imageUrl"]
                
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "name": item["name"],
                    "rakuten_name": chosen_item["itemName"],
                    "price": f"¥{chosen_item['itemPrice']:,}",
                    "raw_price": chosen_item['itemPrice'],
                    "url": chosen_item["affiliateUrl"] if chosen_item.get("affiliateUrl") else chosen_item["itemUrl"],
                    "img": img_url,
                    "reviewCount": chosen_item.get("reviewCount", 0),
                    "reviewAverage": chosen_item.get("reviewAverage", "0.0")
                })
            else:
                print(f"  [WARNING] No item found for rank {item['rank']}: {item['name']}")

    output_filename = "fetched_3new_ginseng_cacao_silk.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items successfully fetched!")
    print(f"Results saved to {output_filename}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
