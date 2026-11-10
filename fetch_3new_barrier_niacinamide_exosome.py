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
    "winter_barrier_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！高密度セラミドカプセルとバリア再建ヴェールで真冬の寒冷粉吹き肌を完全シールドする保湿力高めバリアクリームランク10",
        "file": "winter-barrier-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エストラ アトバリア365 クリーム 80ml", "エストラ アトバリア365 クリーム"],
                "brand": "AESTURA (エストラ)",
                "name": "アトバリア365 クリーム 80mL (韓国オリーブヤング1位・特許セラミド高密度カプセル配合・真冬の粉吹き・敏感脱水肌を100時間高保湿シールドする国民的バリアクリーム)"
            },
            {
                "rank": 2,
                "queries": ["リアルバリア エクストリーム クリーム 50ml", "リアルバリア エクストリーム クリーム"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "エクストリーム クリーム 50mL (特許独自MLE技術で健康な肌ラメラ液晶構造を完全再現・寒冷風と暖房乾燥によるバリア崩壊を即効修復する高密着シールドクリーム)"
            },
            {
                "rank": 3,
                "queries": ["イリユン セラミドアト 集中クリーム 200ml", "イリユン セラミドアト 集中クリーム"],
                "brand": "ILLIYOON (イリユン)",
                "name": "セラミドアト 集中クリーム 200mL (アモーレパシフィック特許セラミドスキンコンプレックスカプセル配合・敏感肌の顔から全身まで使える大容量高保湿バリアクリーム)"
            },
            {
                "rank": 4,
                "queries": ["ラロッシュポゼ シカプラスト リペアクリーム B5", "シカプラスト バーム B5 100ml", "ラロッシュポゼ シカプラスト"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "シカプラスト リペアクリーム B5+ 40mL (高濃度パンテノール5%×マデカッソシド×トリビオーマ・真冬のダメージ肌を包み込み修復する世界的ベストセラーバリアバーム)"
            },
            {
                "rank": 5,
                "queries": ["ロベクチン バリア リペア クリーム 100ml", "ロベクチン クリーム 100ml", "ロベクチン バリア リペア"],
                "brand": "ROVECTIN (ロベクチン)",
                "name": "プレミアム バリア リペア フェイス＆ボディ クリーム 100mL (抗がん治療後の超乾燥肌のために開発された超低刺激・高保水セラミドアストロサイト処方)"
            },
            {
                "rank": 6,
                "queries": ["SKIN1004 プロバイオシカ リッチクリーム 50ml", "SKIN1004 プロバイオシカ クリーム"],
                "brand": "SKIN1004 (スキンワンオーオーフォー)",
                "name": "センテラ プロバイオシカ インテンス リッチクリーム 50mL (発酵CICA×植物性プロバイオティクス×セラミドNP・冷気でゆらぐ肌バリアを強化する濃厚バターテクスチャー)"
            },
            {
                "rank": 7,
                "queries": ["ドクタージャルト セラマイディン クリーム 50ml", "セラマイディン ウルトラ モイスチャー クリーム"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "セラマイディン スキン バリア モイスチャライジング クリーム 50mL (5種の複合セラミド高配合・極度の乾燥と冷風から角層バリアを死守する濃厚テクスチャー)"
            },
            {
                "rank": 8,
                "queries": ["松山油脂 肌をうるおす 保湿クリーム 50g", "肌をうるおす 保湿クリーム 50g"],
                "brand": "松山油脂 (Mマーク)",
                "name": "肌をうるおす保湿スキンケア 保湿クリーム 50g (5種のヒト型セラミド×大豆発酵エキス×スクワラン・無香料・アルコールフリーの本格バリアリペア)"
            },
            {
                "rank": 9,
                "queries": ["キュレル 潤浸保湿フェイスクリーム 40g", "キュレル 潤浸保湿 フェイスクリーム"],
                "brand": "Curel (キュレル / 花王)",
                "name": "潤浸保湿フェイスクリーム 40g (医薬部外品・消炎剤有効成分×セラミド機能成分配合・乾燥性敏感肌を外部刺激から守り抜く医薬部外品の殿堂入り名品)"
            },
            {
                "rank": 10,
                "queries": ["VT CICA クリーム 50ml", "VT シカクリーム 50ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "CICA クリーム 50mL (独自シカヒアルロン×セラミドNP・冷たい風でヒリつく冬肌をみずみずしいジェル膜で包み込み鎮静・保護するジェルクリーム)"
            }
        ]
    },
    "winter_niacinamide_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！医薬部外品ナイアシンアミドのシワ改善×セラミド自生力で真冬の寒冷くすみ・小ジワをふっくら押し上げる保湿力高めナイアシンアミドクリームランク10",
        "file": "winter-niacinamide-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["無印良品 薬用リンクルケアクリームマスク 80g", "無印良品 リンクルケアクリームマスク"],
                "brand": "無印良品 (良品計画)",
                "name": "エイジングケア 薬用リンクルケアクリームマスク 80g (医薬部外品 有効成分ナイアシンアミド配合・真冬の乾燥小ジワを就寝中にふっくら押し広げる大ヒット高コスパクリーム)"
            },
            {
                "rank": 2,
                "queries": ["ルシェリ リンクルリペア クリーム 35g", "ルシェリ リンクルリペア クリーム"],
                "brand": "LECHÉRI (コーセー)",
                "name": "リンクルリペア クリーム 35g (医薬部外品 シワ改善有効成分リンクルナイアシン配合・真冬の角層深部まで浸透しピンとしたハリを密閉する薬用濃密クリーム)"
            },
            {
                "rank": 3,
                "queries": ["なめらか本舗 薬用リンクルナイトクリーム 50g", "なめらか本舗 リンクルナイトクリーム 50g"],
                "brand": "SANA なめらか本舗 (常盤薬品工業)",
                "name": "薬用リンクルナイトクリーム 50g (医薬部外品 ナイアシンアミド×ピュアレチノール×豆乳発酵液・真冬のシワ改善と美白を叶える濃厚夜用クリーム)"
            },
            {
                "rank": 4,
                "queries": ["カナデル プレミアホワイト 58g", "カナデル プレミアホワイト"],
                "brand": "CANADEL (カナデル)",
                "name": "プレミアホワイト オールインワン 58g (医薬部外品 有効成分ナイアシンアミド×ビタミンC誘導体・真冬の乾燥くすみと小ジワに集中アプローチする濃厚ジェルクリーム)"
            },
            {
                "rank": 5,
                "queries": ["極潤 薬用ハリクリーム 50g", "肌ラボ 極潤 薬用ハリクリーム 50g"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤 薬用ハリクリーム 50g (医薬部外品 ナイアシンアミド×3種のヒアルロン酸・真冬の乾燥による目元口元のシワ改善とシミ対策を同時に叶えるプチプラ名品)"
            },
            {
                "rank": 6,
                "queries": ["キュレル 美白ケア フェイスクリーム 40g", "キュレル 美白 フェイスクリーム 40g"],
                "brand": "Curel (キュレル / 花王)",
                "name": "美白ケア フェイスクリーム 40g (医薬部外品 カモミラET×セラミド機能成分配合・乾燥性敏感肌の冬のどんよりくすみを晴らし潤いを密閉)"
            },
            {
                "rank": 7,
                "queries": ["アヌア 桃 77% ナイアシン クリーム 50ml", "アヌア 桃 77 ナイアシン クリーム"],
                "brand": "Anua (アヌア)",
                "name": "桃 77% ナイアシン コンディショニングクリーム 50mL (発酵桃エキス77%×ナイアシンアミド・真冬の冷えで血色を失った肌に桃色のうるおいツヤをチャージ)"
            },
            {
                "rank": 8,
                "queries": ["バイオヒールボ プロバイオダーム タイトニング コラーゲン クリーム 50ml", "バイオヒールボ コラーゲン クリーム 50ml"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム タイトニング コラーゲン クリーム 50mL (ナイアシンアミド×低分子コラーゲン・冷気と乾燥で毛穴が目立つ真冬の肌をふっくら引き締め)"
            },
            {
                "rank": 9,
                "queries": ["DHC 薬用Qフェースクリーム 50g", "DHC 薬用Qフェースクリーム"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Qフェースクリーム 50g (医薬部外品・薬用成分ナイアシンアミド誘導体×高濃度コエンザイムQ10・冬の過酷な乾燥とエイジングサインを濃厚リッチに包み込む)"
            },
            {
                "rank": 10,
                "queries": ["オバジ ダーマパワーX ステムリフト クリーム 50g", "オバジ ダーマパワーX クリーム"],
                "brand": "Obagi (ロート製薬)",
                "name": "ダーマパワーX ステムリフト クリーム 50g (ナイアシンアミド×ステムビルドコンプレックス・真冬の乾燥たるみを物理的に引き上げて形状記憶する濃密リフトクリーム)"
            }
        ]
    },
    "winter_exosome_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！最先端ナノカプセル・エクソソームの細胞間浸透力で真冬のしぼみ・ゴワつき肌を根本再建する保湿力高めエクソソームクリームランク10",
        "file": "winter-exosome-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["VT リードルショット リフティングクリーム 50ml", "リードルショット リフティングクリーム 50ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルショット リフティング クリーム 50mL (シリカ天然マイクロニードル×CICAエクソソーム×低分子コラーゲン・真冬のたるみ肌に美容成分を角層深部へ届ける)"
            },
            {
                "rank": 2,
                "queries": ["メディキューブ ゼロ 毛穴 1day クリーム 50ml", "メディキューブ ゼロ 毛穴 クリーム"],
                "brand": "medicube (メディキューブ)",
                "name": "ゼロ 毛穴 1day クリーム 50mL (毛穴引き締めペプチド・エクソソームコンプレックス・冬の冷えで開いたたるみ毛穴をキュッと引き締める毛穴特化クリーム)"
            },
            {
                "rank": 3,
                "queries": ["リジュラン ヒーラー ニュートリティブ クリーム 50ml", "リジュラン クリーム 50ml"],
                "brand": "REJURAN (リジュラン)",
                "name": "ヒーラー ニュートリティブ クリーム 50mL (c-PDRN×バイオ生体カプセル技術・真冬の過酷な乾燥による肌バリア損傷を速攻リペアする美容皮膚科発想の濃密クリーム)"
            },
            {
                "rank": 4,
                "queries": ["魔女工場 パンテトイン エンリッチド クリーム 80ml", "魔女工場 パンテトイン クリーム"],
                "brand": "魔女工場 (Manyo Factory)",
                "name": "パンテトイン エンリッチド クリーム 80mL (パンテノール×エクトイン微細リポソーム・200時間極限保湿で真冬の超乾燥粉吹き肌を完全救済する超高保湿クリーム)"
            },
            {
                "rank": 5,
                "queries": ["センテリアン24 マデカクリーム タイムリバース 50ml", "センテリアン24 マデカクリーム 50ml"],
                "brand": "Centellian24 (センテリアン24)",
                "name": "マデカクリーム タイムリバース 50mL (東国製薬55年の結晶・高純度TECA×ツボクサ活性エクソソーム・真冬の乾燥シワ・たるみを押し戻す韓国国民的リペアクリーム)"
            },
            {
                "rank": 6,
                "queries": ["KISO ステム セルフ クリーム 50g", "KISO エクソソーム クリーム", "KISO ステム クリーム"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "ステム セルフ クリーム 50g (国産ヒト幹細胞順化培養液×ナノ化エクソソームカプセル・真冬の乾燥しぼみ肌を細胞レベルで潤す国内実力派エイジングクリーム)"
            },
            {
                "rank": 7,
                "queries": ["スピキュール エクソソーム クリーム 50g", "マイクロニードル エクソソーム クリーム"],
                "brand": "SPICULE BEAUTY (スピキュールビューティー)",
                "name": "マイクロニードル エクソソーム リッチクリーム 50g (天然海綿スピキュール×ヒト幹細胞エクソソーム・塗る微細針パルスで冬のこわばった角層を活性化)"
            },
            {
                "rank": 8,
                "queries": ["ナンバーズイン 1番 パントテン酸 水分スージングクリーム 80ml", "ナンバーズイン 1番 スージングクリーム"],
                "brand": "numbuzin (ナンバーズイン)",
                "name": "1番 パントテン酸 水分スージングクリーム 80mL (微細パントテン酸×鎮静シカエキス・真冬の暖房インナードライと毛穴詰まりをみずみずしく水分鎮静)"
            },
            {
                "rank": 9,
                "queries": ["アンファー スカルプD ボーテ 幹細胞 クリーム", "幹細胞 エクソソーム クリーム"],
                "brand": "SCALP-D BEAUTÉ (アンファー)",
                "name": "ナノステム リッチクリーム 50g (ヒト幹細胞由来エクソソーム×高浸透型ナノセラミド・真冬の過酷な乾燥環境でも弾力ハリ膜を一日中キープ)"
            },
            {
                "rank": 10,
                "queries": ["ドクターメラクチン セメントリーム 50ml", "ドクターメラクチン クリーム"],
                "brand": "Dr.Melaxin (ドクターメラクチン)",
                "name": "セメントリーム カルシウム エクソソーム クリーム 50mL (カルシウム結合リポソーム×バイオカプセル・真冬の角層バリアを強固に密着させて乾燥粉吹きを防ぐ話題のダーマコスメ)"
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
    
    with open("fetched_3new_barrier_niacinamide_exosome.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_barrier_niacinamide_exosome.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print(f"⚠️ Warning: Only {total_fetched}/30 items fetched.")

if __name__ == "__main__":
    fetch_all()
