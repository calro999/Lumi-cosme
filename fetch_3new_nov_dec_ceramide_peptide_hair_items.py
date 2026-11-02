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
    "winter_ceramide_cream": {
        "title": "保湿力の強さで冬の肌荒れ・粉吹き乾燥とさようなら！角層バリアを高密度修復する高保湿セラミドクリームランク10",
        "page_file": "winter-ceramide-cream.html",
        "items": [
            {"rank": 1, "query": "キュレル 潤浸保湿フェイスクリーム 40g", "brand": "Curel (キュレル)", "name": "潤浸保湿フェイスクリーム 40g (医薬部外品)"},
            {"rank": 2, "query": "AESTURA アトバリア365 クリーム 80ml", "brand": "AESTURA (エストラ)", "name": "アトバリア365 クリーム 80ml"},
            {"rank": 3, "query": "松山油脂 肌をうるおす 保湿クリーム 50g", "brand": "松山油脂 (M mark)", "name": "肌をうるおす保湿スキンケア 保湿クリーム 50g"},
            {"rank": 4, "query": "リアルバリア エクストリーム クリーム 50ml", "brand": "Real Barrier (リアルバリア)", "name": "エクストリーム クリーム 50ml"},
            {"rank": 5, "query": "エトヴォス モイスチャライジングクリーム 30g", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングクリーム 30g"},
            {"rank": 6, "query": "ケアセラ AP フェイス＆ボディクリーム 70g", "brand": "ロート製薬 ケアセラ", "name": "ケアセラ AP高保湿フェイス＆ボディクリーム 70g"},
            {"rank": 7, "query": "シェルクルール ナチュレポウ デュオクリーム 30g", "brand": "シェルクルール (Cher-Couleur)", "name": "ナチュレポウ デュオクリーム 30g"},
            {"rank": 8, "query": "KISO ハイドロクリーム セラミド 50g", "brand": "KISO (キソ)", "name": "ハイドロクリーム セラミド 50g"},
            {"rank": 9, "query": "ラロッシュポゼ シカプラスト リペアクリーム B5+ 40ml", "brand": "LA ROCHE-POSAY (ラロッシュポゼ)", "name": "シカプラスト リペアクリーム B5+ 40ml"},
            {"rank": 10, "query": "セタフィル モイスチャライジングクリーム 566g", "brand": "Cetaphil (セタフィル)", "name": "モイスチャライジングクリーム 566g"}
        ]
    },
    "winter_peptide_serum": {
        "title": "保湿力の強さで冬の乾燥小ジワ・刻まれジワとさようなら！塗るボトックス発想でふっくら押し返す高保湿ペプチド美容液ランク10",
        "page_file": "winter-peptide-serum.html",
        "items": [
            {"rank": 1, "query": "The Ordinary マルチペプチド HA セラム 30ml", "brand": "The Ordinary (ジオーディナリー)", "name": "マルチペプチド + HA セラム 30ml (旧ビュッフェ)"},
            {"rank": 2, "query": "BIOHEAL BOH プロバイオダーム リフティング アンプル 30ml", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "プロバイオダーム コラーゲン リフティング アンプル 30ml"},
            {"rank": 3, "query": "メディキューブ トリプル コラーゲン セラム 55ml", "brand": "medicube (メディキューブ)", "name": "トリプル コラーゲン セラム 55ml"},
            {"rank": 4, "query": "VT リードルショット リフティング セラム 30ml", "brand": "VT COSMETICS (ブイトー)", "name": "リードルショット リフティング セラム 30ml"},
            {"rank": 5, "query": "魔女工場 ビフィダ バイオーム コンプレックス アンプル 50ml", "brand": "manyo (魔女工場)", "name": "ビフィダ バイオーム コンプレックス アンプル 50ml"},
            {"rank": 6, "query": "KISO ピュアエッセンス PE ペプチド 30ml", "brand": "KISO (キソ)", "name": "ピュアエッセンス PE ペプチド 原液 30ml"},
            {"rank": 7, "query": "Cos De BAHA ペプチド セラム 30ml", "brand": "Cos De BAHA (コスデバハ)", "name": "ペプチド フェイシャル セラム (P) 30ml"},
            {"rank": 8, "query": "Anua ドクダミ 77 スージング アンプル 30ml", "brand": "Anua (アヌア)", "name": "ドクダミ 77% スージング アンプル 30ml"},
            {"rank": 9, "query": "goodal 済州 青みかん ビタC アンプル 30ml", "brand": "goodal (グーダル)", "name": "グリーンタンジェリン ビタC ダークスポット ケア セラム 30ml"},
            {"rank": 10, "query": "ネイチャーリパブリック スネイル ソリューション エッセンス 40ml", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "スネイル ソリューション エッセンス 40ml"}
        ]
    },
    "winter_hair_serum": {
        "title": "保湿力の強さで冬の毛先パサつき・静電気爆発とさようなら！芯まで潤い満たす洗い流さない高保湿ヘアセラム・ヘアエッセンスランク10",
        "page_file": "winter-hair-serum.html",
        "items": [
            {"rank": 1, "query": "ラサーナ 海藻 ヘア エッセンス しっとり 120ml", "brand": "La Sana (ラサーナ)", "name": "海藻 ヘア エッセンス しっとり 120ml (洗い流さない髪の美容液)"},
            {"rank": 2, "query": "オルビス エッセンスインヘアミルク 140g", "brand": "ORBIS (オルビス)", "name": "エッセンスインヘアミルク 140g (浸透美容液成分配合)"},
            {"rank": 3, "query": "ケラスターゼ オレオ リラックス マジック ナイト セラム 90ml", "brand": "KERASTASE (ケラスターゼ)", "name": "オレオ リラックス マジック ナイト セラム 90ml (夜用くせ毛ケアヘアセラム)"},
            {"rank": 4, "query": "ミルボン エルジューダ ブリーチケア セラム 120ml", "brand": "MILBON (ミルボン)", "name": "エルジューダ ブリーチケア セラム 120ml"},
            {"rank": 5, "query": "ロレアル パリ エルセーヴ エクストラ リッチ フィニッシュ 100ml", "brand": "L'OREAL PARIS (ロレアル パリ)", "name": "エルセーヴ エクストラオーディナリー オイル エクストラリッチ フィニッシュ 100ml"},
            {"rank": 6, "query": "ルシードエル オイルトリートメント EX ヘアセラム 100ml", "brand": "LUCIDO-L (ルシードエル)", "name": "オイルトリートメント #EXヘアセラム 100ml"},
            {"rank": 7, "query": "moremo ウォーター トリートメント ミラクル 10 200ml", "brand": "moremo (モレモ)", "name": "ウォーター トリートメント ミラクル 10 200ml (高密着リペア)"},
            {"rank": 8, "query": "モロッカンオイル トリートメント 100ml", "brand": "MOROCCANOIL (モロッカンオイル)", "name": "モロッカンオイル トリートメント 100ml (アルガンオイル配合)"},
            {"rank": 9, "query": "アミノレスキュー ハイダメージ ヘアオイル セラム 100ml", "brand": "aminoRESQ (アミノレスキュー)", "name": "ハイダメージ ヘアパック トリートメント セラム 100ml"},
            {"rank": 10, "query": "スティーブンノル モイスチュアソフニング エマルジョン 100ml", "brand": "STEPHEN KNOLL (スティーブンノル)", "name": "モイスチュアソフニング エマルジョン N 100ml (髪の深層補修美容液)"}
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
                            if isinstance(images[0], dict):
                                img_url = images[0].get("imageUrl", "")
                            elif isinstance(images[0], str):
                                img_url = images[0]
                                
                        if not img_url:
                            small_images = chosen.get("smallImageUrls", [])
                            if small_images:
                                if isinstance(small_images[0], dict):
                                    img_url = small_images[0].get("imageUrl", "")
                                elif isinstance(small_images[0], str):
                                    img_url = small_images[0]
                        
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
                print(f"    Retry attempt {attempt+1} for {q_try}: {e}")
                time.sleep(1.2)
        time.sleep(0.5)
        
    print(f"  ❌ FAILED to find valid item for {raw_q}")
    return None

results = {}

print("==================================================================")
print("FETCHING 30 RAKUTEN ITEMS LIVE VIA OFFICIAL API (20260401 VERSION)")
print("==================================================================")

for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:35]}...)")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Rank {item_info['rank']}: {item_info['brand']} - {item_info['query']}")
        item_res = fetch_item_with_retry(item_info)
        if item_res:
            results[cat_key]["items"].append(item_res)
        else:
            print(f"FATAL: Missing product rank {item_info['rank']} in category {cat_key}")

with open("fetched_3new_nov_dec_ceramide_peptide_hair_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nFinished fetching all items. Results saved to fetched_3new_nov_dec_ceramide_peptide_hair_data.json")
