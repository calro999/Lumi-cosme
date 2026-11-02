import json
import re

with open("fetched_3new_nov_dec_ceramide_lotion_lip_squalane_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_ceramide_lotion"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 圧倒的コスパ×3種のヒト型セラミド！全身に浴びるように使える大容量の最高峰",
        "catch": "500mlでヒト型セラミドを贅沢配合。惜しみなく重ね付けして真冬の角層を水分で満たす殿堂入りローション",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "500ml (スキンコンディショナー 高保湿)",
        "type": "ヒト型セラミド配合・弱酸性高保湿化粧水",
        "features": "ヒト型セラミド（AP・NP・EOP）、ヒアルロン酸、コラーゲン、アミノ酸、ハトムギ種子エキス",
        "value": "ドラッグストアで手に入るプチプラ化粧水の常識を覆した名作。浸透性に優れたヒト型セラミドを3種類配合し、顔だけでなく乾燥で粉吹くボディまで贅沢に潤す",
        "desc_p1": "11月中旬から12月にかけて湿度が急激に下がる日本の冬は、洗顔直後から角質層の水分が猛スピードで蒸散します。高価な化粧水を少量ケチケチ使うよりも、良質な保湿成分を高配合した化粧水をたっぷりと惜しみなく肌に吸わせることが、冬のバリア機能維持における鉄則です。その理想を最も高次元で具現化したのがセザンヌの『スキンコンディショナー 高保湿』です。",
        "desc_p2": "人の皮膚にあるセラミドと酷似した立体構造を持つ3種のヒト型セラミド（AP・NP・EOP）を核に、ヒアルロン酸やアミノ酸などのNMF（天然保湿因子）成分をバランスよくブレンド。少し白濁したまろやかなテクスチャーながら、肌にのせるとスッと角層深くまで浸透し、ベタつきを残さずみずみずしい潤いを与えます。無香料・無着色・無鉱物油・アルコールフリーの弱酸性処方なので、寒風で敏感に傾いた肌にも刺激なく吸い付きます。",
        "target": "朝晩バシャバシャと重ね付けして内側から潤したい方、お風呂上がりに顔からデコルテ・全身まで一気に保湿したい方、圧倒的なコスパを求める方",
        "point": "手のひらに500円玉大を出し、ハンドプレスで優しく押し込む工程を2〜3回繰り返す『ミルフィーユ保水』が劇的に効果的です。コットンに浸して3分間の集中パックもおすすめ。"
    },
    {
        "rank": 2,
        "tag": "🌿 5種のヒト型セラミド×大豆発酵エキス！濃厚なとろみで乾ききった角層をほぐす高保水水",
        "catch": "老舗油脂メーカーの皮膚科学。角層の水分保持力を根本から底上げする濃密モイストリッチ処方",
        "brand_name": "松山油脂 (M mark)",
        "capacity": "120ml (肌をうるおす保湿スキンケア 保湿浸透水 モイストリッチ)",
        "type": "5種のヒト型セラミド＆大豆由来成分配合・低刺激高保湿化粧水",
        "features": "ヒト型セラミド1・2・3・5・6II、ダイズ種子エキス、大豆発酵エキス、ヒアルロン酸Na、無香料・アルコールフリー",
        "value": "人間の角質細胞間脂質を構成する主要なヒト型セラミドを5種類網羅。とろみのある美容液のようなリッチな感触で、冬のゴワついた角質を柔らかくほぐす",
        "desc_p1": "冬の寒さによって肌の血行が悪くなると、ターンオーバーが乱れて古い角質が硬く蓄積し、化粧水が肌表面で弾かれて浸透しにくくなる『ゴワつき現象』が起きます。松山油脂の『肌をうるおす 保湿浸透水 モイストリッチ』は、そんな真冬の硬化肌を解きほぐすために生まれた高保湿設計です。",
        "desc_p2": "ヒト型セラミドを5種配合しているだけでなく、角層の水分保持をサポートする大豆胚芽抽出液や大豆発酵エキスを凝縮。手のひらに出すと美容液のようにリッチなとろみがありながら、肌に乗せた瞬間にまろやかに崩れて角層深部へ吸い込まれていきます。アルコールやパラベン、香料を徹底排除したクリーンな無添加設計で、真冬のエアコン暖房によるピリつきや赤みが生じやすい敏感肌でも、吸い付くようなもっちり素肌を取り戻せます。",
        "target": "冬になると肌が硬くゴワついて化粧水が入らない方、とろみのある高保湿化粧水が好みの方、無添加で低刺激な処方にこだわりたい方",
        "point": "適量を手のひらで包むように温めてから、顔の内側から外側へじっくりとハンドプレス。手のひらが肌にピタッと吸い付くまで押し込むことで浸透力が最大化します。"
    },
    {
        "rank": 3,
        "tag": "💉 ヘパリン類似物質×セラミド類似成分！保水有効成分で真冬の肌構造を根本から立て直す",
        "catch": "コーセー×マルホの医療発想。肌の保水メカニズムを再活性化させ、過酷な暖房下でも乾燥知らずへ",
        "brand_name": "Carte HD (カルテHD)",
        "capacity": "150ml (モイスチュア ローション / 医薬部外品)",
        "type": "医薬部外品・ヘパリン類似物質HD＆セラミド類似ポリマー配合高保湿化粧水",
        "features": "ヘパリン類似物質HD（保水有効成分）、グリチルリチン酸ジカリウム（消炎有効成分）、セラミド類似ポリマー、アミノ酸",
        "value": "皮膚科領域の保水有効成分ヘパリン類似物質と、コーセー独自のセラミド類似ポリマーが融合。荒れ果てた肌のラメラ構造を整えて持続保水を叶える",
        "desc_p1": "乾燥肌治療の医療現場で長年用いられてきた保水有効成分『ヘパリン類似物質』を、毎日のスキンケアに最適化させたカルテHD。11月・12月の冬本番に、どんな保湿クリームを重ねても内側から乾いて突っ張ってしまう『深層乾燥肌』に最も確かな手応えをもたらす薬用ローションです。",
        "desc_p2": "ヘパリン類似物質HDが肌の基底層付近まで働きかけて保水構造を整え、角層ラメラ構造をサポートするセラミド類似ポリマーが水分をがっちり抱え込みます。さらに抗炎症成分グリチルリチン酸ジカリウムが、寒暖差によるヒリつきや肌荒れを穏やかに鎮静。エモリエントカプセル技術により、まろやかな化粧液が肌に溶け込み、まるで保護マスクで包まれたような安心感が長時間持続します。",
        "target": "何を塗っても夕方には頬がカサつく深刻な乾燥肌、エアコン暖房の風で肌がピリピリする方、製薬技術に基づいた確かな保水力を求める方",
        "point": "洗顔後すぐに500円玉大を取り、顔全体になじませたあと、目元や口元の乾燥小ジワが気になるゾーンへ指先で軽くトントンと重ね付けしてください。"
    },
    {
        "rank": 4,
        "tag": "💎 浸透型ヒアルロン酸×ヒト型セラミド！角層をうるおいで膨潤させる濃密エイジング保水",
        "catch": "ミネラルコスメのエトヴォスが追求した高機能保湿。天然ラベンダーの香りに包まれる至福のスキンケア",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "150ml (モイスチャライジングローション)",
        "type": "ヒト型セラミド配合・天然ラベンダー精油香るリッチ保湿ローション",
        "features": "グルコシルセラミド、POs-Ca（ホスホリルオリゴ糖Ca）、リピジュア、ヒアルロン酸、天然ラベンダー花水",
        "value": "肌の水分保持力を高めるPOs-Caとセラミドの相乗効果。キメの乱れた冬の肌をみずみずしく膨らませ、後から使う美容液の馴染みを劇的に向上",
        "desc_p1": "冬の乾燥は角層のキメを萎縮させ、光の乱反射を奪ってどんよりとした『冬の乾燥くすみ』を引き起こします。エトヴォスの『モイスチャライジングローション』は、肌のバリア機能を整えながら、ふっくらとしたツヤと透明感を呼び覚ます高機能ローションです。",
        "desc_p2": "角層の水分保持力を育むPOs-Ca（ホスホリルオリゴ糖Ca）とセラミド前駆体を配合し、肌本来が持っている潤いを生み出す力をバックアップ。さらに高保水成分リピジュアとヒアルロン酸が、乾いた肌表面に潤いのヴェールを形成します。とろりとしたテクスチャーが肌の上でスッとほどけ、角層のすみずみまで浸透。天然ラベンダー精油の心地よいアロマが、真冬のスキンケア時間を贅沢な癒しのひとときに変えてくれます。",
        "target": "冬の乾燥によるくすみやキメの乱れが気になる方、ハリ・ツヤ不足を感じる30代・40代、精油の心地よい香りでリラックスしたい方",
        "point": "500円玉大を手にとり、手のひら全体を使って顔を包み込むようにハンドプレス。深呼吸しながらラベンダーの香りを楽しむことで自律神経の緊張もほぐれます。"
    },
    {
        "rank": 5,
        "tag": "🔬 8種の天然型セラミドを高圧乳化！洗顔後すぐに角層バリアを先行再建する新世代ローション",
        "catch": "ロート製薬のセラミド先端技術。壊れやすい冬のバリア膜を最初のステップで隙間なく補強",
        "brand_name": "ロート製薬 ケアセラ",
        "capacity": "130ml (ケアセラ AP 高保湿先行バリア乳液・ローション)",
        "type": "8種の天然型セラミド配合・先行バリア型高保湿マイクロローション",
        "features": "天然型セラミド（セラミド1・2・3・6II・EOS・カプロオイルフィトスフィンゴシン・カプロオイルスフィンゴシン）、ペプチドCP、ワセリン微細化配合",
        "value": "ドラッグストアで手に入る最高峰のセラミド配合数。洗顔直後の無防備な素肌に、角質細胞間脂質そのものを補給して乾燥の侵入を水際で食い止める",
        "desc_p1": "洗顔や入浴の直後は、皮脂膜やセラミドが洗い流されて肌が無防備な状態に晒されています。特に11月〜12月の低湿度下では、洗顔後わずか数分で水分が失われます。ケアセラAPは、この最も乾燥しやすいタイミングで角層バリアを先行修復するために設計された革新的なアイテムです。",
        "desc_p2": "皮膚科学に基づき厳選された8種類もの天然型セラミドに加え、肌のセラミド産生を促すペプチドCPを高配合。高圧乳化技術によって微細化されたワセリンとセラミドが、化粧水のようにみずみずしく広がりながらも、乳液のような高いシールド力を発揮します。洗顔後すぐに馴染ませることで、乾燥で硬くなった肌が瞬時に柔らかく解きほぐされ、後から重ねるアイテムの浸透も見違えるほどスムーズになります。",
        "target": "洗顔後すぐに肌がつっぱる・赤くなる方、セラミドを高濃度で補給したい方、敏感肌で肌荒れを繰り返しやすい方",
        "point": "洗顔後、タオルドライした直後に1〜2プッシュを手に取り、優しく顔全体に広げます。乾燥が気になる首元やデコルテまで伸ばすのがおすすめです。"
    },
    {
        "rank": 6,
        "tag": "💨 微細化セラミド機能成分が角層深部へシュッ！メイクの上からも真冬の砂漠肌を即レスキュー",
        "catch": "キュレルの独自技術でセラミドを微細スプレー化。いつでもどこでも全身に瞬時バリア補給",
        "brand_name": "Curel (キュレル)",
        "capacity": "250g (ディープモイスチャースプレー / 医薬部外品)",
        "type": "医薬部外品・微細化セラミド機能成分配合ミスト状高保湿化粧水",
        "features": "微細化セラミド機能成分、アラントイン（消炎有効成分）、ユーカリエキス、無香料・弱酸性",
        "value": "水分子よりも細かいレベルでセラミド機能成分をスプレー化。お風呂上がりの秒速保湿から、日中のエアコン直撃肌への水分補給まで万能に活躍",
        "desc_p1": "真冬のオフィスや室内で一日中過ごしていると、エアコン暖房の温風によって肌の水分が奪われ、夕方には頬がつっぱりメイクが粉を吹いてしまうことがあります。そんな日中のレスキューアイテムとして美容業界でも絶賛されているのがキュレルの『ディープモイスチャースプレー』です。",
        "desc_p2": "花王の独自技術によってセラミド機能成分を超微細なミスト状に分散。ひと吹きするだけでシルクのような霧が顔全体を均一に包み込み、メイクを崩すことなく角層深くまで潤いを届けます。さらに消炎有効成分アラントイン配合で、冬の冷風でヒリつく肌の炎症を穏やかに抑制。250gの大容量ボトルは逆さまでもスプレーできるため、冬にカサつきやすい背中や脚の保湿にもストレスフリーに使えます。",
        "target": "日中の暖房下で肌の乾燥やつっぱりを感じる方、お風呂上がりに素早く全身を保湿したい方、背中や手の届かない部分もケアしたい方",
        "point": "肌から約20cm離し、円を描くようにスプレーした後、手のひらで軽く押さえます。メイク直しの際はティッシュで余分な皮脂を押さえてからスプレーすると密着度が高まります。"
    },
    {
        "rank": 7,
        "tag": "🍶 アミノ酸×セラミド×純米発酵の力！酒蔵の知恵が息づく濃密しっとり大容量ローション",
        "catch": "一升瓶まるごとのアミノ酸を凝縮。吸い付くようなもっちり素肌へ導く日本酒コスメの金字塔",
        "brand_name": "菊正宗 (きくまさむね)",
        "capacity": "500ml (日本酒の化粧水 高保湿)",
        "type": "日本酒（コメ発酵液）＆セラミド・アミノ酸配合・高保湿大容量化粧水",
        "features": "コメ発酵液、ヒト型セラミド（NP・AP・EOP）、アミノ酸（アルギニン・グルタミン酸・ロイシン等）、プラセンタエキス、アルブチン",
        "value": "老舗酒蔵のコメ発酵エキスにヒト型セラミド3種をプラス。日本酒に含まれる天然アミノ酸が角層を柔らかく満たし、冬の乾燥くすみを一掃",
        "desc_p1": "古くから杜氏（とうじ）の手が白く美しいことに着目して開発された菊正宗のスキンケアシリーズ。その看板商品である高保湿化粧水は、日本酒一升分のアミノ酸とヒト型セラミドを贅沢にブレンドした超実力派のロングセラーアイテムです。",
        "desc_p2": "肌の構成要素であるアミノ酸が角層の角質細胞内部（NMF）を潤し、ヒト型セラミドが細胞と細胞の間を埋めて水分の蒸散を徹底ガード。ほんのり甘い日本酒の香りが広がり、とろみのあるリッチなテクスチャーが肌の上でするすると伸びて吸い付くようなモチモチ感を与えます。500mlのポンプ式ボトルで手軽に使え、冬のお風呂上がりに家族全員で全身の乾燥対策として愛用できる圧倒的な安心感があります。",
        "target": "アミノ酸とセラミドの両方をたっぷりと補給したい方、ボディの粉吹き乾燥も一緒にケアしたい方、手軽なポンプ式を好む方",
        "point": "お風呂上がりに全身へ惜しみなく伸ばした後、乾燥しやすい顔には2〜3プッシュを重ね付け。コットンパックとして使えば、エステ上がりのような透明感が蘇ります。"
    },
    {
        "rank": 8,
        "tag": "🧪 原液5%高配合の超濃密アプローチ！サロン品質のヒト型セラミドがインナードライを根本解決",
        "catch": "クレンジングバームで有名なink.が誇る本格派。セラミド原液を高濃度でダイレクトにチャージ",
        "brand_name": "ink. (インク)",
        "capacity": "100ml (モイストエッセンスローション)",
        "type": "ヒト型セラミド原液5%配合・高濃度原液スキンローション",
        "features": "ヒト型セラミド5種（EOP・NP・AP・AS・NS）、ヒアルロン酸、エラスチン、コラーゲン、グリチルリチン酸2K",
        "value": "原液メーカーならではの贅沢設計。ヒト型セラミドを推奨濃度以上の5%という高濃度で配合し、冬の過酷な乾燥でボロボロになった肌バリアを急速リペア",
        "desc_p1": "一般的な化粧水に含まれるセラミドの配合量は通常コンマ数パーセント程度ですが、ink.の『モイストエッセンスローション』は、なんとヒト型セラミド原液を『5%』という破格の高濃度で贅沢配合した本格派の保湿化粧水です。",
        "desc_p2": "皮膚のバリア膜を構成する主要な5種類のヒト型セラミドをバランスよく配合し、肌のラメラ構造をダイレクトに修復。少しとろみのある美容液のような濃厚なテクスチャーながら、肌に伸ばすとスーッと溶け込むように浸透し、内側から押し返すような密度感をもたらします。無香料・無着色・パラベンフリー・アルコールフリーの安心設計で、冬の冷風で赤みが出やすい肌にも優しく寄り添います。",
        "target": "一般的なセラミド化粧水では保湿力が物足りない方、インナードライを短期間で立て直したい方、高濃度原液の確かな効果を実感したい方",
        "point": "洗顔後、適量（100円玉大）を手に取り、優しく顔全体に伸ばしてハンドプレス。特に乾燥が深刻な頬骨周りや口元には、指先でトントンと重ね塗りを。"
    },
    {
        "rank": 9,
        "tag": "🌸 トリプルセラミド×ナノコラーゲン！ドラッグストアで愛され続ける冬の乾燥対策大本命",
        "catch": "明色化粧品のロングセラー。角層を密閉して水分を逃さない『しっとり超保水』ヴェール",
        "brand_name": "明色化粧品 (MEISHOKU)",
        "capacity": "180ml (セラコラ しっとり化粧水)",
        "type": "トリプルセラミド＆ナノコラーゲン配合・弱酸性高浸透化粧水",
        "features": "セラミド1・3・6II、加水分解コラーゲン、ヒアルロン酸、無香料・無着色・アルコールフリー",
        "value": "トリプルセラミドと浸透型ナノコラーゲンの黄金タッグ。手頃な価格ながら真冬の過酷な乾燥に負けないもっちりとした弾力肌へと導く",
        "desc_p1": "長年ドラッグストアの店頭で多くの乾燥肌ユーザーから支持され続けている『セラコラ』シリーズ。そのしっとり化粧水は、冬の寒気で皮脂と水分が同時に失われた肌に、必要不可欠な脂質と保水成分を同時にチャージできる優秀なローションです。",
        "desc_p2": "皮膚バリアの土台を作るセラミド1、水分保持を担うセラミド3、ターンオーバーを促すセラミド6IIという3種類のセラミドをバランス配合。さらに分子量の小さいナノコラーゲンが角層深部まで届き、しぼんだ肌を内側からふっくらと押し上げます。ベタつかないのに潤いの膜が長時間肌を包み込み、冬の朝のメイク前にも使いやすい絶妙な仕上がりです。",
        "target": "手頃な価格で毎日続けられるセラミド化粧水を探している方、コラーゲンのハリ感も同時に欲しい方、シンプルな低刺激処方を好む方",
        "point": "洗顔後、コットンまたは手のひらに適量を取り、顔全体になじませます。乾燥が気になる部分はコットンに化粧水を足して優しくパッティングすると効果的です。"
    },
    {
        "rank": 10,
        "tag": "🌿 3種の植物エキス×高保水成分！リニューアルでさらに潤いバリアが進化した名作",
        "catch": "無印良品の超定番がリニューアル。天然由来成分100%にこだわり冬の敏感肌を穏やかに満たす",
        "brand_name": "無印良品 (MUJI)",
        "capacity": "300ml (敏感肌用化粧水 高保湿タイプ)",
        "type": "天然由来成分100%・敏感肌用高保湿低刺激化粧水",
        "features": "ユーカリ葉エキス、スベリヒユエキス、グレープフルーツ種子エキス、セラミド類似成分、高保水ポリクオタニウム-51",
        "value": "岩手県釜石の天然水を使用した無印良品の最高峰高保湿化粧水。リニューアルにより肌バリアをサポートする植物由来成分が大幅に強化",
        "desc_p1": "日本のシンプルスキンケアを代表する無印良品の敏感肌用シリーズ。2023年秋の大型リニューアルにより、天然由来成分100%処方へと進化し、冬のデリケートな肌に対する保護能力がさらに高まりました。",
        "desc_p2": "肌保護成分としてユーカリ葉エキスやスベリヒユエキスを配合し、ヒアルロン酸の約2倍の保水力を持つリピジュア（ポリクオタニウム-51）とセラミド類似成分が角層の水分蒸発を強力にブロック。少しとろみのある柔らかなテクスチャーが肌にスッと馴染み、摩擦を感じさせずにしっとりとした潤い膜を形成します。大容量300mlで惜しみなく使え、冬の日常使いに最適な頼れる1本です。",
        "target": "天然由来・無添加の安心処方を重視する方、季節の変わり目や冬の寒さで肌がゆらぎやすい方、家族全員でシェアしたい方",
        "point": "洗顔後、手のひらに適量をとり、顔全体に優しくなじませます。別売りのスプレーヘッドやポンプヘッドを付けると毎日のスキンケアがより快適になります。"
    }
]

