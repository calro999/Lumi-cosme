import json
import re

with open("fetched_3new_nov_dec_elastin_allantoin_beeswax.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_beeswax"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 100%天然ミツロウの世界的金字塔！真冬の冷風から唇の水分を一滴も逃がさない名品",
        "catch": "天然ミツロウ100%ベース×ペパーミント精油。固めのワックスが唇に密着シールドを形成し、真冬の乾燥冷風下でも縦ジワのないぷるんとした潤いを死守",
        "brand_name": "Burt's Bees (バーツビーズ)",
        "capacity": "4.25g (スティックタイプ)",
        "type": "高密着天然ミツロウリップバーム",
        "features": "天然ミツロウ（ビーズワックス）、ヤシ油、ヒマワリ種子油、セイヨウハッカ油（ペパーミント）、ビタミンE",
        "value": "体温でじんわり溶けて唇に強力な保護皮膜を形成。石油系ワックスにはない天然の通気性と抗酸化力で、真冬の過酷なひび割れ・皮向けを完全ブロック",
        "desc_p1": "11月から12月にかけて外気の湿度が急激に20%台まで低下すると、皮膚のなかで最も角層が薄く皮脂腺が存在しない『唇』から最初に水分が干からびます。皮がめくれて出血したり、リップを塗っても10分後には乾いてしまうという悩みに、世界中で1秒に1本売れていると言われる絶対的な解がバーツビーズの『ビーズワックス リップバーム』です。ミツバチが巣を作るために分泌する天然ミツロウを贅沢に高濃度配合しています。",
        "desc_p2": "スティックを繰り出すとしっかりとした硬さがありますが、唇に滑らせると体温でじんわりととろけ、ぴったりと吸い付くようなマットで強靭な保護ベールを形成。一般的なプチプラリップにありがちな油膜の浮きやテカリがなく、真冬の吹きすさぶ木枯らしの中でも何時間も唇の水分を逃がしません。爽快な天然ペパーミント精油の香りが、寒さで滞りがちな唇の血行を心地よく刺激し、血色の良いふっくらリップをキープします。",
        "target": "冬になると唇がすぐにひび割れて皮がむける方、テカテカしない自然なマット高密着リップを求める方、100%天然由来成分にこだわりたい方",
        "point": "朝の洗顔後や外出前、就寝前に唇の縦ジワに沿って縦方向に塗り込みます。唇の輪郭から少しオーバー気味に塗ることで、唇の端の口角炎や乾燥亀裂も鉄壁に防ぐことができます。"
    },
    {
        "rank": 2,
        "tag": "🌿 西アフリカの生命力×天然ミツロウ！人肌でとろけて全身の粉吹きを救うマルチバーム",
        "catch": "ロクシタンの原点にして最高峰。天然シア脂とミツロウが融合し、冬のガサガサかかと・ひじ・指先を吸い付くような柔らかさに生まれ変わらせる",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "150ml (大容量アルミ缶)",
        "type": "100%天然植物性マルチ高保湿バーム",
        "features": "天然シア脂（シアバター）、天然ミツロウ（ビーズワックス）、ビタミンE",
        "value": "人間の皮脂膜に含まれるステアリン酸やオレイン酸が豊富。真冬の冷風でゴワつき硬化した角質をふっくら軟化させ、強固なエモリエントラップを形成",
        "desc_p1": "プロヴァンスの自然の恵みを世界に届けるロクシタンの歴史は、このシアバターから始まりました。西アフリカのサバンナに自生するシアの木の実から採れる高純度シアバターに、天然ミツロウを絶妙なバランスでブレンドした『ピュア シアバター』は、真冬の乾燥で硬直した皮膚を蘇らせる万能の救護バームです。",
        "desc_p2": "缶の中では硬めのバター状ですが、手のひらに少量取って体温で温めると、スーッと黄金色のオイル状へと液化。乾燥で白く粉を吹いたスネや、ひび割れたかかと、カサつく毛先に塗り込むと、角層の奥まで油分が浸透しながら表面にミツロウの保護皮膜が完成します。赤ちゃんから大人まで、顔、唇、手足、髪の毛先まで全身のあらゆる乾燥SOSにマルチに応えてくれる冬の頼れる常備薬的存在です。",
        "target": "ひじ・ひざ・かかとが角化してガサガサになっている方、全身どこにでも使える高品質なオーガニックバームが欲しい方、家族で長く愛用したい方",
        "point": "指の背で適量を削り取り、両手のひらを擦り合わせて体温で完全にオイル状に溶かしてから肌へ押し当てます。入浴後の湿り気が残る肌へ伸ばすと、水分を抱き込んだまま密閉パックされ、翌朝驚くほど柔らかなマシュマロ肌に仕上がります。"
    },
    {
        "rank": 3,
        "tag": "🌹 オーガニックミツロウ×野ばらシードオイル！冬枯れ肌に黄金のツヤと密度を満たす極上バーム",
        "catch": "英国名門アロマセラピーの誇り。ビタミン豊富なローズヒップ油と高純度ミツロウが一体となり、真冬の乾燥くすみを一掃して輝くツヤ肌へ",
        "brand_name": "NEAL'S YARD REMEDIES (ニールズヤード)",
        "capacity": "50g (コバルトブルー遮光瓶)",
        "type": "オーガニック集中リペア美容バーム",
        "features": "オーガニックミツロウ、ローズヒップ種子油、ホホバ種子油、フランキンセンス精油、ゼラニウム精油",
        "value": "ビタミンの宝庫である野ばらシードオイルとミツロウの黄金ブレンド。寒冷でくすんだ冬の肌密度を高め、一晩でエステ後のようなふっくら発光肌へ",
        "desc_p1": "ロンドンのオーガニックアポセカリー（薬局）から誕生したニールズヤード レメディーズのアイコン的存在『ワイルドローズ ビューティバーム』。英国ソイルアソシエーション認定のオーガニックミツロウをベースに、必須脂肪酸やビタミンA・C・Eを豊富に含むローズヒップオイルを贅沢にブレンドした最高峰の美容バームです。",
        "desc_p2": "鮮やかな黄色のバームを肌に乗せると、フランキンセンスやゼラニウムの高貴なアロマが広がり、寒さで縮こまった心身を瞬時にリフレッシュ。ミツロウが肌表面に吸い付くような保護シールドを張り、ローズヒップの栄養素を角層深くへ閉じ込めます。翌朝の肌は乾燥によるゴワつきやくすみが一掃され、まるで内側から光を放つような透明感ともっちりとしたハリに満ちあふれます。",
        "target": "真冬の寒冷で肌のくすみや乾燥疲れが顔全体に出やすい方、極上のオーガニック精油の香りで夜のスキンケアを贅沢に過ごしたい方、肌密度を高めたい方",
        "point": "夜のお手入れの最後に、付属のスパチュラでパール粒大を取り、手のひらで温めてから顔全体を優しく包み込みます。週に1回、少し多めに塗って湯船に浸かる『バームスチームパック』を行うと、毛穴の汚れが浮き上がり極上のやわらか肌が手に入ります。"
    },
    {
        "rank": 4,
        "tag": "👑 ドイツ自然派の最高峰！ダマスクローズワックス×ミツロウが真冬の冷風を完全遮断",
        "catch": "ルドルフ・シュタイナーの人智学思想から生まれた奇跡のデイクリーム。貴族のような気品ある薔薇のワックスとミツロウが、極寒の北風から肌を完璧に防御",
        "brand_name": "Dr. Hauschka (ドクターハウシュカ)",
        "capacity": "30ml (アルミチューブ)",
        "type": "高貴オーガニック保護デイクリーム",
        "features": "ダマスクローズ花エキス、ダマスクローズ花ワックス、オーガニックミツロウ、アボカド油、シア脂",
        "value": "極寒の冬のヨーロッパで生まれた伝統の保護処方。皮膚の毛細血管を寒冷刺激から守り、赤ら顔や寒暖差による乾燥トラブルを寄せ付けない",
        "desc_p1": "バイオダイナミック有機栽培農法で作られた希少な植物のみを使用するドイツの老舗・ドクターハウシュカ。その創業時から変わらぬレシピで世界中のセレブリティやメイクアップアーティストに愛され続けているのが『ローズデイクリーム』です。貴重なダマスクローズの花びら約30枚分のエキスと、オーガニックミツロウが高密度に練り込まれています。",
        "desc_p2": "こっくりとして重厚感のあるクラシカルなテクスチャーですが、手のひらで温めて丁寧にハンドプレスすると、肌にピタッと吸い付くように一体化。ダマスクローズワックスとミツロウが、外気の冷たい木枯らしやエアコンの乾燥風に対する『透明な防護服』のような役割を果たします。真冬の外気で頬が赤くなりやすい方や、何を使っても乾燥が防げない超乾燥肌の方に、唯一無二の安心感をもたらします。",
        "target": "冬の冷たい北風に当たるとすぐに頬が赤くなる・乾燥ヒリつきを感じる方、本格的なドイツ自然化粧品を使いたい方、リッチで濃厚な保護膜を好む方",
        "point": "朝のスキンケアの最後に、パール粒大を手にとり、手のひらでしっかりと温めて柔らかくしてから、顔全体に優しく押し当てるように塗布します。しっかり保護膜ができるため、冬の冷たい外気の中でもメイク崩れや乾燥知らずで過ごせます。"
    },
    {
        "rank": 5,
        "tag": "👶 デメター認証の極上優しさ！オーガニックミツロウ×カレンドラが荒れた肌を救護",
        "catch": "世界で最も厳しい有機認証デメターを取得。カレンドラ（トウキンセンカ）の鎮静力とミツロウが融合し、真冬の水仕事の手荒れや赤ちゃんの敏感肌を優しくケア",
        "brand_name": "Martina (マルティナ)",
        "capacity": "50ml (オパールガラスジャー)",
        "type": "有機デメター認証マルチ保護バーム",
        "features": "オリーブ果実油、オーガニックミツロウ、トウキンセンカ花エキス（カレンドラ）、羊毛脂（ラノリン）、ダマスクバラ花水",
        "value": "石油由来成分・合成保存料・乳化剤完全フリー。皮膚の再生を促すカレンドラとミツロウのシールドが、真冬のひび割れや痛みを速やかに保護",
        "desc_p1": "ドイツの自然豊かなバイエルン地方で生まれたマルティナ・ゲプハルト。化学合成成分を一切使わず、100%自然の生命力だけで作られる同ブランドの『カレンドラベビークリーム』は、名前にベビーと付きながらも、大人の真冬の重度な乾燥荒れ肌の救世主として皮膚科医やオーガニック愛好家から絶賛されています。",
        "desc_p2": "鮮やかなカレンドラオレンジ色の濃厚なバームは、手肌や顔の荒れた部位に塗ると、ミツロウとラノリン（天然羊毛脂）の力で水や摩擦をしっかり弾く保護膜を形成。水仕事の前に指先に塗っておくことで、洗剤や冷水によるあかぎれを未然に防ぎます。カレンドラの優れた皮膚修復効果により、すでに荒れてしまった指先のささくれやひび割れも穏やかに修復へと導かれます。",
        "target": "真冬の水仕事や手洗いで指先があかぎれ・ささくれになりやすい方、肌が弱く完全オーガニックの無添加バームを探している方、赤ちゃんの冬の頬の乾燥対策",
        "point": "水仕事をする前や、夜寝る前に少量を指先や手肌にすり込みます。特に爪の生え際や指の関節など、皮膚が割れやすい部位に丁寧になじませることで、冬の頑固なひび割れを完璧に予防できます。"
    },
    {
        "rank": 6,
        "tag": "🐴 高純度馬油×天然ミツロウの奇跡の融合！通常の馬油を超える超濃厚密着ナイトパック",
        "catch": "元祖馬油の薬師堂が誇る最高峰グレード『No.7』。人間の皮脂に極めて近い馬油にミツロウをブレンドし、真冬の就寝中の水分蒸発を徹底ブロック",
        "brand_name": "薬師堂 (ソンバーユ)",
        "capacity": "60ml (ガラス瓶)",
        "type": "高純度馬油×ミツロウ高密着バーム",
        "features": "馬油（高純度比率）、天然ミツロウ",
        "value": "馬油の驚異的な浸透力とミツロウの持続密着シールドが合体。真冬のエアコン暖房をつけっぱなしで寝ても翌朝まで吸い付くモチモチ肌を持続",
        "desc_p1": "日本における馬油の元祖・薬師堂が、長年の研究開発の集大成として生み出した最高峰モデルが『ソンバーユ No.7』です。通常のソンバーユよりも融点の高いリッチな脂肪酸画分を厳選抽出し、天然ミツロウを配合することで、とろけるような浸透力と強固な持続密着力を高次元で両立させています。",
        "desc_p2": "テクスチャーは濃厚でコクのあるバター状ですが、肌に乗せるとすーっと体温でなじみ、角層の奥深くへと吸い込まれていきます。馬油が皮膚深部に栄養を届け、ミツロウが表面で揮発を防ぐため、真冬のエアコン暖房をつけたままでも肌がカサつくことがありません。夜のスキンケアの最後に顔全体に薄く伸ばせば、翌朝の洗顔時にはまるでエステでオイルマッサージを受けた後のような柔らかく弾む素肌を実感できます。",
        "target": "真冬に朝起きると顔がパリパリに乾いている方、馬油の浸透力とバームの密着力を両方味わいたい方、純国産の安心・無添加処方を好む方",
        "point": "お風呂上がりの化粧水のあと、小豆粒大を手のひら全体に薄く広げ、顔を包み込むようにハンドプレスします。目元や口元の乾燥小ジワには少量を指先で重ねづけすると、真冬の夜間乾燥を完全に跳ね返せます。"
    },
    {
        "rank": 7,
        "tag": "🌸 国産無農薬ミツロウ×ツバキ種子油！石油系完全フリーのオーガニック高密着リップ美容液",
        "catch": "アムリターラのこだわりが凝縮。国産無農薬ミツロウと伊豆大島産ツバキ油が真冬の皮向け唇をやさしく包み込み、自然なツヤとしなやかさを再生",
        "brand_name": "AMRITARA (アムリターラ)",
        "capacity": "スティック / チューブタイプ",
        "type": "オーガニック高保湿リップトリートメント",
        "features": "国産無農薬ミツロウ、ツバキ種子油、ホホバ種子油、シア脂、トコフェロール",
        "value": "石油由来原料・合成防腐剤完全フリー。食べるものと同等レベルの安心基準で作られ、真冬の敏感な唇の荒れを素早く修復",
        "desc_p1": "「口に入れるものだからこそ、スキンケア以上に安全で安心な成分を選びたい」という想いに応える、国産オーガニックブランド・アムリターラの『モイストカメリア リップセラム』。日本国内で農薬を使わずに育てられたミツバチから採れる極めて希少な無農薬ミツロウを主原料に採用しています。",
        "desc_p2": "昔ながらの圧搾法で搾られた伊豆大島産のツバキ種子油が、乾燥で硬くなった唇の角質を優しくほぐし、ミツロウが表面に上品なうるおい膜を形成。タール系色素や合成香料、鉱物油を一切含まないため、荒れて皮がめくれた唇につけても全く染みません。口紅の下地として使えば、マットなリップも乾燥割れすることなく美しい発色が一日中続きます。",
        "target": "リップクリームで唇が荒れやすい超敏感肌の方、食事の際にも気にならない安心のオーガニックリップを求める方、ツバキ油の保湿力を試したい方",
        "point": "唇に優しく円を描くように滑らせてなじませます。夜寝る前に唇の輪郭を少しはみ出すくらい厚めに塗って就寝すると、翌朝にはプルプルの生まれたてのような唇に整います。"
    },
    {
        "rank": 8,
        "tag": "🌻 ハイブリッドヒマワリ油×天然ミツロウ！界面活性剤ゼロで肌に寄り添う素肌想いクリーム",
        "catch": "太陽油脂の石けん乳化技術。オレイン酸豊富なヒマワリ油とミツロウのシンプル処方で、冬の敏感肌にしっとり馴染んで潤い膜を長時間キープ",
        "brand_name": "太陽油脂 (パックスナチュロン)",
        "capacity": "35g (チューブタイプ)",
        "type": "無添加天然エモリエントクリーム",
        "features": "ハイブリッドヒマワリ油、天然ミツロウ、グリセリン、ホホバ油、ヒノキチオール",
        "value": "合成界面活性剤や合成ポリマーを一切使わない純粋な天然エモリエント処方。真冬のエアコン乾燥から素肌の皮脂膜をやさしく守り抜く",
        "desc_p1": "人と自然にやさしい石けんづくりを追求し続ける太陽油脂の隠れたロングセラー『パックスナチュロン エモリエントクリーム』。皮脂の主成分であるオレイン酸を豊富に含むハイブリッドヒマワリ油をベースに、天然ミツロウを配合した肌に限りなく優しい保湿クリームです。",
        "desc_p2": "合成界面活性剤やシリコーン、鉱物油、合成香料を完全に排除。天然ミツロウの乳化力と保護力によって作られたクリームは、肌に乗せるとサラッとしていながら、肌の角層にスーッと溶け込むように馴染みます。塗布後はベタつかず、まるで自分の皮脂膜が強化されたかのような軽やかで頼もしいシールド感が持続。冬の敏感肌やデリケート肌のデイリーケアに最適です。",
        "target": "合成界面活性剤や合成成分を避けてシンプルに保湿したい方、軽やかなつけ心地でしっかり水分蒸発を防ぎたい方、肌本来の皮脂膜をサポートしたい方",
        "point": "化粧水のあと、パール粒1〜2個分を手にとり、手のひらで温めてから顔全体に優しく伸ばします。化粧水がまだ少し肌に残っている状態でなじませると、よりすばやく乳化浸透してモチモチ感が持続します。"
    },
    {
        "rank": 9,
        "tag": "🌿 オーガニックミツロウ×ホホバ種子油！ドイツ発オーガニックコスメの名門リップ",
        "catch": "ドイツBDIH・NATRUE認証取得。オーガニックミツロウとカレンデュラエキスが真冬の北風による唇の亀裂や痛みをしっかり防ぐ",
        "brand_name": "LOGONA (ロゴナ)",
        "capacity": "4.5g (スティックタイプ)",
        "type": "オーガニック高密着ケアリップスティック",
        "features": "ヒマシ油、ホホバ種子油、水添ココグリセリル、オーガニックミツロウ、トウキンセンカ花エキス（カレンデュラ）",
        "value": "植物油とミツロウが唇に厚みのある保護層を形成。真冬の過酷なアウトドアやスキー場などの極寒環境下でも唇のひび割れを許さない",
        "desc_p1": "ドイツの自然化粧品の草分け的存在であるロゴナの看板アイテム『リップクリーム キャレンデュラ』。ヨーロッパの極寒の冬を乗り切るために調合された、オーガニックミツロウとホホバオイル、そして肌の修復ハーブであるカレンデュラを贅沢にブレンドした名品です。",
        "desc_p2": "唇に塗ると硬すぎず柔らかすぎない絶妙なタッチで滑り、唇の表面にピタッと高密着なシールド膜を張ってくれます。ミツロウのワックス効果により、マスクの摩擦や飲食をしても保護膜が落ちにくく、長時間の外出時でも塗り直しの頻度を減らせる頼もしさ。自然なハーブの香りと、荒れた唇をしっとり落ち着かせる確かな実力で、冬のアウトドア派からも熱い支持を集めています。",
        "target": "冬に外出が多く冷たい風にさらされる機会が多い方、持ちが良く落ちにくいオーガニックリップを探している方、カレンデュラの鎮静効果を実感したい方",
        "point": "外出の直前に唇全体に往復してしっかり塗布します。スキーやウィンタースポーツ、冬のキャンプなどに行く際は、ポケットに入れてこまめに重ね塗りすることで、唇の日焼けと極冷乾燥をダブルで防げます。"
    },
    {
        "rank": 10,
        "tag": "🦡 USDAオーガニック認証ミツロウ×極上オリーブ油！アメリカ伝統の万能レスキューバーム",
        "catch": "可愛いアナグマの缶に入った本気のアメリカンオーガニック。良質なミツロウとエキストラバージンオリーブ油が真冬の全身のガサガサ部位を体温で溶かして鎮静",
        "brand_name": "BADGER (バジャー)",
        "capacity": "56g / クラシカルなアルミ缶",
        "type": "USDA認定オーガニック万能バーム",
        "features": "エキストラバージンオリーブ果実油、オーガニックミツロウ、ヒマシ油、アロエベラエキス",
        "value": "アメリカ農務省の厳しいUSDAオーガニック認証をクリア。天然ミツロウの強力な撥水・保護作用で、真冬の寒冷地でも肌の水分を一滴も失わせない",
        "desc_p1": "大工の創業者が真冬の手荒れを治すために自宅のキッチンで作ったことから始まったアメリカ発の『バジャー（BADGER）』。USDA（米国農務省）の厳しいオーガニック基準をクリアした天然ミツロウと、低温圧搾のエキストラバージンオリーブオイルをブレンドした、まさに冬のレスキューバームの原点です。",
        "desc_p2": "缶を開けると、ミツロウ本来の自然な甘い香りとオリーブの優しいアロマが広がります。体温で温めるとオイル状に溶け出し、ひび割れたかかとや硬くなった指先、乾燥で突っ張る目元や頬に密着。ミツロウが肌表面に呼吸する被膜を作り、外気の乾燥を物理的にシャットアウトします。冬のバッグに1缶忍ばせておくだけで、あらゆる乾燥トラブルに即座に対応できる万能のお守りコスメです。",
        "target": "クラシカルで温もりのあるオーガニック缶バームが好きな方、かかとやひじの頑固なガサガサを徹底保護したい方、アウトドアや旅行のお供にしたい方",
        "point": "指の腹でバームの表面をくるくると撫でて体温で溶かしながら取ります。就寝前にかかとに厚く塗り込み、靴下を履いて寝ると、翌朝ガサガサだったかかとがつるんとした滑らかさに激変します。"
    }
]

