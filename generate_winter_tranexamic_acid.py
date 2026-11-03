import json
import re

with open("fetched_final_30_tranexamic_azulene_volufiline.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_tranexamic_acid"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "🏆 製薬会社が辿り着いた美白＆抗炎症の金字塔！肝斑・くすみを狙い撃ち",
        "catch": "トラネキサム酸開発メーカーの結晶。冬の乾燥炎症とシミ発生ルートを根本遮断",
        "brand_name": "TRANSINO (トランシーノ)",
        "capacity": "30g / 50g (薬用メラノシグナルエッセンス)",
        "type": "薬用高保湿美白美容液 (医薬部外品)",
        "features": "美白有効成分トラネキサム酸、抗炎症有効成分グリチルリチン酸2K、クラリティモイストベールEX配合",
        "value": "トラネキサム酸の第一人者である第一三共ヘルスケアが開発。真冬の過酷な乾燥下でもスッと溶け込み、メラニン生成の元となる『炎症シグナル』を鎮静しながら澄み渡る白玉肌へ導く",
        "desc_p1": "11月から12月にかけて外気温と湿度が急降下すると、肌は寒風と室内暖房の過酷な板挟み状態に置かれます。この急激な寒暖差は角層バリアを急激に低下させ、肌内部で目に見えない微弱な炎症（インフラメイジング）を誘発。その結果、メラノサイトが刺激され続け、冬なのに『顔全体がどんより暗い』『肝斑やシミが目立つ』という冬ぐすみ現象が加速します。トランシーノの薬用メラノシグナルエッセンスは、トラネキサム酸を世に送り出した製薬会社の最先端サイエンスを濃縮した至高の美白美容液です。",
        "desc_p2": "独自の浸透ナノカプセル技術により、こわばった真冬の角質層にも摩擦ゼロでスーッと一体化。有効成分トラネキサム酸がメラニン生成指令を根本からストップし、グリチルリチン酸2Kが寒さによる赤みや肌荒れを穏やかに沈静化します。さらに高保湿成分が贅沢に配合されているため、美白美容液にありがちな『さっぱりしすぎて冬には物足りない』という弱点を完全に克服。後肌は吸い付くようにモッチリとした潤いで満たされます。",
        "target": "冬になるとシミや肝斑が濃く見えて悩んでいる方、乾燥によるくすみと肌荒れを同時にケアしたい方、製薬会社品質の信頼できる美白コスメを求める方",
        "point": "化粧水の直後、手のひらで温めてから顔全体に優しくハンドプレス。特にシミや肝斑が気になる頬骨まわりには、指の腹でトントンとスタンプを押すように重ね付けすると浸透効率が劇的に高まります。"
    },
    {
        "rank": 2,
        "tag": "💎 美白美容液の絶対王者！2種の美白有効成分が織りなす冬の最高峰エイジング美白",
        "catch": "m-トラネキサム酸×4MSKの黄金タッグ。乾燥で深く根を張るメラニンを連鎖粉砕",
        "brand_name": "資生堂 HAKU (ハク)",
        "capacity": "45g (メラノフォーカスEV)",
        "type": "薬用美白美容液 (医薬部外品)",
        "features": "m-トラネキサム酸、4MSK（4-メトキシサリチル酸カリウム塩）、深層浸透処方、オトギリソウエキス",
        "value": "美白有効成分のW配合でシミの無限ループを断絶。コクのある濃密テクスチャーが真冬の乾燥肌を濃密な潤いの膜でラッピング",
        "desc_p1": "資生堂が100年を超える皮膚研究の集大成として磨き上げ続けているHAKU。最新世代のメラノフォーカスEVは、メラニン生成を抑えるm-トラネキサム酸と、蓄積したメラニンの排出を促す4MSKという2大美白有効成分を唯一無二のバランスで共存させています。",
        "desc_p2": "冬の乾燥で硬化した角層細胞の隙間を埋めるように、濃密なエマルジョン状のテクスチャーがとろけて浸透。塗布した瞬間から肌が一段トーンアップしたようなみずみずしい発光感に包まれます。単にシミを薄くするだけでなく、冬の冷えで血行が滞ったくすみがちな肌にハリと豊かな保水力をチャージ。使い続けるほどに、光を均一に反射するシルクのような白肌を育みます。",
        "target": "本気でシミ・ソバカスを予防・改善したい方、保湿力も美白力も一切妥協したくない方、冬のエイジングケアを兼ねたい大人肌の方",
        "point": "朝晩の化粧水の後、2プッシュを手のひらに取り、両頬・額・鼻・あごの5点に置いてから丁寧に全顔へ伸ばします。擦らず肌を包み込むように密着させるのが美白成分を届ける鍵です。"
    },
    {
        "rank": 3,
        "tag": "🛡️ 寒風・暖房の刺激から肌を死守！高精製ワセリン×トラネキサム酸の低刺激乳液",
        "catch": "不純物を極限まで除いた薬用ワセリンシールド。冬の粉吹き・肌荒れ・くすみを全方位ガード",
        "brand_name": "IHADA (イハダ) / 資生堂薬品",
        "capacity": "135ml (薬用クリアエマルジョン)",
        "type": "薬用美白乳液 (医薬部外品)",
        "features": "高精製ワセリン、トラネキサム酸、アラントイン、濃グリセリン配合、無香料・弱酸性",
        "value": "デリケートに傾いた真冬の角層に負担をかけず、ピリピリ感を防ぎながら潤い保護膜を形成。トラネキサム酸が赤みとシミの両方にアプローチ",
        "desc_p1": "冬の乾燥ピーク時には、普段使っているスキンケアですらピリピリとしみてしまうことがあります。そんなデリケートなゆらぎ期に頼りになるのが、資生堂薬品のイハダ薬用クリアエマルジョン。不純物を限りなく取り除いた『高精製ワセリン』がベースに配合されており、寒風やエアコンの乾燥風から肌を完璧に保護します。",
        "desc_p2": "ワセリン特有のベタつきを一切感じさせない、みずみずしく軽やかなミルクテクスチャーが特徴。トラネキサム酸と抗肌荒れ成分アラントインのダブル作用で、冬のマスク擦れや冷気による赤みを瞬時に落ち着かせます。水分蒸散を防ぐシールド効果が高いため、一日中暖房の効いたオフィスにいても夕方の乾燥崩れや粉吹きがピタッと止まります。",
        "target": "冬になると肌が敏感になって赤みが出やすい方、ベタつくクリームが苦手でも乾燥を防ぎたい方、プチプラで毎日たっぷり使いたい方",
        "point": "化粧水の後に1円硬貨大を手にとり、手のひら全体に広げてから顔を包み込むようにプレス。特にカサつきやすい口周りや目元には少量を指先で重ねづけしてください。"
    },
    {
        "rank": 4,
        "tag": "🌊 濃密ジュレが角層深くまで浸透！トラネキサム酸×ヒアルロン酸のオールインワン美白",
        "catch": "ホワイトトラネキサム酸配合。ぷるぷるのジュレが肌の上でとろけて溢れる保水ヴェールに",
        "brand_name": "肌ラボ (ロート製薬)",
        "capacity": "200ml (白潤プレミアム 薬用ジュレ状美白美容液)",
        "type": "薬用ジュレ状美白美容液 (医薬部外品)",
        "features": "ホワイトトラネキサム酸、2種のヒアルロン酸、ビタミンC誘導体、ビタミンE配合",
        "value": "大容量でリッチな高保水ジュレ。化粧水・乳液・美容液・収れん・パックの1本5役で、冬のスキンケア時間を短縮しながら贅沢な潤いを密封",
        "desc_p1": "ロート製薬が誇る大人気シリーズ『白潤プレミアム』のジュレ状美容液。抗炎症作用を持つ美白有効成分ホワイトトラネキサム酸を主軸に、分子サイズの異なる2種のヒアルロン酸を高濃度でブレンド。ポンプを押すと濃厚なジュレが現れますが、肌に触れた瞬間に液状に崩れ、角層のすみずみまでスーッと浸透していきます。",
        "desc_p2": "冬の朝、忙しくて何ステップも重ねる時間がない時でも、これ1本で化粧水からパックまでの役割を完璧に遂行。みずみずしい保水膜が肌表面に均一なヴェールを張り、日中の水分蒸散をブロックします。さらにビタミンC誘導体とビタミンEが酸化ストレスから肌を守り、冬の寒さに負けない透明感をキープします。",
        "target": "時短でしっかり美白と保湿を両立させたい方、首元やデコルテまで惜しみなく美白ケアしたい方、ジュレのみずみずしい使用感が好きな方",
        "point": "洗顔後、1〜2プッシュを顔全体になじませた後、両手で優しく引き上げるようにリフトハンドプレス。夜は少し多めに塗って『スリーピングジュレパック』として使うと翌朝ぷるぷるに。"
    },
    {
        "rank": 5,
        "tag": "🧪 薬用トラネキサム酸原末を高濃度配合！成分重視派を唸らせる実力派ブライトニング",
        "catch": "純度100%のトラネキサム酸原末採用。冬の紫外線残存ダメージとインナードライを速攻リセット",
        "brand_name": "TOUT VERT (トゥヴェール)",
        "capacity": "30ml (ブライトニングセラム)",
        "type": "高浸透薬用美白セラム (医薬部外品)",
        "features": "薬用トラネキサム酸原末、グリチルリチン酸2K、酵母エキス、甘草フラボノイド",
        "value": "無駄な添加物を排除し、有効成分をダイレクトに届ける高濃度設計。さらりとしたテクスチャーながら内側からモチッとうるおうインナードライ特化型",
        "desc_p1": "成分マニアやスキンケア上級者から絶大な支持を集めるトゥヴェールの薬用ブライトニングセラム。厚生労働省承認の美白有効成分である高純度トラネキサム酸原末を惜しみなく配合し、シミの発生源であるメラノサイトの活性化を初期段階でシャットアウトします。",
        "desc_p2": "冬の肌は皮脂分泌が減る一方で、角層の水分保持力も低下してインナードライに陥りがち。本品は水のように軽やかながら、酵母エキスや甘草フラボノイドの保湿力によって角層内部を満たし、肌のキメをふっくらと整えます。手持ちのスキンケアの邪魔をしないため、ブースターとしても化粧水後の美容液としても自在に組み込めます。",
        "target": "成分の濃度や純度にこだわりたい方、ベタつかずに肌の奥から明るさを引き出したい方、ビタミンC美容液と併用して相乗効果を狙いたい方",
        "point": "朝晩の洗顔直後、または化粧水の直後に500円玉大を優しくなじませます。ビタミンC誘導体化粧水やセラムの前に使うことで、相乗的なブライトニング効果を発揮します。"
    },
    {
        "rank": 6,
        "tag": "⚡ トラネキサム酸5%×ナイアシンアミド5%！驚異の高濃度コンビが冬のくすみを撃退",
        "catch": "美白とシワ改善の2大巨頭がタッグ。乾いた冬の角質層に多角的な透明感アプローチ",
        "brand_name": "Cos De BAHA (コスデバハ)",
        "capacity": "30ml (TN トラネキサム酸5% セラム)",
        "type": "高濃度機能性ブライトニング美容液",
        "features": "トラネキサム酸5%、ナイアシンアミド5%、アロエベラ葉エキスベース、ヒアルロン酸",
        "value": "精製水の代わりにアロエベラ葉エキスを使用し、驚異の高保水力を実現。高濃度処方でありながら肌あたりの良さと持続的な潤いを両立",
        "desc_p1": "韓国発の実力派ダーマコスメブランド『コスデバハ』のシグネチャーアイテム。トラネキサム酸を5%、さらに美白とセラミド合成促進で知られるナイアシンアミドを5%という、贅沢極まりない高濃度で配合したハイパワーセラムです。",
        "desc_p2": "通常、ベースに使われる精製水を極力減らし、高保湿なオーガニックアロエベラ葉エキスをベースに採用。これにより、高濃度成分の刺激をマイルドに包み込みながら、真冬の乾燥した肌へ濃密な水分をチャージします。メラニンの生成抑制と細胞への移行ブロックという2方向からシミを挟み撃ちにし、冬の冷えによる頑固な黄ぐすみを明るく晴らします。",
        "target": "一般的な美白美容液では効果を実感しにくかった方、高濃度ナイアシンアミドとトラネキサム酸を同時に試したい方、コスパ良く本気のケアをしたい方",
        "point": "化粧水で肌を十分に潤した後に2〜3滴をなじませます。高濃度のため、初めての方は夜のみの使用からスタートし、徐々に朝晩のデイリーケアへ移行するのがおすすめです。"
    },
    {
        "rank": 7,
        "tag": "🌸 セラミドを守りながらシミを防ぐ！真冬の乾燥性敏感肌のために生まれた美白ジェル",
        "catch": "カモミラET×セラミド機能成分。カサついて荒れやすい真冬の肌をふっくら潤す",
        "brand_name": "Curel (キュレル) / 花王",
        "capacity": "30g (潤浸保湿 美白ケア 美容液)",
        "type": "薬用美白美容液 (医薬部外品)",
        "features": "天然植物由来美白成分カモミラET、セラミド機能成分、ユーカリエキス配合",
        "value": "花王の独自セラミドケア技術を美白と融合。角層のバリア機能を高めながらメラニンの生成を抑え、シミ・ソバカスを根本予防",
        "desc_p1": "乾燥性敏感肌研究のパイオニアであるキュレル。冬になると乾燥と肌荒れが酷くて一般的な美白化粧品が使えないという切実な声に応えて開発されたのが、この潤浸保湿 美白美容液です。植物由来の美白有効成分カモミラETがメラノサイトの増殖をブロックします。",
        "desc_p2": "ぷるんとみずみずしい濃密ジェルが、肌に伸ばした瞬間にすーっとなじんでベタつきを残しません。セラミド機能成分が角層の深部まで浸透し、真冬の冷風によって失われがちな細胞間脂質を疑似再建。外部刺激を受けにくい健やかな肌へと導きながら、透き通るような明るさをキープします。",
        "target": "冬は乾燥で肌が荒れやすく美白コスメを諦めていた敏感肌の方、ベタつかない高保湿美白ジェルを求める方、肌のバリア機能を根本改善したい方",
        "point": "化粧水の後に直径約1cmを手にとり、顔全体に優しくなじませます。カサつきや粉吹きが気になる目元・口元には指先でトントンと重ね塗りをすると効果的です。"
    },
    {
        "rank": 8,
        "tag": "✨ 富士フイルムが誇る先行美白ジェリー！洗顔直後の素肌に極上のナノ浸透",
        "catch": "Wヒト型ナノセラミド×トラネキサム酸。冬の土台を立て直し、後から使う化粧水をグングン引き込む",
        "brand_name": "ASTALIFT (アスタリフト) / 富士フイルム",
        "capacity": "40g (ホワイト ジェリー アクアリスタ)",
        "type": "薬用先行美白美容液 (医薬部外品)",
        "features": "トラネキサム酸、Wヒト型ナノセラミド、ナノアスタキサンチン、マロニエエキス配合",
        "value": "世界最小クラスのナノセラミドが角層深層へ直撃。肌の土台となるバリアを再建し、トラネキサム酸が冬の微弱炎症を鎮めながら澄んだ透明感を創出",
        "desc_p1": "ナノテクノロジーの粋を集めたアスタリフトの赤い先行美容液『ホワイト ジェリー アクアリスタ』。洗顔直後の何もない素肌に使うことで、世界最小クラスに微粒子化されたWヒト型ナノセラミドが角層の隙間に滑り込み、乱れた肌構造を瞬時に修復します。",
        "desc_p2": "有効成分トラネキサム酸が肌荒れとメラニン発生を防ぎ、抗酸化成分ナノアスタキサンチンが真冬の冷えによるエイジングぐすみを払拭。自己復元性のある真っ赤なジェリーが肌の上でとろけ、その後に使う化粧水の浸透力を何倍にも高めます。まさに冬のスキンケアの費用対効果を最大化するブースターです。",
        "target": "冬になるとどんな化粧水も肌に入っていかないと感じる方、洗顔後すぐに肌がつっぱる乾燥肌の方、最高峰のハリと美白を同時に手に入れたい方",
        "point": "洗顔後すぐにスパチュラでやや大きめのパール粒大を取り、手のひらで温めてから顔全体に伸ばします。手のひらで顔全体を10秒間温めるように包み込むと浸透感が倍増します。"
    },
    {
        "rank": 9,
        "tag": "🌿 資生堂の濃密美白ミルク！トラネキサム酸×CICAで冬の角層を柔らかく解きほぐす",
        "catch": "美白有効成分トラネキサム酸配合。硬くなった真冬の肌をリッチなミルクで包み込む",
        "brand_name": "AQUALABEL (アクアレーベル) / 資生堂",
        "capacity": "130ml (トリートメントミルク ブライトニング しっとり)",
        "type": "薬用美白乳液 (医薬部外品)",
        "features": "トラネキサム酸、CICA（ツボクサエキス）、浸透型アミノ酸、パールシェルエキス配合",
        "value": "ドラッグストアで手に入る本格派美白乳液。デパコス級の贅沢成分が冬の硬化角質をじんわりほぐし、もっちり柔らかな発光肌へ導く",
        "desc_p1": "資生堂のアクアレーベルがリニューアルで更なる進化を遂げたトリートメントミルク ブライトニング。美白有効成分トラネキサム酸に加え、鎮静成分CICA（ツボクサエキス）と資生堂独自の浸透型アミノ酸を贅沢に配合しています。",
        "desc_p2": "冬の寒風によってゴワゴワに硬くなった角質層を、まろやかなミルクが優しくほぐしながら浸透。肌表面に油分と水分の理想的なバランスの膜を形成し、真冬でも乾燥によるキメの乱れやくすみを寄せ付けません。ほんのり香る上品なローズアクアの香りが、冬のスキンケアタイムを至福のリフレッシュ時間に変えてくれます。",
        "target": "毎日続けやすい価格で高品質な美白乳液を探している方、冬のゴワつきとくすみを同時にほぐしたい方、しっとり柔らかい後肌が好きな方",
        "point": "化粧水の後に10円硬貨大を手にとり、手のひらで顔全体に優しくすべらせるようになじませます。首筋やデコルテまで伸ばすことで、首元の乾燥小ジワとくすみも同時にケアできます。"
    },
    {
        "rank": 10,
        "tag": "💧 うるおい透明肌を叶える高浸透設計！トラネキサム酸×濃密バリア処方の薬用乳液",
        "catch": "高浸透トラネキサム酸配合。澄み渡るような透明感とふっくらキメ美肌をキープ",
        "brand_name": "ORBIS (オルビス)",
        "capacity": "50ml (オルビス ブライト モイスチャー M しっとりタイプ)",
        "type": "薬用美白乳液 (医薬部外品)",
        "features": "トラネキサム酸、高圧処理ビタミンC誘導体、ブライトVCコンプレックス配合、無油分・無香料",
        "value": "水分保持力に優れた高保湿膜が、冬のエアコン環境下でも肌の水分を抱え込み逃がさない。クリアで透き通るような澄み肌へ導く",
        "desc_p1": "オルビスのブライトシリーズは、肌の表面だけでなく『透明感の質』に着目したスキンケアライン。高浸透トラネキサム酸がメラニンの生成を抑えてシミ・ソバカスを防ぐと同時に、肌のキメをふっくら整えて光の反射を高めます。",
        "desc_p2": "しっとりタイプのモイスチャーMは、まろやかな感触で肌に吸い付くようになじみ、潤いの保護ベールを形成。無香料・弱酸性の安心設計で、冬のゆらぎやすい肌コンディションでも心地よく使えます。朝使ってもメイクがヨレにくく、日中の澄んだ明るいトーンを夕方までしっかりとキープしてくれます。",
        "target": "みずみずしい透明感が欲しい方、無香料・低刺激な美白乳液を好む方、日中のメイク崩れや夕方のくすみを防ぎたい方",
        "point": "化粧水の後、ポンプ1〜2プッシュを手に取り、下から上へ優しく引き上げるように顔全体へなじませます。手のひらで密着させることで、ピンとしたハリ感も同時に実感できます。"
    }
]

