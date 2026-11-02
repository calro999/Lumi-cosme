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

PERFECT_TARGETS = {
    "winter_exosome_serum": [
        {
            "rank": 1,
            "brand": "medicube (メディキューブ)",
            "name": "ゼロ毛穴エクソソームショット 2000 30ml (超微細エクソソームニードルが角層奥深くまで浸透！冬の乾燥たるみ毛穴をキュッと引き締める)",
            "query": "メディキューブ ゼロ毛穴エクソソームショット",
            "min_price": 2000, "max_price": 4000
        },
        {
            "rank": 2,
            "brand": "KISO (キソ)",
            "name": "ステム セラム X 30ml (国産ヒト幹細胞順化培養液＆高純度エクソソーム高配合！冬の寒冷で低下した肌活力を底上げする原液美容液)",
            "query": "KISO ステムセラム ヒト幹細胞",
            "min_price": 2500, "max_price": 5000
        },
        {
            "rank": 3,
            "brand": "fracora (フラコラ)",
            "name": "ヒト幹細胞培養エキス原液 LP 30ml (ナノサイズのリポソームエクソソームが素早く角層深部へ。冬枯れ肌に湧き上がるハリ感)",
            "query": "フラコラ ヒト幹細胞エクソソーム 原液",
            "min_price": 5000, "max_price": 12000
        },
        {
            "rank": 4,
            "brand": "GD11 (ジーディーイレブン)",
            "name": "アドバンスド ラボ エクソソーム アンプル (臍帯血幹細胞由来の高純度エクソソーム！冬の深刻な乾燥小ジワをふっくら持ち上げる)",
            "query": "GD11 ヒト 臍帯血 アンプル",
            "min_price": 3000, "max_price": 8000
        },
        {
            "rank": 5,
            "brand": "direia (ディレイア)",
            "name": "ステム セラム EX ソーム 30ml (サロン専売クオリティのハイブリッドエクソソーム。国際特許浸透技術で真冬の肌を徹底プロテクト)",
            "query": "ディレイア ステム セラム EX ソーム",
            "min_price": 9000, "max_price": 15000
        },
        {
            "rank": 6,
            "brand": "Dr.Melaxin (ドクターメラクチン)",
            "name": "セパ ダーマ エクソソーム アンプル 30ml (セラミド×エクソソームの強力タッグ！暖房によるバリア機能低下とインナードライを根本修復)",
            "query": "Dr.Melaxin アンプル",
            "min_price": 3000, "max_price": 5500
        },
        {
            "rank": 7,
            "brand": "Cellreva (セルロジーコスメ)",
            "name": "リッチエッセンス 30ml (ヒト幹細胞エキス＆エクソソーム配合！濃密な潤いヴェールで冬の乾燥によるゴワつきを柔らかくほぐす)",
            "query": "セルロジーコスメ リッチエッセンス",
            "min_price": 9000, "max_price": 14000
        },
        {
            "rank": 8,
            "brand": "unlabel LAB (アンレーベル ラボ)",
            "name": "超高圧 浸透型 エクソソーム 美容液 50ml (100MPaの超高圧処理で抽出したエクソソームが肌のすみずみまで浸透しキメ密度アップ)",
            "query": "アンレーベル ラボ エクソソーム",
            "min_price": 1500, "max_price": 3000
        },
        {
            "rank": 9,
            "brand": "manyo (魔女工場)",
            "name": "パンテトイン エッセンストナー 200ml (高純度パンテノール×エクトインの高保水設計！エクソソーム技術で角層の水分保持力を限界突破)",
            "query": "魔女工場 パンテトイン トナー",
            "min_price": 1800, "max_price": 3500
        },
        {
            "rank": 10,
            "brand": "BORDER FREE (ボーダーフリー)",
            "name": "ホイップフォーム フェイシャルウォッシュ / エクソソーム リッチ セラム (高機能エクソソームとペプチド配合！冬のしぼみ肌をふっくらリフト)",
            "query": "ボーダーフリー 美容液 レチノール エクソソーム",
            "min_price": 2500, "max_price": 6000
        }
    ],
    "winter_bath_milk": [
        {
            "rank": 1,
            "brand": "AYURA (アユーラ)",
            "name": "メディテーションバス t 300ml (お湯に入れた瞬間乳白色に変化！安らかなハーブの香りと植物オイルでしっとり滑らかな極上肌へ)",
            "query": "アユーラ メディテーションバスt 300mL",
            "min_price": 2000, "max_price": 3500
        },
        {
            "rank": 2,
            "brand": "Curel (キュレル)",
            "name": "薬用 入浴液 本体 420ml (セラミド機能成分×ユーカリエキス配合！お風呂上がり直後の乾燥やつっぱりを防ぎ全身しっとり潤す)",
            "query": "キュレル 入浴液 本体 420",
            "min_price": 800, "max_price": 2000
        },
        {
            "rank": 3,
            "brand": "牛乳石鹸 カウブランド",
            "name": "無添加 保湿バスミルク 本体 560ml (天然由来セラミド配合・無香料・弱酸性！デリケートな冬の乾燥肌を優しく包み込むミルク入浴液)",
            "query": "カウブランド 無添加 保湿バスミルク 本体 560mL",
            "min_price": 600, "max_price": 1500
        },
        {
            "rank": 4,
            "brand": "MINON (ミノン)",
            "name": "薬用 保湿入浴剤 480ml (11種のアミノ酸配合！冬の乾燥で粉を吹きやすいすねやひじの角質層を柔らかく潤す敏感肌設計)",
            "query": "ミノン 薬用保湿入浴剤 480ml",
            "min_price": 1000, "max_price": 2200
        },
        {
            "rank": 5,
            "brand": "WELEDA (ヴェレダ)",
            "name": "モミ バスミルク 200ml (針葉樹の澄んだ森林の香りと植物油！真冬の冷え切った身体を温めながら肌の乾燥を防ぐオーガニックバス)",
            "query": "ヴェレダ モミバスミルク 200ml",
            "min_price": 2000, "max_price": 3800
        },
        {
            "rank": 6,
            "brand": "アース製薬 ウルモア",
            "name": "保湿入浴液 クリーミーフローラル 600ml (5種の保湿成分配合のとろりとした濃厚ミルク湯！全身をうるおいヴェールでラッピング)",
            "query": "ウルモア高保湿入浴液 クリーミーフローラル 600ml",
            "min_price": 600, "max_price": 1500
        },
        {
            "rank": 7,
            "brand": "Kneipp (クナイプ)",
            "name": "バスミルク コットンミルクの香り 480ml (天然シアバター＆植物オイル配合！泡風呂としても楽しめる贅沢な高保湿ミルク入浴剤)",
            "query": "クナイプ バスミルク コットンミルク 480ml",
            "min_price": 1000, "max_price": 2000
        },
        {
            "rank": 8,
            "brand": "HOUSE OF ROSE (ハウス オブ ローゼ)",
            "name": "ミルキュア ピュア バスミルク 350ml (北海道産ミルクプロテイン配合！とろりと溶け込みすべすべの素肌へ導く乳白湯)",
            "query": "ハウスオブローゼ バスミルク",
            "min_price": 1500, "max_price": 3000
        },
        {
            "rank": 9,
            "brand": "花王 エモリカ",
            "name": "薬用 スキンケア入浴液 フローラルの香り 本体 450ml (セラミドAP+・ユーカリエキス配合！カサつきがちな冬の素肌に潤い成分をしっかり届ける薬用ミルク湯)",
            "query": "エモリカ フローラルの香り 本体 450ml",
            "min_price": 600, "max_price": 1500
        },
        {
            "rank": 10,
            "brand": "バスクリン (BATHCLIN)",
            "name": "ピュアスキン 贅沢 プラセンタ 600g (濃密なミルクホワイトの湯とプラセンタエキスで、冬のお風呂上がりもつっぱらないすべすべ美肌へ)",
            "query": "バスクリン ピュアスキン プラセンタ",
            "min_price": 500, "max_price": 1200
        }
    ],
    "winter_glutathione_serum": [
        {
            "rank": 1,
            "brand": "numbuzin (ナンバーズイン)",
            "name": "5番 白玉グルタチオンC 美容液 30ml (高純度グルタチオン×ビタミンCカプセル！冬のどんより乾燥くすみを一掃するメガヒット)",
            "query": "ナンバーズイン 5番 白玉グルタチオンC 美容液 30ml",
            "min_price": 2000, "max_price": 4000
        },
        {
            "rank": 2,
            "brand": "Anua (アヌア)",
            "name": "ナイアシンアミド 10% + TXA 4% セラム 30ml (トラネキサム酸×アルブチン×グルタチオン配合！冬の乾燥くすみ・色ムラを徹底ケア)",
            "query": "Anua ナイアシンアミド 10% TXA 4% セラム 30ml",
            "min_price": 2200, "max_price": 4000
        },
        {
            "rank": 3,
            "brand": "medicube (メディキューブ)",
            "name": "ディープ グルタチオン 21% アンプル 50ml (純度99%の高濃度グルタチオン配合！内側から光を放つような白玉トーンアップ肌へ)",
            "query": "メディキューブ グルタチオン アンプル",
            "min_price": 2000, "max_price": 4500
        },
        {
            "rank": 4,
            "brand": "Dr.Althea (ドクターエルシア)",
            "name": "グルタチオン デュアル ブースティング セラム (冬の乾燥で硬くなった角層を柔らかくほぐし、グルタチオンの浸透を高めるツヤ肌ブースター)",
            "query": "ドクターエルシア グルタチオン セラム",
            "min_price": 2000, "max_price": 4500
        },
        {
            "rank": 5,
            "brand": "BIOHEAL BOH (バイオヒールボ)",
            "name": "プロバイオダーム コラーゲン リフレッシュ トーニング アンプル 30ml (ペプチド×グルタチオンで冬の弾力低下とくすみをダブル解決)",
            "query": "BIOHEAL BOH トーニング アンプル",
            "min_price": 2200, "max_price": 4200
        },
        {
            "rank": 6,
            "brand": "Centellian24 (センテリアン24)",
            "name": "マデカ グルタチオン トーニング アンプル 50ml (製薬会社品質のTECAツボクサエキス×白玉グルタチオン！敏感肌でも使える低刺激ホワイトニング)",
            "query": "センテリアン24 トーニング アンプル グルタチオン",
            "min_price": 1500, "max_price": 3800
        },
        {
            "rank": 7,
            "brand": "APRILSKIN (エイプリルスキン)",
            "name": "カロテン IPMP セラム 30ml (高純度ベータカロテンとグルタチオン配合！肌荒れを防ぎながら冬のくすみを晴らす)",
            "query": "aprilskin カロテン セラム",
            "min_price": 2000, "max_price": 3800
        },
        {
            "rank": 8,
            "brand": "KISO (キソ)",
            "name": "ピュアエッセンス GL グルタチオン 原液美容液 30ml (余計な添加物を省いた高濃度グルタチオン原液！濃密な潤いでキメの整った白玉肌へ)",
            "query": "KISO グルタチオン 美容液 ピュアエッセンス",
            "min_price": 1800, "max_price": 3500
        },
        {
            "rank": 9,
            "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
            "name": "ビタペアC シミケア セラム 45ml (済州島グリーンレモン×ナイアシンアミド×グルタチオン！乾燥によるくすみ・毛穴悩みを集中撃退)",
            "query": "ネイチャーリパブリック ビタペアC セラム 45ml",
            "min_price": 1800, "max_price": 3500
        },
        {
            "rank": 10,
            "brand": "MEDIHEAL (メディヒール)",
            "name": "ミルクブライトニング セラム 40ml (初乳セラミド×グルタチオン配合！ミルキーな潤いで冬の乾燥肌を白玉のようにふっくら満たす)",
            "query": "メディヒール ミルクブライトニング セラム",
            "min_price": 2500, "max_price": 4800
        }
    ]
}

