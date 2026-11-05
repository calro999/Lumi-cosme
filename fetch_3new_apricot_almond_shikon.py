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
    "winter_apricot_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の目元・首元のポツポツ乾燥＆ゴワつきをなめらかに整える高保湿杏仁オイルコスメランク10",
        "file": "winter-apricot-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アンミオイル 30ml", "アンミオイル ジーランドビフ", "アンミオイル"],
                "brand": "ZEALAND BIFU (ジーランドビフ)",
                "name": "アンミオイル 30ml (主原料の杏仁オイルを70%以上高配合・冬の目元や首周りの気になるポツポツ角質粒やざらつきを柔らかく整える伝説のロングセラー美容オイル)"
            },
            {
                "rank": 2,
                "queries": ["生活の木 アプリコットカーネルオイル 70ml", "生活の木 アプリコットカーネルオイル", "アプリコットカーネル 生活の木"],
                "brand": "生活の木 (Tree of Life)",
                "name": "有機 アプリコットカーネルオイル 70ml (低温圧搾コールドプレス・肌馴染み抜群のオレイン酸とリノール酸が真冬のカチコチ角層をふっくらほぐす高純度オーガニックオイル)"
            },
            {
                "rank": 3,
                "queries": ["&SH アプリコットカーネルオイル 80ml", "&SH アプリコットカーネルオイル", "&SH 杏仁オイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100% ピュア アプリコットカーネルオイル 80ml (無添加・国産充填・ビタミンAやB群を含有し真冬の洗顔後ブースターとして抜群の浸透力を誇る大容量キャリアオイル)"
            },
            {
                "rank": 4,
                "queries": ["アプリコットカーネルオイル 未精製 オーガニック 50ml", "アプリコットカーネルオイル マンディムーン 50ml", "マンディムーン アプリコットカーネルオイル"],
                "brand": "Mandy Moon (マンディムーン)",
                "name": "オーガニック アプリコットカーネルオイル (未精製) 50ml (低温圧搾コールドプレス・杏の種子の栄養を壊さず抽出・冬の乾燥による首元や目元の小ジワをふっくら満たすリッチオイル)"
            },
            {
                "rank": 5,
                "queries": ["アプリコットカーネル 100ml", "アプリコットカーネルオイル 100ml", "アプリコットカーネルオイル"],
                "brand": "spa hinoki (スパヒノキ)",
                "name": "オーガニック アプリコットカーネルオイル 100ml (コスモスオーガニック認証・未精製コールドプレス・真冬の首元や目元のざらつき・粉吹き角層をしっとり滑らかに包み込む高保湿オイル)"
            },
            {
                "rank": 6,
                "queries": ["アプリコットカーネルオイル 300mL", "マカダミア屋 アプリコットカーネルオイル", "アプリコットカーネルオイル 300ml"],
                "brand": "マカダミア屋",
                "name": "天然無添加 アプリコットカーネルオイル 300ml (ポンプ付大容量・真冬の入浴後の全身保湿からデコルテ・首元のポツポツざらつき集中マッサージまで贅沢に使える高純度植物油)"
            },
            {
                "rank": 7,
                "queries": ["アプリコットオイル 40mL 医薬", "薬用アプリコットオイル 40ml", "アプリコットオイル 首 イボ"],
                "brand": "AIWA (アイワ)",
                "name": "薬用 アプリコットオイル 40ml (医薬部外品・グリチルレチン酸ステアリル配合・真冬の肌荒れやひび割れを防ぎながら首元や目元の角質粒を滑らかに集中ケアする薬用オイル)"
            },
            {
                "rank": 8,
                "queries": ["つぶぽろん 目元 温感", "つぶぽろん 目元和漢", "つぶぽろん"],
                "brand": "リベルタ (つぶぽろん)",
                "name": "つぶぽろん 目元温和漢パック 1.8g (杏仁オイル×ハトムギエキス×和漢植物成分配合・温感ジェルで真冬の目元の頑固なざらつき・角質粒を優しくピーリング＆保湿ケアするスティックパック)"
            },
            {
                "rank": 9,
                "queries": ["アプリコットオイル 118ml ナウフーズ", "NOW Foods アプリコットオイル 118ml", "ナウフーズ アプリコットオイル"],
                "brand": "NOW Foods (ナウフーズ)",
                "name": "ピュア アプリコットオイル 118ml (100%純粋コールドプレス・非遺伝子組み換え・真冬の乾燥小ジワや髪のパサつきをひと塗りでシルクのように整える世界的ベストセラーオイル)"
            },
            {
                "rank": 10,
                "queries": ["自然化粧品研究所 アプリコットカーネルオイル", "自然化粧品研究所 杏仁オイル 100ml", "自然化粧品研究所 杏仁"],
                "brand": "自然化粧品研究所",
                "name": "アプリコットカーネルオイル (杏仁油) 100ml (国内精製・肌に優しい低刺激処方・冬のナイトケアで手持ちのクリームにブレンドして乾燥バリアを飛躍的に強化するスキンケアオイル)"
            }
        ]
    },
    "winter_sweet_almond_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！高濃度オレイン酸とビタミンEが真冬の粉吹き肌＆デリケートな乾燥角層をふっくらほぐす高保湿スイートアーモンドオイルコスメランク10",
        "file": "winter-sweet-almond-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ヴェレダ アーモンド フェイシャルオイル", "ヴェレダ アーモンドオイル フェイス", "ヴェレダ アーモンド オイル"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "アーモンド フェイシャルオイル 50ml (無香料・有機アーモンドオイル×プラム種子油配合・冬の寒暖差や冷風で敏感に傾いた角層バリアを優しく包み込み刺激から守る集中トリートメントオイル)"
            },
            {
                "rank": 2,
                "queries": ["ロクシタン アーモンド シャワーオイル", "ロクシタン アーモンド モイスチャライジング シャワーオイル 250ml", "ロクシタン アーモンド シャワーオイル 250ml"],
                "brand": "L'OCCITANE (ロクシタン)",
                "name": "アーモンド モイスチャライジング シャワーオイル 250ml (水に触れると濃密ミルクに変化・入浴中の皮膚から水分が逃げるのを防ぎ洗い上がりから極上のベルベット肌へ導くインバス名品)"
            },
            {
                "rank": 3,
                "queries": ["生活の木 スイートアーモンドオイル 250ml", "生活の木 スイートアーモンドオイル 70ml", "生活の木 スイートアーモンドオイル"],
                "brand": "生活の木 (Tree of Life)",
                "name": "スイートアーモンドオイル 250ml (低温圧搾コールドプレス・肌滑らかなテクスチャーで真冬のカチコチに冷えた脚やお腹のマッサージ、洗顔後のプレオイルに最適な定番キャリアオイル)"
            },
            {
                "rank": 4,
                "queries": ["ナウフーズ スイートアーモンドオイル 473ml", "NOW Foods スイートアーモンドオイル 473ml", "NOW アーモンドオイル 473ml"],
                "brand": "NOW Foods (ナウフーズ)",
                "name": "100% ピュア スイートアーモンドオイル 473ml (圧搾抽出・無臭・圧倒的な大容量で真冬の粉吹きすね・肘・踵からヘアパックまで全身惜しみなく高保湿できる世界的大人気オイル)"
            },
            {
                "rank": 5,
                "queries": ["&SH スイートアーモンドオイル 100ml", "&SH スイートアーモンドオイル 1000ml", "&SH アーモンドオイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100% ピュア スイートアーモンドオイル 100ml (無添加コールドプレス・赤ちゃんから使える低刺激設計・真冬の洗顔後すぐに肌をほぐして化粧水の浸透を高めるブースターオイル)"
            },
            {
                "rank": 6,
                "queries": ["オーガニック スイートアーモンドオイル 100mL spahinoki", "スイートアーモンドオイル 100mL spahinoki", "スイートアーモンドオイル 100ml"],
                "brand": "spa hinoki (スパヒノキ)",
                "name": "オーガニック スイートアーモンドオイル 100ml (エコサートコスモス認証・未精製コールドプレス・真冬のデリケートな乾燥肌をしっとり潤し皮脂膜を健やかに育む高純度オーガニックオイル)"
            },
            {
                "rank": 7,
                "queries": ["天然無添加 国内精製 スイートアーモンドオイル 500ml", "スイートアーモンドオイル 500ml", "アーモンドオイル 500ml"],
                "brand": "自然化粧品研究所",
                "name": "天然無添加 国内精製 スイートアーモンドオイル 500ml (大容量ポンプ仕様・真冬の家族全員のボディ保湿やお風呂上がりの全身エモリエントマッサージに惜しみなく使える大容量ボトル)"
            },
            {
                "rank": 8,
                "queries": ["スイートアーモンドオイル 300mL", "マカダミア屋 スイートアーモンドオイル 300ml", "マカダミア屋 アーモンドオイル 300ml"],
                "brand": "マカダミア屋",
                "name": "天然100% スイートアーモンドオイル 300ml (ポンプボトル・抜群のクッション性と保湿持続力で真冬の冷え固まったふくらはぎのリンパマッサージやガサガサ踵を集中トリートメントする万能オイル)"
            },
            {
                "rank": 9,
                "queries": ["ヴェレダ スキンフード N 75ml", "ヴェレダ スキンフード 75ml", "ヴェレダ スキンフード"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "スキンフード 75ml (アーモンド油×ヒマワリ油×パンジーエキス・1926年誕生の超ロングセラー・真冬のゴワつく肘・膝・かかとや極度の乾燥肌を鉄壁の潤い膜で守る濃厚リッチクリーム)"
            },
            {
                "rank": 10,
                "queries": ["自然化粧品研究所 スイートアーモンドオイル", "自然化粧品研究所 スイートアーモンドオイル 100ml", "自然化粧品研究所 アーモンドオイル"],
                "brand": "自然化粧品研究所",
                "name": "スイートアーモンドオイル 100ml (国内精製・無香料・ビタミンEとミネラルを豊かに保持し真冬のクレンジングからナイトパックまで多用途に使える無添加スキンケアオイル)"
            }
        ]
    },
    "winter_shikon": {
        "title": "保湿力の強さで肌乾燥とさようなら！伝統の紫根エキス（シコニン）が真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する高保湿紫根コスメランク10",
        "file": "winter-shikon.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エイジングケア 紫根化粧水 200mL", "紫根化粧水 200mL", "紫根化粧水"],
                "brand": "自然の都タマチャンショップ (美肌和漢)",
                "name": "エイジングケア 紫根化粧水 200ml (天然ムラサキ根エキス×ヒアルロン酸配合・真冬の冷風で赤みやヒリつきを起こした肌を穏やかに鎮静しながら角層深部までみずみずしく満たす大人気和漢ローション)"
            },
            {
                "rank": 2,
                "queries": ["紫根エキス 原液 20mL", "自然化粧品研究所 紫根エキス 20ml", "自然化粧品研究所 紫根エキス"],
                "brand": "自然化粧品研究所",
                "name": "紫根エキス (シコンエキス) 原液 20ml (天然ムラサキ根から抽出したシコニン高濃度原液・手持ちの化粧水や乳液に数滴混ぜるだけで真冬の激しい乾燥荒れ肌を集中レスキューする高機能アンプル)"
            },
            {
                "rank": 3,
                "queries": ["オリーブマノン 紫草", "日本オリーブ 紫草オリーブマノン 30ml", "紫草 オリーブマノン 30ml"],
                "brand": "日本オリーブ (オリーブマノン)",
                "name": "紫草 (シコン) オリーブマノン うるおい美容液 30ml (天然紫根エキス×自社農園産オリーブ油・真冬の木枯らしでカサつく角層をピンクの濃密オイルヴェールで包み込みふっくら整える和漢美容液)"
            },
            {
                "rank": 4,
                "queries": ["自然化粧品研究所 紫根クリーム", "自然化粧品研究所 紫根クリーム 35g", "紫根クリーム 自然化粧品研究所"],
                "brand": "自然化粧品研究所",
                "name": "紫根クリーム (シコンクリーム) 35g (高純度シコニン×ホホバ油×スクワラン・真冬の水仕事や冷気による手荒れ・頬の粉吹き・ひび割れを集中ガードする濃厚ピンクモイスチャークリーム)"
            },
            {
                "rank": 5,
                "queries": ["紫根エキス30ml", "シコンエキス 30ml", "紫根 美容液"],
                "brand": "手作り化粧品材料 マンディムーン",
                "name": "高濃度 シコンエキス (紫根) 30ml (水溶性天然植物エキス・紫根の主成分シコニンを高純度抽出・冬の乾燥荒れ肌やカサつき・赤み肌のスキンケアに1滴プラスして角質修復を促す和漢ブースター)"
            },
            {
                "rank": 6,
                "queries": ["藍と紫根の目元パック", "藍と紫根 目元パック", "藍と紫根"],
                "brand": "シェモア (Chezmoi)",
                "name": "藍と紫根の目元パック 30g (和漢植物エキス紫根×藍エキス高配合・真冬の過酷な乾燥でくすみ・小ジワ・たるみが現れやすいデリケートな目元を寝ている間に集中リペアするピールオフパック)"
            },
            {
                "rank": 7,
                "queries": ["椿のリップクリーム 椿乃", "紫根 リップクリーム", "紫根 リップ"],
                "brand": "椿乃 (TSUBAKINO)",
                "name": "椿のリップクリーム (五島列島産ヤブツバキ油×天然紫根エキス配合) 4g (無添加・真冬の冷たい外気で皮むけや縦ジワ・ひび割れを起こした唇をじんわり修復し美しい血色感を与える和漢濃密リップ)"
            },
            {
                "rank": 8,
                "queries": ["魔女工場 ピュア クレンジングオイル", "魔女工場 ピュア クレンジングオイル 200ml", "魔女工場 クレンジングオイル ピュア"],
                "brand": "manyo (魔女工場)",
                "name": "ピュア クレンジングオイル 200ml (米ぬか油×ダイズ油×ホホバ油配合・冬の濃密メイクも角栓も擦らずスルリと溶かし落としながら肌本来の潤い膜を守り抜く韓国No.1クレンジング名品)"
            },
            {
                "rank": 9,
                "queries": ["紫根 フェイスマスク 30枚", "MITOMO シコン フェイスマスク", "紫根 パック 30枚"],
                "brand": "MITOMO (ミトモ)",
                "name": "CARE601 紫根＋EGF プレミアムエッセンスマスク 30枚入り (天然紫根エキス×上皮成長因子EGF配合・真冬の暖房下で水分がカラカラに蒸発した素肌を贅沢な和漢美容液で毎日満たす大容量密着シートマスク)"
            },
            {
                "rank": 10,
                "queries": ["洗顔用 紫根石けん", "ちのしお 紫根せっけん 100g", "紫根 石鹸 100g"],
                "brand": "自然派くらぶ",
                "name": "洗顔用 紫根石けん 泡立てネット付 100g (天然紫根エキス配合・植物油脂100%の伝統枠練り製法・真冬の乾燥敏感肌でも洗顔後につっぱらずしっとり滑らかな洗い上がりを叶える和漢スキンケアソープ)"
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
                
                # リトライ＆レートリミット対策（2.5秒ウェイト）
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
                        time.sleep(4)
                
                if chosen_item:
                    print(f"  -> Found item: {chosen_item['itemName'][:40]}... (¥{chosen_item['itemPrice']})")
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

    output_filename = "fetched_3new_apricot_almond_shikon.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items successfully fetched!")
    print(f"Results saved to {output_filename}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
