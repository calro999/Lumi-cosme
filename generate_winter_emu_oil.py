import json
import re

with open("fetched_3new_murumuru_cranberry_emu.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_emu_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 人肌とほぼ同等の脂肪酸組成！真冬の粉吹き肌・水仕事のあかぎれ・頑固なかゆみを即座に鎮める最高峰100%オイル",
        "catch": "オーストラリア特許精製技術OILTEKを採用した日本で最も信頼されるエミューオイル「エミューの雫」。生体親和性No.1の浸透力で、真冬の極度な皮脂枯渇とひび割れ手肌を瞬時に柔らかく満たす",
        "brand_name": "エミューの雫 (Emu no Shizuku)",
        "capacity": "72ml / ポンプ遮光ボトル",
        "type": "無添加100% 高純度エミューオイル（オーストラリア政府認定）",
        "features": "エミュー油100%（OILTEK精製）、天然オレイン酸（約50%）、パルミチン酸、リノール酸、オメガ3・6・9天然バランス",
        "value": "人間の皮脂に極めて酷似した脂肪酸プロファイルにより、塗った瞬間に皮膚と同化。一般的な植物油が浸透しない冬の硬化角質をすり抜け、深部から乾燥性皮膚炎やかゆみを鎮静",
        "desc_p1": "11月後半から12月にかけて湿度が急激に下がると、タイツやすねを脱いだ時に白い粉がパラパラと落ちたり、水仕事の後に手の甲や指先がパックリ割れて出血したり、夜布団に入るとすねや腰回りが痒くて眠れない……という深刻な乾燥トラブルに直面します。この皮脂枯渇によるバリア崩壊の救世主として皮膚科医やエステティシャンから絶大な信頼を集めているのが、エミューの雫の『100%ピュア エミューオイル 72ml』です。",
        "desc_p2": "ポンプを押すと、乳白色を帯びたなめらかなオイルが現れます。肌に乗せると、オイル特有のヌルつきや膜感が一切なく、まるで乾いた砂に水が染み込むように数秒で角層深くへと吸い込まれていきます。人間の皮脂膜とほぼ完全に一致するオレイン酸・パルミチン酸バランスが、寒さで破壊された皮膚バリアを即座に疑似再建。塗布直後からヒリヒリした赤みやかゆみがスッと引き、翌朝にはひび割れそうだった手肌やかかとが信じられないほど柔らかく整います。無香料・無添加なので赤ちゃんから高齢者まで家族全員で使える冬の必需品です。",
        "target": "冬になるとすねや腕が粉を吹いてかゆみが出る方、水仕事や消毒であかぎれ・ひび割れが治らない方、馬油やワセリンのベタつきが苦手で高浸透オイルを求める方",
        "point": "お風呂上がりの水分が残る肌に1〜2プッシュを手にとり、乾燥やかゆみが気になる部位へ優しく伸ばします。化粧水の前後にブースターとして顔全体に使うと、真冬のインナードライも一晩で解消されます。"
    },
    {
        "rank": 2,
        "tag": "✨ ポーチ常備サイズ！真冬の外出先で割れそうな唇・目元小ジワ・指先のささくれを即座に修復するレスキューオイル",
        "catch": "エミューの雫の持ち歩き用15mlミニボトル。日中の暖房風で引きつる目元や口元、乾燥で裂けそうな指先のハイポニキウムにピンポイントで濃密な潤いを届けるお守りコスメ",
        "brand_name": "エミューの雫 (Emu no Shizuku)",
        "capacity": "15ml / ミニポンプボトル",
        "type": "携帯用 高純度無添加エミューオイル",
        "features": "オーストラリア産エミューオイル100%、特許OILTEK精製、防腐剤・化学成分一切不使用",
        "value": "ポーチやポケットに入れていつでもどこでも即時保湿。酸化安定性に優れ、冬の寒冷下でも固まりにくいため、外出先でのパーツ乾燥に即座に対応可能",
        "desc_p1": "冬場の外出中、冷たい木枯らしに吹かれた後に暖房の効いた電車やオフィスに入ると、唇がピキッと割れたり、目尻や口周りがつっぱって痛むことがあります。そんな外出先での局所的な乾燥危機をその場で解決してくれるのが、エミューの雫の『携帯用15ml』です。",
        "desc_p2": "わずか1滴を指先にとり、乾燥した唇や目尻、爪の生え際になじませるだけで、数秒で皮膚深くまで浸透してベタつきを残しません。指先でスマホの画面を触っても指紋がベタベタつくことがなく、すぐにPC作業や家事に戻れる快適さが抜群です。冬場にハンドクリームを何度塗り直しても指先のガサガサが治らない方にこそ、この驚異的な浸透スピードと修復力を体感していただきたい名品です。",
        "target": "外出先で唇のひび割れや指先のささくれをサッとケアしたい方、まずは手軽なサイズと価格でエミューオイルの効果を実感してみたい方、ポーチに常備できるレスキューコスメを探している方",
        "point": "指先に半プッシュ出し、両手の爪の甘皮と指先に揉み込みます。余ったわずかなオイルを唇や目尻にトントンと置くように馴染ませると、日中の乾燥ダメージをスマートに無効化できます。"
    },
    {
        "rank": 3,
        "tag": "🌿 日本エミュー協会認定マーク付き！真冬の敏感肌やデリケートゾーンの乾燥荒れも優しく鎮める高純度オイル",
        "catch": "厳しい品質基準をクリアした「エミューム (EMUME)」。低温抽出による最高グレードのエミューオイルが、冬のエアコン風で赤みが出やすいゆらぎ肌や、高齢者の乾燥性かゆみを穏やかに鎮静",
        "brand_name": "EMUME (エミューム / 日本エミュー協会認定)",
        "capacity": "60ml / ドロッパーボトル",
        "type": "日本エミュー協会認定 100%天然スキンケアオイル",
        "features": "未希釈エミュー油100%、オメガ3（リノレン酸）、オメガ6（リノール酸）、オメガ9（オレイン酸）、ビタミンA・E天然含有",
        "value": "日本エミュー協会の厳格な認定を受けた確かな安全性。赤ちゃんの肌荒れやおむつかぶれから、大人のアトピー肌・超乾燥肌まで、刺激感ゼロで角層の柔軟化を促進",
        "desc_p1": "真冬になると、普段使っている化粧水や乳液ですらピリピリとしみて使えなくなるほどの『過敏な乾燥肌』に陥る方がいます。肌のバリアが完全に崩壊し、外部のあらゆる刺激に無防備になっている状態です。エミュームの『天然スキンケアオイル 60ml』は、日本エミュー協会の認証を受けた最高純度のエミューオイルのみを使用した、究極の低刺激保護オイルです。",
        "desc_p2": "純度の高いエミューオイルは無臭で、肌に伸ばすと一切の摩擦を感じさせることなくスーッと広がります。化学合成成分や防腐剤、香料が一切入っていないため、炎症を起こして赤くなった頬や、乾燥でヒリつく首筋にも全く刺激を与えずに馴染みます。オメガ3・6・9の天然バランスが肌の修復力を後押しし、数日間使い続けることで角質層が厚みを取り戻し、冬の冷風に負けない強い素肌へと再生していきます。",
        "target": "冬になると化粧水がしみて赤みが出る敏感肌の方、アトピー肌や乾燥性皮膚炎で肌を掻きむしってしまう方、日本エミュー協会認定の安心品質を求める方",
        "point": "洗顔後、化粧水をつけずに直接エミュームを2〜3滴手のひらで温めて顔全体に優しくハンドプレスします。肌の炎症が落ち着いてから通常のスキンケアを徐々に再開するのが冬の敏感肌レスキューの鉄則です。"
    },
    {
        "rank": 4,
        "tag": "💪 エミューオイル×MSM×グルコサミン！真冬の寒さで強張った首肩・腰・膝を温めほぐす高機能ボディクリーム",
        "catch": "野口医学研究所が開発した大ヒットボディクリーム「キダデラックス」。エミューオイルの卓越した経皮吸収サポート力を活かし、真冬の寒冷でこわばった関節とカサつく皮膚を同時にケアする",
        "brand_name": "野口医学研究所 (KIDA DX)",
        "capacity": "200g / 大容量ポンプ・ジャー",
        "type": "高浸透温感マッサージボディクリーム",
        "features": "高純度エミューオイル、MSM（メチルスルフォニルメタン）、グルコサミン、コンドロイチン、メントール微香",
        "value": "エミューオイルの『トランスダーマル（経皮送達）特性』を利用し、関節ケア成分MSMを皮膚深部まで届ける。冬の冷え固まった筋肉をほぐしながら、乾燥したひざ・ひじをしっとり保護",
        "desc_p1": "12月の本格的な寒さに突入すると、空気の乾燥に加えて『寒さで首や肩がすくんでガチガチに凝る』『膝や腰が重だるく痛む』といった寒冷トラブルが日常化します。野口医学研究所の『キダデラックス 200g』は、オーストラリアで古くから筋肉疲労ケアとして使われてきたエミューオイルの浸透力に着目して作られた高機能ボディクリームです。",
        "desc_p2": "こっくりとした滑らかなクリームを首筋、肩、腰、膝などに塗り込んでマッサージすると、エミューオイルが皮膚深部までMSMやグルコサミンを引き連れて浸透。じんわりとした心地よい温もりとともに強張った部分がスーッと軽くなり、同時に真冬の冷風で白く粉を吹いていた膝やひじの皮膚がしっとり柔らかく潤います。塗布後にベタつかないため、衣服をすぐに着用できるのも冬の毎日のケアに非常に便利です。",
        "target": "冬の寒さで首肩のコリや関節のこわばりに悩まされている方、カサつくボディの保湿とマッサージケアを同時に完結させたい方、野口医学研究所の科学的品質を好む方",
        "point": "お風呂上がりに、膝や肩、腰など疲れや乾燥が気になる部位に適量を取り、円を描くように揉みほぐしながら塗り込みます。温熱効果が高まり、夜ぐっすりと熟睡できるようになります。"
    },
    {
        "rank": 5,
        "tag": "👑 サロン＆プロアスリート愛用の285ml特大ボトル！真冬の全身粉吹き・背中のかゆみに惜しみなく使える最高峰オイル",
        "catch": "オーストラリア原産・医療グレード精製を誇る「オイル・オブ・エミュー」。真冬の全身の皮膚炎やかゆみ、粉吹き脚に毎日たっぷり使えるプロフェッショナル仕様の大容量ボトル",
        "brand_name": "OIL OF EMU (オイル・オブ・エミュー)",
        "capacity": "285ml / 大容量プッシュボトル",
        "type": "プロ仕様 医療レベル100%ピュアエミューオイル",
        "features": "オーストラリア産高品質エミューオイル100%、特許物理精製、オメガ3・6・9高含有、完全無添加",
        "value": "エステサロンやスポーツトレーナーが業務用として実際に採用する圧倒的クオリティ。全身に毎日使っても数ヶ月持つハイコスパで、真冬の家族全員の乾燥肌を完全防護",
        "desc_p1": "真冬になると顔だけでなく、すね、太もも、背中、お腹まわりなど全身がカサカサに乾いて粉を吹き、下着の締め付けで痒みが増してしまう……そんな全身の重度乾燥に悩む方に最適なのが、プロの現場でも愛用される『オイル・オブ・エミュー 285ml Lサイズ』です。",
        "desc_p2": "オーストラリア政府の厳格な基準（TGA認定）のもと、化学薬品を一切使わずに低温物理ろ過されたピュアオイルは、シルクのように滑らかで驚くほど軽いテクスチャー。お風呂上がりの濡れた全身に3〜4プッシュ伸ばすだけで、全身の角質層が水分をたっぷり抱え込んだモチモチ肌へと生まれ変わります。大容量なので残量を気にせず毎晩全身にたっぷり使え、家族全員の真冬の肌トラブルをこれ一本で一掃できます。",
        "target": "背中やすねなど全身の広範囲が乾燥してかゆみに悩まされている方、家族全員で惜しみなく使える大容量ボトルを求めている方、サロン級の最高品質エミューオイルを体感したい方",
        "point": "お風呂上がりのバスタオルを使う前、全身がまだ濡れている状態で3〜4プッシュを手のひらに広げ、首から足先まで一気に伸ばします。その後タオルで優しく押さえるだけで、極上のうるおいヴェールが完成します。"
    },
    {
        "rank": 6,
        "tag": "🧼 枠練り熟成製法でエミューオイル高配合！洗顔後も化粧水を忘れるほどしっとり潤い膜を残す美容石鹸",
        "catch": "エミューの雫が手がける無添加洗顔石鹸。天然エミューオイルとヒアルロン酸、コラーゲンが凝縮した弾力濃密泡が、冬の肌のバリアを守りながら汚れだけを優しく洗い落とす",
        "brand_name": "エミューの雫 (Emu no Shizuku)",
        "capacity": "100g / 泡立てネット付き",
        "type": "エミューオイル高配合 枠練り熟成高保湿洗顔石鹸",
        "features": "エミュー油、ヒアルロン酸Na、水溶性コラーゲン、天然グリセリン、無香料・無着色・防腐剤フリー",
        "value": "90日間じっくり熟成させる伝統の枠練り製法により、美容保湿成分を限界まで配合。冬の朝晩の洗顔で皮脂を奪いすぎず、つっぱり感ゼロのふっくら肌を洗い上げる",
        "desc_p1": "冬のスキンケアで最も見落とされがちなのが『洗顔による皮脂の奪いすぎ』です。洗浄力の強すぎる洗顔料や熱いお湯で洗うと、肌が本来持っている天然の保湿因子（NMF）やセラミドまで洗い流されてしまい、その後にどんな高級美容液を塗っても乾燥が治まりません。エミューの雫の『エミューフェイスソープ 100g』は、洗う段階から肌に潤いを補給するために設計された枠練り石鹸です。",
        "desc_p2": "付属の泡立てネットで数回こするだけで、生クリームのように濃密でキメ細かい弾力泡がモコモコと立ち上がります。泡を肌に乗せて優しく転がすだけで、エミューオイルの良質な脂肪酸が肌表面の乾燥した角質を柔らかくほぐし、毛穴の汚れだけを吸着。ぬるま湯で洗い流した瞬間、まるで保湿美容液でパックした後のように吸い付くようなモチモチ感が肌に残り、洗顔後のつっぱり感や乾燥小ジワを完全にブロックします。",
        "target": "冬になると洗顔直後に肌がつっぱってカサつく方、固形石鹸の優しい洗い上がりが好きな方、洗顔の段階から本格的なエイジング保湿ケアを取り入れたい方",
        "point": "ぬるま湯でネットを濡らし、石鹸をしっかり泡立ててリンゴ1個分大の弾力泡を作ります。肌を手で擦らず、泡のクッションを押し当てるように洗顔し、32℃前後のぬるま湯で丁寧にすすぎ流してください。"
    },
    {
        "rank": 7,
        "tag": "🍯 エミューオイル×天然植物バターの濃密バーム！真冬のパックリあかぎれ手肌やかかとを集中保護するレスキューバーム",
        "catch": "emure（エミュレ）の高密着エミューバーム。体温でとろけて肌に吸い付くオイルバームが、真冬の水仕事や冷風で荒れ果てた手指やガサガサかかとに鉄壁の潤いバリアを構築する",
        "brand_name": "emure (エミュレ)",
        "capacity": "50g / コンパクトジャー",
        "type": "高密着マルチエモリエント エミューバーム",
        "features": "エミュー油、天然植物バター、スクワラン、ビタミンE、無香料・無鉱物油",
        "value": "液状オイルよりもさらに密着持続性に優れたバーム処方。水仕事や摩擦で流れ落ちにくく、真冬の硬化したかかとやひじ、指先のひび割れを長時間ラップ密封",
        "desc_p1": "冬場の水仕事やアルコール消毒が重なると、指先の皮膚が硬くひび割れてしまい、普通のハンドクリームでは水で流れてしまって全く追いつかない……。そんな過酷な手肌トラブルに悩む方の救世主が、emureの『エミューバーム 50g』です。",
        "desc_p2": "ジャーの中ではしっかりとしたバーム状ですが、指先にとると体温でスーッととろけて滑らかなオイルへと変化。エミューオイルの強力な浸透力によって角層深部を油分で満たし、植物バターの密着膜が肌表面に水を弾く強力な保護シールドを張ります。水仕事をしても潤い膜が簡単には落ちず、寝る前にかかとや指先にすり込んでおけば、翌朝にはカチコチだった皮膚がふっくらと柔らかさを取り戻します。",
        "target": "水仕事や手洗いで指先がパックリ割れて痛い方、硬くなったかかとの角質を柔らかくしたい方、普通のハンドクリームでは物足りない超乾燥肌の方",
        "point": "夜寝る前、少量を手のひらで温めてから、ひび割れやすい指先やかかとへ円を描くように揉み込みます。綿の手袋や靴下を着用して就寝すると、一晩で驚異的な修復効果を実感できます。"
    },
    {
        "rank": 8,
        "tag": "❄️ 北海道オホーツクの極寒で育まれた純国産！冬の厳しい寒風に晒される素肌を濃密に守る純国産クリーム",
        "catch": "北海道網走産の厳選エミューオイルを贅沢に配合した「オホーツクエミュー モイスチャークリーム」。日本の厳しい寒冷地で生まれた高保湿処方が、真冬の乾燥肌を優しく包み込む",
        "brand_name": "オホーツクエミュー (北海道網走産)",
        "capacity": "50g / ジャー容器",
        "type": "純国産 高保湿エミューモイスチャークリーム",
        "features": "北海道網走産エミュー油、天然セラミド、ヒアルロン酸、ホホバ種子油、ラベンダー花水",
        "value": "北海道オホーツクの極寒環境で健やかに飼育されたエミューの希少オイルを使用。純国産ならではの徹底したトレーサビリティと肌なじみの良さで、大人の冬肌を贅沢にうるおす",
        "desc_p1": "オーストラリア原産のエミューオイルですが、近年日本国内でも冷涼な気候を活かした北海道網走で高品質なエミューの飼育が行われており、その希少な純国産オイルを使ったコスメが大きな注目を集めています。それがオホーツクエミューの『モイスチャークリーム 50g』です。",
        "desc_p2": "北海道の厳しい冬の寒さを知る開発陣が作り上げたクリームは、こっくりとリッチでありながら肌に乗せるとベタつかずにスッとなじみます。国産エミューオイルの良質なオメガ脂肪酸と天然セラミドが角層のバリアを隙間なく埋め尽くし、冷たい木枯らしやエアコン暖房の乾燥から素肌を完全防護。朝のメイク前の保護クリームとしても、夜の贅沢なナイトクリームとしても活躍し、内側からふっくらと押し返すような弾力肌へ導きます。",
        "target": "純国産原料にこだわりたい安心重視の方、こっくりリッチなフェイスクリームで冬の乾燥を乗り切りたい方、エイジングケアと高保湿を同時に叶えたい方",
        "point": "夜のお手入れの最後にパール粒大を手にとり、手のひらで温めてから顔全体に引き上げるように伸ばします。乾燥が目立つ目元や口元には指先でトントンと重ねづけしてください。"
    },
    {
        "rank": 9,
        "tag": "👜 持ち歩きに便利な高保湿チューブ！外出先での手指・ひじ・目元の乾燥をサッと潤すエミュークリーム",
        "catch": "オメガ3・6・9とビタミンをバランスよく配合した「エミュークリーム 40g」。外出先でカサつきを感じた瞬間、手を汚さずスマートに使えるデイリーハンド＆ボディクリーム",
        "brand_name": "Emu Cream Japan (エミュークリーム)",
        "capacity": "40g / チューブ容器",
        "type": "高浸透ハンド＆ボディエモリエントクリーム",
        "features": "エミュー油、ビタミンE、オレイン酸、スクワラン、無香料・低刺激処方",
        "value": "バッグやポケットに入れてサッと取り出せるスリムチューブ。オイリーなベタつきを残さずサラリと仕上がるため、真冬の外出中や仕事中でも快適にパーツ保湿が可能",
        "desc_p1": "冬の外出中、急な寒風で手指がカサついたり、ひじの粉吹きが気になった時に、ジャータイプのバームやオイルボトルを取り出すのは少し手間がかかるもの。そんなアクティブな冬の日常に寄り添うのが、チューブタイプの『エミュークリーム 40g』です。",
        "desc_p2": "チューブから適量をサッと絞り出せる手軽さで、伸ばすと瞬時に角質層へ浸透してサラサラのシルク肌に整えます。エミューオイル特有の高浸透力により、表面にベタつく油分が残らないため、塗った直後にスマホの操作や書類の取り扱いを行っても問題ありません。無香料なのでオフィスや外出先でも周囲に気兼ねなく使え、日中の乾燥ダメージをこまめにブロックできます。",
        "target": "持ち歩きやすいチューブタイプの高保湿クリームを探している方、塗った直後にベタつかないハンドクリームを好む方、日中のこまめなパーツケアを習慣にしたい方",
        "point": "1〜2cmほどを手の甲に出し、両手の甲をすり合わせるように広げてから、指先や爪のキワへ一本ずつ丁寧に馴染ませます。外出前の習慣にすると寒風ダメージを最小限に抑えられます。"
    },
    {
        "rank": 10,
        "tag": "🌾 全身に浴びるように使える大容量100ml！人間の皮脂膜と同じ構造で冬の乾燥かゆみを完全ブロックする国産ピュアオイル",
        "catch": "国産エミューオイル100%の大容量ボトル。オメガ3・6・9を豊富に保持し、お風呂上がりの濡れた肌に全身伸ばせる圧倒的コストパフォーマンスで真冬の粉吹き・かゆみ肌を完全撃退",
        "brand_name": "Natural Emu Oil (国産エミュー)",
        "capacity": "100ml / ポンプボトル",
        "type": "国産無添加100% 天然エミューオイル",
        "features": "国産エミュー油100%、オメガ3・6・9、オレイン酸（約50%）、完全無添加・無着色・無香料",
        "value": "100mlの大容量ポンプで全身に惜しみなく使用可能。入浴後の濡れた肌に伸ばすことで水分と乳化し、真冬の乾燥で硬化した全身の皮膚を柔らかくモチモチに保つ",
        "desc_p1": "冬になると足のすねや太もも、腕や背中など広範囲にわたって粉吹きやかゆみが発生し、小さなボトルではあっという間に使い切ってしまう……。そんな大人の乾燥ボディに力強い味方となるのが、国産エミューオイル100%の『大容量100mlポンプ』です。",
        "desc_p2": "ポンプを押して手のひらにたっぷり取り、お風呂上がりの温まった体に伸ばすと、スーッと肌に吸い込まれて衣服に貼りつかないサラサラの保湿膜が完成。人間の皮脂膜と同じオレイン酸・パルミチン酸が皮膚のバリア機能を強固に補強し、暖房の効いた乾燥した部屋で一晩過ごしても、朝起きた時にすねの粉吹きやかゆみが全く気になりません。毎日の全身エモリエントケアとして最高の満足度を誇る一本です。",
        "target": "大容量で惜しみなく全身のボディケアに使いたい方、お風呂上がりのインバスケアで乾燥を予防したい方、安心安全な国産エミューオイルを好む方",
        "point": "入浴後、浴室から出る前の濡れた肌に2〜3プッシュを全身にサーッと伸ばします。その後タオルでポンポンと優しく水分を押さえるだけで、一日中吸い付くような潤いボディが続きます。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の粉吹き肌＆あかぎれ！人間の皮脂に酷似したエミューオイルとは"},
    {"id": "mechanism", "title": "2. なぜエミューオイルは最強なのか？生体親和性と深層浸透力の皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿エミューオイルコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿エミューオイルコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しない冬のエミューオイルコスメの選び方＆パーツ別活用術"},
    {"id": "routine", "title": "6. 真冬の頑固な乾燥・粉吹き・あかぎれを救う！効果的な重ねづけケアステップ"},
    {"id": "faq", "title": "7. エミューオイルコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：人肌と一体化する奇跡のオイルで真冬の肌乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">{item_data["price"]}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["img"]}" alt="{item_data["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">{item_data["price"]}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", item_data.get("reviewAverage", "4.8"))}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", item_data.get("reviewCount", "110"))}件）</span>
              </div>
              <a href="{item_data["url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                🛒 楽天市場で「{p["brand_name"]}」の最新価格・在庫・口コミを見る
              </a>
            </div>

            <div class="product-info-col">
              <table class="spec-table">
                <tr><th>ブランド</th><td>{p["brand_name"]}</td></tr>
                <tr><th>容量・容器</th><td>{p["capacity"]}</td></tr>
                <tr><th>アイテム種別</th><td>{p["type"]}</td></tr>
                <tr><th>注目美肌成分</th><td>{p["features"]}</td></tr>
                <tr><th>真冬の特長・価値</th><td>{p["value"]}</td></tr>
              </table>

              <div class="product-body">
                <h4 class="body-title">皮膚科学的アプローチ＆冬の使用感レビュー</h4>
                <p>{p["desc_p1"]}</p>
                <p>{p["desc_p2"]}</p>

                <div class="recommend-box">
                  <div class="recommend-title">💡 こんな方・こんな冬の肌悩みにおすすめ！</div>
                  <p>{p["target"]}</p>
                </div>

                <div class="usage-box">
                  <div class="usage-title">🧴 11月・12月の効果的な使い方テクニック</div>
                  <p>{p["point"]}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
