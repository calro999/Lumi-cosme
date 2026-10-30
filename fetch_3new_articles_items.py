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
    "winter_holiday_coffret": {
        "title": "贅沢なうるおいと輝きで真冬の乾燥肌・メイクを特別格上げ！11月12月限定ホリデーコレクション＆高保湿クリスマスコフレランク10",
        "page_file": "winter-holiday-coffret.html",
        "items": [
            {"rank": 1, "query": "コスメデコルテ クリスマスコフレ ホワイトブリス コフレ", "brand": "DECORTÉ (コスメデコルテ)", "name": "ホワイトブリス コレクション (毎年即完売！最高峰の粉質とスキンケア発想のうるおいで冬の透明感を極める限定ホリデーコフレ)"},
            {"rank": 2, "query": "ディオール クリスマスコフレ ホリデー オファー ミスディオール", "brand": "DIOR (ディオール)", "name": "ディオール ホリデー オファー (ミスディオール＆高保湿リップ現品が入った豪華ポーチ付き・真冬の美しさを底上げする限定セット)"},
            {"rank": 3, "query": "ルナソル クリスマスコフレ アイカラーレーション スペシャルエディション", "brand": "LUNASOL (ルナソル)", "name": "アイカラーレーション スペシャルエディション (贅沢なラメと高密着オイルリッチ処方・真冬の澄んだ空気でドラマティックに輝く8色パレット)"},
            {"rank": 4, "query": "SABON クリスマスコフレ ホリデー スクラブ ボディケア", "brand": "SABON (サボン)", "name": "ホリデー スクラブ＆ボディケア リミテッドセット (死海の塩と植物オイルの濃厚保湿・バスルームを極上の甘い香りで満たす限定コレクション)"},
            {"rank": 5, "query": "クレ ド ポー ボーテ クリスマスコフレ ルージュアレーブル ホリデー", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "ホリデーコレクション ルージュアレーブル / セラム限定キット (資生堂最高峰・宝石のような限定パッケージと極上のうるおい膜)"},
            {"rank": 6, "query": "キールズ クリスマスコフレ クリーム UFC ホリデー", "brand": "KIEHL'S (キールズ)", "name": "ホリデー リミテッド エディション クリーム UFC セット (真冬の砂漠肌を救う世界的No.1高保湿クリームの限定ホリデーエディション)"},
            {"rank": 7, "query": "ジルスチュアート クリスマスコフレ ホリデーコレクション", "brand": "JILL STUART (ジルスチュアート)", "name": "ホリデーコレクション コフレ (毎年争奪戦！甘く華やかな香りと高保湿リップ＆アイカラーが詰まったプリンセス限定コフレ)"},
            {"rank": 8, "query": "SK-II フェイシャルトリートメントエッセンス ホリデー フェスティブ ギフト", "brand": "SK-II (エスケーツー)", "name": "ピテラ ベストコレクション ホリデー リミテッド (ピテラ90%以上の奇跡の滴・冬の乾燥ゴワつきをリセットしクリアな素肌へ)"},
            {"rank": 9, "query": "ローラメルシエ アンバーバニラ ボディケア コフレ ホリデー", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "リュクス インダルジェンス アンバーバニラ コレクション (人類モテの甘い香りと高保湿ボディクリームがセットになった冬限定の贅沢品)"},
            {"rank": 10, "query": "SHIRO ホリデー オードパルファン ハンド美容液 セット", "brand": "SHIRO (シロ)", "name": "ホリデー フェイバリット コフレ (天然植物エキスの恵み・冬の乾燥手肌をうるおす限定ハンド美容液と心温まる限定フレグランス)"}
        ]
    },
    "winter_enzyme_wash": {
        "title": "保湿力の強さで冬の角質ゴワつき・くすみ毛穴とさようなら！つっぱらず透明感を呼び覚ます高保湿酵素洗顔パウダーランク10",
        "page_file": "winter-enzyme-wash.html",
        "items": [
            {"rank": 1, "query": "オバジC 酵素洗顔パウダー 30個", "brand": "Obagi (オバジ)", "name": "オバジC 酵素洗顔パウダー (ピュアビタミンC×2種の酵素配合・冬の角栓詰まりやくすみを徹底分解しながらつっぱらない大人気品)"},
            {"rank": 2, "query": "suisai スイサイ スイサイ ビューティクリア ゴールド パウダーウォッシュ", "brand": "suisai (スイサイ)", "name": "ビューティクリア ゴールド パウダーウォッシュ (金の美容オイル・スクワラン高配合！乾燥肌のための超しっとり酵素洗顔)"},
            {"rank": 3, "query": "ファンケル ディープクリア 洗顔パウダー", "brand": "FANCL (ファンケル)", "name": "ディープクリア 洗顔パウダー (炭×吸着泥×酵素のトリプルアプローチ・弾力ある濃密クッション泡で真冬のうるおいを守る)"},
            {"rank": 4, "query": "カネボウ クラリファイング パウダー ウォッシュ 酵素洗顔", "brand": "KANEBO (カネボウ)", "name": "クラリファイング パウダー ウォッシュ (白とピンクの2色パウダー・不要な古い角質だけを取り去りしっとり吸い付くような洗い上がり)"},
            {"rank": 5, "query": "est エスト クラリファイイング ジェル ウォッシュ 洗顔", "brand": "est (エスト)", "name": "クラリファイイング クレンジング ウォッシュ / パウダー (角栓崩壊技術を採用・冬の頑固な角栓を溶かして洗い流し極上の透明素肌へ)"},
            {"rank": 6, "query": "ミノン アミノモイスト クリアウォッシュ パウダー", "brand": "MINON (ミノン アミノモイスト)", "name": "クリアウォッシュ パウダー (9種の保潤アミノ酸配合・敏感肌・乾燥肌でも毎日使える低刺激設計のうるおい酵素洗顔)"},
            {"rank": 7, "query": "キュレル 潤浸保湿 パウダー洗顔料", "brand": "Curel (キュレル)", "name": "泡洗顔料 / 潤浸保湿 洗顔パウダー (セラミドを守って洗う消炎剤配合処方・真冬の肌荒れやカサつきを防ぎながら毛穴汚れオフ)"},
            {"rank": 8, "query": "ルシェリ 酵素洗顔パウダー コーセー", "brand": "LECHERI (ルシェリ)", "name": "酵素洗顔パウダー (コラーゲン×アミノ酸系洗浄成分・冬のゆるみ毛穴やキメの乱れをなめらかに整えるエイジングケア酵素洗顔)"},
            {"rank": 9, "query": "雪肌精 クリア トリートメント エッセンス 洗顔 パウダー", "brand": "SEKKISEI (雪肌精)", "name": "ホワイト パウダー ウォッシュ (和漢植物エキスを濃縮・キメ細かなメレンゲ泡が冬のくすみを取り除き雪のように澄んだ素肌へ)"},
            {"rank": 10, "query": "ドクターシーラボ VC100 ホットピール 酵素 洗顔 パウダー", "brand": "DR.CI:LABO (ドクターシーラボ)", "name": "VC100 パウダーウォッシュ (高浸透ビタミンC(APPS)×トリプル酵素・冬の乾燥で硬くなった角層を柔らかくほぐす濃密泡)"}
        ]
    },
    "winter_tinted_lip_balm": {
        "title": "保湿力の強さで冬のカサカサ唇＆血色レスとさようなら！ひと塗りでぷるんと潤う高保湿カラーリップバームランク10",
        "page_file": "winter-tinted-lip-balm.html",
        "items": [
            {"rank": 1, "query": "ディオール アディクト リップ グロウ リップバーム", "brand": "DIOR (ディオール)", "name": "アディクト リップ グロウ (97%自然由来成分・唇の水分量に反応して自分だけの色に染まる！一日中うるおいが続く世界的名品)"},
            {"rank": 2, "query": "シャネル ルージュ ココ ボーム リップボーム", "brand": "CHANEL (シャネル)", "name": "ルージュ ココ ボーム (オリーブ由来有用成分配合・シアーから鮮やかな発色まで重ね塗りで自在に調整できる極上リップボーム)"},
            {"rank": 3, "query": "KANEBO モイスチャールージュエッセンス リップ", "brand": "KANEBO (カネボウ)", "name": "ルージュスターヴァイブラント / モイスチャールージュ (脈打つような血色感と濃密なうるおい膜が持続・真冬の乾燥から唇を鉄壁ガード)"},
            {"rank": 4, "query": "NARS アフターグロー リップバーム", "brand": "NARS (ナーズ)", "name": "アフターグロー リップバーム (モノイオイル配合・透け感のあるシアーな輝きとシルキーな保湿感でふっくら弾むような魅惑の唇へ)"},
            {"rank": 5, "query": "ボビイ ブラウン エクストラ リップ ティント", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "エクストラ リップ ティント (6種のボタニカルオイル配合・リップクリーム並みの高い保湿力で荒れた唇を即効トリートメント)"},
            {"rank": 6, "query": "アディクション リップ オイル ティント バーム", "brand": "ADDICTION (アディクション)", "name": "リップ セラム ティント (ホホバ種子油・シアバター配合・みずみずしいツヤと落ちにくい自然な血色ティントが長時間持続)"},
            {"rank": 7, "query": "シスレー フィト リップ バーム リップケア", "brand": "SISLEY (シスレー)", "name": "フィト リップ ツイスト / バーム (植物由来のスキンケア成分を凝縮・ひと塗りでなめらかなツヤとふっくらボリュームを与える贅沢バーム)"},
            {"rank": 8, "query": "キュレル リップケアクリーム ほんのり色づくタイプ", "brand": "Curel (キュレル)", "name": "リップケアクリーム ほんのり色づくタイプ (セラミド機能成分配合・乾燥して敏感になった唇を低刺激にうるおし自然な血色をプラス)"},
            {"rank": 9, "query": "メンソレータム リップフォンデュ ロート製薬", "brand": "メンソレータム (ロート製薬)", "name": "リップフォンデュ (とろけるフォンデュのように唇を包み込む濃密オイルラップ処方・冬のプチプラ界最強のウルウル持続力)"},
            {"rank": 10, "query": "オペラ リップティント N リップケア", "brand": "OPERA (オペラ)", "name": "リップティント N (スクワランオイル高配合・鏡なしでスルスル塗れて透けるキレイ色が落ちずに続く大定番リップ)"}
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

output_file = "rakuten_3new_articles_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAll 3 new categories fetched! Saved to {output_file}")
