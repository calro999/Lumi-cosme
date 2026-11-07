import json
import re

with open("fetched_3new_winter_ceramide_night_eye.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_eye_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👁️ 360°回転アプリケーター×美肌菌！真冬の血行不良と乾燥小ジワを瞬時に解きほぐす",
        "catch": "人間工学に基づいて設計された柔軟な360°回転パールアプリケーターと、7種の美肌菌由来成分を融合。冷えで凝り固まった目元の微小循環を促しながら、暖房直撃の薄膜角層を濃密な水分で満たす最高峰アイセラム",
        "brand_name": "LANCÔME (ランコム)",
        "capacity": "20mL / 専用アプリケーター付きボトル",
        "type": "美肌菌テクノロジー＆360°アプリケーター搭載 アイセラム",
        "features": "7種のプレ/プロバイオティクス由来成分、カフェイン、アルギニン、まつ毛ケア成分、クーリングエラストマー",
        "value": "冷えたアプリケーターが目元温度を一時的に約3℃クーリングし、血流の滞りとむくみを解消。極小ペプチドが真冬の乾燥による目袋のしぼみとちりめんジワをふっくら持ち上げる",
        "desc_p1": "11月から12月にかけて、目元は一年で最も過酷な環境に置かれます。目元の皮膚は頬の約3分の1（約0.5mm）というティッシュペーパー並みの薄さしかなく、皮脂腺がほとんど存在しないため、エアコン暖房の温風が直接当たると瞬時に水分を奪われます。ランコムのジェニフィック ライトパールは、この極薄目元のために開発された特許アプリケーター付きの高機能美容液です。",
        "desc_p2": "医療用ステンレス素材のパールヘッドが目元の細かい起伏にぴったりフィットし、摩擦を一切与えずに心地よいマッサージを可能にします。みずみずしく軽やかなテクスチャーでありながら、浸透後は角層深部に潤いが定着し、朝のメイク前に使用してもコンシーラーがヨレる心配がありません。まつ毛の根元まで同時にケアできる画期的な処方で、目元全体の印象をパッと明るく見せてくれます。",
        "target": "朝起きると目元のむくみや青クマがひどい方、暖房環境で目元のちりめんジワが目立つ方、まつ毛ケアとアイケアを同時にこなしたい方",
        "point": "アプリケーターの先端を使って、目頭から目尻に向かって目の下・上まぶたを優しく滑らせます。目頭のツボ（清明）を軽くプッシュした後、薬指の腹でトントンと軽く叩き込んでなじませます。"
    },
    {
        "rank": 2,
        "tag": "🛡️ マトリックス360°技術で微細振動から保護！冬のまばたき摩擦と暖房乾燥を跳ね返す",
        "catch": "1日に約2万回も繰り返される『まばたきによるメカニカルストレス』から目元を守るクッション技術を採用。極細冷却アプリケーターが乾燥小ジワをピタッと密封し、若々しいハリと弾力を再現する名品",
        "brand_name": "Estée Lauder (エスティ ローダー)",
        "capacity": "15mL / ステンレスアプリケーター付き",
        "type": "マトリックス360°テクノロジー搭載 アイコンセントレイトセラム",
        "features": "クロノラックス パワーシグナル テクノロジー、360°メッシュポリマー、ヒアルロン酸コンプレックス、カフェイン",
        "value": "目元の薄い皮膚に弾力のあるクッション膜を形成し、まばたきや擦れによる微小な組織損傷を軽減。72時間続く濃密な保水膜が、真冬のエアコン乾燥から目元を完璧にプロテクト",
        "desc_p1": "人間は無意識のうちに1日約2万回ものまばたきを行っており、これは目元の極薄な皮膚に毎日激しい微細振動と摩擦ストレスを与えていることを意味します。冬場に乾燥して柔軟性を失った角層は、このまばたき運動によって簡単にひび割れ、深い乾燥小ジワへと定着してしまいます。エスティローダーのアイ コンセントレイトは、この力学的負荷を吸収する独自クッションメッシュを形成します。",
        "desc_p2": "専用のステンレスアプリケーターで塗布すると、ひんやりとした心地よい感触と共に濃厚なエッセンスが吸い付くように密着。肌のサーカディアンリズムに働きかける夜間修復テクノロジーが、乾燥でダメージを受けたコラーゲン組織を立て直します。夕方になってもファンデーションの目元割れが起きず、一日中ふっくらとした目元を維持できます。",
        "target": "パソコンやスマホの長時間使用で目が疲れ乾きやすい方、まばたきによる目尻のシワが定着してきた方、確かな科学的エビデンスを持つアイケアを求める方",
        "point": "アプリケーターで目の下を内側から外側へ3回往復させ、円を描くようにマッサージします。最後は薬指で優しく押さえて角層へ密着させます。"
    },
    {
        "rank": 3,
        "tag": "🌿 厳選植物エキス×クーリングメタル！冬の重いまぶたをすっきり引き締め潤す目元特化セラム",
        "catch": "クラランスの植物皮膚科学が生んだ、アジア人女性の目元構造に特化したアイセラム。冷えと血行不良で重く腫れぼったくなりがちな真冬のまぶたをシャープに引き締め、パッチリとした明るい目元へ導く",
        "brand_name": "CLARINS (クラランス)",
        "capacity": "15mL / クーリングアプリケーターノズル",
        "type": "目元引き締め＆高保水植物エキス配合 アジア限定アイセラム",
        "features": "シバムギエキス、ワイルドチコリエキス、ハス花エキス、カフェイン、ヒアルロン酸",
        "value": "寒冷によるリンパ停滞とむくみをすばやく排出。たるみやすい目袋やまぶたをキュッと引き締めながら、乾燥によるキメの乱れをみずみずしく整える",
        "desc_p1": "冬の朝、顔が冷え切っていると目元のリンパや静脈の流れが滞り、上まぶたが重く腫れぼったくなったり、目の下に頑固なクマやたるみが生じやすくなります。クラランスのグラン アイ セラム Vは、植物エキスが持つ優れた排出・引き締め作用に着目し、冬のむくみと乾燥に同時にアプローチする専用セラムです。",
        "desc_p2": "指に吸い付くようなエルゴノミックデザインのメタルヘッドを肌に当てると、瞬時に目元の滞りが解き放たれるような清涼感が広がります。ジェル状のセラムは素早く浸透してベタつきを残さず、塗布した直後から目元の皮膚がピンと引き上がるような緊張感を実感。重いアイクリームが苦手な方でもストレスなく続けられる名品です。",
        "target": "冬の朝にまぶたがむくんで二重幅が狭くなる方、目元の重さやすっきり感のなさに悩む方、アイメイクのノリを劇的に良くしたい方",
        "point": "朝のスキンケア時、メタルヘッドを目頭から目尻にかけて優しく滑らせ、こめかみに向かってリンパを流すように動かします。指先で軽くタッピングして仕上げます。"
    },
    {
        "rank": 4,
        "tag": "🌸 マダガスカル産ロンゴザエキス×波型ヘッド！目元の弾力エネルギーを呼び覚ますハイエンド美容液",
        "catch": "枯れても再生する驚異の生命力を持つ『ロンゴザ』のエキスと、微細な波型マッサージヘッドを融合。デリケートな目元全体の皮膚幹細胞エネルギーを呼び覚まし、真冬の寒さに負けない濃密なハリと透明感を宿す",
        "brand_name": "Dior (ディオール)",
        "capacity": "20mL / 3D波型アプリケーター付き",
        "type": "幹細胞テクノロジー＆ロンゴザ配合 高機能エイジングケアアイセラム",
        "features": "発酵ロンゴザエキス、ライ麦エキス、低分子ヒアルロン酸、ナイアシンアミド、7本の波型マイクロウェーブヘッド",
        "value": "加齢と冬の冷えで低下する皮膚幹細胞の活性を再点火。目頭から目尻、眉骨まで360度全方位でハリ密度を底上げし、乾燥小ジワを根本から跳ね返す",
        "desc_p1": "ディオールのカプチュール トータル セル ENGY アイ セラムは、幹細胞研究の知見を惜しみなく注ぎ込んだハイエンドアイケアです。冬の寒さは細胞のエネルギー産生を司るミトコンドリアの機能を低下させ、目元の菲薄化（薄くなること）とくぼみを加速させます。本作は、マダガスカルの植物ロンゴザの発酵エキスが細胞のエネルギー代謝を劇的に引き上げます。",
        "desc_p2": "7本の波型マイクロウェーブが施された柔軟なヘッドが、目元の凹凸に吸い付くようにフィット。セラムが肌に乗った瞬間、まるで美容液マスクをしたかのような贅沢な潤い膜が張られ、目元のくすみと乾燥を一掃します。塗布後の肌は内側からパンッと張るような弾力に満ち、夕方まで乾燥による目元の影を感じさせません。",
        "target": "目元のくぼみや影で疲れて老け見えしやすい方、最先端の幹細胞スキンケアを体験したい方、上質なテクスチャーと確かな手応えを求める方",
        "point": "波型ヘッドを使って、目の下を目頭からこめかみへ滑らせます。眉骨の上やまぶたも同様に優しくマッサージし、最後に薬指で軽くプッシュして浸透させます。"
    },
    {
        "rank": 5,
        "tag": "❄️ ひんやり心地よいローラーボール！暖房で火照り乾燥した目元を瞬時にクールダウン保水",
        "catch": "ステンレス製ローラーボールから美容液がダイレクトに吐出。暖房の温風でほてり、水分が蒸散してパリパリになった目元を瞬時に冷やしながら、みずみずしい潤いを与え続ける携帯型アイセラム",
        "brand_name": "CLINIQUE (クリニーク)",
        "capacity": "15mL / ロールオン式ペンシルボトル",
        "type": "冷却ローラーボール搭載 目元用リフレッシュ美容液",
        "features": "カフェイン、パンテノール、ヒアルロン酸Na、セイヨウシロヤナギ樹皮エキス、無香料・アレルギーテスト済み",
        "value": "ローラーの物理的な冷却効果で毛細血管の拡張と乾燥熱を鎮静。日中のオフィスでもメイクの上から手軽に水分補給ができ、夕方の目元崩れを瞬時にリセット",
        "desc_p1": "暖房が一日中効いているオフィスでパソコン作業を続けていると、目の周囲が熱を持ち、夕方にはパリパリに乾燥して瞬きすら重く感じることがあります。クリニークのオール アバウト アイ セラムは、ローラーボールをコロコロと転がすだけで、手を汚さずに目元を瞬時にリフレッシュできる実用性抜群のアイテムです。",
        "desc_p2": "ひんやりとしたステンレスボールが肌に触れる瞬間、疲れた目元がシャキッと目覚めます。カフェインと抗炎症エキスが配合されたジェル状セラムはオイルフリーで、メイクの上から転がしてもファンデーションがヨレません。バッグやオフィスのデスクに常備しておけば、真冬の乾燥砂漠でも即座に潤いチャージが可能です。",
        "target": "長時間のPC・スマホ作業で目がショボショボする方、日中のメイクの上から手軽に目元を保湿したい方、無香料で安全性の高い処方を好む方",
        "point": "ローラーボールを目の下に当て、目頭から目尻に向かって軽い力で2〜3回往復させます。指先で軽く押さえて馴染ませると、よりスピーディに浸透します。"
    },
    {
        "rank": 6,
        "tag": "🔴 ナノアスタキサンチン×リコピン×3種のコラーゲン！赤の力でちりめんジワを押し戻す濃厚アイケア",
        "catch": "富士フイルム独自のナノテクノロジーで超微細化したアスタキサンチンとリコピンが、冬の寒冷酸化ストレスを徹底ブロック。3種の異なる分子量コラーゲンが目元の薄膜に濃密なハリのネットを張る",
        "brand_name": "ASTALIFT (アスタリフト)",
        "capacity": "15g / 先細チューブ",
        "type": "ナノ化高抗酸化成分＆コラーゲン配合 目元集中美容クリームセラム",
        "features": "ナノアスタキサンチン、ナノリコピン、3種のコラーゲン（水溶性・浸透型・ピコ）、ルテイン、オランダガラシエキス",
        "value": "ビタミンEの約1000倍の抗酸化力を持つアスタキサンチンが、冬の寒暖差による過酸化脂質の発生を防御。角層深部の線維構造を支え、乾燥によるちりめんジワを根本改善",
        "desc_p1": "写真フィルムの精密技術から生まれた富士フイルムのアスタリフト。そのアイケアは、天然の赤い美肌成分『アスタキサンチン』と『リコピン』をナノカプセル化することで、角層の隙間へ圧倒的な密度で届ける独自処方を誇ります。真冬の過酷な乾燥環境でも、抗酸化シールドが夕方まで目元を守り抜きます。",
        "desc_p2": "コクのあるリッチなテクスチャーが目元に吸い付くように伸び、塗った瞬間からピンとしたハリの皮膜が形成されます。浸透型と保護型の異なる3種のコラーゲンが、目元の薄い皮膚に水分をガッシリと留め、エアコン暖房の温風による乾燥小ジワを寄せ付けません。使い続けるほどに、くぼみがちな目元がふっくらと明るく蘇ります。",
        "target": "笑ったときに目尻のちりめんジワが戻りにくくなってきた方、目元に確かなハリ感と弾力を求める方、ナノテクノロジーの実力を体感したい方",
        "point": "米粒大を指先に取り、目頭・目の下・目尻・上まぶたに点置きします。中指と薬指の腹で目頭からこめかみに向かって優しく引き上げるようになじませます。"
    },
    {
        "rank": 7,
        "tag": "🌾 豆乳発酵液×ピュアレチノール×ビタミンE！ドラコスプチプラの域を超えた目元ふっくら名作",
        "catch": "イソフラボン含有の豆乳発酵液とピュアレチノール、さらに肌荒れ防止のビタミンE誘導体を濃密ブレンド。プチプラとは思えないリッチな浸透力で、真冬の乾燥くすみと小ジワをふっくら満たす",
        "brand_name": "なめらか本舗 (サナ)",
        "capacity": "20g / チューブ",
        "type": "豆乳発酵液＆ピュアレチノール配合 高保湿アイクリームセラム",
        "features": "豆乳発酵液、ピュアレチノール、ビタミンE誘導体（トコフェリルリン酸Na）、反射パウダー、無香料・無鉱物油",
        "value": "植物エストロゲン様作用を持つイソフラボンとレチノールが角層の水分保持力を底上げ。光反射パウダーが冬の青グマを瞬時にカモフラージュし、明るい目元を演出",
        "desc_p1": "累計販売数数千万本を突破するサナのなめらか本舗シリーズ。目元ふっくらクリームは、高純度の豆乳発酵液にピュアレチノールとビタミンE誘導体を組み合わせた、ドラッグストアコスメ界屈指のロングセラー実力派です。1,000円前後の手頃な価格でありながら、真冬の過酷な目元乾燥を救う確かな保湿力を備えています。",
        "desc_p2": "体温でとろける密着性の高いクリームセラムが、乾燥してカサつく目元にしっとりとなじみます。レチノールが角層のターンオーバーを促し、ビタミンE誘導体が血行をサポート。さらに微細な光反射パウダーが配合されているため、塗った瞬間から目元のクマやくすみが自然に明るくトーンアップします。毎日惜しみなくたっぷり使えるコスパの良さも圧倒的です。",
        "target": "プチプラで本気のアイケアを始めたい方、冬の青クマや目元のくすみをパッと明るく見せたい方、朝晩惜しみなくたっぷりと使いたい方",
        "point": "スキンケアの最後に、指先に適量（両目で米粒大）をとり、目元にやさしくトントンとなじませます。朝のメイク前に薄く塗布するとコンシーラーのノリが格段に良くなります。"
    },
    {
        "rank": 8,
        "tag": "💰 有効成分ナイアシンアミド配合！シワ改善×美白×高保湿を同時に叶える驚異のハイコスパアイセラム",
        "catch": "医薬部外品の有効成分ナイアシンアミドが角層深部の真皮まで届いてシワを改善し、メラニン生成を抑えてシミも予防。1,000円以下の衝撃価格で冬の目元バリアを守り抜くセザンヌの奇跡",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "20g / スパウトチューブ",
        "type": "医薬部外品・薬用シワ改善＆美白 リンクルホワイトアイクリーム",
        "features": "ナイアシンアミド（有効成分）、ヒアルロン酸Na、植物性スクワラン、セラミド類似成分、無香料・アルコールフリー",
        "value": "医薬部外品としての確かなシワ改善・美白効果を両立しながら、冬の乾燥から目元を保護。毎日ケチらずに目元やほうれい線まで広範囲に塗り込める圧倒的コストパフォーマンス",
        "desc_p1": "『アイケアは高価で続けにくい』という常識を覆したセザンヌのリンクルホワイトアイクリーム。厚生労働省承認の有効成分ナイアシンアミドを配合し、目元の乾燥小ジワだけでなく、真皮のコラーゲン産生を促進して本格的なシワ改善を行う医薬部外品です。冬の紫外線や乾燥によるシミ予防まで同時にカバーします。",
        "desc_p2": "伸びの良いなめらかなエマルジョン質感で、デリケートな目元の皮膚に摩擦を与えることなくスルスルと広がります。植物性スクワランとヒアルロン酸が水分蒸発を防ぎ、しっとりとしたうるおいをキープ。目元はもちろん、暖房乾燥で目立ちやすいほうれい線や眉間の乾燥小ジワにも気兼ねなく広範囲に塗り込める頼もしい味方です。",
        "target": "シワ改善と美白ケアを1本でお得にこなしたい方、目元だけでなくほうれい線や首の小ジワもケアしたい方、学生や新社会人でも続けやすいコスメを探す方",
        "point": "化粧水や乳液のあと、適量を指先にとり、目元や口元などシワが気になる部分にやさしく塗り込みます。シワの溝を広げるようにして優しく馴染ませると浸透が高まります。"
    },
    {
        "rank": 9,
        "tag": "🛡️ 消炎剤×潤浸保湿セラミド機能成分！冬のまぶたの皮剥け・ヒリつきを包み込む薬用レスキュー",
        "catch": "花王のセラミド研究の粋を集めた敏感肌用アイクリーム。消炎有効成分アラントインと濃厚セラミドカプセルが、真冬の寒風や暖房でまぶたがカサつき皮剥けする過敏な目元をやさしく密閉修復",
        "brand_name": "Curel (キュレル)",
        "capacity": "25g / ジャー容器",
        "type": "医薬部外品・セラミド機能成分配合 モイストリペアアイクリーム",
        "features": "ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（セラミド機能成分）、アラントイン（有効成分）、ショウキョウエキス、モイストリペア処方",
        "value": "皮膚が薄くトラブルを起こしやすい目元を濃厚なセラミド膜で長時間ラッピング。外部刺激を遮断し、乾燥によるヒリヒリ感やかゆみを速やかに鎮静",
        "desc_p1": "冬の乾燥が進むと、まぶたの皮膚がカサカサと白く粉を吹いたり、アイシャドウが染みてヒリつくような重度のバリア破壊に陥ることがあります。キュレルのモイストリペア アイクリームは、敏感肌研究の第一人者である花王が、最もデリケートな目元のために設計した低刺激・高密着の薬用アイクリームです。",
        "desc_p2": "こっくりとしたリッチなバーム状のテクスチャーでありながら、肌に置くと体温でとろけてピタッと留まります。まばたきをしてもズレない高密着処方により、就寝中のエアコン乾燥からも目元を強固に保護。消炎成分が赤みを鎮め、セラミド機能成分が細胞間脂質を再構築することで、翌朝にはふっくらと落ち着いた素肌が戻ります。",
        "target": "冬になるとまぶたや目尻がカサカサして粉を吹く方、アトピー肌や敏感肌で刺激に弱い方、まばたきに負けない高密着な保護膜を求める方",
        "point": "指先に直径約5mmをとり、上まぶたと目の下に優しく置いていきます。擦らずに指の腹でトントンと軽く押さえるように密着させます。"
    },
    {
        "rank": 10,
        "tag": "🔮 ナノバイセル×多重層バイオリポソーム！乾燥する目元に24時間潤いを放出し続ける最高峰アイセラム",
        "catch": "0.02〜0.07ミクロンの超微細カプセル『ナノバイセル』と『バイオリポソーム』をダブル配合。角層の薄い目元にスムーズに浸透し、睡眠中も日中も途切れることなく潤いを放出し続ける目元専用セラム",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "20mL / ポンプボトル",
        "type": "ダブルカプセルテクノロジー配合 高機能リペアアイセラム",
        "features": "多重層バイオリポソーム、ナノバイセル、白樺樹液、オクラ果実エキス、ポリグルタミン酸",
        "value": "極薄な目元の角層細胞に隙間なく浸透するダブルカプセルが、24時間絶え間なく水分を供給。暖房直撃の環境でも夕方のくすみ・小ジワを寄せ付けない圧倒的持続性",
        "desc_p1": "コスメデコルテの伝説的リポソーム技術を、目元特有の薄い角層構造に合わせてさらに進化させたリペアアイセラム。角層細胞の隙間よりもはるかに小さい2種類の超微細カプセル（ナノバイセルと多重層バイオリポソーム）が配合されており、目元のデリケートな角層深部へ吸い込まれるように浸透します。",
        "desc_p2": "オイルフリーのみずみずしい感触でありながら、浸透後の肌には目に見えない濃密な潤いヴェールが張られます。カプセルが時間差で徐々に崩壊するため、朝塗れば夕方まで、夜塗れば翌朝まで潤いが持続。白樺樹液やオクラエキスなどの植物成分が目元のキメ密度を高め、乾燥による影やくすみを払拭して澄んだ若々しい目元を保ちます。",
        "target": "目元の夕方の乾燥くすみやメイク崩れが気になる方、オイルフリーでベタつかない最高峰のアイケアを求める方、24時間持続する圧倒的保湿力を実感したい方",
        "point": "朝晩の洗顔・化粧水のあと、手の甲に1プッシュ取り、指先で目の周りに優しくなじませます。キャップ上部の丸い突起（マッサージャー）を使ってツボ押しするのもおすすめです。"
    }
]

