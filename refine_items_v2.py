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

def fetch_single(query, display_name, brand, rank, max_price=10000):
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=10&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                for it in items:
                    item_obj = it["Item"]
                    p = item_obj.get("itemPrice", 0)
                    name = item_obj.get("itemName", "")
                    imgs = item_obj.get("mediumImageUrls", [])
                    if p > 0 and p <= max_price and imgs:
                        raw_img = imgs[0].get("imageUrl", "")
                        high_res_img = raw_img
                        if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                            high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                        elif "?_ex=" in high_res_img:
                            high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                        
                        aff_url = item_obj.get("affiliateUrl", "") or item_obj.get("itemUrl", "")
                        return {
                            "rank": rank,
                            "brand": brand,
                            "display_name": display_name,
                            "rakuten_name": name,
                            "price": p,
                            "image_url": high_res_img,
                            "affiliate_url": aff_url,
                            "shop_name": item_obj.get("shopName", "")
                        }
        except Exception as e:
            print(f"  Attempt {attempt+1} failed for {query}: {e}")
            time.sleep(2.5)
            continue
        time.sleep(1.5)
    return None

with open("fetched_3winter_nov_dec_final_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 修正対象アイテム
fixes = [
    # winter_gel_wash
    ("winter_gel_wash", 2, "ルナソル ポリッシングクリア", "ポリッシングクリア ジェルウォッシュ 150g (独自のポリッシングクレンズ処方・泡立てないジェルが角栓を分解しうるおい陶器肌へ導く洗顔ジェル)", "LUNASOL (ルナソル / カネボウ)", 5000),
    ("winter_gel_wash", 5, "ビオレ おうちdeエステ なめらか", "おうちdeエステ 肌をなめらかにするマッサージ洗顔ジェル 150g (角栓クリア処方・ドラッグストアで大人気！泡立て不要で毛穴汚れを溶かし落とす)", "Biore (ビオレ / 花王)", 2000),
    ("winter_gel_wash", 6, "キュレル 泡洗顔料", "潤浸保湿 泡洗顔料 150ml (セラミドを守りながら洗う低刺激設計・冬の乾燥性敏感肌をふんわり包み込む薬用洗顔)", "Curel (キュレル / 花王)", 2500),
    
    # winter_lip_primer
    ("winter_lip_primer", 5, "ポール&ジョー リップスティック トリートメント", "リップスティック トリートメント (コラーゲン・オレンジハチミツ・ヒアルロン酸配合・唇をうるおいで満たし口紅の密着度を格上げする猫型リップベース)", "PAUL & JOE (ポール＆ジョー)", 4500),
    ("winter_lip_primer", 8, "エテュセ リップエディション", "リップエディション (プランパー ヘルシースタイル) (ジンジンほてリップ・冬の青白い唇に血色とボリュームを与え口紅のノリを最大化するリップ下地)", "ettusais (エテュセ)", 3500),
    ("winter_lip_primer", 10, "キャンメイク リップエッセンス", "プランプリップケアスクラブ (砂糖スクラブ配合・洗い流し不要で古い角質をケアしぷるぷるのうるおいリップ下地を作る名品)", "CANMAKE (キャンメイク)", 1500)
]

for cat, rank, q, disp, brand, max_p in fixes:
    print(f"Refining {cat} rank #{rank}: {q} ...")
    res = fetch_single(q, disp, brand, rank, max_p)
    if res:
        print(f"  ✓ Replaced with: {res['rakuten_name'][:40]} | ¥{res['price']} | Shop: {res['shop_name']}")
        for i, item in enumerate(data[cat]["items"]):
            if item["rank"] == rank:
                data[cat]["items"][i] = res
                break
    else:
        print(f"  ❌ Failed for {q}")
    time.sleep(2)

with open("fetched_3winter_nov_dec_final_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("\nFinished refining all 30 items!")
