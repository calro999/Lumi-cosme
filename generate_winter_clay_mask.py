import json
import html

with open("fetched_3new_nov_dec_2026_1122.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_clay_mask"]["items"]

details = [
    {
        "rank": 1,
        "clay_type": "海泥（タナクラクレイ）× アセチル化ヒアルロン酸",
        "display_name": "ルミナイジング クレイex 100g",
        "texture": "なめらかな生クリーム状ペースト（微細スクラブ感あり）",
        "capacity": "100g",
        "moist_points": "アセチル化ヒアルロン酸Na、カミツレ花エキス、オタネニンジン根エキス",
        "wash_feel": "しっとりツルン（水洗い後もツッパリ感なし）",
        "summary": "乾燥して硬くなった冬の角層をやさしく磨き上げ、洗い流した直後から化粧水が入りやすい肌へ整える名品",
        "prose_1": "デパコス系の洗い流すクレイマスクとして長年支持を集めるイプサの『ルミナイジング クレイex』。最大の魅力は、皮脂吸着に優れた海泥ベースのペーストでありながら、高保水成分のアセチル化ヒアルロン酸（スーパーヒアルロン酸）やカミツレ花エキスがしっかり組み込まれている点にあります。乾いた状態でも濡れた肌でも使える2WAY仕様なので、11月・12月の寒い夜に浴室で温まりながら使えるのが大きな強みです。",
        "prose_2": "肌に伸ばすと厚みのあるクリーミーな泥が密着し、5分ほど置いてからぬるま湯でクルクル馴染ませると、粒子の細かいクレイが古い角質や小鼻のざらつきを穏やかに絡め取ってくれます。洗い流した後は「皮脂を根こそぎ奪われたキュッとした感じ」ではなく、内側に水分が残ったような柔らかな手触りに。週1〜2回のケアに取り入れると、冬のファンデーションの密着度がぐっと変わります。",
        "best_for": "寒さで肌がゴワつき、いつもの化粧水が表面で弾かれるように感じる方・デパコスらしい上品な洗い上がりを求める方",
        "pro_tip": "乾いた肌に塗ると吸着力が上がり、濡れた肌に伸ばすとマイルドに整います。乾燥しやすい12月は、湯船に数分浸かって顔を軽く濡らした状態で使うのが快適です。"
    },
    {
        "rank": 2,
        "clay_type": "アマゾンホワイトクレイ（カオリン）× アロエベラ液汁",
        "display_name": "レアアース マスク 125mL",
        "texture": "密度の高いマットクリーム状（少量でよく伸びる）",
        "capacity": "125mL",
        "moist_points": "アロエベラ液汁、カラスムギ穀粒（オートミール）、スクワラン、グリセリン",
        "wash_feel": "毛穴スッキリ＋すべすべ（過度な乾燥感なし）",
        "summary": "楽天市場でもレビュー360件超・★4.6台の高評価。ホワイトクレイの毛穴吸着力とアロエの保湿バランスが秀逸",
        "prose_1": "キールズのロングセラーである『レアアース マスク』は、ブラジル・アマゾン川流域のミネラルを含むホワイトクレイ（カオリン）を主軸にしながら、肌を落ち着かせるアロエベラ液汁やオートミール由来の保湿成分、スクワランをバランスよく配合した洗い流すパックです。125mL入りの大容量ジャーで持ちが良く、冬は乾燥しやすい頬を避けてTゾーン中心に部分使いするのも賢い方法です。",
        "prose_2": "テクスチャーはやや硬めに見えますが、肌に薄く均一に広がり、塗ってから数分経つとほんのり温かみを感じます。完全にパリパリにひび割れるまで待つ必要はなく、少し乾き始めたタイミング（約5〜10分）でぬるま湯を含ませたタオルや手で優しく落とすと、小鼻周りの詰まり感がすっきりしつつも突っ張りにくい仕上がりになります。",
        "best_for": "暖房の部屋でTゾーンだけ皮脂が浮きやすく毛穴汚れが気になる方・1瓶で長持ちする実力派を探している方",
        "pro_tip": "頬が特に乾きやすい真冬は、額・鼻・顎の「Tゾーン＋アゴ先」だけにポイント使いし、10分以内に洗い流すと必要な皮脂まで落としすぎません。"
    },
    {
        "rank": 3,
        "clay_type": "6種の複合クレイ × 緑豆エキス＆ツボクサ",
        "display_name": "緑豆毛穴クレイパック 120mL",
        "texture": "ホイップのように軽く瑞々しいクリームクレイ",
        "capacity": "120mL",
        "moist_points": "緑豆（リョクトウ）種子エキス、ナイアシンアミド、アラントイン、ツボクサエキス",
        "wash_feel": "極めてしっとり・もっちり（クレイ初心者にも◎）",
        "summary": "韓国コスメで人気急上昇中の「乾きにくくてつっぱらない」新世代クレイパック。ホイップ質感で肌に負担をかけにくい",
        "prose_1": "「泥パックは放置中にカピカピに固まって肌が痛くなるから苦手」というイメージを大きく変えてくれるのが、beplain（ビープレーン）の『緑豆毛穴クレイパック』です。整肌効果のある緑豆エキスをベースに、粒子の異なる複数のクレイをきめ細かなクリーム状に練り込んでおり、肌に塗ってから10分経っても表面がひび割れにくい処方になっています。",
        "prose_2": "水分をたっぷり含んだ柔らかいテクスチャーのおかげで、冬の冷えた浴室でも肌の上でスルスル伸び、洗い流す際も水とすぐ混ざってサッと落ちます。ナイアシンアミドやアラントインといった保湿・整肌サポート成分もしっかり入っているため、パック後の肌がカサつくどころか、キメが整ってワントーン明るく澄んだような印象に仕上がります。",
        "best_for": "従来の固まるクレイマスクで乾燥・ヒリつきを経験したことがある方・時短（3〜5分）で済ませたい方",
        "pro_tip": "洗顔後の水気を軽く拭いた肌に肌色が隠れるくらい薄く塗り、3〜5分ほど置いたらぬるま湯で優しく洗い流すだけで十分手応えを感じられます。"
    },
    {
        "rank": 4,
        "clay_type": "済州島火山灰（ヴォルカニック）× 乳酸・AHA",
        "display_name": "スーパーヴォルカニック ポア クレイマスク 100mL",
        "texture": "ムースのように柔らかいシルキーペースト",
        "capacity": "100mL",
        "moist_points": "パンテノール、乳酸、グリセリン、ツボクサ関連保湿サポート",
        "wash_feel": "さっぱりなめらか（リニューアル後さらにクリーミーに）",
        "summary": "プチプラ帯で圧倒的な知名度を誇る定番クレイ。クリーミーな塗り心地に進化し、冬の鼻周りざらつき対策に重宝",
        "prose_1": "チェジュ島の火山灰由来の吸着力で世界的なヒットを続けるイニスフリーの『スーパーヴォルカニック ポア クレイマスク』。従来品よりもクリーミーな質感へとアップデートされており、真冬の乾燥シーズンでも容器の中で硬くなりにくく、指にすっと取って広げやすいのが特徴です。価格も¥1,880（調査時点）と手に取りやすく、初めてのクレイパックとしても定番です。",
        "prose_2": "毛穴の皮脂や古い角質を吸着する火山灰に加え、角質を穏やかに整えるAHA（乳酸）や肌荒れを防ぐ成分をバランスよく組み合わせています。冬場はエアコンで顔全体が乾きやすい一方で、小鼻の横や眉間だけは角栓が溜まりがち。週に1回、気になる箇所に10分ほど乗せて流すだけでも、翌朝のベースメイクのノリが格段に整います。",
        "best_for": "2,000円以下で信頼できる定番品を探している方・小鼻や眉間のざらつきと黒ずみケアを習慣にしたい方",
        "pro_tip": "塗ったあと放置時間を10分〜15分と長く取りすぎず、表面が半乾きになる7〜8分程度で流し始めると、つっぱり感を抑えながらすっきり洗い上がります。"
    },
    {
        "rank": 5,
        "clay_type": "棚倉クレイ × 化石サンゴパウダー × 植物オイル",
        "display_name": "ピュリファイング クレイマスク 120g",
        "texture": "濃厚なボタニカルオイルを抱えた滑らかクリーム",
        "capacity": "120g",
        "moist_points": "植物油（ホホバ油・シア脂系エモリエント）、化石サンゴ、精油ブレンド",
        "wash_feel": "オイルケア後のようなしっとり吸い付く後肌",
        "summary": "乾燥肌の大人世代から絶大な支持を集めるTHREEの名品。植物オイルとクレイの融合で、冬でも潤い膜が残る",
        "prose_1": "日本の国産クレイである「棚倉クレイ」と沖縄県産の化石サンゴパウダーに、THREEならではの豊かな植物オイルを贅沢に練り込んだ『ピュリファイング クレイマスク』。クレイマスクでありながらエモリエント成分が豊富に含まれているため、塗っている最中も精油の深い香りに包まれながら、まるでトリートメントクリームを乗せているような心地よさがあります。",
        "prose_2": "汚れや不要な角質はしっかり吸着しつつ、肌本来が持つ潤いまで奪わない処方設計は、皮脂分泌が減って乾燥が進む11月・12月の大人肌にまさに理想的。5〜7分ほど置いてぬるま湯で洗い流すと、肌がふっくら柔らかくほぐれ、その後に使うオイルや化粧水が驚くほどすんなり馴染みます。",
        "best_for": "30代〜50代以上の乾燥肌・エイジング世代の方、精油の香りで年末の疲れを癒やしながらケアしたい方",
        "pro_tip": "1〜2分ほど湯船で顔が温まってから薄く伸ばし、5分経ったら乳化させるように少しずつぬるま湯を足して洗い流すと、オイルの潤いが心地よく残ります。"
    },
    {
        "rank": 6,
        "clay_type": "5種のクレイ × マダガスカル産CICA × 小豆パウダー",
        "display_name": "マダガスカル センテラ ポアマイジング クイッククレイスティックマスク 27g",
        "texture": "固形スティック（肌に滑らせるとしっとり密着）",
        "capacity": "27g",
        "moist_points": "ツボクサエキス（CICA）、小豆（アズキ）種子エキス、アロエベラ葉エキス",
        "wash_feel": "みずみずしく鎮静感あり（手も爪の間も汚れない）",
        "summary": "「手が泥で汚れる」「スパチュラを洗うのが面倒」という悩みを一掃するスティック式。部分塗りが圧倒的に楽",
        "prose_1": "冬場の寒い脱衣所や洗面台で、指やスパチュラを使って冷たいクレイをすくう作業すら億劫な日に画期的なのが、SKIN1004の『クイッククレイスティックマスク』です。リップクリームを大きくしたような繰り出し式スティックになっており、洗顔後の肌に直接くるくると滑らせるだけで手を汚さずに均一に塗布できます。",
        "prose_2": "5種類のクレイを配合しながら、SKIN1004の代名詞である高純度マダガスカル産CICA（ツボクサエキス）や保湿力の高いアロエベラ葉エキスを掛け合わせているため、乾燥や寒暖差で赤みが出やすい冬肌にも使いやすい処方。小鼻の脇やTゾーンだけピンポイントに塗って3〜5分で洗い流せる手軽さは、忙しい平日の夜にも無理なく続けられます。",
        "best_for": "クレイパックの手間・爪の間が汚れるストレスをなくしたい方、小鼻やTゾーンの部分ケアを時短で済ませたい方",
        "pro_tip": "使用後はスティック表面の水分を軽くティッシュで拭き取ってからキャップを閉めると衛生的に保てます。乾燥する頬は避けてTゾーン中心に塗るのも簡単です。"
    },
    {
        "rank": 7,
        "clay_type": "グリーンクレイ × シカヒアルロン × クランベリー",
        "display_name": "CICA カプセルマスク 7.5g×10個",
        "texture": "しっとり柔らかなクリームクレイ（1回使い切り個包装）",
        "capacity": "7.5g×10個",
        "moist_points": "CICA（ツボクサエキス）、3種ヒアルロン酸、緑茶パウダー、クランベリー果実エキス",
        "wash_feel": "もっちり鎮静＆ひんやり心地よい（旅行・帰省にも◎）",
        "summary": "1回分ずつの個包装だから冬場の旅行・年末年始の帰省にも持ち運びやすい。クリームベースで乾きにくい設計",
        "prose_1": "ジャータイプのクレイマスクは開封後に少しずつ水分が飛んで硬くなりがちですが、VTの『CICA カプセルマスク』は1回7.5gずつのポーション型個包装になっているため、いつでも開けたての瑞々しいクリームクレイを使えるのが最大のメリット。11月・12月の温泉旅行や年末年始の帰省ポーチに1〜2個忍ばせておくのにも重宝します。",
        "prose_2": "ベースがしっとりしたクリーム処方で、VT独自の保湿鎮静成分「シカリオ」と3重ヒアルロン酸を組み合わせているため、10〜15分置いてもパリパリに乾燥しません。柔らかい緑茶パウダーが穏やかに古い角質をからめ取り、洗い流した後は肌のごわつきが抜けてつるんとした触り心地に整います。",
        "best_for": "いつも新鮮な状態で使いたい方・年末年始の旅行や外泊先に持って行きたい方・マスク摩擦や暖房ゆらぎが気になる方",
        "pro_tip": "1個7.5gとたっぷり入っているので、顔だけでなくザラつきが気になる首筋やデコルテまで一緒に伸ばして湯船で温まるのもおすすめです。"
    },
    {
        "rank": 8,
        "clay_type": "天然クレイ100%（モンモリロナイト主体の砂漠ミネラル粘土）",
        "display_name": "キャニスターセット 400g (クレイパウダー／パック・入浴両用)",
        "texture": "水に溶くと絹のように滑らかな粘土ジェル状",
        "capacity": "400g（専用キャニスター付）",
        "moist_points": "豊富な天然ミネラル（シリカ・マグネシウム・カルシウム等）による浸透圧保湿",
        "wash_feel": "驚くほどしっとりスベスベ（入浴剤にも使える万能品）",
        "summary": "400gでフェイスパックにも冬のお風呂のバスクレイ（入浴剤）にも使える名品。ミネラルの恵みで湯上がり肌まで潤う",
        "prose_1": "アメリカ西海岸の砂漠地帯で採掘される高品質な天然クレイのみを使用したCLAYD（クレイド）の『キャニスターセット 400g』。粒子が非常に細かいため、水と混ぜてペーストにすると絹のように滑らかな質感になり、肌を擦らずに優しく密着します。防腐剤や香料などを一切含まない100%天然泥なので、自分の肌状態に合わせて水分量を調整できるのが魅力です。",
        "prose_2": "さらに冬場ならではの楽しみ方が「バスクレイ（入浴剤）」としての活用。湯船に溶かして浸かると身体が芯から温まり、全身の肌あたりが驚くほどまろやかになります。フェイスパックとして使うときは、手持ちの化粧水やホホバオイルを1〜2滴混ぜてペーストを作ると、真冬の超乾燥肌でも極上のしっとり感を楽しめます。",
        "best_for": "無添加・天然100%のクレイにこだわりたい方、フェイスパックと冬の温浴入浴剤の両方で贅沢に使いたい方",
        "pro_tip": "パック用に水で溶く際は金属製スプーンを避け、ガラスや木製の器・スプーンで水（または精製水）を少しずつ加えてマヨネーズ状にしてから冷蔵保存すると約1〜2週間使えます（※都度作る場合は大さじ1弱で1回分）。"
    },
    {
        "rank": 9,
        "clay_type": "モロッコ産溶岩クレイ（ガスール100%）",
        "display_name": "ガスール固形 500g / 粉末",
        "texture": "水で溶くとトロッと艶のある粘土クリーム状",
        "capacity": "500g",
        "moist_points": "マグネシウム・カルシウムなどの天然ミネラル（モロッコアトラス山脈由来）",
        "wash_feel": "洗い流したのにオイルを塗った後のようなしっとり感",
        "summary": "「泥なのに洗うと肌がしっとり潤う」と長年愛されるモロッコ産ガスール。500g大容量でボディにも惜しみなく使える",
        "prose_1": "モロッコで古くから美容と洗浄に使われてきた天然粘土「ガスール」をそのまま製品化したナイアードの大定番。レビュー件数60件超・★4.6台と安定した人気を誇り、500g入りで¥1,980（調査時点）という圧倒的なコストパフォーマンスを誇ります。化学的な界面活性剤を一切使わず、粘土のイオンと吸着作用だけで汚れを落とすため、皮脂膜を取りすぎないのが最大の特徴です。",
        "prose_2": "粉末タイプは水を加えて数十秒混ぜるだけですぐに滑らかなペースト状になり、肌に乗せるとヒンヤリせずまろやかな感触。乾燥が厳しい11月・12月は、ぬるま湯で溶いたペーストにアルガンオイルやホホバオイルを数滴垂らして「オイルイン泥パック」にアレンジすると、冬でも驚くほどもっちり潤った洗い上がりになります。",
        "best_for": "界面活性剤や添加物を避けたい敏感肌の方、顔だけでなくデコルテや背中・ひじ・かかとの乾燥ザラつきにもたっぷり使いたい方",
        "pro_tip": "放置しすぎて乾かすと洗い流しにくくなるため、お風呂で塗ってから3〜5分以内・ペーストがまだ湿っているうちに流すのがコツです。"
    },
    {
        "rank": 10,
        "clay_type": "ピンククレイ（カオリン・モロッコ溶岩クレイ）× セラミド＆CICA",
        "display_name": "ピンククレイパック 110g (洗い流す保湿泥パック)",
        "texture": "ぷるんと柔らかなペースト状（垂れにくく密着）",
        "capacity": "110g",
        "moist_points": "ヒト型セラミド（セラミドNP/AP/EOP）、ツボクサエキス、ビタミンC誘導体、スクワラン",
        "wash_feel": "つるんとしっとり（冬のくすみ晴らしにぴったり）",
        "summary": "2,000円以下でヒト型セラミドやスクワランまで配合された、ドラッグストア系でも人気の高保湿ピンク泥パック",
        "prose_1": "クレイシャンプーでも定評のあるCLAYGE（クレージュ）のフェイス用洗い流すパック『ピンククレイパック 110g』。肌に優しいピンククレイやモロッコ溶岩クレイをベースにしつつ、保湿の要であるセラミドやスクワラン、さらにビタミンC誘導体やツボクサエキスを配合し、くすみやすい冬の素肌を明るい印象へ導く設計です。",
        "prose_2": "優しいローズ系の香りと柔らかいペースト質感で、寒い夜のバスタイムでもストレスなく伸ばせます。洗顔後に軽くタオルで水気を拭いた肌へ広げ、3〜5分ほど湯船に浸かってから洗い流すと、毛穴のモヤつきがスッキリ抜けつつも、セラミドやスクワランのおかげで肌表面がしっとり柔らかく仕上がります。",
        "best_for": "2,000円前後の予算でセラミド配合の保湿泥パックを試したい方、冬の血行不良による顔色のどんより感が気になる方",
        "pro_tip": "洗い流した直後は角層の透明感が引き出され、同時に乾燥も始まりやすいタイミング。浴室を出たらすぐ化粧水や導入美容液で水分を補給しましょう。"
    }
]

