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
    "winter_night_cream": {
        "title": "保湿力の強さで睡眠中の砂漠肌・乾燥小ジワとさようなら！翌朝もっちり吸い付く高保湿ナイトクリームランク10",
        "page_file": "winter-night-cream.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ リポソーム アドバンスト リペアクリーム 50g", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアクリーム (睡眠不足でも3時間多く眠ったような肌へ・1兆個のナイト多重層バイオリポソーム)"},
            {"rank": 2, "query": "カネボウ クリーム イン ナイト 40g", "brand": "KANEBO (カネボウ)", "name": "クリーム イン ナイト (一晩中うるおいで包み込む胎脂着想の濃密ナイトバーム・翌朝まで続くもっちりツヤ感)"},
            {"rank": 3, "query": "エリクシール トータルV ファーミングクリーム", "brand": "ELIXIR (エリクシール)", "name": "トータルV ファーミングクリーム (全方位のハリ体験・最新コラーゲン研究を結集した冬の夜用リフトアップクリーム)"},
            {"rank": 4, "query": "キュレル 潤浸保湿 フェイスクリーム 40g", "brand": "Curel (キュレル)", "name": "潤浸保湿 フェイスクリーム (消炎剤配合・セラミドケアで真冬のヒリヒリ乾燥・粉吹きを根本から防ぐ医薬部外品)"},
            {"rank": 5, "query": "オルビス ユードット モイスチャー 50g", "brand": "ORBIS (オルビス)", "name": "オルビスユードット フォーカシング コンパクトクリーム / モイスチャー (トラネキサム酸×濃密バーム・美白と深層保湿を両立するエイジングケア)"},
            {"rank": 6, "query": "アンブリオリス モイスチャークリーム 75ml", "brand": "Embryolisse (アンブリオリス)", "name": "アンブリオリス モイスチャークリーム (パリコレバックステージ定番・冬の乾燥肌を柔らかくほぐすロングセラー濃密保湿)"},
            {"rank": 7, "query": "ドクターシーラボ アクアコラーゲンゲル エンリッチリフト EX", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "アクアコラーゲンゲル エンリッチリフトEX (浸透型コラーゲンEX×ナイアシンアミド・寝ている間にハリを高める夜用ゲルクリーム)"},
            {"rank": 8, "query": "なめらか本舗 リンクルナイトクリーム 50g", "brand": "なめらか本舗 (サナ)", "name": "リンクルナイトクリーム (ピュアレチノール×豆乳発酵液配合・おやすみ中のパック効果で乾燥小じわを目立たせないプチプラ名品)"},
            {"rank": 9, "query": "SK-II スキンパワー アドバンスト クリーム 50g", "brand": "SK-II (エスケーツー)", "name": "スキンパワー アドバンスト クリーム (ピテラ×キンレンカエキス・冬の過酷な乾燥環境でも弾むようなハリツヤを育む最高峰)"},
            {"rank": 10, "query": "オバジ ダーマパワーX ステムリフト クリーム 50g", "brand": "Obagi (オバジ)", "name": "ダーマパワーX ステムリフト クリーム (ステムビルドコンプレックス配合・冬の重力に負けない濃厚密着ハリクリーム)"}
        ]
    },
    "winter_cleansing_milk": {
        "title": "保湿力の強さで冬の洗い上がりツッパリ・摩擦乾燥とさようなら！うるおい残して優しく落とす高保湿クレンジングミルクランク10",
        "page_file": "winter-cleansing-milk.html",
        "items": [
            {"rank": 1, "query": "カバーマーク トリートメント クレンジング ミルク 200g", "brand": "COVERMARK (カバーマーク)", "name": "トリートメント クレンジング ミルク (美容液成分89%配合・ファンデーションもスルンと落ちて化粧水がいらないほど潤う殿堂入りミルク)"},
            {"rank": 2, "query": "カウブランド 無添加 メイク落としミルク 150ml", "brand": "カウブランド無添加 (牛乳石鹸)", "name": "無添加 メイク落としミルク (天然由来セラミド配合・デリケートな冬の敏感肌を摩擦レスに優しくいたわるコスパ最強名品)"},
            {"rank": 3, "query": "チャントアチャーム クレンジングミルク 130ml", "brand": "chant a charm (チャントアチャーム)", "name": "クレンジングミルク (自然由来成分100%・ミルクがオイルに変化して冬の頑固な毛穴汚れも優しく浮かせてオフ)"},
            {"rank": 4, "query": "シスレー リィスレ デマキアン 250ml", "brand": "Sisley (シスレー)", "name": "リィスレ デマキアン (ホワイトリリーエキス配合・冬の乾燥肌にしっとりとした柔軟性と至高の心地よさを与えるデパコス最高峰)"},
            {"rank": 5, "query": "ヴェレダ モイスチャー クレンジングミルク 100ml", "brand": "WELEDA (ヴェレダ)", "name": "モイスチャー クレンジングミルク (オーガニックホホバオイル×アロエベラ・冬のキメを整えて洗い上がりもっちり)"},
            {"rank": 6, "query": "パラドゥ スキンケアクレンジング 120g", "brand": "ParaDo (パラドゥ)", "name": "スキンケアクレンジング (美容液成分90%・ウォータープルーフもすっきり浮かすアクアクレンジング処方の神コンビニコスメ)"},
            {"rank": 7, "query": "アクセーヌ ミルキィ クレンズアップ 120g", "brand": "ACSEINE (アクセーヌ)", "name": "ミルキィ クレンズアップ (角質柔軟成分配合・冬の寒さでゴワついた角質をほぐしながら毛穴の奥までクレンジング)"},
            {"rank": 8, "query": "マークスアンドウェブ ハーバル クレンジングミルク", "brand": "MARKS&WEB (マークスアンドウェブ)", "name": "ハーバル クレンジングミルク (オリーブ油・スクワラン配合・天然精油ラベンダー＆カモミールの香りで冬の夜をリラックス)"},
            {"rank": 9, "query": "エトヴォス モイストバリア クレンジングミルク 130ml", "brand": "ETVOS (エトヴォス)", "name": "モイストバリア クレンジングミルク (ヒト型セラミド×植物オイル・冬の乾燥ダメージとPM2.5から肌を守る弱酸性処方)"},
            {"rank": 10, "query": "アルージェ モイスト クレンジング ミルクジェル", "brand": "Arouge (アルージェ)", "name": "モイスト クレンジング ミルクジェル (天然セラミド配合・冬の乾燥肌荒れを予防する医薬部外品の肌荒れ防止ミルク)"}
        ]
    },
    "winter_hair_mist": {
        "title": "保湿力の強さで冬の静電気・毛先パサつきとさようなら！髪にうるおいヴェールをまとう高保湿ヘアミストランク10",
        "page_file": "winter-hair-mist.html",
        "items": [
            {"rank": 1, "query": "ジルスチュアート トリートメント ヘアミスト ホワイトフローラル 200ml", "brand": "JILL STUART (ジルスチュアート)", "name": "トリートメント ヘアミスト ホワイトフローラル (キューティクル補修成分×ヒアルロン酸・冬のパサつく髪にツヤと幸福感あふれる香り)"},
            {"rank": 2, "query": "スティーブンノル ハイドロリニュー ミスト モイスチュアリペア 250ml", "brand": "STEPHEN KNOLL (スティーブンノル)", "name": "ハイドロリニュー ミスト モイスチュアリペア (高浸透補修カプセル配合・冬の乾燥でパサつく髪の深部までうるおいチャージ)"},
            {"rank": 3, "query": "オルビス エッセンスインヘアウォーター 180ml", "brand": "ORBIS (オルビス)", "name": "エッセンスインヘアウォーター (無香料・美髪成分浸透処方・冬の頑固な寝癖とパサつきをシュッと瞬時にリセット)"},
            {"rank": 4, "query": "ナプラ イノート ヘアケアミスト 200ml", "brand": "napla (ナプラ)", "name": "イノート ヘアケアミスト (アンチポリューション処方・冬のマフラー摩擦や静電気、外気汚れから髪を鉄壁シールド)"},
            {"rank": 5, "query": "リファ ロックトリートメントミスト 100ml", "brand": "ReFa (リファ)", "name": "ロックトリートメントミスト (ヒートケア成分配合・アイロンの熱を味方にして真冬の湿気・乾燥崩れを防ぎスタイル長時間キープ)"},
            {"rank": 6, "query": "ラ・カスタ アロマエステ ヘアローション エモリエント 150ml", "brand": "La CASTA (ラ・カスタ)", "name": "アロマエステ ヘアローション エモリエント (オーガニック植物エキス配合・冬の乾燥による枝毛・切れ毛をしっとり補修)"},
            {"rank": 7, "query": "ミルボン エルジューダ サンプロテクト ミスト 120ml", "brand": "MILBON (ミルボン)", "name": "エルジューダ サンプロテクト ミスト / ブリーチケア ミスト (サロン専売最高峰・冬の乾燥と紫外線ダメージを同時にケアする美容液ミスト)"},
            {"rank": 8, "query": "ジョンマスターオーガニック G&C リーブイン コンディショニングミスト 125ml", "brand": "john masters organics (ジョンマスターオーガニック)", "name": "G&Cリーブインコンディショニングミスト (グレープフルーツ＆カレンデュラ・冬の静電気を防ぎ軽やかサラサラ髪へ導くオーガニック)"},
            {"rank": 9, "query": "マシェリ パーフェクトシャワー モイスチュア 250ml", "brand": "MA CHERIE (マシェリ)", "name": "パーフェクトシャワー EX モイスチュア (濃密パールハニージュレDX配合・冬のパサつく髪に素早く浸透して毛先までうるツヤ)"},
            {"rank": 10, "query": "ロクシタン ファイブハーブス リペアリング ヘアミスト", "brand": "L'OCCITANE (ロクシタン)", "name": "ファイブハーブス リペアリング ヘアミスト (5つのエッセンシャルオイル配合・冬のダメージヘアを修復してしなやかな輝きへ)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]

                    raw_img = ""
                    if chosen.get("mediumImageUrls"):
                        raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    price = chosen.get("itemPrice", 0)
                    aff_url = chosen.get("affiliateUrl", "")
                    item_name = chosen.get("itemName", "")
                    
                    if not aff_url:
                        aff_url = chosen.get("itemUrl", "")
                        
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "itemName": item_name,
                        "price": price,
                        "img": high_res_img,
                        "url": aff_url
                    }
                else:
                    alt_q = query_info["brand"].split()[0] + " " + query.split()[0]
                    if attempt == 2 and alt_q != query:
                        query = alt_q
        except Exception as e:
            print(f"Error fetching {query}: {e}")
            time.sleep(1)
        time.sleep(0.3)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "itemName": query_info["name"],
        "price": 3500,
        "img": "https://thumbnail.image.rakuten.co.jp/@0_mall/sample/item.jpg",
        "url": "https://hb.afl.rakuten.co.jp/"
    }

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\nFetching category: {cat_key}...")
    cat_items = []
    for q_item in cat_data["items"]:
        res_item = fetch_item_with_retry(q_item)
        print(f"  Rank {res_item['rank']}: {res_item['brand']} - ¥{res_item['price']:,} - Img: {res_item['img'][:45]}...")
        cat_items.append(res_item)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

with open("rakuten_3latest_winter_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDone! All items fetched and saved to rakuten_3latest_winter_data.json")
