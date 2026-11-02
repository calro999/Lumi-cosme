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
    "winter_ceramide_lotion": {
        "title": "保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10",
        "page_file": "winter-ceramide-lotion.html",
        "items": [
            {"rank": 1, "query": "セザンヌ スキンコンディショナー高保湿 500ml", "brand": "CEZANNE (セザンヌ)", "name": "スキンコンディショナー 高保湿 500ml (ヒト型セラミド配合)"},
            {"rank": 2, "query": "松山油脂 肌をうるおす 保湿浸透水 120ml", "brand": "松山油脂 (M mark)", "name": "肌をうるおす保湿スキンケア 保湿浸透水 モイストリッチ 120ml"},
            {"rank": 3, "query": "カルテHD モイスチュア ローション 150ml", "brand": "Carte HD (カルテHD)", "name": "モイスチュア ローション 高保湿化粧水 150ml (医薬部外品)"},
            {"rank": 4, "query": "エトヴォス モイスチャライジングローション 150ml", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングローション 150ml (ヒト型セラミド配合)"},
            {"rank": 5, "query": "ケアセラ AP 先行バリア乳液", "brand": "ロート製薬 ケアセラ", "name": "ケアセラ AP 高保湿先行バリア乳液 130ml (8種の天然型セラミド配合)"},
            {"rank": 6, "query": "キュレル ディープモイスチャースプレー 250g", "brand": "Curel (キュレル)", "name": "ディープモイスチャースプレー 250g (医薬部外品 微細化セラミド)"},
            {"rank": 7, "query": "菊正宗 日本酒の化粧水 高保湿 500ml", "brand": "菊正宗 (きくまさむね)", "name": "日本酒の化粧水 高保湿 500ml (セラミド配合)"},
            {"rank": 8, "query": "ink. モイストエッセンスローション 100ml", "brand": "ink. (インク)", "name": "モイストエッセンスローション 100ml (高濃度ヒト型セラミド原液)"},
            {"rank": 9, "query": "ナノエマルジョン 50ml トゥヴェール", "brand": "TOUT VERT (トゥヴェール)", "name": "ナノエマルジョン 50ml (インナードライ対策 浸透湿潤セラミド)"},
            {"rank": 10, "query": "敏感肌用 化粧水 高保湿 300ml 無印良品", "brand": "無印良品 (MUJI)", "name": "敏感肌用 化粧水 高保湿タイプ 300ml (リニューアル版)"}
        ]
    },
    "winter_medicinal_lip": {
        "title": "保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10",
        "page_file": "winter-medicinal-lip.html",
        "items": [
            {"rank": 1, "query": "資生堂 モアリップ 8g", "brand": "資生堂薬品 (SHISEIDO)", "name": "モアリップN 8g (第3類医薬品 / 口唇炎・口角炎治療薬)"},
            {"rank": 2, "query": "ユースキン リリップ ケア スティック", "brand": "yuskin (ユースキン)", "name": "リリップケアスティック 3.5g (医薬部外品 / ひび割れ高密着処方)"},
            {"rank": 3, "query": "メンソレータム ヒビプロ LP 6g", "brand": "ロート製薬 メンソレータム", "name": "メンソレータム ヒビプロ LP 6g (第3類医薬品 / ひび割れ密封修復)"},
            {"rank": 4, "query": "キュレル リップケアバーム 4.2g", "brand": "Curel (キュレル)", "name": "リップケアバーム 4.2g (医薬部外品 / セラミド機能成分配合)"},
            {"rank": 5, "query": "アルージェ トータルモイストベール リップエッセンス 8g", "brand": "Arouge (アルージェ)", "name": "トータルモイストベール リップエッセンス 8g (医薬部外品 / 天然セラミド)"},
            {"rank": 6, "query": "オバジ ダーマパワーX リップエッセンス 10g", "brand": "Obagi (オバジ)", "name": "ダーマパワーX リップエッセンス 10g (ビタミンA誘導体・コラーゲン配合)"},
            {"rank": 7, "query": "ニベア ディープモイスチャー リップ 2.2g", "brand": "NIVEA (ニベア)", "name": "ディープモイスチャーリップ 無香料 2.2g (医薬部外品 / 高保水持続)"},
            {"rank": 8, "query": "ロート製薬 メンソレータム メディカルリップnc 8.5g", "brand": "ロート製薬 メンソレータム", "name": "メンソレータム メディカルリップnc 8.5g (第3類医薬品 / 唇あれ治療薬)"},
            {"rank": 9, "query": "DHC 薬用リップクリーム 1.5g", "brand": "DHC (ディーエイチシー)", "name": "薬用リップクリーム 1.5g (医薬部外品 / オリーブバージンオイル配合)"},
            {"rank": 10, "query": "ロート製薬 メンソレータム メルティクリームリップ 無香料 2.4g", "brand": "ロート製薬 メンソレータム", "name": "メルティクリームリップ 無香料 2.4g (モイストバンク技術)"}
        ]
    },
    "winter_squalane_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！たった1滴で極上ツヤ膜を張る高純度スクワランオイルランク10",
        "page_file": "winter-squalane-oil.html",
        "items": [
            {"rank": 1, "query": "HABA スクワラン 30ml", "brand": "HABA (ハーバー)", "name": "高品位スクワラン 30ml (純度99.9% 美容オイル)"},
            {"rank": 2, "query": "無印良品 オリーブスクワランオイル 100ml", "brand": "無印良品 (MUJI)", "name": "オリーブスクワランオイル 100ml (天然植物由来100%)"},
            {"rank": 3, "query": "KISO キソ スクワラン", "brand": "KISO (キソ)", "name": "スクワランオイル 50ml (深海鮫肝油 スクワラン100%)"},
            {"rank": 4, "query": "HABA スクワランII 60ml", "brand": "HABA (ハーバー)", "name": "スクワランII 60ml (植物由来スクワラン配合)"},
            {"rank": 5, "query": "チューンメーカーズ 精製スクワラン 20ml", "brand": "TUNEMAKERS (チューンメーカーズ)", "name": "精製スクワラン 原液 20ml"},
            {"rank": 6, "query": "ハイム スクワランオイル 60ml", "brand": "ハイム化粧品 (HEIM)", "name": "スクワランオイル 60ml (無香料・無着色・高純度オイル)"},
            {"rank": 7, "query": "spa hinoki スクワラン", "brand": "spa hinoki (スパヒノキ)", "name": "スクワラン 美容オイル 50ml (純度99%以上 国産)"},
            {"rank": 8, "query": "The Ordinary 植物由来 スクワラン", "brand": "The Ordinary (ジオーディナリー)", "name": "100%植物由来スクワラン 30ml (Plant-Derived Squalane)"},
            {"rank": 9, "query": "スクワランオイル 100ml 美容オイル", "brand": "&SH (アンドエスエイチ)", "name": "スクワランオイル 100ml (天然ピュアオイル)"},
            {"rank": 10, "query": "Sugar Squalane Oil 植物性スクワラン", "brand": "Sugar Squalane (シュガースクワラン)", "name": "シュガー スクワランオイル 30ml (植物性サトウキビ由来)"}
        ]
    }
}

