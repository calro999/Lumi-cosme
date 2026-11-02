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
    "winter_shea_butter": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然の濃厚ベールで極上保護する高保湿シアバターランク10",
        "page_file": "winter-shea-butter.html",
        "items": [
            {"rank": 1, "query": "ロクシタン シアバター 150ml", "brand": "L'OCCITANE (ロクシタン)", "name": "ピュア シアバター 150ml (100%オーガニック植物性保湿バーム)"},
            {"rank": 2, "query": "ママバター フェイス＆ボディクリーム 25g", "brand": "MAMA BUTTER (ママバター)", "name": "フェイス＆ボディクリーム 25g (天然シアバター100%配合)"},
            {"rank": 3, "query": "生活の木 シアバター 精製 100g", "brand": "生活の木 (Tree of life)", "name": "シアバター 精製 100g (天然植物性エモリエントバター)"},
            {"rank": 4, "query": "spa hinoki オーガニック シアバター 75g", "brand": "spa hinoki (スパヒノキ)", "name": "オーガニック シアバター 75g (ECOCERT認証 未精製)"},
            {"rank": 5, "query": "ロクシタン シアバター 10ml", "brand": "L'OCCITANE (ロクシタン)", "name": "ピュア シアバター 10ml ミニサイズ (持ち運び用ポータブル)"},
            {"rank": 6, "query": "ナウフーズ シアバター 100% 207ml", "brand": "NOW Foods (ナウフーズ)", "name": "100% ピュア シアバター 207ml (大容量ナチュラル保湿バーム)"},
            {"rank": 7, "query": "サンホワイト P-1 50g", "brand": "日興リカ サンホワイト", "name": "サンホワイト P-1 50g (高品質白色ワセリン・シアバターと併用推奨バリア)"},
            {"rank": 8, "query": "クナイプ ビオ オイル バーム 50g", "brand": "Kneipp (クナイプ)", "name": "ビオ オイルバーム ローズ 50g (オーガニックシアバター配合)"},
            {"rank": 9, "query": "エチュード シアバター ハンドクリーム", "brand": "ETUDE (エチュード)", "name": "シアバター リッチモイスト ハンド＆マルチクリーム 50ml"},
            {"rank": 10, "query": "シアバター ボディクリーム 150g", "brand": "naturie / ボディケア", "name": "シアバター高配合 高保湿ボディクリーム 150g"}
        ]
    },
    "winter_jojoba_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！皮脂膜を補い真冬の肌を柔らかく包む高保湿ホホバオイルランク10",
        "page_file": "winter-jojoba-oil.html",
        "items": [
            {"rank": 1, "query": "無印良品 ホホバオイル 200ml", "brand": "無印良品 (MUJI)", "name": "ホホバオイル 200ml (天然植物由来100%ピュアオイル)"},
            {"rank": 2, "query": "インカオイル オーガニックホホバ ゴールド 120ml", "brand": "INCA OIL (インカオイル)", "name": "オーガニック ホホバオイル ゴールド 120ml (未精製一番搾り)"},
            {"rank": 3, "query": "spa hinoki オーガニック ホホバオイル 100ml", "brand": "spa hinoki (スパヒノキ)", "name": "オーガニック ホホバオイル 100ml (ECOCERT認証 ゴールド)"},
            {"rank": 4, "query": "マカダミ屋 ゴールデンホホバオイル 80ml", "brand": "マカダミ屋 (Macadamia-ya)", "name": "未精製 ゴールデンホホバオイル 80ml (天然無添加・低温圧搾)"},
            {"rank": 5, "query": "生活の木 ホホバオイル ゴールデン 100ml", "brand": "生活の木 (Tree of life)", "name": "ホホバオイル・ゴールデン 100ml (有機栽培 未精製ピュアオイル)"},
            {"rank": 6, "query": "無印良品 ホホバオイル 100ml", "brand": "無印良品 (MUJI)", "name": "ホホバオイル 100ml (持ち運びしやすい中容量ボトル)"},
            {"rank": 7, "query": "ナウフーズ ホホバオイル 118ml", "brand": "NOW Foods (ナウフーズ)", "name": "100% ピュア モイスチャライジング ホホバオイル 118ml"},
            {"rank": 8, "query": "自然化粧品研究所 精製ホホバオイル 100ml", "brand": "自然化粧品研究所", "name": "精製ホホバオイル 100ml (低刺激・サラサラ高浸透タイプ)"},
            {"rank": 9, "query": "KISO キソ ホホバオイル 50ml", "brand": "KISO (キソ)", "name": "オーガニック ゴールデン ホホバオイル 50ml (低温圧搾)"},
            {"rank": 10, "query": "ease aroma ホホバオイル 100ml", "brand": "ease aroma (イーズアロマ)", "name": "未精製 ホホバオイル 100ml (ゴールデン・キャリアオイル)"}
        ]
    },
    "winter_urea_cream": {
        "title": "保湿力の強さでガサガサ角質とさようなら！硬くなったかかと・ひじをしっとり柔らかく整える高保湿尿素クリームランク10",
        "page_file": "winter-urea-cream.html",
        "items": [
            {"rank": 1, "query": "ケラチナミンコーワ 20%尿素配合クリーム 150g", "brand": "興和新薬 (Kowa)", "name": "ケラチナミンコーワ 20%尿素配合クリーム 150g (第3類医薬品 / ガサガサ角質改善)"},
            {"rank": 2, "query": "フェルゼアプレミアム HPバーム 30g", "brand": "ライオン フェルゼア", "name": "フェルゼアプレミアム HPバーム 30g (第2類医薬品 / ヘパリン類似物質配合)"},
            {"rank": 3, "query": "資生堂 尿素10%クリーム 100g", "brand": "資生堂 (SHISEIDO)", "name": "尿素10%クリーム ジャー 100g (指定医薬部外品 / ヒアルロン酸・スクワラン配合)"},
            {"rank": 4, "query": "メンソレータム やわらか素肌クリームU 145g", "brand": "ロート製薬 メンソレータム", "name": "メンソレータム やわらか素肌クリームU 145g (第3類医薬品 / 尿素20%・ビタミンE)"},
            {"rank": 5, "query": "アトリックス 尿素10%配合 ハンドクリーム 60g", "brand": "atrix (アトリックス)", "name": "メディケイティッド 尿素10% ハンドクリーム 60g (医薬部外品)"},
            {"rank": 6, "query": "ザーネクリーム 100g エーザイ", "brand": "Eisai (エーザイ)", "name": "ザーネクリーム 100g (医薬部外品 / 天然ビタミンE＆消炎成分・角質柔軟)"},
            {"rank": 7, "query": "ロコベースリペア かかとケアバーム", "brand": "第一三共ヘルスケア", "name": "ロコベースリペア かかとケアバーム 20g (角質集中密着・セラミド3)"},
            {"rank": 8, "query": "資生堂 尿素10%クリーム チューブ 60g", "brand": "資生堂 (SHISEIDO)", "name": "尿素10%クリーム チューブ 60g (指定医薬部外品 / 持ち歩き用)"},
            {"rank": 9, "query": "メンソレータム 濃厚こってりクリーム 70g", "brand": "ロート製薬 メンソレータム", "name": "メンソレータム 薬用ハンドベール 濃厚こってりクリーム 70g (シアバター配合)"},
            {"rank": 10, "query": "ユースキン 120g ボトル", "brand": "yuskin (ユースキン)", "name": "ユースキン 120g ボトル (指定医薬部外品 / ビタミンB2・C配合 ひび・あかぎれ治療)"}
        ]
    }
}

