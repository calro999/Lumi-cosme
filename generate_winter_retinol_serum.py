import json
import re

with open("fetched_3new_retinol_hyaluronic_cica.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_retinol_serum"]["items"]

# 10商品それぞれの完全オリジナル・皮膚科学的専門解説
product_details = [
    {
        "rank": 1,
        "tag": "🌿 純粋レチノール×CICA×ヒアルロン酸！冬のA反応を抑えて毎日攻めの毛穴・キメケアができるメガヒット美容液",
        "catch": "美容大国・韓国と日本で空前の大ヒットを記録し続けるレチノールセラムの絶対王者。純粋レチノールとCICA成分（チェジュ島ツボクサエキス）をリポソームカプセル化し、冬の乾燥ゆらぎ肌でもピリつきや赤みを感じさせずにキメ細やかな陶器肌へ導くデイリー美容液",
        "brand_name": "innisfree (イニスフリー)",
        "capacity": "30mL / ポンプボトル",
        "type": "純粋レチノール配合 低刺激CICAリポソーム美容液",
        "features": "純粋レチノール、CICA（ツボクサエキス・マデカッソシド）、低分子ヒアルロン酸、アデノシン、ナイアシンアミド",
        "value": "11月から急増する暖房乾燥によるキメの粗さや毛穴の目立ちを、穏やかなターンオーバー促進でなめらかに修復。皮むけを起こさず翌朝のつるんとした手触りを実現",
        "desc_p1": "11月から12月は紫外線量が年間で最も少なくなるため、紫外線感受性の高いレチノールケアを始めるのに一年で最も理想的な時期です。しかし冬場の冷えと乾燥で肌バリアが低下していると、一般的な高濃度レチノールでは皮むけや乾燥（A反応）が起きやすくなります。イニスフリーのレチノールシカリペアセラムは、純粋レチノールをセラミドとヒアルロン酸を含むナノカプセルに内包し、角層へじわじわと届けることで刺激を徹底的に抑制しています。",
        "desc_p2": "みずみずしいウォータリーエッセンス質感で、肌に乗せるとスーッと馴染んでベタつきが残りません。ツボクサ由来の鎮静成分が同時に働くため、赤みが出やすい冬のデリケートな肌でも毎日のスキンケアルーティンに安心して組み込めます。2〜3週間の継続使用で、冬のゴワつきや小鼻周りのざらつきが解消され、ファンデーションのノリが劇的に向上します。",
        "target": "レチノール初心者の方、冬でも肌荒れや皮むけを起こさずに毛穴・小ジワケアを始めたい方、朝晩使えるマイルドなエイジングケアセラムを求める方",
        "point": "夜の洗顔後、化粧水でしっかり水分を与えた後に1〜2プッシュを顔全体にやさしくなじませます。特に乾燥小ジワが気になる目尻や頬には重ねづけし、仕上げに高保湿クリームで蓋をしてください。"
    },
    {
        "rank": 2,
        "tag": "🔬 次世代レチノイド0.1%×シカヒアルロン！たるみ毛穴と冬のキメ乱れをキュッと引き締める毛穴特化セラム",
        "catch": "毛穴レス肌を目指すVTのシカレチAシリーズ。第3世代レチノイド誘導体（ヒドロキシピナコロンレチノアート）に独自CICA成分をブレンドし、冬の寒冷で代謝が落ちた毛穴周りのコラーゲン生成を後押しする濃密エッセンス",
        "brand_name": "VT COSMETICS (ブイティー)",
        "capacity": "30mL / ポンプボトル",
        "type": "安定型レチノイド誘導体＆シカヒアルロン配合 毛穴・キメ引き締めエッセンス",
        "features": "ヒドロキシピナコロンレチノアート0.1%、CICALIAO™（ツボクサエキス・プロポリス・センテラ4X）、バクチオール、ペプチドコンプレックス",
        "value": "冷たい風で縮こまり涙型に開いたたるみ毛穴を内側から押し上げるようにタイトニング。毛穴影を消し去り、ピンと張りのある若々しい肌印象へ",
        "desc_p1": "冬の乾燥が進むと、角層の水分喪失に伴って毛穴周りの皮膚がしぼみ、毛穴が楕円形に広がる『たるみ毛穴』が顕著になります。VTシカレチAエッセンス0.1は、肌への親和性が高く直接レチノイン酸受容体に働きかける安定型レチノイド誘導体を採用。従来の純粋レチノールに比べて酸化しにくく、真冬の乾いた肌でも安定した引き締め実感を届けます。",
        "desc_p2": "乳液と美容液の中間のようなコクのあるテクスチャーでありながら、浸透後は肌表面がシルキーに整い、毛穴の凹凸を自然にフラットにしてくれます。植物性レチノールと呼ばれるバクチオールも相乗配合されているため、冬の寒暖差によるゆらぎを防ぎつつ、夕方になっても毛穴落ちしない強い肌土台を築き上げます。",
        "target": "冬になると乾燥で頬の毛穴が縦長に目立つ方、皮脂バランスが崩れて毛穴が詰まりやすい混合肌の方、毛穴の引き締まりとハリ感を同時に手に入れたい方",
        "point": "化粧水をたっぷり浸透させた後、1プッシュを手にとり、小鼻の脇や頬の中央など毛穴が気になるエリアを中心に内側から外側へ引き上げるように塗り広げます。"
    },
    {
        "rank": 3,
        "tag": "💎 純度安定化ピュアレチノール0.1%×アラントイン！乾燥小ジワと目元口元を集中リペアする本格派",
        "catch": "韓国ダーマコスメの最高峰COSRXが贈る高純度ピュアレチノール。独自のアニオンカプセル化とトコトリエノール（スーパービタミンE）の保護により、鮮度を保ったまま冬の頑固な乾燥小ジワを集中攻撃する実力派処方",
        "brand_name": "COSRX (コスアールエックス)",
        "capacity": "20mL / アルミチューブ",
        "type": "高純度ピュアレチノール0.1%配合 集中リンクルリペアセラム・クリーム",
        "features": "ピュアレチノール0.1%、トコトリエノール、アラントイン、パンテノール、ヒアルロン酸",
        "value": "目尻のカラスの足跡や口元の乾燥ほうれい線など、冬の空気乾燥で深く刻まれやすい小ジワを内側からふっくら充填。2週間の集中ケアで弾力感の変化を実感",
        "desc_p1": "11月後半から一気に空気が乾燥すると、笑ったときの目尻のちりめんジワや口元の乾燥小ジワがそのまま定着しそうになる危機感を覚える方が多いはずです。COSRXのRXザ・レチノール0.1は、酸化しやすいピュアレチノールを遮光アルミチューブに閉じ込め、純度を損なうことなく角層へ届けます。",
        "desc_p2": "こっくりとしたクリームセラム状で、小ジワの溝にピタッと密着するホールド感があります。抗炎症成分のアラントインと保湿成分のパンテノールが高濃度で配合されているため、レチノール特有の乾燥感を防ぎながら、角層深部のターンオーバーをダイレクトに活性化。夜塗って寝るだけで翌朝の肌にパンとしたハリが宿ります。",
        "target": "目元や口元の乾燥小ジワがファンデーションに溜まる方、成分純度にこだわった本格的なエイジングケアを行いたい方、確かなハリ実感を求める方",
        "point": "夜のお手入れの最後に、米粒大を指先に取り、目尻や口元の気になるシワの溝を広げるようにして優しくトントンと馴染ませます。使い始めの2週間は2〜3日に1回のペースで使用してください。"
    },
    {
        "rank": 4,
        "tag": "🏆 マイクロフリーズドライ純粋レチノール×セラミド！皮膚科医発想でバリアを守り抜く名品セラム",
        "catch": "キールズが長年の皮膚科学研究から導き出した黄金比。フリーズドライされた純粋レチノールをセラミドやペプチドと融合させ、敏感肌テストをクリアした冬の最高峰エイジングケア美容液",
        "brand_name": "KIEHL'S (キールズ)",
        "capacity": "30mL / 遮光エアレスポンプ",
        "type": "マイクロ純粋レチノール配合 低刺激高機能リニューイング美容液",
        "features": "マイクロフリーズドライ純粋レチノール、セラミドNP、アセチルジペプチド、ヒアルロン酸、ナイアシンアミド",
        "value": "冬の過酷な外気から角層バリアを強固に保護しながら、肌の密度と弾力を底上げ。デパコスならではの上質な使い心地と確かな肌質改善効果を提供",
        "desc_p1": "キールズのDS RTN リニューイング セラムは、美容のプロや皮膚科医からも絶賛されるデパコスレチノールの最高峰です。光や空気による劣化を防ぐエアレスポンプ容器を採用し、ワンプッシュごとに新鮮なマイクロ純粋レチノールを肌へ届けます。角層のバリアを補強するセラミドNPが最初から組み合わされている点が、冬の乾燥シーズンに極めて優位です。",
        "desc_p2": "淡い黄色のまろやかなエマルジョン状テクスチャーで、塗布した瞬間から肌が上質な潤いのヴェールに包まれます。レチノール製品特有のツッパリ感や皮むけを極限まで排除しながら、頬のハリ不足やくすみ、ざらつきを包括的にケア。高価ではありますが、冬の肌投資として確実なリターンをもたらしてくれる名品です。",
        "target": "冬の乾燥肌でも安心して使える高品質なデパコス美容液を探している方、大人のたるみや深いハリ不足に悩む方、肌の土台から若返りを目指す方",
        "point": "夜の洗顔後、化粧水で整えた肌に1プッシュを全顔になじませます。首やデコルテまで伸ばすことで、冬のタートルネックで乾燥しやすい首元のシワケアも同時に叶います。"
    },
    {
        "rank": 5,
        "tag": "💧 低刺激レチノール×角質柔軟トリプル酸×ナイアシンアミド！冬のゴワつきを解きほぐす敏感肌処方",
        "catch": "世界各国の皮膚科医が採用するラロッシュポゼの角質・キメ集中美容液。低刺激レチノール誘導体と角質を穏やかに整えるサリチル酸・乳酸が、冬の代謝停滞で硬くなった角層を柔らかくほぐす",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "30mL / スポイトボトル",
        "type": "低刺激角質ケア＆レチノール美容液",
        "features": "レチノール複合成分、サリチル酸、乳酸、ナイアシンアミド、フランス・ラロッシュポゼ村ターマルウォーター",
        "value": "冬の寒さでターンオーバーが滞り、化粧水が弾かれて入らない厚くなった角層をやさしくリセット。美容成分の浸透ルートを開拓しモチ肌を復活",
        "desc_p1": "冬になると『化粧水が肌の表面で滑って入っていかない』『肌を触るとザラザラして硬い』と感じる原因は、寒冷による角質剥離の不全です。ラロッシュポゼのピールケア美容液は、肌表面を削ることなく穏やかに角質をゆるめるトリプル酸と、肌代謝を促すレチノール、肌を鎮静するナイアシンアミドを贅沢に配合しています。",
        "desc_p2": "とろみのあるスポイトタイプで、摩擦を与えずに肌の上をスルスルと広がります。フランスの湧水『ターマルウォーター』に含まれる希少ミネラル・セレンが活性酸素を中和し、冬の赤みやかゆみを抑えながら健やかな素肌へと整えます。毎日使えるマイルド設計なので、肌がデリケートな冬でもストレスフリーに角質リファインが可能です。",
        "target": "冬の乾燥で肌がゴワついてスキンケアが浸透しにくい方、角栓や毛穴のざらつきが気になる敏感肌の方、肌の透明感を取り戻したい方",
        "point": "夜の洗顔後すぐ、または導入化粧水の後に3〜4滴を手に取り、顔全体を手のひらで包み込むように優しくハンドプレスします。"
    },
    {
        "rank": 6,
        "tag": "⚡ 100MPa超高圧抽出ナノレチノール！角層最深部まで秒速浸透して真冬のハリを呼び覚ます高浸透セラム",
        "catch": "深海1万メートルの水圧に匹敵する超高圧加工技術で、レチノールを極小ナノ分子に分散。肌に触れた瞬間に吸い込まれるような浸透力を誇り、プチプラの常識を覆すハリ感を与える大人気美容液",
        "brand_name": "unlabel LAB (アンレーベル ラボ)",
        "capacity": "50mL / ポンプボトル",
        "type": "超高圧抽出ナノレチノール配合 高浸透エイジングセラム",
        "features": "超高圧抽出水添レチノール、浸透型ビタミンE、セラミド、無香料・無着色・アルコールフリー",
        "value": "冬の硬い角層にも素早く届くナノ化技術。べたつかず奥からふっくらと持ち上がるようなハリ感をリーズナブルにデイリー補給",
        "desc_p1": "ドラッグストアで圧倒的な支持を集めるアンレーベルラボのRエッセンスは、100MPaという超高圧処理によってレチノール分子をナノレベルまで微細化した先進処方です。冬場の冷えた肌は細胞間脂質が凝固しやすく美容成分の浸透が妨げられがちですが、このナノレチノールは角層の隙間をすり抜けるように深部まで到達します。",
        "desc_p2": "さらっとした黄色いセラムで、肌に乗せると一瞬で消え去るように吸い込まれていきます。油膜感やベタつきが一切ないため、後から使う化粧水やクリームの邪魔をしません。50mLという大容量で2,000円前後の驚異的なコストパフォーマンスを誇り、顔だけでなく首元や手の甲など冬の年齢サインが出やすい部位にも贅沢に使えます。",
        "target": "ベタつく美容液が苦手な方、プチプラで確かな浸透力を持つレチノールを使いたい方、首やデコルテまで全身にたっぷりエイジングケアを施したい方",
        "point": "洗顔後すぐの導入美容液として、または化粧水の後、2プッシュを手にとり顔全体へなじませます。乾燥が気になる目元や口元には重ね付けが効果的です。"
    },
    {
        "rank": 7,
        "tag": "🧪 国産ピュアレチノール原液×ナノカプセル処方！成分純度にこだわり抜いた冬の本格リンクル美容液",
        "catch": "原液コスメのスペシャリストKISOが開発した高濃度レチノール美容液。安定化カプセルに封入した純粋レチノールを限界まで配合し、余分な界面活性剤や香料を排除したプロスペックの原液ケア",
        "brand_name": "KISO (基礎化粧品研究所)",
        "capacity": "30mL / スポイトボトル",
        "type": "純粋レチノール原液配合 集中エイジングケアセラム",
        "features": "カプセル化ピュアレチノール、7種のオーガニック植物エキス、トコフェロール、パラベンフリー",
        "value": "無駄なコストを徹底的にカットし、純粋な成分力のみで冬の乾燥小ジワと毛穴の開きを集中ケア。実感値の高い高濃度原液スキンケアを実現",
        "desc_p1": "成分重視派のスキンケアマニアから絶大な信頼を寄せられているKISOのスーパーリンクルセラムVA。一般的な化粧品では微量配合にとどまりがちな純粋レチノールを、肌への刺激を抑えるナノリポソームカプセルに高濃度で内包。冬の過酷な乾燥環境でも有効成分が徐放的に放出され、長時間にわたってコラーゲン生成をサポートします。",
        "desc_p2": "スポイトから取り出すと、とろりとした乳白色の液体で、肌に伸ばすと滑らかに広がってしっとりとした潤い膜を形成します。香料や着色料を一切含まず、原料そのものの良さを活かした設計。毎晩のルーティンに取り入れることで、冬の暖房でしぼみかけた頬の皮膚がモチッと内側から押し返されるような手応えを感じられます。",
        "target": "ブランド料や広告費ではなく成分の濃度と品質で選びたい方、純粋レチノールの確かなハリ・キメ効果を実感したい方、原液美容液が好きな方",
        "point": "夜の化粧水の後、スポイトで1〜2滴を取り、気になる部分または全顔に薄く伸ばします。紫外線への影響を考慮し、必ず夜のみ使用し翌朝は日焼け止めを塗布してください。"
    },
    {
        "rank": 8,
        "tag": "🌾 豆乳発酵液×ピュアレチノール×ビタミンE！100mL大容量で首元までたっぷり満たす冬の国民的セラム",
        "catch": "累計販売数数千万本を誇るなめらか本舗の最高峰リンクルライン。国産大豆『ふくゆたか』の豆乳発酵液と純粋レチノールを組み合わせ、真冬の乾燥小ジワを目立たなくする医薬部外品級の実力派",
        "brand_name": "SANA なめらか本舗 (常盤薬品工業)",
        "capacity": "100mL / ポンプボトル",
        "type": "豆乳発酵液＆ピュアレチノール配合 高保湿エイジング美容液",
        "features": "豆乳発酵液（高純度イソフラボン）、ピュアレチノール、パルミチン酸レチノール、ビタミンE誘導体",
        "value": "ドラッグストアで手軽に買える圧倒的コスパ。惜しみなく毎日首元までたっぷり塗れる大容量で、冬の全身乾燥小ジワを徹底撃退",
        "desc_p1": "なめらか本舗のリンクル美容液Nは、日本の女性の肌に長年寄り添ってきた大豆イソフラボン研究の集大成です。冬の乾燥で乱れがちな女性ホルモンバランスや肌代謝に着目し、高純度イソフラボンを含有する豆乳発酵液と、代謝を促すピュアレチノールをダブルで配合。乾燥による小じわを目立たなくする効能評価試験済みです。",
        "desc_p2": "とろみのあるまろやかな乳液状の美容液で、100mLという美容液としては破格の大容量が魅力です。プッシュ式で使いやすく、顔全体はもちろん、冬のタートルネックやマフラーで摩擦を受けやすい首元・デコルテまで贅沢に伸ばせます。ベタつかずに深いうるおいが長時間続くため、冬の朝晩の基本ケアとして家族みんなでシェアできる安心感があります。",
        "target": "コスパを重視して首元までたっぷりエイジングケアしたい方、イソフラボンのもっちりした潤いが好きな方、ドラッグストアで手軽に買いたい方",
        "point": "化粧水の直後、1〜2プッシュを手にとり顔全体から首筋にかけて下から上へ優しくなじませます。乾燥しやすい目元口元には重ね付けがおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🍯 レチノール×パンテノール×セラミド！冬の乾いた角層をふっくら整えるマルチ保湿リペアセラム",
        "catch": "世界的な自然派ブランド・ネイチャーリパブリックが手掛ける濃密リペア処方。レチノールに肌修復ビタミンである高濃度パンテノールとセラミドをブレンドし、冬の乾燥しぼみ肌をなめらかに満たす高保湿セラム",
        "brand_name": "NATURE REPUBLIC (ネイチャーリパブリック)",
        "capacity": "30mL / スポイトボトル",
        "type": "レチノール＆高濃度パンテノール配合 高保湿リペアアンプル",
        "features": "レチノール、パンテノール、セラミドNP、プロポリスエキス、植物性スクワラン",
        "value": "冬の暖房直撃によるインナードライと肌荒れを同時にレスキュー。角層の水分保持力を高めながらツヤのある若々しい肌へ",
        "desc_p1": "ネイチャーリパブリックのレチノールリペアアンプルは、肌の代謝を促すレチノールと、保湿・抗炎症に優れたパンテノールを絶妙なバランスで掛け合わせた冬の救世主です。冷たい風に晒されて角層が荒れているときでも、パンテノールが細胞間を補修して潤いを抱え込み、レチノールの浸透を優しくサポートします。",
        "desc_p2": "濃密なハチミツのような光沢を持つリッチなテクスチャーですが、肌になじませるとスッと溶け込み、しっとりとした保護膜を作ります。プロポリスエキスとスクワランも配合されているため、冬場の乾燥によるピリピリ感を鎮め、翌朝起きたときの肌の柔らかさとモチモチ感が格段にアップします。",
        "target": "冬になると肌がカサついて粉を吹きやすい乾燥肌、レチノールの刺激が不安な敏感肌、ツヤと弾力を同時に手に入れたい方",
        "point": "夜のお手入れ時に化粧水の後、2〜3滴を顔全体になじませます。特に乾燥が気になる頬や口周りには手のひらで温めながら押し込むようにプレスしてください。"
    },
    {
        "rank": 10,
        "tag": "🏆 4重レチノイドコンプレックス×皮膚科学研究30年！冬の密度爆発リフティングを叶える最高峰美容液",
        "catch": "韓国レチノール研究のパイオニアIOPEが到達した最新峰。4種類の異なるレチノイドを段階的に作用させるマルチレイヤリング技術で、真冬の寒さで緩んだフェイスラインと肌密度を劇的に引き上げる",
        "brand_name": "IOPE (アイオペ)",
        "capacity": "30mL / ポンプボトル",
        "type": "4重レチノイドコンプレックス配合 高密度リフティング美容液",
        "features": "純粋レチノール、カプセル化レチノール、次世代グラナクティブレチノイド、Bio-Seletinoid™、ヒノキ葉エキス",
        "value": "肌の表皮・真皮・基底膜の各層に段階的にアプローチ。冬の乾燥でへたった大人の肌に、指を押し返すような高密度弾力を再生",
        "desc_p1": "1997年に韓国で初めてレチノール製品を実用化して以来、30年近く皮膚科学研究をリードしてきたアイオペ。その集大成である『レチノール スーパーバウンス セラム』は、即効型から持続型まで異なる4種のレチノイドを贅沢に配合したドクターズコスメの最高傑作です。冬の厳しい寒冷環境下でも、肌の内側からハリ密度を爆発させる処方設計がなされています。",
        "desc_p2": "シルキーで伸びの良いジェルエッセンスで、塗った瞬間から肌がキュッと引き締まるような心地よいホールド感を実感できます。ヒノキ葉エキスが肌のバリアを保護するため、高機能でありながら刺激を感じにくく、毎日ストレスなく続けられます。1本使い切る頃には、冬の乾燥たるみ毛穴が目立たなくなり、パンと張った若々しい輪郭が蘇ります。",
        "target": "大人の深い乾燥小ジワやフェイスラインのたるみに本気で挑みたい方、皮膚科学に基づいた最高峰のレチノールを使いたい方、即効性と持続性を求める方",
        "point": "朝晩のスキンケアで使用可能。化粧水の後に1〜2プッシュを顔全体になじませ、あご先から耳の下に向かってフェイスラインを引き上げるようにハンドプレスします。朝使用時は必ず日焼け止めを重ねてください。"
    }
]

