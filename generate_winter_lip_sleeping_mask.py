import json
import re

with open("fetched_3new_mask_lip_serum.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_lip_sleeping_mask"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 世界中で3秒に1個売れる伝説の夜用リップ！寝ている間に古い角質を溶かしぷるぷるに蘇生",
        "catch": "韓国アモーレパシフィックが世界に誇る夜用リップマスクの絶対的王者LANEIGE。ビタミンCと抗酸化ベリー成分が睡眠中の乾燥角質を優しく軟化・剥離し、翌朝には生まれたてのふっくら唇へ導く",
        "brand_name": "LANEIGE (ラネージュ)",
        "capacity": "20g (スパチュラ付属)",
        "type": "ベリーフルーツコンプレックス配合 ナイトリップスリーピングマスク",
        "features": "ベリーフルーツコンプレックス（ラズベリー、ストロベリー、クランベリー、ブルーベリー）、ビタミンC、シアバター、ココナッツオイル",
        "value": "日中にいくらリップクリームを塗り直しても治らなかった『真冬のガサガサ皮剥け・縦ジワ』が、たった1晩の厚塗りパックでつるんと解消する圧倒的再生力",
        "desc_p1": "冬の寒さと室内暖房により、唇の水分量は急激に低下します。特に睡眠中は呼吸や寝返りによって水分が猛烈に蒸発しますが、ラネージュのスリーピングマスクは独自のモイスチャーラップ技術により、唇の表面に濃密な保湿保護フィルムを形成。8時間の間、水分の蒸散を完全に遮断します。",
        "desc_p2": "バーム状のこっくりとしたテクスチャーは、唇に乗せると体温でするりと溶けてピタッと密着。付属のスパチュラでたっぷり厚めに塗って就寝し、翌朝ティッシュオフまたはぬるま湯で軽くすすぐだけで、めくれ上がっていた乾燥皮が優しく取り去られ、驚くほどなめらかで血色の良いツヤ唇が手に入ります。20gと大容量でひと冬じゅう惜しみなく使える点も高評価です。",
        "target": "毎年冬になると唇の皮剥けや出血を繰り返す方、日中のリップ塗り直しから解放されたい方、口紅の発色やノリを良くしたい方",
        "point": "夜寝る直前に、付属のスパチュラで少し多めの量を取り、唇全体とその輪郭より少しオーバー気味にたっぷり厚塗りします。翌朝、コットンやティッシュで優しく拭き取るか、洗顔時に洗い流してください。"
    },
    {
        "rank": 2,
        "tag": "💧 5D複合セラミド×ホホバ種子の生体バリア！ベタつかずピタッと密着するリペアエッセンス",
        "catch": "ファヘやオリーブヤングのリップ部門で圧倒的人気を誇るTorridenのソリッドインシリーズ。5種類の複合セラミドと高保湿ホホバ種子油が、皮脂腺のない唇に理想的な疑似バリアを形成",
        "brand_name": "Torriden (トリデン)",
        "capacity": "11mL / チューブ容器",
        "type": "5D複合セラミド×ホホバ種子油配合 高密着リップエッセンスバーム",
        "features": "5Dセラミドコンプレックス（NP, NS, AP, AS, EOP）、ホホバ種子油、フルボ酸、低刺激処方",
        "value": "無香料・無着色で唇への負担が極めて少ない安心設計。夜の集中パックとしてはもちろん、日中の乾燥対策や口紅下地としてもマルチに活躍する軽やかな高密着ヴェール",
        "desc_p1": "唇には皮脂を分泌する皮脂腺がなく、角質層も通常の肌の3分の1程度の薄さしかありません。そのため、冬の寒冷外気に晒されるとダイレクトに細胞間脂質が流出します。トリデンのソリッドインリップは、分子量の異なる5重のセラミドを補うことで、唇そのもののバリア機能を物理的に再構築します。",
        "desc_p2": "チューブタイプで塗りやすく、濃厚でありながら髪の毛が張り付かない絶妙なテクスチャーが秀逸です。ホホバ種子油が硬くなった唇の角質を柔らかくほぐし、フルボ酸が健やかな代謝をサポート。就寝前にたっぷり重ね付けすることで、翌朝まで一度も乾燥を感じさせない濃密なうるおい膜が持続します。",
        "target": "重たいベタつきや香料が苦手な方、持ち歩きやすさと夜の集中パックを両立させたい方、皮剥けしやすい敏感な唇をお持ちの方",
        "point": "チューブから直接唇に適量を押し出し、斜めカットの先端を使って塗り広げます。夜寝る前は、唇の中央だけでなく口角のキワまでしっかり厚めに塗り重ねるのがポイントです。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 医薬部外品・花王の夜用集中密封！指でたっぷり塗る高密着・高保水リッチバーム",
        "catch": "日本のドラッグストアで不動の支持を誇るニベアの最高峰夜用リップ。5つの保湿成分と消炎有効成分が、寝ている間にひび割れ荒れを繰り返す冬の唇を濃密密閉パック",
        "brand_name": "NIVEA (ニベア / 花王)",
        "capacity": "7g / ジャー容器 (医薬部外品)",
        "type": "薬用消炎成分×5大保湿成分配合 高密着ナイトプロテクトバーム",
        "features": "ビタミンE誘導体、グリチルレチン酸ステアリル、ローヤルゼリーエキス、トレハロース、ホホバオイル",
        "value": "500円前後の手頃な価格帯ながら、医薬部外品としての本格的な消炎・保護効果を発揮。指塗りで唇の縦ジワの奥までしっかりバームを塗り込める高コスパ名品",
        "desc_p1": "ニベア ディープモイスチャー ナイトプロテクトは、睡眠中の無自覚な口呼吸や寝室の乾燥暖房から唇を死守するために設計されたジャータイプの薬用リップバームです。消炎成分のグリチルレチン酸ステアリルと血行促進作用を持つビタミンE誘導体が配合されており、荒れてヒリつく冬の唇を穏やかに鎮静します。",
        "desc_p2": "こっくりとした厚みのあるバームが体温でとろけ、唇の縦ジワの溝にぴったりとフィット。ローヤルゼリーエキスやトレハロースなどの高保水成分が角層に水分を繋ぎ止め、外側を強固な油膜でラッピングします。無香料設計で就寝時も香りが気にならず、朝起きても唇表面にしっとりとした油膜がしっかり残っています。",
        "target": "プチプラで確実な効果のある夜用リップを探している方、唇のひび割れや痛みを防ぎたい方、香料に敏感な方",
        "point": "指先に適量を取り、唇の中央から外側に向かって円を描くようにマッサージしながら塗り込みます。特に縦ジワが深い部分は、指先で優しくトントンと叩き込むように馴染ませてください。"
    },
    {
        "rank": 4,
        "tag": "🍯 高濃縮プロポリスの濃厚蜜膜！真冬のしぼんだ唇にリッチな栄養と弾力ツヤをチャージ",
        "catch": "韓国の有名皮膚科医プロデュースCNP Laboratoryが手掛けるプロポリスリップ。蜂の巣から抽出された抗酸化プロポリスエキスとハチミツが、栄養不足でしぼんだ冬の唇をぷっくり蜜艶に仕上げる",
        "brand_name": "CNP Laboratory (シーエヌピー)",
        "capacity": "15g / ジャー容器",
        "type": "高純度プロポリスエキス×ハチミツ配合 リッチスリーピングマスク",
        "features": "プロポリスエキス、ハチミツエキス、シアバター、フィトステロールズ、抗酸化フラボノイド",
        "value": "蜜のように濃厚でリッチなテクスチャー。寒さで血行が悪くなり紫色にくすんだ唇に、内側から押し返すような弾力と温かみのある健康的なピンクの艶を付与",
        "desc_p1": "冬の乾燥は唇の水分を奪うだけでなく、冷えによって血流が滞り、唇の弾力低下やくすみを引き起こします。CNPのプロポリスリップスリーピングマスクは、過酷な自然界で蜂が巣を守るために作り出す天然の抗菌・抗酸化物質『プロポリス』を贅沢に凝縮。傷んだ粘膜を優しくいたわりながら、豊富なアミノ酸とビタミンを補給します。",
        "desc_p2": "まるで本物のハチミツのような黄金色のとろみバームが、唇の表面を隙間なくコーティング。夜塗って眠れば、翌朝には乾燥による小ジワが目立たなくなり、ぽってりとしたグラマラスなボリューム感が蘇ります。天然ハチミツ由来のほのかな甘い香りもリラックスタイムにぴったりです。",
        "target": "唇のしぼみや縦ジワ、血色の悪さに悩む方、ハチミツ系コスメの濃厚な使用感が大好きな方、デパコス級の贅沢感を味わいたい方",
        "point": "夜のお手入れの最後に、指またはリップブラシで唇全体にたっぷり乗せます。週に1回、ラップを小さく切って唇に乗せる『ラップパック』を3分間行うと、プロポリスの浸透が格段に深まります。"
    },
    {
        "rank": 5,
        "tag": "🔬 医薬部外品・消炎剤×セラミド機能カプセル！ひび割れ荒れを繰り返す敏感唇の集中バーム",
        "catch": "花王キュレルの皮膚科学が辿り着いた夜用リップケアの決定版。唇パック処方により、寝ている間の乾燥から唇を守り続け、荒れて皮剥けした粘膜を夜通し集中リペア",
        "brand_name": "Curel (キュレル / 花王)",
        "capacity": "4.2g / ジャー容器 (医薬部外品)",
        "type": "薬用消炎成分×セラミド機能成分配合 ナイト集中リップバーム",
        "features": "消炎剤有効成分、セラミド機能カプセル、植物由来モイストキープ成分、ホホバ油",
        "value": "無香料・無着色・アルコールフリー・アレルギーテスト済み。刺激に極端に弱く、市販のリップクリームで荒れやすい超敏感な唇でも完全に安心して使える低刺激設計",
        "desc_p1": "唇の荒れが慢性化し、笑っただけで口角や中央がピキッと裂けてしまうような深刻な冬の唇トラブルには、医療発想のキュレル リップケアバームが不可欠です。本品は角層細胞間脂質の働きを補う『セラミド機能カプセル』が微細化されて配合されており、角層の隙間へ素早く浸透して水分保持力を根本から回復させます。",
        "desc_p2": "体温でとろけるソフトワックスベースが唇の凹凸に吸い付き、寝具の摩擦や空気の乾燥から唇を完全にシールド。皮剥けを無理に引きちぎることなく、バームの密閉力で柔らかく鎮静させ、自然な代謝によるターンオーバーを促進します。ベタつきが少なくマット寄りの仕上がりなので、男性の冬の唇ケアにも強く支持されています。",
        "target": "口角炎や唇のひび割れを繰り返している方、一般的なリップクリームで唇が痒くなったりブツブツが出やすい敏感肌、男性の唇乾燥ケア",
        "point": "就寝前に清潔な指先で適量を取り、荒れやすい口角や縦ジワに沿って優しく馴染ませます。摩擦を与えないよう、バームの厚みで唇を覆うように置くのがコツです。"
    },
    {
        "rank": 6,
        "tag": "💎 美肌のプロが追求した唇用美容液！角質ケア×濃密保湿で澄んだピンクのふっくら唇へ",
        "catch": "スキンケアの名門タカミが開発した、唇のスキンケアという新発想。荒れを予防するだけでなく、唇のターンオーバーに着目し、透明感のあるふっくらとした美肌唇を育む",
        "brand_name": "TAKAMI (タカミ)",
        "capacity": "7g / チューブ容器",
        "type": "角質ケア×エイジングケア配合 唇用高機能美容液",
        "features": "クロレラエキス、セラミド、アミノ酸複合体、ビタミンP誘導体、ヒアルロン酸",
        "value": "単に油分で覆うだけでなく、唇の代謝を正常化させてくすみや古い角質をリセット。塗るだけで縦ジワが消え去ったようなエステ級のハリと透明感を与える",
        "desc_p1": "タカミリップは、皮膚が薄くターンオーバーが早い唇の特性（約3〜5日周期）に着目した画期的な唇用美容液です。冬の乾燥によって角質肥厚を起こし、茶色くくすんで硬くなった唇の代謝を穏やかにサポート。健康な角質層の再生を促すことで、内側から血色感あふれるピンクの唇へと導きます。",
        "desc_p2": "こっくりと濃密でありながら重すぎない絶妙なジェルバームテクスチャーで、塗った瞬間から唇の表面がつるんとしたガラスのような艶でコーティングされます。夜のスペシャルケアとして厚塗りしておくと、翌朝には唇の輪郭がキュッと引き締まり、縦ジワの目立たない若々しい唇が手に入ります。",
        "target": "唇のくすみや縦ジワ、年齢によるボリューム低下が気になる方、デパコス品質の確実なエイジングケアを唇にも施したい方",
        "point": "チューブの先端を直接唇に当て、中央から外側に向けて優しく滑らせます。就寝前は米粒2粒分ほどを贅沢に厚塗りし、唇の輪郭を少しはみ出すくらいまで塗り広げて休んでください。"
    },
    {
        "rank": 7,
        "tag": "⚡ ビタミンA誘導体×コラーゲン！真冬のしぼみ・深い縦ジワを内側から押し上げる弾力セラム",
        "catch": "ロート製薬の先進皮膚科学オバジのエイジングケアシリーズ。ビタミンA誘導体とエラスチン、コラーゲンを贅沢に凝縮し、冬の乾燥でしぼんだ唇にピンとしたハリと弾力を取り戻す",
        "brand_name": "Obagi (オバジ / ロート製薬)",
        "capacity": "10g / チューブ容器",
        "type": "ビタミンA誘導体×エラスチン×コラーゲン配合 リップ美容液",
        "features": "エラスプロ®、コラプラス®、ビタミンA誘導体、ヒアルロン酸Na、シア脂",
        "value": "製薬会社ならではの深層アプローチ。年齢とともに深くなる唇の縦ジワにダイレクトに働きかけ、ふっくらと押し返されるようなボリューム感を実感",
        "desc_p1": "オバジ ダーマパワーX リップエッセンスは、唇のハリと弾力を司る真皮構造に着目した本格的エイジングケアリップです。ロート製薬独自の『エラスプロ』と『コラプラス』に加え、ターンオーバーを促すビタミンA誘導体を配合。冬の寒さで縮こまった唇の組織を細胞レベルで活性化させます。",
        "desc_p2": "濃厚で粘度の高いリッチなエッセンスが唇にピタッと密着し、潤いを長時間ホールド。塗布直後から唇の縦ジワが目立たなくなり、内側から水分とコラーゲンが満ちてきたような弾力を実感できます。就寝前のパックとして使うことで、翌朝のリップメイクの仕上がりが劇的にランクアップします。",
        "target": "唇の深い縦ジワが気になってマットリップが塗れない方、年齢とともに唇が薄くなってきたと感じる方、製薬会社の確かな技術力を信頼する方",
        "point": "米粒大を指またはチューブから直接取り、唇の縦ジワの繊維に沿って垂直方向に優しく塗り込みます。夜は少し多めに乗せて、唇をすり合わせずにそのまま就寝してください。"
    },
    {
        "rank": 8,
        "tag": "🌿 オーガニック植物オイルの贅沢な濃密蜜膜！冬の唇をリッチに満たすデパコスの名品",
        "catch": "フランスの名門クラランスが誇るオイル美容の傑作。オーガニックホホバ、ヘーゼルナッツ、ローズヒップのトリプルプラントオイルが、真冬の過酷な乾燥から唇をエレガントに保護",
        "brand_name": "CLARINS (クラランス)",
        "capacity": "7mL / チューブ・チップ容器",
        "type": "オーガニック植物オイル配合 濃密リップトリートメントオイル",
        "features": "ホホバ種子油、ヘーゼルナッツ種子油、ローズヒップオイル（カニナバラ果実油）、98%スキンケア成分処方",
        "value": "オイルでありながらベタつかず、唇を包み込むような至高のテクスチャー。天然植物の豊かな栄養が角層を柔らかくほぐし、翌朝まで高貴なツヤと柔らかさが持続",
        "desc_p1": "クラランスのリップコンフォートオイルは、65年以上にわたる植物オイル研究の粋を集めて作られたスキンケア発想のリップオイルです。配合されているオーガニックホホバオイルとヘーゼルナッツオイルは人間の皮脂膜と非常に親和性が高く、硬くなった唇の角質層へ素早く浸透してエモリエント効果を発揮します。",
        "desc_p2": "クッションのように柔らかい大型アプリケーターが、一度の塗布で唇全体をたっぷりと包み込みます。夜の就寝前に塗ることで、睡眠中にオイルの栄養分がじっくりと補給され、翌朝にはふっくらと柔らかく弾力のある唇へ整います。上品で心地よい天然アロマの香りも毎晩の就寝前の癒やしとなります。",
        "target": "デパコスならではの贅沢な使用感と香りに癒やされたい方、植物オイルによる本格的な角質柔軟効果を求める方、ギフトにも喜ばれる名品を探している方",
        "point": "付属のチップで唇全体にたっぷりと乗せます。就寝前は特に唇の輪郭部分まで広めに塗布し、ナイトオイルパックとして使用するのがおすすめです。"
    },
    {
        "rank": 9,
        "tag": "💋 高密着ハイドロゲルが隙間なく吸着！10分間でカサつき唇に水分を緊急チャージする集中パック",
        "catch": "リップパックの代名詞CHOOSY（チューシー）のハイドロゲルシートマスク。唇の形にぴったりフィットするゲルシートが、ヒアルロン酸やコラーゲンなどの美容成分を逃さず角層へ圧送",
        "brand_name": "CHOOSY (チューシー)",
        "capacity": "20枚入 / 個包装または大容量",
        "type": "高密着ハイドロゲルシート 唇専用集中密閉パック",
        "features": "ヒアルロン酸Na、加水分解コラーゲン、セラミド、ビタミンE、植物エキスコンプレックス",
        "value": "塗るバームとは異なる『ゲルシート密閉』による強制経皮吸収。冬のデート前や大事なイベントの前夜に、10分で速攻プルプル唇を完成させる即効性",
        "desc_p1": "バームやオイルを塗るだけでは追いつかないほど極度に乾燥し、カサカサに干からびてしまった冬の唇には、物理的な密閉浸透を叶えるチューシーのハイドロゲルパックが絶大な威力を発揮します。ぷるぷるのゲルシート自体が美容液を固めて作られており、唇に乗せると体温で美容成分がジワジワと溶け出します。",
        "desc_p2": "唇全体だけでなく、乾燥して荒れやすい唇の周りの皮膚までしっかりカバーするワイドサイズ設計。密着中に剥がれ落ちることがなく、本を読んだりスマホを見ながら手軽にケアできます。パックを剥がした瞬間、まるで唇が水を飲んだかのような瑞々しさと弾力が蘇り、縦ジワが一気に消え去ります。",
        "target": "特別な日の前夜に即効でぷるぷる唇を作りたい方、塗るバーム以外の集中密閉ケアを試したい方、唇の周囲のカサつきも同時にケアしたい方",
        "point": "洗顔後、清潔な唇にゲルシートをぴったりと密着させます。約10〜15分置いてからゆっくり剥がし、唇に残った美容液を手で優しくパッティング。その後にリップバームを重ねると潤いが長時間持続します。"
    },
    {
        "rank": 10,
        "tag": "🌿 発売以来の超ロングセラー！人間の皮脂に酷似したオリーブバージンオイルの鉄壁シールド",
        "catch": "日本のリップクリーム史に輝くDHCの薬用リップクリーム。人間の皮脂に極めて近いオリーブバージンオイルを高配合し、冬の厳しい乾燥や寒風から唇の粘膜を強力に保護",
        "brand_name": "DHC (ディーエイチシー)",
        "capacity": "1.5g / スティック容器 (医薬部外品)",
        "type": "薬用オリーブバージンオイル×アロエエキス配合 リップトリートメント",
        "features": "指定成分無添加、オリーブバージンオイル、アロエエキス、甘草誘導体、ビタミンE",
        "value": "一度塗れば数時間塗り直しが不要なほどの持続力。スティックの手軽さでありながらバームに匹敵する保護膜を形成し、冬の過酷なひび割れを未然に完全ブロック",
        "desc_p1": "DHCの薬用リップクリームは、スキンケア成分として名高いオリーブバージンオイルを主成分に、植物性アロエエキスと抗炎症作用を持つ甘草誘導体を絶妙なバランスで配合した医薬部外品です。人間の皮脂膜と組織が非常に似ているため、唇に乗せた瞬間に親和してスルスルとなじみ、薄くて強固な保護バリアを形成します。",
        "desc_p2": "ベタつきのない自然なツヤ感でありながら、寒風に吹かれても乾かないタフな保湿シールド力は圧巻です。就寝前に唇の縦ジワを埋めるように往復して重ね塗りしておけば、翌朝までしっとりとした柔らかさがキープされます。スティックタイプなので枕元に置いておき、寝る直前に手軽に塗布できる手軽さも魅力です。",
        "target": "スティックタイプで手軽に夜の集中保湿を行いたい方、ベタつくのが苦手な方、ドラッグストアで手軽に買える確実な名品を求める方",
        "point": "夜寝る前に、スティックを少し繰り出し、力を入れずに唇の体温でバームを溶かすようにして優しく2〜3往復塗り重ねてください。"
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
        "q": "夜用リップスリーピングマスクを塗って寝ると、寝返りで枕や布団に付きませんか？",
        "a": "寝る直前の5〜10分前に塗布し、唇になじませておくのが最も効果的です。また、唇の表面に厚く乗せるだけでなく、指やスパチュラで縦ジワの溝に沿って軽くプレスして密着させると、寝具への付着を大幅に減らすことができます。気になる場合は、就寝直前に軽くティッシュオフしても、角層表面には十分な保護膜が定着しています。"
    },
    {
        "q": "冬に唇の皮がめくれてガサガサしている時、スクラブで削っても大丈夫ですか？",
        "a": "冬の乾燥で皮剥けや出血が起きている状態でのスクラブ使用は厳禁です。無理に摩擦で角質を削ると粘膜が傷つき、口唇炎や色素沈着の原因になります。まずはリップスリーピングマスクを毎晩厚塗りして数日間集中的に保湿してください。マスクに含まれる油分やエモリエント成分によって古い角質が自然に柔らかくなり、洗顔時やティッシュオフの際に摩擦なしでスルッと剥がれ落ちます。"
    },
    {
        "q": "夜用のリップマスクは朝のメイク前や口紅の下地として使っても良いですか？",
        "a": "使用量を調整すれば下地としても極めて優秀です。朝のスキンケアの最初に米粒半分程度の少量を唇に薄く伸ばしておき、メイクの最後にリップカラーを塗る直前に軽くティッシュオフしてください。これだけで唇の縦ジワがふっくらと目立たなくなり、マットリップやティントを塗っても一日中皮剥けやひび割れが起きなくなります。"
    },
    {
        "q": "無意識に唇を舐めてしまう癖があるのですが、乾燥悪化の原因になりますか？",
        "a": "非常に深刻な乾燥悪化要因です。唇を舐めると、唾液に含まれる消化酵素（アミラーゼ等）が唇のデリケートな粘膜を刺激するだけでなく、付着した水分が蒸発する際に唇本来の水分まで一緒に奪い去る『過乾燥』を引き起こします。唇が乾いたと感じたら舐めるのではなく、即座に高密着バームで油膜を補充することを習慣づけてください。"
    },
    {
        "q": "日中の通常のリップクリームと、夜用リップスリーピングマスクの成分的な違いは何ですか？",
        "a": "最大の違いは『配合ワックスの融点と油分の粘度、および密閉持続時間』にあります。日中用リップは塗りやすさやベタつき防止を優先してサラサラした液状油や軽めのワックスが多く使われますが、夜用スリーピングマスクは8時間以上の睡眠中に水分蒸散を完全に遮断するため、高粘度のマイクロクリスタリンワックスやシアバター、高濃度セラミドを贅沢に配合し、物理的なオクルーシブ（密閉）膜を形成するよう設計されています。"
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
            "headline": "保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10",
            "description": "11月・12月の夜間暖房と寒冷乾燥による唇の皮剥け・縦ジワ・ひび割れを徹底救済！ラネージュ、トリデン、ニベア、CNP、キュレルまで夜用高密着リップスリーピングマスクの科学的修復メカニズム・最新実勢価格・口コミを網羅してご紹介。",
            "image": items[0]["image_url"],
            "datePublished": "2026-11-12T05:00:00+09:00",
            "dateModified": "2026-11-12T05:00:00+09:00",
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
            "name": "真冬の高保湿リップスリーピングマスクおすすめランキング10選",
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
                    "name": "冬の徹底保湿ケア特集",
                    "item": "https://lumi-cosme.vercel.app/winter-lip-sleeping-mask"
                }
            ]
        }
    ]
}

