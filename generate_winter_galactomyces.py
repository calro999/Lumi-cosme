import json
import re

with open("fetched_3new_nov_dec_proteoglycan_propolis_galactomyces_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_galactomyces"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計販売数数百万本の世界的メガヒット！ガラクトミセス93.69%＋高濃度ナイアシンアミド",
        "catch": "冬枯れくすみ肌に圧倒的な透明感と水分密度を充填。キメの整った毛穴レスな陶器肌へ導く導入美容液",
        "brand_name": "魔女工場 (Manyo Factory)",
        "capacity": "50ml (ガラク ナイアシン 2.0 エッセンス)",
        "type": "高純度ガラクトミセス発酵ブースターエッセンス",
        "features": "ガラクトミセス発酵ろ過物93.69%、ナイアシンアミド4%、ヒアルロン酸Na、低刺激ヴィーガン認証",
        "value": "低温培養で抽出された高純度ガラクトミセスが角層のNMF生成を促進し、4%のナイアシンアミドが冬の乾燥くすみを一掃。ベタつかず角層深部を潤いで満たす",
        "desc_p1": "11月から12月にかけて気温が下がり空気が乾燥すると、肌のターンオーバーが停滞して古い角質が蓄積し、顔全体がどんよりと茶色くくすんで見えがちです。韓国コスメ界の殿堂入り美容液として知られる魔女工場のガラク ナイアシン 2.0 エッセンスは、厳選されたガラクトミセス発酵ろ過物を93.69%という極めて高い濃度で配合した発酵導入液です。",
        "desc_p2": "テクスチャーは水のようにサラサラとしており、洗顔直後の肌に乗せると一瞬で角層の隙間に浸透。天然保湿因子（NMF）の産生を力強くサポートし、細胞一つひとつの水分保持能を底上げします。さらに4%配合されたナイアシンアミドがメラニンの移動を抑制し、冬特有の乾燥くすみとキメの乱れを同時に解消。朝晩使い続けることで、ファンデーションのトーンが1段階上がったかのような澄んだ透明美肌を実感できます。",
        "target": "冬になると肌がくすんで透明感が失われる方、毛穴の開きやキメの粗さが気になる方、サラッとした使い心地で高保湿を叶えたい方",
        "point": "洗顔直後の無垢な肌に、スポイト1回分を取り顔全体に優しくなじませます。特にくすみやすい頬骨まわりや乾燥する口角には、手のひらで軽く押し込むようにハンドプレスしてください。"
    },
    {
        "rank": 2,
        "tag": "👑 奇跡の独自酵母ピテラを90%以上配合！半世紀愛される最高峰フェイシャルトリートメント",
        "catch": "素肌の運命を変える伝説のエッセンス。冬の過酷な環境でも揺るがない強靭な角層バリアを確立",
        "brand_name": "SK-II (エスケーツー)",
        "capacity": "230ml (フェイシャル トリートメント エッセンス)",
        "type": "独自発酵酵母ピテラ（ガラクトミセス培養液）高配合化粧液",
        "features": "ピテラ（ガラクトミセス培養液/整肌保湿成分）90%以上配合、50種以上の微量栄養素（アミノ酸・ミネラル・有機酸）",
        "value": "杜氏の手の美しさから着想を得て発見された伝説の酵母発酵成分。肌の本来持つ天然保湿因子（NMF）と酷似した組成を持ち、真冬の乾燥環境でも肌自ら潤う力を引き出す",
        "desc_p1": "冬の乾燥対策において『一時的な保湿』ではなく『肌そのものの水分自給力を鍛えたい』と願うすべての女性の憧れ、SK-IIのフェイシャル トリートメント エッセンス。酒造りの職人である杜氏の手が驚くほど白く滑らかであったことから生まれた、ピテラ（ガラクトミセス培養液）を90%以上も配合した最高峰のスキンケアです。",
        "desc_p2": "独特の発酵香は純粋なピテラが高濃度である証拠。パッティングするたびに50種類以上のビタミン、アミノ酸、ミネラルが角層の深部へと吸い込まれ、硬くこわばった冬の角質を滑らかに整えます。エアコン暖房による水分蒸発を食い止め、キメの乱れ、透明感、ハリ、ツヤ、弾力のすべてを高次元で引き上げます。冬のボーナスで手に入れたい永遠の銘品です。",
        "target": "30代・40代からの本格エイジングケアを始めたい方、冬の乾燥による複合的な肌トラブル（くすみ・小ジワ・ハリ低下）を根本解決したい方",
        "point": "コットンに500円玉大をたっぷり含ませ、顔全体を優しくリズミカルにパッティングします。肌がひんやりとして手のひらに吸い付くまでじっくり入れ込むのが効果を倍増させる秘訣です。"
    },
    {
        "rank": 3,
        "tag": "⚖️ ガラクトミセス95%配合の超高濃縮トーンエッセンス！水分の油分バランスを黄金比に整える",
        "catch": "肌本来の水分保持力を呼び覚ます。乾燥とベタつきが混在する冬のインナードライを徹底攻略",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "100ml (ガラクトミセス 95 トーン バランシング エッセンス)",
        "type": "高濃度発酵バランシングトーンエッセンス",
        "features": "ガラクトミセス発酵ろ過物95%、ナイアシンアミド2%、ヒアルロン酸、アデノシン配合",
        "value": "95%という高純度発酵エキスが角層をみずみずしく潤し、ナイアシンアミドとアデノシンがハリと透明感をバックアップ。100mlの大容量で惜しみなく使える",
        "desc_p1": "冬の肌は、表面はカサつくのにTゾーンは皮脂でテカるという『インナードライ』に陥りやすくなります。COSRXのガラクトミセス95エッセンスは、発酵ろ過物を95%配合し、角層の水分油分バランスを理想的な中庸状態へとコントロールする機能派トリートメントです。",
        "desc_p2": "とろみのある滑らかな美容液が肌に触れるとスッと液状に変化し、摩擦レスに伸び広がります。アデノシンが乾燥小ジワをケアしながら、ガラクトミセスの豊富なアミノ酸が角層細胞の隙間を水分で満たします。使い続けることで肌の皮脂過剰が収まり、ふっくらと柔らかなマシュマロ肌へと導きます。",
        "target": "冬でもTゾーンがテカるのに頬が突っ張るインナードライ肌の方、コスパの良い大容量発酵美容液を求める方",
        "point": "洗顔後、化粧水で整えた肌に2〜3プッシュを取り、顔の内側から外側へ優しく伸ばします。乾燥しやすい頬には重ねてハンドプレスしてください。"
    },
    {
        "rank": 4,
        "tag": "🌱 余計な添加物ゼロの100%植物性ヴィーガン発酵！必要な成分だけをダイレクトに届けるDIYエキス",
        "catch": "シンプルな原液処方だから肌に素直に響く。手持ちの化粧水に混ぜて発酵パワーをプラス",
        "brand_name": "ONE THING (ワンシング)",
        "capacity": "150ml (ガラクトミセス 培養液)",
        "type": "100%ガラクトミセス発酵植物性培養液",
        "features": "ガラクトミセス培養液100%、ヴィーガン認証取得、EWGグリーン等級原料使用",
        "value": "1つの成分だけに特化したシンプル設計。防腐剤や香料などの肌負担を徹底排除し、純粋なガラクトミセスの力だけで冬の素肌力を底上げする",
        "desc_p1": "『肌に不要なものは一切与えたくない』というクリーンビューティー志向の女性から圧倒的支持を集めるONE THING。ガラクトミセス培養液のみをボトルに詰めた、極めてピュアな発酵トナーです。",
        "desc_p2": "サラッとした水のような感触で、コットンパックに最適。洗顔後の肌にたっぷりと含ませて5分間パックすることで、乾燥でゴワついた角質が柔らかく解きほぐされ、驚くほどの透明感と吸水性が蘇ります。手持ちのクリームやオイルにブレンドしてオリジナルの発酵コスメを作るのもおすすめです。",
        "target": "敏感肌で添加物が気になる方、コットンパックで集中透明感ケアをしたい方、手持ちコスメをカスタムしたい方",
        "point": "コットンにたっぷり浸して、頬や額などの乾燥・くすみスポットに3〜5分密着させるローションパックが最も効果的です。拭き取り用としても優れています。"
    },
    {
        "rank": 5,
        "tag": "🔬 国産高純度ガラクトミセス原液！自社製造だから実現した無添加＆高濃度の本格派エッセンス",
        "catch": "原料メーカーのこだわりが凝縮。冬の乾燥で硬化した角層を柔らかくほぐし潤いの通り道を開く",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "20ml (ガラクトミセス エッセンス GM)",
        "type": "高純度ガラクトミセス原液美容液",
        "features": "国産ガラクトミセス培養液高濃度配合、完全無添加（パラベン・合成香料・着色料・アルコールフリー）",
        "value": "徹底した品質管理のもと国内ラボで製造。希釈されていないピュアなガラクトミセスエキスが、真冬の乾燥小ジワとくすみを集中ケアする",
        "desc_p1": "冬の肌トラブルの多くは、角層の水分を引き込む『呼び水』が不足していることから起こります。基礎化粧品研究所（KISO）のガラクトミセスエッセンスGMは、国産の高品質なガラクトミセス培養液をそのままボトルに詰めた高純度原液です。",
        "desc_p2": "とろみ剤などの不要な添加物が入っていないため、肌への吸い込みスピードが抜群。洗顔直後の素肌に数滴馴染ませるだけで、角層の柔軟性が一気に高まり、その後に重ねる化粧水や乳液の潤い保持力が飛躍的に向上します。敏感肌でも赤みや刺激を感じにくい優しい使い心地です。",
        "target": "原液コスメで本格的な保湿・透明感ケアをしたい方、安心の国産無添加にこだわりたい方、化粧水の入りが悪くなったと感じる方",
        "point": "洗顔後、化粧水の前に手のひらに3〜4滴取り、顔全体に優しくハンドプレスします。目元や口元など乾燥しやすい部分には指先でトントンと重ねてください。"
    },
    {
        "rank": 6,
        "tag": "🧪 極限発酵×温冷二重発酵が生んだ97%高濃縮！ミシャが誇る第5世代タイムレボリューション",
        "catch": "発酵エキスの粒子を極小化。角層深くまでスーッと吸い込まれる驚異の高浸透トリートメント",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "150ml (タイムレボリューション ザ ファースト トリートメント エッセンス 5X)",
        "type": "極限二重発酵酵母トリートメントエッセンス",
        "features": "極限発酵酵母培養液97%、温冷二重発酵プロセス採用、角質ケア・キメ改善処方",
        "value": "特殊な極限環境での発酵と温冷ろ過プロセスにより、美容成分を極小粒子化。真冬の冷えで閉ざされた肌へもしっかり潤いを届ける",
        "desc_p1": "冬の寒さによって肌表面が硬くなると、通常の化粧水では角層内部まで潤いが届きません。韓国コスメの先駆者ミシャが長年改良を重ねてきた『タイムレボリューション 5X』は、酵母エキスを温冷二重発酵させることで、成分の粒子をナノレベルまで極小化した高浸透エッセンスです。",
        "desc_p2": "肌に触れた瞬間に吸い込まれるような浸透感を誇り、塗布後の肌はベタつかずシルクのように滑らか。乱れた肌のキメをキュッと整え、真冬の寒冷外気や暖房の乾燥に晒されても乾きを感じさせないしなやかな強さを素肌に与えます。",
        "target": "冬になると肌が硬くゴワついて化粧水が入らない方、サラサラなのに深部が潤う浸透感を求める方、キメを整えたい方",
        "point": "洗顔直後のファーストステップとして、手またはコットンに適量を取り、優しく顔全体に馴染ませます。重ねづけするごとに肌の柔らかさが増していきます。"
    },
    {
        "tag": "🌹 西洋ダマスクローズ水×ガラクトミセスの贅沢融合！冬の乾燥枯れ肌を華やかに潤す高機能化粧水",
        "rank": 7,
        "catch": "優雅な天然ローズの香りに包まれて。保湿・引き締め・くすみケアを1本で完結させる発酵トナー",
        "brand_name": "Secret Key (シークレットキー)",
        "capacity": "150ml (スターティング トリートメント エッセンス ローズ)",
        "type": "ダマスクローズ水配合ガラクトミセスエッセンス",
        "features": "ガラクトミセス発酵ろ過物、ダマスクローズ花水水溶液、アルブチン、アデノシン",
        "value": "美肌効果で名高いダマスクローズ水とガラクトミセスを掛け合わせることで、保水力と抗酸化力を両立。冬のスキンケアタイムを心地よい香りで癒す",
        "desc_p1": "寒さで気分まで塞ぎがちな冬の朝晩に、スキンケアを至福のひとときに変えてくれるのがシークレットキーのローズトリートメントエッセンスです。高純度ガラクトミセスに天然ダマスクローズ水をブレンドした贅沢処方です。",
        "desc_p2": "みずみずしいローションが肌にスーッと浸透し、ローズの保湿成分が肌表面を優しくコーティング。アルブチンとアデノシンのダブルアプローチで、乾燥くすみを払いながらふっくらとしたハリをもたらします。ほのかな天然ローズの香りが心まで解きほぐします。",
        "target": "天然ローズの香りでリラックスしたい方、くすみと乾燥を同時にケアしたい方、デイリーにたっぷり使える発酵トナーを好む方",
        "point": "洗顔後、手のひらに適量を出して深呼吸しながら香りを楽しんだ後、顔全体に優しくハンドプレスして浸透させてください。"
    },
    {
        "rank": 8,
        "tag": "💎 ガラクトミセス発酵ろ過物95.7%の超高含有！SK-IIのジェネリックとして大人気の実力派",
        "catch": "価格は数分の一で効果は本物。惜しみなくバシャバシャ使って冬の乾燥小ジワを撃退",
        "brand_name": "FROM NATURE (フロムネイチャー)",
        "capacity": "150ml (AGE インテンス トリートメント エッセンス)",
        "type": "高純度ガラクトミセス発酵エイジングエッセンス",
        "features": "ガラクトミセス発酵ろ過物95.7%、ナイアシンアミド、アデノシン、ヒアルロン酸配合",
        "value": "高級デパコス発酵化粧水とほぼ同等の成分比率をプチプラで実現。冬の全身や首元の乾燥・シワケアにも気兼ねなくたっぷり使える",
        "desc_p1": "『高級なガラクトミセス化粧水を毎日惜しみなく使いたい』という声に応えて大ヒットしているのがフロムネイチャーのAGEインテンスエッセンスです。発酵ろ過物を95.7%も配合しながら、驚異的なリーズナブルさを誇ります。",
        "desc_p2": "とろみのあるまろやかなテクスチャーで、肌に伸ばすとスーッと広がって角層に潤いの層を形成します。ナイアシンアミドとアデノシンがしっかり配合されているため、冬の乾燥小ジワやたるみ毛穴のケアにも頼もしい存在。朝晩のスキンケアで首やデコルテまでたっぷり使うのがおすすめです。",
        "target": "プチプラで高濃度のガラクトミセスを試したい方、首やデコルテまで広範囲に発酵ケアを行いたい方、乾燥小ジワが気になる方",
        "point": "洗顔後、500円玉大を手にとって顔全体から首筋までなじませます。乾燥が気になる日は2〜3回重ねづけすると潤いの密度が跳ね上がります。"
    },
    {
        "rank": 9,
        "tag": "💧 原料メーカー直販のピュア培養液！大容量100mlで手持ちのコスメを手軽に発酵スキンケアへ格上げ",
        "catch": "シンプルな全成分で安心。肌本来のNMF生成をサポートし冬のゴワつきをリセット",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml (ガラクトミセス培養液)",
        "type": "無添加ガラクトミセス高保水培養液",
        "features": "ガラクトミセス培養液、パラベンフリー、フェノキシエタノールフリー、国内精製",
        "value": "手作りコスメ原料の老舗が手がける無添加エキス。シンプルだからこそ敏感肌でも安心して使え、冬のバリア機能を土台から強化する",
        "desc_p1": "余計な香料や着色料、防腐剤を極力避けたい敏感肌の方に最適なのが、自然化粧品研究所のガラクトミセス培養液です。国内のクリーンな工場で丁寧に精製された大容量100mlボトルです。",
        "desc_p2": "水のようにさらりとした質感で、肌への浸透が非常に速いのが特徴。角層の天然保湿因子（NMF）と親和性が高いため、肌に乗せるとスッと吸い込まれ、内側からしっとりとしたうるおいを保ちます。手持ちの化粧水に10%程度ブレンドして使うなど、アレンジも自由自在です。",
        "target": "完全無添加の安全な発酵コスメを求める敏感肌の方、大容量で長く使いたい方、手作りコスメを楽しみたい方",
        "point": "洗顔直後のブースターとしてそのまま肌になじませるか、手持ちのシンプルな化粧水に数滴垂らして混ぜて使用してください。"
    },
    {
        "rank": 10,
        "tag": "⚡ 発酵ブースター×マルチビタミン導入！冬のどんより疲労肌を即効チャージするオールインワン液",
        "catch": "ガラクトミセスが角層を耕しビタミンが浸透。真冬の過酷な乾燥でも明るくハリのある素肌へ",
        "brand_name": "VELY VELY (ブリーブリー)",
        "capacity": "150ml (ガラクトミセス オールインワン ブースティング エッセンス)",
        "type": "発酵ガラクトミセス角層導入ブースター",
        "features": "ガラクトミセス発酵抽出物、ビタミンコンプレックス、ヒアルロン酸複合体、弱酸性処方",
        "value": "ガラクトミセスによる角質柔軟化とビタミンの相乗効果で、冬の寒さでくすんだ肌を生き生きと蘇らせるオールインワン設計",
        "desc_p1": "忙しい冬の朝、何ステップも重ねる時間がないけれど乾燥やくすみはしっかり防ぎたい方に最適なのが、VELY VELYのガラクトミセス ブースティング エッセンスです。導入液・化粧水・美容液の役割を兼ね備えた高機能エッセンスです。",
        "desc_p2": "とろみのあるジェルローションが肌の上でスッとほどけ、微細な発酵成分が角層深部へすばやく浸透。ビタミン複合成分が冬の乾燥くすみを明るく照らし、夕方までツヤやかなハリ感をキープします。メイク前に使うとファンデーションの密着感が格段にアップします。",
        "target": "朝のスキンケアをスピーディーに完了させたい方、くすみと乾燥を同時にケアしたい方、ツヤ肌ベースを作りたい方",
        "point": "洗顔後、1〜2プッシュを手にとり顔全体に優しく塗り広げます。手のひら全体で包み込むように密着させた後、すぐに乳液やクリームで保護してください。"
    }
]

