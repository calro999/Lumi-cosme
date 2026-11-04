import json
import re

with open("fetched_final_30_tamanu_baobab_kombucha.json", "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["winter_kombucha"]["items"]

# 各商品ごとの完全オリジナルなレビュー＆詳細データ
product_details = [
    {
        "rank": 1,
        "tag": "✨ 発酵紅茶×乳酸菌バイオーム！寒さでどんより濁った冬枯れ肌に透き通る水光ツヤを宿す極上トナー",
        "catch": "韓国ハイエンドスキンケアLAVIENが誇る発酵コンブチャ化粧水。じっくり発酵熟成させた紅茶エキスと美肌菌バイオームが、真冬の寒冷でこわばった角層を瞬時にほぐし、満水状態の発光ガラススキンへ導く最高峰トナー",
        "brand_name": "LAVIEN (ラヴィアン)",
        "capacity": "150ml / プレミアムポンプボトル",
        "type": "高保湿・角層発酵トリートメント化粧水",
        "features": "発酵紅茶エキス（コンブチャ）、マイクロバイオーム複合体、8重ヒアルロン酸、アデノシン",
        "value": "エステ級の圧倒的なツヤ肌効果でリピーター続出。一度の使用で乾燥くすみとゴワつきが一掃され、冬のファンデーションがピタッと吸い付くように密着する贅沢体験",
        "desc_p1": "11月から12月にかけて寒さが本格化すると、毛細血管が収縮して血行不良に陥り、顔全体がどんよりと土気色にくすんで生気を失ってしまいます。さらにエアコン暖房によって角層の水分が蒸発し、表面はテカるのに内側はカラカラという深刻な『冬のインナードライ』が多発します。この冬の複合トラブルを一撃で晴らしてくれるのが、LAVIENの『コンブバイオーム ディープハイドレーション フェイシャルトナー』です。",
        "desc_p2": "厳選された紅茶葉を酵母と乳酸菌でじっくり発酵させて生まれたコンブチャ発酵液には、天然のポリフェノール、有機酸、ビタミンB群が凝縮されています。少しとろみのあるまろやかな液をハンドプレスすると、冬の寒さで硬直した角質層へみるみる吸い込まれ、8重のヒアルロン酸が角層深部から水分をパンパンに満たします。表面にはベタつきを残さず、まるで肌の内側から発光しているかのようなみずみずしい『水光ツヤ（ガラススキン）』が誕生。夕方になってもくすまず、冴え渡る透明感が持続します。",
        "target": "冬になると顔色がどんよりくすんで疲れて見えやすい方、インナードライで化粧ノリが悪い方、発酵コスメでワンランク上のツヤ肌を目指したい方",
        "point": "洗顔後、適量を手のひらに取り、顔全体を優しく包み込むようにハンドプレスします。特に乾燥やくすみが気になる日は、コットンにたっぷり含ませて3分間ローションパックをすると、サロン帰りのような透明ツヤ肌が即座に手に入ります。"
    },
    {
        "rank": 2,
        "tag": "💎 高濃度発酵紅茶エキス濃縮！寒暖差と暖房で乱れた肌バリアを集中再建するレスキューアンプル",
        "catch": "コンブチャの強力な抗酸化・鎮静パワーを高濃度に凝縮したプレミアム美容液。冬の室内外の寒暖差ストレスでピリつく敏感肌を素早く穏やかに鎮め、ピンとしたハリ弾力で満たす集中ケアアンプル",
        "brand_name": "LAVIEN (ラヴィアン)",
        "capacity": "50ml / スポイト付きボトル",
        "type": "高純度・高保湿鎮静カーミングセラム",
        "features": "高濃度コンブチャ発酵液、シカ（ツボクサエキス）、パンテノール、ナイアシンアミド",
        "value": "少量で驚くほどの伸びと密着感。冬の冷風で赤みが出やすい頬や、暖房でちりめんジワが寄った目元・口元を濃密な発酵ヴェールで強力に保護",
        "desc_p1": "冬の外出先から暖房の効いた部屋に入った瞬間、頬がカッと火照って赤くなったり、ヒリヒリとした刺激を感じたりする『寒暖差ショック』。肌の自律神経とバリア機能が悲鳴を上げているサインです。LAVIENの『コンブバイオーム ディープハイドラ カーミングアンプル』は、発酵紅茶エキスの抗炎症力とシカ・パンテノールの鎮静成分を融合させ、真冬のデリケートな肌を緊急レスキューしてくれます。",
        "desc_p2": "スポイトから取り出すと、とろりとした琥珀色の濃密なセラム。肌に乗せた瞬間、ヒンヤリと心地よい水分感とともに角層深くまでスーッと浸透していきます。コンブチャ由来のグルコン酸やアミノ酸が肌のキメをキュッと整え、ナイアシンアミドが冬の乾燥による小ジワやくすみにアプローチ。塗った直後から肌の内側がもっちりと吸い付くような弾力で満たされ、真冬の乾燥冷気にさらされても赤みやツッパリ感を一切寄せ付けません。",
        "target": "真冬の寒暖差で肌が敏感になり赤みが出やすい方、乾燥によるハリ不足や小ジワを本気でケアしたい方、濃厚な美容液で肌密度を高めたい方",
        "point": "化粧水で肌を整えた後、スポイト1〜2滴を顔全体に伸ばし、指先で優しくタッピングしながら馴染ませます。特に乾燥しやすい目尻やほうれい線には重ねづけすると、ふっくらとしたハリが蘇ります。"
    },
    {
        "rank": 3,
        "tag": "💦 506時間熟成発酵のミクロミスト！メイクの上から冬の砂漠肌を瞬時に水光リセット",
        "catch": "506時間じっくり低温発酵させたコンブチャエキスを微細なミストに凝縮。日中のエアコン暖房で干からびた肌にシュッとひと吹きするだけで、微粒子ミストが肌を潤し夕方のメイク崩れを完全に防ぐ神ミスト",
        "brand_name": "elishacoy (エリシャコイ)",
        "capacity": "100ml / エアゾールフリー微細スプレーボトル",
        "type": "発酵紅茶バイオーム高保湿ミスト化粧水",
        "features": "506時間熟成コンブチャ発酵抽出物（酵母/キシリヌム/紅茶発酵物）、アミノ酸複合体、植物性スクワラン",
        "value": "ガス不使用でありながら超微細なフォグミストを実現。メイクを一切崩さず、オフィスや外出先でも乾燥を感じた瞬間に極上の水分チャージが可能",
        "desc_p1": "冬の午後、暖房の温風を直接浴び続けていると、肌表面の水分がどんどん奪われ、ファンデーションが粉を吹いたり毛穴に落ちたりしてしまいます。『今すぐ水分補給したいけれど、普通の水ミストを吹きかけると蒸発時に余計乾燥する…』そんな冬のミスト難民を救うのが、エリシャコイの『コンブチャ ギョルバイオームミスト』です。",
        "desc_p2": "スプレーを押すと、まるで霧のように超微細なミストがふんわりと顔全体を包み込みます。水っぽさが肌表面に残らず、506時間発酵のコンブチャエキスと植物性スクワランが瞬時に角層へ密着。日中の乾燥でごわついた肌がスーッとほぐれ、メイク仕立てのみずみずしい透明感とツヤがその場で復活します。ガスを使っていないため環境にも優しく、オフィスや機内など乾燥が過酷な場所での常備コスメとして圧倒的人気を博しています。",
        "target": "オフィスの暖房乾燥で日中にメイクが粉吹き崩れする方、手軽に持ち歩ける高保湿ミストを探している方、ベタつかずツヤだけを足したい方",
        "point": "顔から20〜30cmほど離し、目を閉じて顔全体に円を描くように3〜4回スプレーします。吹きかけた後は手で触らず、自然に角層へ吸い込まれるのを待つだけで、崩れない発光ツヤ肌が完成します。"
    },
    {
        "rank": 4,
        "tag": "🗽 NY発ラグジュアリー！汚染物質と冬の寒冷ダメージから肌を保護する最高峰エッセンス",
        "catch": "世界中のセレブリティに愛されるFreshのブラックティーコンブチャコレクション。微小な抗酸化シールドが、真冬の寒冷・乾燥・都市汚染から肌を鉄壁ガードし、吸い付くようなハリ弾力を呼び覚ます",
        "brand_name": "Fresh (フレッシュ)",
        "capacity": "150ml / プレステージガラスボトル",
        "type": "最高峰プレミアムトリートメントエッセンス",
        "features": "高濃度発酵ブラックティー（コンブチャ）、ヒアルロン酸、マンダリン果皮エキス、キゲリアアフリカーナ果実エキス",
        "value": "ラグジュアリーブランドならではの圧倒的な浸透力と気品ある香り。冬のエイジングサインを根本から跳ね返し、サロン帰りのような気品ある輝きを演出",
        "desc_p1": "冬の肌ダメージは、乾燥や寒さだけでなく、空気中に浮遊する微小粒子状物質やストレスによって肌内部に過剰なフリーラジカルが発生することでも加速します。Freshの『ブラックティー コンブチャ フェイシャルトリートメント エッセンス』は、発酵ブラックティーが持つ強力な抗酸化力に着目し、肌表面に見えないプロテクトシールドを形成してあらゆる外的ダメージを無力化します。",
        "desc_p2": "洗顔後の素肌に数滴馴染ませると、上質な紅茶のアロマが心地よく香り、スキンケアの時間が極上のスパ体験へと変わります。サラリとした感触でありながら肌に伸ばした瞬間に深く浸透し、キメのひとつひとつが水分でふっくらと膨らむのを指先で実感。キゲリアアフリカーナ果実エキスが冬の寒さでたるみがちなフェイスラインを引き締め、内側から押し返すような弾力と上品なツヤをもたらします。",
        "target": "最高品質のプレミアム発酵コスメで贅沢にお手入れしたい方、冬の乾燥小ジワやたるみ毛穴を根本からケアしたい方、紅茶の優雅な香りに癒されたい方",
        "point": "手のひらに5〜6滴を取り、手のひら全体に広げてから、顔の中心から外側へ向かって優しくプレスします。首筋やデコルテまで滑らせるように馴染ませると、デコルテ周りの乾燥くすみも一掃されます。"
    },
    {
        "rank": 5,
        "tag": "🍊 フルーツ幹細胞×コンブチャ！冬の不要な角質を摩擦レスでオフするつっぱらない洗顔ジェル",
        "catch": "アメリカのオーガニック名門アンダルーナチュラルズが誇る名品洗顔ジェル。コンブチャ発酵液とフルーツ幹細胞が、冬の乾燥で硬化した角質や毛穴汚れを優しく溶かし出し、洗い上がりはつっぱり知らずの透明肌",
        "brand_name": "ANDALOU NATURALS (アンダルーナチュラルズ)",
        "capacity": "178ml / チューブタイプ",
        "type": "弱酸性・高保湿オーガニッククレンジングジェル",
        "features": "オーガニックコンブチャエキス、フルーツ幹細胞複合体、柳皮エキス（天然サリシン）、アロエベラ液汁",
        "value": "ノンコメドジェニック・低刺激処方。冬の朝洗顔としても最適で、余分な皮脂汚れだけをオフして天然の水分膜を守り抜く高コスパオーガニック",
        "desc_p1": "冬の朝、鏡を見た時に肌がゴワついてくすんでいるからといって、洗浄力の強い洗顔料やスクラブを使ってしまうと、肌に必要な皮脂まで洗い流されて日中の乾燥崩れが致命的になります。アンダルーナチュラルズのクレンジングジェルは、発酵紅茶エキスのマイルドな天然有機酸（AHA様作用）を利用し、摩擦を一切かけずに不要な古い角質だけを優しく浮き上がらせてくれます。",
        "desc_p2": "手にとると、みずみずしいジェルからフレッシュな柑橘の爽やかな香りが広がります。水を加えて軽く泡立てて肌を滑らせると、アロエベラベースの潤いジェルがクッションとなり、指先の摩擦をゼロに抑えながら毛穴の酸化皮脂を吸着。ぬるま湯で洗い流した瞬間、まるで肌が一皮剥けたようにパッと明るい透明感が現れ、触ると吸い付くように柔らかく、つっぱり感は皆無です。その後の化粧水の浸透が劇的にアップします。",
        "target": "冬の朝洗顔後につっぱりやすい方、毛穴の黒ずみや角栓を肌に負担なくケアしたい方、爽やかなシトラスの香りで朝のリフレッシュをしたい方",
        "point": "濡らした手のひらに500円玉大を取り、軽く泡立ててから顔全体を優しく滑らせるように洗います。小鼻やあご先などザラつきが気になる部分は、指の腹で小さな円を描くように撫でてからぬるま湯で丁寧にすすぎます。"
    },
    {
        "rank": 6,
        "tag": "🌱 発酵紅茶×植物性ヴィーガンコラーゲン！真冬のしぼみ肌にハリのラップをかける濃密クリーム",
        "catch": "韓国クリーンビューティーHERBLOOMが開発した発酵コンブチャ×ヴィーガンコラーゲンの高保湿クリーム。冬の寒冷と暖房で干からびて弾力を失った肌に、濃密な水分膜とふっくらハリを密閉チャージ",
        "brand_name": "HERBLOOM (ハーブルーム)",
        "capacity": "50ml / エコフレンドリージャー",
        "type": "高保湿・弾力ヴィーガンコラーゲンクリーム",
        "features": "発酵紅茶エキス（コンブチャ）、植物性ヴィーガンコラーゲン、シアバター、セラミドNP",
        "value": "韓国ヴィーガン認証取得。動物性原料や合成香料を完全排除し、肌にも環境にも優しいエシカル処方でありながら、真冬の過酷な乾燥を跳ね返す圧倒的な保湿力",
        "desc_p1": "真冬になると、肌内部の水分とコラーゲンが失われ、頬の位置が下がったように感じたり、フェイスラインのハリが低下したりと『冬枯れたるみ』が進行します。ハーブルームのヴィーガンコラーゲンクリームは、発酵コンブチャの豊富な栄養素と酵母発酵で作られた植物性コラーゲンを贅沢にドッキングさせ、肌表面に濃密な弾力ネットを張り巡らせてくれます。",
        "desc_p2": "こっくりとした滑らかなテクスチャーでありながら、肌に伸ばすと体温でバターのようにとろけてピタッと密着。セラミドNPとシアバターが強固なエモリエント膜を形成し、夜塗って眠れば暖房を一晩中つけた寝室でも朝まで全く乾燥しません。翌朝の肌はまるでスチームを当てた後のようにふっくらと押し返すような弾力に満ち、キメが整ってメイクのりが格段に良くなります。",
        "target": "冬の乾燥で肌のハリ不足やたるみ毛穴が気になる方、ヴィーガン処方の高機能エイジングケアクリームを探している方、こっくり濃厚な保湿感が好きな方",
        "point": "スキンケアの最後に、パール大をスパチュラで取り、手のひらで温めてから顔全体に引き上げるように伸ばします。乾燥が激しい目元や首元には少量を重ね塗りし、最後に手のひらで温めるホットプレスを行うと効果的です。"
    },
    {
        "rank": 7,
        "tag": "🍊 清柑柚子×発酵紅茶の贅沢アロマ！冬の乾燥ボディと髪にツヤと香りを届けるマルチミスト",
        "catch": "お茶の力で肌と心を癒す韓国TEA BLESSの大ヒットパフュームミスト。発酵コンブチャエキスと柚子セラミドが融合し、冬のパサつく髪や粉吹きやすいボディにみずみずしい潤いと上品なティーノートをプラス",
        "brand_name": "TEA BLESS (ティーブレス)",
        "capacity": "100ml / スプレーボトル",
        "type": "高保湿ヘア＆ボディフレグランスミスト",
        "features": "発酵コンブチャエキス、柚子エキス（柚子セラミド）、パンテノール、ツバキ種子油",
        "value": "香水のように変化する奥深いシトラスティーの香りを楽しみながら、真冬の静電気や乾燥による粉吹きを一本で即効リペアできるマルチパーパス名品",
        "desc_p1": "冬は服を脱いだ時にすねや腕がカサカサと粉を吹いていたり、マフラーを取った瞬間に髪が静電気でフワフワ浮いてしまったりと、ボディや髪の乾燥にも悩まされる季節です。TEA BLESSのパフュームミストは、上質なフレグランスと本格的な高保湿スキンケアを両立させた画期的なアイテムです。",
        "desc_p2": "シュッと吹きかけると、清らかな青みかんと柚子の爽快感に、発酵紅茶の深みのあるアールグレイノートが重なり合い、冬の寒さで縮こまった心がホッとほぐれます。微粒子ミストに含まれる柚子セラミドとコンブチャエキスが、乾燥した肌や髪のキューティクルに瞬時に吸着。ベタつきを残さずサラリとしたシルクのような手触りに整え、冬の静電気を防ぎながら一日中ふんわりと心地よい香りをまとわせます。",
        "target": "冬のボディや髪の乾燥・静電気を同時にケアしたい方、きつすぎない上品なお茶の香りのフレグランスが好きな方、オフィスでのリフレッシュに使いたい方",
        "point": "お風呂上がりのボディ全体や、スタイリング前のパサつく髪に15cmほど離してスプレーします。マフラーやコートの内側に軽く吹きかけておくと、動くたびに上品な柚子紅茶の香りがふわりと香ります。"
    },
    {
        "rank": 8,
        "tag": "💆‍♀️ オーガニックハーブティー水仕込み！冬の頭皮乾燥フケ・かゆみを防ぐ濃密スカルプケア",
        "catch": "ベースの水にまでこだわり、オーガニックハーブティー水と発酵コンブチャエキスを贅沢に使用。冬の冷気と乾燥で荒れやすい頭皮環境を健やかに整え、根元からふんわり立ち上がる美髪を育む",
        "brand_name": "HERBANIENCE (ハーバニエンス)",
        "capacity": "300ml / エコパウチ・ボトル",
        "type": "アミノ酸系高保湿オーガニックスカルプシャンプー",
        "features": "発酵紅茶エキス（コンブチャ）、南阿蘇産オーガニックハーブティー水、植物性アミノ酸洗浄成分、バオバブ種子油",
        "value": "石油系界面活性剤・シリコン・合成香料不使用。サロン品質のアミノ酸濃密泡で頭皮の潤いを守りながら優しく洗い上げ、真冬のフケやかゆみを根本からブロック",
        "desc_p1": "冬になると、顔の皮膚だけでなく頭皮も強烈な乾燥にさらされています。外気の乾燥や熱いお湯での洗髪によって頭皮の皮脂膜が失われ、パラパラとした細かいフケが出たり、頭皮が痒くなったりするトラブルが急増します。ハーバニエンスは、精製水の代わりにオーガニックハーブティー水をベースにし、そこに発酵コンブチャエキスを溶け込ませた究極のスカルプケアシャンプーです。",
        "desc_p2": "ポンプから出すと、天然ハーブとシトラスラベンダーの心が洗われるような香りが浴室を満たします。アミノ酸系の洗浄成分がキメ細やかなもっちり濃密泡を作り出し、頭皮と髪の摩擦を完全にゼロにしながら汚れだけを吸着。コンブチャ由来の酵母菌や有機酸が頭皮の善玉菌環境（スカルプマイクロバイオーム）を整え、洗い流した後は頭皮がつっぱらずみずみずしい潤い感が続きます。根元からふんわりとしたハリコシが蘇ります。",
        "target": "冬になると頭皮の乾燥フケやかゆみに悩まされる方、髪のボリューム不足やパサつきを改善したい方、自然由来成分にこだわったシャンプーを選びたい方",
        "point": "ぬるま湯（38度前後）で頭皮をしっかり予洗いした後、適量を手のひらで泡立てて頭皮に乗せます。指の腹で頭皮を揉みほぐすようにマッサージしながら洗い、泡を1分ほど置いて『泡パック』してからしっかりすすぎます。"
    },
    {
        "rank": 9,
        "tag": "🌿 死海ミネラル×発酵コンブチャ！冬の冷えで血行不良になったどんより肌を覚醒させるクレイマスク",
        "catch": "英国発オーガニックマスクブランドEarth Kissが手掛ける濃密シートマスク。死海由来の豊富なミネラル泥と発酵紅茶エキスが、冬の冷えと暖房でくすんだ肌を15分間でリフレッシュする集中トリートメント",
        "brand_name": "Earth Kiss (アースキス)",
        "capacity": "1回分（美容液たっぷり含有）/ 個包装シートマスク",
        "type": "オーガニック発酵ミネラルシートマスク",
        "features": "発酵紅茶エキス（コンブチャ）、死海ミネラルクレイ、シカエキス、アロエベラ液汁",
        "value": "エコサートコスモスオーガニック認証取得。100%植物性生分解性シートを採用し、冬の肌にミネラルと発酵の栄養を集中補給できるスペシャルケア",
        "desc_p1": "真冬の週末、一週間の寒さと暖房によるストレスで肌が疲れ果て、どんよりとくすんでツヤを失っている時にこそ投入したいのが、Earth Kissのコンブチャシートマスクです。古来より美肌の聖地として知られる死海のミネラルソルトと、発酵紅茶エキスの抗酸化パワーを組み合わせ、自宅にいながら本格的なタラソ発酵スパを体験できます。",
        "desc_p2": "封を開けると、ミネラルとハーブの心地よいアロマが広がり、美容液をひたひたに含んだ肌触りの良いシートが肌に吸い付くようにピタッと密着。死海の豊富なマグネシウムやカルシウムが冬の冷えで滞った巡りをサポートし、コンブチャ発酵液が乾燥した角質を柔らかく解きほぐします。15分後にシートを剥がすと、まるで温泉から上がった直後のように血色感が巡り、白く澄み渡るような透明感とふっくらした弾力が復活します。",
        "target": "週末にスペシャルな集中美肌トリートメントを行いたい方、冬のくすみや血行不良を速攻でリセットしたい方、オーガニック認証シートマスクを好む方",
        "point": "洗顔後、化粧水で肌を軽く整えた後にシートを隙間なく密着させます。15分置いた後、シートを剥がし、肌表面に残った濃密美容液を手のひらでハンドプレスして馴染ませます。残った液は首やデコルテにも塗り広げましょう。"
    },
    {
        "rank": 10,
        "tag": "🧬 紅茶発酵液×マルチペプチド！真冬の乾燥小ジワをふっくら持ち上げ水光ツヤを保つ高保湿セラム",
        "catch": "発酵コンブチャの保水力とマルチペプチドのハリ弾力アプローチを融合させた進化系美容液。真冬の過酷な乾燥環境下でも水分蒸散を防ぎ、内側から押し返すようなキメ密度と輝くガラススキンを実現",
        "brand_name": "K-Glow Lab (コンブチャバイオーム)",
        "capacity": "30ml / スポイト付き遮光ガラスボトル",
        "type": "高濃度発酵ペプチドエイジングケア美容液",
        "features": "発酵紅茶エキス（コンブチャ）、アセチルヘキサペプチド-8、パルミトイルトリペプチド-5、ヒアルロン酸Na",
        "value": "分子量の異なるペプチドを贅沢にブレンド。冬の冷えや乾燥による目元・口元の乾燥小ジワをピンポイントでケアし、使うほどに肌密度が高まるサロン処方",
        "desc_p1": "年齢とともに肌のコラーゲン産生力は低下しますが、冬の寒冷刺激とエアコンの強烈な乾燥が加わると、皮膚のハリを支える土台が一気に崩れ、深いシワやたるみ毛穴へと進行してしまいます。K-Glow Labのコンブチャセラムは、紅茶発酵液の抗酸化・角層柔軟作用をベースに、表情ジワや乾燥シワにアプローチするマルチペプチドを高濃度に配合しています。",
        "desc_p2": "みずみずしく軽やかなテクスチャーでありながら、肌に伸ばすと吸い付くように角層へと浸透。ペプチドが角質層のすみずみまで行き渡り、乾燥でしぼんだ角質細胞を内側からピンと持ち上げるようなハリ感を与えます。コンブチャ由来の有機酸がキメをキュッと引き締めるため、毛穴の開きも目立たなくなり、光を均一に反射するつるんとした陶器肌が一日中キープされます。",
        "target": "冬の乾燥小ジワやハリ不足を同時にケアしたい方、キメ密度の高い水光ツヤ肌を作りたい方、ペプチド配合の高機能美容液を試したい方",
        "point": "化粧水の直後、スポイトから1〜2滴を取り、気になる目尻、ほうれい線、おでこを中心に優しく引き上げるように伸ばします。ハンドプレスでじっくり押し込むことで、内側からパンとした弾力が蘇ります。"
    }
]

# FAQ 生成
faqs = [
    {
        "q": "コンブチャ（Kombucha / 発酵紅茶エキス）は、冬の肌にどのような美肌効果をもたらすのですか？",
        "a": "コンブチャは紅茶や緑茶にスコビー（酵母菌・酢酸菌の共生体）を加えて発酵させた伝統的な発酵飲料・エキスです。発酵のプロセスによって、紅茶に含まれるポリフェノール（カテキンやテアフラビン）が超微細化され、さらに乳酸、グルコン酸、酢酸などの『天然有機酸』や『ビタミンB群・アミノ酸』が爆発的に増加します。11月〜12月の寒さで血行が悪くなり、暖房乾燥で角層がゴワついた冬枯れ肌に対して、角質を摩擦レスで柔軟にしながら深部まで水分を行き渡らせ、内側から発光するようなみずみずしい透明感（水光ツヤ）を取り戻す効果があります。"
    },
    {
        "q": "昆布（海藻）のコンブチャとは違うのですか？肌につけても紅茶の香りがしますか？",
        "a": "名前に『コンブ』と入っているため海藻の昆布茶と混同されやすいですが、コスメで使われるコンブチャは100%『発酵紅茶（または発酵茶葉）』のエキスです。海藻臭さは一切なく、多くのアイテムでは上質で気品あるアールグレイやシトラスティーの心地よい香りが漂います。スキンケアのたびに心地よいティーアロマでリフレッシュでき、真冬のストレスから解放されるリラクゼーション効果も抜群です。"
    },
    {
        "q": "発酵コスメ特有の刺激や、肌に合わない心配はありませんか？",
        "a": "コンブチャは微生物による自然発酵によって成分が細かく分解されているため、分子が小さく肌への親和性が極めて高いのが特徴です。また弱酸性に保たれているため、冬の寒冷や暖房乾燥でアルカリ性に傾きがちな敏感肌のpHバランスを健康な弱酸性へと整える効果があります。アルコールやパラベンを排除した低刺激処方のアイテムが多く、冬のデリケートな肌でも安心してお使いいただけますが、重度の酵母アレルギーをお持ちの方は事前にパッチテストを行うことを推奨します。"
    },
    {
        "q": "11月〜12月のスキンケアで、コンブチャコスメを取り入れる最もおすすめのステップは？",
        "a": "最も即効性を実感できるのは『洗顔直後の化粧水（トナー）または導入エッセンス』としての活用です。寒さで硬化した角質層にコンブチャの発酵エキスが浸透することで、硬直した細胞がスーッとほぐれ、肌が水分をごくごく飲み込む満水スポンジ状態になります。さらに日中にエアコン暖房で乾燥を感じた時は、エリシャコイのような『コンブチャミスト』をメイクの上から吹きかけると、夕方の乾燥くすみと粉吹き崩れを完全に防ぐことができます。"
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
            "name": "保湿力の強さで肌乾燥とさようなら！発酵紅茶の力で冬の血行不良くすみ＆角層枯れを一掃する高保湿コンブチャコスメランク10",
            "description": "11月・12月の冷えによる血行不良と暖房インナードライを救う高保湿コンブチャ（発酵紅茶エキス）コスメを徹底厳選！LAVIEN、エリシャコイ、Fresh、アンダルーナチュラルズ、HERBLOOMまで厳選。",
            "numberOfItems": 10,
            "itemListElement": schema_items
        },
        {
            "@type": "Article",
            "headline": "保湿力の強さで肌乾燥とさようなら！発酵紅茶の力で冬の血行不良くすみ＆角層枯れを一掃する高保湿コンブチャコスメランク10",
            "description": "11月・12月の冷えによる血行不良と暖房インナードライを救う高保湿コンブチャ（発酵紅茶エキス）コスメを徹底厳選！LAVIEN、エリシャコイ、Fresh、アンダルーナチュラルズ、HERBLOOMまで厳選。",
            "image": items[0]["image"],
            "datePublished": "2026-11-04T22:00:00+09:00",
            "dateModified": "2026-11-04T22:00:00+09:00",
            "inLanguage": "ja",
            "mainEntityOfPage": "https://lumi-cosme.vercel.app/winter-kombucha"
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
  <title>保湿力の強さで肌乾燥とさようなら！発酵紅茶の力で冬の血行不良くすみ＆角層枯れを一掃する高保湿コンブチャコスメランク10 | Lumi Cosme</title>
  <meta name="description" content="11月・12月の冷えによる血行不良と暖房インナードライを救う高保湿コンブチャ（発酵紅茶エキス）コスメを徹底厳選！LAVIEN、エリシャコイ、Fresh、アンダルーナチュラルズ、HERBLOOMまで、楽天市場で買える本物の高保湿10選を詳しく解説。">
  <meta name="keywords" content="コンブチャ コスメ,発酵紅茶 スキンケア,LAVIEN トナー,エリシャコイ コンブチャミスト,冬 くすみ 保湿,インナードライ 発酵化粧水,水光ツヤ肌">
  <link rel="canonical" href="https://lumi-cosme.vercel.app/winter-kombucha">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #854d0e;
      --primary-dark: #713f12;
      --primary-light: #fef9c3;
      --accent: #ca8a04;
      --text-main: #1f2937;
      --text-sub: #4b5563;
      --text-light: #6b7280;
      --bg-page: #fefce8;
      --bg-card: #ffffff;
      --border-color: #fef08a;
      --shadow-sm: 0 2px 4px rgba(133, 77, 14, 0.05);
      --shadow-md: 0 4px 12px rgba(133, 77, 14, 0.1);
      --shadow-lg: 0 10px 25px -5px rgba(133, 77, 14, 0.15);
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
      background: linear-gradient(135deg, #713f12 0%, #854d0e 50%, #ca8a04 100%);
      color: #ffffff;
      padding: 2.2rem 1.5rem 2.8rem;
      text-align: center;
      box-shadow: 0 4px 20px rgba(113, 63, 18, 0.25);
    }}
    .site-header-nav {{
      max-width: 1100px;
      margin: 0 auto 1.25rem;
      text-align: left;
    }}
    .site-header-nav a {{
      color: #fef9c3;
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
      color: #fef9c3;
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
      background: linear-gradient(to right bottom, #fef9c3, #fefce8);
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
      background: linear-gradient(135deg, #fefce8 0%, #fef9c3 100%);
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
      background: #fefce8;
      border: 1px solid #fef08a;
    }}
    .point-block {{
      background: #fffbeb;
      border: 1px solid #fde68a;
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
    <h1>保湿力の強さで肌乾燥とさようなら！発酵紅茶の力で冬の血行不良くすみ＆角層枯れを一掃する高保湿コンブチャコスメランク10</h1>
    <p>11月・12月の冷えによる血行不良と暖房インナードライを一掃。発酵紅茶（コンブチャ）の酵母・ポリフェノール・有機酸の恵みで、真冬でも内側から発光する極上の水光透明肌へ</p>
  </header>

  <main class="container">
    <section class="intro-card">
      <span class="intro-badge">11月〜12月・冬の血行不良くすみ＆インナードライ撃退特集</span>
      <h2>なぜ11〜12月のどんより冬枯れ肌に「発酵紅茶（コンブチャ）」が劇的に効くのか？</h2>
      <p>11月から12月へと進むにつれて、気温の急激な低下に伴い私たちの体内では皮膚表面の毛細血管をぎゅっと縮めて熱を逃がさない防御反応が働きます。しかしこの生体反応の代償として、顔の皮膚細胞への酸素や栄養の供給が滞り、肌全体がどんよりと灰色がかった『冬の寒冷くすみ・血行不良』が引き起こされます。</p>
      <p>さらに追い打ちをかけるのが、オフィスや自宅の強力なエアコン暖房です。温風にさらされた角質層からは水分が急速に奪われ、キメが萎縮して光を綺麗に反射できなくなります。その結果、肌表面には古い角質が居座ってゴワつき、いくらファンデーションを塗っても夕方には土気色に沈んでしまうのです。この『血行不良・角質硬化・乾燥くすみ』の三重苦を同時に解決する鍵として、いま世界中で空前の注目を浴びているのが『コンブチャ（発酵紅茶エキス）』です。</p>
      
      <div class="science-box">
        <h3>🔬 科学が解き明かす「コンブチャ発酵液」の抗酸化＆水光ツヤメカニズム</h3>
        <p>コンブチャ（学名：Saccharomyces/Xylinum/Black Tea Ferment）は、厳選された紅茶葉にスコビー（酵母と酢酸菌の共生体）を加えて長期間じっくり発酵熟成させた植物発酵エキスです。発酵の神秘的な力により、紅茶本来の強力なポリフェノール（テアフラビンやカテキン）が微細分子化され、細胞への抗酸化浸透力が飛躍的にアップします。</p>
        <p>さらに発酵の過程で、肌のキメを整える<strong>『天然有機酸（グルコン酸・乳酸）』</strong>、角層の代謝を助ける<strong>『ビタミンB群』</strong>、そして保湿力を司る<strong>『高濃度アミノ酸』</strong>が生成。角質を傷つけることなく古い角質を優しく緩め、微細な発酵保水膜が角層深くまで満ちることで、内側から光を放つような透明感溢れる『水光肌（ガラススキン）』を呼び覚まします。</p>
      </div>

      <p>本記事では、楽天市場で実際に購入できる正規取り扱いアイテムの中から、韓国ハイエンドブランドLAVIENからNY名門Fresh、オーガニックミストまで、冬枯れ肌に圧倒的な透明感と潤いをもたらす高保湿コンブチャコスメ厳選10選を詳しくご紹介します。</p>

      <div class="toc-card">
        <h3>📑 目次：高保湿コンブチャコスメTOP10</h3>
        <ul class="toc-list">
          <li><a href="#rank-1">第1位：LAVIEN コンブバイオーム トナー</a></li>
          <li><a href="#rank-2">第2位：LAVIEN コンブバイオーム カーミングアンプル</a></li>
          <li><a href="#rank-3">第3位：elishacoy コンブチャ ギョルバイオームミスト</a></li>
          <li><a href="#rank-4">第4位：Fresh ブラックティー コンブチャ エッセンス</a></li>
          <li><a href="#rank-5">第5位：ANDALOU NATURALS シトラスコンブチャ クレンジング</a></li>
          <li><a href="#rank-6">第6位：HERBLOOM コンブチャ ヴィーガン コラーゲンクリーム</a></li>
          <li><a href="#rank-7">第7位：TEA BLESS パフューム 清柑柚子コンブチャミスト</a></li>
          <li><a href="#rank-8">第8位：HERBANIENCE オーガニック スカルプシャンプー</a></li>
          <li><a href="#rank-9">第9位：Earth Kiss オーガニック 発酵コンブチャ マスク</a></li>
          <li><a href="#rank-10">第10位：K-Glow Lab コンブチャ ペプチド グロウセラム</a></li>
        </ul>
      </div>
    </section>

    <section class="table-section">
      <h2>🏆 高保湿コンブチャコスメおすすめ比較一覧</h2>
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
      <h2>💡 失敗しない高保湿コンブチャコスメの選び方＆活用術</h2>
      
      <h3>1. 「発酵濃度」と「プラス配合成分」に注目する</h3>
      <p>コンブチャコスメを選ぶ際は、単に紅茶エキスが入っているだけでなく、どのような発酵菌（酵母・酢酸菌）で熟成されているか、そして冬の肌悩みに合わせたサポート成分が何かが重要です。極度のインナードライやくすみが気になる場合は、LAVIENやFreshのようにマイクロバイオーム（乳酸菌複合体）やヒアルロン酸が組み合わされたトナーやエッセンスが最適です。また日中の暖房乾燥対策には、持ち歩きに便利な微粒子ミストを携帯すると一日中ツヤ肌をキープできます。</p>

      <div class="guide-grid">
        <div class="guide-card">
          <h4>発酵化粧水・エッセンス</h4>
          <p>洗顔直後の角層にたっぷり水分と有機酸をチャージ。古い角質を緩めて満水状態を作り、発光するような透明感を呼び起こします。</p>
        </div>
        <div class="guide-card">
          <h4>濃縮アンプル・美容液</h4>
          <p>寒暖差ストレスでピリつく肌を集中鎮静。ナイアシンアミドやペプチドとの相乗効果で、冬の乾燥小ジワをふっくら持ち上げます。</p>
        </div>
        <div class="guide-card">
          <h4>携帯用マイクロミスト</h4>
          <p>オフィスや外出先での暖房乾燥を即座にリセット。メイクの上から微細な水分ヴェールを吹きかけ、夕方のくすみ崩れを阻止します。</p>
        </div>
      </div>

      <h3>2. 11月〜12月のくすみ肌を晴らす「3分間ローションパック」手順</h3>
      <p>冬の血行不良くすみとゴワつきを最速で解消したい朝は、コンブチャ化粧水を使った『集中ローションパック』が劇的な効果を発揮します。</p>
      <ol style="margin-left: 1.5rem; margin-bottom: 1rem; color: var(--text-sub); line-height: 1.8;">
        <li><strong>コットンを湿らせる：</strong> 大判のコットンにコンブチャ化粧水を裏面までヒタヒタになるくらいたっぷり含ませます。</li>
        <li><strong>薄く裂いて密着：</strong> コットンを3〜4枚に薄く割き、両頬、おでこ、あご先に隙間なくピタッと貼り付けます。</li>
        <li><strong>3分間で剥がす：</strong> 3分経ったら剥がし、肌表面に残った発酵エキスを優しくハンドプレス。驚くほど透明感溢れる水光肌に仕上がります。</li>
      </ol>
    </section>

    <section class="faq-section">
      <h2>❓ コンブチャスキンケアに関するよくある質問（FAQ）</h2>
      <div class="faq-item">
        <div class="faq-q">コンブチャ（Kombucha / 発酵紅茶エキス）は、冬の肌にどのような美肌効果をもたらすのですか？</div>
        <div class="faq-a">コンブチャは紅茶や緑茶にスコビー（酵母菌・酢酸菌の共生体）を加えて発酵させた伝統的な発酵飲料・エキスです。発酵のプロセスによって、紅茶に含まれるポリフェノール（カテキンやテアフラビン）が超微細化され、さらに乳酸、グルコン酸、酢酸などの『天然有機酸』や『ビタミンB群・アミノ酸』が爆発的に増加します。11月〜12月の寒さで血行が悪くなり、暖房乾燥で角層がゴワついた冬枯れ肌に対して、角質を摩擦レスで柔軟にしながら深部まで水分を行き渡らせ、内側から発光するようなみずみずしい透明感（水光ツヤ）を取り戻す効果があります。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">昆布（海藻）のコンブチャとは違うのですか？肌につけても紅茶の香りがしますか？</div>
        <div class="faq-a">名前に『コンブ』と入っているため海藻の昆布茶と混同されやすいですが、コスメで使われるコンブチャは100%『発酵紅茶（または発酵茶葉）』のエキスです。海藻臭さは一切なく、多くのアイテムでは上質で気品あるアールグレイやシトラスティーの心地よい香りが漂います。スキンケアのたびに心地よいティーアロマでリフレッシュでき、真冬のストレスから解放されるリラクゼーション効果も抜群です。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">発酵コスメ特有の刺激や、肌に合わない心配はありませんか？</div>
        <div class="faq-a">コンブチャは微生物による自然発酵によって成分が細かく分解されているため、分子が小さく肌への親和性が極めて高いのが特徴です。また弱酸性に保たれているため、冬の寒冷や暖房乾燥でアルカリ性に傾きがちな敏感肌のpHバランスを健康な弱酸性へと整える効果があります。アルコールやパラベンを排除した低刺激処方のアイテムが多く、冬のデリケートな肌でも安心してお使いいただけますが、重度の酵母アレルギーをお持ちの方は事前にパッチテストを行うことを推奨します。</div>
      </div>
      <div class="faq-item">
        <div class="faq-q">11月〜12月のスキンケアで、コンブチャコスメを取り入れる最もおすすめのステップは？</div>
        <div class="faq-a">最も即効性を実感できるのは『洗顔直後の化粧水（トナー）または導入エッセンス』としての活用です。寒さで硬化した角質層にコンブチャの発酵エキスが浸透することで、硬直した細胞がスーッとほぐれ、肌が水分をごくごく飲み込む満水スポンジ状態になります。さらに日中にエアコン暖房で乾燥を感じた時は、エリシャコイのような『コンブチャミスト』をメイクの上から吹きかけると、夕方の乾燥くすみと粉吹き崩れを完全に防ぐことができます。</div>
      </div>
    </section>

    <section class="related-links">
      <h3>🔗 あわせて読みたい！冬の高保湿スキンケア特集</h3>
      <div class="related-grid">
        <a href="/winter-tamanu-oil" class="related-card">🌿 高保湿タマヌオイルコスメ10選</a>
        <a href="/winter-baobab-oil" class="related-card">🌳 高保湿バオバブオイルコスメ10選</a>
        <a href="/winter-galactomyces" class="related-card">🍶 高保湿ガラクトミセス発酵コスメ10選</a>
        <a href="/winter-bifida" class="related-card">🔬 高濃度ビフィズス菌発酵コスメ10選</a>
        <a href="/winter-sake-kasu" class="related-card">🍶 高保湿酒粕コスメ10選</a>
        <a href="/winter-face-mist" class="related-card">💦 冬の高保湿フェイスミスト10選</a>
        <a href="/winter-calendula" class="related-card">🌼 高保湿カレンデュラコスメ10選</a>
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

with open("winter-kombucha.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved winter-kombucha.html successfully!")
