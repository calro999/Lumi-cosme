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
            {"rank": 2, "query": "リジュラン デュアル エフェクト アンプル 30ml", "brand": "REJURAN (リジュラン)", "name": "デュアル エフェクト アンプル 30ml (本家サーモン注射発想のc-PDRNを高濃度配合！角層深部を集中補修し究極のハリ肌へ)"},
            {"rank": 3, "query": "メディキューブ PDRN ピンク ペプチド アンプル", "brand": "medicube (メディキューブ)", "name": "PDRN ピンク ペプチド アンプル 30ml (サーモンDNA由来PDRN×ペプチド配合！暖房による乾燥小ジワと弾力低下を徹底ケア)"},
            {"rank": 4, "query": "Anua PDRN ヒアルロン酸 カプセル 100 セラム", "brand": "Anua (アヌア)", "name": "PDRN ヒアルロン酸 カプセル 100 セラム 30ml (スマートカプセル技術でPDRNとヒアルロン酸が角層深部へ瞬時に浸透)"},
            {"rank": 5, "query": "ダーマファーム ウルトラセラム PDRN", "brand": "DERMAFIRM (ダーマファーム)", "name": "ウルトラセラム PDRN 30ml (リポソーム化された高純度PDRNが冬の寒冷ダメージ肌を滑らかに整えるドクターズコスメ)"},
            {"rank": 6, "query": "IOPE PDRN カフェイン ショット", "brand": "IOPE (アイオペ)", "name": "PDRN カフェイン ショット 30ml (Bio-PDRN×カフェイン配合！冬のむくみ感とフェイスラインのゆるみをキュッと引き締める)"},
            {"rank": 7, "query": "ナンバーズイン 9番 濃密 PDRN エッセンス", "brand": "numbuzin (ナンバーズイン)", "name": "9番 秘密の濃密ハリツヤ アンプル (弾力ペプチドとPDRN様成分が乾燥でハリを失った大人の肌をもっちり満たす)"},
            {"rank": 8, "query": "BIOHEAL BOH プロバイオダーム 3D リフティング アンプル", "brand": "BIOHEAL BOH (バイオヒールボ)", "name": "プロバイオダーム 3D リフティング アンプル 30ml (タンタン美容液として大人気！マイクロバイオームとペプチドで密度の高い肌へ)"},
            {"rank": 9, "query": "ドクターエルシア スキン リペア セラム", "brand": "Dr.Althea (ドクターエルシア)", "name": "オアシス スキン リペア セラム (砂漠のように乾いた冬の素肌に素早く水分補給し、バリア機能をサポートする集中美容液)"},
            {"rank": 10, "query": "イニスフリー レチノール シカ リペア セラム", "brand": "innisfree (イニスフリー)", "name": "レチノール シカ リペア セラム 30ml (低刺激レチノール×シカ成分！冬のゴワつきやキメの乱れをつるんとなめらかに整える)"}
        ]
    },
    "winter_collagen_mask": {
        "title": "保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10",
        "page_file": "winter-collagen-mask.html",
        "items": [
            {"rank": 1, "query": "バイオダンス バイオコラーゲン リアルディープマスク", "brand": "BIODANCE (バイオダンス)", "name": "バイオ コラーゲン リアル ディープ マスク (白から透明に変わる元祖ゲルマスク！一晩貼って寝るだけで翌朝驚きの水光陶器肌)"},
            {"rank": 2, "query": "メディキューブ コラーゲン ナイト ラッピング マスク", "brand": "medicube (メディキューブ)", "name": "コラーゲン ナイト ラッピング マスク 75ml (塗って寝るだけで一晩中コラーゲン皮膜が密閉！暖房乾燥から肌を鉄壁ガード)"},
            {"rank": 3, "query": "ダーマファーム バイオコラーゲン マスク", "brand": "DERMAFIRM (ダーマファーム)", "name": "バイオ コラーゲン リアル ハイドロゲル マスク (高分子コラーゲンを低分子化して角層奥深くまで浸透させる高密着ゲルシート)"},
            {"rank": 4, "query": "センテリアン24 マデカ ダーマ リアル コラーゲン マスク", "brand": "Centellian24 (センテリアン24)", "name": "マデカ ダーマ リアル コラーゲン マスク (製薬会社品質のTECAツボクサエキス×コラーゲン配合！敏感肌もぷるぷるに満たす)"},
            {"rank": 5, "query": "Anua ナイト ラッピング マスク", "brand": "Anua (アヌア)", "name": "コラーゲン 70% ナイト ラッピング クリーム マスク (70%の高純度コラーゲン水配合！一晩中肌の水分蒸散を防ぎ翌朝もっちり)"},
            {"rank": 6, "query": "Abib コラーゲン ゲル マスク", "brand": "Abib (アビブ)", "name": "コラーゲン ゲル マスク セダム / イェリコ (シート自体が植物性コラーゲンエキスを固めたゲル！肌の凹凸に吸い付くように密着)"},
            {"rank": 7, "query": "VT リードルショット ハイドロゲル マスク", "brand": "VT COSMETICS (ブイティー)", "name": "リードルショット 100 ハイドロゲル マスク (CICA REEDLEと美容成分をゲルに凝縮！角層のすみずみまで浸透をブースト)"},
            {"rank": 8, "query": "ダルバ ホワイトトリュフ ナリシング ハイドロゲル マスク", "brand": "d'Alba (ダルバ)", "name": "ホワイトトリュフ ナリシング リペア ゲル マスク (イタリア産ホワイトトリュフエキス配合！リッチな栄養で冬のしぼみ肌を底上げ)"},
            {"rank": 9, "query": "メディヒール コラーゲン エッセンシャル マスク", "brand": "MEDIHEAL (メディヒール)", "name": "コラーゲン エッセンシャル マスク (加水分解コラーゲン配合！冬の乾燥で低下した弾力とキメを集中トリートメント)"},
            {"rank": 10, "query": "グーダル 青みかん ビタC ジェル マスク", "brand": "goodal (グーダル)", "name": "青みかん ビタC ハイドロゲル マスク (濃縮ビタミンCと水分がぷるぷるゲルからじわじわ放出！くすんだ冬肌に透明感をチャージ)"}
        ]
    },
    "winter_carbonic_shampoo": {
        "title": "保湿力の強さで冬の頭皮乾燥フケ・寒冷凝固とさようなら！高濃度マイクロ炭酸泡で毛穴汚れを浮かし血行を巡らせる高保湿炭酸シャンプーランク10",
        "page_file": "winter-carbonic-shampoo.html",
        "items": [
            {"rank": 1, "query": "b.ris ビーリス オーガニック スパークリング シャンプー 200g", "brand": "b.ris (ビーリス)", "name": "オーガニックスパークリングシャンプー 200g (5,000ppmの高濃度炭酸泡×植物オイル！冬の頭皮を優しく洗い上げツヤ髪へ)"},
            {"rank": 2, "query": "MELCE メルス スパークリング スパシャンプー", "brand": "MELCE (メルス)", "name": "スパークリング スパシャンプー 200g (高濃度炭酸×ミネラルクレイ×浸透補修カプセル！濃密もっちり泡でサロン帰りのうるツヤ髪)"},
            {"rank": 3, "query": "ルメント スパークリングオイル クレンジング＆シャンプー", "brand": "Le ment (ルメント)", "name": "スパークリングオイル クレンジング＆シャンプー 200g (高濃度炭酸5,000ppm×高級レアオイル配合！冬の乾燥頭皮と毛先をしっとり潤す)"},
            {"rank": 4, "query": "ミルボン プラーミア クリアスパフォーム 170g", "brand": "MILBON (ミルボン)", "name": "プラーミア クリアスパフォーム 170g (プロ仕様4,400ppmの微細炭酸泡！冬の寒さで固まった頭皮の皮脂汚れをスッキリ除去)"},
            {"rank": 5, "query": "クレイエンス クレイスパ 炭酸シャンプー", "brand": "clayence (クレイエンス)", "name": "クレイスパ 炭酸スパシャンプー 200g (炭酸泡とクレイの力で頭皮環境をリセット！冬の乾燥フケを防ぎ根元からふんわり立ち上げ)"},
            {"rank": 6, "query": "クレージュ スパークリング スパシャンプー 150g", "brand": "CLAYGE (クレージュ)", "name": "スパークリング スパシャンプー 150g (ナチュラルクレイ×高濃度炭酸泡！じんわり温冷感で頭皮のコリをほぐし地肌引き締め)"},
            {"rank": 7, "query": "ハニーチェ 炭酸泡シャンプー", "brand": "Honeyce (ハニーチェ)", "name": "クリーミーハニー 炭酸ホイップシャンプー (生ハチミツ配合の濃密炭酸ホイップ泡！冬のパサつく髪を潤いヴェールでコート)"},
            {"rank": 8, "query": "グログロス 炭酸 スカルプ シャンプー", "brand": "Glowgros (グログロス)", "name": "濃密炭酸 スカルプスパシャンプー (超微細マイクロバブルが頭皮の角質層まで浸透！血行を促しハリコシのある美髪へ)"},
            {"rank": 9, "query": "ドクターゼロ 炭酸スカルプシャンプー", "brand": "DR ZERO (ドクターゼロ)", "name": "リデニカル スカルプ リフレッシュ 炭酸シャンプー (育毛成分リデンシル配合！冬の頭皮環境を健やかに整える本格スカルプケア)"},
            {"rank": 10, "query": "エラスチン 炭酸スカルプシャンプー", "brand": "ELASTINE (エラスチン)", "name": "パフューム ピュアブリーズ 炭酸スパフォーム (優雅な香りと炭酸泡で至福のバスタイム！冬の乾燥頭皮をすっきり洗い上げる)"}
        ]
    }
}

