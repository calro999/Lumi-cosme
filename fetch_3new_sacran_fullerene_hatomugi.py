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
    "winter_sacran": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の約10倍の驚異的保水膜が真冬のエアコン暖房による砂漠化インナードライ肌を救う高保湿サクラン（スイゼンジノリ多糖体）コスメランク10",
        "file": "winter-sacran.html",
        "items": [
            {
                "rank": 1,
                "query": "サクラン原液 ナチュドール 20mL",
                "brand": "NATUDOR (ナチュドール)",
                "name": "サクラン原液 20mL (熊本県阿蘇水系の希少藍藻スイゼンジノリから抽出された純度100%原液・ヒアルロン酸の約10倍の保水力で冬のエアコン暖房下でも角層水分をがっちり掴んで離さない高純度モイスチャー美容液)"
            },
            {
                "rank": 2,
                "query": "ピアベルピア Qモイスト 50ml",
                "brand": "Piabelpia (ピアベルピア)",
                "name": "Qモイスト 50ml (スイゼンジノリ多糖体×コエンザイムQ10×ヒアルロン酸配合・乾燥性敏感肌のために開発された高保水美容液・真冬の寒風でゴワつく角層を柔軟にほぐし、吸い付くようなモチ肌へ導く)"
            },
            {
                "rank": 3,
                "query": "MAIKO マイコ モイスチャーローション",
                "brand": "MAIKO (マイコ)",
                "name": "モイスチャーローション 120ml (新成分サクラン高配合・京都生まれの上質和漢ローション・分子量1600万の巨大多糖体ヴェールが肌表面に第二の皮膚を形成し、冬の過酷な乾燥気流を完全ブロック)"
            },
            {
                "rank": 4,
                "query": "スイゼンジノリ サクラン 化粧水 しっとり",
                "brand": "たっぷりサクラン",
                "name": "スイゼンジノリ サクラン 化粧水 しっとり 500ml (大容量高保湿ローション・スイゼンジノリ多糖体×植物エキス配合・惜しみなく全身にバシャバシャ使える高保水化粧水で真冬の粉吹き肌を瞬時にリセット)"
            },
            {
                "rank": 5,
                "query": "デュフラ フィトフォース オーガニック",
                "brand": "DIEUFRA (デュフラ フィトフォース)",
                "name": "オーガニック デュフラ モイストローション (オーガニック認証植物エキス×スイゼンジノリ多糖体配合・プロ仕様サロン専売化粧水・乾燥によるキメの乱れや毛穴の開きをしっとり整える)"
            },
            {
                "rank": 6,
                "query": "サクラン スカルプケアマスク 200g",
                "brand": "Gracia (グラシア)",
                "name": "サクラン スカルプケアマスク 200g (スイゼンジノリ多糖体×濃密リペア成分配合・冬の暖房や静電気で乾燥する頭皮と毛髪を同時に集中保湿・根元からふんわり立ち上がるしなやかな美髪へ)"
            },
            {
                "rank": 7,
                "query": "スイゼンジノリ サクラン 化粧品 オールインワン",
                "brand": "たっぷりサクラン",
                "name": "スイゼンジノリ サクラン オールインワンゲル 250g (1本で化粧水・乳液・美容液・クリーム・パックの5役・サクランの自己修復ヴェールが忙しい冬の朝晩も潤い密封を持続させる多機能ゲル)"
            },
            {
                "rank": 8,
                "query": "ライフセラ サクライズ 化粧液",
                "brand": "LifeCella (ライフセラ / 久光製薬)",
                "name": "サクライズ 化粧液 100ml (高濃保水サクラン×低分子ヒアルロン酸配合・製薬会社が開発した高機能濃密化粧液・肌の水分保持能を根本からサポートし、冬の砂漠肌を満たす)"
            },
            {
                "rank": 9,
                "query": "おひさまでつくった化粧水 150mL",
                "brand": "エリデン化粧品",
                "name": "おひさまでつくった化粧水 150mL (スイゼンジノリ多糖体×植物セラミド配合・無香料・無着色・鉱物油フリーの敏感肌設計・冬の冷えや乾燥でバリアが弱った肌に優しい弱酸性モイスチャー)"
            },
            {
                "rank": 10,
                "query": "サクラン 30ml 化粧品原料",
                "brand": "自然化粧品研究所 / スキンケア原料",
                "name": "サクラン（スイゼンジノリ多糖体液） 30ml (プロ用コスメ原料グレード・手持ちの化粧水や乳液に1〜2滴ブレンドするだけで真冬の極上プレミアム高保湿コスメへとアップグレードできる原液)"
            }
        ]
    },
    "winter_fullerene": {
        "title": "保湿力の強さで肌乾燥とさようなら！ビタミンCの250倍の抗酸化力と持続型水分保持膜が真冬の寒冷酸化枯れ肌としぼみ小ジワを救い出す高保湿フラーレンコスメランク10",
        "file": "winter-fullerene.html",
        "items": [
            {
                "rank": 1,
                "query": "チューンメーカーズ フラーレン 10ml",
                "brand": "TUNEMAKERS (チューンメーカーズ)",
                "name": "フラーレン原液 10ml (水溶性フラーレン高濃度配合・真冬の紫外線・寒冷ストレス・暖房気流による酸化ダメージを徹底消去・角層のラメラ液晶を守り抜いて乾燥小ジワを防ぐ集中美容液)"
            },
            {
                "rank": 2,
                "query": "KISO 水溶性フラーレン 10%",
                "brand": "KISO (キソ)",
                "name": "モイスチャーセラムRS 20ml (国内最高水準の水溶性フラーレン10%配合・ビタミンC誘導体×プロテオグリカン黄金比ブレンド・真冬のくすみとインナードライを跳ね返す高濃度原液美容液)"
            },
            {
                "rank": 3,
                "query": "エッセンスセレクトゲル トゥヴェール",
                "brand": "TOUT VERT (トゥヴェール)",
                "name": "エッセンスセレクトゲル 100g (規定値以上フラーレン×ヒト型セラミド5種×持続型ペプチド配合・真冬の寒冷でしぼみ切った肌密度を立て直す最高峰エイジングケアオールインワン)"
            },
            {
                "rank": 4,
                "query": "ビューティーモール フラーレン CCクリーム",
                "brand": "BEAUTY MALL (ビューティーモール)",
                "name": "APPS+E(TPNa) フラーレンCCクリーム 20g (高浸透ビタミンC誘導体APPS×リポフラーレン配合・冬の乾燥崩れを完全に防ぎ、日中の暖房下でもツヤと潤いを保ち続ける高機能ベース)"
            },
            {
                "rank": 5,
                "query": "BMモイストFクリーム フラーレン",
                "brand": "BEAUTY MALL (ビューティーモール)",
                "name": "BMモイストFクリーム 30g (ダブルフラーレン×ビタミンAレチノールカプセル高配合・リッチなエモリエント膜が真冬の夜の水分蒸散をブロックし、翌朝ピンと張ったハリ肌へ導く濃密クリーム)"
            },
            {
                "rank": 6,
                "query": "ビノワ パーフェクトコラーゲンゲル エンリッチド 100g",
                "brand": "Vinowa (ビノワ)",
                "name": "パーフェクトコラーゲンゲル エンリッチド 100g (フラーレン×トリプルコラーゲン×ヒアルロン酸配合・こっくり濃厚なゲルが乾燥小ジワを目立たなくし、真冬の肌に潤いヴェールを密着させる)"
            },
            {
                "rank": 7,
                "query": "フラーレン 美容液 原液 30ml",
                "brand": "自然化粧品研究所 / 原液シリーズ",
                "name": "高濃度フラーレン原液 美容液 30ml (ラジカルスポンジ高配合・植物由来多糖体ブレンド・角層の深部まで抗酸化パワーを届け、冬特有の夕方のくすみやパサつきを寄せ付けないピュアエッセンス)"
            },
            {
                "rank": 8,
                "query": "フラーレン フェイスマスク",
                "brand": "ARTISTIC&CO. (アーティスティックアンドシーオー)",
                "name": "PE ザ クイーン ゴールデンビューティーマスク 5枚入 (フラーレン×ツバメの巣エキス×生セラミド配合・エステサロン発の最高峰プレミアム密着マスク・冬の特別な日の前夜に使う極上ケア)"
            },
            {
                "rank": 9,
                "query": "ラクトリーアイ 目元用クリーム",
                "brand": "en-team (エンチーム)",
                "name": "ラクトリーアイ 15g (高純度フラーレン×乳酸菌生産物質配合・冬の寒さと乾燥で血行不良になりがちな目元のクマ・小ジワ・乾燥まぶたをふっくら持ち上げる目元専用エイジングクリーム)"
            },
            {
                "rank": 10,
                "query": "ラブミータッチ ラブミーリップス",
                "brand": "Lov me Touch (ラブミータッチ)",
                "name": "ラブミーリップス 2.0 (上原恵理医師監修・高純度リポフラーレン×ボリュームアップペプチド配合・真冬の寒風でガサガサに皮むけする唇をふっくら縦ジワレスに整える濃密リップ美容液)"
            }
        ]
    },
    "winter_hatomugi": {
        "title": "保湿力の強さで肌乾燥とさようなら！古来伝承の和漢ヨクイニンが真冬のゴワつく角層を柔軟にほぐし透き通るみずみずしさを宿す高保湿ハトムギコスメランク10",
        "file": "winter-hatomugi.html",
        "items": [
            {
                "rank": 1,
                "query": "ナチュリエ ハトムギ保湿ジェル",
                "brand": "naturie (ナチュリエ / イミュ)",
                "name": "スキンコンディショニングジェル (ハトムギ保湿ジェル) 180g (天然ハトムギエキス高配合・油分に頼らず水分で肌を満たすマイクロゲル構造・冬の暖房乾燥でごわつく角層にみずみずしい保水膜を形成)"
            },
            {
                "rank": 2,
                "query": "セザンヌ 濃密スキンコンディショナー",
                "brand": "CEZANNE (セザンヌ)",
                "name": "濃密スキンコンディショナー 410ml (ヒト型セラミド3種×ハトムギ種子エキス×ヒアルロン酸配合・とろみのある高保湿化粧水が真冬の乾燥肌を濃密ラッピング・弱酸性＆大容量で全身使える名作)"
            },
            {
                "rank": 3,
                "query": "アルビオン スキンコンディショナー 165ml",
                "brand": "ALBION (アルビオン)",
                "name": "薬用スキンコンディショナー エッセンシャル N 165ml (濃縮ハトムギエキス×ハトムギ油配合・医薬部外品・冬の冷えや乾燥による肌荒れ・ゴワつきを防ぎ、澄んだ透明感としなやかな潤いを叶える名品)"
            },
            {
                "rank": 4,
                "query": "雪肌精 化粧水 200ml",
                "brand": "雪肌精 (SEKKISEI / コーセー)",
                "name": "薬用雪肌精 ブライトニング エッセンス ローション 200ml (甘草由来有効成分×国産ハトムギエキス高配合・医薬部外品・冬のくすみと乾燥にアプローチし、みずみずしく透き通るような雪肌へ導く)"
            },
            {
                "rank": 5,
                "query": "ナチュリエ ハトムギ化粧水 500ml",
                "brand": "naturie (ナチュリエ / イミュ)",
                "name": "ハトムギ化粧水 スキンコンディショナー 500ml (天然ハトムギエキス配合・角層への浸透性を極限まで高めた処方・真冬のローションパックや導入保水に最適な国民的ベストセラー化粧水)"
            },
            {
                "rank": 6,
                "query": "肌ラボ 極潤 ハトムギ 泡洗顔",
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤 ハトムギ泡洗顔 160ml (ハトムギエキス×ドクダミエキス×ヒアルロン酸配合・濃密なもっちり泡が真冬の乾燥した素肌を擦らず優しく洗い上げ、キメの整った清潔なすっぴん肌へ整える)"
            },
            {
                "rank": 7,
                "query": "ハトムギ 原液 美容液",
                "brand": "自然化粧品研究所 / 原液シリーズ",
                "name": "ヨクイニンエキス (ハトムギ原液) 美容液 90ml (濃密和漢エキス100%・冬の乾燥で硬化した首元・目元のポツポツ角質粒やザラつきに直接働きかけ、ふっくら滑らかな柔肌へと導く集中美容液)"
            },
            {
                "rank": 8,
                "query": "麗白 ハトムギ ボディミルク 400ml",
                "brand": "麗白 (レイハク / 熊野油脂)",
                "name": "ハトムギ ボディミルク 400ml (天然保湿成分ハトムギエキス×ヒアルロン酸配合・滑らかなエマルジョンが真冬の粉吹きすねや腕全体にスッと伸び広がり、ベタつかず一日中しっとり肌をキープ)"
            },
            {
                "rank": 9,
                "query": "コーセー ソフティモ ハトムギ クレンジング",
                "brand": "softymo (ソフティモ / コーセー)",
                "name": "薬用ホワイト クレンジングウォッシュ (ハトムギ) 190g (ハトムギエキス配合・医薬部外品・クリーミーな微細泡が冬のメイク汚れと毛穴の余分な角質を包み込んで落とし、しっとり洗い上げる洗顔フォーム)"
            },
            {
                "rank": 10,
                "query": "ハトムギ 保湿クリーム",
                "brand": "プラチナレーベル / 熊野油脂",
                "name": "ハトムギ エキス高配合 オールインワン モイスチャークリーム 300g (ハトムギ種子エキス×植物オイル配合・大容量こっくり高保湿クリーム・真冬の就寝前のナイトパックや全身の乾燥ケアに活躍)"
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
            q = item["query"]
            print(f"Rank {item['rank']}: Trying '{q}' ...")
            encoded_q = urllib.parse.quote(q)
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            
            chosen_item = None
            for attempt in range(4):
                try:
                    time.sleep(2.5) # レートリミット回避
                    with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
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
                        else:
                            if attempt == 0 and len(q.split()) > 1:
                                simple_q = q.split()[0]
                                print(f"    Fallback trying '{simple_q}' ...")
                                encoded_q = urllib.parse.quote(simple_q)
                                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                except urllib.error.HTTPError as e:
                    print(f"    HTTP Error {e.code}: {e.reason} (attempt {attempt+1})")
                    time.sleep(5.0)
                except Exception as e:
                    print(f"    Attempt {attempt+1} error: {e}")
                    time.sleep(3.5)
            
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
                    "review_average": chosen_item.get("reviewAverage", "0.0")
                })
            else:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_sacran_fullerene_hatomugi.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_sacran_fullerene_hatomugi.json!")

if __name__ == "__main__":
    fetch_all()
