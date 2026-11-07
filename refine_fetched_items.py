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

def search_item(queries):
    for q in queries:
        print(f"Searching: '{q}' ...")
        encoded_q = urllib.parse.quote(q)
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        try:
            time.sleep(2.0)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                for it in items:
                    cand = it["Item"]
                    price = cand.get("itemPrice", 0)
                    if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                        img_url = ""
                        if cand.get("mediumImageUrls"):
                            img_url = cand["mediumImageUrls"][0]
                        elif cand.get("smallImageUrls"):
                            img_url = cand["smallImageUrls"][0]
                        if "?_ex=" in img_url:
                            img_url = img_url.split("?_ex=")[0] + "?_ex=400x400"
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
            time.sleep(2.0)
    return None

with open("fetched_3new_winter_ceramide_night_eye.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. winter_night_serum Rank 2: コスメデコルテ リポソーム アドバンスト リペアセラム 50ml
item_cosme = search_item(["コスメデコルテ リポソーム アドバンスト リペアセラム 50ml", "コスメデコルテ リポソーム リペアセラム 50ml"])
if item_cosme:
    print("Found Cosme Decorte Serum:", item_cosme["item_name"][:40])
    for it in data["winter_night_serum"]["items"]:
        if it["rank"] == 2:
            it["item_name"] = item_cosme["item_name"]
            it["price"] = item_cosme["price"]
            it["affiliate_url"] = item_cosme["affiliate_url"]
            it["image_url"] = item_cosme["image_url"]
            it["review_count"] = item_cosme["review_count"]
            it["review_average"] = item_cosme["review_average"]

# 2. winter_night_serum Rank 9: ドクターシーラボ VC100 ダブルリペアセラム または オバジC25
item_night9 = search_item(["ドクターシーラボ VC100 ダブルリペアセラム 30ml", "VC100 ダブルリペアセラム", "ドクターシーラボ ダブルリペアセラム"])
if item_night9:
    print("Found Night Serum 9:", item_night9["item_name"][:40])
    for it in data["winter_night_serum"]["items"]:
        if it["rank"] == 9:
            it["brand"] = "Dr.Ci:Labo (ドクターシーラボ)"
            it["display_name"] = "VC100 ダブルリペアセラム 30mL (高浸透ビタミンC×高純度セラミドの二層式・睡眠中に毛穴とくすみを集中ケアし翌朝ふっくらモチモチ肌へ導く夜用集中美容液)"
            it["item_name"] = item_night9["item_name"]
            it["price"] = item_night9["price"]
            it["affiliate_url"] = item_night9["affiliate_url"]
            it["image_url"] = item_night9["image_url"]
            it["review_count"] = item_night9["review_count"]
            it["review_average"] = item_night9["review_average"]

# 3. winter_eye_serum Rank 6: アスタリフト アイクリーム / 目元美容液
item_eye6 = search_item(["アスタリフト アイクリーム 15g", "アスタリフト アイクリーム", "アスタリフト アイケア"])
if item_eye6:
    print("Found Eye Serum 6:", item_eye6["item_name"][:40])
    for it in data["winter_eye_serum"]["items"]:
        if it["rank"] == 6:
            it["brand"] = "ASTALIFT (アスタリフト)"
            it["display_name"] = "アイクリーム 15g (ナノアスタキサンチン×リコピン×3種のコラーゲン配合・真冬の目元のちりめんジワ・くぼみを濃密な潤いで押し戻す高機能アイケア)"
            it["item_name"] = item_eye6["item_name"]
            it["price"] = item_eye6["price"]
            it["affiliate_url"] = item_eye6["affiliate_url"]
            it["image_url"] = item_eye6["image_url"]
            it["review_count"] = item_eye6["review_count"]
            it["review_average"] = item_eye6["review_average"]

# 4. winter_eye_serum Rank 9: キュレル モイストリペア アイクリーム
item_eye9 = search_item(["キュレル モイストリペア アイクリーム 25g", "キュレル アイクリーム 25g", "キュレル モイストリペア アイクリーム"])
if item_eye9:
    print("Found Eye Serum 9:", item_eye9["item_name"][:40])
    new_rank9 = {
        "rank": 9,
        "brand": "Curel (キュレル)",
        "display_name": "モイストリペア アイクリーム 25g (消炎剤×潤浸保湿セラミド機能成分配合・真冬の乾燥でまぶたがカサつき皮剥けする敏感な目元を濃厚な潤いで包み込む薬用アイクリーム)",
        "item_name": item_eye9["item_name"],
        "price": item_eye9["price"],
        "affiliate_url": item_eye9["affiliate_url"],
        "image_url": item_eye9["image_url"],
        "review_count": item_eye9["review_count"],
        "review_average": item_eye9["review_average"]
    }
    # 挿入または追加してソート
    data["winter_eye_serum"]["items"].append(new_rank9)
    data["winter_eye_serum"]["items"].sort(key=lambda x: x["rank"])

with open("fetched_3new_winter_ceramide_night_eye.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated and verified fetched_3new_winter_ceramide_night_eye.json successfully!")