def fetch_single(query_info):
    q = query_info["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if not items:
                    return None
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
                    "query": q,
                    "rakuten_name": chosen.get("itemName", ""),
                    "price": chosen.get("itemPrice", 0),
                    "image": img_url,
                    "affiliateUrl": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                    "reviewCount": chosen.get("reviewCount", 0),
                    "reviewAverage": chosen.get("reviewAverage", "0.0")
                }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 3.5 * (attempt + 1)
                print(f"    [Rate limit 429 hit] Waiting {wait_time}s before retry #{attempt+1}...")
                time.sleep(wait_time)
            else:
                print(f"    HTTP Error: {e.code}")
                time.sleep(2)
        except Exception as e:
            print(f"    Request error: {e}")
            time.sleep(2)
    return None

if __name__ == "__main__":
    results = {}
    for cat_key, cat_val in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching for category: {cat_key} ...")
        print(f"==========================================")
        cat_result = {
            "title": cat_val["title"],
            "page_file": cat_val["page_file"],
            "items": []
        }
        for q_info in cat_val["items"]:
            item_data = fetch_single(q_info)
            if not item_data:
                # alternative query
                alt_q = q_info["brand"].split()[0] + " " + q_info["name"].split()[0]
                print(f"  Fallback search with query: {alt_q}")
                time.sleep(2.0)
                item_data = fetch_single({"rank": q_info["rank"], "brand": q_info["brand"], "name": q_info["name"], "query": alt_q})
            
            if item_data:
                print(f"  ✓ Rank {q_info['rank']}: {item_data['name']} -> ¥{item_data['price']:,} (Review: {item_data['reviewAverage']} / {item_data['reviewCount']}件) [Image: {bool(item_data['image'])}]")
                cat_result["items"].append(item_data)
            else:
                print(f"  ❌ FAILED TO FETCH Rank {q_info['rank']}: {q_info['name']}")
            time.sleep(1.3)
        results[cat_key] = cat_result

    out_file = "fetched_3new_nov_dec_shea_jojoba_urea_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nAll done! Successfully saved data to {out_file}")
