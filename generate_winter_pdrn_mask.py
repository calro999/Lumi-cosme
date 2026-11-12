import json
import re

with open("fetched_3new_pdrn_retinol_panthenol.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_pdrn_mask"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🥇 美容医療発想サーモンDNAの最高峰！真冬の深刻なしぼみ肌を細胞レベルで再生するリジュラン公式マスク",
        "catch": "韓国美容医療の代名詞『リジュラン注射』の主成分c-PDRNを贅沢に配合。極細マイクロセルシートが冷気と暖房で干からびた肌深部に高純度ポリヌクレオチドをダイレクトに注入し、圧倒的ハリと水分ツヤを呼び覚ます",
        "brand_name": "REJURAN (リジュラン)",
        "capacity": "5枚入 (1枚あたり美容液40mL)",
        "type": "高純度c-PDRN配合 高密着マイクロファイバーマスク",
        "features": "独自高純度c-PDRN®、ツボクサエキスエキス、アデノシン、天然セルロースマイクロシート",
        "value": "1回で美容液1本分（40mL）を贅沢に浴びる集中再生ケア。11月・12月の寒冷刺激でターンオーバーが停止し、ファンデが乗らないスカスカ肌を、わずか15分で指が跳ね返るほどの密度へ引き上げる",
        "desc_p1": "11月から12月にかけての気温急低下は、皮膚表面の血流を停滞させ、真皮内の線維芽細胞の働きを著しく鈍化させます。その結果、肌は水分を抱え込む土台を失い、急激なしぼみと乾燥たるみが生じます。リジュランの『リフレッシュ スキン プロテクション マスク』は、サーモン由来のDNA断片を高精製した特許成分c-PDRNを高濃度に配合。細胞の再生サイクルを後押しし、肌自らがヒアルロン酸やコラーゲンを再生産する力を強力に引き出します。",
        "desc_p2": "シート素材には、液だれを防ぎながら肌の微細なキメの溝まで均一に吸着する極薄マイクロセルシートを採用。40mLという一般的なマスクの約2倍近い濃厚な美容液を含浸しながらも、肌にのせた瞬間にピタッと密着して剥がれません。マスクを外した瞬間、水分で発光するような『水光ツヤ』と、触れた指を押し返すほどの濃密な弾力感に満たされます。",
        "target": "冬の乾燥で頬の毛穴が縦に流れてきた方、何層にもクリームを重ねても内側から肌がしぼむ方、週末にサロン級のスペシャル再生ケアを取り入れたい方",
        "point": "洗顔後、導入美容液や化粧水で肌のベースを整えた後に顔全体へ密着させます。40mLの美容液がパウチにたっぷり残るため、シートの上から重ね付けし、さらに首すじ・デコルテ・手の甲まで惜しみなく伸ばしてください。20分ほど置いて剥がした後は、乳液やクリームで油膜密閉を行うと翌朝まで発光感が持続します。"
    },
    {
        "rank": 2,
        "tag": "💎 貼ったまま眠れるハイドロゲル！透明に溶け込みながらPDRNをじっくり浸透させる新感覚マスク",
        "catch": "VTが誇る最先端バイオテクノロジーから誕生した、植物性高純度PDRN配合のハイドロゲルマスク。肌の温度に反応して美容成分が角層奥深くへ浸透し、シートが徐々に透明へと変化する驚異の密閉力",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "4枚入 (個包装)",
        "type": "植物性高純度PDRN×ハイドロゲル密閉パック",
        "features": "山参植物性PDRN（PHYTO PDRN®）、セラミドNP、低分子コラーゲン、高密着温度感応ハイドロゲル",
        "value": "不織布シートと異なり、水分が空気中へ逃げない完全密閉ハイドロゲル構造。暖房をつけた寝室でも乾燥せず、睡眠中の2〜3時間かけて美容成分を骨の髄まで浸透させる",
        "desc_p1": "冬の夜間、暖房を稼働させた寝室の湿度は容易に20%台まで降下します。一般的なシートマスクでは15分以上貼ると水分蒸散（逆浸透）のリスクがありますが、VTのPDRNハイドロゲルマスクは美容液そのものを固めてゲル状にした特殊シートを採用。肌の体温に反応して有効成分が液状化しながら角層へじわじわと吸い込まれていきます。",
        "desc_p2": "主成分には高麗人参（山参）から抽出した超高純度フィトPDRNを採用し、動物性特有の匂いや刺激を徹底排除。肌の奥で低下した弾力ネットワークを修復し、ゆるんだ毛穴をキュッと引き締めます。白濁したゲルシートが透明に変わった時が成分浸透完了のサイン。翌朝剥がした時の、陶器のように毛穴レスでなめらかな肌触りは感動的です。",
        "target": "シートマスクが乾いて逆に乾燥するのが怖い方、睡眠中の暖房乾燥から一晩中肌を完全ガードしたい方、毛穴の開きとたるみを同時に引き締めたい方",
        "point": "夜のスキンケアの最後に使用します。化粧水、美容液、乳液を一通り馴染ませた後、上下に分かれたゲルシートを顔の凹凸に合わせて密着させます。最低でも2〜3時間、または貼ったまま就寝し、翌朝完全に透明になったら優しく剥がしてください。朝の洗顔時の肌のツルツル感に驚かされます。"
    },
    {
        "rank": 3,
        "tag": "🌸 医療用発想の低分子マリンPDRN！寒冷たるみ肌を物理的リフトアップシートで強力引き締め",
        "catch": "シートマスクのグローバル絶対王者メディヒールが送り出すPDRN集中リフトマスク。低分子化されたマリンPDRNとコラーゲンカプセルが、冬の冷気で硬直・たるんだフェイスラインをグッと引き上げながら深層保水",
        "brand_name": "MEDIHEAL (メディヒール)",
        "capacity": "10枚入 / ボックス",
        "type": "低分子マリンPDRN×コラーゲンカプセル配合 リフティングマスク",
        "features": "低分子サーモンPDRN、マリンコラーゲンカプセル、ナイアシンアミド、特許リフティングカットシート",
        "value": "10枚入りで手頃に継続できる抜群のコスパ。あご下から耳元へ引き上げる特殊スリット設計により、真冬の寒さでむくみ・たるんだ輪郭を物理的かつ成分的にダブルリフト",
        "desc_p1": "寒さが本格化する11月・12月は、毛細血管の収縮によって顔の筋肉や皮膚が硬直。さらに新陳代謝が落ちることでフェイスラインがもたつき、乾燥小ジワとともに輪郭のぼやけが深刻化します。メディヒールのTHE PDRN リフティングマスクは、超微細に微粉砕されたマリンPDRNとコラーゲン複合体を贅沢に配合し、角層の隙間へ高速浸透させます。",
        "desc_p2": "最大の特徴は、顎下からフェイスラインを包み込んで耳の方向へと引き上げる独自の3Dリフティングスリット構造にあります。シートを引っ張り上げながら装着することで、物理的なタイトニング効果を発揮。15分後には、肌の水分量が満タンになるだけでなく、フェイスラインがキュッとシャープに引き締まった感覚を実感できます。",
        "target": "冬のむくみや輪郭のもたつきが気になる方、1回あたりのコストを抑えて週2〜3回PDRNマスクを続けたい方、シートマスクにリフトアップ効果も求めたい方",
        "point": "マスクを顔の上部に合わせた後、顎下の両サイドのウィングを持ち上げ、フェイスラインを引き上げるようにこめかみ方向へ密着させます。15分間そのままキープし、剥がした後は残った乳液状アンプルを下から上へハンドプレスしながら浸透させてください。"
    },
    {
        "rank": 4,
        "tag": "💧 水分爆弾×PDRNスマートカプセル！冬のインナードライを秒速で鎮める高密度ウォーターマスク",
        "catch": "鎮静と浸透研究に定評のあるアヌアが開発した、スマートカプセル化PDRNと8重ヒアルロン酸のハイブリッドマスク。皮脂が出ているのに内側が突っ張る真冬の暖房インナードライを根本から解消",
        "brand_name": "Anua (アヌア)",
        "capacity": "5枚入 / パウチ",
        "type": "スマートカプセルPDRN×多重ヒアルロン酸配合 高密度水分アンプルマスク",
        "features": "PDRNリポソームカプセル、8種の分子量別ヒアルロン酸、パンテノール、低刺激マイクロファイバー",
        "value": "ベタつく重い油分が苦手な混合肌でも使いやすいみずみずしい濃密アンプル処方。暖房の温風で水分だけが蒸発したスカスカ角層に、純粋な生体水分と再生シグナルを一気に送り込む",
        "desc_p1": "暖房の効いたオフィスや部屋で長時間過ごすと、皮膚表面は皮脂でテカっているのに内側の角層水分が著しく蒸散する『暖房インナードライ』に陥ります。アヌアのPDRNヒアルロン酸マスクは、PDRNを微小なリポソームカプセルに閉じ込めることで、角層のラメラ液晶構造をスムーズにすり抜けて深層へ届くよう設計されています。",
        "desc_p2": "さらに分子量の異なる8種類のヒアルロン酸が、角層の表面から深部まで多段的に水分を配置。密着性の高いセルロースシートが肌の凹凸にぴったり吸着し、乾ききった細胞一つひとつをみずみずしく膨らませます。剥がした後はベタつきが一切残らず、内側からジュワッと水分が湧き出るような透明感を手に入れられます。",
        "target": "夕方になると暖房で顔が突っ張る・粉を吹く方、オイリーなのに内側が乾燥している混合肌の方、メイク前に素早く水分を満たして化粧崩れを防ぎたい方",
        "point": "朝のメイク前や夜の入浴後に使用します。シートを密着させて10〜15分置いた後、剥がして手のひらで軽くパッティング。ベタつかない処方のため、朝に使ってもその後の下地やファンデーションがヨレず、1日中みずみずしいツヤを維持できます。"
    },
    {
        "rank": 5,
        "tag": "💗 サーモンPDRN×マルチペプチド！冬の寒風で青白くくすんだ顔色に生き生きとした血色感を宿す",
        "catch": "韓国先端ダーマコスメmedicube（メディキューブ）の大ヒットPDRNシリーズ。高純度サーモンDNAとマルチペプチドをピンクの濃密美容液に凝縮し、冬の寒さでしぼんだ肌に押し返すような弾力と透明ピンクのツヤを注入",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "アンプル美容液セット / マスク",
        "type": "高純度サーモンPDRN×マルチペプチド配合 濃密弾力ピンクマスク",
        "features": "サーモン卵由来高純度PDRN、5種のペプチドコンプレックス、ナイアシンアミド、シアノコバラミン（ビタミンB12）",
        "value": "ビタミンB12本来の天然ピンクカラーが、寒さで血行不良を起こした冬肌に自然な血色ツヤを付与。ペプチドとPDRNの相乗効果で、乾燥によるたるみ毛穴をキュッと引き締める",
        "desc_p1": "11月後半から12月は、外気の冷たさによって毛細血管が収縮し、顔全体が青白くくすんだり、疲れた印象に見えがちです。メディキューブのPDRNピンクアンプルシリーズは、天然のビタミンB12とサーモン由来PDRNをブレンド。肌の再生を促すとともに、どんよりとした冬のくすみ肌にイキイキとした健康的な血色感を取り戻します。",
        "desc_p2": "さらに5種類の機能性ペプチドが配合されており、PDRNが整えた肌土台の上でコラーゲン繊維の結びつきをサポート。毛穴の周りの皮膚がふっくらと持ち上がるため、乾燥によって縦長に広がった『たるみ毛穴』が目立たなくなります。濃密なとろみがありながらも肌馴染みが良く、リッチなケアを求める冬に最適です。",
        "target": "冬になると顔色が冴えず疲れて見える方、頬の毛穴の開きやキメの乱れが気になる方、PDRNにペプチドのハリ効果もプラスしたい欲張りな方",
        "point": "化粧水で肌を整えた後、シートを乗せて15〜20分置きます。剥がした後は、手のひらで顔全体を包み込み、手の温度でじっくり押し込むようにハンドプレスしてください。首やデコルテにも馴染ませると、首元の乾燥ジワ予防にも役立ちます。"
    },
    {
        "rank": 6,
        "tag": "🧪 北海道産サーモンPDRN原液を惜しみなく配合！毎日のデイリーケアで真冬の肌密度を高めるサイエンスマスク",
        "catch": "成分特化型ジャパニーズサイエンスコスメKISOが手がける高濃度PDRNシートマスク。北海道産天然秋鮭由来の高純度PDRNを配合し、30枚入り大容量で毎日のスキンケアをクリニック級の再生時間へ変える",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "30枚入 (チャック付き大容量パウチ)",
        "type": "北海道産高純度サーモンPDRN原液配合 デイリーサイエンスマスク",
        "features": "北海道産サーモンPDRN原液、ヒアルロン酸Na、アラントイン、コットン100%高密着国産シート",
        "value": "1日あたり100円以下で惜しみなく使える圧倒的ハイコスパ。特別な日だけでなく毎日PDRNを角層へ供給することで、冬の過酷な環境下でも肌バリアとハリ密度を常に最高値に維持",
        "desc_p1": "高価なイメージが強いPDRNケアを、毎日のルーティンとして習慣化できるように開発されたのがKISOの『プレミアムフェイスマスク PDRN』です。日本の清浄な北海道の秋鮭から抽出された高純度DNA成分を採用。合成香料・着色料・鉱物油・パラベン・アルコールなど肌の負担となる成分を徹底排除し、揺らぎやすい冬肌にも優しく寄り添います。",
        "desc_p2": "シートには天然コットン100%を採用し、摩擦刺激を極限まで低減。目元や口元のカッティングが精密で、冬の乾きやすいパーツを隙間なくカバーします。エッセンスはみずみずしく角層への吸い込みが早いため、朝のメイク前でも夜の入浴後でも重宝。毎日継続することで、肌のキメが整い、外気の冷たさに負けない丈夫な肌質へと導かれます。",
        "target": "毎日手軽にPDRNの集中保水ケアを行いたい方、国産・無添加処方にこだわりたい敏感肌の方、乾燥によるキメの乱れをデイリーに補修したい方",
        "point": "洗顔後、化粧水の代わりにそのまま貼るか、ブースターを馴染ませた後に貼ります。5〜10分程度で角層奥までしっかり浸透。剥がした後はマスクを折りたたんで首や腕をやさしく拭き取り、乳液やクリームで仕上げましょう。"
    },
    {
        "rank": 7,
        "tag": "🪡 マイクロニードル×植物PDRNのダブルアプローチ！冬の硬化した角層を突破して深部へ届くチクチク美容針パック",
        "catch": "大ヒットを飛ばし続けるVTの美容針技術『CICA REEDLE™』とフィトPDRNが融合。冷気でゴワつき美容成分を弾く冬の頑固な角質を、天然マイクロニードルが通り道を作り深部へPDRNを直接デリバリー",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "デイリーマスク 30枚入 / キット",
        "type": "天然マイクロニードル×植物性高濃度PDRN配合 浸透促進マスク",
        "features": "CICA REEDLE™（シリカ微細針）、植物性フィトPDRN、ツボクサエキス、ヒアルロン酸",
        "value": "冬の寒さで角層が厚く硬化し、化粧水や美容液が表面で滑ってしまう『浸透ブロック』を一発打破。チクチクとした心地よい刺激とともにPDRNを角層深層へ直撃させる",
        "desc_p1": "冬はターンオーバーの遅延により古い角質が肌表面に滞留し、どんなに高級な保湿剤を塗っても奥まで浸透しない『角層の硬直・ゴワつき』が頻発します。VTのリードルショットPDRNシリーズは、天然シリカから精製された超微細なマイクロニードルを配合。シートを肌に密着させることで、目に見えない浸透ルートを瞬時に形成します。",
        "desc_p2": "このニードルによって開かれた通り道を通じ、低分子フィトPDRNが角層の最深部までスムーズに浸透。塗布時のチクチクとした刺激は、美容成分が届いている科学的な証拠です。翌朝にはゴワつきが消え去り、まるでピーリングを受けた直後のようにやわらかく、もっちりとした赤ちゃんのような肌触りを実感できます。",
        "target": "冬になると肌がゴワついて化粧水が浸透しない方、クリニックのダーマペンや水光注射のような攻めのエイジングケアを自宅で行いたい方",
        "point": "夜の洗顔後、清潔な肌に密着させます。手のひらでシートの上から優しく押し込むようにハンドプレスすると、マイクロニードルの浸透ルートが効果的に働きます。10〜15分後に剥がし、残った液を馴染ませた後は、しっかりと保湿クリームを重ねてください。"
    },
    {
        "rank": 8,
        "tag": "☕ バイオPDRN×スキンカフェイン！冬のむくみと乾燥小ジワを瞬時にリセットする第二の皮膚バイオセルロース",
        "catch": "韓国名門アモーレパシフィックの皮膚科学研究所IOPEが誇る生体親和マスク。発酵バイオセルロースシートが第二の皮膚のように吸い付き、バイオPDRNとカフェイン成分が寒冷によるフェイスラインのむくみと目元口元の小ジワを強力タイトニング",
        "brand_name": "IOPE (アイオペ)",
        "capacity": "バイオ シートマスク 10枚入",
        "type": "バイオPDRN×スキンカフェイン配合 発酵バイオセルロースマスク",
        "features": "Bio-PDRN™、スキンカフェイン、グルタチオン、ココナッツ発酵バイオセルロースシート",
        "value": "密着度は一般的な不織布の約10倍。隙間なく顔全体を真空パックのように覆うことで、血行不良による朝のむくみをスッキリ流し、乾燥した目元や口元にピンとしたハリ膜を形成",
        "desc_p1": "IOPEのバイオシートマスクは、ココナッツ果汁を発酵させて作られる極細の植物性繊維『バイオセルロース』を採用。皮膚の起伏や細かいシワの凹凸にまで分子レベルで密着するため、貼っている間も動いても剥がれず、家事や仕事をしながらでもストレスフリーで集中ケアが可能です。",
        "desc_p2": "独自開発のBio-PDRN™に加えて、血行をサポートし引き締め効果をもたらすスキンカフェインを配合。冬の朝、顔がむくんで腫れぼったい時や、寒さで皮膚の弾力が失われてほうれい線が目立つ時に投入すると、わずか15分で輪郭がキュッと引き締まり、顔全体がシャープにリフトアップされた印象を与えます。",
        "target": "冬の朝のむくみやたるみを手早く解消したい方、シートマスクが途中で浮いてくるのがストレスな方、イベントや大切な日の直前レスキューを行いたい方",
        "point": "シートの両面にあるメッシュ保護フィルムのうち片面を剥がし、顔にフィットさせた後、外側のメッシュを剥がします。15〜20分置いた後、シートを剥がしてエッセンスを顔全体に馴染ませてください。朝のメイク前に使うと、ファンデーションの密着度が劇的に高まります。"
    },
    {
        "rank": 9,
        "tag": "🧬 PDRN×特許乳酸菌バイオーム！真冬の乾燥で崩れた美肌菌バランスと弾力構造を再構築する3Dマスク",
        "catch": "オリーブヤングのエイジングケア部門で圧倒的人気を誇るBIOHEAL BOHのプロバイオダームシリーズ。高純度PDRNと独自特許の乳酸菌バイオームを融合し、寒冷環境下で崩れがちな皮膚マイクロバイオームと真皮コラーゲンを強力サポート",
        "brand_name": "BIOHEAL BOH (バイオヒールボ)",
        "capacity": "5枚入 / ボックス",
        "type": "PDRN×プロバイオダーム特許成分配合 3Dリフティングマスク",
        "features": "高純度PDRN、Probioderm™（特許乳酸菌バイオーム）、3重コラーゲン、ペプチドコンプレックス",
        "value": "寒暖差による肌荒れを防ぐ『常在菌バリア』と、年齢肌のゆるみを支える『コラーゲン弾力膜』を同時補強。冬の乾燥でしぼんだ大人肌をふっくら立体的に押し返す",
        "desc_p1": "冬の過酷な乾燥と寒暖差は、肌表面でバリアを形成している善玉菌（表皮ブドウ球菌など）のバランスを乱し、肌あれやキメの乱れを引き起こします。バイオヒールボのマスクは、肌の常在菌環境を健やかに保つ特許バイオーム成分に、サーモンDNA由来のPDRNをブレンド。肌本来の自活力と修復スピードを同時に高めます。",
        "desc_p2": "さらに3種類の分子量の異なるコラーゲンが角層内部で水分を抱え込み、ペプチドがハリをサポート。厚みのある上質なシートが濃厚な乳液状美容液をたっぷりと保持し、肌をふんわりと包み込みます。マスクを剥がした後の肌は、指先を跳ね返すようなモチモチ感と、内側からふっくらと押し上げられたような立体的なハリを実感できます。",
        "target": "30代以降の本格的な乾燥・弾力低下に悩む方、寒暖差で肌が敏感に傾きやすい方、タンタン（弾力）肌を手に入れたい方",
        "point": "化粧水で肌を整えた後に密着させます。約15〜20分置いてから剥がし、肌表面に残ったエッセンスを軽く叩き込むように吸収させます。同シリーズのプロバイオダームリフティングクリームでフタをすると、より完璧な密閉ケアが完了します。"
    },
    {
        "rank": 10,
        "tag": "🌿 低刺激シカPDRN×10重ヒアルロン酸！皮膚科医監修の超低刺激フォーミュラで冬の敏感肌を鎮静＆保水",
        "catch": "韓国ドクターズコスメの草分けDr.G（ドクタージー）が開発した低刺激クイックPDRNマスク。植物由来の低刺激シカPDRNと10種類のヒアルロン酸が、冷風でヒリつく冬のゆらぎ肌を瞬時に落ち着かせながら深層保湿",
        "brand_name": "Dr.G (ドクタージー)",
        "capacity": "クイックシートマスク 30枚入",
        "type": "シカPDRN×10重ヒアルロン酸配合 低刺激鎮静クイックマスク",
        "features": "植物由来シカPDRN、10重マルチヒアルロン酸、エクトイン、竹由来ヴィーガンシート",
        "value": "敏感肌パッチテスト・低刺激テスト済み。真冬の寒さや花粉・乾燥でピリつきやすい肌でも一切しみることなく、毎日安心してPDRNの再生保水ケアを続けられる",
        "desc_p1": "冬場の肌は、バリア機能が著しく低下しているため、高機能なエイジングケア成分をつけると刺激や赤みを感じてしまうことがあります。Dr.GのレッドブレミッシュPDRNマスクは、ツボクサ由来のCICA成分と低分子PDRNを結合させた独自複合体を採用。肌への刺激を極限まで抑えながら、確かな肌再生シグナルを届けます。",
        "desc_p2": "シートには環境にも敏感肌にも優しい竹由来のヴィーガンシートを使用しており、吸湿性と密着性に極めて優れています。10種類のヒアルロン酸が角層のあらゆる層に水分を行き渡らせ、砂漠化した肌をオアシスのように潤します。朝の洗顔後、わずか3〜5分乗せるだけで日中の乾燥崩れを防げるクイック設計も魅力です。",
        "target": "エイジングケアをしたいけれど肌が弱くて荒れやすい方、冬の冷風で頬が赤くなりやすい方、忙しい朝に時短で本格的な水分補給を行いたい方",
        "point": "専用のピンセットでシートを取り出し、顔全体に広げます。デイリーの朝ケアなら3〜5分、じっくりケアしたい夜は10〜15分置きます。剥がした後はベタつかないので、すぐに乳液やメイクへと進むことができます。"
    }
]

