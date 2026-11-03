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
    "winter_marula_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！アルガン超えの抗酸化力と極上浸透膜で砂漠肌を救う高保湿マルラオイルランク10",
        "file": "winter-marula-oil.html",
        "items": [
            {
                "rank": 1,
                "query": "ヴァーチェ マルラオイル 純度100％",
                "brand": "VIRCHE (ヴァーチェ)",
                "name": "マルラオイル 18ml (最高峰オーガニック未精製・エイジングケア高保湿ブースター美容オイル)"
            },
            {
                "rank": 2,
                "query": "The Ordinary 100 コールドプレス ヴァージン マルラ オイル",
                "brand": "The Ordinary (ジ オーディナリー)",
                "name": "100% コールドプレス ヴァージンマルラオイル 30ml (高純度低温圧搾・冬の乾燥ゴワつきをほぐす高保湿オイル)"
            },
            {
                "rank": 3,
                "query": "マルラオイル 未精製 オーガニック 50ml",
                "brand": "monday moon (マンデイムーン)",
                "name": "未精製オーガニック マルラオイル 50ml (低温圧搾コールドプレス・年齢肌の水分蒸発を防ぐ原液オイル)"
            },
            {
                "rank": 4,
                "query": "オーガニック マルラオイル 100ml 美容オイル 未精製",
                "brand": "マカダミ屋 (Macadamiya)",
                "name": "100%ピュア 未精製オーガニックマルラオイル 100ml (高純度オレイン酸・リノール酸配合・全身使える高保湿キャリアオイル)"
            },
            {
                "rank": 5,
                "query": "マルラオイル 未精製 100% キャリアオイル 10ml",
                "brand": "自然化粧品研究所",
                "name": "未精製マルラオイル 10ml〜 (植物性ピュア100%・目元や口元の乾燥小ジワ集中ケア携帯オイル)"
            },
            {
                "rank": 6,
                "query": "オーガニック マルラオイル 美容オイル 無添加 100% キャリアオイル 20mL",
                "brand": "アロマ ルイボス naturalshop",
                "name": "オーガニック未精製マルラオイル 20ml (コールドプレス製法・冬の粉吹き・肌荒れを防ぐ高浸透美容オイル)"
            },
            {
                "rank": 7,
                "query": "マルラオイル 50ml 無添加 100% オーガニック 未精製",
                "brand": "ナチュラルマルラ (Natural Marula)",
                "name": "オーガニック未精製マルラオイル 50ml (抗酸化オメガ脂肪酸凝縮・真冬のインナードライ対策ブースター)"
            },
            {
                "rank": 8,
                "query": "SH マルラオイル 未精製 キャリアオイル",
                "brand": "アンドエスエイチ (&SH)",
                "name": "マルラオイル 80ml 未精製 (ボタニカル高保湿・髪・頭皮・顔・ボディマルチ美容オイル)"
            },
            {
                "rank": 9,
                "query": "マルラオイル 未精製 100ml IST",
                "brand": "IST (アイエスティ)",
                "name": "ピュアマルラオイル 未精製 100ml (南アフリカ産・高純度未精製キャリアオイル)"
            },
            {
                "rank": 10,
                "query": "ヴァーチェ ブライトニングローション",
                "brand": "VIRCHE (ヴァーチェ)",
                "name": "ブライトニングローション 150ml (マルラオイル×持続型ビタミンC誘導体配合・くすみと乾燥を払う高保湿化粧水)"
            }
        ]
    },
    "winter_birch_juice": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然ミネラルの潤い巡る白樺樹液で乾かない水光肌へ導く高保水バーチコスメランク10",
        "file": "winter-birch-juice.html",
        "items": [
            {
                "rank": 1,
                "query": "ROUND LAB ラウンドラボ シラカバ 水分クリーム 80ml",
                "brand": "ROUND LAB (ラウンドラボ)",
                "name": "シラカバ水分クリーム 80ml (江原道インジェ産白樺樹液×ビタヒアルロン酸配合・韓国オリーブヤング殿堂水分クリーム)"
            },
            {
                "rank": 2,
                "query": "Anua シラカバ 70 水分 ブースティング セラム",
                "brand": "Anua (アヌア)",
                "name": "シラカバ70 水分ブースティングセラム 30ml (白樺樹液70%配合・角層深くまで水分を届ける高浸透保水セラム)"
            },
            {
                "rank": 3,
                "query": "ROUND LAB ラウンドラップ シラカバ 水分アンプル 50ml",
                "brand": "ROUND LAB (ラウンドラボ)",
                "name": "シラカバ水分アンプル美容液 50ml (濃縮白樺樹液配合・インナードライの隙間を埋める水分爆弾美容液)"
            },
            {
                "rank": 4,
                "query": "Anua シラカバ70水分ブースティングクリーム 50ml",
                "brand": "Anua (アヌア)",
                "name": "シラカバ70 水分ブースティングクリーム 50ml (白樺樹液×パンテノール配合・潤いシールド水分ジェルクリーム)"
            },
            {
                "rank": 5,
                "query": "ROUND LAB シラカバ水分サンクリーム 50ml",
                "brand": "ROUND LAB (ラウンドラボ)",
                "name": "シラカバ水分日焼け止め 50ml (白樺樹液エッセンス高配合・冬の乾燥下地にもなるしっとり水分サンクリーム)"
            },
            {
                "rank": 6,
                "query": "Anua シラカバ水分ブースティングパッド 70枚",
                "brand": "Anua (アヌア)",
                "name": "シラカバ水分ブースティングパッド 70枚 (白樺樹液たっぷり浸透・冬の朝のメイク前3分集中水分チャージトナーパッド)"
            },
            {
                "rank": 7,
                "query": "ROUND LAB シラカバ 水分 クレンザー 150ml",
                "brand": "ROUND LAB (ラウンドラボ)",
                "name": "シラカバ水分クレンザー 150ml (白樺樹液弱酸性処方・冬のつっぱりを防ぐうるおい水分洗顔料)"
            },
            {
                "rank": 8,
                "query": "Anua シラカバ モイスチャーマスクパック 10枚",
                "brand": "Anua (アヌア)",
                "name": "シラカバ モイスチャーマスクパック 10枚入 (白樺樹液濃縮エッセンス密着シート・真冬の緊急保水レスキューマスク)"
            },
            {
                "rank": 9,
                "query": "白樺 樹液 化粧水 KOIVE モイスチャライジングトナー",
                "brand": "KOIVE (コイヴ)",
                "name": "モイスチャライジングトナー 150ml (天然白樺樹液をベースにした超濃密ミネラル高保湿化粧水)"
            },
            {
                "rank": 10,
                "query": "ROUND LAB シラカバ 水分 トナー 300ml",
                "brand": "ROUND LAB (ラウンドラボ)",
                "name": "シラカバ水分トナー 300ml (白樺樹液×ヒアルロン酸配合・弱酸性高浸透水分化粧水)"
            }
        ]
    },
    "winter_azelaic_acid": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬のインナードライ赤みと乾燥毛穴を鎮めて潤す高濃度アゼライン酸コスメランク10",
        "file": "winter-azelaic-acid.html",
        "items": [
            {
                "rank": 1,
                "query": "KISO CARE バランシングクリームAZ 20g アゼライン酸",
                "brand": "KISO (キソ)",
                "name": "キソ バランシングクリーム AZ 20g (高純度アゼライン酸20%配合・皮脂バランスと角層バリアを整える高保湿クリーム)"
            },
            {
                "rank": 2,
                "query": "dr365 セラムショット アゼライン酸",
                "brand": "dr365 (ドクターサンロクゴ)",
                "name": "A.Z. セラムショット 30ml (高純度アゼライン酸×ビタミンC誘導体配合・毛穴キメ集中ドクターズ美容液)"
            },
            {
                "rank": 3,
                "query": "Anua アゼライン酸インテンスカーミングセラム",
                "brand": "Anua (アヌア)",
                "name": "アゼライン酸インテンスカーミングセラム 30ml (アゼライン酸×CICAツボクサ配合・寒暖差赤みとテカリを鎮める美容液)"
            },
            {
                "rank": 4,
                "query": "旭研究所 業務用アゼライン酸液20％ 30mL",
                "brand": "旭研究所 (Asahi Laboratories)",
                "name": "業務用アゼライン酸液20％ 30ml (皮膚科学発想・高濃度アゼライン酸原液配合スポット集中美容液)"
            },
            {
                "rank": 5,
                "query": "マキアレイベル ディーププラスAZ 高濃度美容液",
                "brand": "Macchia Label (マキアレイベル)",
                "name": "ディーププラスAZ 30ml (高純度アゼライン酸×浸透型保湿成分配合・大人の乾燥毛穴レスキュー美容液)"
            },
            {
                "rank": 6,
                "query": "cosdebaha AZアゼライン酸15%美容液",
                "brand": "Cos De BAHA (コスデバハ)",
                "name": "AZ アゼライン酸15%セラム 30ml (高濃度アゼライン酸15%×ナイアシンアミド×ヒアルロン酸高保湿処方)"
            },
            {
                "rank": 7,
                "query": "トゥヴェール グリシルグリシン アゼライン酸誘導体 バランシングGAローション",
                "brand": "TOUT VERT (トゥヴェール)",
                "name": "バランシングGAローション 100ml (アゼライン酸誘導体原液×グリシルグリシン6%配合・キメ毛穴プレ化粧水)"
            },
            {
                "rank": 8,
                "query": "KISO バランシングエッセンス AZ アゼライン酸",
                "brand": "KISO (キソ)",
                "name": "バランシングエッセンス AZ 30ml (アゼライン酸誘導体原液配合・しっとり潤いながら皮脂崩れを防ぐ美容液)"
            },
            {
                "rank": 9,
                "query": "アゼライン酸 美容液 30ml アゼライン酸誘導体 15%",
                "brand": "DERMA SHARE (ダーマシェア)",
                "name": "アゼライン酸誘導体15% CICAリペアセラム 30ml (冬の肌荒れ・赤み・インナードライを整える高保湿セラム)"
            },
            {
                "rank": 10,
                "query": "DRX AZA クリア クリーム 15g アゼライン酸",
                "brand": "DRX (ディーアールエックス / ロート製薬)",
                "name": "AZAクリア クリーム 15g (クリニック推奨・高濃度アゼライン酸20%配合フェイスクリーム)"
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
            q = item["query"]
            print(f"Fetching Rank {item['rank']}: '{q}' ...")
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(q)}&hits=5&format=json&sort=standard"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
            
            chosen_item = None
            for attempt in range(3):
                try:
                    time.sleep(1.2)
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
                    time.sleep(1.5)
            
            if not chosen_item:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}! Query: '{q}'")
                continue
            
            img_url = ""
            if chosen_item.get("mediumImageUrls"):
                img_url = chosen_item["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
            elif chosen_item.get("smallImageUrls"):
                img_url = chosen_item["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
            
            price = chosen_item.get("itemPrice", 0)
            aff_url = chosen_item.get("affiliateUrl", "") or chosen_item.get("itemUrl", "")
            raw_title = chosen_item.get("itemName", item["name"])
            
            print(f"  ✅ SUCCESS: {price}円 | img:{bool(img_url)} | {raw_title[:45]}")
            results[cat_key]["items"].append({
                "rank": item["rank"],
                "name": item["name"],
                "brand": item["brand"],
                "price": price,
                "raw_title": raw_title,
                "affiliate_url": aff_url,
                "img_url": img_url
            })
            
    with open("fetched_final_30_marula_birch_azelaic.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_final_30_marula_birch_azelaic.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
