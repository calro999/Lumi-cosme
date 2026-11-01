import json
import re

with open("fetched_3nov_dec_needle_salt_gloss_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_lip_gloss"]["items"]

gloss_details = [
    {
        "rank": 1,
        "tag": "🏆 美容界の絶対王者！カプサイシン×チェリーオイルで24時間ふっくらボリューミー",
        "catch": "世界中で数秒に1本売れるプランプリップの金字塔。冬の縦ジワを瞬時に消し去りガラスのような水光ツヤが持続",
        "brand_name": "DIOR (ディオール)",
        "capacity": "6ml",
        "type": "高保湿ボリュームアッププランプリップグロス",
        "features": "ヒアルロン酸Na、チェリーオイル（セイヨウミザクラ種子油）、トウガラシ果実エキス（カプサイシン）、メントール",
        "value": "90%自然由来成分に進化。唇のボリュームアップと濃密ケア効果を最高次元で両立するホリデーシーズンの必須コスメ",
        "desc_p1": "11月から12月へと向かい寒風が吹き荒れる季節、寒さと乾燥で血色を失い、縦ジワが深く刻まれてしぼんでしまった冬の唇に、ひと塗りで圧倒的な生命感とぷるんとした立体ツヤを宿す世界的名品が、パルファン・クリスチャン・ディオールの『ディオール アディクト リップ マキシマイザー』です。リッププランパーというジャンルを確立した伝説的アイテムであり、現在は90%自然由来成分へと進化を遂げています。",
        "desc_p2": "唇に乗せた瞬間に広がる心地よいジンジン・スースーとした刺激は、トウガラシ果実エキス由来のカプサイシンとメントールによるもの。この微細な刺激が冬の寒さで滞った唇の毛細血管の血流を一気に活性化させ、内側から押し上げるようにふっくらと膨らませます。さらに濃密なチェリーオイルとヒアルロン酸が角層深部を潤し、まるで水滴をコーティングしたかのような圧倒的な水光フィルム膜を形成。暖房の効いた部屋に一日中いても唇が一切乾かず、ホリデーのイルミネーションに美しく反射するツヤが持続します。",
        "target": "唇の縦ジワやボリューム不足に悩む方、ホリデーシーズンの特別なツヤと血色感を求める方、本格的な保湿持続力を重視する方",
        "point": "単体での濡れツヤ使いはもちろん、お気に入りのマットリップやティントの上から唇の中央（山と下唇の真ん中）にだけポンポンと重ねると、唇の立体感が劇的に際立ちます。"
    },
    {
        "rank": 2,
        "tag": "🌿 99%スキンケア成分！ヘーゼルナッツ×ホホバの濃密植物オイルが冬の乾燥唇を完全シールド",
        "catch": "クラランスが誇るオイル美容の真髄。まるで唇専用の高濃度美容液のようなリッチな潤いと心地よい密着感",
        "brand_name": "CLARINS (クラランス)",
        "capacity": "12ml（チューブタイプ・クッションチップ）",
        "type": "植物オイル高配合リップ美容液グロス",
        "features": "ヘーゼルナッツオイル、オーガニックホホバオイル、シアバター、カニナバラ果実油、99%スキンケア処方",
        "value": "植物オイル研究のパイオニアが生んだ高機能グロス。クッションアプリケーターでとろけるように唇を包み込む贅沢ケア",
        "desc_p1": "フランスの植物スキンケアのパイオニア、クラランスがオイル美容の知見を注ぎ込んだ『リップコンフォート リップパーフェクター』。冬の厳しい乾燥や木枯らしによって皮剥けやひび割れを起こしやすいデリケートな唇のために、なんと全成分の99%をスキンケア成分で構成した、まさに「塗るリップ美容液グロス」です。",
        "desc_p2": "肌との親和性が極めて高いヘーゼルナッツオイルとオーガニックホホバオイルが、唇の表面に柔らかく濃厚なオイルヴェールを形成。乾燥で硬くなった唇の皮を瞬時に柔らかくほぐし、水分蒸発を完璧にシャットアウトします。先端のふわふわとしたクッションチップが唇の凹凸に優しくフィットし、摩擦を感じさせずに均一に塗布可能。ベタつきのないクリーミーなツヤと甘いベリーのような香りに包まれ、日中のリップメイクと集中リップケアを同時に完結できます。",
        "target": "グロス特有のベタつきや髪が唇にくっつく感触が苦手な方、極度の乾燥で唇の皮が剥けやすい方、ナチュラルな血色ツヤを好む方",
        "point": "就寝前のナイトリップトリートメントとしても優秀で、夜たっぷりと塗って眠ると、翌朝の洗顔時にはふっくらと柔らかな生まれたての唇を実感できます。"
    },
    {
        "rank": 3,
        "tag": "🌸 花蜜のような濃密ツヤ×温感プランプ！ホリデーの口元を最高峰に美しく演出する花束セラム",
        "catch": "小瓶に咲き誇るクリスタルフラワーが愛らしさ満点。心地よい温感と清涼感のハーモニーで唇をぷっくりボリュームアップ",
        "brand_name": "JILL STUART (ジルスチュアート)",
        "capacity": "6ml",
        "type": "花蜜高保湿プランプリップ美容液",
        "features": "クリスタルフローラルブーケオイル（ダマスクローズ・エーデルワイス等）、温感成分（バニリルブチル）、清涼感成分（メントキシプロパンジオール）",
        "value": "持っているだけで気分が高揚するジュエリーのようなボトル。ホリデーシーズンのギフトや自分へのご褒美コスメとして不動の人気",
        "desc_p1": "冬のホリデーシーズンに圧倒的なときめきと華やかさを届けてくれるジルスチュアートの『クリスタルブルーム リップブーケ セラム』。まるで咲き誇る花々から集めた蜜をそのまま閉じ込めたかのような、濃密なツヤと保湿力を誇る大ヒットプランプリップセラムです。",
        "desc_p2": "塗った瞬間に広がる温感成分（バニリルブチル）と清涼感成分（メントキシプロパンジオール）の心地よいジンジン感が、冬の寒さで冷え切った唇を優しく刺激。内側からポッと上気したような自然な血色感と、ふっくらとした厚みのあるボリューム感を呼び覚まします。ダマスクローズエキスやエーデルワイスエキスなどのボタニカルフラワーオイルが唇を優雅にラッピングし、光を乱反射する微細なクリスタルパールが冬の夜の街灯りの下で息をのむほど美しい輝きを放ちます。",
        "target": "ホリデーのイルミネーションデートやパーティーで華やかに見せたい方、可愛いパッケージでメイク時間を楽しみたい方、ギフトを探している方",
        "point": "唇の輪郭よりわずか1mm外側にオーバーリップ気味にチップで滑らせることで、人中短縮効果とあどけない立体的なぷっくり唇が完成します。"
    },
    {
        "rank": 4,
        "tag": "✨ エレガンスの極み！植物性ワックスが叶える軽やかな水光ツヤとラグジュアリーな潤い",
        "catch": "シャネル独自のハイドラボーストコンプレックス配合。ベタつきを徹底排除した洗練されたフィルムツヤが大人の品格を格上げ",
        "brand_name": "CHANEL (シャネル)",
        "capacity": "5.5g",
        "type": "ラグジュアリー高保湿リップグロス",
        "features": "ホホバ・ヒマワリ・ミモザの天然植物ワックス、オリゴペプチド、高屈折率エモリエントオイル",
        "value": "シャネルの美学が息づく気品ある発色と輝き。大人の女性の唇を乾燥から守りつつ洗練された濡れツヤをもたらす名品",
        "desc_p1": "世界最高峰のメゾン、シャネルが誇るリップグロスの名品『ルージュ ココ グロス』。従来のグロスにありがちな「重たい」「風で髪が唇にへばりつく」というネガティブな要素を最新のフォーミュラ技術で徹底的に解消し、極めてみずみずしく軽やかなテクスチャーを実現しています。",
        "desc_p2": "ホホバ、ヒマワリ、ミモザの3種の天然植物ワックスを融合させた独自の「ハイドラボースト コンプレックス」が、唇に触れた瞬間に体温でなめらかにメルト。薄膜のジェルフィルムとなって唇表面の凹凸を隙間なく埋め尽くし、光を均一に反射する極上の水光ツヤを生み出します。さらにオリゴペプチドが唇のハリと弾力をサポート。冬の乾いた空気の中でも唇が乾かず、上品で落ち着きのある洗練された大人の口元を一日中維持できます。",
        "target": "ベタつかない上質なリップグロスを求める方、フォーマルな場やビジネスシーンでも浮かない上品なツヤを好む方、大人の品格を演出したい方",
        "point": "付属のココーンアプリケーターの湾曲した面で下唇の中央にたっぷりと乗せ、輪郭に向けて薄くぼかすと、計算されたグラデーションツヤが手に入ります。"
    },
    {
        "rank": 5,
        "tag": "💧 水滴のような微細ラメが煌めく！水光ガラス膜で冬の乾燥唇をラッピングする韓国バズコスメ",
        "catch": "SNSで大バズり！プランプ効果のあるウォーターグロス。手持ちのどんなリップも一瞬で韓国アイドル級のちゅるん唇へ",
        "brand_name": "rom&nd (ロムアンド)",
        "capacity": "4.3g（シリコンスパチュラタイプ）",
        "type": "水光ガラス膜プランプリップグロス",
        "features": "スイートアーモンドオイル、メントール、微細偏光パール、シリコン製フラットスパチュラ",
        "value": "プチプラとは思えない美しいガラスツヤ。シリコンスパチュラ採用で口紅の上から重ねても色が濁らず拭き取りやすい神設計",
        "desc_p1": "韓国コスメブームを牽引するロムアンドの『グラスティング ウォーター グロス』は、まるで水滴の膜を唇にピンと張ったかのような「水光（ムルグァン）ガラスツヤ」を叶える大人気グロスです。冬の寒冷でくすみがちな唇に、繊細な多色偏光ラメが星屑のようにキラキラと反射し、圧倒的な透明感を与えてくれます。",
        "desc_p2": "スイートアーモンドオイルをはじめとする保湿成分が唇をしっかり包み込み、冬の乾燥風から唇をガード。メントールによる心地よいクーリングプランプ効果で唇の縦ジワをフラットに整えます。特筆すべきは、アプリケーターが一般的なフロッキー毛ではなく「透明なシリコンスパチュラ」になっている点。ティントや濃い色の口紅の上に重ねて使っても、使用後にティッシュでサッと拭き取れるため、ボトル内の液を濁らせず衛生的に使い続けられます。",
        "target": "韓国アイドルのような水光ツヤ唇（ちゅるんリップ）を作りたい方、手持ちのリップの色を邪魔せずにラメとツヤだけを足したい方",
        "point": "ティントを塗ってしっかり定着させた後、このグロスを唇全体に擦らず「置くように」塗布すると、色の層とツヤの層が分離して綺麗な2層ガラス膜が完成します。"
    },
    {
        "rank": 6,
        "tag": "🌶️ カプサイシン誘導体＆ヒアルロン酸！ドラッグストアで買えるプチプラ最高峰のぷっくり厚膜",
        "catch": "千円台前半で手に入る奇跡のプランプ力。濃厚な厚みのあるジェル膜が冬のガサガサ皮剥けを瞬時に封印",
        "brand_name": "CANMAKE (キャンメイク)",
        "capacity": "チューブ / スパチュラタイプ",
        "type": "高保湿ボリュームプランプリップグロス",
        "features": "トウガラシ果実エキス（カプサイシン誘導体）、ヒアルロン酸Na、加水分解コラーゲン、ミネラルオイル",
        "value": "学生から大人まで圧倒的支持を誇るキャンメイクの技術力。デパコス級のプランプ感と保湿ラッピングをドラコス価格で実現",
        "desc_p1": "「プランプリップを試してみたいけれど、いきなり数千円のデパコスを買うのは迷う…」という全コスメユーザーの味方が、キャンメイクの『ボリューミーリップグロス』です。ドラッグストアで気軽に手に入る価格設定でありながら、カプサイシン誘導体とヒアルロン酸を贅沢に配合し、デパコスの名品に匹敵するプランプ効果を発揮します。",
        "desc_p2": "テクスチャーは適度な粘度と厚みを持つ濃密ジェルタイプ。冬の乾燥でガサガサに皮剥けしてしまった唇の上に乗せると、厚膜ジェルが凹凸をフラットに埋め立ててラップのように密封します。じんわりとした温感が唇を刺激し、血色の悪い冬の唇にポッと自然なピンクの温もりをプラス。ポーチに1本入れておくだけで、外出先での急激な乾燥やメイク直しに絶大な安心感をもたらしてくれます。",
        "target": "コスパ最強のリッププランパーを探している方、ドラッグストアで手軽に購入したい方、厚みのある密着ツヤが好きな方",
        "point": "リップクリームを塗らずに直接このグロスを塗布することで、プランプ成分がダイレクトに唇に作用し、最大限のボリュームアップ効果を引き出せます。"
    },
    {
        "rank": 7,
        "tag": "💎 みずみずしい濃密ジェルが唇にピタッとフィット！透明感あふれる濡れたような立体ツヤが持続",
        "catch": "スプーン型スパチュラですくって乗せる新感覚。ぷるんとしたゼリーのような厚みと透明感が一日中崩れない",
        "brand_name": "RMK (アールエムケー)",
        "capacity": "5.5g（スプーン型スパチュラ）",
        "type": "高密着ジェルリップグロス",
        "features": "濃密ジェリーポリマー、オリーブ果実油、アーモンド油、ローズヒップ油（カニナバラ果実油）",
        "value": "発売以来数々のベスコスを受賞し続けるRMKの伝説的グロス。独自のジェリー膜が唇の動きにしなやかに追従する秀逸な処方",
        "desc_p1": "透明感メイクのパイオニアであるRMKを代表する名品『リップジェリーグロス』。従来のリップグロスとは一線を画す「濃密なジェリーポリマー」を採用しており、まるで唇の上に透明なゼリーを薄く広げたかのような、ぷるんとしたみずみずしい立体ツヤを演出します。",
        "desc_p2": "オリーブ果実油やアーモンド油などの植物オイルが唇をじんわりと潤し、冬の過酷な乾燥風に晒されてもツヤの膜が割れたり乾いたりしません。付属のスプーン型スパチュラが秀逸で、適量のジェリーをすくい取って下唇の中央に乗せ、唇を軽くすり合わせるだけで均一な濡れツヤ膜が完成。冬のコートやマフラーの重たい装いに対して、顔全体にパッと垢抜けた透明感と軽やかさをプラスしてくれます。",
        "target": "ゼリーのようなぷるんとした弾力ツヤが好きな方、手持ちの口紅のニュアンスチェンジを楽しみたい方、乾燥崩れを防ぎたい方",
        "point": "スプーンのくぼんだ面で唇の中央に多めにジェリーを乗せ、外側に向かって薄く伸ばすと、光が集まるハイライト効果で唇が立体的に見えます。"
    },
    {
        "rank": 8,
        "tag": "👘 ワックスと美容オイルの黄金比！素の唇を洗練された大人の潤いツヤでラッピングするSUQQU",
        "catch": "素の唇の色を引き立てる絶妙な透け感。冬の乾いた唇を品格ある湿度感で包み込む大人世代のための名作",
        "brand_name": "SUQQU (スック)",
        "capacity": "5.4g",
        "type": "高密着ラッピング美容液リップグロス",
        "features": "ラッピングオイルワックス処方、スクワラン、ホホバ種子油、シア脂、ヒアルロン酸",
        "value": "大人の肌色を最も美しく引き立てるSUQQUの計算された色艶。派手すぎず上品な「濡れ艶」で乾燥唇を気高く格上げ",
        "desc_p1": "大人の女性たちから圧倒的な信頼を集めるSUQQUの『トリートメント ラッピング リップ』。冬の唇に若々しいハリと洗練された艶を取り戻すために開発された本品は、従来のグロスの「ツヤツヤしすぎて子供っぽく見えてしまう」という悩みを完全に払拭する、計算し尽くされた大人のためのリップグロスです。",
        "desc_p2": "最大の特徴は、高粘度ワックスと厳選された美容オイルを黄金比で配合した「ラッピング処方」。塗った瞬間に唇の水分をギュッと閉じ込め、まるで上質な薄絹を一枚重ねたかのような上品で落ち着いた湿度感ある艶を生み出します。冬の暖房下でも乾燥ジワが浮き出ず、夕方になってもふっくらとした美しいフォルムをキープ。派手なラメに頼らず、素の唇そのものが潤っているかのような洗練された仕上がりを叶えます。",
        "target": "30代〜50代で上品な大人のリップメイクを楽しみたい方、派手なラメやギラギラしたツヤが苦手な方、確かな保湿持続力を求める方",
        "point": "冬のシックな装い（ウールコートやカシミヤニット）に合わせる際、口紅を塗らずにこのラッピングリップを直塗りするだけで、抜け感のある知的な美しさが完成します。"
    },
    {
        "rank": 9,
        "tag": "🌿 植物由来オイル×アミノ酸誘導体！界面活性剤やタール色素フリーで荒れやすい冬の唇を守る",
        "catch": "クレンジング不要で石けんオフ可能。冬の乾燥でピリつきやすい超敏感な唇にも安心の低刺激ミネラル処方",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "6.7g",
        "type": "低刺激ミネラルプランパーリップ美容液",
        "features": "アミノ酸誘導体、ウラボシヤハズエキス、ビルベリー種子油、トウガラシ果実エキス、タール色素フリー・鉱物油フリー",
        "value": "敏感肌コスメのエトヴォスが放つスキンケア発想のプランパー。唇の皮剥けや炎症を繰り返す冬のデリケート肌を優しくケア",
        "desc_p1": "冬になると唇がすぐに荒れて皮が剥け、市販のリップグロスや口紅を使うとヒリヒリ刺激を感じてしまう…という敏感肌の方に絶大な支持を受けるのが、エトヴォスの『ミネラルリッププランパー シアー』です。石油系界面活性剤、鉱物油、シリコン、タール系色素、合成香料を完全不使用の低刺激処方を誇ります。",
        "desc_p2": "植物由来の保湿オイルと保水アミノ酸誘導体が、荒れた角層バリアを優しく包み込み、潤いを与えながら健やかな状態へと導きます。マイルドな温感をもたらす植物エキス（ウラボシヤハズエキス等）が、敏感肌に負担をかけずに自然なふっくら感と血色感をサポート。シアーな発色で唇本来の透明感を引き出し、石けんとぬるま湯だけでスルリとオフできるため、クレンジングによる冬の摩擦ダメージも完全にゼロに抑えられます。",
        "target": "唇の皮膚が弱く口紅やグロスで荒れやすい敏感肌の方、石けんオフメイクを実践している方、自然派の優しいプランプ感を求める方",
        "point": "乾燥がひどい日はリップクリーム代わりにこまめに塗り直すことで、一日中荒れを防ぎながらナチュラルなツヤメイクをキープできます。"
    },
    {
        "rank": 10,
        "tag": "👑 ボタニカルオイル8種を贅沢ブレンド！冬の唇の縦ジワを瞬時にぼかしふっくら立体リフト",
        "catch": "プロのメイクアップアーティストが絶賛するリッチな処方。美容液のように溶け込み唇のエイジングサインを払拭",
        "brand_name": "BOBBI BROWN (ボビイ ブラウン)",
        "capacity": "6ml",
        "type": "エイジングケア高保湿プランプリップセラム",
        "features": "アボカドオイル、ホホバオイル、オリーブ油等8種のボタニカルオイル複合体、ヒアルロン酸、ペプチド",
        "value": "ニューヨーク発プロフェッショナルメイクの最高峰。唇の小ジワを瞬時にプランプアップさせて華やかな立体美を構築",
        "desc_p1": "世界中のバックステージで活躍するメイクアップアーティストから熱狂的に支持されるボビイ ブラウンの『エクストラ プランプ リップ セラム』。冬の寒冷と乾燥によってハリを失い、小ジワが目立ち始めた大人の唇のために開発された、ラグジュアリーな高機能リッププランパーです。",
        "desc_p2": "アボカド、ホホバ、オリーブなど厳選された8種類のボタニカルオイルを贅沢にブレンド。唇に乗せた瞬間、濃厚なセラムが体温でとろけて角層の奥まで染み渡り、乾燥によって萎縮した唇を内側から押し広げるようにふっくらとリフトアップさせます。微細なペプチド複合体が唇のコラーゲン構造をサポートし、使い続けるほどに素の唇そのものが柔らかく健康的な弾力を取り戻します。ホリデーの特別なメイクにも普段の日常ケアにも手放せなくなる一本です。",
        "target": "唇のエイジングサイン（縦ジワ・しぼみ・ハリ低下）が気になる方、プロ仕様の確かなボリュームアップ効果を実感したい方",
        "point": "リップメイクの最初のステップとして唇全体に馴染ませ、5分置いて唇がふっくら整ってから余分な液を軽くティッシュオフして口紅を塗ると、発色と持ちが劇的にアップします。"
    }
]

