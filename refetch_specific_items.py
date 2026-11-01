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

def fetch_single_item(query, orig_info):
    c_query = clean_query(query)
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(c_query)}&hits=10&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                res_data = json.loads(res.read().decode('utf-8'))
                items = res_data.get("Items", [])
                if items:
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        p = item_obj.get("itemPrice", 0)
                        # ふるさと納税や極端なまとめ売りを除外
                        if "ふるさと納税" in item_obj.get("itemName", ""):
                            continue
                        if orig_info.get("max_price") and p > orig_info["max_price"]:
                            continue
                        if orig_info.get("must_word") and orig_info["must_word"] not in item_obj.get("itemName", ""):
                            continue
                        if p > 0 and item_obj.get("mediumImageUrls"):
                            chosen = item_obj
                            break
                    if not chosen:
                        # 条件に合うものがなければ先頭で除外なし
                        for it in items:
                            if "ふるさと納税" not in it["Item"].get("itemName", "") and it["Item"].get("mediumImageUrls"):
                                chosen = it["Item"]
                                break
                    if not chosen:
                        chosen = items[0]["Item"]

                    raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "") if chosen.get("mediumImageUrls") else ""
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    price = chosen.get("itemPrice", 0)
                    aff_url = chosen.get("affiliateUrl", "") or chosen.get("itemUrl", "")
                    
                    return {
                        "rank": orig_info["rank"],
                        "name": orig_info["name"],
                        "brand": orig_info["brand"],
                        "query_used": c_query,
                        "rakuten_item_name": chosen.get("itemName", ""),
                        "price": price,
                        "image_url": high_res_img,
                        "affiliate_url": aff_url,
                        "shop_name": chosen.get("shopName", "")
                    }
        except Exception as e:
            print(f"Error on attempt {attempt+1} for {query}: {e}")
            time.sleep(1.0)
    return None

# 修正対象アイテム
fixes = [
    # ヘアトリートメント 1位: オージュア クエンチ トリートメント
    {
        "cat": "winter_hair_treatment",
        "rank": 1,
        "query": "オージュア クエンチ ヘアトリートメント",
        "must_word": "トリートメント",
        "max_price": 8000,
        "brand": "Aujua (オージュア / ミルボン)",
        "name": "クエンチ ヘアトリートメント 250g (乾燥でパサつく毛髪内部の水分保持力を補修・しっとりまとまるサロン最高峰)"
    },
    # ヘアトリートメント 9位: スティーブンノル リゲイン トリートメント
    {
        "cat": "winter_hair_treatment",
        "rank": 9,
        "query": "スティーブンノル モイスチュア リゲイン ヘアパック",
        "must_word": "ヘアパック",
        "max_price": 3000,
        "brand": "STEPHEN KNOLL (スティーブンノル)",
        "name": "モイスチュア リゲイン ヘアパック 250g (コーセー独自の高浸透モイスチュアカプセル配合・パサつき深層までうるおいを届けるサロン発想)"
    },
    # ヘアトリートメント 10位: ラックス スーパーリッチシャイン トリートメント
    {
        "cat": "winter_hair_treatment",
        "rank": 10,
        "query": "ラックス スーパーリッチシャイン ダメージリペア トリートメント 300g",
        "max_price": 2500,
        "brand": "LUX (ラックス)",
        "name": "スーパーリッチシャイン ダメージリペア リッチ補修トリートメント 300g (プレミアムゴールドヒアルロン酸オイル配合・冬の枝毛パサつきを濃厚補修)"
    },
    # リップ 5位: メンソレータム ディープモイスト 単品
    {
        "cat": "winter_lip_balm",
        "rank": 5,
        "query": "ロート製薬 メンソレータム ディープモイスト 無香料",
        "max_price": 1000,
        "brand": "メンソレータム (ロート製薬)",
        "name": "ディープモイスト 無香料 4.5g (ヒアルロン酸・シアバター・ホホバオイル配合・楕円形スティックで口角まで塗りやすい薬用高保湿リップ)"
    },
    # リップ 6位: DHC 薬用リップクリーム 単品
    {
        "cat": "winter_lip_balm",
        "rank": 6,
        "query": "DHC 薬用リップクリーム 1.5g",
        "max_price": 1500,
        "brand": "DHC (ディーエイチシー)",
        "name": "薬用リップクリーム 1.5g (高純度オリーブバージンオイル・アロエエキス配合・人の皮脂に似た植物オイルが薄い保護膜を張るロングセラー)"
    },
    # 炭酸泡美容液 7位: オルビス ホワイトクリアエッセンス 本品
    {
        "cat": "winter_carbonic_serum",
        "rank": 7,
        "query": "オルビス ホワイトクリアエッセンス 25ml",
        "max_price": 4500,
        "brand": "ORBIS (オルビス)",
        "name": "ホワイトクリアエッセンス 25ml [医薬部外品] (m-ピクセノール配合・冬の血行不良とメラニン蓄積による頑固なくすみを晴らしうるおい透明素肌へ導く)"
    },
    # 炭酸泡美容液 8位: ソフィーナ iP リニュームース トリートメント（濃密炭酸泡）
    {
        "cat": "winter_carbonic_serum",
        "rank": 8,
        "query": "ソフィーナ iP リニュー ムース ウォッシュ 200g",
        "max_price": 5000,
        "brand": "SOFINA iP (ソフィーナiP)",
        "name": "リニュー ムース ウォッシュ 200g (100%マイクロ炭酸泡・洗うだけで血行促進＆角層をやわらかく解きほぐす高保湿炭酸濃密泡トリートメント)"
    }
]

for item_fix in fixes:
    print(f"Refetching: {item_fix['cat']} rank {item_fix['rank']} -> {item_fix['query']}")
    res = fetch_single_item(item_fix["query"], item_fix)
    if res:
        print(f"  -> Success: {res['rakuten_item_name'][:30]} | ¥{res['price']:,} | Img: {res['image_url'][:50]}")
        # 置換
        target_list = data[item_fix["cat"]]["items"]
        for idx, orig in enumerate(target_list):
            if orig["rank"] == item_fix["rank"]:
                target_list[idx] = res
                break
    else:
        print(f"  -> Failed to fetch {item_fix['query']}")
    time.sleep(0.5)

with open("rakuten_hair_lip_carbonic_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated rakuten_hair_lip_carbonic_data.json successfully!")
