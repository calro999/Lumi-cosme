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

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_rakuten_item(query, min_price=300, max_price=50000):
    time.sleep(1.2)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&minPrice={min_price}&maxPrice={max_price}&hits=10&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
            res_data = json.loads(res.read().decode('utf-8'))
            items = res_data.get("Items", [])
            for it in items:
                chosen = it["Item"]
                p = chosen.get("itemPrice", 0)
                img = ""
                if chosen.get("mediumImageUrls"):
                    img = chosen["mediumImageUrls"][0].get("imageUrl", "")
                if p >= min_price and img:
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in img:
                        img = img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in img:
                        img = img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    aff = chosen.get("affiliateUrl", "")
                    if not aff:
                        aff = chosen.get("itemUrl", "")
                    return {
                        "name": chosen.get("itemName", ""),
                        "price": p,
                        "image_url": img,
                        "affiliate_url": aff,
                        "shop_name": chosen.get("shopName", "")
                    }
    except Exception as e:
        print(f"Error fetching '{query}': {e}")
    return None

# 1. winter_hot_eyemask Rank 5: めぐりズム 森林浴 12枚
res5 = fetch_rakuten_item("めぐりズム 蒸気でホットアイマスク 森林浴 12枚", 800, 3000)
if res5:
    data["winter_hot_eyemask"]["items"][4] = {
        "rank": 5,
        "query": "めぐりズム 蒸気でホットアイマスク 森林浴 12枚",
        "brand": "めぐりズム (花王)",
        "display_name": "蒸気でホットアイマスク 森林浴の香り 12枚入 (みずみずしい森林浴アロマ×約40℃スチーム！奥深い樹木の香りで目元の緊張を芯から解き放つ)",
        "rakuten_item_name": res5["name"],
        "price": res5["price"],
        "image_url": res5["image_url"],
        "affiliate_url": res5["affiliate_url"],
        "shop_name": res5["shop_name"]
    }
    print(f"✓ Hot Eyemask Rank 5 updated: {res5['name'][:30]}")

# 2. winter_hand_mask Rank 1: エビス 美容液 ハンドマスク
res_hm1 = fetch_rakuten_item("エビス うるおい ハンドマスク", 1000, 5000)
if not res_hm1:
    res_hm1 = fetch_rakuten_item("ハンドマスク 美容液 手袋 大容量", 1000, 5000)
if res_hm1:
    data["winter_hand_mask"]["items"][0] = {
        "rank": 1,
        "query": "ハンドマスク 美容液 手袋",
        "brand": "EBiS (エビス化粧品)",
        "display_name": "うるおいハンドマスク 大容量36枚入 (EGF・プラセンタ・ヒアルロン酸等贅沢配合！手袋型でスマホも触れるサロン発想の集中ハンドケア)",
        "rakuten_item_name": res_hm1["name"],
        "price": res_hm1["price"],
        "image_url": res_hm1["image_url"],
        "affiliate_url": res_hm1["affiliate_url"],
        "shop_name": res_hm1["shop_name"]
    }
    print(f"✓ Hand Mask Rank 1 updated: {res_hm1['name'][:30]}")

# 3. winter_hand_mask Rank 8: 韓国コスメ パラフィン ハンドマスク
res_hm8 = fetch_rakuten_item("ハンドマスク パラフィン パック 手袋", 500, 3000)
if not res_hm8:
    res_hm8 = fetch_rakuten_item("ハンドパック 手袋 シアバター", 500, 3000)
if res_hm8:
    data["winter_hand_mask"]["items"][7] = {
        "rank": 8,
        "query": "ハンドパック 手袋 シアバター",
        "brand": "MEDIHEAL (メディヒール / コスメプラザ)",
        "display_name": "シアバター＆パラフィン 集中ハンドトリートメントマスク (濃厚シアバターと温感パラフィン成分でカサつく指先を包み込みシルク肌へ)",
        "rakuten_item_name": res_hm8["name"],
        "price": res_hm8["price"],
        "image_url": res_hm8["image_url"],
        "affiliate_url": res_hm8["affiliate_url"],
        "shop_name": res_hm8["shop_name"]
    }
    print(f"✓ Hand Mask Rank 8 updated: {res_hm8['name'][:30]}")

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFinal items verification:")
for cat_key, c_data in data.items():
    print(f"\nCategory: {cat_key}")
    for it in c_data["items"]:
        print(f"  #{it['rank']}: ¥{it['price']:,} | {it['brand']} | {it['rakuten_item_name'][:30]}... | Img: {it['image_url'][:35]}...")
