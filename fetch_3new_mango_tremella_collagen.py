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
    "winter_mango_butter": {
        "title": "保湿力の強さで肌乾燥とさようなら！体温でとろける高純度ステアリン酸が真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿マンゴーバターコスメランク10",
        "file": "winter-mango-butter.html",
        "items": [
            {
                "rank": 1,
                "query": "&SH マンゴーバター 100g",
                "brand": "&SH (アンドエスエイチ)",
                "name": "&SH 100%ピュア マンゴーバター 100g (体温35℃でスーッととろける未精製グレード・シアバターより軽やかな浸透感で真冬のカチコチかかとやひび割れ手肌を濃密ラッピングする植物性濃密エモリエントバター)"
            },
            {
                "rank": 2,
                "query": "ザボディショップ ボディバター マンゴー 200ml",
                "brand": "THE BODY SHOP (ザ・ボディショップ)",
                "name": "ボディバター マンゴー 200ml (マンゴー種子油×シアバター×ココアバター配合・95%自然由来成分・乾燥して粉を吹く冬の全身に吸い付くように馴染み、フレッシュな甘い果実の香りと共に48時間濃密な潤いを保ち続ける名作)"
            },
            {
                "rank": 3,
                "query": "&SH マンゴーバター 50g",
                "brand": "&SH (アンドエスエイチ)",
                "name": "&SH 高純度マンゴーバター 50g (携帯に便利なアルミ缶容器・外出先で乾燥する指先のささくれやリップケア、真冬の粉吹き頬にサッと体温で溶かして馴染ませるマルチポータブルバター)"
            },
            {
                "rank": 4,
                "query": "ナプラ N. スタイリングセラム 94g",
                "brand": "napla (ナプラ / N.)",
                "name": "N. (エヌドット) スタイリングセラム 94g (シアバター×マンゴー種子脂配合・こっくりとした乳液状テクスチャーが冬の暖房や静電気でパサつく髪の毛先まで潤いを届け、しっとりウェットな束感とツヤを一日中キープ)"
            },
            {
                "rank": 5,
                "query": "ロレッタ ナイトケアクリーム 120g",
                "brand": "Loretta (ロレッタ / モルトベーネ)",
                "name": "ロレッタ ナイトケアクリーム 120g (マンゴー種子脂×アルガンオイル配合・寝る前の洗い流さないヘアトリートメント・夜つければ真冬の乾燥による翌朝の寝癖やうねりを抑え、しっとりまとまる素直な髪へ導くアウトバスクリーム)"
            },
            {
                "rank": 6,
                "query": "山桂産業 マンゴーバター",
                "brand": "山桂産業",
                "name": "山桂産業 精製マンゴーバター 100g 容器入り (化粧品原料グレード・高純度脱臭精製・ステアリン酸とオレイン酸のバランスに優れ、冬の手作りハンドクリームや濃密ボディバームの主原料として絶大な信頼を誇る)"
            },
            {
                "rank": 7,
                "query": "ロレッタ メイクアップミルク",
                "brand": "Loretta (ロレッタ / モルトベーネ)",
                "name": "ロレッタ メイクアップミルク (ナチュラル) 100ml (マンゴーバター×ダマスクローズオイル配合・冬の乾いた髪に軽やかなツヤと柔らかい毛流れをプラスするミルクタイプスタイリング・静電気による髪の広がりを優しく防止)"
            },
            {
                "rank": 8,
                "query": "ラニカイ バス＆ボディ ボディローション マンゴーココナッツ 250ml",
                "brand": "Lanikai Bath and Body (ラニカイ)",
                "name": "ラニカイ バス＆ボディ ボディローション マンゴーココナッツ 250ml (天然マンゴーバター×ホホバオイル×アロエエキス配合・ハワイ生まれの濃厚モイスチャーローション・真冬の入浴後の全身をしっとりベルベット肌に整える)"
            },
            {
                "rank": 9,
                "query": "ラニカイ バス＆ボディ ボディ＆ヘアオイル マンゴーココナッツ 130ml",
                "brand": "Lanikai Bath and Body (ラニカイ)",
                "name": "ラニカイ バス＆ボディ ボディ＆ヘアオイル マンゴーココナッツ 130ml (マンゴー種子油×ククイナッツ油配合・冬の乾燥したボディとパサつく髪へ一本で深いうるおいと自然なツヤを与えるリッチなマルチオイル)"
            },
            {
                "rank": 10,
                "query": "サボネリー ベジタブルソープ マンゴー",
                "brand": "La Savonnerie de Bormes (サボネリー)",
                "name": "サボネリー ベジタブルソープ マンゴー 100g (マンゴーバター×植物性グリセリン配合・プロヴァンス伝統の植物石鹸・クリーミーな泡立ちで肌に必要な皮脂を残しながら真冬の素肌をしっとり洗い上げる高保湿ソープ)"
            }
        ]
    },
    "winter_tremella": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える植物性ムコ多糖類が真冬の干からびインナードライ肌を満たし続ける高保湿シロキクラゲコスメランク10",
        "file": "winter-tremella.html",
        "items": [
            {
                "rank": 1,
                "query": "ピアベルピア Qモイスト",
                "brand": "ピアベルピア (Piabelpia)",
                "name": "ピアベルピア Qモイスト 50ml (シロキクラゲ多糖体×コエンザイムQ10×ヒアルロン酸配合・自重の約500倍の保水力を誇る白キクラゲの濃密ヴェールが、冬のエアコン暖房で干からびた肌深部に吸い付くような潤いを与える高保湿美容液)"
            },
            {
                "rank": 2,
                "query": "ルルルン ハイドラ EX マスク",
                "brand": "LuLuLun (ルルルン)",
                "name": "ルルルン ハイドラ EX マスク (白キクラゲ多糖体×ヒト脂肪由来間葉系細胞エクソソーム×グルタチオン配合・真冬の角層に圧倒的な弾力と水分を満たす白玉シートマスク・毎日の集中保水でインナードライを根本からケア)"
            },
            {
                "rank": 3,
                "query": "アテニア ドレスリフト ローション",
                "brand": "Attenir (アテニア)",
                "name": "ドレスリフト ローション 150ml (医薬部外品・白キクラゲ多糖体×独自原料発酵コラーゲン×ナイアシンアミド配合・とろみのある美容液級の化粧水が真冬の乾いた角層を瞬時にほぐし、押し返すような高密度ハリ肌を叶える大人の名作)"
            },
            {
                "rank": 4,
                "query": "オルビス アクアニスト ローション",
                "brand": "ORBIS (オルビス)",
                "name": "アクアニスト ローション (RM 高保湿タイプ) 180ml (シロキクラゲ多糖体×持続型高保水アミノ酸配合・敏感肌設計・冬の乾燥でバリアが低下した角層の隙間へスッと浸透し、ベタつかずもっちりとした潤いを一日中繋ぎ止める薬用化粧水)"
            },
            {
                "rank": 5,
                "query": "コスメデコルテ イドラクラリティ 薬用 トリートメント エッセンス ウォーター",
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "イドラクラリティ 薬用 トリートメント エッセンス ウォーター 200ml (美肌糖×シロキクラゲエキス配合・医薬部外品・冬の寒暖差やホルモンバランスで乱れがちな毛穴の目立ちや乾燥くすみを防ぎ、透明感あふれるみずみずしい素肌へと導く)"
            },
            {
                "rank": 6,
                "query": "エトヴォス モイスチャライジングローション",
                "brand": "ETVOS (エトヴォス)",
                "name": "モイスチャライジングローション 150ml (シロキクラゲ多糖体×ヒアルロン酸×グルコシルセラミド配合・自らうるおいを抱え込む肌へ育てる高保湿化粧水・とろみのある優しいテクスチャーが冬の敏感な角層を穏やかに満たす)"
            },
            {
                "rank": 7,
                "query": "ファンケル 泥ジェル洗顔 120g",
                "brand": "FANCL (ファンケル)",
                "name": "泥ジェル洗顔 120g (白キクラゲ多糖体×3種のクレイ×アロエベラ葉エキス配合・泡立て不要・真冬の毛穴汚れや黒ずみを吸着しながら、シロキクラゲのうるおい保護ヴェールで洗顔後のツッパリ感を一切寄せ付けないジェル洗顔料)"
            },
            {
                "rank": 8,
                "query": "デュフラ フィトフォース オーガニック",
                "brand": "DIEUFRA (デュフラ)",
                "name": "デュフラ フィトフォース オーガニック モイストローション (シロキクラゲ多糖体×12種のオーガニック植物エキス配合・サロン専売大容量・冬の頑固な乾燥角層へ贅沢に水分を送り込み、みずみずしく柔軟な素肌へ導くプロ仕様化粧水)"
            },
            {
                "rank": 9,
                "query": "ファイテン アクアゴールド プレミアムモイスチャージェル",
                "brand": "Phiten (ファイテン)",
                "name": "ファイテン アクアゴールド プレミアムモイスチャージェル (シロキクラゲ多糖体×アクアゴールド×アクアパラジウム配合・濃密なゴールドジェルが真冬の乾燥ダメージ肌に密着浸透し、ふっくら吸い付くような潤い膜でバリア機能を補強)"
            },
            {
                "rank": 10,
                "query": "PLAMID リッチエッセンス",
                "brand": "PLAMID (プラミド)",
                "name": "PLAMID リッチエッセンス 30ml (シロキクラゲ多糖体×ウマプラセンタエキス×ウマサイタイエキス配合・原液90%超リッチ処方・自重の約500倍の保水力を誇る白キクラゲの濃縮パワーが真冬の深刻な小ジワと乾燥砂漠肌を集中救済)"
            }
        ]
    },
    "winter_collagen": {
        "title": "保湿力の強さで肌乾燥とさようなら！三重らせん生コラーゲンと高浸透ナノペプチドが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる高保湿コラーゲンコスメランク10",
        "file": "winter-collagen.html",
        "items": [
            {
                "rank": 1,
                "query": "アスタリフト ジェリー アクアリスタ 60g",
                "brand": "ASTALIFT (アスタリフト / 富士フイルム)",
                "name": "ジェリー アクアリスタ 60g (水溶性生コラーゲン×浸透型加水分解コラーゲン×Wヒト型ナノセラミド配合・洗顔直後に使う赤い先行美容液・自己復元ジェリーが冬の寒さでしぼんだ角層の土台を立て直し吸い付くハリ感を叶える)"
            },
            {
                "rank": 2,
                "query": "ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX 120g",
                "brand": "DR.CI:LABO (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 120g (浸透型コラーゲンEX×ナイアシンアミド配合・日本初の高浸透処方・真冬の乾燥でたるみがちなフェイスラインと目元・口元を濃密リフト膜で引き上げ続ける最高峰オールインワン)"
            },
            {
                "rank": 3,
                "query": "DHC スーパーコラーゲン スプリーム 100ml",
                "brand": "DHC (ディーエイチシー)",
                "name": "DHC スーパーコラーゲン スプリーム 100ml (最高濃度294倍ジペプチド-8高配合・DHC独自のナノサイズ低分子コラーゲンが肌の奥深く角層まで圧倒的スピードで浸透・冬の深刻な水分不足とハリ不足を1本で跳ね返す導入美容液)"
            },
            {
                "rank": 4,
                "query": "コラリッチEX プレミアムリフトジェル 55g",
                "brand": "cola-rich (コラリッチ / キューサイ)",
                "name": "コラリッチEX プレミアムリフトジェル 55g (8種の集中モイストコラーゲン×リフト成分配合・真冬の乾燥小ジワを目立たなくする効能評価試験済み・角層の表面から深部まで異なるサイズのコラーゲンが隙間なく潤す多機能ジェル)"
            },
            {
                "rank": 5,
                "query": "天使のララ モイスチャーゲル",
                "brand": "天使のララ (エミネット)",
                "name": "天使のララ モイスチャーゲル 100g (高純度独自ピュアコラーゲン×セラミド×月見草油配合・良質な魚鱗由来の生コラーゲンを贅沢に配合・冬の乾燥で敏感に傾いた肌をぷるぷるの保水膜で包み込み、もっちり柔らかく整える)"
            },
            {
                "rank": 6,
                "query": "ニチリ プロショット 生コラーゲン",
                "brand": "ニチリ (Nichiri)",
                "name": "ニチリ プロショット 3ml×25包 (サロン専売品・生コラーゲン×超微粒子ナノプラチナ配合・個包装使い切りタイプ・熱変性していない三重らせん生コラーゲンが冬の枯れ肌に瞬間リフト感と圧倒的な保水密封をもたらす集中補修エッセンス)"
            },
            {
                "rank": 7,
                "query": "ドモホルンリンクル クリーム20",
                "brand": "Domohorn Wrinkle (再春館製薬所)",
                "name": "クリーム20 [医薬部外品] 30g (独自ハモコラーゲン×マツダイコラーゲンペプチド×チューリップエキス配合・真冬の過酷な寒冷乾燥下でも角層奥深くまで豊かなコラーゲンを届け、力強いハリと透明感を呼び覚ます最高峰クリーム)"
            },
            {
                "rank": 8,
                "query": "チューンメーカーズ コラーゲン 20ml",
                "brand": "TUNEMAKERS (チューンメーカーズ)",
                "name": "原液 コラーゲン 20ml (海洋性加水分解コラーゲン100%原液・浸透性に優れた低分子コラーゲンが真冬の乾燥でしぼんだ目元やほうれい線まわりに直接アプローチ・手持ちの化粧水や乳液に混ぜてハリ感を即効プラス)"
            },
            {
                "rank": 9,
                "query": "水溶性コラーゲン 原液 100％ 美容液",
                "brand": "KISO / 原液美容液",
                "name": "水溶性コラーゲン原液 100% 美容液 (天然由来・三重らせん構造を保持した高分子コラーゲン液・肌表面にしなやかで弾力ある保護皮膜を形成し、真冬の外気乾燥による水分蒸散を強力に防ぎ切る純粋モイスチャーリキッド)"
            },
            {
                "rank": 10,
                "query": "EC pH5生コラーゲン",
                "brand": "EC (イーシー)",
                "name": "EC pH5生コラーゲン 美容液 60ml (弱酸性・生コラーゲン高濃度配合・肌と同じpH5に調整された生コラーゲンが角層にスッと馴染み、冬の暖房下でも乾燥知らずのぷるぷる瑞々しい肌質をキープするプロ仕様エッセンス)"
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
            q = item["query"]
            print(f"Rank {item['rank']}: Trying '{q}' ...")
            encoded_q = urllib.parse.quote(q)
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            
            chosen_item = None
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
    
    with open("fetched_3new_mango_tremella_collagen.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_mango_tremella_collagen.json!")

if __name__ == "__main__":
    fetch_all()
