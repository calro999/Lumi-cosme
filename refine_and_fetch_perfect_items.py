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
    "winter_pdrn_serum": {
        "title": "保湿力の強さで冬枯れ肌・弾力低下とさようなら！サーモン注射発想の再生成分で内側から押し返すハリツヤ肌へ導く高保湿PDRN美容液ランク10",
        "page_file": "winter-pdrn-serum.html",
        "items": [
            {"rank": 1, "query": "VT PDRN エッセンス 100", "brand": "VT COSMETICS (ブイティー)", "name": "PDRN エッセンス 100 30ml (植物性高純度PDRN配合！冬の乾燥でしぼんだ肌に潤いと輝きをチャージするメガヒット美容液)"},
            {"rank": 2, "query": "リジュラン アンプル", "brand": "REJURAN (リジュラン)", "name": "ターンオーバーアンプル / デュアル エフェクト アンプル 30ml (本家サーモン注射発想のc-PDRNを高濃度配合！角層深部を集中補修し究極のハリ肌へ)"},
            {"rank": 3, "query": "Anua PDRNヒアルロン酸カプセル100 セラム", "brand": "Anua (アヌア)", "name": "PDRN ヒアルロン酸 カプセル 100 セラム 30ml (スマートカプセル技術でPDRNとヒアルロン酸が角層深部へ瞬時に浸透)"},
            {"rank": 4, "query": "Yunth 生PDRN美容液", "brand": "Yunth (ユンス)", "name": "生PDRN美容液 1ml×28包 (個包装のフレッシュな生PDRN×アスタキサンチン！冬の乾燥小ジワを集中トリートメント)"},
            {"rank": 5, "query": "センテリアン24 PDRN", "brand": "Centellian24 (センテリアン24)", "name": "360度ショット PDRN アクティブセラム 50ml (製薬会社品質のPDRN×TECAツボクサエキス！全方位から肌密度を引き締める)"},
            {"rank": 6, "query": "IOPE PDRN カフェイン", "brand": "IOPE (アイオペ)", "name": "PDRN カフェイン ショット 30ml (Bio-PDRN×カフェイン配合！冬のむくみ感とフェイスラインのゆるみをキュッと引き締める)"},
            {"rank": 7, "query": "ネイチャーリパブリック PDRN 美容液", "brand": "NATURE REPUBLIC (ネイチャーリパブリック)", "name": "コンボ PDRN アンプル 美容液 30ml (植物性PDRN×ナイアシンアミド高配合！冬のくすみと乾燥をクリアに晴らす)"},
            {"rank": 8, "query": "KISO PDRN 美容液", "brand": "KISO (キソ)", "name": "ミルトセラム RN PDRN 120,000ppm配合 美容液 30ml (超高濃度PDRN原液級アプローチ！原液コスメならではの濃密なハリ実感)"},
            {"rank": 9, "query": "イニスフリー レチノール PDRN", "brand": "innisfree (イニスフリー)", "name": "レチノール PDRN アドバンスド セラム 30ml (低刺激レチノール×サーモンPDRNの奇跡のハイブリッド！キメと弾力を同時格上げ)"},
            {"rank": 10, "query": "メディキューブ PDRN アンプル", "brand": "medicube (メディキューブ)", "name": "PDRN ピンク ペプチド アンプル 30ml (サーモンDNA由来PDRN×ペプチド配合！暖房による乾燥小ジワと弾力低下を徹底ケア)"}
        ]
    },
    "winter_collagen_mask": {
        "title": "保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10",
        "page_file": "winter-collagen-mask.html",
        "items": [
            {"rank": 1, "query": "バイオダンス バイオコラーゲン リアルディープマスク", "brand": "BIODANCE (バイオダンス)", "name": "バイオ コラーゲン リアル ディープ マスク (白から透明に変わる元祖ゲルマスク！一晩貼って寝るだけで翌朝驚きの水光陶器肌)"},
            {"rank": 2, "query": "メディキューブ コラーゲン ナイトラッピングマスク", "brand": "medicube (メディキューブ)", "name": "コラーゲン ナイト ラッピング マスク 75ml (塗って寝るだけで一晩中コラーゲン皮膜が密閉！暖房乾燥から肌を鉄壁ガード)"},
            {"rank": 3, "query": "PESTLO T3ベビーコラーゲングローマスク", "brand": "PESTLO (ペストロ)", "name": "T3 ベビー コラーゲン グロー マスク 70ml (赤ちゃんの肌に多いT3コラーゲン配合！塗って剥がすだけで極上の水光ヴェール)"},
            {"rank": 4, "query": "Abib コラーゲン ゲル マスク", "brand": "Abib (アビブ)", "name": "コラーゲン ゲル マスク セダム / イェリコ (シート自体が植物性コラーゲンエキスを固めたゲル！肌の凹凸に吸い付くように密着)"},
            {"rank": 5, "query": "VT シカコラーゲンマスク", "brand": "VT COSMETICS (ブイティー)", "name": "シカ コラーゲン マスク 30枚入 (CICAと低分子コラーゲンのWアプローチ！冬の毎日のスキンケアを贅沢に格上げ)"},
            {"rank": 6, "query": "クリアターン エッセンスマスク コラーゲン", "brand": "CLEAR TURN (クリアターン / コーセー)", "name": "エッセンスマスク コラーゲン 30回分 (高純度コラーゲン配合の国民的デイリーマスク！大容量で毎日たっぷり贅沢保湿)"},
            {"rank": 7, "query": "メディヒール コラーゲン エッセンシャル", "brand": "MEDIHEAL (メディヒール)", "name": "コラーゲン エッセンシャル マスク (加水分解コラーゲン配合！冬の乾燥で低下した弾力とキメを集中トリートメント)"},
            {"rank": 8, "query": "VT リードルショット ハイドロゲルマスク", "brand": "VT COSMETICS (ブイティー)", "name": "リードルショット 100 2ステップ ハイドロゲル マスク (CICA REEDLEと美容成分をゲルに凝縮！角層のすみずみまで浸透をブースト)"},
            {"rank": 9, "query": "バイオ コラーゲン リアルディープマスク", "brand": "DERMAFIRM (ダーマファーム)", "name": "バイオ コラーゲン リアル ハイドロゲル マスク (高分子コラーゲンを低分子化して角層奥深くまで浸透させる高密着ゲルシート)"},
            {"rank": 10, "query": "センテリアン24 マデカダーママスク", "brand": "Centellian24 (センテリアン24)", "name": "マデカ ダーマ マスク インテンシブ フォーミュラ (製薬会社品質のTECAツボクサエキス×コラーゲン配合！敏感肌もぷるぷるに満たす)"}
        ]
    },
    "winter_carbonic_shampoo": {
        "title": "保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10",
        "page_file": "winter-carbonic-shampoo.html",
        "items": [
            {"rank": 1, "query": "b.ris オーガニックスパークリングシャンプー", "brand": "b.ris (ビーリス)", "name": "オーガニックスパークリングシャンプー 200g (5,000ppmの高濃度炭酸泡×植物オイル！冬の頭皮を優しく洗い上げツヤ髪へ)"},
            {"rank": 2, "query": "ルメント スパークリングオイル クレンジング＆シャンプー", "brand": "Le ment (ルメント)", "name": "スパークリングオイル クレンジング＆シャンプー 200g (高濃度炭酸5,000ppm×高級レアオイル配合！冬の乾燥頭皮と毛先をしっとり潤す)"},
            {"rank": 3, "query": "ミルボン プラーミア クリアスパフォーム", "brand": "MILBON (ミルボン)", "name": "プラーミア クリアスパフォーム 170g (プロ仕様4,400ppmの微細炭酸泡！冬の寒さで固まった頭皮の皮脂汚れをスッキリ除去)"},
            {"rank": 4, "query": "スカルプD モーニング 炭酸", "brand": "スカルプD (アンファー)", "name": "モーニング 炭酸ジェット スカルプシャンプー (爽快な炭酸ジェット泡で頭皮の血行を促進！寝癖直しとスカルプケアを同時に叶える)"},
            {"rank": 5, "query": "ナプラ インプライム ソーダシャンプー", "brand": "napla (ナプラ)", "name": "インプライム ソーダシャンプー 200g (天然メントールと炭酸の力で頭皮をクリアに！サロン品質の炭酸クレンジング)"},
            {"rank": 6, "query": "東洋炭酸研究所 TANSANスカルプDRプロ", "brand": "東洋炭酸研究所", "name": "TANSAN スカルプ DR プロ 200g (高濃度炭酸泡が毛穴の奥まで届き頭皮環境を根本ケア！プロ仕様のスカルプフォーム)"},
            {"rank": 7, "query": "ナンバースリー ミュリアム 炭酸", "brand": "NUMBER THREE (ナンバースリー)", "name": "ミュリアム クリスタル スカルプ炭酸クレンジング 250g (炭酸泡と植物エキスで頭皮のベタつきやニオイ、乾燥フケを集中オフ)"},
            {"rank": 8, "query": "TOWAZ 炭酸泡シャンプー", "brand": "TOWAZ (トワズ)", "name": "炭酸泡シャンプー 200g (もっちもちの超濃密炭酸ホイップ！摩擦レスで頭皮を包み込み優しく保湿洗浄)"},
            {"rank": 9, "query": "アンビーク 炭酸シャンプー", "brand": "AMBiQUE (アンビーク)", "name": "炭酸スカルプシャンプー 泡×泥 (高濃度炭酸泡とミネラル泥が冬の乾燥フケ・毛穴汚れを吸着！ハリ・コシを与える)"},
            {"rank": 10, "query": "シーグレイ 炭酸泡シャンプー", "brand": "C gray (シーグレイ)", "name": "炭酸泡 スパークリングシャンプー (高濃度炭酸泡と保湿カラーケア成分配合！冬の乾燥頭皮とパサつく髪をツヤやかに保護)"}
        ]
    }
}

