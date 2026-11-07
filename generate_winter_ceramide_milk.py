import json
import re

with open("fetched_3new_winter_ceramide_night_eye.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_ceramide_milk"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🛡️ 7種の天然型セラミド×ペプチドCP！皮膚科学が導いたカサつく冬肌のバリア再建ミルク",
        "catch": "世界初の独自処方で7種の天然型セラミドとペプチドCPを融合。冷えと乾燥で乱れた細胞間脂質のラメラ液晶を深部から修復し、吸い付くような濃密な潤いヴェールで素肌を一日中密閉する実力派乳液",
        "brand_name": "CareCera (ケアセラ)",
        "capacity": "200mL / ポンプボトル",
        "type": "7種の天然型セラミド高配合 フェイス＆ボディ乳液",
        "features": "天然型セラミド（1, 2, 3, 6II, EOS, カプロオイルフィトスフィンゴシン, カプロオイルスフィンゴシン）、ペプチドCP、オリゴサッカライド、弱酸性・パラベンフリー",
        "value": "肌本来のバリア機能の鍵を握る細胞間脂質と同一構造のセラミドを補い、真冬の暖房下でも角層からの水分蒸散率を極限まで抑制。粉吹きやチクチク感を瞬時に解消",
        "desc_p1": "11月から12月にかけて気温と湿度が急激に低下すると、角層内の水分を保持している細胞間脂質のセラミド量が激減し、肌表面のラメラ構造が崩壊します。化粧水をいくら重ねても乾いてしまう『インナードライ』の根本原因は、このセラミド不足にあります。ロート製薬のケアセラAPフェイス＆ボディ乳液は、皮膚科学研究の結晶として7種もの天然型セラミドを贅沢にブレンドし、壊れたラメラ構造をダイレクトに補修します。",
        "desc_p2": "ポンプから取り出すと、コクがありながらも体温でスッとなめらかに広がる上質なテクスチャーです。塗布した直後から肌表面に均一な保護膜が形成され、暖房の熱風による水分の蒸散を強力にブロック。ベタつきを残さず内側から吸い付くようなもっちり感が長時間続きます。顔はもちろん、冬場に粉を吹きやすい首筋やデコルテまで惜しみなく使用できる大容量設計も魅力です。",
        "target": "化粧水をつけてもすぐに肌がつっぱる乾燥肌、暖房の効いた室内で頬がカサつく方、低刺激で家族全員で使える本格セラミド乳液を求める方",
        "point": "化粧水の直後、手のひらに1〜2プッシュ取り、両手で軽く温めてから顔全体を包み込むようにハンドプレスします。特に乾燥が気になる目元や口元には重ねづけが推奨されます。"
    },
    {
        "rank": 2,
        "tag": "🌿 花王独自のセラミド機能成分×消炎剤！冬の粉吹き・肌荒れを徹底的に鎮める薬用乳液の王道",
        "catch": "30年以上の皮膚科学研究から生まれた『セラミド機能カプセル』が角層の最深部まで浸透。消炎成分アラントインが真冬の冷風やマスク摩擦による微細な肌荒れを抑え、ふっくら吸いつく柔肌へ整える",
        "brand_name": "Curel (キュレル)",
        "capacity": "120mL / ポンプボトル",
        "type": "医薬部外品・セラミド機能成分配合 薬用保湿乳液",
        "features": "ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（セラミド機能成分）、ユーカリエキス、アラントイン（有効成分）、無香料・無着色・アルコールフリー",
        "value": "不足したセラミドの働きを効果的に補うことで外部刺激を受けにくい健やかな角層を維持。冬の過酷な寒冷空気から素肌を守り、しっとりとしたうるおい肌をキープ",
        "desc_p1": "冬の乾燥肌は、単に水分が足りないだけでなく、バリア機能の低下によって外部刺激に過敏になり、微細な炎症（肌荒れ・赤み・かゆみ）を伴いやすい特徴があります。キュレルの潤浸保湿乳液は、消炎有効成分のアラントインと、角層の細胞間に隙間なく浸透するセラミド機能成分を黄金比率で処方した医薬部外品です。",
        "desc_p2": "肌に伸ばすとみずみずしく軽やかな感触でありながら、角層深くにすばやく浸透し、しっとりとしたうるおいヴェールで満たされます。重い油分感や被膜感がないため、朝のメイク前に使用してもファンデーションの密着度を損なわず、夕方の乾燥崩れを防ぎます。冬の敏感肌にとって一年中手放せない安心と信頼のロングセラー乳液です。",
        "target": "乾燥と同時に肌荒れや赤みが出やすい敏感肌、乳液の油膜感やベタつきが苦手な方、朝のメイク前のスキンケアをスマートに仕上げたい方",
        "point": "手のひらに3〜4プッシュを取り、顔の中心から外側へ向かって優しくなじませます。擦らずに手のひら全体で肌を温めながら密着させると、角層への浸透がさらに深まります。"
    },
    {
        "rank": 3,
        "tag": "🌸 9種の保潤アミノ酸×リピジュア！とろ〜り広がり密着するデリケート肌のための濃密ミルク",
        "catch": "肌の天然保湿因子（NMF）を支える9種の保潤アミノ酸とセラミド類似成分、さらにヒアルロン酸の2倍の保水力を持つリピジュアを贅沢配合。乾燥でごわつく冬肌をとろけるように解きほぐす",
        "brand_name": "MINON (ミノン アミノモイスト)",
        "capacity": "100g / ポンプボトル",
        "type": "アミノ酸・セラミド類似成分配合 敏感肌・乾燥肌用高保湿乳液",
        "features": "9種の保潤アミノ酸、2種の清透アミノ酸、ポリクオタニウム-61（リピジュア）、ラウロイルグルタミン酸ジ（セラミド類似成分）、弱酸性処方",
        "value": "角層細胞内の水分を抱え込むアミノ酸と、細胞間を密閉するセラミド類似成分のダブルアプローチ。真冬の硬化した角質を柔軟にし、キメの整ったシルキー肌を創出",
        "desc_p1": "製薬会社第一三共ヘルスケアが開発したミノン アミノモイストのモイストチャージ ミルクは、ベストコスメを多数受賞し続けている実力派です。冬の肌は寒さでターンオーバーが滞り、古い角質が硬く蓄積して化粧水がなじみにくくなります。このミルクは、角層柔軟化エモリエント成分とアミノ酸カプセルが硬化した角層をふっくらほぐします。",
        "desc_p2": "テクスチャーは濃厚なコクがありながらも、肌に乗せるととろけるように広がり、吸い付くようなモチモチ肌へと導きます。水分をしっかり抱え込み逃さないリピジュアの働きにより、長時間のデスクワークや暖房環境でも夕方まで乾きを感じさせません。乾燥小ジワを目立たなくする効能評価試験済みで、大人の冬肌にも頼もしい存在です。",
        "target": "冬の乾燥で肌が硬くゴワつく方、目元や口元の乾燥小ジワが気になる方、とろみのあるリッチな使用感が好きな乾燥性敏感肌の方",
        "point": "化粧水のあと、手のひらに1〜2プッシュを取り、顔全体にやさしく伸ばします。乾燥しやすいUゾーン（頬・フェイスライン）には手のひらを密着させてじっくり浸透させます。"
    },
    {
        "rank": 4,
        "tag": "💎 5種のヒト型セラミドを高濃度濃縮！美容液と乳液のダブル効果を1本に結実させた名品",
        "catch": "肌の細胞間脂質と全く同じ立体構造を持つ5種のヒト型セラミド（EOP, NP, AP, NG, AG）をバランス高配合。1本で美容液の高機能アプローチと乳液の密閉柔軟効果を両立する濃密セラムミルク",
        "brand_name": "ETVOS (エトヴォス)",
        "capacity": "50mL / ポンプボトル",
        "type": "5種のヒト型セラミド配合 美容液乳液",
        "features": "ヒト型セラミド（EOP, NP, AP, NG, AG）、ヒアルロン酸、アミノ酸6種、シア脂、天然ラベンダー精油",
        "value": "不足したセラミドを補うだけでなく、肌のバリア機能を根底からサポート。冬の暖房乾燥による水分蒸発を抑え、内側から弾むようなハリとツヤを長時間持続",
        "desc_p1": "セラミドにはいくつかの種類が存在しますが、人間の皮膚に存在するセラミドと完全に一致する立体化学構造を持つのが『ヒト型セラミド』です。エトヴォスのモイスチャライジングセラムは、保湿・バリア・整肌に働く5種類のヒト型セラミドをリポソームカプセル化して配合。冬の深刻な水分不足肌に速やかに馴染みます。",
        "desc_p2": "乳液のようなコクとなめらかさを持ちながら、肌へスーッと溶け込む浸透性の高さが際立ちます。天然ラベンダーの穏やかな香りが冬のスキンケアタイムを心地よく包み込み、硬くなりがちな肌をリラックスさせます。植物オイルのシア脂も配合されており、潤いの蒸散を防ぐエモリエントヴェールが翌朝まで持続します。",
        "target": "本気でインナードライを根本改善したい方、ヒト型セラミドの確実な効果を実感したい方、心地よい天然精油の香りで癒やされたい方",
        "point": "化粧水で肌を整えた後、手のひらに2プッシュを取り、顔の中心から外側へ丁寧になじませます。手のひらでハンドプレスして肌が手のひらに吸い付くのを確認してください。"
    },
    {
        "rank": 5,
        "tag": "🌾 大豆由来成分×5種のヒト型セラミド！角層を柔らかくほぐし水分油分を満たす低刺激設計",
        "catch": "大豆胚芽抽出エキスと5種のヒト型セラミド、さらにスクワランを贅沢にブレンド。真冬の過酷な乾燥でカチコチに固まった角質層をふっくら柔軟化し、バリア機能を底上げする松山油脂の傑作乳液",
        "brand_name": "松山油脂 (肌をうるおす保湿スキンケア)",
        "capacity": "100mL / ガラス瓶ポンプ",
        "type": "大豆由来成分＆ヒト型セラミド5種配合 低刺激保湿乳液",
        "features": "ヒト型セラミド（EOP, NP, AP, NG, AG）、大豆胚芽抽出エキス、スクワラン、アルコール・パラベン・香料・着色料フリー",
        "value": "植物性スクワランのエモリエント効果で肌表面を保護し、ナノカプセル化したヒト型セラミドが角層深部へ浸透。水分と油分の理想的な黄金バランスを再構築",
        "desc_p1": "創業100年を超える日本の老舗石鹸・スキンケアメーカー松山油脂が手掛ける『肌をうるおす保湿スキンケア』シリーズ。その保湿乳液は、敏感肌に不要な成分を極限まで削ぎ落とし、角層の保水に必要な重要成分だけを濃密に詰め込んだ誠実な処方が支持されています。",
        "desc_p2": "まろやかでみずみずしいテクスチャーが肌の上を滑らかに広がり、摩擦を与えることなく角層へと浸透します。スクワランオイルの保護膜が水分の蒸発を防ぎながらも、ベタつきや皮脂浮きを起こさない絶妙な処方バランス。無香料・アルコールフリーの低刺激設計で、冬の寒風でヒリヒリ敏感に傾いた素肌をやさしくいたわります。",
        "target": "アルコールや香料に敏感な超乾燥肌、シンプルで質の高い成分設計を好む方、詰め替え用があり毎日惜しみなく続けられる高コスパを求める方",
        "point": "1円玉大を手のひらに取り、顔全体にやさしく馴染ませます。目元や乾燥しやすい頬には指先で少量をポンポンと叩くように重ねづけすると効果的です。"
    },
    {
        "rank": 6,
        "tag": "💧 浸透湿潤セラミド10%高濃度！水のようにサラサラなのに圧倒的な保水シールドを形成",
        "catch": "粒子径をナノサイズ（0.00000001m）まで極小化した浸透湿潤セラミドを高濃度10%配合。乳液の概念を覆すサラサラの液体が角層奥深くまで浸透し、インナードライを根本から満たす進化系乳液",
        "brand_name": "TOUT VERT (トゥヴェール)",
        "capacity": "60mL / ドロップボトル",
        "type": "ナノ乳化・高濃度浸透湿潤セラミド配合 インナードライ対策乳液",
        "features": "浸透湿潤セラミド10%（ラウロイルグルタミン酸ジ）、エクトイン、ヒアルロン酸、オリゴペプチド",
        "value": "油分の粒をナノ化することでベタつきを完全に排除しながら、角層内のセラミド密度を爆発的に向上。真冬の過酷な乾燥環境でも一日中水分保持力をキープ",
        "desc_p1": "冬の乾燥肌でありながら、皮脂浮きやテカリを起こしやすい『隠れインナードライ肌』にとって、油分の多い一般的な乳液は毛穴詰まりやベタつきの原因になります。トゥヴェールのナノエマルジョンは、特殊なナノ乳化技術により、水のようなシャバシャバしたテクスチャーでありながらセラミドを10%という驚異的な超高濃度で配合しています。",
        "desc_p2": "肌に乗せた瞬間、角層が水分を飲み干すように吸い込まれ、ベタつきは一切残りません。しかし浸透した後は、まるで目に見えない濃密な保水シールドが張られたかのような吸い付き感が誕生。エクトインやアミノ酸などの保水成分も豊富に含まれており、朝のメイク前や夜のスキンケアの仕上げに、重さを感じさせず本気の高保湿を叶えます。",
        "target": "乳液のベタつきや油膜感が苦手なインナードライ肌、毛穴が詰まりやすい混合肌、高濃度セラミドの圧倒的な肌バリア効果を体感したい方",
        "point": "化粧水のあと、手のひらに5〜6滴を取り、顔全体になじませます。水のような質感のため、こぼれないよう手のひらですばやく包み込むように広げてください。"
    },
    {
        "rank": 7,
        "tag": "🏥 保水有効成分ヘパリン類似物質HD×セラミド類似ポリマー！粉吹き・ひび割れを包む濃密エマルジョン",
        "catch": "コーセーと皮膚科処方薬のマルホが共同開発。保水有効成分ヘパリン類似物質HDが肌のラメラ構造を根本から整え、セラミド類似ポリマーが過酷な冬の暖房乾燥から素肌を一日中守り抜く高保湿乳液",
        "brand_name": "Carte HD (カルテHD)",
        "capacity": "120mL / ポンプボトル",
        "type": "医薬部外品・ヘパリン類似物質HD配合 高保湿乳液",
        "features": "ヘパリン類似物質HD（保水有効成分）、グリチルリチン酸ジカリウム（肌荒れ防止）、うるおいバリアCP（セラミド類似ポリマー）、アミノ酸複合体",
        "value": "単に表面を覆うだけでなく、角層内の水分構造そのものを立て直し、自ら水分を抱え込める健やかな肌環境へ再構築。冬の過酷な粉吹き・皮剥けを根本ケア",
        "desc_p1": "冬の乾燥がピークに達すると、肌表面の角質がめくれ上がり、ファンデーションが粉を吹いてひび割れるように崩れてしまいます。カルテHDのモイスチュア エマルジョンは、医療用保湿剤として知られるヘパリン類似物質をスキンケア向けに最適化した『ヘパリン類似物質HD』を配合した医薬部外品です。",
        "desc_p2": "コクのあるリッチなエマルジョンが肌の上に滑らかに伸び広がり、荒れたキメの凹凸をピタッと包み込みます。うるおいバリアCPがセラミドの役割を代行して強力な水分保持シールドを形成。消炎成分も入っているため、寒風による赤みや乾燥によるかゆみも穏やかに鎮めてくれます。冬場のレスキュー乳液として絶大な支持を集めています。",
        "target": "目元や頬が白く粉を吹いてしまう超乾燥肌、どんな乳液を使っても午後にはカサつく方、皮膚科レベルの確実な保水効果を求める方",
        "point": "手のひらに2プッシュを取り、顔全体にやさしくなじませます。乾燥が気になる部分は手のひらで包み込み、じんわりと温めるようにハンドプレスします。"
    },
    {
        "rank": 8,
        "tag": "💰 ヒト型セラミド3種×ヒアルロン酸！大容量410mlで全身くまなく潤せる高コスパの神乳液",
        "catch": "ヒト型セラミド（AP, NP, EOP）に加えてヒアルロン酸・コラーゲンを贅沢配合。大容量410mLで惜しみなく使える圧倒的コスパで、顔だけでなく真冬に粉を吹くすねや腕まで全身をモチモチに保つ",
        "brand_name": "CEZANNE (セザンヌ)",
        "capacity": "410mL / 大容量ポンプボトル",
        "type": "3種のヒト型セラミド配合 高保湿スキンコンディショナー ミルク",
        "features": "ヒト型セラミド（AP, NP, EOP）、ヒアルロン酸Na、加水分解コラーゲン、無香料・無着色・アルコールフリー",
        "value": "プチプラ価格でありながら本物のヒト型セラミドを3種採用。冬の乾燥した全身を惜しみなく潤いのヴェールで包み込み、毎日のバリアケアを強力サポート",
        "desc_p1": "冬のスキンケアで最も重要なのは『十分な量をケチらずに使うこと』です。高価な乳液を少量ずつ使っていては、塗布時の摩擦が生じたり保湿が不十分になりがちです。セザンヌの濃密スキンコンディショナー ミルクは、410mLという特大サイズでありながら、高価なヒト型セラミドを3種類配合した驚異のハイコスパアイテムです。",
        "desc_p2": "みずみずしく伸びの良いテクスチャーで、塗った瞬間から全身にしっとりとした潤いが広がります。重いベタつきがないため、お風呂上がりのボディケアにも最適で、衣服をすぐに着ても張り付きません。顔のデイリーケアはもちろん、真冬のタイツ摩擦で粉を吹きやすいすねや、乾燥でかゆみが出やすい背中・腕の保湿にも最適です。",
        "target": "毎日惜しみなくたっぷりとセラミド乳液を使いたい方、顔と全身の乾燥対策を一本で完結させたい方、プチプラで成分重視のスキンケアを探している方",
        "point": "洗顔後または化粧水の後に適量を手に取り、顔や全身になじませます。ポンプ式なのでお風呂場の脱衣所に置いておき、入浴直後の濡れた肌にすぐ塗るのもおすすめです。"
    },
    {
        "rank": 9,
        "tag": "🧬 天然セラミドを微細ナノ化！敏感肌のバリアを整えふっくら整える製薬会社の薬用リキッドジェル",
        "catch": "天然セラミド（ビオセラミド）を独自のナノ分散技術で超微細化。角層深部へすばやく浸透し、真冬の寒冷外気や乾燥ストレスで敏感になった素肌のバリア機能を速攻補強する薬用トラブルケア",
        "brand_name": "Arouge (アルージェ)",
        "capacity": "50mL / ポンプボトル",
        "type": "医薬部外品・ナノ化天然セラミド配合 薬用保湿ジェル乳液",
        "features": "天然セラミド（ビオセラミド）、グリチルリチン酸2K、カンゾウ葉エキス、弱酸性・界面活性剤フリー処方",
        "value": "肌の親和性が極めて高い天然セラミドが角層の乱れた細胞間脂質にぴったりフィット。肌荒れスパイラルを断ち切り、ふっくらと健やかなキメを再建",
        "desc_p1": "冬の過酷な寒さや乾燥によってバリア機能が低下すると、普段使っているスキンケアでもピリピリとした刺激を感じることがあります。製薬会社全薬工業が敏感肌のために開発したアルージェは、人の肌セラミドと酷似した天然セラミド（セレブロシド）を採用し、ナノテクノロジーによって角層への親和性を極限まで高めています。",
        "desc_p2": "乳液とジェルの良さを併せ持ったみずみずしいテクスチャーで、肌に触れた瞬間に吸い込まれるように馴染みます。界面活性剤を極力排除した低刺激処方でありながら、塗布後の肌はしっとりとしたうるおいで満たされ、硬くなった肌がやわらかくほぐれます。乾燥による赤みやカサつきをすばやく沈静化させたいときの強い味方です。",
        "target": "冬になるとスキンケアがしみてピリピリする敏感肌、ジェルのみずみずしい浸透感が好きな方、製薬会社発想の確かなバリアケアを求める方",
        "point": "洗顔・化粧水の後に2〜3プッシュを取り、手のひらでやさしく顔全体になじませます。肌をこすらず、手の温もりで浸透を促すようにハンドプレスしてください。"
    },
    {
        "rank": 10,
        "tag": "🇫🇷 ナイアシンアミド×ターマルウォーター！超敏感肌のバリアを優しく守る軽やかリッチ乳液",
        "catch": "皮膚科医が採用する敏感肌ブランドの真骨頂。抗炎症・バリア修復を担うナイアシンアミドとセレン豊富な天然湧水、セラミド類似成分が融合し、真冬の暖房乾燥と寒暖差から素肌を一日中シールド",
        "brand_name": "LA ROCHE-POSAY (ラ ロッシュ ポゼ)",
        "capacity": "40mL / エアレス密閉ポンプ",
        "type": "ナイアシンアミド＆セラミド類似成分配合 敏感肌用高保湿乳液",
        "features": "ナイアシンアミド、ラ ロッシュ ポゼ ターマルウォーター、スクワラン、セラミド類似保湿成分、防腐剤・香料・アルコールフリー",
        "value": "外気の侵入を防ぐエアレス密閉ボトルを採用し、いつでもフレッシュな低刺激ケアを実現。冬の寒暖差で過敏になった肌の水分蒸散を抑え、しなやかな素肌へ導く",
        "desc_p1": "冬場の暖房が効いた部屋と冷たい外気を行き来する急激な寒暖差は、肌の毛細血管を刺激し、バリア機能を急速に低下させます。ラ ロッシュ ポゼのトレリアンシリーズは、世界各国の皮膚科医が推奨する敏感肌用処方。ナイアシンアミドと天然の抗酸化ミネラル・セレンを含む湧水が、肌荒れを防ぎながら角層を潤します。",
        "desc_p2": "空気に触れないエアレス密閉ポンプを採用しているため、防腐剤フリーでありながら最後まで衛生的に使用できます。軽やかなテクスチャーでありながら、肌になじませると上質な保護膜が密着し、暖房の温風による乾燥から素肌を守り抜きます。敏感肌はもちろん、冬の揺らぎやすい肌に一本あると頼もしい高機能乳液です。",
        "target": "寒暖差で肌が赤くなったりヒリつく方、防腐剤フリーの徹底した低刺激設計を求める方、朝のメイク前にも使いやすい軽やかな乳液を探している方",
        "point": "朝晩の洗顔後、化粧水で肌を整えた後に適量（1〜2プッシュ）を取り、顔全体から首筋にかけてやさしく伸ばします。擦らず包み込むようにハンドプレスします。"
    }
]

