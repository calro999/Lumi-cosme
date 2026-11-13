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
    "winter_hyaluronic_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！多段分子ヒアルロン酸の圧倒的保水ヴェールと高密着セルロース膜で真冬の暖房脱水肌を満たす保湿力高めヒアルロン酸シートマスクランク10",
        "file": "winter-hyaluronic-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["トリデン ダイブイン マスク 10枚", "Torriden ダイブイン マスク", "トリデン ダイブイン シートマスク"],
                "brand": "Torriden (トリデン)",
                "name": "ダイブイン マスク 10枚入 (5D複合低分子ヒアルロン酸×ヴィーガンセルロースシート・冬の暖房直撃によるインナードライを秒速で水分満タンにする韓国大ヒット水分爆弾マスク)"
            },
            {
                "rank": 2,
                "queries": ["メディヒール NMF マスク 10枚", "MEDIHEAL N.M.F マスク 10枚", "メディヒール アクアリング マスク"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "N.M.F アクアリング アンプルマスク EX 10枚入 (高濃度ヒアルロン酸Na×生体模倣保湿N.M.F・微細竹由来シートが真冬の干からびた角層を密閉集中補水する世界的ロングセラー)"
            },
            {
                "rank": 3,
                "queries": ["ドクタージャルト バイタルハイドラ マスク", "Dr.Jart バイタル ハイドラ ソリューション", "ドクタージャルト 青 マスク"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "バイタル ハイドラ ソリューション 5枚入 (低分子ヒアルロン酸×キシリトール複合体・極細密着ウォータージェットシートが真冬の冷風で水分蒸発した砂漠肌を即座にリセット)"
            },
            {
                "rank": 4,
                "queries": ["ルルルン ハイドラ EX マスク", "ルルルン ハイドラ EX 28枚", "ルルルン ハイドラ EX 7枚"],
                "brand": "LuLuLun (ルルルン)",
                "name": "ルルルン ハイドラ EX マスク 28枚入 (白玉グルタチオン×多重ヒアルロン酸×セラミド・とろけるメルティシートが真冬のくすみと乾燥つっぱりを同時に晴らす最新デイリーマスク)"
            },
            {
                "rank": 5,
                "queries": ["ダーマレーザー スーパーヒアルロン100", "クオリティファースト ダーマレーザー ヒアルロン酸", "ダーマレーザー 青 マスク"],
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー スーパーヒアルロン100 マスク 7枚入 (高濃度ヒアルロン酸×レーザー美容発想浸透カプセル・シリコンマスク発想の高密着長繊維シートで真冬の角層深部まで一気呵成に送り込む)"
            },
            {
                "rank": 6,
                "queries": ["VT スーパーヒアルロン マスク", "VT ヒアルロン デイリー マスク", "VT スーパーヒアルロン"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "スーパーヒアルロン デイリーモイスチャーマスク 30枚入 (独自G:H8複合ヒアルロン酸×γ-PGA・朝晩惜しみなく使えて真冬のメイクノリを劇的に向上させる高水分アンプルパック)"
            },
            {
                "rank": 7,
                "queries": ["肌ラボ 極潤プレミアム マスク", "極潤 プレミアム ヒアルロン シートマスク", "肌ラボ 極潤 プレミアム パック"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤プレミアム ヒアルロンジュレマスク 4枚入 (8種のヒアルロン酸を美容液ジュレに凝縮・まるでシート状の美容液そのものを貼り付けたような圧倒的濃密保水力)"
            },
            {
                "rank": 8,
                "queries": ["Anua ヒアルロン酸 マスク", "アヌア 水分 マスク 10枚", "Anua アンプル マスク"],
                "brand": "Anua (アヌア)",
                "name": "ヒアルロン酸 水分 アンプルマスク 10枚入 (スマート8重ヒアルロン酸×シリカコンプレックス・油分でフタをする前に角層内の純粋水分量を飽和状態まで引き上げるインナードライ特化型)"
            },
            {
                "rank": 9,
                "queries": ["ウォンジン マスク 10枚", "ウォンジンエフェクト ハイドロバイアル", "Wonjin Effect マスク"],
                "brand": "Wonjin Effect (ウォンジンエフェクト)",
                "name": "ハイドロ バイアル マスク 10枚入 (韓国トップクラス美容外科監修・6重ヒアルロン酸×スキニータッチ医療用ガーゼシートが真冬の赤み・乾燥小ジワを救うクリニック発想マスク)"
            },
            {
                "rank": 10,
                "queries": ["KISO ヒアルロン酸 フェイスマスク 30枚", "KISO マスク ヒアルロン酸 30枚", "KISO ヒアルロン酸 シートマスク"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "プレミアムフェイスマスク HA 30枚入 (高純度ヒアルロン酸Na原液高配合×国産天然コットン100%・香料着色料無添加で冬のゆらぎ肌にも吸い付くように馴染む高コスパサイエンスマスク)"
            }
        ]
    },
    "winter_ceramide_booster": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒト型ナノセラミドの角層柔軟力と先行浸透ブースト処方で真冬の硬直ゴワつき肌を解きほぐす保湿力高めセラミド導入美容液ランク10",
        "file": "winter-ceramide-booster.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アスタリフト ジェリー アクアリスタ 40g", "アスタリフト ジェリー アクアリスタ", "富士フイルム ジェリーアクアリスタ"],
                "brand": "ASTALIFT (富士フイルム アスタリフト)",
                "name": "ジェリー アクアリスタ 40g (世界最小クラスWヒト型ナノセラミド×ナノアスタキサンチン・洗顔直後の素肌に吸い付く自己復元ジェリーが冬の硬化角質を根本から解きほぐす先行美容液の最高峰)"
            },
            {
                "rank": 2,
                "queries": ["エトヴォス アルティモイストセラム", "ETVOS アルティモイストセラム 50ml", "エトヴォス モイスチャライジングセラム 50ml"],
                "brand": "ETVOS (エトヴォス)",
                "name": "アルティモイストセラム 50mL (5種のヒト型セラミド×ナイアシンアミド×ナツメ果実エキス・美容液と乳液の機能を兼ね備え冬の乾燥バリアを瞬時に形成するプレセラム)"
            },
            {
                "rank": 3,
                "queries": ["ワンバイコーセー セラムヴェール 60ml", "ONE BY KOSE セラム ヴェール 60ml", "セラムヴェール ディープリペア 60ml"],
                "brand": "ONE BY KOSÉ (コーセー)",
                "name": "セラム ヴェール ディープリペア 60mL (医薬部外品・肌の水分保持能を改善する有効成分ライスパワー®No.11配合・自らセラミドを作り出す肌へと育てる薬用導入美容液)"
            },
            {
                "rank": 4,
                "queries": ["トワニー タイムリフレッシャー 60ml", "トワニー タイムリフレッシャー", "カネボウ タイムリフレッシャー"],
                "brand": "TWANY (カネボウ トワニー)",
                "name": "タイムリフレッシャー V 60mL (とろみナノエマルジョンが肌表面を包み込み角層をマッサージしながらほぐす・後から使う化粧水をグングン引き込む冬の導入ロングセラー)"
            },
            {
                "rank": 5,
                "queries": ["キュレル ディープモイスチャースプレー 250g", "キュレル スプレー 250g", "キュレル 潤浸保湿 美容液"],
                "brand": "Curel (花王 キュレル)",
                "name": "ディープモイスチャースプレー 250g (医薬部外品・微細化セラミド機能成分が角層深部まで直行・お風呂上がり直後の急激な過乾燥を秒速でブロックする全身先行ミスト)"
            },
            {
                "rank": 6,
                "queries": ["タカミスキンピール 30ml", "タカミ スキンピール 30ml", "TAKAMI スキンピール"],
                "brand": "TAKAMI (タカミ)",
                "name": "タカミスキンピール 30mL (角質美容水・寒さで剥がれ落ちなくなった冬の硬直角質を優しく整えセラミドの自生環境と化粧水の受け入れ態勢を整える毛穴・キメの代名詞)"
            },
            {
                "rank": 7,
                "queries": ["肌をうるおす保湿スキンケア 導入液", "肌をうるおす 保湿浸透水", "松山油脂 肌をうるおす セラミド"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "肌をうるおす 保湿浸透水 モイストリッチ 120mL (大豆由来保湿成分×5種のヒト型セラミド・アルコールフリーで冬の敏感肌にもじんわり吸い込まれる高保湿先行化粧水)"
            },
            {
                "rank": 8,
                "queries": ["エストラ アトバリア365 ハイドロエッセンス", "AESTURA ハイドロエッセンス", "エストラ ハイドロエッセンス"],
                "brand": "AESTURA (アトバリア365)",
                "name": "ハイドロエッセンス 150mL (微細セラミドカプセル×30種のアミノ酸生体水分・化粧水前の肌にセラミドネットワークを張り巡らせる韓国メディカルダーマの傑作)"
            },
            {
                "rank": 9,
                "queries": ["KISO セラミド 原液", "KISO エッセンス CE", "基礎化粧品研究所 セラミド 原液"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "エッセンス CE 20mL (ヒト型セラミド原液ナノエマルジョン・洗顔後の無防備な角層に原液そのままを届けて細胞間脂質をダイレクトに補強するサイエンスブースター)"
            },
            {
                "rank": 10,
                "queries": ["セザンヌ スキンコンディショナー高保湿", "セザンヌ セラミド 化粧水", "セザンヌ 濃密スキンコンディショナー"],
                "brand": "CEZANNE (セザンヌ)",
                "name": "スキンコンディショナー高保湿 500mL (ヒト型セラミド3種×ハトムギエキス×ヒアルロン酸・大容量で惜しみなくバシャバシャ全身に使える冬の神コスパプレ導入ローション)"
            }
        ]
    },
    "winter_collagen_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！超低分子生コラーゲンの高密度ホールド膜と弾力ペプチド処方で真冬の寒冷肌痩せ・たるみ毛穴を押し上げる保湿力高めコラーゲン美容液ランク10",
        "file": "winter-collagen-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["メディキューブ コラーゲングロウセラム", "メディキューブ コラーゲン セラム", "medicube コラーゲン 美容液"],
                "brand": "medicube (メディキューブ)",
                "name": "トリプル コラーゲン セラム 55mL (超低分子加水分解コラーゲン×アテロコラーゲン・冬の寒風でしぼんだ肌にガラス玉のような圧倒的水光ツヤと濃密な押し返し弾力を注入する韓国リフトセラム)"
            },
            {
                "rank": 2,
                "queries": ["魔女工場 コラーゲン セラム", "魔女工場 Vコラーゲン セラム", "Manyo コラーゲン アンプル"],
                "brand": "魔女工場 (Manyo Factory)",
                "name": "Vコラーゲン ハートフィット セラム 50mL (植物性ヴィーガンコラーゲン×シロキクラゲ多糖体・リポソームカプセルが冬の寒さで開いたたるみ毛穴をキュッと引き締めるヴィーガン弾力美容液)"
            },
            {
                "rank": 3,
                "queries": ["アスタリフト エッセンス デスティニー 30ml", "アスタリフト エッセンス デスティニー", "アスタリフト 美容液 30ml"],
                "brand": "ASTALIFT (富士フイルム アスタリフト)",
                "name": "エッセンス デスティニー 30mL (3種の機能性コラーゲン×高濃度ナノアスタキサンチン×レスベラトロール・真冬の寒冷たるみ肌を根本から引き上げる濃密赤のエイジング美容液)"
            },
            {
                "rank": 4,
                "queries": ["ドクターシーラボ デュオセラム", "ドクターシーラボ メディカリフト デュオセラム", "シーラボ デュオセラム 26ml"],
                "brand": "Dr.Ci:Labo (ドクターシーラボ)",
                "name": "エンリッチ メディカリフト デュオセラム 26mL (純粋レチノールオイル層×超低分子浸透コラーゲンエッセンス層・2層を振って混ぜることで冬の深い乾燥溝とハリ不足に同時アタック)"
            },
            {
                "rank": 5,
                "queries": ["ファンケル コアエフェクター 18ml", "ファンケル コアエフェクター", "FANCL コアエフェクター"],
                "brand": "FANCL (ファンケル)",
                "name": "コアエフェクター 18mL (40年の研究から生まれたチオレドキシン×低分子生コラーゲン配合・真冬の過酷な環境で低下した真皮のハリ土台に直接働きかける最高峰プレセラム)"
            },
            {
                "rank": 6,
                "queries": ["VT コラーゲン リードルショット 100", "VT コラーゲン リードルショット", "リードルショット コラーゲン"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "コラーゲン リードルショット 100 50mL (超微細天然美容針CICA REEDLE™×低分子コラーゲン・冷気で硬化した冬の角層を針がチクチク通り抜けコラーゲンを深部へダイレクト注入)"
            },
            {
                "rank": 7,
                "queries": ["ドクターペプチ ペプチドボリュームエッセンス 100ml", "ドクターペプチ ボリュームエッセンス", "DR.PEPTI ボリュームエッセンス"],
                "brand": "DR.PEPTI (ドクターペプチ)",
                "name": "ペプチド ボリューム マスター エッセンス 105mL (酸素マイクロ炭酸泡×フランス産ボルフィリン×超微細コラーゲン・肌の上でプチプチ弾ける泡が真冬のしぼみ肌をふっくら持ち上げる泡美容液)"
            },
            {
                "rank": 8,
                "queries": ["エチュード モイストフル コラーゲン エッセンス", "エチュードハウス モイストフル コラーゲン", "モイストフル コラーゲン エッセンス"],
                "brand": "ETUDE (エチュード)",
                "name": "モイストフル コラーゲン エッセンス 80mL (超微細スーパーコラーゲン™ウォーター×ホワイトルピナスエキス・ゼリーのようなみずみずしいテクスチャーが冬の肌に吸い付くベストセラー)"
            },
            {
                "rank": 9,
                "queries": ["KISO コラーゲン 原液", "KISO エッセンス CL", "基礎化粧品研究所 コラーゲン 原液"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "エッセンス CL 20mL (高純度マリン加水分解コラーゲン原液・不純物を極限まで排した低分子コラーゲンが真冬の乾燥小ジワをふっくら押し戻す濃厚ピュアエッセンス)"
            },
            {
                "rank": 10,
                "queries": ["ネイチャーリパブリック コラーゲン エッセンス", "コラーゲンドリーム 70 エッセンス", "ネイチャーリパブリック コラーゲンドリーム"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "コラーゲンドリーム 70 エッセンス 40mL (ハワイコナ海洋深層水×マリンコラーゲン70%超高配合×アサイーベリー・冬の乾燥で失われたハリ・ツヤを一瞬で満たす濃密弾力セラム)"
            }
        ]
    }
}

def extract_image_url(cand):
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    if isinstance(first, dict):
        raw = first.get("imageUrl", "")
    else:
        raw = str(first)
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

def fetch_all():
    results = {}
    total_fetched = 0
    total_expected = 30
    
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title'][:40]}...)")
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
                img_url = extract_image_url(chosen_item)
                print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                print(f"     Image URL: {img_url}")
                
                aff_url = chosen_item.get("affiliateUrl") or chosen_item.get("itemUrl")
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": aff_url,
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "4.8"))
                })
                total_fetched += 1
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_hyaluronic_ceramide_collagen.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_hyaluronic_ceramide_collagen.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print(f"⚠️ Warning: Only {total_fetched}/30 items fetched.")

if __name__ == "__main__":
    fetch_all()
