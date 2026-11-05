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
    "winter_olive_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！高純度オレイン酸と植物スクワレンが真冬の粉吹き肌とあかぎれ手肌をしっとり潤す高保湿オリーブオイルコスメランク10",
        "file": "winter-olive-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["DHC オリーブバージンオイル 30ml", "DHC オリーブバージンオイル"],
                "brand": "DHC (ディーエイチシー)",
                "name": "DHC オリーブバージンオイル 30ml (スペイン産有機栽培オリーブ果実のフロール・デ・アセイテ/圧搾前の一滴のみを凝縮・天然の皮脂膜を補い真冬の粉吹き・肌荒れを1滴で防護する美容オイルの金字塔)"
            },
            {
                "rank": 2,
                "queries": ["オリーブマノン バージンオイル 200ml", "オリーブマノン バージンオイル"],
                "brand": "オリーブマノン (日本オリーブ)",
                "name": "オリーブマノン バージンオイル 200ml (100%純粋オリーブオイル・無添加・岡山牛窓自社農園の歴史ある伝統製法・真冬の洗顔後のブースターから全身の粉吹き・ひび割れケア、頭皮クレンジングまで万能に潤す大容量オイル)"
            },
            {
                "rank": 3,
                "queries": ["日本オリーブ オリーブマノン うるおいホワイトパック", "オリーブマノン うるおいホワイトパック"],
                "brand": "オリーブマノン (日本オリーブ)",
                "name": "オリーブマノン うるおいホワイトパック 150g (オリーブ油×植物スクワラン×トウキ根エキス配合・湯船に浸かりながら真冬の強張った角層を蒸しパック・くすみと乾燥を瞬時に取り去りもっちり透明肌へ導くクリームパック)"
            },
            {
                "rank": 4,
                "queries": ["オリーブ園 バージンオリーブオイル", "小豆島 オリーブ園 バージンオリーブオイル"],
                "brand": "小豆島オリーブ園 (Oliveen)",
                "name": "小豆島オリーブ園 バージンオリーブオイル 80ml (小豆島特産・高純度精製オリーブ油100%・さらりとしたテクスチャーで角質層に素早く馴染み、真冬の冷風でささくれ立った手肌やかかとをしっとり柔軟化)"
            },
            {
                "rank": 5,
                "queries": ["DHC 薬用ディープクレンジングオイル 200ml", "DHC ディープクレンジングオイル"],
                "brand": "DHC (ディーエイチシー)",
                "name": "薬用ディープクレンジングオイル (L) 200ml (高純度オリーブバージンオイル×ローズマリー配合・医薬部外品・冬の頑固な毛穴汚れや角栓を油分で浮かせつつ、洗い流した後の肌の水分蒸散を防ぎしっとり保つ最高峰クレンジング)"
            },
            {
                "rank": 6,
                "queries": ["パックスオリー ヘアオイル 60ml", "パックスオリー ヘアオイル"],
                "brand": "パックスオリー (PAX Olie / 太陽油脂)",
                "name": "パックスオリー ヘアオイル 60ml (オリーブ油×オリーブスクワラン×マカデミアナッツ油配合・真冬の乾燥でパサつく毛先に自然なまとまりとツヤを与え、乾燥頭皮のマッサージオイルとしても使える無添加ヘアオイル)"
            },
            {
                "rank": 7,
                "queries": ["オリーブマノン エクセレントホワイト エッセンス", "オリーブマノン エッセンス"],
                "brand": "オリーブマノン (日本オリーブ)",
                "name": "オリーブマノン エクセレントホワイト エッセンス 30ml (薬用美白・高保湿美容液・オリーブ果実油×持続型ビタミンC誘導体配合・冬の寒冷血行不良によるくすみを晴らし、乾燥による小ジワを目立たなくする濃密エッセンス)"
            },
            {
                "rank": 8,
                "queries": ["井上誠耕園 美容オリーブオイル", "井上誠耕園 美容オリーブオイル 30ml"],
                "brand": "井上誠耕園 (Inoue Seikoen)",
                "name": "井上誠耕園 美容オリーブオイル 30ml (小豆島のオリーブ農家が丹精込めて精製・人の皮脂と極めて近いオレイン酸トリグリセリドが冬の乾燥肌にスッと馴染み、ふっくら吸い付くようなハリとツヤを取り戻す化粧用オイル)"
            },
            {
                "rank": 9,
                "queries": ["クナイプ ビオ オイル 100ml", "クナイプ ビオ オイル"],
                "brand": "Kneipp (クナイプ)",
                "name": "クナイプ ビオ オイル 100ml (オーガニック認証・高純度オリーブオイル×グレープフルーツ果皮油配合・冬の乾燥でキメが乱れた顔や身体の角質層を柔らかくほぐし、全身にフレッシュな潤いを行き渡らせるフェイス＆ボディオイル)"
            },
            {
                "rank": 10,
                "queries": ["DHC 薬用リップクリーム", "DHC 薬用リップクリーム 1.5g"],
                "brand": "DHC (ディーエイチシー)",
                "name": "DHC 薬用リップクリーム 1.5g (医薬部外品・オリーブバージンオイル×アロエエキス×甘草誘導体配合・真冬の乾燥や冷風による唇の皮むけ・ひび割れを濃密な保護膜で防ぎ、ひと塗りで一日中ぷるぷる感を保つ殿堂入りリップ)"
            }
        ]
    },
    "winter_meadowfoam_oil": {
        "title": "保湿力の強さで肌乾燥とさようなら！熱を味方にする密着エモリエント膜が真冬のパサつく髪とカサつく角層を徹底修復する高保湿メドウフォーム油コスメランク10",
        "file": "winter-meadowfoam-oil.html",
        "items": [
            {
                "rank": 1,
                "queries": ["リファ ロックオイル 100ml", "リファ ロックオイル"],
                "brand": "ReFa (リファ / MTG)",
                "name": "リファ ロックオイル 100ml (メドウフォーム-δ-ラクトン高配合・熱を味方にして真冬のアイロン・ドライヤーダメージからキューティクルを補修し、一日中しっとり艶やかなカールとまとまりをロックする殿堂入りヘアオイル)"
            },
            {
                "rank": 2,
                "queries": ["ナプラ N. シアオイル 150ml", "エヌドット シアオイル 150ml"],
                "brand": "napla (ナプラ / N.)",
                "name": "N. (エヌドット) シアオイル 150ml (メドウフォーム油×シアバター×アルガンオイル配合・サラリとした超軽量テクスチャーでありながら、冬の暖房乾燥でパサつく髪の芯まで潤いを満たしてサラサラしなやかに整えるアウトバスオイル)"
            },
            {
                "rank": 3,
                "queries": ["ハホニコ 十六油 120ml", "ハホニコ ジュウロクユ 120ml"],
                "brand": "HAHONICO (ハホニコ)",
                "name": "プロッフェショナル 十六油 (ジュウロクユ) 120ml (メドウフォーム油をはじめとする厳選16種の天然オイル配合・ドライヤーの熱で毛髪アミノ酸と架橋結合し、真冬の乾燥・静電気・枝毛を強力にブロックするプロ仕様ヘアオイル)"
            },
            {
                "rank": 4,
                "queries": ["ルベル シーソー クリアオイル", "SEE SAW クリアオイル フラット"],
                "brand": "LebeL (ルベル / SEE SAW)",
                "name": "SEE/SAW クリアオイル ♭ (フラット) 80ml (メドウフォーム油×スクワラン配合・光を味方にして冬のパサつくくせ毛やうねりをなめらかに落ち着かせ、毛先までストンとまとまるやわらかな艶髪へ導くサロン専売オイル)"
            },
            {
                "rank": 5,
                "queries": ["エルジューダ サントリートメント セラム 120ml", "ミルボン エルジューダ サントリートメント セラム"],
                "brand": "MILBON (ミルボン / エルジューダ)",
                "name": "エルジューダ サントリートメント セラム 120ml (メドウフォーム油×バオバブオイル配合・冬の紫外線ダメージと乾燥からキューティクルを守り、潤いを与えて滑らかな指通りを一日中持続させる濃密ヘアセラム)"
            },
            {
                "rank": 6,
                "queries": ["COA GINZA フレグランス ヘアオイル", "COA GINZA フレグランスオイル 50ml"],
                "brand": "COA GINZA (コア ギンザ)",
                "name": "COA GINZA フレグランスプレミアムヘアオイル 50ml (銀座トップサロン開発・メドウフォームラクトン×植物オイル高配合・熱反応で冬のパサつき・広がりをリセットし、洗練された高級香水の香りで一日中髪を包み込むトリートメントオイル)"
            },
            {
                "rank": 7,
                "queries": ["オッジィオット セラムCMCオイル 100ml", "oggi otto セラムCMCオイル"],
                "brand": "oggi otto (オッジィオット)",
                "name": "セラムCMCオイル 100ml (高濃度メドウフォーム油×アルガン油×セラミド配合・毛髪内部のCMC脂質をダイレクトに補修・真冬の深刻なハイダメージ毛や静電気で絡まる毛先をしなやかな絹の質感へ変える補修オイル)"
            },
            {
                "rank": 8,
                "queries": ["アンドハニー ディープモイスト ヘアオイル 100ml", "アンドハニー ディープモイスト ヘアオイル"],
                "brand": "&honey (アンドハニー)",
                "name": "ディープモイスト ヘアオイル 3.0 100ml (メドウフォーム油×ハチミツ×プロポリス配合・水分量14%に着目した超高保湿処方・真冬のパサつく髪を甘くみずみずしい潤いヴェールで満たし毛先までしっとりまとめる濃密オイル)"
            },
            {
                "rank": 9,
                "queries": ["トラック オイル ナンバースリー 90ml", "トラックオイル No.3 90ml"],
                "brand": "track (トラック)",
                "name": "track oil No.3 (トラックオイル ナンバースリー) 90ml (メドウフォーム油×オリーブ果実油×金木犀精油配合・真冬の乾燥で広がる剛毛・ハイダメージ毛を濃密な植物膜でしっとりまとめ、手肌の保湿バームとしても使える大人気マルチオイル)"
            },
            {
                "rank": 10,
                "queries": ["自然化粧品研究所 メドウフォームオイル", "&SH メドウフォームオイル 100ml", "メドウフォームオイル 100ml"],
                "brand": "自然化粧品研究所 / &SH",
                "name": "ピュア メドウフォームオイル 100ml (高純度精製・長鎖脂肪酸が豊富で極めて高い酸化安定性を誇るピュア美容オイル・真冬の手持ちクリームへの添加や手作りバーム、ドライヤー前のプレオイルとして幅広く活躍)"
            }
        ]
    },
    "winter_trehalose": {
        "title": "保湿力の強さで肌乾燥とさようなら！細胞を脱水から守る驚異の保水糖が真冬のカラカラ砂漠肌とインナードライを満たし続ける高保湿トレハロースコスメランク10",
        "file": "winter-trehalose.html",
        "items": [
            {
                "rank": 1,
                "queries": ["アクセーヌ モイストバランスローション 360ml", "アクセーヌ モイストバランスローション"],
                "brand": "ACSEINE (アクセーヌ)",
                "name": "モイストバランス ローション 360ml (超微細ナノカプセル×トレハロース配合・角質細胞の隙間より小さいナノカプセルが角層の奥深くまで浸透・一日中乾きを知らないみずみずしい透明肌を維持する敏感肌・乾燥肌の最高峰化粧水)"
            },
            {
                "rank": 2,
                "queries": ["ちふれ 集中保湿美容液", "ちふれ 集中保湿美容液 N"],
                "brand": "CHIFURE (ちふれ)",
                "name": "集中保湿美容液 N 45ml (トレハロース×ヒアルロン酸高配合・ノンアルコール・無香料・真冬の暖房乾燥でカサつく目元や口元をみずみずしい水分クッションで満たし、ふっくら吸い付くような肌に整える高コスパ濃密美容液)"
            },
            {
                "rank": 3,
                "queries": ["菊正宗 日本酒の化粧水 高保湿", "菊正宗 日本酒の化粧水 高保湿 500ml"],
                "brand": "菊正宗 (KIKUMASAMUNE)",
                "name": "日本酒の化粧水 高保湿 500ml (コメ発酵液×トレハロース×セラミド×アミノ酸配合・酒蔵の天然保湿因子が真冬の全身乾燥肌にぐんぐん浸透・とろみのあるテクスチャーで顔からデコルテ、脚までたっぷり潤す大容量化粧水)"
            },
            {
                "rank": 4,
                "queries": ["ファンケル モイストリファイン 化粧液", "ファンケル モイストリファイン"],
                "brand": "FANCL (ファンケル)",
                "name": "モイストリファイン 化粧液 II しっとり 30ml (トレハロース誘導体×VPエキス配合・肌の内側がカラカラに乾くインナードライに直接アプローチ・真冬のキメ乱れと開き毛穴をふっくら潤いで引き締める無添加化粧液)"
            },
            {
                "rank": 5,
                "queries": ["オルビス アクアニスト ローション", "オルビス アクアニスト ローション RM"],
                "brand": "ORBIS (オルビス)",
                "name": "アクアニスト ローション RM (しっとり高保湿) 180ml (植物性トレハロース×持続型アミノ酸配合・敏感肌特有のうるおい低下スパイラルを断ち切り、真冬の刺激を受けやすい肌を健やかに育む低刺激高保湿ローション)"
            },
            {
                "rank": 6,
                "queries": ["カバーマーク セルアドバンスト ローション", "カバーマーク セルアドバンスト ローション WS"],
                "brand": "COVERMARK (カバーマーク)",
                "name": "セルアドバンスト ローション WS 150ml (ナノサイズトレハロース誘導体×クスノハガシワエキス配合・角質層のすみずみまで浸透して真冬の深刻なゴワつき肌に濃密なハリと弾力をみなぎらせる最高峰エイジングケア化粧水)"
            },
            {
                "rank": 7,
                "queries": ["セタフィル モイスチャライジング ローション 591ml", "セタフィル モイスチャライジングローション"],
                "brand": "Cetaphil (セタフィル / ガルデルマ)",
                "name": "モイスチャライジング ローション 591ml (トレハロース×ナイアシンアミド×パンテノール配合・皮膚科医推奨のモイスチャーバリア処方・真冬の粉吹き肌やすねのかゆみ、家族全員の乾燥肌を優しく守る大容量高保湿乳液)"
            },
            {
                "rank": 8,
                "queries": ["イニスフリー グリーンティー シード セラム", "イニスフリー グリーンティーシード ヒアルロン セラム"],
                "brand": "innisfree (イニスフリー)",
                "name": "グリーンティーシード ヒアルロン セラム 80ml (茶葉エキス×トレハロース×カプセルヒアルロン酸配合・洗顔後すぐのまっさらな肌に潤いの道を通し、真冬のブースター美容液として水分保持力を劇的に高める導入美容液)"
            },
            {
                "rank": 9,
                "queries": ["メディヒール ティーツリーケア ソリューション", "メディヒール ティーツリー エッセンシャルマスク"],
                "brand": "MEDIHEAL (メディヒール)",
                "name": "ティーツリー ケアソリューション エッセンシャルマスク 10枚 (トレハロース×ティーツリー抽出油×ツボクサエキス配合・冬の寒暖差やマスク摩擦で荒れやすい角層を鎮静しながら、トレハロースの濃密水分ヴェールで潤すレスキューシートマスク)"
            },
            {
                "rank": 10,
                "queries": ["トレハロース パウダー 100g", "自然化粧品研究所 トレハロース", "トレハロース 化粧品 100g"],
                "brand": "自然化粧品研究所 / &SH",
                "name": "高純度トレハロース パウダー 100g (天然由来・化粧品原料グレード・水に溶かすだけで驚異の保水化粧水が完成・真冬の手持ち化粧水の保湿力ブーストや手作りフェイスパックに重宝する純粋保水パウダー)"
            }
        ]
    }
}

