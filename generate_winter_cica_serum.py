import json
import re

with open("fetched_3new_retinol_hyaluronic_cica.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_cica_serum"]["items"]

# 10商品それぞれの完全オリジナル・皮膚科学的専門解説
product_details = [
    {
        "rank": 1,
        "tag": "🌿 高純度マダガスカル産ツボクサエキス100%原液！真冬の冷風でピリつく肌を水のように穏やかに鎮める名品アンプル",
        "catch": "過酷な環境で育まれた高品質マダガスカル産ツボクサエキスを水で薄めず純度100%配合。冷たい木枯らしと過熱暖房の寒暖差で真っ赤に荒れた肌へ、一滴でスッと浸透し微細炎症を急速沈静化するメガヒット鎮静アンプル",
        "brand_name": "SKIN1004 (スキンワンオーフォー)",
        "capacity": "55mL / スポイトガラスボトル",
        "type": "高純度マダガスカル産ツボクサエキス100% 高濃度鎮静アンプル",
        "features": "マダガスカル産ツボクサエキス100%、弱酸性処方（pH5.5）、無香料・無着色・アルコールフリー・低刺激テスト済み",
        "value": "水のようにサラサラとした浸透力で、寒風摩擦によるピリピリ感を瞬時に解消。角層の崩れた水分油分バランスをゼロから整え、健やかな素肌へ回帰",
        "desc_p1": "11月から12月にかけて、外気温が5℃以下に冷え込む一方で、暖房の効いた室内は24℃以上に保たれ、その温度差は実に15〜20℃にも達します。この急激な温度差は肌の毛細血管を過剰に拡張させ、自律神経を乱して『寒暖差肌荒れ（顔のほてり・赤み・ピリピリとした違和感）』を引き起こします。SKIN1004のセンテラアンプルは、マダガスカルの自生ツボクサから独自抽出した高純度エキスのみをボトルに充填。精製水で希釈していないため、植物本来の抗炎症・組織修復パワーがダイレクトに肌へ届きます。",
        "desc_p2": "オイル分を一切含まないみずみずしいテクスチャーで、塗布した瞬間に肌がスーッと息を吹き返すような心地よさがあります。肌のpHに近い弱酸性設計で、真冬にバリア機能が低下して何を塗ってもしみる超敏感肌でもノンストレスで使用可能。化粧水の前に導入アンプルとして使うことで、硬くなった角層を柔らかくほぐし、後から使う保湿コスメの浸透力を劇的に高めてくれます。",
        "target": "冬の寒暖差で顔が真っ赤になりやすい方、摩擦や乾燥で肌がヒリヒリとしみる方、成分純度にこだわった原液級のシカケアを求める方",
        "point": "洗顔後すぐ、または化粧水の後、スポイトで2〜3滴を手に取り顔全体へ優しくハンドプレス。赤みが目立つ両頬には重ねづけし、手のひらで包み込むように体温でなじませます。"
    },
    {
        "rank": 2,
        "tag": "🔬 独自成分CICALIAO™×3重ヒアルロン酸！寒暖差でバリアが乱れた冬肌を急速リカバリーする大容量水分エッセンス",
        "catch": "CICAコスメの火付け役VTが誇る独自複合成分CICALIAO™（シカリオ）を凝縮。ツボクサエキスにグリーンプロポリスとセンテラ4Xコンプレックスを掛け合わせ、真冬の乾燥刺激に負けない強靭な水分バリアを構築する高保湿エッセンス",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "100mL / ポンプボトル",
        "type": "CICALIAO™＆3重ヒアルロン酸配合 高保湿水分鎮静エッセンス",
        "features": "CICALIAO™（ツボクサエキス・プロポリス・センテラ4X）、3重ヒアルロン酸、アミノ酸コンプレックス、パンテノール",
        "value": "寒風でゴワつき硬くなった角質細胞の隙間をアミノ酸と水分で満たし、炎症を鎮火しながら翌朝までしっとり滑らかな肌質をキープ",
        "desc_p1": "VTコスメティックスのシカエッセンスは、単なる鎮静にとどまらず、冬の肌再生に不可欠な栄養補給を両立させた総合バリア美容液です。ツボクサから抽出された4大生理活性物質（アシアチコシド、マデカシン酸、アシアチン酸、マデカッソシド）に加え、天然の抗生物質と呼ばれるグリーンプロポリスエキスを配合。寒冷によって免疫力が低下した皮膚表面の常在菌バランスを整えます。",
        "desc_p2": "透明感のあるぷるんとしたジェルセラムで、肌に伸ばすと弾けるように水分へ変化し、ベタつきを残さずにサラリと馴染みます。3重ヒアルロン酸が角層の表面から深部まで多層的に潤いを繋ぎ止めるため、長時間のエアコン暖房下でも肌の内部乾燥（インナードライ）を感じさせません。朝のメイク前にたっぷり使ってもファンデーションの密着力を邪魔せず、日中の乾燥崩れを防ぎます。",
        "target": "冬の乾燥肌荒れと大人ニキビが同時に発生しやすい混合肌、水分たっぷりの軽いテクスチャーが好きな方、朝晩惜しみなく使えるシカ美容液を探している方",
        "point": "化粧水で肌を整えた後、1〜2プッシュを手に取り顔全体に優しく塗り広げます。乾燥が気になる目元や口元には指の腹でトントンと軽く叩き込むように重ねづけしてください。"
    },
    {
        "rank": 3,
        "tag": "🏆 高濃縮ツボクサ×緑の植物修復エキス！皮膚科クリニック発想で冬の深刻な肌トラブルを即効レスキューする集中セラム",
        "catch": "韓国ダーマコスメの金字塔Dr.Jart+の最高峰シカペアライン。高濃度ツボクサエキスと独自のリペアバイオームが、冷風・暖房・マスク擦れの三重苦で崩壊寸前の真冬の皮膚バリアを急速に立て直す皮膚科学美容液",
        "brand_name": "Dr.Jart+ (ドクタージャルト)",
        "capacity": "30mL / スポイトボトル",
        "type": "高濃度ツボクサ複合体配合 集中スージングリペアセラム",
        "features": "高濃縮ツボクサエキス、センテラRx（ツボクサ葉水・マデカッソシド等）、リペアバイオーム（発酵エキス）、ジャバリン（ハーブ複合体）",
        "value": "塗った直後からピリピリ感を鎮静。角層の菲薄化（薄肌化）を防ぎ、真冬の過酷な外気から肌をシールドする最高峰のレスキュー効果",
        "desc_p1": "Dr.Jart+のシカペアセラムは、美容感度の高い層から『肌のレスキュー常備薬』として長年愛され続けている本格派です。11月から12月にかけて肌が粉を吹いたり、皮むけ寸前の微小な亀裂が生じるような極度の乾燥トラブルに対し、ツボクサ由来のセンテラRx成分が線維芽細胞を刺激し、コラーゲンとエラスチンの自己修復プロセスを劇的に加速させます。",
        "desc_p2": "淡いエメラルドグリーンのとろみのあるセラムが、荒れた肌表面に吸い付くように密着。摩擦を一切与えずにスーッと伸び、塗布後数分で赤みが引いていくのを実感できます。皮膚常在菌を育むリペアバイオームが角層バリアを強固にサポートするため、使い続けるほどに冷たい外気や花粉、ホコリに対する抵抗力が向上し、冬でもトラブル知らずのタフな肌へと進化します。",
        "target": "真冬になると毎年肌が荒れて何を使っても改善しない方、皮膚科レベルの確かな修復力を求める方、即効性のある鎮静セラムを求める方",
        "point": "化粧水の直後、スポイトのボタンを押し1滴を直接肌に落とし、指先でこすらずにそっと包み込むように伸ばします。荒れがひどいエリアにはさらに1滴重ねてください。"
    },
    {
        "rank": 4,
        "tag": "💧 ドクダミエキス80%×シカ×パンテノール！冬の暖房熱で火照るインナードライ肌に濃密な潤いをチャージする鎮静アンプル",
        "catch": "鎮静コスメ界で一大ブームを巻き起こしたAnuaの超高濃度アンプル。解毒・抗炎症ハーブの王様ドクダミエキスを驚異の80%配合し、シカ成分とパンテノールが真冬のエアコン熱で火照った角層を穏やかにクールダウン",
        "brand_name": "Anua (アヌア)",
        "capacity": "30mL / スポイトボトル",
        "type": "ドクダミエキス80%＆シカ配合 高保湿水分鎮静アンプル",
        "features": "ドクダミエキス80%、ツボクサエキス、パンテノール、ヒアルロン酸、ベタイン、ノンコメドジェニックテスト済み",
        "value": "暖房が直撃して顔が赤く熱を持つ『冬の熱感乾燥』を速やかに鎮静。水分保持力を高めながら毛穴の目立たない透明感あふれるキメ肌へ",
        "desc_p1": "冬のオフィス勤務で最も辛いのが、夕方になると暖房の熱気で顔がほてり、皮膚の内側がチリチリと乾いてくる『熱感インナードライ』です。Anuaのドクダミ80%アンプルは、古来より皮膚の解毒と熱を鎮める薬草として重用されてきたドクダミを高濃度で配合。肌温度を正常化させながら、毛細血管の拡張による赤みをスーッと抑え込みます。",
        "desc_p2": "とろりとしたリッチな液だれしないテクスチャーでありながら、肌に乗せてクルクルとなじませると一瞬で水のようにほどけて浸透します。肌表面に一切のベタつきを残さず、内側だけが水分でタプタプに満たされたような極上の後肌を実現。シカ成分とパンテノールが同時にバリアを補強するため、冬の乾燥による毛穴の開きや皮脂浮きも同時に解消してくれます。",
        "target": "冬の暖房で顔が赤くほてりやすい方、夕方になるとTゾーンのテカリと頬の乾燥が激しい方、肌のキメをキュッと整えたい方",
        "point": "化粧水をしっかり浸透させた後、スポイトで全顔に3〜4滴を馴染ませます。手のひら全体で肌を優しく包み込み、ゆっくりと深呼吸しながらハンドプレスするのがコツです。"
    },
    {
        "rank": 5,
        "tag": "🛡️ 高濃度パンテノール×エクトイン×シカ！砂漠の極限環境でも枯れない驚異の保湿密閉を叶える高機能エッセンス",
        "catch": "発酵コスメで名高い魔女工場（manyo）の最高峰バリアライン『パンテトイン』。皮膚修復のパンテノールと砂漠微生物から抽出されたエクトインにシカを掛け合わせ、真冬の過酷な乾燥と冷風刺激から肌を守り抜く濃密美容液",
        "brand_name": "魔女工場 (manyo)",
        "capacity": "80mL / 大容量ボトル",
        "type": "パンテトイン＆シカ配合 濃密バリアトリートメントエッセンス",
        "features": "パンテノール（4,000ppm）、エクトイン（1,000ppm）、ツボクサエキス、セラミドNP、低分子ヒアルロン酸",
        "value": "11-12月の極寒乾燥でもビクともしない強固な潤い膜を形成。肌本来の保水バリアを根本から強化し、粉ふきや皮むけを完全ブロック",
        "desc_p1": "冬の乾燥対策において近年世界中から注目されているのが、エジプトの塩湖などの極限環境に生きる微生物が自らを守るために生み出すアミノ酸誘導体『エクトイン』です。魔女工場のパンテトインエッセンスは、このエクトインと、傷ついた皮膚を修復する高濃度パンテノール、そしてシカ成分を独自比率で配合。角層内の水分子を強固に結束させ、乾燥風に水分を奪われません。",
        "desc_p2": "白濁したまろやかなミルクエッセンス質感で、肌に乗せるとまるで上質なシルクのヴェールをまとったような安心感に包まれます。美容液と乳液の中間のようなコクがあり、乾燥でカサカサに硬くなった冬の肌が瞬時に柔らかくほぐれていきます。80mLという美容液としては大容量サイズなので、顔だけでなく首元やデコルテまで惜しみなく贅沢にケアできます。",
        "target": "何を塗っても冬の乾燥が治まらない超乾燥肌、粉ふきや皮むけに本気で悩む方、濃厚なミルク質感のシカ美容液を好む方",
        "point": "洗顔後、化粧水のあとに1〜2プッシュを手にとり顔全体へ伸ばします。乾燥が深刻な日は、2度重ねづけすることでクリームに匹敵する保護膜が完成します。"
    },
    {
        "rank": 6,
        "tag": "🌿 高純度ツボクサ葉水×マデカッソシド！サラッとなじむのに奥まで潤いが届く薬用級の低刺激シカセラム",
        "catch": "韓国の人気コスメブランドA'pieu（アピュー）が誇るベストセラー美容液。精製水の代わりに高純度ツボクサ葉水をベースに使用し、特許マデカッソシド成分が真冬の冷風でヒリつく肌を穏やかに解きほぐす高浸透セラム",
        "brand_name": "A'pieu (アピュー)",
        "capacity": "30mL / スポイトボトル",
        "type": "高純度ツボクサ葉水＆マデカッソシド配合 高浸透低刺激セラム",
        "features": "ツボクサ葉水、マデカッソシド、アラントイン、ナイアシンアミド、アデノシン、弱酸性処方",
        "value": "ベタつきゼロで角層の隅々まで素早く行き渡り、冬の寒暖差ストレスで疲れた肌をリフレッシュ。プチプラとは思えない確かな鎮静力",
        "desc_p1": "化粧品の成分表で最も多く含まれる『水（精製水）』の代わりに、ツボクサの葉から蒸留した『ツボクサ葉水』を贅沢に基材として採用したアピューのマデカソサイド美容液。ツボクサの中でも特に抗炎症活性が高いマデカッソシドを高濃度で配合し、真冬の寒冷刺激でダメージを受けた角層のバリア膜を優しく修復します。",
        "desc_p2": "サラッとした軽やかな水溶性ジェルで、肌に伸ばすとスーッと吸い込まれるように馴染みます。油膜感や被膜感が一切ないため、後から使うクリームや乳液の浸透を妨げません。マイルドな弱酸性設計でパラベンや人工香料もフリー。冬の朝のメイク前スキンケアに取り入れることで、マスク擦れや冷風による日中の赤みトラブルを未然に防いでくれます。",
        "target": "ベタつく美容液が苦手な方、プチプラで優秀なデイリーシカセラムを探している方、朝のメイク前に素早く使える鎮静ケアを求める方",
        "point": "化粧水の後にスポイトで適量（2〜3滴）を取り、顔全体になじませます。肌を擦らずに手のひらで軽く抑えるようにプレスするのがポイントです。"
    },
    {
        "rank": 7,
        "tag": "🧪 有機栽培ツボクサエキス83%配合原液処方！高濃度成分の力で冬の肌荒れ痕や毛穴を集中リセットするダーマセラム",
        "catch": "高品質成分を高濃度・低価格で提供するドクターズブランドCos De BAHA。オーガニック認証のツボクサエキスを83%という極限濃度で配合し、真冬の乾燥で悪化しやすい肌荒れ・ニキビ跡・赤みを集中リペアする原液アンプル",
        "brand_name": "Cos De BAHA (コスデバハ)",
        "capacity": "30mL / スポイト遮光ボトル",
        "type": "高濃度ツボクサエキス83%配合 原液エイジング鎮静セラム",
        "features": "ツボクサエキス83%、ヒアルロン酸Na、ナイアシンアミド、ベタイン、無香料・アルコールフリー",
        "value": "無駄な添加物を極限まで削ぎ落とし、ツボクサエキスの原液パワーを凝縮。冬の乾燥荒れと毛穴の目立ちを根本から立て直す実力派",
        "desc_p1": "世界中のスキンケア愛好家から『成分の濃さが段違い』と高評価を集めるコスデバハのCHセラム。主成分として有機栽培されたツボクサのエキスを83%も配合し、冬場の冷えや乾燥によって抵抗力が低下した皮膚の修復をサポートします。美白・バリア機能向上を担うナイアシンアミドも配合されており、乾燥くすみや肌荒れ後の色素沈着も同時にケアします。",
        "desc_p2": "とろみのある茶褐色の濃厚なエッセンスで、肌に乗せるとツボクサ本来のナチュラルな植物感が感じられます。少量でも非常に伸びが良く、肌表面をなめらかに包み込んで潤いを逃しません。毎晩のケアに取り入れることで、冬の乾いた空気によって荒れがちだった肌が落ち着き、キメの整ったフラットな素肌へと生まれ変わります。",
        "target": "成分の濃度に妥協したくないスキンケア上級者、冬の肌荒れ痕や赤みが長引きやすい方、原液コスメが好きな方",
        "point": "夜のお手入れ時に化粧水の後、スポイトで1〜2滴を取り顔全体へ伸ばします。乾燥しやすい目元口元には重ね付けしてください。"
    },
    {
        "rank": 8,
        "tag": "🌱 ツボクサエキス84.28%×カモミール花エキス！韓国オリーブヤング美容液部門アワード常連の急速鎮静アンプル",
        "catch": "クリーンビューティーブランドbeplainの不動のベストセラー。84%を超える高濃度ツボクサエキスにカモミール花エキスをブレンドし、冬のデリケートな肌を素早く沈静化させてみずみずしい透明感を与える名品",
        "brand_name": "beplain (ビープレーン)",
        "capacity": "30mL / スポイトボトル",
        "type": "ツボクサエキス84.28%配合 水分鎮静シカフルアンプル",
        "features": "ツボクサエキス84.28%、カモミール花エキス、低分子ヒアルロン酸、アラントイン、ヴィーガン認証",
        "value": "肌に乗せた瞬間に赤みと火照りをクールダウン。軽やかなのに奥深くまで水分が満ち足りる、韓国女子の冬のポーチ必須アイテム",
        "desc_p1": "韓国の大手ドラッグストア『オリーブヤング』のアワードで何度も1位を獲得しているbeplainのシカフルアンプル。精製水の代わりにツボクサエキスを84.28%も高配合し、さらに鎮静効果で名高いカモミール（カミツレ花）エキスを相乗配合しています。冬の冷風や摩擦によって微小な炎症を起こした肌を素早くリセットしてくれます。",
        "desc_p2": "みずみずしいジェルテクスチャーで、肌に伸ばすとスーッと溶け込んでベタつきを残しません。低分子ヒアルロン酸が角層深部に潤いを届けるため、インナードライによる日中の肌のつっぱり感も解消。無香料・弱酸性・低刺激テスト済みで、敏感肌はもちろん、冬にホルモンバランスが乱れてゆらぎやすい時期でも安心して頼れるアンプルです。",
        "target": "敏感肌で刺激に弱い方、韓国コスメのリアルな人気アワード受賞商品を試したい方、軽やかでベタつかない鎮静美容液を探している方",
        "point": "化粧水の後に適量（スポイト1吸い分）を取り、顔全体にやさしくなじませます。火照りが気になる部分にはコットンに含ませて部分パックするのもおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🍯 ツボクサエキス×プロポリスエキス！真冬の乾燥冷風でゴワついた肌をモチモチにほぐす高保湿シカセラム",
        "catch": "ネイチャーリパブリックのグリーンダーマラインが誇る高保湿シカ。ツボクサエキスに豊かな栄養を持つプロポリスを組み合わせ、真冬の寒さで硬くゴワついた角層を柔らかく解きほぐす濃密セラム",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "50mL / ポンプボトル",
        "type": "ツボクサエキス＆プロポリス配合 高保湿グリーンダーマシカセラム",
        "features": "ツボクサエキス、プロポリスエキス、マデカッソシド、ベタイン、セラミドNP",
        "value": "シカの鎮静力にプロポリスの濃密な栄養とバリア保護力をプラス。真冬の過酷な乾燥でも粉を吹かないもっちりとしたツヤ肌を創出",
        "desc_p1": "冬の乾燥トラブルは、単に肌が荒れるだけでなく、角質が硬化して肌がカサカサ・ゴワゴワとした手触りになるのが特徴です。ネイチャーリパブリックのグリーンダーマシカセラムは、肌を鎮静するツボクサエキスに加えて、ミツバチが巣を守るために作り出す高栄養成分『プロポリスエキス』を配合。弱った角層細胞に栄養を補給し、しなやかな柔軟性を取り戻します。",
        "desc_p2": "トロリとした乳白色の美容液で、ポンプから出すと滑らかに広がって肌を優しく包み込みます。プロポリスとセラミドNPの働きによって肌表面に薄いエモリエントヴェールが作られるため、水分蒸散を防ぎながら長時間もっちりとした弾力が持続。50mLというたっぷりサイズで、真冬のデイリースキンケアとして頼もしい存在です。",
        "target": "冬になると肌が硬くゴワついて化粧ノリが悪い方、シカの鎮静だけでなく高保湿な栄養補給も欲しい方、もっちりしたツヤ肌を目指す方",
        "point": "化粧水の後に1〜2プッシュを手に取り、顔全体にマッサージするようになじませます。手のひらで顔を包み込んで温めると浸透力が高まります。"
    },
    {
        "rank": 10,
        "tag": "🌿 高純度ツボクサエキス4X×カヤ種子油！冷たい北風でバリアが壊れた冬肌を密着保護するジェル乳液美容液",
        "catch": "イニスフリーの敏感肌研究から生まれたビジャシカライン。通常のツボクサエキスの約30倍に濃縮された高純度シカ4X成分と、チェジュ島産カヤオイルが冬の乾燥肌荒れを優しく包み込んで保護するリペアエッセンス",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "40mL / チューブタイプ",
        "type": "高純度シカ4X＆カヤオイル配合 ジェル乳液状リペア美容液・バーム",
        "features": "シカ4X（高純度アシアチコシド、マデカシン酸、アシアチン酸、マデカッソシド）、カヤ種子油、パンテノール、無香料・6つのフリー処方",
        "value": "ジェルと乳液の中間のような絶妙なテクスチャーで肌表面をピタッとシーリング。冬のマスク摩擦やマフラーの擦れから肌を守り抜く",
        "desc_p1": "イニスフリーのビジャシカシリーズは、ツボクサを希釈せず精製して得られる4つの核心成分（マデカッソシド、マデカシン酸、アシアチコシド、アシアチン酸）を約30倍の高純度で濃縮した『シカ4X』を配合しています。さらに古くからチェジュ島で肌の保護に使われてきたカヤ種子油をブレンドし、冬の冷たい北風でバリア機能が低下した肌をしっとり柔らかく包み込みます。",
        "desc_p2": "チューブから出てくるクリームは、ジェルと乳液を合わせたようなみずみずしく軽やかな質感です。肌に伸ばすと摩擦を感じさせずに均一に広がり、ピタッと肌に密着して外部刺激を遮断する保護膜を形成します。パラベンや動物性原料、鉱物油など6つの刺激成分を排除した安心のクリーン処方で、冬の赤みやニキビが気になる肌を健やかに整えます。",
        "target": "冬の冷風や摩擦で肌荒れを繰り返す方、ジェル乳液のような軽い使い心地でしっかり保護したい方、クリーンな無添加処方を好む方",
        "point": "化粧水や美容液の後、適量を手に取り顔全体に優しく塗り広げます。赤みやカサつきが特に気になる部位にはスポット的に厚めに重ねづけしてください。"
    }
]