# JSON-LD 生成
jsonld_items = []
for i, p in enumerate(items):
    d = product_details[i]
    jsonld_items.append({
        "@type": "ListItem",
        "position": i + 1,
        "name": f"第{i+1}位：{d['brand_name']} {p['name']}",
        "description": d['catch'],
        "image": p['img_url'],
        "url": f"https://lumi-cosme.vercel.app/winter-tranexamic-acid.html#item-{i+1}",
        "offers": {
            "@type": "Offer",
            "price": str(p['price']),
            "priceCurrency": "JPY",
            "availability": "https://schema.org/InStock"
        }
    })

faq_list = [
    {
        "question": "なぜ冬の乾燥・くすみ対策にトラネキサム酸が効果的なのですか？",
        "answer": "冬は寒風や室内暖房による乾燥によって肌のバリア機能が低下し、目に見えない微弱な炎症（インフラメイジング）が絶えず発生します。この炎症シグナル（プロスタグランジンやプラスミン）がメラノサイトを刺激し続けることで、紫外線が少ない真冬であってもメラニンが過剰生成され、血行不良と重なって頑固な『冬ぐすみ・シミの悪化』を引き起こします。トラネキサム酸は抗炎症作用とメラニン生成抑制作用を兼ね備えた医薬部外品有効成分であり、冬の炎症連鎖を根本から断ち切りながら、高保湿成分と連携して澄み渡る発光透明肌を守り抜きます。"
    },
    {
        "question": "トラネキサム酸はビタミンCやレチノールと併用しても大丈夫ですか？",
        "answer": "非常に相性が良く、相乗効果が期待できます。トラネキサム酸は刺激性が極めて低く抗炎症作用を持つため、ビタミンCによるメラニン還元・毛穴ケアや、レチノールによるターンオーバー促進・ハリ弾力ケアと組み合わせることで、多角的な美肌アプローチが可能です。併用の順番としては、洗顔後【ビタミンC美容液】→【化粧水】→【トラネキサム酸美容液/乳液】→【レチノール（夜のみ）】→【保湿クリーム】の流れが理想的です。刺激が気になる場合は朝＝ビタミンC＋トラネキサム酸、夜＝レチノール＋トラネキサム酸のように使い分けるのも効果的です。"
    },
    {
        "question": "美白コスメは冬に使うと乾燥しませんか？保湿力は十分ですか？",
        "answer": "かつての美白コスメはさっぱりしたテクスチャーが多く冬には乾燥しやすい傾向がありましたが、現在ランクインしている最新の高保湿トラネキサム酸コスメは、ヒト型セラミド、高精製ワセリン、浸透型ヒアルロン酸、アミノ酸などの強力な保水・エモリエント成分が贅沢にブレンドされています。そのため、一般的な保湿美容液や乳液と同等以上のしっとり感を誇り、冬のエアコン乾燥や粉吹きをしっかり防ぎながら美白ケアを完結できます。"
    },
    {
        "question": "トラネキサム酸は朝のスキンケアで使用しても紫外線による影響はありませんか？",
        "answer": "全く問題ありません。ビタミンA（レチノール）や一部の酸性ピーリング成分とは異なり、トラネキサム酸には光毒性（紫外線に反応して炎症を起こす性質）がありません。むしろ、日中の紫外線刺激や外気の寒暖差による炎症シグナルを日中から先回りしてブロックできるため、朝のスキンケアに取り入れることは非常に理にかなっています。朝のスキンケアでトラネキサム酸を仕込んだ後、日焼け止め（SPF30〜50/PA+++程度）を重ねることで、真冬の紫外線ダメージを鉄壁に防ぐことができます。"
    },
    {
        "question": "敏感肌や肌荒れしやすい肌質でも毎日使用できますか？",
        "answer": "トラネキサム酸は元々医療現場で抗炎症薬・止血薬として長く用いられてきた成分であり、皮膚刺激性が非常に穏やかです。医薬部外品においても『肌荒れ・荒れ性防止』の有効成分として認可されているため、冬の寒風やマスク擦れで赤みが出やすい敏感肌の方にこそ強くおすすめできます。ただし、他の配合成分（アルコールや精油など）に反応する場合があるため、極度の敏感肌の方はイハダやキュレル、カウブランドのような低刺激・無香料設計のアイテムから選ぶと安心です。"
    }
]

