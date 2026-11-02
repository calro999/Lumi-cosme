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
    "winter_rice_power": {
        "title": "保湿力の強さで肌乾燥とさようなら！自らうるおう力を育む米発酵・ライスパワー高保湿ランク10",
        "page_file": "winter-rice-power.html",
        "items": [
            {"rank": 1, "query": "ONE BY KOSE セラム ヴェール ディープリペア", "brand": "ONE BY KOSE (コーセー)", "name": "セラム ヴェール ディープリペア 60ml (医薬部外品・ライスパワーNo.11+配合薬用導入美容液)"},
            {"rank": 2, "query": "米肌 肌潤改善エッセンス コーセー", "brand": "米肌 (MAIHADA)", "name": "肌潤改善エッセンス 30ml (医薬部外品・水分保持能改善・ライスパワーNo.11高濃度)"},
            {"rank": 3, "query": "ライスフォース ディープモイスチュアローション 120ml", "brand": "RICE FORCE (ライスフォース)", "name": "ディープモイスチュアローション 120ml (医薬部外品・薬用保湿化粧水)"},
            {"rank": 4, "query": "米肌 肌潤クリーム コーセー", "brand": "米肌 (MAIHADA)", "name": "肌潤クリーム 40g (ライスパワーNo.11＆発酵ヒアルロン酸配合濃厚高保湿)"},
            {"rank": 5, "query": "菊正宗 日本酒の化粧水 高保湿 500ml", "brand": "菊正宗 (きくまさむね)", "name": "日本酒の化粧水 高保湿 500ml (コメ発酵液・アミノ酸・セラミド大容量化粧水)"},
            {"rank": 6, "query": "白鶴 薬用 大吟醸のうるおい美白水", "brand": "白鶴酒造", "name": "薬用 大吟醸のうるおい美白水 500ml (医薬部外品・米発酵エキス＆トラネキサム酸)"},
            {"rank": 7, "query": "リアル 米ぬか美人 美人エッセンス", "brand": "リアル (米ぬか美人)", "name": "美人エッセンス 40ml (米ぬかエキス＆コメ胚芽油＆酵母エキス高保湿美容液)"},
            {"rank": 8, "query": "松山油脂 肌をうるおす 保湿フェイスクリーム", "brand": "松山油脂 (肌をうるおす)", "name": "肌をうるおす保湿スキンケア 保湿フェイスクリーム 50g (コメヌカ発酵液＆セラミド)"},
            {"rank": 9, "query": "日本盛 日本酒のたっぷり保湿化粧水", "brand": "日本盛", "name": "日本酒のたっぷり保湿化粧水 550ml (純米酒コメ発酵液・ヒアルロン酸・和漢エキス)"},
            {"rank": 10, "query": "ONE BY KOSE ディープ ハイドレーター", "brand": "ONE BY KOSE (コーセー)", "name": "ディープ ハイドレーター 160ml (医薬部外品・ヒアルロン酸＆コメ発酵高保湿化粧水)"}
        ]
    },
    "winter_camellia_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！日本の冬を潤すオレイン酸85%の極上ツヤ膜・高純度椿油ランク10",
        "page_file": "winter-camellia-oil.html",
        "items": [
            {"rank": 1, "query": "大島椿 椿油 60ml", "brand": "大島椿 (OSHIMA TSUBAKI)", "name": "大島椿 60ml (天然椿油100%・昭和2年誕生の元祖高保湿マルチオイル)"},
            {"rank": 2, "query": "黒バラ 純椿油 72ml", "brand": "黒バラ本舗", "name": "黒バラ 純椿油 72ml (生搾り製法・高浸透カメリアオイル・無添加)"},
            {"rank": 3, "query": "かづら清老舗 特製つばき油", "brand": "かづら清老舗 (京都祇園)", "name": "特製つばき油 100ml (長崎五島列島産手摘みヤブツバキ100%・最高級純椿油)"},
            {"rank": 4, "query": "五島特産 純椿油 100ml", "brand": "五島特産 (長崎五島)", "name": "純椿油 100ml (長崎五島列島産・一番搾り無添加コールドプレス)"},
            {"rank": 5, "query": "本島椿 純椿油 118ml", "brand": "本島椿 (伊豆大島)", "name": "純椿油 118ml (伊豆大島産ヤブツバキ種子100%使用・伝統製法)"},
            {"rank": 6, "query": "よーじや うるおい椿オイル", "brand": "よーじや (京都)", "name": "うるおい椿オイル 30ml (高純度精製カメリアオイル・ベタつかない美肌処方)"},
            {"rank": 7, "query": "リバティライフ 椿油 100ml", "brand": "リバティライフ", "name": "国産 椿油 100ml (天然無添加ピュアカメリアオイル・全身マルチケア)"},
            {"rank": 8, "query": "大島椿 アトピコ スキンケアオイル", "brand": "大島椿 アトピコ", "name": "アトピコ スキンケアオイル 30ml (精製ツバキ油100%・低刺激無香料無着色)"},
            {"rank": 9, "query": "自然化粧品研究所 椿油 100ml", "brand": "自然化粧品研究所", "name": "国産 椿油 100ml (未精製ゴールドタイプ・オレイン酸リッチ保湿)"},
            {"rank": 10, "query": "黒バラ本舗 ツバキオイル うるおい補修オイル", "brand": "黒バラ本舗", "name": "ツバキオイル うるおい補修オイル 47ml (アルガン＆ツバキブレンド高保湿エッセンス)"}
        ]
    },
    "winter_amino_acid": {
        "title": "保湿力の強さで肌乾燥とさようなら！天然保湿因子NMFを速攻チャージして乾きを断つ高浸透アミノ酸コスメランク10",
        "page_file": "winter-amino-acid.html",
        "items": [
            {"rank": 1, "query": "ミノン アミノモイスト モイストチャージ ローション II", "brand": "MINON (第一三共ヘルスケア)", "name": "ミノン アミノモイスト モイストチャージ ローションII もっとしっとり 150ml (9種の保潤アミノ酸配合)"},
            {"rank": 2, "query": "松山油脂 肌をうるおす 保湿浸透水 モイストリッチ", "brand": "松山油脂 (肌をうるおす)", "name": "肌をうるおす保湿スキンケア 保湿浸透水 モイストリッチ 120ml (5種のヒト型セラミド＆アミノ酸)"},
            {"rank": 3, "query": "ミノン アミノモイスト モイストチャージ ミルク", "brand": "MINON (第一三共ヘルスケア)", "name": "ミノン アミノモイスト モイストチャージ ミルク 100g (すっとなじむアミノ酸高保湿乳液)"},
            {"rank": 4, "query": "ジーノ アミノ モイスト エッセンス 味の素", "brand": "Jino (味の素)", "name": "アミノ モイスト エッセンス 60ml (味の素のアミノ酸先端バイオ科学・高濃度NMFチャージ)"},
            {"rank": 5, "query": "ドクターシーラボ VC100エッセンスローションEX", "brand": "ドクターシーラボ", "name": "VC100エッセンスローションEX 150ml (高浸透ビタミンC APPS＆11種のアミノ酸)"},
            {"rank": 6, "query": "キュレル 潤浸保湿 化粧水 III とてもしっとり", "brand": "Curel (花王キュレル)", "name": "潤浸保湿 化粧水 III とてもしっとり 150ml (医薬部外品・消炎剤＆アミノ酸系保湿成分)"},
            {"rank": 7, "query": "松山油脂 Mマーク アミノ酸浸透ジェル", "brand": "M-mark (松山油脂)", "name": "アミノ酸浸透ジェル 150ml (角層NMFアミノ酸補給・水分補給高保水ジェル)"},
            {"rank": 8, "query": "ミノン アミノモイスト アミノフルシャワー", "brand": "MINON (第一三共ヘルスケア)", "name": "ミノン アミノモイスト アミノフルシャワー 150g (微細ミスト・日中の暖房乾燥レスキュー)"},
            {"rank": 9, "query": "エトヴォス モイスチャライジングローション", "brand": "ETVOS (エトヴォス)", "name": "モイスチャライジングローション 150ml (天然保湿因子NMF補給・グルコシルセラミド)"},
            {"rank": 10, "query": "ラネージュ クリームスキン ローション", "brand": "LANEIGE (ラネージュ)", "name": "クリームスキン ローション 170ml (高保湿ペプチドアミノ酸・超濃密水分補給)"}
        ]
    }
}