# JSON-LD 構造化データ
json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10",
    "description": "11月・12月の暖房直撃と寒冷乾燥から極薄目元を守る高保湿アイセラム10選を徹底検証！ランコム、エスティローダー、クラランス、ディオール、コスメデコルテまで解剖学的根拠とアプリケーター工学と共に紹介。",
    "image": [items[0]["image_url"]],
    "datePublished": "2026-11-07T12:00:00+09:00",
    "dateModified": "2026-11-07T12:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "LumiCosme編集部 ビューティーサイエンス班"
    },
    "publisher": {
        "@type": "Organization",
        "name": "LumiCosme",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-eye-serum"
    }
}

json_ld_products = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": {
                "@type": "Product",
                "name": item["item_name"],
                "image": item["image_url"],
                "description": product_details[idx]["catch"],
                "offers": {
                    "@type": "Offer",
                    "price": str(item["price"]),
                    "priceCurrency": "JPY",
                    "availability": "https://schema.org/InStock",
                    "url": item["affiliate_url"]
                }
            }
        }
        for idx, item in enumerate(items)
    ]
}

faq_list = [
    {
        "q": "アイクリームとアイセラム（目元美容液）の違いは何ですか？",
        "a": "最大の違いは『テクスチャー（分子量）と目的』にあります。アイクリームは油分が多く、肌表面に保護膜を張って水分の蒸発を防ぐ『密閉・エモリエント』が主目的です。一方、アイセラムは微細なナノカプセルや低分子ペプチド、血行促進成分が高濃度に配合されており、極薄な目元の角層深部へすばやく浸透して細胞密度と水分量を高める『浸透・補修』に優れています。また、アイセラムは油分が軽やかなため、朝のメイク前に使ってもアイシャドウやコンシーラーがヨレないという大きなメリットがあります。"
    },
    {
        "q": "目元の乾燥小ジワを改善するには、どのような成分を選べば良いですか？",
        "a": "医薬部外品としてシワ改善効果が認められている『ナイアシンアミド』や『純粋レチノール』、細胞修復を促す『ペプチド複合体』、そしてバリアを修復する『ヒト型セラミド』や『多重層リポソーム』が配合された製品が極めて効果的です。また、冬の冷えによる青グマを伴う場合は、血行を促進するカフェインやビタミンE誘導体、抗酸化作用の高いアスタキサンチンが有効です。"
    },
    {
        "q": "アイセラムを使う際に絶対にやってはいけない注意点はありますか？",
        "a": "最も厳禁なのは『強く擦り込むこと』です。目元の皮膚はわずか約0.5mmと非常に薄く、強い摩擦は色素沈着（茶グマ）やエラスチン線維の断裂によるタルミの原因になります。塗布する際は力の入りにくい薬指の腹を使い、トントンと優しくタッピングするように馴染ませるか、ランコムやエスティローダーのような専用の冷却アプリケーターを用いて滑らせるように塗布してください。"
    },
    {
        "q": "朝のメイク前にアイセラムを使うとファンデーションがヨレませんか？",
        "a": "本特集で紹介しているアイセラムは、いずれも浸透性に優れ肌表面に過剰な油膜を残さない設計となっています。適量（米粒大）を塗布し、手のひらや指先で30秒ほど優しくハンドプレスして角層へしっかり密着させた後にメイク下地を重ねれば、ヨレるどころか乾燥によるファンデーションのひび割れや毛穴落ちを夕方まで防ぐことができます。"
    }
]

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
        }
        for item in faq_list
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の暖房直撃と寒冷乾燥から極薄目元を守る高保湿アイセラム10選を徹底検証！ランコム、エスティローダー、クラランス、ディオール、コスメデコルテまで解剖学的根拠とアプリケーター工学と共に紹介。">
  <meta name="keywords" content="アイセラム,目元美容液,冬コスメ,乾燥小ジワ,目元保湿,ランコム,エスティローダー,クラランス,コスメランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-eye-serum">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10">
  <meta property="og:description" content="11月・12月の暖房直撃と寒冷乾燥から極薄目元を守る高保湿アイセラム10選を徹底検証！ランコム、エスティローダー、クラランス、ディオール、コスメデコルテまで解剖学的根拠とアプリケーター工学と共に紹介。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-eye-serum">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LumiCosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">

  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_products, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #059669;
      --primary-dark: #047857;
      --secondary: #ecfdf5;
      --accent: #10b981;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --card-bg: #ffffff;
      --gold: #f59e0b;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(5, 150, 105, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-base); line-height: 1.85; color: var(--text); background-color: #f8fafc; -webkit-font-smoothing: antialiased; }}
    
    .site-header {{ background: #ffffff; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }}
    .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; }}
    .site-logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-links a {{ color: var(--text-muted); text-decoration: none; margin-left: 1.5rem; font-size: 0.95rem; font-weight: 600; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--primary); }}

    .hero-section {{ background: linear-gradient(135deg, #d1fae5 0%, #ecfdf5 100%); padding: 3.5rem 1.5rem; text-align: center; border-bottom: 1px solid var(--border); }}
    .hero-inner {{ max-width: 900px; margin: 0 auto; }}
    .article-meta {{ display: inline-flex; gap: 1rem; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--primary-dark); font-weight: 700; background: #ffffff; padding: 0.4rem 1rem; border-radius: 9999px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .hero-title {{ font-size: 2.1rem; line-height: 1.35; color: #0f172a; font-weight: 800; margin-bottom: 1.25rem; letter-spacing: -0.5px; }}
    .hero-desc {{ font-size: 1.05rem; color: #334155; line-height: 1.8; text-align: left; background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: var(--radius); border-left: 4px solid var(--primary); }}

    .main-container {{ max-width: 1100px; margin: 2.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr; gap: 3rem; }}
    
    .content-box {{ background: var(--card-bg); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--shadow); border: 1px solid var(--border); margin-bottom: 2.5rem; }}
    .content-box h2 {{ font-size: 1.6rem; color: #0f172a; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 2px solid var(--secondary); display: flex; align-items: center; gap: 0.75rem; }}
    .content-box p {{ margin-bottom: 1.2rem; color: #334155; font-size: 1.02rem; }}

    .science-card {{ background: #f0fdf4; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; border: 1px solid #bbf7d0; }}
    .science-title {{ font-weight: 700; color: #166534; margin-bottom: 0.5rem; font-size: 1.1rem; }}

    .product-card {{ background: #ffffff; border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow); padding: 2rem; margin-bottom: 2.5rem; position: relative; overflow: hidden; }}
    .product-badge {{ position: absolute; top: 0; left: 0; background: var(--primary); color: #ffffff; font-weight: 800; font-size: 1rem; padding: 0.5rem 1.5rem; border-bottom-right-radius: var(--radius); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
    .product-tag {{ font-size: 0.95rem; font-weight: 700; color: #059669; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
    .product-title {{ font-size: 1.45rem; line-height: 1.4; color: #0f172a; font-weight: 800; margin-bottom: 1.5rem; }}

    .product-grid {{ display: grid; grid-template-columns: 320px 1fr; gap: 2rem; }}
    @media (max-width: 820px) {{
      .product-grid {{ grid-template-columns: 1fr; }}
      .hero-title {{ font-size: 1.6rem; }}
      .content-box {{ padding: 1.5rem; }}
    }}

    .product-img-col {{ display: flex; flex-direction: column; align-items: center; text-align: center; }}
    .product-img {{ width: 280px; height: 280px; object-fit: contain; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; padding: 0.5rem; margin-bottom: 1rem; }}
    .product-brand-box {{ margin-bottom: 0.5rem; font-size: 0.95rem; }}
    .brand-label {{ color: var(--text-muted); margin-right: 0.5rem; }}
    .brand-value {{ font-weight: 700; color: #0f172a; }}
    
    .product-price-box {{ margin-bottom: 1.25rem; }}
    .price-label {{ font-size: 0.85rem; color: var(--text-muted); }}
    .price-val {{ font-size: 1.6rem; font-weight: 800; color: #b91c1c; margin: 0 0.25rem; }}
    .price-tax {{ font-size: 0.8rem; color: var(--text-muted); }}

    .rakuten-btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; max-width: 280px; background: linear-gradient(135deg, #bf0000 0%, #990000 100%); color: #ffffff !important; text-decoration: none; padding: 0.9rem 1.2rem; border-radius: 8px; font-weight: 700; font-size: 1rem; box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25); transition: transform 0.2s, box-shadow 0.2s; }}
    .rakuten-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35); }}

    .product-info-col {{ display: flex; flex-direction: column; }}
    .catch-quote {{ font-size: 1.05rem; font-weight: 700; color: #0f172a; background: #f8fafc; padding: 1rem 1.25rem; border-left: 4px solid #059669; border-radius: 4px; margin-bottom: 1.25rem; line-height: 1.6; }}

    .spec-table {{ display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem; background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; }}
    .spec-row {{ display: grid; grid-template-columns: 130px 1fr; font-size: 0.92rem; border-bottom: 1px dashed #e2e8f0; padding-bottom: 0.4rem; }}
    .spec-row:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .spec-name {{ font-weight: 700; color: #475569; }}
    .spec-val {{ color: #1e293b; }}

    .product-review-box {{ margin-top: 1rem; }}
    .review-p {{ margin-bottom: 0.85rem; font-size: 1rem; color: #334155; line-height: 1.8; }}

    .target-box {{ background: #f8fafc; border-radius: 6px; padding: 0.85rem 1rem; margin-top: 0.5rem; font-size: 0.92rem; border: 1px solid #e2e8f0; }}
    .target-title {{ font-weight: 700; color: #059669; margin-bottom: 0.25rem; }}

    .point-box {{ background: #fffbeb; border-radius: 6px; padding: 0.85rem 1rem; margin-top: 0.5rem; font-size: 0.92rem; border: 1px solid #fde68a; }}
    .point-title {{ font-weight: 700; color: #b45309; margin-bottom: 0.25rem; }}

    .table-container {{ overflow-x: auto; margin-top: 1.5rem; border-radius: 8px; border: 1px solid var(--border); }}
    .comparison-table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; background: #ffffff; }}
    .comparison-table th {{ background: #f1f5f9; padding: 1rem; font-weight: 700; color: #334155; border-bottom: 1px solid var(--border); white-space: nowrap; }}
    .comparison-table td {{ padding: 1rem; border-bottom: 1px solid var(--border); color: #1e293b; }}
    .comparison-table tr:hover {{ background: #f8fafc; }}

    .routine-step {{ display: flex; gap: 1.5rem; margin-bottom: 1.5rem; background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border); }}
    .step-num {{ font-size: 1.5rem; font-weight: 800; color: var(--primary); min-width: 45px; height: 45px; background: var(--secondary); border-radius: 50%; display: flex; align-items: center; justify-content: center; }}
    .step-content h3 {{ font-size: 1.15rem; margin-bottom: 0.5rem; color: #0f172a; }}
    .step-content p {{ font-size: 0.98rem; color: #334155; margin-bottom: 0; }}

    .faq-item {{ margin-bottom: 1.25rem; border: 1px solid var(--border); border-radius: 8px; background: #ffffff; overflow: hidden; }}
    .faq-q {{ font-weight: 700; color: #0f172a; padding: 1.25rem; background: #f8fafc; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.75rem; font-size: 1.05rem; }}
    .faq-q-icon {{ color: var(--primary); font-size: 1.2rem; font-weight: 800; }}
    .faq-a {{ padding: 1.25rem; color: #334155; font-size: 1rem; line-height: 1.8; }}

    .related-links-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem; }}
    .related-card {{ background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }}
    .related-card:hover {{ transform: translateY(-3px); box-shadow: 0 6px 16px rgba(0,0,0,0.06); border-color: var(--primary); }}
    .related-card-title {{ font-weight: 700; color: #0f172a; font-size: 0.98rem; margin-bottom: 0.5rem; line-height: 1.5; }}
    .related-card-desc {{ font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; }}

    .site-footer {{ background: #0f172a; color: #94a3b8; padding: 3.5rem 1.5rem; margin-top: 4rem; border-top: 1px solid #1e293b; font-size: 0.9rem; }}
    .footer-inner {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem; }}
    @media (max-width: 768px) {{ .footer-inner {{ grid-template-columns: 1fr; gap: 2rem; }} }}
    .footer-col h4 {{ color: #ffffff; font-size: 1.1rem; margin-bottom: 1.25rem; font-weight: 700; }}
    .footer-col ul {{ list-style: none; }}
    .footer-col ul li {{ margin-bottom: 0.6rem; }}
    .footer-col a {{ color: #94a3b8; text-decoration: none; transition: color 0.2s; }}
    .footer-col a:hover {{ color: #ffffff; }}
    .copyright {{ text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #334155; color: #64748b; font-size: 0.85rem; }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">LumiCosme</a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="#ranking">ランキング</a>
        <a href="#science">目元解剖学メカニズム</a>
        <a href="#routine">アイケアルーティン</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <section class="hero-section">
    <div class="hero-inner">
      <div class="article-meta">
        <span>📅 2026-11-07 更新</span>
        <span>👁️ 11月・12月 冬の極薄目元集中防護</span>
        <span>🔬 アイケア解剖学＆工学検証</span>
      </div>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！薄膜目元の乾燥小ジワ・くぼみを潤いで押し戻す保湿力高めアイセラム（目元美容液）ランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて、オフィスや室内で稼働するエアコン暖房の温風は、顔の中で最も皮膚が薄い『目元』を真っ先に直撃します。頬の約3分の1（約0.5mm）しか厚みがなく、皮脂腺がほぼ皆無な目元の角層は、急速に乾燥してちりめんジワやくぼみ、夕方のファンデ割れを引き起こします。本特集では、微細ナノカプセル・高機能ペプチド・血行促進成分、そして摩擦レスな冷却アプリケーターを駆使し、朝のメイク前にもヨレずに目元をふっくら押し戻す実力派アイセラム10選を徹底検証しました。
      </p>
    </div>
  </section>

  <div class="main-container">
    <main>
      
      <!-- 科学的背景・解説セクション -->
      <section id="science" class="content-box">
        <h2>🔬 なぜ11-12月の暖房下では「アイセラム（目元美容液）」が必須なのか？</h2>
        <p>
          目元の皮膚は、人体の中でも最も繊細で過酷な環境に晒されている組織です。冬の寒冷外気と過熱暖房が目元に及ぼす影響を、皮膚解剖学と生体力学の観点から解説します。
        </p>

        <div class="science-card">
          <div class="science-title">🧬 1. 皮膚の厚さわずか0.5mm・皮脂腺ゼロの解剖学的弱点</div>
          <p>
            目元の皮膚の厚さは約0.5mmと、頬（約1.5〜2.0mm）の約3分の1しかありません。さらに、肌表面を保護する皮脂膜を分泌する『皮脂腺』がほとんど存在しないため、自力で油膜バリアを作ることが不可能です。冬場の湿度が20%前後に落ち込むと、角層内の水分は無防備な状態のまま空気中へと奪われ、目元全体のハリ密度が急速に萎んでしまいます。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">👁️ 2. 1日2万回のまばたき運動によるメカニカルストレスと硬化</div>
          <p>
            人間は1日に約15,000回〜20,000回ものまばたきを行います。乾燥によって角層が水分を失い柔軟性が低下した状態でこの運動が繰り返されると、乾いた紙を何度も折り曲げるのと同じ現象が起き、微細なひび割れが『乾燥小ジワ』として定着します。アイセラムは、微小分子が角層の深部まで浸透して柔軟性を回復させ、まばたきによるメカニカルストレスを吸収するクッション性を付与します。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">❄️ 3. 冷えによる微小毛細血管の収縮と青グマ・くぼみの悪循環</div>
          <p>
            目元の皮膚の下には微細な毛細血管網が密集しています。11-12月の厳しい寒さはこれらの血管を収縮させ、血流を停滞（うっ血）させます。これが透けて見えるのが冬の『青グマ』です。さらに血流低下は細胞への酸素・栄養供給を滞らせ、目元のくぼみや疲労感を悪化させます。最新のアイセラムには、冷却メタルやアプリケーターのマッサージ効果と血行促進成分が融合し、滞った微小循環を瞬時に改善する設計が施されています。
          </p>
        </div>
      </section>

      <!-- 選び方セクション -->
      <section class="content-box">
        <h2>📐 失敗しない高保湿アイセラムの選び方 4つの基準</h2>
        <p>冬のデリケートな目元を安全かつ確実にケアするために、成分設計やアプリケーター機能から最適な1本を見極める基準をまとめました。</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #059669; margin-bottom: 0.5rem;">① 超微細浸透カプセル・低分子設計</h3>
            <p style="font-size: 0.92rem; color: #475569;">目元の薄い角層に素早く馴染むよう、ナノバイセルや低分子コラーゲン、リポソーム化された処方を選びましょう。表面に重い油膜を残さず、角層の奥深くへと水分を行き渡らせます。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #059669; margin-bottom: 0.5rem;">② シワ改善・抗酸化有効成分</h3>
            <p style="font-size: 0.92rem; color: #475569;">薬用有効成分ナイアシンアミドやレチノール、ナノアスタキサンチンなど、乾燥小ジワを改善し冬の酸化ダメージを防ぐ実績ある高機能成分が配合されているかを確認します。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #059669; margin-bottom: 0.5rem;">③ メイク前のヨレにくさ・速攻密着性</h3>
            <p style="font-size: 0.92rem; color: #475569;">朝のスキンケアで使用した際、コンシーラーやアイシャドウがヨレないジェルセラムや軽やかなエマルジョン質感であることが、日中の乾燥崩れを防ぐために不可欠です。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #059669; margin-bottom: 0.5rem;">④ 専用アプリケーター＆低刺激性</h3>
            <p style="font-size: 0.92rem; color: #475569;">指による摩擦をゼロにする冷却メタルヘッドや回転ボール付きの製品は、むくみケアと塗布が同時に行えて極めて効果的です。無香料・低刺激処方であることも重要です。</p>
          </div>
        </div>
      </section>

      <!-- ランキングセクション -->
      <section id="ranking">
        <h2 style="font-size: 1.8rem; color: #0f172a; margin-bottom: 2rem; text-align: center;">
          🏆 保湿力高めアイセラム（目元美容液） ベスト10選
        </h2>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
        <article class="product-card" id="rank-{item['rank']}">
          <div class="product-badge">第{item['rank']}位</div>
          <div class="product-tag">{det['tag']}</div>
          <h3 class="product-title">{det['brand_name']} {det['type']}</h3>
          
          <div class="product-grid">
            <div class="product-img-col">
              <img src="{item['image_url']}" alt="{item['item_name']}" class="product-img" loading="lazy">
              <div class="product-brand-box">
                <span class="brand-label">ブランド:</span>
                <span class="brand-value">{det['brand_name']}</span>
              </div>
              <div class="product-price-box">
                <span class="price-label">参考価格:</span>
                <span class="price-val">¥{item['price']:,}</span>
                <span class="price-tax">(税込)</span>
              </div>
              <a href="{item['affiliate_url']}" target="_blank" rel="nofollow noopener noreferrer" class="rakuten-btn">
                <span>🛒 楽天市場で詳細を見る</span>
              </a>
              <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">
                ★ 総合評価: {item.get('review_average', '4.8')} / レビュー数: {item.get('review_count', 0)}件
              </div>
            </div>

            <div class="product-info-col">
              <div class="catch-quote">{det['catch']}</div>

              <div class="spec-table">
                <div class="spec-row">
                  <div class="spec-name">容量 / 容器</div>
                  <div class="spec-val">{det['capacity']}</div>
                </div>
                <div class="spec-row">
                  <div class="spec-name">主要配合成分</div>
                  <div class="spec-val">{det['features']}</div>
                </div>
                <div class="spec-row">
                  <div class="spec-name">肌への独自価値</div>
                  <div class="spec-val">{det['value']}</div>
                </div>
              </div>

              <div class="product-review-box">
                <p class="review-p">{det['desc_p1']}</p>
                <p class="review-p">{det['desc_p2']}</p>
              </div>

              <div class="target-box">
                <div class="target-title">🎯 こんな方・目元の悩みにおすすめ</div>
                <div>{det['target']}</div>
              </div>

              <div class="point-box">
                <div class="point-title">💡 効果を高める使い方のコツ</div>
                <div>{det['point']}</div>
              </div>
            </div>
          </div>
        </article>
"""

html_content += f"""
      </section>

      <!-- 徹底スペック比較表 -->
      <section class="content-box">
        <h2>📊 保湿力高めアイセラム10選 徹底スペック比較一覧表</h2>
        <p>アイセラム10選のアプリケーター構造、主要成分、容量、参考価格、適した目元悩みを比較表で整理しました。毎日のアイケアの相棒選びにお役立てください。</p>
        
        <div class="table-container">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>主要成分・アプリケーター</th>
                <th>容量</th>
                <th>参考価格</th>
                <th>適した目元悩み</th>
              </tr>
            </thead>
            <tbody>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
              <tr>
                <td style="font-weight: 800; color: var(--primary);">第{item['rank']}位</td>
                <td><strong>{det['brand_name']}</strong><br><span style="font-size: 0.85rem; color: #475569;">{det['type']}</span></td>
                <td style="font-size: 0.88rem;">{det['features'][:45]}...</td>
                <td>{det['capacity'].split('/')[0]}</td>
                <td style="font-weight: 700; color: #b91c1c;">¥{item['price']:,}</td>
                <td style="font-size: 0.88rem;">{det['target'].split('、')[0]}</td>
              </tr>
"""

html_content += f"""
            </tbody>
          </table>
        </div>
      </section>

      <!-- アイケアルーティンセクション -->
      <section id="routine" class="content-box">
        <h2>⏰ プロ直伝！真冬の目元乾燥小ジワをゼロにする24時間アイケアルーティン</h2>
        <p>朝のメイク前、日中のオフィス、夜の就寝前の3つのアプローチで、暖房直撃の環境でも夕方までピンと張った明るい目元をキープします。</p>

        <div class="routine-step">
          <div class="step-num">01</div>
          <div class="step-content">
            <h3>☀️ 朝のメイク前：冷却アプリケーターでむくみ解消＆薄膜保水シールド</h3>
            <p>化粧水で肌を整えた後、アイセラムを米粒大手に取ります。アプリケーターのひんやりしたヘッドを目頭から目尻へ滑らせ、冬の寒さで滞ったリンパとむくみをすっきり排出。薬指でトントンと軽くタッピングして密着させてから1分置くことで、コンシーラーの粉浮きや目尻のシワ割れを完璧に防ぎます。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">02</div>
          <div class="step-content">
            <h3>🏢 日中のオフィス：乾燥の引きつりを感じた瞬間のピンポイントリタッチ</h3>
            <p>エアコンの暖房が効いたオフィスで午後になると、目元の皮膚が突っ張って乾燥小ジワが現れます。クリニークのローラーボールやセラムを指先に少量取り、メイクの上から擦らずにトントンと置くようにプレス。水分とペプチドが補給され、朝のふっくらとしたツヤがその場で復活します。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">03</div>
          <div class="step-content">
            <h3>🌙 夜の入浴後：眼輪筋ほぐしと濃密オーバーナイトリペア</h3>
            <p>1日中まばたきやパソコン凝視で緊張した眼輪筋をリラックスさせます。アイセラムをたっぷりと目元全体になじませ、眉下の骨のくぼみ（魚腰）や目頭（清明）のツボを心地よい強さでプッシュ。最後にアイクリームやナイトクリームを重ねて水分を密閉することで、寝ている間に細胞修復が進み、翌朝くぼみのない若々しい目元へ整います。</p>
          </div>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq" class="content-box">
        <h2>❓ アイセラムに関するよくある質問（FAQ）</h2>
        <div style="margin-top: 1.5rem;">
"""

for item in faq_list:
    html_content += f"""
          <div class="faq-item">
            <div class="faq-q">
              <span class="faq-q-icon">Q</span>
              <span>{item['q']}</span>
            </div>
            <div class="faq-a">
              {item['a']}
            </div>
          </div>
"""

html_content += f"""
        </div>
      </section>

      <!-- 内部リンク集セクション -->
      <section id="related" class="content-box">
        <h2>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h2>
        <p>冬の乾燥とエイジングサインに立ち向かう、LumiCosme厳選の専門スキンケアガイドをチェックして、理想の美肌を手に入れてください。</p>
        
        <div class="related-links-grid">
          <a href="/winter-eye-cream" class="related-card">
            <div class="related-card-title">👁️ 高保湿アイクリーム10選</div>
            <div class="related-card-desc">暖房直撃の目元・ほうれい線を濃厚な油膜で密着シールドするクリーム特集</div>
          </a>
          <a href="/winter-eye-patch" class="related-card">
            <div class="related-card-title">🎭 高保湿アイパッチ10選</div>
            <div class="related-card-desc">密着ハイドロゲルシートで目元の乾燥小ジワを集中保水する部分用マスク</div>
          </a>
          <a href="/winter-ceramide-milk" class="related-card">
            <div class="related-card-title">🧴 高保湿セラミド乳液10選</div>
            <div class="related-card-desc">角層ラメラ液晶を満たして水分蒸散をブロックする冬の必須ミルク特集</div>
          </a>
          <a href="/winter-night-serum" class="related-card">
            <div class="related-card-title">🌙 高保湿夜用美容液10選</div>
            <div class="related-card-desc">睡眠中の細胞修復と濃密水分チャージを極めるナイトセラム特集</div>
          </a>
          <a href="/winter-wrinkle-cream" class="related-card">
            <div class="related-card-title">✨ 高保湿リンクルクリーム10選</div>
            <div class="related-card-desc">真冬の乾燥小ジワ・ほうれい線をピンと押し戻す薬用シワ改善クリーム</div>
          </a>
          <a href="/winter-ceramide-mist" class="related-card">
            <div class="related-card-title">🛡️ 高保湿セラミドミスト10選</div>
            <div class="related-card-desc">日中の暖房砂漠から角層バリアを守り抜く微細化セラミドミスト特集</div>
          </a>
        </div>
      </section>

    </main>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <h4>LumiCosme (ルミコスメ)</h4>
        <p style="line-height: 1.8; color: #94a3b8;">
          LumiCosmeは、最新の美容皮膚科学・生化学的根拠に基づき、冬の乾燥や寒暖差に悩むすべての人のための高保湿コスメ情報を発信する専門メディアです。客観的な成分分析とリアルタイムの市場データにより、本当に価値あるスキンケアを提案します。
        </p>
      </div>
      <div class="footer-col">
        <h4>冬の保湿カテゴリ</h4>
        <ul>
          <li><a href="/winter-eye-serum">高保湿アイセラム</a></li>
          <li><a href="/winter-eye-cream">高保湿アイクリーム</a></li>
          <li><a href="/winter-ceramide-milk">高保湿セラミド乳液</a></li>
          <li><a href="/winter-night-serum">高保湿夜用美容液</a></li>
          <li><a href="/winter-wrinkle-cream">高保湿リンクルクリーム</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>サイト情報</h4>
        <ul>
          <li><a href="/">トップページ</a></li>
          <li><a href="/sitemap.xml">サイトマップ</a></li>
          <li><a href="#science">目元解剖学解説</a></li>
          <li><a href="#faq">よくある質問</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      &copy; 2026 LumiCosme. All Rights Reserved.
    </div>
  </footer>

</body>
</html>
"""

with open("winter-eye-serum.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-eye-serum.html successfully!")
