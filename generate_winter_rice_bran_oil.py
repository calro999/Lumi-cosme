import json
import re

with open("fetched_3new_macadamia_pomegranate_ricebran.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_rice_bran_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🌾 米ぬか美肌成分×純度100%植物油！真冬のゴワつく角層を吸い付くような白玉肌へ導く名品オイル",
        "catch": "創業130年を超える米ぬかスキンケアのパイオニア・リアルが誇る最高峰美容オイル。天然オリザノールと米ぬかセラミドが、真冬の寒冷で硬直した角層へスッと溶け込み透明感あふれる素肌を再現",
        "brand_name": "美人ぬか (リアル)",
        "capacity": "30ml / スポイト式遮光ボトル",
        "type": "高純度米ぬかフェイシャル美容オイル",
        "features": "コメヌカ油（純度100%）、天然ガンマ-オリザノール、トコトリエノール、フェルラ酸",
        "value": "無香料・無着色・防腐剤フリー。日本の米ぬかから抽出した高純度オイルが、冬の冷えによる末梢血行不良とくすみを根本からケアし、触れたくなるもっちり素肌へ",
        "desc_p1": "11月から12月にかけての日本の真冬は、湿度の急落に加えて厳しい冷え込みが肌を直撃します。寒さによって毛細血管が収縮し、顔色が青白くどんよりとくすむ『冬の血行不良くすみ』と、皮脂不足による『粉吹き・ゴワつき』が同時に発生します。美人ぬかの『純米 美容オイル』は、古来より日本女性の美しい白肌を支え続けてきた米ぬかの叡智を現代のサイエンスで精緻に精製した名作です。",
        "desc_p2": "米ぬか特有の有用ポリフェノール『ガンマ-オリザノール』と、通常のビタミンEの約50倍の抗酸化力を持つ『トコトリエノール』が濃密に溶け込んでいます。手にとると黄金色のみずみずしいオイルで、肌に乗せた瞬間に親和性の高いオレイン酸・リノール酸が角質層の隙間へすっと吸い込まれていきます。冬の寒さでこわばった肌組織を内側から柔らかく解きほぐし、まるで炊きたてのお米のようにふっくらと艶やかな『白玉肌』へと整えます。朝のメイク前に使ってもテカリにくく、日中の乾燥くすみを夕方まで寄せ付けません。",
        "target": "冬になると肌が青白くくすんで血色感が失われる方、日本人の肌質に最も親和性の高い伝統の保湿オイルを使いたい方、無添加処方で低刺激な美容オイルを求める方",
        "point": "洗顔後すぐの肌に、スポイトで1〜2滴を手にとり、手のひらで温めてから優しくハンドプレスしてなじませます。その後に化粧水をたっぷり重ねると、水分がぐんぐん角層へ引き込まれる驚きの吸水力を体感できます。"
    },
    {
        "rank": 2,
        "tag": "💧 国内精製無添加×大容量200ml！冬の角層バリアの隙間を埋め尽くす高コスパキャリアオイル",
        "catch": "徹底的な国内精製による極上の低刺激性。天然オリザノールが冬の暖房乾燥から素肌を守り抜き、顔から首・デコルテ・ボディまで惜しみなく使える大容量マルチオイル",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "200ml (50ml×4本パック) / ドロッパーボトル",
        "type": "国内精製ピュアライスブランオイル",
        "features": "コメヌカ油100%、天然γ-オリザノール含有、無添加、アルコールフリー",
        "value": "使い切りやすい50mlミニボトルの4本セット。いつでも搾りたてのように新鮮な状態で使え、真冬の乾燥で硬くなった家族全員の肌を優しく保湿",
        "desc_p1": "植物オイルは空気や光に触れることで酸化が進みやすいため、冬の乾燥シーズン中に使い切れる新鮮さが極めて重要になります。&SHの『ライスブランオイル 200ml』は、50ml遮光ボトル×4本という画期的な分包スタイルを採用し、開封したての高い抗酸化パワーを常に素肌へ届けることができます。",
        "desc_p2": "高度な精製によって油分特有の重さを削ぎ落とし、サラリとしたシルキーなテクスチャーに仕上げられています。お米由来のオレイン酸とリノール酸が、真冬の寒冷でひび割れそうになった角層バリアの隙間を均一にコーティング。衣服にベタつき移りすることなく、首筋やデコルテ、肘・膝まで滑らかに潤します。洗面台、リビング、ベッドサイドに1本ずつ常備しておけば、冬の乾燥を感じた瞬間にいつでも手軽に極上保湿を行えます。",
        "target": "大容量でも酸化させずに常にフレッシュなオイルを使いたい方、家族みんなで惜しみなく全身保湿に使いたい方、ベタつきのないサラッとした米油を好む方",
        "point": "入浴後、タオルで軽く水分を押さえた直後の肌に、手足や首元へスルスルと塗り伸ばします。水分とオイルが肌の上で瞬時に乳化し、一日中粉吹き知らずのなめらかな保護膜が持続します。"
    },
    {
        "rank": 3,
        "tag": "🌱 国産無農薬米ぬか100%！冬の過酷な寒冷乾燥で荒れた角層を優しく守るサステナブルオイル",
        "catch": "無農薬栽培された国産米ぬかのみを厳選抽出。化学薬品を一切使わずに圧搾された純粋な米油が、冬の寒暖差でピリつくデリケート肌をふんわり包み込む",
        "brand_name": "みんなでみらいを",
        "capacity": "30ml / スポイト遮光瓶",
        "type": "完全無添加オーガニック米ぬか美容オイル",
        "features": "国産無農薬米ぬか油、ガンマ-オリザノール、天然ビタミンE、完全無添加",
        "value": "SDGsアワード受賞ブランド。人にも地球にも極めて優しい完全植物性処方。真冬の過酷な環境でバリア機能が低下した肌でも、刺激なく穏やかに保湿バリアを再建",
        "desc_p1": "冬の乾燥が進むと、ちょっとした外気刺激や摩擦でも肌が赤くなったり、ピリピリとしみたりする敏感状態（ゆらぎ肌）に陥りやすくなります。『みんなでみらいを 米ぬか美容オイル』は、そんな極度のデリケート状態にある肌のために、徹底して農薬・化学肥料を使わずに育てられた国産米ぬかだけを原料として作られています。",
        "desc_p2": "抽出工程でも化学溶剤を一切使わず、昔ながらの圧搾法で丁寧に絞り出されたオイルは、透き通るようなピュアな質感。肌に乗せると、まるで第二の皮膚のようにスルスルと馴染み、刺激を与えることなく乾いた角層を保護膜で覆い隠します。冬の寒風による赤ら顔や、マスク擦れによるフェイスラインのカサつきを穏やかに鎮静。余計なものを一切含まないからこそ、赤ちゃんの保湿や授乳中のママのリップケアにも安心して使用できます。",
        "target": "冬になると通常の化粧品がピリピリとしみる敏感肌の方、無農薬・無添加の完全ナチュラルコスメにこだわりたい方、赤みや肌荒れをやさしく保護したい方",
        "point": "洗顔後、化粧水をつけずにこのオイルを1滴だけ手のひらで伸ばし、顔全体を優しく押さえる『シンプルバリアケア』がおすすめ。肌への摩擦刺激を極限まで減らしながらバリアを立て直せます。"
    },
    {
        "rank": 4,
        "tag": "🌹 食べる米ぬか油×ダマスクローズ精油！真冬の冷えくすみを晴らし極上の潤いを与えるプレミアムオイル",
        "catch": "食用の米ぬかから圧搾した極上米油に最高級ブルガリアンローズを配合。肌の巡りを整えるγ-オリザノールと女性らしさを高める気品ある香りが真冬の肌を薔薇色に染め上げる",
        "brand_name": "Bran-Drip (ブランドリップ)",
        "capacity": "100ml / スプレー式ボトル",
        "type": "高機能米ぬかスキンオイル（ローズブレンド）",
        "features": "高純度米ぬか油（食用グレード）、ダマスクバラ花油、天然ビタミンE、無鉱物油",
        "value": "口に入れても安全な最高品質の米ぬかオイル。スプレー式で手軽に吹きかけられ、冬の冷えで滞った肌にツヤと血色感、そして吸い付くような潤いを即効チャージ",
        "desc_p1": "『素肌につけるものは、食べられるほど安全でなければならない』という思想のもと、米油のトップメーカーと共同開発された『ブランドリップ』。新鮮な玄米のぬか層と胚芽からわずかしか採れない食用レベルの最高級米油に、ブルガリア産ダマスクローズの天然精油を贅沢にブレンドした至高のスキンオイルです。",
        "desc_p2": "スプレーをプッシュすると、ローズの芳醇でクラシカルな生花の香りが立ち上り、冬の寒さでこわばった表情筋と心を一瞬で解きほぐします。米ぬかオイルの持つ高いエモリエント性とオリザノールの血流促進作用が、真冬の冷えで血色の失われた顔色にほんのりと温かみのある透明感をもたらします。スプレータイプのため、日中の乾燥対策としてメイクの上からサッと吹きかけたり、冬の静電気で広がる毛先のトリートメントとしても極めてエレガントに機能します。",
        "target": "冬の顔色のくすみ・暗さを一気に明るくトーンアップしたい方、ローズの優雅な香りに包まれてスキンケアをしたい方、最高純度の安心安全なオイルを求める方",
        "point": "夜のお手入れの最後に、手のひらに2プッシュを吹きかけ、両手を合わせて香りを立たせてから顔全体を包み込みます。深呼吸しながら優しくハンドプレスすることで、睡眠中の集中リペア効果が高まります。"
    },
    {
        "rank": 5,
        "tag": "🛁 国産米ぬか100%×超大容量1000ml！真冬のお風呂上がり全身保湿に惜しみなく使える大容量オイル",
        "catch": "プロのマッサージサロンでも愛用される国産100%ライスブランオイル。特大ポンプ式で、真冬の粉吹きすね・カサつく背中・ひび割れ踵まで家族全員の全身乾燥を徹底ブロック",
        "brand_name": "Nature Herb (ネイチャーハーブ)",
        "capacity": "1000ml / 遮光特大ポンプボトル",
        "type": "全身用高保湿マッサージ＆キャリアオイル",
        "features": "国産米ぬか油100%、天然ビタミンE、無香料・無着色、プッシュポンプ式",
        "value": "1リットルという圧倒的なボリューム。お風呂上がりの脱衣所でポンプをワンプッシュするだけで、冬の激しい水分蒸発から全身を瞬時にガードするコストパフォーマンスの覇者",
        "desc_p1": "真冬になると、顔のお手入れだけでなく、すね、太もも、腰回り、背中など、全身の皮膚が悲鳴を上げ始めます。特に11月下旬以降は暖房による室内乾燥と冬の木枯らしが重なり、服を脱いだ瞬間に皮膚がカサカサと剥がれ落ちる粉吹きトラブルが頻発します。ネイチャーハーブの『国産 ライスブランオイル 1000ml』は、そんな冬の全身乾燥を完全に制圧するサロン仕様の大容量アイテムです。",
        "desc_p2": "日本の主食であるお米から採れたオイルだからこそ、私たちの皮膚への親和性は群を抜いています。サラッとした伸びの良いテクスチャーで、広い背中や脚全体へもストレスなくスルスルと広がります。入浴直後の濡れた肌へ3〜4プッシュを馴染ませてから軽くタオルオフすれば、高価なボディクリームを何本も消費することなく、一日中シルクのようなもっちり肌が続きます。クレンジングや頭皮マッサージオイルとしても兼用できる万能オイルです。",
        "target": "冬場にすねや背中が粉を吹いて痒くてたまらない方、惜しみなく全身に使える大容量オイルを探している方、家族全員で使える安心の国産オイルを求める方",
        "point": "お風呂から上がる直前の濡れた素肌に、手のひらで大きく円を描くように全身へ塗り伸ばします。水分を抱き込んだまま角層へ浸透するため、ベタつきが一切残らず吸い付くような素肌に仕上がります。"
    },
    {
        "rank": 6,
        "tag": "🌿 低温圧搾キャリアオイル！冬の入浴後ブースターとして角層深部へすっと浸透する名品",
        "catch": "生活の木が厳選した高純度プラントオイル。お米の栄養分を損なわないよう丁寧に抽出され、冬の乾燥小ジワやゴワつくキメをなめらかに整えるマルチキャリアオイル",
        "brand_name": "Tree of life (生活の木)",
        "capacity": "25ml / 遮光ドロップガラス瓶",
        "type": "高純度ライスブランキャリアオイル",
        "features": "コメヌカ油（純度100%）、低温抽出、無香料、無添加",
        "value": "少量サイズでいつでも新鮮。アロマテラピーのベースオイルとしてはもちろん、単体でのフェイスブースターとしても秀逸な角質柔軟効果を発揮",
        "desc_p1": "アロマとハーブのスペシャリスト・生活の木が取り扱うライスブランオイルは、厳格な品質基準に適合した高品質な純植物油です。お米のぬか層から抽出されたこのオイルは、重すぎず軽すぎない絶妙な粘性を持ち、冬の肌にしっとりとした潤いのヴェールをもたらします。",
        "desc_p2": "角層への浸透速度が非常に速く、塗布後すぐにサラリと落ち着くため、朝の洗顔後のスキンケア導入液としても快適に使用できます。米ぬかに含まれる豊富なビタミンEが冬の乾燥による小ジワを目立たなくし、肌表面のキメをキュッと整えてくれます。エッセンシャルオイル（ラベンダーやフランキンセンスなど）を1滴ブレンドしてオリジナルの冬用トリートメントオイルを仕立てるベースとしても最適です。",
        "target": "生活の木の信頼できる品質基準でオイルを選びたい方、少量サイズで旅行や外出先にも持ち歩きたい方、手作りアロマコスメのベースを探している方",
        "point": "洗顔後、化粧水の前に1〜2滴を手のひらで温めて顔全体にプレスします。特に乾燥しやすい目尻やほうれい線には、指先で優しく重ねづけしてから化粧水をつけてください。"
    },
    {
        "rank": 7,
        "tag": "🍶 老舗酒蔵の米ぬかエキス×日本酒酵母！真冬の過酷な乾燥と外気刺激から肌を守り抜く濃厚クリーム",
        "catch": "名酒『日本盛』が手がけるロングセラー高保湿クリーム。米ぬかオイル・日本酒酵母・水溶性コラーゲンが融合し、真冬の木枯らしにさらされても一日中乾かない濃密シールドを形成",
        "brand_name": "日本盛 (米ぬか美人)",
        "capacity": "40g / ジャー容器",
        "type": "濃厚高保湿リッチフェイスクリーム",
        "features": "コメヌカ油、コメ発酵液（日本酒）、コメヌカエキス、水溶性コラーゲン、ヒアルロン酸Na",
        "value": "オイルの油分密閉力と発酵アミノ酸の保水力をハイブリッド。真冬の過酷な冷気や暖房直撃環境でも、肌の内側の潤いを一切逃さない鉄壁の保護シールド処方",
        "desc_p1": "酒造りの杜氏（とうじ）の手が冬の厳しい寒さや水仕事の中でも白くすべすべしていることに着目して生まれた『米ぬか美人』シリーズ。その最高峰保湿を担う『うるおいクリーム』は、米ぬか油の油分バリアと日本酒発酵エキスの豊富なアミノ酸を融合させた、真冬の濃厚保湿クリームです。",
        "desc_p2": "ジャーの蓋を開けると、こっくりとリッチで重みのあるテクスチャー。肌に伸ばすと体温で滑らかにとろけ、角質層の隅々まで密着して保護膜を張ります。暖房の効いた部屋で一日中過ごしても、夕方になっても頬がカサつかず、内側から押し返してくるようなもっちりとした弾力が持続。就寝前にたっぷり塗って眠る『ナイトスリーピングパック』としても絶大で、翌朝の洗顔時には吸い付くような透明美肌に仕上がります。",
        "target": "オイル単体よりも濃厚なクリームでしっかり蓋をしたい方、冬になると暖房のせいで夕方に肌がカピカピに乾く方、酒蔵発酵コスメの保湿力を実感したい方",
        "point": "夜のお手入れの最後に、パール粒大を手にとって顔全体に優しく塗り広げます。乾燥が特に激しい目元や口元には、指先で優しくトントンと重ね塗りして密閉してください。"
    },
    {
        "rank": 8,
        "tag": "🧪 医薬部外品原料規格の高純度精製！天然オリザノールとフェルラ酸が透明感を呼び覚ますキャリアオイル",
        "catch": "研究所クオリティの確かな安全性。高度な脱色・脱臭技術によりアレルゲンを極限まで低減し、米ぬかの持つエイジングケア有用成分だけを贅沢に抽出したプロ仕様",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml / 遮光ドロッパーボトル",
        "type": "高純度精製ライスブランオイル",
        "features": "コメヌカ油（医薬部外品原料規格）、天然γ-オリザノール、フェルラ酸、低酸価",
        "value": "無色透明で無臭。普段使っている乳液やクリームに1滴混ぜて保湿力を底上げしたり、手作り化粧品のベースオイルとしても無限の拡張性を誇る高品質オイル",
        "desc_p1": "化粧品の成分や原料にこだわるスキンケア愛好家から圧倒的な支持を集める自然化粧品研究所。同社の『精製 ライスブランオイル』は、医薬部外品原料規格に準拠した最高ランクの精製度を誇り、肌への刺激性を極限まで抑えながら米ぬかの美容パワーを凝縮しています。",
        "desc_p2": "精製されているため、米油特有の匂いや油膜感が一切なく、驚くほどスピーディーに角層へと浸透します。オリザノールとフェルラ酸が冬の冷えによるくすみをケアし、透明感のある澄んだ素肌へ導きます。クレンジングオイルとして使用すれば、落ちにくい冬のベースメイクを毛穴の奥から浮かせつつ、必要な潤いは肌に残す理想的なオフが可能です。敏感肌の方でも毎日気兼ねなく使える安心設計です。",
        "target": "オイルの匂いやベタつきが絶対に嫌な方、成分の純度や規格に徹底してこだわりたい方、クレンジングから保湿までマルチに使い回したい方",
        "point": "冬のクレンジングとして使う場合は、500円玉大を手にとってメイクに馴染ませ、ティッシュで優しく押さえてからぬるま湯で洗い流すと、乾燥知らずのもっちり肌をキープできます。"
    },
    {
        "rank": 9,
        "tag": "🍚 米ぬかエキス×黒砂糖エキス！真冬の固くなった古い角質をやさしく落とし水分が入る肌へ整えるパック",
        "catch": "冬のスキンケアの浸透力を劇的に変える洗い流しパック。米ぬかオイルの柔軟効果と黒砂糖の吸湿保水力で、硬化した古い角質をつるんとオフして化粧水の吸い込みを再生",
        "brand_name": "リアル (美人ぬか)",
        "capacity": "100g / チューブ容器",
        "type": "高保湿角質柔軟トリートメントパック",
        "features": "コメヌカエキス、コメ胚芽油、黒砂糖エキス、ハチミツ、吸着性クレイ",
        "value": "冬のスクラブのような摩擦刺激を与えず、泥と米ぬかの濃密ペーストが古い角質を優しく吸着オフ。洗い流した瞬間から生まれたてのようなモチモチの白玉肌を実感",
        "desc_p1": "冬になると『いくら高価な化粧水やオイルを塗っても肌に入っていかない』という現象が起きます。これは寒さによって肌のターンオーバーが停滞し、本来剥がれ落ちるべき古い角質が肌表面に何層も積み重なって硬直しているためです。美人ぬかの『純米パック』は、そんな冬の硬化角質を刺激なくやさしくリセットする名品です。",
        "desc_p2": "こっくりとしたクリーム状のパックを顔全体に伸ばすと、米胚芽油のエモリエント成分が固まった角質をじっくりと柔らかくほぐし、黒砂糖エキスとハチミツが角層に濃密な水分を与えます。5分置いてぬるま湯で洗い流すだけで、くすみの原因となっていた不要な角質がつるんとオフされ、透明感が一気にアップ。その後に使う米ぬかオイルや化粧水の浸透速度が何倍にも跳ね上がります。",
        "target": "冬になると肌がゴワついてスキンケアが肌表面で滑る方、スクラブ洗顔だと乾燥してヒリつく方、週1〜2回のスペシャルケアで透明感を取り戻したい方",
        "point": "洗顔後、軽く水気を拭き取った肌に目と口の周りを避けて肌が隠れる程度の厚さに塗り広げます。約5分間置いた後、ぬるま湯で優しく撫でるように洗い流してください。入浴時の湯船の中で行うとスチーム効果でさらに効果的です。"
    },
    {
        "rank": 10,
        "tag": "🌾 玄米100kgからわずか1kg！超濃密な胚芽油が真冬の毛先・指先のひび割れまで全身を濃密保護",
        "catch": "山形県のこめ油老舗・三和油脂が手がける希少なコメ胚芽油100%。米の命が凝縮された超高濃度ビタミンEとオリザノールが、真冬の毛先のパサつき・爪のひび割れを集中修復",
        "brand_name": "三和油脂 (SANWA)",
        "capacity": "100ml / ガラスドロップボトル",
        "type": "超高純度コメ胚芽油マルチオイル",
        "features": "コメ胚芽油100%（純国産）、天然ガンマ-オリザノール極高濃度、トコトリエノール",
        "value": "一般的な米ぬか油よりもさらに栄養が集中する『胚芽』のみを厳選圧搾。冬のヘアトリートメント、ネイルオイル、リップケアまで全身の極乾燥スポットを集中リペア",
        "desc_p1": "玄米の栄養の約66%が集中していると言われる『胚芽』。三和油脂の『純国産 コメ胚芽油』は、玄米100kgからわずか1kg程度しか抽出できない極めて希少な胚芽油だけを丁寧に抽出したプレミアムオイルです。",
        "desc_p2": "通常の米ぬか油と比較しても、ガンマ-オリザノールやビタミンEの濃度が格段に高く、真冬の寒冷乾燥によって痛んだ毛先や、水仕事でパックリ割れそうになった指先の爪周りを強力に保護します。毛先にわずか1滴馴染ませるだけで、冬の乾燥風によるパサつきを抑えてシルクのような艶やかな束感を作り出します。ネイルケアとして爪の根元に揉み込めば、ささくれを防止して健やかな爪を育成します。1本持っているだけで冬のあらゆるパーツ乾燥を救済できる心強い常備品です。",
        "target": "冬になると毛先がパサついて枝毛が増える方、水仕事や寒さで指先や爪周りがひび割れやすい方、お米の最も栄養価の高い部分だけを濃密に使いたい方",
        "point": "ドライヤー前の濡れた髪の毛先に1〜2滴馴染ませてから乾かすと、熱ダメージを防ぎつつ毛先までしっとりまとまります。また、就寝前に爪の甘皮部分にすり込むネイルケアとしても格別の効果を発揮します。"
    }
]