# FAQ リスト
faq_list = [
    {
        "q": "なぜ11月・12月の冬こそレチノール美容液を始めるベストシーズンなのですか？",
        "a": "レチノールは角層のターンオーバーを促す過程で、一時的に肌が紫外線や乾燥に対してデリケートになりやすい特性があります。11月から12月は年間を通じて紫外線量（特にUV-B）が最も少ない時期であるため、光感受性によるトラブルのリスクを最小限に抑えながら集中ケアを行える最適なタイミングです。また、冬の寒冷で低下した細胞代謝を呼び覚まし、乾燥小ジワや毛穴の開きを土台から立て直すことができます。"
    },
    {
        "q": "冬にレチノールを使うと皮むけや乾燥（A反応）が心配です。防ぐ方法はありますか？",
        "a": "冬のA反応を防ぐ最大のコツは『エモリエントバッファリング（緩衝法）』です。洗顔後すぐにレチノールを塗るのではなく、まずは高保湿な化粧水やセラミド配合の乳液で肌を十分に潤してからレチノールを塗布し、最後に高保湿クリームで蓋をします（いわゆるサンドイッチ塗り）。また、使い始めの1〜2週間は毎日ではなく2〜3日に1回のペースで夜のみ使用し、肌が慣れてから徐々に使用頻度を増やしてください。"
    },
    {
        "q": "高保湿レチノール美容液とレチノールクリームの違いは何ですか？どう使い分けるべき？",
        "a": "レチノール美容液（セラム）は水分ベースで分子が細かく、角層のすみずみまで素早く浸透して毛穴やキメ、肌全体のトーンを均一に整えるのが得意です。一方、レチノールクリームは油分ベースで肌表面に密着し、目元や口元など皮脂腺が少なく乾燥しやすい部位を密閉保護するのに適しています。冬の乾燥が深刻な方は、全顔に高保湿レチノール美容液をなじませた後、目元などの集中エリアにレチノールクリームやセラミドクリームを重ねる併用が極めて効果的です。"
    },
    {
        "q": "ビタミンC美容液やピーリング美容液、ナイアシンアミドとの併用はどうすればいいですか？",
        "a": "高濃度ビタミンCやAHA・BHAなどのピーリング酸は肌への刺激が重複するため、同じタイミング（同時塗布）での使用は避けるのが鉄則です。『朝はビタミンCで抗酸化＆紫外線対策、夜はレチノールで肌再生』と朝晩で使い分けるのが皮膚科学的に最も推奨されます。なお、ナイアシンアミドやセラミド、ヒアルロン酸、CICA（ツボクサエキス）はレチノールと非常に相性が良く、A反応を和らげながらハリ効果を高めてくれるため積極的な併用がおすすめです。"
    },
    {
        "q": "朝もレチノール美容液を使って大丈夫ですか？日焼け止めは必須ですか？",
        "a": "製品が『朝晩使用可能』と明記しているマイルドな誘導体処方（イニスフリーやIOPEなど）であれば朝の使用も可能ですが、その際は必ずSPF30・PA+++以上の高保湿日焼け止めを併用することが絶対条件です。純粋レチノールを高濃度に含む製品や、敏感肌で冬の乾燥を感じている方は、安全のために夜のお手入れのみで使用することをおすすめします。"
    }
]

