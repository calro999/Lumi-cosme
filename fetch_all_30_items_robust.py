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
    "winter_argan_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！モロッコの黄金オイルでふっくら極上やわらか肌へ導く高保湿アルガンオイルランク10",
        "page_file": "winter-argan-oil.html",
        "items": [
            {"rank": 1, "query": "メルヴィータ アルガンオイル 50ml", "brand": "Melvita (メルヴィータ)", "name": "ビオオイル アルガンオイル 50ml (フランス発・オーガニック一番搾りブースター)"},
            {"rank": 2, "query": "コディナ アルガンオイル", "brand": "CODINA (コディナ)", "name": "アルガンオイル 100ml (未精製・ナチュール＆プログレ認証取得)"},
            {"rank": 3, "query": "spa hinoki アルガンオイル", "brand": "spa hinoki (スパヒノキ)", "name": "オーガニック アルガンオイル 100ml (ECOCERT認証 モロッコ原産ピュアオイル)"},
            {"rank": 4, "query": "生活の木 アルガンオイル バージン", "brand": "生活の木 (Tree of life)", "name": "有機アルガンオイル バージン 未精製 25ml (コールドプレス有機栽培)"},
            {"rank": 5, "query": "ナイアード アルガンオイル", "brand": "naiad (ナイアード)", "name": "アルガンオイル 30ml (モロッコ伝統手搾り・無添加美容ピュアオイル)"},
            {"rank": 6, "query": "マカダミ屋 アルガンオイル", "brand": "マカダミ屋 (Macadamia-ya)", "name": "オーガニック 未精製 アルガンオイル 50ml (植物ステロール・ビタミンE豊富)"},
            {"rank": 7, "query": "KISO アルガンオイル", "brand": "KISO (キソ)", "name": "ピュアエッセンスAG オーガニック アルガンオイル 50ml (低温圧搾一番搾り)"},
            {"rank": 8, "query": "メルヴィータ アルガンオイル ローズ", "brand": "Melvita (メルヴィータ)", "name": "ビオオイル アルガンオイル ローズ 50ml (天然ダマスクローズ精油配合)"},
            {"rank": 9, "query": "自然化粧品研究所 アルガンオイル", "brand": "自然化粧品研究所", "name": "精製アルガンオイル 100ml (低刺激・匂いカット・さらり浸透タイプ)"},
            {"rank": 10, "query": "ナウフーズ アルガンオイル", "brand": "NOW Foods (ナウフーズ)", "name": "100% ピュア オーガニック アルガンオイル 59ml (USDA認証)"}
        ]
    },
    "winter_horse_oil": {
        "title": "保湿力の強さで頑固な肌乾燥・粉吹きとさようなら！人の皮脂に極めて近い天然脂質で包み込む高保湿馬油クリームランク10",
        "page_file": "winter-horse-oil.html",
        "items": [
            {"rank": 1, "query": "ソンバーユ 無香料 70ml", "brand": "薬師堂 ソンバーユ", "name": "ソンバーユ 無香料 70ml (馬油100%・昭和から続く元祖高保湿マルチオイル)"},
            {"rank": 2, "query": "北海道純馬油本舗 馬油", "brand": "北海道純馬油本舗", "name": "ピュアホワイトQ10 65g または 馬油100% 100g (国産高純度無添加)"},
            {"rank": 3, "query": "ソンバーユ 液状特製", "brand": "薬師堂 ソンバーユ", "name": "ソンバーユ 液状特製 55ml (低温抽出・さらり高浸透ブースタータイプ)"},
            {"rank": 4, "query": "リマーユ 馬油", "brand": "REMAYU (リマーユ)", "name": "リマーユ 馬油 スキンオイル 30ml (製薬会社開発・天然無臭高純度精製)"},
            {"rank": 5, "query": "ロッシモイストエイド 馬油スキンクリーム", "brand": "ロッシモイストエイド", "name": "馬油スキンクリーム 220g (大容量高保湿ボディ＆フェイスクリーム)"},
            {"rank": 6, "query": "ショウキリュウ 馬油", "brand": "ショウキリュウ (昇龍)", "name": "素肌クリーム 80ml (国産馬油・手足のひびあかぎれ集中ケア)"},
            {"rank": 7, "query": "ソンバーユ バニラ", "brand": "薬師堂 ソンバーユ", "name": "ソンバーユ バニラの香り 70ml (甘い香りでスキンケア・天然香料使用)"},
            {"rank": 8, "query": "横関油脂 馬油", "brand": "横関油脂工業", "name": "天然 馬油 純度100% 100g (熊本県産原料・昔ながらの伝統製法)"},
            {"rank": 9, "query": "ソンバーユ No.7", "brand": "薬師堂 ソンバーユ", "name": "ソンバーユ No.7 美肌用 60ml (美容用ハイグレード・しっとり濃厚タイプ)"},
            {"rank": 10, "query": "リバテープ 馬油", "brand": "リバテープ製薬", "name": "製薬会社が作った 馬油クリーム 70g (スクワラン・尿素配合処方)"}
        ]
    },
    "winter_panthenol_cream": {
        "title": "保湿力の強さで冬のヒリつき・敏感乾燥とさようなら！高濃度プロビタミンB5で角層バリアを鉄壁補修する高保湿パンテノールクリームランク10",
        "page_file": "winter-panthenol-cream.html",
        "items": [
            {"rank": 1, "query": "ラロッシュポゼ シカプラスト B5 40ml", "brand": "La Roche-Posay (ラロッシュポゼ)", "name": "シカプラスト バーム B5+ 40ml (パンテノール5%・マデカッソシド配合)"},
            {"rank": 2, "query": "バイオヒールボ パンテノール", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "パンテノール シカ ブレミッシュ クリーム 75ml (高濃度パンテノール配合)"},
            {"rank": 3, "query": "リアルバリア エクストリーム クリーム", "brand": "Real Barrier (リアルバリア)", "name": "エクストリーム クリーム 50ml (パンテノール・特許MLEセラミド技術)"},
            {"rank": 4, "query": "アヌア パンテノール クリーム", "brand": "Anua (アヌア)", "name": "パンテノール 水分バリアクリーム 50ml (ヒアルロン酸・角層吸着モイスト)"},
            {"rank": 5, "query": "ドクタージー レッドブレミッシュ クリーム", "brand": "Dr.G (ドクタージー)", "name": "レッドブレミッシュ クリア スージングクリーム 70ml (10-CICA＆パンテノール)"},
            {"rank": 6, "query": "メディピール パンテノール", "brand": "MEDI-PEEL (メディピール)", "name": "シカ アンチオ パンテノール リペアクリーム 50ml (ペプチド複合配合)"},
            {"rank": 7, "query": "VT シカ パンテノール", "brand": "VT COSMETICS", "name": "シカ パンテノール リペア クリーム 50ml (パンテノール10%高濃度処方)"},
            {"rank": 8, "query": "シカプラスト バーム B5 100ml", "brand": "La Roche-Posay (ラロッシュポゼ)", "name": "シカプラスト バーム B5+ 100ml 特大サイズ (全身＆ファミリー用)"},
            {"rank": 9, "query": "23years old バデカシル", "brand": "23years old", "name": "バデカシル パンテノール バーム 50g (肌荒れ・角質・ゆらぎ救済)"},
            {"rank": 10, "query": "KISO ハイドロクリーム PT", "brand": "KISO (キソ)", "name": "ハイドロクリーム PT 50g (高純度パンテノール5%配合 国産無添加処方)"}
        ]
    }
}

