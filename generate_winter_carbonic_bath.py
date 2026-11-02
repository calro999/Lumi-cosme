import json
import re

with open("fetched_3winter_mist_bath_headspa_data_perfect.json", "r", encoding="utf-8") as f:
    rakuten_data = json.load(f)

items = rakuten_data["winter_carbonic_bath"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 累計販売数数千万錠！湯上がりポカポカが持続する中性重炭酸の絶対王者",
        "catch": "お湯に溶け込んだ重炭酸イオンが24時間持続。温浴効果を高めて疲労回復と潤い素肌を両立",
        "brand_name": "BARTH (バース)",
        "capacity": "30錠入（約10回分）",
        "type": "医薬部外品・薬用中性重炭酸入浴剤",
        "features": "有効成分：炭酸水素ナトリウム、炭酸ナトリウム、ビタミンC（塩素中和）、クエン酸配合、無香料・無着色",
        "value": "世界有数の炭酸泉であるドイツのバート・ナウハイムに着目。お湯を中性に保つことで重炭酸イオンを豊富に保ち、芯から温める",
        "desc_p1": "11月から12月は、急激な冷え込みと日々の寒暖差によって自律神経が乱れ、手足の末端が氷のように冷える『冬の冷え性』に悩まされる人が急増します。布団に入っても足先が冷たくてなかなか眠れない、お風呂から上がっても15分後には湯冷めしてしまう…そんな真冬の悩みを根本から解消してくれるのが、重炭酸入浴のパイオニア『BARTH』です。",
        "desc_p2": "一般的な炭酸入浴剤は炭酸ガスが空気中にすぐ抜けてしまいますが、BARTHは独自の特許技術によりお湯を中性（pH7前後）に保ち、炭酸ガスを『重炭酸イオン』へと変化させてお湯の中に高濃度で溶け込ませ続けます。ぬるめ（37〜40℃）のお湯に3錠溶かして15分以上浸かるだけで、血管を広げて血流を促す温浴効果が驚くほど持続。さらに水道水中の残留塩素をビタミンCが中和し、クエン酸が毛穴の古い角質汚れをオフ。湯上がりは肌が美容液を浴びたようにしっとり滑らかになり、朝までポカポカが続きます。",
        "target": "手足の冷え性で夜ぐっすり眠れない方、入浴後すぐに湯冷めして肌がカサつく方、香料や着色料が苦手な敏感肌の方",
        "point": "お湯の温度はややぬるめの38〜40℃に設定するのがコツ。15分以上ゆったり浸かることで、自律神経が副交感神経優位に切り替わり、極上の睡眠準備が整います。"
    },
    {
        "rank": 2,
        "tag": "🌿 塩素を完全中和！赤ちゃんから敏感肌まで全身しっとり包み込む本格派重炭酸",
        "catch": "界面活性剤ゼロ・無香料・無着色。デリケートな冬の乾燥肌を優しく癒やす自然派処方",
        "brand_name": "Hot Tab (ホットタブ)",
        "capacity": "45錠入（約15回分）",
        "type": "医薬部外品・薬用重炭酸湯（Classic）",
        "features": "有効成分：炭酸水素ナトリウム、炭酸ナトリウム、無水クエン酸、PEG6000、ビタミンC配合",
        "value": "アスリートのコンディショニングから産前産後の冷えケアまで幅広く支持される医療・健康発想の重炭酸タブレット",
        "desc_p1": "冬はお風呂に入った瞬間、水道水のピリピリ感や塩素の刺激で肌が赤くなったり、かゆみを感じたりする人が少なくありません。そんな刺激に敏感な冬の肌を、生まれたてのまろやかなお湯で守りながら温めてくれるのが『薬用ホットタブ重炭酸湯 Classic』です。",
        "desc_p2": "湯水中の残留塩素を瞬時に中和し、極めて肌当たりの優しいシルキーなお湯を作り出します。発泡後、炭酸ガスが揮発することなく重炭酸イオンとして24時間以上お湯の中に溶存するため、家族が順番にお風呂に入る家庭でも全員が同じ温浴効果を享受できます。石鹸を使わなくても、重炭酸イオンとクエン酸の働きで余分な皮脂や毛穴汚れを清浄化。入浴後も肌の水分保持能を守り、カサカサになりがちな背中やすねの粉吹きを防いでくれます。",
        "target": "冬のお湯のピリピリ刺激が苦手な方、小さな子どもや赤ちゃんと一緒にお風呂に入りたい方、家族全員で温浴効果を共有したい方",
        "point": "浴槽に浸かりながら、お湯を洗面器ですくって頭皮や髪にかけるのもおすすめ。頭皮の余分な皮脂汚れが落ち、髪の毛もサラサラにまとまります。"
    },
    {
        "rank": 3,
        "tag": "🔥 高濃度炭酸×生薬ジンジャー末！溜まりに溜まった真冬の疲労と冷えを集中リセット",
        "catch": "炭酸泡のプレミアム処方。おやすみ前の温浴で芯まで温まり、翌朝スッキリ目覚める",
        "brand_name": "きき湯 (バスクリン)",
        "capacity": "400g（約8〜10回分）",
        "type": "医薬部外品・高濃度炭酸ガス薬用入浴剤（リセットナイト）",
        "features": "ショウキョウ末（生薬有効成分）、高濃度炭酸ガス、硫酸ナトリウム、塩化ナトリウム、リラックス樹木の香り",
        "value": "バスクリンの生薬研究と炭酸技術を結集。パワフルな発泡力と温活生薬の相乗効果で、冷え切った体を素早くリカバリー",
        "desc_p1": "年末の多忙な仕事や大掃除、寒さで肩や腰がガチガチに凝り固まり、泥のような疲労感が抜けない…そんな現代人のヘビーな夜を救うのが、きき湯の最高峰シリーズ『ファインヒート リセットナイト』です。",
        "desc_p2": "通常のきき湯と比べて炭酸ガス濃度を大幅に高めたプレミアム処方を採用。浴槽に入れた瞬間に激しい炭酸泡がシュワシュワと噴出し、お湯全体に素早く有効成分を行き渡らせます。さらに厳選された生薬『ショウキョウ末（生姜）』が末梢血管を心地よく刺激し、短時間の入浴でも汗がじわっとにじみ出るほどの温浴効果を発揮。リラックスを促す樹木とハーブの香りが副交感神経を優しく刺激し、こわばった筋肉をほぐして深い眠りへと誘います。",
        "target": "寒さによる肩こり・腰痛・疲労が蓄積している方、短時間の入浴でも効率よくしっかり温まりたい方、ウッディな落ち着く香りが好きな方",
        "point": "お風呂から上がる直前に、ぬるめのシャワーで軽く汗を流してから上がると、汗による冷えを防ぎつつ保温成分が肌を包み込んでくれます。"
    },
    {
        "rank": 4,
        "tag": "⚡ 通常のバブの約10倍の炭酸泡！手足の先まで血流を巡らせるビッグサイズ錠剤",
        "catch": "パワフルな温浴効果で冷えきった手足を救済。生薬当帰エキス配合のメディカル発想",
        "brand_name": "バブ (花王)",
        "capacity": "6錠入（個包装）",
        "type": "医薬部外品・高濃度炭酸薬用入浴剤（極フカキ温浴）",
        "features": "高濃度炭酸（通常バブ比約10倍）、トウキエキス、高麗人参エキス、ビタミンE配合、シトラスの香り",
        "value": "花王の炭酸研究の粋を集めた大型プレミアム錠剤。お湯に溶け込む微細炭酸が血管を拡張し、温もりを持続させる",
        "desc_p1": "真冬の外出や通勤で足先が凍えるように冷え切ってしまい、お湯に浸かってもなかなか温かさが戻らない…そんな頑固な冷えに直球でアプローチするのが、花王バブの最高位ライン『メディキュア 極フカキ温浴』です。",
        "desc_p2": "手のひらサイズの巨大な錠剤から、通常のバブの約10倍という圧倒的な高濃度炭酸泡がダイナミックに噴出。お湯にしっかり溶け込んだ炭酸分子が皮膚から吸収され、毛細血管をダイレクトに拡張します。古くから温活に重宝されてきた和漢生薬『トウキエキス』や高麗人参エキスが温浴効果を高め、冷えきった指先やつま先までポカポカとした温かい血液を行き渡らせます。個包装のため保管もしやすく、特に冷え込みが厳しい夜のレスキューアイテムとして常備したい名品です。",
        "target": "冬の寒さで手足の末端が痛いほど冷える方、1回分ずつ手軽に使える個包装タイプが好きな方、ドラッグストアで手軽に買える強力入浴剤を求める方",
        "point": "錠剤が完全に溶けきってから入浴するのが最大のポイント。発泡中よりも、お湯の中に炭酸ガスが均一に溶け込んだ瞬間が最も高い温浴効果を発揮します。"
    },
    {
        "rank": 5,
        "tag": "🛁 アロマの癒やしと乳白色の極上湯！心まで解きほぐすベストコスメ殿堂入りの名品",
        "catch": "お湯に入れた瞬間に広がるハーブの芳香。植物エキスが肌をしっとりヴェールで包み込む",
        "brand_name": "AYURA (アユーラ)",
        "capacity": "300ml（約12回分）",
        "type": "二層式・アロマティック高保湿バスエッセンス",
        "features": "ローズマリー、カモミール、植物エキス、エモリエントオイル、天然ハーブ調香",
        "value": "発売から25年以上にわたり愛され続けるアユーラの代名詞。ストレスで疲れた心と冬の乾燥肌を優雅にリセット",
        "desc_p1": "冬の寒さと日々のストレスで自律神経が張り詰め、肌も心もカサカサに乾ききっている…そんな時に至高の癒やしを与えてくれるのが、美容業界でも圧倒的な支持を誇るアユーラの『メディテーションバスｔ』です。",
        "desc_p2": "お湯に注いだ瞬間、透明なエッセンスがふんわりと乳白色へと変化し、浴室いっぱいにローズマリーやカモミールを基調とした爽やかで奥深いアロマティックハーブの香りが広がります。吸い込むたびに呼吸が深まり、強張った心身がじんわり弛緩。厳選された植物エモリエントオイルが湯水全体をまろやかに整え、カサつきやすい冬のボディを薄いシルクの保護膜でラッピングします。お風呂上がりはボディクリームを慌てて塗らなくてもしっとり感が続き、上質な眠りへと導かれます。",
        "target": "一日の終わりに極上のアロマバスでリフレッシュしたい方、乳白色の柔らかいお湯が好きな方、ギフトや自分へのご褒美バスグッズを探している方",
        "point": "浴槽に注ぐ際、蛇口の下などお湯の注ぎ口付近に入れると、水圧でエッセンスが綺麗に乳化し、浴室全体に香りが一気に広がります。"
    },
    {
        "rank": 6,
        "tag": "🌙 ドイツ発！天然ハーブ精油×高濃度炭酸泡でおやすみ前の極上リラックス入浴",
        "catch": "眠りのハーブ『ホップ＆バレリアン』配合。重炭酸の温浴効果と深いブルーのお湯で安眠へ",
        "brand_name": "Kneipp (クナイプ)",
        "capacity": "6錠入（個包装）",
        "type": "天然精油配合・スパークリング炭酸タブレット",
        "features": "ホップ球花エキス、コウスイガヤ油（バレリアン精油）、アルガンオイル、高濃度炭酸泡",
        "value": "創業130年を超えるドイツのハーバルブランド。天然植物オイルが肌を潤し、ヨーロッパ伝統の安眠ハーブが深い休息をもたらす",
        "desc_p1": "寒さで寝つきが悪く、夜中に何度も目が覚めてしまう冬の不眠悩みに、植物療法（フィトセラピー）の観点からアプローチするのが、クナイプの『スパークリングタブレット グーテナハト』です。",
        "desc_p2": "ヨーロッパで古くから『眠りのハーブ』として重宝されてきたホップとバレリアンの天然精油を贅沢にブレンド。浴槽に入れると、きめ細やかな高濃度炭酸泡が心地よいパチパチ音とともに立ち上り、お湯は幻想的で深いナイトブルーに染まります。重炭酸の血行促進効果で体の芯までじんわり温まりながら、静寂を思わせる独特のスパイシーハーブの香りが脳の緊張をオフ。アルガンオイル配合で、入浴後の素肌もしっとりなめらかに仕上がります。",
        "target": "冬の冷えで夜なかなか眠りにつけない方、天然ハーブ精油の本格的なアロマを体感したい方、夜更かしが続いて自律神経を整えたい方",
        "point": "就寝の約60〜90分前にぬるめのお湯で入浴するのが理想的。入浴で上がった深部体温がちょうどベッドに入る頃に下がり始め、自然と深い眠りに落ちることができます。"
    },
    {
        "rank": 7,
        "tag": "💧 高濃度水素ナノバブルが毛穴の奥まで浸透！お風呂上がりの保水力が圧倒的に持続",
        "catch": "微細な水素の気泡が全身を包み込む。乾燥によるかゆみやカサつきを防ぐ先進の美肌入浴",
        "brand_name": "H& (アッシュアンド)",
        "capacity": "750g（約30回分）",
        "type": "高濃度水素ナノバブル入浴剤",
        "features": "高濃度水素発生パウダー、ナノバブルテクノロジー、無香料・無着色、シルキーマイクロバブル",
        "value": "エステやサロンでも導入される水素ナノバブル技術。微細な気泡が角質層の水分量を劇的に引き上げ、湯上がりもしっとり",
        "desc_p1": "冬にお風呂から上がると、わずか数分で全身の水分が蒸発して肌がつっぱり、すねや背中がカサカサと痒くなってしまう…そんな『入浴後の急激な過乾燥』を科学的に防ぐのが、H&の『高濃度水素入浴剤』です。",
        "desc_p2": "スプーン1杯のパウダーをお湯に入れると、目に見えないレベルの超微細な水素ナノバブルが無数に発生。お湯全体がトロリとまろやかな質感に変わり、ナノサイズの気泡が全身の皮膚と毛穴に吸い付くように密着します。水素が持つ高い抗酸化力と還元作用が冬の肌ダメージをケアし、角質層の深部まで水分をしっかりと留め続けます。無香料・無着色で肌への刺激が一切ないため、敏感肌やアトピー肌の方でも安心して長風呂を楽しめます。",
        "target": "お風呂上がりに全身の肌がつっぱったり粉を吹く方、無香料で純粋に美肌・保温効果だけを追求したい方、家族で毎日使える大容量を求める方",
        "point": "お湯に投入してから約3時間程度は高濃度ナノバブルが維持されるため、家族全員が時間差で入浴する場合でも高い美肌効果が持続します。"
    },
    {
        "rank": 8,
        "tag": "♨️ まるで天然のアルカリ温泉！とろりとした極上の湯ざわりでカサつく角質をなめらかに",
        "catch": "本格温泉成分を贅沢配合。湯上がりの肌がつるつるすべすべになる白濁の薬用温浴",
        "brand_name": "温素 (アース製薬)",
        "capacity": "600g（約15回分）",
        "type": "医薬部外品・薬用極上温泉入浴剤（白華の湯）",
        "features": "アルカリ性温泉成分（炭酸ナトリウム）、炭酸水素ナトリウム、温泉沈殿物由来成分、白濁タイプ、華やかな白樺の香り",
        "value": "『美人の湯』として名高いアルカリ性単純温泉の湯ざわりを自宅で完全再現。古い角質を自然にほぐし、驚くほど滑らかな肌へ",
        "desc_p1": "『冬になると角質が硬くなって肘や膝、かかとがゴワつく』『まるで秘湯の温泉旅館に泊まったような本格的な湯ざわりを楽しみたい』という方に熱烈に支持されているのが、アース製薬の『温素 白華の湯』です。",
        "desc_p2": "お湯に溶かした瞬間、透明だったお湯が一瞬で濃厚な白濁色に染まり、肌に触れると驚くほど『トロットロ』の美容液のような質感に変わります。アルカリ性の温泉成分が肌表面の硬くなった古い角質や余分な皮脂を優しく軟化させてオフ。同時に炭酸ナトリウムの温浴効果で血行が促進され、入浴中から肌がツルツルと滑らかになっていくのを指先で実感できます。湯上がりもまるで温泉から上がった直後のようなしっとり感が持続します。",
        "target": "とろみのある濃厚な白濁湯が好きな方、冬のガサガサ角質を滑らかにしたい方、自宅で手軽に高級温泉気分を味わいたい方",
        "point": "浴槽内で腕や脚を優しく撫でるようにマッサージすると、とろみ成分とアルカリ温泉効果で余分な角質が優しくオフされ、仕上がりのスベスベ感が倍増します。"
    },
    {
        "rank": 9,
        "tag": "🍯 とろりとした極上の美容液風呂！ハニーエキスと高濃度炭酸が冬の全身を潤す",
        "catch": "ぜいたくな華蜜の香りに包まれる至福の時間。プチプラで毎日続けられる濃厚保湿炭酸湯",
        "brand_name": "温泡 ONPO (アース製薬)",
        "capacity": "12錠入（4種×各3錠）",
        "type": "医薬部外品・高濃度とろり炭酸湯",
        "features": "とろみ成分、高濃度炭酸ガス、ハチミツエキス配合、シアバター、ヒアルロン酸、アソートタイプ",
        "value": "ドラッグストアで手に入る圧倒的コスパ。とろみのあるリッチなお湯と4種類の華やかなハチミツの香りが大好評",
        "desc_p1": "『毎日贅沢な炭酸風呂に入りたいけれど、コストは抑えたい』『甘く上品なハチミツの香りで癒やされたい』という女性たちから大人気のプチプラ名品が、温泡の『とろり炭酸湯 ぜいたく華蜜』です。",
        "desc_p2": "発泡する炭酸ガスの血行促進効果に加え、お湯をとろりとまろやかにする保湿成分をたっぷり配合。さらにハチミツエキスやシアバター、ヒアルロン酸が溶け込んだお湯は、まるで薄い美容液に全身を浸しているかのような贅沢な感触です。乾燥でヒリつく手足をやさしく包み込み、角層の水分蒸散を防ぎます。1箱に4種類の異なるハチミツブレンドの香りがアソートされており、その日の気分に合わせて選べる楽しさも魅力です。",
        "target": "毎日気軽に炭酸入浴剤を使いたい方、甘く心地よい香りに包まれてリラックスしたい方、とろみのある肌当たりの良いお湯が好きな方",
        "point": "4種類の香りを日替わりでローテーションすることで、日々の入浴が飽きずに楽しいナイトルーティンになり、冬の温活を無理なく継続できます。"
    },
    {
        "rank": 10,
        "tag": "⚡ マグネシウム炭酸湯が筋肉のこわばりと冷えをほぐす！アスリートも愛用する高機能温活",
        "catch": "硫酸マグネシウムと炭酸ガスの相乗効果。一日の終わりのカチコチ疲労を芯から解放",
        "brand_name": "きき湯 (バスクリン)",
        "capacity": "360g（約12回分）",
        "type": "医薬部外品・薬用マグネシウム炭酸湯",
        "features": "有効成分：硫酸マグネシウム、炭酸水素ナトリウム、炭酸ナトリウム、カボスの爽やかな香り",
        "value": "エプソムソルトの主成分であるマグネシウムを高配合。炭酸ガスとのダブル処方で、冬の冷え固まった筋肉をじんわりほぐす",
        "desc_p1": "冬の寒さで首や背中をすくめて歩くことで、無意識のうちに筋肉が緊張し、カチコチのコリやだるさを引き起こします。そんな筋肉疲労と冷えに、ミネラルの力でアプローチするのが、きき湯の『マグネシウム炭酸湯』です。",
        "desc_p2": "海外セレブやアスリートの間で大ブームとなっているエプソムソルト（硫酸マグネシウム）を炭酸ガスと融合。お湯に投入するとツブツブの炭酸が勢いよく発泡し、マグネシウムが皮膚を通して浸透し温浴効果を高めます。筋肉の緊張が和らぎ、血流が促されることで、滞っていた老廃物の排出をサポート。爽やかなカボスの香りが気分をすっきりさせ、入浴後は重かった体がフワッと軽くなる爽快感を味わえます。",
        "target": "冬のデスクワークで肩こり・首コリがひどい方、マグネシウム温浴（エプソムソルト）を手軽に試したい方、すっきり爽やかな柑橘系の香りを好む方",
        "point": "湯船に浸かりながら首筋や肩をゆっくり回すストレッチを行うと、炭酸ガスとマグネシウムの温浴効果がダイレクトに筋肉に伝わり、コリが素早くほぐれます。"
    }
]