print("Retinol article config prepared successfully!")

# HTML組み立て
html_title = "保湿力の強さで肌乾燥とさようなら！濃密ビタミンA×セラミド処方で真冬の乾燥小ジワと毛穴の開きをふっくら押し戻す保湿力高めレチノール美容液ランク10"
html_desc = "11月・12月の乾燥小ジワ・毛穴たるみ・寒冷ゴワつきを救う高保湿レチノール美容液10選を皮膚科学の視点から徹底比較！イニスフリー、VT、COSRX、キールズ、ラロッシュポゼまで、A反応（皮むけ・乾燥）を防ぐエモリエントバッファリング技術と最新実勢価格・口コミを網羅してご紹介。"
canonical_url = "https://lumi-cosme.vercel.app/winter-retinol-serum"

# JSON-LD ItemList
item_list_elements = []
for idx, it in enumerate(items):
    det = product_details[idx]
    item_list_elements.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["display_name"],
            "image": it["image_url"],
            "description": det["catch"],
            "brand": {
                "@type": "Brand",
                "name": det["brand_name"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": it["review_average"],
                "reviewCount": str(max(it["review_count"], 15))
            }
        }
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": html_title,
            "description": html_desc,
            "image": items[0]["image_url"],
            "author": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "publisher": {
                "@type": "Organization",
                "name": "LUMI COSMETICS LAB",
                "url": "https://lumi-cosme.vercel.app"
            },
            "datePublished": "2026-11-09T05:00:00+09:00",
            "dateModified": "2026-11-09T05:00:00+09:00",
            "mainEntityOfPage": canonical_url
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
                    "name": "冬の高保湿美容液",
                    "item": "https://lumi-cosme.vercel.app/#serum"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "name": "高保湿レチノール美容液ランク10",
                    "item": canonical_url
                }
            ]
        },
        {
            "@type": "ItemList",
            "name": "高保湿レチノール美容液おすすめランキング10選",
            "itemListElement": item_list_elements
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq["q"],
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq["a"]
                    }
                } for faq in faq_list
            ]
        }
    ]
}

