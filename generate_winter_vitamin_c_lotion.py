import json
import html

with open("fetched_3new_nov_dec_2026_1121.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_vitamin_c_lotion"]["items"]

details = [
    {
        "rank": 1,
        "vc_type": "高浸透ビタミンC (APPS) + ナイアシンアミド",
        "display_name": "VC100エッセンスローションEX V 150mL",
        "texture": "とろみリッチ（美容液に近い濃密感）",
        "scent": "爽やかなグレープフルーツ系",
        "capacity": "150mL",
        "moist_partners": "ヒアルロン酸、コラーゲン、ナイアシンアミド",
        "summary": "「ビタミンC化粧水はさっぱりして冬は乾く」という先入観を覆す、とろみ系VCローションの代表格",
        "p1": "ドクターシーラボの『VC100エッセンスローションEX V』は、水溶性と油溶性の両方の性質を持つ高浸透ビタミンC誘導体（APPS）を高濃度で配合しつつ、まるで美容液のような濃密なとろみを持たせた化粧水です。冬の冷気で毛穴が開いたりキメがしぼんだりして見える肌にも、手のひらで優しく押し込むとすーっと馴染んでふっくらとしたツヤを残します。",
        "p2": "リニューアルを重ねてナイアシンアミドなどの整肌・保湿サポート成分も充実しており、11月・12月の乾燥によるくすみ感と毛穴の目立ちを同時にケアしたい方にぴったり。コットンで拭き取るより、清潔な手のひらに500円玉大を出して2回に分けてハンドプレスすると、もっちりとした吸い付き感をより引き出せます。",
        "fit": "冬の頬の乾燥毛穴と夕方くすみが気になる方、化粧水の段階からしっかり保湿手応えが欲しい方",
        "caution": "高濃度なぶん、肌が極端に荒れてヒリついている日はまず少量を顎下で試してから全顔に使うと安心です。"
    },
    {
        "rank": 2,
        "vc_type": "アスコルビン酸誘導体 + グルタチオン + ナイアシンアミド",
        "display_name": "5番 白玉グルタチオンCエッセンシャル化粧水 (トナー) 200mL",
        "texture": "ほどよいとろみ（伸びが良くベタつきにくい）",
        "scent": "ほぼ無香（原料由来の穏やかな香り）",
        "capacity": "200mL",
        "moist_partners": "パンテノール、ヒアルロン酸、グルタチオン、ナイアシンアミド5%",
        "summary": "2,000円以下でグルタチオン・ナイアシンアミド・ビタミンC誘導体をまとめて摂れる韓国発の実力派",
        "p1": "ナンバーズインの『5番トナー』は、冬の寒さで顔色がどんより青白く冴えないときや、乾燥によるキメの乱れが気になるときに頼りになる1本です。白玉ケアで人気のグルタチオンに加えて、ビタミンC誘導体やナイアシンアミド5%（50,000ppm）、パンテノールまで詰め込まれており、単なるさっぱり系トナーとは一線を画すしっとり感があります。",
        "p2": "手に出すとややとろみがありますが、肌に広げるとスッと軽やかに馴染んでベタつきません。重ね付けしてもモロモロしにくいため、冬場のエアコン部屋で過ごす日は2〜3回レイヤリングして水分をたっぷり入れ込んでから乳液・クリームでフタをすると、翌朝の肌トーンが均一に整いやすくなります。",
        "fit": "冬の血行不良くすみやトーンダウンが気になる方、手頃な価格で成分充実の韓国化粧水を試したい方",
        "caution": "さっぱり寄りの仕上がりなので、乾燥肌の方は必ず仕上げにセラミド乳液やクリームを重ねてください。"
    },
    {
        "rank": 3,
        "vc_type": "3-O-エチルアスコルビン酸（高浸透ビタミンC誘導体）",
        "display_name": "薬用しみ対策美白化粧水 しっとりタイプ 170mL (医薬部外品)",
        "texture": "とろみあり（なめらかで垂れにくい）",
        "scent": "柑橘系のフレッシュな香り",
        "capacity": "170mL",
        "moist_partners": "グリチルリチン酸ジカリウム（抗炎症）、アルピニアホワイト、レモンエキス",
        "summary": "1,000円前後で買える医薬部外品。肌荒れ防止成分も入っており冬のゆらぎ予防にも重宝",
        "p1": "ロート製薬『メラノCC』の化粧水には通常タイプと「しっとりタイプ」があり、11月・12月に選ぶなら断然こちらのしっとりタイプです。有効成分の高浸透ビタミンC誘導体（3-O-エチルアスコルビン酸）がメラニンの生成を抑えてシミ・そばかすを防ぎつつ、抗炎症有効成分グリチルリチン酸ジカリウムが冬場の乾燥やマスク摩擦による赤み・ニキビを防いでくれます。",
        "p2": "通常タイプに比べると程よいとろみがあり、手でそのまま塗りやすいテクスチャー。¥990（調査時点）という手頃さなので、顔だけでなく乾燥しやすい首筋やデコルテ、手の甲のトーンケアまで遠慮なく使えるのが大きな強みです。ドラッグストアで詰め替え用が手に入りやすい点も続けやすさにつながります。",
        "fit": "プチプラでしっかり潤う美白・ニキビ予防化粧水を探している方、首やデコルテまでまとめてケアしたい方",
        "caution": "清涼感のある柑橘系の香りが付いているため、無香料派の方やアルコールに非常に敏感な方は確認の上で選んでください。"
    },
    {
        "rank": 4,
        "vc_type": "ピュアビタミンC + 3種のビタミンC誘導体",
        "display_name": "クリアアドバンスドローション 150mL",
        "texture": "とろみのある濃厚エッセンス状（浸透後はなめらか）",
        "scent": "ほのかなシトラス系",
        "capacity": "150mL",
        "moist_partners": "コラーゲンサポート成分、リファインコントロール成分",
        "summary": "製薬会社のビタミンC研究が凝縮されたオバジの本気ローション。冬のゴワつき・くすみに鋭くアプローチ",
        "p1": "ロート製薬の皮膚科学研究ブランド・オバジから登場した『オバジC クリアアドバンスドローション』は、即効性の高いピュアビタミンCと安定性に優れた複数のビタミンC誘導体を組み合わせた設計です。冬は古い角質が剥がれにくくなって肌全体がゴワつき、透明感が失われやすいですが、このローションはとろみのある液が角層をほぐすように浸透していきます。",
        "p2": "150mLで¥4,950（調査時点）と中価格帯ではありますが、1回あたりの使用量が少量でも顔全体に十分行き渡るほど濃密です。使った直後の肌は表面がツルンと整い、光の反射がきれいに出るため、冬の朝に使うとベースメイクの仕上がりに明らかな差が出ます。",
        "fit": "プチプラのVC化粧水では変化を感じにくくなった方、乾燥によるゴワつきとくすみを本気でケアしたい方",
        "caution": "ピュアビタミンC配合品は開封後なるべく早めに使い切り、直射日光を避けた涼しい場所で保管してください。"
    },
    {
        "rank": 5,
        "vc_type": "4種の濃厚ビタミンC（APPS・アスコルビン酸等）",
        "display_name": "ダーマレーザー スーパーVC100ローション (しっとり) 240mL",
        "texture": "まろやかなとろみ（肌あたりが柔らかい）",
        "scent": "ほのかなシトラス精油系",
        "capacity": "240mL",
        "moist_partners": "水添レシチンナノカプセル、ナイアシンアミド、ガラクトミセス培養液",
        "summary": "大ヒットしたシートマスクの浸透技術を化粧水に応用。240mLの大容量でこの価格帯は圧巻",
        "p1": "シートマスクが各所でベストコスメを獲得したクオリティファーストの『ダーマレーザー』シリーズから出ている化粧水。生体膜に近いナノカプセルに4種のビタミンCを閉じ込め、角層への浸透スピードを高めています。「しっとり」タイプはガラクトミセス培養液やナイアシンアミドもしっかり配合され、冬の乾燥肌でもつっぱりにくい処方です。",
        "p2": "240mLという大きめボトルで¥1,650（調査時点）とコストパフォーマンスが非常に高く、バシャバシャたっぷり使いたい人やコットンパックをしたい人にも向いています。防腐剤フリー・アルコールフリー・無着色といった低刺激設計へのこだわりも、冬のデリケートな肌には心強いポイントです。",
        "fit": "大容量で気兼ねなく使える高濃度ビタミンC化粧水が欲しい方、アルコールフリーにこだわりたい方",
        "caution": "とろみがあるぶんボトルを強く振ると出しすぎることがあるので、手のひらに少しずつ出して重ね付けするのがおすすめです。"
    },
    {
        "rank": 6,
        "vc_type": "リン酸L-アスコルビルマグネシウム（APS 6%高配合）",
        "display_name": "薬用ホワイトニングローションαEX 120mL (医薬部外品)",
        "texture": "みずみずしい軽め（イオン導入にも対応）",
        "scent": "無香料",
        "capacity": "120mL",
        "moist_partners": "グリチルリチン酸ジカリウム、高保湿アミノ酸系湿潤成分",
        "summary": "ビタミンC誘導体APSを医薬部外品として高配合。イオン導入器ユーザーや皮脂・赤み悩みにも定評",
        "p1": "成分派スキンケアブランド・トゥヴェールのロングセラー化粧水『薬用ホワイトニングローションαEX』。水溶性ビタミンC誘導体（リン酸L-アスコルビルマグネシウム）を贅沢に配合しており、冬でも暖房の効いた室内でTゾーンがテカりやすい混合肌や、大人ニキビ・赤みが残りやすい肌に高い人気があります。",
        "p2": "テクスチャー自体は他の濃厚とろみ系に比べるとサラリと軽めですが、刺激を抑えた保湿アミノ酸成分が組まれており、化粧水を入れた後にセラミドミルクやクリームで蓋をする前提なら冬のインナードライケアに非常に適しています。美顔器のイオン導入にも対応しているため、週末のスペシャルケアにも活躍します。",
        "fit": "Tゾーンの皮脂くすみや毛穴目立ちが気になる混合肌の方、美顔器（イオン導入）と併用したい方",
        "caution": "単体だと冬場はややさっぱり感じるため、セラミド配合の乳液やクリームとのセット使いを前提にしてください。"
    },
    {
        "rank": 7,
        "vc_type": "速攻型ビタミンC誘導体 + ハイドロキノン誘導体（アルブチン）",
        "display_name": "ラグジュアリーホワイト ローションAO II 120mL",
        "texture": "濃厚なとろみ（しっとり包み込む系）",
        "scent": "上品なカモミール・ローズ系",
        "capacity": "120mL",
        "moist_partners": "ヒト型セラミド（セラミド1・3・6II）、プラセンタエキス、α-リポ酸",
        "summary": "セラミド3種とα-リポ酸を内包した「AOカプセル」配合。エイジング世代の冬の透明感ケアに最適",
        "p1": "ドクターズコスメ・アンプルールの看板化粧水『ローションAO II』は、ビタミンC誘導体だけでなくα-リポ酸やプラセンタエキス、さらに3種類のヒト型セラミドまでを「AOカプセル」に閉じ込めて配合した高保湿ブライトニング化粧水です。冬の冷えによる暗いくすみと、深刻な乾燥による小ジワの両方が気になる大人肌に寄り添う処方になっています。",
        "p2": "少し白濁したまろやかな液体で、肌に伸ばすと吸いつくようなしっとり感が生まれます。「ビタミンC化粧水を使うとどうしても乾く」と諦めていた乾燥肌の方ほど、このセラミド入りのリッチな保湿感に満足しやすいはずです。やさしい植物系の香りも心地よく、夜のお手入れが楽しみになります。",
        "fit": "30代〜50代以上で乾燥によるくすみ・ハリ不足の両方をケアしたい方、セラミド入りVC化粧水を探している方",
        "caution": "とろみが濃いため、夏場に使っていたときと同じ感覚でたくさん塗るより、適量をハンドプレスでじんわり温めながら馴染ませると快適です。"
    },
    {
        "rank": 8,
        "vc_type": "リン酸アスコルビルMg + ナイアシンアミド + グルタチオン",
        "display_name": "薬用Cクリアホワイトローション 120mL (医薬部外品)",
        "texture": "みずみずしくコクのあるクリア質感",
        "scent": "天然精油（ハーバルオレンジ系）",
        "capacity": "120mL",
        "moist_partners": "グリチルリチン酸2K、グルタチオン、10種のビタミン複合体、ヒアルロン酸",
        "summary": "美容皮膚科発想のドクターケイが贈るカクテルビタミン処方。毛穴・くすみ・大人ニキビを全方位ケア",
        "p1": "ビタミン研究の第一人者として知られる青山ヒフ科クリニック監修のドクターケイ。『薬用Cクリアホワイトローション』は、ビタミンC誘導体を筆頭にナイアシンアミドやパントテン酸など複数のビタミン群とグルタチオンを絶妙なバランスで組み合わせた医薬部外品です。",
        "p2": "冬のオフィスは空気が乾燥している一方で、暖房の熱とストレスで皮脂が酸化し、鼻周りや頬の毛穴が黒ずんで見えがちです。この化粧水はベタつかないのに角層をみずみずしく満たし、天然精油の爽やかな香りとともに肌キメをきゅっと引き締めてくれます。レビュー件数190件超・★4.6台（調査時点）というリピーターの厚さも信頼の証です。",
        "fit": "毛穴の黒ずみ・開きと冬の乾燥くすみをまとめて整えたい方、皮膚科医監修のビタミン処方に魅力を感じる方",
        "caution": "天然精油の香りがしっかりあるタイプなので、完全に無香料の製品のみを使いたい方はご注意ください。"
    },
    {
        "rank": 9,
        "vc_type": "安定型ビタミンC誘導体 + アルブチン（W美白）",
        "display_name": "美白化粧水 VC&AR しっとりタイプ 180mL (医薬部外品)",
        "texture": "とろみ強めのまろやか質感",
        "scent": "無香料・無着色",
        "capacity": "180mL",
        "moist_partners": "ヒアルロン酸、トレハロース、グリチルリチン酸2K",
        "summary": "ビタミンC誘導体×アルブチンのW美白有効成分にヒアルロン酸とトレハロースをプラスした高コスパ処方",
        "p1": "ちふれの『美白化粧水 VC&AR しっとりタイプ』は、安定型ビタミンC誘導体とアルブチンという2つの美白有効成分に加え、肌荒れ防止のグリチルリチン酸2Kまで配合した医薬部外品です。しっとりタイプにはヒアルロン酸と保水糖トレハロースがしっかり入っており、プチプラ美白系にありがちな「塗ったあとカサつく感じ」を抑えています。",
        "p2": "180mLで¥1,650（調査時点）と手に取りやすく、無香料・無着色でクセがありません。とろっとした液が手のひらからこぼれにくく、冬の寒い日でも首元までしっかり伸ばせます。詰め替え用も展開されているため、冬場の毎日用サブ化粧水としても優秀です。",
        "fit": "無香料・プチプラで冬の乾燥対策と美白ケアの両方を無理なく続けたい方",
        "caution": "とろみがやや強めなので、朝のメイク前につけすぎると少しペタペタしやすい点だけ量を調整してください。"
    },
    {
        "rank": 10,
        "vc_type": "ビタミンC誘導体 + トラネキサム酸（抗炎症美白）",
        "display_name": "白潤プレミアム 薬用浸透美白化粧水 しっとりタイプ 170mL (医薬部外品)",
        "texture": "美容液級のまろやかとろみ",
        "scent": "無香料・弱酸性・アルコールフリー",
        "capacity": "170mL",
        "moist_partners": "ホワイトトラネキサム酸、グリチルリチン酸2K、2種のナノ化ヒアルロン酸、ビタミンE",
        "summary": "1,000円以下の神コスパ！ビタミンC誘導体×トラネキサム酸×ヒアルロン酸の隙のない布陣",
        "p1": "肌ラボの『白潤プレミアム しっとりタイプ』は、美白有効成分のトラネキサム酸と抗炎症のグリチルリチン酸2Kを主軸に据えつつ、整肌保湿成分としてビタミンC誘導体・ビタミンE・2種のナノ化ヒアルロン酸を贅沢に組み合わせた1本です。紫外線ダメージだけでなく、冬の寒暖差による赤みや摩擦くすみが気になる肌を穏やかに整えます。",
        "p2": "無香料・無着色・鉱物油フリー・アルコール（エタノール）フリー・パラベンフリーと低刺激への配慮が徹底されており、冬に肌が揺らぎやすい方でも使いやすいのが魅力です。¥978（調査時点）という価格からは想像できないほどリッチなうるおい感で、重ね付けしてもしっとりモチモチの後肌が続きます。",
        "fit": "アルコールフリーのプチプラ化粧水で、冬の乾燥・赤み予防・透明感ケアを全部叶えたい方",
        "caution": "とろみ系のため、脂性肌でさっぱり仕上がりを求める方は同シリーズの通常タイプの方が合う場合があります。"
    }
]