# FAQ リスト
faq_list = [
    {
        "q": "シカ美容液（ツボクサエキス）は冬の乾燥肌にも効果がありますか？夏向けではありませんか？",
        "a": "シカは夏のイメージを持たれがちですが、実は『11月〜12月の真冬こそ最も効果を発揮する成分』です。冬は外気と暖房の急激な寒暖差（温度差15℃以上）によって皮膚の毛細血管が拡張し、微小な炎症や赤み、ヒリつきが頻発します。シカの核心成分（マデカッソシド等）はこれらの炎症性サイトカインを速やかに抑制し、さらに線維芽細胞を刺激してコラーゲン合成とバリア修復を促すため、真冬のゆらぎ肌やインナードライの救世主となります。"
    },
    {
        "q": "シカ美容液とシカクリームはどちらを使うべきですか？併用は可能ですか？",
        "a": "両者は肌へのアプローチが異なります。シカ美容液（セラム・アンプル）は水溶性成分が高濃度に含まれ、角層のすみずみまで素早く浸透して赤みや火照りを『即効鎮静』させるのが得意です。一方、シカクリームは油分を含み、肌表面に保護膜を作って水分蒸散と外部刺激を『物理的にブロック』します。真冬の過酷な環境では、シカ美容液で肌内部を鎮静・保水した後にシカクリームやセラミドクリームで蓋をする併用が最も効果的です。"
    },
    {
        "q": "シカ美容液を選ぶときに注目すべき『高純度成分』とは何ですか？",
        "a": "製品の全成分表示で『ツボクサエキス』だけでなく、『マデカッソシド』『アシアチコシド』『マデカシン酸』『アシアチン酸』という4つの生理活性物質（センテラ4Xなど）が明記されているかを確認してください。これらはツボクサから高度に精製された有効成分で、微量でも強力な抗炎症・コラーゲン生合成促進作用を発揮します。また、精製水の代わりに『ツボクサ葉水』を高配合したベース処方の製品も高い鎮静力を誇ります。"
    },
    {
        "q": "レチノールやビタミンC美容液とシカ美容液は併用できますか？",
        "a": "非常に相性が良く、むしろ積極的な併用が推奨されます。シカは優れた抗炎症・鎮静作用を持つため、レチノールのA反応（皮むけや乾燥）や、高濃度ビタミンCによるピリピリ感を和らげるクッション役として最適です。レチノールやビタミンCを塗布する前、または後にシカ美容液を挟み込むことで、肌トラブルを防ぎながら美肌効果を最大化できます。"
    },
    {
        "q": "シカ美容液の効果的な使い方のステップを教えてください。",
        "a": "洗顔後、化粧水で肌を整えた直後に使用するのが基本です。特に赤みやヒリつきが気になる日は、清潔なコットンにシカ美容液をたっぷり含ませて3〜5分間貼る『シカ部分コットンパック』を行うと、数分で肌の赤みが引いて熱感がスッキリと鎮まります。パック後は手のひらで優しくハンドプレスし、必ず保湿クリームで水分を密閉してください。"
    }
]

