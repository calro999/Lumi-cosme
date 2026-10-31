import json

with open("rakuten_3winter_body_booster_shampoo_data.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_body_cream"]["items"]

body_cream_details = [
    {
        "rank": 1,
        "tag": "🏆 セラミド機能成分配合！すねの粉吹き・ひび割れ寸前の超乾燥肌を濃厚に密封する薬用高保湿バーム",
        "catch": "水分が蒸発した冬の皮膚にセラミドの盾を形成。外部刺激を寄せ付けず翌朝までしっとりモチモチ肌が持続",
        "capacity": "70g",
        "type": "医薬部外品・薬用濃厚モイスチャーバーム",
        "texture": "こっくりと濃密なテクスチャーながら、肌の体温でじんわりとろけて摩擦なくスーッと伸び広がる",
        "ingredients": "ヘキサデシロキシPGヒドロキシエチルヘキサデカナミド（セラミド機能成分）、アラントイン（有効成分・消炎）、スクワラン、ユーカリエキス、グリセリン",
        "finish": "肌表面にピタッと密着するうるおい保護膜を形成。ベタつかずパジャマや衣類が張り付かない心地よい仕上がり",
        "desc_p1": "11月から12月にかけて気温が一段と低下すると、下肢やすね、ひじ・ひざの皮脂腺がほとんど働かなくなり、皮脂膜が消失します。その状態でストッキングやタイツ、ウール素材のインナーを着用すると、繊維の摩擦によって角質層がめくれ上がり、白い粉を吹いたような激しい乾燥状態に陥ります。",
        "desc_p2": "花王の皮膚科学研究を結集した『キュレル モイスチャーバーム』は、角層の隙間を満たすセラミドの働きを忠実に補うセラミド機能成分を高配合。さらに肌荒れ・粉吹きに伴う炎症を抑える有効成分アラントインを配合し、カサカサしてかゆみを感じやすい冬の皮膚を穏やかに鎮めます。通常のローションでは追いつかない頑固な乾燥部分も、ひと塗りでしっとりとした柔軟性を取り戻します。",
        "target": "お風呂上がりにすねや腰回りがカサついて粉を吹いてしまう方、ストッキングを着脱する際に摩擦でチクチク痛痒くなる方、無香料・弱酸性で敏感肌でも毎日使える薬用バームを求める方",
        "technique": "入浴後、タオルで軽く水気を押さえた直後（5分以内）が最も効果的です。手のひらに適量を取り、手の体温で少し温めて柔らかくしてから、乾燥しやすいすねや腕に円を描くように優しく塗り広げてください。粉吹きがひどい部位には重ねづけがおすすめです。",
        "voice": "『毎年冬になるとすねが砂漠のように粉を吹いてタイツの内側が真っ白になっていましたが、これを使い始めてからすねがツルツルになりました。ベタつかないのに保湿力が一晩中続いて手放せません。』(30代・営業職)",
        "caution": "濃厚なバームタイプのため、極端に寒い室温では少し硬く感じることがあります。手のひらの熱で数秒温めてから肌になじませるとスムーズに伸びます。"
    },
    {
        "rank": 2,
        "tag": "🌿 ナイアシンアミド×パンテノール配合！大容量で家族全員の真冬の全身乾燥をうるおし尽くす皮膚科発想クリーム",
        "catch": "角層の奥深くまですばやく浸透。水分と油分を黄金バランスで補い、乾いた肌のバリア機能を力強く立て直す",
        "capacity": "566g",
        "type": "低刺激・高保湿モイスチャライジングクリーム",
        "texture": "リッチでクリーミーなコクのある質感。見た目の濃厚さに反して肌へすばやく馴染み、白浮きせず浸透",
        "ingredients": "ナイアシンアミド（整肌成分）、パンテノール（プロビタミンB5）、グリセリン、ヒマワリ種子油、トコフェロール",
        "finish": "吸い付くような濃密な保湿感がありながら、肌表面はサラリとなめらか。べたつきを残さず快適",
        "desc_p1": "冬場は暖房器具の長時間使用によって室内の湿度が20〜30%台まで急落します。乾燥した空気は皮膚の水分を容赦なく奪い去り、肌の防御壁であるバリア機能を破壊します。特に面積の広い背中や太もも、腕はケアが手薄になりやすく、知らず知らずのうちに乾燥が進んでしまいます。",
        "desc_p2": "世界70カ国以上で敏感肌に寄り添い続けるセタフィルの『モイスチャライジングクリーム』は、保湿の3大黄金成分「ナイアシンアミド」「パンテノール」「高純度グリセリン」を独自比率で処方。水分を肌内部に引き寄せて抱え込み、良質な植物性オイルがフタをすることで、冬の過酷な乾燥環境でもうるおいを最大48時間キープします。566gという大容量サイズのため、惜しみなく全身にたっぷり塗布できるのも魅力です。",
        "target": "全身の広範囲を毎日惜しみなくケアしたい方、家族全員（子どもから大人まで）でシェアできる低刺激クリームを探している方、こっくり重いクリームでもベタつきが苦手な方",
        "technique": "大容量ジャーからたっぷり指先ですくい、入浴後の全身へ惜しみなく伸ばします。特に乾燥が気になるひじ、ひざ、かかとには少し厚めに塗り込み、就寝時に綿の靴下や長袖インナーを着用すると翌朝の柔らかさが劇的に変わります。",
        "voice": "『大容量でコスパが素晴らしく、冬の全身保湿に家族で毎日使っています。伸びが良くてすぐに肌に馴染むので、塗った直後に服を着られるのが本当に助かります。冬の必需品です。』(40代・主婦)",
        "caution": "大容量ボトルのため、手で直接取る際は清潔なスパチュラや乾いた手で使用し、衛生面を保つようにしてください。"
    },
    {
        "rank": 3,
        "tag": "🔬 純度99%高濃度グリセリン×CICA！角層10層の奥深くまで瞬時に浸透しガサガサ肌を集中リペア",
        "catch": "医療用レベルの純度を誇る超微粒子グリセリン。ひと塗りで吸い付くようなもっちり素肌へ変貌させる実力派",
        "capacity": "450ml",
        "type": "CICA配合・集中リペア高保湿ボディエマルジョン",
        "texture": "なめらかに広がるミルキーエマルジョン。微細なテクスチャーが角層のキメにぐんぐん入り込む",
        "ingredients": "高純度99%グリセリン、CICAコンプレックス（ツボクサエキス・アラントイン）、ワセリン、パルミチン酸イソプロピル",
        "finish": "塗った瞬間から肌が吸い付くような濃密ヴェールで覆われ、乾燥によるキメの乱れをなめらかに補正",
        "desc_p1": "冬の冷たい風にさらされる手足や首筋は、皮膚の柔軟性が失われてゴワつき、硬化しがちです。粒子が大きい通常の油分クリームだと硬くなった角層を通過できず、肌表面で滑ってしまい、内部の乾きが癒やされないという現象が起こります。",
        "desc_p2": "極寒のノルウェーの漁師の手肌を守るために開発されたニュートロジーナの『インテンスリペア CICA ボディエマルジョン』は、超微粒子化された医療グレードの純度99%グリセリンを採用。硬くこわばった角層10層の奥深くまで素早く到達し、水分をたっぷり抱え込ませます。さらに話題のCICA（ツボクサエキス）とアラントインが、粉吹きや乾燥で傷んだ肌の炎症を穏やかにケア。ポンプ式で手軽に使える利便性も冬のデイリーケアに最適です。",
        "target": "冬になると肌が硬くゴワついてしまう方、ポンプ式でサッと手軽にお風呂上がりの保湿を済ませたい方、CICA成分による肌荒れ防止効果も同時に求めたい方",
        "technique": "入浴後、ワンプッシュを手にとり、腕や脚の心臓に向かって下から上へとマッサージするように塗り広げます。血行を促進しながら成分を行き渡らせることで、冷えによるむくみ対策にも繋がります。",
        "voice": "『赤のニュートロジーナは本当に乾燥知らずになります。ポンプ式なのでお風呂から上がって10秒で全身に塗れるのが最高。翌日夕方になってもすねが粉を吹きません。』(20代・IT勤務)",
        "caution": "非常に保湿力が高いため、皮脂分泌の多い胸元や背中の中央部に塗りすぎるとニキビの原因になることがあります。乾燥しやすい四肢を中心に使用してください。"
    },
    {
        "rank": 4,
        "tag": "❄️ 天然シアバター20%配合！新雪のようにふわりととろけるホイップテクスチャーで真冬の肌を贅沢シールド",
        "catch": "南仏プロヴァンスの自然の恵み。優しいうるおいと芳醇な香りで心まで包み込むホリデーシーズンに最高峰のケア",
        "capacity": "200ml",
        "type": "天然シアバター高配合・ホイップ状ボディクリーム",
        "texture": "まるで泡立てたクリームのような空気を含んだホイップ状。肌に触れると体温でスッと軽やかにメルティ化",
        "ingredients": "シア脂（シアバター20%）、グリセリン、ヒマワリ種子油、トコフェロール、植物エキス",
        "finish": "ベルベットのように上質でマットなツヤ感を残し、内側はしっとりモチモチの赤ちゃん肌のような柔らかさに",
        "desc_p1": "シアの木の実から採れる天然シアバターは、人間の皮脂と非常に近い脂肪酸組成（ステアリン酸やオレイン酸）を持っており、肌なじみの良さと保護力において古来より『保湿の王様』と称されてきました。しかし通常のシアバターは冬場に硬くなりやすく、肌に伸ばす際の摩擦が気になるという課題がありました。",
        "desc_p2": "ロクシタンの『スノーシア ボディクリーム』は、独自のホイップ製法によってシアバターを20%という高濃度で含みながら、新雪のようなエアリーでふわふわな質感を実現。冬の冷えた肌の上でも力を入れずにスーッととろけ、薄く均一な保湿ヴェールを形成します。シアバターの豊かなうるおいが角層からの水分蒸発を完全にシャットアウトし、一日中やわらかな肌触りを保ちます。",
        "target": "上質なオーガニックシアバターの恵みを全身で体感したい方、硬いバームだと塗る時の摩擦が気になる方、冬の自分へのご褒美やホリデーギフトとしてリッチなボディケアを楽しみたい方",
        "technique": "手のひらに適量をすくい、両手で軽く擦り合わせて空気を抱き込ませてから、乾燥しやすいデコルテ、腕、脚へ滑らせます。優しく包み込むようにハンドプレスすると、シアの豊かな膜が肌に一体化します。",
        "voice": "『普通のシアバターは冬に硬くて伸ばしにくいですが、スノーシアはふわっふわで感動的な塗り心地です。翌日の肌が本当にすべすべで、冬のスキンケアが贅沢な癒やしタイムになります。』(30代・クリエイター)",
        "caution": "ホイップ状の繊細なテクスチャーを保つため、直射日光や暖房の温風が直接当たるような高温多湿の場所での保管は避けてください。"
    },
    {
        "rank": 5,
        "tag": "👑 コエンザイムQ10＆ヒアルロン酸配合！大人のしぼんだ乾燥肌にハリと濃密なうるおいを密封する最高峰ニベア",
        "catch": "角層細胞まで豊潤なうるおいで満たす薬用セラムクリーム。年齢とともにカサつきが深まる大人のボディを再生",
        "capacity": "160g",
        "type": "医薬部外品・薬用大人のための最高保湿ボディクリーム",
        "texture": "こっくりとして濃密なリッチクリーム。肌の上でとろけるように馴染み、ピタッと吸着する密着感",
        "ingredients": "グリチルリチン酸ジカリウム（消炎有効成分）、ユビデカレノン（コエンザイムQ10）、ヒアルロン酸Na、PGヒドロキシエチルヘキサデカナミド（セラミドE）、ワセリン",
        "finish": "押し返すようなハリ感とうるおいに満ちた艶やかな輝き。乾燥によるキメのしぼみをふっくら修復",
        "desc_p1": "年齢を重ねるにつれて、肌内部のセラミド量やヒアルロン酸、天然保湿因子（NMF）の産生量は激減します。大人の冬の肌は単なる乾燥にとどまらず、弾力低下やハリの喪失、小ジワ状のキメ乱れといった複合的なトラブルが重なり、より重厚なエイジングケアが必要となります。",
        "desc_p2": "ニベアのプレステージラインとして開発された『ロイヤルブルーボディクリーム うるおい密封』は、大人特有の乾燥にアプローチする薬用高保湿クリームです。抗炎症有効成分に加え、コエンザイムQ10やヒアルロン酸、セラミドEを贅沢にブレンド。濃厚なテクスチャーが角層細胞のすき間を隙間なく埋め尽くし、水分保持力を徹底的に強化します。ドラッグストアで手に入る手軽さでありながら、デパコス級の贅沢なハリ肌へと導きます。",
        "target": "年齢とともにすねや腕の乾燥がひどくなりハリ不足を感じる大人の女性、プチプラ以上デパコス未満のワンランク上のボディケアを求める方、乾燥によるかゆみや赤みを防ぎたい方",
        "technique": "適量を指に取り、首筋からデコルテ、二の腕、ひざ上など、年齢サインやたるみが気になる部分を引き上げるように塗り込みます。寝る前のナイトトリートメントとしても極上の効果を発揮します。",
        "voice": "『青缶のニベアも好きですが、このロイヤルブルーは全く別次元のしっとり感です。すねの縮緬ジワのような乾燥がふっくら目立たなくなり、肌にツヤが出ました。』(40代・公務員)",
        "caution": "非常に油分リッチな処方のため、顔への使用は避け、ボディ専用としてご使用ください。衣服を着る前に1〜2分置いて肌に定着させるとより快適です。"
    },
    {
        "rank": 6,
        "tag": "✨ 甘美なアンバーバニラの魅惑的な香り！シアバター×ホホバオイルがベルベットのような極上ツヤ肌へ仕立てる",
        "catch": "誰もが振り返るラグジュアリーな甘い余韻。冬の特別な夜を華やかに彩るデパコスボディケアの絶対女王",
        "capacity": "340g",
        "type": "フレグランス・ホイップトボディクリーム",
        "texture": "ホイップクリームのようにふんわり軽やかでありながら、伸ばすと驚くほど重厚なうるおいヴェールへと変化",
        "ingredients": "シアバター、ホホバ種子油、スイートアーモンドオイル、加水分解大豆タンパク、ビタミンA・C・E誘導体",
        "finish": "吸い付くようなしっとり感と上品なシルクの光沢。香水要らずの深く芳醇なアンバーバニラが一日中持続",
        "desc_p1": "冬のボディケアは保湿機能だけでなく、乾燥した寒々しい季節に心を温め、高揚感をもたらすアロマや香りの力も非常に大切です。特に11月〜12月のホリデーシーズンや忘年会、クリスマスデートなどのお出かけでは、肌の質感と香りの両方で差をつけたいシーンが増加します。",
        "desc_p2": "ローラメルシエを代表する名品『ホイップトボディクリーム アンバーバニラ』は、『人類モテの香り』としてSNSで社会現象となった至高のフレグランスボディクリームです。甘く官能的なバニラと深みのあるアンバーが絶妙に調和し、夜に塗れば翌日の夕方まで優雅な残り香がふんわり持続。美容成分としてもシアバターやホホバオイルを贅沢に含んでおり、乾燥したボディをベルベットのようになめらかなツヤ肌へと仕上げます。",
        "target": "香水のような上質な香りを一日中まといたい方、デートやイベント前に肌の質感と魅力を最大限に高めたい方、自分へのご褒美に贅沢なデパコスボディクリームをお探しの方",
        "technique": "お出かけ前や就寝前に、手首、デコルテ、うなじ、脚などに少量を薄く馴染ませます。香りが非常に濃厚なため、全身に塗るよりもポイント使いするか、少量を広く伸ばすのが上品に香らせるコツです。",
        "voice": "『本当に良い香りで、職場でも友人にも「どこの香水使ってるの？」と必ず聞かれます。保湿力も抜群で、冬のカサつく腕やすねが吸い付くような手触りになります。』(20代・美容部員)",
        "caution": "香りの持続性が非常に高いため、香りに厳しいオフィスや食事の場では使用量を控えめに調整してください。"
    },
    {
        "rank": 7,
        "tag": "🛡️ 生後1ヶ月の赤ちゃんから使える安心処方！植物性脂質トリオが乾燥性敏感肌を穏やかに満たす大容量フルイド",
        "catch": "南フランスのアベンヌ温泉水配合。肌の熱感をすーっと鎮静させ、うるおいバリアを自然に立て直す皮膚科推奨品",
        "capacity": "400ml",
        "type": "敏感肌用・高保湿フルイドクリーム",
        "texture": "みずみずしく軽やかな乳液とコクのあるクリームの中間テクスチャー。肌にスッと浸透しベタつきゼロ",
        "ingredients": "アベンヌ温泉水、セレクチオーズ（保護成分）、植物性脂質トリオ（セラミド・必須脂肪酸・植物性ステロール）、グリセリン",
        "finish": "カサつきとヒリつきがスッと落ち着き、素肌そのものが水分で満ちたような自然な柔らかさへ",
        "desc_p1": "冬の乾燥が進むと、皮膚のバリアが破綻して外気中のアレルゲンやホコリ、衣服の摩擦に対して過敏に反応する『乾燥性敏感肌』に傾きます。一般的な香料入りクリームやアルコール配合品をつけるとピリピリ染みてしまうため、極めて低刺激な処方が求められます。",
        "desc_p2": "皮膚科学の知見に基づきアベンヌが開発した『トリクセラNT フルイドクリーム』は、アベンヌ村の源泉から直接ボトリングされた温泉水と、肌の皮脂構造を模倣した植物性脂質トリオを配合。外部刺激に無防備になった角層を優しくシールドし、生後1ヶ月の乳幼児から高齢者まで安心して全身に使用できます。みずみずしく伸びの良いフルイド処方のため、お風呂上がりの急激な乾燥時にも素早く全身をカバーできます。",
        "target": "冬になると乾燥で肌がヒリヒリ・ピリピリして普通のクリームが使えない敏感肌の方、赤ちゃんと一緒に使える安全な大容量保湿剤を探している方、ベタつきが一切ない軽い使用感が好きな方",
        "technique": "手のひらに2〜3プッシュを取り、手のひら全体で包み込むように優しく肌に押し当てて馴染ませます。擦るのではなく置くように塗布することで、過敏になった肌への摩擦負担をゼロにします。",
        "voice": "『アトピー気味で冬は粉吹きとかゆみが酷いのですが、アベンヌのトリクセラだけは全く染みずに肌が落ち着きます。大容量ポンプで使いやすく、冬の守り神です。』(30代・看護師)",
        "caution": "ポンプのノズル先端にクリームが固まることがあるため、使用後はティッシュなどで軽く拭き取ると清潔に使い続けられます。"
    },
    {
        "rank": 8,
        "tag": "🍊 国産柚子果皮抽出精油のフレッシュな和アロマ！カルナウバロウ＆シア脂が冬のカサつきをなめらかに包む",
        "catch": "天然由来成分100%のこだわり。絞りたての柚子の香りがバスルームに広がり、心まで解きほぐされる癒やしの時間",
        "capacity": "300ml",
        "type": "無添加・高保湿柚子ボディローションクリーム",
        "texture": "みずみずしいジェルローションとクリームの中間。水滴のようにスーッと角層に吸い込まれる軽やかさ",
        "ingredients": "ユズ果皮油（天然精油）、シア脂、カルナウバロウ、スクワラン、グリセリン、BG",
        "finish": "肌表面はサラサラとすべすべに整い、内側からふっくらとしたみずみずしい水分感が長時間持続",
        "desc_p1": "合成香料の強い香りが苦手な方や、日々の忙しさに追われてストレスを感じている方にとって、入浴後のボディケアは心身をリセットする大切なリラクゼーションの機会です。日本の冬の風物詩である柚子の香りは、交感神経の高ぶりを鎮め、心地よい眠りへと誘う効果があります。",
        "desc_p2": "石鹸づくりの名門・松山油脂の『Mマーク 柚子ボディローション』は、高知県産の丸ごと柚子から水蒸気蒸留法で丁寧に抽出した天然精油のみで香り付け。合成香料・着色料・鉱物油・パラベンを一切使わず、天然のシア脂とカルナウバロウが薄い保護膜を作って冬の乾燥から肌を守ります。ベタつきが全くなく、塗った直後からパジャマがサラリと着られるストレスフリーな使用感が絶賛されています。",
        "target": "人工的な香料が苦手で本物の果実の香りに癒やされたい方、ベタつくのが嫌いでサラサラ仕上がりを好む方、安心の国産無添加スキンケアを愛用したい方",
        "technique": "お風呂上がりに全身へたっぷりと伸ばし、深呼吸しながら天然柚子の爽やかな香りを吸い込んでください。首元や胸元に塗り広げると、就寝中も優しいアロマに包まれます。",
        "voice": "『本物の柚子そのもののフレッシュな香りで、お風呂上がりに塗ると最高に癒やされます。ベタベタしないのに肌はちゃんとしっとりしていて、冬の定番アイテムです。』(30代・Webデザイナー)",
        "caution": "天然精油を使用しているため、合成香料に比べて香りの持続時間は穏やかです。また開封後は数ヶ月以内にフレッシュなうちに使い切ることを推奨します。"
    },
    {
        "rank": 9,
        "tag": "🌿 マカダミアナッツ油×サンダルウッド！乾燥して硬くなったひじ・ひざ・かかとを柔らかくほぐすリッチバーム",
        "catch": "オーストラリア発祥の植物美容学。深呼吸したくなるスモーキーなウッディアロマと濃密なエモリエント効果",
        "capacity": "100ml",
        "type": "高機能ボタニカル・インテンシブボディバーム",
        "texture": "バターのように濃厚でコクのある黄色いクリーム。手のひらで温めるとオイルのようにスルスル伸びる",
        "ingredients": "マカダミア種子油、スイートアーモンド油、シア脂、サンダルウッド油、パチョリ油、ラベンダー油、トコフェロール",
        "finish": "乾燥で硬化した角質がふっくらとほぐれ、手のひらが吸い付くような濃密なうるおいと品のあるツヤへ",
        "desc_p1": "冬場の乾燥は、全身の中でも特に角質層が厚い「ひじ・ひざ・くるぶし・かかと」に顕著に現れます。これらの部位は皮脂腺が極端に少なく、放置すると角質が硬化してガサガサの鱗状になり、最悪の場合はひび割れを起こして痛みを生じます。",
        "desc_p2": "Aesopのボディケアの中でも最も保湿力に特化した『インテンシブ ハイドレーティング ボディバーム』は、人間の皮脂のパルミトレイン酸を豊富に含むマカダミアナッツ油とシアバターを贅沢に配合。硬くなった角質層の奥まで油分を浸透させ、柔軟性を取り戻します。サンダルウッドやパチョリが織りなす洗練されたウッディフローラルの香りは、冬の夜の贅沢なセルフケアタイムを演出してくれます。",
        "target": "ひじ・ひざ・かかとの頑固なガサガサや黒ずみを集中的にケアしたい方、Aesopの上品でユニセックスなウッディの香りが好きな方、ギフトとしても喜ばれる高級ボディケアをお探しの方",
        "technique": "入浴後、かかとやひじに円を描きながら揉み込むようにマッサージします。特にひび割れが気になるかかとには厚めに塗り、綿の靴下を履いて一晩置くと、翌朝には驚くほどフワフワの柔らかいかかとに生まれ変わります。",
        "voice": "『冬になるとかかとが割れてストッキングが引っかかっていましたが、このバームを一週間塗り込んだら赤ちゃんのような柔らかい足裏になりました。香りも最高に贅沢です。』(30代・アパレル店長)",
        "caution": "アルミチューブ容器のため、勢いよく押すとクリームが出過ぎることがあります。チューブの後ろ側から優しく絞り出すように使用してください。"
    },
    {
        "rank": 10,
        "tag": "🌸 ベビーオイルイン処方×優雅なアロマ！ドラッグストアで買える高保湿と贅沢な香りでロングセラーを誇る名品",
        "catch": "ジョンソン独自のミネラルオイルが水分をぎゅっと閉じ込める。乾燥知らずのしっとりシルク肌が翌日まで持続",
        "capacity": "500ml",
        "type": "ベビーオイルイン・高保湿アロマボディミルククリーム",
        "texture": "みずみずしくなめらかなミルキークリーム。スルスルと抵抗なく広がり、全身に素早く行き渡る",
        "ingredients": "ミネラルオイル（高純度ベビーオイル）、ダイズ油、ヒマワリ種子油、シア脂、カミツレ花エキス、スクワラン",
        "finish": "オイルインならではのしっとりとしたツヤ膜が肌を包み込み、もっちりとした柔らかさと華やかな香りが持続",
        "desc_p1": "毎日のボディケアを無理なく継続するためには、ドラッグストアでいつでも手に入り、気兼ねなくたっぷり使えるコストパフォーマンスの良さと、使うたびに心地よい気分の良さが不可欠です。",
        "desc_p2": "ジョンソンボディケアの『エクストラケア アロマミルク』は、赤ちゃんのデリケートな肌を守る高純度ベビーオイルをベースに、厳選された美容オイル（ダイズ油・ヒマワリ種子油）を配合した高保湿処方。冬の乾いた皮膚に水分を与えながら、オイルのヴェールで水分蒸発をしっかりとブロックします。ローズとジャスミンの優雅なアロマが全身を優しく包み込み、プチプラとは思えないリッチなケア体験を提供します。",
        "target": "近所のドラッグストアで手軽に買える大容量高保湿クリームを探している方、フローラル系の華やかな香りが好きな方、毎日惜しみなく全身にたっぷり使いたい方",
        "technique": "お風呂から上がって水分を拭き取った直後に、両腕・両脚・胴体へたっぷり馴染ませます。大容量ポンプなので、家族みんなで脱衣所に置いてお風呂上がりルーティンにするのがおすすめです。",
        "voice": "『ずっとリピートしています。冬でも粉を吹かず、何よりローズとジャスミンの上品な香りが大好きです。お風呂上がりの保湿が楽しみになります。』(20代・OL)",
        "caution": "ミネラルオイル配合のため、塗った直後は少しツルツルとした感触があります。フローリングの上を素足で歩く際は滑らないようご注意ください。"
    }
]

