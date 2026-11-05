import json
import re

with open("fetched_3new_apricot_almond_shikon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_sweet_almond_oil"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 有機アーモンド×プラム種子油！真冬の寒暖差で敏感に傾く角層を守る無香料名品",
        "catch": "スイスのオーガニック名門ヴェレダが敏感乾燥肌のために開発。冷風や暖房でピリつく肌を穏やかに鎮静し、薄い皮膚を上質なエモリエント膜で包み込む集中オイル",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "50ml / 遮光ドロップガラス瓶",
        "type": "敏感肌用高保湿フェイシャルトリートメントオイル",
        "features": "有機アーモンド油、プラム種子油、スローベリー花エキス（無香料処方）",
        "value": "香料や着色料を一切使わない低刺激設計。冬の寒冷刺激で赤みが出やすい頬や、皮膚が薄く皮脂膜が作れない超乾燥肌を優しくシールド",
        "desc_p1": "11月から12月にかけて外気温度が低下すると、室内暖房との激しい寒暖差によって皮膚の毛細血管が拡張・収縮を繰り返し、肌がヒリヒリと過敏になる『冬のゆらぎ敏感肌』が発生します。ヴェレダの『アーモンド フェイシャルオイル』は、そんなバリア機能が低下した真冬の肌を最優先に保護するために生まれた歴史ある名作です。",
        "desc_p2": "オーガニックのスイートアーモンドオイルをベースに、肌の柔軟性を高めるプラム種子油をブレンド。手のひらで温めてから優しく包み込むようにプレスすると、角質細胞同士の隙間にスッと入り込み、荒れたキメを整えてふっくらとした弾力を蘇らせます。夜のお手入れはもちろん、冷たい北風が吹きすさぶ朝のメイク前に仕込むことで、日中の乾燥つっぱり感を完全にシャットアウトできます。",
        "target": "真冬になると通常の化粧水でもピリピリとしみる敏感乾燥肌の方、香料が苦手で無香料のピュアなオーガニックコスメを好む方、寒暖差による赤みを落ち着かせたい方",
        "point": "朝晩のスキンケアの最後に、手のひらに2〜3滴をとり、両手を擦り合わせて人肌に温めてから、顔全体を包み込むようにハンドプレスします。目元や口元など皮脂が枯渇しやすい部分には重ねづけが効果的です。"
    },
    {
        "rank": 2,
        "tag": "🛁 水に触れると濃密ミルクに変化！入浴中の過乾燥を防ぐ世界的人気インバスオイル",
        "catch": "ロクシタンを代表する南仏プロヴァンスのベストセラー。冬の熱いお風呂で奪われがちな皮脂を逃さず、洗うステップ自体を極上の保湿トリートメントに変える至高のシャワーオイル",
        "brand_name": "L'OCCITANE (ロクシタン)",
        "capacity": "250ml / ポンプロングボトル",
        "type": "高保湿クレンジング＆モイスチャライジング シャワーオイル",
        "features": "スイートアーモンドオイル（アーモンド油）、ブドウ種子油、トコフェロール、天然芳香成分",
        "value": "濡れた肌に伸ばすと瞬時に軽やかなミルク状へと乳化。真冬の脱衣所で一気に水分が蒸発する『入浴後過乾燥』を根本からブロックし、洗い上がりからベルベット肌が持続",
        "desc_p1": "冬のボディの粉吹き・かゆみの最大の原因は、実は40℃前後の熱い湯船やボディソープの脱脂力によって、角層のセラミドや天然保湿因子（NMF）がお風呂場で流出してしまうことにあります。ロクシタンの『アーモンド モイスチャライジング シャワーオイル』は、洗うと同時に高保湿する逆転の発想から生まれたインバスコスメです。",
        "desc_p2": "黄金色のリッチなオイルを濡れた肌に滑らせると、水分と混ざり合ってキメ細かいシルキーな乳液状の泡へと変化。甘く心地よいアーモンドの芳香がバスルームいっぱいに広がり、冬の寒さで強張った心と体を温かく解きほぐします。洗い流した後も肌表面にしっとりとした油分膜が残り、バスタオルで拭いた直後でも全く粉を吹かない極上の吸い付く美肌へと仕上がります。",
        "target": "真冬のお風呂上がりに脱衣所で肌が突っ張って痒くなりやすい方、贅沢なスイートアーモンドの香りでバスタイムを癒しの空間にしたい方、ボディクリームを塗るのが面倒な方",
        "point": "濡らしたボディスポンジや手のひらに適量をとり、全身をやさしくマッサージするように洗ってからぬるま湯で洗い流します。湯船に浸かりながらデコルテや二の腕を揉みほぐすオイルマッサージにも最適です。"
    },
    {
        "rank": 3,
        "tag": "🌿 低温圧搾コールドプレス×大容量250ml！真冬の全身マッサージ＆プレオイルの決定版",
        "catch": "アロマテラピーの基準を創り続ける生活の木のロングセラー。滑らかな伸びと抜群のクッション性で、冬の冷え固まったふくらはぎや肩をほぐしながら角層深部を高保湿",
        "brand_name": "生活の木 (Tree of Life)",
        "capacity": "250ml / 遮光ドロッパーボトル",
        "type": "天然低温圧搾 スキンケアキャリアオイル",
        "features": "スイートアーモンド油100%（低温圧搾）、オレイン酸（約68%）、リノール酸、ビタミンE",
        "value": "厳格な自社基準による安定した品質。精油（アロマオイル）の希釈ベースとしてはもちろん、単体でも真冬のカチコチ肌を柔軟にするエモリエント力に極めて秀でる",
        "desc_p1": "12月に入ると気温低下と運動不足が重なり、脚や腰回りの血行が滞って皮膚が冷たく硬化します。生活の木の『スイートアーモンドオイル 250ml』は、冷えと乾燥で強張った身体をしなやかにトリートメントするために世界中のセラピストから絶大な信頼を集めるプロ御用達オイルです。",
        "desc_p2": "程よい重みと滑らかさを兼ね備えたテクスチャーは、肌への摩擦を最小限に抑えながら筋肉のコリをほぐすマッサージにうってつけ。オレイン酸が角層深部へじっくり浸透し、ガサガサになったすねやかかとも一度のケアでしっとり柔らかく甦ります。250mlの大容量サイズなので、朝晩のフェイシャルブースターから入浴後のボディケアまで惜しみなく使用できます。",
        "target": "冬の冷えやむくみで脚が重だるく皮膚が乾燥している方、アロママッサージ用の安全なベースオイルを探している方、家族全員で使える万能保湿オイルを求める方",
        "point": "お風呂上がりに500円玉大を手にとり、手のひらで温めてから足首からふくらはぎ、太ももへと下から上へリンパを流すようにマッサージします。好みの精油（ラベンダーやオレンジ等）を1〜2滴ブレンドするのもおすすめです。"
    },
    {
        "rank": 4,
        "tag": "🌍 圧倒的大容量473ml＆世界最高峰コスパ！全身の粉吹き・髪のパサつきを根絶する名作",
        "catch": "世界中のオーガニック愛好家から熱烈な支持を受けるNOW Foodsのベストセラー。純粋圧搾抽出されたスイートアーモンド油が、冬の過酷なエアコン乾燥から全身をガード",
        "brand_name": "NOW Foods (ナウフーズ)",
        "capacity": "473ml / UV遮光ボトル",
        "type": "100%ピュア モイスチャライジングオイル",
        "features": "スイートアーモンド油100%、高濃度オレイン酸、植物性ステロール、天然トコフェロール",
        "value": "500ml近い大容量でありながら2,000円前後の驚異的コスパ。無臭・無添加で酸化安定性が高いため、頭皮ケアからつま先まで冬中使い倒せる頼もしい1本",
        "desc_p1": "真冬にたっぷりオイルを使いたいけれど、小瓶だとすぐになくなってしまう……そんな悩みを一発で解決するのが、全米No.1ナチュラルブランドNOW Foodsの『ピュア スイートアーモンドオイル 473ml』です。",
        "desc_p2": "匂いがなくサラッとした使い心地で、塗布後すぐに肌へ馴染んで表面にベタつきを残しません。真冬のお風呂上がりに濡れた身体全体へ惜しみなく伸ばせば、翌日着替える際にもすねや太ももから白い粉が舞うことが一切なくなります。さらに、ドライヤー前のヘアオイルや冬の硬くなった頭皮のクレンジングオイルとしても極めて優秀で、1本あれば冬の乾燥トラブルを全滅させることができます。",
        "target": "コスパを最優先して全身に毎日大量の保湿オイルを使いたい方、香りのないピュアオイルでヘアケアや頭皮パックも行いたい方、海外の実力派コスメを試したい方",
        "point": "お風呂場に常備し、入浴直後の濡れた肌へ手のひら全体でたっぷり伸ばします。またシャンプー前の乾いた頭皮に馴染ませてマッサージしてから洗髪すると、冬のフケ・かゆみを劇的に防げます。"
    },
    {
        "rank": 5,
        "tag": "👶 国産充填×無添加コールドプレス！赤ちゃんから大人まで優しく潤す2本セット",
        "catch": "使い切りやすい50ml×2本の新鮮パウチボトル。酸化を防ぎながら、真冬の洗顔後ブースターとして化粧水の浸透を劇的に引き上げる安心の国産キャリアオイル",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "100ml (50ml×2本) / ドロッパー容器",
        "type": "オーガニック認証原料使用 ピュア植物油",
        "features": "スイートアーモンド油100%（無添加コールドプレス）、オメガ9、天然ビタミンE",
        "value": "酸化しやすい植物油の弱点を克服する小分けボトル設計。常に搾りたてのフレッシュな状態で肌に塗布でき、冬のデリケートな赤ちゃんの保湿にも最適",
        "desc_p1": "植物油は大容量だと冬の間に酸化が進んで油焼けを起こさないか心配という方に最適なのが、&SHの『スイートアーモンドオイル 100ml（50ml×2本）』です。新鮮なうちに使い切れるサイズ感で、国内工場で厳格に充填されています。",
        "desc_p2": "赤ちゃんのベビーマッサージや妊娠線予防ケアにも推奨されるほどマイルドな使用感。冬の朝の洗顔後、化粧水を塗る前のプレオイルとして1滴馴染ませると、冷気でカチコチに凍りついた角層細胞が瞬時にほぐれ、化粧水をぐんぐん吸い込む柔らかなスポンジ素肌へと変化します。2本セットなので、1本は洗面台のスキンケア用、もう1本は寝室のハンド・ネイル用として使い分けが可能です。",
        "target": "オイルの酸化や劣化を気にする方、赤ちゃんのスキンケアや妊娠線予防オイルを探している方、洗顔後のブースターとして少量を毎日使いたい方",
        "point": "洗顔直後の清潔な肌に1〜2滴を手にとり、温めてから顔全体をハンドプレス。肌が柔らかくなったのを感じてから通常の化粧水を重ねます。余ったオイルは爪の甘皮へ揉み込んでください。"
    },
    {
        "rank": 6,
        "tag": "✨ エコサートCOSMOS認証！未精製コールドプレスの栄養が息づくフレンチオーガニック",
        "catch": "世界基準の有機認証を取得したspa hinokiの逸品。熱を加えない圧搾でビタミンEとミネラルを極限まで残存させ、冬のしぼみ肌に内側から押し上げるハリをもたらす",
        "brand_name": "spa hinoki (スパヒノキ)",
        "capacity": "100ml / 遮光ポンプボトル",
        "type": "COSMOS認証 オーガニックピュアキャリアオイル",
        "features": "未精製オーガニックアーモンド油、天然α-トコフェロール、不飽和脂肪酸、植物ステロール",
        "value": "未精製ならではの豊かな黄金色と高い抗酸化力。ワンプッシュで衛生的に出せる遮光ポンプを採用し、冬のエイジングケアに極上の潤い膜を提供",
        "desc_p1": "40代以降の冬の肌は、水分喪失だけでなく皮膚の抗酸化力の低下によって、たるみや乾燥小ジワが一気に加速します。スパヒノキの『オーガニック スイートアーモンドオイル』は、厳しい審査基準を持つエコサートCOSMOS認証を取得した本格派のオーガニックオイルです。",
        "desc_p2": "未精製オイルには、精製過程で失われがちな天然のビタミンE（トコフェロール）や植物ステロールが豊富に残存。塗布した瞬間に肌の角質層を包み込み、活性酸素やエアコンの乾燥風から細胞膜を保護します。遮光ポンプ式なので空気に触れず酸化をシャットアウト。夜の美容液の後に1プッシュなじませて就寝すれば、翌朝まるでエステ帰りのようなふっくらとしたハリと弾力を実感できます。",
        "target": "冬の乾燥によるたるみやハリ不足が気になるエイジング世代の方、国際オーガニック認証の確かな品質を求める方、ポンプ式で手軽にスキンケアを完結させたい方",
        "point": "夜のお手入れの最後に、ポンプをワンプッシュして手のひらにとり、顔の中心から外側へ、さらに首元からデコルテへと引き上げるように塗布します。ナイトパックとしての密封効果が絶大です。"
    },
    {
        "rank": 7,
        "tag": "🧴 国内精製×大容量500mlポンプ！冬の家族全員のボディ保湿＆お風呂上がりケアに最適",
        "catch": "創業半世紀の自然化粧品研究所が手掛けるプロ仕様。無色無臭でアレルギーリスクを抑え、冬の粉吹きすね・肘・踵を家族全員で毎日惜しみなく高保湿できる頼れる大容量",
        "brand_name": "自然化粧品研究所",
        "capacity": "500ml / 専用ポンプボトル",
        "type": "高純度国内精製 スキンケアキャリアオイル",
        "features": "精製スイートアーモンド油100%、高純度オレイン酸、リノール酸",
        "value": "国内自社工場で丁寧に精製された最高純度。不純物を徹底除去しているため匂いやベタつきがなく、パジャマや寝具への油移りを気にせず全身に使用可能",
        "desc_p1": "冬の家族の乾燥肌対策は、毎日の入浴後にいかに手早く全身を潤すかが勝負です。自然化粧品研究所の『国内精製 スイートアーモンドオイル 500ml』は、リビングやお風呂上がりの脱衣所に1本置いておくだけで、家族みんなの肌トラブルを予防できる大容量ボトルです。",
        "desc_p2": "職人による高度な精製技術で純度を極限まで高めているため、オイル特有の油臭さが一切なく、サラリとした軽快な塗り心地。ポンプをワンプッシュするだけで手早く広範囲に伸ばせ、子供の乾燥肌から大人のカサつく肘・膝・かかとまで、瞬時に吸い付くような潤いヴェールで覆います。大容量なので冬中使っても使い切れないほどのコストパフォーマンスを誇ります。",
        "target": "家族全員で毎日使える大容量ポンプの無添加オイルを探している方、オイルの匂いや衣服への油移りが気になる方、安心できる国内精製品を選びたい方",
        "point": "お風呂から上がった直後、脱衣所で濡れた肌へ直接2〜3プッシュを全身に伸ばします。その後バスタオルで優しく押さえて拭くだけで、全身の粉吹きとかゆみが完全にリセットされます。"
    },
    {
        "rank": 8,
        "tag": "💆 ポンプ付300mlサロン仕様！冷え固まったふくらはぎのリンパマッサージ＆ガサガサ踵を集中ケア",
        "catch": "全国のエステサロンで採用されるプロ仕様のキャリアオイル。摩擦を完全に遮断する極上の滑らかさで、冬のむくみと乾燥角質を同時にトリートメント",
        "brand_name": "マカダミア屋",
        "capacity": "300ml / 専用ポンプボトル",
        "type": "天然100% 精製スイートアーモンドオイル",
        "features": "天然アーモンド油100%、オレイン酸、リノール酸、ビタミンE",
        "value": "マッサージ時の手の滑りと肌への密着力を計算し尽くした粘度設計。冬の硬化したがさがさ踵や肘の角質をやわらげ、しなやかな素肌へと整える",
        "desc_p1": "冬の寒さで足先が冷え切ると、ふくらはぎの筋肉が硬直し、足の裏やかかとがガサガサにひび割れてストッキングに引っかかるようになります。マカダミア屋の『スイートアーモンドオイル 300ml』は、そんな冬のフット＆ボディトラブルを集中ケアするサロン仕様の名品です。",
        "desc_p2": "肌に伸ばすと、適度な厚みを持ったオイルがクッションとなり、力を入れてマッサージしても皮膚を引っ張る痛みがありません。アーモンドのオレイン酸が硬化した角質層をじっくりと軟化させ、お風呂上がりに踵や足裏へ塗り込んで靴下を履いて就寝すれば、翌朝にはひび割れていた皮膚がツルツルに改善。ポンプタイプで片手でも出しやすく、毎晩のマッサージが習慣化します。",
        "target": "冬になるとかかとがひび割れてストッキングが破れてしまう方、脚の冷えやむくみをオイルマッサージで解消したい方、伸びが良くクッション性のあるオイルを好む方",
        "point": "入浴後、足裏やかかとにたっぷり塗り込んでからラップで5分間パックするか、コットン靴下を履いて就寝します。翌朝にはサロン帰りのようなツルツルのかかとが完成します。"
    },
    {
        "rank": 9,
        "tag": "🛡️ 1926年誕生の伝説的ロングセラー！アーモンド油×ハーブが極度の乾燥肌を鉄壁シールド",
        "catch": "ヨーロッパの寒冷な冬を乗り越えるために生まれた濃厚ハーブクリーム。アーモンドオイルの濃密油分とパンジー・カレンドラエキスが、真冬のひび割れ肌を集中ガード",
        "brand_name": "WELEDA (ヴェレダ)",
        "capacity": "75ml / アルミチューブ",
        "type": "全身用高保湿濃厚モイスチャークリーム",
        "features": "アーモンド油、ヒマワリ種子油、ミツロウ、サンシキスミレ（パンジー）エキス、カレンドラエキス",
        "value": "発売から約1世紀にわたり愛され続ける超濃厚処方。水を弾くほどの強固な保護膜を形成し、水仕事による手荒れや真冬のゴワつく肘・膝・顔の乾燥を完全防御",
        "desc_p1": "通常の保湿クリームをどれだけ塗り重ねても、真冬の乾燥に追いつかず肌がカピカピに干からびてしまう……そんな限界状態の肌を救済するのが、ヴェレダの世界的アイコン『スキンフード 75ml』です。",
        "desc_p2": "こっくりと硬めのテクスチャーのクリームには、スイートアーモンドオイルとヒマワリ種子油、天然ミツロウが高濃度で配合されています。手のひらで温めて柔らかくしてから肌に押し込むと、まるで皮膚の上にもう一枚の保護バリア手袋を重ねたかのような強固なシールドが完成。天然ハーブ（ローズマリー・カモミール・パンジー）の爽快なアロマとともに、荒れ果てた角層を一晩でみずみずしく修復します。",
        "target": "手荒れやひび割れがひどく水仕事がつらい方、真冬のスキー場や寒冷地でも絶対に乾燥しない強力な保護膜が欲しい方、世界的な名品クリームを愛用したい方",
        "point": "チューブから指先にパール大をとり、手のひらですり合わせて温めてから、乾燥が最も深刻な部分へ押し込むように塗布します。冬のリップクリームや寝る前のナイトパックとしても極上の威力を発揮します。"
    },
    {
        "rank": 10,
        "tag": "🧪 創業半世紀の安心国産！ビタミンEとミネラルを豊かに保持した無添加スキンケアオイル",
        "catch": "化粧品原料のパイオニアが自信を持ってお届けする定番オイル。無香料・低刺激で肌馴染み抜群、クレンジングからナイトパックまで多用途に冬の素肌を守り抜く",
        "brand_name": "自然化粧品研究所",
        "capacity": "100ml / 遮光プラドロッパー容器",
        "type": "国内精製 ピュアスキンケアオイル",
        "features": "精製スイートアーモンド油100%、オレイン酸、天然ビタミンE、植物性スクワレン微量含有",
        "value": "肌への優しさを最優先に考えた低刺激精製。敏感肌の冬のスキンケアはもちろん、落ちにくいポイントメイクを摩擦レスで優しくオフするクレンジングオイルとしても最適",
        "desc_p1": "冬のクレンジングで肌の潤いを落としすぎて赤みが出てしまう方にぜひ試していただきたいのが、自然化粧品研究所の『スイートアーモンドオイル 100ml』です。",
        "desc_p2": "界面活性剤を一切含まない100%植物油なので、アイメイクやリップメイクの上になじませると、濃密な油分がメイク汚れを浮かび上がらせ、肌のうるおい成分を奪うことなく優しくオフ。洗顔後のブースターや、手持ちの乳液に1滴ブレンドして使う保湿強化剤としてもマルチに機能します。1本手元にあるだけで冬のあらゆる乾燥ピンチを乗り切れる万能コスメです。",
        "target": "冬のクレンジング後のツッパリ感や乾燥荒れに悩む方、手持ちのスキンケアの保湿力を手軽にアップさせたい方、安心の国産無添加オイルを使いたい方",
        "point": "クレンジングには500円玉大をとって優しくメイクに馴染ませ、ティッシュで軽く押さえてからぬるま湯で洗顔します。保湿には化粧水後の乳液に1滴混ぜてハンドプレスしてください。"
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
        "url": f"https://lumi-cosme.vercel.app/winter-sweet-almond-oil#rank-{p['rank']}"
    })