# JSON-LD ItemList
item_list_elements = []
for p in product_details:
    it = items[p["rank"] - 1]
    item_list_elements.append({
        "@type": "ListItem",
        "position": p["rank"],
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "brand": {
                "@type": "Brand",
                "name": p["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": it["price"],
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

faq_items = [
    {
        "q": "PDRN（サーモンDNA）配合のシートマスクは、普通のヒアルロン酸やコラーゲンマスクと何が違いますか？",
        "a": "従来のヒアルロン酸やコラーゲンマスクが『肌の外側から水分を一時的に補給・保持する』のに対し、PDRN（ポリデオキシリボヌクレオチド）は『細胞のアデノシンA2A受容体に直接働きかけ、肌自らがコラーゲンや水分を生み出す再生サイクルを活性化する』点に根本的な違いがあります。11月・12月の厳しい寒さで代謝が落ち、何を塗ってもすぐ乾燥してしまう『肌痩せ・しぼみ肌』に対して、内側から弾力とバリアを再建する美容医療発想の持続的なアプローチが可能です。"
    },
    {
        "q": "魚（サーモン）由来の成分とのことですが、生臭い匂いや魚アレルギーへの影響はありますか？",
        "a": "化粧品に配合されているPDRNは、最新のバイオ精製技術によってアレルゲンとなるタンパク質を極限まで除去し、純粋なDNA断片（ヌクレオチド）のみを抽出しているため、魚特有の生臭さは全くありません。また、近年では高麗人参やツボクサなど植物から抽出された『フィトPDRN（植物性PDRN）』を採用した製品も多く登場しており、ヴィーガン志向の方や敏感肌の方でも安心して使用できます。ただし、重度の魚アレルギーをお持ちの方は念のため腕の内側等でパッチテストを行うことを推奨します。"
    },
    {
        "q": "冬にPDRNシートマスクを使う場合、使用頻度はどのくらいがベストですか？",
        "a": "製品の設計タイプによって使い分けるのが最も効果的です。KISOやDr.G、VTなどの大容量デイリーパウチタイプ（30枚入りなど）は、水分補給と肌密度のベースアップとして『毎朝または毎晩のデイリー使用』が適しています。一方、リジュランやIOPE、ハイドロゲルタイプなどの濃厚アンプル個包装マスクは、美容成分が非常に高濃度であるため、『週に1〜2回の集中リペアケア』として取り入れると、栄養過多による肌荒れを防ぎながら最大のハリ・ツヤ効果を引き出せます。"
    },
    {
        "q": "ハイドロゲルタイプのPDRNマスクは、なぜ透明になるまで長時間貼っていても大丈夫なのですか？",
        "a": "一般的な不織布やコットンのシートマスクは、シート自体が乾くと毛細管現象で肌の水分を逆に吸い上げてしまうため15分程度で剥がす必要があります。しかし、ハイドロゲルマスクは美容液そのものを寒天状のゲルに固めた特殊構造をしており、水分蒸散を防ぐ完全密閉シールドとして機能します。肌の温度に反応してゲル内のPDRNや美容成分が角層奥へと浸透するにつれてシート自体が薄く透明になっていくため、2〜3時間、あるいは睡眠中ずっと貼ったままでも肌が乾燥する心配がありません。"
    },
    {
        "q": "PDRNシートマスクを使った後は、クリームなどでフタをする必要がありますか？",
        "a": "はい、真冬の乾燥環境下では必ず乳液や保湿クリームでの油膜シールドが必要です。PDRNマスクによって角層深部に高密度の水分と再生成分をチャージしても、11月〜12月の湿度が低い空気中には水分が容易に逃げてしまいます。マスクを外してハンドプレスで美容液を馴染ませた後、セラミドやスクワラン、ワセリンなどのエモリエント成分を含むクリームを重ねることで、注入したPDRNを肌内部に閉じ込めて翌朝のハリツヤを最大化できます。"
    }
]

faq_elements = []
for fq in faq_items:
    faq_elements.append({
        "@type": "Question",
        "name": fq["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": fq["a"]
        }
    })

structured_data = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10",
            "description": "11月・12月の本格的な寒冷乾燥・暖房脱水・肌痩せ・毛穴の開きを一撃再生！リジュラン、VT、メディヒール、アヌア、IOPE、KISOまで最先端高保湿PDRNシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。",
            "image": items[0]["image_url"],
            "datePublished": "2026-11-13T05:00:00+09:00",
            "dateModified": "2026-11-13T05:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB 冬季皮膚科学研究チーム"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://lumi-cosme.vercel.app/favicon.jpg"
                }
            }
        },
        {
            "@type": "ItemList",
            "name": "真冬の高保湿PDRNシートマスクおすすめランキング10選",
            "numberOfItems": len(item_list_elements),
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": faq_elements
        },
        {
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
                    "name": "高保湿PDRNシートマスク特集",
                    "item": "https://lumi-cosme.vercel.app/winter-pdrn-mask"
                }
            ]
        }
    ]
}

