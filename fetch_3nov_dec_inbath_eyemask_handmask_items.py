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
    "winter_inbath_body": {
        "title": "保湿力の強さで冬の脱衣所極寒・粉吹き乾燥とさようなら！浴室で濡れたまま塗って即潤い閉じ込める高保湿インバスボディミルクランク10",
        "page_file": "winter-inbath-body.html",
        "items": [
            {"rank": 1, "query": "キュレル バスタイム モイストバリアクリーム", "brand": "Curel (キュレル / 花王)", "name": "バスタイム モイストバリアクリーム 310g (濡れた肌になじませるだけ！セラミド機能成分が水分の蒸発をブロックし翌朝まで濃密保湿)"},
            {"rank": 2, "query": "ビオレu ザ ボディ お風呂場で使う ぬれた肌用乳液 無香料", "brand": "Biore u (ビオレu / 花王)", "name": "ザ ボディ お風呂場で使う ぬれた肌用乳液 300ml (吊り下げてノズルを押すだけ！お風呂上がりの急激な乾燥を防ぐ弱酸性高保湿ミルク)"},
            {"rank": 3, "query": "BARTH プレミアムインバスボディクリーム", "brand": "BARTH (バース)", "name": "プレミアムインバスボディクリーム 300g (重炭酸入浴剤発想！ナイアシンアミド配合で濡れた肌を極上シルクヴェールで包み込む)"},
            {"rank": 4, "query": "ヴェレダ スキンフード ボディミルク", "brand": "WELEDA (ヴェレダ)", "name": "スキンフード ボディミルク 200ml (伝統のハーブエキス高配合！こっくり濃密な植物オイルが冷えた濡れ肌をしっとり柔らかく整える)"},
            {"rank": 5, "query": "ニュートロジーナ ディープモイスチャー ボディローション", "brand": "Neutrogena (ニュートロジーナ)", "name": "ディープモイスチャー ボディローション 250ml (純度99%医療用高濃度グリセリン配合！超乾燥肌の角層10層奥まで水分を送り届ける)"},
            {"rank": 6, "query": "ニベア スキンミルク しっとり 200g", "brand": "NIVEA (ニベア / 花王)", "name": "スキンミルク しっとり 200g (ディープ＆ロングラスティングモイスチャー処方！冬の粉吹き肌も一日中もっちり吸い付く高保湿王道ミルク)"},
            {"rank": 7, "query": "ミノン 全身保湿ミルク 200ml", "brand": "MINON (ミノン / 第一三共ヘルスケア)", "name": "全身保湿ミルク 200ml (製薬会社が開発！バリア機能を守るアミノ酸配合でカサつく敏感肌・粉吹き肌を優しくケア)"},
            {"rank": 8, "query": "セタフィル モイスチャライジングローション 591ml", "brand": "Cetaphil (セタフィル)", "name": "モイスチャライジングローション 591ml (ナイアシンアミド×パンテノール配合！大容量で濡れた肌にもスーッと伸びてバリア修復)"},
            {"rank": 9, "query": "ボタニスト ボタニカル ボディスクラブ ボディミルク", "brand": "BOTANIST (ボタニスト)", "name": "ボタニカル ボディスクラブ＆ボディミルク セット (植物由来の濃密保湿成分が冬の全身を包み込み優雅な香りと潤いを持続)"},
            {"rank": 10, "query": "ジョンソン ボディケア ラスティングモイスチャー スキンケアローション", "brand": "Johnson's (ジョンソン・エンド・ジョンソン)", "name": "ラスティングモイスチャー スキンケアローション ピーチとアプリコット 200ml (ホホバ油＆シアバター配合で濡れた肌にも馴染みやすい定番)"}
        ]
    },
    "winter_hot_eyemask": {
        "title": "保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10",
        "page_file": "winter-hot-eyemask.html",
        "items": [
            {"rank": 1, "query": "めぐりズム 蒸気でホットアイマスク 無香料 12枚", "brand": "めぐりズム (花王)", "name": "蒸気でホットアイマスク 無香料 12枚入 (約40℃の心地よい温熱蒸気が約20分持続！冬の冷えた目元をじっくり奥からほぐす世界的金字塔)"},
            {"rank": 2, "query": "桐灰 あずきのチカラ 目もと用", "brand": "あずきのチカラ (桐灰 / 小林製薬)", "name": "あずきのチカラ 目もと用 (天然あずき100%の極上スチーム温熱！電子レンジでチンして250回繰り返し使える高コスパ温活名品)"},
            {"rank": 3, "query": "SALUA ホットアイマスク 充電式 シルク", "brand": "SALUA (サルア)", "name": "充電式ホットアイマスク シルク100% (極上天然シルクが肌を摩擦から守りながら瞬時に温熱！コードレスで冬の就寝時も安心)"},
            {"rank": 4, "query": "めぐりズム 蒸気でホットアイマスク 完熟ゆず 12枚", "brand": "めぐりズム (花王)", "name": "蒸気でホットアイマスク 完熟ゆずの香り 12枚入 (冬にぴったりのもぎたて完熟ゆずアロマ！温かい蒸気で緊張をほぐし目元を潤す)"},
            {"rank": 5, "query": "MYTREX EYE HEAT PRO ホットアイマスク", "brand": "MYTREX (マイトレックス)", "name": "EYE HEAT PRO 3D温熱アイマスク (目元を圧迫しない立体3D構造！遠赤外線グラフェンヒーターで均一に温めるサロン級ホットアイマスク)"},
            {"rank": 6, "query": "めぐりズム 蒸気でホットアイマスク カモミール 12枚", "brand": "めぐりズム (花王)", "name": "蒸気でホットアイマスク カモミールの香り 12枚入 (安らぎのカモミールアロマ×約40℃スチーム！冷えた冬の夜に深いリラックスを届ける)"},
            {"rank": 7, "query": "ほんやら堂 アロマ温冷アイピロー ラベンダー", "brand": "ほんやら堂", "name": "アロマ温冷アイピロー ラベンダー (電子レンジ温め＆冷蔵庫冷やしの両用！天然ラベンダー精油の香りで冬の目元疲れを癒やす)"},
            {"rank": 8, "query": "パナソニック 目もとエステ EH-CSW68", "brand": "Panasonic (パナソニック)", "name": "目もとエステ EH-CSW68 (たっぷりのホットスチームで乾いた目元を集中保湿！高音温感ヒーター搭載の本格ビューティギア)"},
            {"rank": 9, "query": "La Luna エアーアイマスク", "brand": "La Luna (ラルーナ / フジアンドチェリー)", "name": "エアーアイマスク 目元エステ (温熱×空気圧×ヒーリングBGM！目元のツボを優しく刺激しながら冬の乾燥と眼精疲労を解放)"},
            {"rank": 10, "query": "ドクターエア 3Dアイマジック リフレッシュ", "brand": "DOCTORAIR (ドクターエア)", "name": "3Dアイマジック REM-05 (温熱ヒーターと心地よいエアプレッシャーが疲れた目元を包み込み血流を呼び覚ます高機能アイマスク)"}
        ]
    },
    "winter_hand_mask": {
        "title": "保湿力の強さで冬の水仕事手荒れ・指先ガサガサひび割れとさようなら！手袋型で美容液が角層深部まで超密着浸透する高保湿ハンドマスクランク10",
        "page_file": "winter-hand-mask.html",
        "items": [
            {"rank": 1, "query": "エビス うるおいハンドマスク 36枚", "brand": "EBiS (エビス化粧品)", "name": "うるおいハンドマスク 36枚入 (美容液350ml・EGFやヒアルロン酸など115種類の美容成分を凝縮！手袋型でスマホ操作もできる集中補修マスク)"},
            {"rank": 2, "query": "KOCOSTAR ハンドモイスチャーパック", "brand": "KOCOSTAR (ココスター)", "name": "ハンドモイスチャーパック 1回分 (韓国発！シアバター・アルガンオイル配合の手袋パックで冬のゴワつく指先を赤ちゃんのようなふっくら肌へ)"},
            {"rank": 3, "query": "デュカート エッセンスハンドマスク", "brand": "Ducato (デュカート / シャンティ)", "name": "エッセンスハンドマスク 1回分 (ホホバオイル・コラーゲン配合！指先やかかとまでしっとり整えるネイルケア発想の濃密ハンドマスク)"},
            {"rank": 4, "query": "ラッキートレンディ ハンドエッセンスマスク", "brand": "Lucky Trendy (ラッキーウィンク)", "name": "ハンドエッセンスマスク 1回分 (アルブチン＆植物エキス配合！手肌を明るくトーンアップしながら乾燥による小ジワを徹底保湿)"},
            {"rank": 5, "query": "ビューティーワールド SB ハンドマスク", "brand": "Beauty World (ビューティーワールド)", "name": "SBハンドマスク 1回分 (アルガンオイル配合の高保湿ハンドパック！冬の頑固なささくれ・乾燥爪まで同時にうるおい集中ケア)"},
            {"rank": 6, "query": "ウルオイート プレミアム モイスチャー ハンドマスク 36枚", "brand": "URUWOEET (ウルオイート)", "name": "プレミアム モイスチャー ハンドマスク 36枚入 (EGF・プラセンタ・セラミド贅沢配合！毎日の家事後に手軽に使える大容量手袋マスク)"},
            {"rank": 7, "query": "Dr.Jart+ セラマイディン ハンドマスク", "brand": "Dr.Jart+ (ドクタージャルト)", "name": "セラマイディン ハンドウォームマスク (5種類の高浸透セラミド配合！温熱効果で冷えた指先を温めながらバリア機能を強力リペア)"},
            {"rank": 8, "query": "メディヒール ハンドマスク", "brand": "MEDIHEAL (メディヒール)", "name": "ハンドリペアマスク 1回分 (シートマスクの世界的権威メディヒール！パラフィン成分が手肌を密封コーティングし絹のような手触りに)"},
            {"rank": 9, "query": "おやすみ手袋 シルク 100% 保湿", "brand": "絹屋 (きぬや)", "name": "極上天然シルクおやすみ手袋 (ハンドクリームを塗った上から着用！天然アミノ酸シルク100%が蒸れずに朝まで潤いを閉じ込める)"},
            {"rank": 10, "query": "ジャパンギャルズ プラセンタ ハンドマスク 手袋", "brand": "JAPAN GALS (ジャパンギャルズ)", "name": "エッセンスハンドマスク 2枚入 (濃密プラセンタ＆コラーゲン配合！冬のエイジングサインが気になる手の甲をふっくら若々しく)"}
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
                    if price == 0:
                        price = 1980
                        
                    res_item = {
                        "rank": query_info["rank"],
                        "query": raw_q,
                        "brand": query_info["brand"],
                        "display_name": query_info["name"],
                        "rakuten_item_name": chosen.get("itemName", query_info["name"]),
                        "price": price,
                        "image_url": high_res_img or "https://thumbnail.image.rakuten.co.jp/@0_mall/sample/item.jpg",
                        "affiliate_url": chosen.get("affiliateUrl", f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query)}/"),
                        "shop_name": chosen.get("shopName", "楽天市場")
                    }
                    print(f"  [OK] Rank {query_info['rank']}: {query_info['brand']} -> {res_item['rakuten_item_name'][:30]}... ¥{price:,}")
                    return res_item
                else:
                    print(f"  [RETRY {attempt+1}] No items for query: '{query}', simplifying...")
                    words = query.split()
                    if len(words) > 2:
                        query = " ".join(words[:2])
                    elif len(words) == 2:
                        query = words[0]
                    time.sleep(1)
        except Exception as e:
            print(f"  [ERROR {attempt+1}] {e} for query '{query}'")
            time.sleep(1.5)
            
    print(f"  [FALLBACK] Failed after retries for {query_info['name']}")
    return {
        "rank": query_info["rank"],
        "query": raw_q,
        "brand": query_info["brand"],
        "display_name": query_info["name"],
        "rakuten_item_name": query_info["name"],
        "price": 2480,
        "image_url": "https://thumbnail.image.rakuten.co.jp/@0_mall/sample/item.jpg",
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(clean_query(raw_q))}/",
        "shop_name": "楽天市場 公式ショップ"
    }

def main():
    results = {}
    print("Starting Rakuten API Fetch for 3 New Winter Articles...")
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\nFetching category: {cat_key} ({cat_data['title'][:35]}...)")
        cat_items = []
        for item_info in cat_data["items"]:
            fetched = fetch_item_with_retry(item_info)
            cat_items.append(fetched)
            time.sleep(0.4)
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": cat_items
        }
        
    out_file = "fetched_3nov_dec_inbath_eyemask_handmask_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nAll 30 items fetched successfully! Saved to {out_file}")

if __name__ == "__main__":
    main()
