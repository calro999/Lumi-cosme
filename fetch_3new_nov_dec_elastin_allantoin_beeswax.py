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
    "winter_elastin": {
        "title": "保湿力の強さで肌乾燥とさようなら！寒冷と暖房乾燥でしぼんだ肌に跳ね返すような弾力と濃密な潤いを取り戻す高保湿エラスチンコスメランク10",
        "file": "winter-elastin.html",
        "items": [
            {
                "rank": 1,
                "queries": ["KISO エラスチン", "キソ エラスチン 美容液"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "GGエッセンス EL 20ml (高純度加水分解エラスチン原液・真冬の寒冷で硬直した角層としぼみ肌に濃密な弾力と潤いを注ぎ込む集中美容液)"
            },
            {
                "rank": 2,
                "queries": ["チューンメーカーズ エラスチン", "TUNEMAKERS エラスチン"],
                "brand": "TUNEMAKERS (チューンメーカーズ)",
                "name": "エラスチン配合エッセンス 20ml (真皮の弾力ネットワークに着目・いつもの化粧水やクリームに1滴混ぜて冬の乾燥小ジワを押し返す高純度原液)"
            },
            {
                "rank": 3,
                "queries": ["オバジX ダーマアドバンスドリフト 50g", "オバジX ダーマアドバンスドリフト"],
                "brand": "Obagi (オバジ) / ロート製薬",
                "name": "オバジX ダーマアドバンスドリフト 50g (エラスプロ×コラプラス配合・真冬の寒冷で重力に負けそうなしぼみ輪郭をピンと引き上げる最高峰リフトクリーム)"
            },
            {
                "rank": 4,
                "queries": ["フラコラ エラスチン", "fracora エラスチン原液", "フラコラ 原液 美容液"],
                "brand": "fracora (フラコラ)",
                "name": "エラスチン原液 30ml (魚由来のピュア低分子エラスチン100%・角層の奥深くまですばやく浸透し冬の乾燥で失われたハリと弾力を再起動するエイジングセラム)"
            },
            {
                "rank": 5,
                "queries": ["シーラボ エンリッチリフトEX 120g", "アクアコラーゲンゲル エンリッチリフトEX", "シーラボ エンリッチリフト"],
                "brand": "Dr.Ci:Labo (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 120g (浸透型コラーゲンEX×エラスチン配合・真冬の超乾燥とたるみを1ステップで跳ね返す濃密高保湿オールインワンゲル)"
            },
            {
                "rank": 6,
                "queries": ["DHC ビューティリフト エッセンス", "DHC ビューティ リフト", "DHC エラスチン 美容液"],
                "brand": "DHC (ディーエイチシー)",
                "name": "DHCビューティリフト エッセンス 50ml (エラスチン×コラーゲン誘導ペプチド配合・真冬のエアコン乾燥で深く刻まれる乾燥サインに濃厚なハリ膜を形成するリフト美容液)"
            },
            {
                "rank": 7,
                "queries": ["ビーグレン QuSomeリフト", "bglen リフト", "ビーグレン リフト 美容液"],
                "brand": "b.glen (ビーグレン)",
                "name": "QuSomeリフト 60g (独自の浸透テクノロジーでエラスチン＆コラーゲンサポートペプチドを真皮まで届けるマッサージ美容液・冬のむくみとしぼみ顔を立体的にリフトアップ)"
            },
            {
                "rank": 8,
                "queries": ["ラプレシア エクストラエッセンス", "ラ・プレシア エッセンス", "エラスチン 美容液 原液"],
                "brand": "UTP (ラ・プレシア)",
                "name": "エクストラエッセンス 50ml (北海道産プラセンタエキス×加水分解エラスチン配合・エステサロン専用の本格エイジングケア処方で真冬の深刻なハリ枯れを救う濃密セラム)"
            },
            {
                "rank": 9,
                "queries": ["太陽のアロエ社 原液", "エラスチン 原液 美容液 10ml", "エラスチン 原液"],
                "brand": "太陽のアロエ社 / 自然化粧品研究所",
                "name": "加水分解エラスチン原液 10ml (水溶性天然マリンエラスチン・冬の洗顔後すぐの素肌や愛用化粧水に数滴プラスするだけでモチモチの弾力肌へ整えるマルチ原液)"
            },
            {
                "rank": 10,
                "queries": ["メディピール ペプチド9 ボリュームエッセンス", "MEDIPEEL ボリュームエッセンス"],
                "brand": "MEDIPEEL (メディピール)",
                "name": "ペプチド9 ボリュームエッセンス プロ 100ml (9種のペプチド×加水分解エラスチン×ボルフィリン・微細な酸素バブルが弾けて真冬の乾燥しぼみ肌をふっくら満たす話題の泡美容液)"
            }
        ]
    },
    "winter_allantoin": {
        "title": "保湿力の強さで肌乾燥とさようなら！冷風と暖房寒暖差で荒れ狂う角層を鎮静＆保水バリアで満たす高保湿アラントインコスメランク10",
        "file": "winter-allantoin.html",
        "items": [
            {
                "rank": 1,
                "queries": ["キュレル 潤浸保湿 フェイスクリーム 40g", "キュレル フェイスクリーム 40g"],
                "brand": "Curel (キュレル) / 花王",
                "name": "潤浸保湿 フェイスクリーム 40g (医薬部外品・消炎有効成分アラントイン×潤浸セラミド機能成分配合・真冬の冷風で赤くピリつく超乾燥敏感肌をふんわり包み込む国民的名品)"
            },
            {
                "rank": 2,
                "queries": ["ミノン モイストチャージ ローション II", "ミノン アミノモイスト ローション II"],
                "brand": "MINON (ミノン) アミノモイスト",
                "name": "モイストチャージ ローション II もっとしっとりタイプ 150ml (医薬部外品・アラントイン（グリチルリチン酸2K）×9種のアミノ酸配合・冬のとろみ角層深層保水化粧水)"
            },
            {
                "rank": 3,
                "queries": ["イハダ 薬用バーム 20g", "IHADA 薬用バーム"],
                "brand": "IHADA (イハダ) / 資生堂",
                "name": "薬用バーム 20g (医薬部外品・抗肌あれ有効成分アラントイン×高精製ワセリン配合・人肌でとろけてピタッと密着し真冬の寒冷刺激とマスク擦れを完全シールドする密着保護バーム)"
            },
            {
                "rank": 4,
                "queries": ["アベンヌ シカルファットプラス リペアクリーム 40g", "シカルファットプラス リペアクリーム"],
                "brand": "Avene (アベンヌ)",
                "name": "シカルファットプラス リペアクリーム 40g (整肌成分アラントイン類似C+Restore×アベンヌ温泉水配合・真冬のひび割れ・粉吹き・極度な乾燥肌を速攻立て直すヨーロッパ伝統の保護クリーム)"
            },
            {
                "rank": 5,
                "queries": ["カルテHD モイスチュア エマルジョン 120ml", "カルテHD モイスチュア エマルジョン"],
                "brand": "Carte (カルテHD) / コーセー マルホ",
                "name": "モイスチュア エマルジョン 120ml (医薬部外品・保水有効成分ヘパリン類似物質×肌荒れ防止有効成分アラントイン（グリチルリチン酸）配合・角層ラメラを整え冬の乾燥連鎖を断つ高保湿乳液)"
            },
            {
                "rank": 6,
                "queries": ["ユースキン シソラ ローション 170ml", "シソラ ローション ポンプ"],
                "brand": "yuskin (ユースキン) シソラ",
                "name": "シソラ ローション 170ml ポンプ (医薬部外品・アラントイン×紫蘇エキス配合・真冬の冷えや入浴後の乾燥かゆみにすーっとなじんで潤いを守る敏感肌用全身ミルキィローション)"
            },
            {
                "rank": 7,
                "queries": ["dプログラム モイストケア ローション MB", "dプログラム モイストケア ローション"],
                "brand": "d program (dプログラム) / 資生堂",
                "name": "モイストケア ローション MB 125ml (医薬部外品・トラネキサム酸×グリチルリチン酸/アラントイン配合・寒暖差でカサつき粉を吹く冬のデリケート肌を深層から潤す薬用高保湿化粧水)"
            },
            {
                "rank": 8,
                "queries": ["ザーネクリーム 100g", "ザーネ クリーム エーザイ"],
                "brand": "Eisai (エーザイ) ザーネ",
                "name": "ザーネクリーム 100g (医薬部外品・天然型ビタミンE×消炎アラントイン（グリチルリチン酸二カリウム）配合・真冬のあかぎれ・手足の粉吹きをなめらかに治す薬用保湿クリーム)"
            },
            {
                "rank": 9,
                "queries": ["アトピアD 保湿フォーム 100g", "アトピアD 保湿フォーム"],
                "brand": "アトピアD (Atopia D)",
                "name": "保湿フォーム 100g (医薬部外品・ヘパリン類似物質×アラントイン配合・濃密なマイクロ泡が摩擦ゼロで肌に溶け込み真冬の極度な乾燥と炎症を同時にケアする泡状高保湿美容液)"
            },
            {
                "rank": 10,
                "queries": ["肌ラボ 薬用 極潤", "極潤 薬用 ヒアルロン", "肌ラボ 極潤 薬用"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤 薬用抗炎症・保湿化粧水 170ml (医薬部外品・アラントイン×濃密ヒアルロン酸配合・真冬の暖房乾燥で赤みやゴワつきが出やすい角層をモチモチのうるおい膜で満たす薬用ローション)"
            }
        ]
    },
    "winter_beeswax": {
        "title": "保湿力の強さで肌乾燥とさようなら！ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥を完全遮断する高保湿ミツロウコスメランク10",
        "file": "winter-beeswax.html",
        "items": [
            {
                "rank": 1,
                "queries": ["バーツビーズ ビーズワックス リップバーム", "バーツビーズ リップバーム"],
                "brand": "Burt's Bees (バーツビーズ)",
                "name": "ビーズワックス リップバーム 4.25g (天然ミツロウ100%ベース×ペパーミントオイル・真冬の過酷な寒風下でも水分を一滴も逃がさない世界的人気の高密着リップバーム)"
            },
            {
                "rank": 2,
                "queries": ["ロクシタン シアバター 150ml", "ロクシタン シアバター"],
                "brand": "L'OCCITANE (ロクシタン)",
                "name": "シアバター 150ml (天然シア脂×ミツロウブレンド・人肌でとろけて肌表面に強固な保護ヴェールを形成し真冬の全身のひび割れ・ガサガサを救護するマルチ保湿バーム)"
            },
            {
                "rank": 3,
                "queries": ["ニールズヤード ワイルドローズ ビューティバーム 50g", "ニールズヤード ビューティバーム"],
                "brand": "NEAL'S YARD REMEDIES (ニールズヤード)",
                "name": "ワイルドローズ ビューティバーム 50g (オーガニックミツロウ×野ばらシードオイル・真冬の乾燥でくすんだ肌にリッチな潤いと輝くツヤを与えて肌密度を高める最高峰バーム)"
            },
            {
                "rank": 4,
                "queries": ["Dr.ハウシュカ ローズデイクリーム 30ml", "ドクターハウシュカ ローズデイクリーム"],
                "brand": "Dr. Hauschka (ドクターハウシュカ)",
                "name": "ローズデイクリーム 30ml (貴重なオーガニックミツロウ×ダマスクローズワックス配合・真冬の厳しい寒冷風から肌を完璧にシールドするヨーロッパ貴族愛用の高貴なリッチクリーム)"
            },
            {
                "rank": 5,
                "queries": ["マルティナ カレンドラ ベビークリーム", "マルティナ ベビークリーム", "マルティナ バーム"],
                "brand": "Martina (マルティナ)",
                "name": "カレンドラベビークリーム 50ml (デメター認証オーガニックミツロウ×カレンドラオイル・水仕事を繰り返す指先や真冬の赤ちゃんの頬も優しく守り抜く100%自然由来の高保湿バーム)"
            },
            {
                "rank": 6,
                "queries": ["ソンバーユ No.7 60ml", "ソンバーユ ナンバーセブン"],
                "brand": "薬師堂 (ソンバーユ)",
                "name": "ソンバーユ No.7 60ml (高純度馬油×天然ミツロウ配合・通常の馬油より濃厚なコクと密着力で真冬の就寝中の肌乾燥と小ジワを徹底的に防ぐ最高峰保湿馬油)"
            },
            {
                "rank": 7,
                "queries": ["アムリターラ リップ", "アムリターラ モイストカメリア", "アムリターラ バーム"],
                "brand": "AMRITARA (アムリターラ)",
                "name": "モイストカメリア リップセラム (国産無農薬ミツロウ×ツバキ種子油配合・石油系原料完全フリーで真冬の皮向け唇をなめらかに修復するオーガニック高密着リップ美容液)"
            },
            {
                "rank": 8,
                "queries": ["パックスナチュロン エモリエントクリーム 35g", "パックスナチュロン エモリエントクリーム"],
                "brand": "太陽油脂 (パックスナチュロン)",
                "name": "エモリエントクリーム 35g (ハイブリッドヒマワリ油×天然ミツロウ配合・合成界面活性剤不使用で冬の乾燥敏感肌にサラッと溶け込み潤い膜を長時間キープする素肌想いクリーム)"
            },
            {
                "rank": 9,
                "queries": ["ロゴナ リップクリーム キャレンデュラ", "ロゴナ リップクリーム"],
                "brand": "LOGONA (ロゴナ)",
                "name": "リップクリーム キャレンデュラ 4.5g (オーガニックミツロウ×ホホバ種子油×カレンデュラエキス・真冬の北風による唇の荒れや乾燥亀裂をしっかり防ぐドイツ発オーガニックリップ)"
            },
            {
                "rank": 10,
                "queries": ["バジャー バーム クラシック", "Badger バーム", "バジャー スリープバーム"],
                "brand": "BADGER (バジャー)",
                "name": "クラシック オーガニックバーム 56g (USDAオーガニック認証ミツロウ×エキストラバージンオリーブ油・真冬のカサつくひじ・かかと・目元へ体温で溶かして密着させる伝統の万能バーム)"
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
                                price = cand.get("itemPrice", 0)
                                if price >= 400 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} failed: {e}")
                        time.sleep(2)
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

    out_file = "fetched_3new_nov_dec_elastin_allantoin_beeswax.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items fetched successfully.")
    print(f"Saved to: {out_file}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
