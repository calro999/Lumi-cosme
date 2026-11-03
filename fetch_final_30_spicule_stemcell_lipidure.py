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
    "winter_spicule": {
        "title": "保湿力の強さで肌乾燥とさようなら！毛穴奥まで潤いを届けて冬枯れ肌をふっくら覚醒させる高保湿スピキュール（針美容液）ランク10",
        "file": "winter-spicule.html",
        "items": [
            {
                "rank": 1,
                "queries": ["VT リードルショット 100", "リードルショット 100"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルショット 100 (50ml) - 天然マイクロニードル95,000本配合・毎晩の浸透ルート開通で冬枯れ肌をふっくら満たす導入針美容液"
            },
            {
                "rank": 2,
                "queries": ["VT リードルショット 300", "リードルショット 300"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルショット 300 (50ml) - 天然マイクロニードル237,500本配合・3日に1度の集中浸透で硬化した真冬の角質をほぐす高濃度セラム"
            },
            {
                "rank": 3,
                "queries": ["VT リードルショット 700", "リードルショット 700"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルショット 700 (30ml) - 天然マイクロニードル570,000本配合・週1回のエステ級集中刺激で毛穴と乾燥小ジワを立て直す最高峰セラム"
            },
            {
                "rank": 4,
                "queries": ["メディリフト ニードルリフトセラム", "ヤーマン ニードルリフトセラム"],
                "brand": "YA-MAN (ヤーマン) / メディリフト",
                "name": "メディリフト ニードルリフトセラム 18g - 24K純金コロイドをまとった天然マイクロニードル約100万本配合・ハリ弾力を底上げする国産プレミアム美容液"
            },
            {
                "rank": 5,
                "queries": ["VT リードルショット 50", "リードルショット 50", "VT リードルショット マイルド"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "マイルド リードルショット 50 (50ml) - 天然ニードル38,000本配合・初めての針美容や敏感肌の朝夜デイリー保湿に最適な低刺激導入美容液"
            },
            {
                "rank": 6,
                "queries": ["スピキュール 美容液", "マイクロニードル 美容液"],
                "brand": "BERRISOM / 韓国スキンケア",
                "name": "高濃度スピキュール ハリ弾力セラム 30ml - 海綿から抽出した天然微細針×ヒアルロン酸・角層深部へうるおいをダイレクト注入する濃密美容液"
            },
            {
                "rank": 7,
                "queries": ["メディキューブ エクソソーム ショット", "medicube エクソソーム", "ゼロワンデイ エクソソーム ショット"],
                "brand": "medicube (メディキューブ)",
                "name": "ゼロワンデイ エクソソーム ショット (2000 / 7500) - エクソソーム×微細ニードル針配合・冬の乾燥毛穴開きをキュッと引き締める毛穴特化美容液"
            },
            {
                "rank": 8,
                "queries": ["ダーマレーザー ウルセラC", "ダーマレーザー ウルセラ"],
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー ウルセラC / ウルセラR 美容液 30ml - レーザー美容発想の超高浸透ナノカプセル×集中保湿で冬のキメ乱れを徹底ケア"
            },
            {
                "rank": 9,
                "queries": ["CNP ダーマアンサー", "CNP ピーリング 美容液"],
                "brand": "CNP Laboratory (シーエヌピー)",
                "name": "ダーマアンサー インビジブル ピーリング ブースター 100ml - 冬の古い角質を拭き取らずに穏やかにほぐし、後の保湿浸透力を倍増させる導入液"
            },
            {
                "rank": 10,
                "queries": ["VT シカ リードルショット", "シカ リードルショット 100"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "シカ リードルショット 100 × CICAマスクセット - CICA（ツボクサエキス）×天然ニードルで冬の寒暖差赤みと乾燥ゴワつきをダブル鎮静＆高保湿"
            }
        ]
    },
    "winter_stem_cell": {
        "title": "保湿力の強さで肌乾燥とさようなら！肌本来のうるおい保持力を根源から呼び覚ます高保湿ヒト幹細胞コスメランク10",
        "file": "winter-stem-cell.html",
        "items": [
            {
                "rank": 1,
                "queries": ["KISO ヒト幹細胞", "キソ ステムセルフロー"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "ステムセルフロー SC 30ml (国産ヒト幹細胞順化培養液高配合・角層細胞の自活保水力を引き出す高純度エイジングケア美容液)"
            },
            {
                "rank": 2,
                "queries": ["フラコラ ヒト幹細胞", "フラコラ ヒト幹細胞培養エキス"],
                "brand": "fracora (フラコラ)",
                "name": "ヒト幹細胞培養エキス原液 LP 30ml (ナノリポソーム化技術で深層浸透・冬の枯れ肌に湧き上がるようなうるおいとハリを与える最高峰原液)"
            },
            {
                "rank": 3,
                "queries": ["アンプルール 美容液", "アンプルール ラグジュアリー"],
                "brand": "AMPLEUR (アンプルール)",
                "name": "ラグジュアリー・デ・エイジ リジュリューションV 32ml (植物幹細胞×GFペプチドカプセル配合・肌密度を高めて冬の乾燥小ジワを撃退する濃密美容液)"
            },
            {
                "rank": 4,
                "queries": ["レカルカ シムセラム", "Lekarka シムセラム"],
                "brand": "Lekarka (レカルカ)",
                "name": "01 SYM SERUM EX (シムセラムEX) 30ml (ヒト歯髄幹細胞順化培養液×EGF配合・サロン発祥の圧倒的保水力とハリツヤをもたらす名品美容液)"
            },
            {
                "rank": 5,
                "queries": ["KISO ヒト幹細胞 クリーム", "キソ ステム フェイシャル クリーム"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "ステム フェイシャル クリーム 50g (ヒト幹細胞培養液エキス15%×ヒト型セラミド配合・翌朝まで乾燥を寄せ付けない濃密シールドクリーム)"
            },
            {
                "rank": 6,
                "queries": ["ディレイア ステムリバイタセラム", "ディレイア 美容液"],
                "brand": "direia (ディレイア)",
                "name": "ステム リバイタセラム 30ml (先進ヒト幹細胞培養液×イノベーティブ3Dナノテクノロジー・プロ仕様の超深層保湿再生美容液)"
            },
            {
                "rank": 7,
                "queries": ["ヒト幹細胞 美容液 30ml", "ヒト幹細胞 美容液"],
                "brand": "美肌自慢 / プレミアムエッセンス",
                "name": "プレミアム ヒト幹細胞 培養液 原液 エッセンス 30ml (冬のゴワつき・カサつき肌にスッとなじみ、キメをふっくら整える濃厚ブースター)"
            },
            {
                "rank": 8,
                "queries": ["ヒト幹細胞 フェイスマスク", "ヒト幹細胞 シートマスク 30枚"],
                "brand": "THE STEM CELL (ザ・ステムセル)",
                "name": "トリートメント フェイシャルマスク 30枚入 (高濃度ヒト幹細胞培養液×植物幹細胞×高保水ヒアルロン酸・毎日の密着集中保水パック)"
            },
            {
                "rank": 9,
                "queries": ["自然化粧品研究所 ヒト幹細胞", "ヒト幹細胞 原液 10ml"],
                "brand": "自然化粧品研究所",
                "name": "ヒト幹細胞培養液エキス 10ml (純国産ピュア原液・手持ちの化粧水や乳液に1〜2滴加えるだけで保湿力を劇的にアップさせる高機能カスタム原液)"
            },
            {
                "rank": 10,
                "queries": ["シーラボ エンリッチリフト", "ドクターシーラボ アクアコラーゲンゲル エンリッチリフト"],
                "brand": "DR.CI:LABO (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 120g (浸透型コラーゲンEX×ナイアシンアミド配合・真冬の乾燥小ジワとハリ不足を引き締めて潤す多機能ゲル)"
            }
        ]
    },
    "winter_lipidure": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の2倍の保水膜で冬の乾燥冷風を完全ブロックする高保水リピジュアコスメランク10",
        "file": "winter-lipidure.html",
        "items": [
            {
                "rank": 1,
                "queries": ["肌をうるおす 保湿美容液", "松山油脂 保湿美容液"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "肌をうるおす保湿スキンケア 保湿美容液 30ml (5種のヒト型セラミド×リピジュア高配合・水分保持力を極限まで高めて砂漠肌を救う高保湿美容液)"
            },
            {
                "rank": 2,
                "queries": ["太陽のアロエ社 ヒアルロン酸", "太陽のアロエ社 原液"],
                "brand": "太陽のアロエ社",
                "name": "ヒアルロン酸 原液 80ml (高純度ヒアルロン酸×水分保持ポリマー・角層細胞に水分を強力に引き寄せて逃さない大ロングセラー保水エッセンス)"
            },
            {
                "rank": 3,
                "queries": ["ラフラ モイスチャーローション", "RAFRA 化粧水"],
                "brand": "RAFRA (ラフラ)",
                "name": "モイスチャーローション 200ml (リピジュア×天然オレンジ精油×高保水アミノ酸配合・冬のオフィス暖房下でも夕方まで乾かない濃密化粧水)"
            },
            {
                "rank": 4,
                "queries": ["肌をうるおす 保湿浸透水", "松山油脂 保湿浸透水 モイストリッチ"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "肌をうるおす保湿スキンケア 保湿浸透水 モイストリッチ 120ml (とろみテクスチャー×リピジュア×大豆発酵エキス・冬の硬化角質をほぐす高保水ローション)"
            },
            {
                "rank": 5,
                "queries": ["アクセーヌ モイストバランスローション", "モイストバランスローション"],
                "brand": "ACSEINE (アクセーヌ)",
                "name": "モイストバランス ローション 360ml (業界最小クラスの超微細ナノカプセル×保水ポリマー配合・一日中うるおいが巡り続ける水分補給化粧水)"
            },
            {
                "rank": 6,
                "queries": ["ルルルン プレシャス RED", "ルルルン プレシャス レッド 32枚"],
                "brand": "LuLuLun (ルルルン)",
                "name": "ルルルンプレシャス RED (モイスト) 32枚入 (リピジュア×発酵酵母細胞壁エキス配合・濃密な美容液ヴェールで大人の乾燥ゴワつきをリセットするシートマスク)"
            },
            {
                "rank": 7,
                "queries": ["キュレル 潤浸保湿 フェイスクリーム", "キュレル フェイスクリーム"],
                "brand": "Curel (キュレル)",
                "name": "潤浸保湿 フェイスクリーム 40g (セラミド機能成分×消炎剤配合・肌荒れを防ぎながらしっとり吸い付く高保水保護ヴェールを形成)"
            },
            {
                "rank": 8,
                "queries": ["無印良品 化粧水 高保湿", "無印良品 敏感肌用 化粧水 高保湿"],
                "brand": "無印良品 (MUJI)",
                "name": "敏感肌用化粧水 高保湿タイプ 300ml (天然水生まれ×リピジュア（ポリクオタニウム-51）×ヒアルロン酸配合・全身にもたっぷり使える高保水化粧水)"
            },
            {
                "rank": 9,
                "queries": ["ポリクオタニウム-51 原液", "リピジュア 保湿", "自然化粧品研究所 保湿原液"],
                "brand": "自然化粧品研究所",
                "name": "高機能保水エッセンス 原液 20ml (ポリクオタニウム-51配合・ヒアルロン酸の2倍の保水膜で洗顔しても落ちにくい人口角層ヴェールを形成)"
            },
            {
                "rank": 10,
                "queries": ["肌をうるおす 保湿クリーム", "松山油脂 保湿クリーム"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "肌をうるおす保湿スキンケア 保湿クリーム 50g (ヒト型セラミド5種×シア脂×リピジュア配合・コクのある濃厚テクスチャーで真冬の冷風を完全遮断)"
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
                        time.sleep(1.3)
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                if cand.get("itemPrice", 0) > 0 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(2.0)
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
            
    with open("fetched_final_30_spicule_stemcell_lipidure.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_success}/{total_needed} items to fetched_final_30_spicule_stemcell_lipidure.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
