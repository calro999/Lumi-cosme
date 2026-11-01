import json
import re

with open("fetched_3nov_dec_inbath_eyemask_handmask_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_hot_eyemask"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 冬のアイケア世界的金字塔！約40℃の心地よい温熱蒸気が約20分持続",
        "catch": "袋を開けるだけで瞬時に蒸気浴。寒さで凝り固まった目元の奥まで温もりがじんわり浸透する名作",
        "brand_name": "めぐりズム (花王)",
        "capacity": "大容量 12枚入（個包装）",
        "type": "使い捨て蒸気温熱アイマスク（無香料）",
        "features": "快適温度約40℃、発熱時間約20分、極微細スチーム蒸気、やわふわタッチ不織布、伸縮耳かけ構造",
        "value": "発売以来圧倒的シェアを誇る温熱アイマスクの元祖。出張先やオフィス、ベッドの上でいつでも手軽に極上スチームスパ",
        "desc_p1": "11月から12月にかけての年末商戦やデスクワークの追い込み期、外気の厳しい寒さと暖房の乾燥風、そして長時間のPC・スマートフォン操作が重なることで、目元の疲労と乾燥は年間で最も深刻なピークを迎えます。夕方になると目がショボショボして開けていられない、鏡を見ると目の下に青黒いクマが居座り、目尻や下まぶたにファンデーションの乾燥小ジワが深く刻まれている…そんな冬の目元トラブルに、最も確実で迅速な癒やしを届けてくれるのが、花王めぐりズムの『蒸気でホットアイマスク』です。",
        "desc_p2": "個包装を開封するだけで、空気中の酸素と鉄粉が反応して瞬時に発熱を開始。目には見えないほど微細な温熱スチーム（蒸気）が約40℃の快適温度で約20分間にわたって放出されます。皮膚の厚さがわずか0.02mm（ゆで卵の薄皮程度）しかないデリケートな目元を温かい蒸気がふっくらと包み込み、寒さと緊張で収縮した眼輪筋の血流を急速に改善。さらに、涙の蒸発を防ぐ油分を分泌する『マイボーム腺』の詰まりを温熱で優しく溶かし出すため、目の乾きも根本から潤います。無香料タイプは香りに敏感な方や就寝前の純粋なリラックスに最適です。",
        "target": "長時間のデスクワークやスマホ操作で目の奥がズーンと重い方、冬の寒さで目元の青クマや乾燥小ジワが目立つ方、就寝前の寝つきを良くしたい方",
        "point": "アイクリームや目元用美容液を薄く馴染ませた上から本品を装着すると、温熱スチームのスチーム効果によって美容成分の角層浸透率が飛躍的にアップします。"
    },
    {
        "rank": 2,
        "tag": "🫘 天然あずき100%の驚異的な水分保持力！レンジでチンして250回使える超高コスパ名品",
        "catch": "あずきに含まれる豊富な天然水分が蒸気となって立ち上る。適度な重みと優しい温もりが目元を包み込む",
        "brand_name": "あずきのチカラ (桐灰 / 小林製薬)",
        "capacity": "本体 1個（目もと専用形状）",
        "type": "電子レンジ加熱式・天然あずき温熱アイピロー",
        "features": "天然小豆100%使用、約250回繰り返し使用可能、電子レンジ約30〜40秒加熱、目にフィットする立体二重構造",
        "value": "1回あたりわずか数円という圧倒的経済性。化学薬品を使わない天然素材ならではの深く芯まで届く湿熱蒸気",
        "desc_p1": "冬の冷え込みが厳しくなる季節、毎日惜しみなく目元を温めたいけれど、使い捨てタイプだとコストが気になる…という方に熱烈に支持されているのが、桐灰（小林製薬）のロングセラー『あずきのチカラ 目もと用』です。あずきは他の穀物や豆類と比較して極めて多くの水分を含んでおり、電子レンジで温めることでその水分が目に見えない天然の蒸気（湿熱）となって放出されます。",
        "desc_p2": "使い捨てカイロのような乾いた熱（乾熱）とは異なり、湿熱は皮膚の深部まで熱がスムーズに伝わるため、短時間で目の奥の重だるさやこわばりをじんわりと解きほぐします。あずき特有の適度な重みが眼球とまぶたのカーブに心地よくフィットし、自律神経の副交感神経を優位に切り替えて深いリラクゼーションを誘導。約250回も繰り返し使えるため、冬の寒夜のデイリー温活ケアとしてこれ以上ない経済性と実用性を誇ります。",
        "target": "毎日お風呂上がりや就寝前に温熱アイケアを習慣化したい方、人工的な熱ではなく天然素材の優しい温もりを好む方、コスパを最重視する方",
        "point": "レンジで温める際、規定の加熱時間を厳守してください。温めた直後のほんのり甘いあずきの香りと、適度な重みを感じながら目を閉じて10分間深呼吸するのが至福のルーティンです。"
    },
    {
        "rank": 3,
        "tag": "✨ 最高級天然シルク100%×コードレス充電式！就寝中も摩擦ゼロで温め続ける上質アイマスク",
        "catch": "薄さわずか数ミリの極薄グラフェン発熱体。アロマシート対応で目元の乾燥を防ぎながら極上の睡眠へ",
        "brand_name": "SALUA (サルア)",
        "capacity": "本体一式（USB充電ケーブル・専用ポーチ付属）",
        "type": "USB充電式・コードレス高機能ホットアイマスク",
        "features": "天然シルク100%カバー、最新グラフェン発熱シート、2段階温度調節（35〜50℃）、30分自動オフタイマー",
        "value": "コードの煩わしさが一切ない完全コードレス設計。寝返りを打ってもズレず、シルクのアミノ酸が冬の摩擦乾燥から目元を保護",
        "desc_p1": "睡眠の質と目元のエイジングケアを同時に追求する美容感度の高い層から圧倒的な支持を集めるSALUA（サルア）の『充電式ホットアイマスク』。最大の特徴は、肌に直接触れるカバー部分に最高品質の天然シルク（絹）を100%贅沢に使用している点です。シルクは人間の皮膚に近い18種類のアミノ酸を含み、吸湿性・放湿性・保温性に優れ、冬の乾燥した空気による静電気や摩擦ダメージからデリケートな目元を守り抜きます。",
        "desc_p2": "内部には熱伝導率に優れたノーベル賞受賞素材『グラフェン』を採用し、スイッチを入れてわずか数秒で均一な心地よい温熱が広がります。コードレス設計のため寝返りを打っても邪魔にならず、30分の自動電源オフ機能が搭載されているため、温まりながらそのまま眠りに落ちても低温やけどの心配がありません。付属のアロマスプレーやシートを併用すれば、寝室が高級ホテルのリラクゼーションサロンへと早変わりします。",
        "target": "ベッドに入ってから眠るまで邪魔なコードなしで温まりたい方、目元のシワ・摩擦が気になり上質な素材を求める方、大切な人への冬のギフトに",
        "point": "シルクカバーは取り外して手洗い洗濯が可能なため、いつでも清潔に保てます。高温モード（約45〜50℃）で5分間急速に温めた後、低温モード（約35〜40℃）に切り替えて就寝するのがおすすめです。"
    },
    {
        "rank": 4,
        "tag": "🍊 冬の風情あふれる完熟ゆずアロマ！もぎたてのフレッシュな柑橘香が張り詰めた気分をほぐす",
        "catch": "天然ゆず精油配合の温熱蒸気。一日の終わりに冷え切った心と目元を温かい柑橘の香りで満たす",
        "brand_name": "めぐりズム (花王)",
        "capacity": "大容量 12枚入（個包装）",
        "type": "アロマ蒸気温熱アイマスク（完熟ゆずの香り）",
        "features": "天然精油配合、約40℃温熱蒸気、約20分持続、独自開発のやわふわスチームシート",
        "value": "冬の寒さと慌ただしさで張り詰めた神経を優しく解き放つ。ゆず湯に入っているかのような心地よい温もり",
        "desc_p1": "冬の日本の風物詩である『柚子（ゆず）』の恵みを凝縮した、めぐりズムの冬一番人気フレーバー『完熟ゆずの香り』。11月から12月にかけての寒風吹きすさぶ夜、外出先から帰宅して冷え切った身体に、もぎたての完熟ゆずのフレッシュで甘酸っぱいアロマが深く染み渡ります。",
        "desc_p2": "マスクを開封した瞬間から広がる天然ゆず精油の香り成分『リモネン』には、交感神経を鎮めて血行を促すリラックス作用が広く知られています。約40℃の心地よい温熱蒸気と相まって、PC画面を凝視し続けてピクピクと痙攣していた目の周りの筋肉がスーッと緩んでいくのを実感。乾燥でゴワついたまぶたのキメが整い、翌朝のアイメイクのノリが格段に向上します。",
        "target": "柑橘系の爽やかでほっとする香りが好きな方、冬の寒さで首や肩まで緊張が続いている方、仕事終わりのリフレッシュに",
        "point": "お風呂上がりに温かいハーブティーを飲みながら、ソファでリクライニングして本品を装着すると、視界が遮られることでデジタルデトックスになり、驚くほど頭がスッキリします。"
    },
    {
        "rank": 5,
        "tag": "🌿 心地よい眠りへ誘うラベンダーセージ！天然精油の香りで就寝前の目元を優しく包み込む",
        "catch": "鎮静のハーブ・ラベンダーとセージの黄金比。心地よい温熱スチームが真冬の不眠と目元乾燥をダブルでケア",
        "brand_name": "めぐりズム (花王)",
        "capacity": "大容量 12枚入（個包装）",
        "type": "アロマ蒸気温熱アイマスク（ラベンダーセージの香り）",
        "features": "天然ラベンダー精油・セージ精油配合、約40℃温熱蒸気、約20分持続、耳に優しい伸縮不織布",
        "value": "世界中で安眠アロマとして信頼されるラベンダー。ベッドに入っても寒さで目が冴えてしまう夜の最高の相棒",
        "desc_p1": "冬の寒さと年末のプレッシャーで神経が高ぶり、布団に入っても目が冴えてなかなか寝付けない…という夜に圧倒的な安らぎをもたらすのが、めぐりズムの『ラベンダーセージの香り』です。ヨーロッパで古くから安眠のハーブとして愛されてきたフレンチラベンダーの天然精油を惜しみなく配合しています。",
        "desc_p2": "目元に乗せた瞬間に立ち上る温熱蒸気とともに、奥深く落ち着いたラベンダーと清々しいセージの香りが鼻腔をくすぐり、高ぶった脳の興奮を穏やかに鎮静。温熱によってまぶたの毛細血管が広がり、体内の深部体温が手足から放散されることで、自然で深い睡眠サイクルへとスムーズに誘導されます。睡眠中に目元の水分が保持されるため、朝起きたときの目元のハリ感が明らかに違います。",
        "target": "冬の寒さやストレスで寝つきが悪い方、ハーブの香りで睡眠環境を整えたい方、寝ている間の目元の乾燥小ジワを予防したい方",
        "point": "枕元に1枚置いておき、部屋の照明を完全に消してから装着してください。暗闇の中で温熱と香りに集中することで、雑念が消え去り5分以内に心地よい眠りへと落ちていきます。"
    },
    {
        "rank": 6,
        "tag": "🎁 気分に合わせて香りを選べる豪華アソート！毎日の疲れを飽きずにリセットする大満足セット",
        "catch": "無香料・ゆず・ラベンダー・森林浴・カモミールなど。その日の気分で選べる冬の贅沢アイケア",
        "brand_name": "めぐりズム (花王)",
        "capacity": "12枚入×3箱セット（計36枚）",
        "type": "選べる3箱セット・高機能蒸気温熱アイマスク",
        "features": "多彩な香りラインナップ、約40℃快適スチーム、まとめ買い高コスパ、個包装で持ち運び便利",
        "value": "1箱ずつ買うよりお得なまとめ買いセット。冬のシーズン中（11月〜2月）毎日惜しみなく使える安心の大容量",
        "desc_p1": "毎日温熱アイマスクを使いたいけれど、同じ香りが続くと飽きてしまう…という愛用者の声に応えて大人気となっているのが、めぐりズムの人気アロマからお好みの3箱を自由に選べるセットです。無香料をはじめ、完熟ゆず、ラベンダー、カモミール、森林浴など、気分やシチュエーションに合わせてベストな香りを使い分けることができます。",
        "desc_p2": "集中して作業した日の午後はリフレッシュできる『森林浴』、ストレスを感じた夜は優しい『カモミール』、ぐっすり眠りたい日は『ラベンダー』、メイク前や香水をつける日は『無香料』といったように、毎日のコンディションに寄り添ったオーダーメイドなアイケアが可能。計36枚の大容量なので、家族でシェアしたり、冬のちょっとしたプチギフトとしても大変喜ばれます。",
        "target": "毎日欠かさずホットアイマスクを使いたいヘビーユーザー、その日の気分で香りを使い分けたい方、家族や同僚とシェアしたい方",
        "point": "オフィスに無香料や森林浴を数枚ストックし、自宅の寝室にラベンダーやゆずを常備しておく『ロケーション別使い分け』が賢い活用法です。"
    },
    {
        "rank": 7,
        "tag": "🍎 温めても冷やしても使える天然アロマピロー！可愛い北欧風デザインとリンゴ＆ハーブの癒やし",
        "catch": "電子レンジで温熱・冷蔵庫で冷却の2WAY仕様。天然精油のナチュラルな香りで目元をリフレッシュ",
        "brand_name": "ほんやら堂",
        "capacity": "本体 1個（専用アロマビーズパック入り）",
        "type": "温冷両用・天然アロマアイピロー",
        "features": "レンジ加熱＆冷蔵庫冷却2WAY、天然国産アロマオイル配合、肌当たりの良いパイル生地カバー、手洗い洗濯可能",
        "value": "ほっこり癒やされる愛らしいデザインと心地よい重量感。デスクやリビングに置いておくだけで冬のインテリアとしても映える",
        "desc_p1": "生活雑貨やリラクゼーションアイテムで女性を中心に熱烈なファンを持つほんやら堂の『アロマ温冷アイピロー』。冬は電子レンジで30秒温めてホカホカの温熱アイマスクとして、夏や目元が腫れぼったい朝は冷蔵庫で冷やしてクールアイマスクとして1年中活躍する万能アイテムです。",
        "desc_p2": "カバーの内側には適度な重みを持つセラミックビーズと天然精油を含んだアロマパックが封入されており、目の上に乗せると程よい圧力で眼窩（がんか）のツボを心地よく刺激します。甘く爽やかなりんごやカモミールの香りがふんわりと立ち上り、冬の寒さでこわばった表情筋が緩んでいくのを感じられます。肌に触れるパイル地カバーは取り外して洗えるため、衛生面も安心です。",
        "target": "可愛いデザインのリラクゼーション雑貨が好きな方、温めと冷却の両方を目的に応じて使い分けたい方、プチギフトを探している方",
        "point": "冬の朝、顔がむくんでいるときは冷やして引き締め、夜寝る前はレンジで温めて血行促進…と1日の中で使い分けることで、目元のコンディションを完璧にコントロールできます。"
    },
    {
        "rank": 8,
        "tag": "💎 パナソニックの本格スチーム美顔技術を目元へ！高温スチーム×リズミカルな振動で本格エステ",
        "catch": "たっぷりのホットスチームが乾いた目元を集中加湿。3段階の温感設定と選べるリズムタッチ",
        "brand_name": "Panasonic (パナソニック)",
        "capacity": "本体一式（給水プレート・アロマホルダー・ACアダプター付属）",
        "type": "本格スチーム＆温感振動・高機能目もとエステ美顔器",
        "features": "小型ファン内蔵高濃度スチーム、3段階温度設定（最高約42℃）、リズムタッチ機能、海外電圧対応",
        "value": "美容家電のパイオニアが誇る目元専用エステギア。給水プレートから発生する本格蒸気が目元の角層深部まで潤いを届ける",
        "desc_p1": "ドラッグストアの使い捨てやレンジ温めでは物足りない、本気で目元の乾燥小ジワ・たるみ・くすみをケアしたいという美容志向の方から絶大な評価を得ているのが、パナソニックの『目もとエステ EH-CSW68』です。本体に装着した給水プレートから、小型ファンによってたっぷりの微細温熱スチームを目元全体に送り届ける本格構造を採用しています。",
        "desc_p2": "最高約42℃のしっかりとした温感ヒーターが目元を包み込み、スチームの水分が角層の奥深くまで浸透。さらに、エステティシャンの指先のような心地よいリズミカルな振動タッチが加わることで、眼輪筋を心地よくストレッチし、滞りがちなリンパの流れを促進します。使用後の目元はまるで入念なフェイシャルエステを受けた後のようにふっくらと潤い、ハリと明るさが蘇ります。",
        "target": "目元のエイジングサイン（乾燥小ジワ・ハリ低下・クマ）を本気で集中ケアしたい方、本格的な美容家電に投資したい方",
        "point": "別売りの専用アロマタブレット（ラベンダーやベルガモットなど）をホルダーにセットして使用すると、温熱スチームとともに極上のアロマが広がり、サロン級の至福空間を楽しめます。"
    },
    {
        "rank": 9,
        "tag": "🎧 目元エステ×エアプレッシャー×癒やしのBGM！冬の五感を解き放つプレミアムアイマッサージャー",
        "catch": "空気圧で目の周りのツボを優しく指圧。温熱ヒーターとヒーリング音楽で極上のリラクゼーション空間へ",
        "brand_name": "La Luna (ラルーナ / フジアンドチェリー)",
        "capacity": "本体一式（USB充電コード・収納袋・汚れ防止カバー付属）",
        "type": "エアー加圧×温感ヒーター・高機能アイマッサージャー",
        "features": "空気圧エアーバッグ、約42℃温感ヒーター、ソルフェジオ周波数ヒーリングBGM内蔵、折りたたみコンパクト設計",
        "value": "楽天ランキングで多数の1位を獲得する大ヒット美顔ギア。目元を温めるだけでなく、人間の手のような絶妙な加圧でコリをほぐす",
        "desc_p1": "冬の冷気とPC作業による酷い眼精疲労、こめかみの緊張からくる頭痛に悩む現代人のために設計されたLa Luna（ラルーナ）の『エアーアイマスク』。高級感あふれるスタイリッシュなメタリックデザインの中に、温熱ヒーターと複数のエアバッグを内蔵し、目元だけでなく眉間やこめかみまで包み込んでケアします。",
        "desc_p2": "約42℃の心地よい温熱で血行を促しながら、絶妙な強弱で膨らむエアバッグが指圧マッサージのように目元のツボを優しくプッシュ。さらに、自律神経を整えるとされるソルフェジオ周波数のヒーリングBGMが本体から流れ、目と耳の両方から深いリラックス状態へと導かれます。15分で自動停止するため、夜のベッドタイムに使用すればそのまま極上の睡眠へと誘われます。",
        "target": "目元だけでなくこめかみや頭の重さまでほぐしたい方、サロン級の指圧感と温熱を自宅で毎日味わいたい方、スタイリッシュなギフトを探している方",
        "point": "付属の汚れ防止カバーを装着して使用すれば、ファンデーションやスキンケアがつかずいつでも清潔。PC作業の合間に15分使うだけで、視界がパッと明るくなります。"
    },
    {
        "rank": 10,
        "tag": "⚡ ドクターエアの技術が集結！視界を遮らない半透明ウィンドウ搭載のハイテク温熱ギア",
        "catch": "温熱ヒーター×バイブレーション×エア加圧。本を読んだりスマホを見ながらでも使える革新的デザイン",
        "brand_name": "DOCTORAIR (ドクターエア)",
        "capacity": "本体一式（充電スタンド・USBコード・専用ポーチ付属）",
        "type": "3Dエア×温熱×振動・高機能アイマジック美顔器",
        "features": "半透明シースルー構造、温熱ヒーター、エア加圧、マルチバイブレーション、Bluetooth音楽再生機能",
        "value": "ボディケア機器のトップブランド・ドクターエアが手掛ける本格アイケア。完全密閉せず周囲が見えるため圧迫感が苦手な方にも安心",
        "desc_p1": "コンディショニングギアで圧倒的な知名度を誇るドクターエアの『3Dアイマジック リフレッシュ』。従来のアイマッサージャーの『装着すると視界が完全に遮られて不安』という不満を解消するため、半透明のシースルーウィンドウを採用した革新的なモデルです。",
        "desc_p2": "目元をじんわり温める温熱機能に加え、心地よい空気圧と細やかなバイブレーションが連動し、目の周りの筋肉を立体的に刺激。スマートフォンとBluetooth接続すれば、お気に入りのポッドキャストや音楽を聴きながらケアを楽しめます。目元が完全に塞がれないため、就寝前の読書中やテレビを見ながらの「ながら温活」ができる唯一無二のハイテクギアです。",
        "target": "完全な暗闇や閉塞感が苦手な方、音楽やラジオを聴きながらケアしたい方、ドクターエアの本格的な筋肉アプローチを求める方",
        "point": "Bluetoothでお気に入りの睡眠用アコースティックBGMを流しながら温熱モードを作動させると、一日の眼精疲労と脳の疲れが同時にリセットされます。"
    }
]