article_title = "お風呂で温まりながらくすみ・ゴワつきを潤いオフ！つっぱらない高保湿クレイマスク＆洗い流す泥パック厳選ランク10【11月・12月】"
article_desc = "11月・12月の冷えでゴワつく肌と冬のくすみをケア！イプサ、キールズ、ビープレーン、イニスフリー、THREE、SKIN1004、VT、CLAYD、ナイアードガスール、クレージュなど、つっぱらずしっとり潤う高保湿クレイマスク・洗い流す泥パック10選を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-clay-mask"

json_ld_graph = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": article_title,
            "description": article_desc,
            "image": items[0]["image_url"],
            "datePublished": "2026-11-22T05:00:00+09:00",
            "dateModified": "2026-11-22T05:00:00+09:00",
            "author": {"@type": "Organization", "name": "Lumi Cosme 編集部"},
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme (ルミコスメ)",
                "logo": {"@type": "ImageObject", "url": "https://lumi-cosme.vercel.app/favicon.jpg"}
            }
        },
        {
            "@type": "ItemList",
            "name": "11月・12月向け高保湿クレイマスク＆洗い流す泥パック10選",
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
                    "name": "乾燥しやすい11月・12月の冬にクレイマスク（泥パック）を使っても大丈夫ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "大丈夫です。ただし冬は『皮脂を取りすぎる乾きやすいタイプ』ではなく、ヒアルロン酸・セラミド・植物オイル・アロエなどが配合された保湿型クレイや、乾いてパリパリに固まる前に3〜5分で洗い流せるクリームタイプの泥パックを選ぶのがポイントです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "シートマスクとクレイマスク、冬のスペシャルケアはどう使い分けるべき？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "冷え込みが厳しく冷たいシートマスクを顔に乗せるのが辛い夜や、古い角質が溜まって化粧水が入りにくいと感じるときは、湯船で温まりながら使えるクレイマスクで先に表面のゴワつきをオフするのがおすすめです。クレイ後にシートマスクを重ねると浸透感がいっそう高まります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬のクレイパックは週に何回くらい使うのがベストですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "乾燥しやすい冬場は、やりすぎると必要な皮脂膜まで落ちやすくなるため、週1〜2回を目安にするのが安心です。Tゾーンだけ皮脂が出やすい混合肌の方は、頬には塗らず鼻・額・あご先だけ部分使いするのも効果的です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "放置時間はパッケージ通り完全に乾くまで待った方が良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "冬場は完全に水分が飛んでひび割れるまで待つと肌の水分まで奪われやすくなります。湯船のスチームがある浴室で使い、少し表面が落ち着いてきた3〜7分程度（半乾き手前）でぬるま湯で優しく洗い流す方が、潤いを残したままスッキリ仕上がります。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬の高保湿フェイスマスク特集", "item": "https://lumi-cosme.vercel.app/winter-face-mask"},
                {"@type": "ListItem", "position": 3, "name": "高保湿クレイマスク＆泥パック10選", "item": canonical_url}
            ]
        }
    ]
}

