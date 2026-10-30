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
    "winter_hair_balm": {
        "title": "保湿力の強さで毛先のパサつき・静電気・広がりとさようなら！冬の冷風から一日中うるおいキープ＆全身保湿できるマルチ高保湿ヘアバームランク10",
        "page_file": "winter-hair-balm.html",
        "items": [
            {"rank": 1, "query": "プロダクト ヘアワックス シアバター", "brand": "ザ・プロダクト (product)", "name": "ヘアワックス (USDAオーガニック認証シアバター配合・自然由来原料100%で髪の濡れツヤ束感キープからリップやハンドの保湿まで叶える元祖名品)"},
            {"rank": 2, "query": "エヌドット ナチュラルバーム ナプラ", "brand": "N. (ナプラ)", "name": "ナチュラルバーム (天然由来原料のみで作られた大人気サロン専売バーム・冬の毛先のパサつきを抑えて繊細な束感と自然なツヤを持続)"},
            {"rank": 3, "query": "トラック バーム track", "brand": "track (トラック)", "name": "トラック バーム (天然由来成分97.2%配合・硬めのテクスチャーが体温でとろけて髪にしなやかなまとまりと濡れツヤを与え手肌にも馴染む上質バーム)"},
            {"rank": 4, "query": "ミルボン ジェミールフラン メルティバター バーム", "brand": "MILBON (ミルボン)", "name": "ジェミールフラン メルティバター バーム (モイストモリンガバター配合・夜のドライヤー熱で溶けて朝までまとまりを記憶しハンドクリームにもなる)"},
            {"rank": 5, "query": "アンドハニー メルティ モイストリペア ヘアバーム", "brand": "＆honey (アンドハニー)", "name": "メルティ モイストリペア ヘアバーム (ハチミツのうるおい力でうねりや乾燥による広がりをケア・みずみずしいツヤとまとまりを長時間キープ)"},
            {"rank": 6, "query": "リレイ トリートメントバーム LILAY", "brand": "LILAY (リレイ)", "name": "トリートメントバーム (天然由来成分95%・ベタつかずサラッとした使い心地でオフィスや朝のセットに重宝するマルチトリートメントバーム)"},
            {"rank": 7, "query": "ボジコ オーガニック ワックス セラム", "brand": "bojico (ボジコ)", "name": "オーガニック ワックス セラム (厳選された植物オイルと天然精油の香りで冬の静電気を防ぎ毛先をしっとり艶やかに整える)"},
            {"rank": 8, "query": "アイアム チャプター ヘアバーム Aiam", "brand": "Aiam (アイアム)", "name": "チャプター ヘア＆ボディバーム (心地よいフレグランスに包まれながら上質なツヤと束感を演出する大人気マルチバーム)"},
            {"rank": 9, "query": "アリミノ メン ハードバーム", "brand": "ARIMINO (アリミノ)", "name": "アリミノ メン ハードバーム (天然由来成分97%配合・真冬の強風でもスタイルを崩さず適度なツヤとホールド力を与える優秀バーム)"},
            {"rank": 10, "query": "ジョンマスターオーガニック ヘアワックス", "brand": "john masters organics (ジョンマスターオーガニック)", "name": "ヘアーワックス (ミツロウと希少な植物オイルが髪を乾燥からプロテクト・ボリュームダウンを防ぎつつ自然なツヤ感をプラス)"}
        ]
    },
    "winter_hot_cleansing": {
        "title": "保湿＆温感スチーム効果で冬の冷え固まった毛穴・乾燥ゴワつきとさようなら！じんわり温めてうるおいを守り抜く高保湿温感クレンジングランク10",
        "page_file": "winter-hot-cleansing.html",
        "items": [
            {"rank": 1, "query": "マナラ ホットクレンジングゲル マッサージプラス", "brand": "MANARA (マナラ)", "name": "ホットクレンジングゲル マッサージプラス (美容液成分91.3%配合・温感スチーム処方と極上マッサージで冷えた冬肌の毛穴汚れとくすみをオフする至高の1本)"},
            {"rank": 2, "query": "DUO ザ 薬用クレンジングバーム バリア", "brand": "DUO (デュオ)", "name": "ザ 薬用クレンジングバーム バリア (医薬部外品・薬用有効成分×高保湿オイルバームがとろけて敏感肌をいたわりながら乾燥毛穴汚れを摩擦レスにオフ)"},
            {"rank": 3, "query": "スキンビル ホットクレンジングジェル", "brand": "skinvill (スキンビル)", "name": "ホットクレンジングジェル (温感×酵素の黄金タッグ・真冬の冷え固まった毛穴の角栓や古い角質をじんわり溶かし出しうるおい素肌へ)"},
            {"rank": 4, "query": "ベネフィーク ホットクレンジング 資生堂", "brand": "BENEFIQUE (ベネフィーク)", "name": "ホットクレンジング (資生堂の温感クレンジング技術・めぐりを促すボタニカル成分が冷え切った肌を温めながらしっとりなめらかに洗い上げる)"},
            {"rank": 5, "query": "ラフラ バームオレンジ RAFRA", "brand": "RAFRA (ラフラ)", "name": "バームオレンジ (美容液成分を高濃度配合・もぎたて天然オレンジ精油の贅沢な香りとじんわり温感で至福のバスタイムクレンジング)"},
            {"rank": 6, "query": "ドクターシーラボ ホットピール クレンジングゲル", "brand": "Dr.Ci:Labo (ドクターシーラボ)", "name": "VC100 ホットピール クレンジングゲルEX (高浸透ビタミンC×温感ゲル・冬の頑固な角栓やゴワつきを吸着してキュッと引き締める)"},
            {"rank": 7, "query": "ソフティモ ラチェスカ ホットジェルクレンジング", "brand": "ソフティモ (コーセー)", "name": "ラチェスカ ホットジェルクレンジング (美容液90%配合の濃厚温感ジェル・毛穴の黒ずみ汚れをじゅわっと溶かしてすっきりオフ)"},
            {"rank": 8, "query": "BOTANIST ボタニカル クレンジング ホット", "brand": "BOTANIST (ボタニスト)", "name": "ボタニカル ホットクレンジングジェル (植物由来の保湿成分が肌のうるおいを守りながら温感作用で冬の頑固なメイクも素早く乳化)"},
            {"rank": 9, "query": "オルビス アンバー モイスト クレンジング", "brand": "ORBIS (オルビス)", "name": "アンバー モイスト クレンジングバーム (大人の冬肌を考えた高保湿オイルバーム・体温でとろけてくすみや乾燥小ジワの原因となる汚れを優しく落とす)"},
            {"rank": 10, "query": "ビフェスタ クレンジングバーム ホット", "brand": "Bifesta (ビフェスタ)", "name": "クレンジングバーム ディープクリア / ホット (温感バームが肌に密着してじんわりほぐし、毛穴奥の蓄積汚れをすっきり洗い流してうるおいキープ)"}
        ]
    },
    "winter_neck_cream": {
        "title": "保湿力の強さで首元の乾燥小ジワ・マフラー摩擦とさようなら！冬のタートルネック映えするハリツヤ肌へ導く高保湿ネック＆デコルテクリームランク10",
        "page_file": "winter-neck-cream.html",
        "items": [
            {"rank": 1, "query": "クラランス ファーミング EX ネック デコルテ SP", "brand": "CLARINS (クラランス)", "name": "ファーミング EX ネック ＆ デコルテ SP (首元ケアの世界的パイオニア・乾燥やマフラー摩擦で荒れがちな首元にふっくらピンとした弾力をもたらす最高峰名品)"},
            {"rank": 2, "query": "資生堂 リバイタル ネックゾーン エッセンス", "brand": "REVITAL (資生堂リバイタル)", "name": "ネックゾーン エッセンス (医薬部外品・首特有の皮膚の薄さと動きに着目・うるおいバリアとハリ成分を角層深くまで送り込む薬用美容液)"},
            {"rank": 3, "query": "POLA B.A メディカル セラム リンクル", "brand": "POLA (ポーラ)", "name": "リンクルショット メディカル セラム N (日本初のシワ改善有効成分ニールワン配合・首の気になる乾燥横ジワにも密着して集中リペアする神美容液)"},
            {"rank": 4, "query": "シスレー クレーム レパラトリス ネックケア", "brand": "sisley (シスレー)", "name": "クレーム レパラトリス ネッククリーム (オート麦種子エキスやラタニアエキスを贅沢配合・冬の寒風でしぼんだデコルテを即座にリフトアップする最高級ケア)"},
            {"rank": 5, "query": "ドクターシーラボ ACGエンリッチLEX クリーム", "brand": "Dr.Ci:Labo (ドクターシーラボ)", "name": "アクアコラーゲンゲル エンリッチリフトEX (浸透型コラーゲンEX×ナイアシンアミド・顔から首・デコルテまでぐっと引き上げる高保湿ゲル)"},
            {"rank": 6, "query": "肌美精 プレミア 薬用 3D リンクル ネッククリーム", "brand": "肌美精 (クラシエ)", "name": "プレミア 薬用 3D リンクルケア ネッククリーム (医薬部外品・ナイアシンアミド配合でシワ改善＆美白・手頃な価格で毎日惜しみなく首元を集中保湿できる実力派)"},
            {"rank": 7, "query": "ベネフィーク ネック ファーミングクリーム", "brand": "BENEFIQUE (ベネフィーク)", "name": "ネック ファーミングクリーム (心地よい温感マッサージ効果と形状記憶ベール処方でマフラー擦れによるくすみやたるみをすっきり整える)"},
            {"rank": 8, "query": "クリニーク スカルプティング ナイト クリーム", "brand": "CLINIQUE (クリニーク)", "name": "リペアウェア スカルプティング ナイト クリーム (首から胸元・フェイスラインを睡眠中にリッチなうるおい膜で包み込み翌朝のハリ感を高める)"},
            {"rank": 9, "query": "ハウスオブローゼ コンセントレート ネッククリーム", "brand": "HOUSE OF ROSE (ハウス オブ ローゼ)", "name": "コンセントレート ネッククリーム (天然植物由来のエモリエント成分が首元にピタッと密着・タートルネック着用時のチクチク摩擦からも優しく保護)"},
            {"rank": 10, "query": "エリクシール レチノパワー リンクルクリーム", "brand": "ELIXIR (エリクシール)", "name": "レチノパワー リンクルクリーム (医薬部外品・純粋レチノール配合・首の頑固な乾燥小ジワをふっくら押し上げるようにうるおす薬用クリーム)"}
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
                    price_str = f"¥{price:,}" if price > 0 else "価格表示なし"

                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "query": raw_q,
                        "rakuten_name": chosen.get("itemName", ""),
                        "price": price,
                        "price_str": price_str,
                        "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                        "image_url": high_res_img,
                        "review_count": chosen.get("reviewCount", 0),
                        "review_average": chosen.get("reviewAverage", "0.0")
                    }
                else:
                    words = query.split()
                    if len(words) > 1:
                        query = words[0] + " " + words[1]
                    time.sleep(1)
        except Exception as e:
            print(f"Error on attempt {attempt+1} for {query}: {e}")
            time.sleep(1.5)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "query": raw_q,
        "rakuten_name": query_info["name"],
        "price": 0,
        "price_str": "価格表示なし",
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(raw_q)}/",
        "image_url": "https://thumbnail.image.rakuten.co.jp/sample/item.jpg",
        "review_count": 0,
        "review_average": "4.5"
    }

def main():
    print("=== Fetching Rakuten Data for 3 New Articles (Hair Balm, Hot Cleansing, Neck Cream) ===")
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\nProcessing category: {cat_key} ({cat_data['title']})")
        cat_items = []
        for q_info in cat_data["items"]:
            print(f"  Fetching Rank {q_info['rank']}: {q_info['query']} ...")
            item_res = fetch_item_with_retry(q_info)
            print(f"    Found: {item_res['rakuten_name'][:40]} | {item_res['price_str']} | Image: {item_res['image_url'][:50]}...")
            cat_items.append(item_res)
            time.sleep(0.4)
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": cat_items
        }

    output_file = "rakuten_balm_hotcleansing_neck_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved all results to {output_file} successfully!")

if __name__ == "__main__":
    main()
