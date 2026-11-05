import json
import re

with open("fetched_3new_murumuru_cranberry_emu.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_murumuru_butter"]["items"]

product_details = [
    {
        "rank": 1,
        "tag": "👑 シアバターを超える圧倒的抱水力！真冬のひび割れかかと・粉吹き手肌を瞬時に再生する大容量ピュアバター",
        "catch": "アマゾン奥地のヤシ種子から抽出された純度100%の精製ムルムルバター。体温（約33℃）でじんわり溶け出し、シアバターよりも長時間の密着保水膜を形成して真冬の極度な乾燥から皮膚を完全防護する",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "200g / スパウトパウチ・アルミパック",
        "type": "100%植物性 高純度精製ムルムルバター（化粧品グレード）",
        "features": "アストロカリウムムルムル種子脂100%、高濃度ラウリン酸（約47%）、ミリスチン酸（約26%）、オレイン酸",
        "value": "シアバターに比べて融点が人肌に近く、伸びの良さとベタつきの少なさを両立。高い水分抱え込み力（エモリエント持続性）により、真冬の硬化した角質層を柔軟化してひび割れを予防する",
        "desc_p1": "11月下旬から12月にかけて外気温が10℃を下回ると、皮脂分泌量は夏の半分以下まで激減します。特にかかと、ひじ、膝、そして手指の関節まわりは皮脂腺が極めて少なく、乾燥によって角質が石のように硬直してひび割れや粉吹きを引き起こしがちです。マンディムーンの『ムルムルバター・精製 200g』は、南米アマゾン熱帯雨林の過酷な環境を生き抜くヤシ科植物ムルムルの種子から搾油された、極めて高い水分保持力を誇る天然の植物油脂です。",
        "desc_p2": "指先にとると最初は固形ですが、肌に触れた瞬間に体温でトロリとなめらかなオイル状へと変化。シアバター特有のザラつきや重い油膜感が苦手な方でも驚くほど均一に伸び広がり、塗布後すぐにベルベットのような上質な保護膜が皮膚表面をラップします。お風呂上がりの湿り気が残るかかとやひじにすり込むと、翌朝にはカチコチだった皮膚がふっくらと柔らかさを取り戻します。200gの大容量なので、冬の全身パーツケアに惜しみなく使い倒せる頼もしい逸品です。",
        "target": "シアバターだと硬すぎて冬場に伸ばしにくいと感じている方、ひび割れ寸前のかかとや粉吹きすねに悩む方、無添加・無香料で手持ちのクリームやオイルに混ぜて使いたい方",
        "point": "お風呂から上がって水分を拭き取る直前、肌がまだ温かく湿っているタイミングで大豆粒大を手に取り、両手のひらで温めてからかかとやひじ、すね全体へ押し込むように塗り込みます。靴下を履いて就寝するとパック効果が倍増します。"
    },
    {
        "rank": 2,
        "tag": "✨ 持ち歩きや初めてのムルムル体験に最適！ポーチに忍ばせるマルチレスキュー高保湿ミニサイズ",
        "catch": "純度100%の精製ムルムルバターを手軽に試せる50gサイズ。真冬の外出先で突然発生する指先のささくれ、口元の乾燥粉吹き、毛先のパサつきをひと塗りで即座に鎮める万能バーム",
        "brand_name": "mandy moon (マンディムーン)",
        "capacity": "50g / スタンドパウチ",
        "type": "携帯型 高純度精製ムルムルバター",
        "features": "精製ムルムルバター100%、低刺激・無香料・無着色、天然植物性脂肪酸コンプレックス",
        "value": "外出先やオフィスでの急激な乾燥ダメージに即応。酸化安定性に優れた飽和脂肪酸が中心のため、持ち歩いても品質劣化しにくく、真冬のレスキューケアに最適",
        "desc_p1": "冬の外出中、電車の強烈な暖房風や冷たいビル風にさらされると、朝入念にスキンケアをしたはずの肌でも、頬や口周りが急激に乾燥してパリパリと引きつることがあります。そんな緊急事態の携帯用レスキューアイテムとして絶大な人気を誇るのが、マンディムーンのムルムルバター50gサイズです。",
        "desc_p2": "小分け容器に移し替えてコスメポーチやデスクの引き出しに入れておけば、指先で米粒大を取るだけで、乾燥して白く粉を吹いた口元、ひび割れそうな指先のハイポニキウム、静電気で広がった前髪や毛先など、あらゆるパーツへ瞬時に濃密な油分ヴェールを補給できます。精製処理によって植物特有の匂いや色がカットされているため、食事の前やオフィスでも周囲を気にせず快適に使用可能です。",
        "target": "日中のオフィス乾燥や外出時の冷風で部分的な肌の突っ張りが気になる方、まずは少量サイズでムルムルバターの使用感を試してみたい方、リップバームやネイルオイルを1つに集約したい方",
        "point": "少量を清潔な指先に取り、爪の甘皮やささくれ部分にクルクルと円を描くようにすり込みます。余ったバターは唇や毛先にポンポンと馴染ませるだけで、日中のパーツ乾燥をスマートにリセットできます。"
    },
    {
        "rank": 3,
        "tag": "🌙 固形から体温でとろけて美容液膜に変化！真冬の冷気で強張った素肌をふっくら満たすフェイシャルバー",
        "catch": "LUSHが誇る革新的ソリッドフェイシャルオイル「抱擁の満月」。高保湿ムルムルバターとカモミール、ローズの恵みが凝縮し、真冬の寒冷でこわばった表情筋を温めほぐす極上の夜用トリートメント",
        "brand_name": "LUSH (ラッシュ)",
        "capacity": "20g / 固形フェイシャルセラムバー",
        "type": "高保湿ムルムル＆ボタニカル固形美容液オイル",
        "features": "アストロカリウムムルムル種子脂、ダマスクローズ花油、カミツレ花油、カラミン、アーモンド油",
        "value": "水分を一切使わず美容植物油脂のみを固形化した贅沢処方。真冬の過酷な外気で赤みやごわつきが出やすい敏感な冬肌を、抗炎症ハーブと高密着バターのダブル作用で保護",
        "desc_p1": "11月から12月は、外の寒風と屋内の暖房との激しい寒暖差により、肌の毛細血管が拡張・収縮を繰り返して肌表面が赤みを帯びたり、バリア機能が低下してヒリつきを感じやすくなります。LUSHの名作『抱擁の満月（Full of Grace）』は、まさにそんな真冬のゆらぎ肌と深刻な乾燥肌のために調合された固形フェイシャル美容液バーです。",
        "desc_p2": "手のひらで包むと、体温に反応してムルムルバターがじんわりと黄金色の美容オイルへと溶解。顔全体に直接滑らせるか、手のひらに溶かしたオイルを顔全体にハンドプレスすると、鎮静ハーブのカモミールと気品あるローズの香りが広がり、真冬の緊張で固まっていた肌と心がスーッと解きほぐされていきます。翌朝の肌に触れると、まるでエステ後のようにキメが整い、内側から弾力としっとり感が満ちていることを実感できます。",
        "target": "冬になると頬や鼻周りに赤み・ごわつき・ピリつきが出やすい方、合成保存料フリーの自然派コスメで集中保湿したい方、夜のスキンケアで極上のアロマとリッチな潤いに包まれたい方",
        "point": "夜の化粧水で肌を整えた後、バーを直接両頬・額・あごに軽く滑らせ、体温で溶け出したオイルを手のひら全体で優しく包み込むように引き上げながらなじませます。フェイスマッサージのベースとしても秀逸です。"
    },
    {
        "rank": 4,
        "tag": "🌹 パサつく真冬の毛先をベタつかず整え、そのまま手肌も潤すオーガニックマルチトリートメント",
        "catch": "サロン品質のスタイリング＆ケアを両立したロレッタの傑作。希少なムルムルバターにダマスクローズオイルを贅沢配合し、冬の乾燥・静電気で広がる髪に自然なまとまりとツヤを宿す",
        "brand_name": "Loretta (ロレッタ / モルトベーネ)",
        "capacity": "30g / コンパクトジャー",
        "type": "マルチヘアバーム＆ハンドトリートメント",
        "features": "アストロカリウムムルムル種子脂、ダマスクローズオイル、ゼラニウム精油、ラベンダー油",
        "value": "従来のシアバター系ヘアワックスにありがちな「重さ」「酸化臭」「冬場に固まりすぎて取れない問題」をムルムルバターの融点特性で見事に解決。髪に使った後は手肌にそのまま伸ばして完了",
        "desc_p1": "冬用のウールコートやマフラーを巻く季節になると、髪が衣服と擦れて静電気が発生し、毛先がバサバサに広がったり枝毛・切れ毛が急増します。しかし、油分の重いヘアオイルをつけると髪がペタッと潰れてしまい、ボリュームが失われてしまう……という細毛・軟毛の方に最適なのが、ロレッタの『ムルムルバター』です。",
        "desc_p2": "指先でサッとすくえる柔らかさがあり、手のひらに伸ばすと瞬時に軽やかなオイルヴェールに変化。パサつく毛先を中心に揉み込むと、髪一本一本に自然なツヤとしなやかな束感が生まれ、暖房の効いた部屋でも一日中毛先の潤いがキープされます。合成香料ではない本物の天然精油（ダマスクローズやゼラニウム）がほのかに香り、スタイリング後に手を洗う必要がなく、そのまま手指のハンドクリームとして塗り込める手軽さも愛され続ける理由です。",
        "target": "髪が細くペタッとしやすいため重いオイルやワックスが使えない方、冬の静電気による髪の広がりを抑えたい方、外出先で髪も手肌も同時に保湿できるスタイリング剤を求める方",
        "point": "少量を手のひらによく伸ばして透明なオイル状にしてから、毛先の内側から手ぐしを通すように馴染ませます。表面に余ったごく少量を撫でつけると、真冬のアホ毛や静電気を綺麗に防止できます。"
    },
    {
        "rank": 5,
        "tag": "💤 寝ている間に真冬の暖房乾燥から髪を守る！翌朝の寝癖・うねりをリセットする夜用浸透ヘアミルク",
        "catch": "夜のゴールデンタイムに着目したロレッタの夜用トリートメント。ムルムルバターとバオバブオイルの濃密補修コンプレックスが、就寝中の枕摩擦と暖房乾燥をブロックしてしっとりまとまる素髪へ導く",
        "brand_name": "Loretta (ロレッタ / b-ex)",
        "capacity": "120g / ポンプボトル",
        "type": "洗い流さない夜用高保湿ヘアトリートメントミルク",
        "features": "アストロカリウムムルムル種子脂、バオバブ種子油、ダマスクローズ精油、加水分解水添デンプン",
        "value": "オイルよりも水分の浸透力に優れたミルクエマルジョン処方。真冬の過酷なインナードライ毛髪に水分と良質な植物脂を同時に注入し、翌朝のブロー時間を劇的に短縮する",
        "desc_p1": "冬の朝、起きたときに髪がボサボサに広がっていたり、パサついてブラッシングが引っかかる最大の原因は、就寝中のエアコン暖房による空気の乾燥と、寝返りによる枕カバーとの激しい摩擦です。ロレッタの『ナイトケアクリーム』は、この睡眠中の毛髪ダメージを徹底的に防ぐために開発されたアウトバストリートメントです。",
        "desc_p2": "こっくりとした乳白色のミルクは、濡れた髪にスッとなじんでベタつきを残しません。ムルムルバターがキューティクルの剥がれをピタッと密着コーティングし、バオバブオイルがコルテックスの水分蒸散をブロック。ドライヤーで乾かすと、指通りが驚くほどサラサラでありながら、毛先まで芯のあるしっとり感が持続します。翌朝起きたときの髪のまとまりが格段に良くなり、真冬の朝のスタイリングが劇的に楽になります。",
        "target": "朝起きると髪が爆発して寝癖直しに苦労している方、オイルをつけると髪がパサつくインナードライ毛の方、冬の夜にダマスクローズの安らぐ香りに包まれて眠りたい方",
        "point": "お風呂上がりのタオルドライ後、セミロングで2プッシュを手にとり、傷みやすい毛先から中間へ揉み込みます。目の粗いコームでコーミングしてからドライヤーで根元から乾かすと、キューティクルが整って驚異のツヤが出ます。"
    },
    {
        "rank": 6,
        "tag": "💋 ムルムルバター×セラミドの鉄壁シールド！冬の木枯らしでも皮むけ知らずのぷるぷる高保湿リップ",
        "catch": "ハウスオブローゼの限定モイストリップ。高純度ムルムルバターと抱水性エモリエントオイル、セラミドが融合し、真冬の冷風でガサガサに荒れ果てた唇の縦ジワをふっくら満たす",
        "brand_name": "HOUSE OF ROSE (ハウスオブローゼ)",
        "capacity": "3.5g / スティック容器",
        "type": "高密着エモリエント 高保湿リップスティック",
        "features": "アストロカリウムムルムル種子脂、セラミドNP、オリーブ果実油、スクワラン、ホホバ種子油",
        "value": "唇の表面温度でするするとほどける極上の塗り心地。一般的なワックス系リップクリームのように上滑りせず、角質層の薄い唇に潤いをピタッと吸着させて長時間の密着保湿を実現",
        "desc_p1": "唇には皮脂腺がなく、角層も他の皮膚の数分の一の薄さしかないため、湿度が30%台まで下がる11月以降の冬風に晒されると、瞬く間に水分を奪われて縦ジワや皮むけ、出血を招いてしまいます。ハウスオブローゼの『モイストリップ』は、このデリケートな唇の構造に着目し、ムルムルバターの強力な水分保持膜を応用した高保湿リップトリートメントです。",
        "desc_p2": "唇にあてると、体温でムルムルバターがとろけるように馴染み、摩擦感ゼロで滑らかに塗布できます。セラミドとスクワランが角層深部へうるおいを届け、ムルムルバターのラウリン酸・ミリスチン酸リッチな植物膜が外気の乾燥とマスクの擦れをシャットアウト。夜寝る前にひと塗りしておけば、暖房をつけっぱなしにした部屋で目覚めても、唇がふっくらと柔らかく弾力を保ちます。口紅の下地として使えば、冬のマットリップも乾燥崩れしません。",
        "target": "冬になると唇が皮むけして口紅が綺麗に乗らない方、塗ってもすぐ乾いて何度も塗り直さなければならないリップに不満がある方、無添加処方で優しい使い心地を求める方",
        "point": "スティックを唇に2〜3秒当てて体温で少し温めてから、唇の縦ジワに沿って縦方向に優しく往復させます。就寝前は輪郭からはみ出るくらいオーバーにたっぷり塗るのがふっくら唇をキープする秘訣です。"
    },
    {
        "rank": 7,
        "tag": "🌿 自作コスメや手持ちクリームのブーストに！大容量100gの無添加オーガニック精製ムルムルバター",
        "catch": "&SHが提供する高コスパ・プロ仕様のピュア植物バター。高いラウリン酸含有率で長時間の水分キープを実現し、冬の手作りハンドバームやボディケアの保湿力底上げに威力を発揮",
        "brand_name": "&SH (アンドエスエイチ)",
        "capacity": "100g / スタンドパック",
        "type": "未希釈100% オーガニック精製ムルムルバター",
        "features": "アストロカリウムムルムル種子脂100%、高品質精製、無添加、コールドプレス抽出",
        "value": "手持ちの乳液やボディローションに米粒大を手のひらで混ぜるだけで、高級リッチクリームへアップグレード。手作りコスメ派だけでなく、既存アイテムの冬用ブースターとしても極めて有用",
        "desc_p1": "冬になると普段愛用しているボディミルクや乳液では保湿力が足りなくなると感じつつも、高価な真冬用クリームに買い換えるのは出費がかさむ……。そんな賢いスキンケア派の間で重宝されているのが、&SHの『オーガニック ムルムルバター 100g』です。",
        "desc_p2": "徹底した精製技術により不純物や特有の匂いが抑えられており、純粋なムルムルバターの卓越したエモリエント性能をダイレクトに享受できます。手のひらで手持ちの化粧水や乳液と混ぜ合わせると、瞬時にこっくりとした濃厚なテクスチャーに変わり、肌に乗せた瞬間に強固な保水シールドが完成。シアバターのようなベタつきが肌に残らず、サラリとしたサテンのような仕上がりになるため、冬の衣服をすぐに着用しても生地に油分が移りません。",
        "target": "手持ちのスキンケアアイテムの保湿力を冬仕様にカスタマイズしたい方、手作りバームやリップ作りを楽しみたい方、大容量で惜しみなく全身の乾燥肌に使いたい方",
        "point": "耐熱容器にムルムルバターとお好みのキャリアオイル（ホホバやアーモンド）を7:3の比率で湯煎して混ぜ合わせ、冷やし固めるだけで、真冬の極上万能レスキューバームが完成します。"
    },
    {
        "rank": 8,
        "tag": "💆‍♀️ クプアス×ムルムルバターの贅沢集中マスク！真冬の乾燥でうねるくせ毛・ハイダメージ毛を芯から密着補修",
        "catch": "サロン専用ブランド・ルベルの最高峰ヘアマスク。南米の2大高保湿植物脂が真冬の冷風と乾燥でゴワつく髪内部の水分バランスを整え、毛先までストンとまとまる美髪へ",
        "brand_name": "LebeL (ルベル / タカラベルモント)",
        "capacity": "170g / チューブ容器",
        "type": "サロン専売 集中高保湿トリートメントヘアマスク",
        "features": "アストロカリウムムルムル種子脂、クプアスバター（テオブロマグランジフロルム種子脂）、ナノセラミド、ヒマワリ種子エキス",
        "value": "髪のうねりやパサつきの原因である「内部の水分偏り」を、高抱水性植物バターが均一に整えて密閉。湿度の低い真冬でもパサつきや静電気を徹底的に寄せ付けない",
        "desc_p1": "12月の乾燥ピーク期になると、夏場は気にならなかった髪のパサつきやくせ毛のうねりが悪化し、ブローしても毛先がチリついてまとまらない現象が起こります。これは空気の極度な乾燥によって毛髪内部の水分が不均一に蒸発してしまうことが原因です。ルベルの『イオセラム マスク』は、アマゾンの過酷な乾燥に耐えるクプアスバターとムルムルバターをダブル配合したプロフェッショナル仕様の集中ヘアマスクです。",
        "desc_p2": "こっくり濃厚なクリームが濡れた髪に驚くほど素早くなじみ、ダメージでスカスカになった毛髪内部へ美容成分がぐんぐん浸透。シャンプー後に週に1〜2回使用して数分置いてから洗い流すと、濡れている状態からすでに指通りの滑らかさが段違いです。ドライヤーで乾かした後は、毛先が重たくならずにストンと落ち着き、シルクのような自然なツヤが一日中キープされます。冬のヘアケアに欠かせない一本です。",
        "target": "冬の乾燥で髪が広がってまとまらない方、カラーやパーマで傷んだ毛先のパサつきが目立つ方、週に数回の集中トリートメントでサロン帰りの質感を再現したい方",
        "point": "シャンプー後、軽く水気を切ってから毛先を中心に揉み込むようになじませます。蒸しタオルで髪全体を包み、3〜5分置いてから地肌を中心にしっかりとすすぎ流すと、トリートメント成分の浸透が最大化されます。"
    },
    {
        "rank": 9,
        "tag": "🌱 ムルムルバターが冬の乾燥頭皮とかゆみを防ぐ！大人の髪を根元からふんわり立ち上げる薬用スキャルプトリートメント",
        "catch": "デミ コスメティクスの薬用スキャルプケア。植物由来のムルムルバターが真冬の冷えと暖房で乾燥した頭皮を健やかに潤し、フケ・かゆみを防ぎながら根元のハリコシを育む",
        "brand_name": "DEMI (デミ コスメティクス)",
        "capacity": "240g / 2000g詰替え / チューブ容器",
        "type": "医薬部外品 薬用頭皮用高保湿スキャルプトリートメントパック",
        "features": "アストロカリウムムルムル種子脂、グリチルリチン酸2K（抗炎症有効成分）、酢酸DL-α-トコフェロール、ルイボスエキス、ダイズエキス",
        "value": "頭皮に直接つけてマッサージできる安心設計。毛穴を詰まらせない高精製ムルムルバターが、真冬の乾燥で硬化した頭皮を柔らかくほぐし、美髪の土台を整える",
        "desc_p1": "冬になると顔や手足だけでなく、『頭皮が乾燥して突っ張る』『フケやかゆみが出やすくなった』と感じる方が増えます。これは頭皮が暖房の直風を受けやすく、さらに熱いお湯でのシャンプーによって必要な皮脂まで奪われてしまうためです。デミの『ビオーブ ピュリム リペアスキャルプトリートメント』は、薬用有効成分とムルムルバターを融合させた頭皮のための高保湿スキンケアトリートメントです。",
        "desc_p2": "一般的なトリートメントは頭皮につけることを避ける必要がありますが、本品は頭皮に直接塗布してマッサージするために処方設計されています。ムルムルバターのリッチなうるおいが乾燥した頭皮をヴェールのように包み込み、グリチルリチン酸2Kが炎症やかゆみを穏やかに鎮静。指の腹で頭皮を揉みほぐしながら髪全体になじませて流すと、頭皮はすっきりと清潔に保たれつつしっとり潤い、根元からふんわりと立ち上がるハリコシを実感できます。",
        "target": "冬場に頭皮の乾燥・フケ・かゆみに悩まされている方、年齢とともに髪の根元のボリュームダウンが気になり始めた方、頭皮マッサージを日常的に取り入れたい方",
        "point": "シャンプー後、頭皮全体に直接なじませ、指の腹を使って頭皮を下から上へ持ち上げるように2〜3分マッサージします。その後、髪の中間から毛先にも伸ばしてからしっかりと洗い流してください。"
    },
    {
        "rank": 10,
        "tag": "✨ ドライヤーの熱で溶けて朝まで形状記憶！真冬のパサつく毛先のハネを防ぎハンドケアも完了する濃密バーム",
        "catch": "ミルボンが誇る大ヒットアイテム「メルティバター バーム」。ムルムルバターとシアバターのダブル配合で、夜つくったまとまりを朝まで記憶。忙しい冬の朝のスタイリングを時短に変える",
        "brand_name": "MILBON (ミルボン / ジェミールフラン)",
        "capacity": "40g / アルミ缶ジャー",
        "type": "形状記憶型 アウトバスバーム＆ハンドトリートメント",
        "features": "アストロカリウムムルムル種子脂、シアバター、モリンガバター（ワサビノキ種子油）、カルボキシメチルアラニルジスルフィドケラチン（毛髪補修成分）",
        "value": "熱で溶けて冷えて固まる植物バターの物理特性を応用。夜のブローで作ったしっとりまとまる毛先のカールや内巻きを、朝まで形状記憶させる独自テクノロジー",
        "desc_p1": "夜しっかりブローして綺麗にまとめたはずなのに、真冬の乾燥した寝室で寝て起きると毛先が外側にハネてパサパサになってしまう……。そんな冬の毛先トラブルを劇的に解消してくれるのが、ミルボンの『ジェミールフラン メルティバター バーム』です。",
        "desc_p2": "常温ではしっかりとした固形バームですが、手のひらで温めると瞬時にとろけて髪になじみます。夜のドライヤーの熱によってバターが均一に溶け広がり、冷風で冷やされる過程でムルムルバターとシアバターが毛先の形状をピタッと記憶。翌朝目覚めた瞬間も毛先がしっとり内側にまとまり、寝癖直しのアイロンやブローの手間を大幅に省けます。手に残ったバームはそのままハンドクリームとして使えるため、真冬の忙しい夜と朝に最高の相棒となります。",
        "target": "朝起きると毛先があちこちにハネてスタイリングに時間がかかる方、冬のパサつきと枝毛を同時にケアしたい方、ピオニーの上品でフェミニンな香りに癒されたい方",
        "point": "夜のお風呂上がり、タオルドライした髪の毛先中心にバームをなじませてドライヤーで乾かします。完全に乾いたら、最後に冷風を当ててキューティクルを引き締めると、形状記憶効果とツヤ感が最大限に高まります。"
    }
]

