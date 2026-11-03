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
    "winter_proteoglycan": {
        "title": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸超えの保水力で乾燥小ジワを撃退する高純度プロテオグリカン原液ランク10",
        "page_file": "winter-proteoglycan.html",
        "items": [
            {"rank": 1, "query": "フラコラ プロテオグリカン原液 30ml", "brand": "fracora (フラコラ)", "name": "プロテオグリカン原液 30ml (高純度・高濃度・浸透型リフト保水原液)"},
            {"rank": 2, "query": "チューンメーカーズ プロテオグリカン 20ml", "brand": "TUNEMAKERS (チューンメーカーズ)", "name": "プロテオグリカン原液 20ml (乾燥小ジワ・ハリ弾力集中保水エッセンス)"},
            {"rank": 3, "query": "PG2 ピュアエッセンス 10ml", "brand": "PG2 (ジョイフルライフ)", "name": "ピュアエッセンス 10ml (高純度プロテオグリカン原液・真空容器採用)"},
            {"rank": 4, "query": "KISO キソ プロテオグリカン 原液 20ml", "brand": "KISO (基礎化粧品研究所)", "name": "プロテオグリカンエッセンス PG 20ml (国産サケ鼻軟骨由来100%原液)"},
            {"rank": 5, "query": "北海道ナチュラルバイオ プロテオグリカン 原液", "brand": "北海道ナチュラルバイオ", "name": "ピュアプロテオグリカン 100% 原液 20ml (あおもりPG認定・超高純度抽出)"},
            {"rank": 6, "query": "自然化粧品研究所 プロテオグリカン原液 30ml", "brand": "自然化粧品研究所", "name": "プロテオグリカン原液 30ml (防腐剤無添加・うるおいバリア高保水)"},
            {"rank": 7, "query": "リッチフェイシャルエッセンス プロテオグリカン", "brand": "BEAUTY AVENUE", "name": "リッチフェイシャルエッセンス プロテオグリカン 30ml (大容量高浸透美容原液)"},
            {"rank": 8, "query": "プラワンシー プレミアム ハイドロゲル アイパッチ プロテオグリカン", "brand": "+ONEC (プラワンシー)", "name": "プレミアム ハイドロゲル アイパッチ (プロテオグリカン＆ツバメの巣配合目元集中ケア)"},
            {"rank": 9, "query": "ナチュドール プロテオグリカン 原液 20ml", "brand": "NATUDOR (ナチュドール)", "name": "プロテオグリカン原液 20ml (高濃度・肌密度を高める深層保水)"},
            {"rank": 10, "query": "ジャパンギャルズ SC プロテオグリカン 原液 100", "brand": "JAPAN GALS (ジャパンギャルズ)", "name": "ピュアビューエッセンス プロテオグリカン原液 100% 25ml (乾燥肌救済プチプラ原液)"}
        ]
    },
    "winter_propolis": {
        "title": "保湿力の強さで肌乾燥とさようなら！濃密な栄養と蜜膜ヴェールで肌荒れ・粉吹きを防ぐ高保湿プロポリスアンプルランク10",
        "page_file": "winter-propolis.html",
        "items": [
            {"rank": 1, "query": "CNP Laboratory プロポリス エナジー アンプル 15ml", "brand": "CNP Laboratory (チャアンドパク)", "name": "プロポリス エナジー アクティブ アンプル 15ml (濃厚蜜光ツヤ・高純度プロポリスエキス)"},
            {"rank": 2, "query": "COSRX フルフィット プロポリス ライト アンプル 30ml", "brand": "COSRX (コスアールエックス)", "name": "フルフィット プロポリス ライト アンプル 30ml (黒蜂プロポリス83.25%高配合)"},
            {"rank": 3, "query": "スキンフード ロイヤルハニー プロポリス エンリッチ エッセンス", "brand": "SKINFOOD (スキンフード)", "name": "ロイヤルハニー プロポリス エンリッチ エッセンス 50ml (熟成プロポリス63%発酵バリア)"},
            {"rank": 4, "query": "バイオヒールボ プロバイオダーム コラーゲン リモデリング セラム", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "プロバイオダーム タイトニング コラーゲン セラム 30ml (プロポリス＆乳酸菌ダブル保湿)"},
            {"rank": 5, "query": "Dr.G ドクタージー ロイヤルブラック スネイル アンプル", "brand": "Dr.G (ドクタージー)", "name": "ロイヤルブラックスネイル ファーストアンプル 165ml (ロイヤルゼリー＆プロポリス高保湿導入液)"},
            {"rank": 6, "query": "ネイチャーリパブリック プロポリス インテンス セラム", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "ハーブオロジー プロポリス エナジー セラム 50ml (グリーンプロポリス配合濃密鎮静セラム)"},
            {"rank": 7, "query": "トニーモリー タイムレス 発酵 スネイル アンプル", "brand": "TONYMOLY (トニーモリー)", "name": "インテンス ケア ゴールド 24K スネール アンプル 100ml (プロポリス＆ゴールド濃密潤いヴェール)"},
            {"rank": 8, "query": "VT コスメティックス プログロス ゴールド カプセル マスク", "brand": "VT COSMETICS (ブイトーク)", "name": "プログロス ゴールド カプセル マスク (プロポリス＆24Kゴールド集中ツヤ栄養パック)"},
            {"rank": 9, "query": "ミシャ ビーポレン リニュー アンプラー", "brand": "MISSHA (ミシャ)", "name": "ビーポレン リニュー アンプラー 40ml (花粉エキス＆プロポリス抗酸化高保湿アンプル)"},
            {"rank": 10, "query": "ホリカホリカ ハニー ローヤルゼリー アンプル", "brand": "HOLIKA HOLIKA (ホリカホリカ)", "name": "ハニーロイヤルカプセル エッセンス 50ml (生ローヤルゼリーカプセル＆蜜膜シールド)"}
        ]
    },
    "winter_galactomyces": {
        "title": "保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10",
        "page_file": "winter-galactomyces.html",
        "items": [
            {"rank": 1, "query": "魔女工場 ガラク ナイアシン 2.0 エッセンス 50ml", "brand": "魔女工場 (Manyo Factory)", "name": "ガラク ナイアシン 2.0 エッセンス 50ml (高純度ガラクトミセス93.69%＋ナイアシンアミド4%)"},
            {"rank": 2, "query": "SK-II フェイシャル トリートメント エッセンス 230ml", "brand": "SK-II (エスケーツー)", "name": "フェイシャル トリートメント エッセンス 230ml (ピテラ/ガラクトミセス培養液90%以上配合の最高峰)"},
            {"rank": 3, "query": "COSRX ガラクトミセス 95 トーン バランシング エッセンス", "brand": "COSRX (コスアールエックス)", "name": "ガラクトミセス 95 トーン バランシング エッセンス 100ml (高濃縮発酵ろ過物95%配合)"},
            {"rank": 4, "query": "ワンシング ガラクトミセス 培養液 150ml", "brand": "ONE THING (ワンシング)", "name": "ガラクトミセス 培養液 150ml (100%植物性ヴィーガン発酵エキス化粧水)"},
            {"rank": 5, "query": "KISO キソ ガラクトミセス 原液 20ml", "brand": "KISO (基礎化粧品研究所)", "name": "ガラクトミセス エッセンス GM 20ml (無添加・国産高純度ガラクトミセス原液)"},
            {"rank": 6, "query": "ミシャ タイムレボリューション ザ ファースト トリートメント エッセンス", "brand": "MISSHA (ミシャ)", "name": "タイムレボリューション ザ ファースト トリートメント エッセンス 5X 150ml (極限発酵酵母エキス97%)"},
            {"rank": 7, "query": "シークレットキー スターティング トリートメント エッセンス", "brand": "Secret Key (シークレットキー)", "name": "スターティング トリートメント エッセンス ローズ 150ml (ダマスクローズ水＆ガラクトミセス配合)"},
            {"rank": 8, "query": "フロムネイチャー エイジ トリートメント エッセンス 150ml", "brand": "FROM NATURE (フロムネイチャー)", "name": "AGE インテンス トリートメント エッセンス 150ml (ガラクトミセス発酵ろ過物95.7%配合)"},
            {"rank": 9, "query": "自然化粧品研究所 ガラクトミセス 培養液 100ml", "brand": "自然化粧品研究所", "name": "ガラクトミセス培養液 100ml (NMF産生促進・キメ密度向上原液)"},
            {"rank": 10, "query": "ピュアビタミン ガラクトミセス 美容液", "brand": "VELY VELY (ブリーブリー)", "name": "ガラクトミセス オールインワン ブースティング エッセンス 150ml (発酵導入ブースター)"}
        ]
    }
}