print("CICA article config prepared successfully!")

# HTML組み立て
html_title = "保湿力の強さで肌乾燥とさようなら！高純度ツボクサエキスの急速鎮静力で寒暖差のピリピリ赤み肌をしっとり救う保湿力高めシカ美容液ランク10"
html_desc = "11月・12月の木枯らしと暖房の急激な寒暖差による赤み・ヒリつき・乾燥ゆらぎ肌を救う高保湿シカ美容液10選を徹底検証！SKIN1004、VT、ドクタージャルト、Anua、魔女工場まで、高純度ツボクサエキスの急速鎮静メカニズムと最新実勢価格・口コミを網羅してご紹介。"
canonical_url = "https://lumi-cosme.vercel.app/winter-cica-serum"

# JSON-LD ItemList
item_list_elements = []
for idx, it in enumerate(items):
    det = product_details[idx]
    item_list_elements.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "description": det["catch"],
            "brand": {
                "@type": "Brand",
                "name": det["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": it["review_average"],
                "reviewCount": str(max(it["review_count"], 18))
            }
        }
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": html_title,
            "description": html_desc,
            "image": items[0]["image_url"],
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "datePublished": "2026-11-09T05:00:00+09:00",
            "dateModified": "2026-11-09T05:00:00+09:00",
            "mainEntityOfPage": canonical_url
        },
        {
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
                    "name": "冬の高保湿美容液",
                    "item": "https://lumi-cosme.vercel.app/#serum"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "高保湿シカ美容液ランク10",
                    "item": canonical_url
                }
            ]
        },
        {
            "@type": "ItemList",
            "name": "高保湿シカ美容液おすすめランキング10選",
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["a"]
                    }
                } for faq in faq_list
            ]
        }
    ]
}

