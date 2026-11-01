import json
import re

with open("fetched_3nov_dec_needle_salt_gloss_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_needle_patch"]["items"]

patch_details = [
    {
        "rank": 1,
        "tag": "🏆 ギネス世界記録認定！ヒアルロン酸微細針が角層深部で溶け出し乾燥小ジワを徹底撃退",
        "catch": "寝ている間に高密度ニードルがじっくり溶解。朝起きて剥がした瞬間に指を押し返すような濃密な弾力感を実感",
        "brand_name": "北の快適工房 (Jコンテンツ)",
        "capacity": "1箱 8枚入り（4回分 / 約1ヶ月分）",
        "type": "目元・口元用高濃度マイクロニードルパッチ",
        "features": "高純度ヒアルロン酸、プラセンタエキス、EGF（ヒト遺伝子組換オリゴペプチド-1）、FGF、レチノール誘導体",
        "value": "世界で最も売れているマイクロニードルパッチとしてギネス認定。エステ級の角層ダイレクト注入ケアを自宅で手軽に実現できる圧倒的信頼度",
        "desc_p1": "11月から12月へと気温と湿度が急落する初冬、乾燥した外気と暖房の効いた室内で最もダメージを受けるのが、皮膚がティッシュ1枚分ほど薄い目元や、会話や笑顔で動く口元のほうれい線エリアです。従来のアイクリームや美容液をいくら重ねても、「肌表面で乾いてしまって角層の奥まで届かない」という深刻なもどかしさを抱えている方に絶対的な答えを提示するのが、北の快適工房の『ヒアロディープパッチ』です。マイクロニードル化粧品として世界売上No.1を記録しギネス世界記録にも認定されている本品は、美容成分そのものを目に見えない極小の針へと結晶化させる最先端技術を採用しています。",
        "desc_p2": "シート1枚あたり数百本もの微細なヒアルロン酸ニードルが整然と並び、就寝前に目元やほうれい線に軽く押し当てて密着させると、角質層のバリアを物理的にすり抜けて美容成分がダイレクトに刺入されます。睡眠中の約5時間をかけて、体温と肌内の水分によって針がゆっくりと溶け出し、純度の高いヒアルロン酸をはじめ、プラセンタエキス、EGF、コラーゲンなどの贅沢なエイジングケア成分が角層深部へと満遍なく拡散。翌朝パッチを剥がした瞬間、乾燥でしぼんでいた目元やほうれい線が内側からパンッと張るような、驚きのふっくら感を体感できます。",
        "target": "目元のちりめんジワやファンデーションのひび割れ落ちに悩む方、ほうれい線の影が気になり始めた方、塗るスキンケアの限界を感じている方",
        "point": "貼る直前に化粧水や乳液の油分が肌表面に残っているとテープの密着力が落ちるため、しっかりハンドプレスで馴染ませてから垂直に押し込むように貼るのがコツです。"
    },
    {
        "rank": 2,
        "tag": "💎 資生堂の美容医療発想！1回分約2,400本の100%ヒアルロン酸ニードルが角層を圧倒的補水",
        "catch": "資生堂が長年培った皮膚科学と精密成型技術が結実。針の密度と純度に一切の妥協がないプレミアムパッチ",
        "brand_name": "NAVISION (ナビジョン / 資生堂)",
        "capacity": "2枚×3包（3回分）",
        "type": "医療機関専売発想プレミアムヒアルロン酸パッチ",
        "features": "高純度100%ヒアルロン酸（防腐剤・界面活性剤・香料・着色料完全無添加）、約2,400本/回",
        "value": "資生堂のクリニック向けブランド発想。添加物を極限まで削ぎ落とし、純粋なヒアルロン酸だけを針に凝縮した最高峰の贅沢ケア",
        "desc_p1": "資生堂の先進美容皮膚科学から生まれた『ナビジョン HA フィルパッチ B』は、美容医療のヒアルロン酸注入発想をホームケアに応用した本格派パッチです。最大の特徴は、2枚（1回分）のパッチに合わせて約2,400本ものニードルが高密度に配列されている点。しかも針の先端形状が独自の山型テーパー形状に設計されており、肌への刺入性が極めて高く、角層深部へ確実に潤いを送り届ける設計が徹底されています。",
        "desc_p2": "成分は驚くべきことに『純度100%のヒアルロン酸』のみ。防腐剤や香料、着色料、界面活性剤などを一切含まないため、冬の極度の乾燥でバリア機能が低下し、刺激に敏感になっている肌でも安心して使用できます。貼った瞬間にチクッとした心地よい手応えがあり、針が角層にしっかり到達したことを実感。一晩じっくりと溶け出したヒアルロン酸が角層の水分保持力を劇的に底上げし、暖房直撃のオフィスに一日中いても目元が乾かない圧倒的な保水シールドを築きます。",
        "target": "成分の純度と安全性を最優先したい敏感肌の方、美容皮膚科での施術前後や特別なイベント前のスペシャル集中ケアを求める方",
        "point": "シートの中央部分（針があるエリア）には絶対に指を触れず、外側の透明フィルムを持って狙った位置に配置し、真上からグッと1回だけ押し込むのが美肌への近道です。"
    },
    {
        "rank": 3,
        "tag": "🔬 ニードル技術のパイオニアが開発！立体ピラミッド針×レチノール誘導体で異次元のハリ感",
        "catch": "製薬会社が特許製法で削り出したマイクロニードル。乾燥小ジワを物理的に押し広げながらハリ成分を深層チャージ",
        "brand_name": "Quanis (クオニス / コスメディ製薬)",
        "capacity": "4回分（8枚入り）",
        "type": "製薬会社開発エイジング特化型ニードルパッチ",
        "features": "持続型ヒアルロン酸、レチノール誘導体、ビタミンC誘導体、エクトイン、高分子コラーゲン",
        "value": "世界で初めて水溶性マイクロニードルを実用化したコスメディ製薬のフラッグシップ。確かなエビデンスに基づく濃密なリフトケア",
        "desc_p1": "水溶性マイクロニードル技術を世界で初めて化粧品として実用化したパイオニア企業、コスメディ製薬が手掛ける自社ブランド『クオニス ダーマフィラー プレミア』。数あるニードルパッチの中でも群を抜く技術力を誇り、針の形状を微細なピラミッド型に加工することで、肌への負担を最小限に抑えつつ角層深部への浸透効率を極限まで高めています。",
        "desc_p2": "本品はヒアルロン酸単体にとどまらず、冬の肌にしなやかなハリを与えるレチノール誘導体、抗酸化をサポートするビタミンC誘導体、過酷な砂漠環境でも水分を抱え込む保水成分エクトインを贅沢にブレンドしてニードル化しています。就寝中に針が角層内でじっくり溶解すると同時に、乾燥によって硬く折りたたまれた皮膚組織をふっくらと再構築。朝起きてパッチを剥がした瞬間、指先が吸い付くようなモチモチ感とピンとしたハリを肌表面に呼び戻します。",
        "target": "乾燥だけでなく年齢とともに深くなる眉間や目尻の刻まれサインに悩む方、製薬会社のエビデンスに基づいた確かな品質を選びたい方",
        "point": "週に1〜2回の定期的なスペシャルケアとして継続することで、角層深部の水分貯水タンクが満たされ、冬の間中乾燥知らずの肌コンディションが定着します。"
    },
    {
        "rank": 4,
        "tag": "🌿 大人気リードルショット発想！CICA×ヒアルロン酸が冬の乾燥ゆらぎと気になる凹凸を鎮静ケア",
        "catch": "SNSで大旋風を巻き起こすVTのニードル技術がパッチに凝縮。乾燥による肌荒れを防ぎながら角層深部を集中保水",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "1箱（パッチ複数枚入り）",
        "type": "鎮静＆マイクロニードル集中ポイントパッチ",
        "features": "CICA（ツボクサエキス、アシアチコシド、マデカッソシド）、ヒアルロン酸Na、ティーツリー葉油、プロポリスエキス",
        "value": "大ヒット美容液『リードルショット』の浸透理論をパッチへ昇華。乾燥と肌トラブルが同時に起きやすい冬のゆらぎ肌に最適な名品",
        "desc_p1": "美容業界にマイクロニードルブームを巻き起こしたVT COSMETICSの『リードルS マイクロパッチ』は、冬特有の複雑な肌悩みに応える新世代パッチです。11月・12月は、外気の急激な乾燥に加えて、暖房による皮脂の酸化やマスク・マフラーの摩擦によって、目元や頬、口周りに突発的な乾燥荒れや赤み、ポツポツとした肌トラブルが頻発します。",
        "desc_p2": "VT独自のツボクサ由来成分（CICAコンプレックス）とヒアルロン酸を微小ニードルに凝縮。トラブルが気になる局所ポイントにピタッと貼ることで、角層深部へ鎮静成分と潤いを直接送り届けて炎症を鎮めつつ、乾いてゴワついた角質を柔らかくほぐします。パッチ自体が薄く目立ちにくい設計のため、日中のテレワーク中やリラックスタイムにも違和感なく使用可能。冬の乾燥と肌荒れの悪循環を断ち切る心強いレスキューアイテムです。",
        "target": "冬の乾燥と同時に大人ニキビや赤みトラブルに悩まされやすい方、手軽にCICAニードルの実力を試してみたい方",
        "point": "気になる部分を清潔に洗顔し化粧水で水分を補給した直後、油分のあるクリームを塗る前に貼ることで、パッチの密着度と成分の浸透力を最大化できます。"
    },
    {
        "rank": 5,
        "tag": "🌸 ドラッグストアで買える高コスパ神パッチ！1,500本のヒアルロン酸針が翌朝の目元をふっくらリペア",
        "catch": "千円台で手に入る圧倒的アクセスの良さ。大判シートで目元からゴルゴ線まで広範囲を丸ごと包み込む実力派",
        "brand_name": "CLEAR TURN (クリアターン / コーセー)",
        "capacity": "1回分（2枚入り）",
        "type": "デイリー集中高保湿マイクロパッチ",
        "features": "100%ヒアルロン酸（微細針1,500本/回）、無香料、無着色、アルコールフリー、弱酸性",
        "value": "全国のドラッグストアでいつでも手軽に入手可能。マイクロニードル初心者でも気負わず試せる驚きのコストパフォーマンス",
        "desc_p1": "「マイクロニードルパッチを使ってみたいけれど、1回数千円もするデパコスや通販限定品は敷居が高い…」という方に朗報となるのが、コーセーの『クリアターン ヒアロチューン マイクロパッチ』です。身近なドラッグストアで1回分から購入できる手軽さでありながら、1回分あたり約1,500本もの100%ヒアルロン酸ニードルを搭載した本格派スペックを誇ります。",
        "desc_p2": "シートの形状が日本人の骨格に合わせてやや大きめの三日月型にカットされており、乾燥小ジワが気になる目尻から下まぶた、さらにはゴルゴラインの手前まで広範囲を一気にカバーできるのが大きな強みです。一晩貼って眠るだけで、寝息や寝返りによる乾燥から目元を完全シールドし、翌朝剥がしたときには内側から水分が湧き出たようなみずみずしいハリを実感。週末の気軽なご褒美ケアとしてリピーターが続出しています。",
        "target": "マイクロニードルパッチを初めて試す入門者の方、ドラッグストアで手軽に購入したい方、広範囲の目元乾燥をケアしたい方",
        "point": "貼った直後に指の腹でトントンと優しく数回押さえてあげると、ニードルが角層にしっかり刺さり、朝まで剥がれずに安定します。"
    },
    {
        "rank": 6,
        "tag": "🩺 皮膚科学発想のドクターズコスメ！濃密ヒアルロン酸ニードルが冬の刻まれ溝を物理的に押し上げる",
        "catch": "クリニック品質を追求するドクターフィルの真骨頂。乾き切った大人肌の角層に深く刺さり濃密に広がる",
        "brand_name": "Dr.PHIL COSMETICS (ドクターフィル / コーセー)",
        "capacity": "2枚入（1回分）",
        "type": "皮膚科学発想ドクターズマイクロパッチ",
        "features": "高分子ヒアルロン酸（100%純粋ニードル）、パラベンフリー、鉱物油フリー、アレルギーテスト済み",
        "value": "皮膚の専門家が開発に携わる高機能処方。冬の極度な乾燥で硬化した角層を確実にほぐしてハリを復活させる信頼の1枚",
        "desc_p1": "コーセーグループのドクターズコスメブランドとして、皮膚科学に基づいた低刺激・高機能ケアを提供するドクターフィル コスメティクスの『IC.U HA マイクロパッチ EX』。冬の乾燥と加齢によって皮膚のコラーゲン構造が緩み、表情の動きとともに深い影として刻まれてしまう目元や口元の溝にダイレクトにアプローチします。",
        "desc_p2": "針の根元から先端までヒアルロン酸の分子構造を壊さずに結晶化させる特殊技術を用いており、角層内に刺入された後にゆっくりと水分を引き寄せながら膨潤。角層深部でスポンジのように水分を抱え込み、萎縮した角質細胞を内側からムクムクと押し広げるように整えます。敏感になりがちな大人の肌を考慮した低刺激設計で、剥がした後の赤みやテープかぶれが起きにくい点も皮膚科学発想ならではの強みです。",
        "target": "敏感肌で市販のテープパッチで赤みやかぶれが出やすい方、乾燥による深い溝や表情ジワを本格的にケアしたい方",
        "point": "就寝前に貼った後、そのまま6時間以上置くことでニードルが完全に溶解し、剥がす際に角質を傷めずスルリと除去できます。"
    },
    {
        "rank": 7,
        "tag": "✨ 炭酸美容のパイオニアが放つ集中パッチ！ヒアルロン酸×複合ペプチド針でキュッと引き締める",
        "catch": "クリニック生まれのドクターメディオンが放つ最先端アプローチ。針が溶けた後の肌密度の高さに感動",
        "brand_name": "Dr.MEDION (ドクターメディオン)",
        "capacity": "目元・口元用集中パッチセット",
        "type": "炭酸美容発想エイジングリペアパッチ",
        "features": "高密度ヒアルロン酸、アセチルヘキサペプチド-8、パルミトイルトリペプチド-5、水溶性プロテオグリカン",
        "value": "炭酸パックの名手が生み出した贅沢パッチ。ヒアルロン酸の保湿力とペプチドの引き締め効果が同時に得られるハイエンド仕様",
        "desc_p1": "炭酸パックの生みの親として美容界に名を馳せる日置正人博士がプロデュースする『ドクターメディオン スパオキシ ニードルパッチ』。炭酸美容で血行を促した後のような巡りの良いハリ肌を目指し、ヒアルロン酸の微小針の中に表情ジワにアプローチする複合ペプチド（アルジルリン等）とプロテオグリカンを高濃度に封入しています。",
        "desc_p2": "冬の寒さで血行が悪くなり、青クマや乾燥くすみが目立つ目元に貼ることで、就寝中に美容成分が角層奥深くへ浸透。ヒアルロン酸が水分を抱え込みながら、ペプチドが緩んだ目元やほうれい線の肌を引き締めるようにサポートします。翌朝剥がした瞬間、まるでエステで極上トリートメントを受けたかのような、ピンと引き上がったすっきりとした目元印象へと導きます。",
        "target": "目元の乾燥だけでなくたるみや重たさ、フェイスラインのゆるみが気になる方、ラグジュアリーなエイジングケアを好む方",
        "point": "夜のスキンケアでドクターメディオンの炭酸パックを使用した後の肌にこのニードルパッチを重ねると、相乗効果で驚異的なハリとツヤが生まれます。"
    },
    {
        "rank": 8,
        "tag": "🇰🇷 韓国発の実力派ニードルパッチ！加水分解ヒアルロン酸×マデカッソシドで冬の乾燥目元がぷるぷるに",
        "catch": "韓国美容の最先端技術をお手頃価格で実感。吸い付くような密着ジェルテープが寝返りの摩擦から目元を守る",
        "brand_name": "THE CURE (ザ・キュア)",
        "capacity": "1回分（2枚入り）",
        "type": "韓国コスメ高保水マイクロアイパッチ",
        "features": "低分子加水分解ヒアルロン酸、マデカッソシド、コラーゲンエキス、アデノシン",
        "value": "韓国オリーブヤングや現地クリニックでも評価される実力派。低分子ヒアルロン酸の浸透スピードとコスパのバランスが優秀",
        "desc_p1": "美容大国・韓国で絶大な支持を集めるマイクロニードルブランド、THE CUREの『マイクロアイパッチ』。分子量の小さい加水分解ヒアルロン酸を採用することで、角層内での溶解スピードと水分浸透率を大幅に向上させた、乾燥肌のためのレスキューアイテムです。",
        "desc_p2": "肌荒れ防止成分であるマデカッソシドと、韓国機能性化粧品の代表格である抗シワ成分アデノシンを配合。冬の冷たい木枯らしにさらされてカサつき、赤みを帯びたデリケートな目元を優しくいたわりながら、たっぷりの水分で満たします。テープ部分に医療用ハイドロコロイド素材が使われており、寝返りを打っても剥がれにくく、就寝中の枕との摩擦ダメージから目元の皮膚を物理的に保護してくれるのも嬉しい設計です。",
        "target": "韓国スキンケアの即効性を好む方、寝返りが多く通常のアイパッチだと朝起きると剥がれてしまう方",
        "point": "目元だけでなく、冬の乾燥でファンデーションが溜まりやすい眉間やおでこの横ジワ部分へのポイント使いにも抜群の効果を発揮します。"
    },
    {
        "rank": 9,
        "tag": "🔬 独自特許の超微細構造体技術！ヒアルロン酸とEGFがほうれい線ゾーンへダイレクトに届く実力派",
        "catch": "皮膚内部に溶ける極小ニードルで特許を取得。ほうれい線のカーブにぴったり沿う専用設計シートが秀逸",
        "brand_name": "ACROPASS (アクロパス)",
        "capacity": "4回分（8枚入り）",
        "type": "ほうれい線・口元専用立体ニードルパッチ",
        "features": "高純度ヒアルロン酸、EGF（上皮成長因子）、アスコルビルグルコシド、独自特許DAB成型ニードル",
        "value": "マイクロ構造体の特許技術を持つアクロパスの看板製品。ほうれい線の形状に特化したカーブ設計で口元の緩みに集中アタック",
        "desc_p1": "世界各国でマイクロニードルの製造特許を保持するラパス社が手掛けるグローバルブランド『アクロパス エイジレスリフター スマイリーパッチ』。本品は特に、冬の乾燥によってファンデーションが深くめり込みやすい「ほうれい線（口元エリア）」に特化して開発された専用設計パッチです。",
        "desc_p2": "口元の筋肉の動きに沿うように計算された三日月カーブのシートに、ヒアルロン酸と上皮成長因子EGFを結晶化した微小ニードルを等間隔に配置。独自技術「DAB製法」により、熱を加えず成分の活性を保ったままニードルを成型しているため、美容成分のフレッシュさが保たれています。乾燥で硬くなった口元の皮膚を深部からほぐし、翌朝パッチを剥がすと笑ってもファンデが割れないなめらかな口元へと導きます。",
        "target": "口元のほうれい線の影が気になって思い切り笑えない方、乾燥によるファンデの溝落ちを予防したい方",
        "point": "貼る際は、口角を少し斜め上に引き上げながらパッチを密着させると、リフトアップした状態を記憶させるように綺麗にフィットします。"
    },
    {
        "rank": 10,
        "tag": "🌿 高純度プロテオグリカン×ヒアルロン酸！極小ニードルが冬の刻まれ溝に吸い付きふっくら満たす",
        "catch": "ヒアルロン酸を超える保水力を持つプロテオグリカンを針状結晶化。年齢肌の深刻な乾きを寝ている間に集中リペア",
        "brand_name": "Harith (ハーリス)",
        "capacity": "2枚×2袋（2回分）",
        "type": "プロテオグリカン配合高機能マイクロパッチ",
        "features": "水溶性プロテオグリカン、高分子ヒアルロン酸、プラセンタ、セラミドNP、水溶性コラーゲン",
        "value": "ヒアルロン酸の1.3倍の保水力を誇るプロテオグリカンをニードル技術と融合。大人の冬の頑固な乾燥ジワに立ち向かう贅沢処方",
        "desc_p1": "高機能エイジングケアブランドとして熱い支持を集めるハーリスの『モイスト パッチ』は、ヒアルロン酸を凌駕する保水力とEGF様作用を持つことで知られる高級美容成分「プロテオグリカン」を贅沢にニードル化した意欲作です。11月・12月の冬、通常の保湿ケアでは追いつかないほど乾き切った大人肌の角層にアプローチします。",
        "desc_p2": "微小な結晶針の中にプロテオグリカン、ヒアルロン酸、セラミド、プラセンタを凝縮。就寝中の肌温と水分によってニードルが溶け出すと同時に、水分をギュッと抱え込んで逃さないプロテオグリカンの濃密な保水ネットワークが角層内に形成されます。朝起きてパッチを剥がした後の肌は、ふっくらと内側から押し上げられたような弾力と、シルクのようになめらかな手触りを実現。乾燥小ジワを忘れさせてくれる完成度の高いアイテムです。",
        "target": "これまでのヒアルロン酸パッチでは物足りなさを感じていた方、プロテオグリカンの高い保水・ハリ効果を実感したい方",
        "point": "パッチを貼った翌朝は、ぬるま湯で優しく洗顔した後にセラミド配合の乳液やクリームで蓋をしてあげると、注入した潤いが一日中キープされます。"
    }
]

