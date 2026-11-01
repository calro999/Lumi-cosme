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
    "winter_morning_mask": {
        "title": "保湿力の強さで冬の朝の冷水洗顔・乾燥砂漠肌とさようなら！60秒貼るだけで洗顔から下地まで満たす朝用高保湿時短シートマスクランク10",
        "page_file": "winter-morning-mask.html",
        "items": [
            {"rank": 1, "query": "サボリーノ 目ざまシート 完熟果実", "brand": "Saborino (サボリーノ / BCL)", "name": "目ざまシート 完熟果実の高保湿タイプ 28枚入り (洗顔・スキンケア・保湿下地が60秒で完了！ざくろ＆ベリーエキスで真冬の肌を贅沢保湿)"},
            {"rank": 2, "query": "クオリティファースト オールインワンシートマスク ザ・ベスト", "brand": "QUALITY 1st (クオリティファースト)", "name": "オールインワンシートマスク ザ・ベストEX 20枚入り (多層構造高密着シート×生コラーゲン・酵母エキス・濃密セラミドで朝の肌を劇的格上げ)"},
            {"rank": 3, "query": "ルルルン プレシャス RED モイスト", "brand": "LuLuLun (ルルルン)", "name": "ルルルン プレシャス RED (モイスト) 32枚入り (お米由来の濃密保湿エキス×L22オイル・冬のゴワつく大人の朝肌をふっくらほぐす)"},
            {"rank": 4, "query": "VT CICA デイリースージングマスク", "brand": "VT COSMETICS (ブイティー)", "name": "CICA デイリースージングマスク 30枚入り (シカヒアルロン×0.2mm極薄密着シート・冬の暖房寒暖差によるゆらぎ赤みを朝から素早く鎮静)"},
            {"rank": 5, "query": "クリアターン ごめんね素肌 キープマスク", "brand": "CLEAR TURN (クリアターン / コーセー)", "name": "ごめんね素肌 キープマスク 7枚入り (睡眠不足や冬の乾燥でボロボロになった肌を朝の集中ケアで速攻リセット・敏感肌対応)"},
            {"rank": 6, "query": "ダーマレーザー スーパーAZ100 マスク", "brand": "クオリティファースト (QUALITY 1st)", "name": "ダーマレーザー スーパーAZ100 マスク 7枚入り (アゼライン酸高濃度配合×高密着シート・冬の乾燥毛穴や大人肌荒れをキュッと引き締め)"},
            {"rank": 7, "query": "ネイチャーリパブリック ビタペアC デイリーシートマスク", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "ビタペアC デイリーシートマスク 30枚入り (済州島グリーンレモンエキス×ビタミンC誘導体・朝のどんより寒冷くすみをパッと明るく)"},
            {"rank": 8, "query": "アンレーベル ラボ V エッセンス シートマスク", "brand": "unlabel LAB (アンレーベル ラボ)", "name": "V エッセンス シートマスク 7枚入り (超高圧浸透型ビタミンC誘導体配合・毛穴の開きやキメの乱れに朝のダイレクト注入ケア)"},
            {"rank": 9, "query": "メディヒール 3ミニッツマスク", "brand": "MEDIHEAL (メディヒール)", "name": "THE N.M.F 3ミニッツマスク 7枚入り (朝のわずか3分で角層深部まで水分爆弾チャージ・真冬でも一日中メイクが乾かない)"},
            {"rank": 10, "query": "ナンバーズイン 3番 シートマスク", "brand": "numbuzin (ナンバーズイン)", "name": "3番 すべすべキメケアシートマスク 4枚入り (発酵成分×毛穴収縮成分・冬の開いた乾燥毛穴をなめらかに整えメイクのりを極限まで高める)"}
        ]
    },
    "winter_gel_wash": {
        "title": "保湿力の強さで冬の朝の泡立て冷え・毛穴角栓ゴワつきとさようなら！うるおい残して透明感を呼び覚ます高保湿マッサージジェル洗顔ランク10",
        "page_file": "winter-gel-wash.html",
        "items": [
            {"rank": 1, "query": "エスト クラリファイイング ジェル ウォッシュ", "brand": "est (エスト / 花王)", "name": "クラリファイイング ジェル ウォッシュ 130g (CPコンプレックス配合・角栓を崩壊して洗い流す独自技術で冬の毛穴の黒ずみ・くすみを一掃)"},
            {"rank": 2, "query": "ルナソル スムージングジェルウォッシュ", "brand": "LUNASOL (ルナソル / カネボウ)", "name": "スムージングジェルウォッシュ 150g (ポリッシングクレンズ処方・泡立てないみずみずしい透明ジェルが毛穴汚れを包み込み陶器肌へ導く)"},
            {"rank": 3, "query": "ビオレ おうちdeエステ 肌をなめらかにするマッサージ洗顔ジェル", "brand": "Biore (ビオレ / 花王)", "name": "おうちdeエステ 肌をなめらかにするマッサージ洗顔ジェル 150g (角栓クリア処方・ドラッグストアで買える名品！湯気のある浴室や朝の洗面所で毛穴ほぐし)"},
            {"rank": 4, "query": "ソフィーナiP ポア クリアリング ジェル ウォッシュ", "brand": "SOFINA iP (花王)", "name": "ポア クリアリング ジェル ウォッシュ 30g (黒の直塗り高密着ジェル・冬の頑固な角栓を溶かして落とし角層のうるおいを守る集中部分洗顔)"},
            {"rank": 5, "query": "オルビス アクアニスト ゼリーウォッシュ", "brand": "ORBIS (オルビス)", "name": "アクアニスト ゼリーウォッシュ 120g (敏感肌対応・クッション性のある厚みジェルが摩擦ダメージをゼロにして冬の乾燥ゆらぎ肌をしっとり洗浄)"},
            {"rank": 6, "query": "キュレル 泡立てないジェル洗顔料", "brand": "Curel (キュレル / 花王)", "name": "潤浸保湿 泡立てないジェル洗顔料 140ml (肌必須成分セラミドを守りながら洗う低刺激処方・冬のひりつき・カサつき肌を優しくケア)"},
            {"rank": 7, "query": "カネボウ スクラビング マッド ウォッシュ", "brand": "KANEBO (カネボウ)", "name": "スクラビング マッド ウォッシュ 130g (モロッコ溶岩クレイ配合・クレイから濃密ジェル、そして濃密泡へと3段階質感変化する感動洗顔)"},
            {"rank": 8, "query": "ビオレ おうちdeエステ 肌をやわらかくする", "brand": "Biore (ビオレ / 花王)", "name": "おうちdeエステ 肌をやわらかくするマッサージ洗顔ジェル 150g (浄潤ほぐし処方・冬のゴワついて化粧水が入らないカサカサ肌をふっくら柔軟に)"},
            {"rank": 9, "query": "ファンケル マイルドクレンジング ジェル", "brand": "FANCL (ファンケル)", "name": "マイルドクレンジング ジェル 120g (摩擦レスなクッションジェル・うるおいバリアを守りながら毛穴汚れやくすみをやさしく吸着オフ)"},
            {"rank": 10, "query": "サンタマルシェ ディープクレンジング", "brand": "Santa Marche (サンタマルシェ)", "name": "ディープクレンジング 400g (緑茶カテキン×重曹配合・100%オイルフリーの高保湿美容液ジェルが冬の毛穴汚れをしっとり洗い流す)"}
        ]
    },
    "winter_lip_primer": {
        "title": "保湿力の強さで冬の口紅縦ジワ落ち・皮剥け色ムラとさようなら！一日中うるおい美発色が続く高保湿リップ下地・リッププライマーランク10",
        "page_file": "winter-lip-primer.html",
        "items": [
            {"rank": 1, "query": "MAC プレップ プライム リップ", "brand": "M・A・C (マック)", "name": "プレップ プライム リップ 1.7g (世界中のメイクアップアーティストが愛用！唇表面をなめらかに整え口紅の発色と持ちを劇的にアップ)"},
            {"rank": 2, "query": "ディオール アディクト リップ マキシマイザー セラム", "brand": "DIOR (ディオール)", "name": "ディオール アディクト リップ マキシマイザー セラム (濃密ヒアルロン酸配合・無色透明のエマルジョンセラムが唇を24時間ふっくら高保湿)"},
            {"rank": 3, "query": "ボビイ ブラウン エクストラ リップ ティント", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "エクストラ リップ ティント (オリーブ・アボカド・ホホバオイル配合・高い保湿力で唇を包み込みナチュラルな血色感を仕込むリップベース)"},
            {"rank": 4, "query": "コスメデコルテ リポソーム リップセラム", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペア リップセラム 7g (美肌カプセルが唇深くまで浸透・冬のガサガサ皮剥けをリペアし口紅の密着度を格上げ)"},
            {"rank": 5, "query": "ジルスチュアート リップグロウ セラムバーム", "brand": "JILL STUART (ジルスチュアート)", "name": "リップグロウ セラムバーム (清涼感ある心地よい刺激とうるおいヴェールで、ふっくらボリュームのあるツヤ唇を演出する名品下地)"},
            {"rank": 6, "query": "エテュセ リップエディション プランパー", "brand": "ettusais (エテュセ)", "name": "リップエディション (プランパー ヘルシースタイル) (ジンジンほてリップ・冬の青白い唇にほんのり温かみと血色を与え縦ジワをぼかす下地)"},
            {"rank": 7, "query": "キールズ リップ バーム No.1", "brand": "KIEHL'S (キールズ)", "name": "リップ バーム No.1 15ml (スクワラン・アロエベラ・小麦胚芽油配合・冬の極寒乾燥から唇を鉄壁ガードするロングセラーリップベース)"},
            {"rank": 8, "query": "オルビス リップトリートメント", "brand": "ORBIS (オルビス)", "name": "リップトリートメント (ヒアルロン酸・植物性セラミド配合・マットリップの乾燥や皮剥けを防ぎ一日中うるおいをキープする薬用リップ下地)"},
            {"rank": 9, "query": "キャンメイク プランプリップケアスクラブ", "brand": "CANMAKE (キャンメイク)", "name": "プランプリップケアスクラブ (洗い流し不要！砂糖スクラブが唇の古い角質をオフしながら高保湿ラッピング・ぷるぷるの土台を作るプチプラ神品)"},
            {"rank": 10, "query": "メンソレータム リップフォンデュ", "brand": "メンソレータム (ロート製薬)", "name": "リップフォンデュ (まるでフォンデュのようにとろけて密着・オイル膜で唇をコートし口紅の縦ジワ落ちを完全ブロックする高保湿バーム)"}
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

    output_file = "fetched_3winter_nov_dec_final_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✓ Saved all fetched data to {output_file}")

if __name__ == "__main__":
    main()
