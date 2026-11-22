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
    "winter_cleansing_water": {
        "file": "winter-cleansing-water.html",
        "url": "/winter-cleansing-water",
        "title": "保湿力の強さで冬洗顔のつっぱりとさようなら！W洗顔不要の高保湿クレンジングウォーター（ミセラー水）ランク10【11月・12月】",
        "items": [
            {
                "rank": 1,
                "brand": "BIODERMA (ビオデルマ)",
                "name": "サンシビオ エイチツーオー D 500mL",
                "queries": ["ビオデルマ サンシビオ H2O 500ml"],
                "must_include": ["ビオデルマ", "サンシビオ"],
                "exclude": ["2本", "3本", "セット", "訳あり"]
            },
            {
                "rank": 2,
                "brand": "Koh Gen Do (江原道)",
                "name": "クレンジングウォーター 380mL",
                "queries": ["江原道 クレンジングウォーター 380ml"],
                "must_include": ["クレンジングウォーター"],
                "exclude": ["ミニ", "100ml", "セット"]
            },
            {
                "rank": 3,
                "brand": "Chacott (チャコット・コスメティクス)",
                "name": "クレンジングウォーター 500mL",
                "queries": ["チャコット クレンジングウォーター 500ml"],
                "must_include": ["チャコット", "クレンジングウォーター"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 4,
                "brand": "Bifesta (マンダム ビフェスタ)",
                "name": "ミセラー クレンジングウォーター セラムモイスト 400mL",
                "queries": ["ビフェスタ ミセラークレンジングウォーター モイスト 400ml"],
                "must_include": ["ビフェスタ", "モイスト"],
                "exclude": ["つめかえ", "詰替", "詰め替え", "セット"]
            },
            {
                "rank": 5,
                "brand": "d program (資生堂 dプログラム)",
                "name": "エッセンスイン クレンジングウォーター 180mL (医薬部外品)",
                "queries": ["資生堂 dプログラム エッセンスイン クレンジングウォーター 180ml"],
                "must_include": ["エッセンスイン", "クレンジングウォーター"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 6,
                "brand": "クレ・ド・ポー ボーテ (Clé de Peau Beauté)",
                "name": "オーミセラーデマキアントヴィサージュ 200mL",
                "queries": ["クレドポーボーテ オーミセラーデマキアントヴィサージュ"],
                "must_include": ["オーミセラーデマキアントヴィサージュ"],
                "exclude": ["セット"]
            },
            {
                "rank": 7,
                "brand": "URIAGE (ユリアージュ)",
                "name": "サーマル クレンジングウォーター (乾燥肌用) 250mL",
                "queries": ["ユリアージュ サーマル クレンジングウォーター"],
                "must_include": ["ユリアージュ", "クレンジング"],
                "exclude": ["セット"]
            },
            {
                "rank": 8,
                "brand": "ETUDE (エチュード)",
                "name": "スンジョン クレンジングウォーター 300mL",
                "queries": ["エチュード クレンジングウォーター スンジョン", "エチュード クレンジングウォーター"],
                "must_include": ["スンジョン", "クレンジングウォーター"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 9,
                "brand": "ma:nyo (魔女工場)",
                "name": "ピュアソイビーン クレンジングウォーター 500mL",
                "queries": ["魔女工場 クレンジングウォーター"],
                "must_include": ["クレンジングウォーター"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 10,
                "brand": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
                "name": "ミセラーウォーター ウルトラ 200mL",
                "queries": ["ラロッシュポゼ ミセラーウォーター ウルトラ"],
                "must_include": ["ミセラーウォーター"],
                "exclude": ["セット", "2本", "400ml"]
            }
        ]
    },
    "winter_moisture_mascara": {
        "file": "winter-moisture-mascara.html",
        "url": "/winter-moisture-mascara",
        "title": "冬の目元乾燥とパンダ目を同時に防ぐ！まつ毛を労わるお湯落ち高保湿・美容液マスカラ厳選10選【11月・12月】",
        "items": [
            {
                "rank": 1,
                "brand": "dejavu (デジャヴュ)",
                "name": "塗るつけまつげ ファイバーウィッグ ウルトラロングE",
                "queries": ["デジャヴュ ファイバーウィッグ ウルトラロングE"],
                "must_include": ["デジャヴュ"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 2,
                "brand": "ヒロインメイク (伊勢半)",
                "name": "ロング＆カールマスカラ アドバンストフィルム",
                "queries": ["ヒロインメイク ロング カールマスカラ アドバンストフィルム"],
                "must_include": ["アドバンストフィルム"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 3,
                "brand": "OPERA (オペラ)",
                "name": "マイラッシュ アドバンスト",
                "queries": ["オペラ マイラッシュ アドバンスト"],
                "must_include": ["マイラッシュ"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 4,
                "brand": "D-UP (ディーアップ)",
                "name": "パーフェクトエクステンション マスカラ (お湯オフ・美容液成分配合)",
                "queries": ["ディーアップ パーフェクトエクステンション マスカラ ブラック"],
                "must_include": ["パーフェクトエクステンション"],
                "exclude": ["ウォータープルーフ", "for カール", "セット", "2本"]
            },
            {
                "rank": 5,
                "brand": "CLINIQUE (クリニーク)",
                "name": "ラッシュ パワー マスカラ ロング ウェアリング フォーミュラ",
                "queries": ["クリニーク ラッシュ パワー マスカラ ロング ウェアリング"],
                "must_include": ["ラッシュ"],
                "exclude": ["2本", "3本", "セット", "ミニ"]
            },
            {
                "rank": 6,
                "brand": "Wonjungyo (ウォンジョンヨ)",
                "name": "ヌードアイラッシュ (コーム型・美容液成分配合お湯落ち)",
                "queries": ["ウォンジョンヨ ヌードアイラッシュ"],
                "must_include": ["ヌードアイラッシュ"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 7,
                "brand": "アンファー (ANGFA)",
                "name": "スカルプD マスカラ ボリュームアップ / ピュアフリー (まつ毛美容液成分配合)",
                "queries": ["アンファー スカルプD マスカラ"],
                "must_include": ["スカルプD", "マスカラ"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 8,
                "brand": "UZU BY FLOWFUSHI (ウズ)",
                "name": "MOTE MASCARA (モテマスカラ)",
                "queries": ["UZU モテマスカラ"],
                "must_include": ["モテマスカラ"],
                "exclude": ["セット", "2本"]
            },
            {
                "rank": 9,
                "brand": "ETVOS (エトヴォス)",
                "name": "ミネラルロングラッシュマスカラ",
                "queries": ["エトヴォス ミネラルロングラッシュマスカラ"],
                "must_include": ["ミネラルロングラッシュ"],
                "exclude": ["セット"]
            },
            {
                "rank": 10,
                "brand": "MAYBELLINE (メイベリン ニューヨーク)",
                "name": "ラッシュニスタ N (お湯落ちフィルムマスカラ)",
                "queries": ["メイベリン ラッシュニスタ"],
                "must_include": ["ラッシュニスタ"],
                "exclude": ["セット", "2本"]
            }
        ]
    },
    "winter_gift_set": {
        "file": "winter-gift-set.html",
        "url": "/winter-gift-set",
        "title": "11月・12月の贈り物に外さない！冬の乾燥肌を潤す人気ブランド高保湿ハンド＆ボディ・リップギフトセット厳選10選",
        "items": [
            {
                "rank": 1,
                "brand": "L'OCCITANE (ロクシタン)",
                "name": "フラワーハンドクリームトリオ (ラッピング・ペーパーバッグ付)",
                "queries": ["ロクシタン ハンドクリーム ギフトセット ラッピング"],
                "must_include": ["ロクシタン", "ハンドクリーム"],
                "exclude": ["アドベント", "中古", "空箱"]
            },
            {
                "rank": 2,
                "brand": "Aesop (イソップ)",
                "name": "アンドラム/レスレクション ハンドバーム＆リップ ギフトセット",
                "queries": ["イソップ ハンドバーム ギフト ラッピング"],
                "must_include": ["イソップ", "ギフト"],
                "exclude": ["中古", "サンプル"]
            },
            {
                "rank": 3,
                "brand": "JILL STUART (ジルスチュアート)",
                "name": "ホワイトフローラル ハンドクリーム＆リップマスク 純正ギフトBOX",
                "queries": ["ジルスチュアート ハンドクリーム リップバーム ギフト"],
                "must_include": ["ジルスチュアート", "ハンドクリーム"],
                "exclude": ["コフレ", "中古"]
            },
            {
                "rank": 4,
                "brand": "SABON (サボン)",
                "name": "ボディスクラブ60g＋ハンドクリーム30mL＋バスボム 3点ギフトセット",
                "queries": ["サボン ハンドクリーム ボディスクラブ ギフトセット"],
                "must_include": ["SABON", "ギフト"],
                "exclude": ["ホリデー", "アドベント", "中古"]
            },
            {
                "rank": 5,
                "brand": "Dior (ディオール)",
                "name": "ミス ディオール ハンド クリーム 50mL (純正ラッピング付ギフト)",
                "queries": ["ディオール ミスディオール ハンドクリーム ギフト"],
                "must_include": ["ディオール", "ハンドクリーム"],
                "exclude": ["ホリデー", "中古"]
            },
            {
                "rank": 6,
                "brand": "SHIRO (シロ)",
                "name": "ハンドソープ＆ハンドクリーム ハンドケアギフトセット",
                "queries": ["SHIRO ハンドソープ ハンドクリーム ギフトセット"],
                "must_include": ["SHIRO", "ハンドクリーム"],
                "exclude": ["箱なし", "中古"]
            },
            {
                "rank": 7,
                "brand": "john masters organics (ジョンマスターオーガニック)",
                "name": "ヘアドライタオル・ヘアケア ギフトセット",
                "queries": ["ジョンマスターオーガニック ギフトセット"],
                "must_include": ["ジョンマスター", "ギフト"],
                "exclude": ["中古"]
            },
            {
                "rank": 8,
                "brand": "NEAL'S YARD REMEDIES (ニールズヤード レメディーズ)",
                "name": "ハンドケア トリオギフト (公式ギフト箱入り)",
                "queries": ["ニールズヤード ハンドケア トリオギフト", "ニールズヤード ハンドクリーム ギフト"],
                "must_include": ["ギフト"],
                "exclude": ["中古"]
            },
            {
                "rank": 9,
                "brand": "PAUL & JOE (ポール＆ジョー)",
                "name": "ハンカチ＆ハンドクリーム 名入れギフトセット",
                "queries": ["ポールアンドジョー ハンドクリーム ギフト"],
                "must_include": ["ポールアンドジョー", "ハンドクリーム"],
                "exclude": ["中古", "ミラー"]
            },
            {
                "rank": 10,
                "brand": "AYURA (アユーラ)",
                "name": "メディテーションバスt＆タオル・ハンディバッグ ギフトセット",
                "queries": ["アユーラ 入浴剤 ギフトセット"],
                "must_include": ["アユーラ", "ギフト"],
                "exclude": ["中古"]
            }
        ]
    }
}

def extract_image_url(cand):
    urls = cand.get("mediumImageUrls") or cand.get("smallImageUrls") or []
    if not urls:
        return ""
    first = urls[0]
    raw = first.get("imageUrl", "") if isinstance(first, dict) else str(first)
    if "?_ex=" in raw:
        return raw.split("?_ex=")[0] + "?_ex=400x400"
    return raw

def match_candidate(cand, must_include, exclude):
    name = cand.get("itemName", "")
    for ex in exclude:
        if ex.lower() in name.lower():
            return False
    for kw in must_include:
        if kw.lower() not in name.lower():
            return False
    return True

def fetch_all():
    results = {}
    total_fetched = 0
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n=== Fetching {cat_key} ===")
        results[cat_key] = {
            "file": cat_data["file"],
            "url": cat_data["url"],
            "title": cat_data["title"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"  Rank {item['rank']}: query='{q}'")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=15&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                try:
                    time.sleep(1.2)
                    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
                        data = json.loads(res.read().decode('utf-8'))
                        items = data.get("Items", [])
                        # Pass 1: strict match + has reviews + lower price preferred for fair/authentic pricing if multiple
                        cands = []
                        for it in items:
                            cand = it["Item"]
                            if cand.get("itemPrice", 0) >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")) and match_candidate(cand, item["must_include"], item.get("exclude", [])):
                                cands.append(cand)
                        rev_cands = [c for c in cands if c.get("reviewCount", 0) > 0]
                        if rev_cands:
                            # Pick highest reviewCount among strict matches
                            rev_cands.sort(key=lambda x: x.get("reviewCount", 0), reverse=True)
                            chosen_item = rev_cands[0]
                        elif cands:
                            chosen_item = cands[0]
                        # Pass 2: fallback without strict must_include
                        if not chosen_item:
                            for it in items:
                                cand = it["Item"]
                                iname = cand.get("itemName", "")
                                if cand.get("itemPrice", 0) >= 500 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    if not any(ex.lower() in iname.lower() for ex in item.get("exclude", [])):
                                        chosen_item = cand
                                        break
                    if chosen_item:
                        break
                except urllib.error.HTTPError as e:
                    print(f"    HTTP Error {e.code}: {e.reason}")
                    time.sleep(2.5)
                except Exception as e:
                    print(f"    Error: {e}")
                    time.sleep(2.0)

            if chosen_item:
                img_url = extract_image_url(chosen_item)
                aff_url = chosen_item.get("affiliateUrl") or chosen_item.get("itemUrl")
                print(f"    -> MATCH: {chosen_item['itemName'][:65]} (¥{chosen_item['itemPrice']:,}, ★{chosen_item.get('reviewAverage')}/{chosen_item.get('reviewCount')}件)")
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": aff_url,
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": str(chosen_item.get("reviewAverage", "0.0"))
                })
                total_fetched += 1
            else:
                print(f"    ❌ FAILED for Rank {item['rank']}: {item['name']}")

    with open("fetched_3new_nov_dec_2026_1123.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nDone! Fetched {total_fetched}/30 items.")

if __name__ == "__main__":
    fetch_all()
