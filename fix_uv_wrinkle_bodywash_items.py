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

with open("rakuten_uv_wrinkle_bodywash_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 修正クエリ定義
FIXES = [
    # wrinkle #5: DEW リンクルスマッシュ (医薬部外品・ナイアシンアミド配合・カネボウのシワ改善美容液)
    {
        "cat": "winter_wrinkle_cream",
        "rank": 5,
        "query": "DEW リンクルスマッシュ",
        "brand": "DEW (カネボウ)",
        "name": "リンクルスマッシュ (医薬部外品・有効成分ナイアシンアミド配合・ヒアルロン酸研究から生まれた目元・口元用シワ改善美容液)"
    },
    # bodywash #3: キュレル 泡ボディウォッシュ 本体 (通常価格品)
    {
        "cat": "winter_body_wash",
        "rank": 3,
        "query": "キュレル 泡ボディウォッシュ 本体",
        "brand": "Curel (キュレル)",
        "name": "泡ボディウォッシュ (医薬部外品・肌の必須成分セラミドを守りながら汚れをすっきり落とす消炎剤配合のマイルド泡)"
    },
    # bodywash #9: ヴェレダ スキンフード ボディウォッシュ / シトラス クリーミーボディウォッシュ
    {
        "cat": "winter_body_wash",
        "rank": 9,
        "query": "ヴェレダ クリーミー ボディウォッシュ",
        "brand": "WELEDA (ヴェレダ)",
        "name": "クリーミー ボディウォッシュ (100%天然由来・ゴマ油＆アーモンド油配合・お肌をしっとり洗い上げる贅沢な植物オイルミルクソープ)"
    },
    # bodywash #10: ハダカラ 泡ボディソープ 本体 (通常価格品)
    {
        "cat": "winter_body_wash",
        "rank": 10,
        "query": "ハダカラ 泡ボディソープ 本体",
        "brand": "hadakara (ハダカラ)",
        "name": "泡ボディソープ (吸着保湿テクノロジー・洗うたびに保湿成分が肌に吸着して洗い流されない高保湿泡ソープ)"
    }
]

def fetch_single(item_info):
    query = item_info["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=10&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        for it in items:
            item_obj = it["Item"]
            price = item_obj.get("itemPrice", 0)
            img_urls = item_obj.get("mediumImageUrls", [])
            # 10,000円以上の異常値（セット品やふるさと納税）を除外
            if 0 < price < 9000 and img_urls:
                raw_img = img_urls[0].get("imageUrl", "")
                high_res_img = raw_img
                if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                    high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                elif "?_ex=" in high_res_img:
                    high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                
                return {
                    "rank": item_info["rank"],
                    "brand": item_info["brand"],
                    "name": item_info["name"],
                    "query_used": query,
                    "rakuten_item_name": item_obj.get("itemName", ""),
                    "price": price,
                    "price_str": f"¥{price:,}",
                    "image_url": high_res_img,
                    "affiliate_url": item_obj.get("affiliateUrl", item_obj.get("itemUrl", "")),
                    "review_count": item_obj.get("reviewCount", 0),
                    "review_average": item_obj.get("reviewAverage", "0.0")
                }
    return None

print("=== Fixing specific items ===")
for fix in FIXES:
    time.sleep(1)
    res = fetch_single(fix)
    if res:
        cat_items = data[fix["cat"]]["items"]
        for idx, it in enumerate(cat_items):
            if it["rank"] == fix["rank"]:
                cat_items[idx] = res
                print(f"✓ Fixed {fix['cat']} #{fix['rank']}: {res['rakuten_item_name'][:30]} | {res['price_str']}")
                break
    else:
        print(f"❌ Failed to fix {fix['cat']} #{fix['rank']}")

# 全アイテムの画像URLを検証・整形
for cat, val in data.items():
    for it in val["items"]:
        img = it["image_url"]
        if "thumbnail.image.rakuten.co.jp/@0_mall/" in img:
            it["image_url"] = img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
        elif "thumbnail.image.rakuten.co.jp/@0_gold/" in img:
            # goldもshop.r10s.jpで直接アクセス可能な場合が多いが、画像表示を確認
            pass
        elif "?_ex=" in img:
            it["image_url"] = img.split("?_ex=")[0] + "?_ex=600x600"

with open("rakuten_uv_wrinkle_bodywash_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated rakuten_uv_wrinkle_bodywash_data.json!")
