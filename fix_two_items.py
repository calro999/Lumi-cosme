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

def fetch_single(query, brand, display_name, rank):
    for attempt in range(5):
        try:
            time.sleep(2)
            encoded_q = urllib.parse.quote(query)
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    raw_item = items[0]["Item"]
                    raw_img = raw_item.get("mediumImageUrls", [{}])[0].get("imageUrl", "")
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    print(f"SUCCESS: {query} -> {raw_item.get('itemName')[:30]} | {high_res_img}")
                    return {
                        "rank": rank,
                        "brand": brand,
                        "display_name": display_name,
                        "item_name": raw_item.get("itemName", ""),
                        "price": raw_item.get("itemPrice", 0),
                        "affiliate_url": raw_item.get("affiliateUrl", ""),
                        "image_url": high_res_img,
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", "0.0"),
                        "shop_name": raw_item.get("shopName", "")
                    }
        except Exception as e:
            print(f"Attempt {attempt+1} error for {query}: {e}")
            time.sleep(2)
    return None

with open("rakuten_bath_wash_mist_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Fix winter_bath_care Rank 10
item_cow = fetch_single("カウブランド バスミルク", "カウブランド 無添加 (牛乳石鹸)", "無添加 保湿バスミルク (天然セラミド配合・デリケート肌用)", 10)
if item_cow:
    for idx, it in enumerate(data["winter_bath_care"]["items"]):
        if it["rank"] == 10:
            data["winter_bath_care"]["items"][idx] = item_cow

# Fix winter_face_mist Rank 9 (コーセー メイク キープ ミスト EX+ 高保湿モイストタイプ)
item_mist = fetch_single("コーセー メイクキープミスト", "KOSE (コーセー)", "メイク キープ ミスト EX+ (高保湿モイスト＆メイク密着キープ)", 9)
if item_mist:
    for idx, it in enumerate(data["winter_face_mist"]["items"]):
        if it["rank"] == 9:
            data["winter_face_mist"]["items"][idx] = item_mist

with open("rakuten_bath_wash_mist_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated json saved!")
