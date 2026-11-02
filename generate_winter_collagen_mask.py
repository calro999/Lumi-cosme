import json
import re

with open("fetched_perfect_3articles_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_collagen_mask"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計2000万枚突破！白から透明に変わる元祖オーバーナイト・リアルディープマスク",
        "catch": "超低分子コラーゲン×ガラクトミセス。朝まで貼って寝るだけで翌朝の肌が陶器のように輝く",
        "brand_name": "BIODANCE (バイオダンス)",
        "capacity": "4枚 / 8枚 / 16枚入",
        "type": "オーバーナイト・ハイドロゲルコラーゲンマスク",
        "features": "243Da超低分子コラーゲン、ガラクトミセス発酵濾過物、オリゴヒアルロン酸、アロエベラ葉エキス",
        "value": "世界中で空前のメガヒットを記録したバイオコラーゲンマスクのパイオニア。美容成分そのものを固めたゲルシートが、3〜4時間かけて角層に溶け込むように浸透",
        "desc_p1": "冬の就寝中、エアコン暖房をつけっぱなしにして眠ると、寝室の湿度は朝方には20%台まで低下します。一般的な不織布シートマスクは15分以上貼ると水分が蒸発して逆に肌の水分を奪う『逆浸透現象』が起きますが、その常識を完全に覆したのがBIODANCEの『バイオ コラーゲン リアル ディープ マスク』です。",
        "desc_p2": "シート自体が美容液そのものを固めた肉厚の乳白色ゲルで作られており、肌に乗せて眠ると体温に反応して美容成分が角層奥深くへと移動。徐々にシートが薄くなり、朝起きる頃には完全に透明へと変化します。243Daという極小サイズの低分子コラーゲンとガラクトミセスが、暖房乾燥で開ききったたるみ毛穴をキュッと引き締め、乾燥小ジワをふっくら持ち上げます。朝シートを剥がした瞬間、手のひらが吸い付くようなプルプル感と、ノーファンデでも発光する水光肌に出会えます。",
        "target": "冬の朝起きると肌がパリパリに乾いている方、暖房をつけたまま眠る習慣のある方、毛穴の開きや弾力不足を一晩で集中リセットしたい方",
        "point": "夜の通常のスキンケア（化粧水・美容液・クリーム）をすべて完了させた後、最後のフタとして本シートを密着させて就寝します。最低3時間以上貼ることで乳白色が完全に透明に変わり、美容成分が角層深部へ移行します。"
    },
    {
        "rank": 2,
        "tag": "✨ 塗って寝るだけのコラーゲン保護皮膜！枕移りゼロで一晩中水分を逃さない",
        "catch": "剥がすタイプの密着ラッピング。翌朝ペリペリ剥がすとキメの整った卵肌が現れる",
        "brand_name": "medicube (メディキューブ)",
        "capacity": "75ml",
        "type": "塗るタイプ・コラーゲンナイトラッピングマスク",
        "features": "低分子コラーゲン、エラスチン、セラミドNP、ヒアルロン酸、アデノシン",
        "value": "シートを貼る手間なく顔全体に均一なコラーゲン皮膜を形成。寝相が悪くても剥がれず、枕やシーツを汚さない革新的なオーバーナイト密閉シールド",
        "desc_p1": "『シートマスクを貼ったまま寝ると寝返りで剥がれてしまう』『髪の毛がシートに張り付いて気になる』という悩みに応え、塗るフィルムタイプとして爆発的な支持を集めているのがメディキューブの『コラーゲン ナイト ラッピング マスク』です。",
        "desc_p2": "専用ブラシや指で顔全体に伸ばすと、約15分で透明な極薄コラーゲンフィルムへと変化。肌表面に一切のベタつきを残さずサラサラに乾くため、枕や布団に付着する心配がゼロです。フィルムの内側では一晩中低分子コラーゲンとエラスチンが角層を密閉保湿し、就寝中のエアコン温風による水分の蒸散を100%シャットアウト。翌朝ぬるま湯で優しくペリペリと剥がすか洗い流すだけで、むきたてのエッグスキンのようなツルツル肌が姿を現します。",
        "target": "シートマスクのズレや寝具への付着がストレスな方、顔だけでなく首元までしっかり密閉パックしたい方、朝の洗顔後の透明感にこだわりたい方",
        "point": "夜のお手入れの最後に、顔全体へ均一な厚みで伸ばします。約15分置いて表面が完全に乾いてサラサラになってからベッドに入ってください。翌朝は端から優しくめくるように剥がせます。"
    },
    {
        "rank": 3,
        "tag": "👶 赤ちゃんの肌に多いT3コラーゲンを高濃度配合！塗って剥がす至福のグローマスク",
        "catch": "大人肌が失ったT3ベビーコラーゲンを補給。剥がした瞬間に鏡を見るのが楽しみになる輝き",
        "brand_name": "PESTLO (ペストロ)",
        "capacity": "70ml",
        "type": "ピールオフ・高保湿T3ベビーコラーゲンパック",
        "features": "T3ベビーコラーゲン、加水分解エラスチン、パンテノール、アロエエキス、低刺激ピールオフ処方",
        "value": "赤ちゃんの肌に最も豊富に含まれる『Type3コラーゲン』に着目。加齢と冬の過酷な寒冷によって弾力を失った大人の肌を、もっちりとした柔らかさへ導く",
        "desc_p1": "人間の皮膚に存在するコラーゲンのうち、柔らかさと弾力性を司るのが『Type3（ベビーコラーゲン）』です。加齢とともに激減し、さらに冬の紫外線や寒さで分解が進むと、肌は硬くゴワつき、柔軟性を失ってしまいます。この失われたコラーゲンを集中的にチャージするのがPESTLOの『T3 ベビー コラーゲン グロー マスク』です。",
        "desc_p2": "クリーム状のパックを肌に塗布すると、徐々に透明な美容フィルムへと変化。T3コラーゲンとエラスチンが角質の隙間を密に埋め尽くし、乾燥によって萎縮したキメをふっくらと押し上げます。一般的なピールオフパックのように肌を引っ張って痛める心配がなく、しっとりとした膜がペロンと綺麗に剥がれる設計。剥がした後の肌はまるでエステ帰りのように潤いに満ち、眩しいほどのツヤを放ちます。",
        "target": "肌が硬くスキンケアの浸透が悪く感じる方、赤ちゃんの肌のような柔らかい弾力を取り戻したい方、エステ級の集中保湿ツヤパックを自宅でしたい方",
        "point": "洗顔後、化粧水とアンプルを軽くなじませてから適量を厚めに塗布。20〜30分ほど置いて完全に乾いたら、顔の輪郭から中心に向かって優しく剥がします。その後クリームで仕上げてください。"
    },
    {
        "rank": 4,
        "tag": "🌿 植物性コラーゲンエキスをそのままゲル化！肌の凹凸に吸い付くヴィーガン密着シート",
        "catch": "シートが美容成分そのもの。乾燥による目元・口元の細かな隙間まで隙間なく潤い密封",
        "brand_name": "Abib (アビブ)",
        "capacity": "10枚入",
        "type": "植物性高密着コラーゲンゲルマスク",
        "features": "セダム由来植物性コラーゲン、ジェリコローズ（復活草）エキス、ヒアルロン酸、弱酸性処方",
        "value": "砂漠でも枯れない驚異の保水力を持つ『復活草エキス』と植物性コラーゲンを配合。冬の極限乾燥下でも肌の水分保持力を限界まで引き上げる",
        "desc_p1": "冬のエアコン環境では、目の下や小鼻の脇、口元のほうれい線など、凹凸のある細かなパーツから乾燥が進行します。一般的なシートマスクでは浮いてしまいがちなこれらの部位に、驚異的な吸着力でピタッと張り付くのがAbibの『コラーゲン ゲル マスク』です。",
        "desc_p2": "シート自体がヴィーガン認証を取得した植物性コラーゲンゲルで作られており、上下セパレート構造のため顔の骨格に合わせてミリ単位で密着させることが可能。過酷な砂漠で一滴の水で蘇る『復活草（ジェリコローズ）』エキスが、乾ききった角層細胞に水分をグングン注ぎ込みます。ゲルが体温でじわじわと薄くなりながら潤いを送り続けるため、パック後は頬の毛穴が目立たなくなり、みずみずしい透明感が長時間続きます。",
        "target": "シートマスクが顔のサイズに合わず浮いてしまう方、目元やほうれい線のパーツ乾燥が気になる方、肌に優しいヴィーガン処方を重視する方",
        "point": "上下に分かれているため、まず下半分を口の位置に合わせて密着させ、その後に上半分を額と目の位置に合わせて重ねます。30〜40分じっくり置くことでゲルが透明に近づき、高い密閉効果を発揮します。"
    },
    {
        "rank": 5,
        "tag": "🐯 CICA×低分子コラーゲンで真冬の肌荒れと乾燥をダブル救済！大容量デイリーゲルマスク",
        "catch": "30枚入りの贅沢設計。冬の毎日のスキンケアで揺らぎを鎮静しながらふっくらハリ肌へ",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30枚入",
        "type": "CICAコラーゲン・デイリー大容量マスク",
        "features": "シカヒアルロン、低分子コラーゲン（大豆由来）、ナイアシンアミド、パンテノール",
        "value": "寒暖差やマスク刺激で荒れやすい冬の肌をCICAで整えつつ、コラーゲンで水分を満たす。毎日惜しみなく使えるコスパ最強のコラーゲンマスク",
        "desc_p1": "『週末のスペシャルケアだけでなく、11月・12月は毎日コラーゲンパックをして乾燥を防ぎたい』という美肌派の願いを叶えるのが、VTの『シカ コラーゲン マスク（30枚入）』です。",
        "desc_p2": "VT独自の鎮静成分『CICA HYALON』に低分子コラーゲンを贅沢にドッキング。寒風や暖房による乾燥で赤みが出やすい冬の素肌を素早くクールダウンしながら、角層のすみずみまで濃密な潤いを届けます。極薄の植物性セルロースシートが肌に吸い付くようにフィットし、液だれすることなく密着。大容量のBOXタイプでありながら最後の1枚まで美容液がヒタヒタに含まれており、朝のメイク前や夜のお風呂上がりに毎日手軽に贅沢なコラーゲンチャージが可能です。",
        "target": "毎日手軽にコラーゲンパックを続けたい方、冬になると乾燥と肌荒れ（赤み・吹き出物）が同時に起きる方、朝のメイクノリを良くしたい方",
        "point": "付属のピンセットで1枚取り出し、洗顔後の清潔な肌に10〜15分乗せます。剥がした後は手のひらで肌に残った美容液を優しくハンドプレスし、乳液やクリームで仕上げてください。"
    },
    {
        "rank": 6,
        "tag": "🇯🇵 コーセーの高品質デイリーケア！高純度コラーゲンが角層深部へ浸透するロングセラー",
        "catch": "弱酸性・無香料・無着色。デリケートな冬の肌にも毎日使える安心の国産大容量マスク",
        "brand_name": "CLEAR TURN (クリアターン / コーセー)",
        "capacity": "30回分",
        "type": "国産高純度コラーゲン・デイリーエッセンスマスク",
        "features": "高純度水溶性コラーゲン、トレハロース誘導体、海洋性エラスチン、弱酸性・ノンアルコール",
        "value": "ドラッグストアで手に入る圧倒的な安心感とコスパ。冬の乾燥でゴワつく角質を柔らかくほぐし、みずみずしい潤いを与え続ける国民的マスク",
        "desc_p1": "冬の乾燥対策は継続が命。高価なパックを月に1回使うよりも、毎日の丁寧な保湿こそがバリア機能を強固に保つ秘訣です。そんな毎日のスキンケアの頼れるパートナーが、コーセーコスメポートの『クリアターン エッセンスマスク コラーゲン』です。",
        "desc_p2": "角層柔軟成分と高純度コラーゲンが、寒さで硬くなった冬の肌を優しく解きほぐします。弱酸性・無着色・ノンアルコールの低刺激設計で、肌が敏感になりがちな12月でもピリピリ感なく快適に使用可能。三層構造のマイクロフィットシートが美容液をたっぷり保持し、目元や口元までしっかりカバーします。入浴後のスキンケアに組み込むことで、暖房による夜間の水分蒸発を効果的に予防します。",
        "target": "ドラッグストアで手軽に買える信頼の国産ブランドを好む方、毎日惜しみなく使える大容量パックを探している方、アルコールフリー処方を求める方",
        "point": "お風呂上がりの体が温まっている状態で使用。5〜10分程度密着させた後、シートを折りたたんで首筋やデコルテまでパッティングすると全身の乾燥予防になります。"
    },
    {
        "rank": 7,
        "tag": "🌍 世界的人気MEDIHEALの進化系！加水分解コラーゲン×ペプチドの集中弾力ケア",
        "catch": "竹由来のセルロースシートが肌に吸着。乾くとキュッと引き締まるリフティング設計",
        "brand_name": "MEDIHEAL (メディヒール)",
        "capacity": "30枚入 / 単品",
        "type": "高密着バイオセルロース・コラーゲンエッセンシャルマスク",
        "features": "加水分解コラーゲン、コラーゲンアミノ酸、プロコラーゲンコンプレックス、パンテノール",
        "value": "シートマスクの世界的権威メディヒールが誇るコラーゲンの決定版。加水分解コラーゲンとアミノ酸が冬の小ジワと乾燥たるみに集中的に働きかける",
        "desc_p1": "世界中で愛されるメディヒールのエッセンシャルマスクシリーズの中でも、冬に圧倒的な指名買いを誇るのが『コラーゲン エッセンシャル マスク』です。リニューアルを経てコラーゲン成分の配合量が大幅にアップしました。",
        "desc_p2": "植物由来の竹セルロースシートは、美容液をたっぷりと抱え込み、肌に乗せるとまるで第二の皮膚のようにピタッと一体化。加水分解コラーゲンとプロコラーゲンコンプレックスが角層深部まで素早く行き渡り、冬の寒冷で縮こまった肌細胞をふっくらと膨らませます。シートが乾くにつれて顔全体を心地よく引き上げるリフティング効果もあり、パックを剥がした後のフェイスラインのすっきり感とハリ感は格別です。",
        "target": "シートマスクの実績と品質にこだわりたい方、冬の乾燥小ジワとたるみ毛穴を同時にケアしたい方、しっかりとしたリフティング感を味わいたい方",
        "point": "シートを顔全体に密着させ、頬の切れ込み部分を斜め上に向かって引き上げるように重ねて貼ると、フェイスラインのリフトアップ効果がさらに高まります。"
    },
    {
        "rank": 8,
        "tag": "⚡ 美容針CICA REEDLE×コラーゲンゲル！美容成分の浸透深度を極限まで高める2ステップ",
        "catch": "天然マイクロニードルが角層へ微細な浸透ルートを形成。その上から濃密ゲルでまるごと密封",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "1枚入（2ステップ）",
        "type": "マイクロニードル×ハイドロゲル2ステップマスク",
        "features": "CICA REEDLE（シリカ天然微細針）、低分子コラーゲン、ヒアルロン酸、アミノ酸複合体",
        "value": "爆発的人気のリードルショットとコラーゲンゲルマスクを1枚に凝縮。針のチクチク感で浸透をブーストし、冬枯れ肌を最速で再生するサロン級パック",
        "desc_p1": "『どんなに良い成分を与えても、冬の硬い角質層に浸透していかない』という悩みを、物理的なマイクロニードル技術で打破するのがVTの『リードルショット 100 2ステップ ハイドロゲル マスク』です。",
        "desc_p2": "STEP1のエッセンスに含まれる天然微細針『シリカ』が、角層に美容成分の通り道となる微細な刺激穴を形成。ほんのりとした心地よいチクチク感とともに導入成分が角層奥深くまで届きます。すかさずSTEP2の贅沢なハイドロゲルコラーゲンマスクを乗せることで、針の刺激によって活性化した肌を鎮静しながら、コラーゲンと潤いを深部へ一気に押し込みます。翌朝の肌密度の高さと弾力感は、自宅ケアの領域を超えた感動を与えてくれます。",
        "target": "冬の角質肥厚でスキンケアの入りが悪くなっている方、リードルショットの美肌効果をパックで体感したい方、特別なイベント前夜の集中ケアに",
        "point": "夜の洗顔後、まずSTEP1のリードルショット美容液を顔全体に塗り広げてしっかり馴染ませます。その後すぐにSTEP2のハイドロゲルマスクを乗せ、20〜30分置いてから剥がします。"
    },
    {
        "rank": 9,
        "tag": "🧬 韓国ドクターズコスメの極み！高機能ハイドロゲルシートが角層深部へ高分子を届ける",
        "catch": "ダーマファームの先端リポソーム技術。暖房直撃によるインナードライを根本修復",
        "brand_name": "DERMAFIRM (ダーマファーム)",
        "capacity": "4枚入",
        "type": "高密着バイオコラーゲン・リアルハイドロゲルマスク",
        "features": "超低分子コラーゲン、リポソームペプチド、アズレン、パンテノール、弱酸性",
        "value": "韓国の美容皮膚科でも採用されるドクターズコスメブランド。敏感肌にも使える低刺激ゲルが、冬の過酷な寒暖差で荒れた肌をしっとり鎮静",
        "desc_p1": "冬の寒さと室内暖房の温度差によって、肌は毛細血管の拡張と収縮を繰り返し、赤みが出たり皮脂バランスが崩れたりします。そんな不安定な冬の大人肌を穏やかに整えながら濃密なハリを与えるのが、ダーマファームの『バイオ コラーゲン リアル ハイドロゲル マスク』です。",
        "desc_p2": "肌を鎮静させるアズレン成分と、角層深部まで届くようにナノリポソーム化された低分子コラーゲンを贅沢に配合。ぷるぷるとした厚みのあるゲルシートが肌の熱を優しく吸収しながら、美容成分をじんわりと角層内へ移行させます。シートが透明になっていく過程で肌のキメが整い、毛穴の目立ちや乾燥によるザラつきがリセット。美容医療級のなめらかな陶器肌へと仕上がります。",
        "target": "冬の寒暖差で肌が赤くなりやすい方、皮膚科品質の安全で高機能なゲルマスクを使いたい方、インナードライによるゴワつきを解消したい方",
        "point": "お風呂上がりに化粧水で肌を整えた後、シートを密着させます。最低でも2時間以上、できれば就寝時のオーバーナイトマスクとして使用すると最も高い保水効果が得られます。"
    },
    {
        "rank": 10,
        "tag": "🌿 韓国製薬大手・東国製薬の技術の粋！TECA×加水分解コラーゲンの高保湿シート",
        "catch": "50年の伝統と信頼。冬の頑固な乾燥トラブル・小ジワを濃厚な薬用植物エキスで癒やす",
        "brand_name": "Centellian24 (センテリアン24)",
        "capacity": "10枚入",
        "type": "製薬会社発想・高機能コラーゲンインテンシブマスク",
        "features": "TECA（高純度ツボクサエキス）、加水分解コラーゲン、エラスチン、セラミド、ヒアルロン酸",
        "value": "韓国薬局の定番軟膏マデカソルの主成分を配合。乾燥による皮むけや小ジワを急速に修復し、ふっくらと健康的な肌バリアを再建する",
        "desc_p1": "12月の真冬になると、冷たい北風や暖房の温風によって口周りや頬に粉吹きや皮むけが発生することがあります。角質がめくれ上がったデリケートな肌でも安心して使える集中補修マスクが、センテリアン24の『マデカ ダーマ マスク インテンシブ フォーミュラ』です。",
        "desc_p2": "東国製薬独自の黄金比率で抽出された高純度ツボクサエキス『TECA』が、乾燥による微細な炎症やダメージを鎮静。さらに加水分解コラーゲンとセラミドが壊れたバリア機能を強力に補修し、水分の蒸散をピタッと防ぎます。乳液のように濃厚なミルキーエッセンスがシート全体に染み込んでおり、肌に乗せるとホッとするような濃密な潤いに包まれます。翌朝には粉吹きが収まり、ふっくらと柔らかな素肌が蘇ります。",
        "target": "冬の寒冷乾燥で皮むけや粉吹きが起きている方、製薬会社ブランドの確かな補修力を求める方、こっくりとしたミルキーな保湿感を好む方",
        "point": "洗顔後、化粧水の後にシートを15〜20分密着させます。袋に残った濃厚なエッセンスは首やデコルテ、乾燥しやすい肘・膝にも贅沢に塗り伸ばしてください。"
    }
]

