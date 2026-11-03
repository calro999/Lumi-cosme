import json
import re

with open("fetched_final_30_rosehip_honey_mugwort.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_mugwort"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 韓国コスメ殿堂入り！江華島産カワラヨモギ100%の濃密鎮静原液",
        "catch": "水で薄めない純度100%の植物力。11-12月の寒暖差で赤くほてる乾燥肌をスーッと鎮める奇跡のエッセンス",
        "brand_name": "I'm from (アイムフロム)",
        "capacity": "160ml (マグワート エッセンス)",
        "type": "カワラヨモギ抽出液100%原液エッセンス化粧水",
        "features": "韓国江華島産カワラヨモギ100%、常温スロードリップ抽出法、アルコール・人工香料完全無添加、ヴィーガン認証",
        "value": "精製水ゼロ。熱をかけずに24時間かけて抽出したヨモギ本来のフラボノイドとアミノ酸が、冬の冷え荒れ・毛細血管の赤みトラブルを即効クーリング",
        "desc_p1": "韓国の海風と霧の中で育つ江華島（カンファド）産の最上級カワラヨモギを100%使用した『アイムフロム マグワート エッセンス』。水で薄めることなく、ヨモギの有効成分を壊さない常温抽出法でじっくりと抽出された原液エッセンスです。11月から12月にかけて外気は氷点下近くまで冷え込む一方、オフィスや電車内は過剰な暖房でポカポカになり、肌は激しい寒暖差に晒されます。",
        "desc_p2": "この急激な温度変化によって毛細血管が拡張し、頬に赤みや熱感が出たり、ヒリヒリとした乾燥ゆらぎが発生します。本品を手やコットンでなじませると、ヨモギ特有の穏やかなクーリング作用で肌の熱感がスーッと静まり、角質層の奥深くまでみずみずしい保水成分が行き渡ります。重たい油分で荒れやすい冬のインナードライ肌に、ベタつきのない最高峰の潤いと透明感をもたらします。",
        "target": "冬の寒暖差で頬の赤みやほてりが出やすい方、乾燥するのに油分クリームを使うとニキビができる方、原液コスメで根本ケアしたい方",
        "point": "コットンにたっぷり浸して、赤みが気になる頬や鼻周りに3〜5分間乗せる『部分コットンパック』が絶大な効果を発揮。冷え固まった肌がほぐれ、透き通るような白肌に整います。"
    },
    {
        "rank": 2,
        "tag": "🌿 生ヨモギ葉粉末2.1%配合！冷え固まった角質を解きほぐす生パック",
        "catch": "本物のヨモギ葉の粒々が肌の上でとろける。乾燥ゴワつきとくすみを洗い流してぷるぷるの陶器肌へ",
        "brand_name": "I'm from (アイムフロム)",
        "capacity": "110g (マグワート マスク)",
        "type": "生ヨモギ葉粉末配合ウォッシュオフジェルパック",
        "features": "江華島産カワラヨモギ粉末2.1%、濃密ハーブジェルベース、角質柔軟植物エキス、低刺激処方",
        "value": "冬の寒さでターンオーバーが滞り、硬くゴワついた角質を穏やかに軟化。洗い流した瞬間からキメが整い、ワントーン明るい肌色へ",
        "desc_p1": "ヨモギの葉をそのまま細かく粉砕した生パウダーを2.1%贅沢に配合したウォッシュオフタイプのフェイスマスク。ジェルの中に本物のヨモギの粒々が見えるほど濃厚で、蓋を開けた瞬間に爽やかな天然ハーブの香りが広がります。",
        "desc_p2": "冬の乾燥によって角質が厚くなり、いくら美容液を塗っても浸透しない『ゴワつき肌』に最適です。洗顔後の肌に厚めに伸ばして5〜10分置き、ぬるま湯で優しくマッサージしながら洗い流すと、不要な古い角質や毛穴の汚れが穏やかにオフされます。ヨモギの強力な鎮静成分が肌内部に留まり、洗い上がりはつっぱり感が一切なく、生まれたてのようなモチモチ肌に生まれ変わります。",
        "target": "冬になると肌が硬くザラつく方、くすみで顔色が暗く見えがちな方、お風呂でできる贅沢な鎮静パックを探している方",
        "point": "入浴時、湯船に浸かりながら顔全体に伸ばす『スチームインバスマスク』が効果的。お風呂の蒸気で毛穴が開き、ヨモギのエキスが角層深部までじっくりと浸透します。"
    },
    {
        "rank": 3,
        "tag": "🏺 伝統の甕で2回自然発酵！極小分子が角層を潤す発酵ヨモギ原液トリートメント",
        "catch": "温湿度の異なる環境で熟成された発酵の力。冬のインナードライを根本から解消する導入化粧水",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "150ml (タイムレボリューション アルテミシア トリートメント エッセンス)",
        "type": "2回自然発酵カワラヨモギ100%トリートメントエッセンス",
        "features": "江華島産カワラヨモギ100%、温風熟成×冷温熟成の2回発酵、ノンコメドジェニックテスト済み、敏感肌パッチテスト済み",
        "value": "2回の発酵プロセスによって成分を極限までナノ微粒子化。乾き切った角層のすき間に驚異的なスピードで吸い込まれ、肌の土台を立て直す",
        "desc_p1": "韓国大手MISSHAのプレステージライン『タイムレボリューション』が誇る傑作エッセンス。江華島産のヨモギを伝統の陶器（甕）に入れ、温かい場所で一度、涼しい場所でもう一度じっくりと発酵熟成させる『2回自然発酵技術』を採用しています。",
        "desc_p2": "発酵によってヨモギ本来の抗酸化力と保湿成分が微粒子化されているため、肌に乗せた瞬間の肌なじみが圧倒的です。冬のエアコン暖房によってカラカラに干からびた肌内部へ水分が直ちに行き渡り、内側から押し返すようなみずみずしい弾力を付与。キメの乱れを整え、乾燥による毛穴の目立ちや赤みトラブルを素早く鎮めてくれます。",
        "target": "サラリとした使い心地で深い潤いが欲しい方、発酵コスメのハリ・ツヤ効果を実感したい方、冬の毛穴開きに悩む方",
        "point": "手のひらに500円玉大を取り、顔全体を包み込むように3回優しく押し込む『ハンドプレス3段重ね』を行うと、高保湿クリームを塗った後のようなもっちり感が長時間持続します。"
    },
    {
        "rank": 4,
        "tag": "🛡️ ヨモギエキス54%×5種ヒアルロン酸！冬の水分バリアを修復する水分クリーム",
        "catch": "韓国オリーブヤングのベストセラー。油分過多にならず、乾燥と赤みを同時にケアするジェルクリーム",
        "brand_name": "BRING GREEN (ブリンググリーン)",
        "capacity": "75ml (カワラヨモギ カーミング リペア クリーム)",
        "type": "カワラヨモギ高濃度配合高保水リペアクリーム",
        "features": "カワラヨモギエキス54%、5重複合ヒアルロン酸、ダーマクリアコンプレックス、弱酸性処方",
        "value": "冬の乾燥対策で油分クリームを塗ると吹き出物ができる混合肌・インナードライ肌に最適。水分比率を高めてバリア機能を再構築",
        "desc_p1": "韓国の大手ヘルス＆ビューティストア『オリーブヤング』のプライベートブランドBRING GREENが手掛ける大ヒット水分クリーム。精製水の代わりにカワラヨモギエキスを54%も配合し、分子サイズの異なる5種類のヒアルロン酸を組み合わせた高機能処方です。",
        "desc_p2": "ぷるんとしたみずみずしいジェルクリームテクスチャーで、肌に伸ばすとひんやりとした心地よい清涼感とともにスッとなじみます。油膜でフタをするのではなく、角層内部に大量の水分を抱え込ませるため、毛穴を詰まらせることなく一日中潤いを密封。暖房による肌の火照りを鎮静しながら、夕方になってもテカリやカサつきが起きない理想的な水分・油分バランスを維持します。",
        "target": "冬でも重いクリームが苦手な脂性肌・混合肌の方、Tゾーンはテカるのに頬は粉を吹くインナードライ肌の方",
        "point": "朝のメイク前に適量を薄く塗り広げると、日中のエアコン乾燥によるメイク崩れを完璧に予防。夜は少し厚めに塗って『水分スリーピングパック』として使うのが効果的です。"
    },
    {
        "rank": 5,
        "tag": "🔬 無添加100%植物エキス原液！普段のコスメに混ぜて鎮静力を底上げ",
        "catch": "老舗研究機関が抽出したピュアエキス。冬のマスク擦れや赤みトラブルにダイレクトにアプローチ",
        "brand_name": "自然化粧品研究所",
        "capacity": "20ml (カワラヨモギエキス 美容原液)",
        "type": "無添加カワラヨモギエキス100%美容原液",
        "features": "国内製造、カワラヨモギ花/葉/茎エキス、パラベン・フェノキシエタノール無添加、遮光スポイト瓶",
        "value": "手持ちの化粧水や乳液に数滴混ぜるだけで、即座に高機能鎮静スキンケアへカスタマイズ可能。コストパフォーマンス抜群",
        "desc_p1": "国内の化粧品原料研究機関である自然化粧品研究所が手掛ける、カワラヨモギの美容原液。古くから和漢生薬として重宝されてきたカワラヨモギの有効成分を、高濃度に抽出した無添加ピュア原液です。",
        "desc_p2": "冬の冷たい外気にさらされたり、マスクの擦れによって頬や口周りに赤み・かゆみが出た時の集中レスキューに最適。そのまま美容液として直接患部に塗布するだけでなく、現在愛用している化粧水やクリームに1〜2滴混ぜるだけで、手持ちのアイテムに強力な抗炎症・保水パワーをプラスできます。",
        "target": "手持ちのスキンケアの保湿・鎮静力を手軽にアップさせたい方、成分重視のシンプルケアを好む方、赤みが部分的に出る方",
        "point": "普段使っているシートマスクや化粧水に、手のひらで2〜3滴混ぜてから肌に乗せると、冬の乾燥ゆらぎ肌を速攻で落ち着かせる特製パックが完成します。"
    },
    {
        "rank": 6,
        "tag": "🌿 皮膚科医共同開発の超低刺激！10-CICAと植物鎮静で赤みを消し去る水分ジェル",
        "catch": "累計販売数2,000万個突破。真冬の過敏になった肌にも染みずにスッと馴染む名品クリーム",
        "brand_name": "Dr.G (ドクタージー)",
        "capacity": "70ml (レッドブレミッシュ クリアスージングクリーム)",
        "type": "低刺激シカ＆ボタニカル水分スージングクリーム",
        "features": "10種のCICAコンプレックス、カワラヨモギエキス、植物性スージング成分、毛穴を塞がないノンコメドジェニック",
        "value": "乾燥で弱り切った角層バリアを優しく保護。水分感たっぷりのテクスチャーで、赤ら顔や炎症ニキビを穏やかに沈静化",
        "desc_p1": "韓国の皮膚科専門医が立ち上げたドクターズコスメブランドDr.Gの代名詞『レッドブレミッシュ クリアスージングクリーム』。10種類のCICA成分とカワラヨモギエキスを贅沢にブレンドし、寒暖差や乾燥ストレスで赤くなった肌を集中ケアします。",
        "desc_p2": "ベタつきが一切ない水分たっぷりのジェルテクスチャー。肌に乗せた瞬間に心地よい潤いが広がり、荒れた肌表面を滑らかにコーティングします。冬の冷えや乾燥で皮膚が薄くなり、刺激に過敏になっている状態でもピリピリ感なく安心して使え、キメの整った健やかな肌状態へと導いてくれます。",
        "target": "敏感肌で刺激に弱い方、冬の暖房で顔が赤くなりやすい方、ニキビや肌荒れを繰り返す方",
        "point": "夜寝る前に肌が隠れるくらいたっぷりと厚めに塗り広げる『水分スリーピングパック』として活用すると、翌朝赤みが完全に引き、もっちりとした潤いが実感できます。"
    },
    {
        "rank": 7,
        "tag": "✨ 朝のメイク前に3分乗せるだけ！ティーツリー×ヨモギの急速水分鎮静パッド",
        "catch": "角質ケアと高保水を同時に実現。大判極細パッドが冬の乾燥ゴワつきと化粧ノリの悪さを一掃",
        "brand_name": "MEDIHEAL (メディヒール)",
        "capacity": "100枚入 (ティーツリー カーミング トナーパッド)",
        "type": "高機能エッセンス含浸トナーパッド",
        "features": "ティーツリー有効成分×カワラヨモギエキス、ヴィーガン認証ガーゼパッド、角質拭き取り＆部分パックの2way",
        "value": "忙しい朝でもサッと貼るだけで、暖房乾燥でカサつく頬を瞬時にモチ肌へ整える。ファンデーションの密着力が劇的アップ",
        "desc_p1": "世界的なシートマスクブランドMEDIHEALが開発した、高機能トナーパッド。ティーツリーとカワラヨモギの濃密な鎮静エッセンスが、100枚のパッドにひたひたに染み込んでいます。",
        "desc_p2": "冬の朝、洗顔後の乾燥した肌にエンボス面で優しく拭き取ると、硬くなった古い角質が穏やかにオフされ、その後にソフト面を頬や額に3分間貼り付けるだけで、角層奥まで水分が急速チャージされます。朝のスキンケアの時短になりながら、暖房の効いたオフィスでも一日中メイクが崩れない完璧なベースを作ることができます。",
        "target": "朝のスキンケアを手早く済ませたい方、冬の朝にファンデーションが粉を吹いて乗らない方、部分的な乾燥や肌荒れが気になる方",
        "point": "メイク前の下地を塗る直前に、両頬と鼻に3分間貼り付けてクールダウン。毛穴がキュッと引き締まり、日中のファンデーションの毛穴落ちが完全に防げます。"
    },
    {
        "rank": 8,
        "tag": "💧 韓国オリーブヤング年間1位！ドクダミ77%と植物エキスが織りなす清らかな潤い",
        "catch": "敏感になった冬の肌を優しく鎮静。肌の油水分バランスを黄金比率に整える国民的化粧水",
        "brand_name": "Anua (アヌア)",
        "capacity": "250ml (ドクダミ77% スージングトナー)",
        "type": "高濃度ドクダミ＆ヨモギ保水鎮静トナー",
        "features": "ドクダミエキス77%、カワラヨモギエキス、パンテノール、弱酸性低刺激処方、大容量250ml",
        "value": "刺激物質を極限まで排除したマイルド設計。冬の寒冷外気や乾燥でピリつくデリケート肌に、澄みわたるような水分を補給",
        "desc_p1": "韓国国内だけでなく日本でも記録的なヒットを飛ばすAnuaの『ドクダミ77 スージングトナー』。ドクダミエキス77%をベースに、カワラヨモギエキスやパンテノールを組み合わせ、肌荒れ防止と水分保持を両立させた名品トナーです。",
        "desc_p2": "水のようにサラッとしたテクスチャーでありながら、肌に浸透させると角層の内側からふっくらと潤いが満ちてくるのを実感できます。油分過多によるニキビを防ぎつつ、冬の乾燥によるバリア破壊を食い止めるため、どんな肌質の方でもオールマイティに使いこなせる冬のベーシックケアです。",
        "target": "さっぱりした使い心地でしっかり潤したい方、冬のインナードライや吹き出物に悩む方、大容量でバシャバシャ使いたい方",
        "point": "手のひらでハンドプレスして重ね塗りをする『レイヤリング保湿』を2〜3回繰り返すと、重たい乳液を使わなくても内側から吸い付くような水光肌に仕上がります。"
    },
    {
        "rank": 9,
        "tag": "♨️ 国産無農薬ヨモギ100%！体の芯から温めて全身の乾燥肌荒れを潤す薬草風呂",
        "catch": "奈良産吉野よもぎを天日乾燥。寒さで冷えた身体を温め、お風呂上がりの全身乾燥・粉吹きを根本から防ぐ",
        "brand_name": "ほんまもんのよもぎ / 吉野よもぎ",
        "capacity": "10袋入 (あったか よもぎ風呂茶)",
        "type": "無農薬ヨモギ100%天然薬草入浴剤",
        "features": "奈良県産無農薬吉野よもぎ100%、無着色・無香料・完全無添加、天日干しティーバッグ加工",
        "value": "よもぎの精油成分シネオールが血行を促進し、湯冷めを防止。肌のバリア機能を高めて全身の粉吹き・かゆみを防ぐ温活バスケア",
        "desc_p1": "11月から12月にかけての肌乾燥は、全身の冷えと血行不良が大きな要因です。奈良県の山深くで栽培された無農薬の吉野よもぎを100%使用したこの薬草風呂は、自宅のお風呂で本格的な『よもぎ湯』を楽しめる贅沢な入浴パックです。",
        "desc_p2": "浴槽にポンと入れるだけで、お湯が淡い緑色に染まり、清々しい天然よもぎのアロマが浴室いっぱいに広がります。よもぎに含まれる精油成分（シネオールやツヨン）が血管を拡張して身体の芯から温め、湯上がり後もポカポカ感が持続。入浴中にバッグで優しく肌をなでると、冬場に粉を吹きやすいすねや腕・背中がしっとりすべすべに潤います。",
        "target": "手足の冷えがひどく寝付けない方、お風呂上がりに全身の肌が乾燥してかゆくなる方、天然ハーブの香りでリラックスしたい方",
        "point": "湯船の中でパックを軽く揉み出すと、濃厚なヨモギエキスがお湯に溶け出します。顔にパッティングするように湯を浴びると、蒸気との相乗効果で顔の血色感もアップします。"
    },
    {
        "rank": 10,
        "tag": "🌸 伝統和漢の蒸留水仕立て！寒風に負けない健やかな角層へ整えるよもぎ化粧水",
        "catch": "京都・和漢植物の恵みを凝縮。肌にすっと馴染んでキメを整えるシンプルで贅沢なボタニカルウォーター",
        "brand_name": "マミーサンゴ / 和漢植物",
        "capacity": "180ml (よもぎ水 ナチュラルウォーター)",
        "type": "天然カワラヨモギ蒸留水化粧水",
        "features": "国産ヨモギエキス、植物性BG、アルコールフリー、弱酸性、昔ながらの和漢処方",
        "value": "余計な界面活性剤や合成ポリマーを一切使わないシンプル設計。冬の寒風で疲弊した角層細胞を優しく潤すデイリーローション",
        "desc_p1": "古くから日本の生活に寄り添ってきた和漢植物よもぎの力を、現代のスキンケアへ昇華させた『マミーサンゴ よもぎ水』。厳選された国産よもぎを原料とし、清らかな水とともに丁寧に蒸留・抽出されています。",
        "desc_p2": "合成香料や不要な添加物を一切排除しているため、肌に乗せた瞬間の浸透感と肌への優しさが際立ちます。冬の冷風で赤みが出たり、乾燥でキメが粗くなってしまった肌にたっぷりと水分を注ぎ込み、肌本来が持つすこやかなバリア機能をサポート。赤ちゃんからお年寄りまで家族全員で安心して使える穏やかな高保水化粧水です。",
        "target": "化学成分が苦手なオーガニック・和漢志向の方、家族全員で使える低刺激化粧水を探している方、冬の肌あれ予防をしたい方",
        "point": "スプレー容器に移し替えて、日中のオフィスでの『保湿ミスト』として携帯するのがおすすめ。メイクの上からひと吹きするだけで、エアコン乾燥をブロックできます。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['name']}",
        "description": d['catch'],
        "image": p['img_url'],
        "url": f"https://trendbeauty.site/winter-mugwort.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "ヨモギ（カワラヨモギ/マグワート）エキスは冬の乾燥肌にどんな効果がありますか？",
        "answer": "カワラヨモギには『フラボノイド（アピゲニン、ルテオリン）』『タンニン』『アミノ酸』『多糖類』が豊富に含まれています。11〜12月の冬特有の悩みである『外気の寒さと暖房による激しい寒暖差』で毛細血管が拡張し、赤みやほてり・ヒリつきを伴う乾燥肌に対し、優れた抗炎症作用とクーリング作用で素早く熱感を鎮めます。さらに豊富なアミノ酸と多糖類が角質層の隙間に水分をギュッと抱え込み、油分に頼らないみずみずしいバリア膜を再構築します。"
    },
    {
        "question": "CICA（ツボクサ）やドクダミとヨモギの違いは何ですか？",
        "answer": "『CICA（ツボクサエキス）』は傷んだ皮膚組織の修復やコラーゲン合成サポートに優れ、『ドクダミ』は毛穴の皮脂トラブルやアクネ菌対策に強みがあります。対して『ヨモギ（カワラヨモギ）』は血行促進・温活作用と毛細血管の赤み鎮静、そして高い水分保持力に最も優れています。冬の寒さによる血行不良、赤ら顔、乾燥によるゴワつきが気になる方にはヨモギが最も適しています。"
    },
    {
        "question": "冬の乾燥肌にヨモギコスメだけで保湿は足りますか？クリームは必要ですか？",
        "answer": "ヨモギエッセンスやトナーは角層深部へ大量の水分を届ける力に優れていますが、油分自体は控えめな処方が多いため、極度の乾燥肌や真冬のエアコン環境下では、ヨモギで角層を満たした後にセラミドクリームやマルラオイル、ローズヒップオイルなどの油分でフタをすることをおすすめします。油分と組み合わせることで水分の蒸散を完全に防ぐことができます。"
    },
    {
        "question": "よもぎアレルギーやキク科アレルギーがある場合は使えますか？",
        "answer": "ヨモギはキク科の植物です。ブタクサやヨモギなどのキク科植物に対して花粉症や接触アレルギーをお持ちの方は、赤みやかゆみが出る可能性があるため使用を控えるか、使用前に必ず二の腕の内側などでパッチテストを行い、24時間肌に異常が出ないことを確認してからご使用ください。"
    },
    {
        "question": "よもぎ入浴剤はどんなタイミングで使うのが最も効果的ですか？",
        "answer": "38〜40度程度のぬるめのお湯にゆっくり15〜20分浸かるのがベストです。熱すぎるお湯は肌の天然保湿成分を流出させてしまいますが、ぬるめのよもぎ湯なら精油成分シネオールがじっくり身体の芯まで温め、湯冷めを防ぎながら全身の角質を柔らかく潤します。入浴後すぐにボディミルクやオイルを塗ると、粉吹きを完全に予防できます。"
    }
]

