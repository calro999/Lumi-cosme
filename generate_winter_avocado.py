import json
import re

with open("fetched_final_30_resurrection_beta_avocado.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_avocado"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🥑 世界的ベストセラー！指先で温めるとみずみずしく崩れる奇跡のアイバーム",
        "catch": "森のバター・アボカドオイルとシアバターを高濃度配合。冬の木枯らしとエアコンで乾燥小ジワ・ちりめんジワが刻まれやすい目元をふっくら濃厚に保護する名作",
        "brand_name": "Kiehl's (キールズ)",
        "capacity": "14g / ジャータイプ",
        "type": "高保湿集中アボカドアイクリーム",
        "features": "アボカドオイル（アボカド油）、シア脂、PCA-Na、β-カロテン",
        "value": "独自のウォーター・イン・オイル処方。固めのクリームを指先で練ると水滴があふれ出し、目元の極薄皮膚に摩擦を一切かけずに密着保護膜を形成",
        "desc_p1": "冬になると真っ先に乾燥サインが現れるのが、顔の中で最も皮膚が薄く（約0.02mm）皮脂腺がほとんど存在しない『目元』です。夕方に鏡を見ると目の下に無数の細かいちりめんジワが走り、アイメイクがヨレて老け見えしてしまう――そんな真冬の目元危機を救う世界的ベストセラーが、キールズの『アイトリートメント AV』です。",
        "desc_p2": "淡いアボカドグリーンのクリームは、容器に入っているときはこっくりと固め。しかし薬指の腹で数回すり合わせると、体温で瞬時にテクスチャーが変化し、みずみずしい水分がじゅわっとあふれ出します。この水分と油分の黄金比が、デリケートな目元に引っかかりなくスルスルと馴染み、表面に極薄のクッション保護膜を形成。夜塗れば翌朝まで目元がふっくらと持ち上がり、メイク前に仕込めばコンシーラーの乾燥割れを完璧にブロックします。",
        "target": "真冬になると目元の乾燥小ジワやちりめんジワが目立つ方、アイクリームの重さでメイクが崩れるのが嫌な方、摩擦レスで目元を優しく保湿したい方",
        "point": "米粒大を薬指の腹に取り、左右の指先を合わせて数回擦り合わせます。クリームがみずみずしいリキッド状に変化したのを確認してから、目の下・目尻・まぶたへポンポンと優しくタップするように馴染ませてください。こすらずにタッピングするのがコツです。"
    },
    {
        "rank": 2,
        "tag": "🥛 森のバターが角質をトロトロに解きほぐす！化粧水の前に使う感動の先行乳液",
        "catch": "アボカドオイルをはじめとする植物オイルとハーブエキスを凝縮。冬の寒冷で硬くこわばった角質層を柔らかくほぐし、毛穴の目立たないふっくら柔肌へ導く",
        "brand_name": "DECORTÉ (コスメデコルテ)",
        "capacity": "150ml / ポンプボトル",
        "type": "角質柔軟・高保湿先行乳液（エマルジョン）",
        "features": "アボカドオイル、セージ油、オリーブ果実油、ラベンダー花水、ローズヒップ油",
        "value": "『乳液先行』スキンケアのパイオニア。冬の寒さでゴワつき化粧水を弾いてしまう肌に、油分と水分のミルフィーユ構造を先に届けて浸透ルートを再起動",
        "desc_p1": "11月から12月にかけて気温が下がると、皮脂が固化して角質が硬くなり、どんなに高級な化粧水をパッティングしても表面を滑り落ちて浸透しない「角質硬化」が起きます。そんな冬のゴワゴワ肌に革命を起こすのが、コスメデコルテの伝説的先行乳液『プリム ラテ ハーバル ミルク』です。",
        "desc_p2": "洗顔後すぐ、化粧水の前にコットンで馴染ませる設計。栄養の宝庫であるアボカドオイルが、角質細胞同士を繋ぐ細胞間脂質と素早くなじみ、まるでカチカチの土壌に恵みの雨が染み込むように肌をトロトロに柔らかく解きほぐします。その後に使う化粧水の吸い込みが何倍にも跳ね上がり、翌朝の肌は毛穴の凹凸が目立たないつるんとしたモチモチ肌に。清々しい天然ハーブの香りが、冬のスキンケアタイムを至福のリラクゼーションに変えてくれます。",
        "target": "冬になると肌がゴワついて化粧水が浸透しにくい方、キメの乱れや毛穴の開きが気になる方、みずみずしく柔らかな肌触りを手に入れたい方",
        "point": "朝晩の洗顔直後、コットンに2プッシュを取り、顔の内側から外側へ螺旋を描くように優しく滑らせます。首筋やデコルテまで伸ばした後、手のひらで軽くハンドプレスして馴染ませ、その後に化粧水を重ねてください。"
    },
    {
        "rank": 3,
        "tag": "🥑 まるで本物のアボカドをすり潰した贅沢ペースト！冬の砂漠肌を救う集中マスク",
        "catch": "完熟アボカド果実エキスとアボカドオイルをそのまま練り上げたような濃厚ペースト。冬の極度な乾燥・ゴワつき・皮むけをわずか15分でリセットする洗い流すパック",
        "brand_name": "Kiehl's (キールズ)",
        "capacity": "100g / ジャータイプ",
        "type": "高濃度アボカド集中保湿フェイシャルマスク",
        "features": "アボカド果実エキス、アボカド油、月見草油、スクワラン",
        "value": "週に2〜3回のスペシャルケア。乾燥で疲弊した角層細胞に良質なオレイン酸とビタミンを一気にチャージし、もっちりと弾むような活力肌を蘇らせる",
        "desc_p1": "週末のご褒美や、寒風に一日中さらされて肌がカサカサに干からびた日の緊急レスキューとして絶大な人気を誇るのが、キールズの『スキン ハイドレーション マスク』です。フタを開けると、まるで完熟アボカドをフォークで潰したてのような、鮮やかな黄緑色のリッチなペーストが現れます。",
        "desc_p2": "手のひらですり潰すように温めてから肌に乗せると、クリーミーなアボカドペーストがピタッと密着。角質層にオレイン酸やビタミンE、必須脂肪酸がじわじわと染み渡り、寒さでこわばった肌を解きほぐします。15分後にぬるま湯で洗い流すと、肌表面が上質なベルベットのように滑らかで柔らかく変化。水滴を弾くほどのふっくらとしたツヤとハリが戻り、翌朝のメイクのノリが劇的に変わります。",
        "target": "週に数回じっくり自宅で本格エステのような集中保湿を行いたい方、冬の皮むけや粉吹きを即座にリセットしたい方、アボカドの栄養をダイレクトに浴びたい方",
        "point": "洗顔後の清潔な肌に使用します。マスカット粒大を取り、手のひらでペースト状になるまで軽く練ってから、目と口の周りを避けて肌が隠れる程度の厚さに均一に塗り広げます。15分置いた後、ぬるま湯で円を描くように優しくマッサージしながら洗い流してください。"
    },
    {
        "rank": 4,
        "tag": "🌿 低温圧搾100%オーガニック！ひび割れ・ガサガサを救う高純度未精製オイル",
        "catch": "有機栽培アボカドの果肉からコールドプレスで抽出した一番搾り。ビタミンA・D・Eと植物ステロールが真冬の肘・かかと・目元の乾燥割れを鉄壁ガード",
        "brand_name": "生活の木 (Tree of Life)",
        "capacity": "25ml / 遮光ドロッパー瓶",
        "type": "100%ピュア有機未精製アボカドオイル",
        "features": "有機アボカド油100%（未精製・コールドプレス製法）",
        "value": "深みのあるグリーンの色と濃厚なコクが本物の証。浸透力とエモリエント力に優れ、真冬の硬化した角質を柔らかく包み込んで水分を逃さない",
        "desc_p1": "アロマとオーガニックのパイオニアである生活の木が手がける『有機アボカドオイル』は、世界的な有機認証を取得した最高品質の未精製オイルです。精製工程で熱や化学物質を加えないコールドプレス製法のため、アボカド本来のビタミン群やクロロフィル、レシチンが壊れることなく丸ごと凝縮されています。",
        "desc_p2": "オリーブオイルよりもさらに濃厚で粘性があり、肌に乗せるとトロリとした密着感。角層への浸透速度が極めて速く、表面だけがテカテカ浮くのではなく、内側からしっとりと吸い付くような潤いが生まれます。真冬の顔のナイトオイルとしてはもちろん、乾燥でひび割れそうなかかとや肘、爪周りのささくれ、冬の木枯らしでパサつく毛先の集中補修まで、全身のガサガサ部位に万能に活躍します。",
        "target": "化学合成成分を一切含まないピュアオーガニックオイルを好む方、真冬の極度なひび割れ・粉吹きに悩む方、顔・体・髪まで全身マルチに使いたい方",
        "point": "夜のお手入れの最後に、手のひらに1〜2滴を落として体温で温めてから、乾燥が気になる部位に優しく押し込みます。化粧水前のブースターオイルとして使う場合は、洗顔直後の濡れた肌に半滴〜1滴を伸ばすと、その後の化粧水の吸い込みが格段に良くなります。"
    },
    {
        "rank": 5,
        "tag": "💄 冷風で皮むけした唇を瞬時にぷるぷるに！高保湿アボカドスティックバーム",
        "catch": "アボカドオイルとセラミドの濃厚デュアル処方。ポケットに入れていつでも手軽にひと塗り、真冬の木枯らしからデリケートな唇をとろけるように守り抜く",
        "brand_name": "SKINFOOD (スキンフード)",
        "capacity": "3.4g / スティック繰り出しタイプ",
        "type": "高保湿リペアリップバーム",
        "features": "アボカドオイル、セラミドNP、シア脂、ミツロウ、マカデミア種子油",
        "value": "体温でスルスルととろける高密着処方。冬の乾燥で縦ジワが目立ち、皮がめくれてリップメイクが乗らない唇に即座に濃密な油分クッションを形成",
        "desc_p1": "11月から12月にかけて、真っ先に冷風のダメージを受けて皮がめくれたり切れて血がにじんだりするのが「唇」です。マスクの摩擦や外気の乾燥でボロボロになった唇を優しくケアしてくれるのが、フードコスメのSKINFOOD『アボカド スティック リップバーム』です。",
        "desc_p2": "唇に乗せると体温でじんわりとろけて、まるでバターを薄く塗ったような滑らかな潤いヴェールが唇を包み込みます。アボカドオイルのオレイン酸とセラミドNPが角層のひび割れを埋め、縦ジワをふっくらと目立たなくカバー。ベタつきすぎず適度な密着感があるため、口紅やティントの下地として仕込むのにも最適で、一日中乾かないぷるんとしたリップを維持できます。",
        "target": "冬になると唇が乾燥して皮がめくれやすい方、口紅を塗ると縦ジワが目立ってしまう方、ポケットに入れて手軽に持ち運べるリップを探している方",
        "point": "乾燥を感じたときにいつでも唇に滑らせるように塗布します。夜寝る前には、唇の輪郭からはみ出るくらいオーバーに2〜3往復塗り重ねてリップパックとして使うと、翌朝の唇がふっくらと柔らかく生まれ変わります。"
    },
    {
        "rank": 6,
        "tag": "🍯 ブラウンシュガー×アボカドオイル！冬の唇の古い角質をつるんとオフするスクラブ",
        "catch": "微細な黒糖スクラブが唇の皮むけ・ガサガサを優しくオフしながら、アボカドオイルの濃厚な油分が同時に密着保湿。赤ちゃんのようなやわらかリップへ",
        "brand_name": "SKINFOOD (スキンフード)",
        "capacity": "14g / チューブタイプ",
        "type": "高保湿リップスクラブ＆モイスチャーパック",
        "features": "アボカドオイル、スクロース（黒糖シュガー）、ホホバ種子油、シア脂",
        "value": "角質ケアと高保湿エモリエントが1ステップ。冬の頑固な皮むけを無理に剥がさず、優しく溶かしながら濃厚な油分膜で包み込む",
        "desc_p1": "冬の乾燥した唇に無理やりリップクリームを重ねても、表面のめくれた皮が邪魔をして綺麗に仕上がりません。SKINFOODの『アボカド＆シュガー リップスクラブ』は、天然のブラウンシュガー粒子が古い角質を摩擦レスに優しくほぐしながら、アボカドオイルが同時に濃密な油分を補給する画期的なリップケアです。",
        "desc_p2": "唇に乗せてくるくると円を描くようにマッサージすると、砂糖の粒が体温と水分でじんわり溶けていき、ガサガサしていた唇の表面がつるんと滑らかに。ティッシュオフした後は、アボカドオイルの上質な油膜が唇に残るため、スクラブ後とは思えないほどしっとりモチモチの仕上がりに感動します。冬のマットリップや濃色リップを綺麗に発色させたい時の前夜ケアに必須のアイテムです。",
        "target": "唇の皮がめくれて口紅がムラになってしまう方、痛くない優しいリップスクラブを探している方、週1〜2回のスペシャルリップケアを取り入れたい方",
        "point": "適量を指先に取り、唇の上で優しく円を描くようにくるくると1分ほどマッサージします。砂糖の粒が溶けてきたら、濡らしたコットンで優しく拭き取るかぬるま湯で洗い流してください。その後リップバームを塗ると完璧です。"
    },
    {
        "rank": 7,
        "tag": "💧 高純度精製でにおいゼロ！敏感肌の全身を包み込む大容量エモリエントオイル",
        "catch": "アボカドオイル特有の独特な青臭さや色を丁寧な精製工程でカット。無香・サラリとした感触で、真冬の粉吹き肌・ボディ・ヘアケアに惜しみなく使える100ml",
        "brand_name": "自然化粧品本舗 (&SH)",
        "capacity": "100ml (50ml×2本) / ボトル",
        "type": "100%天然高純度精製アボカドオイル",
        "features": "精製アボカド油100%（脱色・脱臭精製処方）",
        "value": "未精製オイル特有の香りが苦手な方や、赤ちゃんの肌にも使える極めてマイルドな低刺激性。酸化安定性に優れ、冬の全身保湿を圧倒的コスパで実現",
        "desc_p1": "「アボカドオイルの抜群の保湿力は魅力的だけれど、特有の緑色や青臭い香りが少し気になる」という方に最適なのが、自然化粧品本舗の『精製アボカドオイル 100%』です。丁寧な精製処理によって不純物と香りを徹底的に取り除いており、ほぼ無臭で淡いクリアイエローに仕上げられています。",
        "desc_p2": "アボカドオイル本来の豊富なオレイン酸（約60〜70%）とビタミンEはそのままキープされているため、肌を柔らかく整えるエモリエント効果は一級品。テクスチャーも未精製に比べてサラリと軽やかで、入浴後の濡れた肌に伸ばすと瞬時に角層へと浸透します。50mlの小分けボトル2本セットで酸化を防ぎながら新鮮に使い切れ、顔の保湿はもちろん、真冬のスネや背中の粉吹き防止ボディオイルとしても最高峰の活躍を見せます。",
        "target": "オイル独特の香りが苦手な方、冬のボディの粉吹きやかゆみにたっぷり全身オイルを使いたい方、高品質な精製キャリアオイルを探している方",
        "point": "お風呂から上がる直前、タオルで拭く前の濡れた肌に適量を全身に伸ばします。その後にタオルで軽く水分を押さえるように拭き取ると、油分が水分を抱え込み、ボディクリーム要らずのモチモチ肌が一日中持続します。"
    },
    {
        "rank": 8,
        "tag": "🌿 南仏シアバター×濃厚アボカド！冬の木枯らしに立ち向かうスティックリップ",
        "catch": "ロクシタンを代表するオーガニックシアバターに、エモリエント効果の高いアボカドオイルをブレンド。真冬の過酷な乾燥環境でも潤いが長時間続くリッチな保湿力",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "4.5g / スティックタイプ",
        "type": "シア×アボカド高保湿リップバーム",
        "features": "シア脂（シアバター）、アボカド油、ヒマワリ種子油、ミツロウ、ビタミンE",
        "value": "シアバターの保護膜とアボカドオイルの柔軟効果が融合。硬くなりがちな冬のスティックバームでありながら、唇の上でスルスルと心地よく滑らかに密着",
        "desc_p1": "世界中で愛されるボディケアの王道ロクシタンが誇るロングセラー『シアリッチ リップバーム』。西アフリカ産の高品質オーガニックシアバターに、角質柔軟効果に優れたアボカドオイルを掛け合わせた、真冬の木枯らしに打ち勝つ高保湿リップトリートメントです。",
        "desc_p2": "シアバター特有のこっくりとした保護膜が、冷たい風や室内のエアコンからデリケートな唇を物理的にシールド。同時にアボカドオイルが角層の奥まで浸透して乾燥で硬くなった唇を柔らかく解きほぐします。無香料に近い自然な使い心地で、ベタつきやテカリが目立たないマットな質感に整うため、男性の冬のリップケアやビジネスシーンでの使用にも絶大な人気を誇ります。",
        "target": "テカテカ光るリップが苦手で自然にしっとり整えたい方、シアバターとアボカドの植物パワーを実感したい方、上質なギフトや自分へのご褒美にしたい方",
        "point": "繰り出しすぎず2〜3mm程度を出して、唇の縦ジワに沿って縦方向に優しく塗布します。横に引っ張るのではなく縦に塗ることで、シワの奥まで均一に成分が行き渡り、保湿の持ちが格段にアップします。"
    },
    {
        "rank": 9,
        "tag": "🧖‍♀️ 浸透アボカドオイル×ナノヒアルロン酸！赤ちゃんの肌のような超ふっくら美肌へ",
        "catch": "マンダム独自の超やわらか密着シートに、微細化された浸透アボカドオイルを配合。真冬の乾燥で開いた毛穴やキメの乱れを包み込み、指を弾く柔肌へ整える集中シートマスク",
        "brand_name": "Barrier Repair (マンダム バリアリペア)",
        "capacity": "5枚入り (各27mlエッセンス) / 個包装",
        "type": "超ふっくら角質柔軟シートマスク",
        "features": "浸透型アボカドオイル、ナノヒアルロン酸、ベビーウォーター脂質、スクワラン",
        "value": "無香料・無着色・防腐剤フリー・アルコールフリーの低刺激設計。立体裁断のふんわりシートが真冬の疲れた肌に優しくフィットし、角層をトロトロに満たす",
        "desc_p1": "ドラッグストアで手に入る実力派プチプラシートマスクとして不動の地位を築いているマンダムのバリアリペアシリーズ。その中でも『なめらか超ふっくら』は、微細カプセル化された浸透アボカドオイルを贅沢に配合した、冬の乾燥毛穴・キメ乱れ対策の決定版です。",
        "desc_p2": "綿の種子の周りのうぶ毛から作られた超極細繊維シートは、驚くほど柔らかく、肌に吸い付くように隙間なくフィット。乳液状の濃厚エッセンスが27mlも含まれており、マスクをつけている間中、アボカドオイルが乾いた角質層をじんわりと解きほぐします。はがした後はベタつかず、毛穴の影が消えて内側から発光するような、まさに「赤ちゃんの素肌」のようなふっくら感を体感できます。",
        "target": "プチプラで高機能な冬の集中保湿マスクを探している方、乾燥によって毛穴が目立ってしまう方、敏感肌でも安心して使える低刺激シートを好む方",
        "point": "洗顔後、化粧水の後にシートを顔全体に広げて密着させます。10分ほど置いたらはがし、肌に残った乳液状のエッセンスを手のひらでハンドプレスして馴染ませてください。首や手足にも余った液を伸ばすと全身潤います。"
    },
    {
        "rank": 10,
        "tag": "🌿 南仏プロヴァンス発！完全無添加コールドプレスの極上オーガニックオイル",
        "catch": "有機認証エコサート取得の100%天然アボカド果実オイル。ビタミン・ミネラルがそのまま残る濃厚な深緑色のエモリエントが、冬のガサガサ角質をトロトロに包み込む",
        "brand_name": "TERRA D'OC",
        "capacity": "100ml / ポンプボトル",
        "type": "100%オーガニック未精製アボカドオイル",
        "features": "オーガニック未精製アボカド油100%（エコサート認証・コールドプレス）",
        "value": "遮光ボトル入り・便利なポンプ式。熱を一切加えない低温圧搾により、果実の栄養素を完全保持。冬の深刻な粉吹き・肌の硬化を根本からケアする極上オイル",
        "desc_p1": "フランス・プロヴァンス発のオーガニックコスメブランドTERRA D'OCが届ける『オーガニック アボカドオイル』。厳選されたオーガニックアボカドを伝統的なコールドプレス製法で丁寧に搾油した、本物の果実のエネルギーが詰まった深緑色のピュアオイルです。",
        "desc_p2": "濃厚でリッチなテクスチャーでありながら、肌に乗せると皮脂膜と一体化するように素早く角層へ浸透。不飽和脂肪酸のオレイン酸とパルミトレイン酸が、真冬の寒さでゴワゴワに硬化した角質層をトロトロに柔らかく整え、水分蒸発を物理的にシャットアウトします。便利なプッシュポンプ式のため、片手でサッと手にとれて液垂れせず、毎晩のナイトケアやバスタイム後のボディケアをスマートに格上げしてくれます。",
        "target": "フランス産の本物のオーガニック認証オイルを使いたい方、液垂れしない使いやすいポンプ容器を好む方、冬の深刻な乾燥と肌の硬直を解消したい方",
        "point": "夜のお手入れの最後に1プッシュを手に取り、手のひらで温めてから顔全体を包み込むように馴染ませます。特に乾燥が気になる目元や口元、首筋には指先で重ねづけしてください。バスオイルとして湯船に数滴垂らすのもおすすめです。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "アボカドコスメが真冬（11月〜12月）の乾燥肌に特に効果的とされる理由は？",
        "a": "アボカドは『森のバター』と称されるほど良質な脂肪酸を豊富に含み、その主成分である『オレイン酸』は人間の皮脂膜の構成成分と酷似しています。11月〜12月は寒冷により皮脂分泌が激減し、角質細胞同士を接着する脂質が固化（硬化）してゴワゴワになります。アボカドオイルはこの硬直した角質層を驚異的な親和性でトロトロに解きほぐす『エモリエント軟化力』を持っており、水分を閉じ込めながらふっくらとした柔軟性を取り戻してくれます。"
    },
    {
        "q": "ホホバオイルやアルガンオイルと、アボカドオイルの違いは何ですか？",
        "a": "ホホバオイルは角層表面を保護する『ワックスエステル』が主成分でサラリとしており、アルガンオイルは抗酸化ビタミンEが豊富な『ブースター』に向いています。これに対しアボカドオイルは、より粘性とコクが高く、肌を柔らかくほぐす『オレイン酸』『パルミトレイン酸』『植物ステロール』が群を抜いて濃厚です。そのため、真冬の深刻な粉吹き、カチカチに硬化した角質、目元の深い乾燥小ジワを強力に密閉・軟化させる力においてはアボカドオイルが最も優れています。"
    },
    {
        "q": "アボカドオイルはオイル特有のニキビや毛穴詰まりの原因になりませんか？",
        "a": "精製されたアボカドコスメや配合製品（コスメデコルテのプリムラテ、キールズのアイクリーム、バリアリペアのシートマスク等）は、毛穴を詰まらせないよう絶妙なバランスで処方化されているため心配ありません。ピュアオイルを使用する場合も、適量（顔全体で1〜2滴）を守り、化粧水でしっかり水分を与えた後の蓋として使用すれば、過剰な皮脂分泌を抑えて健やかな肌バランスに整えてくれます。極度の脂性肌・ニキビ肌の方は、目元や口元など乾燥しやすい部分に限定して使用するのがおすすめです。"
    },
    {
        "q": "未精製アボカドオイルと精製アボカドオイルは、どちらを選ぶべきですか？",
        "a": "ご自身の好みと肌状態に合わせて選べます。未精製オイル（生活の木、TERRA D'OC）は鮮やかな深緑色をしており、アボカド本来のビタミン群やクロロフィルなどの栄養が壊れずに残っているため、強力なエイジングケアや極度の乾燥ひび割れ対策に最適です。一方、精製オイル（自然化粧品本舗 &SH）は脱色・脱臭されているため無臭でサラリとしており、オイル特有の香りが苦手な方や、敏感肌・赤ちゃんの肌の全身保湿に適しています。"
    }
]

