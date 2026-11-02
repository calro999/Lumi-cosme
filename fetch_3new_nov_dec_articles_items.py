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
    "winter_exosome_serum": {
        "title": "保湿力の強さで冬の肌荒れ・しぼみ肌とさようなら！次世代細胞サイエンスで角層深部から押し返す高保湿エクソソーム美容液ランク10",
        "page_file": "winter-exosome-serum.html",
        "items": [
            {"rank": 1, "query": "メディキューブ ゼロポア エクソソーム ショット", "brand": "medicube (メディキューブ)", "name": "ゼロポア エクソソーム ショット 2000 30ml (超微細エクソソームコーティングニードルが角層奥深くまで浸透！冬の乾燥毛穴・たるみを引き締める)"},
            {"rank": 2, "query": "KISO ステム セラム X エクソソーム", "brand": "KISO (キソ)", "name": "ステム セラム X 30ml (国産ヒト幹細胞順化培養液＆エクソソーム高配合！冬の寒冷で低下した肌活力を底上げする原液美容液)"},
            {"rank": 3, "query": "フラコラ ヒト幹細胞培養エキス エクソソーム", "brand": "fracora (フラコラ)", "name": "ヒト幹細胞培養エキス原液 LP 30ml (ナノサイズのリポソームエクソソームが素早く角層深部へ。冬枯れ肌に湧き上がるハリ感)"},
            {"rank": 4, "query": "GD11 プレミアム エクソソーム アンプル", "brand": "GD11 (ジーディーイレブン)", "name": "アドバンスド ラボ エクソソーム アンプル (臍帯血幹細胞由来の高純度エクソソーム！冬の深刻な乾燥小ジワをふっくら持ち上げる)"},
            {"rank": 5, "query": "ディレイア ステム セラム EX ソーム", "brand": "direia (ディレイア)", "name": "ステム セラム EX ソーム 30ml (サロン専売クオリティのハイブリッドエクソソーム。国際特許浸透技術で真冬の肌を徹底プロテクト)"},
            {"rank": 6, "query": "Dr.Melaxin セラミド エクソソーム アンプル", "brand": "Dr.Melaxin (ドクターメラクチン)", "name": "セパ ダーマ エクソソーム アンプル 30ml (セラミド×エクソソームの強力タッグ！暖房によるバリア機能低下とインナードライを根本修復)"},
            {"rank": 7, "query": "セルロジーコスメ リッチエッセンス エクソソーム", "brand": "Cellreva (セルロジーコスメ)", "name": "リッチエッセンス 30ml (ヒト幹細胞エキス＆エクソソーム配合！濃密な潤いヴェールで冬の乾燥によるゴワつきを柔らかくほぐす)"},
            {"rank": 8, "query": "アンレーベル ラボ エクソソーム 美容液", "brand": "unlabel LAB (アンレーベル ラボ)", "name": "超高圧 浸透型 エクソソーム 配合 美容液 50ml (100MPaの超高圧処理で抽出したエクソソームが肌のすみずみまで浸透しキメ密度アップ)"},
            {"rank": 9, "query": "魔女工場 パンテトイン エッセンス", "brand": "manyo (魔女工場)", "name": "パンテトイン エッセンス トナー 200ml (高純度パンテノール×エクトインの高保水設計！エクソソーム技術で角層の水分保持力を限界突破)"},
            {"rank": 10, "query": "リジェンスキン SRS セラム ダーマ", "brand": "RegenSkin (リジェンスキン)", "name": "SRS セラム ダーマ エクソソーム 30ml (美容クリニックの術後ケアでも絶賛される成長因子＆エクソソーム処方で冬のゆらぎ肌をリセット)"}
        ]
    },
    "winter_bath_milk": {
        "title": "保湿力の強さで冬の全身粉吹き乾燥・かゆみとさようなら！お湯が極上美容液に変わる高保湿バスミルク・薬用ミルク入浴液ランク10",
        "page_file": "winter-bath-milk.html",
        "items": [
            {"rank": 1, "query": "アユーラ メディテーションバス t 300ml", "brand": "AYURA (アユーラ)", "name": "メディテーションバス t 300ml (お湯に入れた瞬間乳白色に変化！安らかなハーブの香りと植物オイルでしっとり滑らかな極上肌へ)"},
            {"rank": 2, "query": "キュレル 入浴液 本体 420ml", "brand": "Curel (キュレル)", "name": "薬用 入浴液 420ml (セラミド機能成分×ユーカリエキス配合！お風呂上がり直後の乾燥やつっぱりを防ぎ全身しっとり潤す)"},
            {"rank": 3, "query": "カウブランド 無添加 保湿バスミルク 本体 560ml", "brand": "牛乳石鹸 カウブランド", "name": "無添加 保湿バスミルク 560ml (天然由来セラミド配合・無香料・弱酸性！デリケートな冬の乾燥肌を優しく包み込むミルク入浴液)"},
            {"rank": 4, "query": "ミノン 薬用保湿入浴剤 480ml", "brand": "MINON (ミノン)", "name": "薬用 保湿入浴剤 480ml (11種のアミノ酸配合！冬の乾燥で粉を吹きやすいすねやひじの角質層を柔らかく潤す敏感肌設計)"},
            {"rank": 5, "query": "ヴェレダ モミ バスミルク 200ml", "brand": "WELEDA (ヴェレダ)", "name": "モミ バスミルク 200ml (針葉樹の澄んだ森林の香りと植物油！真冬の冷え切った身体を温めながら肌の乾燥を防ぐオーガニックバス)"},
            {"rank": 6, "query": "ウルモア 保湿入浴液 クリーミーフローラル 600ml", "brand": "アース製薬 ウルモア", "name": "保湿入浴液 クリーミーフローラル 600ml (5種の保湿成分配合のとろりとした濃厚ミルク湯！全身をうるおいヴェールでラッピング)"},
            {"rank": 7, "query": "クナイプ バスミルク コットンミルク 480ml", "brand": "Kneipp (クナイプ)", "name": "バスミルク コットンミルクの香り 480ml (天然シアバター＆植物オイル配合！泡風呂としても楽しめる贅沢な高保湿ミルク入浴剤)"},
            {"rank": 8, "query": "ニールズヤード アロマティック バスミルク 200ml", "brand": "NEAL\x27S YARD REMEDIES", "name": "アロマティック バスミルク 200ml (オーガニック植物オイルとラベンダー精油の贅沢ブレンド！冬の乾燥肌をしなやかに整える)"},
            {"rank": 9, "query": "エモリカ 薬用スキンケア入浴液 フローラルの香り", "brand": "花王 エモリカ", "name": "薬用 スキンケア入浴液 450ml (セラミドAP+・ユーカリエキス配合！カサつきがちな冬の素肌に潤い成分をしっかり届ける薬用ミルク湯)"},
            {"rank": 10, "query": "バスクリン ピュアスキン 贅沢 プラセンタ 白濁", "brand": "バスクリン (BATHCLIN)", "name": "ピュアスキン 贅沢 プラセンタ 600g (濃密なミルクホワイトの湯とプラセンタエキスで、冬のお風呂上がりもつっぱらないすべすべ美肌へ)"}
        ]
    },
    "winter_glutathione_serum": {
        "title": "保湿力の強さで冬のどんより乾燥くすみ・透明感不足とさようなら！濃密保湿×白玉グルタチオンで発光ツヤ肌へ導く高保湿グルタチオン美容液ランク10",
        "page_file": "winter-glutathione-serum.html",
        "items": [
            {"rank": 1, "query": "ナンバーズイン 5番 白玉グルタチオンC 美容液 30ml", "brand": "numbuzin (ナンバーズイン)", "name": "5番 白玉グルタチオンC ふりかけマスク 美容液 30ml (高純度グルタチオン×ビタミンCカプセル！冬のどんより乾燥くすみを一掃するメガヒット)"},
            {"rank": 2, "query": "Anua ナイアシンアミド 10% TXA 4% セラム", "brand": "Anua (アヌア)", "name": "ナイアシンアミド 10% + TXA 4% セラム 30ml (トラネキサム酸×アルブチン×グルタチオン配合！冬の乾燥くすみ・色ムラを徹底ケア)"},
            {"rank": 3, "query": "メディキューブ ディープ グルタチオン 21% アンプル", "brand": "medicube (メディキューブ)", "name": "ディープ グルタチオン 21% アンプル 50ml (純度99%の高濃度グルタチオン配合！内側から光を放つような白玉トーンアップ肌へ)"},
            {"rank": 4, "query": "Dr.Althea グルタチオン デュアル ブースティング セラム", "brand": "Dr.Althea (ドクターエルシア)", "name": "グルタチオン デュアル ブースティング セラム (冬の乾燥で硬くなった角層を柔らかくほぐし、グルタチオンの浸透を高めるツヤ肌ブースター)"},
            {"rank": 5, "query": "BIOHEAL BOH グルタチオン トーニング アンプル", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "プロバイオダーム コラーゲン リフレッシュ トーニング アンプル 30ml (ペプチド×グルタチオンで冬の弾力低下とくすみをダブル解決)"},
            {"rank": 6, "query": "センテリアン24 マデカ グルタチオン アンプル", "brand": "Centellian24 (センテリアン24)", "name": "マデカ グルタチオン トーニング アンプル 50ml (製薬会社品質のTECAツボクサエキス×白玉グルタチオン！敏感肌でも使える低刺激ホワイトニング)"},
            {"rank": 7, "query": "APRILSKIN カロテン IPMP セラム グルタチオン", "brand": "APRILSKIN (エイプリルスキン)", "name": "カロテン IPMP グルタチオン 美容液 30ml (高純度グルタチオンとカロテンが肌荒れを防ぎながら冬のくすみを晴らす)"},
            {"rank": 8, "query": "KISO ピュアエッセンス GL グルタチオン 30ml", "brand": "KISO (キソ)", "name": "ピュアエッセンス GL グルタチオン 原液美容液 30ml (余計な添加物を省いた高濃度グルタチオン原液！濃密な潤いでキメの整った白玉肌へ)"},
            {"rank": 9, "query": "ネイチャーリパブリック ビタペアC アンプル 45ml", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "ビタペアC シミケア アンプル 45ml (済州島グリーンレモン×ナイアシンアミド×グルタチオン！乾燥によるくすみ・毛穴悩みを集中撃退)"},
            {"rank": 10, "query": "MEDIHEAL ホワイトミルク 美容液", "brand": "MEDIHEAL (メディヒール)", "name": "ミルクブライトニング セラム 40ml (初乳セラミド×グルタチオン配合！ミルキーな潤いで冬の乾燥肌を白玉のようにふっくら満たす)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    
    fallbacks = [query]
    parts = query.split()
    if len(parts) >= 3:
        fallbacks.append(" ".join(parts[:3]))
    if len(parts) >= 2:
        fallbacks.append(" ".join(parts[:2]))
    if len(parts) >= 1:
        fallbacks.append(parts[0])

    for q_try in fallbacks:
        for attempt in range(4):
            try:
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q_try)}&hits=5&format=json&sort=standard"
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
                        
                        price = chosen.get("itemPrice", 0)
                        aff_url = chosen.get("affiliateUrl", "")
                        images = chosen.get("mediumImageUrls", [])
                        img_url = ""
                        if images:
                            img_url = images[0].get("imageUrl", "")
                        
                        if price > 0 and aff_url and img_url and "sample/item.jpg" not in img_url:
                            print(f"  ✓ Found: {q_try} -> {price}円 | Image: {img_url[:40]}...")
                            return {
                                "rank": query_info["rank"],
                                "brand": query_info["brand"],
                                "name": query_info["name"],
                                "queryUsed": q_try,
                                "itemName": chosen.get("itemName", ""),
                                "price": price,
                                "affiliateUrl": aff_url,
                                "image": img_url
                            }
            except Exception as e:
                print(f"  Retry attempt {attempt+1} for {q_try}: {e}")
                time.sleep(1.2)
        time.sleep(0.5)
    
    print(f"  ❌ FAILED to find valid item for {raw_q}")
    return None

results = {}

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
    print(f"==========================================")
    cat_items = []
    for item_info in cat_data["items"]:
        print(f"Rank {item_info['rank']}: {item_info['brand']} - {item_info['query']}")
        item_res = fetch_item_with_retry(item_info)
        if item_res:
            cat_items.append(item_res)
        else:
            raise RuntimeError(f"Could not fetch item for {item_info}")
        time.sleep(0.4)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

output_file = "fetched_3new_nov_dec_articles_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Successfully fetched all 30 items via Rakuten API and saved to {output_file}!")