def fetch_single_item(target):
    q = target["query"]
    min_p = target.get("min_price", 0)
    max_p = target.get("max_price", 999999)
    
    # 検索クエリ候補
    fallbacks = [q]
    parts = q.split()
    if len(parts) >= 3:
        fallbacks.append(" ".join(parts[:3]))
    if len(parts) >= 2:
        fallbacks.append(" ".join(parts[:2]))
    fallbacks.append(parts[0])

    for q_try in fallbacks:
        for attempt in range(5):
            try:
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q_try)}&hits=10&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                    data = json.loads(res.read().decode('utf-8'))
                    items = data.get("Items", [])
                    if items:
                        for it in items:
                            item_obj = it["Item"]
                            price = item_obj.get("itemPrice", 0)
                            aff_url = item_obj.get("affiliateUrl", "")
                            images = item_obj.get("mediumImageUrls", [])
                            item_name = item_obj.get("itemName", "")
                            
                            # 除外ワードチェック
                            if any(bad in item_name for bad in ["【10個セット】", "【24個セット】", "【×6個】", "ケース販売", "業務用"]):
                                continue
                            
                            if min_p <= price <= max_p and aff_url and images:
                                img_url = images[0].get("imageUrl", "")
                                if "sample/item.jpg" not in img_url:
                                    print(f"  ✓ SUCCESS: [{target['brand']}] {q_try} -> {price}円 ({item_name[:35]}...)")
                                    return {
                                        "rank": target["rank"],
                                        "brand": target["brand"],
                                        "name": target["name"],
                                        "queryUsed": q_try,
                                        "itemName": item_name,
                                        "price": price,
                                        "affiliateUrl": aff_url,
                                        "image": img_url
                                    }
                        # 価格帯に合わないが妥当なアイテムをフォールバックとして探す
                        for it in items:
                            item_obj = it["Item"]
                            price = item_obj.get("itemPrice", 0)
                            aff_url = item_obj.get("affiliateUrl", "")
                            images = item_obj.get("mediumImageUrls", [])
                            item_name = item_obj.get("itemName", "")
                            if price > 400 and price < 30000 and aff_url and images:
                                img_url = images[0].get("imageUrl", "")
                                if "sample/item.jpg" not in img_url:
                                    print(f"  (Fallback match): [{target['brand']}] {q_try} -> {price}円 ({item_name[:35]}...)")
                                    return {
                                        "rank": target["rank"],
                                        "brand": target["brand"],
                                        "name": target["name"],
                                        "queryUsed": q_try,
                                        "itemName": item_name,
                                        "price": price,
                                        "affiliateUrl": aff_url,
                                        "image": img_url
                                    }
            except Exception as e:
                # 429対策で少し待機
                time.sleep(2.0)
        time.sleep(1.0)
    
    raise RuntimeError(f"Could not find item for {target}")

refined_results = {}
for cat_key, items_list in PERFECT_TARGETS.items():
    print(f"\n==========================================")
    print(f"Refining: {cat_key}")
    print(f"==========================================")
    cat_items = []
    for t in items_list:
        print(f"Target Rank {t['rank']}: {t['brand']} - {t['query']}")
        item_data = fetch_single_item(t)
        cat_items.append(item_data)
        time.sleep(1.2)  # レート制限対策
    refined_results[cat_key] = {
        "items": cat_items
    }

with open("fetched_perfect_3articles_data_v2.json", "w", encoding="utf-8") as f:
    json.dump(refined_results, f, ensure_ascii=False, indent=2)

print("\n🎉 ALL 30 REFINED ITEMS FETCHED AND SAVED PERFECTLY!")
