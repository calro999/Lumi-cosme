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
    "winter_retinol_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！濃密ビタミンA×セラミド処方で真冬の乾燥小ジワと毛穴の開きをふっくら押し戻す保湿力高めレチノール美容液ランク10",
        "file": "winter-retinol-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["イニスフリー レチノール シカ リペア セラム 30ml", "イニスフリー レチノール シカ 30ml"],
                "brand": "innisfree (イニスフリー)",
                "name": "レチノール シカ リペア セラム 30mL (純粋レチノール×シカ×ヒアルロン酸・A反応を抑えて毎日使える冬の毛穴・キメ集中美容液)"
            },
            {
                "rank": 2,
                "queries": ["VT シカレチA エッセンス 0.1 30ml", "VT シカレチA エッセンス 30ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "シカレチA エッセンス 0.1 30mL (第3世代レチノイド誘導体×シカヒアルロン・毛穴の開きとたるみを引き締める高保湿エイジングセラム)"
            },
            {
                "rank": 3,
                "queries": ["COSRX レチノール 0.1 20ml", "COSRX ザ レチノール 0.1"],
                "brand": "COSRX (コスアールエックス)",
                "name": "RX ザ・レチノール 0.1 クリーム / セラム 20mL (純度安定化ピュアレチノール0.1%×アラントイン×トコトリエノール・乾燥小ジワを集中密着ケア)"
            },
            {
                "rank": 4,
                "queries": ["キールズ DS RTN リニューイング セラム 30ml", "キールズ レチノール 美容液 30ml"],
                "brand": "KIEHL'S (キールズ)",
                "name": "DS RTN リニューイング セラム 30mL (マイクロフリーズドライ純粋レチノール×セラミド×ペプチド・肌のバリアを守りながらハリを実感する名品)"
            },
            {
                "rank": 5,
                "queries": ["ラロッシュポゼ エファクラ ピールケア セラム 30ml", "ラロッシュポゼ レチノール 美容液 30ml"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "エファクラ ピールケア セラム / レチノールB3セラム 30mL (低刺激レチノール×ナイアシンアミド×ターマルウォーター・敏感肌でも使える冬の角質ケア美容液)"
            },
            {
                "rank": 6,
                "queries": ["アンレーベル ラボ Rエッセンス レチノール 50ml", "アンレーベル ラボ レチノール 50ml"],
                "brand": "unlabel LAB (アンレーベル ラボ)",
                "name": "Vエッセンス / Rエッセンス レチノール 50mL (超高圧100MPa抽出レチノール配合・肌の奥深くまで素早く浸透しふっくら弾力をサポート)"
            },
            {
                "rank": 7,
                "queries": ["KISO レチノール 美容液 30ml", "KISO スーパーリンクルセラム VA 30ml"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "スーパーリンクルセラム VA 30mL (純粋ピュアレチノール原液配合・カプセル化ナノ処方で角層へ穏やかに届き乾燥小ジワを目立たなくする原液美容液)"
            },
            {
                "rank": 8,
                "queries": ["なめらか本舗 リンクル美容液", "サナ なめらか本舗 リンクル美容液 100ml"],
                "brand": "SANA なめらか本舗 (常盤薬品工業)",
                "name": "リンクル美容液 N 100mL (豆乳発酵液×ピュアレチノール×ビタミンE誘導体・首元まで惜しみなくたっぷり使える大容量高保湿エイジングケア)"
            },
            {
                "rank": 9,
                "queries": ["ネイチャーリパブリック レチノール シートマスク 60枚入", "ネイチャーリパブリック レチノール 美容液"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "レチノール パンテノール リペア アンプル 30mL (レチノール×パンテノール×セラミド・肌荒れを防ぎながら冬の乾燥しぼみ肌をなめらかに満たす高保湿セラム)"
            },
            {
                "rank": 10,
                "queries": ["IOPE レチノール スーパー バウンス セラム 30ml", "アイオペ レチノール スーパー バウンス セラム"],
                "brand": "IOPE (アイオペ)",
                "name": "レチノール スーパーバウンス セラム 30mL (4重レチノイドコンプレックス×ヒノキ木エキス・皮膚科学研究30年の結晶が生んだ冬の密度爆発リフティング美容液)"
            }
        ]
    },
    "winter_hyaluronic_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！多層ヒアルロン酸の水分シールドで真冬の暖房インナードライを根本解決する保湿力高めヒアルロン酸クリームランク10",
        "file": "winter-hyaluronic-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["Torriden ダイブイン スージングクリーム 100ml", "トリデン ダイブイン スージングクリーム"],
                "brand": "Torriden (トリデン)",
                "name": "ダイブイン スージングクリーム 100mL (5D複合ヒアルロン酸×トレハロース・オリーブヤング1位獲得！冬の乾いた角層を水分爆弾で満たす大人気ジェルクリーム)"
            },
            {
                "rank": 2,
                "queries": ["ラネージュ ウォーターバンク モイスチャークリーム 50ml", "LANEIGE ウォーターバンク クリーム 50ml"],
                "brand": "LANEIGE (ラネージュ)",
                "name": "ウォーターバンク モイスチャークリーム 50mL (超低分子ブルーヒアルロン酸×セラミド・皮膚の1/2000極小サイズが冬のバリア機能を修復しモチ肌を長時間持続)"
            },
            {
                "rank": 3,
                "queries": ["肌ラボ 極潤プレミアム ヒアルロンクリーム 50g", "極潤プレミアム ヒアルロンクリーム 50g"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤プレミアム ヒアルロンクリーム 50g (8種のスーパーヒアルロン酸×スクワラン・美容液オイルカプセルが肌の上でとろけて真冬の過酷な乾燥を完全密閉)"
            },
            {
                "rank": 4,
                "queries": ["アヌア ヒアルロン酸 水分 クリーム 50ml", "Anua ヒアルロン酸 水分バリア クリーム 50ml"],
                "brand": "Anua (アヌア)",
                "name": "ヒアルロン酸 水分バリアクリーム 50mL (低分子ヒアルロン酸×セラミドNP×パンテノール・ベタつきゼロで暖房下のインナードライを素早くレスキュー)"
            },
            {
                "rank": 5,
                "queries": ["メディキューブ トリプル コラーゲン クリーム 50ml", "メディキューブ コラーゲン クリーム 50ml"],
                "brand": "medicube (メディキューブ)",
                "name": "トリプル コラーゲン クリーム 50mL (3重ヒアルロン酸×低分子コラーゲンコンプレックス・乾いた冬肌にガラス玉のようなツヤとハリを与える濃密保湿クリーム)"
            },
            {
                "rank": 6,
                "queries": ["dプログラム スキンリペアクリーム 45g", "資生堂 dプログラム スキンリペアクリーム"],
                "brand": "d プログラム (資生堂)",
                "name": "スキンリペアクリーム 45g (高精製ワセリン×トラネキサム酸×グリチルリチン酸ジカリウム・寒暖差で荒れやすい冬のゆらぎ肌を抗炎症＆密封ラップ)"
            },
            {
                "rank": 7,
                "queries": ["Dr.G レッド ブレミッシュ クリア スージング クリーム 70ml", "ドクタージー スージングクリーム 70ml"],
                "brand": "Dr.G (ドクタージー)",
                "name": "レッドブレミッシュ クリアスージングクリーム 70mL (10-CICA×微細ヒアルロン酸・韓国皮膚科医推奨の水分ジェルが真冬の熱のこもった乾燥肌を鎮静＆保水)"
            },
            {
                "rank": 8,
                "queries": ["VT スーパーヒアルロン", "VT スーパーヒアルロン クリーム 55ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "スーパーヒアルロン モイスチャークリーム 55mL (G:H8複合ヒアルロン酸×γ-PGA・水分レイヤリング技術で角層の隅々まで潤いを留めて蒸発をシャットアウト)"
            },
            {
                "rank": 9,
                "queries": ["イニスフリー グリーンティー ヒアルロン クリーム 50ml", "イニスフリー グリーンティー モイスト クリーム 50ml"],
                "brand": "innisfree (イニスフリー)",
                "name": "グリーンティー ヒアルロン モイスト クリーム 50mL (美肌茶葉エキス×5種ヒアルロン酸・冬の乾きやすい肌にみずみずしい潤い膜を形成する水分ロッククリーム)"
            },
            {
                "rank": 10,
                "queries": ["松山油脂 肌をうるおす 保湿クリーム 50g", "肌をうるおす 保湿クリーム 50g"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "保湿クリーム 50g (5種のヒト型セラミド×浸透型ヒアルロン酸×シア脂・大豆由来成分が角層をみっちり満たし冬の乾燥から肌を長時間プロテクト)"
            }
        ]
    },
    "winter_cica_serum": {
        "title": "保湿力の強さで肌乾燥とさようなら！高純度ツボクサエキスの急速鎮静力で寒暖差のピリピリ赤み肌をしっとり救う保湿力高めシカ美容液ランク10",
        "file": "winter-cica-serum.html",
        "items": [
            {
                "rank": 1,
                "queries": ["SKIN1004 センテラ アンプル 55ml", "スキン1004 マダガスカル センテラ アンプル"],
                "brand": "SKIN1004 (スキンワンオーフォー)",
                "name": "マダガスカル センテラ アンプル 55mL (高純度ツボクサエキス100%配合・真冬の冷風でピリつく肌を水のような浸透感で素早く沈静化する大ヒット名品)"
            },
            {
                "rank": 2,
                "queries": ["VT CICA エッセンス", "VT シカ エッセンス 500ml"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "シカ スージング エッセンス 100mL (独自CICALIAO×高濃度ツボクサエキス・寒暖差でバリアが乱れた冬肌にすーっと浸透し健やかな水分バリアを形成)"
            },
            {
                "rank": 3,
                "queries": ["ドクタージャルト シカペア セラム 30ml", "dr.jart+ シカペア セラム"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "シカペア セラム 30mL (高濃縮ツボクサコンプレックス×緑のレスキュー植物・冬の激しい乾燥トラブルと肌荒れを一滴で包み込み立て直す皮膚科発想美容液)"
            },
            {
                "rank": 4,
                "queries": ["Anua ドクダミ 80% 水分鎮静アンプル 30ml", "アヌア ドクダミ 80 アンプル 30ml"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 80% 水分鎮静アンプル 30mL (ドクダミエキス80%×シカ成分×パンテノール・冬の暖房下で火照り・赤みが出やすいインナードライ肌に濃密な潤いを集中補給)"
            },
            {
                "rank": 5,
                "queries": ["魔女工場 パンテトイン エッセンス 80ml", "manyo パンテトイン エッセンス 80ml"],
                "brand": "魔女工場 (manyo)",
                "name": "パンテトイン ディープモイスチャー エッセンス 80mL (高濃度パンテノール×エクトイン×シカ成分・極度の乾燥と外部刺激から肌を守り抜く濃密トリートメント美容液)"
            },
            {
                "rank": 6,
                "queries": ["アピュー マデカソサイド 美容液 30ml", "apieu マデカソサイド 美容液"],
                "brand": "A'pieu (アピュー)",
                "name": "マデカソサイド 美容液 30mL (高純度ツボクサ葉水×マデカッソシド配合・サラッとなじむのに奥まで潤いが届き真冬のピリピリ感を穏やかに解きほぐす薬用級セラム)"
            },
            {
                "rank": 7,
                "queries": ["コスデバハ CH セラム", "コスデバハ センテラ"],
                "brand": "Cos De BAHA (コスデバハ)",
                "name": "CH センテラ ツボクサ セラム 30mL (有機栽培ツボクサエキス83%高濃度配合・精製水の代わりにツボクサ葉水をベースにした原液処方で冬の敏感荒れを集中リセット)"
            },
            {
                "rank": 8,
                "queries": ["ビープレーン シカフル アンプル 30ml", "beplain シカフル アンプル"],
                "brand": "beplain (ビープレーン)",
                "name": "シカフル アンプル 30mL (ツボクサエキス84.28%×カモミール花エキス・オリーブヤング美容液部門アワード常連！軽やかなジェルが冬のデリケート肌を急速鎮静)"
            },
            {
                "rank": 9,
                "queries": ["ネイチャーリパブリック グリーンダーマ シカ セラム 50ml", "ネイチャーリパブリック シカ セラム"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "グリーンダーマ CICA セラム 50mL (ツボクサエキス×プロポリスエキス配合・真冬の乾燥冷風でゴワついた肌をもちもちにほぐす高保湿シカ美容液)"
            },
            {
                "rank": 10,
                "queries": ["イニスフリー ビジャ シカ バーム 40ml", "イニスフリー ビジャ シカ エッセンス 40ml"],
                "brand": "innisfree (イニスフリー)",
                "name": "ビジャ シカ リペア エッセンス / バーム 40mL (高純度ツボクサエキス4X×カヤ種子油・冷たい北風でバリア機能が低下した肌をしっとりやわらかく包み込んで保護するジェル乳液美容液)"
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
                total_fetched += 1
            else:
                print(f"❌ CRITICAL: Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_retinol_hyaluronic_cica.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_retinol_hyaluronic_cica.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print("⚠️ Warning: Some items missing.")

if __name__ == "__main__":
    fetch_all()
