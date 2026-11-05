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
    "winter_lactobacillus": {
        "title": "保湿力の強さで肌乾燥とさようなら！美肌菌を育てて自活力あるバリア膜を再建する保湿力高め乳酸菌コスメランク10",
        "file": "winter-lactobacillus.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ラクトデュウ S.E.ローション", "ヤクルト ラクトデュウ ローション", "ヤクルト ラクトデュウ"],
                "brand": "Yakult Beautiens (ヤクルト)",
                "name": "ラクトデュウ S.E.ローション2 (まろやか高保湿) 130mL (乳酸菌生まれの保湿成分S.E.シロタエッセンス配合・真冬の暖房乾燥で乱れた角層バリアを素早く整える大人気化粧水)"
            },
            {
                "rank": 2,
                "queries": ["ももぷり 潤い濃密ミルク", "ももぷり 乳液", "ももぷり 潤い濃密"],
                "brand": "momopuri (ももぷり)",
                "name": "潤い濃密ミルク 150ml (塗る乳酸菌EC-12株×桃セラミド配合・ぷりっと弾む潤い桃肌へ導く濃厚保湿乳液)"
            },
            {
                "rank": 3,
                "queries": ["バイオヒールボ プロバイオダーム リフティングクリーム", "プロバイオダーム クリーム", "プロバイオダーム 50ml"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム 3Dリフティングクリーム 50ml (特許プロバイオティクス乳酸菌発酵成分×ペプチド配合・真冬の乾燥でしぼんだ大人の肌をキュッと引き締める高保湿弾力クリーム)"
            },
            {
                "rank": 4,
                "queries": ["ラロッシュポゼ トレリアン 薬用モイスチャーローション", "ラロッシュポゼ トレリアン ローション", "ラロッシュポゼ 保湿化粧水"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "トレリアン 薬用モイスチャーローション 200mL (プレバイオティクスサーマルウォーター配合・皮膚常在菌のバランスを健やかに保ち、冬の過酷な乾燥刺激から素肌を守る薬用高保湿化粧水)"
            },
            {
                "rank": 5,
                "queries": ["ビオデルマ イドラビオ エッセンスローション", "ビオデルマ イドラビオ ローション", "ビオデルマ イドラビオ"],
                "brand": "BIODERMA (ビオデルマ)",
                "name": "イドラビオ エッセンスローション 200mL (アクアジェニシウム特許×乳酸菌由来フルクトオリゴ糖配合・肌自らの水分巡りとバリア機能を呼び醒ます高保水ブースター化粧水)"
            },
            {
                "rank": 6,
                "queries": ["乳酸菌 エイチジン フローラ 美容液", "H&JIN フローラ 美容液", "乳酸菌 美容液 うるおい 保湿"],
                "brand": "H&JIN (エイチジン)",
                "name": "エイチジン フローラ 美容液 60ml (死菌乳酸菌HJ1株を高濃度配合・冬の肌荒れやインナードライを根本からケアし、みずみずしい素肌へと導く乳酸菌集中美容液)"
            },
            {
                "rank": 7,
                "queries": ["ももぷり 潤い濃密化粧水", "ももぷり 濃密化粧水", "ももぷり 化粧水"],
                "brand": "momopuri (ももぷり)",
                "name": "潤い濃密化粧水 200ml (乳酸菌×桃セラミド×ビタミンC・E配合・とろみのあるテクスチャーが角層深部まで潤いを届け、真冬の粉吹き肌をもっちり満たす化粧水)"
            },
            {
                "rank": 8,
                "queries": ["ラクトデュウ S.E.ミルク", "ヤクルト ラクトデュウ ミルク", "ヤクルト ミルク 保湿"],
                "brand": "Yakult Beautiens (ヤクルト)",
                "name": "ラクトデュウ S.E.ミルク 110mL (S.E.シロタエッセンス×高純度ビタミンA誘導体配合・なめらかなエマルジョンが真冬の乾燥小ジワを目立たなくする高機能乳液)"
            },
            {
                "rank": 9,
                "queries": ["プロバイオダーム タイトニング コラーゲン セラム", "プロバイオダーム セラム", "バイオヒールボ セラム"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム コラーゲン リモデリング セラム 30ml (乳酸菌マイクロバイオーム×低分子コラーゲン配合・毛穴の開きと冬の乾燥たるみを土台からケアするリフティング美容液)"
            },
            {
                "rank": 10,
                "queries": ["ももぷり 潤いジェルクリーム", "ももぷり ジェルクリーム", "ももぷり クリーム"],
                "brand": "momopuri (ももぷり)",
                "name": "潤いジェルクリーム 80g (乳酸菌×桃セラミドのオールインワン保湿ジェル・ぷるんとしたジェルが角層を密着ラッピングして真冬のエアコン暖房から水分を守るクリーム)"
            }
        ]
    },
    "winter_swallow_nest": {
        "title": "保湿力の強さで肌乾燥とさようなら！シアル酸と濃密アミノ酸が真冬の深刻なしぼみ肌を底上げする保湿力高めツバメの巣コスメランク10",
        "file": "winter-swallow-nest.html",
        "items": [
            {
                "rank": 1,
                "queries": ["BI-SU 美巣 アイラッシュセラム", "BI-SU 美巣 セラム", "ツバメの巣 美容液 BI-SU"],
                "brand": "BI-SU (美巣)",
                "name": "天然アナツバメの巣 美巣 エッセンス 美容液 (マレーシア産天然アナツバメの巣エキス100%配合・ローヤルゼリーの200倍のシアル酸が冬の深刻なエイジング乾燥肌を濃密リペアする最高峰美容液)"
            },
            {
                "rank": 2,
                "queries": ["ツバメの巣 フェイスマスク パック", "ツバメの巣 シートマスク", "ツバメの巣 パック 保湿"],
                "brand": "SNP (エスエヌピー)",
                "name": "バードネスト アクア アンプルマスク 10枚入 (ツバメの巣エキス1000mg×高保水ヒアルロン酸配合・真冬の砂漠肌に集中水分チャージする高密着セルロースシートマスク)"
            },
            {
                "rank": 3,
                "queries": ["ツバメの巣 エキス 美容原液", "ツバメの巣 原液", "ツバメの巣 エキス 保湿"],
                "brand": "自然化粧品研究所",
                "name": "ツバメの巣エキス 原液 30ml (加水分解アナツバメ巣エキス100%・シアル酸とEGF様ペプチドをそのまま肌へ届ける冬の集中保湿＆ハリ弾力ブースター原液)"
            },
            {
                "rank": 4,
                "queries": ["ツバメの巣 ハンドクリーム 保湿", "美巣 ハンドクリーム", "ツバメの巣 ハンドクリーム"],
                "brand": "BI-SU (美巣)",
                "name": "天然アナツバメの巣 ハンドクリーム 40g (アナツバメの巣エキス×シアバター×ホホバオイル配合・冬の水仕事や冷気で荒れた手肌をしっとり吸い付くような潤いで包む高保湿ハンドケア)"
            },
            {
                "rank": 5,
                "queries": ["ツバメの巣 保湿 クリーム", "ツバメの巣 クリーム エイジング", "バードネスト クリーム"],
                "brand": "SNP (エスエヌピー)",
                "name": "バードネスト モイスチャークリーム 50g (アナツバメ巣エキス×植物幹細胞エキス配合・こっくり濃厚なエモリエント膜が真冬の暖房直撃による水分蒸散を完全に遮断する保護クリーム)"
            },
            {
                "rank": 6,
                "queries": ["ツバメの巣 スリーピングパック", "バードネスト スリーピングパック", "ツバメの巣 パック"],
                "brand": "SNP (エスエヌピー)",
                "name": "ゴールド コラーゲン スリーピングパック 20本 (ツバメの巣エキス×純金×加水分解コラーゲン配合・寝ている間に濃密アミノ酸が肌を満たし、真冬の朝もぷるんとしたハリ肌へ導く夜用パック)"
            },
            {
                "rank": 7,
                "queries": ["ツバメの巣 リップクリーム 保湿", "美巣 リップクリーム", "ツバメの巣 リップ"],
                "brand": "BI-SU (美巣)",
                "name": "天然アナツバメの巣 リップクリーム 4g (アナツバメの巣エキス×天然ミツロウ配合・真冬の冷風でひび割れやすい唇を濃密保護し、ぷるぷるの血色感ある唇へ整えるリップトリートメント)"
            },
            {
                "rank": 8,
                "queries": ["ツバメの巣 洗顔 保湿", "ツバメの巣 ソープ", "ツバメの巣 石鹸"],
                "brand": "美巣 (BI-SU)",
                "name": "天然アナツバメの巣 フェイシャルソープ 70g (アナツバメ巣エキス配合・キメ細かい濃密泡が冬のデリケートな素肌を摩擦レスに包み込み、潤いを奪わずに洗い上げる極上洗顔石鹸)"
            },
            {
                "rank": 9,
                "queries": ["ツバメの巣 化粧水 保湿", "ツバメの巣 ローション", "バードネスト トナー"],
                "brand": "SNP (エスエヌピー)",
                "name": "バードネスト アクア アンプルトナー 250ml (アナツバメ巣エキス×5重ヒアルロン酸配合・とろけるような高保水リキッドが乾いた角層を潤いで満たす大容量保湿化粧水)"
            },
            {
                "rank": 10,
                "queries": ["ツバメの巣 ボディミルク 保湿", "ツバメの巣 ボディクリーム", "ツバメの巣 ボディ"],
                "brand": "BI-SU (美巣)",
                "name": "天然アナツバメの巣 ボディミルク 200ml (アナツバメ巣エキス×植物オイル配合・冬の入浴後の全身へ素早く浸透し、タイツのこすれや乾燥かゆみを防ぐラグジュアリーボディケア)"
            }
        ]
    },
    "winter_dokudami": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の寒暖差ゆらぎと乾燥赤みを濃密鎮静する保湿力高めドクダミコスメランク10",
        "file": "winter-dokudami.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アヌア ドクダミ 77 スージングトナー", "アヌア ドクダミ トナー", "Anua ドクダミ 77"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 77% スージングトナー 250ml (ドクダミエキス77%高配合・冬の暖房や寒暖差で赤み・ヒリつきを起こした角層を素早く鎮静し、みずみずしく潤す韓国No.1国民的鎮静化粧水)"
            },
            {
                "rank": 2,
                "queries": ["アヌア ドクダミ 80 水分鎮静アンプル", "アヌア ドクダミ アンプル", "Anua ドクダミ 美容液"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 80% 水分鎮静アンプル 30ml (高濃度ドクダミエキス80%×トリプルヒアルロン酸配合・とろみのある濃密テクスチャーが真冬のインナードライに吸い付くように浸透する水分美容液)"
            },
            {
                "rank": 3,
                "queries": ["Abib ドクダミ カーミング トナー スキンブースター", "Abib ドクダミ トナー", "アビブ ドクダミ トナー"],
                "brand": "Abib (アビブ)",
                "name": "ドクダミ カーミング トナー スキンブースター 200ml (智異山産ドクダミエキス配合・冬の乾燥で硬くなった角層を柔軟にほぐし、肌本来の健やかな水分保持力を整えるブースター化粧水)"
            },
            {
                "rank": 4,
                "queries": ["アヌア ドクダミ 70 デイリーリリーフローション", "アヌア ドクダミ 乳液", "Anua ドクダミ ローション"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 70% デイリーリリーフ ローション 200ml (ドクダミエキス70%×3重ヒアルロン酸配合・ベタつかないシルキーな高保湿ミルクが真冬の肌を長時間しっとり保護する低刺激乳液)"
            },
            {
                "rank": 5,
                "queries": ["Abib ドクダミ フィット ガムシートマスク", "Abib ドクダミ シートマスク", "アビブ ドクダミ マスク"],
                "brand": "Abib (アビブ)",
                "name": "ガムシートマスクパック ドクダミステッカー 10枚 (ドクダミエキスを高濃度浸透・極細マイクロファイバーシートが肌に隙間なく超密着し、真冬の乾燥赤みを一晩で集中鎮静)"
            },
            {
                "rank": 6,
                "queries": ["アヌア ドクダミ 77 クリアパッド", "アヌア トナーパッド ドクダミ", "Anua ドクダミ パッド"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 77% クリアパッド 70枚入 (ドクダミ美容液を丸ごと1本分染み込ませた両面エンボスパッド・真冬の洗顔後の拭き取り保湿や部分集中鎮静パックとして活躍する万能トナーパッド)"
            },
            {
                "rank": 7,
                "queries": ["アヌア ドクダミ インテンス カーミング クリーム", "アヌア ドクダミ クリーム", "Anua ドクダミ クリーム"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ インテンス カーミングクリーム 50ml (ドクダミエキス×セラミドNP×パンテノール配合・冬の冷たい外気と乾燥から肌を守り抜くバリア強化高保湿クリーム)"
            },
            {
                "rank": 8,
                "queries": ["アヌア ドクダミ ポア コントロール クレンジングオイル", "アヌア クレンジングオイル ドクダミ", "Anua クレンジングオイル"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ ポアコントロール クレンジングオイル 200ml (非コメドジェニック処方・ドクダミエキス配合でメイク汚れや毛穴の角栓を優しくオフしながら、冬の乾燥しやすい肌をつっぱらせずに洗い上げるオイル)"
            },
            {
                "rank": 9,
                "queries": ["Abib ドクダミ スポット パッド", "Abib ドクダミ パッド", "アビブ トナーパッド"],
                "brand": "Abib (アビブ)",
                "name": "ドクダミ スポット パッド カーミングタッチ 80枚 (智異山ドクダミエキスをたっぷり含んだ無漂白コットンパッド・冬の寒暖差でカサつきやすい両頬やおでこにピタッと貼るだけのクイック水分チャージ)"
            },
            {
                "rank": 10,
                "queries": ["アヌア ドクダミ シルキー モイスチャー サンクリーム", "アヌア 日焼け止め ドクダミ", "Anua サンクリーム"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ シルキー モイスチャー サンクリーム SPF50+ PA++++ 50ml (ドクダミエキス配合・美容液のようにみずみずしい高保湿UV下地・真冬の乾燥冷風と紫外線から素肌を一日中潤いバリアで守る日焼け止め)"
            }
        ]
    }
}

def fetch_all():
    results = {}
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
                    time.sleep(2.5) # レートリミット429回避
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
                    time.sleep(3.5)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(3.0)
            
            if chosen_item:
                print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if "?_ex=" in img_url:
                    img_url = img_url.split("?_ex=")[0] + "?_ex=400x400"
                
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": chosen_item.get("affiliateUrl", chosen_item.get("itemUrl")),
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "4.8"))
                })
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_lacto_swallow_dokudami.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_lacto_swallow_dokudami.json!")

if __name__ == "__main__":
    fetch_all()