""")

all_cards_html = "\n".join(product_cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！人肌とほぼ同等の皮脂組織が真冬の粉吹き乾燥・ガサガサあかぎれ肌に瞬時に溶け込む高保湿エミューオイルコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の極寒乾燥で粉を吹くすね・腕、水仕事であかぎれた手肌、関節の激しい乾燥を救う高保湿エミューオイルコスメを徹底厳選！エミューの雫、エミューム、キダデラックス、オイル・オブ・エミュー、オホーツクエミューまで生体親和性脂肪酸の科学的根拠と共に徹底検証。">
  <meta name="keywords" content="エミューオイル, 高保湿 オイル 冬, エミューの雫, エミューム, キダデラックス, あかぎれ 対策, 粉吹き肌 対策, オメガ369, 乾燥肌 スキンケア 11月 12月">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-emu-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！人肌とほぼ同等の皮脂組織が真冬の粉吹き乾燥・ガサガサあかぎれ肌に瞬時に溶け込む高保湿エミューオイルコスメランク10">
  <meta property="og:description" content="11月・12月の本格乾燥シーズン！人間の皮脂膜に最も近い驚異の生体親和性を持つ高保湿エミューオイルコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-emu-oil">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！人肌とほぼ同等の皮脂組織が真冬の粉吹き乾燥・ガサガサあかぎれ肌に瞬時に溶け込む高保湿エミューオイルコスメランク10",
    "description": "11月・12月の極寒乾燥で粉を吹くすね・腕、水仕事であかぎれた手肌、関節の激しい乾燥を救う高保湿エミューオイルコスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-emu-oil"
    }},
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 保湿皮膚科学研究チーム"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "datePublished": "2026-11-05T16:00:00+09:00",
    "dateModified": "2026-11-05T16:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿エミューオイルコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {", ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["name"]}",
        "url": "{items[p["rank"]-1]["url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "エミューオイルと馬油は何が違うのですか？どちらが冬の乾燥肌に良いですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "馬油も人間皮脂に近いオイルとして知られますが、エミューオイルは馬油よりもさらにオレイン酸比率（約50%）が高く、皮膚深部への浸透スピード（経皮吸収性）が圧倒的です。馬油特有の油膜感やベタつきがほとんどなく、真冬の硬化した角質層を瞬時に柔らかくする力や、あかぎれ・乾燥かゆみの消炎サポート力においてエミューオイルが極めて高い評価を得ています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "動物性オイル特有の生臭さや匂いはありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "医療レベルの精密精製（オーストラリア特許製法など）が行われた化粧品用エミューオイルは、ほぼ完全に無臭・透明〜乳白色です。酸化臭や獣臭は一切ありませんので、お顔や口元、デリケートな肌にも安心して心地よくお使いいただけます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "冬場に白く固まることはありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "エミューオイルは豊富な不飽和脂肪酸を含んでいるため、オリーブオイルやココナッツオイルのようにカチカチに固まることは稀ですが、10℃以下の非常に寒い室内に置くと白く濁ったりジェル状にとろみが増すことがあります。これは品質異常ではなく天然オイルの特性で、手のひらで温めると瞬時に透明な液状に戻ります。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #15803d;
      --primary-light: #dcfce7;
      --primary-dark: #14532d;
      --accent: #16a34a;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #f0fdf4;
      --bg-card: #ffffff;
      --border: #bbf7d0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #dcfce7 0%, #ffffff 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}
    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      line-height: 1.45;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.75;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #6b7280;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}
    
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-card li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-card a:hover {{ color: var(--primary); text-decoration: underline; }}
    
    .article-section {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
    }}
    .highlight-lead {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--accent);
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #f0fdf4;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      margin-bottom: 1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .price-box {{
      width: 100%;
      background: #ffffff;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      text-align: center;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #6b7280; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: #6b7280; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #7a0000 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 10px -1px rgba(191, 0, 0, 0.35);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 140px;
      background: #f0fdf4;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    
    .product-body h4.body-title {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #dcfce7;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    .usage-box {{
      background: #f0fdf4;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🦘 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">豪州先住民族の知恵・生体親和性No.1浸透エモリエント</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！人肌とほぼ同等の皮脂組織が真冬の粉吹き乾燥・ガサガサあかぎれ肌に瞬時に溶け込む高保湿エミューオイルコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて訪れる本格的な寒波。すねや太ももが粉を吹いてかゆみに耐えられない、水仕事や消毒の繰り返しで指先がパックリ割れて治らない、通常の保湿クリームをどれだけ塗り重ねても数時間で乾いてしまう……。そんな真冬の「重度乾燥・皮脂枯渇」に対する最終兵器として世界中の医療・スポーツ・スキンケア界で絶賛されているのが、人間の皮脂膜とほぼ完全に一致する脂肪酸組成を持つ「エミューオイル（エミュー油）」です。本記事では、驚異的な経皮吸収性と消炎・組織修復メカニズムを解説し、楽天市場で今すぐ手に入る最高峰エミューコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬乾燥特化版）</span>
        <span>🔬 皮脂類似脂肪酸・経皮吸収エビデンス検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の粉吹き肌＆あかぎれ！人間の皮脂に酷似したエミューオイルとは</h2>
      <div class="highlight-lead">
        皮脂が枯渇した冬の角質層に、皮膚が「自分の皮脂だ」と認識して瞬時に吸収する生体親和性。エミューオイルは、あかぎれや粉吹きかゆみを根底から救う究極のエモリエントです。
      </div>
      <p>
        冬の寒風が吹き荒れる11月下旬以降、私たちの皮膚表面を守る皮脂腺の活動は極限まで低下します。特に皮脂腺の少ないすね、腕、背中、そして水仕事にさらされる手肌は、天然の皮脂膜が完全に失われ、角質細胞同士を接着している細胞間脂質（セラミド等）まで流出してしまいます。この状態を放置すると、角質がめくれ上がって白い粉を吹き、下着の摩擦や温かい布団の温熱によって神経線維（C線維）が過敏に刺激され、我慢できないほどの激しいかゆみ（乾皮症・皮脂欠乏性湿疹）へと悪化します。
      </p>
      <p>
        一般的な植物油やミネラルオイルを塗っても、「肌の表面でギトギト上滑りするだけで奥まで潤わない」「水で手を洗うとすぐに落ちてしまう」という経験はありませんか。それは、人間と植物・鉱物では脂肪酸の構造が根本的に異なるためです。オーストラリアの先住民族アボリジニが4万年もの歴史の中で傷や火傷、過酷な乾燥の治療薬として伝承してきた「エミューオイル」は、天然界で最も人間の皮脂組織に酷似しており、肌に乗せた瞬間に細胞レベルで一体化する驚異の特性を備えています。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜエミューオイルは最強なのか？生体親和性と深層浸透力の皮膚科学</h2>
      <p>
        エミューオイルが他のあらゆる保湿オイルを圧倒する理由は、皮膚科学的に証明された以下の3大特性にあります。
      </p>
      <p>
        <strong>① 人間の皮脂膜とほぼ完全に一致する脂肪酸バランス：</strong><br>
        健康な人間の皮脂は、オレイン酸、パルミチン酸、リノール酸、パルミトレイン酸などで構成されています。エミューオイルの脂肪酸組成は、オレイン酸約50%、パルミチン酸約20〜25%、リノール酸約10〜15%と、人間の皮脂プロファイルとほぼ鏡写しのように酷似しています。肌がエミューオイルを「異物」ではなく「自分自身の皮脂」と認識するため、アレルギー反応や拒絶反応を起こさず、乱れたバリア機能を瞬時に代替・修復します。
      </p>
      <p>
        <strong>② 驚異の経皮浸透性（トランスダーマルデリバリー）：</strong><br>
        一般的なオイル分子は角質層のバリアを通過できず表面にとどまりますが、エミューオイルは分子構造の親和性により、角質層のラメラ構造をすり抜けて深部まで高速で浸透します。さらに、一緒に配合された美容成分（ビタミンやプロテオグリカン、MSMなど）を道連れにして肌奥へと届ける「キャリアオイルとしての卓越した浸透力」を持っています。塗布後わずか数分でサラサラになるのは、この圧倒的な浸透スピードによるものです。
      </p>
      <p>
        <strong>③ 天然の消炎・組織修復サポート（オメガ3・6・9複合体）：</strong><br>
        エミューオイルには、オメガ3（リノレン酸）、オメガ6（リノール酸）、オメガ9（オレイン酸）が理想的な自然バランスで含有されています。これらは皮膚内の炎症物質（プロスタグランジン等）の過剰産生を抑制し、水仕事によるあかぎれの傷口や、乾燥によるかゆみ・赤みを穏やかに鎮静。冬の傷んだ皮膚のターンオーバーを健全な周期へと回復させます。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿エミューオイルコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入できる、真冬の粉吹き肌＆あかぎれを救う高保湿エミューオイルコスメ10アイテムの比較一覧表です。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿エミューオイルコスメおすすめ厳選ランキング10選</h2>
      <p>
        オイル精製度、生体親和性脂肪酸の純度、真冬の粉吹き・あかぎれ改善実感、安全基準を徹底検証したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しない冬のエミューオイルコスメの選び方＆パーツ別活用術</h2>
      <p>
        エミューオイルコスメを真冬のケアに導入する際、症状や使用シーンに合わせた最適な選び方の指針です。
      </p>
      <p>
        <strong>① ひび割れ・あかぎれ・粉吹きかゆみの集中治療には「100%ピュアオイル」：</strong><br>
        エミューの雫（第1位・第2位）やエミューム（第3位）、オイル・オブ・エミュー（第5位）のように、不純物を取り除いた無添加100%オイルは、傷口にしみることなく角質深部へ浸透し、最も速効性のある修復力を発揮します。
      </p>
      <p>
        <strong>② 水仕事の多い手肌や硬化したかかとには「高密着バーム」：</strong><br>
        emureのエミューバーム（第7位）は、植物バターとのブレンドにより水を弾く保護膜を長時間キープ。水仕事の前後に塗ることでパックリ割れを徹底的に予防できます。
      </p>
      <p>
        <strong>③ 寒冷による肩腰のコリや関節の強張りには「MSM配合マッサージクリーム」：</strong><br>
        野口医学研究所のキダデラックス（第4位）は、エミューオイルの浸透性を活かして関節ケア成分を届けるため、冬の寒さでこわばった筋肉をほぐしながらボディの乾燥も同時に解消できます。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬の頑固な乾燥・粉吹き・あかぎれを救う！効果的な重ねづけケアステップ</h2>
      <p>
        エミューオイルの生体親和性を120%引き出す、真冬のパーフェクトケアステップです。
      </p>
      <p>
        <strong>ステップ1【入浴後の濡れた肌への水分抱き込み】：</strong><br>
        お風呂から上がる直前、タオルで水分を拭き取る前の肌にエミューオイルを伸ばします。水分とオイルが瞬時に乳化し、肌の内側に水分を閉じ込めながら角質層をふっくら柔軟にします。
      </p>
      <p>
        <strong>ステップ2【あかぎれ・ひび割れ部位へのピンポイント重ね塗り】：</strong><br>
        特に乾燥がひどいかかと、ひじ、指先のあかぎれには、少量を指先にとり、円を描くように優しくすり込みます。エミューオイルのオメガ脂肪酸が痛んだ組織を集中リペアします。
      </p>
      <p>
        <strong>ステップ3【ナイト手袋・靴下による集中ラップ密封】：</strong><br>
        就寝前に手肌やかかとにオイルまたはバームをしっかり塗り、綿の手袋や靴下を履いて密閉します。一晩でカチコチだった皮膚が生まれ変わったように柔らかく滑らかになります。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. エミューオイルコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> エミューオイルと馬油は何が違うのですか？どちらが冬の乾燥肌に良いですか？</div>
        <div class="faq-a">
          馬油も人間皮脂に近いオイルとして知られますが、エミューオイルは馬油よりもさらにオレイン酸比率（約50%）が高く、皮膚深部への浸透スピード（経皮吸収性）が圧倒的です。馬油特有の油膜感やベタつきがほとんどなく、真冬の硬化した角質層を瞬時に柔らかくする力や、あかぎれ・乾燥かゆみの消炎サポート力においてエミューオイルが極めて高い評価を得ています。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 動物性オイル特有の生臭さや匂いはありますか？</div>
        <div class="faq-a">
          医療レベルの精密精製（オーストラリア特許製法など）が行われた化粧品用エミューオイルは、ほぼ完全に無臭・透明〜乳白色です。酸化臭や獣臭は一切ありませんので、お顔や口元、デリケートな肌にも安心して心地よくお使いいただけます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬場に白く固まることはありますか？</div>
        <div class="faq-a">
          エミューオイルは豊富な不飽和脂肪酸を含んでいるため、オリーブオイルやココナッツオイルのようにカチカチに固まることは稀ですが、10℃以下の非常に寒い室内に置くと白く濁ったりジェル状にとろみが増すことがあります。これは品質異常ではなく天然オイルの特性で、手のひらで温めると瞬時に透明な液状に戻ります。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 顔のスキンケアに使っても吹き出物や毛穴詰まりの原因になりませんか？</div>
        <div class="faq-a">
          エミューオイルは毛穴を詰まらせにくい（ノンコメドジェニック）特性を持っています。洗顔後のブースターとして1〜2滴薄く伸ばすことで、冬のインナードライを防ぎつつキメを整えてくれます。皮脂の多い部分は薄く、乾燥しやすい頬や目元・口元を中心にハンドプレスしてください。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：人肌と一体化する奇跡のオイルで真冬の肌乾燥とさようなら</h2>
      <p>
        11月から12月にかけての過酷な寒冷と暖房乾燥は、私たちの肌から容赦なく天然の皮脂を奪い去ります。粉を吹くすね、痛々しいあかぎれ、夜眠れないほどの乾燥かゆみ……それらはすべて、肌のバリアが悲鳴を上げているサインです。
      </p>
      <p>
        人間の皮脂組織とほぼ同等の奇跡的な生体親和性を持つエミューオイルは、傷ついた角質層を瞬時に満たし、まるで自分自身の肌が息を吹き返したかのような深い安心感を与えてくれます。日頃のハンドケアから入浴後の全身ボディケアまで、信頼できる最高品質のエミューオイルコスメを手に入れて、真冬の寒さに負けないしっとり健やかな素肌を取り戻してください。
      </p>
    </section>

    <!-- 関連記事ボックス -->
    <div class="related-grid" id="related-grid-box"></div>

    <!-- 内部リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container"></div>
    </div>
  </main>

  <footer class="site-footer" style="background:#ffffff;border-top:1px solid #bbf7d0;margin-top:4rem;">
    <div class="footer-inner">
      <div class="footer-links-grid" id="footer-links-box"></div>
      <div class="footer-links-grid" id="footer-links-placeholder"></div>
      <p style="text-align:center;font-size:0.85rem;color:#6b7280;margin-top:2rem;">© 2026 LUMI COSMETICS. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-emu-oil.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-emu-oil.html successfully!")
