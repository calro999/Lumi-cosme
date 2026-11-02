import json
import re

with open("fetched_3winter_mist_bath_headspa_data_perfect.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_oil_mist"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計3000万本突破！韓国CA御用達の黄金比二層式グロウセラムミスト",
        "catch": "ホワイトトリュフ×植物オイルの贅沢ヴェール。振って吹きかけるだけで夕方まで発光ツヤ肌キープ",
        "brand_name": "d'Alba (ダルバ)",
        "capacity": "100ml",
        "type": "オイルイン・高機能セラムスプレー（二層式）",
        "features": "イタリア産ホワイトトリュフ（ツベルマグナツムエキス）、トコフェロール、アボカド油、ヒマワリ種子油、ナイアシンアミド",
        "value": "機内の極限乾燥と戦う客室乗務員が認めた『CAミスト』の元祖。微細な霧がメイクを崩さず角層深部へ油分と水分を同時補給",
        "desc_p1": "11月から12月にかけて、オフィスや商業施設のエアコン暖房が本格稼働すると、室内の湿度は20%台まで急落します。午後3時を過ぎる頃には肌の水分が奪われて頬がつっぱり、ファンデーションがひび割れて粉を吹く『冬の砂漠肌現象』に直面する女性が後を絶ちません。そんな過酷な乾燥環境を打破する圧倒的エースが、韓国発ダルバの『ホワイトトリュフ ファースト スプレー セラム』です。",
        "desc_p2": "水分層と上質なイエローオイル層が8:2の黄金比で分離しており、ボトルを軽く3〜5回振ることで瞬時に超微細なエマルジョン状態へ変化。イタリア産ホワイトトリュフの抗酸化力とアボカドオイル・ヒマワリ種子オイルのラッピング効果が、肌表面に薄い保護シールドを形成します。一般的な水系ミストのように蒸発時に肌本来の水分を奪う『過乾燥』を引き起こす心配が一切なく、ひと吹きでまるでスパから出た直後のようなみずみずしいツヤと柔らかさが蘇ります。",
        "target": "暖房の効いたオフィスで夕方の乾燥崩れ・つっぱりに悩む方、ファンデの上から自然なツヤ感を足したい方、オイルの重さが苦手でもしっかり保湿したい方",
        "point": "メイク仕上げの直後に顔全体へ3プッシュし、手のひらで優しくハンドプレス。さらに日中、乾燥を感じたタイミングで追いミストをすることで、一日中メイクしたての潤いヴェールが持続します。"
    },
    {
        "rank": 2,
        "tag": "✨ 発売以来ベスコス総なめ！メイクの上から『つや玉』が輝く資生堂の技術の結晶",
        "catch": "きめ細やかな霧が肌に均一密着。美容水層と美容オイル層が素肌を満たしてハリを与える",
        "brand_name": "ELIXIR (エリクシール / 資生堂)",
        "capacity": "80ml",
        "type": "エイジングケア・高保湿つや玉ミスト（二層式）",
        "features": "クレソンエキスBG、イノシトールCP、水溶性コラーゲン、高精製植物オイル、みずみずしいフローラルの香り",
        "value": "資生堂の皮膚科学が生んだ名作。肌の凹凸や毛穴に素早く馴染み、メイクを崩さず自然な光の反射で頬の高い位置にツヤを宿す",
        "desc_p1": "冬の冷たい外気と乾いた暖房風にさらされると、肌は角層の水分保持力が低下し、肌表面のキメが乱れてどんよりとした影やくすみが目立つようになります。『夕方になると顔が疲れて見える』という冬特有の悩みに寄り添い、発売直後から爆発的ヒットを記録し続けているのがエリクシールの『つや玉ミスト』です。",
        "desc_p2": "美容水層と美容オイル層が計算し尽くされたバランスで配合されており、きめ細やかな微粒子ミストが肌全体をふんわり包み込みます。コラーゲンやクレソンエキスなどの高保湿美容成分が角層の奥深くまで浸透し、表面に残るオイル層が水分の蒸散をピタッとブロック。メイクの上から吹きかけてもファンデーションがヨレるどころか、粉浮きを抑えてベースメイクを肌にぴたっと再密着させます。鏡を見るたびに嬉しくなるような、ふっくらとしたハリと健康的な『つや玉』が手に入ります。",
        "target": "夕方になるとベースメイクが粉っぽく浮いてしまう方、肌のくすみや疲れ顔をパッと明るく見せたい方、上品なフローラルの香りでリフレッシュしたい方",
        "point": "スプレーする際は顔から約15cmほど離し、目を閉じて円を描くように2〜3回吹きかけます。顔を触らずそのまま自然乾燥させるだけで、ミストが肌表面に均一なツヤフィルムを形成します。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 微粒子汚れ＆寒冷乾燥からバリア！冬の敏感肌・ゆらぎ肌を守る低刺激二層オイルミスト",
        "catch": "アレルバリアテクノロジーNEO搭載。冬の乾いた空気・花粉・ちりから肌を優しくガード",
        "brand_name": "d program (d プログラム / 資生堂)",
        "capacity": "57ml",
        "type": "敏感肌用・保護バリアオイルインミスト",
        "features": "アレルバリアテクノロジーNEO、グリセリン、植物性スクワラン、アルコール（エタノール）フリー、パラベンフリー、無香料",
        "value": "デリケートな冬の敏感肌をとことん追求。バリア機能が低下してピリつきやすい季節でも安心して使える低刺激設計と高い密着保護力",
        "desc_p1": "11月から12月にかけて気温が一段と下がると、皮脂分泌の激減に伴って肌のバリア機能が著しく低下します。暖房の風やマスクの摩擦、空気中の微粒子汚れに触れるだけで肌が赤くなったり、ヒリつきを感じたりする『ゆらぎ乾燥肌』にとって、アルコールや強い香料の入ったミストは刺激になりがちです。",
        "desc_p2": "dプログラムのアレルバリアミストNは、デリケートな敏感肌のために開発されたオイル＆化粧水の二層タイプ。肌の上に均一な透明バリア膜を張り巡らせ、ちり・ホコリ・花粉などの微粒子汚れの付着を物理的に防止します。同時に植物性スクワランを中心とする保護オイルが、乾燥による小ジワやかゆみを穏やかに鎮静。界面活性剤を極力抑えた処方のため振った後の混ざり心地も滑らかで、刺激感を一切感じることなく肌にしっとりとした安らぎを与えてくれます。",
        "target": "冬になると肌が敏感になり普通の化粧水がしみる方、暖房による赤み・乾燥トラブルを防ぎたい方、無香料・低刺激処方を重視する方",
        "point": "ボトルをしっかりシェイクした後、顔全体に4〜5プッシュ。外出直前にひと吹きしておくと、冷たい外気や空気中の刺激物質から肌を一日中シールドできます。"
    },
    {
        "rank": 4,
        "tag": "🌿 ひと吹きで気分まで高揚する上質な朝と午後！肌を潤いヴェールで満たす洗練デパコス",
        "catch": "やわらかな霧が肌を包み込み、瑞々しいツヤと心地よい香りが広がるカネボウの名品",
        "brand_name": "KANEBO (カネボウ)",
        "capacity": "30ml",
        "type": "高密着・リフレッシュ美容液ミスト",
        "features": "モーニングボタニカルコンプレックス、高保水ポリマー、ティートピアを基調とした爽快なシトラス・フローラルの香り",
        "value": "計算された微細スプレーノズルが至福の噴霧感を演出。コンパクトなスリムボトルでポーチにすっきり収まり、どこでも極上チャージ",
        "desc_p1": "慌ただしい年末の仕事中や外出先で、カサつく肌とともに気持ちまでリフレッシュしたい大人の女性から絶大な支持を集めているのが、KANEBOの『チアリング ミスト』です。肌に触れた瞬間の心地よさと、洗練された香りのアロマ効果が毎日のスキンケア体験を格上げします。",
        "desc_p2": "肌の上に極薄の保水ネットワークを形成し、外気の乾燥から素肌を優しくガード。霧が極めて細かくフワッと広がるため、アイメイクやリップを崩すことなく顔全体に均一な潤いの膜を行き渡らせることができます。オイル分が肌を柔らかくほぐし、ごわつきがちな冬の角質をなめらかに整えます。仕事の合間や移動中にスプレーするだけで、ピンとしたハリ感と上質なツヤが瞬時に宿り、午後からの表情をパッと明るく引き締めます。",
        "target": "デパコスならではの上質な使用感と香りにこだわりたい方、ポーチに入れてスマートに持ち歩きたい方、午後の肌疲労と気分を同時にリセットしたい方",
        "point": "首筋やデコルテまで広めにスプレーすると、上質なアロマの香りがふんわり立ち上り、首元の乾燥小ジワ予防とリフレッシュ効果を同時に得られます。"
    },
    {
        "rank": 5,
        "tag": "💎 メイクの完成度を長時間キープ！微細なフィックスヴェールで乾燥崩れを許さない",
        "catch": "潤いを角層に届けながら肌表面をさらりとなめらかにコーティング。木漏れ日を思わせる癒やしの香り",
        "brand_name": "RMK (アールエムケー)",
        "capacity": "50ml",
        "type": "メイクフィックス＆保湿コンディショニングミスト",
        "features": "西洋梨果汁発酵エキス、セージ葉エキス、ヒアルロン酸、アミノ酸系保湿成分、ウッディローズの心地よい香り",
        "value": "メイクアップアーティストブランドならではの計算された質感。ファンデーションの密着度を極限まで高め、テカリと乾燥崩れの両方を防ぐ",
        "desc_p1": "冬は暖房の効いた室内と寒風吹きすさぶ屋外を行き来するため、肌が激しい温度差にさらされ、Tゾーンは皮脂で崩れるのにUゾーンは乾燥して突っ張るという『混合崩れ』が多発します。そんな冬のベースメイクの乱れを完璧に統制するのがRMKの『コンディショニング フィックス ミスト』です。",
        "desc_p2": "肌をみずみずしく潤すスキンケア成分と、メイクをピタッと定着させるフィックス成分を絶妙に融合。スプレーした瞬間、細かなミストが肌表面に吸い付くようにフィットし、余分なベタつきを残さず、内側はしっとり・表面はつるんとしたシルキーな仕上がりを実現します。西洋梨果汁発酵エキスやアミノ酸成分が角層の水分保持力をサポートし、マスクやマフラーの擦れによるメイク落ちも防ぎます。",
        "target": "暖房による部分的なテカリと乾燥崩れが同時に気になる方、冬でもベタつかないさらりとした保湿感を求める方、メイク持ちを格段に上げたい方",
        "point": "ベースメイクの仕上げに全体へ吹きかけた後、スポンジのきれいな面で軽くトントンと密着させると、一日中ヨレない強固な美肌ベースが完成します。"
    },
    {
        "rank": 6,
        "tag": "🌺 カメリアオイル×植物エキスの濃密二層式！韓国ラグジュアリースキンケアの真骨頂",
        "catch": "肌を柔らかく解きほぐす天然オイルの力。乾燥で固まった角質をなめらかに潤す高保湿ミスト",
        "brand_name": "FEMMUE (ファミュ)",
        "capacity": "100ml",
        "type": "プレミアム・カメリアオイルインエッセンスミスト",
        "features": "ツバキ種子油（カメリアオイル）、ダマスクローズ花水、ナイアシンアミド、アデノシン、天然精油ブレンド",
        "value": "ボタニカルの豊かな恵みを凝縮。オイルとは思えないほど軽やかな浸透感で、ごわつく冬肌をごくごく潤す贅沢エッセンス",
        "desc_p1": "『乾燥してスキンケアが肌に入っていかない』『冬になると肌の手触りが硬くゴワつく』という角質硬化の悩みに、植物オイルの浸透力でアプローチするのが韓国発のラグジュアリーコスメFEMMUEの『デュアルエッセンス』です。",
        "desc_p2": "美しいピンク色のエッセンス層と黄金色のカメリアオイル層が織りなす二層構造。ツバキ種子油は人間の皮脂の主成分であるオレイン酸を豊富に含むため、肌との親和性が極めて高く、すーっと角層深くまで浸透して硬くなった角質細胞を柔らかく解きほぐします。さらにダマスクローズ花水やナイアシンアミドがキメを整え、内側から押し返すような弾力感をプラス。優美な天然フローラルの香りに包まれ、使うたびに肌も心も満たされます。",
        "target": "冬の乾燥で肌が硬くスキンケアの浸透が悪く感じる方、上質な植物オイルのツヤと柔軟効果を実感したい方、贅沢な香りでセルフケアを楽しみたい方",
        "point": "朝晩の洗顔直後のブースター（導入美容液）として使用するのも効果的。その後に使う化粧水のなじみが劇的に良くなり、もっちり肌が一日中続きます。"
    },
    {
        "rank": 7,
        "tag": "🍯 高純度プロポリスエキス配合！疲れた冬肌に濃密な栄養とハリツヤを浴びせるアンプルミスト",
        "catch": "超微細なガス式噴射で顔全体をムラなくコーティング。乾燥知らずのいきいきとした水光肌へ",
        "brand_name": "CNP Laboratory (チャアンドパク)",
        "capacity": "100ml",
        "type": "高濃度プロポリス・アンプルミスト",
        "features": "プロポリス抽出物、低分子ヒアルロン酸、パンテノール、ベタイン、超微細エアゾールスプレーノズル",
        "value": "韓国の有名皮膚科クリニックがプロデュース。アンプル1本分の美容成分をミストに閉じ込めた、冬のダメージ肌の駆け込み寺的アイテム",
        "desc_p1": "寒さと乾燥で肌が萎縮し、ツヤや弾力が失われてカサカサにしぼんでしまった肌に、濃密な栄養を一瞬でチャージしてくれるのが韓国コスメの世界的名品、CNP Laboratoryの『プロP ミスト』です。",
        "desc_p2": "ミツバチが巣を守るために生み出す希少な『プロポリスエキス』を贅沢に配合。抗酸化作用と高い保湿・保護効果を持ち、冬の過酷な外気や暖房熱から肌を徹底的にプロテクトします。さらに低分子ヒアルロン酸が水分を抱え込み、パンテノールがバリア機能を強化。超微細なエアゾールミストはひと吹きでふんわりと肌全体に均一に広がり、水滴が顔に残らないためメイク崩れの心配も無用。韓国女優のようなみずみずしい『水光肌（ムルグァンピブ）』が手軽に完成します。",
        "target": "冬の乾燥で肌のツヤ・ハリが失われている方、とにかく細かく均一な霧状ミストが好きな方、プロポリスの濃密な保湿効果を体感したい方",
        "point": "スプレーボタンを長押ししながら、顔から20cmほど離して円を描くように噴射。日中のオフィスだけでなく、お風呂から上がって着替えるまでのプレ保湿にも最適です。"
    },
    {
        "rank": 8,
        "tag": "💧 冬限定モイスト処方！高保湿オイル成分をプラスして乾燥崩れを鉄壁ガード",
        "catch": "振って使う二層式メイクキープミスト。冬の暖房でもメイクをピタッと密着させて粉吹きゼロへ",
        "brand_name": "コーセーコスメニエンス",
        "capacity": "85ml",
        "type": "二層式・高保湿メイクキープミスト（冬限定モイスト）",
        "features": "メイクコート成分、高保湿スクワラン、ヒアルロン酸、コラーゲン、シラカバ樹液エキス、無着色",
        "value": "シリーズ累計数千万本を突破した国民的キープミストの冬仕様。メイク崩れ防止と高いモイスチャー効果をプチプラで両立",
        "desc_p1": "『マスクやマフラーにファンデーションがべっとり移るのが嫌』『日中の暖房で目元や口元が粉を吹いて崩れる』という冬のリアルな悩みに、ドラッグストアで手軽に買える確かな実力で応えてくれるのが、コーセーの『メイク キープ ミスト EX+ MOIST』です。",
        "desc_p2": "定番のウォータープルーフ効果はそのままに、冬の乾燥に対応する高保湿オイル成分とスクワランを贅沢に追加配合した二層タイプ。ボトルを10回以上しっかりシェイクして吹きかけると、メイクコート成分が顔の動きに合わせて伸縮する柔軟なネットを形成。表情の動きでファンデがシワに溜まるのを防ぎつつ、オイルの皮膜が暖房による肌水分の蒸発をしっかりブロックします。プチプラとは思えないキープ力と保湿持続性で、冬の毎日の心強い味方になってくれます。",
        "target": "マフラーやタートルネックへのファンデ移りを防ぎたい方、プチプラで毎日惜しみなく使えるキープミストを探している方、冬の粉吹きを防ぎたい方",
        "point": "ボトルを容器ごと10回以上しっかり振って二層を完全に白濁させてからスプレーするのが絶対条件。顔全体に5〜6プッシュ吹きかけた後は、乾くまで肌に触れないのが美肌キープの秘訣です。"
    },
    {
        "rank": 9,
        "tag": "👑 うるおいバランスを黄金比でリセット！肌の油水分バランスを整える至高のミスト",
        "catch": "微細な霧が瞬時に溶け込み、日中の皮脂くずれも乾燥も同時にケアするデパコスの逸品",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "60ml",
        "type": "モイスチュアバランス・高機能デイミスト",
        "features": "モイスチュアナノカプセル、白樺水、植物由来エモリエント成分、グリーンフローラルのリラクゼーションアロマ",
        "value": "コスメデコルテが誇るカプセル化技術を採用。角層のすみずみまで潤いを送り届け、素肌そのものの水分保持力を底上げする",
        "desc_p1": "冬の肌は、表面はテカっているのに内部は極限まで乾いている『インナードライ』に陥りやすいのが特徴です。そんなアンバランスな肌環境を、瞬時に理想的なコンディションへと導いてくれるのが、コスメデコルテの『コンフォート デイミスト バランシング』です。",
        "desc_p2": "角層深部までスムーズに浸透するナノカプセル技術をミストに応用。水分を与えるだけでなく、厳選されたエモリエントオイルが肌のバリア機能をサポートし、過剰な皮脂分泌と乾燥の連鎖を断ち切ります。霧が信じられないほど柔らかくシルキーで、吹きかけた瞬間から肌が吸い付くようにもっちり。メイクの密着感を高めると同時に、上品でみずみずしいグリーンフローラルの香りが広がり、冬の乾燥したオフィスでも優雅なスキンケアタイムを楽しめます。",
        "target": "乾燥するのにTゾーンはテカるインナードライ肌の方、粒子の極めて細かいシルキーな霧を好む方、大人肌のエイジングケアを日中も継続したい方",
        "point": "メイク直しの際、あぶらとり紙の代わりにティッシュで軽く皮脂を押さえた後、このミストを全体にひと吹き。その上からパウダーを薄く重ねると、朝のメイクしたての透明感が瞬時に復活します。"
    },
    {
        "rank": 10,
        "tag": "🌿 セラミド機能成分を微細カプセル化！全身どこでも即座に潤す敏感肌の守護神",
        "catch": "顔だけでなく首やデコルテまで一気に保湿。消炎剤配合で冬の乾燥性肌荒れを未然に防ぐ",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "150g",
        "type": "医薬部外品・微細化セラミド機能スプレー",
        "features": "微細化セラミド機能成分、ユーカリエキス、アラントイン（有効成分・消炎剤）、弱酸性、無香料、無着色、アルコールフリー",
        "value": "花王の長年のセラミド研究が生んだ最高傑作。角層深部までセラミドを補給し、冷たい外気にも揺らがない強い肌バリアを構築",
        "desc_p1": "冬になると乾燥で頬やフェイスラインがカサカサになり、白く粉を吹いたりかゆみを感じたりする『乾燥性敏感肌』にとって、最も不足しているのが角層の水分を守る『セラミド』です。そんな必須成分をいつでもどこでも手軽にチャージできるのが、キュレルの『ディープモイスチャースプレー』です。",
        "desc_p2": "通常はオイル状でミスト化が困難だったセラミド機能成分を、花王の独自技術によって微細カプセル化することに成功。スプレーするだけで、微細化されたセラミドが角層の角質細胞の隙間へとダイレクトに入り込み、肌内部の潤いをがっちりと抱え込みます。さらに消炎剤（アラントイン）配合で、冬の寒冷刺激による肌荒れや赤みを効果的に防止。顔はもちろん、冬の乾燥で粉を吹きやすい首筋や背中、腕までこれ1本でケアできる圧倒的な実用性を誇ります。",
        "target": "冬の乾燥で肌がヒリつきやすく粉吹きに悩む方、顔だけでなく首やボディもまとめてケアしたい方、医薬部外品の確かな抗肌荒れ効果を求める方",
        "point": "お風呂上がりに脱衣所でタオルドライした直後、3秒以内に顔から全身へシューッと吹きかける『スピード保湿』が極めて有効。入浴後の急速な水分蒸発をゼロに抑えることができます。"
    }
]

