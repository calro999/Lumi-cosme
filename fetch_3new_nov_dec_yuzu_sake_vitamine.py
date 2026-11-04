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
    "winter_yuzu_ceramide": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の乾いた肌バリアを植物性セラミドと爽やかな和の香りで包み込む高保湿ユズセラミドコスメランク10",
        "file": "winter-yuzu-ceramide.html",
        "items": [
            {
                "rank": 1,
                "queries": ["松山油脂 柚子 ボディローション"],
                "brand": "松山油脂 (Mマークシリーズ)",
                "name": "柚子（ゆず）ボディローション 300ml (天然精油×ユズ種子エキス配合・カサつく全身の角層へみずみずしい潤いとバリアを届ける冬の定番乳液)"
            },
            {
                "rank": 2,
                "queries": ["草花木果 透肌マスクジェル", "草花木果 ゆず マスクジェル"],
                "brand": "草花木果 (そうかもっか)",
                "name": "透肌マスクジェル エンリッチ 90g (高知県産ユズセラミド×八重桜酵母配合・真冬の乾燥毛穴とキメの乱れをふっくら整える美容液ジェル)"
            },
            {
                "rank": 3,
                "queries": ["よーじや ゆず ハンドクリーム"],
                "brand": "よーじや (YOJIYA)",
                "name": "まゆごもり はなほのか ゆず ハンドクリーム 30g / 100g (シルクエキス×天然ユズ果皮油・真冬の水仕事や乾燥から指先を守る高保湿ハンドクリーム)"
            },
            {
                "rank": 4,
                "queries": ["クナイプ バスソルト ユズ ジンジャー"],
                "brand": "Kneipp (クナイプ)",
                "name": "バスソルト ユズ＆ジンジャーの香り 850g (天然岩塩×ユズ精油・冷え切った冬の身体を芯から温め肌にしっとり潤いを与える薬用入浴料)"
            },
            {
                "rank": 5,
                "queries": ["菊正宗 正宗印 導入美容液"],
                "brand": "菊正宗酒造",
                "name": "正宗印 導入美容液 185ml (コメ発酵液×国産ユズセラミド配合・洗顔後の乾いた角層を柔らかく解きほぐす高浸透ブースター)"
            },
            {
                "rank": 6,
                "queries": ["松山油脂 肌をうるおす 保湿浸透水"],
                "brand": "松山油脂 (肌をうるおす保湿スキンケア)",
                "name": "保湿浸透水 モイストリッチ 120ml (5種のヒト型セラミド×大豆・ユズセラミド配合・真冬の超乾燥肌をとろり潤す高保湿化粧水)"
            },
            {
                "rank": 7,
                "queries": ["トコトワ ピュアエッセンスミスト"],
                "brand": "tokotowa organics (トコトワオーガニクス)",
                "name": "ピュアエッセンスミスト イエロー 200ml (高知県産オーガニックユズ果実水×植物オイル・日中のエアコン乾燥から肌を守る二層式ミスト)"
            },
            {
                "rank": 8,
                "queries": ["スキンフード ゆず", "スキンフード ゆずC"],
                "brand": "SKINFOOD (スキンフード)",
                "name": "ゆずC ダークスポット クリアエッセンス 50ml (韓国コフン産ゆずエキス×ビタミンC誘導体・冬の乾燥くすみを晴らしうるおい透明感を与える高保水美容液)"
            },
            {
                "rank": 9,
                "queries": ["松山油脂 柚子 リップクリーム"],
                "brand": "松山油脂 (Mマークシリーズ)",
                "name": "柚子（ゆず）リップクリーム 4g (カルナウバロウ×天然ユズ精油配合・真冬の冷風でひび割れやすい唇をしっとり保護する天然高密着リップ)"
            },
            {
                "rank": 10,
                "queries": ["ユズ フェイスマスク", "高知県産YUZU ジューシーフェイスマスク"],
                "brand": "デイリーアロマジャパン (DAILY AROMA JAPAN)",
                "name": "高知県産YUZU ジューシーフェイスマスク 1枚入 (国産ユズ果実水・精油高配合・真冬の乾燥でこわばった肌を解きほぐす集中アロマ高保湿シートマスク)"
            }
        ]
    },
    "winter_sake_kasu": {
        "title": "保湿力の強さで肌乾燥とさようなら！杜氏の手のようなもっちり透明美肌へ導くアミノ酸濃密補給の高保湿酒粕コスメランク10",
        "file": "winter-sake-kasu.html",
        "items": [
            {
                "rank": 1,
                "queries": ["ワフードメイド 酒粕パック"],
                "brand": "pdc (ピーディーシー) ワフードメイド",
                "name": "酒粕パック 170g (熊本県河津酒造の酒粕エキス配合・真冬のくすみと古い角質をやさしく落とし杜氏のようなもっちり白肌へ導くベストセラー洗い流しパック)"
            },
            {
                "rank": 2,
                "queries": ["ワフードメイド 酒粕マスク"],
                "brand": "pdc (ピーディーシー) ワフードメイド",
                "name": "酒粕マスク 10枚入 (酒粕エキス×米セラミド・極厚多層シートが真冬の乾燥砂漠肌に濃密な発酵アミノ酸を届けきる集中シートマスク)"
            },
            {
                "rank": 3,
                "queries": ["アズマ商事 酒粕洗顔フォーム", "酒粕 洗顔"],
                "brand": "アズマ商事 (旅美人)",
                "name": "酒粕洗顔フォーム 120g (純米酒粕エキス配合・温泉宿で愛され続ける超濃密もっちり泡で真冬の毛穴汚れとくすみを落とす高保湿洗顔)"
            },
            {
                "rank": 4,
                "queries": ["菊正宗 日本酒のクリーム"],
                "brand": "菊正宗酒造",
                "name": "日本酒のクリーム 150g (純米吟醸酒コメ発酵液×4種のセラミド×アミノ酸・真冬のこっくり濃厚ヴェールで顔も体もしっとり守る高保湿クリーム)"
            },
            {
                "rank": 5,
                "queries": ["ワフードメイド 酒粕化粧水"],
                "brand": "pdc (ピーディーシー) ワフードメイド",
                "name": "酒粕化粧水 190ml (振って使う二層式高保湿ローション・酒粕エキスの水分とコメ胚芽油のエモリエントが冬の乾いた角層を瞬時に柔らかく満たす)"
            },
            {
                "rank": 6,
                "queries": ["菊正宗 日本酒の化粧水 高保湿"],
                "brand": "菊正宗酒造",
                "name": "日本酒の化粧水 高保湿 500ml (純米吟醸酒のコメ発酵液×アミノ酸×アルブチン×セラミド・真冬の全身にバシャバシャ使える殿堂入り高保湿化粧水)"
            },
            {
                "rank": 7,
                "queries": ["白玉りっち", "酒粕 オールインワン"],
                "brand": "白玉りっち (酒粕コスメ)",
                "name": "白玉りっち 酒粕オールインワンクリーム 25g (酒粕エキス×コメ発酵液配合・忙しい冬の朝晩にこれひとつで白玉のようなツヤ肌へ導く高保湿ゲル)"
            },
            {
                "rank": 8,
                "queries": ["蔵元美人 白米発酵"],
                "brand": "外池酒造店 (蔵元美人)",
                "name": "白米発酵 しっとり化粧水 150ml (有機栽培米コメ発酵液×酒粕エキス×米ヌカ油・真冬の乾燥で硬くなった肌をやわらかく解きほぐす蔵元コスメ)"
            },
            {
                "rank": 9,
                "queries": ["ワフードメイド 酒粕クリーム"],
                "brand": "pdc (ピーディーシー) ワフードメイド",
                "name": "酒粕クリーム 55g (酒粕エキス×キュウリ果実エキス配合・パックしたてのようなうるおい膜が真冬の冷気から素肌を一日中守り抜く高保湿クリーム)"
            },
            {
                "rank": 10,
                "queries": ["菊正宗 ハンドクリーム 美容液", "菊正宗 ハンドクリーム"],
                "brand": "菊正宗酒造",
                "name": "正宗印 ハンドクリームセラム 70g (日本酒発酵アミノ酸×酒粕エキス×セラミド配合・真冬の水仕事やアルコール消毒で荒れた手肌を吸い付くように潤す美容液ハンドクリーム)"
            }
        ]
    },
    "winter_vitamin_e": {
        "title": "保湿力の強さで肌乾燥とさようなら！寒さで冷えた冬枯れ肌の巡りを高めてふっくら押し返すハリ艶を宿す高純度ビタミンE高保湿コスメランク10",
        "file": "winter-vitamin-e.html",
        "items": [
            {
                "rank": 1,
                "queries": ["クレアス ビタミンEマスク"],
                "brand": "Dear, Klairs (クレアス)",
                "name": "フレッシュリージュースド ビタミンEマスク 90g (高純度ビタミンE（トコフェロール）×ナイアシンアミド配合・寒冷で縮こまった冬枯れ肌をぷるんとした弾力で包み込む形状記憶スリーピングパック)"
            },
            {
                "rank": 2,
                "queries": ["ユースキン 120g ポンプ"],
                "brand": "ユースキン (yuskin)",
                "name": "ユースキン 120g ポンプ (指定医薬部外品・トコフェロール酢酸エステル×グリチルレチン酸配合・ひび・あかぎれ・しもやけを徹底リペアする真冬の国民的救世主)"
            },
            {
                "rank": 3,
                "queries": ["ザーネクリーム 100g"],
                "brand": "Eisai (エーザイ) ザーネ",
                "name": "ザーネクリーム 100g (医薬部外品・天然型ビタミンE×消炎成分配合・真冬のカサつく手肌や粉吹き脚をしっとり滑らかに整える薬用保湿クリーム)"
            },
            {
                "rank": 4,
                "queries": ["メラノCC プレミアム美容液"],
                "brand": "ROHTO (ロート製薬) メラノCC",
                "name": "薬用しみ集中対策 プレミアム美容液 20ml (活性型ビタミンC×トコフェロール酢酸エステル(ビタミンE誘導体)・冬の乾燥くすみと毛穴を濃密な一滴で満たす薬用セラム)"
            },
            {
                "rank": 5,
                "queries": ["ビタミンEオイル 50ml", "ビタミンE オイル スキンケア"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "100%ナチュラル ビタミンEオイル 50ml (天然トコフェロール高濃度・冬の乾燥目元や小ジワ・超乾燥部位に1滴溶け込ませる純度100%リッチオイル)"
            },
            {
                "rank": 6,
                "queries": ["シナジアSCエッセンスEX", "トコフェロール 美容液", "ビタミンE 美容液"],
                "brand": "シナジア (SYNERGIA)",
                "name": "SCエッセンスEX 10ml (トリプルビタミン×高濃度トコフェロール配合・寒暖差で揺らぐ冬肌のキメとバリア機能を速攻チャージする高機能アンプル)"
            },
            {
                "rank": 7,
                "queries": ["オバジX ダーマアドバンスドリフト"],
                "brand": "Obagi (オバジ) / ロート製薬",
                "name": "オバジX ダーマアドバンスドリフト 50g (エラスプロ×トコフェロール配合・真冬の寒冷で重力に負けそうなしぼみ肌をピンと引き上げる高機能リフトクリーム)"
            },
            {
                "rank": 8,
                "queries": ["エトヴォス バイタライジングローション"],
                "brand": "ETVOS (エトヴォス)",
                "name": "バイタライジングローション 120ml (アルガン幹細胞エキス×ビタミンE誘導体×ヒト型セラミド5種・冬のハリ不足と乾燥年齢肌をみずみずしく満たす濃密化粧水)"
            },
            {
                "rank": 9,
                "queries": ["サンホワイト シルキー Y-1"],
                "brand": "日興リカ (サンホワイト)",
                "name": "サンホワイト シルキー Y-1 80g (高純度白色ワセリン・ビタミンEや美容液の後に重ねて冬の冷風と乾燥を100%遮断するベタつかない最高峰保護ワセリン)"
            },
            {
                "rank": 10,
                "queries": ["アベンヌ コールドクリーム"],
                "brand": "Avene (アベンヌ)",
                "name": "コールドクリーム N 40g (ミツロウ×アベンヌ温泉水×トコフェロール配合・真冬のヨーロッパの極寒から生まれた肌のうるおいラップクリーム)"
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
                                if price >= 400 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} failed: {e}")
                        time.sleep(2)
                if chosen_item:
                    print(f"  ✓ Found product: {chosen_item['itemName'][:40]}... (¥{chosen_item['itemPrice']:,})")
                    break
            
            if chosen_item:
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if isinstance(img_url, dict):
                    img_url = img_url.get("imageUrl", "")
                
                # 画像を高解像度化
                if "_ex=128x128" in img_url:
                    img_url = img_url.replace("_ex=128x128", "_ex=500x500")
                elif "_ex=64x64" in img_url:
                    img_url = img_url.replace("_ex=64x64", "_ex=500x500")
                elif "_ex=300x300" in img_url:
                    img_url = img_url.replace("_ex=300x300", "_ex=500x500")

                item_info = {
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "rakuten_item_name": chosen_item.get("itemName", ""),
                    "price": chosen_item.get("itemPrice", 0),
                    "url": chosen_item.get("affiliateUrl", chosen_item.get("itemUrl", "")),
                    "image": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_rate": chosen_item.get("reviewAverage", "4.5"),
                    "shop_name": chosen_item.get("shopName", "楽天市場公式ショップ")
                }
                results[cat_key]["items"].append(item_info)
                total_success += 1
            else:
                print(f"  ❌ FAILED to find item for Rank {item['rank']}: {item['name']}")

    out_file = "fetched_3new_nov_dec_yuzu_sake_vitamine.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n==========================================")
    print(f"Fetch completed: {total_success} / {total_needed} items fetched successfully.")
    print(f"Saved to: {out_file}")
    print(f"==========================================")

if __name__ == "__main__":
    fetch_and_save()