# HTML テーブル行生成
table_rows = []
for it in items:
    r = it["rank"]
    p_info = next((p for p in product_details if p["rank"] == r), None)
    type_name = p_info["type"] if p_info else "高保湿コスメ"
    brand = it["brand"]
    name = it["display_name"].split(" (")[0]
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    
    row = f"""
    <tr>
      <td class="rank-num rank-{r}">{r}位</td>
      <td class="product-thumb"><a href="{url}" target="_blank" rel="nofollow noopener"><img src="{img}" alt="{name}" loading="lazy" width="80" height="80"></a></td>
      <td class="product-name-cell">
        <span class="product-brand">{brand}</span>
        <a href="{url}" target="_blank" rel="nofollow noopener" class="table-prod-link">{name}</a>
      </td>
      <td><span class="type-badge">{type_name}</span></td>
      <td class="product-price">{price}</td>
      <td><a href="{url}" target="_blank" rel="nofollow noopener" class="table-btn">楽天で見る</a></td>
    </tr>
    """
    table_rows.append(row)

table_joined = "\n".join(table_rows)

# 商品カード生成
cards = []
for it in items:
    r = it["rank"]
    p = next((x for x in product_details if x["rank"] == r), product_details[0])
    price = f"¥{it['price']:,}"
    img = it["image"]
    url = it["url"]
    shop = it["shop_name"]
    rate = it["review_rate"]
    reviews = it["review_count"]
    
    card = f"""
    <article class="product-card" id="rank-{r}">
      <div class="card-header">
        <div class="rank-badge rank-{r}">第{r}位</div>
        <div class="card-titles">
          <span class="card-tag">{p['tag']}</span>
          <h3 class="card-name">{it['display_name']}</h3>
        </div>
      </div>
      
      <p class="card-catch"><strong>【注目ポイント】</strong> {p['catch']}</p>
      
      <div class="card-body">
        <div class="card-image-box">
          <a href="{url}" target="_blank" rel="nofollow noopener">
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="card-img">
          </a>
          <div class="card-price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">{price}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <div class="card-review-box">
            <span class="star-rating">★ {rate}</span>
            <span class="review-count">({reviews}件のレビュー)</span>
          </div>
          <a href="{url}" target="_blank" rel="nofollow noopener" class="card-aff-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目オイル・栄養成分</th><td>{p['features']}</td></tr>
            <tr><th>冬の角質柔軟・保護価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="card-desc">
            <h4 class="desc-heading">🔍 美容オイルアナリストによる徹底解説＆冬の使用感</h4>
            <p class="desc-p">{p['desc_p1']}</p>
            <p class="desc-p">{p['desc_p2']}</p>
            
            <div class="eval-box">
              <div class="eval-item">
                <span class="eval-title">🎯 こんな方に特におすすめ</span>
                <p class="eval-text">{p['target']}</p>
              </div>
              <div class="eval-item">
                <span class="eval-title">💡 効果を高める冬のベストな使い方</span>
                <p class="eval-text">{p['point']}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# FAQ HTML生成
faq_items = []
for f in faqs:
    item = f"""
    <div class="faq-card">
      <h3 class="faq-q"><span class="q-icon">Q</span> {f['q']}</h3>
      <div class="faq-a"><span class="a-icon">A</span> <p>{f['a']}</p></div>
    </div>
    """
    faq_items.append(item)

faq_joined = "\n".join(faq_items)

# JSON-LD 生成
schema_items = []
for it in items:
    schema_items.append({
        "@type": "ListItem",
        "position": it["rank"],
        "name": it["brand"] + " " + it["display_name"].split(" (")[0],
        "image": it["image"],
        "offers": {
            "@type": "Offer",
            "priceCurrency": "JPY",
            "price": str(it["price"]),
            "url": it["url"],
            "availability": "https://schema.org/InStock"
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！ガサガサ粉吹き肌をとろける柔軟膜で包み込む濃厚アボカドコスメランク10",
            "description": "森のバターと呼ばれるアボカドの良質なオレイン酸とビタミンE。11月〜12月の寒さでゴワゴワに硬化した角質を解きほぐす高保湿アボカドコスメ10選を徹底比較。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！ガサガサ粉吹き肌をとろける柔軟膜で包み込む濃厚アボカドコスメランク10",
            "description": "冬の粉吹き・ひび割れ・硬直角質をとろとろに解きほぐす森のバター。キールズやコスメデコルテなど名作アボカドコスメ10選を詳細レビュー。",
            "datePublished": "2026-11-04T16:00:00+09:00",
            "dateModified": "2026-11-04T16:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://calro999.github.io/cosme/winter-avocado.html"
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！ガサガサ粉吹き肌をとろける柔軟膜で包み込む濃厚アボカドコスメランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月〜12月の寒さでガサガサ・粉吹き・硬直した角質をトロトロに解きほぐす！森のバターと呼ばれるアボカドオイル・バターを贅沢配合した高保湿コスメおすすめ人気ランキング10選。キールズ、コスメデコルテ、生活の木など楽天市場のリアルタイム価格情報・成分解析付き。">
  <meta name="keywords" content="アボカド コスメ, アボカド アイクリーム, キールズ アボカド, コスメデコルテ プリムラテ, アボカドオイル 保湿, 冬 粉吹き肌 スキンケア, エモリエントオイル, 11月 コスメ, 12月 コスメ">
  <link rel="canonical" href="https://calro999.github.io/cosme/winter-avocado.html">
  <link rel="icon" href="favicon.jpg" type="image/jpeg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --primary-color: #4d7c0f;
      --primary-dark: #3f6212;
      --primary-light: #ecfccb;
      --accent-color: #ca8a04;
      --text-main: #1c1917;
      --text-sub: #44403c;
      --text-light: #78716c;
      --bg-page: #fefce8;
      --bg-card: #ffffff;
      --border-color: #e7e5e4;
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.05);
      --shadow-md: 0 4px 12px rgba(77, 124, 15, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(77, 124, 15, 0.15);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Noto Sans JP', sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      line-height: 1.8;
      padding-bottom: 4rem;
    }}

    .site-header {{
      background: linear-gradient(135deg, #365314 0%, #4d7c0f 50%, #65a30d 100%);
      color: #ffffff;
      padding: 2rem 1.5rem 2.5rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(77, 124, 15, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #ecfccb;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .header-badge {{
      display: inline-block;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(8px);
      padding: 0.4rem 1.2rem;
      border-radius: 9999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 0.8rem;
    }}
    .site-title {{
      font-size: clamp(1.4rem, 4vw, 2.2rem);
      font-weight: 800;
      line-height: 1.35;
      margin-bottom: 1rem;
      text-shadow: 0 2px 4px rgba(0,0,0,0.15);
      max-width: 900px;
      margin-left: auto;
      margin-right: auto;
    }}
    .site-subtitle {{
      font-size: 0.95rem;
      color: #f7fee7;
      max-width: 800px;
      margin: 0 auto;
    }}

    .main-container {{
      max-width: 1040px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .toc-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 0.6rem;
    }}
    .toc-list li a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: color 0.2s;
    }}
    .toc-list li a:hover {{ color: var(--primary-color); font-weight: 700; }}

    .content-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border-color);
    }}
    .section-title {{
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--primary-dark);
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.6rem;
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .section-p {{
      font-size: 1rem;
      color: var(--text-sub);
      margin-bottom: 1.25rem;
      text-align: justify;
    }}

    .compare-table-wrapper {{
      overflow-x: auto;
      margin: 1.5rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      background: #ffffff;
      font-size: 0.92rem;
      min-width: 650px;
    }}
    .compare-table th {{
      background: #f7fee7;
      color: var(--primary-dark);
      padding: 0.9rem 0.75rem;
      text-align: center;
      font-weight: 700;
      border-bottom: 2px solid var(--primary-color);
      white-space: nowrap;
    }}
    .compare-table td {{
      padding: 0.9rem 0.75rem;
      border-bottom: 1px solid var(--border-color);
      vertical-align: middle;
      text-align: center;
    }}
    .compare-table tr:hover {{ background-color: #fefce8; }}
    .rank-num {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.2rem;
    }}
    .rank-1 {{ color: #eab308; }}
    .rank-2 {{ color: #94a3b8; }}
    .rank-3 {{ color: #d97706; }}
    .product-thumb img {{
      border-radius: var(--radius-sm);
      object-fit: cover;
      box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }}
    .product-name-cell {{
      text-align: left !important;
      max-width: 280px;
    }}
    .product-brand {{
      display: block;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--primary-color);
      text-transform: uppercase;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      line-height: 1.4;
      display: inline-block;
      margin-top: 0.2rem;
    }}
    .table-prod-link:hover {{ color: var(--primary-color); text-decoration: underline; }}
    .type-badge {{
      display: inline-block;
      padding: 0.25rem 0.6rem;
      background: #f1f5f9;
      color: #475569;
      border-radius: 4px;
      font-size: 0.78rem;
      font-weight: 600;
      white-space: nowrap;
    }}
    .product-price {{
      font-family: 'Outfit', sans-serif;
      font-weight: 700;
      color: #e11d48;
      font-size: 1rem;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      padding: 0.45rem 0.9rem;
      background: var(--primary-color);
      color: #ffffff;
      text-decoration: none;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
      transition: background 0.2s;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      padding: 2.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow-sm);
      position: relative;
    }}
    .card-header {{
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1rem;
    }}
    .rank-badge {{
      font-family: 'Outfit', sans-serif;
      font-weight: 800;
      font-size: 1.1rem;
      color: #ffffff;
      background: var(--primary-color);
      padding: 0.4rem 1rem;
      border-radius: var(--radius-sm);
      flex-shrink: 0;
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #64748b, #475569); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #78350f); }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 0.2rem 0.75rem;
      border-radius: 9999px;
      margin-bottom: 0.4rem;
    }}
    .card-name {{
      font-size: 1.3rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.4;
    }}
    .card-catch {{
      background: #f8fafc;
      border-left: 4px solid var(--primary-color);
      padding: 0.9rem 1.2rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
      color: #334155;
    }}
    .card-body {{
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .card-body {{ grid-template-columns: 1fr; }}
      .card-image-box {{ max-width: 320px; margin: 0 auto; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .card-img {{
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      margin-bottom: 1rem;
      object-fit: cover;
      max-width: 100%;
      height: auto;
    }}
    .card-price-box {{
      background: #fff1f2;
      border-radius: var(--radius-sm);
      padding: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #9f1239; }}
    .price-val {{ font-family: 'Outfit', sans-serif; font-size: 1.4rem; font-weight: 800; color: #be123c; }}
    .price-tax {{ font-size: 0.75rem; color: #9f1239; }}
    .card-review-box {{
      margin-bottom: 1rem;
      font-size: 0.88rem;
    }}
    .star-rating {{ color: #f59e0b; font-weight: 700; margin-right: 0.4rem; }}
    .review-count {{ color: var(--text-light); }}
    .card-aff-btn {{
      display: block;
      background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 800;
      font-size: 0.95rem;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      box-shadow: 0 4px 10px rgba(225, 29, 72, 0.25);
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .card-aff-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(225, 29, 72, 0.35);
    }}

    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th {{
      width: 25%;
      padding: 0.65rem 0.8rem;
      background: #f8fafc;
      border: 1px solid var(--border-color);
      color: #475569;
      font-weight: 700;
      text-align: left;
    }}
    .spec-table td {{
      padding: 0.65rem 0.8rem;
      border: 1px solid var(--border-color);
      color: var(--text-main);
    }}
    .desc-heading {{
      font-size: 1.08rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .desc-p {{
      font-size: 0.96rem;
      color: var(--text-sub);
      margin-bottom: 1rem;
      line-height: 1.8;
      text-align: justify;
    }}
    .eval-box {{
      background: #f7fee7;
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-top: 1.25rem;
      border: 1px solid #d9f99d;
    }}
    .eval-item {{ margin-bottom: 0.8rem; }}
    .eval-item:last-child {{ margin-bottom: 0; }}
    .eval-title {{
      display: block;
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      margin-bottom: 0.25rem;
    }}
    .eval-text {{
      font-size: 0.92rem;
      color: #1c1917;
      line-height: 1.6;
    }}

    .faq-card {{
      background: #ffffff;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.4rem;
      margin-bottom: 1.25rem;
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      margin-bottom: 0.6rem;
    }}
    .q-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: var(--primary-color);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}
    .a-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 24px;
      height: 24px;
      background: #ca8a04;
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 800;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    .footer-internal-links {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      margin-top: 3rem;
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}
    .footer-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 0.75rem;
      margin-top: 1.25rem;
    }}
    .footer-link-item {{
      padding: 0.65rem 0.85rem;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 600;
      display: block;
      transition: all 0.2s;
    }}
    .footer-link-item:hover {{
      background: var(--primary-light);
      border-color: var(--primary-color);
      color: var(--primary-dark);
    }}

    .site-footer {{
      text-align: center;
      margin-top: 3rem;
      color: var(--text-light);
      font-size: 0.85rem;
    }}
  </style>

  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="index.html">🏠 冬コスメ総合TOPへ戻る</a>
    </div>
    <span class="header-badge">❄️ 11月〜12月・森のバターで角質をトロトロに解きほぐす ❄️</span>
    <h1 class="site-title">保湿力の強さで肌乾燥とさようなら！ガサガサ粉吹き肌をとろける柔軟膜で包み込む濃厚アボカドコスメランク10</h1>
    <p class="site-subtitle">
      寒さでカチカチに硬化した角質と頑固な粉吹き肌を救う！ギネス認定の世界一栄養豊富な果実「アボカド」の良質なオレイン酸＆ビタミンEを凝縮した高保湿コスメ10選を徹底比較！
    </p>
  </header>

  <main class="main-container">
    
    <!-- 目次 -->
    <nav class="toc-box" aria-label="記事の目次">
      <div class="toc-title">📑 目次・もくじ</div>
      <ul class="toc-list">
        <li><a href="#why-avocado">1. なぜ真冬の硬化・粉吹き肌には「アボカド」が最強なのか？</a></li>
        <li><a href="#how-to-choose">2. 失敗しない冬のアボカドコスメの選び方・3つのポイント</a></li>
        <li><a href="#comparison-table">3. 濃厚アボカドコスメ10選 スペック＆価格比較表</a></li>
        <li><a href="#ranking-section">4. 高保湿おすすめコスメランキング10選 詳細レビュー</a></li>
        <li><a href="#faq-section">5. 美容皮膚＆オイル視点で答えるQ&amp;A（よくある質問）</a></li>
        <li><a href="#conclusion">6. まとめ：粉吹き肌と決別するとろけるアボカド保湿ルーティン</a></li>
        <li><a href="#internal-links">7. 関連する冬の高保湿コスメ特集一覧</a></li>
      </ul>
    </nav>

    <!-- セクション1 科学的背景 -->
    <section class="content-section" id="why-avocado">
      <h2 class="section-title">🥑 1. なぜ真冬の硬化・粉吹き肌には「アボカド」が最強なのか？</h2>
      <p class="section-p">
        11月から12月にかけて、冬の寒さが一段と厳しさを増すと、私たちの皮膚生理には決定的な変化が生じます。それは<strong>「皮脂分泌量の劇的な低下」</strong>です。寒冷によって皮膚表面の温度が下がると、皮脂腺の活動が鈍化し、夏場に比べて皮脂の分泌量は半分以下にまで激減します。
      </p>
      <p class="section-p">
        皮脂という天然の保護シールドを失った肌は、角質層の細胞間脂質（セラミドや脂肪酸など）が冷え固まり、まるで乾いたクッキーのようにカチカチに硬直します。これが、<strong>「化粧水をいくらパッティングしても弾かれて入っていかない」「ファンデーションを塗るとウロコのように粉を吹いて剥がれる」「笑うと頬や口元が引きつって痛い」</strong>という真冬特有の角質硬化トラブルの元凶です。
      </p>
      <p class="section-p">
        この硬化した角質層をトロトロに解きほぐし、しっとりとした柔軟性を取り戻すための切り札こそが、<strong>『アボカド（森のバター）』</strong>の濃厚な油分です。
      </p>
      <p class="section-p">
        アボカドは「世界一栄養価の高い果実」としてギネス記録に認定されており、その果肉から得られるオイルには他の植物油にはない突出した美肌パワーが秘められています：
      </p>
      <ul style="padding-left: 1.5rem; margin-bottom: 1.25rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>人体の皮脂膜に極めて近い「オレイン酸（約65%）」：</strong> 人間の皮膚となじみが抜群に良く、寒さで硬化した角層細胞の隙間へと素早く滑り込み、硬い角質をトロトロに柔らかく解きほぐします（エモリエント軟化作用）。</li>
        <li><strong>若返りのビタミンA・D・Eと植物ステロール：</strong> 強い抗酸化作用で冬の冷えや乾燥による肌枯れを防ぎ、角層細胞の再生を力強くバックアップします。</li>
        <li><strong>水分蒸発を物理的に密閉遮断する「濃密シールド膜」：</strong> エアコンの乾いた温風が吹きつけるオフィスでも、内側の水分を逃さず、一日中モチモチのふっくら肌を保ちます。</li>
      </ul>
      <p class="section-p">
        水分を与えるだけでなく、それを抱え込んで硬い肌をほぐす「良質な油分」を補給することこそ、11月〜12月の砂漠肌を救う究極の解決策なのです。
      </p>
    </section>

    <!-- セクション2 選び方 -->
    <section class="content-section" id="how-to-choose">
      <h2 class="section-title">🔍 2. 失敗しない冬のアボカドコスメの選び方・3つのポイント</h2>
      <p class="section-p">
        アボカドコスメを選ぶ際は、ご自身の肌悩みや使用部位に合わせて以下の3つのポイントを意識しましょう。
      </p>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント①：パーツ別の専門処方（目元、先行乳液、唇、全身）を見極める</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          乾燥小ジワが深く刻まれる目元には『キールズのアボカドアイクリーム』、化粧水の浸透を高めたいゴワつき肌には『コスメデコルテの先行乳液プリムラテ』、冷風で皮むけした唇には『スキンフードやロクシタンのリップバーム』など、悩みに直結した専用アイテムを選ぶのが効果的です。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; margin-bottom: 1.25rem;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント②：「未精製（高栄養）」か「精製（無臭・低刺激）」かを好みに合わせて選ぶ</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          ピュアオイルを選ぶ際、アボカド本来のビタミンやクロロフィルを丸ごと享受したい方は深緑色のコールドプレス未精製オイル（生活の木、TERRA D'OC）がおすすめ。一方、独特の青臭さが苦手な方や敏感肌・ボディにたっぷり使いたい方は、無臭でサラリとした精製オイル（&amp;SH）が快適です。
        </p>
      </div>
      <div style="background: var(--bg-page); border-left: 4px solid var(--primary-color); padding: 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;">
        <h3 style="font-size: 1.05rem; font-weight: 700; color: var(--primary-dark); margin-bottom: 0.4rem;">ポイント③：水分とのバランス（乳化・ウォーターインオイル技術）を確認する</h3>
        <p style="font-size: 0.95rem; color: #374151;">
          アボカドの良質な油分を活かしつつ、肌に乗せた瞬間にみずみずしく馴染む設計（キールズの崩れるクリームやバリアリペアのシートマスクなど）を選ぶと、油分特有のベタつきやテカリを感じることなく、ふっくら吸い付くような陶器肌を手に入れられます。
        </p>
      </div>
    </section>

    <!-- セクション3 比較表 -->
    <section class="content-section" id="comparison-table">
      <h2 class="section-title">📊 3. 濃厚アボカドコスメ10選 スペック＆価格比較表</h2>
      <p class="section-p">
        楽天市場公式APIよりリアルタイムに取得した最新の販売価格と製品仕様の一覧表です。目元用・先行乳液・マスク・ピュアオイルなど、多彩なアボカドコスメを比較検討してください。
      </p>
      <div class="compare-table-wrapper">
        <table class="compare-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>商品画像</th>
              <th>商品名・ブランド</th>
              <th>アイテム種別</th>
              <th>楽天参考価格</th>
              <th>商品詳細</th>
            </tr>
          </thead>
          <tbody>
            {table_joined}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4 ランキング詳細 -->
    <section id="ranking-section">
      <h2 style="font-size: 1.6rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 2rem; text-align: center;">
        🏆 濃厚アボカド高保湿コスメおすすめ人気ランキング10選
      </h2>
      {cards_joined}
    </section>

    <!-- セクション5 Q&A -->
    <section class="content-section" id="faq-section">
      <h2 class="section-title">❓ 5. 美容皮膚＆オイル視点で答えるQ&amp;A（よくある質問）</h2>
      {faq_joined}
    </section>

    <!-- セクション6 まとめ -->
    <section class="content-section" id="conclusion">
      <h2 class="section-title">✨ 6. まとめ：粉吹き肌と決別するとろけるアボカド保湿ルーティン</h2>
      <p class="section-p">
        11月から12月にかけての本格的な冬は、皮脂分泌の低下と寒冷によって角質が硬化し、水分だけを与えても粉吹きや引きつりを防ぎきれません。
      </p>
      <p class="section-p">
        「森のバター」と呼ばれるアボカドの豊かなオレイン酸とビタミンEを味方につければ、カチカチに強張った冬肌がとろけるように柔らかく解きほぐされ、触れるたび弾むようなモチモチのツヤ肌が蘇ります。
      </p>
      <p class="section-p">
        目元の集中ケアにキールズ、毎日の洗顔後にはコスメデコルテのプリムラテ、そして全身やおやすみ前の保湿に上質なアボカドオイルを取り入れて、乾燥に怯えることのない、ふっくらと輝く美しい素肌で真冬をお過ごしください。
      </p>
    </section>

    <!-- 内部リンク -->
    <section class="footer-internal-links" id="internal-links">
      <h2 style="font-size: 1.25rem; font-weight: 800; color: #1f2937; margin-bottom: 0.5rem;">
        🔗 併せて読みたい冬コスメ・高保湿スキンケア関連記事
      </h2>
      <p style="font-size: 0.9rem; color: #6b7280;">
        当サイトでは、11月〜12月の肌悩みに合わせた高保湿コスメや成分別ランキングを多数公開しています。
      </p>
      <div class="footer-links-grid" id="footer-links-placeholder">
        <!-- update_all_internal_links.py で同期されます -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 当サイトは楽天市場アフィリエイトプログラムに参加しています。</p>
  </footer>

</body>
</html>
"""

with open("winter-avocado.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated winter-avocado.html successfully. Size: {len(html_content):,} bytes")
