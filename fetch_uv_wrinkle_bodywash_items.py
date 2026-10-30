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
    "winter_uv_cream": {
        "title": "保湿力の強さで冬の紫外線＆乾燥ツッパリとさようなら！まるで美容クリームな極上高保湿日焼け止め・UV美容液ランク10",
        "page_file": "winter-uv-cream.html",
        "items": [
            {"rank": 1, "query": "カネボウ ヴェイル オブ デイ", "brand": "KANEBO (カネボウ)", "name": "ヴェイル オブ デイ (水相成分約75%配合・継続保水ヴェールで夕方までツッパリ知らずの極上UV美容液)"},
            {"rank": 2, "query": "コスメデコルテ サンシェルター マルチプロテクション コンフォート", "brand": "DECORTÉ (コスメデコルテ)", "name": "サンシェルター マルチ プロテクション コンフォート (みずみずしい水膜ヴェール・乾燥と大気中の微粒子から肌を守る高機能UV)"},
            {"rank": 3, "query": "オルビス リンクルブライトUVプロテクター", "brand": "ORBIS (オルビス)", "name": "リンクルブライトUVプロテクター (医薬部外品・ナイアシンアミド配合でシワ改善＆美白しながら高保湿する薬用UV)"},
            {"rank": 4, "query": "クレドポーボーテ クレームUV n", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "クレームUV n (スキンケアクリームそのものの至高のテクスチャー・太陽光を選別して取り込む最高峰エイジングケアUV)"},
            {"rank": 5, "query": "POLA BA ライト セレクター N", "brand": "POLA (ポーラ)", "name": "B.A ライト セレクター N (肌に良い赤色光を透過し紫外線と近赤外線をカット・ハリと弾力を育む日中用クリーム)"},
            {"rank": 6, "query": "ラロッシュポゼ UVイデア XL プロテクショントーンアップ ローズ", "brand": "La Roche-Posay (ラ ロッシュ ポゼ)", "name": "UVイデア XL プロテクショントーンアップ ローズ (シアバター配合・低刺激＆高保湿で血色感と澄んだ透明感を仕込む王道UV)"},
            {"rank": 7, "query": "アディクション スキンプロテクター", "brand": "ADDICTION (アディクション)", "name": "スキンプロテクター (無色透明・メドウフォーム油配合でベタつかずみずみずしい水分膜をキープする名品)"},
            {"rank": 8, "query": "キュレル 潤浸保湿 UVクリーム", "brand": "Curel (キュレル)", "name": "潤浸保湿 UVクリーム (医薬部外品・セラミド機能成分配合・赤みやカサつきを防ぐ乾燥性敏感肌用UV)"},
            {"rank": 9, "query": "アネッサ デイセラム", "brand": "ANESSA (アネッサ)", "name": "デイセラム (サンデュアルケア技術・紫外線を美容の光に変換しながら一日中潤いで満たす美容乳液UV)"},
            {"rank": 10, "query": "スキンアクア ネクスタ トーンアップセラムUV", "brand": "SKIN AQUA NEXTA (スキンアクア ネクスタ)", "name": "トーンアップ セラムUVエッセンス (持続型セラムパック処方・大人の乾燥肌にしっとり密着する高コスパ名品)"}
        ]
    },
    "winter_wrinkle_cream": {
        "title": "保湿力の強さで冬の乾燥小ジワ・ほうれい線とさようなら！角層深く密着する高保湿シワ改善リンクルクリームランク10",
        "page_file": "winter-wrinkle-cream.html",
        "items": [
            {"rank": 1, "query": "エリクシール レチノパワー リンクルクリーム", "brand": "ELIXIR (エリクシール)", "name": "レチノパワー リンクルクリーム (医薬部外品・純粋レチノール配合・冬の乾燥小ジワから深いシワまで押し返す薬用エース)"},
            {"rank": 2, "query": "ポーラ リンクルショット メディカル セラム N", "brand": "POLA (ポーラ)", "name": "リンクルショット メディカル セラム N (医薬部外品・日本初認可成分ニールワン配合・好中球エラスターゼを阻害する世界的名品)"},
            {"rank": 3, "query": "コスメデコルテ iP.Shot プルリポテント ユース コンセントレイト", "brand": "DECORTÉ (コスメデコルテ)", "name": "iP.Shot プルリポテント ユース コンセントレイト (医薬部外品・トラネキサム酸×ナイアシンアミド・表皮と真皮にWアプローチ)"},
            {"rank": 4, "query": "カネボウ リンクル リフト セラム", "brand": "KANEBO (カネボウ)", "name": "リンクル リフト セラム (医薬部外品・ナイアシンアミド配合・吸い付くように密着し跳ね返すようなハリを密閉)"},
            {"rank": 5, "query": "ソフィーナiP 薬用リンクルセラム", "brand": "SOFINA iP (ソフィーナiP)", "name": "薬用 シワ改善セラム (医薬部外品・ナイアシンアミド配合・凹凸密着ラッピング技術で目元・口元の溝を満たす)"},
            {"rank": 6, "query": "オルビス リンクルブライトセラム", "brand": "ORBIS (オルビス)", "name": "リンクルブライトセラム (医薬部外品・Wナイアシン配合・表情の動きにしなやかに追従する高保水ストレッチ膜)"},
            {"rank": 7, "query": "なめらか本舗 リンクルアイクリーム N", "brand": "なめらか本舗 (サナ)", "name": "リンクルアイクリーム N (ピュアレチノール×豆乳発酵液・目元やほうれい線に惜しみなく使える感動の濃密プチプラ)"},
            {"rank": 8, "query": "資生堂 バイタルパーフェクション リンクルリフト ディープレチノホワイト5", "brand": "SHISEIDO (資生堂)", "name": "バイタルパーフェクション リンクルリフト ディープレチノホワイト5 (医薬部外品・純粋レチノール＋4MSK・シワ改善と美白の頂点)"},
            {"rank": 9, "query": "キールズ DS RTN リニューイング セラム", "brand": "KIEHL'S (キールズ)", "name": "DS RTN リニューイング セラム (マイクロレチノール×セラミド×ペプチド配合・刺激を抑えて日々のターンオーバーを促す)"},
            {"rank": 10, "query": "肌ラボ 極潤 薬用ハリクリーム", "brand": "肌ラボ (ロート製薬)", "name": "極潤 薬用ハリクリーム (医薬部外品・ナイアシンアミド×3種のヒアルロン酸・角質層深くまで高浸透する密着ラッピングジェルクリーム)"}
        ]
    },
    "winter_body_wash": {
        "title": "保湿力の強さで冬のお風呂上がり乾燥・かゆみとさようなら！うるおいを守ってしっとり洗い上げる高保湿ボディウォッシュランク10",
        "page_file": "winter-body-wash.html",
        "items": [
            {"rank": 1, "query": "ケアセラ 泡高保湿ボディウォッシュ", "brand": "CareCera (ケアセラ)", "name": "泡の高保湿ボディウォッシュ (8種の天然型セラミド配合・セラミド保持処方で洗うたびにお風呂上がりのカサつきを根本ブロック)"},
            {"rank": 2, "query": "ミノン 全身シャンプー しっとりタイプ", "brand": "MINON (ミノン)", "name": "全身シャンプー しっとりタイプ (医薬部外品・植物性アミノ酸系洗浄成分・肌のバリア機能を守ってカサつき・肌荒れを防ぐ)"},
            {"rank": 3, "query": "キュレル 泡ボディウォッシュ", "brand": "Curel (キュレル)", "name": "泡ボディウォッシュ (医薬部外品・肌の必須成分セラミドを守りながら汚れをすっきり落とす消炎剤配合のマイルド泡)"},
            {"rank": 4, "query": "サボン シャワーオイル", "brand": "SABON (サボン)", "name": "シャワーオイル (4種のボタニカルオイル配合・上質な泡立ちとラグジュアリーな香りで極上のシルク肌へと洗い上げる名品)"},
            {"rank": 5, "query": "ロクシタン アーモンド モイスチャライジング シャワーオイル", "brand": "L'OCCITANE (ロクシタン)", "name": "アーモンド モイスチャライジング シャワーオイル (スイートアーモンドオイル配合・水に触れると贅沢ミルク泡へと変化するオイル洗浄)"},
            {"rank": 6, "query": "ニベア クリームケア ボディウォッシュ W保水美肌", "brand": "NIVEA (ニベア)", "name": "クリームケア ボディウォッシュ W保水美肌 (アミノ酸系マイルド洗浄成分・角層保水成分配合・濃密もっちり泡でみずみずしく整える)"},
            {"rank": 7, "query": "バウンシア 高保湿ボディソープ", "brand": "Bouncia (バウンシア)", "name": "高保湿ボディソープ (シアバター・ヒアルロン酸・コラーゲン配合・誰でも簡単に作れる濃密弾力泡で摩擦ゼロ洗浄)"},
            {"rank": 8, "query": "クナイプ 泡ボディウォッシュ", "brand": "Kneipp (クナイプ)", "name": "泡ボディウォッシュ (天然植物オイル配合・リッチなボタニカルアロマと濃密泡で乾燥しがちな冬の素肌をしっとり保湿)"},
            {"rank": 9, "query": "メルヴィータ リラクセサンス マッサージ シャワージェル", "brand": "Melvita (メルヴィータ)", "name": "リラクセサンス マッサージ シャワージェル (オーガニックアルガンオイル配合・心地よいマッサージ洗いで冬の強張った肌を解きほぐす)"},
            {"rank": 10, "query": "hadakara 泡ボディソープ 薬用 保湿", "brand": "hadakara (ハダカラ)", "name": "薬用 泡ボディソープ (吸着保湿テクノロジー・すすぎ時に保湿成分が肌にしっかり吸着して洗い流されない革新処方)"}
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
                    affiliate_url = chosen.get("affiliateUrl", "")
                    item_url = chosen.get("itemUrl", "")
                    item_name = chosen.get("itemName", "")
                    review_count = chosen.get("reviewCount", 0)
                    review_average = chosen.get("reviewAverage", "0.0")

                    # もし画像が取れなかったり価格が0ならリトライ
                    if not high_res_img or price <= 0:
                        print(f"    [Warning] Missing image or zero price for '{query}', retrying with broader term...")
                        words = query.split()
                        if len(words) > 1:
                            query = words[0]
                            time.sleep(1)
                            continue

                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "query_used": query,
                        "rakuten_item_name": item_name,
                        "price": price,
                        "price_str": f"¥{price:,}" if price > 0 else "オープン価格",
                        "image_url": high_res_img,
                        "affiliate_url": affiliate_url if affiliate_url else item_url,
                        "review_count": review_count,
                        "review_average": review_average
                    }
                else:
                    print(f"    [Retry {attempt+1}] No items for query: '{query}'")
                    words = query.split()
                    if len(words) > 1:
                        query = words[0]
                    time.sleep(1)
        except Exception as e:
            print(f"    [Error attempt {attempt+1}] for '{query}': {e}")
            time.sleep(1.5)
            
    print(f"❌ FAILED to fetch for: {raw_q}")
    return None

results = {}

print("=== Starting Rakuten API Fetch for 3 Winter Categories (30 Items) ===")
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n--- Category: {cat_key} ({cat_data['title'][:30]}...) ---")
    cat_items = []
    for q_info in cat_data["items"]:
        print(f"Fetching #{q_info['rank']}: {q_info['brand']} - {q_info['query']} ...")
        res_item = fetch_item_with_retry(q_info)
        if res_item:
            cat_items.append(res_item)
            print(f"  ✓ Found: {res_item['rakuten_item_name'][:40]} | {res_item['price_str']} | Img: {res_item['image_url'][:50]}...")
        else:
            print(f"  ❌ Failed #{q_info['rank']}")
        time.sleep(0.3)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

output_file = "rakuten_uv_wrinkle_bodywash_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Successfully saved all 30 Rakuten items to {output_file}!")
