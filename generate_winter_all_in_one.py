import json
import html

with open("fetched_3new_nov_dec_2026_1121.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_all_in_one"]["items"]

details = [
    {
        "rank": 1,
        "badge_text": "ヘパリン類似物質HD配合・医薬部外品",
        "display_name": "モイスチュア インストール 100g (高保湿オールインワンゲル・医薬部外品)",
        "form": "濃密エマルジョンゲル",
        "capacity": "100g",
        "key_ingredients": "ヘパリン類似物質HD、グリチルリチン酸ジカリウム、スクワラン、セラミド類似ポリマー",
        "moro_moro": "極めて出にくい（朝のメイク前◎）",
        "catch": "保湿の切り札「ヘパリン類似物質HD」×肌荒れ防止成分で、冬の乾きループを根本から立て直す",
        "review_body_1": "コーセーとマルホが共同開発した医薬部外品ライン「カルテHD」のオールインワンゲル。最大の強みは、保水有効成分「ヘパリン類似物質HD」と消炎有効成分「グリチルリチン酸ジカリウム」をWで配合している点です。11月後半からエアコンの風で頬が赤くヒリつき始めたときでも、しみにくくまろやかに広がります。",
        "review_body_2": "見た目はみずみずしい半透明の乳液ゲルですが、肌に伸ばすとオイルを内包したエモリエントヴェールが溶け出し、クリームを塗った後のようなしっとりした保護膜に変わります。それでいて表面にヌルつきが残らないため、塗ってから2分ほど置けばそのまま下地やファンデーションを重ねてもモロモロが出にくいのが嬉しいポイントです。",
        "good_for": "暖房で夕方になると肌がつっぱる・赤みが出やすい方、化粧水とクリームを分ける余裕がない平日の朝",
        "usage_note": "付属のスパチュラでパール粒2個分を手に取り、乾燥しやすい頬と口元から先に馴染ませてから額・鼻へ伸ばすとバランスよく仕上がります。"
    },
    {
        "rank": 2,
        "badge_text": "資生堂・浸透美容アミノ酸配合",
        "display_name": "スペシャルジェルクリーム EX (モイストスムース) 90g",
        "form": "ぷるんと弾力ジェルクリーム",
        "capacity": "90g",
        "key_ingredients": "D-グルタミン酸・DL-アラニン（浸透美容アミノ酸）、トリプルヒアルロン酸、コラーゲンGL",
        "moro_moro": "出にくい（伸びが軽く密着◎）",
        "catch": "2,000円以下で手に入る資生堂の定番名品。角層の潤い保持機能に着目したアミノ酸が冬のゴワつきをほぐす",
        "review_body_1": "ドラッグストアでも不動の人気を誇る資生堂アクアレーベルの「モイストスムース」は、高い保湿力と毛穴の目立ちにくいなめらかな後肌を両立したジェルクリームです。資生堂が長年研究してきた「ベビーアミノ酸（D-アミノ酸）」と3種のヒアルロン酸を組み合わせ、冬の冷気で硬くなった角層を柔らかくほぐしながら水分を抱え込みます。",
        "review_body_2": "蓋を開けるとぷるっとした濃密なジェルで、指に取るとすっと水のように崩れて広がります。ハーバルローズのほのかな香りが強すぎず、夜の入浴後に使うと心地よい気分転換に。価格が¥1,958（調査時点）と手頃なため、首元やデコルテまで惜しみなく塗り広げたい方にもぴったりです。",
        "good_for": "コスパよく本格的な保湿ケアを続けたい方、重たいクリームのベタつきが苦手だけど乾燥は防ぎたい混合肌の方",
        "usage_note": "乾燥が特に気になる夜や週末は、規定量の約1.5倍を顔全体に厚めに塗り、5分ほど置いてから軽くハンドプレスで押し込む「3分ジェルマスク」使いも快適です。"
    },
    {
        "rank": 3,
        "badge_text": "ナイアシンアミド×浸透型コラーゲン",
        "display_name": "アクアコラーゲンゲル エンリッチリフトEX R 120g",
        "form": "高密度ハリ・リッチゲル",
        "capacity": "120g",
        "key_ingredients": "浸透型コラーゲンEX、浸透型ヒアルロン酸EX、ナイアシンアミド、5種のセラミド",
        "moro_moro": "やや注意（薄くハンドプレスで馴染ませれば○）",
        "catch": "ハリ不足と乾燥小ジワが加速する12月に頼りたい、日本初のコラーゲン研究発想エイジングケアゲル",
        "review_body_1": "ドクターシーラボの看板モデルである金のエンリッチリフトEXは、単なる水分補給ではなく「冬の冷えと乾燥でしぼんだ肌のハリ感」に焦点を当てた一品です。日本初のトータルコラーゲンサイエンスから生まれた浸透型コラーゲンEXと浸透型ヒアルロン酸EX、さらに話題のナイアシンアミドを高濃度でブレンドしています。",
        "review_body_2": "少しこっくりとした琥珀色のリッチな質感で、頬に引き上げるように馴染ませると、肌表面がピンッと吸い付くような密着感があります。120gの大容量ジャーなら朝晩たっぷり使っても約2〜2.5ヶ月持つため、1ヶ月あたりのコストで見ればデパコスクリームよりずっと現実的です。",
        "good_for": "冬の乾燥でほうれい線や目元の小ジワが目立ちやすくなった方、1つで保湿とハリ・弾力ケアを済ませたい大人世代",
        "usage_note": "顔の下から上へ、フェイスラインを手のひらで包み込むように持ち上げながら馴染ませます。朝メイク前に使う場合は量を少し控えめにし、しっかり浸透させてから下地へ移ってください。"
    },
    {
        "rank": 4,
        "badge_text": "ゆらぎ肌対応・薬用バリアフィックス",
        "display_name": "プレミアバリアフィックス 58g (医薬部外品)",
        "form": "濃密メルティジェルクリーム",
        "capacity": "58g",
        "key_ingredients": "グリチルリチン酸ジカリウム、ナイアシンアミド、カーミングコンプレックス、セラミド類似成分",
        "moro_moro": "出にくい（なめらかなクリーム質感）",
        "catch": "寒暖差とマスク摩擦による冬の赤み・肌荒れとシワ改善を同時に狙えるグリーン缶の薬用オールインワン",
        "review_body_1": "カナデルの中でも敏感・ゆらぎ肌向けに設計された「プレミアバリアフィックス」。有効成分として肌荒れを防ぐグリチルリチン酸ジカリウムと、シワ改善・美白（メラニンの生成を抑えシミ・そばかすを防ぐ）を担うナイアシンアミドの両方を配合した医薬部外品です。",
        "review_body_2": "一般的な透明ジェルとは一線を画す、バームとクリームの中間のようなこっくりしたテクスチャー。体温に触れるとじゅわっととろけてピタッと密着し、暖房の風が直接当たるデスクワーク中でも水分が逃げにくい設計になっています。カーミングフローラルの優しい香りも冬のリラックスタイムに好相性です。",
        "good_for": "外気と室内の寒暖差で頬が赤くなりやすい方、敏感肌だけどエイジングケアも諦めたくない方",
        "usage_note": "最初は少量を手のひらで温めてから、こすらずスタンプを押すように頬へ乗せると摩擦刺激を減らせます。"
    },
    {
        "rank": 5,
        "badge_text": "複合型コラーゲンEX×紫根エキス",
        "display_name": "モイスチャージェル 75g",
        "form": "みずみずしい高密着ジェル",
        "capacity": "75g",
        "key_ingredients": "複合型コラーゲンEX（7種）、紫根エキス、ヒアルロン酸、セラミド",
        "moro_moro": "出にくい（朝の時短メイク前にも好適）",
        "catch": "累計販売数でも常に上位を走るロングセラー。重すぎないのに翌朝まで乾きにくい絶妙バランス",
        "review_body_1": "オールインワン市場の定番として長く支持される新日本製薬の「パーフェクトワン モイスチャージェル」。性質の異なる7種のコラーゲンを組み合わせた「複合型コラーゲンEX」に加え、和漢植物由来の紫根エキスやセラミドなど50種もの保湿成分を1瓶に詰め込んでいます。",
        "review_body_2": "質感はとてもみずみずしく、肌に乗せた瞬間にスッと浸透してベタつきが残りません。それでいて内側に水分を留める力が強く、「軽いのにカサつかない」という珍しいバランスを実現しています。無香料・無着色・パラベンフリーでクセがないため、スキンケアの匂いが苦手な方にも選ばれています。",
        "good_for": "重たい油膜感が苦手だけど冬仕様の保湿力が欲しい方、朝のメイク前にサッと使える定番品を探している方",
        "usage_note": "乾燥が厳しい真冬日は、顔全体になじませたあと、乾燥しやすい目元と口元だけに小豆1粒分を重ね付けしておくと安心です。"
    },
    {
        "rank": 6,
        "badge_text": "ナイアシンアミド×濃厚ハリゲル",
        "display_name": "極潤 ハリパーフェクトゲル 100g",
        "form": "濃いとろみ密着ゲル",
        "capacity": "100g",
        "key_ingredients": "ナイアシンアミド（有効成分）、3種のヒアルロン酸、スクワラン、シア脂",
        "moro_moro": "ややとろみ強め（夜は◎、朝は少量推奨）",
        "catch": "1,200円台で買える医薬部外品オールインワン。シア脂とスクワランの濃厚な蓋力で真冬の夜も安心",
        "review_body_1": "ドラッグストアの王道・肌ラボの「極潤 ハリパーフェクトゲル」は、プチプラ価格でありながら有効成分ナイアシンアミドを配合したシワ改善・シミ対策対応の医薬部外品オールインワンです。さらに3種類のヒアルロン酸に加え、スクワランやシア脂といった油性エモリエント成分をしっかり配合しています。",
        "review_body_2": "容器からすくうと糸を引くようなもっちり濃厚なゲルで、肌に伸ばした瞬間に「しっかりフタをされた」という頼もしい保湿感があります。100gで¥1,250（調査時点）という価格帯は家計にも優しく、詰め替え用も手に入りやすいため冬のデイリー使いとして非常に優秀です。",
        "good_for": "1,000円台で乾燥・小ジワ対策までできる高コスパ品を探している方、夜のこってり保湿が好きな乾燥肌の方",
        "usage_note": "油分と増粘剤がしっかりめなので、朝のメイク前に使う場合はパール1粒分ほどに留め、しっかりハンドプレスで落ち着かせてから日焼け止めや下地を重ねてください。"
    },
    {
        "rank": 7,
        "badge_text": "玉造温泉水×ヒト型セラミド",
        "display_name": "メディプラスゲル 180g",
        "form": "ポンプ式湿潤美容ゲル",
        "capacity": "180g（約2ヶ月分）",
        "key_ingredients": "出雲玉造温泉水、グリセリン、ヒト型セラミド（セラミドEOP/NG/NP/AP）、2種のコラーゲン",
        "moro_moro": "乾く前に塗り重ねないのがコツ（1〜2プッシュで◎）",
        "catch": "蓋を開ける手間すら省くポンプ式180g。肌をこする回数そのものを減らす「湿潤美容」発想",
        "review_body_1": "ジャー容器の蓋を開けてスパチュラですくう一手間すら省けるポンプ式オールインワンの代表格が「メディプラスゲル」。肌荒れを防ぐ出雲玉造温泉水をベースに、人の肌と同じ構造を持つヒト型セラミドやアミノ酸、ビタミンCなどをバランスよく配合しています。",
        "review_body_2": "コンセプトは「摩擦ゼロで潤いを長く留める湿潤美容」。1プッシュで顔全体を覆えるほど伸びが良く、塗布後は肌の上にみずみずしい保護膜が形成されます。真冬の朝、冷えた洗面所でパッと1〜2プッシュ押してサッと塗れる手軽さは、忙しい社会人や子育て中の方から絶大な支持を集めています。",
        "good_for": "ジャー容器の開け閉めやスパチュラの手入れが面倒な方、肌の摩擦を極力減らしたい敏感肌の方",
        "usage_note": "指先でクルクル何度も擦り込むと膜がヨレることがあるため、手のひらに広げて顔全体を包み込むように2〜3回押さえて馴染ませるのが鉄則です。"
    },
    {
        "rank": 8,
        "badge_text": "豆乳発酵液×ピュアレチノール",
        "display_name": "とろんと濃ジェル エンリッチ NC 100g",
        "form": "形状記憶もっちり濃ジェル",
        "capacity": "100g",
        "key_ingredients": "豆乳発酵液（保湿）、ピュアレチノール（整肌）、ダイズ種子エキス、ダイズタンパク",
        "moro_moro": "適量なら出にくい（夜はたっぷり塗り◎）",
        "catch": "800円台の驚異的コスパ！豆乳発酵液とピュアレチノール配合で、冬のカサつき肌をふっくら整える",
        "review_body_1": "サナ なめらか本舗のエイジングケアラインから出ている「とろんと濃ジェル エンリッチ NC」は、1,000円を切る価格（¥819・調査時点）でありながら、北海道産丸大豆由来の豆乳発酵液とピュアレチノールを組み合わせた実力派です。",
        "review_body_2": "容器を傾けてもすぐには流れない「形状記憶ジェル」のようなぷるんとした感触ですが、肌に乗せると体温でスッととろけて濃密な化粧水のように広がります。肌表面にオイルの膜がしっかり残るため、冬場の入浴後にこれ1つだけでも翌朝の頬がカサつきにくいと口コミでも高評価を得ています。",
        "good_for": "予算を抑えつつ冬の夜もしっかり潤うオールインワンが欲しい方、レチノールケアを気軽に取り入れたい方",
        "usage_note": "ピュアレチノール配合のため、朝に使用した日は必ず日焼け止めやUVカット下地で紫外線対策を行ってください。"
    },
    {
        "rank": 9,
        "badge_text": "9種のコラーゲン×3種のヒアルロン酸",
        "display_name": "コラリッチ EX ブライトニングリフトジェル 55g",
        "form": "美容オイル粒入り濃厚ジェル",
        "capacity": "55g",
        "key_ingredients": "9種のコラーゲン、3種のヒアルロン酸、3種の美容オイル（シアバター等）、ナイアシンアミド",
        "moro_moro": "出にくい（オイルカプセルが溶けて密着）",
        "catch": "目に見えるオレンジ色の美容オイル粒が弾ける！年齢を重ねた冬の乾燥肌にツヤとハリを与える",
        "review_body_1": "キューサイの「コラリッチ EX ブライトニングリフトジェル」は、役割の異なる9種類のコラーゲンと3種類のヒアルロン酸、さらに肌にツヤをもたらす美容オイルをカプセル化して閉じ込めた贅沢なオールインワンです。これ1つで化粧水・乳液・美容液・クリーム・美容オイル・マッサージジェル・パック・アイクリーム・ネッククリームの9役を担います。",
        "review_body_2": "ジェルの中に浮かぶオレンジ色の粒は、シアバターやアルガンオイルなどを閉じ込めた美容オイルカプセル。肌に伸ばす瞬間に指先で自然につぶれて溶け込み、乾燥でくすんで見えがちな冬の素肌に自然なツヤ感を与えてくれます。首元まで伸ばしやすい滑らかなテクスチャーも魅力です。",
        "good_for": "40代〜60代以上で冬場のハリのなさ・くすみ・首の乾燥までまとめてケアしたい方、美容オイルを別で塗るのが面倒な方",
        "usage_note": "首やデコルテの乾燥シワも気になる方は、あご下から鎖骨に向かって下から上へ軽く流すように塗るとリンパケアも兼ねられます。"
    },
    {
        "rank": 10,
        "badge_text": "トラネキサム酸配合・医薬部外品",
        "display_name": "美白 うるおい ジェル N 108g (医薬部外品)",
        "form": "みずみずしい透明薬用ジェル",
        "capacity": "108g",
        "key_ingredients": "トラネキサム酸（美白有効成分）、ヒアルロン酸、トレハロース、油溶性甘草エキス",
        "moro_moro": "極めて出にくい（無香料・ノンアルコールで穏やか）",
        "catch": "トラネキサム酸とトレハロースの保水力。アルコール無添加で冬のデリケート肌にも優しい処方",
        "review_body_1": "無香料・無着色・アルコールフリーというシンプルな設計で信頼されるちふれの薬用オールインワン「美白 うるおい ジェル N」。美白有効成分のトラネキサム酸が冬の紫外線や乾燥摩擦によるシミ・ソバカスを防ぎつつ、ヒアルロン酸と保水糖トレハロースが角層の水分を逃さず抱え込みます。",
        "review_body_2": "さっぱり寄りの軽い感触に見えますが、実際に塗ってみるともっちりとした保水膜が残り、アルコールフリーなので髭剃り後や冬の乾いた頬にもピリピリしにくいのが特徴です。詰替え用も展開されているため、まずは本体で相性を試してからリピートしやすい点も支持されています。",
        "good_for": "アルコールや香料に弱い敏感肌の方、乾燥対策とあわせてトラネキサム酸の美白ケアも取り入れたい方",
        "usage_note": "極度の乾燥肌の方が真冬の夜に使う場合は、これ1つを塗った後に薄くワセリンや手持ちのクリームを乾燥ポイントに重ねると朝まで磐石です。"
    }
]

