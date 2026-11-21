import json
import html

with open("fetched_3new_nov_dec_2026_1122.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

items = all_data["winter_acne_moisture"]["items"]

details = [
    {
        "rank": 1,
        "form_tag": "薬用高保湿ローション（医薬部外品）",
        "display_name": "アクネケア ローション MB 125mL (医薬部外品)",
        "active_ing": "トラネキサム酸、グリチルリチン酸ジカリウム",
        "moist_base": "酵母エキス、グリセリン、キシリトール、エリスリトール（美肌菌着目）",
        "skin_fit": "乾燥・敏感寄りの大人ニキビ肌",
        "capacity": "125mL",
        "headline": "冬の乾いた頬やアゴにピリピリしみにくい。資生堂の美肌菌発想で繰り返す大人ニキビと乾燥を防ぐ",
        "body_1": "11月・12月になると、思春期の頃のようなTゾーンのベタつきではなく、Uゾーン（頬・口周り・あご先）にポツンと乾燥ニキビができやすくなります。そんな大人の冬ニキビにまず候補に挙がるのが資生堂『dプログラム アクネケア ローション MB』。抗炎症のグリチルリチン酸ジカリウムに加えて、肌荒れやニキビ予防に定評のあるトラネキサム酸をW有効成分として配合した医薬部外品です。",
        "body_2": "アルコール（エチルアルコール）無添加・無香料・パラベンフリーの低刺激処方でありながら、角層にたっぷり水分を抱え込ませる「ビューティーバイオテクノロジー」搭載成分により、塗った後はみずみずしくもっちりとした質感に。冬場、ニキビ用化粧水を使うと頬がパキパキにつっぱってしまう方にこそ試してほしい1本です。",
        "target_scene": "ニキビ用のさっぱり化粧水では冬に皮剥けしてしまう方、赤みや跡になりやすいフェイスラインのゆらぎケア",
        "apply_tip": "清潔な手のひらにディスペンサー2回押し分を取り、ニキビができやすい顎周りにもゴシゴシ擦らず押さえるように馴染ませてください。"
    },
    {
        "rank": 2,
        "form_tag": "薬用保湿液（M しっとりタイプ・医薬部外品）",
        "display_name": "クリアフル モイスチャー M しっとりタイプ 50g (医薬部外品)",
        "active_ing": "グリチルリチン酸ジカリウム",
        "moist_base": "5種の和漢植物エキス（紫根エキス・ハトムギ等）、ナノ化ビタミンC、コラーゲン",
        "skin_fit": "インナードライ・混合肌のニキビケア",
        "capacity": "50g",
        "headline": "オイルカットでありながら真冬もしっとり。和漢植物×ビタミンC誘導体×コラーゲンで毛穴と乾燥を同時に整える",
        "body_1": "オルビスのニキビケアライン『クリアフル』の保湿液には「L（さっぱり）」と「M（しっとり）」があり、暖房と冷気を行き来する11月・12月に選ぶべきは断然「M（しっとりタイプ）」です。ニキビの原因になりやすい過剰な油分を抑えたオイルカット設計のまま、コラーゲンや保水ポリマーが肌表面にうるおいのヴェールを作ってくれます。",
        "body_2": "注目したいのは、バリア機能をサポートする紫根（シコン）エキスなどの和漢成分に加え、浸透型ビタミンC誘導体やナノ化セラミド様成分を組み合わせている点。冬場の乾燥による毛穴の目立ち・ゴワつきを和らげつつ、ノンコメドジェニックテスト済みなので「乳液やクリームを塗るとすぐ詰まる」という不安を抱える方でも取り入れやすい使い心地です。",
        "target_scene": "油分の重いクリームを塗ると白ニキビができやすい混合肌の方、化粧水後の仕上げをベタつかずしっとり保ちたい方",
        "apply_tip": "1〜2プッシュを手のひらに広げ、まずは乾燥しやすい頬から先に馴染ませ、残りをTゾーン・顎へ薄く伸ばすとバランス良く仕上がります。"
    },
    {
        "rank": 3,
        "form_tag": "薬用アミノ酸乳液（医薬部外品）",
        "display_name": "アミノモイスト 薬用アクネケア ミルク 100g (医薬部外品)",
        "active_ing": "ε-アミノカプロン酸、グリチルレチン酸ステアリル",
        "moist_base": "9種の保潤アミノ酸、2種の清透アミノ酸、ヒアルロン酸",
        "skin_fit": "超乾燥肌・敏感肌でニキビもできやすい方",
        "capacity": "100g",
        "headline": "乾燥とニキビが同じ顔に混在する「冬のアンバランス肌」へ。製薬会社発想のアミノ酸ミルクで優しくバリア補整",
        "body_1": "第一三共ヘルスケアの敏感肌ライン『ミノン アミノモイスト』から展開されている「混合肌・ニキビができやすい乾燥肌」向けの薬用乳液です。冬になると「頬はカサカサで粉を吹くのに、鼻や顎にはニキビができる」というアンバランスな肌状態に陥る人が急増しますが、本品はその両方の悩みに寄り添う設計になっています。",
        "body_2": "抗炎症有効成分（ε-アミノカプロン酸とグリチルレチン酸ステアリル）が赤みや肌荒れを防ぎつつ、9種類の保潤アミノ酸が乾燥して隙間だらけになった角層をふっくら満たします。乳液ながらベタつきにくく、伸びがとても軽やか。100gで¥1,605（調査時点）という手頃な価格で続けやすいのも大きな魅力です。",
        "target_scene": "頬の乾燥とアゴの大人ニキビが同時に起きている方、ドラッグストアで買える低刺激・高保湿なニキビ向け乳液を探している方",
        "apply_tip": "化粧水で水分を入れたあと、1〜2プッシュを手に出して顔全体へ。特に乾燥する目の下や口角にはほんの少し重ね付けすると冬場も安心です。"
    },
    {
        "rank": 4,
        "form_tag": "薬用ミルク・乳液（医薬部外品）",
        "display_name": "ACアクティブ モイスチュアミルク 50mL (医薬部外品)",
        "active_ing": "サリチル酸（BHA）、グリチルリチン酸ジカリウム、ビタミンE誘導体",
        "moist_base": "ヒアルロン酸Na-2、リピジュア（メタクリロイルオキシエチルホスホリルコリン）",
        "skin_fit": "角質肥厚・毛穴詰まりを伴う大人ニキビ",
        "capacity": "50mL",
        "headline": "皮膚科領域でも信頼されるノブのACアクティブ。マイルドな角質ケアとリピジュアの濃密保水を1本で両立",
        "body_1": "常盤薬品工業の臨床皮膚医学発想ブランド『NOV（ノブ）』の中でも、大人ニキビと毛穴・保湿を積極ケアする『ACアクティブ』シリーズの薬用乳液です。冬は寒さで角質が硬く厚くなり、毛穴の出口が塞がってニキビが育ちやすくなりますが、マイルドピーリング作用に関わる有効成分サリチル酸が角層を柔らかく保ちながら、ヒアルロン酸と高保水成分リピジュアがしっかり潤いを抱えます。",
        "body_2": "さらっとした白いミルクは肌なじみが非常に早く、塗った後の表面はなめらかでベタつきがありません。それでいて内側の水分保持力が高いため、12月の乾いた室内で過ごしても頬がつっぱりにくいのが特徴。ノンコメドジェニックテスト済み・無香料・無着色で、本気でニキビサイクルを断ちたい方の夜の定番として心強い存在です。",
        "target_scene": "冬のゴワつきで毛穴が詰まり、同じ場所に何度もニキビを繰り返してしまう方、医療機関でも扱われる安心ブランドを選びたい方",
        "apply_tip": "夜のお手入れでは化粧水の後に2プッシュほど馴染ませ、頬だけカサつく場合は上から手持ちのセラミドクリームを薄く部分重ねしてください。"
    },
    {
        "rank": 5,
        "form_tag": "薬用セラミド保湿ジェル（医薬部外品）",
        "display_name": "皮脂トラブルケア 保湿ジェル 120mL (医薬部外品)",
        "active_ing": "アラントイン（消炎剤）",
        "moist_base": "セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、ユーカリエキス",
        "skin_fit": "ベタつき・皮脂過多と乾燥の混在肌",
        "capacity": "120mL",
        "headline": "「皮脂でテカるのに内側が乾く」冬のインナードライニキビに。セラミドの潤いを補いながらノンオイリーに整える",
        "body_1": "花王『キュレル』の緑色のパッケージで親しまれている「皮脂トラブルケア」シリーズの高保湿ジェル。冬の室内は湿度が極端に低いため、肌は乾燥を防ごうとしてかえって皮脂を過剰分泌し、その皮脂が酸化・詰まりを起こして大人ニキビにつながることがあります。本品はオイルフリー処方でありながら、キュレル独自の「セラミド機能成分」で角層のバリアをしっかり立て直す点が秀逸です。",
        "body_2": "水ベースのみずみずしい透明ジェルは、肌に伸ばした瞬間すっと吸い込まれて表面はサラサラ。それでいてアラントインが乾燥やマスク摩擦による荒れを防ぎ、ユーカリエキスが角層の潤いバランスを支えてくれます。120mLの大容量ポンプで¥1,627（調査時点）とコストパフォーマンスも高く、男女問わず使いやすい1本です。",
        "target_scene": "クリームを塗るとすぐ顔がテカってニキビができやすい方、メンズの冬ニキビ対策や朝のメイク前のさっぱり保湿にも",
        "apply_tip": "冬場にこれ1本だけだと頬が物足りない場合は、Tゾーンや顎はこのジェルで抑えつつ、頬骨周りだけキュレルの通常フェイスクリームを薄く塗る「部位別使い」がおすすめです。"
    },
    {
        "rank": 6,
        "form_tag": "無添加薬用化粧液（医薬部外品）",
        "display_name": "アクネケア 化粧液 30mL (医薬部外品)",
        "active_ing": "グリチルリチン酸ジカリウム",
        "moist_base": "漢植物エキス（ウメ果実エキス・シャクヤクエキス・トウニンエキス）、ラフィノース（天然オリゴ糖）",
        "skin_fit": "防腐剤・殺菌剤に敏感な大人ニキビ肌",
        "capacity": "30mL",
        "headline": "殺菌剤不使用で、ゆらぎがちな冬の肌バリアを壊さない。和漢植物と糖の保水力で角層をしっとり整える",
        "body_1": "一般的な市販のニキビケア製品には強い殺菌剤（イソプロピルメチルフェノール等）や高濃度のアルコールが含まれていることがあり、乾燥が進む11月・12月に使うと常在菌バランスが崩れてかえって肌が荒れてしまうケースがあります。ファンケルの『アクネケア 化粧液』は、殺菌剤・防腐剤・香料・合成色素を一切使わない無添加設計で、冬でも穏やかにニキビをケアできる処方です。",
        "body_2": "主役の有効成分グリチルリチン酸ジカリウムに加え、ゴワついた角層を柔軟にするウメ果実エキスやトウニンエキス、さらに水分を抱える天然オリゴ糖（ラフィノース）を配合。30mLのフレッシュボトルで少しとろみのある液が角層へすっと入り込み、ニキビができにくいすべすべとした柔肌へ導きます。",
        "target_scene": "市販のニキビ薬や化粧水でヒリつき・皮むけを起こしたことがある方、防腐剤フリーにこだわる敏感肌の方",
        "apply_tip": "1回100円玉大を清潔な手に取り、乾燥が気になる日は2回重ね付けしてから、同シリーズのジェル乳液や低刺激ミルクで蓋をしましょう。"
    },
    {
        "rank": 7,
        "form_tag": "薬用高精製ワセリンバーム（医薬部外品）",
        "display_name": "薬用クリアバーム 18g (医薬部外品)",
        "active_ing": "m-トラネキサム酸、グリチルリチン酸ジカリウム",
        "moist_base": "高精製ワセリン、ヒアルロン酸Na、ジグリセリン",
        "skin_fit": "冬の粉吹き・赤み・マフラー摩擦からの保護",
        "capacity": "18g",
        "headline": "「ワセリンはニキビに重い？」を覆すみずみずしい薬用バーム。乾燥や摩擦によるニキビ・赤み・跡の予防に",
        "body_1": "資生堂『イハダ』の薬用クリアバームは、従来の「黄色の薬用バーム」の優れた密封保護力を受け継ぎながら、美白有効成分m-トラネキサム酸と抗肌荒れ有効成分グリチルリチン酸ジカリウムを配合し、より軽やかでみずみずしい使用感に仕上げた医薬部外品です。ノンコメドジェニックテスト済みで、冬の乾燥が引き金になる大人ニキビ肌にも使いやすい処方になっています。",
        "body_2": "気温が下がる11月・12月は、マフラーやタートルネックの襟元が顎や頬に擦れてニキビが悪化しがちですが、このバームを指先で温めてごく薄く伸ばすと、肌の潤いを閉じ込めつつ外部摩擦から守るしなやかな保護膜になります。18gのスリムなジャーは持ち運びにも向き、日中の乾燥レスキューにも重宝します。",
        "target_scene": "乾燥で皮がめくれるほど荒れているのにニキビも出ている方、冬の衣類・マスク摩擦による顎周りの悪化を防ぎたい方",
        "apply_tip": "塗りすぎるとベタつくため、米粒1〜2粒分を手のひらで溶かしてから、頬や顎へスタンプのように軽く押し当てて薄い膜を作るのがコツです。"
    },
    {
        "rank": 8,
        "form_tag": "薬用バランスケア乳液（医薬部外品）",
        "display_name": "バランスケア エマルジョン 120mL (医薬部外品)",
        "active_ing": "ヘパリン類似物質HD、グリチルリチン酸ジカリウム",
        "moist_base": "クリアオイルコントロール成分（植物由来）、スクワラン、グリセリン",
        "skin_fit": "「保湿の王道ヘパリン」を使いたいニキビ・混合肌",
        "capacity": "120mL",
        "headline": "高保湿の定番『カルテHD』から生まれた水分・油分バランス特化ライン。ヘパリン類似物質HDで乾燥ニキビを防ぐ",
        "body_1": "乾燥肌の救世主として圧倒的な知名度を持つコーセーの『カルテHD』ですが、実は通常のモイスチュアシリーズより油分感を軽やかに調整し、テカリやニキビが気になりやすい肌向けに作られたのがこの緑の『バランスケア』シリーズです。保水有効成分「ヘパリン類似物質HD」と消炎の「グリチルリチン酸ジカリウム」はそのままに、皮脂バランスを整える成分を組み合わせているのが最大の特徴です。",
        "body_2": "「乾燥するから高保湿なカルテHDを使いたいけれど、頬以外がベタついてニキビができないか心配」という方にとって、まさに待ち望んでいた処方。乳液らしいまろやかなコクとみずみずしさを両立しており、冬の朝に塗ってもメイクが崩れにくく、夜までしっとり感が持続します。",
        "target_scene": "ヘパリン類似物質の保水力を取り入れたいけれど重たいクリームは避けたい方、乾燥とテカリが混在する冬肌の方",
        "apply_tip": "化粧水の後にポンプ2押し分を顔全体に。特に口元や顎に赤みが出ているときは擦らずハンドプレスで押し込むと落ち着きます。"
    },
    {
        "rank": 9,
        "form_tag": "5D複合CICAジェルクリーム（韓国スキンケア）",
        "display_name": "バランスフル シカクリーム 80mL",
        "active_ing": "5D複合CICAコンプレックス（整肌）、パンテノール、アラントイン",
        "moist_base": "ヒアルロン酸、ティーツリー葉エキス、ベタイン",
        "skin_fit": "赤み・熱感・ゆらぎやすい冬の混合ニキビ肌",
        "capacity": "80mL",
        "headline": "韓国・日本公式ストアでもレビュー高評価。5種のCICA×パンテノールで暖房の火照り赤みと水分不足を鎮静",
        "body_1": "トリデンの青い保湿ライン（ダイブイン）と並んで高い人気を誇る緑のライン『バランスフル シカクリーム』。80mLのチューブで¥1,980（調査時点）と手頃ながら、独自の低分子5D複合CICA成分に加え、角層の修復を助けるパンテノール（プロビタミンB5）と鎮静成分アラントインをしっかり配合しています。",
        "body_2": "冬の外気から急に暖かい暖房室へ入ると、顔がカーッと火照って赤みや小さな吹き出物が出やすくなりますが、この水分たっぷりのジェルクリームは乗せた瞬間に肌をひんやり落ち着かせてくれます。油分が控えめで毛穴を塞ぎにくい処方のため、朝のメイク前に塗ってもヨレにくく、重ねても重たくならない使い勝手の良さが光ります。",
        "target_scene": "暖房による火照り赤みやマスク内のムレ・ニキビに悩む方、ベタつかないチューブタイプのCICA保湿クリームを探している方",
        "apply_tip": "洗顔後の化粧水・美容液の仕上げにパール2粒分を伸ばします。真冬の極寒日に頬だけ少し物足りないときは、頬のみオイルを1滴足すと盤石です。"
    },
    {
        "rank": 10,
        "form_tag": "薬用ハトムギ×ヒアルロン酸化粧水（つめかえ・医薬部外品）",
        "display_name": "薬用 極潤 スキンコンディショナー つめかえ用 170mL (医薬部外品)",
        "active_ing": "グリチルリチン酸ジカリウム、ε-アミノカプロン酸",
        "moist_base": "ハトムギエキス（ヨクイニンエキス）、ドクダミエキス、ヒアルロン酸Na、スクワラン",
        "skin_fit": "プチプラでたっぷり使える抗炎症×高保湿ケア",
        "capacity": "170mL（つめかえ用）",
        "headline": "1,000円以下の薬用名品！Wの抗炎症有効成分＋ハトムギ＋ヒアルロン酸＆スクワランで冬の荒れ・ニキビを予防",
        "body_1": "ロート製薬のロングセラー『極潤』シリーズの中で、肌荒れとニキビ予防に特化した薬用白濁ローションが『薬用 極潤 スキンコンディショナー』。今回の楽天市場調査では詰め替え用170mLが¥924と1,000円を切る圧倒的コスパながら、Wの抗炎症有効成分（グリチルリチン酸2K＋ε-アミノカプロン酸）と、ハトムギ・ドクダミなどの和漢植物エキスを贅沢に配合しています。",
        "body_2": "一般的な「ハトムギ化粧水」は冬場に使うとさっぱりしすぎて乾きがちですが、こちらはさすが極潤ブランドだけあってヒアルロン酸Naやスクワランが組み込まれており、シャバシャバしすぎずほどよくしっとり肌に密着します。惜しみなくたっぷり使える価格帯なので、コットンパックや首・デコルテのニキビ予防にもぴったりです。",
        "target_scene": "1,000円前後でニキビ予防と保湿を両立したい学生〜大人世代、顔だけでなく背中やデコルテの冬の乾燥吹き出物ケアにも",
        "apply_tip": "詰め替え用のため本体ボトルや清潔な化粧水容器に移して使用してください。肌が火照りやすい顎周りに3分ほどのローションパックをするのも快適です。"
    }
]

article_title = "冬の乾燥大人ニキビを乾かさず鎮静！高保湿×ノンコメドジェニック薬用スキンケアおすすめランク10【11月・12月】"
article_desc = "11月・12月の暖房乾燥やマスク・マフラー摩擦で増える大人の乾燥ニキビ対策！dプログラム、オルビス クリアフル、ミノン、ノブ ACアクティブ、キュレル、ファンケル、イハダ、カルテHDバランスケア、トリデン、極潤スキンコンディショナーまで高保湿ニキビケア10選を徹底比較。"
canonical_url = "https://lumi-cosme.vercel.app/winter-acne-moisture"

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
            "name": "11月・12月向け冬の乾燥大人ニキビ高保湿スキンケア10選",
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
                    "name": "冬になると頬や顎に大人ニキビが増えるのはなぜですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "11月・12月は外気の乾燥とエアコン暖房によって角層の水分が奪われ（インナードライ）、肌を守ろうとして皮脂分泌が乱れたり、角質が厚く硬くなって毛穴の出口が詰まりやすくなったりします。さらにマフラーやタートルネックの摩擦、年末の睡眠不足も重なり、顎やフェイスラインに乾燥ニキビができやすくなります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ニキビがあるとき、クリームや乳液による保湿は控えた方が良いですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "冬の乾燥ニキビの場合、保湿を控えて洗顔後に化粧水だけで済ませると乾燥がいっそう悪化し、かえって皮脂過剰や炎症が長引くことがあります。コッテリした油分の多いクリームではなく、『ノンコメドジェニック（ニキビのもとになりにくい処方）』や『オイルコントロール系・セラミドジェル・薬用乳液』で適切に水分とバリアを補うことが大切です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "「ノンコメドジェニックテスト済み」とはどういう意味ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ニキビの初期段階であるコメド（面皰）ができにくいかどうかを確認する試験を実施した製品であることを指します（※すべての方にニキビができないわけではありません）。冬場にしっかり保湿をしたいけれど油分で毛穴が詰まらないか不安な場合の有力な目安になります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "すでに赤く腫れたり痛んだりするニキビがある場合の注意点は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "スキンケア化粧品（医薬部外品含む）はあくまで『ニキビ予防』や『肌の保湿・整肌』が役割です。強く腫れて痛むニキビや長引く炎症がある場合は、セルフケアで無理に潰したりせず皮膚科を受診し、処方薬と低刺激の保湿ケアを併用することをおすすめします。"
                    }
                }
            ]
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "ホーム", "item": "https://lumi-cosme.vercel.app/"},
                {"@type": "ListItem", "position": 2, "name": "冬の高保湿化粧水特集", "item": "https://lumi-cosme.vercel.app/winter-lotion"},
                {"@type": "ListItem", "position": 3, "name": "冬の乾燥大人ニキビ高保湿ケア10選", "item": canonical_url}
            ]
        }
    ]
}

