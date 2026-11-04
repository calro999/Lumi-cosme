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
    "winter_damask_rose": {
        "title": "保湿力の強さで肌乾燥とさようなら！女王の濃密潤いヴェールで真冬のしぼみ肌をふっくら満たす高保湿ダマスクローズコスメランク10",
        "file": "winter-damask-rose.html",
        "items": [
            {
                "rank": 1,
                "queries": ["メルヴィータ フラワーブーケ ローズ", "メルヴィータ フラワーブーケ ローズ EX", "メルヴィータ ローズ 化粧水"],
                "brand": "Melvita (メルヴィータ)",
                "name": "フラワーブーケ ローズ EX トナー 100ml (ダマスクローズ蒸留水×マイクロヒアルロン酸・真冬のゴワつく角層を瞬時に満たし吸い付くようなハリとツヤを与える高保湿とろみ化粧水)"
            },
            {
                "rank": 2,
                "queries": ["アルテヤオーガニック ブルガリアンローズ", "アルテヤオーガニック フェイスオイル", "アルテヤ ブルガリアンローズ"],
                "brand": "Alteya Organics (アルテヤオーガニック)",
                "name": "ブルガリアンローズ フェイスオイル 30ml (本場ブルガリアの有機ダマスクローズ精油を濃密配合・冬の冷風で枯れ果てた肌を濃密な油分膜で包み込みふっくら蘇らせるエイジングオイル)"
            },
            {
                "rank": 3,
                "queries": ["ニールズヤード ワイルドローズ ビューティバーム", "ニールズヤード ビューティバーム", "ニールズヤード ローズ バーム"],
                "brand": "NEAL'S YARD REMEDIES (ニールズヤード)",
                "name": "ワイルドローズ ビューティバーム 50g (ビタミンC豊富なローズヒップ×ダマスクローズ・真冬の乾燥粉吹きやひび割れ肌を寝ている間に集中リペアする濃厚マルチバーム)"
            },
            {
                "rank": 4,
                "queries": ["ジュリーク ローズ バランシングミスト", "ジュリーク ミスト ローズ", "ジュリーク ローズ"],
                "brand": "Jurlique (ジュリーク)",
                "name": "ローズ バランシングミスト 100ml (自社オーガニック農園の朝摘みダマスクローズエキス・暖房でカラカラに乾いた日中の肌に微細な潤いヴェールを密着させる高保湿ミスト)"
            },
            {
                "rank": 5,
                "queries": ["ROSE LABO ローズマルチミスト", "ROSE LABO ローズ 美容液", "ROSE LABO"],
                "brand": "ROSE LABO (ローズラボ)",
                "name": "ローズマルチミスト 50ml (食べられるバラから抽出した国産ダマスクローズ水×セラミド・メイクの上から瞬時に潤いと自然なツヤを吹き込み乾燥崩れをブロックする2層式ミスト)"
            },
            {
                "rank": 6,
                "queries": ["ドクターハウシュカ ローズ デイクリーム", "Dr.ハウシュカ ローズ デイクリーム", "ハウシュカ ローズ デイクリーム"],
                "brand": "Dr. Hauschka (ドクターハウシュカ)",
                "name": "ローズ デイクリーム 30ml (貴重なダマスクローズ花エキスとミツロウ・シア脂の黄金比・真冬の厳しい寒風と乾燥から肌を守り抜くロングセラー高保湿デイクリーム)"
            },
            {
                "rank": 7,
                "queries": ["ハウスオブローゼ ラ・ローゼ ボディミルク", "ハウスオブローゼ ラ・ローゼ", "ハウスオブローゼ ラローゼ"],
                "brand": "HOUSE OF ROSE (ハウスオブローゼ)",
                "name": "ラ・ローゼ ボディミルク RG 150ml (朝摘みダマスクローズの天然芳香×ヒアルロン酸・真冬の入浴後に全身を優雅な香りと吸い付くような潤いで包み込む高保湿ボディ乳液)"
            },
            {
                "rank": 8,
                "queries": ["生活の木 フローラルウォーター ローズ", "生活の木 ダマスクローズ フローラルウォーター", "生活の木 ローズウォーター"],
                "brand": "Tree of life (生活の木)",
                "name": "フローラルウォーター ブルガリアン ダマスクローズ 100ml (水蒸気蒸留法による純度100%植物芳香蒸留水・冬のスキンケアのプレ化粧水として乾いた角層を潤す天然フローラルウォーター)"
            },
            {
                "rank": 9,
                "queries": ["パニエデサンス ローズ ハンドクリーム", "パニエデサンス ローズ", "パニエデサンス ハンドクリーム"],
                "brand": "Panier des Sens (パニエデサンス)",
                "name": "エッセンシャルズ ハンドクリーム ローズ 75ml (プロヴァンス産ダマスクローズエキス×シアバター20%・真冬の水仕事や冷風で荒れた手肌をしっとり濃密保護するハンドケア)"
            },
            {
                "rank": 10,
                "queries": ["サンタマリアノヴェッラ ローズウォーター", "サンタマリア ローズウォーター", "ローズウォーター サンタマリアノヴェッラ"],
                "brand": "Santa Maria Novella (サンタ・マリア・ノヴェッラ)",
                "name": "アックア・ディ・ローゼ（ローズウォーター） 250ml (イタリア修道院伝統のダマスクローズ蒸留水・真冬の敏感になった素肌を優しく引き締めリッチな潤いを与える伝統の高保湿化粧水)"
            }
        ]
    },
    "winter_evening_primrose": {
        "title": "保湿力の強さで肌乾燥とさようなら！奇跡のγ-リノレン酸が真冬の深刻なバリア崩壊を救う高保湿月見草オイルコスメランク10",
        "file": "winter-evening-primrose.html",
        "items": [
            {
                "rank": 1,
                "queries": ["&SH イブニングプリムローズオイル", "イブニングプリムローズオイル 精製", "月見草オイル 200ml"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100％ナチュラル イブニングプリムローズオイル（月見草オイル） 200ml (高純度精製・γ-リノレン酸を豊富に含み真冬の極度な乾燥・皮むけ肌を救済する大容量高保湿キャリアオイル)"
            },
            {
                "rank": 2,
                "queries": ["マンディムーン 月見草オイル", "マンディムーン イブニングプリムローズ", "月見草オイル 50ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オーガニック 月見草オイル（イブニングプリムローズ） 50ml (未精製コールドプレス・真冬の角層バリアの隙間を埋めて水分蒸発を強力ストップする高機能エイジングリペアオイル)"
            },
            {
                "rank": 3,
                "queries": ["イブニングプリムローズオイル 精製 オーガニック", "イブニングプリムローズオイル 精製", "月見草オイル 精製"],
                "brand": "Organic Botanics (オーガニックボタニクス)",
                "name": "ピュア イブニングプリムローズ 精製オイル 50ml (有機栽培月見草種子・冬の更年期乾燥やホルモンバランス乱れによるカサつき肌をしっとり柔軟に整える高純度低刺激オイル)"
            },
            {
                "rank": 4,
                "queries": ["トリロジー オイル 20ml", "トリロジー ロザピンプラス", "トリロジー ローズヒップオイル"],
                "brand": "trilogy (トリロジー)",
                "name": "ロザピンプラス 30ml (ローズヒップ油×月見草油×クランベリー種子油の抗酸化シールド・冬の木枯らし乾燥とくすみ・シワを一掃する濃密マルチ美容オイル)"
            },
            {
                "rank": 5,
                "queries": ["カフェドサボン 月見草オイル", "月見草オイル カフェドサボン", "月見草オイル 50ml 未精製"],
                "brand": "Cafe de Savon (カフェ・ド・サボン)",
                "name": "未精製 月見草オイル 50ml (天然γ-リノレン酸9%以上・冬の寒暖差で硬くなった大人のゴワつき肌を吸い付くようなマシュマロ肌へ導く濃厚スキンケアオイル)"
            },
            {
                "rank": 6,
                "queries": ["ナウフーズ 月見草オイル", "Now Foods 月見草オイル", "Now Foods イブニングプリムローズ"],
                "brand": "NOW Foods (ナウフーズ)",
                "name": "イブニングプリムローズ ピュアオイル 118ml (低温圧搾ヘキサンフリー・冬の顔・首・デコルテ・ボディまで惜しみなく使える大容量高コスパ高保湿オイル)"
            },
            {
                "rank": 7,
                "queries": ["ヴェレダ ワイルドローズ ボディオイル", "ヴェレダ ワイルドローズ オイル", "ヴェレダ ざくろ オイル"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ワイルドローズ モイスチャーオイル 100ml ポンプ付 (月見草油×モスカータバラ種子油・冬の冷え固まった肌をほぐしビロードのような滑らかさと高密度の潤いを与えるプレミアムオイル)"
            },
            {
                "rank": 8,
                "queries": ["ニールズヤード フランキンセンス インテンス クリーム", "ニールズヤード インテンス クリーム", "ニールズヤード クリーム"],
                "brand": "NEAL'S YARD REMEDIES (ニールズヤード)",
                "name": "フランキンセンス インテンス リッチクリーム 50g (月見草油×フランキンセンス×バオバブ・真冬の極乾燥下でも濃密な潤いヴェールが持続する最高峰エイジングケアクリーム)"
            },
            {
                "rank": 9,
                "queries": ["クナイプ ビオ オイル", "クナイプ オイル 100ml", "クナイプ ビオオイル"],
                "brand": "Kneipp (クナイプ)",
                "name": "ビオ オイル 100ml (天然植物オイルブレンド×月見草エキス・冬の入浴後の湿った素肌に素早く馴染み乾燥による粉吹きやキメの乱れをなめらかに修復するマルチオイル)"
            },
            {
                "rank": 10,
                "queries": ["カレンデュラ 月見草 オイル", "カレンデュラ オイル", "月見草 バーム"],
                "brand": "Herb Pharmacy (ハーブファーマシー)",
                "name": "スキンブースター フェイシャルオイル 30ml (月見草油×カレンデュラ×ボリジ油・真冬の過酷な寒冷刺激でピリつくデリケート肌を優しく鎮静＆保水するプレミアムオーガニックセラム)"
            }
        ]
    },
    "winter_moringa_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！生命の木がもたらす濃密なベヘン酸ヴェールで一日中乾かない高保湿モリンガオイルコスメランク10",
        "file": "winter-moringa-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["モリンガ 美容 オイル 30ml", "モリンガ スキンケアオイル 30ml", "国産モリンガオイル 30ml"],
                "brand": "ILOKOS (イロコス)",
                "name": "ピュア モリンガ スキンケアオイル 30ml (奇跡の木モリンガ種子油100%低温圧搾・真冬の激しい乾燥としぼみ肌を潤いでパンと押し上げる高純度ブースターオイル)"
            },
            {
                "rank": 2,
                "queries": ["生活の木 モリンガオイル", "生活の木 モリンガ", "モリンガオイル 生活の木"],
                "brand": "Tree of life (生活の木)",
                "name": "モリンガオイル 25ml (低温圧搾コールドプレス・オレイン酸とベヘン酸が冬の角層に濃密な油分膜を形成し一日中しっとり感が持続する純度100%植物美容オイル)"
            },
            {
                "rank": 3,
                "queries": ["マンディムーン モリンガオイル", "マンディムーン モリンガ", "モリンガオイル 50ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オーガニック モリンガオイル（未精製） 50ml (インド産有機モリンガ種子低温圧搾・冬のエアコン乾燥でゴワついた角質を瞬時に柔らかく解きほぐす高浸透ブースターオイル)"
            },
            {
                "rank": 4,
                "queries": ["スパトリートメント モリンガオイル", "スパトリートメント モリンガ", "スパトリートメント オイル"],
                "brand": "Spa treatment (スパトリートメント)",
                "name": "エッセンシャル モリンガオイル 30ml (天然モリンガ種子油100%・冬の乾燥小ジワやくすみが気になる大人の肌に吸い付くような潤いとハリをチャージするサロン品質オイル)"
            },
            {
                "rank": 5,
                "queries": ["ボタニカルファクトリー モリンガ", "BOTANICAL FACTORY モリンガ", "ボタニカルファクトリー オイル"],
                "brand": "BOTANICAL FACTORY (ボタニカルファクトリー)",
                "name": "鹿児島県産 プレミアムモリンガオイル 30ml (本土最南端の契約農家産無農薬モリンガ・冬の木枯らしに負けない健やかな保水バリアを育む完全無添加コールドプレスオイル)"
            },
            {
                "rank": 6,
                "queries": ["カフェドサボン モリンガオイル", "モリンガオイル カフェドサボン", "モリンガオイル 50ml 未精製"],
                "brand": "Cafe de Savon (カフェ・ド・サボン)",
                "name": "未精製 モリンガオイル 50ml (天然ベヘン酸・パルミチン酸含有・真冬のスキンケアの最後に1滴重ねるだけで乾燥蒸発を完全ガードする高保湿植物油)"
            },
            {
                "rank": 7,
                "queries": ["ガールズビーアンビシャス モリンガオイル", "GIRLS BE AMBITIOUS モリンガ", "GIRLS, BE AMBITIOUS モリンガオイル"],
                "brand": "GIRLS, BE AMBITIOUS (ガールズ・ビー・アンビシャス)",
                "name": "フェアトレード オーガニック モリンガオイル 30ml (フィリピン産最高品質モリンガ種子使用・冬の敏感肌や乾燥による赤み・皮むけをしっとり優しく包み込む美容オイル)"
            },
            {
                "rank": 8,
                "queries": ["モリンガ バーム", "モリンガ リップバーム", "モリンガ モイスチャーバーム"],
                "brand": "Moringa Farm (モリンガファーム)",
                "name": "モリンガ モイスチャーリペアバーム 20g (モリンガ種子油×天然ミツロウ・冬の目元・口元のひび割れや外出時の冷風ガードに最適な携帯用マルチバーム)"
            },
            {
                "rank": 9,
                "queries": ["モリンガ月桃石けん", "モリンガ ソープ", "モリンガ 石鹸"],
                "brand": "WELLNESS HAMLET (暮らしっく村)",
                "name": "モリンガ月桃石けん 80g (無農薬モリンガオイル×有機月桃蒸留水・真冬の乾いた肌の潤いを守りながら不要な古い角質をやさしくオフする高保湿洗顔ソープ)"
            },
            {
                "rank": 10,
                "queries": ["モリンガ シャンプー オーガニック", "モリンガ ヘアオイル", "モリンガ シャンプー"],
                "brand": "Herb & Co. (ハーブアンドコー)",
                "name": "オーガニック モリンガ リッチヘアオイル 100ml (モリンガオイル×アルガンオイル・冬の静電気や暖房乾燥でパサつく毛先に濃密なツヤとまとまりを与えるアウトバストリートメント)"
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

    with open("fetched_3new_rose_primrose_moringa.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Fetch finished! Successfully retrieved {total_success} / {total_needed} items.")
    print(f"Saved to fetched_3new_rose_primrose_moringa.json")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
