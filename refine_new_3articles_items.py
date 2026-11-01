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

with open("fetched_3nov_dec_needle_salt_gloss_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_single(query, rank, brand, display_name):
    time.sleep(1.5)
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        if not items:
            return None
        
        chosen = None
        for it in items:
            item_obj = it["Item"]
            if item_obj.get("itemPrice", 0) >= 1000 and item_obj.get("mediumImageUrls"):
                chosen = item_obj
                break
        if not chosen:
            chosen = items[0]["Item"]
        
        raw_img = ""
        if chosen.get("mediumImageUrls"):
            raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "")
        
        high_res_img = raw_img
        if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
            high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
        elif "?_ex=" in high_res_img:
            high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
        
        price = chosen.get("itemPrice", 0)
        aff_url = chosen.get("affiliateUrl", "")
        if not aff_url:
            aff_url = chosen.get("itemUrl", "")
        
        return {
            "rank": rank,
            "brand": brand,
            "display_name": display_name,
            "rakuten_name": chosen.get("itemName", display_name),
            "price": price,
            "image_url": high_res_img,
            "affiliate_url": aff_url,
            "shop_name": chosen.get("shopName", "")
        }

# 1. winter_needle_patch Rank 10: ハーリス モイスト パッチ (Harithoth / 薬用マイクロニードル) または スノーヴァ
print("Refetching winter_needle_patch Rank 10...")
# 「ハーリス モイスト パッチ」または「マイクロニードル パッチ ヒアルロン酸」で検索
item10 = fetch_single("ハーリス モイスト パッチ", 10, "Harith (ハーリス)", "モイスト パッチ 2枚×2袋 (極小マイクロニードル×高濃度プロテオグリカン＆ヒアルロン酸！真冬の目元・眉間・ほうれい線に密着注入)")
if not item10 or item10["price"] == 0:
    item10 = fetch_single("マイクロニードル パッチ ヒアルロン酸 目元", 10, "Nature Republic (ネイチャーリパブリック)", "ヒアルロン酸 マイクロニードルパッチ (角層まで届く針状美容液！目元の乾燥小ジワをふっくら集中ケア)")

if item10:
    print(f"  ✓ Fetched needle patch Rank 10: {item10['display_name'][:30]} | Price: ¥{item10['price']:,}")
    # 既存リストに挿入または更新
    existing = [it for it in data["winter_needle_patch"]["items"] if it["rank"] != 10]
    existing.append(item10)
    existing.sort(key=lambda x: x["rank"])
    data["winter_needle_patch"]["items"] = existing

# 2. winter_bath_salt Rank 10: クナイプ バスソルト ボトル (サンダルウッド 850g)
print("Refetching winter_bath_salt Rank 10...")
item_bath10 = fetch_single("クナイプ バスソルト サンダルウッド 850g", 10, "Kneipp (クナイプ)", "バスソルト サンダルウッドの香り 850g ボトル (深みのあるオリエンタルウッディの温感アロマ×天然岩塩・冬の乾燥肌をなめらかに包み込む大人の名品)")
if item_bath10 and item_bath10["price"] >= 1000:
    print(f"  ✓ Refetched bath salt Rank 10: {item_bath10['display_name'][:30]} | Price: ¥{item_bath10['price']:,}")
    for idx, it in enumerate(data["winter_bath_salt"]["items"]):
        if it["rank"] == 10:
            data["winter_bath_salt"]["items"][idx] = item_bath10
            break

with open("fetched_3nov_dec_needle_salt_gloss_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nVerifying all 3 categories now:")
for cat_key, c_data in data.items():
    print(f"Category {cat_key}: {len(c_data['items'])} items")
    for it in c_data["items"]:
        print(f"  Rank #{it['rank']}: ¥{it['price']:,} | Img: {it['image_url'][:40]}... | URL: {it['affiliate_url'][:40]}...")
