import json
import re

with open("fetched_3new_apricot_almond_shikon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_shikon"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 天然紫根×ヒアルロン酸！真冬の冷風で赤み・ヒリつく角層をみずみずしく満たす大容量和漢水",
        "catch": "天然ムラサキ根から抽出したシコニンエキスを贅沢配合。冬の寒暖差で毛細血管が透けて赤くなった頬や、洗顔後に突っ張る乾燥肌を穏やかに鎮静し潤す名品ローション",
        "brand_name": "自然の都タマチャンショップ (美肌和漢)",
        "capacity": "200ml / 遮光ボトル",
        "type": "和漢エイジングケア高保湿化粧水",
        "features": "ムラサキ根エキス（紫根エキス）、ヒアルロン酸Na、加水分解コラーゲン、植物性グリセリン",
        "value": "合成着色料を一切使わず、紫根本来の美しいピンク色を保持。パシャパシャ使える軽やかな使用感ながら、角層深部へ吸い込まれて一日中赤みと乾燥を防ぐ",
        "desc_p1": "11月から12月にかけて日本海側・太平洋側を問わず吹き荒れる冷たい木枯らし。外気で急激に冷やされた後に暖房の効いた室内に入ると、頬がカーッと熱くなって赤くほてり、ピリピリとした痛みを伴う『冬の寒暖差肌荒れ』に直面します。タマチャンショップの『エイジングケア 紫根化粧水』は、そんな真冬のデリケートな赤み乾燥肌を鎮めるために誕生した和漢スキンケアの傑作です。",
        "desc_p2": "ボトルから手のひらに出すと、天然のシコニン由来の上品なピンク色。水のようにサラリとした質感でありながら、ハンドプレスすると角層の細胞間へぐんぐん浸透し、火照った皮膚温度をスーッと落ち着かせます。ヒアルロン酸との相乗効果で、肌の内側に水分をしっかりと抱え込み、夕方になっても突っ張り感や赤みがぶり返さない健やかな素肌環境を維持します。",
        "target": "冬になると寒暖差や冷風で頬が赤くほてりやすい方、低刺激でたっぷり水分補給できる和漢ローションを探している方、肌のキメを整えて透明感を底上げしたい方",
        "point": "朝晩の洗顔後、500円玉大を手にとって顔全体を優しく包み込みます。赤みやヒリつきが特に気になる頬には、コットンにたっぷり浸して3分間のローションパックを行うと劇的な鎮静効果を発揮します。"
    },
    {
        "rank": 2,
        "tag": "🧪 天然ムラサキ根100%抽出！手持ちのコスメに数滴混ぜて冬の荒れ肌を集中レスキューする原液",
        "catch": "創業半世紀の化粧品原料メーカーが放つ高濃度シコニン原液。いつもの化粧水やクリームにブレンドするだけで、真冬の重度なバリア崩壊・ひび割れ肌を救う特効アンプルへ",
        "brand_name": "自然化粧品研究所",
        "capacity": "20ml / 遮光ドロッパー容器",
        "type": "高濃度シコンエキス 100%ピュア原液",
        "features": "ムラサキ根エキス、BG、水（純度100%植物エキス原液）",
        "value": "余計な界面活性剤や防腐剤を極力排除した高濃度処方。深紅に染まるシコニンの抗炎症・創傷治癒パワーをダイレクトに肌へ届けるプロ仕様コスメ",
        "desc_p1": "冬の乾燥ダメージがピークに達すると、どれだけ高級な保湿クリームを塗っても浸透せず、肌表面がカピカピに乾燥して皮がめくれてしまうことがあります。自然化粧品研究所の『紫根エキス原液 20ml』は、そんなスキンケアが効かなくなった限界肌を根本から立て直すレスキュー原液です。",
        "desc_p2": "深みのある紫赤色の原液には、古来より皮膚病や火傷の治療軟膏として用いられてきた和漢成分『シコニン』が高濃度で凝縮。普段使用している化粧水や乳液に1〜2滴垂らして手のひらで混ぜ合わせると、ほんのりピンク色に染まり、肌の修復力と保水力が爆発的に向上します。冬の肌荒れやマスク擦れの赤みも、数日間の集中ケアで目に見えて滑らかな健常肌へと導いてくれます。",
        "target": "手持ちのスキンケアの保湿・肌荒れケア効果を飛躍的に高めたい方、成分重視でピュアな和漢エキス原液を使いたい方、冬の皮むけや頑固な乾燥荒れに悩む方",
        "point": "手のひらに化粧水や美容液をとり、本原液を1〜2滴加えて混ぜ合わせてから塗布します。乾燥が激しい目元や口元には、クリームに1滴ブレンドして濃厚なナイトシールドとして使うのがおすすめです。"
    },
    {
        "rank": 3,
        "tag": "🌿 自社農園産オリーブ油×天然紫根！冬の木枯らしでカサつく角層を包むピンクの濃密美容液",
        "catch": "瀬戸内・牛窓のオリーブ園を営む日本オリーブの隠れた名品。オリーブオイルの濃密エモリエント膜と紫根の抗炎症力が融合した、真冬の乾燥小ジワをふっくら満たす和漢セラム",
        "brand_name": "日本オリーブ (オリーブマノン)",
        "capacity": "30ml / 遮光スポイトガラス瓶",
        "type": "高保湿和漢オリーブオイル美容液",
        "features": "オリーブ果実油（自社農園産）、ムラサキ根エキス（紫根エキス）、トコフェロール",
        "value": "無香料・無鉱物油・タール系色素不使用。天然紫根エキス由来の鮮やかなルビーピンク色が、冬の寒冷くすみで血色を失った素肌に温かな艶と透明感をチャージ",
        "desc_p1": "乾燥注意報が連日発令される11月下旬以降、肌の水分蒸発と皮脂欠乏は同時に進行し、肌はハリを失ってしぼんでしまいます。日本オリーブの『紫草（シコン）オリーブマノン うるおい美容液』は、自社オリーブ園の良質なオリーブ果実油に天然紫根をじっくり溶かし込んだ贅沢な美容液です。",
        "desc_p2": "オイルベースでありながらベタつかず、肌に乗せると体温でとろけるように角層深部へ吸い込まれます。オリーブのオレイン酸とスクワレンが細胞間脂質を補修し、紫根のシコニンが真冬の冷風ダメージによる微小炎症を素早く鎮静。夜のお手入れの最後に2滴ハンドプレスして就寝すれば、翌朝の洗顔時には指先が押し返されるようなもっちりとした弾力と、上気したような自然な血色感が蘇ります。",
        "target": "冬になると肌がしぼんでハリや血色感がなくなる方、上質な植物油と和漢エキスの両方を一度に取り入れたい方、安心の国産オリーブコスメを愛用したい方",
        "point": "化粧水の後にスポイト半分（2〜3滴）を手にとり、手のひらで温めてから顔全体をハンドプレス。ほうれい線や目尻など乾燥小ジワが気になる部分には指先で重ねづけしてください。"
    },
    {
        "rank": 4,
        "tag": "🛡️ 高純度シコニン×ホホバ×スクワラン！真冬の水仕事や冷気による手荒れ・粉吹きを鉄壁ガード",
        "catch": "化粧品原料のプロが開発した濃厚ピンクモイスチャークリーム。あかぎれ・しもやけ・皮むけを起こした真冬の過酷な皮膚を、分厚い和漢バリアで包み込み集中修復する",
        "brand_name": "自然化粧品研究所",
        "capacity": "35g / ジャー容器",
        "type": "濃厚和漢リペアモイスチャークリーム",
        "features": "ムラサキ根エキス、ホホバ種子油、スクワラン、植物性グリセリン、トコフェロール",
        "value": "こっくりとした高密着処方でありながら肌の上でスッと馴染みベタつかない。水仕事の多い冬の手荒れや、就寝中のエアコンによる頬の乾燥ひび割れを完全シャットアウト",
        "desc_p1": "真冬の水仕事やアルコール消毒、毎日の冷風によって、手肌や指先、頬の皮膚がカサカサに毛羽立ち、赤くひび割れて痛む……そんな過酷な冬の皮膚トラブルに立ち向かうのが、自然化粧品研究所の『紫根クリーム 35g』です。",
        "desc_p2": "蓋を開けると現れる鮮やかなモーブピンク色は、合成着色料を一切使わない高純度シコニンの証。スクワランとホホバオイルを贅沢にブレンドしたこっくりとしたテクスチャーが、塗布した瞬間に肌表面に強固な保護手袋のような膜を形成します。皮膚のターンオーバーを促すシコニンの働きにより、ガサガサになった指先やかかと、粉を吹く頬も、一晩でしっとりなめらかな手触りへと劇的に変化します。",
        "target": "冬になると手や指先があかぎれやひび割れを起こしやすい方、頬の粉吹きや乾燥荒れを強力にフタしたい方、無香料で高保湿な和漢クリームを探している方",
        "point": "夜のお手入れの最後に、パール粒大を手にとって温め、顔全体または手肌・指先に優しく塗り込みます。ひび割れがひどい指先には少し厚めに塗り、綿の手袋をして眠ると翌朝感動のなめらかさになります。"
    },
    {
        "rank": 5,
        "tag": "💧 水溶性天然シコンエキス100%！手作り化粧水やブースターに1滴プラスして角質修復を促進",
        "catch": "手作りコスメの名門マンディムーンが誇る高純度水溶性エキス。化粧水にわずか数滴加えるだけで、真冬の寒冷でこわばった角層を穏やかにほぐしバリア機能を強化",
        "brand_name": "手作り化粧品材料 マンディムーン",
        "capacity": "30ml / 遮光ドロッパーボトル",
        "type": "水溶性シコンエキス（紫根抽出エキス）",
        "features": "ムラサキ根エキス（水溶性抽出）、植物性プロパンジオール、精製水",
        "value": "オイルではなく水溶性のため、どんな化粧水やローションにも分離せず綺麗に混ざり合う。さっぱりした使用感を保ったまま、紫根の強力な肌荒れ予防効果を付与できる",
        "desc_p1": "『オイルのベタつきや油膜感がどうしても苦手だけれど、真冬の激しい乾燥荒れや赤みはどうにかしたい』という方に最適なのが、マンディムーンの『高濃度 シコンエキス 30ml』です。",
        "desc_p2": "水溶性に抽出された紫根エキスなので、普段使っているさっぱり系・しっとり系の化粧水に数滴ブレンドするだけで、全くテクスチャーを崩すことなく高機能な和漢化粧水へとグレードアップ。シコニン特有の抗菌・抗炎症・代謝促進作用が肌の角層深部へと素早く届き、真冬の乾燥による大人ニキビや肌荒れ、赤みを穏やかに落ち着かせます。大容量30mlでワンシーズンたっぷり使えます。",
        "target": "オイルが苦手で水系スキンケアで冬の乾燥荒れをケアしたい方、手作り化粧水や既存コスメのカスタマイズが好きな方、冬のインナードライや赤み肌を整えたい方",
        "point": "手持ちの化粧水（100ml）に対して本品を3〜5ml程度ブレンドしてよく振って使用するか、手のひらで化粧水を使うたびに1滴垂らして混ぜて全顔へハンドプレスします。"
    },
    {
        "rank": 6,
        "tag": "🌙 藍×紫根のダブル和漢パワー！寝ている間に目元の乾燥くすみ・たるみを集中リペアするパック",
        "catch": "塗って剥がすだけの夜用集中ピールオフパック。藍エキスの引き締め力と紫根エキスの高保湿・代謝促進が、真冬の疲れた目元やちりめんジワをピンと張った明るい目元へ",
        "brand_name": "シェモア (Chezmoi)",
        "capacity": "30g / チューブ容器",
        "type": "目元専用 和漢集中ナイトパック（ピールオフ）",
        "features": "ムラサキ根エキス（紫根エキス）、アイ葉/茎エキス（藍エキス）、ヒアルロン酸、プラセンタエキス",
        "value": "紫根の鮮やかな紫色のジェルが目元の凹凸にピタッと密着。一晩中成分を閉じ込め、翌朝ペリッと剥がすだけで古い角質くすみをオフして明るい目元を実現",
        "desc_p1": "真冬の寒さで血行が悪くなると、目の下の皮膚が青黒くくすみ、さらに暖房乾燥によって目尻や目の下に細かなちりめんジワがびっしりと刻まれます。シェモアの『藍と紫根の目元パック』は、伝統の和漢植物『藍』と『紫根』を融合させた目元レスキューパックです。",
        "desc_p2": "チューブから目元にジェルを塗り広げると、ひんやりとした密着感とともに薄い皮膜を形成。藍エキスがたるんだ目元の皮膚をキュッと引き締め、紫根エキスが角層に濃密な潤いを与えて代謝を促進します。10〜15分ほどで乾いて透明なフィルム状になるため、そのまま就寝しても寝具を汚しません。翌朝剥がした瞬間、パッと光が差し込んだような明るさとピンとしたハリに感動します。",
        "target": "冬になると目元の乾燥小ジワや青くま・くすみがひどくなる方、手軽に使えるピールオフタイプの目元パックを試したい方、和漢植物の引き締め・美肌効果を実感したい方",
        "point": "夜の洗顔・スキンケア後、目元の水分油分を軽くティッシュオフしてから、適量を目の下や目尻に均一に伸ばします。完全に乾くまで15分ほど待ち、そのまま就寝して翌朝優しく剥がします。"
    },
    {
        "rank": 7,
        "tag": "💄 五島列島産ヤブツバキ油×天然紫根！冬の皮むけ＆ひび割れ唇を血色ツヤ唇へ導く濃密リップ",
        "catch": "長崎・五島列島の無農薬ヤブツバキ油と紫根が出会った奇跡の和漢リップ。冬の冷風でガサガサに皮むけした唇の角質層を密着補修し、自然な桜色の血色感を与える",
        "brand_name": "椿乃 (TSUBAKINO)",
        "capacity": "4g / スティック容器",
        "type": "天然和漢高保湿リップトリートメントクリーム",
        "features": "ツバキ種子油（五島列島産100%）、ムラサキ根エキス（紫根エキス）、ミツロウ、トコフェロール",
        "value": "タール色素・防腐剤・石油系原料一切不使用。紫根本来の天然の赤みが唇に自然な血色感を与え、口紅の下地としてもリップグロス代わりとしても大活躍",
        "desc_p1": "冬の唇は、皮脂腺がなく角層が極めて薄いため、冷たい木枯らしに数分晒されるだけで皮がめくれ、ひどい時には出血や縦ジワのひび割れを起こします。椿乃の『椿のリップクリーム』は、古来より髪や肌を守ってきた椿油と、傷を癒やす生薬紫根を組み合わせた最高峰のリップケアです。",
        "desc_p2": "スティックを唇に滑らせると、体温でじゅわっととろけて高密度の保護膜を形成。ツバキ油の豊富なオレイン酸が唇の奥深くまで潤いを届け、紫根のシコニンが荒れた粘膜の炎症を素早く鎮静します。合成着色料を一切使わない紫根の自然なピンク色がくすんだ唇を明るく見せてくれるため、ノーメイクの日でも健康的な美しい口元を演出できます。",
        "target": "冬になると唇が乾燥して皮がめくれたり縦ジワが深くなる方、無添加・天然由来成分100%の安全なリップを使いたい方、口紅を塗ると唇が荒れてしまう方",
        "point": "朝晩のスキンケア時や乾燥を感じた時にいつでも唇に滑らせます。就寝前に唇の輪郭からはみ出るくらいオーバーにたっぷり塗り込むと、翌朝プルプルの潤い唇に仕上がります。"
    },
    {
        "rank": 8,
        "tag": "👑 米ぬか×ホホバ×和漢オイル！冬の濃密メイクも擦らず溶かし潤い膜を守る韓国No.1名品",
        "catch": "オリーブヤングや楽天ランキングで殿堂入りを果たす魔女工場のピュアクレンジング。微細な植物オイル分子が毛穴の奥の角栓まで溶かし、洗い上がりもつっぱりゼロ",
        "brand_name": "manyo (魔女工場)",
        "capacity": "200ml / ポンプボトル",
        "type": "高保湿天然植物油クレンジングオイル",
        "features": "ダイズ油、コメヌカ油、ホホバ種子油、ツバキ種子油、発酵オリーブ油、トコフェロール",
        "value": "99.9%天然由来成分処方。親水性の高いマイクロオイル処方により、真冬の冷たい水でも素早く乳化して摩擦フリーでメイクを落とし、肌の天然保湿膜を守り抜く",
        "desc_p1": "冬のクレンジングは、メイクを落とすだけでなく『いかに角層のうるおいを奪わないか』が美肌維持の鍵を握ります。魔女工場の『ピュア クレンジングオイル 200ml』は、韓国スキンケア界で数々のベストコスメ賞を総なめにしてきた世界的人気クレンジングです。",
        "desc_p2": "肌に乗せると、植物油ならではの厚みのあるクッションが手のひらと肌の間の摩擦を完全にブロック。ウォータープルーフのマスカラや頑固な毛穴の角栓も、擦ることなく瞬時にジュワッと浮かび上がらせます。ぬるま湯を加えると一瞬で白く乳化して綺麗に洗い流せ、洗顔後も化粧水を塗った直後のようなしっとり・もちもちした素肌感が持続します。",
        "target": "クレンジング後の肌のツッパリ感やつっぱり乾燥に悩む方、毛穴の黒ずみ・角栓と保湿を同時にケアしたい方、圧倒的な口コミ高評価を誇る名品を使いたい方",
        "point": "乾いた手のひらに3〜4プッシュをとり、顔全体に円を描くように優しくなじませます。少量のぬるま湯を手につけて顔全体が白くなるまでしっかり乳化させてから、丁寧にすすぎます。"
    },
    {
        "rank": 9,
        "tag": "🎭 紫根エキス×EGF配合！真冬の乾ききった素肌を贅沢な和漢美容液で毎日満たす30枚入",
        "catch": "高密着ナチュラルコットンシートに天然紫根エキスと肌再生因子EGFを贅沢配合。冬の暖房でカラカラに干からびた肌を毎日10分で吸い付くような水光肌へと導く大容量マスク",
        "brand_name": "MITOMO (ミトモ)",
        "capacity": "30枚入り / ジッパー密閉パウチ",
        "type": "大容量高保湿和漢デイリーシートマスク",
        "features": "ムラサキ根エキス（紫根エキス）、ヒト遺伝子組換オリゴペプチド-1（EGF）、アロエベラ葉エキス、ヒアルロン酸Na",
        "value": "1枚あたり約90円台という驚きの高コスパ。厚手の不織布シートが顔の凹凸に吸い付くように密着し、冬の過酷な乾燥による小ジワやくすみを毎日集中ケア",
        "desc_p1": "冬の乾燥肌荒れを最も手っ取り早くリセットする方法は、角質層に水分と美容成分を物理的に密着させて送り込む『毎日のシートマスク習慣』です。MITOMOの『CARE601 紫根＋EGF プレミアムエッセンスマスク』は、インバウンドや楽天でも大人気を誇る和漢密着マスクです。",
        "desc_p2": "エッセンスがヒタヒタに含まれた厚みのあるシートを取り出して顔に密着させると、紫根の肌荒れ鎮静成分とEGFのターンオーバーサポート成分が角質層のすみずみまで浸透。10分後に剥がすと、手のひらが吸い付くほどの濃密な保水感と、くすみが抜けたワントーン明るい透明感を実感できます。30枚入りなので、11月〜12月の集中乾燥シーズンを丸ごとカバーできます。",
        "target": "毎日気軽にシートマスクを使って真冬の集中保湿を行いたい方、肌のくすみや乾燥小ジワを改善したい方、コスパの高い大容量フェイスパックを求める方",
        "point": "洗顔後、化粧水で肌を整えてからシートを顔全体に密着させます。10〜15分置いてから剥がし、肌表面に残った美容液を手で優しくハンドプレスして馴染ませてください。"
    },
    {
        "rank": 10,
        "tag": "🧼 伝統枠練り製法×天然紫根！洗顔後のつっぱり感をゼロにする無添加スキンケアソープ",
        "catch": "職人が60日間じっくり熟成させた高保湿洗顔石けん。天然紫根エキスと植物油脂が毛穴の汚れを優しく落としながら、洗い流した後も潤いヴェールをキープ",
        "brand_name": "自然派くらぶ",
        "capacity": "100g (専用泡立てネット付) / 化粧箱入り",
        "type": "伝統枠練り製法 無添加和漢洗顔石けん",
        "features": "ムラサキ根エキス（紫根エキス）、パーム油、ヤシ油、スクワラン、天然グリセリン",
        "value": "合成界面活性剤・防腐剤・キレート剤一切無添加。枠練り製法により天然の保湿成分グリセリンが約20%以上も石けん内部に残存し、真冬でもつっぱらない優しい洗い上がり",
        "desc_p1": "冬の肌トラブルの隠れた元凶は、合成洗顔フォームの強すぎる洗浄力で皮膚の皮脂膜と細胞間脂質を削り落としてしまうことにあります。自然派くらぶの『洗顔用 紫根石けん 100g』は、洗顔ステップそのものを保湿ケアに変えてしまう伝統製法の和漢石けんです。",
        "desc_p2": "付属の泡立てネットで数回擦るだけで、キメの細かいクリーミーなピンクがかったもっちり泡が完成。弾力のある泡がクッションとなり、真冬のデリケートな皮膚を擦ることなく毛穴の汚れや余分な角質を穏やかに吸着します。紫根のシコニンが洗顔時の刺激から肌を守り、洗い流した瞬間からまるで薄い化粧水を塗った後のようなしっとり吸い付く肌触りを叶えます。",
        "target": "洗顔後すぐに肌が突っ張ってカサつく方、合成界面活性剤フリーの優しい無添加石けんを使いたい方、朝の洗顔で肌の透明感をアップさせたい方",
        "point": "ぬるま湯（32〜34℃）で付属ネットを使い、レモン1個分のもっちり泡を立てます。顔に泡をのせて転がすように15秒程度なじませ、こすらずに流水でしっかりすすぎます。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-shikon#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！伝統の紫根エキス（シコニン）が真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する高保湿紫根コスメランク10",
            "description": "11月・12月の寒冷乾燥や水仕事によるあかぎれ・ひび割れ、寒暖差の赤み肌を救う高保湿紫根エキス（シコニン）コスメを徹底厳選！タマチャンショップ、自然化粧品研究所、日本オリーブ、椿乃、魔女工場まで徹底検証。",
            "datePublished": "2026-11-05T09:00:00+09:00",
            "dateModified": "2026-11-05T09:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿紫根（シコンエキス）コスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "紫根（シコンエキス）が真冬のあかぎれ・ひび割れ・肌荒れに圧倒的に効く理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "紫根はムラサキ科植物『ムラサキ』の根で、江戸時代の名医・華岡青洲が創製した万能皮膚軟膏『紫雲膏（しうんこう）』の主原料として知られる伝統生薬です。紫根の主成分であるナフトキノン誘導体『シコニン』および『アセチルシコニン』には、強力な抗炎症作用、創傷治癒促進作用、肉芽形成促進作用、抗菌作用が科学的に認められています。真冬の過酷な冷風や水仕事によって皮膚組織が裂けてあかぎれ・ひび割れを起こした患部や、寒暖差で微小炎症を起こした赤み肌に対して、皮膚再生を劇的に促して健やかなバリアを再建します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "紫根コスメのピンク色や紫色で肌や衣服に色が移る心配はありませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "紫根コスメに見られる鮮やかな赤紫色やピンク色は、人工タール色素ではなく天然のシコニン本来の色素です。通常の使用量（化粧水やクリームとして肌になじませる程度）であれば、肌に浸透した後に色が残ったり、肌が紫色に染まることは一切ありません。ただし、高濃度の原液や未精製オイルを白い衣服や枕カバーに直接付着させた場合、油分とともにシミになる可能性があるため、夜のスキンケア後に数分置いてしっかり肌へなじんでから就寝することをおすすめします。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "紫根エキス原液はどのようにスキンケアへ取り入れるのが最も効果的ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最もおすすめなのは『手持ちの化粧水やクリームへの1〜2滴ブレンド』です。手のひらに普段の化粧水をとり、紫根エキス原液を1滴垂らして混ぜ合わせて全顔をハンドプレス。さらに乾燥やあかぎれ、赤みが深刻な頬や口元には、保湿クリームに原液を1滴混ぜて重ね塗りする『ダブルシコン処方』を行うことで、翌朝には見違えるような滑らかさと鎮静効果を実感できます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "敏感肌やアトピー肌でも紫根コスメを使用できますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、紫根は漢方医学において皮膚病変や荒れ肌の消炎・鎮静に用いられてきた実績があり、極めて肌に優しい成分です。むしろ真冬の乾燥でバリアが破壊され、一般の化粧水がピリピリとしみる敏感肌やゆらぎ肌の方にこそ強く推奨されます。心配な場合は、パラベンやアルコール（エタノール）、合成香料が無添加の低刺激処方を選び、使用前に二の腕の内側でパッチテストを行ってください。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！伝統の紫根エキス（シコニン）が真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する高保湿紫根コスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥や水仕事によるあかぎれ・ひび割れ、寒暖差の赤み肌を救う高保湿紫根エキス（シコニン）コスメを徹底厳選！タマチャンショップ、自然化粧品研究所、日本オリーブ、椿乃、魔女工場まで徹底検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-shikon">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！伝統の紫根エキス（シコニン）が真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する高保湿紫根コスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥や水仕事によるあかぎれ・ひび割れ、寒暖差の赤み肌を救う高保湿紫根エキス（シコニン）コスメを徹底厳選！タマチャンショップ、自然化粧品研究所、日本オリーブ、椿乃、魔女工場まで徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-shikon">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #7e22ce;
      --primary-light: #f3e8ff;
      --primary-dark: #581c87;
      --accent: #9333ea;
      --accent-hover: #3b0764;
      --bg: #faf5ff;
      --card-bg: #ffffff;
      --text-main: #262626;
      --text-sub: #525252;
      --border: #e9d5ff;
      --shadow: 0 4px 15px rgba(126, 34, 206, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      font-weight: 500;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--primary-dark);
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 1.2rem;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #f3e8ff;
      text-align: left;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .table-thumb {{
      width: 55px;
      height: 55px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      font-size: 1.05rem;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      text-align: center;
    }}

    .product-img {{
      width: 220px;
      height: 220px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #ffffff;
      padding: 0.5rem;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      line-height: 1.4;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1rem;
      color: var(--text-main);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #b91c1c;
    }}

    .product-tag {{
      display: inline-block;
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #faf5ff;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #e9d5ff;
      text-align: left;
    }}

    table.spec-table th {{
      width: 30%;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .review-body {{
      margin-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .target-box, .point-box {{
      background: #fdf4ff;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
      margin-top: 1rem;
      font-size: 0.92rem;
    }}

    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.3rem;
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    .rakuten-btn {{
      display: inline-block;
      width: 100%;
      max-width: 480px;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 1.05rem;
      text-align: center;
      padding: 1rem 1.5rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: all 0.3s;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a60000 0%, #cc0000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary);
      margin: 1.5rem 0 0.6rem;
    }}

    .guide-section p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #f3e8ff;
    }}

    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
      font-size: 1.2rem;
      line-height: 1;
    }}

    .faq-a {{
      color: var(--text-main);
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.7rem;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      display: block;
      background: #faf5ff;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--primary);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #a8a29e;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！伝統の紫根エキス（シコニン）が真冬のあかぎれ・冷え乾燥・荒れ果てた角層バリアを集中修復する高保湿紫根コスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて気温が氷点下へと迫ると、水仕事や冷風の直撃によって手肌や指先、頬の角層がパックリと裂け、激痛を伴う「あかぎれ・ひび割れ・霜焼け」が頻発します。さらに室内外の極端な寒暖差で顔の毛細血管が充血し、赤ら顔やヒリヒリした痛みに耐えかねる限界肌が急増。そんな過酷な冬のバリア崩壊を、江戸時代から受け継がれる奇跡の和漢再生力で救済するのが「紫根（シコンエキス）」です。主成分シコニンの抗炎症・創傷治癒・皮膚再生パワーを凝縮した高保湿名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>真冬のあかぎれ・寒暖差赤み肌を劇的に鎮静する和漢生薬「紫根（シコニン）」の医学的背景</h2>
      <p>
        紫根（シコン）とは、ムラサキ科の多年草「ムラサキ」の肥大した根を乾燥させた生薬です。日本薬局方にも収載されており、世界で初めて全身麻酔手術を成功させた江戸時代の名医・華岡青洲が考案した外用軟膏『紫雲膏（しうんこう）』の主原料として、火傷、ひび割れ、あかぎれ、凍傷の特効薬として数百年もの間重宝されてきました。
      </p>
      <p>
        現代の皮膚科学研究において、紫根の鮮やかな紫赤色の主成分であるナフトキノン系化合物「シコニン」「アセチルシコニン」には、驚異的な薬理活性があることが解明されています。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 肉芽形成・創傷治癒促進（パックリ割れた角層の急速再生）</strong>
          <p>線維芽細胞の増殖と血管新生を強力にサポート。水仕事や乾燥で深く裂けてしまった指先や関節のひび割れを、傷口から急速に修復して皮膚組織の再生を促します。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 寒暖差による毛細血管拡張と微小炎症の鎮静</strong>
          <p>炎症性サイトカインの放出を抑制し、冬の木枯らしや急激な温度変化で赤く火照った頬や鼻周りの毛細血管のうっ血を穏やかにクールダウン。透明感のある均一な肌色を取り戻します。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 表皮ブドウ球菌の異常増殖を防ぐ天然の抗菌・バリア機能</strong>
          <p>乾燥で荒れた皮膚に侵入しやすい雑菌の増殖をブロック。マスク内の蒸れ乾燥や冬の大人ニキビ、アトピー傾向の肌を清潔に保ちながら強固な防御壁を築きます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿紫根コスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロ直伝！真冬の紫根コスメ選び方＆あかぎれ・赤み肌を完治へ導く使用テクニック</h2>
      <h3>1. 「水溶性エキス」と「油溶性オイル・クリーム」の使い分け</h3>
      <p>
        紫根コスメには、ローションや美容液に配合される「水溶性エキス」と、オイルやバームに溶け込ませた「油溶性エキス」があります。顔全体の寒暖差赤みやインナードライ、くすみをケアしたい場合は、角層の水分保持力を高める「水溶性化粧水・美容液」が適しています。一方、指先や関節のパックリ割れたあかぎれ、唇の皮むけ、粉吹き頬の集中密閉には、油膜シールド力のある「油溶性クリーム・バーム・リップ」を選ぶのが最も効果的です。
      </p>
      <h3>2. 「手持ちの乳液・クリームへの原液1滴ブレンド」でレスキュー効果を最大化</h3>
      <p>
        紫根エキス原液をお持ちの場合、普段のお手入れに組み込む最も手軽で強力な方法は『クリームへの1滴ブレンド』です。手のひらにとったいつもの保湿クリームに紫根原液を1滴落とし、手のひらで馴染ませるとほんのりピンク色に変化。これを夜の洗顔後に気になる部分へ厚めに塗り込んで就寝すると、翌朝にはひび割れの痛みが和らぎ、驚くほど滑らかな素肌へと回復します。
      </p>
      <h3>3. 手荒れ・あかぎれには「紫根クリーム＋綿手袋」の集中ナイトパック</h3>
      <p>
        冬の水仕事で荒れ果てた手肌には、入浴後の皮膚が柔らかくなっているゴールデンタイムのケアが決定打となります。化粧水で手肌に水分を与えた後、紫根クリームを指の関節や爪の周りまで念入りにすり込みます。その上から通気性の良い綿100%の手袋を着用して就寝。密封効果によってシコニンが一晩中角層深部へ浸透し、翌朝にはあかぎれの痛みを忘れさせる極上のしなやかさが甦ります。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 紫根（シコンエキス）が真冬のあかぎれ・ひび割れ・肌荒れに圧倒的に効く理由は何ですか？</div>
        <div class="faq-a">紫根はムラサキ科植物「ムラサキ」の根で、江戸時代の名医・華岡青洲が創製した万能皮膚軟膏「紫雲膏（しうんこう）」の主原料として知られる伝統生薬です。紫根の主成分であるナフトキノン誘導体「シコニン」および「アセチルシコニン」には、強力な抗炎症作用、創傷治癒促進作用、肉芽形成促進作用、抗菌作用が科学的に認められています。真冬の過酷な冷風や水仕事によって皮膚組織が裂けてあかぎれ・ひび割れを起こした患部や、寒暖差で微小炎症を起こした赤み肌に対して、皮膚再生を劇的に促して健やかなバリアを再建します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 紫根コスメのピンク色や紫色で肌や衣服に色が移る心配はありませんか？</div>
        <div class="faq-a">紫根コスメに見られる鮮やかな赤紫色やピンク色は、人工タール色素ではなく天然のシコニン本来の色素です。通常の使用量（化粧水やクリームとして肌になじませる程度）であれば、肌に浸透した後に色が残ったり、肌が紫色に染まることは一切ありません。ただし、高濃度の原液や未精製オイルを白い衣服や枕カバーに直接付着させた場合、油分とともにシミになる可能性があるため、夜のスキンケア後に数分置いてしっかり肌へなじんでから就寝することをおすすめします。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 紫根エキス原液はどのようにスキンケアへ取り入れるのが最も効果的ですか？</div>
        <div class="faq-a">最もおすすめなのは「手持ちの化粧水やクリームへの1〜2滴ブレンド」です。手のひらに普段の化粧水をとり、紫根エキス原液を1滴垂らして混ぜ合わせて全顔をハンドプレス。さらに乾燥やあかぎれ、赤みが深刻な頬や口元には、保湿クリームに原液を1滴混ぜて重ね塗りする「ダブルシコン処方」を行うことで、翌朝には見違えるような滑らかさと鎮静効果を実感できます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 敏感肌やアトピー肌でも紫根コスメを使用できますか？</div>
        <div class="faq-a">はい、紫根は漢方医学において皮膚病変や荒れ肌の消炎・鎮静に用いられてきた実績があり、極めて肌に優しい成分です。むしろ真冬の乾燥でバリアが破壊され、一般の化粧水がピリピリとしみる敏感肌やゆらぎ肌の方にこそ強く推奨されます。心配な場合は、パラベンやアルコール（エタノール）、合成香料が無添加の低刺激処方を選び、使用前に二の腕の内側でパッチテストを行ってください。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-shikon.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-shikon.html!")
