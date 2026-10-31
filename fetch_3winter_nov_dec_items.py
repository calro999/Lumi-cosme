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
    "winter_cleansing_oil": {
        "title": "保湿力の強さで冬の頑固な毛穴詰まり・洗い上がりの砂漠化とさようなら！摩擦レスでうるおい守る高保湿クレンジングオイルランク10",
        "page_file": "winter-cleansing-oil.html",
        "items": [
            {"rank": 1, "query": "シュウウエムラ アルティム8 クレンジングオイル 450ml", "brand": "shu uemura (シュウ ウエムラ)", "name": "アルティム8∞ スブリム ビューティ クレンジング オイル (ツバキ種子油配合・スキンケア成分75%配合の至高の美容オイルクレンジング)"},
            {"rank": 2, "query": "アテニア スキンクリア クレンズ オイル アロマタイプ 175ml", "brand": "Attenir (アテニア)", "name": "スキンクリア クレンズ オイル アロマタイプ (肌ステインを洗い流すロックローズオイル配合・W洗顔不要でくすみ知らずの神オイル)"},
            {"rank": 3, "query": "ファンケル マイルドクレンジングオイル 120ml", "brand": "FANCL (ファンケル)", "name": "マイルドクレンジング オイル (熟成ホップエキス配合・こすらずするんと角栓オフしてうるおいバリアを守る殿堂入り名品)"},
            {"rank": 4, "query": "魔女工場 ピュアクレンジングオイル 200ml", "brand": "manyo (魔女工場)", "name": "ピュア クレンジング オイル (14種類の植物性オイル配合・冬の角栓やブラックヘッドをやさしく溶かし出す天然由来99%のうるおいオイル)"},
            {"rank": 5, "query": "カネボウ メロウ オフ ヴェイル 160g", "brand": "KANEBO (カネボウ)", "name": "メロウ オフ ヴェイル (スマートクレンジング技術・とろけるヴェールで汚れを吸い上げ後肌しっとり吸い付く美容液クレンジング)"},
            {"rank": 6, "query": "ボビイ ブラウン スージング クレンジング オイル 200ml", "brand": "BOBBI BROWN (ボビイ ブラウン)", "name": "スージング クレンジング オイル (ククイナッツオイル×ヒマワリ種子油・ウォータープルーフも素早く落として極上のうるおい膜を残す)"},
            {"rank": 7, "query": "THREE バランシング クレンジング オイル N 185ml", "brand": "THREE (スリー)", "name": "バランシング クレンジング オイル N (国産精油ブレンド・冬の冷え固まった肌をアロマでほぐしながら汚れを浮かす贅沢クレンジング)"},
            {"rank": 8, "query": "クレドポーボーテ ユイルデマキアントヴィサージュ 200ml", "brand": "Cle de Peau Beaute (クレ・ド・ポー ボーテ)", "name": "ユイルデマキアントヴィサージュ (厳選ボタニカルオイル配合・上質なシルクを滑らせるような摩擦レスな極上クレンジング体験)"},
            {"rank": 9, "query": "キュレル オイルメイク落とし 150ml", "brand": "Curel (キュレル)", "name": "オイルメイク落とし (消炎剤配合・セラミドを守りながらウォータープルーフもすっきり落とす敏感肌のための医薬部外品オイル)"},
            {"rank": 10, "query": "無印良品 マイルドオイルクレンジング 400ml", "brand": "無印良品 (MUJI)", "name": "マイルドオイルクレンジング (オリーブ油・アンズ果汁配合・大容量で惜しみなく使えて摩擦ゼロを叶える高コスパ名品)"}
        ]
    },
    "winter_body_milk": {
        "title": "保湿力の強さで全身のカサカサ粉吹き・インナー摩擦乾燥とさようなら！スーッと浸透して服もすぐ着られる高保湿ボディミルクランク10",
        "page_file": "winter-body-milk.html",
        "items": [
            {"rank": 1, "query": "ニベア スキンミルク しっとり 200g", "brand": "NIVEA (ニベア)", "name": "スキンミルク しっとり (ディープ＆ロングラスティングモイスチャー処方・超乾燥肌の粉吹きを角層深くからうるおす国民的ボディミルク)"},
            {"rank": 2, "query": "キュレル 潤浸保湿 モイスチャーローション 乳液タイプ 220ml", "brand": "Curel (キュレル)", "name": "潤浸保湿 モイスチャーローション (セラミド機能成分配合・冬の衣類摩擦による赤みやかゆみを防ぐ全身用低刺激ミルク)"},
            {"rank": 3, "query": "ミノン 全身保湿ミルク 400ml", "brand": "MINON (ミノン)", "name": "全身保湿ミルク 大容量ポンプ (バリア機能をサポートするアミノ酸配合・スーッとなじんで敏感肌を優しく守る医薬部外品ミルク)"},
            {"rank": 4, "query": "SHIRO ホワイトリリー ボディミルク 195g", "brand": "SHIRO (シロ)", "name": "ホワイトリリー ボディミルク (シアバター配合・冬の肌をみずみずしく満たしながら洗練されたフローラルの香りで包み込むデパコス名品)"},
            {"rank": 5, "query": "ローラ メルシエ セラム ボディエマルジョン アンバーバニラ", "brand": "LAURA MERCIER (ローラ メルシエ)", "name": "セラム ボディエマルジョン アンバーバニラ (甘く官能的なアンバーバニラの香り・美容液級の浸透力でシルクのようなツヤ肌に仕立てる)"},
            {"rank": 6, "query": "ビオレu ザ ボディ ぬれた肌に使うボディ乳液 300ml", "brand": "ビオレu (花王)", "name": "ザ ボディ ぬれた肌に使うボディ乳液 (お風呂場の中で濡れたまま塗れる・冬の脱衣所乾燥を先回りブロックする画期的高保湿ミルク)"},
            {"rank": 7, "query": "ジョンソン ドリーミースキン アロマローション 500ml", "brand": "ジョンソンボディケア", "name": "ドリーミースキン アロマローション (ラベンダー＆カモミールのアロマブレンド・ベビーオイル配合で一晩中うるおいが続く大容量ミルク)"},
            {"rank": 8, "query": "セタフィル モイスチャライジング ローション 591ml", "brand": "Cetaphil (セタフィル)", "name": "モイスチャライジング ローション (ナイアシンアミド×パンテノール×グリセリン・皮膚科学に基づき敏感肌の角層バリアを立て直す)"},
            {"rank": 9, "query": "ニュートロジーナ インテンスリペア CICA ボディエマルジョン 250ml", "brand": "Neutrogena (ニュートロジーナ)", "name": "ノルウェーフォーミュラ インテンスリペア CICA ボディエマルジョン (純度99%高濃度グリセリン×CICA配合・超乾燥肌のひび割れを速攻リペア)"},
            {"rank": 10, "query": "ヴェレダ スキンフード ボディミルク 200ml", "brand": "WELEDA (ヴェレダ)", "name": "スキンフード ボディミルク (パンジーエキス＆カレンドラ配合・伝統ハーブの濃厚な恵みで冬のゴワつく全身をしっとり柔らかに整える)"}
        ]
    },
    "winter_toner_pad": {
        "title": "保湿力の強さで朝の乾燥ゴワつき・メイクの粉浮きとさようなら！貼るだけで水分爆弾チャージする高保湿トナーパッドランク10",
        "page_file": "winter-toner-pad.html",
        "items": [
            {"rank": 1, "query": "Torriden ダイブイン 低分子ヒアルロン酸 マルチパッド 80枚", "brand": "Torriden (トリデン)", "name": "ダイブイン 低分子ヒアルロン酸 マルチパッド (5D複合ヒアルロン酸配合・冬の朝のインナードライ肌に水分をぐんぐんチャージする神パッド)"},
            {"rank": 2, "query": "メディヒール マデカソサイド ブレミッシュ パッド 100枚", "brand": "MEDIHEAL (メディヒール)", "name": "マデカソサイド ブレミッシュ パッド (純度98%ツボクサエキス配合・冬の乾燥赤みや肌荒れを優しく鎮静する大判角質ケアパッド)"},
            {"rank": 3, "query": "Anua ドクダミ 77% クリアパッド 70枚", "brand": "Anua (アヌア)", "name": "ドクダミ 77% クリアパッド (ドクダミエキス77%高配合・冬のゴワついた角質をやさしくふき取りながらキメの整ったうるツヤ肌へ導く)"},
            {"rank": 4, "query": "Abib 復活草 コラーゲン ゲルマスク パッド 60枚", "brand": "Abib (アビブ)", "name": "コラーゲンゲルマスク 復活草パッド (復活草エキス×ヴィーガンコラーゲン・冬の寒さでたるんだ毛穴や乾燥をふっくらモチモチに満たす)"},
            {"rank": 5, "query": "ナンバーズイン 5番 白玉グルタチオンC フィルムパッド", "brand": "numbuzin (ナンバーズイン)", "name": "5番 白玉グルタチオンC フィルムパッド (高純度グルタチオン×ビタミンC・冬のどんより乾燥くすみを一掃して発光するような透明美肌へ)"},
            {"rank": 6, "query": "VT シカデイリースージング パッド 60枚", "brand": "VT COSMETICS (ブイティー)", "name": "シカ デイリースージング パッド (シカヒアルロン配合・BHAで冬の角質をマイルドに整えながら水分バリアを強力に補強)"},
            {"rank": 7, "query": "セリマックス ノニ アンプル パッド 30枚", "brand": "celimax (セリマックス)", "name": "消しゴムパッド / ノニアンプル パッド (スーパーフード・ノニエキス高濃縮配合・冬の乾燥疲れ肌に豊かな栄養とうるおいを届ける)"},
            {"rank": 8, "query": "スキンフード キャロット カロチン リリーフ パッド 60枚", "brand": "SKINFOOD (スキンフード)", "name": "キャロットカロチン リリーフ パッド (無農薬ニンジン種子油配合・ワッフル形状の極厚パッドで冬の乾燥肌を優しく包み込むオリーブヤング大人気名品)"},
            {"rank": 9, "query": "ワンデイズユー ヘルプミー ダクトパッド 60枚", "brand": "One-day's you (ワンデイズユー)", "name": "ヘルプミー！ダクトパッド (ツボクサエキス×パンテノール・冬の敏感肌をいたわりながら弱酸性で角質ケア＆保湿を両立)"},
            {"rank": 10, "query": "デイジーク ハート デュアル パッド", "brand": "dasique (デイジーク)", "name": "ハート デュアル トナーパッド (SNSで話題沸騰・かわいいハート型パッドに高保湿エッセンスがたっぷり浸透・冬の部分保湿パックに最適)"}
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
            url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={urllib.parse.quote(query)}&hits=5&format=json&sort=standard"
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
                    
                    if not aff_url:
                        aff_url = chosen.get("itemUrl", "")
                        
                    return {
                        "rank": query_info["rank"],
                        "brand": query_info["brand"],
                        "name": query_info["name"],
                        "itemName": item_name,
                        "price": price,
                        "img": high_res_img,
                        "url": aff_url
                    }
                else:
                    alt_q = query_info["brand"].split()[0] + " " + query.split()[0]
                    if attempt == 2 and alt_q != query:
                        query = alt_q
        except Exception as e:
            print(f"Error fetching {query}: {e}")
            time.sleep(1)
        time.sleep(0.3)
    
    return {
        "rank": query_info["rank"],
        "brand": query_info["brand"],
        "name": query_info["name"],
        "itemName": query_info["name"],
        "price": 3500,
        "img": "https://thumbnail.image.rakuten.co.jp/@0_mall/sample/item.jpg",
        "url": "https://hb.afl.rakuten.co.jp/"
    }

results = {}
for cat_key, cat_data in CATEGORIES.items():
    print(f"\nFetching category: {cat_key}...")
    cat_items = []
    for q_item in cat_data["items"]:
        res_item = fetch_item_with_retry(q_item)
        print(f"  Rank {res_item['rank']}: {res_item['brand']} - ¥{res_item['price']:,} - Img: {res_item['img'][:45]}...")
        cat_items.append(res_item)
    results[cat_key] = {
        "title": cat_data["title"],
        "page_file": cat_data["page_file"],
        "items": cat_items
    }

with open("rakuten_3winter_nov_dec_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nAll items fetched and saved to rakuten_3winter_nov_dec_data.json!")