article_title = "冬のくすみも乾燥毛穴もまとめて潤す！しっとり高保湿ビタミンC化粧水おすすめランキング10選【11月・12月版】"
article_desc = "「ビタミンC化粧水は冬につっぱる」はもう古い！11月・12月の乾燥くすみ・暖房皮脂毛穴をまとめてケアできる、セラミドやヒアルロン酸・ナイアシンアミド配合の高保湿ビタミンC誘導体化粧水10選（VC100、ナンバーズイン5番、メラノCCしっとり、オバジC等）を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-vitamin-c-lotion"

json_ld_graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": article_title,
            "description": article_desc,
            "image": items[0]["image_url"],
            "datePublished": "2026-11-21T05:00:00+09:00",
            "dateModified": "2026-11-21T05:00:00+09:00",
            "author": {"@type": "Organization", "name": "Lumi Cosme 編集部"},
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme (ルミコスメ)",
                "logo": {"@type": "ImageObject", "url": "https://lumi-cosme.vercel.app/favicon.jpg"}
            }
        },
        {
            "@type": "ItemList",
            "name": "11月・12月向け高保湿ビタミンC化粧水ランキング10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["summary"],
                        "brand": {"@type": "Brand", "name": it["brand"]},
                        "offers": {
                            "@type": "Offer",
                            "price": it["price"],
                            "priceCurrency": "JPY",
                            "availability": "https://schema.org/InStock",
                            "url": it["affiliate_url"]
                        },
                        **(
                            {
                                "aggregateRating": {
                                    "@type": "AggregateRating",
                                    "ratingValue": str(it["review_average"]),
                                    "reviewCount": int(it["review_count"])
                                }
                            }
                            if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
                            else {}
                        )
                    }
                }
                for it, det in zip(items, details)
            ]
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "ビタミンC化粧水は冬に使うと乾燥しませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "かつてのさっぱり系ピュアビタミンC化粧水は皮脂を抑える力が強く乾燥しやすい傾向がありましたが、現在の高保湿タイプはAPPSや3-O-エチルアスコルビン酸などの安定型誘導体に加え、ヒアルロン酸・セラミド・ナイアシンアミド・グリチルリチン酸2Kなどを併用しているため、冬でもしっかりとした潤いを感じられます。化粧水のあとに乳液やクリームでフタをすれば乾燥の心配はほぼありません。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "朝のスキンケアにビタミンC化粧水を使っても日焼けしませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "『ビタミンCを朝塗ると日焼けしやすくなる（ソラレンのような光毒性がある）』というのは誤解です。むしろビタミンCには日中の紫外線や大気ストレスによる酸化を防ぐ働きがあるため、朝のスキンケアにも積極的に取り入れることが推奨されています。もちろん朝は仕上げに日焼け止めやUV下地を併用してください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "とろみのあるビタミンC化粧水はコットンと手、どちらで付けるのが良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "とろみ系の化粧水はコットンに染み込みきらず肌表面で摩擦になりやすいため、基本的には『清潔な手のひら』で温めながらハンドプレスするのがおすすめです。2回に分けてゆっくり押し込むと角層へ均一に入りやすくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "レチノール美容液やクリームと併用しても大丈夫ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "一般的な保湿型ビタミンC誘導体化粧水であれば、保湿クリームや低刺激レチノールと併用しても問題ないケースが多いです。ただし、ピュアビタミンCの高濃度品と高濃度レチノールを同時に使うと刺激を感じることがあるため、敏感肌の方は『朝＝ビタミンC化粧水、夜＝レチノール』と時間帯を分けると安心です。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬の高保湿化粧水特集", "item": "https://lumi-cosme.vercel.app/winter-lotion"},
                {"@type": "ListItem", "position": 3, "name": "高保湿ビタミンC化粧水10選", "item": canonical_url}
            ]
        }
    ]
}