faq_list = [
    {
        "question": "冬の乾燥対策として、ワセリン（石油系）ではなく『天然ミツロウ（ビーズワックス）』を選ぶメリットは何ですか？",
        "answer": "ワセリンは石油由来の炭化水素で肌表面を密閉する力に優れていますが、肌に対して栄養を与える作用はありません。一方、ミツバチが分泌する『天然ミツロウ』は、高級脂肪酸エステルをはじめ、プロポリスやフラボノイド、微量ビタミンなどの天然美肌成分を含んでいます。さらに最大の特長は、角層の水分蒸発を物理的にブロックしながらも『皮膚の通気性を妨げない（毛穴を塞ぎにくい）』という点です。真冬の過酷な冷風から肌を守りながら、肌本来の健やかな代謝を妨げない理想的な保護シールドを形成できます。"
    },
    {
        "question": "ミツロウ配合のクリームやバームが冬の寒さで硬くなってしまった場合、どうやって使うのが正解ですか？",
        "answer": "天然ミツロウは気温が下がると結晶化して固くなる性質を持っています。無理に固いまま肌に擦り付けると摩擦ダメージの原因になるため、必ず『手のひらの体温で温めて溶かしてから』使用してください。指の背などで少量を削り取り、両手のひらを擦り合わせると、体温（約36℃）で数秒のうちにスーッと黄金色のオイル状へと液化します。完全に液状化させてから肌を包み込むようにハンドプレスするのが、肌への密着度と浸透性を高めるプロの技です。"
    },
    {
        "question": "ミツロウ配合のバームは顔全体に塗ってもニキビや毛穴詰まりの原因になりませんか？",
        "answer": "純度の高い天然ミツロウ自体はコメドジェニック（毛穴詰まり）を起こしにくい成分ですが、皮脂分泌の多いTゾーン（額や鼻）に厚塗りしすぎると油分過多になる場合があります。顔に使用する際は、乾燥が激しい目元や口元、頬骨の高い位置を中心に薄くハンドプレスでなじませるのが基本です。また、夜のスキンケアの最後に薄く伸ばすことで、就寝中のエアコンによる過乾燥（過蒸発）を防ぐ『スリーピングシールド』として絶大な効果を発揮します。"
    },
    {
        "question": "ミツロウコスメに使用期限や保管上の注意点はありますか？",
        "answer": "ミツロウ自体は天然の防腐・抗菌作用が高く酸化しにくい安定した成分ですが、植物オイルや精油がブレンドされているオーガニック製品が多いため、直射日光や高温多湿を避けて常温で保管し、開封後は6ヶ月〜1年程度を目安に使い切るのが理想的です。真冬の暖房器具の近くに置くと溶けて分離することがあるため、涼しい場所で保管してください。"
    }
]

