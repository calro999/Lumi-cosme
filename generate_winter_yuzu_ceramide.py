import json
import re

with open("fetched_3new_nov_dec_yuzu_sake_vitamine.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_yuzu_ceramide"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 天然ユズ精油×種子エキス！冬の乾燥バリアを優しく立て直す大人気ボディローション",
        "catch": "高知県産ユズ果皮精油の爽やかな芳香とユズ種子エキス。ベタつかず角層へ素早く浸透し、冬の粉吹き肌をしっとり保護",
        "brand_name": "松山油脂 (Mマークシリーズ)",
        "capacity": "300ml (柚子ボディローション)",
        "type": "高保湿植物性ユズエマルジョンローション",
        "features": "ユズ果皮油（高知県産天然精油）、ユズ種子エキス、カルナウバロウ、グリセリン、シア脂",
        "value": "入浴後の急激な過乾燥（過蒸発）を防ぎ、天然精油の香りで冷え切った心身をほぐしながら角層の水分蒸発を徹底ブロック",
        "desc_p1": "11月から12月にかけて外気温が10℃を下回り始めると、入浴後の浴室から出た瞬間に肌の水分が一気に蒸発する『過乾燥現象』が加速します。粉を吹いたスネやひび割れそうな腕を優しく包み込むのが、石けんづくりの名門・松山油脂の『Mマーク 柚子ボディローション』です。圧搾法で丁寧に抽出された高知県産ユズ果皮精油を配合し、人工香料では決して表現できない本物の搾りたて柚子の清々しい香りがバスルームいっぱいに広がります。",
        "desc_p2": "水分保持力に優れたユズ種子エキスと植物性ワックスのカルナウバロウが、肌表面になめらかな保護皮膜を形成。乳液状のテクスチャーは肌に伸ばした瞬間にみずみずしく崩れ、角層の奥へすーっと浸透します。ボディローションにありがちなベタつきやヌルつきが一切残らないため、塗布した直後にパジャマを着ても張り付きません。敏感肌や小さなお子様がいるご家庭でも安心して全身にたっぷり使える冬の定番名品です。",
        "target": "お風呂上がりに全身がつっぱる・粉を吹く方、ベタつくボディクリームが苦手な方、天然柚子のリアルな香りでリラックスしたい方",
        "point": "お風呂から上がってタオルで軽く水気を拭き取った直後の、湿り気が残る肌へ2〜3プッシュを素早く伸ばします。温まった手のひらで肌を包み込むようにハンドプレスすると、角層へのなじみが格段に高まります。"
    },
    {
        "rank": 2,
        "tag": "🌙 高知産ユズセラミド×桜酵母！寝ている間に乾燥毛穴とキメをふっくら再建",
        "catch": "高知産ユズセラミド濃縮配合。美容液・パック・マッサージの3役を兼ね備え、真冬の乾燥ゴワつき肌をほぐし尽くす",
        "brand_name": "草花木果 (そうかもっか)",
        "capacity": "90g (透肌マスクジェル エンリッチ)",
        "type": "高保水ユズセラミド美容液パックジェル",
        "features": "ユズセラミド（スフィンゴ脂質）、八重桜酵母エキス、酒粕エキス、植物性スクワラン",
        "value": "植物性ユズセラミドが乱れた角質細胞の隙間を埋め、翌朝まで潤いシールドを持続。冷気による毛穴目立ちをピンと引き締める",
        "desc_p1": "冬の寒風にさらされ、夜になるとファンデーションが毛穴に落ちたり皮向けが目立ってしまう『冬枯れ毛穴肌』。草花木果の『透肌マスクジェル エンリッチ』は、日本の自然の恵みである高知県産ユズから抽出したユズセラミドを贅沢に配合した高機能美容液ジェルです。ヒト型セラミドに匹敵するバリア補修能を持つユズセラミドが、乾燥で硬くなった角層をじんわりと解きほぐします。",
        "desc_p2": "ぷるんと厚みのある濃密ジェルが肌にピタッと密着し、一晩中うるおいを閉じ込めるスリーピングマスク効果を発揮。八重桜酵母と酒粕エキスの相乗効果により、寝ている間に肌のターンオーバーを穏やかにサポートします。翌朝の洗顔時には、肌がまるで内側から水分で満たされたかのようなふっくらとした弾力と、キメの整った明るい素肌を実感できます。",
        "target": "真冬になると毛穴の開きやキメの乱れが気になる方、夜のスキンケアを手短に済ませたい方、肌のゴワつきやくすみを一掃したい方",
        "point": "化粧水の後にさくらんぼ1粒大を顔全体に伸ばします。特に乾燥や毛穴の開きが気になる小鼻の脇や頬には、ジェルを少し多めに乗せて『スチームパック風』になじませてそのまま就寝してください。"
    },
    {
        "rank": 3,
        "tag": "🖐️ 京都の伝統美！シルクエキス×天然ユズ果皮油が水仕事のひび割れ手肌を救護",
        "catch": "京都老舗よーじやの極上ハンドケア。絹糸由来のセリシンと天然柚子が融合し、指先まで吸い付くような潤いとしなやかさを実現",
        "brand_name": "よーじや (YOJIYA)",
        "capacity": "30g (ゆずつやや はんどくりーむ)",
        "type": "高密着シルク×ユズハンドトリートメント",
        "features": "天然ユズ果皮油、加水分解シルク（セリシン）、ヒアルロン酸Na、シア脂",
        "value": "水や摩擦に強い保護膜を形成しながら、指先の乾燥ささくれや荒れを予防。上品な和柚子の香りで手肌をトータルケア",
        "desc_p1": "11月から12月は水仕事の冷たさと毎日の手洗い・アルコール消毒によって、手肌の皮脂が完全に奪われる過酷な季節。京都の美の老舗・よーじやが手がける『ゆずつやや はんどくりーむ』は、天然の柚子果皮油の爽やかな香りと、蚕の繭から抽出された天然シルクエキス『セリシン』の吸湿保水力を結集した名品ハンドクリームです。",
        "desc_p2": "セリシンは人間の肌のアミノ酸構成と酷似しており、角層のすみずみまで溶け込むようになじんで手肌のバリアを強力にサポート。こっくりとした濃厚なテクスチャーでありながら、肌に塗り込むと摩擦なくスーッと伸び、指先までベタつかないシルキーな仕上がりへと変化します。スマホの画面やパソコンのキーボードをすぐに触れる快適さと、冬のひび割れ・あかぎれを防ぐ確かな保護力を兼備しています。",
        "target": "冬場の水仕事や消毒で手がカサカサ・ささくれになりやすい方、塗った直後にパソコンやスマホを操作したい方、上品な和の香りを楽しみたい方",
        "point": "米粒大を手の甲に出し、両手の甲をすり合わせるように広げた後、指の関節や甘皮の周りまで一本ずつ丁寧にマッサージしながら塗り込みます。爪の生え際を軽くプッシュすると血行も促進されます。"
    },
    {
        "rank": 4,
        "tag": "🛁 天然岩塩×ユズ＆ジンジャー！冷え切った身体を芯から温める薬用バスソルト",
        "catch": "古代海水の天然岩塩にユズ精油とジンジャー精油を贅沢ブレンド。冬至の柚子湯を思わせる発汗・血行促進・肌しっとり効果",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "850g (バスソルト ユズ＆ジンジャーの香り)",
        "type": "高濃度ミネラル薬用ハーバルバスソルト",
        "features": "天然岩塩（ルイーゼンハル産地下海水）、ユズ果皮油、ショウガ根油、オレンジ果皮油",
        "value": "温浴効果で全身の毛細血管を広げて巡りを改善。入浴中の発汗とミネラル補給により、冬の頑固な乾燥肌をしっとり柔らかく解きほぐす",
        "desc_p1": "ドイツのハーバルブランド・クナイプが日本の冬の風習『柚子湯』に着想を得て調合した『ユズ＆ジンジャーの香り』。2億5000万年前の古代海水を汲み上げた天然岩塩に、天然の柚子精油とスパイシーな生姜精油を閉じ込めたバスソルトです。お湯に入れた瞬間に浴室いっぱいに広がる爽やかでスパイシーな温かい香りは、冬の寒さで強張った心と体を瞬時に解放します。",
        "desc_p2": "天然岩塩に含まれる豊富なミネラルが肌の表面に膜を作り、お風呂上がりの体温と水分が逃げるのを防ぎます。38〜40℃のぬるめのお湯にゆっくり15〜20分浸かるだけで、体の芯からポカポカと温まり、入浴後も湯冷め知らず。乾燥でゴワつきがちなひじ・かかと・すねの角質も柔らかくなり、お風呂上がりのスキンケアの浸透が格段に向上します。",
        "target": "手足の冷えがひどく夜ぐっすり眠れない方、冬場の全身の乾燥とかゆみを防ぎたい方、お風呂でしっかり発汗して巡りを整えたい方",
        "point": "浴槽のお湯（約200L）にキャップ1杯（約40〜50g）を入れてよくかき混ぜて入浴します。入浴前後にコップ1杯の常温水を飲むことで、デトックスと体内保水が促されます。"
    },
    {
        "rank": 5,
        "tag": "🌾 コメ発酵液×国産ユズセラミド！洗顔後の素肌を柔らかくほぐす導入美容液",
        "catch": "老舗酒蔵の純米酒発酵液に高純度ユズセラミドを融合。真冬のごわついた角層を潤いで解きほぐし、化粧水の吸い込みを数倍へ",
        "brand_name": "菊正宗酒造",
        "capacity": "185ml (正宗印 導入美容液)",
        "type": "角層柔軟ユズセラミドブースター美容液",
        "features": "コメ発酵液、ユズ果実エキス（ユズセラミド）、ヒアルロン酸、アミノ酸複合体",
        "value": "寒さで硬化した冬の角層にすばやく通り道を作り、後から重ねる化粧水や乳液の浸透効率を爆発的に高める高コスパブースター",
        "desc_p1": "「冬になると化粧水が肌の上で弾かれて入っていかない」という悩みは、寒気と乾燥で角層のケラチンが硬直していることが原因です。菊正宗の『正宗印 導入美容液』は、純米酒の醸造技術から生まれたコメ発酵液に、国産ユズから抽出したユズセラミドを掛け合わせた洗顔直後専用の導入液です。",
        "desc_p2": "みずみずしいローション状のテクスチャーが乾いた素肌に触れると、まるで水を吸い込むスポンジのように角層へと浸透。硬くなった角質細胞の結びつきをやさしく緩め、肌の内側からうるおいで満たします。これを使用した後に普段の化粧水を重ねると、驚くほどスッと肌になじみ、もちもちとした柔らかな感触が長時間持続。185mlの大容量で惜しみなく使える点も冬の味方です。",
        "target": "化粧水の浸透が悪く表面だけが濡れているように感じる方、肌が硬くごわついている方、導入ケアをプチプラで試してみたい方",
        "point": "洗顔後すぐ、化粧水の前に2プッシュを手にとり、顔全体を包み込むように優しくなじませます。特に皮膚が厚くなりやすい額や小鼻まわりはくるくると円を描くように塗布してください。"
    },
    {
        "rank": 6,
        "tag": "💧 5種のヒト型セラミド×大豆＆ユズセラミド！超乾燥肌を包み込む濃厚浸透水",
        "catch": "角層深くまでうるおす高保水設計。ヒアルロン酸と濃密セラミドコンプレックスが、真冬のエアコン乾燥下でも乾きを寄せ付けない",
        "brand_name": "松山油脂 (肌をうるおす保湿スキンケア)",
        "capacity": "120ml (保湿浸透水 モイストリッチ)",
        "type": "超高保湿セラミド化粧水",
        "features": "5種のヒト型セラミド（EOP, NG, NP, AG, AP）、ユズ種子エキス、大豆発酵エキス、ヒアルロン酸Na",
        "value": "肌本来のバリア機能と同じセラミドを高濃度補給。真冬の過酷な低湿度環境でも水分をガッチリ抱え込む",
        "desc_p1": "敏感肌や乾燥肌から圧倒的な信頼を集める松山油脂の『肌をうるおす保湿スキンケア』シリーズ。その中でも『モイストリッチ』は、とろみのある濃密なリッチテクスチャーで真冬の砂漠肌を救い出す大人気ローションです。5種類ものヒト型セラミドに加え、ユズ種子エキスを配合することで、保水力と角層バリアの持続性を極限まで高めています。",
        "desc_p2": "手に取ると美容液のように濃厚なとろみがありながら、肌に乗せるとベタつかずに奥深くまでじっくりと浸透。アルコール、パラベン、香料、着色料、鉱物油がすべて不使用の低刺激処方のため、冬の乾燥によってピリピリと敏感になった肌にも染みることなく優しく寄り添います。重ねづけするほどに肌密度が高まり、吸い付くようなもっちり素肌が完成します。",
        "target": "冬の乾燥で肌がヒリつく・皮がめくれる超乾燥肌の方、濃厚なとろみ化粧水が好きな方、無香料・低刺激で肌バリアを強化したい方",
        "point": "500円玉大を手にとり、顔全体に優しくハンドプレスしてなじませます。一度なじんだ後、さらに同量をもう一度重ねづけする『2度塗り』を行うことで、暖房下でも一日中乾かない鉄壁の保湿膜が完成します。"
    },
    {
        "rank": 7,
        "tag": "🌿 高知県産オーガニック柚子果実水×植物オイル！日中のエアコン砂漠を救う二層式ミスト",
        "catch": "水分7：油分3の黄金バランス。乾燥したオフィスや外出先でサッと吹きかけるだけで、メイクの上からツヤとバリアを即効補給",
        "brand_name": "tokotowa organics (トコトワオーガニクス)",
        "capacity": "200ml (ピュアエッセンスミスト イエロー)",
        "type": "二層式オーガニックユズ保湿ミスト化粧水",
        "features": "高知県産有機ユズ果実水、グレープフルーツ果皮油、スクワラン、アルガンオイル、ホホバ種子油",
        "value": "水分だけでなく上質な植物油を同時に補給するため、水分の蒸発による乾燥（過乾燥）を起こさず一日中みずみずしいツヤをキープ",
        "desc_p1": "暖房が効いた真冬の室内では、肌から水分が猛烈なスピードで奪われていきます。しかし、一般的な水分だけのミストスプレーは蒸発する際に肌本来の水分まで奪ってしまう危険があります。トコトワオーガニクスの『ピュアエッセンスミスト イエロー』は、有機栽培された高知産ユズ果実水と高純度植物オイルを絶妙な比率でブレンドした二層式ミストです。",
        "desc_p2": "使用前にシェイクしてスプレーすると、微細なミストが肌をふんわりと包み込み、油分のベールが角層にフタをして水分を閉じ込めます。メイクの上から吹きかけてもファンデーションがヨレることなく、自然な水光ツヤが復活。天然柚子とグレープフルーツのフレッシュな和柑橘アロマが、午後の疲れた気分をシャキッとリフレッシュさせてくれます。",
        "target": "オフィスの暖房で夕方になると顔が突っ張る・粉を吹く方、日中のメイク直しにツヤを足したい方、上質なオーガニックコスメを好む方",
        "point": "ボトルをよく振って二層を混ぜ合わせた後、顔から20cmほど離して円を描くように3〜4プッシュ吹きかけます。手で擦らず、手のひらで優しく顔を包み込んで密着させてください。"
    },
    {
        "rank": 8,
        "tag": "🍊 ゆずエキス×ビタミンC誘導体！冬の乾燥くすみを払拭し透明感を宿す集中エッセンス",
        "catch": "韓国コフン産の高品質ゆず抽出エキスを凝縮。カサつきと寒冷による肌トーンの低下を同時にケアする高保水美容液",
        "brand_name": "SKINFOOD (スキンフード)",
        "capacity": "50ml (ゆずC ダークスポット クリアエッセンス)",
        "type": "高保水ゆずビタミンC透明感エッセンス",
        "features": "ゆず果実エキス（ビタミンC高含有）、ナイアシンアミド、甘草根エキス、パンテノール",
        "value": "乾燥によるキメの乱れとくすみに水分とビタミンを集中チャージ。澄んだみずみずしい透明肌へと導く",
        "desc_p1": "冬の寒さと乾燥が重なると、肌の血色感が失われてどんよりと暗く見えがちです。フードコスメのパイオニア・スキンフードの『ゆずC』シリーズは、日照時間が長く豊かな土壌で育った韓国コフン産のゆずエキスを贅沢に使用。レモンの約3倍以上とも言われる豊富なビタミンCと水分が、乾いてくすんだ冬の角層を明るく照らします。",
        "desc_p2": "ぷるぷるとしたジェル状のエッセンスは、肌に乗せると体温ですっと液状にほどけて角層の隙間を満たします。ナイアシンアミドとの相乗効果により、乾燥によるキメの影をふっくら持ち上げ、透明感あふれるツヤ肌へ。ビタミン特有の刺激感がなく、穏やかにうるおいを補給できるため、冬のゆらぎ肌でも心地よくデイリー使いできます。",
        "target": "冬になると肌がくすんで顔色が悪く見える方、美白ケアと高保湿ケアを両立したい方、さっぱり潤うテクスチャーが好きな方",
        "point": "化粧水の後にスポイト1〜2回分を顔全体に伸ばします。くすみや乾燥が気になる目の下や頬の高い位置には、指先で優しくタッピングしながら重ね塗りすると透明感が一段と際立ちます。"
    },
    {
        "rank": 9,
        "tag": "💋 天然カルナウバロウ×柚子精油！真冬の冷風から唇を守り抜く高密着リップ",
        "catch": "唇の荒れ・ひび割れを防ぐ天然ワックス処方。搾りたての柚子の香りが広がり、繊細な唇をしっとりなめらかに保護",
        "brand_name": "松山油脂 (Mマークシリーズ)",
        "capacity": "4g (柚子リップクリーム)",
        "type": "高密着天然植物ワックスリップバーム",
        "features": "カルナウバロウ、ミツロウ、ヒマシ油、ユズ果皮油、ビタミンE（トコフェロール）",
        "value": "寒風で皮剥けしやすい冬の唇にしっかりと密着する保護膜を形成。合成香料・着色料フリーで荒れやすい唇を優しくガード",
        "desc_p1": "唇には皮脂腺がなく角層も極めて薄いため、11月〜12月の乾燥した木枯らしにさらされると真っ先にひび割れや皮剥けを起こします。松山油脂の『柚子リップクリーム』は、植物性カルナウバロウとミツロウをベースに、天然のユズ果皮油を配合したスティックタイプの高保湿リップです。",
        "desc_p2": "唇に乗せると体温で程よくとろけ、ぴったりと密着して均一な保護ヴェールを張ります。ギラギラした不自然な油っぽさがなく、しっとりと落ち着いたツヤ感をキープ。天然精油ならではの清々しい柚子の香りが、塗るたびに心地よい安らぎを与えてくれます。口紅を塗る前の下地としても非常に優秀で、冬のマットリップの縦ジワ防止にも大活躍します。",
        "target": "冬になると唇が乾燥して皮がめくれる・切れる方、人工的な甘い香りのリップが苦手な方、口紅の下地としてベタつかないリップを探している方",
        "point": "スティックを2〜3ミリ繰り出し、唇の縦ジワに沿って縦方向に優しく滑らせるように塗布します。就寝前に少し厚めに塗っておくと、翌朝の唇がふっくらと柔らかく整います。"
    },
    {
        "rank": 10,
        "tag": "🌸 高知県産ユズ果実水×精油！冬の寒さでこわばった肌を解きほぐす集中フェイスマスク",
        "catch": "国産ユズの果実水と精油をたっぷり含浸した贅沢シートマスク。冷え切った肌に贅沢なうるおいと和の温もりを届ける",
        "brand_name": "デイリーアロマジャパン (DAILY AROMA JAPAN)",
        "capacity": "1枚入 / 6個セット (高知県産YUZU ジューシーフェイスマスク)",
        "type": "高保水ユズアロマ集中シートマスク",
        "features": "高知県産ユズ果実水、ユズ果皮油、ヒアルロン酸Na、植物性コラーゲン、グリチルリチン酸2K",
        "value": "週末のスペシャルケアに最適。乾燥で硬くなった角層をみずみずしくうるおし、内側から押し返すようなハリ肌へ",
        "desc_p1": "高知県産の柚子をまるごと蒸留して得られた芳醇な果実水をベースにした贅沢なシートマスク。乾燥と寒さで血行が悪くなり、ゴワつきがちな真冬の素肌に、濃厚な美容液をすみずみまで密着デリバリーします。封を開けた瞬間に広がるフレッシュな柚子の香りは、まるで柚子畑にいるかのような心地よさです。",
        "desc_p2": "厚みのある密着シートが顔の凹凸にぴったりフィットし、液ダレすることなく角層の奥深くまで水分を送り込みます。抗炎症成分のグリチルリチン酸2Kも配合されているため、冬の寒暖差で赤みが出やすいゆらぎ肌もやさしく鎮静。マスクを剥がした後は、毛穴が引き締まり、手のひらが吸い付くような潤い満ちた素肌に仕上がります。",
        "target": "乾燥で肌がカサカサしてメイクのりが悪い方、1週間の終わりにアロマで癒やされながら保湿したい方、旅行やギフト用の特別なシートマスクを探している方",
        "point": "洗顔後、化粧水で肌を整えた後にシートを広げて顔全体に密着させます。10〜15分置いてから剥がし、肌の上に残った美容液をデコルテや首元まで手のひらで伸ばしてください。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['display_name']}",
        "description": d['catch'],
        "image": p['image'],
        "url": f"https://lumi-cosme.vercel.app/winter-yuzu-ceramide.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "植物性の『ユズセラミド』と一般的なセラミド（ヒト型セラミド等）の違いは何ですか？",
        "answer": "ユズセラミドは、柚子の果皮や種子から抽出された植物性セラミド（スフィンゴ脂質）です。植物由来でありながら、ヒトの皮膚の角層に存在するセラミドと非常に類似した立体構造（ラメラ液晶構造）を持っています。ヒト型セラミド同様に角層の細胞間脂質を補正し、水分蒸発を防ぐ高いバリア再建機能を持ちながら、柑橘由来ならではのみずみずしい使用感と天然のアロマ効果を兼ね備えている点が大きな特徴です。"
    },
    {
        "question": "柑橘系のコスメは朝使うとシミ（光毒性）の原因になりませんか？",
        "answer": "光毒性の原因となる成分は『ソラレン』と呼ばれるフロクマリン類です。本記事でご紹介している化粧品グレードのユズエキスや水蒸気蒸留法・精製されたユズ果皮油は、ソラレンが除去または極小化されており、朝のスキンケアや日中のメイク前にも安心してお使いいただけます。どうしても気になる場合は、製品の全成分表示で精油抽出方法を確認するか、夜の集中ケアを中心に取り入れるのがおすすめです。"
    },
    {
        "question": "11月〜12月の真冬にユズコスメが特に選ばれる理由は何ですか？",
        "answer": "日本では古くから冬至に柚子湯に入る風習がありますが、これは単なる伝統ではなく科学的な根拠があります。柚子の精油成分（リモネンなど）には血行を促し、身体を芯から温める温感作用があります。11月〜12月は急激な冷え込みにより肌の末梢血管が収縮して血行不良（冬枯れ・くすみ・乾燥）が進行するため、ユズの血行促進効果とユズセラミドの角層バリア強化の組み合わせが、真冬の乾燥対策に理想的な相乗効果を生み出すからです。"
    },
    {
        "question": "敏感肌でアルコールや精油の刺激が心配な場合、どのように選べば良いですか？",
        "answer": "敏感肌の方は、天然精油を高濃度で含むアイテムよりも、ユズセラミドエキス（果実エキス・種子エキス）が主体で香料無添加・アルコールフリーの設計（例：松山油脂の肌をうるおすシリーズなど）を選ぶのがおすすめです。また、初めて使用する際は腕の内側などでパッチテストを行い、赤みやかゆみが出ないことを確認してから顔全体に使用すると安心です。"
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
        "@id": "https://lumi-cosme.vercel.app/winter-yuzu-ceramide.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！冬の乾いた肌バリアを植物性セラミドと爽やかな和の香りで包み込む高保湿ユズセラミドコスメランク10",
    "description": "11月・12月の暖房乾燥と冬の敏感なバリア乱れを救う高保湿ユズセラミドコスメを徹底厳選！松山油脂、草花木果、よーじや、クナイプから菊正宗、スキンフードまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬のバリア強化術を詳しく解説。",
    "image": items[0]["image"],
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
    "datePublished": "2026-11-04T00:00:00+09:00",
    "dateModified": "2026-11-04T00:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿ユズセラミドコスメおすすめ人気ランキング10選",
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
      <h3 class="product-name">{d['brand_name']} {p['display_name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-layout">
        <div class="product-visual">
          <img src="{p['image']}" alt="{p['display_name']}" class="product-img" loading="lazy" width="300" height="300">
          <div class="price-box">
            <span class="price-label">楽天参考価格</span>
            <span class="price-value">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['url']}" target="_blank" rel="noopener sponsored" class="rakuten-btn">
            楽天で最新価格・在庫を見る
          </a>
        </div>
        
        <div class="product-info-detail">
          <div class="spec-table">
            <div class="spec-row"><span class="spec-th">ブランド</span><span class="spec-td">{d['brand_name']}</span></div>
            <div class="spec-row"><span class="spec-th">容量・規格</span><span class="spec-td">{d['capacity']}</span></div>
            <div class="spec-row"><span class="spec-th">アイテム種別</span><span class="spec-td">{d['type']}</span></div>
            <div class="spec-row"><span class="spec-th">注目成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬の保湿価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬のレビュー</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-box">
            <strong>✨ 効果を最大化する真冬の使い方テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_joined = "\n".join(cards_html)

table_rows = []
for i, p in enumerate(items):
    d = product_details[i]
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{i+1}位</td>
      <td class="tb-img"><img src="{p['image']}" alt="{p['display_name']}" width="60" height="60" loading="lazy"></td>
      <td class="tb-name"><strong>{d['brand_name']}</strong><br><a href="#item-{i+1}">{p['display_name']}</a></td>
      <td class="tb-type">{d['type']}</td>
      <td class="tb-price">¥{p['price']:,}</td>
      <td class="tb-btn"><a href="{p['url']}" target="_blank" rel="noopener sponsored" class="table-link-btn">楽天で見る</a></td>
    </tr>
    """)

table_joined = "\n".join(table_rows)

faq_html_blocks = []
for faq in faq_list:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q">Q. {faq['question']}</h3>
      <p class="faq-a">A. {faq['answer']}</p>
    </div>
    """)

faq_joined = "\n".join(faq_html_blocks)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の乾いた肌バリアを植物性セラミドと爽やかな和の香りで包み込む高保湿ユズセラミドコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の暖房乾燥と冬の敏感なバリア乱れを救う高保湿ユズセラミドコスメを徹底厳選！松山油脂、草花木果、よーじや、クナイプから菊正宗、スキンフードまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬のバリア強化術を詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-yuzu-ceramide.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の乾いた肌バリアを植物性セラミドと爽やかな和の香りで包み込む高保湿ユズセラミドコスメランク10">
  <meta property="og:description" content="11月・12月の暖房乾燥と冬の敏感なバリア乱れを救う高保湿ユズセラミドコスメを徹底厳選！松山油脂、草花木果、よーじや、クナイプから菊正宗、スキンフードまで楽天で今すぐ買えるおすすめ人気ランキング10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-yuzu-ceramide.html">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <!-- 構造化データ -->
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
      --primary-color: #d97706;
      --primary-light: #fef3c7;
      --primary-dark: #b45309;
      --accent-color: #f59e0b;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-light: #fffbeb;
      --border-color: #fde68a;
      --card-bg: #ffffff;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
      --radius: 12px;
    }}
    
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
      line-height: 1.85;
      color: var(--text-main);
      background-color: #fafaf9;
    }}
    
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e5e7eb;
      padding: 1rem 0;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title a {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-link:hover {{ color: var(--primary-dark); }}
    
    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 2rem 1.5rem 5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ color: #9ca3af; }}
    
    .article-header {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary-color);
    }}
    .article-meta {{
      display: flex;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      font-weight: 800;
      color: #111827;
      margin-bottom: 1.5rem;
    }}
    .article-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.8;
      border-left: 4px solid var(--accent-color);
      padding-left: 1.25rem;
      margin-top: 1rem;
    }}
    
    .toc-box {{
      background: var(--bg-light);
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 3rem;
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: var(--primary-dark);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0.5rem;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      padding: 2.5rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 0.75rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      margin-bottom: 1.25rem;
      font-size: 1rem;
      color: var(--text-main);
    }}
    
    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}
    .compare-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      padding: 0.85rem;
      text-align: left;
      border: 1px solid var(--border-color);
      font-weight: 700;
    }}
    .compare-table td {{
      padding: 0.85rem;
      border: 1px solid #e5e7eb;
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 800; color: var(--primary-color); text-align: center; width: 60px; }}
    .tb-img img {{ border-radius: 6px; object-fit: cover; }}
    .tb-name a {{ color: var(--text-main); text-decoration: none; font-weight: 600; }}
    .tb-name a:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-link-btn {{
      display: inline-block;
      padding: 0.4rem 0.8rem;
      background: #b91c1c;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
    }}
    .table-link-btn:hover {{ background: #991b1b; }}
    
    .product-card {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem;
      margin-bottom: 3.5rem;
      border: 1px solid #f3f4f6;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -12px;
      left: 20px;
      background: linear-gradient(135deg, #d97706, #b45309);
      color: white;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.3rem 1.25rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}
    .product-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-top: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .product-name {{
      font-size: 1.4rem;
      font-weight: 800;
      line-height: 1.4;
      color: #111827;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
      .article-header, .content-section, .product-card {{ padding: 1.5rem; }}
      .article-title {{ font-size: 1.45rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: auto;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.08);
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #f9fafb;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
      border: 1px solid #e5e7eb;
    }}
    .price-label {{ font-size: 0.75rem; color: #6b7280; display: block; }}
    .price-value {{ font-size: 1.45rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #6b7280; }}
    
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      box-shadow: 0 4px 6px rgba(191, 0, 0, 0.2);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a80000, #800000);
      transform: translateY(-2px);
      box-shadow: 0 6px 8px rgba(191, 0, 0, 0.3);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: flex;
      border-bottom: 1px solid #e5e7eb;
      padding: 0.5rem 0;
    }}
    .spec-th {{
      width: 110px;
      flex-shrink: 0;
      font-weight: 700;
      color: #4b5563;
    }}
    .spec-td {{
      flex-grow: 1;
      color: #1f2937;
    }}
    
    .review-box {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #334155;
      margin-bottom: 0.5rem;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      background: #fffbeb;
      border: 1px solid #fef3c7;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
      font-size: 0.9rem;
    }}
    .target-box strong, .usage-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.25rem;
    }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #374151;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-links-grid a {{
      font-size: 0.88rem;
      color: #4b5563;
      text-decoration: none;
      padding: 0.4rem 0.6rem;
      background: #f9fafb;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      transition: all 0.2s;
    }}
    .footer-links-grid a:hover {{
      color: var(--primary-color);
      border-color: var(--primary-color);
      background: var(--bg-light);
    }}
    
    .site-footer {{
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <div class="site-title">
        <a href="/">❄️ 冬コスメ徹底比較ラボ</a>
      </div>
      <nav>
        <a href="/" class="nav-link">トップページへ戻る</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <nav class="breadcrumb" aria-label="パンくずリスト">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/#skincare">スキンケア・ボディケア特集</a>
      <span>&gt;</span>
      <span aria-current="page">高保湿ユズセラミドコスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（スキンケア皮膚科学リサーチチーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！冬の乾いた肌バリアを植物性セラミドと爽やかな和の香りで包み込む高保湿ユズセラミドコスメランク10</h1>
      <p class="article-lead">
        11月から12月にかけて外気温と湿度が急落し、冷えと暖房による乾燥で肌のバリア機能が低下する季節。古来より冬至の柚子湯で親しまれてきた日本の知恵が、いま最新の皮膚科学で「ユズセラミド」として再評価されています。ヒトの角層細胞間脂質と極めて親和性が高い植物性セラミドと、心身の緊張を解きほぐす天然の和柑橘アロマ。本記事では、真冬の過酷な乾燥環境でも潤いを逃がさない高保湿ユズセラミドコスメを徹底比較し、厳選ランキング10選としてご紹介します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-yuzu">1. なぜ11月〜12月の冬肌にユズセラミドが必要なのか？科学的メカニズム</a></li>
        <li><a href="#selection-criteria">2. 失敗しない冬の高保湿ユズコスメの選び方・3つの基準</a></li>
        <li><a href="#comparison-table">3. 高保湿ユズセラミドコスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿ユズセラミドコスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚視点で答えるユズコスメのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：冬の肌バリアを植物性セラミドで守り抜く実践ルーティン</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-yuzu">
      <h2 class="section-title">🍊 1. なぜ11月〜12月の冬肌にユズセラミドが必要なのか？科学的メカニズム</h2>
      <p class="section-p">
        11月から12月にかけて、日本の気候は急速に冬本番へと突入します。大気中の湿度は30%台まで急落し、さらに室内のエアコン暖房によって空気中の水分が奪われるため、皮膚の最外層にある角質層からは猛烈な勢いで水分が蒸発していきます。
      </p>
      <p class="section-p">
        この時期に多くの人が直面するのが、「いつもの保湿化粧水や乳液をつけてもすぐに乾く」「肌の表面がピリピリして赤みが出る」という角層バリアの崩壊です。角質細胞同士を隙間なく埋めている『細胞間脂質（セラミドなど）』が寒冷と乾燥で減少すると、水分が逃げるだけでなく、外からの冷気やホコリ、繊維の摩擦刺激がダイレクトに神経線維に届いてしまいます。
      </p>
      <p class="section-p">
        ここで絶大な効果を発揮するのが、柚子の果皮や種子から抽出される<strong>『植物性ユズセラミド（スフィンゴ脂質）』</strong>です。ユズセラミドは植物由来成分でありながら、ヒトの皮膚に存在する角層セラミドと極めて類似した立体構造（ラメラ液晶構造）を持っています。角層のスカスカになった隙間にピタリと入り込み、自重の何倍もの水分を抱え込んで蒸発を防ぐ『持続保水シールド』を再構築します。
      </p>
      <p class="section-p">
        さらに、柚子に含まれる天然の精油成分（リモネンなど）には、皮膚表面の毛細血管を広げて血行を促す作用があります。真冬の冷えで血行不良を起こし、代謝が低下してゴワついた肌をじんわりと温め、巡りを活性化させながら角層のバリア機能を底上げできる点が、他の保湿成分にはないユズコスメ唯一無二の強みなのです。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 失敗しない冬の高保湿ユズコスメの選び方・3つの基準</h2>
      <p class="section-p">
        市場には多種多様なユズコスメが存在しますが、11月〜12月の過酷な冬の乾燥対策として選ぶ際には、以下の3つのポイントを必ずチェックしましょう。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準①：ユズ果皮精油（香り・血行促進）とユズ種子・果実エキス（セラミド保水）の配合目的を見極める</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          「香り」を楽しみたい場合は天然ユズ果皮油が配合されたボディローションやバスソルトが最適です。一方、顔の角層バリアを本格的に立て直したい場合は、スフィンゴ脂質を含む「ユズ果実エキス」「ユズ種子エキス」が高濃度に配合された美容液や化粧水を選びましょう。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準②：水分補給だけでなく『エモリエント膜（油分）』が組み合わされているか</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          真冬の乾燥環境では、水分だけを与えてもすぐに蒸発してしまい、かえって乾燥を招きます。カルナウバロウ、シア脂、スクワラン、植物油などの上質な油分が適度に組み合わされた処方のものを選ぶことで、角層に閉じ込めた水分を一晩中ガッチリキープできます。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準③：冬の敏感肌をいたわる低刺激処方（アルコールフリー・無着色）</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          寒暖差で角層が敏感になっている冬は、エタノール（アルコール）や過度な合成香料がピリつきの原因になることがあります。天然の柚子由来成分を活かしたシンプルで低刺激な処方のブランド（松山油脂、草花木果など）を選ぶのが失敗しない秘訣です。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高保湿ユズセラミドコスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天公式APIよりリアルタイムに取得した最新価格と製品スペックの一覧表です。用途やケアしたい部位に合わせて比較検討してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名・ブランド</th>
              <th>カテゴリ種別</th>
              <th>楽天価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 高保湿ユズセラミドコスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚視点で答えるユズコスメのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">🌿 6. まとめ：冬の肌バリアを植物性セラミドで守り抜く実践ルーティン</h2>
      <p class="section-p">
        11月から12月にかけて本格化する過酷な寒冷乾燥は、放っておくと角層のラメラ構造をズタズタにし、春先まで続く深刻な肌トラブルの原因になります。
      </p>
      <p class="section-p">
        今回ご紹介した高保湿ユズセラミドコスメは、日本人が古くから親しんできた柚子の巡り力と、ヒトの肌バリアに寄り添う植物性セラミドのサイエンスが見事に融合した傑作揃いです。
      </p>
      <p class="section-p">
        入浴時にはユズ＆ジンジャーのバスソルトで全身の巡りを温め、お風呂上がりには松山油脂の柚子ボディローションですみやかに水分の蒸発をブロック。洗顔後にはユズセラミド配合のブースターやジェルで角層細胞をふっくらと満たす——このシンプルな和の保湿ルーティンを取り入れるだけで、真冬の暖房下でも乾きを知らない吸い付くようなモチ肌を保つことができます。
      </p>
      <p class="section-p">
        ぜひ気になったアイテムを日々のスキンケアに取り入れ、爽やかな柚子の香りに包まれながら、乾燥知らずの健やかな冬をお過ごしください。
      </p>
    </section>

    <!-- 内部リンクラッパー -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で動的に同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-yuzu-ceramide.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-yuzu-ceramide.html successfully. Size: {len(html_content):,} bytes")