def fetch_single(query_info):
    q = query_info["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        data = json.loads(res.read().decode('utf-8'))
        items = data.get("Items", [])
        if not items:
            return None
        chosen = None
        for it in items:
            item_obj = it["Item"]
            if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
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
            "rank": query_info["rank"],
            "brand": query_info["brand"],
            "name": query_info["name"],
            "query": q,
            "rakuten_name": chosen.get("itemName", ""),
            "price": chosen.get("itemPrice", 0),
            "image": img_url,
            "affiliateUrl": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
            "reviewCount": chosen.get("reviewCount", 0),
            "reviewAverage": chosen.get("reviewAverage", "0.0")
        }

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title']})")
    print(f"==========================================")
    cat_results = []
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['name']} ...")
        res = None
        for retry in range(3):
            try:
                res = fetch_single(item_info)
                if res:
                    break
            except Exception as e:
                print(f"  Retry {retry+1} due to error: {e}")
                time.sleep(2.0)
            time.sleep(1.0)
            
        if res:
            print(f"  ✓ Found: {res['rakuten_name'][:45]}... (¥{res['price']:,})")
            cat_results.append(res)
        else:
            print(f"  ❌ FAILED to fetch: {item_info['name']}")
        time.sleep(1.2)
    
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_results
    }

output_path = "fetched_3new_nov_dec_ceramide_lotion_lip_squalane_data.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n✓ Saved all 30 fetched items to {output_path}")