faq_items = [
    {
        "q": "なぜ冬（11月・12月）のスキンケアには「セラミド化粧水」が絶対に欠かせないのですか？",
        "a": "冬は外気温の低下と暖房の稼働により、大気中の湿度が20〜30%台まで急落します。この環境下では、角層内の水分を保持する細胞間脂質の主成分『セラミド』が激減し、いくら一般的な水分（精製水中心の化粧水）を与えても数分で蒸散してしまいます。セラミド化粧水は、水分を与えると同時に『水分を挟み込んで逃さないラメラ液晶構造』を角層内に即座に再建するため、真冬の過酷な乾燥環境でも一日中潤いを閉じ込めることができるのです。"
    },
    {
        "q": "「ヒト型セラミド」と「植物性セラミド」「疑似セラミド」の違いと選び方は？",
        "a": "『ヒト型セラミド（セラミドNP、AP、EOP等）』は人間の肌に存在するセラミドと同一の立体構造を持つため、浸透性とバリア修復スピードが最も優れています。本格的なインナードライや乾燥小ジワを改善したい方に最適です。『植物性セラミド（米や大豆由来）』は肌馴染みがよく、ターンオーバーを整える力に優れています。またキュレルなどに使われる『疑似セラミド（セラミド機能成分）』は、分子が安定しており高濃度配合しやすく、敏感肌でも低刺激で惜しみなく使えるというメリットがあります。"
    },
    {
        "q": "セラミド化粧水は「手で塗る」のと「コットンで塗る」のはどちらが良いですか？",
        "a": "冬の乾燥・敏感肌には圧倒的に『手のひらでのハンドプレス』がおすすめです。冬の角層は寒風や乾燥でデリケートになっており、コットンの繊維による微細な摩擦刺激でもバリア機能が低下することがあります。手のひらの体温で化粧水を軽く温めてから、肌を包み込むように優しく押し込むことで、セラミドが角層深部までスムーズに浸透します。ただし、部分的な集中保水を行いたい場合は、摩擦を起こさないよう化粧水をひたひたに含ませたコットンパックを行うのが非常に効果的です。"
    },
    {
        "q": "セラミド化粧水の後に使う乳液やクリームは、どんなものを選べば良いですか？",
        "a": "セラミド化粧水で角層にたっぷりと水分とセラミドを流し込んだ後は、その潤いを密閉するための油分（エモリエント成分）を重ねるのが鉄則です。スクワランオイルやシアバター、ワセリンなどを配合した乳液やクリームを重ねることで、水分蒸発を完全に遮断できます。さらに乳液やクリームにもセラミドが配合されたアイテムを組み合わせる『セラミド重ね使い（Wセラミドケア）』を行うと、真冬の暖房直下でもビクともしない鉄壁の保水肌が完成します。"
    },
    {
        "q": "オイリー肌やニキビができやすい混合肌でも、冬はセラミド化粧水を使うべきですか？",
        "a": "はい、むしろ強く推奨されます。冬にTゾーンがテカったり大人ニキビができたりする方の多くは、角層内部の水分が不足して肌が過剰に皮脂を分泌してしまう『インナードライ（隠れ乾燥）』が原因です。セラミド化粧水で角層深部の水分保持力を正常化させると、過剰な皮脂分泌のシグナルが収まり、テカリや毛穴詰まりが劇的に改善します。オイリー肌やニキビ肌の方は、セザンヌや無印良品のようにベタつかないテクスチャーのものを選ぶと快適です。"
    }
]

