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

with open("fetched_nov_dec_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def fetch_single(query, rank, brand, name):
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        res_data = json.loads(res.read().decode('utf-8'))
        items = res_data.get("Items", [])
        if not items:
            return None
        chosen = items[0]["Item"]
        for it in items:
            if it["Item"].get("itemPrice", 0) > 1000 and it["Item"].get("mediumImageUrls"):
                chosen = it["Item"]
                break
        
        raw_img = chosen.get("mediumImageUrls", [{}])[0].get("imageUrl", "")
        high_res_img = raw_img
        if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
            high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
        elif "?_ex=" in high_res_img:
            high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
            
        aff_url = chosen.get("affiliateUrl", chosen.get("itemUrl", ""))
        return {
            "rank": rank,
            "brand": brand,
            "display_name": name,
            "rakuten_name": chosen.get("itemName", name),
            "price": chosen.get("itemPrice", 0),
            "image_url": high_res_img,
            "affiliate_url": aff_url,
            "shop_name": chosen.get("shopName", "")
        }

# 1. winter_advent_calendar #8 -> MAC 24デイズ M·A·C アイコン アドベント カレンダー
print("Updating winter_advent_calendar #8 ...")
mac_item = fetch_single("MAC アイコン アドベント カレンダー", 8, "M・A・C (マック)", "24 デイズ M·A·C アイコン アドベント カレンダー (ベストセラーのリップスティックやアイシャドウ・限定ハイライトなど冬のメイクを格上げする超豪華24品セット)")
if mac_item:
    data["winter_advent_calendar"]["items"][7] = mac_item
    print("✓ Updated MAC advent calendar successfully!")

time.sleep(1)

# 2. winter_hyaluronic_serum #8 -> イニスフリー グリーンティー シード ヒアルロン セラム 80ml
print("Updating winter_hyaluronic_serum #8 ...")
innisfree_item = fetch_single("イニスフリー グリーンティー シード ヒアルロン セラム 80ml", 8, "INNISFREE (イニスフリー)", "グリーンティー シード ヒアルロン セラム 80ml (ナノカプセルヒアルロン酸×緑茶乳酸菌配合・角層10層まで瞬間浸透し冬のインナードライを長時間潤す導入美容液)")
if innisfree_item:
    data["winter_hyaluronic_serum"]["items"][7] = innisfree_item
    print("✓ Updated INNISFREE hyaluronic serum successfully!")

time.sleep(1)

# 3. winter_hand_wash #4 -> SABON ハンドソープ 200ml
print("Updating winter_hand_wash #4 ...")
sabon_item = fetch_single("SABON 公式 サボン ハンドソープ 200mL パチュリ", 4, "SABON (サボン)", "ハンドソープ 200ml パチュリ・ラベンダー・バニラ (海藻エキス×アロエエキス配合・なめらかな泡立ちで手肌をいたわりながら上品な香りが持続)")
if sabon_item:
    data["winter_hand_wash"]["items"][3] = sabon_item
    print("✓ Updated SABON hand wash successfully!")

with open("fetched_nov_dec_3articles_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("All 3 items updated and saved to fetched_nov_dec_3articles_data.json!")