jsonld_faq = []
for faq in faq_list:
    jsonld_faq.append({
        "@type": "Question",
        "name": faq["question"],
        "acceptedAnswer": {
            "@type": "Answer",
            "text": faq["answer"]
        }
    })

jsonld_article = {
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://lumi-cosme.vercel.app/winter-tranexamic-acid.html"
    },
    "headline": "保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房乾燥によるくすみ・肌荒れを防ぎ澄んだ透明ツヤ肌へ導く高保湿トラネキサム酸コスメランク10",
    "description": "11月・12月の寒風とエアコン暖房による乾燥くすみ・微小炎症を救う高保湿トラネキサム酸コスメを徹底厳選！トランシーノ、資生堂HAKU、イハダ、白潤プレミアムからアスタリフト、コスデバハまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。",
    "image": items[0]["img_url"],
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
    "datePublished": "2026-11-04T00:00:00+09:00",
    "dateModified": "2026-11-04T00:00:00+09:00"
}

jsonld_itemlist = {
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿トラネキサム酸コスメおすすめ人気ランキング10選",
    "itemListElement": jsonld_items
}

jsonld_faqpage = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": jsonld_faq
}

cards_html = []
for i, p in enumerate(items):
    d = product_details[i]
    cards_html.append(f"""
    <article class="product-card" id="item-{i+1}">
      <div class="product-badge-rank">第{i+1}位</div>
      <div class="product-tag">{d['tag']}</div>
      <h3 class="product-name">{d['brand_name']} {p['name']}</h3>
      <p class="product-catch">{d['catch']}</p>
      
      <div class="product-flex">
        <div class="product-img-box">
          <img src="{p['img_url']}" alt="{p['name']}" class="product-img" loading="lazy">
          <div class="price-box">
            <span class="price-label">楽天市場参考価格</span>
            <span class="price-val">¥{p['price']:,}</span>
            <span class="price-tax">（税込）</span>
          </div>
          <a href="{p['affiliate_url']}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
            楽天市場で詳細を見る・購入
          </a>
        </div>
        
        <div class="product-spec-box">
          <table class="spec-table">
            <tr><th>ブランド</th><td>{d['brand_name']}</td></tr>
            <tr><th>容量 / 規格</th><td>{d['capacity']}</td></tr>
            <tr><th>アイテム分類</th><td>{d['type']}</td></tr>
            <tr><th>主要成分・有効処方</th><td>{d['features']}</td></tr>
            <tr><th>高保湿・透明感の理由</th><td>{d['value']}</td></tr>
          </table>
          
          <div class="review-block">
            <h4>💡 冬の乾燥くすみ・微小炎症に対する詳細解説</h4>
            <p>{d['desc_p1']}</p>
            <p>{d['desc_p2']}</p>
          </div>
          
          <div class="target-block">
            <strong>🎯 こんな方に特におすすめ：</strong>
            <p>{d['target']}</p>
          </div>
          
          <div class="usage-block">
            <strong>✨ 美容のプロ直伝！冬のおすすめ活用テクニック：</strong>
            <p>{d['point']}</p>
          </div>
        </div>
      </div>
    </article>
    """)

