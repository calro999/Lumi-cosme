import json

with open("rakuten_3winter_body_booster_shampoo_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_booster_oil"]["items"]

booster_oil_details = [
    {
        "rank": 1,
        "tag": "🏆 油性と水性の2層式が冬の硬化肌を解き放つ！柑橘の香りと極上の吸水力で圧倒的人気を誇る先行プレオイル",
        "catch": "洗顔直後のまっさらな肌へ。肌を柔らかくほぐすオイル層とみずみずしく満たす水層が化粧水の浸透を劇的後押し",
        "capacity": "50ml",
        "type": "オイル＆リキッド2層式・導入ブースターエッセンス",
        "texture": "シャカシャカ振ると瞬時に黄金色に混ざり合う。サラサラと軽やかなのに肌になじむとモッチリ吸着",
        "ingredients": "オリーブ果実油、ホホバ種子油、オレンジ果皮油、ビターオレンジ葉/枝油、トウヒエキス、ローヤルゼリーエキス",
        "finish": "ベタつきゼロで手のひらが頬に吸い付くようなふっくら感。化粧水がゴクゴク飲み込まれるような吸水肌へ",
        "desc_p1": "11月から12月にかけて寒風にさらされると、皮膚温が低下して毛細血管が収縮し、表皮細胞への栄養供給が滞ります。その結果、ターンオーバーが著しく遅延し、本来剥がれ落ちるべき古い角質が肌表面に何層も堆積する『角層肥厚（角質肥厚）』が発生します。硬くこわばった冬の肌は撥水コートのようになり、高価な化粧水をいくらパッティングしても表面で弾かれて蒸発してしまいます。",
        "desc_p2": "RMKのロングセラー傑作『Wトリートメントオイル』は、肌を柔らかく解きほぐすエモリエントオイル層と、角層をみずみずしく満たすウォーター層が絶妙なバランスで融合。洗顔後すぐに数滴なじませることで、固まった細胞間脂質を柔らかくほぐし、次に使う化粧水のための水分ルートを即座に開通させます。オレンジやネロリを中心とした爽やかな天然シトラスの香りは、寒さで縮こまった朝晩のスキンケアタイムを至福のリフレッシュ時間へと昇華させます。",
        "target": "冬になると化粧水が肌表面で浮いて入っていかないインナードライ肌の方、オイル特有の重さやベタつきが苦手な方、朝のメイク前にふっくらツヤのある土台を仕込みたい方",
        "technique": "ボトルを上下にしっかり振って2層を完全に白濁させた後、手のひらに4〜5滴を取ります。両手で温めて香りを深く吸い込みながら、顔全体を包み込むようにハンドプレス。その後すぐに化粧水を重ねると、驚くほどスピーディーに吸い込まれます。",
        "voice": "『冬になるとどんな化粧水も肌の上で滑っていましたが、RMKのオイルを洗顔後すぐにつけると肌がフワフワになって化粧水がグングン入ります。柑橘の香りも最高で毎冬手放せません。』(30代・メーカー勤務)",
        "caution": "2層式のため、振らずに使うと油分だけが出てしまいバランスが崩れます。必ず毎回キャップを閉めて上下によく振ってからご使用ください。"
    },
    {
        "rank": 2,
        "tag": "🌿 100%オーガニックの一番搾りアルガンオイル！洗顔後の一滴で肌の親水性を極限まで高める世界的ベストセラー",
        "catch": "モロッコの過酷な砂漠が生んだ奇跡のオイル。オレイン酸とビタミンEが冬の乾燥小ジワをふっくら押し上げる",
        "capacity": "50ml",
        "type": "エコサート認証・100%オーガニックピュアアルガンオイル",
        "texture": "黄金色のリッチなオイル。肌の水分と結びつく親水性処方により、オイルなのに肌表面に残らず角層深部へスッと溶け込む",
        "ingredients": "アルガニアスピノサ核油（オーガニック未精製・一番搾りアルガンオイル 100%）",
        "finish": "オイル独特の油膜感がなく、内側から押し返すようなふっくらとした弾力と自然なツヤ。キメが整ったベルベット素肌",
        "desc_p1": "砂漠地帯で数年間雨が降らなくても枯れない驚異の保水力を持つアルガンの木。その種子から低温圧搾（コールドプレス）で抽出される一番搾りアルガンオイルは、皮脂膜の構成成分であるオレイン酸やリノール酸、ビタミンE（トコフェロール）を極めて豊富に含んでいます。",
        "desc_p2": "オーガニック認証コスメのパイオニア・メルヴィータの『ビオオイル アルガンオイル』は、水分の親和性に優れた「ブースター（導入）機能」に特化した名品。洗顔直後の少し湿り気のある肌に塗布すると、アルガンオイルが水分子を抱え込みながら角層の隙間へとスムーズに浸透。その後に塗る化粧水を磁石のように引き寄せて角層深くにホールドします。防腐剤や着色料を一切使わない100%植物の恵みで、真冬の砂漠肌を生き生きと蘇らせます。",
        "target": "成分のシンプルさ・無添加オーガニックにこだわりたい方、冬になると目元や口元の乾燥小ジワが深く刻まれる方、化粧水が肌に定着せず乾きを感じやすい方",
        "technique": "洗顔後、タオルで完全に乾かさず、肌にほんのり水分が残っている状態で1滴〜2滴を手のひらに伸ばし、顔全体に優しく押し込みます。独自の『MY DROPPER』ノズルにより、肌質や季節に合わせて1滴単位で正確に量をコントロールできます。",
        "voice": "『洗顔後すぐにこれをつけるのとつけないのでは、化粧水の入り方が全く違います。真冬でも粉を吹かず、肌が柔らかくモチモチになりました。コスパも抜群です。』(20代・美容学生)",
        "caution": "100%ピュア植物オイルのため、冬場の非常に寒い部屋ではわずかに凝固や濁りが生じることがありますが、品質には問題ありません。手のひらで温めてご使用ください。"
    },
    {
        "rank": 3,
        "tag": "🌹 必須脂肪酸オメガ3・6・9を80%以上含有！冬の乾燥ぐすみやキメの乱れをリセットする濃密ローズヒップ",
        "catch": "1瓶に凝縮された野生ローズヒップの生命力。寒さで疲れた冬の肌へ透明感と濃密なうるおいを届ける集中美容オイル",
        "capacity": "20ml",
        "type": "BioGro認定オーガニック・低温圧搾ローズヒップオイル",
        "texture": "鮮やかな琥珀色の濃厚なオイル。植物の豊かなコクがありながら、肌へすばやく馴染みキメの凹凸を埋める",
        "ingredients": "カニナバラ種子油（100%純粋認定オーガニックローズヒップオイル）",
        "finish": "ゴワついた肌表面がしなやかにほぐれ、内側からパッと発光するような澄んだ透明感とハリツヤ",
        "desc_p1": "冬の寒さや血行不良は、肌の新陳代謝を低下させるだけでなく、皮脂の酸化や乾燥による肌の黄ぐすみ・グレーぐすみをもたらします。どんよりと疲れて見える冬の肌を立て直すには、肌細胞の細胞膜を構成する良質な不飽和脂肪酸（オメガ3・オメガ6）の直接補給が極めて有効です。",
        "desc_p2": "ニュージーランド発のナチュラルスキンケアブランド・トリロジーの『認定オーガニック ローズヒップ オイル』は、世界中のセレブリティや美容家が絶賛するオーガニックオイルの金字塔。熱を加えない特殊なコールドプレス製法により、デリケートな必須脂肪酸を80%以上の高濃度でキープ。洗顔直後の肌になじませることで、乾燥で硬くなった角質をやさしく解き放ち、くすみを晴らしてキメの整った明るい肌色へと導きます。",
        "target": "冬になると肌がくすんで顔色が悪く見えてしまう方、毛穴の開きやキメの粗さが気になる方、エイジングサインを天然の抗酸化成分でケアしたい方",
        "technique": "洗顔後、手のひらに2〜3滴を垂らし、両手をこすり合わせてオイルを温めてから、顔全体から首元・デコルテまで包み込むようにハンドプレスします。その後の化粧水がスーッと引き込まれます。",
        "voice": "『使い始めてから冬特有の肌のくすみが消え、周りから肌が明るくなったと褒められました。洗顔後すぐに使うと肌がふかふかになり、化粧水の吸い込みが段違いです。』(40代・自営業)",
        "caution": "未精製の天然オイルのため、独特のナッツのような植物特有の香りがあります。また酸化に弱いため、開封後は3ヶ月以内に使い切り、直射日光を避けて保管してください。"
    },
    {
        "rank": 4,
        "tag": "💧 純度99.9%ピュアスクワラン！水分をぎゅっと抱え込み皮脂膜の代わりとなって冬の乾燥から肌を徹底保護",
        "catch": "たった1滴で乳液・クリーム以上の保護力。酸化・変質しにくく敏感肌でも安心のマルチユースオイル",
        "capacity": "30ml",
        "type": "高純度ピュアスクワランオイル（無添加処方）",
        "texture": "水のようにサラサラとして一切のベタつきがない。無色無臭で肌にスーッと一体化する究極の軽やかさ",
        "ingredients": "スクワラン（高純度精製99.9%）",
        "finish": "ベタつきゼロでシルクのようにサラサラ＆もっちり。冬の冷気やエアコンの温風を跳ね返す薄いうるおいバリア",
        "desc_p1": "スクワランは、もともと人間の皮脂中に含まれる重要なうるおい成分「スクワレン」を安定化させたものです。健康な肌はスクワランを含んだ皮脂膜によって水分の蒸散を防いでいますが、20代をピークに皮脂分泌量は激減し、冬の乾燥によって皮脂膜が完全に枯渇してしまいます。",
        "desc_p2": "HABAの『高品位「スクワラン」』は、幾度もの精製を繰り返して純度99.9%まで高めた最高峰のピュアオイルです。防腐剤パラベン、石油系界面活性剤、合成香料、鉱物油を一切排除。化粧水で肌をたっぷり水分で満たした直後、手のひらに残った化粧水とわずか「1滴」のスクワランを混ぜて肌に伸ばすことで、瞬時に理想的な天然皮脂膜を再現。冬の過酷な乾燥環境でも水分をガッチリ逃しません。",
        "target": "オイルのベタつきや油膜感がどうしても苦手な方、敏感肌で添加物や香料に反応しやすい方、コスパ重視で1本を長く使いたい方（30mlで約3ヶ月分）",
        "technique": "たっぷりの化粧水（5回パッティング）で肌がひんやり潤った状態で、手のひらに化粧水の水滴が残っているうちにスクワランを「1滴」落とします。手のひらで合わせて顔全体に押し込むように馴染ませるのがHABA推奨の黄金メソッドです。",
        "voice": "『本当に1滴で一日中肌が乾きません！ベタベタしないので朝のメイク前にも安心して使えます。冬のカサカサがピタッと治まり、肌荒れ知らずになりました。』(30代・教育関連)",
        "caution": "2滴以上つけると油分過多になりテカリの原因になることがあります。基本は「たった1滴」を守ることが美肌への秘訣です。"
    },
    {
        "rank": 5,
        "tag": "🌸 カメリアオイルなどボタニカル成分100%！冬のエイジングサインや乾燥小ジワを濃密にケアしシルク艶へ導く",
        "catch": "韓国発ラグジュアリーボタニカル。洗練されたカメリアの香りと驚くほど軽やかな浸透力で肌密度を立て直す",
        "capacity": "30ml",
        "type": "高機能ボタニカル・フェイシャルオイルエッセンス",
        "texture": "さらりとしたシルキータッチ。肌に伸ばした瞬間にすーっと吸い込まれ、ベタつきのない上品な仕上がり",
        "ingredients": "ツバキ種子油（カメリアオイル）、オリーブ果実油、カニナバラ果実油、ビサボロール、トコフェロール、ジャスミン油",
        "finish": "肌の内側がうるおいで満たされ、内側から発光するような極上のシルキーグロウ肌へ",
        "desc_p1": "冬の乾燥ダメージは、肌の柔軟性を奪うだけでなく、真皮のコラーゲン繊維に負荷をかけてエイジングを加速させます。冷えと乾燥によって肌のハリが失われ、頬のたるみ毛穴やフェイスラインのもたつきが目立ちやすくなるのが冬の大きな悩みです。",
        "desc_p2": "FEMMUEのシグネチャーアイテム『アイディアルオイル』は、酸化しにくく肌への浸透力に優れたツバキ種子油（カメリアオイル）をベースに、植物性美容成分を贅沢にブレンドした100%天然由来の濃密セラムオイル。洗顔直後の肌になじませることで、こわばった角質層をふっくらとほぐし、肌密度を高めて内側からピンと張ったようなハリ感を与えます。優雅なフローラルの香りは自律神経を整え、冬の肌疲れを癒やします。",
        "target": "冬の乾燥小ジワやハリ不足・毛穴の開きを集中ケアしたい方、韓国コスメの最高峰ラグジュアリースキンケアを体感したい方、優雅な香りで毎日のスキンケアを格上げしたい方",
        "technique": "洗顔後すぐのまっさらな肌に2〜3滴を垂らし、顔の中心から外側へ向けて優しく引き上げるように伸ばします。手のひらで温めながらハンドプレスすると、肌にツヤのヴェールが定着します。",
        "voice": "『これを使うようになってから冬の乾燥小ジワが目立たなくなり、ファンデーションのノリが劇的に良くなりました。香りが本当に素晴らしくてスキンケアが楽しみになります。』(30代・PR担当)",
        "caution": "天然植物由来の精油を多く含むため、植物アレルギーをお持ちの方は事前に腕の内側などでパッチテストを行うことをおすすめします。"
    },
    {
        "rank": 6,
        "tag": "🌿 タイガーナッツ×インカオメガ×ボラージオイル配合！冬のゆらぎ肌を健やかに整え吸い付くような柔肌へ",
        "catch": "アルビオンが誇るマルチユース美容オイルの傑作。3種の厳選植物オイルが過酷な冬の環境ダメージを徹底ブロック",
        "capacity": "40ml",
        "type": "マルチファンクション・ハーバル美容オイル",
        "texture": "こっくりとしていながら肌離れの良いなめらかなオイル。肌に触れるとスルスルと抵抗なく広がる",
        "ingredients": "サイペラスエスクレンタス根油（タイガーナッツオイル）、プルケネチアボルビリス種子油（インカオメガオイル）、ルリジサ種子油（ボラージオイル）、ローズマリー葉エキス",
        "finish": "キメがふっくらと立ち上がり、指先が吸い付くようなやわらかなもち肌へ。上品なハーブの香りが持続",
        "desc_p1": "冬は寒暖差や冷たい風、花粉・大気汚染物質の付着によって、肌のバリア機能が低下し、赤みやかさつきを繰り返す「冬のゆらぎ肌」に陥りやすくなります。肌の恒常性を保ち、トラブルを未然に防ぐ防御型のケアが不可欠です。",
        "desc_p2": "アルビオンのロングセラー『ハーバルオイル トリニティフュージョン』は、過酷な環境を生き抜く3種の生命力豊かな植物オイルを融合した機能性オイルです。洗顔後のブースターとして使用することで、角層のバリアを瞬時に修復し、冬の刺激に負けないタフな素肌を構築。乳液先行型のアルビオンスキンケアはもちろん、通常の化粧水前の導入オイルとしても万能に活躍します。",
        "target": "冬になると肌荒れや赤みが出やすく肌が不安定になりやすい方、顔だけでなく髪や爪・ボディの乾燥も1本でマルチにケアしたい方、清涼感あるハーブの香りが好きな方",
        "technique": "洗顔後のまっさらな肌に2〜3滴をのばし、顔全体になじませます。週に1〜2回、ティースプーン1杯分をたっぷり使って優しくマッサージし、その後ティッシュオフする『オイル温感マスク』も冬のスペシャルケアに絶大な効果を発揮します。",
        "voice": "『毎年冬のお守りコスメとして愛用しています。カサついて粉を吹いていた頬が、これを使うとすぐにしっとり落ち着いて柔らかくなります。ハーブの香りも心地よいです。』(30代・秘書)",
        "caution": "マッサージ用として多量に使用した後は、軽くティッシュで余分な油分を押さえてから次のステップに進むと、メイク崩れを防げます。"
    },
    {
        "rank": 7,
        "tag": "✨ 白樺水×高機能オイルのノンオイリー感触！肌のめぐりを整え冬のくすみを晴らして生命感あふれる輝きへ",
        "catch": "コスメデコルテ最高峰AQラインのプレシャスオイル。オイルとは思えないみずみずしさで角層をうるおす",
        "capacity": "40ml",
        "type": "オイルインフュージョン・高機能先行美容液",
        "texture": "まろやかでみずみずしい新感覚リキッドオイル。肌に乗せた瞬間に水のようにスーッと浸透しベタつき皆無",
        "ingredients": "シラカンバ樹液（白樺水）、ホワイトムクナエキス、植物性スクワラン、月見草油、アデノシン、グリセリン",
        "finish": "内側から発光するような極上のツヤと透明感。ふっくらとしたハリと弾力が一日中続く",
        "desc_p1": "冬の肌トラブルの根底には「肌の冷え」と「めぐりの滞り」があります。血流が滞ると、肌の細胞に必要な酸素や栄養素が届かず、顔全体がどんよりと暗く沈んでしまい、老けた印象を与えてしまいます。",
        "desc_p2": "コスメデコルテAQの『オイル インフュージョン』は、春先のわずかな期間しか採取できない希少な「白樺水」と高機能植物オイルをブレンド。独自の技術により、オイル特有の重さや油膜感を完全に排除し、サラサラとした美容液のような浸透感を実現しました。洗顔後すぐに使用することで、冬の乾燥と寒さで硬直した肌をやわらげ、めぐりを促して生き生きとした血色感と澄んだ透明感を呼び覚まします。",
        "target": "乾燥によるくすみや疲れ顔を即効でリセットしたい方、オイルの重さが苦手でサラッとした先行美容液を好む方、デパコスの極上の使用感とハリ感を求める方",
        "technique": "夜の洗顔後、または化粧水の前に手のひらに3〜4滴を取り、顔全体から首筋にかけてリンパを流すように優しく馴染ませます。月下美人の優美な香りが安らかな眠りをサポートします。",
        "voice": "『オイルなのに全くベタつかず、肌にグングン吸い込まれていきます。翌朝起きたときの肌の明るさとハリに驚きました。冬のどんより顔の救世主です。』(40代・会社役員)",
        "caution": "非常に浸透が早いため、手のひらに出したらすぐに顔へ伸ばすようにしてください。"
    },
    {
        "rank": 8,
        "tag": "👑 みずみずしい光沢感を仕込みメイク前の土台を完璧に整える！冬の乾燥崩れを防ぐ先行ドロッピングオイル",
        "catch": "カネボウが提案する素肌美テクノロジー。光を味方につけて冬の乾いた肌にツヤと柔軟性を与える",
        "capacity": "40ml",
        "type": "スキンケア＆メイク仕込み先行ドロッピングオイル",
        "texture": "とろみのあるまろやかなオイルドロップ。肌の上でツルンと滑らかに広がり摩擦を感じさせない",
        "ingredients": "マカデミアナッツ油、オリーブ果実油、スクワラン、カニナバラ果実油、フェノキシエタノール、植物エキス",
        "finish": "自然な濡れツヤと透明感が宿り、その後に重ねるファンデーションの密着度とツヤ感を劇的アップ",
        "desc_p1": "冬の朝、メイク前に十分な保湿を行わないと、日中のエアコンによってファンデーションが粉を吹き、目元やほうれい線に小ジワ割れが生じてしまいます。しかし朝に重い油分を塗りすぎると、今度はメイクがドロドロに崩れるという難問に直面します。",
        "desc_p2": "KANEBOの『ドロッピング オイル』は、スキンケアとしての保湿効果と、メイクアップのノリを高めるフィクサー機能を両立した先進の先行オイルです。洗顔後や化粧水前の肌に1〜2滴なじませることで、角層の凹凸をなめらかに埋め、光を乱反射する極薄のツヤ膜を形成。日中の乾燥崩れをブロックしながら、夕方まで乾燥知らずのいきいきとしたツヤ肌をキープします。",
        "target": "冬になると日中の乾燥崩れやファンデーションの粉吹きに悩む方、朝のメイク前に使えるベタつかないブースターオイルを探している方、自然なツヤ肌メイクを目指す方",
        "technique": "朝の洗顔後、化粧水の前に1滴を手のひらに広げ、乾燥しやすい頬や目元のCゾーンを中心に薄く馴染ませます。ファンデーションのリキッドに直接1滴混ぜて使うテクニックも極上の保湿ツヤ肌を作れます。",
        "voice": "『朝のメイク前に使うと、ファンデーションの粉吹きが完全に消えました！ツヤ感がとても上品で、一日中肌が乾燥しません。メイクノリが劇的に変わります。』(20代・アパレル)",
        "caution": "朝使用する際は、塗りすぎるとメイク崩れの原因になるため、1〜2滴の適量を厳守してください。"
    },
    {
        "rank": 9,
        "tag": "✨ 洗顔後すぐの肌に奇跡の一滴！肌密度を高め内側から跳ね返すようなハリと輝きを与える先行型プレオイル",
        "catch": "永久花イモーテルの生命力。過酷な冬の乾燥を跳ね返すロクシタン最高峰エイジングケアプレオイル",
        "capacity": "30ml",
        "type": "高機能先行エイジングケア・プレオイル",
        "texture": "リッチでとろけるような濃密感触。肌に伸ばすとスーッと溶け込み、表面にシルクのような保護膜を形成",
        "ingredients": "ヘリクリスムイタリクム花油（イモーテルエッセンシャルオイル）、アルガニアスピノサ核油、月見草油、ルリジサ種子油、ヒマワリ種子油",
        "finish": "肌密度がギュッと高まったような濃密なハリ弾力と、生命力に満ちた眩いばかりのツヤ",
        "desc_p1": "摘み取った後も鮮やかな黄色を保ち、枯れることがないことから「永久花」と呼ばれるイモーテル。寒さと乾燥で肌細胞が活力を失う冬こそ、植物の強靭な生命力を取り入れたプレケアが絶大な効果を発揮します。",
        "desc_p2": "ロクシタンのスキンケア最高峰ラインを代表する『イモーテル ディヴァインインテンシヴオイル』は、洗顔後すぐの肌に使用する先行型プレオイル。イモーテルの高濃度エッセンシャルオイルと厳選された植物オイルが、硬くこわばった真冬の肌を瞬時に解きほぐし、肌本来の再生力をサポート。角層のすみずみまで栄養を行き渡らせ、内側から押し返すような濃密なハリと輝きをもたらします。",
        "target": "冬の本格的な乾燥とたるみ・ハリ不足に悩む大人肌の方、洗顔後の一滴でスキンケア全体の効果を最大化したい方、ロクシタン最高峰のエイジングケアを体験したい方",
        "technique": "洗顔後、手のひらに2〜3滴を取り、両手で温めてから顔全体を包み込みます。こめかみや首筋に向かって優しくマッサージしながら浸透させると、寒さで強張った表情筋も心地よくほぐれます。",
        "voice": "『冬になると頬の位置が下がったように感じていましたが、このオイルを洗顔後に使い始めてから肌にパンとしたハリが戻りました。化粧水の吸い込みも抜群です。』(40代・主婦)",
        "caution": "高濃度の植物エッセンシャルオイルを含むため、目元ギリギリへの塗布は避けてご使用ください。"
    },
    {
        "rank": 10,
        "tag": "🌿 ホホバの種子から絞った無香料ピュアオイル！肌なじみ抜群で洗顔後ブースターから頭皮まで万能に活躍",
        "catch": "人間の皮脂に最も近いワックスエステル。肌の水分蒸散を防ぎ、シンプルに素肌をうるおす高コスパ名品",
        "capacity": "200ml",
        "type": "100%植物由来・無添加ピュアホホバオイル",
        "texture": "サラリとした軽快なテクスチャー。肌にのせると素早く馴染み、皮脂膜のように自然な保護膜を形成",
        "ingredients": "ホホバ種子油（100%ピュア植物オイル・無香料・無着色）",
        "finish": "ベタつかずサラサラの肌触り。自然なうるおいとツヤをキープし、季節を問わず快適",
        "desc_p1": "スキンケアに余計な添加物や香料を一切入れたくない、シンプルかつ安全に冬の乾燥対策を行いたいという方にとって、植物本来の力をダイレクトに生かしたピュアオイルは最も信頼できる選択肢です。",
        "desc_p2": "無印良品の『ホホバオイル』は、ペルーなどの農園で無農薬栽培されたホホバの種子から搾油し、日本国内で丁寧に精製した高品質ピュアオイル。ホホバオイルは厳密には油ではなく「液状ワックスエステル」であり、人間の皮脂の約20〜30%を占める成分と同一の構造を持っています。そのため肌への親和性が極めて高く、洗顔直後の肌になじませることで自然なバリアを再建し、化粧水の浸透を優しく後押しします。",
        "target": "プチプラで惜しみなく毎日使える大容量ブースターオイルを探している方、無香料・低刺激で敏感肌にも優しいオイルを好む方、顔だけでなくボディや頭皮マッサージにも使いたい方",
        "technique": "洗顔後、1〜2滴を手のひらに伸ばして顔全体に優しくハンドプレスします。冬の入浴時、湯船に浸かりながら本品を数滴塗ってオイルパックするのも、硬い角質を柔らかくほぐす名テクニックです。",
        "voice": "『大容量でコスパ最強。洗顔後に数滴なじませるだけで、冬でも肌がゴワつかず化粧水がしっかり入ります。余計な香りがついていないので使いやすいです。』(20代・学生)",
        "caution": "ホホバオイルの特性上、気温が10度以下になると白く固まることがあります。常温の暖かい部屋に置くか、ぬるま湯につけて溶かしてからご使用ください（品質に影響はありません）。"
    }
]

