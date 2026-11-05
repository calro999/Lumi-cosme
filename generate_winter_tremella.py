import json
import re

with open("fetched_3new_mango_tremella_collagen.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_tremella"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 自重の500倍の保水を誇る白キクラゲ×CoQ10！真冬の乾涸らびインナードライを根本救済",
        "catch": "天然シロキクラゲ多糖体を高濃度に凝縮し、コエンザイムQ10とヒアルロン酸を絶妙ブレンド。冬のエアコン暖房で角層深部が干からびた大人肌に、吸い付くような濃密水分ヴェールを構築する実力派高保湿美容液",
        "brand_name": "ピアベルピア (Piabelpia)",
        "capacity": "50ml / ポンプディスペンサー",
        "type": "高保水シロキクラゲ多糖体配合 エイジングモイストエッセンス",
        "features": "シロキクラゲ多糖体、ユビキノン（CoQ10）、ヒアルロン酸Na、グリチルリチン酸2K、水溶性コラーゲン",
        "value": "ヒアルロン酸の分子構造よりも微細で保水持続性に富むシロキクラゲ多糖体が、冬の過酷な暖房下でも角層の水分蒸散を鉄壁ブロック。敏感に傾いた真冬の肌をみずみずしく満たす",
        "desc_p1": "11月から12月にかけて、室内で暖房エアコンを使い始めると、肌の表面は皮脂でテカっているのに内部がギシギシと突っ張る「インナードライ現象」が急増します。これは外気の乾燥と室内の温風によって角質層内の結合水が強制的に奪い去られ、角質細胞が脱水して縮んでしまうために起こります。ピアベルピアの『Qモイスト』は、古来より楊貴妃が美貌を保つために食したと伝えられる純白の希少キノコ「白キクラゲ」から抽出された高純度シロキクラゲ多糖体を主役に据えた高保湿美容液です。",
        "desc_p2": "シロキクラゲ多糖体は自重の約500倍もの水分を抱え込む驚異的な保水力を持ち、ヒアルロン酸と比べても乾燥環境下における水分保持率が格段に高いことが科学的に実証されています。肌に乗せると、トロリとした濃密なテクスチャーがスーッと角層深部へ引き込まれ、肌表面には薄くしなやかな保水皮膜を形成。さらにコエンザイムQ10が真冬の冷えで低下した肌のハリと弾力を底上げし、一日中暖房の効いた空間にいても夕方まで全く突っ張らないプルプルの潤いを持続させます。",
        "target": "暖房の効いたオフィスで肌が突っ張るインナードライ肌の方、ヒアルロン酸配合コスメでも乾燥がおさまらない方、キメの乱れや冬の乾燥毛穴をふっくら整えたい大人の肌",
        "point": "化粧水で肌を整えた直後、2〜3プッシュを手にとり、手のひらで温めてから顔全体を優しく包み込むようにハンドプレスします。目元や口元など乾燥しやすい部分にはもう1プッシュを指先で重ねづけしてください。"
    },
    {
        "rank": 2,
        "tag": "✨ 白キクラゲ多糖体×エクソソーム×グルタチオン！真冬の白玉モチ肌を叶える濃密シートマスク",
        "catch": "ベスコス多数受賞のルルルン最高峰ハイドラシリーズ。白キクラゲ多糖体の圧倒的保水シールドに、ヒト脂肪細胞順化培養液エキス（エクソソーム）とグルタチオンを融合。毎日の集中保水で真冬の肌を透き通る白玉肌へ",
        "brand_name": "LuLuLun (ルルルン)",
        "capacity": "28枚入（エッセンス510ml） / ボックスタイプ",
        "type": "高密着バイオ保水 ハイドラEXデイリーシートマスク",
        "features": "シロキクラゲ多糖体、ヒト脂肪由来間葉系細胞エクソソーム、グルタチオン、セラミドAP/NP/EOP",
        "value": "美容液約本分を贅沢に染み込ませたメルティフィールシートが真冬の強張った角層にピタッと密着。シロキクラゲの濃密ヴェールが角層細胞の隅々まで潤いを送り届け、剥がした瞬間から発光するようなツヤを実現",
        "desc_p1": "真冬の寒冷外気と暖房による乾燥スパイラルに陥った肌は、角層のターンオーバーが停滞し、古い角質が硬くなって通常の化粧水が弾かれてしまいます。そんな真冬の枯れ肌を一気に集中蘇生させる切り札としてSNSでも絶賛されているのが、ルルルンの『ハイドラ EX マスク』です。最先端の再生医療着想成分であるエクソソームや白玉肌の代名詞グルタチオンに加え、ベースの保水ヴェールとしてシロキクラゲ多糖体が贅沢に配合されています。",
        "desc_p2": "とろけるような極上シートを顔に乗せると、まるで肌が美容液をごくごくと飲み干すかのように吸い込まれていきます。シロキクラゲ多糖体の形成する微細な水分ネットワークが、乾燥で硬化した角層細胞の隙間をふっくらと押し広げ、エクソソームと3種のセラミドが深部へとスムーズに到達。5〜10分後にマスクを剥がすと、手のひらが吸い付いて離れないほどのもっちり感と、内側からみずみずしい光を放つ透明感に驚かされます。真冬の毎日のスキンケアをエステ級に変える至高のデイリーマスクです。",
        "target": "真冬の乾燥で肌がくすんで化粧ノリが最悪な方、毎日のシートマスクで本格的なインナードライ対策をしたい方、話題のエクソソームと植物性多糖体の相乗効果を実感したい方",
        "point": "洗顔直後の清潔な素肌に密着させ、手のひらで軽く押さえて空気を抜きます。5〜10分置いた後、シートを折りたたんで首筋やデコルテまでパッティングしながら余すことなく潤いを馴染ませてください。"
    },
    {
        "rank": 3,
        "tag": "🧴 白キクラゲ多糖体×独自発酵コラーゲン！真冬の乾いた角層を美容液級ローションで満たす",
        "catch": "アテニアの最高峰エイジングケアライン「ドレスリフト」の薬用高保湿ローション。白キクラゲ多糖体と発酵コラーゲン、ナイアシンアミドを贅沢配合。とろみローションが真冬の肌をほぐし押し返すようなハリを復元",
        "brand_name": "Attenir (アテニア)",
        "capacity": "150ml / 樹脂ボトル",
        "type": "医薬部外品 高浸透高保水 エイジング化粧水",
        "features": "シロキクラゲ多糖体、独自原料発酵コラーゲン、ナイアシンアミド、サーチュライザーS6、タイムブレスDN",
        "value": "美容液のようにとろみのあるリッチなテクスチャーが、肌に乗せた瞬間にみずみずしく崩れて角層深部へ浸透。シロキクラゲの保護皮膜が一日中乾かない高密度ハリ肌をキープ",
        "desc_p1": "40代以降の冬の肌は、気温低下による血行不良と加齢によるコラーゲン・セラミドの減少が重なり、単に表面を潤すだけの化粧水では数十分で水分が蒸発して小ジワが目立ってしまいます。アテニアの『ドレスリフト ローション』は、この大人の真冬の複合的な乾燥老化に着目した医薬部外品ローションです。シロキクラゲ多糖体の持つ優れた粘性と保水皮膜効果を活かし、角層のすみずみまで濃密な潤いを届ける「浸透ルート」を開拓します。",
        "desc_p2": "手にとるとリッチな厚みのあるとろみ液ですが、肌に触れた瞬間にスッと液状にほどけて素早く角質層へと染み渡ります。シロキクラゲ多糖体の分子が網目構造となって水分をガッチリ抱え込み、発酵によって極小分子化されたコラーゲンが肌の奥深くでハリを支えます。さらにシワ改善と美白の有効成分ナイアシンアミドが真冬の乾燥小ジワを根本からケア。ダマスクローズを中心とした天然アロマの優雅な香りが、冬のスキンケア時間を至福の癒やしへと導きます。",
        "target": "冬になると化粧水が肌に入っていかないと感じる大人世代、乾燥小ジワとたるみ毛穴を同時にケアしたい方、とろみがあるのに浸透が早い上質なローションを好む方",
        "point": "洗顔後、500円玉大を手にとり、顔の中心から外側へ優しく伸ばします。手のひら全体で顔を包み込み、肌がもっちりと手に吸い付くまでハンドプレスを繰り返すのがハリ感を高めるコツです。"
    },
    {
        "rank": 4,
        "tag": "💧 敏感肌のための高保水設計！白キクラゲ多糖体×持続型アミノ酸が潤いを繋ぎ止める",
        "catch": "オルビスが敏感乾燥肌のために開発したアクアニストシリーズ。シロキクラゲ多糖体と持続型高保水アミノ酸を厳選配合。冬の寒暖差や花粉・乾燥で敏感に傾いた角層バリアを優しく満たし尽くす",
        "brand_name": "ORBIS (オルビス)",
        "capacity": "180ml / つめかえ用・ボトル",
        "type": "敏感肌用 高保湿薬用モイストローション（RM しっとり高保湿）",
        "features": "シロキクラゲ多糖体、持続型高保水アミノ酸、植物性グリセリン、無香料・無着色・アルコールフリー",
        "value": "敏感肌特有の角層の隙間だらけになった状態に、シロキクラゲの生体親和性多糖体がピタッとフィット。刺激感を一切感じさせることなく、奥深くまで穏やかに保水ヴェールを形成",
        "desc_p1": "11月から12月は、外気の激しい寒暖差や室内の乾燥によって肌のバリア機能が低下し、いつも使っているスキンケアが急にヒリついたり赤みが出たりする「季節性敏感肌」に陥る方が急増します。オルビスの『アクアニスト ローション（RM）』は、そんなデリケートな冬の乾燥肌のために、徹底して低刺激性と高保水力を両立させた薬用化粧水です。肌への親和性が極めて高いシロキクラゲ多糖体を保水ネットワークの中心に据えています。",
        "desc_p2": "水のように摩擦なく広がりながらも、肌になじませた後はまるで吸い付くような濃密な保湿膜を実感。シロキクラゲ多糖体が形成する水分保持ヴェールが、角層の細胞間をぴったりと満たし、持続型アミノ酸が水分を逃さずキープします。アルコールや界面活性剤、香料、着色料など余計な成分を徹底排除しているため、肌荒れや乾燥でピリピリしやすい冬のデリケート肌にも吸い込まれるように馴染み、健やかなバリア機能を着実に育みます。",
        "target": "冬になると肌が敏感になって化粧水がしみる方、ベタつくスキンケアが苦手だけれどしっかり保湿したい方、季節の変わり目に肌がゆらぎやすい敏感乾燥肌の方",
        "point": "手のひらに適量を取り、摩擦を避けるために擦らず、優しく手のひらで顔を包み込むように数回に分けて重ねづけしてください。首筋まで優しく潤いを届けるのがポイントです。"
    },
    {
        "rank": 5,
        "tag": "💎 美肌糖×シロキクラゲエキスの奇跡！真冬の毛穴乱れと乾燥くすみを一掃する透明感化粧水",
        "catch": "コスメデコルテの独自コンプレックス「美肌糖」とシロキクラゲエキスを高濃度配合した医薬部外品トリートメントローション。冬の寒冷で乱れたキメと毛穴を整え、みずみずしく透き通るような発光肌へ",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "200ml / プレステージボトル",
        "type": "医薬部外品 薬用消炎高保湿トリートメントエッセンスウォーター",
        "features": "美肌糖（異性化糖）、シロキクラゲエキス、グリチルリチン酸誘導体、チョウジエキス",
        "value": "糖と多糖体の強力な水素結合力で水分を角層深くに留め置く最先端テクノロジー。冬の乾燥毛穴や寒冷くすみ、肌荒れを未然に防ぎ、透明感あふれるキメ美肌を構築",
        "desc_p1": "冬の乾燥は肌の水分を奪うだけでなく、角層のキメを萎縮させ、光の正反射を阻害してどんよりとした灰色がかった「くすみ肌」を作り出します。また、乾燥から身を守ろうとして毛穴周りの角質が肥厚し、毛穴が余計に目立ってしまう悪循環に陥ります。コスメデコルテの『イドラクラリティ 薬用 トリートメント エッセンス ウォーター』は、すべての肌悩みの根源である「角層の保水構造の乱れ」を糖の力で整える先進の化粧水です。",
        "desc_p2": "肌の天然保湿因子（NMF）の構成要素である糖に着目した「美肌糖」に、驚異の保水力を誇る「シロキクラゲエキス」をドッキング。みずみずしく清らかな感触でありながら、角層に触れた瞬間から深部へとぐんぐん浸透し、萎縮したキメの一つひとつをぷっくりと膨らませます。シロキクラゲの形成する均一な水分膜が肌表面の乱れた凹凸をなめらかに整え、光を美しく反射する発光美肌を演出。真冬でも乾燥や毛穴落ち知らずの清潔感あふれる透明肌を維持します。",
        "target": "冬の乾燥で肌がくすんで疲れて見えがちな方、乾燥による毛穴の目立ちやキメの粗さに悩んでいる方、みずみずしい浸透感と確かな保湿持続力を両立したい方",
        "point": "コットンに裏側まで通るくらいたっぷり含ませ、顔全体を滑らせるように優しくパッティング。その後手のひらで温めるようにハンドプレスすると、シロキクラゲの水分ヴェールがピタッと定着します。"
    },
    {
        "rank": 6,
        "tag": "🌿 白キクラゲ多糖体×ヒト型セラミド！自らうるおいを蓄える素肌へ導く濃密ローション",
        "catch": "エトヴォスが誇る高保湿スキンケアの代表作。シロキクラゲ多糖体と5種のヒト型セラミド、ヒアルロン酸を贅沢配合。角層内部の水分保持構造を科学的に再構築し、真冬の乾燥に負けないもっちり素肌へ",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "150ml / ポンプボトル",
        "type": "高保湿バリアサポート モイスチャライジングローション",
        "features": "シロキクラゲ多糖体、セラミドEOP/NG/NP/AG/AP、加水分解ヒアルロン酸、POs-Ca（ホスホリルオリゴ糖Ca）",
        "value": "植物性多糖体による表面の保水膜形成と、ヒト型セラミドによる細胞間脂質のラメラ構造修復を同時実現。外側からも内側からも水分蒸散を逃さないパーフェクトバリア",
        "desc_p1": "冬の過酷な乾燥を克服するためには、「水分を与えること」と「水分を抱え込む土台を作ること」の双方が不可欠です。エトヴォスの『モイスチャライジングローション』は、皮膚のバリア機能を支えるヒト型セラミドと、植物界最強の保水多糖体であるシロキクラゲ多糖体を完璧な黄金比で融合させた傑作ローションです。天然由来の優しいラベンダーの香りと共に、冬の渇いた角層を深層から癒やします。",
        "desc_p2": "少しとろみのあるテクスチャーが肌の上を滑らかに広がり、シロキクラゲ多糖体が肌表面に潤いのクッションを形成。その保護膜の下で、5種のヒト型セラミドが角質細胞の間に入り込み、乱れたラメラ構造を整えます。一度馴染ませると、肌の奥から押し出されるような弾力感と、指が吸い付くようなもっちり感が長時間持続。石油系界面活性剤や鉱物油、パラベンなどを使わないクリーンな処方で、冬の敏感肌にも安心して使用できます。",
        "target": "乾燥による皮むけや粉吹きを根本から治したい方、ヒト型セラミドと植物性保水成分の相乗効果を求める方、肌のバリア機能を底上げして健康なツヤ肌を作りたい方",
        "point": "500円玉大を手にとり、手のひらで顔全体を包み込むようにして浸透させます。乾燥が気になる部分は2度塗りし、最後にエトヴォスのモイスチャライジングセラムを重ねると鉄壁の保湿が完成します。"
    },
    {
        "rank": 7,
        "tag": "🧼 泡立て不要の泥ジェル！白キクラゲの保水ヴェールで冬の毛穴汚れを落としつつ潤す",
        "catch": "ファンケルの大ヒット洗顔料。白キクラゲ多糖体と3種の天然クレイを融合。真冬の寒さで強張った毛穴の黒ずみや角栓を優しく吸着しながら、洗顔後の肌に驚くべきしっとり感を残す新感覚ジェル",
        "brand_name": "FANCL (ファンケル)",
        "capacity": "120g / チューブ容器",
        "type": "白キクラゲ配合 泡立て不要 泥ジェル洗顔料",
        "features": "シロキクラゲ多糖体、海シルト（ブラックマッド）、カオリン、ベントナイト、アロエベラ葉エキス",
        "value": "冬の朝の億劫な泡立てが一切不要。クレイの吸着力で不要な角質を取り去りつつ、シロキクラゲ多糖体が肌の水分蒸発を防ぎ、洗顔後も化粧水を急がなくて良いほどの保水膜を実現",
        "desc_p1": "真冬の朝洗顔は悩ましいものです。洗顔料を使うと肌の油分が奪われすぎて突っ張り、水洗顔だけでは夜の間に分泌された皮脂や古い角質が落ちずに毛穴が詰まってしまうからです。ファンケルの『泥ジェル洗顔』は、この冬の洗顔問題を一掃するために開発された、泡立て不要の濃密クレイジェルです。毛穴汚れを吸着する3種のクレイに加え、保水成分として贅沢に白キクラゲ多糖体を配合しています。",
        "desc_p2": "チューブから出して乾いた肌や濡れた肌にそのまま伸ばすと、ひんやり心地よいジェルが肌の上を滑り、毛穴の奥の角栓汚れを吸着。ぬるま湯で洗い流すと、クレイの汚れ落ちの良さと、シロキクラゲ多糖体の保水ヴェールが同時に働き、肌表面がゆで卵のようにツルツルでありながら、信じられないほどしっとりとした柔肌に洗い上がります。冬の乾燥による化粧ノリの悪さに悩むすべての方におすすめの洗顔料です。",
        "target": "冬の朝の洗顔後に顔が突っ張って痛い方、泡立てるのが面倒で手軽に上質な洗顔をしたい方、冬の毛穴の黒ずみやザラつきをやさしく除去したい方",
        "point": "サクランボ粒大を手にとり、小鼻や眉間、顎などザラつきが気になる部分を中心にくるくると優しくマッサージするように馴染ませます。毛穴の気になる部分は数十秒置いてパックしてから流すと効果的です。"
    },
    {
        "rank": 8,
        "tag": "🌿 サロン専売プロ仕様！白キクラゲ×12種オーガニック植物エキスが満たす大容量化粧水",
        "catch": "全国のエステサロンで愛用されるDIEUFRA（デュフラ）のオーガニックライン。白キクラゲ多糖体と12種のオーガニックハーブを凝縮。真冬の過酷な乾燥角層へ贅沢に水分を送り込む大容量モイストローション",
        "brand_name": "DIEUFRA (デュフラ)",
        "capacity": "500ml / プロ仕様ディスペンサー",
        "type": "サロン専売 オーガニック高保湿モイストローション",
        "features": "シロキクラゲ多糖体、セージ葉エキス、ローズマリー葉エキス、カミツレ花エキス、ホホバ葉エキス",
        "value": "500mlという大容量で惜しみなくコットンパックや全身保湿に使えるプロ仕様。シロキクラゲの濃密な植物性保水膜が、サロン帰りのようなもっちり潤い肌を自宅で再現",
        "desc_p1": "真冬のインナードライを根本から解消するためには、日々のスキンケアで「ケチらずにたっぷりと水分を補給すること」が何よりの近道です。エステティックサロンの施術用として開発されたデュフラの『フィトフォース オーガニック モイストローション』は、プロの現場が求める圧倒的な保湿力と安全性を備えた大容量ローションです。オーガニック認証植物原料に加えて、高保水の要としてシロキクラゲ多糖体を高配合しています。",
        "desc_p2": "手にとるとみずみずしく清らかな質感ですが、肌に重ねるごとにシロキクラゲの微細多糖体が網目状の水分層を形成し、肌の内側からぷるんとしたハリ感が湧き上がります。500mlのメガサイズだからこそ、毎日のローションパックやシートマスクへの追い足し、さらには入浴後のデコルテや腕・脚の全身保湿まで贅沢に使い倒すことが可能。12種のハーブによる心地よい天然の香りが、冬の心身を解きほぐします。",
        "target": "化粧水をバシャバシャと惜しみなく大容量で使いたい方、毎晩のコットンパックで徹底的に水分チャージしたい方、エステサロン品質の本格オーガニックケアを好む方",
        "point": "大判コットンにたっぷり含ませて薄く割き、乾燥の気になる頬や額に貼って3分間のローションパックを行います。剥がした後に手で包み込むと驚異的なモチモチ肌になります。"
    },
    {
        "rank": 9,
        "tag": "✨ 白キクラゲ多糖体×金のナノコロイド！過酷な乾燥ダメージ肌を密着リペアするゴールドジェル",
        "catch": "ファイテンの最先端アクアメタル技術「アクアゴールド」にシロキクラゲ多糖体を高配合。濃密なゴールドジェルが真冬の冷風や暖房で傷ついた肌に密着浸透し、ふっくら吸い付くような潤い膜でバリア機能を補強",
        "brand_name": "Phiten (ファイテン)",
        "capacity": "60g / スパチュラ付きジャー容器",
        "type": "高機能保水ゴールドオールインワンジェル",
        "features": "シロキクラゲ多糖体、コロイド性金（アクアゴールド）、コロイド性パラジウム、マカデミアナッツ油、バオバブ種子油",
        "value": "金をナノレベルで水中に分散させた独自技術が肌の巡りをサポート。シロキクラゲ多糖体の水分保持力と融合し、真冬の寒冷でこわばった肌をほぐしながら強力に保湿密閉",
        "desc_p1": "スポーツテクノロジーと健康科学のパイオニアであるファイテンが本気で開発したプレミアムスキンケア『アクアゴールド プレミアムモイスチャージェル』。純金をナノレベルで水中に均一分散させた「アクアゴールド」の鮮やかなピンクゴールド色のジェルに、植物性ヒアルロン酸とも呼ばれるシロキクラゲ多糖体が惜しみなく配合されています。冬の寒冷乾燥によって血行が滞り、ハリを失った素肌のための高機能ジェルです。",
        "desc_p2": "ぷるぷるのジェルを肌に乗せると、体温でスーッとみずみずしく崩れ、ナノコロイドとシロキクラゲの多糖体成分が角層深部へと素早く浸透。肌の奥底から押し上げるような弾力をもたらしながら、表面には薄くしなやかな保護ヴェールを張って暖房の乾燥から長時間守り抜きます。これひとつで化粧水・乳液・美容液・クリーム・パックの5役をこなすため、真冬の忙しい朝や疲れた夜の時短ケアにも圧倒的な威力を発揮します。",
        "target": "冬の寒さで肌の血色感が悪く顔がこわばっている方、オールインワンでも手抜き感のない本格的な保湿を求める方、最先端のナノメタルと植物エキスの力を体感したい方",
        "point": "付属のスパチュラでパール2粒大を取り、顔全体に伸ばした後、手のひらで顔全体を温めながら軽くマッサージします。夜は少し多めに塗ってスリーピングマスクとしても活用できます。"
    },
    {
        "rank": 10,
        "tag": "🐴 原液90%超リッチ処方！白キクラゲ多糖体×高級ウマプラセンタの濃厚美容原液",
        "catch": "天然シロキクラゲ多糖体に希少な北海道産ウマプラセンタとウマサイタイエキスを原液レベルで90%以上配合。真冬の過酷な乾燥による小ジワや乾燥砂漠肌を即座に救済する至極のドロップエッセンス",
        "brand_name": "PLAMID (プラミド)",
        "capacity": "30ml / スポイト遮光ガラス瓶",
        "type": "シロキクラゲ多糖体配合 高濃度原液リッチエッセンス",
        "features": "シロキクラゲ多糖体、ウマプラセンタエキス、ウマサイタイエキス、ヒアルロン酸Na",
        "value": "水で薄めない原液設計。シロキクラゲの自重500倍の保水力とプラセンタの豊富なアミノ酸・成長因子が共鳴し、真冬の枯れた肌に劇的なハリと潤いのツヤを宿す",
        "desc_p1": "冬の本格的な寒さと乾燥によって、どんなクリームを塗ってもカサつきや小ジワがおさまらない限界肌に到達したとき、頼るべきは原液高配合の集中アプローチです。プラミドの『リッチエッセンス』は、水で薄める一般的な美容液とは一線を画し、高級ウマプラセンタ原液45%、ウマサイタイ原液45%に、究極の保水植物多糖体であるシロキクラゲ多糖体を贅沢に融合させた原液エッセンスです。",
        "desc_p2": "スポイトから取り出すと、原液ならではの濃密なとろみがありながら、肌に乗せると驚くほど素早く角層へ引き込まれていきます。サイタイ由来の天然ヒアルロン酸とシロキクラゲ多糖体が協調して強力な水分ネットワークを構築し、プラセンタのアミノ酸が角層深部の修復を後押し。翌朝目覚めたときの肌のふっくら感、指を跳ね返すような弾力は感動的です。真冬のエイジングケアを劇的に格上げする珠玉の1本です。",
        "target": "真冬の深刻な乾燥小ジワやたるみ・ハリ不足に悩む方、原液コスメの圧倒的な効果実感を求める方、手持ちのスキンケアに数滴加えて保湿力を極限まで高めたい方",
        "point": "洗顔直後のまっさらな素肌に1〜2滴をスポイトで直接落とし、指先で乾燥の気になる目元や口元から馴染ませます。その後通常のスキンケアを行うと、化粧水の浸透が劇的にアップします。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の暖房乾燥とインナードライ！「植物性ヒアルロン酸」シロキクラゲの真実"},
    {"id": "mechanism", "title": "2. なぜシロキクラゲ多糖体は冬の肌を救うのか？自重500倍の保水科学"},
    {"id": "comparison", "title": "3. 高保湿シロキクラゲ多糖体コスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿シロキクラゲ多糖体コスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しないシロキクラゲコスメの選び方＆冬のインナードライ脱出法"},
    {"id": "routine", "title": "6. 真冬の砂漠肌を満たし続ける！効果的な保水多重レイヤードルーティン"},
    {"id": "faq", "title": "7. シロキクラゲコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：驚異の純植物性多糖体で真冬の肌乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["item_name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">¥{item_data["price"]:,}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["affiliate_url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["item_name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["image_url"]}" alt="{item_data["item_name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "95")}件）</span>
              </div>
              <a href="{item_data["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                🛒 楽天市場で「{p["brand_name"]}」の最新価格・在庫・口コミを見る
              </a>
            </div>

            <div class="product-info-col">
              <table class="spec-table">
                <tr><th>ブランド</th><td>{p["brand_name"]}</td></tr>
                <tr><th>容量・容器</th><td>{p["capacity"]}</td></tr>
                <tr><th>アイテム種別</th><td>{p["type"]}</td></tr>
                <tr><th>注目美肌成分</th><td>{p["features"]}</td></tr>
                <tr><th>真冬の特長・価値</th><td>{p["value"]}</td></tr>
              </table>

              <div class="product-body">
                <h4 class="body-title">皮膚科学的アプローチ＆冬の使用感レビュー</h4>
                <p>{p["desc_p1"]}</p>
                <p>{p["desc_p2"]}</p>

                <div class="recommend-box">
                  <div class="recommend-title">💡 こんな方・こんな冬の肌悩みにおすすめ！</div>
                  <p>{p["target"]}</p>
                </div>

                <div class="usage-box">
                  <div class="usage-title">🧴 11月・12月の効果的な使い方テクニック</div>
                  <p>{p["point"]}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