def fetch_single(query_info):
    q = query_info["query"]
    queries_to_try = [q]
    parts = q.split()
    if len(parts) > 2:
        queries_to_try.append(" ".join(parts[:2]))
    if len(parts) > 3:
        queries_to_try.append(parts[0])

    for current_q in queries_to_try:
        url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(current_q)}&hits=5&format=json&sort=standard"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        
        for attempt in range(2):
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                    data = json.loads(res.read().decode('utf-8'))
                    items = data.get("Items", [])
                    if not items:
                        break
                    chosen = None
                    for it in items:
                        item_obj = it["Item"]
                        if item_obj.get("itemPrice", 0) > 0 and (item_obj.get("mediumImageUrls") or item_obj.get("smallImageUrls")):
                            chosen = item_obj
                            break
                    if not chosen:
                        chosen = items[0]["Item"]
                        
                    img_url = ""
                    if chosen.get("mediumImageUrls"):
                        img_url = chosen["mediumImageUrls"][0]["imageUrl"].replace("?_ex=128x128", "?_ex=300x300")
                    elif chosen.get("smallImageUrls"):
                        img_url = chosen["smallImageUrls"][0]["imageUrl"].replace("?_ex=64x64", "?_ex=300x300")
                    
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "query": current_q,
                        "rakuten_name": chosen.get("itemName", ""),
                        "price": chosen.get("itemPrice", 0),
                        "rakuten_url": chosen.get("itemUrl", ""),
                        "affiliate_url": chosen.get("affiliateUrl", chosen.get("itemUrl", "")),
                        "img_url": img_url
                    }
            except Exception as e:
                print(f"Error fetching '{current_q}': {e}")
                time.sleep(1.0)
    return None

results = {}
all_success = True
for cat_key, cat_data in CATEGORIES.items():
    print(f"\n==========================================")
    print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
    print(f"==========================================")
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": []
    }
    for item_info in cat_data["items"]:
        print(f"Fetching Rank #{item_info['rank']}: {item_info['name'][:30]} (query: {item_info['query']})")
        res = fetch_single(item_info)
        if res and res.get("price", 0) > 0 and res.get("img_url"):
            print(f"  -> SUCCESS: Price=¥{res['price']:,}, Image={res['img_url'][:45]}...")
            results[cat_key]["items"].append(res)
        else:
            print(f"  -> FAILED to fetch item!")
            all_success = False
        time.sleep(0.4)

output_file = "fetched_3new_nov_dec_rice_camellia_amino_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nSaved all results to {output_file}!")
if all_success:
    print("ALL 30 ITEMS FETCHED WITH 100% SUCCESS!")
else:
    print("WARNING: Some items failed to fetch!")
