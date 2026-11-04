import json
import re

with open("fetched_final_30_manuka_prickly_calendula.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_prickly_pear"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🌵 モロッコ王室秘伝の奇跡！オイルとセラムが融合した冬の最高傑作エッセンス",
        "catch": "過酷な砂漠で自活するサボテンシードオイルと高保湿エッセンスの最適ブレンド。オイルの濃厚な保護膜とセラムの浸透力を完璧に兼ね備え、真冬の乾燥しぼみ肌をふっくら満水へ導く殿堂入り美容液",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "30ml / スポイトボトル",
        "type": "オイルイン高機能エイジングセラム",
        "features": "モロッコ産サボテンシードオイル、サボテンエキス（オプンチアフィクスインジカ茎エキス）、マテ茶葉発酵エキス、アサイーベリーエキス、キヌア種子エキス",
        "value": "アルガンオイルの1.6倍の天然ビタミンEと豊富なリノール酸を含有。オイルなのに一切ベタつかず、真冬の暖房直風で硬直した角層を瞬時にシルクのような柔肌へ変革",
        "desc_p1": "11月から12月にかけて、木枯らしと室内の暖房によって肌内部の水分が抜け落ち、表面は皮脂不足でカサつくのに毛穴は目立つという『複合的な冬枯れ』に直面する女性が後を絶ちません。韓国コスメ界で『オイル美容の概念を根底から覆した名品』として爆発的な支持を受け、日本でもリピーターが続出しているのが、ハクスリーの『オイルエッセンス エッセンスライク オイルライク』です。最大の特徴は、サボテン種子から絞り出された極めて希少なオイルを、みずみずしい水分エッセンスの中に微細に分散させている点にあります。",
        "desc_p2": "スポイトから手のひらに落とすと、トロリとした乳白色のエッセンスが広がり、ハクスリー独自のモロッカンガーデンの高貴で爽やかなボタニカルの香りが漂います。肌に乗せた瞬間、水のようにスルスルと角層深部へ染み渡り、後肌はオイルを塗ったとは思えないほど軽やか。しかし肌内部にはギュッと濃密な水分と油分が満ち足りており、手のひらで触れると吸い付くような弾力と内側から発光するような水光ツヤが宿ります。朝のメイク前に使ってもファンデーションがヨレず、むしろ一日中粉吹きや乾燥割れを完璧に防いでくれます。",
        "target": "オイルのベタつきやテカリが苦手だけど真冬の乾燥を防ぎたい方、肌のキメとしぼみを同時に立て直したい方、上品なボタニカルの香りでリラックスしたい方",
        "point": "化粧水の直後、スポイトで1〜2滴を手にとり、手のひらで軽く温めてから顔全体に引き上げるように伸ばします。乾燥が目立つ目元やほうれい線には、指先で優しくタッピングするように重ねづけをすると、角層の隙間がふっくらと持ち上がります。"
    },
    {
        "rank": 2,
        "tag": "👑 100万個の種子からわずか1リットル！アルガンを超える最高峰ピュア原液",
        "catch": "モロッコ産ウチワサボテン種子を100%低温圧搾した未精製プレミアムオイル。ビタミンEとステロールの驚異的な含有量で、真冬の深く刻まれた乾燥ジワとハリ不足をふっくら押し返す",
        "brand_name": "ナチュラルモロッコ (Natural Morocco)",
        "capacity": "30ml / 遮光ボトル",
        "type": "高純度100%未精製ウチワサボテン原液オイル",
        "features": "未精製ウチワサボテン種子油100%（エコサート認証・コールドプレス製法）、天然トコフェロール、高濃度オメガ6（リノール酸）",
        "value": "防腐剤・化学物質完全無添加。1トンのウチワサボテン果実から採れる種子はわずか数キロ、そこから抽出される貴重な黄金オイル。アルガンオイルを超える圧倒的な抗酸化・保水力を誇る",
        "desc_p1": "世界で最も高価で希少な植物オイルとして美容賢者の間で熱狂的な支持を集めるのが『ウチワサボテン種子オイル』です。極度の乾燥と激しい寒暖差に晒されるモロッコの乾燥砂漠において、自らの細胞内に膨大な水分を蓄え続けるウチワサボテン。その種子には、アルガンオイルの約1.6倍もの天然ビタミンE（トコフェロール）と、肌の皮脂膜の柔軟性を高めるオメガ6系リノール酸が60%以上も凝縮されています。",
        "desc_p2": "淡い黄金色をしたこの原液オイルは、肌に乗せた瞬間の肌馴染みが他のどんな植物オイルとも異なり、角層へグングン吸い込まれていきます。皮脂の構成成分に近い植物性ステロールが豊富に含まれているため、寒冷で硬くゴワついた真冬の角質層をみるみる解きほぐし、まるでエステのスチームを浴びた直後のような柔らかな肌触りを実現。夜のスキンケアの最後に2滴馴染ませるだけで、翌朝の洗顔時に肌密度の詰まり具合に驚かされます。",
        "target": "目元や口元の乾燥小ジワを本気で集中ケアしたい方、本物志向の100%オーガニック原液を使いたい方、冬になるとどんなクリームでも肌がゴワつく方",
        "point": "夜のお手入れの最後に、手のひらに2〜3滴を取り、両手を擦り合わせて温めてから顔全体を包み込みます。特に目元の小ジワやほうれい線には、薬指の腹でトントンと押し込むように馴染ませるのが効果的です。"
    },
    {
        "rank": 3,
        "tag": "🛡️ バターのように溶けて密閉！過酷な砂漠気候から肌を守る高密度クリーム",
        "catch": "サボテンエキスと植物性セラミドを贅沢にブレンドした超リッチな高保湿クリーム。冬の過酷な暖房や冷たい木枯らしから肌バリアを鉄壁ガードするプロテクト設計",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "50ml / 専用スパチュラ付きガラスジャー",
        "type": "高密度バリアプロテクトクリーム",
        "features": "サボテンシードオイル、サボテンエキス、植物性セラミドコンプレックス、シア脂、白樺樹液",
        "value": "バターのような硬めのリッチテクスチャーが体温でスルスルとろけて肌に密着。外的刺激を物理的に遮断しながら水分蒸発を長時間阻止",
        "desc_p1": "『冬の屋外に出た瞬間、冷たい風で顔の皮膚が突っ張って痛い』『暖房の効いた部屋に一日中いると、夕方には肌が干からびてファンデーションがひび割れる』…そんな極限の乾燥トラブルに立ち向かうために作られたのが、ハクスリーの『クリーム モアザンモイスト』です。ハクスリーのクリームラインナップの中で最も高保湿で濃厚な処方を誇ります。",
        "desc_p2": "ガラスジャーに入ったクリームは、一見すると固形のバターのようですが、付属のスパチュラですくって肌の上に乗せると、手のひらの体温でじわっととろけてシルキーな保護膜へと変化します。サボテンエキスと植物性セラミドが肌の角層ラメラ構造を強力にサポートするため、塗った瞬間から肌が包み込まれるような深い安心感に満たされます。表面はサラリとベルベットのように整うため、枕にベタベタつく心配もなく、翌朝まで満水のうるおいが持続します。",
        "target": "真冬になると毎年深刻な乾燥や粉吹きに悩まされる方、こっくり濃厚なのに重すぎない上質なクリームを探している方、肌のバリア機能を根本から立て直したい方",
        "point": "朝晩のスキンケアの最後に、パール大をスパチュラで取り、手のひら全体に温めてから顔を包み込むようにハンドプレスします。冬の特に乾燥がひどい日は、夜に少し厚めに塗ってスリーピングマスクのように使うのがおすすめです。"
    },
    {
        "rank": 4,
        "tag": "🌿 有機オーガニック認証！真冬の目元・口元をピンポイントで押し上げる濃密ドロップ",
        "catch": "フランスの老舗オーガニックブランドCODINAが厳選した未精製ウチワサボテン種子油。1滴に濃縮された豊富な必須脂肪酸が、冬の乾燥によって刻まれたキメの乱れを滑らかに修復",
        "brand_name": "CODINA (コディナ)",
        "capacity": "10ml / スポイト遮光瓶",
        "type": "プレミアムオーガニック美容オイル",
        "features": "未精製ウチワサボテン種子油100%（ナチュール・エ・プログレ認証）、オメガ6（リノール酸）、トコフェロール、植物ステロール",
        "value": "ヨーロッパの厳しいオーガニック認証を取得。酸化に強い安定した脂肪酸組成で、冬のデリケートな目元・口元にハリと弾力を集中チャージ",
        "desc_p1": "オーガニックコスメの本場フランスで絶大な信頼を集めるCODINA（コディナ）の『ウチワサボテンオイル』。過酷なモロッコの半砂漠地帯でたくましく育ったウチワサボテンの種子から、伝統的なコールドプレス製法で熱を加えずに丁寧に抽出された純度100%の美容オイルです。",
        "desc_p2": "1滴手に取るだけでわかる、濃密でコクのあるリッチなテクスチャー。肌に塗布すると植物本来のナッツのような香りがほのかに香り、驚くべきスピードで角層へと浸透していきます。リノール酸とビタミンEが乾燥によって萎縮した角層細胞をふっくらと持ち上げ、目元のちりめんジワや乾燥によるたるみ毛穴を滑らかに整えます。スポイト1滴で顔全体に行き渡るほど伸びが良いため、10mlでも1〜2ヶ月しっかり使えるコストパフォーマンスの高さも魅力です。",
        "target": "オーガニック品質に徹底的にこだわりたい方、目元やほうれい線のエイジングサインが集中的に気になる方、浸透力が高くベタつかない美容オイルを求める方",
        "point": "洗顔後、化粧水をつける前のブースターとして1滴馴染ませるか、アイクリームの代わりに米粒半分程度を目元に優しくタッピングするように塗り込みます。爪の甘皮に馴染ませれば、冬のハイポニキウムの乾燥保護にも最適です。"
    },
    {
        "rank": 5,
        "tag": "💧 精製水の代わりにサボテンエキス90%超！肌のpHを整え満水肌へ導く弱酸性トナー",
        "catch": "一般的な化粧水のように精製水をベースにするのではなく、主原料にサボテンエキスを90%以上贅沢に採用。冬の寒冷で硬化した肌pHを瞬時に弱酸性へ整え、あふれる水分で満たす化粧水",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "120ml / ガラスボトル",
        "type": "高保水弱酸性ブースト化粧水",
        "features": "サボテン茎エキス（90%以上配合）、サボテンシードオイル、センチフォリアバラ花水、紫サルスベリエキス",
        "value": "アルコール・パラベン無添加の弱酸性処方。洗顔後のアルカリ性に傾いた肌を瞬時に整え、角層のすみずみまで満水状態を保つ高機能ローション",
        "desc_p1": "冬のスキンケアにおいて、化粧水が肌に入っていかない最大の原因は、水道水による洗顔で肌のpHがアルカリ性に傾き、角質層のバリアが硬化してしまうことにあります。ハクスリーの『トナー エクストラクトイット』は、ベースとなる水分の90%以上にサボテンエキスを使用し、肌の理想的な弱酸性（pH5.5前後）へと瞬時に引き戻す画期的な高保湿化粧水です。",
        "desc_p2": "サラサラとした透明なテクスチャーでありながら、肌にパッティングするとまるで高濃度の美容液を浴びたかのように角質層がしっとりと潤います。サボテン由来の天然多糖類が水分分子を強力に捕まえるため、塗布した直後から肌表面がツルンと滑らかになり、手のひらがピタッと吸い付くようなモチモチ感が出現。ハクスリー特有のモロッカンガーデンの香りに包まれながら、真冬の乾いた角層を潤いで満たします。",
        "target": "とろみ化粧水特有の肌表面の膜感やベタつきが苦手な方、肌のキメを整えて化粧水の浸透力を上げたい方、弱酸性処方で肌バリアを安定させたい方",
        "point": "洗顔後すぐにコットンに適量を含ませて肌全体を優しく拭き取るように馴染ませた後、さらに手のひらに500円玉大を取り、ハンドプレスで2〜3回重ねづけします。乾燥が激しい日は、コットンを割いて3分間のローションパックを行うと透明感が劇的にアップします。"
    },
    {
        "rank": 6,
        "tag": "👜 ロールオンで乾燥小ジワを直撃！いつでもどこでもサボテンのハリを携帯するタッチオイル",
        "catch": "オーガニック認証ウチワサボテン種子油を配合した携帯型ロールオンオイル。真冬のオフィスや外出先で、ファンデーションの上からでも目元や口元の乾燥小ジワに直塗りできるレスキューコスメ",
        "brand_name": "Melvita (メルヴィータ)",
        "capacity": "10ml / ロールオンボトル",
        "type": "携帯型パーツケア美容オイル",
        "features": "オーガニックウチワサボテン種子油、アルガンオイル、ローズヒップ油、ヒマワリ種子油",
        "value": "フランスのオーガニックコスメ認証『エコサート』取得。ひんやりした金属ボールが目元の血行を促しながら、乾燥によるメイク割れを一瞬でリセット",
        "desc_p1": "朝どんなに完璧にスキンケアをして出かけても、冬のオフィスで数時間エアコンの直風を浴びれば、午後には目尻やほうれい線がパサついてファンデーションが割れてしまうもの。そんな冬の緊急事態にポーチに忍ばせておきたいのが、フランス発メルヴィータの『ビオオイル タッチオイル』です。",
        "desc_p2": "スリムなボトル先端に内蔵された金属製ローラーボールが、目元や口元の細かな凹凸にピタッとフィット。クルクルと滑らせるだけで、ウチワサボテンオイルの上質な油分が適量塗布され、乾燥でひび割れそうになった角層を瞬時に潤します。メイクの上から塗ってもファンデーションがドロドロに崩れることなく、光を反射する上品なハイライトのようなツヤが出現。冬の乾燥崩れ対策として、大人の女性に手放せないアイテムです。",
        "target": "日中のオフィスや外出先で目元や口元の乾燥小ジワが気になる方、メイク直しをスマートに完結させたい方、持ち歩きに便利な高品質オーガニックオイルを探している方",
        "point": "日中のメイク直しの際、乾燥が気になる目尻や口角、ほうれい線にローラーを軽く滑らせ、指の腹でトントンと軽く叩き込んで馴染ませます。その上から軽くパウダーを重ねると、朝のメイク立てのようなツヤ感が復活します。"
    },
    {
        "rank": 7,
        "tag": "💨 微細ミストが角層を瞬時にほぐす！モロッコ産サボテンオイル配合の濃密ブースター",
        "catch": "サロン専売品として開発されたウチワサボテンオイル配合の二層式美容ミスト。超微細なミストが真冬の冷風でこわばった肌を瞬時にほぐし、驚異的な柔らかさと満水ツヤをチャージ",
        "brand_name": "CASEEPO (カシーポ)",
        "capacity": "120ml / スプレーボトル",
        "type": "オイルイン高保湿トリートメントミスト",
        "features": "モロッコ産ウチワサボテン種子油、アルガンオイル、植物性スクワラン、ダマスクローズ水、ヒアルロン酸",
        "value": "オイルと化粧水の黄金バランス処方。振ってスプレーするだけで、微細なオイル粒子が角層の奥まで均一に行き渡り、暖房乾燥を寄せ付けないシールドを形成",
        "desc_p1": "プロのヘアメイクアップアーティストやエステサロンで愛用されているカシーポ（CASEEPO）の『Nミスト』。モロッコ現地で厳選された高品質なウチワサボテンオイルとアルガンオイルを、みずみずしいボタニカルウォーターと絶妙なバランスで組み合わせた二層式ミスト美容液です。",
        "desc_p2": "ボトルをシェイクして吹きかけると、霧のように細かく均一なミストが顔全体を包み込みます。一般的な水分だけのミストスプレーは蒸発する際に肌の水分まで奪ってしまいがちですが、本品はサボテンオイルの油分が同時に肌に密着するため、吹きかけた後もしっとりとした潤い膜が持続。洗顔後のファーストステップとしてはもちろん、真冬の入浴後の乾燥防止や、日中のメイクの上からの乾燥リセットとしても驚異的な実力を発揮します。",
        "target": "ミスト化粧水を使うと逆に乾燥してしまう経験がある方、手軽に顔全体にサボテンオイルの潤いを補給したい方、サロン品質の高機能ブースターを求める方",
        "point": "使用前にボトルをよく振り、顔から20cmほど離して円を描くように3〜4プッシュ吹きかけます。その後、手のひらで顔全体を優しく包み込んでハンドプレスし、オイルと水分を角層に密着させてください。"
    },
    {
        "rank": 8,
        "tag": "🔬 低温圧搾ピュア100%原液！ステロールとオメガ6が冬のひび割れ肌を集中リペア",
        "catch": "自然化粧品研究所が誇る完全無添加・未精製ウチワサボテン種子オイル。余計な成分を一切加えず、砂漠植物の生命力そのものを手持ちのスキンケアにプラスできる高機能原液",
        "brand_name": "自然化粧品研究所",
        "capacity": "10ml / 遮光スポイト瓶",
        "type": "高純度未精製植物オイル原液",
        "features": "未精製オプンチアフィクスインジカ種子油100%、高濃度リノール酸、ビタミンE（α・γトコフェロール）、カンペステロール",
        "value": "国内自社充填の徹底した品質管理。普段使っている手持ちの化粧水や乳液に1滴混ぜるだけで、真冬の極上高保湿コスメへとグレードアップ",
        "desc_p1": "成分に妥協したくないスキンケアマニアから絶大な信頼を集める自然化粧品研究所の『未精製ウチワサボテン種子オイル』。モロッコの契約農家から直輸入された種子を、熱を一切加えないコールドプレスで絞り出し、国内のクリーンルームで丁寧にボトリングされています。",
        "desc_p2": "未精製ならではの深みのある黄金色と、香ばしいナッツのような自然な香りが高純度の証。肌に伸ばすとスッとなじんでサラサラの感触に変わり、乾燥で硬くなった皮膚の柔軟性が劇的に回復します。ステロールが肌バリアのラメラ構造を整え、オメガ6脂肪酸が水分の蒸散を徹底的にガード。お気に入りのクリームや乳液に1滴混ぜて使うこともでき、冬のカスタマイズ美容液として極めて高い費用対効果を誇ります。",
        "target": "成分の純度や製法にこだわりたい本物志向の方、手持ちのスキンケアの保湿力を簡単に底上げしたい方、未精製オイルの高い抗酸化力を実感したい方",
        "point": "洗顔後すぐに1滴を顔全体に馴染ませるか、夜のスキンケアの最後に使用する乳液やクリームに1〜2滴混ぜて手のひらで練り合わせてから塗布します。首筋やデコルテまで伸ばすと、冬の首の小ジワ防止にも効果的です。"
    },
    {
        "rank": 9,
        "tag": "🌿 サボテンの潤いで全身を包み込む！真冬の粉吹きボディをしっとり滑らかに保つ乳液",
        "catch": "サボテンシードオイルとサボテンエキスを高濃度配合した贅沢ボディローション。真冬の寒冷と暖房で粉を吹きやすいすねや腕を、上質なモロッカンガーデンの香りとみずみずしい潤いで包む",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "300ml / ディスペンサーポンプ",
        "type": "高保湿パフュームボディローション",
        "features": "サボテンエキス、サボテンシードオイル、オリーブ油、セージ葉エキス、ブラッククミン種子油",
        "value": "大容量300mlで冬の全身をリッチにケア。乳液のように軽やかなのに、サボテンの保水ヴェールが翌日の入浴時まで粉吹きやカサつきをシャットアウト",
        "desc_p1": "冬になると顔だけでなく、すねや背中、腕が乾燥して白く粉を吹き、タイツやインナーを脱ぐときに粉が舞って痒くなる…そんな冬のボディ乾燥に悩む方に最適なのが、ハクスリーの『ボディローション モロッカンガーデナー』です。ハクスリーのアイコンである爽やかで深みのあるボタニカルの香りを全身に纏いながら、本格的なスキンケア級の高保湿を叶えます。",
        "desc_p2": "ポンプから出すとなめらかなミルク状のテクスチャーで、肌に乗せると体温でするりと伸びて素早く浸透。表面にベタベタした油膜を残さないため、塗ってすぐにパジャマや衣類を着ても張り付くストレスが全くありません。サボテンエキスとサボテンシードオイルが角質層の水分をガッチリとホールドし、真冬の乾燥で硬くなったすねや肘のガサつきをなめらかなツヤ肌へと整えます。",
        "target": "冬になると全身が乾燥して粉を吹いたり痒みが出る方、ベタつかず高保湿なボディミルクを探している方、上質な香りで優雅なボディケアを楽しみたい方",
        "point": "冬のお風呂上がり、タオルで軽く水気を拭き取った直後の湿り気が残る肌に適量を伸ばします。特に乾燥しやすいすね・かかと・肘には、重ねづけをして手のひらで温めるように包み込むと、翌朝までしっとり柔肌が持続します。"
    },
    {
        "rank": 10,
        "tag": "✨ べたつかずシルキーなツヤ！サボテンオイル×アーモンド油が叶える極上ボディオイル",
        "catch": "サボテンシードオイル、スイートアーモンド油、ローズヒップ油をブレンドしたプレミアムボディオイル。真冬の冷えで血行が滞った身体をしっとりほぐし、上品な光沢感を演出",
        "brand_name": "Huxley (ハクスリー)",
        "capacity": "100ml / ガラスボトル",
        "type": "高純度プレミアムボディオイル",
        "features": "サボテンシードオイル、スイートアーモンド油、ローズヒップ油、ひまわり種子油",
        "value": "オイル特有の重さを削ぎ落としたライトドライオイル処方。濡れた肌にもサッとなじみ、冬の乾燥ボディをシルクのような滑らかさへと導く",
        "desc_p1": "真冬のボディケアにおいて、クリームやローションだけでは物足りないと感じる乾燥肌のために設計されたハクスリーの『ボディオイル モロッカンガーデナー』。過酷なモロッコ砂漠のサボテンシードオイルをベースに、肌を柔らかく整える植物オイルを黄金比で配合した贅沢なトリートメントオイルです。",
        "desc_p2": "オイルとは思えないほどサラリとしたシルキーな感触で、肌に伸ばすとスーッと馴染んでベタつきを一切残しません。塗った直後から肌表面に繊細な光沢ツヤが宿り、くすんで見えがちな冬の素肌がいきいきとした健康的な輝きを取り戻します。入浴直後の濡れた肌に馴染ませれば、水分をギュッと閉じ込めるインバスケアとしても大活躍。モロッコの青々とした庭園を思わせる豊かな香りが一日中ふんわりと持続します。",
        "target": "乾燥で身体のツヤやハリが失われていると感じる方、重いボディオイルのベタつきが苦手な方、お風呂上がりの保湿ケアを贅沢なリラクゼーションにしたい方",
        "point": "入浴後、軽く水滴を払った肌に適量を手にとり、足首から太もも、手先から肩に向かってリンパを流すようにマッサージしながら馴染ませます。毛先のパサつきが気になる時は、手のひらに残ったオイルをヘアオイル代わりに馴染ませるのもおすすめです。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "ウチワサボテンオイルとアルガンオイルは、具体的に何が違うのですか？",
        "a": "ウチワサボテン種子オイルは、アルガンオイルの約1.6倍の天然ビタミンE（トコフェロール）と、約60%以上の豊富なリノール酸（オメガ6）を含有しています。アルガンオイルがオレイン酸を多く含み皮脂に近いバリアを作るのに対し、ウチワサボテンオイルはより角層への浸透速度が速く、抗酸化力と角質柔軟化（エモリエント）作用が極めて高いのが特徴です。そのため、真冬の硬直した肌や乾燥小ジワに対して、より劇的なふっくら感をもたらします。"
    },
    {
        "q": "オイル美容液を使うと、日中に日焼けしやすくなったり酸化しませんか？",
        "a": "ウチワサボテンオイルは天然の抗酸化成分（ビタミンEやポリフェノール）が極めて豊富に含まれており、植物オイルの中でも非常に酸化安定性が高いのが特徴です。紫外線による油焼けの心配もなく、むしろ日中の冷風や乾燥ストレスから肌細胞を守るシールドとして朝のメイク前にも安心してお使いいただけます。"
    },
    {
        "q": "11月〜12月のスキンケアで、ウチワサボテンコスメを取り入れるおすすめの順番は？",
        "a": "アイテムの形状に合わせて使い分けます。ハクスリーのトナー（化粧水）で肌pHを整えた後、オイルエッセンスまたは100%原液オイルを2〜3滴馴染ませて角層をほぐし、最後にモアザンモイストクリームで蓋をするライン使いが最強の砂漠肌脱出ルートです。日中の外出時はタッチオイル（ロールオン）を目元や口元に携帯すると一日中乾燥割れを防げます。"
    },
    {
        "q": "脂性肌（オイリー肌）やニキビができやすい肌でも使えますか？",
        "a": "非常に適しています。サボテンシードオイルはノンコメドジェニック性の高いサラッとしたオイルで、毛穴を詰まらせにくい組成です。また、冬の皮脂過剰は肌内部の水分不足（インナードライ）が原因であることが多いため、サボテンの水分と油分をバランス良く補給することで皮脂分泌が正常化し、大人ニキビの予防にもつながります。"
    }
]

