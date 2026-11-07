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

with open("fetched_3new_nov_dec_pdrn_gluta_lip.json", "r", encoding="utf-8") as f:
    existing_data = json.load(f)

def clean_img(img_obj):
    if isinstance(img_obj, dict):
        url = img_obj.get("imageUrl", "")
    elif isinstance(img_obj, str):
        url = img_obj
    else:
        url = ""
    if "?_ex=" in url:
        url = url.split("?_ex=")[0] + "?_ex=400x400"
    return url

# 既存アイテムの画像URLをクリーンアップ
for cat in existing_data.values():
    for item in cat["items"]:
        item["image_url"] = clean_img(item["image_url"])

def fetch_one(queries):
    for q in queries:
        print(f"Trying query: '{q}' ...")
        encoded_q = urllib.parse.quote(q)
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        try:
            time.sleep(2.5)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                for it in items:
                    cand = it["Item"]
                    price = cand.get("itemPrice", 0)
                    imgs = cand.get("mediumImageUrls") or cand.get("smallImageUrls")
                    if price >= 300 and imgs:
                        img_url = clean_img(imgs[0])
                        return {
                            "item_name": cand["itemName"],
                            "price": cand["itemPrice"],
                            "affiliate_url": cand.get("affiliateUrl", cand.get("itemUrl")),
                            "image_url": img_url,
                            "review_count": cand.get("reviewCount", 0),
                            "review_average": str(cand.get("reviewAverage", "4.8"))
                        }
        except Exception as e:
            print(f"  Error: {e}")
            time.sleep(3.0)
    return None

# 1. PDRNクリームの欠落Rank 7を補充
pdrn_ranks = [it["rank"] for it in existing_data["winter_pdrn_cream"]["items"]]
if 7 not in pdrn_ranks:
    print("\n--- Fetching missing PDRN Rank 7 ---")
    res = fetch_one(["クレアス PDRN ビタグルバリアクリーム", "クレアス PDRN クリーム", "klairs PDRN"])
    if res:
        res["rank"] = 7
        res["brand"] = "Dear,Klairs (クレアス)"
        res["display_name"] = "PDRN ビタグルバリアクリーム 60g (ツボクサPDRN×純度99%ピュアビタミンC・寒冷刺激で萎縮した角層を健やかに目覚めさせふっくら弾むハリ肌へ導く濃密バリアクリーム)"
        existing_data["winter_pdrn_cream"]["items"].append(res)
        print("✓ PDRN Rank 7 fetched successfully!")

# 2. グルタチオンクリームの欠落Rankを補充
gluta_ranks = [it["rank"] for it in existing_data["winter_glutathione_cream"]["items"]]

if 4 not in gluta_ranks:
    print("\n--- Fetching missing Gluta Rank 4 ---")
    res = fetch_one(["アビブ グルタチオンソーム", "Abib グルタチオン", "アビブ グルタチオン クリーム"])
    if res:
        res["rank"] = 4
        res["brand"] = "Abib (アビブ)"
        res["display_name"] = "グルタチオンソーム スキンブースタークリーム 50mL (リポソーム化高純度グルタチオン×植物性スクワラン配合・真冬の冷風でくすんだ肌に澄み渡る白玉のような透明感を与える濃密クリーム)"
        existing_data["winter_glutathione_cream"]["items"].append(res)
        print("✓ Gluta Rank 4 fetched successfully!")

if 5 not in gluta_ranks:
    print("\n--- Fetching missing Gluta Rank 5 ---")
    res = fetch_one(["APLB グルタチオン ナイアシンアミド フェイシャルクリーム", "APLB グルタチオン クリーム", "APLB グルタチオン"])
    if res:
        res["rank"] = 5
        res["brand"] = "APLB (エーピーエルビー)"
        res["display_name"] = "グルタチオン ナイアシンアミド フェイシャルクリーム 55mL (高純度グルタチオン×ナイアシンアミド配合・角質層の隅々まで潤いを巡らせ冬の乾燥くすみを一掃する高保湿フェイスクリーム)"
        existing_data["winter_glutathione_cream"]["items"].append(res)
        print("✓ Gluta Rank 5 fetched successfully!")

if 8 not in gluta_ranks:
    print("\n--- Fetching missing Gluta Rank 8 ---")
    res = fetch_one(["ネイチャーリパブリック ビタペアC 7日 ホワイトニング クリーム 50ml", "ビタペアC クリーム 50ml", "ネイチャーリパブリック ビタペアC クリーム"])
    if res:
        res["rank"] = 8
        res["brand"] = "NATURE REPUBLIC (ネイチャーリパブリック)"
        res["display_name"] = "ビタペアC ダークスポット クリーム 50mL (チェジュ島無農薬グリーンレモンエキス×ナイアシンアミド×グルタチオン・冬の乾燥で硬化した角層を柔らかくほぐし潤いで満たす高保湿ビタミンジェルクリーム)"
        existing_data["winter_glutathione_cream"]["items"].append(res)
        print("✓ Gluta Rank 8 fetched successfully!")

if 9 not in gluta_ranks:
    print("\n--- Fetching missing Gluta Rank 9 ---")
    res = fetch_one(["ドクタージー ビタミン クリーム 50ml", "Dr.G ビタミン トーニング クリーム", "ドクタージー ロイヤルブラックスネイル クリーム 50ml"])
    if res:
        res["rank"] = 9
        res["brand"] = "Dr.G (ドクタージー)"
        res["display_name"] = "ロイヤルブラックスネイル クリーム 50mL (ブラックスネイル粘液×グルタチオン×ローヤルゼリーエキス・真冬の過酷な寒冷乾燥から肌を徹底保護し極上の弾力と艶をもたらすリフティングクリーム)"
        existing_data["winter_glutathione_cream"]["items"].append(res)
        print("✓ Gluta Rank 9 fetched successfully!")

# 3. セラミドリップの欠落Rank 7を補充
lip_ranks = [it["rank"] for it in existing_data["winter_ceramide_lip"]["items"]]
if 7 not in lip_ranks:
    print("\n--- Fetching missing Lip Rank 7 ---")
    res = fetch_one(["ニベア ディープモイスチャー リップ 無香料", "ニベア ディープモイスチャーリップ", "ニベア ディープモイスチャー 無香料"])
    if res:
        res["rank"] = 7
        res["brand"] = "NIVEA (花王 ニベア)"
        res["display_name"] = "ディープモイスチャーリップ 無香料 2.2g (5つの保湿成分：はちみつ・アミノ酸系保水成分・セラミド類似成分・オリーブ油配合・唇の体温でとろけて高密着ヴェールが持続する冬の鉄板高保湿リップ)"
        existing_data["winter_ceramide_lip"]["items"].append(res)
        print("✓ Lip Rank 7 fetched successfully!")

# 各カテゴリのランク順ソート
for cat_key in existing_data:
    existing_data[cat_key]["items"].sort(key=lambda x: x["rank"])
    print(f"\nFinal count for {cat_key}: {len(existing_data[cat_key]['items'])} items")

with open("fetched_3new_nov_dec_pdrn_gluta_lip.json", "w", encoding="utf-8") as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

print("\nSuccessfully updated fetched_3new_nov_dec_pdrn_gluta_lip.json!")
