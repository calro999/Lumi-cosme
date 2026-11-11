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
    "winter_ceramide_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！高密度ナノセラミドと濃密マイクロファイバーシートで真冬の寒冷脱水肌を一撃で蘇らせる保湿力高めセラミドシートマスクランク10",
        "file": "winter-ceramide-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ミノン ぷるぷるしっとり肌マスク 4枚", "ミノン アミノモイスト ぷるぷるしっとり肌マスク"],
                "brand": "MINON Amino Moist (ミノン アミノモイスト)",
                "name": "ぷるぷるしっとり肌マスク 4枚入 (9種の保潤アミノ酸×2種の清透アミノ酸×浸透ナノセラミド・敏感肌を濃密ゼリー美容液で満たす冬の救世主)"
            },
            {
                "rank": 2,
                "queries": ["キュレル 潤浸保湿 モイストリペアシートマスク", "キュレル シートマスク 4枚"],
                "brand": "Curel (キュレル / 花王)",
                "name": "潤浸保湿 モイストリペアシートマスク 4枚入 (医薬部外品・消炎剤有効成分×セラミド機能成分配合・ひび割れそうな粉吹き冬肌を隙間なく覆う切り込みシート)"
            },
            {
                "rank": 3,
                "queries": ["トリデン ソリッドイン セラミド マスク", "トリデン セラミド マスク", "Torriden セラミド シートマスク"],
                "brand": "Torriden (トリデン)",
                "name": "ソリッドイン セラミド マスク 10枚入 (5D複合セラミド×パンテノール・ビーガンマイクロファイバーシートが角層の奥まで高密度保湿ヴェールを形成)"
            },
            {
                "rank": 4,
                "queries": ["ドクタージャルト セラマイディン マスク", "Dr.Jart+ セラマイディン フェイシャルマスク", "セラマイディン シートマスク"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "セラマイディン スキンバリア モイスチャライジング マスク 5枚入 (5種複合セラミド×パンテノール・超極細セルロースシートが真冬の砂漠肌を完全密閉)"
            },
            {
                "rank": 5,
                "queries": ["ダーマレーザー スーパーセラミド100 マスク", "ダーマレーザー セラミド100 7枚", "クオリティファースト セラミド100"],
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー スーパー CERAMIDE100 マスク 7枚入 (高濃度天然ナノセラミド×ナノカプセル浸透技術・シリコンマスク発想の高密着シートで真冬のバリア再建)"
            },
            {
                "rank": 6,
                "queries": ["ルルルン プレシャス RED 32枚", "ルルルンプレシャス RED モイスト"],
                "brand": "LuLuLun (ルルルン)",
                "name": "ルルルンプレシャス RED モイスト 32枚入 (コメセラミド×発酵酵母エキス×L22・冬のゴワつく大人の乾燥肌をふっくらほぐす超極厚ふっくらシート)"
            },
            {
                "rank": 7,
                "queries": ["KISO フェイスマスク セラミド 30枚", "KISO セラミド パック", "KISO ヒト型セラミド シートマスク"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "プレミアムフェイスマスク セラミド 30枚入 (ヒト型セラミド5種高配合原液×高密着コットン100%シート・冬のデイリーケアで揺らがない高保水肌へ)"
            },
            {
                "rank": 8,
                "queries": ["VT CICA セラミド カプセル マスク", "VT CICA カプセルマスク 10個", "VT CICA バイタル マスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "CICA セラミド カプセル マスク 10個入 (独自シカヒアルロン×セラミドNP・冷気で赤みが出た冬の敏感肌を鎮静＆高保水クレイパックで滑らかリセット)"
            },
            {
                "rank": 9,
                "queries": ["メディヒール N.M.F アクア アンプルマスク 10枚", "メディヒール NMF アンプルマスク"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "THE N.M.F アンプルマスク 10枚入 (8重ヒアルロン酸×セラミドNP×ハマメリス水・特許ハイドロゲルコットンシートが水分を抱え込み逃さない)"
            },
            {
                "rank": 10,
                "queries": ["毛穴撫子 お米のマスク 10枚", "お米のマスク 10枚入"],
                "brand": "毛穴撫子 (石澤研究所)",
                "name": "お米のマスク 10枚入 (100%国産米由来ライスセラミド×米発酵液・冬の乾燥でぽっかり開いたカサつき毛穴をキュッと密閉ふっくら肌へ)"
            }
        ]
    },
    "winter_lip_sleeping_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10",
        "file": "winter-lip-sleeping-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ラネージュ リップスリーピングマスク ベリー 20g", "ラネージュ リップスリーピングマスク 20g"],
                "brand": "LANEIGE (ラネージュ)",
                "name": "リップスリーピングマスク ベリー 20g (ベリーフルーツコンプレックス×ビタミンC×シアバター・睡眠中に古い角質を優しく溶かし翌朝ぷるんとした赤ちゃん唇へ)"
            },
            {
                "rank": 2,
                "queries": ["トリデン ソリッドイン セラミド リップエッセンス", "Torriden セラミド リップ"],
                "brand": "Torriden (トリデン)",
                "name": "ソリッドイン セラミド リップエッセンス 11mL (5D複合セラミド×ホホバ種子油×フルボ酸・厚塗りパックで真冬のひび割れ皮剥け唇を即効シールド)"
            },
            {
                "rank": 3,
                "queries": ["ケアネル リップ ナイト モイスチャー マスク 5g", "CARE:NEL リップ スリーピング マスク"],
                "brand": "CARE:NEL (ケアネル)",
                "name": "リップ ナイト モイスチャー マスク 5g (天然ベリーエキス×マイクロクリスタリンワックス・寝ている間の乾燥から唇を守り抜く高密着リップパック)"
            },
            {
                "rank": 4,
                "queries": ["CNP プロポリス リップスリーピングマスク", "CNP リップ バーム プロポリス"],
                "brand": "CNP Laboratory (シーエヌピー)",
                "name": "プロポリス リップスリーピングマスク 15g (高濃縮プロポリスエキス×ハチミツエキス・真冬の栄養不足でしぼんだ唇に濃厚な弾力蜜ツヤを与える)"
            },
            {
                "rank": 5,
                "queries": ["キュレル リップケアバーム 4.2g", "キュレル リップケア バーム"],
                "brand": "Curel (キュレル / 花王)",
                "name": "リップケアバーム 4.2g (医薬部外品・消炎剤有効成分×セラミド機能カプセル配合・夜の濃厚パック処方でひび割れ荒れを繰り返す唇を集中補修)"
            },
            {
                "rank": 6,
                "queries": ["タカミ リップ 7g", "タカミリップ 美容液"],
                "brand": "TAKAMI (タカミ)",
                "name": "タカミリップ 7g (唇用美肌美容液・角質ケア×保湿・夜塗れば摩擦や乾燥で荒れた唇の代謝を促しふっくら澄んだピンク色へ導く)"
            },
            {
                "rank": 7,
                "queries": ["オバジ ダーマパワーX リップエッセンス 10g", "オバジ リップエッセンス 10g"],
                "brand": "Obagi (オバジ / ロート製薬)",
                "name": "ダーマパワーX セラム リップエッセンス 10g (ビタミンA誘導体×エラスチン×コラーゲン・冬の縦ジワが気になるしぼみ唇をふっくらボリュームアップ)"
            },
            {
                "rank": 8,
                "queries": ["クラランス リップコンフォートオイル 7ml", "クラランス コンフォート オイル"],
                "brand": "CLARINS (クラランス)",
                "name": "リップ コンフォート オイル 7mL (オーガニックホホバ×ヘーゼルナッツ×ローズヒップ・植物オイルの贅沢な濃密オイルパックで冬の唇をリッチに保護)"
            },
            {
                "rank": 9,
                "queries": ["チューシー リップパック 20枚", "CHOOSY ハイドロゲル リップパック"],
                "brand": "CHOOSY (チューシー)",
                "name": "ハイドロゲル リップパック 20枚入 (高密着ハイドロゲルシート×ヒアルロン酸×セラミド・密閉浸透でカサつく唇に集中水分チャージする専用マスク)"
            },
            {
                "rank": 10,
                "queries": ["DHC 薬用リップクリーム 1.5g", "DHC 薬用 リップ"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用リップクリーム 1.5g (医薬部外品・オリーブバージンオイル×アロエエキス×ビタミンE・人間の皮脂に酷似した密着保護膜で冬の唇荒れを強力予防)"
            }
        ]
    },
    "winter_barrier_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！微細リポソーム化バリア成分とパンテノールの生体浸透力で真冬の暖房インナードライを芯から鎮静する保湿力高めバリア美容液ランク10",
        "file": "winter-barrier-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エストラ アトバリア365 ハイドロエッセンス 150ml", "エストラ アトバリア365 エッセンス"],
                "brand": "AESTURA (エストラ)",
                "name": "アトバリア365 ハイドロエッセンス 150mL (30種のアミノ酸×天然保湿因子NMF・高濃縮乳液状エッセンスが肌深部にバリア水分を満たす先行美容液)"
            },
            {
                "rank": 2,
                "queries": ["トリデン ソリッドイン セラミド エッセンス 100ml", "トリデン ソリッドイン エッセンス"],
                "brand": "Torriden (トリデン)",
                "name": "ソリッドイン セラミド オールインワン エッセンス 100mL (5D複合セラミド×パンテノール・とろみのある高保湿テクスチャーで真冬のインナードライを即効改善)"
            },
            {
                "rank": 3,
                "queries": ["dプログラム カンダンバリア エッセンス 40ml", "dプログラム カンダンバリア"],
                "brand": "d program (資生堂 dプログラム)",
                "name": "カンダンバリア エッセンス 40mL (寒暖差による乾燥トラブルに着目・カンダンバリアコンプレックス配合で冬のゆらぎ肌を整える薬用導入美容液)"
            },
            {
                "rank": 4,
                "queries": ["リアルバリア エクストリーム エッセンス トナー 190ml", "リアルバリア エッセンストナー"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "エクストリーム エッセンス トナー 190mL (特許MLE液晶バリア構造×5種のヒアルロン酸・美容液と化粧水の機能を併せ持つ高保湿バリアアンプルローション)"
            },
            {
                "rank": 5,
                "queries": ["キュレル 潤浸保湿 浸透モイスト美容液 40g", "キュレル 浸透モイスト美容液"],
                "brand": "Curel (キュレル / 花王)",
                "name": "潤浸保湿 浸透モイスト美容液 40g (医薬部外品・セラミド機能成分×生姜エキス・冬の乾燥小ジワが目立つ目元口元をみずみずしく潤す薬用美容液)"
            },
            {
                "rank": 6,
                "queries": ["アヌア ドクダミ 80 水分鎮静アンプル 30ml", "Anua ドクダミ アンプル 30ml"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 80% 水分鎮静アンプル 30mL (高濃度ドクダミエキス80%×パンテノール×ヒアルロン酸・真冬の暖房熱による赤みやほてりを鎮静する水分セラム)"
            },
            {
                "rank": 7,
                "queries": ["COSRX プロポリス ライト アンプル 30ml", "COSRX プロポリス アンプル"],
                "brand": "COSRX (コスアールエックス)",
                "name": "フルフィット プロポリス ライト アンプル 30mL (黒蜂プロポリスエキス83.25%×天然保湿因子・冬の寒風で疲弊した肌に蜜のような濃密なツヤとバリアを補給)"
            },
            {
                "rank": 8,
                "queries": ["SKIN1004 センテラ アンプル 55ml", "スキン1004 センテラ アンプル 55ml"],
                "brand": "SKIN1004 (スキンワンオーオーフォー)",
                "name": "マダガスカル センテラ アンプル 55mL (高純度マダガスカル産ツボクサエキス100%・冬の過酷な外気でバリアが乱れた肌を鎮静＆バリア再建へと導く)"
            },
            {
                "rank": 9,
                "queries": ["ドクタージャルト セラマイディン リキッド 150ml", "セラマイディン リキッド トナー"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "セラマイディン スキンバリア セラム トナー 150mL (5種の複合セラミド×パンテノール・濃密リキッドが肌に触れた瞬間に素早く浸透しバリア膜を形成)"
            },
            {
                "rank": 10,
                "queries": ["ワンバイコーセー セラム ヴェール 60ml", "セラムヴェール ディープリペア 60ml"],
                "brand": "ONE BY KOSÉ (コーセー)",
                "name": "セラム ヴェール ディープリペア 60mL (医薬部外品 有効成分ライスパワーNo.11配合・肌自らのセラミドを生み出す力を改善する冬の日本代表薬用導入美容液)"
            }
        ]
    }
}

def extract_image_url(cand):
    # mediumImageUrls or smallImageUrls
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    if isinstance(first, dict):
        raw = first.get("imageUrl", "")
    else:
        raw = str(first)
    
    # 400x400に高解像度化
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

def fetch_all():
    results = {}
    total_fetched = 0
    total_expected = 30
    
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title'][:35]}...)")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Rank {item['rank']}: Trying query '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                try:
                    time.sleep(2.0)
                    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
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
                except urllib.error.HTTPError as e:
                    print(f"    HTTP Error {e.code}: {e.reason}")
                    time.sleep(3.0)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(2.5)
            
            if chosen_item:
                img_url = extract_image_url(chosen_item)
                print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                print(f"     Image URL: {img_url}")
                
                aff_url = chosen_item.get("affiliateUrl") or chosen_item.get("itemUrl")
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": aff_url,
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "4.8"))
                })
                total_fetched += 1
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_mask_lip_serum.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_mask_lip_serum.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print(f"⚠️ Warning: Only {total_fetched}/30 items fetched.")

if __name__ == "__main__":
    fetch_all()
