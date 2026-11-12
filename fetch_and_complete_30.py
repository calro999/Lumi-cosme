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
    "winter_pdrn_mask": {
        "title": "保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10",
        "file": "winter-pdrn-mask.html",
        "items": [
            {
                "rank": 1,
                "queries": ["リジュラン スキン プロテクション マスク 5枚", "リジュラン ターンオーバー マスク", "リジュラン マスク 5枚"],
                "brand": "REJURAN (リジュラン)",
                "name": "リフレッシュ スキン プロテクション マスク 5枚入 (c-PDRN高濃度配合・美容医療発想のサーモンDNAとマイクロセルシートが真冬の深刻なしぼみ肌を細胞レベルで集中再生)"
            },
            {
                "rank": 2,
                "queries": ["VT PDRN ハイドロゲル マスク 4枚", "VT PDRN マスク 4枚", "VT PDRN カプセルマスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "PDRN ハイドロゲル リアル エンリッチ マスク 4枚入 (植物性高純度PDRN×超密着ハイドロゲルシート・貼ったまま眠れるほど濃密な美容液が透明に溶け込む即効ツヤ肌パック)"
            },
            {
                "rank": 3,
                "queries": ["メディヒール ロゼ PDRN エッセンシャル マスク", "メディヒール PDRN マスク 10枚", "MEDIHEAL PDRN リフティング"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "THE PDRN リフティング アンプルマスク 10枚入 (低分子マリンPDRN×コラーゲンカプセル・特許リフティングシートがフェイスラインを引き締めながら寒冷乾燥を徹底シールド)"
            },
            {
                "rank": 4,
                "queries": ["Anua PDRN ヒアルロン酸 マスク", "アヌア デイリーマスクパック 30枚", "Anua PDRN カプセル マスク"],
                "brand": "Anua (アヌア)",
                "name": "PDRN ヒアルロン酸 カプセル 100 セラム マスク 5枚入 (スマートPDRNカプセル×低分子ヒアルロン酸・角層のすみずみまで弾力水光を満たす冬の贅沢水分アンプルマスク)"
            },
            {
                "rank": 5,
                "queries": ["メディキューブ サーモン PDRN ピンク アンプル", "メディキューブ PDRN アンプル マスク", "メディキューブ ピンク PDRN"],
                "brand": "medicube (メディキューブ)",
                "name": "PDRN ピンク ペプチド アンプル マスク 5枚入 (高純度サーモンPDRN×マルチペプチド・冬の寒風でくすんだ肌にピンクの生き生きとした血色感とハリを同時に与える)"
            },
            {
                "rank": 6,
                "queries": ["KISO CARE 高濃度美容原液配合フェイスマスク PDRN", "KISO フェイスマスク PDRN 30枚", "KISO PDRN シートマスク"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "プレミアムフェイスマスク PDRN 30枚入 (北海道産サーモンPDRN原液高配合×高密着コットン100%シート・毎日のデイリーケアで真冬の肌密度を底上げするサイエンスマスク)"
            },
            {
                "rank": 7,
                "queries": ["VT リードルショット PDRN マスク", "リードルショット PDRN", "VT リードルショット マスク"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "リードルS PDRN デイリーマスク 30枚入 (天然マイクロニードルCICA REEDLE™×高濃度フィトPDRN・角層深部へ直接届くチクチク美容針と植物DNAで冬の毛穴・乾燥たるみを一撃リセット)"
            },
            {
                "rank": 8,
                "queries": ["IOPE バイオ シートマスク 10枚", "アイオペ PDRN マスク", "IOPE バイオ マスク"],
                "brand": "IOPE (アイオペ)",
                "name": "PDRN カフェイン ショット バイオセルロース マスク 5枚入 (バイオPDRN×スキンカフェイン・第二の皮膚と呼ばれる密着ゲルシートが冬のむくみと乾燥小ジワを強力リフト)"
            },
            {
                "rank": 9,
                "queries": ["バイオヒールボ プロバイオダーム コラーゲン マスク", "バイオヒールボ PDRN マスク", "プロバイオダーム タイトニング コラーゲン マスク"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "プロバイオダーム 3D リフティング PDRN コラーゲン マスク 5枚入 (高純度PDRN×特許乳酸菌バイオーム×3重コラーゲン・寒さで硬直したたるみ肌を立体的に引き上げるバイオ密閉パック)"
            },
            {
                "rank": 10,
                "queries": ["Dr.G レッドブレミッシュ クイックシートマスク PDRN", "Dr.G PDRN マスク", "ドクタージー PDRN アンプル マスク"],
                "brand": "Dr.G (ドクタージー)",
                "name": "レッドブレミッシュ PDRN ファーミング アンプル マスク 5枚入 (低刺激シカPDRN×10重ヒアルロン酸・皮膚科医監修の低刺激処方で冬の超敏感肌も安心して使える集中バリアパック)"
            }
        ]
    },
    "winter_retinol_eye_cream": {
        "title": "保湿力の強さで肌乾燥とさようなら！純粋レチノールの角層深部ターンオーバー促進と密着リペアバーム処方で真冬の目元ちりめんジワをふっくら伸ばす保湿力高めレチノールアイクリームランク10",
        "file": "winter-retinol-eye-cream.html",
        "items": [
            {
                "rank": 1,
                "queries": ["エリクシール レチノパワー リンクルクリーム 15g", "資生堂 エリクシール レチノパワー 15g"],
                "brand": "ELIXIR (資生堂 エリクシール)",
                "name": "レチノパワー リンクルクリーム S 15g (医薬部外品・日本で唯一シワ改善が認められた純粋レチノール配合・真冬の深い目尻ジワや乾燥ちりめんジワを根本から押し上げる金字塔)"
            },
            {
                "rank": 2,
                "queries": ["なめらか本舗 リンクルアイクリーム 20g", "なめらか本舗 目元ふっくらクリーム"],
                "brand": "サナ なめらか本舗 (常盤薬品工業)",
                "name": "リンクルアイクリーム N 20g (ピュアレチノール×豆乳発酵液×ビタミンE誘導体・プチプラの枠を超えた濃密密着クリームが真冬の乾燥による目元のくすみと小ジワを徹底ケア)"
            },
            {
                "rank": 3,
                "queries": ["KISO 純粋レチノール 0.2％配合 フェイスクリーム", "KISO レチノール クリーム 50g"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "スーパーリンクルクリーム VA 50g (純粋レチノール高配合原液×7種のオーガニック認証エキス・高純度サイエンス処方で目元だけでなく全顔・首元まで惜しみなくハリを満たす)"
            },
            {
                "rank": 4,
                "queries": ["ポーラ リンクルショット メディカル セラム 20g", "ポーラ リンクルショット 20g", "POLA リンクルショット"],
                "brand": "POLA (ポーラ)",
                "name": "リンクルショット メディカル セラム N 20g (医薬部外品・日本初のシワ改善有効成分ニールワン®配合・真冬の好中球エラスターゼ活性をブロックし目元や眉間の溝を劇的リペア)"
            },
            {
                "rank": 5,
                "queries": ["AHC テン レボリューション リアル アイクリーム 30ml", "AHC アイクリーム 30ml"],
                "brand": "AHC (エーエイチシー)",
                "name": "テン レボリューション リアル アイクリーム フォー フェイス 30mL (超微細ナノカプセルレチノール×ヒト型コラーゲン・顔全体に塗れる韓国売上No.1国民的リッチアイクリーム)"
            },
            {
                "rank": 6,
                "queries": ["イニスフリー レチノール シカ アイクリーム", "Innisfree レチノール シカ アイクリーム 30ml"],
                "brand": "Innisfree (イニスフリー)",
                "name": "レチノール シカ アンプルトリプル リペア アイクリーム 30mL (純粋レチノール×CICAシカバリア・敏感な目元にも毎日使える低刺激処方で真冬の目元くすみと弾力低下を解消)"
            },
            {
                "rank": 7,
                "queries": ["なめらか本舗 薬用リンクルアイクリーム ホワイト 20g", "なめらか本舗 薬用 リンクル アイクリーム 20g"],
                "brand": "サナ なめらか本舗 (常盤薬品工業)",
                "name": "薬用リンクルアイクリーム ホワイト 20g (医薬部外品・ナイアシンアミド×ピュアレチノール・シワ改善と美白を同時に叶え真冬の乾燥で影ができる目元を明るくふっくらブライトニング)"
            },
            {
                "rank": 8,
                "queries": ["アスタリフト アイクリームS 15g", "ASTALIFT アスタリフト アイクリーム", "アスタリフト アイクリーム"],
                "brand": "ASTALIFT (富士フイルム アスタリフト)",
                "name": "アイクリーム 15g (高濃度アスタキサンチン×リコピン×3種のコラーゲン・目元を力強くホールドするリッチな濃密テクスチャーが冬のまぶたのたるみと目尻の乾燥に密着)"
            },
            {
                "rank": 9,
                "queries": ["キュレル 潤浸保湿 モイストリペア アイクリーム 25g", "キュレル アイクリーム 25g", "キュレル モイストリペア アイクリーム"],
                "brand": "Curel (キュレル / 花王)",
                "name": "モイストリペア アイクリーム 25g (医薬部外品・消炎剤有効成分×集中保湿セラミド機能カプセル・皮膚が薄く乾燥しやすい冬のまぶたや目の下にとどまるモイストリペア処方)"
            },
            {
                "rank": 10,
                "queries": ["セザンヌ リンクルホワイトアイクリーム 20g", "セザンヌ アイクリーム 20g"],
                "brand": "CEZANNE (セザンヌ)",
                "name": "リンクルホワイトアイクリーム 20g (医薬部外品・有効成分ナイアシンアミド配合×レチノール誘導体・千円以下で本格シワ改善＆シミ予防ができる冬の神コスパアイクリーム)"
            }
        ]
    },
    "winter_panthenol_balm": {
        "title": "保湿力の強さで肌乾燥とさようなら！高濃度パンテノールの生体組織修復力と濃密密閉バリア膜で真冬のヒリヒリ粉吹き肌を緊急鎮静する保湿力高めパンテノールバームランク10",
        "file": "winter-panthenol-balm.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ラロッシュポゼ シカプラスト リペアクリーム B5+ 40ml", "ラロッシュポゼ シカプラスト バーム B5+ 40ml", "ラロッシュポゼ シカプラスト B5+"],
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "シカプラスト リペア バーム B5+ 40mL (プロビタミンB5パンテノール5%×マデカッソシド×プレバイオティクス・世界中で愛される真冬の肌荒れ・粉吹き・ヒリつきの緊急保護バーム)"
            },
            {
                "rank": 2,
                "queries": ["バイオヒールボ パンテノール シカ クリーム", "BIOHEAL BOH パンテノール シカ", "バイオヒールボ シカ クリーム"],
                "brand": "BIOHEAL BOH (バイオヒールボ)",
                "name": "パンテノール シカ バリア クリーム バーム 50mL (高純度パンテノール10%×CICA・高濃度パンテノールが壊れた角層バリアの隙間を埋め尽くし真冬の寒冷脱水を完全に阻止)"
            },
            {
                "rank": 3,
                "queries": ["アベンヌ シカルファットプラス リペアクリーム 40g", "シカルファットプラス リペアクリーム", "アベンヌ シカルファット"],
                "brand": "Avene (アベンヌ / ピエール ファーブル)",
                "name": "シカルファットプラス リペアクリーム 40g (アベンヌ皮膚科学研究の結晶・独自C+Restore×硫酸銅・亜鉛×温泉水・寒風で傷ついた肌を包帯のように覆い急速リペアする保護クリームバーム)"
            },
            {
                "rank": 4,
                "queries": ["エストラ アトバリア365 クリーム 80ml", "AESTURA アトバリア365 クリーム", "エストラ アトバリア クリーム"],
                "brand": "AESTURA (エストラ)",
                "name": "アトバリア365 クリーム 80mL (高純度セラミド・コレステロール・脂肪酸の複合カプセル×パンテノール・100時間持続する圧倒的保水力で真冬のインナードライを完全防衛)"
            },
            {
                "rank": 5,
                "queries": ["キュレル 潤浸保湿 フェイスクリーム 40g", "キュレル 潤浸保湿クリーム 40g", "キュレル フェイスクリーム 40g"],
                "brand": "Curel (キュレル / 花王)",
                "name": "潤浸保湿 フェイスクリーム 40g (医薬部外品・消炎剤有効成分×セラミド機能成分配合・ふんわり軽いのに角層深部まで潤い吸着し真冬の粉吹き・肌荒れを隙間なく予防)"
            },
            {
                "rank": 6,
                "queries": ["イハダ 薬用バーム 20g", "IHADA 薬用バーム 20g"],
                "brand": "IHADA (イハダ / 資生堂薬品)",
                "name": "薬用バーム 20g (医薬部外品・高精製ワセリン×抗肌あれ有効成分2種配合・人肌でとろけてピタッと密着し真冬のあらゆる外気刺激から肌を守り抜く低刺激バーム)"
            },
            {
                "rank": 7,
                "queries": ["トリデン ソリッドイン セラミド クリーム 100ml", "Torriden セラミド クリーム", "トリデン ソリッドイン クリーム"],
                "brand": "Torriden (トリデン)",
                "name": "ソリッドイン セラミド オールデイ バーム クリーム 100mL (5D複合セラミド×高濃度パンテノール×植物性エモリエント・顔やカサつくパーツにスッとなじみ真冬の粉吹きを即効ラップ)"
            },
            {
                "rank": 8,
                "queries": ["ドクタージャルト シカペア クリーム 50ml", "Dr.Jart+ シカペア クリーム", "ドクタージャルト シカペア 50ml"],
                "brand": "Dr.Jart+ (ドクタージャルト)",
                "name": "シカペア インテンシブ スージング リペア バーム 50mL (ツボクサエキス×パンテノール×アラントイン・真冬の冷気でダメージを受けた敏感肌を一晩で穏やかに鎮静する高機能バーム)"
            },
            {
                "rank": 9,
                "queries": ["リアルバリア エクストリーム クリーム 50ml", "Real Barrier エクストリーム クリーム", "リアルバリア バリア クリーム"],
                "brand": "Real Barrier (リアルバリア)",
                "name": "エクストリーム クリーム バーム 50mL (高純度パンテノール×特許MLE生体液晶バリア構造・冬の過酷な寒冷環境でも健康な肌のラメラ構造を完璧に再現し水分蒸発を物理的にブロック)"
            },
            {
                "rank": 10,
                "queries": ["キールズ クリーム UFC 50ml", "KIEHL'S ウルトラフェイシャルクリーム 50ml", "キールズ UFC 50ml"],
                "brand": "KIEHL'S (キールズ)",
                "name": "ウルトラ フェイシャル クリーム UFC 50mL (スクワラン×プロアークティシン×氷河プロテイン・過酷な極寒地でも潤いをキープし続ける真冬の世界的ロングセラー高保湿バームクリーム)"
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
    
    with open("fetched_3new_pdrn_retinol_panthenol.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_fetched}/{total_expected} items to fetched_3new_pdrn_retinol_panthenol.json!")
    if total_fetched == total_expected:
        print("🎉 30/30 ITEMS PERFECTLY FETCHED!")
    else:
        print(f"⚠️ Warning: Only {total_fetched}/30 items fetched.")

if __name__ == "__main__":
    fetch_all()