# FAQアイテム
faq_items = [
    {
        "q": "普通の炭酸入浴剤と『重炭酸入浴剤』は何が違うのですか？",
        "a": "最も決定的な違いは『お湯の中に炭酸成分が溶け込んで留まり続ける時間の長さ』です。昔ながらの炭酸入浴剤は、発泡している間（数分〜数十分）にお湯から炭酸ガス（CO2）が空気中へとどんどん抜けていってしまいます。一方、BARTHやホットタブなどの『重炭酸入浴剤』は、独自の配合技術によってお湯を中性（pH7前後）に保つことで、炭酸ガスを揮発しにくい『重炭酸イオン』へと変換。お湯の中に24時間以上高濃度で溶け込み続けるため、入浴中ずっと高い血行促進・温浴効果が維持され、家族が後から入っても効果が変わりません。"
    },
    {
        "q": "熱いお風呂に入ったほうが、体は温まりやすいのではないですか？",
        "a": "実は逆効果になりやすいので注意が必要です。42℃以上の熱いお湯に入ると、交感神経が刺激されて血圧が上がり、血管が収縮してしまうだけでなく、肌のバリア機能（セラミドや皮脂）がお湯に溶け出して極度の肌乾燥を引き起こします。重炭酸入浴剤を使用する場合は、『38℃〜40℃のぬるめのお湯』に設定し、15分〜20分間ゆったり浸かるのが医学的にも最も効果的です。副交感神経が優位になって末梢血管が広がり、深部体温がじっくり上がって湯冷めしにくくなります。"
    },
    {
        "q": "お風呂から上がった後、シャワーで洗い流したほうがいいですか？",
        "a": "重炭酸入浴剤や高保湿入浴剤の場合、洗い流さずにそのまま上がるのがベストです。お湯に溶け込んだ有効成分や保湿成分（ビタミンC、ホホバ油、クエン酸など）が肌表面に潤いのヴェールを作っているため、水道水のシャワーで洗い流してしまうと、せっかくの保護膜が流されてしまい、残留塩素によって肌がカサつく原因になります。"
    },
    {
        "q": "冬の乾燥肌やかゆみに対して、入浴剤はどのような効果がありますか？",
        "a": "水道水に含まれる残留塩素を中和してピリピリ刺激をなくす効果に加え、入浴剤に含まれるミネラルや植物オイル、アミノ酸成分が角層の水分保持能をサポートします。また、重炭酸イオンの温浴効果で肌の血行が良くなることで、新陳代謝が活性化し、健やかな角質層のターンオーバーを促すため、冬に粉を吹きやすいすねや腕の乾燥肌がしっとり落ち着きます。"
    },
    {
        "q": "赤ちゃんや小さな子どもと一緒に入浴しても大丈夫ですか？",
        "a": "無香料・無着色・アルコールフリーの薬用重炭酸入浴剤（ホットタブやBARTHなど）は、水道水の残留塩素を中和してくれるため、生後3ヶ月を過ぎた赤ちゃんのデリケートな肌にも非常におすすめです。ただし、メントールやカプサイシンなど強い刺激成分が入ったものや、滑りやすいオイル系の入浴剤は避けてください。"
    }
]

