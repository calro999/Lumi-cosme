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
    "winter_liposome": {
        "title": "保湿力の強さで肌乾燥とさようなら！多重層カプセルが角層深くまで潤いを巡らせ続ける高保湿リポソームコスメランク10",
        "file": "winter-liposome.html",
        "items": [
            {
                "rank": 1,
                "queries": ["コスメデコルテ リポソーム アドバンスト リペアセラム"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアセラム 50ml / 75ml (1滴に1兆個の多重層バイオリポソーム・角層深層へ持続潤いを届ける最高峰ブースター)"
            },
            {
                "rank": 2,
                "queries": ["コスメデコルテ リポソーム アドバンスト リペアクリーム"],
                "brand": "DECORTÉ (コスメデコルテ)",
                "name": "リポソーム アドバンスト リペアクリーム 50g (ナイト多重層バイオリポソーム配合・睡眠中の肌を濃密カプセルで包み込むリペアクリーム)"
            },
            {
                "rank": 3,
                "queries": ["カネボウ フュージョニング ソリューション"],
                "brand": "KANEBO (カネボウ)",
                "name": "フュージョニング ソリューション 60ml (高浸透ナノ微細乳化リポソーム処方・冬の肌キメとツヤを瞬時に引き上げる新生美容液)"
            },
            {
                "rank": 4,
                "queries": ["VT リードルショット リポソーム", "VT リードルショット 100"],
                "brand": "VT COSMETICS (ブイティー)",
                "name": "マイルド リードルショット 50 / 100 50ml (シカニードル×リポソームカプセル処方・角層奥まで美容成分を届ける導入美容液)"
            },
            {
                "rank": 5,
                "queries": ["エトヴォス モイスチャライジングセラム"],
                "brand": "ETVOS (エトヴォス)",
                "name": "モイスチャライジングセラム 50ml (5種のヒト型セラミドをリポソーム化配合・乾燥した冬の角層バリアを再建する高保水美容液)"
            },
            {
                "rank": 6,
                "queries": ["魔女工場 ビフィダ バイオーム コンプレックス アンプル"],
                "brand": "魔女工場 (Manyo Factory)",
                "name": "ビフィダ バイオーム コンプレックス アンプル 50ml (微粒子リポソーム乳酸菌×ヒアルロン酸10種・真冬の揺らぐ肌基礎体力を底上げする集中アンプル)"
            },
            {
                "rank": 7,
                "queries": ["イニスフリー グリーンティーシード セラム"],
                "brand": "innisfree (イニスフリー)",
                "name": "グリーンティーシード ヒアルロン セラム 80ml (ナノカプセル化ヒアルロン酸×緑茶乳酸菌・角層深層へ素早く水分を補給する高保水セラム)"
            },
            {
                "rank": 8,
                "queries": ["ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX"],
                "brand": "DR.CI:LABO (ドクターシーラボ)",
                "name": "アクアコラーゲンゲル エンリッチリフトEX 120g (浸透型リポソームコラーゲン配合・真冬の乾燥たるみをパンッと引き締める濃厚ゲル)"
            },
            {
                "rank": 9,
                "queries": ["ヒアテノール アンプル", "ネイチャーリパブリック ヒアテノール"],
                "brand": "NATURE REPUBLIC (ネイチャーリパブリック)",
                "name": "ヒアテノール ハイドラ アンプル 30ml (植物性ナノリポソームヒアルロン酸×パンテノール・乾いた角層を速攻オアシス化する水分アンプル)"
            },
            {
                "rank": 10,
                "queries": ["菊正宗 日本酒の美容液"],
                "brand": "菊正宗酒造",
                "name": "日本酒の美容液 150ml (コメ発酵液×高純度アミノ酸ナノリポソーム配合・真冬の乾燥肌にしっとり吸い付くうるおいを与えるプチプラ名品)"
            }
        ]
    },
    "winter_coenzyme_q10": {
        "title": "保湿力の強さで肌乾燥とさようなら！寒さで活力を失った冬枯れ肌に濃密なハリと弾力を満たす高濃度コエンザイムQ10コスメランク10",
        "file": "winter-coenzyme-q10.html",
        "items": [
            {
                "rank": 1,
                "queries": ["DHC 薬用Qクイックジェル モイスト＆ホワイトニング"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Qクイックジェル モイスト＆ホワイトニング 100g (高濃度コエンザイムQ10 0.3%×薬用美白・真冬のハリと美白を1個で叶えるオールインワン)"
            },
            {
                "rank": 2,
                "queries": ["Q10 クリーム"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Qフェーストクリーム 50g (コエンザイムQ10高濃度配合・真冬の冷えによる小ジワ・乾燥を濃厚リペアする高保湿クリーム)"
            },
            {
                "rank": 3,
                "queries": ["DHC 薬用Qローション"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Qローション 160ml (鮮やかな黄色は高濃度Q10の証・角層深くまで浸透し冬枯れ肌をみずみずしく満たす薬用化粧水)"
            },
            {
                "rank": 4,
                "queries": ["チューンメーカーズ コエンザイムQ10"],
                "brand": "TUNEMAKERS (チューンメーカーズ)",
                "name": "コエンザイムQ10 原液 10ml / 20ml (浸透型ナノカプセル化ユビキノン・冬の寒さでしぼんだ目元や口元に弾力と活力を集中チャージする原液)"
            },
            {
                "rank": 5,
                "queries": ["コエンリッチ ナイトリニュー ハンドクリーム", "コエンリッチ ナイトリニュー"],
                "brand": "KOSE (コーセー) コエンリッチ",
                "name": "ナイトリニュー ハンドセラム 80g (マイクロカプセル化コエンザイムQ10×ローヤルゼリー・就寝中に手肌を集中リペアする濃厚夜用ハンドクリーム)"
            },
            {
                "rank": 6,
                "queries": ["ニベア プレミアムボディミルク モイスチャー"],
                "brand": "NIVEA (ニベア花王)",
                "name": "プレミアムボディミルク モイスチャー 200g (コエンザイムQ10×プレミアムモイスト成分・粉吹きやすい真冬の全身をもっちり潤す高保湿ミルク)"
            },
            {
                "rank": 7,
                "queries": ["コエンリッチ 薬用ホワイトニング ハンドクリーム モイストジェル", "コエンリッチ 薬用ホワイトニング"],
                "brand": "KOSE (コーセー) コエンリッチ",
                "name": "薬用ホワイトニング ハンドクリーム ディープモイスチュア 80g (高純度コエンザイムQ10×ホホバオイル・冷たい水仕事や乾燥から手肌を死守する保護ヴェール)"
            },
            {
                "rank": 8,
                "queries": ["セザンヌ モイスチュアリッチ エッセンスローション"],
                "brand": "CEZANNE (セザンヌ)",
                "name": "モイスチュアリッチ エッセンスローション 160ml (コエンザイムQ10×2種のコラーゲン配合・プチプラながら冬の乾燥肌をとろりと潤す高保湿化粧水)"
            },
            {
                "rank": 9,
                "queries": ["コエンリッチ プレミアム"],
                "brand": "KOSE (コーセー) コエンリッチ",
                "name": "ザ プレミアム 薬用リンクルホワイト ハンドクリーム 60g (コエンザイムQ10×ナイアシンアミド配合・手肌のシワ改善とシミ予防を同時に叶えるプレミアムハンドケア)"
            },
            {
                "rank": 10,
                "queries": ["DHC ミルク"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用Q クイックジェル モイスト＆ホワイトニング L 100g (高純度コエンザイムQ10配合・冬の乾燥肌をしっとりモチモチに包み込む薬用ジェル)"
            }
        ]
    },
    "winter_astaxanthin": {
        "title": "保湿力の強さで肌乾燥とさようなら！赤の抗酸化力で冬の乾燥小ジワを跳ね返し濃密な潤いを満たす高保湿アスタキサンチンコスメランク10",
        "file": "winter-astaxanthin.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アスタリフト ジェリー アクアリスタ"],
                "brand": "ASTALIFT (アスタリフト) / 富士フイルム",
                "name": "ジェリー アクアリスタ 40g / 60g (ナノアスタキサンチン×Wヒト型ナノセラミド配合・洗顔後の素肌を満たす最高峰先行ジェリー美容液)"
            },
            {
                "rank": 2,
                "queries": ["アスタリフト クリーム アドバンスド", "アスタリフト アドバンスド クリーム", "アスタリフト クリーム"],
                "brand": "ASTALIFT (アスタリフト) / 富士フイルム",
                "name": "アドバンスド クリーム 30g (ナノアスタキサンチン×リコピン・真冬の過酷な乾燥を濃厚な潤いの膜で閉じ込める高機能リペアクリーム)"
            },
            {
                "rank": 3,
                "queries": ["アスタリフト モイストローション", "アスタリフト アドバンスドローション", "アスタリフト ローション"],
                "brand": "ASTALIFT (アスタリフト) / 富士フイルム",
                "name": "モイストローション 130ml (ナノアスタキサンチン×水溶性コラーゲン・乾燥でこわばった冬の角層をすみずみまで解きほぐす薬用高保湿化粧水)"
            },
            {
                "rank": 4,
                "queries": ["DHC アスタキサンチン オールインワンジェル", "DHC アスタキサンチン コラーゲン オールインワンジェル"],
                "brand": "DHC (ディーエイチシー)",
                "name": "アスタキサンチン コラーゲン オールインワンジェル 120g (高純度アスタキサンチン×加水分解エラスチン・冬の時短ケアでハリ艶を宿す濃厚ジェル)"
            },
            {
                "rank": 5,
                "queries": ["KISO アスタキサンチン", "キソ アスタキサンチン 原液"],
                "brand": "KISO (基礎化粧品研究所)",
                "name": "アスタキサンチン 原液 20ml (ヘマトコッカス藻由来天然アスタキサンチン100%・手持ちの化粧水やクリームに1滴混ぜて冬枯れ肌を蘇らせる原液)"
            },
            {
                "rank": 6,
                "queries": ["アスタキサンチン 美容液"],
                "brand": "Sungboon Editor (成分エディター)",
                "name": "アスタキサンチン カプセル 美容液 30ml (赤のアスタキサンチンカプセル×ナイアシンアミド・くすんだ冬肌に透明感とハリを満たす話題の韓国セラム)"
            },
            {
                "rank": 7,
                "queries": ["アスタリフト 美容液"],
                "brand": "ASTALIFT (アスタリフト) / 富士フイルム",
                "name": "ザ セラム マルチチューン 40ml (薬用多機能美容液・カフェイン×ナノアスタキサンチン配合で冬の乾燥くすみとハリ不足を瞬時にケア)"
            },
            {
                "rank": 8,
                "queries": ["アスタブラン Wリフト エマルジョン", "アスタブラン エマルジョン", "コーセー アスタブラン"],
                "brand": "KOSE (コーセー) アスタブラン",
                "name": "Wリフト エマルジョン とてもしっとり 100ml (進化型アスタキサンチンCPX配合・真冬の乾いた角層を濃厚な油分と水分で満たす薬用高保湿乳液)"
            },
            {
                "rank": 9,
                "queries": ["アスタキサンチン クリーム"],
                "brand": "自然派高保湿スキンケア",
                "name": "アスタキサンチン リッチ オールインワンジェル 100g (天然ヘマトコッカス抽出アスタキサンチン×レチノール誘導体・冬の目元口元をピンと保つ濃密ジェル)"
            },
            {
                "rank": 10,
                "queries": ["ピュアエクセレントG エッセンスミルク", "明色 ピュアエクセレントG"],
                "brand": "明色化粧品",
                "name": "ピュアエクセレントG エッセンスミルク 100ml (天然アスタキサンチン×レチノール誘導体配合・冬の乾燥小ジワを目立たなくする高保湿乳液)"
            }
        ]
    }
}

def fetch_and_save():
    results = {}
    total_needed = sum(len(c["items"]) for c in CATEGORIES.values())
    total_success = 0
    
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==================== Verifying {cat_key} ====================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Trying Rank {item['rank']}: '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                for attempt in range(2):
                    try:
                        time.sleep(1.3)
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(1.8)
                if chosen_item:
                    break
            
            if not chosen_item:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}!")
                continue
            
            img_url = ""
            if chosen_item.get("mediumImageUrls"):
                img_url = chosen_item["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
            elif chosen_item.get("smallImageUrls"):
                img_url = chosen_item["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
            
            price = chosen_item.get("itemPrice", 0)
            aff_url = chosen_item.get("affiliateUrl", "") or chosen_item.get("itemUrl", "")
            raw_title = chosen_item.get("itemName", item["name"])
            
            print(f"  ✅ SUCCESS Rank {item['rank']}: {price}円 | img:{bool(img_url)} | {raw_title[:35]}")
            results[cat_key]["items"].append({
                "rank": item["rank"],
                "name": item["name"],
                "brand": item["brand"],
                "price": price,
                "raw_title": raw_title,
                "affiliate_url": aff_url,
                "img_url": img_url
            })
            total_success += 1
            
    with open("fetched_final_30_liposome_coenzyme_astaxanthin.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {total_success}/{total_needed} items to fetched_final_30_liposome_coenzyme_astaxanthin.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
