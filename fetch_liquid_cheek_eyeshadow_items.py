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
    "winter_liquid_foundation": {
        "title": "保湿力の強さで肌乾燥・粉吹きとさようなら！美容液級のうるおいで一日中ひび割れ・毛穴落ちを防ぐ高保湿リキッドファンデーションランク10",
        "page_file": "winter-liquid-foundation.html",
        "items": [
            {"rank": 1, "query": "資生堂 エッセンス スキングロウ ファンデーション", "brand": "SHISEIDO (資生堂)", "name": "エッセンス スキングロウ ファンデーション (ナイアシンアミド×ケフィア発酵エキス・美容液を纏う至高のうるツヤ肌)"},
            {"rank": 2, "query": "コスメデコルテ ゼン ウェア グロウ", "brand": "DECORTÉ (コスメデコルテ)", "name": "ゼン ウェア グロウ (うるおい成分高配合・24時間みずみずしく上品な光沢をキープする薄膜密着ファンデ)"},
            {"rank": 3, "query": "ディオールスキン フォーエヴァー フルイド グロウ", "brand": "DIOR (クリスチャン・ディオール)", "name": "ディオールスキン フォーエヴァー フルイド グロウ (86%スキンケアベース・内側からあふれ出る極上グロウ)"},
            {"rank": 4, "query": "カネボウ コンフォートスキン ウェア", "brand": "KANEBO (カネボウ)", "name": "コンフォートスキン ウェア (スキンリフレクトカラー×保湿バリア・素肌そのものが美しいと錯覚させる心地よさ)"},
            {"rank": 5, "query": "SUQQU ザ リクイド ファンデーション", "brand": "SUQQU (スック)", "name": "ザ リクイド ファンデーション (国産美容エキス13種贅沢配合・極上の艶膜が肌を包み込む最高峰リキッド)"},
            {"rank": 6, "query": "シュウウエムラ アンリミテッド ケア ツヤ セラム ファンデーション", "brand": "shu uemura (シュウ ウエムラ)", "name": "アンリミテッド ケア ツヤ セラム ファンデーション (日本のツバキオイル配合・乾燥くすみを防ぎ長時間しっとり密着)"},
            {"rank": 7, "query": "RMK リクイドファンデーション フローレスカバレッジ", "brand": "RMK (アールエムケー)", "name": "リクイドファンデーション フローレスカバレッジ (アミノ酸誘導体×シアバター・みずみずしい抜け感ツヤ肌)"},
            {"rank": 8, "query": "エトヴォス ミネラルフレッシュスキンリキッド", "brand": "ETVOS (エトヴォス)", "name": "ミネラルフレッシュスキンリキッド (ヒト型セラミド5種×植物オイル・石けんオフ可能な敏感肌救済ファンデ)"},
            {"rank": 9, "query": "マキアージュ ドラマティックエッセンスリキッド", "brand": "MAQuillAGE (マキアージュ)", "name": "ドラマティックエッセンスリキッド (フルカバー×高保湿乳液処方・毛穴落ちと乾燥崩れをWブロック)"},
            {"rank": 10, "query": "メイベリン フィットミー リキッド ファンデーション R", "brand": "MAYBELLINE NEW YORK (メイベリン ニューヨーク)", "name": "フィットミー リキッド ファンデーション R (ビタミンE配合・冬の乾燥崩れを防ぎながら素肌感をキープする高コスパ名品)"}
        ]
    },
    "winter_cream_cheek": {
        "title": "保湿力の強さで肌乾燥・寒暖差くすみとさようなら！冬の冷え切った頬にじゅわっと上気ツヤを仕込む高保湿チークランク10",
        "page_file": "winter-cream-cheek.html",
        "items": [
            {"rank": 1, "query": "シャネル リップ＆チーク ボーム N°1 ドゥ シャネル", "brand": "CHANEL (シャネル)", "name": "リップ＆チーク ボーム N°1 ドゥ シャネル (レッドカメリアオイル配合・体温でとろけて唇と頬をしっとり彩る)"},
            {"rank": 2, "query": "アディクション チークポリッシュ", "brand": "ADDICTION (アディクション)", "name": "チークポリッシュ (ローズヒップオイル×シアバター・みずみずしく肌に溶け込み内側から上気したような血色感)"},
            {"rank": 3, "query": "コスメデコルテ クリーム ブラッシュ", "brand": "DECORTÉ (コスメデコルテ)", "name": "クリーム ブラッシュ (スクワラン高配合・弾力のあるスフレタッチで乾燥知らずのしっとりハリツヤ)"},
            {"rank": 4, "query": "ローラメルシエ ティンティド モイスチャライザー ブラッシュ", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "ティンティド モイスチャライザー ブラッシュ (12時間保湿持続・植物性ボタニカルブレンドで乾燥肌をふっくら演出)"},
            {"rank": 5, "query": "エトヴォス ミネラルマルチパウダー", "brand": "ETVOS (エトヴォス)", "name": "ミネラルマルチパウダー (アルガンオイル配合・目元・頬・唇に使えるしっとり低刺激マルチバームパウダー)"},
            {"rank": 6, "query": "hince トゥルーディメンション グロウチーク", "brand": "hince (ヒンス)", "name": "トゥルーディメンション グロウチーク (微細パール×クレイテクスチャー・粉飛び皆無で澄んだ水彩画のような発色)"},
            {"rank": 7, "query": "アンドビー &be クリームチーク", "brand": "&be (アンドビー)", "name": "クリームチーク (河北裕介プロデュース・天然由来植物油配合で冬の乾燥小じわに入り込まない上品ツヤ)"},
            {"rank": 8, "query": "キャンメイク クリームチーク", "brand": "CANMAKE (キャンメイク)", "name": "クリームチーク (エモリエント成分配合・体温でとろけるジェルテクスチャーで長年愛される名品)"},
            {"rank": 9, "query": "セザンヌ チークブラッシュ", "brand": "CEZANNE (セザンヌ)", "name": "チークブラッシュ (美容オイル高配合パウダー・しっとり素肌に密着して粉浮きしない驚きのプチプラ)"},
            {"rank": 10, "query": "フーミー リップ＆チーク", "brand": "WHOMEE (フーミー)", "name": "リップ＆チーク (イガリシノブプロデュース・植物スクワラン×セラミド配合で冬の血色感をじゅわっと引き出す)"}
        ]
    },
    "winter_cream_eyeshadow": {
        "title": "保湿力の強さでまぶたの乾燥・二重幅の粉落ちとさようなら！濡れツヤと透明感を一日中キープする高保湿アイシャドウランク10",
        "page_file": "winter-cream-eyeshadow.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ アイグロウジェム スキンシャドウ", "brand": "DECORTÉ (コスメデコルテ)", "name": "アイグロウジェム スキンシャドウ (うるおい弾力ベース・湿度を感じる濡れツヤと密着感で冬の目元をケア)"},
            {"rank": 2, "query": "ローラメルシエ キャビアスティック アイカラー", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "キャビアスティック アイカラー (クリーミーな描き心地・乾燥まぶたにもスルスル伸びてピタッと高密着)"},
            {"rank": 3, "query": "ボビイブラウン ロングウェア クリーム シャドウ スティック", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "ロングウェア クリーム シャドウ スティック (高い保湿効果×16時間持続・冬の乾燥によるヨレを完全防止)"},
            {"rank": 4, "query": "アディクション ザ アイシャドウ スパークル", "brand": "ADDICTION (アディクション)", "name": "ザ アイシャドウ スパークル (高密着オイル配合・ホリデーの煌めきを粉飛びゼロでまぶたに密着)"},
            {"rank": 5, "query": "エトヴォス ミネラルアイバーム", "brand": "ETVOS (エトヴォス)", "name": "ミネラルアイバーム (美容クリーム処方×天然ミネラル・目元の乾燥小じわをケアしながら繊細に輝くスキンケアアイシャドウ)"},
            {"rank": 6, "query": "シャネル オンブル プルミエール ラック", "brand": "CHANEL (シャネル)", "name": "オンブル プルミエール ラック (みずみずしいリキッドテクスチャー・まぶたを乾燥から守りメタリックな光沢を演出)"},
            {"rank": 7, "query": "SUQQU リクイド ラスター アイズ", "brand": "SUQQU (スック)", "name": "リクイド ラスター アイズ (うるおい膜を形成するリキッド・光と影が揺らめく洗練された大人の冬アイメイク)"},
            {"rank": 8, "query": "フジコ シェイクシャドウ SV", "brand": "Fujiko (フジコ)", "name": "シェイクシャドウ SV (水と光の粒をシェイク・油分ゼロなのにみずみずしく二重幅にたまらない密着力)"},
            {"rank": 9, "query": "キャンメイク アイカラーマジシャン", "brand": "CANMAKE (キャンメイク)", "name": "アイカラーマジシャン (リキッドなのにサラサラ密着・速乾で夜までヨレない高密着イルミネーションシャドウ)"},
            {"rank": 10, "query": "エクセル イルミクチュールシャドウ", "brand": "excel (エクセル)", "name": "イルミクチュールシャドウ (セラミド×シアバター配合・体温でとろけるクリーム処方で冬のまぶたをしっとり彩る)"}
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
                    shop_name = chosen.get("shopName", "")
                    reviews = chosen.get("reviewCount", 0)
                    rev_avg = chosen.get("reviewAverage", 0.0)
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "search_query": raw_q,
                        "raw_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "formatted_price": f"¥{price:,}",
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": shop_name,
                        "review_count": reviews,
                        "review_average": rev_avg
                    }
                else:
                    parts = query.split()
                    if len(parts) > 2:
                        query = " ".join(parts[:2])
                        continue
        except Exception as e:
            print(f"Error on {query_info['name']} (attempt {attempt+1}): {e}")
            time.sleep(1)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "search_query": raw_q,
        "raw_item_name": query_info["name"],
        "price": 0,
        "formatted_price": "¥0",
        "image_url": "",
        "affiliate_url": "",
        "shop_name": "",
        "review_count": 0,
        "review_average": 0.0
    }

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\nFetching items for {cat_key}: {cat_data['title']}...")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"  Rank {item_info['rank']}: {item_info['brand']} {item_info['name']} (Query: {item_info['query']})")
        item_res = fetch_item_with_retry(item_info)
        print(f"    -> Result: {item_res['formatted_price']} | Shop: {item_res['shop_name'][:20]} | Img: {bool(item_res['image_url'])}")
        results[cat_key]["items"].append(item_res)
        time.sleep(0.3)

output_filename = "rakuten_liquid_cheek_eyeshadow_data.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully saved all item data to {output_filename}")
