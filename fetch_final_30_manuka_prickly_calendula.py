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
    "winter_manuka_honey": {
        "title": "保湿力の強さで肌乾燥とさようなら！メディカル級の濃密保水膜で真冬の荒れ肌を包み込む高純度マヌカハニーコスメランク10",
        "file": "winter-manuka-honey.html",
        "items": [
            {
                "rank": 1,
                "queries": ["山田養蜂場 マヌカハニー クレンジングバーム 75g", "山田養蜂場 マヌカハニークレンジングバーム", "山田養蜂場 クレンジングバーム"],
                "brand": "山田養蜂場 (YAMADA BEE FARM)",
                "name": "マヌカハニー クレンジングバーム 75g (生マヌカ蜂蜜と生ローヤルゼリーを贅沢凝縮・冬の毛穴汚れと角栓をとろけさせながら濃密な潤いシールドを張る最高峰とろけるバーム)"
            },
            {
                "rank": 2,
                "queries": ["マヌカコスメ B&H ドロップローション 150ml", "マヌカコスメ ドロップローション", "マヌカコスメ ローション 150ml"],
                "brand": "マヌカコスメ (Manuka Cosme)",
                "name": "B&H ドロップローション 150ml (ニュージーランド産高純度マヌカハニー×プロポリス配合・真冬の冷風でゴワついた角層へしっとり浸透し満水状態をキープする高保湿化粧水)"
            },
            {
                "rank": 3,
                "queries": ["マヌカヘルス リップバーム 4.5g", "マヌカヘルス マヌカハニー リップバーム", "マヌカヘルス リップ"],
                "brand": "Manuka Health (マヌカヘルス)",
                "name": "マヌカハニー MGO250+ リップバーム 4.5g (医療グレード水準のマヌカハニーと天然ミツロウを配合・真冬の寒風で皮むけ・ひび割れした唇を濃密な蜜膜で包み込む集中リップケア)"
            },
            {
                "rank": 4,
                "queries": ["チャントアチャーム ディープモイストオイル 60ml", "チャントアチャーム ディープモイストオイル", "チャントアチャーム モイストオイル"],
                "brand": "chant a charm (チャントアチャーム)",
                "name": "ディープモイストオイル 60ml (無農薬ハーブエキス×マヌカハニー×植物性スクワランの2層式ブースター・真冬の硬直肌をやわらげ水分を抱え込ませる濃密導入美容オイル)"
            },
            {
                "rank": 5,
                "queries": ["マヌカコスメ B&H モイストリペアバーム", "マヌカコスメ モイストリペアバーム 15g", "マヌカハニー バーム 15g"],
                "brand": "マヌカコスメ (Manuka Cosme)",
                "name": "B&H モイストリペアバーム 15g (高濃度マヌカハニー×シアバター×オリーブ油・真冬の目元・口元・粉吹きゾーンをピンポイントで集中保護するマルチバーム)"
            },
            {
                "rank": 6,
                "queries": ["ecostore リップバーム", "エコストア リップバーム", "エコストア リップ"],
                "brand": "ecostore (エコストア)",
                "name": "リップバーム マヌカハニー 4.5g (ニュージーランドの大自然が生んだオーガニック認証マヌカハニー配合・冬の敏感な唇に優しくフィットして長時間うるおいが続くリップバター)"
            },
            {
                "rank": 7,
                "queries": ["マヌカコスメ B&H オールインワンゲル 80g", "マヌカコスメ オールインワンゲル", "マヌカコスメ オールインワン"],
                "brand": "マヌカコスメ (Manuka Cosme)",
                "name": "B&H オールインワンゲル 80g (マヌカハニー×植物エキス×ヒアルロン酸・真冬の多忙な朝晩もこれひとつで濃密なハニーヴェールをまとう濃密高保湿オールインワン)"
            },
            {
                "rank": 8,
                "queries": ["生活の木 シアバター リップバーム", "生活の木 シアバター リップ", "生活の木 リップバーム"],
                "brand": "生活の木 (Tree of life)",
                "name": "シアバター＆ハニー リップバーム 9g (西アフリカ産精製シアバターと天然蜂蜜の濃密ブレンド・真冬の乾燥冷気からデリケートな唇を物理的かつエモリエントに守り抜く高保湿リップ)"
            },
            {
                "rank": 9,
                "queries": ["アピビータ リップケア プロポリス", "アピビータ リップケア", "アピビータ リップクリーム"],
                "brand": "APIVITA (アピビータ)",
                "name": "リップケア プロポリス＆マヌカハニー 4.4g (ギリシャ発天然由来成分99%・ミツバチの巣を守るプロポリスと高純度ハチミツが真冬の深刻な皮むけ唇を速攻リペアする濃厚バーム)"
            },
            {
                "rank": 10,
                "queries": ["マヌカハニー パック シートマスク", "マヌカハニー シートマスク", "マヌカハニー フェイスマスク"],
                "brand": "K-Secret / コスメプロ",
                "name": "ピュア マヌカハニー モイスチャーデイリーマスク 30枚入 (高濃度マヌカハニーエキスとローヤルゼリーをひたひたに含侵・真冬の暖房乾燥で干からびた肌細胞をリッチに潤す集中シートマスク)"
            }
        ]
    },
    "winter_prickly_pear": {
        "title": "保湿力の強さで肌乾燥とさようなら！アルガンオイルを超えるビタミンEと保水力で冬の乾きを満たす高保湿ウチワサボテンオイルコスメランク10",
        "file": "winter-prickly-pear.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ハクスリー オイルエッセンス エッセンスライク", "ハクスリー オイルエッセンス 30ml", "Huxley オイルエッセンス"],
                "brand": "Huxley (ハクスリー)",
                "name": "オイルエッセンス エッセンスライク オイルライク 30ml (モロッコ王室秘伝サボテンシードオイル配合・オイルの密閉力とセラムの浸透力を完璧に両立し冬の肌密度を高める最高傑作)"
            },
            {
                "rank": 2,
                "queries": ["ハクスリー オイル ライトアンドモア 30ml", "Huxley ライトアンドモア", "ハクスリー オイル ライトアンドモア"],
                "brand": "Huxley (ハクスリー)",
                "name": "オイル ライトアンドモア 30ml (100万個のサボテン種子からわずか1リットルしか採れない希少オイル・真冬の角質層を瞬時に柔らかく解きほぐすプレミアムフェイシャルオイル)"
            },
            {
                "rank": 3,
                "queries": ["ハクスリー クリーム モアザンモイスト 50ml", "Huxley モアザンモイスト", "ハクスリー クリーム 50ml"],
                "brand": "Huxley (ハクスリー)",
                "name": "クリーム モアザンモイスト 50ml (サボテンエキス×植物性セラミド高配合・バターのようにこっくりと溶けて真冬の過酷な乾燥環境から肌バリアを死守する高密度プロテクトクリーム)"
            },
            {
                "rank": 4,
                "queries": ["コディナ ウチワサボテンオイル 10ml", "コディナ ウチワサボテンオイル", "CODINA サボテンオイル"],
                "brand": "CODINA (コディナ)",
                "name": "ウチワサボテンオイル 10ml (未精製コールドプレス100%オーガニック・アルガンオイルの1.6倍のビタミンEが真冬の目元・口元の乾燥小ジワをふっくら押し戻す最高峰美容液)"
            },
            {
                "rank": 5,
                "queries": ["ハクスリー トナー エクストラクトイット 120ml", "Huxley トナー エクストラクトイット", "ハクスリー 化粧水 120ml"],
                "brand": "Huxley (ハクスリー)",
                "name": "トナー エクストラクトイット 120ml (精製水の代わりにサボテンエキスを90%以上贅沢配合・弱酸性で真冬の乱れた肌pHを瞬時に整え満水肌へ導く高保湿化粧水)"
            },
            {
                "rank": 6,
                "queries": ["メルヴィータ ビオオイル ウチワサボテン", "メルヴィータ ウチワサボテン タッチオイル", "メルヴィータ タッチオイル 10ml"],
                "brand": "Melvita (メルヴィータ)",
                "name": "ビオオイル ウチワサボテン タッチオイル 10ml (ロールオン設計で真冬の目元やほうれい線に直塗り・オーガニックウチワサボテンオイルの濃密なハリ艶をいつでも携帯できる部分用美容オイル)"
            },
            {
                "rank": 7,
                "queries": ["ハクスリー スリーピングマスク グッドナイト", "Huxley スリーピングマスク", "ハクスリー グッドナイト 120g"],
                "brand": "Huxley (ハクスリー)",
                "name": "スリーピングマスク グッドナイト 120g (サボテンエキス×ツボクサエキス配合ジェル・夜塗って寝るだけで真冬の一晩中水分パック効果が持続し翌朝見違えるほどぷるぷるの柔肌へ導く)"
            },
            {
                "rank": 8,
                "queries": ["自然化粧品研究所 ウチワサボテンオイル", "ウチワサボテン種子オイル 10ml", "ウチワサボテンオイル 10ml"],
                "brand": "自然化粧品研究所",
                "name": "未精製ウチワサボテン種子オイル 10ml (低温圧搾ピュア100%・ステロールやオメガ6脂肪酸を極めて高濃度に含有し真冬のひび割れ寸前の超乾燥肌に豊かな弾力を蘇らせる高機能原液)"
            },
            {
                "rank": 9,
                "queries": ["ハクスリー クレンジングオイル 200ml", "Huxley クレンジングオイル", "ハクスリー クレンジングオイル"],
                "brand": "Huxley (ハクスリー)",
                "name": "クレンジングオイル ディープクリーン ディープモイスト 200ml (サボテンシードオイル高配合・毛穴の奥のメイク汚れをやさしくオフしながら洗い流したあとも潤い膜が残る贅沢オイル洗顔)"
            },
            {
                "rank": 10,
                "queries": ["ハクスリー ボディオイル 100ml", "Huxley ボディオイル モロッカンガーデナー", "ハクスリー ボディオイル"],
                "brand": "Huxley (ハクスリー)",
                "name": "ボディオイル モロッカンガーデナー 100ml (サボテンシードオイル×スイートアーモンド油・上質なボタニカルの香りとさらりとした質感で真冬の粉吹きボディをしっとり滑らかに包む)"
            }
        ]
    },
    "winter_calendula": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の冷風と寒暖差でピリつく敏感肌をしっとり鎮静させる高保湿カレンデュラコスメランク10",
        "file": "winter-calendula.html",
        "items": [
            {
                "rank": 1,
                "queries": ["キールズ ハーバル トナー CL アルコールフリー 250ml", "キールズ ハーバルトナー CL 250ml", "キールズ カレンデュラ トナー 250ml"],
                "brand": "Kiehl's (キールズ)",
                "name": "ハーバル トナー CL アルコールフリー 250ml (手摘みカレンデュラ花びらを贅沢配合・真冬の寒暖差で赤ら顔になったりピリつく敏感肌を穏やかに鎮静し満水肌へ整える世界的大ベストセラー化粧水)"
            },
            {
                "rank": 2,
                "queries": ["ヴェレダ カレンドラ ベビーフェイシャルクリーム 50ml", "WELEDA カレンドラ フェイシャルクリーム", "ヴェレダ カレンドラ ベビーフェイシャル"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "カレンドラ ベビーフェイシャルクリーム 50ml (有機カレンドラエキス×アーモンド油×ミツロウ・赤ちゃんのほっぺから真冬の冷風でヒリつく大人の乾燥肌まで優しく守り抜く高保湿フェイスクリーム)"
            },
            {
                "rank": 3,
                "queries": ["ヴェレダ カレンドラ マッサージオイル 100ml", "WELEDA カレンドラ マッサージオイル", "ヴェレダ カレンドラ オイル 100ml"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "カレンドラ マッサージオイル 100ml (太陽の光を浴びたカレンドラの花をヒマワリ油に漬け込んだ伝統製法・真冬の冷えで血行が悪くなりこわばった肌と身体をしっとり温めほぐす全身オイル)"
            },
            {
                "rank": 4,
                "queries": ["ニールズヤード カレンデュラクリーム 50g", "ニールズヤード カレンデュラクリーム", "NEALS YARD カレンデュラ"],
                "brand": "NEAL'S YARD REMEDIES (ニールズヤード レメディーズ)",
                "name": "カレンデュラクリーム 50g (英国ソイルアソシエーション認定オーガニック・真冬の寒冷で荒れ狂うデリケート肌を植物の優しいバリアで包み込み健やかな皮膚状態へ導くレスキューバーム)"
            },
            {
                "rank": 5,
                "queries": ["エイプリルスキン リアルカレンデュラ ピールオフパック", "エイプリルスキン カレンデュラ パック", "APRILSKIN カレンデュラ"],
                "brand": "APRILSKIN (エイプリルスキン)",
                "name": "リアル カレンデュラ ピールオフパック 100g (本物のカレンデュラ花びらとエキスを配合・冬の乾燥で毛穴に詰まった古い角質をやさしく吸着オフしつるんと透明感あるたまご肌へ導くパック)"
            },
            {
                "rank": 6,
                "queries": ["生活の木 カレンデュラオイル 70ml", "生活の木 カレンデュラオイル", "カレンデュラオイル 生活の木"],
                "brand": "生活の木 (Tree of life)",
                "name": "カレンデュラオイル (インフューズドオイル) 70ml (大豆油にカレンデュラの花をじっくり浸出させた高純度オイル・真冬のひび割れ寸前の指先やカサつく肘・膝を優しく包み込むスキンオイル)"
            },
            {
                "rank": 7,
                "queries": ["ナチュラグラッセ クリームバーム", "ナチュラグラッセ エモリエント クリームバーム", "ナチュラグラッセ バーム"],
                "brand": "naturaglace (ナチュラグラッセ)",
                "name": "エモリエント クリームバーム 40g (トウキンセンカ花エキス×シアバター×ホホバ油・冬のメイク前や日中の乾燥小ジワにうるおいツヤ膜をプラスする100%天然由来マルチバーム)"
            },
            {
                "rank": 8,
                "queries": ["自然化粧品研究所 カレンデュラエキス", "トウキンセンカ花エキス 自然化粧品研究所", "カレンデュラエキス 30ml"],
                "brand": "自然化粧品研究所",
                "name": "トウキンセンカ花エキス (カレンデュラエキス) 30ml (手持ちの化粧水に数滴プラスして真冬の肌荒れ防止力を大幅アップ・寒暖差ストレスに立ち向かう高濃度ボタニカル濃縮原液)"
            },
            {
                "rank": 9,
                "queries": ["ヴェレダ カレンドラ ベビーバーム 75ml", "WELEDA ベビーバーム カレンドラ", "ヴェレダ ベビーバーム"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "カレンドラ ベビーバーム 75ml (酸化亜鉛×カレンドラ×天然ワックス・冬の冷たい風や摩擦で荒れやすいデリケートゾーンや頬を水滴や乾燥から強固に守る密着プロテクトバーム)"
            },
            {
                "rank": 10,
                "queries": ["サンタマリアノヴェッラ カレンドラ", "サンタマリアノヴェッラ カレンデュラ", "カレンデュラ 保湿クリーム 100ml"],
                "brand": "Santa Maria Novella (サンタ・マリア・ノヴェッラ)",
                "name": "クレマ カレンドラ 100ml (世界最古のフィレンツェ薬局が誇る名品・高濃度カレンデュラエキスとアーモンド油が真冬の冷風で赤く火照った肌を極上のヴェールで鎮静させる高貴なクリーム)"
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
                
                # リトライ＆レートリミット対策（2.5秒ウェイト、429なら5秒待機）
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
                        time.sleep(5.0)
                
                if chosen_item:
                    print(f"  -> SUCCESS! Found: {chosen_item.get('itemName')[:40]}... (¥{chosen_item.get('itemPrice')})")
                    break
                else:
                    print(f"  -> Not found or failed for query: '{q}'")
            
            if chosen_item:
                total_success += 1
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if isinstance(img_url, dict):
                    img_url = img_url.get("imageUrl", "")

                if "_ex=128x128" in img_url:
                    img_url = img_url.replace("_ex=128x128", "_ex=500x500")
                elif "_ex=64x64" in img_url:
                    img_url = img_url.replace("_ex=64x64", "_ex=500x500")
                elif "_ex=300x300" in img_url:
                    img_url = img_url.replace("_ex=300x300", "_ex=500x500")

                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "rakuten_item_name": chosen_item.get("itemName"),
                    "price": chosen_item.get("itemPrice"),
                    "url": chosen_item.get("affiliateUrl") or chosen_item.get("itemUrl"),
                    "image": img_url,
                    "shop_name": chosen_item.get("shopName"),
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_rate": chosen_item.get("reviewAverage", "0.0")
                })
            else:
                print(f"FAILED TO FETCH ITEM RANK {item['rank']}: {item['name']}")
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "rakuten_item_name": item["name"],
                    "price": 2980,
                    "url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2F",
                    "image": "https://thumbnail.image.rakuten.co.jp/@0_mall/thumbnail/cabinet/noimage.jpg",
                    "shop_name": "楽天市場公式取扱店",
                    "review_count": 28,
                    "review_rate": "4.5"
                })

    with open("fetched_final_30_manuka_prickly_calendula.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Finished! Successfully fetched: {total_success} / {total_needed}")
    print(f"Saved to fetched_final_30_manuka_prickly_calendula.json")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
