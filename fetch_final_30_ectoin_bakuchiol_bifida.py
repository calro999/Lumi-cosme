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
    "winter_ectoin": {
        "title": "保湿力の強さで肌乾燥とさようなら！極限環境の生命力で乾かない水分シェルターを築く高保水エクトインコスメランク10",
        "file": "winter-ectoin.html",
        "items": [
            {"rank": 1, "query": "ラブミータッチ ホワイトシャインローション リッチ 30mL", "brand": "Lov me Touch (ラブミータッチ)", "name": "ホワイトシャインローション リッチ 30ml (高純度エクトイン×ビタミンC誘導体×フラーレン配合高機能美容液)"},
            {"rank": 2, "query": "SKINFONIA 美容液 30ml", "brand": "SKINFONIA (スキンフォニア)", "name": "バランスリペアセラム 30ml (高純度エクトイン×セラミド×ナイアシンアミド配合ドクターズセラム)"},
            {"rank": 3, "query": "ラブミータッチ スキンバリア ナノミルク リッチ", "brand": "Lov me Touch (ラブミータッチ)", "name": "スキンバリア ナノミルク リッチ 50ml (エクトイン×高濃度セラミド15%配合浸透乳液)"},
            {"rank": 4, "query": "beplain シカテロル美容液", "brand": "beplain (ビープレーン)", "name": "シカテロル アンプル 30ml (高浸透エクトイン×シカ高濃度濃縮鎮静美容液)"},
            {"rank": 5, "query": "もち肌コラーゲンセラム メディキューブ", "brand": "medicube (メディキューブ)", "name": "トリプルコラーゲンセラム 55ml (エクトイン×3重コラーゲン配合濃密水分リフトセラム)"},
            {"rank": 6, "query": "リジェンスキン SRS ダーマクリームプラス エクトイン", "brand": "RegenSkin (リジェンスキン)", "name": "SRS ダーマクリームプラス 50ml (高純度エクトイン配合・真冬の皮膚バリア再生保護クリーム)"},
            {"rank": 7, "query": "ヴァーチェ ミネラルベールパウダー エクトイン", "brand": "VIRCHE (ヴァーチェ)", "name": "ミネラルベールパウダー (高純度エクトイン配合・真冬の乾燥崩れを防ぐモイストミネラルパウダー)"},
            {"rank": 8, "query": "Abib エアリーサンスティック エクトイン", "brand": "Abib (アビブ)", "name": "エアリーサンスティック スムージングバー 23g (エクトイン配合・真冬の紫外線と乾燥から守る高保湿スティック)"},
            {"rank": 9, "query": "かづきれいこ キープモイストウォーター", "brand": "REIKO KAZKI (カヅキレイコ)", "name": "キープモイストウォーター 50ml (高純度エクトイン配合・メイク密着高保湿フィックスミスト化粧水)"},
            {"rank": 10, "query": "Sola ソラ バランシングセラム エクトイン", "brand": "Sola (ソラ)", "name": "バランシングセラム 50ml (エクトイン×フラーレン×レチノール配合集中保水セラム)"}
        ]
    },
    "winter_bakuchiol": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の敏感肌でも皮剥けゼロでハリツヤ満たす高保湿バクチオールランク10",
        "file": "winter-bakuchiol.html",
        "items": [
            {"rank": 1, "query": "エッセンスBK 30mL バクチオール 配合 美容液", "brand": "自然化粧品研究所", "name": "エッセンスBK 30ml (植物性バクチオール配合・乾燥小ジワをふっくら満たす高保湿乳液美容液)"},
            {"rank": 2, "query": "By Wishtrend バクチオール ナイトクリーム", "brand": "By Wishtrend (バイウィッシュトレンド)", "name": "ビタミンA-mazing バクチオール ナイトクリーム 30g (バクチオール×レチナール低刺激ハリ弾力クリーム)"},
            {"rank": 3, "query": "ドクターケイ ABC-Gリペアセラム 25ml", "brand": "Dr.K (ドクターケイ)", "name": "ABC-Gリペアセラム 25ml (高濃度バクチオール×レチノール誘導体×ビタミンCトリプルリペア美容液)"},
            {"rank": 4, "query": "ワンシング PDRN バクチオール セラム", "brand": "ONE THING (ワンシング)", "name": "PDRN バクチオール セラム 30ml (植物性ヴィーガンバクチオール×高浸透サーモンPDRN配合セラム)"},
            {"rank": 5, "query": "ネオゼン バクチオール", "brand": "NEOGEN (ネオゼン)", "name": "リアル バクチオール ファーミング セラム 30ml (高純度植物性バクチオール配合・弾力リフト美容液)"},
            {"rank": 6, "query": "クレアス ミッドナイトブルーカーミングクリーム", "brand": "Dear, Klairs (クレアス)", "name": "ミッドナイトブルー カーミングクリーム 60ml (バクチオール＆グアイアズレン配合・真冬の鎮静保湿バーム)"},
            {"rank": 7, "query": "トゥヴェール ナノエマルジョン ディープ 60mL", "brand": "TOUT VERT (トゥヴェール)", "name": "ナノエマルジョン ディープ 60ml (バクチオール×ヒト型セラミド配合インナードライ対策高保湿乳液)"},
            {"rank": 8, "query": "イニスフリー レチノール シカ", "brand": "innisfree (イニスフリー)", "name": "レチノール シカ リペア セラム 30ml (植物性バクチオール類似低刺激処方・真冬の毛穴キメ集中セラム)"},
            {"rank": 9, "query": "VT リードルショット レチノール", "brand": "VT COSMETICS (ブイティー)", "name": "シカレチA エッセンス 0.1 30ml (バクチオール×安定化レチノール×CICA針美容液)"},
            {"rank": 10, "query": "バクチオール 美容液 2本セット 高配合 植物由来100％ オイル美容液", "brand": "BOTANICAL LAB", "name": "高濃度バクチオール100%植物性オイル美容液 20ml (皮剥けゼロ・真冬の高保湿ハリ弾力オイル)"}
        ]
    },
    "winter_bifida": {
        "title": "保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房に負けない強靭バリアを育む高濃度ビフィダ美容液ランク10",
        "file": "winter-bifida.html",
        "items": [
            {"rank": 1, "query": "Manyo 魔女工場 ビフィダ バイオーム アンプル", "brand": "魔女工場 (Manyo Factory)", "name": "ビフィダ バイオーム コンプレックス アンプル 50ml (美肌菌×5種プロバイオティクス殿堂入り美容液)"},
            {"rank": 2, "query": "numbuzin ナンバーズイン 3番 すべすべキメケアセラム 50ml", "brand": "numbuzin (ナンバーズイン)", "name": "3番 すべすべキメケアセラム 50ml (ビフィズス菌発酵エキス42%＋ガラクトミセス配合キメ改善セラム)"},
            {"rank": 3, "query": "エスティローダー アドバンス ナイト リペア SMR 50ml", "brand": "ESTEE LAUDER (エスティ ローダー)", "name": "アドバンス ナイト リペア SMR コンプレックス 50ml (ビフィズス菌発酵エキス配合・夜間集中修復美容液)"},
            {"rank": 4, "query": "MISSHA ミシャ タイムレボリューションナイトリペア", "brand": "MISSHA (ミシャ)", "name": "タイムレボリューション ナイトリペア アンプル 5X 50ml (極限発酵ビフィダ77.2%配合・濃密夜用発酵美容液)"},
            {"rank": 5, "query": "ランコム ジェニフィック 美容液", "brand": "LANCOME (ランコム)", "name": "ジェニフィック アルティメ セラム 30ml (美肌菌・ビフィズス菌培養溶解質配合最高峰ブースター美容液)"},
            {"rank": 6, "query": "イニスフリー ブラックティー ユース セラム", "brand": "innisfree (イニスフリー)", "name": "ブラックティー ユース セラム 50ml (ビフィズス菌培養溶解質×発酵ブラックティー濃厚疲労回復セラム)"},
            {"rank": 7, "query": "トニーモリー 2X ツーエックス ファースト エッセンス", "brand": "TONYMOLY (トニーモリー)", "name": "2X ファースト エッセンス 200ml (高純度発酵ビフィズス菌マイクロカプセル配合ブースター導入化粧液)"},
            {"rank": 8, "query": "manyo ビフィダバイオームアンプルトナー", "brand": "魔女工場 (Manyo Factory)", "name": "ビフィダ バイオーム アンプル トナー 400ml (大容量弱酸性・美肌菌バリア高保湿化粧水)"},
            {"rank": 9, "query": "mixsoon ビフィダトナー", "brand": "mixsoon (ミクスン)", "name": "ビフィダ トナー 150ml (純度100%ビフィズス菌発酵エキス・角層バリア再建高保湿化粧水)"},
            {"rank": 10, "query": "魔女工場 ビフィダ ミスト", "brand": "魔女工場 (Manyo Factory)", "name": "ビフィダ アンプル ミスト 120ml (美肌菌バリア微細マイクロミスト・日中暖房乾燥レスキュー)"}
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
                    time.sleep(1.3)
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
            
    with open("fetched_final_30_ectoin_bakuchiol_bifida.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all 30 items to fetched_final_30_ectoin_bakuchiol_bifida.json successfully!")

if __name__ == "__main__":
    fetch_and_save()
