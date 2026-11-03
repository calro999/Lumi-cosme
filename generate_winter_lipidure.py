import json
import re

with open("fetched_final_30_spicule_stemcell_lipidure.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_lipidure"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 5種のヒト型セラミド×リピジュア！敏感肌の水分バリアを極限まで強化する傑作美容液",
        "catch": "角層深部をセラミドで満たし、表面をリピジュア膜で鉄壁シールド。冬の砂漠肌を完全救済",
        "brand_name": "松山油脂 (肌をうるおす保湿スキンケア)",
        "capacity": "30ml (肌をうるおす 保湿美容液)",
        "type": "高保水ヒト型セラミド×リピジュア配合美容液",
        "features": "ヒト型セラミド5種（1/2/3/5/6II）、リピジュア（ポリクオタニウム-51）、大豆由来保湿成分、無香料・アルコールフリー",
        "value": "細胞間脂質を補うセラミドと人工細胞膜リピジュアの黄金コンビ。洗顔後も持続する耐水性保水ヴェールで一日中もっちり肌をキープ",
        "desc_p1": "11月から12月にかけて外気湿度が急激に30%以下へ落ち込み、オフィスのエアコン温風が一日中顔に直撃する過酷な初冬。どんなに水分を補給しても、肌表面から蒸散してしまっては意味がありません。松山油脂の『肌をうるおす 保湿美容液』は、人の皮膚構造に近い5種のヒト型セラミドと、ヒアルロン酸の2倍の保水力を持つリピジュアを贅沢に融合させた大人気美容液です。",
        "desc_p2": "とろみのあるみずみずしいジェル状テクスチャーが肌に伸ばした瞬間にスーッとほどけ、角層深部へセラミドを補給。同時にリピジュアが肌表面にナノスケールの生体適合性保護膜を張り巡らせ、エアコンの風による水分蒸発を物理的にシャットアウトします。低刺激処方でアルコールや香料を一切含まないため、冬の寒暖差でピリピリしやすいデリケートな敏感肌でも安心して使え、夕方になってもファンデーションの粉吹きや乾燥崩れが起きません。",
        "target": "冬になると日中の乾燥や粉吹きがひどい方、敏感肌で刺激に弱い方、セラミドとリピジュアのW保湿をコスパ良く続けたい方",
        "point": "化粧水の直後、手のひらに2プッシュを取り、顔全体を温めるようにハンドプレス。乾燥小ジワが目立ちやすい目元やほうれい線には1プッシュを重ね付けするのが効果的です。"
    },
    {
        "rank": 2,
        "tag": "💧 累計数千万本突破の殿堂入り！角層に水分を磁石のように吸着させる濃厚保水エッセンス",
        "catch": "高純度ヒアルロン酸×保水ネットワーク。いつものスキンケアに混ぜるだけで乾燥肌を緊急レスキュー",
        "brand_name": "太陽のアロエ社",
        "capacity": "80ml + ミニボトル付 (ヒアルロン酸 原液)",
        "type": "バイオ技術抽出高純度ヒアルロン酸原液",
        "features": "国内自社工場製造、高純度ヒアルロン酸ナトリウム、リピジュア等とのブレンド相性抜群、無香料・低刺激",
        "value": "1gで6リットルの水を抱え込む驚異の保水力。リピジュアコスメや化粧水と合わせることで、角層の水分保持率を極限まで引き上げる",
        "desc_p1": "口コミサイトやSNSで長年ベスコスを受賞し続ける太陽のアロエ社の高純度ヒアルロン酸原液。国内の厳格なバイオ発酵技術によって抽出された純粋なヒアルロン酸水溶液で、余分な界面活性剤や香料を一切排除した直球の保水成分です。",
        "desc_p2": "水のようにみずみずしいのに、肌に広げると驚くほど濃厚なとろみ膜となって密着。リピジュア配合の化粧水や乳液と一緒に使うことで、ヒアルロン酸が抱え込んだ大量の水分をリピジュアの人工膜がガッチリと閉じ込める『サンドイッチ保水』が完成します。顔だけでなく、冬にパサつく毛先や乾燥するボディ、リップパックなど全身の乾燥ケアに惜しみなく使えます。",
        "target": "シンプルで確実な水分補給を求める方、手持ちのスキンケアの保湿力を底上げしたい方、髪から全身まで保湿したい方",
        "point": "愛用の化粧水に1〜2滴混ぜて使うのが王道。さらに洗髪後の濡れた髪の毛先に少量なじませてからドライヤーで乾かすと、冬の静電気とパサつきを劇的に抑えられます。"
    },
    {
        "rank": 3,
        "tag": "🍊 働く女性の強い味方！天然オレンジ精油×リピジュア配合の濃密高保湿化粧水",
        "catch": "一日中乾かない濃密保水ヴェール。天然アロマの心地よい香りで冬のスキンケアが至福に",
        "brand_name": "RAFRA (ラフラ)",
        "capacity": "200ml (モイスチャーローション)",
        "type": "高保水リピジュア配合エイジングケア化粧水",
        "features": "リピジュア（ポリクオタニウム-51）、ヒト型セラミド、アミノ酸複合体、天然オレンジ精油、低分子コラーゲン",
        "value": "乾燥と戦うオフィスワーカーのために開発。洗顔しても落ちにくいリピジュアの皮膜が、長時間の暖房環境下でも瑞々しいハリを維持",
        "desc_p1": "シンプルで上質なスキンケアを提案するラフラの人気化粧水『モイスチャーローション』。天然の完熟オレンジから抽出したフレッシュな精油の香りに包まれながら、リピジュアとヒト型セラミドによる高機能な水分補給が叶います。",
        "desc_p2": "少しとろみのあるまろやかなテクスチャーが肌の上に広がり、角質層の隅々まで素早く浸透。肌表面にリピジュアによる滑らかな保護フィルムを形成するため、朝のメイク前に使用するとファンデーションが吸い付くように密着し、夕方になってもエアコンの乾燥風に負けないツヤ肌が持続します。合成香料や着色料は不使用で、肌への優しさも追求されています。",
        "target": "冬のオフィス暖房で夕方に肌がカピカピになる働く女性、柑橘系アロマの香りで癒やされたい方、高機能な高保湿化粧水を求める方",
        "point": "コットンではなく手のひらで温めながら2回に分けて重ね付けするのがおすすめ。1回目で角層をほぐし、2回目でリピジュアの保水膜を均一に定着させます。"
    },
    {
        "rank": 4,
        "tag": "🌾 とろみテクスチャーで角質をほぐす！大豆発酵エキス×リピジュアの高保水ローション",
        "catch": "硬くなった冬の角質層を柔らかく解きほぐし、角層深くまで潤いを引き込むモイストリッチ処方",
        "brand_name": "松山油脂 (肌をうるおす保湿スキンケア)",
        "capacity": "120ml (保湿浸透水 モイストリッチ)",
        "type": "超高保湿とろみ化粧水",
        "features": "リピジュア、大豆胚芽抽出液、5種のヒト型セラミド、ヒアルロン酸ナトリウム、アルコールフリー",
        "value": "美容液並みの濃厚なとろみ。大豆由来成分が肌のバリアを整え、リピジュアが表面からの水分蒸発を防ぐ二段構えの保湿設計",
        "desc_p1": "松山油脂の肌をうるおすシリーズの中でも、特に極度の乾燥肌や真冬のゴワつきに特化して作られた『保湿浸透水 モイストリッチ』。一般的なさらさら化粧水とは一線を画す、美容液のようにリッチなとろみテクスチャーが特徴です。",
        "desc_p2": "寒冷刺激で硬くこわばった角質層を大豆発酵成分がじんわりと解きほぐし、奥深くまで水分を浸透。肌表面にはリピジュアとヒアルロン酸が手を取り合って高密度の水分ネットワークを構築します。塗布した直後から肌がふっくらと柔らかくなり、キメの溝ひとつひとつが水分で満たされていくような深い潤い感を体感できます。",
        "target": "冬になると化粧水が肌に弾かれて入らないと感じる方、とろみのある高保湿ローションが好きな方、アルコールや香料に敏感な方",
        "point": "洗顔後、適量（500円玉大）を手のひらに取り、顔全体に優しくなじませた後、両手で顔を包み込んで10秒間キープ。手のぬくもりで浸透がより深まります。"
    },
    {
        "rank": 5,
        "tag": "🔬 業界最小クラスのナノカプセル×保水ポリマー！一日中乾きを知らない名品ローション",
        "catch": "皮膚科医が推奨する低刺激高機能設計。角層細胞の隙間をナノ水分子で満たし続ける",
        "brand_name": "ACSEINE (アクセーヌ)",
        "capacity": "360ml (モイスチャーバランス ローション)",
        "type": "持続型超微細ナノカプセル高保湿化粧水",
        "features": "微細ナノカプセル化技術、セルバウンス技術、リピジュア様保水ポリマー、無香料・無着色・低刺激性",
        "value": "角層の隙間（40〜60ナノ）よりも小さい超微細カプセルが深層まで浸透。肌の中でカプセルが徐々に潤いを放出し、一日中乾かない水分タンクを実現",
        "desc_p1": "皮膚生理学に基づいた敏感肌ブランド・アクセーヌの金字塔『モイスチャーバランス ローション』。角質層の隙間よりもはるかに小さいナノカプセルに水分保持成分を閉じ込め、角層の最深部まで送り届ける独自技術を採用しています。",
        "desc_p2": "テクスチャーは水のようにサラッとしているのに、肌になじませるとまるで吸い込まれるように消え、内側から押し返すようなモチモチ感へと変化。表面に保水ポリマー膜が形成されるため、暖房の効いた乾燥部屋に何時間いても潤いが持続します。360mlの大容量で朝晩惜しみなく使えるのも、冬の乾燥対策に心強いポイントです。",
        "target": "ベタつくテクスチャーは嫌いだけど圧倒的な保水力が欲しい方、敏感肌で肌荒れを繰り返しやすい方、大容量で贅沢に使いたい方",
        "point": "500円玉大を手のひらに取り、2〜3回に分けて重ね付けするのがアクセーヌ推奨の使い方。重ねるごとに肌がひんやりとし、水分満タンのサインがわかります。"
    },
    {
        "rank": 6,
        "tag": "💆 大人のごわつく乾燥肌をほぐす！リピジュア×白麹発酵エキスの濃密シートマスク",
        "catch": "リピジュアの人工保護膜で美容液を完全密閉。10分間の集中密着で吸い付くモチ肌へ",
        "brand_name": "LuLuLun (ルルルン)",
        "capacity": "32枚入 (ルルルンプレシャス RED モイスト)",
        "type": "高保湿エイジングケア大容量フェイスマスク",
        "features": "リピジュア（ポリクオタニウム-51）、発酵酵母細胞壁エキス、白麹エキス、サククラン（スイゼンジノリ多糖体）、超極厚ふっくらシート",
        "value": "年齢とともに硬くなる冬の角質層をほぐすリッチ処方。リピジュアがシートを剥がした後も肌表面に留まり、翌朝まで潤いを持続",
        "desc_p1": "大人の肌悩みに応えるルルルンプレシャスシリーズの中でも、最高峰の超乾燥・ごわつき対策として君臨する『RED（モイスト）』。美容液をたっぷり含んだ極厚の3層構造シートが、顔の凹凸に吸い付くように密着します。",
        "desc_p2": "注目成分であるリピジュアに加えて、日本の伝統発酵技術から生まれた白麹エキスや、ヒアルロン酸の約5倍の保水力を持つサクランを贅沢に配合。冬の寒さで強張った角質をじっくりと柔らかくほぐし、剥がした瞬間には手のひらに吸い付くような濃密な弾力肌へと導きます。32枚入りで毎日使えるため、真冬の乾燥シーズンを完全に乗り切れます。",
        "target": "冬になると肌がゴワついてファンデが浮いてしまう方、毎日のシートマスクで徹底的に乾燥対策をしたい大人世代",
        "point": "入浴後、5〜10分間密着させます。剥がしたマスクを折りたたんで首元やデコルテ、手の甲まで優しくパッティングすると全身の保湿が完了します。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 医薬部外品のセラミド機能カプセル！乾燥性敏感肌を外部刺激から守り抜く名品クリーム",
        "catch": "消炎剤配合で肌荒れを防ぎながら、ふんわり軽いのに吸い付く高保水保護ヴェールを形成",
        "brand_name": "Curel (キュレル)",
        "capacity": "40g (潤浸保湿 フェイスクリーム)",
        "type": "薬用セラミド機能高保湿フェイスクリーム (医薬部外品)",
        "features": "セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、消炎剤（アラントイン）、ユーカリエキス、弱酸性",
        "value": "角層の深部まで浸透するセラミド機能成分とリピジュア等の保水ケアとの相乗効果。冬の赤み・肌荒れを未然に防ぐ鉄壁クリーム",
        "desc_p1": "乾燥性敏感肌研究の金字塔であるキュレルの『潤浸保湿 フェイスクリーム』。肌の必須成分セラミドの働きを補う独自機能成分を配合し、冬の過酷な乾燥環境下でも角層のバリア機能を健やかに維持します。",
        "desc_p2": "ふわっとスフレのように軽いテクスチャーでありながら、肌に塗り広げるとしっとりと吸い付くような保護ヴェールへ変化。リピジュア配合の化粧水や美容液を塗った直後に重ねることで、補給した水分を完全に閉じ込め、外部の冷風や摩擦刺激をブロックします。医薬部外品の消炎剤配合で、寒暖差による赤みやカサつきを防ぐ安心感も抜群です。",
        "target": "重い油分クリームだとニキビやベタつきが気になる方、冬になると赤みやヒリつきが出やすい乾燥敏感肌の方",
        "point": "朝晩の乳液や美容液の後、直径約2cm程度を手に取り、顔全体に優しくなじませます。特にカサつきやすい頬や目の周りには重ね付けしてください。"
    },
    {
        "rank": 8,
        "tag": "🌿 天然水仕込み×リピジュア配合！全身に惜しみなくバシャバシャ使える高コスパ化粧水",
        "catch": "岩手県釜石の天然水とポリクオタニウム-51が融合。低刺激でたっぷり潤すデイリー名品",
        "brand_name": "無印良品 (MUJI)",
        "capacity": "300ml (敏感肌用化粧水 高保湿タイプ)",
        "type": "大容量生体適合性ポリマー配合高保湿化粧水",
        "features": "ポリクオタニウム-51（リピジュア）、ヒアルロン酸Na、グレープフルーツ種子エキス、無香料・無着色・無鉱物油・弱酸性・パラベンフリー・アルコールフリー",
        "value": "300mlで1,000円前後の驚異的コスパ。惜しみなくコットンパックや全身保湿に使えるため、冬の全身乾燥を完全に防止できる",
        "desc_p1": "世代を超えて愛され続ける無印良品のスキンケアシリーズ最高傑作『敏感肌用化粧水 高保湿タイプ』。ベースには岩手県釜石の洞窟から汲み出された超軟水の天然水を使用し、そこに肌保護成分としてリピジュア（ポリクオタニウム-51）とヒアルロン酸をバランス良く配合しています。",
        "desc_p2": "敏感肌に優しい徹底した無添加設計でありながら、肌になじませるとしっとりとしたうるおい膜が吸着。11月〜12月の乾燥時期には、顔だけでなく首元、デコルテ、乾燥して粉を吹く脚や腕まで全身に惜しみなくバシャバシャと重ね付けできます。手持ちの高級美容液の前のプレ化粧水としても極めて優秀です。",
        "target": "毎日たっぷり量を気兼ねなく使いたい方、全身の乾燥対策を1本で済ませたい方、敏感肌でシンプルな処方を好む方",
        "point": "スプレーヘッドを取り付けてお風呂上がりに全身に吹きかけるか、大判のコットンにたっぷり含ませて乾燥する頬に3分間ローションパックするのがおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🧪 原液コスメのパイオニア！保水ポリマー×セラミド×ヒアルロン酸の黄金比率ローション",
        "catch": "肌に必要な原液だけを調合。冬の乾燥ゴワつきを速攻でみずみずしい柔肌へ変える",
        "brand_name": "TUNEMAKERS (チューンメーカーズ)",
        "capacity": "120ml (原液保湿水)",
        "type": "高純度原液調合高保湿化粧水",
        "features": "リピジュア・セラミド・ヒアルロン酸・ハチミツ・コラーゲンを独自の『原液黄金比』でブレンド、無香料・無着色・鉱物油フリー",
        "value": "原料を薄めず原液のまま調合しているため、一般的な化粧水とは段違いの濃密保水力。硬化した真冬の角質層を瞬時に柔らかく整える",
        "desc_p1": "原液美容のスペシャリストであるチューンメーカーズが、乾燥肌のために原液をそのまま組み合わせて作り上げた『原液保湿水』。リピジュア、セラミド、ヒアルロン酸、ハチミツ、コラーゲンという高保湿成分を【5:3:2:1:1】の黄金比率でブレンドしています。",
        "desc_p2": "余計な界面活性剤や香料を一切加えず、成分本来の力だけで勝負した濃密なテクスチャー。肌に乗せるとスッと角質層へ引き込まれ、乾き切った細胞同士の隙間を隙間なく埋め尽くします。表面にはリピジュアとハチミツによる保護膜が形成され、触れた瞬間に手のひらが吸い付くような吸湿モチ肌を叶えます。",
        "target": "市販の化粧水では保湿力が持続しないと感じる方、原液コスメの実力派処方を試したい方、冬のインナードライを根本から解消したい方",
        "point": "手のひらに適量（100円玉大）を取り、顔全体になじませた後、乾燥がひどい部分にはもう一度少量を取り、指先で優しくトントンと押し込むように重ね付けしてください。"
    },
    {
        "rank": 10,
        "tag": "🛡️ 5種のヒト型セラミド×シア脂×リピジュア！冬の冷風を完全遮断する鉄壁保護クリーム",
        "catch": "コクのある濃厚テクスチャーが体温でとろける。一晩中潤いを逃さない真冬のシールド",
        "brand_name": "松山油脂 (肌をうるおす保湿スキンケア)",
        "capacity": "50g (肌をうるおす 保湿クリーム)",
        "type": "高機能セラミド×シア脂×リピジュア高保湿フェイスクリーム",
        "features": "ヒト型セラミド5種、リピジュア（ポリクオタニウム-51）、シア脂、スクワラン、大豆発酵エキス",
        "value": "植物油と生体適合性ポリマーが合体。肌表面に水分の蒸散を許さない二重の被膜を形成し、冬の暖房下でも夕方までモチモチ肌を死守",
        "desc_p1": "松山油脂のスキンケア技術の粋を集めた冬の最高峰クリーム『肌をうるおす 保湿クリーム』。角質層を潤す5種のヒト型セラミドに加え、肌を柔らかく包み込むシア脂とスクワラン、そして表面の水分蒸発を防ぐリピジュアをバランス良く調合しています。",
        "desc_p2": "ジャーからすくった瞬間はこっくりと濃厚な質感ですが、肌に乗せると手の温もりでスーッとなめらかにとろけて密着。油分のベタつきや皮膜感を感じさせないのに、肌の内側にはしっかりとした水分が閉じ込められている安心感があります。暖房を一晩中つけたままの寝室で寝ても、翌朝起きたときの肌はふっくら柔らかく、乾燥によるツッパリ感が一切ありません。",
        "target": "どんなクリームを塗っても朝起きるとカサついている方、シアバターの保護力とリピジュアの保水膜を両方欲しい方",
        "point": "スキンケアの最後に、パール1粒大を手に取り、両手ですり合わせて温めてから顔全体を包み込むように塗布。目元や口元など乾燥しやすい部分には指先で優しく重ね付けしてください。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['name']}",
        "description": d['catch'],
        "image": p['img_url'],
        "url": f"https://trendbeauty.site/winter-lipidure.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "リピジュア（ポリクオタニウム-51）とはどのような成分ですか？ヒアルロン酸と何が違いますか？",
        "answer": "リピジュアは、人間の細胞膜を構成するリン脂質（ホスホリルコリン極性基）をモデルにして、日本油脂（現・日油）が開発した生体適合性ポリマーです。医療現場で人工血管や人工心臓の内壁、コンタクトレンズの保水剤として使用されるほど高い安全性と親和性を持っています。ヒアルロン酸との決定的な違いは『保水力の高さ（ヒアルロン酸の約2倍）』と『耐水性（水で洗っても落ちにくい特性）』です。肌になじませると表面にラメラ液晶構造の保護膜を形成し、冬のエアコン暖房環境下でも水分を逃さずキープします。"
    },
    {
        "question": "11月〜12月の冬にリピジュアコスメを使うメリットは何ですか？",
        "answer": "冬は乾燥した北風と室内暖房によって、角質層の水分が猛スピードで蒸散する『過乾燥』が起きます。通常の水性保湿成分は外気の乾燥に引っ張られて蒸発してしまいがちですが、リピジュアは肌表面に水分子をがっちり捕捉するナノヴェールを形成するため、湿度が20%台に落ち込む極限環境でも蒸散を防ぎます。さらに、硬くなった角質細胞のキメを整えて夕方のファンデーションの毛穴落ちや粉吹きを劇的に防止します。"
    },
    {
        "question": "セラミド配合のスキンケアと一緒に使っても大丈夫ですか？",
        "answer": "非常に相性が良く、皮膚科学的にも最も推奨される組み合わせの一つです。セラミドは『角質細胞同士の隙間（細胞間脂質）』を満たして内側のバリアを整えるのに対し、リピジュアは『肌表面』に人工的な角層バリア膜を張ります。つまり『内側のセラミド×外側のリピジュア』という内外ダブルの鉄壁シールドが完成し、真冬の乾燥冷風を完全にシャットアウトできます。"
    },
    {
        "question": "リピジュアは敏感肌やアトピー肌、ニキビ肌でも使えますか？",
        "answer": "リピジュアは生体適合性が極めて高く、アレルギー反応や皮膚刺激性が極めて少ない成分として医療分野でも認められています。油分（オイル）ではなく水溶性のポリマーであるため、毛穴を詰まらせてニキビを悪化させる心配もありません。冬の乾燥でバリア機能が低下し、何をつけてもヒリヒリしてしまう敏感肌や乾燥性アトピー肌の水分保護膜としても理想的です。"
    },
    {
        "question": "リピジュア配合のコスメを使うタイミングや順番は？",
        "answer": "化粧水タイプや美容液タイプのリピジュアコスメは、洗顔後、油分のあるクリームやオイルを塗る前のステップで使用するのが基本です。水分を与えながら表面に保水膜を張るため、その後にセラミドクリームやシアバターなどで油分のフタを重ねると、保水膜がより強固に密閉されます。また、朝のメイク前に使うと日中の乾燥崩れ防止に絶大な威力を発揮します。"
    }
]

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
        "@id": "https://lumi-cosme.vercel.app/winter-lipidure.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の2倍の保水膜で冬の乾燥冷風を完全ブロックする高保水リピジュアコスメランク10",
    "description": "11月・12月の過酷な暖房乾燥と冬のインナードライを救う高保水リピジュア（ポリクオタニウム-51）コスメを徹底厳選！松山油脂のセラミド美容液から太陽のアロエ社、アクセーヌ、ルルルンプレシャスまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
    "image": items[0]["img_url"],
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
    "name": "真冬の高保水リピジュア（ポリクオタニウム-51）コスメおすすめ人気ランキング10選",
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
      <h3 class="product-name">{d['brand_name']} {p['name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-flex">
        <div class="product-img-box">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で詳細を見る・購入
          </a>
        </div>
        
        <div class="product-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{d['brand_name']}</td></tr>
            <tr><th>容量 / 規格</th><td>{d['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・保水構造</th><td>{d['features']}</td></tr>
            <tr><th>高保水ヴェールの理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の乾燥肌・インナードライに対する詳細解説</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-block">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-block">
            <strong>✨ 美容のプロ直伝！冬のおすすめ活用テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_str = "\n".join(cards_html)

faq_html = []
for f in faq_list:
    faq_html.append(f"""
      <div class="faq-item">
        <h3 class="faq-q">Q. {f['question']}</h3>
        <p class="faq-a">A. {f['answer']}</p>
      </div>
    """)
faq_str = "\n".join(faq_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の2倍の保水膜で冬の乾燥冷風を完全ブロックする高保水リピジュアコスメランク10 - 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の過酷な暖房乾燥と冬のインナードライを救う高保水リピジュア（ポリクオタニウム-51）コスメを徹底厳選！松山油脂のセラミド美容液から太陽のアロエ社、アクセーヌ、ルルルンプレシャスまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="リピジュア,ポリクオタニウム-51,高保水,乾燥肌,冬コスメ,インナードライ,松山油脂,アクセーヌ,ルルルン,楽天コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-lipidure.html">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の2倍の保水膜で冬の乾燥冷風を完全ブロックする高保水リピジュアコスメランク10">
  <meta property="og:description" content="11月・12月の過酷な暖房乾燥と冬のインナードライを救う高保水リピジュア（ポリクオタニウム-51）コスメを徹底厳選！松山油脂のセラミド美容液から太陽のアロエ社、アクセーヌ、ルルルンプレシャスまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lipidure.html">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
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
      --primary: #0e4c6b;
      --primary-light: #166b94;
      --accent: #0284c7;
      --bg: #f7fafd;
      --card-bg: #ffffff;
      --text: #22292f;
      --text-muted: #56646f;
      --border: #d4e5f2;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(14, 76, 107, 0.08);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Kaku Gothic ProN", "Yu Gothic", Meiryo, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: linear-gradient(135deg, #093348, #0f5275);
      color: #fff;
      padding: 18px 24px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      letter-spacing: 0.5px;
    }}
    .breadcrumb {{
      max-width: 1080px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{ color: var(--primary-light); text-decoration: none; }}
    .main-container {{
      max-width: 1080px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: #fff;
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 32px;
    }}
    .article-badge {{
      display: inline-block;
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #0c364c;
      margin-bottom: 20px;
      font-weight: 800;
    }}
    .meta-box {{
      display: flex;
      gap: 18px;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .lead-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #313c45;
      margin-bottom: 18px;
    }}
    .toc-box {{
      background: #f3f8fc;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin: 28px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary);
      margin-bottom: 14px;
    }}
    .toc-list {{
      list-style-position: inside;
      line-height: 2;
    }}
    .toc-list a {{ color: var(--primary-light); text-decoration: none; }}
    .toc-list a:hover {{ text-decoration: underline; }}
    
    .guide-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
      line-height: 1.4;
    }}
    .guide-section h3 {{
      font-size: 1.2rem;
      color: #0b374e;
      margin: 24px 0 12px;
    }}
    .guide-section p {{
      margin-bottom: 16px;
      font-size: 0.98rem;
      line-height: 1.85;
    }}
    .guide-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 24px 0;
    }}
    .grid-card {{
      background: #f4f9fd;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #d6e7f4;
    }}
    .grid-card h4 {{
      color: var(--primary);
      margin-bottom: 8px;
      font-size: 1.05rem;
    }}
    
    /* Product Cards */
    .product-card {{
      background: #fff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      padding: 32px;
      margin-bottom: 36px;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -14px;
      left: 24px;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(2, 132, 199, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #0369a1;
      background: #e0f2fe;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }}
    .product-name {{
      font-size: 1.4rem;
      line-height: 1.4;
      color: #0b344a;
      margin-bottom: 8px;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #075985;
      margin-bottom: 24px;
    }}
    .product-flex {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    @media (min-width: 768px) {{
      .product-flex {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}
    .product-img-box {{
      flex: 0 0 280px;
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 10px;
      background: #fafafa;
      border: 1px solid #f0f0f0;
      padding: 8px;
    }}
    .price-box {{
      margin: 14px 0;
      padding: 10px;
      background: #f0f8ff;
      border-radius: 8px;
      border: 1px dashed #bddcf5;
    }}
    .price-label {{ display: block; font-size: 0.78rem; color: #627484; }}
    .price-val {{ font-size: 1.5rem; font-weight: 800; color: #0284c7; }}
    .price-tax {{ font-size: 0.8rem; color: #627484; }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #fff;
      font-weight: 700;
      text-align: center;
      padding: 14px 20px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.98rem;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #d60000, #b00000);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
    }}
    .product-spec-box {{
      flex: 1;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 18px;
      font-size: 0.88rem;
    }}
    .spec-table th {{
      width: 28%;
      background: #eef6fc;
      padding: 8px 12px;
      border: 1px solid #d4e5f2;
      text-align: left;
      color: #0b4566;
      font-weight: 600;
    }}
    .spec-table td {{
      padding: 8px 12px;
      border: 1px solid #d4e5f2;
      background: #fff;
    }}
    .review-block {{
      background: #f4f9fd;
      border-left: 4px solid var(--accent);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
    }}
    .review-block h4 {{
      font-size: 0.98rem;
      color: #0e4c6b;
      margin-bottom: 8px;
    }}
    .review-block p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #27343d;
      margin-bottom: 8px;
    }}
    .review-block p:last-child {{ margin-bottom: 0; }}
    .target-block, .usage-block {{
      font-size: 0.9rem;
      margin-bottom: 10px;
      line-height: 1.7;
    }}
    
    /* FAQ Section */
    .faq-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 24px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 18px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      color: #0369a1;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #2c3a44;
    }}
    
    /* Internal Links Grid */
    .internal-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .internal-section h2 {{
      font-size: 1.4rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
    }}
    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }}
    .internal-card {{
      background: #f4f8fc;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #d5e5f3;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      background: #fff;
    }}
    .internal-card h4 {{
      color: var(--primary);
      font-size: 0.98rem;
      margin-bottom: 6px;
      font-weight: 700;
    }}
    .internal-card p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    
    footer {{
      background: #092636;
      color: #c4d7e3;
      padding: 48px 20px 24px;
      font-size: 0.88rem;
      line-height: 1.8;
    }}
    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px 20px;
      margin-bottom: 24px;
    }}
    .footer-links a {{ color: #dbeaf4; text-decoration: none; font-size: 0.82rem; }}
    .footer-links a:hover {{ text-decoration: underline; }}
    .footer-copy {{
      text-align: center;
      border-top: 1px solid #133c54;
      padding-top: 24px;
      color: #84a2b6;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
    </div>
  </header>
  
  <div class="breadcrumb">
    <a href="/">トップ</a> &gt; <a href="/winter-lipidure.html">高保水リピジュアコスメ</a>
  </div>
  
  <main class="main-container">
    <article class="article-header">
      <span class="article-badge">2026-2027年 冬季最新・人工角層バリア特集</span>
      <h1>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の2倍の保水膜で冬の乾燥冷風を完全ブロックする高保水リピジュアコスメランク10</h1>
      <div class="meta-box">
        <span>📅 公開日: 2026年11月4日</span>
        <span>✍️ 執筆・監修: 冬コスメ徹底比較ラボ 編集部</span>
        <span>⏱️ 読了目安: 約12分</span>
      </div>
      <p class="lead-text">
        11月から12月にかけて、木枯らしとともに湿度が急激に下がり、オフィスのエアコン温風が一日中素肌の水分を奪い去る過酷な季節。「朝しっかり保湿してメイクしたはずなのに、お昼過ぎには頬が突っ張って粉を吹く」「ファンデーションが乾燥崩れして毛穴落ちが目立つ」という悩みを抱えていませんか？
      </p>
      <p class="lead-text">
        その根本原因は、外気の激しい乾燥によって、塗布した化粧水の水分が肌から逃げ出してしまう『水分の蒸散』にあります。この過酷な環境下で圧倒的な保水力を発揮するのが、医療用の人工血管やコンタクトレンズの保水剤から誕生した生体適合性ポリマー『リピジュア（ポリクオタニウム-51）』です。ヒアルロン酸の約2倍の保水力を持ち、水洗いしても落ちない耐水性バリア膜を形成するリピジュアコスメから、楽天で今すぐ買えるおすすめ名品10選を徹底比較します。
      </p>
      
      <div class="toc-box">
        <div class="toc-title">📑 目次（タップで各項目へジャンプ）</div>
        <ol class="toc-list">
          <li><a href="#mechanism">なぜ真冬のオフィス暖房乾燥に「リピジュア（ポリクオタニウム-51）」が最強なのか？</a></li>
          <li><a href="#selection">冬のリピジュアコスメ選びで失敗しないための4大チェックポイント</a></li>
          <li><a href="#ranking">真冬の高保水リピジュア（ポリクオタニウム-51）コスメおすすめ人気ランキング10選</a></li>
          <li><a href="#synergy">美容のプロ直伝！リピジュア×セラミドの『二重シールド』で一日中乾かない美肌術</a></li>
          <li><a href="#faq">リピジュアコスメに関するよくある質問（FAQ）</a></li>
          <li><a href="#related">あわせて読みたい冬の集中高保湿ケア特集</a></li>
        </ol>
      </div>
    </article>
    
    <section class="guide-section" id="mechanism">
      <h2>なぜ真冬のオフィス暖房乾燥に「リピジュア（ポリクオタニウム-51）」が最強なのか？</h2>
      <p>
        肌の乾燥対策として最も有名なヒアルロン酸ですが、実は湿度が30%を下回る真冬のエアコン暖房環境下では、自身の抱えた水分を空気中に奪われてしまいやすいという弱点があります。一方、日本の技術が生んだ高機能保湿成分『リピジュア（ポリクオタニウム-51）』は、過酷な低湿度環境でも水分をガッチリ抱え込み続ける特性を持っています。
      </p>
      <p>
        リピジュアは、ヒトの生体膜（細胞膜）を構成する主要成分であるリン脂質（ホスホリルコリン極性基）を人工的に合成した生体適合性高分子です。医療現場で人工血管や人工心臓の内壁コーティング、あるいはドライアイを防ぐコンタクトレンズの保水剤として実用化されているほど、人体への親和性と安全性が証明されています。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>💧 1. ヒアルロン酸の約2倍の水分保持力</h4>
          <p>同じ濃度のヒアルロン酸水溶液と比較して約2倍の保水力を誇り、乾いた外気に触れても水分を放出しません。11月〜12月の乾燥した室内でも潤いが蒸発しません。</p>
        </div>
        <div class="grid-card">
          <h4>🛡️ 2. 水洗いしても落ちない「耐水性バリア」</h4>
          <p>肌表面のタンパク質となじんで強固なナノヴェール（人工角層）を形成。水で洗顔しても約80%以上の保水効果が皮膚表面に留まるため、夕方まで潤いが長持ちします。</p>
        </div>
        <div class="grid-card">
          <h4>🔬 3. ラメラ液晶構造の自己組織化</h4>
          <p>角質細胞間脂質（セラミドや脂肪酸）と同じような層状構造（ラメラ構造）を肌表面で自発的に形成し、乱れたキメの凹凸をなめらかに埋めて外部刺激を遮断します。</p>
        </div>
      </div>
    </section>
    
    <section class="guide-section" id="selection">
      <h2>冬のリピジュアコスメ選びで失敗しないための4大チェックポイント</h2>
      <p>
        リピジュアの類まれな保水力を最大限に活かすために、アイテムを選ぶ際にチェックすべき4つのポイントをまとめました。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>① セラミドとの同時配合（Wバリア処方）</h4>
          <p>リピジュアは主に角層の『表面保護』に優れています。そのため、角層の『内部（細胞間脂質）』を満たすヒト型セラミド（松山油脂など）が同時配合された製品を選ぶと、内外両面から乾燥を完璧にブロックできます。</p>
        </div>
        <div class="grid-card">
          <h4>② アイテム形状（化粧水・美容液・クリーム）</h4>
          <p><strong>・化粧水タイプ：</strong> 朝晩バシャバシャ使って角層全体に保水膜を行き渡らせる。<br>
          <strong>・美容液タイプ：</strong> 高濃度配合で夕方の乾燥崩れや目元・口元の小ジワを集中ケア。<br>
          <strong>・クリームタイプ：</strong> 油分とリピジュア膜で寝ている間の水分蒸散を完全阻止。</p>
        </div>
        <div class="grid-card">
          <h4>③ 成分表示名称（ポリクオタニウム-51）</h4>
          <p>全成分表示では『ポリクオタニウム-51』と記載されます。表示順が上位にあるものや、チューンメーカーズのように原液ブレンドを謳うアイテムは高い保水実感を得られます。</p>
        </div>
        <div class="grid-card">
          <h4>④ 低刺激・アルコールフリー設計</h4>
          <p>冬の乾燥でバリアが低下した肌は、アルコールや強い防腐剤で刺激を感じやすいもの。無香料・無着色・アルコールフリーの低刺激処方を選びましょう。</p>
        </div>
      </div>
    </section>
    
    <section id="ranking">
      <h2 style="font-size: 1.6rem; color: #0c364c; border-bottom: 3px solid #0284c7; padding-bottom: 10px; margin-bottom: 36px; font-weight: 800;">
        🏆 真冬の高保水リピジュア（ポリクオタニウム-51）コスメおすすめ人気ランキング10選
      </h2>
      
      {cards_str}
      
    </section>
    
    <section class="guide-section" id="synergy">
      <h2>美容のプロ直伝！リピジュア×セラミドの『二重シールド』で一日中乾かない美肌術</h2>
      <p>
        冬の厳しい乾燥環境を乗り切るための最強テクニックが、皮膚科学に基づいた『セラミド×リピジュアの二重シールド法』です。
      </p>
      <div class="guide-grid">
        <div class="grid-card">
          <h4>1. まずはリピジュア化粧水で角層に水分の道を引く</h4>
          <p>洗顔後、松山油脂やラフラ、無印良品などのリピジュア配合化粧水をたっぷりなじませます。角質細胞のすみずみまでナノサイズの水分が行き渡り、表面に潤いの下地が整います。</p>
        </div>
        <div class="grid-card">
          <h4>2. ヒト型セラミド美容液で細胞間をがっちり接着</h4>
          <p>化粧水がなじんだら、ヒト型セラミド美容液を重ねます。細胞と細胞の隙間をセメントのように埋め、水分が蒸散する隙間をなくします。</p>
        </div>
        <div class="grid-card">
          <h4>3. 仕上げのリピジュアクリームで人工角層シールドを密着</h4>
          <p>最後にリピジュアやシアバター配合のクリームで蓋をします。肌表面に水洗いしても落ちない耐水性フィルムが完成し、暖房直風にもびくともしない鉄壁の美肌が完成します。</p>
        </div>
      </div>
    </section>
    
    <section class="faq-section" id="faq">
      <h2>リピジュアコスメに関するよくある質問（FAQ）</h2>
      {faq_str}
    </section>
    
    <section class="internal-section" id="related">
      <h2>あわせて読みたい！冬の乾燥撃退・集中保湿スキンケア特集</h2>
      <div class="internal-grid">
        <a href="/winter-ceramide-cream.html" class="internal-card">
          <h4>🛡️ 高保湿セラミドクリーム10選</h4>
          <p>角層の細胞間脂質をガッチリ補強。リピジュアと組み合わせたい冬の鉄壁保湿クリーム。</p>
        </a>
        <a href="/winter-spicule.html" class="internal-card">
          <h4>🪡 高保湿スピキュール（針美容液）10選</h4>
          <p>天然マイクロニードルが角層深部へ通り道を開く！リピジュアの浸透力を最大化する導入コスメ。</p>
        </a>
        <a href="/winter-stem-cell.html" class="internal-card">
          <h4>🧬 高保湿ヒト幹細胞コスメ10選</h4>
          <p>肌細胞の根源から保水力を呼び覚ます！冬枯れ肌の密度を高める最高峰エイジングケア。</p>
        </a>
        <a href="/winter-hyaluronic-serum.html" class="internal-card">
          <h4>💧 高保水ヒアルロン酸美容液10選</h4>
          <p>リピジュアと相乗効果を発揮する水分保持の王様。乾いた角層に大量の水分を蓄える。</p>
        </a>
        <a href="/winter-shea-butter.html" class="internal-card">
          <h4>🧈 高保湿シアバターコスメ10選</h4>
          <p>アフリカの大自然が育んだ濃密植物油脂。リピジュアの上から重ねて水分を完全密閉する。</p>
        </a>
        <a href="/winter-vaseline.html" class="internal-card">
          <h4>🛡️ 高純度ワセリンおすすめ10選</h4>
          <p>水分蒸散をゼロに抑える究極の物理シールド。真冬の粉吹き肌・ひび割れを救う救世主。</p>
        </a>
      </div>
    </section>
  </main>
  
  <footer>
    <div class="footer-inner">
      <div class="footer-links">
        <a href="/">トップページ</a>
        <a href="/winter-lipidure.html">高保水リピジュア</a>
        <a href="/winter-spicule.html">高保湿スピキュール</a>
        <a href="/winter-stem-cell.html">高保湿ヒト幹細胞</a>
        <a href="/winter-rosehip-oil.html">高保湿ローズヒップオイル</a>
        <a href="/winter-honey.html">高保湿ハチミツコスメ</a>
        <a href="/winter-mugwort.html">高保水ヨモギコスメ</a>
        <a href="/winter-marula-oil.html">高保湿マルラオイル</a>
        <a href="/winter-birch-juice.html">高保水白樺樹液</a>
        <a href="/winter-azelaic-acid.html">高濃度アゼライン酸</a>
        <a href="/winter-ceramide-cream.html">高保湿セラミドクリーム</a>
      </div>
      <div class="footer-copy">
        &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved. 当サイトは楽天アフィリエイトプログラムに参加しています。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-lipidure.html", "w", encoding="utf-8") as f:
    f.write(full_html.strip())

print("✅ winter-lipidure.html generated successfully!")
