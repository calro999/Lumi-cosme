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
    "category_1": {
        "title": "高保湿フェイスクリーム＆濃密バーム",
        "items": [
            {"rank": 1, "query": "キールズ クリーム UFC 50ml", "brand": "Kiehl's (キールズ)", "name": "キールズ クリーム UFC"},
            {"rank": 2, "query": "コスメデコルテ リポソーム アドバンスト リペアクリーム", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム アドバンスト リペアクリーム"},
            {"rank": 3, "query": "キュレル 潤浸保湿フェイスクリーム 40g", "brand": "Curel (キュレル)", "name": "潤浸保湿フェイスクリーム 【医薬部外品】"},
            {"rank": 4, "query": "カルテHD モイスチュア クリーム 40g", "brand": "Carte (カルテHD)", "name": "モイスチュア クリーム 【医薬部外品】"},
            {"rank": 5, "query": "ラロッシュポゼ シカプラスト B5", "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)", "name": "シカプラスト リペアクリーム B5+"},
            {"rank": 6, "query": "アベンヌ シカルファットプラス 40g", "brand": "Avene (アベンヌ)", "name": "シカルファットプラス リペアクリーム"},
            {"rank": 7, "query": "エリクシール トータルV ファーミングクリーム", "brand": "ELIXIR (エリクシール)", "name": "トータルV ファーミングクリーム"},
            {"rank": 8, "query": "エトヴォス モイスチャライジングクリーム", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングクリーム"},
            {"rank": 9, "query": "ミノン アミノモイスト モイストチャージ クリーム", "brand": "MINON (ミノン)", "name": "アミノモイスト モイストチャージ クリーム"},
            {"rank": 10, "query": "イハダ 薬用バーム 20g", "brand": "IHADA (イハダ)", "name": "薬用バーム 【医薬部外品】"}
        ]
    },
    "category_2": {
        "title": "高保湿ファンデーション＆美容液下地",
        "items": [
            {"rank": 1, "query": "クレドポーボーテ ヴォワールコレクチュールn", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "ヴォワールコレクチュールn"},
            {"rank": 2, "query": "資生堂 エッセンス スキングロウ ファンデーション", "brand": "SHISEIDO (資生堂)", "name": "エッセンス スキングロウ ファンデーション"},
            {"rank": 3, "query": "ポールアンドジョー モイスチュアライジング プライマー", "brand": "PAUL & JOE (ポール＆ジョー)", "name": "モイスチュアライジング ファンデーション プライマー"},
            {"rank": 4, "query": "カネボウ クリーム イン デイ 40g", "brand": "KANEBO (カネボウ)", "name": "クリーム イン デイ (日中用クリーム・化粧下地)"},
            {"rank": 5, "query": "コスメデコルテ ルースパウダー 00", "brand": "DECORTÉ (コスメデコルテ)", "name": "ルースパウダー (シルキータッチ)"},
            {"rank": 6, "query": "ディオールスキン フォーエヴァー スキン コレクト コンシーラー", "brand": "Dior (ディオール)", "name": "ディオールスキン フォーエヴァー スキン コレクト コンシーラー"},
            {"rank": 7, "query": "スック リクイド ファンデーション", "brand": "SUQQU (スック)", "name": "ザ リクイド ファンデーション"},
            {"rank": 8, "query": "アンドビー UVプライマー", "brand": "&be (アンドビー)", "name": "UVプライマー SPF50+ PA++++"},
            {"rank": 9, "query": "アディクション スキンケア ファンデーション", "brand": "ADDICTION (アディクション)", "name": "ザ スキンケア ファンデーション"},
            {"rank": 10, "query": "エクセル スキンスムージング クッションファンデーション", "brand": "excel (エクセル)", "name": "スキンスムージング クッションファンデーション"}
        ]
    },
    "category_3": {
        "title": "高保湿リップケア＆うるツヤ濃密ティント",
        "items": [
            {"rank": 1, "query": "ラネージュ リップスリーピングマスク", "brand": "LANEIGE (ラネージュ)", "name": "リップスリーピングマスク (ベリー)"},
            {"rank": 2, "query": "ディオール アディクト リップ マキシマイザー", "brand": "Dior (ディオール)", "name": "ディオール アディクト リップ マキシマイザー"},
            {"rank": 3, "query": "タカミ リップ 7g", "brand": "TAKAMI (タカミ)", "name": "タカミリップ (唇用美容液)"},
            {"rank": 4, "query": "キュレル リップケアバーム", "brand": "Curel (キュレル)", "name": "リップケアバーム 【医薬部外品】"},
            {"rank": 5, "query": "クラランス リップコンフォートオイル", "brand": "CLARINS (クラランス)", "name": "リップコンフォートオイル"},
            {"rank": 6, "query": "オバジ ダーマパワーX リップエッセンス", "brand": "Obagi (オバジ)", "name": "ダーマパワーX リップエッセンス"},
            {"rank": 7, "query": "ロムアンド ジューシーラスティングティント", "brand": "rom&nd (ロムアンド)", "name": "ジューシーラスティングティント"},
            {"rank": 8, "query": "ジョンマスターオーガニック リップカーム", "brand": "john masters organics (ジョンマスター)", "name": "リップカーム (オリジナルシトラス)"},
            {"rank": 9, "query": "エテュセ リップエディション", "brand": "ettusais (エテュセ)", "name": "リップエディション (プランパー ヘルシースタイル)"},
            {"rank": 10, "query": "メンソレータム メルティクリームリップ 無香料", "brand": "メンソレータム (ロート製薬)", "name": "メルティクリームリップ (無香料)"}
        ]
    }
}

def fetch_single_item(query_info):
    query = query_info["query"]
    for attempt in range(4):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    raw_item = items[0]["Item"]
                    raw_img = ""
                    if raw_item.get("mediumImageUrls"):
                        raw_img = raw_item["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "display_name": query_info["name"],
                        "item_name": raw_item.get("itemName", ""),
                        "price": raw_item.get("itemPrice", 0),
                        "affiliate_url": raw_item.get("affiliateUrl", ""),
                        "image_url": high_res_img,
                        "shop_name": raw_item.get("shopName", ""),
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", 0)
                    }
                else:
                    print(f"No item found for query '{query}'")
                    return None
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[429 Rate Limit] Waiting 2s for '{query}' (attempt {attempt+1})...")
                time.sleep(2.0)
            else:
                print(f"HTTP {e.code} for '{query}': {e}")
                break
        except Exception as e:
            print(f"Error on '{query}': {e}")
            break
        time.sleep(1.2)
    return None

all_data = {}
for cat_key, cat_val in CATEGORIES.items():
    print(f"\n=== Fetching {cat_val['title']} ({cat_key}) ===")
    cat_items = []
    for q in cat_val["items"]:
        item = fetch_single_item(q)
        if item:
            print(f"  ✓ [{item['rank']}] {item['display_name']} - {item['price']}円")
            cat_items.append(item)
        else:
            print(f"  ✗ Failed for {q['query']}")
        time.sleep(1.2)
    all_data[cat_key] = cat_items

with open("rakuten_items_data.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("\nFinal Results Summary:")
for cat_key, items in all_data.items():
    print(f"  {cat_key}: {len(items)} items fetched")
