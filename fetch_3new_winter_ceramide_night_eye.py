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
    "winter_ceramide_milk": {
        "title": "保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10",
        "file": "winter-ceramide-milk.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ケアセラ AP フェイス ボディ乳液 200ml", "ケアセラ AP フェイス ボディ乳液", "ケアセラ 乳液 200ml"],
                "brand": "CareCera (ケアセラ)",
                "name": "ケアセラ APフェイス＆ボディ乳液 200mL (7種の天然型セラミド×ペプチドCP配合・カサつく乾燥肌のラメラ構造を深部から修復する高保湿乳液)"
            },
            {
                "rank": 2,
                "queries": ["キュレル 潤浸保湿 乳液 120ml", "キュレル 乳液 120ml", "キュレル 潤浸保湿 乳液"],
                "brand": "Curel (キュレル)",
                "name": "潤浸保湿 乳液 120mL (花王独自のセラミド機能成分×ユーカリエキス配合・消炎剤配合で冬の粉吹き・肌荒れを防ぎしっとり保つ薬用乳液)"
            },
            {
                "rank": 3,
                "queries": ["ミノン アミノモイスト モイストチャージ ミルク 100g", "ミノン モイストチャージ ミルク", "ミノン アミノモイスト ミルク"],
                "brand": "MINON (ミノン アミノモイスト)",
                "name": "モイストチャージ ミルク 100g (9種の保潤アミノ酸×リピジュア×セラミド類似成分・とろ〜り広がり吸い付くように馴染むロングセラー高保湿乳液)"
            },
            {
                "rank": 4,
                "queries": ["ETVOS モイスチャライジングセラム 50ml", "エトヴォス モイスチャライジングセラム", "ETVOS モイスチャライジング セラム"],
                "brand": "ETVOS (エトヴォス)",
                "name": "モイスチャライジングセラム 50mL (ヒト型セラミド5種をバランス高濃度配合・美容液と乳液の機能を1本に凝縮した濃密セラミドミルク)"
            },
            {
                "rank": 5,
                "queries": ["松山油脂 肌をうるおす 保湿乳液", "肌をうるおす保湿スキンケア 保湿乳液", "松山油脂 保湿乳液 100ml"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "保湿乳液 100mL (大豆由来成分×5種のヒト型セラミド配合・角質層をやわらげ水分と油分をバランスよく蓄える低刺激高保湿乳液)"
            },
            {
                "rank": 6,
                "queries": ["トゥヴェール ナノエマルジョン 50ml", "トゥヴェール ナノエマルジョン", "TOUT VERT ナノエマルジョン"],
                "brand": "TOUT VERT (トゥヴェール)",
                "name": "ナノエマルジョン 50mL (浸透湿潤セラミド10%高濃度配合・粒子をナノ化することで水のようにサラサラなのに圧倒的な保護膜をつくる浸透乳液)"
            },
            {
                "rank": 7,
                "queries": ["カルテHD モイスチュア エマルジョン 120ml", "カルテHD エマルジョン 120ml", "カルテHD モイスチュア エマルジョン"],
                "brand": "Carte HD (カルテHD)",
                "name": "モイスチュア エマルジョン 120mL (保水有効成分ヘパリン類似物質HD×セラミド類似ポリマー配合・まろやかな感触で冬の深刻なカサつきを包み込む高保湿乳液)"
            },
            {
                "rank": 8,
                "queries": ["セザンヌ 濃密スキンコンディショナー ミルク", "セザンヌ スキンコンディショナー ミルク 410ml", "セザンヌ セラミド 乳液"],
                "brand": "CEZANNE (セザンヌ)",
                "name": "濃密スキンコンディショナー ミルク 410mL (ヒト型セラミド3種×ヒアルロン酸配合・全身にも惜しみなく使えるコスパ最強の高保湿セラミド乳液)"
            },
            {
                "rank": 9,
                "queries": ["アルージェ トラブルリペア リキッド", "アルージェ モイスト トリートメント ジェル", "アルージェ エマルジョン"],
                "brand": "Arouge (アルージェ)",
                "name": "モイスト トリートメント ジェル 50mL (天然セラミドをナノ粒子化して配合・敏感肌のバリアを整えふっくらとしたなめらか肌へ導く薬用ジェル乳液)"
            },
            {
                "rank": 10,
                "queries": ["ラロッシュポゼ トレリアン ダーマアレルゴ ライトクリーム", "ラロッシュポゼ トレリアン センシティブ フルイド", "ラロッシュポゼ トレリアン フルイド"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "トレリアン センシティブ フルイド 40mL (ナイアシンアミド×ターマルウォーター×セラミド類似成分配合・超敏感肌にも優しい軽やか高保湿乳液)"
            }
        ]
    },
    "winter_night_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10",
        "file": "winter-night-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エスティローダー ナイトリペア 50ml", "エスティローダー アドバンス ナイト リペア 50ml", "アドバンス ナイト リペア SMR コンプレックス 50ml"],
                "brand": "Estée Lauder (エスティ ローダー)",
                "name": "アドバンス ナイト リペア SMR コンプレックス 50mL (独自の夜間修復テクノロジー搭載・睡眠中の肌再生リズムにアプローチし翌朝劇的なふっくら弾力を叶える世界的人気セラム)"
            },
            {
                "rank": 2,
                "queries": ["コスメデコルテ リポソーム ナイトクリーム 50g", "コスメデコルテ リポソーム アドバンスト リペアセラム 50ml", "コスメデコルテ リポソーム リペアセラム 50ml"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアセラム 50mL (1滴に1兆個のナイトバイオリポソームを凝縮・睡眠中の角層深部へ潤いと美容成分を持続放出し続ける最高峰ナイト美容液)"
            },
            {
                "rank": 3,
                "queries": ["イヴサンローラン ピュアショット ナイトセラム 30ml", "YSL ピュアショット ナイトセラム 30ml", "ピュアショット ナイトセラム"],
                "brand": "YVES SAINT LAURENT (イヴ・サンローラン)",
                "name": "ピュアショット ナイトセラム 30mL (モロッコ産ムーンライトカクタス×グリコール酸の二層式・寝ている間に日中の酸化ダメージをリセットし翌朝つるんとなめらかな発光肌へ導く名品)"
            },
            {
                "rank": 4,
                "queries": ["クラランス ダブル セーラム EX 50ml", "クラランス ダブルセーラム 50ml", "ダブル セーラム EX 50ml"],
                "brand": "CLARINS (クラランス)",
                "name": "ダブル セーラム EX 50mL (水分7:油分3の黄金比率・21種の厳選植物エキスが夜間の細胞活性を底上げし真冬のしぼみ肌に濃密なハリと艶を吹き込むエイジングケア美容液)"
            },
            {
                "rank": 5,
                "queries": ["キールズ ミッドナイト ボタニカル コンセントレート 30ml", "キールズ ミッドナイト 30ml", "キールズ ボタニカル コンセントレート 30ml"],
                "brand": "KIEHL'S (キールズ)",
                "name": "ミッドナイト ボタニカル コンセントレート 30mL (イブニングプリムローズ×スクワラン×ラベンダー精油・寝ている間の水分蒸散を防ぎ翌朝モチモチの柔らか肌へ整える夜用オイルセラム)"
            },
            {
                "rank": 6,
                "queries": ["魔女工場 ビフィダ バイオーム コンプレックス アンプル 50ml", "魔女工場 ビフィダ アンプル 50ml", "manyo ビフィダ アンプル"],
                "brand": "manyo (魔女工場)",
                "name": "ビフィダ バイオーム コンプレックス アンプル 50mL (高純度ビフィズス菌発酵溶解質×ペプチド・夜間の肌バリアを集中補強し寒冷刺激によるゴワつきや弾力低下を根本からリカバリー)"
            },
            {
                "rank": 7,
                "queries": ["ミシャ ナイトレボリューション アンプル 5X", "ミシャ 紫 アンプル 50ml", "MISSHA ナイトレボリューション"],
                "brand": "MISSHA (ミシャ)",
                "name": "タイム レボリューション ナイトリペア アンプル 5X 50mL (極限発酵を経た10種の発酵成分を配合・冬の寝室の乾燥に負けず翌朝までリッチな潤いと弾力をキープする韓国ロングセラー)"
            },
            {
                "rank": 8,
                "queries": ["アテニア ナイトエステセラム", "アテニア ミッドナイトモイスチャライザー 30g", "アテニア ミッドナイト"],
                "brand": "Attenir (アテニア)",
                "name": "ミッドナイトモイスチャライザー 30g (時計美容理論から生まれた夜用美容マスクセラム・冬の就寝中の肌再生ピークに合わせた成分が翌朝ぷるんとした弾力肌を再生)"
            },
            {
                "rank": 9,
                "queries": ["オバジ ダーマパワーX ステムリフト セラム 50ml", "オバジ ステムリフト セラム 50ml", "オバジ ダーマパワー セラム"],
                "brand": "Obagi (オバジ)",
                "name": "ダーマパワーX ステムリフト セラム 50mL (コラーゲン×エラスチン×独自ステムビルドコンプレックス・夜のスキンケアで角層深部から押し上げるようなピンとしたハリをチャージ)"
            },
            {
                "rank": 10,
                "queries": ["アヌア スノーカーミング セラム", "アヌア ナイトセラム", "VT リードルショット 100 50ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルショット 100 50mL (天然マイクロニードル×CICA成分配合・夜の洗顔直後に導入することで角層深部へ美容成分の通り道をつくり翌朝の肌キメと浸透力を劇的改善)"
            }
        ]
    },
    "winter_eye_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10",
        "file": "winter-eye-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ランコム ジェニフィック アドバンスト ライトパール 20ml", "ランコム アイセラム 20ml", "ジェニフィック ライトパール 20ml"],
                "brand": "LANCÔME (ランコム)",
                "name": "ジェニフィック アドバンスト ライトパール 20mL (360°しなやかに回転するアプリケーター×美肌菌発酵エキス・真冬の血行不良と乾燥小ジワを瞬時にほぐし潤いで満たすアイセラム)"
            },
            {
                "rank": 2,
                "queries": ["エスティローダー ナイトリペア アイ コンセントレイト 15ml", "エスティローダー アイセラム 15ml", "アドバンス ナイト リペア アイ コンセントレイト SMR"],
                "brand": "Estée Lauder (エスティ ローダー)",
                "name": "アドバンス ナイト リペア アイ コンセントレイト SMR コンプレックス 15mL (微細振動アプリケーター付き・冬のまばたき摩擦や暖房乾燥から目元の薄い皮膚を密着シールドする濃密セラム)"
            },
            {
                "rank": 3,
                "queries": ["クラランス グラン アイ セラム V 15ml", "クラランス アイセラム 15ml", "グラン アイ セラム V 15ml"],
                "brand": "CLARINS (クラランス)",
                "name": "グラン アイ セラム V 15mL (厳選植物エキス×クーリングメタルアプリケーター・冬の寒さでむくみや乾燥くすみが起きやすい目元をすっきりと引き締め潤す名品アイセラム)"
            },
            {
                "rank": 4,
                "queries": ["ディオール カプチュール トータル セル ENGY アイ セラム 20ml", "ディオール アイセラム 20ml", "カプチュール トータル アイ セラム 20ml"],
                "brand": "Dior (ディオール)",
                "name": "カプチュール トータル セル ENGY アイ セラム 20mL (ロンゴザエキス×微細浸透技術・波型の専用マッサージヘッドでデリケートな目元のハリと水分密度を同時に高める高機能セラム)"
            },
            {
                "rank": 5,
                "queries": ["クリニーク オール アバウト アイ セラム 15ml", "クリニーク アイセラム 15ml", "オール アバウト アイ セラム 15ml"],
                "brand": "CLINIQUE (クリニーク)",
                "name": "オール アバウト アイ セラム 15mL (ひんやり心地よいローラーボール式・冬の暖房で火照り乾燥した目元を瞬時にクールダウンしながらみずみずしい潤いを与え続けるアイ美容液)"
            },
            {
                "rank": 6,
                "queries": ["ザ レチノタイム リンクルアイセラム", "レチノタイム アイセラム 20g", "レチノタイム リンクルデイミルク"],
                "brand": "THE RETINOTIME (ザ・レチノタイム)",
                "name": "リンクルデイミルク UV / リンクルアイセラム 20g (薬用シワ改善有効成分ナイアシンアミド配合・真冬の目元のちりめんジワを角層深部からふっくらと押し上げる本格派セラム)"
            },
            {
                "rank": 7,
                "queries": ["なめらか本舗 目元ふっくらクリーム 20g", "なめらか本舗 リンクルアイクリーム N 20g", "なめらか本舗 アイクリーム 20g"],
                "brand": "なめらか本舗 (サナ)",
                "name": "目元ふっくらクリーム / リンクルアイクリーム N 20g (豆乳発酵液×ピュアレチノール×ビタミンE誘導体・プチプラとは思えない濃密な潤いで冬の乾燥くすみを一掃)"
            },
            {
                "rank": 8,
                "queries": ["セザンヌ リンクルホワイトアイクリーム", "セザンヌ アイクリーム", "セザンヌ まつげ美容液 EX"],
                "brand": "CEZANNE (セザンヌ)",
                "name": "リンクルホワイトアイクリーム 20g (有効成分ナイアシンアミド配合・シワ改善×美白ケアを同時に叶えながら目元をしっとり保護する驚きのハイコスパ目元美容液)"
            },
            {
                "rank": 9,
                "queries": ["トリデン ダイブイン アイセラム", "Torriden アイセラム", "トリデン セルメイジング アイセラム"],
                "brand": "Torriden (トリデン)",
                "name": "セルメイジング 低分子コラーゲン アイセラム 30mL (5種の低分子コラーゲン×ペプチド配合・繊細な目元の皮膚にスッとなじみ日中のメイク前にもヨレずに使えるぷるぷる水分セラム)"
            },
            {
                "rank": 10,
                "queries": ["コスメデコルテ リポソーム アドバンスト リペアアイセラム 20ml", "コスメデコルテ アイセラム 20ml", "リポソーム リペアアイセラム 20ml"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアアイセラム 20mL (ナノバイセル×多重層バイオリポソームのダブルカプセル配合・乾燥しがちな目元に24時間潤いを放出し続ける目元用濃密美容液)"
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
    
    with open("fetched_3new_winter_ceramide_night_eye.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_winter_ceramide_night_eye.json!")

if __name__ == "__main__":
    fetch_all()
