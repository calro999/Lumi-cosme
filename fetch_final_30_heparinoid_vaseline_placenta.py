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
    "winter_heparinoid": {
        "title": "保湿力の強さで肌乾燥とさようなら！角層深部の保水構造を立て直す薬用ヘパリン類似物質コスメランク10",
        "page_file": "winter-heparinoid.html",
        "items": [
            {"rank": 1, "query": "コーセー カルテHD モイスチュア ローション 150ml", "brand": "Carte (カルテHD / コーセーマルホ)", "name": "モイスチュア ローション 150ml (医薬部外品・ヘパリン類似物質HD高保湿化粧水)"},
            {"rank": 2, "query": "カルテHD モイスチュア エマルジョン 120ml", "brand": "Carte (カルテHD / コーセーマルホ)", "name": "モイスチュア エマルジョン 120ml (医薬部外品・ヘパリン類似物質HD高保湿乳液)"},
            {"rank": 3, "query": "コーセー カルテHD モイスチュア クリーム 40g", "brand": "Carte (カルテHD / コーセーマルホ)", "name": "モイスチュア クリーム 40g (医薬部外品・濃密うるおいバリア保護クリーム)"},
            {"rank": 4, "query": "大正製薬 アドライズ アクティブローション", "brand": "AdryS (大正製薬 アドライズ)", "name": "アクティブローション ディープモイスト 120ml (医薬部外品・薬用保湿＆美白化粧水)"},
            {"rank": 5, "query": "ヒルメナイド 油性クリーム", "brand": "matsukiyo (マツキヨ)", "name": "ヒルメナイド油性クリーム 80g (第2類医薬品・ヘパリン類似物質0.3%配合濃厚クリーム)"},
            {"rank": 6, "query": "ロート製薬 ヘパソフト 薬用 顔ローション 100g", "brand": "ロート製薬 (ヘパソフト)", "name": "ヘパソフト 薬用 顔ローション 100g (医薬部外品・ワセリンベースヘパリン保水乳液)"},
            {"rank": 7, "query": "ヒルドプレミアム ミルクローション 100ml", "brand": "StayFree (ステイフリー)", "name": "ヒルドプレミアム ミルクローション 100ml (医薬部外品・ヘパリン類似物質＆GK2配合薬用保湿乳液)"},
            {"rank": 8, "query": "ヒルドプレミアム 薬用オールインワンゲル 100g", "brand": "StayFree (ステイフリー)", "name": "ヒルドプレミアム オールインワンゲル 100g (医薬部外品・ヘパリン類似物質高配合時短ゲル)"},
            {"rank": 9, "query": "ピアソンHPローション 50g", "brand": "日医工 (ピアソンHP)", "name": "ピアソンHP ローション 50g (第2類医薬品・ヘパリン類似物質0.3%配合ローション)"},
            {"rank": 10, "query": "カルテHD モイスチュア バーム 15g", "brand": "Carte (カルテHD / コーセーマルホ)", "name": "モイスチュア バーム 15g (医薬部外品・ヘパリン類似物質部分用高密着バーム)"}
        ]
    },
    "winter_vaseline": {
        "title": "保湿力の強さで肌乾燥とさようなら！水分蒸発をゼロに抑えて冬の冷風から守り抜く高純度ワセリンランク10",
        "page_file": "winter-vaseline.html",
        "items": [
            {"rank": 1, "query": "サンホワイト P-1 50g 日興リカ", "brand": "日興リカ (SUNWHITE)", "name": "サンホワイト P-1 50g (最高純度・高品質白色ワセリン・無添加)"},
            {"rank": 2, "query": "プロペト ピュアベールa 30g", "brand": "第一三共ヘルスケア (プロペト)", "name": "プロペト ピュアベールa 30g (第3類医薬品・目元や口元にも安心のピュアワセリン)"},
            {"rank": 3, "query": "健栄製薬 ベビーワセリン 100g", "brand": "健栄製薬 (KENEI)", "name": "ベビーワセリン 100g (無香料・無着色・パラベンフリー低刺激ワセリン)"},
            {"rank": 4, "query": "ヴァセリン オリジナル ピュアスキンジェリー 80g", "brand": "Vaseline (ユニリーバ)", "name": "オリジナル ピュアスキンジェリー 80g (ピュアワセリン100%・世界基準の万能保護)"},
            {"rank": 5, "query": "IHADA イハダ 薬用バーム 20g", "brand": "IHADA (資生堂イハダ)", "name": "薬用バーム 20g (医薬部外品・高精製ワセリン配合とろける薬用密封バーム)"},
            {"rank": 6, "query": "サンホワイト シルキー Y-1 80g", "brand": "日興リカ (SUNWHITE)", "name": "サンホワイト シルキー Y-1 80g (ベタつかない伸びの良いエアリー高純度ワセリン)"},
            {"rank": 7, "query": "健栄製薬 ベビーワセリンリップ 10g", "brand": "健栄製薬 (KENEI)", "name": "ベビーワセリンリップ 10g (唇の皮むけ・ひび割れ集中保護チューブ)"},
            {"rank": 8, "query": "大洋製薬 ワセリンHG チューブ", "brand": "大洋製薬 (TAIYO)", "name": "ワセリンHG チューブ 60g (刺激が少なく伸びが良い高純度白色ワセリン)"},
            {"rank": 9, "query": "健栄製薬 白色ワセリン 50g", "brand": "健栄製薬 (KENEI)", "name": "日本薬局方 白色ワセリン 50g (第3類医薬品・皮膚の保護や荒れ予防の定番)"},
            {"rank": 10, "query": "ヴァセリン アドバンスドリペア ボディローション 400ml", "brand": "Vaseline (ユニリーバ)", "name": "アドバンスドリペア ボディーローション 400ml (極小ワセリンジェリー配合高保湿乳液)"}
        ]
    },
    "winter_placenta": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の代謝低下とハリ不足を跳ね返す高濃度プラセンタ原液ランク10",
        "page_file": "winter-placenta.html",
        "items": [
            {"rank": 1, "query": "フラコラ プラセンタ原液 30ml", "brand": "fracora (フラコラ)", "name": "ディープ プラセンタエキス原液 30ml (高濃度・高浸透ピュアプラセンタ100%)"},
            {"rank": 2, "query": "ビービーラボラトリーズ 水溶性プラセンタエキス原液 30ml", "brand": "Bb LABORATORIES (ビービーラボ)", "name": "水溶性プラセンタエキス原液 30ml (国内契約農場豚プラセンタ100%抽出の最高峰)"},
            {"rank": 3, "query": "チューンメーカーズ プラセンタエキス 20ml", "brand": "TUNEMAKERS (チューンメーカーズ)", "name": "プラセンタエキス 20ml (高純度原液美容液・くすみ＆乾燥集中ケア)"},
            {"rank": 4, "query": "KISO キソ プラセンタ 原液 20ml", "brand": "KISO (基礎化粧品研究所)", "name": "プラセンタエッセンス PC 20ml (国産馬プラセンタ高濃度原液エキス)"},
            {"rank": 5, "query": "エビス 美容液 エクセレントバイオ EX100 33ml", "brand": "EBiS (エビス化粧品)", "name": "エクセレントバイオ EX100 33ml (植物性プラセンタ100%原液・キメと弾力アップ)"},
            {"rank": 6, "query": "ホワイトラベル プラセンタ もっちり白肌エッセンス 20g", "brand": "WHITE LABEL (ミックコスモ)", "name": "贅沢プラセンタのもっちり白肌エッセンス 20g (国産100%プラセンタ高配合美容液)"},
            {"rank": 7, "query": "十勝プラセンタ研究所 トカプラエッセンスEX", "brand": "十勝プラセンタ研究所", "name": "トカプラエッセンスEX 30ml (北海道十勝産原料100%・非加熱生プラセンタ高濃度美容液)"},
            {"rank": 8, "query": "リアル プラセンタエキス 原液 30ml", "brand": "REAL (リアル)", "name": "プラセンタエッセンス原液 30ml (国産豚プラセンタ・透明感と潤い補給)"},
            {"rank": 9, "query": "プラセンタ 原液 100 美容液", "brand": "自然化粧品研究所", "name": "ピュアプラセンタ原液 100ml (大容量高濃度プラセンタ・全身エイジングケア)"},
            {"rank": 10, "query": "馬プラセンタ 原液 美容液", "brand": "KISO CARE", "name": "キソ 馬プラセンタ原液エキス 20ml (アミノ酸豊富な北海道産サラブレッド抽出液)"}
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
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "query": current_q,
                        "rakuten_name": chosen.get("itemName", ""),
                        "price": chosen.get("itemPrice", 0),
                        "rakuten_url": chosen.get("itemUrl", ""),
                        "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                        "img_url": img_url
                    }
            except Exception as e:
                print(f"Error fetching '{current_q}': {e}, retrying...")
                time.sleep(2.0)
    return None

results = {}
all_success = True
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Fetching Rank #{item_info['rank']}: {item_info['name'][:30]} (query: {item_info['query']})")
        res = fetch_single(item_info)
        if res and res.get("price", 0) > 0 and res.get("img_url"):
            print(f"  -> SUCCESS: Price=¥{res['price']:,}, Image={res['img_url'][:45]}...")
            results[cat_key]["items"].append(res)
        else:
            print(f"  -> FAILED to fetch item!")
            all_success = False

output_file = "fetched_3new_nov_dec_heparinoid_vaseline_placenta_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nSaved all results to {output_file}!")
if all_success:
    print("🎉 ALL 30 ITEMS FETCHED WITH 100% SUCCESS!")
else:
    print("❌ WARNING: Some items failed to fetch!")
