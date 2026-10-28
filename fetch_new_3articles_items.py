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
    "winter_lotion": {
        "title": "高保湿化粧水＆とろみ浸透ローション",
        "page_file": "winter-lotion.html",
        "items": [
            {"rank": 1, "query": "イプサ タイムR アクア", "brand": "IPSA (イプサ)", "name": "ザ・タイムR アクア 【医薬部外品】 (薬用水分保持化粧水)"},
            {"rank": 2, "query": "アクセーヌ モイストバランス ローション", "brand": "ACSEINE (アクセーヌ)", "name": "モイストバランス ローション (超微細ナノカプセル高保湿化粧水)"},
            {"rank": 3, "query": "エスト ローション", "brand": "est (エスト)", "name": "エスト ザ ローション (砂漠植物エクトイン高保水化粧水)"},
            {"rank": 4, "query": "カルテHD モイスチュア ローション", "brand": "Carte HD (カルテHD)", "name": "モイスチュア ローション 【医薬部外品】 (ヘパリン類似物質配合)"},
            {"rank": 5, "query": "オルビスユー エッセンスローション", "brand": "ORBIS (オルビス)", "name": "オルビスユー エッセンスローション 【医薬部外品】 (とろぱしゃ濃密化粧水)"},
            {"rank": 6, "query": "コスメデコルテ リポソーム トリートメントリキッド", "brand": "DECORTÉ (コスメデコルテ)", "name": "リポソーム トリートメント リキッド (多重層リポソーム化粧水)"},
            {"rank": 7, "query": "カネボウ スキン ハーモナイザー", "brand": "KANEBO (カネボウ)", "name": "スキン ハーモナイザー (皮脂制御×オイルイン2層式ローション)"},
            {"rank": 8, "query": "白潤プレミアム 薬用浸透美白化粧水", "brand": "肌ラボ (ロート製薬)", "name": "白潤プレミアム 薬用浸透美白化粧水 【医薬部外品】 (トラネキサム酸配合)"},
            {"rank": 9, "query": "極潤プレミアム ヒアルロン液", "brand": "肌ラボ (ロート製薬)", "name": "極潤プレミアム ヒアルロン液 (8種のヒアルロン酸配合濃厚とろみ)"},
            {"rank": 10, "query": "アテニア ドレスリフト ローション", "brand": "Attenir (アテニア)", "name": "ドレスリフト ローション 【医薬部外品】 (高密度ハリ保湿化粧水)"}
        ]
    },
    "winter_cleansing": {
        "title": "高保湿クレンジングバーム＆濃密ミルク",
        "page_file": "winter-cleansing.html",
        "items": [
            {"rank": 1, "query": "DUO クレンジングバーム", "brand": "DUO (デュオ)", "name": "ザ クレンジングバーム (とろける高保湿毛穴ケア)"},
            {"rank": 2, "query": "カバーマーク トリートメント クレンジングミルク", "brand": "COVERMARK (カバーマーク)", "name": "トリートメント クレンジング ミルク (美容液成分89%配合)"},
            {"rank": 3, "query": "シュウウエムラ アルティム8 クレンジング オイル", "brand": "shu uemura (シュウ ウエムラ)", "name": "アルティム8∞ スブリム ビューティ クレンジング オイルn"},
            {"rank": 4, "query": "カネボウ メロウ オフ ヴェール", "brand": "KANEBO (カネボウ)", "name": "メロウ オフ ヴェール (吸い付くとろみクレンジングクリーム)"},
            {"rank": 5, "query": "ファンケル マイルドクレンジング オイル", "brand": "FANCL (ファンケル)", "name": "マイルドクレンジング オイル (熟成ホップエキス配合・バリア保護)"},
            {"rank": 6, "query": "バニラコ クリーンイットゼロ クレンジング バーム", "brand": "BANILA CO (バニラコ)", "name": "クリーン イット ゼロ クレンジング バーム オリジナル"},
            {"rank": 7, "query": "アテニア スキンクリア クレンズ オイル アロマ", "brand": "Attenir (アテニア)", "name": "スキンクリア クレンズ オイル アロマタイプ (肌ステインオフ)"},
            {"rank": 8, "query": "クリニーク テイクデイオフ クレンジングバーム", "brand": "CLINIQUE (クリニーク)", "name": "テイク ザ デイ オフ クレンジング バーム (低刺激・乳化クレンジング)"},
            {"rank": 9, "query": "ミノン アミノモイスト クレンジング", "brand": "MINON (ミノン)", "name": "アミノモイスト モイストミルキィ クレンジング (乾燥敏感肌用)"},
            {"rank": 10, "query": "コスメデコルテ AQ クレンジングオイル", "brand": "DECORTÉ (コスメデコルテ)", "name": "AQ クレンジング オイル (上質エモリエント補給)"}
        ]
    },
    "winter_day_cream": {
        "title": "高保湿UV美容液＆朝用デイクリーム",
        "page_file": "winter-day-cream.html",
        "items": [
            {"rank": 1, "query": "カネボウ クリーム イン デイ", "brand": "KANEBO (カネボウ)", "name": "クリーム イン デイ SPF20 / PA+++ (朝のうるおい水分パック)"},
            {"rank": 2, "query": "ランコム エクスペール トーンアップ ローズ", "brand": "LANCÔME (ランコム)", "name": "UV エクスペール トーン アップ ローズ N SPF50+ / PA++++"},
            {"rank": 3, "query": "コスメデコルテ サンシェルター トーンアップCC", "brand": "DECORTÉ (コスメデコルテ)", "name": "サンシェルター マルチ プロテクション トーンアップCC SPF50+ / PA++++"},
            {"rank": 4, "query": "オルビス リンクルブライトUVプロテクター", "brand": "ORBIS (オルビス)", "name": "リンクルブライトUVプロテクター 【医薬部外品】 SPF50+ / PA++++ (シワ改善・美白)"},
            {"rank": 5, "query": "エリクシール デーケアレボリューション トーンアップ", "brand": "ELIXIR (エリクシール)", "name": "デーケアレボリューション トーンアップ SP+ aa 【医薬部外品】 SPF50+ / PA++++"},
            {"rank": 6, "query": "アスタリフト ホワイトソリューション", "brand": "ASTALIFT (アスタリフト)", "name": "D-UVクリア ホワイトソリューション SPF50+ / PA++++ (表情追従UV)"},
            {"rank": 7, "query": "ラロッシュポゼ UVイデア トーンアップ ローズ", "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)", "name": "UVイデア XL プロテクショントーンアップ ローズ SPF50+ / PA++++"},
            {"rank": 8, "query": "ダルバ トーンアップ サンクリーム", "brand": "d'Alba (ダルバ)", "name": "ウォータフル トーンアップ サンクリーム SPF50+ / PA++++ (白トリュフ配合水光UV)"},
            {"rank": 9, "query": "クレドポーボーテ クレームUV", "brand": "Clé de Peau Beauté (クレ・ド・ポー ボーテ)", "name": "クレームUV n SPF50+ / PA++++ (極上エイジングケア日焼け止め)"},
            {"rank": 10, "query": "キュレル 潤浸保湿 UVエッセンス", "brand": "Curel (キュレル)", "name": "潤浸保湿 UVエッセンス 【医薬部外品】 SPF30 / PA+++ (セラミド機能成分配合)"}
        ]
    }
}

def clean_query(q):
    # 楽天APIで400になる1文字単語を除去
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
                        "shop_name": raw_item.get("shopName", ""),
                        "review_count": raw_item.get("reviewCount", 0),
                        "review_average": raw_item.get("reviewAverage", 0)
                    }
                else:
                    print(f"No item found for query '{query}' (attempt {attempt+1})")
        except urllib.error.HTTPError as e:
            print(f"HTTPError fetching '{query}' (attempt {attempt+1}): {e.code}")
            time.sleep(1.5)
        except Exception as e:
            print(f"Error fetching '{query}' (attempt {attempt+1}): {e}")
            time.sleep(1.5)
        time.sleep(1.0)
    return None

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n=== Fetching category: {cat_data['title']} ===")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Fetching Rank {item_info['rank']}: {item_info['name']} ...", end=" ", flush=True)
        res = fetch_item_with_retry(item_info)
        if res:
            print(f"OK (Price: ¥{res['price']:,}, Shop: {res['shop_name'][:15]})")
            results[cat_key]["items"].append(res)
        else:
            print("FAILED")
        time.sleep(1.1)

output_file = "rakuten_new_3articles_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nAll data successfully fetched and saved to {output_file}!")