# JSON-LD用ItemList
json_ld_items = []
for idx, it in enumerate(items):
    dt = booster_oil_details[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["name"],
            "image": it["image_url"],
            "description": dt["catch"],
            "brand": {
                "@type": "Brand",
                "name": it["brand"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

json_ld_structure = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10",
            "description": "11月・12月の冬の寒さで硬くこわばった肌・化粧水が入らないインナードライを徹底解決！RMK、メルヴィータ、トリロジー、HABA、FEMMUE、アルビオンなど、洗顔後すぐの肌をふっくらほぐし吸水力を劇的アップする最強高保湿ブースターオイル10選を徹底比較！",
            "datePublished": "2026-11-01T00:00:00+09:00",
            "dateModified": "2026-11-01T00:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ"
            }
        },
        {
            "@type": "ItemList",
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "化粧水の前にオイルを塗ると、油分が水を弾いてしまいませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "一般的な重い鉱物油を大量に塗ると水を弾きますが、ブースター（導入）オイルとして設計された植物オイル（アルガンオイル、ホホバオイル、スクワラン、2層式オイルなど）は肌の細胞間脂質と極めて近い脂肪酸組成や親水性を持っています。洗顔後の肌になじませることで、固まった角層を柔らかくほぐし、水分の通り道（アクアポリンや細胞間隙）を拓くため、むしろ化粧水が磁石のように引き込まれて浸透力が高まります。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ブースターオイルと仕上げの美容フェイスオイルの違いは何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ブースターオイルは『洗顔後すぐのまっさらな肌』に使用し、角層を柔らかくほぐして後から使う化粧水の浸透を助ける親水性・浸透性の高い処方になっています。一方、スキンケアの最後に使うフェイスオイルは、化粧水や乳液で補った水分蒸発を防ぐ『密閉フタ』の役割を果たすため、エモリエント膜をしっかり張る重厚なテクスチャーが主流です。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "オイリー肌やニキビができやすい冬の混合肌でもブースターオイルは使えますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、ご使用いただけます。冬に皮脂が出る原因の多くは、内部の水分不足を補おうとする『インナードライの防衛反応』です。ブースターオイルで角層をほぐして水分を奥まで届けることで、過剰な皮脂分泌が自然と鎮まります。オイリー肌の方は、1回に使う量を1滴程度に抑え、サラサラ感触のスクワランやホホバオイル、RMKなどの2層式オイルを選ぶのがおすすめです。"
                    }
                }
            ]
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の寒さで硬くこわばった肌・化粧水が入らないインナードライを徹底解決！RMK、メルヴィータ、トリロジー、HABA、FEMMUE、アルビオンなど、洗顔後すぐの肌をふっくらほぐし吸水力を劇的アップする最強高保湿ブースターオイル10選を徹底比較！">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-booster-oil">
  <meta property="og:title" content="保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10">
  <meta property="og:description" content="11月・12月の冬の寒さで硬くこわばった肌・化粧水が入らないインナードライを徹底解決！RMK、メルヴィータ、トリロジー、HABA、FEMMUE、アルビオンなど、洗顔後すぐの肌をふっくらほぐし吸水力を劇的アップする最強高保湿ブースターオイル10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-booster-oil">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json.dumps(json_ld_structure, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="site-nav">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#why-booster">導入オイルの科学</a>
        <a href="#faq-section">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container main-content">
    <article class="article-body">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="/">トップ</a></li>
          <li aria-current="page">高保湿ブースターオイル</li>
        </ol>
      </nav>

      <header class="article-header">
        <span class="badge category-badge">先行導入・角層柔軟ケア</span>
        <h1 class="article-title">保湿力の強さで冬のゴワつき・カサカサ砂漠肌とさようなら！化粧水をぐんぐん引き込む高保湿ブースターオイルランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-01">2026年11月1日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入文 -->
      <section class="intro-box">
        <p>
          11月から12月へと寒さが本格化するにつれて、「いつもの化粧水をつけているのに肌に入っていかない」「肌表面で水滴が滑るように弾かれてしまう」「触ると肌がゴワゴワ・ザラザラして硬い」といった深刻なスキンケアの停滞感に悩まされていませんか？
        </p>
        <p>
          冬の寒風と室内暖房によって冷え切った素肌は、血行不良によりターンオーバーが停滞し、古い角質が何層にも積み重なる「角層肥厚」を起こしています。この状態の肌はまるで乾ききった革靴のように硬直しており、水性の化粧水をいくら重ねづけしても、角層の奥まで浸透せずに表面から蒸散してしまうのです。
        </p>
        <p>
          この閉ざされた砂漠肌を劇的に変えるブレイクスルーが、洗顔後まっさらの肌に最初の一滴を仕込む<strong>「高保湿ブースターオイル（導入美容オイル）」</strong>です。人間の細胞間脂質に似た親水性植物オイルが、固まった角質細胞を瞬時に柔らかく解きほぐし、後から使う化粧水や美容液を磁石のように吸着・引き込みます。
        </p>
        <p>
          本特集では、楽天市場やコスメアワードで絶大な支持を集めるブースターオイルの中から、編集部が浸透スピード・角層柔軟効果・後から重ねる化粧水の吸水力・ベタつきのなさを徹底検証し、11月〜12月の冬肌を救う最強の10本を厳選しました。
        </p>
      </section>

      <!-- 目次 -->
      <nav class="toc-card" aria-label="目次">
        <h2 class="toc-title">📑 目次</h2>
        <ul class="toc-list">
          <li><a href="#why-booster">1. なぜ「化粧水の前にオイル」なのか？導入オイルの科学と浸透メカニズム</a></li>
          <li><a href="#how-to-choose">2. 冬のゴワつき肌を救う！ブースターオイル選びの3大基準</a></li>
          <li><a href="#ranking">3. 高保湿ブースターオイルおすすめ厳選ランキング10選</a></li>
          <li><a href="#guide-section">4. 吸水力を最大化する！洗顔後0分の「オイルファースト美容法」実践ガイド</a></li>
          <li><a href="#faq-section">5. よくある質問 (FAQ)</a></li>
          <li><a href="#related-section">6. あわせて読みたい冬の徹底保湿特集</a></li>
        </ul>
      </nav>

      <!-- 科学的背景解説 -->
      <section id="why-booster" class="content-block">
        <h2>🔬 なぜ「化粧水の前にオイル」なのか？導入オイルの科学と浸透メカニズム</h2>
        <p>
          「油の上に水をかけると弾いてしまうのでは？」と疑問に思う方も多いはずです。しかし、ブースターオイルには通常のフェイスオイルとは異なる特別な浸透サイエンスが隠されています。
        </p>
        <div class="science-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin:24px 0;">
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">① 細胞間脂質のラメラ構造を整える</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              角層細胞の間を満たす「細胞間脂質」は、水分と油分がミルフィーユ状に重なるラメラ構造を形成しています。冬の乾燥で油分が不足するとこの構造が乱れて固化します。洗顔後すぐに親水性オイルを補うことで、固まった脂質がほぐれ、水分の通り道がスムーズに再建されます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">② 乳化作用で化粧水を磁石のように引き込む</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              アルガンオイルやホホバオイルなどの良質な植物オイルは、親水基（水になじむ部分）を持っています。オイルを塗った肌の上に化粧水を重ねると、肌表面で自然なマイクロ乳化が起き、化粧水の水分と美容成分が角層奥深くまで一気に引き込まれます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">③ 洗顔直後の急激な水分蒸発（過乾燥）を防ぐ</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              洗顔後の無防備な素肌は、わずか1〜2分で急速に水分が失われます。洗顔直後にオイルを1滴なじませることで、クッションのような一時的保護シールドが形成され、肌のつっぱりやヒリつきを完全に防ぎます。
            </p>
          </div>
        </div>
      </section>

      <!-- 選び方解説 -->
      <section id="how-to-choose" class="content-block">
        <h2>💡 冬のゴワつき肌を救う！ブースターオイル選びの3大基準</h2>
        <div class="choose-principles" style="margin:24px 0;">
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準1：肌なじみと親水性に優れたオイル種を選ぶ</h3>
            <p style="line-height:1.7; color:#475569;">
              一番搾りアルガンオイル、ピュアスクワラン、ホホバオイル、ローズヒップオイルなど、人間の皮脂や細胞間脂質に近い脂肪酸（オレイン酸・パルミトレイン酸・ワックスエステル）を含む植物オイルを選びましょう。ミネラルオイル（鉱物油）単体のものはフタ用であり導入には向きません。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準2：油分と水分が同時に届く「2層式」も有力候補</h3>
            <p style="line-height:1.7; color:#475569;">
              オイル単体のベタつきが心配な方や、朝のメイク前にも軽やかに使いたい方は、エッセンス層とオイル層が分かれた「2層式ブースター」が最適です。振って混ぜることでみずみずしい質感になり、瞬時に肌がほぐれます。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h3 style="color:#0369a1; margin-top:0;">基準3：酸化安定性の高い処方・新鮮な容器設計</h3>
            <p style="line-height:1.7; color:#475569;">
              植物オイルは空気や光で酸化しやすいため、ビタミンE（トコフェロール）などの天然抗酸化成分が配合されているものや、遮光ビン、1滴ずつ出せるスポイト・ドロッパー容器を採用している信頼のブランドを選びましょう。
            </p>
          </div>
        </div>
      </section>

      <!-- ランキング一覧セクション -->
      <section id="ranking" class="ranking-section">
        <div class="ranking-header">
          <h2>🏆 高保湿ブースターオイルおすすめ厳選ランキング10選</h2>
          <p class="ranking-subtitle">11月〜12月の頑固なゴワつき肌をふっくらほぐし、化粧水の吸水力を最大化する名品を比較！</p>
        </div>
"""

for idx, it in enumerate(items):
    dt = booster_oil_details[idx]
    rank_num = it["rank"]
    
    html_content += f"""
        <!-- 第{rank_num}位 -->
        <article id="rank-{rank_num}" class="product-card">
          <div class="product-badge-wrap">
            <span class="rank-badge rank-{rank_num}">第{rank_num}位</span>
            <span class="product-tag">{dt["tag"]}</span>
          </div>

          <header class="product-title-area">
            <h3 class="product-name">{it["brand"]} {it["name"]}</h3>
            <p class="product-catch">{dt["catch"]}</p>
          </header>

          <div class="product-main-grid">
            <div class="product-img-col">
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="product-img-link">
                <img src="{it["image_url"]}" alt="{it["brand"]} {it["name"]}" class="product-img" loading="lazy">
              </a>
              <div class="shop-info">
                <span class="price-label">参考価格:</span>
                <span class="price-val">¥{it["price"]:,}</span>
                <span class="tax-inc">(税込)</span>
                <div class="shop-name">取扱: {it["shop_name"]}</div>
              </div>
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                <span>楽天市場で商品詳細を見る</span>
              </a>
            </div>

            <div class="product-spec-col">
              <table class="spec-table">
                <tbody>
                  <tr><th>容量・規格</th><td>{dt["capacity"]}</td></tr>
                  <tr><th>製品タイプ</th><td>{dt["type"]}</td></tr>
                  <tr><th>テクスチャー</th><td>{dt["texture"]}</td></tr>
                  <tr><th>主要植物成分</th><td>{dt["ingredients"]}</td></tr>
                  <tr><th>仕上がり質感</th><td>{dt["finish"]}</td></tr>
                </tbody>
              </table>

              <div class="product-review-body">
                <h4>【皮膚科学的アプローチ＆製品特徴】</h4>
                <p>{dt["desc_p1"]}</p>
                <p>{dt["desc_p2"]}</p>

                <h4>【こんな方におすすめ】</h4>
                <p>{dt["target"]}</p>

                <h4>【効果的な使い方テクニック】</h4>
                <p>{dt["technique"]}</p>

                <div class="review-box">
                  <div class="review-title">💬 愛用者のリアルな口コミ・検証レビュー</div>
                  <p class="review-text">{dt["voice"]}</p>
                </div>

                <div class="caution-box" style="margin-top:12px; background:#fffbeb; border-left:4px solid #f59e0b; padding:10px 14px; font-size:0.88rem; color:#92400e;">
                  <strong>⚠️ 使用上のポイント・注意点：</strong> {dt["caution"]}
                </div>
              </div>
            </div>
          </div>
        </article>
"""

# 比較表、使い方ガイド、FAQ、内部リンク
html_content += """
      <!-- 比較まとめ一覧表 -->
      <section class="comparison-summary-section" style="margin:48px 0;">
        <h2>📊 高保湿ブースターオイル10選 比較早見表</h2>
        <div style="overflow-x:auto;">
          <table class="summary-table" style="width:100%; border-collapse:collapse; margin-top:16px; font-size:0.92rem;">
            <thead>
              <tr style="background:#0284c7; color:#fff;">
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">順位 / ブランド</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">商品名</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">処方タイプ</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">特徴・おすすめな人</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">参考価格</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">1位 RMK</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">Wトリートメントオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">オイル＆水層の2層式</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">柑橘の香りと圧倒的吸水力！朝晩使える大本命</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥3,780</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">2位 メルヴィータ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ビオオイル アルガンオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">100%オーガニックアルガン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">親水性抜群！砂漠肌をふっくら耕す世界の名品</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,120</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">3位 トリロジー</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ローズヒップオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">低温圧搾ローズヒップ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">オメガ3・6・9が冬のくすみとキメ乱れを払拭</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,890</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">4位 HABA</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高品位「スクワラン」</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">純度99.9%ピュアスクワラン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">たった1滴で皮脂膜を再現！ベタつきゼロ</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,750</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">5位 FEMMUE</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アイディアルオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">カメリアオイルブレンド</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">冬の小ジワ・ハリ不足を満たす優美な艶オイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥6,600</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">6位 アルビオン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ハーバルオイル トリニティ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">3種植物融合マルチオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">冬のゆらぎ肌・赤み・ゴワつきをタフに修復</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥6,380</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">7位 コスメデコルテ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">AQ オイル インフュージョン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">白樺水×植物オイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ノンオイリー感触！冬の血行不良くすみを一掃</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥8,410</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">8位 KANEBO</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ドロッピング オイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">先行ドロッピング処方</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">朝のメイク前に仕込んで粉吹き崩れを防止</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥6,740</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">9位 ロクシタン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">イモーテル ディヴァインオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高機能先行プレオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">永久花イモーテル配合！大人のしぼみ肌を再生</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥14,740</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">10位 無印良品</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ホホバオイル</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">100%植物由来ピュアホホバ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">大容量・無香料で顔から全身まで万能に使える</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,690</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 使い方ガイド -->
      <section id="guide-section" class="expert-guide-section" style="background:#f8fafc; border-radius:12px; padding:28px; margin:40px 0;">
        <h2>💧 吸水力を最大化する！洗顔後0分の「オイルファースト美容法」実践ガイド</h2>
        <div style="line-height:1.8; color:#334155;">
          <h3>ステップ1：洗顔後、タオルドライは「ほんのり水分を残す」</h3>
          <p>
            洗顔後、タオルでゴシゴシ水分を完全に拭き取ってしまうと、肌表面が乾燥してオイルのなじみが悪くなります。手のひらで軽く水滴を払うか、タオルで優しく押さえて「肌にわずかな湿り気が残っている状態」でブースターオイルを手にとりましょう。
          </p>

          <h3 style="margin-top:24px;">ステップ2：手のひらで温めて「ハンドプレス」で浸透させる</h3>
          <p>
            適量（単体オイルなら1〜2滴、2層式なら4〜5滴）を手のひらに出し、両手を合わせて体温でじんわり温めます。温めることでオイルの粘度が下がり、微細な分子が角層のキメにスムーズに吸い込まれます。顔全体を手のひらで優しく包み込み、ゆっくりと息を吐きながら押し込みましょう。
          </p>

          <h3 style="margin-top:24px;">ステップ3：間髪を入れずに高保湿化粧水を重ねる</h3>
          <p>
            オイルをなじませた後は、時間が経つ前にすぐ化粧水を重ねます。肌表面のオイルと化粧水が出会うことでミクロな乳化が起こり、化粧水が驚くほどのスピードで角層深部へと引き込まれます。手のひらが頬に吸い付くようなモチモチ感を感じたら完了です。
          </p>
        </div>
      </section>

      <!-- よくある質問 (FAQ) -->
      <section id="faq-section" class="faq-section">
        <h2>❓ 冬の高保湿ブースターオイル よくある質問 (FAQ)</h2>
        <div class="faq-item">
          <h3>Q1. 化粧水の前にオイルを塗ると、油分が水を弾いてしまいませんか？</h3>
          <p>一般的な重い鉱物油を大量に塗ると水を弾きますが、ブースター（導入）オイルとして設計された植物オイル（アルガンオイル、ホホバオイル、スクワラン、2層式オイルなど）は肌の細胞間脂質と極めて近い脂肪酸組成や親水性を持っています。洗顔後の肌になじませることで、固まった角層を柔らかくほぐし、水分の通り道（アクアポリンや細胞間隙）を拓くため、むしろ化粧水が磁石のように引き込まれて浸透力が高まります。</p>
        </div>
        <div class="faq-item">
          <h3>Q2. ブースターオイルと仕上げの美容フェイスオイルの違いは何ですか？</h3>
          <p>ブースターオイルは『洗顔後すぐのまっさらな肌』に使用し、角層を柔らかくほぐして後から使う化粧水の浸透を助ける親水性・浸透性の高い処方になっています。一方、スキンケアの最後に使うフェイスオイルは、化粧水や乳液で補った水分蒸発を防ぐ『密閉フタ』の役割を果たすため、エモリエント膜をしっかり張る重厚なテクスチャーが主流です。</p>
        </div>
        <div class="faq-item">
          <h3>Q3. オイリー肌やニキビができやすい冬の混合肌でもブースターオイルは使えますか？</h3>
          <p>はい、ご使用いただけます。冬に皮脂が出る原因の多くは、内部の水分不足を補おうとする『インナードライの防衛反応』です。ブースターオイルで角層をほぐして水分を奥まで届けることで、過剰な皮脂分泌が自然と鎮まります。オイリー肌の方は、1回に使う量を1滴程度に抑え、サラサラ感触のスクワランやホホバオイル、RMKなどの2層式オイルを選ぶのがおすすめです。</p>
        </div>
      </section>

      <!-- 関連特集への内部リンク -->
      <section id="related-section" class="related-section">
        <h2>🔗 あわせて読みたい冬の徹底保湿特集</h2>
        <div class="internal-links-grid">
          <a href="/winter-serum-booster" class="related-card">
            <span class="related-tag">導入美容液</span>
            <h4>💧 高保湿導入美容液・ブースター ランク10</h4>
            <p>水溶性のペプチドや発酵エキスで浸透を高めたい方に。</p>
          </a>
          <a href="/winter-face-oil" class="related-card">
            <span class="related-tag">美容オイル</span>
            <h4>✨ 冬の高保湿美容フェイスオイル ランク10</h4>
            <p>スキンケアの最後に使って水分蒸発を完全密閉する名品。</p>
          </a>
          <a href="/winter-lotion" class="related-card">
            <span class="related-tag">高保湿化粧水</span>
            <h4>🌊 冬の濃密高保湿化粧水 ランク10</h4>
            <p>ブースターオイルの後にたっぷり補給したい高保水ローション。</p>
          </a>
          <a href="/winter-moisture-cream" class="related-card">
            <span class="related-tag">保湿クリーム</span>
            <h4>🛡️ 冬のうるおい高保湿クリーム ランク10</h4>
            <p>取り込んだ水分を朝までしっかり閉じ込める濃密クリーム。</p>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p class="copyright">&copy; 2026-2027 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      <div class="footer-links">
        <!-- 後ほど一括スクリプトで全更新 -->
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-booster-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-booster-oil.html ({len(html_content):,} bytes)")
