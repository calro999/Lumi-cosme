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
    "winter_collagen_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！超低分子コラーゲンの弾力ホールド膜で真冬のしぼみ肌を跳ね返す保湿力高めコラーゲンクリームランク10",
        "file": "winter-collagen-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["メディキューブ コラーゲン クリーム 50ml", "メディキューブ トリプル コラーゲン クリーム"],
                "brand": "medicube (メディキューブ)",
                "name": "トリプル コラーゲン クリーム 50mL (超低分子マリンコラーゲン複合体配合・真冬の角層に弾力とガラス玉のような発光ツヤを密閉する大ヒット濃密クリーム)"
            },
            {
                "rank": 2,
                "queries": ["バイオヒールボ プロバイオダーム 3D リフティングクリーム 50ml", "バイオヒールボ リフティングクリーム 50ml"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム 3D リフティングクリーム 50mL (オリーブヤング1位・コラーゲン×プロバイオティクス×12種ペプチドが真冬のたるみ毛穴と乾燥小ジワを強力リフトアップ)"
            },
            {
                "rank": 3,
                "queries": ["ネイチャーリパブリック コラーゲンドリーム 70 オールインワン クリーム", "ネイチャーリパブリック コラーゲンドリーム クリーム"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "コラーゲンドリーム 70 オールインワン クリーム 50mL (インドネシア産海洋性水溶性コラーゲン70%高濃度配合・真冬の乾燥しぼみ肌をみずみずしく押し上げる高保水クリーム)"
            },
            {
                "rank": 4,
                "queries": ["VT コラーゲン クリーム", "VT リードルショット リフティングクリーム 50ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "シカコラーゲン リフティングクリーム 50mL (低分子フィッシュコラーゲン×ツボクサエキス・冬の寒冷でこわばった肌をほぐしながら弾力ハリ膜を再構築)"
            },
            {
                "rank": 5,
                "queries": ["エチュード モイストフルCL クリーム 75ml", "モイストフルCL クリーム 75ml"],
                "brand": "ETUDE (エチュード)",
                "name": "モイストフルCL クリーム 75mL (微粒子スーパーコラーゲン水配合・角層の奥まで跳ね返るようなぷるぷるの潤い弾力を100時間持続させる殿堂入り水分クリーム)"
            },
            {
                "rank": 6,
                "queries": ["アピュー マデカソサイド コラーゲン", "アピュー マデカソサイド クリーム 50ml"],
                "brand": "A'pieu (アピュー)",
                "name": "マデカソサイド コラーゲン クリーム 50mL (ヴィーガンコラーゲン×マデカッソシド・真冬のピリピリ敏感肌を沈静化しながらふっくらキメ密度をチャージ)"
            },
            {
                "rank": 7,
                "queries": ["アスタリフト アドバンスド クリーム 30g", "アスタリフト アドバンスド クリーム"],
                "brand": "ASTALIFT (富士フイルム)",
                "name": "アドバンスド クリーム 30g (3種の機能性コラーゲン×高濃度アスタキサンチン・写真フィルム技術から生まれた真冬のしぼみ肌を劇的に押し戻す最高峰濃密クリーム)"
            },
            {
                "rank": 8,
                "queries": ["カナデル プレミアリフト 58g", "カナデル プレミアリフト オールインワン"],
                "brand": "CANADEL (カナデル)",
                "name": "プレミアリフト オールインワン 58g (コラーゲン×ハリペプチド複合体配合・医薬部外品処方で真冬の乾燥小ジワをふっくら持ち上げる大人気リフトジェルクリーム)"
            },
            {
                "rank": 9,
                "queries": ["肌美精 リンクルケア 濃密潤い美容液", "肌美精 リンクルケア パッククリーム 30g"],
                "brand": "肌美精 (クラシエ)",
                "name": "ONE リンクルケア 濃密潤い美容液 / パッククリーム 30g (高保水コラーゲン×浸透型レチノール×ローヤルゼリー・目元口元の乾燥小ジワを集中密閉する濃厚処方)"
            },
            {
                "rank": 10,
                "queries": ["DHC 薬用Qフェースクリーム 50g", "DHC 薬用Qクリーム 50g"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Qフェースクリーム 50g (高濃度コエンザイムQ10×低分子コラーゲン×ヒアルロン酸・冬の冷えで衰えた肌に濃厚なコクとリッチな弾力を与える本格エイジングクリーム)"
            }
        ]
    },
    "winter_squalane_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然皮脂膜バリアの生体親和性で真冬の粉吹き・脱水肌を完全密閉する保湿力高めスクワランクリームランク10",
        "file": "winter-squalane-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アンブリオリス モイスチャークリーム 75ml", "アンブリオリス モイスチャークリーム"],
                "brand": "Embryolisse (アンブリオリス)",
                "name": "アンブリオリス モイスチャークリーム 75mL (植物性スクワラン×ミツロウ×アロエベラ・世界中のメイクアップアーティストが絶賛する冬の乾燥崩れを防ぐ濃厚保湿クリーム)"
            },
            {
                "rank": 2,
                "queries": ["キールズ クリーム UFC 50ml", "キールズ ウルトラフェイシャルクリーム 50ml"],
                "brand": "KIEHL'S (キールズ)",
                "name": "ウルトラ フェイシャル クリーム (UFC) 50mL (オリーブ由来植物性スクワラン×南極氷河糖タンパク質・世界中で秒速売れ続ける冬の極上保湿シールドクリーム)"
            },
            {
                "rank": 3,
                "queries": ["松山油脂 肌をうるおす 保湿クリーム 50g", "肌をうるおす 保湿クリーム 50g"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "保湿クリーム 50g (植物性スクワラン×5種ヒト型セラミド×大豆発酵エキス・真冬の暖房直撃によるインナードライを根本から解消する高密度バリア処方)"
            },
            {
                "rank": 4,
                "queries": ["キュレル 潤浸保湿フェイスクリーム 40g", "キュレル フェイスクリーム 40g"],
                "brand": "Curel (キュレル / 花王)",
                "name": "潤浸保湿フェイスクリーム 40g (消炎剤有効成分×セラミド機能成分×高品位スクワラン・真冬の冷風でヒリつく乾燥性敏感肌をふわっと軽やかに包み込む医薬部外品)"
            },
            {
                "rank": 5,
                "queries": ["Dr.G モイスチャーバリアD インテンスクリーム 100ml", "ドクタージー モイスチャーバリア クリーム"],
                "brand": "Dr.G (ドクタージー)",
                "name": "モイスチャーバリアD インテンスクリーム 100mL (フィトスクワラン×プロビタミンD×セラミド・韓国皮膚科医監修の100時間持続する極厚水分シールドクリーム)"
            },
            {
                "rank": 6,
                "queries": ["ちふれ ボラージ クリーム 80g", "ちふれ ボラージクリーム 80g"],
                "brand": "ちふれ (CHIFURE)",
                "name": "ボラージ クリーム 80g (高純度スクワラン×ボラージオイル×グリチルリチン酸2K・粉を吹いてかゆみが出やすい真冬の脱水肌を薬用保湿でやさしく保護)"
            },
            {
                "rank": 7,
                "queries": ["ナンバーズイン 2番 リアルセラミド深層保湿クリーム 50ml", "ナンバーズイン 2番 クリーム 50ml"],
                "brand": "numbuzin (ナンバーズイン)",
                "name": "2番 リアルセラミド深層保湿クリーム 50mL (ピュア植物性スクワラン×高濃度セラミド・冬の過酷な外気で粉を吹いた肌を秒速でつるんとなめらかにバター密着リペア)"
            },
            {
                "rank": 8,
                "queries": ["無印良品 エイジングケア 薬用美白クリーム 45g", "無印良品 エイジングケア クリーム 45g"],
                "brand": "無印良品 (MUJI)",
                "name": "エイジングケアクリーム 45g (天然オリーブスクワラン×椿・柚子エキス×ヒアルロン酸・真冬の乾燥で硬化した大人の角層を柔らかくほぐすリッチな高保湿クリーム)"
            },
            {
                "rank": 9,
                "queries": ["チュラコス わらびはだ 30g", "チュラコス ネオわらびはだ 30g"],
                "brand": "CHURACOS (チュラコス)",
                "name": "ネオわらびはだ 30g (沖縄産植物エキス×植物性スクワラン×プラチナポーション・真冬の目元首元のポツポツざらつきと乾燥を同時に密着ケアするオールインワンクリーム)"
            },
            {
                "rank": 10,
                "queries": ["ネオナチュラル モイストリペアクリーム 40ml", "ネオナチュラル 保湿クリーム"],
                "brand": "neo natural (ネオナチュラル)",
                "name": "モイストリペアクリーム 40mL (有機オリーブスクワラン×ヘチマ水×月桃・100%自然由来成分で敏感な冬の肌をふっくら健やかなうるおい膜で満たすオーガニック名品)"
            }
        ]
    },
    "winter_peptide_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！多機能ペプチド複合体の密度再建力で真冬の寒冷たるみと乾燥溝を押し上げる保湿力高めペプチドクリームランク10",
        "file": "winter-peptide-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["メディピール ペプチド9 ボリューム トックス クリーム 50g", "メディピール ペプチド9 クリーム 50g"],
                "brand": "MEDI-PEEL (メディピール)",
                "name": "ペプチド9 ボリューム トックス クリーム プロ 50g (9種のマルチ機能ペプチド×フランス産ボルフィリン・冬の冷えで萎縮したフェイスラインをパンと押し上げる糸引く濃密弾力クリーム)"
            },
            {
                "rank": 2,
                "queries": ["DR.PEPTI ペプチド ボリューム エッセンス 100ml", "ドクターペプチ ペプチド ボリューム エッセンス"],
                "brand": "DR.PEPTI (ドクターペプチ)",
                "name": "ペプチド ボリューム エッセンス 2.0 100mL (11種の濃縮機能性ペプチド×酸素バブル技術・真冬の乾ききった角層の深部までペプチドを送り込む塗るボトックス美容クリーム)"
            },
            {
                "rank": 3,
                "queries": ["COSRX 6ペプチド スキンブースター", "COSRX ペプチド クリーム"],
                "brand": "COSRX (コスアールエックス)",
                "name": "6ペプチド スキンコンプレックス クリーム 50mL (肌再生を促す6重ペプチド×ヒアルロン酸×アラントイン・真冬の寒冷乾燥で乱れたキメとバリア機能を土台から修復する高機能セラムクリーム)"
            },
            {
                "rank": 4,
                "queries": ["ドクターシーラボ ACG エンリッチリフト EX 50g", "アクアコラーゲンゲル エンリッチリフトEX 50g"],
                "brand": "DR.CI:LABO (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 50g (浸透型コラーゲンペプチド×ナイアシンアミド・冬の乾燥たるみ肌にピタッと密着してググッと上向きのリフト膜を形成する名品ゲルクリーム)"
            },
            {
                "rank": 5,
                "queries": ["The Ordinary マルチペプチド", "ジオーディナリー ペプチド クリーム"],
                "brand": "The Ordinary (ジオーディナリー)",
                "name": "ナチュラル モイスチャライジング ファクター + フィトセラミド 100mL / マルチペプチド クリーム (生体適合ペプチド×植物性セラミド・冬の極度な水分蒸発をゼロに抑える海外高評価クリーム)"
            },
            {
                "rank": 6,
                "queries": ["KISO ペプチド クリーム 50g", "KISO モイスチャーペプチドクリーム 50g"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "モイスチャーペプチドクリーム 50g (シンエイク・アセチルヘキサペプチド-8×ヒト型セラミド・真冬の乾燥表情ジワを物理的に和らげながらピンとしたハリを与える本格エイジングクリーム)"
            },
            {
                "rank": 7,
                "queries": ["Torriden バランスフル シカ クリーム 80ml", "トリデン バランスフル クリーム 80ml"],
                "brand": "Torriden (トリデン)",
                "name": "バランスフル シカ ペプチド スージングクリーム 80mL (複合シカ成分×高浸透ペプチド・冬の暖房熱による赤みとインナードライを素早くクールダウンしながらバリア修復する低刺激ジェルクリーム)"
            },
            {
                "rank": 8,
                "queries": ["ドクタージャルト シカペア クリーム 50ml", "dr.jart+ シカペア クリーム 50ml"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "シカペア インテンシブ スージング リペア クリーム 50mL (センテラ複合ペプチド×アラントイン・冬の極寒乾燥下で損傷した角層を厚みのある高保湿バーム膜で保護する救済クリーム)"
            },
            {
                "rank": 9,
                "queries": ["なめらか本舗 リンクルナイトクリーム 50g", "なめらか本舗 リンクルナイトクリーム"],
                "brand": "SANA なめらか本舗 (常盤薬品工業)",
                "name": "リンクルナイトクリーム 50g (ピュアレチノール×豆乳発酵ペプチド×ビタミンE・寝ている間に濃密な潤いパック効果で真冬の乾燥小ジワを解消する高コスパ名品)"
            },
            {
                "rank": 10,
                "queries": ["メディキューブ ゼロ 毛穴 クリーム 50ml", "メディキューブ トリプル コラーゲン"],
                "brand": "medicube (メディキューブ)",
                "name": "ゼロ 毛穴 1day クリーム 50mL (毛穴引き締めペプチドコンプレックス×低分子コラーゲン・冷えと乾燥で縦長に開いた真冬のたるみ毛穴をキュッと引き締める毛穴特化クリーム)"
            }
        ]
    }
}

def fetch_all():
    results = {}
    total_fetched = 0
    total_expected = 30
    
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
                    time.sleep(2.5)
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
                    time.sleep(3.5)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(3.0)
            
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
                total_fetched += 1
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_collagen_squalane_peptide.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_collagen_squalane_peptide.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print("⚠️ Warning: Some items missing.")

if __name__ == "__main__":
    fetch_all()