article_title = "真冬の朝5秒で角層までうるおう！乾燥知らずの高保湿オールインワンジェル＆クリーム厳選ランキング10【11月・12月】"
article_desc = "11月・12月の忙しい朝や極寒の夜でもこれ1つで乾燥知らず！カルテHD、アクアレーベル、ドクターシーラボ、カナデル、メディプラスゲルなど、モロモロが出にくく朝まで潤う高保湿オールインワンジェル＆クリーム10選を成分・使用感・コスパで徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-all-in-one"

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
            "name": "11月・12月向け高保湿オールインワンジェル＆クリームランキング10選",
            "numberOfItems": 10,
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": it["rank"],
                    "item": {
                        "@type": "Product",
                        "name": f"{it['brand']} {det['display_name']}",
                        "image": it["image_url"],
                        "description": det["catch"],
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
                    "name": "真冬の11月・12月でもオールインワンだけで本当に乾燥しませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "セラミドやスクワラン、シア脂、ヘパリン類似物質などの油性エモリエント成分がバランスよく乳化された『クリームゲルタイプ』や『医薬部外品タイプ』を選べば、真冬の暖房下でも十分な保湿力を発揮します。水分だけのさっぱりした透明ジェルではなく、適度な油膜感がある製品を選ぶのがポイントです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "朝のメイク前にオールインワンを塗るとモロモロ（消しゴムのカス）が出ることがあるのはなぜ？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "オールインワンジェルに多く含まれる高分子ポリマー（カルボマーなど）が肌表面で乾く前に、日焼け止めや下地を重ねて擦ることでポリマー同士が絡まってモロモロになります。対策としては、塗布量をパール1〜2粒分に抑え、塗布後2〜3分待ってしっかり馴染ませてからメイクに入ること、また乳液ベースのゲルを選ぶことが有効です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "化粧水の後にオールインワンを塗っても問題ありませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "全く問題ありません。むしろ、すでに手持ちの化粧水がある場合は『導入化粧水または通常の化粧水＋オールインワンをクリーム代わり』として使うことで、水分と油分の密閉力が格段に高まり、極度の乾燥肌でも真冬を乗り切りやすくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "スパチュラ（ヘラ）を使うタイプとポンプタイプ、どちらがおすすめ？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "朝の1分1秒を惜しむ方や衛生的・手軽に済ませたい方にはポンプタイプ（メディプラスゲルなど）が便利です。一方、こっくり硬めのクリーム状で油分密閉力が高い処方はポンプで吸い上げにくいため、ジャー容器＋スパチュラ仕様が多くなります。夜のリッチケアにはジャータイプが向いています。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬のフェイスクリーム特集", "item": "https://lumi-cosme.vercel.app/winter-moisture-cream"},
                {"@type": "ListItem", "position": 3, "name": "高保湿オールインワンジェル＆クリーム10選", "item": canonical_url}
            ]
        }
    ]
}

