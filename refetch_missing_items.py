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

with open("rakuten_scalp_bath_wipe_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 補完対象のアイテムリスト
missing_targets = [
    {
        "cat": "winter_scalp_scrub",
        "rank": 2,
        "query": "ロクシタン ピュアフレッシュネス スカルプ",
        "brand": "L'OCCITANE (ロクシタン)",
        "name": "ファイブハーブス ピュアフレッシュネス スカルプスクラブ 150ml (シーソルト×5つのハーブエッセンシャルオイル・冬の頭皮環境を健やかに整え根元から立ち上がる美髪へ)"
    },
    {
        "cat": "winter_scalp_scrub",
        "rank": 6,
        "query": "アヴェダ プラマサナ スカルプ",
        "brand": "AVEDA (アヴェダ)",
        "name": "プラマサナ エクスフォリエーティング スカルプ トリートメント 75ml (海藻エキス×ラクトバチルス発酵液配合・冬の角層バリアを保ちながら不要な角質を穏やかに除去)"
    },
    {
        "cat": "winter_scalp_scrub",
        "rank": 8,
        "query": "フローラノーティス エッセンシャル スカルプ",
        "brand": "Flora Notis JILL STUART (フローラノーティス)",
        "name": "エッセンシャルスカルプスクラブ 180g (シュガースクラブ×厳選フラワーオイル配合・ジャスミンの芳醇な香りに包まれながらしっとり潤い頭皮へ導く)"
    },
    {
        "cat": "winter_scalp_scrub",
        "rank": 9,
        "query": "ボディショップ スカルプ スクラブ",
        "brand": "THE BODY SHOP (ザ・ボディショップ)",
        "name": "ティーツリー ピューリファイング スカルプスクラブ 240ml (ケニア産フェアトレードティーツリーオイル×ソルトスクラブ・冬のニット帽蒸れによるベタつきとフケをリフレッシュ)"
    },
    {
        "cat": "winter_medicinal_bath",
        "rank": 10,
        "query": "バスクリン 日本の名湯 アソート",
        "brand": "バスクリン (日本の名湯)",
        "name": "日本の名湯 至福の贅沢 30g×14包 [医薬部外品] (温泉科学プロジェクトから生まれた本格薬用入浴剤・冬の冷えた体を名湯の湯ざわりと保湿成分で芯から癒やす)"
    },
    {
        "cat": "winter_wipe_lotion",
        "rank": 4,
        "query": "イプサ クリアアップ ローション",
        "brand": "IPSA (イプサ)",
        "name": "クリアアップ ローション 2 150ml (乾燥肌用・グレープシードオイル配合の2層式ふき取りローション・冬の硬くなった角層を柔らかく解きほぐしうるおい導入)"
    }
]

def fetch_single(target):
    query = target["query"]
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                res_data = json.loads(res.read().decode('utf-8'))
                items = res_data.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls") and "ふるさと納税" not in item_obj.get("itemName", ""):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]

                    raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "") if chosen.get("mediumImageUrls") else ""
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"

                    aff_url = chosen.get("affiliateUrl", "")
                    if not aff_url:
                        raw_item_url = chosen.get("itemUrl", "")
                        aff_url = f"https://hb.afl.rakuten.co.jp/hgc/{AFF_ID}/?pc={urllib.parse.quote(raw_item_url)}"

                    price = chosen.get("itemPrice", 0)
                    print(f"  [SUCCESS] {target['cat']} rank {target['rank']} | {target['brand']} | ¥{price:,} | {chosen.get('itemName', '')[:40]}")
                    return {
                        "rank": target["rank"],
                        "brand": target["brand"],
                        "name": target["name"],
                        "raw_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url
                    }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 3.0 * (attempt + 1)
                print(f"  [429 Rate limited] waiting {wait_time}s on '{query}'...")
                time.sleep(wait_time)
            else:
                print(f"  [HTTPError {e.code}] on '{query}'")
                time.sleep(2)
        except Exception as e:
            print(f"  [ERROR] {e} on '{query}'")
            time.sleep(2)
    return None

for target in missing_targets:
    cat = target["cat"]
    rank = target["rank"]
    print(f"\nFetching missing item for {cat} rank {rank}: '{target['query']}'...")
    res = fetch_single(target)
    if res:
        # 既存リスト内を探すか、追加するか
        existing_items = data[cat]["items"]
        found_idx = -1
        for i, it in enumerate(existing_items):
            if it["rank"] == rank:
                found_idx = i
                break
        if found_idx >= 0:
            existing_items[found_idx] = res
        else:
            existing_items.append(res)
    else:
        print(f"❌ FAILED to fetch for rank {rank}")
    time.sleep(2.0)

# 各カテゴリをrank順にソート
for cat in data:
    data[cat]["items"] = sorted(data[cat]["items"], key=lambda x: x["rank"])
    print(f"{cat}: {len(data[cat]['items'])}/10 items present")

with open("rakuten_scalp_bath_wipe_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nDone updating rakuten_scalp_bath_wipe_data.json!")
