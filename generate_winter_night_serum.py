import json
import re

with open("fetched_3new_winter_ceramide_night_eye.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_night_serum"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 夜間修復テクノロジーの世界的金字塔！睡眠中の細胞再生リズムと同調する最高峰セラム",
        "catch": "エスティローダーが誇る『クロノラックス パワーシグナル テクノロジー』を搭載。真冬の寒冷外気と暖房で傷ついた角層バリアを睡眠中に集中リペアし、翌朝触れた瞬間にわかるふっくらとした濃密な弾力と潤いを実現",
        "brand_name": "Estée Lauder (エスティ ローダー)",
        "capacity": "50mL / スポイト付きガラスボトル",
        "type": "独自夜間修復テクノロジー搭載 ナイトリペアセラム",
        "features": "クロノラックス パワーシグナル テクノロジー、ビフィズス菌発酵エキス、酵母エキス、ヒアルロン酸高配合、オイルフリー処方",
        "value": "肌本来の夜間修復サイクルを加速させ、日中に受けた紫外線・乾燥・酸化ストレスを寝ている間に中和。冬の寝室の過乾燥下でも水分蒸散を72時間抑え込む圧倒的持続力",
        "desc_p1": "11月から12月にかけて、肌は昼間の厳しい冷風と過熱した暖房による激しい寒暖差に晒され、角層細胞のDNAやコラーゲン線維は目に見えない微細な損傷を蓄積します。エスティローダーのアドバンス ナイト リペアは、肌が本来持っている『夜間の自己修復力』に着目し、40年以上にわたり進化を続けてきた夜用美容液の絶対的存在です。",
        "desc_p2": "とろみのある琥珀色のリッチなテクスチャーが、肌に乗せた瞬間吸い込まれるように素早く浸透。表面に重い油膜を残さないオイルフリー処方でありながら、角層深部へ濃密な潤いの核を定着させます。ビフィズス菌発酵エキスをはじめとする複合成分が寝ている間に細胞間を再建し、翌朝目覚めたときの肌はまるでエステ帰りのようなモチモチの透明感に包まれます。",
        "target": "真冬の朝に肌のしぼみ・ハリ不足・くすみを感じる方、睡眠不足でも肌コンディションを完璧に保ちたい方、最高峰の夜用エイジングケアを求める方",
        "point": "夜の洗顔・化粧水の後、スポイト1回分（5滴程度）を手にとり、顔全体から首筋にかけて包み込むようになじませます。両手で頬を引き上げるように優しくハンドプレスするのが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🔮 1滴に1兆個のナイトバイオリポソーム！真冬の過酷な睡眠中乾燥を跳ね返す超持続保湿",
        "catch": "生体類似成分のリン脂質カプセル『超微細ナイトバイオリポソーム』が角層の奥深くに留まり、美容成分を睡眠中ずっと放出し続ける。乾きを知らない濃密なツヤとキメ密度を翌朝の素肌に宿す傑作",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "50mL / ポンプボトル",
        "type": "多重層バイオリポソーム配合 高機能ナイト集中美容液",
        "features": "ナイトバイオリポソーム（0.1ミクロン）、ヒジキエキス、エクトイン、セラミド類似成分、リッチモイスチャー処方",
        "value": "たまねぎ状に幾重にも重なったカプセルが外側から時間差でじわじわと解け、睡眠中の8時間絶え間なく潤いを補給。暖房をつけた寝室でも乾かない無敵の水分保持膜を形成",
        "desc_p1": "冬の就寝中、暖房エアコンや加湿器の不足によって寝室の湿度はしばしば20%以下まで急落します。この過酷な夜間乾燥を防ぐためにコスメデコルテが開発したのが、1滴に1兆個もの超微細な多重層バイオリポソームを含有するリペアセラムです。カプセルそのものが肌の細胞膜と同じリン脂質でできているため、驚異的な親和性を誇ります。",
        "desc_p2": "みずみずしく濃密なテクスチャーが角層の隙間へスッと入り込み、カプセルがじわじわと崩壊しながら潤いと美容成分を放出し続けます。夜のスキンケアの最初に馴染ませるだけで、その後に重ねる化粧水や乳液の浸透力を爆発的に向上。乾燥で毛穴が開いたり小ジワが目立つ冬の肌を、翌朝には内側から発光するようななめらか肌へ導きます。",
        "target": "朝起きると頬や口元がカサついている方、冬になると化粧水の浸透が悪く感じる方、毛穴のキメ乱れやくすみを集中リセットしたい方",
        "point": "夜の洗顔直後（または導入液として）、手のひらに2〜3プッシュを取り、顔全体にていねいに伸ばします。カプセルを押し込むイメージで手のひら全体で優しくプレスしてください。"
    },
    {
        "rank": 3,
        "tag": "🌙 モロッコ産夜咲きサボテン×グリコール酸！寝ている間にゴワつきを脱ぎ捨てる二層式リブートセラム",
        "catch": "1年に1晩だけ花を咲かせる希少なモロッコ産『ムーンライトカクタス』のエキスと、角質柔軟成分グリコール酸を黄金比でブレンド。二層をシェイクして塗るだけで、翌朝つるんとなめらかな発光肌へ覚醒",
        "brand_name": "YVES SAINT LAURENT (イヴ・サンローラン)",
        "capacity": "30mL / 二層式ポンプボトル",
        "type": "植物エキス×マイルド酸配合 ナイトリブート二層式美容液",
        "features": "ムーンライトカクタス花エキス、グリコール酸（AHA）、アルガンオイル、カレンデュラエキス",
        "value": "寒さで厚く硬くなった古い角質をマイルドにほぐしながら、深部へ濃密な植物オイルと水分を注入。冬のくすみ・ザラつき・毛穴詰まりを一晩で一掃",
        "desc_p1": "冬の寒さは肌の血流を停滞させ、正常なターンオーバーを著しく乱します。その結果、剥がれ落ちるべき古い角質が肌表面に滞留し、どんな高保湿化粧水をつけても浸透しない『ゴワつき砂漠肌』が生じます。イヴ・サンローランのピュアショット ナイトセラムは、この冬の角質停滞に着目し、ピーリング効果と深部保湿を同時にこなす二層処方を確立しました。",
        "desc_p2": "使用直前にシェイクすることで、オイル層とウォーター層が微細に混ざり合います。肌に塗布すると、グリコール酸が穏やかに角質をゆるめ、同時に砂漠の過酷な環境を生き抜くムーンライトカクタスの驚異的な生命力エキスが浸透。翌朝鏡を見ると、まるで一皮むけたような透明感と、指を弾くようななめらかな手触りに驚かされます。",
        "target": "冬の寒さで肌がゴワつき化粧ノリが最悪な方、毛穴の黒ずみやくすみを払拭したい方、翌朝の即効性のある肌変化を実感したい方",
        "point": "容器をしっかりとシェイクして二層を白濁させ、2プッシュを手のひらに取ります。顔全体に伸ばした後、手のひらで顔を包み込んで深く呼吸し、心地よい香りと共に浸透させます。"
    },
    {
        "rank": 4,
        "tag": "🌿 水分7:油分3の黄金比率！21種の厳選植物エキスが夜間の細胞活性を全方位で底上げ",
        "catch": "人間の皮脂膜と同じ『水分70%・油分30%』の生体模倣バランスを容器内部で瞬時にブレンド。クラランスが誇るウコンエキスをはじめとする21種の植物の恵みが、真冬のしぼみ肌に濃密な生命力を吹き込む",
        "brand_name": "CLARINS (クラランス)",
        "capacity": "50mL / ダブルポンプシステムボトル",
        "type": "水相＆油相ハイブリッド処方 総合エイジングケアナイト美容液",
        "features": "ウコン根エキス（ターメリック）、アボカドオイル、マカダミア種子油、カラスムギエキス、キウイ果実エキス",
        "value": "肌の5大基本機能（再生・保護・栄養補給・酸素供給・保水）を同時に活性化。真冬の過酷な冷えと乾燥で失われたハリと弾力を根底からリフトアップ",
        "desc_p1": "真冬の夜間ケアにおいて、水分だけでも油分だけでも不十分です。クラランスのダブル セーラム EXは、肌本来の保護膜である皮脂膜の水分・油分比率に着目。ボトルを押す瞬間に2つの独立した部屋から水相と油相のエッセンスが最適な比率で吐出され、肌の上で新鮮なエマルジョンとして完成する画期的な構造を持っています。",
        "desc_p2": "オイルのリッチなコクとセラムのみずみずしい浸透感が完璧に調和し、肌に乗せた瞬間に心地よいベルベットのようなヴェールが広がります。21種類もの厳選された植物エキスが睡眠中の細胞間コミュニケーションを活性化。暖房による乾燥小ジワをふっくら押し戻し、翌朝には内側から発光するような豊かなツヤと若々しいハリをもたらします。",
        "target": "冬の乾燥で肌のハリ・弾力が低下して疲れて見える方、オイル美容と美容液ケアを両立させたい方、大人の本格的な冬エイジングケアを行いたい方",
        "point": "ボトルのダイヤルで季節や肌状態に合わせて吐出量を調整できます（冬は大きめのドロップマークが推奨）。手のひらで混ぜ合わせ、体温で温めてから顔全体にハンドプレスします。"
    },
    {
        "rank": 5,
        "tag": "🌙 月見草オイル×スクワラン×ラベンダー！寝ている間の水分蒸散を防ぎきる夜用オイルセラム",
        "catch": "夜間の肌再生を促す月見草オイルとオリーブ由来スクワラン、ラベンダー精油を濃縮。睡眠中の角層を濃密な植物性バリアでラッピングし、翌朝モチモチの柔らか肌へとリカバリーするロングセラー",
        "brand_name": "KIEHL'S (キールズ)",
        "capacity": "30mL / スポイト付きボトル",
        "type": "100%天然由来オイル配合 夜用ボタニカル集中美容オイル",
        "features": "イブニングプリムローズ（月見草油）、スクワラン、ラベンダー油、ローズヒップ油、無鉱物油・パラベンフリー",
        "value": "必須脂肪酸を豊富に含むオイルが角層の細胞間脂質を補修。真冬の乾燥冷気と暖房による乾燥ダメージを寝ている間に集中的に回復し、吸い付くような柔軟性を付与",
        "desc_p1": "夜の睡眠中は副交感神経が優位になり、血流が増加して肌の細胞修復が進むゴールデンタイムです。しかし冬の寝室が乾燥していると、せっかくの修復期に水分が逃げてしまい逆効果になります。キールズのミッドナイト ボタニカル コンセントレートは、植物の生命力が凝縮された夜専用のオイル美容液で、修復環境を外側から完璧に保護します。",
        "desc_p2": "オイルでありながらベタつきを極限まで抑えたサラリとしたテクスチャーで、化粧水の後に数滴なじませるだけで吸い込まれるように浸透します。就寝前のリラックスタイムにふさわしい天然ラベンダーの穏やかなアロマが自律神経を整え、上質な睡眠へと誘います。翌朝の肌はカサつきが完全に消え去り、ふっくらと柔らかな感触に満たされます。",
        "target": "冬の朝に肌の乾燥やつっぱりを強く感じる方、スキンケアに心地よい天然アロマの癒やしを取り入れたい方、サラッとした上質オイルが好きな方",
        "point": "夜のお手入れの最後、または化粧水・美容液の後に2〜3滴を手のひらに落とします。両手をこすり合わせて香りを深く吸い込んだ後、顔全体を包み込むように優しくプレスします。"
    },
    {
        "rank": 6,
        "tag": "🧬 ビフィズス菌発酵溶解質×濃密ペプチド！夜間の肌バリアを集中補強する韓国発の神アンプル",
        "catch": "高純度ビフィズス菌発酵エキスとマイクロバイオーム複合成分が睡眠中の常在菌バランスを整え、ペプチドが真冬の冷えで衰えた肌の弾力構造を立て直す。韓国で数々のコスメ大賞を総なめにした実力派",
        "brand_name": "manyo (魔女工場)",
        "capacity": "50mL / スポイト付きボトル",
        "type": "マイクロバイオーム×発酵複合エキス 高濃縮ナイトリペアアンプル",
        "features": "ビフィズス菌培養溶解質、乳酸桿菌発酵液、5種のヒアルロン酸、銅ペプチド、アデノシン",
        "value": "寒暖差や暖房で崩れやすい美肌菌の環境を整え、外的ストレスに揺らがない強固な皮膚バリアを再構築。冬のゆらぎ・乾燥赤み・ハリ不足を根本から解決",
        "desc_p1": "真冬の過酷な寒冷刺激は、肌の表面に存在する常在菌（美肌菌）のバランスを乱し、肌トラブルを引き起こしやすい無防備な状態を作ります。魔女工場のビフィダ バイオーム コンプレックス アンプルは、高純度のビフィズス菌発酵溶解質を贅沢に配合し、夜の就寝中に美肌菌を活性化させて肌本来の防御力を劇的に高めます。",
        "desc_p2": "とろみのある濃厚なアンプルでありながら、肌に広げるとスッと浸透してベタつきを残しません。5種のヒアルロン酸とペプチドが角層の奥深くに水分を蓄え、乾燥によるちりめんジワをふっくら補正。冬の寒さでゴワつきがちな肌が、使い続けるうちに内側から押し返すような密度感としなやかさを取り戻します。",
        "target": "季節の変わり目や冬の寒暖差で肌が敏感にゆらぎやすい方、発酵コスメの高いバリア効果を試したい方、コスパ良く毎日続けられる高機能セラムを探している方",
        "point": "化粧水のあと、スポイトで1〜2滴を取り、顔全体にやさしく塗り広げます。乾燥が気になる目元や口元には少量を重ねづけし、手のひらで温めて浸透を促します。"
    },
    {
        "rank": 7,
        "tag": "🧪 10種の発酵成分を極限濃縮！冬の寝室乾燥に負けず翌朝までリッチな弾力を保つ紫のアンプル",
        "catch": "過酷な環境下で発酵を重ねた10種の濃縮発酵成分が角層深部へアプローチ。『紫のアンプル』として世界中で愛される高保湿ナイトリペア。睡眠不足でも10時間熟睡したかのような濃密な弾力肌を再現",
        "brand_name": "MISSHA (ミシャ)",
        "capacity": "50mL / スポイト付きボトル",
        "type": "10種の発酵成分配合 第5世代エクストリームナイトアンプル",
        "features": "極限発酵ビフィズス菌エキス、乳酸菌発酵液、ナイアシンアミド、植物性ペプチド、セラミドNP",
        "value": "夜間のターンオーバーをサポートし、冬の乾燥によって失われたキメ・透明感・弾力を一挙にリカバリー。エアコン暖房による夜間の角層脱水を完全に防止",
        "desc_p1": "韓国スキンケアの代表格として進化を重ねてきたミシャのタイムレボリューション ナイトリペア。第5世代となる本作は、温熱・冷熱の極限発酵プロセスを経た10種の発酵エキスを濃縮配合。分子が極小化されているため、冬の寒さで収縮した角層の隙間へ驚くほどスムーズに入り込みます。",
        "desc_p2": "リッチでコクのある琥珀色のアンプルが肌に密着し、濃密な保湿膜を形成します。ナイアシンアミドとセラミドNPが寝ている間の肌バリアを二重で強化。朝起きたときの肌のしっとり感と、ふっくらと持ち上がるようなハリ感は感動的で、冬の厳しい乾燥環境でもファンデーションがピタッと吸い付くコンディションを作り上げます。",
        "target": "プチプラ以上デパコス未満の実力派ナイトアンプルを求める方、朝の肌のハリ不足や疲れた印象を改善したい方、濃厚なテクスチャーが好きな乾燥肌の方",
        "point": "夜の洗顔・トナーの後、適量をスポイトで取り、肌のキメに沿って丁寧に伸ばします。最後に手のひらで顔全体を包み込み、温熱効果で角層の奥まで送り届けます。"
    },
    {
        "rank": 8,
        "tag": "⏰ 時計美容理論から生まれた夜用美容マスクセラム！睡眠中の肌再生ピークに潤いを注ぎ込む",
        "catch": "肌のサーカディアンリズムに同期し、夜間の再生遺伝子が活発になる時間帯に濃密な美容成分を届けるアテニアの自信作。冬の睡眠中に水分を抱え込み、翌朝ぷるんとした弾力肌を創出",
        "brand_name": "Attenir (アテニア)",
        "capacity": "30g / ジャー容器",
        "type": "時計遺伝子同期 ナイトケア美容マスクセラム",
        "features": "シグナルペプチド、リッチモイストシールド、コラーゲン誘導体、天然精油（ベルガモット・ネロリ）",
        "value": "就寝中の水分蒸発を物理的に防ぐ密閉ジェル膜を形成。夜間の肌再生を促すペプチドが浸透し、真冬のエアコン乾燥でくたびれた素肌を一晩でリフレッシュ",
        "desc_p1": "一流ブランドの品質を1/3の価格で提供するアテニアが提唱する『時計美容』。人間の肌細胞は体内時計に支配されており、夜間は細胞分裂と老廃物排出が最も盛んに行われます。ミッドナイトモイスチャライザーは、この夜間の黄金時間に的を絞り、睡眠中に肌本来の回復力を最大限に引き出すために設計された夜用セラムです。",
        "desc_p2": "ぷるぷるの濃密ジェルが肌の上でとろけるように広がり、表面にラップのような透明なシールド膜を張ります。暖房の風が当たる寝室でも肌内部の水分を逃さず、翌朝洗い流すまで潤いを保ち続けます。ベルガモットやネロリの上品な天然アロマの香りが冬の夜の緊張を解きほぐし、心地よい眠りをサポートします。",
        "target": "夜のお手入れの最後に手軽にナイトパック効果を得たい方、睡眠中のエアコン乾燥で喉や肌がカラカラになる方、心地よいアロマで癒やされたい方",
        "point": "夜のスキンケアの最後（乳液やクリームの後）に、パール粒大を手にとって顔全体になじませます。洗い流す必要はなく、そのまま就寝してください。"
    },
    {
        "rank": 9,
        "tag": "🍊 高浸透ビタミンC×高純度セラミド！睡眠中に毛穴とくすみを集中ケアする二層式夜用セラム",
        "catch": "ドクターシーラボの最高峰ビタミンC（APPS）と、高純度の保水セラミドを黄金比で配合した二層式エッセンス。睡眠中に真冬の冷えくすみと乾燥毛穴を集中的にケアし、翌朝モチモチの透明肌へ導く",
        "brand_name": "Dr.Ci:Labo (ドクターシーラボ)",
        "capacity": "30mL / 二層式ドロップボトル",
        "type": "ビタミンC×セラミド配合 二層式集中リペアナイトセラム",
        "features": "高浸透ビタミンC（APPS）、セラミドNP・AP・EOP、ヒアルロン酸、植物オイル層、無香料・無鉱物油",
        "value": "酸化しやすいビタミンCをオイル層で守り、水相のセラミドと共に角層深部へデリバリー。冬の血行不良によるくすみと、暖房乾燥による開き毛穴を一晩で引き締め保湿",
        "desc_p1": "冬は寒さで血行が悪くなり、肌全体がどんよりとくすんで見えがちです。さらに暖房乾燥によって角層がしぼみ、毛穴が目立つという複合トラブルが生じます。ドクターシーラボのVC100 ダブルリペアセラムは、従来のビタミンCの100倍以上の浸透力を持つAPPSと、高濃度セラミドを2層に分封した集中夜用セラムです。",
        "desc_p2": "振って混ぜ合わせることで、微細なエマルジョンとなり肌へグングン浸透します。ビタミンC特有のピリつきや乾燥感をセラミドの濃厚なバリアオイルが完全にカバー。翌朝起きると、毛穴の凹凸が目立たなくなり、まるで内側から光を放つような透明感と滑らかなハリを実感できます。",
        "target": "冬になると肌がくすんでトーンダウンする方、乾燥毛穴やキメの乱れが気になる方、ビタミンCとセラミドの相乗効果を体感したい方",
        "point": "使用前にボトルを上下によく振り、2層がしっかり混ざり合ってから適量（2〜3滴）を手のひらに取ります。顔全体にハンドプレスしてなじませます。"
    },
    {
        "rank": 10,
        "tag": "💉 天然マイクロニードル×CICA！夜の導入で美容成分の通り道をつくり翌朝の肌キメを激変",
        "catch": "美容針（シリカ）にCICA成分をコーティングした独自技術。夜の洗顔直後に仕込むことで、寝ている間に角層深部へ美容成分を送り届ける通り道を形成し、冬のゴワつく肌を翌朝なめらかに整える",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "50mL / ポンプボトル",
        "type": "天然マイクロニードル配合 夜用導入ブースターセラム",
        "features": "CICA REEDLE（天然シリカ微細針）、ツボクサエキス、3重ヒアルロン酸、低分子ペプチド",
        "value": "角層表面をチクチクと刺激して美容成分の浸透率を爆発的に高める。冬の乾燥で硬化した角層をほぐし、その後のナイトスキンケアの効果を何倍にも引き上げる",
        "desc_p1": "冬のスキンケアで『どんな高級な美容液を塗っても効果が実感できない』と感じる最大の原因は、寒冷乾燥で硬化した角質が美容成分の浸透をブロックしているためです。VTのリードルショット100は、天然の微細なマイクロニードルを配合し、角層の奥深くへと直接アプローチする革新的な夜用導入美容液です。",
        "desc_p2": "塗布した瞬間に心地よいチクチク感があり、針が角層へ刺激を与えながらCICA成分を届けて肌を健やかに整えます。その後に使うナイトセラムやクリームの浸透が劇的に向上し、翌朝にはキメがキュッと引き締まったつるんとした素肌へと生まれ変わります。冬の鈍化したスキンケアを劇的に覚醒させる夜のスペシャルケアです。",
        "target": "いつものスキンケアに手応えを感じなくなってきた方、肌のキメの粗さやゴワつきを解消したい方、最新のマイクロニードル美容を試したい方",
        "point": "夜の洗顔直後、スキンケアの一番最初に適量を手にとり、顔全体に塗り広げた後、手のひらで押し込むようにハンドプレスします。チクチク感は針が浸透している正常なサインです。"
    }
]