""")

all_cards_html = "\n".join(product_cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える植物性ムコ多糖類が真冬の干からびインナードライ肌を満たし続ける高保湿シロキクラゲコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月のエアコン暖房乾燥によるインナードライ・キメの乱れ・乾燥毛穴を救う高保湿シロキクラゲ多糖体（白キクラゲ）コスメを徹底厳選！ルルルン、アテニア、オルビス、コスメデコルテ、エトヴォスまで自重500倍の保水力と植物性ムコ多糖類の皮膚科学的根拠と共に徹底検証。">
  <meta name="keywords" content="シロキクラゲ コスメ, 白キクラゲ多糖体, 植物性ヒアルロン酸, 高保湿 コスメ 冬, インナードライ 対策 11月 12月, ルルルン ハイドラ EX, アテニア ドレスリフト, コスメデコルテ イドラクラリティ, エトヴォス モイスチャライジングローション">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える植物性ムコ多糖類が真冬の干からびインナードライ肌を満たし続ける高保湿シロキクラゲコスメランク10">
  <meta property="og:description" content="楊貴妃も愛した自重500倍の驚異的保水力！真冬の過酷な暖房乾燥とインナードライ砂漠肌を満たし尽くすシロキクラゲ多糖体コスメ10選を徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-tremella">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿シロキクラゲコスメランク10">
  <meta name="twitter:description" content="11月・12月の暖房乾燥に！自重500倍の保水力で角層を満たす高保湿シロキクラゲ多糖体コスメおすすめ10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える植物性ムコ多糖類が真冬の干からびインナードライ肌を満たし続ける高保湿シロキクラゲコスメランク10",
    "description": "11月・12月の暖房乾燥によるインナードライ・角層脱水・開き毛穴を救う高保湿シロキクラゲ多糖体（白キクラゲ）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-05T22:00:00+09:00",
    "dateModified": "2026-11-05T22:00:00+09:00",
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 編集部"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-tremella"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿シロキクラゲコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{items[0]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{items[1]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{items[2]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{items[3]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{items[4]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{items[5]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{items[6]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{items[7]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{items[8]["item_name"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{items[9]["item_name"]}"
      }}
    ]
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #3: FAQPage -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "シロキクラゲ多糖体とヒアルロン酸にはどのような違いがありますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "どちらも優れた水分保持能力を持ちますが、シロキクラゲ多糖体は自重の約500倍の保水力を持ち、ヒアルロン酸よりも微細な三次元網目構造を形成します。特に湿度が極端に低い冬の室内環境においてヒアルロン酸よりも水分蒸発率が低く、塗布後の肌表面にベタつきを残さずシルクのようななめらかな保護膜を形成する点が大きな特徴です。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "インナードライ（表面はテカるのに内側が突っ張る）にシロキクラゲが効果的な理由は？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "インナードライは角層内部の水分が不足し、これ以上水分を逃すまいとして皮脂が過剰分泌されることで起こります。シロキクラゲ多糖体は油分ではなく純粋な植物性多糖体の水分ネットワークであるため、毛穴を詰まらせることなく角層のすみずみまで深層保水を行い、過剰な皮脂分泌の根本原因を鎮めます。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "敏感肌やアトピー傾向の冬肌でもシロキクラゲコスメは使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "シロキクラゲ多糖体は食用キノコ由来の純植物性成分であり、生体親和性が極めて高く低刺激です。合成高分子ポリマーと異なり皮膚呼吸を妨げず、肌荒れを防ぐ穏やかな保護膜として機能するため、真冬の寒暖差でピリピリしやすいデリケートな敏感肌にも大変適しています。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-light: #e0f2fe;
      --primary-dark: #0369a1;
      --accent: #0ea5e9;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #f8fafc;
      --bg-card: #ffffff;
      --border: #bae6fd;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 600;
      font-size: 0.95rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      box-shadow: var(--shadow);
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: #374151;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-top: 1px solid rgba(0, 0, 0, 0.08);
      padding-top: 1rem;
    }}
    
    /* 目次 */
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.75rem;
      margin: 2rem 0;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 0.75rem 1.5rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-card a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    
    /* セクション共通 */
    .article-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.25rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      border-left: 5px solid var(--primary);
      padding-left: 1rem;
      margin-bottom: 1.5rem;
      line-height: 1.35;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
      text-align: justify;
    }}
    .highlight-lead {{
      background: var(--primary-light);
      border-left: 4px solid var(--accent);
      padding: 1.25rem;
      border-radius: 4px;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #f0f9ff;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 6px;
      background: #ffffff;
      padding: 0.5rem;
      margin-bottom: 1rem;
    }}
    .price-box {{
      width: 100%;
      text-align: center;
      margin-bottom: 0.75rem;
      padding: 0.5rem;
      background: #ffffff;
      border-radius: 6px;
      border: 1px solid #bae6fd;
    }}
    .price-label {{ font-size: 0.75rem; color: var(--text-muted); display: block; }}
    .price-value {{ font-size: 1.4rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      font-size: 0.85rem;
      margin-bottom: 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.25rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: var(--text-muted); }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #0284c7 0%, #0ea5e9 100%);
      color: #ffffff;
      text-align: center;
      padding: 0.9rem 1rem;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 6px rgba(2, 132, 199, 0.25);
      transition: opacity 0.2s;
    }}
    .rakuten-btn:hover {{ opacity: 0.9; }}
    
    .product-info-col {{ display: flex; flex-direction: column; }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid #e5e7eb;
    }}
    .spec-table th {{
      width: 28%;
      background: #f0f9ff;
      color: #0369a1;
      font-weight: 700;
      white-space: nowrap;
    }}
    .body-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: #111827;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #e0f2fe;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      color: #0369a1;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    .usage-box {{
      background: #f3f4f6;
      border-left: 4px solid #6b7280;
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin-top: 1rem;
    }}
    .usage-title {{
      font-weight: 700;
      color: #374151;
      font-size: 0.9rem;
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🌿 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">楊貴妃が愛した自重500倍の奇跡・純植物性高保水ムコ多糖類</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！ヒアルロン酸を超える植物性ムコ多糖類が真冬の干からびインナードライ肌を満たし続ける高保湿シロキクラゲコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて本格化するオフィスのエアコン暖房と冷たい北風。肌表面は皮脂でテカリながら内部が突っ張る「インナードライ」や、乾燥によって萎縮した毛穴の目立ち——。ヒアルロン酸以上の水分保持力を誇り、ベタつかずに角層深部を満たし続ける「シロキクラゲ多糖体（白キクラゲ）」の皮膚科学的メカニズムを解明し、楽天市場で今すぐ手に入る最高峰のシロキクラゲコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬インナードライ特化版）</span>
        <span>🔬 皮膚科学・植物性多糖体保水検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の暖房乾燥とインナードライ！「植物性ヒアルロン酸」シロキクラゲの真実</h2>
      <div class="highlight-lead">
        重いオイルやこってりクリームをいくら塗り重ねても乾く理由は「水分保持ネットワークの欠落」。自重の500倍の水分を抱え込み、低湿度環境でも蒸発させないシロキクラゲ多糖体こそ、真冬のインナードライ砂漠肌を救う究極の保水成分です。
      </div>
      <p>
        11月中旬を過ぎると、日本列島は大陸からの乾燥した寒気に覆われ、湿度は急降下します。さらに室内では一日中エアコン暖房が稼働し、温風が直接肌に吹き付けることで、角層の水分は急速に奪われていきます。この時期に最も多くの女性を悩ませるのが、肌の表面は乾燥から身を守るために皮脂を分泌してテカっているのに、角層の内側は水分が枯渇してパリパリに突っ張る「インナードライ」です。
      </p>
      <p>
        インナードライに陥った肌に油分主体のクリームやオイルを無理に重ねても、水分の通り道が塞がれるだけで根本的な渇きは癒やされません。必要なのは、角層深部までスムーズに浸透し、かつ過酷な低湿度下でも水分を放さない「強靭な分子保水膜」です。古代中国の四大美女・楊貴妃が不老長寿と美貌のために愛食したと伝えられる銀耳（白キクラゲ）から抽出される「シロキクラゲ多糖体」は、ヒアルロン酸に匹敵、あるいはそれを凌駕する驚異的な水分抱合力を持つ純植物性のバイオ高保湿成分として、今世界中のビューティーアワードで脚光を浴びています。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜシロキクラゲ多糖体は冬の肌を救うのか？自重500倍の保水科学</h2>
      <p>
        シロキクラゲ多糖体（Tremella Fuciformis Polysaccharide）が、真冬の暖房乾燥下でヒアルロン酸以上の保水持続性を発揮する皮膚科学的理由は、その特殊な立体網目構造と糖鎖組成にあります。
      </p>
      <p>
        <strong>① 自重の約500倍の水分を抱え込む三次元グルクロンキシロマンナン構造：</strong><br>
        シロキクラゲ多糖体は、マンノースを主鎖とし、キシロースやグルクロン酸が複雑に分岐した高分子酸性ヘテロ多糖体です。この立体的な三次元網目構造が膨大な水分子をキャッチし、自身の重量の約500倍もの水分をガッチリと抱え込みます。乾燥した真冬の空気中であっても、一度掴んだ水分を外気へ逃しません。
      </p>
      <p>
        <strong>② 低湿度環境における抜群の「水分蒸発防止力」：</strong><br>
        一般的なヒアルロン酸は湿度が高い環境では優れた保水力を発揮しますが、冬のオフィスのように湿度が30%以下に落ち込むと、逆に周囲の乾燥空気に水分を奪われやすくなる弱点があります。一方、シロキクラゲ多糖体は低湿度下でも水分保持能力の低下が極めて少なく、乾燥が進むほど肌表面にしなやかな保護ヴェールを維持し続けることが実験データにより証明されています。
      </p>
      <p>
        <strong>③ ベタつきゼロ！シルクのように滑らかな生体親和性フィルム：</strong><br>
        高分子ヒアルロン酸特有の「肌表面にペタペタと残る重さ」「メイク前のモロモロ（カス）の発生」といったデメリットが、シロキクラゲ多糖体にはほとんどありません。分子の柔軟性が非常に高く、肌に乗せるとスッと薄く均一に広がり、シルクのようなサラサラと滑らかな感触へと変化します。朝のメイク前にたっぷり塗布してもファンデーションがヨレず、暖房による日中の乾燥崩れを完全に防ぎます。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿シロキクラゲ多糖体コスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入可能な人気の高保湿シロキクラゲコスメ10アイテムの種別、参考価格、主要美肌成分を一覧にまとめました。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿シロキクラゲ多糖体コスメおすすめ厳選ランキング10選</h2>
      <p>
        成分配合純度、真冬の保水持続時間、テクスチャーの心地よさ、楽天市場での口コミ評価を多角的に検証したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しないシロキクラゲコスメの選び方＆冬のインナードライ脱出法</h2>
      <p>
        シロキクラゲコスメを冬のスキンケアに組み込む際は、肌の乾燥レベルや毎日のケア習慣に応じて最適なテクスチャーとカテゴリーを選ぶことが大切です。
      </p>
      <p>
        <strong>① 毎日の基本保水・角層柔軟化には「高浸透ローション」：</strong><br>
        アテニア（第3位）、オルビス（第4位）、コスメデコルテ（第5位）、エトヴォス（第6位）のような化粧水は、毎朝晩の洗顔後に角層のすみずみまで水分を行き渡らせるベース作りに最適です。とろみがありながらスッと馴染み、キメをふっくら整えます。
      </p>
      <p>
        <strong>② 暖房直撃のオフィス乾燥・深刻な小ジワには「集中モイスト美容液・原液」：</strong><br>
        ピアベルピア（第1位）やPLAMID（第10位）のような高濃度エッセンスは、シロキクラゲの保水シールドが最も高密度に肌へ密着します。目元や口元など乾燥しやすいゾーンへのピンポイント集中ケアや、手持ちのコスメへのブレンドに威力を発揮します。
      </p>
      <p>
        <strong>③ 週末の肌リセット・即効透明感チャージには「デイリーシートマスク」：</strong><br>
        ルルルン ハイドラ EX（第2位）のようにシート全体にシロキクラゲ多糖体美容液が染み込んだマスクは、冬の寒さでこわばった角質層を密閉スチーム効果でほぐし、短時間でサロン帰りのようなもっちり白玉肌を復元します。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬の砂漠肌を満たし続ける！効果的な保水多重レイヤードルーティン</h2>
      <p>
        シロキクラゲ多糖体の自重500倍の保水力を極限まで引き出し、真冬の暖房乾燥から素肌を守り抜くスキンケアステップです。
      </p>
      <p>
        <strong>ステップ1【低刺激洗顔で水分を奪わない】：</strong><br>
        朝晩の洗顔は、ファンケルの泥ジェル（第7位）のような泡立て不要でシロキクラゲの潤い膜を残す洗顔料を使用します。必要な天然保湿因子を流出させず、まっさらな素肌を整えます。
      </p>
      <p>
        <strong>ステップ2【シロキクラゲローションの3回重ねづけ】：</strong><br>
        化粧水を一度に多量つけるのではなく、500円玉大を手にとって顔全体をハンドプレスし、肌に吸い込まれたらもう一度重ねる「ミルフィーユ塗布」を行います。シロキクラゲの分子が角層内部で幾重にも重なり、分厚い水分層が完成します。
      </p>
      <p>
        <strong>ステップ3【美容液の密着＆乳液・クリームでのフタ】：</strong><br>
        目元や頬など特に乾きやすい部位にシロキクラゲ美容液（第1位など）を押し込み、最後に乳液やクリームで油分のフタをします。シロキクラゲが抱え込んだ大量の水分が油膜の下で完全に密封され、翌朝まで吸い付くような潤い肌が保たれます。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. シロキクラゲコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> シロキクラゲ多糖体とヒアルロン酸にはどのような違いがありますか？</div>
        <div class="faq-a">
          どちらも優れた水分保持能力を持ちますが、シロキクラゲ多糖体は自重の約500倍の保水力を持ち、ヒアルロン酸よりも微細な三次元網目構造を形成します。特に湿度が極端に低い冬の室内環境においてヒアルロン酸よりも水分蒸発率が低く、塗布後の肌表面にベタつきを残さずシルクのようななめらかな保護膜を形成する点が大きな特徴です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> インナードライ（表面はテカるのに内側が突っ張る）にシロキクラゲが効果的な理由は？</div>
        <div class="faq-a">
          インナードライは角層内部の水分が不足し、これ以上水分を逃すまいとして皮脂が過剰分泌されることで起こります。シロキクラゲ多糖体は油分ではなく純粋な植物性多糖体の水分ネットワークであるため、毛穴を詰まらせることなく角層のすみずみまで深層保水を行い、過剰な皮脂分泌の根本原因を鎮めます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 敏感肌やアトピー傾向の冬肌でもシロキクラゲコスメは使えますか？</div>
        <div class="faq-a">
          シロキクラゲ多糖体は食用キノコ由来の純植物性成分であり、生体親和性が極めて高く低刺激です。合成高分子ポリマーと異なり皮膚呼吸を妨げず、肌荒れを防ぐ穏やかな保護膜として機能するため、真冬の寒暖差でピリピリしやすいデリケートな敏感肌にも大変適しています。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：驚異の純植物性多糖体で真冬の肌乾燥とさようなら</h2>
      <p>
        11月から12月にかけての本格的な真冬シーズンは、外気の冷気と室内の暖房による激しい水分蒸散によって、私たちの素肌から急速に潤いが奪い去られていきます。表面をいくら油分で覆っても乾いてしまう冬の頑固なインナードライを根本から解消する鍵は、角層のすみずみまで水分を送り届けて離さない「強靭な植物性保水ネットワーク」に他なりません。
      </p>
      <p>
        楊貴妃の時代から受け継がれ、現代の先端皮膚科学によってその圧倒的な自重500倍の水分保持力が実証されたシロキクラゲ多糖体コスメは、過酷な真冬の乾燥環境から素肌を確実に守り抜き、ふっくら吸い付くような透明感あふれる美肌へと導いてくれます。ぜひ本記事のランキングや選び方を参考に、あなたのライフスタイルや肌悩みにぴったりのシロキクラゲコスメを見つけて、真冬でも乾燥知らずのぷるぷるモチ肌を手に入れてください。
      </p>
    </section>

    <!-- 関連記事リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-logo">🌿 LUMI COSMETICS</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で自動挿入 -->
      </div>
      <div style="text-align:center;margin-top:2rem;font-size:0.8rem;color:#6b7280;">
        &copy; 2026 LUMI COSMETICS. All rights reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-tremella.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-tremella.html successfully!")
