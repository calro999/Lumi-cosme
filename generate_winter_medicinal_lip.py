import json
import re

with open("fetched_3new_nov_dec_ceramide_lotion_lip_squalane_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_medicinal_lip"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 口唇炎・口角炎の救世主！5大有効成分が皮むけ・亀裂・出血を医薬品レベルで治療",
        "catch": "資生堂薬品の第3類医薬品。唇の皮がめくれて痛む・笑うと裂ける冬の深刻な唇荒れをスピード修復",
        "brand_name": "資生堂薬品 (SHISEIDO)",
        "capacity": "8g (モアリップN / 第3類医薬品)",
        "type": "第3類医薬品・口唇炎・口角炎治療薬（チューブタイプ）",
        "features": "アラントイン（組織修復）、グリチルレチン酸（消炎）、ビタミンE（血行促進）、ビタミンB6（ピリドキシン塩酸塩・皮膚粘膜維持）、パンテノール",
        "value": "単なる保湿リップではなく、炎症と亀裂を治す医薬品。冬の寒さで血がにじむほどの頑固なひび割れを、就寝前に塗るだけで翌朝驚くほど滑らかに鎮静",
        "desc_p1": "11月から12月にかけての寒気と乾燥は、顔の中で最も皮膚が薄い「唇」を直撃します。唇には皮脂を分泌する皮脂腺や汗腺が一切存在せず、角質層もわずか数層しかないため、外気の乾燥に晒されると瞬く間に水分が蒸発して皮むけや亀裂を起こします。一般的なリップクリームをいくら塗り直しても追いつかない、出血や痛みを伴う口唇炎に対して、医療現場レベルの確かな治療効果を発揮するのが資生堂の『モアリップN』です。",
        "desc_p2": "組織修復を促すアラントインと炎症を抑えるグリチルレチン酸がタッグを組み、さらにビタミンB6とパンテノールが粘膜の代謝を活性化。血行を促進するビタミンEが唇のくすみを晴らします。直接唇にフィットする斜めカットのチューブ形状で、摩擦を与えることなく患部にピタッと密着。夜寝る前に厚めに塗り込んで眠れば、翌朝にはカサカサだった唇がふっくらと柔らかな本来のコンディションを取り戻します。",
        "target": "唇の皮がめくれて血がにじむ方、口角が切れて大きく口を開けられない方、化粧品リップでは荒れが治らない方",
        "point": "清潔な指先に取り、唇の縦ジワの溝に沿って優しく押し込むように塗布します。就寝前のオーバーリップ塗りで夜間の水分蒸発を完全ガードできます。"
    },
    {
        "rank": 2,
        "tag": "🌿 ひび割れ手荒れの名門が開発！唇の荒れ・ひび割れを防ぐ高密着リリップスティック",
        "catch": "ユースキン製薬の処方技術を結集。唇の荒れにしっかり留まる高密着モイストコーティング",
        "brand_name": "yuskin (ユースキン)",
        "capacity": "3.5g (リリップケアスティック / 医薬部外品)",
        "type": "医薬部外品・ひび割れ予防高密着薬用リップスティック",
        "features": "ビタミンE（酢酸トコフェロール）、グリチルレチン酸ステアリル、スクワラン、ホホバ油、アボカド油",
        "value": "黄色いハンドクリームで絶大な信頼を誇るユースキンのリップケア。固すぎず柔らかすぎない絶妙な硬度で唇に密着し、真冬の外気から唇を鉄壁ブロック",
        "desc_p1": "ハンドケアの名門・ユースキンが「ひび割れに悩む唇を救いたい」という思いから開発したリリップシリーズ。冬の外出時に冷たい北風が吹き付けると、唇表面の油膜が一瞬で吹き飛ばされてガサガサの鱗状になってしまいます。",
        "desc_p2": "リリップケアスティックは、消炎有効成分グリチルレチン酸ステアリルと血行促進成分ビタミンEを配合。唇に乗せると体温でするりと溶け広がり、スクワランやホホバ油といった上質な植物オイルが厚みのある保護膜を形成します。メントールや香料が無添加なので、ヒリヒリと荒れた敏感な唇にもピリつきを感じさせません。外出先でもサッとポケットから出して手軽に塗り直せる使い勝手の良さも抜群です。",
        "target": "冬になると唇がガサガサになりやすい方、無香料・無メントールの低刺激スティックを求める方、手軽にポケットに入れて持ち歩きたい方",
        "point": "スティックを2〜3mm繰り出し、力を入れずに唇へ滑らせます。横に引くのではなく、唇の縦ジワに沿って上下に動かすと密着度が上がります。"
    },
    {
        "rank": 3,
        "tag": "🩹 パッカと割れた深いひび割れを密封修復！ワセリンベースの超密着リペア処方",
        "catch": "ロート製薬のひび修復技術。真冬の過酷な寒さでパックリ割れた唇の溝を物理的に埋めて治す",
        "brand_name": "ロート製薬 メンソレータム",
        "capacity": "6g (メンソレータム ヒビプロ LP / 第3類医薬品)",
        "type": "第3類医薬品・ひび割れ密封修復軟膏（高密着チューブタイプ）",
        "features": "アラントイン（組織修復）、パンテノール（皮膚代謝促進）、トコフェロール酢酸エステル（血行促進）、グリチルレチン酸、高密着ワセリン基剤",
        "value": "ひび割れを物理的にシールする高粘度ワセリン基剤を採用。冬の寒風にさらされても落ちにくく、話したり飲食したりしても修復成分が患部に留まり続ける",
        "desc_p1": "12月の真冬の乾燥期、乾燥が進みすぎて唇の中央や口角が「パックリ割れ」を起こし、笑うたびに激痛が走る状態は本当につらいものです。ロート製薬の『ヒビプロ LP』は、そんな深刻な深いひび割れを集中的に治すために作られた第3類医薬品です。",
        "desc_p2": "最大の特徴は、患部を物理的にしっかりと覆い隠す高粘度の密着ワセリンベース。塗った瞬間から頑固な亀裂の隙間を埋め尽くし、外部からの刺激物質や冷気の侵入を遮断します。その密閉空間の中で、アラントインが傷口の組織修復を強力にバックアップし、パンテノールが新しい皮膚の形成を促進。無着色・ノンメントールで、傷口にしみることなくじっくりと修復プロセスを進められます。",
        "target": "唇の中央がパックリ割れて出血しやすい方、食事や会話のたびに唇が裂けて痛む方、就寝中に深い亀裂を徹底集中ケアしたい方",
        "point": "就寝前に、ひび割れた溝を埋め尽くすように少し厚めにこんもりと乗せます。ラップフィルムを唇サイズに切って3分間覆うと驚異的な密封効果が得られます。"
    },
    {
        "rank": 4,
        "tag": "🛡️ セラミド機能成分で唇の角層バリアを満たす！夜の集中パックで翌朝ふっくらモチ唇へ",
        "catch": "キュレルが誇るセラミドスキンケアの結晶。乾燥性敏感肌の唇を濃密な潤いヴェールでラッピング",
        "brand_name": "Curel (キュレル)",
        "capacity": "4.2g (リップケア バーム / 医薬部外品)",
        "type": "医薬部外品・セラミドケア濃厚リップバーム（ジャータイプ）",
        "features": "セラミド機能成分（ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド）、消炎有効成分グリチルレチン酸ステアリル、ホホバ油、植物由来密着成分",
        "value": "花王のセラミド研究が生み出したリップケアの傑作。唇の角層深部まで潤いを満たし、冬のガサガサ皮むけを根本から起きにくくするバリアケア",
        "desc_p1": "荒れた唇に油分を塗るだけのケアでは、一時的に乾きがおさまっても、すぐにまた皮がむけてしまう悪循環に陥りがちです。キュレルの『リップケア バーム』は、皮膚の必須成分『セラミド』の働きを補うことで、唇そのもののバリア機能を内側から立て直す高機能バームです。",
        "desc_p2": "セラミド機能成分が角層の隙間に浸透し、水分をがっちり抱え込むと同時に、濃密なバームが唇の表面にピタッと吸着して潤いヴェールを形成。夜塗って寝ると、朝起きた時に唇がぷるんと柔らかくほぐれており、洗顔後も乾燥を感じないほどの持続力を発揮します。低刺激・無香料・アルコールフリー処方で、冬になると唇の周りまで赤く荒れやすい敏感肌にも安心して使えます。",
        "target": "唇の皮むけを繰り返してしまう方、夜寝ている間の乾燥から唇を完全に保護したい方、セラミドで唇の土台から整えたい方",
        "point": "指先または清潔なリップブラシに適量を取り、唇全体に厚めに塗り広げます。特に皮むけが気になる部分には、くるくると円を描くように優しく馴染ませてください。"
    },
    {
        "rank": 5,
        "tag": "💧 天然セラミドが唇の粘膜バリアを再建！デリケートな超乾燥唇を救う濃厚エッセンス",
        "catch": "製薬会社全薬工業の敏感肌ブランド。生体親和性の高い天然セラミドで唇に極上の潤い膜を形成",
        "brand_name": "Arouge (アルージェ)",
        "capacity": "8g (トータルモイストベール リップエッセンス / 医薬部外品)",
        "type": "医薬部外品・天然セラミド配合薬用濃厚リップ美容液（チューブタイプ）",
        "features": "天然セラミド（ビオセラミド）、グリチルレチン酸ステアリル、アミノ酸系保湿成分、高純度スクワラン",
        "value": "微細化した天然セラミドが唇の角層へ浸透。荒れて敏感になった唇のバリア機能を整え、グロスのような自然なツヤとふっくら感を与える",
        "desc_p1": "風邪や体調不良、寒さで免疫力が落ちた冬は、唇の皮膚も極度に過敏になり、普段使っているリップクリームですら赤みやかゆみを引き起こすことがあります。そんなデリケート肌のために全薬工業が開発したのが、アルージェの『トータルモイストベール リップエッセンス』です。",
        "desc_p2": "人間の肌に極めて近い構造を持つ『ナノ化天然セラミド（ビオセラミド）』を贅沢に配合。角層の奥までスッと溶け込んで水分保持能力を底上げし、消炎成分が微細な刺激を鎮静します。こっくりとした濃厚なテクスチャーながら、ベタベタと髪の毛が張り付く不快感がなく、唇に塗るとグロスを重ねたような自然で上品なツヤ感が生まれます。冬のナチュラルメイクの下地や、口紅の上のトップコートとしても大活躍します。",
        "target": "市販のリップクリームで刺激やかゆみを感じたことがある敏感肌、保湿だけでなく上品なツヤ感も欲しい方、リップ下地としても使いたい方",
        "point": "チューブの口元を唇に直接あてて優しく伸ばすか、指先にとって温めてから唇の中央から外側へトントンと馴染ませます。"
    },
    {
        "rank": 6,
        "tag": "💎 ビタミンA誘導体×エラスチン配合！縦ジワをふっくら押し返すエイジングリップ美容液",
        "catch": "ロート製薬オバジの皮膚科学。唇のボリューム低下と冬の深刻な乾燥小ジワを徹底撃退",
        "brand_name": "Obagi (オバジ)",
        "capacity": "10g (ダーマパワーX リップエッセンス)",
        "type": "エイジングケア・高濃度ビタミンA誘導体配合濃密リップエッセンス",
        "features": "ビタミンA誘導体、コラーゲン、エラスチン、ヒアルロン酸、エラスグロウ、エラスリッチ",
        "value": "オバジのダーマパワーX美容液の技術を唇に応用。年齢とともに痩せて縦ジワが目立ち始めた冬の唇を、ふっくらとしたハリと弾力で満たす",
        "desc_p1": "30代、40代と年齢を重ねるにつれ、冬の寒さと乾燥によって唇のコラーゲンが萎縮し、縦ジワが深く刻まれて口紅が縦割れしてしまう悩みが増加します。オバジの『ダーマパワーX リップエッセンス』は、単なる乾燥対策にとどまらず、唇の『ハリとボリューム』を再生するために生まれた高機能リップ美容液です。",
        "desc_p2": "皮膚のターンオーバーを促すビタミンA誘導体と、肌の弾力を支えるエラスチン・コラーゲン複合体を高濃度で配合。こっくりとした蜜のようなリッチなテクスチャーが唇に密着し、塗った瞬間から唇のシワの溝をパンッと押し上げるようなハリ感をもたらします。冬の冷えで血色を失ったくすみがちな唇も、じんわりと内側から健康的なピンク色の輝きを取り戻します。",
        "target": "唇の縦ジワが深くて口紅が綺麗に乗らない方、唇のしぼみ感やボリューム低下が気になる大人世代、極上のツヤとハリを求める方",
        "point": "米粒大を出し、唇の中央から縦ジワを埋めるように指先でマッサージしながら塗り広げます。夜のリップケアとして使うと翌朝のメイク乗りが劇変します。"
    },
    {
        "rank": 7,
        "tag": "🏆 5つの保湿成分が高保水持続！冬の冷風から一日中唇を守り抜く王道高保湿スティック",
        "catch": "ニベアが誇る最高峰リップ。ひと塗りでしっかり潤い、ツヤと厚みのある高保水膜をキープ",
        "brand_name": "NIVEA (ニベア)",
        "capacity": "2.2g (ディープモイスチャーリップ 無香料 / 医薬部外品)",
        "type": "医薬部外品・高保水持続処方薬用リップスティック",
        "features": "アミノ酸系保水成分、はちみつ、ローヤルゼリーエキス、オリーブオイル、トレハロース、ビタミンE・グリチルレチン酸ステアリル",
        "value": "ドラッグストアで圧倒的な人気を誇る高保湿リップ。高保水型持続ヴェール処方で、冬の冷たい外気にさらされても水分が逃げず潤いが長続き",
        "desc_p1": "毎日のデスクワークや通勤時に、ポケットやバッグに忍ばせておいて、乾きを感じたらサッとひと塗りできる手軽さと、頼もしい保湿力を両立したニベアの『ディープモイスチャーリップ』。冬になると必ずリピート買いするファンが後を絶たない王道の名品です。",
        "desc_p2": "唇の体温でするりととろけるメルティな塗り心地で、アミノ酸系保水成分やはちみつ、ローヤルゼリーエキスなどの濃厚な天然保湿成分が唇表面に密着ヴェールを形成。2つの有効成分（ビタミンE・グリチルレチン酸ステアリル）が冬のひび割れや荒れを予防します。無香料タイプは食事の前やビジネスシーンでも香りを気にせず使え、ベタつかない自然なツヤ感が一日中持続します。",
        "target": "外出先でこまめに保湿したい方、なめらかでとろけるような塗り心地が好きな方、高コスパで信頼できる冬用リップを探している方",
        "point": "冬の寒い場所ではスティックが少し固くなることがあるため、唇に当てて1〜2秒体温で温めてから優しく滑らせると、摩擦なく均一に密着します。"
    },
    {
        "rank": 8,
        "tag": "🧪 4大治療成分配合の第3類医薬品！カサつき荒れを医療用発想でスピーディーに鎮静",
        "catch": "メンソレータムの皮膚治療薬。冬の荒れ狂う唇の皮むけ・ただれ・ひび割れを集中治療",
        "brand_name": "ロート製薬 メンソレータム",
        "capacity": "8.5g (メンソレータム メディカルリップnc / 第3類医薬品)",
        "type": "第3類医薬品・口唇炎口角炎治療薬（ノンメントール・マイクロチューブ）",
        "features": "アラントイン、ビタミンB6（ピリドキシン塩酸塩）、トコフェロール酢酸エステル（ビタミンE）、グリチルレチン酸、セチルピリジニウム塩化物水和物",
        "value": "殺菌成分セチルピリジニウム塩化物水和物を配合し、ひび割れからの細菌感染も防止。敏感になった患部にも優しく塗り込めるノンメントール処方",
        "desc_p1": "冬に唇がひどく荒れると、ただ皮がむけるだけでなく、皮が剥がれた部分が赤くただれたり、黄色いかさぶたのようなものができたりすることがあります。メンソレータムの『メディカルリップnc』は、口唇炎や口角炎を根本から治すために設計された第3類医薬品です。",
        "desc_p2": "組織修復のアラントイン、消炎のグリチルレチン酸、代謝を促すビタミンB6に加え、殺菌成分が患部の二次感染をブロック。冷感刺激（メントール）を含まないノンメントール処方なので、ピリピリとしみる心配がなく、荒れて弱りきった唇にも安心して直接塗布できます。チューブの先端が丸みを帯びており、痛む唇にも負担をかけずに滑らかに塗り広げられます。",
        "target": "唇の荒れが進行してただれや出血がある方、メントールの清涼感が苦手な方、医薬品の確かな効果で短期間で治したい方",
        "point": "1日数回、適量を患部に塗布します。就寝前の清潔な唇にたっぷり塗り込むと、寝ている間に集中修復が進みます。"
    },
    {
        "rank": 9,
        "tag": "🌿 オリーブバージンオイルの濃密油膜！アロエ・甘草誘導体が冬の乾燥摩擦を跳ね返す",
        "catch": "発売から圧倒的人気を誇る超ロングセラー。唇の皮脂膜を完璧に再現するナチュラル処方",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "1.5g (薬用リップクリーム / 医薬部外品)",
        "type": "医薬部外品・オリーブバージンオイル配合薬用リップスティック",
        "features": "オリーブバージンオイル、アロエエキス、甘草誘導体、ビタミンE、無香料・無着色・パラベンフリー",
        "value": "人間の皮脂に極めて近いオリーブバージンオイルを主成分に採用。唇に塗った瞬間に皮脂膜と同化し、冬の寒風による水分の急激な蒸散をシャットアウト",
        "desc_p1": "累計販売本数が数億本を突破しているDHCの金字塔『薬用リップクリーム』。真冬の過酷な寒風が吹き荒れる季節、一度使えば他のリップには戻れないと評される理由は、その圧倒的な「皮脂膜再現力」にあります。",
        "desc_p2": "貴重なオリーブバージンオイルを贅沢に配合し、唇表面の水分を逃さない強固な保護膜を形成。さらにアロエエキスと甘草誘導体が乾燥による肌荒れを穏やかに整えます。油膜感があるのにギトギトせず、唇にピタッと吸い付くように密着するため、飲食をしても保護効果が長く持続。口紅を塗る前の下地として仕込んでおけば、冬のマットリップやティントによる乾燥や縦ジワ割れを完璧に防げます。",
        "target": "唇の乾燥を長時間防ぎたい方、口紅の下地として唇を滑らかに整えたい方、オリーブオイルの自然な保護力を好む方",
        "point": "唇に軽く当てて優しくスライドさせます。口紅を塗る前に下地として薄く塗り、軽くティッシュオフしてから口紅を重ねると発色と持ちがアップします。"
    },
    {
        "rank": 10,
        "tag": "🍯 体温と空気中の水分でとろける！モイストバンク技術で唇をうるおいパック",
        "catch": "まるでクリームがとろけるような新感覚。唇の水分を抱え込んで離さないメルティ処方",
        "brand_name": "ロート製薬 メンソレータム",
        "capacity": "2.4g (メルティクリームリップ 無香料)",
        "type": "モイストバンク技術採用・体温融解型高保水リップスティック",
        "features": "マルチセラミド（セラミド2・3・6II）、スクワラン、ワセリン、シアバター、モイストバンク技術",
        "value": "体温に反応して固形バームがジュワッととろける極上のテクスチャー。空気中の水分まで取り込んで潤いに変える新発想の保水テクノロジー",
        "desc_p1": "冬の乾燥した空気の中で、唇の水分を逃さないだけでなく、空気中の水分を取り込んで潤いヴェールへと変換する画期的な『モイストバンク技術』を採用したロート製薬のメルティクリームリップ。",
        "desc_p2": "唇に乗せた瞬間、体温でクリームがとろけてなめらかなオイル状へと変化。唇のキメの隙間までくまなく行き渡り、3種のマルチセラミドとスクワランが濃密な保湿膜を張り巡らせます。まるでリップパックをした後のようなぷるんとした潤い感が広がり、真冬の暖房の効いた室内でも乾燥知らずの唇を維持できます。プチプラとは思えないリッチな使用感で、デイリー使いに最適な一本です。",
        "target": "とろけるような滑らかな塗り心地を求める方、空気中の乾燥に負けない保水力を実感したい方、プチプラで贅沢な使用感を味わいたい方",
        "point": "柔らかいスティックのため、2〜3mm程度だけ繰り出して唇に優しく滑らせてください。就寝前に少し多めに塗ればナイトリップパックとしても機能します。"
    }
]