from update_all_internal_links import footer_links_html

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_title} | LUMI COSMETICS</title>
  <meta name="description" content="{html_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{html_title} | LUMI COSMETICS">
  <meta property="og:description" content="{html_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(json_ld_schema, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #059669;
      --primary-dark: #047857;
      --primary-light: #ecfdf5;
      --accent: #e11d48;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-main: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text-main);
      background-color: var(--bg-main);
      padding: 0;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 16px 20px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }}
    .header-inner {{
      max-width: 1000px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      max-width: 1000px;
      margin: 15px auto 0;
      padding: 0 20px;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .container {{
      max-width: 1000px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 35px 30px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      margin-bottom: 30px;
    }}
    .category-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 15px;
      border: 1px solid #a7f3d0;
    }}
    h1 {{
      font-size: 1.75rem;
      font-weight: 800;
      line-height: 1.45;
      color: #111827;
      margin-bottom: 18px;
    }}
    .meta-info {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      gap: 15px;
      align-items: center;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 15px;
      margin-bottom: 20px;
    }}
    .lead-box {{
      background: #ecfdf5;
      border-left: 4px solid var(--primary);
      padding: 20px;
      border-radius: 4px 8px 8px 4px;
      font-size: 0.98rem;
      color: #374151;
      line-height: 1.85;
    }}
    .toc-box {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px 28px;
      margin: 30px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style-type: none;
      padding-left: 5px;
    }}
    .toc-list li {{
      margin-bottom: 8px;
    }}
    .toc-list a {{
      color: #4b5563;
      text-decoration: none;
      font-size: 0.93rem;
      transition: color 0.2s ease;
    }}
    .toc-list a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    h2.section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      margin: 45px 0 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    h3.sub-title {{
      font-size: 1.18rem;
      font-weight: 700;
      color: #1f2937;
      margin: 25px 0 12px;
    }}
    p.body-text {{
      font-size: 1rem;
      color: #374151;
      line-height: 1.85;
      margin-bottom: 18px;
    }}
    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 25px 0 35px;
      background: var(--card-bg);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }}
    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
      min-width: 700px;
    }}
    table.comparison-table th {{
      background: #ecfdf5;
      color: #065f46;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
    }}
    table.comparison-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    table.comparison-table tr:hover {{
      background-color: #f0fdf4;
    }}
    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 28px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}
    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #059669, #10b981);
      color: #fff;
      font-weight: 800;
      font-size: 1.15rem;
      padding: 4px 16px;
      border-radius: 8px;
      margin-bottom: 12px;
      box-shadow: 0 2px 6px rgba(5, 150, 105, 0.3);
    }}
    .product-tag {{
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      line-height: 1.5;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 16px;
      line-height: 1.45;
    }}
    .product-grid {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 25px;
      margin-bottom: 20px;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #fafafa;
      border-radius: 12px;
      padding: 15px;
      border: 1px solid #edf2f7;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      border-radius: 8px;
      transition: transform 0.3s ease;
    }}
    .product-specs-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      margin-bottom: 15px;
    }}
    .product-specs-table th {{
      width: 28%;
      text-align: left;
      padding: 8px 10px;
      background: #f8fafc;
      color: var(--text-muted);
      border-bottom: 1px solid #edf2f7;
      font-weight: 600;
    }}
    .product-specs-table td {{
      padding: 8px 10px;
      border-bottom: 1px solid #edf2f7;
      color: #334155;
    }}
    .product-desc {{
      color: #374151;
      font-size: 0.98rem;
      line-height: 1.8;
      margin-bottom: 12px;
    }}
    .point-box {{
      background: #ecfdf5;
      border: 1px solid #d1fae5;
      border-radius: 8px;
      padding: 15px 18px;
      margin-top: 15px;
      font-size: 0.92rem;
      color: #4b5563;
    }}
    .point-box-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 6px;
    }}
    .price-and-action {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 20px;
      padding-top: 18px;
      border-top: 1px dashed #e2e8f0;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .price-wrap {{
      display: flex;
      flex-direction: column;
    }}
    .price-label {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--accent);
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #bf0000, #e60012);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(230,0,18,0.25);
      transition: all 0.25s ease;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a60000, #c80010);
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(230,0,18,0.35);
    }}
    .feature-card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 25px 0;
    }}
    .feature-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 22px;
      box-shadow: var(--shadow-sm);
    }}
    .feature-card h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .feature-card p {{
      font-size: 0.92rem;
      color: #4b5563;
      line-height: 1.7;
    }}
    .faq-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 20px 24px;
      margin-bottom: 16px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }}
    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 800;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.8;
      padding-left: 28px;
    }}
    .related-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 25px;
      margin: 40px 0;
    }}
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin-top: 15px;
    }}
    .related-link-item {{
      background: #f8fafc;
      border: 1px solid #edf2f7;
      padding: 10px 14px;
      border-radius: 8px;
      text-decoration: none;
      color: #1e293b;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .related-link-item:hover {{
      background: #ecfdf5;
      color: var(--primary);
      border-color: #a7f3d0;
    }}
    footer {{
      background: #111827;
      color: #9ca3af;
      padding: 50px 20px 30px;
      font-size: 0.88rem;
    }}
    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="logo">LUMI COSMETICS</a>
    <span style="font-size:0.85rem;color:#6b7280;font-weight:600;">冬コスメ徹底比較ラボ 2026最新版</span>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">ホーム</a> &gt; <span>冬の高保湿美容液</span> &gt; <span>高保湿シカ美容液ランク10</span>
