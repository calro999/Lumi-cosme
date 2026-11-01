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

with open("rakuten_hair_lip_carbonic_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

# 1. オージュア クエンチ ヘアトリートメント 250g 単品
q1 = clean_query("ミルボン オージュア クエンチ ヘアトリートメント 250g")
url1 = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q1)}&hits=5&format=json"
req1 = urllib.request.Request(url1, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req1, context=ctx) as res:
    d = json.loads(res.read())
    chosen = None
    for it in d["Items"]:
        name = it["Item"]["itemName"]
        if "ヘアトリートメント" in name and "シャンプー" not in name:
            chosen = it["Item"]
            break
    if chosen:
        raw_img = chosen["mediumImageUrls"][0]["imageUrl"]
        high_res = raw_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
        data["winter_hair_treatment"]["items"][0] = {
            "rank": 1,
            "name": "クエンチ ヘアトリートメント 250g (乾燥でパサつく毛髪内部の水分保持力を補修・しっとりまとまるサロン最高峰)",
            "brand": "Aujua (オージュア / ミルボン)",
            "query_used": q1,
            "rakuten_item_name": chosen["itemName"],
            "price": chosen["itemPrice"],
            "image_url": high_res,
            "affiliate_url": chosen["affiliateUrl"] or chosen["itemUrl"],
            "shop_name": chosen["shopName"]
        }
        print("Updated Aujua Treatment Rank 1!")

time.sleep(0.5)

# 2. スティーブンノル モイスチュアコントロール ヘアパック W 220g
q2 = clean_query("スティーブンノル モイスチュアコントロール ヘアパック")
url2 = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q2)}&hits=5&format=json"
req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req2, context=ctx) as res:
    d = json.loads(res.read())
    chosen = d["Items"][0]["Item"]
    raw_img = chosen["mediumImageUrls"][0]["imageUrl"]
    high_res = raw_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
    data["winter_hair_treatment"]["items"][8] = {
        "rank": 9,
        "name": "モイスチュアコントロール ヘアパック W 220g (コーセー独自の高浸透モイスチュアカプセル配合・パサつき深層までうるおいを届けるサロン発想)",
        "brand": "STEPHEN KNOLL (スティーブンノル)",
        "query_used": q2,
        "rakuten_item_name": chosen["itemName"],
        "price": chosen["itemPrice"],
        "image_url": high_res,
        "affiliate_url": chosen["affiliateUrl"] or chosen["itemUrl"],
        "shop_name": chosen["shopName"]
    }
    print("Updated Stephen Knoll Rank 9!")

time.sleep(0.5)

# 3. オルビス ホワイトクリアエッセンス 本品 25ml
q3 = clean_query("オルビス ホワイトクリアエッセンス ボトル入り")
url3 = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q3)}&hits=5&format=json"
req3 = urllib.request.Request(url3, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req3, context=ctx) as res:
    d = json.loads(res.read())
    chosen = None
    for it in d["Items"]:
        name = it["Item"]["itemName"]
        if "6ml" not in name and "ミニ" not in name:
            chosen = it["Item"]
            break
    if not chosen and d["Items"]:
        chosen = d["Items"][0]["Item"]
    if chosen:
        raw_img = chosen["mediumImageUrls"][0]["imageUrl"]
        high_res = raw_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
        data["winter_carbonic_serum"]["items"][6] = {
            "rank": 7,
            "name": "ホワイトクリアエッセンス 25ml [医薬部外品] (m-ピクセノール配合・冬の血行不良とメラニン蓄積による頑固なくすみを晴らしうるおい透明素肌へ導く)",
            "brand": "ORBIS (オルビス)",
            "query_used": q3,
            "rakuten_item_name": chosen["itemName"],
            "price": chosen["itemPrice"],
            "image_url": high_res,
            "affiliate_url": chosen["affiliateUrl"] or chosen["itemUrl"],
            "shop_name": chosen["shopName"]
        }
        print("Updated Orbis Rank 7!")

with open("rakuten_hair_lip_carbonic_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All refined perfectly!")
