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
    "winter_advent_calendar": {
        "title": "保湿力の強さで冬のご褒美肌とさようなら乾燥！毎日開けるワクワクと濃密スキンケアが叶う人気コスメアドベントカレンダーランク10",
        "page_file": "winter-advent-calendar.html",
        "items": [
            {"rank": 1, "query": "ロクシタン アドベントカレンダー", "brand": "L'OCCITANE (ロクシタン)", "name": "ホリデー アドベントカレンダー (ベストセラーのシアハンドクリームやスキンケア・ボディケアが贅沢に詰まった冬限定の豪華BOX)"},
            {"rank": 2, "query": "キールズ アドベントカレンダー", "brand": "KIEHL'S (キールズ)", "name": "キールズ ホリデー アドベントカレンダー (名品UFCクリームやカレンデュラ化粧水・レチノール美容液など冬の集中保湿ケアが勢揃い)"},
            {"rank": 3, "query": "SABON アドベントカレンダー", "brand": "SABON (サボン)", "name": "SABON アドベントカレンダー (死海の塩ボディスクラブやシャワーオイル・フェイスポリッシャーなど冬のバスタイムを極上にする24アイテム)"},
            {"rank": 4, "query": "ポール&ジョー アドベントカレンダー メイクアップ コレクション", "brand": "PAUL & JOE (ポール＆ジョー)", "name": "メイクアップ コレクション アドベントカレンダー (大人気のモイスチュアライジングプライマーやリップ・限定コスメが詰まった心ときめく特別セット)"},
            {"rank": 5, "query": "クラランス アドベント カレンダー", "brand": "CLARINS (クラランス)", "name": "アドベント カレンダー (ダブルセーラムやリップオイル・ボディフィットなど冬の肌を引き締め潤す植物バイオスキンケア満載)"},
            {"rank": 6, "query": "ボディショップ アドベントカレンダー", "brand": "THE BODY SHOP (ザ・ボディショップ)", "name": "アドベントカレンダー ビューティー (高保湿シアボディバターやハンドクリーム・シャワージェルが毎日楽しめるヴィーガン仕様ホリデー)"},
            {"rank": 7, "query": "クリニーク アドベント カレンダー 24", "brand": "CLINIQUE (クリニーク)", "name": "クリニーク アドベント カレンダー 24 (モイスチャーサージシリーズの高保湿ジェルクリームやクレンジングバームなど皮膚科学発想の保湿ケア)"},
            {"rank": 8, "query": "イヴサンローラン アドベントカレンダー ノエル", "brand": "Yves Saint Laurent (イヴ・サンローラン)", "name": "ノエル アドベントカレンダー (ピュアショットシリーズやルージュピュールクチュールなどYSLのアイコンが揃ったラグジュアリーな冬の贈り物)"},
            {"rank": 9, "query": "ディオール アドベントカレンダー", "brand": "Dior (ディオール)", "name": "ディオール モンテーニュ アドベント カレンダー (プレステージやカプチュールトータルの高保湿スキンケア・ミスディオールの香りに包まれる至高のカレンダー)"},
            {"rank": 10, "query": "メルヴィータ アドベントカレンダー", "brand": "Melvita (メルヴィータ)", "name": "クリスマスコフレ アドベントカレンダー (アルガンオイルやローズ化粧水など100%オーガニック植物オイルの力で冬の砂漠肌を満たす)"}
        ]
    },
    "winter_hyaluronic_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！水分爆弾で超乾燥・インナードライを救う高保湿ヒアルロン酸美容液ランク10",
        "page_file": "winter-hyaluronic-serum.html",
        "items": [
            {"rank": 1, "query": "Torriden ダイブイン セラム 50ml", "brand": "Torriden (トリデン)", "name": "ダイブイン 低分子ヒアルロン酸 セラム 50ml (5種の分子サイズ異なるヒアルロン酸が角層深部まで素早く浸透・内側からパンッと弾む潤い肌へ)"},
            {"rank": 2, "query": "ラロッシュポゼ ヒアルB5 セラム", "brand": "LA ROCHE-POSAY (ラロッシュポゼ)", "name": "ヒアル B5 クリーミーセラム 30ml (2種の純粋ヒアルロン酸×パンテノール配合・敏感肌のバリアを整えながら濃密なハリと弾力をプラス)"},
            {"rank": 3, "query": "太陽のアロエ社 ヒアルロン酸 原液 80ml", "brand": "太陽のアロエ社", "name": "ヒアルロン酸原液 80ml (国内製造の高純度バイオヒアルロン酸100%・化粧水に混ぜても単体でも使える圧倒的保水力と高コスパ)"},
            {"rank": 4, "query": "コスメデコルテ リポソーム アドバンスト リペアセラム 50ml", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアセラム 50ml (1滴に1兆個の微細リポソームカプセル×ヒアルロン酸配合・24時間うるおいが続く名品美容液)"},
            {"rank": 5, "query": "The Ordinary ヒアルロン酸 2% + B5 30ml", "brand": "The Ordinary (ジオーディナリー)", "name": "ヒアルロン酸2% + B5 セラム 30ml (低・中・高分子ヒアルロン酸コンプレックス×プロビタミンB5・水分補給に特化したシンプル高濃度処方)"},
            {"rank": 6, "query": "VT スーパーヒアルロン セラム", "brand": "VT COSMETICS (ブイティー)", "name": "スーパーヒアルロン アンプルセラム 50ml (G:H8複合ヒアルロン酸×ガンマPGA配合・みずみずしい水分保護膜を形成し一日中乾かないツヤ肌へ)"},
            {"rank": 7, "query": "肌ラボ 極潤プレミアム ヒアルロン液 170ml", "brand": "肌ラボ (ロート製薬)", "name": "極潤プレミアム ヒアルロン液 170ml (世界初の乳酸発酵ヒアルロン酸を含む8種のヒアルロン酸を高濃度配合・美容液級の濃密保湿ローション)"},
            {"rank": 8, "query": "ドクターシーラボ スーパー100 ヒアルロン酸", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "スーパー100シリーズ ヒアルロン酸原液 30ml (高純度濃縮ヒアルロン酸が角層の水分抱水力を格段に高め乾燥による小ジワを目立たなくする)"},
            {"rank": 9, "query": "アベンヌ ハイドランス インテンス セラム", "brand": "Avene (アベンヌ)", "name": "ハイドランス インテンス セラム 30ml (コエドバイオテクノロジー×ヒアルロン酸・深層アベンヌ温泉水が乾いた角層を潤いで満たし続ける)"},
            {"rank": 10, "query": "魔女工場 パンテトイン エッセンス トナー", "brand": "魔女工場 (Manyo Factory)", "name": "パンテトイン エッセンス トナー 200ml (高保水ヒアルロン酸×エクトイン×パンテノール配合・極度の乾燥環境でも水分を逃さない濃密保水)"}
        ]
    },
    "winter_hand_wash": {
        "title": "保湿力の強さで冬の手洗い手荒れ・カサつき砂漠肌とさようなら！洗うたび潤いベールをまとう高保湿ハンドウォッシュランク10",
        "page_file": "winter-hand-wash.html",
        "items": [
            {"rank": 1, "query": "イソップ アンドラム アロマティック ハンドウォッシュ 500ml", "brand": "Aesop (イソップ)", "name": "アンドラム アロマティック ハンドウォッシュ 500ml (マンダリン・ローズマリー・シダーウッドの精油と植物オイル配合・手肌の潤いを守りながら優しく洗浄)"},
            {"rank": 2, "query": "SHIRO サボン クレイハンドソープ", "brand": "SHIRO (シロ)", "name": "サボン クレイハンドソープ 145ml (鹿児島県産火山灰クレイ×アロエベラ葉エキス配合・汚れを吸着しながらしっとり吸い付くような洗い上がり)"},
            {"rank": 3, "query": "ロクシタン シア リキッドハンドソープ 300ml", "brand": "L'OCCITANE (ロクシタン)", "name": "シア リキッドハンドソープ ヴァーベナ 300ml (高保湿シアバターエキス配合・冬の頻繁な手洗いでも皮脂を奪いすぎず、つっぱり感ゼロの優しい泡立ち)"},
            {"rank": 4, "query": "SABON ハンドウォッシュ パチュリ ラベンダー バニラ", "brand": "SABON (サボン)", "name": "ハンドウォッシュ パチュリ・ラベンダー・バニラ 200ml (海藻エキス×アロエエキス配合・なめらかな泡立ちで手肌をいたわりながら上品な香りが持続)"},
            {"rank": 5, "query": "ミノン 薬用 泡ハンドソープ 250ml", "brand": "MINON (第一三共ヘルスケア)", "name": "ミノン 薬用泡ハンドソープ 250ml [医薬部外品] (植物性アミノ酸系洗浄成分配合・敏感肌の手肌バリアを守りながら殺菌・消毒できる低刺激処方)"},
            {"rank": 6, "query": "MARKS&WEB ハーバルハンドソープ 250ml", "brand": "MARKS&WEB (マークスアンドウェブ)", "name": "ハーバルハンドソープ リフレッシュ 250ml (植物性石けんベース×マンダリン・ラベンダー精油・保湿成分グリセリン配合でキメ細かな泡立ち)"},
            {"rank": 7, "query": "モルトンブラウン オレンジ＆ベルガモット ハンドウォッシュ 300ml", "brand": "MOLTON BROWN (モルトンブラウン)", "name": "オレンジ＆ベルガモット ハンドウォッシュ 300ml (英国王室御用達・セビリア産ビターオレンジオイル配合で手肌を瑞々しく洗い上げる上質ソープ)"},
            {"rank": 8, "query": "BAUM アロマティック ハンドウォッシュ 300ml", "brand": "BAUM (バウム / 資生堂)", "name": "アロマティック ハンドウォッシュ 300ml (樹木由来の保水成分配合・森林浴のような心地よい香りに包まれ、乾燥しがちな手肌をしっとり洗い上げる)"},
            {"rank": 9, "query": "ジョーマローン イングリッシュペアー ハンドウォッシュ 250ml", "brand": "JO MALONE LONDON (ジョー マローン)", "name": "イングリッシュ ぺアー ＆ フリージア ボディ ＆ ハンド ウォッシュ 250ml (メドウフォーム油配合・きめ細やかな泡が肌を優しく洗い上げエレガントに香る)"},
            {"rank": 10, "query": "キュレル 泡ハンドウォッシュ 230ml", "brand": "Curel (花王)", "name": "キュレル 泡ハンドウォッシュ 230ml [医薬部外品] (セラミドを守って洗う弱酸性低刺激処方・ひび割れやあかぎれを防ぎ手荒れを根本から予防)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    for attempt in range(6):
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
                    if not aff_url:
                        aff_url = chosen.get("itemUrl", "")
                    
                    item_name = chosen.get("itemName", query_info["name"])
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "display_name": query_info["name"],
                        "rakuten_name": item_name,
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": chosen.get("shopName", "")
                    }
                else:
                    # 検索語を少し短くして再試行
                    q_words = query.split()
                    if len(q_words) > 1:
                        query = " ".join(q_words[:-1])
                        time.sleep(0.5)
                        continue
        except Exception as e:
            print(f"Error fetching {query} (attempt {attempt+1}): {e}")
            time.sleep(1)
            continue
    return None

def main():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title']})")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": []
        }
        for item_info in cat_data["items"]:
            print(f"Fetching Rank #{item_info['rank']}: {item_info['query']} ...")
            fetched = fetch_item_with_retry(item_info)
            if fetched:
                print(f"  ✓ Found: {fetched['display_name'][:30]}... | Price: ¥{fetched['price']:,} | Shop: {fetched['shop_name']}")
                results[cat_key]["items"].append(fetched)
            else:
                print(f"  ❌ FAILED to fetch: {item_info['query']}")
            time.sleep(0.4)

    with open("fetched_nov_dec_3articles_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n✓ Saved all fetched data to fetched_nov_dec_3articles_data.json")

if __name__ == "__main__":
    main()
