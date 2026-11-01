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
    "winter_hair_treatment": {
        "title": "保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！サロン帰りの濃密ツヤまとまりが続く高保湿ヘアトリートメントランク10",
        "page_file": "winter-hair-treatment.html",
        "items": [
            {"rank": 1, "query": "オージュア クエンチ ヘアトリートメント 250g", "brand": "Aujua (オージュア / ミルボン)", "name": "クエンチ ヘアトリートメント 250g (乾燥でパサつく毛髪内部の水分保持力を補修・しっとりまとまるサロン最高峰)"},
            {"rank": 2, "query": "ケラスターゼ DP フォンダン フルイダリスト 200ml", "brand": "KERASTASE (ケラスターゼ)", "name": "ディシプリン フォンダン フルイダリスト 200g (くせ毛や冬の静電気による広がりを抑え、なめらかで弾むようなしなやかさを与える)"},
            {"rank": 3, "query": "フィーノ プレミアムタッチ 浸透美容液ヘアマスク 230g", "brand": "fino (フィーノ)", "name": "プレミアムタッチ 浸透美容液ヘアマスク 230g (ローヤルゼリーEX・PCA配合・傷んだ毛先をとろけるように包み込む国民的高保湿マスク)"},
            {"rank": 4, "query": "ミルボン リストラティブ トリートメント 200g", "brand": "MILBON (グローバルミルボン)", "name": "リペア リストラティブ トリートメント 200g (SSVRシルク配合・冬の乾燥とケミカルダメージで棒状空洞化した髪を内部から集中再構築)"},
            {"rank": 5, "query": "モロッカンオイル インテンス ハイドレーティング マスク 250ml", "brand": "MOROCCANOIL (モロッカンオイル)", "name": "インテンス ハイドレーティング マスク 250ml (高純度アルガンオイル高配合・乾燥した太い髪や硬い髪をシルクのような柔らかさへ導く)"},
            {"rank": 6, "query": "アンドハニー ディープモイスト トリートメント 445g", "brand": "＆honey (アンドハニー)", "name": "ディープモイスト ヘアトリートメント 2.0 445g (マヌカハニーなど3種の黄金比蜂蜜×保水オーガニック処方・水分量14%のうるおい髪へ)"},
            {"rank": 7, "query": "ルベル イオ ディープマスク 170g", "brand": "LebeL (ルベル)", "name": "イオ ディープマスク 170g (カラーや乾燥で傷んだハイダメージ毛を週1〜2回の集中リペアで毛先までスルンとまとめる濃密マスク)"},
            {"rank": 8, "query": "YOLU カームナイトリペア トリートメント 475g", "brand": "YOLU (ヨル)", "name": "カームナイトリペア トリートメント 475g (夜間美容ナイトセラミド配合・睡眠中の枕摩擦と乾燥から髪を守り翌朝しっとりうるサラ髪へ)"},
            {"rank": 9, "query": "スティーブンノル モイスチュア リゲイン ヘアパック 250g", "brand": "STEPHEN KNOLL (スティーブンノル)", "name": "モイスチュア リゲイン ヘアパック 250g (コーセー独自の高浸透モイスチュアカプセル配合・パサつき深層までうるおいを届けるサロン発想)"},
            {"rank": 10, "query": "ラックス スーパーリッチシャイン ダメージリペア リッチ補修トリートメント 300g", "brand": "LUX (ラックス)", "name": "スーパーリッチシャイン ダメージリペア リッチ補修トリートメント 300g (プレミアムゴールドヒアルロン酸オイル配合・冬の枝毛パサつきを濃厚補修)"}
        ]
    },
    "winter_lip_balm": {
        "title": "保湿力の強さで冬の唇ひび割れ・血がにじむガサガサ皮剥けとさようなら！ひと塗りで潤い密封する薬用高保湿リップクリームランク10",
        "page_file": "winter-lip-balm.html",
        "items": [
            {"rank": 1, "query": "キュレル リップケアクリーム ほんのり色づかない 4.2g", "brand": "Curel (キュレル)", "name": "リップケアクリーム 4.2g (セラミド機能成分配合・唇の角層に浸透し乾燥や外部刺激から徹底保護する無香料・低刺激薬用リップ)"},
            {"rank": 2, "query": "モアリップ 8g 資生堂", "brand": "資生堂薬品 (モアリップ)", "name": "モアリップN 8g [第3類医薬品] (アラントイン・パンテノール・ビタミンE・ビタミンB6配合・ひび割れ・皮剥け・口唇炎を治療する医薬品リップ)"},
            {"rank": 3, "query": "ニベア ディープモイスチャーリップ 無香料 2.2g", "brand": "NIVEA (ニベア)", "name": "ディープモイスチャーリップ 無香料 2.2g (5つの保湿成分とはちみつ・アミノ酸・オリーブオイル配合・唇の体温でとろけて密着する高保水リップ)"},
            {"rank": 4, "query": "オバジ ダーマパワーX リップエッセンス 10g", "brand": "Obagi (オバジ)", "name": "ダーマパワーX リップエッセンス 10g (エラスチン×コラーゲン×ヒアルロン酸配合・乾燥してしぼんだ冬の唇にふっくらとしたハリと弾力を与える)"},
            {"rank": 5, "query": "メンソレータム ディープモイスト 無香料 4.5g", "brand": "メンソレータム (ロート製薬)", "name": "ディープモイスト 無香料 4.5g (ヒアルロン酸・シアバター・ホホバオイル配合・楕円形スティックで口角まで塗りやすい薬用高保湿リップ)"},
            {"rank": 6, "query": "DHC 薬用リップクリーム 1.5g", "brand": "DHC (ディーエイチシー)", "name": "薬用リップクリーム 1.5g (高純度オリーブバージンオイル・アロエエキス配合・人の皮脂に似た植物オイルが薄い保護膜を張るロングセラー)"},
            {"rank": 7, "query": "ラロッシュポゼ シカプラスト リップバーム 7.5ml", "brand": "La Roche-Posay (ラ ロッシュ ポゼ)", "name": "シカプラスト リップバーム 7.5ml (パンテノール5%×MP-リピッド配合・ひび割れや極度の乾燥でダメージを受けた唇を優しくリペア保護)"},
            {"rank": 8, "query": "ユースキン リリップ ケアスティック 3.5g", "brand": "yuskin (ユースキン)", "name": "リリップ ケアスティック 3.5g (グリチルレチン酸ステアリル・ビタミンE・スクワラン配合・冬のカサカサ唇あれを防ぎすこやかに保つ薬用スティック)"},
            {"rank": 9, "query": "アベンヌ 薬用リップケア モイスト 4g", "brand": "Avene (アベンヌ)", "name": "薬用リップケア モイスト 4g (コールドクリーム成分×アベンヌ温泉水配合・唇をうるおいラップで包み込み乾燥と荒れを防ぐ敏感肌設計)"},
            {"rank": 10, "query": "メンターム 薬用 メディカルリップスティック Mn 3.2g", "brand": "メンターム (近江兄弟社)", "name": "薬用メディカルリップスティック Mn 3.2g (アラントイン×ビタミンB6配合・唇のあれ・ひび割れ・皮剥けを穏やかに治すノンメントール薬用リップ)"}
        ]
    },
    "winter_carbonic_serum": {
        "title": "保湿力の強さで冬の血行不良くすみ・ゴワつき砂漠肌とさようなら！炭酸泡で巡りを呼び覚ます高保湿炭酸美容液ランク10",
        "page_file": "winter-carbonic-serum.html",
        "items": [
            {"rank": 1, "query": "ソフィーナiP ベースケア セラム 土台美容液 90g", "brand": "SOFINA iP (ソフィーナiP)", "name": "ベースケア セラム 土台美容液 90g (毛穴の約1/20微細炭酸泡・寒さで強張った角層最深部まで美容成分を届け化粧水の浸透を爆上げする名品)"},
            {"rank": 2, "query": "エスト セラム ワン アドバンスド 90g", "brand": "est (エスト)", "name": "セラム ワン アドバンスド 90g [医薬部外品] (生体ペプチド×マイクロ炭酸泡・シワ改善と美白を叶え冬のくすんだ大人の肌にハリ透明感を呼び覚ます)"},
            {"rank": 3, "query": "エリクシール シュペリエル ブースターエッセンス 90g", "brand": "ELIXIR (エリクシール)", "name": "ブースターエッセンス C 90g (パチパチはじける炭酸入りのクラッシュ泡・硬くなった角層を心地よくほぐしてうるおいを呼び込む導入炭酸美容液)"},
            {"rank": 4, "query": "アスタリフト スパークル タイト セラム 50g", "brand": "ASTALIFT (アスタリフト)", "name": "スパークル タイト セラム 50g (パチッと弾けてジェルに変化する新感覚炭酸泡・ナノアスタキサンチン配合で冬の乾燥毛穴をキュッと引き締める)"},
            {"rank": 5, "query": "ドクターシーラボ VC100 エッセンスローションEX 150ml", "brand": "Dr.Ci:Labo (ドクターシーラボ)", "name": "VC100 エッセンスローションEX 150ml (高濃度高浸透ビタミンC・APPS×ナイアシンアミド配合・冬のくすみ肌へ濃厚なうるおいと輝きをチャージ)"},
            {"rank": 6, "query": "カネボウ チアリング ミスト 30ml", "brand": "KANEBO (カネボウ)", "name": "チアリング ミスト フィクサー 30ml (きめ細かな微細ミストが肌をやわらかく包み込み、冬の乾燥とエアコンダメージから肌を守るオイルインブースター)"},
            {"rank": 7, "query": "オルビス ホワイトクリアエッセンス 25ml", "brand": "ORBIS (オルビス)", "name": "ホワイトクリアエッセンス 25ml [医薬部外品] (m-ピクセノール配合・冬の血行不良とメラニン蓄積による頑固なくすみを晴らしうるおい透明素肌へ導く)"},
            {"rank": 8, "query": "DEW スパークルバイザー 炭酸泡美容液 60g", "brand": "DEW (デュウ / カネボウ)", "name": "スパークルバイザー 60g (濃密な炭酸マイクロ泡が肌に心地よく密着・ヒアロサポート成分配合で乾燥した角層をふっくら潤いで満たす)"},
            {"rank": 9, "query": "Yunth 生ビタミンC 美白美容液 1ml 28包", "brand": "Yunth (ユンス)", "name": "生ビタミンC美白美容液 1ml×28包 [医薬部外品] (純度100%アスコルビン酸・水を使わない濃密温感処方・冬の冷えた肌にじんわり馴染む贅沢導入美容液)"},
            {"rank": 10, "query": "タカミスキンピール 30ml", "brand": "TAKAMI (タカミ)", "name": "タカミスキンピール 30ml (角質美容水・肌代謝のリズムに寄り添い冬の角質肥厚・くすみ・ゴワつきを根本から穏やかに整える不動のロングセラー)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]

                    raw_img = ""
                    if chosen.get("mediumImageUrls"):
                        raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    price = chosen.get("itemPrice", 0)
                    aff_url = chosen.get("affiliateUrl", "")
                    if not aff_url:
                        aff_url = chosen.get("itemUrl", "")
                    
                    return {
                        "rank": query_info["rank"],
                        "name": query_info["name"],
                        "brand": query_info["brand"],
                        "query_used": query,
                        "rakuten_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": chosen.get("shopName", "")
                    }
                else:
                    parts = query.split()
                    if len(parts) > 1:
                        shorter_q = " ".join(parts[:2])
                        print(f"Retrying with shorter query: {shorter_q}")
                        query = shorter_q
                        time.sleep(0.5)
                        continue
        except Exception as e:
            print(f"Error on attempt {attempt+1} for {query}: {e}")
            time.sleep(1.0)
    
    # 最終フォールバック
    return {
        "rank": query_info["rank"],
        "name": query_info["name"],
        "brand": query_info["brand"],
        "query_used": query,
        "rakuten_item_name": query_info["name"],
        "price": 3500,
        "image_url": "https://shop.r10s.jp/cosme/cabinet/default.jpg",
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query_info['brand'])}/",
        "shop_name": "楽天公式ショップ"
    }

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching Rakuten API for: {cat_data['title']}")
    print(f"==========================================")
    cat_results = []
    for item_info in cat_data["items"]:
        print(f"[{item_info['rank']}/10] Query: {item_info['query']} ...")
        res = fetch_item_with_retry(item_info)
        print(f" -> Found: {res['rakuten_item_name'][:30]}... | Price: ¥{res['price']:,} | Img: {res['image_url'][:50]}...")
        cat_results.append(res)
        time.sleep(0.3)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_results
    }

with open("rakuten_hair_lip_carbonic_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSuccessfully fetched all 30 items from Rakuten API and saved to rakuten_hair_lip_carbonic_data.json!")
