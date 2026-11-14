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
    "winter_cica_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！高純度ツボクサエキス・CICAの濃厚鎮静ヴェールと密着シートで真冬の寒暖差赤み・暖房荒れを速攻鎮静する保湿力高めCICAシートマスクランク10",
        "file": "winter-cica-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["VT CICA デイリースージングマスク 30枚", "VT CICA マスク 30枚", "VT シカ デイリー マスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "CICA デイリースージングマスク 30枚入 (独自シカヒアロン™×0.2mm超極薄シート・冬の暖房寒暖差で赤らんだゆらぎ肌を秒速クールダウンして水分鎮静する大ヒットデイリーマスク)"
            },
            {
                "rank": 2,
                "queries": ["メディヒール ティーツリー マスク 10枚", "MEDIHEAL ティーツリー エッセンシャル マスク", "メディヒール ティーツリー 10枚"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "ティーツリー エッセンシャルマスク 10枚入 (高純度ティーツリー抽出液×ツボクサエキス・竹由来微細セルロースシートが真冬のエアコン乾燥で過敏になった角層を穏やかに鎮静)"
            },
            {
                "rank": 3,
                "queries": ["アピュー マデカソ CICA シートマスク", "アピュー マデカソサイド シートマスク", "A'pieu マデカソ マスク"],
                "brand": "A'pieu (アピュー)",
                "name": "マデカソ CICA シートマスク 10枚入 (高純度マデカッソシド×ツボクサ葉水・ガーゼとテンセルの特殊3層シートが冬のヒリつく乾燥肌に吸い付くように密着して保護)"
            },
            {
                "rank": 4,
                "queries": ["ドクタージャルト シカペア マスク", "Dr.Jart シカペア カーミング マスク", "シカペア セラム マスク"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "シカペア カーミング セラム マスク 5枚入 (タイガーハーブ高濃度CICAコンプレックス×植物由来高密着シート・真冬の冷風で赤みと皮剥けを起こしたSOS肌を集中レスキュー)"
            },
            {
                "rank": 5,
                "queries": ["Anua ドクダミ マスク 10枚", "アヌア ドクダミ 77 マスク", "Anua スージング シートマスク"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ 77% スージングシートマスク 10枚入 (自然由来ドクダミエキス77%×CICA・冬の寒気と暖房の摩擦で熱を持った肌を自然の恵みで優しく鎮める鎮静特化マスク)"
            },
            {
                "rank": 6,
                "queries": ["ネイチャーリパブリック CICA デイリーマスク", "ネイチャーリパブリック グリーンダーマ CICA マスク", "ネイリパ CICA マスク 30枚"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "グリーンダーマ CICA デイリーシートマスク 30枚入 (ツボクサエキス×プロポリスエキス・乾燥で敏感に傾いた冬の角層バリアを強固にし健やかなキメを育てる高保湿デイリーパック)"
            },
            {
                "rank": 7,
                "queries": ["ダーマレーザー スーパーTEATREE100", "クオリティファースト ダーマレーザー ティーツリー", "ダーマレーザー 緑 マスク"],
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー スーパーTEATREE100 マスク 7枚入 (プレミアムティーツリー×高濃度CICA・わずか3分のレーザー美容発想浸透で冬の突発的な肌荒れ・毛穴の開きを一気呵成に引き締める)"
            },
            {
                "rank": 8,
                "queries": ["KISO CICA フェイスマスク 30枚", "KISO マスク ツボクサ 30枚", "KISO CICA シートマスク"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "プレミアムフェイスマスク CICA 30枚入 (高純度ツボクサエキス原液配合×国産天然コットン100%・冬のゆらぎ肌にも負担のない無添加サイエンス処方で穏やかに整える)"
            },
            {
                "rank": 9,
                "queries": ["イニスフリー ビジャ シカ マスク", "innisfree ビジャ シカ シートマスク", "イニスフリー シカ マスク"],
                "brand": "innisfree (イニスフリー)",
                "name": "ビジャ シカ マスク 5枚入 (済州島カヤの実オイル×センテラアジアティカ・真冬の寒冷刺激でこわばった肌を柔らかくほぐし油水分バランスを整えるメディカル発想マスク)"
            },
            {
                "rank": 10,
                "queries": ["COSRX ピュアフィット CICA マスク", "コスアールエックス CICA マスク", "COSRX シカ シートマスク"],
                "brand": "COSRX (コスアールエックス)",
                "name": "ピュアフィット CICA カーム トゥルー シートマスク 10枚入 (独自CICA-7コンプレックス81%配合×極薄ヴィーガンシート・冬の乾燥性敏感肌を包み込み深いリラックスとうるおいを与える)"
            }
        ]
    },
    "winter_glutathione_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！高純度白玉グルタチオンの抗酸化発光力とビタミンC多重浸透膜で真冬の寒冷血行不良くすみを晴らす保湿力高めグルタチオンシートマスクランク10",
        "file": "winter-glutathione-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ナンバーズイン 5番 マスク 4枚", "ナンバーズイン 5番 白玉 マスク", "numbuzin 5番 マスク"],
                "brand": "numbuzin (ナンバーズイン)",
                "name": "5番 白玉グルタチオンCふりかけマスク 4枚入 (白玉グルタチオン×高濃度ビタミンCパウダーふりかけシート・冬の冷えによるどんより血行不良くすみを一掃する韓国メガヒット発光マスク)"
            },
            {
                "rank": 2,
                "queries": ["メディキューブ グルタチオン マスク", "medicube グルタチオン フェイスマスク", "メディキューブ グロウ マスク 4枚"],
                "brand": "medicube (メディキューブ)",
                "name": "グルタチオン グロウ フェイスマスク 4枚入 (純度99%高純度グルタチオン×ナイアシンアミド・冬の乾燥でしぼんだ肌に眩い水光ツヤを密着ホールドするエステ級ツヤマスク)"
            },
            {
                "rank": 3,
                "queries": ["VT グルタチオン デイリーマスク", "VT グルタチオン マスク 30枚", "VT グルタチオン モイスチャーマスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "グルタチオン デイリーモイスチャーマスク 30枚入 (高純度グルタチオン×ポリグルタミン酸・朝晩のデイリー密着ケアで真冬の乾燥くすみを根本から晴らす大容量ブライトニングパック)"
            },
            {
                "rank": 4,
                "queries": ["ダーマレーザー スーパーVC100 マスク 7枚", "クオリティファースト ダーマレーザー VC100", "ダーマレーザー 金 マスク"],
                "brand": "QUALITY 1st (クオリティファースト)",
                "name": "ダーマレーザー スーパーVC100 マスク 7枚入 (4種の濃厚ビタミンC×高濃度カプセル浸透・真冬の硬直角層にレーザーのように深く届いて毛穴とくすみを同時に引き締めるベストコスメ受賞マスク)"
            },
            {
                "rank": 5,
                "queries": ["KISO グルタチオン フェイスマスク 30枚", "KISO マスク グルタチオン 30枚", "基礎化粧品研究所 グルタチオン マスク"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "プレミアムフェイスマスク グルタチオン 30枚入 (純白玉グルタチオン原液配合×国産天然コットン100%・冬の過酸化皮質と血行不良によるくすみを科学的にケアする大容量サイエンスマスク)"
            },
            {
                "rank": 6,
                "queries": ["バイオヒールボ マスク 5枚", "BIOHEAL BOH プロバイオダーム マスク", "バイオヒールボ タイトニング マスク"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム タイトニング コラーゲン / グルタチオン マスク 5枚入 (乳酸菌ポストバイオティクス×グルタチオン・真冬の寒冷肌痩せとくすみを跳ね返す韓国オリーブヤング殿堂入りリフトマスク)"
            },
            {
                "rank": 7,
                "queries": ["アヌア グルタチオン マスク", "Anua 白玉 マスク 10枚", "Anua グルタチオン シートマスク"],
                "brand": "Anua (アヌア)",
                "name": "白玉グルタチオン ビタミンC アンプルマスク 10枚入 (リポソームグルタチオン×高純度アスコルビン酸・冬の紫外線ダメージと乾燥が重なる角層を均一な透明美肌へ整える)"
            },
            {
                "rank": 8,
                "queries": ["ドクターエルシア オアシス マスク", "Dr.Althea オアシス カーミング マスク", "ドクターエルシア スクワラン マスク"],
                "brand": "Dr.Althea (ドクターエルシア)",
                "name": "オアシス カーミング マスク 5枚入 (高保湿プレミアム植物幹細胞×高純度グルタチオン・真冬の砂漠肌を高級スパ帰りのようなみずみずしい透明美肌へ導くシルクタッチマスク)"
            },
            {
                "rank": 9,
                "queries": ["イニスフリー ビタミンC マスク", "innisfree ビタミンC シートマスク", "イニスフリー グリーンティー マスク"],
                "brand": "innisfree (イニスフリー)",
                "name": "ビタミンC グリーンティー エンザイム 明るい肌 マスク 10枚入 (緑茶酵素×デュアルビタミンC誘導体・真冬の角質肥厚によるくすみをマイルドにオフしながら純白のキメ肌へ整える)"
            },
            {
                "rank": 10,
                "queries": ["ドクタージー スネイル マスク 10枚", "Dr.G ブラックスネイル マスク", "ドクタージー マスク 10枚"],
                "brand": "Dr.G (ドクタージー)",
                "name": "ブラックスネイル グルタチオン マスク 10枚入 (高栄養ブラックスネイル粘液×高純度グルタチオン・冬の寒冷で活力を失った肌に濃密な弾力と輝きを呼び戻すクリニック発想マスク)"
            }
        ]
    },
    "winter_hyaluronic_lotion": {
        "title": "保湿力の強さで肌乾燥とさようなら！多段分子ヒアルロン酸の超濃密保水クッションと浸透ブースト処方で真冬のカサつきインナードライを潤し尽くす保湿力高めヒアルロン酸化粧水ランク10",
        "file": "winter-hyaluronic-lotion.html",
        "items": [
            {
                "rank": 1,
                "queries": ["肌ラボ 極潤プレミアム ヒアルロン液 170ml", "極潤プレミアム ヒアルロン液", "極潤 プレミアム ローション"],
                "brand": "肌ラボ (ロート製薬)",
                "name": "極潤プレミアム ヒアルロン液 170mL (8種のヒアルロン酸配合・まるで美容液のようなとろみテクスチャーが真冬の干からびた角層を濃密な水分クッションで満たす最高峰プチプラ化粧水)"
            },
            {
                "rank": 2,
                "queries": ["トリデン ダイブイン トナー 300ml", "Torriden ダイブイン トナー", "トリデン 低分子ヒアルロン酸 トナー"],
                "brand": "Torriden (トリデン)",
                "name": "ダイブイン 低分子ヒアルロン酸 トナー 300mL (5D複合低分子ヒアルロン酸×アラントイン・シャバシャバなのに奥から吸い付くような潤い！冬の暖房インナードライを秒速充填する韓国神トナー)"
            },
            {
                "rank": 3,
                "queries": ["アクセーヌ モイストバランス ローション 360ml", "アクセーヌ モイストバランス ローション", "ACSEINE モイストバランス"],
                "brand": "ACSEINE (アクセーヌ)",
                "name": "モイストバランス ローション 360mL (超微細ナノカプセル化ヒアルロン酸×セラミド類似成分・水のような軽やかさで角層の隅々まで染み渡り1日中潤いが続く皮膚科医推奨の傑作)"
            },
            {
                "rank": 4,
                "queries": ["ナンバーズイン 1番 トナー 300ml", "ナンバーズイン 1番 鎮静トナー", "numbuzin 1番 トナー"],
                "brand": "numbuzin (ナンバーズイン)",
                "name": "1番 澄んだ水分鎮静トナー 300mL (ヒアルロン酸×ツボクサ×ドクダミ×カンゾウのハーブ水分・冬の乾燥と火照りを同時に鎮めながらみずみずしい透明肌へ導く大容量トナー)"
            },
            {
                "rank": 5,
                "queries": ["ドクタージャルト バイタルハイドラ トナー", "Dr.Jart バイタル ハイドラ トナー", "ドクタージャルト ハイドラ トナー"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "バイタル ハイドラ ソリューション トナー 150mL (低分子ヒアルロン酸×プレバイオティクス×アクアキシル・冬の強風で水分蒸散が激しい角層バリアを強固に立て直す水分ブースト化粧水)"
            },
            {
                "rank": 6,
                "queries": ["オルビス アクアニスト ローション 180ml", "オルビスユー エッセンスローション 180ml", "オルビス 化粧水 とてもしっとり"],
                "brand": "ORBIS (オルビス)",
                "name": "オルビス アクアニスト ローション RM (高保湿) 180mL (持続型ヒアルロン酸×浸透型アミノ酸・真冬の敏感肌にも摩擦レスに広がりうるおいを逃さない設計の低刺激高保湿ローション)"
            },
            {
                "rank": 7,
                "queries": ["キュレル 化粧水 III 150ml", "キュレル 潤浸保湿 化粧水 とてもしっとり", "Curel 化粧水 3"],
                "brand": "Curel (花王 キュレル)",
                "name": "潤浸保湿 化粧水 III とてもしっとり 150mL (医薬部外品・消炎剤有効成分×ユーカリエキス×ヒアルロン酸様高保水処方・冬の粉吹き肌にすーっと馴染みカサつきを防ぐ敏感肌の定番)"
            },
            {
                "rank": 8,
                "queries": ["イハダ 薬用ローション とてもしっとり 180ml", "IHADA 薬用ローション とてもしっとり", "イハダ 化粧水 とてもしっとり"],
                "brand": "IHADA (資生堂 イハダ)",
                "name": "薬用ローション (とてもしっとり) 180mL (医薬部外品・高精製ワセリン×多重保湿ヒアルロン酸・冬の冷えや花粉・乾燥による肌荒れスパイラルを断ち切る薬用高保湿化粧水)"
            },
            {
                "rank": 9,
                "queries": ["ちふれ 濃厚 保湿化粧水 180ml", "ちふれ 濃厚 保湿化粧水", "ちふれ 化粧水 濃厚"],
                "brand": "CHIFURE (ちふれ)",
                "name": "濃厚 保湿化粧水 180mL (ヒアルロン酸×牡丹エキス×芍薬エキス・リッチな感触のとろみ美容液化粧水が真冬の乾燥小ジワを目立たなくするエイジングケアプチプラ名品)"
            },
            {
                "rank": 10,
                "queries": ["KISO ヒアルロン酸 化粧水", "KISO モイスチャーローション HA", "基礎化粧品研究所 ヒアルロン酸 化粧水"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "ヒアルロン酸 浸透化粧水 HA 150mL (高純度ヒアルロン酸Na原液ブレンド・余計な成分を極限まで削ぎ落とし角層の水分要求にピュアに応える高濃度サイエンスローション)"
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
    
    with open("fetched_3new_cica_glutathione_hyaluronic.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_cica_glutathione_hyaluronic.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print(f"⚠️ Warning: Only {total_fetched}/30 items fetched.")

if __name__ == "__main__":
    fetch_all()
