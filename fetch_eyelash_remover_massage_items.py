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
    "winter_eyelash_serum": {
        "title": "保湿力の強さで冬のまつ毛抜け・パサつき乾燥とさようなら！ハリ・コシ・密度感を呼び覚ます高保湿まつ毛美容液・アイラッシュセラムランク10",
        "page_file": "winter-eyelash-serum.html",
        "items": [
            {"rank": 1, "query": "ラッシュアディクト アイラッシュ コンディショニング セラム", "brand": "Lashaddict (ラッシュアディクト)", "name": "アイラッシュ コンディショニング セラム (独自ナノペプチド複合体配合・真冬の乾燥で細く弱った自まつ毛に圧倒的なハリ・コシ・密度感を与える世界的ベストセラー)"},
            {"rank": 2, "query": "エマーキット まつ毛美容液 水橋保寿堂製薬", "brand": "EMAKED (エマーキット)", "name": "アイラッシュセラム (加水分解ムコ多糖やヒアルロン酸配合・就寝前にひと塗りで根元から太く力強い美まつ毛を育む超濃厚処方)"},
            {"rank": 3, "query": "ディオール ディオールショウ マキシマイザー 4D", "brand": "DIOR (ディオール)", "name": "ディオールショウ マキシマイザー 4D (ブルーフラワーエキス高配合・まつ毛美容液＆マスカラ下地のダブルケアで24時間トリートメント＆濃密ボリューム)"},
            {"rank": 4, "query": "ランコム シィル ブースター ラッシュ セラム", "brand": "LANCÔME (ランコム)", "name": "シィル ブースター ラッシュ セラム (4種のアミノ酸やマデカッソシド配合・冬の摩擦やビューラーダメージで傷んだまつ毛を毛先まで濃密コーティング補修)"},
            {"rank": 5, "query": "コスメデコルテ AQ アイラッシュ ファイン セラム", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ アイラッシュ ファイン セラム (白樺水や厳選ハーブエキス配合・まぶたのキワまでみずみずしくうるおし艶やかでしなやかな上質まつ毛へ)"},
            {"rank": 6, "query": "マジョリカ マジョルカ ラッシュジェリードロップ EX プレミアム", "brand": "MAJOLICA MAJORCA (マジョリカ マジョルカ)", "name": "ラッシュジェリードロップ EX プレミアム (濃密毛髪補修成分配合・ジュレがまつ毛1本1本に密着しパックのようにうるおいを閉じ込める高コスパ名品)"},
            {"rank": 7, "query": "スカルプD まつげ美容液 プレミアム", "brand": "スカルプD ボーテ", "name": "ピュアフリーアイラッシュセラム プレミアム (まつ毛ケア成分2倍配合・ナノ化カプセルが角層深くまで浸透し大人のまぶたケアも同時に叶える)"},
            {"rank": 8, "query": "UZU まつげ美容液", "brand": "UZU BY FLOWFUSHI (ウズ)", "name": "まつげ美容液 (指でまぶたとまつ毛にサッと塗るだけ・高純度ピュア成分と天然ミネラル配合でデリケートな冬の目元全体をうるおす)"},
            {"rank": 9, "query": "エトヴォス アイラッシュセラム", "brand": "ETVOS (エトヴォス)", "name": "ミネラルアイラッシュセラム (7種のフリー処方・敏感肌でも安心な低刺激設計でパンテノールと植物エキスが自まつ毛を健やかに保護)"},
            {"rank": 10, "query": "リバイタラッシュ アドバンス ジャパン", "brand": "RevitaLash (リバイタラッシュ)", "name": "リバイタラッシュ アドバンス ジャパン (眼科医開発・独自バイオペプチン複合体が冬の乾燥に負けないしなやかで存在感あるまつ毛を育むドクターズコスメ)"}
        ]
    },
    "winter_point_makeup_remover": {
        "title": "保湿力の強さで目元・口元の摩擦ダメージ＆乾燥小ジワとさようなら！デリケートな皮膚をうるおいで守り抜く高保湿ポイントメイクリムーバーランク10",
        "page_file": "winter-point-makeup-remover.html",
        "items": [
            {"rank": 1, "query": "ルナソル ポイントメイクオフN", "brand": "LUNASOL (ルナソル)", "name": "ポイントメイクオフN (ウォーターとオイルの2層タイプ・デリケートな目元や口元に負担をかけず濃密アイメイクもこすらずスルンと落とす名品)"},
            {"rank": 2, "query": "シャネル デマキヤン ユー アンタンス", "brand": "CHANEL (シャネル)", "name": "デマキヤン ユー アンタンス (コーンフラワー水と上質エモリエントオイル配合・頑固なウォータープルーフマスカラも瞬時に浮かせ後肌をしっとり保つ)"},
            {"rank": 3, "query": "クレ ド ポー ボーテ デマキアン YL", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "デマキアン YL (資生堂最高峰・独自保湿成分配合でポイントメイクを優しく取り去りながら乾燥小ジワを防ぐラグジュアリーリムーバー)"},
            {"rank": 4, "query": "ビフェスタ ミセラー アイメイクアップリムーバー", "brand": "Bifesta (ビフェスタ)", "name": "ミセラー アイメイクアップリムーバー (ビタミンB・E誘導体配合・プチプラ界の絶対王者！こすらずオフしてまつ毛や目元のうるおいを強力キープ)"},
            {"rank": 5, "query": "ランコム ビファシル リムーバー", "brand": "LANCÔME (ランコム)", "name": "ビファシル (世界中で数々のベストコスメを受賞・敏感な目元にも優しい2層式フォーミュラで濃密ティントやマスカラを完璧クレンジング)"},
            {"rank": 6, "query": "クリニーク テイク ザ デイ オフ リッド リムーバー", "brand": "CLINIQUE (クリニーク)", "name": "テイク ザ デイ オフ (皮膚科学に基づいた無香料・アレルギーテスト済み処方・まぶたや唇に刺激を与えず素早く落とす実力派)"},
            {"rank": 7, "query": "ヘレナルビンスタイン プロディジー メイクアップ リムーバー", "brand": "HELENA RUBINSTEIN (ヘレナ ルビンスタイン)", "name": "オール マスカラ リムーバー (ウォータープルーフマスカラのエキスパートが生み出した、まつ毛をいたわりながら瞬時にオフする高保湿リムーバー)"},
            {"rank": 8, "query": "OSAJI ポイント メイクリムーバー", "brand": "OSAJI (オサジ)", "name": "ポイントメイクリムーバー (敏感肌ブランド発・皮脂バランスを崩さず植物性オイルがデリケートな粘膜近くのアイラインまで優しくオフ)"},
            {"rank": 9, "query": "SUQQU アイメイクアップ リムーバー", "brand": "SUQQU (スック)", "name": "アイ＆リップ メイクアップ リムーバー (水層と油層の絶妙な黄金比率・まぶたにうるおいヴェールを残しながら大人の華やかラメも綺麗に除去)"},
            {"rank": 10, "query": "コーセー ソフティモ スーパー ポイントメイクアップ リムーバー", "brand": "KOSE softymo (ソフティモ)", "name": "スーパー ポイントメイクアップ リムーバー (ヒアルロン酸・トレハロース配合のジェルローションタイプ・目に染みにくく涙に近い中性処方で高保湿)"}
        ]
    },
    "winter_massage_cream": {
        "title": "保湿力の強さで冬の冷えむくみ・乾燥くすみ・フェイスラインたるみとさようなら！巡りを高めてふっくら上向き肌へ導く高保湿フェイスマッサージクリームランク10",
        "page_file": "winter-massage-cream.html",
        "items": [
            {"rank": 1, "query": "POLA B.A マッサージクリーム", "brand": "POLA (ポーラ)", "name": "B.A マッサージクリーム (最高峰エイジングケア・肌の上でとろけて心地よい指すべりを実現・冬の冷え固まった表情筋をほぐし圧倒的な立体ハリ肌へ)"},
            {"rank": 2, "query": "SUQQU デザイニング マッサージ クリーム", "brand": "SUQQU (スック)", "name": "デザイニング マッサージ クリーム (元祖『顔筋マッサージ』専用クリーム・リッチなコクから軽やかなオイルへ質感が変化しフェイスラインをシャープに引き締める)"},
            {"rank": 3, "query": "エリクシール シュペリエル フェイスエフェクト マッサージ", "brand": "ELIXIR (エリクシール)", "name": "フェイスエフェクト マッサージ (コラーゲン・エラスチンエキス配合・冬の乾燥で硬くなった角層を柔らかくほぐし『つや玉』が輝く肌へ導く薬用クリーム)"},
            {"rank": 4, "query": "コスメデコルテ AQ マッサージクリーム", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ マッサージクリーム (白樺水や厳選ペプチド配合・コクのあるとろけるテクスチャーで血行を促し、くすみを一掃して輝く透明感を呼び覚ます)"},
            {"rank": 5, "query": "アルビオン エクシア マッサージクリーム", "brand": "ALBION (アルビオン エクシア)", "name": "アンベアージュ マッサージ / エクシア ラディアンスリニュー マッサージ (濃密なコクが肌を包み込み、冬の乾燥毛穴やたるみを上向きにリフトアップする至高品)"},
            {"rank": 6, "query": "KANEBO カネボウ スキンバウンシング クリーム マッサージ", "brand": "KANEBO (カネボウ)", "name": "スキン スムージング マッサージ クリーム (弾むようなハリ感を与えるリッチな処方・摩擦レスな極上のクッション性で冬の血色不良とゴワつきをリセット)"},
            {"rank": 7, "query": "カバーマーク セルアドバンスト マッサージ クリーム", "brand": "COVERMARK (カバーマーク)", "name": "マッサージクリーム (肌のめぐりに着目・まろやかなクリームが肌温度でなめらかに広がり、冬の乾燥小ジワや乾燥くすみを押し上げる)"},
            {"rank": 8, "query": "雪肌精 ハーバル マッサージ パック", "brand": "SEKKISEI (雪肌精)", "name": "ハーバル マッサージ パック (和漢植物エキスを濃縮・マッサージしながら約2分パックするだけで真冬のくすみ・毛穴・キメの乱れを一度にケア)"},
            {"rank": 9, "query": "ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX プラセンタ", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "アクアコラーゲンゲル エンリッチリフトEX (金コロイド×浸透型コラーゲン配合・マッサージしながらリフトアップケアができる高機能オールインワン)"},
            {"rank": 10, "query": "ちふれ ウォッシャブル コールド クリーム マッサージ", "brand": "CHIFURE (ちふれ)", "name": "ウォッシャブル コールド クリーム (マッサージ＆クレンジング両用・指先がふっと軽くなるオイル化サインで冬の頑固な角栓やコリを優しくオフする国民的人気品)"}
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
                    aff_url = chosen.get("affiliateUrl", chosen.get("itemUrl", ""))
                    item_name = chosen.get("itemName", "")
                    shop_name = chosen.get("shopName", "")
                    
                    print(f"  [Success] rank {query_info['rank']}: {query_info['brand']} | Price: ¥{price:,} | Img: {high_res_img[:60]}...")
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "price": price,
                        "image": high_res_img,
                        "affiliate_url": aff_url,
                        "rakuten_item_name": item_name,
                        "shop_name": shop_name
                    }
                else:
                    print(f"  [Empty] query: '{query}' returned no items, trying fallback query...")
                    if len(query.split()) > 2:
                        query = " ".join(query.split()[:2])
                        time.sleep(0.5)
                        continue
        except Exception as e:
            print(f"  [Error attempt {attempt+1}] {e}")
            time.sleep(1)
            
    print(f"  [Failed] Could not find item for query: {raw_q}")
    return None

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
    print(f"==========================================")
    cat_items = []
    for item_info in cat_data["items"]:
        fetched = fetch_item_with_retry(item_info)
        if fetched:
            cat_items.append(fetched)
        else:
            print(f"CRITICAL: Failed to fetch rank {item_info['rank']} for {cat_key}")
        time.sleep(0.4)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

output_file = "rakuten_eyelash_remover_massage_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAll categories fetched! Saved to {output_file}")
