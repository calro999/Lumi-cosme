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
    "winter_macadamia_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！若さの脂肪酸パルミトレイン酸が真冬の皮脂枯れ肌を瞬時に満たす高保湿マカデミアナッツオイルコスメランク10",
        "file": "winter-macadamia-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["生活の木 マカデミアナッツオイル", "生活の木 プラントオイル マカデミア", "マカデミアナッツオイル 生活の木"],
                "brand": "Tree of life (生活の木)",
                "name": "マカデミアナッツオイル 25ml (低温圧搾コールドプレス・パルミトレイン酸約20%含有・真冬の硬化した角層を瞬時にほぐし皮脂膜を再現する高浸透ブースターオイル)"
            },
            {
                "rank": 2,
                "queries": ["マカダミアナッツオイル 1000ml", "マカダミアナッツオイル 500ml", "マカダミアナッツオイル 大容量"],
                "brand": "Beau temps (ボータン)",
                "name": "ピュア マカダミアナッツオイル 1000ml ポンプ付 (パルミトレイン酸高含有・真冬の極度な乾燥で硬くなった全身の肌を柔らかく包み込む大容量サロン品質キャリアオイル)"
            },
            {
                "rank": 3,
                "queries": ["クナイプ ビオ オイル ローズ", "クナイプビオ オイル", "クナイプ オイル 100ml"],
                "brand": "Kneipp (クナイプ)",
                "name": "クナイプビオ オイル ローズ 100ml (天然マカデミアナッツ油×ダマスクローズ・真冬の肌のキメをふっくら整え女性らしい華やかな潤いとツヤをもたらす名品マルチオイル)"
            },
            {
                "rank": 4,
                "queries": ["カフェドサボン マカダミアナッツオイル", "マカダミアナッツオイル カフェドサボン", "マカダミアナッツオイル 50ml 未精製"],
                "brand": "Cafe de Savon (カフェ・ド・サボン)",
                "name": "未精製 マカダミアナッツオイル 50ml (ナッツの栄養を丸ごと残したゴールデンカラー・冬の暖房直撃によるインナードライを濃密油分膜で完全ガードする無添加オイル)"
            },
            {
                "rank": 5,
                "queries": ["&SH マカダミアナッツオイル", "マカダミアナッツオイル 200ml &SH", "マカダミアナッツオイル 200ml"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100％ナチュラル マカダミアナッツオイル 200ml (高純度精製・サラリと馴染んでベタつかない消えるオイル・真冬の顔から首・ボディまで惜しみなく使える大容量高保湿オイル)"
            },
            {
                "rank": 6,
                "queries": ["ニベア プレミアムボディミルク モイスチャー", "ニベア プレミアムボディミルク", "ニベア モイスチャー プレミアム"],
                "brand": "NIVEA (ニベア花王)",
                "name": "プレミアムボディミルク モイスチャー 200g (高保湿マカデミアナッツオイル配合・真冬の粉吹きすねやガサガサ肘を吸い付くような潤いヴェールで満たす高保湿ボディミルク)"
            },
            {
                "rank": 7,
                "queries": ["自然化粧品研究所 マカデミアナッツオイル", "自然化粧品研究所 マカダミア", "マカデミアナッツオイル 100ml 自然化粧品研究所"],
                "brand": "自然化粧品研究所",
                "name": "精製 マカデミアナッツオイル 100ml (化粧品原料グレード・パルミトレイン酸の優れた浸透力で冬のスキンケアのプレ化粧水前ブースターとしても最適な高純度キャリアオイル)"
            },
            {
                "rank": 8,
                "queries": ["スパヒノキ マカダミアナッツオイル", "spa hinoki マカダミア", "スパヒノキ オイル"],
                "brand": "spa hinoki (スパヒノキ)",
                "name": "オーガニック マカダミアナッツオイル 100ml (コスモスオーガニック認証取得・真冬の乾燥による小ジワやゴワつきを柔らかくほぐし吸い付くような弾力肌へ整える最高級オイル)"
            },
            {
                "rank": 9,
                "queries": ["マカダミア ナチュラル オイル", "マカダミア オイル トリートメント", "マカダミア ヘアオイル"],
                "brand": "Macadamia Natural Oil (マカダミアナチュラルオイル)",
                "name": "ヒーリング オイルスプレー 125ml (マカダミアナッツ油×アルガンオイル・冬の静電気やパサつき・枝毛を濃密補修し一日中シルクのような艶髪をキープする高機能ヘアミスト)"
            },
            {
                "rank": 10,
                "queries": ["マカダミアナッツ バター 50g", "マカダミア バター 50g", "マカダミア バーム"],
                "brand": "Mandy Moon Raw Butter (マンディムーン)",
                "name": "マカダミアナッツ バター 50g (水素添加マカダミア油・体温でとろける極上テクスチャー・冬の唇のひび割れや目元の激しい乾燥を密着保護する高保湿植物性バター)"
            }
        ]
    },
    "winter_pomegranate_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ5プニカ酸が真冬のしぼみ肌に濃密な弾力と潤いを呼び戻す高保湿ザクロオイルコスメランク10",
        "file": "winter-pomegranate-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ヴェレダ ざくろ ファーミングフェイシャルオイル", "ヴェレダ ざくろ フェイシャルオイル", "ヴェレダ ざくろ オイル 30ml"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ざくろ ファーミングフェイシャルオイル 30ml (希少なプニカ酸濃縮配合・冬の寒冷でハリを失いしぼんだ肌を内側からピンと押し上げる最高峰エイジングトリートメントオイル)"
            },
            {
                "rank": 2,
                "queries": ["ヴェレダ ざくろ オイル 100ml", "ヴェレダ ざくろ ボディオイル", "ヴェレダ ざくろ 100ml"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ざくろ モイスチャーオイル 100ml ポンプ付 (有機ザクロ種子油×マカダミアナッツ油・真冬の冷え固まったボディをしっとり引き締めビロードのような潤いを与えるプレミアムオイル)"
            },
            {
                "rank": 3,
                "queries": ["&SH ポメグラネート オイル", "ポメグラネート オイル 50ml", "ポメグラネートオイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100％ナチュラル ポメグラネート オイル 50ml (低温圧搾ザクロ種子油100%・プニカ酸と抗酸化ポリフェノールが真冬の枯れ肌に驚異の保水膜を形成するピュアシードオイル)"
            },
            {
                "rank": 4,
                "queries": ["ザクロオイル 未精製 オーガニック", "ザクロオイル オーガニック", "ザクロオイル 50ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オーガニック ザクロオイル（未精製） 10ml (有機栽培ザクロ種子油・希少なプニカ酸を約70%含有し真冬の目元やほうれい線の乾燥小ジワをふっくら満たす原液美容オイル)"
            },
            {
                "rank": 5,
                "queries": ["ざくろ オイル 100ml ポンプ付", "ざくろ オイル 100ml", "ヴェレダ ざくろ オイル"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ざくろ ボディオイル 100ml 大容量 (オーガニックプニカ酸×ホホバ種子油・冬の冷え固まった肌を温めながらマッサージし内側から弾むようなツヤとハリを与える名品オイル)"
            },
            {
                "rank": 6,
                "queries": ["ザクロシードオイル", "ポメグラネート シードオイル", "ザクロ オイル 美容"],
                "brand": "Natural Beauty (ナチュラルビューティー)",
                "name": "オーガニック ザクロシードオイル 30ml (高純度コールドプレス・真冬の過酷な寒冷乾燥でキメが乱れた大人肌を濃密なオメガ5ヴェールで保護するエイジングオイル)"
            },
            {
                "rank": 7,
                "queries": ["イオス シア ボディローション ザクロ", "イオス ザクロ", "ザクロ ボディローション"],
                "brand": "EOS (イオス)",
                "name": "シアベター ボディローション ザクロ＆ラズベリー 473ml (天然シアバター×ザクロ種子油・冬の乾燥肌を24時間濃密保湿しフルーティーな香りで包み込む高保湿大容量ローション)"
            },
            {
                "rank": 8,
                "queries": ["ヴェレダ ざくろ ファーミングローション", "ざくろ 化粧水 ヴェレダ", "ざくろ ファーミングローション"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ざくろ ファーミングローションEX 145ml (ザクロ果実エキス×シロキクラゲ多糖体・真冬の乾いた角層を潤いで満たし吸い付くようなもっちり肌に整える高保湿プレミアム化粧水)"
            },
            {
                "rank": 9,
                "queries": ["アンダルーナチュラルズ ザクロ", "Andalou ザクロ", "アンダルー イルミネーティング セラム"],
                "brand": "Andalou Naturals (アンダルーナチュラルズ)",
                "name": "イルミネーティング トリートメントセラム ザクロ 32ml (ザクロ種子油×フルーツ幹細胞複合体・冬の紫外線ダメージと乾燥くすみを同時に晴らす高保湿エイジング美容液)"
            },
            {
                "rank": 10,
                "queries": ["フルーツルーツ ザクロ", "FRUITS ROOTS ザクロ", "フルーツルーツ オイル"],
                "brand": "fruits roots (フルーツルーツ)",
                "name": "ジューシー クレンジングオイル ザクロ 100ml (国産オーガニックザクロエキス×コメ胚芽油・真冬の乾いたメイク汚れを潤いを残しながらするんと落とす高保湿植物クレンジング)"
            }
        ]
    },
    "winter_rice_bran_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然ガンマ-オリザノールと濃密ビタミンEが真冬の冷えくすみ＆バリア枯渇を救う高保湿米ぬかオイルコスメランク10",
        "file": "winter-rice-bran-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["美人ぬか 純米 美容オイル", "美人ぬか 純米乳液", "美人ぬか 純米 保湿"],
                "brand": "美人ぬか (リアル)",
                "name": "純米 美容オイル 30ml (米ぬか美肌成分×純度100%植物油・真冬の寒冷でゴワつく肌に米ぬかセラミドとオリザノールが濃密に浸透し吸い付くような白玉肌へ導くフェイシャルオイル)"
            },
            {
                "rank": 2,
                "queries": ["&SH ライスブランオイル", "ライスブランオイル 200ml &SH", "ライスブランオイル 200ml"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100％ナチュラル ライスブランオイル（米油） 200ml (国内精製無添加・天然オリザノールとオレイン酸が冬の角層バリアの隙間を埋め尽くす高コスパ高保湿キャリアオイル)"
            },
            {
                "rank": 3,
                "queries": ["みんなでみらいを 米ぬかオイル", "米ぬかオイルセラム", "米ぬか 美容オイル 30ml"],
                "brand": "みんなでみらいを",
                "name": "米ぬか美容オイル 30ml (国産無農薬米ぬかオイル100%・冬の過酷な寒冷乾燥で荒れた角層をしっとり保護しキメの整った素肌へ導く無添加スキンケアオイル)"
            },
            {
                "rank": 4,
                "queries": ["ブランドリップ 100ml", "ブランドリップ 米ぬか", "米ぬか オイル ブランドリップ"],
                "brand": "Bran-Drip (ブランドリップ)",
                "name": "米ぬかスキンオイル ブランドリップ 100ml (食べる米ぬかから抽出した最高純度米ぬか油×ダマスクローズ油・冬の冷えによるくすみを晴らし極上の潤いを与えるプレミアムオイル)"
            },
            {
                "rank": 5,
                "queries": ["米油 キャリアオイル", "ライスブランオイル 1000ml", "こめ油 美容オイル"],
                "brand": "Nature Herb (ネイチャーハーブ)",
                "name": "国産 ライスブランオイル 1000ml ポンプ付 (国内産米ぬか100%・天然ビタミンEとγ-オリザノール高含有・真冬のお風呂上がり全身保湿に惜しみなく使える大容量高保湿オイル)"
            },
            {
                "rank": 6,
                "queries": ["生活の木 ライスブランオイル", "生活の木 プラントオイル ライス", "生活の木 コメヌカ"],
                "brand": "Tree of life (生活の木)",
                "name": "ライスブランオイル 25ml (コメヌカ油100%・冬の入浴後のブースターとして角層深部へすっと浸透し乾燥小ジワを目立たなくするスキンケアキャリアオイル)"
            },
            {
                "rank": 7,
                "queries": ["米ぬか美人 うるおいクリーム", "米ぬか美人 保湿クリーム", "米ぬか美人 クリーム"],
                "brand": "日本盛 (米ぬか美人)",
                "name": "米ぬか美人 うるおいクリーム 40g (老舗酒蔵の米ぬかエキス×日本酒酵母×水溶性コラーゲン・真冬の激しい乾燥と外気刺激から肌を守り抜く濃厚保湿リッチクリーム)"
            },
            {
                "rank": 8,
                "queries": ["自然化粧品研究所 ライスブランオイル", "自然化粧品研究所 コメヌカ油", "ライスブランオイル 100ml 自然化粧品研究所"],
                "brand": "自然化粧品研究所",
                "name": "精製 ライスブランオイル 100ml (医薬部外品原料規格・天然オリザノールとフェルラ酸が冬の冷えによるくすみをケアし透明感あふれる健やかな角層へ整える植物油)"
            },
            {
                "rank": 9,
                "queries": ["リアル 米ぬか パック", "純米パック リアル", "美人ぬか 純米パック"],
                "brand": "リアル (美人ぬか)",
                "name": "純米パック 100g (米ぬかエキス×コメ胚芽油×黒砂糖エキス・真冬の固くなった古い角質をやさしく包んで落とし水分がぐんぐん入る柔らかな素肌に整える洗い流しパック)"
            },
            {
                "rank": 10,
                "queries": ["お米のオイル 三和油脂", "三和油脂 まいにちのこめ油", "コメ胚芽油 美容"],
                "brand": "三和油脂 (SANWA)",
                "name": "純国産 コメ胚芽油 スキン＆ヘアケア 100ml (玄米100kgからわずか1kgしか採れない超濃密胚芽油・冬のパサつく髪の毛先や指先のひび割れまで全身を濃密保護するマルチオイル)"
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
                    except urllib.error.HTTPError as e:
                        if e.code == 429:
                            print(f"  Rate limited (429), waiting 5.5s...")
                            time.sleep(5.5)
                        else:
                            print(f"  HTTP error: {e.code}")
                    except Exception as e:
                        print(f"  Error: {e}")
                
                if chosen_item:
                    break
            
            if chosen_item:
                total_success += 1
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0].get("imageUrl", "")
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0].get("imageUrl", "")
                
                # 画像を高解像度化
                img_url = img_url.replace("?_ex=128x128", "?_ex=300x300")
                aff_url = chosen_item.get("affiliateUrl", chosen_item.get("itemUrl", ""))
                price = chosen_item.get("itemPrice", 0)
                
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "name": item["name"],
                    "rakuten_name": chosen_item.get("itemName", ""),
                    "price": f"¥{price:,}",
                    "raw_price": price,
                    "img": img_url,
                    "url": aff_url
                })
                print(f"  -> Rank {item['rank']} SUCCESS: {item['brand']} - ¥{price:,}")
            else:
                print(f"  ❌ Rank {item['rank']} FAILED to fetch from Rakuten API!")

    with open("fetched_3new_macadamia_pomegranate_ricebran.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Fetch finished! Successfully retrieved {total_success} / {total_needed} items.")
    print(f"Saved to fetched_3new_macadamia_pomegranate_ricebran.json")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