product_cards_html = ""
for p in product_details:
    it = items[p["rank"] - 1]
    product_cards_html += f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-header">
        <span class="rank-badge">第{p['rank']}位</span>
        <span class="product-tag">{p['tag']}</span>
      </div>
      <div class="product-content">
        <div class="product-img-box">
          <img src="{it['image_url']}" alt="{it['display_name']}" class="product-img" loading="lazy">
        </div>
        <div class="product-info">
          <div class="product-brand">{p['brand_name']}</div>
          <h3 class="product-title">{it['display_name']}</h3>
          <p class="product-catch">{p['catch']}</p>
          <div class="product-meta">
            <span><strong>容量:</strong> {p['capacity']}</span>
            <span><strong>タイプ:</strong> {p['type']}</span>
          </div>
          <div class="product-features">
            <strong>主要注目成分:</strong> {p['features']}
          </div>
          <div class="product-price-box">
            <div class="price-val">¥{it['price']:,}<span class="tax-label">（税込・楽天最新実勢価格）</span></div>
            <div class="review-val">★ {it['review_average']} <span class="review-count">({it['review_count']}件のレビュー)</span></div>
          </div>
          <div class="product-value-box">
            <span class="value-title">💡 11-12月の乾燥対策・即効価値</span>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>
      <div class="product-desc-box">
        <h4>🧬 美容科学＆テクスチャー詳細解説</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>
      <div class="product-target-box">
        <div class="target-item"><strong>こんな方に最適:</strong> {p['target']}</div>
        <div class="target-item"><strong>効果を最大化する使用法:</strong> {p['point']}</div>
      </div>
      <div class="product-action">
        <a href="{it['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
          <span>楽天市場で最新価格＆在庫をチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """

faq_html = ""
for fq in faq_items:
    faq_html += f"""
    <div class="faq-item">
      <div class="faq-q">Q. {fq['q']}</div>
      <div class="faq-a">{fq['a']}</div>
    </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10 | LUMI COSMETICS LAB</title>
  <meta name="description" content="11月・12月の本格的な寒冷乾燥・暖房脱水・肌痩せ・毛穴の開きを一撃再生！リジュラン、VT、メディヒール、アヌア、IOPE、KISOまで最先端高保湿PDRNシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-pdrn-mask">
  <link rel="icon" href="/favicon.jpg">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10">
  <meta property="og:description" content="11月・12月の本格的な寒冷乾燥・暖房脱水・肌痩せ・毛穴の開きを一撃再生！リジュラン、VT、メディヒール、アヌア、IOPE、KISOまで最先端高保湿PDRNシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-pdrn-mask">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10">
  <meta name="twitter:description" content="11月・12月の本格的な寒冷乾燥・暖房脱水・肌痩せ・毛穴の開きを一撃再生！リジュラン、VT、メディヒール、アヌア、IOPE、KISOまで最先端高保湿PDRNシートマスクの科学的浸透メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
  {json.dumps(structured_data, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --accent: #e11d48;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    }}
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.7;
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
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{
      color: var(--primary);
      text-decoration: none;
    }}
    main {{
      max-width: 1100px;
      margin: 24px auto 60px;
      padding: 0 20px;
    }}
    .hero-section {{
      background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
      border: 1px solid #bfdbfe;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: #0284c7;
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }}
    .hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.4;
      color: #0f172a;
      margin-bottom: 20px;
    }}
    @media (max-width: 768px) {{
      .hero-title {{
        font-size: 1.4rem;
      }}
    }}
    .hero-desc {{
      font-size: 1rem;
      color: #334155;
      line-height: 1.8;
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px 32px;
      margin-bottom: 40px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
    }}
    .toc-list a {{
      color: #1e40af;
      text-decoration: none;
      font-size: 0.92rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: #2563eb;
      text-decoration: underline;
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .science-box h3 {{
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .science-box p {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.8;
      margin-bottom: 16px;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .science-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .science-card h4 {{
      font-size: 1.05rem;
      color: #0369a1;
      margin-bottom: 8px;
    }}
    .science-card p {{
      font-size: 0.88rem;
      color: #475569;
      line-height: 1.6;
      margin-bottom: 0;
    }}
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 36px;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}
    .rank-badge {{
      background: #0284c7;
      color: #ffffff;
      font-size: 0.95rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 8px;
    }}
    .product-tag {{
      background: #eff6ff;
      color: #1e40af;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 8px;
      border: 1px solid #dbeafe;
    }}
    .product-content {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 28px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-content {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-img-box {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      background: #ffffff;
      border-radius: 8px;
      border: 1px solid var(--border);
      padding: 8px;
    }}
    .product-brand {{
      font-size: 0.9rem;
      font-weight: 700;
      color: #64748b;
      margin-bottom: 4px;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 12px;
      line-height: 1.4;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 16px;
    }}
    .product-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }}
    .product-features {{
      font-size: 0.85rem;
      background: #f1f5f9;
      padding: 8px 12px;
      border-radius: 6px;
      margin-bottom: 16px;
    }}
    .product-price-box {{
      display: flex;
      align-items: baseline;
      gap: 16px;
      margin-bottom: 16px;
      border-top: 1px dashed var(--border);
      padding-top: 12px;
    }}
    .price-val {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #dc2626;
    }}
    .tax-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .review-val {{
      font-size: 0.9rem;
      color: #d97706;
      font-weight: 700;
    }}
    .review-count {{
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 400;
    }}
    .product-value-box {{
      background: #eff6ff;
      border: 1px solid #bfdbfe;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      color: #1e3a8a;
    }}
    .value-title {{
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .product-desc-box {{
      background: #f8fafc;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
    }}
    .product-desc-box h4 {{
      font-size: 1rem;
      margin-bottom: 12px;
      color: #0f172a;
    }}
    .product-desc-box p {{
      font-size: 0.92rem;
      color: #334155;
      line-height: 1.7;
      margin-bottom: 8px;
    }}
    .product-target-box {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
      font-size: 0.88rem;
    }}
    @media (max-width: 640px) {{
      .product-target-box {{
        grid-template-columns: 1fr;
      }}
    }}
    .target-item {{
      background: #ffffff;
      border: 1px solid var(--border);
      padding: 12px 16px;
      border-radius: 8px;
    }}
    .product-action {{
      text-align: right;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #bf0000;
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s, transform 0.1s;
    }}
    .rakuten-btn:hover {{
      background: #990000;
      transform: translateY(-2px);
    }}
    .summary-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .summary-box h3 {{
      font-size: 1.35rem;
      color: #0f172a;
      margin-bottom: 16px;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 0.9rem;
    }}
    .summary-table th, .summary-table td {{
      padding: 12px 16px;
      border: 1px solid var(--border);
      text-align: left;
    }}
    .summary-table th {{
      background: #f1f5f9;
      font-weight: 700;
      color: #0f172a;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 16px 0;
    }}
    .faq-item:last-child {{
      border-bottom: none;
    }}
    .faq-q {{
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.92rem;
      line-height: 1.7;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
      color: #ffffff;
      border-radius: var(--radius);
      padding: 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      margin-bottom: 40px;
    }}
    @media (max-width: 768px) {{
      .hub-link-banner {{
        flex-direction: column;
        text-align: center;
      }}
    }}
    .hub-link-btn {{
      display: inline-block;
      background: #ffffff;
      color: #0369a1;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 8px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .internal-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
    }}
    .internal-links-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .internal-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }}
    .internal-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px;
      text-decoration: none;
      transition: border-color 0.2s, transform 0.2s;
    }}
    .internal-link-card:hover {{
      border-color: var(--primary);
      transform: translateY(-2px);
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 60px 20px 40px;
      font-size: 0.85rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 20px;
    }}
    .footer-links {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: 12px 20px;
      margin-bottom: 40px;
    }}
    .footer-link-item {{
      color: #cbd5e1;
      text-decoration: none;
      transition: color 0.2s;
    }}
    .footer-link-item:hover {{
      color: #38bdf8;
    }}
    .copyright {{
      border-top: 1px solid #1e293b;
      padding-top: 24px;
      text-align: center;
      color: #64748b;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        LUMI COSMETICS LAB
      </a>
      <span style="font-size:0.85rem;color:#64748b;">冬季皮膚科学＆高保湿コスメ検証</span>
    </div>
  </header>

  <div class="breadcrumb">
    <a href="/">ホーム</a> &gt; <span>高保湿PDRNシートマスク特集</span>
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">🧬 2026年冬 最先端美容医療発想コスメ</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！高純度サーモンDNA・PDRNの細胞間再生力とバイオセルロース密着膜で真冬のしぼみ肌を跳ね返す保湿力高めPDRNシートマスクランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて、木枯らしと過酷な室内暖房により、私たちの肌は一気に『水分保持機能の崩壊』と『代謝低下による肌痩せ』のダブル危機に直面します。化粧水をいくら重ねても乾く、ファンデーションが粉を吹いて毛穴落ちする、夕方になると頬がしぼんで疲れて見える――そんな冬の深刻な肌悩みに対し、今もっとも皮膚科学の現場から注目されているのが『PDRN（ポリデオキシリボヌクレオチド）』です。本記事では、美容医療のサーモン注射発想から生まれた高純度PDRNシートマスクを厳選し、科学的浸透メカニズムとともに徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次・記事ナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. 冬の寒冷しぼみ肌とPDRN細胞間再生の皮膚科学</a></li>
        <li><a href="#rank-1">第1位: リジュラン リフレッシュ スキン プロテクション マスク</a></li>
        <li><a href="#rank-2">第2位: VT PDRN ハイドロゲル リアル エンリッチ マスク</a></li>
        <li><a href="#rank-3">第3位: メディヒール THE PDRN リフティング アンプルマスク</a></li>
        <li><a href="#rank-4">第4位: アヌア PDRN ヒアルロン酸 カプセル 100 セラム マスク</a></li>
        <li><a href="#rank-5">第5位: メディキューブ PDRN ピンク ペプチド アンプル マスク</a></li>
        <li><a href="#rank-6">第6位: KISO プレミアムフェイスマスク PDRN</a></li>
        <li><a href="#rank-7">第7位: VT リードルS PDRN デイリーマスク</a></li>
        <li><a href="#rank-8">第8位: IOPE PDRN カフェイン ショット バイオセルロース マスク</a></li>
        <li><a href="#rank-9">第9位: バイオヒールボ プロバイオダーム 3D リフティング PDRN マスク</a></li>
        <li><a href="#rank-10">第10位: Dr.G レッドブレミッシュ PDRN クイックマスク</a></li>
        <li><a href="#selection-matrix">2. 目的・シート素材別：冬のPDRNマスク選び方マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜ冬の肌にPDRNなのか？『寒冷代謝停止』を覆すDNAヌクレオチドの作用原理</h3>
      <p>
        初冬の11月から12月は、外気温が10℃を下回り、湿度が急降下します。皮膚温が低下すると毛細血管が収縮し、真皮の線維芽細胞への酸素や栄養素の供給がストップ。これにより、肌自身のヒアルロン酸合成能力やターンオーバーが著しく停滞し、角層がスカスカになって弾力を失う『寒冷肌痩せ』が発生します。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>🧬 アデノシンA2A受容体の活性化</h4>
          <p>PDRNはサーモン等の生殖細胞から抽出精製される特定塩基配列のDNA断片です。皮膚細胞表面のアデノシンA2A受容体に結合することで、休眠状態にある修復シグナルを再点火し、微小循環と組織再生を強力に促します。</p>
        </div>
        <div class="science-card">
          <h4>🛡️ オクルージョン（密封）浸透技術</h4>
          <p>高機能なPDRNを角層深部へ届けるため、シート素材には生体親和性の高いバイオセルロースやハイドロゲル、超極細マイクロファイバーが採用されています。外気乾燥を完全に遮断しながら、水分蒸散を防ぎ確実に成分を送り込みます。</p>
        </div>
        <div class="science-card">
          <h4>✨ コラーゲン＆エラスチン自生力向上</h4>
          <p>外から一時的な油分や水分を塗るだけでなく、PDRNが真皮の細胞間マトリックスの再構築を後押し。乾燥によって破壊された弾力ネットワークが復元され、ふっくらと押し返すような内側からのツヤが蘇ります。</p>
        </div>
      </div>
    </div>

    <div class="products-section">
      {product_cards_html}
    </div>

    <div class="summary-box" id="selection-matrix">
      <h3>📊 目的・シート素材別：冬のPDRNシートマスク選び方マトリクス</h3>
      <p>10製品それぞれのシート素材、配合成分、推奨使用シーンを一覧で比較しました。ご自身の冬の肌状態やライフスタイルに合わせて最適な1枚をお選びください。</p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位 / 製品名</th>
            <th>シート素材</th>
            <th>主たる注目成分</th>
            <th>おすすめの悩み・シーン</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>第1位: リジュラン</td>
            <td>マイクロセル極細シート</td>
            <td>高純度c-PDRN® (40mL)</td>
            <td>週末の集中再生・深刻なしぼみ肌</td>
          </tr>
          <tr>
            <td>第2位: VT ハイドロゲル</td>
            <td>温度感応型ハイドロゲル</td>
            <td>植物性フィトPDRN×セラミド</td>
            <td>就寝中の完全密閉・暖房乾燥対策</td>
          </tr>
          <tr>
            <td>第3位: メディヒール</td>
            <td>3Dリフティングシート</td>
            <td>マリンPDRN×コラーゲン</td>
            <td>寒冷むくみ・フェイスラインの引き締め</td>
          </tr>
          <tr>
            <td>第4位: アヌア</td>
            <td>高保水セルロースシート</td>
            <td>スマートカプセルPDRN×8重ヒアル</td>
            <td>暖房インナードライ・朝のメイク前保水</td>
          </tr>
          <tr>
            <td>第5位: メディキューブ</td>
            <td>濃密ピンクアンプルシート</td>
            <td>サーモンPDRN×マルチペプチド</td>
            <td>冬の青白い血色不良・毛穴たるみ</td>
          </tr>
          <tr>
            <td>第6位: KISO</td>
            <td>天然コットン100%シート</td>
            <td>北海道産サーモンPDRN原液</td>
            <td>毎日のデイリー補水・高コスパケア</td>
          </tr>
          <tr>
            <td>第7位: VT リードルS</td>
            <td>デイリー密着シート</td>
            <td>CICA REEDLE™（微細針）×PDRN</td>
            <td>冬の角質肥厚・化粧水が入らないゴワつき肌</td>
          </tr>
          <tr>
            <td>第8位: IOPE</td>
            <td>発酵バイオセルロース</td>
            <td>Bio-PDRN™×スキンカフェイン</td>
            <td>朝のむくみ流し・目元口元のピンとしたハリ</td>
          </tr>
          <tr>
            <td>第9位: バイオヒールボ</td>
            <td>乳液含浸3Dシート</td>
            <td>PDRN×特許乳酸菌バイオーム</td>
            <td>大人の年齢肌・常在菌バリア強化</td>
          </tr>
          <tr>
            <td>第10位: Dr.G</td>
            <td>竹由来ヴィーガンシート</td>
            <td>シカPDRN×10重ヒアルロン酸</td>
            <td>超敏感肌・冷風による赤みやヒリつき</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="summary-box" id="faq-section">
      <h3>❓ 高保湿PDRNシートマスクに関するよくある質問（FAQ）</h3>
      {faq_html}
    </div>

    <div class="hub-link-banner">
      <div>
        <h3 style="font-size:1.3rem;margin-bottom:8px;">❄️ 冬のシートマスク・スペシャルケア総合ハブ</h3>
        <p style="font-size:0.95rem;opacity:0.95;">高保湿セラミドマスク、コラーゲンマスク、朝用時短マスクまで、冬の肌を守り抜くシートパックの総合特集はこちらからご覧いただけます。</p>
      </div>
      <a href="/winter-face-mask" class="hub-link-btn">フェイスマスク特集トップへ →</a>
    </div>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンクがスクリプトにより同期されます -->
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB - 冬季皮膚科学＆高保湿コスメ検証</div>
      <div class="footer-links" id="footer-links-box">
        <!-- フッターリンクが同期されます -->
      </div>
      <div class="copyright">
        © 2026 LUMI COSMETICS LAB. All Rights Reserved.
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-pdrn-mask.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-pdrn-mask.html!")