# HTML テーブル行生成
table_rows = []
for it in items:
    r = it["rank"]
    p_info = next((p for p in product_details if p["rank"] == r), None)
    type_name = p_info["type"] if p_info else "高保湿コスメ"
    brand = it["brand"]
    name = it["display_name"].split(" (")[0]
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    
    row = f"""
    <tr>
      <td class="rank-num rank-{r}">{r}位</td>
      <td class="product-thumb"><a href="{url}" target="_blank" rel="nofollow noopener"><img src="{img}" alt="{name}" loading="lazy" width="80" height="80"></a></td>
      <td class="product-name-cell">
        <span class="product-brand">{brand}</span>
        <a href="{url}" target="_blank" rel="nofollow noopener" class="table-prod-link">{name}</a>
      </td>
      <td><span class="type-badge">{type_name}</span></td>
      <td class="product-price">{price}</td>
      <td><a href="{url}" target="_blank" rel="nofollow noopener" class="table-btn">楽天で見る</a></td>
    </tr>
    """
    table_rows.append(row)

table_joined = "\n".join(table_rows)

# 商品カード生成
cards = []
for it in items:
    r = it["rank"]
    p = next((x for x in product_details if x["rank"] == r), product_details[0])
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    shop = it["shop_name"]
    rate = it["review_rate"]
    reviews = it["review_count"]
    
    card = f"""
    <article class="product-card" id="rank-{r}">
      <div class="card-header">
        <div class="rank-badge rank-{r}">第{r}位</div>
        <div class="card-titles">
          <span class="card-tag">{p['tag']}</span>
          <h3 class="card-name">{it['display_name']}</h3>
        </div>
      </div>
      
      <p class="card-catch"><strong>【注目ポイント】</strong> {p['catch']}</p>
      
      <div class="card-body">
        <div class="card-image-box">
          <a href="{url}" target="_blank" rel="nofollow noopener">
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="product-img">
          </a>
          <div class="card-price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">{price}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <div class="card-review-box">
            <span class="star-rating">★ {rate}</span>
            <span class="review-count">({reviews}件のレビュー)</span>
          </div>
          <a href="{url}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="review-text-box">
            <h4>💡 美容皮膚・テクスチャー詳細レビュー</h4>
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          
          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ：</strong> {p['target']}
          </div>
          
          <div class="point-box">
            <strong>✨ 11-12月の効果的な使い方テクニック：</strong> {p['point']}
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML 生成
faq_items = []
for f in faqs:
    faq_html = f"""
    <div class="faq-item">
      <h3 class="faq-q"><span class="faq-q-badge">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="faq-a-badge">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(faq_html)

