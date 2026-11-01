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
    "winter_foot_mask": {
        "title": "保湿力の強さで冬のかかとひび割れ・タイツ電線ガサガサとさようなら！履くだけで角質深部まで濃密柔軟ケアする高保湿かかとパック＆保湿ソックスランク10",
        "page_file": "winter-foot-mask.html",
        "items": [
            {"rank": 1, "query": "ベビーフット 浸透補修フットマスク", "brand": "Baby Foot (ベビーフット / リベルタ)", "name": "浸透補修フットマスク 1回分 (削らない高保湿！シアバター＆植物オイル配合でガサガサかかとをしっとり柔軟化)"},
            {"rank": 2, "query": "小林製薬 かかとちゃん M-L グレー", "brand": "かかとちゃん (桐灰 / 小林製薬)", "name": "かかとちゃん M-Lサイズ (履くだけで保湿！チタンアルファ加工特殊ゴムが体温を逃さず水分を閉じ込めるロングセラー)"},
            {"rank": 3, "query": "KOCOSTAR フットモイスチャーパック", "brand": "KOCOSTAR (ココスター)", "name": "フットモイスチャーパック 1回分 (韓国発！シアバター＆アルガンオイル配合の靴下型パックでカサつく足裏を集中補修)"},
            {"rank": 4, "query": "太陽ニット かかとツルツル靴下", "brand": "太陽ニット (たいようニット)", "name": "かかとツルツル靴下 婦人用 (特殊高分子保湿シートをかかとに内蔵！普段履きするだけでガサガサかかとが滑らかに)"},
            {"rank": 5, "query": "ビューティーワールド SB 脱いだらしっとり フットマスク", "brand": "Beauty World (ビューティーワールド)", "name": "脱いだらしっとり フットマスク 1回分 (アルガンオイル＆オリーブ果実油配合！20分履くだけで足裏全体がもっちり)"},
            {"rank": 6, "query": "エビス 潤いフットマスク 12回分", "brand": "EBiS (エビス化粧品)", "name": "うるおいフットマスク 12回分 (美容液350ml贅沢配合！EGFやヒアルロン酸など115種類の美容成分が角質深部へ浸透)"},
            {"rank": 7, "query": "ドクターショール かかと用 保湿ソックス", "brand": "Dr.Scholl (ドクター・ショール)", "name": "かかと用保湿ソックス (オープントゥ設計で寝ている間にムレずに集中ケア！オイルラップ構造で朝まで密着)"},
            {"rank": 8, "query": "山忠 足うら美人 レギュラー", "brand": "足うら美人 (山忠)", "name": "足うら美人 レギュラー丈 (新潟の老舗ニット工場直製！二重編み特殊保湿シートでクリームいらずのツルツルかかとへ)"},
            {"rank": 9, "query": "ラッキートレンディ フットエッセンスマスク", "brand": "Lucky Trendy (ラッキーウィンク)", "name": "フットエッセンスマスク 1回分 (尿素＆植物エキス配合！冬の硬くなった古い角質を柔らかくほぐし潤いチャージ)"},
            {"rank": 10, "query": "シルク かかと 保湿 ソックス", "brand": "絹屋 (きぬや)", "name": "極上天然シルク かかと保湿ケアソックス (天然シルク100%の優しい肌触り！就寝中に通気性を保ちながらかかとを集中保湿)"}
        ]
    },
    "winter_eye_patch": {
        "title": "保湿力の強さで冬の目元ちりめんジワ・乾燥クマとさようなら！ぷるぷる高密着ハイドロゲルが角層深部を潤す高保湿アイパッチランク10",
        "page_file": "winter-eye-patch.html",
        "items": [
            {"rank": 1, "query": "プチフェ ゴールド ハイドロゲル アイパッチ 60枚", "brand": "PETITFEE (プチフェ)", "name": "ブラックパール＆ゴールド ハイドロゲル アイパッチ 60枚入 (世界各国で大ヒット！純金＆黒真珠エキス配合で冬の乾燥目元にハリツヤ注入)"},
            {"rank": 2, "query": "ミシャ ビタC プラス ハイドロゲル アイパッチ 60枚", "brand": "MISSHA (ミシャ)", "name": "ビタC プラス ハイドロゲル アイパッチ 60枚入 (高純度ビタミンC×コラーゲン配合！目元のくすみ・乾燥小ジワをぷるぷる密着ケア)"},
            {"rank": 3, "query": "ヘイミッシュ ローズ ハイドロゲル アイパッチ 60枚", "brand": "Heimish (ヘイミッシュ)", "name": "ブルガリアンローズウォーター ハイドロゲル アイパッチ 60枚入 (優雅なダマスクローズの香りと濃厚美容液ゲルが乾燥目元をしっとり整える)"},
            {"rank": 4, "query": "クリアターン 肌ふっくら アイゾーンマスク 32回分", "brand": "CLEAR TURN (クリアターン / コーセー)", "name": "肌ふっくら アイゾーンマスク 32回分 64枚入 (レチノール誘導体×ヒアルロン酸配合！目元・口元の乾燥小ジワを目立たなくするデイリーパック)"},
            {"rank": 5, "query": "JMsolution アイパッチ 60枚", "brand": "JMsolution (ジェイエムソリューション)", "name": "マリンルミナス パール ディープモイスチャー アイパッチ 60枚入 (海洋深層水とパールエキス配合！疲れた目元を冷却保湿し引き締める)"},
            {"rank": 6, "query": "グーダル 青みかん ビタC ハイドロゲル アイパッチ", "brand": "goodal (グーダル / CLIO)", "name": "青みかん ビタC 水分ハイドロゲル アイパッチ 60枚入 (ビタミンC誘導体とヒアルロン酸を閉じ込めたぷるぷるシート！5分で集中うるおいチャージ)"},
            {"rank": 7, "query": "ピュアスマイル チューシー アイパッチ", "brand": "CHOOSY (チューシー / サン・スマイル)", "name": "ハイドロゲル アイパッチ 2枚入 (ぷるぷるゲルが目元に吸い付くように密着！コラーゲン＆植物エキスが冬の乾燥ダメージを集中リペア)"},
            {"rank": 8, "query": "ドクタージャルト クライオラバー マスク", "brand": "Dr.Jart+ (ドクタージャルト)", "name": "クライオラバー モイスチャライジング マスク (高密着アンプル×冷却ラバーシート！美容液を急速浸透させて冬の砂漠肌をリセット)"},
            {"rank": 9, "query": "ネイチャーリパブリック スネイル ハイドロゲル アイパッチ", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "スネール ソリューション ハイドロゲル アイパッチ 60枚入 (高純度カタツムリ粘液濾過物配合！冬の乾燥による目元のたるみ・シワをふっくら補修)"},
            {"rank": 10, "query": "エチュードハウス コラーゲン アイパッチ", "brand": "ETUDE (エチュード)", "name": "モイストフルCL アイパッチ 2枚入 (スーパーコラーゲンウォーター配合！密着ゲルが冬の乾燥でしぼんだ目元に弾力と潤いを与える)"}
        ]
    },
    "winter_nail_serum": {
        "title": "保湿力の強さで冬の爪割れ・二枚爪・ガサガサ縦ジワとさようなら！浸透ケラチンと高保湿成分で強くしなやかな美爪を育てる高保湿ネイル補修美容液ランク10",
        "page_file": "winter-nail-serum.html",
        "items": [
            {"rank": 1, "query": "ドクターネイル ディープセラム 3.3ml", "brand": "Dr.Nail (ドクターネイル / 興和)", "name": "ディープセラム 3.3ml (製薬会社が開発！水溶性浸透補修成分ジメチルスルホン配合で薄い爪・割れ爪の内部まで直接ケラチン補強)"},
            {"rank": 2, "query": "メンソレータム ハンドベール リッチネイル爪補強コート", "brand": "メンソレータム (ロート製薬)", "name": "ハンドベール リッチネイル 爪補強コート 10ml (補強ファイバーと加水分解ケラチン配合！無色マットで塗った瞬間爪を物理的＆成分的に保護)"},
            {"rank": 3, "query": "エテュセ クイックケアセラム", "brand": "ettusais (エテュセ)", "name": "クイックケアセラム 9ml (ホホバ油・マカデミアナッツ油配合！リムーバー不要でツヤを与えながら冬の乾燥爪を集中トリートメント)"},
            {"rank": 4, "query": "OPI プロスパ ネイル キューティクルオイル トゥゴー 7.5ml", "brand": "O・P・I (オーピーアイ)", "name": "プロスパ ネイル＆キューティクルオイル トゥーゴー 7.5ml (サロン仕様のクプアスバター＆ホワイトティエキス配合！持ち歩きやすいジェル状ペンタイプ)"},
            {"rank": 5, "query": "スパルーチェ 爪美容液プラス 10ml", "brand": "SpaLuce (スパルーチェ)", "name": "爪美容液プラス 10ml (高浸透ケラチン×フッ素配合！爪の内部浸透と表面バリアを同時に叶えるネイルサロン専売品質)"},
            {"rank": 6, "query": "LCN アンティセプト 16ml", "brand": "LCN (エルシーエヌ)", "name": "アンティセプト 16ml (ドイツの老舗ネイルケア！爪とハイポニキウムを清潔に保ちながら健やかなピンクの美爪を育成)"},
            {"rank": 7, "query": "カントリー＆ストリーム ネイルトリートメントオイル 7g", "brand": "Country & Stream (カントリー＆ストリーム)", "name": "ネイルトリートメントオイル 7g (ハチミツ＆オーガニックオイル配合！チューブタイプで外出先でもサッと指先のひび割れ・乾燥をケア)"},
            {"rank": 8, "query": "デュカート ネイルリペアセラム", "brand": "Ducato (デュカート / シャンティ)", "name": "ネイルリペアセラム (パンテノール＆加水分解シルク配合！水溶性でベタつかずスマホやパソコン作業中もすぐに使える爪の美容液)"},
            {"rank": 9, "query": "アディクション ザ ネイルポリッシュ 001C セラム", "brand": "ADDICTION (アディクション)", "name": "ザ ネイル オイル 10ml (ローズヒップオイルやオーガニックシアバター配合！極上の香りと浸透感で爪と指先を潤すデパコス名品)"},
            {"rank": 10, "query": "無印良品 ネイルケアオイル 3.2g", "brand": "無印良品 (MUJI)", "name": "ネイルケアオイル 3.2g (カミツレ花エキス・ホホバ種子油配合！筆ペンタイプで使いやすく無香料・無鉱物油の低刺激処方)"}
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
                    affiliate_url = chosen.get("affiliateUrl", "")
                    item_url = chosen.get("itemUrl", "")
                    final_url = affiliate_url if affiliate_url else item_url
                    
                    return {
                        "rank": query_info["rank"],
                        "name": query_info["name"],
                        "brand": query_info["brand"],
                        "rakuten_name": chosen.get("itemName", query_info["name"]),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": final_url,
                        "shop_name": chosen.get("shopName", "楽天市場正規取扱店"),
                        "review_count": chosen.get("reviewCount", 0),
                        "review_average": chosen.get("reviewAverage", 0.0),
                        "item_caption": chosen.get("itemCaption", "")[:120]
                    }
                else:
                    print(f"Warning: No items returned for '{query}', trying simplified query...")
                    simplified = query.split()[0]
                    if simplified != query and len(simplified) >= 2:
                        query = simplified
                        continue
        except Exception as e:
            print(f"Attempt {attempt+1} failed for '{query}': {e}")
            time.sleep(1.5)
    
    print(f"Failed to fetch for '{raw_q}'")
    return None

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching for Category: {cat_key} ({cat_data['title'][:35]}...)")
    print(f"==========================================")
    cat_items = []
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['query']} ...")
        res = fetch_item_with_retry(item_info)
        if res:
            cat_items.append(res)
            print(f"  ✓ Found: {res['rakuten_name'][:40]} | ¥{res['price']:,} | Image: {res['image_url'][:50]}...")
        else:
            print(f"  ❌ FAILED for {item_info['query']}")
        time.sleep(0.5)
    
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

output_file = "fetched_3nov_dec_foot_eye_nail_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone! Saved all fetched data to {output_file}")