def fetch_item(query_info):
    raw_q = query_info["query"]
    url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(raw_q)}&hits=5&format=json&sort=standard"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
    with urllib.request.urlopen(req, context=ctx, timeout=10) as res:
        data = json.loads(res.read().decode('utf-8'))
        items = data.get("Items", [])
        if items:
            chosen = None
            for it in items:
                item_obj = it["Item"]
                if item_obj.get("itemPrice", 0) > 0 and item_obj.get("mediumImageUrls"):
                    chosen = item_obj
                    break
            if not chosen:
                chosen = items[0]["Item"]

            raw_img = ""
            if chosen.get("mediumImageUrls"):
                raw_img = chosen["mediumImageUrls"][0].get("imageUrl", "")
            
            high_res_img = raw_img
            if "thumbnail.image.rakuten.co.jp/@0_mall/" in high_res_img:
                high_res_img = high_res_img.replace("https://thumbnail.image.rakuten.co.jp/@0_mall/", "https://shop.r10s.jp/").split("?_ex=")[0]
            elif "?_ex=" in high_res_img:
                high_res_img = high_res_img.split("?_ex=")[0] + "?_ex=600x600"
            
            price = chosen.get("itemPrice", 0)
            aff_url = chosen.get("affiliateUrl", "")
            item_name = chosen.get("itemName", "")
            
            if price > 0 and high_res_img and aff_url:
                return {
                    "rank": query_info["rank"],
                    "brand": query_info["brand"],
                    "name": query_info["name"],
                    "matchedItemName": item_name,
                    "price": price,
                    "image": high_res_img,
                    "affiliateUrl": aff_url
                }
    raise ValueError(f"Could not find valid item for {raw_q}")

def main():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\nFetching perfect items for {cat_key}...")
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": []
        }
        for it in cat_data["items"]:
            success = False
            for attempt in range(5):
                try:
                    time.sleep(0.4)
                    fetched = fetch_item(it)
                    print(f"  ✓ Rank {it['rank']}: {it['brand']} -> {fetched['matchedItemName'][:40]} | ¥{fetched['price']:,}")
                    results[cat_key]["items"].append(fetched)
                    success = True
                    break
                except Exception as e:
                    print(f"    Retry {attempt+1} for {it['query']}: {e}")
                    time.sleep(1.2)
            if not success:
                raise RuntimeError(f"Failed to fetch {it['query']}")

    with open("fetched_perfect_3articles_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n🎉 ALL 30 ITEMS FETCHED PERFECTLY!")

if __name__ == "__main__":
    main()