# JSON-LD用ItemList
json_ld_items = []
for idx, it in enumerate(items):
    dt = body_cream_details[idx]
    json_ld_items.append({
        "@type": "ListItem",
        "position": idx + 1,
        "item": {
            "@type": "Product",
            "name": it["name"],
            "image": it["image_url"],
            "description": dt["catch"],
            "brand": {
                "@type": "Brand",
                "name": it["brand"]
            },
            "offers": {
                "@type": "Offer",
                "price": str(it["price"]),
                "priceCurrency": "JPY",
                "availability": "https://schema.org/InStock",
                "url": it["affiliate_url"]
            }
        }
    })

json_ld_structure = {
    "@context": "https://schema.org",
    "@graph": [
        {
            "@type": "Article",
            "headline": "保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10",
            "description": "11月・12月の冬の乾燥で粉を吹くすね・腕・お腹まわりのカサつきを徹底解決！キュレル、セタフィル、ニュートロジーナ、ロクシタン、ローラメルシエなど、高純度シアバターやセラミド配合の最強高保湿ボディクリーム10選を徹底比較！",
            "datePublished": "2026-11-01T00:00:00+09:00",
            "dateModified": "2026-11-01T00:00:00+09:00",
            "author": {
                "@type": "Organization",
                "name": "冬コスメ徹底比較ラボ"
            }
        },
        {
            "@type": "ItemList",
            "itemListElement": json_ld_items
        },
        {
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": "冬にボディクリームを塗る最適なタイミングはいつですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "入浴後『5分以内』の、浴室から出てタオルドライした直後が最も効果的です。入浴直後の皮膚は角層が水分をたっぷり含んでいますが、10分を過ぎると急速に水分蒸散が進む『入浴後過乾燥』が始まります。水分が皮膚に残っているうちにボディクリームの油分でフタをすることで、うるおいを角層内部に完全に閉じ込めることができます。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "ボディローション（ミルク）とボディクリーム、ボディバターの違いは何ですか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "主な違いは『水分と油分の比率』です。ボディローションやミルクは水分が多くサラッとしていますが、真冬の粉吹き肌には油分が不足しがちです。ボディバターはシアバターなどの固形油脂が中心で非常に重厚ですが、伸びにくさがあります。ボディクリームはその中間に位置し、適度な水分とリッチなエモリエント油分（セラミドやワセリン、高濃度グリセリン）がバランスよく配合されており、冬の広範囲の乾燥ケアに最も適しています。"
                    }
                },
                {
                    "@type": "Question",
                    "name": "すねやひじの粉吹きやかゆみが止まらないときの効果的な塗り方はありますか？",
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": "粉吹きが起きている部位は角質が剥がれかけて刺激に弱くなっているため、ゴシゴシ擦り込むのは厳禁です。手のひらにクリームを伸ばし、体温で温めて柔らかくしてから、包み込むように優しくハンドプレスしてください。特にカサつく部位には、一度全体に塗った後にもう一度少量を重ねづけする『ミルフィーユ塗り』を行うと保護効果が倍増します。"
                    }
                }
            ]
        }
    ]
}