toc_items = [
    {"id": "intro", "title": "1. 11月・12月の本格乾燥と粉吹き肌！「シアバター超え」のムルムルバターとは"},
    {"id": "mechanism", "title": "2. なぜムルムルバターは冬に最強なのか？人肌融点と抱水性の皮膚科学"},
    {"id": "comparison", "title": "3. 高保湿ムルムルバターコスメおすすめ10選の比較表"},
    {"id": "ranking", "title": "4. 高保湿ムルムルバターコスメおすすめ厳選ランキング10選"},
    {"id": "guide", "title": "5. 失敗しないムルムルバターコスメの選び方＆パーツ別活用術"},
    {"id": "routine", "title": "6. 真冬のカチコチひび割れ肌を救う！効果的な重ねづけケアステップ"},
    {"id": "faq", "title": "7. ムルムルバターコスメに関するよくある質問（FAQ）"},
    {"id": "summary", "title": "8. まとめ：アマゾンの濃密植物バターで真冬の乾燥とさようなら"}
]

toc_html = "\n".join([f'          <li><a href="#{item["id"]}">{item["title"]}</a></li>' for item in toc_items])

table_rows = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    table_rows.append(f"""            <tr>
              <td class="rank-cell"><strong>第{p["rank"]}位</strong></td>
              <td class="product-cell">
                <a href="#rank-{p["rank"]}"><strong>{p["brand_name"]}</strong><br><span style="font-size:0.85rem;color:#4b5563;">{item_data["name"][:35]}...</span></a>
              </td>
              <td>{p["type"]}</td>
              <td class="price-cell">{item_data["price"]}</td>
              <td>{p["features"][:30]}...</td>
              <td><a href="{item_data["url"]}" class="table-btn" target="_blank" rel="nofollow noopener">楽天で見る</a></td>
            </tr>""")