# JSON-LD構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {p['capacity']}",
        "image": item['image'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliateUrl'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10",
    "description": "11月・12月の冬本番に深刻化する冷気と暖房による角層バリア崩壊・深層インナードライ・粉吹き乾燥を徹底解決！ヒト型セラミドや疑似セラミドを贅沢配合した高保湿セラミド化粧水10選を徹底比較！セザンヌ、松山油脂、カルテHD、エトヴォス、ケアセラ、キュレル、菊正宗など、真冬でも内側からみずみずしく潤う名品を厳選。",
    "image": items[0]['image'],
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
    "name": "冬の高保湿セラミド化粧水 おすすめランキング10選",
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
            "name": item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item["a"]
            }
        } for item in faq_items
    ]
}

cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="feature-tag">{p['tag']}</span>
        </div>
        <h3 class="product-name">{p['brand_name']} {p['capacity']}</h3>
        <p class="product-catch">{p['catch']}</p>
        
        <div class="product-body">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高保湿セラミド化粧水" class="product-img" loading="lazy" width="280" height="280">
          </div>
          <div class="product-meta">
            <table class="meta-table">
              <tr>
                <th>タイプ</th>
                <td>{p['type']}</td>
              </tr>
              <tr>
                <th>主要成分</th>
                <td>{p['features']}</td>
              </tr>
              <tr>
                <th>容量 / 実勢価格</th>
                <td>{p['capacity']} / <span class="price-val">¥{item['price']:,}</span> (税込・楽天市場最新)</td>
              </tr>
              <tr>
                <th>独自バリュー</th>
                <td>{p['value']}</td>
              </tr>
            </table>
          </div>
        </div>
        
        <div class="product-desc-box">
          <h4 class="desc-heading">🔍 冬（11月・12月）の肌悩みへのアプローチ＆使用感</h4>
          <p class="desc-text">{p['desc_p1']}</p>
          <p class="desc-text">{p['desc_p2']}</p>
          
          <div class="recommend-box">
            <div class="recommend-target">
              <span class="rec-icon">🎯</span>
              <strong>こんな方におすすめ：</strong> {p['target']}
            </div>
            <div class="recommend-usage">
              <span class="rec-icon">💡</span>
              <strong>効果を高めるプロの使い方：</strong> {p['point']}
            </div>
          </div>
        </div>

        <div class="cta-wrap">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            <span class="rakuten-icon">🛍️</span> 楽天市場で「{p['brand_name']}」の最安値・口コミを見る（¥{item['price']:,}〜）
          </a>
        </div>
      </article>
