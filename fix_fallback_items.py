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

with open("rakuten_3latest_articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 修正対象のクエリリスト
fixes = [
    {
        "cat": "winter_cleansing_balm",
        "rank": 3,
        "query": "ルルルン クレンジングバーム モイスト",
        "brand": "LuLuLun (ルルルン)",
        "name": "クレンジングバーム リッチモイスト (植物由来オイル高配合・冬の乾燥肌をうるおいで包み込む濃密バーム)"
    },
    {
        "cat": "winter_scalp_shampoo",
        "rank": 6,
        "query": "スカルプD ボーテ シャンプー 女性用",
        "brand": "スカルプD ボーテ (アンファー)",
        "name": "ナチュラスター スカルプシャンプー (天然由来成分90%以上・冬の寒暖差やストレスで硬くなった頭皮を優しくほぐす)"
    },
    {
        "cat": "winter_cica_cream",
        "rank": 5,
        "query": "バイオヒールボ パンテノール シカ クリーム",
        "brand": "BIOHEAL BOH (バイオヒールボ)",
        "name": "パントシカ バリアクリーム (高浸透パンテノール×CICA成分・冬の乱れた肌バリアを再構築してつるんとした健やか肌へ)"
    },
    {
        "cat": "winter_cica_cream",
        "rank": 8,
        "query": "ネイチャーリパブリック グリーンダーマ シカ クリーム",
        "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "name": "グリーンダーマ CICA デイリークリーム (プロポリスエキス×センテラ成分・冬の肌のカサつきと肌荒れを同時にうるおす大容量)"
    },
    {
        "cat": "winter_cica_cream",
        "rank": 10,
        "query": "スキンアンドラブ レッドエックス クリーム",
        "brand": "SKIN&LAB (スキンアンドラブ)",
        "name": "K プラス レッドエックス クリーム (ビタミンK×CICAエキス配合・冬の寒暖差で起こる頬の赤ら顔や毛細血管の目立ちを集中ケア)"
    }
]

for item in fixes:
    cat = item["cat"]
    rank = item["rank"]
    q = item["query"]
    print(f"Refetching for {cat} Rank {rank} with query: {q}...")
    success = False
    for attempt in range(5):
        try:
            time.sleep(2.0)
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                res_data = json.loads(res.read().decode('utf-8'))
                items = res_data.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
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
                    aff_url = chosen.get("affiliateUrl", "") or chosen.get("itemUrl", "")
                    item_name = chosen.get("itemName", "")
                    
                    if "sample" not in high_res_img and price > 0:
                        # update in data
                        target_list = data[cat]["items"]
                        for idx, existing in enumerate(target_list):
                            if existing["rank"] == rank:
                                target_list[idx] = {
                                    "rank": rank,
                                    "brand": item["brand"],
                                    "name": item["name"],
                                    "itemName": item_name,
                                    "price": price,
                                    "img": high_res_img,
                                    "url": aff_url
                                }
                                print(f"  ✓ Fixed: Rank {rank} {item['brand']} - ¥{price:,} - {high_res_img[:50]}")
                                success = True
                                break
                    if success:
                        break
        except Exception as e:
            print(f"  Attempt {attempt+1} error: {e}")
            time.sleep(2.5)
    if not success:
        print(f"  ❌ Failed to fix Rank {rank} in {cat}")

with open("rakuten_3latest_articles_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFix script completed.")