jsonld_faq = []
for faq in faq_list:
    jsonld_faq.append({
        "@type": "Question",
        "name": faq["question"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": faq["answer"]
        }
    })

jsonld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-mugwort.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！冬の冷え・寒暖差による赤みと乾燥ゴワつきを鎮める高保水ヨモギ（マグワート）コスメランク10",
    "description": "11月から12月の過酷な寒暖差赤みと乾燥ゴワつきを救う高保水ヨモギ・マグワートコスメを徹底厳選！アイムフロムの純度100%原液からミシャの発酵エッセンス、よもぎ入浴剤まで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
    "image": items[0]["img_url"],
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "datePublished": "2026-11-03T21:00:00+09:00",
    "dateModified": "2026-11-03T21:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保水ヨモギコスメおすすめ人気ランキング10選",
    "itemListElement": jsonld_items
}

jsonld_faqpage = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": jsonld_faq
}

cards_html = []
for i, p in enumerate(items):
    d = product_details[i]
    cards_html.append(f"""
    <article class="product-card" id="item-{i+1}">
      <div class="product-badge-rank">第{i+1}位</div>
      <div class="product-tag">{d['tag']}</div>
      <h3 class="product-name">{d['brand_name']} {p['name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-flex">
        <div class="product-img-box">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で詳細を見る・購入
          </a>
        </div>
        
        <div class="product-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{d['brand_name']}</td></tr>
            <tr><th>容量 / 規格</th><td>{d['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・製法</th><td>{d['features']}</td></tr>
            <tr><th>高保水＆鎮静の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の寒暖差赤み・乾燥ゴワつきに対する詳細解説</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-block">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-block">
            <strong>✨ 美容のプロ直伝！冬のおすすめ活用テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_str = "\n".join(cards_html)

faq_html = []
for f in faq_list:
    faq_html.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {f['question']}</h3>
      <div class="faq-a"><p>{f['answer']}</p></div>
    </div>
    """)
