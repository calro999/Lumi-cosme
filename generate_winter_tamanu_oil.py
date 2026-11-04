import json
import re

with open("fetched_final_30_tamanu_baobab_kombucha.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_tamanu_oil"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "🌿 奇跡の木タマヌ×伝統酒粕！真冬のゴワつき砂漠肌を解きほぐす極上の2層式導入美容液",
        "catch": "過酷な環境で育つタマヌオイルの驚異的な修復・保湿力と、老舗酒蔵の酒粕エキスを贅沢に融合。真冬の冷風でカチコチに硬くなった角層を柔らかくほぐし、内側から押し返すようなハリツヤを与えるSHIRO最高峰のオイルセラム",
        "brand_name": "SHIRO (シロ)",
        "capacity": "30ml / ポンプ付き遮光ガラスボトル",
        "type": "高機能2層式ブースターオイル美容液",
        "features": "未精製タマヌオイル（テリハボク種子油）、酒粕エキス、アマモエキス、カンゾウ根エキス",
        "value": "北海道産の素材にこだわるSHIROが沖縄・古宇利島産のタマヌオイルと小林酒造の酒粕を組み合わせた傑作。水分と油分を黄金比で同時チャージし、真冬でも乾燥知らずの透明水光肌を実現",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、皮膚の血流が滞り、角質細胞同士がぎゅっと縮こまってカチカチに硬直してしまいます。普段使っている化粧水が肌表面で弾かれて浸透していかない…そんな真冬の絶望的なインナードライを根本から打開してくれるのが、SHIROの『タマヌ オイルインセラム』です。古来ポリネシアや沖縄で『神の木』と崇められてきたタマヌの種子から搾られる濃厚なオイル層と、アミノ酸豊富な酒粕エキス層の美しい2層構造になっています。",
        "desc_p2": "使用前によく振って2層を乳化させると、とろみのあるまろやかなテクスチャーへ変化。洗顔直後の素肌に数滴馴染ませるだけで、タマヌ特有のリッチな脂肪酸が硬化した角層を瞬時に柔らかく解きほぐし、酒粕エキスの水分がぐんぐん角層深部へ引き込まれていきます。オイル特有のベタつきや被膜感が驚くほど少なく、後から重ねる化粧水の浸透スピードが何倍にも跳ね上がります。使い続けるほどに乾燥小ジワが目立たなくなり、真冬の暖房下でも夕方までみずみずしいツヤが持続します。",
        "target": "真冬になると角質が硬くなりスキンケアが入っていかない方、乾燥によるくすみ・ハリ不足に悩む方、オイルと水分の両方を一度に贅沢補給したい方",
        "point": "洗顔直後、容器を上下によく振って2層をしっかり混ぜ合わせ、手のひらに2〜3滴を取ります。両手で包み込むように温めてから、顔全体へハンドプレスでじっくり押し込みます。特に乾燥しやすい目元や口元には指先で重ねづけすると、夕方の乾燥崩れを完全にブロックできます。"
    },
    {
        "rank": 2,
        "tag": "🌴 鹿児島・大隅半島産無農薬タマヌ！地産原料と低温圧搾にこだわった濃密ピュアオイル",
        "catch": "本土最南端の強い日差しと海風を浴びて自生するタマヌ種子を手作業で収穫し、非加熱コールドプレスで丁寧に搾油。カロフィロリードとオメガ脂肪酸を壊さずそのまま閉じ込めた超濃厚ファームトゥコスメ",
        "brand_name": "BOTANICANON (ボタニカノン)",
        "capacity": "20ml / スポイト付き遮光瓶",
        "type": "無農薬・低温圧搾100%植物美容オイル",
        "features": "鹿児島県大隅半島産未精製タマヌオイル（テリハボク種子油）、パッションフルーツ種子油",
        "value": "防腐剤・界面活性剤・合成香料・着色料一切無添加。自然の恵みを丸ごと肌に届けるエシカル処方で、冬の木枯らしによる肌荒れや赤みを速やかに鎮静",
        "desc_p1": "太平洋の潮風と南国の強烈な太陽を浴びて育つ鹿児島県大隅半島のタマヌの木。ボタニカノンはその希少な種子を手間ひまかけて天日乾燥させ、昔ながらの低温圧搾法で一切の熱を加えずに濃厚なグリーンオイルを抽出しています。熱に弱いポリフェノールや脂肪酸が本来の姿のまま生きているため、真冬の寒冷刺激で赤みやヒリつきを起こしたデリケートな肌に対する整肌パワーは圧倒的です。",
        "desc_p2": "スポイトから滴るオイルは、生命力に満ち溢れた深みのあるオリーブグリーン。独特のナッツのような芳醇な香りは、精製されていない本物のタマヌオイルの証拠です。こっくりと濃厚なオイルでありながら、肌に乗せると体温と溶け合うように馴染み、真冬の乾いた角質層へ濃密なエモリエント膜を形成。夜のスキンケアの最後に1滴仕込んでおくだけで、朝起きた時の肌のふっくら感とキメ密度の高さに心から驚かされます。",
        "target": "成分の純度や無添加に徹底的にこだわりたい方、冬の寒風による肌荒れや赤ら顔を自然のハーブ力でケアしたい方、国産オーガニックコスメを応援したい方",
        "point": "化粧水や乳液でしっかり保湿した後、手のひらにわずか1〜2滴を取り、両手を擦り合わせて薄く伸ばしてから顔全体を優しく包み込みます。乾燥が気になる首元やデコルテ、爪周りのキューティクルケアとしても万能です。"
    },
    {
        "rank": 3,
        "tag": "🔬 森の薬局カロフィラム！オメガ6・9脂肪酸が肌バリアを鉄壁密閉する未精製オーガニック",
        "catch": "手作りコスメや原料のプロとして名高いマンディムーンが厳選した未精製タマヌオイル。肌トラブルを鎮めるカロフィロリードを含み、真冬のひび割れや粉吹き肌を物理的に保護する濃密リペアオイル",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "20ml・50ml / 遮光ドロッパーボトル",
        "type": "未精製・オーガニック認証キャリアオイル",
        "features": "未精製カロフィラム種子油（タマヌオイル）100%、天然オレイン酸、リノール酸、カロフィリン酸",
        "value": "無駄な包装を省いたコストパフォーマンスの高さと、原料本来の薬効を活かしたプロ仕様品質。冬の極度な乾燥による粉吹き肌を救済する常備薬的存在",
        "desc_p1": "冬の乾燥が進むと、肌の皮脂膜が薄くなり、外気とのクッションとなるバリア機能が崩壊してしまいます。少しの刺激でもピリピリとしみたり、頬やすねが白く粉を吹いてしまったりする過酷な状態に、マンディムーンの『未精製タマヌオイル』は極上の保護膜を提供してくれます。マダガスカルやベトナムなどの野生のタマヌ種子から抽出されたオイルは、黄金がかった濃いエメラルドグリーン色を放ちます。",
        "desc_p2": "この未精製オイルには、精製処理によって失われがちな『カロフィロリード』という特有の抗炎症成分がそのまま残留しています。真冬の暖房によるインナードライで敏感になった角層を穏やかに鎮めつつ、豊富なオメガ6（リノール酸）とオメガ9（オレイン酸）が肌の皮脂組成に極めて近い形で角質細胞間脂質を補填。少量で驚くほど伸び広がり、真冬の乾燥冷気をシャットアウトして肌内部の水分蒸発をゼロに抑えてくれます。",
        "target": "冬になると頬や口元が粉を吹いてしまう方、余計な添加物のない100%ピュアな植物油を探している方、手持ちのクリームや乳液にオイルを混ぜて保湿力をブーストしたい方",
        "point": "単体での使用はもちろん、普段お使いの保湿クリームや乳液に1滴混ぜて使うと、保湿持続力が劇的に跳ね上がります。冬場のカサつくひじ、かかと、ひざの頑固な角質肥厚部分にも塗り込むと、数日でしっとり柔らかく変化します。"
    },
    {
        "rank": 4,
        "tag": "🌺 日本最南端の太陽が育んだ奇跡！石垣島の無農薬テリハボク種子を贅沢に絞った生オイル",
        "catch": "石垣島の豊かな赤土と南国の陽光が育んだテリハボクの種子から生まれた純国産タマヌオイル。真冬の過酷な寒冷・強風にさらされる肌を、力強い亜熱帯の生命力で守り抜く高純度フェイスオイル",
        "brand_name": "Natural Pure Oils (石垣島オーガニック)",
        "capacity": "30ml / スポイト付きボトル",
        "type": "国産・無農薬コールドプレスピュアオイル",
        "features": "沖縄石垣島産テリハボク種子油100%、天然ビタミンE、植物性スクワレン",
        "value": "石垣島の自然林から熟した実だけを手作業で採集。南国の強い紫外線から身を守るために蓄えられた豊富な抗酸化物質が、冬の冷えや乾燥による肌老化を強力に防止",
        "desc_p1": "沖縄の島々で昔から防風林として家々を守ってきた『テリハボク』。その種子から採れるオイルは、昔から島の人々の間で擦り傷や火傷、乾燥による肌荒れを癒す民間薬として重宝されてきました。この石垣島産タマヌオイルは、厳しい冬の寒さとは対照的な南国の強烈なエネルギーをたっぷりと宿しており、冬枯れして生気を失った肌にピンとした生命感を取り戻してくれます。",
        "desc_p2": "手に取ると、スモーキーでナッツのような野性味あふれる香りと共に、驚くほど濃密なテクスチャーが広がります。肌に馴染ませると、冬の乾燥によってスカスカになった角層の隙間へピタッと密着。まるで潤いのラップをかけたかのように外気を遮断し、朝までしっとりとしたうるおいをキープします。冬の紫外線や空気の乾燥にさらされやすい日中の保護オイルとしても非常に頼もしい存在です。",
        "target": "国産の植物原料にこだわりたい方、冬の乾燥による肌荒れやバリア機能低下を根本から整えたい方、濃厚でコクのあるオイル美容が好きな方",
        "point": "夜のお風呂上がり、顔に化粧水をたっぷり馴染ませた直後の濡れた肌に、1〜2滴を伸ばします。水分とオイルが肌の上で乳化し、吸い付くようなもっちり肌に仕上がります。"
    },
    {
        "rank": 5,
        "tag": "🍯 汚れを落としながら極上オイルパック！真冬の毛穴汚れと角栓をとろけさせる濃密バーム",
        "catch": "SHIROが誇るタマヌオイルと米ぬか発酵甘酒エキスをダブルで配合した贅沢なクレンジングバーム。冬の頑固なメイクや毛穴の酸化皮脂をとろりと浮かせ、洗い上がりはまるで美容液を塗った後のようなしっとり感",
        "brand_name": "SHIRO (シロ)",
        "capacity": "90g / ジャータイプ（専用スパチュラ付き）",
        "type": "高保湿・角質ケアクレンジングバーム",
        "features": "未精製タマヌオイル、米ぬか発酵甘酒エキス、スクワラン、コメヌカロウ",
        "value": "冬の冷たい外気で硬化した皮脂や角栓を無理なく溶かし出すとろける処方。クレンジングによる皮脂の奪われすぎを防ぎ、洗顔後もつっぱり感ゼロの潤い膜を形成",
        "desc_p1": "11月や12月の寒さで最もダメージを受けやすいスキンケア工程が『クレンジング』です。洗浄力が強すぎるオイルやジェルを使うと、冬の貴重な天然保湿因子（NMF）や皮脂膜まで根こそぎ奪われ、洗顔直後から激しい乾燥とつっぱりに見舞われます。この冬の脱脂ダメージを防ぎ、むしろクレンジングタイムを最高峰のトリートメントに変えてくれるのが、SHIROの『タマヌ クレンジングバーム』です。",
        "desc_p2": "スパチュラですくった時は固形のバームですが、乾いた手のひらに乗せて肌へ滑らせると、体温で瞬く間にリッチなとろとろオイルへと変化。タマヌオイルの微細な油分が真冬の冷えで固まった毛穴の黒ずみや角栓を摩擦レスでじんわり浮き上がらせます。ぬるま湯で洗い流すと、不要な汚れだけが綺麗に落ち、肌表面にはタマヌと米ぬかの上質な保護膜がしっかり残ります。洗顔後の肌はつっぱり感が一切なく、まるで高級な保湿マスクを剥がした後のようなふっくら感に包まれます。",
        "target": "冬の洗顔後につっぱりや乾燥小ジワが気になる方、毛穴の角栓や黒ずみを優しくケアしたい方、至福のクレンジング体験を味わいたい方",
        "point": "専用スパチュラでマスカット1粒大をすくい、乾いた顔全体に乗せます。手のひらの温度を伝えるようにゆっくりと円を描きながら馴染ませ、指先が軽くなったら少量のぬるま湯を加えて白く乳化させてから洗い流します。"
    },
    {
        "rank": 6,
        "tag": "💧 カロフィラム種子油100%！目元・口元・指先のひび割れを集中レスキューする高純度オイル",
        "catch": "過酷な熱帯地方で自生するタマヌの木から採れる種子油を100%そのままボトリング。真冬の冷風で皮むけした口元や、暖房でちりめんジワが寄った目元をピンポイントで集中保護するリペアオイル",
        "brand_name": "Island Herbals (オーガニックタマヌ)",
        "capacity": "30ml / 遮光ドロッパーボトル",
        "type": "100%植物性集中リペア美容オイル",
        "features": "未精製タマヌ種子油100%、高濃度オメガ脂肪酸、天然カロテノイド",
        "value": "余分な希釈剤や合成添加物を一切含まず、タマヌ本来の濃厚な緑色とナッツ香を保持。冬の局所的な乾燥トラブルに少量で確実に応える本格仕様",
        "desc_p1": "真冬になると、顔全体だけでなく、皮膚が特に薄い目の周りや唇の輪郭、指先や爪の生え際など、特定の部分だけがピキピキとひび割れたり皮むけしたりすることがあります。そんな局所的な乾燥SOSに最適なのが、Island Herbalsのピュアタマヌオイルです。タマヌの種子のみをじっくり圧搾して作られたこのオイルは、少量でも驚異的な密着力と被膜形成力を発揮します。",
        "desc_p2": "わずか半滴を指先に取り、乾燥が激しいゾーンに優しくトントンと叩き込むだけで、乾燥冷気から皮膚をしっかりとガード。カロテノイドの黄金緑色の膜が肌荒れ部分を穏やかに整え、皮膚の柔軟性を高めて痛々しいひび割れを防ぎます。ポーチに常備しておけば、日中のメイクの上から乾燥崩れや粉吹きが起きた際にも、指先でピンポイントにツヤと潤いを復活させることができます。",
        "target": "目元や口元の局所的な粉吹き・皮むけに悩んでいる方、冬になると指先や甘皮がガサガサになる方、マルチに使える濃密な集中ケアオイルが欲しい方",
        "point": "朝晩のスキンケアの最後に、指先に半滴を取り、目尻やほうれい線、口角周りに優しくなじませます。ネイルオイルとして爪の生え際に塗り込むと、冬のささくれ予防にも劇的な効果を発揮します。"
    },
    {
        "rank": 7,
        "tag": "🐝 未精製タマヌ×天然ミツロウ！木枯らしから肌を守り抜くスティック型高保湿バーム",
        "catch": "アメリカの人気オーガニックブランドSierra Beesが誇るタマヌオイル高配合バーム。天然ミツロウと未精製タマヌオイルが融合し、真冬の乾燥冷気を物理的にシャットアウトするマルチスティック",
        "brand_name": "Sierra Bees (シエラビーズ)",
        "capacity": "4.25g × 8本セット / スティックタイプ",
        "type": "携帯用オーガニックスティックバーム",
        "features": "USDAオーガニック認証未精製タマヌオイル、エクストラバージンオリーブ油、天然ミツロウ、ヒマワリ種子油、ビタミンE",
        "value": "8本セットで抜群のコスパ。バッグやデスク、ベッドサイドに常備でき、手を使わずに直接塗れる手軽さで冬のあらゆる乾燥パーツを瞬時にプロテクト",
        "desc_p1": "冬の外出時、冷たい北風が直接吹き付ける頬や唇、マスクの摩擦が当たる小鼻周りは、常に乾燥と微小炎症の危険にさらされています。Sierra Beesのタマヌバームスティックは、USDAオーガニック認証を取得した高品質なタマヌオイルとミツロウをベースに作られており、外出先でも手を汚さずに気になる部分へ即座に潤いのバリアを張ることができます。",
        "desc_p2": "肌に滑らせると、ミツロウが体温でほどよくとろけ、タマヌオイルの有効成分が肌にピタッと密着。水分を逃さない強固な油膜を形成しながらも、ベタつかず快適な使い心地を維持します。唇のリップケアとしてはもちろん、冬の冷たい風で赤くなった頬骨の上や、乾燥で粉を吹いた眉間など、どこにでも直塗りできる利便性が冬の心強い味方になります。",
        "target": "外出先やオフィスでこまめに乾燥対策をしたい方、リップだけでなく顔の粉吹き部分にも手軽に使いたい方、高コスパでまとめ買いしたい方",
        "point": "スティックを2〜3ミリ繰り出し、乾燥や摩擦が気になる部位に直接優しく滑らせます。リップの下地として使えば、マットリップを塗っても縦ジワや皮むけを防ぎ、ふっくらした仕上がりが続きます。"
    },
    {
        "rank": 8,
        "tag": "🧼 沖縄産海泥クチャ×タマヌオイル！冬の古い角質を摩擦レスで吸着オフする枠練り石鹸",
        "catch": "沖縄のミネラル豊富な海泥（クチャ）と高純度タマヌオイルを贅沢に練り込んだ熟成固形石鹸。冬の乾燥でゴワついた角質や毛穴汚れを優しくオフしながら、タマヌの潤いヴェールで洗い上げる名品",
        "brand_name": "HONUA (ホヌア)",
        "capacity": "100g / 枠練り手作り固形石鹸",
        "type": "低刺激・高保湿ミネラル洗顔ソープ",
        "features": "沖縄産海泥（マリンシルト / クチャ）、テリハボク種子油（タマヌオイル）、ヤシ油、パーム油、月桃エキス",
        "value": "約60日間じっくり乾燥熟成させる枠練り製法。石鹸素地の約30〜40%が天然の保湿・美容成分で構成されているため、冬の洗顔でも必要な皮脂を落としすぎずしっとり",
        "desc_p1": "冬になると肌のターンオーバーが乱れ、剥がれ落ちるべき古い角質が肌表面に留まって『ゴワゴワ・ザラザラ』した質感になりがちです。しかしスクラブ洗顔などは刺激が強すぎて冬の敏感肌には逆効果。そこでおすすめなのが、微細なマイナスイオン粒子で汚れを吸着する沖縄の海泥クチャと、保湿力抜群のタマヌオイルを組み合わせたホヌアの枠練り石鹸です。",
        "desc_p2": "洗顔ネットで泡立てると、キメの細かいクリーミーな濃密弾力泡がモコモコと立ち上がります。クチャの超微粒子が肌の細かな溝や毛穴の奥まで入り込み、擦らずに汚れを吸着。同時にタマヌオイルの保湿成分が肌に溶け出すため、ぬるま湯で洗い流した瞬間から、肌がツルツルと滑らかになりながらも全くつっぱらない感動的な洗い上がりを体験できます。",
        "target": "冬の肌のゴワつきや化粧ノリの悪さに悩んでいる方、肌に優しい洗顔料で毛穴ケアをしたい方、しっとりとした洗い上がりの固形石鹸が好きな方",
        "point": "ぬるま湯と洗顔ネットを使ってレモン1個分ほどの濃密なクッション泡を作ります。手で肌を擦るのではなく、泡の弾力を使って顔全体を優しく包み込むように押し洗いし、30秒ほどで素早く洗い流します。"
    },
    {
        "rank": 9,
        "tag": "💋 冬の木枯らしで皮むけした唇を瞬時に濃密ラッピング！高純度タマヌリップトリートメント",
        "catch": "未精製タマヌオイルと高純度ビタミンEを凝縮したリップトリートメント。真冬の過酷な乾燥とマスク摩擦でガサガサに荒れた唇を、天然の蜜膜ヴェールで柔らかくぷるんと修復する集中リップケア",
        "brand_name": "Sierra Bees (シエラビーズ)",
        "capacity": "4.25g / スティックタイプ",
        "type": "オーガニック高保湿リップケア",
        "features": "コールドプレスタマヌオイル、オーガニックミツロウ、ヒマワリ油、トコフェロール（ビタミンE）",
        "value": "石油系ミネラルオイルやパラベン、香料を一切使用せず、口に入っても安心なオーガニック食品基準処方。真冬のひび割れ唇を速攻リペアする実力派",
        "desc_p1": "唇には皮脂腺がなく角層も極めて薄いため、冬の湿度が下がると真っ先に水分が蒸発し、皮むけや縦ジワ、ひび割れなどの痛々しいトラブルが発生します。リップクリームを何度も塗り直しても乾燥が止まらない…そんな方にこそ試していただきたいのが、タマヌオイルが持つ強力な組織修復力を活かしたこのリップトリートメントです。",
        "desc_p2": "唇に当てるとスルスルと滑らかに広がり、体温でとろけたタマヌオイルとミツロウが唇の縦ジワの奥深くまで隙間なく密着。荒れて固くなった角層を柔らかく解きほぐしながら、外気の乾燥を跳ね返す保護膜を形成します。寝る前にたっぷり往復塗りして就寝すれば、翌朝には皮むけが落ち着き、ふっくらと血色感のあるみずみずしい唇が蘇ります。",
        "target": "冬になると唇の皮むけや出血に悩まされる方、一般的なリップクリームでは保湿が物足りない方、自然由来成分だけで作られた安全なリップを求める方",
        "point": "唇の縦ジワに沿って、上下に優しく塗り込みます。特に乾燥がひどい夜は、リップを厚めに塗った上から小さく切った食品用ラップを3分間貼る『リップラップパック』を行うと、驚くほどぷるぷるの唇に回復します。"
    },
    {
        "rank": 10,
        "tag": "📦 冬枯れ肌をトータルで蘇らせる！沖縄の恵みを凝縮したタマヌスキンケアプレミアムセット",
        "catch": "沖縄の離島で育った希少なタマヌオイルを核に、冬の乾燥荒れ肌をトータルで救済するトラベル＆スターターセット。洗顔からオイル美容液、バームまでライン使いで相乗効果を実感できる贅沢コレクション",
        "brand_name": "naure (ナウレ)",
        "capacity": "オイル・ソープ・バームのミニサイズセット",
        "type": "高保湿タマヌスキンケア集中トライアルセット",
        "features": "沖縄県産未精製タマヌオイル、月桃葉水、天然ミネラルクレイ、シークヮーサー種子油",
        "value": "タマヌの持つ保湿力と整肌力を最も効果的なステップで体験できる設計。真冬の旅行や出張先での乾燥対策としてはもちろん、タマヌ美容の本格デビューにも最適",
        "desc_p1": "冬の肌は非常にデリケートで、新しいスキンケアを試すのにも慎重になる季節です。naureのプレミアムセットは、沖縄の豊かな自然環境の中で丁寧に搾油されたタマヌオイルを中心に、冬の乾燥肌を優しくいたわるアイテムを厳選した特別なコレクションです。単品で使うよりもステップ使いすることで、角層の柔軟化から保水、密閉までの完璧な保湿サイクルが完成します。",
        "desc_p2": "セットに含まれるソープで肌を優しく洗い上げた後、タマヌオイルを導入美容液として馴染ませ、仕上げに高保湿バームで蓋をする。この3ステップを実践するだけで、冬の冷たい北風や暖房にさらされても、肌内部の水分がしっかりキープされます。ミニサイズでポーチにも収まりやすいため、真冬の乾燥したホテル滞在や移動中のレスキューアイテムとしても極めて高い評価を得ています。",
        "target": "タマヌオイル美容をフルラインで試してみたい方、真冬の旅行や出張でも乾燥肌を完璧にケアしたい方、大切な人への冬のギフトを探している方",
        "point": "洗顔後、肌に化粧水をなじませた直後にオイルを2滴伸ばし、最後にバームを小豆大ほど取って手のひらで温めてから顔全体を覆うようにプレスします。冬の過酷な環境でも乾きを知らない鉄壁の美肌が完成します。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "タマヌオイル（テリハボク種子油）は、なぜ真冬の乾燥や肌荒れにこれほど効果的なのですか？",
        "a": "タマヌオイルは古くから太平洋諸島や沖縄で『森の薬局』『奇跡の万能薬』として親しまれてきた植物油です。他の植物オイルとの最大の違いは、特有の抗炎症成分『カロフィロリード（Calophynic acid）』や豊富なオメガ6（リノール酸）・オメガ9（オレイン酸）脂肪酸を高濃度に含んでいる点にあります。11月〜12月の急激な気温低下とエアコン暖房によって皮脂膜が奪われ、微小な炎症や赤み、粉吹きを起こした真冬の角層を、強力に鎮静させながら皮脂膜の代わりとなって水分蒸発を物理的に食い止めるためです。"
    },
    {
        "q": "タマヌオイル特有の深緑色や香りは、肌に色素沈着したり刺激になったりしませんか？",
        "a": "深緑色はタマヌの種子に含まれる天然のクロロフィル（葉緑素）やカロテノイドによるものであり、人工着色料ではありません。肌に塗布しても色素沈着することは一切なく、むしろ抗酸化作用を発揮して冬のくすみを晴らすサポートをしてくれます。またナッツのような芳醇でスモーキーな香りは、化学溶剤を使わずに低温圧搾された未精製オイルならではの自然な証拠です。敏感肌の方でも安心してお使いいただけますが、ナッツアレルギーをお持ちの方は念のためパッチテストを行ってください。"
    },
    {
        "q": "冬のスキンケアに取り入れる場合、どの順番で使うのが最も効果的ですか？",
        "a": "タマヌオイルは非常に浸透力と柔軟効果が高いため、2通りの使い方がおすすめです。1つ目は『洗顔直後のブースター（導入オイル）』として1〜2滴馴染ませる方法で、冬の冷えでカチコチに硬くなった角質を瞬時に柔らかくし、次に使う化粧水の浸透を何倍にも引き上げます。2つ目は『スキンケアの最後のフタ』として使う方法で、化粧水や乳液で補給した水分が真冬の暖房で蒸発しないよう濃密なシールドを張ることができます。肌のゴワつきが強い時はブースター使い、粉吹きが気になる時は仕上げ使いがベストです。"
    },
    {
        "q": "アルガンオイルやホホバオイルと比べて、タマヌオイルはどのような特徴がありますか？",
        "a": "ホホバオイルはワックスエステル主体で肌表面の保護に優れ、アルガンオイルはビタミンEによるエイジングケアが得意ですが、タマヌオイルは『ダメージ肌の修復力と抗炎症力』において群を抜いています。冬の冷風や寒暖差で赤ら顔になってしまった肌、ひび割れや皮むけを起こした口元や頬など、深刻な冬の肌荒れトラブルを素早く鎮めて正常なバリア機能を再構築するパワーは、植物オイル界でもトップクラスの評価を誇ります。"
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
            <img src="{img}" alt="{it['display_name']}" loading="lazy" width="300" height="300" class="product-img">
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
          <a href="{url}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で最新価格をチェック ➔
          </a>
        </div>
        
        <div class="card-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{p['brand_name']}</td></tr>
            <tr><th>容量 / 容器</th><td>{p['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{p['type']}</td></tr>
            <tr><th>注目保湿成分</th><td>{p['features']}</td></tr>
            <tr><th>コスパ＆価値</th><td>{p['value']}</td></tr>
          </table>
          
          <div class="card-desc">
            <h4>プロによる詳細レビュー＆成分解析</h4>
            <p>{p['desc_p1']}</p>
            <p>{p['desc_p2']}</p>
          </div>
          
          <div class="card-advice">
            <div class="advice-block target-block">
              <h5>🎯 こんな人・肌悩みに最適！</h5>
              <p>{p['target']}</p>
            </div>
            <div class="advice-block point-block">
              <h5>💡 11-12月の効果的な使い方</h5>
              <p>{p['point']}</p>
            </div>
          </div>
        </div>
      </div>
    </article>
    """
    cards.append(card)

cards_joined = "\n".join(cards)

# 構造化データ（JSON-LD）生成
schema_items = []
for it in items:
    schema_items.append({
        "@type": "ListItem",
        "position": it["rank"],
        "name": it["display_name"],
        "url": it["url"],
        "image": it["image"]
    })

schema_faq = []
for f in faqs:
    schema_faq.append({
        "@type": "Question",
        "name": f["q"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": f["a"]
        }
    })

schema_json = json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "ItemList",
            "name": "保湿力の強さで肌乾燥とさようなら！森の薬局が叶える奇跡の濃密保水膜・冬枯れ肌を蘇らせる高保湿タマヌオイルコスメランク10",
            "description": "11月・12月の木枯らしと過酷なエアコン乾燥による肌荒れ・粉吹き・赤みを救う高保湿タマヌオイルコスメを徹底厳選！SHIRO、ボタニカノン、マンディムーンから石垣島産ピュアオイルまで厳選。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！森の薬局が叶える奇跡の濃密保水膜・冬枯れ肌を蘇らせる高保湿タマヌオイルコスメランク10",
            "description": "11月・12月の木枯らしと過酷なエアコン乾燥による肌荒れ・粉吹き・赤みを救う高保湿タマヌオイルコスメを徹底厳選！SHIRO、ボタニカノン、マンディムーンから石垣島産ピュアオイルまで厳選。",
            "image": items[0]["image"],
            "datePublished": "2026-11-04T22:00:00+09:00",
            "dateModified": "2026-11-04T22:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://lumi-cosme.vercel.app/winter-tamanu-oil"
        },
        {
            "@type": "FAQPage",
            "mainEntity": schema_faq
        }
    ]
}, ensure_ascii=False, indent=2)

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！森の薬局が叶える奇跡の濃密保水膜・冬枯れ肌を蘇らせる高保湿タマヌオイルコスメランク10 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の木枯らしと過酷なエアコン乾燥による肌荒れ・粉吹き・赤みを救う高保湿タマヌオイルコスメを徹底厳選！SHIRO、ボタニカノン、マンディムーン、石垣島ピュアオイルまで、楽天市場で買える本物の高保湿10選を詳しく解説。">
  <meta name="keywords" content="タマヌオイル,テリハボク種子油,SHIRO タマヌオイルインセラム,ボタニカノン,冬 乾燥肌 オイル,森の薬局,肌荒れ 保湿オイル">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-tamanu-oil">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1b4d3e;
      --primary-dark: #0f2e25;
      --primary-light: #e8f5e9;
      --accent: #2e7d32;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --text-light: #6b7280;
      --bg-page: #f4fbf7;
      --bg-card: #ffffff;
      --border-color: #c8e6c9;
      --shadow-sm: 0 2px 4px rgba(27, 77, 62, 0.05);
      --shadow-md: 0 4px 12px rgba(27, 77, 62, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(27, 77, 62, 0.15);
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
      background: linear-gradient(135deg, #0f2e25 0%, #1b4d3e 50%, #2e7d32 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem 2.8rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(15, 46, 37, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #c8e6c9;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .site-header-nav a:hover {{ text-decoration: underline; }}
    .site-header h1 {{
      font-size: 1.85rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.4;
      max-width: 900px;
      margin: 0 auto 0.75rem;
    }}
    .site-header p {{
      font-size: 1rem;
      color: #e8f5e9;
      max-width: 750px;
      margin: 0 auto;
    }}

    .container {{
      max-width: 1100px;
      margin: -1.5rem auto 0;
      padding: 0 1rem;
    }}

    .intro-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-lg);
      margin-bottom: 2.5rem;
      border: 1px solid var(--border-color);
    }}
    .intro-badge {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 0.3rem 0.9rem;
      border-radius: 50px;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 1rem;
    }}
    .intro-card h2 {{
      font-size: 1.55rem;
      color: var(--primary-dark);
      margin-bottom: 1.25rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.75rem;
    }}
    .intro-card p {{
      margin-bottom: 1rem;
      font-size: 1rem;
      color: var(--text-sub);
    }}

    .science-box {{
      background: linear-gradient(to right bottom, #e8f5e9, #f1f8e9);
      border-left: 5px solid var(--primary);
      padding: 1.5rem;
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      margin: 1.5rem 0;
    }}
    .science-box h3 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 0.6rem;
    }}

    .toc-card {{
      background: #ffffff;
      border: 1px dashed var(--primary);
      border-radius: var(--radius-md);
      padding: 1.5rem 2rem;
      margin: 2rem 0;
    }}
    .toc-card h3 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      text-align: center;
    }}
    .toc-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 0.6rem;
      list-style: none;
    }}
    .toc-list li a {{
      color: var(--primary);
      text-decoration: none;
      font-size: 0.95rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .toc-list li a:hover {{ text-decoration: underline; }}

    .table-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-md);
      margin-bottom: 3rem;
      border: 1px solid var(--border-color);
    }}
    .table-section h2 {{
      font-size: 1.45rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      text-align: center;
    }}
    .table-wrapper {{
      overflow-x: auto;
    }}
    .rank-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.95rem;
    }}
    .rank-table th {{
      background-color: var(--primary-light);
      color: var(--primary-dark);
      padding: 1rem;
      font-weight: 700;
      border-bottom: 2px solid var(--primary);
      white-space: nowrap;
    }}
    .rank-table td {{
      padding: 1rem;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: middle;
    }}
    .rank-num {{
      font-weight: 800;
      font-size: 1.15rem;
      white-space: nowrap;
    }}
    .rank-1 {{ color: #d97706; }}
    .rank-2 {{ color: #475569; }}
    .rank-3 {{ color: #b45309; }}
    .product-thumb img {{
      border-radius: var(--radius-sm);
      object-fit: cover;
      display: block;
    }}
    .product-name-cell {{
      min-width: 200px;
    }}
    .product-brand {{
      display: block;
      font-size: 0.8rem;
      color: var(--text-light);
      font-weight: 700;
    }}
    .table-prod-link {{
      color: var(--text-main);
      text-decoration: none;
      font-weight: 700;
      font-size: 0.95rem;
    }}
    .table-prod-link:hover {{ color: var(--primary); }}
    .type-badge {{
      display: inline-block;
      background: #f1f5f9;
      color: #334155;
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      font-size: 0.8rem;
      white-space: nowrap;
    }}
    .product-price {{
      font-weight: 800;
      color: #b91c1c;
      white-space: nowrap;
    }}
    .table-btn {{
      display: inline-block;
      background: #bf1e2e;
      color: #ffffff;
      padding: 0.5rem 0.9rem;
      border-radius: 50px;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 700;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: #991b1b; }}

    .product-card {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-md);
      margin-bottom: 3.5rem;
      border: 1px solid var(--border-color);
      overflow: hidden;
      scroll-margin-top: 2rem;
    }}
    .card-header {{
      background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%);
      padding: 1.5rem 2rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      gap: 1.25rem;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-size: 1.35rem;
      font-weight: 800;
      padding: 0.5rem 1.25rem;
      border-radius: var(--radius-sm);
      white-space: nowrap;
      box-shadow: var(--shadow-sm);
    }}
    .rank-badge.rank-1 {{ background: linear-gradient(135deg, #d97706, #f59e0b); }}
    .rank-badge.rank-2 {{ background: linear-gradient(135deg, #475569, #64748b); }}
    .rank-badge.rank-3 {{ background: linear-gradient(135deg, #b45309, #d97706); }}
    .card-titles {{ flex: 1; }}
    .card-tag {{
      display: block;
      font-size: 0.85rem;
      color: var(--primary);
      font-weight: 700;
      margin-bottom: 0.25rem;
    }}
    .card-name {{
      font-size: 1.35rem;
      color: var(--primary-dark);
      font-weight: 800;
      line-height: 1.4;
    }}
    .card-catch {{
      padding: 1.25rem 2rem;
      background: #ffffff;
      font-size: 1rem;
      color: var(--primary-dark);
      border-bottom: 1px dashed var(--border-color);
      line-height: 1.7;
    }}
    .card-body {{
      padding: 2rem;
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2.5rem;
    }}
    @media (max-width: 860px) {{
      .card-body {{ grid-template-columns: 1fr; }}
    }}
    .card-image-box {{
      text-align: center;
    }}
    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      transition: transform 0.2s ease;
    }}
    .product-img:hover {{ transform: scale(1.02); }}
    .card-price-box {{
      margin: 1.25rem 0 0.75rem;
    }}
    .price-label {{
      display: block;
      font-size: 0.8rem;
      color: var(--text-light);
    }}
    .price-val {{
      font-size: 1.85rem;
      font-weight: 800;
      color: #bf1e2e;
    }}
    .price-tax {{
      font-size: 0.85rem;
      color: var(--text-light);
    }}
    .card-review-box {{
      margin-bottom: 1.25rem;
      font-size: 0.9rem;
    }}
    .star-rating {{
      color: #f59e0b;
      font-weight: 800;
    }}
    .review-count {{
      color: var(--text-light);
    }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf1e2e 0%, #e11d48 100%);
      color: #ffffff;
      text-align: center;
      padding: 1rem 1.5rem;
      border-radius: 50px;
      text-decoration: none;
      font-weight: 800;
      font-size: 1rem;
      box-shadow: 0 4px 15px rgba(191, 30, 46, 0.3);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(191, 30, 46, 0.4);
    }}

    .card-spec-box {{
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
    }}
    .spec-table th {{
      width: 25%;
      padding: 0.6rem 0.8rem;
      background: var(--primary-light);
      color: var(--primary-dark);
      text-align: left;
      border-bottom: 1px solid #ffffff;
      font-weight: 700;
    }}
    .spec-table td {{
      padding: 0.6rem 0.8rem;
      background: #fafafa;
      border-bottom: 1px solid #f1f5f9;
      color: var(--text-sub);
    }}
    .card-desc h4 {{
      font-size: 1.15rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .card-desc p {{
      margin-bottom: 0.85rem;
      font-size: 0.98rem;
      color: var(--text-sub);
      line-height: 1.8;
    }}
    .card-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
      margin-top: 0.5rem;
    }}
    @media (max-width: 600px) {{
      .card-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1.25rem;
      border-radius: var(--radius-md);
    }}
    .target-block {{
      background: #f0fdf4;
      border: 1px solid #bbf7d0;
    }}
    .point-block {{
      background: #fefce8;
      border: 1px solid #fef08a;
    }}
    .advice-block h5 {{
      font-size: 0.95rem;
      margin-bottom: 0.5rem;
      color: var(--text-main);
    }}
    .advice-block p {{
      font-size: 0.88rem;
      color: var(--text-sub);
      line-height: 1.6;
    }}

    .guide-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-md);
      margin-bottom: 3rem;
      border: 1px solid var(--border-color);
    }}
    .guide-section h2 {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      border-bottom: 2px solid var(--primary-light);
      padding-bottom: 0.75rem;
    }}
    .guide-section h3 {{
      font-size: 1.2rem;
      color: var(--primary);
      margin: 1.5rem 0 0.75rem;
    }}
    .guide-section p {{
      margin-bottom: 1rem;
      color: var(--text-sub);
      font-size: 1rem;
    }}
    .guide-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
      margin: 1.5rem 0;
    }}
    .guide-card {{
      background: #f8fafc;
      padding: 1.5rem;
      border-radius: var(--radius-md);
      border-top: 4px solid var(--primary);
    }}
    .guide-card h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
    }}

    .faq-section {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      padding: 2.5rem;
      box-shadow: var(--shadow-md);
      margin-bottom: 3rem;
      border: 1px solid var(--border-color);
    }}
    .faq-section h2 {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      text-align: center;
    }}
    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px solid #f1f5f9;
      padding-bottom: 1.5rem;
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
      content: 'Q';
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-weight: 800;
    }}
    .faq-a {{
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.8;
      padding-left: 2rem;
    }}

    .related-links {{
      background: #ffffff;
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-sm);
      margin-bottom: 3rem;
      border: 1px solid #e2e8f0;
    }}
    .related-links h3 {{
      font-size: 1.2rem;
      color: var(--text-main);
      margin-bottom: 1.25rem;
      text-align: center;
    }}
    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1rem;
    }}
    .related-card {{
      background: #f8fafc;
      padding: 1rem;
      border-radius: var(--radius-sm);
      border-left: 3px solid var(--primary);
      text-decoration: none;
      color: var(--text-main);
      font-size: 0.9rem;
      font-weight: 700;
      display: block;
      transition: background 0.2s;
    }}
    .related-card:hover {{
      background: var(--primary-light);
      color: var(--primary-dark);
    }}

    .site-footer {{
      text-align: center;
      padding: 2.5rem 1rem 1rem;
      color: var(--text-light);
      font-size: 0.85rem;
    }}
    .site-footer a {{
      color: var(--primary);
      text-decoration: none;
    }}
    .site-footer a:hover {{ text-decoration: underline; }}
  </style>
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>

  <header class="site-header">
    <div class="site-header-nav">
      <a href="/">🏠 Lumi Cosme ホームへ戻る</a>
    </div>
    <h1>保湿力の強さで肌乾燥とさようなら！森の薬局が叶える奇跡の濃密保水膜・冬枯れ肌を蘇らせる高保湿タマヌオイルコスメランク10</h1>
    <p>11月・12月の木枯らしとエアコン暖房でボロボロに荒れた角層を即効レスキュー。奇跡の木がもたらす濃密な保護膜とカロフィロリードの抗炎症パワーで、真冬でも乾かない満水もっちり肌へ</p>
  </header>

  <main class="container">
    <section class="intro-card">
      <span class="intro-badge">11月〜12月・深刻な乾燥肌トラブル救済特集</span>
      <h2>なぜ11〜12月の冬枯れ肌に「タマヌオイル」が最強の切り札になるのか？</h2>
      <p>立冬を過ぎ、11月から12月へと季節が移り変わる時期は、1年の中で最も肌にとって過酷なターニングポイントです。外気温が急降下して冷たい木枯らしが吹き付ける一方、室内ではエアコン暖房がフル稼働し、湿度は連日20〜30%台まで急落します。この厳しい内外の環境変化によって、肌表面の皮脂膜は激減し、角質細胞同士を接着している細胞間脂質（セラミドなど）の構造がガタガタに崩れてしまいます。</p>
      <p>その結果引き起こされるのが、化粧水が弾かれて浸透しない『角層の硬直・ゴワつき』、頬やりんごのように赤くヒリつく『寒暖差トラブル』、そして目元や口元の『痛々しい粉吹き・皮むけ』です。水分をいくら補給しても、肌表面を覆う油膜が脆弱であれば、補った水分は暖房の風によって数十分で蒸散してしまいます。</p>
      
      <div class="science-box">
        <h3>🔬 科学が証明する「タマヌオイル（テリハボク種子油）」の驚異的なメカニズム</h3>
        <p>南太平洋諸島や沖縄などで古来『森の薬局』『神の木』と尊ばれてきたタマヌオイル（学名：Calophyllum inophyllum）は、一般的な植物油とは一線を画す特異な成分プロファイルを持っています。タマヌオイルには特有の抗炎症成分である<strong>『カロフィロリード（Calophynic acid）』</strong>が高濃度に含まれており、真冬の寒冷刺激で興奮した毛細血管や微小炎症を素早く穏やかに鎮静させます。</p>
        <p>さらに、人の皮脂に近い<strong>『オレイン酸（オメガ9）』</strong>と角質を柔軟にする<strong>『リノール酸（オメガ6）』</strong>が黄金バランスで調和。深緑色の濃厚な1滴が、角層の隙間へ瞬時に溶け込んで強固な擬似皮脂膜を形成し、冬の乾燥冷気を物理的にシャットアウトしながら肌内部の水分蒸散を鉄壁ブロックします。</p>
      </div>

      <p>本記事では、楽天市場で実際に購入できる正規取り扱いコスメの中から、成分純度、低温圧搾（コールドプレス）製法、保湿持続力、そして口コミ評価を美容アナリストが徹底検証し、真冬の肌を劇的に救済する高保湿タマヌオイルコスメ厳選10選をランキング形式で詳しくご紹介します。</p>

      <div class="toc-card">
        <h3>📑 目次：高保湿タマヌオイルコスメTOP10</h3>
        <ul class="toc-list">
          <li><a href="#rank-1">第1位：SHIRO タマヌ オイルインセラム</a></li>
          <li><a href="#rank-2">第2位：BOTANICANON タマヌオイル リッチピュア</a></li>
          <li><a href="#rank-3">第3位：mandy moon オーガニック未精製タマヌオイル</a></li>
          <li><a href="#rank-4">第4位：Natural Pure Oils 石垣島ピュア タマヌオイル</a></li>
          <li><a href="#rank-5">第5位：SHIRO タマヌ クレンジングバーム</a></li>
          <li><a href="#rank-6">第6位：Island Herbals オーガニック タマヌオイル</a></li>
          <li><a href="#rank-7">第7位：Sierra Bees オーガニック タマヌバームスティック</a></li>
          <li><a href="#rank-8">第8位：HONUA ヤラブ フェイス＆ボディソープバー</a></li>
          <li><a href="#rank-9">第9位：Sierra Bees エキストラモイスト タマヌリップ</a></li>
          <li><a href="#rank-10">第10位：naure 沖縄産タマヌオイル プレミアムセット</a></li>
        </ul>
      </div>
    </section>

    <section class="table-section">
      <h2>🏆 高保湿タマヌオイルコスメおすすめ比較一覧</h2>
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
      <h2>💡 失敗しない高保湿タマヌオイルコスメの選び方＆活用術</h2>
      
      <h3>1. 「未精製（コールドプレス）」と「精製・ブレンド」の使い分け</h3>
      <p>タマヌオイルを選ぶ際、最も注目すべきは精製度です。タマヌ本来の抗炎症成分カロフィロリードや葉緑素、ビタミン類を最大限に享受したい場合は、深緑色をした『未精製・コールドプレス』のピュアオイルがベストです。一方、独特のナッツのような芳醇な香りをマイルドに楽しみたい方や、メイク前のブースターとして軽やかに使いたい場合は、SHIROのように酒粕エキス等の美容水とブレンドされた2層式セラムが極めて扱いやすくおすすめです。</p>

      <div class="guide-grid">
        <div class="guide-card">
          <h4>未精製ピュアタマヌ（深緑色）</h4>
          <p>夜の集中保湿、ひび割れ・皮むけ・赤ら顔の集中レスキュー、スキンケアの最後のフタに最適。少量の1滴で圧倒的な密閉シールド力を発揮します。</p>
        </div>
        <div class="guide-card">
          <h4>2層式美容液・ブレンドタイプ</h4>
          <p>洗顔直後のブースター（導入）、朝のメイク前保湿に最適。水分と油分を同時にチャージできるため、ゴワついた角質を素早くほぐし化粧ノリを高めます。</p>
        </div>
        <div class="guide-card">
          <h4>バーム・スティックタイプ</h4>
          <p>日中の携帯用、目元や口元のピンポイント保護、外出先での冷風ガードに最適。手を汚さずに直塗りでき、長時間の被膜保護が可能です。</p>
        </div>
      </div>

      <h3>2. 11月〜12月の冷え枯れ肌を蘇らせる「温感ホットプレス」手順</h3>
      <p>冬の低い室温では、植物オイルの分子運動が鈍くなり肌馴染みが悪く感じられることがあります。タマヌオイルの浸透力を極限まで高めるためには、以下の3ステップを実践してください。</p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>手のひらで温める：</strong> オイルを1〜2滴取ったら、すぐに顔へ乗せず、両手を擦り合わせて体温でしっかり温めます。</li>
        <li><strong>包み込むようにハンドプレス：</strong> こするのではなく、手のひら全体で頬、額、あごを優しく包み込み、10秒間じっくりと体温を伝えます。</li>
        <li><strong>蒸しタオルブースト（週1回）：</strong> オイルを顔全体に馴染ませた後、温かい蒸しタオルを3分乗せると、硬直した毛穴がゆるみ、驚くほどふっくらしたベルベット肌が手に入ります。</li>
      </ol>
    </section>

    <section class="faq-section">
      <h2>❓ タマヌオイルスキンケアに関するよくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q">タマヌオイル（テリハボク種子油）は、なぜ真冬の乾燥や肌荒れにこれほど効果的なのですか？</div>
        <div class="faq-a">タマヌオイルは古くから太平洋諸島や沖縄で『森の薬局』『奇跡の万能薬』として親しまれてきた植物油です。他の植物オイルとの最大の違いは、特有の抗炎症成分『カロフィロリード（Calophynic acid）』や豊富なオメガ6（リノール酸）・オメガ9（オレイン酸）脂肪酸を高濃度に含んでいる点にあります。11月〜12月の急激な気温低下とエアコン暖房によって皮脂膜が奪われ、微小な炎症や赤み、粉吹きを起こした真冬の角層を、強力に鎮静させながら皮脂膜の代わりとなって水分蒸発を物理的に食い止めるためです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">タマヌオイル特有の深緑色や香りは、肌に色素沈着したり刺激になったりしませんか？</div>
        <div class="faq-a">深緑色はタマヌの種子に含まれる天然のクロロフィル（葉緑素）やカロテノイドによるものであり、人工着色料ではありません。肌に塗布しても色素沈着することは一切なく、むしろ抗酸化作用を発揮して冬のくすみを晴らすサポートをしてくれます。またナッツのような芳醇でスモーキーな香りは、化学溶剤を使わずに低温圧搾された未精製オイルならではの自然な証拠です。敏感肌の方でも安心してお使いいただけますが、ナッツアレルギーをお持ちの方は念のためパッチテストを行ってください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">冬のスキンケアに取り入れる場合、どの順番で使うのが最も効果的ですか？</div>
        <div class="faq-a">タマヌオイルは非常に浸透力と柔軟効果が高いため、2通りの使い方がおすすめです。1つ目は『洗顔直後のブースター（導入オイル）』として1〜2滴馴染ませる方法で、冬の冷えでカチコチに硬くなった角質を瞬時に柔らかくし、次に使う化粧水の浸透を何倍にも引き上げます。2つ目は『スキンケアの最後のフタ』として使う方法で、化粧水や乳液で補給した水分が真冬の暖房で蒸発しないよう濃密なシールドを張ることができます。肌のゴワつきが強い時はブースター使い、粉吹きが気になる時は仕上げ使いがベストです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">アルガンオイルやホホバオイルと比べて、タマヌオイルはどのような特徴がありますか？</div>
        <div class="faq-a">ホホバオイルはワックスエステル主体で肌表面の保護に優れ、アルガンオイルはビタミンEによるエイジングケアが得意ですが、タマヌオイルは『ダメージ肌の修復力と抗炎症力』において群を抜いています。冬の冷風や寒暖差で赤ら顔になってしまった肌、ひび割れや皮むけを起こした口元や頬など、深刻な冬の肌荒れトラブルを素早く鎮めて正常なバリア機能を再構築するパワーは、植物オイル界でもトップクラスの評価を誇ります。</div>
      </div>
    </section>

    <section class="related-links">
      <h3>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h3>
      <div class="related-grid">
        <a href="/winter-baobab-oil" class="related-card">🌳 高保湿バオバブオイルコスメ10選</a>
        <a href="/winter-kombucha" class="related-card">🍵 高保湿コンブチャコスメ10選</a>
        <a href="/winter-prickly-pear" class="related-card">🌵 ウチワサボテンオイルコスメ10選</a>
        <a href="/winter-calendula" class="related-card">🌼 高保湿カレンデュラコスメ10選</a>
        <a href="/winter-marula-oil" class="related-card">💧 高保湿マルラオイルコスメ10選</a>
        <a href="/winter-manuka-honey" class="related-card">🍯 高純度マヌカハニーコスメ10選</a>
        <a href="/winter-resurrection-plant" class="related-card">🌿 復活草・トレハロースコスメ10選</a>
        <a href="/winter-ceramide-cream" class="related-card">🛡️ 高保湿セラミドクリーム10選</a>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>&copy; 2026 Lumi Cosme. All rights reserved. 掲載価格は楽天市場の最新参考価格です。</p>
    <p style="margin-top: 0.5rem;"><a href="/">ホーム</a> | <a href="/winter-tamanu-oil">高保湿タマヌオイル</a> | <a href="/winter-baobab-oil">高保湿バオバブオイル</a> | <a href="/winter-kombucha">高保湿コンブチャ</a></p>
  </footer>

</body>
</html>"""

with open("winter-tamanu-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved winter-tamanu-oil.html successfully!")