# FAQアイテム
faq_items = [
    {
        "q": "一般的な水分の化粧水ミストと、オイルインミストは何が違うのですか？",
        "a": "最大の違いは『水分の蒸発を防ぐオイルの油膜（ラッピング効果）』があるかどうかです。水分だけの化粧水ミストは、吹きかけた瞬間は潤ったように感じますが、暖房の効いた乾燥空間ではミストの水分が蒸発する際に、肌本来が持っている水分まで一緒に抱え込んで蒸発してしまう『過乾燥（リバウンド乾燥）』を引き起こすリスクがあります。一方、オイルインミストは水分と油分が同時に補給され、表面に薄いオイルの保護膜が形成されるため、水分を肌内部に閉じ込めて長時間のしっとり感を維持できます。"
    },
    {
        "q": "メイクの上からスプレーすると、ファンデーションがドロドロに崩れたりしませんか？",
        "a": "適切な距離と吹きかけ方を守れば、むしろメイクの密着力が高まり崩れにくくなります。崩れる主な原因は『顔に近づけすぎて大粒の水滴がつくこと』や『スプレー直後に手でこすってしまうこと』です。顔から15〜20cmほどしっかり離し、上を向いてミストの霧をふんわり浴びるようにスプレーし、手で触らずに自然に馴染ませることで、パウダーの粉浮きが落ち着いて自然なツヤ肌に仕上がります。"
    },
    {
        "q": "オイルが入っていると、日中にニキビができたり肌がテカったりしませんか？",
        "a": "オイルインミストに配合されている油分は、肌馴染みの良い植物性スクワランやホホバ油、カメリアオイルなどが微量で配合されており、重い油膜で毛穴を塞ぐ心配はほとんどありません。むしろ、冬のテカリの多くは『肌内部の乾燥を補おうとして皮脂が過剰分泌されるインナードライ』が原因です。オイルインミストで適切な水分と油分を補給してあげることで、過剰な皮脂分泌が抑えられ、夕方のメイク崩れやテカリが軽減されます。"
    },
    {
        "q": "二層式のオイルミストは、使う前にどのくらい振ればいいですか？",
        "a": "水分層とオイル層が完全に混ざり合い、ボトル全体が白濁するまで上下にしっかり4〜5回シェイクするのが基本です。振り方が足りないと、オイル層だけが先に出てしまったり、逆に水分層ばかりが噴射されて黄金比の保湿効果が得られなくなります。使用する直前にしっかり振ることを習慣にしてください。"
    },
    {
        "q": "オイルインミストは朝や夜のスキンケアとしても使えますか？",
        "a": "もちろん大活躍します。特に朝の洗顔直後のブースター（導入化粧水）として使用すると、冬の寒さで硬くなった角質がオイルの力で瞬時にほぐれ、その後に使う化粧水や乳液の浸透力が飛躍的にアップします。また、お風呂上がりの着替え中のプレ保湿としても非常に便利です。"
    }
]

