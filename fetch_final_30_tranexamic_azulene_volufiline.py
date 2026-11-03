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
    "winter_tranexamic_acid": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房乾燥によるくすみ・肌荒れを防ぎ澄んだ透明ツヤ肌へ導く高保湿トラネキサム酸コスメランク10",
        "file": "winter-tranexamic-acid.html",
        "items": [
            {
                "rank": 1,
                "queries": ["トランシーノ 美容液", "トランシーノ メラノシグナルエッセンス"],
                "brand": "TRANSINO (トランシーノ)",
                "name": "薬用メラノシグナルエッセンス 30g / 50g (第一三共ヘルスケア・トラネキサム酸配合薬用美白美容液)"
            },
            {
                "rank": 2,
                "queries": ["HAKU メラノフォーカスEV", "HAKU 美容液"],
                "brand": "資生堂 HAKU (ハク)",
                "name": "メラノフォーカスEV 45g (m-トラネキサム酸×4MSKのW有効成分・高保湿エイジング美白美容液)"
            },
            {
                "rank": 3,
                "queries": ["イハダ 薬用クリアエマルジョン", "イハダ エマルジョン"],
                "brand": "IHADA (イハダ) / 資生堂薬品",
                "name": "薬用クリアエマルジョン 135ml (高精製ワセリン×トラネキサム酸配合・冬の肌荒れと乾燥くすみを防ぐ薬用乳液)"
            },
            {
                "rank": 4,
                "queries": ["白潤プレミアム ジュレ", "白潤プレミアム 美白ジュレ", "肌ラボ 白潤プレミアム"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "白潤プレミアム 薬用ジュレ状美白美容液 200ml (ホワイトトラネキサム酸×2種のヒアルロン酸・濃厚濃密オールインワンジュレ)"
            },
            {
                "rank": 5,
                "queries": ["トゥヴェール ブライトニングセラム", "トゥヴェール トラネキサム酸"],
                "brand": "TOUT VERT (トゥヴェール)",
                "name": "ブライトニングセラム 30ml (薬用トラネキサム酸原末配合・冬のインナードライとメラニン生成を抑える浸透美白セラム)"
            },
            {
                "rank": 6,
                "queries": ["コスデバハ トラネキサム酸 美容液", "コスデバハ TN"],
                "brand": "Cos De BAHA (コスデバハ)",
                "name": "TN トラネキサム酸5% + ナイアシンアミド5% セラム 30ml (高濃度トラネキサム酸×ナイアシンアミド高保湿セラム)"
            },
            {
                "rank": 7,
                "queries": ["キュレル 美白ケア 美容液", "キュレル 薬用美白美容液"],
                "brand": "Curel (キュレル) / 花王",
                "name": "潤浸保湿 美白美容液 30g (カモミラET×セラミド機能成分配合・真冬の乾燥性敏感肌を包み込む高保湿ジェル)"
            },
            {
                "rank": 8,
                "queries": ["アスタリフト ホワイト ジェリー アクアリスタ", "アスタリフト ジェリー 美白"],
                "brand": "ASTALIFT (アスタリフト) / 富士フイルム",
                "name": "ホワイト ジェリー アクアリスタ 40g (Wヒト型ナノセラミド×トラネキサム酸配合・極上先行美白ジュリー)"
            },
            {
                "rank": 9,
                "queries": ["アクアレーベル トリートメントミルク 美白", "アクアレーベル 美白 乳液", "アクアレーベル トラネキサム酸"],
                "brand": "AQUALABEL (アクアレーベル) / 資生堂",
                "name": "トリートメントミルク ブライトニング 130ml (トラネキサム酸×高保湿CICA・角層深くうるおいを満たす濃厚美白乳液)"
            },
            {
                "rank": 10,
                "queries": ["オルビス ブライト モイスチャー", "オルビス 美白 乳液"],
                "brand": "ORBIS (オルビス)",
                "name": "オルビス ブライト モイスチャー M 50ml (高浸透トラネキサム酸配合・みずみずしく濃密に潤す薬用高保湿乳液)"
            }
        ]
    },
    "winter_azulene": {
        "title": "保湿力の強さで肌乾燥とさようなら！寒暖差の赤ら顔とヒリつく真冬の敏感肌を濃密バリアで包み込む高保湿アズレンコスメランク10",
        "file": "winter-azulene.html",
        "items": [
            {
                "rank": 1,
                "queries": ["クレアス ブルーカーミングクリーム", "Klairs ミッドナイトブルー"],
                "brand": "Dear, Klairs (クレアス)",
                "name": "ミッドナイトブルー カーミングクリーム 30ml / 60ml (グアイアズレン×ツボクサエキス配合・寒暖差赤みと真冬の肌荒れをレスキューする青の鎮静バーム)"
            },
            {
                "rank": 2,
                "queries": ["アズレン スージング クリーム", "グアイアズレン クリーム", "アズレン フェイスクリーム"],
                "brand": "SUR.MEDIC (サーメディック)",
                "name": "アズレン スージング カーミングクリーム 50ml (天然グアイアズレン×セラミドNP配合・寒風ダメージを受けた角層を包み込む濃厚ブルーシールド)"
            },
            {
                "rank": 3,
                "queries": ["ダーマファーム R4 アンプル", "DERMAFIRM アズレン", "ダーマファーム アズレン"],
                "brand": "DERMAFIRM (ダーマファーム)",
                "name": "ウルトラ スージング R4 アンプル 30ml (高純度アズレンリポソーム×ペプチドコンプレックス配合・冬のゆらぎ肌を速攻ケアする紫の濃密美容液)"
            },
            {
                "rank": 4,
                "queries": ["アズレン 美容液", "グアイアズレン アンプル", "アズレン カーミング アンプル"],
                "brand": "Bellflower (ベルフラワー)",
                "name": "アズレン デイリー カーミングセラム 50ml (グアイアズレン×ツボクサエキス・冷たい外気でヒリつく肌を穏やかに満たす高保水セラム)"
            },
            {
                "rank": 5,
                "queries": ["ダーマファーム R4 クリーム", "DERMAFIRM クリーム", "ダーマファーム スージング"],
                "brand": "DERMAFIRM (ダーマファーム)",
                "name": "ウルトラ スージング R4 クリーム 50g (リポソーム化アズレン×17種アミノ酸配合・冬の乾燥と赤みを封じ込める高保湿カーミングクリーム)"
            },
            {
                "rank": 6,
                "queries": ["VT シカ スージングマスク", "VT デイリースージングマスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "CICA デイリースージングマスク 30枚入 (ツボクサエキス×カモミール由来アズレン成分・真冬の冷えた肌に密着して水分満タンにするデイリーシートマスク)"
            },
            {
                "rank": 7,
                "queries": ["リアルバリア シカレリーフ", "リアルバリア エクストリーム クリーム", "リアルバリア クリーム"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "エクストリーム クリーム 50ml (特許MLE皮膚バリア技術×パンテノール・極度の乾燥と冷風ダメージを包み込む高保湿鎮静シールド)"
            },
            {
                "rank": 8,
                "queries": ["コスメデコルテ リポソーム アドバンスト リペアセラム", "コスメデコルテ リポソーム 美容液"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアセラム 50ml (多重層バイオリポソーム×カモミラエキス配合・1兆個のマイクロカプセルが届ける真冬の最高峰浸透保湿)"
            },
            {
                "rank": 9,
                "queries": ["カウブランド 無添加 全身保湿ミルククリーム", "カウブランド 保湿クリーム"],
                "brand": "カウブランド 無添加フェイスケア",
                "name": "無添加 全身保湿ミルククリーム 250g (素肌由来セラミド×植物性スクワラン配合・寒風でヒリつく超敏感肌を優しく守る低刺激高保湿クリーム)"
            },
            {
                "rank": 10,
                "queries": ["アルージェ モイスト トリートメント ジェル", "アルージェ ジェル"],
                "brand": "Arouge (アルージェ) / 全薬工業",
                "name": "モイスト トリートメント ジェル 50ml (天然セラミド×抗炎症成分グリチルリチン酸・冬の冷えによるバリア破綻を優しく修復する薬用高保湿ジェル)"
            }
        ]
    },
    "winter_volufiline": {
        "title": "保湿力の強さで肌乾燥とさようなら！寒さでしぼんだ目元・口元をふっくら満たして冬枯れ影を跳ね返す高濃度ボルフィリンコスメランク10",
        "file": "winter-volufiline.html",
        "items": [
            {
                "rank": 1,
                "queries": ["KISO ボルフィリン 原液", "キソ ボルフィリン"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "ボルフィリン原液 100% 20ml (フランスセダーマ社純正ハナスゲ根エキス配合・目元やほうれい線の冬枯れしぼみ肌をふっくら持ち上げる最高峰原液)"
            },
            {
                "rank": 2,
                "queries": ["ボルフィリン 原液 美容液", "ハナスゲ根エキス 原液", "ボルフィリン 100%"],
                "brand": "自然化粧品研究所",
                "name": "ハナスゲ根エキス (ボルフィリン) 原液 10ml (フランスセダーマ社原料・手持ちのクリームや美容液に1滴混ぜて使う高濃度ボリュームアップ原液)"
            },
            {
                "rank": 3,
                "queries": ["メディピール ペプチド9 ボリューム エッセンス", "MEDIPEEL ペプチド9"],
                "brand": "MEDI-PEEL (メディピール)",
                "name": "ペプチド9 ボリューム オールインワン エッセンス 100ml (ボルフィリン5%×ペプチド9種・微細酸素バブルが角層深層で弾けて冬のたるみ肌をパンッと跳ね返す)"
            },
            {
                "rank": 4,
                "queries": ["シドミュール ボルフィリン", "sidmool ボルフィリン"],
                "brand": "SIDMOOL (シドミュール)",
                "name": "ボルフィリン40 弾力マルチバーム 9.5ml (セダーマ社認証ボルフィリン高配合・乾燥でしぼんだ目元・リップ・ほうれい線に潤いとハリを与える特濃スティック)"
            },
            {
                "rank": 5,
                "queries": ["ボルフィリン アイクリーム", "ボルフィリン 目元 美容液", "ハナスゲ アイクリーム"],
                "brand": "DERMA FACTORY (ダーマファクトリー)",
                "name": "ボルフィリン20% アイクリーム 30ml (フランス産ボルフィリン20%高配合・冬の乾燥くぼみ目元とほうれい線をふっくらケアする濃厚クリーム)"
            },
            {
                "rank": 6,
                "queries": ["ワンシング セラム", "ONE THING エッセンス", "ワンシング ツボクサ"],
                "brand": "ONE THING (ワンシング)",
                "name": "ペプチド レチナール セラム 30ml (弾力サポートペプチド×植物性ハリ成分・冬の肌萎縮にアプローチする高浸透エイジングケア美容液)"
            },
            {
                "rank": 7,
                "queries": ["ボルフィリン クリーム 弾力", "ハナスゲ クリーム 保湿", "ボルフィリン ボリューム クリーム"],
                "brand": "Tosowoong (トソウン)",
                "name": "ボルフィリン100% ボリューム リフティングクリーム 50ml (フランスセダーマ社特許ボルフィリン×高保水シア脂・真冬の影を消し去る高保湿リフトクリーム)"
            },
            {
                "rank": 8,
                "queries": ["アビブ コラーゲン アイパッチ", "Abib コラーゲン パッチ"],
                "brand": "Abib (アビブ)",
                "name": "コラーゲン アイパッチ レディテクスチャー 60枚 (発酵ハナスゲエキス×ヴィーガンコラーゲン・冬の乾燥でしわむ目元をひんやり潤すハイドロゲルシート)"
            },
            {
                "rank": 9,
                "queries": ["オバジX ダーマアドバンスドリフト", "オバジ ダーマアドバンスドリフト クリーム"],
                "brand": "Obagi (オバジ) / ロート製薬",
                "name": "オバジX ダーマアドバンスドリフト 50g (パワーリフトテクノロジー×高浸透コラーゲンエラスチン・冬の重力としぼみに挑む高機能リフトクリーム)"
            },
            {
                "rank": 10,
                "queries": ["エピステーム アイパーフェクトショット", "エピステーム アイクリーム"],
                "brand": "episteme (エピステーム) / ロート製薬",
                "name": "アイパーフェクトショットa 18g (パワライズコンプレックス×植物性ボリュームエキス・真冬の目袋や乾燥まぶたを360度引き締める最高峰目元美容クリーム)"
            }
        ]
    }
}

def fetch_and_save():
    results = {}
    total_needed = sum(len(c["items"]) for c in CATEGORIES.values())
    total_success = 0
    
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==================== Verifying {cat_key} ====================")
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
                        time.sleep(1.2)
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(1.5)
                if chosen_item:
                    break
            
            if not chosen_item:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}!")
                continue
            
            img_url = ""
            if chosen_item.get("mediumImageUrls"):
                img_url = chosen_item["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
            elif chosen_item.get("smallImageUrls"):
                img_url = chosen_item["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
            
            price = chosen_item.get("itemPrice", 0)
            aff_url = chosen_item.get("affiliateUrl", "") or chosen_item.get("itemUrl", "")
            raw_title = chosen_item.get("itemName", item["name"])
            
            print(f"  ✅ SUCCESS Rank {item['rank']}: {price}円 | img:{bool(img_url)} | {raw_title[:35]}")
            results[cat_key]["items"].append({
                "rank": item["rank"],
                "name": item["name"],
                "brand": item["brand"],
                "price": price,
                "raw_title": raw_title,
                "affiliate_url": aff_url,
                "img_url": img_url
            })
            total_success += 1
            
    with open("fetched_final_30_tranexamic_azulene_volufiline.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_success}/{total_needed} items to fetched_final_30_tranexamic_azulene_volufiline.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