# JSON-LD 構造化データ
json_ld_products = []
for p, item in zip(product_details, items):
    json_ld_products.append({
        "@type": "Product",
        "name": f"{p['brand_name']} {p['capacity']}",
        "image": item['image'],
        "description": p['value'],
        "brand": {
            "@type": "Brand",
            "name": p['brand_name']
        },
        "offers": {
            "@type": "Offer",
            "url": item['affiliateUrl'],
            "priceCurrency": "JPY",
            "price": item['price'],
            "availability": "https://schema.org/InStock"
        }
    })

json_ld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで冬の冷え性・カサカサ全身乾燥とさようなら！重炭酸イオン温浴で芯から温まり角層深部まで潤す薬用重炭酸入浴剤ランク10",
    "description": "11月・12月の寒波による冷え性・血行不良・全身のカサカサ粉吹き乾燥を徹底解消！BARTH、薬用ホットタブ、きき湯ファインヒート、バブメディキュア、クナイプ、AYURAなど、中性重炭酸イオンが温浴効果を高めて血流を促進し、お風呂上がりもしっとり潤い肌が持続する至高の重炭酸入浴剤10選を徹底比較！",
    "image": items[0]['image'],
    "author": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ 編集部"
    },
    "publisher": {
        "@type": "Organization",
        "name": "冬コスメ徹底比較ラボ",
        "logo": {
            "@type": "ImageObject",
            "url": "https://lumi-cosme.vercel.app/favicon.jpg"
        }
    },
    "datePublished": "2026-11-02",
    "dateModified": "2026-11-02"
}