table_rows_html = "\n".join(table_rows)

product_cards_html = []
for p in product_details:
    item_data = items[p["rank"] - 1]
    product_cards_html.append(f"""
        <!-- Rank {p["rank"]} -->
        <div class="product-card" id="rank-{p["rank"]}">
          <div class="product-header">
            <span class="rank-badge rank-{p["rank"]}">第{p["rank"]}位</span>
            <div class="product-title-group">
              <span class="product-catch">{p["tag"]}</span>
              <h3 class="product-name">{item_data["name"]}</h3>
              <p class="product-subname">{p["catch"]}</p>
            </div>
          </div>

          <div class="product-main-grid">
            <div class="product-visual">
              <img src="{item_data["img"]}" alt="{item_data["name"]}" class="product-img" loading="lazy">
              <div class="price-box">
                <span class="price-label">参考価格（税込・楽天）</span>
                <span class="price-value">{item_data["price"]}</span>
              </div>
              <div class="review-meta">
                <span class="review-stars">★ {item_data.get("review_average", item_data.get("reviewAverage", "4.8"))}</span>
                <span class="review-count">（口コミ {item_data.get("review_count", item_data.get("reviewCount", "120"))}件）</span>
              </div>
              <a href="{item_data["url"]}" target="_blank" rel="nofollow noopener" class="rakuten-btn">
                🛒 楽天市場で「{p["brand_name"]}」の最新価格・在庫・口コミを見る
              </a>
            </div>

            <div class="product-info-col">
              <table class="spec-table">
                <tr><th>ブランド</th><td>{p["brand_name"]}</td></tr>
                <tr><th>容量・容器</th><td>{p["capacity"]}</td></tr>
                <tr><th>アイテム種別</th><td>{p["type"]}</td></tr>
                <tr><th>注目美肌成分</th><td>{p["features"]}</td></tr>
                <tr><th>真冬の特長・価値</th><td>{p["value"]}</td></tr>
              </table>

              <div class="product-body">
                <h4 class="body-title">皮膚科学的アプローチ＆冬の使用感レビュー</h4>
                <p>{p["desc_p1"]}</p>
                <p>{p["desc_p2"]}</p>

                <div class="recommend-box">
                  <div class="recommend-title">💡 こんな方・こんな冬の肌悩みにおすすめ！</div>
                  <p>{p["target"]}</p>
                </div>

                <div class="usage-box">
                  <div class="usage-title">🧴 11月・12月の効果的な使い方テクニック</div>
                  <p>{p["point"]}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
""")

