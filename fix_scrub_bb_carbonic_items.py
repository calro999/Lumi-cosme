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

with open("rakuten_scrub_bb_carbonic_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

fixes = [
    {
        "cat": "winter_lip_scrub",
        "rank": 7,
        "query": "CHOOSY リップスクラブ",
        "brand": "CHOOSY (チューシー)",
        "name": "リップスクラブ パウチ / ポット (天然シュガースクラブ×シアバター配合・唇の古い角質を優しく除去しふっくら保湿する専用スクラブ)"
    },
    {
        "cat": "winter_lip_scrub",
        "rank": 8,
        "query": "バーツビーズ リップスクラブ",
        "brand": "BURT'S BEES (バーツビーズ)",
        "name": "コンディショニング リップスクラブ (ハニー クリスタル×ミツロウ配合・100%天然由来成分で冬のガサガサ皮剥けをなめらかに整える)"
    },
    {
        "cat": "winter_carbonic_pack",
        "rank": 10,
        "query": "オバジX フレームリフトムースウォッシュ",
        "brand": "Obagi (オバジ)",
        "name": "オバジX フレームリフトムースウォッシュ (高密度炭酸マイクロ泡・毛穴より小さな炭酸泡で血行促進しながらハリと透明感を与える濃密泡パック洗顔)"
    }
]

def fetch_one(fix_info):
    time.sleep(1.5)
    query = fix_info["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        d = json.loads(res.read().decode('utf-8'))
        items = d.get("Items", [])
        if items:
            chosen = items[0]["Item"]
            raw_img = chosen.get("mediumImageUrls", [{}])[0].get("imageUrl", "")
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in raw_img:
                high_res_img = raw_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in raw_img:
                high_res_img = raw_img.split("?_ex=")[0] + "?_ex=600x600"
            else:
                high_res_img = raw_img

            price = chosen.get("itemPrice", 0)
            return {
                "rank": fix_info["rank"],
                "brand": fix_info["brand"],
                "name": fix_info["name"],
                "query": fix_info["query"],
                "rakuten_name": chosen.get("itemName", ""),
                "price": price,
                "price_str": f"¥{price:,}" if price > 0 else "価格表示なし",
                "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                "image_url": high_res_img,
                "review_count": chosen.get("reviewCount", 0),
                "review_average": chosen.get("reviewAverage", "4.5")
            }
    raise Exception(f"Failed to fetch {query}")

for fix in fixes:
    cat = fix["cat"]
    rank = fix["rank"]
    print(f"Fixing {cat} Rank {rank}: {fix['query']} ...")
    res = fetch_one(fix)
    # 既存配列内の対象インデックスを差し替え
    items = data[cat]["items"]
    for i, it in enumerate(items):
        if it["rank"] == rank:
            items[i] = res
            print(f"  Successfully updated: {res['rakuten_name'][:40]} | {res['price_str']}")
            break

with open("rakuten_scrub_bb_carbonic_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated all fixed items!")