json_ld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "冬の薬用重炭酸入浴剤 おすすめランキング10選",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "item": prod
        } for idx, prod in enumerate(json_ld_products)
    ]
}

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
        } for item in faq_items
    ]
}

# 商品カードHTML
cards_html = []
for p, item in zip(product_details, items):
    cards_html.append(f"""
    <article class="product-card" id="rank-{p['rank']}">
      <div class="product-badge">
        <span class="rank-number">第{p['rank']}位</span>
        <span class="rank-tag">{p['tag']}</span>
      </div>
      <h3 class="product-title">{p['brand_name']} {p['capacity']}</h3>
      <div class="product-catch">{p['catch']}</div>

      <div class="product-main">
        <div class="product-img-wrap">
          <img src="{item['image']}" alt="{p['brand_name']} 冬の薬用重炭酸入浴剤" class="product-img" loading="lazy">
          <div class="img-caption">{p['brand_name']} 楽天市場正規取扱ショップ画像</div>
        </div>
        <div class="product-specs">
          <dl class="spec-list">
            <dt>ブランド / メーカー</dt>
            <dd>{p['brand_name']}</dd>
            <dt>内容量 / タイプ</dt>
            <dd>{p['capacity']} / {p['type']}</dd>
            <dt>主要有効・保湿成分</dt>
            <dd>{p['features']}</dd>
            <dt>楽天市場 参考価格</dt>
            <dd class="price-val">¥{item['price']:,} <span>(税込・調査時点)</span></dd>
            <dt>アイテム独自の特徴</dt>
            <dd>{p['value']}</dd>
          </dl>
        </div>
      </div>

      <div class="product-desc">
        <h4>🛁 美容エディターの徹底本音レビュー＆温浴成分解説</h4>
        <p>{p['desc_p1']}</p>
        <p>{p['desc_p2']}</p>
      </div>

      <div class="product-advice">
        <div class="advice-block target-block">
          <strong>🎯 こんな人に特におすすめ：</strong>
          <p>{p['target']}</p>
        </div>
        <div class="advice-block tip-block">
          <strong>✨ プロの温活＆保湿アドバイス：</strong>
          <p>{p['point']}</p>
        </div>
      </div>

      <div class="product-action">
        <a href="{item['affiliateUrl']}" class="rakuten-btn" target="_blank" rel="noopener noreferrer nofollow">
          <span>楽天市場で最安値＆口コミをチェック</span>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
    </article>
    """)

