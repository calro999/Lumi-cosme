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

def update_item(cat, rank, brand, display_name, query, min_price=300, max_price=50000):
    print(f"Refining [{cat}] Rank {rank}: '{query}' ...")
    res = fetch_rakuten_item(query, min_price, max_price)
    if res:
        for idx, it in enumerate(data[cat]["items"]):
            if it["rank"] == rank:
                data[cat]["items"][idx] = {
                    "rank": rank,
                    "query": query,
                    "brand": brand,
                    "display_name": display_name,
                    "rakuten_item_name": res["name"],
                    "price": res["price"],
                    "image_url": res["image_url"],
                    "affiliate_url": res["affiliate_url"],
                    "shop_name": res["shop_name"]
                }
                print(f"  ✓ Updated Rank {rank}: {res['name'][:35]} | ¥{res['price']:,} | {res['shop_name']}")
                return True
    print(f"  ❌ Failed for Rank {rank}")
    return False

# 1. winter_inbath_body
# Rank 2: ビオレu ぬれた肌に使うボディ乳液
update_item("winter_inbath_body", 2, "Biore u (ビオレu / 花王)", 
            "ザ ボディ お風呂場で使う ぬれた肌用乳液 無香料 300ml (吊り下げてノズルを押すだけ！お風呂上がりの急激な乾燥を防ぐ弱酸性高保湿ミルク)",
            "ビオレu ぬれた肌に使うボディ乳液 無香料", 500, 3000)

# Rank 6: ニベア スキンミルク しっとり 200g (単品)
update_item("winter_inbath_body", 6, "NIVEA (ニベア / 花王)", 
            "スキンミルク しっとり 200g (ディープ＆ロングラスティングモイスチャー処方！冬の粉吹き肌も一日中もっちり吸い付く高保湿王道ミルク)",
            "ニベア スキンミルク しっとり 200g", 400, 2000)

# Rank 8: セタフィル モイスチャライジング ローション (単品)
update_item("winter_inbath_body", 8, "Cetaphil (セタフィル)", 
            "モイスチャライジングローション 591ml (ナイアシンアミド×パンテノール配合！大容量で濡れた肌にもスーッと伸びてバリア修復)",
            "セタフィル モイスチャライジングローション 591ml", 1500, 3500)

# 2. winter_hot_eyemask
# Rank 1: めぐりズム 蒸気でホットアイマスク 無香料 (12枚入 単品)
update_item("winter_hot_eyemask", 1, "めぐりズム (花王)", 
            "蒸気でホットアイマスク 無香料 12枚入 (約40℃の心地よい温熱蒸気が約20分持続！冬の冷えた目元をじっくり奥からほぐす世界的金字塔)",
            "めぐりズム 蒸気でホットアイマスク 無香料 12枚", 800, 2500)

# Rank 4: めぐりズム 蒸気でホットアイマスク 完熟ゆず (12枚入 単品)
update_item("winter_hot_eyemask", 4, "めぐりズム (花王)", 
            "蒸気でホットアイマスク 完熟ゆずの香り 12枚入 (冬にぴったりのもぎたて完熟ゆずアロマ！温かい蒸気で緊張をほぐし目元を潤す)",
            "めぐりズム 蒸気でホットアイマスク 完熟ゆず 12枚", 800, 2500)

# Rank 5: MYTREX EYE HEAT
update_item("winter_hot_eyemask", 5, "MYTREX (マイトレックス)", 
            "EYE HEAT PRO 3D温熱アイマスク (目元を圧迫しない立体3D構造！遠赤外線グラフェンヒーターで均一に温めるサロン級ホットアイマスク)",
            "MYTREX ホットアイマスク", 1500, 6000)

# 3. winter_hand_mask
# Rank 1: EBiS うるおいハンドマスク (エビス化粧品)
update_item("winter_hand_mask", 1, "EBiS (エビス化粧品)", 
            "うるおいハンドマスク 36枚入 (美容液350ml・EGFやヒアルロン酸など115種類の美容成分を凝縮！手袋型でスマホ操作もできる集中補修マスク)",
            "エビス うるおいハンドマスク", 1000, 4000)

# Rank 3: ハンドマスク 手袋 パック
update_item("winter_hand_mask", 3, "Ducato (デュカート / シャンティ)", 
            "エッセンスハンドマスク 1回分 (ホホバオイル・コラーゲン配合！指先やかかとまでしっとり整えるネイルケア発想の濃密ハンドマスク)",
            "ハンドマスク 手袋 美容液", 400, 3000)

# Rank 7: Dr.Jart+ セラマイディン ハンドクリーム / マスク
update_item("winter_hand_mask", 7, "Dr.Jart+ (ドクタージャルト)", 
            "セラマイディン ハンドウォームマスク (5種類の高浸透セラミド配合！温熱効果で冷えた指先を温めながらバリア機能を強力リペア)",
            "Dr.Jart セラマイディン ハンド", 1000, 3500)

# Rank 8: メディヒール ハンドマスク または ハンドケア パック
update_item("winter_hand_mask", 8, "MEDIHEAL (メディヒール)", 
            "ハンドリペアマスク 1回分 (シートマスクの世界的権威メディヒール！パラフィン成分が手肌を密封コーティングし絹のような手触りに)",
            "ハンドケア 手袋 パック", 500, 3000)

# Rank 10: ジャパンギャルズ ハンドマスク
update_item("winter_hand_mask", 10, "JAPAN GALS (ジャパンギャルズ)", 
            "エッセンスハンドマスク 2枚入 (濃密プラセンタ＆コラーゲン配合！冬のエイジングサインが気になる手の甲をふっくら若々しく)",
            "ハンドマスク 手袋 プラセンタ", 500, 3000)

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nRefinement complete! Verifying current data:")
for cat_key, c_data in data.items():
    print(f"\nCategory {cat_key}:")
    for it in c_data["items"]:
        print(f"  Rank #{it['rank']}: ¥{it['price']:,} | {it['rakuten_item_name'][:35]} | Img: {it['image_url'][:35]}...")
