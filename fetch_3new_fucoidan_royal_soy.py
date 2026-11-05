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
    "winter_fucoidan": {
        "title": "保湿力の強さで肌乾燥とさようなら！海の自己治癒多糖体ヴェールが真冬のエアコン暖房による砂漠化インナードライを潤し尽くす高保湿フコイダンコスメランク10",
        "file": "winter-fucoidan.html",
        "items": [
            {
                "rank": 1,
                "queries": ["フコイダン 美容液 原液", "フコイダン 保湿 美容液", "モズク フコイダン 美容液"],
                "brand": "Limveil (リムヴェール)",
                "name": "高濃度フコイダン美容液 50ml (オキナワモズク由来高分子フコイダン高濃度配合・海の自己治癒多糖体ヴェールが真冬のエアコン暖房下でも角層水分を密着ホールドする高純度モイスチャー美容液)"
            },
            {
                "rank": 2,
                "queries": ["タカミ エッセンス", "タカミ エッセンスCE", "タカミ 美容液"],
                "brand": "TAKAMI (タカミ)",
                "name": "タカミエッセンスCE 30mL (ビタミンC・E×褐藻エキス/フコイダン高配合・毛穴・キメ・乾燥くすみを多角的にケアし、冬の冷気で硬化した角層をしっとりほぐす機能性美容液)"
            },
            {
                "rank": 3,
                "queries": ["フコイダン 保湿ローション", "フコイダン 化粧水", "アトピーラボ フコイダン"],
                "brand": "AtopiLabo (アトピーラボ)",
                "name": "フコイダン保湿ローション 200ml (天然高分子フコイダン高配合・超乾燥肌や敏感肌のために開発された低刺激高保水化粧水・真冬の粉吹き肌や暖房による突っ張りを優しく鎮静)"
            },
            {
                "rank": 4,
                "queries": ["ガゴメ昆布 フコイダン", "ガゴメ昆布 美容液", "ガゴメ昆布 エキス"],
                "brand": "自然化粧品研究所",
                "name": "ガゴメ昆布エキス 30ml (北海道産ガゴメ昆布由来の高粘性フコイダン原液・自重の数十倍の水分を抱え込む濃密バイオ皮膜が冬の外気乾燥から素肌を守り抜くプロ用原液)"
            },
            {
                "rank": 5,
                "queries": ["フコイダン 化粧水 保湿", "海藻 化粧水 高保湿", "モズク 化粧水"],
                "brand": "myufull (ミューフル)",
                "name": "PNローション 300ml (海藻フコイダン×天然植物エキス配合・全成分天然由来のノンオイル高保湿ローション・肌本来の自己回復力を引き出し冬の乾燥角層をみずみずしく満たす)"
            },
            {
                "rank": 6,
                "queries": ["フコイダン クリーム", "フコイダン モイスチャークリーム", "海藻 クリーム 保湿"],
                "brand": "MarUmi (マルミ)",
                "name": "セカンドスキンヴェール 60g (高純度フコイダン×スクワラン配合・第二の皮膚のように角層を覆う高機能保湿クリーム・真冬の冷たいすきま風と水分蒸散をブロック)"
            },
            {
                "rank": 7,
                "queries": ["フコイダン オールインワン", "フコイダン ジェル", "海藻 オールインワン"],
                "brand": "HLH",
                "name": "f ミラクルセラム 30mL (オキナワモズク由来フコイダン配合オールインワン美容液・多糖体の粘弾性皮膜が忙しい冬の朝晩も一日中うるおいを逃さない多機能モイスチャー)"
            },
            {
                "rank": 8,
                "queries": ["フコイダン スカルプ", "海藻 スカルプローション", "スカルプ エッセンス 保湿 頭皮"],
                "brand": "スカルプフコイダン",
                "name": "フコイダン スカルプエッセンス 150ml (高分子フコイダン配合・冬の暖房や静電気で乾燥・フケ・かゆみを起こしやすい頭皮の角層バリアを整える頭皮用高保湿美容液)"
            },
            {
                "rank": 9,
                "queries": ["ピューキアトリートメントソープ", "フコイダン 石鹸", "海藻 石鹸 洗顔"],
                "brand": "PUKIA (ピューキア)",
                "name": "トリートメントソープ 枠練り洗顔石鹸 100g (高純度フコイダン×海泥配合・濃密なもっちり泡が冬のデリケートな素肌を摩擦レスに包み込み、潤いを奪わずにしっとり洗い上げる無添加枠練り石鹸)"
            },
            {
                "rank": 10,
                "queries": ["フコイダン フェイスマスク", "フコイダン パック シート", "海藻 シートマスク 高保湿"],
                "brand": "マリンモイスト",
                "name": "フコイダン高保湿バイオセルロースマスク (モズクフコイダンエッセンスを贅沢に凝縮・高密着シートが真冬の干からびた肌に吸い付き、角層深部まで集中水分チャージ)"
            }
        ]
    },
    "winter_royal_jelly": {
        "title": "保湿力の強さで肌乾燥とさようなら！女王蜂だけの特有成分デセン酸と濃密アミノ酸が真冬の冷気で硬化したエイジング砂漠肌をしっとり満たす高保湿ローヤルゼリーコスメランク10",
        "file": "winter-royal-jelly.html",
        "items": [
            {
                "rank": 1,
                "queries": ["山田養蜂場 RJ 地肌ケア", "山田養蜂場 RJ", "山田養蜂場 美容液"],
                "brand": "山田養蜂場 (YAMADA BEE FARM)",
                "name": "RJ地肌ケア＆スキンケア エッセンス (生ローヤルゼリーエキスを極限まで濃縮・デセン酸と40種以上のアミノ酸が真冬の冷気で萎縮した角層を深部からふっくら再生させる薬用高保湿エッセンス)"
            },
            {
                "rank": 2,
                "queries": ["素肌しずく ゲル Sa", "素肌しずく オールインワン", "素肌しずく 化粧水"],
                "brand": "素肌しずく (アサヒグループ食品)",
                "name": "素肌しずく ゲル Sa 200g (高純度ローヤルゼリーエキス×プラセンタ×浸透型ヒアルロン酸配合・濃密ゲルが角層深部でパシャッと弾け、真冬の乾燥砂漠肌を即座に満たす高機能オールインワン)"
            },
            {
                "rank": 3,
                "queries": ["グレイスワン 濃潤リペアジェル", "グレイスワン オールインワン", "グレイスワン リペアジェル"],
                "brand": "GRACE ONE (グレイスワン / コーセーコスメポート)",
                "name": "濃潤リペアジェル 100g (発酵ローヤルゼリーエキス×3種のコラーゲン×スクワラン配合・復元ジェルが真冬の乾燥小ジワをピーンと持ち上げてうるおいを長時間密封する多機能オールインワン)"
            },
            {
                "rank": 4,
                "queries": ["チューンメーカーズ ローヤルゼリーエキス", "チューンメーカーズ ローヤルゼリー", "ローヤルゼリー 原液"],
                "brand": "TUNEMAKERS (チューンメーカーズ)",
                "name": "ローヤルゼリーエキス原液 20ml (天然ビタミン・ミネラル・良質タンパク質を凝縮・真冬の寒冷で活力を失った肌にダイレクトに滋養を与え、化粧ノリとしなやかさを取り戻す集中原液)"
            },
            {
                "rank": 5,
                "queries": ["プリオール うるおい美リフトゲル", "資生堂 プリオール 美リフトゲル", "プリオール ゲル"],
                "brand": "PRIOR (プリオール / 資生堂)",
                "name": "うるおい美リフトゲル 120ml (発酵ローヤルゼリーGL×濃密コラーゲン配合・大人の乾燥肌にしっとり馴染み、真冬の暖房下でも夕方までハリとツヤが続く高保湿リフトゲル)"
            },
            {
                "rank": 6,
                "queries": ["蜂乳 クリーム石鹸 特選", "蜂乳 クリーム石鹸", "蜂乳 洗顔"],
                "brand": "蜂乳 (ホウニュウ)",
                "name": "特選 蜂乳クリーム石鹸 200mL (大正時代から愛される伝統の生ローヤルゼリー配合液体洗顔料・ハチミツと王乳の天然保湿膜で冬の洗顔後も一切突っ張らずしっとり滑らかな肌へ)"
            },
            {
                "rank": 7,
                "queries": ["山田養蜂場 RJエクセレント", "山田養蜂場 エクセレント クリーム", "山田養蜂場 クリーム"],
                "brand": "山田養蜂場 (YAMADA BEE FARM)",
                "name": "RJエクセレント 薬用クリーム (厳選された熟成ローヤルゼリーエキスを高濃度配合・リッチで濃厚なバターテクスチャーが冬の強烈な乾燥風から肌バリアを鉄壁ガード)"
            },
            {
                "rank": 8,
                "queries": ["ローヤルゼリー トリートメント", "ハチミツ トリートメント 保湿", "ハニー ヘアマスク トリートメント"],
                "brand": "Honeyce (ハニーチェ)",
                "name": "生ローヤルゼリー＆ハニー 集中補修ヘアトリートメント (生ローヤルゼリー×オーガニックハチミツ配合・冬の静電気や乾燥でバサつく毛髪のダメージホールを密着補修し毛先までまとまるツヤ髪へ)"
            },
            {
                "rank": 9,
                "queries": ["カントリー&ストリーム ハニーフルリップ", "カントリー ストリーム リップ", "ハニーフルリップ"],
                "brand": "Country & Stream (カントリー&ストリーム)",
                "name": "ハニーフルリップ 10g (ローヤルゼリーエキス×ハチミツ×シアバター配合・唇に濃密な厚膜ヴェールを形成し、真冬のひび割れ・皮むけ・ガサガサ唇をぷるぷるに蘇らせる高保湿リップ美容液)"
            },
            {
                "rank": 10,
                "queries": ["ネイチャーリパブリック ジンセン ロイヤルシルク", "ジンセン ロイヤルシルク クリーム", "ロイヤルシルク ウォータリークリーム"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "ジンセン ロイヤルシルク ウォータリークリーム 60g (純度99%純金×生ローヤルゼリー×高麗紅参×黄金シルク配合・極上の栄養感で真冬の寒冷酸化と乾燥萎縮を跳ね返すプレミアムクリーム)"
            }
        ]
    },
    "winter_soy_isoflavone": {
        "title": "保湿力の強さで肌乾燥とさようなら！植物エストロゲンと濃密大豆発酵液が真冬の水分蒸散としぼみ肌をふっくらモチモチに再生する高保湿豆乳イソフラボンコスメランク10",
        "file": "winter-soy-isoflavone.html",
        "items": [
            {
                "rank": 1,
                "queries": ["なめらか本舗 リンクルアイクリーム", "なめらか本舗 アイクリーム", "豆乳イソフラボン アイクリーム"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "リンクルアイクリーム N 20g (高純度豆乳イソフラボン×ピュアレチノール×ビタミンE誘導体配合・真冬の暖房下で乾きやすい目元のちりめんジワをふっくら持ち上げる大人気密着アイクリーム)"
            },
            {
                "rank": 2,
                "queries": ["なめらか本舗 リンクルナイトクリーム", "なめらか本舗 ナイトクリーム", "豆乳イソフラボン ナイトクリーム"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "リンクルナイトクリーム 50g (滋賀県産大豆たまほまれ使用の豆乳発酵液×ピュアレチノール配合・おやすみ中のパック効果で真冬の朝も吸い付くようなモチ肌を実感できる濃厚高保湿ナイトクリーム)"
            },
            {
                "rank": 3,
                "queries": ["なめらか本舗 とろんと濃ジェル エンリッチ", "なめらか本舗 とろんと濃ジェル", "なめらか本舗 オールインワン"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "とろんと濃ジェル エンリッチ 高保湿タイプ 100g (1個で6役・高濃度豆乳イソフラボン含有の濃厚形状記憶ジェルが真冬の乾燥でしぼんだ角層の隙間を満たし、もっちり弾力を維持するオールインワン)"
            },
            {
                "rank": 4,
                "queries": ["豆乳よーぐるとぱっく 玉の輿", "豆腐の盛田屋 パック", "玉の輿 パック"],
                "brand": "豆腐の盛田屋",
                "name": "豆乳よーぐるとぱっく 玉の輿 150g (濃厚豆乳発酵液×ヨーグルトエキス×ローヤルゼリー配合・お風呂で塗って流すだけで真冬のごわつく角質を優しくほぐし、生まれたてのようなモチモチ白肌へ導くパック)"
            },
            {
                "rank": 5,
                "queries": ["なめらか本舗 ミスト化粧水", "マイクロミスト化粧水 なめらか本舗", "なめらか本舗 ミスト"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "マイクロミスト化粧水 NC 150g (豆乳イソフラボン微粒子ミスト・毛穴より細かい超微細マイクロミストがメイクの上からでも角層深くまで浸透し、真冬の日中暖房による乾燥砂漠肌を瞬時にリフレッシュ)"
            },
            {
                "rank": 6,
                "queries": ["なめらか本舗 美容液", "豆乳イソフラボン 美容液", "ダイズ 美容液 保湿"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "薬用リンクル美容液 ホワイト 30ml (高純度豆乳イソフラボン×持続型ビタミンC×ナイアシンアミド配合・真冬の乾燥くすみと乾燥小ジワを同時に晴れやかに整える濃密美容液)"
            },
            {
                "rank": 7,
                "queries": ["なめらか本舗 クレンジング洗顔 NC", "なめらか本舗 クレンジング洗顔", "なめらか本舗 洗顔"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "クレンジング洗顔 NC 150g (高純度豆乳イソフラボン×豆乳発酵液配合・濃密で弾力のあるキメ細かい泡が真冬の乾いた肌を擦らずに汚れを落とし、洗い上がりもしっとり吸い付く素肌を保つ洗顔フォーム)"
            },
            {
                "rank": 8,
                "queries": ["豆乳 乳液 なめらか本舗", "なめらか本舗 乳液", "豆乳イソフラボン 乳液"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "乳液 NC 150ml (滋賀県産大豆たまほまれ由来の高純度豆乳イソフラボン配合・さらりとなめらかなエマルジョンが角層の水分油分バランスを黄金比に整え、乾燥知らずの素肌を保つ高保湿乳液)"
            },
            {
                "rank": 9,
                "queries": ["四季折々 豆乳 ボディミルク", "豆乳 ボディミルク", "熊野油脂 豆乳 ボディ"],
                "brand": "四季折々 / 熊野油脂",
                "name": "豆乳イソフラボン 保湿ボディミルク 500ml (高純度豆乳発酵液配合・大容量ポンプ式・冬の入浴後に全身へ素早く浸透し、タイツのこすれやすねの粉吹き乾燥を一日中しっとり防ぐ全身用高保湿ミルク)"
            },
            {
                "rank": 10,
                "queries": ["なめらか本舗 しっとり化粧水 NC", "なめらか本舗 しっとり化粧水", "なめらか本舗 化粧水"],
                "brand": "なめらか本舗 (常盤薬品工業)",
                "name": "しっとり化粧水 NC 200ml (高純度豆乳イソフラボン×ヒト型セラミド配合・角層への浸透性を極限まで高めたとろみローションで、冬の暖房直撃下でも一日中乾かない濃密うるおい肌を土台から構築)"
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
                    time.sleep(2.2) # レートリミット回避
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
                    print(f"    HTTP Error {e.code}: {e.reason}")
                    time.sleep(3.0)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(2.5)
            
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
    
    with open("fetched_3new_fucoidan_royal_soy_fixed.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_fucoidan_royal_soy_fixed.json!")

if __name__ == "__main__":
    fetch_all()