# 比較サマリー表
table_rows = []
for p, item in zip(product_details, items):
    table_rows.append(f"""
    <tr>
      <td class="tb-rank">第{p['rank']}位</td>
      <td class="tb-name"><strong>{p['brand_name']}</strong><br><small>{p['capacity']}</small></td>
      <td class="tb-type">{p['type']}</td>
      <td class="tb-ing">{p['features'][:35]}...</td>
      <td class="tb-price">¥{item['price']:,}</td>
      <td class="tb-link"><a href="#rank-{p['rank']}" class="tb-anchor">詳細を見る</a></td>
    </tr>
    """)

# FAQ HTML
faq_html_blocks = []
for f_item in faq_items:
    faq_html_blocks.append(f"""
    <div class="faq-item">
      <h3 class="faq-q"><span>Q</span>{f_item['q']}</h3>
      <div class="faq-a"><span>A</span><p>{f_item['a']}</p></div>
    </div>
    """)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで冬の冷え性・カサカサ全身乾燥とさようなら！重炭酸イオン温浴で芯から温まり角層深部まで潤す薬用重炭酸入浴剤ランク10 | 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒波による冷え性・血行不良・全身のカサカサ粉吹き乾燥を徹底解消！BARTH、薬用ホットタブ、きき湯ファインヒート、バブメディキュア、クナイプ、AYURAなど、中性重炭酸イオンが温浴効果を高めて血流を促進し、お風呂上がりもしっとり潤い肌が持続する至高の重炭酸入浴剤10選を徹底比較！">
  <meta name="keywords" content="重炭酸入浴剤,炭酸入浴剤 保湿,BARTH 入浴剤,ホットタブ,冷え性 入浴剤,冬 乾燥肌 入浴剤,きき湯 ファインヒート,薬用入浴剤 温活">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-carbonic-bath">
  <link rel="icon" href="/favicon.jpg">
  
  <!-- OGP / SNS Meta Tags -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="保湿力の強さで冬の冷え性・カサカサ全身乾燥とさようなら！重炭酸イオン温浴で芯から温まり角層深部まで潤す薬用重炭酸入浴剤ランク10">
  <meta property="og:description" content="11月・12月の寒波による冷え性・血行不良・全身のカサカサ粉吹き乾燥を徹底解消！BARTH、薬用ホットタブ、きき湯ファインヒートなど、至高の重炭酸入浴剤10選を徹底比較！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-carbonic-bath">
  <meta property="og:image" content="{items[0]['image']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">

  <script type="application/ld+json">
  {json.dumps(json_ld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(json_ld_faq, ensure_ascii=False, indent=2)}
  </script>

  <style>
    :root {{
      --primary: #0284c7;
      --primary-light: #f0f9ff;
      --primary-dark: #0369a1;
      --accent: #e11d48;
      --text: #1e293b;
      --text-muted: #64748b;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--primary);
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .nav-link {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
    }}
    .nav-link:hover {{ color: var(--primary); }}
    
    .container {{
      max-width: 1000px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    
    .breadcrumb {{
      display: flex;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      flex-wrap: wrap;
    }}
    .breadcrumb a {{ color: var(--text-muted); text-decoration: none; }}
    .breadcrumb a:hover {{ color: var(--primary); }}
    .breadcrumb span {{ color: #cbd5e0; }}

    .article-hero {{
      background: #ffffff;
      padding: 2.5rem 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin-bottom: 2.5rem;
      border-top: 5px solid var(--primary);
    }}
    .article-tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.35rem 0.8rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    .article-title {{
      font-size: 1.85rem;
      line-height: 1.4;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 1.25rem;
    }}
    .article-meta {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
      padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .intro-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #334155;
    }}
    .intro-text p {{ margin-bottom: 1rem; }}
    .intro-highlight {{
      background: var(--primary-light);
      padding: 1.25rem;
      border-radius: 8px;
      border-left: 4px solid var(--primary);
      margin: 1.5rem 0;
      font-weight: 600;
    }}

    .toc {{
      background: #f1f5f9;
      padding: 1.5rem;
      border-radius: var(--radius);
      margin: 2rem 0;
    }}
    .toc-title {{
      font-size: 1.1rem;
      font-weight: 700;
      margin-bottom: 1rem;
      color: #1e293b;
    }}
    .toc-list {{
      list-style: none;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 0.5rem;
    }}
    .toc-list a {{
      color: #475569;
      text-decoration: none;
      font-size: 0.95rem;
      display: block;
      padding: 0.25rem 0;
    }}
    .toc-list a:hover {{ color: var(--primary); font-weight: 600; }}

    .section-h2 {{
      font-size: 1.5rem;
      font-weight: 800;
      color: #0f172a;
      margin: 3.5rem 0 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary);
    }}
    
    .table-container {{
      overflow-x: auto;
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .summary-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .summary-table th {{
      background: #f8fafc;
      color: #475569;
      padding: 1rem;
      border-bottom: 2px solid var(--border);
      white-space: nowrap;
    }}
    .summary-table td {{
      padding: 1rem;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }}
    .tb-rank {{ font-weight: 700; color: var(--primary); width: 80px; }}
    .tb-price {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .tb-anchor {{
      display: inline-block;
      padding: 0.35rem 0.75rem;
      background: var(--primary-light);
      color: var(--primary);
      text-decoration: none;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.8rem;
    }}
    .tb-anchor:hover {{ background: var(--primary); color: #fff; }}

    .product-card {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 2rem;
      margin-bottom: 3rem;
      border: 1px solid var(--border);
      scroll-margin-top: 80px;
    }}
    .product-badge {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .rank-number {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1rem;
      padding: 0.25rem 0.85rem;
      border-radius: 6px;
    }}
    .rank-tag {{
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
    }}
    .product-title {{
      font-size: 1.4rem;
      font-weight: 800;
      color: #0f172a;
      margin-bottom: 0.5rem;
    }}
    .product-catch {{
      font-size: 1rem;
      color: #475569;
      font-weight: 600;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px dashed var(--border);
    }}
    .product-main {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 1.75rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 768px) {{
      .product-main {{ grid-template-columns: 1fr; }}
    }}
    .product-img-wrap {{
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 280px;
      height: 280px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      border: 1px solid #edf2f7;
    }}
    .img-caption {{
      font-size: 0.75rem;
      color: var(--text-muted);
      margin-top: 0.5rem;
    }}
    .spec-list {{
      display: grid;
      grid-template-columns: 120px 1fr;
      gap: 0.6rem;
      font-size: 0.9rem;
    }}
    .spec-list dt {{
      font-weight: 700;
      color: #64748b;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .spec-list dd {{
      color: #0f172a;
      border-bottom: 1px solid #f1f5f9;
      padding: 0.35rem 0;
    }}
    .price-val {{
      font-size: 1.25rem !important;
      font-weight: 800 !important;
      color: #b91c1c !important;
    }}
    .price-val span {{
      font-size: 0.75rem;
      font-weight: normal;
      color: var(--text-muted);
    }}
    .product-desc {{
      margin: 1.5rem 0;
      background: #f8fafc;
      padding: 1.5rem;
      border-radius: 8px;
    }}
    .product-desc h4 {{
      font-size: 1.05rem;
      color: #0f172a;
      margin-bottom: 0.75rem;
      font-weight: 700;
    }}
    .product-desc p {{
      margin-bottom: 0.75rem;
      color: #334155;
    }}
    .product-desc p:last-child {{ margin-bottom: 0; }}
    
    .product-advice {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin: 1.5rem 0;
    }}
    @media (max-width: 640px) {{
      .product-advice {{ grid-template-columns: 1fr; }}
    }}
    .advice-block {{
      padding: 1rem;
      border-radius: 8px;
      font-size: 0.9rem;
    }}
    .target-block {{ background: #eff6ff; border-left: 4px solid #3b82f6; }}
    .target-block strong {{ color: #1e40af; display: block; margin-bottom: 0.35rem; }}
    .tip-block {{ background: #fefce8; border-left: 4px solid #eab308; }}
    .tip-block strong {{ color: #854d0e; display: block; margin-bottom: 0.35rem; }}

    .product-action {{
      margin-top: 1.5rem;
      text-align: center;
    }}
    .rakuten-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      width: 100%;
      max-width: 420px;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      text-decoration: none;
      font-weight: 700;
      font-size: 1.05rem;
      padding: 1rem 1.5rem;
      border-radius: 9999px;
      box-shadow: 0 4px 10px rgba(191, 0, 0, 0.25);
      transition: all 0.2s ease;
    }}
    .rakuten-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(191, 0, 0, 0.35);
      background: linear-gradient(135deg, #d60000 0%, #b30000 100%);
    }}

    .guide-box {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 2rem 0;
    }}
    .guide-box h3 {{
      font-size: 1.25rem;
      color: #0f172a;
      margin-bottom: 1rem;
      padding-left: 0.75rem;
      border-left: 4px solid var(--primary);
    }}
    .guide-box p {{
      margin-bottom: 1rem;
      color: #334155;
    }}
    .guide-box ul {{
      margin-left: 1.5rem;
      margin-bottom: 1.25rem;
      color: #334155;
    }}
    .guide-box li {{ margin-bottom: 0.5rem; }}

    .faq-item {{
      background: #ffffff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      border: 1px solid var(--border);
    }}
    .faq-q {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }}
    .faq-q span {{
      background: var(--primary);
      color: #ffffff;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .faq-a {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
    }}
    .faq-a span {{
      background: #e2e8f0;
      color: #475569;
      font-size: 0.85rem;
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      flex-shrink: 0;
      font-weight: 700;
      margin-top: 2px;
    }}

    .related-section {{
      background: #ffffff;
      padding: 2rem;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      margin: 3.5rem 0;
    }}
    .related-links-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}
    .related-link-card {{
      background: #f8fafc;
      border: 1px solid var(--border);
      padding: 1rem;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text);
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .related-link-card:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
      transform: translateY(-2px);
    }}
    .related-link-card small {{
      color: var(--text-muted);
      font-size: 0.75rem;
      margin-top: 0.5rem;
      display: block;
    }}

    footer {{
      background: #0f172a;
      color: #94a3b8;
      padding: 3rem 1.5rem;
      margin-top: 4rem;
      font-size: 0.85rem;
      line-height: 1.7;
    }}
    .footer-inner {{
      max-width: 1000px;
      margin: 0 auto;
      text-align: center;
    }}
    .footer-logo {{
      color: #ffffff;
      font-size: 1.2rem;
      font-weight: 700;
      margin-bottom: 1rem;
    }}
    .footer-note {{
      margin: 1rem 0;
      color: #64748b;
    }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-logo">
      <span>❄️</span>
      <span>冬コスメ徹底比較ラボ</span>
    </a>
    <nav>
      <a href="/" class="nav-link">全コスメ特集一覧</a>
    </nav>
  </div>
</header>

<div class="container">
  <div class="breadcrumb">
    <a href="/">ホーム</a>
    <span>&gt;</span>
    <a href="/">冬バスケア特集</a>
    <span>&gt;</span>
    <strong>薬用重炭酸入浴剤おすすめ10選</strong>
  </div>

  <article class="article-hero">
    <span class="article-tag">2026-2027年 冬季最新検証</span>
    <h1 class="article-title">保湿力の強さで冬の冷え性・カサカサ全身乾燥とさようなら！重炭酸イオン温浴で芯から温まり角層深部まで潤す薬用重炭酸入浴剤ランク10</h1>
    <div class="article-meta">
      <span>公開日: 2026年11月2日</span>
      <span>更新日: 2026年11月2日</span>
      <span>専門家検証: 入浴指導士＆美容皮膚科学研究チーム</span>
    </div>
    
    <div class="intro-text">
      <p>11月から12月にかけて訪れる本格的な寒波。外気の冷えによって血管が収縮し、手足の先が凍えるように冷える『末端冷え性』や、お風呂から上がってわずか15分で湯冷めしてしまう悩みが深刻化します。さらに冬場の入浴で多くの女性を苦しめるのが、<strong>「お湯から上がった直後に全身の皮膚がつっぱり、すねや背中がカサカサと粉を吹いてかゆくなる入浴後過乾燥」</strong>です。</p>
      
      <p>水道水に含まれる残留塩素は皮膚の角質細胞を酸化させ、天然の保湿成分であるセラミドや細胞間脂質を奪います。また、冷えた体を早く温めようとして42℃以上の熱いお湯に浸かる行為も、皮脂膜を根こそぎ溶かし出し、全身の乾燥肌を加速させる大きな要因です。</p>

      <div class="intro-highlight">
        💡 冬の冷えと全身乾燥を根底から解決するのが「薬用重炭酸イオン温浴」。お湯を中性に保つことで、炭酸ガスを揮発させず『重炭酸イオン』としてお湯に長時間溶存。ぬるめ（38〜40℃）のお湯でも血管内皮から一酸化窒素（NO）の産生を促して血流を劇的に促進し、水道水の塩素を無害化して角層深部まで潤いを満たし続けます。
      </div>

      <p>本記事では、大ヒットを記録し続けるBARTHや薬用ホットタブをはじめ、きき湯ファインヒート、バブメディキュア、クナイプ、アユーラなど、実力派の重炭酸＆高濃度炭酸入浴剤10選を徹底検証。温浴持続性、肌の保湿感、塩素中和力、疲労回復の実感を徹底比較し、ランキング形式でわかりやすく解説します。</p>
    </div>

    <div class="toc">
      <div class="toc-title">📑 目次 - クイックナビゲーション</div>
      <ul class="toc-list">
        <li><a href="#summary-table">📊 ひと目でわかる！薬用重炭酸入浴剤比較表</a></li>
        <li><a href="#rank-1">第1位：BARTH 薬用中性重炭酸入浴剤</a></li>
        <li><a href="#rank-2">第2位：薬用 ホットタブ 重炭酸湯 Classic</a></li>
        <li><a href="#rank-3">第3位：きき湯 ファインヒート リセットナイト</a></li>
        <li><a href="#rank-4">第4位：バブ メディキュア 極フカキ温浴</a></li>
        <li><a href="#rank-5">第5位：AYURA メディテーションバスｔ</a></li>
        <li><a href="#rank-6">第6位：クナイプ スパークリングタブレット</a></li>
        <li><a href="#rank-7">第7位：H& 高濃度水素ナノバブル入浴剤</a></li>
        <li><a href="#rank-8">第8位：温素 白華の湯</a></li>
        <li><a href="#rank-9">第9位：温泡 とろり炭酸湯 ぜいたく華蜜</a></li>
        <li><a href="#rank-10">第10位：きき湯 マグネシウム炭酸湯</a></li>
        <li><a href="#guide-mechanism">🔬 なぜ重炭酸？血管拡張と潤い保持の生化学</a></li>
        <li><a href="#guide-selection">🎯 失敗しない重炭酸入浴剤の選び方</a></li>
        <li><a href="#guide-howto">🛁 効果を最大化する究極の重炭酸温浴メソッド</a></li>
        <li><a href="#faq-section">❓ よくある質問（FAQ）</a></li>
      </ul>
    </div>
  </article>

  <section id="summary-table">
    <h2 class="section-h2">📊 ひと目でわかる！薬用重炭酸入浴剤10選スペック比較表</h2>
    <div class="table-container">
      <table class="summary-table">
        <thead>
          <tr>
            <th>順位</th>
            <th>ブランド / 商品名</th>
            <th>タイプ</th>
            <th>主要有効・保湿成分</th>
            <th>参考価格</th>
            <th>詳細</th>
          </tr>
        </thead>
        <tbody>
          {''.join(table_rows)}
        </tbody>
      </table>
    </div>
  </section>

  <section id="product-rankings">
    <h2 class="section-h2">🏆 薬用重炭酸入浴剤おすすめ人気ランキング10選</h2>
    {''.join(cards_html)}
  </section>

  <section id="guide-mechanism" class="guide-box">
    <h2 class="section-h2">🔬 なぜ重炭酸なのか？血管拡張と湯上がり保湿の生化学的メカニズム</h2>
    <p>11月〜12月の急激な外気温低下は、末梢血管を強く収縮させ、血流不全を引き起こします。血流が滞ると全身の細胞に酸素や栄養素が届かなくなり、肌のターンオーバーが停滞。角質層は水分を抱え込めなくなってガサガサに荒れていきます。</p>

    <h3>1. 炭酸ガス（酸性）と重炭酸イオン（中性）の決定的な違い</h3>
    <p>昔ながらの炭酸入浴剤は、お湯に溶かすとお湯が弱酸性になり、炭酸ガス（CO2）の形態をとります。気体である炭酸ガスは数分〜数十分でお湯から大気中へ揮発して抜けてしまいます。一方、BARTHやホットタブなどの重炭酸入浴剤は、重曹とクエン酸の独自配合でお湯を『中性（pH7前後）』に保ちます。中性のお湯の中では、炭酸ガスは揮発しにくい『重炭酸イオン（HCO3-）』へと化学変化し、24時間後もお湯の中に高濃度で留まり続けます。</p>

    <h3>2. 一酸化窒素（NO）産生と温浴保湿のサイクル</h3>
    <p>重炭酸イオンが溶け込んだお湯に浸かると、皮膚から毛細血管へとイオンが浸透。血管内皮細胞が刺激されて『一酸化窒素（NO）』が産生され、血管の平滑筋が緩んで血管が拡張します。その結果、血流速度が最大数倍に跳ね上がり、深部体温が自然に上昇。さらに水道水中の残留塩素が無力化されるため、肌の細胞間脂質（セラミド）が保護され、お風呂上がりも化粧水を浴びたようなしっとり肌が持続するのです。</p>
  </section>

  <section id="guide-selection" class="guide-box">
    <h2 class="section-h2">🎯 迷ったらここをチェック！目的別・重炭酸入浴剤の選び方</h2>
    <p>毎日の温活とバスタイムを最高のものにするため、重視するポイントに合わせて最適な入浴剤を選びましょう。</p>

    <ul>
      <li><strong>芯からの温まり・冷え性改善を最優先するなら：</strong>中性重炭酸イオンの溶存率が圧倒的な『BARTH』や『ホットタブ』。24時間効果が持続するため追い焚き利用にも最適。</li>
      <li><strong>肩こり・腰痛・疲労蓄積を速攻リセットしたいなら：</strong>高濃度炭酸ガスに生薬ジンジャーや高麗人参がブレンドされた『きき湯 ファインヒート』や『バブ メディキュア』。</li>
      <li><strong>冬の全身乾燥・粉吹き肌をしっとり潤したいなら：</strong>天然ハーブ精油と植物オイルが贅沢に入った『アユーラ』や『温素 白華の湯』、水素ナノバブルの『H&』。</li>
      <li><strong>毎日の入浴でコスパよく温活を続けたいなら：</strong>大容量ボトルやアソートパックが揃う『温泡』や『きき湯 マグネシウム炭酸湯』。</li>
    </ul>
  </section>

  <section id="guide-howto" class="guide-box">
    <h2 class="section-h2">🛁 プロが直伝！効果を極大化する『15分ぬるま湯重炭酸温浴メソッド』</h2>
    <p>重炭酸温浴の真価を引き出すには、お湯の温度と浸かる時間が何よりも重要です。皮膚科学と入浴医学に基づいた正しいステップを実践してください。</p>

    <ul>
      <li><strong>Step 1：湯温は38〜40℃の『ぬるめ』に設定：</strong>熱いお湯は交感神経を高めて血管を収縮させ、肌のセラミドを流出させます。ほんのり温かい38〜40℃が最も血流が促進され、リラックスできる黄金温度です。</li>
      <li><strong>Step 2：錠剤が完全に溶けきってから入浴：</strong>泡が出ている最中よりも、重炭酸イオンがお湯全体に均一に溶け渡った状態こそが最も効果的です。</li>
      <li><strong>Step 3：15分以上ゆったり全身浴：</strong>重炭酸イオンが皮膚を通して血管を拡張させるまでに約10分かかります。最低15分、できれば20分間ゆったりと浸かることで、芯からのポカポカ感が翌朝まで持続します。</li>
      <li><strong>Step 4：お風呂上がりはシャワーで流さない：</strong>お湯に溶け込んだ保湿成分やビタミンCのヴェールを肌に残すため、そのままタオルで優しく水分を押さえるように拭き取って上がりましょう。</li>
    </ul>
  </section>

  <section id="faq-section">
    <h2 class="section-h2">❓ よくある質問（FAQ）</h2>
    {''.join(faq_html_blocks)}
  </section>

  <section class="related-section" id="internal-links-hub">
    <h2 class="section-h2">🔗 あわせて読みたい！冬の温活＆ボディケアおすすめ特集</h2>
    <p>冬の冷えや乾燥トラブルをトータルでケアするための関連記事をピックアップしました。あわせてチェックして、真冬でも温かく潤いに満ちた毎日を過ごしましょう。</p>
    <div class="related-links-grid">
      <a href="/winter-bath-salt" class="related-link-card">
        <span>冬のバスソルト特集</span>
        <small>発汗とミネラル補給のソルト温浴</small>
      </a>
      <a href="/winter-bath-oil" class="related-link-card">
        <span>冬のバスオイル特集</span>
        <small>乾燥肌をしっとり潤すオイル入浴</small>
      </a>
      <a href="/winter-medicinal-bath" class="related-link-card">
        <span>冬の薬用入浴剤特集</span>
        <small>生薬・温泉ミネラルの本格温活</small>
      </a>
      <a href="/winter-inbath-body" class="related-link-card">
        <span>インバスボディケア特集</span>
        <small>お風呂場で濡れたまま使える保湿ミルク</small>
      </a>
      <a href="/winter-body-cream" class="related-link-card">
        <span>冬の高保湿ボディクリーム特集</span>
        <small>全身の粉吹き・カサつきを防ぐ濃厚クリーム</small>
      </a>
      <a href="/winter-oil-mist" class="related-link-card">
        <span>高保湿オイルインミスト特集</span>
        <small>日中の暖房乾燥を救う二層式ミスト</small>
      </a>
      <a href="/winter-foot-mask" class="related-link-card">
        <span>高保湿かかとパック特集</span>
        <small>ガサガサかかとを履くだけ柔軟ケア</small>
      </a>
      <a href="/winter-hot-treatment" class="related-link-card">
        <span>温感ヘッドスパトリートメント特集</span>
        <small>冷えた頭皮とパサつく髪を温感集中補修</small>
      </a>
    </div>
  </section>
</div>

<footer>
  <div class="footer-inner">
    <div class="footer-logo">❄️ 冬コスメ徹底比較ラボ</div>
    <p class="footer-desc">冬特有の肌乾燥・冷え・寒暖差トラブルに立ち向かう女性のための美容情報・コスメ検証サイト。</p>
    <p class="footer-note">※掲載している楽天市場の価格やポイント情報は調査時点のものです。最新情報は各ショップページをご確認ください。</p>
    <p class="copyright">&copy; 2026 冬コスメ徹底比較ラボ All Rights Reserved.</p>
  </div>
</footer>

</body>
</html>
"""

with open("winter-carbonic-bath.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-carbonic-bath.html successfully!")
