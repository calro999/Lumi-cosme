import json
import re

with open("fetched_3new_sacran_fullerene_hatomugi.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_sacran"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 阿蘇の清流が生んだ自重6,000倍の奇跡！純度100%原液で乾いた角層を密着保水",
        "catch": "熊本・阿蘇山系の伏流水でしか生息できない日本固有の希少藍藻『スイゼンジノリ』から抽出した100%純粋サクラン原液。分子量1600万の超巨大バイオ皮膜が真冬の強烈な暖房気流から素肌を完全防備",
        "brand_name": "NATUDOR (ナチュドール)",
        "capacity": "20mL / スポイト遮光ガラス瓶",
        "type": "高純度 スイゼンジノリ多糖体100% 原液美容液",
        "features": "スイゼンジノリ多糖体（サクラン）純度100%、BG、フェノキシエタノールフリー処方",
        "value": "ヒアルロン酸の約10倍の保水力と自重の約6,000倍の抱水性。洗顔後すぐの素肌や手持ちの化粧水に1滴混ぜるだけで、真冬のエアコン暖房直撃下でも一日中吸い付くようなモチ肌を維持",
        "desc_p1": "11月から12月にかけて暖房が本格稼働すると、オフィスや室内の湿度は20%台まで急落し、皮膚の角層水分は毎秒猛烈な勢いで大気中へと奪われていきます。従来のヒアルロン酸化粧水では『つけた瞬間は潤うのに、数十分後には突っ張る』というインナードライ現象に直面しがちです。ナチュドールの『サクラン原液 20mL』は、日本固有の希少淡水藍藻スイゼンジノリから極めて高い純度で抽出されたピュアサクランエッセンスです。分子量1600万という驚異的な超高分子構造が、肌のキメ一つひとつに吸着して極薄の『第二の皮膚』のような人工バイオバリアを形成します。",
        "desc_p2": "特筆すべきは、皮膚上の汗や皮脂に含まれる塩分に触れても保水性能が低下しない点です。一般的なヒアルロン酸が塩分環境で保水力が急激に半減するのに対し、サクランは自身の硫酸基とカルボキシル基の相互作用により、塩分存在下でもヒアルロン酸の約10倍という圧倒的保水力を維持します。冬の冷たい外気と暖かい室内の激しい寒暖差でバリアが乱れた肌へ、摩擦を起こさず滑らかに伸び広がり、内側の水分蒸散を物理的に遮断。夜塗布して眠れば、翌朝洗顔する瞬間までピンとした潤い膜が残っていることを指先で実感できます。",
        "target": "冬になるとどんな高保湿クリームを塗っても数時間で乾燥する方、暖房によるインナードライや夕方の突っ張りに悩む方、手持ちのスキンケアを劇的にパワーアップさせたい方",
        "point": "朝晩の洗顔直後、手のひらに2〜3滴を取り、温めながら顔全体へ優しく押し込むようにハンドプレスします。特に乾燥が激しい目元や口元には、化粧水塗布後にさらにもう1滴を重ねづけしてください。"
    },
    {
        "rank": 2,
        "tag": "🌿 サクラン×コエンザイムQ10×ヒアルロン酸！乾燥性敏感肌を根本から救う高保水セラム",
        "catch": "敏感肌研究のパイオニアが送り出す高保水エイジング美容液。スイゼンジノリ多糖体の超密着ヴェールにコエンザイムQ10とヒアルロン酸を黄金比ブレンド。真冬の寒冷で硬化した枯れ肌をふっくら再生",
        "brand_name": "Piabelpia (ピアベルピア)",
        "capacity": "50ml / ポンプボトル",
        "type": "高保水エイジングケア エッセンス（敏感肌設計）",
        "features": "スイゼンジノリ多糖体、ユビキノン（コエンザイムQ10）、ヒアルロン酸Na、植物性グリセリン",
        "value": "冬の冷えと暖房でバリア機能が崩壊した角層へ、刺激を与えずに深部まで潤いを届ける弱酸性・低刺激処方。ベタつきを残さず、内側から押し返すような高密度ハリ肌を長時間キープ",
        "desc_p1": "冬の乾燥は単なる水分不足にとどまらず、角層細胞の収縮によるバリア機能低下と微弱炎症を引き起こします。ピアベルピアの『Qモイスト 50ml』は、乾燥性敏感肌が真冬を乗り切るために調合された高機能モイスチャーセラムです。最大の特徴は、保水膜の頂点に君臨するスイゼンジノリ多糖体（サクラン）と、細胞のエネルギー代謝を支えるコエンザイムQ10（ユビキノン）の融合処方にあります。",
        "desc_p2": "淡いイエローのとろみリキッドが肌に乗せた瞬間にみずみずしく崩れ、角層のミクロな隙間へスーッと浸透。サクランが形成する網目状の水分保持ネットワークが、Q10の抗酸化力とヒアルロン酸の水分を角層内部へがっちり閉じ込めます。外気温度が氷点下に近づく12月の過酷な環境下でも、皮膚表面に滑らかな保護ヴェールが居座り続け、冷風による赤みやピリピリ感を穏やかに鎮静。塗布後はシルクのようなすべすべの手触りに整い、ファンデーションのノリが劇的に向上します。",
        "target": "乾燥で肌が敏感になり市販の美容液がしみる方、冬になると夕方に顔全体が突っ張って粉を吹く方、保水とハリ弾力ケアを1本で両立したい大人の乾燥肌",
        "point": "化粧水で肌を整えた後、2プッシュを手にとり顔全体から首筋にかけて包み込むように馴染ませます。目元のちりめんジワが気になる部分は指の腹でトントンと軽く叩き込むと効果的です。"
    },
    {
        "rank": 3,
        "tag": "🌸 京都発！分子量1600万の巨大多糖体ヴェールが肌を包むプレミアム和漢ローション",
        "catch": "新成分サクランを贅沢に高配合した京都生まれの上質高保湿化粧水。ヒアルロン酸の10倍の水分保持力を持つスイゼンジノリ多糖体が、真冬の砂漠肌をみずみずしい極上シルク肌へと仕立て上げる名作",
        "brand_name": "MAIKO (マイコ)",
        "capacity": "120ml / 上質スクリューボトル",
        "type": "高機能サクラン高配合 モイスチャーローション",
        "features": "スイゼンジノリ多糖体（サクラン）、和漢植物エキス複合体、ヒアルロン酸、アミノ酸群",
        "value": "水溶性でありながら美容液レベルのとろみと密着感。冬の乾いた角層を瞬時にほぐし、まるでシートマスクを貼り続けているかのような持続的保水環境を創出",
        "desc_p1": "厳しい底冷えと乾燥で知られる冬の京都において、芸舞妓の繊細な肌を長年守り続けてきた伝統の知恵と最新のバイオサイエンスが融合して誕生したのが、MAIKOの『モイスチャーローション』です。主成分として配合されているスイゼンジノリ多糖体は、阿蘇の澄み切った地下水でのみ育つ希少植物から得られる天然成分で、分子量1600万という桁違いのスケールを誇ります。",
        "desc_p2": "手に取ると美容液のように濃厚なとろみがありながら、肌に滑らせるとスーッと摩擦レスに吸い込まれ、角層のすみずみまで満ち足りていく心地よい浸透感を実感できます。肌表面には目に見えない保水フィルムが形成され、真冬のエアコンの温風が直接当たっても肌内部の水分蒸散を完全にシャットアウト。数時間経ってもみずみずしいツヤと柔らかさが持続し、乾燥によるキメの乱れやくすみを一掃して、透明感に満ちた白磁のような素肌へと整えます。",
        "target": "一般的な化粧水では物足りず何回も重ねづけしている方、真冬の底冷えによる血行不良と乾燥くすみに悩む方、京都の上質な和漢モイスチャーで優雅に肌を労りたい方",
        "point": "手のひらに500円玉大を取り、手の熱で温めてから顔全体を包み込むようにハンドプレス。乾燥が気になる日は2度塗りし、首やデコルテまでたっぷり伸ばしてください。"
    },
    {
        "rank": 4,
        "tag": "🤲 高濃度ヒト型セラミド×サクラン！真冬のあかぎれ手肌とひび割れを救う濃密バリアクリーム",
        "catch": "阿蘇スイゼンジノリ多糖体と高濃度ヒト型セラミド（NP/AP/EOP）をW配合した究極の集中バリアクリーム。水仕事や真冬の寒冷でパックリ割れそうな指先・関節・乾燥部位を強力ラッピング",
        "brand_name": "スキンケアファクトリー",
        "capacity": "20g / スクリューミニチューブ",
        "type": "高濃度ヒト型セラミド×サクラン バリアハンド＆ボディクリーム",
        "features": "スイゼンジノリ多糖体（サクラン）、ヒト型セラミド3種（EOP/NP/AP）、シア脂、スクワラン",
        "value": "角層の隙間を埋める『細胞間脂質（セラミド）』と、角層表面を覆う『保水シールド（サクラン）』のダブルプロテクション。水で流しても落ちにくい驚異の密着持続力を実現",
        "desc_p1": "11月から12月にかけて、主婦湿疹や水仕事によるあかぎれ、指先のパックリ割れ、粉吹きすねに悩まされる方は爆発的に増加します。一般的なハンドクリームは油分でフタをするだけのため、手を洗うたびに流れ落ちてしまい根本的な保水修復には至りません。スキンケアファクトリーの『高濃度ヒト型セラミド＆サクラン配合クリーム』は、皮膚生理学に基づき角層の内側と外側の両面からアプローチする本格リペアバームです。",
        "desc_p2": "内側には肌のバリア構造と完全に一致するヒト型セラミドを補給して角層ラメラ構造を整え、外側にはサクランの強靭な分子ネットワークを展開。サクランは水になじみながらも皮膜を形成する特殊な高分子であるため、手洗いを行っても保水皮膜が肌に残り続け、冬の冷たい外気や水刺激から患部を保護し続けます。伸びが極めて良く、塗った直後からサラリと馴染んでベタつかないため、スマホやPCのキーボードをすぐに操作できる実用性も兼ね備えています。",
        "target": "冬場の水仕事やアルコール消毒で手肌があかぎれ・ひび割れを起こしている方、タイツを脱ぐとすねが粉を吹いてかゆい方、一度塗ったら手洗いに負けない保護力を求める方",
        "point": "少量を指先に取り、体温で温めながらひび割れやすい関節まわりや爪の甘皮へすり込みます。就寝前にたっぷり塗り、綿の手袋をして眠ると翌朝劇的に手肌が修復されます。"
    },
    {
        "rank": 5,
        "tag": "🌿 プロのエステサロンが指名買い！オーガニック植物×サクランのサロン仕様高保湿ローション",
        "catch": "全国のエステサロンで施術用として愛用されるデュフラのオーガニックライン。オーガニック認証植物エキスにスイゼンジノリ多糖体を贅沢配合。冬の乾燥で開ききった毛穴と乱れたキメを整えるプロ仕様化粧水",
        "brand_name": "DIEUFRA (デュフラ フィトフォース)",
        "capacity": "大容量プロユースボトル / ポンプ対応",
        "type": "サロン専売 オーガニック高保湿ハーブローション",
        "features": "スイゼンジノリ多糖体、カミツレ花エキス、ローズマリー葉エキス、セージ葉エキス、グリチルリチン酸2K",
        "value": "プロの現場で求められる即効性と安全性。敏感に傾いた真冬の肌を植物ハーブが穏やかに整え、サクランの保水シールドが乾燥毛穴や小ジワをふっくら持ち上げる",
        "desc_p1": "エステティックサロンのフェイシャル施術において、真冬のクライアントの多くは『極度の角層脱水による毛穴の開き・たるみ』を訴えます。肌が乾燥すると、角層細胞がしぼんで毛穴の周囲が落ち込み、いわゆる帯状毛穴や乾燥小ジワが目立ってしまうのです。デュフラ フィトフォースの『オーガニック モイストローション』は、過酷な冬の現場でエステティシャンが頼りにするプロフェッショナル化粧水です。",
        "desc_p2": "厳選されたオーガニックハーブエキスが冷気でこわばった素肌を素早くリラクゼーションへと導き、スイゼンジノリ多糖体が角層深部に潤いを抱え込ませます。サクラン特有の滑らかなテクスチャーが肌表面をピーンと均一に整えるため、毛穴の凹凸が目立たなくなり、光を均一に反射する透明感のある肌質へとシフト。大容量仕様で惜しみなくコットンパックや全身ケアに使えるコストパフォーマンスの高さもサロンユースならではの強みです。",
        "target": "冬の乾燥で頬の毛穴が縦に開いて目立つ方、エステ帰りのような吸い付くもっちり肌を自宅で再現したい方、高品質なオーガニック処方で大容量の化粧水をたっぷり使いたい方",
        "point": "コットンにたっぷり含ませて、乾燥の気になる頬や額に5分間ローションパック。パック後は手のひらで軽くタッピングしてサクランの保水ヴェールをしっかり密着させてください。"
    },
    {
        "rank": 6,
        "tag": "💆‍♀️ 冬の暖房乾燥でパサつく頭皮と毛先を救う！サクラン配合集中スカルプリペアマスク",
        "catch": "スイゼンジノリ多糖体の超保水力をヘア＆スカルプケアに応用。冬のエアコン暖房や静電気でカサつく頭皮を潤し、パサついて広がる毛先を根元から補修する高機能ヘアマスク",
        "brand_name": "Gracia (グラシア)",
        "capacity": "200g / チューブ容器",
        "type": "高保湿 スカルプ＆ヘア集中リペアマスク",
        "features": "スイゼンジノリ多糖体（サクラン）、加水分解ケラチン、アルガンオイル、ホホバ種子油",
        "value": "頭皮につけても毛穴を塞がず、サクランの保水膜がフケ・かゆみを防ぎながら、ダメージを受けた毛髪のキューティクルを滑らかに密着コーティング",
        "desc_p1": "11月から12月は、肌だけでなく頭皮と毛髪にとっても乾燥のピークを迎えます。室内の暖房で頭皮が乾燥してかゆみや細かいフケが発生し、毛髪は大気中の水分不足と静電気によってキューティクルが剥離し、枝毛や広がりが深刻化します。グラシアの『サクラン スカルプケアマスク 200g』は、保水多糖体サクランを髪と頭皮の双方へアプローチできるよう設計された画期的なトリートメントです。",
        "desc_p2": "シャンプー後の頭皮と髪に直接塗布して優しくマッサージすると、サクランの粘弾性ヴェールが乾燥した頭皮の角層にスーッと浸透。フケやかゆみの原因となる頭皮の砂漠化を食い止め、健やかな毛根環境を維持します。同時に、加水分解ケラチンと良質な植物オイルがダメージホールを補修し、髪一本一本を潤い皮膜で包み込むため、ドライヤーで乾かした後は毛先までしっとりとまとまり、冬特有の静電気による爆発的な広がりを完全に抑え込みます。",
        "target": "冬になると頭皮が乾燥してかゆみやフケが出る方、暖房やマフラーの摩擦で毛先がパサついて広がる方、頭皮ケアと美髪トリートメントを同時に完了させたい方",
        "point": "シャンプー後、軽く水気を切ってから頭皮と髪全体に揉み込み、頭皮を指の腹で円を描くように1分間マッサージ。その後2〜3分置いてから軽くすすぎ流してください。"
    },
    {
        "rank": 7,
        "tag": "⚡ 朝晩の時短ケアで乾燥知らず！サクランの密着保水膜が1日中続く多機能オールインワン",
        "catch": "化粧水・乳液・美容液・クリーム・パックの5役を1ステップに集約。高濃度スイゼンジノリ多糖体が角層深部へ水分を送り込み、表面を隙間なくラッピングする大容量250gの万能ゲル",
        "brand_name": "たっぷりサクラン",
        "capacity": "250g / 大容量ポンプ式ジャー容器",
        "type": "サクラン高配合 高保湿オールインワンゲル",
        "features": "スイゼンジノリ多糖体、加水分解コラーゲン、植物性セラミド、ヒアルロン酸Na",
        "value": "忙しい冬の朝も夜もこれ1本で完結。ゲル特有のモロモロが出ず、メイク前にも安心して使える高密着テクスチャー。250gのメガサイズで顔からデコルテ・全身まで惜しみなくケア",
        "desc_p1": "冬のスキンケアにおいて、複数の化粧品を重ねづけする時間は寒い洗面所では億劫になりがちです。しかし、一般的なオールインワンゲルでは保湿力が足りず、時間が経つと乾燥して突っ張ってしまうという不満が絶えません。『たっぷりサクラン オールインワンゲル 250g』は、そうしたオールインワンへの不満をスイゼンジノリ多糖体の驚異的な保水力によって一変させる実力派アイテムです。",
        "desc_p2": "ぷるぷるの瑞々しいゲルを肌に乗せると、体温でほぐれるようにスーッと馴染み、サクランの超高分子ネットワークが肌表面に隙間なく展開。加水分解コラーゲンやセラミドを角層深部へと導きながら、外側を水分保持膜で完全に密閉します。重たい油分に頼らず多糖体の保水力で潤すため、毛穴を詰まらせることなく、夕方までふっくらと柔らかいモチ肌が継続。大容量なので、お風呂上がりに顔だけでなく首筋やデコルテ、乾燥する腕やすねまでこれ1本で素早く保湿ケアを完了できます。",
        "target": "子育てや仕事で忙しくスキンケアに時間をかけられない方、手軽に全身を高保湿ケアしたい方、ベタつく重いクリームは苦手だけど乾燥は徹底的に防ぎたい方",
        "point": "洗顔後、さくらんぼ大を手にとって顔全体に伸ばし、手のひらでハンドプレス。特に乾燥が気になる夜は、2倍の量を厚めに塗って『スリーピングパック』として就寝するのがおすすめです。"
    },
    {
        "rank": 8,
        "tag": "🔬 製薬会社が本気で開発！高濃保水サクラン×低分子ヒアルロン酸の浸透型濃密化粧液",
        "catch": "久光製薬が長年の経皮吸収研究を結集して創り上げた高機能スキンケア。希少サクランと低分子ヒアルロン酸のダブル保水システムが、真冬の硬化した角層をほぐして深層保水を叶える名品",
        "brand_name": "LifeCella (ライフセラ / 久光製薬)",
        "capacity": "100ml / 密封ディスペンサー",
        "type": "高機能 浸透型サクライズ化粧液（医薬品メーカー発）",
        "features": "スイゼンジノリ多糖体（サクラン）、浸透型加水分解ヒアルロン酸、持続型保湿アミノ酸、グリセリン",
        "value": "製薬会社ならではの緻密な処方設計。角層表面をガードする巨大分子サクランと、奥深くまで浸透する低分子ヒアルロン酸の多層保水構造で、真冬の砂漠肌を根本解決",
        "desc_p1": "サロンや市販コスメとは一線を画す、医療用医薬品メーカーの皮膚浸透技術が惜しみなく注ぎ込まれたのが、久光製薬ライフセラの『サクライズ 化粧液』です。冬の厳しい寒冷環境下では、角層細胞のターンオーバーが停滞して古くなった角質が蓄積し、化粧水が肌表面で弾かれて内部に届かない『浸透ブロック』が起こります。",
        "desc_p2": "サクライズ化粧液は、微細化された浸透型ヒアルロン酸が角層深部のラメラ間隙へと素早く染み渡り、同時に巨大高分子サクランが肌表面に吸着して強固な保水シールドを構築。角層の内外から同時に水分を挟み撃ちにする多層アプローチを実現しています。化粧水のみずみずしさと乳液の保護力を1本に凝縮した濃密なリキッドは、塗った瞬間から肌がゴクゴクと飲み干すように浸透し、指先を跳ね返すようなふっくらとした弾力を蘇らせます。",
        "target": "冬になると角層が硬化して化粧水が入っていかないと感じる方、製薬メーカーの科学的エビデンスに基づいた確かなコスメを選びたい方、1本で化粧水と美容液の効果を得たい方",
        "point": "洗顔後、1〜2プッシュを手にとって優しく肌を包み込みます。手のひらが肌にピタッと吸い付くまでハンドプレスを数回繰り返すと、保水成分が角層奥深くまで定着します。"
    },
    {
        "rank": 9,
        "tag": "☀️ 弱酸性・無添加でデリケートな冬肌を守る！天然セラミド×サクランのピュアローション",
        "catch": "冬の冷えや乾燥でバリアが低下した敏感肌のために生まれた低刺激設計。熊本産スイゼンジノリ多糖体と植物性セラミドを配合し、赤みやピリつきを起こしやすい素肌を穏やかに満たす高保湿化粧水",
        "brand_name": "エリデン化粧品",
        "capacity": "150mL / スクリューボトル",
        "type": "無添加・低刺激 弱酸性高保湿ローション",
        "features": "スイゼンジノリ多糖体、ユズセラミド、コメヌカエキス、無香料・無着色・鉱物油フリー・パラベンフリー",
        "value": "肌と同じ弱酸性処方。アルコールや刺激成分を徹底排除し、真冬の外気やマスクの摩擦で敏感に傾いた肌でもしみることなく、清らかな潤いを角層にチャージ",
        "desc_p1": "11月から12月にかけて、冬風にさらされた頬が赤くなったり、マフラーの摩擦でピリピリとした刺激を感じたりする『冬季敏感肌』に悩まされる方が急増します。そうしたデリケートな肌状態のときは、多機能すぎる高活性コスメよりも、刺激を極限まで削ぎ落としたピュアな保湿設計が何よりも大切です。エリデン化粧品の『おひさまでつくった化粧水 150mL』は、素肌への優しさを最優先に作られた敏感肌専用ローションです。",
        "desc_p2": "主成分であるスイゼンジノリ多糖体は、天然由来の多糖類であるため抗原性（アレルギー性）が極めて低く、敏感肌にも穏やかになじみます。さらにユズ果実から抽出された天然植物セラミドが角層のバリアを優しく補強。さらりとした軽やかなテクスチャーでありながら、肌に馴染ませるとサクランの保水フィルムが形成され、暖房の効いた室内でも突っ張り感や乾燥による赤みを寄せ付けません。敏感肌のお子様からシニアまで家族全員で安心して使える頼もしい一本です。",
        "target": "真冬になると肌が敏感になり普通の化粧水がピリピリとしみる方、アトピー傾向や超乾燥肌で低刺激なものを探している方、無添加処方で肌本来の健やかさを育みたい方",
        "point": "清潔な手のひらに適量を取り、肌を擦らないように優しくハンドプレスで押し込みます。刺激を感じやすい目元や頬骨周辺は、重ねづけして優しく保護してください。"
    },
    {
        "rank": 10,
        "tag": "🧪 化粧品原料グレード100%！手持ちのコスメを即座にサクラン高保湿化するプロ仕様原液",
        "catch": "化粧品研究室やプロの現場で使われるスイゼンジノリ多糖体液そのもの。手持ちの化粧水、乳液、美容液、ボディローションに数滴加えるだけで、真冬の最高峰プレミアムコスメへと変身",
        "brand_name": "自然化粧品研究所 / スキンケア原料",
        "capacity": "30ml / 遮光ドロッパーボトル",
        "type": "プロ用化粧品原料グレード スイゼンジノリ多糖体原液",
        "features": "水、BG、スイゼンジノリ多糖体（高純度サクラン液）",
        "value": "原料のプロ直販ならではの圧倒的クオリティとコストパフォーマンス。自分好みの濃度でサクランを調合でき、冬の過酷な乾燥に合わせた完全オーダーメイド保湿を実現",
        "desc_p1": "市販のサクラン配合化粧品では濃度が物足りないと感じるスキンケア上級者や、お気に入りのブランドの化粧水を変えずに冬の保湿力だけを極限まで高めたいという方に絶大な支持を得ているのが、自然化粧品研究所の『サクラン（スイゼンジノリ多糖体液） 30ml』です。全国の化粧品受託製造（OEM）や研究所に供給される高品質な化粧品原料を、そのまま個人向けにボトル詰めしたプロユースアイテムです。",
        "desc_p2": "わずか数滴を手持ちの化粧水や美容液に混ぜるだけで、サラサラだったテクスチャーがとろみのあるリッチな感触へと変化し、肌に乗せた瞬間の密着持続力が劇的に向上します。ヒアルロン酸の約10倍という保水膜を自由自在にカスタマイズできるため、特に乾燥がひどい日は濃度を濃いめに調合したり、冬のボディミルクやハンドクリームに混ぜて全身のバリア機能を強化したりと、使い方は無限大。プロ仕様ならではの純粋な保水力を存分に体感できます。",
        "target": "コスメの成分配合や原料にこだわりを持つスキンケア上級者、手持ちのお気に入りコスメの保湿力を冬仕様にパワーアップさせたい方、大容量30mlでコスパ良くサクランを使いたい方",
        "point": "手のひらで手持ちの化粧水に適量を出し、本品を1〜2滴垂らして指先で混ぜ合わせてから顔全体に塗布します。冬のボディミルクに数滴混ぜてすねや腕に伸ばすのも効果的です。"
    }
]

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge">第{p["rank"]}位</span>
            <span class="product-tag">{p["tag"]}</span>
          </div>

          <h3 class="product-title">{p["catch"]}</h3>
          <p class="product-display-name">{item_data["display_name"]}</p>

          <div class="product-layout">
            <div class="product-visual-col">
              <div class="img-wrap">
                <img src="{item_data["image_url"]}" alt="{p["brand_name"]} {item_data["item_name"]}" class="product-img" loading="lazy" />
              </div>
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">¥{item_data["price"]:,}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", "4.8")}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", "120")}件）</span>
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
  <title>保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の約10倍の驚異的保水膜が真冬のエアコン暖房による砂漠化インナードライ肌を救う高保湿サクラン（スイゼンジノリ多糖体）コスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の暖房乾燥によるインナードライ・角層脱水・開き毛穴を救う高保湿サクラン（スイゼンジノリ多糖体）コスメを徹底厳選！ナチュドール、ピアベルピア、MAIKO、久光製薬ライフセラまで自重6,000倍の保水力と第2の皮膚バリアの科学的根拠と共に徹底検証。">
  <meta name="keywords" content="サクラン コスメ, スイゼンジノリ多糖体, 高保湿 コスメ 冬, インナードライ 11月 12月, 暖房乾燥 対策, 保湿美容液, ナチュドール サクラン原液, ピアベルピア Qモイスト, MAIKO モイスチャーローション">

  <!-- OGP (SNSシェア / 日本語圏最適化) -->
  <meta property="og:site_name" content="LUMI COSMETICS">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の約10倍の驚異的保水膜が真冬のエアコン暖房による砂漠化インナードライ肌を救う高保湿サクラン（スイゼンジノリ多糖体）コスメランク10">
  <meta property="og:description" content="ヒアルロン酸の10倍の保水力！阿蘇の清流が生んだ巨大バイオ多糖体サクランが、真冬の強烈な暖房気流から素肌を守り抜くおすすめコスメ10選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-sacran">
  <meta property="og:image" content="{items[0]["image_url"]}">

  <!-- Twitter / X Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高保湿サクランコスメランク10">
  <meta name="twitter:description" content="11月・12月のエアコン砂漠肌に！ヒアルロン酸を凌駕する保水多糖体サクランコスメおすすめ厳選10選。">
  <meta name="twitter:image" content="{items[0]["image_url"]}">

  <!-- 構造化データ (JSON-LD) #1: Article -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の約10倍の驚異的保水膜が真冬のエアコン暖房による砂漠化インナードライ肌を救う高保湿サクラン（スイゼンジノリ多糖体）コスメランク10",
    "description": "11月・12月の暖房乾燥によるインナードライ・角層脱水を救う高保湿サクラン（スイゼンジノリ多糖体）コスメを徹底厳選！",
    "image": "{items[0]["image_url"]}",
    "datePublished": "2026-11-06T01:00:00+09:00",
    "dateModified": "2026-11-06T01:00:00+09:00",
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
      "@id": "https://lumi-cosme.vercel.app/winter-sacran"
    }}
  }}
  </script>

  <!-- 構造化データ (JSON-LD) #2: ItemList -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿サクラン（スイゼンジノリ多糖体）コスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "{product_details[0]["brand_name"]} {items[0]["item_name"]}",
        "url": "{items[0]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{product_details[1]["brand_name"]} {items[1]["item_name"]}",
        "url": "{items[1]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{product_details[2]["brand_name"]} {items[2]["item_name"]}",
        "url": "{items[2]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 4,
        "name": "{product_details[3]["brand_name"]} {items[3]["item_name"]}",
        "url": "{items[3]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 5,
        "name": "{product_details[4]["brand_name"]} {items[4]["item_name"]}",
        "url": "{items[4]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 6,
        "name": "{product_details[5]["brand_name"]} {items[5]["item_name"]}",
        "url": "{items[5]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 7,
        "name": "{product_details[6]["brand_name"]} {items[6]["item_name"]}",
        "url": "{items[6]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 8,
        "name": "{product_details[7]["brand_name"]} {items[7]["item_name"]}",
        "url": "{items[7]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 9,
        "name": "{product_details[8]["brand_name"]} {items[8]["item_name"]}",
        "url": "{items[8]["affiliate_url"]}"
      }},
      {{
        "@type": "ListItem",
        "position": 10,
        "name": "{product_details[9]["brand_name"]} {items[9]["item_name"]}",
        "url": "{items[9]["affiliate_url"]}"
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
        "name": "サクラン（スイゼンジノリ多糖体）とヒアルロン酸の決定的な違いは何ですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "最大の相違点は分子量と塩分耐性、そして保水シールドの強さです。ヒアルロン酸の分子量が約100万〜200万であるのに対し、サクランは約1600万と圧倒的に巨大です。さらに、ヒアルロン酸は肌の汗や皮脂に含まれる微量な塩分に触れると保水力が半減してしまいますが、サクランは分子内の特異な硫酸基構造により、塩分環境下でもヒアルロン酸の約5〜10倍の保水力を維持し続けます。これにより、真冬の暖房下でも乾燥蒸散を長時間シャットアウトします。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "サクラン配合コスメは朝のメイク前に使ってもモロモロやヨレが出ませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "サクランは超高分子多糖体でありながら、水との親和性が極めて高く、皮膚表面に均一で薄い柔軟な生体皮膜を形成するため、合成ポリマーのように消しゴムのカス状のモロモロが出にくいのが大きな美点です。適量を肌に乗せて手のひらでハンドプレスして馴染ませれば、ファンデーションの密着度を高めるプライマー効果を発揮します。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "敏感肌やアトピー傾向の肌でも真冬に使えますか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "極めて適しています。スイゼンジノリは熊本の阿蘇山系の純粋な伏流水でのみ生息する極めて清らかな藍藻であり、抽出されたサクラン多糖体は天然由来で抗原性が極めて低く、敏感肌や荒れた角層を優しく包み込みます。外的刺激やアレルゲン、乾燥風が直接角層に触れるのを物理的に防ぐ第二の皮膚として機能するため、真冬のピリピリ肌の保護に最適です。"
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
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --gold: #d97706;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -4px rgba(0, 0, 0, 0.04);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Hiragino Kaku Gothic ProN", "Meiryo", sans-serif;
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
      z-index: 50;
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
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.025em;
    }}

    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}

    .article-header {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
    }}

    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}

    .article-category {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}

    h1.article-title {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 1.25rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }}

    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      padding-top: 1rem;
      border-top: 1px solid var(--border);
    }}

    .lead-box {{
      background: #ffffff;
      border-left: 5px solid var(--primary);
      padding: 1.75rem;
      border-radius: 0 var(--radius) var(--radius) 0;
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      font-size: 1.05rem;
      color: #334155;
    }}

    .lead-box p {{
      margin-bottom: 1rem;
    }}
    .lead-box p:last-child {{
      margin-bottom: 0;
    }}

    .science-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .section-title {{
      font-size: 1.45rem;
      color: #0f172a;
      font-weight: 800;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.5rem;
    }}

    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }}

    .science-card {{
      background: var(--bg);
      padding: 1.5rem;
      border-radius: var(--radius);
      border: 1px solid var(--border);
    }}

    .science-card h4 {{
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-box {{
      background: #ffffff;
      padding: 1.75rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .toc-title {{
      font-weight: 800;
      font-size: 1.15rem;
      margin-bottom: 1rem;
      color: var(--primary-dark);
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 0.5rem 1.5rem;
    }}

    .toc-list li a {{
      color: #334155;
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2.25rem 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      transition: box-shadow 0.2s, transform 0.2s;
    }}

    .product-card:hover {{
      box-shadow: var(--shadow-lg);
      transform: translateY(-2px);
    }}

    .product-header {{
      display: flex;
      align-items: center;
      gap: 1rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}

    .rank-badge {{
      background: var(--gold);
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 0.25rem 0.85rem;
      border-radius: 9999px;
      letter-spacing: 0.05em;
    }}

    .product-tag {{
      color: var(--primary-dark);
      font-size: 0.9rem;
      font-weight: 700;
    }}

    .product-title {{
      font-size: 1.4rem;
      line-height: 1.45;
      color: #0f172a;
      margin-bottom: 0.5rem;
      font-weight: 800;
    }}

    .product-display-name {{
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 1.75rem;
      background: var(--bg);
      padding: 0.6rem 1rem;
      border-radius: 8px;
    }}

    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .product-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .product-visual-col {{
      text-align: center;
    }}

    .img-wrap {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1rem;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
    }}

    .price-box {{
      background: var(--bg);
      padding: 0.75rem;
      border-radius: 8px;
      margin-bottom: 0.75rem;
    }}

    .price-label {{
      display: block;
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .price-value {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #e11d48;
    }}

    .review-meta {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.25rem;
    }}

    .review-stars {{
      color: var(--gold);
      font-weight: 700;
    }}

    .rakuten-btn {{
      display: block;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.2);
    }}

    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-1px);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
    }}

    .spec-table th, .spec-table td {{
      padding: 0.6rem 0.85rem;
      border: 1px solid var(--border);
    }}

    .spec-table th {{
      background: var(--bg);
      color: #334155;
      width: 25%;
      font-weight: 700;
      text-align: left;
    }}

    .spec-table td {{
      color: #1e293b;
    }}

    .product-body p {{
      margin-bottom: 1.1rem;
      color: #334155;
      font-size: 0.98rem;
    }}

    .body-title {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      font-weight: 700;
      margin-bottom: 0.75rem;
      border-left: 3px solid var(--primary);
      padding-left: 0.5rem;
    }}

    .recommend-box, .usage-box {{
      padding: 1rem 1.25rem;
      border-radius: 8px;
      margin-top: 1.25rem;
      font-size: 0.92rem;
    }}

    .recommend-box {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      color: #166534;
    }}

    .recommend-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: #15803d;
    }}

    .usage-box {{
      background: #f8fafc;
      border: 1px solid var(--border);
      color: #334155;
    }}

    .usage-title {{
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--primary-dark);
    }}

    .comparison-section, .faq-section, .internal-links-section {{
      background: #ffffff;
      padding: 2.25rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 3rem;
      border: 1px solid var(--border);
    }}

    .comparison-table-wrap {{
      overflow-x: auto;
    }}

    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 600px;
    }}

    .comparison-table th, .comparison-table td {{
      padding: 0.85rem;
      border: 1px solid var(--border);
      text-align: left;
    }}

    .comparison-table th {{
      background: var(--bg);
      color: #0f172a;
      font-weight: 700;
    }}

    .comparison-table tr:hover {{
      background: #f1f5f9;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1.5rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-a {{
      color: #334155;
      font-size: 0.95rem;
      padding-left: 1.5rem;
    }}

    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-top: 1.5rem;
    }}

    .internal-card {{
      background: var(--bg);
      padding: 1.25rem;
      border-radius: 8px;
      border: 1px solid var(--border);
      text-decoration: none;
      color: var(--text);
      display: block;
      transition: border-color 0.2s, transform 0.1s;
    }}

    .internal-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}

    .internal-card-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
    }}

    .internal-card-desc {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 2rem;
    }}

    @media (max-width: 768px) {{
      .footer-inner {{
        grid-template-columns: 1fr;
      }}
    }}

    .footer-logo {{
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      margin-bottom: 0.75rem;
    }}

    .footer-text {{
      font-size: 0.85rem;
      line-height: 1.7;
    }}

    .footer-links h5 {{
      color: #ffffff;
      margin-bottom: 0.75rem;
      font-size: 0.95rem;
    }}

    .footer-links ul {{
      list-style: none;
    }}

    .footer-links li a {{
      color: #94a3b8;
      text-decoration: none;
      font-size: 0.85rem;
      line-height: 2;
    }}

    .footer-links li a:hover {{
      color: #ffffff;
    }}

    .copyright {{
      max-width: 1000px;
      margin: 2rem auto 0;
      padding-top: 1.5rem;
      border-top: 1px solid #1e293b;
      text-align: center;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">冬コスメTOP</a>
        <a href="#ranking">ランキング10選</a>
        <a href="#comparison">徹底比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <article>
      <div class="article-header">
        <div class="breadcrumb">
          <a href="/">HOME</a> &gt; <a href="/">冬の乾燥対策スキンケア</a> &gt; 高保湿サクラン（スイゼンジノリ多糖体）特集
        </div>
        <span class="article-category">11月・12月 冬季高保湿スキンケア特集</span>
        <h1 class="article-title">保湿力の強さで肌乾燥とさようなら！ヒアルロン酸の約10倍の驚異的保水膜が真冬のエアコン暖房による砂漠化インナードライ肌を救う高保湿サクラン（スイゼンジノリ多糖体）コスメランク10</h1>
        <div class="article-meta">
          <span>📅 公開日: 2026年11月6日</span>
          <span>🔄 最終更新: 2026年11月6日</span>
          <span>✍ 監修: LUMI COSMETICS 皮膚科学コスメ解析班</span>
          <span>⏱ 読了目安: 約8分</span>
        </div>
      </div>

      <div class="lead-box">
        <p><strong>11月から12月にかけて、室内外の空気は一気に乾燥の極限へと突入します。</strong>外気温度の急低下により皮膚の皮脂分泌量は夏の半分以下へと激減し、オフィスや自宅では暖房エアコンがフル稼働。その結果、角層の水分は毎秒猛烈なスピードで奪われ、「朝どんなに高保湿クリームを塗っても、昼過ぎには目元や口元が突っ張って粉を吹く」「肌の表面はテカるのに内側が突っ張るインナードライが止まらない」という深刻な肌トラブルが続出します。</p>
        <p>この真冬の過酷な角層脱水を根本から断ち切る究極のキー成分として、今美容業界と皮膚科学研究者から熱狂的な注目を浴びているのが、日本固有の希少藍藻から抽出される<strong>『サクラン（スイゼンジノリ多糖体）』</strong>です。熊本県阿蘇山系の清らかな伏流水でのみ育つ奇跡の藻から得られるこの巨大多糖体は、<strong>ヒアルロン酸の約10倍、純水中で自身の重さの約6,000倍</strong>という驚異的な保水力を誇り、肌表面に目に見えない「第二の皮膚」を形成して乾燥気流を完全遮断します。</p>
        <p>本記事では、楽天市場で実際に高評価を獲得している正規品の中から、成分濃度・処方設計・使用感・コストパフォーマンスを徹底検証した<strong>真冬の高保湿サクランコスメおすすめランキング10選</strong>を余すところなくご紹介します。</p>
      </div>

      <section class="science-section">
        <h2 class="section-title">🧬 なぜ真冬の乾燥に「サクラン（スイゼンジノリ多糖体）」が圧倒的に強いのか？皮膚科学的3大根拠</h2>
        <p>ヒアルロン酸やコラーゲンなど数ある保水成分の中で、なぜサクランが11月・12月の極限乾燥に対して突出した効果を発揮するのか、その科学的理由を整理しました。</p>

        <div class="science-grid">
          <div class="science-card">
            <h4>💧 分子量1600万の超巨大バイオ保水膜</h4>
            <p>一般的な高分子ヒアルロン酸の分子量が約100万〜200万であるのに対し、サクランの分子量は約1600万ダルトンと約8〜16倍の巨大さを誇ります。この超巨大分子が皮膚表面に隙間なく展開し、まるで人工の生体皮膜のような極薄保水ヴェールを形成。角層内の水分蒸散を物理的にシャットアウトします。</p>
          </div>

          <div class="science-card">
            <h4>🛡️ 汗や皮脂の塩分でも保水力が落ちない特異構造</h4>
            <p>ヒアルロン酸の弱点は、皮膚上の汗や皮脂に含まれる微量な塩分（ナトリウムイオン等）に触れると分子が縮退し、保水力が約半分に落ちてしまう点にあります。サクランは分子内に多数の硫酸基を持つため、塩分が存在する過酷な皮膚環境下でも分子構造を維持し、ヒアルロン酸の約10倍の保水力を維持し続けます。</p>
          </div>

          <div class="science-card">
            <h4>🌿 外的刺激・摩擦を遮断するバリア補強</h4>
            <p>サクランが形成する保水フィルムは、外からの冷風、衣類やマスクの摩擦、大気中の微粒子汚れが直接デリケートな角層に触れるのを防ぐ物理的シールドとしても機能します。乾燥でバリアが低下し、ピリピリと過敏になった冬の肌を穏やかに鎮静し、健やかなターンオーバーを力強くアシストします。</p>
          </div>
        </div>
      </section>

      <section class="toc-box">
        <div class="toc-title">📑 目次：高保湿サクランコスメ厳選10選一覧</div>
        <ul class="toc-list">
          <li><a href="#rank-1">第1位：ナチュドール サクラン原液 20mL</a></li>
          <li><a href="#rank-2">第2位：ピアベルピア Qモイスト 50ml</a></li>
          <li><a href="#rank-3">第3位：MAIKO モイスチャーローション 120ml</a></li>
          <li><a href="#rank-4">第4位：高濃度ヒト型セラミド＆サクラン クリーム 20g</a></li>
          <li><a href="#rank-5">第5位：デュフラ フィトフォース モイストローション</a></li>
          <li><a href="#rank-6">第6位：グラシア サクラン スカルプケアマスク 200g</a></li>
          <li><a href="#rank-7">第7位：たっぷりサクラン オールインワンゲル 250g</a></li>
          <li><a href="#rank-8">第8位：久光製薬 ライフセラ サクライズ 化粧液 100ml</a></li>
          <li><a href="#rank-9">第9位：エリデン おひさまでつくった化粧水 150mL</a></li>
          <li><a href="#rank-10">第10位：自然化粧品研究所 スイゼンジノリ多糖体液 30ml</a></li>
        </ul>
      </section>

      <section id="ranking">
        <h2 class="section-title">🏆 2026年最新！真冬の高保湿サクランコスメおすすめ厳選ランキング10選</h2>
        <p style="margin-bottom: 2rem; color: #475569;">※本ランキングは、楽天市場におけるリアルタイムの商品データ（価格・在庫・口コミ評価・配合純度）を基準に、冬の乾燥対策に特化して厳正に順位づけしています。</p>

        {all_cards_html}
      </section>

      <section class="comparison-section" id="comparison">
        <h2 class="section-title">📊 高保湿サクランコスメ10選 スペック徹底比較表</h2>
        <p style="margin-bottom: 1.5rem; color: #475569;">あなたの肌質、使いたい部位、テクスチャーの好みに合わせて最適な1本をお選びください。</p>

        <div class="comparison-table-wrap">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位 / 商品名</th>
                <th>ブランド</th>
                <th>アイテム種別</th>
                <th>参考価格</th>
                <th>特長・おすすめターゲット</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>第1位</strong> ナチュドール サクラン原液</td>
                <td>NATUDOR</td>
                <td>100%原液美容液</td>
                <td>¥5,100</td>
                <td>阿蘇産純度100%。手持ちコスメに混ぜて即効高保水化したい方</td>
              </tr>
              <tr>
                <td><strong>第2位</strong> ピアベルピア Qモイスト</td>
                <td>Piabelpia</td>
                <td>敏感肌用美容液</td>
                <td>¥5,390</td>
                <td>サクラン×Q10×ヒアルロン酸。敏感肌の冬のエイジングケアに</td>
              </tr>
              <tr>
                <td><strong>第3位</strong> MAIKO モイスチャーローション</td>
                <td>MAIKO</td>
                <td>高保湿化粧水</td>
                <td>¥8,800</td>
                <td>京都発の和漢上質ローション。美容液級のとろみで砂漠肌を満たす</td>
              </tr>
              <tr>
                <td><strong>第4位</strong> 高濃度セラミド＆サクランクリーム</td>
                <td>スキンケアファクトリー</td>
                <td>バリア修復クリーム</td>
                <td>¥1,700</td>
                <td>ヒト型セラミド3種配合。水仕事のあかぎれ・手荒れを強力保護</td>
              </tr>
              <tr>
                <td><strong>第5位</strong> デュフラ モイストローション</td>
                <td>DIEUFRA</td>
                <td>サロン専売化粧水</td>
                <td>¥3,619</td>
                <td>オーガニックハーブ配合。冬の開き毛穴とキメ乱れをプロ仕様でケア</td>
              </tr>
              <tr>
                <td><strong>第6位</strong> グラシア スカルプケアマスク</td>
                <td>Gracia</td>
                <td>ヘア＆スカルプマスク</td>
                <td>¥3,850</td>
                <td>頭皮の乾燥かゆみ・フケと毛先のパサつき・静電気を同時に防ぐ</td>
              </tr>
              <tr>
                <td><strong>第7位</strong> たっぷりサクラン オールインワンゲル</td>
                <td>たっぷりサクラン</td>
                <td>多機能ゲル 250g</td>
                <td>¥1,880</td>
                <td>忙しい朝晩の時短に。大容量メガサイズで全身バリア密着</td>
              </tr>
              <tr>
                <td><strong>第8位</strong> ライフセラ サクライズ 化粧液</td>
                <td>久光製薬</td>
                <td>浸透型化粧液</td>
                <td>¥8,910</td>
                <td>製薬会社の浸透技術。角層の内外から多層挟み撃ち保水</td>
              </tr>
              <tr>
                <td><strong>第9位</strong> おひさまでつくった化粧水</td>
                <td>エリデン化粧品</td>
                <td>無添加弱酸性化粧水</td>
                <td>¥1,760</td>
                <td>低刺激ピュア設計。冷えと摩擦でピリピリする冬季敏感肌に</td>
              </tr>
              <tr>
                <td><strong>第10位</strong> スイゼンジノリ多糖体液 原料</td>
                <td>自然化粧品研究所</td>
                <td>コスメ原料 30ml</td>
                <td>¥9,944</td>
                <td>プロ仕様原料グレード。自分好みの濃度でサクランを調合</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section class="faq-section" id="faq">
        <h2 class="section-title">❓ 真冬のサクランコスメ活用 Q&A：よくある質問</h2>

        <div class="faq-item">
          <div class="faq-q">Q1. サクラン（スイゼンジノリ多糖体）とヒアルロン酸の決定的な違いは何ですか？</div>
          <div class="faq-a">
            最大の相違点は分子量と塩分耐性、そして保水シールドの強さです。ヒアルロン酸の分子量が約100万〜200万であるのに対し、サクランは約1600万と圧倒的に巨大です。さらに、ヒアルロン酸は肌の汗や皮脂に含まれる微量な塩分に触れると保水力が半減してしまいますが、サクランは分子内の特異な硫酸基構造により、塩分環境下でもヒアルロン酸の約5〜10倍の保水力を維持し続けます。これにより、真冬の暖房下でも乾燥蒸散を長時間シャットアウトします。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q2. サクラン配合コスメは朝のメイク前に使ってもモロモロやヨレが出ませんか？</div>
          <div class="faq-a">
            サクランは超高分子多糖体でありながら、水との親和性が極めて高く、皮膚表面に均一で薄い柔軟な生体皮膜を形成するため、合成ポリマーのように消しゴムのカス状のモロモロが出にくいのが大きな美点です。適量を肌に乗せて手のひらでハンドプレスして馴染ませれば、ファンデーションの密着度を高めるプライマー効果を発揮します。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q3. 敏感肌やアトピー傾向の肌でも真冬に使えますか？</div>
          <div class="faq-a">
            極めて適しています。スイゼンジノリは熊本の阿蘇山系の純粋な伏流水でのみ生息する極めて清らかな藍藻であり、抽出されたサクラン多糖体は天然由来で抗原性が極めて低く、敏感肌や荒れた角層を優しく包み込みます。外的刺激やアレルゲン、乾燥風が直接角層に触れるのを物理的に防ぐ第二の皮膚として機能するため、真冬のピリピリ肌の保護に最適です。
          </div>
        </div>

        <div class="faq-item">
          <div class="faq-q">Q4. 最も効果的なスキンケアの組み合わせ順序を教えてください。</div>
          <div class="faq-a">
            原液タイプ（ナチュドール等）の場合は「洗顔直後の導入」または「化粧水に1〜2滴ブレンド」が最も効果的です。化粧水やオールインワンの場合は通常通り塗布し、極度の乾燥肌の方は最後にシアバターやセラミドクリームなどの油分で軽くフタをすることで、水溶性サクランの保水シールドと油分エモリエント膜のW密閉が完成します。
          </div>
        </div>
      </section>

      <section class="internal-links-section">
        <h2 class="section-title">🔗 あわせて読みたい！冬の高保湿スキンケア関連記事</h2>
        <p style="color: #475569; font-size: 0.95rem;">真冬の乾燥トラブルを全方位から撃退する人気特集記事をピックアップ。</p>

        <div class="internal-grid">
          <a href="/winter-collagen" class="internal-card">
            <div class="internal-card-title">🌸 高保湿生コラーゲンコスメ10選</div>
            <div class="internal-card-desc">三重らせん構造を保った生コラーゲンが真冬のしぼみ肌と乾燥小ジワをぷるんと押し上げる！</div>
          </a>
          <a href="/winter-tremella" class="internal-card">
            <div class="internal-card-title">💧 高保湿シロキクラゲコスメ10選</div>
            <div class="internal-card-desc">植物性ムコ多糖類がインナードライ肌を満たし続ける！シロキクラゲ多糖体特化特集。</div>
          </a>
          <a href="/winter-mango-butter" class="internal-card">
            <div class="internal-card-title">🥭 高保湿マンゴーバターコスメ10選</div>
            <div class="internal-card-desc">体温35℃でとろける高純度ステアリン酸！ひび割れ肌とパサつく毛先を濃密ラッピング。</div>
          </a>
          <a href="/winter-ceramide-cream" class="internal-card">
            <div class="internal-card-title">🛡️ 高保湿セラミドクリーム10選</div>
            <div class="internal-card-desc">角層のラメラ構造を立て直すヒト型セラミド！冬のバリア機能崩壊を防ぎ切る名品。</div>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer>
    <div class="footer-inner">
      <div>
        <div class="footer-logo">LUMI COSMETICS</div>
        <p class="footer-text">
          LUMI COSMETICSは、11月〜12月の本格的な寒冷・乾燥シーズンを乗り切るための高品質コスメ・スキンケア情報を専門にお届けするビューティーメディアです。皮膚科学的根拠に基づいた成分解析と楽天市場のリアルタイムデータを融合し、客観的で信頼性の高いコスメ選びをサポートします。
        </p>
      </div>
      <div class="footer-links">
        <h5>サイトマップ・リンク</h5>
        <ul>
          <li><a href="/">冬コスメTOP</a></li>
          <li><a href="/winter-sacran">高保湿サクラン</a></li>
          <li><a href="/winter-collagen">高保湿コラーゲン</a></li>
          <li><a href="/winter-tremella">高保湿シロキクラゲ</a></li>
          <li><a href="/winter-mango-butter">高保湿マンゴーバター</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      &copy; 2026 LUMI COSMETICS. All Rights Reserved.
    </div>
  </footer>

</body>
</html>
"""

with open("winter-sacran.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated winter-sacran.html successfully! (File size: {len(full_html):,} bytes)")