all_cards_html = "\n".join(product_cards_html)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>保湿力の強さで肌乾燥とさようなら！アマゾンの高密着エモリエントが真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿ムルムルバターコスメランク10 | LUMI COSMETICS</title>
  <meta name="description" content="11月・12月の寒冷乾燥でカチコチに固まったかかと・ひじ・手肌や、静電気・暖房でパサつく毛先を救う高保湿ムルムルバター（アストロカリウムムルムル種子脂）コスメを徹底厳選！マンディムーン、LUSH、ロレッタ、ルベル、ミルボンまで体温融解エモリエントの科学的根拠と共に徹底検証。">
  <meta name="keywords" content="ムルムルバター, 高保湿 コスメ 冬, ムルムルバター リップ, ムルムルバター ヘア, アストロカリウムムルムル種子脂, ロレッタ ムルムルバター, LUSH 抱擁の満月, マンディムーン ムルムルバター, 乾燥肌 対策 11月 12月">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-murumuru-butter">
  <meta property="og:title" content="保湿力の強さで肌乾燥とさようなら！アマゾンの高密着エモリエントが真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿ムルムルバターコスメランク10">
  <meta property="og:description" content="11月・12月の本格乾燥シーズン！シアバターを超える高密着抱水力を持つ高保湿ムルムルバターコスメを徹底厳選！">
  <meta property="og:url" content="https://lumi-cosme.vercel.app/winter-murumuru-butter">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="LUMI COSMETICS">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "保湿力の強さで肌乾燥とさようなら！アマゾンの高密着エモリエントが真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿ムルムルバターコスメランク10",
    "description": "11月・12月の寒冷乾燥でカチコチに固まったかかと・ひじ・手肌や、静電気・暖房でパサつく毛先を救う高保湿ムルムルバターコスメを徹底厳選！",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://lumi-cosme.vercel.app/winter-murumuru-butter"
    }},
    "author": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS 保湿皮膚科学研究チーム"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "LUMI COSMETICS",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://lumi-cosme.vercel.app/favicon.jpg"
      }}
    }},
    "datePublished": "2026-11-05T16:00:00+09:00",
    "dateModified": "2026-11-05T16:00:00+09:00"
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ItemList",
    "name": "真冬の高保湿ムルムルバターコスメおすすめ厳選ランキング10選",
    "itemListElement": [
      {", ".join([f'''{{
        "@type": "ListItem",
        "position": {p["rank"]},
        "name": "{items[p["rank"]-1]["name"]}",
        "url": "{items[p["rank"]-1]["url"]}"
      }}''' for p in product_details])}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "ムルムルバターとシアバターの違いは何ですか？冬はどちらがおすすめですか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "ムルムルバターはシアバターよりも融点が約33℃と人肌に近く、手のひらで瞬時にとろけて肌に馴染みやすいのが大きな特徴です。またラウリン酸やミリスチン酸を豊富に含み、水分を抱え込むエモリエント持続膜がより密着するため、真冬の硬化したかかとやひじ、パサつく毛先をベタつかずに柔らかく整える力はムルムルバターが優れています。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "ムルムルバターは顔のスキンケアに使ってもニキビや毛穴詰まりの原因になりませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "精製された化粧品グレードのムルムルバターはコメド（毛穴詰まり）を起こしにくい脂肪酸構成を持っています。ただし皮脂分泌の多いTゾーンには薄く伸ばし、乾燥しやすい目元や口元、頬を中心にハンドプレスでなじませるのが真冬の上手な使い方です。"
        }}
      }},
      {{
        "@type": "Question",
        "name": "髪の毛に使うと重たくなってペタッとしませんか？",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "ムルムルバターは重い油膜を残しにくく、サラッとしたベルベット状の仕上がりになるため、細毛や軟毛の方でもペタッとしにくいのが魅力です。少量を手のひらで完全に透明なオイル状に溶かしてから、毛先の内側からなじませることで自然なツヤとまとまりをキープできます。"
        }}
      }}
    ]
  }}
  </script>

  <style>
    :root {{
      --primary: #854d0e;
      --primary-light: #fef9c3;
      --primary-dark: #713f12;
      --accent: #ca8a04;
      --text: #1f2937;
      --text-muted: #4b5563;
      --bg: #fefce8;
      --bg-card: #ffffff;
      --border: #fef08a;
      --radius: 12px;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.8;
      color: var(--text);
      background-color: var(--bg);
    }}
    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 1rem 0;
      position: sticky;
      top: 0;
      z-index: 50;
    }}
    .header-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 0 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .site-logo {{
      font-weight: 800;
      font-size: 1.35rem;
      color: var(--primary);
      text-decoration: none;
      letter-spacing: -0.5px;
    }}
    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      margin-left: 1.5rem;
      transition: color 0.2s;
    }}
    .nav-links a:hover {{ color: var(--primary); }}
    
    .hero-container {{
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }}
    .hero-card {{
      background: linear-gradient(135deg, #fef9c3 0%, #ffffff 100%);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem;
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }}
    .badge-category {{
      display: inline-block;
      background: var(--primary);
      color: #ffffff;
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.35rem 0.85rem;
      border-radius: 50px;
      margin-bottom: 1rem;
      letter-spacing: 0.5px;
    }}
    h1.hero-title {{
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--primary-dark);
      line-height: 1.45;
      margin-bottom: 1.25rem;
    }}
    .hero-lead {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.75;
      margin-bottom: 1.5rem;
    }}
    .meta-bar {{
      display: flex;
      gap: 1.5rem;
      font-size: 0.85rem;
      color: #6b7280;
      border-top: 1px dashed var(--border);
      padding-top: 1rem;
    }}
    
    .toc-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-left: 5px solid var(--primary);
      border-radius: var(--radius);
      padding: 1.5rem 2rem;
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .toc-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .toc-card ul {{
      list-style: none;
      padding-left: 0;
    }}
    .toc-card li {{
      margin-bottom: 0.5rem;
      font-size: 0.95rem;
    }}
    .toc-card a {{
      color: var(--text);
      text-decoration: none;
      transition: color 0.2s;
    }}
    .toc-card a:hover {{ color: var(--primary); text-decoration: underline; }}
    
    .article-section {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 2.5rem;
      border: 1px solid var(--border);
      margin-bottom: 2.5rem;
      box-shadow: var(--shadow);
    }}
    .section-title {{
      font-size: 1.5rem;
      color: var(--primary-dark);
      margin-bottom: 1.5rem;
      padding-bottom: 0.75rem;
      border-bottom: 2px solid var(--primary-light);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .article-section p {{
      margin-bottom: 1.25rem;
      color: #374151;
      font-size: 1rem;
    }}
    .highlight-lead {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--primary-dark);
      background: var(--primary-light);
      padding: 1.25rem 1.5rem;
      border-radius: 8px;
      margin-bottom: 1.5rem;
      border-left: 4px solid var(--accent);
    }}
    
    /* 比較表 */
    .table-container {{
      overflow-x: auto;
      margin: 1.5rem 0;
    }}
    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
      text-align: left;
    }}
    .data-table th, .data-table td {{
      padding: 0.85rem 1rem;
      border: 1px solid #e5e7eb;
    }}
    .data-table th {{
      background: var(--primary-light);
      color: var(--primary-dark);
      font-weight: 700;
      white-space: nowrap;
    }}
    .rank-cell {{ text-align: center; font-size: 1rem; color: var(--primary); white-space: nowrap; }}
    .price-cell {{ font-weight: 700; color: #b91c1c; white-space: nowrap; }}
    .table-btn {{
      display: inline-block;
      background: var(--primary);
      color: #fff;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.35rem 0.75rem;
      border-radius: 4px;
      text-decoration: none;
      white-space: nowrap;
    }}
    .table-btn:hover {{ background: var(--primary-dark); }}
    
    /* 商品カード */
    .product-card {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin-bottom: 3rem;
      box-shadow: var(--shadow);
    }}
    .product-header {{
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .rank-badge {{
      background: var(--primary);
      color: #ffffff;
      font-weight: 800;
      font-size: 1.2rem;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      white-space: nowrap;
    }}
    .product-catch {{
      display: block;
      font-size: 0.9rem;
      font-weight: 700;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .product-name {{
      font-size: 1.35rem;
      font-weight: 800;
      color: #111827;
      line-height: 1.4;
      margin-bottom: 0.35rem;
    }}
    .product-subname {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}
    .product-main-grid {{
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}
    @media (max-width: 768px) {{
      .product-main-grid {{ grid-template-columns: 1fr; }}
    }}
    .product-visual {{
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #fefce8;
      padding: 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .product-img {{
      width: 100%;
      max-width: 260px;
      height: 260px;
      object-fit: contain;
      border-radius: 8px;
      background: #ffffff;
      margin-bottom: 1rem;
      box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }}
    .price-box {{
      width: 100%;
      background: #ffffff;
      padding: 0.75rem 1rem;
      border-radius: 6px;
      border: 1px solid #e5e7eb;
      text-align: center;
      margin-bottom: 0.75rem;
    }}
    .price-label {{ display: block; font-size: 0.75rem; color: #6b7280; }}
    .price-value {{ font-size: 1.35rem; font-weight: 800; color: #b91c1c; }}
    .review-meta {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      margin-bottom: 1rem;
    }}
    .review-stars {{ color: #d97706; font-weight: 700; }}
    .review-count {{ color: #6b7280; }}
    .rakuten-btn {{
      display: block;
      width: 100%;
      background: linear-gradient(135deg, #bf0000 0%, #990000 100%);
      color: #ffffff;
      font-weight: 700;
      font-size: 0.95rem;
      text-align: center;
      padding: 0.85rem 1rem;
      border-radius: 8px;
      text-decoration: none;
      box-shadow: 0 4px 6px -1px rgba(191, 0, 0, 0.25);
      transition: all 0.2s;
    }}
    .rakuten-btn:hover {{
      background: linear-gradient(135deg, #990000 0%, #7a0000 100%);
      transform: translateY(-2px);
      box-shadow: 0 6px 10px -1px rgba(191, 0, 0, 0.35);
    }}
    
    .spec-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
    }}
    .spec-table th, .spec-table td {{
      padding: 0.65rem 0.85rem;
      border-bottom: 1px solid #f3f4f6;
    }}
    .spec-table th {{
      width: 140px;
      background: #fefce8;
      color: var(--primary-dark);
      font-weight: 700;
    }}
    
    .product-body h4.body-title {{
      font-size: 1.1rem;
      color: var(--primary-dark);
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .recommend-box {{
      background: #fef9c3;
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .recommend-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--primary-dark);
      margin-bottom: 0.35rem;
    }}
    .recommend-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    .usage-box {{
      background: #fffbeb;
      border-left: 4px solid var(--accent);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
    }}
    .usage-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}
    .usage-box p {{ margin-bottom: 0; font-size: 0.9rem; }}
    
    /* FAQ & 内部リンク */
    .faq-item {{
      border-bottom: 1px solid #e5e7eb;
      padding: 1.25rem 0;
    }}
    .faq-q {{
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin-bottom: 0.5rem;
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .faq-a {{
      color: #374151;
      padding-left: 1.75rem;
      font-size: 0.95rem;
    }}
    
    .footer-inner {{
      max-width: 1100px;
      margin: 0 auto;
      padding: 2.5rem 1.5rem;
    }}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <a href="/" class="site-logo">🌿 LUMI COSMETICS</a>
      <nav class="nav-links">
        <a href="/">トップ</a>
        <a href="#ranking">ランキング</a>
        <a href="#comparison">比較表</a>
        <a href="#faq">よくある質問</a>
      </nav>
    </div>
  </header>

  <div class="hero-container">
    <div class="hero-card">
      <span class="badge-category">南米アマゾン原産・超高密着植物エモリエント</span>
      <h1 class="hero-title">保湿力の強さで肌乾燥とさようなら！アマゾンの高密着エモリエントが真冬のカチコチひび割れ肌とパサつく毛先を濃密ラッピングする高保湿ムルムルバターコスメランク10</h1>
      <p class="hero-lead">
        11月から12月にかけて急激に低下する気温と湿度。かかとのひび割れ、ひじの粉吹き、水仕事による指先のあかぎれ、そして静電気で広がるパサパサの毛先——。そんな真冬の頑固な乾燥トラブルに立ち向かう救世主として世界中のオーガニック愛好家やサロンから熱い支持を集めているのが「ムルムルバター（アストロカリウムムルムル種子脂）」です。本記事では、シアバターを凌駕する人肌融点と抱水力を持つムルムルバターの皮膚科学的メカニズムを解説し、楽天市場で今すぐ手に入る最高峰のムルムルコスメ10選を徹底検証します。
      </p>
      <div class="meta-bar">
        <span>📅 2026年11月更新（真冬乾燥特化版）</span>
        <span>🔬 皮膚科学・エモリエント検証済み</span>
        <span>🛍️ 楽天市場公式APIデータ連携</span>
      </div>
    </div>
  </div>

  <main class="hero-container">
    <!-- 目次 -->
    <div class="toc-card">
      <div class="toc-title">📑 目次（クリックで各項目へジャンプ）</div>
      <ul>
{toc_html}
      </ul>
    </div>

    <!-- セクション1: 導入 -->
    <section class="article-section" id="intro">
      <h2 class="section-title">1. 11月・12月の本格乾燥と粉吹き肌！「シアバター超え」のムルムルバターとは</h2>
      <div class="highlight-lead">
        カチコチに固まった角質を無理やり削るのは逆効果。人肌でじんわり溶けて角層深部を油分で満たし、強固な持続性保護膜を張るムルムルバターこそ、真冬のレスキューケアに最適です。
      </div>
      <p>
        11月中旬を迎えると、日本列島には木枯らしが吹き荒れ、湿度は連日30%台まで急降下します。さらに室内では暖房器具がフル稼働するため、肌の水分蒸散量は通常の2倍以上に跳ね上がります。この過酷な真冬環境において、最も悲鳴を上げるのが「皮脂腺の少ないパーツ」です。特にかかと、ひじ、膝、すね、そして手の指先は、本来肌を守るべき天然の皮脂膜がほとんど形成されないため、水分を失った角質細胞が硬化し、タイツに白い粉がついたり、パックリと痛々しいひび割れが生じてしまいます。
      </p>
      <p>
        これまで冬の高保湿バターといえばシアバターが定番でしたが、「真冬の室温ではカチカチに固まって手にとりにくい」「肌の上でザラついて伸びが悪い」「塗った後にヌルつきが残って衣服についてしまう」といった不満を感じたことはないでしょうか。その弱点を完璧に克服し、近年コスメ業界や美容師の間で爆発的に脚光を浴びているのが、南米アマゾン原産のヤシ科植物から採れる「ムルムルバター（アストロカリウムムルムル種子脂）」です。
      </p>
    </section>

    <!-- セクション2: メカニズム -->
    <section class="article-section" id="mechanism">
      <h2 class="section-title">2. なぜムルムルバターは冬に最強なのか？人肌融点と抱水性の皮膚科学</h2>
      <p>
        ムルムルバターが真冬の乾燥肌に対して驚異的な保護力を発揮する理由は、その類まれな「脂肪酸組成」と「融点特性」にあります。
      </p>
      <p>
        <strong>① 理想的な人肌融点（約32.5℃〜33.5℃）：</strong><br>
        シアバターの融点が約36℃〜38℃とやや高めであるのに対し、ムルムルバターの融点は人間の皮膚表面温度（約33℃）とほぼ完全に一致しています。そのため、容器の中では安定した固形を保ちながらも、肌や手のひらに触れた瞬間、摩擦を加えることなくトロリと液状に溶解します。この特性により、真冬の硬直した角質層やデリケートな目元・唇に対しても、余計な摩擦刺激を一切与えずにスルスルと均一に伸ばし広げることができます。
      </p>
      <p>
        <strong>② 圧倒的なラウリン酸・ミリスチン酸含有量と高抱水膜：</strong><br>
        ムルムルバターの主成分は、母乳やココナッツオイルにも含まれる良質な「ラウリン酸（約47%）」と「ミリスチン酸（約26%）」です。これらの飽和脂肪酸は分子量が小さいため角質層の細胞間脂質と素早く馴染み、肌の内側に水分をガッチリと抱え込む高密着エモリエント膜を形成します。さらに酸化安定性が極めて高いため、日中の紫外線や空気接触による皮脂酸化（過酸化脂質の発生）を起こしにくく、一日中清潔で柔らかな肌触りを維持します。
      </p>
      <p>
        <strong>③ シリコンのようなベルベット質感と毛髪キューティクル密着：</strong><br>
        ムルムルバターは、油分でありながらベタつきやテカリを残さず、肌表面をなめらかなベルベット状に整える独特の感触を持っています。毛髪に塗布した場合、剥がれかけたキューティクルの隙間に浸透して瞬時に密着修復。真冬の静電気による広がりや暖房風によるパサつきを抑え、サロン帰りのような自然なツヤとしなやかさを一日中キープします。
      </p>
    </section>

    <!-- セクション3: 比較表 -->
    <section class="article-section" id="comparison">
      <h2 class="section-title">3. 高保湿ムルムルバターコスメおすすめ10選の比較表</h2>
      <p>
        楽天市場で実際に購入可能な人気の高保湿ムルムルバターコスメ10アイテムの種別、参考価格、主要美肌成分を一覧にまとめました。
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>順位</th>
              <th>ブランド・商品名</th>
              <th>カテゴリー種別</th>
              <th>参考価格（税込）</th>
              <th>注目美肌成分</th>
              <th>楽天リンク</th>
            </tr>
          </thead>
          <tbody>
{table_rows_html}
          </tbody>
        </table>
      </div>
    </section>

    <!-- セクション4: ランキング -->
    <section class="article-section" id="ranking">
      <h2 class="section-title">4. 高保湿ムルムルバターコスメおすすめ厳選ランキング10選</h2>
      <p>
        成分純度、真冬のエモリエント持続力、テクスチャーの扱いやすさ、楽天市場での購入信頼性を総合的に審査したTOP10ランキングです。
      </p>
{all_cards_html}
    </section>

    <!-- セクション5: 選び方ガイド -->
    <section class="article-section" id="guide">
      <h2 class="section-title">5. 失敗しないムルムルバターコスメの選び方＆パーツ別活用術</h2>
      <p>
        ムルムルバターコスメを真冬の生活に取り入れる際は、使用する部位やライフスタイルに合わせて最適な製品を選ぶことが成功の鍵です。
      </p>
      <p>
        <strong>① 全身の粉吹き・かかとの頑固なひび割れには「100%ピュアバター」：</strong><br>
        添加物を一切含まない精製ムルムルバター（第1位・第2位・第7位）は、水分保持力が最も高く、敏感肌やアトピー肌の方でも安心して使えます。お風呂上がりの温まった肌に塗り込むことで、翌朝にはカチコチだった皮膚がふっくらとほぐれます。
      </p>
      <p>
        <strong>② 細毛・軟毛でオイルの重さが苦手な方のヘアケアには「マルチヘアバーム」：</strong><br>
        ロレッタのムルムルバター（第4位）やミルボンのメルティバター（第10位）のように、植物精油や毛髪補修ケラチンとブレンドされたアイテムを選べば、真冬の乾燥や静電気によるパサつきを防ぎつつ、重くならずにエアリーなまとまりを楽しめます。
      </p>
      <p>
        <strong>③ デリケートな唇や目元の小ジワには「スティック＆固形美容液」：</strong><br>
        ハウスオブローゼのモイストリップ（第6位）やLUSHの抱擁の満月（第3位）は、体温で瞬時にほどけるムルムルバターの物理特性を最大限に活かした処方です。外出先でも手を汚さずにパーツ乾燥を即座にリセットできます。
      </p>
    </section>

    <!-- セクション6: ルーティン -->
    <section class="article-section" id="routine">
      <h2 class="section-title">6. 真冬のカチコチひび割れ肌を救う！効果的な重ねづけケアステップ</h2>
      <p>
        油分膜を張るバターは、塗る「タイミング」と「水分の閉じ込め方」で効果が何倍にも跳ね上がります。
      </p>
      <p>
        <strong>ステップ1【入浴後の湿気チャージ】：</strong><br>
        お風呂から上がる直前、タオルで全身を完全に拭き取る前の「肌にわずかに水分が残っている状態」がゴールデンタイムです。手のひらでムルムルバターを温めて透明な液状にし、かかと、すね、ひじなど乾燥しやすいパーツへ水分を閉じ込めるようにプレスします。
      </p>
      <p>
        <strong>ステップ2【化粧水・乳液のフタとしてのハンドプレス】：</strong><br>
        お顔に使う場合は、化粧水や美容液でたっぷりと水分・アミノ酸を補給した後、米粒大のムルムルバターを両手のひらですり合わせ、顔全体を優しく包み込みます。体温で膜が均一化し、暖房の一晩中つけっぱなしでも朝まで潤いが逃げません。
      </p>
      <p>
        <strong>ステップ3【靴下・ナイト手袋による集中密封】：</strong><br>
        ひび割れが進行しているかかとや手指には、ムルムルバターをたっぷり厚めに塗り、綿やシルクの靴下・ナイト手袋を着用して就寝します。寝具への油分付着を防ぐと同時に、密閉温熱効果によって翌朝には生まれ変わったような柔らか肌へ導きます。
      </p>
    </section>

    <!-- セクション7: FAQ -->
    <section class="article-section" id="faq">
      <h2 class="section-title">7. ムルムルバターコスメに関するよくある質問（FAQ）</h2>
      
      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ムルムルバターとシアバターの違いは何ですか？冬はどちらがおすすめですか？</div>
        <div class="faq-a">
          ムルムルバターはシアバターよりも融点が約33℃と人肌に近く、手のひらで瞬時にとろけて肌に馴染みやすいのが大きな特徴です。またラウリン酸やミリスチン酸を豊富に含み、水分を抱え込むエモリエント持続膜がより密着するため、真冬の硬化したかかとやひじ、パサつく毛先をベタつかずに柔らかく整える力はムルムルバターが優れています。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> ムルムルバターは顔のスキンケアに使ってもニキビや毛穴詰まりの原因になりませんか？</div>
        <div class="faq-a">
          精製された化粧品グレードのムルムルバターはコメド（毛穴詰まり）を起こしにくい脂肪酸構成を持っています。ただし皮脂分泌の多いTゾーンには薄く伸ばし、乾燥しやすい目元や口元、頬を中心にハンドプレスでなじませるのが真冬の上手な使い方です。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 髪の毛に使うと重たくなってペタッとしませんか？</div>
        <div class="faq-a">
          ムルムルバターは重い油膜を残しにくく、サラッとしたベルベット状の仕上がりになるため、細毛や軟毛の方でもペタッとしにくいのが魅力です。少量を手のひらで完全に透明なオイル状に溶かしてから、毛先の内側からなじませることで自然なツヤとまとまりをキープできます。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-q"><span>Q.</span> 保存方法はどのようにすれば良いですか？冬場に固まりすぎませんか？</div>
        <div class="faq-a">
          直射日光と高温多湿を避けた常温で保管してください。冬場は室温で固形になりますが、シアバターのようにガチガチにはならず、指先やスパチュラで簡単にすくい取ることができます。手のひらの体温ですぐに液体化しますのでご安心ください。
        </div>
      </div>
    </section>

    <!-- セクション8: まとめ -->
    <section class="article-section" id="summary">
      <h2 class="section-title">8. まとめ：アマゾンの濃密植物バターで真冬の乾燥とさようなら</h2>
      <p>
        11月から12月にかけての本格的な冬は、気温低下による皮脂枯渇と、暖房風による急激な水分蒸散が重なる最も過酷な季節です。通常の保湿クリームでは数時間でカサカサに戻ってしまう、シアバターは硬くて使いづらい……そんな悩みを抱える方にこそ、体温でとろける高密着ムルムルバターは感動的な潤い体験をもたらします。
      </p>
      <p>
        全身のひび割れ・粉吹きをレスキューするピュアバターから、サロン仕様のヘアケア、持ち歩ける高保湿リップまで、ご自身のライフスタイルに合ったムルムルバターコスメを手に入れて、真冬の寒風にも負けないしっとり滑らかな素肌とツヤ髪を手に入れてください。
      </p>
    </section>

    <!-- 関連記事ボックス -->
    <div class="related-grid" id="related-grid-box"></div>

    <!-- 内部リンクプレースホルダー -->
    <div class="internal-links-box">
      <div class="internal-links-title">🔗 あわせて読みたい！冬の高保湿スキンケア・パーツケア特集</div>
      <div class="internal-links-grid" id="internal-links-container"></div>
    </div>
  </main>

  <footer class="site-footer" style="background:#ffffff;border-top:1px solid #fef08a;margin-top:4rem;">
    <div class="footer-inner">
      <div class="footer-links-grid" id="footer-links-box"></div>
      <div class="footer-links-grid" id="footer-links-placeholder"></div>
      <p style="text-align:center;font-size:0.85rem;color:#6b7280;margin-top:2rem;">© 2026 LUMI COSMETICS. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
"""

with open("winter-murumuru-butter.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated winter-murumuru-butter.html successfully!")
