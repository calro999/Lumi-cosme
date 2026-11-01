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
    "winter_scalp_scrub": {
        "title": "保湿力の強さで冬の頭皮乾燥フケ・毛穴詰まり・かゆみとさようなら！うるおい頭皮へ導く高保湿スカルプスクラブランク10",
        "page_file": "winter-scalp-scrub.html",
        "items": [
            {"rank": 1, "query": "SABON ヘッドスクラブ リフレッシング 300g", "brand": "SABON (サボン)", "name": "ヘッドスクラブ リフレッシング 300g (死海の塩×ボタニカルオイル配合・冬の凝り固まった頭皮の古い角質と毛穴汚れをオフし潤いをチャージ)"},
            {"rank": 2, "query": "ロクシタン ファイブハーブス スカルプスクラブ", "brand": "L'OCCITANE (ロクシタン)", "name": "ファイブハーブス ピュアフレッシュネス スカルプスクラブ 150ml (シーソルト×5つのハーブエッセンシャルオイル・冬の頭皮環境を健やかに整え根元から立ち上がる美髪へ)"},
            {"rank": 3, "query": "uka スカルプクレンジング ディープ&ライト", "brand": "uka (ウカ)", "name": "スカルプクレンジング ディープ＆ライト 100ml (アミノ酸系植物由来洗浄成分×天然精油・きめ細かな泡で冬の乾燥頭皮を守りながら皮脂詰まりを一掃)"},
            {"rank": 4, "query": "ラカスタ アロマエステ スカルプ クレンジング", "brand": "La CASTA (ラ・カスタ)", "name": "アロマエステ スカルプ クレンジング リファイン 150ml (オーガニック植物成分×ハーブエキス配合・冬の乾燥フケや頭皮のニオイを穏やかにオフするジェルクレンジング)"},
            {"rank": 5, "query": "ヴェレダ ローズマリー スカルプクレンジング", "brand": "WELEDA (ヴェレダ)", "name": "ローズマリー スカルプクレンジング 200g (天然由来100%・クレイ×竹炭×オーガニックローズマリーエキス配合・冬の頭皮マッサージとディープクレンズを1本で完了)"},
            {"rank": 6, "query": "アヴェダ プラマサナ スカルプ トリートメント", "brand": "AVEDA (アヴェダ)", "name": "プラマサナ エクスフォリエーティング スカルプ トリートメント 75ml (海藻エキス×ラクトバチルス発酵液配合・冬の角層バリアを保ちながら不要な角質を穏やかに除去)"},
            {"rank": 7, "query": "OSAJI スカルプ クレンジング", "brand": "OSAJI (オサジ)", "name": "スカルプクレンジング セラム 150g (敏感肌設計・冬の乾燥でデリケートになった頭皮を摩擦レスな濃密セラムで包み込み毛穴の酸化皮脂を浮き上がらせる)"},
            {"rank": 8, "query": "フローラノーティス スカルプスクラブ", "brand": "Flora Notis JILL STUART (フローラノーティス)", "name": "エッセンシャルスカルプスクラブ 180g (シュガースクラブ×厳選フラワーオイル配合・ジャスミンの芳醇な香りに包まれながらしっとり潤い頭皮へ導く)"},
            {"rank": 9, "query": "ボディショップ ティーツリー スカルプ スクラブ", "brand": "THE BODY SHOP (ザ・ボディショップ)", "name": "ティーツリー ピューリファイング スカルプスクラブ 240ml (ケニア産フェアトレードティーツリーオイル×ソルトスクラブ・冬のニット帽蒸れによるベタつきとフケをリフレッシュ)"},
            {"rank": 10, "query": "ミルボン スカルプ ジェルシャンプー", "brand": "MILBON (ミルボン)", "name": "スカルプ ピュリファイング ジェルシャンプー 200ml (サロン専売・脂肪酸をターゲットにした濃密泡が冬の頭皮の過酸化脂質を選択的に除去し保湿)"}
        ]
    },
    "winter_medicinal_bath": {
        "title": "保湿力の強さで冬の冷え性・湯冷めカサつき砂漠肌とさようなら！芯までポカポカ潤う薬用高保湿重炭酸入浴剤ランク10",
        "page_file": "winter-medicinal-bath.html",
        "items": [
            {"rank": 1, "query": "BARTH 中性重炭酸入浴剤 30錠", "brand": "BARTH (バース)", "name": "薬用 BARTH 中性重炭酸入浴剤 30錠 [医薬部外品] (お湯を中性に保ち高濃度重炭酸イオンを長時間キープ・冬の冷え性疲労と湯上がり過乾燥を徹底予防)"},
            {"rank": 2, "query": "薬用 ホットタブ 重炭酸湯 Classic 45錠", "brand": "HOT TAB (ホットタブ)", "name": "薬用 ホットタブ 重炭酸湯 Classic 45錠 [医薬部外品] (ビタミンC配合で残留塩素を無害化・自然炭酸泉のような微細炭酸が毛細血管を広げ芯まで温め肌を保湿)"},
            {"rank": 3, "query": "きき湯 ファインヒート リセットナイト 400g", "brand": "バスクリン (きき湯)", "name": "きき湯 ファインヒート リセットナイト 400g [医薬部外品] (高濃度炭酸ガス×ジンジャー末×硫酸ナトリウム配合・冬の凝り固まった筋肉をほぐしポカポカ快眠へ)"},
            {"rank": 4, "query": "アユーラ メディテーションバスt 300ml", "brand": "AYURA (アユーラ)", "name": "メディテーションバスt 300ml (2層タイプのアロマ入浴料・ローズマリーやカモミールの安らぐハーブの香りと植物オイルが冬の乾燥肌をしっとりラッピング)"},
            {"rank": 5, "query": "クナイプ バスソルト ホップ バレリアン 850g", "brand": "Kneipp (クナイプ)", "name": "バスソルト ホップ＆バレリアンの香り 850g (古代海水の天然岩塩×ヨーロッパ伝統ハーブ精油・冬の冷え切った体を芯から温め質の良い深い睡眠へ誘う)"},
            {"rank": 6, "query": "エプソムソルト 2.2kg シークリスタルス", "brand": "Sea Crystals (シークリスタルス)", "name": "エプソムソルト オリジナル 2.2kg (純度99%以上高純度硫酸マグネシウム・冬の発汗温浴で代謝を促進しミネラルが肌のバリア機能を整えてツルツルに)"},
            {"rank": 7, "query": "ツムラのくすり湯 バスハーブ 650ml", "brand": "ツムラ (ツムラライフサイエンス)", "name": "ツムラのくすり湯 バスハーブ 650ml [医薬部外品] (生薬抽出エキス100%・センキュウやトウキが血行を促進し冬のしつこい冷え症やひび・あかぎれを改善)"},
            {"rank": 8, "query": "バブ メディキュア ほぐし 6錠", "brand": "バブ (花王)", "name": "バブ メディキュア ほぐし 6錠入 [医薬部外品] (通常の10倍の高濃度炭酸泡×高麗人参エキス配合・湯温を長時間逃さず温浴効果を高めて冬の疲労をリセット)"},
            {"rank": 9, "query": "ヴェレダ アルニカ バスミルク 200ml", "brand": "WELEDA (ヴェレダ)", "name": "アルニカ バスミルク 200ml (天然ハーブアルニカエキス配合・冬の冷えや運動後のこわばった体を温かいハーブスチームバスでじんわり解きほぐす)"},
            {"rank": 10, "query": "ハホニコ 薬用 ホットバブルプロ", "brand": "HAHONICO (ハホニコ)", "name": "薬用 ホットバブルプロ 30錠 [医薬部外品] (サロン品質のマイクロ重炭酸バブル・水道水のカルキを除去しながら高濃度重炭酸が温浴効果を高め冬の全身を潤す)"}
        ]
    },
    "winter_wipe_lotion": {
        "title": "保湿力の強さで冬の朝の冷水洗顔・乾燥つっぱりとさようなら！拭くだけで角質オフ＆濃密保水する朝用ふき取り高保湿化粧水ランク10",
        "page_file": "winter-wipe-lotion.html",
        "items": [
            {"rank": 1, "query": "カネボウ ラディアント スキン リファイナー", "brand": "KANEBO (カネボウ)", "name": "ラディアント スキン リファイナー 200ml (肌をうるおいで満たしながら余分な皮脂や古い角質をスルリと取り去り、ちゅるんとした透明ツヤ肌に整える拭き取りローション)"},
            {"rank": 2, "query": "ビオデルマ サンシビオ H2O 500ml", "brand": "BIODERMA (ビオデルマ)", "name": "サンシビオ エイチツーオー H2O D 500ml (肌に優しいミセルウォーター・敏感肌のバリアを守りながら朝の寝起き皮脂や汚れを素早くオフし高保湿)"},
            {"rank": 3, "query": "ネイチャーコンク 薬用 クリアローション とてもしっとり", "brand": "Nature Conc (ネイチャーコンク)", "name": "薬用 クリアローション とてもしっとり 200ml [医薬部外品] (ハトムギエキス×月見草油配合・角質オフ・朝洗顔・保湿・美白・肌あれ防止を1本で叶える多機能)"},
            {"rank": 4, "query": "オバジ ピーリングローション", "brand": "Obagi (オバジ)", "name": "オバジ ピーリングローション 150ml (デイリー角質ケア・冬の寒さでターンオーバーが滞ったゴワつき肌を滑らかに解きほぐし化粧水の浸透を高める)"},
            {"rank": 5, "query": "クリニーク クラリファイング ローション 1 200ml", "brand": "CLINIQUE (クリニーク)", "name": "クラリファイング ローション 1 200ml (皮膚科学発想・乾燥肌用ふき取り化粧水・不要な角質を穏やかにオフして冬のくすみを取り払いみずみずしい素肌へ)"},
            {"rank": 6, "query": "チャコット クレンジングウォーター 500ml", "brand": "Chacott COSMETICS (チャコット)", "name": "クレンジングウォーター 500ml (ステージメイク発想の圧倒的保水力・植物性うるおい成分配合で朝のふき取り洗顔も突っ張らずしっとりもちもち仕上げ)"},
            {"rank": 7, "query": "ベネフィーク リセットクリア N 200ml", "brand": "BENEFIQUE (ベネフィーク / 資生堂)", "name": "リセットクリア N 200ml (とろみのある浄化感クリアローション・冬の硬くなった角層をほぐしながらサビのように酸化した皮脂汚れを優しくリセット)"},
            {"rank": 8, "query": "ちふれ ふきとり化粧水 150ml", "brand": "CHIFURE (ちふれ)", "name": "ふきとり化粧水 150ml (トレハロース配合・クレンジング後の油分や朝の汚れをマイルドにオフし、つっぱらずみずみずしい肌を保つ高コスパ名品)"},
            {"rank": 9, "query": "雪肌精 クリアウェルネス ピュアコンク 200ml", "brand": "雪肌精 CLEAR WELLNESS (コーセー)", "name": "ピュアコンク SS 200ml (日本の自然由来イトワ配合・低刺激性ふき取り保水・冬の乾燥でデリケートに傾いた肌のキメをふっくら整える)"},
            {"rank": 10, "query": "無印良品 拭き取り化粧水 400ml", "brand": "無印良品 (MUJI)", "name": "拭き取り化粧水 400ml (岩手県釜石の天然水使用・古い角質や毛穴汚れをやさしく拭き取り透明感を引き出す大容量デイリーローション)"}
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
                    item_name = chosen.get("itemName", "")
                    
                    if not aff_url:
                        raw_item_url = chosen.get("itemUrl", "")
                        aff_url = f"https://hb.afl.rakuten.co.jp/hgc/{AFF_ID}/?pc={urllib.parse.quote(raw_item_url)}"

                    print(f"  [FOUND] rank {query_info['rank']} | {query_info['brand']} | ¥{price:,} | {item_name[:40]}...")
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "raw_item_name": item_name,
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url
                    }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_sec = 2.5 * (attempt + 1)
                print(f"  [RATE LIMIT 429] Waiting {wait_sec}s for query '{query}' (attempt {attempt+1})...")
                time.sleep(wait_sec)
            else:
                print(f"  [HTTP ERROR {e.code}] query '{query}': {e}")
                time.sleep(2)
        except Exception as e:
            print(f"  [ERROR] {query}: {e}")
            time.sleep(2)
            
    print(f"  [FALLBACK] Failed all attempts for {query_info['query']}")
    return None

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for q_info in cat_data["items"]:
        item_data = fetch_item_with_retry(q_info)
        if item_data:
            results[cat_key]["items"].append(item_data)
        else:
            print(f"❌ CRITICAL: Could not fetch item for rank {q_info['rank']} ({q_info['name']})")
        time.sleep(1.2)

with open("rakuten_scalp_bath_wipe_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\n" + "="*50)
print(f"All done! Saved to rakuten_scalp_bath_wipe_data.json")
print("="*50)
