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

def fetch_single(query, display_name, brand, rank):
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
            # 不適切な高額セットなどを除外
            if p > 0 and p < 20000 and imgs:
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
    return None

with open("fetched_3winter_nov_dec_final_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 修正対象アイテム
fixes = [
    # winter_gel_wash
    ("winter_gel_wash", 2, "ルナソル スムージングジェルウォッシュ 150g", "スムージングジェルウォッシュ 150g (ポリッシングクレンズ処方・泡立てないみずみずしい透明ジェルが毛穴汚れを包み込み陶器肌へ導く)", "LUNASOL (ルナソル / カネボウ)"),
    ("winter_gel_wash", 5, "オルビス ゼリーウォッシュ", "アクアニスト ゼリーウォッシュ 120g (敏感肌対応・クッション性のある厚みジェルが摩擦ダメージをゼロにして冬の乾燥ゆらぎ肌をしっとり洗浄)", "ORBIS (オルビス)"),
    ("winter_gel_wash", 6, "キュレル 泡洗顔料", "潤浸保湿 泡洗顔料 150ml (肌必須成分セラミドを守りながら洗う低刺激処方・冬のひりつき・カサつき肌を優しくケア)", "Curel (キュレル / 花王)"),
    
    # winter_lip_primer
    ("winter_lip_primer", 4, "コスメデコルテ リペア リップセラム", "リポソーム アドバンスト リペア リップセラム 7g (美肌カプセルが唇深くまで浸透・冬のガサガサ皮剥けをリペアし口紅の密着度を格上げ)", "DECORTÉ (コスメデコルテ)"),
    ("winter_lip_primer", 5, "ジルスチュアート リップグロウ セラムバーム 単品", "リップグロウ セラムバーム (清涼感ある心地よい刺激とうるおいヴェールで、ふっくらボリュームのあるツヤ唇を演出する名品下地)", "JILL STUART (ジルスチュアート)"),
    ("winter_lip_primer", 8, "オルビス リップベース", "リップベース 唇用下地 (ヒアルロン酸・植物性セラミド配合・マットリップの乾燥や皮剥けを防ぎ一日中うるおいをキープするリップ下地)", "ORBIS (オルビス)"),
    ("winter_lip_primer", 10, "メンソレータム リップフォンデュ 単品", "リップフォンデュ (まるでフォンデュのようにとろけて密着・オイル膜で唇をコートし口紅の縦ジワ落ちを完全ブロックする高保湿バーム)", "メンソレータム (ロート製薬)")
]

for cat, rank, q, disp, brand in fixes:
    print(f"Refining {cat} rank #{rank}: {q} ...")
    res = fetch_single(q, disp, brand, rank)
    if res:
        print(f"  ✓ Replaced with: {res['rakuten_name'][:40]} | ¥{res['price']} | Shop: {res['shop_name']}")
        # 既存リストのrank該当箇所を置換
        for i, item in enumerate(data[cat]["items"]):
            if item["rank"] == rank:
                data[cat]["items"][i] = res
                break
    else:
        print(f"  ❌ Failed for {q}")
    time.sleep(1)

with open("fetched_3winter_nov_dec_final_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Finished refining!")
