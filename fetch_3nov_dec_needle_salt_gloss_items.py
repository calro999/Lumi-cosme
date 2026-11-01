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
    "winter_needle_patch": {
        "title": "保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10",
        "page_file": "winter-needle-patch.html",
        "items": [
            {"rank": 1, "query": "北の快適工房 ヒアロディープパッチ", "brand": "北の快適工房 (Jコンテンツ)", "name": "ヒアロディープパッチ 8枚入り (ギネス世界記録認定！ヒアルロン酸微細針が寝ている間に溶け出し目元・ほうれい線の乾燥小ジワを集中注入ケア)"},
            {"rank": 2, "query": "資生堂 ナビジョン HA フィルパッチ", "brand": "NAVISION (ナビジョン / 資生堂)", "name": "HA フィルパッチ B 2枚×3包 (資生堂の美容医療発想！1回分約2,400本の100%ヒアルロン酸マイクロニードルが角層深部に潤いをダイレクト密着注入)"},
            {"rank": 3, "query": "クオニス ダーマフィラー プレミア", "brand": "Quanis (クオニス / コスメディ製薬)", "name": "ダーマフィラー プレミア 4回分 (マイクロニードル技術のパイオニア製薬会社が開発！立体形状ヒアルロン酸針とレチノール配合で極上のハリ弾力)"},
            {"rank": 4, "query": "VT リードルS マイクロパッチ", "brand": "VT COSMETICS (ブイティー)", "name": "リードルS マイクロパッチ 1箱 (大人気リードルショット発想！CICA成分とヒアルロン酸ニードルが冬の乾燥ゆらぎ・気になるスポットを角層から徹底ケア)"},
            {"rank": 5, "query": "クリアターン ヒアロチューン マイクロパッチ", "brand": "CLEAR TURN (クリアターン / コーセー)", "name": "ヒアロチューン マイクロパッチ 1回分 (1500本のヒアルロン酸針！ドラッグストアで気軽に買える高コスパ本格マイクロパッチで翌朝ふっくら)"},
            {"rank": 6, "query": "ドクターフィル IC.U HA マイクロパッチ", "brand": "Dr.PHIL COSMETICS (ドクターフィル / コーセー)", "name": "IC.U HA マイクロパッチ EX 2枚入 (皮膚科学発想のドクターズコスメ！高密度ヒアルロン酸ニードルが冬の乾燥によるたるみ・刻まれジワを押し広げる)"},
            {"rank": 7, "query": "メディオン スパオキシ ニードルパッチ", "brand": "Dr.MEDION (ドクターメディオン)", "name": "スパオキシ ニードルパッチ (炭酸美容のパイオニアが放つ集中パッチ！ヒアルロン酸と複合ペプチド針が目元・口元をピンと引き締める)"},
            {"rank": 8, "query": "ザキュア マイクロアイパッチ", "brand": "THE CURE (ザ・キュア)", "name": "マイクロアイパッチ 1回分 (韓国発の実力派ニードルパッチ！加水分解ヒアルロン酸とマデカッソシド配合で真冬の乾燥目元をぷるぷるに)"},
            {"rank": 9, "query": "アクロパス スマイリーパッチ", "brand": "ACROPASS (アクロパス)", "name": "エイジレスリフター スマイリーパッチ 4回分 (独自特許マイクロ構造体技術！ヒアルロン酸とEGFがほうれい線ゾーンへダイレクトに届く実力派)"},
            {"rank": 10, "query": "パッチエム マイクロニードル アイパッチ", "brand": "Patch M (パッチエム)", "name": "マイクロアイパッチ 5回分セット (高分子ヒアルロン酸×コラーゲン配合のマイクロニードルがお手頃価格で毎日続けられる高コスパパッチ)"}
        ]
    },
    "winter_bath_salt": {
        "title": "保湿力の強さで冬の冷え性・全身カサつき乾燥とさようなら！マグネシウム＆ミネラル温浴で湯上がりしっとり極上肌へ導く高保湿バスソルトランク10",
        "page_file": "winter-bath-salt.html",
        "items": [
            {"rank": 1, "query": "シークリスタルス エプソムソルト オリジナル", "brand": "Sea Crystals (シークリスタルス)", "name": "国産 エプソムソルト オリジナル 2.2kg (純度99%以上硫酸マグネシウム配合・真冬の冷えた体を芯から温め全身の粉吹き乾燥を防ぐ大ベストセラー)"},
            {"rank": 2, "query": "クナイプ バスソルト ホップ バレリアン", "brand": "Kneipp (クナイプ)", "name": "バスソルト グーテナハト ホップ＆バレリアンの香り 850g (ドイツ古代海水から精製された天然岩塩×植物精油・冬の不眠と肌乾燥をダブルで癒やす名作)"},
            {"rank": 3, "query": "NEHAN TOKYO エプソルト", "brand": "NEHAN TOKYO (ネハントウキョウ)", "name": "エプソルト (epsalt) 800g (創業420年の徳島県馬居化成が誇る最高純度99.99%硫酸マグネシウム・シルクのような極上湯上がり肌へ導くラグジュアリーソルト)"},
            {"rank": 4, "query": "MARKS&WEB ハーバルバスソルト マンダリン", "brand": "MARKS&WEB (マークスアンドウェブ)", "name": "ハーバルバスソルト マンダリン/ラベンダー 240g (天日塩×天然精油・ミネラルが肌を引き締めながらフルーティーな香りで冬のバスタイムを満たす)"},
            {"rank": 5, "query": "SABON バスソルト デッドシー", "brand": "SABON (サボン)", "name": "バスソルト ローズ 350g (死海の塩100%配合・ミネラルが凝縮された天然塩とエッセンシャルオイルで湯上がりの肌がしっとり柔らかく吸い付く)"},
            {"rank": 6, "query": "BARAKA ジョルダニアン デッドシーソルト", "brand": "BARAKA (バラカ)", "name": "ジョルダニアン デッドシーソルト 500g (ヨルダン死海最深層から採取された無添加天然ソルト・マグネシウム含有率が驚異的で極寒の冷えを解消)"},
            {"rank": 7, "query": "SHIRO バスソルト ホワイトリリー", "brand": "SHIRO (シロ)", "name": "ホワイトリリー バスソルト 400g (オホーツク海産の自然塩に上品なホワイトリリーの香りをプラス・ミネラル豊富な湯で肌をしっとり保湿)"},
            {"rank": 8, "query": "アユーラ メディテーションバスソルト", "brand": "AYURA (アユーラ)", "name": "メディテーションバスソルト 300g (海塩×アユーラ独自の安らぎ森林香・冬の張り詰めた気分をほぐし湯冷めを防いで潤いヴェールをキープ)"},
            {"rank": 9, "query": "ヒマラヤ岩塩 ルビーソルト 入浴用", "brand": "天然ヒマラヤ岩塩", "name": "ヒマラヤ岩塩 ルビーソルト 入浴用 1kg (太古の地殻変動が生んだミネラル＆硫黄高含有の赤い岩塩・まるで天然温泉のような発汗温浴と保湿力)"},
            {"rank": 10, "query": "クナイプ バスソルト サンダルウッド", "brand": "Kneipp (クナイプ)", "name": "バスソルト サンダルウッドの香り 850g (深みのあるオリエンタルウッディの温感アロマ×天然岩塩・冬の乾燥肌をなめらかに包み込む大人の名品)"}
        ]
    },
    "winter_lip_gloss": {
        "title": "保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10",
        "page_file": "winter-lip-gloss.html",
        "items": [
            {"rank": 1, "query": "ディオール アディクト リップ マキシマイザー", "brand": "DIOR (ディオール)", "name": "ディオール アディクト リップ マキシマイザー (ヒアルロン酸×チェリーオイル配合・唇を瞬時にふっくらプランプアップさせ24時間潤いが続く世界的金字塔)"},
            {"rank": 2, "query": "クラランス リップコンフォート リップパーフェクター", "brand": "CLARINS (クラランス)", "name": "リップコンフォート リップパーフェクター (ヘーゼルナッツ・ホホバオイル等99%スキンケア成分！濃密な植物オイルヴェールが冬の唇をしっとり包む)"},
            {"rank": 3, "query": "ジルスチュアート クリスタルブルーム リップブーケ セラム", "brand": "JILL STUART (ジルスチュアート)", "name": "クリスタルブルーム リップブーケ セラム (花蜜のような濃密ツヤとうるおい・心地よい温感＆清涼感プランプでホリデーの唇を最高峰に美しく演出)"},
            {"rank": 4, "query": "シャネル ルージュ ココ グロス", "brand": "CHANEL (シャネル)", "name": "ルージュ ココ グロス (ホホバ・ヒマワリ・ミモザの天然ワックス配合・ベタつかず極上の水光ツヤと高い保湿持続力を叶える名品リップグロス)"},
            {"rank": 5, "query": "ロムアンド グラスティング ウォーター グロス", "brand": "rom&nd (ロムアンド)", "name": "グラスティング ウォーター グロス (微細ラメが水滴のようにキラキラ輝く！スイートアーモンドオイル配合で唇を乾燥から守る水光ガラス膜グロス)"},
            {"rank": 6, "query": "キャンメイク プランプリップケアスクラブ グロス", "brand": "CANMAKE (キャンメイク)", "name": "ボリューミーリップグロス (カプサイシン誘導体＆ヒアルロン酸配合・プチプラの常識を覆すぷっくり厚みツヤ膜で冬の乾燥唇をボリュームアップ)"},
            {"rank": 7, "query": "RMK リップジェリーグロス", "brand": "RMK (アールエムケー)", "name": "リップジェリーグロス (みずみずしい濃密ジェルが唇にピタッとフィット・透明感あふれる濡れたような立体ツヤが長時間持続するロングセラー)"},
            {"rank": 8, "query": "SUQQU トリートメント ラッピング リップ", "brand": "SUQQU (スック)", "name": "トリートメント ラッピング リップ (ワックスと美容オイルの黄金ブレンドが唇を密封ラッピング・素の唇を底上げする洗練された大人の潤いツヤ)"},
            {"rank": 9, "query": "エトヴォス ミネラルリッププランパー シアー", "brand": "ETVOS (エトヴォス)", "name": "ミネラルリッププランパー シアー (植物由来オイル×アミノ酸誘導体配合・界面活性剤やタール色素フリーで敏感な冬の唇もぷっくり潤すミネラルグロス)"},
            {"rank": 10, "query": "ボビイ ブラウン エクストラ プランプ リップ セラム", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "エクストラ プランプ リップ セラム (ボタニカルオイル8種を贅沢ブレンド・冬の唇の縦ジワを瞬時にぼかしふっくら立体的なハリを与えるリッチグロス)"}
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
            time.sleep(0.3)

    output_file = "fetched_3nov_dec_needle_salt_gloss_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Saved all fetched data to {output_file}")

if __name__ == "__main__":
    main()