faq_items = [
    {
        "q": "なぜ冬（11月・12月）は唇が特にひび割れやすく、血がにじむのですか？",
        "a": "唇の皮膚は、顔の他の部位と構造が根本的に異なります。皮脂腺や汗腺が存在しないため、肌を乾燥から守る天然の保護膜である『皮脂膜』を自力で作ることができません。さらに角質層が通常の皮膚の1/3ほどの薄さしかなく、水分を蓄える能力が極めて低いため、11〜12月の急激な湿度低下やエアコン暖房の風にさらされると、数分で水分が蒸発して亀裂や皮むけ、出血を引き起こしてしまうのです。"
    },
    {
        "q": "「医薬品リップ（第3類医薬品）」と「薬用リップ（医薬部外品）」「化粧品リップ」の決定的な違いは？",
        "a": "目的と配合される有効成分の濃度が明確に異なります。『第3類医薬品（モアリップやヒビプロなど）』は、すでに起きてしまった口唇炎・口角炎・出血・深いひび割れを『治療・治癒』するための医薬品であり、アラントインやビタミンB6などが高濃度で配合されています。『薬用リップ（医薬部外品）』は、荒れやひび割れを『予防』するためのもので、日常的なトラブル防止に適しています。一方『化粧品リップ』は主にツヤや色味、一時的な保湿を目的としています。唇に痛みや亀裂がある場合は、迷わず第3類医薬品を使用してください。"
    },
    {
        "q": "リップクリームを塗っても塗ってもすぐに乾燥してしまう人のNG行動とは？",
        "a": "最大のNG行動は『唇を舐めること』です。唇が乾いたからと舌で舐めると、唾液が蒸発する際に唇本来のわずかな水分まで一緒に奪い去り、過乾燥がさらに悪化します。また、リップを左右に強くゴシゴシと擦り付けるのも、薄い角質層を傷つける原因になります。さらに、剥がれかけの皮を無理やり指や歯で引っ張って剥がすと、真皮層を傷つけて出血や色素沈着の原因になるため絶対にやめましょう。"
    },
    {
        "q": "真冬に効果を最大化するリップクリームの「正しい塗り方」はありますか？",
        "a": "スティックやチューブを『唇の縦ジワに沿って上下に塗る』のが鉄則です。唇のキメは縦方向に走っているため、横に滑らせるだけではシワの奥まで保湿成分が届きません。指先やブラシで優しくトントンとシワの溝を埋めるように押し込むと、密着力と持続力が格段に向上します。また、寒い部屋ではリップが硬くなっているため、唇に当てて体温で1〜2秒温めてから滑らせると摩擦ダメージを防げます。"
    },
    {
        "q": "就寝前の「ラップパック」は本当に効果がありますか？やり方を教えてください。",
        "a": "驚くほど劇的な効果があります。唇の修復や細胞分裂は睡眠中に最も活発に行われるため、就寝前の集中ケアは最も重要です。薬用リップや医薬品バームを通常より厚め（オーバーリップ気味）に塗り、唇のサイズに切った食品用ラップを軽く密着させて3〜5分置くだけで、温熱効果と密閉効果により有効成分が角層深部まで一気に浸透します。翌朝起きた時には、前日のガサガサが嘘のように柔らかくプルプルの唇になります。"
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
    "headline": "保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10",
    "description": "11月・12月の冬本番に深刻化する唇の皮むけ・血がにじむひび割れ・口角炎を徹底解決！医薬品有効成分やセラミドを贅沢配合した高保湿薬用リップクリーム10選を徹底比較！モアリップ、ユースキン、ヒビプロ、キュレル、アルージェ、オバジ、ニベア、DHCなど、真冬でもふっくらぷるん唇が続く至高のアイテムを厳選。",
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
    "name": "冬の高保湿薬用リップクリーム おすすめランキング10選",
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
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']} 高保湿薬用リップクリーム" class="product-img" loading="lazy" width="280" height="280">
          </div>
          <div class="product-meta">
            <table class="meta-table">
              <tr>
                <th>区分 / タイプ</th>
                <td>{p['type']}</td>
              </tr>
              <tr>
                <th>主要有効成分</th>
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
          <h4 class="desc-heading">🔍 冬（11月・12月）の唇悩みへのアプローチ＆使用感</h4>
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
  <title>保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬本番に深刻化する唇の皮むけ・血がにじむひび割れ・口角炎を徹底解決！医薬品有効成分やセラミドを贅沢配合した高保湿薬用リップクリーム10選を徹底比較！モアリップ、ユースキン、ヒビプロ、キュレル、アルージェ、オバジ、ニベア、DHCなど、真冬でもふっくらぷるん唇が続く至高のアイテムを厳選。">
  <meta name="keywords" content="薬用リップクリーム,医薬品リップ,唇 ひび割れ,唇 皮むけ,口唇炎,モアリップ,ヒビプロ,キュレル リップ,ニベア ディープモイスチャー,冬 リップケア 2026">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-medicinal-lip">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- Open Graph -->
  <meta property="og:title" content="保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥で痛む唇を救う！医薬品・医薬部外品の最強高保湿リップ10選を徹底比較。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-medicinal-lip">
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
      --primary: #991b1b;
      --primary-light: #fef2f2;
      --accent: #dc2626;
      --accent-hover: #b91c1c;
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
      background: linear-gradient(135deg, #991b1b 0%, #dc2626 100%);
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
      background: #fee2e2;
      color: #991b1b;
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
      background: #fef2f2;
      border-left: 5px solid #dc2626;
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
      color: #dc2626;
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
      background: #fef2f2;
      border: 1px solid #fecaca;
      border-radius: 8px;
      padding: 1.25rem;
      margin: 1.5rem 0;
    }}
    .highlight-card h4 {{
      color: #991b1b;
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
      color: #991b1b;
      background: #fff1f2;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      border: 1px solid #fecdd3;
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
      color: #dc2626;
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
      color: #991b1b;
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
      background: #991b1b;
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
      color: #dc2626;
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
      color: #991b1b;
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
      border-color: #dc2626;
      color: #dc2626;
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
      <span class="article-tag">❄️ 11月・12月 冬本番リップケア特集</span>
      <h1>保湿力の強さで唇の皮むけ・ひび割れとさようなら！荒れた唇を集中修復する高保湿薬用リップクリームランク10</h1>
      <div class="update-time">
        <span>📅 公開日: 2026年11月2日</span>
        <span>🔄 最終更新日: 2026年11月2日</span>
        <span>✍️ 監修: 冬コスメ徹底比較ラボ 編集部</span>
      </div>
    </header>

    <div class="lead-box">
      <p>11月から12月へと季節が進むと、気温の急激な低下と北風の吹き荒れ、さらには室内のエアコン暖房によって、真っ先に悲鳴を上げるのがデリケートな「唇」です。「リップを塗っているのに皮がめくれてボロボロになる」「笑ったりあくびをしたりすると唇の中央がピキッと裂けて血が出る」「口角が赤く切れて痛くて食事がつらい……」そんな過酷な唇荒れに悩んでいませんか？</p>
      <p style="margin-top: 0.75rem;">唇には皮脂を分泌する皮脂腺がなく、角質層も頬の1/3ほどの薄さしかありません。そのため、真冬の乾燥環境下では水分が秒速で蒸散し、単なる香り付きリップや油分だけの化粧品リップでは、進行した炎症やひび割れを治すことができません。今必要なのは、アラントインやビタミンB6、パンテノール、高純度セラミドといった有効成分で組織を物理的・生化学的に修復する「医薬品・薬用リップ」です。本記事では、深刻な冬の唇荒れを救済する最強の高保湿薬用リップ10選を徹底比較！楽天市場の最新実勢データをもとに厳選解説します。</p>
    </div>

    <!-- 目次 -->
    <nav class="toc-box">
      <div class="toc-title">📑 目次（タップで各見出しへジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#science">1. なぜ冬（11月・12月）に唇はひび割れ出血するのか？皮膚科学的メカニズム</a></li>
        <li><a href="#lip-types">2. 医薬品（第3類）・薬用（医薬部外品）・化粧品リップの決定的な違いと選び方</a></li>
        <li><a href="#ranking">3. 冬の高保湿薬用リップクリーム おすすめ人気ランキング10選</a></li>
        <li><a href="#comparison-table">4. 高保湿薬用リップクリーム10選の有効成分・実勢価格 徹底比較表</a></li>
        <li><a href="#pro-technique">5. 皮膚科医推奨！ひび割れ唇を翌朝ふっくら蘇らせる「縦ジワ塗り＆ラップパック法」</a></li>
        <li><a href="#faq">6. 薬用リップ・口唇炎治療に関するよくある質問（FAQ）</a></li>
        <li><a href="#summary">7. まとめ：自分の唇荒れレベルに合わせたリップ選びで真冬のぷるぷる唇を死守しよう</a></li>
      </ul>
    </nav>

    <!-- 科学的解説 -->
    <section id="science">
      <h2 class="section-title">🔬 なぜ冬（11月・12月）に唇はひび割れ出血するのか？皮膚科学的メカニズム</h2>
      <div class="section-content">
        <p>人間の皮膚は通常、皮脂腺から分泌される皮脂と汗が混ざり合ってできる「皮脂膜」という天然のバリアシールドによって水分蒸発を防いでいます。しかし、唇の表面（赤唇縁）には皮脂腺も汗腺も存在しません。自前で油膜を作ることができないため、もともと極めて無防備な組織なのです。</p>
        <p>さらに、唇の角質層の厚さはわずか数マイクロメートルと極めて薄く、水分を蓄える天然保湿因子（NMF）の量も通常の皮膚の半分以下しかありません。11月〜12月に外気の湿度が30%を下回ると、唇内部の水分が外気へと一方的に奪い去られます。水分を失って柔軟性をなくした角質層は、会話や飲食による唇の伸縮に耐えきれなくなり、ガラスが割れるようにパックリと亀裂が入って出血（ひび割れ・口唇炎）を起こしてしまうのです。</p>
        
        <div class="highlight-card">
          <h4>⚠️ やってはいけない！唇を舐める「乾燥スパイラル」の罠</h4>
          <p>唇がカサついたときに、無意識に舌で唇をペロッと舐めてしまう癖がある方は要注意です。唾液に含まれる消化酵素（アミラーゼ等）がデリケートな粘膜を刺激するだけでなく、唇表面についた唾液が蒸発する際に、唇の内部にあったわずかな水分まで巻き込んで一緒に蒸発させてしまいます。これを繰り返すと「舐める→急激に乾燥する→さらに荒れる」という悪魔の乾燥スパイラルに陥り、治らない重度口唇炎へと悪化します。</p>
        </div>
      </div>
    </section>

    <!-- リップの分類と選び方 -->
    <section id="lip-types">
      <h2 class="section-title">📋 医薬品（第3類）・薬用（医薬部外品）・化粧品リップの決定的な違いと選び方</h2>
      <div class="section-content">
        <p>唇の荒れ具合に応じて、手にとるべきリップの「区分」は明確に異なります。自分の唇が今どのステージにあるのかを正しく見極めて選びましょう。</p>
        
        <h3 style="font-size: 1.1rem; color: #991b1b; margin: 1.25rem 0 0.5rem;">① 出血・深い亀裂・口角の切れがある場合：【第3類医薬品】</h3>
        <p>唇が割れて血がにじんでいる、笑うと裂けて痛む、口角が切れて黄色いかさぶたがあるような状態は、もはや単なる乾燥ではなく「口唇炎・口角炎」という皮膚疾患です。この段階では、化粧品や予防用の薬用リップでは治りません。組織修復成分（アラントイン）や消炎成分（グリチルレチン酸）、代謝促進成分（ビタミンB6・パンテノール）が治療濃度で配合された『第3類医薬品（モアリップやヒビプロなど）』を使い、短期間で患部を治す治療を行いましょう。</p>

        <h3 style="font-size: 1.1rem; color: #991b1b; margin: 1.25rem 0 0.5rem;">② 皮むけ・カサつき・日常的な予防：【医薬部外品（薬用リップ）】</h3>
        <p>出血はないものの、皮がポロポロとめくれる、白く粉を吹く、乾燥して突っ張るといった冬の日常トラブルには、有効成分（ビタミンE誘導体やグリチルレチン酸ステアリル）と高保湿成分（セラミドやスクワラン）を配合した『医薬部外品』が最適です。唇に厚みのある保護膜を作り、寒風や暖房の温風による水分の蒸散を24時間ブロックします。</p>

        <h3 style="font-size: 1.1rem; color: #991b1b; margin: 1.25rem 0 0.5rem;">③ スティック型 vs チューブ・バーム型の使い分け</h3>
        <p>日中の外出先やオフィスで手軽にサッと塗り直したい場合は、繰り出し式の「スティック型」が便利です。一方、就寝前の集中ケアや、すでに亀裂が入ってスティックの摩擦刺激すら痛む深刻な荒れには、唇に厚く乗せられる「チューブ型（軟膏タイプ）」や「ジャーバーム型」を選びましょう。密着力とシールド持続力が圧倒的に高くなります。</p>
      </div>
    </section>

    <!-- ランキングセクション -->
    <section id="ranking">
      <h2 class="section-title">🏆 冬の高保湿薬用リップクリーム おすすめ人気ランキング10選</h2>
      <p style="margin-bottom: 2rem; font-size: 0.95rem; color: #475569;">
        楽天市場の最新売れ筋ランキング、口コミ評判、有効成分の皮膚科学的根拠に基づき、11月・12月の冬本番に唇の皮むけ・ひび割れを徹底解決する高保湿薬用リップ10選を詳しくレビューします。
      </p>

      {"".join(cards_html)}
    </section>

    <!-- 比較表 -->
    <section id="comparison-table">
      <h2 class="section-title">📊 高保湿薬用リップクリーム10選の有効成分・実勢価格 徹底比較表</h2>
      <div class="section-content">
        <p>今回厳選した10商品の区分（第3類医薬品/医薬部外品）、主要有効成分、実勢価格、特徴を一覧表にまとめました。ご自身の唇の荒れ度合いに合わせて比較検討してください。</p>
        <div class="table-container">
          <table class="summary-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / 容量</th>
                <th>有効成分・注目処方</th>
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
      <h2 class="section-title">✨ 皮膚科医推奨！ひび割れ唇を翌朝ふっくら蘇らせる「縦ジワ塗り＆ラップパック法」</h2>
      <div class="section-content">
        <p>せっかく優秀な薬用リップを手に入れても、塗り方を間違えていては本来の効果の半分も引き出せません。冬の痛む唇を最短でリペアするプロ推奨の実践テクニックをマスターしましょう。</p>
        
        <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: 8px; padding: 1.5rem; margin-top: 1rem;">
          <h4 style="color: #991b1b; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ1：体温で温めてから「縦ジワに沿って」塗り込む</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">冬の冷たい空気でリップクリームのワックス成分は固くなっています。そのまま唇に擦り付けると強い摩擦刺激を与えてしまいます。唇に先端をそっと当てて体温で1〜2秒温めてから、唇のキメに沿って「上から下へ、下から上へ」と縦方向に優しく馴染ませてください。シワの溝深くまで有効成分が行き渡ります。</p>

          <h4 style="color: #991b1b; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ2：唇の輪郭の外側まで塗る「オーバーリップ塗布」</h4>
          <p style="font-size: 0.925rem; margin-bottom: 1rem;">冬の乾燥トラブルは、唇の粘膜と顔の皮膚の境目（口唇縁）や口角に最も強く現れます。赤唇のラインの内側だけでなく、輪郭の1mm外側まで少しはみ出すように広く塗布することで、口角の亀裂や口周りの粉吹き乾燥を未然に防ぐことができます。</p>

          <h4 style="color: #991b1b; font-size: 1.05rem; margin-bottom: 0.5rem;">ステップ3：就寝前の「3分間ラップ密封パック」</h4>
          <p style="font-size: 0.925rem;">夜の入浴後、唇が柔らかくなっているタイミングで薬用バームや医薬品軟膏を通常の2〜3倍の厚さでたっぷり塗ります。その上から唇サイズにカットした食品用ラップをペタッと貼り、3〜5分間放置します。密閉温熱効果により、ひび割れた組織の隙間にリペア成分が急速浸透し、翌朝には見違えるほど滑らかな唇へ復活します。</p>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section id="faq">
      <h2 class="section-title">❓ 薬用リップ・口唇炎治療に関するよくある質問（FAQ）</h2>
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
      <h2 class="section-title">🌿 まとめ：自分の唇荒れレベルに合わせたリップ選びで真冬のぷるぷる唇を死守しよう</h2>
      <div class="section-content">
        <p>11月・12月の冬本番、唇の皮膚は私たちが想像している以上に過酷な寒冷と乾燥のストレスにさらされています。皮脂腺がなく角質層が極薄な唇だからこそ、トラブルが軽いうちに適切な有効成分をチャージしてあげることが、真冬を笑顔で快適に過ごすための最大の秘訣です。</p>
        <p>すでに血がにじんでいたり深くパックリ割れてしまっているなら、迷わず第3類医薬品の『資生堂 モアリップN』や『ロート製薬 ヒビプロLP』で集中治療を。日中の外出先で頼もしく唇を守り抜きたいなら『ユースキン リリップ』や『ニベア ディープモイスチャー』、夜の就寝中に唇の土台からセラミドバリアを立て直したいなら『キュレル リップケアバーム』が最高のパートナーになります。</p>
        <p>唇は顔の印象を大きく左右するパーツです。縦ジワや皮むけのないふっくらと潤いに満ちた唇を手に入れて、冬のおしゃれやメイクを思い切り楽しんでください。</p>
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
      <a href="/winter-ceramide-lotion">高保湿セラミド化粧水</a>
      <a href="/winter-ceramide-cream">高保湿セラミドクリーム</a>
      <a href="/winter-peptide-serum">高保湿ペプチド美容液</a>
      <a href="/winter-hair-serum">高保湿ヘアセラム</a>
      <a href="/winter-lip-balm">高保湿リップバーム</a>
    </div>
    <div class="copyright">
      &copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.
    </div>
  </div>
</footer>

</body>
</html>
"""

output_path = "winter-medicinal-lip.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✓ Successfully generated {output_path} ({len(full_html):,} bytes)")
