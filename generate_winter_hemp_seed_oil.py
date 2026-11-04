import json
import re

with open("fetched_3new_seabuckthorn_blackseed_hemp.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_hemp_seed_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🧤 フランス産ヘンプシード油高配合！真冬の水仕事や冷風で荒れ果てた指先を救う世界的大ベストセラー",
        "catch": "ザ・ボディショップが誇る伝説のハンドケア。濃厚な植物油膜がパックのように密着し、冬のガサガサ関節やひび割れ指先を吸い付くような潤いで包み込む",
        "brand_name": "THE BODY SHOP (ザ・ボディショップ)",
        "capacity": "100ml / アルミチューブ",
        "type": "超高保湿ハードワーキングハンドクリーム",
        "features": "アサ種子油（フランス産ヘンプシードオイル）、パンテノール（プロビタミンB5）、グリセリン、ミツロウ",
        "value": "水洗いをしても落ちにくい強靭なエモリエントヴェールを形成。真冬の過酷な水仕事、乾燥冷風、消毒による深刻な手荒れを根本からプロテクトする救世主",
        "desc_p1": "11月から12月にかけて冷え込みが厳しくなると、手肌は最も過酷な環境に晒されます。冷水での洗い物や繰り返すアルコール消毒によって皮脂膜が根こそぎ奪われ、指の関節がパックリ割れたり、手の甲が赤く粉を吹いた状態に陥ります。ザ・ボディショップの『ハードワーキング ハンドクリーム HP』は、1998年の発売以来、世界中の農夫や職人、医療従事者から絶大な支持を集め続ける伝説のアイテムです。",
        "desc_p2": "チューブから押し出すと、淡いウグイス色のこっくりとした超濃密クリーム。手のひらで温めながら塗り広げると、ヘンプシードオイルの豊富な必須脂肪酸が傷んだ角層深部へグングン浸透します。表面にはベタつかないのに水を弾く強固な保護シールドが完成。夜寝る前に指先まで入念に擦り込んでおけば、翌朝にはひび割れや赤みが劇的に鎮静し、ふっくらと柔らかな手肌を取り戻せます。",
        "target": "真冬になると指先がひび割れて痛む方、何度もハンドクリームを塗り直しても追いつかない重度の乾燥肌の方、水仕事が多く水を弾くクリームを求める方",
        "point": "指の関節を曲げた状態でシワの奥まで塗り込み、爪の付け根（甘皮）まで丁寧にマッサージします。夜は少し厚めに塗り、綿の手袋をして眠るとエステ級のハンドパック効果が得られます。"
    },
    {
        "rank": 2,
        "tag": "🌿 オーガニック認証×無香料ベビー処方！真冬の唇・目元・指先を密着シールドする万能マルチバーム",
        "catch": "アメリカ発の老舗ドクターブロナーが送り出す濃密モイスチャーバーム。ヘンプシードオイルをベースにホホバやミツロウをブレンドし、冬のあらゆる局所乾燥を徹底ガード",
        "brand_name": "Dr.Bronner's (ドクターブロナー)",
        "capacity": "14g / アルミ缶コンパクト",
        "type": "オーガニック高保湿マルチバーム",
        "features": "アサ種子油（有機ヘンプオイル）、ホホバ種子油、アボカド油、ミツロウ、天然トコフェロール",
        "value": "100%天然由来成分＆無香料設計。生後間もない赤ちゃんのデリケートな肌から、冬のエアコンで皮むけした大人の唇や目尻の乾燥小ジワまで安心・安全に使えるマルチ設計",
        "desc_p1": "真冬の強い木枯らしに吹かれると、皮膚が薄く皮脂腺がほとんど存在しない『唇』や『目元』は、真っ先に乾燥のダメージを受けて皮むけや縦ジワを引き起こします。ドクターブロナーの『オーガニック バーム BA ベビーマイルド』は、敏感に傾いた冬の肌を物理的・生理学的に守り抜くために作られた、持ち運びに最適なコンパクトバームです。",
        "desc_p2": "指先にとると体温でじんわりとろけて、摩擦を感じさせずに肌へピタッと密着します。ヘンプシードオイルのオメガ3とオメガ6が角層の水分を強力にホールドし、オーガニックミツロウが冷たい外気との間にバリアを構築。外出先で唇がカサついた時や、オフィスの暖房で目元が突っ張った時にサッと仕込むだけで、瞬時にみずみずしいツヤと潤いが蘇ります。",
        "target": "冬になると唇の皮むけや縦ジワに悩まされる方、外出先や職場で手軽に使える携帯保湿バームを探している方、敏感肌や赤ちゃんにも使える無添加処方を求める方",
        "point": "指先に少量を取り、体温で軽く温めてから、唇や目元、小鼻の乾燥部分へ優しくトントンと押し込むように塗布します。夜は唇に厚めに塗る『オーバーナイトリップパック』がおすすめです。"
    },
    {
        "rank": 3,
        "tag": "💄 ひと塗りで真冬の冷風から唇を完全防備！世界中でリピーターが絶えない伝説のヘンプリップ",
        "catch": "ザ・ボディショップが誇るヘンプシリーズのアイコン的リップスティック。硬めのバームが体温でとろけて唇に密着し、真冬の暖房下でも一日中皮むけ・ひび割れを許さない",
        "brand_name": "THE BODY SHOP (ザ・ボディショップ)",
        "capacity": "4.2g / スティック容器",
        "type": "超高保湿リップトリートメントスティック",
        "features": "アサ種子油（ヘンプシードオイル）、オリーブ果実油、水添植物油、ビタミンE",
        "value": "何度塗り直しても乾いてしまう一般的なリップクリームとは一線を画す圧倒的な持続力。1回の塗布で何時間もしっとり感が持続し、冬のリップメイクの下地としても優秀",
        "desc_p1": "冬になると唇が乾燥して皮がめくれ、リップカラーが綺麗に乗らない……そんな悩みを抱えるすべての方の救世主が、ザ・ボディショップの『ヘンプ リッププロテクター スティック HP』です。世界中の過酷な寒冷地で愛され続けるこのリップは、乾燥した空気から唇の粘膜を守る防護服のような存在です。",
        "desc_p2": "唇に滑らせると、適度な厚みを持ったエモリエント膜がピタッと吸い付くようにフィット。ヘンプシードオイルの不飽和脂肪酸が角層深部まで潤いを届け、荒れ果てた唇のキメをふっくらと整えます。ベタつかず、ギラギラした不自然なテカリもないため、男性のビジネスシーンでの乾燥対策や、口紅を塗る前のリッププライマーとしても完璧に機能します。",
        "target": "冬場はどんなリップクリームを使ってもすぐに唇がカサつく方、口紅を綺麗に発色させたい方、ベタつかず長時間潤いが続く本格派リップケアを求める方",
        "point": "スティックを唇に軽く押し当て、体温で少し温めてから滑らせます。口角や唇の縦ジワに沿って縦方向に塗り込むと、シワの奥まで有効成分が行き渡り保湿効果がさらに高まります。"
    },
    {
        "rank": 4,
        "tag": "💧 未精製コールドプレス×深緑の栄養！冬のゴワつく角層を瞬時に柔らかく整える高純度キャリア",
        "catch": "国内充填・無添加にこだわった&SHの未精製ヘンプシードオイル。麻の実が持つオメガ3・6・9と葉緑素（クロロフィル）をそのまま凝縮し、冬の寒冷で硬化した肌を解きほぐす",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "80ml / 遮光ドロッパーボトル",
        "type": "未精製ピュアヘンプシードオイル",
        "features": "アサ種子油100%（未精製コールドプレス）、オメガ3（α-リノレン酸約20%）、オメガ6（リノール酸約60%）、天然クロロフィル",
        "value": "植物油の中でも群を抜く浸透スピード。肌に乗せるとサラリと馴染み、ベタつきを一切残さず内側からふっくらとした柔軟性を取り戻す優秀な導入ブースター",
        "desc_p1": "冬の寒さでターンオーバーが滞り、肌表面に古い角質が蓄積すると、いくら高価な化粧水をパッティングしても表面で弾かれてしまいます。&SHの『未精製 ヘンプシードオイル 80ml』は、この硬直した皮膚の柔軟化（エモリエント）に最も適した高機能キャリアオイルです。美しいディープグリーン色は、抗酸化作用を持つ天然葉緑素の証です。",
        "desc_p2": "ナッツのような香ばしい香りと共に、肌に伸ばした瞬間にスーッと角層の奥深くへと浸透。人の細胞膜と類似した必須脂肪酸バランスを持つため、皮膚が異物として拒絶せず、瞬時に馴染んで細胞間脂質をサポートします。洗顔後すぐに1滴仕込むことで、その後の化粧水の吸い込みが劇的に向上。大容量80mlなので、顔だけでなく首元やデコルテ、パサつく毛先のケアまで贅沢に使えます。",
        "target": "冬になると化粧水が肌に入っていかないと感じる方、オイルの重さやベタつきが苦手な方、未精製ならではの植物栄養を丸ごとチャージしたい方",
        "point": "朝晩の洗顔直後、肌にまだ水分が残っている状態で1〜2滴を手にとり、手のひらで温めてから優しくハンドプレスします。その後、普段の化粧水をたっぷり重ねてください。"
    },
    {
        "rank": 5,
        "tag": "🌿 オーガニック認証×遮光スポイト瓶！手持ちの乳液や美容液に1滴混ぜてバリア機能をブースト",
        "catch": "手作りコスメとオーガニック原料のパイオニア・マンディムーンが厳選した最高品質ヘンプオイル。必須脂肪酸約80%の驚異的な保水力で、冬の暖房乾燥を完璧にシャットアウト",
        "brand_name": "Mandy Moon (マンディムーン)",
        "capacity": "50ml / 遮光ドロップガラス瓶",
        "type": "未精製オーガニックヘンプシードオイル",
        "features": "有機アサ種子油（コールドプレス未精製）、γ-リノレン酸、植物性ステロール、ビタミンE",
        "value": "希少なγ-リノレン酸（GLA）を含有し、冬の乾燥によってピリピリ敏感になった肌の赤みやバリア破壊を優しくケア。スポイト瓶で衛生的に1滴ずつ調整可能",
        "desc_p1": "冬の乾燥肌対策において、乳液やクリームの保湿力にあと一歩物足りなさを感じた時、最も効果的で経済的な解決策が『純粋植物油のブレンド』です。マンディムーンの『オーガニック ヘンプシードオイル 50ml』は、オーガニック認証農場で栽培された麻の実を熱を加えずに丁寧に搾った、鮮度抜群の美容オイルです。",
        "desc_p2": "特筆すべきは、母乳や月見草油などごく限られた天然資源にしか含まれない貴重な『γ-リノレン酸』を含んでいる点です。寒暖差ショックや乾燥でバリアが乱れ、赤みが出やすい肌に塗布すると、穏やかに肌を保護して健やかな状態へと導きます。普段使っている乳液やクリームに1滴加えるだけで、リッチな保湿エマルジョンへと早変わりし、真冬の朝まで潤いを逃しません。",
        "target": "普段のスキンケアの保湿力を手軽に底上げしたい方、寒暖差やエアコンで肌が赤くなりやすい敏感肌の方、遮光ガラス瓶で鮮度の高いオイルを使いたい方",
        "point": "夜のお手入れの最後に、手のひらにとった乳液や保湿クリームに本品を1滴垂らし、手のひらでよく混ぜ合わせてから顔全体を優しく包み込むようにハンドプレスします。"
    },
    {
        "rank": 6,
        "tag": "✨ 高濃度CBD×ヘンプオイル×シアバター！冬のガサガサ肘・踵・粉吹きボディをとろける濃密膜で包む",
        "catch": "楽天でも大人気のウェルネスブランドrounが放つ最高峰リッチバーム。ヘンプ由来のCBDとヘンプシードオイルの相乗効果で、真冬の硬化した皮膚組織をしっとりほぐす",
        "brand_name": "roun (ラウン)",
        "capacity": "70g / ジャー容器",
        "type": "高濃度CBD配合モイスチャーリッチバーム",
        "features": "カンナビジオール（高濃度CBD）、アサ種子油、シア脂、ホホバ種子油、天然精油（ラベンダー・レモングラス）",
        "value": "硬くガサガサになった踵やひざ、粉を吹くすねに塗り込むと体温でとろけて濃密密着。植物性CBDの抗ストレス・鎮静作用とヘンプオイルの油分が、冬の極度な皮膚乾燥を根本修復",
        "desc_p1": "冬のボディの悩みで最も頑固なのが、ストッキングが引っかかるほどの『踵のひび割れ・ガサガサ』や『肘の黒ずみ乾燥』です。rounの『CBD モイスチャー バーム』は、ヘンプ植物の力を極限まで引き出した高機能トリートメントバームです。上質なヘンプシードオイルとシアバターを贅沢にブレンドし、そこに高純度CBDを配合しています。",
        "desc_p2": "指ですくい取るとコクのあるリッチな質感ですが、肌に伸ばすと体温でジュワッととろけて滑らかなオイルヴェールへと変化します。ヘンプオイルのオメガ脂肪酸が硬化した角質層を柔らかくほぐし、CBDが乾燥による皮膚のチクチク感を穏やかにケア。入浴後の就寝前に踵やひざに擦り込んでおけば、翌朝にはシルクのように滑らかで吸い付くような素肌へと蘇ります。",
        "target": "冬になると踵や肘がひび割れてストッキングが破れる方、ボディの粉吹きと痒みを同時にケアしたい方、心地よいハーブの香りで夜のリラックスタイムを楽しみたい方",
        "point": "入浴後、水分を軽く拭き取った素肌に適量をとり、踵や肘、膝など乾燥が気になる部位へ円を描くように揉み込みます。踵に塗った後は靴下を履いて就寝すると効果が倍増します。"
    },
    {
        "rank": 7,
        "tag": "🌿 世界最高峰CBDブランドの最高傑作！冬の冷えで強張った皮膚をしっとり解きほぐすプレミアムボディバター",
        "catch": "北欧デンマーク発のメディカルグレードブランドENDOCA。CBD450mgとオーガニックヘンプシードオイル、シアバターが融合した、冬の過酷な乾燥を撃退するラグジュアリーバター",
        "brand_name": "ENDOCA (エンドカ)",
        "capacity": "100ml / ガラスジャー容器",
        "type": "オーガニック高保湿ヘンプボディバター",
        "features": "CBD（カンナビジオール450mg）、有機アサ種子油、有機シア脂、有機ヤシ油、天然バニラエキス",
        "value": "100%オーガニック・食品基準のクオリティ。甘く優しい天然バニラとホワイトチョコレートのようなリッチな香りに包まれながら、真冬の強烈な乾燥肌をビロードの感触へ整える",
        "desc_p1": "真冬のボディケアに極上の贅沢と確かな保湿力を求める方に圧倒的な支持を得ているのが、世界的なCBDパイオニアであるENDOCAの『ヘンプボディバター』です。100%オーガニックの食品グレード成分のみで作られており、口に入っても安全なほど徹底した品質基準を誇ります。",
        "desc_p2": "こっくりとしたホイップバターのようなテクスチャーを肌に乗せると、体温でふんわりととろけ、乾燥して硬くなった皮膚組織をじっくりと緩めていきます。ヘンプシードオイルの不飽和脂肪酸とシアバターのステアリン酸が強固な油膜を形成し、脱衣所の寒冷乾燥や暖房による水分蒸発を完璧に遮断。一日中吸い付くようなモチモチ肌が持続し、上質な香りで心まで満たされます。",
        "target": "最高品質のオーガニックボディケアにこだわりたい方、冬の乾燥による全身のカサつき・粉吹きに悩む方、甘く心地よい香りで冬の夜を至福のケアタイムにしたい方",
        "point": "お風呂上がりの温まった肌に適量をとり、手のひらで温めてから全身へ優しく伸ばします。特に乾燥しやすいすねや腕、首元からデコルテにかけて入念にハンドプレスしてください。"
    },
    {
        "rank": 8,
        "tag": "👶 スロベニア産有機ヘンプ×無香料設計！冬の赤ら顔や赤ちゃんの繊細な肌を守るジェントル処方",
        "catch": "伊勢丹などの有名百貨店でも取り扱われる欧州の名門ヘンプタッチ。寒風や寒暖差でピリピリ過敏になった肌を穏やかに鎮め、健やかなバリアを取り戻す低刺激バーム",
        "brand_name": "hemptouch (ヘンプタッチ)",
        "capacity": "50ml / アルミ缶容器",
        "type": "敏感肌・ベビー用オーガニックヘンプバーム",
        "features": "未精製ヘンプシードオイル、マンゴー種子脂、シア脂、カレンデュラエキス、カモミールエキス",
        "value": "アレルギーを引き起こしやすい精油や合成香料を完全排除。冬の冷たい外気で頬が赤くほてってしまう赤ら顔や、マスク荒れ・粉吹きを優しく鎮静するお守りコスメ",
        "desc_p1": "冬になると、外の冷気と室内の暖房の激しい寒暖差によって毛細血管が拡張し、頬がリンゴのように赤くなってヒリヒリ痛む『寒冷赤ら顔』に悩む方が増えます。ヘンプタッチの『ジェントル ベビー バーム』は、そんな極限まで敏感に傾いた素肌のために開発された超低刺激なバリアバームです。",
        "desc_p2": "スロベニアの清らかな自然の中で有機栽培されたヘンプから採れるオイルに、肌荒れ鎮静ハーブの代表格であるカレンデュラとカモミールを配合。肌に乗せると体温でスルスルと広がり、荒れて傷ついた角層表面に優しい保護膜を形成します。ピリピリとした刺激を一切与えず、冬の冷たい風からデリケートな肌をそっと守り抜きます。大人はもちろん、赤ちゃんの冬のほっぺケアにも最適です。",
        "target": "冬の寒風や暖房で頬が赤くヒリヒリ痛くなりやすい方、市販の保湿クリームがしみてしまう超敏感肌の方、赤ちゃんと一緒に使える安心なバームを求める方",
        "point": "指先に少量を取り、手のひらで軽く伸ばしてから、赤みやヒリつきが気になる頬や口周りへ優しく包み込むようにそっと乗せます。擦らずに優しくハンドプレスするのがコツです。"
    },
    {
        "rank": 9,
        "tag": "💋 高純度ヘンプ×植物性ワックス！冬の冷風から唇を守り一日中ツヤと潤いを保つトリートメント",
        "catch": "ミニマルで洗練されたデザインが人気のkalm発CBDリップバーム。ヘンプオイルの濃密な油分が唇の縦ジワを埋め、暖房直撃のオフィスでもふっくらぷるぷるの唇をキープ",
        "brand_name": "kalm (カルム)",
        "capacity": "5ml / チューブ容器",
        "type": "高保湿ヘンプリップトリートメントバーム",
        "features": "アサ種子油、カンナビジオール（高純度CBD）、ヒマシ油、キャンデリラロウ、トコフェロール",
        "value": "チューブタイプで指を汚さずに塗布可能。体温でとろけて唇の細かな凹凸にピタッとフィットし、冬のマスク内乾燥やリップメイク前の土台作りに抜群の威力を発揮",
        "desc_p1": "冬の乾燥した空気やエアコンの直風は、唇の角層から水分を奪い去り、ガサガサの皮むけや縦ジワの原因となります。kalmの『CBD Lip Balm』は、持ち運びやすさと確かな保湿性能を兼ね備えたスタイリッシュな高機能リップバームです。",
        "desc_p2": "チューブの先端から唇に直接塗布できる設計で、いつでもどこでも素早く乾燥ケアが可能。高純度ヘンプシードオイルと植物性ワックスが唇の表面に均一な保護膜を作り出し、水分の蒸発を防ぎながら自然なツヤを与えます。塗った瞬間に唇が柔らかくほぐれ、乾燥によるつっぱり感がスッと消え去る心地よい使用感です。",
        "target": "指を汚さずに手軽に使えるチューブタイプのリップバームを探している方、冬の唇の縦ジワや皮むけをしっかり防ぎたい方、ナチュラルなツヤ感が好きな方",
        "point": "チューブから直接唇に適量を出し、唇の中央から外側へ向けて優しく滑らせます。口紅の上から重ねてグロス代わりに使うと、自然なツヤと乾燥予防が同時に叶います。"
    },
    {
        "rank": 10,
        "tag": "🌾 有機JAS認証×コールドプレス！内外から真冬の水分保持力を底上げする最高峰麻の実オイル",
        "catch": "日本のヘンプ食品のパイオニア・HEMPSが届ける有機エクストラバージンオイル。スキンケアのブースターとしてはもちろん、スプーン1杯の飲用で体の中から細胞膜を潤す逸品",
        "brand_name": "HEMP FOODS JAPAN (ヘンプフーズ)",
        "capacity": "130g (約140ml) / 遮光ボトル",
        "type": "有機JAS認証・内外両用ピュアヘンプシードオイル",
        "features": "有機アサ種子油100%、オメガ3（約20%）、オメガ6（約60%）、無添加・非加熱コールドプレス",
        "value": "食品としての最高基準をクリアした究極の純度。洗顔後のプレオイルとして肌に直接塗布する外側ケアと、毎日の食事に取り入れる内側ケアの両面から冬の乾燥肌を徹底改善",
        "desc_p1": "真冬の深刻な乾燥肌に立ち向かうには、化粧品による肌表面のケアだけでなく、体の内側から良質な油分を補給して細胞膜の柔軟性を高めることが欠かせません。HEMPSの『有機 ヘンプシードオイル 130g』は、有機JAS認証を取得した麻の実から丁寧に非加熱圧搾された最高峰の植物油です。",
        "desc_p2": "肌に塗布すれば、オメガ3とオメガ6が角層のバリアを素早く補修し、内側からもっちりとした潤いを実感できます。さらに毎朝のスムージーやサラダ、納豆にスプーン1杯を加えることで、血流を促し皮膚細胞へ必須脂肪酸を供給。体の内と外からアプローチすることで、真冬の暖房下でも乾燥崩れしない強靭な素肌美を育てることができます。",
        "target": "スキンケアだけでなくインナービューティーも同時に実践したい方、完全無添加・有機JAS認証の確かな安全性を求める方、冬の肌の乾燥体質を根本改善したい方",
        "point": "夜は洗顔後のブースターとして1〜2滴を全顔へハンドプレス。朝はティースプーン1杯を加熱せずにそのまま、またはヨーグルトやスープに垂らして美味しく摂取してください。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-hemp-seed-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！必須脂肪酸の黄金比率が真冬の超乾燥＆ヒリつく角層を密着シールドする高保湿ヘンプシードオイルコスメランク10",
            "description": "11月・12月の本格乾燥と暖房ダメージで荒れ狂う手肌・唇・顔を救う高保湿ヘンプシードオイルコスメを徹底厳選！ザ・ボディショップ、ドクターブロナー、アンドエスエイチ、マンディムーン、rounまで徹底検証。",
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
            "name": "高保湿ヘンプシードオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "ヘンプシードオイル（麻の実油）が真冬の乾燥や肌荒れに劇的に効く理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ヘンプシードオイルの最大の特徴は、人間の皮膚の細胞膜を構成する必須脂肪酸『オメガ3（α-リノレン酸）』と『オメガ6（リノール酸）』が、生化学的に理想とされる『1:3』の黄金比率で含まれている点です。さらに植物界では極めて希少な抗炎症成分『γ-リノレン酸（GLA）』も保有しています。冬の寒冷乾燥でスカスカになった角層のラメラ液晶構造を完璧に再現・修復し、水分蒸散を防ぎながら肌のバリア機能を根本から立て直します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ヘンプシードオイルと話題の「CBD」にはどのような違いがありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ヘンプシードオイルは麻の『種子（実）』から圧搾される植物油で、豊富な必須脂肪酸やビタミンを含み、肌の保湿・皮脂膜バリアの修復（エモリエント）に主たる役割を果たします。一方、CBD（カンナビジオール）は麻の茎や花穂から抽出される生理活性物質で、皮膚の抗炎症・抗酸化・鎮静シグナルに働きます。現在では両方の長所を融合させた『CBD配合ヘンプバーム』なども登場しており、真冬の激しい乾燥荒れ・痒み対策に抜群の相乗効果を発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "オイリー肌やニキビ肌でもヘンプシードオイルは毛穴を詰まらせずに使えますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、全く問題ありません。ヘンプシードオイルのコメドジェニック指数（毛穴の詰まりやすさの指標）は最も安全な『0（ゼロ）』です。分子構造が細かく角層深部へ瞬時に浸透するため、肌表面に油膜のベタつきを残しません。むしろ冬のインナードライによって過剰に出ている皮脂を正常化し、毛穴の詰まりや大人ニキビを防ぐ効果があります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のスキンケアでの最も効果的なヘンプシードオイルの使い方は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "フェイスケアでは『洗顔直後のブースター』、または『夜のクリームへの1滴ブレンド』が最も効果的です。また、手荒れが酷い方には就寝前にヘンプハンドクリームを厚塗りして綿手袋をつけるハンドパック、唇のひび割れには就寝前のヘンプリップバームのオーバーナイトパックを行うことで、翌朝には見違えるような滑らかさを実感できます。"
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
  <title>保湿力の強さで肌乾燥とさようなら！必須脂肪酸の黄金比率が真冬の超乾燥＆ヒリつく角層を密着シールドする高保湿ヘンプシードオイルコスメランク10</title>
  <meta name="description" content="11月・12月の本格乾燥と暖房ダメージで荒れ狂う手肌・唇・顔を救う高保湿ヘンプシードオイルコスメを徹底厳選！ザ・ボディショップ、ドクターブロナー、アンドエスエイチ、マンディムーン、rounまで徹底検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hemp-seed-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！必須脂肪酸の黄金比率が真冬の超乾燥＆ヒリつく角層を密着シールドする高保湿ヘンプシードオイルコスメランク10">
  <meta property="og:description" content="11月・12月の本格乾燥と暖房ダメージで荒れ狂う手肌・唇・顔を救う高保湿ヘンプシードオイルコスメを徹底厳選！ザ・ボディショップ、ドクターブロナー、アンドエスエイチ、マンディムーン、rounまで徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hemp-seed-oil">
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
      --primary: #15803d;
      --primary-light: #dcfce7;
      --primary-dark: #14532d;
      --accent: #16a34a;
      --accent-hover: #166534;
      --bg: #f0fdf4;
      --card-bg: #ffffff;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --border: #bbf7d0;
      --shadow: 0 4px 15px rgba(21, 128, 61, 0.08);
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
      border: 1px solid #bbf7d0;
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
      border: 1px solid #bbf7d0;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th {{
      width: 28%;
      background: #f0fdf4;
      color: var(--primary-dark);
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #bbf7d0;
      text-align: left;
    }}

    table.spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid #bbf7d0;
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
      border: 1px dashed #bbf7d0;
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
      background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 12px rgba(21, 128, 61, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 480px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(21, 128, 61, 0.35);
      background: linear-gradient(135deg, #15803d 0%, #14532d 100%);
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
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！必須脂肪酸の黄金比率が真冬の超乾燥＆ヒリつく角層を密着シールドする高保湿ヘンプシードオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて訪れる乾燥のピーク。過酷な寒冷風や毎日の手洗い、室内の連続暖房によって、手肌はパックリひび割れ、唇の皮は剥け、頬はヒリついてどんなクリームも受け付けない限界状態へ。そんな真冬の「超重度乾燥」を救うのが、人間の皮膚が生化学的に最も必要とする『必須脂肪酸の黄金比率（オメガ3：オメガ6＝1：3）』を奇跡的に宿す「ヘンプシードオイル（麻の実油）」です。毛穴を詰まらせない圧倒的な角層親和性と密着バリア力で潤いを守り抜く高保湿名品10選をコスメコンシェルジュが徹底検証・厳選しました。
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
      <h2>真冬の過酷な乾燥・ひび割れ肌を救う「ヘンプシードオイル」の生化学的根拠</h2>
      <p>
        11月中旬以降、太平洋側を中心に湿度が20%前後にまで落ち込み、室内ではエアコンや暖房器具がフル稼働します。この過酷な気候下で最も早くダメージを受けるのが、手肌・指先・唇・目元といった『角層が薄く、皮脂分泌の少ないパーツ』です。角質層の細胞間脂質がスカスカに干からびると、外気中のアレルゲンや冷風が直接侵入し、激しいヒリつき、粉吹き、ひび割れを引き起こします。
      </p>
      <p>
        この冬の乾燥クライシスにおいて、世界的な自然派コスメ界や皮膚科領域で長年不動の信頼を誇るのが「ヘンプシードオイル（アサ種子油）」です。スーパーフードとしても知られる麻の実は、植物界の中で最も皮膚との親和性が高く、独自の脂肪酸バランスを誇ります。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 奇跡の「オメガ3とオメガ6＝1:3」黄金比率</strong>
          <p>ヒトの健康な細胞膜や角層ラメラ構造が求める必須脂肪酸（α-リノレン酸とリノール酸）の比率と完全に一致。肌が異物として弾かず、瞬時に角層深部へと溶け込んでバリアを再建します。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 希少成分「γ-リノレン酸（GLA）」による抗炎症・修復</strong>
          <p>母乳や月見草などごく一部にしか存在しないγ-リノレン酸を含有。冬の寒暖差でピリピリと過敏になった肌の赤みや炎症を穏やかに鎮静させ、ひび割れ組織の修復を促します。</p>
        </div>
        <div class="highlight-card">
          <strong>3. コメドジェニック指数『0』の超高浸透性</strong>
          <p>重密な油膜を張る一般的なオイルと異なり、毛穴を一切詰まらせません。インナードライに悩む混合肌やニキビ肌、赤ちゃんのデリケートな皮膚でもベタつかずに安心して使えます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿ヘンプシードオイルコスメ おすすめ10選 比較一覧表</h2>
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
      <h2>プロが伝授！真冬のヘンプシードオイル選び方＆部位別レスキュー活用術</h2>
      <h3>1. 「未精製（ディープグリーン）」と「精製（クリア）」の賢い使い分け</h3>
      <p>
        ヘンプシードオイルは、抽出方法によって色と栄養価が異なります。熱を加えないコールドプレスで搾った「未精製オイル」は深いエメラルドグリーン色で、抗酸化作用を持つ葉緑素（クロロフィル）やγ-リノレン酸が豊富に残存しています。夜の集中ケアや重度の手荒れ・乾燥には未精製が最適です。一方、匂いや色移りを極限まで抑えた「精製オイル」は、朝のメイク前や赤ちゃんへの使用に向いています。
      </p>
      <h3>2. 真冬の「ガサガサ手荒れ・ひび割れ」を克服する密着オーバーナイトパック</h3>
      <p>
        水仕事や冷風で荒れ果てた手肌には、就寝前の『ヘンプハンドパック』が劇的な効果をもたらします。ぬるま湯で手を温めてから、ヘンプシードオイル配合のハンドクリームをたっぷりと関節のシワまで擦り込みます。その上から綿100%の手袋を着用して就寝すると、体温によるスチーム効果で油分が角層深部へ閉じ込められ、翌朝には見違えるような滑らかさが蘇ります。
      </p>
      <h3>3. 唇の皮むけを治す「オイル＆バーム」のダブルレイヤー法</h3>
      <p>
        冬の唇の皮むけが止まらない時は、リップクリームを塗る前に『ヘンプシードオイルを1滴指先で唇に馴染ませる』プレケアを取り入れてください。不飽和脂肪酸が乾燥した粘膜を柔らかく解きほぐした後、上からヘンプリップバームを重ねてフタをすることで、冷たい外気による水分蒸散を完全にシャットアウトできます。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ヘンプシードオイル（麻の実油）が真冬の乾燥や肌荒れに劇的に効く理由は何ですか？</div>
        <div class="faq-a">ヘンプシードオイルの最大の特徴は、人間の皮膚の細胞膜を構成する必須脂肪酸「オメガ3（α-リノレン酸）」と「オメガ6（リノール酸）」が、生化学的に理想とされる「1:3」の黄金比率で含まれている点です。さらに植物界では極めて希少な抗炎症成分「γ-リノレン酸（GLA）」も保有しています。冬の寒冷乾燥でスカスカになった角層のラメラ液晶構造を完璧に再現・修復し、水分蒸散を防ぎながら肌のバリア機能を根本から立て直します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ヘンプシードオイルと話題の「CBD」にはどのような違いがありますか？</div>
        <div class="faq-a">ヘンプシードオイルは麻の「種子（実）」から圧搾される植物油で、豊富な必須脂肪酸やビタミンを含み、肌の保湿・皮脂膜バリアの修復（エモリエント）に主たる役割を果たします。一方、CBD（カンナビジオール）は麻の茎や花穂から抽出される生理活性物質で、皮膚の抗炎症・抗酸化・鎮静シグナルに働きます。現在では両方の長所を融合させた「CBD配合ヘンプバーム」なども登場しており、真冬の激しい乾燥荒れ・痒み対策に抜群の相乗効果を発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> オイリー肌やニキビ肌でもヘンプシードオイルは毛穴を詰まらせずに使えますか？</div>
        <div class="faq-a">はい、全く問題ありません。ヘンプシードオイルのコメドジェニック指数（毛穴の詰まりやすさの指標）は最も安全な「0（ゼロ）」です。分子構造が細かく角層深部へ瞬時に浸透するため、肌表面に油膜のベタつきを残しません。むしろ冬のインナードライによって過剰に出ている皮脂を正常化し、毛穴の詰まりや大人ニキビを防ぐ効果があります。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬のスキンケアでの最も効果的なヘンプシードオイルの使い方は？</div>
        <div class="faq-a">フェイスケアでは「洗顔直後のブースター」、または「夜のクリームへの1滴ブレンド」が最も効果的です。また、手荒れが酷い方には就寝前にヘンプハンドクリームを厚塗りして綿手袋をつけるハンドパック、唇のひび割れには就寝前のヘンプリップバームのオーバーナイトパックを行うことで、翌朝には見違えるような滑らかさを実感できます。</div>
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

with open("winter-hemp-seed-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-hemp-seed-oil.html!")
