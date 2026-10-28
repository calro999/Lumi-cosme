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
    "winter_bath_care": {
        "title": "高保湿入浴剤＆バスミルク",
        "page_file": "winter-bath-care.html",
        "items": [
            {"rank": 1, "query": "アユーラ メディテーションバス", "brand": "AYURA (アユーラ)", "name": "メディテーションバスt (安らぎのアロマ・うるおい2層式入浴剤)"},
            {"rank": 2, "query": "BARTH 中性重炭酸入浴剤", "brand": "BARTH (バース)", "name": "薬用 BARTH 中性重炭酸入浴剤 【医薬部外品】 (血行促進・疲労回復・温活)"},
            {"rank": 3, "query": "キュレル 入浴剤", "brand": "Curel (キュレル)", "name": "潤浸保湿 入浴剤 【医薬部外品】 (セラミド機能成分配合・乾燥肌用)"},
            {"rank": 4, "query": "クナイプ バスソルト ホップ バレリアン", "brand": "Kneipp (クナイプ)", "name": "バスソルト グーテナハト ホップ＆バレリアンの香り (天然岩塩温活)"},
            {"rank": 5, "query": "シークリスタルス エプソムソルト", "brand": "Sea Crystals (シークリスタルス)", "name": "エプソムソルト オリジナル (硫酸マグネシウム・超微細温活ミネラル)"},
            {"rank": 6, "query": "ミノン 薬用保湿入浴剤", "brand": "MINON (ミノン)", "name": "薬用保湿入浴剤 【医薬部外品】 (11種のアミノ酸配合・敏感肌処方)"},
            {"rank": 7, "query": "ウルモア 保湿入浴液 クリーミーフローラルの香り", "brand": "ウルモア (アース製薬)", "name": "保湿入浴液 ウルモア クリーミーフローラル (濃厚とろみベール)"},
            {"rank": 8, "query": "SABON バスソルト ローズ", "brand": "SABON (サボン)", "name": "バスソルト ローズ (死海の塩＆贅沢エッセンシャルオイル)"},
            {"rank": 9, "query": "ヴェレダ アルニカ バスミルク", "brand": "WELEDA (ヴェレダ)", "name": "アルニカ バスミルク (天然ハーブエキス＆植物オイル保湿)"},
            {"rank": 10, "query": "カウブランド 無添加 保湿入浴付替", "brand": "カウブランド 無添加", "name": "無添加 薬用肌をいたわる保湿入浴料 【医薬部外品】 (天然セラミド配合)"}
        ]
    },
    "winter_face_wash": {
        "title": "うるおい吸着・高保湿洗顔料",
        "page_file": "winter-face-wash.html",
        "items": [
            {"rank": 1, "query": "カネボウ コンフォート ストレッチィ ウォッシュ", "brand": "KANEBO (カネボウ)", "name": "コンフォート ストレッチィ ウォッシュ (糸引く濃密泡・美容液洗顔)"},
            {"rank": 2, "query": "オバジX フレームリフト ムースウォッシュ", "brand": "Obagi (オバジ)", "name": "オバジX フレームリフト ムースウォッシュ (炭酸濃密ホイップ泡洗顔)"},
            {"rank": 3, "query": "エスト AC クラリファイイング ウォッシュ", "brand": "est (エスト)", "name": "AC クラリファイイング ウォッシュ (温感ジェル・角栓毛穴洗浄)"},
            {"rank": 4, "query": "オルビスユードット フォーミングウォッシュ", "brand": "ORBIS (オルビス)", "name": "オルビスユードット フォーミングウォッシュ 【医薬部外品】 (高密着ねばり泡)"},
            {"rank": 5, "query": "ソフィーナiP リニュー ムース ウォッシュ", "brand": "SOFINA iP (ソフィーナiP)", "name": "リニュー ムース ウォッシュ (100%炭酸マイクロ泡・血行促進洗顔)"},
            {"rank": 6, "query": "キュレル 潤浸保湿 泡洗顔料", "brand": "Curel (キュレル)", "name": "潤浸保湿 泡洗顔料 【医薬部外品】 (セラミドを守って洗う消炎剤配合)"},
            {"rank": 7, "query": "コスメデコルテ クレイブラン", "brand": "DECORTÉ (コスメデコルテ)", "name": "クレイ ブラン (ホワイトクレイ配合・うるおい吸着洗顔クリーム)"},
            {"rank": 8, "query": "ミノン アミノモイスト ジェントルウォッシュ ホイップ", "brand": "MINON (ミノン)", "name": "アミノモイスト ジェントルウォッシュ ホイップ (9種の保水アミノ酸)"},
            {"rank": 9, "query": "ファンケル 泥ジェル洗顔", "brand": "FANCL (ファンケル)", "name": "泥ジェル洗顔 (泡立てない3way毛穴マッサージ洗顔ジェル)"},
            {"rank": 10, "query": "ポーラ BA ウォッシュ", "brand": "POLA (ポーラ)", "name": "B.A ウォッシュ N (極上弾力泡・糖化くすみクリア洗顔クリーム)"}
        ]
    },
    "winter_face_mist": {
        "title": "高保湿ミスト化粧水＆オイルミスト",
        "page_file": "winter-face-mist.html",
        "items": [
            {"rank": 1, "query": "エリクシール シュペリエル つや玉ミスト", "brand": "ELIXIR (エリクシール)", "name": "つや玉ミスト (美容水×美容オイル2層式うるおいヴェール)"},
            {"rank": 2, "query": "ダルバ ホワイトトリュフ ファースト スプレー セラム", "brand": "d'Alba (ダルバ)", "name": "ホワイトトリュフ ファースト スプレー セラム (白トリュフ配合水光ミスト)"},
            {"rank": 3, "query": "コスメデコルテ コンフォート デイミスト セット プロテクト", "brand": "DECORTÉ (コスメデコルテ)", "name": "コンフォート デイミスト セット＆プロテクト (メイクキープ＆高保湿)"},
            {"rank": 4, "query": "キュレル ディープモイスチャースプレー 150g", "brand": "Curel (キュレル)", "name": "ディープモイスチャースプレー 【医薬部外品】 (微細化セラミドカプセル)"},
            {"rank": 5, "query": "dプログラム アレルバリア ミスト N", "brand": "d program (資生堂)", "name": "アレルバリア ミスト N (花粉・ちり・ほこり・乾燥ブロック2層ミスト)"},
            {"rank": 6, "query": "CNP プロポリス アンプル ミスト", "brand": "CNP Laboratory (チャアンドパク)", "name": "プロポリス トリートメント アンプル ミスト (濃厚ハチミツうるおいチャージ)"},
            {"rank": 7, "query": "アベンヌ ウオーター 300ml", "brand": "Avene (アベンヌ)", "name": "アベンヌ ウオーター (南仏の深層ミネラル温泉水100%スプレー)"},
            {"rank": 8, "query": "クラランス フィックス メイクアップ", "brand": "CLARINS (クラランス)", "name": "フィックス メイクアップ (ダマスクローズ水配合・密着ミスト)"},
            {"rank": 9, "query": "アディクション メイクアップ フィックス マイクロ ミスト", "brand": "ADDICTION (アディクション)", "name": "メイクアップ フィックス マイクロ ミスト (超微細超微粒子うるおいヴェール)"},
            {"rank": 10, "query": "ラロッシュポゼ ターマルウォーター 300g", "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)", "name": "ターマルウォーター (セレン豊富・バリア機能をサポートする整肌ミスト)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    for attempt in range(5):
        try:
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=3&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
                data = json.loads(res.read().decode('utf-8'))
                items = data.get("Items", [])
                if items:
                    raw_item = items[0]["Item"]
                    raw_img = ""
                    if raw_item.get("mediumImageUrls"):
                        raw_img = raw_item["mediumImageUrls"][0].get("imageUrl", "")
                    
                    high_res_img = raw_img
                    if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                        high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
                    elif "?_ex=" in high_res_img:
                        high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "display_name": query_info["name"],
                        "item_name": raw_item.get("itemName", ""),
                        "price": raw_item.get("itemPrice", 0),
                        "affiliate_url": raw_item.get("affiliateUrl", ""),
                        "image_url": high_res_img,
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", "0.0"),
                        "shop_name": raw_item.get("shopName", "")
                    }
                else:
                    print(f"  [Attempt {attempt+1}] No items for: {query}")
        except Exception as e:
            print(f"  [Attempt {attempt+1}] Error fetching {query}: {e}")
        time.sleep(1)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "display_name": query_info["name"],
        "item_name": query_info["name"],
        "price": 0,
        "affiliate_url": f"https://search.rakuten.co.jp/search/mall/{urllib.parse.quote(query)}/",
        "image_url": "https://lumi-cosme.vercel.app/2.jpg",
        "review_count": 0,
        "review_average": "0.0",
        "shop_name": ""
    }

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_data['title']} ({cat_key})")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['name']} (Query: {item_info['query']})")
        item_res = fetch_item_with_retry(item_info)
        print(f"  -> Found: {item_res['item_name'][:45]}... | ¥{item_res['price']:,} | Img: {item_res['image_url'][:50]}")
        results[cat_key]["items"].append(item_res)
        time.sleep(0.5)

output_filename = "rakuten_bath_wash_mist_data.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAll items successfully fetched and saved to {output_filename}")