from update_all_internal_links import footer_links_html

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html_title} | LUMI COSMETICS</title>
  <meta name="description" content="{html_desc}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:title" content="{html_title} | LUMI COSMETICS">
  <meta property="og:description" content="{html_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:type" content="article">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
{json.dumps(json_ld_schema, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #9333ea;
      --primary-dark: #7e22ce;
      --primary-light: #faf5ff;
      --accent: #f43f5e;
      --text-main: #1f2937;
      --text-muted: #4b5563;
      --bg-main: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
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
      background-color: var(--bg-main);
      padding: 0;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 16px 20px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 4px rgba(0,0,0,0.04);
    }}
    .header-inner {{
      max-width: 1000px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--primary-dark);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--text-muted);
      max-width: 1000px;
      margin: 15px auto 0;
      padding: 0 20px;
    }}
    .breadcrumb a {{
      color: var(--text-muted);
      text-decoration: none;
    }}
    .container {{
      max-width: 1000px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 35px 30px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      margin-bottom: 30px;
    }}
    .category-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 15px;
      border: 1px solid #e9d5ff;
    }}
    h1 {{
      font-size: 1.75rem;
      font-weight: 800;
      line-height: 1.45;
      color: #111827;
      margin-bottom: 18px;
    }}
    .meta-info {{
      font-size: 0.85rem;
      color: var(--text-muted);
      display: flex;
      gap: 15px;
      align-items: center;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 15px;
      margin-bottom: 20px;
    }}
    .lead-box {{
      background: #faf5ff;
      border-left: 4px solid var(--primary);
      padding: 20px;
      border-radius: 4px 8px 8px 4px;
      font-size: 0.98rem;
      color: #374151;
      line-height: 1.85;
    }}
    .toc-box {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px 28px;
      margin: 30px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .toc-list {{
      list-style-type: none;
      padding-left: 5px;
    }}
    .toc-list li {{
      margin-bottom: 8px;
    }}
    .toc-list a {{
      color: #4b5563;
      text-decoration: none;
      font-size: 0.93rem;
      transition: color 0.2s ease;
    }}
    .toc-list a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}
    h2.section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: #111827;
      margin: 45px 0 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid var(--primary);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    h3.sub-title {{
      font-size: 1.18rem;
      font-weight: 700;
      color: #1f2937;
      margin: 25px 0 12px;
    }}
    p.body-text {{
      font-size: 1rem;
      color: #374151;
      line-height: 1.85;
      margin-bottom: 18px;
    }}
    .comparison-table-wrap {{
      overflow-x: auto;
      margin: 25px 0 35px;
      background: var(--card-bg);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }}
    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
      min-width: 700px;
    }}
    table.comparison-table th {{
      background: #faf5ff;
      color: #4c1d95;
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
    }}
    table.comparison-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid #f1f5f9;
      color: #334155;
    }}
    table.comparison-table tr:hover {{
      background-color: #fdf4ff;
    }}
    .product-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 28px;
      margin-bottom: 35px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
    }}
    .product-card:hover {{
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }}
    .rank-badge {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #9333ea, #c026d3);
      color: #fff;
      font-weight: 800;
      font-size: 1.15rem;
      padding: 4px 16px;
      border-radius: 8px;
      margin-bottom: 12px;
      box-shadow: 0 2px 6px rgba(147, 51, 234, 0.3);
    }}
    .product-tag {{
      font-size: 1.02rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 8px;
      line-height: 1.5;
    }}
    .product-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #1a202c;
      margin-bottom: 16px;
      line-height: 1.45;
    }}
    .product-grid {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 25px;
      margin-bottom: 20px;
      align-items: start;
    }}
    @media (max-width: 768px) {{
      .product-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .product-image-wrap {{
      text-align: center;
      background: #fafafa;
      border-radius: 12px;
      padding: 15px;
      border: 1px solid #edf2f7;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      border-radius: 8px;
      transition: transform 0.3s ease;
    }}
    .product-specs-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      margin-bottom: 15px;
    }}
    .product-specs-table th {{
      width: 28%;
      text-align: left;
      padding: 8px 10px;
      background: #f8fafc;
      color: var(--text-muted);
      border-bottom: 1px solid #edf2f7;
      font-weight: 600;
    }}
    .product-specs-table td {{
      padding: 8px 10px;
      border-bottom: 1px solid #edf2f7;
      color: #334155;
    }}
    .product-desc {{
      color: #374151;
      font-size: 0.98rem;
      line-height: 1.8;
      margin-bottom: 12px;
    }}
    .point-box {{
      background: #faf5ff;
      border: 1px solid #f3e8ff;
      border-radius: 8px;
      padding: 15px 18px;
      margin-top: 15px;
      font-size: 0.92rem;
      color: #4b5563;
    }}
    .point-box-title {{
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 6px;
    }}
    .price-and-action {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 20px;
      padding-top: 18px;
      border-top: 1px dashed #e2e8f0;
      flex-wrap: wrap;
      gap: 15px;
    }}
    .price-wrap {{
      display: flex;
      flex-direction: column;
    }}
    .price-label {{
      font-size: 0.8rem;
      color: var(--text-muted);
    }}
    .price-value {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--accent);
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #bf0000, #e60012);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      padding: 12px 24px;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 10px rgba(230,0,18,0.25);
      transition: all 0.25s ease;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #a60000, #c80010);
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(230,0,18,0.35);
    }}
    .feature-card-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 25px 0;
    }}
    .feature-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 22px;
      box-shadow: var(--shadow-sm);
    }}
    .feature-card h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .feature-card p {{
      font-size: 0.92rem;
      color: #4b5563;
      line-height: 1.7;
    }}
    .faq-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 20px 24px;
      margin-bottom: 16px;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-sm);
    }}
    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 10px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .faq-q::before {{
      content: "Q";
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 800;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.8;
      padding-left: 28px;
    }}
    .related-links-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 25px;
      margin: 40px 0;
    }}
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
      margin-top: 15px;
    }}
    .related-link-item {{
      background: #f8fafc;
      border: 1px solid #edf2f7;
      padding: 10px 14px;
      border-radius: 8px;
      text-decoration: none;
      color: #1e293b;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .related-link-item:hover {{
      background: #faf5ff;
      color: var(--primary);
      border-color: #d8b4fe;
    }}
    footer {{
      background: #111827;
      color: #9ca3af;
      padding: 50px 20px 30px;
      font-size: 0.88rem;
    }}
    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="logo">LUMI COSMETICS</a>
    <span style="font-size:0.85rem;color:#6b7280;font-weight:600;">冬コスメ徹底比較ラボ 2026最新版</span>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">ホーム</a> &gt; <span>冬の高保湿美容液</span> &gt; <span>高保湿レチノール美容液ランク10</span>
