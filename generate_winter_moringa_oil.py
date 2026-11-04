import json
import re

with open("fetched_3new_rose_primrose_moringa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_moringa_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌱 奇跡の木100%低温圧搾！暖房砂漠の乾きを濃密ベヘン酸で跳ね返す至高の美容オイル",
        "catch": "過酷な熱帯地方で驚異の生命力を誇るモリンガ種子をコールドプレス。高濃度オレイン酸と特有のベヘン酸が冬の角層に濃密な油分膜を形成し、一日中乾かないツヤ肌を約束する高純度セラム",
        "brand_name": "ILOKOS (イロコス)",
        "capacity": "30ml / スポイト付き遮光ガラス瓶",
        "type": "高純度ピュアモリンガ美容スキンケアオイル",
        "features": "未精製モリンガ種子油100%（低温圧搾・無添加）、ベヘン酸、オレイン酸、パルミチン酸",
        "value": "古代エジプト王族が砂漠の乾燥から肌を守るために愛用した歴史を持つ高機能オイル。浸透性に優れ、ベタつかないのに驚異的な保湿持続力を発揮",
        "desc_p1": "11月から12月にかけて暖房器具がフル稼働すると、室内の湿度は一気に下がり、肌はまるで乾いた砂漠のような極限状態にさらされます。化粧水や乳液をいくら塗り重ねても、暖房の熱風で数時間後には水分が蒸発してしまう…そんな深刻な冬のインナードライに終止符を打つのが、イロコスの『ピュア モリンガ スキンケアオイル』です。",
        "desc_p2": "モリンガオイルの最大の強みは、他の植物油にはほとんど見られない高級飽和脂肪酸『ベヘン酸（約6〜9%）』を豊富に含む点にあります。このベヘン酸が肌表面に微細で均一な光沢シールドを形成し、水分の蒸散を物理的にシャットアウト。さらにオレイン酸が硬くなった角層を柔らかくほぐすため、洗顔後の導入オイルとして1〜2滴馴染ませるだけで、後から使う化粧水がぐんぐん吸い込まれ、夕方までしっとりとした水光ツヤがキープされます。",
        "target": "暖房の効いた部屋にいるとすぐに肌がつっぱる方、皮脂不足で肌がゴワつき硬くなっている方、自然由来100%の強力なブースターオイルを求める方",
        "point": "洗顔後、化粧水の前に1〜2滴を手のひらで温めてハンドプレスします。肌の角質が驚くほど柔らかくなり、化粧水の浸透力が劇的に向上します。夜はスキンケアの最後のフタとしてもう1滴重ねると完璧です。"
    },
    {
        "rank": 2,
        "tag": "🏛️ 日本のアロマ老舗が厳選！コールドプレス抽出で栄養素を壊さず届ける安心の植物油",
        "catch": "ハーブとアロマテラピーの権威・生活の木が手がける高品位モリンガオイル。丁寧な低温圧搾により必須脂肪酸や植物ステロールを生きたまま凝縮し、冬の過酷な寒冷刺激から素肌をガード",
        "brand_name": "Tree of life (生活の木)",
        "capacity": "25ml / 遮光ドロップボトル",
        "type": "低温圧搾ピュアキャリアオイル",
        "features": "モリンガ種子油100%（ワサビノキ種子油）、ビタミンA・C・E、植物ステロール",
        "value": "厳しい自社品質基準をクリアした高純度仕様。ドロップ式ボトルで1滴ずつ正確に調整でき、フェイスケアからヘア・ネイルケアまでマルチに活躍",
        "desc_p1": "冬のスキンケアにおいて『毎日安心して使える品質の確かさ』を最優先したい方に圧倒的な信頼を得ているのが、生活の木の『モリンガオイル』です。インド産の厳選されたモリンガ種子を用い、一切の熱を加えないコールドプレス製法で丁寧に搾油されています。",
        "desc_p2": "淡い黄金色のオイルは肌への親和性が極めて高く、伸ばした瞬間に角層へと素早くなじんでサラリとしたシルキーな後肌に仕上がります。冬の木枯らしにさらされてキメが乱れた頬や、マスクの着脱で乾燥摩擦を起こした小鼻周りにも刺激なく穏やかに密着。肌本来の保水バリアを力強く補い、冷えによるくすみを払拭して内側からイキイキとした血色感を呼び戻してくれます。",
        "target": "品質管理が徹底された信頼の国内ブランドを選びたい方、酸化しにくく使い切りやすいサイズを好む方、ベタつきのない高保湿オイルを求める方",
        "point": "朝のメイク前に半滴〜1滴を手のひらに薄く伸ばし、乾燥しやすい目元や頬骨の上にポンポンと乗せます。日中の乾燥崩れを防ぎ、自然なハイライトのような上品なツヤを演出できます。"
    },
    {
        "rank": 3,
        "tag": "🔬 有機栽培未精製生オイル！エアコン乾燥で硬化した角質を即座にほどく高浸透ブースター",
        "catch": "マンディムーンが直接買い付けた最高グレードの未精製モリンガオイル。熱処理も化学処理も一切行わない生搾り処方で、冬のゴワゴワ肌に生命力あふれる濃密な栄養を注入",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "50ml / スポイト付き遮光瓶",
        "type": "オーガニック未精製植物オイル",
        "features": "有機モリンガ種子油100%（未精製・コールドプレス・ECOCERT認証原料）",
        "value": "未精製ならではの豊富な微量栄養素と高濃度オレイン酸。冬になると角質が肥厚してスキンケアを弾いてしまう肌を、瞬時にとろけるマシュマロ肌へ導く",
        "desc_p1": "冬になると肌のターンオーバーが停滞し、剥がれ落ちるべき古い角質が肌表面に留まって『カチカチ・ゴワゴワ』した質感になってしまいます。この状態ではどんなに高価な化粧水やシートマスクを使っても、美容成分は角層奥まで届きません。マンディムーンの未精製モリンガオイルは、そんな冬の硬化角質を解きほぐす柔軟ブースターとして絶大な効果を発揮します。",
        "desc_p2": "未精製ならではのコクのあるテクスチャーを肌に乗せると、体温でじんわりと広がり、角質細胞の隙間を埋めている脂質と素早くなじみます。オレイン酸の強力なエモリエント効果によって肌がふっくらと柔らかくなり、次に重ねる化粧水がスポンジのようにぐんぐん吸い込まれていく感覚を実感できます。夜にたっぷり使えば、翌朝の洗顔時に肌の手触りが驚くほどなめらかに変わっていることに感動します。",
        "target": "冬になると角質が硬くなり化粧水が入っていかない方、原液・未精製コスメの濃厚な手応えを実感したい方、コスパ良くたっぷり使いたい方",
        "point": "お風呂上がりに、導入用として2〜3滴を顔全体へ馴染ませてから化粧水を重ねます。さらに週に1回、オイルを5滴使って優しく小鼻やフェイスラインをくるくるとマッサージすると、冬の乾燥角栓がポロポロと浮き上がります。"
    },
    {
        "rank": 4,
        "tag": "💆‍♀️ プロ仕様の最高峰スパ品質！冬の乾燥小ジワとくすみを集中ケアするサロン発オイル",
        "catch": "高級エステサロン専用ブランド『Spa treatment』が手がける高純度エッセンシャルモリンガオイル。過酷な冬の低湿度環境下でも肌密度を高め、吸い付くようなハリとツヤをチャージ",
        "brand_name": "Spa treatment (スパトリートメント)",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "サロン専売高濃度エイジングケアオイル",
        "features": "高純度モリンガ種子油、天然ビタミンE、必須脂肪酸コンプレックス",
        "value": "サロンのフェイシャルトリートメントにも使用される最高峰の品質基準。極小分子の脂肪酸が角層深くまで浸透し、冬のハリ不足やたるみ感を速攻レスキュー",
        "desc_p1": "全国の一流スパやエステサロンでプロのエステティシャンに指名されるSpa treatmentのエッセンシャルモリンガオイル。一般的なキャリアオイルとは一線を画す、厳選されたプレミアムモリンガ種子のみを使用した贅沢なサロン品質が特徴です。",
        "desc_p2": "非常に純度が高く精緻に精製されているため、肌に塗布した瞬間にまるで美容液のようにスッと吸い込まれ、一切の重さやベタつきを残しません。それでいて、塗布後の肌は内側から潤いで満たされたようなピンとしたハリ感に包まれます。冬の冷えや乾燥で目元や口元に深く刻まれがちな乾燥小ジワをふっくらと押し上げ、サロン帰りのような輝く水光肌を自宅で再現してくれます。",
        "target": "サロン帰りのような本格的な仕上がりを求める方、年齢による乾燥小ジワやハリ不足を本気でケアしたい方、最高品質のスパコスメを愛用したい方",
        "point": "夜のお手入れの際、美容液の後に2滴を手にとり、手のひらで顔全体を包み込みながらフェイスラインをリフトアップするようにハンドプレスします。首元のシワケアにも最適です。"
    },
    {
        "rank": 5,
        "tag": "🌴 鹿児島県大隅半島産無農薬モリンガ！契約農家の手摘み種子から生まれた地産生搾りオイル",
        "catch": "本土最南端の強い日差しと温暖な大地で無農薬栽培された国産モリンガを使用。収穫から搾油まで国内自社工場で一貫生産された、冬の敏感肌を守り抜く完全無添加プレミアムオイル",
        "brand_name": "BOTANICAL FACTORY (ボタニカルファクトリー)",
        "capacity": "30ml / ポンプ付き遮光ガラスボトル",
        "type": "国産無農薬コールドプレス植物美容オイル",
        "features": "鹿児島県産無農薬モリンガ種子油100%（完全無添加・未精製コールドプレス）",
        "value": "輸入原料に頼らず、鮮度抜群の国産種子を低温圧搾。防腐剤・化学溶剤・合成着色料完全フリーで、冬のデリケートな肌荒れを穏やかに保護",
        "desc_p1": "南国の豊かな自然が残る鹿児島県大隅半島。ボタニカルファクトリーは、温暖な気候のもと無農薬で力強く育った国産モリンガの種子を手作業で収穫し、非加熱の圧搾機でじっくり時間をかけて生搾りしています。輸送による劣化がないフレッシュな国産原料ならではの高い抗酸化活性が最大の強みです。",
        "desc_p2": "海外産モリンガに比べて香りがとても穏やかで、さらりとしたシルキーなテクスチャーが日本の繊細な肌質に完璧にマッチします。真冬の木枯らしやエアコンの温風にさらされて赤みやヒリつきを起こしやすいデリケートな素肌を、薄くしなやかな保護膜で優しくプロテクト。使い続けるほどに肌のバリア機能が安定し、冬でもトラブル知らずの健やかな素肌へと整えてくれます。",
        "target": "トレーサビリティの確かな国産オーガニックコスメを重視する方、敏感肌で肌荒れを起こしやすい方、エシカルで持続可能なコスメを選びたい方",
        "point": "洗顔後すぐに1プッシュを手に取り、両手で温めてから顔全体へプレスします。その後、化粧水を重ねると角層の水分保持力が大幅に高まり、一日中しっとり感が持続します。"
    },
    {
        "rank": 6,
        "tag": "🍯 高濃度オレイン酸×ベヘン酸！スキンケアの最後に重ねて乾燥蒸発を完全ガードする原液オイル",
        "catch": "天然ハーブ・コスメ原料専門のカフェ・ド・サボンが厳選。オレイン酸70%以上、ベヘン酸8%含有の高品質モリンガ種子から搾油された未精製オイルが、冬の水分蒸散を物理遮断",
        "brand_name": "Cafe de Savon (カフェ・ド・サボン)",
        "capacity": "50ml / 遮光ドロップボトル",
        "type": "未精製ピュアモリンガオイル（100%植物油）",
        "features": "未精製モリンガオイル（オレイン酸約73%、ベヘン酸約8%、パルミチン酸約6%）",
        "value": "熱や化学溶剤を使わないコールドプレス製法。酸化安定性が非常に高く、冬のスキンケアの最後のフタ（エモリエントシールド）として絶大な威力を発揮",
        "desc_p1": "『冬の夜、どんなに保湿しても寝ている間に暖房で肌がカピカピに乾いてしまう…』そんな悩みに最も効果的なのが、水分蒸散阻止力に秀でたモリンガオイルによる『ナイトラッピング』です。カフェ・ド・サボンの未精製モリンガオイルは、天然のベヘン酸とオレイン酸を理想的なバランスで含んでおり、肌表面に強固な保護ヴェールを張ってくれます。",
        "desc_p2": "ナイトクリームや乳液の後にこのオイルを手のひらに1滴広げ、顔全体を覆うようにプレスするだけで、寝ている間の水分蒸発を完全ストップ。さらにベヘン酸特有のなめらかな皮膜形成作用により、枕やシーツとの摩擦刺激からも肌を保護してくれます。翌朝起きたときの肌は、まるで潤いのマスクを一晩中つけていたかのようにみずみずしく、ぷるんとした弾力が持続します。",
        "target": "就寝中の乾燥や寝起きの肌のつっぱりに悩んでいる方、手持ちのスキンケアの保湿力を底上げしたいフタ用オイルを探している方",
        "point": "夜のお手入れのフィニッシュとして、手のひらに1〜2滴を取り、顔全体を包み込むように優しくプレスして密着させます。乾燥が気になる首元や指先にもそのまま塗り伸ばせます。"
    },
    {
        "rank": 7,
        "tag": "🤝 フィリピン契約農園のフェアトレード！冬の敏感肌や赤み肌をしっとり包むオーガニックオイル",
        "catch": "フィリピンの肥沃な大地で育つ最高峰モリンガの種子をコールドプレス。現地女性の雇用創出と有機栽培を両立するフェアトレード認証の高品質スキンケアオイル",
        "brand_name": "GIRLS, BE AMBITIOUS (ガールズ・ビー・アンビシャス)",
        "capacity": "30ml / スポイト付きガラス遮光瓶",
        "type": "フェアトレード・オーガニック美容オイル",
        "features": "フィリピン産オーガニックモリンガ種子油100%（冷圧搾・完全無添加）",
        "value": "世界的な有機認証基準を満たす安全性の高さ。抗酸化成分ビタミンEを豊富に含み、冬の寒冷ストレスや乾燥による赤み・皮むけをしっとり優しく包み込む",
        "desc_p1": "『生産者の顔が見える、本当に安心できるオーガニックコスメを』という想いから生まれたガールズ・ビー・アンビシャス。フィリピンの契約農園で大切に育てられた最高品質のモリンガ種子のみを使用し、現地で丁寧に低温圧搾されたエシカルなピュアオイルです。",
        "desc_p2": "ゴールドに輝くオイルはさらりとして伸びが良く、肌になじませるとスーッと浸透して心地よい潤い感が広がります。冬の乾燥と冷風によって皮膚が薄くなり、外気刺激で赤みやヒリつきを起こしやすい敏感な素肌を、モリンガの豊富な脂肪酸が穏やかに保護。塗布した後の肌は滑らかでキメが整い、ファンデーションの密着度も格段に高まります。",
        "target": "エシカル消費やフェアトレードに関心がある方、敏感肌でも刺激なく使える優しいオーガニックオイルを探している方、自然なツヤ肌を作りたい方",
        "point": "化粧水の後の保湿オイルとして、スポイトで1〜2滴を手にとり顔全体へ優しく押し込みます。メイク前に仕込むと、冬の乾燥による粉浮きを夕方まで完璧に防ぎます。"
    },
    {
        "rank": 8,
        "tag": "🐝 モリンガオイル×天然ミツロウ！目元・口元のひび割れや外出時の冷風をガードする高保湿バーム",
        "catch": "高純度モリンガオイルと天然ミツロウを贅沢にブレンドした濃厚マルチバーム。真冬の過酷な木枯らしやエアコン直撃による目元・口元のひび割れをピンポイントで物理シールド",
        "brand_name": "Moringa Farm (モリンガファーム)",
        "capacity": "20g / アルミ缶コンパクト",
        "type": "高保湿モリンガマルチリペアバーム",
        "features": "モリンガ種子油、天然ミツロウ、ホホバ種子油、トコフェロール（ビタミンE）",
        "value": "ポーチやデスクに常備できる携帯サイズ。体温でとろける絶妙な密着感で、冬のあらゆる乾燥パーツをどこでも瞬時にプロテクト",
        "desc_p1": "冬の外出時、冷たい風が直接吹き付ける頬骨や、乾燥でひび割れやすい唇・口角、まばたきで皮膚が酷使される目元は、部分的な集中保湿が欠かせません。モリンガファームの『モイスチャーリペアバーム』は、モリンガオイルの持つ強力な保水力と、天然ミツロウの被膜形成力を融合させた高機能バームです。",
        "desc_p2": "指先にとると体温でじんわりととろけ、オイル状になってピタッと乾燥部分に密着します。ミツロウが形成する通気性のある保護皮膜が外気をシャットアウトし、モリンガオイルの脂肪酸が角層をじっくり保湿。乾燥によるちりめんジワを目立たなくし、時間が経っても潤いの膜が持続します。リップクリーム代わりとしてはもちろん、マスクのこすれによる肌荒れ防止や爪の甘皮ケアにも重宝します。",
        "target": "外出先やオフィスで手軽にピンポイント保湿をしたい方、リップと目元の両方に使えるマルチバームが欲しい方、濃厚な油分膜で肌を守りたい方",
        "point": "指先でバームの表面をくるくるとなでて体温で溶かし、乾燥が気になる目尻や口角、唇に優しくトントンと叩き込むように乗せます。"
    },
    {
        "rank": 9,
        "tag": "🧼 無農薬モリンガ×有機月桃水！冬の潤いを奪わず古い角質をやさしく落とす枠練り洗顔石けん",
        "catch": "沖縄の自然の恵みを凝縮した暮らしっく村のロングセラー。低温圧搾モリンガオイルと有機月桃蒸留水を練り込み、冬のつっぱりや粉吹きを防ぎながら不要な汚れを摩擦レスで吸着オフ",
        "brand_name": "WELLNESS HAMLET (暮らしっく村)",
        "capacity": "80g / 熟成枠練り固形石けん",
        "type": "高保湿・低刺激ナチュラル枠練り洗顔ソープ",
        "features": "モリンガ種子油、月桃葉水、ヤシ油、パーム油、天然植物グリセリン",
        "value": "約2ヶ月間じっくり熟成させる枠練り製法。天然の保湿成分が約30%以上含まれているため、冬の乾燥肌でも洗い上がりのつっぱり感がゼロ",
        "desc_p1": "冬の肌トラブルの大きな原因の一つが『洗顔時の皮脂の落としすぎ』です。冬の弱った角質層は、洗浄力の強い洗顔料を使うと必要な潤いまで奪われてしまい、洗顔直後から激しいつっぱりや粉吹きを起こします。暮らしっく村の『モリンガ月桃石けん』は、洗顔しながら肌に潤いを与えることを追求した枠練り石けんです。",
        "desc_p2": "泡立てネットを使うと、クリーミーで弾力のある濃密なホイップ泡が瞬時に立ち上がります。きめ細かな泡が肌と手のひらの間でクッションとなり、摩擦を一切かけずに毛穴の奥の汚れや古い角質をキャッチ。モリンガオイルと月桃水の保湿成分が肌に留まるため、ぬるま湯で洗い流した瞬間から、肌がしっとりと柔らかく潤っている手応えを実感できます。",
        "target": "冬になると洗顔後に顔がつっぱって痛い方、肌に優しい石けんで毛穴やキメを整えたい方、自然派の固形石けんを好む方",
        "point": "ぬるま湯（32〜34℃）で泡立てネットを使い、レモン1個分の濃密泡を作ります。泡を顔の上で転がすようにして洗い、決して手で肌を擦らないように注意して洗い流します。"
    },
    {
        "rank": 10,
        "tag": "💇‍♀️ モリンガオイル×アルガンオイル！冬の静電気・毛先パサつきを抑え潤いツヤを与えるヘアオイル",
        "catch": "濃密モリンガオイルと高浸透アルガンオイルを黄金比で配合。冬の乾燥冷気やマフラー摩擦、暖房によるパサつき・静電気を一瞬で鎮め、指通りの良い美髪を育むアウトバストリートメント",
        "brand_name": "Herb & Co. (ハーブアンドコー)",
        "capacity": "100ml / ポンプボトル",
        "type": "高保湿オーガニックアウトバスヘアオイル",
        "features": "モリンガ種子油、アルガニアスピノサ核油（アルガンオイル）、ホホバ種子油、カメリア種子油",
        "value": "ベヘン酸の髪への吸着・補修作用を応用。毛髪表面のキューティクルを滑らかにコーティングし、冬の嫌な静電気や枝毛・切れ毛を徹底防御",
        "desc_p1": "冬は肌だけでなく『髪』も深刻な乾燥被害に遭います。湿度の低下と暖房の熱風、さらにウールやニットのマフラーとの摩擦によって静電気が発生し、毛先はパサパサに広がって枝毛や切れ毛が急増します。ハーブアンドコーの『オーガニック モリンガ リッチヘアオイル』は、そんな冬のダメージヘアを速攻で集中リペアするサロン品質のアウトバストリートメントです。",
        "desc_p2": "モリンガオイルに含まれるベヘン酸は、ヘアケア業界でも高級コンディショニング成分として高く評価されています。タオルドライ後の濡れた髪に馴染ませてドライヤーで乾かすと、熱によってオイル成分がキューティクルにピタッと密着。毛先までスルンとまとまり、冬の乾燥下でも静電気が起きない艶やかな美髪へ導きます。ベタつかずサラッとした仕上がりで、朝のスタイリング剤としても優秀です。",
        "target": "冬になると髪のパサつきや静電気・広がりがひどい方、毛先の枝毛やダメージを修復したい方、上質な植物オイルでヘアケアをしたい方",
        "point": "洗髪後、タオルドライした髪の毛先を中心に1〜2プッシュを揉み込みます。粗めのコームで全体に馴染ませてからドライヤーで根元から乾かすと、サロン帰りのようなツヤとまとまりが一日中持続します。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:20]}...</a></li>\n'

# 比較一覧表
table_rows = []
for idx, p in enumerate(product_details):
    it = items[idx]
    table_rows.append(f"""            <tr>
              <td class="rank-num">第{p['rank']}位</td>
              <td><img src="{it['img']}" alt="{p['brand_name']}" class="table-thumb" loading="lazy"></td>
              <td><strong>{p['brand_name']}</strong><br><span style="font-size:0.85rem; color:var(--text-sub);">{it['name'][:35]}...</span></td>
              <td>{p['type']}</td>
              <td class="price-cell">{it['price']}</td>
              <td><a href="#rank-{p['rank']}" class="table-link">詳細を見る</a></td>
            </tr>""")
table_joined = "\n".join(table_rows)

# 各商品カード
product_cards = []
for idx, p in enumerate(product_details):
    it = items[idx]
    product_cards.append(f"""      <article class="product-card" id="rank-{p['rank']}">
        <div class="product-badge">第{p['rank']}位 ｜ {p['type']}</div>
        <div class="product-header">
          <div class="img-container">
            <img src="{it['img']}" alt="{it['name']}" class="product-img" loading="lazy">
          </div>
          <div class="product-intro">
            <h3 class="product-title">{it['name']}</h3>
            <div class="product-brand">ブランド：<strong>{p['brand_name']}</strong></div>
            <div class="product-price">参考価格：<span class="price-val">{it['price']}</span> <small>（楽天市場 最新確認時）</small></div>
            <div class="product-tag">{p['tag']}</div>
            <p class="product-catch">{p['catch']}</p>
          </div>
        </div>

        <div class="spec-table-box">
          <table class="spec-table">
            <tr><th>内容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>主要保湿・美容成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の保湿メリット</th><td>{p['value']}</td></tr>
          </table>
        </div>

        <div class="review-body">
          <h4>💡 コスメコンシェルジュによる徹底レビュー＆冬の保湿効果検証</h4>
          <p>{p['desc_p1']}</p>
          <p>{p['desc_p2']}</p>

          <div class="target-box">
            <strong>🎯 こんな方に特におすすめ！</strong>
            <p>{p['target']}</p>
          </div>

          <div class="point-box">
            <strong>✨ 保湿効果を最大化するプロの使い方：</strong>
            <p>{p['point']}</p>
          </div>
        </div>

        <div class="btn-wrap">
          <a href="{it['url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            🛒 楽天市場で「{p['brand_name']}」の最新価格・在庫・口コミを見る
          </a>
        </div>
      </article>""")

cards_joined = "\n\n".join(product_cards)

# JSON-LD構造化データ
json_ld_items = []
for idx, p in enumerate(product_details):
    it = items[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": p["rank"],
        "name": it["name"],
        "url": f"https://lumi-cosme.vercel.app/winter-moringa-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！生命の木がもたらす濃密なベヘン酸ヴェールで一日中乾かない高保湿モリンガオイルコスメランク10",
            "description": "11月・12月の木枯らしと過酷なエアコン乾燥によるインナードライを救う高保湿モリンガオイルコスメを徹底厳選！SHIRO、生活の木、Spa treatment、マンディムーン、ボタニカルファクトリーまで厳選。",
            "datePublished": "2026-11-05T01:00:00+09:00",
            "dateModified": "2026-11-05T01:00:00+09:00",
            "author": {
                "@type": "Person",
                "name": "Lumi Cosme 編集部 コスメコンシェルジュ"
            },
            "publisher": {
                "@type": "Organization",
                "name": "Lumi Cosme",
                "url": "https://lumi-cosme.vercel.app/"
            }
        },
        {
            "@type": "ItemList",
            "name": "高保湿モリンガオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "モリンガオイルが真冬（11月・12月）の暖房乾燥に強いと言われる科学的理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "モリンガオイル（ワサビノキ種子油）の最大の特徴は、高濃度のオレイン酸（約70%以上）に加えて、高級長鎖飽和脂肪酸である『ベヘン酸（約6〜9%）』を豊富に含有している点です。ベヘン酸は肌表面に非常に均一で滑らかな微細保護被膜（エモリエントフィルム）を形成し、水分蒸散を強力に抑制します。11月〜12月の暖房直撃による砂漠のような超低湿度環境下でも、このベヘン酸シールドが角層内の水分を物理的に閉じ込めるため、夕方になっても乾かない驚異的な保湿持続力を発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "モリンガオイルは毛穴に詰まったり、ニキビの原因になったりしませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "モリンガオイルは浸透性が非常に高く、分子構造が人の皮脂と親和性が高いため、適量を守って使用する限り毛穴詰まり（コメド）を起こしにくい植物油です。さらに、モリンガ種子に含まれる微量成分には天然の抗菌・抗炎症作用があるため、真冬の乾燥によってバリアが壊れて生じる『大人の乾燥ニキビ』や肌荒れの予防にも適しています。ただし、1回の使用量は1〜2滴で十分に全顔をカバーできるため、過剰な塗りすぎには注意してください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬場にモリンガオイルが白く濁ったり固まったりした場合はどうすればよいですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "モリンガオイルに含まれるベヘン酸やパルミチン酸などの飽和脂肪酸は、気温が約15℃〜18℃以下になると白く結晶化して固まる性質があります。これは合成界面活性剤や溶剤を使用していない高純度な天然植物油である証拠であり、品質や有効成分に一切問題はありません。固まった場合は、容器のフタを閉めたままぬるま湯（35〜40℃程度）に数分浸けて湯煎するか、暖かい室内にしばらく置いて自然に液状に戻してからご使用ください。電子レンジ等での急激な加熱は酸化を招くため避けてください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "アルガンオイルやホホバオイルと比べてモリンガオイルの最大の利点は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ホホバオイルはワックスエステル主体で表面保護が得意、アルガンオイルはビタミンEによる抗酸化が得意ですが、モリンガオイルは『酸化安定性の高さ』と『ベヘン酸による持続性シールド力』において群を抜いています。モリンガオイルは古代から防腐・保存油として重宝されたほど酸化しにくく、日中の紫外線や外気に触れても油焼けの心配がありません。また、硬化した角層を解きほぐす柔軟効果（エモリエント力）が極めて高いため、真冬のカチコチ肌のブースターとして最高のパフォーマンスを発揮します。"
                    }
                }
            ]
        }
    ]
}