faq_items = [
    {
        "q": "バイオコラーゲンマスクとは何ですか？普通のシートマスクとの最大の違いは？",
        "a": "従来の一般的なシートマスクは、不織布やコットンシートに液状の美容液を含ませたものです。15〜20分以上貼ると水分が蒸散し、逆に肌の水分を奪う『逆浸透現象』が起きます。一方、バイオコラーゲンマスク（リアルディープマスク）は、コラーゲンや美容成分そのものを固めてハイドロゲル化したシートです。肌の体温に反応して美容成分が角層奥深くまで徐々に浸透していくため、3〜4時間、あるいは一晩中貼ったまま眠ることが可能です。成分が肌に吸収されると、白かったシートが徐々に透明へと変化します。"
    },
    {
        "q": "貼ったまま寝ても肌荒れや息苦しさ、ニキビの原因になりませんか？",
        "a": "バイオコラーゲンマスクは高密着でありながら通気性を持つバイオゲル構造で作られており、肌を完全に窒息させることはありません。また、低刺激・弱酸性処方のものが主流です。ただし、重度の脂性肌の方や活動性のニキビがある場合は、長時間の密封によって皮脂がこもる可能性があるため、就寝時ではなく入浴後の2〜3時間の使用から試すことをおすすめします。"
    },
    {
        "q": "冬の就寝中に貼る際、マスクの下には何を塗るべきですか？",
        "a": "バイオコラーゲンマスクは強力な密閉シールド効果（ラッピング効果）を持つため、下地として塗るスキンケアの浸透を大幅に高めます。おすすめの手順は、【洗顔 → 高保湿化粧水 → PDRN美容液やビタミンCアンプル → 軽めの乳液・クリーム → バイオコラーゲンマスク】です。美容液をしっかり仕込んでおくことで、一晩かけてその美容成分もろとも角層深部へ押し込むことができます。"
    },
    {
        "q": "朝起きた後、剥がした後のスキンケアはどうすれば良いですか？",
        "a": "透明になったマスクを端から優しくめくるように剥がします。肌表面にベタつきはほとんど残っておらず、すでに角層深部まで潤いが満ちている状態です。ぬるま湯で軽く顔をすすぎ、その後に通常の朝のスキンケア（化粧水・乳液・日焼け止め）を行ってください。驚くほど化粧ノリが良くなり、ファンデーションが日中まったく粉を吹かなくなります。"
    },
    {
        "q": "使用頻度はどれくらいが理想ですか？毎日使っても大丈夫？",
        "a": "ハイドロゲルタイプのディープマスク（BIODANCEなど）は、週に1〜2回のスペシャルケアとして取り入れるのが最も効果的でコスパにも優れています。乾燥が最も深刻な11月・12月や、大切なイベントの前夜に集中使用するのがおすすめです。なお、大容量タイプのVTシカコラーゲンマスクやクリアターンなどは毎日デイリーに使える設計となっています。"
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
    "headline": "保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10",
    "description": "11月・12月の冬の夜間暖房による砂漠肌・朝の粉吹き・たるみ毛穴を徹底解決！一晩貼って寝るだけで白から透明に変わるバイオコラーゲンリアルディープマスク＆ゲルマスク10選を徹底比較！BIODANCE、メディキューブ、PESTLO、Abib、VT、クリアターン、メディヒールなど、翌朝ぷるん肌が蘇る至高のマスクを厳選。",
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
    "name": "冬の高密着バイオコラーゲンマスク おすすめランキング10選",
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

# 商品カードHTML作成
cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge-wrap">
          <span class="product-rank-badge rank-{p['rank']}">第{p['rank']}位</span>
          <span class="product-tag">{p['tag']}</span>
        </div>
        <div class="product-header">
          <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
          <p class="product-catch">{p['catch']}</p>
        </div>
        <div class="product-layout">
          <div class="product-img-box">
            <img src="{item['image']}" alt="{p['brand_name']} {p['capacity']}" class="product-img" loading="lazy" width="300" height="300">
            <div class="product-price-tag">参考価格: <span>¥{item['price']:,}</span> (税込)</div>
          </div>
          <div class="product-specs">
            <table class="spec-table">
              <tr><th>アイテムタイプ</th><td>{p['type']}</td></tr>
              <tr><th>注目美容成分</th><td>{p['features']}</td></tr>
              <tr><th>期待できる効果</th><td>{p['value']}</td></tr>
              <tr><th>おすすめの肌質</th><td>{p['target']}</td></tr>
            </table>
          </div>
        </div>
        <div class="product-body">
          <div class="product-desc">
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          <div class="product-advice">
            <div class="advice-title">💡 美容コンシェルジュの使いこなしポイント</div>
            <p>{p['point']}</p>
          </div>
        </div>
        <div class="product-action">
          <a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最安値・在庫をチェック
            <svg class="btn-arrow" viewBox="0 0 24 24" width="18" height="18"><path fill="currentColor" d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
          </a>
        </div>
      </article>
""")

comparison_rows = []
for p, item in zip(product_details, items):
    comparison_rows.append(f"""
            <tr>
              <td class="col-rank"><span class="table-rank rank-{p['rank']}">{p['rank']}</span></td>
              <td class="col-thumb"><img src="{item['image']}" alt="{p['brand_name']}" class="table-img" loading="lazy" width="60" height="60"></td>
              <td class="col-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
              <td class="col-type">{p['type']}</td>
              <td class="col-features">{p['features']}</td>
              <td class="col-price">¥{item['price']:,}</td>
              <td class="col-btn"><a href="{item['affiliateUrl']}" target="_blank" rel="nofollow noopener" class="table-btn">楽天詳細</a></td>
            </tr>
""")

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の夜間暖房による砂漠肌・朝の粉吹き・たるみ毛穴を徹底解決！一晩貼って寝るだけで白から透明に変わるバイオコラーゲンリアルディープマスク＆ゲルマスク10選を徹底比較！BIODANCE、メディキューブ、PESTLO、Abib、VT、クリアターン、メディヒールなど、翌朝ぷるん肌が蘇る至高のマスクを厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-collagen-mask">
  <meta name="robots" content="index, follow, max-image-preview:large">
  
  <!-- OGP & SNS -->
  <meta property="og:title" content="保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10">
  <meta property="og:description" content="11月・12月の冬の夜間暖房による砂漠肌・朝の粉吹き・たるみ毛穴を徹底解決！一晩貼って寝るだけで白から透明に変わるバイオコラーゲンリアルディープマスク10選！">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-collagen-mask">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="theme-color" content="#d97706">

  <!-- 構造化データ (JSON-LD) -->
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
      --primary: #d97706;
      --primary-light: #fffbeb;
      --primary-dark: #b45309;
      --text-main: #2d3748;
      --text-sub: #718096;
      --bg-page: #fbfbfc;
      --bg-card: #ffffff;
      --border: #edf2f7;
      --border-focus: #fcd34d;
      --shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      --radius: 16px;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(10px);
      background-color: rgba(255, 255, 255, 0.95);
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.25rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-sub);
    }}
    .breadcrumb a {{ color: var(--text-sub); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .container {{
      max-width: 900px;
      margin: 0 auto;
      padding: 24px 20px 80px;
    }}
    .hero-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
    }}
    .post-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.8rem;
      padding: 6px 14px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }}
    .post-title {{
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.45;
      color: #1a202c;
      margin-bottom: 20px;
      letter-spacing: -0.5px;
    }}
    .post-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: var(--text-sub);
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
    }}
    .intro-text p {{
      margin-bottom: 16px;
      font-size: 1.02rem;
      color: #4a5568;
    }}
    .callout-box {{
      background: #fffbeb;
      border-left: 4px solid var(--primary);
      padding: 20px;
      border-radius: 0 12px 12px 0;
      margin: 24px 0;
    }}
    .callout-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
    }}
    .toc-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 24px;
      margin: 32px 0 48px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px 20px;
    }}
    @media (max-width: 640px) {{
      .toc-list {{ grid-template-columns: 1fr; }}
      .post-title {{ font-size: 1.45rem; }}
      .hero-section {{ padding: 24px 18px; }}
    }}
    .toc-list a {{
      color: #3182ce;
      text-decoration: none;
      font-size: 0.92rem;
    }}
    .toc-list a:hover {{ text-decoration: underline; }}
    
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      margin: 56px 0 24px;
      padding-bottom: 12px;
      border-bottom: 2px solid var(--primary);
      color: #1a202c;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .subsection-title {{
      font-size: 1.25rem;
      font-weight: 700;
      margin: 32px 0 16px;
      color: #2d3748;
    }}
    .content-box {{
      background: #ffffff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }}
    .content-box p {{ margin-bottom: 16px; }}
    .content-box ul, .content-box ol {{
      margin: 16px 0 20px 24px;
      color: #4a5568;
    }}
    .content-box li {{ margin-bottom: 8px; }}

    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      position: relative;
    }}
    .product-badge-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }}
    .product-rank-badge {{
      background: #2d3748;
      color: #ffffff;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 6px 16px;
      border-radius: 9999px;
    }}
    .product-rank-badge.rank-1 {{ background: linear-gradient(135deg, #d97706, #f59e0b); }}
    .product-rank-badge.rank-2 {{ background: linear-gradient(135deg, #4b5563, #9ca3af); }}
    .product-rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #d97706); }}
    .product-tag {{
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 700;
      font-size: 0.85rem;
      padding: 6px 14px;
      border-radius: 8px;
    }}
    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 6px;
    }}
    .product-catch {{
      color: var(--primary);
      font-weight: 700;
      font-size: 0.98rem;
      margin-bottom: 20px;
    }}
    .product-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-layout {{ grid-template-columns: 1fr; }}
    }}
    .product-img-box {{
      text-align: center;
      background: #f8fafc;
      padding: 16px;
      border-radius: 12px;
      border: 1px solid #e2e8f0;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      object-fit: contain;
    }}
    .product-price-tag {{
      margin-top: 12px;
      font-size: 0.9rem;
      color: #718096;
    }}
    .product-price-tag span {{
      color: #e53e3e;
      font-weight: 800;
      font-size: 1.25rem;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 10px 12px;
      border-bottom: 1px solid #edf2f7;
    }}
    .spec-table th {{
      width: 32%;
      background: #f7fafc;
      color: #4a5568;
      font-weight: 600;
      text-align: left;
    }}
    .product-desc {{
      margin-bottom: 20px;
      font-size: 0.98rem;
      color: #4a5568;
    }}
    .product-advice {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
      padding: 18px;
      border-radius: 10px;
      margin-bottom: 24px;
    }}
    .advice-title {{
      font-weight: 700;
      color: #166534;
      margin-bottom: 6px;
      font-size: 0.95rem;
    }}
    .product-advice p {{
      color: #15803d;
      font-size: 0.92rem;
      margin-bottom: 0;
    }}
    .rakuten-btn {{
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, #bf0000, #e60000);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 1.05rem;
      padding: 16px 28px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #a80000, #cc0000);
    }}

    /* 比較表 */
    .table-wrap {{
      overflow-x: auto;
      margin: 24px 0 40px;
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
    }}
    .comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      min-width: 720px;
    }}
    .comparison-table th, .comparison-table td {{
      padding: 14px 12px;
      border-bottom: 1px solid #edf2f7;
      text-align: left;
    }}
    .comparison-table th {{
      background: #f8fafc;
      font-weight: 700;
      color: #4a5568;
    }}
    .table-rank {{
      display: inline-block;
      width: 28px;
      height: 28px;
      line-height: 28px;
      text-align: center;
      border-radius: 50%;
      background: #2d3748;
      color: #fff;
      font-weight: 700;
    }}
    .table-rank.rank-1 {{ background: #f59e0b; }}
    .table-rank.rank-2 {{ background: #9ca3af; }}
    .table-rank.rank-3 {{ background: #d97706; }}
    .table-img {{
      border-radius: 6px;
      border: 1px solid #e2e8f0;
      object-fit: contain;
    }}
    .table-btn {{
      display: inline-block;
      background: #bf0000;
      color: #fff;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.78rem;
      padding: 6px 12px;
      border-radius: 6px;
      white-space: nowrap;
    }}

    /* FAQ */
    .faq-item {{
      background: #ffffff;
      border-radius: 12px;
      border: 1px solid var(--border);
      margin-bottom: 16px;
      padding: 20px;
    }}
    .faq-q {{
      font-weight: 800;
      font-size: 1.05rem;
      color: #1a202c;
      margin-bottom: 10px;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }}
    .faq-q-mark {{
      color: var(--primary);
      font-weight: 900;
    }}
    .faq-a {{
      color: #4a5568;
      font-size: 0.95rem;
      line-height: 1.7;
      padding-left: 24px;
    }}

    /* 内部リンク */
    .related-links-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-top: 24px;
    }}
    @media (max-width: 640px) {{
      .related-links-grid {{ grid-template-columns: 1fr; }}
    }}
    .related-link-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      text-decoration: none;
      color: inherit;
      transition: all 0.2s ease;
      display: block;
    }}
    .related-link-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      border-color: var(--primary);
    }}
    .related-card-tag {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      margin-bottom: 8px;
      background: var(--primary-light);
      color: var(--primary);
    }}
    .related-card-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: #2d3748;
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #1a202c;
      color: #a0aec0;
      padding: 60px 20px 40px;
      font-size: 0.9rem;
    }}
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
    }}
    .footer-title {{
      color: #ffffff;
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 20px;
    }}
    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px 16px;
      margin-bottom: 32px;
    }}
    .footer-links a {{
      color: #cbd5e0;
      text-decoration: none;
      font-size: 0.85rem;
    }}
    .footer-links a:hover {{
      color: #ffffff;
      text-decoration: underline;
    }}
    .copyright {{
      text-align: center;
      border-top: 1px solid #2d3748;
      padding-top: 24px;
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="header-nav">
        <a href="/" style="color: #4a5568; text-decoration: none; font-size: 0.9rem; font-weight: 600;">TOPへ戻る</a>
      </nav>
    </div>
  </header>

  <nav class="breadcrumb" aria-label="パンくずリスト">
    <a href="/">HOME</a> &gt; <span>高密着バイオコラーゲンマスク ランキング</span>
  </nav>

  <main class="container">

    <section class="hero-section">
      <span class="post-badge">2026年最新冬コスメ厳選</span>
      <h1 class="post-title">保湿力の強さで朝の乾燥砂漠肌・毛穴開きとさようなら！寝ている間に角層深部へ溶け込み朝ぷるん肌が蘇る高密着バイオコラーゲンマスクランク10</h1>
      <div class="post-meta">
        <span>執筆・監修: 冬コスメ徹底比較ラボ 編集部</span>
        <span>更新日: 2026年11月02日</span>
        <span>検証基準: 密着持続性・翌朝の保水力・低分子化技術・肌負担レス度</span>
      </div>
      <div class="intro-text">
        <p>11月・12月、真冬の寒さが本格化すると、多くの方が夜間にエアコン暖房を稼働させたまま眠るようになります。しかし、密閉された冬の寝室は、加湿器を設置していても明け方には湿度が20%前後にまで落ち込み、睡眠中の7〜8時間という長大な時間は、肌にとって過酷極まりない<strong>『乾燥砂漠の拷問』</strong>と化します。</p>
        <p>夜に入念に化粧水や高価なナイトクリームを塗りたくっても、朝目覚めた瞬間に『肌がカサカサに突っ張っている』『頬の毛穴がぽっかり開き、Tゾーンだけ脂浮きしている』というインナードライに苦しむ方が後を絶ちません。従来の不織布シートマスクでは、15分を過ぎると乾いたシートが肌の水分を奪い始めるため、就寝中のケアには絶対に使えませんでした。</p>
        <p>この冬の夜間乾燥の壁を完璧に打ち破ったのが、今SNSや美容誌を席巻している<strong>『バイオコラーゲン リアルディープマスク（ハイドロゲルマスク）』</strong>です。美容液そのものをゲル状に固めた特殊シートが一晩中肌に吸い付き、体温で美容成分を角層深部へ送り届けながら、白から透明へと変化。朝剥がした瞬間、まるでエステ直後のような発光する陶器肌へと導いてくれます。</p>
      </div>

      <div class="callout-box">
        <div class="callout-title">📌 なぜ冬の睡眠中にバイオコラーゲンマスクが劇的に効くのか？</div>
        <p>ゲルシートが肌表面に強力な物理的密閉膜（オクルーシブ効果）を形成。暖房による水分蒸発を100%遮断するだけでなく、睡眠中の副交感神経優位な時間帯（肌の細胞修復・ターンオーバーが最も活発になるゴールデンタイム）に合わせて、超低分子コラーゲンが角層の隙間へじわじわと移行し続けるためです。</p>
      </div>

      <div class="toc-box">
        <div class="toc-title">📋 目次</div>
        <ul class="toc-list">
          <li><a href="#why-collagen-mask">1. 冬の睡眠中乾燥の罠とバイオゲルの革新性</a></li>
          <li><a href="#how-to-choose">2. 失敗しないバイオコラーゲンマスクの選び方</a></li>
          <li><a href="#ranking">3. 高密着バイオコラーゲンマスクおすすめランキング10選</a></li>
          <li><a href="#comparison">4. 全10商品スペック比較一覧表</a></li>
          <li><a href="#effective-use">5. 朝まで剥がれない！プロが教えるオーバーナイト装着術</a></li>
          <li><a href="#faq">6. よくある質問 (FAQ)</a></li>
        </ul>
      </div>
    </section>

    <!-- セクション1 -->
    <section id="why-collagen-mask" class="content-box">
      <h2 class="section-title">1. 冬の睡眠中乾燥の罠とバイオゲルの革新性</h2>
      <p>冬の朝の肌コンディションが最悪になってしまう最大の理由は、<strong>『睡眠中の無自覚な水分蒸散（不感蒸泄）』</strong>にあります。</p>
      
      <h3 class="subsection-title">① エアコン暖房による「不感蒸泄」の激増</h3>
      <p>人間は睡眠中、呼気や皮膚から一晩に約500mlもの水分を失っています。冬の暖房の温風が直接肌に当たると、角層表面の水分保持能力を大きく上回るスピードで水分が奪われ、肌内部はカラカラのミイラ状態に陥ります。肌はこれに対抗しようとして過剰な皮脂を分泌するため、『朝起きるとTゾーンはベタつくのに頬はつっぱる』という最悪の冬インナードライが完成します。</p>

      <h3 class="subsection-title">② 一般的なシートマスクが就寝時に絶対NGな理由</h3>
      <p>コットンや不織布のマスクは、水分が蒸発する際に気化熱とともに肌本来の潤いまで奪い去る『逆浸透（水分奪還現象）』を引き起こします。15分以上放置したシートマスクは、肌を潤すどころか乾燥を加速させる危険な凶器となってしまいます。</p>

      <h3 class="subsection-title">③ バイオコラーゲンゲルの「白から透明へ変わる」科学</h3>
      <p>BIODANCEなどに代表されるバイオコラーゲンマスクは、不織布の台紙を一切使わず、高純度コラーゲンエキスとヒアルロン酸そのものをハイドロゲルとして凝固させたものです。肌に密着させると、肌の体温（約36℃）に反応してゲル内の美容成分が分子レベルで角層へ徐々に移行。成分が肌へ吸収されるに伴ってシートの厚みが減り、乳白色から完全な透明フィルムへと変化します。朝まで貼っていても逆浸透が絶対に起きない、冬の夜間ケアの究極の進化形です。</p>
    </section>

    <!-- セクション2 -->
    <section id="how-to-choose" class="content-box">
      <h2 class="section-title">2. 失敗しないバイオコラーゲンマスクの選び方</h2>
      <p>自分にぴったりのバイオコラーゲンマスクを選ぶ際は、以下の3つの基準をチェックしましょう。</p>

      <ul>
        <li><strong>【形状タイプ】シートゲル型か、塗るピールオフ型か：</strong> 最も密着力が高く本格的な水分補給ができるのは貼るシートゲル型（BIODANCE、Abibなど）。寝相が悪くシートが剥がれやすい方や、首元までムラなく密閉したい方には塗るフィルム型（メディキューブ、PESTLO）が便利です。</li>
        <li><strong>【コラーゲンの分子量】：</strong> コラーゲンは分子量が小さければ小さいほど角層の奥深くへと浸透します。243Da（ダルトン）や300Daなど、超低分子化されたコラーゲンを採用している製品は、暖房乾燥で硬くなった肌への浸透実感が格段に違います。</li>
        <li><strong>【サポート美容成分】：</strong> 鎮静重視ならCICAやツボクサエキス（VT、センテリアン24）、毛穴引き締め・キメ重視ならガラクトミセスやペプチド配合（BIODANCE、メディヒール）を選びましょう。</li>
      </ul>
    </section>

    <!-- セクション3: ランキング -->
    <section id="ranking">
      <h2 class="section-title">3. 高密着バイオコラーゲンマスクおすすめランキング10選</h2>
      <p style="margin-bottom: 24px; color: #4a5568;">当ラボ編集部が楽天市場で人気のコラーゲンマスクを厳選検証し、11月・12月の冬枯れ肌をプルプルに蘇らせるおすすめ10選をランキング形式でご紹介します。</p>
      
      {''.join(cards_html)}
    </section>

    <!-- セクション4: 比較表 -->
    <section id="comparison">
      <h2 class="section-title">4. 全10商品スペック比較一覧表</h2>
      <p style="margin-bottom: 16px; color: #4a5568;">横スクロールで各商品の価格・配合成分・特徴をひと目で比較できます。</p>
      <div class="table-wrap">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>画像</th>
              <th>商品名 / 容量</th>
              <th>タイプ</th>
              <th>注目美容成分</th>
              <th>参考価格</th>
              <th>詳細</th>
            </tr>
          </thead>
          <tbody>
            {''.join(comparison_rows)}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション5: 塗り方のコツ -->
    <section id="effective-use" class="content-box">
      <h2 class="section-title">5. 朝まで剥がれない！プロが教えるオーバーナイト装着術</h2>
      <p>就寝中にマスクがズレたり剥がれたりせず、翌朝まで完璧な密着状態をキープするためのプロ直伝のステップです。</p>

      <h3 class="subsection-title">STEP 1: スキンケアのクリームは「薄め」に仕上げる</h3>
      <p>マスクの下に美容液（PDRNやヒアルロン酸）を仕込むのは非常に効果的ですが、油分の多いこってり系ナイトクリームを厚塗りしすぎると、ゲルの吸着力が落ちて滑り落ちやすくなります。クリームは薄く均一に伸ばし、肌表面のベタつきが落ち着いてからゲルマスクを貼りましょう。</p>

      <h3 class="subsection-title">STEP 2: 目と口のくり抜き部分を「小鼻や眉間」に再利用</h3>
      <p>ゲルマスクの目元や口元のくり抜きパーツは捨てずに、乾燥しやすい小鼻の脇や眉間、ほうれい線に貼り重ねましょう。ゲル同士がピタッとくっつき、最も乾燥しやすい部位を集中的にダブル補強できます。</p>

      <h3 class="subsection-title">STEP 3: 最初の20分は仰向けでゲルの密着を安定させる</h3>
      <p>貼った直後はゲルが柔らかく動く可能性があります。就寝直前に貼るのではなく、就寝の20〜30分前に装着してスマホを見たり読書をしたりしながら仰向けでリラックス。体温でゲルが肌に吸い付き安定してからベッドに入ると、朝まで一切ズレることなく密着し続けます。</p>
    </section>

    <!-- セクション6: FAQ -->
    <section id="faq">
      <h2 class="section-title">6. よくある質問 (FAQ)</h2>
      <div class="faq-list">
        {''.join([f'''
        <div class="faq-item">
          <div class="faq-q"><span class="faq-q-mark">Q.</span><span>{item['q']}</span></div>
          <div class="faq-a">{item['a']}</div>
        </div>
        ''' for item in faq_items])}
      </div>
    </section>

    <!-- 内部リンク集 -->
    <section class="content-box" style="margin-top: 48px;">
      <h2 class="section-title" style="margin-top: 0;">あわせて読みたい！冬の乾燥・集中ケア関連記事</h2>
      <div class="related-links-grid">
        <a href="/winter-pdrn-serum" class="related-link-card">
          <span class="related-card-tag">マスク前の仕込みに最適 NEW</span>
          <div class="related-card-title">サーモン注射発想で押し返すハリ！高保湿PDRN美容液おすすめ10選</div>
        </a>
        <a href="/winter-carbonic-shampoo" class="related-link-card">
          <span class="related-card-tag">冬の頭皮冷え・フケ解消 NEW</span>
          <div class="related-card-title">濃密マイクロ炭酸泡で血行促進！冬の高保湿炭酸スカルプシャンプー10選</div>
        </a>
        <a href="/winter-sleeping-mask" class="related-link-card">
          <span class="related-card-tag">夜間集中密閉</span>
          <div class="related-card-title">寝ている間に潤いを閉じ込める！冬のスリーピングマスクおすすめ10選</div>
        </a>
        <a href="/winter-eye-patch" class="related-link-card">
          <span class="related-card-tag">目元集中ハイドロゲル</span>
          <div class="related-card-title">目元のちりめんジワ・乾燥クマを撃退！高保湿ハイドロゲルアイパッチ10選</div>
        </a>
        <a href="/winter-oil-mist" class="related-link-card">
          <span class="related-card-tag">日中暖房・粉吹き対策</span>
          <div class="related-card-title">水分とオイルの黄金比！日中も瞬時に艶肌復活する高保湿オイルインミスト10選</div>
        </a>
        <a href="/winter-night-cream" class="related-link-card">
          <span class="related-card-tag">夜用濃密クリーム</span>
          <div class="related-card-title">朝まで乾かない鉄壁の潤いバリア！高保湿ナイトクリームおすすめ10選</div>
        </a>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-title">冬コスメ徹底比較ラボ - カテゴリ別ランキング</div>
      <div class="footer-links">
        <!-- フッターリンクは後ほど一括スクリプトで最新化されます -->
        <a href="/winter-collagen-mask">バイオコラーゲンマスク</a>
        <a href="/winter-pdrn-serum">高保湿PDRN美容液</a>
        <a href="/winter-carbonic-shampoo">高濃度炭酸シャンプー</a>
        <a href="/winter-oil-mist">高保湿オイルインミスト</a>
        <a href="/winter-carbonic-bath">薬用重炭酸入浴剤</a>
        <a href="/winter-hot-treatment">温感ヘッドスパトリートメント</a>
      </div>
      <div class="copyright">
        &copy; 2026 冬コスメ徹底比較ラボ 編集部. All Rights Reserved.
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open("winter-collagen-mask.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("🎉 Successfully generated winter-collagen-mask.html!")