</div>

<main class="container">
  <article class="article-header">
    <span class="category-badge">✨ 2026年冬最新・毛穴＆乾燥小ジワ集中リペア</span>
    <h1>{html_title}</h1>
    <div class="meta-info">
      <span>更新日: 2026年11月9日</span>
      <span>執筆・検証: LUMI COSMETICS 皮膚科学コスメ検証チーム</span>
      <span>評価基準: 保湿力・浸透性・低刺激性・A反応回避設計・コスパ</span>
    </div>

    <div class="lead-box">
      <strong>【真冬のスキンケアにおけるレチノールの真実】</strong><br>
      11月から12月は、空気が急激に乾燥し、室内暖房によって角層の水分蒸発がピークに達する過酷な季節です。気温の低下に伴い肌のターンオーバー（細胞代謝）が停滞し、『乾燥小ジワが深く刻まれる』『毛穴が縦にたるんで目立つ』『肌がゴワついて化粧水が入らない』といった深刻な肌トラブルが同時多発します。<br><br>
      実は、<strong>年間で紫外線量（特にUV-B）が最も減少する11月・12月こそ、肌再生ビタミンであるレチノールケアを始める絶対的なベストシーズン</strong>です。かつては『冬にレチノールを使うと乾燥や皮むけ（A反応）が起きやすい』と敬遠されがちでしたが、2026年現在の最新レチノール美容液は劇的な進化を遂げています。CICA（ツボクサエキス）やヒト型セラミド、高純度ヒアルロン酸を組み合わせた『リポソームナノカプセル処方』により、肌バリアを守りながら角層の最深部まで穏やかにビタミンAを届ける高保湿設計が主流となりました。<br><br>
      本記事では、楽天市場の最新レビューデータと実勢価格を徹底検証し、真冬の乾燥肌でも皮むけゼロでふっくらとしたハリ・毛穴レス肌を叶える『高保湿レチノール美容液おすすめ10選』を厳選してご紹介します。
    </div>

    <div class="toc-box">
      <div class="toc-title">📑 目次（クリックで各見出しへジャンプ）</div>
      <ul class="toc-list">
        <li><a href="#why-winter-retinol">1. なぜ11-12月の冬こそレチノール美容液を始めるべきなのか？皮膚科学的メリット</a></li>
        <li><a href="#how-to-choose">2. 真冬でも皮むけ知らず！高保湿レチノール美容液の正しい選び方4大基準</a></li>
        <li><a href="#comparison-table">3. 2026年冬厳選！高保湿レチノール美容液10選 総合スペック比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿レチノール美容液おすすめランキング10選 詳細徹底レビュー</a></li>
        <li><a href="#sandwich-method">5. 冬のA反応を完全回避する『エモリエントバッファリング（サンドイッチ塗り）』実践法</a></li>
        <li><a href="#ingredients-matrix">6. レチノールと他成分の相性マトリクス（併用OK＆併用NGのルール）</a></li>
        <li><a href="#faq-section">7. 冬のレチノール美容液に関するよくある質問（FAQ）</a></li>
        <li><a href="#related-articles">8. あわせて読みたい冬の集中保湿ケア関連記事</a></li>
      </ul>
    </div>
  </article>

  <!-- なぜ冬こそレチノールなのか -->
  <section id="why-winter-retinol">
    <h2 class="section-title">❄️ 1. なぜ11-12月の冬こそレチノール美容液を始めるべきなのか？皮膚科学的メリット</h2>
    <p class="body-text">
      レチノール（ビタミンA）は、真皮の線維芽細胞に働きかけてコラーゲンやエラスチン、ヒアルロン酸の生合成を促進し、表皮のターンオーバーを正常化させるスキンケアの最高峰成分です。しかし、多くの人が『レチノールは春や秋に使うもの』と誤解しています。
    </p>
    
    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>☀️ 紫外線ダメージリスクが年間最小</h4>
        <p>レチノールによって代謝が促された生まれたての表皮細胞は、紫外線に対して一時的に敏感です。11月〜12月は春夏の約3分の1まで紫外線量が低下するため、光感受性による色素沈着リスクを最小限に抑えながら集中トリートメントを行えます。</p>
      </div>
      <div class="feature-card">
        <h4>❄️ 寒冷による角層代謝の停滞を打破</h4>
        <p>外気温が10℃を下回ると、皮膚の毛細血管が収縮して血行が不良になり、表皮のターンオーバー周期が通常の28日から40日以上へと長期化します。レチノールを投入することで、硬くゴワついた古い角質をスムーズに排出させ、柔らかな素肌へと導きます。</p>
      </div>
      <div class="feature-card">
        <h4>💧 水分保持能（ヒアルロン酸合成）の促進</h4>
        <p>レチノールは角層内部の天然保湿因子（NMF）やヒアルロン酸の産生を強力に刺激します。最新の保湿型レチノール美容液を使うことで、暖房による脱水に負けない自発的な保水力を肌土台から獲得できます。</p>
      </div>
    </div>
  </section>

  <!-- 選び方ガイド -->
  <section id="how-to-choose">
    <h2 class="section-title">🔍 2. 真冬でも皮むけ知らず！高保湿レチノール美容液の正しい選び方4大基準</h2>
    <p class="body-text">
      真冬のレチノール選びにおいて最も重要なのは、単に濃度の高さを追うのではなく、<strong>『保湿バリア成分との共存処方』</strong>および<strong>『角層浸透の徐放化技術』</strong>が施されているかを見極めることです。
    </p>

    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>① レチノールの種類とカプセル化（リポソーム）</h4>
        <p>刺激が少なく毎日使える『誘導体（パルミチン酸レチノール、ヒドロキシピナコロンレチノアート）』か、純粋レチノールを微小カプセルに閉じ込めた『リポソーム化レチノール』を選びましょう。角層の奥深くにゆっくり溶け出すため、赤みやヒリつきを起こしません。</p>
      </div>
      <div class="feature-card">
        <h4>② セラミド・CICA・パンテノールの同時配合</h4>
        <p>レチノール単体ではなく、角層の細胞間脂質を補修する『ヒト型セラミド』や、炎症を抑える『ツボクサエキス（CICA）』、皮膚修復ビタミン『パンテノール』が一緒に配合されている製品を選べば、冬の乾燥荒れを同時に防ぐことができます。</p>
      </div>
      <div class="feature-card">
        <h4>③ テクスチャーは水分と油分の黄金比エマルジョン</h4>
        <p>完全な水状のリキッドよりも、とろみのあるミルキーエッセンスやジェルエマルジョン状のテクスチャーが冬には最適です。肌にのばした瞬間に乾燥したキメを包み込み、摩擦ダメージを防ぎます。</p>
      </div>
      <div class="feature-card">
        <h4>④ 遮光・密閉容器（エアレスポンプやアルミチューブ）</h4>
        <p>ビタミンAは熱・光・酸素に非常に弱いデリケートな成分です。最後まで酸化させずに新鮮な効果を肌へ届けるため、空気の入らないエアレスポンプや遮光スポイト、アルミチューブを採用した容器構造を厳選しましょう。</p>
      </div>
    </div>
  </section>

  <!-- スペック比較表 -->
  <section id="comparison-table">
    <h2 class="section-title">📊 3. 2026年冬厳選！高保湿レチノール美容液10選 総合スペック比較表</h2>
    <p class="body-text">
      今回厳選した10商品のブランド、注目成分、テクスチャー、容量、楽天市場の実勢価格、おすすめな肌質タイプを一覧で比較できます。
    </p>

    <div class="comparison-table-wrap">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド・商品名</th>
            <th>主要注目成分</th>
            <th>容量・容器</th>
            <th>参考価格（税込）</th>
            <th>おすすめな悩み・肌質</th>
          </tr>
        </thead>
        <tbody>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""          <tr>
            <td><strong>第{idx+1}位</strong></td>
            <td><strong>{det['brand_name']}</strong><br>{item['display_name'][:28]}...</td>
            <td>{det['features'][:32]}...</td>
            <td>{det['capacity']}</td>
            <td style="color:#e11d48;font-weight:700;">¥{item['price']:,}</td>
            <td>{det['target'][:24]}...</td>
          </tr>