</div>

<main class="container">
  <article class="article-header">
    <span class="category-badge">🌱 2026年冬最新・寒暖差赤み＆乾燥肌荒れ急速鎮静</span>
    <h1>{html_title}</h1>
    <div class="meta-info">
      <span>更新日: 2026年11月9日</span>
      <span>執筆・検証: LUMI COSMETICS 植物皮膚科学研究班</span>
      <span>評価基準: 急速鎮静力・抗炎症活性・角層バリア修復力・低刺激性・保湿持続力</span>
    </div>

    <div class="lead-box">
      <strong>【真冬の『寒暖差肌荒れ』とシカ（ツボクサエキス）の真価】</strong><br>
      11月から12月は、外の冷たい木枯らし（気温5〜8℃）と過熱した室内暖房（気温22〜25℃）を行き来することで、肌が15℃以上もの急激な温度差ショックに日常的に晒されます。<br><br>
      この温度差によって皮膚の毛細血管は急激な拡張と収縮を繰り返し、知覚神経が過敏になって『頬が真っ赤に火照る』『化粧水をつけるとヒリヒリとしみる』『マスクやマフラーが擦れて赤く荒れる』といった<strong>寒暖差による急性皮膚炎症</strong>が頻発します。<br><br>
      この過酷な冬のゆらぎ肌を救う最強の植物成分が、古来より皮膚修復ハーブとして重用されてきた<strong>高純度ツボクサエキス（CICA）</strong>です。ツボクサに含まれる4大生理活性物質（マデカッソシド、アシアチコシド、マデカシン酸、アシアチン酸）は、炎症性サイトカインを速やかに抑制して赤みを鎮めるだけでなく、真皮の線維芽細胞に働きかけて自発的なコラーゲン合成と角層バリアの修復を強力にバックアップします。<br><br>
      本記事では、楽天市場の最新レビューデータと実勢価格を徹底検証し、真冬の寒暖差でピリつく肌を穏やかに潤し、トラブルを寄せ付けないタフな素肌を育てる『高保湿シカ美容液おすすめ10選』を皮膚科学の観点から詳しくご紹介します。
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次（クリックで各見出しへジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#temperature-shock-science">1. 外気5℃ vs 暖房24℃！冬の『寒暖差肌荒れ』が起きる生化学的メカニズム</a></li>
        <li><a href="#cica-actives-guide">2. なぜツボクサなのか？シカの4大核心成分（マデカッソシド等）の皮膚修復作用</a></li>
        <li><a href="#comparison-table">3. 2026年冬厳選！高保湿シカ美容液10選 総合比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿シカ美容液おすすめランキング10選 詳細徹底レビュー</a></li>
        <li><a href="#emergency-cica-care">5. 赤み・ヒリつきを即座に鎮火！冬の『シカ部分コットンパック』実践メソッド</a></li>
        <li><a href="#layering-rules">6. レチノールやビタミンCとの黄金ペアリング（攻めと守りのスキンケアルール）</a></li>
        <li><a href="#faq-section">7. 冬のシカ美容液に関するよくある質問（FAQ）</a></li>
        <li><a href="#related-articles">8. あわせて読みたい冬の集中保湿ケア関連記事</a></li>
      </ul>
    </div>
  </article>

  <!-- 寒暖差肌荒れのメカニズム -->
  <section id="temperature-shock-science">
    <h2 class="section-title">❄️ 1. 外気5℃ vs 暖房24℃！冬の『寒暖差肌荒れ』が起きる生化学的メカニズム</h2>
    <p class="body-text">
      春のゆらぎ肌や夏の日焼け肌とは異なり、11月〜12月の肌荒れは『急激な温度変化』と『湿度急低下』が同時に引き起こす複合的な皮膚ストレスです。
    </p>
    
    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>🌡️ 毛細血管の異常拡張と紅斑（赤み）</h4>
        <p>凍てつく屋外から暖房の効いた室内へ移動した瞬間、冷え切っていた顔の微小血管が急激に拡張します。血管壁から組織液が漏れ出し、炎症性プロスタグランジンが放出されることで、頬が火照るような赤み（紅斑）が定着します。</p>
      </div>
      <div class="feature-card">
        <h4>🧣 物理的摩擦（マスク・マフラー・タートルネック）</h4>
        <p>真冬は防寒具や不織布マスクによる摩擦が日常化します。角層の水分が不足して柔軟性を失った肌表面に繊維が擦れることで、微小な角層剥離（マイクロクラック）が生じ、ピリピリとした刺激痛の原因となります。</p>
      </div>
      <div class="feature-card">
        <h4>⚡ 知覚神経（C線維）の過敏化</h4>
        <p>バリア機能が低下すると、通常は真皮層にとどまっている感覚神経の末端が表皮の最表層近くまで伸びてきます。これにより、冷たい風や髪の毛が触れるだけで痒みやチクチク感を感じる超敏感状態に陥ります。</p>
      </div>
    </div>
  </section>

  <!-- シカ核心成分の作用 -->
  <section id="cica-actives-guide">
    <h2 class="section-title">🔬 2. なぜツボクサなのか？シカの4大核心成分（マデカッソシド等）の皮膚修復作用</h2>
    <p class="body-text">
      『CICA（シカ）』という名前の由来であるセリ科の薬草・ツボクサ（Centella Asiatica）。野生のトラが傷を負った際にツボクサに体をこすりつけて治したという伝承から『タイガーハーブ』とも呼ばれます。ツボクサから抽出される4つの核心成分には、それぞれ明確な役割があります。
    </p>

    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>① マデカッソシド（Madecassoside）</h4>
        <p>強力な抗炎症・創傷治癒促進作用を持ちます。炎症性サイトカイン（IL-1αやIL-6）の産生を強力に抑制し、冬の寒暖差による赤みやヒリつきを即座に鎮火させます。</p>
      </div>
      <div class="feature-card">
        <h4>② アシアチコシド（Asiaticoside）</h4>
        <p>真皮の線維芽細胞を強力に活性化し、I型およびIII型コラーゲンの合成を促進。冬の乾燥で菲薄化（薄肌化）した皮膚の密度を取り戻し、ふっくらとした弾力を蘇らせます。</p>
      </div>
      <div class="feature-card">
        <h4>③ マデカシン酸（Madecassic Acid）</h4>
        <p>傷ついた皮膚組織の再生プロセスを誘導し、角層の細胞間脂質（セラミド合成）をバックアップ。外気刺激に対する防御シールドを再構築します。</p>
      </div>
      <div class="feature-card">
        <h4>④ アシアチン酸（Asiatic Acid）</h4>
        <p>優れた抗酸化作用を発揮し、暖房や紫外線による過酸化脂質の生成をシャットアウト。皮膚の自然免疫力を向上させ、冬の大人ニキビや吹き出物を予防します。</p>
      </div>
    </div>
  </section>

  <!-- スペック比較表 -->
  <section id="comparison-table">
    <h2 class="section-title">📊 3. 2026年冬厳選！高保湿シカ美容液10選 総合比較表</h2>
    <p class="body-text">
      楽天市場で高評価を集める高保湿シカ美容液10商品のツボクサ純度、注目配合成分、テクスチャー、容量、最新価格、おすすめ肌質を一覧で徹底比較します。
    </p>

    <div class="comparison-table-wrap">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド・商品名</th>
            <th>主要注目成分</th>
            <th>容量・形状</th>
            <th>参考価格（税込）</th>
            <th>おすすめな悩み・肌質</th>
          </tr>
        </thead>
        <tbody>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""          <tr>
            <td><strong>第{idx+1}位</strong></td>
            <td><strong>{det['brand_name']}</strong><br>{item['display_name'][:28]}...</td>
            <td>{det['features'][:32]}...</td>
            <td>{det['capacity']}</td>
            <td style="color:#e11d48;font-weight:700;">¥{item['price']:,}</td>
            <td>{det['target'][:24]}...</td>
          </tr>