# JSON-LD構造化データ作成
faq_data = [
    {
        "q": "ガラクトミセスとはどのような成分ですか？なぜ冬の乾燥やくすみに効くのですか？",
        "a": "ガラクトミセスは、お酒を造る醸造所で使われる天然酵母の一種をじっくり発酵・培養して得られる発酵ろ過エキスです。アミノ酸、ペプチド、ビタミンB群、ミネラル、有機酸など50種類以上の美肌成分を含み、人の肌にもともと備わっている天然保湿因子（NMF）と極めて類似した組成を持ちます。11月・12月の冬は寒さで角層が硬化し水分を抱え込めなくなりますが、ガラクトミセスが角質を柔らかくほぐし、肌本来のNMF生成をサポートすることで、内側から湧き出るような透明感と高密度の潤いを取り戻します。"
    },
    {
        "q": "独特の匂い（お酒や酵母のような香り）はありますか？",
        "a": "高純度なガラクトミセス発酵化粧品（特にSK-IIやピュア原液など）は、酵母が発酵する過程で生じる独特の自然な発酵香（少し酸味のあるような香り）がします。これは人工香料を添加せず、有効成分がそのまま高濃度に含まれている証拠です。多くの製品は肌になじませると数秒で香りが消えるため、慣れると気にならなくなります。"
    },
    {
        "q": "レチノールやビタミンC、ナイアシンアミドと一緒に併用しても問題ありませんか？",
        "a": "非常に相性が良く、むしろ併用が強く推奨されます。ガラクトミセスが角層を整えて浸透ルートを切り拓くため、後から使うビタミンCやレチノールの浸透効率が飛躍的に高まります。また、魔女工場のようにガラクトミセスとナイアシンアミドが最初から黄金比率でブレンドされている製品も多く、冬の乾燥小ジワとくすみ対策に最高のシナジーを生み出します。"
    },
    {
        "q": "ガラクトミセス美容液はどの順番で使用するのがベストですか？",
        "a": "テクスチャーが水のようにサラサラしている製品（魔女工場やSK-IIなど）は、『洗顔直後（化粧水の前、または化粧水代わり）』のファーストステップで使うのが最も効果的です。角層深部まで一気に浸透し、その後の乳液やクリームの保湿保持力を何倍にも高めてくれます。"
    },
    {
        "q": "11月〜12月の真冬にガラクトミセスの効果を最大化する使い方のコツは？",
        "a": "『コットンパック』による集中補給が劇的な効果を発揮します。週に2〜3回、大判の薄手コットンにガラクトミセスエッセンスをたっぷり含ませ、乾燥やくすみが気になる両頬や額に3〜5分間密着させてください。角層の水分密度が満タンになり、まるで内側から発光するような極上の透明ツヤ肌に仕上がります。"
    }
]