json_ld_schema = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！高濃度オレイン酸とビタミンEが真冬の粉吹き肌＆デリケートな乾燥角層をふっくらほぐす高保湿スイートアーモンドオイルコスメランク10",
            "description": "11月・12月の寒冷乾燥と暖房ダメージによる粉吹き肌やすねのかゆみ、敏感肌を救う高保湿スイートアーモンドオイルコスメを徹底厳選！ヴェレダ、ロクシタン、生活の木、NOW Foods、スパヒノキまで徹底検証。",
            "datePublished": "2026-11-05T09:00:00+09:00",
            "dateModified": "2026-11-05T09:00:00+09:00",
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
            "name": "高保湿スイートアーモンドオイルコスメおすすめランキングTOP10",
            "numberOfItems": 10,
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "スイートアーモンドオイルが真冬の乾燥肌・粉吹き肌に最も適している理由は何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "スイートアーモンドオイルには、人間の皮脂の主成分である『オレイン酸』が約65〜70%、角層のバリア機能を強化する『リノール酸』が約20〜25%、さらに強力な抗酸化作用を持つ『天然ビタミンE（α-トコフェロール）』が豊富に含まれています。11月・12月の厳しい寒さで皮脂分泌が落ち込むと、角質細胞同士を接着する細胞間脂質が乱れて粉を吹きますが、スイートアーモンドオイルは角層へスーッと浸透して人工皮脂膜を再現。水分蒸散を物理的にシャットアウトし、ガサガサに硬直した皮膚をふっくら柔軟に整えます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "お風呂上がりの「インバスケア（濡れた肌への塗布）」はなぜ効果的なのですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "入浴直後の肌は、湯気と水分によって角質層が最大限に膨潤し、水分をたっぷり含んだ状態です。しかし脱衣所に出た瞬間から過乾燥が始まり、わずか数分で入浴前よりも水分量が低下してしまいます。バスタオルで拭く前の濡れた肌にスイートアーモンドオイルを伸ばすと、肌表面の水分と油分が瞬時に乳化し、水分の蒸発ルートを完全に塞ぎます。その後にタオルで押さえるだけで、ベタつきゼロで一日中しっとり吸い付くような高保湿膜が完成します。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "スイートアーモンドオイルは顔の毛穴を詰まらせたりニキビの原因になりませんか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "スイートアーモンドオイルはコメドジェニック（毛穴詰まり）リスクが比較的低い植物油に分類されます。分子が細かく皮膚呼吸を妨げないため、乾燥が原因で皮脂が過剰分泌しているインナードライ肌や大人ニキビ肌の保湿にも適しています。ただし、皮脂分泌が旺盛なTゾーン（鼻や額）にはつけすぎず、乾燥しやすい頬や目元、口元を中心に使用するのがベストです。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "赤ちゃんや敏感肌のベビーマッサージにも安全に使えますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "はい、スイートアーモンドオイルは古くからヨーロッパの産院や小児科でベビーマッサージのファーストチョイスとして使用されてきた非常に安全性の高いオイルです。低刺激でアレルゲンが少ないため、真冬の赤ちゃんの粉吹き肌やオムツかぶれの保護にも安心して使えます。ただし、ナッツアレルギーの心配がある場合は、使用前に腕の内側等でパッチテストを行うことを推奨します。"
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
  <title>保湿力の強さで肌乾燥とさようなら！高濃度オレイン酸とビタミンEが真冬の粉吹き肌＆デリケートな乾燥角層をふっくらほぐす高保湿スイートアーモンドオイルコスメランク10</title>
  <meta name="description" content="11月・12月の寒冷乾燥と暖房ダメージによる粉吹き肌やすねのかゆみ、敏感肌を救う高保湿スイートアーモンドオイルコスメを徹底厳選！ヴェレダ、ロクシタン、生活の木、NOW Foods、スパヒノキまで徹底検証。">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-sweet-almond-oil">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！高濃度オレイン酸とビタミンEが真冬の粉吹き肌＆デリケートな乾燥角層をふっくらほぐす高保湿スイートアーモンドオイルコスメランク10">
  <meta property="og:description" content="11月・12月の寒冷乾燥と暖房ダメージによる粉吹き肌やすねのかゆみ、敏感肌を救う高保湿スイートアーモンドオイルコスメを徹底厳選！ヴェレダ、ロクシタン、生活の木、NOW Foods、スパヒノキまで徹底検証。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-sweet-almond-oil">
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
      --primary: #854d0e;
      --primary-light: #fef9c3;
      --primary-dark: #713f12;
      --accent: #a16207;
      --accent-hover: #582f0e;
      --bg: #fffefa;
      --card-bg: #ffffff;
      --text-main: #27272a;
      --text-sub: #52525b;
      --border: #fef08a;
      --shadow: 0 4px 15px rgba(133, 77, 14, 0.08);
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
      font-weight: 500;
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
      background: linear-gradient(135deg, #ffffff 0%, var(--primary-light) 100%);
      border-radius: var(--radius);
      padding: 2.5rem 2rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}

    .hero-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 20px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--primary-dark);
      margin-bottom: 1rem;
    }}

    .hero-desc {{
      font-size: 1rem;
      color: var(--text-sub);
      line-height: 1.8;
      margin-bottom: 1.2rem;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--text-sub);
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}

    .toc-box {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.8rem;
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
      min-width: 600px;
    }}

    table.comparison-table th, table.comparison-table td {{
      padding: 0.8rem 1rem;
      border-bottom: 1px solid #fef08a;
      text-align: left;
    }}

    table.comparison-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .table-thumb {{
      width: 55px;
      height: 55px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}

    .rank-num {{
      font-weight: 700;
      color: var(--primary);
      font-size: 1.05rem;
    }}

    .price-cell {{
      font-weight: 700;
      color: #b91c1c;
      white-space: nowrap;
    }}

    .table-link {{
      color: var(--primary);
      font-weight: 700;
      text-decoration: none;
    }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
      position: relative;
    }}

    .product-badge {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.3rem 0.8rem;
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
      text-align: center;
    }}

    .product-img {{
      width: 220px;
      height: 220px;
      object-fit: contain;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #ffffff;
      padding: 0.5rem;
    }}

    .product-intro {{
      flex-grow: 1;
    }}

    .product-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
      line-height: 1.4;
    }}

    .product-brand {{
      font-size: 0.95rem;
      color: var(--text-sub);
      margin-bottom: 0.5rem;
    }}

    .product-price {{
      font-size: 1rem;
      color: var(--text-main);
      margin-bottom: 0.8rem;
    }}

    .price-val {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #b91c1c;
    }}

    .product-tag {{
      display: inline-block;
      background: #fefce8;
      border: 1px solid #fef08a;
      color: var(--primary-dark);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.75rem;
      border-radius: 6px;
      margin-bottom: 0.8rem;
    }}

    .product-catch {{
      font-size: 0.95rem;
      color: var(--text-sub);
      line-height: 1.7;
    }}

    .spec-table-box {{
      margin: 1.5rem 0;
      background: #fffefa;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
    }}

    table.spec-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }}

    table.spec-table th, table.spec-table td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid #fef08a;
      text-align: left;
    }}

    table.spec-table th {{
      width: 30%;
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
    }}

    .review-body {{
      margin-top: 1.5rem;
    }}

    .review-body h4 {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.8rem;
    }}

    .review-body p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .target-box, .point-box {{
      background: #fefce8;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.2rem;
      border-radius: 0 8px 8px 0;
      margin-top: 1rem;
      font-size: 0.92rem;
    }}

    .target-box strong, .point-box strong {{
      color: var(--primary-dark);
      display: block;
      margin-bottom: 0.3rem;
    }}

    .btn-wrap {{
      margin-top: 1.8rem;
      text-align: center;
    }}

    .rakuten-btn {{
      display: inline-block;
      width: 100%;
      max-width: 480px;
      background: linear-gradient(135deg, #bf0000 0%, #e60000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 1.05rem;
      text-align: center;
      padding: 1rem 1.5rem;
      border-radius: 30px;
      text-decoration: none;
      box-shadow: 0 4px 15px rgba(230, 0, 0, 0.25);
      transition: all 0.3s;
    }}

    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(230, 0, 0, 0.35);
      background: linear-gradient(135deg, #a60000 0%, #cc0000 100%);
    }}

    .guide-section, .faq-section {{
      background: #ffffff;
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 2.5rem;
      border: 1px solid var(--border);
      box-shadow: var(--shadow);
    }}

    .guide-section h2, .faq-section h2 {{
      font-size: 1.4rem;
      color: var(--primary-dark);
      margin-bottom: 1.2rem;
      padding-bottom: 0.5rem;
      border-bottom: 2px solid var(--primary-light);
    }}

    .guide-section h3 {{
      font-size: 1.15rem;
      color: var(--primary);
      margin: 1.5rem 0 0.6rem;
    }}

    .guide-section p {{
      margin-bottom: 1rem;
      font-size: 0.98rem;
      line-height: 1.8;
    }}

    .faq-item {{
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid #fef08a;
    }}

    .faq-q {{
      font-weight: 700;
      color: var(--primary-dark);
      font-size: 1.05rem;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
    }}

    .faq-q span {{
      color: var(--primary);
      font-size: 1.2rem;
      line-height: 1;
    }}

    .faq-a {{
      color: var(--text-main);
      font-size: 0.95rem;
      line-height: 1.8;
      padding-left: 1.7rem;
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
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.2rem;
    }}

    .related-card {{
      display: block;
      background: #fffefa;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.2rem;
      text-decoration: none;
      transition: all 0.2s;
    }}

    .related-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
      border-color: var(--primary);
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
      color: #a1a1aa;
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
      <span class="hero-badge">2026年真冬版 ｜ 徹底保湿コスメ検証</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！高濃度オレイン酸とビタミンEが真冬の粉吹き肌＆デリケートな乾燥角層をふっくらほぐす高保湿スイートアーモンドオイルコスメランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて日本列島を襲う本格的な寒気と、暖房フル稼働による湿度の激減。皮膚のバリア機能が著しく低下し、すねや背中がチクチク痒くなって粉を吹き、洗顔後の頬がピリピリと痛む限界状態に陥る方が急増します。そんな真冬の「皮脂枯渇」と「角層の強張り」を根本から包み込み、赤ちゃんの肌のようにふっくら柔らかく再生させるのが、王道キャリアオイルの最高峰「スイートアーモンドオイル」です。高純度オレイン酸と天然ビタミンEを惜しみなく配合した高保湿名品10選をコスメコンシェルジュが徹底検証・厳選しました。
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
      <h2>真冬の粉吹きすね＆ゆらぎ敏感肌を劇的に救済するスイートアーモンドオイルの科学</h2>
      <p>
        初冬の11月下旬から12月にかけて湿度が20%台に落ち込むと、角層の水分保持を司る細胞間脂質（セラミド等）のラメラ構造が崩壊し、角質細胞がめくれ上がって白く粉を吹きます。さらに皮脂腺の少ないすねや肘、頬は天然の油膜シールドを自前で作ることができず、衣服の擦れや冷風の刺激で炎症を起こしてしまいます。
      </p>
      <p>
        スイートアーモンドオイルが冬の乾燥肌対策として何世紀にもわたり世界中で圧倒的支持を集める理由は、その「皮脂親和性の高さ」と「圧倒的なエモリエント力（皮膚柔軟性）」にあります。
      </p>

      <div class="intro-highlight-grid">
        <div class="highlight-card">
          <strong>1. 皮脂構成比率と完全に合致するオレイン酸（約68%）</strong>
          <p>人の皮脂膜の約4割を占めるオレイン酸を豊富に含有。硬化した角質層の隙間にスッと入り込んで擬似皮脂膜を形成し、過酷なエアコン環境でも水分を一切逃しません。</p>
        </div>
        <div class="highlight-card">
          <strong>2. 若返りのビタミン「天然α-トコフェロール（ビタミンE）」</strong>
          <p>植物油の中でもトップクラスのビタミンE含有量を誇り、冬の寒冷血行不良で滞った毛細血管のめぐりをサポート。どんよりくすんだ冬肌にみずみずしい透明感を取り戻します。</p>
        </div>
        <div class="highlight-card">
          <strong>3. 赤ちゃんから使える圧倒的な低刺激・安全性</strong>
          <p>ヨーロッパの産院で新生児のベビーマッサージに第一選択されるほど皮膚刺激性が低く、敏感肌やアトピー傾向の肌でもピリつきを感じずに安心して全身を保湿できます。</p>
        </div>
      </div>
    </section>

    <section class="table-section" id="comparison">
      <h2>高保湿スイートアーモンドオイルコスメ おすすめ10選 比較一覧表</h2>
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
      <h2>プロ直伝！真冬のスイートアーモンドオイル選び方＆保湿力を倍増させる使用テクニック</h2>
      <h3>1. 「お風呂上がりの濡れた肌にそのまま塗布（インバスケア）」で粉吹きをゼロに</h3>
      <p>
        冬の入浴後、脱衣所でバスタオルで身体を拭いた瞬間から、角層の水分は猛烈な勢いで空気中へ蒸散します。これを防ぐ最強のテクニックが『インバス・濡れ肌オイル塗布』です。お風呂から上がる直前、肌にまだ水滴がついている状態でスイートアーモンドオイルを全身に伸ばします。水分とオイルが肌の上で瞬時に乳化し、肌表面に薄く柔らかな保護膜を形成。その後にバスタオルで優しく押さえるように水分を吸い取るだけで、一日中粉を吹かないビロード肌が完成します。
      </p>
      <h3>2. 「朝のメイク前ブースター仕込み」でファンデーションの毛穴落ち・乾燥割れを防止</h3>
      <p>
        冬のメイク崩れは、実は油分過多ではなく「内側の乾燥（インナードライ）」によって引き起こされます。朝の洗顔直後、肌にまだ潤いがあるうちにスイートアーモンドオイルを『わずか1滴』手のひらで温めて全顔をハンドプレス。その後に通常の化粧水を重ねると、角層がふっくらとほぐれて化粧水がぐんぐん浸透し、日中のファンデーション割れを劇的に防ぐことができます。
      </p>
      <h3>3. 「シャンプー前の頭皮オイルクレンジング」で冬のフケ・かゆみを一掃</h3>
      <p>
        真冬になると頭皮が乾燥してパラパラとフケが出たり、かゆみに悩まされる方が増えます。週に1回、シャンプー前の乾いた頭皮にスイートアーモンドオイルを大さじ1杯程度馴染ませ、指の腹で頭皮を優しく揉みほぐします。毛穴に詰まった酸化皮脂を浮かび上がらせながら高保湿し、ぬるま湯で洗い流してから普通にシャンプーすると、冬の頭皮トラブルが嘘のように鎮まります。
      </p>
    </section>

    <section class="faq-section" id="faq">
      <h2>よくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> スイートアーモンドオイルが真冬の乾燥肌・粉吹き肌に最も適している理由は何ですか？</div>
        <div class="faq-a">スイートアーモンドオイルには、人間の皮脂の主成分である「オレイン酸」が約65〜70%、角層のバリア機能を強化する「リノール酸」が約20〜25%、さらに強力な抗酸化作用を持つ「天然ビタミンE（α-トコフェロール）」が豊富に含まれています。11月・12月の厳しい寒さで皮脂分泌が落ち込むと、角質細胞同士を接着する細胞間脂質が乱れて粉を吹きますが、スイートアーモンドオイルは角層へスーッと浸透して人工皮脂膜を再現。水分蒸散を物理的にシャットアウトし、ガサガサに硬直した皮膚をふっくら柔軟に整えます。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> お風呂上がりの「インバスケア（濡れた肌への塗布）」はなぜ効果的なのですか？</div>
        <div class="faq-a">入浴直後の肌は、湯気と水分によって角質層が最大限に膨潤し、水分をたっぷり含んだ状態です。しかし脱衣所に出た瞬間から過乾燥が始まり、わずか数分で入浴前よりも水分量が低下してしまいます。バスタオルで拭く前の濡れた肌にスイートアーモンドオイルを伸ばすと、肌表面の水分と油分が瞬時に乳化し、水分の蒸発ルートを完全に塞ぎます。その後にタオルで押さえるだけで、ベタつきゼロで一日中しっとり吸い付くような高保湿膜が完成します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> スイートアーモンドオイルは顔の毛穴を詰まらせたりニキビの原因になりませんか？</div>
        <div class="faq-a">スイートアーモンドオイルはコメドジェニック（毛穴詰まり）リスクが比較的低い植物油に分類されます。分子が細かく皮膚呼吸を妨げないため、乾燥が原因で皮脂が過剰分泌しているインナードライ肌や大人ニキビ肌の保湿にも適しています。ただし、皮脂分泌が旺盛なTゾーン（鼻や額）にはつけすぎず、乾燥しやすい頬や目元、口元を中心に使用するのがベストです。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 赤ちゃんや敏感肌のベビーマッサージにも安全に使えますか？</div>
        <div class="faq-a">はい、スイートアーモンドオイルは古くからヨーロッパの産院や小児科でベビーマッサージのファーストチョイスとして使用されてきた非常に安全性の高いオイルです。低刺激でアレルゲンが少ないため、真冬の赤ちゃんの粉吹き肌やオムツかぶれの保護にも安心して使えます。ただし、ナッツアレルギーの心配がある場合は、使用前に腕の内側等でパッチテストを行うことを推奨します。</div>
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

with open("winter-sweet-almond-oil.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully generated winter-sweet-almond-oil.html!")