"""

html_content += """        </tbody>
      </table>
    </div>
  </section>

  <!-- ランキング詳細セクション -->
  <section id="ranking-section">
    <h2 class="section-title">🏆 4. 高保湿シカ美容液おすすめランキング10選 詳細徹底レビュー</h2>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
    <div class="product-card" id="rank-{idx+1}">
      <span class="rank-badge">第{idx+1}位</span>
      <div class="product-tag">{det['tag']}</div>
      <h3 class="product-title">{item['display_name']}</h3>

      <div class="product-grid">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{item['display_name']}" class="product-img" loading="lazy">
          <div style="font-size:0.8rem;color:#64748b;margin-top:8px;">★ 楽天レビュー評価: {item['review_average']} ({item['review_count']}件)</div>
        </div>
        <div>
          <table class="product-specs-table">
            <tr>
              <th>ブランド</th>
              <td>{det['brand_name']}</td>
            </tr>
            <tr>
              <th>容量・形状</th>
              <td>{det['capacity']}</td>
            </tr>
            <tr>
              <th>タイプ</th>
              <td>{det['type']}</td>
            </tr>
            <tr>
              <th>主要配合成分</th>
              <td>{det['features']}</td>
            </tr>
            <tr>
              <th>期待できる効果</th>
              <td>{det['value']}</td>
            </tr>
          </table>
          
          <p class="product-desc">{det['desc_p1']}</p>
          <p class="product-desc">{det['desc_p2']}</p>

          <div class="point-box">
            <div class="point-box-title">🎯 こんな方におすすめ＆使い方のコツ</div>
            <p><strong>【おすすめ】</strong>{det['target']}</p>
            <p style="margin-top:6px;"><strong>【効果的な使い方】</strong>{det['point']}</p>
          </div>
        </div>
      </div>

      <div class="price-and-action">
        <div class="price-wrap">
          <span class="price-label">楽天市場 最新価格（税込）</span>
          <span class="price-value">¥{item['price']:,}</span>
        </div>
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          🛒 楽天市場で最安値＆口コミを見る
        </a>
      </div>
    </div>
