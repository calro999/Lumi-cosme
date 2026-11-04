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
    "winter_tamanu_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！森の薬局が叶える奇跡の濃密保水膜・冬枯れ肌を蘇らせる高保湿タマヌオイルコスメランク10",
        "file": "winter-tamanu-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["SHIRO タマヌ オイルインセラム", "SHIRO タマヌオイルインセラム", "SHIRO タマヌ"],
                "brand": "SHIRO (シロ)",
                "name": "タマヌ オイルインセラム 30ml (奇跡の木タマヌオイル×酒粕エキス・真冬の硬直肌をときほぐし濃密なツヤとハリで満たす2層式高保湿導入美容液)"
            },
            {
                "rank": 2,
                "queries": ["ボタニカノン オイル", "ボタニカノン タマヌ", "BOTANICANON タマヌオイル"],
                "brand": "BOTANICANON (ボタニカノン)",
                "name": "タマヌオイル リッチピュア 20ml (鹿児島県南大隅町産無農薬タマヌ種子低温圧搾・冬の寒風による赤みや乾燥肌荒れを速攻レスキューする濃密ピュアオイル)"
            },
            {
                "rank": 3,
                "queries": ["タマヌオイル 未精製", "マンディムーン タマヌ", "タマヌオイル 50ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オーガニック未精製タマヌオイル 20ml/50ml (伝統的なコールドプレス製法・カロフィロリードとオメガ脂肪酸が真冬の深刻なカサつきと角層荒れを物理シールドする美容オイル)"
            },
            {
                "rank": 4,
                "queries": ["石垣島タマヌオイル 30ml", "タマヌオイル 100%", "タマヌ オイル 原液"],
                "brand": "Natural Pure Oils (石垣島オーガニック)",
                "name": "石垣島ピュア タマヌオイル 30ml (国産無農薬・深緑色の濃厚な1滴が冬のゴワつく乾燥肌を驚くほどしなやかに整える高純度ボタニカルオイル)"
            },
            {
                "rank": 5,
                "queries": ["シロ タマヌ クレンジングバーム 90g", "SHIRO タマヌ クレンジングバーム", "タマヌ クレンジング"],
                "brand": "SHIRO (シロ)",
                "name": "タマヌ クレンジングバーム 90g (タマヌオイルと甘酒エキスを凝縮・真冬のメイクや毛穴汚れをとろりとオフしながら極上の潤い膜を残すプレミアムバーム)"
            },
            {
                "rank": 6,
                "queries": ["オーガニック タマヌ オイル 30ml", "タマヌ バーム", "タマヌ モイスチャーバーム"],
                "brand": "Island Herbals (オーガニックタマヌ)",
                "name": "オーガニック タマヌ スキンリペアオイル 30ml (カロフィラム種子油100%・冬の目元・口元・指先のひび割れや粉吹きをピンポイントで密閉保護する高純度リペアオイル)"
            },
            {
                "rank": 7,
                "queries": ["Sierra Bees オーガニック リップクリーム", "タマヌ リップ", "タマヌ クリーム"],
                "brand": "Sierra Bees (シエラビーズ)",
                "name": "オーガニック タマヌ＆ティーツリー バームスティック 8種パック (未精製タマヌオイル×天然ミツロウ配合・真冬の過酷な寒冷でもカサつきを許さず密着保護する高保湿バーム)"
            },
            {
                "rank": 8,
                "queries": ["HONUA Surfrider ヤラブ フェイス＆ボディソープバー", "タマヌ 石鹸", "タマヌ ソープ"],
                "brand": "HONUA (ホヌア)",
                "name": "ヤラブ（タマヌ）フェイス＆ボディソープバー 枠練固形石鹸 100g (沖縄産タマヌオイルと枠練り製法・冬の古い角質を摩擦レスで吸着オフしながらしっとり洗い上げる洗顔バー)"
            },
            {
                "rank": 9,
                "queries": ["Sierra Bees リップクリーム", "タマヌ リップバーム", "タマヌ リップクリーム"],
                "brand": "Sierra Bees (シエラビーズ)",
                "name": "オーガニック エキストラモイスト タマヌリップバーム 4.25g (低温圧搾タマヌオイルとビタミンE・真冬の冷風で皮むけした唇を瞬時に濃密ラッピングする高保湿リップ)"
            },
            {
                "rank": 10,
                "queries": ["naure トラベルセット タマヌオイル", "タマヌ オイル スキンケア", "タマヌ フェイスオイル"],
                "brand": "naure (ナウレ)",
                "name": "naure 沖縄産タマヌオイル スキンケアプレミアムセット (ビタミンE高含有・真冬の乾燥小ジワや寒暖差による乾燥くすみを跳ね返し健やかなハリ肌へ導くエイジングケアセット)"
            }
        ]
    },
    "winter_baobab_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！生命の木が蓄える驚異の保水力で真冬のカチコチ肌を解きほぐす高保湿バオバブオイルコスメランク10",
        "file": "winter-baobab-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ミルボン エルジューダ MO", "エルジューダ MO 120ml", "ミルボン エルジューダ"],
                "brand": "MILBON (ミルボン)",
                "name": "ディーセス エルジューダ MO 120ml (アフリカ産バオバブオイル配合・冬の乾燥と静電気でパサつく硬い髪をしなやかで柔らかくまとまりのある美髪へ導くアウトバストリートメント)"
            },
            {
                "rank": 2,
                "queries": ["ヴェーダヴィ モーリスメセゲ ベジタブルオイル バオバブ", "モーリスメセゲ バオバブ", "バオバブオイル 美容オイル"],
                "brand": "Maurice Messegue (モーリスメセゲ / ヴェーダヴィ)",
                "name": "ベジタブルオイル バオバブ 50ml (フランス植物療法の権威・過酷な乾燥を生き抜く生命の木から抽出した高純度オイルが冬の硬化角層をふっくらほぐす極上美容オイル)"
            },
            {
                "rank": 3,
                "queries": ["バオバブオイル 未精製", "マンディムーン バオバブ", "バオバブオイル 50ml"],
                "brand": "mandy moon (マンディムーン)",
                "name": "オーガニック未精製バオバブオイル 50ml (ゴールドに輝く低温圧搾油・オレイン酸とリノール酸が絶妙なバランスで乾燥肌のバリア機能を強固にサポートするフェイスオイル)"
            },
            {
                "rank": 4,
                "queries": ["メルヴィータ タッチオイル", "メルヴィータ ビオオイル", "Melvita バオバブ"],
                "brand": "Melvita (メルヴィータ)",
                "name": "ビオオイル タッチオイル 10ml (ロールオンタイプでいつでも集中保湿・目元や口元など真冬の乾燥小ジワが気になる部分をピンポイントでケアする携帯オーガニックオイル)"
            },
            {
                "rank": 5,
                "queries": ["コディナ バオバブオイル", "CODINA バオバブ", "バオバブオイル 100ml"],
                "brand": "CODINA (コディナ)",
                "name": "バオバブオイル 30ml/100ml (フランス・ブルゴーニュ発オーガニックコスメ・高い抗酸化力と肌再生力で冬の乾燥くすみやゴワつきを解きほぐすプレミアムオイル)"
            },
            {
                "rank": 6,
                "queries": ["バオバブオイル キャリアオイル", "自然化粧品研究所 バオバブオイル", "バオバブオイル オーガニック 未精製"],
                "brand": "自然化粧品研究所 / Botanicals",
                "name": "オーガニック未精製 バオバブオイル 15ml/50ml (無添加コールドプレス・化粧水前のブースターや手作りコスメのベースとしても冬の角質層をみずみずしく満たすピュアオイル)"
            },
            {
                "rank": 7,
                "queries": ["スパヒノキ バオバブオイル", "スパヒノキ バオバブ", "オーガニック バオバブオイル 50ml"],
                "brand": "spahinoki (スパヒノキ)",
                "name": "オーガニック バオバブオイル 50ml (エコサートコスモス認証・ビタミンE豊富な濃密オイルが真冬の冷風から素肌を守り抜きもっちり吸い付くような弾力肌へ整える名品)"
            },
            {
                "rank": 8,
                "queries": ["ナプラ N. シアオイル", "エヌドット シアオイル", "ナプラ シアオイル 150ml"],
                "brand": "napla (ナプラ)",
                "name": "N. シアオイル 150ml (バオバブオイル×3種の超高圧処理植物オイル・さらりとしたテクスチャーで真冬の髪の内部まで濃密な潤いを届け乾燥パサつきを根本から補修)"
            },
            {
                "rank": 9,
                "queries": ["soel LIVING-OIL 美容オイル", "バオバブ 美容オイル", "バオバブ フェイスオイル"],
                "brand": "soel (ソエル)",
                "name": "LIVING-OIL スキンケア美容オイル 60ml (バオバブオイル高配合の生オイル・真冬の過酷な暖房環境下でも乾燥を許さず一日中みずみずしいバリア膜をキープする高保湿生セラム)"
            },
            {
                "rank": 10,
                "queries": ["Aura Cacia スキンケア オイル", "バオバブ バーム", "バオバブ リッチバーム"],
                "brand": "Aura Cacia (オーラカシア)",
                "name": "オーガニック ナリシング スキンケアオイル 30ml (高純度バオバブ種子油ブレンド・冬のかかと・ひじ・指先のガサガサ角質を柔らかくなめらかに整える万能ナリシングオイル)"
            }
        ]
    },
    "winter_kombucha": {
        "title": "保湿力の強さで肌乾燥とさようなら！発酵紅茶の力で冬の血行不良くすみ＆角層枯れを一掃する高保湿コンブチャコスメランク10",
        "file": "winter-kombucha.html",
        "items": [
            {
                "rank": 1,
                "queries": ["LAVIEN コンブバイオーム トナー", "コンブバイオーム ディープハイドレーションフェイシャルトナー", "LAVIEN トナー"],
                "brand": "LAVIEN (ラヴィアン)",
                "name": "コンブバイオーム ディープハイドレーション フェイシャルトナー 150ml (発酵紅茶コンブチャ×マイクロバイオーム・真冬のこわばった角層を素早くほぐし水分を満たしてキメ細やかな発光肌へ導く高保湿化粧水)"
            },
            {
                "rank": 2,
                "queries": ["LAVIEN コンブバイオーム アンプル", "コンブバイオーム ディープハイドラカーミングアンプル", "LAVIEN アンプル"],
                "brand": "LAVIEN (ラヴィアン)",
                "name": "コンブバイオーム ディープハイドラ カーミングアンプル 50ml (発酵紅茶エキス濃縮アンプル・真冬の寒暖差やエアコン乾燥で乱れた肌バリアを集中補修し澄んだ輝きを放つ水光肌へ導く高濃度セラム)"
            },
            {
                "rank": 3,
                "queries": ["elishacoy コンブチャ ミスト", "エリシャコイ コンブチャ", "コンブチャ ギョルバイオームミスト"],
                "brand": "elishacoy (エリシャコイ)",
                "name": "コンブチャ ギョルバイオームミスト 100ml (506時間熟成発酵紅茶エキス・乾燥を感じた瞬間にメイクの上から微細な水分ベールを吹きかけ一日中うるおいツヤを死守するミスト美容液)"
            },
            {
                "rank": 4,
                "queries": ["フレッシュ ブラックティー セット", "fresh ブラックティー コンブチャ", "コンブチャ ブラックティー エッセンス"],
                "brand": "Fresh (フレッシュ)",
                "name": "ブラックティー コンブチャ フェイシャルトリートメント エッセンス 150ml (NY発祥ラグジュアリースキンケア・超微細な抗酸化シールドで真冬の冷気・汚染物質・乾燥ダメージから肌を守る最高峰エッセンス)"
            },
            {
                "rank": 5,
                "queries": ["アンダルーナチュラルズ コンブチャ", "シトラスコンブチャ クレンジングジェル", "コンブチャ クレンジング"],
                "brand": "ANDALOU NATURALS (アンダルーナチュラルズ)",
                "name": "クリアスキン シトラスコンブチャ クレンジングジェル 178ml (発酵紅茶エキス×フルーツ幹細胞・真冬の不要な古い角質やメイク汚れをマイルドに吸着オフしつっぱらない透明美肌へ)"
            },
            {
                "rank": 6,
                "queries": ["コンブチャヴィーガンコラーゲンクリーム", "ハーブルーム コンブチャ", "コンブチャ クリーム"],
                "brand": "HERBLOOM (ハーブルーム)",
                "name": "コンブチャ ヴィーガン コラーゲンクリーム 50ml (高濃度発酵紅茶×植物性ヴィーガンコラーゲン・真冬の乾燥でしぼんだ肌にぷるんとした弾力と濃密なうるおいラップをかける高保湿クリーム)"
            },
            {
                "rank": 7,
                "queries": ["ティーブレス コンブチャ", "パフューム ヘア&ボディミスト コンブチャ", "TEA BLESS コンブチャ"],
                "brand": "TEA BLESS (ティーブレス)",
                "name": "パフューム ヘア＆ボディミスト 清柑柚子コンブチャ 100ml (発酵紅茶エキス×柚子セラミド・冬の乾燥したボディやパサつく髪に心地よい香りとみずみずしい潤いを同時に届けるマルチミスト)"
            },
            {
                "rank": 8,
                "queries": ["ハーバニエンス シャンプー", "ハーバニエンス スカルプ", "コンブチャ シャンプー"],
                "brand": "HERBANIENCE (ハーバニエンス)",
                "name": "オーガニック スカルプシャンプー 300ml (発酵紅茶エキスとオーガニックハーブティー水・真冬の頭皮乾燥によるフケやかゆみを防ぎ根元からふんわり立ち上がる潤い美髪を育むスカルプケア)"
            },
            {
                "rank": 9,
                "queries": ["Earth Kiss コンブチャ マスク", "コンブチャ シートマスク", "コンブチャ フェイスマスク"],
                "brand": "Earth Kiss (アースキス)",
                "name": "オーガニック 発酵コンブチャ クレイシートマスク (発酵紅茶エキスと死海クレイミネラル・真冬の暖房下で干からびてくすんだ肌に15分間の集中ミネラル保湿を与える濃密マスク)"
            },
            {
                "rank": 10,
                "queries": ["コンブチャセラム ペプチド", "コンブチャ セラム", "コンブチャ 美容液"],
                "brand": "K-Glow Lab (コンブチャバイオーム)",
                "name": "コンブチャ ペプチド グロウセラム 30ml (紅茶発酵液×マルチペプチド・真冬の血行不良によるどんより肌を明るく照らしキメ密度の高い水光ツヤ肌を一日中維持する高保湿美容液)"
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

    with open("fetched_final_30_tamanu_baobab_kombucha.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n==========================================")
    print(f"Finished! Successfully fetched: {total_success} / {total_needed}")
    print(f"Saved to fetched_final_30_tamanu_baobab_kombucha.json")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
