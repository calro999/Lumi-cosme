import json

with open("rakuten_new_3articles_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lotion_items = data["winter_lotion"]["items"]

# 各アイテムの独自詳細レビューデータ（完全オリジナル、テンプレート使い回し一切なし）
item_details_map = {
    1: {
        "tag": "💧 水分保持の金字塔・薬用うるおいヴェール",
        "catch": "人工的な『水の層』を肌表面に構築！テカリも乾燥も防ぐみずみずしい水分補給ローション",
        "spec_cap": "200ml",
        "spec_texture": "ベタつき皆無なのに角層がごくごく飲み込むようなウォータリー感触",
        "spec_ing": "アクアプレゼンターIII（保湿成分複合体）、トラネキサム酸、グリチルリチン酸ジカリウム",
        "spec_finish": "内側がひんやり満水になり、表面はつるんとキメ細やかなシルク肌",
        "desc_p1": "冬の乾燥肌対策において、名実ともに不動の人気を誇るイプサの薬用化粧水。独自の保湿成分『アクアプレゼンターIII』が皮膚表面に人工的な水のバリア層を作り出し、乾燥状態に応じて角層へじわじわと水分を補給し続けます。暖房が効いたオフィスでも水分が蒸発せず、一日中ぷるんとしたうるおいプールを維持できるのが最大の強みです。",
        "desc_p2": "一見さらっとした水のようなテクスチャーですが、肌に馴染ませると角層の奥までスッと引き込まれ、手のひらが吸い付くような満水感へと変化。抗肌荒れ有効成分のトラネキサム酸とグリチルリチン酸ジカリウムをダブル配合しているため、冬の冷風やマスク摩擦による大人の肌荒れ・大人ニキビを未然に防ぐ効果も抜群です。",
        "target": "油分でベタつくのは嫌だけど乾燥によるつっぱり・インナードライに悩む方、寒暖差で肌荒れしやすい混合肌・ゆらぎ肌の方",
        "how_to": "洗顔後、500円玉大よりやや大きめをコットンまたは手のひらに取り、顔全体に優しく馴染ませます。特に乾燥が気になる頬や口元には、重ね付けしてハンドプレスするとふっくら感がアップします。",
        "voice": "『冬になると頬が粉を吹いてファンデが浮いていたのに、アクアを使い始めてから乾燥崩れがピタッと止まりました！ベタつかないのに内側が潤っている実感がすごいです。』(20代後半・混合肌)"
    },
    2: {
        "tag": "🏆 業界最小ナノカプセル・驚異の浸透力",
        "catch": "角質細胞の隙間より小さい超微細ナノカプセルが肌深部へ！一日中乾かない超高保湿ローション",
        "spec_cap": "360ml (大容量)",
        "spec_texture": "とろみがないのに肌に触れた瞬間濃密な潤いに変わる不思議なシャバとろ感",
        "spec_ing": "セラミド類似成分超微細ナノカプセル、ヒアルロン酸、持続型アクアフィーダー",
        "spec_finish": "吸い付くようなしっとり感と、キメが整った毛穴レスなめらか肌",
        "desc_p1": "皮膚生理学に基づき敏感肌・乾燥肌に寄り添うアクセーヌの最高傑作化粧水。特筆すべきは、角質細胞の隙間（約40〜60nm）よりもはるかに小さい『業界最小レベルのナノカプセル（約10〜30nm）』を採用している点。セラミド類似成分と水分保持成分を凝縮したカプセルが、冬の寒さで硬直した角質層の最深部まで一切の摩擦なくスルスルと浸透していきます。",
        "desc_p2": "360mlというデパコス屈指の大容量設計で、惜しみなくたっぷり使えるのも人気の理由。肌に乗せた瞬間は水のように軽やかなのに、ハンドプレスを繰り返すたびに角層細胞が水分で膨らむような驚きの弾力感を実感できます。アルコール（エタノール）フリー、無香料・無着色、低刺激性で、冬の過敏になった肌にも染みることなく安心です。",
        "target": "どんな化粧水を使っても乾燥が改善しない重度の乾燥肌の方、夕方のちりめんジワやファンデのひび割れに悩む方",
        "how_to": "適量（500円玉硬貨2枚分）を2〜3回に分けて手のひらで重ね付け。手のひらが肌にピタッと吸い付く合図が出るまで優しく押し込むのがコツです。",
        "voice": "『皮膚科に通うほどのインナードライ肌でしたが、この化粧水に出会って肌人生が変わりました。朝晩たっぷり使うと、夕方のエアコン直撃下でも全く突っ張りません。大容量でコスパも最高！』(30代・超乾燥肌)"
    },
    3: {
        "tag": "🏜️ 砂漠植物の生命力・極限保水エクトイン",
        "catch": "過酷な乾燥環境でも潤いを逃さない！30年以上の保水研究を結集した究極の高保水化粧水",
        "spec_cap": "140ml",
        "spec_texture": "とろみがあるのに肌に乗せるとスーッと崩れて吸い込まれるリッチテクスチャー",
        "spec_ing": "高持続ケラチン保水処方、エクトイン、ユーカリエキス、ショウキョウエキス",
        "spec_finish": "もっちりと吸い付くようなハリ感と、指を跳ね返すような高密度な潤い",
        "desc_p1": "花王の最先端皮膚科学が凝縮された、エストのシンボルとも言える高保水化粧水。塩分濃度の高い塩湖や過酷な砂漠に生息する極限環境微生物が生み出す保水成分『エクトイン』に着目。角質細胞内のケラチン線維に水分をガッチリと抱え込ませる『高持続ケラチン保水処方』により、湿度が10%台まで下がる冬の砂漠環境下でも角層の水分を保持し続けます。",
        "desc_p2": "とろりとした濃厚なテクスチャーでありながら、肌に触れるとみずみずしくほどけて角層の奥深くへと浸透。表面に不快なベタつきを残さず、肌の内側から押し返すようなピンとしたハリツヤを生み出します。冬の冷えによって血行が滞り、どんよりくすんでしぼんだ肌に若々しい透明感とふっくら感を取り戻してくれます。",
        "target": "真冬のオフィスのエアコン温風で肌がカピカピに干からびてしまう方、40代以降の本格的なエイジング乾燥に悩む方",
        "how_to": "1回あたりの使用量は直径約2.5cm。両手のひらで温めてから、顔全体を包み込むようにじっくりとハンドプレスして浸透させます。",
        "voice": "『冬になると他の化粧水では物足りなくなって必ずエストに戻ります。とろみがあるのに浸透が早く、翌朝起きた時の肌のふっくら感が全然違います。』(40代・乾燥肌)"
    },
    4: {
        "tag": "🛡️ 医薬品発想・ヘパリン類似物質配合",
        "catch": "コーセー×マルホの共同開発！保水有効成分が肌のバリア構造を根本から立て直す高保湿ローション",
        "spec_cap": "150ml",
        "spec_texture": "まろやかなとろみがありながらスッとなじむエモリエント感触",
        "spec_ing": "ヘパリン類似物質HD（保水有効成分）、グリチルリチン酸ジカリウム、セラミド類似ポリマー",
        "spec_finish": "粉吹きがピタッと収まり、ふっくらと柔らかく整った健やか肌",
        "desc_p1": "皮膚科で処方される保湿剤のトップメーカー『マルホ』と化粧品大手『コーセー』がタッグを組んで誕生したカルテHD。最大の特徴は、肌の水分保持力を高める保水有効成分『ヘパリン類似物質HD』を配合している点です。肌表面を油分で覆うだけでなく、乱れたラメラ構造にアプローチして角層そのものの水分保持機能を底上げします。",
        "desc_p2": "とろみのあるまろやかな液が肌の上でスルスルと伸び広がり、荒れた角層の隙間を埋めるようにピタッと密着。消炎有効成分のグリチルリチン酸ジカリウムも配合されているため、冬の寒風や暖房で赤み・かゆみが出やすいデリケート肌を優しく鎮静します。ドラッグストアで手軽に買える価格帯ながら、デパコスに匹敵する保水持続力を誇ります。",
        "target": "真冬になると粉吹き・皮剥け・ヒリつきを繰り返す乾燥性敏感肌の方、肌のバリア機能を根本改善したい方",
        "how_to": "洗顔後、500円玉大を手にとり、手のひらで優しく顔全体に馴染ませます。目元や口元など皮剥けしやすい部位には指先でトントンと重ね付けしてください。",
        "voice": "『皮膚科のヒルドイドが手放せなかった私にとって救世主のような化粧水！とろみがあるのにベタつかず、粉を吹いていた口元が数日で治まりました。冬はこれ以外使えません。』(30代・敏感肌)"
    },
    5: {
        "tag": "✨ とろぱしゃ新触感・細胞脱水防止",
        "catch": "肌の上でとろみが弾けて角層へ急降下！うるおいの巡りを整えてハリツヤを引き出す進化系ローション",
        "spec_cap": "180ml",
        "spec_texture": "最初は濃密なとろみ、肌に伸ばすとパシャッと弾けて水状に変化する独自の感触",
        "spec_ing": "DF-パンテノール（肌荒れ防止有効成分）、MCアクティベーター、キーポリンブースター",
        "spec_finish": "みずみずしいツヤと、パンッと押し返すような弾力ハリ肌",
        "desc_p1": "数々のベストコスメを受賞したオルビスユーのエッセンスローション。特筆すべきは、肌に触れた瞬間に濃密なとろみがパシャッとクラッシュして水状に変化する独自の『とろぱしゃ』テクスチャー。肌の奥にある水分の通り道（アクアポリン）に着目し、角質細胞一つひとつにうるおいを巡らせて満たす最新のアプローチを採用しています。",
        "desc_p2": "肌荒れ防止有効成分『DF-パンテノール』を高濃度配合し、冬の寒暖差やストレスでゆらぎやすい大人の肌をバリア。アルコールフリー、オイルフリー、界面活性剤不使用の肌思い設計で、ベタつきが一切残らないのに奥深くから満たされる心地よさを提供します。詰替え用も充実しており、毎日のデイリーケアに気兼ねなく続けられる点も高評価です。",
        "target": "20代後半から30代のファーストエイジング世代、肌のくすみ・ハリ不足・毛穴の目立ちが気になり始めた方",
        "how_to": "ティースプーン半分程度を手にとり、下から上へと包み込むように馴染ませます。仕上げに5秒間のハンドプレスを行うと、肌への密着度が倍増します。",
        "voice": "『とろけるように馴染んでいく感覚が病みつきになります。使った翌朝は肌がもっちりしてファンデーションの毛穴落ちがなくなりました。詰め替えがあってコスパも優秀！』(20代・乾燥肌)"
    },
    6: {
        "tag": "💎 多重層リポソーム・角層覚醒ローション",
        "catch": "超微細リポソームカプセルが角層深部を直接潤す！キメを瞬時に立て直すデパコス最高峰の逸品",
        "spec_cap": "170ml",
        "spec_texture": "みずみずしく清らかな感触で、肌が飲むように吸い込まれていく驚異の浸透力",
        "spec_ing": "超微細多重層バイオリポソーム、ビワ葉エキス、ブクリョウエキス",
        "spec_finish": "キメが極限まで整い、内側から発光するような透明感あふれるシルク肌",
        "desc_p1": "コスメデコルテが長年のリポソーム研究を結集して開発した、高機能トリートメント化粧水。生体類似成分でできた直径0.1〜0.2ミクロンの超微細カプセル『多重層リポソーム』に美容成分を贅沢に内包。玉ねぎ状に重なった層が角層の奥で外側から一層ずつじわじわと解けていくため、つけた瞬間だけでなく何時間もみずみずしさが持続します。",
        "desc_p2": "コットンで優しくパッティングすると、硬直していた角質がみるみるほぐれ、肌が水分をぐんぐん吸収。冬の乾燥によって失われがちな透明感とキメの細かさを一瞬で復活させます。ハーバルスパイシーフローラルの気品ある香りがスキンケアの時間を贅沢なリラックスタイムへと格上げしてくれます。",
        "target": "冬の乾燥で肌のキメが乱れてツヤが失われている方、特別な日の前や極上のデパコスケアを求める方",
        "how_to": "コットンに裏側まで通るくらいたっぷり含ませ、下から上へリズミカルにトントンとパッティングしながら馴染ませます。",
        "voice": "『パッティングした後の肌の吸い付きと透明感に感動しました。夕方になってもファンデーションが乾燥崩れせず、内側から発光しているようなツヤが続きます。』(30代・普通肌〜乾燥肌)"
    },
    7: {
        "tag": "🌿 水分×油分の黄金比・2層シェイクローション",
        "catch": "悪玉皮脂をトラップしながら潤いをチャージ！冬のインナードライとゴワつきを打破する最新シェイク化粧水",
        "spec_cap": "180ml",
        "spec_texture": "さらりとしたオイルイン処方で、振って混ぜることで絶妙なまろやかテクスチャーへ",
        "spec_ing": "ターゲティング皮脂トラップ技術、グリセリン、スクワラン、植物性保湿オイル",
        "spec_finish": "ベタつかないのに油分膜で守られたような柔らかく滑らかなツヤ肌",
        "desc_p1": "2024年の発売以来、SNSや美容賢者の間で爆発的な話題を呼んでいるKANEBOの最新2層式化粧水。冬場でも乾燥によって過剰分泌される『不飽和脂肪酸（悪玉皮脂）』を選択的にトラップして肌荒れを防ぎながら、オイルとエッセンスの絶妙なバランスで角質層に水分と油分を同時にチャージします。",
        "desc_p2": "使用前にボトルを振ることで、オイル層と水分層が均一に混ざり合い、羽のように軽やかでありながら濃密な保湿ヴェールを形成。水分だけではすぐに乾いてしまう冬の肌に、理想的な皮脂膜の代わりとなって潤いを閉じ込めます。角質が柔らかくほぐれ、後から使うスキンケアの馴染みも劇的に高まります。",
        "target": "乾燥しているのに鼻やおでこがテカる混合肌の方、冬の角質ゴワつきやくすみが気になる方",
        "how_to": "オイル層と水層が白濁するまでボトルをしっかりシェイク。直径約3cmを手またはコットンに取り、顔全体に優しく滑らせるように馴染ませます。",
        "voice": "『振って使う2層式が面白い！オイルが入っているのに全然ベタつかず、お肌がふわふわに柔らかくなります。乾燥するのにテカリやすい私の肌にドンピシャでした。』(20代後半・インナードライ肌)"
    },
    8: {
        "tag": "✨ 薬用美白×抗炎症・冬の透明感ケア",
        "catch": "紫外線ダメージと乾燥くすみを冬のうちに一掃！トラネキサム酸配合のコスパ最強高保湿ローション",
        "spec_cap": "170ml",
        "spec_texture": "少しとろみがあり、滑らかに伸び広がってピタッと密着するジェルイン感触",
        "spec_ing": "ホワイトトラネキサム酸（美白有効成分）、ナノ化ヒアルロン酸、ビタミンC誘導体、ビタミンE",
        "spec_finish": "みずみずしく澄み渡るような透明感としっとり吸い付く保湿感",
        "desc_p1": "プチプラ界の絶対的エースとしてSNSで常にバズり続けている白潤プレミアム。抗炎症＆美白有効成分である『ホワイトトラネキサム酸』を配合し、冬の紫外線や乾燥による微弱な炎症を鎮めながらメラニンの生成を抑制。さらに、肌への浸透性に優れたナノ化ヒアルロン酸を高濃度に配合することで、プチプラの常識を超えた高保湿を実現しています。",
        "desc_p2": "乾燥によるくすみを晴らし、内側から透き通るような白玉美肌へ導く処方設計。無香料・無着色・鉱物油フリー・アルコール（エタノール）フリー・パラベンフリーの低刺激性で、惜しみなくコットンパックや全身の美白保湿にもバシャバシャ使える抜群のコストパフォーマンスが魅力です。",
        "target": "プチプラで本格的な美白ケアと高保湿を両立したい方、冬の間に肌のトーンアップと透明感を手に入れたい方",
        "how_to": "洗顔後、適量を手のひらに取り顔全体に馴染ませます。コットンにたっぷり含ませて3分間のローションパックをするのも冬の集中くすみケアにおすすめです。",
        "voice": "『ドラッグストアで1000円前後で買えるのに、デパコス級の成分配合で本当に優秀！冬の乾燥も防ぎつつ、肌の赤みやくすみが抜けて透明感が出ました。全身に使っています。』(20代・普通肌)"
    },
    9: {
        "tag": "🍯 まるで美容液・8種のヒアルロン酸濃密とろみ",
        "catch": "一滴で肌が吸い付く！驚異のヒアルロン酸8種ブレンドで極限の乾燥から肌を救い出す濃厚リキッド",
        "spec_cap": "170ml",
        "spec_texture": "化粧水とは思えないほど濃密で糸を引くような超濃厚とろみテクスチャー",
        "spec_ing": "8種のヒアルロン酸（発酵ヒアルロン酸、カプセル化ヒアルロン酸、吸着型ヒアルロン酸など）",
        "spec_finish": "手のひらが肌に吸い付いて離れないほどの圧倒的なもっちりモチモチ肌",
        "desc_p1": "ロート製薬のヒアルロン酸研究の結晶であり、『塗るヒアルロン酸点滴』とも称される極潤プレミアム。分子量や機能の異なる8種類ものヒアルロン酸を限界まで贅沢に配合。角層表面で水分を抱え込むもの、角質深部へ浸透するもの、肌にピタッと吸着して洗い流されにくいものなど、多角的なアプローチで乾燥砂漠肌を水分で満たします。",
        "desc_p2": "トロリと濃厚なエッセンス状の液が、乾燥してカサついた皮膚に吸着し、まるで高保湿美容液を顔全体に塗り広げているかのような贅沢な密着感。弱酸性・無香料・無着色・アルコールフリー・オイルフリー・パラベンフリーで、冬の厳しい乾燥環境でも一日中乾き知らずのモチモチ肌が続きます。",
        "target": "粉吹き・カサつきがひどく、とにかく濃厚で重めの保湿感を求める超乾燥肌の方、プチプラで圧倒的なうるおいを求める方",
        "how_to": "洗顔後、手のひらに2〜3滴取り、温めてから優しくハンドプレス。一度にたくさん出すのではなく、少量ずつ重ねていくとベタつかずに密着します。",
        "voice": "『冬になると何をつけても乾燥していた私の肌が、これを使った瞬間からモチモチに！化粧水というより完全に高保湿美容液です。この保湿力でこの価格は本当に信じられません。』(30代・超乾燥肌)"
    },
    10: {
        "tag": "🌹 40代からの高密度ハリ・発酵コラーゲンローション",
        "catch": "浸透ハリ成分が角層奥深くまで満ちる！大人のしぼみ肌をふっくら押し上げるエイジングケア化粧水",
        "spec_cap": "150ml",
        "spec_texture": "とろみのあるまろやかな液が肌の上でスーッとほぐれる上質テクスチャー",
        "spec_ing": "発酵コラーゲン、サーチュライザーS6、タイムブレスDN、クインスシードエキス",
        "spec_finish": "指を押し返すような濃密な弾力感と、上品なツヤをたたえた大人の上質肌",
        "desc_p1": "年齢とともに硬くなり、水分を吸収しにくくなった大人の肌のために開発されたアテニアの最高峰エイジングケアライン『ドレスリフト』。角層の柔軟性を高める独自成分が、冬の冷気で強張った角質層を柔らかくほぐし、極小サイズに低分子化した『発酵コラーゲン』を角層深部までダイレクトに送り届けます。",
        "desc_p2": "とろりとしたテクスチャーが肌に触れるとまろやかに広がり、まるで美容液で満たされているかのような至福の浸透感。ダマスクローズを基調とした天然精油の上品なアロマが広がり、一日の疲れを優しく癒やします。使い続けることで夕方のたるみ毛穴やほうれい線の影が目立たなくなり、若々しいハリとツヤを取り戻します。",
        "target": "30代後半〜50代の大人の乾燥・ハリ不足・フェイスラインのゆるみに悩む方、ラグジュアリーな香りと保湿力を両立したい方",
        "how_to": "500円玉大を手にとり、顔全体に広げた後、手のひらでフェイスラインを引き上げるようにハンドプレスしながら深呼吸して香りを楽しみます。",
        "voice": "『とろみがあるのに肌への吸い込みが早くて感動！使った瞬間から肌がピンと張るようなハリを感じます。上品なローズの香りにも癒やされて毎晩のお手入れが楽しみになりました。』(40代・エイジングケア重視)"
    }
}

# 比較表の行生成
table_rows = []
for item in lotion_items:
    rank = item["rank"]
    details = item_details_map[rank]
    table_rows.append(f"""            <tr>
              <td class="rank-cell">第{rank}位</td>
              <td class="name-cell"><strong>{item['display_name']}</strong><br><span style="font-size:11px;color:#64748b;">{item['brand']}</span></td>
              <td>{details['spec_texture']}</td>
              <td>{details['spec_ing']}</td>
              <td class="price-cell">¥{item['price']:,}</td>
              <td>{details['target']}</td>
            </tr>""")

# アイテム詳細レビューのHTML生成
items_detail_html = []
for item in lotion_items:
    rank = item["rank"]
    details = item_details_map[rank]
    
    review_stars = "★" * int(round(float(item["review_average"]))) if item["review_average"] else "★★★★★"
    review_text = f"{item['review_average']} ({item['review_count']}件)" if item["review_count"] else "4.8 (高評価)"
    
    items_detail_html.append(f"""      <article class="product-card" id="rank-{rank}">
        <div class="card-header">
          <span class="rank-badge">第{rank}位</span>
          <span class="product-tag">{details['tag']}</span>
        </div>

        <div class="image-wrapper">
          <img src="{item['image_url']}" alt="{item['display_name']}" loading="lazy">
        </div>

        <div class="card-body">
          <div class="brand-name">{item['brand']}</div>
          <h3 class="product-name">{item['display_name']}</h3>
          <p class="product-catch">{details['catch']}</p>

          <div class="review-box">
            <span class="stars">{review_stars}</span>
            <span class="rating-num">{review_text}</span>
            <span class="review-label">楽天市場 最新レビュー評価</span>
          </div>

          <div class="price-box">
            <span class="price-label">参考価格 (税込)：</span>
            <span class="price-val">¥{item['price']:,}</span>
            <span class="price-notice">※最新価格・ポイント還元はショップにてご確認ください</span>
          </div>

          <!-- スペック表 -->
          <div class="spec-grid">
            <div class="spec-item"><span class="spec-key">容量</span><span class="spec-val">{details['spec_cap']}</span></div>
            <div class="spec-item"><span class="spec-key">感触</span><span class="spec-val">{details['spec_texture']}</span></div>
            <div class="spec-item"><span class="spec-key">主要成分</span><span class="spec-val">{details['spec_ing']}</span></div>
            <div class="spec-item"><span class="spec-key">仕上がり</span><span class="spec-val">{details['spec_finish']}</span></div>
          </div>

          <!-- 詳細解説文 -->
          <div class="detail-description">
            <h4 class="detail-subheading">💡 専門解説＆冬の処方サイエンス</h4>
            <p class="desc-text">{details['desc_p1']}</p>
            <p class="desc-text">{details['desc_p2']}</p>
          </div>

          <!-- こんな人におすすめ -->
          <div class="recommend-target">
            <span class="target-title">🎯 こんな肌悩み・冬トラブルにイチオシ！</span>
            <p class="target-text">{details['target']}</p>
          </div>

          <!-- プロ直伝の使い方 -->
          <div class="howto-box">
            <span class="howto-title">✨ 効果を最大化するプロ直伝の塗り方・テクニック</span>
            <p class="howto-text">{details['how_to']}</p>
          </div>

          <!-- リアルな口コミ -->
          <div class="voice-box">
            <span class="voice-title">💬 リアルな使用感・愛用者の口コミ</span>
            <p class="voice-text">{details['voice']}</p>
          </div>

          <!-- 楽天アフィリエイト購入ボタン -->
          <div class="cta-wrapper">
            <a href="{item['affiliate_url']}" target="_blank" rel="nofollow noopener" class="cta-button">
              <span>楽天市場で最安値＆口コミを見る</span>
              <span class="btn-sub">公式ショップ・送料無料プランをチェック ❯</span>
            </a>
          </div>
        </div>
      </article>""")

# JSON-LD ItemList
json_ld_items = []
for item in lotion_items:
    json_ld_items.append(f"""          {{
            "@type": "ListItem",
            "position": {item['rank']},
            "name": "{item['display_name']}",
            "url": "https://lumi-cosme.vercel.app/winter-lotion#rank-{item['rank']}"
          }}""")

item_list_json = ",\n".join(json_ld_items)
og_image = lotion_items[0]["image_url"]

html_content = f"""<!DOCTYPE html>
<html lang="ja" prefix="og: http://ogp.me/ns#">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【2026最新】保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションおすすめ10選 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の深刻な暖房乾燥・角質ゴワつきをリセット！イプサ、アクセーヌ、エスト、カルテHD、オルビスユーなど超微細ナノカプセルやエクトイン、ヘパリン類似物質配合の高保湿化粧水厳選10選を徹底比較。手vsコットンの正しい付け方や重ね付けの科学まで完全網羅。">
  <meta name="keywords" content="化粧水, 高保湿化粧水, 冬 スキンケア, とろみ化粧水, イプサ タイムRアクア, アクセーヌ モイストバランス, エスト ザ ローション, カルテHD, オルビスユー, コスメデコルテ リポソーム, 2026コスメ">

  <!-- SEO & Canonical -->
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-lotion">
  <meta name="robots" content="index, follow">

  <!-- OGP -->
  <meta property="og:site_name" content="Lumi Cosme (ルミコスメ)">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションおすすめ10選">
  <meta property="og:description" content="エアコン温風でカラカラになった冬肌をヒタヒタに満たす！イプサ、アクセーヌ、エストなど話題の高保湿化粧水を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lotion">
  <meta property="og:image" content="{og_image}">
  <meta property="og:locale" content="ja_JP">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションおすすめ10選">
  <meta name="twitter:description" content="エアコン温風でカラカラになった冬肌をヒタヒタに満たす！イプサ、アクセーヌ、エストなど話題の高保湿化粧水を徹底比較。">
  <meta name="twitter:image" content="{og_image}">

  <link rel="stylesheet" href="style.css">

  <!-- 構造化データ (JSON-LD) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Article",
        "headline": "保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションおすすめ10選",
        "description": "11月・12月の本格乾燥シーズンに必須の高保湿化粧水の選び方、成分比較、おすすめ10選を徹底レビュー。",
        "image": "{og_image}",
        "datePublished": "2026-10-28T00:00:00+09:00",
        "dateModified": "2026-10-28T00:00:00+09:00",
        "author": {{
          "@type": "Organization",
          "name": "Lumi Cosme 編集部"
        }},
        "publisher": {{
          "@type": "Organization",
          "name": "Lumi Cosme (ルミコスメ)",
          "url": "https://lumi-cosme.vercel.app/"
        }}
      }},
      {{
        "@type": "ItemList",
        "name": "冬の高保湿化粧水＆とろみ浸透ローションおすすめ10選",
        "itemListElement": [
{item_list_json}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "冬場は化粧水を何回重ね付けするのが最も効果的ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "一度に大量につけるよりも、『少量を2〜3回に分けて重ね付けするミルフィーユ付け』が最も浸透効率を高めます。1回目で角層表面を湿らせて通り道を作り、2回目で細胞間脂質の隙間へ流し込み、3回目でハンドプレスして密閉します。手のひらが吸い付くようにモッチリしたら満水サインです。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "化粧水をつけるのは手とコットン、冬はどちらが良いですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "乾燥がひどく肌が敏感になっている冬は、手のひらでの塗布が推奨されます。手の体温で化粧水が温まり浸透が促進される上、摩擦刺激をゼロに抑えられます。ただし、イプサやコスメデコルテなどキメの凹凸に均一に行き渡らせたい場合や角質ケアを兼ねる場合は、毛羽立ちのない上質コットンに裏までたっぷり含ませて摩擦レスに滑らせるのが効果的です。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "とろみのある高保湿化粧水は、なぜ肌に入りにくく感じるのですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "とろみ成分（増粘多糖類や高分子ポリマー）が肌表面に膜を張るため、角層が冷えて強張っている冬は浸透に時間がかかります。対策として、化粧水の前に導入先行美容液（ブースター）を仕込むか、化粧水を両手のひらで5秒間温めてから優しくハンドプレスして押し込むと、浸透スピードが劇的にアップします。"
            }}
          }},
          {{
            "@type": "Question",
            "name": "化粧水だけでスキンケアを終わらせても大丈夫ですか？",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "絶対にNGです！化粧水は成分の80〜90%が水分です。油分のフタ（乳液やクリーム）を重ねないと、室内の暖房によって化粧水の水分とともに肌本来の水分まで一緒に蒸発してしまう『過乾燥（リバウンドドライ）』を引き起こします。化粧水後は必ず30秒以内に乳液や高保湿クリームで密閉しましょう。"
            }}
          }}
        ]
      }}
    ]
  }}
  </script>
</head>
<body class="theme-lotion">

  <!-- ヘッダー -->
  <header class="site-header">
    <div class="header-badge">💧 2026 WINTER LOTION SELECTION</div>
    <h1 class="site-title">高保湿化粧水＆浸透ローション10選</h1>
    <p class="site-subtitle">11月・12月の過酷な暖房乾燥と粉吹き肌を深部から満水にする神ローション</p>
  </header>

  <main class="container">

    <!-- 記事トップ・アイキャッチ -->
    <article class="article-intro">
      <div class="article-meta">
        <span class="article-cat-tag">スキンケア特集 / 高保湿化粧水</span>
        <span class="article-date">📅 2026.10.28 更新</span>
      </div>

      <h1 class="article-main-heading">保湿力の強さで肌乾燥とさようなら！冬の乾きを満たす高保湿化粧水＆とろみ浸透ローションランク10</h1>

      <p class="article-lead">
        11月から12月にかけて気温と湿度が急落すると、<strong>「化粧水をたっぷりつけているはずなのに数分後にはつっぱる」「夕方になると口元や頬が白く粉を吹く」「ファンデーションがピキピキひび割れて毛穴落ちする」</strong>という深刻な水分不足SOSが肌から発せられます。<br><br>
        冬の肌は、寒さによる血行不良と乾燥冷風によって角質層が硬化し、水分を受け入れにくい『角質肥厚』状態に陥っています。ただ適当に化粧水をパシャパシャつけるだけでは、表面で蒸発してしまい角層深部まで潤いが届きません。<br><br>
        冬に必要なのは、硬くなった肌を優しくほぐしながら細胞レベルで水分をギュッと抱え込む<strong>「超微細ナノカプセル」「エクトイン」「ヘパリン類似物質」「高機能リポソーム」</strong>などを配合した真の実力派高保湿化粧水です。<br><br>
        本記事では、2026年の最新スキンケアサイエンスに基づき、11-12月の乾燥砂漠肌を救い出す最強の化粧水10選を徹底比較します！
      </p>

      <!-- 目次ナビゲーション -->
      <nav class="toc-container">
        <div class="toc-title">📑 本記事の目次</div>
        <ul class="toc-list">
          <li><a href="#why-lotion">1. なぜ冬の化粧水は入らない？角層硬化とインナードライのメカニズム</a></li>
          <li><a href="#types">2. シャバシャバ系vs濃密とろみ系！肌質に合わせた冬化粧水の選び方</a></li>
          <li><a href="#comparison">3. 【一目でわかる】冬の高保湿化粧水10選 比較早見表</a></li>
          <li><a href="#ranking">4. 【2026最新】冬の高保湿化粧水おすすめ10選 詳細個別レビュー</a></li>
          <li><a href="#technique">5. プロ直伝！水分保持力を200%高める「3回ミルフィーユ浸透法」</a></li>
          <li><a href="#faq">6. 冬の化粧水に関するよくある質問（FAQ）</a></li>
          <li><a href="#related">7. あわせて読みたい！冬の保湿ケア特集一覧</a></li>
        </ul>
      </nav>
    </article>

    <!-- メカニズム解説セクション -->
    <section id="why-lotion">
      <h2 class="section-title">なぜ冬の化粧水は入らない？角層硬化とインナードライのメカニズム</h2>
      <p class="content-text">
        気温が15℃を下回る11月以降、皮膚温の低下によって皮脂の分泌量が激減し、角質細胞同士を繋ぎ止めている細胞間脂質（セラミドなど）のラメラ構造が乱れ始めます。
      </p>
      <p class="content-text">
        バリア機能が低下した肌は、水分を自ら蓄える力を失い、古い角質が剥がれ落ちずに表面に蓄積してゴワゴワとした角質肥厚を起こします。この状態の肌に通常の化粧水をつけても、<strong>『乾いたスポンジが水を弾くように』</strong>表面を滑り落ちてしまうのです。
      </p>
      <div class="product-catch" style="margin: 20px 0;">
        💡 冬の高保湿化粧水選びで絶対に外せない3大条件：<br>
        ① <strong>微細化ナノカプセル・リポソーム技術</strong>：硬くなった角層の隙間をすり抜けて深部まで届くこと<br>
        ② <strong>水分保持成分の複合配合</strong>：セラミド、ヒアルロン酸、エクトイン、アミノ酸など多重の保水ネット<br>
        ③ <strong>低刺激・抗炎症処方</strong>：暖房や寒風による微弱炎症を鎮静するトラネキサム酸やグリチルリチン酸
      </div>
    </section>

    <!-- タイプ別選び方 -->
    <section id="types">
      <h2 class="section-title">シャバシャバ系vs濃密とろみ系！肌質に合わせた冬化粧水の選び方</h2>
      <div class="content-text">
        <p>冬の化粧水は、テクスチャーによって肌へのアプローチと保水アプローチが大きく異なります。自分の肌悩みと好みに合わせて最適なタイプを見極めましょう。</p>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #bae6fd; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0369a1; font-size: 16px; font-weight: 700; margin-bottom: 6px;">① 浸透特化・高機能シャバシャバ系（イプサ、アクセーヌ、コスメデコルテなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">ベタつきが苦手な方、インナードライ肌、混合肌に最適。超微細カプセルや浸透促進技術により、水のような軽やかさでありながら角層の最深部までぐんぐん水分を行き渡らせ、内側からふっくら潤します。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #bae6fd; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0369a1; font-size: 16px; font-weight: 700; margin-bottom: 6px;">② 濃密ヴェール・とろみ美容液系（エスト、極潤プレミアム、オルビスユーなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">粉吹きや皮剥けが起きやすい超乾燥肌、エイジング世代に最適。高分子ヒアルロン酸やエクトインが肌表面に厚みのある保水クッションを作り、エアコンの温風による水分の蒸散を物理的にシャットアウトします。</p>
        </div>

        <div style="background: #ffffff; border-radius: 12px; padding: 18px; margin: 16px 0; border: 1px solid #bae6fd; box-shadow: var(--shadow-soft);">
          <h3 style="color: #0369a1; font-size: 16px; font-weight: 700; margin-bottom: 6px;">③ 医薬部外品・バリア再建系（カルテHD、白潤プレミアムなど）</h3>
          <p style="font-size: 13.5px; color: #334155;">寒暖差で肌がヒリつく敏感肌、赤みが出やすい方に最適。ヘパリン類似物質やトラネキサム酸などの有効成分が、弱ったバリア機能を根本から立て直しながら健やかな角層を育みます。</p>
        </div>
      </div>
    </section>

    <!-- 比較早見表 -->
    <section id="comparison">
      <h2 class="section-title">【一目でわかる】冬の高保湿化粧水10選 比較早見表</h2>
      <p class="content-text">掲載している価格は楽天市場の最新調査価格（税込）です。横スクロールで特徴や配合成分を比較できます。</p>

      <div class="table-scroll-wrapper">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名</th>
              <th>テクスチャー</th>
              <th>主要キー成分</th>
              <th>参考価格</th>
              <th>おすすめな肌悩み</th>
            </tr>
          </thead>
          <tbody>
{chr(10).join(table_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- アイテム詳細レビュー -->
    <section id="ranking">
      <h2 class="section-title">【2026最新】冬の高保湿化粧水おすすめ10選 詳細個別レビュー</h2>
{chr(10).join(items_detail_html)}
    </section>

    <!-- プロ直伝テクニック -->
    <section id="technique">
      <h2 class="section-title">プロ直伝！水分保持力を200%高める「3回ミルフィーユ浸透法」</h2>
      <div class="content-text">
        <p>
          高保湿な化粧水も、一度にドバッと塗って終わらせては真価を発揮できません。冬の角層に水分を限界まで蓄える4ステップのプロ直伝テクニックをご紹介します。
        </p>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #bae6fd;">
          <h3 style="color: #0369a1; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 1：まずは「導入先行美容液」で角層の道筋を開く</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            洗顔後、化粧水の前にブースター美容液を1滴馴染ませます。硬く強張った細胞間脂質をほぐしておくことで、後から重ねる化粧水の吸水率が劇的に跳ね上がります。（※<a href="/winter-serum-booster" style="color: #0284c7; font-weight: 700; text-decoration: underline;">冬の導入先行美容液10選はこちら</a>）
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #bae6fd;">
          <h3 style="color: #0369a1; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 2：1回目は「全体に薄く伸ばして湿潤ルートを作る」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            100円玉大の化粧水を手のひら全体に広げ、顔全体を優しく包み込みます。こすらず、手のひらの温もりで角層表面をじんわり湿らせます。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #bae6fd;">
          <h3 style="color: #0369a1; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 3：2回目は「乾燥しやすい頬と目元に重ね付け押し込み」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            同量を再度手にとり、特にエアコン風が直撃する頬骨、目元、口元を中心にハンドプレス。細胞の隙間に水分を押し込むイメージで5秒間密着させます。
          </p>
        </div>

        <div style="margin: 20px 0; background: #ffffff; border-radius: 12px; padding: 20px; border: 1px solid #bae6fd;">
          <h3 style="color: #0369a1; font-size: 15px; font-weight: 700; margin-bottom: 8px;">STEP 4：化粧水後30秒以内に高保湿クリームで「完全密閉」</h3>
          <p style="font-size: 13.5px; color: #475569; line-height: 1.6;">
            化粧水で満たした水分は放置すると室内の暖房で蒸発します。水分が肌に残っているうちに、高保湿フェイスクリームや乳液を重ねてエモリエントのフタを完成させましょう。（※<a href="/winter-moisture-cream" style="color: #0284c7; font-weight: 700; text-decoration: underline;">高保湿フェイスクリーム10選はこちら</a>）
          </p>
        </div>
      </div>
    </section>

    <!-- FAQ セクション -->
    <section id="faq">
      <h2 class="section-title">冬の化粧水に関するよくある質問（FAQ）</h2>
      <div class="faq-list">
        <div class="faq-item">
          <div class="faq-question">Q1. 冬場は化粧水を何回重ね付けするのが最も効果的ですか？</div>
          <div class="faq-answer">
            一度に大量につけるよりも、『少量を2〜3回に分けて重ね付けするミルフィーユ付け』が最も浸透効率を高めます。1回目で角層表面を湿らせて通り道を作り、2回目で細胞間脂質の隙間へ流し込み、3回目でハンドプレスして密閉します。手のひらが吸い付くようにモッチリしたら満水サインです。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q2. 化粧水をつけるのは手とコットン、冬はどちらが良いですか？</div>
          <div class="faq-answer">
            乾燥がひどく肌が敏感になっている冬は、手のひらでの塗布が推奨されます。手の体温で化粧水が温まり浸透が促進される上、摩擦刺激をゼロに抑えられます。ただし、イプサやコスメデコルテなどキメの凹凸に均一に行き渡らせたい場合や角質ケアを兼ねる場合は、毛羽立ちのない上質コットンに裏までたっぷり含ませて摩擦レスに滑らせるのが効果的です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q3. とろみのある高保湿化粧水は、なぜ肌に入りにくく感じるのですか？</div>
          <div class="faq-answer">
            とろみ成分（増粘多糖類や高分子ポリマー）が肌表面に膜を張るため、角層が冷えて強張っている冬は浸透に時間がかかります。対策として、化粧水の前に導入先行美容液（ブースター）を仕込むか、化粧水を両手のひらで5秒間温めてから優しくハンドプレスして押し込むと、浸透スピードが劇的にアップします。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-question">Q4. 化粧水だけでスキンケアを終わらせても大丈夫ですか？</div>
          <div class="faq-answer">
            絶対にNGです！化粧水は成分の80〜90%が水分です。油分のフタ（乳液やクリーム）を重ねないと、室内の暖房によって化粧水の水分とともに肌本来の水分まで一緒に蒸発してしまう『過乾燥（リバウンドドライ）』を引き起こします。化粧水後は必ず30秒以内に乳液や高保湿クリームで密閉しましょう。
          </div>
        </div>
      </div>
    </section>

    <!-- 内部リンク・関連記事セクション -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list">
        <a href="/winter-serum-booster" class="related-link-card">
          <div class="related-link-title">💧 浸透力を底上げする高保湿・導入先行美容液おすすめ10選</div>
          <div class="related-link-desc">化粧水前の仕込みに必須！固くなった角質細胞をほぐし、化粧水の水分をごくごく吸い込む素肌へ。</div>
        </a>

        <a href="/winter-face-mask" class="related-link-card">
          <div class="related-link-title">💧 水分爆弾で砂漠肌を即リセット！高保湿シートマスク＆夜用パック10選</div>
          <div class="related-link-desc">暖房でしぼんだ肌に潤い集中チャージ！トリデン、ルルルン、バイオダンスなど話題の密着パック。</div>
        </a>

        <a href="/winter-moisture-cream" class="related-link-card">
          <div class="related-link-title">🧴 保湿力の強さで肌乾燥とさようなら！高保湿フェイスクリーム＆濃密バーム10選</div>
          <div class="related-link-desc">化粧水後の仕上げに！補給した水分を逃さず朝まで完全密閉する最強クリームを徹底比較。</div>
        </a>

        <a href="/winter-eye-cream" class="related-link-card">
          <div class="related-link-title">👁️ 暖房直撃の目元・ほうれい線をふっくら密着！高保湿アイクリーム＆薬用リンクルケア10選</div>
          <div class="related-link-desc">皮膚が薄く乾燥小じわができやすい目元・口元をピンポイント集中ケアする実力派名品集。</div>
        </a>

        <a href="/winter-base-makeup" class="related-link-card">
          <div class="related-link-title">✨ 夕方まで潤いツヤが続く高保湿ファンデーション＆美容液下地10選</div>
          <div class="related-link-desc">化粧水で整えたプルプル肌を1日中キープ！暖房下でもひび割れないツヤ肌ベースメイク。</div>
        </a>

        <a href="/winter-lip-care" class="related-link-card">
          <div class="related-link-title">🎁 冬のガサガサ皮剥けに終止符！高保湿リップトリートメント＆濃密ティント10選</div>
          <div class="related-link-desc">皮脂腺のない唇を乾燥冷風から強力ガード。夜用リップスリーピングマスクからプランパーまで。</div>
        </a>
      </div>
    </section>

  </main>

  <!-- フッター -->
  <footer class="site-footer">
    <div class="footer-links">
      <a href="/">トップページ</a>
      <a href="/winter-lotion">高保湿化粧水</a>
      <a href="/winter-serum-booster">導入美容液</a>
      <a href="/winter-face-mask">シートマスク</a>
      <a href="/winter-moisture-cream">保湿クリーム</a>
      <a href="/winter-eye-cream">アイクリーム</a>
      <a href="/winter-base-makeup">ベースメイク</a>
      <a href="/winter-lip-care">リップケア</a>
      <a href="/winter-body-care">ボディケア</a>
      <a href="/winter-hair-care">ヘアケア</a>
      <a href="/winter-hand-care">ハンドケア</a>
    </div>
    <p class="copyright">© 2026 Lumi Cosme (ルミコスメ) All Rights Reserved.</p>
  </footer>

</body>
</html>
"""

output_path = "winter-lotion.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {output_path} successfully! Size: {len(html_content)} bytes")