faqs_joined = "\n".join(faq_items)

# 全体HTMLテンプレート（サボテン・モロッカンに合わせたオリーブグリーン・サンドベージュ系デザイン）

schema_items = []
for idx, it in enumerate(items, 1):
    schema_items.append({
        "@type": "ListItem",
        "position": idx,
        "name": it["display_name"],
        "url": f"https://lumi-cosme.vercel.app/winter-prickly-pear#rank-{it['rank']}",
        "image": it["image"]
    })

schema_faq = []
for f in faqs:
    schema_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！アルガンオイルを超えるビタミンEと保水力で冬の乾きを満たす高保湿ウチワサボテンオイルコスメランク10",
            "description": "11月・12月の木枯らしと過酷なエアコン乾燥による肌しぼみを救う高保湿ウチワサボテンオイルコスメを徹底厳選！ハクスリー、CODINA、メルヴィータまで厳選。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！アルガンオイルを超えるビタミンEと保水力で冬の乾きを満たす高保湿ウチワサボテンオイルコスメランク10",
            "description": "11月・12月の木枯らしと過酷なエアコン乾燥による肌しぼみを救う高保湿ウチワサボテンオイルコスメを徹底厳選！ハクスリー、CODINA、メルヴィータまで厳選。",
            "image": items[0]["image"],
            "datePublished": "2026-11-04T19:00:00+09:00",
            "dateModified": "2026-11-04T19:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://lumi-cosme.vercel.app/winter-prickly-pear"
        },
        {
            "@type": "FAQPage",
            "mainEntity": schema_faq
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！アルガンオイルを超えるビタミンEと保水力で冬の乾きを満たす高保湿ウチワサボテンオイルコスメランク10 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の過酷な木枯らしと暖房乾燥による肌しぼみを救う高保湿ウチワサボテンオイルコスメを徹底厳選！Huxley（ハクスリー）、CODINA、メルヴィータ、自然化粧品研究所まで、楽天市場で買える本物の高保湿10選を詳しく解説。">
  <meta name="keywords" content="ウチワサボテンオイル,サボテンシードオイル,ハクスリー Huxley,冬 高保湿 美容液,11月 コスメ,12月 コスメ,乾燥肌 オイル美容液,ビタミンE 保湿">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-prickly-pear">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2d6a4f;
      --primary-dark: #1b4332;
      --primary-light: #d8f3dc;
      --accent: #d4a373;
      --text-main: #212529;
      --text-sub: #495057;
      --text-light: #6c757d;
      --bg-page: #f8f9fa;
      --bg-card: #ffffff;
      --border-color: #e9ecef;
      --shadow-sm: 0 2px 4px rgba(45, 106, 79, 0.05);
      --shadow-md: 0 4px 12px rgba(45, 106, 79, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(45, 106, 79, 0.15);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      padding-bottom: 4rem;
    }}

    .site-header {{
      background: linear-gradient(135deg, #1b4332 0%, #2d6a4f 50%, #40916c 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem 2.8rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(27, 67, 50, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #d8f3dc;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .header-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 0.8rem;
    }}
    .site-title {{
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.15);
      max-width: 920px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #e8f5e9;
      max-width: 820px;
      margin: 0 auto;
    }}

    .main-container {{
      max-width: 1040px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .toc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.6rem;
    }}
    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s ease;
    }}
    .toc-list a:hover {{ color: var(--primary); text-decoration: underline; }}

    .intro-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .intro-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}
    .intro-section p {{
      margin-bottom: 1.2rem;
      color: var(--text-sub);
      font-size: 1rem;
    }}
    .intro-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}
    .intro-card {{
      background: #f1f8f4;
      border-left: 4px solid var(--primary);
      padding: 1.2rem;
      border-radius: var(--radius-sm);
    }}
    .intro-card h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}
    .intro-card p {{
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-bottom: 0;
    }}

    .table-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2rem 1.5rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
      overflow-x: auto;
    }}
    .table-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 680px;
    }}
    .compare-table th, .compare-table td {{
      padding: 1rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
      vertical-align: middle;
    }}
    .compare-table th {{
      background: #e8f5e9;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    .rank-num {{
      font-weight: 800;
      font-size: 1.1rem;
      white-space: nowrap;
    }}
    .rank-1 {{ color: #2d6a4f; }}
    .rank-2 {{ color: #1b4332; }}
    .rank-3 {{ color: #40916c; }}
    .product-thumb img {{
      border-radius: 6px;
      object-fit: cover;
      display: block;
      border: 1px solid #c8e6c9;
    }}
    .product-name-cell {{ min-width: 220px; }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-light);
      margin-bottom: 0.2rem;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: block;
    }}
    .table-prod-link:hover {{ color: var(--primary); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      background: #e8f5e9;
      color: var(--primary-dark);
      font-size: 0.75rem;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-weight: 600;
    }}
    .product-price {{
      font-weight: 800;
      color: #b91c1c;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s ease;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border-color);
      scroll-margin-top: 2rem;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.2rem;
      margin-bottom: 1.2rem;
      border-bottom: 1px dashed var(--border-color);
      padding-bottom: 1rem;
    }}
    .rank-badge {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
      color: #ffffff;
      font-size: 1.25rem;
      font-weight: 800;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      box-shadow: 0 2px 6px rgba(45, 106, 79, 0.3);
    }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.3rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      line-height: 1.4;
      color: var(--text-main);
    }}
    .card-catch {{
      background: #f1f8f4;
      border-left: 4px solid var(--primary);
      padding: 0.8rem 1rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.5rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    }}

    .card-body {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img, .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-md);
      border: 1px solid #c8e6c9;
      margin-bottom: 1rem;
      transition: transform 0.2s ease;
    }}
    .card-img:hover {{ transform: scale(1.02); }}
    .card-price-box {{
      margin-bottom: 0.6rem;
    }}
    .price-label {{
      font-size: 0.8rem;
      color: var(--text-light);
      display: block;
    }}
    .price-val {{
      font-size: 1.6rem;
      font-weight: 800;
      color: #b91c1c;
    }}
    .price-tax {{
      font-size: 0.8rem;
      color: var(--text-light);
    }}
    .card-review-box {{
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
    }}
    .star-rating {{ color: #d4a373; font-weight: 700; }}
    .card-aff-btn, .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #2d6a4f 0%, #1b4332 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-sm);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      box-shadow: 0 4px 10px rgba(27, 67, 50, 0.2);
      transition: all 0.2s ease;
    }}
    .card-aff-btn:hover, .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(27, 67, 50, 0.3);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      margin-bottom: 1.5rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.8rem;
      border-bottom: 1px solid var(--border-color);
      text-align: left;
    }}
    .spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      background: #f1f8f4;
      font-weight: 700;
    }}
    .review-text-box {{
      background: #fdfdfd;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1.25rem;
      margin-bottom: 1.2rem;
    }}
    .review-text-box h4 {{
      font-size: 1rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}
    .review-text-box p {{
      font-size: 0.92rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
      line-height: 1.7;
    }}
    .review-text-box p:last-child {{ margin-bottom: 0; }}
    .target-box, .point-box {{
      background: #f1f8f4;
      padding: 0.8rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}
    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
    }}

    .guide-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}
    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 1.2rem;
    }}
    .step-list {{
      counter-reset: step;
      list-style: none;
      display: grid;
      gap: 1rem;
    }}
    .step-item {{
      background: #f1f8f4;
      border-radius: var(--radius-sm);
      padding: 1.2rem 1.2rem 1.2rem 3.5rem;
      position: relative;
    }}
    .step-item::before {{
      counter-increment: step;
      content: counter(step);
      position: absolute;
      left: 1.2rem;
      top: 1.2rem;
      background: var(--primary);
      color: #ffffff;
      width: 1.8rem;
      height: 1.8rem;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 0.9rem;
    }}
    .step-item h3 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}
    .step-item p {{
      font-size: 0.9rem;
      margin-bottom: 0;
    }}

    .faq-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border-color);
      padding: 1.2rem 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      margin-bottom: 0.6rem;
    }}
    .faq-q-badge {{
      background: var(--primary);
      color: #ffffff;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      color: var(--text-sub);
      font-size: 0.93rem;
    }}
    .faq-a-badge {{
      background: #c8e6c9;
      color: #1b4332;
      padding: 0.1rem 0.5rem;
      border-radius: 4px;
      font-size: 0.85rem;
      font-weight: 700;
    }}

    .related-links-section {{
      background: var(--bg-card);
      border-radius: var(--radius-md);
      padding: 2.5rem 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .related-links-section h2 {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #fdfdfd;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 1rem;
      text-decoration: none;
      transition: all 0.2s ease;
      display: block;
    }}
    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
      border-color: var(--primary);
    }}
    .related-card h3 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.4;
    }}
    .related-card p {{
      font-size: 0.8rem;
      color: var(--text-light);
      margin-bottom: 0;
      line-height: 1.5;
    }}

    .site-footer {{
      background: #1b4332;
      color: #d8f3dc;
      text-align: center;
      padding: 3rem 1.5rem;
      font-size: 0.85rem;
      margin-top: 4rem;
    }}
    .site-footer a {{
      color: #c8e6c9;
      text-decoration: none;
      margin: 0 0.5rem;
    }}
    .site-footer a:hover {{ text-decoration: underline; }}
  </style>

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="/">🏠 Lumi Cosme ホームに戻る</a>
    </div>
    <span class="header-badge">2026-2027 冬の砂漠肌レスキュー特集</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！<br>アルガンオイルを超えるビタミンEと保水力で冬の乾きを満たす高保湿ウチワサボテンオイルコスメランク10</h1>
    <p class="site-subtitle">11月〜12月の木枯らしと過酷なエアコン乾燥でしぼみきった肌へ。40度を超える酷暑と極寒のモロッコ砂漠を生き抜くウチワサボテン種子の驚異的な生命力が、アルガンオイルの1.6倍のビタミンEと高濃度リノール酸で角層細胞をふっくら満水へ導く幻のオイルコスメを徹底比較！</p>
  </header>

  <main class="main-container">

    <!-- 目次 -->
    <nav class="toc-box">
      <h2 class="toc-title">📑 本記事の目次（タップで各商品へスキップ）</h2>
      <ul class="toc-list">
        <li><a href="#intro">🌵 なぜアルガンを超えるのか？ウチワサボテンオイルの秘密</a></li>
        <li><a href="#table">📊 高保湿ウチワサボテンコスメ10選 スペック比較表</a></li>
        <li><a href="#rank-1">第1位：ハクスリー オイルエッセンス エッセンスライク オイルライク</a></li>
        <li><a href="#rank-2">第2位：ナチュラルモロッコ オーガニック ウチワサボテンオイル 30ml</a></li>
        <li><a href="#rank-3">第3位：ハクスリー クリーム モアザンモイスト 50ml</a></li>
        <li><a href="#rank-4">第4位：コディナ ウチワサボテンオイル 10ml</a></li>
        <li><a href="#rank-5">第5位：ハクスリー トナー エクストラクトイット 120ml</a></li>
        <li><a href="#rank-6">第6位：メルヴィータ ビオオイル タッチオイル 10ml</a></li>
        <li><a href="#rank-7">第7位：カシーポ Nミスト オーガニックサボテン美容液 120ml</a></li>
        <li><a href="#rank-8">第8位：自然化粧品研究所 未精製ウチワサボテン種子オイル 10ml</a></li>
        <li><a href="#rank-9">第9位：ハクスリー ボディローション モロッカンガーデナー 300ml</a></li>
        <li><a href="#rank-10">第10位：ハクスリー ボディオイル モロッカンガーデナー 100ml</a></li>
        <li><a href="#guide">💡 サボテンオイルで真冬の肌密度を高めるプロの使いこなし術</a></li>
        <li><a href="#faq">❓ よくある質問と皮膚科学的回答</a></li>
      </ul>
    </nav>

    <!-- 導入解説 -->
    <section class="intro-section" id="intro">
      <h2>🌵 アルガンオイルを超える驚異の保水力！なぜウチワサボテンが冬に選ばれるのか？</h2>
      <p>11月・12月を迎えると、空気中の水分が極端に減少し、さらに室内では暖房の乾いた温風が吹き荒れます。この環境下で起きるのが、角質層の水分が蒸発して皮膚が硬く縮こまり、どんな高価な化粧水やクリームを塗っても弾かれて浸透しない『角質硬化とインナードライの悪循環』です。</p>
      <p>この真冬の難問を打開する鍵として、世界中の美容家や皮膚科医から『奇跡のエイジングケアオイル』と称賛されているのが、モロッコ産『ウチワサボテン種子オイル（オプンチアフィクスインジカ種子油）』です。1トンのウチワサボテン果実から採れる種子はわずか数キロ、そこから絞り出されるオイルは1リットルにも満たないという、極めて希少価値の高い植物オイルです。</p>
      
      <div class="intro-grid">
        <div class="intro-card">
          <h3>🥑 1. アルガンオイルの約1.6倍の天然ビタミンE</h3>
          <p>強力な抗酸化作用を持つ天然トコフェロール（ビタミンE）をアルガンオイルの約1.6倍、オリーブオイルの約400倍も含有。冬の冷気と乾燥による肌細胞の酸化ストレスを食い止め、ふっくらとしたハリと弾力を取り戻します。</p>
        </div>
        <div class="intro-card">
          <h3>💧 2. 60%以上の高濃度リノール酸による角層柔軟化</h3>
          <p>オメガ6系必須脂肪酸であるリノール酸を豊富に含み、寒さで硬直した角質細胞の間に入り込んでラメラ構造を柔らかくほぐします。水分保持力を根本から底上げし、化粧水がグングン吸い込まれる肌土台を再構築します。</p>
        </div>
        <div class="intro-card">
          <h3>✨ 3. オイル特有のベタつきを一切感じさせない高浸透</h3>
          <p>皮脂に近い植物性ステロールを多く含むため、肌への親和性が極めて高く、塗布した瞬間にサラリと吸い込まれるように浸透。朝のメイク前に使ってもファンデーションを崩さず、一日中内側から発光する水光ツヤを保ちます。</p>
        </div>
      </div>
    </section>

    <!-- 比較表 -->
    <section class="table-section" id="table">
      <h2>📊 高保湿ウチワサボテンコスメ10選 スペック徹底比較表</h2>
      <p style="font-size:0.9rem; color:var(--text-sub); margin-bottom:1rem;">※楽天市場公式取扱店・直営店の最新参考価格（税込）を表示しています。各商品リンクより現在のポイント還元率や在庫状況をご確認いただけます。</p>
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>商品名 / ブランド</th>
            <th>アイテム分類</th>
            <th>参考価格</th>
            <th>楽天詳細</th>
          </tr>
        </thead>
        <tbody>
          {table_joined}
        </tbody>
      </table>
    </section>

    <!-- 商品カード一覧 -->
    <section class="products-section">
      {cards_joined}
    </section>

    <!-- 効果的な使い方ガイド -->
    <section class="guide-section" id="guide">
      <h2>💡 サボテンオイルで真冬の肌密度を高めるプロの使いこなし3大テクニック</h2>
      <p>希少なウチワサボテンオイルのポテンシャルを余すところなく引き出し、真冬の暖房下でも乾かないシルク肌を完成させるためのテクニックです。</p>
      
      <div class="step-list">
        <div class="step-item">
          <h3>ステップ1：洗顔直後の『プレオイル』で硬直した角層をほぐす</h3>
          <p>冬の寒さで冷え固まった肌は、水分を弾いてしまいます。洗顔後すぐにウチワサボテンオイル（原液またはハクスリーのオイルエッセンス）を1滴、手のひらで温めてから馴染ませてください。高濃度リノール酸が角層細胞をふんわり柔軟化し、その後に重ねる化粧水の吸い込みが劇的にアップします。</p>
        </div>
        <div class="step-item">
          <h3>ステップ2：弱酸性トナーの『重ねづけ』で細胞を満水状態に</h3>
          <p>精製水の代わりにサボテンエキスを贅沢に配合した弱酸性化粧水（ハクスリー トナー）を、手のひらで優しく2〜3回重ねづけ。サボテン由来の天然多糖類が水分をがっちりホールドし、角層のすみずみまで満水状態をキープします。</p>
        </div>
        <div class="step-item">
          <h3>ステップ3：高密度クリームによる『高気密シーリング』</h3>
          <p>水分と美容成分を閉じ込めるため、サボテンエキスと植物性セラミドを凝縮した高密度クリーム（ハクスリー モアザンモイスト）をハンドプレスで密着。バターのようにとろけた保護膜が、真冬の冷風やエアコンの直風から肌バリアを鉄壁ガードします。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="faq-section" id="faq">
      <h2>❓ ウチワサボテンオイルコスメに関するよくある質問（FAQ）</h2>
      {faqs_joined}
    </section>

    <!-- 内部リンク -->
    <section class="related-links-section">
      <h2>🔗 あわせて読みたい！冬の徹底保湿・エイジングケア特集</h2>
      <div class="related-grid">
        <a href="/winter-manuka-honey" class="related-card">
          <h3>🍯 高純度マヌカハニーコスメ厳選10</h3>
          <p>野生マヌカ花の驚異的なMGO抗菌力と蜜膜！冬のひび割れ・皮むけ・ガサガサ角層を救う最高峰コスメ特集。</p>
        </a>
        <a href="/winter-resurrection-plant" class="related-card">
          <h3>🌵 復活草・トレハロースコスメ厳選10</h3>
          <p>砂漠の極限乾燥を生き抜くテマリカヒバの驚異的な保水力！冬の干からびた肌細胞を満水へ導く名品まとめ。</p>
        </a>
        <a href="/winter-argan-oil" class="related-card">
          <h3>🌰 高保湿アルガンオイルコスメ厳選10</h3>
          <p>モロッコの黄金と呼ばれる伝統オイル。オレイン酸とビタミンEが冬の乾燥肌にしっとり馴染む名品集。</p>
        </a>
        <a href="/winter-marula-oil" class="related-card">
          <h3>🐘 奇跡のマルラオイルコスメ厳選10</h3>
          <p>アフリカの過酷な大地が生んだ奇跡のオイル！アルガンを凌ぐ抗酸化力と浸透力で冬のハリ艶を呼び戻す。</p>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <p>&copy; 2026-2027 Lumi Cosme (ルミコスメ) - 冬の乾燥対策・高保湿スキンケア専門ガイド</p>
    <p style="margin-top:0.5rem;">
      <a href="/">トップページ</a> | 
      <a href="/winter-prickly-pear">ウチワサボテンオイル</a> | 
      <a href="/winter-manuka-honey">マヌカハニー</a> | 
      <a href="/winter-resurrection-plant">復活草コスメ</a> | 
      <a href="/winter-beta-glucan">ベータグルカン</a>
    </p>
  </footer>

</body>
</html>
"""

with open("winter-prickly-pear.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-prickly-pear.html successfully!")