def clean_query(q):
    words = [w for w in q.split() if len(w) >= 2]
    return " ".join(words)

def fetch_item_with_retry(query_info):
    raw_q = query_info["query"]
    query = clean_query(raw_q)
    
    # クエリのフォールバック候補
    fallbacks = [query]
    parts = query.split()
    if len(parts) >= 3:
        fallbacks.append(" ".join(parts[:3]))
    if len(parts) >= 2:
        fallbacks.append(" ".join(parts[:2]))
    if len(parts) >= 1:
        fallbacks.append(parts[0])

    for q_try in fallbacks:
        for attempt in range(4):
            try:
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q_try)}&hits=5&format=json&sort=standard"
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
                time.sleep(0.3)
            except Exception as e:
                print(f"Error fetching {q_try} (attempt {attempt+1}): {e}")
                time.sleep(0.5)

    raise ValueError(f"Could not fetch valid item for {raw_q}")

def main():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching for Category: {cat_key} ({cat_data['title'][:30]}...)")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "page_file": cat_data["page_file"],
            "items": []
        }
        for it in cat_data["items"]:
            print(f"Fetching Rank {it['rank']}: {it['brand']} - {it['name'][:35]}...")
            fetched = fetch_item_with_retry(it)
            print(f"  ✓ Found: {fetched['matchedItemName'][:40]} | ¥{fetched['price']:,} | Img: {fetched['image'][:50]}...")
            results[cat_key]["items"].append(fetched)
            time.sleep(0.3)

    out_file = "fetched_3nov_dec_pdrn_collagen_carbonic_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n🎉 Successfully fetched all items and saved to {out_file}!")

if __name__ == "__main__":
    main()