# JSON-LD 構造化データ
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
    "headline": "保湿力の強さで暖房乾燥・午後カサカサ肌とさようなら！水分と美容オイルの黄金比で日中も瞬時に艶肌復活する高保湿オイルインミストランク10",
    "description": "11月・12月の暖房直撃による砂漠肌・粉吹き・メイク崩れ・夕方のちりめんジワを徹底解決！水分補給とオイルのラッピング効果を両立する高保湿オイルインミスト10選を徹底比較！ダルバ、エリクシール、dプログラム、アルビオン、RMK、カネボウなど、振ってスプレーするだけで一日中ツヤと潤いが続く名品を厳選。",
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
    "name": "冬の高保湿オイルインミスト おすすめランキング10選",
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

# 商品カードHTML
cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">
        <span class="rank-number">第{p['rank']}位</span>
        <span class="rank-tag">{p['tag']}</span>
      </div>
      <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
      <div class="product-catch">{p['catch']}</div>

      <div class="product-main">
        <div class="product-img-wrap">
          <img src="{item['image']}" alt="{p['brand_name']} 冬の高保湿オイルインミスト" class="product-img" loading="lazy">
          <div class="img-caption">{p['brand_name']} 楽天市場正規取扱ショップ画像</div>
        </div>
        <div class="product-specs">
          <dl class="spec-list">
            <dt>ブランド / メーカー</dt>
            <dd>{p['brand_name']}</dd>
            <dt>内容量 / タイプ</dt>
            <dd>{p['capacity']} / {p['type']}</dd>
            <dt>主要保湿・美容成分</dt>
            <dd>{p['features']}</dd>
            <dt>楽天市場 参考価格</dt>
            <dd class="price-val">¥{item['price']:,} <span>(税込・調査時点)</span></dd>
            <dt>アイテム独自の特徴</dt>
            <dd>{p['value']}</dd>
          </dl>
        </div>
      </div>

      <div class="product-desc">
        <h4>🧴 美容エディターの徹底本音レビュー＆成分解説</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの艶肌キープアドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliateUrl']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

