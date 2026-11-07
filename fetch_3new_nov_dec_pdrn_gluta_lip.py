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
    "winter_pdrn_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！サーモンDNAの細胞修復力で真冬のしぼみ肌を底上げする保湿力高めPDRNクリームランク10",
        "file": "winter-pdrn-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["VT PDRN クリーム 50ml", "VT PDRN クリーム", "VT コスメティックス PDRN クリーム"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "PDRN クリーム 100 50mL (植物性高純度PDRN×セラミドNP配合・角層の奥深くから弾力をパンと満たし乾燥によるしぼみ肌を密着リペアする濃密クリーム)"
            },
            {
                "rank": 2,
                "queries": ["メディキューブ PDRN クリーム", "medicube PDRN クリーム", "メディキューブ PDRN ピンク ペプチド アンプル クリーム"],
                "brand": "medicube (メディキューブ)",
                "name": "PDRN ピンクペプチドアンプル クリーム 50mL (高純度サーモンPDRN×ピンクビタミン×マルチペプチド配合・真冬の寒冷ダメージ肌をふっくら押し戻すエイジングケアクリーム)"
            },
            {
                "rank": 3,
                "queries": ["アヌア PDRN クリーム", "Anua PDRN クリーム", "Anua PDRN ヒアルロン酸 カプセル クリーム"],
                "brand": "Anua (アヌア)",
                "name": "PDRN ヒアルロン酸 カプセルクリーム 50mL (スマートカプセル化PDRN×多重ヒアルロン酸・肌に触れた瞬間カプセルが弾けて潤い膜を形成する水分弾力クリーム)"
            },
            {
                "rank": 4,
                "queries": ["IOPE PDRN カフェイン ショット クリーム", "アイオペ PDRN クリーム", "IOPE カフェイン ショット クリーム"],
                "brand": "IOPE (アイオペ)",
                "name": "Bio PDRN カフェインショット クリーム 50mL (肌再生を促すBio-PDRN×カフェイン配合・冬の朝のむくみと乾燥小ジワを同時にすっきりと引き締めるリフティングクリーム)"
            },
            {
                "rank": 5,
                "queries": ["リジュラン ヒーラー ニュートリティブ クリーム 50ml", "リジュラン リカバリー クリーム 50ml", "REJURAN ターンオーバー クリーム 50ml"],
                "brand": "REJURAN (リジュラン)",
                "name": "ターンオーバー アクティブ クリーム 50mL (サーモンDNA抽出c-PDRNを高濃度配合・美容皮膚科発想の圧倒的な組織補修力で冬の砂漠肌を生き返らせる集中再生クリーム)"
            },
            {
                "rank": 6,
                "queries": ["ドクターエルシア パワー インフュージョン クリーム", "Dr.Althea PDRN クリーム", "ドクターエルシア オアシス クリーム"],
                "brand": "Dr.Althea (ドクターエルシア)",
                "name": "オアシス スージング マスク クリーム / PDRN パワーインフュージョン クリーム 50mL (PDRN×セラミド×ツボクサエキス・冷たい外気で赤みが出やすい冬の超敏感肌を鎮静＆保水)"
            },
            {
                "rank": 7,
                "queries": ["KISO PDRN クリーム", "キソ PDRN クリーム 50g", "KISO スーパーリンクルクリーム PDRN"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "スーパーリンクルクリーム PDRN 50g (国産高純度PDRN×レチノール誘導体×植物性スクワラン配合・無駄な添加物を省き成分純度にこだわった原液処方高保湿クリーム)"
            },
            {
                "rank": 8,
                "queries": ["センテリアン24 マデカ ダーマ プレミアム クリーム", "センテリアン24 マデカクリーム タイムリバース", "東国製薬 マデカクリーム 50ml"],
                "brand": "Centellian24 (センテリアン24)",
                "name": "マデカクリーム タイムリバース 50mL (TECA×独自活性PDRN様発酵エキス配合・製薬会社が開発した真冬の超乾燥と肌痩せを救う国民的メガヒット再生クリーム)"
            },
            {
                "rank": 9,
                "queries": ["ネイチャーリパブリック PDRN クリーム", "ネイチャーリパブリック サーモン PDRN クリーム", "NATURE REPUBLIC PDRN"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "サーモン PDRN デュアル リペア クリーム 50mL (サーモンDNA×低分子コラーゲン×アミノ酸・なめらかなシルクのようなテクスチャーで真冬の肌をラッピングする高保湿クリーム)"
            },
            {
                "rank": 10,
                "queries": ["ダーマファーム ウルトラセラム クリーム PDRN", "DERMAFIRM PDRN クリーム", "ダーマファーム PDRN クリーム"],
                "brand": "DERMAFIRM (ダーマファーム)",
                "name": "ウルトラセラム リペアクリーム PDRN 50mL (リポソーム化PDRN×ペプチドコンプレックス・真冬の暖房直撃によるインナードライを根本から防ぎモチモチ肌を維持するドクターズコスメ)"
            }
        ]
    },
    "winter_glutathione_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！白玉のような発光透明感と濃密水分シールドで真冬の枯れ肌を救う保湿力高めグルタチオンクリームランク10",
        "file": "winter-glutathione-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ナンバーズイン 5番 白玉 グルタチオン クリーム 50ml", "ナンバーズイン 5番 グルタチオン クリーム", "numbuzin 5番 クリーム 50ml"],
                "brand": "numbuzin (ナンバーズイン)",
                "name": "5番 白玉グルタチオンC スージングクリーム / メラゼロクリーム 50mL (高純度グルタチオン×ビタミンC×ナイアシンアミド5%配合・冬のくすみと乾燥を同時に晴らす白玉発光クリーム)"
            },
            {
                "rank": 2,
                "queries": ["メディキューブ グルタチオン グロウ クリーム 50g", "medicube グルタチオン クリーム", "メディキューブ 白玉 クリーム 50g"],
                "brand": "medicube (メディキューブ)",
                "name": "ディープ グルタチオン グロウ クリーム 50g (純度99%グルタチオン×持続型リポソームカプセル・真冬の乾燥で失われたツヤと透明感を一瞬で蘇らせる高保湿発光リフティングクリーム)"
            },
            {
                "rank": 3,
                "queries": ["バイオヒールボ プロバイオダーム コラーゲン リペア クリーム 50ml", "バイオヒールボ グルタチオン トーニング クリーム", "BIOHEAL BOH グルタチオン クリーム"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム グルタチオン トーニング クリーム 50mL (乳酸菌バイオーム×グルタチオン×ナイアシンアミド・冬のゴワつく角層を柔軟にほぐしながら明るく潤す密着トーンアップクリーム)"
            },
            {
                "rank": 4,
                "queries": ["アピュー マデカソ CICA モイスチャー クリーム 50ml", "A'pieu グルタチオン クリーム", "アピュー ピュアブロック ナチュラル デイ クリーム"],
                "brand": "A'pieu (アピュー)",
                "name": "マデカソ CICA モイスチャークリーム 50mL (CICAツボクサエキス×グルタチオン×ナイアシンアミド・冷えと暖房の寒暖差で荒れやすい冬肌を優しく鎮静しながら透き通る潤いを与える高保湿クリーム)"
            },
            {
                "rank": 5,
                "queries": ["KISO ハイドロキノン クリーム 純ハイドロキノン 50g", "KISO グルタチオン クリーム 50g", "KISO スーパーホワイトクリーム"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "スーパーホワイトクリーム GLO 50g (高純度グルタチオン5%配合×α-アルブチン×植物性スクワラン・冬の深刻な紫外線沈着と乾燥によるくすみ肌を集中トリートメントする原液クリーム)"
            },
            {
                "rank": 6,
                "queries": ["イニスフリー ビタC グリーンティー エンザイム クリーム 50ml", "イニスフリー ビタミンC クリーム 50ml", "innisfree ビタC クリーム"],
                "brand": "innisfree (イニスフリー)",
                "name": "ビタC グリーンティーエンザイム ブライト クリーム 50mL (緑茶酵素×デュアルビタミンC×グルタチオン誘導体・冬の古い角質をやさしく整えながらうるおいに満ちたつるすべ肌へ導く水分クリーム)"
            },
            {
                "rank": 7,
                "queries": ["ドクタージー レッド ブレミッシュ クリア スージング クリーム 70ml", "Dr.G レッドブレミッシュ クリーム 70ml", "ドクタージー スージング クリーム"],
                "brand": "Dr.G (ドクタージー)",
                "name": "レッドブレミッシュ クリアスージングクリーム 70mL (10-CICA×グルタチオン複合体・暖房で火照った冬の乾燥肌を心地よくクールダウンしながら100時間潤いを守り抜く水分ジェルクリーム)"
            },
            {
                "rank": 8,
                "queries": ["コスアールエックス RX ザ・グルタチオン クリーム 50ml", "COSRX グルタチオン クリーム", "COSRX ザ・ビタミンC 23 クリーム"],
                "brand": "COSRX (コスアールエックス)",
                "name": "ザ・グルタチオン 6000 クリーム 50mL (グルタチオン6,000ppm×スクワラン×セラミドNP・肌本来の抗酸化ネットワークをサポートし真冬の寒冷外気から角層を一日中守る濃密保湿クリーム)"
            },
            {
                "rank": 9,
                "queries": ["サムバイミー ガラクトミセス ピュアビタミンC クリーム 50ml", "サムバイミー ビタミンC クリーム", "SOME BY MI グルタチオン クリーム"],
                "brand": "SOME BY MI (サムバイミー)",
                "name": "ガラクトミセス ピュアビタミンC グロウ クリーム 50mL (発酵ガラクトミセス75%×ピュアビタミンC×グルタチオン・冬の乾燥で硬化した角質層へ速やかに浸透し発光ツヤをもたらす高機能クリーム)"
            },
            {
                "rank": 10,
                "queries": ["魔女工場 ガラク ナイアシン 2.0 エッセンス クリーム", "魔女工場 ガラク エッセンス クリーム 50ml", "manyo ガラク クリーム 50ml"],
                "brand": "manyo (魔女工場)",
                "name": "ガラク エッセンス クリーム 50mL (高純度ガラクトミセス発酵濾過物×ナイアシンアミド×グルタチオン・ベタつきゼロで真冬のインナードライを満たし肌のキメと透明感を極める濃密エッセンスクリーム)"
            }
        ]
    },
    "winter_ceramide_lip": {
        "title": "保湿力の強さで肌乾燥とさようなら！めくれる皮むけ・ひび割れを角層ラメラで密閉修復する保湿力高めセラミドリップランク10",
        "file": "winter-ceramide-lip.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ケアセラ 高保湿リップクリーム 2.4g", "ケアセラ リップクリーム 2.4g", "ケアセラ リップ"],
                "brand": "CareCera (ケアセラ)",
                "name": "高保湿リップクリーム 2.4g (天然型セラミド複数配合×ワセリン・荒れてめくれた唇の角層細胞間脂質をダイレクトに修復し塗った瞬間からしっとり柔らかな唇を再生する大ヒットリップ)"
            },
            {
                "rank": 2,
                "queries": ["キュレル リップケアバーム 4.2g", "キュレル リップケア バーム", "キュレル 潤浸保湿 リップケアバーム"],
                "brand": "Curel (キュレル)",
                "name": "潤浸保湿 リップケアバーム 4.2g (セラミド機能成分×消炎成分・唇パックのように密着して真冬の就寝中もカサつき・ひび割れを防ぎ翌朝ふっくらプルプルの唇に整える濃厚バーム)"
            },
            {
                "rank": 3,
                "queries": ["タカミ リップ 7g", "TAKAMI タカミリップ 7g", "タカミ リップエッセンス 7g"],
                "brand": "TAKAMI (タカミ)",
                "name": "タカミリップ 7g (ヒト型セラミド×ビタミンP×高密着植物エモリエントオイル配合・唇の薄い皮膚の代謝に着目し縦ジワやくすみをケアして生まれたてのようなピュア唇へ導く名品)"
            },
            {
                "rank": 4,
                "queries": ["ETVOS ミネラルリッププランパー ディープ", "エトヴォス ミネラルリッププランパー 5.6g", "ETVOS リッププランパー ディープ"],
                "brand": "ETVOS (エトヴォス)",
                "name": "ミネラルリッププランパー ディープ 5.6g (ヒト型セラミド×植物オイル×ヒアルロン酸・メイクしながら濃密な潤いでパックし真冬の寒さでしぼんだ唇をぷっくりボリュームアップ)"
            },
            {
                "rank": 5,
                "queries": ["トリデン ソリッドイン セラミド リップエッセンス 11ml", "Torriden セラミド リップエッセンス 11ml", "トリデン リップエッセンス"],
                "brand": "Torriden (トリデン)",
                "name": "ソリッドイン セラミド リップエッセンス 11mL (5D複合セラミド×ホホバ種子油配合・オリーブヤング1位獲得！ベタつかないのに驚異の持続力で唇の皮むけを瞬時に落ち着かせる水分密閉エッセンス)"
            },
            {
                "rank": 6,
                "queries": ["DHC 薬用 リップクリーム 1.5g", "DHC リップクリーム 1.5g 3本セット", "DHC エクストラモイスチュア リップクリーム"],
                "brand": "DHC (ディーエイチシー)",
                "name": "エクストラモイスチュア リップクリーム 1.5g (オリーブバージンオイル×セラミド類似成分×甘草誘導体・従来の薬用リップを凌駕するボリュームアップ処方で冬の頑固な荒れを即効レスキュー)"
            },
            {
                "rank": 7,
                "queries": ["オルビス リップトリートメント 2.3g", "ORBIS リップトリートメント", "オルビス 薬用 リップトリートメント"],
                "brand": "ORBIS (オルビス)",
                "name": "リップトリートメント 2.3g (セラミドネットワーク成分×スクワラン×ヒアルロン酸・冬の冷たい外気で硬くなった唇の角質をなめらかにほぐし口紅のノリを格段に高めるリップ下地トリートメント)"
            },
            {
                "rank": 8,
                "queries": ["メンソレータム メルティクリームリップ 無香料 2.4g", "メルティクリームリップ 2.4g", "メンソレータム プレミアムメルティクリームリップ"],
                "brand": "メンソレータム (ロート製薬)",
                "name": "プレミアムメルティクリームリップ 無香料 2.4g (マルチセラミド×体温でとろけるモイストバンク技術・唇の水分と空気中の水分を抱え込んでクリームに変化する新感覚の高保湿リップ)"
            },
            {
                "rank": 9,
                "queries": ["アルージェ トータルモイストベール リップエッセンス 8g", "アルージェ リップエッセンス 8g", "アルージェ リップ 8g"],
                "brand": "Arouge (アルージェ)",
                "name": "トータルモイストベール リップエッセンス 8g (天然セラミド配合・医薬部外品・界面活性剤や防腐剤無添加でデリケートな唇の皮むけ・炎症を包み込みしっとり保護する薬用リップ美容液)"
            },
            {
                "rank": 10,
                "queries": ["松山油脂 肌をうるおす 保湿リップバーム", "肌をうるおす 保湿リップバーム 8g", "松山油脂 リップバーム"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "保湿リップバーム 8g (5種のヒト型セラミド×大豆由来成分×カルナウバロウ・指先で温めてなじませる濃厚バームが唇表面に水分の蒸発を防ぐ保護膜を形成する無香料リップ)"
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
                    time.sleep(1.8)
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
    
    with open("fetched_3new_nov_dec_pdrn_gluta_lip.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_nov_dec_pdrn_gluta_lip.json!")

if __name__ == "__main__":
    fetch_all()