rows_html = ""
for it, det in zip(items, details):
    rows_html += f"""            <tr>
              <td><span class="vc-rank">{it['rank']}位</span></td>
              <td><strong>{html.escape(it['brand'])}</strong><br><span class="sub-txt">{html.escape(det['display_name'])}</span></td>
              <td>{html.escape(det['vc_type'])}</td>
              <td>{html.escape(det['moist_partners'].split('、')[0])}・{html.escape(det['moist_partners'].split('、')[1]) if '、' in det['moist_partners'] else ''}</td>
              <td>{html.escape(det['texture'].split('（')[0])}</td>
              <td class="vc-price">¥{it['price']:,}<br><span class="sub-txt">{html.escape(det['capacity'])}</span></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rev_txt = (
        f'<span class="rev-tag">★ {it["review_average"]} ({it["review_count"]:,}件のレビュー)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="rev-tag">楽天市場 取扱人気アイテム</span>'
    )
    cards_html += f"""
      <article class="vc-card" id="rank-{it['rank']}">
        <header class="vc-card-head">
          <div class="vc-badges">
            <span class="rank-chip r-{it['rank']}">RANK {it['rank']}</span>
            <span class="vc-type-chip">{html.escape(det['vc_type'])}</span>
            {rev_txt}
          </div>
          <h3>{html.escape(it['brand'])} / {html.escape(det['display_name'])}</h3>
        </header>

        <div class="vc-card-layout">
          <div class="vc-left">
            <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            <div class="vc-price-box">
              <span>参考価格（税込）</span>
              <strong>¥{it['price']:,}</strong>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天で最新価格・在庫をチェック →
            </a>
            <div class="item-caption">楽天掲載名：{html.escape(it['item_name'][:48])}</div>
          </div>

          <div class="vc-right">
            <p class="vc-summary">{html.escape(det['summary'])}</p>
            <div class="vc-meta-grid">
              <div><span>容量</span><strong>{html.escape(det['capacity'])}</strong></div>
              <div><span>質感</span><strong>{html.escape(det['texture'])}</strong></div>
              <div><span>香り</span><strong>{html.escape(det['scent'])}</strong></div>
              <div><span>保湿パートナー</span><strong>{html.escape(det['moist_partners'])}</strong></div>
            </div>
            <p class="vc-prose">{html.escape(det['p1'])}</p>
            <p class="vc-prose">{html.escape(det['p2'])}</p>
            <div class="vc-notes">
              <div class="note-fit"><strong>おすすめな人：</strong>{html.escape(det['fit'])}</div>
              <div class="note-caution"><strong>使い方のコツ・注意点：</strong>{html.escape(det['caution'])}</div>
            </div>
          </div>
        </div>
      </article>
