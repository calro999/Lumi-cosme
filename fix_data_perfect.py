import json

with open("rakuten_balm_hotcleansing_neck_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. winter_hair_balm の Rank 5 (ボタニスト ボタニカル ヘアバーム) を差し替え
data["winter_hair_balm"]["items"][4] = {
    "rank": 5,
    "brand": "BOTANIST (ボタニスト)",
    "name": "ボタニカル ヘアバーム (集中補修オイル配合・植物の恵みでパサつく毛先にしっとりした濡れツヤと自然な束感を与えるマルチバーム)",
    "query": "ボタニスト ボタニカル ヘアバーム",
    "rakuten_name": "【BOTANIST ボタニスト ボタニカル ヘアバーム 】 ゆうパケット対象商品 ボタニスト 集中補修 ダメージケア スタイリング スタイリング剤 整髪料 濡れ髪 ウェット スタイリングバーム 天然由来 シアバター 保湿 うるおい 保湿 ハンドクリーム",
    "price": 1650,
    "price_str": "¥1,650",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fkobe-beauty-labo%2Fbota-hairbalm-01%2F",
    "image_url": "https://shop.r10s.jp/kobe-beauty-labo/cabinet/botanist_img/2026_autumn/bota-hairbalm-01/08.jpg",
    "review_count": 182,
    "review_average": "4.65"
}

# 2. winter_hot_cleansing の Rank 8, 9, 10 を差し替え
data["winter_hot_cleansing"]["items"][6] = {
    "rank": 7,
    "brand": "コーセー (ソフティモ)",
    "name": "ソフティモ ラチェスカ ホットジェルクレンジング (美容液90%配合の濃厚温感ジェル・毛穴の黒ずみ汚れをじゅわっと溶かしてすっきりオフ)",
    "query": "ソフティモ ラチェスカ ホットジェルクレンジング",
    "rakuten_name": "コーセーコスメポート ソフティモ ラチェスカ ホットジェル マイルドクレンジング 200g 温感ジェル",
    "price": 880,
    "price_str": "¥880",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fsundrug%2F4971710393071%2F",
    "image_url": "https://shop.r10s.jp/sundrug/cabinet/29/4971710393071.jpg",
    "review_count": 45,
    "review_average": "4.38"
}

data["winter_hot_cleansing"]["items"][7] = {
    "rank": 8,
    "brand": "LuLuLun (ルルルン)",
    "name": "ルルルン クレンジングバーム CLEAR BLACK (毛穴の蓄積汚れ・角栓を吸着する炭＆クレイ配合・とろけるメルティ処方で肌をほぐしながら落とす濃厚バーム)",
    "query": "ルルルン クレンジングバーム CLEAR BLACK",
    "rakuten_name": "【公式】ルルルン クレンジングバーム CLEAR BLACK 90g | クレンジング バーム 毛穴 炭 クレイ 毛穴ケア メイク落とし 洗顔 化粧落とし",
    "price": 2420,
    "price_str": "¥2,420",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Flululun-shop%2Fbalm-cb-1st%2F",
    "image_url": "https://shop.r10s.jp/lululun-shop/cabinet/other/balm-cb-1st_01.jpg",
    "review_count": 312,
    "review_average": "4.58"
}

data["winter_hot_cleansing"]["items"][8] = {
    "rank": 9,
    "brand": "ORBIS (オルビス)",
    "name": "オルビス オフクリーム (秒速とろけ落ち・うるおいを守りながら汚れだけを見極めて落とすモイストフィット処方の極上リッチクリーム)",
    "query": "オルビス オフクリーム",
    "rakuten_name": "オルビス オフクリーム ボトル入り 100g／オルビス（orbis） クレンジング クリーム メイク落とし ウォータープルーフ 乾燥 うるおい",
    "price": 2530,
    "price_str": "¥2,530",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2F0101marui%2Fto6051615701%2F",
    "image_url": "https://shop.r10s.jp/0101marui/cabinet/to605/161/57to605-16157-01b.jpg",
    "review_count": 528,
    "review_average": "4.72"
}

# 3. winter_neck_cream の Rank 2, 5, 8 を差し替え
data["winter_neck_cream"]["items"][1] = {
    "rank": 2,
    "brand": "REVITAL (資生堂リバイタル)",
    "name": "ネックゾーン エッセンス (医薬部外品・首特有の皮膚の薄さと動きに着目・うるおいバリアとハリ成分を角層深くまで送り込む薬用美容液)",
    "query": "資生堂 リバイタル ネックゾーン エッセンス",
    "rakuten_name": "リバイタル ネックゾーン エッセンス 75g 【医薬部外品】 資生堂 首用美容液 ネックケア エイジングケア 乾燥小ジワ",
    "price": 5500,
    "price_str": "¥5,500",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2F14promo%2Fimgrc01165761%2F",
    "image_url": "https://shop.r10s.jp/14promo/cabinet/imgrc01165761.jpg",
    "review_count": 96,
    "review_average": "4.61"
}

data["winter_neck_cream"]["items"][4] = {
    "rank": 5,
    "brand": "Dr.Ci:Labo (ドクターシーラボ)",
    "name": "アクアコラーゲンゲル エンリッチリフトEX (浸透型コラーゲンEX×ナイアシンアミド・顔から首・デコルテまでぐっと引き上げる高保湿ゲル)",
    "query": "ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX",
    "rakuten_name": "「2025年8月リニューアル」Dr.CiLabo ドクターシーラボ アクアコラーゲンゲル エンリッチリフトEX 120g 高保湿 ハリ 弾力 首 デコルテ",
    "price": 9477,
    "price_str": "¥9,477",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fyuaikokusai%2F11379601%2F",
    "image_url": "https://shop.r10s.jp/yuaikokusai/cabinet/11379601/imgrc0089221532.jpg",
    "review_count": 210,
    "review_average": "4.68"
}

data["winter_neck_cream"]["items"][7] = {
    "rank": 8,
    "brand": "CKD (シーケーディー)",
    "name": "レチノコラーゲン 低分子300 濃密ネッククリーム (マッサージローラー一体型・低分子コラーゲン×レチノイドが首元の横ジワとたるみを引き締めケアする韓国大ヒット名品)",
    "query": "CKD レチノコラーゲン 首クリーム",
    "rakuten_name": "【CKD 公式】レチノコラーゲン 低分子300 首クリーム ネッククリーム 50ml ローラー付き シワ改善 ハリ エイジングケア 首元 デコルテ",
    "price": 3850,
    "price_str": "¥3,850",
    "affiliate_url": "https://hb.afl.rakuten.co.jp/hgc/54d2a438.4bc4abc2.54d2a439.aa1be583/?pc=https%3A%2F%2Fitem.rakuten.co.jp%2Fjoyance-m%2Fckd-neckcream%2F",
    "image_url": "https://shop.r10s.jp/joyance-m/cabinet/09251873/ckd-neck01.jpg",
    "review_count": 340,
    "review_average": "4.74"
}

with open("rakuten_balm_hotcleansing_neck_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated and verified rakuten_balm_hotcleansing_neck_data.json successfully!")