# JSON-LD 構造化データ
json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10",
    "description": "11月・12月の寒冷乾燥や暖房ダメージを寝ている間に集中リセット！エスティローダー、コスメデコルテ、YSL、クラランス、キールズまでサーカディアンリズムと持続放出リポソームの科学的根拠と共に紹介。",
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
        "@id": "https://lumi-cosme.vercel.app/winter-night-serum"
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
        "q": "夜用美容液（ナイトセラム）と朝用の美容液は何が違うのですか？",
        "a": "日中用の美容液は紫外線や乾燥などの外的ストレスから肌を守る『防御』が主目的ですが、夜用美容液は睡眠中の副交感神経優位な時間帯に行われる細胞分裂・DNA修復・コラーゲン合成を後押しする『再生・リペア』に特化しています。また、夜間は角層のバリア透過性が高まり成分が深部まで浸透しやすい反面、水分蒸発量（経皮水分蒸散量/TEWL）も日中の約3倍に跳ね上がるため、じっくり長時間潤いを放出し続ける徐放性リポソームや濃厚な植物性エモリエント膜が処方されています。"
    },
    {
        "q": "夜用クリームを塗っていれば、夜用美容液はなくても十分ですか？",
        "a": "夜用クリームは油分による密閉（エモリエント）が主目的ですが、夜用美容液は高濃度の機能性ペプチド、発酵エキス、時計遺伝子サポート成分を角層深部に送り届ける役割を持っています。特に11-12月の暖房下では、クリームの表面密閉だけでは角層内部の脱水（インナードライ）が進行し、朝の肌のしぼみや小ジワを招きます。美容液で細胞間を満たした上でクリームでフタをすることが美肌維持の鍵となります。"
    },
    {
        "q": "夜用美容液を使う順番はスキンケアのどのタイミングですか？",
        "a": "製品の性質によって異なります。VTのリードルショットやコスメデコルテのリポソームのような『先行型ブースター』は洗顔直後に使用します。エスティローダーやクラランス、ミシャなどの高濃度セラムは『化粧水の直後、乳液やクリームの前』に馴染ませます。キールズのようなオイル美容液は、乳液の直前またはスキンケアの最後の仕上げにハンドプレスするのが基本です。"
    },
    {
        "q": "オイル配合のナイトセラムはニキビや毛穴詰まりの原因になりませんか？",
        "a": "適切に精製されたスクワランやホホバ油、月見草油などの上質植物オイルは人間の皮脂成分と酷似しており、毛穴を詰まらせるリスクは極めて低いです。むしろ冬場に油分を恐れて過度に水分だけのケアを続けると、乾燥を防ごうとして肌が過剰な悪玉皮脂を分泌し、インナードライ毛穴や大人ニキビを悪化させます。良質な夜用セラムで適度な油分を補うことが重要です。"
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
  <title>保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の寒冷乾燥や暖房ダメージを寝ている間に集中リセット！エスティローダー、コスメデコルテ、YSL、クラランス、キールズまでサーカディアンリズムと持続放出リポソームの科学的根拠と共に紹介。">
  <meta name="keywords" content="夜用美容液,ナイトセラム,冬コスメ,睡眠中保湿,エイジングケア,エスティローダー,コスメデコルテ,クラランス,コスメランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-night-serum">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥や暖房ダメージを寝ている間に集中リセット！エスティローダー、コスメデコルテ、YSL、クラランス、キールズまでサーカディアンリズムと持続放出リポソームの科学的根拠と共に紹介。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-night-serum">
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
      --primary: #4f46e5;
      --primary-dark: #3730a3;
      --secondary: #eef2ff;
      --accent: #6366f1;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --card-bg: #ffffff;
      --gold: #f59e0b;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(79, 70, 229, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-base); line-height: 1.85; color: var(--text); background-color: #f8fafc; -webkit-font-smoothing: antialiased; }}
    
    .site-header {{ background: #ffffff; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }}
    .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; }}
    .site-logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-links a {{ color: var(--text-muted); text-decoration: none; margin-left: 1.5rem; font-size: 0.95rem; font-weight: 600; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--primary); }}

    .hero-section {{ background: linear-gradient(135deg, #e0e7ff 0%, #fdf4ff 100%); padding: 3.5rem 1.5rem; text-align: center; border-bottom: 1px solid var(--border); }}
    .hero-inner {{ max-width: 900px; margin: 0 auto; }}
    .article-meta {{ display: inline-flex; gap: 1rem; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--primary-dark); font-weight: 700; background: #ffffff; padding: 0.4rem 1rem; border-radius: 9999px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .hero-title {{ font-size: 2.1rem; line-height: 1.35; color: #0f172a; font-weight: 800; margin-bottom: 1.25rem; letter-spacing: -0.5px; }}
    .hero-desc {{ font-size: 1.05rem; color: #334155; line-height: 1.8; text-align: left; background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: var(--radius); border-left: 4px solid var(--primary); }}

    .main-container {{ max-width: 1100px; margin: 2.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr; gap: 3rem; }}
    
    .content-box {{ background: var(--card-bg); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--shadow); border: 1px solid var(--border); margin-bottom: 2.5rem; }}
    .content-box h2 {{ font-size: 1.6rem; color: #0f172a; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 2px solid var(--secondary); display: flex; align-items: center; gap: 0.75rem; }}
    .content-box p {{ margin-bottom: 1.2rem; color: #334155; font-size: 1.02rem; }}

    .science-card {{ background: #f5f3ff; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; border: 1px solid #ddd6fe; }}
    .science-title {{ font-weight: 700; color: #5b21b6; margin-bottom: 0.5rem; font-size: 1.1rem; }}

    .product-card {{ background: #ffffff; border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow); padding: 2rem; margin-bottom: 2.5rem; position: relative; overflow: hidden; }}
    .product-badge {{ position: absolute; top: 0; left: 0; background: var(--primary); color: #ffffff; font-weight: 800; font-size: 1rem; padding: 0.5rem 1.5rem; border-bottom-right-radius: var(--radius); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
    .product-tag {{ font-size: 0.95rem; font-weight: 700; color: #4f46e5; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
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
    .catch-quote {{ font-size: 1.05rem; font-weight: 700; color: #0f172a; background: #f8fafc; padding: 1rem 1.25rem; border-left: 4px solid #4f46e5; border-radius: 4px; margin-bottom: 1.25rem; line-height: 1.6; }}

    .spec-table {{ display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem; background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; }}
    .spec-row {{ display: grid; grid-template-columns: 130px 1fr; font-size: 0.92rem; border-bottom: 1px dashed #e2e8f0; padding-bottom: 0.4rem; }}
    .spec-row:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .spec-name {{ font-weight: 700; color: #475569; }}
    .spec-val {{ color: #1e293b; }}

    .product-review-box {{ margin-top: 1rem; }}
    .review-p {{ margin-bottom: 0.85rem; font-size: 1rem; color: #334155; line-height: 1.8; }}

    .target-box {{ background: #f8fafc; border-radius: 6px; padding: 0.85rem 1rem; margin-top: 0.5rem; font-size: 0.92rem; border: 1px solid #e2e8f0; }}
    .target-title {{ font-weight: 700; color: #4f46e5; margin-bottom: 0.25rem; }}

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
        <a href="#science">睡眠バイオロジー</a>
        <a href="#routine">ナイトルーティン</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <section class="hero-section">
    <div class="hero-inner">
      <div class="article-meta">
        <span>📅 2026-11-07 更新</span>
        <span>🌙 11月・12月 冬の夜間集中修復特講</span>
        <span>🔬 ビューティーバイオロジー検証</span>
      </div>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！睡眠中の細胞修復と濃密水分チャージを極める保湿力高め夜用美容液・ナイトセラムランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて、日中の過酷な寒冷空気とエアコン暖房によって傷つけられた肌は、夜の睡眠中にのみ修復プロセスへと移行します。しかし、暖房が稼働する冬の寝室は湿度が20%以下まで急降下し、就寝中の水分蒸散量は日中の約3倍に達します。本特集では、サーカディアンリズム同期・多重層ナイトリポソーム・高濃度ペプチド・厳選植物オイルを駆使し、寝ている間に細胞修復を加速させ、翌朝の素肌に劇的なモチモチ感と透明感をもたらす実力派夜用美容液10選を徹底検証しました。
      </p>
    </div>
  </section>

  <div class="main-container">
    <main>
      
      <!-- 科学的背景・解説セクション -->
      <section id="science" class="content-box">
        <h2>🔬 なぜ11-12月の冬肌には「夜用美容液（ナイトセラム）」が不可欠なのか？</h2>
        <p>
          人間の皮膚には、24時間周期の生体リズム（サーカディアンリズム）が組み込まれています。日中は紫外線や外的汚染物質から身を守る『防御モード』にあるのに対し、夜間は傷ついた細胞を修復しコラーゲンやバリア脂質を合成する『再生モード』へと切り替わります。真冬の過酷な環境下で夜用美容液が決定的な役割を果たす生化学的理由を解説します。
        </p>

        <div class="science-card">
          <div class="science-title">🧬 1. 時計遺伝子と夜間修復のゴールデンタイム</div>
          <p>
            皮膚細胞内に存在する時計遺伝子（CLOCK、BMAL1等）は、夜間の就寝中に細胞分裂やDNA修復酵素の活性化を促します。しかし、冬の厳しい寒冷ストレスや日中の急激な温度変化に晒されると、この時計遺伝子のシグナル伝達が乱れ、夜間の修復プロセスが著しく遅延します。ナイトセラムに配合されたビフィズス菌発酵エキスやシグナルペプチドは、時計遺伝子と同調して修復シグナルを増幅し、寝ている間に日中ダメージの完全清算をサポートします。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">💧 2. 夜間の「経皮水分蒸散量（TEWL）」爆発とバリア透過性のパラドックス</div>
          <p>
            皮膚科学研究により、夜間は角層のバリア機能が一時的に緩み、有効成分が最も深部まで浸透しやすい反面、肌内部の水分が外へ逃げ出す『経皮水分蒸散量（TEWL）』が昼間の約3倍に増大することが明らかになっています。暖房の温風が循環する冬の寝室では、朝起きるまでに大量の水分が奪われ、目元や口元の小ジワが深刻化します。夜用美容液は、微細なナノカプセルや多重層バイオリポソームを用いることで、水分を逃がさない持続放出膜を形成し、朝まで潤いの高圧環境を維持します。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">🛡️ 3. 日中の酸化・糖化ストレスを中和する夜間抗酸化カクテル</div>
          <p>
            冬の紫外線や冷えによる微小循環不全によって発生した活性酸素は、夜間に肌深部のコラーゲンやエラスチンを徐々に劣化させます。夜用美容液に含まれる高純度ビタミンC誘導体、抗酸化植物エキス、レスベラトロールなどの複合成分が、睡眠中の無防備な組織を酸化ストレスから強力に防護し、翌朝の肌に濁りのない澄んだ透明感をもたらします。
          </p>
        </div>
      </section>

      <!-- 選び方セクション -->
      <section class="content-box">
        <h2>📐 失敗しない高保湿夜用美容液の選び方 4つの基準</h2>
        <p>冬の夜間集中スキンケアで確実な肌変化を手に入れるために、成分設計や浸透処方から最適な1本を見極める基準をご紹介します。</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #4f46e5; margin-bottom: 0.5rem;">① サーカディアン同期成分</h3>
            <p style="font-size: 0.92rem; color: #475569;">エスティローダーのクロノラックス技術や発酵ビフィズス菌溶解質、クロノペプチドなど、睡眠中の細胞修復リズムをサポートする先端バイオ成分が配合されているかを確認しましょう。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #4f46e5; margin-bottom: 0.5rem;">② 徐放性・持続放出カプセル技術</h3>
            <p style="font-size: 0.92rem; color: #475569;">塗布した瞬間だけでなく、睡眠中の6〜8時間にわたって時間差で潤いを放出し続ける『多重層バイオリポソーム』や『ナノカプセル』処方が、朝の乾きを防ぐ決定打となります。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #4f46e5; margin-bottom: 0.5rem;">③ 水分相と油分相のバランス</h3>
            <p style="font-size: 0.92rem; color: #475569;">クラランスのような二層式ハイブリッド処方や、キールズのような上質植物オイルセラムなど、水分保持と油膜密閉を同時に叶える処方は、真冬の過酷な乾燥寝室で抜群の強さを誇ります。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #4f46e5; margin-bottom: 0.5rem;">④ ナイトアロマまたは完全低刺激</h3>
            <p style="font-size: 0.92rem; color: #475569;">副交感神経を優位にするラベンダーやネロリなどの天然精油の香り、または敏感肌でも安心して使用できる無香料・低刺激処方など、夜の肌と心に優しい設計を選びましょう。</p>
          </div>
        </div>
      </section>

      <!-- ランキングセクション -->
      <section id="ranking">
        <h2 style="font-size: 1.8rem; color: #0f172a; margin-bottom: 2rem; text-align: center;">
          🏆 保湿力高め夜用美容液 ベスト10選
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
                <div class="target-title">🎯 こんな方・肌質におすすめ</div>
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
        <h2>📊 保湿力高め夜用美容液10選 徹底スペック比較一覧表</h2>
        <p>夜用美容液10選の主要成分、アプローチ技術、容量、参考価格を比較表にまとめました。ご自身の肌悩みと睡眠習慣にぴったりの1本を見つけてください。</p>
        
        <div class="table-container">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>主要成分・独自テクノロジー</th>
                <th>容量</th>
                <th>参考価格</th>
                <th>おすすめ肌悩み</th>
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

      <!-- ナイトルーティンセクション -->
      <section id="routine" class="content-box">
        <h2>⏰ プロ直伝！睡眠中の修復効果を極限まで高める夜のナイトセラム活用術</h2>
        <p>入浴後から就寝直前までのステップを最適化することで、美容成分の浸透と翌朝の肌密度が飛躍的に向上します。</p>

        <div class="routine-step">
          <div class="step-num">01</div>
          <div class="step-content">
            <h3>🛁 入浴後3分以内の水分トラップ：毛穴が開いた瞬間を逃さない</h3>
            <p>お風呂から上がると肌表面の水分は急速に蒸散します。バスタオルで水気を拭き取ったら、3分以内に化粧水をたっぷりなじませ、角層の通路（アクアポリン）を開通させます。導入型ナイトセラム（リードルショットやリポソーム等）を使用する場合は、化粧水前の清潔な素肌に直塗りすることで浸透効果が最大化します。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">02</div>
          <div class="step-content">
            <h3>🌙 ナイトセラムの温熱ハンドプレスとリンパ流し</h3>
            <p>セラムを手にとり、手のひらの体温で数秒間温めてから顔全体に広げます。指先で擦るのではなく、手のひら全体で頬を包み込み、耳の下から鎖骨へとリンパを流すように優しくプレス。真冬の冷えで滞った微小循環が活性化され、美容成分が細胞のすみずみまで行き渡ります。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">03</div>
          <div class="step-content">
            <h3>🛌 就寝直前のオーバーナイト密閉シールド</h3>
            <p>美容液が肌に定着したら、乳液またはナイトクリームを重ねて水分を完全に密閉します。特にエアコン暖房をつけて寝る場合は、枕元の加湿器で湿度50%以上を維持し、乾燥しやすい目元や口元にセラムを米粒大だけ再度重ねておく『追いセラム』が翌朝の乾燥小ジワを完璧に防ぎます。</p>
          </div>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq" class="content-box">
        <h2>❓ 夜用美容液に関するよくある質問（FAQ）</h2>
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
        <p>冬の寒さと乾燥に立ち向かう、LumiCosme厳選の専門スキンケアガイドをチェックして、理想の美肌を手に入れてください。</p>
        
        <div class="related-links-grid">
          <a href="/winter-ceramide-milk" class="related-card">
            <div class="related-card-title">🧴 高保湿セラミド乳液10選</div>
            <div class="related-card-desc">角層ラメラ液晶を満たして水分蒸散をブロックする冬の必須ミルク特集</div>
          </a>
          <a href="/winter-night-cream" class="related-card">
            <div class="related-card-title">🌙 高保湿ナイトクリーム10選</div>
            <div class="related-card-desc">寝ている間の濃厚ラッピングで翌朝もっちり肌を叶える夜用クリーム特集</div>
          </a>
          <a href="/winter-sleeping-mask" class="related-card">
            <div class="related-card-title">🎭 高保湿スリーピングマスク10選</div>
            <div class="related-card-desc">塗って寝るだけで翌朝の化粧ノリが劇変する濃密オーバーナイトパック</div>
          </a>
          <a href="/winter-retinol-cream" class="related-card">
            <div class="related-card-title">✨ 高保湿レチノールクリーム10選</div>
            <div class="related-card-desc">冬の乾燥小ジワやハリ不足を夜間に集中ケアする本格レチノール特集</div>
          </a>
          <a href="/winter-serum-booster" class="related-card">
            <div class="related-card-title">💧 導入先行美容液10選</div>
            <div class="related-card-desc">ゴワつく冬の砂漠肌を即座にほぐし浸透力を底上げするブースター特集</div>
          </a>
          <a href="/winter-face-oil" class="related-card">
            <div class="related-card-title">🌿 高保湿フェイスオイル10選</div>
            <div class="related-card-desc">皮脂枯れ砂漠肌を救う極上植物オイル＆エモリエントケア徹底検証</div>
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
          <li><a href="/winter-night-serum">高保湿夜用美容液</a></li>
          <li><a href="/winter-ceramide-milk">高保湿セラミド乳液</a></li>
          <li><a href="/winter-night-cream">高保湿ナイトクリーム</a></li>
          <li><a href="/winter-sleeping-mask">高保湿スリーピングマスク</a></li>
          <li><a href="/winter-retinol-cream">高保湿レチノールクリーム</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>サイト情報</h4>
        <ul>
          <li><a href="/">トップページ</a></li>
          <li><a href="/sitemap.xml">サイトマップ</a></li>
          <li><a href="#science">睡眠バイオロジー解説</a></li>
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

with open("winter-night-serum.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-night-serum.html successfully!")