# 比較表データ生成
table_rows = []
for p, item in zip(patch_details, items):
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
for p, item in zip(patch_details, items):
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
            <div class="meta-item"><span class="meta-label">カテゴリ：</span><span class="meta-value">{p['type']}</span></div>
            <div class="meta-item"><span class="meta-label">主要成分：</span><span class="meta-value">{p['features']}</span></div>
            <div class="meta-item"><span class="meta-label">取扱店舗：</span><span class="meta-value">{item['shop_name']}</span></div>
          </div>
          <div class="product-points">
            <h4>💡 ここが冬の乾燥小ジワに効く注目ポイント！</h4>
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
          <strong>✨ プロの使いこなしアドバイス：</strong>
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
        "q": "マイクロニードルパッチは貼る時にチクチクした痛みがありますか？",
        "a": "貼った直後に指で軽く上から押さえた際、ほんの少しチクッとした心地よい刺激を感じることがありますが、強い痛みや出血を伴うことは一切ありません。針の長さは数百マイクロメートル（0.2mm〜0.3mm前後）と非常に微小で、皮膚の神経が密集する真皮までは到達せず、角質層の範囲内に留まるように精密設計されています。数分〜数十分経つと体温と水分で針が徐々に溶解し、刺激感は自然に消失しますのでご安心ください。"
    },
    {
        "q": "金属アレルギーがありますが、マイクロニードルパッチを使っても大丈夫ですか？",
        "a": "全く問題ありません。マイクロニードルパッチの「針」は金属やプラスチックではなく、純粋な『ヒアルロン酸』や『コラーゲン』などの美容成分そのものを水分を抜いて微細な針状に乾燥・結晶化させたものです。肌に刺さると体内の水分に溶けて美容液へと戻るため、金属アレルギーの方でも安心してご使用いただけます。"
    },
    {
        "q": "使う頻度はどのくらいがベストですか？毎晩使ってもいいのでしょうか？",
        "a": "基本的には「週に1〜2回」のスペシャルケアとしての使用が最も推奨されます。マイクロニードルによって角層深部に注入されたヒアルロン酸は数日間かけて水分を抱え込み続けるため、週に1〜2回のペースでも十分にふっくらとしたハリを維持できます。乾燥が特に深刻な時期や大事なイベントの前には、最初の2週間だけ3日おきに使用し、肌状態が上向いたら週1回のメンテナンスに切り替える集中アプローチも効果的です。"
    },
    {
        "q": "貼る前に普段のスキンケア（化粧水やクリーム）はどう塗ればいいですか？",
        "a": "化粧水や乳液で肌を十分に保湿した後に使用するのが基本ですが、最も重要なのは「貼る直前のパッチ貼付部分に油分や水分を過剰に残さないこと」です。クリームやオイルが肌表面にベタベタ残っていると、パッチの粘着テープが密着せず睡眠中に剥がれてしまいます。化粧水をしっかりハンドプレスで馴染ませ、貼る部分だけティッシュオフしてサラッとした状態にしてから垂直に貼り、パッチを貼った後にパッチの外側エリアへクリームを塗布するのが最も剥がれにくいプロの塗り方です。"
    },
    {
        "q": "朝起きてパッチを剥がすときに痛かったり肌を傷めたりしませんか？",
        "a": "5〜6時間以上の睡眠時間を確保していれば、ニードルは角層深部ですでに完全に溶解して液状化しているため、針による痛みは全くありません。粘着テープを剥がす際は、端から急に引っ張るのではなく、肌を手で軽く押さえながらゆっくり優しく剥がしてください。もし肌表面にわずかに溶け残ったヒアルロン酸のゲルが付着している場合は、擦らずに朝の洗顔時にぬるま湯で優しく洗い流せば綺麗に落ちます。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(patch_details, items):
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
    "headline": "保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10",
    "description": "11月・12月の冬の凍える冷気とエアコン暖房で深く刻まれる目元・口元の乾燥小ジワ・ほうれい線を徹底解決！北の快適工房、資生堂ナビジョン、クオニス、VT CICA、コーセークリアターン、ドクターフィルなど、寝ている間にヒアルロン酸針が角層深部へダイレクト注入する最強高保湿マイクロニードルパッチ10選を徹底比較！",
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
            "name": "高保湿マイクロニードルパッチ特集",
            "item": "https://lumi-cosme.vercel.app/winter-needle-patch"
        }
    ]
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の高保湿マイクロニードルパッチおすすめ人気ランキング10選",
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
  <title>保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の凍える冷気とエアコン暖房で深く刻まれる目元・口元の乾燥小ジワ・ほうれい線を徹底解決！北の快適工房、資生堂ナビジョン、クオニス、VT CICA、コーセークリアターン、ドクターフィルなど、寝ている間にヒアルロン酸針が角層深部へダイレクト注入する最強高保湿マイクロニードルパッチ10選を徹底比較！">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-needle-patch">
  <link rel="icon" href="/favicon.jpg">
  <link rel="stylesheet" href="style.css">

  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10">
  <meta property="og:description" content="11月・12月の冬の凍える冷気とエアコン暖房で深く刻まれる目元・口元の乾燥小ジワ・ほうれい線を徹底解決！寝ている間にヒアルロン酸針が角層深部へダイレクト注入する最強高保湿マイクロニードルパッチ10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-needle-patch">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！高保湿マイクロニードルパッチランク10">
  <meta name="twitter:description" content="11月・12月の冬の目元・ほうれい線の乾燥小ジワを寝ている間に集中リセット！最強高保湿マイクロニードルパッチ10選を本音レビュー！">
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
      --primary: #c026d3;
      --primary-dark: #a21caf;
      --primary-light: #fdf4ff;
      --accent: #d946ef;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #fafaf9;
      --card-bg: #ffffff;
      --border: #f1f5f9;
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
      border: 1px solid #e2e8f0;
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
      border: 1px solid #e2e8f0;
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
      border: 1px solid #e2e8f0;
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
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
    }}
    .comparison-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #334155;
      white-space: nowrap;
    }}
    .comparison-table tr:hover {{
      background-color: #fdf4ff;
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
      border: 1px solid #e2e8f0;
      position: relative;
      margin-bottom: 40px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
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
      box-shadow: 0 4px 10px rgba(192, 38, 211, 0.3);
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
      background: #f8fafc;
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
      border: 1px solid #e2e8f0;
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
      background: #fdf4ff;
      border: 1px solid #f5d0fe;
      color: #86198f;
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
      background: #f8fafc;
      border: 1px solid #e2e8f0;
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
      <a href="/winter-needle-patch">高保湿マイクロニードルパッチ特集</a>
    </nav>
  </div>

  <main class="container">
    <article class="article-body">
      <header class="article-header">
        <div class="article-tag-wrap">
          <span class="badge">冬の乾燥小ジワ集中救済</span>
          <span class="badge">マイクロニードルDDS浸透</span>
          <span class="badge">2026年最新徹底検証</span>
        </div>
        <h1 class="article-title">保湿力の強さで冬の目元・ほうれい線乾燥小ジワとさようなら！寝ている間にヒアルロン酸針が角層深部へ直接届く高保湿マイクロニードルパッチランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-02">2026年11月2日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入部 -->
      <section class="intro-box">
        <p>
          11月から12月へと向かい、冬の寒風が吹き始める季節。ふとオフィスの鏡や電車の窓に映った自分の顔を見て、<strong>「目元にファンデーションがひび割れるようにめり込んでいる」「笑ったあとのほうれい線の影が戻らない」「夕方になると目尻がカサついてちりめんジワが目立つ」</strong>とハッとした経験はありませんか。
        </p>
        <p>
          冬の目元や口元の皮膚は、人体の中でも最も過酷な環境に晒されています。特に目元の皮膚はわずか0.02mmと卵の薄皮ほどの厚さしかなく、皮脂腺がほとんど存在しないため、湿度が急降下する11月以降は一瞬で水分が蒸発してしまいます。さらに室内ではエアコン暖房の温風が直撃し、角質細胞同士を接着する細胞間脂質（セラミド）が破壊され、柔軟性を失った皮膚が折り紙のようにシワを刻んでしまうのです。
        </p>
        <p>
          ここで多くの方が高級アイクリームやシートマスクを重ねて塗りたくりますが、実は「塗るだけ」のケアには限界があります。私たちの肌表面には外部刺激から体を守る強固な「角層バリア」が存在するため、分子量の大きいヒアルロン酸やコラーゲンは肌の奥深くへ浸透できず、肌表面を覆うだけで終わってしまいがちです。
        </p>
        <p>
          この肌の壁を科学的に打破し、美容医療の注入発想をホームケアで実現したのが<strong>「高保湿マイクロニードルパッチ」</strong>です。純度の高いヒアルロン酸そのものを目に見えない極小の針へと結晶化させ、就寝前に肌へ押し当てることで、角層バリアを物理的に通り抜けて深部へ直接美容成分を届けます。寝ている間に針がゆっくりと溶け出し、翌朝剥がした瞬間には内側から水分が湧き出たような吸い付くハリと弾力を体感できます。本記事では、11月・12月の冬に本当に買うべき実力派マイクロニードルパッチ10選を徹底比較し、ランキング形式で詳しくご紹介します。
        </p>
      </section>

      <!-- 特集セクション：なぜ冬の小ジワには「刺すヒアルロン酸」なのか -->
      <section class="guide-box" id="guide-section">
        <h2>なぜ冬の乾燥小ジワには「塗る」より「刺す」ヒアルロン酸なのか？3つの浸透メカニズム</h2>
        <div class="guide-item">
          <h3>1. 角層バリアの「500ダルトンの壁」を物理的に突破するDDS技術</h3>
          <p>
            皮膚科学において、外用薬や化粧品成分が角層を通過できる分子量には「500ダルトン（分子量の単位）の限界」があるとされています。しかし、肌の保水力を支える高分子ヒアルロン酸の分子量は数十万〜数百万ダルトンにも達するため、通常は角層表面に留まることしかできません。マイクロニードル技術は、ヒアルロン酸そのものを微細な針に成型して角質層へ直接差し込むため、分子量の壁を軽々とクリアし、目的の深度へ100%の成分を届けるドラッグデリバリーシステム（DDS）を成立させています。
          </p>
        </div>
        <div class="guide-item">
          <h3>2. 睡眠中の6〜8時間をかけた「徐放型（じょほうがた）溶解」で朝まで保水持続</h3>
          <p>
            通常のシートマスクは15分ほどで剥がさなければ逆に水分が奪われてしまいますが、マイクロニードルパッチは就寝中ずっと肌に貼ったまま過ごせます。体温と角層内のわずかな水分に反応し、針が数時間かけてじんわりと均一に溶け出していくため、角層細胞の隙間が隙間なく潤いで満たされ、翌朝まで一切乾かない濃密な保湿環境がキープされます。
          </p>
        </div>
        <div class="guide-item">
          <h3>3. 針による心地よい物理的アプローチが肌の巡りと弾力呼び覚ましをサポート</h3>
          <p>
            微小なニードルが皮膚に接触することで、微細な刺激が伝わり、寒さで滞りがちな目元や口元の巡りを優しくサポートします。美容成分の化学的な保水作用と、ニードルによる物理的なアプローチが融合することで、冬の寒冷でこわばった皮膚組織がしなやかさを取り戻します。
          </p>
        </div>
      </section>

      <!-- 選び方ガイド -->
      <section class="guide-box">
        <h2>失敗しない！冬用マイクロニードルパッチの賢い選び方3つの基準</h2>
        <div class="guide-item">
          <h3>① 針の密度と本数（1回分あたり1,000本以上を目安に）</h3>
          <p>
            マイクロニードルの効果を左右する第一の要素は「針の密度」です。針の本数が少なすぎると成分の注入ポイントがまばらになり、十分なふっくら感を得られません。1回分（左右2枚）で1,000本〜2,000本以上の高密度設計を採用しているアイテムを選ぶと、乾燥小ジワの隙間を余すところなく埋め尽くすことができます。
          </p>
        </div>
        <div class="guide-item">
          <h3>② ヒアルロン酸以外の「プラスα配合成分」（レチノール・EGF・ペプチド）</h3>
          <p>
            真冬の肌悩みは乾燥だけでなく、ハリ不足や刻まれた表情ジワの定着も絡み合っています。純粋なヒアルロン酸だけでなく、肌のターンオーバーを促すレチノール誘導体、細胞活性を助けるEGF（上皮成長因子）、表情ジワをほぐすペプチド（アルジルリンなど）、高い保水力を誇るプロテオグリカンなどがニードル内に一緒に結晶化されている製品を選ぶと、エイジングケア効果が飛躍的に高まります。
          </p>
        </div>
        <div class="guide-item">
          <h3>③ 粘着テープの低刺激性と形状密着力（ハイドロコロイド素材・目元専用カット）</h3>
          <p>
            パッチは一晩中肌に貼り続けるため、テープ部分の素材選びも極めて重要です。医療用ハイドロコロイドや低刺激粘着剤を採用しているものを選べば、剥がす際の摩擦ダメージや赤みトラブルを防げます。また、目尻のカーブやほうれい線の傾斜に立体的に沿う形状にカッティングされているかどうかも、就寝中の剥がれを防ぐ決定打となります。
          </p>
        </div>
      </section>

      <!-- 徹底比較表 -->
      <section id="comparison" class="comparison-section">
        <h2>【徹底比較】冬の目元・ほうれい線を満たす高保湿マイクロニードルパッチスペック比較表</h2>
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
        <h2>【2026年最新】11月・12月に買うべき高保湿マイクロニードルパッチランキング10選</h2>
        {"".join(product_cards_html)}
      </section>

      <!-- 実践テクニック -->
      <section class="guide-box">
        <h2>効果を最大化！マイクロニードルパッチ「失敗しない貼り方＆夜の美肌ルーティン」</h2>
        <div class="guide-item">
          <h3>ステップ1：スキンケアの油分をティッシュオフして土台を整える</h3>
          <p>
            化粧水や美容液をしっかり肌に馴染ませた後、パッチを貼る目元や口元のエリアだけティッシュで優しく押さえて表面の余分な水分・油分を取り除きます。油分が残っていると粘着テープが浮き、睡眠中に剥がれてしまう最大の原因になります。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ2：中央の針には触れず、真上から「垂直プレス」で押し込む</h3>
          <p>
            ケースからパッチを取り出す際、中央のニードル部分には絶対に指を触れないように注意しましょう。狙った小ジワやほうれい線の上に配置したら、横に滑らせたり擦ったりせず、真上から指の腹でグッと垂直に1〜2回強く押し当てます。この垂直プレスによって針が角層にしっかり刺入されます。
          </p>
        </div>
        <div class="guide-item">
          <h3>ステップ3：外側エリアにクリームを重ね、朝は優しくぬるま湯オフ</h3>
          <p>
            パッチを貼り終えたら、パッチを避けた顔の他のエリアに乳液や高保湿クリームを塗って全体のスキンケアを完了させます。翌朝は無理に一気に剥がさず、端からゆっくり剥がした後、肌表面に残った微細なゲルをぬるま湯で洗い流しましょう。
          </p>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq-section" class="faq-section">
        <h2>よくある質問（FAQ）：高保湿マイクロニードルパッチの疑問を徹底解決</h2>
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
        <h2>まとめ：冬の乾燥小ジワは「角層ダイレクト注入」でスマートに解決しよう</h2>
        <p>
          11月から12月にかけての寒風と暖房乾燥は、私たちが思っている以上に目元や口元の水分を容赦なく奪い去ります。従来のスキンケアをいくら念入りに塗り重ねても「夕方になると小ジワが目立つ」「ファンデーションが割れてしまう」と感じていたなら、それは成分が角層バリアの手前で止まっていた証拠かもしれません。
        </p>
        <p>
          美容医療発想のマイクロニードルパッチを取り入れれば、寝ている間のリラックスタイムがそのまま最高峰のエステ注入時間へと早変わりします。翌朝起きて鏡を見たときの、ふっくらと押し返してくるような目元と口元のハリ感をぜひ実感し、真冬の寒さや暖房直撃に負けない自信に満ちた美肌でホリデーシーズンを過ごしてください。
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

with open("winter-needle-patch.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✓ Created winter-needle-patch.html successfully!")