rows_html = ""
for it, det in zip(items, details):
    rows_html += f"""            <tr>
              <td><span class="tbl-rank">{it['rank']}位</span></td>
              <td><strong>{html.escape(it['brand'])}</strong><br><span class="tbl-sub">{html.escape(det['display_name'].split('(')[0].strip())}</span></td>
              <td>{html.escape(det['form'])}</td>
              <td>{html.escape(det['key_ingredients'].split('、')[0])}</td>
              <td>{html.escape(det['moro_moro'])}</td>
              <td class="tbl-price">¥{it['price']:,}<br><span class="tbl-sub">{html.escape(det['capacity'])}</span></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rating_html = (
        f'<span class="rating-pill">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="rating-pill">楽天取扱・注目アイテム</span>'
    )
    cards_html += f"""
      <article class="aio-card" id="rank-{it['rank']}">
        <div class="aio-card-top">
          <div class="aio-rank-row">
            <span class="rank-pill rank-{it['rank']}">第{it['rank']}位</span>
            <span class="badge-pill">{html.escape(det['badge_text'])}</span>
            {rating_html}
          </div>
          <h3 class="aio-prod-title">{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
        </div>

        <div class="aio-card-body">
          <div class="aio-media-col">
            <div class="img-frame">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="price-panel">
              <span class="price-cap">楽天市場 最新確認価格（税込）</span>
              <span class="price-num">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場で在庫・詳細を見る →
            </a>
            <p class="rakuten-item-ref">掲載商品：{html.escape(it['item_name'][:48])}</p>
          </div>

          <div class="aio-info-col">
            <div class="catch-strip">{html.escape(det['catch'])}</div>

            <dl class="spec-dl">
              <div><dt>形状タイプ</dt><dd>{html.escape(det['form'])}</dd></div>
              <div><dt>内容量</dt><dd>{html.escape(det['capacity'])}</dd></div>
              <div><dt>注目成分</dt><dd>{html.escape(det['key_ingredients'])}</dd></div>
              <div><dt>朝のメイク相性</dt><dd>{html.escape(det['moro_moro'])}</dd></div>
            </dl>

            <div class="review-prose">
              <p>{html.escape(det['review_body_1'])}</p>
              <p>{html.escape(det['review_body_2'])}</p>
            </div>

            <div class="tips-pair">
              <div class="tip-box tip-target">
                <strong>向いている肌・シーン</strong>
                <p>{html.escape(det['good_for'])}</p>
              </div>
              <div class="tip-box tip-how">
                <strong>冬場の上手な塗り方</strong>
                <p>{html.escape(det['usage_note'])}</p>
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
  <meta name="keywords" content="オールインワンジェル 冬, 高保湿 オールインワン クリーム, 11月 12月 スキンケア 時短, カルテHD モイスチュアインストール, アクアレーベル, ドクターシーラボ, カナデル, メディプラスゲル">
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
      --brand: #c2410c;
      --brand-dark: #9a3412;
      --brand-soft: #fff7ed;
      --brand-border: #fed7aa;
      --ink: #1c1917;
      --muted: #57534e;
      --line: #e7e5e4;
      --bg: #fafaf9;
      --card: #ffffff;
      --radius: 14px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.75;
    }}
    header.top-bar {{
      background: #ffffff;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .top-bar-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .brand-link {{
      font-weight: 800;
      font-size: 1.15rem;
      color: var(--ink);
      text-decoration: none;
    }}
    .top-nav {{
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      font-size: 0.85rem;
    }}
    .top-nav a {{
      color: var(--brand);
      text-decoration: none;
      font-weight: 700;
    }}
    .breadcrumb {{
      max-width: 1080px;
      margin: 14px auto 0;
      padding: 0 20px;
      font-size: 0.82rem;
      color: var(--muted);
    }}
    .breadcrumb a {{ color: var(--brand); text-decoration: none; }}
    main {{
      max-width: 1080px;
      margin: 20px auto 64px;
      padding: 0 20px;
    }}
    .hero-box {{
      background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
      border: 1px solid var(--brand-border);
      border-radius: var(--radius);
      padding: 36px 30px;
      margin-bottom: 32px;
    }}
    .hero-label {{
      display: inline-block;
      background: var(--brand);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .hero-box h1 {{
      font-size: 1.75rem;
      line-height: 1.4;
      color: #292524;
      margin-bottom: 16px;
    }}
    @media (max-width: 720px) {{
      .hero-box {{ padding: 24px 18px; }}
      .hero-box h1 {{ font-size: 1.35rem; }}
    }}
    .hero-meta {{
      font-size: 0.84rem;
      color: var(--muted);
      margin-bottom: 16px;
    }}
    .hero-lead p {{
      font-size: 0.98rem;
      color: #292524;
      margin-bottom: 12px;
    }}
    .hero-lead p:last-child {{ margin-bottom: 0; }}
    .toc-panel {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 22px 26px;
      margin-bottom: 32px;
    }}
    .toc-panel h2 {{
      font-size: 1.05rem;
      margin-bottom: 12px;
      color: var(--ink);
    }}
    .toc-panel ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 8px 18px;
    }}
    .toc-panel a {{
      color: var(--brand-dark);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
    }}
    .toc-panel a:hover {{ text-decoration: underline; }}

    .editorial-block {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 28px;
      margin-bottom: 32px;
    }}
    .editorial-block h2 {{
      font-size: 1.35rem;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--brand-border);
      color: var(--ink);
    }}
    .editorial-block p {{
      font-size: 0.95rem;
      color: #44403c;
      margin-bottom: 14px;
    }}
    .three-cols {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-top: 18px;
    }}
    .col-card {{
      background: var(--brand-soft);
      border: 1px solid var(--brand-border);
      border-radius: 10px;
      padding: 18px;
    }}
    .col-card h3 {{
      font-size: 1rem;
      color: var(--brand-dark);
      margin-bottom: 8px;
    }}
    .col-card p {{
      font-size: 0.87rem;
      margin-bottom: 0;
      color: #44403c;
    }}

    .table-wrap {{
      overflow-x: auto;
      margin-top: 16px;
    }}
    .spec-compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.86rem;
      min-width: 640px;
    }}
    .spec-compare-table th, .spec-compare-table td {{
      border: 1px solid var(--line);
      padding: 10px 12px;
      text-align: left;
      vertical-align: top;
    }}
    .spec-compare-table th {{
      background: #ffedd5;
      color: #7c2d12;
      font-weight: 700;
      white-space: nowrap;
    }}
    .spec-compare-table tr:nth-child(even) {{ background: #fafaf9; }}
    .tbl-rank {{ font-weight: 800; color: var(--brand); white-space: nowrap; }}
    .tbl-price {{ font-weight: 800; color: #b91c1c; white-space: nowrap; }}
    .tbl-sub {{ font-size: 0.78rem; color: var(--muted); font-weight: 400; }}

    .ranking-heading {{
      font-size: 1.45rem;
      font-weight: 800;
      margin: 36px 0 20px;
      color: var(--ink);
    }}
    .aio-card {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 26px;
      margin-bottom: 28px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }}
    .aio-card-top {{
      border-bottom: 1px solid var(--line);
      padding-bottom: 14px;
      margin-bottom: 20px;
    }}
    .aio-rank-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .rank-pill {{
      background: var(--brand);
      color: #fff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .rank-pill.rank-1 {{ background: #b45309; }}
    .rank-pill.rank-2 {{ background: #475569; }}
    .rank-pill.rank-3 {{ background: #9a3412; }}
    .badge-pill {{
      background: var(--brand-soft);
      color: var(--brand-dark);
      border: 1px solid var(--brand-border);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .rating-pill {{
      font-size: 0.82rem;
      font-weight: 700;
      color: #b45309;
      margin-left: auto;
    }}
    .aio-prod-title {{
      font-size: 1.22rem;
      font-weight: 800;
      color: var(--ink);
      line-height: 1.4;
    }}
    .aio-card-body {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 26px;
    }}
    @media (max-width: 820px) {{
      .aio-card-body {{ grid-template-columns: 1fr; }}
    }}
    .img-frame {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 240px;
      object-fit: contain;
    }}
    .price-panel {{
      background: #fafaf9;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .price-cap {{
      display: block;
      font-size: 0.75rem;
      color: var(--muted);
    }}
    .price-num {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #c2410c 0%, #9a3412 100%);
      color: #ffffff;
      text-align: center;
      font-weight: 700;
      font-size: 0.92rem;
      padding: 13px 16px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ opacity: 0.92; }}
    .rakuten-item-ref {{
      font-size: 0.74rem;
      color: var(--muted);
      margin-top: 8px;
      line-height: 1.4;
    }}
    .catch-strip {{
      background: var(--brand-soft);
      border-left: 4px solid var(--brand);
      padding: 10px 14px;
      font-weight: 700;
      font-size: 0.94rem;
      color: #7c2d12;
      margin-bottom: 16px;
      border-radius: 0 8px 8px 0;
    }}
    .spec-dl {{
      border-top: 1px solid var(--line);
      margin-bottom: 16px;
      font-size: 0.86rem;
    }}
    .spec-dl > div {{
      display: grid;
      grid-template-columns: 120px 1fr;
      border-bottom: 1px solid var(--line);
      padding: 7px 0;
      gap: 10px;
    }}
    .spec-dl dt {{ font-weight: 700; color: var(--muted); }}
    .spec-dl dd {{ color: var(--ink); }}
    .review-prose p {{
      font-size: 0.93rem;
      color: #44403c;
      margin-bottom: 12px;
    }}
    .tips-pair {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-top: 14px;
    }}
    @media (max-width: 640px) {{
      .tips-pair {{ grid-template-columns: 1fr; }}
    }}
    .tip-box {{
      border-radius: 8px;
      padding: 12px 14px;
      font-size: 0.85rem;
    }}
    .tip-target {{ background: #f5f5f4; border: 1px solid #e7e5e4; }}
    .tip-how {{ background: #fff7ed; border: 1px solid #fed7aa; }}
    .tip-box strong {{ display: block; margin-bottom: 4px; color: var(--ink); }}
    .tip-box p {{ margin: 0; color: #44403c; line-height: 1.6; }}

    .faq-row {{
      border-bottom: 1px solid var(--line);
      padding: 16px 0;
    }}
    .faq-row:last-child {{ border-bottom: none; }}
    .faq-row h3 {{ font-size: 1rem; color: var(--ink); margin-bottom: 6px; }}
    .faq-row p {{ font-size: 0.9rem; margin-bottom: 0; color: #44403c; }}

    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--line);
      border-radius: var(--radius);
      padding: 26px;
      margin-top: 32px;
    }}
    .internal-links-title {{
      font-size: 1.15rem;
      font-weight: 800;
      margin-bottom: 16px;
      color: var(--ink);
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 14px;
    }}
    .internal-link-card {{
      background: #fafaf9;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--brand); }}

    footer {{
      background: #1c1917;
      color: #a8a29e;
      padding: 48px 20px 32px;
      font-size: 0.84rem;
    }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #fafaf9; font-weight: 800; font-size: 1rem; margin-bottom: 16px; }}
    .footer-links-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px 14px;
      margin-bottom: 28px;
    }}
    .footer-links-grid a {{ color: #d6d3d1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #fdba74; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #292524; padding-top: 20px; text-align: center; font-size: 0.78rem; }}
  </style>
</head>
<body>
  <header class="top-bar">
    <div class="top-bar-inner">
      <a href="/" class="brand-link">Lumi Cosme</a>
      <nav class="top-nav">
        <a href="/winter-moisture-cream">クリーム特集</a>
        <a href="/winter-lotion">化粧水特集</a>
        <a href="/winter-emulsion">乳液特集</a>
      </nav>
    </div>
  </header>

  <nav class="breadcrumb" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-moisture-cream">冬の高保湿クリーム特集</a> &gt; <span>高保湿オールインワンジェル＆クリーム10選</span>
  </nav>

  <main>
    <section class="hero-box">
      <span class="hero-label">2026年11月・12月 冬季時短保湿セレクション</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="hero-meta">更新日：<time datetime="2026-11-21">2026年11月21日</time> ／ 監修・調査：Lumi Cosme 編集部</div>
      <div class="hero-lead">
        <p>
          11月後半を過ぎて朝の洗面所がぐっと冷え込んでくると、化粧水・美容液・乳液・クリームと何ステップも塗り重ねるのが億劫になる日が増えてきます。さらに年末の繁忙期や帰省・温泉旅行など、スキンケアの荷物を減らしつつ保湿だけは妥協したくない場面も重なる季節です。
        </p>
        <p>
          とはいえ、過去のオールインワンにありがちだった「水っぽいだけで暖房の部屋だと昼過ぎにカサつく」「下地を重ねると消しゴムのカスのようなモロモロが出る」という弱点を持つ製品を冬に選ぶと失敗します。本記事では、ヘパリン類似物質やヒト型セラミド、油性エモリエントをしっかり乳化した<strong>真冬対応の高保湿オールインワン10品</strong>を、楽天の最新実勢価格とともに比較しました。
        </p>
      </div>
    </section>

    <nav class="toc-panel" aria-label="目次">
      <h2>この記事でわかること</h2>
      <ul>
        <li><a href="#why-dry">1. なぜ冬に「普通のオールインワン」だと乾きやすいのか</a></li>
        <li><a href="#choose">2. 11月・12月の肌質＆用途別・失敗しない選び方</a></li>
        <li><a href="#compare">3. 高保湿オールインワン10選 スペック＆価格比較表</a></li>
        <li><a href="#ranking">4. 厳選おすすめランキング10選（個別詳細レビュー）</a></li>
        <li><a href="#layering">5. 翌朝まで潤いを逃さない「冬場の塗り方3つの工夫」</a></li>
        <li><a href="#faq">6. オールインワンの冬の疑問 Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="editorial-block" id="why-dry">
      <h2>1. なぜ「オールインワンは冬に物足りない」と言われがちなのか？</h2>
      <p>
        オールインワン化粧品の多くは、水を抱え込む力に優れたポリマー（カルボマーやキサンタンガムなど）でとろみやゲル状の見た目を作っています。塗った直後はぷるんと瑞々しく感じますが、<strong>油分（スクワラン・シア脂・セラミド等）の配合比率が低いさっぱり系ジェル</strong>は、湿度30%を切る11月〜12月の暖房室内では水分が外気に奪われやすく、数時間後に頬のつっぱりを感じやすくなります。
      </p>
      <p>
        冬の乾燥対策としてオールインワンを選ぶなら、単に「水分が多い透明ジェル」ではなく、油性エモリエント成分や細胞間脂質を補う成分が乳化されている<strong>「エマルジョンゲル（乳液・クリーム寄り）」</strong>を手に取ることが重要です。水分を与えると同時に蒸発を防ぐフタの役割まで1回で完了するため、フルラインケアと遜色ない保湿感が翌朝まで続きやすくなります。
      </p>
    </section>

    <section class="editorial-block" id="choose">
      <h2>2. 失敗しない！11月・12月の目的別オールインワン選び3基準</h2>
      <div class="three-cols">
        <div class="col-card">
          <h3>朝のメイク前・時短重視なら</h3>
          <p>増粘ポリマーの割合が抑えられた乳液ベースのゲル（カルテHD、アクアレーベルなど）が向いています。塗ってから2分ほど置けば下地と混ざってモロモロが出にくく、ファンデーションのノリも安定します。</p>
        </div>
        <div class="col-card">
          <h3>夜の暖房・粉吹きガードなら</h3>
          <p>シア脂・スクワラン・オイルカプセル・コラーゲンなど油分と抱水力が高いこっくり系（極潤ハリパーフェクトゲル、カナデル、コラリッチなど）をセレクト。寝室の乾燥から一晩中肌を守ります。</p>
        </div>
        <div class="col-card">
          <h3>肌荒れ・シワ・美白も狙うなら</h3>
          <p>「医薬部外品」の表記がある製品が狙い目です。ヘパリン類似物質やグリチルリチン酸ジカリウムは寒暖差の肌荒れ予防に、ナイアシンアミドやトラネキサム酸は冬場の小ジワ・くすみケアに役立ちます。</p>
        </div>
      </div>
    </section>

    <section class="editorial-block" id="compare">
      <h2>3. 高保湿オールインワンジェル＆クリーム10選 比較一覧表</h2>
      <p>楽天市場で確認できた最新実勢価格（税込）と、テクスチャー・朝のメイクとの相性を一覧にまとめました。</p>
      <div class="table-wrap">
        <table class="spec-compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>形状タイプ</th>
              <th>主力保湿・有効成分</th>
              <th>朝のメイク相性</th>
              <th>参考価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{rows_html}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="ranking-heading" id="ranking">4. 11月・12月におすすめの高保湿オールインワン厳選ランキング10選</h2>
    <section aria-label="ランキング詳細">
{cards_html}    </section>

    <section class="editorial-block" id="layering">
      <h2>5. オールインワンをフルライン級に変える「冬場の塗り方」3つの工夫</h2>
      <div class="three-cols">
        <div class="col-card">
          <h3>工夫1：洗顔後の「半乾き前」に乗せる</h3>
          <p>お風呂上がりや洗顔後は1分単位で角層から水分が逃げていきます。タオルで水気を優しく押さえたら、肌がまだ少しひんやり湿っているうちにオールインワンを伸ばすと、角層の水分ごと閉じ込めやすくなります。</p>
        </div>
        <div class="col-card">
          <h3>工夫2：乾燥しやすい頬・目元だけ二度塗り</h3>
          <p>Tゾーンは皮脂が出やすく頬だけ乾く方は、全顔に薄く1回塗ったあと、乾燥が気になる頬骨周り・口角・目の下だけに米粒大を追加で点置きし、薬指でそっと馴染ませるとテカリと乾燥を同時に防げます。</p>
        </div>
        <div class="col-card">
          <h3>工夫3：朝は塗ったあと「2分待つ」</h3>
          <p>塗ってすぐ日焼け止めやリキッドファンデーションを塗るとゲル成分と混ざってヨレの原因に。着替えや歯磨きの前にサッと塗って2分ほど定着させてからメイクを始めると、モロモロ知らずで密着力も上がります。</p>
        </div>
      </div>
    </section>

    <section class="editorial-block" id="faq">
      <h2>6. 冬のオールインワンに関するよくある質問（FAQ）</h2>
      <div class="faq-row">
        <h3>Q1. 真冬の11月・12月でも本当にこれ1本だけで大丈夫ですか？</h3>
        <p>今回上位に挙げたカルテHDやアクアレーベル、ドクターシーラボのような油性エモリエント（スクワランやセラミド類似成分、シア脂等）を含む乳化型ゲルであれば、一般的な乾燥肌・混合肌の方は1本でも十分対応できます。極度の乾燥肌で雪国や長時間暖房の部屋にいる方は、夜だけ頬にクリームやワセリンを少し重ねるとより万全です。</p>
      </div>
      <div class="faq-row">
        <h3>Q2. 朝使うとファンデーションが消しゴムのカスみたいにポロポロ出ます。</h3>
        <p>ゲルを固める増粘ポリマーが肌表面に残った状態で、下地やファンデーションを強く擦り伸ばすと起きやすい現象です。朝は塗る量を少し控えめにする、擦らず手のひらで押さえるように馴染ませる、そして馴染んでから2〜3分時間を置いてベースメイクに入ると大きく改善します。</p>
      </div>
      <div class="faq-row">
        <h3>Q3. 手持ちの化粧水や導入美容液と併用しても良いですか？</h3>
        <p>もちろん併用できます。特に冬の朝、洗顔後に肌がゴワついていると感じる時は、導入美容液や化粧水をさっと馴染ませてからオールインワンでフタをする使い方にすると、保湿の持続力がぐっと伸びます。</p>
      </div>
      <div class="faq-row">
        <h3>Q4. 1つあたりの持ち（使用期間）はどれくらいですか？</h3>
        <p>内容量にもよりますが、75g〜100gの標準サイズを朝晩使って約1.5〜2ヶ月、180gのメディプラスゲルや120gのアクアコラーゲンゲルなら約2〜2.5ヶ月が目安です。1本で全工程が済むため、トータルのスキンケア費用を抑えやすい点もメリットです。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-moisture-cream" class="internal-link-card">
          <strong>冬のフェイスクリーム特集</strong>
          <span>夜の集中密閉におすすめの高保湿クリーム10選</span>
        </a>
        <a href="/winter-lotion" class="internal-link-card">
          <strong>冬の高保湿化粧水特集</strong>
          <span>インナードライを潤す濃厚化粧水10選</span>
        </a>
        <a href="/winter-emulsion" class="internal-link-card">
          <strong>冬の高保湿乳液特集</strong>
          <span>角層を柔らかく整える乳液10選</span>
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

with open("winter-all-in-one.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-all-in-one.html successfully!")