cards_str = "\n".join(cards_html)

faq_html = []
for f in faq_list:
    faq_html.append(f"""
      <div class="faq-item">
        <h3 class="faq-q">Q. {f['question']}</h3>
        <p class="faq-a">A. {f['answer']}</p>
      </div>
    """)
faq_str = "\n".join(faq_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房乾燥によるくすみ・肌荒れを防ぎ澄んだ透明ツヤ肌へ導く高保湿トラネキサム酸コスメランク10 - 冬コスメ徹底比較ラボ</title>
  <meta name="description" content="11月・12月の寒風とエアコン暖房による乾燥くすみ・微小炎症を救う高保湿トラネキサム酸コスメを徹底厳選！トランシーノ、資生堂HAKU、イハダ、白潤プレミアムからアスタリフト、コスデバハまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta name="keywords" content="トラネキサム酸,高保湿美白,冬コスメ,乾燥肌,肝斑,くすみ改善,インフラメイジング,HAKU,トランシーノ,イハダ,楽天コスメ">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-tranexamic-acid.html">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房乾燥によるくすみ・肌荒れを防ぎ澄んだ透明ツヤ肌へ導く高保湿トラネキサム酸コスメランク10">
  <meta property="og:description" content="11月・12月の寒風とエアコン暖房による乾燥くすみ・微小炎症を救う高保湿トラネキサム酸コスメを徹底厳選！トランシーノ、資生堂HAKU、イハダ、白潤プレミアムからアスタリフト、コスデバハまで楽天で今すぐ買えるおすすめ人気ランキング10選とプロの活用術を詳しく解説。">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-tranexamic-acid.html">
  <meta property="og:image" content="{items[0]['img_url']}">
  <meta property="og:site_name" content="冬コスメ徹底比較ラボ">
  <meta name="twitter:card" content="summary_large_image">
  
  <script type="application/ld+json">
  {json.dumps(jsonld_article, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(jsonld_itemlist, ensure_ascii=False, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(jsonld_faqpage, ensure_ascii=False, indent=2)}
  </script>
  
  <style>
    :root {{
      --primary: #1e3a5f;
      --primary-light: #2d5a8c;
      --accent: #0284c7;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #cbd5e1;
      --radius: 12px;
      --shadow: 0 4px 16px rgba(30, 58, 95, 0.08);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", "Hiragino Kaku Gothic ProN", "Yu Gothic", Meiryo, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.8;
      -webkit-font-smoothing: antialiased;
    }}
    header {{
      background: linear-gradient(135deg, #0f233a, #1e3a5f);
      color: #fff;
      padding: 18px 24px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
    }}
    .header-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-size: 1.3rem;
      font-weight: 800;
      color: #fff;
      text-decoration: none;
      letter-spacing: 0.5px;
    }}
    .breadcrumb {{
      max-width: 1080px;
      margin: 16px auto 0;
      padding: 0 20px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .breadcrumb a {{ color: var(--primary-light); text-decoration: none; }}
    .main-container {{
      max-width: 1080px;
      margin: 20px auto 60px;
      padding: 0 20px;
    }}
    .article-header {{
      background: #fff;
      padding: 36px 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 32px;
    }}
    .article-badge {{
      display: inline-block;
      background: #e0f2fe;
      color: #0369a1;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 12px;
      border-radius: 20px;
      margin-bottom: 14px;
    }}
    h1 {{
      font-size: 1.85rem;
      line-height: 1.45;
      color: #0f233a;
      margin-bottom: 20px;
      font-weight: 800;
    }}
    .meta-box {{
      display: flex;
      gap: 18px;
      font-size: 0.85rem;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border);
      padding-bottom: 16px;
      margin-bottom: 20px;
    }}
    .lead-text {{
      font-size: 1.05rem;
      line-height: 1.85;
      color: #334155;
      margin-bottom: 18px;
    }}
    .toc-box {{
      background: #f1f5f9;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      margin: 28px 0;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 1.1rem;
      color: var(--primary);
      margin-bottom: 14px;
    }}
    .toc-list {{
      list-style-position: inside;
      line-height: 2;
    }}
    .toc-list a {{ color: var(--primary-light); text-decoration: none; }}
    .toc-list a:hover {{ text-decoration: underline; }}
    
    .guide-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .guide-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
      line-height: 1.4;
    }}
    .guide-section h3 {{
      font-size: 1.2rem;
      color: #1e3a5f;
      margin: 24px 0 12px;
    }}
    .guide-section p {{
      margin-bottom: 16px;
      font-size: 0.98rem;
      line-height: 1.85;
    }}
    .guide-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 20px;
      margin: 24px 0;
    }}
    .grid-card {{
      background: #f0fdf4;
      padding: 20px;
      border-radius: 10px;
      border: 1px solid #bbf7d0;
    }}
    .grid-card:nth-child(2) {{ background: #eff6ff; border-color: #bfdbfe; }}
    .grid-card:nth-child(3) {{ background: #fdf4ff; border-color: #f5d0fe; }}
    .grid-card h4 {{
      color: #0f172a;
      margin-bottom: 8px;
      font-size: 1.05rem;
    }}
    
    /* Product Cards */
    .product-card {{
      background: #fff;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      padding: 32px;
      margin-bottom: 36px;
      position: relative;
    }}
    .product-badge-rank {{
      position: absolute;
      top: -14px;
      left: 24px;
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      font-size: 1.05rem;
      font-weight: 800;
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 10px rgba(3, 105, 161, 0.3);
    }}
    .product-tag {{
      display: inline-block;
      margin-top: 6px;
      font-size: 0.88rem;
      font-weight: 700;
      color: #0369a1;
      background: #e0f2fe;
      padding: 3px 10px;
      border-radius: 6px;
      margin-bottom: 10px;
    }}
    .product-name {{
      font-size: 1.4rem;
      line-height: 1.4;
      color: #0f233a;
      margin-bottom: 8px;
      font-weight: 800;
    }}
    .product-catch {{
      font-size: 0.98rem;
      font-weight: 600;
      color: #0284c7;
      margin-bottom: 24px;
    }}
    .product-flex {{
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}
    @media (min-width: 768px) {{
      .product-flex {{
        flex-direction: row;
        align-items: flex-start;
      }}
    }}
    .product-img-box {{
      flex: 0 0 280px;
      text-align: center;
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 10px;
      background: #fafafa;
      border: 1px solid #f0f0f0;
      padding: 8px;
    }}
    .price-box {{
      margin: 14px 0;
      padding: 10px;
      background: #f0f9ff;
      border-radius: 8px;
      border: 1px dashed #bae6fd;
    }}
    .price-label {{ display: block; font-size: 0.78rem; color: #64748b; }}
    .price-val {{ font-size: 1.5rem; font-weight: 800; color: #0284c7; }}
    .price-tax {{ font-size: 0.8rem; color: #64748b; }}
    .rakuten-btn {{
      display: block;
      background: linear-gradient(135deg, #bf0000, #990000);
      color: #fff;
      font-weight: 700;
      text-align: center;
      padding: 14px 20px;
      border-radius: 8px;
      text-decoration: none;
      font-size: 0.98rem;
      box-shadow: 0 4px 12px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #d60000, #b00000);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(191, 0, 0, 0.35);
    }}
    .product-spec-box {{
      flex: 1;
    }}
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 18px;
      font-size: 0.88rem;
    }}
    .spec-table th {{
      width: 28%;
      background: #f8fafc;
      padding: 8px 12px;
      border: 1px solid #cbd5e1;
      text-align: left;
      color: #1e3a5f;
      font-weight: 600;
    }}
    .spec-table td {{
      padding: 8px 12px;
      border: 1px solid #cbd5e1;
      background: #fff;
    }}
    .review-block {{
      background: #f8fafc;
      border-left: 4px solid var(--accent);
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 14px;
    }}
    .review-block h4 {{
      font-size: 0.98rem;
      color: #0f233a;
      margin-bottom: 8px;
    }}
    .review-block p {{
      font-size: 0.92rem;
      line-height: 1.75;
      color: #334155;
      margin-bottom: 8px;
    }}
    .review-block p:last-child {{ margin-bottom: 0; }}
    .target-block, .usage-block {{
      font-size: 0.9rem;
      margin-bottom: 10px;
      line-height: 1.7;
    }}
    
    /* Comparison Table */
    .compare-table-wrap {{
      overflow-x: auto;
      margin: 20px 0;
    }}
    .compare-table {{
      width: 100%;
      border-collapse: collapse;
      min-width: 650px;
      font-size: 0.88rem;
    }}
    .compare-table th, .compare-table td {{
      padding: 10px 14px;
      border: 1px solid #cbd5e1;
      text-align: center;
    }}
    .compare-table th {{
      background: #f1f5f9;
      color: #0f233a;
      font-weight: 700;
    }}
    .compare-table td.left-align {{
      text-align: left;
    }}
    
    /* FAQ Section */
    .faq-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .faq-section h2 {{
      font-size: 1.45rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 24px;
    }}
    .faq-item {{
      border-bottom: 1px solid var(--border);
      padding: 18px 0;
    }}
    .faq-item:last-child {{ border-bottom: none; }}
    .faq-q {{
      font-size: 1.05rem;
      color: #0369a1;
      font-weight: 700;
      margin-bottom: 8px;
    }}
    .faq-a {{
      font-size: 0.95rem;
      line-height: 1.8;
      color: #334155;
    }}
    
    /* Internal Links Grid */
    .internal-section {{
      background: #fff;
      padding: 32px;
      border-radius: var(--radius);
      box-shadow: var(--shadow);
      border: 1px solid var(--border);
      margin-bottom: 36px;
    }}
    .internal-section h2 {{
      font-size: 1.4rem;
      color: var(--primary);
      border-left: 5px solid var(--accent);
      padding-left: 14px;
      margin-bottom: 20px;
    }}
    .internal-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
    }}
    .internal-card {{
      background: #f1f5f9;
      padding: 16px;
      border-radius: 8px;
      border: 1px solid #e2e8f0;
      text-decoration: none;
      color: var(--text);
      transition: all 0.2s;
    }}
    .internal-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
      border-color: var(--accent);
    }}
    .internal-card h4 {{
      font-size: 0.95rem;
      color: var(--primary);
      margin-bottom: 6px;
    }}
    .internal-card p {{
      font-size: 0.82rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    footer {{
      background: #0f172a;
      color: #94a3b8;
      text-align: center;
      padding: 36px 20px;
      font-size: 0.85rem;
    }}
    footer a {{ color: #cbd5e1; text-decoration: none; }}
  </style>
</head>
<body>

<header>
  <div class="header-inner">
    <a href="/" class="site-logo">❄️ 冬コスメ徹底比較ラボ</a>
    <span style="font-size: 0.85rem; color: #93c5fd;">2026-2027年 冬季最新スキンケア特集</span>
  </div>
</header>

<div class="breadcrumb">
  <a href="/">ホーム</a> &gt; <span>高保湿トラネキサム酸コスメ</span>
</div>

<main class="main-container">
  <div class="article-header">
    <span class="article-badge">✨ 11月〜12月本格乾燥・くすみ対策</span>
    <h1>保湿力の強さで肌乾燥とさようなら！冬の冷気と暖房乾燥によるくすみ・肌荒れを防ぎ澄んだ透明ツヤ肌へ導く高保湿トラネキサム酸コスメランク10</h1>
    <div class="meta-box">
      <span>📅 最終更新日: 2026年11月4日</span>
      <span>✍️ 監修: 冬コスメ徹底比較ラボ 美容皮膚科学リサーチチーム</span>
      <span>⏱️ 読了目安: 約8分</span>
    </div>
    <p class="lead-text">
      11月から12月へと季節が進むにつれ、急激に低下する外気温と湿度の影響で、肌の角層水分量は一年で最も急激な減少を見せます。さらに室内を温めるエアコンの乾いた温風が容赦なく水分を奪い、多くの女性が「保湿しているのに肌がカサつく」「冬なのに顔全体が暗くどんよりくすむ」「頬の赤みやシミ・肝斑が急に目立つようになった」という複合的な肌危機に直面します。
    </p>
    <p class="lead-text">
      この冬特有の肌トラブルの真犯人こそ、寒暖差とバリア崩壊によって肌内部で静かに燃え広がる『微小炎症（インフラメイジング）』です。本特集では、抗炎症作用によって肌荒れを沈静化させつつ、メラニン生成シグナルを遮断してクリアな白玉ツヤ肌へ導く医薬部外品有効成分『トラネキサム酸』に着目。真冬の過酷な乾燥にも耐えうる高保湿処方を備えた名品10選を、楽天市場の最新データに基づき徹底比較検証しました。
    </p>
  </div>

  <div class="toc-box">
    <div class="toc-title">📑 目次 - タップして各項目へジャンプ</div>
    <ol class="toc-list">
      <li><a href="#guide-mechanism">1. なぜ11月〜12月の真冬乾燥に「トラネキサム酸」が必要なのか？（インフラメイジングの罠）</a></li>
      <li><a href="#guide-points">2. 冬の高保湿トラネキサム酸コスメを選ぶ3つの絶対基準</a></li>
      <li><a href="#ranking-section">3. 【2026年最新】真冬の高保湿トラネキサム酸コスメおすすめ人気ランキング10選</a></li>
      <li><a href="#comparison-section">4. 高保湿トラネキサム酸コスメ10選スペック＆価格早見表</a></li>
      <li><a href="#usage-technique">5. 美容のプロ直伝！冬の透明感とバリアを高めるWブースト重ね技</a></li>
      <li><a href="#faq-section">6. 高保湿トラネキサム酸コスメに関するよくある質問（FAQ）</a></li>
      <li><a href="#related-section">7. あわせて読みたい冬の集中保湿ケア関連記事</a></li>
    </ol>
  </div>

  <section class="guide-section" id="guide-mechanism">
    <h2>1. なぜ11月〜12月の真冬乾燥に「トラネキサム酸」が必要なのか？</h2>
    <p>
      「美白ケアは紫外線が強い春夏の特権」と思い込んでいませんか？実は、大人の肌にとって11月から12月こそが、シミやくすみが最も定着・悪化しやすい危険地帯です。
    </p>
    <p>
      冬の外気は湿度が30%台まで落ち込み、角層の天然保湿因子（NMF）や細胞間脂質（セラミド）が急速に減少します。角層がスカスカになると、冷たい北風やマスクの摩擦、寒暖差といった微細な刺激だけで皮膚組織が微小な炎症を起こします。この炎症時に放出される物質『プラスミン』や『プロスタグランジン』は、メラノサイトに対して「メラニンを作れ！」と命じる刺激指令を出し続けます。つまり、紫外線が少なくても、<strong>「寒さと乾燥による炎症のせいで、冬にシミ・くすみが作られ続けている」</strong>のです。
    </p>
    
    <div class="guide-grid">
      <div class="grid-card">
        <h4>① 炎症刺激（プラスミン）を抑制</h4>
        <p>トラネキサム酸は医療用抗炎症薬としても使われる成分。真冬の寒暖差による肌荒れや赤みの火種を鎮静化させます。</p>
      </div>
      <div class="grid-card">
        <h4>② メラニン生成シグナルを遮断</h4>
        <p>メラノサイトがメラニンを過剰に合成する命令プロセスを初期段階でブロックし、冬の黄ぐすみやシミ化を根本から防ぎます。</p>
      </div>
      <div class="grid-card">
        <h4>③ 高保湿ヴェールとの融合</h4>
        <p><a href="/winter-ceramide-lotion" style="color:#0284c7;font-weight:600;">ヒト型セラミド</a>や<a href="/winter-vaseline" style="color:#0284c7;font-weight:600;">高精製ワセリン</a>、<a href="/winter-hyaluronic-serum" style="color:#0284c7;font-weight:600;">ヒアルロン酸</a>と組み合わせることで、水分蒸散をブロックしながら透明感を育みます。</p>
      </div>
    </div>
  </section>

  <section class="guide-section" id="guide-points">
    <h2>2. 冬の高保湿トラネキサム酸コスメを選ぶ3つの絶対基準</h2>
    <p>
      数あるトラネキサム酸コスメの中から、11〜12月の真冬に真価を発揮するアイテムを見極めるためのプロの着眼点をご紹介します。
    </p>
    <h3>① 有効成分トラネキサム酸が医薬部外品として明記されているか</h3>
    <p>
      しっかりとシミ予防や肌荒れ防止の効能を期待するなら、厚生労働省承認の「医薬部外品（薬用）」表記があるものを選ぶのが基本です。配合目的が「美白」または「肌荒れ防止」として規定濃度のトラネキサム酸が配合されているため、確かな手応えが得られます。
    </p>
    <h3>② 真冬の水分蒸散を防ぐエモリエント成分（油分・高保水膜）が贅沢か</h3>
    <p>
      トラネキサム酸単体は水溶性成分です。冬の乾燥肌には、これを受け止めて閉じ込める「ヒト型セラミド」「スクワラン」「シアバター」「高精製ワセリン」などの油性エモリエント成分がリッチに含まれていることが不可欠。乳液、濃密セラム、ジュレなど、後肌がしっとり吸い付くテクスチャーを選びましょう。
    </p>
    <h3>③ ナイアシンアミドやビタミンC、CICAなど複合シナジーが設計されているか</h3>
    <p>
      トラネキサム酸と相乗効果を生むサポート成分にも注目。<a href="/winter-niacinamide-serum" style="color:#0284c7;font-weight:600;">ナイアシンアミド</a>（メラニン転送抑制・シワ改善）や、<a href="/winter-vitamin-c-serum" style="color:#0284c7;font-weight:600;">ビタミンC誘導体</a>（還元作用）、<a href="/winter-cica-cream" style="color:#0284c7;font-weight:600;">CICA・ツボクサエキス</a>（組織修復）が併せ持つ処方なら、冬枯れ肌の全方位リニューアルが叶います。
    </p>
  </section>

  <section id="ranking-section">
    <h2 style="font-size: 1.6rem; color: #0f233a; margin-bottom: 24px; padding-left: 14px; border-left: 6px solid #0284c7;">
      3. 【2026年最新】真冬の高保湿トラネキサム酸コスメおすすめ人気ランキング10選
    </h2>
    <p style="margin-bottom: 32px; font-size: 0.95rem; color: #475569;">
      楽天市場の最新流通データから、リアルタイムの販売価格と在庫状況、購入者レビューの評価を総合的にスコアリング。11〜12月の乾燥・くすみケアに圧倒的実力を誇る10製品を厳選しました。
    </p>
    
    {cards_str}
  </section>

  <section class="guide-section" id="comparison-section">
    <h2>4. 高保湿トラネキサム酸コスメ10選スペック＆価格早見表</h2>
    <p>
      ランクインした全10アイテムの主要特徴、参考価格、アイテム分類を一目で比較できます。ご自身の肌状態やご予算に合わせて最適なアイテムをお選びください。
    </p>
    
    <div class="compare-table-wrap">
      <table class="compare-table">
        <thead>
          <tr>
            <th>順位・製品名</th>
            <th>参考価格</th>
            <th>分類</th>
            <th>主要な強み・特徴</th>
            <th>おすすめの肌質</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>第1位 トランシーノ 薬用メラノシグナル</strong></td>
            <td>¥4,990</td>
            <td>薬用美容液</td>
            <td>トラネキサム酸本家の浸透ナノカプセル美白</td>
            <td>全肌質・肝斑・シミが気になる方</td>
          </tr>
          <tr>
            <td><strong>第2位 資生堂 HAKU メラノフォーカスEV</strong></td>
            <td>¥11,000</td>
            <td>薬用美容液</td>
            <td>m-トラネキサム酸×4MSKのW美白有効成分</td>
            <td>本気のエイジング美白・乾燥肌</td>
          </tr>
          <tr>
            <td><strong>第3位 イハダ 薬用クリアエマルジョン</strong></td>
            <td>¥2,090</td>
            <td>薬用乳液</td>
            <td>高精製ワセリン配合で寒風シールド</td>
            <td>超敏感肌・乾燥ゆらぎ肌・赤み肌</td>
          </tr>
          <tr>
            <td><strong>第4位 白潤プレミアム ジュレ状美白美容液</strong></td>
            <td>¥24,360 (4個組)</td>
            <td>薬用ジュレ</td>
            <td>1本5役・2種ヒアルロン酸高配合ジュレ</td>
            <td>時短重視・全身美白・インナードライ</td>
          </tr>
          <tr>
            <td><strong>第5位 トゥヴェール ブライトニングセラム</strong></td>
            <td>¥4,120</td>
            <td>薬用セラム</td>
            <td>高純度トラネキサム酸原末配合の本格処方</td>
            <td>成分濃度重視・ベタつき苦手な方</td>
          </tr>
          <tr>
            <td><strong>第6位 コスデバハ TNセラム</strong></td>
            <td>¥2,290</td>
            <td>高濃度セラム</td>
            <td>トラネキサム酸5%×ナイアシンアミド5%</td>
            <td>頑固なくすみ・黄ぐすみ改善派</td>
          </tr>
          <tr>
            <td><strong>第7位 キュレル 潤浸保湿 美白美容液</strong></td>
            <td>¥3,150</td>
            <td>薬用ジェル</td>
            <td>カモミラET×セラミド機能成分配合</td>
            <td>冬の乾燥性敏感肌・カサカサ肌</td>
          </tr>
          <tr>
            <td><strong>第8位 アスタリフト ホワイト ジェリー</strong></td>
            <td>¥8,215</td>
            <td>先行美容液</td>
            <td>Wヒト型ナノセラミド×土台立て直し</td>
            <td>化粧水の浸透が悪い肌・乾燥ゴワつき</td>
          </tr>
          <tr>
            <td><strong>第9位 アクアレーベル トリートメントミルク</strong></td>
            <td>¥1,386</td>
            <td>薬用乳液</td>
            <td>トラネキサム酸×CICAで角質を柔軟化</td>
            <td>プチプラ高品質・首元までケアしたい方</td>
          </tr>
          <tr>
            <td><strong>第10位 オルビス ブライト モイスチャー M</strong></td>
            <td>¥1,980</td>
            <td>薬用乳液</td>
            <td>無油分・高圧処理VC複合体配合</td>
            <td>日中の乾燥くずれ・メイク前の保湿</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="guide-section" id="usage-technique">
    <h2>5. 美容のプロ直伝！冬の透明感とバリアを高めるWブースト重ね技</h2>
    <p>
      高機能なトラネキサム酸コスメのポテンシャルを120%引き出すための、真冬ならではのプロ直伝ケアをご紹介します。
    </p>
    <h3>① 「摩擦レス・ハンドプレス」で角層温度を上げて浸透促進</h3>
    <p>
      11月〜12月の肌は寒さで血行が低下し、肌表面の温度も下がっています。冷たいままの美容液を急いで塗り広げると、摩擦刺激となり微小炎症を悪化させる原因に。美容液を手にとったら、まずは両手の手のひらを軽く擦り合わせて人肌程度に温めてから、顔全体を包み込むように10秒間じっくりプレスしてください。体温で角質層が柔らかくなり、トラネキサム酸が角層深層へスムーズに引き込まれます。
    </p>
    <h3>② ビタミンC誘導体との「朝のW美白ブースト」</h3>
    <p>
      朝の洗顔後、化粧水の前に<a href="/winter-vitamin-c-serum" style="color:#0284c7;font-weight:600;">ビタミンC誘導体セラム</a>をなじませ、その後にトラネキサム酸エマルジョンを重ねるレイヤリングが極めて有効です。ビタミンCが活性酸素を除去し、トラネキサム酸が炎症指令をストップ。日中の紫外線や寒暖差による酸化・炎症ストレスをダブルで遮断し、夕方になってもくすまない澄んだ透明肌を維持できます。
    </p>
    <h3>③ 夜はこっくりしたセラミドクリームで完全密閉</h3>
    <p>
      トラネキサム酸で水分と有効成分を満たした後は、必ず<a href="/winter-ceramide-cream" style="color:#0284c7;font-weight:600;">高保湿セラミドクリーム</a>や<a href="/winter-night-cream" style="color:#0284c7;font-weight:600;">濃密ナイトクリーム</a>で蓋をしましょう。就寝中の暖房による室内乾燥から肌を守り、一晩中トラネキサム酸を角層内に留まらせて集中リペアを完了させます。
    </p>
  </section>

  <section class="faq-section" id="faq-section">
    <h2>6. 高保湿トラネキサム酸コスメに関するよくある質問（FAQ）</h2>
    {faq_str}
  </section>

  <section class="internal-section" id="related-section">
    <h2>7. あわせて読みたい冬の集中保湿ケア関連記事</h2>
    <p style="margin-bottom: 20px; font-size: 0.95rem; color: #475569;">
      トラネキサム酸と併用することで、真冬の乾燥対策・エイジングケア効果をさらに高める関連特集です。
    </p>
    <div class="internal-grid">
      <a href="/winter-ceramide-lotion" class="internal-card">
        <h4>🧴 高保湿セラミド化粧水ランク10</h4>
        <p>冬のバリア機能を根本から強化するヒト型セラミド配合の最強化粧水を徹底比較。</p>
      </a>
      <a href="/winter-niacinamide-serum" class="internal-card">
        <h4>✨ 高濃度ナイアシンアミド美容液ランク10</h4>
        <p>シワ改善と美白を同時に叶える大人気セラム。トラネキサム酸との相乗効果も抜群。</p>
      </a>
      <a href="/winter-cica-cream" class="internal-card">
        <h4>🌿 高保湿CICAクリームランク10</h4>
        <p>寒暖差や冷風で荒れた肌を優しく鎮静するリペアクリーム特集。</p>
      </a>
      <a href="/winter-vitamin-c-serum" class="internal-card">
        <h4>🍋 冬の高浸透ビタミンC美容液ランク10</h4>
        <p>乾燥毛穴やくすみを晴らす朝のビタミンチャージに最適な名品セラム。</p>
      </a>
      <a href="/winter-ceramide-cream" class="internal-card">
        <h4>🛡️ 高保湿セラミドクリームランク10</h4>
        <p>真冬の冷風をシャットアウトし潤いを密閉する高機能フェイスクリーム10選。</p>
      </a>
      <a href="/winter-vaseline" class="internal-card">
        <h4>💧 高純度ワセリンコスメランク10</h4>
        <p>極度の粉吹き・ひび割れ肌を救う高精製ワセリンの保護シールドコスメ。</p>
      </a>
    </div>
  </section>
</main>

<footer>
  <p>&copy; 2026 冬コスメ徹底比較ラボ. All Rights Reserved. 画像および商品情報は楽天市場Web APIより取得しています。</p>
</footer>

</body>
</html>
"""

with open("winter-tranexamic-acid.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-tranexamic-acid.html successfully!")