# HTML Cards
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
            <span class="value-title">💡 11-12月の唇乾燥対策・即効価値</span>
            <p>{p['value']}</p>
          </div>
        </div>
      </div>
      <div class="product-desc-box">
        <h4>👄 美容科学＆テクスチャー詳細解説</h4>
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
  <title>保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10 | LUMI COSMETICS LAB</title>
  <meta name="description" content="11月・12月の夜間暖房と寒冷乾燥による唇の皮剥け・縦ジワ・ひび割れを徹底救済！ラネージュ、トリデン、ニベア、CNP、キュレルまで夜用高密着リップスリーピングマスクの科学的修復メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-lip-sleeping-mask">
  <link rel="icon" href="/favicon.jpg">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10">
  <meta property="og:description" content="11月・12月の夜間暖房と寒冷乾燥による唇の皮剥け・縦ジワ・ひび割れを徹底救済！ラネージュ、トリデン、ニベア、CNP、キュレルまで夜用高密着リップスリーピングマスクの科学的修復メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-lip-sleeping-mask">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LUMI COSMETICS LAB">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10">
  <meta name="twitter:description" content="11月・12月の夜間暖房と寒冷乾燥による唇の皮剥け・縦ジワ・ひび割れを徹底救済！ラネージュ、トリデン、ニベア、CNP、キュレルまで夜用高密着リップスリーピングマスクの科学的修復メカニズム・最新実勢価格・口コミを網羅してご紹介。">
  <meta name="twitter:image" content="{items[0]['image_url']}">
  <script type="application/ld+json">
  {json.dumps(structured_data, ensure_ascii=False, indent=2)}
  </script>
  <style>
    :root {{
      --primary: #e11d48;
      --primary-light: #ffe4e6;
      --primary-dark: #be123c;
      --accent: #f59e0b;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #fff1f2;
      --card-bg: #ffffff;
      --border: #fecdd3;
      --radius: 16px;
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
      background: #fafaf9;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid #f2e8e9;
      position: sticky;
      top: 0;
      z-index: 100;
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
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .breadcrumb {{
      max-width: 1100px;
      margin: 12px auto;
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
      margin: 0 auto;
      padding: 24px 20px 80px;
    }}
    .hero-section {{
      background: linear-gradient(135deg, #ffe4e6 0%, #ffffff 100%);
      border: 1px solid #fecdd3;
      border-radius: var(--radius);
      padding: 40px 32px;
      margin-bottom: 40px;
    }}
    .hero-tag {{
      display: inline-block;
      background: var(--primary);
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
      color: #881337;
      margin-bottom: 16px;
    }}
    .hero-desc {{
      font-size: 1rem;
      color: #4c0519;
      line-height: 1.7;
    }}
    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin-bottom: 40px;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 8px 16px;
    }}
    .toc-list a {{
      color: var(--primary);
      text-decoration: none;
      font-size: 0.9rem;
      transition: color 0.2s;
    }}
    .toc-list a:hover {{
      color: var(--primary-dark);
      text-decoration: underline;
    }}
    .science-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 48px;
    }}
    .science-box h3 {{
      font-size: 1.35rem;
      color: #881337;
      margin-bottom: 16px;
    }}
    .science-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin-top: 24px;
    }}
    .science-card {{
      background: #fff5f5;
      border: 1px solid #fed7aa;
      border-radius: 12px;
      padding: 20px;
      border-left: 4px solid var(--primary);
    }}
    .science-card h4 {{
      font-size: 1rem;
      margin-bottom: 8px;
      color: #881337;
    }}
    .science-card p {{
      font-size: 0.9rem;
      color: #475569;
      line-height: 1.6;
    }}
    .section-title {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #881337;
      margin: 48px 0 24px;
      padding-left: 12px;
      border-left: 6px solid var(--primary);
    }}
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }}
    .product-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 1.1rem;
      font-weight: 800;
      padding: 6px 16px;
      border-radius: 8px;
    }}
    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 6px;
    }}
    .product-content {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 28px;
      margin-bottom: 24px;
    }}
    @media (max-width: 768px) {{
      .product-content {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-img-box {{
      width: 100%;
      height: 240px;
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border);
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .product-img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      transition: transform 0.3s;
    }}
    .product-img:hover {{
      transform: scale(1.04);
    }}
    .product-brand {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      line-height: 1.4;
      margin-bottom: 8px;
      color: #0f172a;
    }}
    .product-catch {{
      font-size: 0.95rem;
      color: #475569;
      line-height: 1.6;
      margin-bottom: 12px;
    }}
    .product-meta {{
      display: flex;
      gap: 16px;
      font-size: 0.85rem;
      color: #64748b;
      margin-bottom: 8px;
    }}
    .product-features {{
      font-size: 0.85rem;
      background: #fdf2f8;
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
      color: #e11d48;
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
      background: #fff1f2;
      border: 1px solid #fecdd3;
      border-radius: 8px;
      padding: 12px 16px;
      font-size: 0.9rem;
      color: #881337;
    }}
    .value-title {{
      font-weight: 700;
      display: block;
      margin-bottom: 4px;
    }}
    .product-desc-box {{
      background: #fffafb;
      border-radius: 8px;
      padding: 20px;
      margin-bottom: 20px;
      border: 1px solid #ffe4e6;
    }}
    .product-desc-box h4 {{
      font-size: 1rem;
      margin-bottom: 12px;
      color: #881337;
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
      color: #881337;
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
      background: #ffe4e6;
      font-weight: 700;
      color: #881337;
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
      color: #881337;
      margin-bottom: 8px;
      font-size: 1rem;
    }}
    .faq-a {{
      color: #334155;
      font-size: 0.92rem;
      line-height: 1.7;
    }}
    .hub-link-banner {{
      background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
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
      color: #be123c;
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
      border: 1px solid #e2e8f0;
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
      color: #fda4af;
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
    <a href="/">ホーム</a> &gt; <span>高保湿リップスリーピングマスク特集</span>
  </div>

  <main>
    <div class="hero-section">
      <span class="hero-tag">🌙 11月・12月 就寝中集中密閉ラッピング</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！就寝中の濃厚密閉ラッピング処方で真冬のガサガサ皮剥け唇をぷるんと再生する保湿力高めリップスリーピングマスクランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて外気湿度と室温が急激に低下し、エアコン暖房の稼働により睡眠中の空気は過酷な砂漠状態へと化します。皮脂腺も汗腺も存在しない唇は自力で皮脂膜を作ることができず、寝ている間の水分蒸散と無意識な口呼吸によって、朝起きると皮剥け・ひび割れ・出血に見舞われがちです。本特集では、高粘度マイクロクリスタリンワックスや高濃度セラミド、高純度植物オイルを融合し、一晩で赤ちゃんのようなふっくら唇へと再生させる夜用リップスリーピングマスク10選を徹底検証しました。
      </p>
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次・記事ナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#science-guide">1. なぜ唇は冬の睡眠中に急激にひび割れるのか？皮膚解剖学の真実</a></li>
        <li><a href="#rank-1">第1位: LANEIGE リップスリーピングマスク ベリー</a></li>
        <li><a href="#rank-2">第2位: Torriden ソリッドイン セラミド リップエッセンス</a></li>
        <li><a href="#rank-3">第3位: NIVEA ディープモイスチャー ナイトプロテクト</a></li>
        <li><a href="#rank-4">第4位: CNP Laboratory プロポリス リップスリーピングマスク</a></li>
        <li><a href="#rank-5">第5位: Curel リップケアバーム (医薬部外品)</a></li>
        <li><a href="#rank-6">第6位: TAKAMI タカミリップ</a></li>
        <li><a href="#rank-7">第7位: Obagi ダーマパワーX セラム リップエッセンス</a></li>
        <li><a href="#rank-8">第8位: CLARINS リップ コンフォート オイル</a></li>
        <li><a href="#rank-9">第9位: CHOOSY ハイドロゲル リップパック</a></li>
        <li><a href="#rank-10">第10位: DHC 薬用リップクリーム</a></li>
        <li><a href="#selection-matrix">2. 唇の荒れレベル別：夜用リップマスク最適選択マトリクス</a></li>
        <li><a href="#faq-section">3. よくある質問・Q&Aセクション</a></li>
      </ul>
    </div>

    <div class="science-box" id="science-guide">
      <h3>🔬 なぜ唇は日中のリップクリームだけでは治らないのか？夜間密閉ラッピングの皮膚科学</h3>
      <p>
        唇の赤みは、薄い粘膜の直下に毛細血管が透けて見えている状態です。通常の顔の皮膚と比較して、唇には以下のような極めて過酷な解剖学的弱点が存在します。
      </p>
      <div class="science-grid">
        <div class="science-card">
          <h4>① 皮脂腺・汗腺がゼロ＝皮脂膜が存在しない</h4>
          <p>皮脂膜という天然の保護シールドを自力で形成できないため、外気の湿度が下がると無防備な角層から秒速で水分が空気中へ奪われます。</p>
        </div>
        <div class="science-card">
          <h4>② 角層の厚さが通常の皮膚のわずか1/3以下</h4>
          <p>角質細胞の重なりが極めて薄く、細胞間脂質の蓄積量も少ないため、摩擦や乾燥などの外部ストレスによって容易に亀裂が生じます。</p>
        </div>
        <div class="science-card">
          <h4>③ 就寝中の口呼吸と暖房風による強制蒸散</h4>
          <p>寝ている間の6〜8時間、会話や飲食による補給がない無防備な状態で温風に晒され続けることで、朝の皮剥けや出血が発生します。</p>
        </div>
      </div>
      <p style="margin-top: 20px;">
        この生理的弱点を完全に克服するのが、夜用リップスリーピングマスクの『オクルーシブ（密閉）処方』です。日中用リップよりも融点が高く粘り気のある高密着ワックスベースが、8時間以上にわたり水分蒸散を物理的にシャットアウト。同時に角質軟化成分が古い角皮をふやかして優しく整えます。
      </p>
    </div>

    <h2 class="section-title">真冬の唇乾燥とさようなら！高保湿リップスリーピングマスクおすすめランキング10選</h2>

    {product_cards_html}

    <div class="summary-box" id="selection-matrix">
      <h3>📊 唇の荒れ症状別：リップスリーピングマスク最適選択マトリクス</h3>
      <p>
        冬の唇トラブルの状態（皮剥け、ひび割れ、縦ジワしぼみ、敏感荒れ）に合わせて最適な製品を選ぶことで、短期間でぷるんとした健康的な唇を取り戻せます。
      </p>
      <table class="summary-table">
        <thead>
          <tr>
            <th>唇のトラブル状態</th>
            <th>おすすめのアイテム</th>
            <th>注目の主要成分</th>
            <th>テクスチャーと仕上がり</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>ガサガサ皮剥け・角質肥厚</strong></td>
            <td>LANEIGE / CHOOSY</td>
            <td>ベリーフルーツコンプレックス、ヒアルロン酸</td>
            <td>とろけるバーム / 密閉ハイドロゲル</td>
          </tr>
          <tr>
            <td><strong>出血・ひび割れ・ヒリヒリ痛い</strong></td>
            <td>キュレル / ニベア ナイトプロテクト</td>
            <td>消炎グリチルリチン酸、セラミド機能成分</td>
            <td>低刺激保護ベール / 薬用濃厚リッチバーム</td>
          </tr>
          <tr>
            <td><strong>軽いつけ心地・ベタつき嫌い</strong></td>
            <td>Torriden / DHC</td>
            <td>5D複合セラミド、オリーブバージンオイル</td>
            <td>みずみずしいエッセンス / なめらかスティック</td>
          </tr>
          <tr>
            <td><strong>深い縦ジワ・しぼみ・ハリ不足</strong></td>
            <td>Obagi / TAKAMI</td>
            <td>ビタミンA誘導体、エラスチン、アミノ酸</td>
            <td>高粘度弾力セラム / 唇専用スキンケア美容液</td>
          </tr>
          <tr>
            <td><strong>血色不良・くすみ・贅沢ケア</strong></td>
            <td>CNP / クラランス</td>
            <td>プロポリス、オーガニック植物オイル</td>
            <td>濃密蜜バーム / リッチプラントオイル</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="hub-link-banner">
      <div>
        <h4>❄️ あわせてチェックしたい冬の集中保湿ケア</h4>
        <p>唇だけでなく、顔全体の角層深部まで潤いを満たす高保湿セラミドシートマスク特集も公開中！</p>
      </div>
      <a href="/winter-ceramide-mask" class="hub-link-btn">高保湿セラミドシートマスク特集へ →</a>
    </div>

    <div class="summary-box" id="faq-section">
      <h2 style="font-size: 1.3rem; margin-bottom: 20px; color: #881337;">❓ 真冬の高保湿リップスリーピングマスクに関するよくある質問（FAQ）</h2>
      {faq_html}
    </div>

    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container">
        <!-- 内部リンク更新スクリプトで自動挿入されます -->
      </div>
    </div>
  </main>

  <footer>
    <div class="footer-inner">
      <div class="footer-title">LUMI COSMETICS LAB 関連コンテンツ一覧</div>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- フッターリンク更新スクリプトで自動挿入されます -->
      </div>
      <div class="copyright">
        &copy; 2026 LUMI COSMETICS LAB. All rights reserved. 掲載されている商品価格・仕様・レビュー情報は楽天市場APIよりリアルタイムに自動取得された最新データです。
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-lip-sleeping-mask.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Successfully generated winter-lip-sleeping-mask.html!")