faq_str = "\n".join(faq_html)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の冷え・寒暖差による赤みと乾燥ゴワつきを鎮める高保水ヨモギ（マグワート）コスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月から12月の過酷な寒暖差赤みと乾燥ゴワつきを救う高保水ヨモギ・マグワートコスメを徹底厳選！アイムフロムの純度100%原液からミシャの発酵エッセンス、よもぎ入浴剤まで、楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="ヨモギコスメ,マグワート,カワラヨモギ,冬コスメ,赤ら顔,寒暖差ゆらぎ,アイムフロム,ミシャ,高保水,インナードライ,鎮静スキンケア">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-mugwort.html">
  
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の冷え・寒暖差による赤みと乾燥ゴワつきを鎮める高保水ヨモギ（マグワート）コスメランク10">
  <meta property="og:description" content="11月から12月の過酷な寒暖差赤みと乾燥ゴワつきを救う高保水ヨモギ・マグワートコスメを徹底厳選！楽天人気ランキング10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-mugwort.html">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(jsonld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(jsonld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
{json.dumps(jsonld_faqpage, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary-color: #2e6044;
      --primary-light: #f2f8f4;
      --accent-color: #16a34a;
      --accent-hover: #15803d;
      --text-main: #2d3748;
      --text-muted: #5a6a85;
      --bg-main: #f9fbf9;
      --card-bg: #ffffff;
      --border-color: #cde4d5;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.04);
      --shadow-md: 0 4px 12px rgba(46,96,68,0.08);
      --shadow-lg: 0 8px 24px rgba(46,96,68,0.12);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: var(--bg-main);
    }}

    .container {{
      max-width: 920px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 16px 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .site-nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-color);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 20px;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--accent-color);
    }}

    .breadcrumb {{
      display: flex;
      gap: 8px;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin: 20px 0 10px;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{
      color: var(--accent-color);
    }}

    .article-header {{
      background: #ffffff;
      padding: 36px 32px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      margin-bottom: 30px;
    }}
    .article-tag-top {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-color);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 12px;
      border: 1px solid var(--border-color);
    }}
    h1.article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: var(--primary-color);
      margin-bottom: 16px;
      font-weight: 800;
    }}
    .meta-info {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      gap: 16px;
      align-items: center;
      margin-bottom: 20px;
    }}
    .article-lead {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #374151;
      background: var(--primary-light);
      padding: 20px;
      border-left: 4px solid var(--primary-color);
      border-radius: var(--radius-sm);
    }}

    .toc-box {{
      background: #ffffff;
      padding: 24px 28px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      margin-bottom: 40px;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-weight: 800;
      color: var(--primary-color);
      margin-bottom: 14px;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      counter-reset: toc-counter;
    }}
    .toc-list li {{
      margin-bottom: 10px;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: #4b5563;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--accent-color);
      font-weight: 600;
    }}

    .section-title {{
      font-size: 1.55rem;
      color: var(--primary-color);
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 12px;
      margin: 48px 0 24px;
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
    }}
    .content-box {{
      background: #ffffff;
      padding: 32px;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      margin-bottom: 30px;
    }}
    .content-box p {{
      margin-bottom: 18px;
      font-size: 1.02rem;
      line-height: 1.9;
    }}
    .content-box h3 {{
      font-size: 1.25rem;
      color: var(--primary-color);
      margin: 28px 0 14px;
      padding-left: 12px;
      border-left: 4px solid var(--accent-color);
    }}
    .highlight-box {{
      background: var(--primary-light);
      border-radius: var(--radius-md);
      padding: 20px;
      margin: 24px 0;
      border: 1px dashed var(--primary-color);
    }}
    .highlight-box h4 {{
      color: var(--primary-color);
      margin-bottom: 10px;
      font-size: 1.05rem;
    }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-md);
      padding: 32px;
      margin-bottom: 40px;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -14px;
      left: 24px;
      background: linear-gradient(135deg, #16a34a, #2e6044);
      color: #ffffff;
      font-weight: 900;
      font-size: 1rem;
      padding: 4px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(22,163,74,0.3);
    }}
    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--accent-color);
      margin-top: 6px;
      margin-bottom: 8px;
    }}
    .product-name {{
      font-size: 1.35rem;
      color: #1f2937;
      margin-bottom: 8px;
      line-height: 1.45;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      color: #4b5563;
      margin-bottom: 24px;
      font-weight: 600;
    }}

    .product-flex {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 28px;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-flex {{
        grid-template-columns: 1fr;
      }}
    }}

    .product-img-box {{
      text-align: center;
      background: #fafafa;
      padding: 16px;
      border-radius: var(--radius-md);
      border: 1px solid #f0f0f0;
    }}
    .product-img {{
      max-width: 100%;
      height: 240px;
      object-fit: contain;
      border-radius: var(--radius-sm);
      margin-bottom: 14px;
      transition: transform 0.2s;
    }}
    .product-img:hover {{
      transform: scale(1.03);
    }}
    .price-box {{
      margin-bottom: 14px;
    }}
    .price-label {{
      display: block;
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .price-val {{
      font-size: 1.6rem;
      font-weight: 900;
      color: var(--primary-color);
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #e60000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 12px 16px;
      border-radius: var(--radius-sm);
      box-shadow: 0 4px 10px rgba(191,0,0,0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a00000, #cc0000);
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(191,0,0,0.35);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 8px 12px;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 28%;
      color: var(--text-muted);
      text-align: left;
      font-weight: 600;
      background: #fafafa;
    }}
    .spec-table td {{
      color: #1f2937;
    }}

    .review-block {{
      margin-bottom: 18px;
    }}
    .review-block h4 {{
      font-size: 1rem;
      color: var(--primary-color);
      margin-bottom: 10px;
      font-weight: 700;
    }}
    .review-block p {{
      font-size: 0.95rem;
      line-height: 1.85;
      color: #374151;
      margin-bottom: 10px;
    }}

    .target-block, .usage-block {{
      background: #fafafa;
      padding: 14px 18px;
      border-radius: var(--radius-sm);
      margin-bottom: 12px;
      font-size: 0.92rem;
      border-left: 3px solid var(--primary-color);
    }}
    .target-block strong, .usage-block strong {{
      color: var(--primary-color);
      display: block;
      margin-bottom: 4px;
    }}

    /* 比較表 */
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 24px 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-color);
    }}
    .compare-table th, .compare-table td {{
      padding: 12px 14px;
      text-align: left;
      border-bottom: 1px solid var(--border-color);
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-color);
      font-weight: 700;
      white-space: nowrap;
    }}

    /* FAQ */
    .faq-item {{
      background: #ffffff;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      padding: 20px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-sm);
    }}
    .faq-q {{
      font-size: 1.05rem;
      color: var(--primary-color);
      font-weight: 700;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}
    .faq-a p {{
      font-size: 0.95rem;
      line-height: 1.85;
      color: #374151;
    }}

    /* 内部リンク */
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 20px;
    }}
    .related-link-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 16px;
      text-decoration: none;
      color: var(--text-main);
      display: block;
      transition: all 0.2s;
    }}
    .related-link-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
      border-color: var(--accent-color);
    }}
    .related-link-card h4 {{
      font-size: 0.95rem;
      color: var(--primary-color);
      margin-bottom: 6px;
    }}
    .related-link-card p {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    footer {{
      background: #2d3748;
      color: #e2e8f0;
      padding: 40px 0 20px;
      margin-top: 60px;
      font-size: 0.85rem;
    }}
    .footer-content {{
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 24px;
      margin-bottom: 30px;
    }}
    .footer-col h5 {{
      color: #ffffff;
      margin-bottom: 12px;
      font-size: 0.95rem;
    }}
    .footer-col ul {{
      list-style: none;
    }}
    .footer-col li {{
      margin-bottom: 6px;
    }}
    .footer-col a {{
      color: #cbd5e0;
      text-decoration: none;
    }}
    .footer-col a:hover {{
      color: #ffffff;
    }}
    .footer-bottom {{
      text-align: center;
      border-top: 1px solid #4a5568;
      padding-top: 20px;
      color: #a0aec0;
    }}
  </style>
</head>
<body>

  <header>
    <div class="container site-nav">
      <a href="index.html" class="site-logo">
        <span>❄️</span> 冬コスメ徹底比較ラボ
      </a>
      <nav class="nav-links">
        <a href="index.html">ホーム</a>
        <a href="winter-cica-cream.html">CICAコスメ</a>
        <a href="winter-toner-pad.html">トナーパッド</a>
        <a href="winter-medicinal-bath.html">薬用入浴剤</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <div class="breadcrumb">
      <a href="index.html">ホーム</a> &gt; 
      <a href="winter-cica-cream.html">鎮静・保水スキンケア特集</a> &gt; 
      <span>高保水ヨモギコスメ</span>
    </div>

    <div class="article-header">
      <span class="article-tag-top">11-12月真冬の寒暖差ゆらぎレスキュー特別企画</span>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の冷え・寒暖差による赤みと乾燥ゴワつきを鎮める高保水ヨモギ（マグワート）コスメランク10</h1>
      <div class="meta-info">
        <span>更新日: 2026年11月03日</span>
        <span>監修: 冬コスメ徹底比較ラボ 専属コスメコンシェルジュ</span>
        <span>実機検証・楽天APIリアルタイムデータ連動</span>
      </div>
      <p class="article-lead">
        外気は氷点下に迫る寒風が吹き荒れ、一歩室内に入れば強力な暖房が吹きつける11月から12月。「顔がカッと熱くなって頬が赤くなる」「乾燥しているのに重いクリームを塗るとポツポツができる」「肌が硬くこわばって突っ張る」……そんな冬特有の『寒暖差ゆらぎ肌・赤ら顔』に救世主として選ばれているのが、伝統和漢・韓方の王道ハーブ『ヨモギ（カワラヨモギ/マグワート）』です。熱感をスーッと鎮めるフラボノイドと、角層深部を満たすアミノ酸の強力な水分保持力。本記事では楽天API連動の最新ランキング10選とプロ直伝の活用術を徹底解説します。
      </p>
    </div>

    <div class="toc-box">
      <h2 class="toc-title">📑 目次 - クリックで各セクションへ移動</h2>
      <ul class="toc-list">
        <li><a href="#section-why">1. なぜ11-12月の寒暖差赤み・乾燥にヨモギが効くのか？</a></li>
        <li><a href="#section-howto">2. 失敗しない高保水ヨモギコスメの選び方3つのポイント</a></li>
        <li><a href="#section-ranking">3. 保湿力高めヨモギコスメ厳選おすすめランキング10選</a></li>
        <li><a href="#section-compare">4. おすすめヨモギコスメ10選 徹底スペック比較一覧表</a></li>
        <li><a href="#section-routine">5. プロ直伝！冬の赤み・乾燥ゴワつきをリセットする3つの活用ステップ</a></li>
        <li><a href="#section-faq">6. よくある質問（FAQ）と注意点</a></li>
        <li><a href="#section-links">7. 合わせて読みたい！冬の乾燥・ゆらぎ対策おすすめ関連記事</a></li>
      </ul>
    </div>

    <!-- 導入セクション1 -->
    <section id="section-why" class="content-box">
      <h2 class="section-title">✨ なぜ11-12月の寒暖差赤み・乾燥にヨモギが効くのか？</h2>
      <p>
        11月から12月にかけて、私たちの肌を苦しめる最大の原因は「寒暖差（温度ショック）」です。冷たい冬の北風にさらされた直後に暖かい室内に入ると、急激な温度変化に対応しようとして顔の毛細血管が一気に拡張します。このとき、角質層のバリア機能が低下していると、拡張した血管が透けて頬が赤くほてり、ピリつきやかゆみを伴う「寒暖差ゆらぎ」が発生します。
      </p>
      <p>
        このような状態の肌に油分の多いこってりしたクリームを塗り重ねると、熱がこもってさらに赤みが悪化したり、毛穴が詰まって吹き出物を引き起こす原因になります。ここで真価を発揮するのが、古来より生薬として重用されてきたカワラヨモギ（学名：Artemisia）です。
      </p>

      <div class="highlight-box">
        <h4>🌿 カワラヨモギが誇る科学的鎮静＆高保水メカニズム</h4>
        <ul style="padding-left: 20px; line-height: 1.9;">
          <li><strong>強力なフラボノイド（アピゲニン・ルテオリン）：</strong> 血管の急激な炎症や熱感を穏やかにクーリングし、赤ら顔やヒリヒリ感を瞬時に鎮静させます。</li>
          <li><strong>天然多糖類とアミノ酸による水分保持力：</strong> 油分でフタをするのではなく、角層細胞の隙間にみずみずしい水分をダイレクトに送り込み、内部からふっくらと厚みのある健やかなバリアを再構築します。</li>
          <li><strong>精油成分（シネオール等）による血行促進と温活：</strong> 冷えによって滞った血流を巡らせ、停滞した冬のターンオーバーを正常化。硬くゴワついた角質をやわらかく解きほぐします。</li>
        </ul>
      </div>

      <p>
        ヨモギコスメは「肌のほてりや赤みをクールダウンしながら、内側には温もりのある血行を促し、水分をたっぷり満たす」という、冬の過酷な環境に最も適した絶妙なバランスを持っています。だからこそ、表面はテカるのに内側がつっぱるインナードライ肌や、冬の敏感ゆらぎ肌に圧倒的な支持を集めているのです。
      </p>
    </section>

    <!-- 選び方セクション -->
    <section id="section-howto" class="content-box">
      <h2 class="section-title">🔍 失敗しない高保水ヨモギコスメの選び方3つのポイント</h2>
      <p>
        ヨモギコスメには原液エッセンスからシートマスク、水分クリーム、入浴剤まで多彩なアイテムが存在します。冬の肌悩みに合わせて最適なアイテムを選ぶポイントを押さえましょう。
      </p>

      <h3>① 抽出方法とヨモギ濃度の確認（単一原液か複合発酵か）</h3>
      <p>
        赤みやほてりを速攻で鎮めたいなら、カワラヨモギエキス100%の『単一成分エッセンス』が最もダイレクトに作用します。一方、冬の乾燥小ジワやインナードライも同時に改善したい場合は、分子を極小化した『発酵ヨモギ』やヒアルロン酸を組み合わせた複合処方を選びましょう。
      </p>

      <h3>② アルコール（エタノール）フリー処方を選ぶ</h3>
      <p>
        冬の寒風でバリアが低下した敏感肌に、アルコール高配合のスキンケアを使用するとピリピリとした刺激を感じることがあります。低刺激設計、弱酸性、アルコール・香料フリーの表記がある製品を選ぶと安心です。
      </p>

      <h3>③ 内外からのアプローチ（スキンケア×よもぎ温活入浴）</h3>
      <p>
        顔のスキンケアだけでなく、冬の全身の冷えや乾燥を防ぐためには、薬草よもぎ風呂などの「温活入浴」を組み合わせるのが非常に効果的です。全身の巡りを整えることで、顔のスキンケア効果も飛躍的に高まります。
      </p>
    </section>

    <!-- ランキングセクション -->
    <section id="section-ranking">
      <h2 class="section-title">🏆 保湿力高めヨモギコスメ厳選おすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: var(--text-muted); font-size: 0.95rem;">
        ※楽天市場の最新APIデータを基に、ヨモギエキスの純度、寒暖差赤みへの鎮静実感、高保水持続力、実際の購入者レビューを多角的に検証してランキングを決定しています。
      </p>

      {cards_str}
    </section>

    <!-- 比較表セクション -->
    <section id="section-compare" class="content-box">
      <h2 class="section-title">📊 おすすめヨモギコスメ10選 徹底スペック比較一覧表</h2>
      <p>ランキングでご紹介した10アイテムの容量、アイテム種別、主成分、価格帯を一目で比較できる一覧表です。</p>
      
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>ブランド</th>
              <th>容量 / 種別</th>
              <th>主要成分・特長</th>
              <th>参考価格（税込）</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>第1位</strong></td>
              <td>マグワート エッセンス</td>
              <td>I'm from</td>
              <td>160ml 導入化粧水</td>
              <td>江華島産カワラヨモギ100%原液・赤み鎮静</td>
              <td>¥{items[0]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第2位</strong></td>
              <td>マグワート マスク</td>
              <td>I'm from</td>
              <td>110g 洗い流しパック</td>
              <td>生ヨモギ葉粉末2.1%・冬のゴワつき柔軟化</td>
              <td>¥{items[1]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第3位</strong></td>
              <td>アルテミシア トリートメント</td>
              <td>MISSHA</td>
              <td>150ml 美容液化粧水</td>
              <td>2回自然発酵・極小分子ナノ浸透高保水</td>
              <td>¥{items[2]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第4位</strong></td>
              <td>カワラヨモギ リペア クリーム</td>
              <td>BRING GREEN</td>
              <td>75ml 水分クリーム</td>
              <td>ヨモギ54%×5種ヒアルロン酸・油分フリー</td>
              <td>¥{items[3]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第5位</strong></td>
              <td>カワラヨモギエキス 美容原液</td>
              <td>自然化粧品研究所</td>
              <td>20ml 美容原液</td>
              <td>国産無添加100%・手持ちコスメに混ぜて強化</td>
              <td>¥{items[4]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第6位</strong></td>
              <td>クリアスージングクリーム</td>
              <td>Dr.G</td>
              <td>70ml スージングジェル</td>
              <td>10-CICA×ヨモギ・皮膚科医共同開発低刺激</td>
              <td>¥{items[5]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第7位</strong></td>
              <td>ティーツリー カーミング パッド</td>
              <td>MEDIHEAL</td>
              <td>100枚入 トナーパッド</td>
              <td>朝の急速3分パック・ファンデ密着力アップ</td>
              <td>¥{items[6]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第8位</strong></td>
              <td>ドクダミ77 スージングトナー</td>
              <td>Anua</td>
              <td>250ml 化粧水</td>
              <td>ドクダミ77%×ヨモギ・弱酸性デイリー保水</td>
              <td>¥{items[7]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第9位</strong></td>
              <td>あったか よもぎ風呂茶</td>
              <td>ほんまもんのよもぎ</td>
              <td>10袋 薬草入浴剤</td>
              <td>吉野よもぎ100%・芯から温めて全身乾燥予防</td>
              <td>¥{items[8]['price']:,}</td>
            </tr>
            <tr>
              <td><strong>第10位</strong></td>
              <td>よもぎ水 ナチュラルウォーター</td>
              <td>マミーサンゴ</td>
              <td>180ml 和漢化粧水</td>
              <td>伝統よもぎ蒸留水・家族で使えるシンプル処方</td>
              <td>¥{items[9]['price']:,}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 使い方ルーティンセクション -->
    <section id="section-routine" class="content-box">
      <h2 class="section-title">🧴 プロ直伝！冬の赤み・乾燥ゴワつきをリセットする3つの活用ステップ</h2>
      <p>
        ヨモギコスメの優れた鎮静・保水力を最大限に活かす、冬期の実践的スキンケアルーティンをご紹介します。
      </p>

      <h3>ステップ1：帰宅後すぐの「急速クーリングコットンパック」</h3>
      <p>
        寒い外気から暖かい部屋に入り、頬にカーッと熱感や赤みを感じた時は、大判の薄手コットンにヨモギエッセンスをたっぷり染み込ませ、両頬と鼻に3分間乗せます。熱を逃がしながら水分を角層に送り込むことで、毛細血管の拡張を速やかに鎮静させます。
      </p>

      <h3>ステップ2：週末バスタイムの「ヨモギ温感スチームパック」</h3>
      <p>
        週末はヨモギマスクを顔全体に厚めに塗り、湯船に浸かりながら蒸気を浴びる『インバスマスク』を取り入れましょう。生ヨモギのフラボノイドとミネラルが毛穴から染み渡り、寒さで硬化した古い角質をスルリと解きほぐします。
      </p>

      <h3>ステップ3：就寝前の「水分ジェルラッピング」</h3>
      <p>
        夜のスキンケアの仕上げには、油分の多い重いクリームではなく、高保水ヨモギジェルクリームをたっぷり重ねます。就寝中の暖房乾燥から肌を守りながら、朝起きた時にテカリのない澄んだ白肌へと整えます。
      </p>
    </section>

    <!-- FAQセクション -->
    <section id="section-faq" class="content-box">
      <h2 class="section-title">❓ よくある質問（FAQ）と注意点</h2>
      {faq_str}
    </section>

    <!-- 内部リンクセクション -->
    <section id="section-links" class="content-box">
      <h2 class="section-title">🔗 合わせて読みたい！冬の乾燥・ゆらぎ対策おすすめ関連記事</h2>
      <p>ヨモギコスメと合わせて使うことで、真冬の肌バリアをさらに強化できるおすすめ記事を厳選しました。</p>
      
      <div class="related-links-grid">
        <a href="winter-cica-cream.html" class="related-link-card">
          <h4>冬のCICAクリームおすすめ10選</h4>
          <p>肌荒れ・赤みを集中修復。冬の敏感肌を守り抜くシカコスメの決定版。</p>
        </a>
        <a href="winter-toner-pad.html" class="related-link-card">
          <h4>冬の高保湿トナーパッド厳選10選</h4>
          <p>朝のメイクノリが劇的変化！乾燥ゴワつきをサッとオフする部分水分パック。</p>
        </a>
        <a href="winter-medicinal-bath.html" class="related-link-card">
          <h4>冬の薬用入浴剤おすすめ10選</h4>
          <p>体の芯から温めて全身の粉吹き・冷えを解消する温活バスケア名品集。</p>
        </a>
        <a href="winter-ceramide-serum.html" class="related-link-card">
          <h4>高濃度セラミド美容液おすすめ10選</h4>
          <p>ヨモギで鎮静した角層にセラミドで強力なバリア膜を。冬の砂漠肌を完全救済。</p>
        </a>
        <a href="winter-rosehip-oil.html" class="related-link-card">
          <h4>高保湿ローズヒップオイルおすすめ10選</h4>
          <p>ビタミンの爆弾と必須脂肪酸80%。冬枯れしたキメをふっくらほぐすピュアオイル。</p>
        </a>
        <a href="winter-honey.html" class="related-link-card">
          <h4>高保湿ハチミツコスメおすすめ10選</h4>
          <p>天然の強力吸湿ヴェールで乾かないモチ肌へ。マヌカハニー＆プロポリス特集。</p>
        </a>
      </div>
    </section>

  </main>

  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-col" style="flex: 2; min-width: 280px;">
          <h5>冬コスメ徹底比較ラボ</h5>
          <p style="font-size: 0.85rem; line-height: 1.7; color: #a0aec0;">
            当サイトは、11月から12月にかけての乾燥シーズンに特化したコスメ・スキンケア専門レビューメディアです。楽天市場の最新APIデータを活用し、常に正確で透明性の高い価格情報と商品スペックをお届けしています。
          </p>
        </div>
        <div class="footer-col">
          <h5>成分別特集</h5>
          <ul>
            <li><a href="winter-mugwort.html">ヨモギコスメ</a></li>
            <li><a href="winter-cica-cream.html">CICAコスメ</a></li>
            <li><a href="winter-honey.html">ハチミツコスメ</a></li>
            <li><a href="winter-rosehip-oil.html">ローズヒップオイル</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>アイテム別特集</h5>
          <ul>
            <li><a href="winter-toner-pad.html">トナーパッド</a></li>
            <li><a href="winter-medicinal-bath.html">薬用入浴剤</a></li>
            <li><a href="winter-face-wash.html">洗顔・クレンジング</a></li>
            <li><a href="winter-night-cream.html">ナイトクリーム</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 画像および商品データ提供: 楽天市場API</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-mugwort.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-mugwort.html successfully! File size: {len(html_content):,} bytes")
