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
    "winter_murumuru_butter": {
        "title": "保湿力の強さで肌乾燥とさようなら！アマゾンの高密着エモリエントが真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿ムルムルバターコスメランク10",
        "file": "winter-murumuru-butter.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ムルムルバター 精製 200g"],
                "brand": "mandy moon (マンディムーン)",
                "name": "ムルムルバター・精製 200g (クリア・Refined) (アマゾンのヤシ種子から抽出・シアバターを超える高融点と持続性保水膜で真冬の硬化したかかとやひじ、粉吹き手肌をベルベットのようになめらかにほぐす高純度バター)"
            },
            {
                "rank": 2,
                "queries": ["ムルムルバター 精製 50g"],
                "brand": "mandy moon (マンディムーン)",
                "name": "ムルムルバター・精製 50g (クリア・Refined) (お試しサイズ・体温でじんわりとろけて肌にピタッと吸着・真冬の頑固なひび割れや乾燥小ジワを濃密にラッピングする万能植物バター)"
            },
            {
                "rank": 3,
                "queries": ["LUSH 抱擁の満月 保湿クリーム", "LUSH 抱擁の満月"],
                "brand": "LUSH (ラッシュ)",
                "name": "抱擁の満月 (Full of Grace) フェイシャルセラムバー 20g (ムルムルバター×ローズオイル×カモミール配合・固形から体温でとろけるオイル美容液バー・真冬の極寒乾燥と暖房風で強張った素肌をふっくら柔らかく満たす至高のフェイシャルケア)"
            },
            {
                "rank": 4,
                "queries": ["モルトベーネ ロレッタ ムルムルバター 30g", "ロレッタ ムルムルバター 30g"],
                "brand": "Loretta (ロレッタ / モルトベーネ)",
                "name": "ロレッタ ムルムルバター 30g (天然ムルムルバター×ダマスクローズオイル配合・細い髪やパサつく冬の毛先に自然なツヤとまとまりを与え、そのまま手肌のハンドバームとしても使える洗い流さないトリートメント)"
            },
            {
                "rank": 5,
                "queries": ["ロレッタ ナイトケアクリーム 120g", "ロレッタ ナイトケアクリーム"],
                "brand": "Loretta (ロレッタ / b-ex)",
                "name": "ナイトケアクリーム 120g (ムルムルバター×バオバブオイル配合・寝ている間に真冬の暖房乾燥でパサついた髪深部まで潤いを浸透補修し、翌朝の寝癖や広がりを抑えるアウトバスヘアミルク)"
            },
            {
                "rank": 6,
                "queries": ["ハウスオブローゼ モイストリップ", "ムーミン モイストリップ Y ハウスオブローゼ"],
                "brand": "HOUSE OF ROSE (ハウスオブローゼ)",
                "name": "モイストリップ (ムルムルバター＆セラミド配合) 3.5g (体温でとろけるムルムルバターが真冬の冷たい木枯らしから唇を死守・皮むけや縦ジワを防ぎ、ぷるんとした潤い膜を長時間キープする高保湿リップ)"
            },
            {
                "rank": 7,
                "queries": ["&SH ムルムルバター 100g", "&SH ムルムルバター 50g"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "オーガニック ムルムルバター 100g (精製・無添加) (高い抱水性を持つラウリン酸・ミリスチン酸が豊富・冬の手作り高保湿バームや手持ちクリームのブーストに最適なピュアバター)"
            },
            {
                "rank": 8,
                "queries": ["ルベル イオセラム マスク 170g", "ルベル イオセラム マスク"],
                "brand": "LebeL (ルベル / タカラベルモント)",
                "name": "イオセラム マスク 170g (クプアスバター×ムルムルバター高配合・真冬の乾燥でパサつきうねる頑固なくせ毛・ハイダメージ毛を濃密な植物脂ヴェールで芯から包み込む集中ヘアマスク)"
            },
            {
                "rank": 9,
                "queries": ["ビオーブ ピュリム リペアスキャルプトリートメント"],
                "brand": "DEMI (デミ コスメティクス)",
                "name": "ビオーブ ピュリム リペアスキャルプトリートメント 240g / 2000g (ムルムルバター×薬用有効成分配合・冬の寒冷で乾燥しかゆみが出やすい大人の頭皮と髪に潤いを与え、ふんわりしなやかに整えるスキャルプパック)"
            },
            {
                "rank": 10,
                "queries": ["ジェミールフラン メルティバター バーム 40g", "ジェミールフラン メルティバター バーム"],
                "brand": "MILBON (ミルボン / ジェミールフラン)",
                "name": "メルティバター バーム 40g (ムルムルバター×シアバター配合・夜のドライヤー熱で溶けて朝まで記憶・真冬の乾燥による毛先のハネやパサつきを抑えてハンドクリームにもなる濃密バーム)"
            }
        ]
    },
    "winter_cranberry_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ3・6・9とスーパービタミンEが真冬の寒冷くすみ＆酸化乾燥を撃退する高保湿クランベリーシードオイルコスメランク10",
        "file": "winter-cranberry-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["オイルマルシェ クランベリー 10ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オイルマルシェ・クランベリー 10ml (未精製・コールドプレス) (オメガ3・6・9が黄金バランス・スーパービタミンEトコトリエノールが冬の寒冷血行不良によるどんよりくすみと乾燥を瞬時に晴らすピュア美容オイル)"
            },
            {
                "rank": 2,
                "queries": ["&SH クランベリーオイル 10ml"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "オーガニック クランベリーシードオイル 10ml (未精製・100%植物性) (ビタミンEの40倍以上の抗酸化力を持つトコトリエノール含有・真冬の暖房乾燥による皮脂の酸化を防ぎふっくらキメを整える導入美容オイル)"
            },
            {
                "rank": 3,
                "queries": ["クランベリーオイル オーガニック 30ml", "クランベリーオイル 30ml"],
                "brand": "Natural Elements (ナチュラルエレメンツ)",
                "name": "ピュア クランベリーシードオイル 30ml (オーガニック認証・コールドプレス未精製) (寒冷地育ちの果実が蓄えた濃密必須脂肪酸が角層深部へスッと馴染み、冬の粉吹き肌をごわつきゼロのやわ肌へ導くエイジングケアオイル)"
            },
            {
                "rank": 4,
                "queries": ["MiMC ミネラルクリーミーアイベース", "ミネラルクリーミーアイベース MiMC"],
                "brand": "MiMC (エムアイエムシー)",
                "name": "ミネラルクリーミーアイベース (クランベリー種子油配合) (目元の皮膚が最も薄く乾燥しやすい冬に最適・クランベリー種子油と植物美容液成分でアイメイクしながらデリケートな目元を一日中高保湿ケアするクリームベース)"
            },
            {
                "rank": 5,
                "queries": ["ナチュラグラッセ スキンバランシング ベース", "スキンバランシングベース ナチュラグラッセ"],
                "brand": "naturaglace (ナチュラグラッセ)",
                "name": "スキンバランシング ベース 25ml (クランベリー種子油×サジーオイル配合・SPF31 PA++・冬の乾燥と寒冷くすみを自然なツヤで飛ばし一日中しっとり潤い膜をキープする高保湿美容液下地)"
            },
            {
                "rank": 6,
                "queries": ["グロウン アルケミスト クランベリー バランシング トナー", "グロウン アルケミスト クランベリー"],
                "brand": "GROWN ALCHEMIST (グロウン・アルケミスト)",
                "name": "バランシング トナー (ローズ・ギンコ＆クランベリー) 200ml (オーストラリア発オーガニック・クランベリー種子＆果実エキスが冬のインナードライ毛穴を引き締めながら角層の水分保持力を限界まで引き上げる高機能化粧水)"
            },
            {
                "rank": 7,
                "queries": ["リアルフレッシュフォームクランベリー NEOGEN", "リアルフレッシュフォーム クランベリー"],
                "brand": "NEOGEN (ネオゼン)",
                "name": "リアルフレッシュ フォーム クランベリー 160g (本物クランベリー発酵エキス配合・ボトル底に本物の果実を漬け込んだ贅沢処方・冬の乾燥くすんだ角質をやさしい濃密ホイップ泡で洗い落とす美容液洗顔フォーム)"
            },
            {
                "rank": 8,
                "queries": ["CBD リップバーム クランベリー", "CBD リップバーム 保湿リップ クランベリー"],
                "brand": "CANNAX (カンナックス)",
                "name": "CBD 高保湿リップバーム (ハニー＆クランベリー) 10g (クランベリー種子油×CBD50mg×ハチミツ配合・真冬の冷風でガサガサに荒れた唇を体温でとろけるオイルヴェールで密着保護するリペアリップ)"
            },
            {
                "rank": 9,
                "queries": ["&SH クランベリーシードオイル オーガニック", "&SH クランベリーオイル 50ml"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "オーガニック クランベリーシードオイル 50ml (高純度コールドプレス抽出・真冬の粉吹き肌や目元・口元の小ジワにぐんぐん浸透・ベタつかずシルクのような滑らかさを保つ大容量オイル)"
            },
            {
                "rank": 10,
                "queries": ["ニックス リップ IV クランベリー", "ゾンケ クランベリー ルージュ", "クランベリー フェイスオイル"],
                "brand": "NYX Professional / Botanical Lab",
                "name": "ハイドレーティング リップオイル セラム (クランベリー) 4.2ml (クランベリーオイル高配合・冬の乾燥した唇に美容液オイルの濃密なうるおいとぷるんとしたガラスのようなツヤを与えるケア＆グロスリップ)"
            }
        ]
    },
    "winter_emu_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！人肌とほぼ同等の皮脂組織が真冬の粉吹き乾燥・ガサガサあかぎれ肌に瞬時に溶け込む高保湿エミューオイルコスメランク10",
        "file": "winter-emu-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エミューの雫 72ml"],
                "brand": "エミューの雫 (Emu no Shizuku)",
                "name": "エミューの雫 72ml (100%無添加・高品質エミューオイル) (人間の皮脂と極めて近い脂肪酸バランス・オーストラリア特許製法OILTEK精製・真冬の粉吹き肌やすねのかゆみ、水仕事のあかぎれ手肌に瞬時に浸透する最高峰保湿オイル)"
            },
            {
                "rank": 2,
                "queries": ["エミューの雫 15ml"],
                "brand": "エミューの雫 (Emu no Shizuku)",
                "name": "エミューの雫 お試しサイズ 15ml (持ち歩き用・ポーチ常備サイズ・真冬の乾燥でひび割れやすい唇や目元・口元の小ジワ、指先のささくれにひと塗りで極上のうるおいを与えるレスキューオイル)"
            },
            {
                "rank": 3,
                "queries": ["エミューム 60ml"],
                "brand": "EMUME (エミューム / 日本エミュー協会認定)",
                "name": "エミューム 60ml (無添加エミューオイル100%) (日本エミュー協会認定の安心品質・浸透力とエモリエント持続性が抜群・冬のガサガサかかとや関節周りの乾燥、赤みが出やすいデリケート肌を優しく鎮静)"
            },
            {
                "rank": 4,
                "queries": ["キダデラックスクリーム 200g", "キダデラックス 200g エミューオイル"],
                "brand": "野口医学研究所 (KIDA DX)",
                "name": "キダデラックス 高浸透エミュークリーム 200g (高純度エミューオイル×MSM×グルコサミン配合・真冬の寒冷でこわばった関節や首肩を温めながら、極度の乾燥で硬化した皮膚を柔らかく解きほぐす高機能ボディクリーム)"
            },
            {
                "rank": 5,
                "queries": ["オイル・オブ・エミュー 285ml", "オイルオブエミュー"],
                "brand": "OIL OF EMU (オイル・オブ・エミュー)",
                "name": "オイル・オブ・エミュー 285ml (オーストラリア政府認定・医療レベル精製100%ピュアオイル) (プロアスリートやサロンでも愛用・真冬の頑固な粉吹きすねや背中の乾燥かゆみに惜しみなく使える大容量最高峰オイル)"
            },
            {
                "rank": 6,
                "queries": ["エミューの雫 石鹸", "エミューフェイスソープ"],
                "brand": "エミューの雫 (Emu no Shizuku)",
                "name": "エミューフェイスソープ 100g (枠練り熟成製法・エミューオイル高配合石鹸・もっちりとしたキメ細かい弾力泡が汚れだけを吸着し、冬の洗顔後も化粧水がいらないほどしっとり潤い膜を残す洗顔ソープ)"
            },
            {
                "rank": 7,
                "queries": ["emure balm エミューバーム", "エミューバーム 50g"],
                "brand": "emure (エミュレ)",
                "name": "emure balm (エミューバーム) 50g (エミューオイル×天然植物バター配合・体温でスッと溶けて肌奥まで密着・真冬の水仕事であかぎれた指先や粉吹くかかと、ひじのひび割れを集中ガードする濃厚保湿バーム)"
            },
            {
                "rank": 8,
                "queries": ["網走 エミューオイル", "エミューモイスチャークリーム 網走産"],
                "brand": "オホーツクエミュー (北海道網走産)",
                "name": "エミュー モイスチャークリーム 50g (北海道網走産エミューオイル使用) (日本の寒冷地・オホーツクで育まれた高品質エミューオイルを贅沢に配合・真冬の厳しい寒風に晒される素肌を濃密な潤いで守る純国産クリーム)"
            },
            {
                "rank": 9,
                "queries": ["エミュークリーム 40g", "エミューオイル クリーム 40g"],
                "brand": "Emu Cream Japan (エミュークリーム)",
                "name": "エミュークリーム 40g (オメガ3・6・9＆ビタミン配合) (持ち歩きに便利なチューブタイプ・真冬の外出先で指先やひじ、目元が乾燥したときにサッと塗れてベタつかず深層までしっとり整える高保湿ハンド＆ボディクリーム)"
            },
            {
                "rank": 10,
                "queries": ["国産 エミュー オイル 100ml", "エミューオイル 100ml"],
                "brand": "Natural Emu Oil (国産エミュー)",
                "name": "国産ピュア エミューオイル 100ml (天然無添加100%・オメガ3・6・9高含有) (お風呂上がりの濡れた肌に全身伸ばせる大容量・人間の皮脂膜と同じ構造でバリア機能を補強し真冬の粉吹き・かゆみ乾燥を完全ブロック)"
            }
        ]
    }
}

def fetch_all():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Rank {item['rank']}: Trying '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                for attempt in range(3):
                    try:
                        time.sleep(2.5) # レートリミット回避
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
                        time.sleep(3.5)
                
                if chosen_item:
                    print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                    break

            if chosen_item:
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
                    "review_average": chosen_item.get("reviewAverage", "0.0")
                })
            else:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_murumuru_cranberry_emu.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_murumuru_cranberry_emu.json!")

if __name__ == "__main__":
    fetch_all()