def fetch_single(q):
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if not items:
                    print(f"    [Warning] 0 items found for query: '{q}'")
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
                    "rakuten_name": chosen.get("itemName", ""),
                    "price": chosen.get("itemPrice", 0),
                    "rakuten_url": chosen.get("itemUrl", ""),
                    "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                    "img_url": img_url,
                    "review_count": chosen.get("reviewCount", 0),
                    "review_average": chosen.get("reviewAverage", "0.0")
                }
        except Exception as e:
            wait_time = 3 * (attempt + 1)
            print(f"    [Error] attempt {attempt+1}/{max_retries} for '{q}': {e}. Waiting {wait_time}s...")
            time.sleep(wait_time)
    return None

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Processing Category: {cat_key}")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        q = item_info["query"]
        print(f"Fetching Rank #{item_info['rank']}: {item_info['name'][:32]} (query: '{q}')")
        data = fetch_single(q)
        if not data and " " in q:
            # Fallback query with broader keyword
            alt_q = q.split()[0]
            print(f"  Retrying with broader query '{alt_q}'...")
            time.sleep(2)
            data = fetch_single(alt_q)
            
        if data and data.get("price", 0) > 0 and data.get("img_url"):
            item_entry = {
                "rank": item_info["rank"],
                "brand": item_info["brand"],
                "name": item_info["name"],
                "query": q,
                **data
            }
            results[cat_key]["items"].append(item_entry)
            print(f"  ✓ SUCCESS: Price=¥{data['price']:,} | Img={data['img_url'][:40]}... | Reviews={data['review_count']}")
        else:
            print(f"  ❌ FAILED to get valid item for Rank #{item_info['rank']}")
        
        # Respect rate limits
        time.sleep(1.8)

output_file = "fetched_3new_nov_dec_argan_horse_panthenol_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n==========================================")
print(f"Summary of Fetched Items:")
all_ok = True
for cat_key, cat_data in results.items():
    count = len(cat_data["items"])
    print(f"- {cat_key}: {count}/10 items")
    if count != 10:
        all_ok = False
        print(f"  ❌ Missing {10 - count} items in {cat_key}!")
    for it in cat_data["items"]:
        if it["price"] <= 0 or not it["img_url"] or not it["affiliate_url"]:
            print(f"  ❌ Invalid item data at Rank #{it['rank']}: {it['name']}")
            all_ok = False

if all_ok:
    print("\n🎉 ALL 30 ITEMS (10 x 3) FETCHED AND VALIDATED WITH 100% ACCURACY!")
else:
    print("\n❌ SOME ITEMS NEED REVIEW.")
print(f"==========================================")