def fetch_all():
    results = {}
    for cat_key, cat_data in CATEGORIES.items():
        print(f"\n==========================================")
        print(f"Fetching category: {cat_key} ({cat_data['title'][:30]}...)")
        print(f"==========================================")
        results[cat_key] = {
            "title": cat_data["title"],
            "file": cat_data["file"],
            "items": []
        }
        for item in cat_data["items"]:
            chosen_item = None
            for q in item["queries"]:
                print(f"Rank {item['rank']}: Trying '{q}' ...")
                encoded_q = urllib.parse.quote(q)
                url = f"https://openapi.rakuten.co.jp/ichibams/api/IchibaItem/Search/20260401?applicationId={APP_ID}&accessKey={ACCESS_KEY}&affiliateId={AFF_ID}&keyword={encoded_q}&hits=5&format=json&sort=standard"
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
                
                for attempt in range(3):
                    try:
                        time.sleep(2.5) # レートリミット回避
                        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
                            data = json.loads(res.read().decode('utf-8'))
                            items = data.get("Items", [])
                            for it in items:
                                cand = it["Item"]
                                price = cand.get("itemPrice", 0)
                                if price >= 300 and (cand.get("mediumImageUrls") or cand.get("smallImageUrls")):
                                    chosen_item = cand
                                    break
                            if chosen_item:
                                break
                    except Exception as e:
                        print(f"  Attempt {attempt+1} error: {e}")
                        time.sleep(3.5)
                
                if chosen_item:
                    print(f"  -> Found: {chosen_item['itemName'][:40]} (¥{chosen_item['itemPrice']:,})")
                    break

            if chosen_item:
                img_url = ""
                if chosen_item.get("mediumImageUrls"):
                    img_url = chosen_item["mediumImageUrls"][0]
                elif chosen_item.get("smallImageUrls"):
                    img_url = chosen_item["smallImageUrls"][0]
                
                if "?_ex=" in img_url:
                    img_url = img_url.split("?_ex=")[0] + "?_ex=400x400"
                
                results[cat_key]["items"].append({
                    "rank": item["rank"],
                    "brand": item["brand"],
                    "display_name": item["name"],
                    "item_name": chosen_item["itemName"],
                    "price": chosen_item["itemPrice"],
                    "affiliate_url": chosen_item.get("affiliateUrl", chosen_item.get("itemUrl")),
                    "image_url": img_url,
                    "review_count": chosen_item.get("reviewCount", 0),
                    "review_average": chosen_item.get("reviewAverage", "0.0")
                })
            else:
                print(f"❌ Failed to fetch rank {item['rank']} for {cat_key}!")
    
    with open("fetched_3new_olive_meadowfoam_trehalose.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nSaved all items to fetched_3new_olive_meadowfoam_trehalose.json!")

if __name__ == "__main__":
    fetch_all()