"""

html_doc = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(article_title)} | Lumi Cosme</title>
  <meta name="description" content="{html.escape(article_desc)}">
  <meta name="keywords" content="ビタミンC 化粧水 冬, 高保湿 ビタミンC誘導体 化粧水, 11月 12月 くすみ 毛穴 化粧水, VC100エッセンスローションEX, ナンバーズイン 5番, メラノCC しっとり, オバジC, ドクターケイ">
  <link rel="canonical" href="{canonical_url}">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="article">
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="{html.escape(article_title)}">
  <meta property="og:description" content="{html.escape(article_desc)}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{html.escape(items[0]['image_url'])}">
  <meta property="og:locale" content="ja_JP">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
{json.dumps(json_ld_graph, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --accent: #d97706;
      --accent-dark: #b45309;
      --accent-bg: #fefce8;
      --accent-line: #fde68a;
      --text: #1e293b;
      --muted: #64748b;
      --border: #e2e8f0;
      --page: #fffdf7;
      --card: #ffffff;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--page);
      color: var(--text);
      line-height: 1.75;
    }}
    .site-nav {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .site-nav-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .logo {{ font-weight: 800; font-size: 1.15rem; color: var(--text); text-decoration: none; }}
    .nav-links {{ display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.85rem; }}
    .nav-links a {{ color: var(--accent-dark); text-decoration: none; font-weight: 700; }}
    .crumb {{
      max-width: 1080px;
      margin: 14px auto 0;
      padding: 0 20px;
      font-size: 0.82rem;
      color: var(--muted);
    }}
    .crumb a {{ color: var(--accent-dark); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .intro-banner {{
      background: linear-gradient(135deg, #fefce8 0%, #fef3c7 100%);
      border: 1px solid var(--accent-line);
      border-radius: 14px;
      padding: 36px 30px;
      margin-bottom: 30px;
    }}
    .intro-kicker {{
      display: inline-block;
      background: var(--accent);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .intro-banner h1 {{
      font-size: 1.75rem;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    @media (max-width: 720px) {{
      .intro-banner {{ padding: 24px 18px; }}
      .intro-banner h1 {{ font-size: 1.35rem; }}
    }}
    .meta-line {{ font-size: 0.83rem; color: var(--muted); margin-bottom: 16px; }}
    .intro-banner p {{ font-size: 0.97rem; color: #334155; margin-bottom: 10px; }}
    .intro-banner p:last-child {{ margin-bottom: 0; }}

    .toc-wrap {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 30px;
    }}
    .toc-wrap h2 {{ font-size: 1.05rem; margin-bottom: 12px; }}
    .toc-wrap ol {{
      padding-left: 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px 20px;
    }}
    .toc-wrap a {{ color: var(--accent-dark); text-decoration: none; font-weight: 600; font-size: 0.9rem; }}
    .toc-wrap a:hover {{ text-decoration: underline; }}

    .sec-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 30px;
    }}
    .sec-card h2 {{
      font-size: 1.35rem;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--accent-line);
    }}
    .sec-card p {{ font-size: 0.95rem; color: #334155; margin-bottom: 14px; }}
    .matrix-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}
    .matrix-item {{
      background: var(--accent-bg);
      border: 1px solid var(--accent-line);
      border-radius: 10px;
      padding: 18px;
    }}
    .matrix-item h3 {{ font-size: 1rem; color: var(--accent-dark); margin-bottom: 8px; }}
    .matrix-item p {{ font-size: 0.87rem; margin-bottom: 0; }}

    .table-scroll {{ overflow-x: auto; margin-top: 14px; }}
    .vc-table {{ width: 100%; border-collapse: collapse; font-size: 0.86rem; min-width: 650px; }}
    .vc-table th, .vc-table td {{ border: 1px solid var(--border); padding: 10px 12px; text-align: left; vertical-align: top; }}
    .vc-table th {{ background: #fef3c7; color: #78350f; font-weight: 700; white-space: nowrap; }}
    .vc-table tr:nth-child(even) {{ background: #fffdf7; }}
    .vc-rank {{ font-weight: 800; color: var(--accent-dark); white-space: nowrap; }}
    .vc-price {{ font-weight: 800; color: #be123c; white-space: nowrap; }}
    .sub-txt {{ font-size: 0.77rem; color: var(--muted); font-weight: 400; }}

    .list-title {{ font-size: 1.45rem; font-weight: 800; margin: 34px 0 18px; }}
    .vc-card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 26px;
      margin-bottom: 26px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }}
    .vc-card-head {{
      border-bottom: 1px solid var(--border);
      padding-bottom: 14px;
      margin-bottom: 18px;
    }}
    .vc-badges {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}
    .rank-chip {{
      background: var(--accent-dark);
      color: #fff;
      font-weight: 800;
      font-size: 0.85rem;
      padding: 4px 11px;
      border-radius: 6px;
    }}
    .rank-chip.r-1 {{ background: #ca8a04; }}
    .rank-chip.r-2 {{ background: #475569; }}
    .rank-chip.r-3 {{ background: #b45309; }}
    .vc-type-chip {{
      background: var(--accent-bg);
      border: 1px solid var(--accent-line);
      color: #92400e;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .rev-tag {{ font-size: 0.8rem; font-weight: 700; color: #b45309; margin-left: auto; }}
    .vc-card-head h3 {{ font-size: 1.22rem; color: #0f172a; line-height: 1.4; }}

    .vc-card-layout {{
      display: grid;
      grid-template-columns: 270px 1fr;
      gap: 24px;
    }}
    @media (max-width: 820px) {{
      .vc-card-layout {{ grid-template-columns: 1fr; }}
    }}
    .vc-left {{ display: flex; flex-direction: column; gap: 10px; }}
    .product-img {{
      width: 100%;
      max-height: 240px;
      object-fit: contain;
      border: 1px solid var(--border);
      border-radius: 10px;
      background: #fff;
      padding: 10px;
    }}
    .vc-price-box {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
    }}
    .vc-price-box span {{ display: block; font-size: 0.75rem; color: var(--muted); }}
    .vc-price-box strong {{ font-size: 1.4rem; color: #be123c; }}
    .rakuten-btn {{
      display: block;
      text-align: center;
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      color: #fff;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 13px 16px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ opacity: 0.92; }}
    .item-caption {{ font-size: 0.74rem; color: var(--muted); line-height: 1.4; }}

    .vc-summary {{
      background: var(--accent-bg);
      border-left: 4px solid var(--accent);
      padding: 10px 14px;
      font-weight: 700;
      color: #78350f;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
      font-size: 0.94rem;
    }}
    .vc-meta-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px 14px;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    @media (max-width: 560px) {{
      .vc-meta-grid {{ grid-template-columns: 1fr; }}
    }}
    .vc-meta-grid div span {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .vc-meta-grid div strong {{ color: #0f172a; }}
    .vc-prose {{ font-size: 0.93rem; color: #334155; margin-bottom: 12px; }}
    .vc-notes {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.86rem;
      margin-top: 12px;
    }}
    .note-fit {{ background: #f8fafc; border: 1px solid var(--border); padding: 10px 12px; border-radius: 8px; }}
    .note-caution {{ background: #fefce8; border: 1px solid var(--accent-line); padding: 10px 12px; border-radius: 8px; }}

    .faq-block {{ border-bottom: 1px solid var(--border); padding: 15px 0; }}
    .faq-block:last-child {{ border-bottom: none; }}
    .faq-block h3 {{ font-size: 1rem; margin-bottom: 6px; }}
    .faq-block p {{ font-size: 0.9rem; margin-bottom: 0; color: #334155; }}

    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 26px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-size: 1.15rem; font-weight: 800; margin-bottom: 16px; }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 14px;
    }}
    .internal-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--accent); }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 48px 20px 32px;
      font-size: 0.84rem;
    }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #f8fafc; font-weight: 800; font-size: 1rem; margin-bottom: 16px; }}
    .footer-links-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px 14px;
      margin-bottom: 28px;
    }}
    .footer-links-grid a {{ color: #cbd5e1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #fcd34d; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1e293b; padding-top: 20px; text-align: center; font-size: 0.78rem; }}
  </style>
</head>
<body>
  <header class="site-nav">
    <div class="site-nav-inner">
      <a href="/" class="logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/winter-lotion">化粧水特集</a>
        <a href="/winter-vitamin-c-serum">ビタミンC美容液</a>
        <a href="/winter-all-in-one">オールインワン</a>
      </nav>
    </div>
  </header>

  <nav class="crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-lotion">冬の高保湿化粧水特集</a> &gt; <span>高保湿ビタミンC化粧水10選</span>
  </nav>

  <main>
    <section class="intro-banner">
      <span class="intro-kicker">2026年11月・12月 ブライトニング＆保水ケア</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="meta-line">公開・検証：<time datetime="2026-11-21">2026年11月21日</time> ／ Lumi Cosme スキンケア調査チーム</div>
      <p>
        「ビタミンC化粧水は夏場に皮脂やテカリを抑えるためのもの」と思って、11月・12月になると引き出しの奥にしまってしまう方は少なくありません。しかし実際には、気温が下がる初冬から真冬こそ、<strong>血行不良による顔色のどんより感（くすみ）</strong>と、<strong>暖房の室内で酸化した皮脂による毛穴目立ち</strong>が同時に気になりやすい時期です。
      </p>
      <p>
        近年のビタミンC化粧水は、ピュアビタミンC一辺倒だった時代から大きく進化し、APPSや3-O-エチルアスコルビン酸といった低刺激・高浸透の誘導体に、ヒアルロン酸・セラミド・ナイアシンアミドを重ねた<strong>「しっとり系・とろみ系」</strong>が主流になっています。冬場でもつっぱりにくく、明るい印象と潤いの両方を狙える10本を厳選しました。
      </p>
    </section>

    <nav class="toc-wrap" aria-label="目次">
      <h2>本記事の内容</h2>
      <ol>
        <li><a href="#winter-vc">なぜ11月・12月に「しっとり系ビタミンC化粧水」が頼れるのか</a></li>
        <li><a href="#select-guide">つっぱらない誘導体の見分け方と質感セレクト</a></li>
        <li><a href="#vc-table">高保湿ビタミンC化粧水10選 スペック比較表</a></li>
        <li><a href="#ranking">冬におすすめの高保湿ビタミンC化粧水ランキング10選</a></li>
        <li><a href="#apply-method">冬の角層にしっかり届けるハンドプレス2段階手順</a></li>
        <li><a href="#faq">よくある疑問 Q&amp;A</a></li>
      </ol>
    </nav>

    <section class="sec-card" id="winter-vc">
      <h2>1. なぜ冬こそ「しっとり高保湿なビタミンC化粧水」が効くのか</h2>
      <p>
        11月から12月にかけて外気が冷えると、顔の皮膚表面の血流量が落ちて血色がくすみやすくなります。さらに乾燥によって角質細胞がめくれ上がると、光をきれいに反射できずに肌全体がグレーがかって見える「乾燥くすみ」が重なります。
      </p>
      <p>
        ここに保湿成分をたっぷり抱えたビタミンC誘導体化粧水を取り入れると、角層を水分でふっくら整えながら、皮脂酸化やくすみ印象に多角的にアプローチできます。ただし、エタノール比率が高く脱脂力の強いタイプを冬に使うと赤みやカサつきの原因になるため、<strong>「保湿成分（ヒアルロン酸・セラミド・グリセリン等）との組み合わせ」</strong>を見極めることが肝心です。
      </p>
    </section>

    <section class="sec-card" id="select-guide">
      <h2>2. 乾燥肌でも失敗しない！冬向けVC化粧水3つの見極め軸</h2>
      <div class="matrix-grid">
        <div class="matrix-item">
          <h3>① 誘導体の種類をチェック</h3>
          <p>水と油の両方に馴染みやすい「APPS（パルミチン酸アスコルビルリン酸3Na）」や、持続性の高い「3-O-エチルアスコルビン酸」「VCグルコシド」は、冬でもつっぱりにくい代表的な誘導体です。</p>
        </div>
        <div class="matrix-item">
          <h3>② 同時配合の「保湿パートナー」</h3>
          <p>ビタミンC単体ではなく、ヒト型セラミド・ナイアシンアミド・パンテノール・ナノ化ヒアルロン酸などが併記されているアイテムを選ぶと、塗った後のしっとり感が長く続きます。</p>
        </div>
        <div class="matrix-item">
          <h3>③ 冬の敏感肌はノンアルコール優先</h3>
          <p>頬が冷風でヒリつきやすい方や髭剃り後の男性が兼用する場合は、エタノール（アルコール）フリー設計やグリチルリチン酸2K配合の医薬部外品を選ぶと穏やかに使えます。</p>
        </div>
      </div>
    </section>

    <section class="sec-card" id="vc-table">
      <h2>3. 高保湿ビタミンC化粧水10選 比較一覧表</h2>
      <p>楽天市場の最新調査価格（税込）と、配合されているビタミンCの種類・質感を比較しました。</p>
      <div class="table-scroll">
        <table class="vc-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>主なビタミンC成分</th>
              <th>保湿・整肌パートナー</th>
              <th>質感</th>
              <th>価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{rows_html}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="list-title" id="ranking">4. 11月・12月向け 高保湿ビタミンC化粧水おすすめランキング10選</h2>
    <section aria-label="商品詳細レビュー">
{cards_html}    </section>

    <section class="sec-card" id="apply-method">
      <h2>5. 冬の冷えた肌にしっかり入る「2段階ハンドプレス」のコツ</h2>
      <div class="matrix-grid">
        <div class="matrix-item">
          <h3>ステップ1：手のひらを少し温める</h3>
          <p>冬の冷えた手でそのまま化粧水をつけると角層が締まって馴染みにくくなります。500円玉大を手のひらに出したら、両手を軽く合わせて人肌に温めてから顔に広げましょう。</p>
        </div>
        <div class="matrix-item">
          <h3>ステップ2：2回に分けて押し込む</h3>
          <p>とろみのあるVC化粧水を1回で大量に乗せると表面で滑ってしまいます。半量ずつ2回に分け、特に乾燥毛穴や頬のくすみが気になる箇所に手のひらで5秒ほど優しく密着させてください。</p>
        </div>
        <div class="matrix-item">
          <h3>ステップ3：30秒以内に乳液・クリーム</h3>
          <p>ビタミンC化粧水はあくまで「水分の土台づくり」です。肌がしっとり濡れているうちに、セラミド乳液や保湿クリームを重ねて油分のフタをすることで、朝まで潤いと透明感が保たれます。</p>
        </div>
      </div>
    </section>

    <section class="sec-card" id="faq">
      <h2>6. 冬のビタミンC化粧水 よくある質問（FAQ）</h2>
      <div class="faq-block">
        <h3>Q1. ビタミンC化粧水は朝使うとシミになりやすいというのは本当ですか？</h3>
        <p>いいえ、ビタミンC自体に紫外線を吸収してシミを作る光毒性はありません（柑橘類の皮に含まれるソラレンと混同されがちです）。むしろ日中の酸化ストレスから肌を守る働きがあるため、朝のお手入れにも安心して使えます。もちろん日中は日焼け止めの併用をおすすめします。</p>
      </div>
      <div class="faq-block">
        <h3>Q2. 敏感肌でも使える高保湿ビタミンC化粧水はどれですか？</h3>
        <p>アルコール（エタノール）無添加かつ抗炎症成分が入っている『ダーマレーザー スーパーVC100ローション（しっとり）』や『白潤プレミアム しっとりタイプ』、またはパンテノール入りの『ナンバーズイン 5番トナー』が比較的穏やかで取り入れやすい設計です。</p>
      </div>
      <div class="faq-block">
        <h3>Q3. 化粧水とビタミンC美容液はどちらを優先すべきですか？</h3>
        <p>「まずは日々の保湿と顔全体のトーンケアを手軽に始めたい」なら化粧水、「気になる頬のシミ・毛穴スポットを集中的にケアしたい」なら美容液が向いています。すでに高保湿なヒアルロン酸化粧水を使っている場合は、ポイントでビタミンC美容液を足す組み合わせも人気です。</p>
      </div>
      <div class="faq-block">
        <h3>Q4. 開封後は冷蔵庫に入れた方が良いですか？</h3>
        <p>多くの誘導体化粧水は常温安定性が高いため、直射日光の当たらない涼しい洗面所や室内での保管で問題ありません。ただし『オバジC』のようなピュアビタミンC配合品は品質を保つため、高温多湿を避けてなるべく2〜3ヶ月以内を目安に使い切るのが理想です。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-lotion" class="internal-link-card">
          <strong>冬の高保湿化粧水総合特集</strong>
          <span>乾燥肌を潤す定番・名品化粧水10選</span>
        </a>
        <a href="/winter-vitamin-c-serum" class="internal-link-card">
          <strong>高保湿ビタミンC美容液特集</strong>
          <span>集中ケア向けビタミンC美容液10選</span>
        </a>
        <a href="/winter-hyaluronic-lotion" class="internal-link-card">
          <strong>高保湿ヒアルロン酸化粧水特集</strong>
          <span>保水力に特化した化粧水10選</span>
        </a>
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">Lumi Cosme (ルミコスメ) 冬の高保湿特集一覧</div>
      <div class="footer-links-grid" id="footer-links-box">
        <a href="/">トップページ</a>
      </div>
      <p class="copyright">&copy; 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-vitamin-c-lotion.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-vitamin-c-lotion.html successfully!")