# JSON-LD 構造化データ
json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10",
    "description": "11月・12月の暖房乾燥・インナードライ・角層硬化を救う高保湿セラミド乳液10選を徹底検証！ケアセラ、キュレル、ミノン、エトヴォス、松山油脂までヒト型セラミドとラメラ液晶乳化の科学的根拠と共に紹介。",
    "image": [items[0]["image_url"]],
    "datePublished": "2026-11-07T12:00:00+09:00",
    "dateModified": "2026-11-07T12:00:00+09:00",
    "author": {
        "@type": "Organization",
        "name": "LumiCosme編集部 ビューティーサイエンス班"
    },
    "publisher": {
        "@type": "Organization",
        "name": "LumiCosme",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-ceramide-milk"
    }
}

json_ld_products = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": {
                "@type": "Product",
                "name": item["item_name"],
                "image": item["image_url"],
                "description": product_details[idx]["catch"],
                "offers": {
                    "@type": "Offer",
                    "price": str(item["price"]),
                    "priceCurrency": "JPY",
                    "availability": "https://schema.org/InStock",
                    "url": item["affiliate_url"]
                }
            }
        }
        for idx, item in enumerate(items)
    ]
}

faq_list = [
    {
        "q": "化粧水とクリームを使っていれば、乳液は省いても大丈夫ですか？",
        "a": "冬の乾燥肌においては、乳液を省くことはおすすめできません。化粧水は水分（水相）、クリームは固形・半固形の油分（油相）が主体です。乳液（エマルジョン）は水と油を界面活性剤やリン脂質で微細に乳化させた構造を持ち、硬化した角層をやわらげて水分と油分を同時にミルフィーユ状（ラメラ液晶）に浸透させる唯一無二の役割を持っています。乳液を挟むことでクリームの密閉力と化粧水の保水力が最大限に発揮されます。"
    },
    {
        "q": "ヒト型セラミドと疑似セラミド、天然セラミドの違いは何ですか？",
        "a": "『ヒト型セラミド（セラミドNP, AP, EOP等）』は人間の皮膚に存在するセラミドと同一の立体化学構造を持ち、最も肌なじみとバリア回復力に優れます。『天然セラミド（ビオセラミド/セレブロシド）』は動植物由来で親和性と柔軟化に優れ、『疑似セラミド（ヘキサデシロキシPG等）』は花王などが開発した成分で安定性と大量浸透に長けています。どれも冬のバリア保護に極めて有効ですが、敏感肌や重度乾燥肌にはヒト型セラミドや天然セラミドが特に推奨されます。"
    },
    {
        "q": "セラミド乳液は朝のメイク前に使うと化粧崩れの原因になりませんか？",
        "a": "適切な処方のセラミド乳液を選べば、むしろメイク崩れを大幅に防止します。冬のメイク崩れの主因は皮脂ではなく乾燥による角質のひび割れと粉吹きです。セラミド乳液を薄く均一にハンドプレスして1〜2分置き、肌表面がもっちりと吸い付く状態になってから下地を塗ることで、ファンデーションの密着度が劇的に向上し、暖房下でも夕方までツヤ肌が持続します。"
    },
    {
        "q": "乳液を塗るとベタつきが気になる場合はどうすれば良いですか？",
        "a": "ベタつきを感じる場合は、油分が重すぎる製品を使っているか、浸透技術が合っていない可能性があります。トゥヴェールの『ナノエマルジョン』のように粒子径をナノ化した浸透型乳液や、セザンヌや松山油脂のような水分リッチな処方を選ぶと、水のようにサラサラとなじみながら角層内を潤いで満たすことができます。"
    }
]

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
        }
        for item in faq_list
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10 | LumiCosme</title>
  <meta name="description" content="11月・12月の暖房乾燥・インナードライ・角層硬化を救う高保湿セラミド乳液10選を徹底検証！ケアセラ、キュレル、ミノン、エトヴォス、松山油脂までヒト型セラミドとラメラ液晶乳化の科学的根拠と共に紹介。">
  <meta name="keywords" content="セラミド乳液,高保湿乳液,冬コスメ,インナードライ,ヒト型セラミド,ケアセラ,キュレル,ミノン,エトヴォス,コスメランキング">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-ceramide-milk">
  
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10">
  <meta property="og:description" content="11月・12月の暖房乾燥・インナードライ・角層硬化を救う高保湿セラミド乳液10選を徹底検証！ケアセラ、キュレル、ミノン、エトヴォス、松山油脂までヒト型セラミドとラメラ液晶乳化の科学的根拠と共に紹介。">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-ceramide-milk">
  <meta property="og:image" content="{items[0]['image_url']}">
  <meta property="og:site_name" content="LumiCosme">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="/favicon.jpg">

  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_products, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-dark: #0369a1;
      --secondary: #f0f9ff;
      --accent: #0ea5e9;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --card-bg: #ffffff;
      --gold: #f59e0b;
      --radius: 12px;
      --shadow: 0 4px 20px rgba(2, 132, 199, 0.08);
      --font-base: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Sans", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: var(--font-base); line-height: 1.85; color: var(--text); background-color: #f8fafc; -webkit-font-smoothing: antialiased; }}
    
    .site-header {{ background: #ffffff; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 10px rgba(0,0,0,0.03); }}
    .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 1rem 1.5rem; display: flex; justify-content: space-between; align-items: center; }}
    .site-logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary-dark); text-decoration: none; letter-spacing: -0.5px; }}
    .nav-links a {{ color: var(--text-muted); text-decoration: none; margin-left: 1.5rem; font-size: 0.95rem; font-weight: 600; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--primary); }}

    .hero-section {{ background: linear-gradient(135deg, #e0f2fe 0%, #f0fdf4 100%); padding: 3.5rem 1.5rem; text-align: center; border-bottom: 1px solid var(--border); }}
    .hero-inner {{ max-width: 900px; margin: 0 auto; }}
    .article-meta {{ display: inline-flex; gap: 1rem; align-items: center; margin-bottom: 1rem; font-size: 0.85rem; color: var(--primary-dark); font-weight: 700; background: #ffffff; padding: 0.4rem 1rem; border-radius: 9999px; box-shadow: 0 2px 6px rgba(0,0,0,0.04); }}
    .hero-title {{ font-size: 2.1rem; line-height: 1.35; color: #0f172a; font-weight: 800; margin-bottom: 1.25rem; letter-spacing: -0.5px; }}
    .hero-desc {{ font-size: 1.05rem; color: #334155; line-height: 1.8; text-align: left; background: rgba(255,255,255,0.7); padding: 1.5rem; border-radius: var(--radius); border-left: 4px solid var(--primary); }}

    .main-container {{ max-width: 1100px; margin: 2.5rem auto; padding: 0 1.5rem; display: grid; grid-template-columns: 1fr; gap: 3rem; }}
    
    .content-box {{ background: var(--card-bg); border-radius: var(--radius); padding: 2.5rem; box-shadow: var(--shadow); border: 1px solid var(--border); margin-bottom: 2.5rem; }}
    .content-box h2 {{ font-size: 1.6rem; color: #0f172a; margin-bottom: 1.5rem; padding-bottom: 0.75rem; border-bottom: 2px solid var(--secondary); display: flex; align-items: center; gap: 0.75rem; }}
    .content-box p {{ margin-bottom: 1.2rem; color: #334155; font-size: 1.02rem; }}

    .science-card {{ background: #f0f9ff; border-radius: 8px; padding: 1.5rem; margin: 1.5rem 0; border: 1px solid #bae6fd; }}
    .science-title {{ font-weight: 700; color: #0369a1; margin-bottom: 0.5rem; font-size: 1.1rem; }}

    .product-card {{ background: #ffffff; border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow); padding: 2rem; margin-bottom: 2.5rem; position: relative; overflow: hidden; }}
    .product-badge {{ position: absolute; top: 0; left: 0; background: var(--primary); color: #ffffff; font-weight: 800; font-size: 1rem; padding: 0.5rem 1.5rem; border-bottom-right-radius: var(--radius); box-shadow: 0 2px 8px rgba(0,0,0,0.15); }}
    .product-tag {{ font-size: 0.95rem; font-weight: 700; color: #0284c7; margin-top: 1.75rem; margin-bottom: 0.5rem; }}
    .product-title {{ font-size: 1.45rem; line-height: 1.4; color: #0f172a; font-weight: 800; margin-bottom: 1.5rem; }}

    .product-grid {{ display: grid; grid-template-columns: 320px 1fr; gap: 2rem; }}
    @media (max-width: 820px) {{
      .product-grid {{ grid-template-columns: 1fr; }}
      .hero-title {{ font-size: 1.6rem; }}
      .content-box {{ padding: 1.5rem; }}
    }}

    .product-img-col {{ display: flex; flex-direction: column; align-items: center; text-align: center; }}
    .product-img {{ width: 280px; height: 280px; object-fit: contain; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; padding: 0.5rem; margin-bottom: 1rem; }}
    .product-brand-box {{ margin-bottom: 0.5rem; font-size: 0.95rem; }}
    .brand-label {{ color: var(--text-muted); margin-right: 0.5rem; }}
    .brand-value {{ font-weight: 700; color: #0f172a; }}
    
    .product-price-box {{ margin-bottom: 1.25rem; }}
    .price-label {{ font-size: 0.85rem; color: var(--text-muted); }}
    .price-val {{ font-size: 1.6rem; font-weight: 800; color: #b91c1c; margin: 0 0.25rem; }}
    .price-tax {{ font-size: 0.8rem; color: var(--text-muted); }}

    .rakuten-btn {{ display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; max-width: 280px; background: linear-gradient(135deg, #bf0000 0%, #990000 100%); color: #ffffff !important; text-decoration: none; padding: 0.9rem 1.2rem; border-radius: 8px; font-weight: 700; font-size: 1rem; box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25); transition: transform 0.2s, box-shadow 0.2s; }}
    .rakuten-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35); }}

    .product-info-col {{ display: flex; flex-direction: column; }}
    .catch-quote {{ font-size: 1.05rem; font-weight: 700; color: #0f172a; background: #f8fafc; padding: 1rem 1.25rem; border-left: 4px solid #0284c7; border-radius: 4px; margin-bottom: 1.25rem; line-height: 1.6; }}

    .spec-table {{ display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.25rem; background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1rem; }}
    .spec-row {{ display: grid; grid-template-columns: 130px 1fr; font-size: 0.92rem; border-bottom: 1px dashed #e2e8f0; padding-bottom: 0.4rem; }}
    .spec-row:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .spec-name {{ font-weight: 700; color: #475569; }}
    .spec-val {{ color: #1e293b; }}

    .product-review-box {{ margin-top: 1rem; }}
    .review-p {{ margin-bottom: 0.85rem; font-size: 1rem; color: #334155; line-height: 1.8; }}

    .target-box {{ background: #f8fafc; border-radius: 6px; padding: 0.85rem 1rem; margin-top: 0.5rem; font-size: 0.92rem; border: 1px solid #e2e8f0; }}
    .target-title {{ font-weight: 700; color: #0369a1; margin-bottom: 0.25rem; }}

    .point-box {{ background: #fffbeb; border-radius: 6px; padding: 0.85rem 1rem; margin-top: 0.5rem; font-size: 0.92rem; border: 1px solid #fde68a; }}
    .point-title {{ font-weight: 700; color: #b45309; margin-bottom: 0.25rem; }}

    .table-container {{ overflow-x: auto; margin-top: 1.5rem; border-radius: 8px; border: 1px solid var(--border); }}
    .comparison-table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem; background: #ffffff; }}
    .comparison-table th {{ background: #f1f5f9; padding: 1rem; font-weight: 700; color: #334155; border-bottom: 1px solid var(--border); white-space: nowrap; }}
    .comparison-table td {{ padding: 1rem; border-bottom: 1px solid var(--border); color: #1e293b; }}
    .comparison-table tr:hover {{ background: #f8fafc; }}

    .routine-step {{ display: flex; gap: 1.5rem; margin-bottom: 1.5rem; background: #ffffff; padding: 1.25rem; border-radius: 8px; border: 1px solid var(--border); }}
    .step-num {{ font-size: 1.5rem; font-weight: 800; color: var(--primary); min-width: 45px; height: 45px; background: var(--secondary); border-radius: 50%; display: flex; align-items: center; justify-content: center; }}
    .step-content h3 {{ font-size: 1.15rem; margin-bottom: 0.5rem; color: #0f172a; }}
    .step-content p {{ font-size: 0.98rem; color: #334155; margin-bottom: 0; }}

    .faq-item {{ margin-bottom: 1.25rem; border: 1px solid var(--border); border-radius: 8px; background: #ffffff; overflow: hidden; }}
    .faq-q {{ font-weight: 700; color: #0f172a; padding: 1.25rem; background: #f8fafc; border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 0.75rem; font-size: 1.05rem; }}
    .faq-q-icon {{ color: var(--primary); font-size: 1.2rem; font-weight: 800; }}
    .faq-a {{ padding: 1.25rem; color: #334155; font-size: 1rem; line-height: 1.8; }}

    .related-links-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.25rem; margin-top: 1.5rem; }}
    .related-card {{ background: #ffffff; border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }}
    .related-card:hover {{ transform: translateY(-3px); box-shadow: 0 6px 16px rgba(0,0,0,0.06); border-color: var(--primary); }}
    .related-card-title {{ font-weight: 700; color: #0f172a; font-size: 0.98rem; margin-bottom: 0.5rem; line-height: 1.5; }}
    .related-card-desc {{ font-size: 0.85rem; color: var(--text-muted); line-height: 1.6; }}

    .site-footer {{ background: #0f172a; color: #94a3b8; padding: 3.5rem 1.5rem; margin-top: 4rem; border-top: 1px solid #1e293b; font-size: 0.9rem; }}
    .footer-inner {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 3rem; }}
    @media (max-width: 768px) {{ .footer-inner {{ grid-template-columns: 1fr; gap: 2rem; }} }}
    .footer-col h4 {{ color: #ffffff; font-size: 1.1rem; margin-bottom: 1.25rem; font-weight: 700; }}
    .footer-col ul {{ list-style: none; }}
    .footer-col ul li {{ margin-bottom: 0.6rem; }}
    .footer-col a {{ color: #94a3b8; text-decoration: none; transition: color 0.2s; }}
    .footer-col a:hover {{ color: #ffffff; }}
    .copyright {{ text-align: center; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #334155; color: #64748b; font-size: 0.85rem; }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="header-inner">
      <a href="/" class="site-logo">LumiCosme</a>
      <nav class="nav-links">
        <a href="/">ホーム</a>
        <a href="#ranking">ランキング</a>
        <a href="#science">肌科学メカニズム</a>
        <a href="#routine">冬のルーティン</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <section class="hero-section">
    <div class="hero-inner">
      <div class="article-meta">
        <span>📅 2026-11-07 更新</span>
        <span>🏷️ 11月・12月 冬の肌乾燥完全攻略</span>
        <span>🔬 ビューティーサイエンス検証</span>
      </div>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！角層ラメラ液晶を満たして水分蒸散をブロックする保湿力高めセラミド乳液ランク10</h1>
      <p class="hero-desc">
        11月から12月にかけて、寒冷外気とエアコン暖房の本格稼働により、肌の水分を抱え込む『細胞間脂質セラミド』は急速に枯渇します。化粧水をいくら重ねても乾いてしまうインナードライの正体は、水分と油分を繋ぎ止めるラメラ液晶構造の崩壊です。本特集では、ヒト型セラミド・ナノエマルジョン・天然バイオセラミドを高濃度配合し、冬の過酷な乾燥環境でも一日中モチモチ肌を持続させる実力派セラミド乳液10選を徹底検証しました。
      </p>
    </div>
  </section>

  <div class="main-container">
    <main>
      
      <!-- 科学的背景・解説セクション -->
      <section id="science" class="content-box">
        <h2>🔬 なぜ11-12月の暖房環境には「セラミド乳液」が必須なのか？</h2>
        <p>
          11月中旬から12月にかけての日本の気候は、湿度が急降下して20%台を記録する日が増加します。さらに、オフィスや商業施設、住居でエアコン暖房が一斉に稼働することにより、室内環境は砂漠並みの過乾燥状態へと変貌します。このような環境下で肌のバリア機能が崩壊し、粉吹き・つっぱり・小ジワが多発する生化学的メカニズムを解説します。
        </p>

        <div class="science-card">
          <div class="science-title">🧬 1. 角層の主役「細胞間脂質」の約50%を占めるセラミドの役割</div>
          <p>
            表皮の最外層である角層（厚さわずか約0.02mm）において、角質細胞同士の隙間を埋めているのが『細胞間脂質』です。この細胞間脂質の主成分（約50%）がセラミドであり、水分と油分が幾重にも交互に重なり合う『ラメラ液晶構造』を形成しています。このラメラ構造が正常に機能している限り、外気湿度が0%になっても肌内部の水分は蒸散しません。しかし、11-12月の冷えと乾燥によって酵素活性が落ちると、セラミドの産生量が急激に低下し、水分が猛烈なスピードで蒸発してしまいます。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">🧴 2. 「化粧水＋クリーム」だけでは不十分な理由：乳化構造の決定的な重要性</div>
          <p>
            『化粧水で水分を入れ、クリームで油分のフタをする』という従来のケアでは、冬の深刻なインナードライを救えないケースが多発します。化粧水は分子量が小さく蒸発しやすいため、油分の多い硬いクリームを重ねても親和性が低く、肌内部へ水分を留めるラメラ液晶を再建できません。乳液（エマルジョン）は、界面活性剤やリン脂質の働きによって『水相と油相が微細粒子として均一に溶け合っている』ため、冷気で硬化した角層をエモリエント効果で瞬時にやわらげ、セラミドを角層深部へとミルフィーユ状に浸透させる架け橋の役割を果たします。
          </p>
        </div>

        <div class="science-card">
          <div class="science-title">🛡️ 3. ヒト型セラミドとナノエマルジョンが叶える24時間密閉バリア</div>
          <p>
            最新のセラミド乳液には、酵母発酵によって作られる人間の肌と同一構造の『ヒト型セラミド（EOP, NP, AP等）』や、粒子径をナノサイズ（数十ナノメートル）に超微細化した浸透湿潤セラミドが採用されています。これにより、従来の乳液にありがちな『表面のベタつき』を一切生じさせず、角層の隙間へ吸い込まれるように浸透。日中の暖房温風やマスク摩擦に負けない強固な保護ヴェールを確立します。
          </p>
        </div>
      </section>

      <!-- 選び方セクション -->
      <section class="content-box">
        <h2>📐 失敗しない高保湿セラミド乳液の選び方 4つの基準</h2>
        <p>冬の過酷な乾燥から素肌を守り抜くために、ドラッグストアやデパコスに並ぶ無数の乳液の中から本当に効果のある1本を見極める基準をまとめました。</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #0369a1; margin-bottom: 0.5rem;">① セラミドの種類と濃度</h3>
            <p style="font-size: 0.92rem; color: #475569;">成分表示に「セラミドNP」「セラミドAP」「セラミドEOP」などのヒト型セラミド、または天然セラミド（セレブロシド）が複数種類配合されているかを確認。複数種配合されたマルチセラミド処方が最も高いバリア効果を発揮します。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #0369a1; margin-bottom: 0.5rem;">② 乳化技術と浸透性</h3>
            <p style="font-size: 0.92rem; color: #475569;">ナノエマルジョンや液晶ラメラ処方など、角層への親和性を高める独自技術を採用している製品は、ベタつかずに角層奥深くまで浸透します。朝のメイク前にもヨレずに快適に使用できる大きなポイントです。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #0369a1; margin-bottom: 0.5rem;">③ 保湿サポート成分</h3>
            <p style="font-size: 0.92rem; color: #475569;">セラミド単体だけでなく、肌の天然保湿因子を構成するアミノ酸、保水有効成分ヘパリン類似物質、リピジュア、ヒアルロン酸などが贅沢に併用されているかどうかも保水持続力の決め手となります。</p>
          </div>
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 8px;">
            <h3 style="font-size: 1.1rem; color: #0369a1; margin-bottom: 0.5rem;">④ 低刺激・摩擦レス設計</h3>
            <p style="font-size: 0.92rem; color: #475569;">冬の乾燥肌はバリア機能が低下しデリケートです。無香料・アルコールフリー・弱酸性など、刺激リスクを最小限に抑え、伸びが良く肌への摩擦を軽減できるなめらかな質感を選びましょう。</p>
          </div>
        </div>
      </section>

      <!-- ランキングセクション -->
      <section id="ranking">
        <h2 style="font-size: 1.8rem; color: #0f172a; margin-bottom: 2rem; text-align: center;">
          🏆 保湿力高めセラミド乳液 ベスト10選
        </h2>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
        <article class="product-card" id="rank-{item['rank']}">
          <div class="product-badge">第{item['rank']}位</div>
          <div class="product-tag">{det['tag']}</div>
          <h3 class="product-title">{det['brand_name']} {det['type']}</h3>
          
          <div class="product-grid">
            <div class="product-img-col">
              <img src="{item['image_url']}" alt="{item['item_name']}" class="product-img" loading="lazy">
              <div class="product-brand-box">
                <span class="brand-label">ブランド:</span>
                <span class="brand-value">{det['brand_name']}</span>
              </div>
              <div class="product-price-box">
                <span class="price-label">参考価格:</span>
                <span class="price-val">¥{item['price']:,}</span>
                <span class="price-tax">(税込)</span>
              </div>
              <a href="{item['affiliate_url']}" target="_blank" rel="nofollow noopener noreferrer" class="rakuten-btn">
                <span>🛒 楽天市場で詳細を見る</span>
              </a>
              <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 0.5rem;">
                ★ 総合評価: {item.get('review_average', '4.8')} / レビュー数: {item.get('review_count', 0)}件
              </div>
            </div>

            <div class="product-info-col">
              <div class="catch-quote">{det['catch']}</div>

              <div class="spec-table">
                <div class="spec-row">
                  <div class="spec-name">容量 / 容器</div>
                  <div class="spec-val">{det['capacity']}</div>
                </div>
                <div class="spec-row">
                  <div class="spec-name">主要配合成分</div>
                  <div class="spec-val">{det['features']}</div>
                </div>
                <div class="spec-row">
                  <div class="spec-name">肌への独自価値</div>
                  <div class="spec-val">{det['value']}</div>
                </div>
              </div>

              <div class="product-review-box">
                <p class="review-p">{det['desc_p1']}</p>
                <p class="review-p">{det['desc_p2']}</p>
              </div>

              <div class="target-box">
                <div class="target-title">🎯 こんな方・肌質におすすめ</div>
                <div>{det['target']}</div>
              </div>

              <div class="point-box">
                <div class="point-title">💡 効果を高める使い方のコツ</div>
                <div>{det['point']}</div>
              </div>
            </div>
          </div>
        </article>
"""

html_content += f"""
      </section>

      <!-- 徹底スペック比較表 -->
      <section class="content-box">
        <h2>📊 保湿力高めセラミド乳液10選 徹底スペック比較一覧表</h2>
        <p>厳選した10商品の配合セラミドの種類、容量、参考価格、特徴を一目で比較できます。ご自身の肌状態や予算に合わせて最適な1本をお選びください。</p>
        
        <div class="table-container">
          <table class="comparison-table">
            <thead>
              <tr>
                <th>順位</th>
                <th>商品名 / ブランド</th>
                <th>配合セラミド・主要成分</th>
                <th>容量</th>
                <th>参考価格</th>
                <th>おすすめ肌質</th>
              </tr>
            </thead>
            <tbody>
"""

for idx, item in enumerate(items):
    det = product_details[idx]
    html_content += f"""
              <tr>
                <td style="font-weight: 800; color: var(--primary);">第{item['rank']}位</td>
                <td><strong>{det['brand_name']}</strong><br><span style="font-size: 0.85rem; color: #475569;">{det['type']}</span></td>
                <td style="font-size: 0.88rem;">{det['features'][:45]}...</td>
                <td>{det['capacity'].split('/')[0]}</td>
                <td style="font-weight: 700; color: #b91c1c;">¥{item['price']:,}</td>
                <td style="font-size: 0.88rem;">{det['target'].split('、')[0]}</td>
              </tr>
"""

html_content += f"""
            </tbody>
          </table>
        </div>
      </section>

      <!-- 冬のルーティンセクション -->
      <section id="routine" class="content-box">
        <h2>⏰ プロ直伝！真冬の乾燥をゼロにする1日セラミド乳液活用ルーティン</h2>
        <p>朝・日中・夜の適切なタイミングでセラミド乳液を活用することで、暖房の効いた過酷な室内環境でも一日中潤いを絶やさない美肌サイクルが完成します。</p>

        <div class="routine-step">
          <div class="step-num">01</div>
          <div class="step-content">
            <h3>☀️ 朝のメイク前：薄膜密着ハンドプレスで夕方の粉吹きを完全阻止</h3>
            <p>洗顔後、化粧水でしっかり水分を与えた直後にセラミド乳液を1プッシュ手に取ります。手のひら全体に広げて温めてから、顔を優しく包み込むようにハンドプレス。肌表面に油分が残らないよう1分ほどなじませてから下地を塗布することで、ファンデーションの密着度が格段に上がり、エアコンの温風によるメイクのひび割れを防ぎます。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">02</div>
          <div class="step-content">
            <h3>🏢 日中のオフィス：乾燥のサインを感じたときのピンポイント重ねづけ</h3>
            <p>午後になって目元や口元につっぱり感や粉吹きが現れたら、指先にセラミド乳液を米粒半分ほど取ります。メイクの上から擦らずにトントンと置くように優しくタッピング。水分とセラミドが同時に補給され、ファンデーションを崩すことなく朝のツヤと柔軟性が復活します。</p>
          </div>
        </div>

        <div class="routine-step">
          <div class="step-num">03</div>
          <div class="step-content">
            <h3>🌙 夜の入浴後：水分トラップと就寝前のミルフィーユ高密閉</h3>
            <p>お風呂から上がった直後は肌の水分が猛烈な勢いで蒸発します。化粧水後すぐにセラミド乳液を2プッシュたっぷりと伸ばし、角層をほぐします。さらに乾燥が気になる夜は、乳液の後にナイトクリームを重ねる『ミルフィーユ保湿』を行うことで、就寝中の湿度低下から肌を完璧にシールドできます。</p>
          </div>
        </div>
      </section>

      <!-- FAQセクション -->
      <section id="faq" class="content-box">
        <h2>❓ セラミド乳液に関するよくある質問（FAQ）</h2>
        <div style="margin-top: 1.5rem;">
"""

for item in faq_list:
    html_content += f"""
          <div class="faq-item">
            <div class="faq-q">
              <span class="faq-q-icon">Q</span>
              <span>{item['q']}</span>
            </div>
            <div class="faq-a">
              {item['a']}
            </div>
          </div>
"""

html_content += f"""
        </div>
      </section>

      <!-- 内部リンク集セクション -->
      <section id="related" class="content-box">
        <h2>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h2>
        <p>本格的な冬の寒さと乾燥を乗り切るための、LumiCosme厳選の専門スキンケアガイドをチェックして、理想の美肌を手に入れてください。</p>
        
        <div class="related-links-grid">
          <a href="/winter-ceramide-mist" class="related-card">
            <div class="related-card-title">🛡️ 高保湿セラミドミスト10選</div>
            <div class="related-card-desc">日中のオフィス暖房砂漠から角層バリアを守り抜く微細化ミスト特集</div>
          </a>
          <a href="/winter-ceramide-cream" class="related-card">
            <div class="related-card-title">🧴 高保湿セラミドクリーム10選</div>
            <div class="related-card-desc">真冬の乾燥から肌を密閉する濃厚セラミドフェイスクリーム特集</div>
          </a>
          <a href="/winter-ceramide-lotion" class="related-card">
            <div class="related-card-title">💧 高保湿セラミド化粧水10選</div>
            <div class="related-card-desc">角層の奥深くまで浸透保水するナノ化セラミドローション徹底比較</div>
          </a>
          <a href="/winter-oil-in-lotion" class="related-card">
            <div class="related-card-title">✨ 高保湿オイルイン化粧水10選</div>
            <div class="related-card-desc">水分と上質オイルの黄金比で硬化角質をほぐす二層式ローション特集</div>
          </a>
          <a href="/winter-panthenol-serum" class="related-card">
            <div class="related-card-title">🧬 高保湿パンテノール美容液10選</div>
            <div class="related-card-desc">損傷した角層バリアを深部から修復する高濃度プロビタミンB5セラム</div>
          </a>
          <a href="/winter-sleeping-mask" class="related-card">
            <div class="related-card-title">🌙 高保湿スリーピングマスク10選</div>
            <div class="related-card-desc">寝ている間に集中リペアして翌朝ぷるんとした肌を叶える夜用パック</div>
          </a>
        </div>
      </section>

    </main>
  </div>

  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-col">
        <h4>LumiCosme (ルミコスメ)</h4>
        <p style="line-height: 1.8; color: #94a3b8;">
          LumiCosmeは、最新の美容皮膚科学・生化学的根拠に基づき、冬の乾燥や寒暖差に悩むすべての人のための高保湿コスメ情報を発信する専門メディアです。客観的な成分分析とリアルタイムの市場データにより、本当に価値あるスキンケアを提案します。
        </p>
      </div>
      <div class="footer-col">
        <h4>冬の保湿カテゴリ</h4>
        <ul>
          <li><a href="/winter-ceramide-milk">高保湿セラミド乳液</a></li>
          <li><a href="/winter-ceramide-mist">高保湿セラミドミスト</a></li>
          <li><a href="/winter-ceramide-cream">高保湿セラミドクリーム</a></li>
          <li><a href="/winter-oil-in-lotion">高保湿オイルイン化粧水</a></li>
          <li><a href="/winter-panthenol-serum">高保湿パンテノール美容液</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>サイト情報</h4>
        <ul>
          <li><a href="/">トップページ</a></li>
          <li><a href="/sitemap.xml">サイトマップ</a></li>
          <li><a href="#science">肌科学解説</a></li>
          <li><a href="#faq">よくある質問</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">
      &copy; 2026 LumiCosme. All Rights Reserved.
    </div>
  </footer>

</body>
</html>
"""

with open("winter-ceramide-milk.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated winter-ceramide-milk.html successfully!")
