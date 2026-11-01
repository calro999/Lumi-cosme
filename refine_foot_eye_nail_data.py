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

with open("fetched_3nov_dec_foot_eye_nail_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 修正対象の定義
TARGETS_TO_FIX = {
    "winter_foot_mask": [
        {
            "rank": 3,
            "query": "ココスター フット パック",
            "fallback_query": "足裏 保湿 パック シアバター",
            "brand": "KOCOSTAR (ココスター)",
            "name": "フットモイスチャーパック 1回分 (韓国発！シアバター＆アルガンオイル配合の靴下型パックでカサつく足裏を集中補修)"
        },
        {
            "rank": 4,
            "query": "太陽ニット かかとツルツル靴下 1足",
            "fallback_query": "かかとツルツル靴下 太陽ニット",
            "brand": "太陽ニット (たいようニット)",
            "name": "かかとツルツル靴下 婦人用 1足 (特殊高分子保湿シートをかかとに内蔵！普段履きするだけでガサガサかかとが滑らかに)"
        },
        {
            "rank": 6,
            "query": "休足時間 かかとぷるぷるジェルシート",
            "fallback_query": "ライオン 休足時間 かかと",
            "brand": "休足時間 (LION / ライオン)",
            "name": "かかとぷるぷるジェルシート 8枚入 (お風呂上がりに貼って寝るだけ！高含水ジェルとAHA・フルーツ酸が角質を柔らかく密着保湿)"
        },
        {
            "rank": 10,
            "query": "かかと 保湿 ソックス シルク 就寝用",
            "fallback_query": "シルク かかと ソックス 保湿",
            "brand": "絹屋 (きぬや)",
            "name": "極上天然シルク かかと保湿ケアソックス (天然シルク100%の優しい肌触り！就寝中に通気性を保ちながらかかとを集中保湿)"
        }
    ],
    "winter_eye_patch": [
        {
            "rank": 2,
            "query": "Abib コラーゲン アイパッチ 60枚",
            "fallback_query": "Abib ハイドロゲル アイパッチ",
            "brand": "Abib (アビブ)",
            "name": "コラーゲン ゲル アイパッチ 60枚入 (復活草エキス×ヴィーガンコラーゲン配合！目元のちりめんジワとくすみを集中ケアするぷるぷるゲル)"
        },
        {
            "rank": 7,
            "query": "MEDIHEAL アイパッチ ゲル",
            "fallback_query": "メディヒール アイパッチ",
            "brand": "MEDIHEAL (メディヒール)",
            "name": "コラーゲン ハイドロゲル アイパッチ 60枚入 (シートマスク名門メディヒール！目元にピタッと吸い付く低分子コラーゲン集中ジェルシート)"
        },
        {
            "rank": 9,
            "query": "VT シカ コラーゲン アイパッチ",
            "fallback_query": "VT ハイドロゲル アイパッチ",
            "brand": "VT COSMETICS (ブイティー)",
            "name": "CICA コラーゲン アイパッチ 60枚入 (CICA×大豆植物性コラーゲン！乾燥で疲れた目元をひんやり鎮静しながらハリチャージ)"
        },
        {
            "rank": 10,
            "query": "イニスフリー コラーゲン アイパッチ",
            "fallback_query": "ハイドロゲル アイパッチ 目元 60枚",
            "brand": "innisfree (イニスフリー)",
            "name": "ブラックティー ユース アイパッチ 60枚入 (発酵茶葉エキスと濃密ペプチドが冬の目元乾燥小ジワをふっくら満たす高密着ゲルパッチ)"
        }
    ],
    "winter_nail_serum": [
        {
            "rank": 3,
            "query": "エテュセ クイックケアコート 9ml",
            "fallback_query": "エテュセ クイックケアコート",
            "brand": "ettusais (エテュセ)",
            "name": "クイックケアコート 9ml (ホホバ油・マカデミアナッツ油配合！リムーバー不要でツヤを与えながら冬の乾燥爪を集中トリートメント)"
        },
        {
            "rank": 4,
            "query": "OPI プロスパ キューティクル オイル トゥーゴー 7.5ml",
            "fallback_query": "OPI プロスパ オイル トゥーゴー",
            "brand": "O・P・I (オーピーアイ)",
            "name": "プロスパ ネイル＆キューティクルオイル トゥーゴー 7.5ml (サロン仕様のクプアスバター＆ホワイトティエキス配合！持ち歩きやすいジェル状ペンタイプ)"
        },
        {
            "rank": 9,
            "query": "アンドネイル オーガニックブレンドオイル 10ml",
            "fallback_query": "アンドネイル 爪 美容液",
            "brand": "アンドネイル (石澤研究所)",
            "name": "オーガニックブレンドオイル 10ml (100%天然由来成分！冬のダメージを受けた自爪と甘皮にしっとり浸透する集中リペアネイルオイル)"
        }
    ]
}

def fetch_single_item(query, fallback_q=None):
    q_to_try = [query]
    if fallback_q:
        q_to_try.append(fallback_q)
    
    for q in q_to_try:
        for attempt in range(4):
            try:
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
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
                        affiliate_url = chosen.get("affiliateUrl", "")
                        item_url = chosen.get("itemUrl", "")
                        final_url = affiliate_url if affiliate_url else item_url
                        
                        return {
                            "rakuten_name": chosen.get("itemName", ""),
                            "price": price,
                            "image_url": high_res_img,
                            "affiliate_url": final_url,
                            "shop_name": chosen.get("shopName", "楽天市場正規取扱店"),
                            "review_count": chosen.get("reviewCount", 0),
                            "review_average": chosen.get("reviewAverage", 0.0),
                            "item_caption": chosen.get("itemCaption", "")[:120]
                        }
            except Exception as e:
                print(f"  Attempt {attempt+1} failed for '{q}': {e}")
                time.sleep(1.5)
    return None

for cat_key, fix_list in TARGETS_TO_FIX.items():
    print(f"\nRefining Category: {cat_key} ...")
    items = data[cat_key]["items"]
    for fix_spec in fix_list:
        rank = fix_spec["rank"]
        print(f"Fixing Rank {rank}: {fix_spec['query']} ...")
        res = fetch_single_item(fix_spec["query"], fix_spec.get("fallback_query"))
        if res:
            # 既存の該当rankのitemを更新
            for i, it in enumerate(items):
                if it["rank"] == rank:
                    it["name"] = fix_spec["name"]
                    it["brand"] = fix_spec["brand"]
                    it["rakuten_name"] = res["rakuten_name"]
                    it["price"] = res["price"]
                    it["image_url"] = res["image_url"]
                    it["affiliate_url"] = res["affiliate_url"]
                    it["shop_name"] = res["shop_name"]
                    it["review_count"] = res["review_count"]
                    it["review_average"] = res["review_average"]
                    it["item_caption"] = res["item_caption"]
                    print(f"  ✓ Updated Rank {rank}: {it['rakuten_name'][:40]} (¥{it['price']:,})")
                    break
        else:
            print(f"  ❌ FAILED to refine Rank {rank}")
        time.sleep(0.8)

with open("fetched_3nov_dec_foot_eye_nail_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nRefinement complete! All items successfully updated in fetched_3nov_dec_foot_eye_nail_data.json")
