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
    "winter_carbonic_wash": {
        "title": "保湿力の強さで冬の朝の寒冷くすみ・血行不良ゴワつきとさようなら！濃密炭酸ホイップでうるおい血色肌へ導く高保湿炭酸泡洗顔ランク10",
        "page_file": "winter-carbonic-wash.html",
        "items": [
            {"rank": 1, "query": "ソフィーナiP リニュー ムース ウォッシュ", "brand": "SOFINA iP (花王)", "name": "リニュー ムース ウォッシュ 200g (100%マイクロ炭酸泡が毛穴より小さく角層深部まで密着・血流を促進しながら洗い上がりしっとりツヤ肌)"},
            {"rank": 2, "query": "SHIRORU クリスタルホイップ 洗顔料", "brand": "SHIRORU (シロル)", "name": "クリスタルホイップ 120g (高濃度炭酸1,000ppm以上の濃密もっちり泡・コラーゲンやヒアルロン酸など保湿美容成分92.3%配合)"},
            {"rank": 3, "query": "オバジX フレームリフト ムースウォッシュ", "brand": "Obagi (ロート製薬)", "name": "オバジX フレームリフト ムースウォッシュ 150g (濃密炭酸ホイップ×リフトケア発想・大人のゆるみ毛穴や冬の乾燥くすみを一掃してハリ肌へ)"},
            {"rank": 4, "query": "est エスト アクティベート サーキュレーター", "brand": "est (エスト / 花王)", "name": "アクティベート サーキュレーター 170g (炭酸マッサージ洗顔料の名品・冬の冷え切った朝の肌を濃密泡パックで巡らせ血色感と透明感を注入)"},
            {"rank": 5, "query": "ビフェスタ 泡洗顔 コントロールケア", "brand": "Bifesta (マンダム)", "name": "ビフェスタ 泡洗顔 コントロールケア 180g [医薬部外品] (薬用成分×高濃度炭酸泡・冬の乾燥肌荒れや大人ニキビを防ぎキメ細かな透明美肌へ)"},
            {"rank": 6, "query": "ドクターシーラボ VC100 ホットウォッシングフォーム", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "VC100 ホットウォッシングフォーム 120g (じんわり温感×高浸透ビタミンC×濃密炭酸泡・冷え固まった冬の角栓とくすみを温めて優しくオフ)"},
            {"rank": 7, "query": "肌ナチュール ホワイトクリーミーホイップ", "brand": "肌ナチュール (HADA NATURE)", "name": "ホワイトクリーミーホイップ 105g [医薬部外品] (美白有効成分トラネキサム酸×高濃度炭酸泡・洗いながらシミ予防と高保湿うるおいパック)"},
            {"rank": 8, "query": "エリクシール ルフレ バランシング バブル", "brand": "ELIXIR (資生堂)", "name": "エリクシール ルフレ バランシング バブル 168g (ジェルが空気に触れて濃密もこもこ泡に変化・毛穴の奥の皮脂を吸着しながら角層水分をキープ)"},
            {"rank": 9, "query": "クレージュ スパークリングホイップ 洗顔", "brand": "CLAYGE (クレージュ)", "name": "スパークリングホイップ 150g (ナチュラルクレイ×濃密炭酸泡・お風呂上がりの急激な乾燥を防ぐヒアルロン酸・セラミド高配合処方)"},
            {"rank": 10, "query": "Yunth 生ビタミンC 泡洗顔", "brand": "Yunth (ユンス)", "name": "ナノバブル フォームウォッシュ (超微細ナノバブル泡×ピュアビタミンC・冬の朝のくすみ肌を瞬時に明るくほぐす摩擦レス洗顔)"}
        ]
    },
    "winter_control_color": {
        "title": "保湿力の強さで冬の寒さ赤ら顔・血行不良くすみとさようなら！色ムラ補正とうるおい透明感を両立する高保湿コントロールカラーランク10",
        "page_file": "winter-control-color.html",
        "items": [
            {"rank": 1, "query": "ジルスチュアート ルーセントシフォン トーンアップ プライマー", "brand": "JILL STUART (ジルスチュアート)", "name": "ルーセントシフォン トーンアップ プライマー 30g SPF35/PA+++ (みずみずしい美容液タッチで真冬の乾燥を防ぎ、シフォンのような透き通るツヤ肌をキープ)"},
            {"rank": 2, "query": "エレガンス モデリング カラーアップ ベース", "brand": "Elégance (エレガンス)", "name": "モデリング カラーアップ ベース UV / EX 30g (寒暖差赤みや血行不良を自在に補正・肌色を鮮明にリセットして夕方まで崩れない名品)"},
            {"rank": 3, "query": "コスメデコルテ ロージー グロウライザー", "brand": "DECORTÉ (コスメデコルテ)", "name": "ロージー グロウライザー 30ml SPF20/PA++ (血色感ピンク×多彩なパール×高保湿エマルジョン・真冬のどんより顔に生命感あふれるツヤを宿す)"},
            {"rank": 4, "query": "フーミー コントロールカラーベース", "brand": "WHOMEE (フーミー)", "name": "コントロールカラーベースN 15g SPF21/PA++ (イガリシノブ監修・冬の赤ら顔にはイエローやブルー、くすみにはパープルで計算された透明感補正)"},
            {"rank": 5, "query": "RMK ベーシック コントロールカラー N", "brand": "RMK (アールエムケー)", "name": "ベーシック コントロールカラー N 30g SPF10〜15/PA+ (ジェル状のうるおい膜が冬の乾燥肌にしっとり密着・色ムラを消し去り光を透過するピュア肌へ)"},
            {"rank": 6, "query": "ポール＆ジョー ラトゥー エクラ ファンデーション プライマー N", "brand": "PAUL & JOE (ポール＆ジョー)", "name": "ラトゥー エクラ ファンデーション プライマー N 30ml SPF20/PA++ (3種のラベンダーパール×オレンジフラワー水・真冬の黄ぐすみを光で飛ばす発光下地)"},
            {"rank": 7, "query": "セザンヌ UVウルトラフィットベースEX", "brand": "CEZANNE (セザンヌ)", "name": "UVウルトラフィットベースEX 30g (16種の保湿成分配合・高保湿微細パールが冬のカサつき肌にピタッと密着し色ムラを長時間補正)"},
            {"rank": 8, "query": "メディア リュクス カラーコントロールベース", "brand": "media luxe (カネボウ)", "name": "カラーコントロールベース 30g (赤み・くすみを明るく補正・ヒアルロン酸配合でカサつく大人の冬肌をなめらかに整える)"},
            {"rank": 9, "query": "エクセル モチベートユアスキン", "brand": "excel (エクセル)", "name": "モチベートユアスキン 40g SPF48/PA+++ (美容液成分89%配合・ノンケミカル処方でカサつく冬肌を優しくケアしながら素肌をトーンアップ補正)"},
            {"rank": 10, "query": "インテグレート エアフィールメーカー", "brand": "INTEGRATE (資生堂)", "name": "エアフィールメーカー 30g SPF25/PA++ (ラベンダー・ミント・レモンカラー・冬の寒冷赤みやくすみを透け感ヴェールで均一リセット)"}
        ]
    },
    "winter_multi_balm": {
        "title": "保湿力の強さで冬の外出先カサつき・粉吹き乾燥とさようなら！ポーチに1つで顔・唇・毛先・指先まで全身救う高保湿マルチバームランク10",
        "page_file": "winter-multi-balm.html",
        "items": [
            {"rank": 1, "query": "ザ プロダクト ヘアワックス 42g", "brand": "product (ザ・プロダクト)", "name": "ヘアワックス オーガニック マルチバーム 42g (USDA認証オーガニックシアバター配合・髪のスタイリングだけでなく唇・ひじ・指先の乾燥も即効レスキュー)"},
            {"rank": 2, "query": "スチームクリーム 75g", "brand": "STEAMCREAM (スチームクリーム)", "name": "スチームクリーム 75g (高温スチーム製法×オートミールエキス・顔・からだ・手肌・毛先までスーッと浸透する全身用万能保湿クリームバーム)"},
            {"rank": 3, "query": "イハダ 薬用バーム 20g", "brand": "IHADA (イハダ / 資生堂)", "name": "薬用バーム 20g [医薬部外品] (高精製ワセリン配合・冬の寒風による肌荒れ・粉吹き・ひび割れ部分にピタッと密着して水分蒸散を完全ブロック)"},
            {"rank": 4, "query": "エルバビーバ ベビーバター 50g", "brand": "erbaviva (エルバビーバ)", "name": "ベビーバター 50g (USDAオーガニック・ミツロウとシアバターが体温でとろけて赤ちゃんのデリケート肌から大人の目元・指先まで高保湿保護)"},
            {"rank": 5, "query": "KAHI カヒ マルチバーム 9g", "brand": "KAHI (カヒ)", "name": "リンクルバウンズ マルチバーム スティック 9g (韓国発メガヒット・サーモン3重複合成分配合・外出先でもメイクの上から目元・首元・ほうれい線に即時ツヤ注入)"},
            {"rank": 6, "query": "チャントアチャーム バリアバーム", "brand": "chant a charm (チャントアチャーム)", "name": "バリアバーム 20g (100%自然成分・無農薬ハーブエキス×植物性セラミド配合・冬の急激な寒暖差やエアコン乾燥からデリケートな肌を守る)"},
            {"rank": 7, "query": "ドクターブロナー オーガニック マジックバーム", "brand": "Dr. Bronner's (ドクターブロナー)", "name": "オーガニック マジックバーム 57g (アボカド油・ヘンプ油・ホホバ油配合・USDA認証オーガニックで乾燥したひじ・かかと・リップを徹底保湿)"},
            {"rank": 8, "query": "トリロジー エブリシング バーム 45ml", "brand": "trilogy (トリロジー)", "name": "エブリシング バーム 45ml (認定オーガニック・ローズヒップオイルやマルラオイル配合・顔・ボディ・ネイル・ヘアまで全身を柔らかく整える名品)"},
            {"rank": 9, "query": "バジャー クラシック バーム", "brand": "BADGER (バジャー)", "name": "クラシック オーガニック バーム 56g (エキストラバージンオリーブオイル×ミツロウベース・冬の極度のカサつき・あかぎれ手肌をやさしく包み込む)"},
            {"rank": 10, "query": "ヴァセリン オリジナル ピュアスキンジェリー 100g", "brand": "Vaseline (ヴァセリン)", "name": "オリジナル ピュアスキンジェリー 100g (無香料・無着色・防腐剤無添加・150年の歴史を誇る純度100%ワセリンが肌の水分を逃さず保護する万能バーム)"}
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

    with open("fetched_new_3articles_nov_dec_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n✓ Saved all fetched data to fetched_new_3articles_nov_dec_data.json")

if __name__ == "__main__":
    main()