table_rows = ""
for it, det in zip(items, details):
    table_rows += f"""            <tr>
              <td class="c-rank">{it['rank']}位</td>
              <td><strong>{html.escape(it['brand'])}</strong><div class="c-sub">{html.escape(det['display_name'])}</div></td>
              <td>{html.escape(det['clay_type'])}</td>
              <td>{html.escape(det['wash_feel'])}</td>
              <td class="c-price">¥{it['price']:,}<div class="c-sub">{html.escape(det['capacity'])}</div></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rating_pill = (
        f'<span class="clay-rate">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="clay-rate">楽天市場 確認済アイテム</span>'
    )
    cards_html += f"""
      <article class="clay-card" id="item-{it['rank']}">
        <div class="clay-card-head">
          <div class="clay-meta-row">
            <span class="clay-rank-badge">RANK {it['rank']}</span>
            <span class="clay-type-badge">{html.escape(det['clay_type'])}</span>
            {rating_pill}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <p class="clay-catch">{html.escape(det['summary'])}</p>
        </div>

        <div class="clay-grid">
          <div class="clay-visual">
            <div class="clay-img-box">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="clay-price-box">
              <span class="price-lbl">楽天市場 最新確認価格（税込）</span>
              <span class="price-val">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場で商品・価格を見る →
            </a>
            <div class="clay-ref-name">取得商品：{html.escape(it['item_name'][:52])}</div>
          </div>

          <div class="clay-detail">
            <div class="clay-specs">
              <div><span>テクスチャー</span><strong>{html.escape(det['texture'])}</strong></div>
              <div><span>内容量</span><strong>{html.escape(det['capacity'])}</strong></div>
              <div><span>保湿・整肌成分</span><strong>{html.escape(det['moist_points'])}</strong></div>
              <div><span>洗い上がり</span><strong>{html.escape(det['wash_feel'])}</strong></div>
            </div>

            <div class="clay-prose">
              <p>{html.escape(det['prose_1'])}</p>
              <p>{html.escape(det['prose_2'])}</p>
            </div>

            <div class="clay-notes">
              <div class="note-item">
                <strong>こんな冬の肌悩みにおすすめ</strong>
                <p>{html.escape(det['best_for'])}</p>
              </div>
              <div class="note-item">
                <strong>つっぱらない使い方のコツ</strong>
                <p>{html.escape(det['pro_tip'])}</p>
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
  <meta name="keywords" content="クレイマスク 乾燥肌 冬, 泥パック 保湿, 洗い流すパック 11月 12月, イプサ ルミナイジングクレイ, キールズ レアアースマスク, ビープレーン 緑豆, ナイアード ガスール">
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
      --teal: #0f766e;
      --teal-deep: #134e4a;
      --teal-soft: #f0fdfa;
      --teal-line: #99f6e4;
      --stone-bg: #f8faf9;
      --ink: #1e293b;
      --muted: #475569;
      --border: #e2e8f0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--stone-bg);
      color: var(--ink);
      line-height: 1.78;
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
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .logo-link {{
      font-weight: 800;
      font-size: 1.12rem;
      color: var(--teal-deep);
      text-decoration: none;
    }}
    .nav-links {{
      display: flex;
      gap: 14px;
      flex-wrap: wrap;
      font-size: 0.85rem;
    }}
    .nav-links a {{
      color: var(--teal);
      text-decoration: none;
      font-weight: 700;
    }}
    .crumbs {{
      max-width: 1080px;
      margin: 14px auto 0;
      padding: 0 20px;
      font-size: 0.82rem;
      color: var(--muted);
    }}
    .crumbs a {{ color: var(--teal); text-decoration: none; }}
    main {{
      max-width: 1080px;
      margin: 20px auto 64px;
      padding: 0 20px;
    }}
    .clay-hero {{
      background: linear-gradient(135deg, #f0fdfa 0%, #ccfbf1 100%);
      border: 1px solid var(--teal-line);
      border-radius: 16px;
      padding: 36px 30px;
      margin-bottom: 28px;
    }}
    .clay-tag {{
      display: inline-block;
      background: var(--teal);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .clay-hero h1 {{
      font-size: 1.72rem;
      line-height: 1.42;
      color: var(--teal-deep);
      margin-bottom: 14px;
    }}
    .clay-hero-meta {{
      font-size: 0.84rem;
      color: var(--muted);
      margin-bottom: 16px;
    }}
    .clay-hero p {{
      font-size: 0.96rem;
      margin-bottom: 10px;
      color: #1e293b;
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--teal);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .toc-box h2 {{
      font-size: 1.05rem;
      color: var(--teal-deep);
      margin-bottom: 10px;
    }}
    .toc-box ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 6px 18px;
    }}
    .toc-box a {{
      color: var(--teal);
      text-decoration: none;
      font-size: 0.92rem;
      font-weight: 600;
    }}
    .section-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .section-card h2 {{
      font-size: 1.32rem;
      color: var(--teal-deep);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--teal-soft);
    }}
    .section-card p {{
      font-size: 0.96rem;
      margin-bottom: 12px;
    }}
    .clay-3col {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .clay-pillar {{
      background: var(--teal-soft);
      border: 1px solid var(--teal-line);
      border-radius: 12px;
      padding: 18px;
    }}
    .clay-pillar h3 {{
      font-size: 1rem;
      color: var(--teal-deep);
      margin-bottom: 8px;
    }}
    .clay-pillar p {{ font-size: 0.89rem; margin-bottom: 0; }}
    .table-scroll {{ overflow-x: auto; margin-top: 14px; }}
    .compare-tbl {{
      width: 100%;
      border-collapse: collapse;
      min-width: 720px;
      font-size: 0.88rem;
    }}
    .compare-tbl th {{
      background: var(--teal-deep);
      color: #fff;
      text-align: left;
      padding: 11px 12px;
    }}
    .compare-tbl td {{
      padding: 12px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }}
    .compare-tbl tr:nth-child(even) td {{ background: #f8fafc; }}
    .c-rank {{ font-weight: 800; color: var(--teal); white-space: nowrap; }}
    .c-price {{ font-weight: 700; color: var(--teal-deep); white-space: nowrap; }}
    .c-sub {{ font-size: 0.78rem; color: var(--muted); font-weight: 400; margin-top: 2px; }}

    .ranking-sec-title {{
      font-size: 1.4rem;
      color: var(--teal-deep);
      margin: 34px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--teal);
    }}
    .clay-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(15, 118, 110, 0.04);
    }}
    .clay-card-head {{ margin-bottom: 18px; }}
    .clay-meta-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .clay-rank-badge {{
      background: var(--teal-deep);
      color: #fff;
      font-weight: 800;
      font-size: 0.8rem;
      padding: 4px 11px;
      border-radius: 6px;
    }}
    .clay-type-badge {{
      background: var(--teal-soft);
      color: var(--teal);
      border: 1px solid var(--teal-line);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .clay-rate {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #b45309;
      background: #fef3c7;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .clay-card-head h3 {{
      font-size: 1.25rem;
      color: var(--ink);
      margin-bottom: 6px;
    }}
    .clay-catch {{
      font-size: 0.92rem;
      color: var(--teal);
      font-weight: 700;
    }}
    .clay-grid {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .clay-img-box {{
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{
      max-width: 100%;
      height: 210px;
      object-fit: contain;
    }}
    .clay-price-box {{
      background: var(--teal-soft);
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .price-lbl {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .price-val {{ font-size: 1.35rem; font-weight: 800; color: var(--teal-deep); }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      text-align: center;
      background: #bf0000;
      color: #fff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 12px 14px;
      border-radius: 8px;
      text-decoration: none;
    }}
    .rakuten-btn:hover {{ background: #990000; }}
    .clay-ref-name {{
      margin-top: 8px;
      font-size: 0.72rem;
      color: var(--muted);
      line-height: 1.4;
      word-break: break-all;
    }}
    .clay-specs {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    .clay-specs div span {{
      display: block;
      font-size: 0.74rem;
      color: var(--muted);
    }}
    .clay-prose p {{
      font-size: 0.94rem;
      margin-bottom: 10px;
    }}
    .clay-notes {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .note-item {{
      background: var(--teal-soft);
      border: 1px solid var(--teal-line);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.85rem;
    }}
    .note-item strong {{
      display: block;
      color: var(--teal-deep);
      margin-bottom: 4px;
    }}
    .note-item p {{ margin: 0; font-size: 0.84rem; }}

    .step-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }}
    .step-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-top: 4px solid var(--teal);
      border-radius: 10px;
      padding: 16px;
    }}
    .step-card h3 {{ font-size: 0.96rem; color: var(--teal-deep); margin-bottom: 6px; }}
    .step-card p {{ font-size: 0.86rem; margin: 0; }}

    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 14px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-item h3 {{
      font-size: 1rem;
      color: var(--teal-deep);
      margin-bottom: 6px;
    }}
    .faq-item p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{
      font-weight: 800;
      font-size: 1.08rem;
      color: var(--teal-deep);
      margin-bottom: 14px;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 12px;
    }}
    .internal-link-card {{
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--teal); }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 44px 20px 30px;
      font-size: 0.84rem;
    }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #f8fafc; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px 14px;
      margin-bottom: 24px;
    }}
    .footer-links-grid a {{ color: #cbd5e1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #5eead4; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1e293b; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .clay-hero {{ padding: 24px 18px; }}
      .clay-hero h1 {{ font-size: 1.32rem; }}
      .clay-grid {{ grid-template-columns: 1fr; }}
      .clay-specs, .clay-notes {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="site-nav">
    <div class="site-nav-inner">
      <a href="/" class="logo-link">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/winter-face-mask">シートマスク特集</a>
        <a href="/winter-peel-serum">角質柔軟特集</a>
        <a href="/winter-bath-care">冬バスケア特集</a>
      </nav>
    </div>
  </header>

  <nav class="crumbs" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-face-mask">冬のフェイスマスク特集</a> &gt; <span>高保湿クレイマスク＆泥パック10選</span>
  </nav>

  <main>
    <section class="clay-hero">
      <span class="clay-tag">2026年11月・12月 バスタイム保湿泥ケア特集</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="clay-hero-meta">更新日：<time datetime="2026-11-22">2026年11月22日</time> ／ 編集部・成分リサーチ</div>
      <p>
        11月下旬から12月にかけて夜が一気に冷え込むと、冷蔵庫や洗面所に置いてある冷たいシートマスクを顔に貼るのが少し億劫になる日が増えてきます。しかも気温が下がった肌はターンオーバーのテンポが乱れやすく、古い角質が表面に残って化粧水がなじみにくくなったり、くすみ感や小鼻のざらつきが目立ちやすくなったりする季節でもあります。
      </p>
      <p>
        そんな冬に頼りになるのが、お風呂で湯船に浸かりながら使える<strong>「保湿型クレイマスク（洗い流す泥パック）」</strong>です。かつての「カピカピに乾いて突っ張る泥パック」とは異なり、近年はヒアルロン酸・ヒト型セラミド・植物オイル・CICAなどを抱え込んだクリーミー処方が主流。本記事では、汚れやゴワつきをすっきりオフしつつ潤いを残す実力派10品を、楽天市場の最新確認価格とともにまとめました。
      </p>
    </section>

    <nav class="toc-box" aria-label="目次">
      <h2>この記事でわかること</h2>
      <ul>
        <li><a href="#why-clay">1. なぜ冬にあえて「保湿クレイマスク」が役立つのか</a></li>
        <li><a href="#clay-types">2. 肌タイプ別・クレイの種類と選び方3パターン</a></li>
        <li><a href="#compare-table">3. 高保湿クレイマスク10選 スペック比較表</a></li>
        <li><a href="#ranking-list">4. 保湿力高めクレイマスク＆泥パックおすすめ10選</a></li>
        <li><a href="#bath-method">5. ツッパリ感をゼロにする「お風呂スチーム塗り」4ステップ</a></li>
        <li><a href="#faq">6. 冬のクレイマスク Q&amp;A</a></li>
      </ul>
    </nav>

    <section class="section-card" id="why-clay">
      <h2>1. なぜ冬に「クレイ＝乾く」イメージを覆す保湿泥パックが効くのか</h2>
      <p>
        クレイ（天然粘土鉱物）には微細な粒子にマイナスの電荷を帯びた構造を持つものが多く、酸化した古い皮脂や毛穴周りの汚れ、ゴワつきの原因となる不要な角質を物理的に絡め取ってくれる性質があります。冬は空気の乾燥と冷えで肌表面が硬くなりやすいため、いくら上から高級な美容液を重ねても「角層の入り口」が固まったままだと馴染みにくくなるのが悩ましいところです。
      </p>
      <p>
        そこで重要なのが、強いスクラブやピーリング剤でこすり落とすのではなく、<strong>保湿成分（アセチル化ヒアルロン酸・セラミド・植物油・天然ミネラルなど）を含んだ柔らかいクレイペースト</strong>で穏やかに包み込むアプローチです。入浴中の湯気の中で使えばペーストが乾き固まる前に洗い流せるため、肌の潤いを守りながらツルンと柔らかな状態へリセットできます。
      </p>
    </section>

    <section class="section-card" id="clay-types">
      <h2>2. 11月・12月の肌状態で選ぶ！保湿クレイ3つの基準</h2>
      <div class="clay-3col">
        <div class="clay-pillar">
          <h3>① 乾燥肌・大人肌には「オイル／セラミド配合クリーム系」</h3>
          <p>THREE、イプサ、クレージュのように植物オイル・ヒアルロン酸・セラミドをペーストに練り込んだタイプは、洗い流した後もしっとりした保護膜が残りやすく冬に最適です。</p>
        </div>
        <div class="clay-pillar">
          <h3>② 敏感・赤みゆらぎ肌には「CICA・緑豆・ガスール系」</h3>
          <p>beplain（緑豆）、VT（CICA）、ナイアード（ガスール100%）などは摩擦を抑えた柔らかいペーストになりやすく、寒暖差で敏感に傾いた日でも穏やかに使えます。</p>
        </div>
        <div class="clay-pillar">
          <h3>③ 小鼻・Tゾーンのざらつき対策には「火山灰・カオリン系」</h3>
          <p>キールズやイニスフリー、SKIN1004のスティック型は毛穴吸着に強く、乾燥する頬は避けてTゾーンだけ部分使いする「パーツケア」として冬場も大活躍します。</p>
        </div>
      </div>
    </section>

    <section class="section-card" id="compare-table">
      <h2>3. 高保湿クレイマスク＆洗い流す泥パック10選 比較一覧表</h2>
      <p>楽天市場の最新実勢価格（税込）とクレイ種別・洗い上がりの傾向を一覧で比較できます。</p>
      <div class="table-scroll">
        <table class="compare-tbl">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>主力クレイ × 保湿設計</th>
              <th>洗い上がりの質感</th>
              <th>参考価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{table_rows}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="ranking-sec-title" id="ranking-list">4. 保湿力高めクレイマスク＆洗い流す泥パック厳選ランキング10選</h2>
    <section aria-label="クレイマスク詳細レビュー">
{cards_html}    </section>

    <section class="section-card" id="bath-method">
      <h2>5. 冬に乾燥させない「湯船スチーム塗り」4ステップ</h2>
      <div class="step-grid">
        <div class="step-card">
          <h3>Step 1：洗顔後、水気を軽く押さえる</h3>
          <p>クレンジングや洗顔が終わったら、清潔なタオルで顔の水滴をそっと押さえます。製品によって「乾いた肌用」「濡れた肌OK」があるため事前確認を忘れずに。</p>
        </div>
        <div class="step-card">
          <h3>Step 2：厚めに塗って摩擦を防ぐ</h3>
          <p>薄く伸ばしすぎると途中で乾きやすくなります。肌の色がうっすら隠れるくらいの厚みを意識し、乾燥しやすい目の際・唇周りは1cmほど空けて塗ります。</p>
        </div>
        <div class="step-card">
          <h3>Step 3：放置は「3〜7分」が冬の目安</h3>
          <p>湯船に浸かりながらスチーム環境で置くと乾燥しません。完全にパリパリに割れるまで待たず、表面が少し落ち着いたら洗い流し始めるのがコツです。</p>
        </div>
        <div class="step-card">
          <h3>Step 4：ぬるま湯＋即座の保湿導入</h3>
          <p>熱いシャワーを直接顔に当てると乾燥の原因になるため、32〜35℃程度のぬるま湯を手ですくって優しく落とし、風呂上がりはすぐ化粧水を馴染ませます。</p>
        </div>
      </div>
    </section>

    <section class="section-card" id="faq">
      <h2>6. 冬のクレイマスク・泥パックに関するFAQ</h2>
      <div class="faq-item">
        <h3>Q1. 乾燥肌でも冬にクレイマスクを使って大丈夫ですか？</h3>
        <p>はい。ただし「放置中にカピカピに乾くさっぱり系」ではなく、ヒアルロン酸・セラミド・植物オイルを含むクリームクレイや、3〜5分で洗い流せる保湿泥パックを選び、頬が乾く日はTゾーン中心に使うのが安全です。</p>
      </div>
      <div class="faq-item">
        <h3>Q2. シートマスクとはどうやって使い分ければいいですか？</h3>
        <p>肌がゴワついて化粧水やシートマスクの美容液が入りにくいと感じる日に先にクレイマスクで不要な角質をオフし、その後に高保湿シートマスクや乳液で水分・油分を補給すると手応えが変わります。</p>
      </div>
      <div class="faq-item">
        <h3>Q3. 頻度はどのくらいが理想ですか？</h3>
        <p>11月・12月の乾燥しやすい時期は、週1〜2回が目安です。毎日使うと角層を守る必要な皮脂まで落としやすくなるため、肌のざらつきやくすみ感が気になるときのスペシャルケアに留めましょう。</p>
      </div>
      <div class="faq-item">
        <h3>Q4. 完全に乾くまで待った方が汚れは落ちますか？</h3>
        <p>乾ききるまで放置するとクレイが肌表面の水分まで吸い上げてしまい、つっぱりや赤みの原因になります。少し濡れた状態・半乾き手前で優しく洗い流す方が、冬場は潤いを保ちながらすっきり仕上がります。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の角質・マスクケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-face-mask" class="internal-link-card">
          <strong>冬のシートマスク特集</strong>
          <span>クレイ後の集中水分チャージに最適</span>
        </a>
        <a href="/winter-peel-serum" class="internal-link-card">
          <strong>角質柔軟美容液特集</strong>
          <span>ゴワつきをほぐす塗る角質ケア10選</span>
        </a>
        <a href="/winter-bath-care" class="internal-link-card">
          <strong>冬の高保湿入浴剤特集</strong>
          <span>湯船で全身しっとり温浴ケア</span>
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

with open("winter-clay-mask.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-clay-mask.html successfully!")
