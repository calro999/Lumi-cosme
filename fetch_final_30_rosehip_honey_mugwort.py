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
    "winter_rosehip_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！ビタミンの爆弾と濃密オメガ脂肪酸で冬枯れ肌をふっくら満たす高保湿ローズヒップオイルランク10",
        "file": "winter-rosehip-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["トリロジー ローズヒップ オイル 20ml", "トリロジー ローズヒップオイル"],
                "brand": "Trilogy (トリロジー)",
                "name": "オーガニック認定 ローズヒップ オイル 20ml (世界最高峰ピュアオイル・必須脂肪酸80%以上含有の集中保湿美容オイル)"
            },
            {
                "rank": 2,
                "queries": ["トリロジー ロザピンプラス 30ml", "トリロジー ロザピン プラス"],
                "brand": "Trilogy (トリロジー)",
                "name": "ロザピンプラス 30ml (ローズヒップ×トマト種子×クランベリー高抗酸化プレミアム美容オイル)"
            },
            {
                "rank": 3,
                "queries": ["生活の木 ローズヒップオイル", "生活の木 有機ローズヒップ"],
                "brand": "生活の木 (Tree of Life)",
                "name": "有機ローズヒップオイル・バージン 25ml (未精製オーガニック低温圧搾・冬のゴワつき肌をほぐす純植物性オイル)"
            },
            {
                "rank": 4,
                "queries": ["SH ローズヒップオイル 未精製", "アンドエスエイチ ローズヒップオイル"],
                "brand": "&SH (アンドエスエイチ)",
                "name": "未精製オーガニック ローズヒップオイル 50ml (天然ビタミンC・E・オメガ3＆6凝縮・冬の集中ナイトリペア)"
            },
            {
                "rank": 5,
                "queries": ["ローズヒップオイル 未精製 オーガニック", "マンデイムーン ローズヒップオイル"],
                "brand": "monday moon (マンデイムーン)",
                "name": "未精製オーガニック ローズヒップオイル 50ml (エコサート認証原料・角層深部のインナードライを潤す原液美容オイル)"
            },
            {
                "rank": 6,
                "queries": ["クナイプ ビオ オイル ローズ", "クナイプ クナイプビオ オイル ローズ"],
                "brand": "Kneipp (クナイプ)",
                "name": "クナイプビオ オイル ローズ 100ml (天然ローズヒップオイル配合・フェイス＆ボディのキメを整える濃密高保湿オイル)"
            },
            {
                "rank": 7,
                "queries": ["ローズヒップオイル 100ml キャリアオイル", "ローズヒップオイル 100ml"],
                "brand": "自然化粧品研究所 / マカダミ屋",
                "name": "ピュア ローズヒップオイル 100ml (低温圧搾コールドプレス・顔からデコルテ全身の乾燥小ジワを包み込む大容量オイル)"
            },
            {
                "rank": 8,
                "queries": ["トリロジー ローズヒップ オイル 45ml", "トリロジー ローズヒップ 45ml"],
                "brand": "Trilogy (トリロジー)",
                "name": "ローズヒップオイル ラージサイズ 45ml (毎日たっぷり使える大容量・角層バリア再構築ブースター)"
            },
            {
                "rank": 9,
                "queries": ["ローズヒップ オイル 美容オイル オーガニック", "ローズヒップオイル スキンケア"],
                "brand": "Natural Beauty Selection",
                "name": "オーガニックピュア ローズヒップオイル 30ml (遮光ボトル採用・熱をかけず生搾りした高活性トコフェロール処方)"
            },
            {
                "rank": 10,
                "queries": ["ローズヒップ 10ml キャリアオイル", "ローズヒップオイル お試し"],
                "brand": "インセント / NAGOMI AROMA",
                "name": "ピュア ローズヒップオイル 10ml〜 (目元・口元の乾燥ピンポイント集中リペア・ポーチ常備用)"
            }
        ]
    },
    "winter_honey": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然の強力吸湿ヴェールと濃厚生ハニーで乾かないモチ肌を叶える高保湿ハチミツコスメランク10",
        "file": "winter-honey.html",
        "items": [
            {
                "rank": 1,
                "queries": ["HACCI フェイスオイル エスケーピオン", "HACCI オイル"],
                "brand": "HACCI (ハッチ)",
                "name": "フェイスオイル エスケーピオン 30ml (厳選天然ハチミツ×高機能ボタニカルオイル・驚異の浸透と黄金のツヤをもたらす最高峰プレオイル)"
            },
            {
                "rank": 2,
                "queries": ["COSRX プロポリス シナジートナー", "COSRX プロポリス 化粧水"],
                "brand": "COSRX (コスアールエックス)",
                "name": "フルフィット プロポリス シナジートナー 150ml (黒蜂プロポリスエキス72.6%×蜂蜜エキス10%配合・吸い付く高保湿水光肌トナー)"
            },
            {
                "rank": 3,
                "queries": ["山田養蜂場 ハニーラボ", "ハニーラボ パック"],
                "brand": "山田養蜂場 (YAMADA BEE FARM)",
                "name": "ハニーラボ スリーピングパック 50ml (完熟ハチミツ×カミツレ花エキス・寝ている間に角層を満たす濃密夜用パック)"
            },
            {
                "rank": 4,
                "queries": ["HACCI クレンジングミルク", "HACCI クレンジング"],
                "brand": "HACCI (ハッチ)",
                "name": "クレンジングミルク 190ml (贅沢はちみつ85%以上美容液成分・乾燥肌をいたわりながらメイクオフする高保湿ミルク)"
            },
            {
                "rank": 5,
                "queries": ["SKINFOOD ロイヤルハニー プロポリス", "スキンフード ロイヤルハニー"],
                "brand": "SKINFOOD (スキンフード)",
                "name": "ロイヤルハニー プロポリス エンリッチ エッセンス 50ml (熟成プロポリス63%×熟成ハチミツ配合・冬の極度乾燥バリアアンプル)"
            },
            {
                "rank": 6,
                "queries": ["ベキュアハニー ワンダーハニー", "ベキュアハニー ハンドクリーム"],
                "brand": "VECUA Honey (ベキュア ハニー)",
                "name": "ワンダーハニー とろとろハンドクリーム 50g (北海道産アカシア蜂蜜×ミツロウ配合・ベタつかず潤いの手袋を張る高保湿ハンドクリーム)"
            },
            {
                "rank": 7,
                "queries": ["アンドハニー ヘアオイル ディープモイスト", "&honey ディープモイスト"],
                "brand": "&honey (アンドハニー)",
                "name": "ディープモイスト ヘアオイル3.0 100ml (水分量14%に着目・マヌカハニー×生ハチミツ配合の超高保湿濃密ヘアオイル)"
            },
            {
                "rank": 8,
                "queries": ["カントリー＆ストリーム ハチミツ", "カントリー＆ストリーム リップクリーム"],
                "brand": "カントリー＆ストリーム (Country & Stream)",
                "name": "ナチュラル ハニーリップ 10g (ハチミツ×ローヤルゼリーエキス・冬のひび割れ唇をぷるぷるに保つ濃密密着ハニーリップ)"
            },
            {
                "rank": 9,
                "queries": ["山田養蜂場 RJ エッセンス ローヤルゼリー", "山田養蜂場 RJ エッセンス"],
                "brand": "山田養蜂場 (YAMADA BEE FARM)",
                "name": "薬用 RJエッセンス 30ml (美白＆抗シワ有効成分×高濃度デセン酸含有ローヤルゼリー・冬枯れ肌を蘇らせる薬用美容液)"
            },
            {
                "rank": 10,
                "queries": ["マヌカハニー コスメ クリーム", "マヌカコスメ リッチモイスト", "マヌカハニー 保湿クリーム"],
                "brand": "マヌカコスメ (MANUKA COSME)",
                "name": "マヌカコスメ B8 リッチモイストドロップ 80g (ニュージーランド産UMF15+マヌカハニー配合・冬の乾燥荒れを防ぐオールインワン高保水ドロップ)"
            }
        ]
    },
    "winter_mugwort": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の冷え・寒暖差による赤みと乾燥ゴワつきを鎮める高保水ヨモギ（マグワート）コスメランク10",
        "file": "winter-mugwort.html",
        "items": [
            {
                "rank": 1,
                "queries": ["I'm From マグワート エッセンス", "アイムフロム マグワート エッセンス", "マグワート エッセンス"],
                "brand": "I'm from (アイムフロム)",
                "name": "マグワート エッセンス 160ml (韓国江華島産カワラヨモギエキス100%・寒暖差で赤くほてる乾燥肌を瞬時に落ち着かせる導入化粧水)"
            },
            {
                "rank": 2,
                "queries": ["I'm From マグワート マスク", "アイムフロム マグワート マスク", "マグワート マスク"],
                "brand": "I'm from (アイムフロム)",
                "name": "マグワート マスク 110g (生ヨモギ葉粉末2.1%高配合・角質のキメを整え冷え固まった肌をほぐす高保水ウォッシュオフパック)"
            },
            {
                "rank": 3,
                "queries": ["MISSHA アルテミシア トリートメント エッセンス", "ミシャ アルテミシア エッセンス"],
                "brand": "MISSHA (ミシャ)",
                "name": "タイムレボリューション アルテミシア トリートメント エッセンス 150ml (伝統の甕で2回自然発酵・冬のインナードライを鎮める発酵ヨモギ100%原液)"
            },
            {
                "rank": 4,
                "queries": ["ブリンググリーン カワラヨモギ", "ブリンググリーン ヨモギ"],
                "brand": "BRING GREEN (ブリンググリーン)",
                "name": "カワラヨモギ カーミング リペア クリーム 75ml (カワラヨモギエキス54%×5種のヒアルロン酸・冬の乾燥バリアを修復する水分鎮静クリーム)"
            },
            {
                "rank": 5,
                "queries": ["カワラヨモギ エキス 原液", "カワラヨモギ 原液"],
                "brand": "自然化粧品研究所",
                "name": "カワラヨモギエキス 20ml 美容原液 (無添加植物エキス100%・冬のマスク荒れや乾燥による赤みトラブルを整える集中ケア原液)"
            },
            {
                "rank": 6,
                "queries": ["ドクタージー レッドブレミッシュ クリーム", "Dr.G レッドブレミッシュ"],
                "brand": "Dr.G (ドクタージー)",
                "name": "レッドブレミッシュ クリアスージングクリーム 70ml (10-CICA×植物性スージング成分配合・冬のほてり赤みと乾燥を同時に防ぐ低刺激水分クリーム)"
            },
            {
                "rank": 7,
                "queries": ["メディヒール ティーツリー パッド", "MEDIHEAL ティーツリー パッド"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "ティーツリー カーミング トナーパッド 100枚入 (ティーツリー×ヨモギ鎮静エッセンスたっぷり・朝のメイク前の急速部分水分パック)"
            },
            {
                "rank": 8,
                "queries": ["Anua ドクダミ 77 トナー", "アヌア ドクダミ 77"],
                "brand": "Anua (アヌア)",
                "name": "ドクダミ77 スージングトナー 250ml (ドクダミ77%×植物性鎮静複合体・冬の冷えによる毛穴詰まりと赤みを清らかに潤す高保水化粧水)"
            },
            {
                "rank": 9,
                "queries": ["よもぎ 入浴剤 オーガニック", "よもぎ 入浴剤"],
                "brand": "ほんまもんのよもぎ / 吉野よもぎ",
                "name": "あったか よもぎ風呂 10袋入 (国産無農薬ヨモギ100%・冬の冷えた身体の芯から温めて全身の乾燥肌荒れを潤す薬草入浴剤)"
            },
            {
                "rank": 10,
                "queries": ["カワラヨモギ 化粧水", "ヨモギ フェイスマスク", "よもぎ 化粧水"],
                "brand": "アルテ (Arte) / 和漢植物",
                "name": "国産カワラヨモギ ハーバルモイスチャーローション 150ml (伝統和漢ヨモギ蒸留水×植物エキス・寒風に負けない健やかな角層へ整える高保湿化粧水)"
            }
        ]
    }
}

def fetch_and_save():
    results = {}
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
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                for attempt in range(2):
                    try:
                        time.sleep(1.8) # レートリミット回避
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                if cand.get("itemPrice", 0) > 0 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(3.0)
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
            
            print(f"  ✅ SUCCESS Rank {item['rank']}: {price}円 | img:{bool(img_url)} | {raw_title[:40]}")
            results[cat_key]["items"].append({
                "rank": item["rank"],
                "name": item["name"],
                "brand": item["brand"],
                "price": price,
                "raw_title": raw_title,
                "affiliate_url": aff_url,
                "img_url": img_url
            })
            
    with open("fetched_final_30_rosehip_honey_mugwort.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_final_30_rosehip_honey_mugwort.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