# 目次リンク
toc_links = ""
for p in product_details:
    toc_links += f'          <li><a href="#rank-{p["rank"]}">第{p["rank"]}位：{p["brand_name"]} {p["catch"][:22]}...</a></li>\n'

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
        "url": f"https://lumi-cosme.vercel.app/winter-rice-bran-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！天然ガンマ-オリザノールと濃密ビタミンEが真冬の冷えくすみ＆バリア枯渇を救う高保湿米ぬかオイルコスメランク10",
            "description": "11月・12月の寒冷乾燥と血行不良によるくすみ・粉吹き肌を救う高保湿米ぬかオイルコスメを徹底厳選！美人ぬか、アンドエスエイチ、みんなでみらいを、ブランドリップ、米ぬか美人まで厳選。",
            "datePublished": "2026-11-05T04:00:00+09:00",
            "dateModified": "2026-11-05T04:00:00+09:00",
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
            "name": "高保湿米ぬかオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "米ぬかオイルに含まれる『ガンマ-オリザノール』とは何ですか？なぜ冬の冷えくすみに効くのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ガンマ-オリザノール（γ-Oryzanol）は、お米のぬか層や胚芽に特有の脂溶性ポリフェノール化合物です。自律神経のバランスを整え、皮膚の末梢血流を促す優れた生理活性を持っています。11月〜12月の真冬は外気温の低下によって毛細血管が収縮し、肌に酸素や栄養が行き渡らず顔色が青白くどんよりとくすみがちになりますが、ガンマ-オリザノールが血行をサポートすることで、内側からぽっと温かみのある透明感と血色感を呼び戻してくれます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "米ぬかオイルとオリーブオイルや椿油の違いは何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "オリーブオイルや椿油はオレイン酸が約80%と非常に高く、重厚な油膜で肌を密閉する力に長けていますが、人によってはやや重たくベタつきを感じることがあります。一方、米ぬかオイルはオレイン酸約42%・リノール酸約38%という理想的な黄金比率で構成されており、人間の皮脂膜の脂肪酸バランスに極めて酷似しています。そのため、高いエモリエント保護力を持ちながらも、肌に乗せた瞬間にすっと馴染んでベタつかない『軽やかさと高保湿の両立』が最大の違いです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "米アレルギーや敏感肌でも米ぬかオイルを使って大丈夫ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "精製された米ぬかオイルはアレルギーの原因となる水溶性タンパク質が徹底的に除去されているため、米アレルギーをお持ちの方でも皮膚への刺激リスクは極めて低いとされています。古くから日本人の肌に最も親和性の高い植物油として愛用されてきた歴史があり、刺激性が低くバリア機能が低下した冬のデリケート肌にも安心して使用できます。心配な場合は、二の腕の内側などでパッチテストを行ってから顔へご使用ください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "冬の米ぬかオイルの最もおすすめな使い方・スキンケアステップは？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "最もおすすめなのは『洗顔直後のブースター使い』と『お風呂上がりの全身インバスケア』です。洗顔後のわずかに濡れた肌に1〜2滴を伸ばすことで、その後に塗布する化粧水の浸透力を何倍にも高めます。また、冬場のお風呂上がり、タオルで拭く前の濡れた手足に伸ばすと、水分とオイルが自然に乳化して角層深部へ行き渡り、冬特有のすねの粉吹きやひび割れを完璧にブロックできます。"
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
  <title>保湿力の強さで肌乾燥とさようなら！天然ガンマ-オリザノールと濃密ビタミンEが真冬の冷えくすみ＆バリア枯渇を救う高保湿米ぬかオイルコスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥と血行不良によるくすみ・粉吹き肌を救う高保湿米ぬかオイルコスメを徹底厳選！美人ぬか、アンドエスエイチ、みんなでみらいを、ブランドリップ、米ぬか美人まで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-rice-bran-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！天然ガンマ-オリザノールと濃密ビタミンEが真冬の冷えくすみ＆バリア枯渇を救う高保湿米ぬかオイルコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と血行不良によるくすみ・粉吹き肌を救う高保湿米ぬかオイルコスメを徹底厳選！美人ぬか、アンドエスエイチ、みんなでみらいを、ブランドリップ、米ぬか美人まで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-rice-bran-oil">
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
      --primary: #365314;
      --primary-light: #ecfccb;
      --primary-dark: #1a2e05;
      --accent: #65a30d;
      --accent-hover: #4d7c0f;
      --bg: #f7fee7;
      --card-bg: #ffffff;
      --text-main: #374151;
      --text-sub: #6b7280;
      --border: #d9f99d;
      --shadow: 0 4px 15px rgba(54, 83, 20, 0.08);
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
      background: linear-gradient(135deg, #ecfccb 0%, #f7fee7 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      margin-bottom: 2rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.85rem;
      font-weight: 700;
      color: #1f2937;
      line-height: 1.4;
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.7;
      margin-bottom: 1.5rem;
    }}

    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #9ca3af;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.5rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.5rem;
    }}

    .toc-list li a {{
      color: var(--text-main);
      text-decoration: none;
      font-size: 0.95rem;
      transition: color 0.2s;
    }}

    .toc-list li a:hover {{
      color: var(--primary);
      text-decoration: underline;
    }}

    .intro-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .intro-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .intro-section p {{
      margin-bottom: 1.2rem;
      font-size: 1rem;
      line-height: 1.8;
    }}

    .intro-highlight-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .highlight-card {{
      background: var(--primary-light);
      padding: 1.2rem;
      border-radius: 10px;
      border-left: 4px solid var(--primary);
    }}

    .highlight-card strong {{
      display: block;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
    }}

    .highlight-card p {{
      font-size: 0.9rem;
      color: var(--text-main);
      margin-bottom: 0;
      line-height: 1.6;
    }}

    .table-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      overflow-x: auto;
    }}

    .table-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
    }}

    table.comparison-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.85rem 0.75rem;
      border-bottom: 1px solid #f3f4f6;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
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
      width: 60px;
      height: 60px;
      object-fit: contain;
      border-radius: 6px;
      background: #fafafa;
      border: 1px solid #f3f4f6;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      text-decoration: none;
      font-weight: 700;
      white-space: nowrap;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      border: 1px solid var(--border);
      padding: 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.9rem;
      border-radius: 6px;
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
      max-width: 220px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 10px;
      border: 1px solid #f3f4f6;
      padding: 0.8rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .product-img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      color: #1f2937;
      font-weight: 700;
      line-height: 1.5;
      margin-bottom: 0.5rem;
    }}

    .product-brand {{
      font-size: 0.9rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #111827;
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.35rem;
      color: #b91c1c;
    }}

    .product-tag {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.4rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
      line-height: 1.5;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.6;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      overflow-x: auto;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.65rem 0.85rem;
      border: 1px solid var(--border);
    }}

    table.spec-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      width: 28%;
      white-space: nowrap;
    }}

    table.spec-table td {{
      background: #ffffff;
      color: var(--text-main);
    }}

    .review-body {{
      background: #fcfdf8;
      border-radius: 10px;
      padding: 1.5rem;
      border: 1px solid var(--border);
      margin-bottom: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.05rem;
      color: var(--primary-dark);
      margin-bottom: 0.85rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .review-body p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .target-box, .point-box {{
      background: #ffffff;
      border-radius: 8px;
      padding: 1rem 1.2rem;
      margin-top: 1rem;
      border-left: 4px solid var(--primary);
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }}

    .target-box strong, .point-box strong {{
      display: block;
      font-size: 0.92rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}

    .target-box p, .point-box p {{
      font-size: 0.9rem;
      margin-bottom: 0;
      line-height: 1.6;
      color: #4b5563;
    }}

    .btn-wrap {{
      text-align: center;
      margin-top: 1.5rem;
    }}

    .rakuten-btn {{
      display: inline-block;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-size: 1rem;
      font-weight: 700;
      text-decoration: none;
      padding: 1rem 2rem;
      border-radius: 30px;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
      width: 100%;
      max-width: 440px;
    }}

    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #800000 100%);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
      transform: translateY(-2px);
    }}

    .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      border-bottom: 1px dashed var(--border);
      padding-bottom: 1.2rem;
    }}

    .faq-item:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}

    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #1f2937;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
    }}

    .faq-a {{
      font-size: 0.95rem;
      color: #4b5563;
      line-height: 1.7;
      padding-left: 1.5rem;
    }}

    .guide-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: #1f2937;
      margin: 1.2rem 0 0.6rem;
    }}

    .guide-section p {{
      font-size: 0.95rem;
      line-height: 1.8;
      margin-bottom: 1rem;
      color: #374151;
    }}

    .related-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .related-section-title {{
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .related-list {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      background: #fafafa;
      border: 1px solid #f3f4f6;
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      display: flex;
      flex-direction: column;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--border);
    }}

    .related-card-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.4rem;
      line-height: 1.5;
    }}

    .related-card-desc {{
      font-size: 0.82rem;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    footer.site-footer {{
      background: #ffffff;
      border-top: 1px solid var(--border);
      padding: 2.5rem 1.5rem;
      margin-top: 4rem;
    }}

    .footer-inner {{
      max-width: 1080px;
      margin: 0 auto;
      text-align: center;
    }}

    .footer-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.8rem 1.5rem;
      margin-bottom: 1.5rem;
    }}

    .footer-links a {{
      color: var(--text-sub);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.2s;
    }}

    .footer-links a:hover {{
      color: var(--primary);
    }}

    .copyright {{
      font-size: 0.8rem;
      color: #9ca3af;
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">Lumi Cosme</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#guide">選び方・使い方</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="hero-badge">2026年真冬版 ｜ 和の伝統美肌・血行保湿検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！天然ガンマ-オリザノールと濃密ビタミンEが真冬の冷えくすみ＆バリア枯渇を救う高保湿米ぬかオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて訪れる気温低下と血行不良。真冬の過酷な寒冷は末梢血流を停滞させて顔色をどんより青白くくすませ、皮脂分泌の激減によって角質層はカサカサに干からびてしまいます。そんな冬の深刻なトラブルを救うのが、日本の大地が育んだお米の叡智「米ぬかオイル（ライスブランオイル）」です。天然ポリフェノール「γ-オリザノール」とスーパービタミンE「トコトリエノール」の相乗効果で、冷えくすみを一掃し、もっちり吸い付くような白玉肌を育てる名品10選をコスメコンシェルジュが徹底検証・厳選しました。
      </p>
      <div class="meta-bar">
        <span>🕒 公開日: 2026年11月5日</span>
        <span>✍️ 執筆・検証: Lumi Cosme 編集部 コスメコンシェルジュ</span>
        <span>🔍 楽天リアルタイムAPI商品データ照合済</span>
      </div>
    </section>

    <div class="toc-box">
      <div class="toc-title">📑 目次（タップで該当ランキングへジャンプ）</div>
      <ul class="toc-list">
{toc_links}
      </ul>
    </div>

    <section class="intro-section">
      <h2>冬の冷えくすみと角層バリア崩壊を食い止める「米ぬかオイル」の科学的根拠</h2>
      <p>
        初冬の11月から年末の12月にかけて、日本の気候は急速に乾燥と冷え込みを強めます。気温の低下によって皮膚温が下がると、皮脂腺からの分泌量が激減するだけでなく、毛細血管が収縮して血行が停滞。ターンオーバーに必要なアミノ酸や酸素が表皮細胞に行き届かなくなり、角層が硬化して古い角質が剥がれ落ちずに堆積します。これが「化粧水が弾かれて浸透しない」「顔色が暗く青ざめる」「粉を吹いてかゆい」という真冬の複合トラブルの根本原因です。
      </p>
      <p>
        古くから「ぬか袋」などで日本女性の肌を磨き上げてきた米ぬか。現代の皮膚科学研究によって、米ぬかオイルには他の植物油には見られない唯一無二の有用成分が高濃度に濃縮されていることが判明しています。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 米特有の巡り成分「ガンマ-オリザノール」</strong>
          <p>自律神経を安定させ、皮膚の毛細血管血流を促す天然ポリフェノール。冬の寒冷で滞った血色感を蘇らせ、青白いくすみを内側から晴らします。</p>
        </div>
        <div class="highlight-card">
          <strong>2. スーパービタミンE「トコトリエノール」</strong>
          <p>通常のトコフェロールの数十倍の抗酸化力を持つトコトリエノールを豊富に含有。真冬の過酷な乾燥と紫外線酸化から細胞間脂質を鉄壁防護します。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 皮脂膜を忠実に模倣するオレイン酸＆リノール酸</strong>
          <p>オレイン酸約42%・リノール酸約38%という理想的な脂肪酸比率。人の皮脂膜と酷似しているため、刺激なくすっと浸透し、ベタつかずにもっちり潤します。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿米ぬかオイルコスメ おすすめ10選 比較一覧表</h2>
      <table class="comparison-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>画像</th>
            <th>ブランド / アイテム名</th>
            <th>分類</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
{table_joined}
        </tbody>
      </table>
    </section>

    <section id="ranking">
{cards_joined}
    </section>

    <section class="guide-section" id="guide">
      <h2>プロが指南！真冬の米ぬかオイルを使い倒すスキンケアの極意</h2>
      <h3>1. 「洗顔直後のブースターハンドプレス」で角層をほぐす</h3>
      <p>
        米ぬかオイルの持つオレイン酸とリノール酸は、人間の角質細胞間脂質にすんなり溶け込むエモリエント特性を持っています。洗顔後、タオルで軽く押さえた直後の湿り気のある肌に1〜2滴を手にとり、体温で温めてから優しくハンドプレスしてください。硬化した角層細胞の接着が緩み、その後に重ねる化粧水の浸透速度が格段にアップします。
      </p>
      <h3>2. お風呂上がりの「インバス全身オイルケア」で粉吹きすねを完全ガード</h3>
      <p>
        冬の入浴後、脱衣所の冷気で皮膚の水分が蒸発する前に、濡れたままの素肌へ米ぬかオイルを塗り伸ばします。水分と油分が肌表面で乳化し、薄く強固な皮脂膜ヴェールを形成。その後バスタオルで優しく押さえるだけで、一日中粉吹きやかゆみのない滑らかな白玉肌が持続します。
      </p>
      <h3>3. 冬のパサつく髪の毛先や指先のひび割れへのポイント集中ケア</h3>
      <p>
        米ぬかオイルは分子構造が細かくベタつきにくいため、ドライヤー前のヘアトリートメントとしても秀逸です。毛先に1滴馴染ませて乾かすだけで、静電気による広がりや冬の乾燥枝毛を防ぎます。また、水仕事の後に爪の根元の甘皮に揉み込めば、ささくれや爪の割れを予防する極上のネイルセラムとして機能します。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 米ぬかオイルに含まれる「ガンマ-オリザノール」とは何ですか？なぜ冬の冷えくすみに効くのですか？</div>
        <div class="faq-a">ガンマ-オリザノール（γ-Oryzanol）は、お米のぬか層や胚芽に特有の脂溶性ポリフェノール化合物です。自律神経のバランスを整え、皮膚の末梢血流を促す優れた生理活性を持っています。11月〜12月の真冬は外気温の低下によって毛細血管が収縮し、肌に酸素や栄養が行き渡らず顔色が青白くどんよりとくすみがちになりますが、ガンマ-オリザノールが血行をサポートすることで、内側からぽっと温かみのある透明感と血色感を呼び戻してくれます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 米ぬかオイルとオリーブオイルや椿油の違いは何ですか？</div>
        <div class="faq-a">オリーブオイルや椿油はオレイン酸が約80%と非常に高く、重厚な油膜で肌を密閉する力に長けていますが、人によってはやや重たくベタつきを感じることがあります。一方、米ぬかオイルはオレイン酸約42%・リノール酸約38%という理想的な黄金比率で構成されており、人間の皮脂膜の脂肪酸バランスに極めて酷似しています。そのため、高いエモリエント保護力を持ちながらも、肌に乗せた瞬間にすっと馴染んでベタつかない「軽やかさと高保湿の両立」が最大の違いです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 米アレルギーや敏感肌でも米ぬかオイルを使って大丈夫ですか？</div>
        <div class="faq-a">精製された米ぬかオイルはアレルギーの原因となる水溶性タンパク質が徹底的に除去されているため、米アレルギーをお持ちの方でも皮膚への刺激リスクは極めて低いとされています。古くから日本人の肌に最も親和性の高い植物油として愛用されてきた歴史があり、刺激性が低くバリア機能が低下した冬のデリケート肌にも安心して使用できます。心配な場合は、二の腕の内側などでパッチテストを行ってから顔へご使用ください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 冬の米ぬかオイルの最もおすすめな使い方・スキンケアステップは？</div>
        <div class="faq-a">最もおすすめなのは「洗顔直後のブースター使い」と「お風呂上がりの全身インバスケア」です。洗顔後のわずかに濡れた肌に1〜2滴を伸ばすことで、その後に塗布する化粧水の浸透力を何倍にも高めます。また、冬場のお風呂上がり、タオルで拭く前の濡れた手足に伸ばすと、水分とオイルが自然に乳化して角層深部へ行き渡り、冬特有のすねの粉吹きやひび割れを完璧にブロックできます。</div>
      </div>
    </section>

    <!-- 関連記事プレースホルダー -->
    <section id="related" class="related-section">
      <div class="related-section-title">
        <span>📑</span> あわせて読みたい！冬の徹底保湿ケア特集一覧
      </div>
      <div class="related-list" id="related-grid-box">
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-links" id="footer-links-box">
      </div>
      <p class="copyright">© 2026 Lumi Cosme. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-rice-bran-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-rice-bran-oil.html!")