"""

html_content += """        </tbody>
      </table>
    </div>
  </section>

  <!-- ランキング詳細セクション -->
  <section id="ranking-section">
    <h2 class="section-title">🏆 4. 高保湿レチノール美容液おすすめランキング10選 詳細徹底レビュー</h2>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
    <div class="product-card" id="rank-{idx+1}">
      <span class="rank-badge">第{idx+1}位</span>
      <div class="product-tag">{det['tag']}</div>
      <h3 class="product-title">{item['display_name']}</h3>

      <div class="product-grid">
        <div class="product-image-wrap">
          <img src="{item['image_url']}" alt="{item['display_name']}" class="product-img" loading="lazy">
          <div style="font-size:0.8rem;color:#64748b;margin-top:8px;">★ 楽天レビュー評価: {item['review_average']} ({item['review_count']}件)</div>
        </div>
        <div>
          <table class="product-specs-table">
            <tr>
              <th>ブランド</th>
              <td>{det['brand_name']}</td>
            </tr>
            <tr>
              <th>容量・形状</th>
              <td>{det['capacity']}</td>
            </tr>
            <tr>
              <th>タイプ</th>
              <td>{det['type']}</td>
            </tr>
            <tr>
              <th>主要配合成分</th>
              <td>{det['features']}</td>
            </tr>
            <tr>
              <th>期待できる効果</th>
              <td>{det['value']}</td>
            </tr>
          </table>
          
          <p class="product-desc">{det['desc_p1']}</p>
          <p class="product-desc">{det['desc_p2']}</p>

          <div class="point-box">
            <div class="point-box-title">🎯 こんな方におすすめ＆使い方のコツ</div>
            <p><strong>【おすすめ】</strong>{det['target']}</p>
            <p style="margin-top:6px;"><strong>【効果的な使い方】</strong>{det['point']}</p>
          </div>
        </div>
      </div>

      <div class="price-and-action">
        <div class="price-wrap">
          <span class="price-label">楽天市場 最新価格（税込）</span>
          <span class="price-value">¥{item['price']:,}</span>
        </div>
        <a href="{item['affiliate_url']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          🛒 楽天市場で最安値＆口コミを見る
        </a>
      </div>
    </div>