schema_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10",
    "description": "11月・12月の真冬乾燥・くすみ・キメの乱れに！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液10選を徹底比較。魔女工場、SK-II、COSRX、KISOなど厳選。",
    "image": items[0]["img_url"],
    "datePublished": "2026-11-03T12:00:00+09:00",
    "dateModified": "2026-11-03T12:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部",
        "url": "https://lumi-cosme.vercel.app/"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-galactomyces"
    }
}

schema_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": it["rank"],
            "name": it["name"],
            "item": {
                "@type": "Product",
                "name": it["name"],
                "image": it["img_url"],
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "JPY",
                    "price": str(it["price"]),
                    "availability": "https://schema.org/InStock",
                    "url": it["affiliate_url"]
                }
            }
        } for it in items
    ]
}

schema_faq = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": f["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f["a"]
            }
        } for f in faq_data
    ]
}

schema_breadcrumb = {
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
            "name": "高浸透ガラクトミセス美容液ランク10",
            "item": "https://lumi-cosme.vercel.app/winter-galactomyces"
        }
    ]
}

# 商品カードHTML構築
items_html = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    
    items_html += f"""
    <!-- Rank {p['rank']} -->
    <div class="product-card" id="rank-{p['rank']}">
      <div class="product-rank-badge">第{p['rank']}位</div>
      <div class="product-header">
        <span class="product-tag">{p['tag']}</span>
        <h3 class="product-title">{p['catch']}</h3>
        <div class="product-meta">
          <span class="product-brand">ブランド: {p['brand_name']}</span>
          <span class="product-capacity">規格・容量: {p['capacity']}</span>
          <span class="product-type">タイプ: {p['type']}</span>
        </div>
      </div>

      <div class="product-body">
        <div class="product-img-wrap">
          <img src="{it['img_url']}" alt="{it['name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-price-box">
            <span class="price-label">楽天市場参考価格:</span>
            <span class="price-val">{price_str}</span>
            <span class="price-tax">(税込・送料込目安)</span>
          </div>
          <div class="product-features">
            <strong>主成分・処方特徴:</strong> {p['features']}
          </div>
          <div class="product-value-point">
            <strong>冬の高保湿アプローチ:</strong> {p['value']}
          </div>
        </div>
      </div>

      <div class="product-desc">
        <p class="desc-lead">{p['desc_p1']}</p>
        <p class="desc-detail">{p['desc_p2']}</p>
      </div>

      <div class="product-advice-grid">
        <div class="advice-box target-box">
          <div class="advice-title">💡 こんな肌悩みの方に最適</div>
          <p>{p['target']}</p>
        </div>
        <div class="advice-box usage-box">
          <div class="advice-title">🧴 保湿効果を最大化する使用法</div>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-cta">
        <a href="{it['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener nofollow">
          楽天市場で詳細・最安値をチェック <span>→</span>
        </a>
      </div>
    </div>
    """

