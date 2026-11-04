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
    "winter_resurrection_plant": {
        "title": "保湿力の強さで肌乾燥とさようなら！カラカラ砂漠肌を驚異の保水力で満たす復活草・トレハロースコスメランク10",
        "file": "winter-resurrection-plant.html",
        "items": [
            {
                "rank": 1,
                "queries": ["abib 復活草クリーム 75ml", "Abib 復活草 クリーム"],
                "brand": "Abib (アビブ)",
                "name": "復活草クリーム ニュートリションチューブ 75ml (極限の砂漠でも自活する復活草の生命力を凝縮・冬の乾燥でしぼんだ角層を濃密な水分と栄養で満たす高保湿バリアクリーム)"
            },
            {
                "rank": 2,
                "queries": ["Abib 復活草ビフィダセラム", "アビブ 復活草 エッセンス", "Abib 復活草セラム"],
                "brand": "Abib (アビブ)",
                "name": "復活草ビフィダセラム ファーミングドロップ 50ml (復活草エキス×ビフィズス菌発酵液・真冬の寒冷で弾力を失った肌深層へ水分を巡らせキメを整える濃密弾力エッセンス)"
            },
            {
                "rank": 3,
                "queries": ["オルビスユー エッセンスローション 180mL 本体", "オルビスユー エッセンスローション 180ml"],
                "brand": "ORBIS (オルビス)",
                "name": "オルビスユー エッセンスローション 180ml (独自高保湿成分MCアクアポリン×トレハロース配合・真冬のとろぱしゃ濃密浸透で角層細胞のすみずみまで満水状態を保つ名品化粧水)"
            },
            {
                "rank": 4,
                "queries": ["キラ アクティブローション 150ml", "綺羅化粧品 アクティブローション", "オルビスユー ジェルモイスチャライザー 50g"],
                "brand": "KIRA (綺羅化粧品)",
                "name": "キラ アクティブローション 150ml (トレハロース×天然植物保湿エキス高配合・冬の寒風で乱れた角層ラメラ構造を整え潤いを長時間離さない高保湿化粧水)"
            },
            {
                "rank": 5,
                "queries": ["VT シカコラーゲンマスク 30枚", "VT コラーゲン マスク 30枚入", "VT マスク 30枚入"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "シカコラーゲンデイリーマスク 30枚入 (復活草エキス×低分子コラーゲン×CICA・朝晩の密着シートで真冬のエアコン乾燥を打破しぷるぷる満水肌へ導く大容量パック)"
            },
            {
                "rank": 6,
                "queries": ["松山油脂 肌をうるおす保湿浸透水 モイストリッチ 120ml", "松山油脂 肌をうるおす 保湿浸透水"],
                "brand": "松山油脂 (M-mark)",
                "name": "肌をうるおす保湿浸透水 モイストリッチ 120ml (大豆由来保湿成分×5種のヒト型セラミド×トレハロース・とろみのある感触で真冬の荒れた角層をしっとり潤す低刺激化粧水)"
            },
            {
                "rank": 7,
                "queries": ["魔女工場 ビフィダバイオームコンセントレートクリーム", "魔女工場 ビフィダ バイオーム コンセントレート クリーム"],
                "brand": "Manyo Factory (魔女工場)",
                "name": "ビフィダバイオーム コンセントレート クリーム 50ml (ビフィズス菌培養溶解質×復活草ペプチド×10重ヒアルロン酸・真冬の過酷な寒さに立ち向かう高栄養シールドクリーム)"
            },
            {
                "rank": 8,
                "queries": ["ミシャ グロウ スキンバーム 50ml", "MISSHA 水分クリーム グロウ"],
                "brand": "MISSHA (ミシャ)",
                "name": "グロウ スキンバーム 50ml (ダマスクローズ水×復活草由来トレハロース・朝のメイク前に塗るだけで一日中みずみずしいツヤをキープする水分パック下地バーム)"
            },
            {
                "rank": 9,
                "queries": ["Abib ガムシートマスク 復活草", "アビブ 復活草 マスクパック 10枚", "Abib 復活草フィット"],
                "brand": "Abib (アビブ)",
                "name": "ガムシートマスクパック 復活草フィット 10枚 (マイクロファイバーシートが肌に吸い付くように密着・復活草の凝縮エッセンスが真冬の干からびた肌を集中リカバリーする救急パック)"
            },
            {
                "rank": 10,
                "queries": ["自然化粧品研究所 トレハロース 20g", "トレハロース 20g メール便可", "トレハロース パウダー"],
                "brand": "自然化粧品研究所",
                "name": "高純度トレハロースパウダー 20g (砂漠植物の細胞保護メカニズムを応用・手持ちの化粧水や乳液にサッと溶かして真冬の極度な水分蒸発を鉄壁ガードするマルチ保水パウダー)"
            }
        ]
    },
    "winter_beta_glucan": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える水分保持力で冬のバリアを立て直す高保湿ベータグルカンコスメランク10",
        "file": "winter-beta-glucan.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ランコム ジェニフィック アルティメ セラム 30mL", "ランコム ジェニフィック アルティメ セラム", "ランコム ジェニフィック アルティメ"],
                "brand": "LANCÔME (ランコム)",
                "name": "ジェニフィック アルティメ セラム 30ml (次世代高機能成分β-グルカン配合・冬の過酷な寒冷ストレスと乾燥によるダメージを秒速で修復する最高峰美肌ステディセラム)"
            },
            {
                "rank": 2,
                "queries": ["スパトリートメント βエッセンス 300ml", "スパトリートメント βエッセンス", "ウェーブ スパトリートメント βエッセンス"],
                "brand": "Spa treatment (スパトリートメント)",
                "name": "βエッセンス 300ml (高純度スエヒロタケ由来β-グルカンを贅沢配合・サロン業務用大容量で真冬の顔からデコルテまで濃密な保水クッションで包み込むプロ用美容液)"
            },
            {
                "rank": 3,
                "queries": ["アイユニーク ベータグルカン パワーモイスチャーセラム 50ml", "ベータグルカン セラム アイユニーク", "ベータグルカンセラム 韓国"],
                "brand": "iUNIK (アイユニック)",
                "name": "ベータグルカン パワーモイスチャー セラム 50ml (ヒアルロン酸より20%高い水分保持力を持つ100%純粋酵母β-グルカン・真冬の極度な乾燥とバリア破綻を鎮静する名作水分セラム)"
            },
            {
                "rank": 4,
                "queries": ["リアルバリア エクストリームクリーム 50ml", "リアルバリア エクストリーム クリーム 50ml"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "エクストリームクリーム 50ml (特許MLE独自セラミド×β-グルカン×アラントイン・真冬の寒冷で崩壊した角層ラメラ構造を完璧に再建する超高保湿バリアリペアクリーム)"
            },
            {
                "rank": 5,
                "queries": ["ガラクトミセス β-グルカン 美容液 30mL", "ガラクトミセス βーグルカン配合美容液", "ガラクトミセス β-グルカン"],
                "brand": "自然化粧品研究所 / ナチュラス",
                "name": "ガラクトミセス×β-グルカン配合美容液 30ml (天然発酵ガラクトミセスと高保水β-グルカンの黄金比・冬のくすみと乾燥ゴワつきを解きほぐし透明感あふれるモチ肌へ導く濃密セラム)"
            },
            {
                "rank": 6,
                "queries": ["ドクタージー レッド ブレミッシュ クリア スージング クリーム 70ml", "Dr.G レッド ブレミッシュ クリア スージング クリーム"],
                "brand": "Dr.G (ドクタージー)",
                "name": "レッドブレミッシュ クリアスージングクリーム 70ml (10-CICA×高純度β-グルカン配合・冬の寒暖差で赤みや痒みが出やすい敏感ゆらぎ肌を冷やし潤す水分鎮静シカクリーム)"
            },
            {
                "rank": 7,
                "queries": ["KISO ヒト型セラミド原液 10％配合", "KISO CARE ヒト型セラミド原液", "KISO 美容液 セラミド"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "キソ ヒトミドエッセンス X 20ml (高濃度ヒト型セラミド5種×植物性β-グルカン・真冬の冷気でスカスカになった角層細胞の隙間を埋め尽くす濃厚バリア美容液)"
            },
            {
                "rank": 8,
                "queries": ["魔女工場 パンテトイン クリーム 80ml", "manyo パンテトインクリーム80mL"],
                "brand": "Manyo Factory (魔女工場)",
                "name": "パンテトイン ディープモイスチャークリーム 80ml (パンテノール×エクトイン×β-グルカン高配合・真冬の砂漠肌を200時間しっとり包み込む超濃厚リッチバームクリーム)"
            },
            {
                "rank": 9,
                "queries": ["Anua ドクダミ 77 スージングトナー 250ml", "アヌア ドクダミ 77 スージングトナー 250ml"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 77% スージングトナー 250ml (ドクダミエキス×植物性β-グルカン×ヒアルロン酸・冬の乾燥ニキビや赤みを鎮静させながらサラリと角層深部を潤す低刺激化粧水)"
            },
            {
                "rank": 10,
                "queries": ["イニスフリー グリーンティーシード セラム 80ml", "INNISFREE グリーンティーシード ヒアルロン セラム"],
                "brand": "innisfree (イニスフリー)",
                "name": "グリーンティーシード ヒアルロン セラム 80ml (緑茶乳酸菌発酵溶解質×ナノカプセルヒアルロン酸×β-グルカン・冬の洗顔後3秒で肌の水分バリアをチャージする名品ブースター導入美容液)"
            }
        ]
    },
    "winter_avocado": {
        "title": "保湿力の強さで肌乾燥とさようなら！ガサガサ粉吹き肌をとろける柔軟膜で包み込む濃厚アボカドコスメランク10",
        "file": "winter-avocado.html",
        "items": [
            {
                "rank": 1,
                "queries": ["キールズ アイトリートメント AV 14g", "キールズ アボカド アイクリーム 14g", "キールズ KIEHLS アイトリートメント"],
                "brand": "Kiehl's (キールズ)",
                "name": "アイトリートメント AV (アボカド アイクリーム) 14g (森のバター・アボカドオイル高配合・指先で温めるとみずみずしく崩れて真冬の目元のちりめんジワをふっくら満たす世界的ベストセラー)"
            },
            {
                "rank": 2,
                "queries": ["コスメデコルテ プリム ラテ ハーバル ミルク 150mL", "コスメデコルテ プリムラテ 150ml"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "プリム ラテ ハーバル ミルク 150ml (森のバターと呼ばれるアボカドオイルをはじめとする植物オイルを贅沢にブレンド・真冬の硬直した肌を解きほぐし毛穴の目立たないふっくら柔肌へ整える先行乳液)"
            },
            {
                "rank": 3,
                "queries": ["キールズ スキン ハイドレーション マスク 100g", "キールズ アボカド マスク 100g"],
                "brand": "Kiehl's (キールズ)",
                "name": "スキン ハイドレーション マスク 100g (完熟アボカド果実エキス×アボカドオイル配合・まるで本物のアボカドをすり潰したようなリッチなペーストが冬の極度な乾燥肌を集中レスキューする洗い流すパック)"
            },
            {
                "rank": 4,
                "queries": ["生活の木 アボカドオイル 25mL", "生活の木 アボカドオイル 70ml"],
                "brand": "生活の木 (Tree of Life)",
                "name": "有機アボカドオイル 25ml (低温圧搾オーガニック100%未精製・オレイン酸やビタミンEが豊富で真冬の肘・かかと・ひび割れ寸前の超乾燥肌をしっとり保護する濃厚植物オイル)"
            },
            {
                "rank": 5,
                "queries": ["スキンフード アボカド スティック リップバーム", "SKINFOOD アボカド リップバーム"],
                "brand": "SKINFOOD (スキンフード)",
                "name": "アボカド スティック リップバーム 3.4g (高純度アボカドオイルとセラミド配合・真冬の冷風で皮むけした唇にとろけるように馴染み長時間しっとり膜をキープする高保湿リップ)"
            },
            {
                "rank": 6,
                "queries": ["スキンフード アボカド&シュガー", "SKINFOOD アボカド スクラブ"],
                "brand": "SKINFOOD (スキンフード)",
                "name": "アボカド＆シュガー リップスクラブ (天然アボカドオイル×微細ブラウンシュガー・真冬のガサガサ角質を優しくオフしながら濃厚な油分膜でぷるぷるに仕上げるリップスクラブ)"
            },
            {
                "rank": 7,
                "queries": ["&SH アボカドオイル 100ml", "アボカドオイル 100ml 精製"],
                "brand": "自然化粧品本舗 (&SH)",
                "name": "精製アボカドオイル 100ml (天然アボカド果肉から抽出・肌への親和性が極めて高いオレイン酸が角質層を柔らかく整え真冬の粉吹き肌をしっとり落ち着かせるマルチケアオイル)"
            },
            {
                "rank": 8,
                "queries": ["ロクシタン シアリッチ リップバーム スティック", "ロクシタン シア リップバーム スティック 4.5g"],
                "brand": "L'OCCITANE (ロクシタン)",
                "name": "シアリッチ リップバーム 4.5g (オーガニックシアバター×アボカドオイル配合・真冬の木枯らしでガサガサに荒れた唇をとろけるように潤してぷるぷるに保つ濃密リップケア)"
            },
            {
                "rank": 9,
                "queries": ["マンダム バリアリペア シートマスク なめらか 5枚", "バリアリペア シートマスク なめらか"],
                "brand": "Barrier Repair (マンダム バリアリペア)",
                "name": "シートマスク なめらか超ふっくら 5枚入 (浸透アボカドオイル×ナノヒアルロン酸・超やわらか密着シートが真冬の毛穴開きや乾燥キメ乱れを包み込みふっくら陶器肌へ整える集中マスク)"
            },
            {
                "rank": 10,
                "queries": ["オーガニック アボカドオイル 100ml 低温圧搾", "TERRA D'OC アボカドオイル 100ml", "アボカドオイル 100ml"],
                "brand": "TERRA D'OC",
                "name": "オーガニック アボカドオイル 100ml (未精製コールドプレス製法・緑豊かなアボカド本来のビタミン・ミネラルが真冬のガサガサ角質を驚くほど柔らかく包み込む高純度エモリエントオイル)"
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
                
                for attempt in range(2):
                    try:
                        time.sleep(2.0)
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
                        print(f"  Attempt {attempt+1} failed: {e}")
                        time.sleep(2.5)
                if chosen_item:
                    print(f"  ✓ Found product: {chosen_item['itemName'][:40]}... (¥{chosen_item['itemPrice']:,})")
                    break
            
            if chosen_item:
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if isinstance(img_url, dict):
                    img_url = img_url.get("imageUrl", "")
                
                # 画像を高解像度化
                if "_ex=128x128" in img_url:
                    img_url = img_url.replace("_ex=128x128", "_ex=500x500")
                elif "_ex=64x64" in img_url:
                    img_url = img_url.replace("_ex=64x64", "_ex=500x500")
                elif "_ex=300x300" in img_url:
                    img_url = img_url.replace("_ex=300x300", "_ex=500x500")

                item_info = {
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "rakuten_item_name": chosen_item.get("itemName", ""),
                    "price": chosen_item.get("itemPrice", 0),
                    "url": chosen_item.get("affiliateUrl", chosen_item.get("itemUrl", "")),
                    "image": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_rate": chosen_item.get("reviewAverage", "4.5"),
                    "shop_name": chosen_item.get("shopName", "楽天市場公式ショップ")
                }
                results[cat_key]["items"].append(item_info)
                total_success += 1
            else:
                print(f"  ❌ FAILED to find item for Rank {item['rank']}: {item['name']}")

    out_file = "fetched_final_30_resurrection_beta_avocado.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items fetched successfully.")
    print(f"Saved to: {out_file}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
