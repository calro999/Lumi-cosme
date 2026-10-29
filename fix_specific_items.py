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

with open("rakuten_sleeping_nail_foot_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

FIX_ITEMS = [
    # category, rank, query, brand, display_name
    ("winter_sleeping_mask", 5, "イニスフリー グリーンティー プロバイオティクス スリーピングマスク", "innisfree (イニスフリー)", "グリーンティー スリーピングマスク (緑茶乳酸菌×濃密ジェル水分チャージ)"),
    ("winter_sleeping_mask", 10, "エリクシール ホワイト スリーピングクリアパック C", "ELIXIR (エリクシール)", "スリーピングクリアパック C 【医薬部外品】 (美白有効成分m-トラネキサム酸配合)"),
    ("winter_nail_oil", 10, "キャンメイク メイクミーハッピー ネイルオイル", "CANMAKE (キャンメイク)", "メイクミーハッピー ネイルオイル (植物オイル高配合・ロールオンプチプラ神オイル)"),
    ("winter_foot_cream", 1, "ニュートロジーナ フットクリーム 56g", "Neutrogena (ニュートロジーナ)", "ノルウェーフォーミュラ インテンスリペア フットクリーム (純度99%高濃度グリセリン)"),
    ("winter_foot_cream", 6, "メンソレータム ヒビプロ KTα 24g", "メンソレータム (ロート製薬)", "ヒビプロ KTα 【第3類医薬品】 (ひび割れ修復アラントイン・密着ワセリンベース)")
]

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

for cat, rank, raw_q, brand, disp_name in FIX_ITEMS:
    query = clean_query(raw_q)
    print(f"Fixing {cat} Rank {rank}: {query}...")
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                res_data = json.loads(res.read().decode('utf-8'))
                items = res_data.get("Items", [])
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
                    
                    # Update item in data
                    for i, it in enumerate(data[cat]["items"]):
                        if it["rank"] == rank:
                            data[cat]["items"][i] = {
                                "rank": rank,
                                "brand": brand,
                                "display_name": disp_name,
                                "item_name": raw_item.get("itemName", ""),
                                "price": raw_item.get("itemPrice", 0),
                                "affiliate_url": raw_item.get("affiliateUrl", ""),
                                "image_url": high_res_img,
                                "review_count": raw_item.get("reviewCount", 0),
                                "review_average": raw_item.get("reviewAverage", "4.5"),
                                "shop_name": raw_item.get("shopName", "")
                            }
                            print(f"-> Successfully updated Rank {rank}: {raw_item.get('itemName')[:35]} | ¥{raw_item.get('itemPrice')}")
                            break
                    break
                else:
                    words = query.split()
                    if len(words) > 1:
                        query = " ".join(words[:-1])
                        continue
        except Exception as e:
            print(f"Error: {e}, retry {attempt+1}")
            time.sleep(1)
    time.sleep(0.5)

with open("rakuten_sleeping_nail_foot_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nRefinements completed and saved to rakuten_sleeping_nail_foot_data.json!")