# 比較テーブル作成
table_rows = ""
for idx, p in enumerate(product_details):
    it = items[idx]
    price_str = f"¥{it['price']:,}" if it['price'] > 0 else "オープン価格"
    table_rows += f"""
    <tr>
      <td class="tbl-rank">第{p['rank']}位</td>
      <td class="tbl-name"><a href="#rank-{p['rank']}">{p['brand_name']}<br><strong>{p['capacity']}</strong></a></td>
      <td class="tbl-type">{p['type']}</td>
      <td class="tbl-feat">{p['features']}</td>
      <td class="tbl-price">{price_str}</td>
    </tr>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の真冬乾燥に！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液10選を徹底比較！魔女工場、SK-II、COSRX、KISOなど厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-galactomyces">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP -->
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10 | 冬コスメ徹底比較ラボ">
  <meta property="og:description" content="11月・12月の真冬乾燥に！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液10選を徹底比較！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-galactomyces">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta name="twitter:card" content="summary_large_image">

  <!-- JSON-LD 構造化データ -->
  <script type="application/ld+json">
  {json.dumps(schema_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_faq, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_breadcrumb, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0d9488;
      --primary-light: #ccfbf1;
      --primary-dark: #0f766e;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --bg-light: #f0fdfa;
      --border-color: #99f6e4;
      --card-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --card-hover-shadow: 0 10px 15px -3px rgba(13, 148, 136, 0.12), 0 4px 6px -4px rgba(0, 0, 0, 0.05);
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
      background-color: #f8fafc;
    }}

    .site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border-color);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-inner {{
      max-width: 1000px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .container {{
      max-width: 900px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-wrap {{
      background: #ffffff;
      padding: 3rem 2.5rem;
      border-radius: 12px;
      box-shadow: var(--card-shadow);
      border: 1px solid #ccfbf1;
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .breadcrumb a {{
      color: var(--primary-dark);
      text-decoration: none;
    }}

    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #134e4a;
      margin-bottom: 1.5rem;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 2rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #99f6e4;
    }}

    .lead-box {{
      background: #f0fdfa;
      border-left: 4px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      line-height: 1.8;
      color: #115e59;
    }}

    .section-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #134e4a;
      margin: 3rem 0 1.5rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid #ccfbf1;
      border-radius: 12px;
      padding: 2rem;
      margin-bottom: 3rem;
      position: relative;
      box-shadow: var(--card-shadow);
      transition: box-shadow 0.2s ease;
    }}

    .product-card:hover {{
      box-shadow: var(--card-hover-shadow);
    }}

    .product-rank-badge {{
      position: absolute;
      top: -12px;
      left: 1.5rem;
      background: #0d9488;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.9rem;
      padding: 0.25rem 1rem;
      border-radius: 20px;
      box-shadow: 0 2px 4px rgba(13, 148, 136, 0.3);
    }}

    .product-header {{
      margin-top: 0.5rem;
      margin-bottom: 1.25rem;
    }}

    .product-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      margin-bottom: 0.5rem;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      line-height: 1.5;
      margin-bottom: 0.5rem;
    }}

    .product-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .product-body {{
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 1.5rem;
      align-items: center;
      margin-bottom: 1.5rem;
      background: var(--bg-light);
      padding: 1.25rem;
      border-radius: 8px;
    }}

    @media (max-width: 640px) {{
      .product-body {{
        grid-template-columns: 1fr;
      }}
      .article-wrap {{
        padding: 1.5rem 1rem;
      }}
    }}

    .product-img-wrap {{
      text-align: center;
      background: #ffffff;
      padding: 0.5rem;
      border-radius: 8px;
      border: 1px solid #99f6e4;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 200px;
      object-fit: contain;
    }}

    .product-price-box {{
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px dashed #99f6e4;
    }}

    .price-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #0f766e;
    }}

    .price-tax {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .product-features, .product-value-point {{
      font-size: 0.95rem;
      line-height: 1.6;
    }}

    .product-desc {{
      margin: 1.5rem 0;
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}

    .desc-lead {{
      margin-bottom: 1rem;
      font-weight: 500;
    }}

    .product-advice-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-bottom: 1.5rem;
    }}

    @media (max-width: 640px) {{
      .product-advice-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .advice-box {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
      line-height: 1.6;
    }}

    .target-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .usage-box {{
      background: #f0fdfa;
      border: 1px solid #99f6e4;
      color: #115e59;
    }}

    .advice-title {{
      font-weight: 700;
      margin-bottom: 0.35rem;
    }}

    .product-cta {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      background: linear-gradient(135deg, #0d9488, #0f766e);
      color: #ffffff;
      font-weight: 700;
      font-size: 1rem;
      padding: 0.85rem 2rem;
      border-radius: 50px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(13, 148, 136, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 420px;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 8px 12px -2px rgba(13, 148, 136, 0.35);
      background: linear-gradient(135deg, #14b8a6, #0d9488);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 2rem 0;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      background: #ffffff;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem 0.75rem;
      border: 1px solid #99f6e4;
      text-align: left;
    }}

    .comparison-table th {{
      background: #f0fdfa;
      color: #134e4a;
      font-weight: 700;
      white-space: nowrap;
    }}

    .tbl-rank {{
      font-weight: 700;
      color: var(--primary-dark);
      white-space: nowrap;
      text-align: center;
    }}

    .tbl-name a {{
      color: #0f172a;
      text-decoration: none;
    }}

    .tbl-name a:hover {{
      color: var(--primary);
    }}

    .tbl-price {{
      font-weight: 700;
      color: #0f766e;
      white-space: nowrap;
    }}

    .faq-list {{
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin: 2rem 0;
    }}

    .faq-item {{
      background: #f0fdfa;
      border: 1px solid #99f6e4;
      border-radius: 8px;
      padding: 1.25rem;
    }}

    .faq-q {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1rem;
      color: #134e4a;
      margin-bottom: 0.5rem;
    }}

    .faq-q-badge {{
      background: #0d9488;
      color: #ffffff;
      font-size: 0.8rem;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      flex-shrink: 0;
    }}

    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
      padding-left: 2rem;
    }}

    .internal-links-box {{
      background: #f0fdfa;
      border: 1px solid #99f6e4;
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3rem;
    }}

    .internal-links-title {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #134e4a;
      margin-bottom: 1.25rem;
      text-align: center;
    }}

    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 0.85rem;
    }}

    .internal-link {{
      display: block;
      background: #ffffff;
      border: 1px solid #99f6e4;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      text-decoration: none;
      color: #334155;
      font-size: 0.9rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }}

    .internal-link:hover {{
      border-color: #0d9488;
      color: #0d9488;
      transform: translateY(-2px);
      box-shadow: 0 2px 4px rgba(13, 148, 136, 0.1);
    }}

    .site-footer {{
      background: #ffffff;
      border-top: 1px solid #ccfbf1;
      padding: 2.5rem 0;
      margin-top: 4rem;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <span style="font-size: 0.85rem; color: #0f766e;">2026年最新 保湿ランキング</span>
    </div>
  </header>

  <main class="container">
    <article class="article-wrap">
      <div class="breadcrumb">
        <a href="/">ホーム</a> &gt; <span>高浸透ガラクトミセス美容液ランク10</span>
      </div>

      <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！角層の水分密度を極限まで高めて冬のくすみを晴らす高浸透ガラクトミセス美容液ランク10</h1>

      <div class="article-meta">
        <span>更新日: 2026年11月3日</span>
        <span>検証カテゴリー: 高浸透美容液・ガラクトミセス発酵エキス</span>
        <span>監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>

      <div class="lead-box">
        <strong>【11月・12月の冬本番に深刻化するゴワつき・浸透不全・冬枯れくすみを根本解決！】</strong><br>
        冷気が本格化し、室内暖房の風が容赦なく肌を奪う11月〜12月。「いつもの化粧水が肌表面で弾かれて全然入っていかない」「夕方になると肌がどんよりと黄ぐすみ、キメが乱れて疲弊して見える」という深刻な角質硬化と水分密度低下に悩む方が急増します。<br><br>
        冬の急激な寒暖差は、肌のターンオーバーを乱して古い角質を蓄積させ、角層内の天然保湿因子（NMF）の生成力を大幅に低下させます。そこで今冬、スキンケアのプロや成分マニアから圧倒的な支持を集めているのが<strong>『発酵の力で角層深部を耕すガラクトミセス培養液』</strong>です。<br><br>
        日本酒を造る杜氏の手の驚くべき若々しさから発見された天然酵母ガラクトミセスは、人の肌が本来持つNMFと極めて近いアミノ酸やミネラルを豊富に含有。硬くなった冬枯れ角質を優しくほぐし、角層の水分密度を極限まで高めて透明感を呼び覚ます、2026年最新の厳選10品を徹底検証・ランキング化しました。
      </div>

      <h2 class="section-title">🍶 ガラクトミセスが冬の過酷なゴワつき・くすみ乾燥を救う3大発酵アプローチ</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ガラクトミセス培養液は、天然酵母を丁寧に培養・発酵・ろ過して抽出される複合美肌エキスです。人工的な保湿成分では決して真似のできない、以下の3つの独自作用で冬の肌環境を根本改善します。</p>
        <ul style="margin: 1rem 0 1rem 1.5rem;">
          <li><strong>1. 天然保湿因子（NMF）と酷似したアミノ酸・ミネラル補給：</strong> 角層内で水分を掴んで離さない「天然保湿因子（NMF）」とアミノ酸組成がほぼ一致。冬の寒さで生産能力が落ちた肌に直接潤いの元を補給し、自ら水分を抱え込む土台を再建します。</li>
          <li><strong>2. 硬化した角質の柔軟化と浸透ブースター機能：</strong> 酵母発酵で生じる有機酸やペプチドが、寒冷刺激で肥厚・硬直した古い角質を優しくほぐします。肌の浸透ルートを再開通させ、後から重ねる化粧水やクリームの吸収効率を最大化します。</li>
          <li><strong>3. キメの整流化と乾燥黄ぐすみのブライトニング：</strong> ビタミンB群や微量元素の働きにより、乱れたターンオーバーを整流化。毛穴の影やキメの粗さによる凹凸くすみを払拭し、内側から透明な光を放つ澄んだ素肌へと整えます。</li>
        </ul>
      </div>

      <h2 class="section-title">🏆 高浸透ガラクトミセス美容液・発酵導入液おすすめランキング10選</h2>

      {items_html}

      <h2 class="section-title">📊 高浸透ガラクトミセス美容液10品 徹底スペック比較表</h2>
      <div class="comparison-table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品名・容量</th>
              <th>種別・タイプ</th>
              <th>主成分・処方特徴</th>
              <th>参考価格</th>
            </tr>
          </thead>
          <tbody>
            {table_rows}
          </tbody>
        </table>
      </div>

      <h2 class="section-title">💡 11月・12月の冬本番にガラクトミセスの効果を最大化する使用法</h2>
      <div style="margin-bottom: 2.5rem; font-size: 0.95rem; line-height: 1.8; color: #334155;">
        <p>ガラクトミセスの発酵パワーを活かし、冬でもくすまない潤い満タン肌を維持するための実践的ステップをご紹介します。</p>
        <div style="background: #f0fdfa; border: 1px solid #99f6e4; border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h3 style="font-size: 1.05rem; margin-bottom: 0.5rem; color: #0f766e;">① 洗顔後『30秒以内』にファーストステップとして塗布</h3>
          <p>冬の洗顔後は急速に角質が冷えて硬直します。タオルオフ後すぐにガラクトミセスを素肌に馴染ませることで、毛穴と角層が柔軟に保たれ、その後のスキンケア全体の浸透力が飛躍的にアップします。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0f766e;">② 週に2回の『5分間ローションパック』で水分密度を最大化</h3>
          <p>薄手のコットンにガラクトミセスエッセンスをたっぷりと浸し、乾燥やくすみが気になる両頬や額に貼って5分間パック。角層の水分密度が一気に満タンになり、エステ直後のような透き通るツヤ肌を実感できます。</p>
          <h3 style="font-size: 1.05rem; margin: 1rem 0 0.5rem; color: #0f766e;">③ ビタミンCやナイアシンアミドとの併用で相乗効果</h3>
          <p>ガラクトミセスで肌を整えた後にビタミンC美容液や高保湿ナイアシンアミドを重ねると、浸透性が高まりブライトニング効果が倍増します。冬のどんより疲労肌を一網打尽にする最強の組み合わせです。</p>
        </div>
      </div>

      <h2 class="section-title">❓ 専門家が答える！ガラクトミセスコスメのよくある質問</h2>
      <div class="faq-list">
        {"".join([f'''
        <div class="faq-item">
          <div class="faq-q">
            <span class="faq-q-badge">Q</span>
            <span>{f["q"]}</span>
          </div>
          <div class="faq-a">{f["a"]}</div>
        </div>
        ''' for f in faq_data])}
      </div>

      <div class="internal-links-box">
        <h3 class="internal-links-title">🔗 あわせて読みたい冬の高保湿スキンケア・コスメ特集</h3>
        <div class="internal-links-grid">
          <a href="/winter-proteoglycan" class="internal-link">🧬 高純度プロテオグリカン原液10選</a>
          <a href="/winter-propolis" class="internal-link">🐝 高保湿プロポリスアンプル10選</a>
          <a href="/winter-heparinoid" class="internal-link">🩺 薬用ヘパリン類似物質コスメ10選</a>
          <a href="/winter-placenta" class="internal-link">✨ 高濃度プラセンタ原液10選</a>
          <a href="/winter-vaseline" class="internal-link">🛡️ 高純度ワセリン高保湿10選</a>
          <a href="/winter-ceramide-lotion" class="internal-link">🧴 高保湿セラミド化粧水10選</a>
          <a href="/winter-ceramide-cream" class="internal-link">🧴 高保湿セラミドクリーム10選</a>
          <a href="/winter-rice-power" class="internal-link">🌾 米発酵・ライスパワー高保湿10選</a>
          <a href="/winter-amino-acid" class="internal-link">💧 高浸透アミノ酸コスメ10選</a>
          <a href="/winter-squalane-oil" class="internal-link">✨ 高純度スクワランオイル10選</a>
          <a href="/winter-argan-oil" class="internal-link">🥑 高保湿アルガンオイル10選</a>
          <a href="/winter-panthenol-cream" class="internal-link">🧪 高保湿パンテノールクリーム10選</a>
          <a href="/winter-horse-oil" class="internal-link">🐴 高保湿馬油クリーム10選</a>
          <a href="/winter-shea-butter" class="internal-link">🧈 高保湿シアバター10選</a>
          <a href="/winter-urea-cream" class="internal-link">🦶 高保湿尿素クリーム10選</a>
        </div>
      </div>

    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved.</p>
      <p style="margin-top: 0.5rem; font-size: 0.8rem; color: #94a3b8;">当サイトは楽天市場アフィリエイトプログラムに参加しており、適格販売により収入を得ています。</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-galactomyces.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-galactomyces.html!")