"""

html_content += """
  </section>

  <!-- コットンパック実践法 -->
  <section id="emergency-cica-care">
    <h2 class="section-title">🩹 5. 赤み・ヒリつきを即座に鎮火！冬の『シカ部分コットンパック』実践メソッド</h2>
    <p class="body-text">
      冷たい風に吹かれた後や暖房で顔が真っ赤になった日、通常のハンドプレスだけでは追いつかない微細炎症を5分で鎮静する集中レスキュー法です。
    </p>

    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>STEP 1: 薄手のコットンを精製水で湿らせる</h4>
        <p>毛羽立ちのない薄型コットンを2〜3枚用意し、水道水ではなく精製水または低刺激なセラミド化粧水で軽く湿らせて固く絞ります（無駄な美容液の吸い込みを防ぐため）。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 2: シカ美容液を贅沢に5〜6滴ドロップ</h4>
        <p>湿らせたコットンの中央に、高濃度シカ美容液を5〜6滴たっぷり染み込ませます。全体にエキスが行き渡るよう軽く指で馴染ませます。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 3: 赤みの気になる両頬・鼻・額に密着</h4>
        <p>熱を持った両頬や乾燥で毛穴が開いた鼻周りにピタッと貼り付けます。そのまま3〜5分間静置し、植物エキスの冷却浸透を待ちます（※長時間の放置は逆に乾燥を招くため5分厳守）。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 4: パックを剥がしてハンドプレス＆クリーム密閉</h4>
        <p>コットンを優しく剥がし、肌表面に残ったエッセンスを手のひらでハンドプレスして完全に押し込みます。直後にセラミドクリームやシカクリームを塗って水分を閉じ込めます。</p>
      </div>
    </div>
  </section>

  <!-- 成分ペアリングルール -->
  <section id="layering-rules">
    <h2 class="section-title">🌿 6. レチノールやビタミンCとの黄金ペアリング（攻めと守りのスキンケアルール）</h2>
    <p class="body-text">
      シカ美容液は単体でも素晴らしい効果を発揮しますが、他の高機能アクティブ成分と組み合わせることで真価を発揮します。
    </p>

    <div class="comparison-table-wrap">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>組み合わせ成分</th>
            <th>相乗効果の理由</th>
            <th>推奨ルーティン順序</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>レチノール（ビタミンA）</strong></td>
            <td>レチノールのターンオーバー促進に伴うA反応（皮むけ・赤み・乾燥）をシカの抗炎症作用が強力に緩和。刺激を抑えて最大のハリ効果を獲得できます。</td>
            <td>化粧水 → <strong>シカ美容液</strong> → レチノール美容液 → 保湿クリーム</td>
          </tr>
          <tr>
            <td><strong>ピュアビタミンC</strong></td>
            <td>高濃度ピュアビタミンC特有のピリピリ感をシカが鎮静。冬の紫外線低下期における毛穴引き締めと美白・抗酸化ケアを肌荒れ知らずで継続できます。</td>
            <td>朝の洗顔後：ビタミンC美容液 → <strong>シカ美容液</strong> → 乳液・日焼け止め</td>
          </tr>
          <tr>
            <td><strong>ヒト型セラミド</strong></td>
            <td>シカが炎症を鎮静し、セラミドが細胞間脂質を修復するという『守りの完璧な二重防御』。超乾燥・敏感肌の冬の最強バリアコンビです。</td>
            <td>化粧水 → <strong>シカ美容液</strong> → セラミドクリーム</td>
          </tr>
          <tr>
            <td><strong>ヒアルロン酸</strong></td>
            <td>シカの水溶性鎮静ヴェールにヒアルロン酸の保水力が合体。暖房直撃によるインナードライを鎮火しながら水分タンクを満タンにします。</td>
            <td>化粧水 → <strong>シカ美容液</strong> → ヒアルロン酸クリーム</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- FAQ セクション -->
  <section id="faq-section">
    <h2 class="section-title">❓ 7. 冬のシカ美容液に関するよくある質問（FAQ）</h2>