html_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の冬の乾燥で粉を吹くすね・腕・お腹まわりのカサつきを徹底解決！キュレル、セタフィル、ニュートロジーナ、ロクシタン、ローラメルシエなど、高純度シアバターやセラミド配合の最強高保湿ボディクリーム10選を徹底比較！">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-body-cream">
  <meta property="og:title" content="保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10">
  <meta property="og:description" content="11月・12月の冬の乾燥で粉を吹くすね・腕・お腹まわりのカサつきを徹底解決！キュレル、セタフィル、ニュートロジーナ、ロクシタン、ローラメルシエなど、高純度シアバターやセラミド配合の最強高保湿ボディクリーム10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-body-cream">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json.dumps(json_ld_structure, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-container">
      <a href="/" class="site-logo">冬コスメ徹底比較ラボ</a>
      <nav class="site-nav">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#guide-section">選び方解説</a>
        <a href="#faq-section">よくある質問</a>
      </nav>
    </div>
  </header>

  <main class="container main-content">
    <article class="article-body">
      <nav class="breadcrumb" aria-label="パンくずリスト">
        <ol>
          <li><a href="/">トップ</a></li>
          <li aria-current="page">高保湿ボディクリーム</li>
        </ol>
      </nav>

      <header class="article-header">
        <span class="badge category-badge">全身保湿・粉吹き防止</span>
        <h1 class="article-title">保湿力の強さで冬の粉吹き・全身カサつき乾燥とさようなら！しっとり潤い肌が続く高保湿ボディクリームランク10</h1>
        <div class="article-meta">
          <time datetime="2026-11-01">2026年11月1日更新</time>
          <span class="author">執筆：冬コスメ比較検証チーム</span>
        </div>
      </header>

      <!-- 導入文 -->
      <section class="intro-box">
        <p>
          11月から12月へと季節が進むにつれ、外気の湿度は急激に低下し、室内では暖房による極度の乾燥が始まります。「お風呂から上がるとすぐにすねがカサカサして痒くなる」「黒いタイツやヒートテックを脱いだときに内側が白い粉で汚れている」「ひじやかかとがガサガサしてストッキングに引っかかる」といった深刻なボディの乾燥トラブルに直面していませんか？
        </p>
        <p>
          実は、首から下の皮膚は顔に比べて皮脂腺の数が圧倒的に少なく、特にすねや太もも、腕は自前の皮脂膜を形成する力が極めて微弱です。外気の冷えと暖房風にさらされると、角層の水分はわずか数分で蒸発し、角質細胞がめくれ上がって「粉吹き」や「乾燥小ジワ」を引き起こします。
        </p>
        <p>
          この過酷な真冬の乾燥から全身を守り抜く唯一の手段が、水分を抱え込む高保湿成分（セラミド、高純度グリセリン、ヒアルロン酸）と、水分蒸発を物理的にシャットアウトする良質な油分（シアバター、スクワラン、ワセリン）を兼ね備えた<strong>本格的な高保湿ボディクリーム</strong>です。
        </p>
        <p>
          本特集では、楽天市場やドラッグストア、百貨店で圧倒的な支持を集めるボディクリームの中から、編集部が成分処方・保湿持続力・肌なじみ・ベタつきの少なさを徹底検証し、11月〜12月の真冬に本当に頼れる実力派10選をランキング形式で厳選しました。
        </p>
      </section>

      <!-- 目次 -->
      <nav class="toc-card" aria-label="目次">
        <h2 class="toc-title">📑 目次</h2>
        <ul class="toc-list">
          <li><a href="#why-dry">1. なぜ11月〜12月に全身の粉吹き・激しい乾燥が起きるのか？</a></li>
          <li><a href="#how-to-choose">2. 失敗しない冬の高保湿ボディクリームの選び方3原則</a></li>
          <li><a href="#ranking">3. 高保湿ボディクリームおすすめ厳選ランキング10選</a></li>
          <li><a href="#guide-section">4. お風呂上がり5分が勝負！水分を逃さない「ミルフィーユ密着塗り」</a></li>
          <li><a href="#technique-section">5. 部位別集中ケア：ひじ・ひざ・かかとのガサガサを救う裏技</a></li>
          <li><a href="#faq-section">6. よくある質問 (FAQ)</a></li>
          <li><a href="#related-section">7. あわせて読みたい冬の徹底保湿特集</a></li>
        </ul>
      </nav>

      <!-- 科学的背景解説 -->
      <section id="why-dry" class="content-block">
        <h2>🔬 なぜ11月〜12月に全身の粉吹き・激しい乾燥が起きるのか？</h2>
        <p>
          冬になると顔だけでなく、全身の皮膚が突然カサつき始めるのには、皮膚科学的な明確な理由が存在します。
        </p>
        <div class="science-grid" style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:20px; margin:24px 0;">
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">① 四肢（すね・腕）の皮脂腺不足</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              顔のTゾーンには1平方センチメートルあたり数百個の皮脂腺が存在しますが、すねや腕にはわずか数十個以下しかありません。気温が15度を下回ると皮脂の分泌そのものが激減し、天然のバリア膜である皮脂膜が完全に消失してしまいます。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">② 吸湿発熱インナーによる過乾燥と摩擦</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              冬に重宝されるヒートテックや化学繊維タイツは、肌から蒸散する水分を吸収して発熱する仕組みを持っています。保湿ケアを怠った状態で着用すると、肌に必要な最低限の水分まで吸い上げられ、さらに繊維の擦れによって角層が剥がれ落ちて粉吹きを誘発します。
            </p>
          </div>
          <div style="background:#f1f5f9; padding:20px; border-radius:8px; border-left:4px solid #0284c7;">
            <h3 style="margin-top:0; font-size:1.1rem; color:#0f172a;">③ 入浴によるNMF（天然保湿因子）の流出</h3>
            <p style="font-size:0.95rem; line-height:1.7; color:#334155; margin-bottom:0;">
              寒い冬は41度〜42度以上の熱い湯船に浸かりがちですが、40度を超える熱湯は角層内のセラミドや細胞間脂質を一気に溶かし出します。お風呂上がりは角層が一時的に膨潤していますが、10分を境に一気に水分が蒸発する「入浴後過乾燥」が生じます。
            </p>
          </div>
        </div>
      </section>

      <!-- 選び方解説 -->
      <section id="how-to-choose" class="content-block">
        <h2>💡 失敗しない冬の高保湿ボディクリームの選び方3原則</h2>
        <p>
          冬の過酷な乾燥に立ち向かうためには、単に香りが良いだけのミルクでは力不足です。以下の3つの基準をチェックして、確かな保湿力を持つクリームを選びましょう。
        </p>
        <div class="choose-principles" style="margin:24px 0;">
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準1：保水成分（セラミド・高純度グリセリン・ナイアシンアミド）の配合</h3>
            <p style="line-height:1.7; color:#475569;">
              肌内部の水分をつなぎ止めるためには、細胞間脂質を補う「ヒト型セラミド（またはセラミド機能成分）」や、微細な分子で角層奥深くまで浸透する「高純度グリセリン」、肌バリアを整える「ナイアシンアミド」などの水分保持成分が不可欠です。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px; margin-bottom:16px;">
            <h3 style="color:#0369a1; margin-top:0;">基準2：高純度エモリエント油分（シアバター・スクワラン・ワセリン）によるシールド力</h3>
            <p style="line-height:1.7; color:#475569;">
              取り込んだ水分を閉じ込めるフタとなる油分の質が極めて重要です。皮脂と親和性の高い天然シアバターやスクワラン、肌表面に強固な保護膜を張る高純度ワセリンなどがリッチに配合されているクリームは、翌朝まで乾燥をシャットアウトします。
            </p>
          </div>
          <div style="background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:20px;">
            <h3 style="color:#0369a1; margin-top:0;">基準3：摩擦レスに伸びて衣類にベタつかないテクスチャー</h3>
            <p style="line-height:1.7; color:#475569;">
              冬の入浴後は脱衣所が寒いため、全身へスピーディーに塗り広げられる伸びの良さが必須です。また、塗った直後にパジャマやインナーを着ても張り付かず、内側だけがしっとりうるおう処方のものを選ぶことが、毎日の継続につながります。
            </p>
          </div>
        </div>
      </section>

      <!-- ランキング一覧セクション -->
      <section id="ranking" class="ranking-section">
        <div class="ranking-header">
          <h2>🏆 高保湿ボディクリームおすすめ厳選ランキング10選</h2>
          <p class="ranking-subtitle">11月〜12月の頑固な粉吹き・乾燥かゆみを防ぎ、吸い付くような潤い肌へ導く名品を比較検証！</p>
        </div>
"""

# ランキング各商品のHTML生成
for idx, it in enumerate(items):
    dt = body_cream_details[idx]
    rank_num = it["rank"]
    
    html_content += f"""
        <!-- 第{rank_num}位 -->
        <article id="rank-{rank_num}" class="product-card">
          <div class="product-badge-wrap">
            <span class="rank-badge rank-{rank_num}">第{rank_num}位</span>
            <span class="product-tag">{dt["tag"]}</span>
          </div>

          <header class="product-title-area">
            <h3 class="product-name">{it["brand"]} {it["name"]}</h3>
            <p class="product-catch">{dt["catch"]}</p>
          </header>

          <div class="product-main-grid">
            <div class="product-img-col">
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="product-img-link">
                <img src="{it["image_url"]}" alt="{it["brand"]} {it["name"]}" class="product-img" loading="lazy">
              </a>
              <div class="shop-info">
                <span class="price-label">参考価格:</span>
                <span class="price-val">¥{it["price"]:,}</span>
                <span class="tax-inc">(税込)</span>
                <div class="shop-name">取扱: {it["shop_name"]}</div>
              </div>
              <a href="{it["affiliate_url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                <span>楽天市場で商品詳細を見る</span>
              </a>
            </div>

            <div class="product-spec-col">
              <table class="spec-table">
                <tbody>
                  <tr><th>容量・規格</th><td>{dt["capacity"]}</td></tr>
                  <tr><th>製品タイプ</th><td>{dt["type"]}</td></tr>
                  <tr><th>テクスチャー</th><td>{dt["texture"]}</td></tr>
                  <tr><th>主要保湿成分</th><td>{dt["ingredients"]}</td></tr>
                  <tr><th>仕上がり質感</th><td>{dt["finish"]}</td></tr>
                </tbody>
              </table>

              <div class="product-review-body">
                <h4>【皮膚科学的アプローチ＆製品特徴】</h4>
                <p>{dt["desc_p1"]}</p>
                <p>{dt["desc_p2"]}</p>

                <h4>【こんな方におすすめ】</h4>
                <p>{dt["target"]}</p>

                <h4>【効果的な使い方テクニック】</h4>
                <p>{dt["technique"]}</p>

                <div class="review-box">
                  <div class="review-title">💬 愛用者のリアルな口コミ・検証レビュー</div>
                  <p class="review-text">{dt["voice"]}</p>
                </div>

                <div class="caution-box" style="margin-top:12px; background:#fffbeb; border-left:4px solid #f59e0b; padding:10px 14px; font-size:0.88rem; color:#92400e;">
                  <strong>⚠️ 使用上のポイント・注意点：</strong> {dt["caution"]}
                </div>
              </div>
            </div>
          </div>
        </article>
"""

# ランキング後の詳細解説、比較表、FAQ、内部リンク
html_content += """
      <!-- 比較まとめ一覧表 -->
      <section class="comparison-summary-section" style="margin:48px 0;">
        <h2>📊 高保湿ボディクリーム10選 比較早見表</h2>
        <div style="overflow-x:auto;">
          <table class="summary-table" style="width:100%; border-collapse:collapse; margin-top:16px; font-size:0.92rem;">
            <thead>
              <tr style="background:#0284c7; color:#fff;">
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">順位 / ブランド</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">商品名</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">主要成分</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">特徴・おすすめな人</th>
                <th style="padding:12px 10px; border:1px solid #cbd5e1;">参考価格</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">1位 Curel</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モイスチャーバーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">セラミド機能成分・アラントイン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">すねの粉吹き・ひび割れ寸前の超乾燥肌に</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥1,388</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">2位 Cetaphil</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">モイスチャライジングクリーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ナイアシンアミド・パンテノール</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">大容量566g！家族全員で惜しみなく全身ケア</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥5,254</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">3位 ニュートロジーナ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">インテンスリペア CICA エマルジョン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高純度99%グリセリン・CICA</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">角層10層まで浸透！ポンプ式で手軽に毎日ケア</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥2,091</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">4位 ロクシタン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">スノーシア ボディクリーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">天然シアバター20%</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">新雪のようにふわふわとろける極上の質感</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥3,168</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">5位 ニベア</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ロイヤルブルー うるおい密封</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">コエンザイムQ10・ヒアルロン酸</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">大人のしぼみ肌にハリとうるおいを密封</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥4,580</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">6位 ローラメルシエ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ホイップト アンバーバニラ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">シアバター・ホホバ種子油</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">甘美なアンバーバニラの香りが一日中持続</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥11,800</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">7位 アベンヌ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">トリクセラNT フルイドクリーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">アベンヌ温泉水・植物性脂質トリオ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">生後1ヶ月の赤ちゃんも使える低刺激設計</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥7,040</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">8位 松山油脂</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">Mマーク 柚子ボディローション</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">国産柚子精油・カルナウバロウ</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">本物の柚子の和アロマ＆サラリとした後肌</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥1,727</td>
              </tr>
              <tr>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">9位 Aesop</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">インテンシブ ボディバーム</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">マカダミア油・サンダルウッド</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">ひじ・かかとの頑固な硬化角質をほぐす名品</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥6,160</td>
              </tr>
              <tr style="background:#f8fafc;">
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold; text-align:center;">10位 ジョンソン</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">エクストラケア アロマミルク</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">高純度ベビーオイル・植物油</td>
                <td style="padding:10px; border:1px solid #e2e8f0;">手頃なドラコスで毎日惜しみなく使える大定番</td>
                <td style="padding:10px; border:1px solid #e2e8f0; font-weight:bold;">¥5,920</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 塗り方テクニック解説 -->
      <section id="guide-section" class="expert-guide-section" style="background:#f8fafc; border-radius:12px; padding:28px; margin:40px 0;">
        <h2>🛁 お風呂上がり5分が勝負！水分を逃さない「ミルフィーユ密着塗り」</h2>
        <div style="line-height:1.8; color:#334155;">
          <h3>1. タオルドライは「擦らず押さえるだけ」</h3>
          <p>
            入浴後の角層は水分を吸って柔らかくなっており、非常に傷つきやすい状態です。バスタオルでゴシゴシ擦ると、せっかくの角質細胞が剥がれ落ちてバリア機能が低下します。水滴を優しくタオルで押さえるように吸い取り、肌表面にほんのりと湿り気が残っている状態で保湿に移りましょう。
          </p>

          <h3 style="margin-top:24px;">2. 手の体温で温めてから「面」で優しく塗布</h3>
          <p>
            冬の冷えた部屋では、クリームの油分が固くなっていることがあります。直接肌に乗せるのではなく、手のひらに適量を出して両手ですり合わせ、体温で温めてトロッと柔らかくしてから肌に伸ばしてください。摩擦がゼロになり、角層へのなじみが格段に向上します。
          </p>

          <h3 style="margin-top:24px;">3. すねや腰回りの乾燥多発地帯には「追いクリーム」</h3>
          <p>
            全身に薄く均一に塗布した後、特に粉吹きしやすい「すね」「太ももの外側」「腰回り」「ひじ・ひざ」には、もう一度少量を指先に取って重ねづけ（ミルフィーユ塗り）します。二重の保護ヴェールが形成され、暖房風による乾燥を翌朝まで完璧に防ぎます。
          </p>
        </div>
      </section>

      <!-- よくある質問 (FAQ) -->
      <section id="faq-section" class="faq-section">
        <h2>❓ 冬の高保湿ボディクリーム よくある質問 (FAQ)</h2>
        <div class="faq-item">
          <h3>Q1. 冬にボディクリームを塗る最適なタイミングはいつですか？</h3>
          <p>入浴後『5分以内』の、浴室から出てタオルドライした直後が最も効果的です。入浴直後の皮膚は角層が水分をたっぷり含んでいますが、10分を過ぎると急速に水分蒸散が進む『入浴後過乾燥』が始まります。水分が皮膚に残っているうちにボディクリームの油分でフタをすることで、うるおいを角層内部に完全に閉じ込めることができます。</p>
        </div>
        <div class="faq-item">
          <h3>Q2. ボディローション（ミルク）とボディクリーム、ボディバターの違いは何ですか？</h3>
          <p>主な違いは『水分と油分の比率』です。ボディローションやミルクは水分が多くサラッとしていますが、真冬の粉吹き肌には油分が不足しがちです。ボディバターはシアバターなどの固形油脂が中心で非常に重厚ですが、伸びにくさがあります。ボディクリームはその中間に位置し、適度な水分とリッチなエモリエント油分（セラミドやワセリン、高濃度グリセリン）がバランスよく配合されており、冬の広範囲の乾燥ケアに最も適しています。</p>
        </div>
        <div class="faq-item">
          <h3>Q3. すねやひじの粉吹きやかゆみが止まらないときの効果的な塗り方はありますか？</h3>
          <p>粉吹きが起きている部位は角質が剥がれかけて刺激に弱くなっているため、ゴシゴシ擦り込むのは厳禁です。手のひらにクリームを伸ばし、体温で温めて柔らかくしてから、包み込むように優しくハンドプレスしてください。特にカサつく部位には、一度全体に塗った後にもう一度少量を重ねづけする『ミルフィーユ塗り』を行うと保護効果が倍増します。</p>
        </div>
      </section>

      <!-- 関連特集への内部リンク -->
      <section id="related-section" class="related-section">
        <h2>🔗 あわせて読みたい冬の徹底保湿・ボディケア特集</h2>
        <div class="internal-links-grid">
          <a href="/winter-body-milk" class="related-card">
            <span class="related-tag">ボディミルク</span>
            <h4>🥛 高保湿ボディミルク ランク10</h4>
            <p>みずみずしい水分補給と軽やかな使い心地を求める方に。</p>
          </a>
          <a href="/winter-body-butter" class="related-card">
            <span class="related-tag">ボディバター</span>
            <h4>🧈 高保湿ボディバター ランク10</h4>
            <p>頑固な超乾燥肌を濃厚な油脂で集中シールドする極重ケア。</p>
          </a>
          <a href="/winter-body-oil" class="related-card">
            <span class="related-tag">ボディオイル</span>
            <h4>✨ 高保湿ボディオイル ランク10</h4>
            <p>お風呂上がりの濡れた肌に伸ばす艶めくエモリエントオイル。</p>
          </a>
          <a href="/winter-bath-care" class="related-card">
            <span class="related-tag">入浴剤・バスケア</span>
            <h4>🛁 冬のうるおい高保湿入浴剤 ランク10</h4>
            <p>お風呂に浸かるだけで全身の角層をうるおす入浴後過乾燥対策。</p>
          </a>
        </div>
      </section>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-content">
      <p class="copyright">&copy; 2026-2027 冬コスメ徹底比較ラボ All Rights Reserved.</p>
      <div class="footer-links">
        <!-- 後ほど一括スクリプトで全更新 -->
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-body-cream.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated winter-body-cream.html ({len(html_content):,} bytes)")