def fetch_single(query_info):
    q = query_info["query"]
    queries_to_try = [q]
    parts = q.split()
    if len(parts) > 2:
        queries_to_try.append(" ".join(parts[:2]))
    if len(parts) > 3:
        queries_to_try.append(parts[0])

    for current_q in queries_to_try:
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(current_q)}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        
        for attempt in range(3):
            try:
                time.sleep(1.2)
                with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                    data = json.loads(res.read().decode('utf-8'))
                    items = data.get("Items", [])
                    if not items:
                        break
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and (item_obj.get("mediumImageUrls") or item_obj.get("smallImageUrls")):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]
                        
                    img_url = ""
                    if chosen.get("mediumImageUrls"):
                        img_url = chosen["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
                    elif chosen.get("smallImageUrls"):
                        img_url = chosen["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
                    
                    if not img_url:
                        continue
                        
                    price = chosen.get("itemPrice", 0)
                    aff_url = chosen.get("affiliateUrl", "") or chosen.get("itemUrl", "")
                    raw_title = chosen.get("itemName", query_info["name"])
                    
                    return {
                        "rank": query_info["rank"],
                        "name": query_info["name"],
                        "brand": query_info["brand"],
                        "price": price,
                        "raw_title": raw_title,
                        "affiliate_url": aff_url,
                        "img_url": img_url
                    }
            except Exception as e:
                print(f"Error fetching '{current_q}' (attempt {attempt+1}): {e}")
                time.sleep(2.0)
    return None

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching Rakuten items for {cat_key}: {cat_data['title']}")
    print(f"==========================================")
    cat_items = []
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['query']} ...")
        res = fetch_single(item_info)
        if res:
            print(f"  ✓ Found: {res['name'][:40]}... (¥{res['price']:,}) | Img: {res['img_url'][:50]}...")
            cat_items.append(res)
        else:
            print(f"  ❌ FAILED to fetch: {item_info['query']}")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

output_path = "fetched_3new_nov_dec_proteoglycan_propolis_galactomyces_data.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone! Saved all Rakuten data to {output_path}")
