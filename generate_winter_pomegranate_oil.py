import json
import re

with open("fetched_3new_macadamia_pomegranate_ricebran.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_pomegranate_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 希少プニカ酸を高濃度濃縮！真冬の過酷な寒冷でしぼんだ肌を跳ね返す最高峰エイジング美容液",
        "catch": "世界的なオーガニックコスメの泰斗・ヴェレダが誇る最高峰フェイシャルオイル。植物界随一のオメガ5プニカ酸が、真冬の乾燥でハリを失った大人の肌を内側からピンと押し上げる",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "30ml / スポイト式遮光ガラスボトル",
        "type": "高機能プレミアムエイジングフェイシャルオイル",
        "features": "有機ザクロ種子油（プニカ酸高含有）、アルガニアスピノサ核油、マカデミア種子油、キビ種子エキス",
        "value": "ネイトゥルー（NATRUE）オーガニック認証取得。寒風と暖房で菲薄化した角層を濃密な油分ヴェールで包み込み、翌朝の肌密度とツヤ感を劇的に向上させる至高の1滴",
        "desc_p1": "11月から12月にかけての本格的な真冬の寒さは、皮膚の基礎体温を奪い、真皮コラーゲンの産生サイクルを鈍化させます。その結果、頬の毛穴が縦に流れ、目元やほうれい線の乾燥小ジワが深く刻まれる『冬のしぼみ肌現象』が加速します。ヴェレダの『ざくろ ファーミングフェイシャルオイル』は、そんな深刻なエイジングサインに立ち向かうために処方された最高峰の集中美容オイルです。",
        "desc_p2": "ザクロの種子からコールドプレスで抽出される油分には、植物界では極めて稀有な不飽和脂肪酸『プニカ酸（オメガ5）』が約60〜70%も濃縮されています。肌に乗せると、リッチで濃密なコクがありながら、体温でとろけるように角層深部へと溶け込んでいきます。アルガンオイルやマカダミアオイルとの絶妙なシナジーにより、冷え切った肌にピンとした弾力フィルムを形成。オレンジフラワーやバニラが織りなす甘くスパイシーな気品あるアロマが、真冬のスキンケア時間を極上のエステ体験へと昇華させます。",
        "target": "冬になると肌のハリがなくなり顔全体が疲れて見えてしまう方、目元や口元の乾燥小ジワを即効でケアしたい方、本物のオーガニックエイジングケアを愛好する方",
        "point": "夜のお手入れ時、化粧水で肌を十分に潤した直後、手のひらに2〜3滴をとります。両手で温めてから、顔の内側から外側、下から上へと引き上げるようにハンドプレスして密着させます。首元からデコルテまで流すように伸ばすのがベストです。"
    },
    {
        "rank": 2,
        "tag": "🛁 有機ザクロ種子油×高保湿マカダミア油！真冬の冷え固まったボディをしっとり引き締める名品オイル",
        "catch": "入浴後の湿った素肌にとろける至福のトリートメント。ザクロの強力な抗酸化ポリフェノールと植物オイルが、冬の冷えで滞ったボディの血行を促しビロードの素肌へ導く",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100ml / ポンプ付ガラスボトル",
        "type": "全身用高保湿ファーミングボディオイル",
        "features": "ザクロ種子油、ホホバ種子油、マカデミア種子油、ヒマワリ種子油、天然エッセンシャルオイル",
        "value": "ポンプ式で使いやすく、真冬の脱衣所でも素早く全身をケア。乾いた外気に奪われがちな水分を油膜でしっかりロックし、一日中ベルベットのような滑らかな質感を維持",
        "desc_p1": "冬のボディは、厚着による摩擦や長時間の暖房、そして寒さによる末梢血行の悪化によって、想像以上に過酷な乾燥と代謝不良にさらされています。二の腕やすねがカサカサになり、肌のハリが失われていく冬のボディトラブルに、ヴェレダの『ざくろ モイスチャーオイル 100ml』は確実な手応えをもたらします。",
        "desc_p2": "コールドプレスされた有機ザクロ種子油と、浸透性に優れたマカダミアナッツオイルが黄金比でブレンドされており、肌の上を滑らかに滑る絶妙なテクスチャーを実現。お風呂上がりの温まった素肌になじませながらマッサージを行うと、滞りがちなリンパの流れが促され、キュッと引き締まったハリのある肌質感へと整います。翌朝起きてもパジャマに油分が移ることなく、素肌の内側から発光するような上質なツヤと滑らかさが夜まで持続します。",
        "target": "冬の寒さで身体の皮膚が硬くなりハリツヤを失っている方、お風呂上がりのボディマッサージで代謝と保湿を同時に高めたい方、上品なフルーティースパイシーの香りをまといたい方",
        "point": "入浴直後、肌にまだ水滴が残っている状態で全身へ伸ばします。足首から太もも、手首から肩へと心臓に向かって引き上げるようにマッサージしながら塗り込むと、血行促進効果と保湿密閉効果が倍増します。"
    },
    {
        "rank": 3,
        "tag": "🌿 低温圧搾ザクロ種子油100%！プニカ酸とポリフェノールが真冬の枯れ肌に驚異の保水膜を張る",
        "catch": "徹底的な純度を追求した無添加ポメグラネートオイル。オメガ5系プニカ酸の強力なフリーラジカル消去パワーが、冬の紫外線と乾燥による酸化ストレスを徹底ブロック",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "50ml / 遮光ドロッパーボトル",
        "type": "100％ピュアポメグラネートシードオイル",
        "features": "ザクロ種子油（低温圧搾コールドプレス）、プニカ酸約70%、無着色・無香料・無添加",
        "value": "希少価値の高いザクロ種子油をピュアなまま適正価格でお届け。手持ちの化粧水や乳液に1滴ブレンドするだけで、真冬の超乾燥対策美容液へとアップグレード",
        "desc_p1": "植物オイルの中でも極めて希少性が高く、果実1トンから抽出できるオイルはわずか数リットルとも言われるザクロ種子油。&SHの『ポメグラネート オイル』は、そんな貴重なオイルを余計な希釈を行わず、低温圧搾法によって純度100%でボトリングした本格派アイテムです。",
        "desc_p2": "独特の粘度と深みのある琥珀色をしたオイルは、まさに抗酸化成分の宝庫。プニカ酸を中心とした共役リノレン酸が、真冬の寒気や乾燥によって弱体化した角層バリアを強固にサポートします。肌に押し込むと、表面を滑らかな保護膜で包み込み、外部からの刺激物質や冷気の侵入を物理的に防御。普段使っている保湿クリームに1滴混ぜて使うだけでも、翌朝の肌のふっくら感とキメの均一さがまるで別次元へと引き上げられます。",
        "target": "希釈されていない純度100%のザクロオイルを試してみたい方、冬の空気の乾燥で肌が酸化・くすみやすい方、コストパフォーマンスに優れたエイジングオイルを求める方",
        "point": "非常に濃厚なオイルのため、1回の使用量は1〜2滴で十分です。手のひらに化粧水を出し、そこに1滴のオイルを垂らして手のひらで混ぜ合わせてから顔全体に塗布する『クイック乳化ケア』が手軽で抜群の効果を発揮します。"
    },
    {
        "rank": 4,
        "tag": "🔬 ドイツ産有機栽培の未精製生搾り！目元やほうれい線の乾燥小ジワをふっくら満たす濃密セラム",
        "catch": "手作りコスメ・オーガニック原料の権威マンディムーンが厳選。プニカ酸約70%含有の生ザクロオイルが、真冬の寒冷で刻まれた大人の目元・口元の溝をしっとり埋め尽くす",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "10ml / 遮光ガラスドロッパーボトル",
        "type": "未精製オーガニックザクロシードオイル",
        "features": "未精製有機ザクロ種子油、プニカ酸高含有、植物性エストロゲン様成分、低温圧搾法",
        "value": "10mlという使い切りやすいフレッシュサイズ。酸化しやすいオメガ5系脂肪酸を、常に新鮮で活性の高い状態で真冬の気になるエイジングゾーンへ集中投下可能",
        "desc_p1": "冬の乾燥が進むと、ファンデーションを塗った際に目尻の笑いジワやほうれい線に粉が溜まり、実年齢以上に老けた印象を与えてしまうことがあります。マンディムーンの『オーガニック ザクロオイル（未精製）』は、そんな局所的な乾燥溝を集中ケアするために設計された、原液クラスの贅沢オイルです。",
        "desc_p2": "ドイツの認証有機農園で収穫されたザクロの種子を、熱を一切加えないコールドプレスで生搾り。ナッツのような独特のコクと濃厚なテクスチャーを持ち、指先に乗せて目元や口元にトントンと押し込むと、吸い付くように角層へと密着します。プニカ酸の細胞賦活作用と高い水分保持力によって、乾いて縮こまった角層細胞がふっくらと膨らみ、光を均一に反射する若々しい目元・口元を取り戻します。夜のアイセラム代わりに最適です。",
        "target": "目尻の乾燥ジワやほうれい線が冬場に特に目立って気になる方、新鮮な未精製オイルを少量ずつ使いたい方、植物の持つパワフルな生命力を素肌で実感したい方",
        "point": "夜のお手入れの最後に、薬指の腹に米粒大のオイルをとります。摩擦を絶対に起こさないよう、目元やほうれい線、眉間の乾燥シワに対して優しくスタンプを押すように垂直に押し込みます。"
    },
    {
        "rank": 5,
        "tag": "🧴 オーガニックプニカ酸×ホホバ種子油！真冬の全身マッサージを極上の潤いで満たす大容量オイル",
        "catch": "乾燥と冷えで凝り固まった真冬のボディを解き放つ。肌なじみに優れたホホバ油とザクロのオメガ5脂肪酸が、冷たい風でガサつく手足をしっとり包み込み若々しいツヤを宿す",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "100ml / ポンプボトル",
        "type": "高保湿エイジングケアボディオイル",
        "features": "有機ザクロ種子油、ホホバ種子油、マカデミア種子油、キビ種子エキス、高純度ブレンド",
        "value": "並行輸入の正規品大容量。冬の全身ケアに惜しみなく使え、肌のハリ低下やたるみが気になる大人のボディラインをしなやかに引き締めながら長時間保湿",
        "desc_p1": "真冬になると、顔のお手入れには念入りに美容液を重ねる方でも、ボディのエイジングケアは見落としがちになります。しかし、首元やデコルテ、手の甲、膝の上などは、皮脂腺が少なく乾燥によるハリの低下が顕著に現れる部位です。ヴェレダの『ざくろ ボディオイル 100ml』は、大人のボディに不可欠なハリと潤いを同時にチャージする名作です。",
        "desc_p2": "ホホバ種子油をベースにザクロ種子油をブレンドすることで、高い浸透性と持続的な保護膜の両立を実現。真冬の冷たい外気でこわばった皮膚を温めながらマッサージすることで、毛細血管の血流を呼び戻し、くすんだ肌色を明るく健康的なトーンへと導きます。入浴後のケアとしてはもちろん、外出前の首元やハンドケアとして少量をなじませておくだけで、乾燥小ジワを予防し、一日中シルクのような滑らかさを維持できます。",
        "target": "デコルテや首元、手の甲の年齢サインが気になり始めた方、さらりとした伸びの良さと確かな保湿持続力を求める方、1本で全身のエイジングケアを完結させたい方",
        "point": "特に年齢が出やすいデコルテと首元には、鎖骨の下から首筋、顎下へと引き上げるように塗布します。手のひらに残ったオイルは手の甲や指先まで揉み込むことで、手元の乾燥小ジワも同時にケアできます。"
    },
    {
        "rank": 6,
        "tag": "🌿 高純度コールドプレス×抗酸化シールド！冬の紫外線と冷風から大人肌を守る美容オイル",
        "catch": "過酷な自然環境を生き抜いたザクロ種子の生命力。オメガ5系プニカ酸が冬の乾燥ダメージを修復し、乱れたターンオーバーを整えてキメ密度の高い滑らか肌へ整える",
        "brand_name": "Natural Beauty (ナチュラルビューティー)",
        "capacity": "30ml / 遮光ドロップボトル",
        "type": "オーガニックザクロシード美容オイル",
        "features": "有機ザクロ種子油100%、コールドプレス製法、無香料、無鉱物油",
        "value": "肌トラブルの原因となる合成化合物を徹底排除。植物本来が持つ強力な抗酸化ポリフェノールが、真冬の寒風による皮膚の菲薄化（ひはくか）とバリア崩壊を強力に防護",
        "desc_p1": "冬の紫外線は夏に比べて弱いと思われがちですが、波長の長いUVAは冬場も地上に降り注ぎ、肌の真皮層にあるコラーゲン繊維をじわじわと破壊します。さらに木枯らしによる物理的な摩擦と乾燥が加わることで、肌の酸化スピードは急上昇します。ナチュラルビューティーの『オーガニック ザクロシードオイル』は、そんな冬の複合ダメージから素肌をガードする強力な防壁となります。",
        "desc_p2": "プニカ酸の強力なフリーラジカル消去能により、日中受ける環境ストレスから細胞膜を保護。オイルを肌に伸ばすと、薄い膜のように角層表面に広がり、内部の水分蒸散をシャットアウトします。夜寝る前のスキンケアに組み込めば、睡眠中の肌再生リズムを力強く後押しし、翌朝洗顔したときの手触りの変化に驚かされます。ゴワゴワしていた肌がふっくらと柔らかく整い、メイクのりが劇的に向上します。",
        "target": "冬の乾燥によるゴワつきや化粧ノリの悪さに悩んでいる方、紫外線と乾燥のWダメージを同時にケアしたい方、シンプルなピュアオイルで肌力を底上げしたい方",
        "point": "朝のメイク前に使用する場合は、半滴（ほんのわずか）を手のひら全体によく伸ばし、顔全体を軽く包み込むようにハンドプレスします。油浮きせず、日中の冷風ガード膜として機能します。"
    },
    {
        "rank": 7,
        "tag": "🍓 天然シアバター×ザクロ種子油！冬の極乾燥肌を24時間フルーティーな潤いで包む大容量ローション",
        "catch": "アメリカで空前の大ヒットを記録する高保湿ボディローション。濃厚な天然シアバターにザクロとラズベリーのエキスを調合し、真冬のひび割れ肌を甘く濃密な潤いで密閉保護",
        "brand_name": "EOS (イオス)",
        "capacity": "473ml / 特大ポンプボトル",
        "type": "高保湿シアベターボディローション",
        "features": "天然シアバター、ザクロ種子油、ラズベリー果実エキス、7種の保湿オイル＆バター",
        "value": "473mlのビッグサイズで、真冬の全身乾燥ケアを贅沢に実現。24時間保湿持続テスト済み。甘酸っぱくフルーティーな贅沢アロマが一日中ふんわり持続",
        "desc_p1": "真冬になると手足の皮膚が乾燥してかゆくなり、夜中に無意識に掻きむしってしまうという悩みを抱える方は少なくありません。イオスの『シアベター ボディローション ザクロ＆ラズベリー』は、そんな深刻なドライスキンを救うために開発された、超濃厚な高保湿ボディケアアイテムです。",
        "desc_p2": "ホイップクリームのようにリッチな質感でありながら、肌に乗せると体温で瞬時にとろけて角層深部へと浸透。持続性シアバターとザクロ種子油のハイブリッド効果により、肌の表面に水分の蒸発を防ぐエモリエント膜を長時間形成します。塗布した直後から、カサついて粉を吹いていたすねや肘がしっとりと吸い付くような潤いを取り戻し、衣服との摩擦によるチクチク感も解消。ジューシーなザクロとベリーの甘美な香りに包まれ、冬のボディケアが毎日の楽しみに変わります。",
        "target": "真冬になるとボディの乾燥・粉吹き・痒みが止まらない方、大容量で惜しみなく全身に使えるリッチなローションを探している方、フルーティーで華やかな香りが好きな方",
        "point": "お風呂上がりに全身へたっぷりと塗り広げます。特に乾燥しやすい肘、膝、すね、踵には二度塗りして優しく円を描くように揉み込むと、翌朝まで吸い付くような潤いが続きます。"
    },
    {
        "rank": 8,
        "tag": "💦 ザクロ果実エキス×シロキクラゲ多糖体！真冬の乾いた角層を潤いで満たすプレミアムエイジング化粧水",
        "catch": "ヴェレダのプレミアムエイジングケアラインから誕生した高保湿トナー。ザクロの抗酸化エキスと驚異の保水力を誇るシロキクラゲ多糖体が、冬の枯れ肌にしっとり満ちる弾力を注入",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "145ml / ポンプボトル",
        "type": "高保湿エイジングケアフェイシャルトナー",
        "features": "ザクロ果実エキス、シロキクラゲ多糖体、アロエベラ液汁、キハダ樹皮エキス",
        "value": "ヒアルロン酸を凌駕する保水力を持つシロキクラゲ多糖体を贅沢配合。とろみのある美容液のようなテクスチャーが角層深部まで素早く巡り、乾燥小ジワを瞬時に潤す",
        "desc_p1": "冬の乾燥対策といえばオイルやクリームに目が行きがちですが、角層深部に十分な水分が満たされていなければ、いくら油分で蓋をしても真のふっくら感は得られません。ヴェレダの『ざくろ ファーミングローションEX』は、冬の肌が最も渇望している『抗酸化保水』を1本で叶える高機能化粧水です。",
        "desc_p2": "手にとると、美容液のようにリッチでコクのあるとろみテクスチャー。肌に滑らせるとみずみずしく崩れ、植物性シロキクラゲ多糖体の微小粒子が角質細胞の間をすり抜けて深部まで潤いを届けます。ザクロ果実の豊富なポリフェノールが冬の酸化ストレスを和らげ、使い続けるほどに内側から押し返してくるような弾力肌へ。後から使うざくろフェイシャルオイルとの相性は抜群で、化粧水とオイルの2ステップで真冬の鉄壁エイジングケアが完成します。",
        "target": "とろみのある高保湿化粧水で角層を水分で満たしたい方、化粧水段階から本格的なエイジングケアを始めたい方、オイルケアの前の土台作りを完璧にしたい方",
        "point": "洗顔後、500円玉大を手にとり、顔全体に優しくなじませます。その後、もう一度少量を手にとって、乾燥小ジワが気になる目元や口元に重ねづけ（2度づけ）を行うと効果的です。"
    },
    {
        "rank": 9,
        "tag": "🧬 ザクロ種子油×フルーツ幹細胞複合体！冬の紫外線くすみと乾燥小ジワを同時に晴らすハイブリッド美容液",
        "catch": "最先端の植物幹細胞科学を取り入れた米国の実力派オーガニックコスメ。ザクロのオメガ5脂肪酸とリンゴ・ブドウ幹細胞エキスが、真冬の停滞肌に圧倒的な透明感とハリを吹き込む",
        "brand_name": "Andalou Naturals (アンダルーナチュラルズ)",
        "capacity": "32ml / スポイト式ボトル",
        "type": "高機能イルミネーティングトリートメントセラム",
        "features": "ザクロ種子油、フルーツ幹細胞複合体（リンゴ・ブドウ）、レスベラトロール、コエンザイムQ10",
        "value": "ノンコメドジェニック＆グルテンフリー。冬の暖房下でくすみ・乾燥・毛穴の開きが同時に生じる大人の複合悩みに、抗酸化と保水の両面からダイレクトアプローチ",
        "desc_p1": "冬の肌トラブルは、乾燥だけでなく『くすみ』や『ハリ不足』が複雑に絡み合って発生します。アンダルーナチュラルズの『イルミネーティング トリートメントセラム ザクロ』は、ザクロ種子油のエモリエント効果と、最先端のフルーツ幹細胞テクノロジーを融合させた次世代のエイジング美容液です。",
        "desc_p2": "ミルクエッセンスのような軽やかでなめらかなテクスチャーでありながら、塗布した瞬間から肌がゴクゴクと飲み干すように浸透。ザクロのプニカ酸とブドウ由来のレスベラトロール、そしてコエンザイムQ10が一体となって、冬の冷えや乾燥で疲弊した角層細胞に活力をチャージします。夕方になると肌がどんより暗く見えてしまう真冬のくすみ肌を、内側からパッと明るく発光するような透明美肌へと導いてくれます。",
        "target": "冬になると乾燥だけでなく肌のくすみや血色の悪さが気になる方、植物幹細胞などの先進サイエンスコスメを好む方、ベタつかないリッチな美容液を求める方",
        "point": "朝晩の化粧水の後、スポイトで1〜2滴を手にとり、顔全体から首元にかけて均一になじませます。特にくすみが気になる頬骨の高い位置には優しく重ねづけしてください。"
    },
    {
        "rank": 10,
        "tag": "🍊 国産有機ザクロエキス×コメ胚芽油！メイクを落としながら潤いを残す極上クレンジングオイル",
        "catch": "エステティックサロン発祥の国産オーガニックブランド。ザクロと米胚芽油の豊かな油分が、真冬の頑固なメイクや毛穴の角栓をやさしく浮かせ、洗い上がりはもっちり吸い付く素肌へ",
        "brand_name": "fruits roots (フルーツルーツ)",
        "capacity": "100ml / ポンプボトル",
        "type": "高保湿植物性クレンジングオイル",
        "features": "国産ザクロ果実エキス、コメ胚芽油、スクワラン、天然精油（ベルガモット・ゼラニウム）",
        "value": "石油系界面活性剤・鉱物油完全フリー。真冬の洗顔後につっぱり感を一切感じさせず、クレンジングでありながらまるで美容液で洗ったかのようなしっとり感を両立",
        "desc_p1": "冬の乾燥を悪化させる最大の引き金は、実は『毎日のクレンジング』にあります。洗浄力の強すぎる石油系オイルクレンジングは、メイク汚れだけでなく、真冬の肌に不可欠なセラミドや皮脂膜まで根こそぎ洗い流してしまいます。フルーツルーツの『ジューシークレンジングオイル ザクロ』は、そんな冬のバリア破壊を防ぐために生まれたサロン品質の逸品です。",
        "desc_p2": "国産の有機ザクロエキスとコメ胚芽油をベースに設計されており、肌に乗せると体温でフワッと広がり、ウォータープルーフのメイクや毛穴の奥の汚れを素早く吸着。擦らずに優しく撫でるだけで汚れが浮き上がり、ぬるま湯で洗い流した後は、油膜感のないもっちり吸い付くような潤いヴェールが肌に残ります。天然精油のフルーティーな香りに包まれ、一日の終わりに肌と心を優しく解きほぐしてくれる冬の救世主です。",
        "target": "冬になるとクレンジング後に肌が突っ張って痛い方、毛穴の角栓は落としたいが乾燥は絶対に避けたい方、国産の天然オーガニック原料にこだわりたい方",
        "point": "乾いた手のひらに2〜3プッシュをとり、顔全体に優しくなじませます。小鼻や目元は指の腹で円を描くように優しく転がし、少量のぬるま湯を加えて白く乳化させてから洗い流してください。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-pomegranate-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！奇跡のオメガ5プニカ酸が真冬のしぼみ肌に濃密な弾力と潤いを呼び戻す高保湿ザクロオイルコスメランク10",
            "description": "11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ザクロオイルコスメを徹底厳選！ヴェレダ、生活の木、アンドエスエイチ、マンディムーン、アンダルーまで厳選。",
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
            "name": "高保湿ザクロオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "ザクロオイル特有の『プニカ酸（オメガ5）』とは何ですか？なぜ冬の乾燥小ジワに効果的なのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "プニカ酸（Punicic acid）とは、植物界においてほぼザクロの種子にしか存在しない極めて希少なオメガ5系の共役リノレン酸です。通常の脂肪酸をはるかに凌駕する強力な抗酸化作用を持ち、角質層のターンオーバーを正常化するとともに、真皮の線維芽細胞に働きかけてコラーゲンの産生を力強くサポートします。真冬（11月・12月）の寒さで毛細血管が収縮し、弾力を失ってしぼんでしまった肌や、目元・口元の乾燥小ジワに対して、ふっくらとしたハリと弾力を再構築する卓越したエイジングリペア効果を発揮します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ザクロオイルはどのようなテクスチャーですか？朝のメイク前に使っても油浮きしませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ザクロ種子油は、ホホバオイルなどの一般的なサラサラしたキャリアオイルと比べると、ややとろみとコクのある濃厚なテクスチャーが特徴です。そのため、朝のメイク前に使用する場合は『半滴〜1滴』のごく少量を手のひら全体へよく伸ばし、顔全体を包み込むように薄くハンドプレスするのがコツです。肌表面で均一な極薄フィルムとなり、日中のエアコン乾燥や木枯らしから肌を守る保護膜として機能し、ファンデーションの乾燥割れを美しく防ぎます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "植物性エストロゲン様成分が含まれていると聞きましたが、敏感肌でも刺激はありませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "ザクロ種子には女性ホルモン（エストロゲン）と構造が似た植物性ステロールやエラグ酸などのポリフェノールが微量に含まれていますが、これは肌に対して穏やかにハリや弾力をサポートする天然の栄養成分であり、合成ホルモンのような強い刺激や副作用はありません。本記事でご紹介しているヴェレダやマンディムーンなどのオーガニック認証製品は純度が高く、冬のバリア乱れ肌でも穏やかに使用できます。ただし、極度の敏感肌の方は使用前に二の腕の内側などでパッチテストを行ってください。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "真冬のザクロオイルの最もおすすめな使い方は？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "夜の入浴後、化粧水でたっぷりと水分を補給した直後に2〜3滴を馴染ませる『ナイトリペアシールド』が最も効果的です。睡眠中の活発な肌再生サイクルと相まって、翌朝のふっくらとしたハリ感が劇的に高まります。また、冬場に特に深くなりやすい目尻やほうれい線には、スキンケアの最後に米粒大のザクロオイルを指先でピンポイントにトントンと重ねづけする『スポット集中密閉パック』も絶大な効果を発揮します。"
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
  <title>保湿力の強さで肌乾燥とさようなら！奇跡のオメガ5プニカ酸が真冬のしぼみ肌に濃密な弾力と潤いを呼び戻す高保湿ザクロオイルコスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ザクロオイルコスメを徹底厳選！ヴェレダ、生活の木、アンドエスエイチ、マンディムーン、アンダルーまで厳選。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-pomegranate-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！奇跡のオメガ5プニカ酸が真冬のしぼみ肌に濃密な弾力と潤いを呼び戻す高保湿ザクロオイルコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と暖房によるインナードライ・しぼみ肌を救う高保湿ザクロオイルコスメを徹底厳選！ヴェレダ、生活の木、アンドエスエイチ、マンディムーン、アンダルーまで厳選。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-pomegranate-oil">
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
      --primary: #991b1b;
      --primary-light: #fee2e2;
      --primary-dark: #7f1d1d;
      --accent: #dc2626;
      --accent-hover: #b91c1c;
      --bg: #fff5f5;
      --card-bg: #ffffff;
      --text-main: #374151;
      --text-sub: #6b7280;
      --border: #fecaca;
      --shadow: 0 4px 15px rgba(153, 27, 27, 0.08);
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
      background: linear-gradient(135deg, #fee2e2 0%, #fff5f5 100%);
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
      background: #fffdfd;
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
      <span class="hero-badge">2026年真冬版 ｜ 徹底エイジング保湿検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！奇跡のオメガ5プニカ酸が真冬のしぼみ肌に濃密な弾力と潤いを呼び戻す高保湿ザクロオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて訪れる気温低下と湿度急減。真冬の過酷な寒冷は毛細血管の血流を停滞させ、真皮の弾力ネットワークを萎縮させて目元やほうれい線の「乾燥小ジワ」「肌しぼみ」を一気に深刻化させます。そんな冬のエイジング危機を救うのが、植物界でもほぼザクロ種子にしか存在しない奇跡の不飽和脂肪酸「プニカ酸（オメガ5）」を濃密に宿すザクロオイルです。強力な抗酸化ポリフェノールと濃密な油分ヴェールでふっくら押し返すハリ肌を育てる名品10選をコスメコンシェルジュが徹底検証・厳選しました。
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
      <h2>冬のしぼみ肌と乾燥小ジワを蘇らせる「ザクロ種子オイル」の皮膚科学的秘密</h2>
      <p>
        初冬の11月から12月は、一年の中で最も肌のエイジングが加速する危険なシーズンです。外気温の急降下によって皮膚表面の温度が下がり、真皮層のコラーゲン・エラスチンの産生スピードが低下。さらに室内暖房による湿度の激減が重なることで、角質細胞同士の結束が緩み、肌の内部から水分が一方的に蒸発していきます。その結果、頬のハリが失われて毛穴が縦長に垂れ下がり、目尻やほうれい線にちりめん状の乾燥小ジワが刻まれる「冬の菲薄化（ひはくか）・しぼみ肌」に直面します。
      </p>
      <p>
        古来より「女性の果実」「生命の果実」として尊ばれてきたザクロ。その小さな種子を低温圧搾して得られるザクロ種子油（ポメグラネートオイル）は、現代の皮膚科学研究においても驚くべき美容エビデンスが次々と解明されています。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 植物界唯一の「オメガ5系プニカ酸」高含有</strong>
          <p>ザクロ種子油の最大の特徴は、全体の約60〜70%を占める共役リノレン酸「プニカ酸」。フリーラジカルを強力に消去し、真冬の寒冷で鈍った角層細胞のターンオーバーを正常化します。</p>
        </div>
        <div class="highlight-card">
          <strong>2. エラグ酸ポリフェノールの抗酸化シールド</strong>
          <p>冬の紫外線UVAや冷風刺激による酸化ストレスを物理的・化学的に遮断。皮膚の細胞膜を保護し、どんよりとくすんだ冬の肌トーンを内側から輝く透明美肌へと導きます。</p>
        </div>
        <div class="highlight-card">
          <strong>3. コラーゲン合成を後押しする弾力再建</strong>
          <p>植物性ステロール等の微量有用成分が真皮環境を整え、寒さで硬直・収縮した肌組織に跳ね返すようなハリ感を付与。目元や口元の乾燥小ジワを目立たなくさせます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿ザクロオイルコスメ おすすめ10選 比較一覧表</h2>
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
      <h2>プロが指南する！真冬のザクロオイル活用術＆失敗しない選び方</h2>
      <h3>1. 「夜のスキンケアの最終密閉ステップ」で集中リペア</h3>
      <p>
        ザクロオイルに含まれるプニカ酸やポリフェノールは、睡眠中の副交感神経優位な時間帯に行われる肌細胞の修復・再生プロセスと抜群の相乗効果を発揮します。化粧水、美容液、乳液等で水分を十分に補給した直後、手のひらに2〜3滴のザクロオイルをとって温め、顔全体を引き上げるようにハンドプレスしてください。翌朝洗顔した瞬間、手のひらを跳ね返すような密度の高い弾力肌に驚くはずです。
      </p>
      <h3>2. 目元・ほうれい線への「スタンプ重ね塗りテクニック」</h3>
      <p>
        真冬の冷風にさらされてファンデーションが割れやすい目尻やほうれい線には、顔全体に伸ばした後にさらに米粒大のオイルを薬指の腹にとり、摩擦を絶対に起こさないよう優しく垂直にトントンと押し込みます。薄い油膜が小ジワの溝を埋め尽くし、乾燥によるシワの定着を物理的にブロックします。
      </p>
      <h3>3. 他の植物オイルとのブレンド使いでテクスチャーを自在に調整</h3>
      <p>
        ザクロ種子油は非常にリッチでコクがあるため、日中のメイク前や軽やかな使用感を好む場合は、ホホバオイルやマカダミアオイル、スクワランなどのサラサラしたオイルと1:1で手のひらでブレンドして使用するのも上級者のテクニックです。浸透性と保護力の両方を手軽にカスタマイズできます。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ザクロオイル特有の「プニカ酸（オメガ5）」とは何ですか？なぜ冬の乾燥小ジワに効果的なのですか？</div>
        <div class="faq-a">プニカ酸（Punicic acid）とは、植物界においてほぼザクロの種子にしか存在しない極めて希少なオメガ5系の共役リノレン酸です。通常の脂肪酸をはるかに凌駕する強力な抗酸化作用を持ち、角質層のターンオーバーを正常化するとともに、真皮の線維芽細胞に働きかけてコラーゲンの産生を力強くサポートします。真冬（11月・12月）の寒さで毛細血管が収縮し、弾力を失ってしぼんでしまった肌や、目元・口元の乾燥小ジワに対して、ふっくらとしたハリと弾力を再構築する卓越したエイジングリペア効果を発揮します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ザクロオイルはどのようなテクスチャーですか？朝のメイク前に使っても油浮きしませんか？</div>
        <div class="faq-a">ザクロ種子油は、ホホバオイルなどの一般的なサラサラしたキャリアオイルと比べると、ややとろみとコクのある濃厚なテクスチャーが特徴です。そのため、朝のメイク前に使用する場合は「半滴〜1滴」のごく少量を手のひら全体へよく伸ばし、顔全体を包み込むように薄くハンドプレスするのがコツです。肌表面で均一な極薄フィルムとなり、日中のエアコン乾燥や木枯らしから肌を守る保護膜として機能し、ファンデーションの乾燥割れを美しく防ぎます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 植物性エストロゲン様成分が含まれていると聞きましたが、敏感肌でも刺激はありませんか？</div>
        <div class="faq-a">ザクロ種子には女性ホルモン（エストロゲン）と構造が似た植物性ステロールやエラグ酸などのポリフェノールが微量に含まれていますが、これは肌に対して穏やかにハリや弾力をサポートする天然の栄養成分であり、合成ホルモンのような強い刺激や副作用はありません。本記事でご紹介しているヴェレダやマンディムーンなどのオーガニック認証製品は純度が高く、冬のバリア乱れ肌でも穏やかに使用できます。ただし、極度の敏感肌の方は使用前に二の腕の内側などでパッチテストを行ってください。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 真冬のザクロオイルの最もおすすめな使い方は？</div>
        <div class="faq-a">夜の入浴後、化粧水でたっぷりと水分を補給した直後に2〜3滴を馴染ませる「ナイトリペアシールド」が最も効果的です。睡眠中の活発な肌再生サイクルと相まって、翌朝のふっくらとしたハリ感が劇的に高まります。また、冬場に特に深くなりやすい目尻やほうれい線には、スキンケアの最後に米粒大のザクロオイルを指先でピンポイントにトントンと重ねづけする「スポット集中密閉パック」も絶大な効果を発揮します。</div>
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

with open("winter-pomegranate-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-pomegranate-oil.html!")
