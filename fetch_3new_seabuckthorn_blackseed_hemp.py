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
    "winter_seabuckthorn_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ7と黄金ビタミンが真冬の寒冷くすみ＆粉吹き肌を満たす高保湿サジーオイルコスメランク10",
        "file": "winter-seabuckthorn-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["サジーオイル 未精製 オーガニック 10ml", "サジーオイル 未精製", "サジー オイル オーガニック"],
                "brand": "Mandy Moon (マンディムーン)",
                "name": "オーガニック サジーオイル (未精製) 10ml (低温圧搾コールドプレス・オメガ7パルミトレイン酸＆天然βカロテン高濃度凝縮・真冬の寒冷くすみと粉吹き肌を救う濃厚リペアオイル)"
            },
            {
                "rank": 2,
                "queries": ["ヴェレダ ヒッポファンフルーティ オイル", "ヴェレダ ヒッポファン オイル", "ヴェレダ ヒッポファン"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ヒッポファンフルーティ オイル 100ml (有機サジー果実油×セサミオイル・真冬の粉吹きすねや冷え固まったボディをしっとり黄金の潤いで包み込む大人気高保湿ボディオイル)"
            },
            {
                "rank": 3,
                "queries": ["&SH シーバックソーンオイル 80ml", "&SH シーバックソーンオイル", "&SH サジー オイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "オーガニック シーバックソーンオイル 80ml (無添加コールドプレス・オメガ7の圧倒的浸透力で冬のゴワつく角層を瞬時に柔らかくほぐす高機能ブースターキャリアオイル)"
            },
            {
                "rank": 4,
                "queries": ["Life-flo ピュア シーバックソーンオイル", "Life-flo シーバックソーン", "シーバックソーンオイル Life-flo"],
                "brand": "Life-flo (ライフフロー)",
                "name": "ピュア シーバックソーンオイル 30ml (天然シーベリー種子油100%・冬の過酷なエアコン乾燥によるインナードライを鉄壁ガードする高濃度エイジングケアオイル)"
            },
            {
                "rank": 5,
                "queries": ["WELEDA ヒッポファン ハンドクリーム", "ヴェレダ ヒッポファン ハンドクリーム", "ヒッポファン ハンドクリーム"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ヒッポファン (シーバックソーン) ハンドクリーム 50ml (有機サジーオイル×ミツロウ配合・真冬の水仕事や冷風でひび割れた指先をしっとり滑らかに保護する集中ハンドクリーム)"
            },
            {
                "rank": 6,
                "queries": ["グアマラル シーベリー オイル", "シーベリー オイル グアマラル", "シーベリー オイルリキッド 50ml"],
                "brand": "Guamaral (グアマラル)",
                "name": "シーベリー ピュアオイルリキッド 50ml (モンゴル産天然サジー100%・外用スキンケア＆インナーケア両用・冬の寒さで血行を失った肌に若々しいハリと輝きを与える高純度オイル)"
            },
            {
                "rank": 7,
                "queries": ["Purilla サジー石けん", "サジー石けん 100g Purilla", "サジー 石鹸"],
                "brand": "Purilla (ピュリラ)",
                "name": "サジー高保湿無添加石けん 100g (天然サジーオイル高配合・冬の洗顔後のつっぱり感をゼロにし洗い上がりからしっとり柔らかな肌へ導く濃密モイスチャー洗顔ソープ)"
            },
            {
                "rank": 8,
                "queries": ["バジャー フェイスオイル シーバックソーン", "フェイスオイル シーバックソーン 29.5", "バジャー シーバックソーン"],
                "brand": "Badger (バジャー)",
                "name": "フェイスオイル シーバックソーン 29.5ml (USDAオーガニック認証・サジー果実エキス×ホホバ×ザクロ・真冬の乾燥小ジワをふっくら押し上げる極上フェイスセラム)"
            },
            {
                "rank": 9,
                "queries": ["RIMEDO クレンジング サジー", "RIMEDO クレンジング", "RIMEDO クレンジング セラム"],
                "brand": "RIMEDO (リメド)",
                "name": "クレンジング セラム＆バーム (サジー・CICA・ビタミンC配合) 100g (真冬の濃密メイクも擦らずオフしながらサジーオイルの濃密潤いで洗い流し後もしっとり保つ高機能クレンジング)"
            },
            {
                "rank": 10,
                "queries": ["ボタニティ マキオール セバム美容液", "ボタニティ セバム美容液", "ボタニティ 美容液"],
                "brand": "BOTANITY (ボタニティ)",
                "name": "マキオール セバム美容液 50ml (特許サジー・シーベリー複合エキス配合・冬のインナードライによる過剰皮脂と毛穴開きを整えキメの整った素肌美へ導く高機能エッセンス)"
            }
        ]
    },
    "winter_black_seed_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！奇跡のチモキノンが真冬のバリア崩壊＆乾燥荒れ肌を根本鎮静する高保湿ブラックシードオイルコスメランク10",
        "file": "winter-black-seed-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アメイジングハーブズ ブラックシード 120ml", "アメイジングハーブズ ブラックシード 純粋低温圧搾", "Amazing Herbs ブラックシードオイル"],
                "brand": "Amazing Herbs (アメイジングハーブズ)",
                "name": "コールドプレス 100% ピュア ブラックシードオイル 120ml (世界最高峰エジプト産ニゲラ種子・高濃度チモキノン処方・真冬の重度な粉吹きと乾燥荒れ肌を根本から救済する名品オイル)"
            },
            {
                "rank": 2,
                "queries": ["NOW Foods ブラッククミンシード", "NOW ブラッククミンシードオイル", "ナウフーズ ブラッククミン"],
                "brand": "NOW Foods (ナウフーズ)",
                "name": "オーガニック ブラッククミンシードオイル 237ml (コールドプレス未精製・非遺伝子組み換え・必須脂肪酸の強力なエモリエント効果で真冬の硬直角層を柔らかく満たす高機能植物油)"
            },
            {
                "rank": 3,
                "queries": ["Nature's Way ブラックシード", "Nature's Way ブラックシード オイル", "ネイチャーズウェイ ブラックシード"],
                "brand": "Nature's Way (ネイチャーズウェイ)",
                "name": "オーガニック ブラックシード オイル 236ml (USDA認定オーガニック・チモキノン高含有・冬の暖房直撃による乾燥性肌荒れや角層ゴワつきを解きほぐすプレミアムキャリアオイル)"
            },
            {
                "rank": 4,
                "queries": ["Pure Indian Foods オーガニック ブラックシードオイル", "Pure Indian Foods ブラックシード", "Pure Indian Foods"],
                "brand": "Pure Indian Foods (ピュアインディアンフーズ)",
                "name": "オーガニック ブラックシードオイル 240ml (伝統アーユルヴェーダ製法・低温圧搾未精製・冬の冷風で赤くヒリつく敏感肌を素早く鎮静し濃密な油分膜で守り抜くピュアオイル)"
            },
            {
                "rank": 5,
                "queries": ["iYURA KERANYA ピュア ブラックシード", "iYURA KERANYA", "ブラックシード ヘアオイル"],
                "brand": "iYURA (イユラ)",
                "name": "KERANYA ピュア ブラックシード 濃密ヘアオイル 100ml (ニゲラ種子油×伝統アーユルヴェーダハーブ・冬の乾燥フケや頭皮の痒み・髪のパサつきを根元から濃密補修するヘアセラム)"
            },
            {
                "rank": 6,
                "queries": ["ブラッククミンシードオイル 30ml", "ブラッククミンシードオイル 化粧品原料", "ブラッククミンシードオイル"],
                "brand": "自然原料研究所",
                "name": "ブラッククミンシードオイル 30ml [化粧品原料グレード] (低温圧搾コールドプレス・オメガ6＆オメガ9豊富・手持ちのクリームや乳液に1滴混ぜて真冬の保湿バリアを底上げする原液オイル)"
            },
            {
                "rank": 7,
                "queries": ["ブラッククミンシードオイル 10ml", "ブラッククミン オイル 10ml", "ブラッククミンシードオイル"],
                "brand": "プラントコスメ原料",
                "name": "ブラッククミンシードオイル 10ml [お試し・集中スポット用] (高純度未精製・チモキノン凝縮・冬の繰り返す頑固な乾燥荒れや目元・口元のピリつく部位にピンポイントで密着するレスキューオイル)"
            },
            {
                "rank": 8,
                "queries": ["ブラックシードオイル 240ml Amazing Herbs", "Amazing Herbs 240ml", "ブラックシード 純粋低温圧搾 240ml"],
                "brand": "Amazing Herbs (アメイジングハーブズ)",
                "name": "ブラックシード 純粋低温圧搾オイル 240ml 大容量ボトル (エジプト産最高峰グレード・顔だけでなく真冬の粉吹きすねや肘・背中まで全身に贅沢に使えるサロン品質オイル)"
            },
            {
                "rank": 9,
                "queries": ["食用ブラッククミンシードオイル120ml", "ブラッククミンシードオイル120ml", "ブラッククミン オイル 120ml"],
                "brand": "Nigella Care (ニゲラケア)",
                "name": "無添加 エクストラバージン ブラッククミンシードオイル 120ml (コールドプレス100%・スキンケア＆美容インナーケア両用・体の内外から真冬の抗酸化と水分保持力を高めるスーパーオイル)"
            },
            {
                "rank": 10,
                "queries": ["ブラックシードオイル 500mg Amazing Herbs", "アメイジングハーブズ ブラックシードオイル 500mg", "ブラックシードオイル サプリ"],
                "brand": "Amazing Herbs (アメイジングハーブズ)",
                "name": "ブラックシードオイル 500mg ソフトジェル 90粒 (純粋ブラッククミン種子油100%カプセル・真冬の極度なインナードライを体内から満たし肌の水分蒸散を防ぐインナービューティーサプリ)"
            }
        ]
    },
    "winter_hemp_seed_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！必須脂肪酸の黄金比率が真冬の超乾燥＆ヒリつく角層を密着シールドする高保湿ヘンプシードオイルコスメランク10",
        "file": "winter-hemp-seed-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ハンドクリーム HP 100mL ヘンプ", "ボディショップ ヘンプ ハンドクリーム 100ml", "ハンドクリーム HP 100mL"],
                "brand": "THE BODY SHOP (ザ・ボディショップ)",
                "name": "ハードワーキング ハンドクリーム HP (ヘンプ) 100ml (フランス産ヘンプシードオイル配合・真冬の水仕事や冷風で荒れ果てた指先・関節のひび割れを包み込む世界的大ベストセラー)"
            },
            {
                "rank": 2,
                "queries": ["ドクターブロナー オーガニック バーム BA ベビーマイルド", "ドクターブロナー オーガニック バーム BA", "ドクターブロナー マジックバーム ベビーマイルド"],
                "brand": "Dr.Bronner's (ドクターブロナー)",
                "name": "オーガニック バーム BA ベビーマイルド 14g (ヘンプシードオイル×ホホバ×アボカド・真冬の唇のひび割れや目元の激しい乾燥を密着シールドする無香料マルチバーム)"
            },
            {
                "rank": 3,
                "queries": ["リップ スティック HP 4.2g ヘンプ", "ボディショップ ヘンプ リップ", "リップ スティック HP 4.2g"],
                "brand": "THE BODY SHOP (ザ・ボディショップ)",
                "name": "ヘンプ リッププロテクター スティック HP 4.2g (ヘンプシードオイル高配合・真冬の冷風で皮むけ・ひび割れを起こした過酷な唇を長時間しっとり密着シールドする伝説のリップクリーム)"
            },
            {
                "rank": 4,
                "queries": ["&SH ヘンプシードオイル 未精製 80ml", "&SH ヘンプシードオイル 80ml", "&SH ヘンプシードオイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100% ピュア ヘンプシードオイル (未精製) 80ml (低温圧搾コールドプレス・オメガ3とオメガ6が1:3の黄金比率・冬の洗顔後ブースターとして角層深部へすっと馴染む高機能キャリアオイル)"
            },
            {
                "rank": 5,
                "queries": ["ヘンプシードオイル 未精製 オーガニック 50ml", "ヘンプシードオイル 50ml マンディムーン", "ヘンプシードオイル 未精製 50ml"],
                "brand": "Mandy Moon (マンディムーン)",
                "name": "オーガニック ヘンプシードオイル (未精製) 50ml (遮光ボトル・必須脂肪酸約80%含有・真冬の乳液や美容液にブレンドしてバリア機能を強力ブーストする高純度植物油)"
            },
            {
                "rank": 6,
                "queries": ["CBD バーム モイスチャー roun", "roun CBD バーム", "CBD バーム モイスチャー 70g"],
                "brand": "roun (ラウン)",
                "name": "CBD モイスチャー バーム 70g (ヘンプ由来CBD×シアバター×ヘンプシードオイル・真冬のガサガサ肘・踵・粉吹きボディをとろける濃密膜で包み込む高保湿リッチバーム)"
            },
            {
                "rank": 7,
                "queries": ["エンドカ ヘンプボディバター", "ENDOCA ヘンプボディバター", "エンドカ ボディバター"],
                "brand": "ENDOCA (エンドカ)",
                "name": "ヘンプボディバター CBD450mg 100ml (高純度ヘンプエキス×シアバター×ココナッツオイル・真冬の寒冷でこわばった皮膚組織をしっとりほぐす世界最高峰オーガニックボディバター)"
            },
            {
                "rank": 8,
                "queries": ["ヘンプタッチ ベビー バーム", "hemptouch ベビー バーム", "ベビー バーム ジェントル ヘンプタッチ"],
                "brand": "hemptouch (ヘンプタッチ)",
                "name": "ジェントル ベビー バーム 50ml (スロベニア産有機ヘンプシードオイル配合・無香料・真冬の極度な乾燥でピリピリ敏感になった赤ら顔や赤ちゃんの繊細な肌を守る低刺激バーム)"
            },
            {
                "rank": 9,
                "queries": ["kalm CBD Lip Balm", "kalm リップバーム", "kalm CBD リップ"],
                "brand": "kalm (カルム)",
                "name": "CBD リップバーム 5ml (高純度ヘンプオイル×植物性ワックス・冬の冷たい外気からデリケートな唇の粘膜を守り一日中ツヤと潤いをキープする高保湿リップトリートメント)"
            },
            {
                "rank": 10,
                "queries": ["HEMPS 有機ヘンプシードオイル", "ヘンプフーズ 有機ヘンプシードオイル", "ヘンプシードオイル 有機 麻の実油 180g"],
                "brand": "HEMP FOODS JAPAN (ヘンプフーズ)",
                "name": "有機 ヘンプシードオイル 130g (有機JAS認定・低温圧搾エクストラバージン・冬のスキンケア前のオイルブースターや乾燥予防インナーケアにも最適な奇跡の麻の実オイル)"
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
                        time.sleep(5)
                
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

    output_filename = "fetched_3new_seabuckthorn_blackseed_hemp.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items successfully fetched!")
    print(f"Results saved to {output_filename}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