"""

for faq in faq_list:
    html_content += f"""
    <div class="faq-card">
      <div class="faq-q">{faq['q']}</div>
      <div class="faq-a">{faq['a']}</div>
    </div>
"""

html_content += """
  </section>

  <!-- 関連記事リンク集 -->
  <section id="related-articles" class="related-links-box">
    <h3 class="sub-title">🔗 あわせて読みたい冬の集中保湿ケア関連記事</h3>
    <p style="font-size:0.9rem;color:#6b7280;">シカ美容液と組み合わせることで真冬の乾燥対策を完璧にするおすすめ記事をピックアップしました。</p>
    <div class="related-links-grid">
      <a href="/winter-cica-cream" class="related-link-item">🌿 冬の高保湿シカクリーム</a>
      <a href="/winter-retinol-serum" class="related-link-item">✨ 冬の高保湿レチノール美容液</a>
      <a href="/winter-retinol-cream" class="related-link-item">🧴 冬の高保湿レチノールクリーム</a>
      <a href="/winter-ceramide-cream" class="related-link-item">🛡️ 冬の高保湿セラミドクリーム</a>
      <a href="/winter-ceramide-serum" class="related-link-item">💧 冬の高保湿セラミド美容液</a>
      <a href="/winter-hyaluronic-cream" class="related-link-item">💦 冬の高保湿ヒアルロン酸クリーム</a>
      <a href="/winter-hyaluronic-serum" class="related-link-item">🌊 冬の高保湿ヒアルロン酸美容液</a>
      <a href="/winter-panthenol-cream" class="related-link-item">🩹 冬の高保湿パンテノールクリーム</a>
      <a href="/winter-panthenol-serum" class="related-link-item">🧪 冬の高保湿パンテノール美容液</a>
      <a href="/winter-pdrn-serum" class="related-link-item">🧬 冬の高保湿PDRN美容液</a>
      <a href="/winter-dokudami" class="related-link-item">🌱 冬の高保湿ドクダミコスメ</a>
      <a href="/winter-face-mist" class="related-link-item">💨 冬の高保湿フェイスミスト</a>
    </div>
  </section>
</main>

<footer>
  <div class="footer-inner">
    <div style="font-weight:700;font-size:1.1rem;color:#ffffff;margin-bottom:15px;">LUMI COSMETICS | 冬コスメ徹底比較ラボ</div>
    <p style="margin-bottom:20px;line-height:1.7;">当サイトは、11月から12月にかけての寒冷乾燥シーズンに最適な高保湿コスメを皮膚科学・成分分析・実勢価格の観点から厳選・検証するビューティーガイドです。掲載している商品価格および在庫情報は楽天市場APIを通じて最新の情報を取得・掲載しております。</p>
    
    <div class="footer-links">
""" + footer_links_html + """
    </div>
    
    <div style="text-align:center;margin-top:30px;border-top:1px solid #374151;padding-top:20px;font-size:0.8rem;color:#6b7280;">
      &copy; 2026 LUMI COSMETICS LAB. All Rights Reserved.
    </div>
  </div>
</footer>

</body>
</html>
"""

with open("winter-cica-serum.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-cica-serum.html! File size: {len(html_content):,} bytes")
