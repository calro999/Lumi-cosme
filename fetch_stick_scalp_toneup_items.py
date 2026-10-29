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
    "winter_stick_serum": {
        "title": "高保湿スティック美容液＆ポータブル保湿バーム",
        "page_file": "winter-stick-serum.html",
        "items": [
            {"rank": 1, "query": "イプサ ザ・タイムR デイエッセンススティックe", "brand": "IPSA (イプサ)", "name": "ザ・タイムR デイエッセンススティックe (水分約65%配合・メイク直しうるおいスティック)"},
            {"rank": 2, "query": "KAHI リンクルバウンス マルチバーム", "brand": "KAHI (カヒ)", "name": "リンクルバウンス マルチバーム (サーモン複合体×済州島天然発酵オイルスティック)"},
            {"rank": 3, "query": "ダルバ マルチバーム スティック", "brand": "d'Alba (ダルバ)", "name": "ダブルセラム オールインワンマルチバーム (ホワイトトリュフ×2層式高保湿スティック)"},
            {"rank": 4, "query": "アスタリフト ザ セラム リンクルリペア 朝用", "brand": "ASTALIFT (アスタリフト)", "name": "ザ セラム リンクルリペア 朝用 【医薬部外品】 (ナイアシンアミド・朝用シールドスティック)"},
            {"rank": 5, "query": "クラブ エアリータッチ デイエッセンス", "brand": "クラブコスメチックス (club)", "name": "エアリータッチ デイエッセンス (うるおい成分80%・極細偏光パールスティック)"},
            {"rank": 6, "query": "エトヴォス ミネラルラディアントスキンバーム", "brand": "ETVOS (エトヴォス)", "name": "ミネラルラディアントスキンバーム (植物オイル×天然ミネラルハイライトバーム)"},
            {"rank": 7, "query": "タイムシークレット 薬用デイエッセンスバーム", "brand": "TIME SECRET (タイムシークレット)", "name": "薬用デイエッセンスバーム 【医薬部外品】 (ナイアシンアミド配合・シワ改善スティック)"},
            {"rank": 8, "query": "コスメデコルテ スティックセラム", "brand": "DECORTÉ (コスメデコルテ)", "name": "ホワイトロジスト スティックセラム 【医薬部外品】 (コウジ酸美白＆集中保湿スティック)"},
            {"rank": 9, "query": "ネイチャーリパブリック スティック美容液", "brand": "NATURE REPUBLIC", "name": "インテンスマルチアンプルバーム (コラーゲン＆プロポリス濃縮ケアスティック)"},
            {"rank": 10, "query": "MiMC ビオモイスチュアスティック", "brand": "MiMC (エムアイエムシー)", "name": "ビオモイスチュアスティック (オメガ3・6リッチオイル・天然100%植物バーム)"}
        ]
    },
    "winter_scalp_serum": {
        "title": "高保湿スカルプローション＆頭皮用美容液",
        "page_file": "winter-scalp-serum.html",
        "items": [
            {"rank": 1, "query": "キュレル 頭皮保湿ローション 120ml", "brand": "Curel (キュレル)", "name": "頭皮保湿ローション 【医薬部外品】 (セラミド機能成分配合・ダイレクトタッチノズル)"},
            {"rank": 2, "query": "ミルボン オージュア モイストカーム ローション", "brand": "Aujua (ミルボン オージュア)", "name": "モイストカーム モイスチュアローション (角層深部保湿・地肌かゆみ乾燥リペア)"},
            {"rank": 3, "query": "ヴェレダ ヘアトニック", "brand": "WELEDA (ヴェレダ)", "name": "オーガニック ヘアトニック (天然ハーブエキス・伝統のヘッドスカルプローション)"},
            {"rank": 4, "query": "無印良品 スカルプケアローション", "brand": "無印良品 (MUJI)", "name": "植物発酵液 薬用スカルプローション 【医薬部外品】 (米ぬか発酵液×植物エキス頭皮保湿)"},
            {"rank": 5, "query": "アスタリフト スカルプフォーカス エッセンス 150ml", "brand": "ASTALIFT (アスタリフト)", "name": "スカルプフォーカス エッセンス 【医薬部外品】 (ナノアスタキサンチン・薬用頭皮育毛美容液)"},
            {"rank": 6, "query": "サブリミック アデノバイタル スカルプ パワーショット", "brand": "SHISEIDO (資生堂プロフェッショナル)", "name": "サブリミック アデノバイタル スカルプ パワーショット 【医薬部外品】 (最先端薬用頭皮エッセンス)"},
            {"rank": 7, "query": "ジョンマスター スカルプ", "brand": "john masters organics", "name": "ディープスカルプPセラム (ピュリファイングスカルプ・濃密ボタニカル頭皮美容液)"},
            {"rank": 8, "query": "資生堂 アデノゲン 薬用アデノゲンEX", "brand": "SHISEIDO (資生堂)", "name": "薬用アデノゲンEX 【医薬部外品】 (生体内薬用成分アデノシン配合・頭皮血行＆保湿エッセンス)"},
            {"rank": 9, "query": "スカルプD ボーテ 薬用スカルプセラム", "brand": "アンファー (ANGFA)", "name": "スカルプD ボーテ メディカルエストロジー スカルプセラム 【医薬部外品】 (ソイセラム配合)"},
            {"rank": 10, "query": "ちふれ 薬用育毛エッセンス", "brand": "ちふれ (CHIFURE)", "name": "薬用育毛エッセンス 【医薬部外品】 (甘草・センブリ抽出液・無香料頭皮ローション)"}
        ]
    },
    "winter_toneup_base": {
        "title": "高保湿コントロールカラー＆血色感トーンアップ下地",
        "page_file": "winter-toneup-base.html",
        "items": [
            {"rank": 1, "query": "ポール&ジョー モイスチュアライジング プライマー", "brand": "PAUL & JOE (ポール＆ジョー)", "name": "モイスチュアライジング ファンデーション プライマー (美容液成分90%・うるおい濃密下地)"},
            {"rank": 2, "query": "コスメデコルテ ロージー グロウライザー", "brand": "DECORTÉ (コスメデコルテ)", "name": "ロージー グロウライザー (内側から発光する血色ピンク・光のヴェール下地)"},
            {"rank": 3, "query": "ジルスチュアート イルミネイティング セラムプライマー", "brand": "JILL STUART (ジルスチュアート)", "name": "イルミネイティング セラムプライマー (ミルクのようになめらか・ツヤ肌セラムベース)"},
            {"rank": 4, "query": "エレガンス モデリング カラーアップ ベース UV", "brand": "Elégance (エレガンス)", "name": "モデリング カラーアップ ベース UV (肌色補正×毛穴フラット・高密着ベース)"},
            {"rank": 5, "query": "ラロッシュポゼ トーンアップ ローズ 30ml", "brand": "La Roche-Posay (ラ ロッシュ ポゼ)", "name": "UVイデア XL プロテクショントーンアップ ローズ (敏感肌用・自然な血色感UV)"},
            {"rank": 6, "query": "ウォンジョンヨ トーンアップベース 01", "brand": "Wonjungyo (ウォンジョンヨ)", "name": "トーンアップベース NA (アイドル級の透明感・高密着トーンアップ)"},
            {"rank": 7, "query": "RMK ルミナス メイクアップベース 30ml", "brand": "RMK (アールエムケー)", "name": "ルミナス メイクアップベース (シアバター＆シルクエッセンス・光沢膜プライマー)"},
            {"rank": 8, "query": "クレ・ド・ポー ボーテ ヴォワールコレクチュールn", "brand": "Clé de Peau Beauté", "name": "ヴォワールコレクチュールn (至高の補正力・長時間うるおい持続ラグジュアリー下地)"},
            {"rank": 9, "query": "ナチュラグラッセ カラーコントロール ベース 01", "brand": "naturaglace (ナチュラグラッセ)", "name": "カラーコントロール ベース (100%天然由来・肌色補正バイオレット)"},
            {"rank": 10, "query": "エトヴォス ミネラルインナートリートメントベース", "brand": "ETVOS (エトヴォス)", "name": "ミネラルインナートリートメントベース (ヒト型セラミド×植物オイル・まるで美容液下地)"}
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
                        "review_average": raw_item.get("reviewAverage", 0.0),
                        "item_caption": raw_item.get("itemCaption", "")[:120],
                        "shop_name": raw_item.get("shopName", "")
                    }
                else:
                    print(f"  [Attempt {attempt+1}] No items found for query: {query}")
        except Exception as e:
            print(f"  [Attempt {attempt+1}] Error querying {query}: {e}")
        time.sleep(1.2)
    
    raise ValueError(f"Failed to fetch item for: {query}")

def main():
    result = {}
    print("=== 楽天APIリアルタイムデータ取得開始（新3特集・計30アイテム） ===")
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n--- カテゴリ取得中: {cat_data['title']} ---")
        items_res = []
        for q_info in cat_data["items"]:
            print(f"  取得中 Rank {q_info['rank']}: {q_info['name']} ...")
            item_data = fetch_item_with_retry(q_info)
            print(f"    -> 取得成功: {item_data['item_name'][:30]}... 価格: ¥{item_data['price']:,} (画像: {bool(item_data['image_url'])})")
            items_res.append(item_data)
            time.sleep(0.8)
        result[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": items_res
        }
    
    with open("rakuten_stick_scalp_toneup_data.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("\n全30アイテムの楽天APIデータ取得が完了し、'rakuten_stick_scalp_toneup_data.json' に保存しました。")

if __name__ == "__main__":
    main()