""")

table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">第{p['rank']}位</span></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br>{p['capacity']}</td>
              <td class="col-feat">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化する冷気と暖房による角層バリア崩壊・深層インナードライ・粉吹き乾燥を徹底解決！ヒト型セラミドや疑似セラミドを贅沢配合した高保湿セラミド化粧水10選を徹底比較！セザンヌ、松山油脂、カルテHD、エトヴォス、ケアセラ、キュレル、菊正宗など、真冬でも内側からみずみずしく潤う名品を厳選。">
  <meta name="keywords" content="セラミド化粧水,高保湿化粧水,冬 スキンケア,ヒト型セラミド,インナードライ,粉吹き乾燥,セザンヌ,松山油脂,カルテHD,キュレル,おすすめ 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-ceramide-lotion">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10">
  <meta property="og:description" content="11月・12月の冷気と暖房で干上がった肌を救う！ヒト型セラミド高配合の最強化粧水10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-ceramide-lotion">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
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
  
  <style>
    :root {{
      --primary: #1e3a8a;
      --primary-light: #eff6ff;
      --accent: #e11d48;
      --accent-hover: #be123c;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg-gray: #f8fafc;
      --border: #e2e8f0;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: #f1f5f9;
    }}
    header {{
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
      color: white;
      padding: 1rem 0;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .header-container {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 800;
      text-decoration: none;
      color: white;
      letter-spacing: -0.025em;
    }}
    .nav-links {{
      display: flex;
      gap: 1rem;
    }}
    .nav-links a {{
      color: rgba(255,255,255,0.9);
      text-decoration: none;
      font-size: 0.875rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{
      color: white;
      text-decoration: underline;
    }}
    .main-wrap {{
      max-width: 920px;
      margin: 2rem auto;
      background: white;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
      padding: 2.5rem 2rem;
    }}
    @media (max-width: 640px) {{
      .main-wrap {{
        padding: 1.5rem 1rem;
        margin: 1rem 0.5rem;
      }}
    }}
    .article-header {{
      border-bottom: 2px solid var(--border);
      padding-bottom: 1.5rem;
      margin-bottom: 2rem;
    }}
    .article-tag {{
      display: inline-block;
      background: #e0f2fe;
      color: #0369a1;
      font-size: 0.8125rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.75rem;
    }}
    h1 {{
      font-size: 1.75rem;
      line-height: 1.4;
      color: #0f172a;
      font-weight: 800;
      margin-bottom: 1rem;
    }}
    @media (max-width: 640px) {{
      h1 {{
        font-size: 1.4rem;
      }}
    }}
    .update-time {{
      font-size: 0.8125rem;
      color: var(--text-muted);
      display: flex;
      gap: 1rem;
    }}
    .lead-box {{
      background: #eff6ff;
      border-left: 5px solid #2563eb;
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 0.975rem;
      color: #1e293b;
    }}
    .toc-box {{
      background: var(--bg-gray);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.5rem;
      margin-bottom: 2.5rem;
    }}
    .toc-title {{
      font-weight: 800;
      font-size: 1.05rem;
      margin-bottom: 0.75rem;
      color: var(--primary);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-list li {{
      margin-bottom: 0.5rem;
    }}
    .toc-list a {{
      color: #2563eb;
      text-decoration: none;
      font-size: 0.925rem;
    }}
    .toc-list a:hover {{
      text-decoration: underline;
    }}
    h2.section-title {{
      font-size: 1.35rem;
      color: #0f172a;
      border-left: 5px solid var(--primary);
      padding-left: 0.75rem;
      margin: 3rem 0 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-content {{
      margin-bottom: 2rem;
      font-size: 0.975rem;
      color: #334155;
    }}
    .section-content p {{
      margin-bottom: 1rem;
    }}
    .highlight-card {{
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-radius: 8px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .highlight-card h4 {{
      color: #be123c;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}
    .product-card {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--card-shadow);
      position: relative;
    }}
    .product-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      display: inline-block;
      font-size: 0.875rem;
      font-weight: 800;
      color: white;
      padding: 0.25rem 0.85rem;
      border-radius: 6px;
      background: #64748b;
    }}
    .rank-1 {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
    .rank-2 {{ background: linear-gradient(135deg, #94a3b8, #64748b); }}
    .rank-3 {{ background: linear-gradient(135deg, #d97706, #b45309); }}
    .feature-tag {{
      font-size: 0.8125rem;
      font-weight: 700;
      color: #0369a1;
      background: #f0f9ff;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      border: 1px solid #bae6fd;
    }}
    .product-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.4;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 1.25rem;
    }}
    .product-body {{
      display: flex;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 640px) {{
      .product-body {{
        flex-direction: column;
        align-items: center;
      }}
    }}
    .product-img-box {{
      flex-shrink: 0;
      width: 240px;
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border);
      object-fit: contain;
    }}
    .product-meta {{
      flex-grow: 1;
    }}
    .meta-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
    }}
    .meta-table th, .meta-table td {{
      padding: 0.6rem 0.75rem;
      border-bottom: 1px solid var(--border);
    }}
    .meta-table th {{
      width: 30%;
      background: var(--bg-gray);
      color: #475569;
      font-weight: 700;
      text-align: left;
    }}
    .meta-table td {{
      color: #1e293b;
    }}
    .price-val {{
      font-weight: 800;
      color: #e11d48;
      font-size: 1.05rem;
    }}
    .product-desc-box {{
      background: #f8fafc;
      border-radius: 8px;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
    }}
    .desc-heading {{
      font-size: 1rem;
      font-weight: 700;
      color: #1e3a8a;
      margin-bottom: 0.75rem;
    }}
    .desc-text {{
      font-size: 0.925rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 0.75rem;
    }}
    .recommend-box {{
      margin-top: 1rem;
      padding-top: 1rem;
      border-top: 1px dashed var(--border);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      font-size: 0.875rem;
    }}
    .recommend-target, .recommend-usage {{
      display: flex;
      gap: 0.5rem;
      color: #334155;
    }}
    .rec-icon {{
      flex-shrink: 0;
    }}
    .cta-wrap {{
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: white;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.975rem;
      padding: 0.85rem 1.75rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px -1px rgba(230, 0, 0, 0.25);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      width: 100%;
      max-width: 520px;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 12px -2px rgba(230, 0, 0, 0.35);
      color: white;
    }}
    .table-container {{
      overflow-x: auto;
      margin: 2rem 0;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.875rem;
      min-width: 600px;
    }}
    .summary-table th, .summary-table td {{
      padding: 0.75rem;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #1e3a8a;
      color: white;
      font-weight: 700;
    }}
    .summary-table tr:nth-child(even) {{
      background: #f8fafc;
    }}
    .table-rank {{
      display: inline-block;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      color: white;
      font-weight: 700;
      font-size: 0.75rem;
      background: #64748b;
    }}
    .col-price {{
      font-weight: 700;
      color: #e11d48;
    }}
    .table-btn {{
      display: inline-block;
      background: #bf0000;
      color: white;
      text-decoration: none;
      padding: 0.3rem 0.6rem;
      border-radius: 4px;
      font-weight: 700;
      font-size: 0.75rem;
    }}
    .faq-item {{
      background: var(--bg-gray);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.25rem;
      margin-bottom: 1rem;
    }}
    .faq-q {{
      font-weight: 700;
      color: #1e3a8a;
      font-size: 1rem;
      margin-bottom: 0.5rem;
      display: flex;
      gap: 0.5rem;
    }}
    .faq-a {{
      font-size: 0.925rem;
      color: #334155;
      line-height: 1.7;
    }}
    .internal-links-box {{
      background: #f1f5f9;
      border-radius: 8px;
      padding: 1.5rem;
      margin: 3rem 0;
    }}
    .internal-links-title {{
      font-weight: 800;
      font-size: 1.1rem;
      color: #0f172a;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 0.75rem;
    }}
    .internal-link-card {{
      background: white;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.75rem;
      text-decoration: none;
      color: #1e293b;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
      display: block;
    }}
    .internal-link-card:hover {{
      border-color: #2563eb;
      color: #2563eb;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1rem 2rem;
      font-size: 0.875rem;
      margin-top: 4rem;
    }}
    .footer-container {{
      max-width: 1080px;
      margin: 0 auto;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-bottom: 2rem;
    }}
    .footer-links a {{
      color: #cbd5e1;
      text-decoration: none;
    }}
    .footer-links a:hover {{
      color: white;
    }}
    .copyright {{
      text-align: center;
      border-top: 1px solid #334155;
      padding-top: 1.5rem;
      font-size: 0.8125rem;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-container">
    <a href="/" class="site-title">✨ 冬コスメ徹底比較ラボ</a>
    <nav class="nav-links">
      <a href="/">ホーム</a>
      <a href="/#skincare">スキンケア</a>
      <a href="/#haircare">ヘアケア</a>
      <a href="/#bodycare">ボディケア</a>
    </nav>
  </div>
</header>

<main class="main-wrap">
  <article>
    <header class="article-header">
      <span class="article-tag">❄️ 11月・12月 冬本番スキンケア特集</span>
      <h1>保湿力の強さで肌乾燥とさようなら！角層深く浸透してバリアを守る高保湿セラミド化粧水ランク10</h1>
      <div class="update-time">
        <span>📅 公開日: 2026年11月2日</span>
        <span>🔄 最終更新日: 2026年11月2日</span>
        <span>✍️ 監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>
    </header>

    <div class="lead-box">
      <p>11月から12月へと向かうにつれ、外気の湿度は30%以下まで急降下し、オフィスや自宅のエアコン暖房が肌の水分を無慈悲に奪い去っていきます。「朝どんなに丁寧に保湿しても、昼過ぎには頬が突っ張って痛い」「ファンデーションを塗ると粉を吹いてひび割れる」「いつもの化粧水をつけると肌がピリピリとしみる……」そんな深刻な真冬の乾燥トラブルに直面していませんか？</p>
      <p style="margin-top: 0.75rem;">その根本原因は、角質層の水分を挟み込んで保つ細胞間脂質の要である「セラミド」が寒冷乾燥によって失われ、肌のバリア機能が崩壊していることにあります。精製水中心の一般的な化粧水で水分だけを与えても、砂漠に水を撒くように数分で蒸発してしまい、かえって乾燥を悪化させることすらあります。本記事では、角層のラメラ液晶構造を物理的に再建する「ヒト型セラミド」や「高濃度セラミド機能成分」を高配合した至高の高保湿セラミド化粧水10選を徹底比較！楽天市場の最新価格・レビューデータを踏まえて厳選解説します。</p>
    </div>

    <!-- 目次 -->
    <nav class="toc-box">
      <div class="toc-title">📑 目次（タップで各見出しへジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#science">1. 11月・12月に「セラミド化粧水」が絶対に必要な科学的理由</a></li>
        <li><a href="#how-to-choose">2. 失敗しない！冬の高保湿セラミド化粧水の選び方3大鉄則</a></li>
        <li><a href="#ranking">3. 冬の高保湿セラミド化粧水 おすすめ人気ランキング10選</a></li>
        <li><a href="#comparison-table">4. 高保湿セラミド化粧水10選のスペック・実勢価格 徹底比較表</a></li>
        <li><a href="#pro-technique">5. 美容皮膚科医発想！真冬の保水力を3倍に高める「ミルフィーユ保水術」</a></li>
        <li><a href="#faq">6. セラミド化粧水に関するよくある質問（FAQ）</a></li>
        <li><a href="#summary">7. まとめ：自分の肌質に合ったセラミド化粧水で真冬のモチ肌を手に入れよう</a></li>
      </ul>
    </nav>

    <!-- 科学的解説 -->
    <section id="science">
      <h2 class="section-title">🔬 11月・12月に「セラミド化粧水」が絶対に必要な科学的理由</h2>
      <div class="section-content">
        <p>人間の皮膚の最外層にある「角質層」は、わずか0.02mm（食品用ラップフィルム1枚分）ほどの厚さしかありません。この極薄のシールドの中で、レンガのように積み重なった角質細胞の間を埋め尽くし、水分をがっちりと挟み込んで逃さないようにしているのが「細胞間脂質」であり、その主成分の約50%を占めるのが『セラミド』です。</p>
        <p>11月から12月にかけて気温が15℃を下回り、暖房がフル稼働し始めると、大気の水分保持量が激減します。湿度が30%を下回る超乾燥環境では、肌内部から空気中へ水分が奪われる「経表皮水分蒸散量（TEWL）」が急激に上昇。さらに寒さによる血行不良で肌自身のセラミド産生能力も低下するため、角層のラメラ構造（水と油が交互に重なり合うミルフィーユ状の組織）がスカスカに崩壊してしまいます。</p>
        
        <div class="highlight-card">
          <h4>💡 水分補給だけでは防げない「インナードライ」の恐怖</h4>
          <p>セラミドが不足した角層にいくら一般的な水分（化粧水）をパッティングしても、抱え込む脂質が存在しないため、わずか数分で蒸発してしまいます。それどころか、蒸発する際に肌本来が持っていたわずかな水分まで一緒に奪い去る「過乾燥」を招き、内側はカラカラなのに表面だけ皮脂でテカる『インナードライ』を悪化させます。だからこそ、水分のファーストステップである化粧水の段階で、セラミドそのものを角層へ浸透させることが、真冬のスキンケアにおける唯一無二の解決策なのです。</p>
        </div>
      </div>
    </section>

    <!-- 選び方 -->
    <section id="how-to-choose">
      <h2 class="section-title">🎯 失敗しない！冬の高保湿セラミド化粧水の選び方3大鉄則</h2>
      <div class="section-content">
        <p>ドラッグストアやECサイトには「セラミド配合」を謳う化粧水が無数に並んでいますが、成分表記や配合バランスによって保水力と浸透力には決定的な差があります。11月・12月の本格的な乾燥を乗り越えるために、以下の3つのポイントを必ずチェックしてください。</p>
        
        <h3 style="font-size: 1.1rem; color: #1e3a8a; margin: 1.25rem 0 0.5rem;">① 「ヒト型セラミド」または「複合型セラミド」が明記されているか</h3>
        <p>最も保水力が高く肌馴染みが良いのは、人間の皮膚に存在するセラミドと同一構造を持つ『ヒト型セラミド（成分名にセラミドNP、セラミドAP、セラミドEOP、セラミドNGなどアルファベットが付くもの）』です。単一のセラミドだけでなく、複数のヒト型セラミドがバランスよくブレンドされた「複合型」を選ぶことで、角層の隙間を立体的に埋めることができます。また、花王キュレルなどが採用する「セラミド機能成分」は、高濃度でも安定した浸透力を発揮し、敏感肌でもトラブルなく使える優れた選択肢です。</p>

        <h3 style="font-size: 1.1rem; color: #1e3a8a; margin: 1.25rem 0 0.5rem;">② テクスチャーと「浸透設計」が肌質に合っているか</h3>
        <p>冬の乾燥肌には、美容液のように少しとろみのある「モイストリッチタイプ」が角層を柔軟にほぐすため適しています。一方、インナードライやオイリー肌、男性の肌には、ナノ化技術や微細乳化技術でシャバシャバした質感ながら角層深部まで一瞬で届く「高浸透ナノエマルジョン型」が最適です。表面のベタつきが苦手な方でも、内部密度を高める化粧水を選ぶことで日中のメイク崩れを防げます。</p>

        <h3 style="font-size: 1.1rem; color: #1e3a8a; margin: 1.25rem 0 0.5rem;">③ 冬の敏感肌を刺激しない「低刺激・フリー処方」であること</h3>
        <p>冬の寒風にさらされた肌は、バリア機能が著しく低下しており、普段は問題ない成分でも赤みやヒリつきを感じやすくなっています。エタノール（アルコール）、合成香料、合成着色料、パラベンなどが無添加の弱酸性処方を選びましょう。特に消炎成分（アラントインやグリチルリチン酸2K）が配合されている薬用ローションであれば、微細な肌荒れを穏やかに整えながら水分を補給できます。</p>
      </div>
    </section>

    <!-- ランキングセクション -->
    <section id="ranking">
      <h2 class="section-title">🏆 冬の高保湿セラミド化粧水 おすすめ人気ランキング10選</h2>
      <p style="margin-bottom: 2rem; font-size: 0.95rem; color: #475569;">
        楽天市場の最新実売データ、口コミ評価、成分の専門的分析に基づき、11月・12月の過酷な冬に本当におすすめできる高保湿セラミド化粧水10選をランキング形式で詳しくレビューします。
      </p>

      {"".join(cards_html)}
    </section>

    <!-- 比較表 -->
    <section id="comparison-table">
      <h2 class="section-title">📊 高保湿セラミド化粧水10選のスペック・実勢価格 徹底比較表</h2>
      <div class="section-content">
        <p>今回厳選した10商品の容量、主要配合成分、実勢価格、特徴を一覧表にまとめました。ご自身の予算や肌悩みに合わせて最適なアイテムを比較検討してください。</p>
        <div class="table-container">
          <table class="summary-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / 容量</th>
                <th>注目保湿成分</th>
                <th>楽天市場実勢価格</th>
                <th>商品リンク</th>
              </tr>
            </thead>
            <tbody>
              {"".join(table_rows)}
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- プロの使い方 -->
    <section id="pro-technique">
      <h2 class="section-title">✨ 美容皮膚科医発想！真冬の保水力を3倍に高める「ミルフィーユ保水術」</h2>
      <div class="section-content">
        <p>どんなに優秀なセラミド化粧水を手に入れても、塗布の仕方が雑では効果が半減してしまいます。冬の冷え固まった肌を内側からみずみずしく膨らませる、プロ直伝の3ステップ保水テクニックをご紹介します。</p>
        
        <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h4 style="color: #1e3a8a; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ1：手のひらで温めて「呼び水」をつくる</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">冷たい化粧水をそのまま肌に乗せると、毛穴が収縮して浸透が妨げられます。適量を手のひらに取り、両手を合わせて人肌に温めてから、顔全体を優しく包み込むようにハンドプレスします。まずは角層表面のゴワつきを柔らかくほぐすファーストステップです。</p>

          <h4 style="color: #1e3a8a; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ2：2〜3回の「重ね付け（ミルフィーユ保水）」</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">1回で大量の化粧水をつけるよりも、少量を2〜3回に分けて重ね塗りする方が、角層の奥深くまで均一に浸透します。1回目がスッと肌になじんだら、2回目を重ね、手のひらが肌に吸い付く感覚（もっちり感）が出るまで丁寧に押し込みます。</p>

          <h4 style="color: #1e3a8a; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ3：間髪入れずに「油分シールド」でフタをする</h4>
          <p style="font-size: 0.925rem;">化粧水をつけてから時間が経つと水分が蒸発を始めます。肌表面が濡れているうち、遅くとも1分以内に乳液やスクワランオイル、高保湿クリームを塗り広げ、セラミドで満たされた水分を外気から完全に遮断してください。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq">
      <h2 class="section-title">❓ セラミド化粧水に関するよくある質問（FAQ）</h2>
      <div class="section-content">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q"><span>Q.</span><strong>{item['q']}</strong></div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- まとめ -->
    <section id="summary">
      <h2 class="section-title">🌿 まとめ：自分の肌質に合ったセラミド化粧水で真冬のモチ肌を手に入れよう</h2>
      <div class="section-content">
        <p>11月から12月にかけての本格的な冬は、1年の中で最も肌のバリア機能が試される過酷な季節です。冷たい寒風と室内のエアコン暖房によって、角質細胞間のセラミドは刻一刻と失われ、放置すれば粉吹き、赤み、乾燥小ジワといった深刻な肌トラブルへと進行します。</p>
        <p>全身に惜しみなく浴びるように水分補給したいなら大容量の『セザンヌ』や『菊正宗』、乾燥でゴワついた角層を濃厚にほぐしたいなら『松山油脂』、皮脂膜ごと根本修復したい深刻な砂漠肌なら薬用の『カルテHD』や先行型の『ケアセラAP』、日中のメイクの上から手軽に水分チャージしたいなら『キュレル ディープモイスチャースプレー』が最適です。</p>
        <p>化粧水はスキンケアの最初の基盤。角層にセラミドをたっぷり蓄えることで、その後に重ねる美容液やクリームの密閉力も飛躍的に高まります。今日から高保湿セラミド化粧水をスキンケアの主役に据えて、暖房直下でも一日中吸い付くようなモチモチの健やか素肌をキープしてください。</p>
      </div>
    </section>

    <!-- 内部リンク -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンク更新スクリプトにより自動展開 -->
      </div>
    </div>
  </article>
</main>

<footer>
  <div class="footer-container">
    <div class="footer-links">
      <a href="/">冬コスメTOP</a>
      <a href="/winter-ceramide-cream">高保湿セラミドクリーム</a>
      <a href="/winter-peptide-serum">高保湿ペプチド美容液</a>
      <a href="/winter-hair-serum">高保湿ヘアセラム</a>
      <a href="/winter-exosome-serum">高保湿エクソソーム美容液</a>
      <a href="/winter-medicinal-bath">薬用入浴剤</a>
    </div>
    <div class="copyright">
      &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.
    </div>
  </div>
</footer>

</body>
</html>
"""

output_path = "winter-ceramide-lotion.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✓ Successfully generated {output_path} ({len(full_html):,} bytes)")