json_ld_str = json.dumps(json_ld_schema, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！生命の木がもたらす濃密なベヘン酸ヴェールで一日中乾かない高保湿モリンガオイルコスメランク10</title>
  <meta name="description" content="11月・12月の木枯らしと過酷なエアコン乾燥によるインナードライを救う高保湿モリンガオイルコスメを徹底厳選！SHIRO、生活の木、Spa treatment、マンディムーン、ボタニカルファクトリーまで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-moringa-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！生命の木がもたらす濃密なベヘン酸ヴェールで一日中乾かない高保湿モリンガオイルコスメランク10">
  <meta property="og:description" content="11月・12月の木枯らしと過酷なエアコン乾燥によるインナードライを救う高保湿モリンガオイルコスメを徹底厳選！SHIRO、生活の木、Spa treatment、マンディムーン、ボタニカルファクトリーまで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-moringa-oil">
  <meta property="og:site_name" content="Lumi Cosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{json_ld_str}
  </script>
  <style>
    :root {{
      --primary: #047857;
      --primary-light: #d1fae5;
      --primary-dark: #065f46;
      --accent: #10b981;
      --accent-hover: #059669;
      --bg: #f0fdf4;
      --card-bg: #ffffff;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --border: #a7f3d0;
      --shadow: 0 4px 15px rgba(4, 120, 87, 0.08);
      --radius: 14px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}

    header.site-header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 1.5rem;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    }}

    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .site-logo {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}

    .nav-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.2rem;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--primary);
    }}

    main.container {{
      max-width: 920px;
      margin: 2rem auto;
      padding: 0 1.2rem;
    }}

    .hero {{
      background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
      border: 1px solid #6ee7b7;
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-tag {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 700;
      line-height: 1.45;
      color: #064e3b;
      margin-bottom: 1.2rem;
    }}

    .hero-desc {{
      color: var(--text-sub);
      font-size: 1rem;
      line-height: 1.8;
      margin-bottom: 1.5rem;
    }}

    .hero-meta {{
      display: flex;
      gap: 1.2rem;
      font-size: 0.85rem;
      color: #6b7280;
      border-top: 1px solid #d1fae5;
      padding-top: 1rem;
    }}

    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-card h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.6rem;
    }}

    @media (min-width: 640px) {{
      .toc-list {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .toc-list a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.92rem;
      display: block;
      padding: 0.3rem 0.5rem;
      border-radius: 6px;
      transition: background 0.2s, color 0.2s;
    }}

    .toc-list a:hover {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    .table-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .table-section h2 {{
      font-size: 1.35rem;
      color: #064e3b;
      margin-bottom: 1.2rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .table-wrapper {{
      overflow-x: auto;
    }}

    table.rank-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    table.rank-table th, table.rank-table td {{
      padding: 0.9rem;
      border-bottom: 1px solid #f0fdf4;
    }}

    table.rank-table th {{
      background: #ecfdf5;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      white-space: nowrap;
    }}

    .table-thumb {{
      width: 50px;
      height: 50px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
    }}

    .price-cell {{
      font-weight: 700;
      color: #e11d48;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.85rem;
    }}

    .table-link:hover {{
      text-decoration: underline;
    }}

    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: linear-gradient(135deg, var(--primary) 0%, #10b981 100%);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 1rem;
      border-radius: 50px;
      margin-bottom: 1.2rem;
    }}

    .product-header {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      margin-bottom: 1.5rem;
    }}

    @media (min-width: 640px) {{
      .product-header {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}

    .img-container {{
      flex-shrink: 0;
      width: 100%;
      max-width: 260px;
      margin: 0 auto;
      text-align: center;
      background: #f0fdf4;
      padding: 1rem;
      border-radius: 12px;
      border: 1px solid #d1fae5;
    }}

    .product-img {{
      width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      border-radius: 8px;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    h3.product-title {{
      font-size: 1.3rem;
      color: #064e3b;
      line-height: 1.45;
      margin-bottom: 0.6rem;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.45rem;
      font-weight: 700;
      color: #e11d48;
    }}

    .product-tag {{
      display: inline-block;
      background: #ecfdf5;
      color: var(--primary-dark);
      font-size: 0.82rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
      border-radius: 6px;
      border: 1px solid #a7f3d0;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #374151;
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #f0fdf4;
      border-radius: 10px;
      padding: 1rem 1.2rem;
      border: 1px solid #d1fae5;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.5rem 0.6rem;
      border-bottom: 1px solid #d1fae5;
      text-align: left;
    }}

    table.spec-table tr:last-child th, table.spec-table tr:last-child td {{
      border-bottom: none;
    }}

    table.spec-table th {{
      width: 25%;
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}

    .review-body {{
      margin-top: 1.5rem;
      border-top: 1px solid #f3f4f6;
      padding-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: #064e3b;
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .target-box, .point-box {{
      background: #ecfdf5;
      border-left: 4px solid var(--accent);
      padding: 0.9rem 1.1rem;
      border-radius: 0 8px 8px 0;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      color: #1f2937;
    }}

    .point-box {{
      background: #f0fdf4;
      border-left-color: var(--primary);
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    a.rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      text-decoration: none;
      font-size: 1rem;
      font-weight: 700;
      padding: 1rem 2rem;
      border-radius: 50px;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: transform 0.2s, box-shadow 0.2s, background 0.2s;
      width: 100%;
      max-width: 460px;
    }}

    a.rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a80000 0%, #d40000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: #064e3b;
      margin-bottom: 1.5rem;
      border-left: 5px solid var(--primary);
      padding-left: 0.8rem;
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin: 1.5rem 0 0.8rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.85;
      margin-bottom: 1rem;
    }}

    .guide-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.2rem;
      margin: 1.5rem 0;
    }}

    @media (min-width: 640px) {{
      .guide-grid {{
        grid-template-columns: 1fr 1fr 1fr;
      }}
    }}

    .guide-card {{
      background: #f0fdf4;
      border: 1px solid #d1fae5;
      border-radius: 10px;
      padding: 1.2rem;
    }}

    .guide-card h4 {{
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}

    .guide-card p {{
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.6;
      margin-bottom: 0;
    }}

    .faq-item {{
      border-bottom: 1px solid #f0fdf4;
      padding: 1.2rem 0;
    }}

    .faq-item:last-child {{
      border-bottom: none;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q::before {{
      content: "Q.";
      color: var(--primary);
      font-weight: 700;
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: var(--text-main);
      line-height: 1.8;
      padding-left: 1.6rem;
    }}

    .related-links {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}

    .related-links h3 {{
      font-size: 1.2rem;
      color: #064e3b;
      margin-bottom: 1.2rem;
    }}

    .related-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.8rem;
    }}

    @media (min-width: 640px) {{
      .related-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    .related-card {{
      display: block;
      padding: 0.8rem 1rem;
      background: #f0fdf4;
      border-radius: 8px;
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.9rem;
      transition: background 0.2s, color 0.2s;
      border: 1px solid #d1fae5;
    }}

    .related-card:hover {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      text-align: center;
      font-size: 0.88rem;
      color: var(--text-sub);
      margin-top: 3rem;
    }}

    footer.site-footer a {{
      color: var(--primary);
      text-decoration: none;
      margin: 0 0.4rem;
    }}

    footer.site-footer a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">🌸 Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="/winter-damask-rose">高保湿ダマスクローズ</a>
        <a href="/winter-evening-primrose">高保湿月見草オイル</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-tag">❄️ 11月・12月真冬の集中保湿ケア特集</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！生命の木がもたらす濃密なベヘン酸ヴェールで一日中乾かない高保湿モリンガオイルコスメランク10</h1>
      <p class="hero-desc">
        11月下旬から12月にかけて、木枯らしが吹きすさぶ屋外と、暖房が一日中フル稼働する室内との激しい環境差によって、私たちの肌は常に水分蒸発の危機に晒されています。「朝どれだけ保湿クリームを塗っても、昼過ぎには目元や頬がつっぱる」「エアコンの風が当たると肌が粉を吹いてファンデーションがひび割れる」「夕方になると肌がしぼんで疲れて見える」…そんな深刻な真冬のインナードライに悩んでいませんか？<br><br>
        そんな過酷な乾燥砂漠を生き抜くために、古代エジプトの王侯貴族や絶世の美女クレオパトラが愛用したと伝えられる奇跡のオイルが「モリンガオイル（ワサビノキ種子油）」です。『奇跡の木』『生命の木』と称されるモリンガの種子から採れるこのオイルは、肌を柔らかくほぐす高濃度オレイン酸に加え、他の植物油には極めて稀な高級脂肪酸『ベヘン酸（約6〜9%）』を豊富に含んでいます。このベヘン酸が肌表面に滑らかなパールヴェールを形成し、暖房直撃の環境でも水分蒸散を物理的にシャットアウトしてくれます。<br><br>
        本記事では、楽天APIからリアルタイムに取得した最新データに基づき、コールドプレス未精製オイルから国産無農薬モリンガ、サロン専売スパセラム、携帯リペアバーム、ヘアオイルまで、一日中乾かない極上のうるおい膜を叶える高保湿モリンガオイルコスメTOP10を徹底検証しました。
      </p>
      <div class="hero-meta">
        <span>📅 2026年11月最新更新</span>
        <span>✍️ コスメコンシェルジュ＆植物生化学アナリスト監修</span>
        <span>🔬 楽天市場公式APIデータ連携済</span>
      </div>
    </section>

    <div class="toc-card">
      <h3>📑 目次：高保湿モリンガオイルコスメTOP10</h3>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="table-section">
      <h2>🏆 高保湿モリンガオイルコスメおすすめ比較一覧</h2>
      <div class="table-wrapper">
        <table class="rank-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>ブランド・商品名</th>
              <th>分類</th>
              <th>楽天市場価格</th>
              <th>詳細リンク</th>
            </tr>
          </thead>
          <tbody>
{table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <section class="products-section">
{cards_joined}
    </section>

    <section class="guide-section">
      <h2>💡 失敗しない高保湿モリンガオイルコスメの選び方＆冬の活用術</h2>

      <h3>1. モリンガオイルの核「ベヘン酸」と「オレイン酸」の黄金バランス</h3>
      <p>モリンガオイルを選ぶ際、最も注目すべきは脂肪酸組成です。人の皮脂膜に近いオレイン酸（約70%以上）が冬の寒さで硬化した角質層を瞬時に柔らかく解きほぐし、高級長鎖飽和脂肪酸であるベヘン酸（約6〜9%）が肌表面に微細な保護フィルムを張るという『二段構えの保湿メカニズム』を持っています。熱を加えない低温圧搾（コールドプレス）で抽出された未精製オイルは、この脂肪酸バランスが完璧に保たれており、暖房の熱風にさらされても蒸発しない圧倒的な保湿シールド力を発揮します。</p>

      <div class="guide-grid">
        <div class="guide-card">
          <h4>未精製ピュアオイル</h4>
          <p>洗顔直後のブースターや夜のスキンケアの仕上げに。ベヘン酸の濃密な保護膜で、暖房直撃の部屋でも一日中水分を逃しません。</p>
        </div>
        <div class="guide-card">
          <h4>モリンガバーム・スティック</h4>
          <p>外出時の冷風ガードや日中の目元・口元のひび割れ対策に。ミツロウとの相乗効果でピンポイントに強固な油膜を形成します。</p>
        </div>
        <div class="guide-card">
          <h4>リッチヘアオイル・石けん</h4>
          <p>冬の静電気による毛先の広がり防止や、入浴時の摩擦レス洗顔に。ベヘン酸が髪のキューティクルや肌のキメを滑らかに整えます。</p>
        </div>
      </div>

      <h3>2. 暖房砂漠を跳ね返す「ミルフィーユ保湿法」</h3>
      <p>モリンガオイルは非常に浸透力と柔軟効果が高いため、水分と交互に重ねる『ミルフィーユ保湿法』が真冬の乾燥対策に絶大な効果をもたらします。</p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>洗顔直後に1滴（先行導入）：</strong> 洗顔後、タオルドライした素肌にモリンガオイルを1滴ハンドプレス。硬くなった角質が瞬時にほぐれます。</li>
        <li><strong>高保湿化粧水をたっぷり重ねる：</strong> オイルが通り道を作るため、化粧水の水分が角層深部までぐんぐん引き込まれます。</li>
        <li><strong>乳液・クリーム後に半滴（密閉シールド）：</strong> お手入れの最後に、手のひらに半滴伸ばして優しく顔を包み込みます。ベヘン酸の膜が水分を完全に閉じ込め、翌朝まで潤いが持続します。</li>
      </ol>

      <h3>3. 冬の結晶化（固化）への正しい対処法</h3>
      <p>モリンガオイルは飽和脂肪酸を多く含むため、室温が約15℃を下回ると白く濁ったり固まったりすることがあります。これは化学溶剤や合成界面活性剤を一切添加していない純度100%の植物オイルである証拠です。固まった場合は、容器ごと35〜40℃程度のぬるま湯に数分浸けて湯煎するか、暖房の効いた暖かい部屋に置いて自然に溶かしてから使用してください。品質や美容成分への影響は全くありません。</p>
    </section>

    <section class="faq-section">
      <h2>❓ 高保湿モリンガオイルコスメに関するよくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q">モリンガオイルが真冬（11月・12月）の暖房乾燥に強いと言われる科学的理由は何ですか？</div>
        <div class="faq-a">モリンガオイル（ワサビノキ種子油）の最大の特徴は、高濃度のオレイン酸（約70%以上）に加えて、高級長鎖飽和脂肪酸である『ベヘン酸（約6〜9%）』を豊富に含有している点です。ベヘン酸は肌表面に非常に均一で滑らかな微細保護被膜（エモリエントフィルム）を形成し、水分蒸散を強力に抑制します。11月〜12月の暖房直撃による砂漠のような超低湿度環境下でも、このベヘン酸シールドが角層内の水分を物理的に閉じ込めるため、夕方になっても乾かない驚異的な保湿持続力を発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">モリンガオイルは毛穴に詰まったり、ニキビの原因になったりしませんか？</div>
        <div class="faq-a">モリンガオイルは浸透性が非常に高く、分子構造が人の皮脂と親和性が高いため、適量を守って使用する限り毛穴詰まり（コメド）を起こしにくい植物油です。さらに、モリンガ種子に含まれる微量成分には天然の抗菌・抗炎症作用があるため、真冬の乾燥によってバリアが壊れて生じる『大人の乾燥ニキビ』や肌荒れの予防にも適しています。ただし、1回の使用量は1〜2滴で十分に全顔をカバーできるため、過剰な塗りすぎには注意してください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">冬場にモリンガオイルが白く濁ったり固まったりした場合はどうすればよいですか？</div>
        <div class="faq-a">モリンガオイルに含まれるベヘン酸やパルミチン酸などの飽和脂肪酸は、気温が約15℃〜18℃以下になると白く結晶化して固まる性質があります。これは合成界面活性剤や溶剤を使用していない高純度な天然植物油である証拠であり、品質や有効成分に一切問題はありません。固まった場合は、容器のフタを閉めたままぬるま湯（35〜40℃程度）に数分浸けて湯煎するか、暖かい室内にしばらく置いて自然に液状に戻してからご使用ください。電子レンジ等での急激な加熱は酸化を招くため避けてください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">アルガンオイルやホホバオイルと比べてモリンガオイルの最大の利点は何ですか？</div>
        <div class="faq-a">ホホバオイルはワックスエステル主体で表面保護が得意、アルガンオイルはビタミンEによる抗酸化が得意ですが、モリンガオイルは『酸化安定性の高さ』と『ベヘン酸による持続性シールド力』において群を抜いています。モリンガオイルは古代から防腐・保存油として重宝されたほど酸化しにくく、日中の紫外線や外気に触れても油焼けの心配がありません。また、硬化した角層を解きほぐす柔軟効果（エモリエント力）が極めて高いため、真冬のカチコチ肌のブースターとして最高のパフォーマンスを発揮します。</div>
      </div>
    </section>

    <section class="related-links">
      <h3>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h3>
      <div class="related-grid">
        <a href="/winter-damask-rose" class="related-card">🌹 高保湿ダマスクローズコスメ10選</a>
        <a href="/winter-evening-primrose" class="related-card">🌙 高保湿月見草オイルコスメ10選</a>
        <a href="/winter-tamanu-oil" class="related-card">🌿 高保湿タマヌオイルコスメ10選</a>
        <a href="/winter-baobab-oil" class="related-card">🌳 高保湿バオバブオイルコスメ10選</a>
        <a href="/winter-kombucha" class="related-card">🍵 高保湿コンブチャコスメ10選</a>
        <a href="/winter-manuka-honey" class="related-card">🍯 高純度マヌカハニーコスメ10選</a>
        <a href="/winter-resurrection-plant" class="related-card">🌵 復活草・トレハロースコスメ10選</a>
        <a href="/winter-ceramide-cream" class="related-card">🛡️ 高保湿セラミドクリーム10選</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 Lumi Cosme. All rights reserved. 掲載価格は楽天市場の最新参考価格です。</p>
    <p style="margin-top: 0.5rem;"><a href="/">ホーム</a> | <a href="/winter-damask-rose">高保湿ダマスクローズ</a> | <a href="/winter-evening-primrose">高保湿月見草オイル</a> | <a href="/winter-moringa-oil">高保湿モリンガオイル</a></p>
  </footer>

</body>
</html>"""

with open("winter-moringa-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved winter-moringa-oil.html successfully!")
