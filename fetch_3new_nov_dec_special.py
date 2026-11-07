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
    "winter_ceramide_mist": {
        "title": "保湿力の強さで肌乾燥とさようなら！日中の暖房砂漠から角層バリアを守り抜く保湿力高めセラミドミストランク10",
        "file": "winter-ceramide-mist.html",
        "items": [
            {
                "rank": 1,
                "queries": ["キュレル ディープモイスチャースプレー 250g", "キュレル ディープモイスチャースプレー", "キュレル スプレー 250"],
                "brand": "Curel (キュレル)",
                "name": "ディープモイスチャースプレー 250g (微細化したセラミド機能成分が肌の奥深くまで浸透・メイクの上からもひと吹きで砂漠肌を満たす大容量ミスト化粧水)"
            },
            {
                "rank": 2,
                "queries": ["ETVOS モイストバリア", "エトヴォス モイストバリア", "ETVOS バリアミスト"],
                "brand": "ETVOS (エトヴォス)",
                "name": "モイストバリアミスト 50mL (ヒト型セラミド5種×植物エキス配合・真冬の寒冷空気やエアコン暖房の乾燥から素肌を守り抜くプロテクトミスト)"
            },
            {
                "rank": 3,
                "queries": ["CNP プロポリス アンプル ミスト 100ml", "CNP ミスト プロポリス", "CNP プロポリス アンプル ミスト"],
                "brand": "CNP Laboratory (チャアンドパク)",
                "name": "プロポリス アンプル ミスト 100ml (高純度プロポリスエキス×セラミドNP配合・超微細なフォグミストが乾いた肌にツヤと潤いの濃密シールドを形成)"
            },
            {
                "rank": 4,
                "queries": ["ミノン アミノモイスト アミノフルシャワー 150g", "ミノン アミノフルシャワー", "ミノン アミノモイスト ミスト"],
                "brand": "MINON (ミノン アミノモイスト)",
                "name": "アミノフルシャワー 150g (9種の保潤アミノ酸×セラミド類似成分配合・日中のカサつく敏感肌をふんわり微粒子シャワーで瞬時に鎮静保水するミスト)"
            },
            {
                "rank": 5,
                "queries": ["ダルバ ホワイトトリュフ ファーストスプレーセラム 100ml", "ダルバ ミスト 100ml", "dAlba ファーストスプレーセラム"],
                "brand": "d'Alba (ダルバ)",
                "name": "ホワイトトリュフ ファースト スプレー セラム 100ml (イタリア産ホワイトトリュフ×植物オイル×セラミド配合・韓国CA御用達の二層式ツヤ肌保湿ミスト)"
            },
            {
                "rank": 6,
                "queries": ["ラロッシュポゼ ターマルウォーター 300g", "ラロッシュポゼ ターマルウォーター 150g", "ラロッシュポゼ ターマルウォーター"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "ターマルウォーター 300g (天然のセレンや希少ミネラルを豊富に含む湧水100%・乾燥で過敏に傾いた肌のバリアを整え落ち着かせるミスト化粧水)"
            },
            {
                "rank": 7,
                "queries": ["カルテHD モイスチュア ミストローション", "カルテHD ミスト", "カルテHD ミストローション"],
                "brand": "Carte HD (カルテHD)",
                "name": "モイスチュア ミストローション 60ml (保水有効成分ヘパリン類似物質HD×うるおいバリアCP配合・日中の暖房乾燥による粉吹きをその場でリセットする高保湿ミスト)"
            },
            {
                "rank": 8,
                "queries": ["メイクカバー うるおいミスト", "MAKE COVER うるおいミスト", "うるおいミスト セラミド"],
                "brand": "MAKE COVER (メイクカバー)",
                "name": "うるおいミスト 65g (3種のセラミド×ヒアルロン酸配合・メイク崩れを防ぎながら冬のエアコン乾燥から素肌を一日中ラップして守る仕上げミスト)"
            },
            {
                "rank": 9,
                "queries": ["dプログラム アレルバリア ミスト", "資生堂 dプログラム ミスト", "dプログラム ミスト"],
                "brand": "d program (dプログラム)",
                "name": "アレルバリア ミスト N 57mL (オイル×化粧水の二層バリア処方・冬の乾燥や微粒子汚れから肌を守り瞬時にしっとりしたツヤ肌へ導く敏感肌用ミスト)"
            },
            {
                "rank": 10,
                "queries": ["トリデン ダイブイン ミスト", "Torriden ダイブイン ミスト", "トリデン ミスト 100ml"],
                "brand": "Torriden (トリデン)",
                "name": "ダイブイン 低分子ヒアルロン酸 スプレー ミスト 100ml (5重複合低分子ヒアルロン酸×セラミドNP配合・角層の隙間へ素早く水分をチャージする高密着ミスト)"
            }
        ]
    },
    "winter_panthenol_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！損傷した角層バリアを深部から修復する保湿力高めパンテノール美容液ランク10",
        "file": "winter-panthenol-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["バイオヒールボ パンテノール アンプル", "BIOHEAL BOH パンテノール シカ アンプル", "バイオヒールボ シカ アンプル 30ml"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "パンテセル シカ ブレミッシュ アンプル 30ml (高濃度パンテノール10%×CICA成分配合・真冬の冷気と暖房で傷んだ肌バリアを集中リペアする濃厚美容液)"
            },
            {
                "rank": 2,
                "queries": ["ラロッシュポゼ ヒアルB5 セラム", "ラロッシュポゼ ヒアルB5", "ヒアルB5 セラム 30ml"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "ヒアルB5 セラム 30mL (高純度プロビタミンB5/パンテノール×2種の分子量ヒアルロン酸配合・真冬の乾燥しぼみ肌をふっくらモチモチに満たす薬用級高保湿セラム)"
            },
            {
                "rank": 3,
                "queries": ["ジオーディナリー アミノ酸 B5", "The Ordinary アミノ酸 B5", "ジオーディナリー アミノ酸"],
                "brand": "The Ordinary (ジ オーディナリー)",
                "name": "アミノ酸 + B5 30ml (天然保湿因子NMFを模倣した17%高濃度アミノ酸×プロビタミンB5配合・角層深部の水分保持力を劇的に引き上げるブースティングセラム)"
            },
            {
                "rank": 4,
                "queries": ["COSRX プロポリス ライト アンプル", "コスアールエックス プロポリス アンプル", "COSRX プロポリス 30ml"],
                "brand": "COSRX (コスアールエックス)",
                "name": "フルフィット プロポリス ライト アンプル 30ml (黒蜂プロポリスエキス83.25%×パンテノール配合・冬の乾燥枯れ肌に蜜のような濃密な潤いと弾力ツヤを宿す名作美容液)"
            },
            {
                "rank": 5,
                "queries": ["アヌア シラカバ セラム", "Anua シラカバ 水分 セラム", "アヌア 水分 セラム 30ml"],
                "brand": "Anua (アヌア)",
                "name": "シラカバ 70% 水分 ブースティング セラム 30ml (清浄シラカバ樹液70%×パンテノール配合・角層を水分で満たして冬のインナードライを根本ケアする水分セラム)"
            },
            {
                "rank": 6,
                "queries": ["魔女工場 パンテトイン エッセンス", "魔女工場 パンテトイン", "manyo パンテトイン"],
                "brand": "manyo (魔女工場)",
                "name": "パンテトイン エッセンス 200ml (パンテノール×エクトイン高配合・過酷な極寒乾燥環境でも角層の水分蒸散をブロックする濃厚高保湿エッセンス)"
            },
            {
                "rank": 7,
                "queries": ["スキンアンドラブ パンテノール", "SKIN&LAB パンテノール", "パンテノール アンプル 美容液"],
                "brand": "SKIN&LAB (スキンアンドラブ)",
                "name": "トリセル パンテノール 5% アンプル 30ml (プロビタミンB5高濃度5%×トリプルペプチド配合・冬の寒暖差で弱った角層バリアを強固に再建するリペア美容液)"
            },
            {
                "rank": 8,
                "queries": ["リアルバリア アンプル", "Real Barrier アンプル", "リアルバリア アクアスージング"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "アクア スージング アンプル 30ml (独自特許MLEバリア×パンテノール配合・乱れた角層ラメラ構造を整えて冬の水分蒸発を完全ガードするバリア集中美容液)"
            },
            {
                "rank": 9,
                "queries": ["ドクタージャルト シカペア セラム", "シカペア セラム 30ml", "ドクタージャルト シカ セラム 50ml"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "シカペア インテンシブ スージング リペア セラム 30ml (ツボクサエキス×パンテノール配合・真冬の冷風や摩擦で敏感にゆらいだ肌を速攻クールダウン＆高保湿ケア)"
            },
            {
                "rank": 10,
                "queries": ["SAM'U PH センシティブ アンプル", "サミュ PH アンプル", "SAMU アンプル 30ml"],
                "brand": "SAM'U (サミュ)",
                "name": "PHセンシティブ アンプル 30ml (パンテノール×マルチヒアルロン酸配合・冬の乾燥でアルカリに傾いた素肌を理想的な弱酸性pH5.5へ導く高保湿鎮静アンプル)"
            }
        ]
    },
    "winter_oil_in_lotion": {
        "title": "保湿力の強さで肌乾燥とさようなら！水分と上質オイルの黄金比で満たす保湿力高めオイルイン化粧水ランク10",
        "file": "winter-oil-in-lotion.html",
        "items": [
            {
                "rank": 1,
                "queries": ["RMK Wトリートメントローション", "RMK トリートメントローション 160", "RMK Wトリートメント ローション 160ml"],
                "brand": "RMK (アールエムケー)",
                "name": "Wトリートメント ローション 160ml (オイル層とローション層の絶妙バランス・冬の冷気で硬化した角層をとろけるように柔軟化しリッチな潤いで満たす二層式化粧水)"
            },
            {
                "rank": 2,
                "queries": ["SHIRO タマヌ オイルイン セラム", "SHIRO 酒粕米ぬか オイルインローション", "SHIRO オイルイン"],
                "brand": "SHIRO (シロ)",
                "name": "タマヌ オイルインセラム 30ml (古来より伝わる奇跡の万能オイル・タマヌ×酒粕エキス配合・冬のゴワつく乾燥肌をふっくら艶やかに整える濃密二層式オイルローション)"
            },
            {
                "rank": 3,
                "queries": ["アルビオン フローラドリップ 160ml", "アルビオン フローラドリップ 80ml", "アルビオン フローラドリップ"],
                "brand": "ALBION (アルビオン)",
                "name": "フローラドリップ 160ml (5種の厳選ハーブを純白麹で発酵濃縮・濃密な美容オイルのようなリッチな感触で冬の枯れ肌に劇的なハリと潤いを与える高機能発酵液)"
            },
            {
                "rank": 4,
                "queries": ["カネボウ スキン ハーモナイザー 180ml", "KANEBO スキン ハーモナイザー", "スキン ハーモナイザー カネボウ"],
                "brand": "KANEBO (カネボウ)",
                "name": "スキン ハーモナイザー 180ml (オイル層とエッセンス層の黄金シェイク処方・冬の悪玉皮脂をトラップしながら角層深くまで贅沢な潤いを閉じ込めるバランシング化粧水)"
            },
            {
                "rank": 5,
                "queries": ["コスメデコルテ リポソーム アドバンスト リペアローション", "コスメデコルテ リペアローション 100ml", "コスメデコルテ ローション"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアローション 100ml (多重層バイオリポソームオイルカプセル配合・肌に乗せた瞬間から角層深部へ潤いオイル成分を放出し続ける名品化粧液)"
            },
            {
                "rank": 6,
                "queries": ["ヴェレダ ざくろ モイスチャーローション", "ヴェレダ モイスチャーローション", "WELEDA ローション 保湿"],
                "brand": "WELEDA (ヴェレダ)",
                "name": "ざくろ モイスチャーローション 100ml (高貴なざくろ種子オイル×植物エキス配合・冬の乾燥による小ジワやハリ不足を上質オイルヴェールで包み込むエイジングケア化粧水)"
            },
            {
                "rank": 7,
                "queries": ["オルビス アンバー ヴァイタルトリートメントローション", "オルビス アンバー ローション", "オルビス アンバー"],
                "brand": "ORBIS (オルビス)",
                "name": "アンバー ヴァイタルトリートメントローション 120ml (オイルインリッチ設計の薬用高保湿化粧液・大人世代の真冬の乾燥小ジワを改善しふっくら弾むハリ肌へ導く)"
            },
            {
                "rank": 8,
                "queries": ["ファミュ デュアルエッセンス", "FEMMUE デュアルエッセンス 100ml", "FEMMUE デュアルエッセンス"],
                "brand": "FEMMUE (ファミュ)",
                "name": "デュアルエッセンス 100ml (カメリアオイル×フラワーエッセンスの贅沢二層式・微細なミストが肌をふんわり包み真冬の乾燥肌にしっとりしたツヤと柔軟性を与えるミスト化粧水)"
            },
            {
                "rank": 9,
                "queries": ["ハクスリー トナー エクストラクトイット", "Huxley トナー 120ml", "ハクスリー エクストラクトイット"],
                "brand": "Huxley (ハクスリー)",
                "name": "トナー エクストラクト イット 120ml (サハラ砂漠の希少サボテンシードオイル90%以上天然由来・乾燥した肌の水分油分バランスを黄金比に整える弱酸性高保湿トナー)"
            },
            {
                "rank": 10,
                "queries": ["ラネージュ クリームスキン ローション 170ml", "ラネージュ クリームスキン 170ml", "LANEIGE クリームスキン 170ml", "ラネージュ クリームスキン"],
                "brand": "LANEIGE (ラネージュ)",
                "name": "クリームスキン ローション 170ml (高保湿クリームまるごと1個分を化粧水に溶かし込んだ特許マイクロ乳化技術・ひと塗りで乳液・クリーム級の潤いが続く濃厚化粧水)"
            }
        ]
    }
}

def fetch_all():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title'][:35]}...)")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Rank {item['rank']}: Trying query '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                try:
                    time.sleep(2.0)
                    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                        data = json.loads(res.read().decode('utf-8'))
                        items = data.get("Items", [])
                        for it in items:
                            cand = it["Item"]
                            price = cand.get("itemPrice", 0)
                            if price >= 300 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                chosen_item = cand
                                break
                    if chosen_item:
                        break
                except urllib.error.HTTPError as e:
                    print(f"    HTTP Error {e.code}: {e.reason}")
                    time.sleep(3.0)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(2.5)
            
            if chosen_item:
                print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if "?_ex=" in img_url:
                    img_url = img_url.split("?_ex=")[0] + "?_ex=400x400"
                
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": chosen_item.get("affiliateUrl", chosen_item.get("itemUrl")),
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "4.8"))
                })
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_nov_dec_special.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_nov_dec_special.json!")

if __name__ == "__main__":
    fetch_all()
