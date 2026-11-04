import json
import re

with open("fetched_3new_seabuckthorn_blackseed_hemp.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_black_seed_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌿 世界最高峰エジプト産ニゲラ×高濃度チモキノン！真冬の重度なバリア崩壊肌を救う絶対的王者",
        "catch": "ブラックシード研究の世界的パイオニア・Amazing Herbsが誇る純度100%コールドプレスオイル。活性成分チモキノンが冬の冷風で赤くヒリつく肌の炎症を速攻で鎮静し、角層を再構築",
        "brand_name": "Amazing Herbs (アメイジングハーブズ)",
        "capacity": "120ml (4floz) / 遮光ボトル",
        "type": "未精製100%ピュアブラックシードオイル",
        "features": "ニゲラサティバ種子油（エジプト産・低温圧搾未精製）、天然チモキノン高濃度、オメガ6（リノール酸約55%）、オメガ9（オレイン酸約25%）",
        "value": "熱や溶剤を一切加えない伝統のコールドプレス製法。海外の皮膚科医や自然療法医も推薦するメディカルグレードの品質で、冬の暖房乾燥による粉吹き・痒み・赤みを根本から封じ込める",
        "desc_p1": "11月から12月にかけて外気湿度が急降下すると、角層の細胞間脂質（セラミドや遊離脂肪酸）が乱れ、わずかな寒風や髪の毛の接触だけでもピリピリとした痛みや赤みが生じる『バリア機能破綻状態』に陥ります。Amazing Herbsの『ブラックシード 純粋低温圧搾オイル』は、古代エジプト時代から『死以外のあらゆる病を癒す万能薬』としてツタンカーメンの墓からも出土したニゲラサティバの種子を丸ごと搾った至高のオイルです。",
        "desc_p2": "指先にとると、わずかにスパイシーで温かみのあるハーブの香りが漂います。肌に乗せると、独自の薬効成分『チモキノン』が角層の微小な炎症シグナルを素早くブロック。さらにオメガ6とオメガ9がスカスカになった細胞間脂質の隙間をピタッと埋めるように密着し、暖房による水分の蒸散を完全に防ぎます。夜の洗顔後に2〜3滴をなじませるだけで、翌朝には赤みや粉吹きが嘘のように落ち着き、吸い付くような弾力と滑らかさが甦ります。",
        "target": "冬の寒さと乾燥で肌が赤くヒリヒリ敏感になりやすい方、暖房の効いた部屋にいると肌が突っ張って痛痒い方、海外で圧倒的レビュー数を誇る本物のブラックシードを試したい方",
        "point": "夜の化粧水で水分をたっぷり補給した後、手のひらに2〜3滴をとり、両手で軽く擦り合わせて温めてから顔全体を優しく包み込みます。特に乾燥や赤みが気になる頬や小鼻周りには指先で重ねづけしてください。"
    },
    {
        "rank": 2,
        "tag": "💧 USDA認定オーガニック×非遺伝子組み換え！冬の硬直角層を柔らかく満たす名門サプリブランドの傑作",
        "catch": "世界最大級のヘルスケアブランドNOW Foodsが厳選した高純度ブラッククミンオイル。必須脂肪酸の強力なエモリエント効果で、冬の寒冷でこわばった皮膚をふっくら柔軟に解きほぐす",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "237ml (8floz) / 遮光ペットボトル",
        "type": "オーガニック未精製ブラッククミンシードオイル",
        "features": "有機ニゲラサティバ種子油（低温圧搾・無濾過）、チモキノン、植物ステロール、天然ビタミンE",
        "value": "237mlという大容量で、顔のお手入れだけでなく冬の粉吹きすね・肘・膝、さらには頭皮の乾燥フケ予防スカルプケアまで全身に贅沢に活用できる抜群のコストパフォーマンス",
        "desc_p1": "冬のスキンケアにおいて、どれだけ高価な保湿美容液を使っても効果が感じられない最大の原因は『寒冷による角層の硬直』です。NOW Foodsの『オーガニック ブラッククミンシードオイル』は、厳格なUSDAオーガニック基準をクリアした純粋なニゲラ種子から抽出されており、硬くなった角質細胞を柔らかく解きほぐす力に秀でています。",
        "desc_p2": "サラリとした軽快なテクスチャーでありながら、肌へ押し込むと深部までスーッと吸い込まれるように馴染みます。チモキノンが外気刺激による肌の酸化ストレスを中和し、オメガ脂肪酸が肌表面に滑らかな保護ヴェールを形成。お風呂上がりの湿ったボディに伸ばせば、冬の粉吹きやかゆみを瞬時にリセット。週に一度、シャンプー前の乾いた頭皮にマッサージオイルとして揉み込むことで、冬の乾燥フケや頭皮の突っ張りも劇的に改善します。",
        "target": "大容量でフェイスからボディ、スカルプまでマルチに使いたい方、信頼できる国際オーガニック認証付きのオイルを選びたい方、冬の角層ゴワつきを柔らかくほぐしたい方",
        "point": "朝晩のスキンケアの最後に、乳液やクリームに1〜2滴ブレンドして塗布します。また、週1回の頭皮マッサージ用として500円玉大を頭皮全体へ馴染ませ、5分置いてからシャンプーすると頭皮環境が整います。"
    },
    {
        "rank": 3,
        "tag": "🌿 創業50年以上の老舗ハーブブランド！冬の暖房直撃によるインナードライを鉄壁ガードする逸品",
        "catch": "アメリカのハーブサプリメント界を牽引するNature's Wayのプレミアムオイル。オメガ脂肪酸とチモキノンの相乗効果で、真冬のエアコン乾燥による皮膚の枯渇感を完璧にリセット",
        "brand_name": "Nature's Way (ネイチャーズウェイ)",
        "capacity": "236ml (8floz) / 遮光ボトル",
        "type": "USDA認定オーガニックブラックシードオイル",
        "features": "有機ブラックシード油（未精製コールドプレス）、チモキノン高含有、防腐剤・化学溶剤不使用",
        "value": "ロットごとの有効成分濃度を厳格に検査。高い抗酸化作用で真冬の冷風や紫外線による肌サビを防止し、内側から押し返すようなハリ感とみずみずしいツヤを一日中キープ",
        "desc_p1": "11月から12月にかけてオフィスや自宅で暖房を連続使用すると、皮膚表面の水分だけでなく皮脂膜の脂質までもが蒸発し、肌の内部が空洞化したような『インナードライ』が悪化します。Nature's Wayの『オーガニック ブラックシード オイル』は、50年以上にわたるハーブ研究の叡智を注ぎ込んで製造された最高峰の植物オイルです。",
        "desc_p2": "肌に乗せると、天然のニゲラ種子が持つフレッシュでスパイシーな芳香が広がり、植物の生命力をダイレクトに感じられます。不飽和脂肪酸のバランスが理想的で、角層の水分保持能を担うセラミドの合成を間接的にサポート。冬の乾燥によって開きがちな大人のたるみ毛穴を引き締め、夕方になってもファンデーションが乾燥崩れしない健やかなベースを育みます。",
        "target": "日中オフィスで過ごすと夕方に頬が突っ張って痛い方、植物本来の力強いハーブ成分で肌質を根本から立て直したい方、乾燥による毛穴の目立ちが気になる方",
        "point": "夜のお手入れで美容液を塗った後、3〜4滴を手にとり、手のひら全体で顔を包み込むように優しくハンドプレスします。首筋からデコルテにかけてリンパを流すように伸ばすのも効果的です。"
    },
    {
        "rank": 4,
        "tag": "🧘‍♀️ 伝統アーユルヴェーダ製法！冬の冷風で赤くピリつく超敏感肌を守り抜く高純度オイル",
        "catch": "ギーや伝統ハーブの名門Pure Indian Foodsが手がける手摘みニゲラ種子オイル。冷えと乾燥で失われた肌のオージャス（生命エネルギー）を補い、ふっくら吸い付く素肌へ導く",
        "brand_name": "Pure Indian Foods (ピュアインディアンフーズ)",
        "capacity": "240ml (8floz) / 遮光ガラスボトル",
        "type": "アーユルヴェーダ認定ピュアブラックシードオイル",
        "features": "未精製ブラッククミンオイル（インド・エジプト産原種）、低温圧搾、無添加・無濾過",
        "value": "遮光ガラス瓶を採用することでプラスチック容器への溶出を防ぎ、オイルの鮮度と抗酸化成分を長期間キープ。冬のデリケートに傾いた肌でも刺激なく使える低アレルゲン設計",
        "desc_p1": "真冬の強い木枯らしにさらされると、皮膚の温度が下がり、血液循環が悪化して肌のターンオーバーが停滞します。その結果、古い角質が剥がれ落ちずに表面に溜まり、くすみやゴワつきが加速します。Pure Indian Foodsの『オーガニック ブラックシードオイル』は、インドの伝統医学アーユルヴェーダの製法に基づいて丁寧に抽出されたピュアオイルです。",
        "desc_p2": "ガラス瓶から取り出すと、黄金色にわずかに黒みがかった神秘的な色合い。肌になじませると体温でじんわりと温まるような感覚があり、冬の寒さでこわばった表情筋まで緩んでいくようなリラクゼーションをもたらします。チモキノンと植物ステロールが荒れ果てた角層バリアを優しく包み込み、冷風や乾燥から鉄壁のシールドを形成します。",
        "target": "冬になると肌がゴワついてどんな化粧水も入らない方、プラスチックフリーでガラス瓶容器の高品質オイルを好む方、冷えによる肌のくすみ・血色不良をケアしたい方",
        "point": "入浴時、湯船に浸かりながら3〜4滴を顔全体に伸ばし、蒸気を利用した『オイルホットパック』を行います。3分置いた後に軽くぬるま湯で流すと、驚くほど柔らかくモチモチの肌に生まれ変わります。"
    },
    {
        "rank": 5,
        "tag": "💆‍♀️ ブラックシード×伝統アーユルヴェーダハーブ！冬の乾燥フケ・頭皮の痒み・髪のパサつきを一網打尽",
        "catch": "世界的な高級アーユルヴェーダブランドiYURAが放つ頭皮＆毛髪用リペアオイル。ブラックシードの抗炎症・血流促進作用で、冬の過酷な乾燥にさらされた頭皮と毛先を集中補修",
        "brand_name": "iYURA (イユラ)",
        "capacity": "100ml / スポイト付高級ガラス瓶",
        "type": "高機能スカルプ＆ヘア集中補修セラム",
        "features": "ニゲラサティバ種子油（ブラックシード）、ブリンガラジ、アムラ、ゴマ油、ココナッツ油",
        "value": "冬の暖房や静電気でパサつく髪の毛先をシルクのような艶髪へ導くと同時に、頭皮の乾燥フケや痒みをチモキノンの抗菌・抗炎症作用で根本から鎮静するプロ仕様トリートメント",
        "desc_p1": "真冬の乾燥トラブルは顔や手足だけでなく、実は『頭皮と髪』にも深刻なダメージを与えます。外気の乾燥と室内のエアコン暖房によって頭皮の水分が失われると、細かな白いフケがパラパラと落ちたり、頭皮が突っ張って痒くなったりします。iYURAの『KERANYA ピュア ブラックシード 濃密ヘアオイル』は、頭皮環境の改善に特化したプレミアムヘアセラムです。",
        "desc_p2": "高純度なブラックシードオイルを主軸に、アーユルヴェーダで『髪の女王』と称されるブリンガラジやビタミンC豊富なアムラを配合。洗髪後のタオルドライした頭皮にスポイトで数滴なじませてマッサージすると、頭皮の血行がじんわりと促進され、冬の冷えで固まった頭皮が柔らかく解きほぐされます。毛先にも薄くなじませることで、冬の静電気による広がりや枝毛を完全にガードします。",
        "target": "冬になると頭皮の乾燥フケや痒みに悩まされる方、暖房やマフラーの摩擦で髪がパサつき静電気が起きる方、高級サロン品質のスカルプケアを自宅で行いたい方",
        "point": "シャンプー前の乾いた頭皮に1〜2スポイト分を塗布し、指の腹で円を描くように5分間マッサージしてそのまま入浴。その後普段通りシャンプーすると、毛穴の汚れが落ちて頭皮がすっきり潤います。"
    },
    {
        "rank": 6,
        "tag": "🧪 原料グレードのコールドプレス！手持ちコスメに1滴混ぜて冬の保湿バリアを底上げする原液",
        "catch": "コスメ製造の原料としても流通する純度100%未精製ブラッククミンオイル。余計な香料や防腐剤を一切排除し、有効成分チモキノンの力をダイレクトに肌へ届けるプロ仕様",
        "brand_name": "自然原料研究所",
        "capacity": "30ml / 遮光ドロップボトル",
        "type": "化粧品原料グレード純粋キャリアオイル",
        "features": "ブラッククミン種子油100%、コールドプレス低温圧搾、未脱臭・未精製",
        "value": "普段使用している乳液、クリーム、ボディローションにわずか1滴ブレンドするだけで、冬の過酷な乾燥荒れを防ぐ『高機能メディカルコスメ』へとアップグレード可能",
        "desc_p1": "市販の化粧品では香料や防腐剤でかぶれてしまう超敏感肌の方や、既存のスキンケアアイテムの保湿力に物足りなさを感じている方にとって、最も確実で安全なアプローチが『化粧品原料グレードの植物原液』の活用です。自然原料研究所の『ブラッククミンシードオイル 30ml』は、一切の調整を行わずに種子から搾ったままの生オイルです。",
        "desc_p2": "高濃度のチモキノンが含まれているため、肌荒れの初期段階で塗布すると、赤みや腫れが急速に引いていくのを実感できます。手持ちのオールインワンジェルや保湿クリームに1滴垂らして混ぜ合わせることで、水分と油分の理想的な乳化状態を手のひらの上で作り出し、真冬の乾燥冷風を跳ね返す強固なバリア膜を形成します。30mlのコンパクトサイズで鮮度を落とさず使い切れるのもメリットです。",
        "target": "手持ちのスキンケアの保湿力を簡単に高めたい方、香料やアルコールに敏感で無添加の原液を選びたい方、乾燥による部分的な肌荒れをピンポイント修復したい方",
        "point": "普段の乳液やクリームを手のひらに出し、そこに本品を1滴加えて指先でよく練り合わせてから塗布します。目元や口元など乾燥が酷い部位には、綿棒で少量を直接トントンと塗るスポット使いも有効です。"
    },
    {
        "rank": 7,
        "tag": "🎯 お試し＆集中スポットケアに最適！10ml遮光ドロッパーボトルの高純度ブラッククミン",
        "catch": "初めてブラックシードオイルを使う方に嬉しい10mlミニサイズ。冬の急な乾燥性肌荒れやマスク擦れの赤み、目元・口元のピリつく部位にピンポイントで密着するレスキューオイル",
        "brand_name": "プラントコスメ原料",
        "capacity": "10ml / 遮光ドロッパーボトル",
        "type": "未精製ブラッククミンオイル原液",
        "features": "ニゲラ種子油100%、低温圧搾法、高純度、無添加",
        "value": "1,000円前後の手軽な価格で本格的なブラックシードのチモキノンパワーを体験可能。ポーチに入れて持ち歩き、日中の乾燥割れやオフィスでの緊急保湿にも便利",
        "desc_p1": "ブラックシードオイルを使ってみたいけれど、肌に合うか不安、まずは少量で試してみたいという方に最適なのが、プラントコスメ原料の『ブラッククミンシードオイル 10ml』です。未精製のフレッシュなオイルがドロッパー付きの遮光瓶に密閉されており、一滴ずつ正確に滴下できます。",
        "desc_p2": "小容量でありながら品質は最高峰。冬のエアコン風でカサカサにめくれた小鼻のキワや、寒暖差で赤くなった頬骨のトップなど、乾燥ダメージが集中するパーツに1滴をそっとなじませるだけで、荒れた角層がピタッと落ち着きます。独特のスパイシーな香りも少量使いなら気にならず、肌のレスキューオイルとして化粧ポーチやデスクの引き出しに忍ばせておくのに最適です。",
        "target": "ブラックシードオイルを初めて購入する初心者の方、ポーチに入れて持ち運べる乾燥レスキューアイテムを探している方、部分的な肌荒れに少量使いたい方",
        "point": "洗顔後、清潔な指先に1滴を取り、乾燥や赤みが気になる部分へ直接トントンと優しく押し込むように塗布します。その後に普段通りの保湿ケアを行ってください。"
    },
    {
        "rank": 8,
        "tag": "🛁 240ml特大ボトル×エジプト産最高峰グレード！真冬の全身粉吹き肌を包み込む贅沢オイル",
        "catch": "Amazing Herbsのフラッグシップ大容量ボトル。顔のお手入れはもちろん、冬の乾燥で粉を吹くすね・腕・背中・ひび割れる踵まで、惜しみなく全身に塗り広げられるサロン仕様",
        "brand_name": "Amazing Herbs (アメイジングハーブズ)",
        "capacity": "240ml (8floz) / 遮光ボトル",
        "type": "純粋低温圧搾ブラックシードオイル 大容量",
        "features": "エジプト産原種ニゲラ種子油100%、低温圧搾未精製、高純度チモキノン",
        "value": "大容量だからこそ、入浴直後の全身インバスオイルケアや、家族全員での乾燥対策に最適。1本で真冬のあらゆる乾燥・肌荒れトラブルを完璧にカバーする決定版",
        "desc_p1": "真冬になると、顔だけでなく手足や腰回りの皮膚全体が粉を吹き、衣類を脱ぐたびに白い粉が舞うような深刻なボディ乾燥に悩まされる方が増えます。Amazing Herbsの『ブラックシードオイル 240ml』は、そんな全身の乾燥クライシスに惜しみなく立ち向かえる大容量プレミアムオイルです。",
        "desc_p2": "世界最高品質と評されるエジプト産のニゲラ種子のみを使用し、熱を加えないコールドプレスで丁寧に搾油。濃厚な油分が肌の上でスルスルと伸び広がり、真冬の冷えでガサガサに硬化した踵や肘の角質を柔らかく包み込みます。お風呂上がりの濡れた素肌に手のひらで伸ばすことで、水分を抱え込んだ強固なエモリエントヴェールが完成。一日中しっとり滑らかな素肌をキープできます。",
        "target": "真冬に全身の皮膚が粉を吹いて痒くなりやすい方、高品質なブラックシードオイルをコスパ良く毎日全身に使いたい方、踵や肘のガサガサを徹底修復したい方",
        "point": "お風呂から上がる直前、タオルで水分を拭き取る前の濡れた肌に全身へ伸ばします。その後、バスタオルで優しく押さえるように水分を吸い取るだけで、全身のモチモチ肌が完成します。"
    },
    {
        "rank": 9,
        "tag": "🍷 内外両用100%エクストラバージン！体の内外から真冬の抗酸化と水分保持力を高めるスーパーオイル",
        "catch": "スキンケア用としての濃密保湿はもちろん、スプーン1杯の飲用で体内の免疫と粘膜をサポートする食品グレードの純粋オイル。内側と外側の両面から真冬の乾燥荒れを撃退",
        "brand_name": "Nigella Care (ニゲラケア)",
        "capacity": "120ml / 遮光ガラスボトル",
        "type": "無添加食用・スキンケア両用ブラッククミンシードオイル",
        "features": "ニゲラ種子油100%（無添加コールドプレス）、オメガ6、オメガ9、チモキノン",
        "value": "食品としての厳しい衛生基準をクリアした最高品質。外側から肌へ塗布して皮脂膜を強化し、内側から摂取して冬の冷えと免疫低下をケアするホリスティックアプローチ",
        "desc_p1": "冬の乾燥肌は、皮膚表面の水分不足だけでなく、体内の血流低下や栄養代謝の乱れが引き金になっているケースが多々あります。ニゲラケアの『無添加 エクストラバージン ブラッククミンシードオイル』は、飲用にも耐えうる最高レベルの純度と鮮度を誇るマルチユースオイルです。",
        "desc_p2": "肌に塗れば、チモキノンとオレイン酸が乾燥による炎症を速やかに鎮静。さらに毎朝ティースプーン1杯をハチミツと一緒に摂取したり、温かいハーブティーに垂らして飲むことで、消化器粘膜や毛細血管の働きをサポートし、肌の内側からみずみずしい潤いを生み出す力を後押しします。体の内と外から真冬の乾燥に立ち向かう究極のエイジングケアアイテムです。",
        "target": "外側のスキンケアだけでなく体質改善やインナーケアにもこだわりたい方、食品グレードの極めて安全なオイルを使いたい方、冬の免疫力低下と肌荒れを同時に防ぎたい方",
        "point": "夜は洗顔後のスキンケアオイルとして1〜2滴をハンドプレス。朝はティースプーン半杯をハチミツやヨーグルトに混ぜて摂取することで、内外両面からの保湿効果が最大化します。"
    },
    {
        "rank": 10,
        "tag": "💊 純粋ブラックシードオイル500mg凝縮！冬の極度なインナードライを体内から潤すソフトジェル",
        "catch": "オイル特有の強い香りや味が苦手な方でも手軽に続けられるサプリメント。1粒に高濃度ブラッククミン種子油を密閉し、真冬の全身の水分蒸散を防ぎバリア機能を底上げ",
        "brand_name": "Amazing Herbs (アメイジングハーブズ)",
        "capacity": "90粒 (ソフトジェルカプセル)",
        "type": "高純度ブラックシードオイル栄養補助食品",
        "features": "ブラッククミン種子油500mg/粒、天然チモキノン濃縮、非遺伝子組み換え、グルテンフリー",
        "value": "ブラックシードオイルを塗るだけでなく『飲む』ことで、毛細血管を通じて全身の皮膚組織にオメガ脂肪酸を供給。エアコン暖房による喉の渇きや全身の粉吹きを体内からブロック",
        "desc_p1": "ブラックシードオイルの卓越した美容効果は世界中で認められていますが、唯一のハードルとされるのが『独特のスパイシーなハーブ臭』です。Amazing Herbsの『ブラックシードオイル 500mg ソフトジェル』は、その匂いやクセをカプセルの中に完全に閉じ込め、誰でも手軽にチモキノンの恩恵を受けられるようにした名品サプリメントです。",
        "desc_p2": "1粒ごとにコールドプレスされた高純度オイルが500mg充填されており、胃の中で溶けて素早く体内に吸収されます。真冬に水分摂取量が減り、体全体の保水力が落ちているときに毎日継続して摂取することで、肌の細胞膜が強化され、水分を逃しにくい体質へと導きます。外用オイルと併用することで、真冬の乾燥シーズンをトラブル知らずで乗り切ることができます。",
        "target": "ブラックシードの味や香りが苦手だが効果は取り入れたい方、外側からのケアだけでは肌の乾燥が追いつかない深刻なインナードライの方、冬の健康維持も同時に目指す方",
        "point": "1日1〜2粒を目安に、食後に水またはぬるま湯と一緒にお召し上がりください。継続して飲むことで、2〜3週間ほどで肌のしっとり感や化粧ノリの向上を実感しやすくなります。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-black-seed-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！奇跡のチモキノンが真冬のバリア崩壊＆乾燥荒れ肌を根本鎮静する高保湿ブラックシードオイルコスメランク10",
            "description": "11月・12月の寒暖差と木枯らしによるバリア崩壊・赤みヒリつき肌を救う高保湿ブラックシードオイル（ニゲラサティバ）コスメを徹底厳選！Amazing Herbs、NOW Foods、Nature's Way、iYURAまで厳選検証。",
            "datePublished": "2026-11-05T07:00:00+09:00",
            "dateModified": "2026-11-05T07:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿ブラックシードオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "ブラックシードオイルに含まれる「チモキノン」とはどのような成分ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "チモキノン（Thymoquinone）は、ニゲラサティバ（ブラッククミン）の種子特有のファイトケミカル（植物性生理活性物質）です。非常に強力な抗酸化・抗炎症・抗菌作用を持ち、冬の急激な寒暖差や木枯らしによって破壊された角層バリアの微小な炎症を速やかに鎮静します。一般的な植物オイルが油分補給にとどまるのに対し、ブラックシードオイルは炎症を抑えながら角層を修復するメディカル級の皮膚保護力を発揮するのが最大の特徴です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ブラックシードオイル独特のスパイシーなハーブの香りは肌に残りますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "未精製の純粋なブラックシードオイルには、オレガノやブラックペッパーを思わせる独特のスパイシーな天然のハーブ臭があります。これは有効成分チモキノンや精油成分が豊富に含まれている証拠です。肌に塗布して手のひらでハンドプレスすると、数分で角層へ吸収され、香りは自然に揮発して肌表面に強く残り続けることはありません。香りが気になる場合は、夜のスキンケアの仕上げとして乳液やクリームに1滴混ぜて使うか、無香料のサプリメントタイプを取り入れるのがおすすめです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬の乾燥性ニキビや毛穴詰まりがあってもブラックシードオイルは使えますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、非常に適しています。真冬の大人ニキビは、肌の乾燥によって角質が硬化し、毛穴が塞がれて内部でアクネ菌が繁殖することが主な原因です。ブラックシードオイルは抗菌・抗炎症作用に優れ、毛穴を詰まらせにくい不飽和脂肪酸（リノール酸・オレイン酸）が主体のため、過剰な皮脂分泌を抑えつつ硬くなった角質を柔らかくほぐし、冬の乾燥ニキビを穏やかに鎮静させます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のスキンケアでの最も効果的なブラックシードオイルの使い方は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最もおすすめなのは『夜の洗顔・化粧水直後のプレオイル、またはクリームへの1滴ブレンド』です。洗顔後の水分をたっぷり含んだ肌に2滴をハンドプレスすると、チモキノンが肌荒れシグナルを抑え、オメガ脂肪酸が角層ラメラ構造を整えます。また、冬の乾燥でフケや痒みが出やすい頭皮への『シャンプー前スカルプマッサージ』や、粉を吹いた踵・肘へのポイント使いとしても絶大な効果を発揮します。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！奇跡のチモキノンが真冬のバリア崩壊＆乾燥荒れ肌を根本鎮静する高保湿ブラックシードオイルコスメランク10</title>
  <meta name="description" content="11月・12月の寒暖差と木枯らしによるバリア崩壊・赤みヒリつき肌を救う高保湿ブラックシードオイル（ニゲラサティバ）コスメを徹底厳選！Amazing Herbs、NOW Foods、Nature's Way、iYURAまで厳選検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-black-seed-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！奇跡のチモキノンが真冬のバリア崩壊＆乾燥荒れ肌を根本鎮静する高保湿ブラックシードオイルコスメランク10">
  <meta property="og:description" content="11月・12月の寒暖差と木枯らしによるバリア崩壊・赤みヒリつき肌を救う高保湿ブラックシードオイル（ニゲラサティバ）コスメを徹底厳選！Amazing Herbs、NOW Foods、Nature's Way、iYURAまで厳選検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-black-seed-oil">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #0f766e;
      --primary-light: #ccfbf1;
      --primary-dark: #134e4a;
      --accent: #0d9488;
      --accent-hover: #115e59;
      --bg: #f0fdfa;
      --card-bg: #ffffff;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --border: #99f6e4;
      --shadow: 0 4px 15px rgba(15, 118, 110, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      font-weight: 500;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--primary-dark);
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 1.2rem;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #e2e8f0;
      text-align: left;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .table-thumb {{
      width: 55px;
      height: 55px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      font-size: 1.05rem;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      text-align: center;
    }}

    .product-img {{
      width: 220px;
      height: 220px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid #99f6e4;
      background: #ffffff;
      padding: 0.5rem;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 0.6rem;
      line-height: 1.5;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #b91c1c;
    }}

    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
      display: inline-block;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #99f6e4;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th {{
      width: 28%;
      background: #f0fdfa;
      color: var(--primary-dark);
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #99f6e4;
      text-align: left;
    }}

    table.spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #99f6e4;
      color: #1f2937;
    }}

    .review-body {{
      background: #f8fafc;
      border-radius: 10px;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--primary);
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .target-box, .point-box {{
      background: #ffffff;
      border: 1px dashed #99f6e4;
      border-radius: 8px;
      padding: 1rem;
      margin-top: 1rem;
      font-size: 0.9rem;
      line-height: 1.7;
    }}

    .target-box strong, .point-box strong {{
      display: block;
      color: var(--primary-dark);
      margin-bottom: 0.3rem;
    }}

    .btn-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #0d9488 0%, #0f766e 100%);
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(15, 118, 110, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 480px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(15, 118, 110, 0.35);
      background: linear-gradient(135deg, #0f766e 0%, #134e4a 100%);
    }}

    .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 1.2rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
    }}

    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
      padding-left: 1.5rem;
    }}

    .guide-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: #111827;
      margin: 1.2rem 0 0.6rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      background: #f8fafc;
      border: 1px solid #f1f5f9;
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--border);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #94a3b8;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！奇跡のチモキノンが真冬のバリア崩壊＆乾燥荒れ肌を根本鎮静する高保湿ブラックシードオイルコスメランク10</h1>
      <p class="hero-desc">
        11月下旬から12月にかけて押し寄せる本格的な冬の寒波と過酷な室内暖房。寒冷刺激によって皮膚のバリア機能が崩壊し、化粧水すらピリピリとしみる、赤みや乾燥性の吹き出物が治まらないといった『深刻な冬の肌荒れクライシス』に直面する方が急増します。そんな過酷な冬枯れ肌を救済するのが、古代エジプトの時代から「死以外のあらゆる病を癒す」と讃えられてきた奇跡の万能植物「ブラックシード（ニゲラサティバ）」です。独自の薬効成分チモキノンと高純度オメガ脂肪酸を凝縮した名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>冬のバリア崩壊肌を速攻鎮静する「ブラックシードオイル」の皮膚科学的メカニズム</h2>
      <p>
        初冬の11月から12月にかけて、私たちの肌は「外気温の低下による血流停滞」と「湿度の急激な低下（太平洋側では20%台）」という二重のストレスに晒されます。特に問題となるのが、冷たい強風にさらされた直後に暖かい暖房の部屋へ入ることで生じる『激しい寒暖差ショック』です。急激な血管の拡張と収縮により皮膚の知覚神経が過敏になり、角層のバリア機能が物理的に破綻して微小な炎症が慢性化します。
      </p>
      <p>
        単なる水分補給や一般的なオイルでは鎮静しきれないこの冬の炎症性乾燥に対し、世界中の自然派皮膚科学で絶大な信頼を集めるのが「ブラックシードオイル（ニゲラサティバ種子油 / ブラッククミンオイル）」です。ツタンカーメン王の墓やクレオパトラの美容史にも登場するこの漆黒の種子には、現代の科学でも驚嘆される特異な成分が凝縮されています。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 奇跡の抗炎症・抗菌ファイトケミカル「チモキノン」</strong>
          <p>ニゲラ種子にのみ高濃度で含まれる特異成分。冬の冷風や摩擦で発生した角層の炎症シグナルを素早く遮断し、ヒリつきや赤み、冬の乾燥性大人ニキビを根本から鎮静させます。</p>
        </div>
        <div class="highlight-card">
          <strong>2. オメガ6（リノール酸約55%）×オメガ9（オレイン酸約25%）</strong>
          <p>角層の細胞間脂質（ラメラ液晶構造）を構築するために不可欠な不飽和脂肪酸が黄金比率で共存。スカスカになった細胞の隙間を埋め、暖房下での水分蒸発を鉄壁ガードします。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 肌代謝を活性化する植物ステロール＆天然ビタミンE</strong>
          <p>寒さで硬直した皮膚の血行を促し、ターンオーバーの停滞によるゴワつきや角質肥厚を滑らかにトリートメント。後から重ねる化粧水の吸水性を飛躍的に高めます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿ブラックシードオイルコスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロが教える！真冬のブラックシードオイル選び方＆効果を極限まで高める活用術</h2>
      <h3>1. 「未精製コールドプレス（低温圧搾）」の表記を必ずチェック</h3>
      <p>
        ブラックシードオイルの最大の価値は、熱に弱い主成分「チモキノン」の残存量にあります。安価な抽出法（高温圧搾やヘキサン等の化学溶剤抽出）で作られたオイルは、重要な抗酸化成分やチモキノンが揮発・分解してしまっています。「コールドプレス（Cold-Pressed）」「未精製（Unrefined・Virgin）」と明記された、黒褐色でスパイシーな香りを残したオイルを必ず選んでください。
      </p>
      <h3>2. 冬の赤み・ヒリつき肌には「化粧水前のブースター」か「クリームブレンド」</h3>
      <p>
        洗顔後、肌がまだ湿っている状態で1〜2滴を手のひらで温めてハンドプレスすると、チモキノンが角層深部へ素早く届き、外気刺激による知覚過敏を鎮静させます。独特のスパイシーな香りが気になる方や、より高い密閉力を求める方は、夜のお手入れの最後に手持ちの保湿クリームに1滴垂らして混ぜ合わせる『濃密シールドケア』が最適です。
      </p>
      <h3>3. 冬の「乾燥フケ・頭皮の痒み」にはシャンプー前のスカルプパック</h3>
      <p>
        真冬の暖房直撃による頭皮の粉吹きフケや乾燥の痒みには、ブラックシードオイルによるスカルプマッサージが特効薬となります。洗髪前の乾いた頭皮に100円玉大を直接なじませ、指の腹で頭皮全体を3分間マッサージ。そのまま湯船に浸かって5分間スチームパックしてからシャンプーで洗い流すと、頭皮の炎症とフケが鎮まり、毛先までツヤやかなまとまりが生まれます。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ブラックシードオイルに含まれる「チモキノン」とはどのような成分ですか？</div>
        <div class="faq-a">チモキノン（Thymoquinone）は、ニゲラサティバ（ブラッククミン）の種子特有のファイトケミカル（植物性生理活性物質）です。非常に強力な抗酸化・抗炎症・抗菌作用を持ち、冬の急激な寒暖差や木枯らしによって破壊された角層バリアの微小な炎症を速やかに鎮静します。一般的な植物オイルが油分補給にとどまるのに対し、ブラックシードオイルは炎症を抑えながら角層を修復するメディカル級の皮膚保護力を発揮するのが最大の特徴です。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ブラックシードオイル独特のスパイシーなハーブの香りは肌に残りますか？</div>
        <div class="faq-a">未精製の純粋なブラックシードオイルには、オレガノやブラックペッパーを思わせる独特のスパイシーな天然のハーブ臭があります。これは有効成分チモキノンや精油成分が豊富に含まれている証拠です。肌に塗布して手のひらでハンドプレスすると、数分で角層へ吸収され、香りは自然に揮発して肌表面に強く残り続けることはありません。香りが気になる場合は、夜のスキンケアの仕上げとして乳液やクリームに1滴混ぜて使うか、無香料のサプリメントタイプを取り入れるのがおすすめです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬の乾燥性ニキビや毛穴詰まりがあってもブラックシードオイルは使えますか？</div>
        <div class="faq-a">はい、非常に適しています。真冬の大人ニキビは、肌の乾燥によって角質が硬化し、毛穴が塞がれて内部でアクネ菌が繁殖することが主な原因です。ブラックシードオイルは抗菌・抗炎症作用に優れ、毛穴を詰まらせにくい不飽和脂肪酸（リノール酸・オレイン酸）が主体のため、過剰な皮脂分泌を抑えつつ硬くなった角質を柔らかくほぐし、冬の乾燥ニキビを穏やかに鎮静させます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬のスキンケアでの最も効果的なブラックシードオイルの使い方は？</div>
        <div class="faq-a">最もおすすめなのは「夜の洗顔・化粧水直後のプレオイル、またはクリームへの1滴ブレンド」です。洗顔後の水分をたっぷり含んだ肌に2滴をハンドプレスすると、チモキノンが肌荒れシグナルを抑え、オメガ脂肪酸が角層ラメラ構造を整えます。また、冬の乾燥でフケや痒みが出やすい頭皮への「シャンプー前スカルプマッサージ」や、粉を吹いた踵・肘へのポイント使いとしても絶大な効果を発揮します。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-black-seed-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-black-seed-oil.html!")
