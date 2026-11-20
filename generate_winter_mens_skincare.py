import json
import html

with open("fetched_3new_nov_dec_2026_1121.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_mens_skincare"]["items"]

details = [
    {
        "rank": 1,
        "category_tag": "化粧水（1本で乳液級の保水膜）",
        "display_name": "オルビス ミスター エッセンスローション 180mL (医薬部外品)",
        "alcohol": "アルコールフリー",
        "scent": "無香料",
        "capacity": "180mL",
        "key_spec": "グリチルリチン酸ジカリウム、D-パンテノール、銀杏葉エキス、ローヤルゼリーエキス",
        "gift_fit": "◎ 自分用にも清潔感あるギフトにも定番",
        "headline": "「ベタつく乳液は塗りたくない、でも冬は乾く」男性のために作られた1本完結型ローション",
        "text1": "オルビスのメンズライン『オルビス ミスター』で一番人気を誇るのがこのエッセンスローション。化粧水でありながら、肌に触れた瞬間にとろみがパシャッと弾け、角層内部に水分を抱え込みつつ表面には目に見えないうるおい保護膜を作ってくれます。男性が嫌いがちなヌルつきや油っぽさを徹底的に抑えながら、暖房の部屋でも頬が乾きにくい絶妙な処方です。",
        "text2": "医薬部外品として肌荒れ防止成分（グリチルリチン酸ジカリウム）を配合しているため、11月・12月の乾燥した朝の髭剃り後に起きやすいカミソリ負けや赤みの予防にもぴったり。無香料・アルコールフリーでクセがなく、スキンケア初心者からベテランまでまず失敗しない1本です。",
        "who": "洗顔後に何本も塗るのが面倒な方、髭剃り後のヒリつきと午後のテカリを同時に抑えたい方",
        "tip": "1〜2プッシュを手のひらに広げ、アゴや頬の髭剃りエリアを擦らずそっと押さえるように馴染ませてください。"
    },
    {
        "rank": 2,
        "category_tag": "デパコス高保湿化粧水（ギフト人気No.1級）",
        "display_name": "ハイドレーティング ローション C 150mL",
        "alcohol": "アルコール配合（※さっぱり系、保湿持続力◎）",
        "scent": "シトラスウッディの洗練された香り",
        "capacity": "150mL",
        "key_spec": "ツバキ種子エキス、シソエキス、独自トリプルツバキGLエキス（保湿）",
        "gift_fit": "👑 12月のクリスマス・誕生日ギフトの大本命",
        "headline": "資生堂のメンズプレステージライン。つけた瞬間スッと馴染み、冬のカサつきと過剰皮脂のバランスを整える",
        "text1": "11月・12月のクリスマスプレゼントや特別な贈り物として毎年指名買いが集中するのが『SHISEIDO MEN（資生堂メン）』のハイドレーティング ローション C。男性肌の「水分保持力は低いのに皮脂分泌は活発」という特性を研究し、ツバキ種子エキスなどを組み合わせた独自保湿成分が、冬場の乾燥によるゴワつきを穏やかに整えます。",
        "text2": "ボトルの質感も非常にスタイリッシュで、洗面台に置くだけで雰囲気が出るデザイン。使い心地はみずみずしく、塗った直後にスマートフォンや書類を触ってもベタつきにくいのに、肌の内側はもっちり潤うバランスは見事の一言。パートナーへの冬のギフトにも自分へのご褒美にも申し分ありません。",
        "who": "12月のクリスマスプレゼントを探している方、上質な使い心地と香りで毎日のケアを楽しみたい男性",
        "tip": "乾燥が特に厳しい真冬日は、手のひらで2回に分けて押し込んだあと、同ラインのモイスチャライザー等を薄く重ねると完璧です。"
    },
    {
        "rank": 3,
        "category_tag": "高保湿メンズ化粧水（リペア処方）",
        "display_name": "ザ リペアローション 100g",
        "alcohol": "低刺激処方（7つのフリー設計）",
        "scent": "爽やかなフローラルフルーティ系",
        "capacity": "100g",
        "key_spec": "リンゴ果実培養細胞エキス、トレハロース、ヒアルロン酸、セラミド様保湿成分",
        "gift_fit": "◎ トレンド感あるパウチ・ギフトにも人気",
        "headline": "乾燥による肌荒れ・かさつきに特化したバルクオムの高保湿ローション。潤いを抱えて逃がさない処方",
        "text1": "メンズスキンケアの知名度を大きく押し上げたバルクオムのなかでも、冬の乾燥やシェービング後のカサつきを気にする人に支持されているのが『ザ リペアローション』です。高い水分保持力を持つトレハロースやリンゴ果実培養細胞エキスなどの共通美容成分に加え、乾燥ダメージを受けやすい男性の角層にしっとりとどまる濃密な保湿設計を採用しています。",
        "text2": "とろっとしたまろやかな感触ながら、肌に伸ばすとベタつかずにスッと馴染みます。白いパウチ（またはボトル）のミニマルな見た目はおしゃれで、旅行や出張・ジムのシャワー後にも持ち運びやすいのが魅力。冬場、夕方になると口周りが白く粉を吹きやすい男性に特に向いています。",
        "who": "口周りや頬の粉吹き・つっぱりに悩んでいる男性、見た目もスマートな国内人気ブランドを使いたい方",
        "tip": "洗顔・髭剃り後、タオルで水気を取ってからすぐに500円玉大をなじませると角層への入りがスムーズです。"
    },
    {
        "rank": 4,
        "category_tag": "薬用オールインワンジェル（医薬部外品）",
        "display_name": "薬用オールインワンジェル モイストタイプ 100g (医薬部外品)",
        "alcohol": "アルコールフリー・7つの無添加",
        "scent": "爽やかなシトラス系",
        "capacity": "100g",
        "key_spec": "ヘパリン類似物質、グリチルリチン酸ジカリウム、プラセンタエキス、ナイアシンアミド",
        "gift_fit": "◎ コスパ・機能重視の男性に大好評",
        "headline": "ヘパリン類似物質×プラセンタ×グリチルリチン酸2K。冬のカサカサ乾燥肌を1本で立て直す実力派",
        "text1": "ネット通販を中心に男性から厚い信頼を集めるNULL（ヌル）の『薬用オールインワンジェル モイストタイプ』。注目すべきは、保湿有効成分のヘパリン類似物質と抗炎症のグリチルリチン酸ジカリウム、さらに美白有効成分プラセンタエキスまで配合した贅沢な医薬部外品処方である点です。",
        "text2": "モイストタイプは冬場の過酷な乾燥に耐えられるよう潤いの持続力を強化していますが、仕上がりは男性が好むサラッとした後肌。エタノール（アルコール）不使用なので、電動シェーバーやT字カミソリで剃った直後の敏感な頬につけてもしみにくく、冬の朝晩これ1本で完結させたい方に極めて使い勝手の良い設計です。",
        "who": "乾燥肌・敏感肌でアルコール入り化粧水がしみる男性、1本で保湿・髭剃り後ケア・美白まで済ませたい方",
        "tip": "ワンプッシュまたは適量を取り、顔全体に広げたあと、乾燥しやすい髭剃り跡にもう少しだけ薄く重ねると効果的です。"
    },
    {
        "rank": 5,
        "category_tag": "無添加オールインワン化粧液（2本セット）",
        "display_name": "メン オールインワン スキンコンディショナー II しっとり 60mL×2本",
        "alcohol": "アルコール（エタノール）フリー・無添加",
        "scent": "無香料",
        "capacity": "60mL×2本セット",
        "key_spec": "ムクロジエキス、日本酒（コメ発酵液）、植物性スクワラン、グリセリン",
        "gift_fit": "○ 敏感肌の男性・実用的まとめ買い向け",
        "headline": "防腐剤・香料・アルコール一切不使用。髭剃りで荒れた冬の超敏感肌にも優しいファンケルのしっとりゲル",
        "text1": "無添加化粧品の老舗ファンケルが男性の肌データをもとに開発した『ファンケル メン オールインワン スキンコンディショナー II しっとり』。化粧水・乳液・美容液の3役を1本に凝縮し、乾燥が厳しい11月〜12月でもしっかり潤いを閉じ込める「II しっとり」タイプです。",
        "text2": "アルコールや合成香料に反応して肌が赤くなりやすい男性にとって、ファンケルの無添加設計は大きな安心材料になります。みずみずしいジェル状で液だれしにくく、肌に伸ばすとベタつかずにスッと馴染んでしっとり整います。今回紹介の商品は2本セット（¥5,175・調査時点）のため、冬の間切らさずストックしておけるのも便利です。",
        "who": "冬になると髭剃り負けで頬が真っ赤になる敏感肌の男性、無香料・ノンアルコールの安心感を求める方",
        "tip": "1回の使用目安は3〜4プッシュ。無添加処方でフレッシュさを保つため、1本あたり開封後60日を目安に使い切りましょう。"
    },
    {
        "rank": 6,
        "category_tag": "ボタニカル高保湿オールインワンジェル",
        "display_name": "モイスチュアライジング ジェル 230mL",
        "alcohol": "エタノール含有量控えめ・植物由来処方",
        "scent": "天然香料使用のウッディシトラス",
        "capacity": "230mL（大容量ポンプ）",
        "key_spec": "エーデルワイスエキス、セージ葉エキス、アストロカリウムムルムル種子脂、セラミド様成分",
        "gift_fit": "◎ 男女兼用・おしゃれなポンプギフトにも",
        "headline": "コーセー発・植物の恵みを凝縮した230mL大容量ポンプ。自然派の香りと抜群のコスパが魅力",
        "text1": "KOSEのジェンダーレス・メンズ向けスキンケアライン『magnifique（マニフィーク）』のモイスチュアライジング ジェルは、230mLというたっぷり使えるポンプボトルで¥2,750（調査時点）という高いコストパフォーマンスが光ります。化粧水・乳液・美容液が1本になったオールインワン仕様です。",
        "text2": "天然由来の保湿成分やムルムルバター由来のエモリエント成分がバランスよく溶け込んでおり、冬の冷たい空気で硬くなった男性の角層を柔らかくほぐしてくれます。天然精油由来のウッディな香りは落ち着きがあり、朝晩のケアがちょっとしたリフレッシュ時間に変わります。パッケージも洗練されていてプレゼントにも喜ばれます。",
        "who": "毎日たっぷり惜しみなく使いたい男性、ウッディ系の自然で爽やかな香りが好きな方",
        "tip": "ポンプ式なので洗面台に置いておき、お風呂上がりや朝の洗顔後すぐ1〜2プッシュをサッと顔と首元まで伸ばすのが習慣化しやすくておすすめです。"
    },
    {
        "rank": 7,
        "category_tag": "1本4役・ボタニカルオールインワンローション",
        "display_name": "ボタニカル ローション ＆ アフターシェーブ 115mL",
        "alcohol": "アルコールフリー（低刺激）",
        "scent": "ベルガモット＆ローズマリー精油",
        "capacity": "115mL",
        "key_spec": "4種の植物エキス（ビルベリー葉、チャ葉、チガヤ根、オウゴン根）、セラミド",
        "gift_fit": "👑 30代〜50代男性へのクリスマスギフトに大定番",
        "headline": "枯れない男の肌へ。1本で化粧水・美容液・乳液・アフターシェーブをこなす大人のボタニカル名品",
        "text1": "「少し良い大人のメンズギフト」として楽天や百貨店で常に人気を集めている『クワトロボタニコ』のオールインワン化粧水。4種類の植物エキスを厳選配合し、乾燥・ハリ不足・皮脂テカリ・毛穴目立ちといった男性特有の冬トラブルにトータルで向き合います。",
        "text2": "とろみのある白濁ローションは、水っぽいだけの化粧水と違って乳液成分も含まれているため、これ1本で冬場の乾きをかなりしっかり抑えられます。ノンアルコールで髭剃り後もしみにくく、ベルガモットとローズマリーの天然精油の香りも非常に上品。「何をプレゼントしたら良いか分からない」という時の贈り物にも鉄板です。",
        "who": "30代〜50代で清潔感のある肌を目指したい男性、上品な香り付きのギフトを探している方",
        "tip": "冬場の乾燥が強い時は、1回顔全体になじませたあとに半量ほど追加してハンドプレスすると、翌朝までしっとり感が長持ちします。"
    },
    {
        "rank": 8,
        "category_tag": "エイジングケア高保湿メンズ化粧水",
        "display_name": "アスタリフト メン モイストローション 120mL",
        "alcohol": "アルコール配合（爽やかな使用感）",
        "scent": "爽やかなシトラスグリーンの香り",
        "capacity": "120mL",
        "key_spec": "ナノアスタキサンチン、3種のコラーゲン、ヒオウギエキス、グリチルリチン酸2K",
        "gift_fit": "👑 30代〜50代男性への本命クリスマスギフト",
        "headline": "レビュー約500件・★4.73の高評価！富士フイルムのナノ技術で冬のハリ不足と乾燥を跳ね返す",
        "text1": "富士フイルムの写真フィルム技術をスキンケアに応用した『アスタリフト メン』。なかでも赤いジェル状液体が特徴の『モイストローション』は、楽天公式ショップでも490件以上のレビューと★4.73（調査時点）という圧倒的な支持を集めるヒット商品です。",
        "text2": "極小化した「ナノアスタキサンチン」と「3種のコラーゲン」が、冬の冷えと乾燥でしぼんで疲れて見えがちな大人の男性肌にハリとツヤを与えます。見た目は濃いオレンジ〜赤色ですが肌に色が付くことはなく、すっと浸透して表面はベタつかないのに内側がピンと潤う実力派。スーツ姿が似合う大人の男性への冬ギフトとしても高い人気を誇ります。",
        "who": "30代後半〜50代で顔の疲れ印象・乾燥小ジワが気になり始めた男性、実績とレビュー評価の高いものを選びたい方",
        "tip": "肌荒れ予防のグリチルリチン酸2K入りなので、普段の髭剃り後ケアとしても活躍します。さらに保湿を強めたい場合は同シリーズの乳液やジェリーとの併用も人気です。"
    },
    {
        "rank": 9,
        "category_tag": "薬用エイジングケア・オールインワンクリーム",
        "display_name": "バイタルクリームパーフェクション 90g (医薬部外品)",
        "alcohol": "アルコールフリー（無香料）",
        "scent": "無香料",
        "capacity": "90g",
        "key_spec": "m-トラネキサム酸、コエンザイムQ10、Wヒアルロン酸、ローヤルゼリーエキス",
        "gift_fit": "○ ドラッグストアでも買える実力派クリーム",
        "headline": "ジェルでは物足りない超乾燥肌の男性へ。1,200円台で買えるクリームタイプの薬用オールインワン",
        "text1": "「夏はジェルで十分だったけど、11月・12月になると口周りや頬がカサカサに突っ張る」という男性にぴったりなのが、ウーノの『バイタルクリームパーフェクション』。さらっとしたジェルではなく、肌をしっかり覆って水分蒸発を防ぐ「クリームタイプ」のオールインワン（1品5役）です。",
        "text2": "医薬部外品として有効成分m-トラネキサム酸を配合し、乾燥による小ジワを目立たなくする効能評価試験済み。こっくりしたクリームに見えますが、肌に伸ばすとベタつきが残りにくいよう設計されており、しかも¥1,280（調査時点）という手頃さ。真冬の夜、寝る前の乾燥対策として非常に頼もしい存在です。",
        "who": "冬はジェルタイプだとどうしても乾いてしまう乾燥肌の男性、コスパ良くシワ・シミ予防ケアを始めたい方",
        "tip": "最初はアーモンド粒1個分ほどを取り、乾燥しやすい頬と口元を中心に伸ばしてから余った分をTゾーンに薄く広げるとテカリを防げます。"
    },
    {
        "rank": 10,
        "category_tag": "アルコールフリー乳液（高保湿バーム）",
        "display_name": "アクティブエイジバーム 110mL (医薬部外品)",
        "alcohol": "ノンアルコール（ヒリつきにくい）",
        "scent": "無香料",
        "capacity": "110mL",
        "key_spec": "ビタミンC誘導体（L-アスコルビン酸 2-グルコシド）、コエンザイムQ10、ヒアルロン酸",
        "gift_fit": "○ 手頃で毎日続けやすい乾燥・髭剃り後ケア",
        "headline": "髭剃り後のヒリつきゼロを目指すノンアルコール乳液。冬の頬の乾燥と年齢サインを1本で穏やかに保湿",
        "text1": "ニベアメンのなかでも、冬の乾燥や年齢によるカサつきに配慮された大人の薬用乳液『アクティブエイジバーム』。アルコール無配合・無香料の優しい処方で、冬場にカミソリを当てた直後のデリケートな肌にもヒリつかず、なめらかに伸びて角層を保護してくれます。",
        "text2": "乳液ながら重すぎない「バーム（なめらかな乳液）」仕様のため、化粧水後のフタとしてはもちろん、時間がない朝はこれ1本をアフターシェーブ兼保湿乳液として使う男性も多く見られます。¥1,337（調査時点）と価格も良心的で、冬の常備アイテムとして取り入れやすい1本です。",
        "who": "髭剃り後に化粧水がしみて辛い敏感肌の方、手頃な価格で無香料・ノンアルコールの保湿乳液を探している方",
        "tip": "洗顔や髭剃り後に軽く化粧水で水分を入れてから、または乾燥が軽めの日なら洗顔直後に10円玉大を伸ばすだけでしっとり整います。"
    }
]