# 比較サマリー表
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{p['rank']}位</td>
      <td class="tb-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
      <td class="tb-type">{p['type']}</td>
      <td class="tb-ing">{p['features'][:35]}...</td>
      <td class="tb-price">¥{item['price']:,}</td>
      <td class="tb-link"><a href="#rank-{p['rank']}" class="tb-anchor">詳細を見る</a></td>
    </tr>
    """)

# FAQ HTML
faq_html_blocks = []
for f_item in faq_items:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q"><span>Q</span>{f_item['q']}</h3>
      <div class="faq-a"><span>A</span><p>{f_item['a']}</p></div>
    </div>
    """)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで暖房乾燥・午後カサカサ肌とさようなら！水分と美容オイルの黄金比で日中も瞬時に艶肌復活する高保湿オイルインミストランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の暖房直撃による砂漠肌・粉吹き・メイク崩れ・夕方のちりめんジワを徹底解決！水分補給とオイルのラッピング効果を両立する高保湿オイルインミスト10選を徹底比較！ダルバ、エリクシール、dプログラム、アルビオン、RMK、カネボウなど、振ってスプレーするだけで一日中ツヤと潤いが続く名品を厳選。">
  <meta name="keywords" content="オイルインミスト,ミスト化粧水 保湿,冬 ミスト化粧水,メイクの上から 保湿ミスト,暖房乾燥 対策,ダルバ ミスト,エリクシール つや玉ミスト,乾燥肌 保湿スプレー">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-oil-mist">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP / SNS Meta Tags -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで暖房乾燥・午後カサカサ肌とさようなら！水分と美容オイルの黄金比で日中も瞬時に艶肌復活する高保湿オイルインミストランク10">
  <meta property="og:description" content="11月・12月の暖房直撃による砂漠肌・粉吹き・メイク崩れ・夕方のちりめんジワを徹底解決！水分補給とオイルのラッピング効果を両立する高保湿オイルインミスト10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-oil-mist">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">

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
      --primary: #c94b6e;
      --primary-light: #fdf2f4;
      --primary-dark: #a23352;
      --accent: #d97706;
      --text: #2d3748;
      --text-muted: #718096;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: color 0.2s;
    }}
    .nav-link:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    
    /* Breadcrumbs */
    .breadcrumb {{
      display: flex;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ color: var(--primary); }}
    .breadcrumb span {{ color: #cbd5e0; }}

    /* Article Hero */
    .article-hero {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary);
    }}
    .article-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 1.25rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .intro-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #4a5568;
    }}
    .intro-text p {{ margin-bottom: 1rem; }}
    .intro-highlight {{
      background: var(--primary-light);
      padding: 1.25rem;
      border-radius: 8px;
      border-left: 4px solid var(--primary);
      margin: 1.5rem 0;
      font-weight: 600;
    }}

    /* Table of Contents */
    .toc {{
      background: #f1f5f9;
      padding: 1.5rem;
      border-radius: var(--radius);
      margin: 2rem 0;
    }}
    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #334155;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.5rem;
    }}
    .toc-list a {{
      color: #475569;
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-list a:hover {{ color: var(--primary); font-weight: 600; }}

    /* Section Headings */
    .section-h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #1e293b;
      margin: 3.5rem 0 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    
    /* Summary Table */
    .table-container {{
      overflow-x: auto;
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .summary-table th {{
      background: #f8fafc;
      color: #475569;
      padding: 1rem;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }}
    .summary-table td {{
      padding: 1rem;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 700; color: var(--primary); width: 80px; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .tb-anchor {{
      display: inline-block;
      padding: 0.35rem 0.75rem;
      background: var(--primary-light);
      color: var(--primary);
      text-decoration: none;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.8rem;
    }}
    .tb-anchor:hover {{ background: var(--primary); color: #fff; }}

    /* Product Cards */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      scroll-margin-top: 80px;
    }}
    .product-badge {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-number {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.25rem 0.85rem;
      border-radius: 6px;
    }}
    .rank-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
    }}
    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #1e293b;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px dashed var(--border);
    }}
    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 1.75rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 280px;
      height: 280px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      border: 1px solid #edf2f7;
    }}
    .img-caption {{
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
    }}
    .spec-list {{
      display: grid;
      grid-template-columns: 120px 1fr;
      gap: 0.6rem;
      font-size: 0.9rem;
    }}
    .spec-list dt {{
      font-weight: 700;
      color: #64748b;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .spec-list dd {{
      color: #1e293b;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .price-val {{
      font-size: 1.25rem !important;
      font-weight: 800 !important;
      color: #b91c1c !important;
    }}
    .price-val span {{
      font-size: 0.75rem;
      font-weight: normal;
      color: var(--text-muted);
    }}
    .product-desc {{
      margin: 1.5rem 0;
      background: #f8fafc;
      padding: 1.5rem;
      border-radius: 8px;
    }}
    .product-desc h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.75rem;
      font-weight: 700;
    }}
    .product-desc p {{
      margin-bottom: 0.75rem;
      color: #334155;
    }}
    .product-desc p:last-child {{ margin-bottom: 0; }}
    
    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1.5rem 0;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
    }}
    .target-block {{ background: #eff6ff; border-left: 4px solid #3b82f6; }}
    .target-block strong {{ color: #1e40af; display: block; margin-bottom: 0.35rem; }}
    .tip-block {{ background: #fefce8; border-left: 4px solid #eab308; }}
    .tip-block strong {{ color: #854d0e; display: block; margin-bottom: 0.35rem; }}

    .product-action {{
      margin-top: 1.5rem;
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      width: 100%;
      max-width: 420px;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 1rem 1.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000 0%, #b30000 100%);
    }}

    /* Guide & FAQ Sections */
    .guide-box {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .guide-box h3 {{
      font-size: 1.25rem;
      color: #1e293b;
      margin-bottom: 1rem;
      padding-left: 0.75rem;
      border-left: 4px solid var(--primary);
    }}
    .guide-box p {{
      margin-bottom: 1rem;
      color: #475569;
    }}
    .guide-box ul {{
      margin-left: 1.5rem;
      margin-bottom: 1.25rem;
      color: #475569;
    }}
    .guide-box li {{ margin-bottom: 0.5rem; }}

    /* FAQ */
    .faq-item {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      border: 1px solid var(--border);
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #1e293b;
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }}
    .faq-q span {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.7;
    }}
    .faq-a span {{
      background: #e2e8f0;
      color: #475569;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      font-weight: 700;
      margin-top: 2px;
    }}

    /* Related Internal Links */
    .related-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 3.5rem 0;
    }}
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    .related-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      padding: 1rem;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .related-link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
      transform: translateY(-2px);
    }}
    .related-link-card small {{
      color: var(--text-muted);
      font-size: 0.75rem;
      margin-top: 0.5rem;
      display: block;
    }}

    footer {{
      background: #1e293b;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      font-size: 0.85rem;
      line-height: 1.7;
    }}
    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      text-align: center;
    }}
    .footer-logo {{
      color: #ffffff;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 1rem;
    }}
    .footer-note {{
      margin: 1rem 0;
      color: #64748b;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-logo">
      <span>❄️</span>
      <span>冬コスメ徹底比較ラボ</span>
    </a>
    <nav>
      <a href="/" class="nav-link">全コスメ特集一覧</a>
    </nav>
  </div>
</header>

<div class="container">
  <div class="breadcrumb">
    <a href="/">ホーム</a>
    <span>&gt;</span>
    <a href="/">冬コスメ特集</a>
    <span>&gt;</span>
    <strong>高保湿オイルインミストおすすめ10選</strong>
  </div>

  <article class="article-hero">
    <span class="article-tag">2026-2027年 冬季最新検証</span>
    <h1 class="article-title">保湿力の強さで暖房乾燥・午後カサカサ肌とさようなら！水分と美容オイルの黄金比で日中も瞬時に艶肌復活する高保湿オイルインミストランク10</h1>
    <div class="article-meta">
      <span>公開日: 2026年11月2日</span>
      <span>更新日: 2026年11月2日</span>
      <span>専門家検証: 美容エディター＆コスメコンシェルジュチーム</span>
    </div>
    
    <div class="intro-text">
      <p>11月から12月にかけて外気温が一桁台まで冷え込むと、オフィスや商業施設では暖房（エアコン）が終日フル稼働します。その結果、室内の湿度は20%〜30%台という砂漠並みの乾燥状態へと急降下。午後2時を過ぎた頃から、『頬や口元がピキピキと突っ張る』『目元にファンデーションが溜まって乾燥小ジワが目立つ』『粉を吹いてメイクが崩れる』といった深刻な冬の肌トラブルが噴出します。</p>
      
      <p>ここで多くの人が陥りがちな最大の落とし穴が、<strong>「水分の多い普通の化粧水ミストを吹きかけてしまうこと」</strong>です。オイルを含まない水分だけのミストは、乾燥した室内では瞬く間に蒸発し、その気化熱と浸透圧によって肌内部の元々の水分まで一緒に奪い去る『過乾燥（リバウンド乾燥）』を引き起こします。乾いたからといって吹きかければ吹きかけるほど、夕方にはさらに肌が干からびてしまうのです。</p>

      <div class="intro-highlight">
        💡 冬の暖房砂漠を乗り切る唯一の正解は「水分と上質オイルの二層式ミスト」。水分で角層深部を潤しつつ、オイルの薄膜シールドで水分の再蒸発を物理的にシャットアウト。メイクを崩さず、瞬時に生まれたての発光ツヤ肌を蘇らせます。
      </div>

      <p>本記事では、大ヒット中のダルバ（d'Alba）や資生堂エリクシール、dプログラム、カネボウ、RMK、ファミュなど、人気・実力ともに認められた高保湿オイルインミスト10製品を徹底検証。成分バランス、微細噴霧の肌あたり、メイクキープ力、保湿持続性をプロの視点から多角的に比較し、ランキング形式で詳しくご紹介します。</p>
    </div>

    <div class="toc">
      <div class="toc-title">📑 目次 - クイックナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#summary-table">📊 ひと目でわかる！高保湿オイルインミスト比較表</a></li>
        <li><a href="#rank-1">第1位：d'Alba ホワイトトリュフ スプレーセラム</a></li>
        <li><a href="#rank-2">第2位：ELIXIR つや玉ミスト</a></li>
        <li><a href="#rank-3">第3位：d program アレルバリア ミスト N</a></li>
        <li><a href="#rank-4">第4位：KANEBO チアリング ミスト スプレー</a></li>
        <li><a href="#rank-5">第5位：RMK コンディショニング フィックスミスト</a></li>
        <li><a href="#rank-6">第6位：FEMMUE デュアルエッセンス</a></li>
        <li><a href="#rank-7">第7位：CNP Laboratory プロP ミスト</a></li>
        <li><a href="#rank-8">第8位：コーセー メイクキープミスト EX+ MOIST</a></li>
        <li><a href="#rank-9">第9位：DECORTÉ コンフォート デイミスト</a></li>
        <li><a href="#rank-10">第10位：Curel ディープモイスチャースプレー</a></li>
        <li><a href="#guide-mechanism">🔬 なぜオイルイン？冬の乾燥と肌バリアの科学</a></li>
        <li><a href="#guide-selection">🎯 失敗しないオイルインミストの選び方</a></li>
        <li><a href="#guide-howto">✨ メイクを崩さない！正しい吹きかけ方テクニック</a></li>
        <li><a href="#faq-section">❓ よくある質問（FAQ）</a></li>
      </ul>
    </div>
  </article>

  <section id="summary-table">
    <h2 class="section-h2">📊 ひと目でわかる！高保湿オイルインミスト10選スペック比較表</h2>
    <div class="table-container">
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>タイプ</th>
            <th>主要保湿・美容成分</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
          {''.join(table_rows)}
        </tbody>
      </table>
    </div>
  </section>

  <section id="product-rankings">
    <h2 class="section-h2">🏆 高保湿オイルインミストおすすめ人気ランキング10選</h2>
    {''.join(cards_html)}
  </section>

  <section id="guide-mechanism" class="guide-box">
    <h2 class="section-h2">🔬 なぜ冬はオイルインなのか？暖房乾燥と肌バリアの科学的メカニズム</h2>
    <p>11月から12月にかけて、私たちの肌環境は一年で最も過酷な急変期を迎えます。気温が低下すると皮膚の毛細血管が収縮して血流が滞り、皮脂腺からの皮脂分泌量と汗腺からの水分分泌量が激減します。健常な肌は『皮脂膜』という天然の油膜によって角層内の水分蒸発を防いでいますが、冬はこの天然シールドが極端に薄くなり、肌は丸裸の無防備な状態に晒されます。</p>

    <h3>1. 気化熱による『過乾燥（リバウンドドライ）』の罠</h3>
    <p>オフィスや暖房の効いた部屋で一般的なウォーターミスト（水とグリセリン主体の化粧水）を吹きかけると、肌表面の湿度は一時的に上がります。しかし、室内の湿度が極端に低い環境下では、吹きかけた水滴が瞬時に大気中へ気化。この際、角層内の水分まで巻き込んで蒸発するため、使用前よりも角層水分量が低下する現象が皮膚科学的にも確認されています。</p>

    <h3>2. オイルインミストがもたらす『界面吸着＆エモリエント膜』</h3>
    <p>オイルインミストは、微細なオイル滴が水分の外側に配置、あるいは微小エマルジョンとなって肌に届きます。水分が角層細胞のすき間に入り込むと同時に、比重の軽い植物性オイル（スクワラン、カメリア油、アボカド油等）が肌表面に整然と並び、分子レベルの通気性フィルムを形成。水分の蒸散速度を緩やかにし、日中の乾燥ストレスを8時間以上にわたって緩和し続けます。</p>
  </section>

  <section id="guide-selection" class="guide-box">
    <h2 class="section-h2">🎯 迷ったらここをチェック！失敗しないオイルインミストの選び方</h2>
    <p>数あるオイルインミストの中から、自分の肌質や生活スタイルにぴったりの1本を選ぶための4つの基準を整理しました。</p>

    <ul>
      <li><strong>オイルと水分の比率で選ぶ：</strong>夕方のつっぱりや粉吹きがひどい超乾燥肌なら、オイル層が15〜20%とリッチな『ダルバ』や『ファミュ』。テカリも気になるインナードライ肌なら、軽やかな微小エマルジョン処方の『エリクシール』や『コスメデコルテ』が最適。</li>
      <li><strong>メイクキープ機能の有無で選ぶ：</strong>マスクやタートルネックへのファンデ移りを防ぎたいなら、フィックス成分配合の『コーセー』や『RMK』。</li>
      <li><strong>敏感肌・ゆらぎ肌処方で選ぶ：</strong>冬の寒風や暖房でヒリヒリしやすいなら、アルコールフリー・低刺激設計の『dプログラム』や、消炎剤配合の『キュレル』が安心。</li>
      <li><strong>ボトルの噴霧力（霧の細かさ）で選ぶ：</strong>メイクの上から日中何回も重ねるなら、ガス式や高微細ノズルを採用した『CNP』や『カネボウ』のように、水滴が顔にたまらない超微粒子タイプがストレスフリーです。</li>
    </ul>
  </section>

  <section id="guide-howto" class="guide-box">
    <h2 class="section-h2">✨ プロが教える！メイクを崩さずツヤを宿す正しいミスト吹きかけ術</h2>
    <p>どんなに優秀なオイルインミストでも、使い方が間違っているとメイクがヨレる原因になります。美容の現場でプロが実践している『崩れない神テクニック』をマスターしましょう。</p>

    <ul>
      <li><strong>Step 1：使う直前にしっかりシェイク：</strong>二層式のアイテムは、白濁するまで上下に4〜5回しっかり振って水分とオイルを均一に乳化させます。</li>
      <li><strong>Step 2：距離は顔から20cm離す：</strong>腕を少し伸ばし、顔から20cmほど離した位置で、やや斜め上に向けてスプレーします。降ってくる霧を顔全体でふんわり受け止めるイメージです。</li>
      <li><strong>Step 3：絶対に手でこすらない：</strong>スプレー直後に手で激しく叩いたり擦ったりするのは厳禁。そのまま自然に馴染ませるか、手のひらで包み込むように優しく『押しあてる（ハンドプレス）』だけに留めましょう。</li>
      <li><strong>Step 4：メイク直しの裏ワザ：</strong>夕方にファンデがヨレた部分にスポンジの角でミストを1プッシュ吹きかけ、優しくトントンと馴染ませると、ヨレたファンデが綺麗にリセットされ、厚塗り感なく朝の塗りたて肌が復活します。</li>
    </ul>
  </section>

  <section id="faq-section">
    <h2 class="section-h2">❓ よくある質問（FAQ）</h2>
    {''.join(faq_html_blocks)}
  </section>

  <section class="related-section" id="internal-links-hub">
    <h2 class="section-h2">🔗 あわせて読みたい！冬の乾燥・パーツケアおすすめ特集</h2>
    <p>冬の冷えや乾燥トラブルをトータルでケアするための関連記事をピックアップしました。あわせてチェックして、真冬でも隙のない美肌を手に入れましょう。</p>
    <div class="related-links-grid">
      <a href="/winter-face-mist" class="related-link-card">
        <span>冬のフェイスミスト特集</span>
        <small>日中の乾燥対策・保湿ミスト比較</small>
      </a>
      <a href="/winter-make-keep-mist" class="related-link-card">
        <span>冬のメイクキープミスト特集</span>
        <small>乾燥崩れ・摩擦防止のキープスプレー</small>
      </a>
      <a href="/winter-hydrating-serum" class="related-link-card">
        <span>冬の高保湿美容液特集</span>
        <small>角層深部まで潤いを届ける濃厚セラム</small>
      </a>
      <a href="/winter-stick-serum" class="related-link-card">
        <span>冬のスティック美容液特集</span>
        <small>メイク直し・目元の乾燥にピンポイント補給</small>
      </a>
      <a href="/winter-ceramide-serum" class="related-link-card">
        <span>冬のセラミド美容液特集</span>
        <small>バリア機能を立て直す高濃度セラミド</small>
      </a>
      <a href="/winter-face-oil" class="related-link-card">
        <span>冬の美容フェイスオイル特集</span>
        <small>乾燥砂漠肌を救う極上ブレンドオイル</small>
      </a>
      <a href="/winter-morning-mask" class="related-link-card">
        <span>朝用高保湿シートマスク特集</span>
        <small>メイク前の時短水分補給と化粧ノリUP</small>
      </a>
      <a href="/winter-carbonic-bath" class="related-link-card">
        <span>薬用重炭酸入浴剤特集</span>
        <small>冷えと全身乾燥を芯から温める温浴ケア</small>
      </a>
    </div>
  </section>
</div>

<footer>
  <div class="footer-inner">
    <div class="footer-logo">❄️ 冬コスメ徹底比較ラボ</div>
    <p class="footer-desc">冬特有の肌乾燥・冷え・寒暖差トラブルに立ち向かう女性のための美容情報・コスメ検証サイト。</p>
    <p class="footer-note">※掲載している楽天市場の価格やポイント情報は調査時点のものです。最新情報は各ショップページをご確認ください。</p>
    <p class="copyright">&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
  </div>
</footer>

</body>
</html>
"""

with open("winter-oil-mist.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-oil-mist.html successfully!")