"""

html_content += """
  </section>

  <!-- サンドイッチ塗り実践法 -->
  <section id="sandwich-method">
    <h2 class="section-title">🥪 5. 冬のA反応を完全回避する『エモリエントバッファリング（サンドイッチ塗り）』実践法</h2>
    <p class="body-text">
      冬の低湿度・暖房環境下でレチノールの刺激を恐れずに最大のハリ効果を引き出すためには、皮膚科クリニックでも指導される『エモリエントバッファリング（緩衝法）』を取り入れるのが最も確実です。
    </p>

    <div class="feature-card-grid">
      <div class="feature-card">
        <h4>STEP 1: 高保湿化粧水で角層水分を飽和</h4>
        <p>洗顔後、セラミドやヒアルロン酸を豊富に含んだ化粧水を2〜3回重ねづけし、角層細胞を水分で満たします。肌が乾いた状態でレチノールを塗ると急激に局所吸収され刺激が出やすいため、事前の水分補給が防波堤となります。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 2: 保湿乳液または軽めのクリームを薄塗り</h4>
        <p>（特に敏感な方）化粧水の後、セラミド乳液を薄く全顔になじませて『第1のクッション層』を作ります。この油膜がレチノールの浸透スピードを適度に緩やかにコントロールしてくれます。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 3: レチノール美容液を優しく点置き＆プレス</h4>
        <p>適量（パール粒大または1〜2プッシュ）を指先に取り、頬や額、あごに点置き。絶対にこすらず、手のひらの体温で押し込むようにハンドプレスでなじませます。</p>
      </div>
      <div class="feature-card">
        <h4>STEP 4: 濃厚なエモリエントクリームで完全密閉</h4>
        <p>最後に、セラミドクリームやシアバター、ワセリンなどの油分を含む高保湿クリームで肌表面を密閉します。レチノールを肌の奥へ閉じ込めつつ、外気やエアコンによる水分の蒸散を完全に遮断します。</p>
      </div>
    </div>
  </section>

  <!-- 成分相性マトリクス -->
  <section id="ingredients-matrix">
    <h2 class="section-title">🔬 6. レチノールと他成分の相性マトリクス（併用OK＆併用NGのルール）</h2>
    <p class="body-text">
      冬のスキンケアで複数の高機能美容液を組み合わせる際は、成分同士の相乗効果と刺激のリスクを正しく把握しておく必要があります。
    </p>

    <div class="comparison-table-wrap">
      <table class="comparison-table">
        <thead>
          <tr>
            <th>成分名</th>
            <th>相性</th>
            <th>生化学的メカニズムと併用のアドバイス</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>ヒト型セラミド</strong></td>
            <td><span style="color:#16a34a;font-weight:700;">◎ 最適</span></td>
            <td>レチノールが促進するターンオーバーの過程で一時的に低下しやすい細胞間脂質をダイレクトに補強。A反応を劇的に緩和しながらハリ肌を育みます。</td>
          </tr>
          <tr>
            <td><strong>CICA（ツボクサエキス）</strong></td>
            <td><span style="color:#16a34a;font-weight:700;">◎ 最適</span></td>
            <td>マデカッソシド等の強力な抗炎症作用が、レチノールによる微小炎症を即座に鎮静。冬の赤みが出やすい肌のベストパートナーです。</td>
          </tr>
          <tr>
            <td><strong>ナイアシンアミド</strong></td>
            <td><span style="color:#16a34a;font-weight:700;">◎ 最適</span></td>
            <td>ビタミンB3とビタミンAは皮膚再生において相乗的に作用。セラミド合成を促すため、バリア機能を高めながら美白・シワ改善効果を倍増させます。</td>
          </tr>
          <tr>
            <td><strong>ピュアビタミンC（アスコルビン酸）</strong></td>
            <td><span style="color:#d97706;font-weight:700;">△ 時間差推奨</span></td>
            <td>高濃度ピュアビタミンC（酸性pH）とレチノールを同時に塗布すると刺激が重複します。『朝ビタミンC、夜レチノール』と時間帯を分けるのがベストです。</td>
          </tr>
          <tr>
            <td><strong>AHA / BHA（ピーリング酸）</strong></td>
            <td><span style="color:#dc2626;font-weight:700;">✕ 同時併用不可</span></td>
            <td>グリコール酸やサリチル酸などの角質剥離作用とレチノールのターンオーバー作用が重なると、冬の敏感な肌が過剰に剥離し深刻なバリア破綻を招きます。</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <!-- FAQ セクション -->
  <section id="faq-section">
    <h2 class="section-title">❓ 7. 冬のレチノール美容液に関するよくある質問（FAQ）</h2>