article_title = "髭剃り負けと冬の粉吹きを一掃！メンズ高保湿スキンケア人気ランキング10選【11月・12月の乾燥対策＆ギフトにも】"
article_desc = "11月・12月の寒風と毎日の髭剃りで荒れやすい男性肌を救う高保湿メンズスキンケア10選！オルビスミスター、資生堂メン、バルクオム、NULL、クワトロボタニコ、アスタリフトメンまで、ベタつかないのにしっかり潤う名品を自分用・クリスマスギフト目線で徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-mens-skincare"

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
            "name": "11月・12月向けメンズ高保湿スキンケアランキング10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["headline"],
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
                    "name": "冬になると顔がテカるのに口周りが粉を吹きます。なぜですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "男性の肌は皮脂量が多い一方で、角層の水分量が少ないため、冬場に空気が乾燥すると『水分不足を補おうとして皮脂が過剰に出るインナードライ』に陥りやすくなります。あぶらとり紙や洗顔で皮脂を取るだけでなく、化粧水やオールインワンでしっかり水分と保湿成分を補うことで、粉吹きとテカリの両方が落ち着きやすくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "髭剃り後に化粧水がしみて痛い時はどうすればいいですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "清涼感を出すためにエタノール（アルコール）が多く含まれるメンズ化粧水は、シェービング直後の細かい傷がある角層に刺激になりやすいです。冬場は『アルコールフリー（ノンアルコール）』や抗炎症有効成分（グリチルリチン酸ジカリウム等）入りのオルビスミスター、NULL、ファンケルメン、ニベアメン アクティブエイジバームなどを選ぶとしみにくくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "12月のクリスマスプレゼントとして男性に贈るならどれが喜ばれますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ギフト映えやブランド力、香りの良さを重視するなら『SHISEIDO MEN ハイドレーティング ローション C』『アスタリフト メン モイストローション』『クワトロボタニコ ボタニカル ローション＆アフターシェーブ』の3つが特に人気です。普段スキンケアに慣れていない相手なら、1本でケアが終わるクワトロボタニコやマニフィークのようなオールインワン系だと使い続けてもらいやすいです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "男性でも化粧水のあとに乳液やクリームを塗るべきですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "11月・12月の乾燥する季節は、水分だけの化粧水だけでは数時間で蒸発してしまうため、乳液やクリームでフタをすることが推奨されます。ただし『2本も塗るのは面倒・ベタつきが苦手』という場合は、最初から乳液成分や油性エモリエントが配合されたオールインワン（オルビスミスター、NULL、クワトロボタニコ、ウーノなど）を選べば1ステップで済みます。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬のホリデーギフト・コフレ特集", "item": "https://lumi-cosme.vercel.app/winter-holiday-coffret"},
                {"@type": "ListItem", "position": 3, "name": "メンズ高保湿スキンケア10選", "item": canonical_url}
            ]
        }
    ]
}

