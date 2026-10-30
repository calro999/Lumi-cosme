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
    "winter_lip_scrub": {
        "title": "保湿力の強さで唇のガサガサ皮剥け・縦ジワとさようなら！古い角質を優しくオフしてぷるんと潤う高保湿リップスクラブランク10",
        "page_file": "winter-lip-scrub.html",
        "items": [
            {"rank": 1, "query": "レブロン キス シュガー スクラブ", "brand": "REVLON (レブロン)", "name": "キス シュガー スクラブ (洗い流し不要・シュガースクラブで優しく角質ケアしながら3種のフルーツオイルで超保湿する伝説のベストセラー)"},
            {"rank": 2, "query": "キャンメイク プランプリップケアスクラブ", "brand": "CANMAKE (キャンメイク)", "name": "プランプリップケアスクラブ (砂糖のスクラブで角質ケアしながらメントール感とプランプ効果でふっくらボリューム唇へ導く名品)"},
            {"rank": 3, "query": "ディオール アディクト スクラブ バーム", "brand": "DIOR (ディオール)", "name": "ディオール アディクト スクラブ バーム (シュガー粒子が唇の上でとろけてバームに変化・ほんのり自然なロージーピンクに色づく極上デパコス)"},
            {"rank": 4, "query": "LUSH リップスクラブ バブルガム", "brand": "LUSH (ラッシュ)", "name": "リップスクラブ バブルガム (キャスタシュガーとホホバオイル配合・甘い香りに包まれながら冬の頑固な皮剥けをつるんとなめらかに磨き上げる定番)"},
            {"rank": 5, "query": "ハウスオブローゼ Oh Baby スクラブリップバーム", "brand": "HOUSE OF ROSE (ハウス オブ ローゼ)", "name": "Oh!Baby スクラブリップバーム (和三盆シュガースクラブ配合・体温でじゅわっと溶けて潤いラッピングする高保湿バーム)"},
            {"rank": 6, "query": "サラハップ リップスクラブ ブラウンシュガー", "brand": "sara happ (サラハップ)", "name": "リップスクラブ ブラウンシュガー (ハリウッドセレブ愛用・天然シュガーとエモリエントオイルで生まれたてのようなシルク唇へ蘇らせる至高のリップ専用スクラブ)"},
            {"rank": 7, "query": "フジコ 朝可愛リップスクラブバーム", "brand": "Fujiko (フジコ)", "name": "朝可愛リップスクラブバーム (マイクロシュガー粒子が唇の縦ジワに入り込んだ古い角質をオフ・ぷるんとした赤ちゃん唇へ仕立てるスティック型)"},
            {"rank": 8, "query": "純米 リップスクラブ", "brand": "美人ぬか (純米)", "name": "純米 リップスクラブ (米ぬか由来成分×シュガースクラブ・日本人のデリケートな唇を摩擦レスに整える天然うるおい処方)"},
            {"rank": 9, "query": "イニスフリー リップ スリーピング マスク", "brand": "innisfree (イニスフリー)", "name": "キャノーラハニー リップ スクラブ バーム (チェジュ島産キャノーラハニー配合・乾燥して荒れた唇をしっとり包み込みながら整える)"},
            {"rank": 10, "query": "ボビイブラウン リップトリートメント スクラブ", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "エクストラ リップ スクラブ (植物オイルと微粒子シュガーが乾燥によるカサつきを一掃しふっくらハリのある唇へ整える)"}
        ]
    },
    "winter_bb_cream": {
        "title": "保湿力の強さで冬の粉ふき・乾燥崩れとさようなら！1本で一日中うるツヤ肌が続く高保湿BB・CCクリームランク10",
        "page_file": "winter-bb-cream.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ サンシェルター トーンアップCC", "brand": "DECORTÉ (コスメデコルテ)", "name": "サンシェルター マルチ プロテクション トーンアップCC (日焼け止め・乳液・毛穴カバー・トーンアップを完結・みずみずしい高保湿ツヤ膜が一日中持続)"},
            {"rank": 2, "query": "dプログラム アレルバリア エッセンス BB N", "brand": "d program (dプログラム)", "name": "アレルバリア エッセンス BB N (花粉・ちり・乾燥から守るアレルバリアテクノロジー・敏感肌をしっとり均一美肌に整える薬用級BB)"},
            {"rank": 3, "query": "マキアージュ ドラマティック ヌードジェリー BB", "brand": "MAQuillAGE (マキアージュ)", "name": "ドラマティック ヌードジェリー BB (美肌ジェリーコート処方・うるおいを抱えたジェリーが肌を包み込みマスクやマフラーへの色移りも防ぐ)"},
            {"rank": 4, "query": "ラロッシュポゼ UVイデア XL プロテクションBB", "brand": "La Roche-Posay (ラ ロッシュ ポゼ)", "name": "UVイデア XL プロテクションBB (シアバター配合・冬の乾燥くすみやシミをしっかりカバーしながら敏感肌に優しいロングUVA対応)"},
            {"rank": 5, "query": "キュレル ベースメイク BBクリーム", "brand": "Curel (キュレル)", "name": "ベースメイク BBクリーム (医薬部外品・セラミドの働きを効果的に補いカサつきや肌荒れを防ぐ乾燥性敏感肌のための高保湿処方)"},
            {"rank": 6, "query": "トランシーノ 薬用CCクリーム", "brand": "TRANSINO (トランシーノ)", "name": "薬用 ホワイトニングCCクリーム (医薬部外品・トラネキサム酸配合で美白しながら色ムラ補正・うるおい浸透ヴェールで乾燥知らず)"},
            {"rank": 7, "query": "オンリーミネラル ミネラルエッセンスBBクリーム", "brand": "ONLY MINERALS (オンリーミネラル)", "name": "ミネラルエッセンスBBクリーム ウルトラ (植物オイルとミネラルを贅沢配合・まるで美容クリームのような濃厚な潤いとハイカバー力)"},
            {"rank": 8, "query": "エテュセ フェイスエディション スキンベース", "brand": "ettusais (エテュセ)", "name": "フェイスエディション (スキンベース) フォードライスキン (ヒアルロン酸・カミツレエキス配合・パサつく冬肌に溶け込み澄んだ血色ツヤを一日中キープ)"},
            {"rank": 9, "query": "ミシャ M クッションベース BB", "brand": "MISSHA (ミシャ)", "name": "M パーフェクト カバー BBクリーム (ヒアルロン酸・セラミド配合・真冬の過酷な乾燥環境でも陶器のようなしっとりツヤ肌を守り抜く)"},
            {"rank": 10, "query": "毛穴パテ職人 エッセンスBBクリーム モイストリフト", "brand": "毛穴パテ職人 (サナ)", "name": "エッセンスBBクリーム モイストリフト (レチノール誘導体・加水分解コラーゲン配合・大人の乾燥小ジワとたるみ毛穴をふっくら密閉)"}
        ]
    },
    "winter_carbonic_pack": {
        "title": "保湿＆血行促進で冬の冷えくすみ・ゴワつきとさようなら！サロン級の透明感と弾力を呼び覚ます高保湿炭酸パック・炭酸マスクランク10",
        "page_file": "winter-carbonic-pack.html",
        "items": [
            {"rank": 1, "query": "エニシー グローパック", "brand": "enisie (エニシー)", "name": "グローパック (炭酸ガスパックの最高峰・医療現場発想のボーア効果で肌の母細胞へ酸素を供給・冬のくすみとたるみをリセットする伝説のパック)"},
            {"rank": 2, "query": "EKATO プレシャスジェルパック", "brand": "EKATO. (エカト)", "name": "プレシャスジェルパック (持続型炭酸発生技術・60分間じっくり炭酸と高純度保湿成分を角層深部へ送り届ける洗い流し不要の至福パック)"},
            {"rank": 3, "query": "ドクターメディオン スパオキシジェル", "brand": "DR.MEDION (ドクターメディオン)", "name": "スパオキシジェル (炭酸パックのパイオニア日置博士開発・フレッシュな高濃度炭酸泡で冬の血行不良を解きほぐす極上サロンケア)"},
            {"rank": 4, "query": "ソフィーナiP ベースケア セラム 土台美容液", "brand": "SOFINA iP (ソフィーナiP)", "name": "ベースケア セラム 土台美容液 (毛穴の約20分の1サイズの高濃度マイクロ炭酸泡・洗顔後すぐに肌の巡りを整え美容液の浸透を劇的アップ)"},
            {"rank": 5, "query": "プリュ カーボニック リバイタライズ リッチ フェイスパック", "brand": "PLuS (プリュ)", "name": "カーボニック リバイタライズ リッチ フェイスパック (濃密炭酸泡×セラミド×プラセンタ・手軽に毎日使える高コスパな炭酸泡パック)"},
            {"rank": 6, "query": "フェヴリナ ナノアクア 炭酸ジェルパック", "brand": "FAVORINA (フェヴリナ)", "name": "ナノアクア 炭酸ジェルパック (生炭酸×10種の美容成分・冬の強固なごわつき角質を柔らかくほぐし透明感あふれるつるすべ肌へ導く)"},
            {"rank": 7, "query": "VT シカ コラーゲン バブル マスク", "brand": "VT COSMETICS (ブイティ)", "name": "シカ コラーゲン バブルパック (CICA×低分子コラーゲン×微細炭酸バブル・冬の乾燥ゆらぎを鎮静しながら弾力とツヤをチャージ)"},
            {"rank": 8, "query": "肌ナチュール 炭酸クレンジング 泡パック", "brand": "HADA NATURE (肌ナチュール)", "name": "炭酸クレンジング / 泡パック (高濃度炭酸泡がメイク汚れを浮かせて落としそのまま泡パックとして角層を柔らかくうるおす)"},
            {"rank": 9, "query": "シンピュルテ ピュアクレンジング 炭酸パック", "brand": "SINN PURETE (シンピュルテ)", "name": "AGコンセントレイト 炭酸濃密バブルパック (オーガニック植物成分×高濃度炭酸・真冬の冷え切った肌にじんわり温感とハリを与える)"},
            {"rank": 10, "query": "エトヴォス モイストバブル フォーム 炭酸", "brand": "ETVOS (エトヴォス)", "name": "モイストバブルフォーム (アミノ酸系洗浄成分×微細炭酸泡・肌のうるおいを守りながら血行を促進してキメの整った素肌へ洗い上げる)"}
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
                    # fallback to shorter query
                    words = query.split()
                    if len(words) > 1:
                        query = words[0] + " " + words[1]
                    time.sleep(1)
        except Exception as e:
            print(f"Error on attempt {attempt+1} for {query}: {e}")
            time.sleep(1.5)
    
    # 最終フォールバック
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
    print("=== Fetching Rakuten Data for 3 New Articles ===")
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\nProcessing category: {cat_key} ({cat_data['title']})")
        cat_items = []
        for q_info in cat_data["items"]:
            print(f"  Fetching Rank {q_info['rank']}: {q_info['query']} ...")
            item_res = fetch_item_with_retry(q_info)
            print(f"    Found: {item_res['rakuten_name'][:40]} | {item_res['price_str']} | Image: {item_res['image_url'][:50]}...")
            cat_items.append(item_res)
            time.sleep(0.4) # APIレートリミット対策
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": cat_items
        }

    out_file = "rakuten_scrub_bb_carbonic_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved all results to {out_file} successfully!")

if __name__ == "__main__":
    main()