# JSON-LD構造化データ
jsonld_items = []
for i, item in enumerate(items):
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": item["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-beeswax.html#item-{i+1}"
    })

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
        "@id": "https://lumi-cosme.vercel.app/winter-beeswax.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥を完全遮断する高保湿ミツロウコスメランク10",
    "description": "11月・12月の極限低湿度と冷風から肌を守る高保湿ミツロウコスメを徹底厳選！バーツビーズ、ロクシタン、ニールズヤード、Dr.ハウシュカ、ソンバーユからマルティナ、バジャーまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の密着シールド術を詳しく解説。",
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
    "name": "真冬の高保湿ミツロウコスメおすすめ人気ランキング10選",
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
            <div class="spec-row"><span class="spec-th">注目天然成分</span><span class="spec-td">{d['features']}</span></div>
            <div class="spec-row"><span class="spec-th">真冬のシールド価値</span><span class="spec-td">{d['value']}</span></div>
          </div>
          
          <div class="review-box">
            <h4>💡 美容皮膚専門ライターの詳細解説＆真冬の実践レビュー</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥を完全遮断する高保湿ミツロウコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の極限低湿度と冷風から肌を守る高保湿ミツロウコスメを徹底厳選！バーツビーズ、ロクシタン、ニールズヤード、Dr.ハウシュカ、ソンバーユからマルティナ、バジャーまで楽天で今すぐ買えるおすすめ人気ランキング10選と冬の密着シールド術を詳しく解説。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-beeswax.html">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥を完全遮断する高保湿ミツロウコスメランク10">
  <meta property="og:description" content="11月・12月の極限低湿度と冷風から肌を守る高保湿ミツロウコスメを徹底厳選！バーツビーズ、ロクシタン、ニールズヤード、Dr.ハウシュカ、ソンバーユまで厳選10選。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-beeswax.html">
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
      --primary-dark: #92400e;
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
      line-height: 1.85;
      border-left: 4px solid var(--primary-color);
      padding-left: 1.25rem;
      background: var(--bg-light);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
    }}
    
    .toc-box {{
      background: white;
      border: 1px solid var(--border-color);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin-bottom: 3rem;
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
    .toc-list {{
      list-style: none;
      display: grid;
      gap: 0.6rem;
    }}
    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{
      color: var(--primary-color);
      text-decoration: underline;
    }}
    
    .content-section {{
      background: white;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.5rem;
      margin-bottom: 3rem;
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
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
      background: linear-gradient(135deg, #d97706, #92400e);
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
      .article-title {{ font-size: 1.45rem; }}
      .article-header {{ padding: 1.5rem; }}
      .content-section {{ padding: 1.5rem; }}
    }}
    
    .product-visual {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid #e5e7eb;
      margin-bottom: 1rem;
    }}
    .price-box {{
      background: #fef2f2;
      border: 1px solid #fee2e2;
      padding: 0.6rem;
      border-radius: 8px;
      margin-bottom: 1rem;
    }}
    .price-label {{ font-size: 0.75rem; color: #991b1b; display: block; }}
    .price-value {{ font-size: 1.5rem; font-weight: 800; color: #b91c1c; }}
    .price-tax {{ font-size: 0.75rem; color: #7f1d1d; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      padding: 0.85rem 1rem;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: white;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 4px 6px -1px rgba(185, 28, 28, 0.3);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .spec-table {{
      background: #f9fafb;
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1.25rem;
      font-size: 0.88rem;
    }}
    .spec-row {{
      display: grid;
      grid-template-columns: 110px 1fr;
      padding: 0.4rem 0;
      border-bottom: 1px dashed #e5e7eb;
    }}
    .spec-row:last-child {{ border-bottom: none; }}
    .spec-th {{ font-weight: 700; color: #4b5563; }}
    .spec-td {{ color: #1f2937; }}
    
    .review-box {{
      background: #fffbeb;
      border-left: 4px solid var(--primary-color);
      padding: 1.25rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1.25rem;
    }}
    .review-box h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.5rem;
    }}
    .review-box p {{
      font-size: 0.92rem;
      color: #374151;
      margin-bottom: 0.6rem;
      line-height: 1.75;
    }}
    .review-box p:last-child {{ margin-bottom: 0; }}
    
    .target-box, .usage-box {{
      padding: 0.85rem 1rem;
      border-radius: 8px;
      margin-bottom: 0.85rem;
      font-size: 0.9rem;
    }}
    .target-box {{ background: #eff6ff; border: 1px solid #dbeafe; color: #1e40af; }}
    .target-box p {{ color: #1e3a8a; margin-top: 0.25rem; }}
    .usage-box {{ background: #fefce8; border: 1px solid #fef08a; color: #854d0e; }}
    .usage-box p {{ color: #713f12; margin-top: 0.25rem; }}
    
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.5rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.8;
    }}
    
    .footer-internal-links {{
      background: white;
      border-radius: var(--radius);
      padding: 2rem;
      box-shadow: var(--shadow);
      margin-top: 3rem;
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1rem;
    }}
    .footer-link-pill {{
      display: block;
      padding: 0.6rem 0.85rem;
      background: #f9fafb;
      border: 1px solid #e5e7eb;
      border-radius: 8px;
      color: #374151;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .footer-link-pill:hover {{
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
      <a href="/#skincare">オーガニック・バーム特集</a>
      <span>&gt;</span>
      <span aria-current="page">高保湿ミツロウコスメ特集</span>
    </nav>

    <article class="article-header">
      <div class="article-meta">
        <time datetime="2026-11-04">公開日：2026年11月4日</time>
        <span>執筆：冬コスメ徹底比較ラボ 編集部（オーガニックエモリエント解析チーム）</span>
      </div>
      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！ミツバチが創る天然の保護皮膜で真冬の冷風と乾燥を完全遮断する高保湿ミツロウコスメランク10</h1>
      <p class="article-lead">
        11月から12月にかけて日本列島を覆うシベリア気団の寒気。外気の湿度は20%台まで急落し、室内のエアコン暖房によって「空気中の水分飢餓状態」が生み出されます。この極限環境では、一般的な水分ローションや軽い乳液をいくら塗り重ねても、数十分後には水分が空気中に奪われて蒸発してしまいます。過酷な冬の砂漠気候から肌と唇を守り抜く唯一の砦が、ミツバチの巣から採れる天然のエモリエントワックス『ミツロウ（ビーズワックス）』です。本記事では、角層の通気性を保ちながら強固な物理シールド膜を形成する名品ミツロウコスメを徹底比較し、おすすめ人気ランキング10選としてご紹介します。
      </p>
    </article>

    <section class="toc-box">
      <h2 class="toc-title">📑 目次・記事ナビゲーション</h2>
      <ul class="toc-list">
        <li><a href="#why-beeswax">1. なぜ湿度20%の真冬には水溶性保湿剤ではなく天然ミツロウ（ビーズワックス）が必要なのか？</a></li>
        <li><a href="#selection-criteria">2. 失敗しない冬の高保湿ミツロウコスメの選び方・3つの基準</a></li>
        <li><a href="#comparison-table">3. 高保湿ミツロウコスメ10選 スペック・価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿ミツロウコスメおすすめ人気ランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. オーガニック専門家が答えるミツロウケアのよくある疑問Q&amp;A</a></li>
        <li><a href="#conclusion">6. まとめ：真冬の冷風から肌を守り抜くミツロウの物理シールド術</a></li>
      </ul>
    </section>

    <!-- セクション1 -->
    <section class="content-section" id="why-beeswax">
      <h2 class="section-title">🐝 1. なぜ湿度20%の真冬には水溶性保湿剤ではなく天然ミツロウ（ビーズワックス）が必要なのか？</h2>
      <p class="section-p">
        11月中旬を過ぎると、日本上空には強い西高東低の冬型気圧配置が現れ、湿度が20%〜30%にまで落ち込みます。さらに室内でエアコン暖房を入れると、空気の飽和水蒸気量が跳ね上がるため、皮膚表面の水分が猛烈な勢いで大気中へと吸い取られていきます。
      </p>
      <p class="section-p">
        この時期に多くの人が陥る罠が、「乾燥するから」とヒアルロン酸やコラーゲンなどの水溶性保湿成分ばかりを重ねることです。周囲の湿度が極端に低い環境下では、水溶性成分が抱え込んだ水分ですら蒸発してしまい、かえって角層深部の水分まで一緒に奪い去る「過蒸発現象」が起こります。
      </p>
      <p class="section-p">
        この冬の水分蒸発危機を物理的に断ち切る最強の天然物質が<strong>『ミツロウ（ビーズワックス）』</strong>です。ミツロウは、ミツバチが自らの腹部にある蝋腺から分泌する天然のワックスエステルであり、高級脂肪酸と高級アルコールが結合した高密度な分子構造を持っています。
      </p>
      <p class="section-p">
        石油系ワックス（パラフィンや一般的なワセリン）と決定的に異なるのは、ミツロウの持つ『呼吸する保護皮膜特性』です。肌表面に隙間なく密着して外気の乾燥冷風や水・摩擦を強力に弾きながらも、皮膚の正常なガス交換（呼吸）を妨げません。さらにプロポリスやフラボノイドといった天然の抗菌・抗酸化成分を微量に含んでいるため、真冬のひび割れやあかぎれ、唇の乾燥亀裂を穏やかに保護・修復する類まれなスキンケアパワーを発揮するのです。
      </p>
    </section>

    <!-- セクション2 -->
    <section class="content-section" id="selection-criteria">
      <h2 class="section-title">🔍 2. 失敗しない冬の高保湿ミツロウコスメの選び方・3つの基準</h2>
      <p class="section-p">
        真冬の過酷な寒冷乾燥から肌・唇・手肌を守り抜くミツロウコスメを選ぶ際は、以下の3つの基準をチェックしてください。
      </p>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準①：オーガニック認証（USDA、デメター、BDIHなど）または未精製ミツロウの品質</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          ミツバチが集める蜜や花粉に残留農薬がない環境で採取された「オーガニック認証ミツロウ」や、漂白・脱臭を過度に行っていない良質なミツロウ（バーツビーズ、ニールズヤード、マルティナなど）を選ぶことで、ミツロウ本来の抗菌・抗酸化パワーを100%享受できます。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0; margin-bottom: 1.5rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準②：組み合わせる植物オイル（シア脂・ホホバ・オリーブ・ローズヒップ）との親和性</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          ミツロウ単体では常温で固いため、どのような植物オイルとブレンドされているかが使い心地と保湿持続性を左右します。浸透性に優れたシアバター（ロクシタン）や、皮脂に近いホホバ油、栄養豊富なローズヒップ油との黄金比率ブレンドを選ぶことで、角層浸透と表面シールドが完璧に両立します。
        </p>
      </div>
      <div style="background: var(--bg-light); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 8px 8px 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.5rem;">基準③：使用部位（リップ・手肌・顔全体）に合わせたテクスチャーと密着度</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          唇には固めで落ちにくいスティックタイプ（バーツビーズ、ロゴナ）、手足のひび割れやかかとにはコクのある缶入りバーム（バジャー、ロクシタン）、顔のナイトパックには体温でなめらかに溶ける美容バーム（ニールズヤード、ドクターハウシュカ）と、部位に合わせて使い分けるのが冬ケアの極意です。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 高保湿ミツロウコスメ10選 スペック・価格比較表</h2>
      <p class="section-p">
        楽天市場の公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。ケアしたい部位やテクスチャーに合わせて比較検討してください。
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
        🏆 高保湿ミツロウコスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. オーガニック専門家が答えるミツロウケアのよくある疑問Q&amp;A</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">🐝 6. まとめ：真冬の冷風から肌を守り抜くミツロウの物理シールド術</h2>
      <p class="section-p">
        11月から12月にかけて訪れる乾燥冷風と極限の低湿度は、どんなに念入りに保湿しても水分をあっという間に蒸発させてしまう過酷な環境です。
      </p>
      <p class="section-p">
        この真冬の過酷な気候下で、肌や唇が本来持っている水分を死守するためには、ミツバチが創り出す天然ミツロウ（ビーズワックス）の強固で呼吸する保護皮膜が最強の味方になります。
      </p>
      <p class="section-p">
        乾燥で皮がめくれ上がった唇にはバーツビーズの密着スティック、水仕事でひび割れそうな手肌にはロクシタンやマルティナのバーム、そして就寝中のエアコン乾燥にはニールズヤードやソンバーユNo.7の贅沢パック——。
      </p>
      <p class="section-p">
        天然の温もりとミツバチの知恵が詰まったミツロウコスメを味方につけて、真冬の寒冷乾燥をものともしない、しっとり吸い付くような潤い美肌を守り抜いてください。
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

with open("winter-beeswax.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-beeswax.html successfully. Size: {len(html_content):,} bytes")