rows_html = ""
for it, det in zip(items, details):
    rows_html += f"""            <tr>
              <td><span class="m-rank">{it['rank']}位</span></td>
              <td><strong>{html.escape(it['brand'])}</strong><br><span class="m-sub">{html.escape(det['display_name'])}</span></td>
              <td>{html.escape(det['category_tag'].split('（')[0])}</td>
              <td>{html.escape(det['alcohol'])}</td>
              <td>{html.escape(det['gift_fit'])}</td>
              <td class="m-price">¥{it['price']:,}<br><span class="m-sub">{html.escape(det['capacity'])}</span></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rev_txt = (
        f'<span class="m-rev">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="m-rev">楽天 取扱人気品</span>'
    )
    cards_html += f"""
      <article class="m-card" id="rank-{it['rank']}">
        <div class="m-card-header">
          <div class="m-tag-line">
            <span class="m-rank-badge r-{it['rank']}">第{it['rank']}位</span>
            <span class="m-cat-chip">{html.escape(det['category_tag'])}</span>
            {rev_txt}
          </div>
          <h3>{html.escape(it['brand'])} — {html.escape(det['display_name'])}</h3>
        </div>

        <div class="m-card-grid">
          <div class="m-media">
            <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            <div class="m-price-box">
              <span class="m-price-lbl">楽天市場 最新価格（税込）</span>
              <span class="m-price-val">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天で在庫・ギフト対応を見る →
            </a>
            <p class="m-ref">掲載商品：{html.escape(it['item_name'][:48])}</p>
          </div>

          <div class="m-detail">
            <div class="m-headline">{html.escape(det['headline'])}</div>
            <table class="m-spec-tbl">
              <tr><th>内容量</th><td>{html.escape(det['capacity'])}</td></tr>
              <tr><th>刺激配慮</th><td>{html.escape(det['alcohol'])}</td></tr>
              <tr><th>香り</th><td>{html.escape(det['scent'])}</td></tr>
              <tr><th>主な配合成分</th><td>{html.escape(det['key_spec'])}</td></tr>
              <tr><th>ギフト適性</th><td>{html.escape(det['gift_fit'])}</td></tr>
            </table>
            <p class="m-p">{html.escape(det['text1'])}</p>
            <p class="m-p">{html.escape(det['text2'])}</p>
            <div class="m-callout-wrap">
              <div class="m-callout">
                <strong>こんな男性におすすめ</strong>
                <p>{html.escape(det['who'])}</p>
              </div>
              <div class="m-callout alt">
                <strong>冬の使いこなしポイント</strong>
                <p>{html.escape(det['tip'])}</p>
              </div>
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
  <meta name="keywords" content="メンズ スキンケア 冬, メンズ 高保湿 化粧水, 髭剃り負け 乾燥, クリスマスプレゼント メンズ コスメ, オルビスミスター, 資生堂メン, バルクオム, NULL, アスタリフトメン, クワトロボタニコ">
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
      --navy: #1e3a8a;
      --blue: #2563eb;
      --ice: #eff6ff;
      --ice-border: #bfdbfe;
      --ink: #0f172a;
      --muted: #475569;
      --line: #e2e8f0;
      --bg: #f8fafc;
      --card: #ffffff;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.75;
    }}
    header.nav-bar {{
      background: #0f172a;
      color: #fff;
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .nav-bar-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .brand {{ color: #fff; font-weight: 800; font-size: 1.15rem; text-decoration: none; }}
    .nav-menu {{ display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.85rem; }}
    .nav-menu a {{ color: #93c5fd; text-decoration: none; font-weight: 700; }}
    .nav-menu a:hover {{ color: #fff; }}
    .crumb {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .crumb a {{ color: var(--blue); text-decoration: none; }}

    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .hero {{
      background: linear-gradient(135deg, #1e293b 0%, #1e3a8a 100%);
      color: #f8fafc;
      border-radius: 14px;
      padding: 38px 32px;
      margin-bottom: 30px;
    }}
    .hero-tag {{
      display: inline-block;
      background: #3b82f6;
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .hero h1 {{ font-size: 1.72rem; line-height: 1.4; margin-bottom: 12px; color: #ffffff; }}
    @media (max-width: 720px) {{
      .hero {{ padding: 26px 18px; }}
      .hero h1 {{ font-size: 1.35rem; }}
    }}
    .hero-meta {{ font-size: 0.83rem; color: #cbd5e1; margin-bottom: 16px; }}
    .hero p {{ font-size: 0.96rem; color: #e2e8f0; margin-bottom: 10px; }}
    .hero p:last-child {{ margin-bottom: 0; }}

    .toc-box {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 30px;
    }}
    .toc-box h2 {{ font-size: 1.05rem; margin-bottom: 12px; }}
    .toc-box ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px 18px;
    }}
    .toc-box a {{ color: var(--navy); text-decoration: none; font-weight: 600; font-size: 0.9rem; }}
    .toc-box a:hover {{ text-decoration: underline; }}

    .panel {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 30px;
    }}
    .panel h2 {{
      font-size: 1.35rem;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--ice-border);
    }}
    .panel p {{ font-size: 0.95rem; color: #334155; margin-bottom: 12px; }}
    .split-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}
    .split-item {{
      background: var(--ice);
      border: 1px solid var(--ice-border);
      border-radius: 10px;
      padding: 18px;
    }}
    .split-item h3 {{ font-size: 1rem; color: var(--navy); margin-bottom: 8px; }}
    .split-item p {{ font-size: 0.87rem; margin-bottom: 0; }}

    .table-box {{ overflow-x: auto; margin-top: 14px; }}
    .m-compare {{ width: 100%; border-collapse: collapse; font-size: 0.86rem; min-width: 650px; }}
    .m-compare th, .m-compare td {{ border: 1px solid var(--line); padding: 10px 12px; text-align: left; vertical-align: top; }}
    .m-compare th {{ background: #dbeafe; color: #1e3a8a; font-weight: 700; white-space: nowrap; }}
    .m-compare tr:nth-child(even) {{ background: #f8fafc; }}
    .m-rank {{ font-weight: 800; color: var(--navy); white-space: nowrap; }}
    .m-price {{ font-weight: 800; color: #be123c; white-space: nowrap; }}
    .m-sub {{ font-size: 0.77rem; color: var(--muted); font-weight: 400; }}

    .sec-title {{ font-size: 1.45rem; font-weight: 800; margin: 34px 0 18px; }}
    .m-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 26px;
      margin-bottom: 26px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }}
    .m-card-header {{
      border-bottom: 1px solid var(--line);
      padding-bottom: 14px;
      margin-bottom: 18px;
    }}
    .m-tag-line {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }}
    .m-rank-badge {{
      background: var(--navy);
      color: #fff;
      font-weight: 800;
      font-size: 0.86rem;
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .m-rank-badge.r-1 {{ background: #b45309; }}
    .m-rank-badge.r-2 {{ background: #475569; }}
    .m-rank-badge.r-3 {{ background: #1d4ed8; }}
    .m-cat-chip {{
      background: var(--ice);
      border: 1px solid var(--ice-border);
      color: var(--navy);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .m-rev {{ font-size: 0.8rem; font-weight: 700; color: #b45309; margin-left: auto; }}
    .m-card-header h3 {{ font-size: 1.2rem; color: var(--ink); line-height: 1.4; }}

    .m-card-grid {{
      display: grid;
      grid-template-columns: 270px 1fr;
      gap: 24px;
    }}
    @media (max-width: 820px) {{
      .m-card-grid {{ grid-template-columns: 1fr; }}
    }}
    .m-media {{ display: flex; flex-direction: column; gap: 10px; }}
    .product-img {{
      width: 100%;
      max-height: 240px;
      object-fit: contain;
      border: 1px solid var(--line);
      border-radius: 10px;
      background: #fff;
      padding: 10px;
    }}
    .m-price-box {{
      background: #f1f5f9;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
    }}
    .m-price-lbl {{ display: block; font-size: 0.75rem; color: var(--muted); }}
    .m-price-val {{ font-size: 1.4rem; font-weight: 800; color: #be123c; }}
    .rakuten-btn {{
      display: block;
      text-align: center;
      background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%);
      color: #fff;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 13px 16px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ opacity: 0.92; }}
    .m-ref {{ font-size: 0.74rem; color: var(--muted); line-height: 1.4; margin: 0; }}

    .m-headline {{
      background: var(--ice);
      border-left: 4px solid var(--blue);
      padding: 10px 14px;
      font-weight: 700;
      color: var(--navy);
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
      font-size: 0.94rem;
    }}
    .m-spec-tbl {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      margin-bottom: 14px;
    }}
    .m-spec-tbl th, .m-spec-tbl td {{
      border-bottom: 1px solid var(--line);
      padding: 7px 6px;
      text-align: left;
      vertical-align: top;
    }}
    .m-spec-tbl th {{ width: 115px; color: var(--muted); font-weight: 700; white-space: nowrap; }}
    .m-p {{ font-size: 0.93rem; color: #334155; margin-bottom: 12px; }}
    .m-callout-wrap {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 12px;
    }}
    @media (max-width: 640px) {{
      .m-callout-wrap {{ grid-template-columns: 1fr; }}
    }}
    .m-callout {{
      background: #f8fafc;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      font-size: 0.85rem;
    }}
    .m-callout.alt {{ background: var(--ice); border-color: var(--ice-border); }}
    .m-callout strong {{ display: block; margin-bottom: 4px; color: var(--ink); }}
    .m-callout p {{ margin: 0; color: #334155; line-height: 1.6; }}

    .faq-unit {{ border-bottom: 1px solid var(--line); padding: 15px 0; }}
    .faq-unit:last-child {{ border-bottom: none; }}
    .faq-unit h3 {{ font-size: 1rem; margin-bottom: 6px; }}
    .faq-unit p {{ font-size: 0.9rem; margin-bottom: 0; color: #334155; }}

    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--line);
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
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--blue); }}

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
    .footer-links-grid a:hover {{ color: #93c5fd; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1e293b; padding-top: 20px; text-align: center; font-size: 0.78rem; }}
  </style>
</head>
<body>
  <header class="nav-bar">
    <div class="nav-bar-inner">
      <a href="/" class="brand">Lumi Cosme</a>
      <nav class="nav-menu">
        <a href="/winter-holiday-coffret">ホリデーギフト特集</a>
        <a href="/winter-lotion">化粧水特集</a>
        <a href="/winter-face-wash">洗顔料特集</a>
      </nav>
    </div>
  </header>

  <nav class="crumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-holiday-coffret">冬のホリデーギフト特集</a> &gt; <span>メンズ高保湿スキンケア10選</span>
  </nav>

  <main>
    <section class="hero">
      <span class="hero-tag">2026年11月・12月 メンズ乾燥対策＆ギフト特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="hero-meta">更新日：<time datetime="2026-11-21">2026年11月21日</time> ／ Lumi Cosme 編集部</div>
      <p>
        11月から12月にかけて空気が一気に乾き始めると、男性の肌には<strong>「朝の髭剃り後に頬やアゴがヒリヒリ赤くなる」「夕方になるとおでこはベタつくのに口周りは白く粉を吹く」</strong>という厄介なトラブルが立て続けに起こります。これは、男性特有の皮脂量の多さと角層の水分不足に、毎日のシェービング摩擦が重なって起きる現象です。
      </p>
      <p>
        さらに12月はクリスマスプレゼントや年末年始の挨拶ギフトとしてメンズスキンケアを選ぶ機会も増える時期。本記事では「ヌルつき・テカリは苦手だけど冬でもしっかり潤う」メンズ向けの高保湿化粧水・乳液・オールインワン10製品を、実用目線とギフト適性の両方から比較しました。
      </p>
    </section>

    <nav class="toc-box" aria-label="目次">
      <h2>この記事のナビゲーション</h2>
      <ul>
        <li><a href="#mens-dry">1. 冬に男性の肌が一気に荒れる「髭剃り×インナードライ」の仕組み</a></li>
        <li><a href="#gift-or-self">2. 自分用と12月ギフト用で変わる失敗しない選び方</a></li>
        <li><a href="#mens-table">3. メンズ高保湿スキンケア10選 比較スペック表</a></li>
        <li><a href="#ranking">4. 人気ランキング10選（使用感・刺激配慮・価格詳細）</a></li>
        <li><a href="#shave-routine">5. カミソリ負けを和らげる冬の洗顔＆保湿3ステップ</a></li>
        <li><a href="#faq">6. メンズ冬のスキンケア FAQ</a></li>
      </ul>
    </nav>

    <section class="panel" id="mens-dry">
      <h2>1. 男性肌が11月・12月に荒れやすい本当の理由</h2>
      <p>
        男性の肌は女性と比べて皮脂分泌量がおよそ2倍前後あるため、夏場は何も塗らなくても平気に感じることが少なくありません。ところが、角層内部に蓄えられる水分量は女性の半分程度と言われており、湿度が低下する11月〜12月には一気に乾燥が表面化します。
      </p>
      <p>
        加えて、毎朝のシェービングでは髭と一緒に肌表面の薄い角質層もわずかに削られます。そこにエタノール（アルコール）の強いトニック系化粧水を塗ると、水分が一層飛ぶだけでなくヒリつき・赤みにつながりやすくなります。冬場に頼りたいのは、<strong>「水分と適度な保護膜を同時に与えつつ、ベタつきが残りにくい設計」</strong>のアイテムです。
      </p>
    </section>

    <section class="panel" id="gift-or-self">
      <h2>2. 失敗しない！自分用＆クリスマスギフト用の選び方3ポイント</h2>
      <div class="split-grid">
        <div class="split-item">
          <h3>① カミソリ負けしやすいならノンアルコール</h3>
          <p>スースーする清涼感が強い製品は冬場はしみやすいため、オルビスミスターやNULL、ファンケルメン、クワトロボタニコ、ニベアメンなどのアルコールフリー設計を選ぶと穏やかに使えます。</p>
        </div>
        <div class="split-item">
          <h3>② 習慣化しやすさ優先なら「1本完結」</h3>
          <p>「化粧水の後に乳液を塗るのは続かない」という男性には、化粧水＋乳液の機能を備えたオールインワン型（オルビスミスター、マニフィーク、NULL、クワトロボタニコ等）が現実的です。</p>
        </div>
        <div class="split-item">
          <h3>③ 12月のプレゼントならボトル＆香り重視</h3>
          <p>クリスマスギフトとして贈るなら、SHISEIDO MEN、アスタリフト メン、クワトロボタニコ、マニフィークなど、洗面台に置いて格好がつくデザインと上品な香りのブランドが喜ばれます。</p>
        </div>
      </div>
    </section>

    <section class="panel" id="mens-table">
      <h2>3. メンズ高保湿スキンケア10選 比較一覧表</h2>
      <p>楽天市場で確認した実勢価格（税込）と、アルコール配合の有無・ギフト適性をまとめました。</p>
      <div class="table-box">
        <table class="m-compare">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>アイテム種別</th>
              <th>アルコール配慮</th>
              <th>ギフト適性</th>
              <th>価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{rows_html}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="sec-title" id="ranking">4. メンズ高保湿スキンケア厳選ランキング10選</h2>
    <section aria-label="商品詳細">
{cards_html}    </section>

    <section class="panel" id="shave-routine">
      <h2>5. カミソリ負けと粉吹きを減らす冬の朝3ステップ</h2>
      <div class="split-grid">
        <div class="split-item">
          <h3>Step 1：熱いお湯で顔を洗わない</h3>
          <p>寒い朝に40℃以上の熱いシャワーや湯で顔を流すと、肌を守る皮脂膜まで一気に落ちてしまいます。32〜34℃くらいのぬるま湯でさっと流すだけで乾燥の度合いが大きく変わります。</p>
        </div>
        <div class="split-item">
          <h3>Step 2：髭剃り前は蒸しタオルor洗顔泡</h3>
          <p>乾いた硬い髭をそのまま剃ると角層へのダメージが増えます。洗顔料の泡やシェービングフォームで髭を柔らかくしてから刃を当てると、肌への引っかかりが減ります。</p>
        </div>
        <div class="split-item">
          <h3>Step 3：タオル拭き後「すぐ」保湿</h3>
          <p>顔を拭いたら乾燥が始まる前に、手のひらに取った化粧水やオールインワンを擦らず優しく押さえつけます。口の周りなど粉を吹きやすい箇所だけ少量重ね付けするのがコツです。</p>
        </div>
      </div>
    </section>

    <section class="panel" id="faq">
      <h2>6. 冬のメンズスキンケア よくある疑問（FAQ）</h2>
      <div class="faq-unit">
        <h3>Q1. ベタベタするのが本当に嫌いなのですが、冬用は全部ベタつきますか？</h3>
        <p>最近のメンズ向け高保湿品は、女性のクリームのように油膜を厚く乗せるのではなく、角層の内部に水分を抱え込んで表面はサラッと整える設計（オルビスミスター、NULL、アスタリフトメン等）が増えています。1〜2分経てば手触りも気になりにくくなります。</p>
      </div>
      <div class="faq-unit">
        <h3>Q2. 女性用（共有）の化粧水やクリームを借りてもいいですか？</h3>
        <p>もちろん肌に合えば問題ありませんが、女性用の極度にリッチなクリームは男性の皮脂量と合わずにTゾーンがテカりすぎたり、ニキビの原因になったりすることがあります。ベタつきが気になる場合はメンズ設計品の方がバランスを取りやすいです。</p>
      </div>
      <div class="faq-unit">
        <h3>Q3. 12月のクリスマスギフトに選ぶときの予算相場は？</h3>
        <p>友人や職場の相手なら2,500〜3,500円前後（オルビスミスター、マニフィーク、クワトロボタニコ、バルクオム）、パートナーや特別な贈り物なら4,000〜5,000円前後のデパコス・高機能ライン（SHISEIDO MEN、アスタリフト メン）が選ばれやすい価格帯です。</p>
      </div>
      <div class="faq-unit">
        <h3>Q4. 乾燥がひどくて夜中に顔がかゆくなることがあります。</h3>
        <p>洗顔料の洗浄力が強すぎる可能性と、化粧水だけで油分のフタが足りていない可能性の両方が考えられます。ぬるま湯洗顔に切り替え、夜だけはクリームタイプの『ウーノ バイタルクリームパーフェクション』や乳液バーム『ニベアメン アクティブエイジバーム』などで水分を逃さないケアに切り替えると落ち着きやすくなります。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-holiday-coffret" class="internal-link-card">
          <strong>冬のクリスマスコフレ・ギフト特集</strong>
          <span>ホリデーシーズンに喜ばれる人気ギフト</span>
        </a>
        <a href="/winter-all-in-one" class="internal-link-card">
          <strong>高保湿オールインワン特集</strong>
          <span>時短で潤う高保湿ゲル＆クリーム10選</span>
        </a>
        <a href="/winter-lotion" class="internal-link-card">
          <strong>冬の高保湿化粧水特集</strong>
          <span>乾燥知らずの実力派化粧水10選</span>
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

with open("winter-mens-skincare.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-mens-skincare.html successfully!")