# 比較表データ生成
table_rows = []
for p, item in zip(gloss_details, items):
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
for p, item in zip(gloss_details, items):
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
            <div class="meta-item"><span class="meta-label">内容量：</span><span class="meta-value">{p['capacity']}</span></div>
            <div class="meta-item"><span class="meta-label">仕上がり：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要成分：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の乾燥唇＆ホリデーツヤに効く注目ポイント！</h4>
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
          <strong>✨ プロのメイクアップアドバイス：</strong>
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
        "q": "プランパー特有のピリピリ・スースー感は唇に悪影響はありませんか？",
        "a": "全く問題ありません。プランパーに含まれるピリピリ感や温感は、トウガラシ果実エキス（カプサイシン誘導体）やバニリルブチル、セイヨウハッカ（メントール）などの安全な食品由来・化粧品認可成分によって引き起こされています。これらは唇表面の毛細血管を一時的に心地よく刺激して血流を促し、内側からふっくらとボリュームアップさせるための作用です。刺激は通常15〜30分程度で自然に落ち着きます。ただし、唇に深い傷や強い炎症がある場合は使用を控え、ピュアな保湿オイル等でまず傷を治してください。"
    },
    {
        "q": "冬の外出時、風やマフラーでグロスが髪にくっつくのを防ぐ塗り方はありますか？",
        "a": "髪やマフラーの付着を防ぐ秘訣は「塗る範囲のコントロール」です。唇の輪郭全体にたっぷり塗ってしまうと髪が触れやすくなるため、グロスを塗る際は『唇の中央（内側2/3）』に重点的に乗せ、外側の輪郭付近は指先やブラシで極めて薄くぼかすだけに留めましょう。中央に光が集まることで立体的なぷっくりツヤを際立たせつつ、風でなびいた髪が唇の端にくっつくストレスを劇的に減らすことができます。"
    },
    {
        "q": "手持ちの口紅やマットリップと綺麗に重ねるコツは？",
        "a": "口紅を塗った直後にグロスを強く擦り合わせるように重ねると、口紅の色がヨレてチップも汚れてしまいます。まず口紅を塗った後、軽くティッシュオフして余分な油分を抑えて密着させます。その上から、グロスをチップの先端でポンポンと置くように軽くタッピングしながら乗せるのがプロの技です。シリコンスパチュラタイプのグロス（ロムアンド等）を使うか、指先に取って乗せると口紅の色移りを防げます。"
    },
    {
        "q": "プランプリップグロスは夜寝る前のリップケアとしても使えますか？",
        "a": "ラメや着色料が含まれておらず、植物オイルやヒアルロン酸主体の製品（クラランスやディオールの無色タイプ、エトヴォス等）であれば、夜の集中リップケアとしても非常に優秀です。睡眠中にエアコン暖房の風で唇が乾燥するのを高粘度オイル膜が完璧に防ぎ、翌朝起きたときに縦ジワのないぷるんとした潤い唇を保つことができます。強いカプサイシン刺激が気になる方は、刺激の少ないオイル系を選ぶとリラックスして眠れます。"
    },
    {
        "q": "リップオイルとリップグロスは何が違いますか？",
        "a": "リップオイルはサラリとした質感で角層深部へのオイル浸透とケアを最優先したアイテムですが、リップグロスは高粘度のワックスやポリマーを配合し、唇表面に厚みのあるフィルム膜を形成して『立体的なガラスツヤ』と『外部刺激からの密封ラッピング効果』を長時間持続させる点に特化しています。特に冬の強い寒風やエアコン下では、膜が蒸発しにくいリップグロスのほうが高い保護持続力を発揮します。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(gloss_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {item['display_name']}",
        "image": item['image_url'],
        "description": p['catch'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "price": str(item['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock",
            "url": item['affiliate_url']
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10",
    "description": "11月・12月の冬の唇乾燥・縦ジワ・皮剥け・血色レスを徹底解決！ディオール、クラランス、ジルスチュアート、シャネル、ロムアンド、キャンメイク、RMK、SUQQUなど、カプサイシンや濃密植物オイルで唇をふっくら満たしホリデーの濡れツヤをキープする最強高保湿プランプリップグロス10選を徹底比較！",
    "image": items[0]['image_url'],
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ"
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

json_ld_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": fq["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": fq["a"]
            }
        } for fq in faq_items
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
            "name": "高保湿プランプリップグロス特集",
            "item": "https://lumi-cosme.vercel.app/winter-lip-gloss"
        }
    ]
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿プランプリップグロスおすすめ人気ランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の唇乾燥・縦ジワ・皮剥け・血色レスを徹底解決！ディオール、クラランス、ジルスチュアート、シャネル、ロムアンド、キャンメイク、RMK、SUQQUなど、カプサイシンや濃密植物オイルで唇をふっくら満たしホリデーの濡れツヤをキープする最強高保湿プランプリップグロス10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-lip-gloss">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10">
  <meta property="og:description" content="11月・12月の冬の唇乾燥・縦ジワしぼみを徹底解決！カプサイシンや濃密植物オイルで唇をふっくら満たしホリデーの濡れツヤをキープする最強高保湿プランプリップグロス10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lip-gloss">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！高保湿プランプリップグロスランク10">
  <meta name="twitter:description" content="11月・12月の冬の唇乾燥・縦ジワしぼみを解消！最強高保湿プランプリップグロス10選を本音レビュー！">
  <meta name="twitter:image" content="{items[0]['image_url']}">

  <!-- 構造化データ JSON-LD -->
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
      --primary: #e11d48;
      --primary-dark: #be123c;
      --primary-light: #fff1f2;
      --accent: #f43f5e;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #fffbfb;
      --card-bg: #ffffff;
      --border: #ffe4e6;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 960px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ヘッダー */
    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid #e2e8f0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 68px;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .site-nav a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 500;
      transition: color 0.2s;
    }}
    .site-nav a:hover {{ color: var(--primary); }}

    /* パンくずリスト */
    .breadcrumb {{
      padding: 16px 0;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .breadcrumb span {{ margin: 0 8px; }}

    /* 記事ヘッダー */
    .article-header {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 40px;
      margin-bottom: 32px;
      box-shadow: var(--shadow);
      border: 1px solid #fecdd3;
    }}
    .article-tag-wrap {{
      display: flex;
      gap: 8px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 9999px;
      font-size: 0.8rem;
      font-weight: 700;
      background: var(--primary-light);
      color: var(--primary);
    }}
    .article-title {{
      font-size: 2rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .article-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.9rem;
      color: var(--text-muted);
    }}

    /* 本文コンテンツ */
    .article-body {{
      display: flex;
      flex-direction: column;
      gap: 32px;
    }}

    .intro-box, .guide-box, .summary-box {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px;
      box-shadow: var(--shadow);
      border: 1px solid #fecdd3;
    }}
    .intro-box p, .guide-item p, .summary-box p {{
      margin-bottom: 16px;
      font-size: 1.05rem;
    }}
    .intro-box p:last-child, .guide-item p:last-child, .summary-box p:last-child {{
      margin-bottom: 0;
    }}

    .guide-box h2, .ranking-section h2, .comparison-section h2, .faq-section h2, .summary-box h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary-light);
      position: relative;
    }}
    .guide-box h2::after, .ranking-section h2::after, .comparison-section h2::after, .faq-section h2::after, .summary-box h2::after {{
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 60px;
      height: 2px;
      background: var(--primary);
    }}

    .guide-item {{
      margin-bottom: 24px;
    }}
    .guide-item:last-child {{
      margin-bottom: 0;
    }}
    .guide-item h3 {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* 比較表 */
    .table-wrap {{
      overflow-x: auto;
      margin-top: 16px;
      border-radius: 12px;
      border: 1px solid #fecdd3;
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.95rem;
      text-align: left;
      background: #ffffff;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid #fecdd3;
      vertical-align: middle;
    }}
    .comparison-table th {{
      background: #fff1f2;
      font-weight: 700;
      color: #9f1239;
      white-space: nowrap;
    }}
    .comparison-table tr:hover {{
      background-color: #fff1f2;
    }}
    .rank-cell {{
      font-weight: 800;
      color: var(--primary);
      white-space: nowrap;
    }}
    .brand-cell strong {{
      color: #0f172a;
    }}
    .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    /* ランキングカード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 36px;
      box-shadow: var(--shadow);
      border: 1px solid #fecdd3;
      position: relative;
      margin-bottom: 40px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(225, 29, 72, 0.1);
    }}
    .product-badge {{
      position: absolute;
      top: -16px;
      left: 36px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #ffffff;
      font-weight: 800;
      font-size: 1.1rem;
      padding: 6px 20px;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.3);
    }}
    .product-header {{
      margin-top: 10px;
      margin-bottom: 20px;
    }}
    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 4px 12px;
      border-radius: 6px;
      margin-bottom: 8px;
    }}
    .product-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 8px;
    }}
    .product-catch {{
      font-size: 1rem;
      color: var(--primary-dark);
      font-weight: 600;
    }}

    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 28px;
      margin-bottom: 24px;
      background: #fff5f5;
      padding: 24px;
      border-radius: 12px;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
      .article-header {{ padding: 24px; }}
      .article-title {{ font-size: 1.5rem; }}
      .product-card {{ padding: 24px; }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #ffffff;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #fecdd3;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 240px;
      object-fit: contain;
      border-radius: 4px;
    }}
    .product-meta-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.95rem;
      margin-bottom: 16px;
    }}
    .meta-item {{
      display: flex;
      gap: 8px;
    }}
    .meta-label {{
      font-weight: 700;
      color: #475569;
      min-width: 90px;
    }}
    .meta-value {{
      color: #0f172a;
    }}
    .price-val {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #e11d48;
    }}
    .product-points {{
      background: #ffffff;
      padding: 16px;
      border-radius: 8px;
      border-left: 4px solid var(--primary);
    }}
    .product-points h4 {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 6px;
    }}
    .product-points p {{
      font-size: 0.9rem;
      color: #475569;
      line-height: 1.6;
    }}

    .product-description {{
      margin-bottom: 24px;
    }}
    .product-description h4 {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
    }}
    .product-description p {{
      font-size: 1rem;
      color: #334155;
      margin-bottom: 12px;
      line-height: 1.8;
    }}

    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 16px;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}
    .target-block {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      color: #1e3a8a;
    }}
    .tip-block {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      color: #9f1239;
    }}
    .advice-block strong {{
      display: block;
      margin-bottom: 6px;
    }}

    .product-action {{
      text-align: center;
      margin-top: 20px;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      max-width: 440px;
      background: linear-gradient(135deg, #bf0000, #e60012);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 16px 24px;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(230, 0, 18, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a30000, #cc0010);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(230, 0, 18, 0.35);
    }}

    /* FAQ */
    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .faq-item {{
      background: #ffffff;
      border: 1px solid #fecdd3;
      border-radius: 12px;
      padding: 24px;
    }}
    .faq-q {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-q span {{
      color: var(--primary);
      font-size: 1.3rem;
      line-height: 1;
    }}
    .faq-a {{
      font-size: 1rem;
      color: #334155;
      line-height: 1.8;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-a span {{
      color: #e11d48;
      font-weight: 800;
      font-size: 1.1rem;
      line-height: 1;
    }}

    /* フッター */
    .site-footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 40px 0;
      margin-top: 60px;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      text-align: center;
    }}
    .footer-copy {{
      margin-top: 16px;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="site-logo">
        <span>✨ 冬コスメ徹底比較ラボ</span>
      </a>
      <nav class="site-nav">
        <a href="/">トップページに戻る</a>
      </nav>
    </div>
  </header>

  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">ホーム</a>
      <span>&gt;</span>
      <a href="/winter-lip-gloss">高保湿プランプリップグロス特集</a>
    </nav>
  </div>

  <main class="container">
    <article class="article-body">
      <header class="article-header">
        <div class="article-tag-wrap">
          <span class="badge">冬の唇皮剥け・縦ジワ予防</span>
          <span class="badge">ホリデープランプ＆水光ガラスツヤ</span>
          <span class="badge">2026年最新徹底検証</span>
        </div>
        <h1 class="article-title">保湿力の強さで冬の唇乾燥・縦ジワしぼみとさようなら！ホリデーの煌めきとぷるんとした濃密ツヤが続く高保湿プランプリップグロスランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-02">2026年11月2日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入部 -->
      <section class="intro-box">
        <p>
          11月から12月へと街がイルミネーションで彩られるホリデーシーズン。クリスマスマーケットやディナー、忘年会など華やかなイベントが増える一方で、ふと鏡を見ると<strong>「唇の縦ジワが深く刻まれて口紅が綺麗に乗らない」「寒さで唇が青白く血色を失っている」「暖房の効いた室内で数時間過ごすと唇の皮がカサカサに剥けてくる」</strong>という悩みに直面していませんか。
        </p>
        <p>
          唇の皮膚は、顔の他の部位と比べて極めて特殊な解剖学的構造を持っています。角質層の厚さは頬の3分の1以下しかなく、汗腺も皮脂腺も一切存在しません。つまり、自前の皮脂膜を作って水分を閉じ込める機能が生まれつきゼロなのです。そのため、外気湿度が急激に下がる11月以降、冷たい木枯らしとエアコン暖房の温風にさらされると、唇内部の水分はわずか数十分で限界まで蒸発し、砂漠のように萎縮してしまいます。
        </p>
        <p>
          通常のリップクリームでは「油膜で覆うだけ」で根本的なボリュームアップや華やかさに欠け、マットリップでは縦ジワの影がより一層目立ってしまう――そんな冬の唇のジレンマを劇的に解決するのが、<strong>「高保湿プランプリップグロス」</strong>です。
        </p>
        <p>
          トウガラシ果実エキス（カプサイシン誘導体）やバニリルブチルといった温感プランプ成分が、冬の冷えで収縮した毛細血管の血流を優しく刺激。内側から押し上げるように唇をふっくらとボリュームアップさせ、血色の良い自然なピンク色の温もりを呼び覚まします。さらに、ヘーゼルナッツオイルやホホバオイル、高屈折率ポリマーが唇表面に水光フィルム膜を形成し、光を美しく乱反射させながら水分蒸散を鉄壁ブロック。ホリデーの夜空やイルミネーションの下で息をのむほど魅力的な、ぷるんと潤いに満ちた無敵の唇が一日中持続します。本記事では、11月・12月の冬に本当に買うべき実力派の高保湿プランプリップグロス10選を徹底検証し、ランキング形式で詳しくご紹介します。
        </p>
      </section>

      <!-- 特集セクション：なぜ冬の唇にプランプグロスが不可欠なのか -->
      <section class="guide-box" id="guide-section">
        <h2>なぜ冬の唇には「普通のリップ」より「プランプグロス」なのか？3つの美容解剖学的理由</h2>
        <div class="guide-item">
          <h3>1. 「皮脂膜ゼロ」の粘膜を、高粘度植物オイル＆ワックスが人工シールド</h3>
          <p>
            唇には自ら油分を分泌する皮脂腺が存在しないため、冬の乾燥から唇を守るには「人工的な強力バリア膜」を外から補給する以外に方法がありません。高保湿プランプリップグロスは、粘度の高い植物ワックスやエモリエントオイルを高密度に配合しており、塗った瞬間に唇の微細な凹凸を滑らかに埋めて密封。外部の乾いた空気との接触を完全に断ち切り、角層の水分を一日中逃しません。
          </p>
        </div>
        <div class="guide-item">
          <h3>2. カプサイシン＆バニリルブチルの「微小血流刺激」が内側から唇をふっくら膨らませる</h3>
          <p>
            冬の唇が萎縮して小さく見えたり縦ジワが深く見える最大の要因は、寒さによる「毛細血管の収縮と血行不良」です。プランパー特有の微細な温感刺激は、停滞していた唇の血流を一気に活性化させ、物理的に組織をふっくらと膨満（プランプ）させます。外から油分を塗るだけでなく、内側から細胞を押し広げる相乗アプローチこそが冬の縦ジワ消滅の鍵です。
          </p>
        </div>
        <div class="guide-item">
          <h3>3. 高屈折率ポリマーと微細ラメが「光の錯視」で縦ジワの影を完全に消滅</h3>
          <p>
            マットやシアーな口紅では、光がそのままシワの溝に入り込んで影を強調してしまいますが、リップグロスの高屈折率フィルム膜はあらゆる角度からの光を均一に乱反射します。ガラス玉のように光を集めて発光させることで、縦ジワの溝の影を光で飛ばし、肉眼でも写真でも滑らかで立体的な唇を演出します。
          </p>
        </div>
      </section>

      <!-- 選び方ガイド -->
      <section class="guide-box">
        <h2>失敗しない！冬用高保湿プランプリップグロスの賢い選び方3つの基準</h2>
        <div class="guide-item">
          <h3>① プランプ刺激の強弱と体感（カプサイシン系 vs 温感バニリル系 vs 低刺激ペプチド系）</h3>
          <p>
            プランパーの刺激感には個性があります。ディオールやキャンメイクのような「カプサイシン＋メントール」は強いジンジン感とともに瞬時のボリュームアップを誇ります。ジルスチュアートのような「バニリルブチル」は温かいポカポカ感が特徴。敏感肌の方やピリピリ感が苦手な方は、刺激成分ではなくペプチドやヒアルロン酸の浸透でふっくらさせるエトヴォスやSUQQUのような低刺激タイプが最適です。
          </p>
        </div>
        <div class="guide-item">
          <h3>② 配合オイルの純度とスキンケア効果（90%以上の美容液・スキンケア処方）</h3>
          <p>
            冬のグロス選びでは、見た目のツヤだけでなく「素の唇をケアする成分の含有率」が極めて重要です。チェリーオイル、ホホバオイル、ヘーゼルナッツオイル、スクワランなどの高品質な天然植物油がベースになっているアイテムを選べば、メイクを落とした後も唇が乾燥せず、使うほどに柔らかく整っていきます。
          </p>
        </div>
        <div class="guide-item">
          <h3>③ アプリケーターの形状と衛生面（シリコンスパチュラ・クッションチップ・スプーン型）</h3>
          <p>
            口紅の上から重ねて使う機会が多い冬のグロスは、チップの素材もチェックしましょう。シリコンスパチュラ型（ロムアンドなど）は使用後にティッシュで拭き取れてボトル内が濁りません。クッションチップ（クラランスなど）は摩擦レスで荒れた唇にも優しく塗布できます。
          </p>
        </div>
      </section>

      <!-- 徹底比較表 -->
      <section id="comparison" class="comparison-section">
        <h2>【徹底比較】冬の唇を満たす高保湿プランプリップグロススペック比較表</h2>
        <div class="table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>ブランド・商品名</th>
                <th>参考価格</th>
                <th>タイプ</th>
                <th>内容量</th>
                <th>主要成分・特徴</th>
              </tr>
            </thead>
            <tbody>
              {"".join(table_rows)}
            </tbody>
          </table>
        </div>
      </section>

      <!-- ランキング一覧 -->
      <section id="ranking" class="ranking-section">
        <h2>【2026年最新】11月・12月に買うべき高保湿プランプリップグロスランキング10選</h2>
        {"".join(product_cards_html)}
      </section>

      <!-- 実践テクニック -->
      <section class="guide-box">
        <h2>効果を最大化！プロ直伝「縦ジワを消し去る立体プランプグラデーションテク」</h2>
        <div class="guide-item">
          <h3>ステップ1：素の唇の油分をオフし、ティントや口紅を中央から塗る</h3>
          <p>
            ファンデーションや余分な皮脂が唇に残っているとグロスが滑ってしまうため、軽くティッシュオフします。お好みのティントや口紅を唇の内側から外側に向かってグラデーションになるよう塗り、1分ほど置いて唇にしっかり定着させます。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ2：プランプグロスを「唇の中央2/3」にだけタッピングして置く</h3>
          <p>
            グロスを塗る際は、全体にベタッと塗り広げるのではなく、上唇の山部分と下唇の中央にだけチップでポンポンと置くように重ねます。左右に擦り合わせず、光が集まるハイライトポイントを中央に集中させることが、小顔効果とぷっくり立体唇を作るプロの黄金律です。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ3：上唇の山のM字カーブにわずかにハイライトを光らせる</h3>
          <p>
            チップに残った微量のグロスで、上唇の山の頂点（キューピッドボウ）のキワをちょんと撫でるように光を仕込みます。このひと手間で人中がキュッと短縮されて見え、あどけなさと洗練された色気が同居する冬のホリデーメイクが完成します。
          </p>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section" class="faq-section">
        <h2>よくある質問（FAQ）：高保湿プランプリップグロスの疑問を徹底解決</h2>
        <div class="faq-list">
          {"".join([f'''
          <div class="faq-item">
            <h3 class="faq-q"><span>Q.</span> {fq["q"]}</h3>
            <p class="faq-a"><span>A.</span> {fq["a"]}</p>
          </div>
          ''' for fq in faq_items])}
        </div>
      </section>

      <!-- まとめセクション -->
      <section class="summary-box">
        <h2>まとめ：冬の乾燥唇は「高保湿プランプグロス」でぷるんとうるおう主役に格上げしよう</h2>
        <p>
          11月から12月にかけての寒気と暖房乾燥は、顔の中で最も皮膚が薄い唇に真っ先に容赦ないダメージをもたらします。ガサガサに皮が剥けて血色を失った唇では、せっかくの冬のホリデーファッションやメイクも台無しになってしまいます。
        </p>
        <p>
          今回厳選した最新の高保湿プランプリップグロスを取り入れれば、ひと塗りで内側から血色とボリュームが満ち溢れ、冬の街のイルミネーションを美しく反射するみずみずしい濡れツヤを手に入れることができます。乾燥の季節だからこそ、ぷるんと潤った無敵のリップで自信に満ちた笑顔あふれる冬を過ごしてください。
        </p>
      </section>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p class="footer-copy">&copy; 2026 冬コスメ徹底比較ラボ - All Rights Reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-lip-gloss.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✓ Created winter-lip-gloss.html successfully!")