rows_html = ""
for it, det in zip(items, details):
    rows_html += f"""            <tr>
              <td class="a-rank">第{it['rank']}位</td>
              <td><strong>{html.escape(it['brand'])}</strong><br><span class="a-sub">{html.escape(det['display_name'])}</span></td>
              <td>{html.escape(det['form_tag'])}</td>
              <td>{html.escape(det['active_ing'])}</td>
              <td>{html.escape(det['skin_fit'])}</td>
              <td class="a-price">¥{it['price']:,}<br><span class="a-sub">{html.escape(det['capacity'])}</span></td>
            </tr>
"""

cards_html = ""
for it, det in zip(items, details):
    rate_badge = (
        f'<span class="acne-rate">★ {it["review_average"]} ({it["review_count"]:,}件)</span>'
        if int(it.get("review_count", 0)) > 0 and float(it.get("review_average", 0)) > 0
        else '<span class="acne-rate">楽天市場 在庫確認済</span>'
    )
    cards_html += f"""
      <article class="acne-card" id="rank-{it['rank']}">
        <div class="acne-top">
          <div class="acne-badges">
            <span class="acne-rank">第{it['rank']}位</span>
            <span class="acne-form">{html.escape(det['form_tag'])}</span>
            {rate_badge}
          </div>
          <h3>{html.escape(it['brand'])} {html.escape(det['display_name'])}</h3>
          <div class="acne-hook">{html.escape(det['headline'])}</div>
        </div>

        <div class="acne-layout">
          <div class="acne-left">
            <div class="acne-img-wrap">
              <img src="{html.escape(it['image_url'])}" alt="{html.escape(it['brand'])} {html.escape(det['display_name'])}" class="product-img" loading="lazy">
            </div>
            <div class="acne-price-card">
              <span class="p-cap">楽天市場 最新確認価格（税込）</span>
              <span class="p-num">¥{it['price']:,}</span>
            </div>
            <a href="{html.escape(it['affiliate_url'])}" target="_blank" rel="noopener noreferrer nofollow sponsored" class="rakuten-btn">
              楽天市場で詳細・口コミを見る →
            </a>
            <p class="acne-sku">掲載：{html.escape(it['item_name'][:52])}</p>
          </div>

          <div class="acne-right">
            <dl class="acne-dl">
              <div><dt>主な有効・整肌成分</dt><dd>{html.escape(det['active_ing'])}</dd></div>
              <div><dt>保湿サポート基材</dt><dd>{html.escape(det['moist_base'])}</dd></div>
              <div><dt>向いている肌質</dt><dd>{html.escape(det['skin_fit'])}</dd></div>
              <div><dt>内容量</dt><dd>{html.escape(det['capacity'])}</dd></div>
            </dl>

            <div class="acne-text">
              <p>{html.escape(det['body_1'])}</p>
              <p>{html.escape(det['body_2'])}</p>
            </div>

            <div class="acne-advice-grid">
              <div class="advice-box">
                <strong>このアイテムが合う悩み</strong>
                <p>{html.escape(det['target_scene'])}</p>
              </div>
              <div class="advice-box">
                <strong>刺激を減らす冬の上手な塗り方</strong>
                <p>{html.escape(det['apply_tip'])}</p>
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
  <meta name="keywords" content="大人ニキビ 乾燥 冬 スキンケア, ノンコメドジェニック 高保湿, 11月 12月 ニキビケア 化粧水 乳液, dプログラム アクネケア, オルビス クリアフル, カルテHD バランスケア, ミノン 薬用アクネケア">
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
      --cyan: #0e7490;
      --cyan-dark: #164e63;
      --cyan-soft: #ecfeff;
      --cyan-border: #a5f3fc;
      --bg: #f8fafc;
      --ink: #0f172a;
      --muted: #475569;
      --line: #e2e8f0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.78;
    }}
    header.nav-bar {{
      background: #fff;
      border-bottom: 1px solid var(--line);
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .nav-bar-inner {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 13px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
    }}
    .brand-txt {{ font-weight: 800; font-size: 1.12rem; color: var(--cyan-dark); text-decoration: none; }}
    .nav-menu {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; }}
    .nav-menu a {{ color: var(--cyan); font-weight: 700; text-decoration: none; }}
    .bread {{ max-width: 1080px; margin: 14px auto 0; padding: 0 20px; font-size: 0.82rem; color: var(--muted); }}
    .bread a {{ color: var(--cyan); text-decoration: none; }}
    main {{ max-width: 1080px; margin: 20px auto 64px; padding: 0 20px; }}

    .acne-hero {{
      background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
      border: 1px solid var(--cyan-border);
      border-radius: 16px;
      padding: 34px 28px;
      margin-bottom: 24px;
    }}
    .hero-badge {{
      display: inline-block;
      background: var(--cyan);
      color: #fff;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }}
    .acne-hero h1 {{
      font-size: 1.7rem;
      line-height: 1.42;
      color: var(--cyan-dark);
      margin-bottom: 12px;
    }}
    .hero-date {{ font-size: 0.84rem; color: var(--muted); margin-bottom: 14px; }}
    .acne-hero p {{ font-size: 0.96rem; margin-bottom: 10px; }}

    .ng-ok-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 16px;
      margin-bottom: 26px;
    }}
    .ng-box, .ok-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 18px 20px;
    }}
    .ng-box {{ border-top: 4px solid #dc2626; }}
    .ok-box {{ border-top: 4px solid var(--cyan); }}
    .ng-box h2, .ok-box h2 {{ font-size: 1rem; margin-bottom: 8px; }}
    .ng-box h2 {{ color: #991b1b; }}
    .ok-box h2 {{ color: var(--cyan-dark); }}
    .ng-box ul, .ok-box ul {{ padding-left: 18px; font-size: 0.88rem; }}
    .ng-box li, .ok-box li {{ margin-bottom: 4px; }}

    .toc-panel {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 20px 24px;
      margin-bottom: 28px;
    }}
    .toc-panel h2 {{ font-size: 1.05rem; color: var(--cyan-dark); margin-bottom: 10px; }}
    .toc-panel ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 6px 18px;
    }}
    .toc-panel a {{ color: var(--cyan); text-decoration: none; font-size: 0.92rem; font-weight: 600; }}

    .block-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 28px;
      margin-bottom: 28px;
    }}
    .block-box h2 {{
      font-size: 1.32rem;
      color: var(--cyan-dark);
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--cyan-soft);
    }}
    .block-box p {{ font-size: 0.95rem; margin-bottom: 12px; }}

    .axis-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .axis-card {{
      background: var(--cyan-soft);
      border: 1px solid var(--cyan-border);
      border-radius: 12px;
      padding: 18px;
    }}
    .axis-card h3 {{ font-size: 1rem; color: var(--cyan-dark); margin-bottom: 8px; }}
    .axis-card p {{ font-size: 0.88rem; margin: 0; }}

    .tbl-wrap {{ overflow-x: auto; margin-top: 14px; }}
    .spec-tbl {{ width: 100%; border-collapse: collapse; min-width: 740px; font-size: 0.87rem; }}
    .spec-tbl th {{ background: var(--cyan-dark); color: #fff; text-align: left; padding: 11px 12px; }}
    .spec-tbl td {{ padding: 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
    .spec-tbl tr:nth-child(even) td {{ background: #f8fafc; }}
    .a-rank {{ font-weight: 800; color: var(--cyan); white-space: nowrap; }}
    .a-price {{ font-weight: 700; color: var(--cyan-dark); white-space: nowrap; }}
    .a-sub {{ font-size: 0.78rem; color: var(--muted); font-weight: 400; }}

    .rank-h2 {{
      font-size: 1.4rem;
      color: var(--cyan-dark);
      margin: 34px 0 18px;
      padding-left: 12px;
      border-left: 5px solid var(--cyan);
    }}
    .acne-card {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 26px;
      margin-bottom: 24px;
      box-shadow: 0 2px 10px rgba(14, 116, 144, 0.05);
    }}
    .acne-top {{ margin-bottom: 18px; }}
    .acne-badges {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 10px; }}
    .acne-rank {{
      background: var(--cyan-dark);
      color: #fff;
      font-weight: 800;
      font-size: 0.82rem;
      padding: 4px 12px;
      border-radius: 6px;
    }}
    .acne-form {{
      background: var(--cyan-soft);
      color: var(--cyan);
      border: 1px solid var(--cyan-border);
      font-size: 0.78rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .acne-rate {{
      background: #fef3c7;
      color: #b45309;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 999px;
    }}
    .acne-top h3 {{ font-size: 1.24rem; margin-bottom: 6px; }}
    .acne-hook {{ font-size: 0.92rem; color: var(--cyan); font-weight: 700; }}

    .acne-layout {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      align-items: start;
    }}
    .acne-img-wrap {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
    }}
    .product-img {{ max-width: 100%; height: 210px; object-fit: contain; }}
    .acne-price-card {{
      background: var(--cyan-soft);
      border-radius: 10px;
      padding: 10px 12px;
      text-align: center;
      margin-bottom: 10px;
    }}
    .p-cap {{ display: block; font-size: 0.74rem; color: var(--muted); }}
    .p-num {{ font-size: 1.35rem; font-weight: 800; color: var(--cyan-dark); }}
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
    .acne-sku {{ margin-top: 8px; font-size: 0.72rem; color: var(--muted); line-height: 1.4; word-break: break-all; }}

    .acne-dl {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
      background: #f8fafc;
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px 14px;
      margin-bottom: 14px;
      font-size: 0.84rem;
    }}
    .acne-dl dt {{ font-size: 0.74rem; color: var(--muted); }}
    .acne-dl dd {{ font-weight: 700; margin: 0; }}
    .acne-text p {{ font-size: 0.94rem; margin-bottom: 10px; }}
    .acne-advice-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-top: 12px;
    }}
    .advice-box {{
      background: var(--cyan-soft);
      border: 1px solid var(--cyan-border);
      border-radius: 10px;
      padding: 12px 14px;
      font-size: 0.84rem;
    }}
    .advice-box strong {{ display: block; color: var(--cyan-dark); margin-bottom: 4px; }}
    .advice-box p {{ margin: 0; }}

    .zone-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-top: 14px;
    }}
    .zone-card {{
      background: #f8fafc;
      border: 1px solid var(--line);
      border-left: 4px solid var(--cyan);
      border-radius: 10px;
      padding: 16px;
    }}
    .zone-card h3 {{ font-size: 0.98rem; color: var(--cyan-dark); margin-bottom: 6px; }}
    .zone-card p {{ font-size: 0.87rem; margin: 0; }}

    .faq-row {{ border-bottom: 1px solid var(--line); padding: 14px 0; }}
    .faq-row:last-child {{ border-bottom: none; }}
    .faq-row h3 {{ font-size: 1rem; color: var(--cyan-dark); margin-bottom: 6px; }}
    .faq-row p {{ font-size: 0.92rem; margin: 0; }}

    .internal-links-box {{
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 24px;
      margin-top: 32px;
    }}
    .internal-links-title {{ font-weight: 800; font-size: 1.08rem; color: var(--cyan-dark); margin-bottom: 14px; }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 12px;
    }}
    .internal-link-card {{
      border: 1px solid var(--line);
      border-radius: 10px;
      padding: 12px;
      text-decoration: none;
      display: block;
    }}
    .internal-link-card:hover {{ border-color: var(--cyan); }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 44px 20px 30px;
      font-size: 0.84rem;
    }}
    .footer-inner {{ max-width: 1080px; margin: 0 auto; }}
    .footer-title {{ color: #f8fafc; font-weight: 800; margin-bottom: 14px; }}
    .footer-links-grid {{ display: flex; flex-wrap: wrap; gap: 8px 14px; margin-bottom: 24px; }}
    .footer-links-grid a {{ color: #cbd5e1; text-decoration: none; font-size: 0.8rem; }}
    .footer-links-grid a:hover {{ color: #67e8f9; text-decoration: underline; }}
    .copyright {{ border-top: 1px solid #1e293b; padding-top: 18px; text-align: center; font-size: 0.78rem; }}

    @media (max-width: 760px) {{
      .acne-hero {{ padding: 24px 18px; }}
      .acne-hero h1 {{ font-size: 1.32rem; }}
      .acne-layout, .acne-dl, .acne-advice-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header class="nav-bar">
    <div class="nav-bar-inner">
      <a href="/" class="brand-txt">Lumi Cosme</a>
      <nav class="nav-menu">
        <a href="/winter-lotion">化粧水特集</a>
        <a href="/winter-moisture-cream">クリーム特集</a>
        <a href="/winter-cica-cream">シカクリーム特集</a>
      </nav>
    </div>
  </header>

  <nav class="bread" aria-label="パンくずリスト">
    <a href="/">ホーム</a> &gt; <a href="/winter-lotion">冬の高保湿化粧水特集</a> &gt; <span>冬の乾燥大人ニキビ高保湿ケア10選</span>
  </nav>

  <main>
    <section class="acne-hero">
      <span class="hero-badge">2026年11月・12月 乾燥ゆらぎ＆大人ニキビ対策</span>
      <h1>{html.escape(article_title)}</h1>
      <div class="hero-date">更新日：<time datetime="2026-11-22">2026年11月22日</time> ／ 監修・データ調査：Lumi Cosme 編集部</div>
      <p>
        夏場は気にならなかったのに、11月・12月に入ってエアコン暖房をつけ始めた頃から「頬は粉を吹くほど乾いているのに、なぜかアゴや口周りにポツポツと大人ニキビができる」という経験はありませんか。冬のニキビは、皮脂の多さだけでなく<strong>「角層の水分不足（インナードライ）＋硬化した角質の毛穴詰まり＋マフラーやマスクの摩擦」</strong>が重なって起きるケースが非常に多いのが特徴です。
      </p>
      <p>
        ここに殺菌剤やアルコールが強めの思春期向けさっぱり化粧水を当ててしまうと、肌はさらに乾いて防御反応から皮脂を出しやすくなります。本記事では、ノンコメドジェニック発想や抗炎症有効成分（グリチルリチン酸ジカリウム等）を備えつつ、<strong>冬でもつっぱらず角層をしっかり潤せる高保湿ニキビケア10選</strong>を楽天の最新価格とあわせて厳選しました。
      </p>
    </section>

    <div class="ng-ok-grid">
      <div class="ng-box">
        <h2>冬ニキビを悪化させやすいNG習慣</h2>
        <ul>
          <li>「油分が怖いから」と化粧水だけで乳液・ジェルを省く</li>
          <li>清涼感の強いアルコール入り・脱脂力の高い洗顔を使い続ける</li>
          <li>毛先やウール製マフラー・マスクの縁がアゴ周りに直接擦れ続ける</li>
        </ul>
      </div>
      <div class="ok-box">
        <h2>11月・12月の正解アプローチ</h2>
        <ul>
          <li>抗炎症有効成分＋低刺激保湿（セラミド・アミノ酸・ヘパリン等）を選ぶ</li>
          <li>オイル控えめ・ノンコメドジェニック処方の乳液や保湿ジェルで蓋をする</li>
          <li>頬（乾燥ゾーン）とTゾーン・顎（ニキビゾーン）で塗布量に差をつける</li>
        </ul>
      </div>
    </div>

    <nav class="toc-panel" aria-label="目次">
      <h2>この記事のメニュー</h2>
      <ul>
        <li><a href="#winter-acne-why">1. 11月・12月に「乾燥大人ニキビ」が急増する背景</a></li>
        <li><a href="#select-axes">2. 失敗しない冬ニキビ用高保湿コスメの選び方3軸</a></li>
        <li><a href="#compare-spec">3. 高保湿ニキビケア10選 スペック早見表</a></li>
        <li><a href="#ranking-top10">4. おすすめランキング10選（成分・使用感レビュー）</a></li>
        <li><a href="#zone-care">5. 冬の「乾燥頬×ニキビ顎」塗り分け＆摩擦対策</a></li>
        <li><a href="#faq">6. 冬の乾燥ニキビケア FAQ</a></li>
      </ul>
    </nav>

    <section class="block-box" id="winter-acne-why">
      <h2>1. なぜ冬に「乾燥しているのにニキビができる」矛盾が起きるのか？</h2>
      <p>
        11月から12月にかけて外気の湿度が下がり、室内では暖房がフル稼働すると、肌の角層水分量は急激に低下します。水分を失ってしなやかさをなくした角層は、毛穴の出口付近で硬く厚くなり（角質肥厚）、普段なら自然に排出されるわずかな皮脂さえも出口で引っかかりやすくなります。これが冬特有の白ニキビ・ポツポツ詰まりの正体です。
      </p>
      <p>
        さらに年末に向けて仕事や行事の繁忙期に入り、睡眠リズムの乱れや冷えによる血行低下、タートルネックやマフラーのチクチクした物理摩擦がフェイスラインに集中することで、同じ顎周りに繰り返し炎症が起きやすくなります。だからこそ冬場は<strong>「皮脂を削ぎ落とす」のではなく「角層を水分でふっくら柔らかく保ち、炎症を鎮める」ケア</strong>への切り替えが欠かせません。
      </p>
    </section>

    <section class="block-box" id="select-axes">
      <h2>2. 失敗しない！冬ニキビ向け高保湿コスメの選び方3つの軸</h2>
      <div class="axis-3">
        <div class="axis-card">
          <h3>軸1：医薬部外品の抗炎症成分</h3>
          <p>グリチルリチン酸ジカリウム、トラネキサム酸、アラントイン、ε-アミノカプロン酸などの抗炎症有効成分が入っていると、乾燥や摩擦による赤み・荒れを穏やかに防ぎやすくなります。</p>
        </div>
        <div class="axis-card">
          <h3>軸2：毛穴を塞ぎにくい保湿基材</h3>
          <p>ワセリンや重たい油脂をベタッと塗るより、セラミド機能成分、アミノ酸、ヘパリン類似物質、CICA、ヒアルロン酸など「抱水性が高く油分バランスが整った処方」が安心です。</p>
        </div>
        <div class="axis-card">
          <h3>軸3：ノンコメドジェニック＆低アルコール</h3>
          <p>「ノンコメドジェニックテスト済み」はニキビの元ができにくい設計の目安。さらにエタノール無添加（アルコールフリー）なら冬の敏感に傾いた頬にもしみにくくなります。</p>
        </div>
      </div>
    </section>

    <section class="block-box" id="compare-spec">
      <h2>3. 冬の乾燥大人ニキビ対策 高保湿スキンケア10選 一覧表</h2>
      <p>楽天市場の最新確認価格と、処方カテゴリー・主力成分・向いている肌質を比較しました。</p>
      <div class="tbl-wrap">
        <table class="spec-tbl">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド / 商品名</th>
              <th>タイプ</th>
              <th>主力有効・整肌成分</th>
              <th>適した肌タイプ</th>
              <th>参考価格 / 容量</th>
            </tr>
          </thead>
          <tbody>
{rows_html}          </tbody>
        </table>
      </div>
    </section>

    <h2 class="rank-h2" id="ranking-top10">4. 冬の乾燥大人ニキビ向け高保湿スキンケアおすすめ10選</h2>
    <section aria-label="ランキング詳細レビュー">
{cards_html}    </section>

    <section class="block-box" id="zone-care">
      <h2>5. 真冬の「乾燥頬×ニキビ顎」を両立させる実践ルール</h2>
      <div class="zone-grid">
        <div class="zone-card">
          <h3>① 顔全体を同じ厚さで塗らない</h3>
          <p>頬や目元はしっかり保湿し、すでにプツッとニキビが出ている顎や小鼻は乳液・バームを薄めに。パーツごとに塗布量を変えるだけで詰まりとカサつきの両方を回避できます。</p>
        </div>
        <div class="zone-card">
          <h3>② 襟元・マフラーのチクチク対策</h3>
          <p>ウールや化学繊維のマフラーが顎に当たるとニキビが悪化しがちです。首元に1枚コットンやシルクのインナー・スカーフを挟むか、イハダのような薄い保護バームを顎先に仕込むと摩擦が減ります。</p>
        </div>
        <div class="zone-card">
          <h3>③ 夜の洗顔は32〜34℃のぬるま湯で</h3>
          <p>冬の寒い浴室で熱いシャワー（40℃前後）を顔に当てると皮脂膜が一瞬で流出し、乾燥ニキビの悪循環を招きます。必ず手ですくったぬるま湯で優しくすすぎましょう。</p>
        </div>
      </div>
    </section>

    <section class="block-box" id="faq">
      <h2>6. 冬の乾燥ニキビケアに関するよくある質問</h2>
      <div class="faq-row">
        <h3>Q1. 冬になると顎や口周りにばかりニキビができるのはなぜですか？</h3>
        <p>暖房による水分蒸発（インナードライ）で角層が硬くなって毛穴が詰まりやすくなることに加え、マフラーやタートルネックの擦れ、冬の血行低下や年末の生活リズムの乱れがフェイスラインに出やすいためです。</p>
      </div>
      <div class="faq-row">
        <h3>Q2. ニキビがある日でも乳液や保湿ジェルを塗った方が良いですか？</h3>
        <p>はい。冬場に化粧水だけで終わらせると数分で水分が逃げて乾燥が悪化し、肌が防衛反応で余計に皮脂を出してしまいます。ノンコメドジェニック設計やオイル控えめの薬用乳液・ジェルで適切に蓋をすることが重要です。</p>
      </div>
      <div class="faq-row">
        <h3>Q3. 「ノンコメドジェニックテスト済み」なら絶対ニキビはできませんか？</h3>
        <p>「コメド（ニキビの初期段階）ができにくい処方」を確認した試験ですが、すべての方にニキビができないわけではありません。それでも通常の重たい油分クリームに比べると、冬ニキビ肌の方が試しやすい有力な基準になります。</p>
      </div>
      <div class="faq-row">
        <h3>Q4. 赤く腫れて痛むニキビが治らないときはどうすればよいですか？</h3>
        <p>スキンケア化粧品（医薬部外品を含む）は予防・保湿・肌環境を整える役割が中心です。強く腫れて痛むニキビや長引く炎症がある場合は、セルフケアで触りすぎず皮膚科を受診して適切な外用薬と保湿の併用を相談してください。</p>
      </div>
    </section>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬のゆらぎ・毛穴・低刺激ケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <a href="/winter-lotion" class="internal-link-card">
          <strong>冬の高保湿化粧水特集</strong>
          <span>インナードライを潤す名品ローション10選</span>
        </a>
        <a href="/winter-cica-cream" class="internal-link-card">
          <strong>冬の高保湿シカクリーム特集</strong>
          <span>寒暖差赤み・ゆらぎを鎮静するCICAクリーム</span>
        </a>
        <a href="/winter-azelaic-acid" class="internal-link-card">
          <strong>高濃度アゼライン酸コスメ特集</strong>
          <span>皮脂バランスと角質・毛穴を整える話題成分</span>
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

with open("winter-acne-moisture.html", "w", encoding="utf-8") as f:
    f.write(html_doc)

print("Generated winter-acne-moisture.html successfully!")