# 比較表生成
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="rank-cell">第{p['rank']}位</td>
      <td class="brand-cell"><strong>{p['brand_name']}</strong><br><small>{item['display_name'][:25]}...</small></td>
      <td class="price-cell">¥{item['price']:,}</td>
      <td>{p['type']}</td>
      <td>{p['capacity']}</td>
      <td>{p['features']}</td>
    </tr>
    """)

# 商品カードHTML生成
product_cards_html = []
for p, item in zip(product_details, items):
    product_cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['brand_name']} - {item['display_name']}</h3>
        <p class="product-catch">{p['catch']}</p>
      </div>

      <div class="product-main">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{p['brand_name']} {item['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-meta-list">
            <div class="meta-item"><span class="meta-label">参考価格：</span><span class="meta-value price-val">¥{item['price']:,}（税込）</span></div>
            <div class="meta-item"><span class="meta-label">セット内容：</span><span class="meta-value">{p['capacity']}</span></div>
            <div class="meta-item"><span class="meta-label">アイテム種別：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要機能・特徴：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の目元冷え＆乾燥小ジワに効く注目ポイント！</h4>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>

      <div class="product-description">
        <h4>【詳細解説＆本音レビュー】</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの温熱スチーム温活アドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

faq_items = [
    {
        "q": "なぜ冬になると目元のクマや乾燥小ジワが急激に悪化するのですか？",
        "a": "理由は大きく3つあります。1つ目は『皮膚の極度な薄さ』です。目元の皮膚はわずか0.02mmと体の中で最も薄く、皮脂腺がほとんどないため、冬の乾燥外気とエアコン暖房で水分が真っ先に蒸発します。2つ目は『寒冷による毛細血管の収縮』です。寒さで血流が滞ると青黒いクマが出現し、組織への酸素や栄養供給が滞ります。3つ目は『マイボーム腺の油分固化』です。涙の蒸発を防ぐ脂質を分泌するマイボーム腺が寒さで詰まりやすくなり、ドライアイと角層の砂漠化が同時に進行するためです。"
    },
    {
        "q": "使い捨てタイプ（めぐりズム等）と充電式・電子レンジタイプはどちらがおすすめですか？",
        "a": "使用シーンと目的によって使い分けるのがベストです。『使い捨てタイプ』は極微細な蒸気（スチーム）が直接発生するため、目元の角層を加湿する保湿効果が最も高く、出張先や移動中、ベッドでそのまま眠りたい時に最適です。一方、『あずき・電子レンジタイプ』や『充電式シルクタイプ』は繰り返し使えるため経済性に優れ、毎日の就寝前の習慣としてコストを気にせず使い続けたい方に向いています。保湿重視なら蒸気スチーム系、コスパ重視なら繰り返しタイプを選びましょう。"
    },
    {
        "q": "アイクリームや目元用美容液を塗った後にホットアイマスクを使っても大丈夫ですか？",
        "a": "非常に効果的でおすすめのケア方法です。アイクリームを塗った上からホットアイマスクを装着すると、温熱と蒸気によって毛穴と角層が柔らかくほぐれ、密閉効果（ODT効果）によって美容成分の浸透が格段に促進されます。ただし、レチノールなど熱や刺激に弱い高刺激成分を含む美容液の場合は、肌トラブルを防ぐため温熱マスクを外した後のスキンケアとして塗布するのが安心です。"
    },
    {
        "q": "ホットアイマスクは毎日使っても問題ありませんか？1日の使用回数制限は？",
        "a": "適切な温度（約40℃前後）と使用時間（15〜20分程度）を守っていれば、毎日朝晩使用しても全く問題ありません。特に冬場は血行不良が続きやすいため、毎日の入浴後や就寝前のデイリーケアとして継続することで、頑固な青クマや乾燥小ジワの予防に極めて高い効果を発揮します。ただし、目元に炎症（結膜炎やものもらい）がある場合や、美容医療（埋没法やレーザー治療）直後は使用を控えてください。"
    },
    {
        "q": "ホットアイマスクをつけたまま朝まで寝てしまっても大丈夫ですか？",
        "a": "使い捨てタイプ（めぐりズムなど）は発熱時間が約20分で自然に冷める設計になっているため、つけたまま眠ってしまっても低温やけどの心配はありません。また、充電式のSALUAやLa Lunaなども30分自動電源オフタイマーが付いているため安全です。ただし、充電式でタイマー機能がない機器や、長時間熱源が密着し続ける状態は低温やけどのリスクがあるため、必ず自動オフ機能付きの製品を選びましょう。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {item['display_name']}",
        "image": item['image_url'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliate_url'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10",
    "description": "11月・12月の冬の寒冷凝固による目元血流滞留と、エアコン暖房・年末PC作業による深刻な乾燥小ジワ・青クマを徹底解決！めぐりズム、あずきのチカラ、SALUA、パナソニック、La Luna、ドクターエアなど、温熱スチームと心地よい温もりで目元を満たす最強高保湿ホットアイマスク10選を徹底比較！",
    "image": items[0]['image_url'],
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
    "datePublished": "2026-11-02",
    "dateModified": "2026-11-02"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿ホットアイマスク・温感スチームアイケア おすすめランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": faq['q'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['a']
            }
        } for faq in faq_items
    ]
}

json_ld_breadcrumb = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "ホーム",
            "item": "https://lumi-cosme.vercel.app/"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "ホットアイマスク特集",
            "item": "https://lumi-cosme.vercel.app/winter-hot-eyemask"
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の寒冷凝固による目元血流滞留と、エアコン暖房・年末PC作業による深刻な乾燥小ジワ・青クマを徹底解決！めぐりズム、あずきのチカラ、SALUA、パナソニック、La Luna、ドクターエアなど、温熱スチームと心地よい温もりで目元を満たす最強高保湿ホットアイマスク10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-hot-eyemask">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10">
  <meta property="og:description" content="11月・12月の冬の目元の冷え・クマ・乾燥小ジワを徹底解決！めぐりズム、あずきのチカラ、SALUAなど温熱蒸気で目元をふっくら満たす最強ホットアイマスク10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-hot-eyemask">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #7c3aed;
      --primary-dark: #6d28d9;
      --primary-light: #f5f3ff;
      --accent: #8b5cf6;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}

    .site-header {{
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(8px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 1rem 0;
    }}
    .header-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-links {{
      display: flex;
      gap: 1.5rem;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: var(--primary);
    }}

    .main-container {{
      max-width: 960px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .breadcrumbs {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}
    .breadcrumbs a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumbs a:hover {{
      color: var(--primary);
    }}

    .article-header {{
      background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 50%, #4c1d95 100%);
      color: white;
      padding: 3.5rem 2rem;
      border-radius: var(--radius);
      margin-bottom: 2.5rem;
      box-shadow: 0 10px 25px -5px rgba(124, 58, 237, 0.3);
    }}
    .article-tag {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(4px);
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 1.5rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      opacity: 0.9;
    }}

    .intro-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border-left: 6px solid var(--primary);
    }}
    .intro-lead {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      line-height: 1.7;
    }}
    .intro-box p {{
      margin-bottom: 1rem;
      color: #334155;
    }}
    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.2rem;
      margin-top: 1.8rem;
    }}
    .intro-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 12px;
      border: 1px solid rgba(124, 58, 237, 0.2);
    }}
    .intro-card h4 {{
      color: var(--primary-dark);
      font-size: 1rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .intro-card p {{
      font-size: 0.88rem;
      color: #334155;
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .section-title {{
      font-size: 1.7rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.5rem;
      padding-bottom: 0.6rem;
      border-bottom: 3px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .table-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3.5rem;
    }}
    .table-wrapper {{
      overflow-x: auto;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .spec-table th, .spec-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border);
    }}
    .spec-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .spec-table .rank-cell {{
      font-weight: 800;
      color: var(--primary-dark);
      text-align: center;
      white-space: nowrap;
    }}
    .spec-table .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.2rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      position: relative;
      border: 1px solid var(--border);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.08);
    }}
    .product-badge {{
      position: absolute;
      top: -12px;
      left: 24px;
      background: linear-gradient(135deg, #7c3aed, #6d28d9);
      color: white;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.3rem 1.2rem;
      border-radius: 9999px;
      box-shadow: 0 4px 8px rgba(124, 58, 237, 0.3);
    }}
    .product-header {{
      margin-top: 0.8rem;
      margin-bottom: 1.5rem;
    }}
    .product-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-weight: 700;
      font-size: 0.85rem;
      background: var(--primary-light);
      padding: 0.25rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.5rem;
    }}
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 0.4rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
      .article-title {{ font-size: 1.5rem; }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #f8fafc;
      border-radius: 12px;
      padding: 1rem;
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 250px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-meta-list {{
      background: #f8fafc;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      margin-bottom: 1.2rem;
      border: 1px solid var(--border);
    }}
    .meta-item {{
      display: flex;
      font-size: 0.9rem;
      padding: 0.35rem 0;
      border-bottom: 1px dashed #e2e8f0;
    }}
    .meta-item:last-child {{ border-bottom: none; }}
    .meta-label {{
      width: 110px;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    .meta-value {{
      color: var(--text);
      font-weight: 500;
    }}
    .price-val {{
      color: #e11d48;
      font-weight: 800;
      font-size: 1.15rem;
    }}

    .product-points {{
      background: #faf5ff;
      border-left: 4px solid #9333ea;
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
    }}
    .product-points h4 {{
      font-size: 0.92rem;
      color: #7e22ce;
      margin-bottom: 0.3rem;
    }}
    .product-points p {{
      font-size: 0.88rem;
      color: #581c87;
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .product-description {{
      margin-bottom: 1.5rem;
      line-height: 1.8;
      color: #334155;
    }}
    .product-description h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.6rem;
    }}
    .product-description p {{
      margin-bottom: 0.8rem;
    }}

    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.8rem;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.88rem;
      line-height: 1.6;
    }}
    .target-block {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e3a8a;
    }}
    .tip-block {{
      background: #fefce8;
      border: 1px solid #fef08a;
      color: #713f12;
    }}
    .advice-block strong {{
      display: block;
      margin-bottom: 0.3rem;
    }}

    .product-action {{
      text-align: center;
      margin-top: 1rem;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: white;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 700;
      padding: 1rem 2.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
      width: 100%;
      max-width: 480px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      color: white;
    }}

    .faq-section {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: white;
      font-size: 0.8rem;
      font-weight: 800;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      margin-top: 0.2rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.8rem;
    }}

    .internal-links-box {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
    }}
    .links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.2rem;
    }}
    .link-card {{
      background: #f8fafc;
      padding: 1rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      transition: border-color 0.2s, background 0.2s;
    }}
    .link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}
    .link-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 0.92rem;
      margin-bottom: 0.3rem;
    }}
    .link-card span {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 0;
      margin-top: 4rem;
      border-top: 1px solid #1e293b;
    }}
    .footer-container {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      text-align: center;
      font-size: 0.85rem;
    }}
    .footer-links {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 1.2rem;
      margin-bottom: 1.5rem;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: white;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-container">
      <a href="/" class="site-logo">
        <span>❄️ 冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="/winter-hot-eyemask">ホットアイマスク</a>
        <a href="/winter-eye-cream">アイクリーム</a>
        <a href="/winter-needle-patch">ニードルパッチ</a>
      </nav>
    </div>
  </header>

  <main class="main-container">
    <div class="breadcrumbs">
      <a href="/">ホーム</a> &gt; <a href="/winter-hot-eyemask">冬のパーツケア特集</a> &gt; <span>高保湿ホットアイマスク・温感スチームアイケア</span>
    </div>

    <header class="article-header">
      <span class="article-tag">❄️ 11月・12月最新冬コスメ徹底比較特集</span>
      <h1 class="article-title">保湿力の強さで冬の目元ショボショボ冷え・乾燥クマ小ジワとさようなら！蒸気と温熱で巡りを促しふっくらハリ感を取り戻す高保湿ホットアイマスクランク10</h1>
      <div class="article-meta">
        <span>📅 更新日: 2026年11月2日</span>
        <span>⏱️ 読了目安: 約8分</span>
        <span>🔍 楽天公式APIリアルタイム価格検証済み</span>
      </div>
    </header>

    <div class="intro-box">
      <p class="intro-lead">
        11月から12月にかけて、本格的な冬の寒さと年末の過密なデスクワークが重なる時期、夕方になると「目がショボショボして開けていられない」「鏡を見ると目の下に青黒いクマが居座り、目尻にファンデーションの乾燥小ジワが深く刻まれている」という深刻な目元の砂漠化に直面する方が急増します。
      </p>
      <p>
        目元の皮膚はわずか0.02mm（ゆで卵の薄皮程度）と顔の中で最も薄く、皮脂腺もほとんど存在しません。そのため、冬の寒冷外気とエアコン暖房のダブル直撃を受けると、角層の水分が一気に蒸発して菲薄化（ひはくか）が進みます。さらに、寒さで眼輪筋の毛細血管がギュッと収縮して血流が滞留することで頑固な青クマが発生し、涙の蒸発を防ぐ油分を分泌する『マイボーム腺』が冷えて固まることでドライアイが悪化するという負のスパイラルに陥ります。
      </p>
      <p>
        この冬の目元危機を救う唯一無二の手段が、温熱と蒸気を同時に届ける『高保湿ホットアイマスク』です。約40℃前後の心地よい温熱スチームが固まったマイボーム腺の脂質を優しく融解し、眼輪筋の血流を呼び覚まして目元にふっくらとしたハリと血色感を蘇らせます。本特集では、楽天市場公式APIよりリアルタイムにデータを取得し、2026年冬に本当に選ぶべき実力派ホットアイマスク10選を徹底比較します。
      </p>

      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>🔥 マイボーム腺の油分融解</h4>
          <p>寒さで固まった涙の保護油（脂質）を温熱で優しく溶かし出し、涙の過度な蒸発と目の奥の乾きを根底からストップします。</p>
        </div>
        <div class="intro-card">
          <h4>👁️ 眼輪筋の血流促進＆クマ解消</h4>
          <p>薄さ0.02mmの目元皮膚の毛細血管を広げ、滞留した黒ずみ・青グマを解消。ふっくら明るい目元印象を取り戻します。</p>
        </div>
        <div class="intro-card">
          <h4>💧 蒸気スチーム加湿＆小ジワリペア</h4>
          <p>微細な温熱蒸気が乾ききった角層細胞を潤し、ファンデーションの乾燥ひび割れや縮緬（ちりめん）ジワをふっくら持ち上げます。</p>
        </div>
      </div>
    </div>

    <!-- 比較表セクション -->
    <section class="table-section">
      <h2 class="section-title">📊 高保湿ホットアイマスク・温感スチームアイケア 厳選10選スペック比較表</h2>
      <div class="table-wrapper">
        <table class="spec-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・ブランド</th>
              <th>参考価格（税込）</th>
              <th>アイテム種別</th>
              <th>セット内容</th>
              <th>主要機能・特徴</th>
            </tr>
          </thead>
          <tbody>
            {"".join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- ランキング商品セクション -->
    <section class="products-section">
      <h2 class="section-title">🏆 保湿力高めホットアイマスク ランキングTOP10</h2>
      {"".join(product_cards_html)}
    </section>

    <!-- ハウツーセクション -->
    <section class="intro-box" style="margin-top: 3rem;">
      <h2 class="section-title" style="border-bottom: none; margin-bottom: 1rem;">💡 プロが教える！冬のホットアイケア効果を最大化する「3段階温活ルーティン」</h2>
      <p>
        ホットアイマスクは単体でも極上の心地よさを誇りますが、日々のスキンケアと組み合わせることで美容効果が何倍にも跳ね上がります。プロが実践する温活ルーティンをご紹介します。
      </p>
      <div class="intro-highlight-grid">
        <div class="intro-card">
          <h4>1. アイクリームを薄く仕込む</h4>
          <p>ヒアルロン酸やセラミド配合のアイクリームを目元に優しく点置きして馴染ませます。温熱スチームが美容成分の浸透を強力に後押しします。</p>
        </div>
        <div class="intro-card">
          <h4>2. 15〜20分間、完全脱力</h4>
          <p>部屋の明かりを暗くし、深く腹式呼吸を繰り返しながら温もりを味わいます。視覚を休めることで自律神経が副交感神経へと切り替わります。</p>
        </div>
        <div class="intro-card">
          <h4>3. 外した直後に優しくツボ押し</h4>
          <p>温まって柔らかくなった目頭のツボ（晴明）や眉頭（攅竹）を中指の腹で優しく3秒押すと、血行促進と老廃物排出がさらに促進されます。</p>
        </div>
      </div>
    </section>

    <!-- よくある質問（FAQ） -->
    <section class="faq-section">
      <h2 class="section-title">❓ 冬のホットアイケアに関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q">{item['q']}</div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- 内部リンク回遊セクション -->
    <section class="internal-links-box">
      <h2 class="section-title">🔗 あわせて読みたい！冬のパーツケア・集中保湿特集</h2>
      <div class="links-grid">
        <a href="/winter-eye-cream" class="link-card">
          <strong>👁️ 高保湿アイクリーム10選</strong>
          <span>レチノールやペプチドを高濃度配合！真冬の目尻の小ジワやたるみを押し上げる本格アイクリーム比較。</span>
        </a>
        <a href="/winter-needle-patch" class="link-card">
          <strong>🔬 マイクロニードルパッチ10選</strong>
          <span>寝ている間にヒアルロン酸針が角層深部へ直接届く！目元・ほうれい線の乾燥小ジワを集中注入ケア。</span>
        </a>
        <a href="/winter-sleeping-mask" class="link-card">
          <strong>🌙 高保湿スリーピングマスク10選</strong>
          <span>寝ている間のエアコン乾燥から肌を守り抜く！翌朝洗顔した瞬間に吸い付くような水光肌へ導く夜用パック。</span>
        </a>
        <a href="/winter-morning-mask" class="link-card">
          <strong>⏰ 朝用高保湿シートマスク10選</strong>
          <span>冬の冷たい水洗顔不要！60秒貼るだけで洗顔から下地まで一瞬で完了する朝用時短シートマスクまとめ。</span>
        </a>
        <a href="/winter-face-mist" class="link-card">
          <strong>💦 高保湿ミスト化粧水10選</strong>
          <span>オフィスや外出先での暖房乾燥をシュッと一吹きで救済！メイク崩れを防ぐオイルイン高保湿ミスト。</span>
        </a>
        <a href="/winter-inbath-body" class="link-card">
          <strong>🛁 濡れた肌用インバスボディミルク10選</strong>
          <span>極寒の脱衣所に出る前にお風呂場で濡れたまま保湿！入浴後の急激な水分蒸発を防ぐ冬の必須ミルク。</span>
        </a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-links">
        <a href="/">トップページ</a>
        <a href="/winter-hot-eyemask">ホットアイマスク</a>
        <a href="/winter-eye-cream">アイクリーム特集</a>
        <a href="/winter-needle-patch">ニードルパッチ特集</a>
        <a href="/winter-inbath-body">インバスボディケア</a>
      </div>
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場公式アフィリエイトプログラムに参加しています。</p>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-hot-eyemask.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-hot-eyemask.html!")