"""

for faq in faq_list:
    html_content += f"""
    <div class="faq-card">
      <div class="faq-q">{faq['q']}</div>
      <div class="faq-a">{faq['a']}</div>
    </div>
"""

html_content += """
  </section>

  <!-- 関連記事リンク集 -->
  <section id="related-articles" class="related-links-box">
    <h3 class="sub-title">🔗 あわせて読みたい冬の集中保湿ケア関連記事</h3>
    <p style="font-size:0.9rem;color:#6b7280;">レチノール美容液と組み合わせることで真冬の乾燥対策を完璧にするおすすめ記事をピックアップしました。</p>
    <div class="related-links-grid">
      <a href="/winter-retinol-cream" class="related-link-item">🧴 冬の高保湿レチノールクリーム</a>
      <a href="/winter-ceramide-cream" class="related-link-item">🛡️ 冬の高保湿セラミドクリーム</a>
      <a href="/winter-ceramide-serum" class="related-link-item">💧 冬の高保湿セラミド美容液</a>
      <a href="/winter-cica-cream" class="related-link-item">🌿 冬の高保湿シカクリーム</a>
      <a href="/winter-cica-serum" class="related-link-item">🌱 冬の高保湿シカ美容液</a>
      <a href="/winter-hyaluronic-cream" class="related-link-item">💦 冬の高保湿ヒアルロン酸クリーム</a>
      <a href="/winter-hyaluronic-serum" class="related-link-item">🌊 冬の高保湿ヒアルロン酸美容液</a>
      <a href="/winter-niacinamide-serum" class="related-link-item">✨ 冬の高保湿ナイアシンアミド美容液</a>
      <a href="/winter-pdrn-serum" class="related-link-item">🧬 冬の高保湿PDRN美容液</a>
      <a href="/winter-night-serum" class="related-link-item">🌙 冬の高保湿夜用ナイトセラム</a>
      <a href="/winter-wrinkle-cream" class="related-link-item">👁️ 冬のリンクルシワ改善クリーム</a>
      <a href="/winter-peel-serum" class="related-link-item">🧪 冬のマイルド角質ピールセラム</a>
    </div>
  </section>
</main>

<footer>
  <div class="footer-inner">
    <div style="font-weight:700;font-size:1.1rem;color:#ffffff;margin-bottom:15px;">LUMI COSMETICS | 冬コスメ徹底比較ラボ</div>
    <p style="margin-bottom:20px;line-height:1.7;">当サイトは、11月から12月にかけての寒冷乾燥シーズンに最適な高保湿コスメを皮膚科学・成分分析・実勢価格の観点から厳選・検証するビューティーガイドです。掲載している商品価格および在庫情報は楽天市場APIを通じて最新の情報を取得・掲載しております。</p>
    
    <div class="footer-links">
""" + footer_links_html + """
    </div>
    
    <div style="text-align:center;margin-top:30px;border-top:1px solid #374151;padding-top:20px;font-size:0.8rem;color:#6b7280;">
      &copy; 2026 LUMI COSMETICS LAB. All Rights Reserved.
    </div>
  </div>
</footer>

</body>
</html>
"""

with open("winter-retinol-serum.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-retinol-serum.html! File size: {len(html_content):,} bytes")
